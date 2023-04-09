from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.product_reviews.serializers import ReviewSerializer
from apps.product_reviews.renderers import ReviewJSONRenderer


class MakeReviewAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ReviewSerializer
    renderer_classes = (ReviewJSONRenderer, )

    def post(self, request):
        review = request.data.get('review', {})
        review['customer'] = request.user.pk
        serializer = self.serializer_class(data=review)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
