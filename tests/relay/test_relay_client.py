from unittest import TestCase

from pytest.mock import patch

from oz_defender.relay import RelayClient


class RelayClientTest(TestCase):
    def setUp(self):
        self.relay = RelayClient("test-api-key", "test-api-secret")

    @patch("oz_defender.relay.RelayClient.list_relayers", return_value="[]")
    def test_relay_client(self):
        self.assertEqual(self.relay.list_relayers(), "[]")
