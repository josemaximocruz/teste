from pytubefix import YouTube
from pytubefix.cli import on_progress

# url = "https://youtu.be/NgYASqj-JUo?si=yBfYS_DlH6ZoqrtM"
url = "hhttps://www.youtube.com/watch?v=YlztlOGQpMo"

destino = "pasta_video"

yt = YouTube(url, on_progress_callback= on_progress)
print(yt.title)

ys = yt.streams.get_lowest_resolution()

ys.download(output_path=destino)