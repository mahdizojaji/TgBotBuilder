import requests

from config.settings import TG_BOT_MANAGER_TOKEN


class TelegramMethod:
    def __init__(self, token=None):
        self.token = token or TG_BOT_MANAGER_TOKEN
        if not self.token:
            raise ValueError('token is None')
        self.base_url = 'https://api.telegram.org'

    @staticmethod
    def prepare_data(data):
        return {k: v for k, v in data.items() if v is not None}

    def _req(self, method_name, data, files):
        url = f'{self.base_url}/bot{self.token}/{method_name}'
        data = self.prepare_data(data=data)
        files = self.prepare_data(data=files)
        return requests.post(url=url, data=data, files=files)

    def get_me(self):
        method_name = 'getMe'
        data = {}
        files = {}
        return self._req(method_name=method_name, data=data, files=files).json()

    def set_webhook(self, url, certificate=None, ip_address=None, max_connections=None, allowed_updates=None,
                    drop_pending_updates=None):
        method_name = 'setWebhook'
        data = {
            'url': url,
            'ip_address': ip_address,
            'max_connections': max_connections,
            'allowed_updates': allowed_updates,
            'drop_pending_updates': drop_pending_updates,
        }
        files = {
            'certificate': certificate,
        }
        return self._req(method_name=method_name, data=data, files=files).json()

    def send_message(self, chat_id, text, parse_mode=None, entities=None, disable_web_page_preview=None,
                     disable_notification=None, reply_to_message_id=None, allow_sending_without_reply=None,
                     reply_markup=None):
        method_name = 'sendMessage'
        data = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': parse_mode,
            'entities': entities,
            'disable_web_page_preview': disable_web_page_preview,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'allow_sending_without_reply': allow_sending_without_reply,
            'reply_markup': reply_markup,
        }
        files = {}
        return self._req(method_name=method_name, data=data, files=files).json()
