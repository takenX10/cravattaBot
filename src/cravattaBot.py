from botsistemi_data import *
import telepot
from telepot.loop import MessageLoop
import eel

eel.init('web')
bot = telepot.Bot(token)

# telegram handler
def telegram_message_handler(msg):
    if(debug_print):
        print("Telegram received a message.")
    if(chatid != -1):
        bot.sendMessage(chatid, msg['text'])
        if(debug_print):
            print('Message sent on forward chat')
    eel.message_received(msg['text'], autoscroll)
    if(debug_print):
        print('Message added to eel')

# Main
def main():    
    MessageLoop(bot, telegram_message_handler).run_as_thread()
    print('Listening telegram messages...')
    eel.start('index.html')

if __name__ == "__main__":
    main()
