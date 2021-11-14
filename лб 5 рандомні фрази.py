
import random
first_list = ['Word', 'Like', 'Great', 'Beatufle', 'Bad', 'Coll', 'Never', 'sow-sow']
second_list = ['Andriy', 'Vasya', 'Masha', 'Kolya', 'Albina', 'Katya', 'Zhenya']
third_list = ['first', 'second', 'third', 'fourth', 'fivfth', 'sixth', 'seventh' ]

list_of_strings_list = [first_list + second_list + third_list]

def random_phrase():
    result_string = ""
    for i in range(0,3):
        random_index = random.randrange(0,7)
        resulte_string = result_string + list_of_strings_list[i][random_index] + ""

        return result_string

print(random_phrase())

input()
