import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

import Hydrogen_system.Hydrogen

AlkEl = Hydrogen_system.Hydrogen.Alkelectrolyzer(100)
PemEl = Hydrogen_system.Hydrogen.PEMelectrolyzer(100)
PemFc = Hydrogen_system.Hydrogen.PEM_fuelCell()

if __name__ == "__main__":
    x = [0., 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75]
    # for i in x:
    #     AlkEl.i = i
    #     y.append(AlkEl.volt_rev())
    # plt.plot(x, y, label = "V_rev")
    #
    #
    # y = []
    # for i in x:
    #     AlkEl.i = i
    #     y.append(AlkEl.volt_act_an() + AlkEl.volt_act_cat())
    # plt.plot(x, y, label = "V_act")
    #
    # y = []
    # for i in x:
    #     AlkEl.i = i
    #     y.append(AlkEl.volt_ohm())
    # plt.plot(x, y, label = "V_ohm")

    """碱性电解槽V/A曲线"""

    y = []
    for i in x:
        AlkEl.i = i
        y.append(AlkEl.volt_cell())

    x_output = np.array(x)
    y_output = np.array(y)
    xnew = np.linspace(x_output.min(), x_output.max(), 500)
    func = interp1d(x_output, y_output, kind = 'cubic')
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
    func = interp1d(x_output, y_output, kind = 'cubic')
    ynew = func(xnew)
    plt.plot(xnew, ynew, label = "PEM EL (60℃, 30bar)")

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
    plt.plot(xnew, ynew, label = "PEM FC (60℃, 1bar")


    plt.xlabel("Current density[A/cm²]")
    plt.ylabel("Voltage[V]")
    plt.grid(True, lw=2, ls='--', c='.65')
    plt.legend()
    plt.show()

    """碱性电解槽Efficiency曲线"""

