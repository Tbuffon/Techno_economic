import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

import Hydrogen_system.Hydrogen

AlkEl = Hydrogen_system.Hydrogen.Alkelectrolyzer(100)
PemEl = Hydrogen_system.Hydrogen.PEMelectrolyzer(100)
PemFc = Hydrogen_system.Hydrogen.PEM_fuelCell()

def DrawVAcurve():
    x = [0., 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75]

    """碱性电解槽V/A曲线"""
    y = []
    for i in x:
        AlkEl.i = i
        y.append(AlkEl.volt_cell())
    x_output = np.array(x)
    y_output = np.array(y)
    xnew = np.linspace(x_output.min(), x_output.max(), 500)
    func = interp1d(x_output, y_output, kind='cubic')
    ynew = func(xnew)
    plt.plot(xnew, ynew, label="ALK EL (70℃, 30bar)")

    """PEM电解槽V/A曲线"""
    y = []
    for i in x:
        PemEl.i = i
        y.append(PemEl.volt_cell())
    x_output = np.array(x)
    y_output = np.array(y)
    xnew = np.linspace(x_output.min(), x_output.max(), 500)
    func = interp1d(x_output, y_output, kind='cubic')
    ynew = func(xnew)
    plt.plot(xnew, ynew, label="PEM EL (60℃, 30bar)")

    """PEM燃料电池V/A曲线"""
    y = []
    for i in x:
        PemFc.i = i
        y.append(PemFc.volt_cell())
    x_output = np.array(x)
    y_output = np.array(y)
    xnew = np.linspace(x_output.min(), x_output.max(), 500)
    func = interp1d(x_output, y_output, kind='cubic')
    ynew = func(xnew)
    plt.plot(xnew, ynew, label="PEM FC (60℃, 1bar")

    plt.xlabel("Current density[A/cm²]")
    plt.ylabel("Voltage[V]")
    plt.grid(True, lw=2, ls='--', c='.65')
    plt.legend()
    plt.show()

def DrawAlkElEfficiency():
    """碱性电解槽Efficiency曲线"""
    x = [0., 0.2, 0.4, 0.6, 0.8, 1]

    y = []
    for i in x:
        AlkEl.i = i
        y.append(AlkEl.faraday())
    x_output = np.array(x)
    y_output = np.array(y)
    xnew = np.linspace(x_output.min(), x_output.max(), 500)
    func = interp1d(x_output, y_output, kind='cubic')
    ynew = func(xnew)
    plt.plot(xnew, ynew, label="Cell effciency")

    plt.title("ALK electrolyzer")
    plt.ylabel("Efficiency")
    plt.grid(True, lw=2, ls='--', c='.65')
    plt.legend()
    plt.show()

def DrawPemElEfficiency():
    """Pem电解槽Efficiency曲线"""
    x = [0.2, 0.4, 0.6, 0.8, 1]

    y = []
    for i in x:
        PemEl.i = i
        y.append(PemEl.efficiency())
    x_output = np.array(x)
    y_output = np.array(y)
    xnew = np.linspace(x_output.min(), x_output.max(), 500)
    func = interp1d(x_output, y_output, kind='cubic')
    ynew = func(xnew)
    plt.plot(xnew, ynew, label="Cell effciency")

    plt.title("Pem electrolyzer")
    plt.ylabel("Efficiency")
    plt.grid(True, lw=2, ls='--', c='.65')
    plt.legend()
    plt.show()

if __name__ == "__main__":

    # x = [0., 0.2, 0.4, 0.6, 0.8, 1]

    DrawPemElEfficiency()