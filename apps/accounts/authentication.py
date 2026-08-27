from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):

    def authenticate(
        self,
        request,
        username=None,
        password=None,
        **kwargs
    ):
        if username is None or password is None:
            return None

        user = User.objects.filter(
            username__iexact=username
        ).first()

        if user is None:
            user = User.objects.filter(
                email__iexact=username
            ).first()

        if user is None:
            return None

        if user.check_password(password):
            return user

        return None