import httpx
import asyncio
from x_client_transaction.utils import handle_x_migration_async
from x_client_transaction.transaction import AsyncClientTransaction

async def test():
    headers = {"Authority": "x.com",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Referer": "https://x.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "X-Twitter-Active-User": "yes",
            "X-Twitter-Client-Language": "en"}

    session = httpx.AsyncClient(headers=headers)
    response = await handle_x_migration_async(session)

    method = "POST"
    path = "/1.1/jot/client_event.json"
    ct = AsyncClientTransaction()
    await ct.get_transaction_id(response)
    transaction_id = ct.generate_transaction_id(method=method, path=path)

    print(transaction_id)

asyncio.run(test())