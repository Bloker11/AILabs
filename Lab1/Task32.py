import numpy as np
import matplotlib.pyplot as plt

def listTesting():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 3, 7, 6]
    list3 = list1 + list2
    print(list3)

def numpyTesting():
    vec1 = np.array([1, 2, 3, 4, 5])
    vec2 = np.array([4, 5, 3, 7, 6])
    vec3 = vec1 + vec2
    print(vec3)

def main():
    listTesting()
    numpyTesting()

if __name__ == "__main__":
    main()

def plotTesting():
    vec1 = np.array([1, 2, 3, 4, 5])
    vec2 = np.array([4, 5, 3, 7, 6])
    plt.plot(vec1, vec2, 'bo')
    plt.show()

plotTesting()