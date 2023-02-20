
from rest_framework import status
from rest_framework.response import Response
from .models import Balance, Credit, Debit
from django.core.cache import cache
from rest_framework.views import APIView
import json
from web3 import Web3


class BalanceViewSet(APIView):
    def get(self, request):
        try:
            infura_url = 'https://eth.getblock.io/28dee1d9-7e8c-4d57-8c64-b59fc68cdd2c/mainnet/'  # your uri
            w3 = Web3(Web3.HTTPProvider(infura_url))
            address = '0x8D97689C9818892B700e27F316cc3E41e17fBeb9'
            balance = w3.eth.getBalance(address)
            rtn = {
                "balance": balance,
            }
            cache.set('balance_key', json.dumps(rtn))
            Balance(balance=rtn['balance']).save()
            return Response(rtn, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)


class DebitViewSet(APIView):
    def get(self, request):
        try:
            infura_url = 'https://eth.getblock.io/28dee1d9-7e8c-4d57-8c64-b59fc68cdd2c/mainnet/'  # your uri
            w3 = Web3(Web3.HTTPProvider(infura_url))
            transaction = {
                'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
                'value': 1000000000,
                'gas': 2000000,
                'gasPrice': 234567897654321,
                'nonce': 0,
                'chainId': 1
            }
            key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
            signed = w3.eth.account.signTransaction(transaction, key)
            rtn = {
                'debit': json.dumps(signed)
            }
            cache.set('transaction_debit_key', json.dumps(rtn))
            Debit(debit=rtn['debit']).save()
            return Response(rtn, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)


class CreditViewSet(APIView):
    def get(self, request):
        try:
            infura_url = 'https://eth.getblock.io/28dee1d9-7e8c-4d57-8c64-b59fc68cdd2c/mainnet/'  # your uri
            w3 = Web3(Web3.HTTPProvider(infura_url))
            block = w3.eth.get_block(12345)
            rtn = {
                'credit': list(block)
            }

            cache.set('transaction_credit_key', json.dumps(rtn['credit']))
            Credit(credit=rtn['credit']).save()
            return Response(rtn, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
