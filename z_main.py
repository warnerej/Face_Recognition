import scanning_face as sf
import matching_face as mf
import os

directory = "known_faces"

if not os.path.exists(directory):
    os.makedirs(directory)

user_status = int(input("Are you a new user (1) or an existing user (2): "))

user_name = input("Enter your name: ")

if (user_status == 1):
    print("Line your face up in the center of the camera and click s when you are ready")
    sf.scan_face(user_name)
    print("You are now in our system!")
elif (user_status == 2):
    verification = mf.match_face()

    if (verification[0]):

        if (verification[1].upper() == user_name.upper()):
            print(f"We have your face in our system: {verification[1]}")

        else:
            print(f"We have your face in our system but that is the wrong name")
    else:
        print("You aren't in our systems")
