from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnDict


class ProductJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if 'results' not in data and 'id' not in data:
            return super().render({'errors': data})

        return super().render({'product': data})


class CategoryJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, ReturnDict) and 'id' not in data:
            return super().render({'errors': data})

        return super().render({'category': data})
