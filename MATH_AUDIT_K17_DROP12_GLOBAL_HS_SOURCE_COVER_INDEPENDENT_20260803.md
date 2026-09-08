# Independent audit of the K17 global `H union S` source cover

**Date:** 2026-08-03  
**Verdict:** **GO**, with the exact scope in Section 5.  
**Audited theorem:**
`MATH_THEOREM_K17_DROP12_GLOBAL_HS_SOURCE_COVER_20260803.md`, SHA-256
`7556ec953b062a88810b81f26163ff8c86616019dbaa44a6ac9ce1216d1b30ca`.

This audit gives an independent all-arity proof of the source-cover claim
and directly replays the literal `Z/N` profiles from the frozen all-`U`
ledger.  It does not use occurrence feasibility or full child supplier
rank as an input.

## 1. Bound inputs

```text
compressed parent
  e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
literal final
  fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c
structural catalogue
  790fae940cd80c05e35656027dcb57139180b54c77f567c9b5333ab5d4581434
U112621 endpoint ledger
  f1d9ab4ad29d4806d1b3e6a7518dda17733cd415c24e34a5aa8865f236f067db
Q23 head ledger
  479302b36bf84710d2f5339177d28fd1db86127573646a23009c1bf6252cc5ca
Q23 supplier ledger
  5686f140d3ad542a0d5ed2df5dd832cba1427d208ec9dad21cbb6cd217be3abb
all-U Q23 class ledger
  160fd9c41409ef8bc99977efbeae4a5e45b8da4c492792cdb0ba4d7273d9f58c
class producer audit
  0ef424731eff130de4d9af1aae7d58cdf765b5f695c30ad19da624fdf8ed4df6
independent class replay
  aaef0f9c3923800c4ed353b8f8a0f72196c7c9a79c3c04729babe540d8a3a478
```

The inherited shore has 23 heads and the two parent supplier identities

\[
 a=12973,\qquad b=14851,
\]

with distinct two-head incidence masks

\[
 B_0(a)=\mathtt{c000},\qquad B_0(b)=\mathtt{10004}.
\]

Every structural mode has two endpoints, changes only those endpoint rows,
and retires at most its one length-three donor head.  For an
endpoint-disjoint family, endpoint rows and retired donor heads are
therefore pairwise distinct.

## 2. Independent all-arity subadditivity proof

For one mode `e`, let `D_e` be its retired-head set, `N_e` its post-transfer
neighbor-identity set on the surviving inherited shore, and put

\[
 A_e=N_e\setminus N_0,\qquad C_e=N_0\setminus N_e,
 \qquad
 \gamma_e=|D_e|+|A_e|-|C_e|.
\]

For an endpoint-disjoint family `X`, define `D_X`, `N_X`, `A_X`, `C_X`
analogously after simultaneous materialization.

### 2.1 Gains inject into singleton gains

Take `u in A_X`.  An unchanged source row cannot become a new neighbor,
because simultaneous materialization only rewrites selected endpoints and
only removes inherited heads.  Thus `u` is an endpoint of a unique selected
mode `e`.  Its joint mask satisfies

\[
 B_e(u)\cap (Q\setminus D_X)\ne\varnothing.
\]

Since `D_e subseteq D_X`,

\[
 Q\setminus D_X\subseteq Q\setminus D_e,
\]

so the same row is already a singleton gain: `u in A_e`.  Endpoint
disjointness makes the sets `A_e` pairwise disjoint.  Hence the identity map
is an injection

\[
                    A_X\hookrightarrow\mathop{\dot\bigcup}_{e\in X}A_e.
\tag{2.1}
\]

Additional modes can erase a singleton gain by retiring its last active
head, but cannot create a gain absent from every singleton.

### 2.2 Singleton casualties persist and are disjoint

Take `s in C_e`.  If `s` were not an endpoint of `e`, it would keep its two
distinct parent `Q` neighbors.  Since one mode retires at most one `Q` head,
at least one neighbor would survive, contradicting `s in C_e`.  Therefore
`s` is an endpoint of `e`.

No other member of an endpoint-disjoint family rewrites row `s`.  The joint
child uses the same endpoint mask `B_e(s)` and only restricts it to the
smaller active-head set `Q-D_X`.  Since it was already empty on `Q-D_e`, it
remains empty jointly.  Thus

\[
                         C_e\subseteq C_X.             \tag{2.2}
\]

If one old supplier belonged to both `C_e` and `C_f`, it would be an
endpoint of both modes, contradicting endpoint disjointness.  Therefore the
singleton casualty sets embed disjointly:

\[
             \mathop{\dot\bigcup}_{e\in X}C_e\subseteq C_X.   \tag{2.3}
\]

There may be additional joint-only casualties when different modes retire
the two heads of one old supplier; these only strengthen (2.3).

### 2.3 Credit inequality

Donor disjointness gives `D_X=dotunion_e D_e`.  Combining this with
(2.1)--(2.3),

\[
\begin{aligned}
 \sum_{e\in X}\gamma_e-\gamma_X
 &=\left(\sum_e|A_e|-|A_X|\right)
   +\left(|C_X|-\sum_e|C_e|\right)\\
 &\ge0.
\end{aligned}
\]

Consequently

\[
                       \boxed{\gamma_X\le\sum_{e\in X}\gamma_e}. \tag{2.4}
\]

This proves the proposed inequality for every arity, not just triples.

## 3. Direct all-`U` ledger replay

The frozen TSV was read row by row, without inferring profiles merely from
the class labels.  The replay obtained the exact class census

```text
H 468, S 47, Z 112099, N 7.
```

For every one of the 112,099 `Z` rows it checked simultaneously:

```text
retired mask                         0
old host/donor Q masks               0,0
post host/donor Q masks              0,0
post old-supplier masks              c000,10004
post neighbor identities             2
gamma                                0
```

There were zero failures.

For every one of the seven `N` rows it checked simultaneously:

```text
LR host                              14851
retired mask                         0
post host/donor Q masks              0,0
post old-supplier masks              c000,0
post neighbor identities             1
gamma                               -1
```

There were zero failures.  The seven edge IDs are exactly
`52844,...,52850`.  Since they share endpoint 14851, at most one can occur
in an endpoint-disjoint family.

This direct replay independently confirms the theorem's stronger contextual
description: every `Z` action is the identity on the inherited shore, while
one admitted `N` action deletes only supplier `b`.  Hence a source-free
family has credit exactly zero (`Z` only) or minus one (`Z` plus one `N`).

## 4. Source-cover consequence

The authenticated singleton classes have

\[
 \gamma_e=
 \begin{cases}
  1,&e\in H\cup S,\\
  0,&e\in Z,\\
 -1,&e\in N.
 \end{cases}
\]

If `X cap (H union S)` is empty, (2.4) gives `gamma_X<=0`; the direct
profile replay gives the sharper values in Section 3.  A child of supplier
deficiency at most 20 requires `gamma_X>=1` on the inherited 23/2 shore.
Therefore every such endpoint-disjoint child contains an `H` or `S` mode.
In particular every target-capable triple has a distinguished `H/S` source
coordinate.

## 5. Exact scope and excluded restoration mechanisms

The GO applies only to simultaneous endpoint-disjoint selections from the
authenticated `U112621` catalogue on the literal `e878/fa491` parent, with
the fixed semantic completion and fixed endpoint masks used by the Q23
oracle.

Within this scope another mode cannot restore a singleton casualty: it
cannot rewrite the casualty row, activate a retired head, or identify a
different physical row with the same supplier identity.  It can only retire
more heads, which preserves or enlarges the casualty set.

The proof does **not** cover:

* overlapping transfers, where another mode may rewrite the same supplier
  row;
* root/common-basis recoupling or representation rematerialization, where
  an endpoint mask can become context-dependent;
* actions which activate or replace inherited `Q` heads;
* another parent, root subset, structural catalogue, or noncanonical mode;
* occurrence packing, chronology, residence, upper/compiler gates, or the
  sufficiency of the full child supplier matching.

The phrase "rank-improving" must be read here as reaching supplier rank at
least 16878, equivalently supplier deficiency at most 20.  The theorem is a
necessary inherited-shore cut, not a general rank-additivity statement.

## 6. Verdict

The theorem at final frozen SHA
`7556ec953b062a88810b81f26163ff8c86616019dbaa44a6ac9ce1216d1b30ca`
is **GO** in its declared scope.  Both the all-arity gains/casualties proof
and the independent literal profile replay exclude a hidden restoration or
positive source-free composition.
