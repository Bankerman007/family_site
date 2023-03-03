from django.test import TestCase
from . models import Events

class EventsTestCase(TestCase):
    def test_create_object(self):
        obj = Events.objects.create(item='Test Object')
        self.assertEqual(Events.objects.count(), 1)
