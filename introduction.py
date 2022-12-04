import numpy as np

if __name__ == '__main__':
    # Python list is a optimal data structure for data manipulation, but
    # not optimized for numerical analysis
    grades0 = [50, 50, 47, 97, 49, 3, 53, 42, 26, 74, 82, 62, 37, 15, 70, 27, 36, 35, 48, 52, 63, 64]
    hours = [10.0, 11.5, 9.0, 16.0, 9.25, 1.0, 11.5, 9.0, 8.5, 14.5, 15.5, 13.75, 9.0, 8.0, 15.5,
             8.0, 9.0, 6.0, 10.0, 12.0, 12.5, 12.0]
    grades1 = np.array(grades0)  # numpy ndarray (N-dimension array) is specific for numerical operations

    print(type(grades0), grades0 * 2)  # Duplicate the list length
    print(type(grades1), grades1 * 2)  # Numpy ndarray is able to perform element-wise calculation

    shape = grades1.shape  # returns a <class 'tuple'>

    avg = grades1.mean()  # returns a <class 'float'>

    data = np.array([hours, grades0])
    element = data[0][0]

    avg_hours = data[0].mean()
    avg_grades = data[1].mean()
    print("Average study hours {:.2f}\nAverage grades {:.2f}".format(avg_hours, avg_grades))
