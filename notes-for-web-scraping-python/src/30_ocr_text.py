#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
    image = image.point(lambda x: 0 if x < 143 else 255)
    iamge.save(newFilePath)

    subprocess.call(["tesseract", newFilePath, "output"])

    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close


if __name__ == '__main__':
    from PIL import ImageFilter

    kitten = Image.open("kitten.jpg")
    blurryKitten = kitten.filter(ImageFilter.GuassianBlur)
    blurryKitten.save("kitten_blurred.jpg")
    blurryKitten.show()
    cleanFile("kitten_blurred.jpg", "kitten_blurred_clean.jpg")
