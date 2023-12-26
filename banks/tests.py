from django.test import TestCase
from .models import Bank, Branch

from django.contrib.auth.models import User

# Create your tests here.
class BankTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='Faaiz',
            last_name='Ali',
            email='faaizalitariq@gmail.com',
            username='faaiz',
            password='Pak123pak',
        )
    def test_obj_create(self):
        inst = Bank.objects.create(
            owner=self.user,
            name = 'UBL',
            swift_code = '123',
            institution_number = '008',
            description = 'this is UBL LTD',
        )
        self.assertIsInstance(inst, Bank)
        self.assertEqual(inst.owner, self.user)


class BranchTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='Faaiz',
            last_name='Ali',
            email='faaizalitariq@gmail.com',
            username='faaiz',
            password='Pak123pak',
        )
        self.bank = Bank.objects.create(
            owner=self.user,
            name = 'UBL',
            swift_code = '123',
            institution_number = '008',
            description = 'this is UBL LTD',
        )
    def test_obj_create(self):
        inst = Branch.objects.create(
            bank=self.bank,
            name='branch 1',
            transit_number='1234',
            email='faaiz@outlook.com',
            address='Burewala St#1',
            capacity=10,
        )
        self.assertIsInstance(inst, Branch)
        self.assertEqual(inst.bank, self.bank)
        self.assertEqual(inst.bank.owner, self.user)