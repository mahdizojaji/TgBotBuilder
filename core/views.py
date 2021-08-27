from django.shortcuts import reverse
from django.http import HttpRequest

from rest_framework.views import APIView, Response

from extensions import telegram_types
from extensions.http_requests import TelegramMethod


class RunManagerBot(APIView):
    def get(self, request: HttpRequest):
        tg = TelegramMethod()
        webhook_url = request.build_absolute_uri(reverse("webhook:webhook_manager")).replace('http://', 'https://')
        webhook_result = tg.set_webhook(
            url=webhook_url, allowed_updates=telegram_types.Update.ALL, drop_pending_updates=True
        )
        return Response(webhook_result)
