#!/usr/bin/python3
from time import sleep
import argparse

class Main():

    bot = None
    update_id = None

    bot_token = 'YOUR TELEGRAM BOT TOKEN HERE'

    def __init__(self):
        """Run the bot."""
        # Telegram Bot Authorization Token
        self.bot = telegram.Bot(self.bot_token)

        try:
            self.update_id = self.bot.get_updates()[0].update_id
        except IndexError:
            self.update_id = None

        print(self.bot)


    def get_chats_id(self):
        """
        This method print every single message that was sent to the bot,
        Here you get the Chat ID, Username or Firstname and the message send as output

        This should be used when the chat id is not known, there you can run it, to get it
        """
        for update in self.bot.get_updates():
            print('id: ' + str(update.message.chat.id) +
                  ', User/First Name: ' + str(update.message.chat.first_name) +
                  ', Message:' + str(update.message.text))

        print("If you are not listed, send a message to the bot")

    def send_picture(self, image, chat_ids):
        """
        This method will send a message with an image to every chat provided.
        The message text is random.

        :param image:
        :param chat_ids:
        :return:
        """

        for chat in chat_ids:
            while True:
                try:
                    self.bot.send_photo(chat_id=chat, photo=open(image, 'rb'))
                    print('Picture send to ' + str(chat))
                    break
                except NetworkError:
                    sleep(1)
                except Unauthorized:
                    # The user has removed or blocked the bot.
                    self.update_id += 1

    def send_message(self, text, chat_ids):
        """
        This method will send a message with an image to every chat provided.
        The message text is random.

        :param image:
        :param chat_ids:
        :return:
        """

        for chat in chat_ids:
            while True:
                try:
                    self.bot.send_message(chat_id=chat, text=text, parse_mode=telegram.ParseMode.MARKDOWN)
                    print('Message send to ' + str(chat))
                    break
                except NetworkError:
                    sleep(1)
                except Unauthorized:
                    # The user has removed or blocked the bot.
                    self.update_id += 1


if __name__ == '__main__':
    try:
        import telegram
        from telegram.error import NetworkError, Unauthorized
    except BaseException:
        print('You need to install python telegram: pip3 install python-telegram-bot')
        exit()

    parser = argparse.ArgumentParser(description='Send images trough telegram to a user')
    parser.add_argument('-g', '--get-chats', type=str, default=False, help='Get Chats ID from all Users')
    parser.add_argument('-i', '--image', type=str, help='Image to send')
    parser.add_argument('-m', '--message', type=str, help='Send text message')
    parser.add_argument('-c', '--chat', nargs='+', default=[],
                        help='Provide Chat Id to send image or text to them, example: -c 123456 123456')
    args = parser.parse_args()

    tg = Main()
    if args.message and args.chat:
        tg.send_message(args.message, args.chat)
    if args.image and args.chat:
        tg.send_picture(args.image, args.chat)
    if args.get_chats:
        tg.get_chats_id()



