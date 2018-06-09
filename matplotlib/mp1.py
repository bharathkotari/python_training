'''import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0.0,10.0,0.04)
#print(t)
s=np.sin(5+2*np.pi*t)
plt.plot(t,s)
plt.xlabel('time(t)')
plt.ylabel('function of (t)')
plt.title("sine graph")
plt.grid(True)
plt.savefig("graph.png")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

class A():
    def show_a(self):
        t = np.arange(0.0, 10.0,0.04)
        #print(t)
        s = np.sin(2*np.pi*t)
        plt.plot(t, s)
        plt.xlabel('time (t)')
        plt.ylabel('function of (t)')
        plt.title('Graph Title')
        plt.grid(True)
        plt.savefig("graph1.png")
        plt.show()
    
class B():
    def show_b(self):
        t = np.arange(0.0, 10.0,0.04)
        #print(t)
        s = np.sin(2*np.pi*t)
        plt.plot(t, s)
        plt.xlabel('time (t)')
        plt.ylabel('function of (t)')
        plt.title('Graph Title')
        plt.grid(True)
        plt.savefig("graph2.png")
        plt.show()
 
a = A()
a.show_a()

b = B()
b.show_b()'''

import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 10.0)
x2 = np.linspace(0.0, 20.0)

y1 = np.cos(2 * np.pi * x1) 
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, '-')
plt.title('Subplot 1')
plt.ylabel('Y axis1 value')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '+-')
plt.xlabel('time (s)')
plt.ylabel('Y axis2 value')

plt.show()