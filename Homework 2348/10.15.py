# Victor Lopez
# PSID:1243931
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return (self.team_wins / (self.team_wins + self.team_losses))


if __name__ == "__main__":

    team = Team()

    t_n = input()
    t_w = int(input())
    t_l = int(input())

    team.team_name = t_n
    team.team_wins = t_w
    team.team_losses = t_l

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.t_n, 'has a winning average!')
    else:
        print('Team', team.t_n, 'has a losing average.')