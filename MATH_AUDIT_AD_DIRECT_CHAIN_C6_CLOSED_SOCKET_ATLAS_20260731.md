# Independent audit of the direct-chain C6 closed-socket atlas

Date: 2026-07-31  
Lane: AD independent replay  
Verdict: **PASS**, with the explicit scope below.

## 1. Scope authenticated

The audit uses the stored orientations in

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
```

and treats two different objects separately:

* formal structural forests `F_3,...,F_7`;
* selected strict upper/lower direct hosts only for `n=3,...,6`.

The stored `F_7` is the ambient output of the `n=6` step.  It does not
contain a selected `Q_7`, strict direct occurrence catalogues, or a child
`n=7` side state.  The audit therefore makes no strict `n=7` claim.  It also
does not quantify over arbitrary path reorientations and does not infer a
protected pointwise cap or compiler cap absent from the source.

## 2. Independent checks

The companion verifier authenticates both compact atlas payloads, the
source payload, and the builder hash.  It checks independently:

1. every strict installed/native/role/rooted/closed census row;
2. every exact raw phase-disjoint bank maximum;
3. the unique closed socket and its endpoint action;
4. both near-closed serial-ear ledgers; and
5. every structural installed/closed count through `F_7`.

The strict rows are

\[
\begin{array}{c|c|rrrrr|r}
n&\text{shore}&\text{installed}&\text{native}&\text{zero role}&
 \text{rooted}&\text{closed}&\text{raw max}\\\hline
3&U&0&0&0&0&0&0\\
3&L&0&0&0&0&0&0\\
4&U&2&0&0&1&0&2\\
4&L&1&0&1&1&0&1\\
5&U&11&0&2&2&0&10\\
5&L&9&1&0&0&0&6\\
6&U&55&3&13&15&1&40\\
6&L&66&2&11&13&0&52.
\end{array}                                             \tag{2.1}
\]

Here `rooted` counts integral fundamental minors of determinant `+1` or
`-1`; the columns are individual, not cumulative, predicates.

The structural installed/closed pairs are

\[
 (4,1),(24,5),(96,24),(358,68),(1230,232)              \tag{2.2}
\]

for `F_3,...,F_7`.

## 3. Decisive literal rows

The unique strict closed socket is upper `n=6`, socket `30`.  Its forced
orientation bits are `(1,1,1)`, its role displacement is zero, its rooted
minor is one, and its endpoint action is

\[
                         (77\;215\;122).                \tag{3.1}
\]

Hence the exact strict closed-bank maximum is `1` above and `0` below at
`n=6`, and is zero on both shores through `n=5`.  In particular the joint
two-shore closed-bank density in this stored chain is zero.

Upper socket `42` is native, linear-forest and rooted, with endpoint action
`(100 144)`, but has the forced two-owner role debt

\[
 \{(2887,H),(3909,T)\}\longrightarrow
 \{(2887,T),(3909,H)\}.                                \tag{3.2}
\]

Lower socket `57` is endpoint-neutral and rooted, but has

\[
 \{(1132,H),(1633,T)\}\longrightarrow
 \{(1132,T),(1633,H)\}.                                \tag{3.3}
\]

These ledgers do not cancel.  They are serial-ear leads, not closed sockets.

## 4. Mathematical proof audit

The installed-line formula is exactly the two `A_3` phase cosets of one
suspended C6.  A cyclic local symmetry stays within one phase; only an odd
local symmetry of the decorated candidate host exchanges the phases.

For a line family of size `h` and maximum atom degree `Delta`, a line meets
at most `3(Delta-1)` other lines.  A maximal matching therefore has order at
least

\[
                  \left\lceil{h\over3\Delta-2}\right\rceil.    \tag{4.1}
\]

This is a resource-bank theorem only until rooted cross-block dependencies
are added.  The stabilizer-orbit density theorem correctly requires the
genuine automorphism group of the full decorated state, not the ambient
symmetric group.

For endpoint parity, cutting three old arcs and contracting unchanged
fragments leaves three temporary head/tail labels.  The opposite C6 phase
composes them with a 3-cycle; eliminating the temporary labels contributes
the same sign on both sides.  The relative decoded endpoint action is even
and supported on at most three old path labels, hence is the identity or a
3-cycle.  This proves the parity obstruction but does not apply to a packet
with nonzero role debt such as socket `42`.

## 5. Scope boundary

The audit proves an exact finite obstruction to a **static closed** C6 bank
in this authenticated chain.  It does not obstruct:

* a different decorated host;
* overlapping, state-dependent serial ears;
* an odd actuator carrying and later cancelling role debt;
* a co-designed planted off phase; or
* a compiler-aware common-cap construction.

Thus the correct replacement is a stateful serial/overlapping socket atlas,
not a claim that C6 geometry itself is absent.

## 6. Reproducibility

The frozen files and their SHA-256 values are listed in the final theorem
footer and the accompanying handoff item.  The independent machine-readable
verdict is

```text
scratch/ad_direct_chain_c6_closed_socket_atlas_20260731.independent.json
```

with canonical payload

```text
381282b633c68e72a63ce1f1fd8e6ad0453919a341807a09047abcf0819c1f4d
```
