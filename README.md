# oz-defender
Package for interacting with Open Zeppelin's Defender API

## Installation
Using `pip`
```bash
pip install oz-defender
```

Using `poetry`
```bash
poetry add oz-defender
```

## Usage
This packages is intended to mirror as closely as possible the [defender-relay-client](https://github.com/OpenZeppelin/defender-client/tree/e19212ddd87ba1a82f831498340ab4e31734803f/packages/relay) JavaScript package to provide a unified API across languages.

For the [Relay API](https://docs.openzeppelin.com/defender/relay-api-reference#relay-client-module), used for administrating your team's relayers:
```python
from oz_defender.relay import RelayClient

relay = RelayClient(api_key='defender-team-api-key', api_secret='defender-team-api-secret')
relay.list_relayers()
```

For the [RelayerAPI](https://docs.openzeppelin.com/defender/relay-api-reference#relay-signer-module), used for transaction related operations with a specific relayer
```python
from oz_defender.relay import RelayerClient

relayer = RelayerClient(api_key='relayer-api-key', api_secret='relayer-api-secret')
relayer.list_transactions()
```

## Contributing
`oz-defender` is under active development so we welcome any and all contributions to improve the package!
### Issues
To make it as simple as possible for us to help you, please include the following when [creating an issue](https://github.com/franklin-systems/oz-defender/issues):
- OS
- python version
- `oz-defender` version

### Pull requests
**Note: Unless the change you're making is minor, please open an issue in GitHub to discuss a change before opening a PR**
1. Clone this repository
```bash
git clone https://github.com/franklin-systems/oz-defender
```
2. Install `pre-commit` and its hooks
```bash
pip install pre-commit
```
or if you're using macOS
```bash
brew install pre-commit
```
then
```bash
pre-commit install
```
3. Check out a new branch
```bash
git checkout my-new-feature-branch
```
4. Commit and create your PR with a detailed description and tag the GitHub issue that your work addresses
