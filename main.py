import json, cv2
from math import sqrt
import random

def getEmoji(target):
    with open('data.json', 'r') as fp:
        data = json.load(fp)
        r,g,b = target[0],target[1],target[2]
        proximities = []
        for i in data:
            cr,cg,cb = round(data[i]["col"][0]-90 ),round(data[i]["col"][1]-90),round(data[i]["col"][2]-90) #Negative values adjust the dominance of colour, Lower value = less of the colour
            proximity = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
            proximities.append({"emoji":data[i]["emoji"],"proximity":proximity})
        proximities.sort(key=lambda x: x["proximity"])
        return proximities[random.randint(1,3)]["emoji"]
    
img = cv2.imread("input.png")
sampleSize = 10
height, width = int(img.shape[0]//sampleSize), int(img.shape[1]//sampleSize) #Round down to nearest multiple of sample size
row, rows = []*width, []*height #Preallocate list for speed
for y in range(height):
    print(f'Row {y:02}/{height} [{"█"*y}{" "*(height-y)}]')
    for x in range(width):
        row.append(getEmoji(img[y*sampleSize,x*sampleSize].tolist()))
    rows.append("".join(row))
    row = []*width
print("\n".join(rows))