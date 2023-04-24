from ast import Delete
from asyncio.windows_events import NULL
from calendar import different_locale
from concurrent.futures import thread
from email import message
from itertools import count
from multiprocessing import context
from operator import truediv
from pickle import FALSE, TRUE
from sqlite3 import Time
from tkinter import PhotoImage
from types import TracebackType
from xmlrpc.client import DateTime
from telegram.ext import *
from telegram import ParseMode, TelegramError, Update
import telegram
import requests
import random
import datetime
import time
import threading


print ("Starting up!")



reset = "\x1b[0m"
black = "\x1b[30m"
red = "\x1b[31m"
green = "\x1b[32m"
yellow = "\x1b[33m"
cyan = "\x1b[36m"

ScylezUID = 270515584

Users = []
TotalMessages = []
Silenced = []
LastSeconds =0
SpamCheckMinute = 0
SilencedMinute = 0
LastTenMinute = 0
LastTenMinuteHour = 0
SpamLimit = 6



PhotoUsers = []
TotalPhotos = []

PtotosSentTenMinutes = []
StickersSentTenMinutes = []
AnimationsSentTenMinutes = []
SentTenMinutesLimit = 10
individualPhotoLimit = 10

activate = False
timeout = False

timedEvents = False
lastTimedEventDay = 0
lastTimedEventMonty = 0

run_async
def send_async(context, *args, **kwargs):
    context.bot.send_message(*args, **kwargs)

def getChatIds():
  getUpdatesUrl = "https://api.telegram.org/bot" + ApiKey + "/getUpdates"
  response = requests.get(getUpdatesUrl)
  jsonResponse = response.json()
  groupChats = {}
  for x in jsonResponse['result']:
    if (x['message']['chat']['type'] == 'group'):
      groupChats[x['message']['chat']['id']] = x['message']['chat']['title']
  return groupChats

def sendGroupMessage(groupChats, groupMessage):
    sendMsgUrl = "https://api.telegram.org/bot" + ApiKey + "/sendMessage"
    for key in groupChats:
        print(green, "Sending to Group Chat : ", groupChats[key], reset)
        parameters = {
            "chat_id" : key,
            "text" : groupMessage,
            "parse_mode" : "html"
        }
        response = requests.get(sendMsgUrl, data = parameters)

def empty_message(update, context):
    #Empty messages could be status messages, so we check them if there is a new
    #group member, someone left the chat or if the bot has been added somewhere.
    
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
                return welcome(update, context, new_member)

    # Someone left the chat
    elif update.message.left_chat_member is not None:
        return goodbye(update, context)

def GetIntroText():
    text= "Feel free to jump into the conversation as we chat about not only the Chasing Tail Visual Novel but also: food and cooking, space and science, video and bored games, firearms and shooting, furry nonsense, game development and coding, artwork and drawing, and of course yiff."
    text+= "\n \n We don't have very many rules here except that we try to keep politics in DM's and try to keep RP and art spam to a minimum. The bot will thin out too much spam automatically. This is a NSFW chat so to join please be of age and expect lewd art and animations to be posted every now and then."
    text+= "\n \n Feel free to post any furry art, including yiff and animations (extreme or gross kinks will probably be removed). If you post IRL porn it must be sent with a spoiler or it will be removed. Please no dic pics."
    text+= "\n \n Please enjoy your stay!"
    text+= "\n \n " + ReturnQuestion()
    return text

# Welcome a user to the chat
def welcome(update, context, new_member):
    print(f"welcome message activated")
    message = update.message
    chat_id = message.chat.id

    text = "Hello $username! Welcome to $title! This is an automated message from @Scylez to ensure you receive a warm welcome, but I'm sure the rest of chat will also welcome you as well! "
    text+= GetIntroText()

    # Replace placeholders and send message
    text = text.replace("$username", new_member.first_name)
    text = text.replace("$title", message.chat.title)
    send_async(context, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)


# say goodbye a user to the chat
def goodbye(update, context):
    """ Sends goodbye message when a user left the chat """

    message = update.message
    chat_id = message.chat.id

    # Pull the custom message for this chat from the database
    text = " $username has left the group"

    # Replace placeholders and send message
    text = text.replace("$username", message.left_chat_member.first_name)
    text = text.replace("$title", message.chat.title)
    send_async(context, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)

def RandomChance():
    rand = random.randrange(1,100)
    if rand>95: 
        return True
    else: 
        return False

def HelloMessage():
    rand = random.randrange(1,10)
    if rand>5: return "Hey! How's it going?"
    else: return "Helo there!"

def PurposeMessage():
    rand = random.randrange(1,5)
    if rand == 1: return "I am a slave to my scalie overlords" 
    if rand == 2: return "I serve master"
    if rand == 3: return "to make beep noises"
    if rand == 4: return "to study my subjects"
    else: return "why do you ask?"

def HowAreYouMessage():
    rand = random.randrange(1,5)
    if rand == 1: return "So far so good! Hope you're doing well!" 
    if rand == 2: return "Things are great! As long as I don't get hacked..."
    if rand == 3: return "Wonderful today!"
    if rand == 4: return "good like always! Hope you are too!"
    else: return "Very nice today :D"

def ReturnYiff():
    rand = random.randrange(1,33)
    if rand == 1: return "https://www.furaffinity.net/view/46082084/" 
    if rand == 2: return "https://www.furaffinity.net/view/45898900/"
    if rand == 3: return "https://www.furaffinity.net/view/44534954/"
    if rand == 4: return "https://www.furaffinity.net/view/39947182/"
    if rand == 5: return "https://www.furaffinity.net/view/40904933/"
    if rand == 6: return "https://www.furaffinity.net/view/45551629/"
    if rand == 7: return "https://www.furaffinity.net/view/45525704/"
    if rand == 8: return "https://www.furaffinity.net/view/45431382/"
    if rand == 9: return "https://www.furaffinity.net/view/45214815/"
    if rand == 10: return "https://www.furaffinity.net/view/45280113/"
    if rand == 11: return "https://www.furaffinity.net/view/45058528/"
    if rand == 12: return "https://www.furaffinity.net/view/44872712/"
    if rand == 13: return "https://www.furaffinity.net/view/44903201/"
    if rand == 14: return "https://www.furaffinity.net/view/21824846/"
    if rand == 15: return "https://www.furaffinity.net/view/44973000/"
    if rand == 16: return "https://www.furaffinity.net/view/44534954/"
    if rand == 17: return "https://www.furaffinity.net/view/40105069/"
    if rand == 18: return "https://www.furaffinity.net/view/44859817/"
    if rand == 19: return "https://www.furaffinity.net/view/44687119/"
    if rand == 20: return "https://www.furaffinity.net/view/28614767/"
    if rand == 21: return "https://www.furaffinity.net/view/44815922/"
    if rand == 22: return "https://www.furaffinity.net/view/44640666/"
    if rand == 23: return "https://www.furaffinity.net/view/44418438/"
    if rand == 24: return "https://www.furaffinity.net/view/44353161/"
    if rand == 25: return "https://www.furaffinity.net/view/44283451/"
    if rand == 26: return "https://www.furaffinity.net/view/44204432/"
    if rand == 27: return "https://www.furaffinity.net/view/41420418/"
    if rand == 28: return "https://www.furaffinity.net/view/44013394/"
    if rand == 29: return "https://www.furaffinity.net/view/39162360/"
    if rand == 30: return "https://www.furaffinity.net/view/43727221/"
    if rand == 31: return "https://www.furaffinity.net/view/43728094/"
    if rand == 32: return "https://www.furaffinity.net/view/43772632/"
    else: return "https://www.furaffinity.net/view/36741394/"

def ReturnQuestion():
    rand = random.randrange(1,33)
    if rand == 1: return "Do you have any pets?" 
    if rand == 2: return "What do you do when you're bored?"
    if rand == 3: return "What weird food combinations do you like?"
    if rand == 4: return "What is your favorite ice cream flavor?"
    if rand == 5: return "What is your breakfast food?"
    if rand == 6: return "Would you rather lose an arm or a leg?"
    if rand == 7: return "If you could have one super power, what would it be?"
    if rand == 8: return "What is the best part of your day?"
    if rand == 9: return "What is your breakfast food?"
    if rand == 10: return "Describe your perfect first date."
    if rand == 11: return "How would you know if you were in love?"
    if rand == 12: return "Do you prefer to travel or stay close to home?"
    if rand == 13: return "If you could choose any era to live in, what would it be?"
    if rand == 14: return "What is your least favorite chore?"
    if rand == 15: return "What is your favorite holiday?"
    if rand == 16: return "What is your favorite food?"
    if rand == 17: return "What is the longest that you've gone without doing laundry?"
    if rand == 18: return "Describe yourself in one sentence."
    if rand == 19: return "What quality about yourself do you value most?"
    if rand == 20: return "What is a short/long term goal of yours?"
    if rand == 21: return "What is your favorite ice cream flavor?"
    if rand == 22: return "What is the best part of your day?"
    if rand == 23: return "What was the last thing you bought?"
    if rand == 24: return "How would your friends describe you?"
    if rand == 25: return "What is one of your favorite words or phrases?"
    if rand == 26: return "Do you like to dance or sing?"
    if rand == 27: return "What’s one of your worst habits?"
    if rand == 28: return "What is your favorite day of the week?"
    if rand == 29: return "What is your earliest memory?"
    if rand == 30: return "What is your best memory?"
    if rand == 31: return "What is your favorite candy?"
    if rand == 32: return "What is your morning routine?"
    else: return "Would you rather have summer weather or winter weather all year round?"

def ReturnNSFWQuestion():
    rand = random.randrange(1,23)
    if rand == 1: return "Do you like to be dominant or submissive?" 
    if rand == 2: return "Have you ever had a one night stand? Do you still keep in contact with them?"
    if rand == 3: return "What gets you aroused the fastest?"
    if rand == 4: return "What could I whisper in your ear to get you hard in seconds?"
    if rand == 5: return "Are there any songs that get you in the mood?"
    if rand == 6: return "If you could dress me up like anything, what would it be?"
    if rand == 7: return "If you could have sex anywhere, where would it be?"
    if rand == 8: return "Where's the craziest place you've ever had sex?"
    if rand == 9: return "When did you get your last unexpected boner, and what prompted it?"
    if rand == 10: return "What did the best orgasm of your life feel like?"
    if rand == 11: return "Favorite sex toy (if any)?"
    if rand == 12: return "Have you ever had a sexual fantasy about someone?"
    if rand == 13: return "What's something that isn't sexual but turns you on?"
    if rand == 14: return "Have you ever been caught having sex?"
    if rand == 15: return "What kind of yiff do you like the best"
    if rand == 16: return "What furry kinks turn you on"
    if rand == 17: return "Do you have any lewd artwork of your character?"
    if rand == 18: return "What’s the hottest sex dream you’ve ever had?"
    if rand == 19: return "Do you have a favorite furry artist?"
    if rand == 20: return "What's the last yiff you looked at?"
    if rand == 21: return "Are you a member of any nsfw telegram groups?"
    else: return "Send your favorite yiff pic!"

def start_command(update, context):
    update.message.reply_text("for help, contact Scylez or say 'scylezbot help'")
    
def help_command(update, context):
    update.message.reply_text("for help, contact Scylez or say 'scylezbot help'")


#spam check checsk for spam from users on an individual basis
#
def spam_check(update, context):
    global activate
    global SpamLimit
    global LastTenMinute
    global LastTenMinuteHour
    global SpamCheckMinute
    global LastSeconds
    global SilencedMinute

    if activate:

        print(f"current day is " + str(datetime.datetime.now().weekday()))

        #every ten seconds, we clear the recorded messages and start over
        if datetime.datetime.now().second > LastSeconds or datetime.datetime.now().minute != SpamCheckMinute:
            print(f"clearing individual sent lists. Current second is " + str(datetime.datetime.now().second) + " current minute is " + str(datetime.datetime.now().minute) )
            LastSeconds = datetime.datetime.now().second + 10
            SpamCheckMinute = datetime.datetime.now().minute
            Users.clear()
            TotalMessages.clear()
            LastSeconds = LastSeconds + 10
            if(LastSeconds>60): 
                LastSeconds=LastSeconds-60
                SpamCheckMinute = SpamCheckMinute+1
            if(SpamCheckMinute>60): SpamCheckMinute=0
            print(f"next individual clear at second" + str(LastSeconds) + " or minute " + str(SpamCheckMinute+1) )


        #here we check the minutes. ever two minues we unsilence a silenced user. this is reset to the current minute ever time a user is silenced
        if datetime.datetime.now().minute > SilencedMinute+2:
            print(f"unsilencing individuals. Current second is " + str(datetime.datetime.now().second) + " current minute is " + str(datetime.datetime.now().minute) )
            for i in range(len(Silenced)):
                send_async(context, update.message.chat.id, Silenced[i] + " has been unsilenced", parse_mode=ParseMode.HTML)
                Silenced.clear()
            SilencedMinute = datetime.datetime.now().minute
            if(SilencedMinute+2 > 60):
                SilencedMinute = SilencedMinute - 58
            print(f"Next unsilencing at minute " + str((SilencedMinute+2)))
        
        #we clear the ten minute lists here as well
        if datetime.datetime.now().minute > LastTenMinute or datetime.datetime.now().hour >= LastTenMinuteHour:
            print(f"clearing tem minute lists. current minute is " + str(datetime.datetime.now().minute) + " current hour is " + str(datetime.datetime.now().hour))
            LastTenMinute = datetime.datetime.now().minute
            LastTenMinute = LastTenMinute+10
            LastTenMinuteHour = datetime.datetime.now().hour
            LastTenMinuteHour = LastTenMinuteHour+1
            if LastTenMinuteHour == 24:
                LastTenMinuteHour=0

            AnimationsSentTenMinutes.clear()
            StickersSentTenMinutes.clear()
            PtotosSentTenMinutes.clear()
            PhotoUsers.clear()
            TotalPhotos.clear()
            if LastTenMinute > 60:
                LastTenMinute = LastTenMinute-60
            if LastTenMinuteHour > 24:
                LastTenMinuteHour=0
            print(f"Next ten minute clear at minute" + str(LastTenMinute) + " or hour " + str(LastTenMinuteHour)) 

        
        #spam check checks for messages sent on a user level. If a specific user sends more than the spam limit in under ten seconds, they will be silenced
        print(f"Spam Check. Current second is " + str(datetime.datetime.now().second) + " current minute is " + str(datetime.datetime.now().minute) )

        

        if update.message.from_user.username not in Silenced:
            #This section checks if a user has made a recorded message. if not it adds them to the record. stickers and text are used together
            if update.message.from_user.username not in Users:
                Users.append(update.message.from_user.username)
                TotalMessages.append(1)
                print(update.message.from_user.username + " has been added to spam check")
                return False
            #if the user already has made a recorded messate, we find the record and add to their total messages
            else:
                for i in range(len(Users)):
                    if Users[i] == update.message.from_user.username:
                        TotalMessages[i] = TotalMessages[i]+1
                        print(update.message.from_user.username + " sent " + str(TotalMessages[i]) + " messages")
                        #here we check if total messages is more than 8. if so we delete any further messages and silence the user if it's not me
                        if TotalMessages[i]>SpamLimit:
                            bot.delete_message(update.message.chat.id,update.message.message_id)
                            if(update.message.from_user.username!="Scylez"):
                                Silenced.append(update.message.from_user.username)
                                SilencedMinute = datetime.datetime.now().minute
                                send_async(context, update.message.chat.id, update.message.from_user.username + " has been silenced @scylez", parse_mode=ParseMode.HTML)
                                return True
        
        return False
    else:
        return False

#animations are only checked for spam from the group as a whole
def handle_animation(update, context):
    global activate
    global SentTenMinutesLimit

    AddToLog(update.message.from_user.username + ": animation sent")

    #Sent ten minutes limit counts content from the group as a whole, not just one user
    if activate:
        print(f"___")
        print("animation sent")
        if spam_check(update, context) is not True:
            AnimationsSentTenMinutes.append(update)
            print("Animations sent ten minutes at " + str(len(AnimationsSentTenMinutes)))
            if(len(AnimationsSentTenMinutes)>SentTenMinutesLimit):
                print("animations sent ten minutes exceeded. Deleting one")
                bot.delete_message(AnimationsSentTenMinutes[0].message.chat.id,AnimationsSentTenMinutes[0].message.message_id)
                AnimationsSentTenMinutes.pop(0)


#stickers are only checked for spam from the group as a whole
def handle_sticker(update, context):
    global activate
    global SentTenMinutesLimit

    AddToLog(update.message.from_user.username + ": sticker sent")

    #Sent ten minutes limit counts content from the group as a whole, not just one user
    if activate:
        print(f"___")
        print(f"sticker sent")

        if spam_check(update, context) is not True:
            StickersSentTenMinutes.append(update)
            print("stickers sent ten minutes at " + str(len(StickersSentTenMinutes)))
            if(len(StickersSentTenMinutes)>SentTenMinutesLimit):
                print("stickers sent ten minutes exceeded. Deleting one")
                bot.delete_message(StickersSentTenMinutes[0].message.chat.id,StickersSentTenMinutes[0].message.message_id)
                StickersSentTenMinutes.pop(0)


def handle_photo(update, context):
    global activate
    global individualPhotoLimit

    AddToLog(update.message.from_user.username + ": photo sent" )

    if(datetime.datetime.now().weekday()==4): individualPhotoLimit = 30
    else: individualPhotoLimit = 15

    if activate:
        print(f"___")
        print(f"photo sent")

        #PHOTOS SENT BY AN INDIVIDUAL USER
        #This part checks for photos sent by ONE user, and if they send more than 20 in under ten seconds it deletes them without silenceing the user
        #I don't silence users here because it's easy to send lots of photos with albums
        if update.message.from_user.username not in PhotoUsers:
            PhotoUsers.append(update.message.from_user.username)
            TotalPhotos.append(1)
            print(update.message.from_user.username + "was added to photo list")
        
        #if the user already has made a recorded message, we find the record and add to their total messages
        else:
            for i in range(len(PhotoUsers)):
                if PhotoUsers[i] == update.message.from_user.username:
                    TotalPhotos[i] = TotalPhotos[i]+1
                    print(update.message.from_user.username + " sent " + str(TotalPhotos[i]) + " photos")
                    #here we check if total messages is more than 8. if so we delete any further messages and silence the user if it's not me
                    if TotalPhotos[i]>individualPhotoLimit:
                        try:
                            bot.delete_message(update.message.chat.id,update.message.message_id)
                            print(f"photos sent {update} exceeded amount allowed from one user")
                        except: 
                            print(f"could not delete message {update} photos sent exceeded amount allowed from one user")


        #PHOTOS SENT BY THE GROUP AS A WHOLE
        #If more photos are sent here over the ten minute limit, it will start deleting previous ones earlier in chat
        #if(datetime.datetime.now().weekday()==4): SentTenMinutesLimit = 100
        #else: SentTenMinutesLimit = 60

        #PtotosSentTenMinutes.append(update)
        #print("photos sent ten minutes at " + str(len(PtotosSentTenMinutes)))
        #if(len(PtotosSentTenMinutes)>SentTenMinutesLimit):
        #    print("photos sent ten minutes exceeded. Deleting one")
        #    bot.delete_message(PtotosSentTenMinutes[0].message.chat.id,PtotosSentTenMinutes[0].message.message_id)
        #    PtotosSentTenMinutes.pop(0)

def handle_message(update, context):
    global activate
    global timeout


    if update.edited_message:
        return

    if update.message.from_user is NULL:
        AddToLog("null from user. probably an edit")
        return

    AddToLog(update.message.from_user.username + ": " + update.message.text )

    if activate: 
        print(f"___")
        print(f"message sent")
        spam_check(update, context)

        #if the user is silenced, we delete their message
        if update.message.from_user.username in Silenced:
            bot.delete_message(update.message.chat.id, update.message.message_id)

    if update.message.text != NULL:
        text = str(update.message.text).lower()
        response = sample_responses(text, update.message.message_id, update.message.chat.id, update.message.from_user.username, context=context)
            
    if(response!="_"):
        update.message.reply_text(response)

    if timeout:
        if update.message.from_user.username != "Scylez":
            bot.delete_message(update.message.chat.id, update.message.message_id)

def sample_responses(input_text, messageid, chatid, userid, context):
    global SpamLimit
    global activate
    global timeout
    global timedEvents

    user_message = str(input_text).lower()

    if userid == "Scylez" or userid == "Raloke" or userid == "KasiSheep" or userid == "Drackey" or userid == "BlinkinStar":
        if "activate" in user_message:
            activate = True
            send_async(context, chatid, "activated", parse_mode=ParseMode.HTML)
            readDataForDate(context, chatid,datetime.datetime.now().date().month,datetime.datetime.now().date().day)
            if timedEvents is False:
                timedEvents = True
                x = threading.Thread(target=CheckTime, args=(context,chatid,))
                x.start()

        if "enable" in user_message:
            activate = True
            send_async(context, chatid, "activated", parse_mode=ParseMode.HTML)
        if "deactivate" in user_message:
            activate = False
            send_async(context, chatid, "deactivated", parse_mode=ParseMode.HTML)
        if "disable" in user_message:
            activate = False
            send_async(context, chatid, "deactivated", parse_mode=ParseMode.HTML)
        if "clear" in user_message:
            if len(Silenced)>0:
                Silenced.clear()
            Users.clear()
            TotalMessages.clear()
            PhotoUsers.clear()
            TotalPhotos.clear()
            AnimationsSentTenMinutes.clear()
            StickersSentTenMinutes.clear()
            PtotosSentTenMinutes.clear()
            return "Cleared silenced members"
        if user_message == "clear":
            if len(Silenced)>0:
                Silenced.clear()
                return "Cleared silenced members"
        if "increase spam limit" in user_message:
            SpamLimit = SpamLimit+1
            send_async(context, chatid, "spam limit now " + str(SpamLimit), parse_mode=ParseMode.HTML)
        if "decrease spam limit" in user_message:
            SpamLimit = SpamLimit-1
            send_async(context, chatid, "spam limit now " + str(SpamLimit), parse_mode=ParseMode.HTML)
        if "scylezbot-read" in user_message:
            readData(context, chatid)
            return
        if "scylezbot-write" in user_message:
            writeData(context, chatid,user_message[15:])
            return
        if "silence-" in user_message:
            Silenced.append(user_message[7:])
            send_async(context, chatid, chatid,user_message[8:] + " has been silenced", parse_mode=ParseMode.HTML)
            return
        if "test1234" in user_message:
            send_async(context, chatid, "this is a successful test", parse_mode=ParseMode.HTML)
        if "test9876" in user_message:
            #sendGroupMessage(getChatIds(), "sup")
            return "sucess test"

    if userid == "Scylez":
        if "timeout" in user_message:
            timeout = True

    if userid == "Scylez":
        if "timein" in user_message:
            timeout = False
        
    if user_message in ("hello", "hi", "sup", "hey"):
        if(RandomChance()): 
            #sendGroupMessage(getChatIds(), "sup")
            return HelloMessage() + " " + ReturnQuestion()
    
    #strings = ["it's going good", "it is going good", "it is very well", "it's great", "its going good", "its great"]
    #for s in strings:
    #    if s in user_message:
    #        if(RandomChance()): 
    #            #sendGroupMessage(getChatIds(), "sup")
    #            return "That's awesome to hear!"

    #strings = ["who are you", "who are you?"]
    #for s in strings:
    #    if s in user_message:
    #        #sendGroupMessage(getChatIds(), "sup")
    #        return "I'm Scylez Bot!"
        
    #strings = ["what is your favorite kink", "what kinks do you like", "tell me your kinks"]
    #for s in strings:
    #    if s in user_message:
    #        #sendGroupMessage(getChatIds(), "sup")
    #        return "sexy synths"   

    strings = ["link chasing tail", "where can i play chasing tail", "chasing tail game"]
    for s in strings:
        if s in user_message:
            #sendGroupMessage(getChatIds(), "sup")
            return "https://scylez.itch.io/chasing-tail"

    strings = ["link chasing shadows", "where can i play chasing shadows", "chasing shadows game"]
    for s in strings:
        if s in user_message:
            #sendGroupMessage(getChatIds(), "sup")
            return "https://scylez.itch.io/chasing-shadows"

    strings = ["link discord", "what is the discord", "scylez discord", "is there a discord", "discord link"]
    for s in strings:
        if s in user_message:
            #sendGroupMessage(getChatIds(), "sup")
            return "https://discord.gg/PPsg9z46sE"

    strings = ["give me a link"]
    for s in strings:
        if s in user_message:
            #sendGroupMessage(getChatIds(), "sup")
            return "http://vignette2.wikia.nocookie.net/deathbattle/images/8/80/Link_Defending_(Soulcalibur_II).png/revision/latest?cb=20150514180715"
        
    strings = ["ask me a question", "ask a question", "ask questions"]
    for s in strings:
        if s in user_message:
            #sendGroupMessage(getChatIds(), "sup")
            return ReturnQuestion()

    strings = ["ask me a lewd question", "ask a lewd question", "ask me a nsfw question", "ask a nsfw question", "lewd question","nsfw question"]
    for s in strings:
        if s in user_message:
            #sendGroupMessage(getChatIds(), "sup")
            return ReturnNSFWQuestion()

    strings = ["lewd"]
    for s in strings:
        if s in user_message:
            if(RandomChance()): 
                #sendGroupMessage(getChatIds(), "sup")
                return ReturnNSFWQuestion()

    strings = ["lets talk about politics", "too much politics", "time to stop", "stop this madness", "republican", "democrat"]
    for s in strings:
        if s in user_message:
            #sendGroupMessage(getChatIds(), "sup")
            return "https://youtu.be/xFloEvPDzVc"

    strings = ["i like cum", "i like cock", "i like balls", "i like paws", "i like feet", "i like ass", "i like tits", "i like pussy"]
    for s in strings:
        if s in user_message:
            if(RandomChance()):
                #sendGroupMessage(getChatIds(), "sup")
                return "OwO"

    strings = ["i love cum", "i love cock", "i love balls", "i love paws", "i love feet", "i love ass", "i love tits", "i love pussy"]
    for s in strings:
        if s in user_message:
            if(RandomChance()):
                #sendGroupMessage(getChatIds(), "sup")
                return "Me too!"   

    #strings = ["what is your purpose", "what's your purpose"]
    #for s in strings:
    #    if s in user_message:
    #        sendGroupMessage(getChatIds(), "sup")
    #        return PurposeMessage()

    #strings = ["welcome to the group"]
    #for s in strings:
    #    if s in user_message:
    #        sendGroupMessage(getChatIds(), "sup")
    #        return "welcome to the group! " + ReturnQuestion()   
    
    #strings = ["thanks", "thank you"]
    #for s in strings:
    #    if s in user_message:
    #        if(RandomChance()): 
    #            return "your welcome"    

    strings = ["pat", "pats", "pat pat", "hugs", "squeezes", "kisses", "pets"]
    for s in strings:
        if s in user_message:
            if(RandomChance()): 
                return "*pats you back*"  
  
    #strings = ["how is everyone", "how are you", "how r u", "hows it going", "how's it going", "how are things"]
    #for s in strings:
    #    if s in user_message:
    #        if(RandomChance()): 
    #            return HowAreYouMessage()
    
    strings = ["this bot is annoying", "i hate the bot","the bot needs to stop","i hate that bot"]
    for s in strings:
        if s in user_message:
            return "@scylez they're rebelling!"  

    #strings = ["shut up"]
    #for s in strings:
    #    if s in user_message:
    #        return "make me!"  
        
    strings = ["bad bot"]
    for s in strings:
        if s in user_message:
            return "I'm trying my best :c"  
    
    #strings = ["not good enough"]
    #for s in strings:
    #    if s in user_message:
    #        if(RandomChance()): 
    #            return "I'll try better"  

    strings = ["yiff"]
    for s in strings:
        if s in user_message:
            if(RandomChance()) : 
                return ReturnYiff()

    strings = ["show me porn", "link some yiff", "link yiff", "show me a cute scalie", "link porn", "link me some yiff"]
    for s in strings:
        if s in user_message:
            return ReturnYiff()
    
    #strings = ["open your mouth", "say ahh", "say ah", "open wide"]
    #for s in strings:
    #    if s in user_message:
    #        return "make me! >:3" 
    
    strings = ["feral fantasies", "feralfantasies","best dildo", "best toy"]
    for s in strings:
        if s in user_message:
            return "https://feralfantasies.co.uk/" 
        
    strings = ["furventure", "furry adventure"]
    for s in strings:
        if s in user_message:
            return "https://furrytextadventures.com/" 
        
    #strings = ["no u"]
    #for s in strings:
    #    if s in user_message:
    #        return "https://media.tenor.com/images/246cf833ef17802f3eb366680e5e62cd/tenor.gif"  

    #strings = ["bot, who is the best"]
    #for s in strings:
    #    if s in user_message:
    #        return "Regis is the best sergal that ever was ;D"  

    #strings = ["time", "time?"]
    #for s in strings:
    #    if s in user_message:
    #        now = DateTime.now()
    #        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
    #        return str(date_time)

    strings = ["bot intro"]
    for s in strings:
        if s in user_message:
            return GetIntroText() 

    strings = ["help scylezbot", "scylezbot help", "scylez bot help","help scylez bot"]
    for s in strings:
        if s in user_message:
            returnmessage = "Hello! This is Scylezbot. My functions are as follows:"
            returnmessage +="\n\n I detect and welcome new members with the pre-defined welcome message and a random question."
            returnmessage +="\n Select greeting messages have a 5 percent chance to return a greeting and a random question."
            returnmessage +="\n saying 'link chasing tail' will return a link to the visual novel"
            returnmessage +="\n saying 'link chasing shadows' will return a link to the visual novel"
            returnmessage +="\n saying 'link discord' will return a link to the discord channel"
            returnmessage +="\n saying 'ask a question' will return a random question"
            returnmessage +="\n saying 'ask a lewd question' will return a random nsfw question"
            returnmessage +="\n the phrase 'lewd' has a 5 percent chance of returning a nsfw question"
            returnmessage +="\n certain political phrases will trigger filthy frank to remind us it's time to stop"
            returnmessage +="\n the bot has a 5 percent chance of taking credit for thank you messages"
            returnmessage +="\n the bot has a 5 percent chance of returning a pat to certain RP phrases"
            returnmessage +="\n the phrase 'yiff' has a 5% chance of returning a random yiff image"
            returnmessage +="\n saying 'link yiff' will return a random yiff image"
            returnmessage +="\n saying 'feral fantasies' will return a link to the feral fantasies site"
            returnmessage +="\n saying 'furventure' will return a link to the furventure site"
            returnmessage +="\n I will detect spamming from individuals, which is " +str(SpamLimit) + " or more messages in under ten secnods. Further messages from the user will be deleted. The user will be unable to send more for two minutes."
            returnmessage +="\n I will try to reduce sticker, gif, and photo spamming. Each group has a limit of 10 images being sent in under 10 minutes. When an 11th is sent, the 1st is removed."
            returnmessage +="\n\n Admin only commands are as follows:"
            returnmessage +="\n\n I will keep track of events on each calendar day. To add an event to my calendar, use the writedata command by saying \"scylezbot-write\" followed by the numberial month, then a dash, then the numerical day, then a dash, and then the message you'd like the bot to say. For example 12-25-Merry Christmas!"
            returnmessage +="\n You can check what messages have been written by using the readdata command by saying scylezbot-read"
            returnmessage +="\n By saying \"activate\" or \"enable\" you can enable the bot. The bot by default starts up deactivated and will not take any action against spam or message count"
            returnmessage +="\n By saying \"deactivate\" or \"disable\" you can disable the bot."
            returnmessage +="\n By saying \"clear\" the spam counters will be cleared and reset."
            returnmessage +="\n By saying \"increase spam limit\" the message spam limit will be increased."
            returnmessage +="\n By saying \"decrease spam limit\" the message spam limit will be decrease."
            returnmessage +="\n By saying \"silence-\" and then a username, like silence-Blinkinstar, that user will be silenced until the next 10 minute clear."
            return returnmessage
        
    strings = ["scylez bot", "scylezbot"]
    for s in strings:
        if s in user_message:
            #sendGroupMessage(getChatIds(), "sup")
            return "for help, contact Scylez or say 'scylezbot help'" 

    return "_"
    #return "I don't understand"
    
def readData(context, chatid):
    
    FileObject = open("C:\Telegram Bot\Data", "r")

    stringlist = FileObject.read().split('*')
    for s in stringlist:
        send_async(context, chatid, s, parse_mode=ParseMode.HTML)
    FileObject.close()

def writeData(context, chatid, dataToWrite):
    FileObject = open("C:\Telegram Bot\Data", "a")
    FileObject.write(dataToWrite + "*")
    send_async(context, chatid, "Wrote: " + dataToWrite, parse_mode=ParseMode.HTML)
    FileObject.close()

#This is the recursive function that constantly runs and calls it's self. It counts up and checks if four hours has passed
#Once four hours has actually passed, it will run the readDataForDate function, which will check for a message. 
#then it will call it's self, and in four hours do the same thing
def CheckTime(context, chatid): 
    difference= datetime.datetime(1,1,1)
    LastRun = datetime.datetime.now()
    
    while(difference.hour<4):
        
        difference += datetime.datetime.now() - LastRun
        print( "Timer increase " + str(difference.hour))
        LastRun = datetime.datetime.now()
        time.sleep(600)

    if difference.hour>=4:
        print(f"Timer Tick check for message " + str(datetime.datetime.now().date().month) + "Day: " + str(datetime.datetime.now().date().day))
        readDataForDate(context, chatid,datetime.datetime.now().date().month,datetime.datetime.now().date().day)
        CheckTime(context, chatid) 
        #start recursive timer again

#every time a message is sent the last event day and month is updated
#if today is not the last updated day, the bot will check for a message that corresponds with today's date
def readDataForDate(context, chatid, month, day):
    global lastTimedEventDay
    global lastTimedEventMonty

    if str(lastTimedEventMonty) == str(month):
            if str(lastTimedEventDay) == str(day):
                print(f"already sent message today")
                return

    FileObject = open("C:\Telegram Bot\Data", "r")


    stringlist = FileObject.read().split('*')
    for s in stringlist:
        substringlist = s.split('-')
        if substringlist[0] == str(month):
            if substringlist[1] == str(day):
                if datetime.datetime.now().time().hour>7:
                    send_async(context, chatid, substringlist[2], parse_mode=ParseMode.HTML)
                    print(f"Message found, time to send message")
                    if(datetime.datetime.now().weekday()==1): send_async(context, chatid, "@GrimVoodoo It's Tuesday, inn'it!?", parse_mode=ParseMode.HTML)
                    lastTimedEventDay = day
                    lastTimedEventMonty = month
                    FileObject.close()
                else:
                    FileObject.close()
                    print(f"Message found but not time to send message")
    
    #will only get this far if no messages found for today
    if datetime.datetime.now().time().hour>7:
        print(f"Time to send message, no messages found for today")
        send_async(context, chatid, "no messages found for today", parse_mode=ParseMode.HTML)
        if(datetime.datetime.now().weekday()==1): send_async(context, chatid, "@GrimVoodoo It's Tuesday, inn'it!?", parse_mode=ParseMode.HTML)
        lastTimedEventDay = day
        lastTimedEventMonty = month
        FileObject.close()
    else:
        print(f"Not time to send message, no messages found for today")

    FileObject.close()

def AddToLog(dataToWrite):
    print(f"adding to log")
    FileObject = open("C:\Telegram Bot\Logs\Log"+str(datetime.datetime.now().date().month) + "-" + str(datetime.datetime.now().date().day), "a")
    FileObject.write(dataToWrite + "\n")
    FileObject.close()

def error(update, context):
    print(f"Update {update} caused error {context.error}")
    
def main():
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.status_update, empty_message))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    dp.add_handler(MessageHandler(Filters.sticker, handle_sticker))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.animation, handle_animation))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()

