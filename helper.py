import os
import json
from random import randrange

r = 1

def open_sql_array(relative_path):
    file_object = open(relative_path, "r")
    file_string = file_object.read()
    file_object.close()
    command_array = file_string.split(";")
    return command_array

def execute_sql_commands(relative_path, cursor):
    commands = open_sql_array(relative_path)
    for c in commands:
        cursor.execute(c)

def open_json_file(full_path):
    fd = open(full_path, "r")
    item_list = json.loads(fd.read())
    fd.close()
    return item_list


def write_json_file(content, full_path):
    fd = open(full_path, "w")
    fd.write(json.dumps(content))
    fd.close()


def random_element(py_list):
    return py_list[randrange(len(py_list))]


def other_bin_ele(idx: int):
    # idx should 0 or 1
    if idx == 0:
        return 1
    else:
        return 0


def random_timestamp():
    # 17/10/21 - 1634510437
    # 2/17/22 - 1645137637
    return randrange(1634510437, 1645137637)


def create_directories(source_path, target_path):
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for dir in os.listdir(source_path):
        # print(dir)
        fp = target_path + "/" + dir
        if not os.path.exists(fp):
            os.mkdir(fp)

    # for _, dirs, _ in os.walk("input/louiscl1_20220209"):
    #     for name in dirs:
    #         tp = f"input/auto_dummy_data/{name}"
    #         if not os.path.exists(tp):
    #             os.mkdir(tp)
