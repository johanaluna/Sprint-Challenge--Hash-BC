#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # insert key,value pair
    for i in tickets:
        #hash_table_insert(hash_table, key, value)
         hash_table_insert(hashtable,i.source, i.destination)
    
    #The first item has a None value
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    for i in range(1, length):
        #the next destination uses the previous key
        # as the value in the destination
        # hash_table_retrieve(hash_table, key) 
        route[i] = hash_table_retrieve(hashtable, route[i-1])
    
    # lenght-1 because we dont want to show the none value
    return route[0:length-1]


