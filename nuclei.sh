#/bin/bash
nuclei -l alive -t /root/nuclei-templates/ -rl 500 -json -o res.json -stats -retries 0
python GetInfo.py
python ParseJson.py
rm *_Findings.txt
echo "NucleiFullResult.txt file was successfully created"