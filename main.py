import requests, os

text = "twist"
url = f"https://freetts.com/Home/PlayAudio?Language=en-US&Voice=en-US-Standard-C&TextMessage={text}&type=0"
path = requests.get(url).json()['id']
get_mp3 = open('sound.mp3','wb').write(requests.get(f'https://freetts.com/audio/{path}').content)
os.system('sound.mp3')
