from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserService:
    @staticmethod
    def find_by_username(username) -> User | None:
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @staticmethod
    def find_by_password(password: str) -> User | None:
        try:
            return User.objects.get(password=password)
        except User.DoesNotExist:
            return None

    @staticmethod
    def login(username, password) -> User:
        return authenticate(username=username, password=password)

    @staticmethod
    def create(username, password) -> User:
        return User.objects.create(username=username, password=make_password(password))

