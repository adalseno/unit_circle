import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#@st.cache_data
def circle_xy(r:float=1)->tuple[float,float]:
    """
    Given the raidus r (float)
    returns x and y (float)
    to plot a parametric circle
    """
    t = np.linspace(0,2*np.pi,300)
    x = np.cos(t) * r
    y = np.sin(t) * r
    
    return x,y

def get_quadrant(angle:float)->tuple[float,float, str]:
    """
    Given an angle, in radians
    returns the coordinates of the point on the unit circle
    and the quadrant
    return px,py, q
    """
    # Coordinates
    px = np.cos(angle)
    py = np.sin(angle)
    
    # Convert to degrees 
    ang = angle * 180 /np.pi
    # We need positive angle
    while ang < 0:
        ang += 360

    # Quadrant
    q = q = f"X={px:.2f}, Y={py:.2f}"
    if ang > 0 and ang < 90:
        q += ", Q: I" # first
    elif ang > 90 and ang < 180:
        q += ", Q: II" # second
    elif ang > 180 and ang < 270:
        q += ", Q: III" # third
    elif ang > 270 and ang < 360:
        q += ", Q: IV" # fourth
    else:
        q+= ", Q: ?" # Undetermined
        
    return px,py, q


def plot_circle(x,y, angle:float, val_type:str="Degrees"):
    if val_type == "Degrees":
        ang_r = angle * np.pi / 180
    else:
        ang_r = angle

        
    px, py, q = get_quadrant(ang_r)

    fig, ax = plt.subplots(1,1,figsize=(10,10))
    ax.plot(x,y)
    ax.scatter(px,py, c="r", s=100)
    ax.text(px*1.2, py*1.2, q)
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    st.pyplot(fig)

st.title('Position on the unit circle')

# Get coordinates for the circle
x, y = circle_xy()

# Degrees or radians?
val_type = st.radio(
    "Select degrees or radians",
    ('Degrees', 'Radians'))

# Get value
angle = st.number_input("Insert the value:", value=0.0)

# Plot position
plot_circle(x,y,angle, val_type)

