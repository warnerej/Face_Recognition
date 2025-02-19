import cv2
import face_recognition
import os
import numpy as np

def scan_face(name):
    # Name of file for faces to be stored
    face_file = "known_faces"

    #Opens the default camera
    capture = cv2.VideoCapture(0)

    while(True):

        # Reads a frame from camera and returns if it worked and the fram
        ret, frame = capture.read()

        # Checks if you were able to read from the camera
        if not ret:
            break

        # Gives the popup window a name and displays the frame captured
        cv2.imshow("Face Scanner", frame)

        # Waits for s to be pressed to get a face encodings of each face in the current frame
        if cv2.waitKey(1) & 0xFF == ord('s'):
            face_encodings = face_recognition.face_encodings(frame)

            # Checks to see if a face was read and then saves that data to a known_faces file
            if face_encodings:
                np.save(os.path.join(face_file, f"{name}.npy"), face_encodings[0])
                break
            else:
                print("No face was detected, try again")

    capture.release()
    cv2.destroyAllWindows()