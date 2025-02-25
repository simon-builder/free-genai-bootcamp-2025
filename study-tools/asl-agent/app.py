import streamlit as st
import cv2
import os
import mediapipe as mp

# Set environment variable for Mac camera permissions
os.environ["OPENCV_AVFOUNDATION_SKIP_AUTH"] = "1"

def main():
    st.title("ASL Fingerspelling Practice")
    
    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5
    )
    
    # Add webcam capture
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        st.error("Could not access webcam. Please check permissions.")
        return
    
    # Create a placeholder for webcam feed
    frame_placeholder = st.empty()
    
    # Add a stop button
    stop_button = st.button("Stop")
    
    while not stop_button:
        ret, frame = cap.read()
        if ret:
            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Process the frame and detect hands
            results = hands.process(frame_rgb)
            
            # Draw hand landmarks if detected
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame_rgb,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS
                    )
            
            # Display the frame
            frame_placeholder.image(frame_rgb)
    
    # Release resources
    hands.close()
    cap.release()

if __name__ == "__main__":
    main()