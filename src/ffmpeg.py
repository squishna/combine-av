import subprocess
import sys
import os

def merge_av(video_path, audio_path, output_path):
    """Merges video and audio using FFmpeg."""
    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        sys.exit(1)
    if not os.path.exists(audio_path):
        print(f"Error: Audio file not found: {audio_path}")
        sys.exit(1)

    print(f"Merging {video_path} and {audio_path} into {output_path}...")

    # -c:v copy: Copies the video stream without re-encoding (fast)
    # -c:a aac: Re-encodes audio to AAC for better compatibility in MP4/MKV
    # -shortest: Finish encoding when the shortest input stream ends
    command = [
        "ffmpeg",
        "-y", # Overwrite output file if it exists
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-strict", "experimental",
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"\nSuccess! Merged file saved to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"\nError during merging: {e}")
        sys.exit(1)
