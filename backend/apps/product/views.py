from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .serializers import ProductSerializer


class ProductsAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        # products = request.data.get('products', {})
        # serializer = ProductSerializer(data=products, many=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=201)
        # return Response(serializer.errors, status=400)
        return Response(request.data, status=201)
