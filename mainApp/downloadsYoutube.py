import youtube_dl
def getlinkdownloadNew(currentLink):
    url = ""
    youtube_options = {
    'outtmpl': 'media/uploads/%(title)s%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(youtube_options) as youtubeVariable:
        dict_info = youtubeVariable.extract_info(currentLink, download=False)
        url=dict_info['url']
        print(dict_info.keys)
    return url
