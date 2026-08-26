#!/usr/bin/env python3
"""Gera gráficos com aparência próxima ao visualizador do LTspice."""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

OUT = Path(__file__).resolve().parent / "figuras"
OUT.mkdir(exist_ok=True)

GREEN = "#00ff00"
BLUE = "#4d6bff"
CYAN = "#00ffff"
MAGENTA = "#ff40ff"
RED = "#ff3030"
YELLOW = "#ffff00"


def style():
    plt.rcParams.update({
        "figure.facecolor": "black", "axes.facecolor": "black",
        "savefig.facecolor": "black", "text.color": "white",
        "axes.labelcolor": "white", "axes.edgecolor": "#bfbfbf",
        "xtick.color": "white", "ytick.color": "white",
        "grid.color": "#555555", "grid.alpha": 0.35,
        "font.family": "DejaVu Sans", "font.size": 9,
        "legend.facecolor": "black", "legend.edgecolor": "#777777",
        "legend.labelcolor": "white", "lines.linewidth": 1.25,
    })


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, dpi=220, bbox_inches="tight")
    plt.close(fig)


def divisor():
    vin = np.linspace(0, 15, 301)
    r1, r2, rl = 1200.0, 2200.0, 1000.0
    req = r2 * rl / (r2 + rl)
    sem = vin * r2 / (r1 + r2)
    com = vin * req / (r1 + req)
    fig, ax = plt.subplots(figsize=(7.5, 3.7))
    ax.plot(vin, sem, color=BLUE, label=r"V(vcarga), $R_L=1000\,M\Omega$")
    ax.plot(vin, com, color=GREEN, label=r"V(vcarga), $R_L=1\,k\Omega$")
    ax.axvline(10, color="#aaaaaa", ls="--", lw=.8)
    ax.scatter([10, 10], [sem[200], com[200]], c=[BLUE, GREEN], s=22)
    ax.text(10.2, sem[200]+.2, "6,471 V", color=BLUE)
    ax.text(10.2, com[200]-.55, "3,642 V", color=GREEN)
    ax.set(xlabel="V1 (V)", ylabel="Tensão (V)", xlim=(0, 15), ylim=(0, 10))
    ax.grid(True); ax.legend(loc="upper left", framealpha=.85)
    save(fig, "grafico-item-2-dc.png")


def rc_bode():
    r, c = 3900.0, 100e-9
    fc = 1/(2*np.pi*r*c)
    f = np.logspace(np.log10(3.88), np.log10(38800), 1200)
    h = 1/(1+1j*2*np.pi*f*r*c)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7.5, 5), sharex=True)
    a1.semilogx(f, 20*np.log10(abs(h)), color=GREEN, label="V(vout)")
    a1.axvline(388, color=YELLOW, ls=":", label="referência: 388 Hz")
    a1.axvline(fc, color=CYAN, ls="--", label="corte: 408,1 Hz")
    a1.set_ylabel("Magnitude (dB)"); a1.set_ylim(-45, 2); a1.grid(True); a1.legend()
    a2.semilogx(f, np.angle(h, deg=True), color=MAGENTA)
    a2.axvline(388, color=YELLOW, ls=":"); a2.axvline(fc, color=CYAN, ls="--")
    a2.set(xlabel="Frequência (Hz)", ylabel="Fase (graus)", ylim=(-95, 5)); a2.grid(True)
    save(fig, "grafico-item-3-bode.png")


def rlc_transient():
    l, c = .1, 1e-9
    t = np.linspace(0, 300e-6, 5000)
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    for r, color in zip([4700, 12000, 22000], [GREEN, BLUE, RED]):
        sys = signal.TransferFunction([1], [l*c, r*c, 1])
        tout, y = signal.step(sys, T=t)
        ax.plot(tout*1e6, y, color=color, label=f"R={r/1000:g}k")
    ax.axhline(1, color="#aaaaaa", ls="--", lw=.8)
    ax.set(xlabel="Tempo (µs)", ylabel="V(vout) (V)", xlim=(0, 300), ylim=(-.05, 1.58))
    ax.grid(True); ax.legend(loc="lower right")
    save(fig, "grafico-item-4-transiente.png")


def rlc_bode():
    l, c = .1, 1e-9
    f = np.logspace(np.log10(159.16), np.log10(1591550), 1500)
    w = 2*np.pi*f
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7.5, 5), sharex=True)
    for r, color in zip([4700, 12000, 22000], [GREEN, BLUE, RED]):
        h = 1/(1-w*w*l*c+1j*w*r*c)
        a1.semilogx(f, 20*np.log10(abs(h)), color=color, label=f"R={r/1000:g}k")
        a2.semilogx(f, np.angle(h, deg=True), color=color)
    a1.axhline(0, color="#aaaaaa", ls="--", lw=.8)
    a1.set(ylabel="Magnitude (dB)", ylim=(-90, 9)); a1.grid(True); a1.legend()
    a2.set(xlabel="Frequência (Hz)", ylabel="Fase (graus)", ylim=(-190, 10)); a2.grid(True)
    save(fig, "grafico-item-5-bode.png")


def square_and_fft():
    r, c = 3900.0, 100e-9
    tau, period, ton = r*c, 2.5773e-3, 1.2887e-3
    dt = period/1000
    t = np.arange(0, 20*period+dt, dt)
    vin = np.where(np.mod(t, period) < ton, 1.0, -1.0)
    vout = np.empty_like(vin); vout[0] = -1
    a = np.exp(-dt/tau)
    for i in range(1, len(t)):
        vout[i] = vin[i] + (vout[i-1]-vin[i])*a
    mask = (t >= 5*period) & (t <= 10*period)
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax.plot(t[mask]*1e3, vin[mask], color=GREEN, label="V(vin)")
    ax.plot(t[mask]*1e3, vout[mask], color=BLUE, label="V(vout)")
    ax.set(xlabel="Tempo (ms)", ylabel="Tensão (V)", ylim=(-1.2, 1.2))
    ax.grid(True); ax.legend(loc="upper right")
    save(fig, "grafico-item-6-tempo.png")

    f1, fc = 1/period, 1/(2*np.pi*tau)
    n = np.arange(1, 16)
    vi = np.where(n % 2, 4/(np.pi*n), 0)
    vo = vi/np.sqrt(1+(n*f1/fc)**2)
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax.stem(n-.08, vi, linefmt=GREEN, markerfmt="go", basefmt=" ", label="V(vin)")
    ax.stem(n+.08, vo, linefmt=BLUE, markerfmt="bo", basefmt=" ", label="V(vout)")
    ax.set(xlabel="Ordem harmônica", ylabel="Amplitude de pico (V)", xticks=n, xlim=(.5, 15.5))
    ax.grid(True); ax.legend()
    save(fig, "grafico-item-6-espectro.png")


if __name__ == "__main__":
    style(); divisor(); rc_bode(); rlc_transient(); rlc_bode(); square_and_fft()
