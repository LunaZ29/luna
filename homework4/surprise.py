# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_names(targets):
    for star in targets:
        print(star)

print_star_names(targets)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_star_names_and_spectral_types(targets):
    for star in targets:
        print(f"{star}: {targets[star]['Spectral Type']}")

print_star_names_and_spectral_types(targets)
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_bright_stars(targets):
    bright_stars = []
    for star in targets:
        if targets[star]["Magnitude"] > 0.1:
            bright_stars.append(star)
    return bright_stars

print(find_bright_stars(targets))
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Proxima Centauri"] = {
    "RA": "14h 29m 42.9487s",
    "Dec": "-62° 40′ 46.141″",
    "Magnitude": 11.13,
    "Spectral Type": "M5.5Ve"
}

print(targets)
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def find_brightest_star_near_declination(targets, declination):
    closest_star = None
    closest_declination_diff = float('inf')
    brightest_magnitude = float('inf')

    for star in targets:
        star_declination = float(targets[star]["Dec"].replace("°", "").replace("′", "").replace("″", ""))
        declination_diff = abs(star_declination - declination)
        star_magnitude = targets[star]["Magnitude"]

        if declination_diff < closest_declination_diff or (declination_diff == closest_declination_diff and star_magnitude < brightest_magnitude):
            closest_star = star
            closest_declination_diff = declination_diff
            brightest_magnitude = star_magnitude

    return closest_star

# 6) What is your favorite constellation?
# I like Orion because it is easily recognizable and it has Betelgeuse. 