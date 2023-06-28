import json
import argparse

from playwright.sync_api import sync_playwright



def search_google(query: str, headless: bool = True) -> None:
    """
    This function searches Google for the given query and returns the organic search results in JSON format.
    :param query: The search query
    :return: JSON data containing the organic search results
    """

    # Launch the browser and create a new page
    with sync_playwright() as playwright:
        try:
            # print("Launching browser")
            browser = playwright.chromium.launch(headless=True)
            # Set user agent to Chrome on Linux
            context = browser.new_context(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4454.0 Safari/537.36',
                                          permissions=['geolocation', 'notifications'])
            try:

                # print("Creating new page")
                page = context.new_page()


                # print("Navigating to Google")
                # Navigate to Google search page
                page.goto('https://www.google.com')

                # Get Iframe callout
                # print("Getting iframe")
                # check if iframe is visile if not continue

                # wait page is loaded
                page.wait_for_load_state('networkidle')

                
                # button accept cookies
                buttonAcceptAll = page.query_selector('button#L2AGLb')

                if buttonAcceptAll is not None:
                    #print("Accepting cookies")
                    buttonAcceptAll.click()
                else:
                    #print("No cookies to accept")
                    pass


                #if buttonAcceptAll is not None:
                #    print("Accepting cookies")
                #    buttonAcceptAll.click()
                #else:
                #    print("No cookies to accept")


                iframe = page.query_selector("iframe[name='callout']")

                if iframe is not None:
                    #print("Got iframe")
                    page.frame_locator("iframe[name='callout']").get_by_role(
                        'button').click()
                else:
                    #print("No iframe")
                    pass


                page.get_by_role("combobox", name="Search").click()
                page.get_by_role("combobox", name="Search").fill(query)
                page.get_by_role("combobox", name="Search").press("Enter")

                # print("Waiting for search results to load")
                # Wait for search results to load
                page.wait_for_selector('div#search')
                # print("Search results loaded")

                # Extract the search results
                results = page.query_selector_all('.g')

                # Create a list to store the search results
                search_results = []

                # Loop through each search result and extract the required information
                for index, result in enumerate(results):
                    position = index + 1

                    title = ''
                    link = ''
                    displayed_link = ''
                    favicon = ''
                    description = ''
                    snippet = ''
                    source = ''

                    if result is not None:
                        title_element = result.query_selector('h3')
                        if title_element is not None:
                            title = title_element.inner_text()
                        link_element = result.query_selector('a')
                        if link_element is not None:
                            link = link_element.get_attribute('href')
                        displayed_link_element = result.query_selector(
                            ".TbwUpd")
                        if displayed_link_element is not None:
                            displayed_link = displayed_link_element.inner_text()
                        favicon_element = result.query_selector(
                            '.eqA2re.NjwKYd img')
                        if favicon_element is not None:
                            favicon = favicon_element.get_attribute('src')
                        description_element = result.query_selector(
                            '.MUxGbd.yXK7lf.MUxGbd.yDYNvb.lyLwlc')
                        if description_element is not None:
                            description = description_element.inner_text()
                        snippet_element = result.query_selector(
                            '.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc span:last-child')
                        if snippet_element is not None:
                            snippet = snippet_element.inner_text()
                        source_element = result.query_selector(
                            '.TbwUpd.NJjxre.iUh30.apx8Vc.ojE3Fb span.VuuXrf')
                        if source_element is not None:
                            source = source_element.inner_text()

                    # Create a dictionary for each search result
                    result_dict = {
                        "position": position,
                        "title": title,
                        "link": link,
                        "displayed_link": displayed_link,
                        "favicon": favicon,
                        "description": description,
                        "snippet": snippet,
                        "source": source
                    }

                    # Append the result dictionary to the search_results list
                    search_results.append(result_dict)

                # Create a dictionary to store the final JSON result
                json_result = {
                    "organic_results": search_results
                }

                # Convert the dictionary to JSON format
                json_data = json.dumps(json_result, indent=2)

                # Print the JSON result
                print(json_data, end="")

                return json_data
            except Exception as e:
                print(e)
        finally:
            # Close the browser
            context.close()
            browser.close()


if __name__ == '__main__':
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
    search_google(query=args.query, headless=headless)
