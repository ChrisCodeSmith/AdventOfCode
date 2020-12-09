
# abbreviations: bp_sp = boarding pass seat position

def read_seating_file(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')


def part1():
    """ Calculate the seat ID for each item in the seat_ids list and use pythons builtin max function on the list
        to retrieve the max value
    """
    seating = read_seating_file('04_input.txt')
    seat_ids = []
    for seat in seating:
        seat_ids.append(seat_id(seat))
    print(f"Max Seat ID: {max(seat_ids)}")


def part2():
    """ """
    seating = read_seating_file('04_input.txt')
    seat_ids = []
    for seat in seating:
        seat_ids.append(seat_id(seat))
    last_seat_nmbr = max(seat_ids)
    seating_start = last_seat_nmbr - len(seat_ids) - 1
    last_seat = seating_start
    for seat in set(seat_ids):
        if seat != last_seat + 1:
            print(f"My Seat ID: {last_seat + 1}")
        last_seat = seat
    # print(set(seat_ids))


def seat_id(seat: (int, int)):
    decoded_seat = decode(seat)
    return decoded_seat[0]*8 + decoded_seat[1]


def decode(bp_sp: str):
    """ Return (row, column) tuple from string. The string is binary encoded, not by 0 and 1, but by F&B and L&R
        Therefore we convert it to binary and use pythons int() function to convert it to decimal
    """
    row = ''
    col = ''
    for x in range(0, 7):
        if bp_sp[x] == 'F':
            row = f"{row}0"
        elif bp_sp[x] == 'B':
            row = f"{row}1"
    for x in range(7, 10):
        if bp_sp[x] == 'L':
            col = f"{col}0"
        elif bp_sp[x] == 'R':
            col = f"{col}1"
    row = int(row, 2)
    col = int(col, 2)
    return row, col


if __name__ == '__main__':
    part1()
    part2()
