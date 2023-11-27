import os
import yt_dlp

video_id = "povkn8AgKig"
output_file_vtt = video_id
output_file_txt = video_id + ".txt"

ydl_opts = {
    'writesubtitles': True,
    'writeautomaticsub': True,
    'subtitleslangs': ['en'],
    'skip_download': True,
    'outtmpl': output_file_vtt,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_id, download=False)
    ydl.download([video_id])

# Rename the downloaded .vtt file to .txt
# os.rename(f"{video_id}.en.vtt", output_file_txt)



