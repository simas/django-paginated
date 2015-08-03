# coding: utf-8
from . import settings

'''
Based on
    http://blog.localkinegrinds.com/2007/09/06/digg-style-pagination-in-django/
    and http://djangosnippets.org/snippets/2680/

Recreated by Haisheng HU <hanson2010@gmail.com> on Jun 3, 2012
'''

LEADING_PAGE_RANGE_DISPLAYED = settings.PAGINATED_LEADING_PAGE_RANGE_DISPLAYED
TRAILING_PAGE_RANGE_DISPLAYED = settings.PAGINATED_TRAILING_PAGE_RANGE_DISPLAYED
LEADING_PAGE_RANGE = settings.PAGINATED_LEADING_PAGE_RANGE
TRAILING_PAGE_RANGE = settings.PAGINATED_TRAILING_PAGE_RANGE
NUM_PAGES_OUTSIDE_RANGE = settings.PAGINATED_NUM_PAGES_OUTSIDE_RANGE
ADJACENT_PAGES = settings.PAGINATED_ADJACENT_PAGES


def digg_paginator(context):
    '''
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying leading, adjacent
    and trailing page links in addition to those created by the object_list
    generic view.
    '''

    paginator = context['paginator']
    page_obj = context['page_obj']
    pages = paginator.num_pages
    page = page_obj.number
    in_leading_range = in_trailing_range = False
    pages_outside_leading_range = pages_outside_trailing_range = range(0)
    if pages <= LEADING_PAGE_RANGE_DISPLAYED + NUM_PAGES_OUTSIDE_RANGE + 1:
        in_leading_range = in_trailing_range = True
        page_range = [n for n in range(1, pages + 1)]
    elif page <= LEADING_PAGE_RANGE:
        in_leading_range = True
        page_range = [n for n in range(1, LEADING_PAGE_RANGE_DISPLAYED + 1)]
        pages_outside_leading_range = [
            n + pages for n in range(0, -NUM_PAGES_OUTSIDE_RANGE, -1)
        ]
    elif page > pages - TRAILING_PAGE_RANGE:
        in_trailing_range = True
        page_range = [
            n for n in range(pages-TRAILING_PAGE_RANGE_DISPLAYED+1, pages+1)
            if n > 0 and n <= pages
        ]
        pages_outside_trailing_range = [
            n + 1 for n in range(0, NUM_PAGES_OUTSIDE_RANGE)
        ]
    else:
        page_range = [
            n for n in range(page - ADJACENT_PAGES, page + ADJACENT_PAGES + 1)
            if n > 0 and n <= pages
        ]
        pages_outside_leading_range = [
            n + pages for n in range(0, -NUM_PAGES_OUTSIDE_RANGE, -1)
        ]
        pages_outside_trailing_range = [
            n + 1 for n in range(0, NUM_PAGES_OUTSIDE_RANGE)
        ]

    request = context['request']
    params = request.GET.copy()
    if 'page' in params:
        del(params['page'])
    get_params = params.urlencode()

    previous_page = (
        page_obj.previous_page_number() if page_obj.has_previous() else None
    )
    next_page = page_obj.next_page_number() if page_obj.has_next() else None
    return {
        'pages': pages,
        'page': page,
        'previous': previous_page,
        'next': next_page,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'page_range': page_range,
        'in_leading_range': in_leading_range,
        'in_trailing_range': in_trailing_range,
        'pages_outside_leading_range': pages_outside_leading_range,
        'pages_outside_trailing_range': pages_outside_trailing_range,
        'get_params': get_params,
    }
