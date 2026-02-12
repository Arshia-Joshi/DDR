import re

def extract_dynamic_table_pairs(text):

    data = {}

    
    colon_pattern = r"([A-Za-z0-9\s\/\-\(\)]+):\s*(.*)"
    colon_matches = re.findall(colon_pattern, text)

    for key, value in colon_matches:
        clean_key = key.strip()
        clean_value = value.strip()

        if clean_value == "":
            clean_value = "Not Available"

        data[clean_key] = clean_value

   
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

    pattern = rf"(.+?)\s+({value_regex})"

    matches = re.findall(pattern, text)

    for key, value in matches:
        clean_key = key.strip()
        clean_value = value.strip()
        data[clean_key] = clean_value

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

        lower_key = key.lower()

        
        if any(word in lower_key for word in [
            "property",
            "floors",
            "inspection date",
            "inspected by",
            "customer",
            "mobile",
            "email",
            "address"
        ]):
            structured["property_details"][key] = value

        
        elif "leakage" in lower_key:
            structured["leakage_details"][key] = value

        
        elif any(word in lower_key for word in [
            "tile",
            "nahani",
            "wc",
            "gaps",
            "plumbing",
            "flush",
            "washbasin"
        ]):
            structured["bathroom_observations"][key] = value

       
        elif any(word in lower_key for word in [
            "external wall",
            "paint",
            "crack",
            "rcc",
            "column",
            "beam",
            "corrosion"
        ]):
            structured["external_wall_observations"][key] = value

        
        else:
            structured["other_observations"][key] = value

    return structured
