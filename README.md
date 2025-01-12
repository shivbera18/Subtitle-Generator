# Subtitle-Generator
Video-to-SRT Transcription Framework

This repository presents a robust and comprehensive Python-based framework for the efficient conversion of video files into subtitle files in the SRT format, leveraging the advanced capabilities of Whisper, a state-of-the-art tool for speech-to-text transcription developed by OpenAI. This framework is designed to seamlessly integrate cutting-edge technologies to deliver accurate and reliable subtitle generation while maintaining a streamlined and user-friendly workflow.

Core Features

Audio Extraction with FFmpeg: Utilizes FFmpeg to extract high-quality audio from video files, converting it into a mono-channel, 16kHz .wav format optimized for transcription.

Whisper Model Integration: Implements Whisper's pre-trained deep learning models to perform speech recognition with high precision, producing transcriptions that capture nuanced audio content.

Timestamped Subtitles: Outputs well-structured SRT files with precise timestamping to ensure subtitles align perfectly with the source video, enhancing the viewer experience.

Automated File Management: Employs automated mechanisms to manage temporary files, ensuring that intermediary audio files are removed after processing to optimize disk usage and maintain cleanliness.

System Requirements

Prerequisites

To ensure the proper functioning of the framework, the following prerequisites must be met:

Python Version: Requires Python 3.7 or higher to take advantage of the latest features and libraries.

FFmpeg Installation: FFmpeg must be installed and its executable added to the system's PATH. Detailed installation instructions can be found on the FFmpeg website.

Required Python Packages

The framework relies on the following Python libraries, which can be installed using pip:

pip install ffmpeg-python whisper

These dependencies facilitate seamless integration with FFmpeg and Whisper, enabling efficient audio processing and transcription.

Usage Instructions

Follow these steps to utilize the framework for video-to-SRT conversion:

Clone the Repository:

git clone https://github.com/yourusername/video-to-srt.git
cd video-to-srt

Prepare the Input Video:

Place the target video file within the project directory.

Alternatively, provide the absolute file path within the script.

Execute the Script:
Run the script using the following command:

python script_name.py

Replace script_name.py with the actual name of the Python script.

Configure the Input Path:
Edit the input_video variable within the script to specify the full path to your video file:

input_video = r"C:\path\to\your\video.mp4"

Retrieve the Output:
The generated SRT file will be saved in the same directory as the input video, retaining the video's base filename for consistency.

Example Workflow

Input File Location

Suppose your video file is located at:

C:\Users\Shiv\Desktop\AI ML\Machine Learning Specialization\Week 9.mp4

Output File Location

After running the script, the corresponding subtitle file will be generated as:

C:\Users\Shiv\Desktop\AI ML\Machine Learning Specialization\Week 9.srt

This ensures that the subtitles are readily available alongside the video file for immediate use.

Functional Overview

The framework is structured around several modular functions that perform discrete tasks:

extract_audio(video_path, audio_path): Extracts audio from the specified video file and saves it as a .wav file, ensuring compatibility with Whisper's transcription models.

format_timestamp(seconds): Converts time values from seconds into the SRT-standard timestamp format (e.g., 00:01:23,456), ensuring accurate synchronization.

generate_srt(transcriptions, output_path): Transforms Whisper's transcription results into an SRT file, complete with segment indexing, timestamps, and textual content.

video_to_srt(video_path, output_srt_path): Serves as the central function, orchestrating the entire workflow from audio extraction to subtitle generation and temporary file cleanup.

Technical Notes

Whisper Model Selection

By default, the framework employs Whisper's base model to balance accuracy and processing speed. However, users can opt for other models (e.g., small, medium, large) to tailor performance to their specific needs:

Smaller Models: Faster processing times with moderate accuracy, suitable for straightforward audio content.

Larger Models: Enhanced transcription accuracy, particularly for complex or noisy audio, albeit with increased computational requirements.

File Management

To ensure efficient disk usage, the framework automatically deletes temporary audio files once the transcription and subtitle generation processes are complete. This minimizes storage overhead and maintains a clean working environment.

Licensing

This project is distributed under the MIT License, which permits free use, modification, and distribution. Refer to the LICENSE file for the full terms and conditions governing its usage.

Acknowledgments

The development of this framework is made possible by the integration of two powerful tools:

OpenAI Whisper: An advanced automated speech recognition (ASR) system that leverages deep learning to produce high-quality transcriptions.

FFmpeg: A versatile and widely-used multimedia processing utility that plays a pivotal role in audio extraction and manipulation.

By combining these technologies, the framework delivers a robust solution for video-to-SRT conversion, catering to a wide range of applications including educational content, media accessibility, and archival projects.
