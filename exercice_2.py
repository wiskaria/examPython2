def draw_hollow_square(char_to_draw, size):
    new_char = char_to_draw + " "
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1:
                print(new_char, end="")
            elif j == 0 or j == size - 1:
                print(new_char, end="")
            else:
                print("  ", end="")
        print()


draw_hollow_square("+", 20)
