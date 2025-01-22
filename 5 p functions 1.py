# bank account

def transaction(order):
    net = 0
    for ord in order:
        D_W, value = ord.split(' ')
        if D_W.upper() == 'D':
            net += int(value)
        if D_W.upper() == 'W':
            net -= int(value)
    print(net)


transaction_list = []

while True:
    input1 = input('enter (transaction type "D" or "W") (amount): \n')

    if input1.upper() == 'END':
        break
    D_w, value = input1.split(' ')

    try:
        value = int(value)
    except ValueError:
        print(f'invalid value input: {value}')
        continue
    if D_w.upper() not in ['D', 'W']:
        print(f'invalid transaction input: {D_w}')
        continue

    transaction_list.append(input1)

transaction(transaction_list)
