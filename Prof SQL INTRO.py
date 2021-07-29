
import sqlite3
import numpy as np
import matplotlib.pyplot as plt




def fetch():
    conn = sqlite3.connect('heart.db')

    c = conn.cursor()

    pulsos = c.execute('SELECT pulso FROM sensor').fetchall()

    conn.close()

    return pulsos




def show(data):
    fig = plt.figure()
    
    fig.suptitle('Ritmo Cardiaco')
    
    ax = fig.add_subplot()

    ax.plot(data)
    ax.grid()

    ax.set_xlabel(' ')
    ax.set_ylabel('Pulso')
    
    plt.show()




def stats(data):
    printeables = np.asanyarray([data])

    print("Mean", printeables.mean())
    print("Max", printeables.max())
    print("Min", printeables.min())
    print("Std", printeables.std())

    return printeables



def regiones(data):
    
    datos = np.asanyarray([data])

    meanV = datos.mean()
    stdV = datos.std()

    x1=[]
    y1=[]

    x2=[]
    y2=[]

    x3=[]
    y3=[]

    
    for i in range(len(data)):
        if data[i] <= (meanV-stdV):
            x1.append(i)
            y1.append(data[i])

        elif data[i] >= (meanV+stdV):
            x2.append(i)
            y2.append(data[i])

        else:
            x3.append(i)
            y3.append(data[i])


    
    fig = plt.figure()
    
    fig.suptitle('Ritmo Cardiaco En Distintos Momentos')

    
    ax1 = fig.add_subplot(12,12,(1,36))
    ax2 = fig.add_subplot(12,12,(49,84))
    ax3 = fig.add_subplot(12,12,(97,132))

    ax1.scatter(x1, y1, marker='.', c="red")
    ax1.set_xlabel(' ')
    ax1.set_ylabel('Pulso')
    ax1.grid()
    ax1.set_title('Aburrida')
    


    ax2.scatter(x2, y2, marker='.', c="blue")
    ax2.set_xlabel(' ')
    ax2.set_ylabel('Pulso')
    ax2.grid()
    ax2.set_title('Enganchada')
    


    ax3.scatter(x3, y3, marker='.', c="green")
    ax3.set_xlabel(' ')
    ax3.set_ylabel('Pulso')
    ax3.grid()
    ax3.set_title('Mirando')
    


    plt.show()



if __name__ == '__main__':

    data = fetch()

    show(data)

    stats(data)

    regiones(data)


    