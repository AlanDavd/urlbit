"""URL's configuration."""

# Django
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# Graphene
from graphene_django.views import GraphQLView

# Views
from urlbit.shortener.views import root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('<str:url_hash>/', root, name='root')
]
