from __future__ import annotations

from typing import Dict


PALETTE: Dict[str, str] = {
    "primary": "#2563eb",
    "secondary": "#16a34a",
    "accent": "#f59e0b",
    "muted": "#64748b",
    "danger": "#dc2626",
}


def apply_theme() -> None:
    import matplotlib as mpl
    import seaborn as sns  # type: ignore

    sns.set_theme(context="notebook", style="whitegrid")

    mpl.rcParams.update(
        {
            "figure.figsize": (8.0, 5.0),
            "figure.dpi": 110,
            "axes.titlesize": 13,
            "axes.labelsize": 11,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "axes.prop_cycle": mpl.cycler(color=[
                PALETTE["primary"],
                PALETTE["secondary"],
                PALETTE["accent"],
                "#7c3aed",
                "#059669",
                "#ea580c",
            ]),
        }
    )


