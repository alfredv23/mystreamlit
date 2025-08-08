import streamlit as st
import cv2
import time

def main():
    st.title("Optimized Video Stream with Streamlit")

    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return

    # Initialize session state for the stop button
    if "stop" not in st.session_state:
        st.session_state.stop = False

    # Stop button
    if st.button("Stop"):
        st.session_state.stop = True

    # Stream video frames
    stframe = st.empty()
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Error: Could not read frame.")
                break

            # Convert the frame to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the frame in the Streamlit app
            stframe.image(frame, caption="Video Stream", use_column_width=True)

            # Stop the stream if the button is pressed
            if st.session_state.stop:
                break

            # Limit the frame rate
            time.sleep(0.03)
    finally:
        # Release the webcam
        cap.release()

if __name__ == "__main__":
    main()