# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ipware.ip import get_ip
from .models import EdxRateLimitConfiguration
from importlib import import_module

ALL = (None,)


def real_ip(group, request):
    return get_ip(request)


def get_ratelimit_conf():
    conf = EdxRateLimitConfiguration.objects.all().first()
    if conf:
        if conf.request_frequency:
            rate = str(conf.request_frequency) + conf.time_window_duration

        block = bool(conf.block),
        methods = conf.methods.split(',')
        method = ALL if 'ALL' in methods else methods
        ip_whitelist = conf.ip_whitelist

        return {
            'rate': rate,
            'block': block,
            'method': method,
            'ip_whitelist': ip_whitelist
        }
    return None


def get_whitelist_rate(request, key, group, ip_whitelist):
    ip = None
    if callable(key):  # direct function call to get key
        ip = key(group, request)
    elif '.' in key:  # path of the function inside some package
        mod, attr = key.rsplit('.', 1)
        keyfn = getattr(import_module(mod), attr)
        ip = keyfn(group, request)

    # get whitelist rate if applicable or resort to db configured rate
    if ip in ip_whitelist:
        return ip_whitelist[ip]
    else:
        return None
