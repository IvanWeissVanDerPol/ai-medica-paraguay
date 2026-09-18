#!/usr/bin/env python3
"""Research harness: queries 5 scholarly APIs for the Ometz/Gaby idea corpus."""
import json, time, urllib.request, urllib.parse, sys, os

env = {}
with open(os.path.join(os.path.dirname(__file__), 'keys.env')) as f:
    for line in f:
        if '=' in line and not line.startswith('#'):
            k, v = line.strip().split('=', 1)
            env[k] = v

NCBI = env['NCBI_API_KEY']; CORE = env['CORE_API_KEY']
OA = env['OPENALEX_API_KEY']; UP = env['UNPAYWALL_EMAIL']

def fetch(url, headers=None, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=headers or {'User-Agent': f'research-harness ({UP})'})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            if i == tries-1: return {'error': str(e)[:100]}
            time.sleep(2*(i+1))

def pubmed(query, maxr=5):
    q = urllib.parse.quote(query)
    s = fetch(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={q}&retmax={maxr}&sort=relevance&api_key={NCBI}")
    ids = s.get('esearchresult',{}).get('idlist',[])
    if not ids: return []
    time.sleep(0.12)
    d = fetch(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={','.join(ids)}&api_key={NCBI}")
    out = []
    for pid in ids:
        it = d.get('result',{}).get(pid,{})
        out.append({'source':'pubmed','id':pid,'title': it.get('title',''),
            'journal': it.get('source',''),'pubdate': it.get('pubdate',''),
            'doi': next((a['value'] for a in it.get('articleids',[]) if a['idtype']=='doi'), '')})
    return out

def openalex(query, maxr=5):
    q = urllib.parse.quote(query)
    d = fetch(f"https://api.openalex.org/works?search={q}&per_page={maxr}&sort=cited_by_count:desc&api_key={OA}&mailto={UP}")
    out = []
    for w in d.get('results',[]):
        out.append({'source':'openalex','id':w.get('doi','') or w.get('id',''),
            'title': w.get('title','') or w.get('display_name',''),
            'journal': ((w.get('primary_location') or {}).get('source') or {}).get('display_name',''),
            'pubdate': w.get('publication_date',''),
            'cited_by': w.get('cited_by_count',0),
            'is_oa': (w.get('open_access') or {}).get('is_oa', False)})
    return out

def europepmc(query, maxr=5):
    q = urllib.parse.quote(query)
    d = fetch(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}&format=json&pageSize={maxr}&sort=CITED desc")
    out = []
    for r in d.get('resultList',{}).get('result',[]):
        out.append({'source':'europepmc','id':r.get('doi','') or r.get('id',''),
            'title': r.get('title',''),'journal': r.get('journalTitle',''),
            'pubdate': r.get('pubYear',''),'cited_by': r.get('citedByCount',0),
            'is_oa': r.get('isOpenAccess','')=='Y'})
    return out

def core(query, maxr=5):
    d = fetch(f"https://api.core.ac.uk/v3/search/works/?q={urllib.parse.quote(query)}&limit={maxr}",
              headers={'Authorization': f'Bearer {CORE}'})
    out = []
    for r in d.get('results',[]) or []:
        out.append({'source':'core','id':r.get('id',''),'title': r.get('title',''),
            'journal': r.get('publisher',''),'pubdate': str(r.get('yearPublished','')),
            'doi': r.get('doi','')})
    return out

QUERIES = json.load(open(os.path.join(os.path.dirname(__file__), 'queries.json')))

def main():
    corpus = {}
    for topic, queries in QUERIES.items():
        corpus[topic] = []
        for q in queries:
            for fn in (pubmed, openalex, europepmc, core):
                res = fn(q)
                corpus[topic].extend(res)
                time.sleep(0.12)
        seen = set(); deduped = []
        for r in corpus[topic]:
            t = (r.get('title') or '')[:60].lower()
            if t and t not in seen:
                seen.add(t); deduped.append(r)
        corpus[topic] = deduped
        print(f"[{topic}] {len(deduped)} unique", flush=True)
    with open(os.path.join(os.path.dirname(__file__), 'research_corpus.json'),'w') as f:
        json.dump(corpus, f, ensure_ascii=False, indent=1)
    print(f"TOTAL: {sum(len(v) for v in corpus.values())}")

if __name__ == '__main__':
    main()