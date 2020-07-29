"""Shotener views."""

# Django
from django.shortcuts import get_object_or_404, redirect

# Models
from urlbit.shortener.models import URL


def root(request, url_hash):
    """
    Root path, receive a hashed url and return
    redirection to the full url.
    """
    url = get_object_or_404(URL, url_hash=url_hash)
    return redirect(url.full_url)
