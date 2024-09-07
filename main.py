"""Main entrypoint."""

import os
import base64
import json
import asyncio
from dotenv import load_dotenv
from pathlib import Path
from grab_screenshot import grab_screenshot
from llm import call_llm
from pprint import pprint

# Path to store screenshot and results
DATA_DIR = "data"

URLS = ["https://www.fuzzylabs.ai/"]

PROMPT = """You are an expert in analyzing websites. 
Given the screenshot of only the home page, please provide feedback on how the home page's content can be improved. 
Also, comment on the style and image used and the home page content. It is not always required to critique, there will be some sections that will be good and need no further improvement. 
"""


def encode_image(image_path: str) -> str:
    """Convert screenshot image to base64.

    Args:
        image_path (str): Path to png screenshot image.

    Returns:
        str: Base64 encoded image
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def validate_env(selected_llm: str):
    """Validate if environment variables are set correctly."""
    if "claude" in selected_llm:
        if os.environ.get("ANTHROPIC_API_KEY", None):
            raise ValueError(
                "Set Claude API Key in `.env` file `ANTHROPIC_API_KEY='key-here'`"
            )


async def main() -> None:
    """Main entrypoint."""

    # Load environment variables (secrets for LLM)
    load_dotenv()
    Path(DATA_DIR).mkdir(exist_ok=True)

    await grab_screenshot(urls=URLS, data_dir=DATA_DIR)

    with open(f"{DATA_DIR}/results.json", "r") as fp:
        results = json.load(fp)

    llm_responses = []
    for data in results:
        response = await call_llm(
            model_name="anthropic/claude-3-opus-20240229",
            user_message=PROMPT,
            base64_image=encode_image(data["screenshot"]),
        )
        llm_responses.append(response)
    for i, data in enumerate(results):
        data.update({"llm_response": llm_responses[i]})

    pprint(results)

    # Create a new json with responses from LLM
    with open(f"{DATA_DIR}/analysis.json", "w") as fp:
        json.dump(results, fp)


if __name__ == "__main__":
    asyncio.run(main())
