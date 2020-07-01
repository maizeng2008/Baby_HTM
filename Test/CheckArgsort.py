
def check():
    a_file = open("../overlap_ranked_table.txt", "r")
    list_of_lists = []
    for line in a_file:
        list_of_lists.append(line)
    a_file.close()
    a_file = open("../overlap_ranked_table_ordered.txt", "r")
    list_of_lists_ordered = []
    for line in a_file:
        list_of_lists_ordered.append(line)
    a_file.close()
    print(list_of_lists_ordered[1222])

if __name__ == "__main__":
    check()