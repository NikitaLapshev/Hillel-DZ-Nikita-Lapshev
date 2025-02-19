import asyncio
import time
import random
import argparse
import requests
import httpx

BASE_URL = "https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

# Sync request using requests library
def http_request(url: str) -> str:
    print(f"requesting {url}")
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["name"]

# Async request using httpx
async def httpx_request(url: str) -> str:
    print(f"requesting {url}")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()["name"]

# Generate random Pokemon URLs
def get_urls(n: int) -> list[str]:
    return [BASE_URL.format(pokemon_id=random.randint(1, 500)) for _ in range(n)]

# Synchronous function to fetch Pokemon names
def sync_pokemons():
    urls = get_urls(n=50)
    results = [http_request(url) for url in urls]
    return results

# Asynchronous function to fetch Pokemon names
async def async_pokemons():
    urls = get_urls(n=50)
    tasks = [httpx_request(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

# Main function to handle CLI arguments and execute
def main():
    parser = argparse.ArgumentParser(description="Fetch Pokemon names synchronously or asynchronously.")
    parser.add_argument("library", choices=["requests", "httpx"], help="Choose the library to use: 'requests' for sync, 'httpx' for async.")
    args = parser.parse_args()

    start = time.perf_counter()

    if args.library == "requests":
        print("Using requests for synchronous execution...")
        data = sync_pokemons()
    elif args.library == "httpx":
        print("Using httpx for asynchronous execution...")
        data = asyncio.run(async_pokemons())

    end = time.perf_counter()

    print(data)
    print(f"The length of the collection: {len(data)}")
    print(f"Execution time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
