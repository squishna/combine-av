import argparse

def parse_args():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="A fast CLI tool to merge video and audio files.")
    parser.add_argument("-v", "--video", required=True, help="Path to the input video file.")
    parser.add_argument("-a", "--audio", required=True, help="Path to the input audio file.")
    parser.add_argument("-o", "--output", required=True, help="Path for the output merged file.")
    return parser.parse_args()
