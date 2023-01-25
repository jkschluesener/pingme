'''
PingMe
A simple python class to send a telegram notification via a bot.

Jan K. Schluesener
github.com/jkschluesener/pingme
MIT License
'''

import requests

class PingMe:
    """Send a short message using a telegram bot.
    You need to have a telegram api key and a chat id.
    Supports Markdown formatting

    Supply the api-key and chat-id during initialization,
    then send messages using the `ping` function.
    See keyword arguments to silence notifications and set timeout.

    Jan K. Schluesener
    github.com/jkschluesener/pingme
    MIT License
    """


    def __init__(self, apikey: str, chatid: str) -> None:
        """Class Initialization.
        Set the apikey and chatid to be used for message delivery.

        Parameters
        ----------
        apikey : str
            Telegram bot HTTP API key
        chatid : str
            Target Chat ID
        """

        self.apikey = apikey
        self.chatid = chatid


    def ping(self, message: str, silent: bool=True, timeout_sec: int=5) -> None:
        """_summary_

        Parameters
        ----------
        message : str
            Message to send, with optional markdown formatting
        silent : bool, optional
            Whether a message should ring or be silent, by default True
        timeout_sec : int, optional
            Maximum time to wait for a HTTP response, in seconds, by default 5
        """

        url = f'https://api.telegram.org/bot{self.apikey}/sendMessage'

        head = {
            'accept': 'application/json',
            'content-type': 'application/json'
            }

        data = {
            'text': message,
            'disable_notification': silent,
            'chat_id': self.chatid,
            'parse_mode': 'markdown',
            'disable_web_page_preview': True,
            'reply_to_message_id': None
            }

        response = requests.post(url,
                                 headers=head,
                                 json=data,
                                 timeout=timeout_sec)

        return response.json()['ok']
