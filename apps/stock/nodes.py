from graphene import relay
from graphene_django import DjangoObjectType

from .models import Stock


class StockNode(DjangoObjectType):
    class Meta:
        model = Stock
        filter_fields = ['id', "size", "quantity"]
        interfaces = [relay.Node, ]
