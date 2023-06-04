import json, cv2, sys
from math import sqrt

def getEmoji(target):
    with open(f'{sys.path[0]}/colourAnalysis/data.json', 'r') as fp:
        data = json.load(fp)
        r,g,b = target[0],target[1],target[2]
        proximities = []
        for i in data:
            cr,cg,cb = round(data[i]["col"][0]-90 ),round(data[i]["col"][1]-90),round(data[i]["col"][2]-90) #Negative values adjust the dominance of colour, Lower value = less of the colour
            proximity = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
            proximities.append({"emoji":data[i]["emoji"],"proximity":proximity})
        proximities.sort(key=lambda x: x["proximity"])
        return proximities[0]["emoji"]

def generateMosaic(input, sampleSize):
    srcimg = cv2.imread(input)
    aspect = srcimg.shape[1]/srcimg.shape[0]
    width, height = 750, int(750/aspect)
    print(width,height)
    img = cv2.resize(srcimg, (width,height))
    height, width = int(img.shape[0]//sampleSize), int(img.shape[1]//sampleSize) #Round down to nearest multiple of sample size
    row, rows = []*width, []*height #Preallocate list for speed
    for y in range(height):
        print(f"{y}/{height}")
        for x in range(width):
            row.append(getEmoji(img[y*sampleSize,x*sampleSize].tolist()))
        rows.append("".join(row))
        row = []*width
    print("\n".join(rows))
    return rows