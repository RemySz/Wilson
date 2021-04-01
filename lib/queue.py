# Queue system file
import random


class QueueToken:
    TokenCount: int
    """
    Token is what stores information about a battle/fight in the queue.
    This is where the UID is generated.
    """
    def __init__(self, challenger_id, receiver_id):
        self.CID = challenger_id
        self.RID = receiver_id
        QueueToken.TokenCount += 1
        self.UID = random.random()


class Queue:
    """
    Queue allows games (like Rock Paper Scissors) to fight player vs player.
    This works by having the game enter information about the fight into a queue
    which then can be accepted by the receiver using !accept

    Information stored in a single queue:
        - Unique Identifer (UID) to make sure each game in the queue is different
        - Challenger information
        - Reciever information

    Each game will have it's own separate Queue (as an object)
    """
    def __init__(self):
        self.queue = {}

    def add(self, token: QueueToken):
        self.queue[token.UID] = {
            "CID": token.CID,
            "RID": token.RID
        }
        return token

    def remove(self, UID: int):
        try:
            del self.queue[UID]
        except Exception as e:
            return e
        return

    def clear(self):
        self.queue.clear()


class Stack:
    """
    Similar to a Queue but accepts an infinite number of receivers and a value which is used
    to sort the receivers.
    """
    def __init__(self):
        self.author = None
        self.stack_value = None  # Current highest value
        self.base_value = None  # Base value to add challenger to stack
        self.challengers = []

    def set_author(self, author: int):
        self.author = author

    def add_challenger(self, challenger: int, value: int):
        if self.base_value is not None and value > self.base_value:
            token = {"ID": challenger, "VAL": value}
            self.challengers.append(token)

    def set_base_value(self, value: int):
        if self.base_value is None:
            self.base_value = value

    def sort(self):
        """
        Sorts Stack by challenger value.
        bubble sort :)
        """

        challengers = []
        values = []

        for challenger in self.challengers:
            challengers.append(challenger["ID"])
            values.append(challenger["VAL"])

        for i in range(len(values)):
            if values[i] < values [i+1]:
                pass  # TODO

        del challengers
        del values














