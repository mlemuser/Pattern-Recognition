from typing import List
import pandas as pd
import cv2
import csv


def getImages(paths: List) -> List:
    images = []

    for path in paths:
        images.append(cv2.imread(path))

    return images


def getTrainingData(images_zones: List, original_image) -> List[List[int]]:
    width, height, _ = original_image.shape
    training_data = []

    for image_index, image in enumerate(images_zones):
        for x in range(int(width*0.1), int(width*0.9)):
            for y in range(height):
                if int(image[x, y][0]) * int(original_image[x, y][0]) == 0:
                    (b, g, r) = original_image[x, y]
                    training_data.append([b, g, r, image_index + 1])

    return training_data


def writeInCsv(filename: str, headers: List[str], data: List) -> None:
    with open(filename, 'w', encoding='UTF-8', newline='') as data_file:
        writer = csv.writer(data_file)

        writer.writerow(headers)
        writer.writerows(data)


def adapterTrainingData(filename: str) -> List[List[int]]:
    fullData = pd.read_csv(filename)
    patterns = fullData[['b', 'g', 'r']]
    classes = fullData["clase"]

    return [patterns, classes]


def doAll() -> List[List]:
    images = getImages(
        ["../image/cielo.png", "../image/boscosa.png", "../image/suelo.png"])
    training_data = getTrainingData(
        images, cv2.imread("../image/3-regiones.png"))
    # clase1 = [data for data in training_data if data[2] == 1]
    filename = 'data.csv'

    writeInCsv(filename, ['b', 'g', 'r', "clase"], training_data)
    data_adapted = adapterTrainingData(filename)

    return data_adapted