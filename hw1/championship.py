from random import randint


class Game:
    def __init__(self, team1, team2, score1, score2):
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2

    def print(self):
        print(f'{self.team1} - {self.team2} : {self.score1}-{self.score2}')


class Team:
    points = 0
    wins = 0
    loses = 0
    ties = 0
    goals_scored = 0
    goals_conceded = 0

    def __init__(self, name):
        self.name = name

    def play(self, opponent):
        max_goals = 5
        score = randint(0, max_goals)
        opponent_score = randint(0, max_goals)
        self.goals_scored += score
        opponent.goals_scored += opponent_score
        self.goals_conceded += opponent_score
        opponent.goals_conceded += score
        if score > opponent_score:
            self.points += 3
            self.wins += 1
            opponent.loses += 1
        elif score < opponent_score:
            opponent.points += 3
            opponent.wins += 1
            self.loses += 1
        else:
            self.points += 1
            opponent.points += 1
            self.ties += 1
            opponent.ties += 1
        return Game(self.name, opponent.name, score, opponent_score)


team_names = ['Red', 'Blue', 'Green', 'Yellow', 'Pink', 'White', 'Black']
teams = [Team(name) for name in team_names]
games = []
for i in range(len(teams) - 1):
    for j in range(i + 1, len(teams)):
        games.append(teams[i].play(teams[j]))
max_name_width = max(len(name) for name in team_names)
if max_name_width < 7:
    max_name_width = 7
print('Место {:<{max_name_width}} Очки Победы Поражения Ничьи Забито Пропущено'
      .format('Команда', max_name_width=str(max_name_width)))
teams.sort(key=lambda team: team.points, reverse=True)
for i in range(len(teams)):
    t = teams[i]
    print('{:<5} {:<{max_name_width}} {:<4} {:<6} {:<9} {:<5} {:<6} {}'
          .format(i + 1, t.name, t.points, t.wins, t.loses, t.ties, t.goals_scored, t.goals_conceded,
                  max_name_width=str(max_name_width)))
games_dict = {frozenset({game.team1, game.team2}): game for game in games}


def game_info(team1, team2):
    games_dict[frozenset({team1, team2})].print()


# game_info('Black', 'White')
