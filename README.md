# combine-av

<img src="https://raw.githubusercontent.com/ramkrishna-peg/.github/main/file_00000000991c7208b5208584308287a6.png" align="right" width="200" alt="combine-av logo">

[![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)](https://github.com/squishna/combine-av)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/squishna/combine-av/actions/workflows/ci.yml/badge.svg)](https://github.com/squishna/combine-av/actions)

A command-line media Swiss Army knife powered by FFmpeg. **combine-av** provides a simplified yet powerful interface for merging, batching, extracting, and joining media streams with advanced filtering and hardware acceleration support.

---

## [TABLE OF CONTENTS](#table-of-contents)

-   [Installation](#installation)
-   [Quick Start](#quick-start)
-   [Commands](#commands)
    -   [merge](#merge)
    -   [batch](#batch)
    -   [concat](#concat)
    -   [extract](#extract)
    -   [info](#info)
-   [Advanced Options](#advanced-options)
    -   [Hardware Acceleration](#hardware-acceleration)
    -   [Video Filters](#video-filters)
    -   [Audio Volume & Speed](#audio-volume-speed)
-   [Update](#update)
-   [Troubleshooting](#troubleshooting)
-   [License](#license)

---

## [INSTALLATION](#installation)

Install **combine-av** using our automated setup script. This installs the core application into `~/.combine-av` and creates a symbolic link in `~/.local/bin`.

```bash
curl -sSL https://raw.githubusercontent.com/squishna/combine-av/main/install.sh | bash
```

### System Requirements
- **Python**: Version 3.6 or higher.
- **FFmpeg**: Must be installed and accessible in your system `PATH`.
    - *Linux*: `sudo apt install ffmpeg` or `sudo pacman -S ffmpeg`
    - *macOS*: `brew install ffmpeg`
    - *Windows*: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

---

## [QUICK START](#quick-start)

Merge a video and an audio track into a single file:
```bash
combine merge -v movie.mp4 -a track1.mp3 -o output.mp4
```

Extract the audio from a video:
```bash
combine extract -i movie.mp4 --audio
```

Join multiple clips into one:
```bash
combine concat -i clip1.mp4 clip2.mp4 -o full_video.mp4
```

---

## [COMMANDS](#commands)

### `merge`
Combines video and multiple audio streams into one container.

| Option | Description |
| :--- | :--- |
| `-v, --video` | **Required.** Path to the input video file. |
| `-a, --audio` | **Required.** Path(s) to input audio track(s). Supports multiple tracks. |
| `-o, --output` | **Required.** Final output file path. |
| `-s, --subtitle` | Optional subtitle file (SRT, ASS, VTT). |
| `-f, --format` | Force an output container format (e.g., `mkv`, `webm`). |
| `-q, --quality` | `fast` (copies video streams) or `high` (re-encodes for quality). |

### `batch`
Automatically merge matching video and audio pairs in a directory.

| Option | Description |
| :--- | :--- |
| `-d, --dir` | **Required.** Directory containing source files. |
| `-o, --output-dir` | **Required.** Destination directory for merged results. |
| `-q, --quality` | Quality preset for all files in the batch. |

### `concat`
Losslessly joins multiple video files into a single continuous file.

```bash
combine concat -i clip1.mp4 clip2.mp4 clip3.mp4 -o final_movie.mp4
```

### `extract`
Extracts specific streams from a media file.

- `--audio`: Extracts the primary audio track as a high-quality MP3.
- `--subs`: Extracts the first subtitle track as an SRT file.

### `info`
Provides detailed technical metadata about any media file.
```bash
combine info -i filename.mp4
```

---

## [ADVANCED OPTIONS](#advanced-options)

### Hardware Acceleration
Accelerate re-encoding and filtering using your GPU.

- `--hwaccel nvenc`: NVIDIA (requires `h264_nvenc`).
- `--hwaccel vaapi`: Intel/AMD (requires `h264_vaapi`).
- `--hwaccel videotoolbox`: Apple Silicon/Intel (requires `h264_videotoolbox`).

### Video Filters
Applying filters forces re-encoding of the video stream.

- `--scale {1080p, 720p, 480p, 360p}`: Resizes the video frame while maintaining aspect ratio (adds padding if needed).
- `--rotate {90, 180, 270}`: Rotates the video clockwise by the specified degree.
- `--crop <w:h:x:y>`: Crops the video to the specified dimensions and offsets.
- `--speed <float>`: Changes the playback speed (e.g., `1.5` for 150% speed).

### Audio Volume & Speed
- `--volume <float>`: Multiplies the audio volume (e.g., `2.0` to double volume).
- `--audio-start <seconds>`: Delays or trims the start of the audio tracks.

---

## [UPDATE](#update)

Update **combine-av** to the latest version directly from GitHub:

```bash
combine update
```

---

## [TROUBLESHOOTING](#troubleshooting)

### "FFmpeg not found"
Ensure FFmpeg is in your system PATH. Test it by running `ffmpeg -version` in your terminal.

### "Command not found: combine"
Your shell might not include `~/.local/bin` in its PATH. Add the following line to your `.bashrc` or `.zshrc`:
```bash
export PATH="$PATH:$HOME/.local/bin"
```

### "Unsupported Codec"
If a specific container (like `.mp4`) doesn't support an input codec, use `--format mkv` for maximum compatibility.

---

## [LICENSE](#license)

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for the full text.

---

<p align="center">
    <b>Crafted by squishna with precision and speed.</b><br>
    <i>© 2026 squishna. All rights reserved.</i>
</p>
