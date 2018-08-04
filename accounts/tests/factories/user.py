import datetime

import factory
from django.utils import timezone


def generate_email(user, domain=None):
    if domain is None:
        domain = factory.Faker('domain_name').generate({})
    return '{0.first_name}.{0.last_name}@{1}'.format(user, domain).lower()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'auth.User'
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: 'username_{}'.format(n))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(generate_email)
    password = factory.PostGenerationMethodCall('set_password', 'password123')

    is_active = True
    is_staff = False
    is_superuser = False

    last_login = factory.LazyAttribute(
        lambda _o: datetime.datetime(
            2000, 1, 1,
            tzinfo=timezone.get_current_timezone()
        )
    )

    date_joined = factory.LazyAttribute(
        lambda _o: datetime.datetime(
            1999, 1, 1,
            tzinfo=timezone.get_current_timezone()
        )
    )
