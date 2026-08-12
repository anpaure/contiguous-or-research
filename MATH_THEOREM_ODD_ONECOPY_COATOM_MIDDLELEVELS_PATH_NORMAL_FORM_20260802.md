# Odd one-copy trace rounding forces a Middle Levels path cover

**Date:** 2026-08-02  
**Status:** unconditional necessary normal form, and an unconditional
central-projection converse.  It applies to the lower labelled trace row in
odd dimension.  It does **not** prove the bounded-chain factor, the literal
depth-`d` source lift, residence, upper shadows, or the terminal compiler.

## 0. Result

Put

\[
        k=2r-1,\qquad
        W={k\choose r}={k\choose r-1},
\]

and let `d>=1`.  Consider a linear order-`d` de Bruijn trail containing

* exactly one coloured trace for every rank-`r` owner;
* exactly one marked occurrence of every rank-`(r-1)` target; and
* `C` additional uncoloured bridge traces.

Every marked value is required to be the union of a proper suffix of its
coloured trace.  Parallel occurrences remain distinct, while the owner
labels and the rank-`(r-1)` target labels are each used once.

### Theorem 0.1 (coatom path-cover normal form)

The rank-`r` owners and rank-`(r-1)` marked targets admit a vertex-disjoint
alternating path cover in the Middle Levels graph with at most `C+1` paths.
More precisely, every maximal block of consecutive coloured traces

\[
                   e_a,e_{a+1},\ldots,e_b
\]

projects to the simple alternating path

\[
 T_a,Q_a,T_{a+1},Q_{a+1},\ldots,T_b,Q_b,             \tag{0.1}
\]

where `T_i` is the owner of `e_i` and `Q_i` is its unique marked coatom.
The paths together use every rank-`r` and every rank-`(r-1)` vertex once.

Consequently:

1. with no bridge trace, a linear one-copy chronology projects to a Middle
   Levels Hamilton path;
2. a cyclic one-copy circulation with no bridge projects to a Middle Levels
   Hamilton cycle; and
3. an additive-`C` lower-trace sidecar can destroy at most `C` of the
   coloured-to-coloured Middle Levels links.

The converse holds at the central projection: any alternating Hamilton
cycle, or any alternating path cover, already gives the required one-copy
owner/coatom incidence table.  What it does not give is a literal
order-`d` source word carrying the deeper marked chains.

This separates the integral sequel to the stationary pull clock as follows.

\[
\boxed{
\begin{array}{c}
\text{coatom-rooted bounded chain factor}\quad\text{(open)}\\
\Downarrow\\
\text{Middle Levels owner/coatom path cover}\quad\text{(automatic)}\\
\Downarrow\\
\text{literal depth-}d\text{ overlap/source realization}\quad\text{(open).}
\end{array}}
\]

Thus owner/coatom topology is not an additional marginal rounding
obstruction in odd dimension.  The remaining one-copy obstruction is the
correlated bounded chainization and literal moving-core trace state.

## 1. Trace notation

Let

\[
                 e=(B_0,B_1,\ldots,B_d)              \tag{1.1}
\]

be a coloured trace.  Its owner, tail-state union, and head-state union are

\[
\begin{aligned}
 T(e)&=B_0\cup\cdots\cup B_d,\\
 L(e)&=B_0\cup\cdots\cup B_{d-1},\\
 H(e)&=B_1\cup\cdots\cup B_d.
\end{aligned}                                         \tag{1.2}
\]

The trace marks some distinct proper suffix unions.  Since those values are
nested, it can mark at most one rank-`(r-1)` set: two nested sets of the same
rank are equal.

There are `W` coloured traces and exactly `W` rank-`(r-1)` targets.  Hence
every coloured trace marks exactly one such target.  Denote it by `Q(e)`.
It satisfies

\[
                   Q(e)\subseteq H(e)\subseteq T(e). \tag{1.3}
\]

All `Q(e)` are distinct and run through the complete rank-`(r-1)` layer.

## 2. A coloured adjacency forces the coatom state

### Lemma 2.1 (head-union rigidity)

Let coloured trace `e` be immediately followed in the de Bruijn trail by a
coloured trace `f`.  Their owner labels are distinct.  Then

\[
                         H(e)=Q(e).                  \tag{2.1}
\]

In particular,

\[
                         Q(e)\subset T(f).           \tag{2.2}
\]

#### Proof

Consecutive de Bruijn traces share the state consisting of the last `d`
letters of `e` and the first `d` letters of `f`.  Therefore

\[
                         H(e)=L(f)\subseteq T(f).     \tag{2.3}
\]

If `H(e)` had rank `r`, then (1.3) would give `H(e)=T(e)`.  Equation (2.3)
would then imply

\[
                         T(e)\subseteq T(f).
\]

Both sets have rank `r`, so their owners would be equal, contrary to the
one-copy owner labels.  Thus `H(e)` has rank below `r`.  It contains the
rank-`(r-1)` set `Q(e)`, so it must equal `Q(e)`.  Equation (2.2) follows
from (2.3).  \(\square\)

The argument is occurrence-level.  It does not assume that the source
letters are singletons, that the trace has a positive age composition, or
that every proper suffix is marked.

## 3. Proof of the path-cover theorem

Split the full de Bruijn trail at its `C` uncoloured bridge traces.  The
remaining coloured traces form at most `C+1` maximal linear blocks.

Take one such block `e_a,...,e_b`, and write

\[
                         T_i=T(e_i),\qquad Q_i=Q(e_i).
\]

For every `a<=i<=b`, (1.3) gives `Q_i subset T_i`.  For every `i<b`,
Lemma 2.1 gives `Q_i subset T_(i+1)`.  Hence all consecutive incidences in

\[
                  T_a,Q_a,T_{a+1},Q_{a+1},\ldots,T_b,Q_b
                                                               \tag{3.1}
\]

are edges of the Middle Levels graph.

Every `T_i` is distinct by one-copy owner exactness, and every `Q_i` is
distinct by one-copy coatom exactness.  The two ranks are disjoint shores,
so (3.1) is a simple path.  Different coloured blocks use disjoint owner and
coatom labels.  Their union covers all `W+W` middle-level vertices.  This
proves Theorem 0.1.  \(\square\)

For a cyclic trace circulation, the same proof is cyclic.  With no bridge,
the final coloured trace is followed by the first, so the last coatom also
joins the first owner and (3.1) closes to a Hamilton cycle.

### Corollary 3.1 (contracted rainbow form)

In the bridge-free cyclic case, the coatom order

\[
                         Q_0,Q_1,\ldots,Q_{W-1}       \tag{3.2}
\]

is a Hamilton cycle in `J(2r-1,r-1)`, and

\[
                         Q_i\cup Q_{i+1}=T_{i+1}      \tag{3.3}
\]

(cyclic indices).  In particular, the `W` edge-union colours in (3.2) are
all different and are exactly the rank-`r` layer.

Conversely, every cyclic ordering of all coatoms satisfying (3.3), with the
unions all different, expands uniquely at the central projection to a
Middle Levels Hamilton cycle by inserting `T_(i+1)=Q_i union Q_(i+1)`.

#### Proof

Both `Q_i` and `Q_(i+1)` are different rank-`(r-1)` subsets of the
intervening rank-`r` owner `T_(i+1)`.  Their union is therefore that owner.
All coatom and owner labels are one-copy.  The converse is immediate by
alternating the displayed coatoms with their consecutive unions.  \(\square\)

This is the precise rainbow-Johnson contraction of the Middle Levels row.
It shows that the projected owner chronology is a classical Hamilton
object; the extra OR-word content lies in its labelled age flags.

## 3A. Exact literal moving-core criterion

The remaining literal condition can also be stated without reference to a
de Bruijn graph.  Fix a cyclic coatom order (3.2) satisfying (3.3), and put

\[
 \alpha_i=Q_i\setminus Q_{i+1},\qquad
 \beta_i=Q_{i+1}\setminus Q_i.                       \tag{3.4}
\]

Both are singletons; below we identify them with their elements.  A
depth-`d` **age flag** on `Q_i` is an ordered partition

\[
                  Q_i=C^i_0\mathbin{\dot\cup}\cdots
                         \mathbin{\dot\cup}C^i_{d-1}. \tag{3.5}
\]

Empty age cells are permitted.  Its suffix thresholds are

\[
                  F^i_t=C^i_0\cup\cdots\cup C^i_t,
                  \qquad 0\le t<d.                   \tag{3.6}
\]

### Theorem 3.2 (age-flag spelling equivalence)

The coatom/owner cycle has a literal cyclic depth-`d` source spelling with
state-union `Q_i` and owner `T_(i+1)=Q_i union Q_(i+1)` at every turn if
and only if it has age flags (3.5) such that, cyclically for every `i`,

\[
 \alpha_i\in C^i_{d-1},\qquad
 C^{i+1}_{t+1}\subseteq C^i_t\quad(0\le t<d-1),       \tag{3.7}
\]

and

\[
\begin{split}
 C^{i+1}_0={}&\{\beta_i\}
 \mathbin{\dot\cup}(C^i_{d-1}\setminus\{\alpha_i\})\\
 &\mathbin{\dot\cup}
   \mathop{\dot\bigcup}_{t=0}^{d-2}
      (C^i_t\setminus C^{i+1}_{t+1}).                 \tag{3.8}
\end{split}
\]

For such a spelling, the proper suffix unions available on the trace whose
head-state union is `Q_i` are exactly the flags `F^i_t`.  Hence a prescribed
coatom-rooted chain `C_i` is carried by that trace if and only if every
member of `C_i` is one of the threshold sets in (3.6).

#### Proof

Take the `d` source letters whose union is `Q_i`, and put a coordinate in
`C^i_t` when its most recent occurrence is `t` positions before the newest
letter.  The coordinate `alpha_i` disappears at the next shift, so its most
recent occurrence must be in the dropped oldest letter.  This gives the
first part of (3.7).  A coordinate of age `t<d-1` either survives without a
new occurrence and acquires age `t+1`, or is refreshed into age zero.  This
gives the survivor inclusions in (3.7).  Every old coordinate not selected
as a survivor is refreshed, except for `alpha_i`, which leaves; the unique
new coordinate `beta_i` is born.  These disjoint alternatives are exactly
(3.8).

Conversely, spell the cyclic source word by taking the new letter at turn
`i` to be `C^(i+1)_0`.  Equation (3.8) makes it nonempty (it contains
`beta_i`) and says exactly that shifting the old `d`-letter state and
appending this letter produces the next labelled age partition.  Iterating
cyclically realizes all the declared states.  The dropped oldest letter
contains `alpha_i`; all of its other coordinates are refreshed by (3.8).
Thus the intervening `(d+1)`-window has union
`Q_i union {beta_i}=T_(i+1)`.  Finally, a suffix ending at the newest
letter contains precisely the coordinates whose most recent occurrence has
age at most its threshold, giving (3.6).  \(\square\)

The theorem is an exact necessary-and-sufficient moving-core formulation.
It is stronger than unlabelled age-type balance: it couples the departing
coordinate, the newborn coordinate, every survivor, and every named chain
threshold around one rainbow Hamilton cycle.

## 4. Static chainization is the earlier integral gate

Let `R` be the residual named lower-target bank assigned to coloured traces.
Assume it contains the complete rank-`(r-1)` layer, as it does in the
canonical triangular/Ferrers construction once `d<r-1`: the Ferrers boundary
occupies only its first `d` ranks.

### Corollary 4.1 (coatom-rooted chain partition)

Any exact one-copy marked trace table partitions `R` into `W` inclusion
chains of size at most `d`, one below each owner, and every chain has a
different rank-`(r-1)` maximum.

#### Proof

The marked suffix values of one trace form an inclusion chain and there are
at most `d` proper suffix positions.  Exact named-target usage makes the
chains disjoint and gives union `R`.  Section 1 shows that each trace has
exactly one coatom.  Since every other marked value is a subset of that
coatom, it is the chain maximum.  \(\square\)

Thus zero-defect integral rotor rounding already implies the sharp static
triangular chain factor.  Fractional stationarity, aggregate age-semigroup
integrality, and successor-flow total unimodularity cannot bypass this
chainization requirement.

There is a useful central converse.  Suppose such a coatom-rooted chain
partition has somehow been constructed.  Choose any Middle Levels Hamilton
cycle and one of its parity matchings from coatoms to owners.  Assign the
chain with maximum `Q` to its matched owner `T`; containment of the maximum
implies containment of the whole chain.  This gives owner exactness and a
Hamilton owner/coatom projection simultaneously.  Equivalently, one may use
the already-proved central-matching SCD extension theorem.

This converse is only static/projected.  It does not show that the chain
members occur as suffix unions in a common order-`d` source word.

### Corollary 4.2 (one-sided uniform full-lattice consequence)

Suppose, more generally, that the nonempty lower half of `B_(2r-1)` has a
coatom-rooted partition into `W` chains of size at most `d+C`.  Then the
entire Boolean lattice has a Dilworth partition into `W` chains, every one
of size at most

\[
                         2(d+C)+2.                    \tag{4.1}
\]

For the canonical deadline `d`, this is strictly less than

\[
                  {2^k\over W}+2C+4.                 \tag{4.2}
\]

#### Proof

Index the lower chains by their coatom maxima `Q`.  Make a bipartite graph
between two copies of the coatom layer, joining `Q` to `R` when
`Q cap R=emptyset`.  It is `r`-regular: the complement of `Q` has size `r`,
and `R` is obtained by deleting one of those `r` points.  Hence the graph
has a perfect matching; write its bijection as `R=f(Q)`.

For each `Q`, concatenate

\[
        C_Q
        \quad\hbox{with}\quad
        \{[k]\setminus S:S\in C_{f(Q)}\}.             \tag{4.3}
\]

The second family is a chain in the reverse order.  Its least member is
`[k] setminus f(Q)`, which contains `Q` because `Q cap f(Q)=emptyset`.
Thus (4.3) is one chain.  The lower families partition ranks `1,...,r-1`,
and the complemented families partition ranks `r,...,k-1`.  Add the empty
set and `[k]` to one of the chains.  This proves (4.1).

For odd `k`,

\[
             \Lambda=2^{k-1}-1,
             \qquad d\le\left\lceil{\Lambda\over W}\right\rceil,
\]

because the displayed ceiling is already admissible in the definition of
`d`.  Therefore

\[
 2(d+C)+2
 \le 2{\Lambda\over W}+2C+4
 ={2^k\over W}+2C+4-{2\over W},
\]

which gives (4.2).  \(\square\)

Thus, on the zero-boundary face (or after the boundary targets have also
been absorbed into the `W` coatom chains), even the **static**
additive-constant chainization would imply a one-sided additive-constant
form of uniform Dilworth chain decomposition: no chain is more than a
constant above the average `2^k/W`.  This does not give the lower-size half
of Furedi's uniform-chain conjecture, but it shows that the missing static
theorem has substantial independent combinatorial content; it is not a
routine rounding of the trace circulation.

## 5. Consequence for fixed-owner stationary rotors

The stationary pull-clock construction clears denominators inside periodic
clocks attached to a fixed owner.  A one-copy odd chronology has the
opposite local geometry: every coloured-to-coloured successor link changes
owner and projects through the intervening coatom.

### Corollary 5.1 (global moving-core necessity)

Start from any denominator-cleared disjoint union of owner-local stationary
clock components, and select exactly one coloured trace from every owner.
None of the old within-component successor links can remain between two
selected coloured traces, because both endpoints of such a link have the
same owner while only one trace of that owner was selected.

Therefore every coloured-to-coloured successor link in a one-copy trail is
a cross-owner rethread.  With `C` bridge traces, at least
`max(0,W-C-1)` linear successor links (and `max(0,W-C)` in the cyclic
convention) must be supplied by the moving-core construction rather than
inherited from the owner-local clock.

#### Proof

Each old owner-local successor link joins two occurrences carrying the same
owner label.  A one-copy selection contains at most one of those occurrences,
so it contains no old link with both endpoints selected.  A trail with `W`
coloured and `C` bridge edges has at least `W-C-1` coloured-to-coloured
adjacencies in the linear convention; every one is consequently new.  The
cyclic count gains the closing adjacency.  \(\square\)

This does not lower-bound added **word length**: a global rethread may change
all successor links at zero sidecar cost.  It does rule out a local proof
which keeps the owner-local rotor cycles and merely joins a bounded number
of them.  The integral theorem must be global from the outset.

## 6. Exact remaining statement

For odd dimensions, the lower one-copy problem is now separated into two
Boolean-specific rows.

1. **Deadline chainization.**  Construct the coatom-rooted partition of the
   residual lower ideal into `W` chains of size at most `d`, together with
   the small Ferrers boundary chains.
2. **Literal moving-core realization.**  Choose the Middle Levels path/cycle
   and source letters so those chains occur as proper suffix unions while
   all adjacent `d`-letter state overlaps agree.

After a static chain table has been chosen, fixed-head balance is the
already-proved capacitated Hall problem, and a Hall-safe spanning-tree
skeleton is necessary and sufficient for one Euler component.  The present
theorem shows why those flow rows do not create the static table: the table
itself is an equitable coatom-rooted Boolean chain decomposition.

The Middle Levels theorem removes only the projected owner/coatom topology.
It does not prove either row 1 or row 2, and it does not imply residence,
arbitrary-width upper witnesses, or common-cap/compiler feasibility.
