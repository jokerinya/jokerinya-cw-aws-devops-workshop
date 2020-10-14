from flask import Flask, render_template, request

app = Flask(__name__)

def convert(milisecond):
    hour_in_milisecond = 60*60*1000
    hours = milisecond // hour_in_milisecond
    milisecond_left = milisecond % hour_in_milisecond

    minute_in_milisecond = 60*1000
    minutes = milisecond_left // minute_in_milisecond
    milisecond_left %= minute_in_milisecond

    seconds = milisecond_left // 1000 

    return f"{hours} hour/s "*(hours!=0) + f"{minutes} minute/s "*(minutes!=0)  + f"{seconds} second/s "*(seconds!=0) or f"just {milisecond} milisecond/s"

@app.route("/", methods=["GET"])
def main_get():
    return render_template("index.html", developer_name="Jokerinya", not_valid=False)

@app.route("/", methods=["POST"])
def main_post():
    alpha = request.form['number']
    if not alpha.isdecimal():
        return render_template("index.html", developer_name="Jokerinya", not_valid=True)
    if not (0 < int(alpha)):
        return render_template("index.html", developer_name="Jokerinya", not_valid=True)
    return render_template("result.html", developer_name="Jokerinya", milliseconds=int(alpha), result=convert(int(alpha)))



if __name__ == "__main__":
#     app.run(debug=True)
    app.run(host="0.0.0.0", port=80)
