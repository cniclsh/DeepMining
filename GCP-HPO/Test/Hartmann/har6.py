import numpy as np

def har6(x):
    """6d Hartmann test function
    constraints:
    0 <= xi <= 1, i = 1..6
    global optimum at (0.20169, 0.150011, 0.476874, 0.275332, 0.311652, 0.6573),
    where har6 = 3.32236"""


    a = np.array([[10.0,   3.0, 17.0,   3.5,  1.7,  8.0],
                [ 0.05, 10.0, 17.0,   0.1,  8.0, 14.0],
                [ 3.0,   3.5,  1.7,  10.0, 17.0,  8.0],
                [17.0,   8.0,  0.05, 10.0,  0.1, 14.0]])
    c = np.array([1.0, 1.2, 3.0, 3.2])
    p = np.array([[0.1312, 0.1696, 0.5569, 0.0124, 0.8283, 0.5886],
                [0.2329, 0.4135, 0.8307, 0.3736, 0.1004, 0.9991],
                [0.2348, 0.1451, 0.3522, 0.2883, 0.3047, 0.6650],
                [0.4047, 0.8828, 0.8732, 0.5743, 0.1091, 0.0381]])
    s = 0
    for i in [0,1,2,3]:
        sm = a[i,0]*(x[0]-p[i,0])**2
        sm += a[i,1]*(x[1]-p[i,1])**2
        sm += a[i,2]*(x[2]-p[i,2])**2
        sm += a[i,3]*(x[3]-p[i,3])**2
        sm += a[i,4]*(x[4]-p[i,4])**2
        sm += a[i,5]*(x[5]-p[i,5])**2
        s += c[i]*np.exp(-sm)
    
    return [s]