def generate_board()-> str:
    """
    generate Omok board

    Returns:
        str: Omok board
    """
    while True:
        board_size = int(input("Board size (>10) :"))
        if board_size > 10:
            break

    board_top = f"┌{'┬'*(board_size - 2)}┐"
    board_mid = f"├{'┼'*(board_size - 2)}┤"
    board_bot = f"└{'┴'*(board_size - 2)}┘"
    board = board_top + "\n" + (board_mid + "\n") * (board_size - 2) + board_bot

    return board
