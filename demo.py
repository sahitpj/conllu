'''
The following file is about basic conllu manipulation. The necessary functionalities will be written here
'''

from conllu import parse_single #for parsing a conllu which has a single sentence

data_file = open("sample.conll", "r", encoding="utf-8")
tokenlist = parse_single(data_file) #tokenlist gives the parsed conllu file
print(tokenlist[0].to_tree())


# the tree will have the root, and then the children. Should be easy to access.