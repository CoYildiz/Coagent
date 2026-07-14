from openai import OpenAI
from .call_function import available_functions, call_function
import json



def generate_content(client: OpenAI, messages: list[dict[str,str]], verbose: bool) -> None:
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        
        if not response.usage:
            raise RuntimeError("API response appears to be malformed")
        if verbose:
            print("User prompt:", messages[1]["content"])
            print("Prompt tokens:", response.usage.prompt_tokens)
            print("Response tokens:", response.usage.completion_tokens)


        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, verbose)

                if not result_message["content"]:
                    raise RuntimeError("Function returned no content")

                
                messages.append(result_message)
                
                if verbose:
                    print(f"-> {result_message['content']}")
        else:
            print("Final response:")
            print(message.content)
            break


        
