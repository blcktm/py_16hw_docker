from django.utils.deprecation import MiddlewareMixin
from core.models import Logger
import time


class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        if not request.path.startswith('/admin/'):
            time_diff = time.time() - request.start_time
            Logger.objects.create(request_path=request.path, request_method=request.method, execution_time=time_diff)
        return response
