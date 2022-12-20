"""Main Module"""

cycle_count = 0
next_signal = 20
signal_strength = []
register=1

def increment_cycle():
    signal_increment = 0
    if cycle_count==next_signal:
        signal_strength.append( next_signal * register)
        signal_increment =  40
    return next_signal + signal_increment

for l in open("input.txt","rt", encoding="utf8"):
    move = l.strip().split(" ")
    cycle_count+=1
    next_signal = increment_cycle()
    if move[0]!="noop":
        cycle_count+=1
        next_signal = increment_cycle()
        register += int(move[1])

print (f" signal = {sum(signal_strength)}")
