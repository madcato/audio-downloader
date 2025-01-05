# YouTube Audio Downloader

This tool allows you to download audio from YouTube videos. The format exported is **.mp3**
## Requirements

- Python 3.x
- ffmpeg (for audio extraction). Install on macOS with `brew install ffmpeg`, or follow this instruictions for Windows/Linux [ffmpeg installation guide](https://ffmpeg.org/download.html).
- Module **yt-dlep** for handling YouTube URLs. Install it with `pip install yt-dlp`.

## How to Use

1. **Clone Repository**: Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/madcato/audio-downloader.git
   ```
2. Isntall requirements
3. Ru with:
   ```bash
   python audio_downloader.py <YouTube URL>
   ```
4. Downloaded audio files are saved in the **exports** folder.
