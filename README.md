
# githubからクローンする方法

以下をコマンドラインで実行してください。

```bash
git clone https://github.com/ryomappi/Term3-Science.git
```

# ラマンスペクトルの生成

# 手順

まず、以下のライブラリがインポートできることを確認します。

```python
import matplotlib.pyplot as plt
import pandas as pd
import cv2
```

これができたら、`raman.py`を実行します。

```bash
python raman.py
```

(あるいは、GUI上でrunする)

すると、`spectrun_1.png`と`spectrum_1.csv`が生成されます。

# 備考

もし動かなかったら、raman_spectrum.ipynbの方を使ってください。