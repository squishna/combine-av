import argparse

def parse_args():
    """Parses command line arguments using subcommands."""
    parser = argparse.ArgumentParser(
        prog="combine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
Combine-AV: A powerful FFmpeg-based CLI tool to merge, batch, and extract media.
Version: 0.0.1

Common usage:
  combine merge -v video.mp4 -a audio.mp3 -o output.mp4
  combine batch --dir ./raw --output-dir ./merged
  combine concat -i clip1.mp4 clip2.mp4 -o joined.mp4
  combine extract -i movie.mkv --audio
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands", metavar="COMMAND")

    # Merge Subcommand
    merge_parser = subparsers.add_parser("merge", help="Merge video and multiple audio files.")
    merge_parser.add_argument("-v", "--video", required=True, help="Path to the input video file.")
    merge_parser.add_argument("-a", "--audio", required=True, nargs='+', help="Path(s) to the input audio file(s). Supports multiple tracks.")
    merge_parser.add_argument("-o", "--output", required=True, help="Path for the output merged file.")
    merge_parser.add_argument("-s", "--subtitle", help="Path to an optional subtitle file (.srt, .ass, etc.).")
    merge_parser.add_argument("-f", "--format", help="Force output container format (e.g., mp4, mkv, webm).")
    merge_parser.add_argument("-q", "--quality", choices=["fast", "high"], default="fast", 
                              help="Quality preset: 'fast' copies video streams (rapid), 'high' re-encodes (slower, better compatibility).")
    
    # Advanced Filters
    filter_group = merge_parser.add_argument_group("Video/Audio Filters (Forces Re-encoding)")
    filter_group.add_argument("--scale", choices=["1080p", "720p", "480p", "360p"], 
                              help="Scale the video to a specific resolution.")
    filter_group.add_argument("--rotate", choices=["90", "180", "270"], help="Rotate video clockwise by degrees.")
    filter_group.add_argument("--crop", help="Crop video frame (format: width:height:x:offset:y:offset).")
    filter_group.add_argument("--volume", type=float, default=1.0, help="Adjust audio volume (0.5 = 50%, 2.0 = 200%).")
    filter_group.add_argument("--speed", type=float, default=1.0, help="Change playback speed (e.g., 2.0 for double speed).")
    filter_group.add_argument("--audio-start", type=float, default=0.0, help="Start time for audio in seconds (trims/offsets audio).")
    
    # HW Accel
    hw_group = merge_parser.add_argument_group("Performance Options")
    hw_group.add_argument("--hwaccel", choices=["nvenc", "vaapi", "videotoolbox"], 
                              help="Enable GPU hardware acceleration (requires compatible hardware/drivers).")

    # Batch Subcommand
    batch_parser = subparsers.add_parser("batch", help="Batch process video and audio pairs in a directory.")
    batch_parser.add_argument("-d", "--dir", required=True, help="Directory containing video and audio files with matching names.")
    batch_parser.add_argument("-o", "--output-dir", required=True, help="Directory where merged files will be saved.")
    batch_parser.add_argument("-q", "--quality", choices=["fast", "high"], default="fast", help="Quality preset for all files.")
    batch_parser.add_argument("--scale", choices=["1080p", "720p", "480p", "360p"], help="Scale all videos to resolution.")
    batch_parser.add_argument("--volume", type=float, default=1.0, help="Adjust volume for all files.")
    batch_parser.add_argument("--hwaccel", choices=["nvenc", "vaapi", "videotoolbox"], help="Enable GPU acceleration.")

    # Concat Subcommand
    concat_parser = subparsers.add_parser("concat", help="Concatenate (join) multiple video files into one.")
    concat_parser.add_argument("-i", "--inputs", required=True, nargs='+', help="List of video files to join in order.")
    concat_parser.add_argument("-o", "--output", required=True, help="Output path for the joined video file.")

    # Extract Subcommand
    extract_parser = subparsers.add_parser("extract", help="Extract audio or subtitle tracks from a media file.")
    extract_parser.add_argument("-i", "--input", required=True, help="Input media file.")
    extract_parser.add_argument("-o", "--output", help="Optional custom output path.")
    group = extract_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--audio", action="store_true", help="Extract the primary audio track as MP3.")
    group.add_argument("--subs", action="store_true", help="Extract the first subtitle track as SRT.")

    # Info Subcommand
    info_parser = subparsers.add_parser("info", help="Display detailed metadata for a media file.")
    info_parser.add_argument("-i", "--input", required=True, help="Path to the file you want to inspect.")

    # Update Subcommand
    subparsers.add_parser("update", help="Update combine to the latest version from GitHub.")

    return parser.parse_args()
