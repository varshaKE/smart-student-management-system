import cv2
import numpy as np
from keras.models import load_model

# Load the pre-trained model globally once to avoid graph errors
model = load_model('cyber_bul.h5')

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Prediction function
def predict_face(face_img):
    # Preprocess the face image
    face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    face_img = cv2.resize(face_img, (48, 48))  # Ensure this size matches your model
    face_img = face_img.astype('float32') / 255.0
    face_img = np.expand_dims(face_img, axis=0)  # Add batch dimension
    face_img = np.expand_dims(face_img, axis=-1)  # Add channel dimension (for grayscale)

    # Predict the class
    prediction = model.predict(face_img)
    print(f"Prediction: {prediction}")  # Debugging raw output
    predicted_class = np.argmax(prediction, axis=1)[0]
    return predicted_class

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # Debugging: print the number of faces detected
    print(f"Faces detected: {len(faces)}")

    for (x, y, w, h) in faces:
        # Crop the face region
        face_roi = frame[y:y + h, x:x + w]

        # Predict the class of the face
        predicted_class = predict_face(face_roi)

        # Draw rectangle around the face and display predicted class
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'Class: {predicted_class}', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Show the frame
    cv2.imshow('Face Detection & Prediction', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
