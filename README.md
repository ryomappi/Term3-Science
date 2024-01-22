
# githubからクローンする方法

以下をコマンドラインで実行してください。

```bash
git clone https://github.com/ryomappi/Term3-Science.git
```

ディレクトリ構造は以下のようになります。

```bash
raman
├──raman.py
├──RamanSpectrum_repository.py
├──RamanSpectrum.py
├──raman_spectrum.ipynb
├──baseline_and_smoothing.py
├──data
│  ├──img
│  └──csv
├──README.md
└──.gitignore
```

基本的には、raman.pyを実行するだけで、ラマンスペクトルが生成されます。\
生成されたラマンスペクトルおよび生データは、dataディレクトリに保存されます。

# ラマンスペクトルの生成

## 手順

まず、以下のライブラリがインポートできることを確認します。数が多いですね。

```python
import matplotlib.pyplot as plt
import pandas as pd
import cv2
from scipy.sparse import csc_matrix
from scipy.sparse import spdiags
import scipy.sparse.linalg as spla
import numpy as np
from scipy import signal
import csv
from pathlib import Path
import sys
```

これができたら、`raman.py`を実行します。

```bash
python raman.py <image_path> <spectrum_output_path> <denoised_output_path>
```

* ごめん、今は引数2つ目までしか使えない。

(あるいは、GUI上でrunする)

## 引数の説明

- image_path: ラマンスペクトルを生成したい画像のパス
- spectrum_output_path: ラマンスペクトルを出力したいパス
- denoised_output_path: ノイズ除去したラマンスペクトルを出力したいパス

# 備考

もし動かなかったら、raman_spectrum.ipynbの方を使ってください。
