# Logistic Map and Bifurcation Diagram Visualization

This project visualizes the logistic map and its bifurcation diagram, providing both a static bifurcation plot and an interactive logistic map where the control parameter r(growth rate) can be adjusted dynamically using a slider, as well as change the initial value of $x_0$.

## Overview

The logistic map is a classic example in chaos theory and nonlinear dynamics. It is defined by the recurrence relation:

$$
x_{n+1} = r \ x_n (1 - x_n)
$$

where:
* r is the growth rate parameter (typically between 0 and 4), and
* $x_n$ is the population ratio at step n

As r increases, the system transitions from stable equilibrium → periodic oscillations → deterministic chaos.

This Python script provides:

1. A **static bifurcation diagram** — showing the asymptotic behavior of **$x_n$** as a function of **r**.

2. An interactive **logistic map** — allowing you to explore how different **r** values affect the dynamics over time.

## Dependencies

Make sure you have the following Python libraries installed as shown inside the libraries.txt file.

## How to run

1. Save the script as logistic_map.py.

2. Run the file from your terminal or IDE: python3 logistic_map.py

3. Two plots will appear:
   * A bifurcation diagram (static plot).
   * An interactive logistic map window:
         * Move the slider to change the value of r
         * Press Reset to return to its initial value

## Visualization Details

**Bifurcation Diagram**

* Plots **$x_n$** against the parameter **r**.
* Iterates over 1000 values of **r** between 1 and 4.
* Discards the first 90% of iterations to focus on long-term behavior.

**Logistic Map**

* PLots **$x_n$** over time for a single value of r.
* Updates dynamically when you move the slider.
* Initial parameter $x_0$ can be specified with an accuracy of 4 decimal places.

## Mathematical Insight

| Range of ( r ) | Behavior of System                         |
| -------------: | ------------------------------------------ |
|      0 < r < 1 | Population dies out (converges to 0)       |
|      1 < r < 3 | Stable fixed point                         |
|   3 < r < 3.57 | Periodic oscillations (period doubling)    |
|       r > 3.57 | Chaotic regime with small periodic windows |


1. **Convergence to 0 ⟶ 0 < r < 1**

    * When we say that it converges to zero, it means that as we iterate the logistic map starting from some initial $x_0$, the value of the function becomes extremely small and thus practically zero.
    
    * **Example:** Let r=0.5 and $x_0$=0.87.
    * |  Iterations   | ($x_n$)                                |
      | ------------: | :--------------------------------------|
      |         $x_0$ | 0.87                                   |
      |         $x_1$ | 0.5 * 0.87 * (1 - 0.87) = 0.05655      |
      |         $x_2$ | 0.5 * 0.05655 * (1 - 0.05655) = 0.0267 |
      |         $x_3$ | 0.5 * 0.0267 * (1 - 0.0267) = 0.0130   |
      |         $x_4$ | 0.5 * 0.0130 * (1 - 0.0130) = 0.0064   |
      |         $x_5$ | 0.5 * 0.0064 * (1 - 0.0064) = 0.0032   |

At some point, $x_n$→0.
So for **r=0.5**, the system converges to zero, confirming the theoretical behavior of the logistic mapin this range.

2. **Fixed point ⟶ 1 < r < 3**

   * A fixed point means that for that value of **r** when we have an initial value of **$x_0$** close to **$x^*$** the sequence **$x_n$** at some point will converge meaning the **$x^*$** is a stable fixed point. In other words, small deviations from **$x^*$** decay over time rather than grow.

   * **Example:** Let r=1.5 and $x_0$=0.57.
   * |  Iterations   | ($x_n$)                               |
     | ------------: | :-------------------------------------|
     |         $x_0$ | 0.57                                  |
     |         $x_1$ | 1.5 * 0.57 * (1 - 0.57) = 0.36705     |
     |         $x_2$ | 1.5 * 0.36705 * (1 - 0.36705) = 0.349 |
     |         $x_3$ | 1.5 * 0.349 * (1 - 0.349) = 0.341     |
     |         $x_4$ | 1.5 * 0.341 * (1 - 0.341) = 0.338     |
     |         $x_5$ | 1.5 * 0.338 * (1 - 0.338) = 0.336     |

This time the sequence converges to **$x^*=0.33$**.

3. **Period doubling ⟶ 3 < r < 3.57**
   
   * The period doubling phenomenon is seen as **r** increases beyond 3. The system no longer settles for a singular value, but instead, it oscillates between multiple values.
  
   * **Example:** Let r=3.2 and $x_0$=0.7.
   * |  Iterations   | ($x_n$)                               |
     | ------------: | :-------------------------------------|
     |         $x_0$ | 0.7                                   |
     |         $x_1$ | 3.2 * 0.7 * (1 - 0.7) = 0.672         |
     |         $x_2$ | 3.2 * 0.672 * (1 - 0.672) = 0.705     |
     |         $x_3$ | 3.2 * 0.705 * (1 - 0.705) = 0.6677    |
     |         $x_4$ | 3.2 * 0.6677 * (1 - 0.6677) = 0.7119  |
     |         $x_5$ | 3.2 * 0.7119 * (1 - 0.7119) = 0.6561  |

As we can see with these initial parameters the values of $x_n$ oscillate between two main values, indicating a period-2 cycle. As **r** grows larger, oscillations between 4 values, then 8, 16, 32, etc. appear.

4. **Chaos ⟶ r > 3.57**

   * This is where our values "jump" unpredictably and is characteristic of chaos.
  
   *  **Example:** Let r=3.8 and $x_0$=0.43.
   * |  Iterations   | ($x_n$)                               |
     | ------------: | :-------------------------------------|
     |         $x_0$ | 0.43                                  |
     |         $x_1$ | 3.8 * 0.43 * (1 - 0.43) = 0.93118     |
     |         $x_2$ | 3.8 * 0.93118 * (1 - 0.93118) = 0.245 |
     |         $x_3$ | 3.8 * 0.245 * (1 - 0.245) = 0.702     |
     |         $x_4$ | 3.8 * 0.702 * (1 - 0.702) = 0.794     |
     |         $x_5$ | 3.8 * 0.794 * (1 - 0.794) = 0.624     |

Even though our system is deterministic we can clearly see that chaos exists, since it has sensitivity to initial conditions.
