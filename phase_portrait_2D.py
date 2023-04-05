# Required packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.integrate import odeint


def phase_portrait_2D(params, dxdt, dydt, inits, 
                      fix_pts =  [], arrow_points = 25, xylab = ['x', 'y'], lw = 1.75, quad = True, traj_color = 'r'):
    """ 

    Generates a 2-dimensional phase portrait for a given system of ODEs on [-Lx, Lx]x[-Ly, Ly]
    Additionally, you can also generate trajectories for given initial state and time and fixed point(s)
    ...

    Parameters
    ----------
    params : ndarray
        Array filled with required parameters for the phase portrait
        params = [Lx, Ly, plt_title]

    dxdt, dydt : callable
        The function describing the system of ODEs. dxdt = f(x, y), dydt = g(x, y)

    inits : array 
        Array consisting of coordinates of initial points with the time to be calculated.
        e.g
        inits  = [[x1, y1, t1],
                  [x2, y2, t2],]
                  ...
                  [xn, yn, tn]]
    

    fix_pts : array, optional
        Array consisting of fixed points. Default is set to []

    arrow_points : int, optional
        Defining the number of points on the grid where the arrow will be generated.
        Default value is set to 25

    xylab : array (optional, default = ['x', 'y'])
        The x and y axis labels. Default = ['x', 'y']
        
    lw : float, optional
        Linewidth of the trajectories in the phase portrait. 
        Default value set to 1.75

    quad : bool, optional 
        Showing all quadrants if set to True. Otherwise, only showing the first quadrant (x>=0, y>=0)
        Default is set to True.
        showing all quadrants if True

    traj_color : string, optional
        The color of the trajectories. Default = 'red'
    

    """
    Lx, Ly = params[0], params[1]
    if quad :
        [Xa, Xb] = [-Lx, Lx]
        [Ya, Yb] = [-Ly, Ly]
    else :
        [Xa, Xb] = [0, Lx]
        [Ya, Yb] = [0, Ly]
    X = np.linspace(Xa, Xb, arrow_points)
    Y = np.linspace(Ya, Yb, arrow_points)
    X, Y = np.meshgrid(X, Y)

    def model(U,t):
        """
        Defining a function as an input for the odeint.
        """
        X, Y = U
        return [dxdt(X, Y), dydt(X, Y)]
    def cpoint(Z0,T):
        """
        Function to generate a unique trajectory given the initial points and the time
        
        Inputs
        ------
        Z0 : array
            coordinate of an initial points
        T : int
            time elapsed of the trajectory given the initial point
        """
        tspan = np.linspace(0, T, 300)
        ys = odeint(model, Z0, tspan)
        plt.plot(ys[:, 0], ys[:, 1], linewidth = lw , c = traj_color)

    # Plotting
    sns.set(style='white')
    plt.rcParams['figure.dpi'] = 125
    # Normalizing the dxdt(X, Y), dydt(X, Y)
    u = dxdt(X, Y) 
    v = dydt(X, Y)
    r = np.power(np.add(np.power(u, 2), np.power(v, 2)), 0.5) + 1e-6
    plt.quiver(X, Y, u/r, v/r, alpha = 0.75)
    plt.xlabel(xylab[0])
    plt.ylabel(xylab[1])
    for x0y0t in inits:
        cpoint(x0y0t[:2], x0y0t[2])
    plt.xlim([Xa, Xb])
    plt.ylim([Ya, Yb])
    plt.axvline(x = 0, c = 'k')
    plt.axhline(y = 0, c = 'k')
    plt.title(params[2], fontweight = "bold", fontsize = 12.5)
    if len(fix_pts) > 0:
        plt.scatter([x[0] for x in fix_pts], [x[1] for x in fix_pts], c = 'k', s = 25)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

