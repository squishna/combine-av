import subprocess
import sys
import os
import json

def merge_av(video_path, audio_path, output_path, quality="fast", audio_start=0.0, fmt=None, subtitle_path=None, scale=None, volume=1.0):
    """Merges video, audio, and optional subtitle with scaling and volume support."""
    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        return False
    if not os.path.exists(audio_path):
        print(f"Error: Audio file not found: {audio_path}")
        return False

    print(f"Merging streams into {output_path} (Quality: {quality}, Volume: {volume})...")

    command = ["ffmpeg", "-y"]
    command += ["-i", video_path]
    
    if audio_start > 0:
        command += ["-ss", str(audio_start)]
    command += ["-i", audio_path]
    
    if subtitle_path:
        command += ["-i", subtitle_path]
    
    command += ["-map", "0:v:0", "-map", "1:a:0"]
    if subtitle_path:
        command += ["-map", "2:s:0"]
    
    # Scaling
    scale_map = {"1080p": "1920:1080", "720p": "1280:720", "480p": "854:480", "360p": "640:360"}
    if scale:
        res = scale_map.get(scale)
        command += ["-vf", f"scale={res}:force_original_aspect_ratio=decrease,pad={res}:(ow-iw)/2:(oh-ih)/2"]
        command += ["-c:v", "libx264", "-crf", "18"]
    elif quality == "fast":
        command += ["-c:v", "copy"]
    else:
        command += ["-c:v", "libx264", "-crf", "18"]
        
    # Audio Volume filter (requires re-encoding)
    if volume != 1.0:
        command += ["-af", f"volume={volume}"]
        command += ["-c:a", "aac"]
    else:
        command += ["-c:a", "aac", "-strict", "experimental"]
    
    if subtitle_path:
        command += ["-c:s", "mov_text" if output_path.endswith(".mp4") else "copy"]
    
    command += ["-shortest"]
    if fmt:
        command += ["-f", fmt]
    command.append(output_path)

    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        print(f"Success! Merged file saved to: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during merging: {e.stderr.decode()}")
        return False

def extract_media(input_path, extract_type, output_path=None):
    """Extracts audio or subtitles from a media file."""
    if not os.path.exists(input_path):
        print(f"Error: Input file not found: {input_path}")
        return

    base, _ = os.path.splitext(input_path)
    if extract_type == "audio":
        output_path = output_path or f"{base}_extracted.mp3"
        command = ["ffmpeg", "-y", "-i", input_path, "-vn", "-acodec", "libmp3lame", output_path]
    else: # subs
        output_path = output_path or f"{base}_extracted.srt"
        command = ["ffmpeg", "-y", "-i", input_path, "-map", "0:s:0", "-c:s", "text", output_path]

    print(f"Extracting {extract_type} from {input_path} to {output_path}...")
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        print(f"Success! Extracted file saved to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during extraction: {e.stderr.decode()}")

def get_info(file_path):
    """Retrieves metadata using ffprobe."""
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    command = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", file_path]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        fmt = data.get("format", {})
        streams = data.get("streams", [])
        print(f"\nMetadata for: {file_path}")
        print(f"  Container: {fmt.get('format_name', 'N/A')}")
        print(f"  Duration:  {float(fmt.get('duration', 0)):.2f}s")
        print(f"  Size:      {int(fmt.get('size', 0)) / (1024*1024):.2f} MB")
        for i, s in enumerate(streams):
            codec = s.get("codec_name", "N/A")
            type = s.get("codec_type", "N/A")
            print(f"  Stream #{i}: {type} ({codec})")
            if type == "video":
                print(f"    Resolution: {s.get('width')}x{s.get('height')}")
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"Error retrieving info: {e}")
