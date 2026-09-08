# Double-bridge/two-path repairs in the quotient endpoint graph

Date: 2026-07-28

## 1. Endpoint exchange model

Fix a quotient sigma assignment.  Each lower colour `e` owns one unordered
edge

\[
o_e=\{u_e,v_e\}
\]

in the quotient middle graph.  Replacing its add-pair chooses another edge
`n_e`.  A family of replacements preserves middle degree two exactly when

\[
\sum_e(\mathbf 1_{n_e}-\mathbf 1_{o_e})=0
\tag{1.1}
\]

coordinatewise on the quotient vertices.

When `o_e` and `n_e` share one endpoint, orient the replacement from the old
endpoint that disappears to the new endpoint that appears.  Its contribution
to (1.1) is `-source+target`.  Consequently a degree-preserving family of
such replacements is a disjoint union of directed cycles.  This is the move
class enumerated by `k13_endpoint_cycle_native.cpp`.

## 2. One-double-edge lemma

**Lemma.** Suppose exactly one replacement has disjoint old and new edges

\[
\{a,b\}\longrightarrow\{c,d\}.
\]

All remaining replacements share one endpoint.  Then (1.1) holds if and only
if their directed arcs decompose into directed cycles plus two paths, with
endpoint pairing either

\[
c\leadsto a,\qquad d\leadsto b,
\]

or

\[
c\leadsto b,\qquad d\leadsto a.
\]

All changed lower colours must of course be distinct.

**Proof.** The double replacement contributes

\[
\mathbf e_c+\mathbf e_d-\mathbf e_a-\mathbf e_b.
\]

Thus the ordinary arcs must have divergence

\[
\mathbf e_a+\mathbf e_b-\mathbf e_c-\mathbf e_d.
\]

Delete directed cycles.  Flow decomposition leaves two unit paths from the
two negative-divergence vertices `c,d` to the two positive-divergence
vertices `a,b`, in one of the two pairings.  The converse follows by summing
the path divergences.  \(\square\)

This is a complete characterization, not a heuristic enlargement of the
simple-cycle catalogue.

## 3. The exact five-hole repair

The nonmonotone five-hole seed is

```
scratch/k13_q1h5_q2u1_res0_l3.certificate.json
```

and the repaired certificate is

```
scratch/k13_q1h5_repairu2_hamming9.certificate.json.
```

They differ on only six lower colours.  The unique double replacement is

```
lower 119: old edge (4,21) -> new edge (73,3).
```

The other five changes are exactly the two paths

```
3 -> 17 -> 14 -> 4     (lowers 111,429,215),
73 -> 37 -> 21         (lowers 571,349).
```

Hence the entire Hamming repair is the lemma with no residual directed
cycle.  It restores upper-q2 orbit `2991`, keeps five upper-q1 holes,
preserves residence, and leaves the all-lower compiler Hall graph with
deficiency zero.

This explains the earlier computational discrepancy: exhaustive simple
endpoint cycles through length ten could not find the repair because the
repair is not a directed cycle in the one-endpoint transition graph.

## 4. Current finite search consequence

For the four-hole debt states

```
branch A: lower-q2 hole 233,
branch B: lower-q2 hole 339,
branch C: lower-q2 hole 121,
```

the next complete local catalogue is:

1. choose a double replacement whose collar can create the missing q2
   target;
2. enumerate the two endpoint pairings;
3. enumerate two lower-disjoint directed paths returning the new endpoints
   to the old endpoints;
4. retain only exchanges preserving the upper-q1 budget, both q2 sides,
   residence, connectivity, and nonzero voltage;
5. run the exact all-lower Hall/compiler audit.

The q5 repair proves that this class is necessary in practice and sufficient
for at least one previously inaccessible debt closure.  It does not yet prove
that one of the three q4 debts has a repair in this class.

