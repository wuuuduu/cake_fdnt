import logging
from rest_framework import viewsets, mixins

from cake.models import Cake
from cake.serializers import CakeSerializer

logger = logging.getLogger(__name__)


class CakeCreateListViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet
                            ):
    permission_classes = []
    serializer_class = CakeSerializer
    queryset = Cake.objects.all()
