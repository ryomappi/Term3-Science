import sys
from RamanSpectrum_repository import RamanSpectrum
from pathlib import Path
import os


def run(img_path, spectrum_output_path) -> None:
    raman_spectrum = RamanSpectrum(img_path)
    raman_spectrum.get_spectrum(spectrum_output_path)
    raman_spectrum.save_spectrum(spectrum_output_path)
    # raman_spectrum.outFigCSV(denoised_output_path)

if __name__ == '__main__':
    args = sys.argv
    # 例外処理
    # if len(args) != 4:
    #     print('Missing Argument: require 3 arguments')
    #     raise SyntaxError
    # print(args[1])
    # if not Path(f'data/img/{args[1]}').exists():
    #     raise FileNotFoundError
    # 実行
    run(args[1], args[2])
