from functools import wraps

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from base.service.user_services import UserService


class TokenAuthMiddleware:
    @staticmethod
    def token_required(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            header = request.headers.get('Authorization')
            if header and header.startswith('Bearer '):
                user = UserService.find_by_password(header.split(' ')[1])

                if user is None:
                    return JsonResponse({'error': 'Invalid token'}, status=401)

                request.user = user
                return view_func(request, *args, **kwargs)
            return JsonResponse({'error': 'Token required'}, status=401)
        return _wrapped_view

    @staticmethod
    def csrf_exempt(view_func):
        return method_decorator(csrf_exempt, name='dispatch')(view_func)