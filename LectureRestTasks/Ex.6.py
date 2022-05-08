import math


def function(age, weight, height):
    h1 = (-0.46122 * age) + (0.97314 * weight) + (-0.39203 * height) + 1 * 0.80109
    h2 = (0.78548 * age) + (2.10584 * weight) + (-0.57847 * height) + (1 * 0.43529)
    result = (-0.81546 * 1 / (1 + math.exp(-h1))) + (1.03775 * 1 / (1 + math.exp(-h2))) - 1 * 0.2368
    return result


print(function(23, 75, 176))
