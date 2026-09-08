# Exact audit of the `k=17` GK vertex-disjoint cut route

Date: 2026-07-31  
Status: **GO** for the exact cut-exposure optimization and its scalar
accounting.  **OPEN** for the subsequent palette-safe ear completion.  No
length-24313 word is claimed.

## 1. Why the previously proposed ear schedule is incomplete

The two-cut Greene--Kleitman forest has 674 missing rank-six colours with
no rank-seven superset among its original endpoints.  An old-endpoint to
old-endpoint `j`-edge ear has only `j-2` internal--internal edges.  Hence the
proposed mixture

\[
 (x_1,x_2,x_3,x_4)=(4024,905,252,42)
\]

has room for at most

\[
 252+2(42)=336<674
\]

such colours.  The 380 non-all-unused colours were not accounted for.

Exact local enumeration further gives the following warning.  Among all
674 no-endpoint colours, 266 admit a clean three-edge ear, another 128 admit
a clean four-edge ear, and 280 admit neither against the fixed GK rank-eight
and rank-nine palettes.  All 280 do have a fresh unused--unused core edge;
the obstruction is attachment and turn freshness, not the core itself.

## 2. Exact cut-exposure model

Let `C` be the 380 no-endpoint colours which are not among the 294 colours
whose every rank-seven superset is unused.  For each `c in C`, let `I(c)` be
its original internal GK supersets.

For each old GK edge `e=uv` incident with a relevant internal vertex, use a
binary variable `x_e`.  For each `c in C` and `v in I(c)`, use a binary
variable `y_cv`.  The exact model is

\[
\begin{aligned}
 \sum_{v\in I(c)}y_{cv}&=1 &&(c\in C),\\
 \sum_c y_{cv}&\le \sum_{e\ni v}x_e &&(v\text{ relevant}),\\
 \sum_{e\ni v}x_e&\le1 &&(v\text{ on a candidate cut}),
\end{aligned}
\]

and minimizes `sum_e x_e`.  Thus cuts are pairwise vertex-disjoint and each
colour is assigned injectively to an internal vertex exposed by its chosen
cut.  A secondary optimization minimizes endpoint--internal cuts among
minimum-cardinality solutions.

The exact CP-SAT optimum is

\[
 \boxed{312\text{ cuts}},
\]

and among 312-cut solutions the exact minimum number of one-sided
endpoint--internal cuts is 90.  The frozen certificate therefore has

\[
 90\text{ endpoint--internal cuts},\qquad
 222\text{ internal--internal cuts}.
\]

Of these, 68 cuts expose two assigned colours and 244 expose one, accounting
for all `2(68)+244=380` colours.

The elementary lower bound `ceil(380/2)=190` is not attainable.  Already
40 colours have no superset at an internal vertex incident to an
internal--internal edge; the exact optimization records the stronger global
path-conflict cost.

## 3. Literal certificate replay

The dependency-free replay reconstructs all 10,152 GK edges and verifies:

* every listed cut is the claimed original edge;
* all 624 cut vertices are distinct;
* all 380 assigned colours are distinct and are exactly `C`;
* each assigned colour is contained in its exposed internal vertex;
* the derived cut-type counts are 90 and 222;
* the derived occupancy counts are 244 single and 68 double cuts.

The replay derives these counts from the frozen certificate; it does not
hardcode the cut-type partition.

## 4. Correct scalar ledger after 312 cuts

The 90 endpoint--internal cuts create 90 isolated original endpoint
components and destroy one old turn each.  The 222 internal--internal cuts
destroy two old turns each.  Hence

\[
 90+2(222)=534
\]

old turns are removed.  The seed now has

\[
 10152-312=9840\text{ edges},\quad
 4928-534=4394\text{ turns},\quad
 5224+312=5536\text{ components}.
\]

Using the same 1,535 unused rank-seven vertices requires 5,535 joins and
7,070 new edges.  The corrected ear-count ledger is

\[
 (x_1,x_2,x_3,x_4)=(4336,905,252,42).
\]

Indeed,

\[
\begin{aligned}
 \sum x_i&=5535,\\
 x_2+2x_3+3x_4&=1535,\\
 x_1+2x_2+3x_3+4x_4&=7070.
\end{aligned}
\]

The naive ear-turn count is 12,605.  Each isolated component contributes
one fewer turn than the nontrivial-component formula, so the actual number
of new turns is

\[
 12605-90=12515.
\]

Consequently all scalar rows close exactly:

\[
\begin{aligned}
 9840+7070&=16910 &&\text{rank-eight edge windows},\\
 4394+12515&=16909 &&\text{rank-nine turns},\\
 7070&=(2224+312)+4534 &&\text{rank-six colours plus repeats}.
\end{aligned}
\]

## 5. Scope

This theorem closes only the vertex-disjoint cut-exposure gate.  It does not
select the 5,535 ears, prove their rank-eight/rank-nine palettes fresh, order
the prefix blocks, cover ranks 10 through 17, or certify a length-24313
universal word.

## 6. Frozen artifacts

* optimizer: `scratch/search_k17_gk_min_vertex_disjoint_cuts_20260731.py`
* immutable certificate:
  `scratch/k17_gk_cut312_certificate_30e0812da947f999_20260731.json`
* dependency-free replay:
  `scratch/audit_k17_gk_cut312_certificate_20260731.py`
* replay payload: `scratch/k17_gk_cut312_audit_20260731.json`
* retained solver transcript: `scratch/k17_gk_cut312_search_20260731.log`

The immutable certificate SHA-256 is

```text
30e0812da947f999a5c6d91ca52c323c7ca25302c127daf3434262faed9e9474
```

and the replay payload hash is

```text
ae19f799a6ba6af49e5e2e7b27928ba80359275b4c4ab0a4f027c2ab1b2d7896
```
