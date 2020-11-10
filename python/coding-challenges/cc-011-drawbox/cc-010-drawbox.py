while True:
    try:
        a = int(input("Enter decimal number: ").strip())
        if a==1:
            print(a*"#")
        else:
            print(a*"# ")
            for _ in range(a-2):
                print("# "+ "  "*(a-2)+"#")
            print(a*"# ")
        break
    except:
        print("Invalid entry")