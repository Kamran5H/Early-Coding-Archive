"""Boiling Point Linear Regression Model — Early Coding Archive."""
from __future__ import annotations

# Reference dataset: (Molecular Weight g/mol, Boiling Point C)
DATASET = [
    (18.0, 100.0),   # water
    (46.0, 78.0),    # ethanol
    (16.0, -161.0),  # methane
    (78.0, 80.0),    # benzene
    (58.0, 56.0),    # acetone
]


def fit_ordinary_least_squares(data=DATASET) -> tuple[float, float]:
    """Fit y = slope * x + intercept using closed-form ordinary least squares."""
    n = len(data)
    mean_x = sum(x for x, _ in data) / n
    mean_y = sum(y for _, y in data) / n
    num = sum((x - mean_x) * (y - mean_y) for x, y in data)
    den = sum((x - mean_x) ** 2 for x, _ in data)
    slope = num / den
    intercept = mean_y - slope * mean_x
    return slope, intercept


def predict_boiling_point(mw: float) -> float:
    slope, intercept = fit_ordinary_least_squares()
    return round(slope * mw + intercept, 2)


if __name__ == "__main__":
    bp = predict_boiling_point(60.0)
    print(f"Predicted boiling point for MW=60 (1-propanol): {bp:.2f} °C")
