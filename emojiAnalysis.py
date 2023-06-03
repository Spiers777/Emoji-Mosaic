import requests,re,json,cv2,time
import numpy as np
from pilmoji import Pilmoji
from PIL import Image, ImageFont

def getAvgEmojiCol(emoji):
    my_string = emoji
    with Image.new('RGBA', (43, 43), (255, 255, 255, 0)) as image:
        font = ImageFont.truetype('arial.ttf', 24)
        if font.getsize(emoji)[0] == font.getsize("🔣")[0]:
            with Pilmoji(image) as pilmoji:
                pilmoji.text((10, 10), my_string.strip(), (0, 0, 0), font)

            image = image.crop((9, 9, 35, 35))
            image.save("emoji.png")
            img = cv2.imread('emoji.png')
            avg_color_per_row = np.average(img, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            return avg_color.tolist()
        else:
            return ""

with open('emoji-list.json', 'r', encoding="utf8") as f:
    emojiList = json.load(f)
    colList = {}
    for i in emojiList:
        start = time.time()
        color = getAvgEmojiCol(i)
        if color != "":
            colList[i] = {"emoji":i,"col":getAvgEmojiCol(i)}
            end = time.time()
            print(f"{i} calculated in {end-start}s")
        else:
            print(f"{i} could not be calculated")
    with open('data.json', 'w') as fp:
        json.dump(colList, fp)