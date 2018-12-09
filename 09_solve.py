from collections import defaultdict, deque, namedtuple

def parse(f):
    s = f.split(' ')
    return (int(s[0]), int(s[6]))

def solve_1(data):
    n_players, last_marble = data

    scores = defaultdict(lambda: 0)

    counter = 1
    current = 0
    circle = deque([0])

    # computes the circular index of x.
    c = lambda x: (x % len(circle))

    marble_worth = None
    break_ = False
    while counter <= last_marble:
        # print('iterate')
        for player in range(n_players):
            if counter > last_marble:
                break
            if counter % 23 == 0:
                seven_clockwise = circle[c(current-7)]
                
                del circle[c(current-7)]
                current = c(current-7)

                marble_worth = counter + seven_clockwise
                print(counter, player, marble_worth)
                scores[player] += marble_worth
            else:
                current = c(current+2)
                circle.insert(current, counter)
            counter += 1
            print('Step', counter, player+1, end=': ')
            for i, x in enumerate(circle):
                if i == current:
                    print('(', x, ')', sep='', end=' ')
                else:
                    print(x, end=' ')
            print()

            # print(counter, current, circle[current], circle)
            # if input() == 'break':
            #     marble_worth = last_marble
            #     break
    
    print(max(scores.items(), key=lambda x: x[1]))
    print(scores)




if __name__ == "__main__":
    with open('09_input.txt') as f:
        # solve_1(parse(f.read()))
        solve_1((17, 1104))