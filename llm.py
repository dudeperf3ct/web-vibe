"""Interact with LLMs."""

from litellm import acompletion


async def call_llm(model_name: str, user_message: str, base64_image: str) -> str:
    """Call LLM endpoint.

    Args:
        model_name (str): Name of LLM and it's provider
        user_message (str): User message to be passed to LLM
        base64_image (str): Image encoded as base64

    Returns:
        str: Generate response from LLM
    """
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": "data:image/png;base64," + base64_image},
                },
                {"type": "text", "text": user_message},
            ],
        }
    ]
    response = await acompletion(model=model_name, messages=messages)
    return str(response["choices"][0]["message"]["content"])
