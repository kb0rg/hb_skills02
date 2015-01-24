def count_unique(string1):
    word_count_dict= {}
    words_list = string1.split()
    print words_list
    for word in words_list:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1
        # if word not in word_count_dict.keys():
        #     word_count_dict[word] = 1
        # else:
        #     word_count_dict[word] = word_count_dict[word] + 1

    print word_count_dict

count_unique("I am tired. It is Friday. I am happy tomorrow is the weekend.")