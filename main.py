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
        playing = data['is_playing']

        if not playing:
            return 'None'

        name_data = {
            'author': data['item']['artists'][0]['name'],
            'name': data['item']['name']
        }
        return f'{name_data["author"]} - {name_data["name"]}'
    else:
        return 'None'

def main():
    current_song = request_current_song()
    print(current_song)

if __name__ == '__main__':
    main()
