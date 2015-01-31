def common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between 
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.  


    For example:

        >>> sorted(common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    # ###attempt1
    # list1_dict = {}
    # list2_dict = {}

    # for item in list1:
    #     list1_dict[item] = list1_dict.get(item, 0) + 1
    # # print list1_dict
    # for item in list2:
    #     list2_dict[item] = list2_dict.get(item, 0) + 1
    # # print list2_dict

    # common_items_dict = {}

    # # print "processing list1_dict:"
    # for key in list1_dict:
    #     # print key
    #     common_items_dict[key] = common_items_dict.get(key, 0) + 1
    #     # print key
    #     # print common_items_dict.get(key, 0)
    # # print "processing list2_dict:"
    # for key in list2_dict:
    #     common_items_dict[key] = common_items_dict.get(key, 0) + 1
    #     # print key
    #     # print common_items_dict.get(key, 0)
    
    # # print "list1 and list2 dicts combined is:"
    # # print common_items_dict

    # common_items_list = []
    # for key in common_items_dict:
    #     if common_items_dict[key] > 1: 
    #         # print common_items_dict[key]
    #         common_items_list += [key] * common_items_dict.get(key)
    # # print common_items_list
    # return common_items_list


    ###attempt2

    # """
    # I think I can do this with sets -- but since the directions
    # indicate I should be able to do it with lists and dicts,
    # I want to understand how to make that work....
    # """

    # list1_dict = {}
    # list2_dict = {}

    # for item in list1:
    #     list1_dict[item] = list1_dict.get(item, 0) + 1
    # # print list1_dict
    # for item in list2:
    #     list2_dict[item] = list2_dict.get(item, 0) + 1
    # # print list2_dict

    # common_items_dict = {}

    # # print "processing list1_dict:"
    # for key in list1_dict:
    #     # print key
    #     common_items_dict[key] = common_items_dict.get(key, 0) + 1
    #     # print key
    #     # print common_items_dict.get(key, 0)
    # # print "processing list2_dict:"
    # for key in list2_dict:
    #     common_items_dict[key] = common_items_dict.get(key, 0) + 1
    #     # print key
    #     # print common_items_dict.get(key, 0)
    
    # # print "list1 and list2 dicts combined is:"
    # # print common_items_dict

    # common_items_list = []
    # for key in common_items_dict:
    #     if common_items_dict[key] > 1: 
    #         # print common_items_dict[key]
    #         common_items_list += [key] * common_items_dict.get(key)
    # # print common_items_list
    # return common_items_list

    ### attempt3

    common_items_dict = {}

    for item in list1:
        common_items_dict[item] = common_items_dict.get(item, -1) + 1
    # print "dict with list 1 items is: ", common_items_dict
    for item in list2:
        if common_items_dict.get(item, 0) <= 1:
            common_items_dict[item] = common_items_dict.get(item, -1) + 1
    # print "dict with list2 items is: ", common_items_dict

    common_items_list = []
    for key in common_items_dict:
        if common_items_dict[key] > 0: 
            # print common_items_dict[key]
            common_items_list += [key] * common_items_dict.get(key)
    # print common_items_list
    return common_items_list


a=[1, 2, 3, 4]
b=[1, 2]
c=[1, 1, 2, 2]


print "ex1: should return [1, 2]. returns: ", common_items(a, b)
print
print "ex2 should return [1, 1, 2, 2]. returns: ", common_items(a, c)
print
print "ex3 should return [1, 1, 2, 2]. returns: ", common_items(c, a)


# def unique_common_items(list1, list2):
#     """Produce the set of *unique* common items in two lists.

#     Given two lists, return a list of the *unique* common items shared between 
#     the lists.

#     IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


#     Just like `common_items`, this should find [1, 2]:

#         >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
#         [1, 2]

#     However, now we only want unique items, so for these lists, don't show 
#     more than 1 or 2 once:

#         >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
#         [1, 2]

#     """

#     #### attempt1

#     """
#     I think I can do this with sets -- but since the directions
#     indicate I should be able to do it with lists and dicts,
#     I want to understand how to make that work....
#     """

#     #### reuse code from common_items attempt 1 
#     #### then iterate thru list to weed out dupes?
#     #### this feels REALLY cumbersome
#     list1_dict = {}
#     list2_dict = {}

#     for item in list1:
#         list1_dict[item] = list1_dict.get(item, 0) + 1
#     # print list1_dict
#     for item in list2:
#         list2_dict[item] = list2_dict.get(item, 0) + 1
#     # print list2_dict

#     common_items_dict = {}

#     # print "processing list1_dict:"
#     for key in list1_dict:
#         # print key
#         common_items_dict[key] = common_items_dict.get(key, 0) + 1
#         # print key
#         # print common_items_dict.get(key, 0)
#     # print "processing list2_dict:"
#     for key in list2_dict:
#         common_items_dict[key] = common_items_dict.get(key, 0) + 1
#         # print key
#         # print common_items_dict.get(key, 0)
    
#     # print "list1 and list2 dicts combined is:"
#     # print common_items_dict

#     common_items_list = []
#     for key in common_items_dict:
#         if common_items_dict[key] > 1: 
#             # print common_items_dict[key]
#             common_items_list += [key] * common_items_dict.get(key)
#     # print "unfiltered common items list is ", common_items_list

#     for item1 in common_items_list:
#         for item2 in common_items_list:
#             if item1 == item2:
#                 common_items_list.pop(item2)
#     # print "final unique common items list is ",common_items_list

#     return common_items_list

# print "test1: ", unique_common_items([1, 2, 3, 4], [1, 2])
# print "test2: ", unique_common_items([1, 2, 3, 4], [1, 1, 2, 2])


# # # # def word_length(words):
# # # #     """Given list of words, return list of ascending [(len, [words])].

# # # #     Given a list of words, return a list of tuples, ordered by word-length.
# # # #     Each tuple should have two items--the length of the words for that 
# # # #     word-length, and the list of words of that word length.

# # # #     For example:

# # # #         >>> word_length(["ok", "an", "apple", "a", "day"])
# # # #         [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

# # # #     """
# # # #     # ascending_tpl_lst = []

# # # #     # for word in words:
# # # #     #     ## fixme: add condtional --
# # # #     #     ## currently this will make unique tuple per word 
# # # #     #     ascending_tpl_lst.append((len(word), [word])

# # # #     # ## fixme: invalid syntax on these lines?!
# # # #     # # print ascending_tpl_lst
# # # #     # return ascending_tpl_lst

# # # #     temp_word_len_dict = {}

# # # #     for word in words:
# # # #         temp_word_len_dict[len(word)] = temp_word_len_dict.get(len(word), []) + [word]
# # # #     print temp_word_len_dict
# # # #     print type(temp_word_len_dict)

# # # #     # ascending_tpl_lst = []

# # # #     # for k,v in temp_word_len_dict:
# # # #     #     ascending_tpl_lst.append((k,v))    

# # # #     ascending_tpl_lst = sorted(temp_word_len_dict.items())


# # # #     print ascending_tpl_lst
# # # #     return ascending_tpl_lst

# # # # wordlist = ["ok", "an", "apple", "a", "day"]
# # # # word_length(wordlist)


# # # def adv_word_length_sorted_words(words):
# # #     """Given list of words, return list of ascending [(len, [sorted-words])].

# # #     Given a list of words, return a list of tuples, ordered by word-length.
# # #     Each tuple should have two items--the length of the words for that 
# # #     word-length, and the list of words of that word length. The list of words
# # #     for that length should be sorted alphabetically.

# # #     For example:

# # #         >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
# # #         [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

# # #     """

# # #     temp_word_len_dict = {}

# # #     for word in words:
# # #         temp_word_len_dict[len(word)] = sorted(temp_word_len_dict.get(len(word), []) + [word])
# # #     # print temp_word_len_dict
# # #     # print type(temp_word_len_dict)


# # #     ascending_tpl_word_sorted_lst = sorted(temp_word_len_dict.items())

# # #     print ascending_tpl_word_sorted_lst
# # #     return ascending_tpl_word_sorted_lst

# # # wordlist = ["ok", "an", "apple", "a", "day"]
# # # adv_word_length_sorted_words(wordlist)



# # def pirate_talk(phrase):
# #     """Translate phrase to pirate talk.

# #     Given a phrase, translate each word to the Pirate-speak equivalent.
# #     Words that cannot be translated into Pirate-speak should pass through
# #     unchanged. Return the resulting sentence.
   
# #     Here's a table of English to Pirate translations:

# #     English     Pirate
# #     ----------  ----------------
# #     sir         matey
# #     hotel       fleabag inn
# #     student     swabbie
# #     boy         matey
# #     madam       proud beauty
# #     professor   foul blaggart
# #     restaurant  galley
# #     your        yer
# #     excuse      arr
# #     students    swabbies
# #     are         be
# #     lawyer      foul blaggart
# #     the         th'
# #     restroom    head
# #     my          me
# #     hello       avast
# #     is          be
# #     man         matey

# #     For example:

# #         >>> pirate_talk("my student is not a man")
# #         'me swabbie be not a matey'

# #     You should treat words with punctuation as if they were different
# #     words:

# #         >>> pirate_talk("my student is not a man!")
# #         'me swabbie be not a man!'

# #     """

# #     eng_to_pirate_dict = {"sir": "matey", "hotel" : "fleagba inn",
# #                         "student": "swabbie", "boy": "matey",
# #                         "madam": "proud beauty", "professor": "foul blaggart",
# #                         "restaurant": "galley", "your": "yer", 
# #                         "excuse": "arr", "students": "swabbies",
# #                         "are": "be", "lawyer": "foul blaggart",
# #                         "the": "th'", "restroom": "head",
# #                         "my": "me", "hello": "avast", 
# #                         "is":"be", "man": "matey"}
    
# #     # print eng_to_pirate_dict

# #     phrase_list = phrase.split()
# #     # print phrase_list

# #     # translated_phrase_list = []
# #     # for word in phrase_list:
# #     #     translated_phrase_list.append(eng_to_pirate_dict.get(word, word))

# #     # try with list comprehension:
# #     translated_phrase_list = [eng_to_pirate_dict.get(word, word) for word in phrase_list]
# #     # print translated_phrase_list

# #     phase_made_arrrrglike = (" ").join(translated_phrase_list)

# #     # print phase_made_arrrrglike
# #     return phase_made_arrrrglike

# # print pirate_talk("my student is not a man")
# # print "\n" * 3
# # print pirate_talk("my student is not a man!")


# def sum_zero(list1):
#     """Return list of x,y number pair lists from a list where x+y==0

#     Given a list of numbers, add up each individual pair of numbers.
#     Return a list of each pair of numbers that adds up to 0.

        
#     For example:

#         >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
#         [[-2, 2], [-1, 1]]

#     This should always be a unique list, even if there are
#     duplicates in the input list:

#         >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
#         [[-2, 2], [-1, 1]]

#     Of course, if there are one or more zeros to pair together, 
#     that's fine, too:

#         >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
#         [[-2, 2], [-1, 1], [0, 0]]

#     """

#     ### attemp1 
#     dict_of_zero_pairs = {}

#     for item1 in list1:
#         for item2 in list1:
#             if item1 + item2 == 0:
#                 dict_of_zero_pairs[item1] = dict_of_zero_pairs.get(item1, item2)
#     # print dict_of_zero_pairs

#     # list_of_zero_pairs = dict_of_zero_pairs.items()
#     # print list_of_zero_pairs
#     # ## ends up with list of tuples instead of list of lists
#     # ## AND doesn't weed out inverted dupes

#     # ## attempt2
#     # raw_set_of_zero_pairs = set()

#     # for item1 in list1:
#     #     for item2 in list1:
#     #         if item1 + item2 == 0:
#     #             raw_set_of_zero_pairs.add((item1, item2))
#     # print raw_set_of_zero_pairs
#     # ## ends up with list of tuples instead of list of lists
#     # ## AND doesn't weed out inverted dupes
#     # ## AND prints literally as a set: "set([list of tuples])"

#     # for (num1, num2) in raw_set_of_zero_pairs:
#     #     set.remove((num2, num1))
#     # ## TypeError: descriptor 'remove' requires a 'set' object but received a 'tuple'

#     # ##attempt3
#     # raw_list_of_zero_pairs = []

#     # for item1 in list1:
#     #     for item2 in list1:
#     #         if item1 + item2 == 0:
#     #             raw_list_of_zero_pairs.append([item1, item2])

#     # print raw_list_of_zero_pairs
#     # raw_list_of_zero_pairs.sort()
#     # print "list sorted:"
#     # print raw_list_of_zero_pairs
#     # ## generates lots of duplicates

#     """
#     stuck.
#     try...? make set of tuples, convert to list of lists, sort sublists, convert back
#     to set to weeds out dupes, convert back to list of lists.... ?????  
#     there must be a better way.
#     """

#     # ###attempt4
#     # raw_list_of_zero_pairs = []
#     # for k, v in dict_of_zero_pairs.iteritems():
#     #     raw_list_of_zero_pairs.append([k,v])
#     # ### this is redundant.. I think
#     # print raw_list_of_zero_pairs

#     # ###attempt5
#     # raw_list_of_zero_pairs = dict_of_zero_pairs.items()
#     # print raw_list_of_zero_pairs
#     # ### no. was not redundant, bc iteritems returns iterable,
#     # ### and items returns list of tuples not lists

#     ###attempt6
#     raw_list_of_zero_pairs = []
#     for k, v in dict_of_zero_pairs.iteritems():
#         raw_list_of_zero_pairs.append([k,v])
#     # print raw_list_of_zero_pairs

#     clean_list_of_zero_pairs = []
#     for pairA, pairB in raw_list_of_zero_pairs:
#         if [pairB, pairA] not in clean_list_of_zero_pairs:
#             clean_list_of_zero_pairs.append([pairA, pairB])
#     # print clean_list_of_zero_pairs
#     ### I really can not figure out how to do this without some form of "if __ in __"

#     return clean_list_of_zero_pairs

# print sum_zero([1, 2, 3, -2, -1])
# print "\n" * 3
# print sum_zero([1, 2, 3, -2, -1, 1, 1])
# print "\n" * 3
# print sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0])

