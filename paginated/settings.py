from django.conf import settings


PAGINATED_PER_PAGE = getattr(settings, 'PAGINATED_PER_PAGE', 10)
PAGINATED_NEXT_TEXT = getattr(
    settings, 'PAGINATED_NEXT_TEXT', '&raquo;'
)
PAGINATED_PREV_TEXT = getattr(
    settings, 'PAGINATED_PREV_TEXT', '&laquo;'
)
PAGINATED_LEADING_PAGE_RANGE_DISPLAYED = getattr(
    settings,'PAGINATED_LEADING_PAGE_RANGE_DISPLAYED', 10
)
PAGINATED_TRAILING_PAGE_RANGE_DISPLAYED = getattr(
    settings, 'PAGINATED_TRAILING_PAGE_RANGE_DISPLAYED', 10
)
PAGINATED_LEADING_PAGE_RANGE = getattr(
    settings, 'PAGINATED_LEADING_PAGE_RANGE', 8
)
PAGINATED_TRAILING_PAGE_RANGE = getattr(
    settings, 'PAGINATED_TRAILING_PAGE_RANGE', 8
)
PAGINATED_NUM_PAGES_OUTSIDE_RANGE = getattr(
    settings, 'PAGINATED_NUM_PAGES_OUTSIDE_RANGE', 2
)
PAGINATED_ADJACENT_PAGES = getattr(
    settings, 'PAGINATED_ADJACENT_PAGES', 4
)
PAGINATED_TEMPLATE = getattr(
    settings, 'PAGINATED_TEMPLATE', 'paginated/pagination.html'
)
