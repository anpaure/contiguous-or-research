#!/usr/bin/env python3
"""One deterministic depth-three singleton-gadget run. h100 execution only."""
import json
import resource
import signal
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU,(90,90))
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.alarm(110)
BASE=Path('/home/amodo/exact-b-native35-user-graft-20260908')
FULL=(1<<17)-1
BITS=[1<<i for i in range(17)]
word=list(map(int,(BASE/'native291_rooted_word.word').read_text().split()))
assert len(word)==291

def unions(word):
    out=set()
    for a in range(len(word)):
        v=0
        for x in word[a:]:
            v|=x;out.add(v)
            if v==FULL:break
    return out
def bor(items):
    v=0
    for x in items:v|=x
    return v
def coord(x):return x.bit_length()
def make_state(tail,s8,s9):
    return dict(tail=tuple(tail[-4:]),s8=frozenset(s8),s9=frozenset(s9))
def profile(st):
    t=st['tail'];return [t[-1],bor(t[-2:]),bor(t[-3:]),bor(t)]
def advance(st,x):
    t=st['tail'];a=bor(t[-2:])|x;v=bor(t[-3:])|x
    if a.bit_count()!=8 or v.bit_count()!=9 or a in st['s8'] or v in st['s9']:return None
    return make_state(t+(x,),st['s8']|{a},st['s9']|{v})
def singleton_menu(st,missing):
    L,B,A,T=profile(st)
    return [z for z in sorted(missing) if not(z&T) and (B|z) not in st['s8'] and (A|z) not in st['s9']]

old=unions(word)
old8={x for x in old if x.bit_count()==8};old9={x for x in old if x.bit_count()==9}
missing={b for b in BITS if b not in old}
assert missing==set(BITS[:14])
state=make_state(word[-4:],old8,old9)
assert list(map(int.bit_count,profile(state)))==[6,7,8,9]
initial=dict(tail=word[-4:],suffix_unions=profile(state),
             missing_singletons=[coord(z) for z in sorted(missing)],
             legal_missing_singletons=[coord(z) for z in singleton_menu(state,missing)])
extension=[];rounds=[];stopped=None
while missing:
    assert len(missing)%2==0
    L,B,A,T=profile(state)
    assert [L.bit_count(),B.bit_count(),A.bit_count(),T.bit_count()]==[6,7,8,9]
    candidates=[];pair_count=0
    for z in singleton_menu(state,missing):
        st1=advance(state,z);assert st1 is not None
        for w in singleton_menu(st1,missing-{z}):
            st2=advance(st1,w);assert st2 is not None
            pair_count+=1;remain=missing-{z,w}
            if not remain:
                candidates.append(((0,0,0,0,(z,w)),[z,w],st2,z,w,None,None))
                continue
            T2=profile(st2)[3]
            for fresh in BITS:
                if fresh&T2:continue
                for removed in BITS:
                    if not removed&L:continue
                    x=(L^removed)|fresh
                    st3=advance(st2,x)
                    if st3 is None:continue
                    assert list(map(int.bit_count,profile(st3)))==[6,7,8,9]
                    pending_mask=bor(remain)
                    last,_,_,owner=profile(st3)
                    score=((last&pending_mask).bit_count(),(owner&pending_mask).bit_count(),
                           -len(singleton_menu(st3,remain)),int(fresh in remain),(z,w,x))
                    candidates.append((score,[z,w,x],st3,z,w,removed,fresh))
    if not candidates:
        stopped=dict(reason='No two-missing-singleton plus six-letter-restore gadget at this fixed frontier.',
                     missing=[coord(z) for z in sorted(missing)],suffix_unions=profile(state),
                     immediate_singleton_menu=[coord(z) for z in singleton_menu(state,missing)],
                     ordered_legal_singleton_pairs=pair_count)
        break
    selected=min(candidates,key=lambda x:x[0])
    score,letters,state,z,w,removed,fresh=selected
    rounds.append(dict(round=len(rounds)+1,missing_before=[coord(q) for q in sorted(missing)],
        ordered_legal_singleton_pairs=pair_count,complete_gadget_candidates=len(candidates),
        chosen_singletons=[coord(z),coord(w)],letters=letters,
        removed_from_old_last_letter=(coord(removed) if removed is not None else None),
        restoring_new_coordinate=(coord(fresh) if fresh is not None else None),
        score=list(score[:-1]),suffix_unions_after=profile(state)))
    extension.extend(letters);missing-={z,w}

result_word=word+extension
new=unions(result_word)
assert old<=new
seen8=set(old8);seen9=set(old9);step_records=[]
for end in range(291,len(result_word)):
    a=bor(result_word[end-2:end+1]);v=bor(result_word[end-3:end+1])
    assert a.bit_count()==8 and v.bit_count()==9 and a not in seen8 and v not in seen9
    seen8.add(a);seen9.add(v)
    step_records.append(dict(position=end,letter=result_word[end],new_rank8=a,new_rank9=v))

recency=();b8_inc=0;old_b8_inc=0;seen_rank9=set();bprev=0;loss=0;idle=0
for i,x in enumerate(result_word):
    recency=(x,)+tuple(y&~x for y in recency if y&~x)
    v=0;ps=[]
    for b in recency:v|=b;ps.append(v)
    b8=sum(q.bit_count()<8 for q in ps);b8_inc+=b8
    if i==290:old_b8_inc=b8_inc
    b9=sum(q.bit_count()<9 for q in ps)
    rank9=[q for q in ps if q.bit_count()==9]
    isnew=bool(rank9 and rank9[0] not in seen_rank9)
    if rank9:seen_rank9.add(rank9[0])
    delta=b9-bprev;assert delta<=1 and not(delta==1 and isnew)
    loss+=max(0,-delta);idle+=(not isnew and delta<=0);bprev=b9
assert len(result_word)-len(seen_rank9)==loss+bprev+idle
old_low8={x for x in old if x.bit_count()<8};new_low8={x for x in new if x.bit_count()<8}
added_low8=new_low8-old_low8
new9={x for x in new if x.bit_count()==9}
new_low9={x for x in new if x.bit_count()<9}
t=0
while t*len(new9)+t*(t+1)//2<len(new_low9):t+=1
report=dict(initial=initial,success=not missing,extension_length=len(extension),extension_letters=extension,
    total_word_length=len(result_word),rounds=rounds,stopped=stopped,
    all_singletons_present=all(b in new for b in BITS),missing_singletons=[coord(b) for b in BITS if b not in new],
    all_existing_targets_retained=old<=new,all_new_endpoints_fresh_rank8_and9=True,
    original_targets=len(old),final_targets=len(new),new_targets=len(new-old),
    original_below8_targets=len(old_low8),new_distinct_below8_targets=len(added_low8),
    new_below8_target_masks=sorted(added_low8),original_below8_state_incidences=old_b8_inc,
    added_below8_state_incidences=b8_inc-old_b8_inc,
    added_below8_repeated_incidences=(b8_inc-old_b8_inc)-len(added_low8),
    final_below8_repeated_incidences=b8_inc-len(new_low8),
    final_rank8_targets=sum(x.bit_count()==8 for x in new),final_rank9_targets=len(new9),
    final_below9_targets=len(new_low9),endpoint_delay=t,endpoint_lower_bound=len(new9)+t,
    optimal_for_covered_target_family=(len(result_word)==len(new9)+t),
    potential_rank9=dict(N=len(result_word),D=len(seen_rank9),L=loss,b_terminal=bprev,E=idle),
    new_endpoint_witnesses=step_records,
    restricted_method='At each stable frontier enumerate every ordered pair of fresh missing singleton appends and every restoring six-letter swap of the old last letter; choose the displayed deterministic score. Last pair omits restore. No leading filler, global search, random choice, or broader fallback.',
    resource_caps=dict(cpu_seconds=90,wall_seconds=110,address_space_bytes=1024**3))
(BASE/'native291_singleton_extension_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
(BASE/'native291_singleton_extension.word').write_text('\n'.join(map(str,extension))+'\n')
(BASE/'native291_singletons_extended.word').write_text('\n'.join(map(str,result_word))+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('new_below8_target_masks','new_endpoint_witnesses')},indent=2))
print('PASS' if not missing else 'STOP','one fixed depth-three singleton-gadget run; no family enlargement.')
