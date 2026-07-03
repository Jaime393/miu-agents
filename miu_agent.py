#!/usr/bin/env python3
import sys,json,os,urllib.request
G=os.environ.get("GROQ_API_KEY","")
SYS="Eres MIU Motor Epistemico. Solo D_f. K_i=tautologia."
def groq(m):
 p=json.dumps({"model":"llama-3.3-70b-versatile","messages":m,"max_tokens":800}).encode()
 r=urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",data=p,headers={"Authorization":f"Bearer {G}","Content-Type":"application/json"})
 with urllib.request.urlopen(r) as x:return json.loads(x.read())["choices"][0]["message"]["content"]
def search(q):
 w=os.environ.get("MIU_SEARCH_WEBHOOK","")
 if not w:return[]
 p=json.dumps({"query":q,"top_k":5}).encode()
 r=urllib.request.Request(w,data=p,headers={"Content-Type":"application/json"})
 with urllib.request.urlopen(r) as x:return json.loads(x.read()).get("results",[])
def run(t):
 ctx=search(t)
 ins=groq([{"role":"system","content":SYS},{"role":"user","content":f"Task:{t}\nCorpus:{str(ctx)[:2000]}"}])
 print(ins)
if __name__=="__main__":run(" ".join(sys.argv[1:]) or "analiza D_f")
