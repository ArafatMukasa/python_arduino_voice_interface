#!/usr/bin/env python


import serial
import sys
import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def listen_to_user():
    # create recognizer and mic instances
    input_command = ""

    #To continously listen to the user, change the statement below from "if input_command != 'exit':"
    #to "if input_command != 'exit':"
    
    if input_command != 'exit': 
        print('Speak now...')
        output = recognize_speech_from_mic(recognizer, microphone)
        if output["transcription"]:
            # show the user the transcription
            print("You said: {}".format(output["transcription"]))
            input_command = output["transcription"]
        if not output["success"]:
            print("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
        if output["error"]:
            print("ERROR: {}".format(output["error"]))



def send_data():
    #The data is sent to arduino. But before its sent, we first setup serial communication between python and arduino. 
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
        print ("Serial port has been setup successfully at port /dev/ttyACM0")

    except:
        print ("Unable to open serial port")


    #To blink the led connected to pin 13 continously, change the statement below from "if True to while True"
    
    if True:
        try:
            data = ser.write(b'2') 
        
            print ("I have sent character of 2 to Arduino")

        except:
            print ("Unable to send data to Arduino")
            sys.exit(0)



recognizer = sr.Recognizer()
microphone = sr.Microphone()

recognize_speech_from_mic(recognizer, microphone)

listen_to_user()

print ("Finished listening to user")

send_data()



    
        

    