import ffmpeg
import whisper
import os
from datetime import timedelta


def extract_audio(video_path, audio_path):
    """
    Extracts the audio from the given video file and saves it as a .wav file.
    """
    ffmpeg.input(video_path).output(audio_path, ac=1, ar=16000).run(overwrite_output=True)


def format_timestamp(seconds):
    """
    Converts seconds to SRT timestamp format.
    """
    td = timedelta(seconds=seconds)
    return str(td)[:-3].replace('.', ',')


def generate_srt(transcriptions, output_path):
    """
    Converts Whisper transcriptions into an SRT file.
    """
    with open(output_path, 'w', encoding='utf-8') as srt_file:
        for idx, segment in enumerate(transcriptions):
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            text = segment['text'].strip()
            srt_file.write(f"{idx + 1}\n{start} --> {end}\n{text}\n\n")


def video_to_srt(video_path, output_srt_path):
    """
    Main function to convert video to SRT file.
    """
    # Paths for intermediate audio file
    audio_path = "temp_audio.wav"

    # Extract audio from the video
    print("Extracting audio...")
    extract_audio(video_path, audio_path)

    # Load Whisper model
    print("Loading Whisper model...")
    model = whisper.load_model("base")

    # Perform speech-to-text
    print("Transcribing audio...")
    result = model.transcribe(audio_path)

    # Generate SRT file
    print("Generating SRT file...")
    generate_srt(result['segments'], output_srt_path)

    # Clean up temporary audio file
    os.remove(audio_path)
    print(f"SRT file saved at {output_srt_path}")


if __name__ == "__main__":
    # Input video path
    input_video = r"C:\path\to\your\video.mp4"
    video_dir = os.path.dirname(input_video)
    video_base_name = os.path.splitext(os.path.basename(input_video))[0]

    # Generate output SRT path in the same folder with the same name as the video
    output_srt = os.path.join(video_dir, f"{video_base_name}.srt")

    # Convert video to SRT
    video_to_srt(input_video, output_srt)
