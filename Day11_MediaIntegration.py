import streamlit as st
# PIL :  Library for manipulating images. 
# You can resize, crop, and even apply filters to enhance the images before displaying them in your app.
from PIL import Image

################## Image ##################    

# Load an image
image = Image.open('./files/img/image.png')

# Display the original image
st.subheader('Original Image')
st.image(image, caption='Original Image', use_column_width=True)

# Manipulate the image (e.g., resizing)
resized_image = image.resize((100, 100))

# Display the manipulated image
st.subheader('Resized Image')
st.image(resized_image, caption='Resized Image', use_column_width=True)

############################################

################## Audio ##################    


# import streamlit as st
from pydub import AudioSegment
import tempfile
import shutil

# Display the original audio file
st.subheader("Original Audio File")
st.audio('files/aud/audio.mp3')

# Load the original audio file
audio = AudioSegment.from_file('files/aud/audio.mp3', format="mp3")

# Get the duration of the audio in milliseconds
audio_duration_ms = len(audio)

# Sidebar for trimming settings
st.sidebar.subheader("Trim Settings")
start_trim = st.sidebar.slider(
    "Start Time (ms)", 0, audio_duration_ms - 1, 4000, 1000
)
end_trim = st.sidebar.slider(
    "End Time (ms)", start_trim + 1, audio_duration_ms, 120000, 1000
)

# Validate that start time is less than end time
if start_trim >= end_trim:
    st.error("The end time must be greater than the start time.")
else:
    # Trim the audio
    trimmed_audio = audio[start_trim:end_trim]

    # Save the trimmed audio to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
        temp_file_name = temp_file.name
        trimmed_audio.export(temp_file_name, format='mp3')

    # Optionally, move the file to a final location
    final_file_name = 'files/aud/trimmed_audio.mp3'
    shutil.move(temp_file_name, final_file_name)

    # Display the trimmed audio file
    st.subheader("Trimmed Audio File")
    st.audio(final_file_name)


############################################

################## Video ##################    

import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import shutil
import os

# Display the original video
st.subheader("Original Video")
st.video('files/vid/video.mp4', start_time=10)

# Load the video file with error handling
try:
    video_clip = VideoFileClip('files/vid/video.mp4')
except Exception as error:
    st.error(f"Unable to load the video: {error}")
    st.stop()

# Get the total duration of the video
video_duration_seconds = video_clip.duration

# Sidebar for setting trim points
st.sidebar.subheader("Trim Settings")
start_time = st.sidebar.slider(
    "Start Time (s)", 0.0, video_duration_seconds - 1, 0.0, 1.0
)
end_time = st.sidebar.slider(
    "End Time (s)", start_time + 1.0, video_duration_seconds, video_duration_seconds, 1.0
)

# Ensure the end time is after the start time
if start_time >= end_time:
    st.error("End time must be later than start time.")
else:
    # Trim the video according to user settings
    trimmed_video = video_clip.subclip(start_time, end_time)

    # Save the trimmed video to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
        temp_file_path = temp_file.name
        trimmed_video.write_videofile(temp_file_path, codec='libx264')

    # Move the temporary file to the desired final location
    final_path = 'files/vid/trimmed_video.mp4'
    if os.path.exists(final_path):
        os.remove(final_path)
    shutil.move(temp_file_path, final_path)

    # Display the trimmed video
    st.subheader("Trimmed Video")
    st.video(final_path)

############################################
