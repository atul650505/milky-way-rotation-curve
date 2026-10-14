# ---------------------------------------------------------------------
#  make_sample_spectrum.py
#
#  Produces the placeholder figure sample_spectrum.pdf used in main.tex.
#  The spectrum is synthetic: a few emission components along one model
#  sightline, cut off by an edge at v_term and blurred by a Gaussian of
#  dispersion sigma. It is here to show the edge criterion, and to give
#  you a plotting style to match. Replace it with your own HI4PI
#  spectrum before you hand anything in.
#
#      python3 make_sample_spectrum.py
# ---------------------------------------------------------------------

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import erfc

# --- plotting style: serif text, to sit next to the LaTeX body ---------
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Nimbus Roman No9 L", "Times New Roman", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 11,
    "axes.linewidth": 0.8,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,
})

# --- the model spectrum -----------------------------------------------
V_TERM = 140.0      # true terminal velocity, km/s
SIGMA = 9.0         # turbulent + thermal dispersion, km/s
T_THR = 10.0        # brightness threshold defining the edge, K

v = np.linspace(-30.0, 185.0, 4000)


def gauss(x, amp, mu, sig):
    return amp * np.exp(-0.5 * ((x - mu) / sig) ** 2)


# emission from clouds at several distances along the sightline
emissivity = (gauss(v, 50.0, 8.0, 14.0)
              + gauss(v, 32.0, 40.0, 13.0)
              + gauss(v, 105.0, 118.0, 28.0))

# the tangent point cuts the emission off; blurring makes it a ramp
spectrum = emissivity * 0.5 * erfc((v - V_TERM) / (np.sqrt(2.0) * SIGMA))

# T_edge is the brightness just inside the edge; at v = v_term the erfc
# factor is one half, so the true terminal velocity sits at T_edge/2
t_edge = float(np.interp(V_TERM, v, emissivity))
t_half = 0.5 * t_edge
falling = v > 125.0
v_measured = float(np.interp(-T_THR, -spectrum[falling], v[falling]))

# --- the figure --------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.0, 4.3))

ax.plot(v, spectrum, color="k", lw=1.6)
ax.axhline(T_THR, color="k", ls="--", lw=1.0)
ax.axhline(t_edge, color="0.45", ls=":", lw=1.0)

ax.plot([v_measured], [T_THR], "o", color="k", ms=6, zorder=5)
ax.plot([V_TERM], [t_half], "s", mfc="none", mec="k", ms=7, mew=1.2, zorder=5)

ax.text(-27, T_THR + 3.5, r"threshold $T_{\rm thr}=10$ K", fontsize=10)
ax.text(150, t_edge + 3.0, r"$T_{\rm edge}$", fontsize=10, color="0.35")

ax.annotate(r"$v_{\rm measured}$",
            xy=(v_measured, T_THR), xytext=(152, 33),
            fontsize=10, ha="left",
            arrowprops=dict(arrowstyle="-", lw=0.8, color="k"))
ax.annotate(r"true $v_{\rm term}$ at $T_{\rm edge}/2$",
            xy=(V_TERM, t_half), xytext=(63, 26),
            fontsize=10, ha="left",
            arrowprops=dict(arrowstyle="-", lw=0.8, color="k"))
ax.annotate("nearer gas: peak height measures how much\n"
            "gas there is, not how fast it moves",
            xy=(46, 36), xytext=(-24, 62), fontsize=9.5,
            arrowprops=dict(arrowstyle="-", lw=0.8, color="0.45"))

ax.set_xlabel(r"radial velocity $v_{\rm LSR}$ (km s$^{-1}$)")
ax.set_ylabel(r"brightness temperature $T_B$ (K)")
ax.set_xlim(-30, 185)
ax.set_ylim(0, 108)

fig.tight_layout()
fig.savefig("sample_spectrum.pdf")
fig.savefig("sample_spectrum.png", dpi=300)
print("v_measured = %.1f km/s, v_term = %.1f km/s, bias = +%.1f km/s"
      % (v_measured, V_TERM, v_measured - V_TERM))
