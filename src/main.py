import sys
from src.utils import check_ffmpeg, self_update, batch_process
from src.ffmpeg import merge_av, get_info
from src.cli import parse_args

def main():
    args = parse_args()
    
    if not args.command:
        print("Error: No command specified. Use --help for usage info.")
        sys.exit(1)

    # Basic system check (only if not updating)
    if args.command != "update":
        check_ffmpeg()

    if args.command == "merge":
        merge_av(args.video, args.audio, args.output, 
                 quality=args.quality, 
                 audio_start=args.audio_start, 
                 fmt=args.format,
                 subtitle_path=args.subtitle)
    
    elif args.command == "batch":
        batch_process(args.dir, args.output_dir, quality=args.quality)
        
    elif args.command == "info":
        get_info(args.input)
        
    elif args.command == "update":
        self_update()

if __name__ == "__main__":
    main()
