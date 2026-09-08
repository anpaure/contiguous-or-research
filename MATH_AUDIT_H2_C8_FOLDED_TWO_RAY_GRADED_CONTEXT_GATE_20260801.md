# Folded C8 two-ray hosts close support, not the graded source language

Date: 2026-08-01  
Lane: H2, independent folded-octagon source audit  
Status: exact correction and scope theorem for the canonical aligned folded
Hamilton pair.  The one-/two-host ray formulas are valid.  Their advertised
set-support closure does not imply full graded or contextual equality.

## 0. Verdict

Let `S_0,S_1` be the aligned maximal erosions of the canonical folded C8
Hamilton paths, and let `G_0,G_1` be the two-host ray words

\[
 G_\epsilon=
 (X_L,L_\epsilon,f_2,\ldots,f_{d-1},R_\epsilon,X_R).   \tag{0.1}
\]

The exact ray formulas and common unions are correct:

\[
 X_L=L_0\cup L_1,qquad X_R=R_0\cup R_1,qquad
 L_0\cup R_0=L_1\cup R_1.                              \tag{0.2}
\]

Consequently every old interval of the contracted host word lifts, the only
new set values are the two directed rays, and

\[
       \operatorname{Deck}(S_0)\cup\operatorname{Deck}(G_1)
       =
       \operatorname{Deck}(S_1)\cup\operatorname{Deck}(G_0). \tag{0.3}
\]

Here `Deck` is ungraded set support.  The graded counters are not equal.  In
the canonical aligned fold their exact `L1` distances are

\[
\begin{aligned}
 \|D(S_0)-D(S_1)\|_1&=10d+12,\\
 \|D(G_0)-D(G_1)\|_1&=4d-4,\\
 \|D(S_0)+D(G_1)-D(S_1)-D(G_0)\|_1&=6d+16.             \tag{0.4}
\end{aligned}
\]

The final residue has one positive and one negative unit entry at every
width

\[
                         2d+5,\ldots,5d+12,             \tag{0.5}
\]

`3d+8` entries on each side.  Thus the two hosts cancel the exclusive ray
supports but not the multiplicity/address history of shared OR values.

An earlier folded-audit summary attached `6d+4` to the first line of (0.4);
that was a ledger-label bug.  The regenerated audit now distinguishes the
global minimum-signature cut (`6d+4`) from the common-anchor aligned-base
cut used here (`10d+12`), in agreement with the literal per-depth rows
`32,42,52,...`.

## 1. Local two-ray algebra is GO

Suppress a common core and put

\[
\begin{array}{ll}
L_0=za_3f_1,&L_1=za_1f_1,\\
R_0=za_1f_d,&R_1=za_3f_d.
\end{array}                                               \tag{1.1}
\]

In (0.1), intervals beginning at `L_epsilon` and ending successively at
`f_j` give

\[
             za_{3-2\epsilon}+F[1,j],\quad1\le j<d,     \tag{1.2}
\]

and intervals beginning successively at `f_j` and ending at `R_epsilon`
give

\[
             za_{1+2\epsilon}+F[j,d],\quad2\le j\le d. \tag{1.3}
\]

Both refinements in (0.1) have their old host as block union.  Intervals
trimming both blocks see (0.2), hence are phase common.  This proves the
two-host support theorem and its literal diagonal ray matching.

The alternative one-host word with adjacent halves

\[
 f_{d-1},\ldots,f_1,Z^\epsilon,T^\epsilon,
 f_d,\ldots,f_2                                         \tag{1.4}
\]

is also exact at the OR-support level and has cost one after contracting
`Z,T` to `X=za_1a_3`.  Its previously proved flat obstruction remains:
splitting one internal depth-`d` source letter creates `d` deficient natural
owner windows.  It is a nonflat deadline-`+1` interface, not a flat lift.

## 2. Why common exterior screens do not finish the graded row

Place the opposite ray word next to each folded source, in either order:

\[
                     S_0G_1\quad\hbox{versus}\quad S_1G_0. \tag{2.1}
\]

Their cross-seam counters agree, so the graded distance remains the third
line of (0.4).  The unique minimum active boundary screen of the aligned
fold is

\[
                         H=\{a_1,a_3\}.                  \tag{2.2}
\]

Using `za1a3` instead gives the same result.  Surrounding (2.1) by either
common screen makes the pointwise prefix and suffix chains equal, but does
not alter (0.4).  Hence arbitrary exterior context adds equal crossing
intervals while the internal graded residue survives.

Therefore:

\[
 \boxed{\text{two-ray support closure + common boundary screens}
        \not\Rightarrow\text{ graded/context equality}.}     \tag{2.3}
\]

This does not rule out a different fold/cut, a phase-sensitive collar whose
crossing cells pay (0.5), or a quotient overlap which identifies those
addresses.  It does rule out promoting the present two-host set theorem to
full graded transparency without another argument.

## 3. Replay

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_h2_c8_folded_two_ray_graded_context_gate_20260801.py --write
```

The replay independently reconstructs the aligned folded paths for
`2<=d<=12`, checks (1.1)--(1.3), (0.3)--(0.5), both block orders, and the
two common screens in Section 2.
