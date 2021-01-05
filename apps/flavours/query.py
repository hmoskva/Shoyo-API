import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from .nodes import FlavourNode


class FlavourQuery(graphene.ObjectType):
    all_flavours = DjangoFilterConnectionField(FlavourNode)
    flavour = relay.Node.Field(FlavourNode)
