# The fixed PBBS whole fan reduces exactly to a cover-free cyclic interval factor

**Date:** 2026-08-06  
**Method:** coordinate supports, maximal antecedent envelopes, and minimal
interval covers; no computation or search  
**Status:** unconditional exact compatibility theorem and minimal-obstruction
classification.  The fixed PBBS whole-fan section creates no additional
owner-side coupling.  A proposed mixed-length target table is compatible
with it exactly when its source intervals pass one cover-free cut for every
coordinate.  The stationary mixed rotor does not yet provide such an
interval table on the fixed PBBS chronology.  The remaining assertion is
therefore one PBBS-relative cover-free one-copy rounding lemma, not another
fractional rank-marginal or owner-occurrence theorem.

## 1. Fixed owner row and prescribed source cells

Let

\[
                         T=(T_i)_{i\in\mathbb Z_W}             \tag{1.1}
\]

be a cyclic simple rank-`r` Johnson chronology, and let `d<W/2`.  For a
source word `A`, the prescribed owner equations are

\[
                         T_i=\bigcup_{p=i}^{i+d}A_p.           \tag{1.2}
\]

Write

\[
 O_i=[i,i+d],
 \qquad
 P_p=\bigcap_{i=p-d}^{p}T_i.                                \tag{1.3}
\]

Thus `P` is the maximal depth-`d` antecedent.  Suppose a family `L` of
named strict-lower targets has been assigned pairwise distinct nonempty
cyclic source intervals

\[
                         S\longmapsto I_S,
 \qquad                         |I_S|\le d.                   \tag{1.4}
\]

The source equations to be solved are

\[
                         \bigcup_{p\in I_S}A_p=S
                         \qquad(S\in\mathcal L).              \tag{1.5}
\]

No disjointness of the intervals is assumed.

For a coordinate `x`, define the owner-negative and target-negative
regions

\[
 N_x^{\rm own}=\bigcup_{i:x\notin T_i}O_i,
 \qquad
 N_x^{\rm tar}=\bigcup_{S:x\notin S}I_S,                    \tag{1.6}
\]

and the surviving support

\[
                         Q_x=\mathbb Z_W\setminus
                              (N_x^{\rm own}\cup N_x^{\rm tar}).
                                                                    \tag{1.7}
\]

The point of using the union in (1.6) is that a coordinate absent from one
prescribed interval value is forbidden at every source position of that
interval.

## 2. Exact coordinate criterion

### Theorem 2.1 (PBBS-relative cover-free criterion)

There is a nonempty set-valued source word `A` satisfying simultaneously
(1.2) and (1.5) if and only if, for every coordinate `x`,

\[
 O_i\cap Q_x\ne\varnothing
                    \qquad(i:x\in T_i),                     \tag{2.1}
\]

and

\[
 I_S\cap Q_x\ne\varnothing
                    \qquad(S:x\in S).                       \tag{2.2}
\]

When these conditions hold, the coordinatewise maximal solution is

\[
                         A_p^*=\{x:p\in Q_x\}.               \tag{2.3}
\]

It is automatically nonempty at every source position.

#### Proof

Suppose `A` exists and put

\[
                         E_x=\{p:x\in A_p\}.                 \tag{2.4}
\]

Every owner or target interval whose declared value omits `x` is disjoint
from `E_x`.  Hence `E_x subseteq Q_x`.  Every declared interval whose
value contains `x` must meet `E_x`, proving (2.1)--(2.2).

Conversely use (2.3).  If `x notin T_i`, then `O_i subseteq N_x^(own)`;
if `x notin S`, then `I_S subseteq N_x^(tar)`.  Thus the corresponding
unions of `A^*` omit `x`.  Equations (2.1)--(2.2) give the reverse
inclusions for every positive coordinate.  Therefore all owner and target
unions have exactly their prescribed values.

It remains only to check that no letter is empty.  On a simple Johnson
trace the exact forced set at position `p` is

\[
 F_p=\{D_p,I_{p-d-1}\}\subseteq P_p,                        \tag{2.5}
\]

with the two labels allowed to coincide.  For `x=D_p`, the owner window
`O_p` has `p` as its only owner-compatible source position at the terminal
end of that run.  For `x=I_(p-d-1)`, the owner window `O_(p-d)` has `p` as
its only owner-compatible source position at the initial end.  Condition
(2.1) consequently forces `p in Q_x` for every `x in F_p`.  Hence

\[
                         F_p\subseteq A_p^*,                 \tag{2.6}
\]

and `A_p^*` is nonempty.  \(\square\)

This proves necessity and sufficiency without a separate word variable for
each coordinate.  Once the intervals are chosen, (2.3) is the unique
coordinatewise maximal filling.

## 3. Maximal-envelope form and the mandatory aperture

The owner-negative part of (1.7) has a closed form.

### Lemma 3.1

For every coordinate `x`,

\[
 \mathbb Z_W\setminus N_x^{\rm own}
 =\{p:x\in P_p\}.                                           \tag{3.1}
\]

Consequently

\[
 A_p^*
 =P_p\cap\bigcap_{S:p\in I_S}S,                            \tag{3.2}
\]

where the intersection over an empty target family is the ground set.

#### Proof

A position `p` avoids every owner-negative window exactly when every owner
window containing `p` has `x` in its label.  Those windows are
`O_(p-d),...,O_p`, whose labels intersect to `P_p`.  This proves (3.1),
and substitution into (1.7) proves (3.2). \(\square\)

Thus Theorem 2.1 is equivalently the deterministic pinned-envelope test

\[
 \bigcup_{p\in O_i}A_p^*=T_i,
 \qquad
 \bigcup_{p\in I_S}A_p^*=S.                                \tag{3.3}
\]

The familiar mandatory-core aperture is an atomic consequence.  If
`p in I_S`, then every feasible table must obey

\[
                         \boxed{F_p\subseteq S.}             \tag{3.4}
\]

Indeed every antecedent letter contains `F_p`, and its inclusion in the
target interval forces (3.4).  Conversely, (3.4) for all target intervals
through `p` gives `F_p subseteq A_p^*`, but the positive-hit conditions
(2.1)--(2.2) remain necessary for optional coordinates.

## 4. Exact PBBS whole-fan compatibility

Let `S_PBBS` be the fixed PBBS whole-fan edge section.  It supplies, for
every strict-lower target `S`, a read-only consecutive owner path `K_S`
with

\[
                         \bigcap_{i\in K_S}T_i=S.             \tag{4.1}
\]

After complementation the same path supplies the paired proper-upper
value.

### Corollary 4.1 (whole-fan decoupling is exact)

Fix the labelled PBBS owner chronology and its section `S_PBBS`.  The
pairing

\[
                         S\longmapsto(K_S,I_S)                \tag{4.2}
\]

is realized in one ordinary word if and only if the source intervals
`I_S` satisfy Theorem 2.1.  Mutual overlaps among the owner paths `K_S`
create no further cut.

#### Proof

The owner paths depend only on the fixed tuple `T`.  Theorem 2.1 is exactly
the existence criterion for an antecedent of this same tuple carrying the
source intervals.  Changing the antecedent leaves every owner path and its
complementary upper witness unchanged. \(\square\)

In particular the gap-section occurrence SDR cannot be substituted for
the source theorem: it supplies the `K_S`, not the `I_S`.

## 5. Minimal obstruction certificates

After the owner negatives have been absorbed into `P`, define

\[
                         R_x=\bigcup_{S:x\notin S}I_S.        \tag{5.1}
\]

A failure is now exactly one of the following.

* **Owner kill:** for some `i` with `x in T_i`,
  \[
  O_i\cap\{p:x\in P_p\}\subseteq R_x.                       \tag{5.2}
  \]
* **Target kill:** for some `S` with `x in S`,
  \[
  I_S\cap\{p:x\in P_p\}\subseteq R_x.                      \tag{5.3}
  \]

There are no other obstructions.

Because all physical sets in (5.1)--(5.3) are cyclic intervals or unions
of interval components, these failures have a canonical finite witness.

### Proposition 5.1 (negative-percolation chain)

Choose a cut outside one connected component `J` of the left side of
(5.2) or (5.3), and regard `J` as an ordinary discrete interval.  If `J`
is covered by negative target intervals, then it has an inclusion-minimal
cover

\[
                         H_1,\ldots,H_q                       \tag{5.4}
\]

such that, after deleting portions outside `J`,

1. the left endpoints are strictly increasing;
2. the right endpoints are strictly increasing;
3. consecutive intervals overlap or touch;
4. `H_1` contains the left endpoint of `J`; and
5. `H_q` contains the right endpoint of `J`.

Conversely every chain (5.4) certifies the cover of `J`.

#### Proof

Take an inclusion-minimal subcover and discard every member contained in
another.  Sort by left endpoint.  The right endpoints must then increase,
and absence of an overlap/touch between consecutive members would leave a
point uncovered.  Minimality forces the first and last endpoint
conditions.  The converse is immediate by induction along the chain.
\(\square\)

Thus the exact minimal global obstruction is a negative interval chain
which percolates across every owner-compatible part of one required
positive interval.  Its length can grow with `d`; pairwise conflicts or a
bounded-order local test cannot detect all such failures.

## 6. Run endpoints are automatic safe ports

Unwrap one nonconstant positive owner run of coordinate `x` as

\[
                         [a,b],\qquad b-a+1\ge d+1.           \tag{6.1}
\]

### Lemma 6.1 (eroded run and mandatory endpoints)

The maximal-envelope support contributed by this run is

\[
                         B_x=[a+d,b].                         \tag{6.2}
\]

Its two endpoints `a+d` and `b` belong to the mandatory core of their
respective source positions.  They coincide exactly when the owner run has
minimum length `d+1`.

#### Proof

A source position `p` carries `x` in the maximal envelope precisely when
all owners `T_(p-d),...,T_p` lie in the run, which is (6.2).  The left
endpoint is the delayed insertion occurrence `I_(a-1)` at source position
`a+d`; the right endpoint is the deletion occurrence `D_b` at source
position `b`. \(\square\)

### Corollary 6.2 (interior-only danger)

In every feasible interval table, no target interval whose value omits
`x` may contain either endpoint in Lemma 6.1.  Consequently every
`x`-positive interval containing one of those endpoints automatically
passes its target cut.  Negative percolation can kill only positive
intervals which rely entirely on nonmandatory interior positions of the
eroded runs.

This identifies the exact benefit and the exact limit of the mandatory
core.  It supplies protected ports, but only two per positive owner run.

## 7. A linear interior-payload burden

For a source interval `I`, put

\[
                         F(I)=\bigcup_{p\in I}F_p.            \tag{7.1}
\]

On a simple Johnson trace, `|F_p|<=2`, and hence

\[
                         |F(I)|\le2|I|.                       \tag{7.2}
\]

### Proposition 7.1

If `I_S` represents a target of rank `s`, then at least

\[
                         \boxed{s-2|I_S|}                    \tag{7.3}
\]

of its coordinates, when this number is positive, must be witnessed at
nonmandatory source positions.  In particular every width-at-most-`d`
occurrence of a rank-`s` target has at least `s-2d` such payload
coordinates.

#### Proof

Only coordinates in `F(I_S)` have a mandatory endpoint inside `I_S`.
Equation (7.2) bounds their number.  Every remaining member of `S` must be
supplied at a position where that coordinate is optional, and hence is
subject to the negative-cover cut. \(\square\)

For the deep PBBS rows near `t=r-d`, this is a linear number of coordinates
per target.  Therefore a construction using only mandatory endpoints, a
bounded portal bank, or the native low-rank hook cores cannot make the
mixed rotor compatible.  A positive theorem must coordinate optional
interior witnesses on a linear-density family of target occurrences.

## 8. The natural local placement is impossible for every deep fan cell

For a selected PBBS owner occurrence

\[
 S(i,q)=\bigcap_{h=0}^{q}T_{i+h},\qquad q>d,                 \tag{8.1}
\]

the deep forced-pair separation theorem gives

\[
 F_p\not\subseteq S(i,q)
               \qquad(p\in[i,i+q+d]).                       \tag{8.2}
\]

### Corollary 8.1 (mandatory remote derangement)

No source interval meeting `[i,i+q+d]` can represent the selected deep
target (8.1).  Thus every deep member of the gap-section occurrence SDR
must be assigned to a remote source interval before the cover-free cuts
are even considered.

This is an atomic aperture failure, not a shortage of owner witnesses.
The whole-fan path remains valid read-only; only its literal source address
must be deranged globally.

## 9. Exact surviving lemma

The audited mixed-length rotor supplies a rational stationary circulation
with the correct rank marginals.  It does **not** choose one interval for
each named target on this fixed PBBS timeline, and averaging the cuts in
Theorem 2.1 is insufficient: a union of negative intervals is nonlinear in
the one-dimensional rank histogram.

The remaining statement can now be isolated without owner language.

> **PBBS-relative cover-free mixed-clock lemma.**  On the fixed resident
> PBBS chronology, choose pairwise distinct cyclic intervals `I_S` of
> length at most `d`, one for every required strict-lower target (up to a
> bounded terminal sidecar), with the mixed-length counts of the optimal
> Ferrers ledger, such that for every coordinate `x`:
>
> 1. every `x`-positive owner window and target interval contains a point
>    of the maximal-envelope support of `x` outside all `x`-negative target
>    intervals; and
> 2. equivalently, no owner-kill or target-kill negative-percolation chain
>    from Section 5 exists.

Under this lemma, (2.3) is an ordinary nonempty antecedent of the PBBS row,
the fixed whole-fan section supplies all read-only lower/upper owner
witnesses, and no extra common cap is needed for this interface.

The theorem proved here neither establishes nor refutes that lemma.  It
does prove that the stationary mixed rotor is not by itself a compatibility
proof, that the natural local gap-section placement is impossible, and that
the only remaining compatibility failures are the explicit cover chains
(5.4).  Thus the next positive construction must be a global cyclic
one-copy interval assignment with coordinated interior witnesses, not a
return to separated blocks or a marginal Hall calculation.

## 10. Exact endpoint-chain projection of a linear PBBS atlas

The cover-free lemma contains an already difficult static chain theorem.
This remains true after the `d` extra linear endpoints are retained rather
than discarded.

Open the cyclic PBBS owner row linearly and write its source positions as

\[
                         1,2,\ldots,W+d.                     \tag{10.1}
\]

The `W` interior owner windows are

\[
                         T_i=\bigcup_{p=i}^{i+d}A_p,
                         \qquad1\le i\le W.                  \tag{10.2}
\]

Assume every strict-lower target has been assigned a distinct source
interval of length at most `d`, as in a successful cover-free atlas.  Group
targets by the right endpoint of their assigned interval.

### Theorem 10.1 (linear anchored endpoint-chain projection)

Every such atlas gives a partition of the strict lower ideal into

1. `W` chains `C_(d+i)`, `1<=i<=W`, each of size at most `d` and every
   member contained in the distinct owner `T_i`; and
2. `d` boundary chains `C_1,...,C_d` of respective capacities
   `1,2,...,d`.

The total capacity is exactly

\[
                         dW+{d+1\choose2}.                   \tag{10.3}
\]

#### Proof

At one fixed right endpoint `j`, the intervals ending at `j` are nested as
their left endpoint moves left.  Their union values therefore form one
inclusion chain.  At most `min(d,j)` allowed intervals end at `j`.

For `j=d+i`, every allowed interval ending at `j` is contained in the
owner window `[i,i+d]`, so every target value in that endpoint chain is a
subset of `T_i`.  The owners are distinct on the one-copy PBBS row.  The
first `d` endpoints have capacities `1,...,d` and need no middle anchor.
Summing the capacities proves (10.3). \(\square\)

Put

\[
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},
 \qquad
 e=dW+{d+1\choose2}-\Lambda.                                \tag{10.4}
\]

The endpoint partition has exactly `e` unused slots.  Minimality of `d`
gives

\[
                         0\le e<W+d.                         \tag{10.5}
\]

Thus its mean vacancy is less than one per endpoint chain.  The extra `d`
endpoints contribute only the triangular `O(d^2)` boundary bank; they do
not absorb a positive-density chain imbalance.

### Corollary 10.2 (the relative theorem is not merely a word-order gate)

The PBBS-relative cover-free mixed-clock lemma implies the exact linear
static chain-anchor problem with capacity vector

\[
 \underbrace{d,\ldots,d}_{W\text{ anchored chains}},
                         d,d-1,\ldots,1.                     \tag{10.6}
\]

Consequently the relative lemma is at least as strong as that unresolved
static problem.  The exact ideal containment SDR is weaker: it assigns
targets to labelled owner slots but does not make the targets assigned to
one owner comparable.

This is the precise comparison with the equitable-chain frontier.
Furedi's conjecture concerns a minimum-chain, nearly equal partition of the
entire Boolean lattice.  The present problem is one-sided, has `d` extra
boundary chains, and labels the other chains by distinct middle owners, so
no formal equivalence is asserted.  Nevertheless (10.5) shows the same
unit-scale balancing phenomenon.  The published Tomon equal-`c` theorem
does not reach the critical coefficient `c=d`, while the
Sudakov--Tomon--Wagner construction leaves `o(Lambda)` rather than `O(1)`
targets.  Neither supplies (10.6).

## 11. What the whole-fan towers do and do not splice

For a selected PBBS root `X`, write

\[
                         L_q(X)=\bigcap_{h=0}^{q}g^hX.        \tag{11.1}
\]

Whenever the displayed values have the correct successive ranks, they
form one decreasing inclusion chain.  The whole-fan theorem proves that,
at every rank, every named target has at least one occurrence `(X,q)`.
This gives a natural abstract chainization graph: join a target to every
root tower in which it occurs.

### Proposition 11.1 (exact fan-capacity gate)

A selection of one whole-fan occurrence for every target, with at most `d`
targets assigned to each root, exists if and only if

\[
                         |Y|\le d|N(Y)|
                         \qquad(Y\subseteq\mathcal L)        \tag{11.2}
\]

after any targets allocated to the boundary staircase have been removed.
Here `N(Y)` is the set of root towers containing at least one target of
`Y`.

Under (11.2), the targets assigned to one root automatically form an
inclusion chain and are contained in that root owner.

#### Proof

Replace every root by `d` identical capacity slots and apply Hall's
theorem.  Two correct occurrences at different depths of one root tower
are nested by (11.1), and every one is contained in `X`. \(\square\)

The fixed-section support theorem proves only that every singleton target
family `{S}` has a nonempty neighbourhood.  It does not prove the all-set
cut (11.2).  Thus even the abstract endpoint-chain tableau does not follow
formally from whole-fan support.

There is also no canonical physical cross-SCD splice hidden at a common
target.  If two root towers meet at the same value `S`, their abstract
prefix and suffix chains can be concatenated at `S`.  But their local
owner occurrence does not produce a source occurrence: Corollary 8.1
forbids every local placement when the depth exceeds `d`.  After a remote
source placement is chosen, Theorem 2.1 still requires all coordinate
cover-free cuts.

The laminar-star obstruction gives a sharp logical counterexample to the
missing inference.  Its targets are individually aperture-feasible and
admit compatible abstract inclusion-chain/owner assignments, while one
parent-positive coordinate is erased because its negative child intervals
cover the parent interval.  Hence neither an SCD splice nor the stronger
whole-fan occurrence label determines a physical splice without the
negative-percolation test.

The shortest positive route through the whole-fan towers would therefore
need **both**:

1. the fan-capacity Hall inequalities (11.2), with the exact triangular
   boundary allocation; and
2. an ordering/remote-placement theorem putting those chains on the linear
   PBBS endpoints while avoiding every cover chain from Section 5.

The second condition is strictly stronger and is exactly the relative
mixed-clock lemma of Section 9.

## 12. Dependencies and scope

Used as inputs:

* the fixed PBBS whole-fan read-only theorem;
* the maximal-antecedent and forced-letter identities;
* the deep forced-pair separation theorem; and
* the audited mixed-length stationary rotor.

No finite computation, search, random rounding assertion, or SSH is used.
This note does not prove the cover-free mixed-clock lemma,
`nu(k)<=B(k)+O(1)`, or exact equality.
