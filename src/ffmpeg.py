import subprocess
import sys
import os
import json

def merge_av(video_path, audio_paths, output_path, quality="fast", audio_start=0.0, fmt=None, 
             subtitle_path=None, scale=None, volume=1.0, rotate=None, crop=None, speed=1.0, hwaccel=None):
    """Advanced merge with multi-audio, HW accel, and video filters."""
    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        return False
    
    command = ["ffmpeg", "-y"]
    
    # Input Video
    command += ["-i", video_path]
    
    # Input Audios
    for a_path in audio_paths:
        if audio_start > 0: command += ["-ss", str(audio_start)]
        command += ["-i", a_path]
        
    if subtitle_path:
        command += ["-i", subtitle_path]

    # Mapping: Video from first input, Audios from subsequent inputs
    command += ["-map", "0:v:0"]
    for i in range(1, len(audio_paths) + 1):
        command += ["-map", f"{i}:a:0"]
    if subtitle_path:
        command += ["-map", f"{len(audio_paths) + 1}:s:0"]

    # Filters: Scaling, Rotation, Cropping, Speed
    vf = []
    if scale:
        res = {"1080p": "1920:1080", "720p": "1280:720", "480p": "854:480", "360p": "640:360"}.get(scale)
        vf.append(f"scale={res}:force_original_aspect_ratio=decrease,pad={res}:(ow-iw)/2:(oh-ih)/2")
    if rotate:
        angle = {"90": "transpose=1", "180": "transpose=2,transpose=2", "270": "transpose=2"}.get(rotate)
        vf.append(angle)
    if crop:
        vf.append(f"crop={crop}")
    if speed != 1.0:
        vf.append(f"setpts={1.0/speed}*PTS")
    
    if vf:
        command += ["-vf", ",".join(vf)]
        
    # Audio filters: Volume and Speed
    af = []
    if volume != 1.0: af.append(f"volume={volume}")
    if speed != 1.0: af.append(f"atempo={speed}")
    if af: command += ["-af", ",".join(af)]

    # Encoder settings with HW accel
    re_encode_required = bool(vf or af or quality == "high")
    if re_encode_required:
        if hwaccel == "nvenc": command += ["-c:v", "h264_nvenc"]
        elif hwaccel == "vaapi": command += ["-c:v", "h264_vaapi"]
        elif hwaccel == "videotoolbox": command += ["-c:v", "h264_videotoolbox"]
        else: command += ["-c:v", "libx264", "-crf", "18"]
        command += ["-c:a", "aac"]
    else:
        command += ["-c:v", "copy", "-c:a", "copy"]

    if subtitle_path:
        command += ["-c:s", "mov_text" if output_path.endswith(".mp4") else "copy"]
    
    command += ["-shortest"]
    if fmt: command += ["-f", fmt]
    command.append(output_path)

    print(f"Processing {output_path}...")
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        print(f"Success! Saved to: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")
        return False

def concat_videos(input_paths, output_path):
    """Concatenates multiple video files using the concat demuxer."""
    list_path = "concat_list.txt"
    with open(list_path, "w") as f:
        for p in input_paths:
            f.write(f"file '{os.path.abspath(p)}'\n")
    
    command = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_path, "-c", "copy", output_path]
    print(f"Joining {len(input_paths)} files into {output_path}...")
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        print(f"Success! Joined file saved to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")
    finally:
        if os.path.exists(list_path): os.remove(list_path)

def extract_media(input_path, extract_type, output_path=None):
    """Extracts audio or subtitles."""
    if not os.path.exists(input_path): return
    base, _ = os.path.splitext(input_path)
    if extract_type == "audio":
        output_path = output_path or f"{base}_extracted.mp3"
        command = ["ffmpeg", "-y", "-i", input_path, "-vn", "-acodec", "libmp3lame", output_path]
    else:
        output_path = output_path or f"{base}_extracted.srt"
        command = ["ffmpeg", "-y", "-i", input_path, "-map", "0:s:0", "-c:s", "text", output_path]
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        print(f"Success! Extracted to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")

def get_info(file_path):
    """Retrieves metadata."""
    if not os.path.exists(file_path): return
    command = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", file_path]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        fmt = data.get("format", {})
        streams = data.get("streams", [])
        print(f"\nMetadata for: {file_path}")
        print(f"  Container: {fmt.get('format_name', 'N/A')}")
        print(f"  Duration:  {float(fmt.get('duration', 0)):.2f}s")
        for i, s in enumerate(streams):
            print(f"  Stream #{i}: {s.get('codec_type', 'N/A')} ({s.get('codec_name', 'N/A')})")
    except Exception as e:
        print(f"Error: {e}")
