import speech_recognition as sr  # This allows the computer to listen and understand your voice
import os  # This lets the program talk to your computer's operating system
import webbrowser  # This lets the program open websites on the internet
import datetime  # This lets the program work with dates and times
import re  # This lets the program find patterns in text (regular expressions)
import subprocess  # This allows the program to run other programs on your computer
import platform  # This helps detect which kind of computer you have (Windows, Mac, Linux)
import random  # This lets the program pick a random choice from a list

def say(text):
    """This function makes Bro speak by printing text and using the computer's voice"""
    print(f"Bro: {text}")  # Show the text Bro is saying on the screen
    os.system(f"say '{text}'")  # Use the computer's speech feature to say the text out loud

def takeCommand():
    """This function listens to your voice and tries to understand what you say"""
    r = sr.Recognizer()  # Create a speech recognition object that can listen and understand
    with sr.Microphone() as source:  # Use the microphone as the sound source
        print("Listening...")  # Tell the user Bro is listening
        r.pause_threshold = 1  # Wait 1 second after you stop talking before processing
        audio = r.listen(source)  # Listen to the sound from the microphone
        
        try:
            # Try to convert the speech into text using Google’s speech service
            query = r.recognize_google(audio, language='en-in')  
            print(f"User said: {query}")  # Show what the user said
            return query.lower()  # Return the text in all lowercase letters for easier handling
        
        except Exception as e:  
            # If the speech was not understood, tell the user
            print("Sorry, I did not understand that.")
            return "None"  # Return "None" as a sign that no valid command was heard

def tell_time():
    """This function tells the current time"""
    current_time = datetime.datetime.now().strftime("%I:%M %p")  # Get current time like 02:45 PM
    say(f"The current time is {current_time}")  # Make Bro say the time

def tell_date():
    """This function tells the current date"""
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")  # Get date like Monday, May 16, 2025
    say(f"Today is {current_date}")  # Make Bro say the date

def tell_dark_joke():
    """This function tells a dark humor joke by choosing one randomly"""
    dark_jokes = [
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "What's the difference between a Ferrari and a pile of dead bodies? I don't have a Ferrari in my garage.",
        "Why don't orphans play baseball? They don't know where home is.",
        "Dark humor is like food, not everyone gets it.",
        "What's the hardest part about walking through a field of dead babies? My erection.",
        "What is the difference between a baby and an onion? No one cries when you chop up the baby.",
        "Why don't cannibals eat clowns? Because they taste funny.",
        "What's the difference between a joke and a dead body? Timing.",
        "I have a lot in common with my job. We're both slowly killing me.",
        "Why did the dead baby cross the road? Because it was stapled to the chicken.",
        "How many babies does it take to paint a wall? Depends how hard you throw them.",
        "Do you know the last thing that went through Princess Diana's mind? The dashboard.",
        "What do Princess Diana and Pink Floyd have in common? Their last big hit was The Wall.",
        "How do you get a Jewish girl's number? Roll up her sleeve.",
        "What's the difference between a pizza and a Jew? A pizza doesn't scream in the oven.",
        "What's worse than finding a worm in your apple? The Holocaust.",
        "What breaks when you give it to a three-year-old? Their hips.",
        "How many cops does it take to change a light bulb? None, they just beat the room for being black.",
        "They said to look in the mirror and love what you see. Now I'm charged with vandalism.",
        "My grandfather died peacefully in his sleep, unlike the screaming passengers in his car."
    ]
    joke = random.choice(dark_jokes)  # Pick one joke randomly from the list
    say(joke)  # Make Bro say the joke
    return True  # Tell the program the joke was told successfully

def play_music(query):
    """This function tries to play a song on YouTube based on what the user says"""
    # These are patterns to find the song name in the user's command
    song_patterns = [
        r"play\s+(.*?)(?:\s+on\s+(.*?)|\s+from\s+(.*?))?$",
        r"play\s+song\s+(.*?)(?:\s+on\s+(.*?)|\s+from\s+(.*?))?$",
        r"play\s+music\s+(.*?)(?:\s+on\s+(.*?)|\s+from\s+(.*?))?$"
    ]
    
    for pattern in song_patterns:
        match = re.search(pattern, query)  # Try to find the song name in the user's speech
        if match:
            song_name = match.group(1).strip()  # Extract the song name
            encoded_song = song_name.replace(" ", "+")  # Prepare song name for a website link
            
            try:
                say(f"Playing {song_name} on YouTube...")  # Tell the user what song is playing
                web_url = f"https://www.youtube.com/results?search_query={encoded_song}"  # YouTube search URL
                webbrowser.open(web_url)  # Open the YouTube search page in the browser
                return True  # Song started successfully
                
            except Exception as e:
                say(f"I had trouble playing {song_name} on YouTube.")  # Tell user if error happens
                print(f"Error: {str(e)}")
                return False
    
    return False  # No song name found in the query

def open_website(query):
    """This function opens websites based on what the user says"""
    # A list of popular websites with their names and URLs
    sites = [["Google", "https://www.google.com"],
             ["Stack Overflow", "https://stackoverflow.com"],
             ["Github", "https://github.com"],
             ["Youtube", "https://www.youtube.com"],
             ["Wikipedia", "https://www.wikipedia.org"],
             ["Reddit", "https://www.reddit.com"],
             ["Twitter", "https://twitter.com"],
             ["Facebook", "https://www.facebook.com"],
             ["Instagram", "https://www.instagram.com"],
             ["LinkedIn", "https://www.linkedin.com"],
             ["Pinterest", "https://www.pinterest.com"],
             ["Quora", "https://www.quora.com"],
             ["Netflix", "https://www.netflix.com"],
             ["Amazon", "https://www.amazon.com"],
             ["eBay", "https://www.ebay.com"],
             ["Spotify", "https://www.spotify.com"],
             ["Discord", "https://discord.com"],
             ["Twitch", "https://www.twitch.tv"],
             ["TikTok", "https://www.tiktok.com"],
             ["Snapchat", "https://www.snapchat.com"],
             ["WhatsApp", "https://web.whatsapp.com"],
             ["Telegram", "https://web.telegram.org"],
             ["ChatGPT", "https://chat.openai.com"]]
    
    # Check if any of the popular site names are in the user query
    for site in sites:
        if site[0].lower() in query:
            say(f"Opening {site[0]}...")  # Tell user which site is opening
            try:
                webbrowser.open(site[1])  # Open the website in the browser
                return True
            except Exception as e:
                say(f"I had trouble opening {site[0]}.")  # Tell user if error happens
                print(f"Error: {str(e)}")
                return False
    
    # If not a known site, check if user said something like "open website name"
    open_patterns = [
        r"open\s+(.*?)(?:\s+website|\s+site)?$",
        r"go\s+to\s+(.*?)(?:\s+website|\s+site)?$",
        r"navigate\s+to\s+(.*?)(?:\s+website|\s+site)?$",
        r"browse\s+(.*?)(?:\s+website|\s+site)?$",
        r"visit\s+(.*?)(?:\s+website|\s+site)?$"
    ]
    
    for pattern in open_patterns:
        match = re.search(pattern, query)
        if match:
            website_name = match.group(1).strip()  # Get the website name
            
            # Check if the name already looks like a website address
            if re.search(r'\.[a-z0-9]{2,}(/|$)', website_name) or website_name.startswith(('http://', 'https://')):
                if not website_name.startswith(('http://', 'https://')):
                    website_url = f"https://{website_name}"  # Add https if missing
                else:
                    website_url = website_name
            else:
                # Look for parts of the web address like "dot com" or "dot ac dot in"
                dot_parts = re.findall(r'dot\s+([a-z0-9]+)', query)
                
                if dot_parts:
                    extension = '.'.join(dot_parts)  # Join these parts with dots to make the extension
                    
                    clean_name = website_name
                    for part in dot_parts:
                        # Remove the "dot extension" words from the name
                        clean_name = re.sub(r'\s+dot\s+' + part, '', clean_name)
                    
                    website_url = f"https://www.{clean_name.replace(' ', '')}.{extension}"
                else:
                    # If no extension, add ".com" by default
                    website_url = f"https://www.{website_name.replace(' ', '')}.com"
            
            say(f"Opening {website_name}...")  # Tell user the website is opening
            try:
                webbrowser.open(website_url)  # Open the website
                return True
            except Exception as e:
                say(f"I had trouble opening {website_name}.")  # Tell user if error happens
                print(f"Error: {str(e)}")
                return False
    
    return False  # No website opened

def display_help():
    """This function tells the user what Bro can do"""
    say("I can help you with the following:")
    say("Ask me for the current time")
    say("Ask me for today's date")
    say("Ask me to open any website by saying 'open website name'")
    say("For specific extensions, say 'open website name dot extension'")
    say("For multi-part extensions, say 'open website dot ac dot in'")
    say("Ask me to play songs by saying 'play song name' - I'll play it on YouTube")
    say("Ask me to tell a dark humor joke")
    say("Say goodbye or exit to quit")

def process_query(query):
    """This function looks at what the user said and decides what to do"""
    if "time" in query:
        tell_time()  # Tell the current time
        return True
        
    if "date" in query or "day" in query or "today" in query:
        tell_date()  # Tell today's date
        return True
        
    if "exit" in query or "quit" in query or "goodbye" in query or "bye" in query:
        say("Goodbye! Have a nice day.")  # Say goodbye
        return "exit"
        
    if "help" in query:
        display_help()  # Show help instructions
        return True
    
    # If user asks for a dark joke
    if ("tell" in query or "say" in query or "give" in query) and ("joke" in query or "jokes" in query) and ("dark" in query or "offensive" in query or "messed up" in query):
        tell_dark_joke()
        return True
    
    # Try to play music if the user wants
    music_played = play_music(query)
    if music_played:
        return True
        
    # Try to open a website if the user asks
    website_opened = open_website(query)
    if website_opened:
        return True
    
    # If nothing matched, tell the user you don't understand
    if query != "None":
        say("I'm not sure how to help with that. Try asking for help to see what I can do.")
    
    return False

def main():
    """This is the main function that starts Bro and listens forever"""
    say("Hello, I am Bro the A.I assistant.")
    
    while True:  # Keep listening until the user says exit
        query = takeCommand()  # Listen for what the user says
        
        if query:
            query = query.lower()  # Make the query lowercase so it's easier to check
            
            result = process_query(query)  # Do what the user asked
            
            if result == "exit":  # If user wants to stop, break the loop
                break

if __name__ == '__main__':
    main()  # Start the program
