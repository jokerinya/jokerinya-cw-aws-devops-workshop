vowels = ("a", "e", "i", "o", "u")

def control(el):
    for i in range(len(el)):
        if i+1 == len(el): return False
        if (el[i] in vowels) and (el[i+1] in vowels):
            return True
    return False

entry = ""
while entry != "exit":
    entry = input("Enter your word (For quit type 'exit')").strip().lower()
    if entry == "exit": break

    if entry.isalpha()==False:
        print("Invalid Entry. (Only one word with letters without space)")
        continue

    print("Positive" if control(entry) else "Negative")

