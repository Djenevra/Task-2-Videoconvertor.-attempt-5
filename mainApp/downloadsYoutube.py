import youtube_dl
def getlinkdownloadNew(currentLink):
    url = ""
    youtube_options = {
    'outtmpl': 'media/uploads/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    #'audio-format': 'mp3',
    'extractaudio' : True,
    'postprocessors': [{
        'key' : 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality' : '320',
        }],
    }
    with youtube_dl.YoutubeDL(youtube_options) as youtubeVariable:
        dict_info = youtubeVariable.extract_info(currentLink, download=True)
        url=dict_info['url']
        print(dict_info.keys)
    return url
