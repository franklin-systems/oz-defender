import requests
from pycognito.utils import RequestsSrpAuth

from .exceptions import RelayerException, RelayerTimeout

BASE_API = "https://api.defender.openzeppelin.com/"


class RelayerClient:
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        aws_user_pool_id: str,
        aws_client_id: str,
        aws_srp_pool_region: str,
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.aws_user_pool_id = aws_user_pool_id
        self.aws_client_id = aws_client_id
        self.aws_srp_pool_region = aws_srp_pool_region

    @property
    def headers(self):
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Api-Key": self.api_key,
        }

    @property
    def auth(self):
        return RequestsSrpAuth(
            username=self.api_key,
            password=self.api_secret,
            user_pool_id=self.aws_user_pool_id,
            client_id=self.aws_client_id,
            user_pool_region=self.aws_srp_pool_region,
        )

    def get_relayer(self):
        response = self.get("relayer")

        if "relayerId" in response:
            return response
        else:
            raise self.relayer_exception(response)

    def get_tx(self, defender_id):
        response = self.get(f"txs/{defender_id}")

        if "transactionId" in response:
            return response
        else:
            raise self.relayer_exception(response)

    def relay_tx(self, payload):
        response = self.post("txs", payload)

        if "transactionId" in response:
            return response
        else:
            raise self.relayer_exception(response)

    def get(self, path, params=None):
        try:
            response = requests.get(
                BASE_API + path,
                params=params,
                headers=self.headers,
                auth=self.auth,
                timeout=60,
            )
        except requests.ReadTimeout:
            raise RelayerTimeout(f"GET: {BASE_API + path}")

        return response.json()

    def post(self, path, payload):
        try:
            response = requests.post(
                BASE_API + path,
                json=payload,
                headers=self.headers,
                auth=self.auth,
                timeout=60,
            )
        except requests.ReadTimeout:
            raise RelayerTimeout(f"POST: {BASE_API + path}")

        return response.json()

    def relayer_exception(self, response):
        try:
            message = response["message"]
            return RelayerException(message)
        except:
            # if error parsing fails, return the entire response
            return RelayerException(response)
