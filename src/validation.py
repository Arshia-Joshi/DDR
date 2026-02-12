def validate_and_prepare(merged_data):

    validation = {
        "missing_information": [],
        "conflicts": []
    }

    inspection = merged_data.get("inspection_summary", {})
    thermal = merged_data.get("thermal_summary", {})

    
    property_details = inspection.get("property_details", {})
    for key, value in property_details.items():
        if value == "Not Available":
            validation["missing_information"].append(key)

    
    if not thermal.get("readings"):
        validation["missing_information"].append("Thermal readings")

   
    leakage_details = inspection.get("leakage_details", {})
    avg_temp = thermal.get("average_temperature_difference", 0)

    leakage_present = any(
        value == "Yes" for value in leakage_details.values()
    )

    if leakage_present and avg_temp < 2:
        validation["conflicts"].append(
            "Leakage reported but minimal thermal variation detected."
        )

    merged_data["validation"] = validation

    return merged_data
