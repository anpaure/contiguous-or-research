# Literal lower-deck waste is exactly excess `L1` discrepancy

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional corollary of the fixed-word functional-occurrence
and pinned-waste theorems.  It recasts the remaining one-copy lower problem
as an exact integer `L1`-rounding problem.  It does not construct the
required antecedent or a physically liftable descent move.

## 0. Setup

Use the notation of the pinned-waste theorem.  After deleting the forced
target/address pairs `Pi`, let

\[
 m(S)=|\{C\in\mathcal C_d\setminus C(\Pi):
                    \operatorname{OR}_A(C)=S\}|
 \qquad(S\in\mathcal L\setminus L(\Pi)).             \tag{0.1}
\]

Let

\[
 M=|\{S:m(S)=0\}|,
 \qquad
 D=\sum_S(m(S)-1)_+,                                 \tag{0.2}
\]

let `Q` count remaining cells whose value is one of the already forced
targets, let `R` count remaining rank-`r` cells, and let `sigma` be the
scalar short-cell slack.  The exact pinned-waste identity is

\[
                         M=D+Q+R-\sigma.              \tag{0.3}
\]

Define the occurrence discrepancy

\[
                         V=\sum_S|m(S)-1|.            \tag{0.4}
\]

## 1. Exact `L1` identity

### Theorem 1.1

\[
 \boxed{
  2M=V+Q+R-\sigma,
  \qquad
  2D=V-Q-R+\sigma.}                                  \tag{1.1}
\]

Equivalently, writing

\[
                         s=\sigma-Q-R,                \tag{1.2}
\]

for the residual occurrence surplus,

\[
                         M={V-s\over2},
 \qquad                  D={V+s\over2}.              \tag{1.3}
\]

#### Proof

Every absent target contributes one to (0.4), every target occurring
`m>=2` times contributes `m-1`, and a target occurring once contributes
zero.  Therefore

\[
                              V=M+D.                  \tag{1.4}
\]

Combine (1.4) with (0.3) and solve for `M,D`. \(\square\)

### Corollary 1.2 (parity and the exact optimum)

The integer `V+Q+R-sigma` is nonnegative and even.  Moreover,

\[
 M\le C
 \quad\Longleftrightarrow\quad
 V\le \sigma-Q-R+2C.                                 \tag{1.5}
\]

In particular, complete residual coverage is possible only if

\[
                         Q+R\le\sigma,                \tag{1.6}
\]

and for a fixed word it holds exactly when

\[
                         V=\sigma-Q-R.                \tag{1.7}
\]

#### Proof

Equation (1.5) is (1.1).  The total number of residual-target occurrences
minus the number of residual targets is `s`.  Hence `V>=|s|`.  If `M=0`,
all counts are at least one, so `s>=0` and `V=s`.  Conversely, if `s>=0`
and `V=s`, then (1.3) gives `M=0`. \(\square\)

Thus the one-copy problem is not merely to make the occurrence vector
close to all ones.  It is to attain its **minimum possible** `L1`
discrepancy, up to an additive constant, after the forced-value and
rank-`r` leakage `Q+R` have been priced.

For the unpinned face, put `Q=0`; then

\[
                 2M=\sum_{S\in\mathcal L}|m_A(S)-1|
                         +R_A-\sigma.                 \tag{1.8}
\]

### Corollary 1.3 (forcing only reclassifies existing waste)

Assume `Pi` contains one exact address for each of its distinct strict-
lower target values.  Let `D_A,R_A,M_A` be the unpinned statistics of the
same fixed word.  Then

\[
 \boxed{
 D_A^\Pi+Q_A^\Pi=D_A,\qquad
 R_A^\Pi=R_A,\qquad
 M_A^\Pi=M_A.}                                       \tag{1.9}
\]

Thus the forced rays add no fixed-word literal-waste surcharge.  Their only
possible cost is indirect: the pinned inverse fibre may exclude words with
smaller unpinned waste.

#### Proof

If a forced target `S` occurs `m_A(S)` times, deleting its chosen address
and removing its target row leaves exactly `m_A(S)-1` occurrences counted
by `Q_A^Pi`.  This is exactly the contribution of `S` to the unpinned
duplicate count `D_A`.  Every unforced target has the same occurrence and
duplicate count before and after contraction.  Summing proves the first
identity.  A forced cell has a strict-lower value, so no rank-`r` cell is
deleted, proving the second.  Finally every forced target is present, while
the occurrence status of every unforced target is unchanged, proving the
third. \(\square\)

## 2. Exact unit-transfer descent

### Proposition 2.1

Suppose a physically legal change of the antecedent preserves all owner,
pin, upper, residence, and topology requirements, leaves `Q,R` unchanged,
and changes the residual occurrence vector by

\[
                         m' = m-e_U+e_Z,              \tag{2.1}
\]

where `m(U)>=2` and `m(Z)=0`.  Then

\[
                         V'=V-2,\qquad M'=M-1.        \tag{2.2}
\]

#### Proof

At `U`, the contribution `m(U)-1` to `V` falls by one.  At the absent
target `Z`, the contribution `1` falls to zero.  Every other coordinate of
the occurrence vector is unchanged, proving the first equality.  Equation
(1.1), with fixed `Q,R,sigma`, proves the second. \(\square\)

Consequently a catalogue of physically liftable unit transfers from every
surplus occurrence to every missing target would give a monotone exact
descent with no local minima.  Existing abstract switches or fractional
rotor balance do not yet supply such a catalogue in one resident,
upper-complete owner chronology; this is precisely the physical lifting
content still missing.

## 3. Scope

The identities apply only after one literal word and forced bank have been
fixed.  A pre-word candidate graph may still have multiple possible values
per address.  The corollary does not prove that an arbitrary vector move
(2.1) is realizable, nor that a realizable packet leaves `Q,R` fixed.

Its use is to give the remaining integral rounding problem a single exact
potential:

\[
 \boxed{
  \mathcal E(A,\Pi)
   =\sum_S|m_A^\Pi(S)-1|+Q_A^\Pi+R_A^\Pi-\sigma
   =2M_A^\Pi.}                                       \tag{3.1}
\]

Proving `\mathcal E=O(1)` is exactly the terminal lower-deck part of the
additive-constant conjecture.

## 4. Dependencies

- `MATH_THEOREM_FIXED_WORD_FUNCTIONAL_OCCURRENCE_AND_ONE_PHASE_HALL_COLLAPSE_20260804.md`
- `MATH_THEOREM_PINNED_MAXIMAL_ENVELOPE_GLOBAL_EXTENSION_AND_WASTE_IDENTITY_20260804.md`
