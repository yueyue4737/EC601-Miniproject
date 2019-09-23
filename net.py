import requests

pic_url = 'https://pbs.twimg.com/media/EFDPnooU0AA9geK.jpg'
with open('pic1.jpg', 'wb') as handle:
  response = requests.get(pic_url, stream=True)

  if not response.ok:
    print(response)

  for block in response.iter_content(1024):
    if not block:
      break
    handle.write(block)