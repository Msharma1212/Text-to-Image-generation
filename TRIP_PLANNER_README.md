# Smart Trip Planner

This repo now includes a standalone Flask trip planner app in addition to the existing image generator.

## Files

- `trip_planner_app.py` - Flask backend and itinerary generation logic
- `templates/trip_planner/index.html` - Planner UI
- `static/trip_planner.css` - Styling

## Features

- Destination-based itinerary generation
- Budget estimation by travel style and traveler count
- Packing checklist
- Weather note and backup indoor suggestion
- Suggested local food items

## Run

1. Install Python 3.10+.
2. Install Flask if needed:

```bash
pip install flask
```

3. Start the app:

```bash
python trip_planner_app.py
```

4. Open `http://127.0.0.1:5000`

## Example inputs

- Destination: `Goa`
- Days: `4`
- Travelers: `2`
- Travel style: `Medium`
- Interests: `food, nature, nightlife`
