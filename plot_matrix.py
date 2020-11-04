# TODO: 
import numpy as np
import scipy


def generate_random_matrix(m, n):
    #raise NotImplementedError  # TODO: 删除该行，实现该函数功能
    return(np.random.randint(0,2,(m,n))

def save_matrix(matrix, file_name):
    #raise NotImplementedError  # TODO: 删除该行，实现该函数功能
    return(scipy.misc.imsave(file_name,matrix))

if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
