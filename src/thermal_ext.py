import re

def extract_thermal_json(text):

    hotspots = re.findall(r"Hotspot\s*:\s*(\d+\.?\d*)", text)
    coldspots = re.findall(r"Coldspot\s*:\s*(\d+\.?\d*)", text)

    readings = []

    for h, c in zip(hotspots, coldspots):
        h = float(h)
        c = float(c)
        readings.append({
            "hotspot": h,
            "coldspot": c,
            "difference": round(h - c, 2)
        })

    if readings:
        avg_diff = sum(r["difference"] for r in readings) / len(readings)
    else:
        avg_diff = 0

    return {
        "total_scans": len(readings),
        "average_temperature_difference": round(avg_diff, 2),
        "readings": readings
    }
