from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import User
from .exceptions import NotFound


class EmailBackend(ModelBackend):

    def authenticate(self, request, email=None, username=None, password=None, **kwargs):
        
        try:

            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=email))
        
        except User.DoesNotExist:
        
            User().set_password(password)
            raise NotFound 
        
        except User.MultipleObjectsReturned:
        
            user = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=email)).order_by('id').first()
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user