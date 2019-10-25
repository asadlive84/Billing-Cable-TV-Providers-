from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from user.models import CustomUser


def custom_user(pk):
    return CustomUser.objects.get(pk=pk)


def worker_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and
                  u.is_active and
                  u.is_staff and
                  u.user_type in ['1', '2', '3'] or
                  u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def permission_required_permission_rule(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and
                  u.is_active and
                  u.is_staff and
                  u.user_type == '1' or
                  u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def create_and_update(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and
                  u.is_active and
                  u.is_staff and
                  u.user_type == ['1', '2'] or
                  u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator




