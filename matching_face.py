import cv2
import face_recognition
import os
import numpy as np
import time


def match_face():
    known_faces = []
    face_names = []
    face_file = "known_faces"

    # This gets the face file from known_faces and loads the data into 
    for filename in os.listdir(face_file):
        filepath = os.path.join(face_file, filename) # Gets the file path for a face
        face_encoding = np.load(filepath) # Loads that face encoding into a variable
        known_faces.append(face_encoding) # Adds the face encoding to the list of known faces
        face_names.append(os.path.splitext(filename)[0]) # Takes the name of the face file to be listed as the name of the face

    capture = cv2.VideoCapture(0)
    timer = time.time()

    while(True):

        ret, frame = capture.read()

        if not ret:
            break

        # Setting a time limit for your face to be scanned
        if time.time() - timer > 7:
            print("Time limit reached. Exiting...")
            break

        #Makes the frame smaller so that there it's faster at finding the face location
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        # Iterates through both face_encodings and face_locations at the same time so the values are in pairs
        for face_encoding, face_location in zip(face_encodings, face_locations):
            
            # Sets the default name to "Unknown" so if you aren't recognized you'll be named unknown
            name = "Unknown"

            # Uses face_recognition to compare the known_faces to the current face encoding to check for a match
            matches = face_recognition.compare_faces(known_faces, face_encoding)

            # Goes through matches find the index of the first true for faces matching
            # Then goes into the same index of face_name and finds the name to match to the face
            if True in matches:
                match_index = matches.index(True)
                name = face_names[match_index]

                capture.release()
                cv2.destroyAllWindows()

                return True, name

        # If backup way to exit the code
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
    return False, name