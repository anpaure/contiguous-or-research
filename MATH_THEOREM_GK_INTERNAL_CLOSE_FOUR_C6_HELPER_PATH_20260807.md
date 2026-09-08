# The noncanonical internal-close GK move has an exact four-`C_6` helper path

**Date:** 2026-08-07  
**Status:** **corrected/retracted physical inference.**  The displayed
length-four root-rotation path is exact, and the symmetric difference of
its four `C_6`s is a simple length-18 incidence cycle.  It is not
alternating in the fixed GK factor: at every internal root the common
fixed edge cancels and leaves two status-zero cross edges.  Hence this note
does not replace the missing reverse rethread.  See
`MATH_CORRECTION_GK_ROOT_PATH_C6_SYMMETRIC_DIFFERENCE_NONALTERNATING_20260807.md`.

## 1. The five roots

Let `F,G` be Dyck words and put

\[
                         D=1F0G.                       \tag{1.1}
\]

Define

\[
\begin{aligned}
 U   &=111F0G0100,\\
 W_0 &=101F0G1100,\\
 H_2 &=110F0G1100,\\
 H_3 &=110F1G0100,\\
 W_1 &=101F1G0100.
\end{aligned}                                         \tag{1.2}
\]

All five words are Dyck and distinct.  In the forced two-child notation,
`U=11D0100`; `W_0=10D1100` is the closing-child sink, while
`W_1=10D^+0100` is the internal-close sink obtained by changing the first
return of `D` upward.

## 2. Four literal root rotations

Recall that an edge of the root-rotation graph has the form

\[
 1A1B0C0D'\longleftrightarrow1A0B1C0D',               \tag{2.1}
\]

where all four displayed blocks are Dyck.

## Theorem 2.1

The sequence

\[
                         U-W_0-H_2-H_3-W_1             \tag{2.2}

is a simple path of length four in `R_m`.

### Proof

Each edge is (2.1) with the following block choices.

1. `U-W_0`:
   \[
   A=\varnothing,\quad B=D,\quad C=10,\quad D'=\varnothing.
   \]

2. `H_2-W_0`:
   \[
   A=B=\varnothing,\quad C=F,\quad D'=G1100.
   \]

3. `H_3-H_2`:
   \[
   A=10F,\quad B=G,\quad C=10,\quad D'=\varnothing.
   \]

4. `H_3-W_1`:
   \[
   A=B=\varnothing,\quad C=F1G010,\quad D'=\varnothing.
   \]

Every listed block is Dyck.  Direct substitution gives exactly the words
in (1.2).  Their displayed prefixes distinguish them, so the path is
simple. \(\square\)

## 3. Exact simple-cycle identity and failed alternation

Apply the paired-root `C_6` theorem to the four edges of (2.2).  Adjacent
circuits share exactly the fixed root edge of their common root; all other
resources are disjoint.  Their symmetric difference is therefore a simple
incidence cycle, but the phase of its edges must be audited separately.

## Proposition 3.1 (nonalternating helper cycle)

The symmetric difference of the four paired-root circuits along (2.2) is
one simple incidence cycle of length

\[
                         4\cdot4+2=18.                 \tag{3.1}

It contains all five root facets

\[
                         X_U,X_{W_0},X_{H_2},X_{H_3},X_{W_1}.            \tag{3.2}

At each internal root `W_0,H_2,H_3`, the shared selected fixed edge cancels
and the two surviving incident cross edges were both unselected.  The
cycle therefore has local status `00` and is not alternating.  It cannot
be toggled against the fixed factor, nor can the four original `C_6`s be
toggled sequentially.  A phase-repair/higher-circuit identity is still
required.

## 4. Exact remaining global gate

Even before global planting, Proposition 3.1 fails the local alternating
gate.  In an already chosen standard root path cover, the helper roots
`H_2,H_3` may additionally be internal and physically saturated, and
`W_0` is itself a sink endpoint.

The remaining statement is precisely:

> **Support-two phase-repair and planting lemma.**  For a positive-density
> subbank of the forced roots `U`, augment the simple cycle (3.1) to a
> genuinely alternating higher circuit, and choose/rethread the standard
> cover so that `H_2,H_3` are available helper ports while preserving the
> protected compiler/upper tickets.

The root relation is reduced to a fixed support-two simple-cycle scaffold,
but both its phase repair and its global host placement remain open.
