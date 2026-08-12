# Independent audit of the age-composition Strassen cuts

Date: 2026-08-01

Status: `PASS`, with one repaired scope omission in the `d=2` warning:
the displayed type requires `r>=4`.  The stochastic-order orientation,
the `P/Q` inverse lifts, the positive rotation-orbit circulation and the
counterexample are correct.

## 1. Domination orientation

An age edge `c->c'` obeys

\[
                         Q(c')\le P(c).                \tag{1.1}
\]

If a circulation edge is sampled, its source and target compositions both
have law `pi`.  Hence `Q(c')` has law `Q_*pi`, `P(c)` has law `P_*pi`, and
(1.1) is a monotone coupling with `Q` below `P`.  Therefore the correct
orientation is

\[
                         Q_*\pi\preceq_{st}P_*\pi,
\]

equivalently

\[
 \Pr(Q\in U)\le\Pr(P\in U)
\]

for every upward set `U`, or the reversed inequality on every downward set.

## 2. The pushforward coupling lifts uniquely

The image of `Q` consists of vectors `x=(x_1,...,x_d)` with
`sum x_i<=r-1`; its unique inverse is

\[
                         (r-\sum x_i,x_1,\ldots,x_d).   \tag{2.1}
\]

The image of `P` consists of vectors `y=(y_0,...,y_(d-1))` with
`y_0>0`, `sum y_i<=r`; its unique inverse is

\[
                         (y_0,\ldots,y_{d-1},
                          r-\sum y_i).                 \tag{2.2}
\]

Strassen supplies a coupling `X<=Y` with laws `Q_*pi,P_*pi`.  Applying
(2.1)--(2.2) pointwise gives unique compositions `c',c` of law `pi` and
`Q(c')<=P(c)`.  Orienting mass from `c` to `c'` gives exactly the required
circulation.  No fibre multiplicity or hidden choice is omitted.

## 3. Rotation orbit

For a composition all of whose entries are positive, define

\[
                         \rho(c)=(c_d,c_0,\ldots,c_{d-1}).
\]

Every rotation remains in the legal state space because its new first
entry is positive, and

\[
                         Q(\rho(c))=P(c).              \tag{3.1}
\]

Thus every orbit edge `c->rho(c)` is legal with equality.  Uniform mass on
the distinct orbit points is stationary even when the word has a smaller
rotation period, because `rho` permutes those points.  At the literal level
the transition retains every younger class and refreshes exactly the old
`C_d` class; positivity is precisely what keeps the appended letter
nonempty.

## 4. The `d=2` warning

For `d=2`, a fully marked deficit-gap profile `(2,1)` determines

\[
                         c_2=2,\qquad c_1=1,qquad
                         c_0=r-3.                      \tag{4.1}
\]

This is a legal age composition exactly when `r>=4`, the qualification now
added to the source theorem.  It satisfies the local unit-drop condition
`1>=2-1`.  But for the upward event

\[
                         U=\{x:x_2\ge2\},
\]

the point mass has

\[
                         Q(c)\in U,qquad P(c)\notin U,
\]

because `Q(c)=(1,2)` and the second coordinate of `P(c)` is `c_1=1`.
Hence the Strassen cut fails.  Since both suffix addresses are already
marked, no unmarked suffix can change the uniquely determined type.  The
example correctly proves that the one-row unit-drop law is insufficient.

## 5. Scope

Combining the theorem with the audited age quotient eliminates the explicit
edge-flow variables from the symmetric rank-only fractional gate.  It does
not prove that the triangular vector satisfies the cuts.  It also does not
restore one-copy owner selection, literal connected/rooted support,
comparator pins, Johnson/Catalan topology, upper witnesses, residence at
joins, occurrence-labelled common-cap matching, or regeneration.

The exact next fractional statement is to construct one distribution `pi`
which simultaneously satisfies the suffix-rank capacities and all upward
Strassen cuts, or to give an explicit monotone coupling.  The proposed
unit-descent lemma remains open.

