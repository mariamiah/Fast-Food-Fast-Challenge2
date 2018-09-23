import unittest
from api.models import Order


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order(1, "hamburg", "take_away", "catherine")

    def test_order_id(self):
        self.assertEqual(self.order.order_id, 1, "The order_id should be 1")

    def test_order_name(self):
        self.assertEqual(self.order.order_name, "hamburg", "order_name should\
                         be hamburg")
        self.order.order_name = "salad"
        self.assertEqual(self.order.order_name, "salad", "order_name is now\
                         salad")

    def test_order_type(self):
        self.assertEqual(self.order.order_type, "take_away", "order_type\
                         should be take_away")
        self.order.order_type = "dine_in"
        self.assertEqual(self.order.order_type, "dine_in", "order_type is now\
                         dine_in")

    def test_user_name(self):
        self.assertEqual(self.order.user_name, "catherine", "username should\
                         be catherine")
        self.order.user_name = "Esther"
        self.assertEqual(self.order.user_name, "Esther", "username is now\
                         Esther")
