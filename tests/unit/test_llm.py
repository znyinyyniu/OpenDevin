from opendevin.llm.llm import LLM


def test_completion():
    llm = LLM(model='qwen-max-longcontext')
    messages = [{'role': 'user', 'content': 'Hello, how are you?'}]
    res = llm.completion(messages=messages)
    print(res)
