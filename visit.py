import sys


def snail_walk(n, m):
    if n == 0 or m == 0:
        print(f'Incorrect matrix dimensions: {n}x{m}')
        return

    x_dir = [1, 0, -1, 0]
    y_dir = [0, 1, 0, -1]
    count = n * m  # n rows, m columns
    x = -1
    y = 0
    cons = [m, n-1, m-1, n-2]  # walk constraints

    while count:
        for idx, (dx, dy) in enumerate(zip(x_dir, y_dir)):
            limit = cons[idx]

            while limit:
                x += dx
                y += dy

                print((y, x))
                count -= 1
                limit -= 1
                 
                if count == 0:
                    break
            cons[idx] -= 2 
            if count == 0:
                break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: visit.py 3x4")
        sys.exit(1)
    matrix_str = sys.argv[1]
    
    n, m = matrix_str.split('x')
    n, m = int(n), int(m)
    print(f"Snail matrix walk for a '{n}x{m}' matrix")
    snail_walk(n, m)
