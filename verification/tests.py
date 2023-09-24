"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": [2000], "answer": True},
        {"input": [1900], "answer": False},
        {"input": [2004], "answer": True},
        {"input": [2100], "answer": False},
        {"input": [2020], "answer": True},
        {"input": [2021], "answer": False},
        {"input": [1600], "answer": True},
        {"input": [1700], "answer": False},
        {"input": [1800], "answer": False},
        {"input": [2400], "answer": True}
    ],
    "Extra": [
        {"input": [2500], "answer": False},
        {"input": [1], "answer": False}
    ]
}

