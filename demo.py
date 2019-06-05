# '''
# The following file is about basic conllu manipulation. The necessary functionalities will be written here
# '''

#  #for parsing a conllu which has a single sentence

# data_file = open("demo_abstract.conll", "r", encoding="utf-8")
# tokenlist = parse_single(data_file) #tokenlist gives the parsed conllu file
# tokenTree = from conllu import parse_singletokenlist[0].to_tree()
# l = tokenlist[0]
# print(l.get_noun_chunks())



# # the tree will have the root, and then the children. Should be easy to access.


from os import listdir
from os.path import isfile, join

import sys
sys.path.append("../..")
sys.path.append("../../..")

from GSoC2019.syntaxnet_triplets.src import HearstPatterns
from GSoC2019.conllu.conllu import parse_single, TokenList

conll_data_path = '../abstract_conll_data/'
onlyfiles = [f for f in listdir(conll_data_path) if isfile(join(conll_data_path, f))]



h = HearstPatterns()
count = 0 
results = open('test.txt', 'w')
for conll_file in onlyfiles[:]:
    # data_file = open(conll_data_path + conll_file, "r", encoding="utf-8")
    # tokenList = parse_single(data_file)
    # sentence_tokenList = tokenList[0]
    # # print(conll_data_path + conll_file)
    # print(sentence_tokenList.get_noun_chunks())
    count += 1
    try:
        hearst_patterns = h.find_hearstpatterns(conll_data_path + conll_file)
        # print(hearst_patterns)
        results.write(conll_file + ' :- ' + str(hearst_patterns)+'\n')
    except:
        None
    
print(count)
results.close()
    # print(sentence_tokenList.get_noun_chunks())
