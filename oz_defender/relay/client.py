import requests
from pycognito.utils import RequestsSrpAuth

from .exceptions import RelayException, RelayTimeoutError


class BaseClient:
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
            raise RelayTimeoutError(f"GET: {self.base_api + path}")

        return response

    def post(self, path, payload=None):
        try:
            response = requests.post(
                self.base_api + path,
                json=payload,
                headers=self.headers,
                auth=self.auth,
                timeout=60,
            )
        except requests.ReadTimeout:
            raise RelayTimeoutError(f"POST: {self.base_api + path}")

        return response

    def put(self, path, payload=None):
        try:
            response = requests.put(
                self.base_api + path,
                json=payload,
                headers=self.headers,
                auth=self.auth,
                timeout=60,
            )
        except requests.ReadTimeout:
            raise RelayTimeoutError(f"PUT: {self.base_api + path}")

        return response

    def delete(self, path):
        try:
            response = requests.delete(
                self.base_api + path,
                headers=self.headers,
                auth=self.auth,
                timeout=60,
            )
        except requests.ReadTimeout:
            raise RelayTimeoutError(f"DELETE: {self.base_api + path}")

        return response

    def _handle_response(self, response: requests.Response):
        if not response.ok:
            raise self._relayer_exception(response)

        return response.json()

    def _relayer_exception(self, response: requests.Response):
        # TODO: @ssavarirayan add status code parsing and raise specific exceptions
        try:
            message = response.json()["message"]
            return RelayException(message)
        except:
            # if error parsing fails, return the entire response
            return RelayException(response.json())


class RelayClient(BaseClient):
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        aws_user_pool_id: str = "us-west-2_94f3puJWv",
        aws_client_id: str = "40e58hbc7pktmnp9i26hh5nsav",
        aws_srp_pool_region: str = "us-west-2",
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.aws_user_pool_id = aws_user_pool_id
        self.aws_client_id = aws_client_id
        self.aws_srp_pool_region = aws_srp_pool_region
        self.base_api = "https://defender-api.openzeppelin.com/relayer/"

    def get_relayer(self, relayer_id):
        response = self.get(f"relayers/{relayer_id}")

        return self._handle_response(response)

    def list_relayers(self):
        response = self.get("relayers/summary")

        return self._handle_response(response)

    def list_relayer_keys(self, relayer_id: str):
        response = self.get(f"relayers/{relayer_id}/keys")

        return self._handle_response(response)

    def create_relayer(self, data: dict) -> dict:
        response = self.post("relayers", data)

        return self._handle_response(response)

    def create_relayer_key(self, relayer_id: str) -> dict:
        response = self.post(f"relayers/{relayer_id}/keys")

        return self._handle_response(response)

    def update_relayer(self, relayer_id: str, data: dict) -> dict:
        initial_data = self.get_relayer(relayer_id)

        if "policies" in data:
            response = self.update_relayer_policies(relayer_id, data["policies"])

            if len(data) == 1:
                return self._handle_response(response)

        payload = initial_data | data
        response = self.put(f"relayers", payload)

        return self._handle_response(response)

    def update_relayer_policies(self, relayer_id: str, data: dict):
        initial_data = self.get_relayer(relayer_id)["policies"]
        payload = initial_data | data
        response = self.put(f"relayers/{relayer_id}", payload)

        return self._handle_response(response)

    def delete_relayer_key(self, relayer_id: str, key_id: str):
        response = self.delete(f"relayers/{relayer_id}/keys/{key_id}")

        return self._handle_response(response)


class RelayerClient(BaseClient):
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        aws_user_pool_id: str = "us-west-2_iLmIggsiy",
        aws_client_id: str = "1bpd19lcr33qvg5cr3oi79rdap",
        aws_srp_pool_region: str = "us-west-2",
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.aws_user_pool_id = aws_user_pool_id
        self.aws_client_id = aws_client_id
        self.aws_srp_pool_region = aws_srp_pool_region
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
