# Rock defeats Scissors
# Scissors defeats Paper
# Paper defeats Rock

# The score for a single round is the score for the shape you selected
#   (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round:
#   (0 if you lost, 3 if the round was a draw, and 6 if you won)

# POINTS_ROCK = 1
# POINTS_PAPER = 2
# POINTS_SCISSORS = 3
# POINTS_LOSE = 0
# POINTS_DRAW = 3
# POINTS_WIN = 6

# THEIR_ROCK = "A"
# THEIR_PAPER = "B"
# THEIR_SCISSORS = "C"

# MY_ROCK = "X"
# MY_PAPER = "Y"
# MY_SCISSORS = "Z"

# scores = {
#     (THEIR_ROCK, MY_ROCK): POINTS_ROCK + POINTS_DRAW,
#     (THEIR_ROCK, MY_PAPER): POINTS_PAPER + POINTS_WIN,
#     (THEIR_ROCK, MY_SCISSORS): POINTS_SCISSORS + POINTS_LOSE,
#     (THEIR_PAPER, MY_ROCK): POINTS_ROCK + POINTS_LOSE,
#     (THEIR_PAPER, MY_PAPER): POINTS_PAPER + POINTS_DRAW,
#     (THEIR_PAPER, MY_SCISSORS): POINTS_SCISSORS + POINTS_WIN,
#     (THEIR_SCISSORS, MY_ROCK): POINTS_ROCK + POINTS_WIN,
#     (THEIR_SCISSORS, MY_PAPER): POINTS_PAPER + POINTS_LOSE,
#     (THEIR_SCISSORS, MY_SCISSORS): POINTS_SCISSORS + POINTS_DRAW,
# }

# f = open("day2input.txt")
# contents = f.read().strip()
# games = [tuple(plays.split(" ")) for plays in contents.split("\n")]
# scores = [scores[plays] for plays in games]
# print(sum(scores))

POINTS_ROCK = 1
POINTS_PAPER = 2
POINTS_SCISSORS = 3
POINTS_LOSE = 0
POINTS_DRAW = 3
POINTS_WIN = 6

THEIR_ROCK = "A"
THEIR_PAPER = "B"
THEIR_SCISSORS = "C"

I_SHOULD_LOSE = "X"
I_SHOULD_DRAW = "Y"
I_SHOULD_WIN = "Z"

scores = {
    (THEIR_ROCK, I_SHOULD_LOSE): POINTS_LOSE + POINTS_SCISSORS,
    (THEIR_ROCK, I_SHOULD_DRAW): POINTS_DRAW + POINTS_ROCK,
    (THEIR_ROCK, I_SHOULD_WIN): POINTS_WIN + POINTS_PAPER,
    (THEIR_PAPER, I_SHOULD_LOSE): POINTS_LOSE + POINTS_ROCK,
    (THEIR_PAPER, I_SHOULD_DRAW): POINTS_DRAW + POINTS_PAPER,
    (THEIR_PAPER, I_SHOULD_WIN): POINTS_WIN + POINTS_SCISSORS,
    (THEIR_SCISSORS, I_SHOULD_LOSE): POINTS_LOSE + POINTS_PAPER,
    (THEIR_SCISSORS, I_SHOULD_DRAW): POINTS_DRAW + POINTS_SCISSORS,
    (THEIR_SCISSORS, I_SHOULD_WIN): POINTS_WIN + POINTS_ROCK,
}

f = open("day2input.txt")
contents = f.read().strip()
games = [tuple(plays.split(" ")) for plays in contents.split("\n")]
scores = [scores[plays] for plays in games]
print(sum(scores))
