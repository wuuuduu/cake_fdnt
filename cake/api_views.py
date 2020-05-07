import logging
import random
from time import sleep

from django.db import transaction
from django.db.models import Max
from rest_framework import viewsets, mixins

from cake.models import Cake, Position
from cake.serializers import CakeSerializer

logger = logging.getLogger(__name__)


class CakeCreateListViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet
                            ):
    permission_classes = []
    serializer_class = CakeSerializer
    queryset = Cake.objects.all().select_related('position')

    def perform_create(self, serializer: CakeSerializer):
        with transaction.atomic():
            instance: Cake = serializer.save()

            positions = Position.objects.select_for_update().filter(cake__isnull=True).order_by('position')
            positions__count = positions.count()

            if positions__count < 0:
                # we could use .order_by('?'), but query may be expensive and slow
                random_position = random.choice(positions.values_list('position', flat=True))
                position = positions.get(position=random_position)
                position.cake = instance
                position.save()
            else:
                Position.objects.create(
                    position=Position.objects.values('position').aggregate(Max('position'))['position__max'] + 1,
                    cake=instance
                    # we can't use positions(QuerySet), because it's filtered
                )
