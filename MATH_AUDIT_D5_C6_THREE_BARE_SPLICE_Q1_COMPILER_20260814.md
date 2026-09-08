# Hostile audit of the D5 three-bare-splice q1 obstruction

**Date:** 2026-08-14  
**Verdict:** **PASS with the canonical bare-splice scope stated in the
source.**

Audited source:

`MATH_OBSTRUCTION_D5_C6_THREE_BARE_SPLICE_Q1_COMPILER_20260814.md`

H100 SHA-256:

```text
2f920120ab76e665a46b92de6cdd759cb48e6237e97b5abdf2a52810b76a97a6
```

## 1. Symbolic one-splice lemma

A rank-`r` Johnson edge is uniquely determined by its lower/upper pair
`(L,U)`: its endpoints are the two rank-`r` sets strictly between `L` and
`U`.  If two removed edges have distinct lower colours and distinct upper
colours, exact preservation by a nontrivial cross splice cannot keep the
two original `(L,U)` pairings, because that would reproduce the removed
edges.  The only possible pairing is therefore

```text
(L1,U2), (L2,U1).
```

All four edge containments imply
`L1 union L2` is contained in `U1 intersection U2`.  Distinct `(r-1)`-set
lowers have union size at least `r`, while distinct `(r+1)`-set uppers have
intersection size at most `r`.  Equality is forced, and the common rank-`r`
set is an endpoint of both removed edges.  Hence the removed edges are not
owner-disjoint.  Lemma 1.1 is valid at every rank.

## 2. Candidate completeness and reverse pairing

For one fixed adjacent router cut `P=S+u`, `Q=S+v`, put
`t=N-r-1`.  There are `N-2` neighbours `X!=Q` of `P` that are also adjacent
to `Q`; each leaves `N-3` permitted common-neighbour choices for `Y` after
excluding `P`.  The remaining `(r-1)t` neighbours are at Johnson distance
two from `Q`; each has four common neighbours, three after excluding `P`.
Thus the complete oriented collar count is

```text
(N-2)(N-3)+3(r-1)(N-r-1).
```

At `(N,r)=(23,11)` this is 750.  Naming `X` as the context endpoint joined
to `P` makes each cross pairing a separate oriented candidate.  Whenever
the opposite pairing is a Johnson pairing, reversing the context endpoints
places it in the same enumeration.  Hence neither cross orientation is
lost, and the triangle-type non-induced C4s are included.

## 3. Independent H100 replay

The main signature-join census reports:

```text
candidates per port                       750,750,750
distinct port-0/1 signature pairs             562378
aggregate lower+upper q1-exact triples             40
repeated-context-owner triples                       21
six-distinct-context-owner triples                   19
triples colliding with router owners                 40
collision-set size exactly three                     40
owner-simple triples                                  0
```

Artifacts:

```text
scratch/search_d5_c6_router_all_c4_three_splice_q1_exact_20260814.py
SHA-256 d337daa64bf9e35d33e7d233565d11d436cffbcd770327e8081c944697019693

rank-11/ground-23 output SHA-256
70f49a89ad61f2dcbdf507029b9c98739c70f2bb4301612f5660e809c5700f90
```

An independent bit-mask replay generates candidates through the closed
Johnson common-neighbour formulas instead of the search script's pair of
neighbour loops.  It reproduces all counts and verifies that every one of
the 40 exact triples has a three-owner intersection with the 18-owner
router bank:

```text
scratch/audit_d5_c6_router_all_c4_three_splice_q1_exact_independent_20260814.py
SHA-256 dc56e2fee0b9440ba747d89f1831fb5a512b510b252062bd5dc8555a7b7a4d7d

independent output SHA-256
7e996b7bbc20858e6cb25ea0d107d85ceea571cc18ebed994ded3b5b77f2b0f9
```

## 4. Exact scope

The finite no-go is invariant under relabelling of the canonical router,
but it fixes the three central phase-common cuts and uses exactly one bare
context edge and one direct two-edge splice at each port.  It allows every
ambient rank-11 context edge on all 23 labels, so it does not rely on the
more restrictive frozen-factor edge supply.  It does not cover alternative
router cuts, a cable or fourth refill atom, owner identifications inside a
larger audited package, cancellation across routers, or a global q1 refill
bank.  No q2, residence, or topology conclusion is needed: all 40 q1-exact
bare triples already fail owner simplicity.
