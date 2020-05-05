import factory
from django.contrib.auth import get_user_model

from cake.models import Cake

User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: "First_name_%d" % n)
    last_name = factory.Sequence(lambda n: "Last_name_%d" % n)
    email = factory.Sequence(lambda n: "email_%d@domain.com" % n)
    username = factory.Sequence(lambda n: 'username_%d' % n)
    password = 'pass'

    @factory.post_generation
    def set_password(self, create, extracted, **kwargs):
        self.set_password(self.password)


class CakeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Cake

    name = factory.Sequence(lambda n: "name_%d" % n)
    text = factory.Sequence(lambda n: "text_%d" % n)
