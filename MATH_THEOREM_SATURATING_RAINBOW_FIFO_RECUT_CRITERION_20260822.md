# Saturating rainbow paths: exact FIFO recut criterion and depth ledger

**Status (2026-08-22).**  Every deterministic statement below is proved.
The result gives an exact polynomial-time test for whether the existing
rainbow Johnson path can be recut into the required number of cyclic FIFO
rows.  Passing the test would give `o(W)` damage at the four central ranks.
The published saturating-cycle input does not imply the test, and the
generic deeper-rank seam bound is too large at Gaussian depth.

## 1. Exact completion of one Johnson arc

Put

\[
 n=2m+1,
 \]

and let

\[
 X_0,X_1,\ldots,X_L\in{[n]\choose m},\qquad L<n,
\]

be a simple Johnson arc.  Orient its transitions by

\[
 X_{i+1}=X_i-\{r_i\}+\{a_i\},
 \qquad 0\le i<L.                                  \tag{1.1}
\]

A cyclic FIFO row is a permutation
`C=(C_0,...,C_(n-1))`, read modulo `n`, whose rank-`m` trace is

\[
                         I_C(i,m)=\{C_i,\ldots,C_{i+m-1}\}. \tag{1.2}
\]

The transition from phase `i` removes `C_i` and adds `C_(i+m)`.
Accordingly, give transition `i` the two port assignments

\[
                         C_i=r_i,\qquad C_{i+m}=a_i. \tag{1.3}
\]

### Theorem 1.1 (exact FIFO-arc lemma)

The arc (1.1) is a contiguous trace of a cyclic FIFO row if and only if the
partial phase map in (1.3) is well-defined and injective; explicitly:

1. two ports assigned to the same phase carry the same label; and
2. ports assigned to distinct phases carry distinct labels.

When `L=m`, exactly one phase and one label remain unassigned.  When
`L>m`, every phase is assigned.  Hence every compatible arc with `L>=m`
has a unique completing row.  Reversing the arc creates no additional
eligibility.

#### Proof

Necessity follows immediately from (1.2).  Conversely, complete the
injective partial map (1.3) to a permutation `C`.  When `L<m`, fill the
unassigned phases among `0,...,m-1` with the unused labels of `X_0`; when
`L>=m`, those phases are already assigned.

We claim in either case that

\[
                         X_0=\{C_0,\ldots,C_{m-1}\}. \tag{1.4}
\]

For `i<m`, the removal `r_i=C_i` belongs to `X_i`.  If it had entered at
an earlier transition `j<i`, then the same label would occupy the distinct
phases `i` and `j+m`, contradicting port injectivity.  Thus every assigned
`C_i` with `i<m` already belongs to `X_0`.

If `L<m`, the removal phases `0,...,L-1` and the arrival phases
`m,...,m+L-1` are disjoint.  An arrival cannot be an as-yet-unremoved
member of `X_0`, because it is absent immediately before arrival, and it
cannot equal an earlier removal because those two ports would occupy
distinct phases.  Hence the unused labels of `X_0` fill precisely the
unassigned first-`m` phases, proving (1.4).  If `L>=m`, the `m` removals
`C_0,...,C_(m-1)` are distinct members of `X_0`; cardinality alone proves
(1.4).  Notice that for `L>m` an arrival may legitimately equal an earlier
removal when the two ports have the same cyclic phase, so no stronger claim
is being used.

Now (1.1), (1.3), and induction give

\[
 X_{i+1}=I_C(i,m)-C_i+C_{i+m}=I_C(i+1,m),
\]

so the completed row realizes the whole arc.  If `L=m`, the removal phases
`0,...,m-1` and arrival phases `m,...,2m-1` leave one phase; if `L>m`,
their union is all of `Z_n`.  This proves uniqueness.  Reversing a row arc
is the corresponding arc of the reversed cyclic order, so the same port
condition is necessary and sufficient.  \(\square\)

## 2. Exact recutting of the full rainbow path

Let

\[
 W={n\choose m},\qquad N={n\choose {m-1}},\qquad
 B={W\over n}=\operatorname{Cat}_m.                \tag{2.1}
\]

Take the saturating rainbow path

\[
                         P_*=(X_0,X_1,\ldots,X_N),  \tag{2.2}
\]

whose `N` Johnson edges have distinct rank-`(m-1)` intersection colours.
Form an interval of transition indices for every conflicting pair of ports:
if their transitions have indices `i<j`, include `[i,j]`.  Also include
every interval of `n` consecutive transitions.  Let
`tau_FIFO(P_*)` be the minimum number of transition indices meeting every
one of these intervals.

### Theorem 2.1 (interval-transversal criterion)

Deleting a set of path transitions leaves only FIFO-compatible components
if and only if the deleted set meets every interval just defined.
Consequently, the path can be recut into exactly `B` FIFO rows if and only if

\[
                         \boxed{\tau_{\rm FIFO}(P_*)\le B-1}. \tag{2.3}
\]

The number `tau_FIFO(P_*)` is computed exactly by sorting the intervals by
right endpoint and repeatedly selecting the first uncovered right endpoint.

#### Proof

Two conflicting ports cannot lie in one component, so some transition in
their index interval must be deleted.  A row arc from a simple path has at
most `n-1` transitions, because after `n` FIFO transitions its rank-`m`
state repeats.  This proves necessity of all the intervals.

Conversely, if every conflict interval is hit, no retained component has a
port conflict.  Hitting every length-`n` interval makes its length less than
`n`, so Theorem 1.1 completes it to a row.  Deleting `t` transitions gives
exactly `t+1` nonempty vertex components, including singleton components
between consecutive deleted transitions.  Extra cuts preserve compatibility, and
because `N` is much larger than `B`, they may be placed in nonempty
components until there are exactly `B`.  This proves (2.3).

For completeness, the greedy interval algorithm is optimal.  Let `[a,b]`
be the remaining interval with smallest right endpoint.  Every transversal
must choose a point `p in [a,b]`.  Replacing `p` by `b` cannot uncover an
interval whose right endpoint is at least `b`: if that interval contained
`p` and began after `b`, it would have `p>b`, impossible.  Thus some optimum
contains `b`; delete all intervals hit by `b` and iterate.  \(\square\)

There is a particularly simple necessary statistic.  Put

\[
 \Phi_m(P_*)=
 \bigl|\{0\le i<N-m:a_i\ne r_{i+m}\}\bigr|.        \tag{2.4}
\]

Each violation in (2.4) is a conflict at phase `i+m`, and hence contributes
the interval `[i,i+m]`.  One deleted transition belongs to at most `m+1`
such intervals.  Therefore

\[
 \boxed{
 \Phi_m(P_*)\le(m+1)(B-1)
 }                                                   \tag{2.5}
\]

is necessary for a `B`-row recut.  The saturating-cycle theorem alone gives
no estimate for either side of (2.3) or (2.5).

## 3. Four-rank payoff and exact deeper ledger

Assume (2.3), retain every path vertex, and complete its `B` components to
rows.  The exact number of new middle occurrences is

\[
 W-(N+1)={2W\over m+2}-1=O(W/m).                   \tag{3.1}
\]

Indeed `N/W=m/(m+2)`.  The original `N+1` owners are distinct, so additions
can create at most the number in (3.1) of middle holes.  Complementation
gives the same upper-middle bound.  Only the `B-1` cut path edges can remove
one of the rainbow intersection colours.  Hence

\[
 h_m,h_{m+1}\le {2W\over m+2}-1,
 \qquad
 h_{m-1},h_{m+2}\le B-1.                           \tag{3.2}
\]

All four quantities are `o(W)`.

Fix `1<=H<=m-1`.  For `1<=q<=H`, define

\[
 \mathcal P_q=
 \left\{\bigcap_{t=0}^{q}X_{i+t}:
 0\le i\le N-q,\ 
 \left|\bigcap_{t=0}^{q}X_{i+t}\right|=m-q\right\},
 \qquad
 h_q^P={n\choose m-q}-|\mathcal P_q|.             \tag{3.3}
\]

Thus `h_q^P` is the number of rank-`(m-q)` sets absent from the
consecutive path intersections of the expected rank.  Inside a FIFO row,
(3.3) is exactly a cyclic interval of length `m-q`.
One cut destroys at most `q` such occurrences.  Completion only adds row
windows.  Therefore every completed `B`-row bank obeys

\[
 \boxed{
 h_{m-q}^{\rm row}=h_{m+1+q}^{\rm row}
       \le h_q^P+q(B-1).
 }                                                   \tag{3.4}
\]

Summing gives

\[
 \sum_{q=1}^H
  (h_{m-q}^{\rm row}+h_{m+1+q}^{\rm row})
 \le2\sum_{q=1}^Hh_q^P+H(H+1)(B-1).                \tag{3.5}
\]

This seam term is harmless for `H=o(sqrt n)`, assuming the path shadows in
(3.3) are already good.  At the required
`H=Theta(sqrt(n log n))`, however, it is `Theta(W log n)`, not `o(W)`.

Finally, (3.1) is only `O(B)`.  Let `s` be the number of components with
fewer than `m` transitions.  Each such component requires at least `m`
added cyclic-row positions, so

\[
                              s=O(B/m).             \tag{3.6}
\]

All other rows have unique completions by Theorem 1.1.  Two arbitrary
choices for the short-row completions can differ over the `2H`-rank band
in at most

\[
                         O(snH)=O(BH)               \tag{3.7}
\]

occurrence records.  At `H=Theta(sqrt(n log n))`, this is `o(W)`, since
`BH/W=H/n=o(1)`.  Consequently completion freedom can change the aggregate
band ledger only by `o(W)`; any positive proof must already control the
fixed/unique part to `o(W)` (or introduce a new family of switches).  The
abstract rainbow-path theorem supplies no such control.

The finite `m=3` search in the accompanying checker is evidence only: among
1,998 generated saturating cycles, every tested opening needed at least six
FIFO blocks whereas `B=5`.  No finite sample is used in the proof above.
