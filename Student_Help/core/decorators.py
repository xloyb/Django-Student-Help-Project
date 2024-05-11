# myapp/decorators.py

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseForbidden

def staff_required(view_func):
    actual_decorator = staff_member_required(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return actual_decorator(request, *args, **kwargs)
    return _wrapped_view
