import graphene

from .types import StockType
from .models import Stock


class StockQuery(graphene.ObjectType):
    all_stock = graphene.List(StockType)

    def resolve_all_stock(root, info):
        return Stock.objects.all()
