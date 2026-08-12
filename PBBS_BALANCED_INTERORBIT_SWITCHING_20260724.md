# Balanced inter-orbit switching after PBBS homomesy

Date: 2026-07-24

## Verdict

The PBBS coordinate-homomesy theorem does not by itself split the long
parenthesis orbits into wreaths.  It does, however, put the cycle factor in a
class which is exactly stable under a useful family of switches.  This note
proves the switch criterion, checks the published Hamilton-cycle gluing phase,
and gives exact switch certificates in the two smallest examples singled out
by the homomesy audit.

The concrete new results are:

1. an exact centered-incidence criterion for every alternating-cycle switch;
2. the observation that the Merino--Mütze--Namrata connector sequence is a
   sequence of **balanced pure merges** of PBBS orbits (in the regime where
   their glider connector theorem applies);
3. a three-switch balanced conversion of the PBBS factor of `KG(6,2)` into
   five wreaths;
4. a 43-switch balanced conversion of the PBBS factor of `KG(8,3)` into seven
   wreaths; and
5. a 45-switch conversion of the canonical PBBS factor of `KG(9,4)` into an
   all-depth-complete exact 14-wreath factor, using genuine balanced
   alternating 8-switches.

Every intermediate component in both certificates is point-regular.  The
second certificate has the structured form

\[
  2\text{ merges}+37\text{ one-component reorderings}
  +4\text{ balanced splits}.
\]

These finite certificates validate the proposed "merge first, split
differently" mechanism.  They do not prove the Wreath Conjecture.

There is an important distinction for the Boolean/odd-graph application.
`KG(2m+1,m)` has no 4-cycles, so the ordinary two-edge switches used in the
two certificates are unavailable there.  The shortest switches which stay
inside the space of exact odd-graph wreath factors are the balanced
alternating eight-switches already characterized in
`WREATH_SHADOW_SWITCH_AUDIT.md`.  The new `KG(9,4)` certificate shows that
the odd-graph move class can realize the merge--reorder--split mechanism in
the first nontrivial defective dimension.  It is a finite reachability
certificate, not an all-dimensional switching theorem.

## 1. Point-regular levels and centered incidence

Put

\[
 g=\gcd(n,k),\qquad M=\frac ng,\qquad s=\frac kg.
\]

For a family (or ordered path) `P` of `k`-sets, let

\[
 \iota(P)=\sum_{A\in P}{\bf1}_A\in\mathbb Z^n
\]

be its coordinate-incidence vector, and define its centered vector

\[
 \boxed{
 z(P)=\iota(P)-\frac{k|P|}{n}{\bf1}.
 }
 \tag{1.1}
\]

A cycle is point-regular exactly when `z(C)=0`.  In that case
`k|C|/n` is an integer.  Since `k/n=s/M` in lowest terms,

\[
 M\mid |C|.
 \tag{1.2}
\]

We call a point-regular cycle of length `ell M` a level-`ell` cycle.  The
validated PBBS homomesy theorem says that every parenthesis orbit is a
level-`ell` cycle for some positive integer `ell`.

## 2. General alternating-switch criterion

Let `F` be a 2-factor of `KG(n,k)` whose components are point-regular.  Let
`Z` be a simple even cycle whose edges alternate between `F` and
`E(KG(n,k))\F`, and set

\[
 F'=F\mathbin\triangle Z.
 \tag{2.1}
\]

Deleting the factor edges of `Z` cuts the touched old components into path
segments `P_1,...,P_r`.  The added edges merely sew these segments into the
new components of `F'`.

### Lemma 1 (balanced alternating-switch criterion)

A new component assembled from the segment index set `J` is point-regular if
and only if

\[
 \boxed{
 \sum_{j\in J}z(P_j)=0.
 }
 \tag{2.2}
\]

Consequently `F'` is point-regular componentwise if and only if (2.2) holds
for every new component.

### Proof

The new edges carry no vertices; they only change adjacency.  Hence the
incidence vector and length of the new component are respectively

\[
 \sum_{j\in J}\iota(P_j),\qquad
 \sum_{j\in J}|P_j|.
\]

Subtracting `(k/n)` times the second quantity from the first gives precisely
the left side of (2.2).  Its vanishing is exactly point regularity.  QED

This criterion is lossless: it is neither a sufficient approximation nor an
average over coordinates.

## 3. Ordinary two-edge switches

Suppose `F` contains the edges `ab` and `cd`, with four distinct vertices,
and `ac,bd` are Kneser edges.  Replacing

\[
 ab,cd\quad\hbox{by}\quad ac,bd
 \tag{3.1}
\]

is the symmetric difference with an alternating 4-cycle.

### Corollary 2 (merge versus split)

1. If `ab` and `cd` lie in different point-regular components, (3.1) merges
   those components.  The merged component is automatically point-regular.
2. If the removed edges lie in one component and the switch leaves one
   component, its vertex set is unchanged, so it is automatically
   point-regular.
3. If the switch splits one component into the two cyclic arcs `P,Q`, both
   new components are point-regular if and only if

   \[
     z(P)=0
     \quad\text{(equivalently, }z(Q)=0\text{)}.
     \tag{3.2}
   \]

In the split case (1.2) forces both arc lengths to be multiples of `M`.

The merge assertion is simply

\[
 z(C\cup D)=z(C)+z(D)=0.
\]

This is why all pure merges preserve the PBBS homomesy conclusion without
any additional coordinate calculation.

### Four-cut arc exchange

There is a similarly exact statement for exchanging arcs between two cycles.
Suppose `P` is an arc of `C`, `Q` is an arc of `D`, four boundary edges are
removed, and valid Kneser cross-edges produce

\[
 C'=(C\setminus P)\cup Q,\qquad
 D'=(D\setminus Q)\cup P.
\]

Then

\[
 z(C')=-z(P)+z(Q),\qquad z(D')=z(P)-z(Q).
\]

Therefore the exchange is balanced exactly when

\[
 \boxed{z(P)=z(Q).}
 \tag{3.3}
\]

If the arc lengths differ, (3.3) also forces their difference to be a
multiple of `M`; the two component levels change by opposite integers.

## 4. The published PBBS-to-Hamilton gluing is balanced

In the glider regime `n>=2k+3`, Merino, Mütze and Namrata start from the PBBS
cycle factor.  Their Lemma 34 first joins the `g` single-glider cycles by
`g-1` edge-disjoint alternating 4-cycles; these are pure merges.  They then
contract that joined family to the distinguished node `D` and choose
edge-disjoint alternating 4-cycle connectors indexed by a spanning tree of
their auxiliary graph.  Their final Hamilton cycle is the symmetric
difference of the factor with both connector families; see the proof of their
Theorem 1, specifically the spanning-tree construction preceding the final
symmetric difference.

The connectors may be applied in any tree-edge order.  Every prefix of a
tree is a forest, so the next tree edge joins two distinct current forest
components.  Thus every connector is a pure merge in the sense of Corollary
2.  It follows that:

### Corollary 3

Every intermediate component in the Merino--Mütze--Namrata PBBS gluing
sequence is point-regular.  More precisely, if it is the union of PBBS orbits
of levels `ell_1,...,ell_t`, then it has length

\[
 (\ell_1+\cdots+\ell_t)M
\]

and every ground point occurs

\[
 (\ell_1+\cdots+\ell_t)s
\]

times.

This does not make their Hamilton cycle directly splittable into wreaths, but
it supplies a rigorously balanced "merge" half of a merge--reorder--split
program.  The statement concerns their 4-cycle connector construction, not
the separately handled sparse cases.

Primary source: A. Merino, T. Mütze and Namrata, *Kneser graphs are
Hamiltonian*, [arXiv:2212.03918v4](https://arxiv.org/abs/2212.03918).

## 5. Critical-diagonal peeling

Assume

\[
 n=(2s+1)g,\qquad k=sg,
 \]

so `M=2s+1`.  The PBBS homomesy audit proves that every point-regular
length-`M` Kneser cycle is a wreath.

Let a level-`ell` point-regular cycle contain a contiguous arc `P` of length
`M`.  Remove the two factor edges at the boundary of `P`.  If the two arc
endpoints are Kneser-adjacent and the two complementary-arc endpoints are
also Kneser-adjacent, the corresponding 2-switch closes `P` and its
complement separately.  By Corollary 2 it is balanced exactly when

\[
 \iota(P)=s{\bf1}.
 \tag{5.1}
\]

When (5.1) holds, the new length-`M` component is a wreath and the complement
is a level-`ell-1` point-regular cycle.  We call this a **balanced peel**.

Thus the following is a precise sufficient route on the critical diagonal:

> merge PBBS components by balanced pure merges, reorder the resulting long
> components without changing their vertex sets, and expose closable arcs
> satisfying (5.1); each balanced peel produces one genuine wreath.

The existence of enough such reorderings and peels is not proved in general.

## 6. Exact certificate at `(n,k)=(6,2)`

Here `g=2`, `M=3`, and `s=1`.  The PBBS factor has signatures

\[
 (3,3,3,6).
\]

Its unique long component is

\[
 13,24,35,46,15,26.
\]

It has no balanced length-three cyclic arc.  The six arcs respectively
duplicate points `3,4,5,6,1,2` and omit points `6,1,2,3,4,5`.  Therefore no
single balanced 2-switch can split this component directly into two wreaths.

Nevertheless, three balanced switches suffice:

\[
\begin{array}{c|c|c}
&\text{removed edges}&\text{added edges}\\ \hline
1&(13,26),(34,56)&(13,56),(34,26)\\
2&(12,56),(24,35)&(12,35),(24,56)\\
3&(12,34),(15,46)&(12,46),(34,15).
\end{array}
\tag{6.1}
\]

The component signatures are

\[
 (3,3,3,6)\to(3,3,9)\to(3,3,3,6)\to(3,3,3,3,3).
 \tag{6.2}
\]

Every component at every step is point-regular.  The five final components
are the perfect matchings

\[
\begin{gathered}
 \{12,35,46\},\quad \{13,24,56\},\quad
 \{23,45,16\},\\
 \{14,25,36\},\quad \{34,15,26\},
\end{gathered}
\]

which are exactly the `(6,2)` wreaths.  This proves that merging can be
necessary even on the critical diagonal: a pre-existing wreath acts as a
catalyst for reordering the long component before it is split.

The full certificate is `PBBS_BALANCED_SWITCH_6_2_CERTIFICATE.txt`.

## 7. Exact certificate at `(n,k)=(8,3)`

Here `g=1`, `M=8`, and `s=3`, but this is **not** the critical diagonal.
The PBBS component lengths are

\[
 8,8,8,16,16.
\]

All five components are point-regular.  Only two of the three length-eight
components are wreaths.

Each length-sixteen component can be split by a balanced 2-switch.  For
example the two switches

\[
\begin{array}{c|c|c}
&\text{removed edges}&\text{added edges}\\ \hline
1&(237,458),(367,148)&(237,148),(367,458)\\
2&(126,347),(256,378)&(126,378),(256,347)
\end{array}
\tag{7.1}
\]

produce seven point-regular length-eight cycles.  Exhaustive wreath testing
shows that still only two are wreaths.  This is the promised off-diagonal
warning in exact switch form: minimum length plus point regularity is not
enough.

There is also a sharp monotonicity obstruction.  Suppose all components have
the minimum length `M`.  A balanced 2-switch within one component cannot
split it, because the two positive new component lengths would both be
multiples of `M` and sum to `M`.  A nonsplitting internal switch does not
change its vertex family.  A switch using edges from two components merges
them to length `2M`.  Therefore:

> changing the vertex family of a nonwreath minimum component necessarily
> creates a long component at an intermediate step.

In particular, no algorithm monotone in the number of components, or in the
total level excess, can solve `(8,3)` from this PBBS factor.

An exact 43-switch certificate nevertheless succeeds.  It keeps the two
existing wreaths fixed and performs:

1. two pure merges, combining the three bad PBBS components into one
   point-regular 40-cycle;
2. 37 internal 2-opt switches, each leaving that 40-vertex family and hence
   its point degrees unchanged; and
3. four balanced splits, producing five new wreaths.

Together with the two fixed wreaths, the result is a decomposition of all 56
triples into seven `(8,3)` wreaths.  The certificate is
`PBBS_BALANCED_SWITCH_8_3_CERTIFICATE.txt`.

This path was found on RunPod by a best-first search.  The search visited
12,284 states and expanded 639; these counts are discovery metadata, not a
minimality claim.  The certificate itself is independently checked without
trusting the search.

## 8. Odd graphs and the first available exact switch

For `KG(2m+1,m)`, two distinct vertices have at most one common neighbour, so
the graph has no 4-cycle.  Indeed, if two `m`-sets `A,C` had two common
neighbours, the complement of `A\cup C` would have to contain two distinct
`m`-sets.  This forces `|A union C|<=m`, hence `A=C`, a contradiction.

Thus the ordinary switch (3.1) has no odd-graph analogue.  General
alternating 6-cycles may exist, but they cannot map an exact wreath factor to
another exact wreath factor: every touched induced length-`n` wreath would
have to be cut at least twice, while an alternating 6-cycle removes only
three factor edges.  This is the single-cut obstruction proved in
`WREATH_SHADOW_SWITCH_AUDIT.md`.

The first exact-wreath-preserving operation is an alternating 8-cycle.  It
cuts two old wreaths twice each.  If their path-length profiles are

\[
 \{a,n-a\}\quad\text{and}\quad\{b,n-b\},
\]

the switch yields two new length-`n` wreaths exactly when the reconnection has
two components and

\[
 \boxed{\{a,n-a\}=\{b,n-b\}.}
 \tag{8.1}
\]

In the centered-incidence language, this is the four-segment version of
Lemma 1: each new component must receive segments whose centered vectors sum
to zero.  For a general merge-first route, an alternating 8-cycle with one
removed edge in each of four point-regular components is a four-way pure
merge and is automatically balanced, provided such a connector exists.  A
subsequent alternating switch is balanced precisely when each newly sewn
component satisfies (2.2).

This is the correct `g=1`, odd-graph replacement for the 4-cycle mechanism
tested at `(6,2)` and `(8,3)`.  Existing finite work already shows that the
more restrictive `2+2` exact-wreath eight-switches can improve the complete
multidepth shadow ledger: at `m=4`, six nonincreasing switches take the MSW
factor to an all-depth-complete exact wreath factor.

### 8.1 Exact odd-graph merge--reorder--split certificate at `(9,4)`

The canonical PBBS factor of `KG(9,4)` has component-length signature

\[
 (9,9,9,27,27,45).                                \tag{8.3}
\]

Every component is point-regular by PBBS homomesy, but only the minimum
components are immediately wreaths.  An exact 45-switch certificate
transforms this factor into the archived all-depth-complete 14-wreath factor
`m4_vertical_wreath_factor.txt`.

Every move removes four current factor edges and adds four nonfactor Kneser
edges.  The eight edges form one connected alternating `C_8`.  The complete
route consists of

\[
 \boxed{11\text{ merges}+20\text{ component-preserving reorderings}
 +14\text{ splits}.}                              \tag{8.4}
\]

These operations are interleaved rather than occurring in three monotone
phases.  The component signatures pass through long balanced components of
lengths `108`, `99`, `90`, `81`, `72`, `63`, `54`, and `45` before the final
peels.  Every intermediate component is point-regular and has length
divisible by nine.  The first and final signatures are

\[
 (9,9,9,27,27,45)longrightarrow(9,9,\ldots,9)
 \quad(14\text{ copies}).                         \tag{8.5}
\]

The initial state has 63 alternating 8-cycles, of which 45 preserve
componentwise point regularity.  The best one-step target-edge-overlap gain
is four.  A RunPod best-first search found the route after seeing 5,733
states and expanding 70; these are discovery statistics, not a minimality
claim.

The independent verifier checks all 46 factor states, all 126 middle
vertices, Kneser adjacency, the exact removed and added edge sets, connected
alternation of every `C_8`, point regularity and length divisibility of every
component, and equality of the final edge set with the target factor.  It
also reconstructs the omitted-label permutation of every final cycle and
checks the all-depth missing tuple

\[
 (M_0,M_1,M_2,M_3,M_4)=(0,0,0,0,0).              \tag{8.6}
\]

This is the first direct finite certificate for the odd-graph mechanism.
It proves that temporary long balanced components and alternating 8-switches
can jointly overcome the PBBS orbitwise splitting obstruction.  It does not
give an asymptotic supply or routing theorem.

## 9. Bridge to the step-two Johnson/run ledger

Let

\[
 A_0,A_1,\ldots
\]

be any Kneser cycle and put

\[
 B_i=[n]\setminus(A_i\cup A_{i+1}),
 \qquad |B_i|=n-2k.
\]

Since

\[
 [n]\setminus A_{i+1}=A_i\mathbin\dot\cup B_i
 =A_{i+2}\mathbin\dot\cup B_{i+1},
\]

we have the exact update

\[
 \boxed{A_{i+2}=(A_i\cup B_i)\setminus B_{i+1}.}
 \tag{9.1}
\]

In the odd graph `n=2m+1,k=m`, each `B_i={z_i}` is a singleton, and (9.1)
is a Johnson edge: the step-two subsequence swaps `z_{i+1}` out and `z_i`
in.  On a level-`ell` point-regular odd-graph cycle, every coordinate occurs
as an omitted label exactly `ell` times, because

\[
 \ell(2m+1)-2\ell m=\ell.
 \tag{9.2}
\]

For a minimum cycle, the labels are therefore a permutation.  Along the
step-two Johnson traversal every coordinate then has one cyclic 1-run of
length exactly `m`: the transition which inserts `z_j` and the transition
which removes it are `m` step-two moves apart.  Consequently every such
minimum component is automatically valid for the endpoint-capped erosion
identity through every depth `H<m` (boundary runs are treated as extending
past the path endpoint).

Balanced exact eight-switches preserve this minimum-wreath property while
changing the global ownership and shadow loads.  Their multidepth effect is
already tracked exactly by the local ledger in
`WREATH_MULTIDEPTH_8SWITCH_ENERGY_20260724.md`.

The `(6,2)` and `(8,3)` certificates do **not** directly improve this
single-coordinate run ledger: both have gap `n-2k=2`, so the `B_i` in (9.1)
are two-element blocks and the step-two move changes two coordinates at a
time.  Their contribution is structural evidence for the balanced
merge--reorder--split route, not an odd-graph vertical-factor theorem.

## 10. Independent verification

Run

```text
python3 scratch/verify_pbbs_balanced_switch_certificates.py
python3 scratch/verify_pbbs_odd9_balanced_switch_certificate.py
```

The verifier independently checks, at every step:

* reconstruction of the initial factor from cyclic parenthesis matching;
* exact partition of all `k`-sets;
* Kneser adjacency of every component edge;
* removal and addition of exactly two edges in the gap-two certificates and
  exactly four edges forming a connected alternating `C_8` in `KG(9,4)`;
* point regularity of every resulting component;
* divisibility of every component length by `n/gcd(n,k)`; and
* final wreath structure, by enumerating cyclic equal-block window families.

Expected output:

```text
PASS PBBS_BALANCED_SWITCH_6_2_CERTIFICATE.txt: 3 balanced switches, 5 final wreaths
PASS PBBS_BALANCED_SWITCH_8_3_CERTIFICATE.txt: 43 balanced switches, 7 final wreaths
PASS KG(9,4): 45 balanced alternating-8 switches
```

SHA-256 values at the time of this note:

```text
3cb652bc49af804ed1ac19a3b50d355f6270ad611e09d0039efebb51bf102aeb  PBBS_BALANCED_SWITCH_6_2_CERTIFICATE.txt
baa65b7b71a1c26e072538933b5e707316e567576bb693feabec4251003c1bc8  PBBS_BALANCED_SWITCH_8_3_CERTIFICATE.txt
875bab6f3421e81df450e8e797edd8e84e337aaabf937d815478bac9525d1232  scratch/verify_pbbs_balanced_switch_certificates.py
138e7195f7132f56623a51b905103dcb1365328f0160f71d93bff36c75082c15  PBBS_BALANCED_SWITCH_9_4_CERTIFICATE.txt
ae58c7135d690680be2eb8207e3a347f07c9ab91919ec1ef8bf0fb69dbdc4d20  PBBS_BALANCED_SWITCH_9_4_INITIAL_CENSUS.txt
1fac1c205c761a1275d9460fe94f45cefea34d29001744ea32a29b6325e832be  scratch/verify_pbbs_odd9_balanced_switch_certificate.py
```

The search/reconstruction helpers are:

* `scratch/analyze_pbbs_balanced_switches.py`;
* `scratch/search_pbbs_83_switch_path.py`; and
* `scratch/pbbs_odd9_balanced_switch_search.py`.

## 11. Exact status

### Proved

1. The centered-incidence condition (2.2) is necessary and sufficient for
   an alternating switch to preserve componentwise point regularity.
2. Pure merges of PBBS components preserve point regularity automatically.
3. The published tree-connector Hamilton gluing is balanced at every merge
   stage in its stated regime.
4. Critical-diagonal balanced minimum peels produce genuine wreaths.
5. The exact `(6,2)`, `(8,3)`, and odd-graph `(9,4)` balanced switch
   certificates above.
6. The `(9,4)` route reaches an exact 14-wreath factor with zero missing
   cyclic-interval colours at every depth.
7. A direct balanced split can fail even on the critical diagonal, and an
   off-diagonal nonwreath minimum component forces temporary length growth.

### Still open

1. An all-dimensional supply of alternating connectors which realizes the
   required balanced reorderings and peels.
2. A balanced split theorem for the Hamilton cycle obtained by the published
   glider connectors.
3. The analogous merge--reorder--split theorem using alternating 8-switches
   in the odd graph.
4. Any asymptotic improvement of the OR-word coefficient from this switching
   framework alone.

Accordingly, neither the Wreath Conjecture nor the constant-one OR bound is
claimed here.
