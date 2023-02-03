import random
import sys

sys.setrecursionlimit(10000)


def store_matrix():
    list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    return list


the_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
               24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
counting_main = []
limit_for_decrease = [0, 10, 20, 30]
limit_for_add = [9, 19, 29]


def the_counting_list(number):
    if the_numbers:
        the_choice = the_numbers[random.randrange(number)]
        the_numbers.remove(the_choice)
        return the_choice
    else:
        print("I ran out of numbers")
        exit()


def main_lab(inc_matrix, chosen_number):
    inc_matrix[chosen_number] = 0
    counting_main.append(1)
    check_for_route(inc_matrix)


def check_for_route(new_matrix):
    if new_matrix[39] == 1 or new_matrix[0] == 1:
        # print(new_matrix)
        main_lab(new_matrix, the_counting_list(len(the_numbers)))

    elif new_matrix[39] == 0 and new_matrix[0] == 0:
        # print(new_matrix)
        base_check(new_matrix)

    else:
        print('i am out')
        print(len(counting_main))
        print(the_numbers)
        print(new_matrix)


def base_check(matrix):
    print('Base check initiated')
    n = [0]
    print(f'The Matrix\n'
          f'\n {matrix[0]} {matrix[1]} {matrix[2]} {matrix[3]} {matrix[4]} {matrix[5]} {matrix[6]} {matrix[7]} {matrix[8]} {matrix[9]}'
          f'\n {matrix[10]} {matrix[11]} {matrix[12]} {matrix[13]} {matrix[14]} {matrix[15]} {matrix[16]} {matrix[17]} {matrix[18]} {matrix[19]}'
          f'\n {matrix[20]} {matrix[21]} {matrix[22]} {matrix[23]} {matrix[24]} {matrix[25]} {matrix[26]} {matrix[27]} {matrix[28]} {matrix[29]}'
          f'\n {matrix[30]} {matrix[31]} {matrix[32]} {matrix[33]} {matrix[34]} {matrix[35]} {matrix[36]} {matrix[37]} {matrix[38]} {matrix[39]} '
          f'\n')

    def find_exit_1(the_list):
        print(f'Step: {the_list[-1]}')
        # print(f'Visit log: {n}')
        if the_list[-1] == 29 or the_list[-1] == 38 or the_list[-1] == 39:
            print('')
            print('Path Found!\n')
            print(f'Matrix modified: {len(counting_main)} times')
            print(f'Distance to exit: {len(n)}')
            print(f'The path to exit: {n}')
            exit()
        if matrix[(the_list[-1] + 1)] == 0 and 0 <= the_list[-1] + 1 < 40 and the_list[-1] + 1 not in n \
                and the_list[-1] not in limit_for_add:
            # print(f'What came in INDEX: {the_list[-1]}')
            print('->')
            n.append((the_list[-1] + 1))
            find_exit_1(n)
        elif the_list[-1] < 30 and the_list[-1] + 10 not in n and matrix[(the_list[-1] + 10)] == 0:
            # print(f'What came in INDEX: {the_list[-1]}')
            print('↓')
            n.append((the_list[-1] + 10))
            find_exit_1(n)
        elif the_list[-1] - 10 > 0 and matrix[(the_list[-1] - 10)] == 0 and the_list[-1] - 10 not in n:
            # print(f'What came in INDEX: {the_list[-1]}')
            print('↑')
            n.append((the_list[-1] - 10))
            find_exit_1(n)
        elif the_list[-1] - 1 > 0 and matrix[(the_list[-1] - 1)] == 0 and the_list[-1] - 1 not in n and \
                the_list[-1] not in limit_for_decrease:
            print('<-')
            n.append((the_list[-1] - 1))
            find_exit_1(n)
        else:
            n.clear()
            n.append(0)
            print("")
            print('I hit a dead end, recalculating route')
            find_exit_2(n)

    def find_exit_2(the_list_2):
        print(f'Step: {the_list_2[-1]}')
        if the_list_2[-1] == 29 or the_list_2[-1] == 38 or the_list_2[-1] == 39:
            print('')
            print('Path Found!\n')
            print(f'Matrix modified: {len(counting_main)} times')
            print(f'Distance to exit: {len(n)}')
            print(f'The path to exit: {n}')
            exit()
        elif the_list_2[-1] < 30 and the_list_2[-1] + 10 not in n and matrix[(the_list_2[-1] + 10)] == 0:
            print('↓')
            n.append((the_list_2[-1] + 10))
            find_exit_2(n)
        elif the_list_2[-1] - 10 > 0 and matrix[(the_list_2[-1] - 10)] == 0 and the_list_2[-1] - 10 not in n:
            print('↑')
            n.append((the_list_2[-1] - 10))
            find_exit_2(n)
        elif matrix[(the_list_2[-1] + 1)] == 0 and 0 <= the_list_2[-1] + 1 < 40 and the_list_2[-1] + 1 not in n \
                and the_list_2[-1] not in limit_for_add:
            print('->')
            n.append((the_list_2[-1] + 1))
            find_exit_2(n)
        elif the_list_2[-1] - 1 > 0 and matrix[(the_list_2[-1] - 1)] == 0 and the_list_2[-1] - 1 not in n and \
                the_list_2[-1] not in limit_for_decrease:
            # print(f'What came in INDEX: {the_list_2[-1]}')
            print('<-')
            n.append((the_list_2[-1] - 1))
            find_exit_2(n)
        else:
            n.clear()
            n.append(0)
            print("")
            print('I hit a dead end, recalculating route')
            find_exit_3(n)

    def find_exit_3(the_list_3):
        print(f'Step: {the_list_3[-1]}')
        if the_list_3[-1] == 29 or the_list_3[-1] == 38 or the_list_3[-1] == 39:
            print('')
            print('Path Found!\n')
            print(f'Matrix modified: {len(counting_main)} times')
            print(f'Distance to exit: {len(n)}')
            print(f'The path to exit: {n}')
            exit()
        elif the_list_3[-1] - 10 > 0 and matrix[(the_list_3[-1] - 10)] == 0 and the_list_3[-1] - 10 not in n:
            print('↑')
            n.append((the_list_3[-1] - 10))
            find_exit_3(n)
        elif matrix[(the_list_3[-1] + 1)] == 0 and 0 <= the_list_3[-1] + 1 < 40 and the_list_3[-1] + 1 not in n \
                and the_list_3[-1] not in limit_for_add:
            print('->')
            n.append((the_list_3[-1] + 1))
            find_exit_3(n)
        elif the_list_3[-1] < 30 and the_list_3[-1] + 10 not in n and matrix[(the_list_3[-1] + 10)] == 0:
            print('↓')
            n.append((the_list_3[-1] + 10))
            find_exit_3(n)
        elif the_list_3[-1] - 1 > 0 and matrix[(the_list_3[-1] - 1)] == 0 and the_list_3[-1] - 1 not in n and \
                the_list_3[-1] not in limit_for_decrease:
            # print(f'What came in INDEX: {the_list_2[-1]}')
            print('<-')
            n.append((the_list_3[-1] - 1))
            find_exit_3(n)
        else:
            n.clear()
            n.append(0)
            print("")
            print('I hit a dead end, recalculating route')
            find_exit_4(n)

    def find_exit_4(the_list_4):
        print(f'Step: {the_list_4[-1]}')
        if the_list_4[-1] == 29 or the_list_4[-1] == 38 or the_list_4[-1] == 39:
            print('')
            print('Path Found!\n')
            print(f'Matrix modified: {len(counting_main)} times')
            print(f'Distance to exit: {len(n)}')
            print(f'The path to exit: {n}')
            exit()
        elif the_list_4[-1] < 30 and the_list_4[-1] + 10 not in n and matrix[(the_list_4[-1] + 10)] == 0:
            print('↓')
            n.append((the_list_4[-1] + 10))
            find_exit_4(n)
        elif matrix[(the_list_4[-1] + 1)] == 0 and 0 <= the_list_4[-1] + 1 < 40 and the_list_4[-1] + 1 not in n \
                and the_list_4[-1] not in limit_for_add:
            print('->')
            n.append((the_list_4[-1] + 1))
            find_exit_4(n)
        elif the_list_4[-1] - 10 > 0 and matrix[(the_list_4[-1] - 10)] == 0 and the_list_4[-1] - 10 not in n:
            print('↑')
            n.append((the_list_4[-1] - 10))
            find_exit_4(n)
        elif the_list_4[-1] - 1 > 0 and matrix[(the_list_4[-1] - 1)] == 0 and the_list_4[-1] - 1 not in n and \
                the_list_4[-1] not in limit_for_decrease:
            print('<-')
            n.append((the_list_4[-1] - 1))
            find_exit_4(n)
        else:
            n.clear()
            n.append(0)
            print("")
            print('I hit a dead end, recalculating route')
            find_exit_5(n)

    def find_exit_5(the_list_5):
        print(f'Step: {the_list_5[-1]}')
        if the_list_5[-1] == 29 or the_list_5[-1] == 38 or the_list_5[-1] == 39:
            print('')
            print('Path Found!\n')
            print(f'Matrix modified: {len(counting_main)} times')
            print(f'Distance to exit: {len(n)}')
            print(f'The path to exit: {n}')
            exit()
        elif the_list_5[-1] - 10 > 0 and matrix[(the_list_5[-1] - 10)] == 0 and the_list_5[-1] - 10 not in n:
            print('↑')
            n.append((the_list_5[-1] - 10))
            find_exit_5(n)
        elif matrix[(the_list_5[-1] + 1)] == 0 and 0 <= the_list_5[-1] + 1 < 40 and the_list_5[-1] + 1 not in n \
                and the_list_5[-1] not in limit_for_add:
            print('->')
            n.append((the_list_5[-1] + 1))
            find_exit_5(n)
        elif the_list_5[-1] < 30 and the_list_5[-1] + 10 not in n and matrix[(the_list_5[-1] + 10)] == 0:
            print('↓')
            n.append((the_list_5[-1] + 10))
            find_exit_5(n)
        elif the_list_5[-1] - 1 > 0 and matrix[(the_list_5[-1] - 1)] == 0 and the_list_5[-1] - 1 not in n and \
                the_list_5[-1] not in limit_for_decrease:
            # print(f'What came in INDEX: {the_list_2[-1]}')
            print('<-')
            n.append((the_list_5[-1] - 1))
            find_exit_5(n)
        else:
            n.clear()
            n.append(0)
            print("")
            print('I hit a dead end, recalculating route')
            find_exit_6(n)

    def find_exit_6(the_list_6):
        print(f'Step: {the_list_6[-1]}')
        if the_list_6[-1] == 29 or the_list_6[-1] == 38 or the_list_6[-1] == 39:
            print('')
            print('Path Found!\n')
            print(f'Matrix modified: {len(counting_main)} times')
            print(f'Distance to exit: {len(n)}')
            print(f'The path to exit: {n}')
            exit()
        elif matrix[(the_list_6[-1] + 1)] == 0 and 0 <= the_list_6[-1] + 1 < 40 and the_list_6[-1] + 1 not in n \
                and the_list_6[-1] not in limit_for_add:
            print('->')
            n.append((the_list_6[-1] + 1))
            find_exit_6(n)
        elif the_list_6[-1] - 10 > 0 and matrix[(the_list_6[-1] - 10)] == 0 and the_list_6[-1] - 10 not in n:
            print('↑')
            n.append((the_list_6[-1] - 10))
            find_exit_6(n)
        elif the_list_6[-1] < 30 and the_list_6[-1] + 10 not in n and matrix[(the_list_6[-1] + 10)] == 0:
            print('↓')
            n.append((the_list_6[-1] + 10))
            find_exit_6(n)
        elif the_list_6[-1] - 1 > 0 and matrix[(the_list_6[-1] - 1)] == 0 and the_list_6[-1] - 1 not in n and \
                the_list_6[-1] not in limit_for_decrease:
            # print(f'What came in INDEX: {the_list_2[-1]}')
            print('<-')
            n.append((the_list_6[-1] - 1))
            find_exit_6(n)
        else:
            print('No solution found, we need to change the Matrix')
            print('____' * 20)
            a = len(the_numbers)
            b = the_counting_list(a)
            main_lab(matrix, b)

    find_exit_1(n)


def main():
    matrix = store_matrix()
    the_number = the_counting_list(40)
    main_lab(matrix, the_number)


if __name__ == "__main__":
    main()
