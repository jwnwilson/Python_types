"""
Simple type checking for a python script example
"""
from typing import List
from typing import Mapping
from typing import Sequence
Vector = List[float]


class User:
    def __str__(self):
        return 'User instance!'


def expect_str(input_str: str) -> None:
    """This function will expect a string to print

    :param test: input string
    """
    print(f'This function only takes a string: {input_str}')


def expect_list(input_list: Vector) -> float:
    """return the sum of a list of floats or ints

    :param input_list: list of floats or ints
    """
    return sum(input_list)


def expect_user_mapping(user_mapping: Mapping[str, User]) -> None:
    """Take a mapping of string -> users

    :param user_mapping: [description]
    """
    for key in user_mapping:
        print(f'User: {user_mapping[key]}')


if __name__ == '__main__':
    # This will error and not run
    # expect_str(1)
    expect_str('test')
    sum_num = expect_list([1, 0.2, 0.5])
    print(f'Sum of numbers: {sum_num}')

    expect_user_mapping({
        'test': User()
    })

    # This will error and not run
    # expect_user_mapping({
    #     'test': {}
    # })
