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
import time

import sys
sys.path.append("../..")
sys.path.append("../../..")

from GSoC2019.syntaxnet_triplets.src import HearstPatterns
from GSoC2019.conllu.conllu import parse_single, TokenList

conll_data_path = '../abstract_conll_data/'
onlyfiles = [f for f in listdir(conll_data_path) if isfile(join(conll_data_path, f))]


trial = ['Ludlow.conll', 'Church_of_Satan.conll', 'Walt_Whitman.conll',
            'Cathode_ray_tube.conll', 'Shamgar.conll', 'Rainer_Werner_Fassbinder.conll',
            'Transport_in_Thailand.conll', 'Foreign_relations_of_Uzbekistan.conll',
            'Walvis_Bay.conll', 'Berkeley%2C_California.conll', 'Gaius_Marcius_Coriolanus.conll']


test1 = [
    "Asexual_reproduction.conll",
    "Simonides_of_Ceos.conll",
    "Hawaii.conll"
]

test2 = [
    "Anger.conll",
    "Osman_I.conll",
    "Lillehammer.conll"
]

test3 = [
    "Amalthea_%28moon%29.conll",
    "Haggai.conll",
    "Himachal_Pradesh.conll"
]

h = HearstPatterns(semi=True)
count = 0 
# results = open('test.txt', 'w')
start = time.time()
for conll_file in test3:
    # data_file = open(conll_data_path + conll_file, "r", encoding="utf-8")
    # tokenList = parse_single(data_file)
    # sentence_tokenList = tokenList[0]
    # # # print(conll_data_path + conll_file)
    # print(sentence_tokenList.get_noun_chunks(conll_file[:-6]))
    # count += 1
    try:
        hearst_patterns = h.find_hearstpatterns(conll_data_path + conll_file, conll_file[:-6])
        print(hearst_patterns)
        # print('\n\n')
        # results.write(conll_file + ' :- ' + str(hearst_patterns)+'\n')
    except:
        None
end = time.time()
print(count)
# results.close()
    # print(sentence_tokenList.get_noun_chunks())

print("time taken  - ", end-start)

print("\n\n\n")


for conll_file in test3:
    data_file = open(conll_data_path + conll_file, "r", encoding="utf-8")
    tokenList = parse_single(data_file)
    sentence_tokenList = tokenList[0]
    # # # print(conll_data_path + conll_file)
    print(sentence_tokenList.get_noun_chunks(conll_file[:-6]))
    # count += 1
    # try:
    #     hearst_patterns = h.find_hearstpatterns(conll_data_path + conll_file, conll_file[:-6])
    #     print(hearst_patterns)
    #     # print('\n\n')
    #     # results.write(conll_file + ' :- ' + str(hearst_patterns)+'\n')
    # except:
    #     None

'''

abstracts

1. Ludlow (movie)
2. Church_of_Satan (place)
3. Walt_Whitman (person)
4. Cathode_ray_tube (thing)
5. Shamgar (person)
6. Rainer_Werner_Fassbinder (person)
7. Transport_in_Thailand (thing)
8. Foreign_relations_of_Uzbekistan (thing)
9. Walvis_Bay (place)
10. Berkeley%2C_California (place)
11. Gaius_Marcius_Coriolanus (person)


Test - 1

1. Asexual_reproduction (thing)
2. Simonides_of_Ceos (place)
3. Hawaii


Test - 2

1. Anger (thing)
2. Osman_I (person)
3. Lillehammer (place)

Test - 3

1. Amalthea_%28moon%29 (thing)
2. Haggai (person)
3. Himachal_Pradesh (place)
'''


