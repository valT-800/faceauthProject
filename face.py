import cv2
import pickle
from repository.Repository import detect_late_workers


def detect_faces(company):
    face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
    eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('cascades/haarcascade_smile.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")

    labels = {}
    with open("labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    cap = cv2.VideoCapture(0)

    while(True):

    # Take each frame
        _, frame = cap.read()
    # Fliping the frame
        frame_flip = cv2.flip(frame, 1)
    # Converting the input frame to grayscale
        gray = cv2.cvtColor(frame_flip, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame_flip[y:y+h, x:x+w]

            id_, conf = recognizer.predict(roi_gray)
            if conf>=45 and conf<= 85:

                font = cv2.FONT_HERSHEY_SIMPLEX
                name_id = labels[id_]


                if(id_>=0):

                    #detect the worker
                    worker = company.get_worker(name_id)
                    name = worker.first_name

                    #write time and person to file
                    if not worker.checked:
                        detect_late_workers(worker)
                        worker.checked = not worker.checked

                    color = (255, 255, 255)
                    stroke = 2
                    cv2.putText(frame_flip, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)


            img_item = 'image.png'
            cv2.imwrite(img_item, roi_gray)

            color = (0, 255, 0)
            stroke = 3
            end_cord_x = x+w
            end_cord_y = y+h
            cv2.rectangle(frame_flip, (x, y), (end_cord_x, end_cord_y), color, stroke)

        cv2.imshow('frame', frame_flip)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
         break

    cap.release()
    cv2.destroyAllWindows()