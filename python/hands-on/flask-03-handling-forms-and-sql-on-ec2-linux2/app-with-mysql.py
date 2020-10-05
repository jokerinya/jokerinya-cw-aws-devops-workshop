from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)


app.config['MYSQL_DATABASE_HOST'] = 'RDS ENDPOINT OR localhost'
app.config['MYSQL_DATABASE_USER'] = 'admin  or root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'xxxxxPASSWORDxxxxxx'
app.config['MYSQL_DATABASE_DB'] = 'clarusway'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

# execute the code only ONCE
drop_table="""
DROP TABLE IF EXISTS users;
"""
users_table="""
CREATE TABLE users (
  username varchar(50) NOT NULL,
  email varchar(50),
  PRIMARY KEY (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""
data="""
INSERT INTO users
VALUES
    ("Buddy Rich", "buddy@clarusway.com" ),
    ("Candido", "candido@clarusway.com"),
	("Charlie Byrd", "charlie.byrd@clarusway.com");
"""

cursor.execute(drop_table)
cursor.execute(users_table)
cursor.execute(data)
# cursor.close()
# connection.close()

# until here..


def find_emails(keyword):
    query=f"""
    SELECT * FROM users WHERE username like '%{keyword}%'
    """
    cursor.execute(query)
    result = cursor.fetchall()
    user_emails = [(row[0], row[1]) for row in result]
    if not any(user_emails):
        user_emails = [("Not Found", "Not Found")]
    return user_emails

# Write a function named `insert_email` which adds new email to users table the db.

def insert_email(name, email):
    query = f"""
    SELECT * FROM users WHERE username LIKE '{name}';
    """
    cursor.execute(query)
    result = cursor.fetchall()
    if name == None or email == None:
        response = "User name or Email cannot be empty"
    elif not any(result):
        insert = f"""
        INSERT INTO users VALUES ('{name}', '{email}');
        """
        result = cursor.execute(insert)
        response = f"User {name} added successfully."
    else:
        response = f"User {name} already exists."
    return response


@app.route("/", methods = ["GET", "POST"])
def emails():
    if request.method == "POST":
        user_name = request.form["username"]
        user_emails = find_emails(user_name)
        return render_template("emails.html", name_emails = user_emails , keyword = user_name, show_result = True)
    else:
        return render_template("emails.html", show_result = False)

@app.route("/add", methods = ["GET", "POST"])
def add_email():
    if request.method == "POST":
        user_name = request.form["username"]
        user_email = request.form["useremail"]
        result = insert_email(user_name, user_email)
        return render_template("add-email.html", result = result, show_result = True)
    else:
        return render_template("add-email.html", show_result = False)



if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=80)