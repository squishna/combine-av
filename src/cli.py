import argparse

def parse_args():
    """Parses command line arguments using subcommands."""
    parser = argparse.ArgumentParser(
        prog="combine",
        description="A fast CLI tool to merge video and audio files, batch process directories, and more."
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Merge Subcommand
    merge_parser = subparsers.add_parser("merge", help="Merge a single video and audio file.")
    merge_parser.add_argument("-v", "--video", required=True, help="Path to the input video file.")
    merge_parser.add_argument("-a", "--audio", required=True, help="Path to the input audio file.")
    merge_parser.add_argument("-o", "--output", required=True, help="Path for the output merged file.")
    merge_parser.add_argument("-s", "--subtitle", help="Path to an optional subtitle file (e.g., .srt, .ass).")
    merge_parser.add_argument("-f", "--format", help="Force output format (e.g., mp4, mkv).")
    merge_parser.add_argument("-q", "--quality", choices=["fast", "high"], default="fast", 
                              help="Quality preset: 'fast' copies video (no re-encoding), 'high' re-encodes (better for some players).")
    merge_parser.add_argument("--audio-start", type=float, default=0.0, 
                              help="Start time for audio in seconds (trims/offsets audio).")

    # Batch Subcommand
    batch_parser = subparsers.add_parser("batch", help="Batch process video and audio files in a directory.")
    batch_parser.add_argument("-d", "--dir", required=True, help="Directory containing video and audio files.")
    batch_parser.add_argument("-o", "--output-dir", required=True, help="Directory to save merged files.")
    batch_parser.add_argument("-q", "--quality", choices=["fast", "high"], default="fast", help="Quality preset.")

    # Info Subcommand
    info_parser = subparsers.add_parser("info", help="Display metadata for a media file.")
    info_parser.add_argument("-i", "--input", required=True, help="File to inspect.")

    # Update Subcommand
    subparsers.add_parser("update", help="Update the tool from the GitHub repository.")

    return parser.parse_args()
