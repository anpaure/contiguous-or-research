# K17 drop-12 global `H union S` source cover for endpoint-disjoint selections

**Date:** 2026-08-03

**Status:** exact parent-local inherited-Hall theorem.  In particular, every
endpoint-disjoint three-mode child on the authenticated fixed-bank-safe
catalogue that can have supplier deficiency at most 20 contains an `H` or
`S` coordinate.  The result is stronger: it holds for an endpoint-disjoint
selection of any size.  This is a supplier necessary cut only; it makes no
occurrence, chronology, residence, compiler, or final-word claim.

## 1. Bound parent, shore, and class ledger

The theorem is bound to

```text
compressed parent  e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
literal final      fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c
structural edges   790fae940cd80c05e35656027dcb57139180b54c77f567c9b5333ab5d4581434
U112621 ledger     f1d9ab4ad29d4806d1b3e6a7518dda17733cd415c24e34a5aa8865f236f067db
Q23 head ledger    479302b36bf84710d2f5339177d28fd1db86127573646a23009c1bf6252cc5ca
Q23 supplier ledger
                   5686f140d3ad542a0d5ed2df5dd832cba1427d208ec9dad21cbb6cd217be3abb
all-U class ledger 160fd9c41409ef8bc99977efbeae4a5e45b8da4c492792cdb0ba4d7273d9f58c
class producer audit
                   0ef424731eff130de4d9af1aae7d58cdf765b5f695c30ad19da624fdf8ed4df6
independent replay aaef0f9c3923800c4ed353b8f8a0f72196c7c9a79c3c04729babe540d8a3a478
```

The inherited semantic shore is a set `Q` of 23 old hard heads with exactly
two parent supplier identities

\[
 a=12973,\qquad b=14851.
\]

With Hall bits numbered as in the authenticated ledger, their incidence
masks are

\[
 B_0(a)=\mathtt{c000},\qquad B_0(b)=\mathtt{10004}.
\]

Equivalently, the two nontrivial components of the shore are

```text
13148 -- 12973 -- 12948
15103 -- 14851 -- 1490,
```

and the other 19 heads are isolated.  The parent shore deficit is therefore
`23 - 2 = 21`.

The exact all-`U` partition is

\[
 |H|=468,\qquad |S|=47,\qquad |Z|=112099,\qquad |N|=7.
\]

`H` and `S` both have inherited-shore credit `+1`; their distinction is the
full singleton supplier rank (`H` reaches 16878 while `S` remains at 16877).
`Z` has credit zero and `N` credit minus one.

## 2. Exact simultaneous-shore oracle

For a structural mode `e`, let

* `F_e={h_e,d_e}` be its LR-host/LMR-donor endpoint rows;
* `D_e` be the old `Q`-head retirement mask;
* `B_e(u)` be the 23-bit incidence mask of changed endpoint row
  `u in F_e` after materializing `e`.

Every old `Q` head is a length-three row.  A structural host is length two
before transfer, so among the two endpoints only the LMR donor can be an old
`Q` head; this is exactly what `D_e` records.

For an endpoint-disjoint selection `X`, put

\[
 D_X=\bigcup_{e\in X}D_e,\qquad R_X=Q\setminus D_X.
\]

Only endpoint rows change.  Hence the exact old-shore neighbor-identity set
after simultaneous materialization is

\[
 \begin{aligned}
 N_X={}&\{s\in\{a,b\}\setminus F_X:
                    B_0(s)\cap R_X\ne\varnothing\}\\
     &{}\cup\bigcup_{e\in X}
       \{u\in F_e:B_e(u)\cap R_X\ne\varnothing\},
 \end{aligned}
 \tag{2.1}
\]

where `F_X` is the union of all selected endpoint rows.  Endpoint
disjointness makes the displayed identity union literal, rather than a
multiset approximation.

The active inherited shore has `23-|D_X|` heads, so its exact credit relative
to the parent `23/2` deficit is

\[
 \boxed{\gamma_Q(X)=|D_X|+|N_X|-2.}
 \tag{2.2}
\]

Hall's theorem applied to this literal active head subset gives

\[
 \operatorname{def}(\text{child})
 \ge |R_X|-|N_X|
 =21-\gamma_Q(X).                                      \tag{2.3}
\]

Consequently any child of supplier deficiency at most 20 must satisfy

\[
 \gamma_Q(X)\ge 1.                                      \tag{2.4}
\]

Equations (2.1)--(2.4), not singleton rank additivity, are the complete
Hall argument used below.

### All-arity subadditivity on the frozen shore

For a singleton mode `e`, define its gained and lost supplier-identity sets

\[
 A_e=N_{\{e\}}\setminus\{a,b\},\qquad
 C_e=\{a,b\}\setminus N_{\{e\}},
\]

and define `A_X,C_X` analogously for a simultaneous endpoint-disjoint
family. Then

\[
 \gamma_Q(\{e\})=|D_e|+|A_e|-|C_e|,
 \qquad
 \gamma_Q(X)=|D_X|+|A_X|-|C_X|.                       \tag{2.5}
\]

On this catalogue every mode retires at most one old `Q` head. Distinct
selected modes have distinct donor rows, hence

\[
 D_X=\mathbin{\dot\bigcup}_{e\in X}D_e.               \tag{2.6}
\]

Every jointly gained supplier identity belongs to a unique changed endpoint.
If that endpoint belongs to `e`, its materialized row state in the joint child
is the same as in the singleton `e` child, while the joint active-head set is
a subset of the singleton active-head set. Therefore

\[
 A_X\subseteq\mathbin{\dot\bigcup}_{e\in X}A_e.       \tag{2.7}
\]

Each of the two parent supplier identities has two distinct neighbors in
`Q`, as certified by masks `c000` and `10004`. Retiring at most one head
cannot by itself make either identity a singleton casualty. Thus if
`c in C_e`, mode `e` must change physical row `c`. Endpoint disjointness
makes these casualty identities distinct across modes and prevents any later
mode from restoring the changed row. Further retirements only shrink the
active-head set, so every singleton casualty persists jointly:

\[
 \mathbin{\dot\bigcup}_{e\in X}C_e\subseteq C_X.       \tag{2.8}
\]

Combining (2.5)--(2.8) proves the exact all-arity upper inequality

\[
 \boxed{\gamma_Q(X)\le\sum_{e\in X}\gamma_Q(\{e\}).} \tag{2.9}
\]

This is a literal endpoint/head-incidence proof. It does not invoke or assume
submodularity of the full matching rank.

## 3. Literal `Z` and `N` profiles

The authenticated 112,621-row class ledger and its independent rowwise
replay establish the following stronger facts.

### `Z` profile

Every one of the 112,099 `Z` rows has

```text
D_e                         = 0
B_0(h_e), B_0(d_e)          = 0, 0
B_e(h_e), B_e(d_e)          = 0, 0
post mask of a, b            = c000, 10004
post Q-neighbor identities   = 2
gamma_Q({e})                 = 0.
```

In particular, no `Z` endpoint is `a` or `b`, no `Z` mode retires a `Q`
head, and no `Z` endpoint supplies any old `Q` head before or after the
mode.  Thus `Z` is not merely singleton-nonpositive: it is a literal
identity action on the inherited shore.

For every endpoint-disjoint context `Y`, including contexts that contain
positive modes and retire old heads,

\[
 \gamma_Q(Y\cup\{z\})=\gamma_Q(Y)\qquad(z\in Z).
 \tag{3.1}
\]

### `N` profile

The seven `N` rows are exactly edges

```text
52844 52845 52846 52847 52848 52849 52850.
```

All seven have the same LR host `b=14851`, have no retirement, replace
`B_0(b)=10004` by the empty mask, and give neither changed endpoint a
nonempty `Q` mask.  Row `a=12973` remains at mask `c000`.  Consequently

\[
 \gamma_Q(Y\cup\{n\})\le\gamma_Q(Y)\qquad(n\in N)
 \tag{3.2}
\]

for every endpoint-disjoint context `Y`.  Moreover two `N` modes can never
coexist in an endpoint-disjoint selection because they share row 14851.

These statements are contextual marginal statements.  They directly rule
out the usual mechanism by which several singleton-nonpositive changes can
be jointly positive.

## 4. Global source-cover theorem

### Theorem

Let `X` be any endpoint-disjoint simultaneous selection from `U112621`.  If

\[
 X\cap(H\cup S)=\varnothing,
\]

then

\[
 \gamma_Q(X)\le0.
 \tag{4.1}
\]

More precisely,

\[
 \gamma_Q(X)=
 \begin{cases}
 0,&X\subseteq Z,\\
 -1,&|X\cap N|=1.
 \end{cases}
 \tag{4.2}
\]

Therefore every endpoint-disjoint child capable of supplier deficiency at
most 20 contains at least one mode in `H union S`.  In particular this holds
for every endpoint-disjoint triple.

### Proof

Starting from the empty selection, each `Z` coordinate has exactly zero
contextual marginal by (3.1).  Endpoint disjointness permits at most one
`N` coordinate, and its marginal is nonpositive by (3.2).  Because `Z`
retires no head, an admitted `N` coordinate literally removes `b` while
leaving `a`, giving the exact second line of (4.2).  Thus (4.1) follows.
Condition (2.4) is necessary for deficiency at most 20, so a source-free
selection is impossible.  This proof is independent of occurrence
feasibility and of the full supplier matching outside the inherited shore.
\(\square\)

The theorem also gives a canonical distinguished source role for a complete
triple join.  A lane-compatible duplicate-free convention is: if the child
contains `H`, choose its least authenticated `H` edge; otherwise choose its
least authenticated `S` edge.  Thus the existing `H`-source bilateral lane
covers every child containing `H`, while a separate `S`-source lane need
only cover the no-`H`, `S`-containing face.  The other two coordinates
remain helpers and may lie in any of `H,S,Z,N`; the theorem does not require
either helper to be individually common or supplier-positive, and it does
not transfer the `H`-specific support-two lemma to an `S` source.

The least-edge convention partitions physical children; it is not permission
to erase alternative viable source labels from a proof ledger. Exact join
artifacts must retain every viable `H/S` role label and attach the canonical
partition tag only when projecting to duplicate-free physical children.

## 5. Lossless finite screen and smallest quotient

No `112621 choose 3` scan is needed.  The complete source-free quotient has
only two shore-action signatures:

| signature | multiplicity | action on `Q` | credit |
|---|---:|---|---:|
| `I` (`Z`) | 112099 | preserve both `a,b` | 0 |
| `K_b` (`N`) | 7 | delete `b`; preserve `a` | -1 |

Its endpoint-disjoint composition rules are

\[
 I I=I,\qquad I K_b=K_b,\qquad K_bK_b=\bot,
 \tag{5.1}
\]

where `bottom` denotes endpoint collision at row 14851.  Thus the only
source-free triple signatures are `III` and `IIK_b`, with credits zero and
minus one.  Both are rejected without generating a structural triple.

A lossless implementation needs the following authenticated per-mode data:

```text
edge_index, q23_class, lr_row, lmr_row,
d_q_mask, old_host_q_mask, old_donor_q_mask,
post_host_q_mask, post_donor_q_mask,
post_old_supplier0_q_mask, post_old_supplier1_q_mask.
```

It also needs the ordered 23-head ledger, supplier identities `12973` and
`14851`, and their parent incidence masks.  The audit checks are:

1. all 112,621 authenticated modes occur exactly once;
2. the class census is `468/47/112099/7`;
3. every `Z` row has the literal identity profile above;
4. every `N` row has the literal `K_b` profile and the seven exact edge IDs;
5. all `N` rows share LR endpoint 14851.

After those linear-size checks, the exact triple screen is simply

```text
reject if none of the three class labels is H or S.
```

This screen is a theorem-backed rejection, not a heuristic upper bound.

## 6. Scope boundary

The source cover applies only to simultaneous endpoint-disjoint selections
from the authenticated fixed-bank-safe `U112621` catalogue on the literal
`e878/fa491` parent.  It does not cover overlapping transfers, other parent
tables or root subsets, or actions outside this catalogue.  It proves only
that every target-20 triple has an `H/S` Hall-source coordinate.  It does not
prove that any `H/S`-anchored bilateral join has a complete occurrence
packing or improves the full supplier matching; those survivors still need
the joint three-role occurrence oracle, simultaneous materialization, and
full supplier replay.
