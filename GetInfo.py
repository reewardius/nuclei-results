import json

written_data = set()

with open("res.json", "r") as json_file:
    for line in json_file:
        data = json.loads(line)
        
        if "info" in data:
            info = data["info"]
            
            if "severity" in info:
                severity = info["severity"]
                
                if severity == "info":
                    data_str = json.dumps(data)
                    
                    if data_str not in written_data:
                        written_data.add(data_str)
                        with open("Info_Findings.txt", "a") as findings_file:
                            findings_file.write(data_str + "\n")
                elif severity == "low":
                    data_str = json.dumps(data)
                    
                    if data_str not in written_data:
                        written_data.add(data_str)
                        with open("Low_Findings.txt", "a") as findings_file:
                            findings_file.write(data_str + "\n")
                elif severity == "medium":
                    data_str = json.dumps(data)
                    
                    if data_str not in written_data:
                        written_data.add(data_str)
                        with open("Medium_Findings.txt", "a") as findings_file:
                            findings_file.write(data_str + "\n")
                elif severity == "high":
                    data_str = json.dumps(data)
                    
                    if data_str not in written_data:
                        written_data.add(data_str)
                        with open("High_Findings.txt", "a") as findings_file:
                            findings_file.write(data_str + "\n")
                elif severity == "critical":
                    data_str = json.dumps(data)
                    
                    if data_str not in written_data:
                        written_data.add(data_str)
                        with open("Critical_Findings.txt", "a") as findings_file:
                            findings_file.write(data_str + "\n")