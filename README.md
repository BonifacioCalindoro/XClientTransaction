<h1 align="center">X-Client-Transaction-ID</h1>

<p align="center">
Twitter X-Client-Transaction-Id generator written in python.

<p align="center">
<a href="https://choosealicense.com/licenses/mit/"> <img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/pypi/pyversions/XClientTransaction"></a>
<a href="https://img.shields.io/pypi/dd/XClientTransaction"> <img src="https://img.shields.io/pypi/v/XClientTransaction"></a>
<a href="https://github.com/iSarabjitDhiman/XClientTransaction/commits"> <img src="https://img.shields.io/github/last-commit/iSarabjitDhiman/XClientTransaction"></a>
<a href="https://img.shields.io/pypi/dd/XClientTransaction"> <img src="https://img.shields.io/pypi/dd/XClientTransaction"></a>
<a href="https://discord.gg/pHY6CU5Ke4"> <img alt="Discord" src="https://img.shields.io/discord/1149281691479851018?style=flat&logo=discord&logoColor=white"></a>
<a href="https://twitter.com/isarabjitdhiman"> <img src="https://img.shields.io/twitter/follow/iSarabjitDhiman?style=social"></a>

> Reference : https://antibot.blog/twitter/

## Usage/Examples

```python
python quickstart.py
```

OR (async)

```python
python quickstart_async.py
```

OR

```python
from x_client_transaction import ClientTransaction

response = None # get twitter home page response (check quickstart.py)
method = "POST"
path = "/1.1/jot/client_event.json"

ct = ClientTransaction(home_page_response=response)
print(ct.generate_transaction_id(method=method, path=path))
print(ct.generate_transaction_id(method="GET", path="/i/api/1.1/hashflags.json"))

```

OR (async)

```python
from x_client_transaction import AsyncClientTransaction

response = None # get twitter home page response (check quickstart_async.py)
method = "POST"
path = "/1.1/jot/client_event.json"

ct = AsyncClientTransaction()
await ct.get_transaction_id(response)
print(ct.generate_transaction_id(method=method, path=path))
print(ct.generate_transaction_id(method="GET", path="/i/api/1.1/hashflags.json"))

```


## Authors

- [@iSarabjitDhiman](https://www.github.com/iSarabjitDhiman)

## Feedback

If you have any feedback, please reach out to us at hello@sarabjitdhiman.com or contact me on Social Media @iSarabjitDhiman

## Support

For support, email hello@sarabjitdhiman.com
