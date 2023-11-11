from django.test import TestCase

from shop.models import Product

# from unittest import TestCase

class ProductsTest(TestCase):
    fixtures = ['shop.json', 'myauth.json']

    def test_products_qty(self):
        products_qty = Product.objects.count()
        self.assertEqual(products_qty, 1)

    def test_main_login_required(self):
        response = self.client.get('/')
        self.assertEqual(302, response.status_code)

        self.client.login(username='user', password='123')
        response = self.client.get('/')  # force login
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(200, response.status_code)