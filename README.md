# combine-av

<img src="https://raw.githubusercontent.com/ramkrishna-peg/.github/main/file_00000000991c7208b5208584308287a6.png" align="right" width="200" alt="combine-av logo">

[![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)](https://github.com/squishna/combine-av)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/squishna/combine-av/actions/workflows/ci.yml/badge.svg)](https://github.com/squishna/combine-av/actions)

A high-performance FFmpeg-based CLI tool to merge, batch process, extract, and concatenate media streams with ease.

---

## [INSTALLATION](#installation)

Install **combine-av** instantly using our setup script. This installs the tool to `~/.combine-av` and links the `combine` command to your local bin.

```bash
curl -sSL https://raw.githubusercontent.com/squishna/combine-av/main/install.sh | bash
```

### Requirements
- **Python 3.6+**
- **FFmpeg** (Must be accessible in your system `PATH`)

---

## [COMMANDS](#commands)

### 1. Merge Streams (`merge`)
Combine a video file with one or more audio tracks and optional subtitles.

```bash
combine merge -v video.mp4 -a audio.mp3 -o output.mp4
```

**Key Options:**
- `-a track1.mp3 track2.mp3`: Add multiple audio tracks to a single video.
- `-s subtitles.srt`: Attach a subtitle file.
- `-q {fast,high}`: `fast` (default) uses stream copying; `high` re-encodes for maximum compatibility.
- `--scale {1080p,720p,480p,360p}`: Resize the video frame.
- `--rotate {90,180,270}`: Clockwise rotation.
- `--volume 1.5`: Boost audio volume by 50%.
- `--speed 2.0`: Double the playback speed of both video and audio.
- `--hwaccel {nvenc,vaapi,videotoolbox}`: Use your GPU for ultra-fast processing.

---

### 2. Batch Processing (`batch`)
Automatically merge multiple video/audio pairs within a directory. Files are matched by their base filenames.

```bash
combine batch --dir ./raw_media --output-dir ./merged_output
```

---

### 3. Join Videos (`concat`)
Losslessly join multiple video clips into a single continuous file.

```bash
combine concat -i clip1.mp4 clip2.mp4 clip3.mp4 -o final_movie.mp4
```

---

### 4. Extract Tracks (`extract`)
Quickly pull audio or subtitle tracks out of a media container.

```bash
combine extract -i movie.mkv --audio  # Extracts primary audio as MP3
combine extract -i movie.mkv --subs   # Extracts first subtitle as SRT
```

---

### 5. Media Info (`info`)
Inspect codecs, resolution, and duration of any media file.

```bash
combine info -i file.mp4
```

---

## [DEVELOPMENT](#development)

### Contributions
We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions.

### Self-Update
Keep your `combine` installation up-to-date with the latest features:
```bash
combine update
```

---

## [LICENSE](#license)

Released under the **MIT License**. See [LICENSE](LICENSE) for details.

---

<p align="center">
    <b>Version 0.0.1 • Built by squishna</b>
</p>
