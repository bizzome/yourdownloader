import argparse
import logging
import os
import sys
from typing import Optional

from pytube import YouTube, Playlist
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def setup_argparse() -> argparse.Namespace:
    """Set up command line argument parsing."""
    parser = argparse.ArgumentParser(description='YouTube Video/Audio Downloader')
    parser.add_argument('url', help='YouTube video or playlist URL')
    parser.add_argument('--output', '-o', default=os.path.expanduser('~/Downloads'),
                      help='Output directory (default: ~/Downloads)')
    parser.add_argument('--audio-only', '-a', action='store_true',
                      help='Download audio only')
    parser.add_argument('--quality', '-q', default='highest',
                      choices=['highest', '720p', '480p', '360p'],
                      help='Video quality (default: highest)')
    parser.add_argument('--playlist', '-p', action='store_true',
                      help='Download entire playlist')
    return parser.parse_args()

def on_progress(stream, chunk: bytes, bytes_remaining: int):
    """Callback function for download progress."""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    logger.info(f"Download Progress: {percentage:.1f}%")

def download_video(url: str, output_path: str, audio_only: bool, quality: str) -> Optional[str]:
    """Download a single video."""
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        logger.info(f"Title: {yt.title}")
        
        if audio_only:
            stream = yt.streams.filter(only_audio=True).first()
            if not stream:
                logger.error("No audio stream found")
                return None
        else:
            if quality == 'highest':
                stream = yt.streams.get_highest_resolution()
            else:
                stream = yt.streams.filter(res=quality).first()
                if not stream:
                    logger.warning(f"Quality {quality} not available, using highest available")
                    stream = yt.streams.get_highest_resolution()

        if not stream:
            logger.error("No suitable stream found")
            return None

        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Download the file
        file_path = stream.download(output_path)
        logger.info(f"Download completed: {file_path}")
        return file_path

    except Exception as e:
        logger.error(f"Error downloading video: {str(e)}")
        return None

def download_playlist(url: str, output_path: str, audio_only: bool, quality: str):
    """Download all videos from a playlist."""
    try:
        playlist = Playlist(url)
        logger.info(f"Playlist: {playlist.title}")
        logger.info(f"Number of videos: {len(playlist.video_urls)}")

        for video_url in playlist.video_urls:
            download_video(video_url, output_path, audio_only, quality)

    except Exception as e:
        logger.error(f"Error downloading playlist: {str(e)}")

def main():
    args = setup_argparse()
    
    try:
        if args.playlist:
            download_playlist(args.url, args.output, args.audio_only, args.quality)
        else:
            download_video(args.url, args.output, args.audio_only, args.quality)
    except KeyboardInterrupt:
        logger.info("\nDownload cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

