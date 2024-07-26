from json import loads

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from base.forms import UserForm
from base.service.user_services import UserService
from base.utils.user_utils import UserUtil


@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def post(self, request):
        data = loads(request.body)
        form = UserForm(data)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if UserService.find_by_username(username):
                return JsonResponse({
                    'message': 'User is exist',
                }, status=400)

            user = UserService.create(username, password)

            response = UserUtil.token_data(user)
            return JsonResponse(response, safe=False, status=201)
        return JsonResponse(form.errors, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        data = loads(request.body)
        form = UserForm(data)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if not UserService.find_by_username(username):
                return JsonResponse({
                    'message': 'User not found',
                }, status=400)

            user = UserService.login(username, password)

            response = UserUtil.token_data(user)
            return JsonResponse(response, status=201)
        return JsonResponse(form.errors, status=400)
