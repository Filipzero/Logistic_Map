import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
from matplotlib.widgets import TextBox

font = {'family': 'serif',
        'color': 'cyan',
        'weight': 'normal',
        'size': 15}

# Logistic Map initial parameters
step = np.round(np.linspace(0, 4, 1000), 2)
r = 1
N = 2000
y = np.zeros(N) + 0.5
x = np.zeros(N)

# Bifurcation Diagram initial parameters
rate = np.linspace(1, 4, 1000)
N1 = 2000
y1 = np.zeros(N1) + 0.5
count = np.arange(round(N1*0.9), N1)

# Logistic Map
for n in range(N-1):
    y[n+1] = r * y[n] * (1-y[n]) # Logistic map
    x[n+1] = x[n] + 1 # Creates time indices (0,1,2,...)

# Bifurcation Diagram
for rs in rate:
    for i in range(N1-1):
        y1[i+1] = rs * y1[i] * (1-y1[i])
    u = np.unique(y1[count])
    r1 = rs * np.ones(len(u))
    # plotting
    plt.style.use('dark_background')
    plt.plot(r1, u, '.', color='cyan', markersize=2)
    plt.ylabel(ylabel='X', fontdict=font)
    plt.xlabel(xlabel='r', fontdict=font)
    plt.title('Bifurcation', fontdict=font)
    

# Plotting Logistic Map
fig, ax = plt.subplots()
axes, = ax.plot(x, y, '-o', color='cyan')
ax.set_ylabel(ylabel='X', fontdict=font)
ax.set_xlabel(xlabel='Time', fontdict=font)
ax.set_title('$x_{n+1}$ = r * $x_{n}$ * (1-$x_{n}$)', fontdict=font)

# customizing axes of Logistic Map
fig.canvas.manager.set_window_title('Logistic Map')
ax.grid(color='white')
ax.tick_params(axis='x', colors='cyan')
ax.tick_params(axis='y', colors='cyan')
ax.spines['left'].set_color('cyan')
ax.spines['right'].set_color('cyan')
ax.spines['top'].set_color('cyan')
ax.spines['bottom'].set_color('cyan')
ax.set_facecolor('black')  # inner color of diagram
ax.figure.set_facecolor('black')   # outer color of diagram, they can be deleted
# since I think 'plt.style.use('dark_background')' changes background universally.
ax.set_ylim(0, 1)

# defining axSlider and Reset button
fig.subplots_adjust(bottom=0.25)  # slider was too close to diagram, so I moved it down
ax_slider = fig.add_axes([0.15, 0.1, 0.65, 0.03])  # x position, yposition, width, height
slider = Slider(ax_slider, label='r', valmin=0, valmax=4, valinit=1, valstep=step)  # mechanism of slider
slider.label.set_size(15)  # size of label
slider.label.set_color('cyan')  # color of label
ax_reset = fig.add_axes([0.89, 0.1, 0.045, 0.03])
button = Button(ax_reset, label='Reset', color='black', hovercolor='darkred')
button.label.set_color('cyan')
button.ax.spines['bottom'].set_color('cyan')
button.ax.spines['top'].set_color('cyan')
button.ax.spines['right'].set_color('cyan')
button.ax.spines['left'].set_color('cyan')

# Create x_0 button
axbox = fig.add_axes([0.5, 0.95, 0.035, 0.025])
x_0 = TextBox(axbox, label='$x_{0}$=', color='grey', hovercolor='grey')
x_0.label.set_color('cyan')
x_0.ax.spines['bottom'].set_color('cyan')
x_0.ax.spines['top'].set_color('cyan')
x_0.ax.spines['right'].set_color('cyan')
x_0.ax.spines['left'].set_color('cyan')
x_0.text_disp.set_color('black')

# Text box saying must be between 0 and 1!
ax_label = fig.add_axes([0.54, 0.962, 0.25, 0.03])  # x, y, width, height
ax_label.axis('off')  # hides borders and ticks
ax_label.text(0, 0, 'Must be between 0 and 1 !!!', color='cyan', fontsize=10, va='center')


# updating the plot
def update(val):
    current_v = slider.val
    r_logi = current_v # I had r = current_v, but not necessary. I can rename it, but it still has a connection
    # to its initial r
    for ls in range(N - 1):
        y[ls + 1] = r_logi * y[ls] * (1 - y[ls])
        axes.set_ydata(y)
    fig.canvas.draw()


slider.on_changed(update)


def reset(event):
    slider.reset()

button.on_clicked(reset)

# Text box for initial x_0 value.
def change_value(submit):
    
    try:
        if '.' in submit:
            decimals = submit.split('.')[-1]
            if len(decimals) > 4:
                print("Please enter at most 4 decimal places.")
                return

        new_x0 = float(submit)
        
        if 0 <= new_x0 <= 1:
            y[0] = new_x0  # update initial condition
            # Recalculate logistic map
            for n in range(N - 1):
                y[n + 1] = slider.val * y[n] * (1 - y[n])
            axes.set_ydata(y)
            fig.canvas.draw_idle()

        else:
            print("Value must be between 0 and 1!")

    except ValueError:
        print("Please enter a valid number!")

x_0.on_submit(change_value)

plt.show()
