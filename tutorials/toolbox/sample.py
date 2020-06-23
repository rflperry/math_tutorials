import numpy as np


def sample_unif_cubes(n, d):
    """
    Sample n points from a d dimensional uniform cube
    """
    return np.random.uniform(-0.5, 0.5, size=(n,d))

def sample_unif_balls(n, d):
    """
    Sample n points from a d dimensiona unit ball
    """
    balls = np.random.normal(0,1,size=(n,d))
    
    for i in range(n):
        balls[i,:] *= np.random.power(d) / norm(balls[i,:])
    
    return balls

def sample_unif_spheres(n=30, d=100, d_embedded=None, r=1):
    """
    Sample n points from a d-1 dimensional unit sphere in d dimensions with radius r
    """
    balls = np.random.normal(0,1,size=(n,d))
    
    for i in range(n):
        balls[i,:] /= np.linalg.norm(balls[i,:]) / r
        
    if not d_embedded is None:
        balls = np.hstack((balls, np.zeros((balls.shape[0],d_embedded - d))))
        balls += np.random.normal(0,0.1,balls.shape)
    
    return balls