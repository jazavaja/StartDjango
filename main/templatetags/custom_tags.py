from django import template

register = template.Library()


@register.simple_tag
def custom_time(date_format, seperator, time_format):
    from datetime import datetime
    dd = datetime.now().strftime(date_format)
    tt = datetime.now().strftime(time_format)
    return f"{dd} {seperator} {tt}"
