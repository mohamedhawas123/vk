from django.contrib.contenttypes.models import ContentType
from .models import Action
from django.utils import timezone
import datetime


def create_action(user, verb, target=None):
    now = timezone.now()
    last_min = now - datetime.timedelta(seconds=60)
    similar_action = Action.objects.filter(user_id=user.id, verb=verb, created__gte=last_min)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_action = similar_action.filter(target_ct==target_ct, target_id==target.id)
    
    if not similar_action:
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    
    return False


    
    