from graphene_django import DjangoObjectType

from .models import Flavour


class FlavourType(DjangoObjectType):
    class Meta:
        model = Flavour
        fields = ['id', "name", "image", 'stock', ]
