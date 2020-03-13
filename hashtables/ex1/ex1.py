#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    O(n)
    """
    for i in range(len(weights)):
        weight = weights[i]
        #difference between the limit and the weight
        diff = limit - weight
        # validate if the result of diff is already in the hash
        # hash_table_retrieve(hash_table, key)
        validate = hash_table_retrieve(ht, diff)
        if validate is not None:
            return (i,validate)
        # insert the validate weight in the has table
        # hash_table_insert(hash_table, key, value)
        hash_table_insert(ht,weight,i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
