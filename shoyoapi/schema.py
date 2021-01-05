import graphene
import apps.flavours.query
import apps.flavours.mutations

import apps.stock.query


class Query(apps.flavours.query.FlavourQuery, apps.stock.query.StockQuery, graphene.ObjectType):
    pass


class Mutation(apps.flavours.mutations.FlavourMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
