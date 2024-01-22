import sys
from RamanSpectrum_repository import RamanSpectrum
from MyException import *
from pathlib import Path


def run(img_path, output_path) -> None:
    raman_spectrum = RamanSpectrum(img_path)
    raman_spectrum.get_spectrum(output_path)
    raman_spectrum.save_spectrum(output_path)

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        raise MissingArgumentError('Missing Argument: <image path name> <output path name>')
    if not Path(f'data/img/{args[1]}').exists():
        raise MissingFileError(f'Missing File: {args[1]}')
    run(args[1], args[2])
