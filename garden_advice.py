"""Gardening advice based on the season and plant type."""

SEASONAL_PLANTS: dict[str, list[str]] = {
    "spring": ["tulips", "peas", "lettuce"],
    "summer": ["sunflowers", "tomatoes", "basil"],
    "autumn": ["pansies", "garlic", "kale"],
    "winter": ["hellebores", "winter cabbage", "holly"],
}


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


def get_plant_recommendations(season: str) -> str:
    """Return a sentence recommending plants for the given season."""
    plants = SEASONAL_PLANTS.get(season)
    if plants is None:
        return "No plant recommendations for this season."
    return f"Plants that thrive in {season}: {', '.join(plants)}."


def get_advice(season: str, plant_type: str) -> str:
    """Combine season advice, plant advice and recommendations."""
    return "\n".join(
        [
            get_season_advice(season),
            get_plant_advice(plant_type),
            get_plant_recommendations(season),
        ]
    )


def main() -> None:
    """Ask the user for a season and plant type, then print advice."""
    season = input("Enter the season: ").strip().lower()
    plant_type = input("Enter the plant type: ").strip().lower()
    print(get_advice(season, plant_type))


if __name__ == "__main__":
    main()