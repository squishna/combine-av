from src.utils import check_ffmpeg
from src.ffmpeg import merge_av
from src.cli import parse_args

def main():
    args = parse_args()
    check_ffmpeg()
    merge_av(args.video, args.audio, args.output)

if __name__ == "__main__":
    main()
