from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.http import Http404
from django.template.loader import render_to_string

from . import paginators
from . import settings


def paginated(queryset, request, per_page=settings.PAGINATED_PER_PAGE):
    paginator = Paginator(queryset, per_page)

    try:
        events = paginator.page(request.GET.get('page', 1))
    except PageNotAnInteger:
        raise Http404
    except EmptyPage:
        raise Http404

    pagination = render_to_string(
        settings.PAGINATED_TEMPLATE,
        paginators.digg_paginator({
            'request': request,
            'page_obj': events,
            'paginator': paginator,
        })
    )

    return events, pagination
