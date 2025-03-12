import json
from datetime import datetime
from django.http import HttpResponseForbidden
import requests


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


class BlockIpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_list = []

    def get_ip(self, request):
        http_x = request.META.get('HTTP_X_FORWARDED_FOR')
        if http_x:
            ip = http_x.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def list_country_block(self):
        block_list = [
            'SE', 'IT', 'DE'
        ]
        return block_list

    def __call__(self, request):
        # my_ip = self.get_ip(request)
        my_ip = '2.56.28.0'
        url = f'https://ipinfo.io/{my_ip}?token=77ffa2ec464e8f'
        try:
            result = requests.get(url)
            json_result = result.json()
            print(json_result['country'])
            if json_result['country'] in self.list_country_block():
                return HttpResponseForbidden("Access to the site for users in Italy, Sweden, and Germany is banned.")

        except:
            print('We can not request get from url ipinfo')
        response = self.get_response(request)
        return response
