# coding=utf-8


def get_super_P(n,k):
    """
    get super digit of P
    :param n: number, int
    :param k: the number of times,  int
    :return: P
    """
    if isinstance(n,str):
        n = sum([int(c) for c in n])
        return get_super_P(n,1)
    elif isinstance(n,int):
        if -1 < n < 10 and k == 1:
            return n
        else:
            return get_super_P(str(n) * k,1)
    else:
        raise Exception("type error")


if __name__ == "__main__":
    n = 148
    k = 3
    print(get_super_P(n,k))