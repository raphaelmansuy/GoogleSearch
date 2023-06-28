# Your goal

Complete the following python search_google t to get the HTML snippet of the search result page of Google into JSON format described in the following section.

Add the following result to the JSON format:

- favicon
- description
- snippet
- source

## The python code to complete or modify

```python
import json
import argparse

from playwright.sync_api import sync_playwright

def search_google(query: str) -> None:
    """
    This function searches Google for the given query and returns the organic search results in JSON format.
    :param query: The search query
    :return: JSON data containing the organic search results
    """

    # Launch the browser and create a new page
    with sync_playwright() as playwright:
        #print("Launching browser")
        browser = playwright.chromium.launch(headless=True)
        # Set user agent to Chrome on Linux
        context = browser.new_context(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4454.0 Safari/537.36')
        try: 

            #print("Creating new page")
            page = context.new_page()

            #print("Navigating to Google")
            # Navigate to Google search page
            page.goto('https://www.google.com')

            # Get Iframe callout
            #print("Getting iframe")
            page.frame_locator("iframe[name='callout']").get_by_role('button').click()
            #print("Got iframe")

            page.get_by_role("combobox",name="Search").click()
            page.get_by_role("combobox",name="Search").fill(query)
            page.get_by_role("combobox",name="Search").press("Enter")


            #print("Waiting for search results to load")
            # Wait for search results to load
            page.wait_for_selector('div#search')
            #print("Search results loaded")

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

                if result is not None:
                    title_element = result.query_selector('h3')
                    if title_element is not None:
                        title = title_element.inner_text()
                    link_element = result.query_selector('a')
                    if link_element is not None:
                        link = link_element.get_attribute('href')
                    displayed_link_element = result.query_selector(".TbwUpd")
                    if displayed_link_element is not None:
                        displayed_link = displayed_link_element.inner_text()

                # Create a dictionary for each search result
                result_dict = {
                    "position": position,
                    "title": title,
                    "link": link,
                    "displayed_link": displayed_link
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
            print(json_data,end="")

            return json_data

        finally:
            # Close the browser
            context.close()
            browser.close()


if __name__ == '__main__':
    ## Get arguments from command line
    parser = argparse.ArgumentParser(description='Search Google') 
    parser.add_argument('--query', type=str, help='Search query', required=True)
    args = parser.parse_args()
    # Call the search_google function
    search_google(args.query)
```

## The html snippet example of the search result page of Google

```html
<div>
  <div class="MjjYud">
    <div
      jscontroller="SC7lYd"
      class="g Ww4FFb vt6azd tF2Cxc asEBEc"
      lang="fr"
      style="width: 652px"
      jsaction="QyLbLe:OMITjf;ewaord:qsYrDe;xd28Mb:A6j43c"
      data-hveid="CBMQAA"
      data-ved="2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4QFSgAegQIExAA"
    >
      <div class="GLI8Bc UK95Uc" data-snc="ih6Jnb_jTzNo">
        <div
          class="Z26q7c UK95Uc jGGQ5e VGXe8"
          data-snf="x5WNvb"
          data-snhf="0"
          style="grid-area: x5WNvb"
        >
          <div class="yuRUbf">
            <a
              href="https://www.pandassur.fr/"
              jscontroller="M9mgyc"
              jsname="qOiK6e"
              jsaction="rcuQ6b:npT2md"
              data-ved="2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4QFnoECBEQAQ"
              ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.pandassur.fr/&amp;ved=2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4QFnoECBEQAQ"
              ><br />
              <h3 class="LC20lb MBeuO DKV0Md">
                Pandassur: Assurance emprunteur au meilleur prix
              </h3>
              <div class="TbwUpd NJjxre iUh30 apx8Vc ojE3Fb">
                <span class="H9lube"
                  ><div class="eqA2re NjwKYd Vwoesf" aria-hidden="true">
                    <img
                      class="XNo5Ab"
                      src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAhFBMVEVHcEwaGhoVFRULCwsYFxcZGRn+///6/Pz9///9///9///+///T1NQXFhYVFRUYGBgBAQH8/f39///////4+vr///+trq59fn6RkpKys7PDxMQWFhYaGhqdnp7o6Ojk5eXi4uLw8PBsbGzX2Ng7OzsfHx+srKxRUlJYWFgbGxseHh4fHx//FXBsAAAALHRSTlMAXer/uBY0W5eyxH4aSsws/+r///6gXf//////d/v//9P//////4r/maaN42NiUosAAAG8SURBVHgBZZCJopsgEEXHLXuUBPpESfChmZLl//+vlyBp+zxZWO5hHKFIlhdlhXG13mx3u+1+fSA65kXdpLwoClEf9qezPEfUry+BzZwiJXLRnkKSkEoLKMco1Mi7dDghOxjZ/AgheuRLw9DMBeeXyGuThFXIl5wOSdjFE1J+xjjZpAJx23a9QiSHvp8VFfPDd8jdKIQwVkqNMb3U6p1PLsi3cDMIJGOSjDWBbwtBdu9tgeI3DIW4qST8tkMQrti89rfwiHHyQvAgUfaLqOmTIFjKSaIZJ7sk3Inuk7UWwoTCo5IhPoe5f79PSdWIPDYx6kGqlnlUqh/bIQi6pqx1dkAJrMDZoUN2MhCqck2P0dnAeWbyfkr3qLypqfY4P+DjflwzmvUFl5Sb3r4ZOxWzWVMdG+YHsQldoooWvrNwYiuT9oLBk3I2OnThemOE8a2+XnU7olXDgQu9mEU0PLZMuO6iMDEFGZUMw/fOuU7wkiNdGBj2Wt8ML2moiRPURr6kIjSx4PFIsxcRZWlRcqJpPiqBFNCTIzVRnVQCVT5vV/PTnkSXT4FAkxaXz7EqnqloNjIQFlngSOCYtv4ApdlVJNagPf8AAAAASUVORK5CYII="
                      style="height: 18px; width: 18px"
                      alt=""
                      data-atf="1"
                      data-frt="0"
                    /></div
                ></span>
                <div>
                  <span class="VuuXrf">pandassur.fr</span>
                  <div class="byrV5b">
                    <cite
                      class="apx8Vc tjvcx GvPZzd cHaqb"
                      role="text"
                      style="max-width: 212px"
                      >https://www.pandassur.fr</cite
                    >
                  </div>
                </div>
              </div></a
            >
            <div class="B6fmyf byrV5b Mg1HEd">
              <div class="TbwUpd iUh30 apx8Vc ojE3Fb">
                <span class="H9lube"
                  ><div
                    class="eqA2re NjwKYd"
                    style="height: 18px; width: 18px"
                  ></div
                ></span>
                <div>
                  <span class="VuuXrf">pandassur.fr</span>
                  <div class="byrV5b">
                    <cite
                      class="apx8Vc tjvcx GvPZzd cHaqb"
                      role="text"
                      style="max-width: 212px"
                      >https://www.pandassur.fr</cite
                    >
                  </div>
                </div>
              </div>
              <div class="csDOgf BCF2pd ezY6nb L48a4c">
                <div
                  jscontroller="exgaYe"
                  data-bsextraheight="0"
                  data-frm="true"
                  data-isdesktop="true"
                  data-movewtractions="true"
                  jsdata="l7Bhpb;_;AH4b/8 cECq7c;_;AH4cAE"
                  data-ved="2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4Q2esEegQIERAH"
                >
                  <div
                    role="button"
                    tabindex="0"
                    jsaction="RvIhPd"
                    jsname="I3kE2c"
                    class="iTPLzd rNSxBe lUn2nc"
                    style="position: absolute"
                    aria-label="About this result"
                  >
                    <span jsname="czHhOd" class="D6lY4c mBswFe"
                      ><span
                        jsname="Bil8Ae"
                        class="xTFaxe z1asCe SaPW2b"
                        style="height: 18px; line-height: 18px; width: 18px"
                        ><svg
                          focusable="false"
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 24 24"
                        >
                          <path
                            d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"
                          ></path></svg></span
                    ></span>
                  </div>
                  <span
                    jsname="zOVa8"
                    data-ved="2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4Qh-4GegQIERAI"
                  ></span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="Z26q7c UK95Uc Sth6v"
          data-sncf="0,1,2,3"
          data-snf="Vjbam"
          style="padding-left: 20px; grid-area: Vjbam; width: 92px"
        >
          <div>
            <a
              href="https://www.pandassur.fr/"
              jsname="ACyKwe"
              data-ved="2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4Qqa4BegQIFBAA"
              ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.pandassur.fr/&amp;ved=2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4Qqa4BegQIFBAA"
              ><div
                class="LicuJb uhHOwf BYbUcd"
                aria-hidden="true"
                style="border-radius: 8px; height: 92px; width: 92px"
              >
                <img
                  alt="pandassur from www.pandassur.fr"
                  id="dimg_1"
                  src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFwAAABcCAMAAADUMSJqAAAAkFBMVEX///8AAADSVmv09PTFxcXRUWejo6Pvys/Nzc3PRFzRU2nq6uodHR3QS2L57O7f398jIyNHR0f99/hubm5gYGC6urqzs7Orq6uLi4sqKio6OjpWVlZCQkJOTk55eXnT09PXbH0zMzODg4MWFhb02t7cg5HosrqWlpYODg7fkZ3aeonkoqzswcfUYHPNOlbimqXML/WeAAAEJUlEQVRoge2Y65aqOBBGK4SoyCUooCIXuamgYr//201VArSesc+vOWvNrOHrliRl2EmqKnRogFmzZs2aNWvWf0T8kK/+GHzV1gGVtrTHK1cfDljHmpRg28Ov6sGpkKrg6iayfobncVZjv2vplyuIjn65h8qXYNZ7zoIqwO/rKg0hywKnXAAcyjY1gQe+k0iIUge7o/bHj2xeJhHbAbBAJhnPYjvwecUQzhDu11XUbqLUD2Hj5JHvSJOFu5rZFdtFxxiOR+wucfUs+wiPWAQsBCjbIMJl4L0cqnaAJwBBLUHGCC9tWLAVjQucZ/71kDKes2RH3jm0n8MW+lkY4+j2Lsf5cbMqj7xqTzgouQXhWFfwdIJjXDLH3O0XnEeHEu1wbc2PXmGbPA+dK48rmcQyTHjQykUb7tJaw3dttsj8EX5Ct+yPLT+w/T4LIQntnJayapNP8AXDgHAnxgpD15s+YwfgCWMVW3ByF1SM5XUGpW/DlZlwYKxeYUAZ26DvYupOAW0/Z8sk++XKXxfHP/UbrD+k4KxZs2bNmvUvlX24Xg/yD8FP+KeafTwq/H/g78cGdV54g2+3v96xfTdNzQXIIM9zDFZEJefXMEuqKXZmsEnD/Su86YridgGv67pzoyyPM1q65Ui+qKb6im1MunEF6nzlRExroWed6FYZTfDbU6zXwhVLQ4gnARvDQstaWDc13aXrUgfx7AjOnBf4t9QRdfNmIvjZNVBr/EFZCPcMYRiuRZcbfu890Y58vHwBtBNrgKepKuhwrS31sZ3gSwvvFeueiBp+odEujw6LJ7riLnDcx4PmIDyQyTv8xPlKVWxaFSqXXIYj/IZQcfO2HsEUHCvii9zlutYdVyYM94LNApuPce0jPIJxxngEpyJUzk803KN5F8qCFAW/4yj9Y6tSBK8dzrxfTk3YvwZUpclKW76jOFYbJLkPnTSuhjcuBsB1+7vOnAZ9js3iopsjSsPV8fekLTsqdFKeXuA655rBLfDoKXwIvCneReBoBqbT2Ztm9QZfvcD1i435d/jgFkyQSyGIL1yVi81dN92CmsFPcDVd9ZKAL13a58Q4K8t9gtPGWX7RsPeh6S3Pg/+u7Ce4zpbdlJPo/gKXrLJB5STBRVH0FAUMLA7rGUVR0JAYWBwrZT/DK534YTrl+YWYbnEu3DHPeyGEsfQ8HFZ0sKVm33hNv6ZJsN/A7fjXHbotaPesxVrtIoIvXYrmmrxMT4OHyhaDguo2wNrFj3DtddJ1zErPpfsM8bzgTtTZYimLIawvFYun2rzUA8NpS+Y4+KaH+e44sU7F2nF0mtgqkoGkPsNL6723nph2Xj8mjvfVu0/LOA/RbTrDelrrbkh0ztUzmw/lt0VVh39FfFu2nkdJtv1+iKPFe3mg/9KcNWvWrFmzZs36R/QXI3FN5we7YTwAAAAASUVORK5CYII="
                  data-atf="1"
                  data-frt="0"
                /></div
            ></a>
          </div>
        </div>
        <div
          class="Z26q7c UK95Uc VGXe8"
          data-sncf="2"
          data-snf="nke7rc"
          style="grid-area: nke7rc"
        >
          <div class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc">
            <span
              ><em>pandassur</em> est une Société par Actions Simplifiée au
              capital de 6 000.00 €, inscrite au registre du commerce et des
              sociétés de Bar-le-Duc sous le numéro 910 702&nbsp;...</span
            >
          </div>
        </div>
        <div
          class="Z26q7c UK95Uc VGXe8"
          data-sncf="3"
          data-snf="EXKWif"
          style="grid-area: EXKWif"
        >
          <div class="MUxGbd wuQ4Ob WZ8Tjf">
            You've visited this page many times. Last visit: 6/27/23
          </div>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div
      jscontroller="SC7lYd"
      class="g Ww4FFb vt6azd tF2Cxc asEBEc"
      lang="en"
      style="width: 652px"
      jsaction="QyLbLe:OMITjf;ewaord:qsYrDe;xd28Mb:A6j43c"
      data-hveid="CBsQAA"
      data-ved="2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4QFSgAegQIGxAA"
    >
      <div class="GLI8Bc UK95Uc" data-snc="ih6Jnb_PZxWLc">
        <div
          class="Z26q7c UK95Uc jGGQ5e VGXe8"
          data-snf="x5WNvb"
          data-snhf="0"
          style="grid-area: x5WNvb"
        >
          <div class="yuRUbf">
            <a
              href="https://www.elitizon.com/2023/19-04-pandassur/"
              jscontroller="M9mgyc"
              jsname="qOiK6e"
              jsaction="rcuQ6b:npT2md"
              data-ved="2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4QFnoECBUQAQ"
              ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.elitizon.com/2023/19-04-pandassur/&amp;ved=2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4QFnoECBUQAQ"
              ><br />
              <h3 class="LC20lb MBeuO DKV0Md">Launch of pandassur.fr</h3>
              <div class="TbwUpd NJjxre iUh30 apx8Vc ojE3Fb">
                <span class="H9lube"
                  ><div class="eqA2re NjwKYd Vwoesf" aria-hidden="true">
                    <img
                      class="XNo5Ab"
                      src="data:image/png;base64,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"
                      style="height: 18px; width: 18px"
                      alt=""
                      data-atf="1"
                      data-frt="0"
                    /></div
                ></span>
                <div>
                  <span class="VuuXrf">elitizon</span>
                  <div class="byrV5b">
                    <cite
                      class="apx8Vc qLRx3b tjvcx GvPZzd cHaqb"
                      role="text"
                      style="max-width: 315px"
                      >https://www.elitizon.com<span
                        class="apx8Vc dyjrff ob9lvb"
                        role="text"
                      >
                        › 19-04-pandassur</span
                      ></cite
                    >
                  </div>
                </div>
              </div></a
            >
            <div class="B6fmyf byrV5b Mg1HEd">
              <div class="TbwUpd iUh30 apx8Vc ojE3Fb">
                <span class="H9lube"
                  ><div
                    class="eqA2re NjwKYd"
                    style="height: 18px; width: 18px"
                  ></div
                ></span>
                <div>
                  <span class="VuuXrf">elitizon</span>
                  <div class="byrV5b">
                    <cite
                      class="apx8Vc qLRx3b tjvcx GvPZzd cHaqb"
                      role="text"
                      style="max-width: 315px"
                      >https://www.elitizon.com<span
                        class="apx8Vc dyjrff ob9lvb"
                        role="text"
                      >
                        › 19-04-pandassur</span
                      ></cite
                    >
                  </div>
                </div>
              </div>
              <div class="csDOgf BCF2pd ezY6nb L48a4c">
                <div
                  jscontroller="exgaYe"
                  data-bsextraheight="0"
                  data-frm="true"
                  data-isdesktop="true"
                  data-movewtractions="true"
                  jsdata="l7Bhpb;_;AH4cAM cECq7c;_;AH4cAQ"
                  data-ved="2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4Q2esEegQIFRAJ"
                >
                  <div
                    role="button"
                    tabindex="0"
                    jsaction="RvIhPd"
                    jsname="I3kE2c"
                    class="iTPLzd rNSxBe lUn2nc"
                    style="position: absolute"
                    aria-label="About this result"
                  >
                    <span jsname="czHhOd" class="D6lY4c mBswFe"
                      ><span
                        jsname="Bil8Ae"
                        class="xTFaxe z1asCe SaPW2b"
                        style="height: 18px; line-height: 18px; width: 18px"
                        ><svg
                          focusable="false"
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 24 24"
                        >
                          <path
                            d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"
                          ></path></svg></span
                    ></span>
                  </div>
                  <span
                    jsname="zOVa8"
                    data-ved="2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4Qh-4GegQIFRAK"
                  ></span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="Z26q7c UK95Uc Sth6v"
          data-sncf="0,1,2,3"
          data-snf="Vjbam"
          style="padding-left: 20px; grid-area: Vjbam; width: 92px"
        >
          <div>
            <a
              href="https://www.elitizon.com/2023/19-04-pandassur/"
              jsname="ACyKwe"
              data-ved="2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4Qqa4BegQIGhAA"
              ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.elitizon.com/2023/19-04-pandassur/&amp;ved=2ahUKEwi87di_iuX_AhXIM0QIHQp9Da4Qqa4BegQIGhAA"
              ><div
                class="LicuJb uhHOwf BYbUcd"
                aria-hidden="true"
                style="border-radius: 8px; height: 92px; width: 92px"
              >
                <img
                  alt="pandassur from www.elitizon.com"
                  id="dimg_3"
                  src="data:image/png;base64,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"
                  data-atf="5"
                  data-frt="0"
                /></div
            ></a>
          </div>
        </div>
        <div
          class="Z26q7c UK95Uc VGXe8"
          data-sncf="2"
          data-snf="nke7rc"
          style="grid-area: nke7rc"
        >
          <div class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc">
            <span class="MUxGbd wuQ4Ob WZ8Tjf"
              ><span>Apr 18, 2023</span> — </span
            ><span
              >Welcome to <em>Pandassur</em>, a groundbreaking loan insurance
              broker in France that aims to make the process of obtaining
              insurance more accessible,&nbsp;...</span
            >
          </div>
        </div>
        <div
          class="Z26q7c UK95Uc VGXe8"
          data-sncf="3"
          data-snf="EXKWif"
          style="grid-area: EXKWif"
        >
          <div class="MUxGbd wuQ4Ob WZ8Tjf">
            You've visited this page many times. Last visit: 5/20/23
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

## The example of the json result I want to get

```json
{
  "organic_results": [
    {
      "position": 1,
      "title": "Pandassur: Assurance emprunteur au meilleur prix",
      "link": "https://www.pandassur.fr/",
      "displayed_link": "https://www.pandassur.fr",
      "favicon": "https://serpapi.com/searches/649b809e1d986e4159b015ef/images/ac537d6b0c8b0d9c3e78737ba299da3e3d586dffda7a4f1f4066691069295be5.png",
      "snippet": "Pandassur est spécialisé dans les assurances emprunteurs au meilleur prix. Contactez-nous dès maintenant pour obtenir un devis gratuit et souscrire en ...",
      "snippet_highlighted_words": ["Pandassur"],
      "about_this_result": {
        "keywords": ["pandassur"],
        "languages": ["français"],
        "regions": ["France"]
      },
      "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:-1W3_dJUALgJ:https://www.pandassur.fr/&cd=1&hl=fr&ct=clnk&gl=fr",
      "source": "pandassur.fr"
    },
    {
      "position": 2,
      "title": "pandassur",
      "link": "https://www.youtube.com/channel/UCJ8sMmrJKw4W0bibuZaeaNw",
      "displayed_link": "https://www.youtube.com/channel",
      "favicon": "https://serpapi.com/searches/649b809e1d986e4159b015ef/images/ac537d6b0c8b0d9c3e78737ba299da3e1a76be392fc6f9adf2ea9aa754be5ee5.png",
      "snippet": "Bienvenue sur notre chaîne Youtube dédiée aux finances personnelles et à l'assurance emprunteur au juste prix. Restez à jour sur les dernières tendances du ...",
      "about_this_result": {
        "keywords": ["pandassur"],
        "languages": ["français"],
        "regions": ["France"]
      },
      "source": "YouTube"
    }
  ]
}
```
