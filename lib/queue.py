# Queue system file
"""
TODO: This entire section needs a rework
I think it's best to completely rethink why this is needed.
Seemed like a good idea at the beginning but now it's actual use
is sort of slim.
Need to heavily consider what data structure I will need for the bot.
"""
import random
import threading
import time
import json


def StartTimer(seconds: int):
    time.sleep(seconds)
    return


class StackActivityError(Exception):
    def __init__(self, message="Stack object is not active. Please activity it by .set_author(author: int)"):
        self.message = message

    def __repr__(self):
        return self.message


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
        self.active = False
        self.timer = 0

    def set_author(self, author: int):
        self.author = author
        self.active = True

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
        """
        self.challengers = sorted(self.challengers, key=lambda k: k['VAL'])

    def start_timer(self, seconds):
        self.timer = threading.Thread(
            target=StartTimer,
            args=(seconds, )
        )
        self.timer.start()
        self.timer.join()
        return "Finished"


class DataQueue:
    ids = []
    """
    Creates a queue of objects where data is stored an manipulated.
    
    Example:
        Storing a list of guilds storing a list of channels containing a list of pokemon :cool_steve:
    """
    def __new__(cls):
        with open("../data/data_queue/config.json", 'r') as file:
            config = json.load(file)
            DataQueue.ids = config["ids"]

    def __init__(self):
        self.data = []

    def add(self, obj):
        self.data.append(obj)

    def remove(self, obj):
        self.data.remove(obj)














