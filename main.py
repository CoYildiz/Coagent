import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from functions.generate_content import generate_content

def main() -> None:
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
    ]

  
    generate_content(client, messages, args.verbose)




if __name__ == "__main__":
    main()
