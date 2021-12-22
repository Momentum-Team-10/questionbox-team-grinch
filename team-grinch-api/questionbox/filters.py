# I am not sure I needed another file, I just added it for readability
from rest_framework import filters

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])