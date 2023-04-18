import typing
import uuid

import requests
from pycognito.utils import RequestsSrpAuth

from .exceptions import RelayException, RelayTimeout


class BaseClient:
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

    def get(self, path, params=None):
        try:
            response = requests.get(
                self.base_api + path,
                params=params,
                headers=self.headers,
                auth=self.auth,
                timeout=60,
            )
        except requests.ReadTimeout:
            raise RelayTimeout(f"GET: {self.base_api + path}")

        return response

    def post(self, path, payload):
        try:
            response = requests.post(
                self.base_api + path,
                json=payload,
                headers=self.headers,
                auth=self.auth,
                timeout=60,
            )
        except requests.ReadTimeout:
            raise RelayTimeout(f"POST: {self.base_api + path}")

        return response

    def relayer_exception(self, response: requests.Response):
        # TODO: @ssavarirayan add status code parsing and raise specific exceptions
        try:
            message = response["message"]
            return RelayException(message)
        except:
            # if error parsing fails, return the entire response
            return RelayException(response)


class RelayClient(BaseClient):
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        aws_user_pool_id: str = "us-west-2_94f3puJWv",
        aws_client_id: str = "40e58hbc7pktmnp9i26hh5nsav",
        aws_srp_pool_region: str = "us-west-2",
    ):
        super().__init__(
            api_key,
            api_secret,
            aws_user_pool_id,
            aws_client_id,
            aws_srp_pool_region,
        )
        self.base_api = "https://defender-api.openzeppelin.com/relayer/"

    def list_relayers(self):
        response = self.get("relayers/summary")

        if not response.ok:
            raise self.relayer_exception(response)

        return response.json()

    def list_relayer_keys(self, relayer_id: uuid.UUID):
        response = self.get("relayers/keys")

        if not response.ok:
            raise self.relayer_exception(response)

        return response.json()

    def create_relayer(
        self,
        name: str,
        network: str,
        min_balance: int = int(1e17),
        gas_price_cap: int = None,
        whitelist_receivers: typing.List = [],
        eip1559_pricing: bool = False,
        private_transactions: bool = False,
        use_address_from_relayer_id: str = None,
    ):

        if use_address_from_relayer_id and any(
            [gas_price_cap, whitelist_receivers, eip1559_pricing, private_transactions]
        ):
            raise ValueError(
                "use_address_from_relayer_id cannot be used with other policies"
            )

        if use_address_from_relayer_id:
            payload = {
                "name": name,
                "network": network,
                "minBalance": min_balance,
                "useAddressFromRelayerId": use_address_from_relayer_id,
            }
        else:
            payload = {
                "name": name,
                "network": network,
                "minBalance": min_balance,
                "policies": {
                    "gasPriceCap": gas_price_cap,
                    "whitelistReceivers": whitelist_receivers,
                    "eip1559Pricing": eip1559_pricing,
                    "privateTransactions": private_transactions,
                },
            }

        response = self.post("relayers", payload)

        if not response.ok:
            raise self.relayer_exception(response)

        return response.json()

    def update_relayers(self):
        pass

    def update_relayers_policy(self):
        pass

    def create_relayer_key(self):
        pass

    def delete_relayer_key(self):
        pass


class RelayerClient(BaseClient):
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        aws_user_pool_id: str = "us-west-2_iLmIggsiy",
        aws_client_id: str = "1bpd19lcr33qvg5cr3oi79rdap",
        aws_srp_pool_region: str = "us-west-2",
    ):
        super().__init__(
            api_key,
            api_secret,
            aws_user_pool_id,
            aws_client_id,
            aws_srp_pool_region,
        )
        self.base_api = "https://api.defender.openzeppelin.com/"

    def get_relayer(self):
        pass

    def send_transaction(self):
        pass

    def get_transaction_status(self):
        pass

    def replace_transaction_by_id(self):
        pass

    def replace_transaction_by_nonce(self):
        pass

    def list_transactions(self):
        pass

    def sign_transaction(self):
        pass

    def call_json_rpc(self):
        pass
