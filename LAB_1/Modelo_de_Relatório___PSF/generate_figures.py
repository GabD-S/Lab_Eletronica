#!/usr/bin/env python3
"""Gera as figuras numéricas do Relatório do Roteiro 1.

Os parâmetros abaixo reproduzem exatamente os seis esquemáticos LTspice
armazenados em ../Gabriel. As curvas são calculadas a partir dos modelos
ideais dos circuitos, sem dados experimentais ou capturas da interface.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


OUT = Path(__file__).resolve().parent / "figs"
OUT.mkdir(parents=True, exist_ok=True)

BLUE = "#0057a8"
GREEN = "#16834b"
ORANGE = "#d2691e"
RED = "#b22222"
PURPLE = "#6f42c1"
GRID = "#c7cdd4"


def configure() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.labelsize": 9,
            "axes.titlesize": 10,
            "legend.fontsize": 8,
            "axes.grid": True,
            "grid.color": GRID,
            "grid.alpha": 0.65,
            "grid.linewidth": 0.6,
            "lines.linewidth": 1.7,
            "figure.dpi": 140,
            "savefig.bbox": "tight",
        }
    )


def save(fig: plt.Figure, name: str) -> None:
    fig.savefig(OUT / f"{name}.pdf")
    fig.savefig(OUT / f"{name}.png", dpi=220)
    plt.close(fig)


def divisor_dc() -> None:
    r1, r2, rl = 1.2e3, 2.2e3, 1.0e3
    req = r2 * rl / (r2 + rl)
    vin = np.linspace(0.0, 15.0, 301)
    v_sem = vin * r2 / (r1 + r2)
    v_com = vin * req / (r1 + req)

    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.plot(vin, v_sem, color=BLUE, label=r"sem carga ($R_L=1000\,\mathrm{M\Omega}$)")
    ax.plot(vin, v_com, color=GREEN, label=r"com carga ($R_L=1\,\mathrm{k\Omega}$)")
    ax.scatter([10, 10], [v_sem[200], v_com[200]], color=[BLUE, GREEN], zorder=3)
    ax.annotate("6,471 V", (10, v_sem[200]), xytext=(10.4, 7.0), color=BLUE)
    ax.annotate("3,642 V", (10, v_com[200]), xytext=(10.4, 3.0), color=GREEN)
    ax.axvline(10, color="#666666", linewidth=0.8, linestyle="--")
    ax.set(xlabel="Tensão da fonte V1 (V)", ylabel="Tensão de saída (V)", xlim=(0, 15), ylim=(0, 10))
    ax.legend(loc="upper left")
    fig.tight_layout()
    save(fig, "divisor_dc")


def rc_bode() -> None:
    r, c = 3.9e3, 100e-9
    fc_ref = 388.0
    fc = 1.0 / (2.0 * np.pi * r * c)
    freq = np.logspace(np.log10(3.88), np.log10(38800.0), 900)
    h = 1.0 / (1.0 + 1j * 2.0 * np.pi * freq * r * c)
    mag = 20.0 * np.log10(np.abs(h))
    phase = np.angle(h, deg=True)
    checks = np.array([fc / 10.0, fc, 10.0 * fc])
    hc = 1.0 / (1.0 + 1j * checks / fc)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.2, 5.2), sharex=True)
    ax1.semilogx(freq, mag, color=BLUE, label=r"$|V_{out}/V_{in}|$")
    ax1.scatter(checks, 20 * np.log10(np.abs(hc)), color=RED, s=24, zorder=3)
    ax1.axvline(fc_ref, color=ORANGE, linestyle=":", label="referência: 388 Hz")
    ax1.axvline(fc, color=GREEN, linestyle="--", label="corte efetivo: 408,1 Hz")
    ax1.set(ylabel="Magnitude (dB)", ylim=(-45, 1))
    ax1.legend(loc="lower left", ncol=2)

    ax2.semilogx(freq, phase, color=PURPLE)
    ax2.scatter(checks, np.angle(hc, deg=True), color=RED, s=24, zorder=3)
    ax2.axvline(fc_ref, color=ORANGE, linestyle=":")
    ax2.axvline(fc, color=GREEN, linestyle="--")
    ax2.set(xlabel="Frequência (Hz)", ylabel="Fase (graus)", ylim=(-95, 5))
    fig.tight_layout()
    save(fig, "rc_bode")


def rlc_transient() -> None:
    l, c = 100e-3, 1e-9
    resistances = [4.7e3, 12e3, 22e3]
    colors = [BLUE, GREEN, ORANGE]
    t = np.linspace(0.0, 300e-6, 4000)

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    for r, color in zip(resistances, colors):
        system = signal.TransferFunction([1.0], [l * c, (r + 1e-3) * c, 1.0])
        tout, y = signal.step(system, T=t)
        ax.plot(tout * 1e6, y, color=color, label=rf"$R={r/1e3:g}\,\mathrm{{k\Omega}}$")
        peak = int(np.argmax(y))
        if y[peak] > 1.001:
            ax.scatter(tout[peak] * 1e6, y[peak], color=color, s=22, zorder=3)
    ax.axhline(1.0, color="#666666", linewidth=0.8, linestyle="--")
    ax.set(xlabel="Tempo (µs)", ylabel=r"$V_{out}$ (V)", xlim=(0, 300), ylim=(-0.04, 1.57))
    ax.legend(loc="lower right")
    fig.tight_layout()
    save(fig, "rlc_transiente")


def rlc_bode() -> None:
    l, c = 100e-3, 1e-9
    resistances = [4.7e3, 12e3, 22e3]
    colors = [BLUE, GREEN, ORANGE]
    freq = np.logspace(np.log10(159.16), np.log10(1_591_550.0), 1200)
    w = 2.0 * np.pi * freq

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.2, 5.2), sharex=True)
    for r, color in zip(resistances, colors):
        h = 1.0 / (1.0 - w**2 * l * c + 1j * w * (r + 1e-3) * c)
        label = rf"$R={r/1e3:g}\,\mathrm{{k\Omega}}$"
        ax1.semilogx(freq, 20.0 * np.log10(np.abs(h)), color=color, label=label)
        ax2.semilogx(freq, np.angle(h, deg=True), color=color)
    ax1.axhline(0, color="#666666", linewidth=0.8, linestyle="--")
    ax1.set(ylabel="Magnitude (dB)", ylim=(-85, 8))
    ax1.legend(loc="lower left", ncol=3)
    ax2.set(xlabel="Frequência (Hz)", ylabel="Fase (graus)", ylim=(-190, 10))
    fig.tight_layout()
    save(fig, "rlc_bode")


def rc_square() -> None:
    r, c = 3.9e3, 100e-9
    tau = r * c
    period, high_time = 2.5773e-3, 1.2887e-3
    dt = period / 900.0
    t = np.arange(0.0, 20.0 * period + dt, dt)
    phase = np.mod(t, period)
    vin = np.where(phase < high_time, 1.0, -1.0)
    vout = np.empty_like(vin)
    vout[0] = -1.0
    alpha = np.exp(-dt / tau)
    for idx in range(1, len(t)):
        vout[idx] = vin[idx] + (vout[idx - 1] - vin[idx]) * alpha

    mask = (t >= 5 * period) & (t <= 10 * period)
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.plot(t[mask] * 1e3, vin[mask], color=BLUE, label=r"$V_{in}$")
    ax.plot(t[mask] * 1e3, vout[mask], color=GREEN, label=r"$V_{out}$")
    ax.set(xlabel="Tempo (ms)", ylabel="Tensão (V)", ylim=(-1.2, 1.2))
    ax.legend(loc="upper right", ncol=2)
    fig.tight_layout()
    save(fig, "rc_quadrada_tempo")

    f1 = 1.0 / period
    fc = 1.0 / (2.0 * np.pi * tau)
    harmonics = np.arange(1, 16)
    vin_amp = np.where(harmonics % 2 == 1, 4.0 / (np.pi * harmonics), 0.0)
    vout_amp = vin_amp / np.sqrt(1.0 + (harmonics * f1 / fc) ** 2)

    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.stem(harmonics - 0.10, vin_amp, linefmt=BLUE, markerfmt="o", basefmt=" ", label=r"$V_{in}$")
    ax.stem(harmonics + 0.10, vout_amp, linefmt=GREEN, markerfmt="s", basefmt=" ", label=r"$V_{out}$")
    ax.set(
        xlabel="Ordem harmônica n",
        ylabel="Amplitude de pico (V)",
        xticks=harmonics,
        xlim=(0.4, 15.6),
        ylim=(0, 1.35),
    )
    ax.legend(loc="upper right")
    fig.tight_layout()
    save(fig, "rc_quadrada_espectro")


def main() -> None:
    configure()
    divisor_dc()
    rc_bode()
    rlc_transient()
    rlc_bode()
    rc_square()


if __name__ == "__main__":
    main()
