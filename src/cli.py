import argparse

def parse_args():
    """Parses command line arguments using subcommands."""
    parser = argparse.ArgumentParser(
        prog="combine",
        description="A fast CLI tool to merge video and audio files, batch process directories, and more."
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Merge Subcommand
    merge_parser = subparsers.add_parser("merge", help="Merge video and multiple audio files.")
    merge_parser.add_argument("-v", "--video", required=True, help="Path to the input video file.")
    merge_parser.add_argument("-a", "--audio", required=True, nargs='+', help="Path(s) to the input audio file(s). Supports multiple files.")
    merge_parser.add_argument("-o", "--output", required=True, help="Path for the output merged file.")
    merge_parser.add_argument("-s", "--subtitle", help="Path to an optional subtitle file.")
    merge_parser.add_argument("-f", "--format", help="Force output format (e.g., mp4, mkv).")
    merge_parser.add_argument("-q", "--quality", choices=["fast", "high"], default="fast", 
                              help="Quality preset: 'fast' copies video, 'high' re-encodes.")
    merge_parser.add_argument("--scale", choices=["1080p", "720p", "480p", "360p"], 
                              help="Scale the video to a specific resolution.")
    merge_parser.add_argument("--volume", type=float, default=1.0, help="Adjust audio volume.")
    merge_parser.add_argument("--audio-start", type=float, default=0.0, help="Start time for audio in seconds.")
    
    # Advanced Filters
    merge_parser.add_argument("--rotate", choices=["90", "180", "270"], help="Rotate video clockwise.")
    merge_parser.add_argument("--crop", help="Crop video (format: w:h:x:y).")
    merge_parser.add_argument("--speed", type=float, default=1.0, help="Change playback speed (e.g., 2.0 for 2x).")
    
    # HW Accel
    merge_parser.add_argument("--hwaccel", choices=["nvenc", "vaapi", "videotoolbox"], 
                              help="Enable hardware acceleration for re-encoding.")

    # Batch Subcommand
    batch_parser = subparsers.add_parser("batch", help="Batch process video and audio files in a directory.")
    batch_parser.add_argument("-d", "--dir", required=True, help="Directory containing video and audio files.")
    batch_parser.add_argument("-o", "--output-dir", required=True, help="Directory to save merged files.")
    batch_parser.add_argument("-q", "--quality", choices=["fast", "high"], default="fast", help="Quality preset.")
    batch_parser.add_argument("--scale", choices=["1080p", "720p", "480p", "360p"], help="Scale resolution.")
    batch_parser.add_argument("--volume", type=float, default=1.0, help="Adjust audio volume.")
    batch_parser.add_argument("--hwaccel", choices=["nvenc", "vaapi", "videotoolbox"], help="Enable HW accel.")

    # Concat Subcommand
    concat_parser = subparsers.add_parser("concat", help="Concatenate multiple video files into one.")
    concat_parser.add_argument("-i", "--inputs", required=True, nargs='+', help="List of video files to join.")
    concat_parser.add_argument("-o", "--output", required=True, help="Output joined video file.")

    # Extract Subcommand
    extract_parser = subparsers.add_parser("extract", help="Extract audio or subtitles from a media file.")
    extract_parser.add_argument("-i", "--input", required=True, help="Input media file.")
    extract_parser.add_argument("-o", "--output", help="Output file path.")
    group = extract_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--audio", action="store_true", help="Extract the audio track.")
    group.add_argument("--subs", action="store_true", help="Extract the subtitle track.")

    # Info Subcommand
    info_parser = subparsers.add_parser("info", help="Display metadata for a media file.")
    info_parser.add_argument("-i", "--input", required=True, help="File to inspect.")

    # Update Subcommand
    subparsers.add_parser("update", help="Update the tool from the GitHub repository.")

    return parser.parse_args()
