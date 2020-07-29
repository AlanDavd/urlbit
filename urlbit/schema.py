"""URLBit graphql schemas."""

# Graphene
import graphene

# Schemas
import shortener.schema


class Query(shortener.schema.Query, graphene.ObjectType):
    """Urlbit queries."""
    pass


class Mutation(shortener.schema.Mutation, graphene.ObjectType):
    """Urlbit mutations."""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
