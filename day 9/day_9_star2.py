"""Main Module"""

rope = [[0, 0] for _ in range(10)]
visited_positions = {(0,0)}

for l in open("input.txt","rt", encoding="utf8"):
    direction, count = l.strip().split(" ")
    count = int(count)

    x_delta = 1 if direction == "R" else -1 if direction == "L" else 0
    y_delta = 1 if direction == "U" else -1 if direction == "D" else 0

    for _ in range(count):
        rope[0][0] += x_delta
        rope[0][1] += y_delta

        for i in range(9):
            head_position = rope[i]
            tail_position = rope[i + 1]

            row_dist= head_position[0]-tail_position[0]
            col_dist = head_position[1]-tail_position[1]
            # print(f"col-dist={col_dist}")
            # print(f"row-dist={row_dist}")
            if abs(row_dist) > 1 or abs(col_dist) > 1:
                if row_dist == 0:
                    tail_position[1] += col_dist // 2
                elif col_dist == 0:
                    tail_position[0] += row_dist // 2
                else:
                    tail_position[0] += 1 if row_dist > 0 else -1
                    tail_position[1] += 1 if col_dist > 0 else -1


        # print(f"head={head_position}")
        # print(f"tail={tail_position}")
        visited_positions.add(tuple(rope[-1]))


print (f" visited positions = {len(visited_positions)}")
