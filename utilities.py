def get_king():
    with open("king.txt", "r") as king_file:
        return king_file.read()

def set_king(king):
    with open("king.txt", "w") as king_file:
        return king_file.write(king)

def get_websocket_info():
    with open("king.txt", "r") as king_file:
        return king_file.read().split(",")