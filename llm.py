"""Interact with LLMs."""

from litellm import acompletion


async def call_llm(model_name: str, user_message: str, base64_image: str) -> str:
    """_summary_

    Args:
        model_name (str): _description_
        user_message (str): _description_
        base64_image (str): _description_

    Returns:
        str: _description_
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
