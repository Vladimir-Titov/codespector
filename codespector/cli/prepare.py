import subprocess
import json
import os


def prepare(*args, **kwargs):
    name_only_file = _prepare_name_only_file(*args, **kwargs)
    code_changes = _prepare_diff_file(name_only_file, *args, **kwargs)
    return code_changes

def _prepare_diff_file(name_only_filename: str, *args, **kwargs):
    diff_output = subprocess.run(['git', 'diff', 'origin/master'], stdout=subprocess.PIPE, text=True).stdout

    filtered_diff = [
        line
        for line in diff_output.splitlines()
        if (line.startswith('+') or line.startswith('-')) and not line.startswith('+++') and not line.startswith('---')
    ]

    with open('code_changes_only.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(filtered_diff))

    diff_json = {'diff': '\n'.join(filtered_diff)}
    with open('diff.json', 'w', encoding='utf-8') as f:
        json.dump(diff_json, f, indent=4, ensure_ascii=False)

    print('Файл diff.json успешно создан.')

    if os.path.exists('original_files_temp.json'):
        with open('original_files_temp.json', 'r', encoding='utf-8') as f:
            original_files_data = json.load(f)

        with open('diff.json', 'r', encoding='utf-8') as f:
            diff_data = json.load(f)

        combined_data = {**original_files_data, **diff_data}

        with open('combined.json', 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, indent=4, ensure_ascii=False)

        os.replace('combined.json', 'diff.json')
        print('Файлы original_files_temp.json и diff.json объединены в diff.json.')
    else:
        print('Файл original_files_temp.json не найден, создан только diff.json.')


def _prepare_name_only_file(*args, **kwargs):
    changed_files = subprocess.run(
        ['git', 'diff', '--name-only', 'origin/master'], stdout=subprocess.PIPE, text=True
    ).stdout.splitlines()

    result = {'original files': []}

    for file in changed_files:
        if file.endswith('.json') or file.endswith('.png'):
            continue

        if os.path.isfile(file):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()

            result['original files'].append({'filename': file, 'content': content})
    filename = 'original_files_temp.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    return filename
