import json,glob,sys,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d={f.split("/")[-1][:-5]:json.load(open(f,encoding="utf-8")) for f in glob.glob(os.path.join(BASE,"data","*.json"))}
E=lambda k:{e["id"]:e for e in d[k]["entries"]}
goods,rec,mod,ships,eq,tech,fac=E("goods"),E("recipes"),E("modules"),E("ships"),E("equipment"),E("technologies"),E("factions")
res=set(goods)|{"data","electricity"}
err=[]
for r in rec.values():
    if r["module"] not in mod: err.append("recette: module inconnu "+r["id"])
    for x in r["inputs"]+r["outputs"]:
        if x["item"] not in res: err.append("recette: marchandise inconnue "+x["item"])
    if r.get("unlock") and r["unlock"] not in tech: err.append("recette: tech inconnue "+r["unlock"])
for t in tech.values():
    for p in t["prerequisites"]:
        if p not in tech: err.append("tech: prérequis inconnu "+p)
        elif tech[p]["tier"]>t["tier"]: err.append("tech: palier incohérent "+t["id"])
seen,stack=set(),set()
def dfs(i):
    if i in stack: err.append("cycle "+i); return
    if i in seen: return
    stack.add(i)
    for p in tech[i]["prerequisites"]: dfs(p)
    stack.discard(i); seen.add(i)
for i in tech: dfs(i)
used=set()
for r in rec.values(): used|={x["item"] for x in r["inputs"]}
for s in ships.values(): used|={x["item"] for x in s["build"]["items"]}
used|={"fuel","iron_ore"}
for g in goods:
    if g not in used and g not in ("ammo","missiles"): err.append("marchandise inutilisée "+g)
for m in mod.values():
    if m.get("unlock") and m["unlock"] not in tech: err.append("module: tech inconnue")
for s in ships.values():
    if s["unlock"] not in tech: err.append("vaisseau: tech inconnue "+s["id"])
    for x in s["build"]["items"]:
        if x["item"] not in goods: err.append("vaisseau: marchandise inconnue")
if abs(sum(r["marketShare"] for r in d["employees"]["rarities"])-1)>1e-9: err.append("parts de marché des raretés")
for f in fac.values():
    lv=sorted(f["relationLevels"],key=lambda x:x["min"])
    if lv[0]["min"]!=-100 or lv[-1]["max"]!=100 or any(lv[i]["max"]+1!=lv[i+1]["min"] for i in range(len(lv)-1)): err.append("paliers de relation "+f["id"])
for e in d["events"]["entries"]:
    if e["type"]=="pirate" and e["offlineAllowed"]: err.append("événement destructeur hors ligne")
lang=json.load(open(os.path.join(BASE,"data","lang","fr.json"),encoding="utf-8"))
for k,fn in (("technologies",tech),("ships",ships),("goods",goods),("modules",mod)):
    for i in fn:
        if f"{k}.{i}.name" not in lang: err.append("texte manquant "+k+"."+i)
print(len(tech),"technologies,",len(rec),"recettes,",len(mod),"modules,",len(ships),"vaisseaux")
print("OK : toutes les données sont valides." if not err else "\n".join(err))
if sys.stdin.isatty(): input("\nAppuyez sur Entrée pour fermer cette fenêtre...")
sys.exit(1 if err else 0)
