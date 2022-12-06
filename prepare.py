import datetime
import os


def create_file(path, content):
    if not os.path.exists(path):
        with open(path, 'w') as fp:
            fp.write(content)
    else:
        print(f'{path} file already exists')


if __name__ == '__main__':
    year, month, day = str(datetime.date.today()).split('-')

    create_file(os.path.join(year, 'inputs', f'd{day}.txt'), '')
    create_file(os.path.join(year, f'd{day}.py'), f"""inputs_ = ''''''

if __name__ == '__main__':
    # with open('inputs/d{day}.txt') as fp:
    #     inputs_ = fp.read()
    pass
""")

    print('Have fun!')
