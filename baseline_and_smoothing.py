# 以下のコードは次のサイトを参考にしている
# https://qiita.com/lcmtk/items/06bdd965d8a79bbfd0a9

import csv
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.sparse import csc_matrix
from scipy.sparse import spdiags
import scipy.sparse.linalg as spla

# パラメタを入力します、うまく推定ができないときはここをいじってください
# AsLSでのベースライン推定は ( W(p) + lam*D'D )z = Wy のとき、重み p と罰則項の係数 lam がパラメタです
# Savitzky-Golyでは、測定値をいくつに分割するかを dn で設定し（窓の数は len(Y)/dn になります)、
# 多項式次数を poly で設定します
# paramAsLS = [ lam , p ]
# paramSG   = [ dn , poly ]
paramAsLS = [10**3.5, 0.00005]
paramSG = [80, 5]

# 以下のファイルを読み込みます (ファイル名は適宜変更してください)
filename = 'data/csv/spectrum_2.csv'  # あとで標準入力できるようにする


# 測定データ(csv)を開きます
X = []
Y = []
with open(filename, 'r') as f:
    header = next(csv.reader(f))
    reader = csv.reader(f)
    data = [row for row in reader]
    for i in range(len(data)):
        X.append(float(data[i][1]))
        Y.append(float(data[i][2]))


# AsLSによりベースライン推定を行います
def baseline_als(y, lam, p, niter=10):
    # https://stackoverflow.com/questions/29156532/python-baseline-correction-library
    # p: 0.001 - 0.1, lam: 10^2 - 10^9
    # Baseline correction with asymmetric least squares smoothing,
    # P. Eilers, 2005
    L = len(y)
    D = csc_matrix(np.diff(np.eye(L), 2))
    w = np.ones(L)
    for i in range(niter):
        W = spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spla.spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)
    return z


# Savitzky-Golyによりノイズ除去を行います
def SGs(y, dn, poly):
    # y as np.array, dn as int, poly as int
    n = len(y) // dn
    if n % 2 == 0:
        N = n+1
    elif n % 2 == 1:
        N = n
    else:
        print("window length can't set as odd")
    SGsmoothed = signal.savgol_filter(y, window_length=N, polyorder=poly)
    return SGsmoothed


# csvファイルと図を出力します
def outFigCSV(X, Y, paramAsLS, paramSG):

    # baseline estimation and smoothing
    Y_np = np.array(Y)
    # baseline estimation
    bkg = baseline_als(Y_np, paramAsLS[0], paramAsLS[1])
    fix = Y_np - bkg  # remove baseline
    # smoothing
    smth = SGs(fix, paramSG[0], paramSG[1])

    # csv output
    dataOutput = np.c_[X, Y, bkg, smth]
    np.savetxt('data/csv/processed_2.csv', dataOutput, delimiter=',')

    # figures
    plt.figure(figsize=(12, 9))
    ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
    ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=2)

    ax1.plot(X, Y, linewidth=2)
    ax1.plot(X, bkg, "b", linewidth=1, linestyle="dashed", label="baseline")

    ax2.plot(
        X, fix, "g",
        linewidth=1, linestyle="dashed", label="remove baseline"
    )
    ax2.plot(X, smth, "b", linewidth=2, label="smoothed")

    plt.axis("tight")
    plt.show()


# 実行する
outFigCSV(X, Y, paramAsLS, paramSG)
