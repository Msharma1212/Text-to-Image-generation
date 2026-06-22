from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Dict, List

from flask import Flask, render_template, request


app = Flask(__name__)


@dataclass(frozen=True)
class Destination:
    country: str
    vibe: str
    weather: str
    daily_costs: Dict[str, int]
    highlights: List[str]
    foods: List[str]
    indoors: List[str]
    outdoors: List[str]
    packing: List[str]


DESTINATIONS: Dict[str, Destination] = {
    "goa": Destination(
        country="India",
        vibe="Beach escape with nightlife and laid-back cafes",
        weather="Warm, humid, and usually sunny. Light clothes work best.",
        daily_costs={"budget": 2800, "medium": 5000, "luxury": 9500},
        highlights=["Baga Beach", "Fontainhas", "Dudhsagar Falls", "Anjuna Flea Market", "Chapora Fort"],
        foods=["Goan fish curry", "bebinca", "prawn balchao"],
        indoors=["Museum of Goa", "Latin Quarter cafe trail", "Goan cooking class"],
        outdoors=["Beach hopping", "sunset cruise", "water sports"],
        packing=["sunscreen", "flip-flops", "swimwear", "light cotton clothes"],
    ),
    "manali": Destination(
        country="India",
        vibe="Mountain retreat with adventure, views, and cozy cafes",
        weather="Cool to cold depending on season. Evenings can be chilly.",
        daily_costs={"budget": 2500, "medium": 4800, "luxury": 8500},
        highlights=["Solang Valley", "Old Manali", "Hadimba Temple", "Jogini Falls", "Atal Tunnel"],
        foods=["siddu", "trout", "local cafe platters"],
        indoors=["Tibetan monastery visit", "cafe day", "local handicraft shopping"],
        outdoors=["Paragliding", "waterfall trek", "scenic drives"],
        packing=["jacket", "walking shoes", "thermals", "power bank"],
    ),
    "dubai": Destination(
        country="UAE",
        vibe="Modern luxury, shopping, skyline views, and desert experiences",
        weather="Hot for much of the year. Stay hydrated and plan around midday heat.",
        daily_costs={"budget": 6500, "medium": 11000, "luxury": 22000},
        highlights=["Burj Khalifa", "Dubai Mall", "Dubai Marina", "Desert Safari", "Al Fahidi"],
        foods=["shawarma", "luqaimat", "mixed grill platters"],
        indoors=["Museum of the Future", "Dubai Mall aquarium", "mall-based entertainment"],
        outdoors=["Desert safari", "marina walk", "beach evening"],
        packing=["breathable clothes", "sunglasses", "refillable bottle", "smart casual outfit"],
    ),
    "paris": Destination(
        country="France",
        vibe="Classic city break with art, cafes, and romantic streets",
        weather="Mild but changeable. Layers are useful year-round.",
        daily_costs={"budget": 9000, "medium": 15000, "luxury": 30000},
        highlights=["Eiffel Tower", "Louvre Museum", "Montmartre", "Seine cruise", "Notre-Dame area"],
        foods=["croissants", "crepes", "French onion soup"],
        indoors=["Museum day", "pastry workshop", "covered passages walk"],
        outdoors=["River cruise", "park picnic", "sunset viewpoint"],
        packing=["comfortable shoes", "light jacket", "crossbody bag", "travel adapter"],
    ),
    "tokyo": Destination(
        country="Japan",
        vibe="Fast-paced city with food, tech, tradition, and efficient travel",
        weather="Seasonal swings are noticeable, but walking is part of every plan.",
        daily_costs={"budget": 8500, "medium": 14500, "luxury": 28000},
        highlights=["Shibuya", "Asakusa", "Tokyo Skytree", "Meiji Shrine", "Akihabara"],
        foods=["ramen", "sushi", "convenience store snacks"],
        indoors=["TeamLab-style digital art", "arcades", "department store food halls"],
        outdoors=["Temple walks", "city viewpoints", "neighborhood exploration"],
        packing=["walking shoes", "rail pass wallet", "portable charger", "compact umbrella"],
    ),
}


INTEREST_THEMES = {
    "food": "food hunt with signature local dishes",
    "nature": "outdoor time in scenic spots",
    "history": "cultural stops and historic landmarks",
    "adventure": "high-energy activities and local thrills",
    "nightlife": "evening plans with lively atmosphere",
    "relaxation": "slow moments, cafes, and recharge time",
}


def normalize_destination(name: str) -> str:
    return name.strip().lower()


def get_destination(name: str) -> Destination:
    key = normalize_destination(name)
    return DESTINATIONS.get(key, Destination(
        country="Custom destination",
        vibe="Flexible city break built around your interests",
        weather="Check the live forecast before you go and keep one backup indoor plan each day.",
        daily_costs={"budget": 3000, "medium": 6000, "luxury": 12000},
        highlights=["Main city center", "top-rated local attraction", "popular food street", "cultural landmark"],
        foods=["regional specialties", "street food picks", "a signature dessert"],
        indoors=["museum or gallery", "cafe crawl", "local market"],
        outdoors=["walking tour", "park visit", "sunset viewpoint"],
        packing=["comfortable shoes", "ID copies", "phone charger", "basic medicines"],
    ))


def split_interests(raw_interests: str) -> List[str]:
    values = [item.strip().lower() for item in raw_interests.split(",")]
    return [item for item in values if item]


def parse_int(value: str | None, default: int, lower: int, upper: int) -> int:
    try:
        parsed = int(value or default)
    except (TypeError, ValueError):
        parsed = default
    return max(lower, min(parsed, upper))


def build_itinerary(destination_name: str, days: int, interests: List[str], travel_style: str) -> List[Dict[str, str]]:
    destination = get_destination(destination_name)
    highlights = destination.highlights
    days = max(1, min(days, 10))
    itinerary = []

    for day in range(1, days + 1):
        start = highlights[(day - 1) % len(highlights)]
        mid = highlights[(day) % len(highlights)]
        evening_theme = INTEREST_THEMES.get(interests[(day - 1) % len(interests)], "balanced local exploring") if interests else "balanced local exploring"

        itinerary.append({
            "day": f"Day {day}",
            "morning": f"Start at {start} and ease into the destination's {destination.vibe.lower()}.",
            "afternoon": f"Continue with {mid} plus {destination.outdoors[(day - 1) % len(destination.outdoors)]}.",
            "evening": f"Keep the evening focused on {evening_theme}.",
            "budget_note": f"Target a {travel_style} pace today and leave room for {destination.foods[(day - 1) % len(destination.foods)]}.",
        })

    return itinerary


def build_budget(destination_name: str, days: int, travelers: int, travel_style: str) -> Dict[str, int]:
    destination = get_destination(destination_name)
    daily_total = destination.daily_costs[travel_style] * travelers
    hotel = ceil(daily_total * 0.35)
    food = ceil(daily_total * 0.25)
    transport = ceil(daily_total * 0.15)
    activities = ceil(daily_total * 0.25)

    return {
        "daily_total": daily_total,
        "hotel": hotel * days,
        "food": food * days,
        "transport": transport * days,
        "activities": activities * days,
        "grand_total": daily_total * days,
    }


def build_packing_list(destination_name: str, interests: List[str]) -> List[str]:
    destination = get_destination(destination_name)
    extras = []

    if "adventure" in interests or "nature" in interests:
        extras.extend(["day backpack", "water bottle"])
    if "nightlife" in interests:
        extras.append("evening outfit")
    if "history" in interests:
        extras.append("small notebook or travel journal")

    ordered = destination.packing + extras
    seen = set()
    result = []
    for item in ordered:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def build_food_recommendations(destination_name: str) -> str:
    destination = get_destination(destination_name)
    return ", ".join(destination.foods)


@app.route("/", methods=["GET", "POST"])
def home():
    planner = None
    form_data = {
        "destination": "",
        "days": 4,
        "budget": "medium",
        "travelers": 2,
        "travel_style": "medium",
        "interests": "food, nature",
    }

if request.method == "POST":
    destination_name = request.form.get("destination", "").strip()
    days = parse_int(request.form.get("days"), 4, 1, 10)

    travel_style = request.form.get("travel_style", "medium")
    if travel_style not in {"budget", "medium", "luxury"}:
        travel_style = "medium"

    travelers = parse_int(request.form.get("travelers"), 2, 1, 12)
    interests = split_interests(request.form.get("interests", ""))

    destination = get_destination(destination_name)

# Build planner data
    itinerary = build_itinerary(
        destination_name,
        days,
        interests,
        travel_style
    )

    budget = build_budget(
        destination_name,
        days,
        travelers,
        travel_style
    )

    packing_list = build_packing_list(
        destination_name,
        interests
    )

    food_recommendations = build_food_recommendations(
        destination_name
    )
    
    planner = {
        "destination_name": destination_name.title() if destination_name else "Your Trip",
        "country": destination.country,
        "vibe": destination.vibe,
        "weather": destination.weather,

        "days": days,
        "travelers": travelers,
        "travel_style": travel_style.title(),

        # Main Sections
        "itinerary": itinerary,
        "budget": budget,
        "packing_list": packing_list,

        # Food
        "food_recommendations": food_recommendations,

        # Attractions
        "highlights": destination.highlights,
        "backup_plan": destination.indoors[0],

        # Extra Information
        "must_try_foods": destination.foods,
        "indoor_activities": destination.indoors,
        "outdoor_activities": destination.outdoors,

        # Quick Stats
        "trip_summary": {
            "Destination": destination_name.title(),
            "Country": destination.country,
            "Duration": f"{days} Days",
            "Travelers": travelers,
            "Travel Style": travel_style.title(),
            "Estimated Budget": f"₹{budget['grand_total']:,}"
        },
