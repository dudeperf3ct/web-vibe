# Web Vibe

## Getting Started

Pre-requisities

- [uv](https://docs.astral.sh/uv/)

1. Create a virtual environment and install dependencies using `uv`.

    ```bash
    uv venv --python 3.10
    source .venv/bin/activate
    uv pip install .
    playwright install
    ```

2. Add API secrets to `.env` file.

3. Run the python script.

    ```bash
    uv run python main.py
    ```
