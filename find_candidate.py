N = 3

def check_card(card):
    ''' card の数字が適切かどうかの判定 '''
    card = str(card).zfill(N)
    flg = True
    if not '0'.zfill(N) <= card <= str(10**N-1).zfill(N):
        flg = False
    for i in range(len(card)):
        if card.count(card[i]) > 1:
            flg = False
    return flg

def calc_eat_bite(num1, num2):
    num1 = str(num1).zfill(N)
    num2 = str(num2).zfill(N)
    eat, bite = 0, 0
    for i in range(len(num1)):
        if num1[i] == num2[i]:
            eat += 1
        elif num1[i] in num2:
            bite += 1
    return eat, bite

num_list = [str(n).zfill(N) for n in range(10**N-1) if check_card(n)]
removed_list = []

if __name__ == '__main__':
    correct_num = input('correct num: ')
    while True:
        call = input('\ncall: ')
        if call == 'back':
            num_list += removed_list
        else:
            removed_list = []
            for num in num_list[:]:
                num = str(num)
                if list(calc_eat_bite(num, call)) != list(calc_eat_bite(correct_num, call)):
                    num_list.remove(num)
                    removed_list.append(num)
        print(num_list)
        print(f'{len(num_list)} patterns are equally possible.')
