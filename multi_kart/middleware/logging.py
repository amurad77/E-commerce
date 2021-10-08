from django.utils.deprecation import MiddlewareMixin
from datetime import datetime

class LoggingListMiddleware(MiddlewareMixin):

    def process_response(self, request,response):
        req = request.META.get("HTTP_USER_AGENT")
        date_time = datetime.now().strftime ("%m/%d/%Y")
        res = response.status_code
        with open ('multi_kart/logging.txt','a') as g :
            g.writelines(f'{date_time}, {req}, {res}\n')
        return response