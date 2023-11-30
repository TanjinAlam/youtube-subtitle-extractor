import json
import re
import time

import requests
import webvtt
import os
import yt_dlp
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
bad_words = ['-->','</c>']
host_address = os.getenv("host_address")
# mongo_host = os.getenv("MONGO_HOST")
# mongo_port = int (os.getenv("MONGO_PORT"))
# mongo_username = os.getenv("MONGO_USERNAME")
# mongo_password = os.getenv("MONGO_PASSWORD")


def pre_process_data(file_name: str):
    with open(file_name) as oldfile, open(f"{file_name}.txt", 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)

def post_process_data(file_name: str):
    # Open the file in read mode
    with open(f"{file_name}", 'r') as file:
        # Read the entire content of the file
        content = file.read()
        splits = content.split("\n")[4:]
        splits = [item for item in splits if item!=""]
        splits = ' '.join(splits)
        return splits
        
# def save_data(data):
#     client = MongoClient(
#         host=mongo_host,
#         port=mongo_port,
#         username=mongo_username,
#         password=mongo_password
#     )
#     client['youtube-data']['captions'].insert_one(data)

            
def post_request(data):
    # Replace the URL with the actual endpoint you want to send the POST request to
    url = host_address

    # Data to be sent in the POST request
    post_data = {
        "youtubeNews": data['data'],
        "title": data['title'],
        "author": "bloomberg",
        "source": data['source']
    }

    # Convert the data to JSON format
    json_data = json.dumps(post_data)

    # Set the headers to specify that you are sending JSON data
    headers = {"Content-Type": "application/json"}

    # Make the POST request
    response = requests.post(url, data=json_data, headers=headers)

    print(response.json())
        


def download_caption(file_name : str):
    ydl_opts = {
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'skip_download': True,
        'outtmpl': file_name,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(file_name, download=False)
        ydl.download([file_name])

def remove_file(file_name: str):
    os.remove(file_name)
    print("DELETING", file_name)
    time.sleep(1)


