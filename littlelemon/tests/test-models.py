from django.test import TestCase

from LittleLemon.littlelemon.LittleLemonAPI.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        item1 = MenuItem.objects.create(title="IceCream1", price=80, inventory=100)
        item2 = MenuItem.objects.create(title="IceCream2", price=80, inventory=100)
        self.assertEqual(item1, "IceCream1 : 80")
        self.assertEqual(item2, "IceCream1 : 80")