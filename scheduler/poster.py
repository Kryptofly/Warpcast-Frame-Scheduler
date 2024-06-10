import requests
from config import WARPCAST_API_TOKEN

def post_frame(frame_url):
    warpcast_url = "https://api.warpcast.com/v1/frames"
    headers = {
        'Authorization': f'Bearer {WARPCAST_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    payload = {
        'frame_url': frame_url
    }
    response = requests.post(warpcast_url, headers=headers, json=payload)
    response.raise_for_status()
