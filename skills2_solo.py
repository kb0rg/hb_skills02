#!/usr/bin/env python


"""Hackbright Skills 2: Python Data Structures.

There are a bunch of functions in this file that are not written, but
have documentation strings that explain how they should work. Your job
is to edit this file to write the bodies of these functions.

We expect that you will solve these problems using Python lists
and dictionaries. Some of these problems could be solved with Python
sets (a more advanced data type); if you've learned about sets, you
may use these here.

This file uses "doctests"; the explanation of how the functions should
work contains examples just like you'd see in the Python interpreter.
The examples are actually run and tested when this file is ran.

When you first run this test, it will show test failures for every
function--since the real functions haven't been written yet. As you
write the real functions, your test failure count will go down.

At the point where you've completed this skills assessment, the
only output from this program would be:

   ** ALL TESTS PASSED. GOOD WORK!

Good luck!

"""

def count_unique(string1):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}
  
    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    word_count_dict= {}
    words_list = string1.split()
    for word in words_list:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1
        # if word not in word_count_dict.keys():
        #     word_count_dict[word] = 1
        # else:
        #     word_count_dict[word] = word_count_dict[word] + 1

    return word_count_dict

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
    list1_dict = {}
    list2_dict = {}

    for item in list1:
        list1_dict[item] = list1_dict.get(item, 0) + 1
    # print list1_dict
    for item in list2:
        list2_dict[item] = list2_dict.get(item, 0) + 1
    # print list2_dict

    common_items_dict = {}

    # print "processing list1_dict:"
    for key in list1_dict:
        # print key
        common_items_dict[key] = common_items_dict.get(key, 0) + 1
        # print key
        # print common_items_dict.get(key, 0)
    # print "processing list2_dict:"
    for key in list2_dict:
        common_items_dict[key] = common_items_dict.get(key, 0) + 1
        # print key
        # print common_items_dict.get(key, 0)
    
    # print "list1 and list2 dicts combined is:"
    # print common_items_dict

    common_items_list = []
    for key in common_items_dict:
        if common_items_dict[key] > 1: 
            # print common_items_dict[key]
            # common_items_list += [key] * (common_items_dict.get(key) - 1) # works for 1 of 3 tests
            common_items_list += [key] * common_items_dict.get(key) # works for 2 of 3 tests
    # print common_items_list
    return common_items_list

    # fails 1 of 3


def unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between 
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `common_items`, this should find [1, 2]:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show 
    more than 1 or 2 once:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    list1_dict = {}
    list2_dict = {}

    for item in list1:
        list1_dict[item] = list1_dict.get(item, 0) + 1
    # print list1_dict
    for item in list2:
        list2_dict[item] = list2_dict.get(item, 0) + 1
    # print list2_dict

    common_items_dict = {}

    # print "processing list1_dict:"
    for key in list1_dict:
        # print key
        common_items_dict[key] = common_items_dict.get(key, 0) + 1
        # print key
        # print common_items_dict.get(key, 0)
    # print "processing list2_dict:"
    for key in list2_dict:
        common_items_dict[key] = common_items_dict.get(key, 0) + 1
        # print key
        # print common_items_dict.get(key, 0)
    
    # print "list1 and list2 dicts combined is:"
    # print common_items_dict

    common_items_list = []
    for key in common_items_dict:
        if common_items_dict[key] > 1: 
            # print common_items_dict[key]
            common_items_list += [key] * common_items_dict.get(key)
    # print common_items_list
    return common_items_list

    # fails 2 of 2


def sum_zero(list1):
    """Return list of x,y number pair lists from a list where x+y==0

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

        
    For example:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together, 
    that's fine, too:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    #### attemp1 
    # dict_of_zero_pairs = {}

    # for item1 in list1:
    #     for item2 in list1:
    #         if item1 + item2 == 0:
    #             dict_of_zero_pairs[item1] = dict_of_zero_pairs.get(item1, item2)

    # list_of_zero_pairs = dict_of_zero_pairs.items()
    # print list_of_zero_pairs
    ### ends up with list of tuples instead of list of lists
    ### AND doesn't weed out inverted dupes

    ### attempt2
    # raw_set_of_zero_pairs = set()

    # for item1 in list1:
    #     for item2 in list1:
    #         if item1 + item2 == 0:
    #             raw_set_of_zero_pairs.add((item1, item2))
    # print raw_set_of_zero_pairs
    ### ends up with list of tuples instead of list of lists
    ### AND doesn't weed out inverted dupes
    ### AND prints literally as a set: "set([list of tuples])"

    # for (num1, num2) in raw_set_of_zero_pairs:
    #     set.remove((num2, num1))
    # ## TypeError: descriptor 'remove' requires a 'set' object but received a 'tuple'

    ###attempt3
    # raw_list_of_zero_pairs = []

    # for item1 in list1:
    #     for item2 in list1:
    #         if item1 + item2 == 0:
    #             raw_list_of_zero_pairs.append([item1, item2])

    # print raw_list_of_zero_pairs
    # raw_list_of_zero_pairs.sort()
    # print "list sorted:"
    # print raw_list_of_zero_pairs
    # ## generates lots of duplicates

    """
    stuck.
    try...? make set of tuples, convert to list of lists, sort sublists, convert back
    to set to weeds out dupes, convert back to list of lists.... ?????  
    there must be a better way.
    """


def find_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(find_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(find_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """
    no_dupes_list = []

    no_dupes_set = set(words)
    # print no_dupes_set

    for item in no_dupes_set:
        no_dupes_list.append(item)

    return no_dupes_list
    # passes!


def word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that 
    word-length, and the list of words of that word length.

    For example:

        >>> word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    # ascending_tpl_lst = []

    # for word in words:
    #     ## fixme: add condtional --
    #     ## currently this will make unique tuple per word 
    #     ascending_tpl_lst.append((len(word), [word])

    # ## fixme: invalid syntax on these lines?!
    # # print ascending_tpl_lst
    # return ascending_tpl_lst

    temp_word_len_dict = {}

    for word in words:
        temp_word_len_dict[len(word)] = temp_word_len_dict.get(len(word), []) + [word]
    # print temp_word_len_dict
    # print type(temp_word_len_dict)

    # ascending_tpl_lst = []

    # for k,v in temp_word_len_dict:
    #     ascending_tpl_lst.append((k,v))
    ## can not iterate over ....  

    ascending_tpl_lst = sorted(temp_word_len_dict.items())

    # print ascending_tpl_lst
    return ascending_tpl_lst

    ##passes!


def adv_word_length_sorted_words(words):
    """Given list of words, return list of ascending [(len, [sorted-words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that 
    word-length, and the list of words of that word length. The list of words
    for that length should be sorted alphabetically.

    For example:

        >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    temp_word_len_dict = {}

    for word in words:
        temp_word_len_dict[len(word)] = sorted(temp_word_len_dict.get(len(word), []) + [word])
    # print temp_word_len_dict
    # print type(temp_word_len_dict)


    ascending_tpl_word_sorted_lst = sorted(temp_word_len_dict.items())

    # print ascending_tpl_word_sorted_lst
    return ascending_tpl_word_sorted_lst

    ##passes!

def pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.
   
    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    eng_to_pirate_dict = {"sir": "matey", "hotel" : "fleagba inn",
                        "student": "swabbie", "boy": "matey",
                        "madam": "proud beauty", "professor": "foul blaggart",
                        "restaurant": "galley", "your": "yer", 
                        "excuse": "arr", "students": "swabbies",
                        "are": "be", "lawyer": "foul blaggart",
                        "the": "th'", "restroom": "head",
                        "my": "me", "hello": "avast", 
                        "is":"be", "man": "matey"}
    
    # print eng_to_pirate_dict

    phrase_list = phrase.split()
    # print phrase_list

    # translated_phrase_list = []
    # for word in phrase_list:
    #     translated_phrase_list.append(eng_to_pirate_dict.get(word, word))

    # try with list comprehension:
    translated_phrase_list = [eng_to_pirate_dict.get(word, word) for word in phrase_list]
    # print translated_phrase_list

    phase_made_arrrrglike = (" ").join(translated_phrase_list)

    # print phase_made_arrrrglike
    return phase_made_arrrrglike

    ##passes!

##############################################################################
# END OF SKILLS TEST; YOU CAN STOP HERE.


def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d

def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documenttion tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)
 

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "** ALL TESTS PASSED. GOOD WORK!" 
    print
