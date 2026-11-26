# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.



def eval_rpn(tokens):
    #   Outline:
    #   Create an empty stack.
    #   Go through each token.
    #   Push numbers onto the stack.
    #   If it is an operator, pop two numbers and calculate.
    #   Push the result back and return the final answer.

    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = int(a / b)

            stack.append(result)

    return stack.pop()


def decode_string(s):
    #   Outline:
    #   Create a stack to save previous strings and numbers.
    #   Go through each character.
    #   Build numbers and strings.
    #   Save information when an opening bracket appears.
    #   Repeat the string when a closing bracket appears.
    #   Return the decoded string.

    stack = []
    current = ""
    number = 0

    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)

        elif char == "[":
            stack.append((current, number))
            current = ""
            number = 0

        elif char == "]":
            previous, repeat = stack.pop()
            current = previous + current * repeat

        else:
            current += char

    return current


def daily_temperatures(temps):
    #    Outline:
    #   Create a result list filled with zeros.
    #   Create a stack to store day indexes.
    #   Go through each temperature.
    #   If a warmer temperature appears, calculate the days waited.
    #   Return the result list.

    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous = stack.pop()
            result[previous] = i - previous

        stack.append(i)

    return result


def num_islands(grid):
    # Outline:
    #   Create a counter for the islands.
    #   Go through every position in the grid.
    #   If land is found and has not been visited:
    #       Increase the island counter.
    #       Use a stack to explore connected land.
    #       Mark visited positions.
    #   Return the island counter.

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                stack = [(r, c)]
                visited.add((r, c))

                while stack:
                    row, col = stack.pop()

                    directions = [
                        (0, 1),
                        (0, -1),
                        (1, 0),
                        (-1, 0)
                    ]

                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if (0 <= new_row < rows and
                            0 <= new_col < cols and
                            grid[new_row][new_col] == "1" and
                            (new_row, new_col) not in visited):

                            visited.add((new_row, new_col))
                            stack.append((new_row, new_col))

    return islands


def main():
       # Test Part 1
    print(eval_rpn(["2", "1", "+", "3", "*"]))
    print(eval_rpn(["4", "13", "5", "/", "+"]))

       # Test Part 2
    print(decode_string("3[a]2[bc]"))
    print(decode_string("3[a2[c]]"))

       # Test Part 3
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(daily_temperatures([30, 40, 50, 60]))

       # Test Part 4
    print(num_islands(["11000", "11000", "00100", "00011"]))
    print(num_islands(["11110", "11010", "11000", "00000"]))


if __name__ == "__main__":
    main()
