# Возьмите любые 1-3 задания из прошлых домашних заданий. 
# Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров. 
# Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет" "Зачет" ставится, 
# если Слушатель успешно выполнил задание. 
# "Незачет" ставится, если Слушатель не выполнил задание. 
# Критерии оценивания: слушатель написал корректный код для задачи, 
# добавил к ним логирование ошибок и полезной информации.

import os
from collections import namedtuple
import argparse
import logging

LOG_FORMAT = '{levelname:<3} - {asctime}. ' \
         '{msg}'


def logging():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', metavar='directory', default=None)
    args = parser.parse_args()
    print(f'{args.d}')
    FileOrDirectory = namedtuple(
        'FileOrDirectory', 'name type flag_directory parent', defaults=[None, None, None, None])

    data = []
    for dir_path, dir_name, file_name in os.walk(f'{args.d}'):
        for elem in file_name:
            name_f = elem.split('.')
            if len(name_f) < 2:
                name_f = [str(name_f).strip("[]'"), None]
            data.append(FileOrDirectory(name=name_f[0], type=name_f[1], flag_directory=False,
                                        parent=str(dir_path)))
        for elem in dir_name:
            data.append(FileOrDirectory(name=elem, flag_directory=True,
                                        parent=str(dir_path)))
    logging.basicConfig(format=LOG_FORMAT, style='%', filename='logger.log', filemode='w', encoding='utf-8',
                        level=logging.INFO)
    logger = logging.getLogger()
    for item in data:
        logger.info(item)


if __name__ == '__main__':
    print(logging())



#  'C:\Users\79995\Desktop\GEEK BRAINS\6.seminars\2semester\python2\hm\dz15'