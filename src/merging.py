
def calculate_severity(inspection, thermal):

    leakage_details = inspection.get("leakage_details", {})
    avg_temp_diff = thermal.get("average_temperature_difference", 0)

    leakage_all_time = (
        leakage_details.get("Leakage during", "") == "All time"
    )

    concealed_plumbing = any(
        value == "Yes"
        for key, value in leakage_details.items()
        if "concealed" in key.lower()
    )

   
    if leakage_all_time and concealed_plumbing and avg_temp_diff >= 5:
        severity = "High"
        reasoning = (
            "Continuous leakage with concealed plumbing involvement "
            "and high thermal variation detected."
        )

    elif concealed_plumbing and avg_temp_diff >= 4:
        severity = "Moderate"
        reasoning = (
            "Leakage indicators present with noticeable thermal variation."
        )

    else:
        severity = "Low"
        reasoning = (
            "Limited leakage indicators and low thermal variation."
        )

    return {
        "severity_level": severity,
        "severity_reasoning": reasoning
    }
def merge_inspection_thermal(inspection, thermal):

    merged = {
        "inspection_summary": inspection,
        "thermal_summary": thermal,
        "analysis": {}
    }

    avg_temp_diff = thermal.get("average_temperature_difference", 0)

    leakage_present = any(
        value == "Yes"
        for value in inspection.get("leakage_details", {}).values()
    )

    if leakage_present and avg_temp_diff >= 4:
        merged["analysis"]["moisture_confirmation"] = (
            "Thermal variation supports reported leakage findings."
        )
    else:
        merged["analysis"]["moisture_confirmation"] = (
            "No strong thermal confirmation."
        )


    severity_result = calculate_severity(inspection, thermal)

    merged["analysis"]["severity"] = severity_result

    return merged
