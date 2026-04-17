# combine-av

<img src="https://raw.githubusercontent.com/ramkrishna-peg/.github/main/file_00000000991c7208b5208584308287a6.png" align="right" width="200" alt="combine logo">

A command-line tool to merge video and audio streams with speed and precision.

`combine` is a lightweight Python-based wrapper around FFmpeg that simplifies the process of joining separate video and audio tracks. Whether you're handling a single pair or batch processing an entire directory, `combine` ensures the highest quality with minimal effort.

---

## [INSTALLATION](#installation)

You can install `combine` using our streamlined installation script. This will set up the tool in `~/.combine-av` and link the `combine` command to your `~/.local/bin`.

```bash
curl -sSL https://raw.githubusercontent.com/squishna/combine-av/main/install.sh | bash
```

**Requirements:**
- Python 3.6 or later
- [FFmpeg](https://ffmpeg.org/download.html) (must be in your system `PATH`)

---

## [USAGE](#usage)

### Basic Merge
The primary command for merging a single video and audio file:
```bash
combine merge -v video.mp4 -a audio.mp3 -o output.mp4
```

### Options and Presets
- **Quality Control**: Use `-q high` to re-encode using `libx264` for better compatibility, or stick with the default `-q fast` for instant stream copying.
- **Audio Trimming**: Use `--audio-start <seconds>` to sync or trim your audio track precisely.
- **Format Forcing**: Use `-f <format>` (e.g., `mkv`, `mp4`) to specify the output container.

### Batch Processing
Merge all matching video and audio pairs in a directory automatically:
```bash
combine batch --dir ./my_media --output-dir ./merged
```

### Metadata Inspection
Quickly view the streams and duration of any media file:
```bash
combine info -i file.mp4
```

---

## [SELF-UPDATE](#self-update)

Keep your installation current with the latest features and fixes:
```bash
combine update
```

---

## [LICENSE](#license)

This project is released under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

<p align="center">
    <b>Built with speed. Powered by FFmpeg.</b>
</p>
