# AGT Python Programming Task
#
# Task 1: Problem solving:
#         Complete missing functionality on methods marked with "TODO".
#         Identify bugs in methods marked with "FIXME".
#         Expected functionality is described in the method documentation.
# Task 2: Architecture / code style:
#         Refactor the existing code for readability, best practices, style, validation and documentation etc.
# Task 3: Tests:
#         Write some meaningful unit test(s) for the methods marked with "TEST MISSING"
# Task 4: Ops:
#         Reorganize files, directories and add setup information / scripts
#         in order to the create a redistributable python package with some simple commands
#         Provide an example script on the platform of your choice.
#
# Rules:
# - Use Python 3
# - Avoid all platform specific code
#   The code should run on either a recent Windows and/or common Linux distributions. Preferably all.
# - You may use any built-in python library
# - You may use third party libraries - if they fulfill these conditions:
#   - available at: https://pypi.python.org/pypi and open source
#   - well known and documented (use your judgement)
#   - pure python only (e.g. no compiled plugins written in C or FORTRAN)

import time
from datetime import datetime, timedelta
import threading
import unittest

# FIXME: the intervals seem not to be exactly as intended but slightly off
# TEST MISSING


def schedule_method_calls(method, amount, interval=0.5):
    """
    Calls the given :method: in :amount: of times with each call  EXACTLY :interval: seconds apart
    :param method: A callable object
    :param amount: An inter of the amount of call that should be done
    :param interval: the amount of seconds each call is apart
    :return: None
    """
    if amount < 0:
        raise RuntimeError("Amount should be positive")
    c = 0
    while amount > c:
        c += 1
        init_sec = datetime.utcnow().second
        ms = datetime.utcnow().microsecond
        if ms < 999999 and init_sec == datetime.utcnow().second:
            if c > 1:
                time.sleep((999999 - ms)/1000000.0 + interval -1)
            else:
                time.sleep((999999 - ms)/1000000.0)
        threading.Thread(target=method, args=[]).start()

# TODO
# TEST MISSING


def merge_dictionaries_recursive(*args) -> dict:
    """
    :param args:    a variable amount of dictionaries
                    which may contain other dictionaries as values which should also be merged (tree)                   
    :return: a merged dictionary tree. The merge is done based on identical keys
    """
    # return {"this": "doesn't", "work": "yet"}
    return {key: value for dictionary in args for key, value in dictionary.items()}


# REFACTOR / FIX
def search_in_file(filename, search_terms=[]):
    """
    Searches for given search terms in a text file and returns true if all of them have been found
    :param filename: file to open and search in      
    :param search_terms: terms to search for 
    :return: True if any search term has been found
    """
    try:
        terms = {k: 0 for k in search_terms}
        with open(filename, 'r') as f:
            for line in f:
                for term in list(terms):
                    if line.find(term) != -1:
                        del terms[term]
                if not len(terms):
                    return True
        return False
    except Exception as e:
        print("an error occured when searching in the file: {}".format(str(e)))


class TestSchedule(unittest.TestCase):
    result = []
    interval = None
    amount = None

    def demo_method(self):
        now = datetime.now()
        self.result.append(now)
        print("this should repeat EXACTLY every: " + str(self.interval) + " seconds.")
        print("the time is now: {}".format(now))
        time.sleep(2.2)  # placeholder, here we do some work

    def test_all(self):
        print ("TESTING schedule task in progress")
        time.sleep(2)
        self.result = []
        self.interval = 2
        self.amount = 5
        schedule_method_calls(self.demo_method, self.amount, self.interval)
        previous = ""
        self.result.sort()
        # print (self.result)
        for res in self.result:
            if previous != "":
                self.assertEqual(res.replace(microsecond=0), previous.replace(microsecond=0)
                                 + timedelta(seconds=self.interval))
            previous = res
        print ("Task Schedule tested OK")


class TestMergeDictionaries(unittest.TestCase):
    def simple_test(self):
        d1 = {"hello": "world", "bananas": "are delicious"}
        d2 = {"hello": "again", "this": {"is": "fun"}}
        d3 = {"this": {"is": "easy"}}
        expected_output = {**d1, **d2, **d3}
        actual_output = merge_dictionaries_recursive(d1, d2, d3)
        self.assertEqual(actual_output, expected_output)
        print ("Merged tested OK")


if __name__ == "__main__":
    """
    Runs all methods form demonstration purposes
    """

    d1 = {"hello": "world", "bananas": "are delicious"}
    d2 = {"hello": "again", "this": {"is": "fun"}}
    d3 = {"this": {"is": "easy"}}
    merged_d = merge_dictionaries_recursive(d1, d2, d3)
    print(merged_d)

    print(search_in_file("test.txt", ["dog", "cat"]))
    print(search_in_file("test.txt", ["dog", "lizard"]))

    def demo_method():  # don't change this, it demonstrates the bug
        print("this should repeat EXACTLY every: " + str(interval) + " seconds.")
        print("the time is now: {}".format(datetime.now()))
        time.sleep(0.2)  # placeholder, here we do some work

    interval = 1
    amount = 5
    schedule_method_calls(demo_method, amount, interval)
    ## TESTS!!
    TestMergeDictionaries().simple_test()
    TestSchedule().test_all()