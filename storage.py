import requests
import os

# Get photos/video/GIF from the specified url and store them.
# Input: the twitter entity that contain url, media_url, expanded_url...
# Output: the file_path where the media stored and file_type
def get_pic(entities, idx):
	media = entities["media"][0]
	media_url = media["media_url"]
	web_url = media["url"]
	file_type = media["expanded_url"][-7:-2]
	file_path = './data/top' + str(idx) + '.jpg'
	os.remove(file_path)
	with open(file_path, 'wb') as handle:
		response = requests.get(media_url, stream=True)
		if not response.ok:
			print(response)
		for block in response.iter_content(1024):
			if not block:
				break
			handle.write(block)

	return file_path, file_type