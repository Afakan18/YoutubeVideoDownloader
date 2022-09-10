import pytube as pt

yt = pt.YouTube("https://www.youtube.com/watch?v=JugHj6GNU3E")
t = yt.streams.filter(only_audio=True)
t[0].download()