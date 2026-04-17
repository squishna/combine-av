import subprocess
import sys
import os
import json

def merge_av(video_path, audio_path, output_path, quality="fast", audio_start=0.0, fmt=None, subtitle_path=None):
    """Merges video, audio, and optional subtitle with advanced features."""
    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        return False
    if not os.path.exists(audio_path):
        print(f"Error: Audio file not found: {audio_path}")
        return False
    if subtitle_path and not os.path.exists(subtitle_path):
        print(f"Error: Subtitle file not found: {subtitle_path}")
        return False

    print(f"Merging streams into {output_path} (Quality: {quality})...")

    # Command builder
    command = ["ffmpeg", "-y"]
    
    # Video input
    command += ["-i", video_path]
    
    # Audio input with potential trimming/offsetting
    if audio_start > 0:
        command += ["-ss", str(audio_start)]
    command += ["-i", audio_path]
    
    # Optional subtitle input
    if subtitle_path:
        command += ["-i", subtitle_path]
    
    # Mapping streams
    command += ["-map", "0:v:0", "-map", "1:a:0"]
    if subtitle_path:
        command += ["-map", "2:s:0"]
    
    # Video codec: 'fast' = copy, 'high' = re-encode libx264
    if quality == "fast":
        command += ["-c:v", "copy"]
    else:
        command += ["-c:v", "libx264", "-crf", "18"]
        
    # Audio codec
    command += ["-c:a", "aac", "-strict", "experimental"]
    
    # Subtitle codec: copy for mkv/mp4
    if subtitle_path:
        command += ["-c:s", "mov_text" if output_path.endswith(".mp4") else "copy"]
    
    # Finish when shortest stream ends
    command += ["-shortest"]
    
    # Force output format if specified
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

def get_info(file_path):
    """Retrieves metadata using ffprobe."""
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    command = [
        "ffprobe", 
        "-v", "quiet", 
        "-print_format", "json", 
        "-show_format", 
        "-show_streams", 
        file_path
    ]
    
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
