from django.conf import settings


def admin_site_header(request):
    """
    Return a lazy 'messages' context variable as well as
    'DEFAULT_MESSAGE_LEVELS'.
    """
    return {
        'admin_site_header': settings.ADMIN_SITE_HEADER
    }