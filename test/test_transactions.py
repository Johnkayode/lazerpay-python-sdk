import unittest
import json
import random
import string
from urllib import response

from lazerpay.resource import LazerPayClient


client = LazerPayClient(pubKey="pk_test_z0XAaAI8LhWzXWPKLVnvZrAlbqvNbfNBtSuDJTWjQDz9Wrq42p", secretKey="sk_test_gYS4TDjQTV8fGuJeMqAWJlS0eHeeFbJkupXJW9wvM9QXSdudox")



class TransactionResourceTest(unittest.TestCase):
    """
    TestCase class for the Lazerpay SDK.
    """

    def setUp(self):
        self.client = LazerPayClient(pubKey="pk_test_z0XAaAI8LhWzXWPKLVnvZrAlbqvNbfNBtSuDJTWjQDz9Wrq42p", secretKey="sk_test_gYS4TDjQTV8fGuJeMqAWJlS0eHeeFbJkupXJW9wvM9QXSdudox")
        self.reference = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

    def test_initTransaction(self):
        response = json.loads(self.client.initTransaction( 
            reference=self.reference, # Replace with a reference you generated
            amount="10", 
            customer_name="Njoku Emmanuel", 
            customer_email="kalunjoku123@gmail.com", 
            coin="USDC", 
            currency="NGN", 
            accept_partial_payment=True # By default, it's false
        ))
        self.assertEqual(response["statusCode"], 201)

    def test_getAcceptedCoins(self):
        response = json.loads(self.client.getAcceptedCoins())
        self.assertEqual(response["status"], "success")

    def test_confirmPayment(self):
        response = json.loads(self.client.confirmPayment(
            identifier=self.reference
        ))
        self.assertEqual(response["statusCode"], 404)

    def test_payout(self):
        response = json.loads(self.client.payout(amount=1,
            recipient="0x0B4d358D349809037003F96A3593ff9015E89efA", 
            coin="BUSD", 
            blockchain="Binance Smart Chain"
        ))
        # Insufficient balance
        self.assertEqual(response["statusCode"], 400)