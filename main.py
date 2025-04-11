from fastapi import FastAPI
import yt_dlp

app = FastAPI()

@app.get("/get_links/")
def get_links(video_id: str, resolution: str = None):
    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'format': f'best[height={resolution}]' if resolution else 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get("formats", [])
        return {
            "title": info_dict.get("title", ""),
            "links": [f["url"] for f in formats if "url" in f]
        }