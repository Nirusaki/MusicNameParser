from youtube_title_parse import get_artist_title
title = str(input(print("ENTER THE FREAKING STRING")))
title = title.replace("_"," ")
title = title.replace(".mp3","")
title = title.replace("(","") ## REMOVING SOME COMMONLY USED KEYWORD
title = title.replace("Official","")
title = title.replace("Music","")
title = title.replace("Video","")
artist , title = get_artist_title(title)
print(artist)
print(title)
fstringun = f"[Artist - {artist}]" + f"[Song - {title}]" + "[AYEDAEMON]" + ".mp3" ##AND AYEDAEMON FOR THE INSPIRATION
print(fstringun)
