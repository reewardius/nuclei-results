import json

files = ['Info_Findings.txt', 'Low_Findings.txt', 'Medium_Findings.txt', 'High_Findings.txt', 'Critical_Findings.txt']

delimiter = "======================================================="

with open("NucleiFullResult.txt", "w") as result_file:
    for input_file in files:
        with open(input_file, "r") as input_f:
            level = input_file.split("_")[0]
            result_file.write(delimiter + "\n")
            for line in input_f:
                data = json.loads(line)
                template = data.get("template")
                host = data.get("host")
                matched_at = data.get("matched-at")
                matcher_name = data.get("matcher-name")
                extracted_results = data.get("extracted-results")
                result_file.write(f"[{level}]: {host} : [Template]: {template}: [Matcher]: {matched_at}:{matcher_name}:{extracted_results}\n")