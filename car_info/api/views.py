from rest_framework import decorators, permissions, status, viewsets
from rest_framework.response import Response

from cars.models import Car

from . import serializers
from .permissions import OwnerOrReadOnly


class CarViewSet(viewsets.ModelViewSet):
    """ViewSet для автомобилей."""

    queryset = Car.objects.all()
    permission_classes = (OwnerOrReadOnly, )
    serializer_class = serializers.CarSerializer

    @decorators.action(detail=True,
                       methods=['POST', 'GET'],
                       url_path='comment')
    def comment_car(self, request, pk=None):
        """View для комментирования."""

        car = self.get_object()
        if request.method == 'POST':
            self.permission_classes = (permissions.IsAuthenticated,)

            serializer = serializers.CommentSerializer(
                data=request.data, context={'request': request, 'pk': pk})

            if serializer.is_valid():
                serializer.save()
                return Response({"Сообщение": "Записано."},
                                status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            comments = car.comments.all()
            serializer = serializers.CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
