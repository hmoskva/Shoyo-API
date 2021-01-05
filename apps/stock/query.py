import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from .nodes import StockNode


class StockQuery(graphene.ObjectType):
    all_stock = DjangoFilterConnectionField(StockNode)
