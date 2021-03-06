from django import http
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.template import Context, loader

from django import http
from django.conf import settings

def home(request):
    return direct_to_template(request,'home.html')


def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context:
        MEDIA_URL
            Path of static media (e.g. "media.example.org")
    """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    return http.HttpResponseServerError(t.render(Context({
        'STATIC_URL': settings.STATIC_URL
    })))
