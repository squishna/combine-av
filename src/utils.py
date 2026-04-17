import subprocess
import sys
import os

def check_ffmpeg():
    """Checks if FFmpeg is installed and accessible."""
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: FFmpeg is not installed or not found in your PATH.")
        sys.exit(1)

def batch_process(dir_path, output_dir, quality="fast", scale=None, volume=1.0, hwaccel=None):
    """Batch process with scale, volume, and HW accel support."""
    if not os.path.isdir(dir_path):
        print(f"Error: Directory not found: {dir_path}")
        return

    os.makedirs(output_dir, exist_ok=True)
    
    video_exts = {'.mp4', '.mkv', '.mov', '.avi'}
    audio_exts = {'.mp3', '.wav', '.aac', '.m4a'}
    
    files = os.listdir(dir_path)
    videos = [f for f in files if os.path.splitext(f)[1].lower() in video_exts]
    
    from src.ffmpeg import merge_av
    
    for v_file in videos:
        base_name = os.path.splitext(v_file)[0]
        v_path = os.path.join(dir_path, v_file)
        
        a_file = None
        for ext in audio_exts:
            potential_a = f"{base_name}{ext}"
            if potential_a in files:
                a_file = potential_a
                break
        
        if a_file:
            a_path = os.path.join(dir_path, a_file)
            out_path = os.path.join(output_dir, f"{base_name}_merged.mp4")
            # Batch currently only supports single audio per video
            merge_av(v_path, [a_path], out_path, quality=quality, scale=scale, volume=volume, hwaccel=hwaccel)
        else:
            print(f"Skipping {v_file}: No matching audio file found.")

def self_update():
    """Fetches the latest install.sh and runs it."""
    print("Self-updating from GitHub...")
    url = "https://raw.githubusercontent.com/squishna/combine-av/main/install.sh"
    try:
        subprocess.run(f"curl -sSL {url} | bash", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during self-update: {e}")
        sys.exit(1)
