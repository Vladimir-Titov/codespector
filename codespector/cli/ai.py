import requests

import ujson


def send_to_review(diff_filename: str, *args, **kwargs):
    with open(diff_filename, 'r', encoding='utf-8') as f:
        diff_data = ujson.load(f)

    diff_content = diff_data.get('diff', '')
    original_files = diff_data.get('original files', [])

    original_files_str = ujson.dumps(original_files, indent=4, ensure_ascii=False)

    prompt = (
        'Пожалуйста, проверьте следующие изменения в коде на наличие очевидных проблем с качеством или безопасностью. '
        'Предоставьте краткий отчет в формате markdown:\n\n'
        'DIFF:\n'
        f'{diff_content}\n\n'
        'ORIGINAL FILES:\n'
        f'{original_files_str}'
    )

    request_data = {
        'model': 'codestral-latest',
        'messages': [{'role': 'system', 'content': 'Ты код ревьювер.'}, {'role': 'user', 'content': prompt}],
    }

    response = requests.post(
        'https://api.mistral.ai/v1/chat/completions',
        json=request_data,
        headers={'Authorization': f'Bearer {"example"}'},
        timeout=100,
    )

    with open('request.json', 'w', encoding='utf-8') as f:
        ujson.dump(request_data, f, indent=4, ensure_ascii=False)

    with open('response.json', 'w', encoding='utf-8') as f:
        ujson.dump(response.json(), f, indent=4, ensure_ascii=False)

    resp = response.json()
    clear_response = resp['choices'][0]['message']['content']

    with open('clear_response.txt', 'w', encoding='utf-8') as f:
        f.write(clear_response)
