from django.test import TestCase
from django.urls import reverse
from . import models

# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        for i in range(2):
            models.User.objects.create(
                first_name="Breno",
                last_name="Carvalho",
                email="breno@email.com",
                gender="Male",
                company="XX",
                city="xx",
                title="xx",
                latitude="111",
                longitude="11",
            )

    def test_all_user_view(self):

        ret = self.client.get(reverse("all-users")).json()

        assert len(ret) == 2

    def test_one_user_view(self):

        ret = self.client.get(reverse("one-user", args="1")).json()

        assert ret["id"] == 1
