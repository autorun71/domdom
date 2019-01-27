from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin
import datetime
class WhiteNoiseMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # request.timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        response = self.get_response(request)

        self.process_exception(request, response)
        self.logs(request, response)
        return response



    def process_exception(self, request, exception):

        # print(exception.status_code)
        return 1

    def logs(self, request, exception):
        logs = open('logs/server_logs.txt', 'a', encoding='utf-8')
        all_logs = str(datetime.datetime.now())[:19] + "||IP: " + str(
            request.META['REMOTE_ADDR']) + " || " + str(exception.status_code) + " URL: " + request.get_full_path() + "\n"
        logs.write(all_logs)
        return True