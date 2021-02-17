# coding=utf-8

import json
import csv
from pprint import pprint
import os
import re
from tqdm import tqdm
from collections import Counter


def save_json(obj, f_name):
    with open(f_name + ".json", "w") as f:
        f.write(json.dumps(obj, indent=2, ensure_ascii=False))
    print(f_name + ".json saved")


def load_json(f_path):
    with open(f_path) as f:
        res_ = json.load(f)
        print(f"[LOAD] {f_path} loaded")
        return res_


def save_csv(dict_list_data, f_name):
    with open(f_name + ".csv", 'w') as f:
        dw = csv.DictWriter(f, dict_list_data[0].keys())
        dw.writeheader()
        for row in dict_list_data:
            for k in row:
                if isinstance(row[k], list) or isinstance(row[k], dict):
                    row[k] = json.dumps(row[k], ensure_ascii=False)
            dw.writerow(row)
    print(f_name + ".csv saved")


def print_json(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def load_csv(f_path):
    with open(f_path) as f:
        csv_dict_list = csv.DictReader(f, delimiter=',')
        res_ = [dict(csv_dict) for csv_dict in csv_dict_list]
        print(f"[LOAD] {f_path} loaded")
        return res_


def remove_stop_and_punc(word_list):
    res = list()
    for word in word_list:
        if word not in STOP_WORD and word not in STOP_PUNCTUATION:
            res.append(word)
    return res


def save_list_list(list_list, f_name):
    with open(f_name + ".txt", "w") as f:
        for list_ in list_list:
            f.write(" ".join([str(e) for e in list_]) + "\n")
    print(f_name + ".txt saved")


def get_project_root():
    return os.path.split(os.path.realpath(__file__))[0]


def list2dict(list_, k_name):
    return {list_iter_[k_name]: list_iter_ for list_iter_ in list_}


if __name__ == '__main__':
    print(get_project_root())
