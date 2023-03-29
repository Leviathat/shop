from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnDict
import json


class LoginJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, ReturnDict) and 'token' not in data:
            return super().render({'errors': data})

        return super().render({'user': data})
