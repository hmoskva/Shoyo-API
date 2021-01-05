from graphene import relay
from graphene_django import DjangoObjectType

from .models import Stock


class StockNode(DjangoObjectType):
    class Meta:
        model = Stock
        fields = ['id', "size", "quantity"]
        filter_fields = {
            'size': ['exact'],
            'quantity': ['exact', 'lt', 'lte', 'gt', 'gte'],
        }
        interfaces = [relay.Node, ]
