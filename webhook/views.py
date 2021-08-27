from rest_framework.views import APIView, Response

from extensions.http_requests import TelegramMethod


class ManagerWebHookListener(APIView):
    def post(self, request):
        print(request.data)
        return Response()
