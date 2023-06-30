import json
import asyncio
import playwright
from playwright.async_api import async_playwright


async def search(query: str, headless: bool = True) -> None:
    """
    This function searches Google for the given query and returns the organic search results in JSON format.
    :param query: The search query
    :return: JSON data containing the organic search results
    """

    # Launch the browser and create a new page
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=headless)
        context = await browser.new_context(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4454.0 Safari/537.36',
                                      permissions=['geolocation', 'notifications'])
        try:
            page = await context.new_page()

            # Navigate to Google search page
            await page.goto('https://www.google.com')

            # Get Iframe callout
            # check if iframe is visile if not continue

            # wait page is loaded
            await page.wait_for_load_state('networkidle')

            # button accept cookies
            buttonAcceptAll = await page.query_selector('button#L2AGLb')

            if buttonAcceptAll is not None:
                buttonAcceptAll.click()
            else:
                pass

            iframe = await page.query_selector("iframe[name='callout']")

            if iframe is not None:
                await page.frame_locator("iframe[name='callout']").get_by_role(
                    'button').click()
            else:
                pass

            await page.get_by_role("combobox", name="Search").click()
            await page.get_by_role("combobox", name="Search").fill(query)
            await page.get_by_role("combobox", name="Search").press("Enter")

            # Wait for search results to load
            await page.wait_for_selector('div#search')

            # Extract the search results
            results = await page.query_selector_all('.g')

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
                    title_element = await result.query_selector('h3')
                    if title_element is not None:
                        title = await title_element.inner_text()
                    link_element = await result.query_selector('a')
                    if link_element is not None:
                        link = await link_element.get_attribute('href')
                    displayed_link_element = await result.query_selector(
                        ".TbwUpd")
                    if displayed_link_element is not None:
                        displayed_link = await displayed_link_element.inner_text()
                    favicon_element = await result.query_selector(
                        '.eqA2re.NjwKYd img')
                    if favicon_element is not None:
                        favicon = await favicon_element.get_attribute('src')
                    description_element = await result.query_selector(
                        '.MUxGbd.yXK7lf.MUxGbd.yDYNvb.lyLwlc')
                    if description_element is not None:
                        description = await description_element.inner_text()
                    snippet_element = await result.query_selector(
                        '.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc span:last-child')
                    if snippet_element is not None:
                        snippet = await snippet_element.inner_text()
                    source_element = await result.query_selector(
                        '.TbwUpd.NJjxre.iUh30.apx8Vc.ojE3Fb span.VuuXrf')
                    if source_element is not None:
                        source = await source_element.inner_text()

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

            return json_data
        except Exception as e:
            print(e)
        finally:
            # Close the browser
            await context.close()
            await browser.close()