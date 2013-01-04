from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from ley.models import Ley

from django.contrib.auth.models import User



class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authentication = BasicAuthentication()
        authentication.realm = "This is not an API"
        authorization = DjangoAuthorization()
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']

class LeyResource(ModelResource):
    
    class Meta:
        queryset = Ley.objects.all()
        resource_name = 'leyresource'
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
        authentication.realm = "This is not an API"
        filtering = {
            'numero':  ALL,
        }
