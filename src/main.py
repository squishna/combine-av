import sys
from src.utils import check_ffmpeg, self_update, batch_process
from src.ffmpeg import merge_av, get_info, extract_media, concat_videos
from src.cli import parse_args

def main():
    args = parse_args()
    
    if not args.command:
        print("Error: No command specified. Use --help for usage info.")
        sys.exit(1)

    if args.command != "update":
        check_ffmpeg()

    if args.command == "merge":
        merge_av(args.video, args.audio, args.output, 
                 quality=args.quality, 
                 audio_start=args.audio_start, 
                 fmt=args.format,
                 subtitle_path=args.subtitle,
                 scale=args.scale,
                 volume=args.volume,
                 rotate=args.rotate,
                 crop=args.crop,
                 speed=args.speed,
                 hwaccel=args.hwaccel)
    
    elif args.command == "batch":
        batch_process(args.dir, args.output_dir, 
                      quality=args.quality, 
                      scale=args.scale, 
                      volume=args.volume,
                      hwaccel=args.hwaccel)
        
    elif args.command == "concat":
        concat_videos(args.inputs, args.output)
        
    elif args.command == "extract":
        extract_type = "audio" if args.audio else "subs"
        extract_media(args.input, extract_type, args.output)
        
    elif args.command == "info":
        get_info(args.input)
        
    elif args.command == "update":
        self_update()

if __name__ == "__main__":
    main()
