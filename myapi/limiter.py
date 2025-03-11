import time

from django.core.cache import cache
from rest_framework.throttling import BaseThrottle


class CustomLimiterThrottler(BaseThrottle):
    def __init__(self):
        self.rate = '100/minute'
        self.request = None

    def parse_rate(self, rate):
        if rate is None:
            return None, None
        num, period = rate.split('/')
        num_request = int(num)
        duration_dic = {'second': 1, 'minute': 60, 'hour': 3600, 'day': 86400}
        if period not in duration_dic:
            raise ValueError('Wrong Time Period In Setting Throttler CustomLimiterThrottler Option Available day,hour,'
                             'minute,second')
        duration = duration_dic[period]
        return num_request, duration

    def get_ip_address(self, request):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip_address:
            ip_address = ip_address.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')
        return ip_address

    def allow_request(self, request, view):
        num_request, duration = self.parse_rate(self.rate)
        self.request = request
        ip_address = self.get_ip_address(request)

        cache_key = f'throttler_{ip_address}'
        expire_key = f'expire_throttler__{ip_address}'

        requested_cache = cache.get(cache_key, 0)
        if requested_cache < num_request:
            cache.set(cache_key, requested_cache + 1, timeout=duration)

            cache.set(expire_key, time.time() + duration, timeout=duration)
            return True
        else:
            return False

    def wait(self):
        ip = self.get_ip_address(self.request)

        expire_key = f'expire_throttler__{ip}'
        expire_time = cache.get(expire_key)
        remind_time = int(expire_time - time.time())
        print("remind_time: ", remind_time)
        if remind_time <= 0 or remind_time is None:
            return None
        return remind_time
