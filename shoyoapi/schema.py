import graphene

from apps.flavours.types import FlavourType
from apps.flavours.models import Flavour

from apps.stock.types import StockType
from apps.stock.models import Stock


class Query(graphene.ObjectType):
    all_flavours = graphene.List(FlavourType)
    flavour_by_name = graphene.Field(
        FlavourType, name=graphene.String(required=True))
    all_stock = graphene.List(StockType)

    def resolve_all_flavours(root, info):
        # We can easily optimize query count in the resolve method
        return Flavour.objects.select_related().all()

    def resolve_flavour_by_name(root, info, name):
        try:
            return Flavour.objects.get(name=name)
        except Flavour.DoesNotExist:
            return None

    def resolve_all_stock(root, info):
        # We can easily optimize query count in the resolve method
        return Stock.objects.all()


schema = graphene.Schema(query=Query)
