import graphene
from graphene import relay, Field
from graphene_django import DjangoObjectType
from graphql_relay import from_global_id
from graphql import GraphQLError

from .nodes import FlavourNode
from .models import Flavour


class CreateFlavour(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)

    flavour = Field(FlavourNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name):
        try:
            flavour = Flavour(name=name)
            flavour.save()
            return CreateFlavour(flavour=flavour)
        except Exception as e:
            raise GraphQLError(str(e))


class UpdateFlavour(relay.ClientIDMutation):
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
            return UpdateFlavour(flavour=flavour)
        except Exception as e:
            raise GraphQLError(str(e))


class FlavourMutation(graphene.AbstractType):
    create_flavour = CreateFlavour.Field()
    update_flavour = UpdateFlavour.Field()
