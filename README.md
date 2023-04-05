# phase-portrait-2d

A simple command to generate a phase potrait for a given 2-dimensional system of ordinary differential equations (ODEs). 
Additionally, you can also generate trajectories for given initial state and time and fixed point(s)



# Dependencies
You most likely have all the required packages installed already,
* `odeint` from `SymPy`
* `matplotlib` and `seaborn`
* Of course, `numpy`

# How to use it?
For demonstration purpose, observe a system of ODEs given below:\
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_black%20%5Clarge%20%5Cbegin%7Balign*%7D%20%5Cdfrac%7Bdx%7D%7Bdt%7D%26%3Dy-%5Cdfrac%7Bx%7D%7B2%7D%5C%5C%20%5Cdfrac%7Bdy%7D%7Bdt%7D%26%3Dx%5E2&plus;2x%20%5Cend%7Balign*%7D">

Draw the phase portrait for the system above on $[-3,3]\times [-3,3]$, with trajectories for given initial points $(x(0), y(0))$:
- $(-3, 1)$, for $t=5$ s
- $(-1, -3)$, for $t=15$ s
- $(2, -3)$, for $t=3$ s
- $(1.5, -3)$, for $t=8$ s
and fixed points $(0,0)$ and $(-2,-1)$.

```
# Define the system dxdt, dydt
dxdt = lambda x, y : y - 0.5*x
dydt = lambda x, y : x**2 + 2*x
Lx = 3
Ly = 3
# initial points [[x0_1, y0_1, t0_1], [x0_2, y0_2, t0_2], ..., [x0_n, y0_n, t0_n]]
inits = [[-3, 1, 5], [-1, -3, 15], [2, -3, 3], [1.5, -3, 8]] 
phase_portrait_2D([Lx, Ly, "Phase Portrait Example 1"], dxdt, dydt, inits, fix_pts = [[0, 0], [-2, -1]])
```

Voila ! The result is given below:\
![Phase Portrait Example 1](/pp1.png)


You can also adjust the line width, trajectories color, number of arrows, etc however you like. Go to town !
