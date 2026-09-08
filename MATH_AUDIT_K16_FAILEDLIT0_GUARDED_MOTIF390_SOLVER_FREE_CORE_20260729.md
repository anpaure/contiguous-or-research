# K16 FL0 guarded motif 390: solver-free local obstruction

Date: 2026-07-29

## 1. Scope and result

Let (Q) be the detector-zero, both-(q=1)-complete physical endpoint

```text
scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json
```

and let (R) be the fixed resident endpoint reconstructed from the frozen PBBS data.  Write

* (b_i\in\{0,1\}) for deletion of the (i)-th blue edge in the sorted list (Q\setminus R);
* (r_j\in\{0,1\}) for insertion of the (j)-th red edge in the sorted list (R\setminus Q).

At each middle vertex (v), exact degree two after switching is equivalent to

\[
   \sum_{j:\,v\in r_j} r_j=\sum_{i:\,v\in b_i} b_i.       \tag{D_v}
\]

The guarded core artifact contains eight lower-(q=1) rows, thirteen upper-(q=1) rows, and one residence-motif row.  The following statement is unconditional once those literal rows and the nine displayed degree equations below are accepted.

**Theorem 1 (solver-free motif-390 obstruction).**  There is no binary assignment satisfying:

1. the twenty-one normalized (q=1) rows in Table 1;
2. the nine degree equations in Table 2; and
3. the motif-390 condition
   \[
      b_{11795}+b_{11796}+b_{11821}\ge 1.                 \tag{M390}
   \]

Consequently there is no degree-balanced switch in the fixed catalogue (R\triangle Q) that preserves these twenty-one physical (q=1) colours and destroys motif 390.  In particular, there is no switch in this catalogue that preserves every lower and upper (q=1) colour and hits every inherited short-run motif.

This is a fixed-catalogue obstruction.  It is not an obstruction to a trade using an edge outside (R\cup Q).

## 2. Motif audit

Motif 390 is component 0, coordinate 2, start 8107, length 2.  Its four consecutive states and coordinate-2 bits are

```text
61994(0) -- 57902(1) -- 57998(1) -- 58250(0).
```

All four states have rank 8.  The three closure edges are Johnson edges and, in sorted blue indexing, are

```text
b11796 = (57902,61994)   incoming boundary, upper colour 61998
b11795 = (57902,57998)   internal edge,     lower colour 57870
b11821 = (57998,58250)   outgoing boundary, upper colour 58254.
```

Thus destroying this exact length-2 run requires (M390).

## 3. Exact normalization of the twenty-one guarded palette rows

Every listed colour has base load one in (Q), exactly one blue provider in (Q\setminus R), and either zero or one red provider in (R\setminus Q).  Hence its guarded coverage inequality is exactly (b_i=0) when there is no red provider, or (b_i\le r_j) when there is one.

### Table 1

| row | normalized inequality | blue edge | red edge, if any |
|---|---:|---|---|
| (L_{18526}) | (b_{4006}=0) | (18558,26718) | none |
| (L_{47652}) | (b_{10117}\le r_{10025}) | (47660,47780) | (47908,64036) |
| (L_{51230}) | (b_{10718}\le r_{10650}) | (51358,59422) | (51262,59422) |
| (L_{57614}) | (b_{11849}=0) | (58126,58638) | none |
| (L_{57870}) | (b_{11795}\le r_{11797}) | (57902,57998) | (57871,59918) |
| (L_{57894}) | (b_{11827}\le r_{11806}) | (58022,59942) | (57902,61990) |
| (L_{59406}) | (b_{12127}\le r_{12057}) | (59918,63502) | (59422,60430) |
| (L_{61988}) | (b_{12319}\le r_{12345}) | (61990,62052) | (61989,64036) |
| (U_{27742}) | (b_{5891}=0) | (26718,27678) | none |
| (U_{47645}) | (b_{9749}=0) | (45597,47644) | none |
| (U_{47676}) | (b_{10030}\le r_{9991}) | (47164,47660) | (47644,47668) |
| (U_{47772}) | (b_{3328}=0) | (15004,47644) | none |
| (U_{58254}) | (b_{11821}\le r_{10338}) | (57998,58250) | (50062,58126) |
| (U_{59486}) | (b_{12037}\le r_{5686}) | (59422,59478) | (26718,59478) |
| (U_{59950}) | (b_{12126}\le r_{10798}) | (59918,59948) | (51758,59942) |
| (U_{61998}) | (b_{11796}\le r_{11806}) | (57902,61994) | (57902,61990) |
| (U_{62118}) | (b_{9796}=0) | (45734,61990) | none |
| (U_{62222}) | (b_{9815}\le r_{11867}) | (45838,58126) | (58126,62214) |
| (U_{64038}) | (b_{11579}=0) | (55846,59942) | none |
| (U_{64044}) | (b_{12455}\le r_{9993}) | (64036,64040) | (47660,61996) |
| (U_{65060}) | (b_{12456}=0) | (64036,65028) | none |

Direct intersection/union checks give the displayed lower/upper colour for every provider edge.

## 4. Only nine degree sockets are needed

The proof below uses the following nine instances of (D_v), and no other degree row:

### Table 2

\[
\begin{aligned}
D_{47644}:&\quad r_{8352}+r_{9991}=b_{3328}+b_{9749},\\
D_{61990}:&\quad r_{9710}+r_{11806}=b_{9796}+b_{12319},\\
D_{64036}:&\quad r_{10025}+r_{12345}=b_{12455}+b_{12456},\\
D_{47660}:&\quad r_{9960}+r_{9993}=b_{10030}+b_{10117},\\
D_{59918}:&\quad r_{10793}+r_{11797}=b_{12126}+b_{12127},\\
D_{59942}:&\quad r_{10798}+r_{12168}=b_{11579}+b_{11827},\\
D_{26718}:&\quad r_{5685}+r_{5686}=b_{4006}+b_{5891},\\
D_{59422}:&\quad r_{10650}+r_{12057}=b_{10718}+b_{12037},\\
D_{58126}:&\quad r_{10338}+r_{11867}=b_{9815}+b_{11849}.
\end{aligned}
\]

All variables are binary, so throughout the proof an equality such as (1+x=y\) with (x,y\in\{0,1\}) forces (x=0,y=1).

## 5. The common tail

Define

\[
\mathcal T=\{L_{47652},L_{61988},U_{47645},U_{47676},
U_{47772},U_{62118},U_{64044},U_{65060}\}.
\]

**Lemma 2 (tail lock).**  Under the rows in (mathcal T), (r_{11806}=1) is impossible.

**Proof.**  The rows (U_{47772}) and (U_{47645}) give (b_{3328}=b_{9749}=0).  Equation (D_{47644}) then gives (r_{9991}=0), and (U_{47676}) gives (b_{10030}=0).  Also (U_{62118}) and (U_{65060}) give (b_{9796}=b_{12456}=0).

Assume (r_{11806}=1).  Equation (D_{61990}) forces (b_{12319}=1).  Row (L_{61988}) forces (r_{12345}=1).  Equation (D_{64036}) then forces

\[
   b_{12455}=1,\qquad r_{10025}=0.
\]

Row (U_{64044}) forces (r_{9993}=1).  Equation (D_{47660}), using (b_{10030}=0), forces (b_{10117}=1).  Finally (L_{47652}) requires (b_{10117}\le r_{10025}=0), a contradiction.  \(\square\)

## 6. The three closure-edge branches

**Proof of Theorem 1.**  By (M390), at least one closure edge is deleted.

### Branch I: (b_{11796}=1)

Row (U_{61998}) gives (r_{11806}=1), contradicting Lemma 2.

### Branch II: (b_{11821}=1)

Row (U_{58254}) gives (r_{10338}=1), while (L_{57614}) gives (b_{11849}=0).  Equation (D_{58126}) forces

\[
   b_{9815}=1,\qquad r_{11867}=0,
\]

contradicting (U_{62222}: b_{9815}\le r_{11867}).

### Branch III: (b_{11795}=1)

Row (L_{57870}) gives (r_{11797}=1).  Equation (D_{59918}) therefore gives

\[
   b_{12126}+b_{12127}\ge1.                              \tag{1}
\]

If (b_{12126}=1), then (U_{59950}) gives (r_{10798}=1).  Since (U_{64038}) gives (b_{11579}=0), equation (D_{59942}) forces (b_{11827}=1).  Row (L_{57894}) gives (r_{11806}=1), contradicting Lemma 2.

It remains to take (b_{12126}=0).  By (1), (b_{12127}=1), and (L_{59406}) gives (r_{12057}=1).  Rows (L_{18526}) and (U_{27742}) give (b_{4006}=b_{5891}=0); equation (D_{26718}) gives (r_{5686}=0); and (U_{59486}) gives (b_{12037}=0).  Equation (D_{59422}) now forces

\[
   b_{10718}=1,\qquad r_{10650}=0,
\]

contradicting (L_{51230}:b_{10718}\le r_{10650}).

All branches are impossible.  \(\square\)

The proof does not require the three cases to be exclusive: Branch III already rules out (b_{11795}=1), Branch I rules out (b_{11796}=1), and Branch II rules out (b_{11821}=1).

## 7. Leaf sets and the conditional 147-transversal calculation

Retain (M390), and consider only changes to guarded (q=1) rows.  The four contradiction leaves used above have row sets

\[
\begin{aligned}
\mathcal A&=\{L_{57870},U_{59950},U_{64038},L_{57894}\}\cup\mathcal T,
&&|\mathcal A|=12,\\
\mathcal B&=\{L_{57870},L_{59406},L_{18526},U_{27742},U_{59486},L_{51230}\},
&&|\mathcal B|=6,\\
\mathcal C&=\{U_{61998}\}\cup\mathcal T,
&&|\mathcal C|=9,\\
\mathcal D&=\{U_{58254},L_{57614},U_{62222}\},
&&|\mathcal D|=3.
\end{aligned}
\]

Here (mathcal A) and (mathcal B) are the two subleaves of the internal-edge branch, (mathcal C) is the incoming-boundary branch, and (mathcal D) is the outgoing-boundary branch.  Their relevant intersections are

\[
  \mathcal A\cap\mathcal B=\{L_{57870}\},\qquad
  \mathcal A\cap\mathcal C=\mathcal T,\qquad
  \mathcal B\cap\mathcal C=\varnothing,
\]

and (mathcal D) is disjoint from the other three.

It follows that a (q=1)-row set intersecting all four leaf certificates has size at least three.  Every minimum such set consists of

1. one row (d\in\mathcal D); and
2. either ({L_{57870},c\}) with (c\in\mathcal C), or ({t,b\}) with (t\in\mathcal T) and (b\in\mathcal B).

There are

\[
   3\bigl(9+8\cdot6-8\bigr)=147
\]

distinct minimum row transversals; the subtraction removes the eight duplicate pairs ({L_{57870},t\}), (t\in\mathcal T).

This is a proof-certificate transversal, conditional on keeping (M390) and leaving the nine degree sockets unchanged.  It is **not** a minimum physical edge-expansion theorem.  For existence of one repair, invalidating one leaf may be enough; one need not invalidate all four leaves.

## 8. Exact eligibility halo and catalogue caveat

Besides changing a palette/provider row, an enlarged catalogue can evade this proof by changing the support of one of its degree equations.  The degree-socket halo is

\[
\{47644,61990,64036,47660,59918,59942,26718,59422,58126\}.
\]

Therefore the rigorous persistence statement is:

> If an enlarged move library leaves the literal semantics of all rows in a given leaf unchanged and adds no eligible red or blue variable incident to any degree socket used by that leaf, then that leaf contradiction persists verbatim.

Conversely, merely touching one row or socket invalidates this proof but does not by itself construct a legal alternating circulation.  Endpoint incidence, the second endpoint of every new edge, all other (q=1) colours, and residence of newly created runs still have to be checked.  No claim of a minimal physical augmentation is made here.

The frozen artifact reports that deleting any one of the 22 assumptions makes the fixed model `OPTIMAL` in replay, with no `UNKNOWN` replay.  This establishes solver-backed assumption irredundancy for that exact model.  The artifact does not export the 22 corresponding literal witnesses, so those feasibility statements are not promoted here to solver-free constructions.

## 9. Frozen provenance

```text
guarded core JSON
2f8031fff879faf42b80a169aee2f0a0f5a2484987c5fe625c20fc5bf945c238
scratch/k16_failedlit0_guarded_q1_motif_core_20260729.json

FL0 q1 endpoint
17bd05a0bb0da228e580d65bdec27ce04589072baecb8575e0623fc4ea4343b8
scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json
internal endpoint digest: a40a8470b11e9d9e0546c8077e9be14de93f69af9cb3b784a4fedd0980505abf

FL0 source report
2b0172c1acdd526624f1f82bf4b22c44272b3644e05bd627b236eb0182d99aa4
scratch/k16_fl2_r23_bestpair_probe_20260729.json

resident endpoint
d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951
scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json

PBBS base
8955fc7babdfc37698f51115fad2737fb4dd09c2c3a2f387f02ac690154f460f
scratch/k15_pbbs_trade_baseline.json

B certificate
91c434654d38466790dd373d26ff4e88f115d7cab1c29f71520a99cc4b349985
scratch/k16_pbbs_component_trade_27_factor_20260729.json

A cycles
bc58e466e72c0b418aa24929d45640dcfe6ffbe567caae480939e76367533738
scratch/k15_two_component_a_cycles_20260729.json

core extractor
d33167c29d0d52b437e9c755419c7aeb1b41e0f27d329b40683b5c173b07d974
scratch/extract_k16_overlay_motif_only_min_core_20260729.py

exported model
84a5da06bd8f9eb67fe5412925a6a9dbf4f248eeb065b33d50082bf557aff39f
scratch/k16_failedlit0_guarded_q1_motif_core_20260729.model.pb

solver-free human-branch replay script
d545ed1abe07d3b09f3437d6791ee3badfb419451288893ede1a822fc878f8cc
scratch/audit_k16_failedlit0_motif390_branch_cores_20260729.py

solver-free human-branch replay output (status PASS)
70fd8101aac580b90a4add44213278920f0eb834265f4f0ad32146cacfb74033
scratch/k16_failedlit0_motif390_branch_cores_20260729.audit.json
```

The hashes embedded in the guarded-core JSON agree with the independently recomputed source hashes above.
