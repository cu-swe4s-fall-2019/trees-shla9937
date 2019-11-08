import argparse
import time
import matplotlib
import matplotlib.pyplot as plt
import binary_tree
from binary_tree import Tree
from binary_tree import Node
from avl_tree import avl
from avl_tree.avl import AVL
from avl_tree.avl import AVLNode
from hash_tables_shla9937.hash_table import LPHashTable
from hash_tables_shla9937.hash_table import h_rolling


parser = argparse.ArgumentParser(
           description='Parsing operator.')

parser.add_argument('--structure',
                    type=str,
                    help='binary, AVL, hash',
                    required=True)

parser.add_argument('--input_file',
                    type=str,
                    help='Input file name',
                    required=True)

parser.add_argument('--num_keys',
                    type=int,
                    help='Number of key/value pairs to use',
                    required=True)

args = parser.parse_args()

structure = args.structure
file_name = args.input_file
num_keys = args.num_keys


def parse_file_into_list(file_name):
    key_value_pairs = []
    for line in open(file_name):
        key_value_pairs.append(line.rstrip().split())
    return key_value_pairs


def build_database(structure, num_keys, key_value_pairs):
    if structure == 'binary':
        database = Tree()
        for i in key_value_pairs:
            database.insert(i)
        return database
    elif structure == 'AVL':
        database = AVL()
        for i in key_value_pairs:
            database.insert(i)
        return database
    elif structure == 'hash':
        database = LPHashTable(num_keys, h_rolling)
        for i in key_value_pairs:
            database.insert(i[0], i[1])
        return database


def insert_test(database, key):
    if structure == 'binary':
        for i in key_value_pairs:
            database.insert(i)
        return True
    elif structure == 'AVL':
        for i in key_value_pairs:
            database.insert(i)
        return True
    elif structure == 'hash':
        for i in key_value_pairs:
            database.insert(i[0], i[1])
        return True


def search_database(structure, database, key):
    if structure == 'binary':
        result = database.search(key)
    elif structure == 'AVL':
        result = database.find(key)
    elif structure == 'hash':
        result = database.find(key)
    return result


if __name__ == '__main__':
    key_value_pairs = parse_file_into_list(file_name)
    database = build_database(structure, num_keys, key_value_pairs)
    insert_times = []
    time_num = []
    counter = 0
    test_numbers = []
    # time insertion rates
    # for num in range(1, 10000, 100):
    #     test_list = []
    #     test_list.append(num)
    #     test_list.append(3)
    #     test_numbers.append(test_list)
    # for test_number in test_numbers:
    #     time_0 = time.time()
    #     insert_test(database, test_number[0])
    #     time_1 = time.time()
    #     elapse_time = (time_1 - time_0)
    #     time_num.append(counter)
    #     counter += 1
    #     insert_times.append(elapse_time)
    # time search rates
    # search_list = []
    # counter_1 = 0
    # for i in key_value_pairs:
    #     if counter_1 % 100 == 0:
    #         search_list.append(i[0])
    #     counter_1 += 1
    # for item in search_list:
    #     print(item)
    #     time_0 = time.time()
    #     search_database(structure, database, item)
    #     time_1 = time.time()
    #     elapse_time = (time_1 - time_0)
    #     time_num.append(counter)
    #     counter += 1
    #     insert_times.append(elapse_time)
    # time failed search rates
    search_list = []
    fails = []
    for j in key_value_pairs:
        search_list.append(int(j[0]))
    counter_1 = 0
    for i in range(1, 2000):
        if counter_1 < 101 and i not in search_list:
            fails.append(i)
            counter_1 += 1
    for item in fails:
        print(item)
        time_0 = time.time()
        search_database(structure, database, str(item))
        time_1 = time.time()
        elapse_time = (time_1 - time_0)
        time_num.append(counter)
        counter += 1
        insert_times.append(elapse_time)
    plt.xlabel('Search number')
    plt.ylabel('Time(sec)')
    plt.title(structure+' th sorted assembled tree')
    plt.scatter(time_num, insert_times)
    out_file_0 = structure+'test_sorted_search.png'
    plt.savefig(out_file_0, bbox_inches='tight')
