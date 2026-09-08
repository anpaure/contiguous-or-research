# K17 `final2397`: exact flat-depth-three source obstruction and scoped lower-DM relaxation

**Date:** 2026-08-02  
**Lane:** AD  
**Status:** fixed-factor flat-source no-go proved; exact original lower compiler not reached; an explicitly optimistic envelope-only Hall/DM relaxation is audited

## 1. Frozen input and scope

The fixed factor is

```text
/home/amodo/or15/work/root_k17_c68b_c6xc6_20260802/
  greedy_residence/after_c10c12_2414_single/final2397.factor.tsv
SHA-256 eba52226952cda38d74e98fc7463f54640b0b59736ff88fc2949c8f0c02de1eb
```

Its sparse quotient model is `round003.model`, SHA-256
`9aa9c8137b4b90508aa255536a6f683bfa448b60de497b498f7119e432eb24ec`.
Independent lineage replay regenerated the factor byte for byte.  The strict
five-column factor audit gives:

```text
physical edges                         24,310
distinct rank-8 facets                 24,310, each once
distinct rank-9 owners                 24,310, each degree two
rank-10 caps                           19,448, all covered
protected edges                         3,944
physical components                         1
```

The factor row order is not chronology.  The canonical physical cycle starts
at the least owner `511`, takes its lesser neighbour `8639`, and thereafter
takes the unique nonprevious neighbour.  This agrees row for row with the
independent owner-cycle artifact.

The cap and protected-edge checks above authenticate the supplied factor.
They are not hypotheses used in the source obstruction.  In particular, the
argument below neither assumes residence nor assumes upper completeness.
The already authenticated cyclic upper holes are `1938,408,0` at ranks
`11,12,13`; they play no role here.

## 2. Exact maximal-antecedent theorem

Fix either orientation and cut the owner cycle to obtain

\[
T_0,T_1,\ldots,T_{W-1},\qquad W={17\choose9}=24310.
\]

A nonzero flat depth-three source is a word

\[
A_0,A_1,\ldots,A_{W+2}\ne\varnothing
\]

such that

\[
T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}
\quad(0\le i<W).                                      \tag{2.1}
\]

Define the clipped maximal envelope

\[
P_p=\bigcap_{i=\max(0,p-3)}^{\min(W-1,p)}T_i
\quad(0\le p<W+3).                                    \tag{2.2}
\]

### Theorem 2.1 (maximal flat antecedent, exact quantifiers)

A nonzero source satisfying (2.1) exists if and only if

\[
P_p\ne\varnothing\quad(0\le p<W+3)                    \tag{2.3}
\]

and

\[
T_i=P_i\cup P_{i+1}\cup P_{i+2}\cup P_{i+3}
\quad(0\le i<W).                                      \tag{2.4}
\]

When it exists, `P` is the unique pointwise-largest source.

#### Proof

If `A` satisfies (2.1), then every letter `A_p` lies in every row whose
window contains `p`; hence `A_p subseteq P_p`.  Therefore

\[
T_i=\bigcup_{p=i}^{i+3}A_p
   \subseteq\bigcup_{p=i}^{i+3}P_p
   \subseteq T_i.
\]

Both inclusions are equalities and nonempty `A_p` implies (2.3).  Conversely,
if (2.3)--(2.4) hold, taking `A=P` gives a nonzero source.  The first
containment proves pointwise maximality.  ∎

This theorem is an exact source test, not merely a residence heuristic.

## 3. Short-run cut characterization and a two-run certificate

For one coordinate `x`, inspect its binary trace along the linear owner
sequence.  Formula (2.2) is Boolean erosion by four owner rows, with clipped
ends.  Thus an internal positive run of length at most three contributes no
`x` to any envelope position serving that run, whereas a positive run of
length at least four is restored.  A positive run meeting a linear endpoint
is restored by the clipped envelope.

Consequently, for a cyclic positive run

\[
0,1^\ell,0,\qquad 1\le\ell\le3,                        \tag{3.1}
\]

let `B(R)` be the `ell+1` cycle edges from the edge immediately before the
run through the edge immediately after it.  A cut makes this run harmless if
and only if the cut lies in `B(R)`.  Hence a flat source exists only if

\[
\bigcap_{R\text{ a cyclic short positive run}}B(R)\ne\varnothing. \tag{3.2}
\]

For `final2397` the short positive-run census is

```text
length 1       0
length 2   1,292
length 3   1,105
total      2,397.
```

Two coordinate-zero runs already give a minimal no-cut certificate:

| start | trace owners `0 ; 1,1,1 ; 0` | admissible cut edges |
|---:|---|---|
| 199 | `101166 ; 101165,102157,109837 ; 109838` | `{198,199,200,201}` |
| 294 | `128112 ; 62577,62569,64553 ; 64808` | `{293,294,295,296}` |

The two edge sets are disjoint.  Every cut fails at least one of these two
runs, so every linear opening fails Theorem 2.1 in both orientations.  One
run alone can always be clipped, so this certificate is cardinality-minimal.

The exhaustive all-cut replay independently agrees:

```text
cuts tested                                      24,310
flat-D3 exact cuts                                    0
internal short runs after a cut        2,395 / 2,396 / 2,397
number of cuts in those classes             561 / 7,174 / 16,575
```

The diagnostic cut is selected lexicographically by the number of mismatched
rows, then missing row-bit incidences, then internal short runs, then edge
number.  It is edge `77`, between owners `119506` and `103126`.  Its maximal
erosion has no empty letter but gives

```text
source positions                                24,313
owner rows restored exactly                     18,621
owner rows not restored                          5,689
lost owner-bit incidences                        5,893
internal short runs                              2,395.
```

This proves the fixed-factor flat-depth-three source no-go.  It does not rule
out changing the factor, a nonflat source, or a generalized P/Q retiming.

## 4. Exact lower incidence after a source-passing cut

For clarity, the exact compiler formulation that would apply to a future
source-passing chronology is recorded here.

Let `P` be its maximal source and protect every owner row
`I_i=[i,i+3]`.  Every strict-lower target is a nonempty mask

\[
S\subseteq[17],\qquad |S|\le8,                          \tag{4.1}
\]

so there are `65,535` left vertices.  A lower occurrence cannot contain four
consecutive source positions: that would contain a complete rank-nine owner
row.  Thus the complete occurrence-labelled right catalogue consists of

\[
C=[s,s+\ell),\qquad 1\le\ell\le3,                      \tag{4.2}
\]

and has

\[
(W+3)+(W+2)+(W+1)=72,936                               \tag{4.3}
\]

cells.

For a cell `C`, put

\[
O_C=\bigcup_{p\in C}P_p,                               \tag{4.4}
\]

and for every protected row-bit `(i,b)` put

\[
H_{i,b}=\{p\in[i,i+3]:b\in P_p\}.                     \tag{4.5}
\]

Define

\[
M_C=\{b:\text{some nonempty }H_{i,b}\subseteq C\}.    \tag{4.6}
\]

Then capping `P_p` to `P_p cap S` on `C` is a literal nonzero occurrence of
`S` that preserves every owner row if and only if

\[
S\subseteq O_C,\qquad M_C\subseteq S,\qquad
P_p\cap S\ne\varnothing\quad(p\in C).                 \tag{4.7}
\]

Indeed, the first and third conditions make the cell OR exactly `S` and keep
each letter nonempty.  A protected bit is erased precisely when all its hosts
are captured by `C` and it is absent from `S`, which is exactly the failure of
the middle condition.

A compiler therefore needs a left-perfect matching in this incidence graph.
For a maximum matching, alternating reachability from exposed left vertices
(unmatched `L->R`, matched `R->L`) gives the canonical Hall shore
`(Z_L,Z_R)` with

\[
Z_R=N(Z_L),\qquad |Z_L|-|Z_R|=65535-|M|.               \tag{4.8}
\]

Contracting matching edges and taking SCCs of the remaining directed
nonmatching edges gives the DM blocks.  A left-perfect matching is still only
`PASS_MARGINAL_HALL`: simultaneous cap compatibility must be replayed on the
decoded word.  Failure of one selected matching is not an UNSAT certificate.

Because `final2397` has no source-passing cut, its exact graph (4.7) is
**undefined/not reached**.  No exact lower-compiler deficiency is claimed.

## 5. Optimistic envelope-only relaxation

To continue after the source failure, the audit uses the best-cut envelopes
and deliberately drops (4.6).  Its relaxed edge condition is only

\[
S\subseteq O_C,qquad P_p\cap S\ne\varnothing\ (p\in C). \tag{5.1}
\]

Thus every carrier constraint that an exact protected-row graph would impose
has been removed.  The complete relaxed graph has

```text
left masks                                      65,535
short cells                                     72,936
incidences                                  10,199,999
zero rows                                        3,463
maximum matching                                57,778
matching deficiency                              7,757
canonical Hall shore                       25,488 / 17,731
minus shore                                28,954 / 44,112
balanced core                              11,093 / 11,093
weak components                                  3,464
contracted DM SCCs                              57,414.
```

The shore identity is exact:

\[
25488-17731=7757=65535-57778.                   \tag{5.2}
\]

The DM SCC defect histogram is

```text
-1 : 15,158
 0 : 34,499
+1 :  7,757.
```

All `3,463` degree-zero rows have rank eight and fail already at the support
test: no length-at-most-three envelope union contains them.  Their exact
`C17` orbit anatomy is

```text
199 full zero orbits
  5 orbits with 16 of 17 rotations zero.
```

The five punctured representatives and their unique nonzero rotations are

```text
5783  -> 115410
5931  -> 117442
12879 -> 37830
18795 -> 37590
19283 -> 103124.
```

This is a structural description of the relaxation, not a new universal-word
no-go.  In particular, exactly `85` of its zero masks already occur as
length-four eroded rows (five full rotation orbits with representatives
`1405,2795,4287,6543,18859`).  Those length-four rows could not be lower in a
valid rank-nine chronology, but they demonstrate why the broken surrogate
must not be mistaken for the original compiler face.

## 6. Reproducibility and independent audit

The fail-closed implementation is

```text
scratch/audit_ad_k17_final2397_source_lower_dm_20260802.cpp
SHA-256 b352aa6004e5cb985edeee25a67f2c1b8a0ddd5737ce59088ff81766ea5c3448
```

It was compiled on x86-64 H100 host CPU with GCC 13.3.0 by

```text
g++ -std=c++20 -O3 -DNDEBUG -Wall -Wextra -pedantic \
  audit_ad_k17_final2397_source_lower_dm_20260802.cpp -o audit_final2397
```

The binary SHA-256 is
`51a7e04f98a560da7208a12c846c0d94867b8b4c28ee79123b6b7980f0bf1c5f`.
The full local package is

```text
scratch/ad_k17_final2397_source_lower_dm_v2_20260802/
```

with manifest SHA-256
`088814350b2bd2fb72d136930829767eb0b0b234cfa57c64fe9bd9021030f9a3`.
`sha256sum -c SHA256SUMS` passes all 20 entries.  The principal audit JSON has
SHA-256
`3d2c4c4a69b13b1ca714872568827b682bd194bf70c6f45f4824d27202c9689d`.

An independent code-and-output audit checked the canonical cycle, the
two-run certificate, all-cut/run identities, direct maximal erosion,
Hopcroft--Karp matching, both alternating shores, core balance, matching-edge
contraction, DM SCC membership, and all hashes.  It returned PASS with no
remaining semantic correction.

## 7. Exact boundary

What is proved:

1. the authenticated `final2397` factor has no literal nonzero flat `D^3`
   antecedent under any cut or either orientation;
2. the two displayed coordinate-zero runs are already a minimal certificate;
3. the exact lower-incidence/Hall/DM formulation is fixed for any future
   source-passing chronology;
4. the best-cut envelope-only relaxation has the exact zero/Hall/DM data in
   Section 5.

What is not proved:

1. no lower compiler theorem for `final2397`—that gate is not reached;
2. no obstruction to a residence-changing factor rethread, nonflat source,
   or generalized P/Q schedule;
3. no completion of ranks 11 and 12;
4. no common-cap compiler, universal word, or statement about `nu(17)`.

The constructive next gate is therefore upstream: change the chronology or
source model enough to eliminate the two-run intersection obstruction (and in
fact all internal short runs), then apply the exact graph (4.7), Hall/DM, and
finally simultaneous common-cap replay.  Optimizing the present fixed-cut
relaxation cannot repair the missing owner bits.
