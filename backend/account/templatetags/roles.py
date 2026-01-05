from django import template

register = template.Library()

@register.filter
def has_role(user, role):
    if not user.is_authenticated:
        return False
    return user.role == role


@register.filter
def has_any_role(user, roles):
    if not user.is_authenticated:
        return False
    allowed_roles = [r.strip() for r in roles.split(",")]
    return user.role in allowed_roles
