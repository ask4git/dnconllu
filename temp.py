
# -*- coding: utf-8 -*-

import src.editconllu as ed
from conllu import parse_incr

#
# data = 'cbnu_data'
#
# input_file_path = "C:\\Users\\swishlike\\Desktop\\" + data + ".txt"
# output_file_path = "C:\\Users\\swishlike\\Desktop\\" + data + "_srlchanged.txt"
# output_dir_path = "C:\\Users\\swishlike\\Desktop\\" + data
#
# # # 의미역 정보 변경
# # with open(input_file_path, 'r', encoding='utf-8-sig') as input_file, \
# #         open(output_file_path, 'w', encoding='utf-8-sig') as output_file:
# #     ed.swich_conllu_column(input_file, output_file, 5, 7)
#
#
# # 말뭉치 분할
# with open(output_file_path, 'r', encoding='utf-8-sig') as input_file:
#     ed.split_to_conllu_corpus(input_file, output_dir_path, 10)
#
#
