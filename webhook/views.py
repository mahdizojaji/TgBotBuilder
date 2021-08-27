import re
from rest_framework.views import APIView, Response

import actions
from extensions import http_requests


class ManagerWebHookListener(APIView):
    def post(self, request):
        tg = http_requests.TelegramMethod()
        update = request.data
        if message := update.get('message'):
            if text := message.get('text'):
                if re.search('^/start$', text):
                    actions.ManagerStartCommand(tg, update).run()
        return Response()
