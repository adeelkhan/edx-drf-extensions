from __future__ import absolute_import
from functools import wraps
from django.http import HttpRequest, JsonResponse
from ratelimit import ALL
from ratelimit.utils import is_ratelimited
from edx_rest_framework_extensions.ratelimit.utils import get_whitelist_rate, get_ratelimit_conf
import logging

__all__ = ['ratelimit']


def edxratelimit(group=None, key=None):

    def decorator(fn):
        @wraps(fn)
        def _wrapped(*args, **kw):
            # Work as a CBV method decorator.
            if isinstance(args[0], HttpRequest):
                request = args[0]
            else:
                request = args[1]
            request.limited = getattr(request, 'limited', False)

            conf = get_ratelimit_conf()

            if conf:
                ip_whitelist_rate = get_whitelist_rate(request, key, group, conf['ip_whitelist'])
                rate = ip_whitelist_rate if ip_whitelist_rate else conf['rate']
            else:
                rate = '5/m'
            block = conf['block'] if conf['block'] else True
            method = conf['method'] if conf['method'] else ALL
            print rate

            ratelimited = is_ratelimited(request=request, group=group, fn=fn,
                                         key=key, rate=rate, method=method,
                                         increment=True)
            if ratelimited and block:
                logging.exception('Too many request: Ratelimit of {} exceeded'.format(rate))
                # add log to NR
                return JsonResponse(data={
                    'message': 'Too many request: Ratelimit of {} exceeded'.format(rate),
                    'status': False
                }, status=429)
            return fn(*args, **kw)
        return _wrapped
    return decorator

