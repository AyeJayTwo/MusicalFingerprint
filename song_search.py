def song_chooser():
    
    from pyechonest import config
    from pyechonest	import song
    config.ECHO_NEST_API_KEY="VHLWI61NDUKAGF1AX"

    artist = input('Select an artist: ')
    title = input('Select a song: ')
    
    rkp_results = song.search(artist=artist, title=title)
    songs = rkp_results
    print "Please select a song: "
    counter = 0
    for each in songs:
    	print counter,": ",each
    	counter = counter + 1
    
    key = input('Choose a number: ')
    song = songs[key]
    final_url = song.audio_summary["analysis_url"]
    print "\nNow Analyzing:"
    print song.title+" by "+song.artist_name
    
    return final_url, song.artist_name, song.title