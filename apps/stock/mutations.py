import graphene
from graphene import relay, Field
from graphql_relay import from_global_id
from graphql import GraphQLError

from .nodes import StockNode
from .models import Stock


class UpdateStock(relay.ClientIDMutation):
    class Input:
        quantity = graphene.Int(required=True)
        id = graphene.ID()

    stock = Field(StockNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, quantity, id):
        try:
            stock = Stock.objects.get(pk=from_global_id(id)[1])
            stock.quantity = quantity
            stock.save()
            return UpdateStock(stock=stock)
        except Exception as e:
            raise GraphQLError(str(e))


class StockMutation(graphene.AbstractType):
    update_stock = UpdateStock.Field()
