from RamanSpectrum_repository import RamanSpectrum


def run() -> None:
    img_path = 'data/img/IMG_8647.jpeg'
    raman_spectrum = RamanSpectrum(img_path)
    raman_spectrum.get_spectrum('spectrum_1')
    raman_spectrum.save_spectrum('spectrum_1')
