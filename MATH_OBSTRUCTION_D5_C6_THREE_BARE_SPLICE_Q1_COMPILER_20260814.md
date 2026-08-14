# A simple q1-exact C6 compiler cannot use three bare port splices

**Date:** 2026-08-14  
**Status:** exact general one-splice obstruction plus an exhaustive finite
obstruction for the three canonical port cuts of the actual rank-11,
ground-23 D5 router.  Coupled cables, auxiliary refill trades and globally
balanced multi-router banks remain open.

## 0. Outcome

A two-edge splice between one context edge and one router edge cannot by
itself preserve both immediate-lower and immediate-upper q1 colour
multisets while keeping both the owner and q1 palettes simple.  This is an
all-rank incidence fact.

Allowing the three bare port splices of one 18-owner router to balance one
another does not repair the actual D5 template.  At rank 11 on 23 labels,
each canonical port cut has 750 possible simple Johnson-C4 collars.  Among
the `750^3` triples, an exact signature join finds only 40 whose aggregate
lower and upper q1 currents both vanish.  Every one reuses router owners;
there are zero owner-simple triples.

Thus the flat 226-router atlas cannot be compiled by independently splicing
the three canonical port edges of each router into context strands.  Every
literal compiler must add a coupled cable/refill atom, balance q1 current
across multiple routers, or change the port geometry.

## 1. The local incidence obstruction

Let a Johnson edge between rank-`r` owners have lower and upper colours

\[
             (L,U),\qquad |L|=r-1,quad |U|=r+1,quad L\subset U.
\]

The unordered endpoints of this edge are the two rank-`r` sets strictly
between `L` and `U`; hence the pair `(L,U)` determines the edge.

Consider a two-edge splice.  Suppose its two removed edges have colours

\[
                         (L_1,U_1),\quad(L_2,U_2).    \tag{1.1}
\]

If the added cross edges preserve the lower and upper colour multisets,
then, after possibly interchanging their names, their colours must be

\[
                         (L_1,U_2),\quad(L_2,U_1).    \tag{1.2}
\]

The uncrossed assignment would reproduce `(L_1,U_1)` and `(L_2,U_2)`;
because a pair `(L,U)` determines its Johnson edge, it would reproduce the
two removed edges rather than give a nontrivial cross splice.  Thus only
the crossed assignment `(1.2)` remains.

All four containments in `(1.1)--(1.2)` imply

\[
                         L_1\cup L_2\subseteq U_1\cap U_2.  \tag{1.3}
\]

If `L_1=L_2`, the removed lower colour is repeated.  If `U_1=U_2`, the
removed upper colour is repeated.  Both violate q1 simplicity.  Otherwise

\[
 |L_1\cup L_2|\ge r,qquad |U_1\cap U_2|\le r.
\]

Equation `(1.3)` therefore forces equality:

\[
             M=L_1\cup L_2=U_1\cap U_2,qquad |M|=r. \tag{1.4}
\]

But `M` is one endpoint of each removed Johnson edge `(L_1,U_1)` and
`(L_2,U_2)`.  The removed edges share an owner, so they are not a legal
owner-disjoint two-edge splice.  This proves:

> **Lemma 1.1.** No owner-simple, lower-q1-simple and upper-q1-simple
> two-edge Johnson splice is q1-exact by itself.

The lemma explains why a successful local package must cancel q1 currents
among several splices rather than demand zero current at each port.

## 2. Complete three-port finite census

Fix the canonical 18-owner resident C6 router.  At each of its three
phase-common cuts

\[
                         P_{i,2}--Q_{i,0},             \tag{2.1}
\]

enumerate every ordered context edge `X_i--Y_i` satisfying

\[
 X_i\sim Y_i,qquad X_i\sim P_{i,2},qquad
 Y_i\sim Q_{i,0}.                                    \tag{2.2}
\]

The reverse cross pairing is included by reversing `X_i,Y_i`.  Thus `(2.2)`
exhausts every simple Johnson four-cycle around the fixed cut, including
both commuting squares and the non-induced triangle-type four-cycles.

The count 750 also has a closed audit.  Write adjacent cut owners as
`P=S+u`, `Q=S+v`, where `|S|=r-1`, and put `t=N-r-1`.  Among the neighbours
`X!=Q` of `P`, exactly

```text
t+(r-1)=N-2
```

are adjacent to `Q`; each has `N-2` common neighbours with `Q`, one of
which is the forbidden owner `P`, leaving `N-3` choices for `Y`.  The other
`(r-1)t` choices of `X` are at Johnson distance two from `Q`; they have four
common neighbours, again one equal to `P`, leaving three choices.  Hence

\[
 (N-2)(N-3)+3(r-1)(N-r-1)=21\cdot20+3\cdot10\cdot11=750. \tag{2.3}
\]

This counts a splice by the endpoint attached to `P`, so the opposite
cross pairing is present exactly when the context-edge endpoints are
reversed; it is neither omitted nor identified with the first pairing.

At rank 11 on the 23-point D5 ground there are exactly 750 candidates at
each port.  For every candidate record the signed lower and upper q1
multiset current of replacing

```text
X_i--Y_i, P_i--Q_i    by    X_i--P_i, Y_i--Q_i.
```

A meet-in-the-middle join combines all port-0/port-1 current signatures and
matches their negatives against port 2.  This is an exact enumeration of
all `750^3` triples without a candidate cap.  It gives

```text
candidates per port                         750,750,750
distinct port-0/port-1 signatures               562,378
aggregate lower+upper q1-exact triples                 40
triples with repeated context owners                         21
triples with six distinct context owners                     19
triples colliding with the 18-owner router bank              40
router-owner collision-set size 3                            40
triples with six distinct context owners disjoint
  from the complete 18-owner router bank                      0
fully owner/q1-simple triples                               0.
```

Every exact triple has router-owner collisions; the displayed replay prints
the first 20 literal patterns and counts all 40 before applying the
owner-simplicity filter.
Consequently none defines three physical degree-two splices.

The canonical normalization loses no embeddings: a ground permutation
takes any labelled copy of the router template and its three distinguished
cuts to the displayed copy, while `(2.2)` ranges over every relative
context edge after that normalization.

## 3. Scope

This obstruction rules out exactly the following architecture:

1. one 18-owner router copy;
2. its three canonical central cuts;
3. one bare two-edge Johnson splice from each cut to a context edge; and
4. no auxiliary q1-current carrier.

It does not rule out:

- the certified 36-owner three-splice package, whose cable and exterior
  cycles couple the currents differently;
- a fourth refill square or longer cable;
- cancellation across several routers;
- a noncanonical tapped port geometry; or
- an asymptotic common-history host with a separate q1 refill theorem.

These are the correct remaining compiler lanes.

## 4. H100 provenance

```text
complete C4 census
  scratch/search_d5_c6_router_all_c4_three_splice_q1_exact_20260814.py
  SHA256 d337daa64bf9e35d33e7d233565d11d436cffbcd770327e8081c944697019693

rank-11/ground-23 output
  scratch/search_d5_c6_router_all_c4_three_splice_q1_exact_r11n23_20260814.h100.out
  SHA256 70f49a89ad61f2dcbdf507029b9c98739c70f2bb4301612f5660e809c5700f90

independent common-neighbour replay
  scratch/audit_d5_c6_router_all_c4_three_splice_q1_exact_independent_20260814.py
  SHA256 dc56e2fee0b9440ba747d89f1831fb5a512b510b252062bd5dc8555a7b7a4d7d

independent output
  scratch/audit_d5_c6_router_all_c4_three_splice_q1_exact_independent_20260814.h100.out
  SHA256 7e996b7bbc20858e6cb25ea0d107d85ceea571cc18ebed994ded3b5b77f2b0f9
```

Exhaustive enumeration, independent replay and hashing were run through SSH
on H100.  The local Mac was used only to edit, transfer and operate Git.
