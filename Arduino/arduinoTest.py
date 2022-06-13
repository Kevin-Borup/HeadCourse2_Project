import serial

ArduinoSerial = serial.Serial('COM3', 9600, timeout=0.1)

gateDegrees = ""

keepRunning = True
while(keepRunning):
    userInput = input("Enter gate degrees or 'end': ")

    if (userInput == "end"):
        break

    result = '{0}'.format(userInput)
    print(result.encode('utf-8'))
    ArduinoSerial.write(result.encode('utf-8'))
    print(ArduinoSerial.read())

