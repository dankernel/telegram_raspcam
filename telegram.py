#-*- coding: utf-8 -*-

import os
import sys
import time
import telepot
import datetime
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Press me', callback_data='press')],
    ])

    # Print
    print datetime.datetime.now(), 'Get : ', chat_id, ' ', msg['text'];

    if chat_id != '*** chat_id ***':
        bot.sendMessage(chat_id, '승인된 사용자가 아닙니다.')
        print datetime.datetime.now(), chat_id, '거부';
        return;

    if msg['text'] == "get_cam":

        # Run Cam
        bot.sendMessage(chat_id, '사진 촬영중...')
        print datetime.datetime.now(), '사진 촬영중';
        os.system('raspistill -t 1 -o img.jpg -w 1296 -h 730 -rot 90')

        # Image
        f = open('./img.jpg', 'rb')
        bot.sendMessage(chat_id, '사진 전송중... 잠시만 기다려 주세요.')
        print datetime.datetime.now(), '사진 전송중';
        bot.sendPhoto(chat_id, f)
        f.close()

        # Messge
        bot.sendMessage(chat_id, '사진 수신 완료')
        print datetime.datetime.now(), '사진 전송 완료';
    else :
        print datetime.datetime.now(), '알수없는 명령';
        bot.sendMessage(chat_id, '올바른 요청을 주세요!')

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message})
print('Listening ...')

while 1:
    time.sleep(2);
