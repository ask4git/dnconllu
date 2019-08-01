
# -*- coding: utf-8 -*-

import os
import glob
from conllu import parse_incr

# ETRI = 0
# KNU = 1
# CNU = 2
# CBNU = 3


def pos_pre_processing(_dir_list):
    num_of_org = len(_dir_list)
    file = list(range(num_of_org))
    for i in range(num_of_org):
        file[i] = parse_incr(open(_dir_list[i], 'r', encoding='utf-8-sig'))
    print(file[1])


if __name__ == '__main__':

    root_dir_path = 'C:\\Users\\swishlike\\Desktop\\sample'
    pos_pre_processing(os.listdir(root_dir_path))

    # dir_etri_corpus = root_path + '\\etri'
    # dir_knu_corpus = root_path + '\\knu'
    # dir_cnu_corpus = root_path + '\\cnu'
    # dir_cbnu_corpus = root_path + '\\cbnu'
    #
    # dir_list = [dir_etri_corpus, dir_knu_corpus, dir_cnu_corpus, dir_cbnu_corpus]
    #
    # pos_pre_processing(dir_list)
