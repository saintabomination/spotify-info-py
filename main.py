from dotenv import dotenv_values
import requests

ENV_PATH = '.env'
ENV_FILE = dotenv_values(ENV_PATH)
ACCESS_TOKEN = ENV_FILE['ACCESS_TOKEN']
API_ENDPOINT = 'https://api.spotify.com/v1/me/player/currently-playing'

def request_current_song():
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    request = requests.get(API_ENDPOINT, headers = headers)

    if request.status_code == 200:
        data = request.json()
        print(data)
    else:
        return 'N/A'

def main():
    request_current_song()

if __name__ == '__main__':
    main()
