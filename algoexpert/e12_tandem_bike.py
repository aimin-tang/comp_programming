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
