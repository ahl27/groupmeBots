import requests
import time
import random
from tokens import *

request_params = {'token': GROUPME_TOKEN}
turn_off = False
chance = 0.1
generated_text = False

def print_stuff(st):
    post_params = {'bot_id':BOT_ID, 'text': st}
    requests.post('https://api.groupme.com/v3/bots/post', params=post_params)

old_msg = ''
while True:
    response_messages = requests.get('https://api.groupme.com/v3/groups/' + GROUP_ID + '/messages', params = request_params).json()['response']['messages']
    '''
    if response == 200:
        print('something')
        response_messages = response.json()['response']['messages']

    else:
        print('nothing')
        continue
    '''

    msg = ''
    message = response_messages[0]['text']

    if generated_text:
        old_msg = message
        generated_text = False
        continue
    if message == old_msg:
        continue


    if 'shut up bot' in message:
        time.sleep(1)
        print_stuff("Got the message--I'll stop talking for a bit. Reply with 'come back bot' to turn me back on.")
        turn_off = True
        generated_text = False
        continue

    elif 'come back bot' in message:
        msg = "I'm back! Sorry for leaving."
        turn_off = False
    elif 'canada' in message or 'Canada' in message:
        #handle message
        msg = "That's what I'm talkin' aboot! Sorry for yelling."
    elif 'bot chance = ' in message:
        try:
            x = float(message[-4:])
            if x <= 1 and x >= 0:
                msg = 'Okay. Changed chance to print to ' + str(x)[0:5]
                chance = x
            else:
                msg = 'Sorry, that value isn\'t legal. Put in a value between 0.00 and 1.00.'
        except ValueError:
            msg = "Sorry, that value isn't legal. Put in a value between 0.00 and 1.00"
    elif 'about' in message:
        msg = message.replace("about", "aboot")
    elif 'bot help info' in message:
        msg = "Help:\n \
                {SHUT UP BOT}: Turn me off \n \
                {COME BACK BOT}: Turn me back on \n \
                {CANADA}: print my message! \n \
                {BOT CHANCE = x.xx}: sets chance of printing something to x.xx. Must be 3 digits, 2 decimals.\n \
                Print stuff in lowercase please!"
    else:
        roll = random.random()
        if roll < chance:
            newroll = random.random()
            if newroll < 0.75:
                msg = 'sorry :('
            else:
                msg = 'aboot xD'


    time.sleep(1)

    if not turn_off:
        print_stuff(msg)
        if msg != '':
            generated_text = False

    old_msg = message
    




