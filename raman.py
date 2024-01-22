import sys
from RamanSpectrum_repository import RamanSpectrum
from MyException import *
from pathlib import Path


def run(img_path, spectrum_output_path, denoised_output_path) -> None:
    raman_spectrum = RamanSpectrum(img_path)
    raman_spectrum.get_spectrum(spectrum_output_path)
    raman_spectrum.save_spectrum(spectrum_output_path)
    raman_spectrum.outFigCSV(denoised_output_path)

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        raise MissingArgumentError('Missing Argument: <image_path> <spectrum_output_path> <denoised_output_path>')
    if not Path(f'data/img/{args[1]}').exists():
        raise MissingFileError(f'Missing File: {args[1]}')
    run(args[1], args[2], args[3])
