import matplotlib.pyplot as plt
import pandas as pd
import cv2


class RamanSpectrum:
    def __init__(self, img_path):
        self.img_path = img_path

    def read_img(self):
        return cv2.imread(self.img_path, cv2.IMREAD_GRAYSCALE)

    def pixel_to_wavenumber(self, pixel):
        # kaiserの式のマジックナンバーたちは、設計に基づいた数値であることに注意
        kaiser = 1.87970*10**4 - 10**7/(532 + (633 - 532)/1440 * pixel)
        return kaiser

    def get_raman_intensity(self):
        img = self.read_img()
        height, width = img.shape[:2]
        raman_intensity = []
        for x in range(width):
            sum_intensity = 0
            for y in range(height):
                intensity_of_pixel = img[y, x]
                sum_intensity += intensity_of_pixel
            raman_intensity.append(sum_intensity/height)
        return raman_intensity

    def get_raman_wavenumber(self):
        img = self.read_img()
        height, width = img.shape[:2]
        raman_wavenumber = []
        for x in range(width):
            raman_wavenumber.append(self.pixel_to_wavenumber(x))
        return raman_wavenumber

    def get_spectrum(self, file_name):
        raman_intensity = self.get_raman_intensity()
        raman_wavenumber = self.get_raman_wavenumber()
        plt.xlabel('Wavenumber (cm-1)')
        plt.ylabel('Raman Intensity')
        plt.plot(raman_wavenumber, raman_intensity)
        plt.savefig(f'data/img/{file_name}.png')

    def save_spectrum(self, file_name):
        df = pd.DataFrame({
            'Wavenumber': self.get_raman_wavenumber(),
            'Intensity': self.get_raman_intensity()
        })
        df.to_csv(f'data/csv/{file_name}.csv')
