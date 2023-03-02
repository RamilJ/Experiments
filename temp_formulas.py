def celc_to_kel(celcius):
    kelvin = celcius + 273.15
    return kelvin

def celc_to_fahr(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def kel_to_celc(kelvin):
    celcius = kelvin - 273.15
    return celcius

def kel_to_fahr(kelvin):
    fahrenheit = ((kelvin - 273.15) * 9/5) + 32
    return fahrenheit

def fahr_to_celc(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

def fahr_to_kel(fahrenheit):
    kelvin = ((fahrenheit - 32) * 5/9) + 273.15
    return kelvin