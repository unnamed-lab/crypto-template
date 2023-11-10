from django.http import HttpResponseForbidden
from django.shortcuts import render
def restrict_view_on_wallet_create(event_check_func, template_name='userauths/access_denied.html'):
    def decorator(view_func):
        def wrapped(request, *args, **kwargs):
            if not event_check_func():
                return render(request, template_name)
            return view_func(request, *args, **kwargs)
        return wrapped
    return decorator