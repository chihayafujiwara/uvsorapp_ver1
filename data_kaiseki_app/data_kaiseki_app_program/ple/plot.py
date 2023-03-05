import matplotlib.pyplot as plt

def plot(x,y):
    fig1 = plt.figure(figsize=(6,3))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    ax1 = fig1.add_subplot(1,1,1)
    ax1.plot(x,y,color = "black")
    ax1.set_xlabel('Energy [eV]')
    ax1.set_ylabel('Intensity [a.u]')
    ax1.grid()
    return([fig1])