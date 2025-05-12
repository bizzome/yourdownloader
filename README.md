# YouTube Video/Audio Downloader

A powerful and flexible YouTube video and audio downloader built with Python. This tool allows you to download individual videos or entire playlists, with options for video quality and audio-only downloads.

## Features

- Download individual videos or entire playlists
- Choose video quality (highest, 720p, 480p, 360p)
- Download audio-only versions
- Progress tracking
- Custom output directory
- Comprehensive error handling
- Detailed logging

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage Examples

### Basic Video Download

Download a single video with highest quality:
```bash
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Audio-Only Downloads

Download just the audio from a video (useful for music):
```bash
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --audio-only
```

### Video Quality Options

Download a video in 720p quality:
```bash
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --quality 720p
```

Download a video in 480p quality:
```bash
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --quality 480p
```

### Custom Output Directory

Download to a specific folder:
```bash
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --output "~/Videos/YouTube"
```

### Playlist Downloads

Download an entire playlist:
```bash
python main.py "https://www.youtube.com/playlist?list=PLxxxxxxxx" --playlist
```

Download a playlist in 720p quality:
```bash
python main.py "https://www.youtube.com/playlist?list=PLxxxxxxxx" --playlist --quality 720p
```

Download audio-only from a playlist:
```bash
python main.py "https://www.youtube.com/playlist?list=PLxxxxxxxx" --playlist --audio-only
```

### Combining Options

Download a playlist to a specific directory with custom quality:
```bash
python main.py "https://www.youtube.com/playlist?list=PLxxxxxxxx" --playlist --quality 720p --output "~/Music/Playlist"
```

### Common Use Cases

1. **Downloading Music**:
   ```bash
   # Download a music video as audio only
   python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --audio-only
   ```

2. **Archiving Educational Content**:
   ```bash
   # Download a lecture series in 720p
   python main.py "https://www.youtube.com/playlist?list=PLxxxxxxxx" --playlist --quality 720p --output "~/Videos/Lectures"
   ```

3. **Creating a Video Collection**:
   ```bash
   # Download multiple videos in highest quality
   python main.py "https://www.youtube.com/watch?v=video1" --output "~/Videos/Collection"
   python main.py "https://www.youtube.com/watch?v=video2" --output "~/Videos/Collection"
   ```

4. **Batch Processing**:
   ```bash
   # Download multiple playlists
   python main.py "https://www.youtube.com/playlist?list=PL1" --playlist --output "~/Videos/Playlist1"
   python main.py "https://www.youtube.com/playlist?list=PL2" --playlist --output "~/Videos/Playlist2"
   ```

### Command Line Arguments

- `url`: YouTube video or playlist URL (required)
- `--output`, `-o`: Output directory (default: ~/Downloads)
- `--audio-only`, `-a`: Download audio only
- `--quality`, `-q`: Video quality (choices: highest, 720p, 480p, 360p)
- `--playlist`, `-p`: Download entire playlist

## Error Handling

The script includes comprehensive error handling for various scenarios:
- Invalid URLs
- Network issues
- Unavailable video qualities
- Permission errors
- Disk space issues

All errors are logged with detailed information to help diagnose issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 