
def main():
    # input weight
    weight_on_earth_str = input("Enter weight on Earth: ")

    # ask for planet
    planet = input("Enter a planet: ")

    # type casting
    weight_on_earth = float(weight_on_earth_str)

    # calculate the weight on the desired planet

# global variables

# local variables
    multiple = 0

    if planet == "Mercury":
        # scope of if statement:             
        multiple = 0.376
        
    elif planet == "Venus":
        multiple = 0.889
    elif planet == "Mars":
        multiple = 0.368
    elif planet == "Jupiter":
        multiple = 2.36
    elif planet == "Saturn":
        multiple = 1.081
    elif planet == "Uranus":
        multiple = 0.815
    else:
        multiple = 1.140

    # calculate the weight on the given planet

    weight_on_planet = weight_on_earth * multiple

    # round up the value

    weight_on_planet = round(weight_on_planet,2)


    print(f"The equivalent weight on {planet}: {weight_on_planet}")


if __name__ == "__main__":
    main()