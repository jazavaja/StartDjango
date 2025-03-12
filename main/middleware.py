import json
from datetime import datetime


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        log_data = {
            'method': request.method,
            'path': request.path,
            'timestamp': datetime.now().isoformat(),
            'ip': self.get_ip(request)
        }
        self.save_log(log_data)
        response = self.get_response(request)
        return response

    def get_ip(self, request):
        http_x = request.META.get('HTTP_X_FORWARDED_FOR')
        if http_x:
            ip = http_x.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def save_log(self, log_data):
        file_name = 'request_logs.json'
        logs = []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                logs = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            logs = []

        logs.append(log_data)
        with open(file_name, 'w', encoding='utf-8') as log_file:
            json.dump(logs, log_file, indent=2)
