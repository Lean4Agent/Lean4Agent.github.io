"""Render Lean4Agent Table 1 scores; requires matplotlib.

Source: https://arxiv.org/abs/2606.06523v2, Table 1.
All values are reported percentages on benchmark subsets. No derived means
or difference columns are used because the paper contains inconsistencies there.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


MODELS = ["GPT-5.2", "GLM-5", "Kimi-K2.5", "Gemma-4-31B", "Qwen-3.5-27B"]
PANELS = [
    ("SWE-Bench-Verified", "50 hard problems",
     [50.00, 50.67, 46.00, 32.67, 38.00],
     [62.67, 58.00, 61.33, 60.00, 49.33]),
    ("ELAIP-Bench", "100 questions",
     [20.33, 25.00, 28.33, 27.33, 36.67],
     [32.00, 37.33, 36.00, 35.67, 42.00]),
]


def main():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 12,
        "text.color": "#414b57", "axes.labelcolor": "#414b57",
        "xtick.color": "#414b57", "ytick.color": "#626976",
        "svg.fonttype": "none", "svg.hashsalt": "lean4agent-results",
    })
    fig, axes = plt.subplots(1, 2, figsize=(18, 6.9), dpi=100, sharey=True)
    width = .34
    for ax, (title, subset, failing, passing) in zip(axes, PANELS):
        x = list(range(len(MODELS)))
        left = ax.bar([i - width / 2 for i in x], failing, width,
                      color="#a8bfd4", label="Verification-failing workflows")
        right = ax.bar([i + width / 2 for i in x], passing, width,
                       color="#548235", label="Verification-passing workflows")
        for bars in [left, right]:
            ax.bar_label(bars, labels=[f"{bar.get_height():.2f}" for bar in bars],
                         padding=5, fontsize=10.5, color="#414b57")
        ax.set_title(f"{title}\n{subset}", fontsize=15, fontweight="semibold", pad=24)
        ax.set_xticks(x)
        ax.set_xticklabels(MODELS, rotation=15, ha="right", rotation_mode="anchor")
        ax.set_ylim(0, 80)
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
        ax.set_axisbelow(True)
        ax.grid(axis="y", color="#e5e8eb", linewidth=.8)
        ax.tick_params(axis="both", length=0, pad=8)
        for edge in ["top", "right", "left"]:
            ax.spines[edge].set_visible(False)
        ax.spines["bottom"].set_color("#d7dde3")
    axes[0].set_ylabel("Success rate", labelpad=12)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(.5, .985),
               ncol=2, frameon=False, fontsize=13, columnspacing=3)
    fig.text(.5, .035,
             "Mean success rates across three verification-passing or three verification-failing workflows per model.",
             ha="center", fontsize=11, color="#626976")
    fig.subplots_adjust(left=.065, right=.985, top=.78, bottom=.22, wspace=.16)
    destination = Path(__file__).resolve().parents[1] / "static/images/lean4agent"
    destination.mkdir(parents=True, exist_ok=True)
    fig.savefig(destination / "MainResults.svg", metadata={
        "Date": None, "Title": "Lean4Agent main results",
        "Description": "Reported per-model values from Table 1, arXiv:2606.06523v2.",
    })
    fig.savefig(destination / "MainResults.png", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
