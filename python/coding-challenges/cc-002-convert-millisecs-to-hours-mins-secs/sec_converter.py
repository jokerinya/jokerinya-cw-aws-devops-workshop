print('''###  This program converts milliseconds into hours, minutes, and seconds ###
(To exit the program, please type "exit")''')
while True:
    ms = input('''Please enter the milliseconds (should be greater than zero) : ''')
    if ms.lower() == 'exit':
        print("Exiting the program... Good Bye")
        break
    if (ms.isdecimal()) and (int(ms) > 0):
        ms = int(ms)
        if ms < 1000:
            print(f"just {ms} millisecond/s")
            continue
        seconds= int((ms/1000)%60)
        minutes=int((ms/(1000*60))%60)
        hours=int((ms/(1000*60*60))%24)
        times = [hours,minutes,seconds]
        names_of_times = ["hour/s", "minute/s", "second/s"]
        message = ""
        for i in range(3):
            if times[i] != 0:
                message += f"{times[i]} {names_of_times[i]} "
        print(f"{message}")
    else:
        print("Not Valid Input !!!")
        