command = ""
while command != "quit":
    command = input(">  ").lower()
    if command == 'start':
        print("CAR HAS STARTED")
    elif command == 'stop':
        print("CAR HAS STOPPED")
    elif command == "help":
        print("""
start - start the car
stop  - stop the car
quit -  to quit""")
    elif command == "quit":
        break
    else:
        print(" sorry i don't understand ")
