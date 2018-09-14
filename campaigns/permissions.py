from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import CampaignPartyRelation, CampaignPartyRelationType
from django.contrib.contenttypes.models import ContentType

class IsOwner(BasePermission):
    message = 'You must be the owner of this object.'
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user



class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if CampaignPartyRelation.objects.filter(
                campaign = obj,
                type = CampaignPartyRelationType.CREATOR,
                content_type = ContentType.objects.get(model="user"),
                object_id = request.user.id
        ).exists():
            return True
        return True