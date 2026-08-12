# `k=17` `c68b.greedy48`: physical-circuit locality, residence brackets, and deep upper cones

**Date:** 2026-08-02  
**Lane:** L  
**Status:** exact mathematical reduction and census protocol.  The baseline
rows below are independently replayed.  No single- or paired-circuit finite
verdict is asserted in this note until the physical catalogue and literal
replay fields in Section 9 are filled and independently audited.

## 1. Authenticated input and exact open rows

The fixed input is

```text
scratch/k17_c68b_double_fusion_residence_greedy_20260802/
  c68b.greedy48.factor.tsv
```

with SHA-256

```text
b1343737cb0e3d99dec503e526e566521504478af1c5792c9a7949b6a5796616
```

It is a simple cycle

\[
                 C=(T_i)_{i\in\mathbb Z_W},\qquad W=24310,       \tag{1.1}
\]

through every rank-nine owner exactly once.  Its edges use every rank-eight
intersection exactly once and cover every rank-ten union.  The rank-ten
load histogram is

\[
        1^{16762}2^{1530}3^{170}4^{952}5^{34}.             \tag{1.2}
\]

There are 3,944 immutable protected physical edges.  The cycle has

\[
 2312\text{ positive runs of length }2,qquad
 1887\text{ positive runs of length }3,                    \tag{1.3}
\]

so its positive short-run count and deficit are respectively

\[
                  S(C)=4199,qquad D(C)=6511.              \tag{1.4}
\]

All these runs are free under `Z_17`; their orbit counts are `136,111`.
The exact cyclic all-width owner-union deck is

| rank | covered | total | holes |
|---:|---:|---:|---:|
| 11 | 10,370 | 12,376 | 2,006 |
| 12 | 5,797 | 6,188 | 391 |
| 13 | 2,346 | 2,380 | 34 |
| 14--17 | complete | complete | 0 |

The missing ranks 11--13 form `118,23,2` free orbits.  The two missing
rank-thirteen representatives are `0x0afbf` and `0x0b5ff`.

These are middle-owner facts.  They do not give a source chronology,
depth-three compiler, common cap, or word.

## 2. The literal physical exchange class

Write

\[
 F_i=T_i\cap T_{i+1},\qquad A_i=T_i\cup T_{i+1}.           \tag{2.1}
\]

Thus `F_i` has rank eight and `A_i` has rank ten.  A physical exchange
chooses `s` mutable facet occurrences and replaces

\[
 e_f^- =\{X_f,Y_f\}\quad\hbox{by}\quad
 e_f^+ =\{X'_f,Y'_f\},qquad
 X_f\cap Y_f=X'_f\cap Y'_f=f.                             \tag{2.2}
\]

The following rows are exact and must all be tested on physical occurrence
labels.

### Theorem 2.1 (owner, palette, cap, and simplicity rows)

The replacement (2.2) is a simple rank-eight-rainbow two-factor precisely
when

1. no protected facet occurrence is changed;
2. the added physical edges are distinct and duplicate no retained edge;
3. every owner is balanced:

   \[
   \sum_f\bigl({\bf1}_{X'_f}+{\bf1}_{Y'_f}
              -{\bf1}_{X_f}-{\bf1}_{Y_f}\bigr)=0.        \tag{2.3}
   \]

The rank-eight palette is then preserved literally, because the facet
address `f` of each changed row is unchanged.  If `M(A)` is the old
rank-ten edge-union load and `r(A),a(A)` are the removed and added
multiplicities, immediate-upper completeness is preserved exactly when

\[
                         M(A)-r(A)+a(A)\ge1               \tag{2.4}
\]

for every rank-ten mask `A`.

#### Proof

One old and one new edge occupy each changed facet row, so the lower palette
is unchanged.  Equation (2.3) is exactly preservation of degree two at each
owner.  The two simplicity tests rule out an edge multiplicity.  Only the
displayed rank-ten edge unions change, giving (2.4).  \(\square\)

Exact cap-multiset equality is sufficient but is not necessary.  In
particular, (1.2) makes last-witness protection a substantial row: a removed
load-one cap must be recreated by the same compound exchange.

### Theorem 2.2 (one-component port test)

Delete the `s` old edges from the cycle and distinguish the resulting `2s`
endpoint occurrences as ports.  Let `alpha` pair the two ports belonging to
the same retained path fragment, and let `beta` pair ports joined by the new
edges.  The new physical factor has

\[
                            \frac{c(\alpha\beta)}2         \tag{2.5}
\]

components.  Hence it is one cycle iff `c(alpha beta)=2`.

Here ports are occurrences, not merely owner masks; an isolated retained
owner has two distinct port occurrences.  Formula (2.5) is therefore valid
also when two adjacent old edges are deleted.

#### Proof

Both `alpha` and `beta` are fixed-point-free involutions.  Their alternating
union is the suppressed new factor.  Each alternating union cycle gives two
cycles of the permutation `alpha beta`, proving (2.5).  \(\square\)

## 3. Exact positive-run support

For a positive run `R` of coordinate `z`, define its **closed bracket**
`B(R)` to be its internal owner-cycle edges together with its two boundary
edges.  Thus a run of length `ell` has `ell+1` bracket edges.

### Lemma 3.1 (bracket necessity)

If no edge of `B(R)` is deleted by an exchange, then `R` is still the same
maximal positive run in the final one-cycle order.

#### Proof

All internal edges of the run and both edges joining it to its zero-valued
neighbours remain.  They therefore remain one literal path segment with the
same two zero boundary values in every degree-two completion.  \(\square\)

### Lemma 3.2 (ten brackets per Johnson edge)

Every owner-cycle edge belongs to the closed positive-run brackets of
exactly ten coordinates.

#### Proof

Its two rank-nine endpoints have a rank-eight intersection and rank-ten
union.  The eight intersection coordinates are `1,1`, so the edge is
internal to their positive runs.  The two union-minus-intersection
coordinates are `1,0` and `0,1`, so the edge is a boundary of one positive
run for each.  The remaining seven coordinates are `0,0`.  \(\square\)

### Theorem 3.3 (physical and equivariant locality floors)

An exchange deleting `s` physical edges can change at most `10s` old short
positive runs.  Consequently every flat resident repair of the fixed
`greedy48` order has

\[
                             s\ge\left\lceil4199/10\right\rceil=420. \tag{3.1}
\]

On a `Z_17`-equivariant face, the 247 short-run orbits require at least

\[
                         \left\lceil247/10\right\rceil=25 \tag{3.2}
\]

changed quotient facet orbits.  Thus length-four quotient circuits alone
require at least seven circuits.  A construction using only literal
physical `C8`s requires at least 105 such circuits.  These are support lower
bounds, not no-go theorems or sufficiency statements.

#### Proof

By Lemma 3.1 every old short run must be hit.  Lemma 3.2 bounds the number
hit by one deleted edge.  The equivariant assertion is the same argument
after quotienting free run and edge orbits.  \(\square\)

The exact lower bound for any restricted catalogue is the transversal
number of

\[
            \{B(R)\cap E_{\rm mutable}:R\text{ old short positive}\}. \tag{3.3}
\]

An empty member is an immediate protected no-go.  A fractional packing of
these bracket sets gives a proof certificate stronger than (3.1) whenever
available.

## 4. Exact run delta from a finite port graph

Delete the old seams of a proposed exchange.  For each coordinate `z`, make
one token for every positive block in a retained fragment which meets at
least one port.  Give it weight equal to its number of owners, capped at
four.  Across either the old or new seam matching, join two tokens exactly
when the two incident endpoint values are both one.  Add token weights in a
component, again capping at four.

### Theorem 4.1 (weighted-token replay)

The affected positive runs are exactly the connected components of this
token graph.  A component is short exactly when its capped weight is below
four.  Hence

\[
 \Delta S=#\{\text{new token components of weight}<4\}
          -\#\{\text{old token components of weight}<4\}.              \tag{4.1}
\]

Positive runs wholly internal to retained fragments cancel.  Formula (4.1)
is exact even when several cuts lie inside one old run; it does not freeze
an old mate or assume marginal additivity.

#### Proof

Inside a retained fragment, maximal positive blocks are unchanged.  A seam
merges precisely the two incident blocks whose endpoint bits are both one;
all other seams terminate the blocks.  Transitive closure therefore gives
exactly the new maximal positive runs.  Capping at four preserves precisely
the short/safe dichotomy.  \(\square\)

As an independent invariant, any simple cycle through every rank-nine owner
and every rank-eight facet once has exactly 1,430 positive runs in each
coordinate: degree counting gives `2*C(16,8)-2*C(16,7)=2860` transition
edges, hence 1,430 runs.  An implementation should assert this after every
accepted move.

## 5. Exact all-width upper replay

For a cycle `C`, let

\[
 w_C(U)=\#\{\text{cyclic owner intervals }I:\bigcup_{i\in I}T_i=U\}. \tag{5.1}
\]

The count is by interval occurrence, not merely by distinct target value.
After deleting the old seams, call an old interval **crossing** if it uses at
least one deleted seam.  Define `a_-(U)` to count such old occurrences and
`a_+(U)` to count new-cycle intervals using at least one added seam.  An
interval crossing several seams is counted once.

### Theorem 5.1 (crossing-occurrence identity)

For every target mask `U`,

\[
                         w_{C'}(U)=w_C(U)-a_-(U)+a_+(U).   \tag{5.2}
\]

Consequently a covered target can be lost only if all its old witnesses are
crossing, and it then survives iff a new crossing witness is created.  A
missing target is filled iff `a_+(U)>0`.

#### Proof

The deleted edges split the old cycle into retained path fragments.  Every
interval contained in one fragment persists in the new cycle; if the
fragment is reversed, reverse the interval as well.  This is an
OR-preserving bijection.  Precisely the crossing occurrences remain to be
removed and added, giving (5.2).  \(\square\)

### Lemma 5.2 (rank locality)

If `|U|=r`, every proper interval with union `U` has at most

\[
                              {r\choose9}                 \tag{5.3}
\]

owners, because its owners are distinct rank-nine subsets of `U`.  In
particular the exact radii at ranks 11, 12, and 13 are `55,220,715`.

Thus ranks 11--13 admit a finite seam-collar replay even though all interval
widths are allowed.

### Theorem 5.3 (deep-target upper-cone support)

If a changed interval of rank `r` crosses a seam `e`, then its union contains
the rank-ten cap `A(e)` of that seam.  Therefore gains and casualties at rank
`r` are supported respectively in

\[
 \bigcup_{e\in E^+}\{U:A(e)\subseteq U,\ |U|=r\},\qquad
 \bigcup_{e\in E^-}\{U:A(e)\subseteq U,\ |U|=r\}.         \tag{5.4}
\]

For one seam in `k=17`, the numbers of possible supersets at ranks 11
through 17 are

\[
                         7,21,35,35,21,7,1.               \tag{5.5}
\]

Hence an `s`-edge exchange can fill at most `7s,21s,35s` missing targets at
ranks 11, 12, and 13.  A physical `C8` (`s=4`) can fill at most
`28,84,140`, or 252 in total, before any chronology or collision test.
Across all ranks 11--17, each sign of the deck delta is supported on at most
`127s` seam-target incidences.

#### Proof

An interval crossing `e` contains both endpoint owners and hence their
union `A(e)`.  A fixed rank-ten subset has exactly
`C(7,r-10)` rank-`r` supersets.  Summing gives (5.5).  \(\square\)

This upper-cone condition is necessary, not sufficient: the relevant
suffix and prefix owners must occur in the new order and have union exactly
`U`.

### Proposition 5.4 (linear-time all-width audit)

For a fixed start `i` and coordinate `x`, let

\[
 \tau_i(x)=\min\{t\ge0:x\in T_{i+t}\}.                   \tag{5.6}
\]

Then

\[
             \bigcup_{j=0}^{t}T_{i+j}=\{x:\tau_i(x)\le t\}. \tag{5.7}
\]

Since `T_i` already has nine coordinates, at most eight new arrival times
exist.  Sorting them gives at most nine distinct OR states for this start;
the gaps between consecutive arrival times give their exact occurrence
multiplicities.  Maintaining next occurrences in a doubled cycle therefore
computes the complete all-width occurrence table `w_C` in `O(17W)` time
(with the constant-size sorting absorbed).  This audits ranks 14--17 as
well: their old hole count is zero, so an accepted circuit must create none.

## 6. Physical circuits versus quotient circuits

A one-endpoint-retaining quotient circuit of row length `ell` has a net
moving-owner holonomy `h` in `Z_17`.  Put `g=gcd(17,h)`.

### Theorem 6.1 (moving-cycle lift decomposition)

Its moving-owner development consists of `g` directed cycles.  Each cycle
selects a balanced physical exchange using

\[
                    \frac{17}{g}\ell\text{ old edges and }
                    \frac{17}{g}\ell\text{ new edges},                  \tag{6.1}
\]

old and new rows.  If, in addition, its retained owner occurrences are all
distinct and meet the moving occurrences only in the prescribed alternating
order, this exchange is a simple alternating circuit of length
`2(17/g)ell`; without that simplicity hypothesis it is a closed balanced
alternating module, not necessarily a simple circuit.

#### Proof

Following one quotient lap advances the physical phase by `h`.  The phase
permutation has `gcd(17,h)` cycles, each of length `17/g`; multiplying by
the `ell` quotient rows proves (6.1).  Every retained endpoint is balanced
within its own row (one old and one new incidence), while the directed cycle
balances the moving endpoints.  Thus each lifted moving cycle is an
independently selectable balanced exchange.  The final assertion is exactly
the stated physical-occurrence simplicity test.  \(\square\)

Thus `h=0` gives 17 independently selectable balanced physical modules;
the modules passing the occurrence-simplicity test are physical
`C_(2ell)`s, and for `ell=4` they are literal physical `C8`s.  Since 17 is
prime, `h!=0` gives one large balanced module, which is a simple alternating
circuit of length `34ell` only after the same test.  A quotient-row toggle
which applies all 17 phases is not a census of the individual `h=0` physical
modules.  Physical cap loads, protected occurrences, simplicity, topology,
run delta, and the all-width deck must be replayed after choosing the actual
lift components.

There is a second scope distinction.  A directed cycle of row replacements
enumerates only the class in which every old/new row pair retains one owner.
The complete balanced physical class is (2.2)--(2.3); its minimal circuits
may contain rows with no retained endpoint.  Such `2+2`, `3+1`, or other
compound geometries are not ruled out by a one-endpoint directed-cycle
census.

## 7. Why paired circuits are not marginally additive

Let `Q_1,Q_2` be two candidate circuits.

* Rank-ten cap changes add on disjoint facet supports, but a pair may be
  safe even when each member individually deletes a last witness.
* Component count is computed from the union port involution.  Two circuits
  which individually split the cycle may jointly return one cycle.
* Residence is computed from the union weighted-token graph.  A boundary
  token exposed by one circuit may be joined by the other.
* Equation (5.2) must use the union of cut seams.  A new interval may cross
  both supports, and two marginal ledgers may charge the same target or the
  same old occurrence.

Accordingly a complete disjoint-pair census must start from the raw
protected balanced circuits, including individually cap-unsafe and
disconnected members, and enforce (2.4), (2.5), (4.1), and (5.2) only on the
combined state.  If supports overlap, the second circuit must be regenerated
from the literal first prefix; adding two stale patches is not sound.

Marginal addition is justified only on an explicitly verified private face:
no tracked old or new interval crosses both collars, the positive-token
graphs split between the collars, and the external port pairing is block
diagonal.  For **hole-count** columns one must additionally require target
privacy: no target value has affected occurrences in two collars.  Without
target privacy the occurrence-count deltas still add, but the predicate
`w(U)=0` need not.  On that additive face, if every circuit has effect column

\[
 v_Q=(\Delta S,\Delta H_{11},\Delta H_{12},\Delta H_{13})                \tag{7.1}
\]

and there is a nonzero vector `lambda>=0` with

\[
                              \lambda\cdot v_Q\ge0                       \tag{7.2}
\]

for every allowed column, then no nonnegative combination of those private
circuits is a strict componentwise Pareto improvement.  This is a valid
positive-cut obstruction.  It says nothing about interacting circuits off
the additive face.

## 8. Exact acceptance and Pareto scope

For the present task, a single or compound candidate is **admissible** only
after all of the following literal checks pass:

1. protected facet occurrences fixed;
2. simple physical edge set, every owner degree two, every rank-eight facet
   once;
3. every rank-ten cap still covered;
4. exactly one physical component;
5. complete all-width replay at ranks 11--17, with no new holes at ranks
   14--17; and
6. the positive short-run and deficit histograms rebuilt from the final
   physical order.

A rank-11--13/positive-residence Pareto improvement means

\[
 (S,H_{11},H_{12},H_{13})_{\rm new}
 \le (4199,2006,391,34)                                   \tag{8.1}
\]

componentwise, with at least one strict inequality, unless a different
lexicographic objective is explicitly declared.  A decrease in the sum
alone is not a Pareto theorem.  Rank-ten completeness and the zero holes at
ranks 14--17 are hard guards, not objective credits.

## 9. Finite census ledger to fill after independent replay

The following rows deliberately remain result placeholders in this
mathematical note.

### 9.1 Single physical lift components

```text
PENDING_INDEPENDENT_AUDIT
raw h=0 physical C8 components:
raw h!=0 larger lift circuits, by support:
protected/simple/balanced:
rank10-safe:
one-component:
rank14--17-safe:
Pareto-improving at (S,H11,H12,H13):
best exact vector and witness SHA:
```

### 9.2 General balanced circuits outside the one-endpoint class

```text
PENDING_INDEPENDENT_AUDIT
support bound and enumerated geometries:
raw / protected / cap-safe / connected counts:
Pareto-improving count:
best exact vector and witness SHA:
```

### 9.3 Paired circuits

```text
PENDING_INDEPENDENT_AUDIT
pair universe (disjoint or sequentially regenerated):
raw pairs:
final protected/cap-safe/connected:
rank14--17-safe:
Pareto-improving count:
best exact vector and witness SHA:
```

The earlier `round048` search and its pair shell are useful candidate
generators, but they act on complete quotient option rows.  They do not by
themselves fill Section 9.1's individual physical-lift row or Section 9.2's
general balanced-circuit row.

## 10. Boundary of the theorem

This note proves exact locality, replay, and acceptance criteria.  It does
not prove that any such circuit exists, that the baseline is locally
optimal in a catalogue not fully replayed, or that a Pareto-improving factor
has a depth-three antecedent.  Even an all-width upper-complete resident
owner cycle still requires source-occurrence binding, a literal terminal
compiler/common-cap certificate, and final word verification.
