command = ""
car_started = False  # This variable keeps track of the car's state

while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("Car is already started!")
        else:
            car_started = True
            print("Car started")
    elif command == "stop":
        if not car_started:
            print("Car is already stopped!")
        else:
            car_started = False
            print("Car stopped")
    elif command == "help":
        print("""
Start - to start the car
Stop - to stop the car
Quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand")
