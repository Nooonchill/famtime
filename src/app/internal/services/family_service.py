from typing import Any
import hashlib
import base64
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q

from app.internal.models.family import Family
from app.internal.models.family_role import FamilyRole
from app.internal.models.invitation import Invitation

from app.internal.services.notification_service import *


def try_get_family_by_param(parameter: str, value: Any) -> Family | None:
    try:
        family = Family.objects.get(**{parameter: value})
    except:
        family = None
    return family

def get_family_list(app_user):
    family_roles = FamilyRole.objects.filter(app_user=app_user)
    family_ids = family_roles.values_list('family_id', flat=True)
    families = Family.objects.filter(id__in=family_ids).all()
    return families


def create_family(app_user, family_name, color):
    if FamilyRole.objects.filter(family__name=family_name, app_user=app_user).exists():
        family_name += '#' + str(FamilyRole.objects.filter(family__name=family_name, app_user=app_user).count())
    family = Family.objects.create(name=family_name, color=color)
    FamilyRole.objects.create(family=family, app_user=app_user, role='Owner')
    create_notification(app_user, new_family_message(family), 'Family')
    return family


def add_family(app_user, invite_code):
    invitations = Invitation.objects.filter(code=invite_code).all()
    if invitations.count() == 0:
        return None
    invitation = invitations.latest('created')
    if FamilyRole.objects.filter(family=invitation.family, app_user=app_user).exists():
        return None
    family_users = FamilyRole.objects.filter(family=invitation.family).values_list('app_user', flat=True)
    create_notifications(family_users, new_user_message(app_user, invitation.family), 'Member')
    FamilyRole.objects.create(family=invitation.family, app_user=app_user, role='User')
    create_notification(app_user, add_family_message(invitation.family), 'Family')
    return invitation.family
    

def generate_invite_code(family):
    return Invitation.objects.create(
        family=family,
        code=generate_hash_code(family.name)
    )


def generate_hash_code(input_string):
    hash_object = hashlib.sha256(input_string.encode())
    base64_hash = base64.urlsafe_b64encode(hash_object.digest())
    short_hash = base64_hash[:6].decode('utf-8')
    return short_hash


def get_or_create_invite(family_id):
    now = timezone.now()
    family=Family.objects.get(id=family_id)
    invitation = Invitation.objects.filter(Q(family=family) & Q(created__gte=now-timedelta(days=1))).first()
    if invitation is None:
        invitation = generate_invite_code(family)
    else:
        invitation.update_created()
    return invitation

