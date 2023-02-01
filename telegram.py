import json
import os
import requests
import time
import logging
from pprint import pprint



class Telegram:
    def __init__(self):
        self.URL = "https://api.telegram.org/bot"
        self.token = self.get_token()
        self.whitelist = self.get_whitelist()

        # ignore all previous messages until now
        done = False
        while not done:
            try:
                self.offset_id = self.get_updates(update_offset=False)[-1]['update_id']
            except IndexError:
                print("\nPlease send a telegram message for things to work\n")
            else:
                done = True

    def send_image(self, image_path, text):

        url = self.URL + self.token + "/sendPhoto"
        files = {'photo': open(image_path, 'rb')}

        # Send image only to whitelisted users
        for user_id in json.loads(self.whitelist):

            data = {'chat_id': user_id, 'caption': text}
            r = requests.post(url, files=files, data=data)

            if int(r.status_code) == 200:
                print("Image sent to " + str(user_id) + ".")
            else:
                print("FAILED to send image to " + str(user_id))

    def send_option_keyboard(self, keyboard):

        url = self.URL + self.token + "/sendMessage"
        reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}

        # Send only to whitelisted users
        for user_id in json.loads(self.whitelist):
            text = {'text': "Accept or veto trade:", 'chat_id': user_id, 'reply_markup': reply_markup}

            r = requests.post(url, json=text)

            if int(r.status_code) == 200:
                print("Consent query sent to " + str(user_id) + ".")
            else:
                print("Sending consent query to " + str(user_id) + " failed.")
                print(r.status_code)
                print(r.json())

    def send_message(self, text, user_id: int = None):
        url = self.URL + self.token + "/sendMessage"

        if not user_id:
            # Send message only to whitelisted users
            for user_id in self.whitelist:

                result = None
                while result is None:
                    try:
                        result = requests.post(url, data={'chat_id': user_id, 'text': text})
                    except ConnectionError:
                        print("Sending message to " + str(user_id) + " failed. Trying again...")

                if int(result.status_code) == 200:
                    print(f"Text message sent to {str(user_id)}:\n'{text}'")

                else:
                    print(f"Sending message to {str(user_id)} failed:")
                    print(result.json())
        else:
            result = None
            while result is None:
                try:
                    result = requests.post(url, data={'chat_id': user_id, 'text': text})
                except ConnectionError:
                    print("Sending message to " + str(user_id) + " failed. Trying again...")

    def send_document(self, document, user_id: int = None):
        """Sends a document. Input document must be the path string for the document's directory."""
        url = self.URL + self.token + '/sendDocument'

        if not user_id:
            raise Exception("telegram.send_document() not implemented without providing a user_id. Need to pass user_id as param.")
            for user_id in self.whitelist:
                response = None
                tries = 0
                while response is None:
                    doc = open(document, 'rb')
                    try:
                        response = requests.post(url, data={'chat_id': user_id}, files={'document': doc})
                    except ConnectionError:
                        print("Sending message to " + str(user_id) + " failed. Trying again...")
        else:
            response = None
            tries = 0
            while response is None:
                doc = open(document, 'rb')
                try:
                    response = requests.post(url, data={'chat_id': user_id}, files={'document': doc})
                except ConnectionError:
                    print("Sending message to " + str(user_id) + " failed. Trying again...")

    def get_updates(self, update_offset=True):
        url = self.URL + self.token + "/getUpdates"

        if update_offset:
            result = None
            while result is None:
                try:
                    result = requests.get(url, data={'offset': self.offset_id}).json()
                except ConnectionError:
                    print("Retreiving Telegram updates failed. Trying again...")
            # Update offset_id to consume all received updates except last one
            try:
                self.offset_id = result['result'][-1]['update_id']
            except:
                pass
        else:
            result = None
            while result is None:
                try:
                    result = requests.get(url).json()
                except ConnectionError:
                    print("Retreiving Telegram updates failed. Trying again...")

        return result['result']

    def check_whitelist(self, user_id):
        """Checks whether a given user_id is in the whitelist."""
        return user_id in self.whitelist

    def get_token(self, config):
        """
        Load bot token from environment variable.
        """

        if config.get('telegram bot').get('token') is None:
            raise Exception("Telegram bot token missing in config")
        else:
            return config.get('telegram bot').get('token')

    def get_whitelist(self, config):
        """
        Load whitelist from environment variable.
        """

        if config.get('telegram bot').get('whitelist') is None:
            raise Exception("Telegram bot user whitelist missing in config")
        else:
            return config['telegram bot']['whitelist']

