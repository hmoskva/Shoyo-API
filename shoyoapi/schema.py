import graphene
import apps.flavours.query
import apps.stock.query


class Query(apps.flavours.query.FlavourQuery, apps.stock.query.StockQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
