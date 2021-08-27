from extensions.http_requests import TelegramMethod


class ManagerStartCommand:
    def __init__(self, tg, update):
        self.tg: TelegramMethod = tg
        self.update: dict = update
        self.message = self.update['message']
        self.message_id = self.message['message_id']
        self.chat = self.message['chat']
        self.chat_type = self.chat['type']
        self.chat_id = self.chat['id']

    def run(self):
        text = """
        به ربات ساز خوش آمدید.
        """
        if self.chat_type == 'private':
            return self.tg.send_message(
                chat_id=self.chat_id,
                text=text,
                reply_to_message_id=self.message_id,
                allow_sending_without_reply=True,
            )
