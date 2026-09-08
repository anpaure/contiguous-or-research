# The symmetric `q+2` independent-rotation profile has an exponential top-rank deficit

**Date:** 2026-08-13  
**Status:** exact fractional profile theorem and analytic obstruction.  Distributed-core
decorations preserve the owner, immediate-lower, and immediate-upper packet currents
literally.  However, choosing the two-emission rotation independently and uniformly for
each core coordinate does not cover all lower ranks: the rank-`R-2` load is exponentially
small at triangular depth.  Correlated complete-ticket schedules are therefore
load-bearing.

## 1. Packet and random decoration

Put

\[
 k=2R-1,\qquad q=d+1,\qquad N=q+2,\qquad c=R-q.         \tag{1.1}
\]

In one upper-rich two-hole packet, let `F` be a `c`-set and let
`y_0,...,y_(N-1)` be distinct toggles disjoint from `F`.  For every `f in F`, choose
independently and uniformly an address `a in Z_N` and emit `f` on

\[
                         P_a=\{a,a+q-1\}=\{a,a-3\}.       \tag{1.2}
\]

At phase `i`, the source letter is the set of emitted core coordinates together with
`y_i`.

Every `P_a` meets every cyclic `(q-1)`-interval when `q>=4`.  Therefore, for **every**
choice of the rotations, not just on average, all source intervals of width at least
`q-1` have the same union as in the repeated-core packet.  In particular the complete
immediate-lower, owner, and immediate-upper rows are unchanged literally.

## 2. Exact hit probabilities

Fix a cyclic source interval `J` of width `ell<q`.  A uniform rotation `P_a` meets `J`
exactly when

\[
                         a\in J\cup(J+3).                  \tag{2.1}
\]

Hence its hit probability is

\[
 p_\ell=
 \begin{cases}
 {2\ell\over q+2},&1\le\ell\le3,\\[2mm]
 {\ell+3\over q+2},&3\le\ell\le q-2,\\[2mm]
 1,&\ell=q-1.
 \end{cases}                                               \tag{2.2}
\]

At the common endpoint `ell=3` the two formulas agree.  The first line follows because
the two `ell`-arcs are disjoint; in the second line their overlap has size `ell-3`.

The `c` core coordinates make independent choices.  Thus the number of core coordinates
in an `ell`-cell is exactly

\[
                         H_\ell\sim\operatorname{Bin}(c,p_\ell), \tag{2.3}
\]

and the cell rank is `ell+H_ell` because its toggle interval has `ell` distinct labels.

## 3. Symmetric target load

Average the decorated packets over the full ground-set orbit and normalize the packet
factor so every rank-`R` owner has load one.  Every packet has the same number of cells
at each width as owners.  Ground-set symmetry is transitive on every target rank.

### Theorem 3.1 (exact raw lower profile)

The aggregate raw load of every fixed rank-`s` target is

\[
 \boxed{
 \lambda_s={W\over\binom{k}{s}}
 \sum_{\ell=1}^{q-1}
 \Pr\bigl[\operatorname{Bin}(c,p_\ell)=s-\ell\bigr],
 \qquad W=\binom{k}{R}.}                                  \tag{3.1}
\]

The same decorated fractional family retains owner and immediate-lower load exactly one
and the original marked immediate-upper load exactly one.

#### Proof

Equation (2.3) gives the rank distribution of a uniformly rooted width-`ell` occurrence.
Owner normalization supplies exactly `W` physical occurrences at every width.  After
full symmetrization these are uniform within their rank, giving the corresponding term
of (3.1).  Summing the possible widths proves the formula.  The three high shores are
unchanged packetwise, as observed in Section 1. \(\square\)

## 4. Exact rank-`R-2` deficit

At `s=R-2`, only widths `ell=q-2,q-1` can possibly contribute.  At width `q-1`, the
core is deterministically complete, giving rank `R-1`, not `R-2`.  At width `q-2`, a
rank-`R-2` cell requires all `c` core coordinates and has probability

\[
                         p_{q-2}^{c}
 =\left(1-{1\over q+2}\right)^c.                         \tag{4.1}
\]

Also

\[
 {\binom{2R-1}{R}\over\binom{2R-1}{R-2}}
 ={R+1\over R-1}.                                        \tag{4.2}
\]

Therefore

\[
 \boxed{
 \lambda_{R-2}
 ={R+1\over R-1}
  \left(1-{1\over q+2}\right)^{R-q}.}                    \tag{4.3}
\]

At triangular depth `q=Theta(sqrt R)`,

\[
                         \lambda_{R-2}
 =\exp\{-\Theta(\sqrt R)\}.                              \tag{4.4}
\]

For every sufficiently large parameter it is strictly below one.  The optimal Ferrers
boundary has no rank-`R-2` deletion, so the residual demand at that rank is one.  The
independent-rotation family consequently fails even fractional lower coverage; thinning
cannot repair it.

## 5. Consequence

This obstruction is not a defect of the `q+2` packet or its three high shores.  It is a
correlation failure.  Near-top lower targets require almost every core coordinate to use
a rotation hitting the **same** marked interval.  Independent uniform rotations make
that event exponentially rare.

The complete nested-ticket portal resolves the local version by assigning rotations
coherently from a target chain's threshold word.  What remains is the global problem of
grouping those correlated endpoint tickets into schedule-compatible packets and rounding
the owner/root/upper/lower incidence system integrally.

## 6. Verification ledger

The formula was independently evaluated on `ssh h100` for all odd `k<=2001` in the
legal range and at larger dyadic samples through `k=8191`.  In every tested case the
minimum load occurred at rank `R-2`, with the exact value (4.3).  This finite observation
is not used in the proof.

* script: `scratch/audit_qplus2_distributed_profile_20260813.py`;
* frozen scan: `scratch/audit_qplus2_distributed_profile_scan_2001_20260813.out`.
