import streamlit as st
import cv2
import os
import mediapipe as mp
import numpy as np

# Set environment variable for Mac camera permissions
os.environ["OPENCV_AVFOUNDATION_SKIP_AUTH"] = "1"

def calculate_finger_positions(landmarks):
    # Get palm and finger positions
    palm_base = np.array([landmarks[0].y])  # Wrist point
    
    # Get fingertip positions relative to their bases
    fingertips_y = np.array([
        landmarks[8].y,   # index tip
        landmarks[12].y,  # middle tip
        landmarks[16].y,  # ring tip
        landmarks[20].y   # pinky tip
    ])
    
    # Get finger base positions
    finger_bases_y = np.array([
        landmarks[5].y,   # index base
        landmarks[9].y,   # middle base
        landmarks[13].y,  # ring base
        landmarks[17].y   # pinky base
    ])
    
    # Calculate if fingers are extended (comparing with their base position)
    fingers_extended = fingertips_y < finger_bases_y
    
    # Check thumb position (tucked in or not)
    thumb_tip_x = landmarks[4].x
    palm_x = landmarks[0].x
    thumb_tucked = thumb_tip_x > palm_x  # True if thumb is tucked in
    
    return fingers_extended, thumb_tucked

def recognize_letter(landmarks):
    if not landmarks:
        return None
    
    fingers_extended, thumb_tucked = calculate_finger_positions(landmarks.landmark)
    
    # A: Fist (all fingers down)
    if not any(fingers_extended):
        return 'A'
    
    # B: All fingers up, thumb tucked
    elif (all(fingers_extended) and thumb_tucked):
        return 'B'
    
    # C: Curved fingers (partially extended)
    elif (all(fingers_extended) and 
          landmarks.landmark[8].x - landmarks.landmark[4].x < 0.1):  # Fingers curved inward
        return 'C'
    
    return None

def main():
    st.title("ASL Fingerspelling Practice")
    
    # Add sidebar info
    st.sidebar.header("Hand Detection Status")
    status_placeholder = st.sidebar.empty()
    
    # Initialize current letter in session state
    if 'current_letter' not in st.session_state:
        st.session_state.current_letter = 'A'
    
    # Add letter selection
    col1, col2 = st.columns([3,1])
    with col1:
        letter_display = st.empty()
        letter_display.header(f"Try signing: {st.session_state.current_letter}")
    with col2:
        if st.button("Next Letter"):
            # Cycle through letters
            st.session_state.current_letter = (
                "B" if st.session_state.current_letter == "A" 
                else "C" if st.session_state.current_letter == "B" 
                else "A"
            )
            letter_display.header(f"Try signing: {st.session_state.current_letter}")
    
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
            
            # Update status
            if results.multi_hand_landmarks:
                status_placeholder.success("Hand Detected")
                hand_landmarks = results.multi_hand_landmarks[0]
                
                # Draw landmarks
                mp_drawing.draw_landmarks(
                    frame_rgb,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )
                
                # Recognize letter
                detected_letter = recognize_letter(hand_landmarks)
                if detected_letter:
                    if detected_letter == st.session_state.current_letter:
                        status_placeholder.success(f"Correct! Letter {detected_letter}")
                    else:
                        status_placeholder.info(f"Detected: {detected_letter}")
            else:
                status_placeholder.warning("No Hand Detected")
            
            # Display the frame
            frame_placeholder.image(frame_rgb)
    
    # Release resources
    hands.close()
    cap.release()

if __name__ == "__main__":
    main()