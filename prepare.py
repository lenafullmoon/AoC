import datetime
import os
import requests


def create_file(path, content):
    if not os.path.exists(path):
        with open(path, 'w') as fp:
            fp.write(content)
    else:
        print(f'{path} file already exists')


if __name__ == '__main__':
    year, month, day = str(datetime.date.today()).split('-')

    try:
        input_content = requests.get(
             f'https://adventofcode.com/{year}/day/{int(day)}/input',
             headers={'cookie': os.environ.get('SESSION_ID')}
        ).content.decode().strip()
    except:
        input_content = ''
        print('Could not populate input file!')

    create_file(os.path.join(year, 'inputs', f'd{day}.txt'), input_content)

    create_file(os.path.join(year, f'd{day}.py'), f"""inputs_ = ''''''

if __name__ == '__main__':
    # with open('inputs/d{day}.txt') as fp:
    #     inputs_ = fp.read()
    pass
""")

    print('Have fun!')
