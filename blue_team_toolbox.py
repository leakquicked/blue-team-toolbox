import argparse,json,re
from pathlib import Path
RULES=[["encoded","\\b(base64|encodedcommand|-enc)\\b","medium"],["evasion","\\b(disable antivirus|clear event log|wevtutil cl)\\b","high"]]
def analyze_text(text):
    findings=[]
    for rule,pattern,severity in RULES:
        for m in re.finditer(pattern,text,re.I):
            findings.append({"rule":rule,"severity":severity,"line":text.count("\\n",0,m.start())+1,"match":m.group(0)[:120]})
    return findings
def main():
    p=argparse.ArgumentParser(description="Offline text triage helpers for blue-team learning")
    p.add_argument("input",type=Path)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    if not a.input.is_file(): p.error("input file not found")
    report={"tool":"blue-team-toolbox","count":0,"findings":analyze_text(a.input.read_text(encoding="utf-8",errors="replace"))}
    report["count"]=len(report["findings"])
    data=json.dumps(report,indent=2,ensure_ascii=False)
    if a.output: a.output.write_text(data+"\\n",encoding="utf-8")
    print(data)
if __name__=="__main__": main()
