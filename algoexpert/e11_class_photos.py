def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] < blueShirtHeights[0]:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
        return True
    elif redShirtHeights[0] > blueShirtHeights[0]:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
        return True
    else:
        return False

reds = [5, 8, 1, 3, 4]
blues = [6, 9, 2, 4, 5]

print(classPhotos(reds, blues))
# True