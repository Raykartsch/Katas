# from collections import Counter
# def anagrams(word, words):
#     param = Counter(word)
#     anagrams = []
#     for i in range(len(words)):
#         a = Counter(words[i])
#         for key in param:
#             if key in a:
#                 keeping = True if param.get(key) == a.get(key) and param.items() == a.items() else False
#                 if not keeping: break
#                 if words[i] not in anagrams: anagrams.append(words[i])
#     return anagrams
