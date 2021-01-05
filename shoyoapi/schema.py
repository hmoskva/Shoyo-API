import graphene
import apps.flavours.query
import apps.flavours.mutations

import apps.stock.query
import apps.stock.mutations


class Query(apps.flavours.query.FlavourQuery, apps.stock.query.StockQuery, graphene.ObjectType):
    pass


class Mutation(apps.flavours.mutations.FlavourMutation, apps.stock.mutations.StockMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
