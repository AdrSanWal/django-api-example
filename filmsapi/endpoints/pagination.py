from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from config.settings import REST_FRAMEWORK


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        first = self.page.start_index()
        last = self.page.end_index()
        count = last - first + 1

        return Response({
            'totalPages': self.page.paginator.num_pages,
            'totalItems': self.page.paginator.count,
            'countItemsOnPage': count,
            'firstItemOnPage': first,
            'lastItemOnPage': last,
            'currentPage': self.page.number,
            'next': self.page.has_next(),
            'previous': self.page.has_previous(),
            'results': data
        })
