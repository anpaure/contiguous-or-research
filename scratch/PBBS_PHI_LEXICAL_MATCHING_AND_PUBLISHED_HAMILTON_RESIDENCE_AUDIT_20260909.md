# The exact PBBS matching in the published middle-levels constructions

2026-09-09. Bounded primary-source literature and pure-proof audit by
`exact_b_induction`. No mathematical program, construction search, or
downloaded generator was executed. The all-dimensional exact OR-word goal
remains open.

## 1. Result and scope

The matching fixed by the verified optimal seventeen-coordinate carrier is
exactly the **r-lexical matching N** in Gregor--Mütze--Nummenpalo's notation
for the middle levels of the (2r+1)-cube. It is also the matching between
the two states with the same Dyck word and shift in Mütze's book proof.

The standard Hamiltonization does not keep this matching fixed. Each book-
proof pull removes exactly one of its edges. A spanning pull tree produces
a Hamilton cycle missing exactly p_r-1 edges of Phi, where p_r is the number
of plane trees with r edges, equivalently the number of initial factor
components. This is an explicit all-dimensional near-preservation theorem,
not a theorem that a Hamilton cycle contains all of Phi.

More decisively for the current compiler, **every output of the book-proof
pull family has a positive coordinate run of length one in its lower-layer
projection, for every r>=2**. The proof below treats selected and unselected
pulls, and survives reversal of the output cycle. Thus this family does not
satisfy even the first of the two required delayed-deletion exclusions.

The bounded review did not locate a published all-r theorem producing a
Hamilton cycle containing the entire specified N. This is not a literature-
wide nonexistence assertion and is not an impossibility theorem for such
cycles. The alternative rotational theorem inspected specifies symmetry and
Hamiltonicity, not containment of N or residence.

## 2. Primary sources and retained local interfaces

The exact primary sources inspected are:

1. P. Gregor, T. Mütze, J. Nummenpalo, *A short proof of the middle levels
   theorem*, Discrete Analysis 2018:8, DOI 10.19086/da.3659,
   [published-version PDF](https://arxiv.org/pdf/1710.08249).
   The matching definitions are in Section 2, printed pp.3--4; the factor
   is in Section 1.1; the pull-edge positions are Proposition 3(ii), and
   the modified paths are at the end of its proof, printed p.8.
2. T. Mütze, *A book proof of the middle levels theorem*, Combinatorica
   44 (2024), 205--208,
   [author's arXiv version v4](https://arxiv.org/pdf/2306.13019).
   PDF p.1 defines the triples and map f. PDF p.2 defines G(x), displays
   Figure 4, defines S(x), and proves disjointness for **any two distinct
   pullable trees**, before the spanning-tree selection.
3. A. Merino, O. Mička, T. Mütze, *On a combinatorial generation problem of
   Knuth*, [paper](https://arxiv.org/pdf/2007.07164), Theorems 1--2,
   Section 1.4, printed p.3. These assert a rotational middle-levels
   Hamilton cycle, arbitrary coprime shift, and a generation algorithm.
   They do not assert containment of the present fixed matching.

The older matching-extension results surfaced in the bounded search concern
the full hypercube, not its middle two levels. They cannot be transferred
by restricting the Hamilton cycle: restriction generally breaks it into
paths. Likewise, the theorem excluding unions of two lexicographic
matchings does not exclude a fixed lexical matching plus an arbitrary
second matching; we do not use that different statement.

Already present in this repository, and not claimed anew:

* `K17_OPTIMAL_CARRIER_FIXED_PBBS_MATCHING_AND_EXACT_DIFFERENCE_CERTIFICATE_20260909.md`,
  Sections 1--4: the named-label identity M_out=Phi and the fixed-matching
  permutation formulation. Its actual incoming matching is not assumed to
  equal the other published lexical matching.
* `K15_FIXED_M0_RESIDENCE_AS_WIDTH_TWO_THREE_ARC_IDEAL_20260729.md`,
  Sections 1--3: residence is precisely the two arc exclusions below.
* `MATH_MERINO_MICKA_MUTZE_STRICT_SPIRAL_PROJECTION_20260729.md`,
  Sections 1--3: the rotational theorem already supplies middle ownership,
  topology and one immediate shadow, but not the extra OR-word gates.
* `MATH_THEOREM_GMN_LEXICAL_FIXED_COORDINATE_RUN_SPECTRUM_AND_STEM_NOGO_20260805.md`:
  earlier fixed-coordinate run-spectrum and protected-stem obstructions.
  The short local run obstruction in Section 5 below addresses the specific
  two-transition residence requirement instead.

## 3. Exact matching identification, including gauge

Put n=2r+1, identify a lower set with its length-n binary word, and read
sites in their positive cyclic order. A one is an up-step, a zero a
down-step. Let

    S_j = number of ones minus number of zeros in positions 1,...,j.

Let j_* be the **first** index attaining the minimum among S_0,...,S_n.
Since S_n=-1, j_*>0 and the bit at j_* is zero. Cutting immediately after
j_* writes the circular word as D0 with D a Dyck word.

Here is the boundary check, which matters for the earliest-tie convention.
Before wrapping, every partial sum relative to S_(j_*) is nonnegative.
After wrapping and before the last bit, its value is

    -1-S_(j_*)+S_q >= 0,       0<=q<j_*,

because S_q>=S_(j_*)+1 before the first minimum. The final sum is -1.
Thus the final zero is exactly the cyclic unmatched zero. Conversely the
unique Dyck-root cut has this first-minimum property.

The GMN matching N flips the zero at the earliest prefix attaining the
largest surplus of zeros over ones. This is precisely j_*. Therefore,
in the same coordinate direction,

    N(L)=L+u(L)=Phi(L).                                  (3.1)

No complementation, coordinate-dependent permutation, or cycle-dependent
gauge is needed. If one writes the physical coordinate order in reverse,
one must conjugate both definitions by that single reversal; (3.1) is an
identity in the positive-order convention used here and in the retained
PBBS normalization 0D.

For the book proof write

    <D,b,s> = rho^s(Db),      D Dyck, b in {0,1}.

The unmatched site of <D,0,s> is the final site of D0 rotated by s. Hence

    Phi(<D,0,s>)=<D,1,s>.                                (3.2)

The book's map sends an upper triple <D,1,s> back to <D,0,s>, so this is
its entire upper-to-lower matching. Its other matching is generated by
the tree-rotation step; it need not be the incoming matching of the actual
PBBS factor or of the supplied optimum.

## 4. What a published pull does to Phi

Use the book proof's f, which is a map on both middle layers and is **not**
the repository's complement-except-root PBBS f. Let x=110u0v be pullable,
with u,v Dyck words, and set y=x0 and z=101u0v0. Its relevant states are

    V0=y       =110u0v0,
    V1=f(y)    =110u1v0,
    V2=f^2(y)  =010u1v0,
    V3=f^3(y)  =011u1v0,
    V4=f^4(y)  =001u1v0,
    V5=f^5(y)  =101u1v0,
    V6=f^6(y)  =100u1v0,
    Z0=z       =101u0v0,
    Z1=f(z)    =111u0v0.                                 (4.1)

The displayed six-cycle is

    G(x)=(V0,V1,V6,V5,Z0,Z1).                            (4.2)

Its three old factor edges are V0V1, V5V6, Z0Z1. Exactly V5V6 is a Phi
edge, because the book's odd-to-even steps are Phi inverse. The other
three edges of G(x) are outside the old factor, and thus outside Phi,
since the full Phi matching was already in that factor.

Consequently every selected pull deletes exactly one Phi edge and adds
none. The sets S(x) consisting of the nine states in (4.1) are pairwise
disjoint over distinct pullable x. In particular the deleted Phi edges
are all distinct and another selected pull cannot restore one.

There are p_r initial components, indexed by plane trees. The connected
pull host has a spanning tree; using its p_r-1 edges gives a Hamilton cycle
with exactly

    binom(2r+1,r)-(p_r-1)                               (4.3)

of the prescribed Phi edges. Equation (4.3) is a consequence of the exact
edge accounting, not an assertion explicitly advertised as the main
theorem of the paper. For r>=3 there are at least two plane-tree types
(path and star), so a Hamilton output in this family omits Phi edges.
For r=1,2 the initial factor has one component and no pull is needed.

This proves failure of full matching preservation by this method. It does
not prove that Phi cannot be preserved by a different alternating exchange.

## 5. A protected local failure of the required residence

Let a middle cycle be projected to its successive rank-r states L_i.
Write its insertion and deletion labels as

    b_i=L_(i+1) minus L_i,    d_i=L_i minus L_(i+1).

The desired lower residence is

    b_i != d_(i+1) and b_i != d_(i+2) for every i.       (5.1)

It is equivalent to every positive coordinate run in the lower sequence
having length at least three. In the upper sequence U_i=L_i union L_(i+1)
this is positive-run length at least four. Distinct middle vertices forbid
a one-position zero gap in the lower sequence, so lower runs dilate by one
without merging. These equivalences are already proved in the retained
fixed-M0 residence note.

Fix **any** pullable x and its nine-state stencil (4.1). Such an x exists
for every r>=2; take u empty and v=(10)^(r-2). Consider any set of selected
book-proof pulls, including one producing a Hamilton cycle.

**Case 1: G(x) is not selected.** The factor path

    V2--V3--V4--V5--V6

remains. Its lower projection is

    010u1v0,   001u1v0,   100u1v0.

The third displayed coordinate has trace 0,1,0. It is inserted and then
deleted on the very next lower transition.

**Case 2: G(x) is selected.** The new edge V6V1, followed by the unchanged
path V1--V2--V3--V4, remains. Its lower projection is

    100u1v0,   010u1v0,   001u1v0.

The second coordinate has trace 0,1,0, giving the same violation.

The two cases are protected against all other chosen pulls: all vertices
of each displayed path belong to S(x), while S(x') is disjoint from S(x)
for **every other eligible x'**, regardless of whether x is selected.
This is exactly the quantifier in the book proof's disjointness statement.

A Hamilton output can traverse either path backwards. The trace 0,1,0
and the fact that the two incident lower transitions are consecutive are
unchanged by reversal. Thus orientation cannot avoid the violation.

We have proved:

    For every r>=2 and every output formed by the book-proof pull family,
    some lower positive coordinate run has length one.                (5.2)

In particular changing only its spanning tree cannot supply (5.1). This
is stronger than saying that the paper does not promise residence, but its
scope is this exact construction family. It says nothing against the
verified optimum's different incoming matching or other Hamiltonizations.

## 6. The remaining constructive matching theorem

Fixing Phi still leaves the exact r-regular bipartite choice graph from the
retained seventeen-coordinate note. A desired all-r theorem could select
a second perfect matching P disjoint from Phi such that the resulting
successor has few usable components (one is sufficient), satisfies (5.1),
and supports the required higher unions and lower capped targets.

Neither arbitrary middle-levels Hamiltonicity nor rotational Hamiltonicity
supplies those extra conclusions. Conversely the exact OR-word argument
does not require insisting on a single Hamilton component: the successful
seventeen-coordinate carrier has two components.

The obvious Phi-preserving exchanges act only on P: toggle a P-alternating
even cycle in the graph with Phi removed. This is the old fixed-matching
formulation, not a new existence theorem. Such a switch preserves the two
middle decks. Residence must still be checked on the resulting consecutive
two- and three-arc motifs, and all other target witnesses require separate
transport or reconstruction. The canonical book pull cannot be substituted
for such an exchange, because its removed-edge set contains Phi.

No general matching-preserving connecting family with all these properties
was proved or imported in this audit. The useful new information is the
exact published matching identification, its quantified loss under the
standard gluing method, and the all-r local residence obstruction that
rules out choosing a better spanning tree within that method.

## 7. Audit status

The source definitions, cut convention, nine-state formulas, matching-edge
accounting, and both temporal cases were read and checked symbolically.
No numerical tests of native PBBS versus the other lexical matching were
made, and none are needed for (3.1). This is an internal research audit,
not an external or formal certification. No all-rank OR coverage theorem,
exact all-dimensional construction, or new finite word is claimed.

Postscript: `exact_equality_structure` independently read this entire note
and checked both surviving paths and the two 0,1,0 traces in Section 5.
It passed the implication from the stated stencil and all-eligible
disjointness, including reversal and the lower-to-upper dilation argument.
That second review did not independently reopen the external paper; the
primary-source verification remains attributed to this author above.
