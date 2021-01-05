import graphene

from .types import FlavourType
from .models import Flavour


class FlavourQuery(graphene.ObjectType):
    all_flavours = graphene.List(FlavourType)
    flavour_by_name = graphene.Field(
        FlavourType, name=graphene.String(required=True))

    def resolve_all_flavours(root, info):
        return Flavour.objects.select_related().all()

    def resolve_flavour_by_name(root, info, name):
        try:
            return Flavour.objects.get(name=name)
        except Flavour.DoesNotExist:
            return None
