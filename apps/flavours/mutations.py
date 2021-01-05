import graphene
from graphene import relay, Field
from graphene_django import DjangoObjectType
from graphql_relay import from_global_id
from graphql import GraphQLError

from .nodes import FlavourNode
from .models import Flavour


class RelayCreateFlavour(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)

    flavour = Field(FlavourNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name):
        try:
            flavour = Flavour(name=name)
            flavour.save()
            return RelayCreateFlavour(flavour=flavour)
        except Exception as e:
            raise GraphQLError(str(e))


class RelayUpdateFlavour(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        id = graphene.ID()

    flavour = Field(FlavourNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name, id):
        try:
            flavour = Flavour.objects.get(pk=from_global_id(id)[1])
            flavour.name = name
            flavour.save()
            return RelayUpdateFlavour(flavour=flavour)
        except Exception as e:
            raise GraphQLError(str(e))


class FlavourMutation(graphene.AbstractType):
    relay_create_flavour = RelayCreateFlavour.Field()
    relay_update_flavour = RelayUpdateFlavour.Field()
