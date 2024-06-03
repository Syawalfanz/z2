def calculate_price(length, width, height, weight):
    volume = length * width * height
    
    if weight <= 1:
        if volume <= 5000:
            return volume, 3
        elif volume <= 10000:
            return volume, 5
        else:
            return volume, 7
    elif weight <= 5:
        if volume <= 5000:
            return volume, 5
        elif volume <= 10000:
            return volume, 7
        else:
            return volume, 9
    else:
        if volume <= 5000:
            return volume, 7
        elif volume <= 10000:
            return volume, 9
        else:
            return volume, 11
