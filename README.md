# oz-defender
Package for interacting with Open Zeppelin's Defender API

## Installation
Using `pip`
```bash
$ pip install oz-defender
```

Using `poetry`
```bash
$ poetry add oz-defender
```

## Usage
This package is intended to mirror as closely as possible the [defender-client](https://github.com/OpenZeppelin/defender-client) JavaScript package to provide a unified API across languages.

### Relay
See [defender-relay-client](https://www.npmjs.com/package/defender-relay-client) for this module's inspiration.

For the [Relay API](https://docs.openzeppelin.com/defender/relay-api-reference#relay-client-module), used for administrating your team's relayers:
```python
from oz_defender.relay import RelayClient

relay = RelayClient(api_key='defender-team-api-key', api_secret='defender-team-api-secret')
relay.list_relayers()
```

For the [Relayer API](https://docs.openzeppelin.com/defender/relay-api-reference#relay-signer-module), used for transaction related operations with a specific relayer
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

**NOTE: Unless the change you're making is minor, please open an issue in GitHub to discuss a change before opening a PR**

### Development
This package is developed using [poetry](https://python-poetry.org/docs/). Make sure its installed on your machine and peep the documentation to familiarize yourself with its commands.

1. Clone this repository
```bash
$ git clone https://github.com/franklin-systems/oz-defender
```
2. Install `pre-commit` and its hooks
```bash
$ pip install pre-commit
```
or if you're using macOS
```bash
$ brew install pre-commit
```
then
```bash
$ pre-commit install
```
3. Check out a new branch
```bash
$ git checkout my-new-feature-branch
```
4. Commit and create your PR with a detailed description and tag the GitHub issue that your work addresses

### Testing `oz_defender` locally
1. Install (if it's your first time) or update deps
```bash
$ poetry install
```
or
```bash
$ poetry update
```
2. Initialize a shell in `poetry` virtual env
```bash
$ poetry shell
```
3. Enter a python REPL
```bash
(oz-defender-py3.10) $ python3
```
4. Import `oz_defender` and off you go
```python
>>> from oz_defender import *
>>> relayer = RelayerClient(api_key='relayer-api-key', api_secret='relayer-api-secret')
```
5. Quit the python REPL and re-initialize to pick up code changes as you develop
