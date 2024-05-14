from http import HTTPStatus
from typing import List, Optional

import dashscope


def dashscope_completion(
        model: str,
        messages: List = [],
        base_url: Optional[str] = None,
        api_version: Optional[str] = None,
        api_key: Optional[str] = None,
        **kwargs,
):
    response = dashscope.Generation.call(
        model='qwen-turbo',
        api_key=api_key,
        prompt=messages[0]['content'],
        seed=1234,
        top_p=0.8,
        result_format='message',
        enable_search=False,
        max_tokens=1500,
        temperature=0.85,
        repetition_penalty=1.0
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
        response['choices'] = response['output']['choices']
        return response
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))