# coding=utf-8


import re


def judge_credit_card(card_number):
    """
    judge a valid credit card number
    :param card_number: card number,str
    :return: card number?,bool
    """
    if not re.match(r"[4-6]",card_number):
        return False
    if not re.search(r"^\d{4}-\d{4}-\d{4}-\d{4}$",card_number):
        return False
    if re.search(r"(\d)\1{3,}",card_number.replace("-","")):
        return False
    return True


if __name__ == "__main__":
    card_number1 = "2165-6565-6698-9648"
    card_number2 = "4565-6565-6698-96446"
    card_number3 = "4565-6565-6698-964A"
    card_number4 = "456-6565-6698-9648"
    card_number5 = "4565-6565-6698,9644"
    card_number6 = "4565-6566-6698-9644"
    card_number7 = "4565-6565-6698-9644"
    print(judge_credit_card(card_number1))
    print(judge_credit_card(card_number2))
    print(judge_credit_card(card_number3))
    print(judge_credit_card(card_number4))
    print(judge_credit_card(card_number5))
    print(judge_credit_card(card_number6))
    print(judge_credit_card(card_number7))