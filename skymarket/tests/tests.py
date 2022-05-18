
from django.test import TestCase
from rest_framework.test import APIClient

from tests.selection.test_selection import test_retrieve_selection, test_get_all_selection, test_post_selection
from tests.cat.test_cat import test_retrieve_cat
from tests.ads.adv_create_test import test_retrieve_adv, test_get_all_adv, test_post_adv
from users.test_users import test_list_users

#pytest tests/ -vv
class UseFactoryClassTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def run_tests(self):
        test_retrieve_adv(self.client)
        test_get_all_adv(self.client)
        test_post_adv(self.client)
        test_retrieve_cat(self.client)
        test_list_users(self.client)
        test_retrieve_selection(self.client)
        test_get_all_selection(self.client)
        test_post_selection(self.client)
