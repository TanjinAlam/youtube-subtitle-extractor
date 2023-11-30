
import os
from helper import post_process_data, post_request, pre_process_data , download_caption, remove_file
import requests
from dotenv import load_dotenv
import time

load_dotenv()
google_api_key = os.getenv("google_api_key")


def get_latest_video():
    channel_id = "UCIALMKvObZNtJ6AmdCLP7Lg"  
    max_result = "5"
    url = f"https://www.googleapis.com/youtube/v3/search?channelId={channel_id}&order=date&part=snippet&type=video&videoCaption=closedCaption&maxResults={max_result}&key={google_api_key}"
    arr_result = []
    response = requests.get(url)
    data = response.json()
    for yt in data['items']:
        arr_result.append({'title': yt['snippet']['title'], 'id': yt['id']['videoId'], 'date': yt['snippet']['publishedAt']})
    
    for y_data in arr_result:
        download_caption(y_data['id'])
        data = pre_process_data(f"{y_data['id']}.en.vtt")
        process_data = post_process_data(f"{y_data['id']}.en.vtt.txt")
        # #Create stored data
        db_data = { 'date' : y_data['date'], 'data' : process_data , 'title': y_data['title'], 'source':y_data['id']}
        post_request(db_data)
        remove_file(f"{y_data['id']}.en.vtt")
        remove_file(f"{y_data['id']}.en.vtt.txt")
        # Assuming you are getting channelId and max_result from the query parameters
    


while True:
    get_latest_video()
    time.sleep(30)  #



