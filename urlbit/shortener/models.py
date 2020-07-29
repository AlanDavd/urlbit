"""Short URL model."""

# Django
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Hash
from hashlib import md5

# Graphql
from graphql import GraphQLError


class URL(models.Model):
    """URL model."""

    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        validate = URLValidator()
        try:
            validate(self.full_url)
        except ValidationError as ve:
            raise GraphQLError('invalid url')

        return super().save(*args, **kwargs)
