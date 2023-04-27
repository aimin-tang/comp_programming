def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.

    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.reverse()

    result = 0
    for i in range(len(redShirtSpeeds)):
        result += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return result

reds = [5, 5, 3, 9, 2]
blues = [3, 6, 7, 2, 1]
fastest = True
print(tandemBicycle(reds, blues, fastest))
# 32