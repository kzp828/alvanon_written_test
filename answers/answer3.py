# coding=utf-8


def compute_coefficient(list01,list02):
    """
    Compute Karl Pearson’s coefficient of correlation
    :param list01:first group data,list
    :param list02:second group data,list
    :return: Karl Pearson’s coefficient of correlation,str
    """
    mean1 = sum(list01) / len(list01)
    mean2 = sum(list02) / len(list02)
    covariance = sum((x - mean1) * (y - mean2) for x, y in zip(list01, list02))
    variance1 = sum((x - mean1) ** 2 for x in list01)
    variance2 = sum((y - mean2) ** 2 for y in list02)
    return str(round(covariance / (variance1 ** 0.5 * variance2 ** 0.5),3))


if __name__ == "__main__":
    array01 = [15,12,8,8,7,7,7,6,5,3]
    array02 = [10,25,17,11,13,17,20,13,9,15]
    print(compute_coefficient(array01,array02))