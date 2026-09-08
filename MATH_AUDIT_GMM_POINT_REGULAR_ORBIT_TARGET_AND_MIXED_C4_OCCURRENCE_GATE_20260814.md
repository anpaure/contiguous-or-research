# Hostile audit: GMM orbit targets and the mixed-C4 occurrence gate

**Date:** 2026-08-14  
**Source:**
`MATH_REDUCTION_GMM_POINT_REGULAR_ORBIT_TARGET_AND_EXACT_C4_C6_AVAILABILITY_GATE_20260814.md`  
**Verdict:** PASS at the stated reduction scope; no GMM Markov theorem is
claimed

## 1. Corrections forced by the audit

An earlier draft incorrectly treated the induced-square action

\[
 e_A+e_B-e_C-e_D
\]

as if it were the complete lower-moving `C_4` catalogue.  That led to a
false independent-support obstruction.  The missing mixed star/top square
has lower action `e_A-e_B`, so it moves a single surplus token along an
arbitrary edge of `J(n,m-1)`.  The source now removes the false obstruction
and proves constructive conformal connectivity of the entire abstract
fixed-mass surplus simplex.

The first replacement formula also had `p in B`; this was an indexing
error.  In the final normal form `B=K+b`, both `p,a` are outside `B`.
For a fixed adjacent transfer `K+b -> K+a`, `p` has `m+1` choices and then
`c` has `m` choices, giving `m(m+1)` atoms.  Equations (3.4)--(3.9) now use
this convention consistently.

## 2. Orbit-target audit

The desired point degree is integral because

\[
 {D(m-1)\over 2m+1}
 ={2\over m}{2m\choose m-2}
 ={2m-1\choose m-2}-{2m-1\choose m-3}.
\]

Hence `(2m+1)/gcd(2m+1,m-1)` divides `D`.  When the gcd is one, every
cyclic orbit is full.  When it is three, orbit sizes are `n` and `n/3`;
the number of short orbits is the Catalan integer

\[
 {1\over s}{s\choose t},\qquad n=3s,\quad m-1=3t,\quad s=2t+1.
\]

At `m=7`, this is exactly two short orbits, with total short mass `10`;
the other `4995` blocks give `333` full orbits, and
`D=1430=95(15)+5`.  At `m=4`, the orbit profile is `9^9,3^1`, so `42`
cannot be a whole-orbit sub-sum.  The square-sum exchange proof supplies a
simple regular family independently of cyclic orbits.  This section
passes.

## 3. Mixed-C4 algebra and conformality audit

For owners

\[
 Kpa, Kpc, Kpb, Kab
\]

with old edges `12,34` and new edges `23,41`, direct intersections give

\[
 \{Kp,Kb\}\longrightarrow\{Kp,Ka\},
\]

and direct unions give

\[
 \{Kpac,Kpab\}\longrightarrow\{Kpbc,Kpab\}.
\]

Thus the boxed lower and upper actions in (3.2) are correct.  Because the
unit lower actions are the oriented edges of the connected Johnson graph,
moving one token at a time along paths proves the nonnegative routing
claim without any cancellation or intermediate debt.  It does not prove
that the required two cycle edges occur.

## 4. Occurrence and chronology audit

For surplus source `B=K+b`, a selected edge of colour `B` has outside
labels `{p,a}` with `p,a\notin B`.  Choosing its orientation and `b\in B`,
the second old edge must have colour `B-b+p=K+p` and labels `{a,c}`.  The
condition `c\ne b` is exactly what prevents the two old edges from sharing
the owner `K+p+b`.  These facts give the two-step sum (3.7), whose inner
term is

\[
 \deg_{H_{B-b+p}}(a)-
 \mathbf1_{\{a,b\}\in E(H_{B-b+p})}.
\]

Therefore vanishing of every such continuation term is necessary and
sufficient for zero mixed occurrence candidates.  This is the sharp
structural cut frozen by the note.  Hamilton safety is correctly kept in
the separate indicator `chi_C`; path-forest degree bounds alone do not
decide that chronology.

The small verification is scoped correctly: exhaustive normalized `m=2`
enumeration and a seeded, nonexhaustive `m=3` sample replay the incidence
and switch predicates.  They are evidence for formula integrity only.

## 5. Scope verdict

The source proves:

- existence of a point-regular simple target, with an exact cyclic-orbit
  construction except at the stated `m=4` whole-orbit obstruction;
- complete conformal routing of abstract lower-surplus ledgers by mixed
  unit actions;
- the exact two-step occurrence count and the exact zero-occurrence cut;
- separate Hamilton chronology criteria for repeated-colour `C_4`s and
  the explicit injective-lower rectangle `C_6`.

It does **not** prove that a GMM cycle realizes the target, that every
point-nonregular GMM cycle has a legal mixed move, or that the legal state
graph reaches upper perfection.  With those exclusions explicit, PASS.

## 6. Frozen provenance

Source SHA-256: `6755598e30761edb94a604624e6d4c71d57ca4255260c15f86a13ffdeb8b6bc0`  
Verifier: `scratch/search_gmm_mixed_c4_occurrence_small_20260814.py`  
Verifier SHA-256: `b52c7eb868d290ca06134867e420a56257162672ebe3059b64a6a157348334cb`  
`m=2` output SHA-256: `8b53cec2fa162cf09e826e661440d7d82df6dca249fe3817a772f9485ff26d59`  
`m=3` output SHA-256: `7278b44605a59a680c7f6e71a4310a3ab43a09028c96c4ea9057a20d4faa1a40`  
Audit SHA-256 before provenance insertion:
`b1e91f687b3df51101956fff5f051c70fa72b190ffc38987435028a9ba58aef3`.
