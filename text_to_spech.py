import gtts 
import playsound 
text  = input("enter somthing here:")
sound = gtts. GTTS(text,lang = "en")
sound.save ("welcome.mp3")
playsound.playsound ("welcome.mp3")
