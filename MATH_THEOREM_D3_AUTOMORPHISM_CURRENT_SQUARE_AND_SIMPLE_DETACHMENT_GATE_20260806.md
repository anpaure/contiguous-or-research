# The `D_3` port-automorphism square cancels every rail current, but is not simple

**Date:** 2026-08-06  
**Method:** pure symbolic calculation  
**Status:** unconditional complete-current multifactor trade and an exact
capacity-one obstruction.  It does not yet give a plantable partial factor.

## 1. The four conjugate sealed slots

Use the suffix-stable negative edge `12` of the anchored `D_3` pentagon.
Its inverse-pair normal form has

\[
 X=(V,\infty),\qquad Y=(1,U,6),qquad
 (a,d;b,c)=(4,3;5,2).                                \tag{1.1}
\]

The port automorphism group

\[
 H=\langle(2\ 3),(4\ 5)\rangle                     \tag{1.2}
\]

fixes the ordered banks `X,Y` and sends (1.1) to the four slots

\[
 (4,3;5,2),\quad(4,2;5,3),\quad
 (5,3;4,2),\quad(5,2;4,3).                           \tag{1.3}
\]

Every conjugate is endpoint-sealed, because (1.2) preserves the `D_3`
port family and conjugates the sealed trade.

For fixed `X,Y`, write `D(a,d)` for the **complete** proper-interval
current of the inverse-pair move.  At every interval length the two-rail
formula has the form

\[
                         D(a,d)=F(a)-F(d)             \tag{1.4}
\]

for a profile-dependent map `F`.  Hence, simultaneously at every width,

\[
 \boxed{D(4,3)-D(4,2)-D(5,3)+D(5,2)=0.}             \tag{1.5}
\]

This is the ordinary rectangular cocycle identity on the active labels.

## 2. Literal cancellation leaves four rows on each shore

For fixed ordered banks `X,Y`, let

\[
 \mathcal P(a,d;b,c)=
 \{(a,b,X,c,d,Y),\ (b,d,X,a,c,Y)\}.                  \tag{2.1}
\]

The native involution sends

\[
 \mathcal P(a,d;b,c)\longleftrightarrow
 \mathcal P(d,a;b,c).                                \tag{2.2}
\]

Take the signed square

\[
 T(4,3;5,2)-T(4,2;5,3)-T(5,3;4,2)+T(5,2;4,3).      \tag{2.3}
\]

For a row `(p,q,X,r,s,Y)`, record only its active tuple `pqrs`.  Expanding
(2.3), four identical rows occur once on each shore and cancel:

\[
                         4523,\ 5432,\ 5423,\ 4532.  \tag{2.4}
\]

The reduced old and new shores are therefore

\[
\begin{aligned}
 \mathcal Q^-&=\{5342,4253,2534,3425\},\\
 \mathcal Q^+&=\{3524,2435,5243,4352\},             \tag{2.5}
\end{aligned}
\]

with `X,Y` restored in the fixed slots of every tuple.

### Theorem 2.1 (complete-current four-for-four identity)

The two row families in (2.5) have equal aggregate cyclic interval
multisets at every length.  They also have equal oriented endpoint current.

#### Proof

Each summand of (2.3) is exact on the two central cyclic interval palettes.
Equation (1.5) cancels every proper lower interval current.  Complementation
cancels every proper upper interval current.  Removing rows which occur on
both shores preserves all those equalities and gives (2.5).

Each summand is an endpoint-sealed conjugate of edge `12`; hence the signed
sum, and therefore the reduced identity, has zero oriented endpoint
current.  \(\square\)

Thus (2.5) is a genuine finite all-width trade identity, not merely a q1
relation.

## 3. Exact simplicity obstruction

At the `D_3` base put `X=(\infty)` and `Y=(1,6)`.  A row with active tuple
`pqrs` has the seven cyclic rank-three windows

\[
 pq\infty,\ q\infty r,\ \infty rs,\ rs1,\ s16,\ 16p,\ 6pq.
                                                               \tag{3.1}
\]

Already on the old shore of (2.5), the rows `5342` and `2534` both contain

\[
                         \{\infty,3,5\},\qquad
                         \{\infty,3,4\}.              \tag{3.2}
\]

There are further repetitions: `5342` and `4253` share
`{infinity,2,4}`, while `5342` and `2534` share `{1,2,6}`, and so on.
Consequently `Q^-` is not a simple partial central factor.  The same
conclusion follows for `Q^+` from equality of the aggregate central
ledger.

### Proposition 3.1 (no naive common-tail planting)

Appending one identical common suffix to all four rows does not make
(2.5) simple.

#### Proof

The common-tail functor sends every base central state `Z` on the base
segment to `Z+S_0`, with the same `S_0` in every row.  Hence each equality
in (3.2) remains an equality after suspension.  \(\square\)

The all-width current is solved, but central capacity one is not.

## 4. The exact successor

The required next statement is a finite detachment theorem.

> **Automorphism-square detachment lemma.**  Lift the eight signed
> inverse-pair packets of (2.3) into finitely many tail/context sheets so
> that (i) every central owner/root occurrence is used at most once on each
> shore, (ii) the paired all-width claims still realize the pointwise
> rectangle cancellation (1.5), (iii) endpoints remain sealed, and (iv)
> after cancelling common rows the resulting action is nontrivial.

Any such detachment is constant-size at the packet-type level.  Together
with the polynomial protected-factor completion theorem, it would give a
plantable zero-current changing-slot macro for all sufficiently large
dimensions.

The obstruction in Section 3 explains why abstract orbit cancellation is
not by itself that lemma: identical current profiles force shared claims,
whereas a partial exact factor requires the central occurrences to split.
