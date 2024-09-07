"""Grab a screenshot for a given web url using playwright."""

from pathlib import Path
import asyncio
from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext
from pprint import pprint
import hashlib

DATA_DIR = "data"


async def grab_screenshot(urls: list[str]) -> None:
    """Grab and store screenshot using Playwright API.

    Args:
        urls (list[str]): List of url.
    """
    crawler = PlaywrightCrawler(
        # Limit the crawl to max requests. Remove or increase it for crawling all links.
        max_requests_per_crawl=10,
        # Headless mode, set to False to see the browser in action.
        headless=False,
        # Browser types supported by Playwright.
        browser_type="chromium",
    )

    # Define the default request handler, which will be called for every request.
    # The handler receives a context parameter, providing various properties and
    # helper methods. Here are a few key ones we use for demonstration:
    # - request: an instance of the Request class containing details such as the URL
    #   being crawled and the HTTP method used.
    # - page: Playwright's Page object, which allows interaction with the web page
    #   (see https://playwright.dev/python/docs/api/class-page for more details).
    @crawler.router.default_handler
    async def request_handler(context: PlaywrightCrawlingContext) -> None:
        context.log.info(f"Processing {context.request.url} ...")

        # TODO: Grab rest of the pages of the website and not only the homepage.

        # Extract data from the page using Playwright API.
        url_hash = hashlib.md5(str(context.request.url).encode("utf-8")).hexdigest()
        screenshot_path = f"{DATA_DIR}/screenshot_{url_hash}.png"
        data = {
            "url": context.request.url,
            "title": await context.page.title(),
            "screenshot": screenshot_path,
        }
        pprint(data)

        # Push the extracted data to the default dataset.
        await context.push_data(data)

        # Grab a full page screenshot of the website
        await context.page.screenshot(path=screenshot_path, full_page=True, type="png")

    # Run the crawler with the initial list of URLs.
    await crawler.run(urls)

    # Export the entire dataset to a JSON file
    await crawler.export_data(f"{DATA_DIR}/results.json")


async def main(urls: list[str]) -> None:
    """Main entrypoint.

    Args:
        urls (list[str]): List of urls
    """
    Path(DATA_DIR).mkdir(exist_ok=True)
    await grab_screenshot(urls)


if __name__ == "__main__":
    urls = ["https://www.fuzzylabs.ai/"]
    asyncio.run(main(urls))
