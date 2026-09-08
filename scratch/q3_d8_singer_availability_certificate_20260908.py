"""One <=2s exact availability diagnostic; no optimizer."""
import os,json,time,resource
from collections import Counter
os.sched_setaffinity(0,set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
START=time.monotonic()
BASE='/tmp/Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_CATALOGUE_20260908_ternarylift.json'
CAT='/tmp/Q3_D8_SINGER_TWO_GENERIC_ORBITS_CATALOGUE_20260908_ternarylift.json'
OUT='/tmp/Q3_D8_SINGER_AVAILABILITY_CERTIFICATE_20260908_ternarylift.json'
with open(BASE) as f: base=json.load(f)
with open(CAT) as f: data=json.load(f)
candidates=base['candidates']; critical=set(base['critical'])
def mask(items): return sum(1<<i for i in items)
critical_mask=mask(critical); all_mask=(1<<len(base['reps']))-1
cm=[mask(c['critical']) for c in candidates]
cv=[mask(c['cover']) for c in candidates]
self_ids=[i for i,c in enumerate(candidates) if c['mode']=='short' and c['row_count']==4]
full_ids=[i for i,c in enumerate(candidates) if c['mode']=='full']
assert len(self_ids)==2184 and len(full_ids)==336 and len(data['pairs'])==54
def witness(covered):
    missing=all_mask^covered
    if not missing: return None
    missing_critical=missing&critical_mask
    preferred=missing_critical or missing
    t=(preferred&-preferred).bit_length()-1
    code=base['reps'][t]
    return dict(target_orbit_id=t,code=code,target=[(code//(3**i))%3 for i in range(8)],
                rank=base['ranks'][t],orbit_size=base['sizes'][t],
                missing_target_orbit_count=missing.bit_count(),
                missing_critical_orbit_count=missing_critical.bit_count())
source_records=[]; full_records=[]; survivors=[]
for pi,pair in enumerate(data['pairs']):
    fixed=mask(pair['critical']); coverage=mask(pair['cover'])
    allowed_self=[i for i in self_ids if not(cm[i]&fixed)]
    allowed_full=[i for i in full_ids if not(cm[i]&fixed)]
    complete=coverage
    for i in allowed_self+allowed_full: complete|=cv[i]
    miss=witness(complete)
    source_records.append(dict(source_pair=pi,aggregates=pair['aggregates'],
                               compatible_self_count=len(allowed_self),compatible_full_count=len(allowed_full),
                               missing=miss))
    if miss is not None: continue
    for fi in allowed_full:
        sf=[i for i in allowed_self if not(cm[i]&cm[fi])]
        complete=coverage|cv[fi]
        for i in sf: complete|=cv[i]
        miss=witness(complete)
        full_records.append(dict(source_pair=pi,full_candidate_id=fi,compatible_self_count=len(sf),missing=miss))
        if miss is None: survivors.append(dict(source_pair=pi,full_candidate_id=fi))
certificate=dict(source_records=source_records,full_records=full_records,survivors=survivors)
with open(OUT,'w') as f: json.dump(certificate,f)
summary=dict(elapsed=time.monotonic()-START,source_pairs=54,
             source_pairs_excluded=sum(r['missing'] is not None for r in source_records),
             source_pairs_passing=sum(r['missing'] is None for r in source_records),
             full_cases_checked=len(full_records),full_cases_excluded=sum(r['missing'] is not None for r in full_records),
             surviving_source_full_cases=len(survivors),
             source_missing_rank_distribution=dict(Counter(r['missing']['rank'] for r in source_records if r['missing'])),
             full_missing_rank_distribution=dict(Counter(r['missing']['rank'] for r in full_records if r['missing'])),
             source_compatible_self_distribution=dict(Counter(r['compatible_self_count'] for r in source_records)),
             full_compatible_self_distribution=dict(Counter(r['compatible_self_count'] for r in full_records)),
             first_excluded_source=next((r for r in source_records if r['missing']),None),
             first_excluded_full=next((r for r in full_records if r['missing']),None),certificate=OUT)
summary['elapsed']=time.monotonic()-START
print(json.dumps(summary),flush=True)
