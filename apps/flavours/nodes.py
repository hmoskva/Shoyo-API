from graphene import relay
from graphene_django import DjangoObjectType

from .models import Flavour


class FlavourNode(DjangoObjectType):
    class Meta:
        model = Flavour
        fields = ['id', 'name', 'stock']
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'stock': ['exact'],
            'stock__size': ['exact'],
            'stock__quantity': ['exact', 'lt', 'lte', 'gt', 'gte'],
        }
        interfaces = [relay.Node, ]
