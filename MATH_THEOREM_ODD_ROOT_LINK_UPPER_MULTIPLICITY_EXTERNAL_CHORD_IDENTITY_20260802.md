# Odd rooted paths: exact upper multiplicity equals external-chord load

**Date:** 2026-08-02  
**Status:** unconditional identity and an exact reformulation of the
immediate-upper gate.  It does not construct the required path, address
higher upper ranks, impose residence, or solve the lower compiler.

## 0. Outcome

Let `k=2r-1`, and let

\[
                         T_0,T_1,\ldots,T_{W-1}
\tag{0.1}
\]

be a Hamilton path through all rank-`r` owners whose adjacent intersections

\[
                         L_i=T_i\cap T_{i+1}
\tag{0.2}
\]

are all distinct.  Write `M` for the unique rank-`(r-1)` set omitted by
the `L_i`.  This is exactly the owner form of a directed root-link Hamilton
path, with terminal matching root `M`.

For each rank-`(r+1)` set `R`, let

* `u_R` be the number of adjacent-owner unions equal to `R`;
* `a_R` be the number of the two path endpoints which are facets of `R`;
* `m_R=1_(M subset R)`; and
* `g_R` be the number of path edges whose intersection lies in `R` while
  **both** endpoint owners lie outside `R`.

Then

\[
 \boxed{
 u_R-g_R
   =2(r+1)-{r+1\choose2}-a_R+m_R.}
\tag{0.3}
\]

Equivalently, with

\[
 h_r={r+1\choose2}-2(r+1)+1
     ={(r+1)(r-4)\over2}+1,
\tag{0.4}
\]

one has the exact defect identity

\[
 \boxed{u_R-1=g_R-(h_r+a_R-m_R).}
\tag{0.5}
\]

Thus immediate-upper surjectivity is equivalent to the pointwise load
system

\[
 \boxed{g_R\ge h_r+a_R-m_R\qquad\text{for every }R.}
\tag{0.6}
\]

The total slack in (0.6) is forced:

\[
 \boxed{
 \sum_R\bigl(g_R-h_r-a_R+m_R\bigr)
     =W-1-{2r-1\choose r+1}
     =\operatorname{Cat}_r-1.}
\tag{0.7}
\]

At `K17`, `r=9`, so the generic threshold is exactly `26`, while the total
excess over all thresholds is only `4861`.  Immediate-upper coverage is
therefore a tight near-balanced external-chord design, not an unstructured
set-cover row.

## 1. The three types of a root contained in `R`

Fix `R in binom([k],r+1)`.  Its owner facets are

\[
                         \mathcal F_R={T\in\mathcal T:T\subset R},
                         \qquad |\mathcal F_R|=r+1.
\tag{1.1}
\]

There are

\[
                         N_R={r+1\choose r-1}={r+1\choose2}
\tag{1.2}
\]

rank-`(r-1)` roots contained in `R`.  All of them occur as path-edge
intersections except `M` when `M subset R`.

For a used root `L subset R`, its path-edge owners have the form

\[
                         L+\{x\},\quad L+\{y\},
                         \qquad x\ne y,\qquad x,y\notin L.
\tag{1.3}
\]

Exactly one of the following occurs.

1. **Internal:** `x,y in R`.  Both owners are facets of `R`, and their
   union is `R`.  These edges are counted by `u_R`.
2. **Boundary:** exactly one of `x,y` lies in `R`.  The edge has one owner
   in `mathcal F_R` and one outside.  Let their number be `b_R`.
3. **External chord:** `x,y notin R`.  Both owners lie outside `R`.  These
   edges are counted by `g_R`.

The three cases are exhaustive because `R-L` has exactly two elements.
Distinct path edges have distinct roots, so counting the used roots inside
`R` gives

\[
             u_R+b_R+g_R={r+1\choose2}-m_R.
\tag{1.4}
\]

## 2. Facet-degree conservation

The path degree sum over the `r+1` facet owners of `R` is

\[
                         2(r+1)-a_R,
\tag{2.1}
\]

because an endpoint facet has path degree one and every other facet has
degree two.  An internal edge contributes two to this degree sum, a
boundary edge contributes one, and an external chord contributes zero.
Therefore

\[
                         2u_R+b_R=2(r+1)-a_R.
\tag{2.2}
\]

Subtracting (1.4) from (2.2) gives (0.3), and rearranging gives (0.5)--
(0.6).  This proves the pointwise theorem.

### Theorem 2.1 (connectivity is unnecessary)

The identities (0.3)--(0.7) remain valid if the Hamilton path is replaced
by any spanning directed root-link factor consisting of one directed path
and any number of disjoint directed cycles, provided:

* the source and sink of the path are the two named endpoints;
* every other vertex has one selected incoming and one selected outgoing
  arc; and
* the sink root is `M`.

#### Proof

The selected outgoing arcs use every tail root except the sink `M` exactly
once, so (1.4) is unchanged.  Every cycle vertex and every internal path
vertex has undirected selected degree two, while the source and sink have
degree one.  Therefore the facet-degree sum (2.1), and hence (2.2), is also
unchanged.  The proof of (0.3)--(0.7) used no connectivity statement beyond
these two ledgers.  \(\square\)

This extension is operationally important at `K17`: the external-load
cardinality rows (5.1) are exact already in the degree-satisfied pre-solve
factor.  They may be imposed before lazy subtour elimination; a selected
solution cannot evade them by splitting into several cycles.

### Theorem 2.2 (degree-deficit projection identity)

Connectivity is also unnecessary for the ordinary projection of the
augmented lollipop.  More generally, let `P` be a root-labelled Johnson
subgraph which selects exactly one edge of every rank-`(r-1)` root outside
an omitted set `E`, selects no edge of a root in `E`, and has owner degrees
at most two.  For a rank-`(r+1)` set `R`, define

\[
 e_R=|\{L\in E:L\subset R\}|,
 \qquad
 a_R^P=\sum_{\substack{T\subset R\\|T|=r}}(2-\deg_P(T)).
\tag{2.3}
\]

Let `p_R` count selected edges whose two owners are facets of `R`, and let
`g_R^P` count selected edges whose root lies in `R` but whose two owners
both lie outside `R`.  Then

\[
 \boxed{p_R-1=g_R^P-(h_r+a_R^P-e_R).}
\tag{2.4}
\]

#### Proof

Writing `b_R^P` for the boundary edges gives

\[
 p_R+b_R^P+g_R^P={r+1\choose2}-e_R,
 \qquad
 2p_R+b_R^P=2(r+1)-a_R^P.
\tag{2.5}
\]

The first equation counts selected roots contained in `R`; the second is
the selected-degree sum over the owner facets of `R`.  Subtracting and
using (0.4) proves (2.4).  No component count or orientation enters either
ledger.  \(\square\)

For the ordinary projection used by the `h=1` incidence master, take
`E={M,D}`.  The owner-degree deficits are one unit at the fixed boundary
owner `B` and one unit at each of the three selected `D`-neighbour owners.
These are counted with multiplicity if an owner appears in both roles.  Put

\[
 a'_R=\mathbf1_{\{B\subset R\}}
      +|\{T:T\text{ is a selected `D`-neighbour owner and }T\subset R\}|,
 \quad
 d_R=\mathbf1_{\{D\subset R\}}.
\tag{2.6}
\]

Then (2.4) becomes the exact master row

\[
 \boxed{p_R-1=g_R^P-(h_r+a'_R-m_R-d_R).}
\tag{2.7}
\]

Thus ordinary immediate-upper coverage is equivalent to

\[
 \boxed{g_R^P\ge h_r+a'_R-m_R-d_R\qquad\text{for every }R,}
\tag{2.8}
\]

already before any subtour-connectivity constraints are imposed.

## 3. Global current and Catalan slack

Each path edge has exactly one rank-`(r+1)` owner union, so

\[
                         \sum_Ru_R=W-1.
\tag{3.1}
\]

There are

\[
                         U={2r-1\choose r+1}
\tag{3.2}
\]

upper colours.  Summing `u_R-1` proves (0.7) directly, since

\[
                         W-U=\operatorname{Cat}_r.
\tag{3.3}
\]

The external current also has a useful independent check.  For a fixed
path edge with root `L` and exchanged coordinates `x,y`, an upper set `R`
counts it as an external chord precisely when

\[
                         L\subset R,\qquad x,y\notin R.
\]

After fixing `L,x,y`, there are `r-2` unused ground coordinates and `R`
must choose two of them.  Hence every path edge contributes to exactly

\[
                         {r-2\choose2}
\tag{3.4}
\]

external loads, and

\[
                         \sum_Rg_R=(W-1){r-2\choose2}.
\tag{3.5}
\]

Likewise

\[
 \sum_Ra_R=2(r-1),\qquad
 \sum_Rm_R={r\choose2}.
\tag{3.6}
\]

Equations (3.5)--(3.6) replay the sum of (0.3) and give a convenient exact
audit ledger.

### 3.1 Local Kneser-transform form

For every used root `L`, record its exchanged pair

\[
                         P_L=\{x,y\}\in{{[k]\setminus L}\choose2}.
\tag{3.7}
\]

Fix `R` and write `Z_L=R-L` for every root `L subset R`.  Both `P_L` and
`Z_L` are two-subsets of the `r`-element complement of `L`.  The three
cases of Section 1 become

\[
\begin{array}{c|c}
P_L=Z_L&\text{internal provider of }R,\\
|P_L\cap Z_L|=1&\text{boundary edge},\\
P_L\cap Z_L=\varnothing&\text{external chord for }R.
\end{array}
\tag{3.8}
\]

In particular,

\[
 g_R=
 \sum_{\substack{L\in{{R}\choose{r-1}}\\L\ne M}}
        \mathbf1_{\{P_L\cap(R-L)=\varnothing\}}.
\tag{3.9}
\]

For each fixed root, the map from the selected pair `P_L` to its external
two-set loads is exactly one column of the Kneser graph `KG(r,2)`.  For
`r>=4`, its degree is `binom(r-2,2)` and its standard eigenvalue list
(suppressing zero multiplicities) is

\[
                         {r-2\choose2},\qquad -(r-3),\qquad 1.
\tag{3.10}
\]

Thus, for `r>=4`, the immediate-upper gate is an occurrence-labelled
Boolean sum of invertible local Kneser transforms, coupled by the
requirement that the chosen pairs form one owner path.

At `r=9`, an independently uniform pair choice at every used root would
give, before endpoint conditioning,

\[
 {9+1\choose2}{ {7\choose2}\over {9\choose2}}
 =45\cdot{21\over36}=26.25
\tag{3.11}
\]

expected external load per generic `R`, against the integer threshold 26.
The fractional margin is only one quarter.  This explains why aggregate
capacity passes while literal rounding remains tight.

## 4. Two sharp low-rank consequences

### 4.1 `K5`: upper coverage is automatic

At `r=3`, the complement of `R` has size one.  Two distinct exchanged
coordinates cannot both lie outside `R`, so

\[
                         g_R=0.
\]

Equation (0.3) becomes

\[
                         u_R=2-a_R+m_R.
\tag{4.1}
\]

If at most one path endpoint is a facet of `R`, then `u_R>=1`.  If both
endpoints are facets, the terminal owner lies in `R`; since it contains the
terminal root `M`, one has `m_R=1`, and again `u_R=1`.  Thus every rooted
Hamilton path at `K5` is immediate-upper-surjective.  This recovers the
independent theorem and the `2,280/2,280` exhaustive result in
`MATH_AUDIT_K5_ROOT_LINK_UPPER_CENSUS_AND_FIXED_BOUNDARY_NOGO_20260802.md`.

### 4.2 `K7`: exact internal/external duality

At `r=4`, the constant term in (0.3) vanishes:

\[
                         u_R=g_R-a_R+m_R.
\tag{4.2}
\]

Moreover `binom(r-2,2)=1`.  Every path edge with exchanged pair `{x,y}`
contributes to the unique external colour

\[
                         R^*=[7]\setminus\{x,y\}.
\tag{4.3}
\]

Thus the immediate-upper palette is complete exactly when this dual
external-colour word meets

\[
                         g_R\ge1+a_R-m_R
\tag{4.4}
\]

for all `R`.  The `K5` automaticity ends sharply at `K7`: from this rank
onward, external-root traffic is a genuine independent distribution row.

## 5. The `K17` exact load target

For `K17`,

\[
 r=9,\qquad W={17\choose9}=24310,
 \qquad U={17\choose10}=19448,
 \qquad \operatorname{Cat}_9=4862.
\]

Equation (0.4) gives

\[
                         h_9=26.
\]

Therefore a candidate rooted Hamilton path is rank-ten-complete exactly
when

\[
 \boxed{
 g_R\ge26+a_R-m_R
 \qquad\left(R\in{{[17]}\choose{10}}\right).}
\tag{5.1}
\]

Every path edge contributes to `binom(7,2)=21` external colours, so

\[
                         \sum_Rg_R=24309\cdot21=510489.
\tag{5.2}
\]

The threshold sum is

\[
 19448\cdot26+16-36=505628,
\tag{5.3}
\]

leaving exactly

\[
                         510489-505628=4861
                         =\operatorname{Cat}_9-1
\tag{5.4}
\]

units of repeat slack.

This is the useful finite consequence.  Rank-ten coverage should be encoded
or constructed as a balanced lower-bound design on the external loads
`g_R`; checking actual owner unions is equivalent but hides the tight
current.  The remaining rank-eleven-through-seventeen excursions are not
controlled by (5.1).

### 5.1 Exact ordinary-projection row for the incidence master

For the ordinary projection of Theorem 2.2, the exact `K17` coverage row is

\[
 \boxed{
 g_R^P\ge26+a'_R-m_R-d_R
 \qquad\left(R\in{{[17]}\choose{10}}\right).}
\tag{5.5}
\]

There are `W-2=24308` ordinary root edges, and each contributes to 21
external colours.  Hence

\[
                         \sum_R g_R^P=24308\cdot21=510468.
\tag{5.6}
\]

The four owner-degree deficit units contribute `4(r-1)=32` in total, while
each of `M,D` lies in `binom(9,2)=36` rank-ten sets.  The total threshold is

\[
                         19448\cdot26+32-36-36=505608.
\tag{5.7}
\]

Therefore the ordinary projection has exactly

\[
                         510468-505608=4860
                         =\operatorname{Cat}_9-2
\tag{5.8}
\]

units of rank-ten repeat slack.  This is one unit tighter than the rooted
Hamilton-path ledger, as it must be because the ordinary projection has
one fewer selected root edge.

## 6. Scope and next theorem

The identity assumes a rooted Hamilton path, equivalently that all but one
rank-`(r-1)` roots occur exactly once.  It does not assert existence of that
path for prescribed endpoints.  The `K5` audit already proves that an
arbitrary frozen matching and boundary can fail before upper coverage.

The immediate mathematical target is now:

> **Balanced external-chord linearization.**  Jointly choose the containment
> matching, lollipop endpoints and rooted Hamilton path so that the external
> loads satisfy (0.6), while retaining the residence component floor.

For `K17`, this is a near-regular `26/27/...` load problem with only 4,861
total repeat units.  It is substantially more structured than a generic
19,448-row upper set cover, but its integral construction remains open.
