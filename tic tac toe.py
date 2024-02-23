from collections import Counter

EMPTY_BOARD = 0
HUMAN = 1
AI = -1


def player(BOX):
  counter = Counter(BOX)
  x_position = counter[1]
  o_position = counter[-1]

  if x_position + o_position == 9:
    return None
  elif x_position > o_position:
    return AI
  else:
    return HUMAN


def actions(BOX):
  play = player(BOX)
  actions_list = [(play, i) for i in range(len(BOX)) if BOX[i] == EMPTY_BOARD]
  return actions_list


def result(BOX, a):
  (play, index) = a
  BOX_copy = BOX.copy()
  BOX_copy[index] = play
  return BOX_copy


def terminal(BOX):
  for i in range(3):
    if BOX[3 * i] == BOX[3 * i + 1] == BOX[3 * i + 2] != EMPTY_BOARD:
      return BOX[3 * i]
    if BOX[i] == BOX[i + 3] == BOX[i + 6] != EMPTY_BOARD:
      return BOX[i]

  if BOX[0] == BOX[4] == BOX[8] != EMPTY_BOARD:
    return BOX[0]
  if BOX[2] == BOX[4] == BOX[6] != EMPTY_BOARD:
    return BOX[2]

  if player(BOX) is None:
    return 0

  return None


def utility(BOX, cost):
  term = terminal(BOX)
  if term is not None:
    return (term, cost)

  action_list = actions(BOX)
  utils = []
  for action in action_list:
    new_s = result(BOX, action)
    utils.append(utility(new_s, cost + 1))

  score = utils[0][0]
  idx_cost = utils[0][1]
  play = player(BOX)
  if play == HUMAN:
    for i in range(len(utils)):
      if utils[i][0] > score:
        score = utils[i][0]
        idx_cost = utils[i][1]
  else:
    for i in range(len(utils)):
      if utils[i][0] < score:
        score = utils[i][0]
        idx_cost = utils[i][1]
  return (score, idx_cost)


def minimax(BOX):
  action_list = actions(BOX)
  utils = []
  for action in action_list:
    new_s = result(BOX, action)
    utils.append((action, utility(new_s, 1)))

  if len(utils) == 0:
    return ((0, 0), (0, 0))

  sorted_list = sorted(utils, key=lambda l: l[0][1])
  action = min(sorted_list, key=lambda l: l[1])
  return action


def print_board(BOX):

  def convert(num):
    if num == HUMAN:
      return 'X'
    if num == AI:
      return 'O'
    return '_'

  i = 0
  for _ in range(3):
    for _ in range(3):
      print(convert(BOX[i]), end=' ')
      i += 1
    print()


if __name__ == '__main__':
  BOX = [EMPTY_BOARD for _ in range(9)]
  print(" --------------------------------------------------")
  print('|   Welcome to the Tic Tac Toe game with the AI!   |')
  print(" -------------------------------------------------- ")
  print("\n Hi i am Tacky your competitor AI ")
  print("\n\nFor Your reference you are 'x' and i am 'O'")
  print("/n/nGet ready to Lose")

  while terminal(BOX) is None:
    play = player(BOX)
    if play == HUMAN:
      print('\n\nIt is Your turn Human !', end='\n\n')
      x = int(input('Enter the Row  [0-1st row,1-2nd row,2-3rd row ]:'))
      y = int(
          input('Enter the Column [0-1st column,1-2nd column,2-3rd column ]:'))
      index_position = 3 * x + y
      if BOX[index_position] != EMPTY_BOARD:
        print('Open your eyes , Its already been filled choose other position')
        continue

      BOX = result(BOX, (1, index_position))
      print_board(BOX)
    else:
      print('\n\nIt is my turn , let me think !!!')
      action = minimax(BOX)
      BOX = result(BOX, action[0])
      print_board(BOX)

  winner = utility(BOX, 1)[0]
  if winner == HUMAN:
    print("You have won!")
  elif winner == AI:
    print("You have lost!")
  else:
    print("It's a tie.")
