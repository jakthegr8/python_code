# TIC TAC TOA GAME
def print_game_ui(p_inp):
  for row in p_inp:
    print(f'| {row[0]} | {row[1]} | {row[2]} |')
    print('---  ---  ---')
  return

def play_tic_toc_toa():
  # You can use simple list also instead of matrix list
  output  = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
  player1 = input('Play the game with X or O ? ')
  print(f'You have selected "{player1}"')
  print_game_ui(output)
  if player1 == 'X': player2 = 'O'
  marker = player1
  player = '[Player 1]:'

  while True:
    not_empty = True
    while not_empty:
      input_loc = int(input(f'{player} Enter the location number: '))
      output, not_empty = update_loc(input_loc, output, marker)
      if not_empty: print('The location is not empty!')

    print_game_ui(output)
    if winner(output):
      print(f'{player} is the WINNER!')
      return True

    if marker == 'X': 
      marker = 'O'
      player = '[Player 2]:'
    else:
      marker = 'X'
      player = '[Player 1]:'


def winner(p_inp):
  if p_inp[0][0] == p_inp[0][1] == p_inp[0][2] != ' ':
    return True
  elif p_inp[1][0] == p_inp[1][1] == p_inp[1][2] != ' ':
    return True
  elif p_inp[2][0] == p_inp[2][1] == p_inp[2][2] != ' ':
    return True
  elif p_inp[0][0] == p_inp[1][1] == p_inp[2][2] != ' ':
    return True
  elif p_inp[0][0] == p_inp[1][0] == p_inp[2][0] != ' ':
    return True
  elif p_inp[0][1] == p_inp[1][1] == p_inp[2][1] != ' ':
    return True
  elif p_inp[0][2] == p_inp[1][2] == p_inp[2][2] != ' ':
    return True
  elif p_inp[0][0] == p_inp[1][1] == p_inp[2][2] != ' ':
    return True
  elif p_inp[2][0] == p_inp[1][1] == p_inp[0][2] != ' ':
    return True
  else:
    return False


def update_loc(loc, p_inp, marker):
  not_empty = False
  map_numbers = {
    1: [0,0],
    2: [0,1],
    3: [0,2],
    4: [1,0],
    5: [1,1],
    6: [1,2],
    7: [2,0],
    8: [2,1],
    9: [2,2],
  }
  lmx = map_numbers[loc]
  if p_inp[lmx[0]][lmx[1]] == ' ': 
    p_inp[lmx[0]][lmx[1]] = marker
  else:
    not_empty = True
  return [p_inp, not_empty]


play_tic_toc_toa()

# OUTPUT

# Play the game with X or O ? X
# You have selected "X"
# |   |   |   |
# ---  ---  ---
# |   |   |   |
# ---  ---  ---
# |   |   |   |
# ---  ---  ---
# [Player 1]: Enter the location number: 1
# | X |   |   |
# ---  ---  ---
# |   |   |   |
# ---  ---  ---
# |   |   |   |
# ---  ---  ---
# [Player 2]: Enter the location number: 2
# | X | O |   |
# ---  ---  ---
# |   |   |   |
# ---  ---  ---
# |   |   |   |
# ---  ---  ---
# [Player 1]: Enter the location number: 5
# | X | O |   |
# ---  ---  ---
# |   | X |   |
# ---  ---  ---
# |   |   |   |
# ---  ---  ---
# [Player 2]: Enter the location number: 3
# | X | O | O |
# ---  ---  ---
# |   | X |   |
# ---  ---  ---
# |   |   |   |
# ---  ---  ---
# [Player 1]: Enter the location number: 9
# | X | O | O |
# ---  ---  ---
# |   | X |   |
# ---  ---  ---
# |   |   | X |
# ---  ---  ---
# [Player 1]: is the WINNER!
