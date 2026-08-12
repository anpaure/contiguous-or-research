# Audit of the shifted-eight dynamic-flat support-four source

## 1. Frozen source and intended scope

```text
scratch/threadA_search_k16_shifted8_unrestricted_interacting_support4_dynamicflat_20260730.cpp
SHA-256 89e2f2f2a92284fe8f0ed2e2abb25b564c2e572ce2c6d3a7b8a9a57391f63467

included geometry source
scratch/search_ad_k16_bad2_splitbuffer_pair_20260730.cpp
SHA-256 65abf0532b0bbfced9041cbc3d22b48a66ffc7044525e412c37890a62c36d655
```

The intended catalogue consists of every rooted directed cycle

\[
 3846\leftarrow p\leftarrow x\leftarrow y\leftarrow3846
\]

such that

1. at least one support pair has distance at most six;
2. the old three-flat set changes;
3. the new word still has exactly three flats.

No fixed incoming-donor restriction is imposed.  The source is meant as the
dynamic-flat supplement to a separate fixed-flat search.

## 2. Parts that are correct

### 2.1 Boundary hitting

If a three-flat set changes but retains cardinality three, at least one old
flat is destroyed.  Destroying an old flat at edge (e) requires changing
row (e) or (e+1).  For old flat edges 6320, 12869, 12871, every such cycle
therefore meets

```text
{6320,6321,12869,12870,12871,12872}.
```

Classifying a triple by the first one of its roles (p,x,y) that lies in this
set is a valid unique partition, provided the three branches are implemented
with explicit braces.

### 2.2 Interaction completion

After fixing three support positions among (3846,p,x,y), if they already
contain a distance-at-most-six pair, the fourth role is unrestricted.  If
they do not, the fourth role must lie in the union of their six-collars.
`collar_union` implements this exact condition.

### 2.3 Flat accounting and full geometry

Only edges incident with a changed row can alter equality.  If `before` and
`after` count old and new flat edges in that incident-edge union, then

\[
 3-\texttt{before}+\texttt{after}
\]

is the exact new global flat count.  `flat_change` computes this correctly,
including shared incident edges only once.  Candidates passing this count are
sent to the full `geometry` routine, which reconstructs the dynamic depth
schedule, rejects overruns, counts zero envelopes, and checks every middle
row.  Thus an enumerated `g.exact()` candidate is a genuine exact dynamic
chronology.

### 2.4 Upper replay

`upper_holes` maintains the distinct nested ORs of every interval ending at
the current row.  It therefore checks arbitrary interval lengths and every
upper rank, not merely a bounded window.

### 2.5 Signature content

For a legal cell interval, `sig` computes all ordered envelopes, their allowed
union, and the mandatory mask.  The required records

```text
13964: E=(6221,4a21,0a29), A=6a29, M=6809;
13966: E=(4a21,0a29),      A=4a29, M=4809
```

are the correct complete component signatures.  This is stronger and correct,
unlike an ordered-envelope-only check.

## 3. Fatal enumeration bug

The third generation branch ends with

```cpp
if(already_close(fixed))
  for(int x=0;x<N;++x) if(!boundary(x)) test(p,x,y);
else
  for(int x:collar_union(fixed)) if(!boundary(x)) test(p,x,y);
```

but the source has no braces.  Standard C++ binds an `else` to the nearest
unmatched `if`, so the actual parse is

```cpp
if (already_close(fixed)) {
  for (int x=0; x<N; ++x) {
    if (!boundary(x)) test(p,x,y);
    else
      for (int z:collar_union(fixed))
        if (!boundary(z)) test(p,z,y);
  }
}
```

Clang emits `-Wdangling-else` at this line.

Consequences:

1. If (y) is the first boundary role and
   ({3846,p,y}) contains no close pair, the intended collar-(x) branch is
   never executed.  Valid catalogue columns are omitted.
2. If the fixed triple already has a close pair, every boundary value of the
   loop variable triggers an additional complete collar loop.  Many columns
   are duplicated, contradicting the source comment that generation is
   unique.

Therefore no count or no-go from this source is proof-valid.  The minimal
repair is to brace both arms of the outer `if (already_close(fixed))`, then
rerun from a clean output directory.

## 4. Dynamic-cell identity caveat

Even after fixing the branch bug, a dynamic flat may be created before row
4654.  In that case depth at 4654 can be below three, and the interval
`[4654,4657)` is not a legal length-three compiler cell.  Moreover cumulative
cell IDs before 4654 change, so the interval is no longer cell 13964 (and the
same issue applies to 13966).

The current `sig` routine does not check

```text
depth[4654] >= 3,
depth[4655] >= 2,
```

or preservation of the cumulative cell IDs.  It simply computes three/two
envelopes and can label an illegal interval as a provider.  A theorem that
hard-protects the old named cells must require no new flat before 4654 (which
also preserves their cumulative IDs, because all old flats are later), or
must explicitly rebuild the Hall graph and refer only to the physical
intervals rather than old cell IDs.

This caveat cannot create a false exact-middle count: `geometry` remains
correct.  It can create a false `two_provider` classification.

## 5. Lineage hardening

The input guard checks root value, one bad row count, zero envelopes, and
upper completeness, but not the exact input SHA, old flat set, bad-row label
and missing bit, or the two base signatures.  For a frozen theorem run, bind
the input SHA

```text
e8c720ef977b5f561c32d84c7c4a51e710999eab80d88bf814aa1f855b254f06
```

externally and assert at startup:

```text
flats={6320,12869,12871};
bad row 3845: 6ba8->69a8, missing0200;
both complete base signatures as displayed above.
```

## 6. Verdict

The boundary-hitting reduction, intended interaction split, flat-count
identity, full dynamic geometry, arbitrary-upper replay, and mathematical
signature definitions are sound.  The source as frozen is nevertheless
**not complete and must not support a no-go**, because the dangling `else`
omits one entire branch and duplicates another.  After bracing and rerunning,
the result will still need the legal-cell/ID guard before any two-provider or
Hall conclusion.
