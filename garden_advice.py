"""Gardening advice based on the season and plant type."""


def get_season_advice(season: str) -> str:
    """Return advice for the given season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    if season == "winter":
        return "Protect your plants from frost with covers."
    return "No advice for this season."


def get_plant_advice(plant_type: str) -> str:
    """Return advice for the given plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    if plant_type == "vegetable":
        return "Keep an eye out for pests!"
    return "No advice for this type of plant."


def get_advice(season: str, plant_type: str) -> str:
    """Combine season and plant advice into one message."""
    return f"{get_season_advice(season)}\n{get_plant_advice(plant_type)}"


def main() -> None:
    """Ask the user for a season and plant type, then print advice."""
    # Normalising here so "Summer " and "summer" behave the same
    season = input("Enter the season: ").strip().lower()
    plant_type = input("Enter the plant type: ").strip().lower()
    print(get_advice(season, plant_type))


if __name__ == "__main__":
    main()