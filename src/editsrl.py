
# semantic_role_labeling.py
# -*- coding: utf-8 -*-

from conllu import parse_incr


class SemanticRoleLabeling:
    @staticmethod
    def move_srltag_to_verb(conllu_data_file):
        for tokenlist in parse_incr(conllu_data_file):
            print(tokenlist)
            print(SemanticRoleLabeling.move_srltag_to_verb_in_sentence(tokenlist).serialize())

    @staticmethod
    def move_srltag_to_verb_in_sentence(tokenlist):
        srltag_list = []
        for token in tokenlist:
            if token["misc"] is None:
                continue
            taglist = str(token["misc"])[16:-9]
            id = token["id"]
            tags = taglist.split('), (')
            for tag in tags:
                tagset = tag.split(' / ')
                srltag_list.append([tagset[1], '(' + tagset[0] + ' / ' + str(id) + ')'])
            token["misc"] = None

        for dat in srltag_list:
            for token in tokenlist:
                if token["id"] == int(dat[0]):
                    if token["misc"] is None:
                        token["misc"] = dat[1].strip()
                    else:
                        token["misc"] += ', ' + dat[1].strip()
        return tokenlist

    @staticmethod
    def srltagprocess(_sentence):
        pass

    @staticmethod
    def to_json(input_file):
        pass
