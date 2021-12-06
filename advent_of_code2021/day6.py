def read_puzzle(filepath):
    with open(filepath, 'r') as in_f:
        line = in_f.readlines()[0]
    return [int(x) for x in line.split(',')]


class LanternFishSquad():
    def __init__(self, timers):
        self.list_fishes = {t: timers.count(t) for t in range(9)}

    def clock(self):
        new_list_fishes = {}
        for timer in range(9):
            if timer == 8:
                new_list_fishes[8] = self.list_fishes[0]
            elif timer == 6:
                new_list_fishes[6] = self.list_fishes[0] + self.list_fishes[7]
            else:
                new_list_fishes[timer] = self.list_fishes[timer + 1]

        self.list_fishes = new_list_fishes

    def __len__(self):
        return sum(self.list_fishes.values())

    def __repr__(self):
        return ','.join([str(fish) for fish in self.list_fishes])


if __name__ == '__main__':
    init_timers = read_puzzle('./inputs/day6.txt')
    squad = LanternFishSquad(init_timers)
    for i in range(1, 1 + 256):
        squad.clock()
    print(len(squad))
