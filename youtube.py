import youtube_dl, pickle

             # UCVTyTA7-g9nopHeHbeuvpRA is the channel id (1517+ videos)
PLAYLIST_ID = 'UU3RFDPzA5H8DTLxQ1cTf12A'  # Late Night with Seth Meyers

with youtube_dl.YoutubeDL({'ignoreerrors': True}) as ydl:

    playd = ydl.extract_info(PLAYLIST_ID, download=False)

    with open('playlist.pickle', 'wb') as f:
        pickle.dump(playd, f, pickle.HIGHEST_PROTOCOL)

    vids = [vid for vid in playd['entries'] if 'Demomaker' in vid['title']]
    print(sum('Demomaker' in vid['title'] for vid in vids), '/', len(vids))