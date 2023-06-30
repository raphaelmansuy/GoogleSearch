import modal

playwright_image = modal.Image.debian_slim(python_version="3.10").run_commands(
    "apt-get install -y software-properties-common",
    "apt-add-repository non-free",
    "apt-add-repository contrib",
    "apt-get update",
    "apt-get install -y tree",
    "pip install playwright",
    "pip install asyncio",
    "playwright install-deps chromium",
    "playwright install chromium",
).copy_local_dir("./google_search", "/root/google_search")

# include local modules google/search.py and google/search.py
stub = modal.Stub("google-search", image=playwright_image)


@stub.function(image=playwright_image)
@modal.web_endpoint(method="GET")
async def search(query: str, headless: bool = True):
    import google_search.search as google_search
    res = await google_search.search(query=query, headless=headless)
    return res


@stub.local_entrypoint()
async def main(query: str):

    import json
    import argparse
    import asyncio
    # Get arguments from command line
    headless: bool = True
    try:
        res = await search.call(query=str, headless=headless)
        # Write the results in JSON format to stdout
        print(val, end="", flush=True, file=sys.stdout)
    except Exception as e:
        # print error message to stderr
        print(e, file=sys.stderr)
