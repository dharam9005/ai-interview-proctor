import cv2

def start_emotion_detection():
    # Load face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not detected!")
        return

    print("Emotion Detection Started... Press Q to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        emotion_text = "Focused / Neutral"

        if len(faces) == 0:
            emotion_text = "No Face Detected (Distracted)"
        elif len(faces) > 1:
            emotion_text = "Multiple Faces (Suspicious)"
        else:
            emotion_text = "Focused / Attentive"

        # Draw rectangle + emotion label
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, emotion_text, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("AI Interview Emotion Monitor", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()