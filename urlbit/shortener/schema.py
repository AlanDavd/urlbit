"""Shortener graphql schema."""

# Django
from django.db.models import Q

# Graphene
import graphene
from graphene_django import DjangoObjectType

# Models
from urlbit.shortener.models import URL


class URLType(DjangoObjectType):
    """URL schema."""

    class Meta:
        """Meta options."""
        model = URL


class Query(graphene.ObjectType):
    """Query schema."""

    urls = graphene.List(
        URLType,
        url=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int()
    )

    def resolve_urls(self, info, url=None, first=None, skip=None, **kwargs):
        """Resolve incoming requests."""
        queryset = URL.objects.all()

        if url:
            _filter = Q(full_url__icontains=url)
            queryset = queryset.filter(_filter)

        if first:
            queryset = queryset[:first]

        if skip:
            queryset = queryset[skip:]

        return queryset


class CreateURL(graphene.Mutation):
    """Crate new URL mutation."""
    url = graphene.Field(URLType)

    class Arguments:
        """Data accepted by the server."""
        full_url = graphene.String()

    def mutate(self, info, full_url):
        """Receive data and save it into DB."""
        url = URL(full_url=full_url)
        url.save()

        return CreateURL(url=url)


class Mutation(graphene.ObjectType):
    """Hold shotener's app mutations"""
    create_url = CreateURL.Field()
