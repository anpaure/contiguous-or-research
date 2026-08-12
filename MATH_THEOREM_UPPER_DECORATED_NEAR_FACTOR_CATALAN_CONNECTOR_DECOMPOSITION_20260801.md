# Upper-decorated near-factors split exactly into a Catalan forest, a connector forest, and a bounded Hall residue

Date: 2026-08-01  
Lane: additive-constant regeneration / remaining rooted host gate  
Status: exact equivalence and finite replay.  The two large pieces are not constructed uniformly.

## 0. Outcome

Fix one perfect matching `M0` of the middle-levels incidence graph `ML_m`
between ranks `m-1,m` of `[2m-1]`.  Put

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U={2W\over m+1}=\operatorname{Cat}_m.                 \tag{0.1}
\]

The exact upper-decorated `s`-component certificate from
`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`
has a forced two-scale decomposition:

1. an upper-exact **rooted Catalan forest** with `W-C=U` edges and exactly
   `C` path components;
2. `C-s` further matching edges forming a forest on those Catalan
   components; and
3. a residual perfect matching on `s` vertices per shore.

Conversely those three objects give an upper-surjective q1 factor with at
most `s` components.

Thus the `O(1)` rooted-host gate is not one opaque `W`-edge search.  Its
irreducible global part is an exact Catalan four-resource forest followed by
a Catalan-scale component connector.  Ordinary Hall is needed only for the
last `O(1)` edges.

The result is also a sharp warning: any successful upper-surjective
`O(1)`-component host necessarily contains such a Catalan forest as a
subcertificate.  The ordered-four-transversal obstruction has not been
removed by the small protected-factor theorem; it has been located exactly.

## 1. Rooted link coordinates

Let

\[
 {cal L}={ [2m-1]\choose m-1},\qquad
 {cal M}={ [2m-1]\choose m}.
\]

For every incidence `e=LU` not in `M0`, define

\[
 \operatorname{up}(e)=M_0(L)\cup U\in{[2m-1]\choose m+1}, \tag{1.1}
\]

and the directed link

\[
                  \lambda(e):L\longrightarrow M_0^{-1}(U).\tag{1.2}
\]

For a matching `Q subset ML_m-M0`, distinct edges have distinct tails and
distinct heads.  Hence its links form a directed partial permutation.  We
retain edge labels; graphic independence excludes a loop, an opposite
parallel pair, or an ordinary undirected cycle.  In `ML_m` loops were already
removed with `M0`, and an opposite pair would make an incidence `C4`, which
does not exist.

Call `Q0` a **rooted Catalan forest** when

1. `Q0` is a matching in `ML_m-M0`;
2. `up` is a bijection from `Q0` to the `U` rank-`m+1` colours; and
3. the labelled links `lambda(Q0)` are graphic-independent.

Since `|Q0|=U=W-C`, its link forest spans `W` lower vertices and has exactly
`C` components, including isolated vertices.

## 2. Exact decomposition theorem

### Theorem 2.1 (Catalan forest plus connector forest)

Fix `0<=s<=C`.  The following are equivalent.

1. There is a matching `Q subset ML_m-M0` of size `W-s` such that
   `up(Q)` covers every rank-`m+1` colour and `lambda(Q)` is
   graphic-independent.
2. There are `Q0,Q1 subset ML_m-M0` whose union is a matching, such that
   * `Q0` is a rooted Catalan forest;
   * `|Q1|=C-s`; and
   * after contracting every component of `lambda(Q0)`, the labelled links
     of `Q1` form a loopless forest.

Under either condition `Q=Q0 union Q1`.  If the graph left after deleting
the endpoints of `Q` has a perfect matching, then `M0` and the completed
second matching form an upper-surjective q1 factor with at most `s`
components.

#### Proof

Assume 1.  For each upper colour choose one edge of `Q` carrying it, and let
`Q0` be the set of chosen edges.  Since `Q` is a matching and its links are
graphic-independent, the same is true of every subset.  The `U` choices are
therefore a rooted Catalan forest.  Put `Q1=Q\Q0`.  Its size is

\[
                         (W-s)-U=C-s.                       \tag{2.1}
\]

Adding the links of `Q1` to the forest `lambda(Q0)` creates no cycle.
Equivalently, after contracting the old components they form a loopless
forest.

Conversely, a forest of links between distinct components of another forest
has acyclic union.  Their union is a matching by hypothesis, and `Q0`
already carries every upper colour, so their union satisfies 1.

Finally complete `Q` by the residual perfect matching `R`, and put
`M1=Q union R`.  Then `M0 union M1` is a q1 factor and is upper-surjective.
The permutation `M0^{-1}M1` has component count

\[
 W-r_{\rm gr}(\lambda(M_1))
 \le W-r_{\rm gr}(\lambda(Q))
 =s.                                                        \tag{2.2}
\]

This proves the last assertion.  \(\square\)

### Corollary 2.2 (protected plus-phase version)

Properly edge-colour a 2-bounded protected plus bank

\[
                         P=P_0\mathbin{\dot\cup}P_1.
\]

Theorem 2.1 preserves `P` provided `M0` contains `P0`, `Q0 union Q1`
contains `P1`, and the residual matching avoids every already selected edge.
Thus the fixed-`H` rooted-host gate is exactly the search for a protected
rooted Catalan forest and protected connector forest, followed by an
`s=O(H)` Hall instance.

The small protected-factor theorem guarantees a two-factor containing `P`
without these two forests.  It cannot manufacture them after the fact.

## 3. Exact converse from a decorated factor

Let `F=M0 union M1` be an upper-surjective q1 factor with `c` components.
Delete one `M1` edge from each permutation cycle, obtaining `Q`.  Then
`lambda(Q)` is a spanning forest with `c` components and `|Q|=W-c`.

If the deleted occurrences are upper-transparent--every deleted colour is
still carried by `Q`--then Theorem 2.1 applies with `s=c`.  Select one
remaining occurrence of every upper colour to obtain `Q0`; all other kept
edges are `Q1`.  The deleted edges are the residual perfect matching.

For the additive-constant target, exact transparency can be weakened.  The
deletion loses at most `c` upper colours, so a `c=O(1)` factor gives the same
decomposition with `O(1)` named terminal casualties, payable by bounded
eviction or literal append.

This is the precise sense in which component openings and upper damage are
the same bounded sidecar row.

## 4. What the Catalan count means

The forced count `C` has two simultaneous interpretations.

1. It is the excess of q1 occurrences over immediate-upper colours:
   \[
                         W-U=C.                             \tag{4.1}
   \]
2. It is the number of components of every rooted Catalan forest:
   \[
                  W-|Q_0|=W-U=C.                           \tag{4.2}
   \]

Thus every exact upper transversal begins at Catalan component scale.  An
`O(1)`-component factor must spend `C-O(1)` additional, occurrence-compatible
connector edges.  This is a global synchronization problem; fixed-`H`
protected factor extension alone has no numerical leverage over it.

The theorem suggests a clean attack order:

1. construct the rooted Catalan forest `Q0` with the protected plus collars;
2. prove a connector Hall/graphic theorem on its `C` components, leaving
   only `O(H)` components;
3. solve the remaining `O(H)`-vertex Hall problem and charge any opened upper
   colours to the terminal sidecar.

The first row is the rooted ordered-four-transversal gate.  The second is
the exact topology gate.  They should not be conflated with the final small
Hall completion.

## 5. Finite calibration at `m=4`

The audit freezes an upper-surjective q1 factor on `ML(7)` whose permutation
cycles have lower-shore lengths

\[
                              3,11,21.                       \tag{5.1}
\]

One upper-transparent cut in each cycle leaves a matching `Q` of size 32.
Choosing one occurrence of each of the 21 upper colours gives

\[
 |Q_0|=21=W-C,qquad C=14,\qquad |Q_1|=11=C-3.             \tag{5.2}
\]

The 21 links of `Q0` form a 14-component forest; the 11 connector links
reduce it to three components; and the three cut edges are exactly the
residual perfect matching.  This is a literal replay of Theorem 2.1, not a
dimension count only.

Run

```text
python3 scratch/audit_upper_decorated_near_factor_catalan_connector_20260801.py
```

Canonical payload SHA-256:

```text
5991ddb5d3a405fe89670408867efe520f67530e5f85b995fe09bf9b8cc5c894
```

## 6. Exact remaining statement

The strongest isolated owner-layer theorem still missing is:

> **Protected rooted Catalan-connector theorem.**  For every fixed protected
> plus-phase collar bank in sufficiently large dimension, there is a rooted
> Catalan forest `Q0` containing its first matching shore and a disjoint
> connector forest `Q1` of size `C-O(1)` containing its second shore, such
> that the `O(1)` unmatched vertices satisfy residual Hall and only `O(1)`
> named upper colours are lost at the openings.

Together with the fixed-`H` q1 planting theorem this would close owner degree,
q1, immediate upper palette and bounded topology.  Residence outside the
protected collars, arbitrary-width upper witnesses, and complete compiler
damage would still require their separate guarded rows.
