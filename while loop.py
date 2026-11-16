
print("==============================================")
print("          PHYSICS FORMULA SOLVER")
print("==============================================")
print("Welcome to the Physics Formula Solver System!")

# Function 1: Calculate Speed
def calculate_speed():
    print("\n--- SPEED CALCULATION ---")

    distance = get_number("Enter distance (m): ")
    time = get_number("Enter time (s): ")

    if time == 0:
        print("Error! Time cannot be zero.")
    else:
        speed = distance / time
        print("Calculated Speed =", round(speed, 2), "m/s")


# Function 2: Calculate Force
def calculate_force():
    print("\n--- FORCE CALCULATION ---")

    mass = get_number("Enter mass (kg): ")
    acceleration = get_number("Enter acceleration (m/s²): ")

    force = mass * acceleration
    print("Calculated Force =", round(force, 2), "N")


# Function 3: Calculate Density
def calculate_density():
    print("\n--- DENSITY CALCULATION ---")

    mass = get_number("Enter mass (kg): ")
    volume = get_number("Enter volume (m³): ")

    if volume == 0:
        print("Error! Volume cannot be zero.")
    else:
        density = mass / volume
        print("Calculated Density =", round(density, 2), "kg/m³")


# Function 4: Calculate Work Done
def calculate_work():
    print("\n--- WORK DONE CALCULATION ---")

    force = get_number("Enter force (N): ")
    distance = get_number("Enter distance (m): ")

    work = force * distance
    print("Calculated Work Done =", round(work, 2), "J")


# Function 5: Calculate Pressure
def calculate_pressure():
    print("\n--- PRESSURE CALCULATION ---")

    force = get_number("Enter force (N): ")
    area = get_number("Enter area (m²): ")

    if area == 0:
        print("Error! Area cannot be zero.")
    else:
        pressure = force / area
        print("Calculated Pressure =", round(pressure, 2), "Pa")


# Main Program
while True:

    print("\n==============================================")
    print("             MAIN MENU")
    print("==============================================")
    print("1. Calculate Speed")
    print("2. Calculate Force")
    print("3. Calculate Density")
    print("4. Calculate Work Done")
    print("5. Calculate Pressure")
    print("6. Exit Program")
    print("==============================================")

    choice = input("Select an operation (1-6): ")

    if choice == "1":
        calculate_speed()

    elif choice == "2":
        calculate_force()

    elif choice == "3":
        calculate_density()

    elif choice == "4":
        calculate_work()

    elif choice == "5":
        calculate_pressure()

    elif choice == "6":
        print("\nThank you for using the Physics Formula Solver!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid selection! Please choose between 1 and 6.")
        continue

    # Ask user whether to continue
    while True:
        answer = input(
            "\nWould you like to perform another calculation? (Yes/No): "
        ).strip().lower()

        if answer == "yes":
            break

        elif answer == "no":
            print("\nThank you for using the Physics Formula Solver!")
            print("Goodbye!")
            exit()

        else:
            print("Invalid response! Please enter Yes or No.")
