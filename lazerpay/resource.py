import json
import requests

from .utils.constants import (API_URL_INIT_TRANSACTION, API_URL_GET_ACCEPTED_COINS, 
                            API_URL_CONFIRM_TRANSACTION, API_URL_TRANSFER_FUNDS
                        )


class LazerPayClient():

    """
    Base Resource Client
    """

    def __init__(self, pubKey, secretKey):
        self.pubKey = pubKey
        self.secretKey = secretKey
        self.headers = {"Content-Type":"Application/json", "x-api-key": self.pubKey}

    def __to_format(self, response):
        if type(response) == "json":
            return response.json()
        else:
            return response.content

    def __get_data(self, url, headers=None):
        return self.__to_format(requests.get(url, headers=headers or self.headers))

    def __post_data(self, url, data, headers=None):
        return self.__to_format(requests.post(url, data=json.dumps(data), headers=headers or self.headers))




    def initTransaction(self, reference, amount, customer_name, customer_email, coin, currency, accept_partial_payment=False):
        """
        Initiate a crypto payment transfer.

        Attributes:
            reference (string): unique transaction reference
            amount (string): fiat amount
            customer_name (string): Customer's name
            customer_email (string): Customer's email
            coin (string): Coin
            currency (string): Currency
            accept_partial_payment (boolean): 
        
        Returns:
            reponse dict from Lazerpay
        """

        data = {"reference": reference, "amount": amount, "customer_name":customer_name, "customer_email": customer_email,
            "coin": coin, "currency": currency, "accept_partial_payment": accept_partial_payment
        }
        return self.__post_data(url=API_URL_INIT_TRANSACTION, data=data)

    def getAcceptedCoins(self):
        """
        Gets the list of accepted cryptocurrencies on Laz
        """
        return self.__get_data(url=API_URL_GET_ACCEPTED_COINS)

    def confirmPayment(self, identifier):
        """
        Confirm your customer's transaction after payment has been made.
        """
        return self.__get_data(url=f'{API_URL_CONFIRM_TRANSACTION}/{identifier}')

    def payout(self, amount, recipient, coin, blockchain):
        """
        Pay

        Attributes:
            amount (int): 
            recipient (string): 
            coin (string): 
            blockchain (string): 
        
        Returns:
            reponse dict from Lazerpay
        """

        data = {"amount": amount, "recipient": recipient, "coin": coin, "blockchain": blockchain}
        self.headers["Authorization"] = f"Bearer {self.secretKey}"
        return self.__post_data(url=API_URL_TRANSFER_FUNDS, data=data, headers=self.headers)