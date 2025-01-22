# find distance from (0,0):

def robot_moves(moves):
    x, y = 0, 0
    for move in moves:
        direction, value = move.split(' ')
        if direction == 'up':
            y += int(value)
        elif direction == 'down':
            y -= int(value)
        elif direction == 'left':
            x -= int(value)
        elif direction == 'right':
            x += int(value)
    distance = ((x**2) + (y**2))**0.5
    print(distance)


moves = []

while True:
    input_move = input('enter (move) (step):\n').lower()
    if input_move.lower() == 'end':
        break

    direction, value = input_move.split(' ')

    if direction not in ['right', 'left', 'up', 'down']:
        print(f'invalid direction: {direction}')
        continue

    try:
        value = int(value)
    except ValueError:
        print(f'{value} is not an int')
        continue

    moves.append(input_move)

robot_moves(moves)



# try:
#    yechizo faght try mikone
# except:
#    agar try krdio error dad in karo kn
# else:
#    agar error nadad in karo kn
# finally:
#    che error bede che nade in karo kn