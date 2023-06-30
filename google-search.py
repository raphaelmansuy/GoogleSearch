import json
import argparse
import sys
import asyncio


import google.search as google_search


async def main():
    # Get arguments from command line
    headless: bool = True
    parser = argparse.ArgumentParser(description='Search Google')
    parser.add_argument('--query', type=str,
                        help='Search query', required=True)
    # Add healdless argument
    parser.add_argument('--headless', type=bool,
                        help='Headless mode', required=False, default=True)
    args = parser.parse_args()
    if args.headless == False:
        headless = False
    #print("Headless =", args.headless)    
    # Call the search_google function
    res = await google_search.search(query=args.query, headless=False)

    # Print the results in JSON format to stdout nicely formatted 
    # inccluding a special character to be used with jq


    # Write the results in JSON format to stdout
    sys.stdout.write(res)


if __name__ == '__main__':
    asyncio.run(main())