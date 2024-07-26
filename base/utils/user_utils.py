from django.contrib.auth.models import User


class UserUtil:
    @staticmethod
    def token_data(user: User) -> dict:
        return {
            'token': user.password,
        }
