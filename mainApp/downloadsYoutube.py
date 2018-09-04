import youtube_dl


def getlinkdownloadNew(currentLink):
    path_template = 'media/uploads/%(title)s.%(ext)s'

    youtube_options = {
        'outtmpl': path_template,
        'format': 'bestaudio/best',
        # 'audio-format': 'mp3',
        'extractaudio': True,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }
        ],
    }

    path = None
    title = None

    with youtube_dl.YoutubeDL(youtube_options) as youtubeVariable:
        video_info = youtubeVariable.extract_info(currentLink, download=True)
        title = video_info.get('title')
        ext = video_info.get('ext')

        path = path_template % {'title': title, 'ext': ext}

    return path, title
