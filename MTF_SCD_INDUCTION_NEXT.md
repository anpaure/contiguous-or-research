# Move-to-front SCD induction: certified small tours, an exact parity lift,
# and a radius-monotone obstruction

## 1. Verdict

The move-to-front implication in the supplied text is correct, but it is not
new relative to the current ledger.  It is Theorem 1 of
`GLOBAL_MTF_SCD_HANDOFF.md`: an MTF--SCD tour gives

\[
        \nu(k)\le W(k)+k-1.
\]

The displayed five-dimensional tour is a valid new finite certificate.  It
does **not** provide the missing induction.  In fact it is a path, not a
cycle, and its induced OR word has length 14 whereas the optimum is 12.

This note adds two general results.

1. An exact one-coordinate lift takes arbitrary genuine MTF state paths to
   two lifted path families.  If the source is a closed state walk, its two
   copies splice into one path.  Closing ordinary paths by the exact reset
   lemma gives a parity-propagation theorem for near-width path covers.
2. Any direct-transversal path-cover induction whose chain radius changes by
   one in one globally fixed orientation at every assigned-chain step has
   reset excess `Omega(W)`, even if all pairwise MTF transitions and all
   collision choices are granted for free.  Repeatedly deleting the last
   star pair in that orientation therefore cannot prove constant one.  This
   does not exclude covers mixing orientations, using same-radius arcs, or
   making reset states serve as assigned-chain states.

The small-tour certificate and checker are in
`mtf_scd_small_verify.cpp`.  No `k=6` state/chains/update certificate was
present anywhere in the workspace; the prose assertion that one was found
is therefore not promoted to the theorem ledger.

## 2. Exact audit of the small tours

### 2.1 A cyclic tour for `k=3`

The states

\[
 (1,2,4),\qquad (4,1,2),\qquad (2,4,1)
\]

are related cyclically by the updates `4,2,1`.  They expose the SCD

\[
 (0,1,3,7),\qquad (4,5),\qquad (2,6).
\]

This is a genuine directed MTF--SCD cycle.

### 2.2 A path tour for `k=4`

An exact search followed by independent checking gives the six states

\[
\begin{array}{c|c}
\Pi_i&C_i\\ \hline
(1,2,4,8)&(0,1,3,7,15)\\
(8,1,2,4)&(8,9,11)\\
(4,8,1,2)&(4,12,13)\\
(2,4,8,1)&(2,6,14)\\
(8,2,4,1)&(10)\\
(5,8,2)&(5).
\end{array}
\]

The update masks are

\[
                     8,4,2,8,5.
\]

The six displayed chains are saturated, symmetric, disjoint, and partition
the 4-cube.  This is a genuine MTF--SCD path.

### 2.3 The supplied `k=5` certificate

The ten states, chains, and updates in the supplied text pass all of the
following checks.

* Every state is an ordered partition of the five coordinates.
* Every listed nonempty chain member is a prefix union of its state.
* The ten chains are saturated and symmetric, are pairwise disjoint, and
  partition all 32 subsets.
* Applying the nine updates
  \[
                 8,16,1,2,8,18,20,5,9
  \]
  gives exactly the next listed state.
* Reversely initializing the first state gives the length-14 word
  \[
  8,16,1,2,4,8,16,1,2,8,18,20,5,9,
  \]
  whose contiguous ORs cover all 31 nonzero masks.

The first five chains are one cyclic-interval block.  The last five are the
radius-one chains of a second cyclic order; the first state of this second
block retains a split minimum in order to make the seam.  Thus this example
is finite evidence for the already-recorded cyclic-interval/wreath program,
not an independent general mechanism.

The path does not close in one move.  Its final state is

\[
                         (9,4,16,2),
\]

whereas the first chain, having empty minimum and full top, has the unique
exposing state

\[
                         (4,2,1,16,8).
\]

Any update producing the latter state would have to use `X={4}`.  But after
that update the old first block `9={1,8}` remains tied and is the second
block, so the result cannot be the required singleton state.  Therefore the
displayed path is not a directed cycle and cannot simply be doubled
recursively.

### 2.4 Artifact status

The workspace previously contained no explicit small MTF--SCD tour
certificate.  The checker now certifies `k=3,4,5`.  It does not certify
`k=6`; the statement that a six-dimensional tour was found came without its
states, chains, or update masks.  A bounded exact search did not produce one,
but that is neither an impossibility result nor evidence against existence.

## 3. Exact state lifts by one coordinate

Let

\[
                     \Pi=(B_1,\ldots,B_s)
\]

be an ordered partition of `[k]`, and let `z` be a new coordinate.  Define

\[
\begin{aligned}
 L_z(\Pi)&=(B_1,\ldots,B_s,\{z\}),\\
 U_z(\Pi)&=(B_1\cup\{z\},B_2,\ldots,B_s),\\
 V_z(\Pi)&=(\{z\},B_1,\ldots,B_s).
\end{aligned}                                                    \tag{3.1}
\]

Here the notation means that `z` is adjoined to the indicated block; it is
not an integer sum.

### Lemma 1 (lift identities)

For every nonempty `X subseteq [k]`,

\[
\boxed{
 L_z(M_X\Pi)=M_X(L_z\Pi),\qquad
 U_z(M_X\Pi)=M_{X\cup\{z\}}(U_z\Pi).
}                                                               \tag{3.2}
\]

Moreover:

* the old prefix unions of `Pi` occur unchanged in `L_z(Pi)`;
* the nonempty prefix unions of `U_z(Pi)` are `z` union the nonempty
  prefix unions of `Pi`;
* the prefix unions of `V_z(Pi)` are `{z}` and `z` union every nonempty
  prefix union of `Pi`.

#### Proof

The update `X` is disjoint from `z`, so appending the last block `{z}`
commutes with deleting `X` from all old blocks.  This proves the first
identity.  In the second identity the update `X union {z}` removes `z` from
the old first block and removes `X` from every old block, leaving

\[
  (X\cup\{z\}, B_1\setminus X,\ldots,B_s\setminus X),
\]

which is exactly `U_z(M_X Pi)`.  The prefix statements follow directly from
(3.1).  QED.

### Corollary 2 (two-copy lift of a path cover)

Suppose `L` states in `p` genuine MTF paths cover all but `q` nonempty masks
of the `k`-cube.  Let the first states of the paths have `s_1,...,s_p`
blocks.  Then the two lifted families `L_z` and `U_z` give `2L` states in
`2p` genuine paths on `k+1` coordinates.  They miss exactly the two copies
of the old missing masks and, possibly, the singleton `{z}`.  Consequently

\[
 \nu(k+1)
 \le 2L-p+2\sum_{j=1}^p s_j+2q+1.                \tag{3.3}
\]

The term `1` may be deleted if `{z}` is already exposed by some additional
state.  Formula (3.3) is mainly a structural statement; the ordinary trimmed
OR lift can give a shorter numerical bound while forgetting the path-cover
structure.

## 4. Closed-walk splicing

The preceding two copies can be joined without a reset when the source walk
is closed.

### Theorem 3 (closed-walk parity lift)

Let

\[
 \Pi_0\longrightarrow\Pi_1\longrightarrow\cdots
 \longrightarrow\Pi_{\ell-1}\longrightarrow\Pi_0              \tag{4.1}
\]

be a directed closed MTF walk.  Suppose the closing update is `X_0`, so
`Pi_0=M_(X_0)(Pi_(ell-1))`.  Then

\[
\begin{aligned}
 &L_z(\Pi_0),L_z(\Pi_1),\ldots,L_z(\Pi_{\ell-1}),\\
 &V_z(\Pi_{\ell-1}),U_z(\Pi_0),U_z(\Pi_1),\ldots,
 U_z(\Pi_{\ell-2})                                      \tag{4.2}
\end{aligned}
\]

is one directed MTF path of `2 ell` states.

For `ell=1`, interpret (4.2) simply as
`L_z(Pi_0),V_z(Pi_0)`; the assertion is immediate.  The displayed closing
seam below is needed only when `ell>=2`.

If the union of the prefix chains along (4.1) misses `q` nonempty old masks,
then (4.2) misses exactly the lower and upper copies of those masks, hence
`2q` masks in total.  In particular `{z}` is not missed.

#### Proof

The lower transitions and ordinary upper transitions follow from Lemma 1.
The seam transitions are

\[
 L_z(\Pi_{\ell-1})\xrightarrow{\{z\}}V_z(\Pi_{\ell-1})
 \xrightarrow{X_0\cup\{z\}}U_z(\Pi_0).
\]

The first equality is immediate.  For the second,

\[
 M_{X_0\cup\{z\}}(V_z(\Pi_{\ell-1}))
   =(X_0\cup\{z\},\Pi_{\ell-1}-X_0)
   =U_z(\Pi_0).
\]

The lower half exposes every old covered mask.  The state `V_z` exposes
`{z}` and the upper copy of every mask exposed at the cut state; the other
`U_z` states expose the upper copies at every other state.  This proves the
coverage statement.  QED.

For `p` closed walks of total cyclic length `L`, cut-state block counts
`s_j`, and total defect `q`, the usual initialization argument applied to
(4.2) gives

\[
                  \boxed{\nu(k+1)\le 2L+\sum_j s_j+2q.}         \tag{4.3}
\]

### Corollary 4 (closing ordinary paths first)

An ordinary path whose first state has `s` blocks can be closed by the exact
ordered-partition reset in `s` updates.  Since the final update returns to
the already counted first state, the resulting cyclic list has only `s-1`
new states.  Hence `p` paths of total state count `L`, first-state block sum

\[
                         R=\sum_j s_j,
\]

and mask defect `q` lift to `p` paths in the next dimension having

\[
                    2(L+R-p)                                    \tag{4.4}
\]

states, first-state block sum `R+p`, and defect at most `2q`.  Reset states
may incidentally cover masks that the original assigned states missed.

Therefore the property

\[
 L=W(k)+o(W(k)),\qquad R=o(W(k)),\qquad q=o(W(k))                \tag{4.5}
\]

propagates from dimension `k` to dimension `k+1`.  Indeed,

\[
 W(2m+1)=2W(2m)-\operatorname{Cat}_m,
 \qquad W(2m+2)=2W(2m+1),                                      \tag{4.6}
\]

and `Cat_m=o(W(2m))`; also `p<=R`, so the new reset mass remains lower
order.

This is a real induction lemma, but not a base construction.  Iterating from
one fixed small dimension accumulates a nonvanishing relative error.  What
it does show is that any near-width, low-reset path-cover theorem proved on
one parity automatically transfers to the other parity without losing the
leading constant.

## 5. Why a radius-only induction cannot close the problem

Now take `k=2m`.  An SCD chain of radius `d` has ranks

\[
                       m-d,m-d+1,\ldots,m+d.
\]

The forced number of radius-`d` chains is

\[
 c_d=\binom{2m}{m-d}-\binom{2m}{m-d-1},
 \qquad 0\le d\le m.                                           \tag{5.1}
\]

Any state exposing such a chain has at least `2d+2` blocks when `d<m`:
one block for the nonempty minimum, `2d` singleton increment blocks, and
one block for the nonempty complement of the top.  The endpoint `d=m` has
only one chain and does not affect the asymptotics.

### Theorem 5 (radius-decreasing reset barrier)

Consider any **direct transversal** state-path cover of an SCD: every path
state is the chosen exposing state of one SCD chain, there are no auxiliary
states between assigned chains, and every arc goes from radius `d` to radius
`d-1`.  Grant, optimistically, that every desired pairwise MTF arc exists and
composes.  The reset excess in the exact path-cover bound still satisfies

\[
 \sum_{\text{components }j}(s_j-1)
 \ge
 \sum_{d=0}^m (2d+1)(c_d-c_{d+1})_+-2,
 \qquad c_{m+1}=0.                                             \tag{5.2}
\]

Moreover,

\[
 \boxed{
 \sum_{d=0}^m (2d+1)(c_d-c_{d+1})_+-2
      =\left(\frac4{\sqrt e}+o(1)\right)W(2m).
 }                                                               \tag{5.3}
\]

Thus even an ideal radius-decreasing path cover gives, through the reset
ledger, no better than

\[
 \left(1+\frac4{\sqrt e}+o(1)\right)W(2m),                     \tag{5.4}
\]

far from constant one.

#### Proof

At radius `d`, at most `c_(d+1)` paths can enter from the preceding radius.
Therefore at least `(c_d-c_(d+1))_+` components start at radius `d`.  Each
such first state has reset excess at least `2d+1`, except for the unique
radius-`m` full chain, whose minimum and top complement are empty and whose
reset excess is `2m-1`.  Subtracting two proves (5.2).

The sequence `c_d` is unimodal.  Indeed

\[
 \frac{c_{d+1}}{c_d}
 =\frac{(2d+3)(m-d)}{(2d+1)(m+d+2)},                            \tag{5.5}
\]

so its maximum occurs at

\[
                         d_*=(1/\sqrt2+o(1))\sqrt m.
\]

Uniformly for `d=x sqrt(m)` in bounded `x`-ranges, the central local limit
estimate gives

\[
 c_d=\frac{W(2m)}{\sqrt m}
          \left(2x e^{-x^2}+o(1)\right).                       \tag{5.6}
\]

Since the positive differences in (5.2) begin at the peak, summation by
parts gives

\[
 \sum_{d\ge d_*}(2d+1)(c_d-c_{d+1})
 =(2d_*+1)c_{d_*}+2\sum_{d>d_*}c_d.                            \tag{5.7}
\]

The first term tends to `(2/sqrt(e))W`.  The second tends to

\[
 2W\int_{1/\sqrt2}^{\infty}2x e^{-x^2}\,dx
   =\frac2{\sqrt e}W.
\]

This proves (5.3).  QED.

Even reversing the hypothetical monotone direction does not give constant
one.  The identical calculation for starts
`(c_d-c_(d-1))_+` yields reset excess

\[
                     \left(\frac4{\sqrt e}-2+o(1)\right)W,
                                                                    \tag{5.8}
\]

which is still a positive fraction (`about 0.426 W`).

Theorem 5 is stronger than the known statement that the particular
Greene--Kleitman last-pair map has about `W/2` starts.  It says that **no
direct transversal with one globally fixed monotone radius orientation** can
make the reset cost lower order.  A successful path-cover proof must use
same-radius motion, mixed orientations, reset/assigned-state sharing, or an
equally global substitute.

## 6. What is genuinely new, and what remains open

### Existing ledger, merely reconfirmed

* MTF--SCD tour `implies nu(k)<=W(k)+k-1`.
* The exact state fiber and quotient-chain one-step criterion.
* The ordered-partition reset/path-cover bound.
* The last-pair map is many-to-one and by itself leaves `Theta(W)` starts.
* Long same-radius rotor/long-run atoms are a valid conditional route.

### New in this note

* Machine-checkable `k=3,4,5` tour certificates; the displayed `k=5` tour is
  independently validated and identified as two cyclic-interval blocks.
* The exact lower/upper state-lift identities (3.2).
* The closed-walk parity splice (4.2) and the low-reset propagation theorem
  (4.4)--(4.6).
* The globally oriented direct-transversal radius barrier (5.2), including
  its asymptotic constants (5.3) and (5.8).

### Still open

The parity lift does not manufacture the required low-reset path cover.  The
remaining sufficient target is still:

> Construct, in one parity and arbitrarily large dimensions, genuine MTF
> state paths whose total visited-state count is `W+o(W)`, whose first-state
> block sum is `o(W)`, and whose uncovered-mask count is `o(W)`.

Theorem 5 sharpens this target: the paths cannot be built only by repeatedly
shortening SCD chains.  They need long same-radius motion (or an equally
global substitute), precisely the missing integrality step in the rotor and
long-run-atom formulations.
