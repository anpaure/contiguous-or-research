# PBBS gap-potential common sections at every entrance depth

**Date:** 2026-08-05  
**Method:** pure cyclic-parenthesis mathematics; no computation or search  
**Status:** unconditional for every `m>=1` and every entrance depth
`1<=p<=m`.  This is the exact one-sided fixed-factor common-section theorem
left open in Section 5 of
`MATH_AUDIT_N_PBBS_NESTED_FAN_SECTION_AND_MORTALITY_GATE_20260727.md`.

## 1. One section at a fixed entrance depth

Put `n=2m+1` and `g=f^2`.  Fix `1<=p<=m`.  For every entrance root

\[
                         T\in{[n]\choose m-p},
\]

form its expanded unmatched-mark word: `A` denotes a forward-unmatched
zero, `C` a reverse-unmatched zero, and a shared coordinate is expanded in
the order `C_x,A_x`.  There are `2p+1` symbols of each type.

Index the `C` symbols cyclically, let `z_i` count the `A` symbols strictly
between consecutive `C` symbols, and put

\[
                         h(i+1)-h(i)=z_i-1.         \tag{1.1}
\]

Choose a `C_0` at a global maximum of `h`, and let `A_0` be the last `A`
before it.  Number the remaining `C` symbols forward and the remaining
`A` symbols backward.  Define

\[
 \boxed{
 \sigma_p(T)=T\cup\{C_0,C_1,\ldots,C_{p-1}\}.}    \tag{1.2}
\]

Resolve a tie between global maxima by any fixed rule depending only on
the literal root `T`.

The all-depth corridor theorem, applied to the deficit-`(2p+1)` word
`T`, proves that (1.2) is a middle state and

\[
 \boxed{
 \bigcap_{t=0}^{p}g^t\sigma_p(T)=T.}              \tag{1.3}
\]

Thus `sigma_p` chooses one corrected depth-`p` occurrence of every
entrance root.

## 2. Restricting a deeper global corridor

Fix `d>=1` with `p+d<=m`, put `Q=p+d`, and take

\[
                         S\in{[n]\choose m-Q}.
\]

Apply the global-maximum corridor theorem directly to `S`.  At its chosen
boundary write `A_0,C_0`, number the `C` symbols forward as

\[
 C_0,C_1,\ldots,C_{2Q},
\]

and the `A` symbols backward as

\[
 A_0,A_1,\ldots,A_{2Q}.
\]

The resulting fan starts at

\[
 B_0=S\cup\{C_0,\ldots,C_{Q-1}\},                 \tag{2.1}
\]

and satisfies

\[
                         \bigcap_{t=0}^{Q}g^tB_0=S.\tag{2.2}
\]

Its depth-`p` entrance root is, by the nested-prefix formula,

\[
 T=L_p(B_0)
  =S\cup\{C_0,\ldots,C_{d-1}\}.                  \tag{2.3}
\]

### Lemma 2.1 (induced survivor sets)

The expanded unmatched-mark word of `T` is the literal restriction of the
expanded word of `S` to

\[
 \boxed{
 \{A_0,A_1,\ldots,A_{2p}\}
 \quad\hbox{and}\quad
 \{C_d,C_{d+1},\ldots,C_{d+2p}\}.}               \tag{2.4}
\]

#### Proof

Starting from `S`, form `T` by flipping the consecutive reverse survivors
`C_0,...,C_(d-1)`.  The forward half of the corridor flip calculation says
that these flips remove the `2d` forward survivors

\[
                         F_1,\ldots,F_{2d},
\]

where `F_0=A_0` and `A_j=F_(2Q+1-j)`.  The surviving forward symbols are
therefore precisely `A_0,...,A_(2p)`.  The reversed calculation leaves
precisely `C_d,...,C_(d+2p)`.  Contraction preserves cyclic physical
order, and the shared-coordinate convention is the same before and after
restriction. `square`

### Lemma 2.2 (strict induced maximum)

In the induced word (2.4), `C_d` is the unique global maximum of the
potential (1.1), and `A_0` is the last retained `A` before it.

#### Proof

Let `R_j` be the number of retained `A` symbols strictly between `C_d`
and `C_(d+j)`, for `1<=j<=2p`.  Suppose `A_h`, `1<=h<=2p`, lies in this
arc.  If it lies in the gap after `C_i`, where

\[
                         d\le i\le d+j-1,
\]

then moving backward from `A_0` to `A_h` crosses at least

\[
 (2Q+1)-1-i\ge 2p+d+1-j                       \tag{2.5}
\]

`C` symbols.  The global corridor inequality gives `y_h<=h`.  Hence such
an `A_h` must satisfy

\[
                         h\ge2p+d+1-j.             \tag{2.6}
\]

Among `h=1,...,2p`, there are at most

\[
                         (j-d)_+                    \tag{2.7}
\]

indices satisfying (2.6).  Therefore

\[
                         R_j\le(j-d)_+<j.           \tag{2.8}
\]

Normalize the induced potential to be zero at `C_d`.  Its value at
`C_(d+j)` is exactly `R_j-j`, which is negative by (2.8).  Thus `C_d`
is the unique maximum.

Finally, `A_1,...,A_(2p)` precede `A_0` in backward `A` order, while
`C_0,...,C_(d-1)` have been removed from the survivor word.  Hence `A_0`
is the last retained `A` before `C_d`. `square`

The count (2.5) includes the shared-coordinate convention correctly: at
a physical `C_i,A_h` pair, moving backward reaches `A_h` before crossing
`C_i`, so the number crossed is `2Q-i`, which is the displayed lower
bound at the right endpoint as well.

## 3. Exact common-section theorem

### Theorem 3.1 (every deeper target occurs in the fixed section)

For every `d>=0` with `p+d<=m` and every

\[
                         S\in{[n]\choose m-p-d},
\]

there is an entrance root `T` such that

\[
 \boxed{
 \sigma_p(T)=X,
 \qquad
 \bigcap_{t=0}^{p+d}g^tX=S.}                     \tag{3.1}
\]

The same fixed map `sigma_p` works simultaneously for all `d`.

#### Proof

For `d=0`, take `T=S` and use (1.3).  For `d>=1`, use (2.3).  Lemma 2.2
says that when the rule (1.1)--(1.2) is applied to this literal root `T`,
its uniquely selected boundary is

\[
                         A_0,C_d.
\]

Numbering from that boundary, its first `p` reverse symbols are
`C_d,...,C_(d+p-1)`.  Therefore

\[
 \begin{aligned}
 \sigma_p(T)
 &=T\cup\{C_d,\ldots,C_{d+p-1}\}\\
 &=S\cup\{C_0,\ldots,C_{p+d-1}\}=B_0.
 \end{aligned}                                    \tag{3.2}
\]

Equation (2.2) now proves (3.1).

The rule `sigma_p` was defined before `S` and `d` were introduced.  If
two targets at one depth tried to use the same root, (3.2) would give the
same deterministic start and hence the same terminal intersection, so
the targets would be equal.  Reuse of one root across different depths is
automatically one compatible nested future tower. `square`

This proves all integral configuration inequalities of the old Section 5
at once.  It is stronger than the one-depth Hall criterion and stronger
than its fractional support-function relaxation: one explicit vertex of
every root simplex is selected.

## 4. Exact ledgers and occurrence compiler

Put

\[
 M=N_p={n\choose m-p},
 \qquad
 \mathcal X_p=\{\sigma_p(T):|T|=m-p\}.
\]

At extension depth `d`, let `b_d` be the number of selected histories
which have died, `G_d=M-b_d` the correct mass, `H_d` the number of missing
rank-`(m-p-d)` targets, and `E_d,tilde E_d` the raw and floor-correct
repeat excesses.

### Corollary 4.1

For every `0<=d<=m-p`,

\[
 \boxed{
 H_d=0,
 \qquad
 G_d\ge N_{p+d},
 \qquad
 b_d\le N_p-N_{p+d},
 \qquad
 E_d=G_d-N_{p+d},
 \qquad
 \widetilde E_d=0.}                               \tag{4.1}
\]

In particular `b_0=E_0=0`.  For `d>=1`,

\[
 (b_d-b_{d-1})+(E_d-E_{d-1})
 =N_{p+d-1}-N_{p+d}.                              \tag{4.2}
\]

#### Proof

Theorem 3.1 gives full support.  The standard mortality identity then
gives (4.1), exactly as in the `p=1` specialization.  Subtract consecutive
zero-hole identities to obtain (4.2). `square`

### Corollary 4.2 (integral lower occurrence SDR)

For each target in every controlled rank, choose one pair `(X,p+d)` from
(3.1).  These pairs are distinct occurrence-labelled cyclic interval
cells and give an integral one-sided lower compiler.

The statement is inside the uncut PBBS deck.  It does not assert that the
chosen cells survive an opening, erosion, Ferrers-boundary deletion, or an
ordinary-word translation.

## 5. Scope

The theorem uses one canonical PBBS factor and one deterministic section;
it uses no coordinate conjugacy, averaging, or independent rankwise
matching.  It closes:

1. every one-depth Hall gate;
2. the all-depth integral configuration-selection gate;
3. the mortality staircase and floor-correct repeat-excess gate;
4. the one-sided occurrence-level lower compiler.

It does not close:

1. the phase-shifted upper bank;
2. component hitting or rebundling into one factor;
3. residence after physical cutting;
4. survival of the chosen cells under literal erosion;
5. terminal common-cap compatibility in the final ordinary word.

At `p=1`, this theorem specializes to
`MATH_THEOREM_PBBS_GAP_POTENTIAL_SECTION_ALL_DEPTH_LOWER_COMPLETE_20260805.md`.

