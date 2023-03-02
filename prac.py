# imports the formula module
import temp_formulas as tf

# prompt the user for the temperature and the input and output units
temperature = input("Enter the temperature value with unit: ").upper()

# convert the temperature
match temperature:
    # check if C is present in the input
    case A if 'C' in A:
        print("1. Convert C to F")
        print("2. Convert C to K")
        number = input("Select number: ")
        # select the conversion for the temperature
        match number:
            # C to F
            case "1":
                temp = float(temperature[:-1])
                converted_temp = tf.celc_to_fahr(temp)
                print("The %.2fC is equivalent to %.2fF" %(temp, converted_temp))
            # C to K
            case "2":
                temp = float(temperature[:-1])
                converted_temp = tf.celc_to_kel(temp)
                print("The %.2fC is equivalent to %.2fK" %(temp, converted_temp))
    # check if F is present in the input
    case B if 'F' in B:
        print("1. Convert F to C")
        print("2. Convert F to K")
        number = input("Select number: ")
        # select the conversion for the temperature
        match number:
            # F to C
            case "1":
                temp = float(temperature[:-1])
                converted_temp = tf.fahr_to_celc(temp)
                print("The %.2fF is equivalent to %.2fC" %(temp, converted_temp))
            # F to K
            case "2":
                temp = float(temperature[:-1])
                converted_temp = tf.fahr_to_kel(temp)
                print("The %.2fF is equivalent to %.2fK" %(temp, converted_temp))
    # check if K is present in the input
    case C if 'K' in C:
        print("1. Convert K to C")
        print("2. Convert K to F")
        number = input("Select number: ")
        # select the conversion for the temperature
        match number:
            # K to C
            case "1":
                temp = float(temperature[:-1])
                converted_temp = tf.kel_to_celc(temp)
                print("The %.2fK is equivalent to %.2fC" %(temp, converted_temp))
            # K to F
            case "2":
                temp = float(temperature[:-1])
                converted_temp = tf.kel_to_fahr(temp)
                print("The %.2fK is equivalent to %.2fF" %(temp, converted_temp))
    # for error checking
    case _:
        print("Invalid Input")
