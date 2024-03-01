from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_menu_representation(self):
        # Add a new instance of the Menu model
        menu_item = Menu.objects.create(title='Example Menu Item', price=10.99, inventory=1)
        
        # Compare the string representation of the newly added object with the anticipated value
        expected_representation = f"{menu_item.title} - ${menu_item.price}"
        self.assertEqual(str(menu_item), expected_representation)


