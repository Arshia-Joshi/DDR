import re

def extract_dynamic_table_pairs(text):

    data = {}

   
    lines = text.split("\n")

   
    colon_pattern = r"^([A-Za-z0-9\s\/\-\(\)]+):\s*(.+)$"

    for line in lines:
        line = line.strip()
        if not line:
            continue

        colon_match = re.match(colon_pattern, line)

        if colon_match:
            key = colon_match.group(1).strip()
            value = colon_match.group(2).strip()

            if value == "":
                value = "Not Available"

            data[key] = value

   
    value_patterns = [
        "Yes",
        "No",
        "Moderate",
        "All time",
        "Not sure",
        "N/A",
        r"\d+%"
    ]

    value_regex = "|".join(value_patterns)

    table_pattern = rf"^(.+?)\s+({value_regex})$"

    for line in lines:
        line = line.strip()
        if not line:
            continue

        match = re.match(table_pattern, line)

        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()

            data[key] = value

    return data
def structure_inspection_data(flat_data):

    structured = {
        "property_details": {},
        "leakage_details": {},
        "bathroom_observations": {},
        "external_wall_observations": {},
        "other_observations": {}
    }

    for key, value in flat_data.items():
        lk = key.lower()

        if any(w in lk for w in ["property", "floor", "customer", "mobile", "email", "address", "inspection"]):
            structured["property_details"][key] = value

        elif "leakage" in lk:
            structured["leakage_details"][key] = value

        elif any(w in lk for w in ["wc", "tile", "nahani", "plumbing", "gaps"]):
            structured["bathroom_observations"][key] = value

        elif any(w in lk for w in ["external", "wall", "crack", "rcc", "paint", "fungus", "moss"]):
            structured["external_wall_observations"][key] = value

        else:
            structured["other_observations"][key] = value

    return structured
