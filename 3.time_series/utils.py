"""
Génération de séries temporelles NON stationnaires
Objectif pédagogique : les étudiants doivent les restationnariser
"""

import numpy as np
import pandas as pd


# --------------------------------------------------
# Utilitaire : index temporel
# --------------------------------------------------
def _time_index(n=200, start="2000-01-01", freq="ME"):
    return pd.date_range(start=start, periods=n, freq=freq)


# --------------------------------------------------
# 1. Série I(1) : Random walk + bruit
# --------------------------------------------------
def ts_nonstationary_I1(n=200, seed=42, noise_std=0.3):
    np.random.seed(seed)

    e = np.random.normal(size=n)
    noise = np.random.normal(scale=noise_std, size=n)

    y = np.cumsum(e) + noise

    return pd.DataFrame({"y": y}, index=_time_index(n))


# --------------------------------------------------
# 2. Série I(2) : Double random walk + bruit
# --------------------------------------------------
def ts_nonstationary_I2(n=200, seed=42, noise_std=0.3):
    np.random.seed(seed)

    e = np.random.normal(size=n)
    noise = np.random.normal(scale=noise_std, size=n)

    y = np.cumsum(np.cumsum(e)) + noise

    return pd.DataFrame({"y": y}, index=_time_index(n))


# --------------------------------------------------
# 3. Racine unitaire saisonnière + bruit
# --------------------------------------------------
def ts_nonstationary_seasonal(
    n=240,
    seasonal_period=12,
    seed=42,
    noise_std=0.2
):
    np.random.seed(seed)

    e = np.random.normal(size=n)
    noise = np.random.normal(scale=noise_std, size=n)

    y = np.zeros(n)

    for t in range(seasonal_period, n):
        y[t] = y[t - seasonal_period] + e[t]

    y += noise

    return pd.DataFrame({"y": y}, index=_time_index(n))


# --------------------------------------------------
# 4. Variance non constante (log / Box-Cox requis)
# --------------------------------------------------
def ts_nonstationary_heteroskedastic(
    n=200,
    seed=42,
    noise_std=0.1
):
    np.random.seed(seed)

    t = np.arange(n)
    e = np.random.normal(scale=noise_std, size=n)

    # tendance exponentielle + bruit multiplicatif
    y = np.exp(0.02 * t) * (1 + e)

    return pd.DataFrame({"y": y}, index=_time_index(n))


def ts_for_students(random_seed):
    # génère 5 séries d'un peu de tout 

    possibilities = [ts_nonstationary_I1,
                     ts_nonstationary_I2,
                     ts_nonstationary_seasonal,
                        ts_nonstationary_heteroskedastic]
    
    choices = np.random.choice(possibilities, size=5, replace=True)
    print(choices)
    ts_list = [choice(seed=random_seed + i) for i, choice in enumerate(choices)]

    return ts_list
    