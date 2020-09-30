import speech_recognition as sr
import webbrowser
import pyttsx3
import os

print("<<--------------------------------------!! WELCOME !!------------------------------------>>\n")
pyttsx3.speak("Hello User !! How may I help you!!")
print("THE TOOLS AVAILABLE IN YOUR PC ARE : ")
print("1.) Chrome")
print("2.) Window Media Player")
print("3.) Notepad")
print("4.) Date")
print("5.) Calander\n")
print("                  SPEAK YOUR REQUIREMENTS                  ")
pyttsx3.speak("SPEAK YOUR REQUIREMENTS")
print("                  WE ARE LISTENING.....                  ")


while True:
 r = sr.Recognizer()
 with sr.Microphone() as source:
   print("                  START SAYING...                  ")
   audio = r.listen(source)
 print("<<---------------------------------!! WE GOT YOU !!------------------------------->>")


 ch = r.recognize_google(audio) 

 if ("date" in ch) and ("run" in ch):
  		webbrowser.open("http://192.168.43.26/cgi-bin/f.py?x=date")

 elif ("calander" in ch) and ("run" in ch):
  		webbrowser.open("http://192.168.43.26/cgi-bin/f.py?x=cal")

 elif (("launch" in ch) or ("run" in ch) or("execute" in ch) or ("open" in ch)) and (("chrome" in ch) or ("google chrome") or ("BROWSER" in ch)):
		pyttsx3.speak("launching chrome for you")
		print("launching chrome for you")
		os.system("chrome")
		
 elif (("launch" in ch) or ("run" in ch) or("execute" in ch) or ("open" in ch)) and  (("notepad" in ch) or ("editor" in ch)):	
		pyttsx3.speak("launching notepad for you")
		print("launching notepad for you")
		os.system("notepad")
		
 elif (("play" in ch) or ("OPEN" in ch) or ("launch" in ch) or ("RUN" in ch) or ("open" in ch)) and (("wmplayer" in ch) or ("music" in ch)):
		pyttsx3.speak("launching wmplayer for you")
		print("launching wmplayer for you")
		os.system("wmplayer")
		
 elif ("exit" in ch)  or ("quit" in ch) or ("stop" in ch):
		print("<<-------------------------------!! STOPPED !!------------------------------->>")
		break

 else:
  		print("NOT AVAILABLE")
