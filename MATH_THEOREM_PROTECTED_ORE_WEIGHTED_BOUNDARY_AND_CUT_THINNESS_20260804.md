# Protected Middle-Levels extension as an exact weighted-boundary inequality

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical identity and sufficient
cut-thinness criterion.  It sharpens the protected Ore--Ryser formulation
for a prescribed maximum-degree-two incidence bank.  It does not construct
the balanced upper-witness bank required by the common-history hinge ring.

## 0. Setting

Fix `m>=2`.  Let `ML_m` be the `m`-regular bipartite containment graph with shores

\[
 \mathcal L={ [2m-1]\choose m-1},
 \qquad
 \mathcal U={ [2m-1]\choose m}.
\]

Let `P subseteq ML_m` have maximum degree at most two.  For
`A subseteq mathcal L` and `U in mathcal U`, put

\[
 a_U=|N(U)\cap A|,
 \qquad
 p_U=e_P(U,\mathcal L\setminus A).
\tag{0.1}
\]

The exact protected Ore--Ryser theorem says that `P` extends to a spanning
two-factor if and only if

\[
 \lambda_P(A)\le \sigma(A)
 \qquad(A\subseteq\mathcal L),
\tag{0.2}
\]

where

\[
 \lambda_P(A)=
 \sum_U\left(\min\{2,a_U\}-\min\{2-p_U,a_U\}\right)
\tag{0.3}
\]

and

\[
 \sigma(A)=\sum_U\min\{2,a_U\}-2|A|.
\tag{0.4}
\]

The point of this note is that the right side is exactly a weighted vertex
boundary, rather than an opaque Hall slack.

## 1. Exact weighted-boundary identity

For `0<=a<=m`, define

\[
 h_m(a)=
 \begin{cases}
 0,&a=0\text{ or }a=m,\\
 (m-2)/m,&a=1,\\
 2(m-a)/m,&2\le a\le m-1.
 \end{cases}
\tag{1.1}
\]

### Theorem 1.1

For every `A subseteq mathcal L`,

\[
 \boxed{\sigma(A)=\sum_{U\in\mathcal U}h_m(a_U).}
\tag{1.2}
\]

Equivalently, if

\[
 n_1(A)=|\{U:a_U=1\}|,
 \qquad
 b_{\ge2}(A)=\sum_{U:2\le a_U\le m-1}(m-a_U),
\tag{1.3}
\]

then

\[
 \boxed{
 m\sigma(A)=(m-2)n_1(A)+2b_{\ge2}(A).}
\tag{1.4}
\]

#### Proof

Regularity gives

\[
 \sum_U a_U=m|A|.
\tag{1.5}
\]

Therefore

\[
 \sigma(A)=
 \sum_U\left(\min\{2,a_U\}-{2a_U\over m}\right).
\tag{1.6}
\]

The summand in (1.6) is zero at `a=0,m`, equals `(m-2)/m`
at `a=1`, and equals `2(m-a)/m` for `2<=a<=m-1`.
This is (1.2), and grouping the two kinds of mixed owners gives (1.4).
\(\square\)

At the endpoint `a_U=m`, all neighbours of `U` lie in `A`, so
`p_U=0` automatically.  Thus this owner contributes zero both to the
weighted boundary and to the protected loss.  This endpoint is not a
discarded positive-capacity row.

Thus only owners meeting both shores of the lower cut contribute capacity.
An owner with one neighbour in `A` contributes `m-2` integer tokens after
scaling by `m`; an owner with at least two contributes two tokens for each
neighbour outside `A`.

## 2. Exact protected consumption

Put

\[
 q_1^P(A)=|\{U:a_U=1,\ p_U=2\}|,
 \qquad
 q_{\ge2}^P(A)=\sum_{U:a_U\ge2}p_U.
\tag{2.1}
\]

### Theorem 2.1

The protected loss is

\[
 \boxed{\lambda_P(A)=q_1^P(A)+q_{\ge2}^P(A).}
\tag{2.2}
\]

Consequently `P` extends to a spanning two-factor if and only if, for every
`A subseteq mathcal L`,

\[
 \boxed{
 m\bigl(q_1^P(A)+q_{\ge2}^P(A)\bigr)
 \le (m-2)n_1(A)+2b_{\ge2}(A).}
\tag{2.3}
\]

#### Proof

For a fixed owner the summand in (0.3) is zero when `a_U=0`; it is one
exactly when `a_U=1,p_U=2`; and it equals `p_U` when `a_U>=2`.
Summing proves (2.2).  Combine (2.2) with Theorem 1.1 and (0.2).
\(\square\)

Equation (2.3) is the exact balanced-endpoint condition missing from a
mere `o(W)` upper-cone reservoir.  It prices the protected bank against
every lower cut in the same units.

### Corollary 2.2 (separated cut-thinness certificate)

It is sufficient that, for every `A subseteq mathcal L`,

\[
 m q_1^P(A)\le(m-2)n_1(A)
\tag{2.4}
\]

and

\[
 m q_{\ge2}^P(A)\le2b_{\ge2}(A).
\tag{2.5}
\]

More formally, it is enough to choose nonnegative numbers
`c_1(A),c_2(A)` for every cut, with

\[
 c_1(A)+c_2(A)\le (m-2)n_1(A)+2b_{\ge2}(A),
\]

such that `m q_1^P(A)<=c_1(A)` and
`m q_{\ge2}^P(A)<=c_2(A)`.  The displayed separated certificate is the
special choice `c_1=(m-2)n_1` and `c_2=2b_{\ge2}`.

#### Proof

Add (2.4) and (2.5), then apply Theorem 2.1. \(\square\)

The separated certificate is stronger than necessary, but exposes the two
different construction tasks: do not saturate too many one-neighbour
owners from the wrong shore, and make the remaining protected incidences a
`2/m`-thin selection of the multi-neighbour boundary.

## 3. Sharp singleton row

For `A={x}`, each of the `m` owners over `x` has `a_U=1`.  Hence

\[
 n_1(A)=m,
 \qquad b_{\ge2}(A)=0,
 \qquad \sigma(A)=m-2.
\tag{3.1}
\]

The exact row (2.3) becomes

\[
 \boxed{
 |\{U\supset x:e_P(U,\mathcal L\setminus\{x\})=2\}|\le m-2.}
\tag{3.2}
\]

Thus every lower star must retain at least two owner-neighbours not already
saturated from its complement.  The one-cone obstruction with `m-1`
saturated neighbours violates (3.2) by exactly one.

## 4. Consequence for the hinge-ring programme

For the cyclic common-history hinge ring, all potentially lost old upper
targets lie above finitely many rank-`m+1` seam bases.  Cone localization
shows that a dedicated witness reservoir may use `o(W)` incidences, but the
counterexample demonstrates that this scalar fact does not imply factor
extension.

The proof-safe positive target is now exact:

> construct the occurrence-labelled avoiding witness paths so that their
> protected incidence union satisfies (2.3) for every lower-shore cut.

Once (2.3) holds, residual Ore--Ryser supplies the spanning owner/lower-q1
two-factor.  The common-history cyclic rethread then preserves the entire
strict-lower compiler, while the protected reservoir retains every target
in the localized upper-damage family.  Component distribution and the
common cap remain separate global rows.

No assertion that such a cut-thin reservoir exists is made here.

## 5. Dependency

The only nontrivial input is the exact protected Ore--Ryser criterion in
`MATH_OBSTRUCTION_UPPER_CONE_WITNESS_BANK_PROTECTED_FACTOR_EXTENSION_20260804.md`.
