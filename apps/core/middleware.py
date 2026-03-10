"""
core/middleware.py — Custom middleware for request/response logging.
"""
import logging
import time

logger = logging.getLogger('apps.core')


class RequestLoggingMiddleware:
    """
    Logs every incoming request with method, path, status code,
    and response time. Keeps operations teams informed without
    adding overhead to business logic.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.monotonic()
        response = self.get_response(request)
        duration_ms = (time.monotonic() - start) * 1000

        user = getattr(request, 'user', None)
        username = user.username if (user and user.is_authenticated) else 'anonymous'

        logger.info(
            "%s %s → %s | %.1fms | user=%s",
            request.method,
            request.path,
            response.status_code,
            duration_ms,
            username,
        )
        return response
