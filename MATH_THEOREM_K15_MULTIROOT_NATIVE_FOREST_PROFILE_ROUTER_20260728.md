# Multi-root native forests and the exact Hall-20 to Hall-19 profile router

Date: 2026-07-28

Status: abstract matching theorem plus a search-free application to the frozen
`k=15` carrier chain.  This proves one exact Hall-rank descent.  It does **not**
produce a common compiler for all lower targets, a length-6438 covering word,
or a proof that `nu(15)=6438`.

## 1. Compiler graphs and their positive DM shore

Let `G=(L,R,E)` be an occurrence-labelled compiler graph.  The left vertices
are lower targets and the right vertices are physical short-interval cells;
two cells with identical contents remain different right vertices.  Put

\[
       \operatorname{def}(G)=|L|-\nu(G),
\]

where `nu(G)` is the maximum matching size.

Fix a maximum matching and start alternating searches at its unmatched left
vertices.  Write `L+` and `R+` for the reached left and right vertices.  The
connected components of \(G[L^+\cup R^+]\) are the positive
Dulmage--Mendelsohn (DM) components.

### Lemma 1.1 (DM direct sum)

If the positive components have shores `(X_i,Y_i)`, then

\[
 \operatorname{def}(G)
   =|L^+|-|R^+|
   =\sum_i\bigl(|X_i|-|Y_i|\bigr).                 \tag{1.1}
\]

The chosen maximum matching saturates the left vertices outside \(L^+\), and
the matching rank of a positive component is \(|Y_i|\).

#### Proof

Alternating reachability gives `N(L+) = R+`.  Each reached right vertex is
matched to a reached left vertex, while every reached left vertex except an
alternating-search root is matched inside the same reached component.
Consequently a component of shores `(X_i,Y_i)` has matching rank `|Y_i|` and
gap `|X_i|-|Y_i|`.  The restriction of the fixed maximum matching to the
unreached vertices saturates \(L\setminus L^+\).  Adding the component matchings
gives

\[
 \nu(G)=|L\setminus L^+|+\sum_i|Y_i|,
\]

which is (1.1).  This also proves that the decomposition is a genuine rank
direct sum, rather than only a count of Hall witnesses.  \(\square\)

## 2. Multi-root native forests

Fix one physical controller word `Q`.  If cell `c` is a right vertex, let
`tr_Q(c)` be the OR of `Q` on the occurrence interval represented by `c`.

### Definition 2.1

A pair \((X,Y)\) is an \(s\)-root native forest under \(Q\) if there is a set
\(\Omega\subseteq X\), \(|\Omega|=s\), such that

1. `|X|=|Y|+s`;
2. \(c\mapsto\operatorname{tr}_Q(c)\) is a bijection from \(Y\) onto
   \(X\setminus\Omega\); and
3. every displayed pair `(tr_Q(c),c)` is an incidence edge.

The elements of \(\Omega\) are the exposed native roots.  The word *forest* is
a name for this simultaneous pin family; it does not assert that the full
incidence component is an acyclic graph.

### Lemma 2.2 (native rank and roots)

An `s`-root native forest has matching rank `|Y|=|X|-s`, witnessed by its
native pins.  If it is a positive DM component, its contribution to global
deficiency is exactly `s`.

This follows immediately from Definition 2.1 and Lemma 1.1.

### Theorem 2.3 (gap-preserving forest fusion)

Suppose two disjoint positive components of a graph `G_0` are native forests
`(X_1,Y_1,Omega_1)` and `(X_2,Y_2,Omega_2)`.  Suppose a literal carrier move
produces `G_1` in which

* their target shore is exactly \(X_1\sqcup X_2\);
* their replacement right shore has size `|Y_1|+|Y_2|`;
* its native traces are exactly
  \((X_1\cup X_2)\setminus(\Omega_1\cup\Omega_2)\); and
* every other positive component has the same target shore and gap.

Then the replacement is an `(s_1+s_2)`-root native forest and

\[
                 \operatorname{def}(G_1)
                 =\operatorname{def}(G_0).          \tag{2.1}
\]

It may be connected even when the two old forests were separate.  Thus a
neutral move can change the component geometry and physical chronology
without paying or gaining matching rank.

#### Proof

The first three hypotheses give a bijection from the replacement right shore
to the union target shore with precisely `s_1+s_2` omitted roots.  Lemma 2.2
gives the same total gap as the two old components.  All other terms in the
DM direct sum (1.1) are unchanged.  \(\square\)

## 3. A profile router can discharge a remote component

For a target block `X`, the restricted profile of a physical cell `c` is
`N(c) intersect X`, with physical multiplicity retained.  A *profile router*
is a matching-neutral move which changes component geometry or physical row
placement while leaving the restricted profile multiset of some other
positive component unchanged.

### Theorem 3.1 (remote-discharge/direct-sum criterion)

Let `G_0 -> G_1 -> G_2` be literal compiler moves on the same target universe.
Assume:

1. `G_0 -> G_1` satisfies Theorem 2.3 and hence is matching-neutral;
2. `C=(X_C,Y_C)` is a positive DM component of `G_1` of gap `s`, and its
   target shore and restricted profile multiset are unchanged by the first
   move;
3. the positive DM shore of `G_2` is obtained from that of `G_1` by deleting
   `C`, with all surviving component target shores and gaps unchanged; and
4. in `G_2`, the target block `X_C` has a matching of size `|X_C|` (equivalently,
   `C` has moved to the saturated side of the DM decomposition).

Then

\[
 \nu(G_2)=\nu(G_1)+s,
 \qquad
 \operatorname{def}(G_2)=\operatorname{def}(G_1)-s. \tag{3.1}
\]

The gain is *remote*: the forest fused by the first move may survive unchanged
in the final positive shore, while `C` is the component discharged.

#### Proof

By Lemma 1.1, `C` contributes exactly `s` to the deficiency of `G_1`.
Hypothesis 3 removes precisely this summand and changes no other summand.
Hypothesis 4 is the local saturation certificate explaining why the block is
absent from the final positive shore.  Applying (1.1) to both endpoints gives
(3.1).  \(\square\)

There is also a useful row-level certificate for Hypothesis 4.  Cancel a
multiset of identical physical restricted profiles between the two endpoint
graphs.  If the retained common bank has a fixed matching of rank `mu` and
the contracted exceptional banks have ranks `b` and `b+s`, with their matched
left and right vertices disjoint from that common matching, then their union
has ranks `mu+b` and `mu+b+s`.  The disjointness clause is essential: scalar
profile counts alone do not imply a rank sum.

## 4. Exact application at `k=15`

The frozen states are

```text
X20      scratch/k15_segment_braid_hall20_zero6.json
X20merge scratch/k15_h20_h19_root8216_chain/router/candidate_0000.json
X19      scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
```

and the literal moves are

\[
 X_{20}\xrightarrow{\operatorname{RF}(180,2764,4210)}
 X_{20}^{\rm merge}
 \xrightarrow{\operatorname{FR}(123,722,4710)}X_{19}.       \tag{4.1}
\]

Two independent, search-free checkers reconstruct all three incidence graphs:

```text
scratch/audit_k15_h20_h19_profile_router_theorem.py
scratch/audit_k15_h19_root8216_chain_independent.py
```

Both report `PASS`.

### 4.1 The neutral multi-root forest

In `X20`, the positive shore contains the disjoint native bases

\[
 (161/160)_{8217},\qquad (160/159)_{8218}.          \tag{4.2}
\]

The first braid replaces them by one connected native forest

\[
             (321/319)_{\operatorname{core}=8216},           \tag{4.3}
\]

whose exposed native roots are exactly `{8217,8218}`.  Its target shore is
the disjoint union of the two old target shores.  The other eighteen positive
components retain their target sets.  Therefore Theorem 2.3 proves that the
Hall deficiency stays 20.

The physical change is nontrivial.  Of the 319 restricted profiles, 317 are
common.  The two old-only profiles are

```text
{8218,8222,8282,8286,9242,9246,9306,9310}
{8219,8223,9243,9247}
```

and the two new-only profiles are

```text
{8282,8286,9306,9310}
{8218,8219,8222,8223,9242,9243,9246,9247}.
```

Thus this is a literal profile router, not an identity move.

### 4.2 The remote rank-one discharge

The component actually discharged by the second braid is the disjoint old
component

\[
                         C_{24610}:161/160.                    \tag{4.4}
\]

The first braid leaves its complete restricted profile multiset unchanged.
The forest (4.3) survives in `X19` with gap two.

On the fixed 161-target shore of (4.4), the second braid changes

```text
old physical neighbourhood: 160 cells, rank 160
new physical neighbourhood: 162 cells, rank 161.
```

After cancelling 159 common profiles, the profile surgery is

\[
 \{26146,26402\}
 \quad\longmapsto\quad
 \{24610,25634\}\sqcup\{26146\}\sqcup\{26402\}.    \tag{4.5}
\]

The profile `{24610,25634}` already had one physical occurrence, so (4.5)
creates its second copy.  One explicit four-target part of a full restricted
matching is

```text
24610 -> cell 1212
25634 -> cell 4713
26146 -> cell 11150
26402 -> cell 17586.
```

The final 162-cell neighbourhood is disjoint from the final positive-DM right
shore.  Hence (4.4) is fully saturated in the final graph, while every
surviving positive component has its old target shore and gap.  Theorem 3.1
with `s=1` gives

\[
             16363\longmapsto16364,
 \qquad      H20\longmapsto H19.                              \tag{4.6}
\]

The independent complete-profile contraction gives the same direct sum:
the common bank has rank 16343 and the exceptional boundary ranks are 20 and
21.

## 5. Exact common-`Q` lift on the former Hall-20 shore

The final positive shore has `516/497` vertices and 18 components.  Seventeen
have gap one; (4.3) has gap two.  Under one maximal erosion controller, the
497 physical right cells have pairwise distinct native traces equal exactly
to the 516 shore targets minus the 19 exposed roots.  Thus all 18 components
are native forests simultaneously under one `Q`.

The stronger frozen audit

```text
scratch/audit_k15_h20_h19_exposed_roots_common_q.py
scratch/k15_h20_h19_exposed_roots_common_q_certificate.json
```

checks the former 677-target Hall-20 critical shore.  This shore is the
disjoint union of the final 516-target positive shore and the discharged
161-target component (4.4).  In the final physical bank, native target 25634
has two cells, 1212 and 4713.  Shrinking **either one** from controller value
25634 to the exposed root 24610 leaves the other copy for 25634 and preserves

* all 497 native pins of the final positive shore;
* all 160 non-root native pins of the discharged component;
* one new literal pin of root 24610;
* every central carrier window; and
* non-emptiness of every controller cell.

Consequently one common modified controller realizes

\[
                       497+160+1=658                         \tag{5.1}
\]

simultaneous pins on the former 677-target shore, leaving exactly its 19
forest roots.  Both choices of the duplicate 25634 cell pass 3,573 explicit
survival-witness checks.  This is the literal common-`Q` realization of the
rank-one remote discharge, not merely an incidence matching.

After reserving these 497 literal native pins, the residual **incidence**
graph has rank 15867, and

\[
                         497+15867=16364.                      \tag{5.2}
\]

Equation (5.2) is a matching-rank direct sum.  It is not a common-word
compiler theorem: the 15,867 exterior incidence pairs have not been shown to
be realized by that same controller word.  The literal theorem is (5.1),
shore-local on 658 pins, not a 16,364-pin common compiler.  Six lower targets
still have degree zero, the Hall deficiency is still 19, and no complete
length-6438 word follows from this note.

## 6. Reproducible evidence

Run only the lightweight frozen-certificate audits:

```bash
python3 scratch/audit_k15_h20_h19_profile_router_theorem.py
python3 scratch/audit_k15_h19_root8216_chain_independent.py
python3 scratch/audit_k15_h20_h19_exposed_roots_common_q.py
```

The expected state data are

```text
Hall deficiencies: 20,20,19
matching ranks:     16363,16363,16364
DM shores:          677/657,677/657,516/497
component counts:   20,19,18
lower holes:        [4,18,11,1,0,0,0] at all three states
upper holes:        zero at q=1,...,7 at all three states
zero targets:       six at all three states
```

The theorem identifies the exact mechanism behind the descent: neutral
two-root forest fusion is a legality/profile router, and a later braid uses a
duplicate common profile to discharge a *different* gap-one DM component.
