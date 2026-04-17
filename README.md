# combine

A fast, lightweight CLI tool to merge video and audio files, batch process directories, and inspect media metadata using FFmpeg.

## Features

-   **Fast Merging**: Uses stream copying by default to merge video and audio in seconds without quality loss.
-   **Subcommand Architecture**: Clean and intuitive CLI with `merge`, `batch`, `info`, and `update` commands.
-   **High Quality Preset**: Re-encode video using `libx264` with a high-quality CRF setting when needed.
-   **Audio Trimming**: Offset or trim audio starts with the `--audio-start` flag.
-   **Batch Processing**: Automatically pairs video and audio files in a directory by filename and merges them all at once.
-   **Metadata Inspection**: Built-in `info` command to view duration, codecs, and resolution.
-   **Self-Updating**: Keep the tool up-to-date with a single command.

## Installation

Install `combine` directly from GitHub using the following command:

```bash
curl -sSL https://raw.githubusercontent.com/squishna/combine-av/main/install.sh | bash
```

*Note: Ensure `~/.local/bin` is in your `$PATH`. You may need to add `export PATH="$PATH:$HOME/.local/bin"` to your `.bashrc` or `.zshrc`.*

### Requirements

-   **Python 3.6+**
-   **FFmpeg** (installed and available in your PATH)

## Usage

### 1. Merge Video and Audio
```bash
combine merge -v video.mp4 -a audio.mp3 -o output.mp4
```

**Advanced Merge Options:**
-   `--quality high`: Re-encodes video for better compatibility/quality.
-   `--audio-start 5.5`: Starts the audio from the 5.5-second mark.
-   `--format mkv`: Forces the output container format.

### 2. Batch Process a Directory
Merges all video and audio files with matching names in a folder:
```bash
combine batch --dir ./my_clips --output-dir ./merged_output
```

### 3. Inspect Media Info
```bash
combine info -i video.mp4
```

### 4. Update the Tool
```bash
combine update
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
