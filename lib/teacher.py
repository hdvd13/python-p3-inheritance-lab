#!/usr/bin/env python

from user import User

import random

knowledge = [
    "Python function call definition",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "str is a data type in Python",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge=[None]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]