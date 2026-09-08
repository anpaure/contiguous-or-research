# The folded octagon's two residual rays have an exact two-host compiler closure

Date: 2026-08-01  
Lane: AD, quotient-fold terminal compiler  
Status: exact all-depth source-set, common-cap and physical-cell matching
theorem.  Actual occurrence of the two hosts and their owner/deadline/
residence admissibility are hypotheses supplied by the ambient fold.

## 0. Result

After the quotient fold, suppose the only phase-zero-exclusive source masks
are the two nested families

\[
\begin{aligned}
 \mathcal P_0&=\{K+za_3+F[1,j]:1\le j\le d-1\},\\
 \mathcal S_0&=\{K+za_1+F[j,d]:2\le j\le d\},
\end{aligned}                                             \tag{0.1}
\]

and phase one swaps `a1,a3`:

\[
\begin{aligned}
 \mathcal P_1&=\{K+za_1+F[1,j]:1\le j\le d-1\},\\
 \mathcal S_1&=\{K+za_3+F[j,d]:2\le j\le d\}.
\end{aligned}                                             \tag{0.2}
\]

Then two actual old letters suffice, with exact common caps and no cross-host
overshoot.  Put

\[
\begin{array}{ll}
 L_0=K+za_3+f_1,&L_1=K+za_1+f_1,\\
 R_0=K+za_1+f_d,&R_1=K+za_3+f_d,
\end{array}                                               \tag{0.3}
\]

and

\[
 X_L=L_0\cup L_1=K+za_1a_3+f_1,qquad
 X_R=R_0\cup R_1=K+za_1a_3+f_d.                         \tag{0.4}
\]

Starting from the core word

\[
                  X_L,f_2,f_3,\ldots,f_{d-1},X_R,       \tag{0.5}
\]

use in phase `epsilon` the two overlapping binary refinements

\[
 X_L\mapsto(X_L,L_\epsilon),\qquad
 X_R\mapsto(R_\epsilon,X_R).                            \tag{0.6}
\]

Every old interval has its injective full-block lift.  The new right-facing
cells at the left host are exactly `P_epsilon`; the new left-facing cells at
the right host are exactly `S_epsilon`.  All intervals trimming both hosts
are phase-common because

\[
                  L_0\cup R_0=L_1\cup R_1
                    =K+za_1a_3+\{f_1,f_d\}.             \tag{0.7}
\]

Therefore

\[
 \operatorname{Deck}(W^0)-\operatorname{Deck}(W^1)
     =\mathcal P_0\mathbin{\dot\cup}\mathcal S_0,
 \qquad
 \operatorname{Deck}(W^1)-\operatorname{Deck}(W^0)
     =\mathcal P_1\mathbin{\dot\cup}\mathcal S_1.      \tag{0.8}
\]

No unlisted phase-exclusive side cell is born.

## 1. Literal ray addresses

In the expanded phase word, start at the second member `L_epsilon` of the
left split.  Ending successively at `L_epsilon,f2,...,f_j` gives

\[
 L_\epsilon\cup F[2,j]
  =K+z+a_{3-2\epsilon}+F[1,j],                           \tag{1.1}
\]

where the notation means `a3` in phase zero and `a1` in phase one.  These
are the `d-1` distinct cells of `P_epsilon`.

Dually, start successively at `f_j,...,f_(d-1),R_epsilon`
and end at the first member `R_epsilon` of the right split.  Their values are

\[
 F[j,d-1]\cup R_\epsilon
  =K+z+a_{1+2\epsilon}+F[j,d],                           \tag{1.2}
\]

giving the `d-1` distinct cells of `S_epsilon`.  The two families are
disjoint because their active labels differ.  Thus the occurrence-labelled
target-to-cell graph contains a literal diagonal perfect matching of size
`2d-2`.

## 2. Full old-deck and cross-host closure

Both replacements in (0.6) have the old union as block union.  Simultaneous
block contraction therefore gives an injective equal-OR lift of every old
physical interval.

A genuinely new interval can trim only the left block, only the right block,
or both.  The first two cases are precisely (1.1)--(1.2), together with
outward cells using the full pieces `X_L,X_R`, whose values were already
present before refinement.  There is exactly one double-trimmed cell (both
hosts are at the ends of the displayed rail), and its value is

\[
        L_\epsilon\cup F[2,d-1]\cup R_\epsilon.          \tag{2.1}
\]

Equation (0.7) makes (2.1) independent of `epsilon`.  Hence the complete
two-host side-cell family is common, proving (0.8).

This is stronger than separately verifying the two rays: it closes the
cross-host overshoot gate exactly.

## 3. Common caps and Hall

The positionwise cap word is

\[
             X_L,X_L,f_2,\ldots,f_{d-1},X_R,X_R.         \tag{3.1}
\]

It contains both terminal phase words literally.  Full-block lifts and side
cells are disjoint physical cell classes.  Therefore any old matching carried
on full-block lifts combines with the diagonal ray matching from Section 1,
with no cell collision and no subset-Hall obstruction.  At the local source
level, common-cap/compiler matching is completely closed.

On a phase reversal, contract both marked blocks and re-expand them with
`L_(1-epsilon),R_(1-epsilon)`.  If the old ray tasks have become native or
have other retained cells in the quotient fold, the same two marked
boundaries reset rather than accumulate.  This last sentence is conditional
on simultaneous contraction-safe transport of the ambient protected bank;
the local identities alone do not prove that external matching.

## 4. Exact scope

The theorem proves:

* two source positions of additive refinement cost;
* every old OR interval by full-block lift;
* all `2d-2` prescribed ray occurrences in distinct cells;
* one literal pointwise common cap;
* no phase-exclusive cross-host cell; and
* exact local Hall.

It assumes that `X_L,X_R` are actual old source letters at the displayed
rail ends.  It does not infer their existence from set containment, nor does
it prove that inserting the two positions preserves a flat depth-`d` owner
row.  Owner, q1 and topology supplied by the quotient fold must be accompanied
by an explicit deadline/residence acceptance of (0.6), or by an equal-length
prepared-host realization.  Simultaneous contraction of the full protected
compiler bank is also separate.

## 5. Replay

Run

```text
python3 scratch/audit_ad_octagon_folded_two_ray_twohost_closure_20260801.py
```

The dependency-free replay checks `2<=d<=64`: full-block transport, exact
directed deck differences, all ray addresses, their diagonal matching,
the pointwise cap word, and phase-independence of every double-trimmed cell.
