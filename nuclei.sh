#/bin/bash
nuclei -l alive -t /root/nuclei-templates/ -rl 500 -json -o res.json -stats -retries 2 # change alive to your file with subdomains
python GetInfo.py
python ParseJson.py
rm *_Findings.txt
echo "NucleiFullResult.txt file was successfully created"
