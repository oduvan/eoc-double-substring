"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "aaaa",
            "answer": 2
        },
        {
            "input": "abc",
            "answer": 0
        },
        {
            "input": "aghtfghkofgh",
            "answer": 3
        }
    ],
    "Extra": [
        {
            "input": "",
            "answer": 0
        },{
            "input": "abababaab",
            "answer": 3
        },{
            "input": "arefhjaref!!",
            "answer": 4
        },{
            "input": "aa",
            "answer": 1
        },{
            "input": "aaaaa",
            "answer": 2
        }
    ]
}
