from src.extract_text import extract_text_from_pdf
from src.sample_ext import extract_dynamic_table_pairs, structure_inspection_data
from src.thermal_ext import extract_thermal_json
from src.merging import merge_inspection_thermal
from src.validation import validate_and_prepare
from src.llm import generate_ddr_with_ollama
import json


inspection_text = extract_text_from_pdf("data/Sample_Report.pdf")
thermal_text = extract_text_from_pdf("data/Thermal_Images.pdf")


flat_data = extract_dynamic_table_pairs(inspection_text)
structured_inspection = structure_inspection_data(flat_data)


thermal_data = extract_thermal_json(thermal_text)

#thermal_data["average_temperature_difference"] = 1

merged_data = merge_inspection_thermal(structured_inspection, thermal_data)


validated_data = validate_and_prepare(merged_data)

final_ddr = generate_ddr_with_ollama(validated_data)



#print("\n--- MERGED DATA  ---\n")
#print(json.dumps(merged_data, indent=4))

print("\n\n===== FINAL DDR =====\n")
print(final_ddr)
