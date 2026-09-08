# Endpoint-retaining long circuits: exact palette algebra and residence drift

**Date:** 2026-08-02  
**Status:** exact theorem plus an independently replayed `k=17` calibration.
The finite calibration is deliberately limited to the rank-eight/rank-ten factor,
one-cycle topology, and positive/zero residence.  Ranks 11--17, a depth-three
source, and the lower compiler are separate rows.

## 1. The exchange

Let `F` be a simple two-factor on rank-`r` owners.  Its rows are indexed by
rank-`r-1` facets, and the row at `f` is an edge whose endpoint intersection
is `f`.  Choose distinct facets `f_i`, moving owners `x_i`, and retained
owners `y_i`, with indices in `Z/tZ`, such that

\[
 e_i=\{x_i,y_i\},\qquad
 f_i=x_i\cap y_i=x_{i+1}\cap y_i.                 \tag{1.1}
\]

Replace each `e_i` by

\[
 e_i'=\{x_{i+1},y_i\}.                            \tag{1.2}
\]

Call this an endpoint-retaining circuit of row length `t`.

### Theorem 1 (exact central and immediate-palette algebra)

The symmetric difference in the owner--facet incidence graph is the
alternating circuit

\[
 x_0-f_0-x_1-f_1-\cdots-x_{t-1}-f_{t-1}-x_0,
                                                               \tag{1.3}
\]

of length `2t`.  After (1.2):

1. every facet row is still used exactly once;
2. every owner degree is unchanged;
3. every retained endpoint `y_i` is unchanged in its row; and
4. the rank-`r+1` cap load satisfies the exact identity

\[
 M'(U)=M(U)-\#\{i:x_i\cup y_i=U\}
              +\#\{i:x_{i+1}\cup y_i=U\}.          \tag{1.4}
\]

Consequently the immediate upper palette is complete iff `M'(U)>=1` for
every cap `U`.  Equality of the old and new cap multisets is sufficient but
not necessary.  A particularly useful sufficient face is

\[
 M(x_i\cup y_i)\ge2
 \quad\hbox{for every cap not recreated by the circuit}.       \tag{1.5}
\]

#### Proof

At row `f_i`, (1.1) deletes the incidence `x_i-f_i` and inserts
`x_{i+1}-f_i`; the incidence `y_i-f_i` is retained.  The inserted and deleted
moving incidences alternate as (1.3).  Each `x_i` is deleted once and
inserted once, while each `y_i` is unchanged.  This proves the facet and
degree assertions.  Only the displayed edge unions change, giving (1.4)
and its two consequences. \(\square\)

This theorem is the endpoint-retaining specialization of the general
integer-kernel row in the existing physical-circuit theorem.  Its useful new
point here is that long circuits may be fuelled by cap **slack** rather than
being cap-multiset exact.

## 2. Exact topology

Delete the old edges `e_i`.  The retained factor is a path system.  Give
each deleted-edge endpoint occurrence a port.  Let `alpha` pair the two
ports which lie at opposite ends of the same retained path, and let `beta`
pair ports joined by the new edges.

### Theorem 2 (terminal involution test)

The new factor has `c(alpha beta)/2` components.  In particular it is one
cycle iff `alpha beta` has two permutation cycles.

If the construction is developed from a quotient under `Z_m`, and the
quotient terminal cycle has voltage `v`, the developed factor has

\[
                         \gcd(m,v)                         \tag{2.1}
\]

components.  Thus a quotient one-cycle lifts to a physical Hamilton cycle
iff `gcd(m,v)=1`.

#### Proof

The union of the two fixed-point-free involutions is the suppressed terminal
two-factor.  Every alternating component is counted twice by `alpha beta`,
which proves the first assertion.  Traversing one quotient component changes
phase by `v`; the phase permutation has `gcd(m,v)` cycles. \(\square\)

## 3. Residence is a finite-state boundary functional

Fix residence depth `d`.  For one coordinate, use states

\[
                 0,1,2,\ldots,d,d+1,                       \tag{3.1}
\]

where `0` means that the last symbol was zero, `j<=d` means that the active
positive run has length `j`, and `d+1` means length at least `d+1`.  Reading
one increments the positive state, capped at `d+1`; reading zero sends every
state to zero and charges one short run exactly from states `1,...,d`.

Every oriented retained path therefore has an exact state/cost transfer
map.  Reversing the path uses the independently computed reversed transfer.

### Theorem 3 (exact retained-path automaton)

For a fixed cut set, the number and deficit of short positive runs in any
terminal rethread are obtained by composing the transfer maps in the order
specified by its port matching.  Hence all internal retained-path
contributions cancel when two terminal rethreads are compared; the exact
residence drift is a function only of the oriented path transfers and their
new joins.

The same statement holds for zero gaps after complementing the coordinate
trace.

#### Proof

The automaton records exactly the only information a prefix can pass to its
successor: whether a run is open, and its length up to the acceptance
threshold.  Composition is therefore identical to scanning the concatenated
binary trace.  A retained path occurs once in each rethread, possibly with
opposite orientation, so its strictly internal completed runs are unchanged;
only its transfer state participates in the terminal comparison. \(\square\)

There is a simpler useful corollary.  Suppose no retained path is identically
one in the coordinate under study.  For an oriented path `P`, let `h(P)` and
`t(P)` be its leading and trailing positive-run lengths, capped at `d+1`.
For a join `P->Q`, define

\[
 b(P,Q)={\bf1}_{0<t(P)+h(Q)\le d}.                         \tag{3.2}
\]

Then the short-run drift is

\[
 \Delta S=\sum_{\text{new joins}}b(P,Q)
          -\sum_{\text{old joins}}b(P,Q).                 \tag{3.3}
\]

When all-one fragments occur, Theorem 3 rather than (3.3) is exact.

### Definition (clean merger absorber)

An endpoint circuit is a clean merger absorber when its automaton boundary
charge is nonpositive for every affected coordinate and strictly negative
for at least one.  Such a circuit has provably negative residence drift.
More generally, a finite sequence of circuits is an accepting return packet
when the composed transfer state returns to the guarded terminal face with
negative total charge.  No monotonicity of intermediate factors is required.

This is the precise long-circuit successor to standard local `C6` pulls:
support may be arbitrarily long, while exact acceptance remains a bounded
finite-state calculation for fixed `d` and support size.

## 4. The authenticated `k=17` `C10` calibration

The old factor is

```text
scratch/k17_upper_decorated_longrun_circuit_20260802/seed3502/
  floor3553.factor.tsv
```

and the terminal factor is

```text
scratch/k17_upper_decorated_longrun_circuit_20260802/seed3502/
  c10_escape_from3553.factor.tsv
```

with SHA-256 values

```text
3049f49f3bc52273bfcb874786795ab3984978a5e7f741b0ee3cc85dcfbade7e
33d6719dbd6f5bc49e3b7c31f0350385c9ac2de035e767a82680ca137e5cf7be
```

The quotient moving-owner circuit is

\[
 6905\to13747\to9655\to9687\to6891\to6905.               \tag{4.1}
\]

Its five representative facet rows are

\[
 6873,9651,9623,4843,6889.                                \tag{4.2}
\]

The free `Z_17` development changes 85 physical facet rows, i.e. seventeen
literal incidence `C10`s.  An independent row-by-row C++ replay proves:

* every rank-eight facet once;
* every rank-nine owner of degree two;
* every rank-ten cap covered;
* all 3,944 protected rows unchanged; and
* one physical cycle.

The 85 physical changes split into exactly seventeen directed moving-owner
cycles of length five.  Formula (1.4) changes 136 cap multiplicities, so the
exchange is not cap-multiset exact; nevertheless every removed cap has old
load at least two and all 19,448 cap values remain covered.  This is a literal
instance of the slack-fuelled condition (1.5).

The positive residence vector changes by

\[
 (0,1972,1581)\longmapsto(0,1938,1564),                  \tag{4.3}
\]

so the number of positive short runs drops by `51=3*17`, and the positive
deficit drops by `85=5*17`.  Equivariance is literal: each coordinate has
short-run drift `-3` and deficit drift `-5`.  The zero side changes by

\[
 8500\longmapsto8534,                                    \tag{4.4}
\]

showing that this is a one-polarity residence absorber, not a bi-resident
packet.  Each coordinate has zero-gap-count drift `+2`, while its zero-deficit
drift is zero; the total zero-deficit score is unchanged at 18,156.

The independent replay artifacts are

```text
scratch/audit_k17_endpoint_circuit_longrun_20260802.cpp
scratch/k17_upper_decorated_longrun_circuit_20260802/longrun3502.audit.json
scratch/k17_upper_decorated_longrun_circuit_20260802/longrun3502.trace.tsv
```

with SHA-256 values

```text
47feac9f900322af7aa05396fc4ee00ba6ebb734d5d467e897e8a940348df177
95f34c453b60905206413f8796af09828a1a2d03d34cd52870d41412685e441b
ffaa63590a0fa9b5622f4e91ff261d9c18a031ac9f61440cd73798d8a7972038
```

### 4.1 A genuinely bi-resident `C14`

A later exact census supplies a stronger calibration.  Its old and new
factors are

```text
/home/amodo/or15/work/root_k17_c68b_c6xc6_20260802/greedy_residence/
  c10c12_escape_from3111.factor.tsv
  c14_escape_from3094.factor.tsv
```

with SHA-256 values

```text
4921aea3c4b48ecdb974e1ecbd68bc76ca771dd920b44b0234da81ced6381ffe
d46c2146359464d2b716ab46e01698b2321ad3ca016f28328be1b1e77ba1a222
```

The complete quotient-length-seven census contains 3,840,798 simple
endpoint circuits, of which 907 are cap-safe, 268 retain one physical cycle,
and four improve positive residence.  The selected circuit develops to 119
physical row changes, namely seventeen directed moving-owner cycles of
length seven.  Independent replay gives

\[
\begin{array}{c|ccc|c|c}
 &\#1&\#2&\#3&\text{short count}&\text{deficit}\\ \hline
\text{positive, old}&0&1598&1496&3094&4692\\
\text{positive, new}&0&1564&1496&3060&4624\\
\text{zero, old}&3400&2448&2380&8228&17476\\
\text{zero, new}&3366&2465&2346&8177&17374.
\end{array}                                                     \tag{4.5}
\]

Thus every coordinate has drift

\[
 (\Delta S_+,\Delta D_+,\Delta S_0,\Delta D_0)=(-2,-4,-3,-6). \tag{4.6}
\]

This is a literal clean merger absorber for both polarities.  Unlike the
first `C10`, it removes some load-one caps; the same compound circuit
recreates every such value, as required by (1.4).  Hence the two exact cap
closure mechanisms seen in practice are now both authenticated:

1. spend only duplicate cap occurrences; or
2. transport last-witness cap units around the full long circuit.

The independent artifacts are

```text
scratch/k17_upper_decorated_longrun_circuit_20260802/longrun3060.audit.json
scratch/k17_upper_decorated_longrun_circuit_20260802/longrun3060.trace.tsv
```

with SHA-256 values

```text
9b444788c3e17bb46a40e8ad445ccb0a6194f0361757f3a81320f5b66d6935a2
a142a77b3d6c95bca242dbe69df4d85982ba407e526cc4cbd7803187efa732eb
```

## 5. Boundary of the theorem

The theorem proves an exact exchange language for searching beyond standard
Mütze `C6` pulls.  It does **not** prove a uniform supply of clean merger
absorbers, residence zero, or a bounded accepting return path.  It also does
not claim preservation of ranks 11--17, a literal depth-three antecedent, or
the lower common-cap/compiler incidence graph.  Those must be audited as
separate gates after every accepted terminal factor.
