# Independent audit: balanced optional core and central-`D` binomial bound

**Date:** 2026-08-04  
**Method:** independent symbolic replay; pure mathematics only  
**Audited theorem:**
`MATH_THEOREM_OPTIONAL_BOOTSTRAP_BALANCED_CORE_AND_CENTRAL_D_BINOMIAL_20260804.md`

## Verdict

**GO, after four typographical repairs and one explicit asymptotic-range
qualification.**  The two-parameter Boolean minimum-degree induction, the
asymmetric peeling charge, the central-binomial corollaries, and the
optional-core substitution are all correct.  Nothing in the argument
proves the sharper one-sided threshold-shadow conjecture

\[
 |\mathcal A|\ge \binom{2D-1}{D-1}.
\]

The audited theorem was repaired only by restoring four missing TeX
backslashes, deleting one repeated phrase, and saying explicitly that the
optional specialization uses the eventual range `D=d-3>=2`.  No
mathematical claim or proof mechanism was changed.

## 1. Independent replay of the coordinate-section induction

Let

\[
 \mathcal A\subseteq\binom{[N]}k,
 \qquad
 \mathcal C\subseteq\binom{[N]}{k+1}
\]

have lower-to-upper minimum degree at least `a` and upper-to-lower minimum
degree at least `b`.  Fix an incidence `A_* subset C_*` and write
`x=C_*-A_*`.

In the `x=0` section, a lower set has at most one upper neighbour outside
the section, namely the set obtained by adjoining `x`; an upper set has no
lower facet containing `x`.  Thus its minimum degrees are at least
`(a-1,b)`.  This section is nonempty when `a>=2`, because `A_*` has an
upper neighbour different from `C_*`, and that neighbour cannot contain
`x`.

In the `x=1` section, after deleting `x`, a lower set loses no upper
neighbour and an upper set loses at most its unique facet not containing
`x`.  Thus its minimum degrees are at least `(a,b-1)`.  This section is
nonempty when `b>=2`, because an `A`-neighbour of `C_*` different from
`A_*` necessarily contains `x`.

Induction gives

\[
\begin{aligned}
 |\mathcal A_0|&\ge\binom{a+b-2}{b-1},&
 |\mathcal A_1|&\ge\binom{a+b-2}{b-2},\\
 |\mathcal C_0|&\ge\binom{a+b-2}{b},&
 |\mathcal C_1|&\ge\binom{a+b-2}{b-1}.
\end{aligned}
\]

The two sections are disjoint and exhaustive on each shore, so Pascal's
identity yields

\[
 |\mathcal A|\ge\binom{a+b-1}{b-1},
 \qquad
 |\mathcal C|\ge\binom{a+b-1}{b}.
\]

The base cases are exact: if `a=1`, one upper vertex supplies `b` lower
vertices; if `b=1`, one lower vertex supplies `a` upper vertices.  The
lifted consecutive levels `binom(S,b-1)` and `binom(S,b)` for
`|S|=a+b-1` attain equality, so both indices and shore orientations are
correct.

## 2. Independent replay of asymmetric peeling

Let `G=(L,R;E)` satisfy

\[
 |R|\ge |L|,
 \qquad
 |E|\ge D|R|.
\]

Delete a left vertex at current degree at most `a-1` or a right vertex at
current degree at most `b-1`.  If deletion exhausted the graph, charging
each edge when its first endpoint disappears would give

\[
 |E|\le (a-1)|L|+(b-1)|R|.
\]

When `a+b=D+1`, the right side is at most `(D-1)|R|`, contradicting the
edge hypothesis.  Hence a nonempty `(a,b)`-minimum-degree core survives.
Taking

\[
 b-1=\lfloor D/2\rfloor,
 \qquad a=D+1-b
\]

and invoking the section theorem proves

\[
 |L|\ge\binom D{\lfloor D/2\rfloor}.
\]

Under the strict imbalance `|R|>|L|`, take `a+b=D+2` with `a>=2`.  The
complete-deletion charge becomes

\[
\begin{aligned}
 (a-1)|L|+(b-1)|R|
 &=D|R|-(a-1)(|R|-|L|)\\
 &<D|R|,
\end{aligned}
\]

again impossible.  Balancing `b-1` proves

\[
 |L|\ge\binom{D+1}{\lfloor(D+1)/2\rfloor}.
\]

This extra dimension genuinely uses both strict shore imbalance and
`a>=2`; the non-strict proof cannot supply it.

## 3. Optional-core substitution

For the minimal optional maximizer, the preceding wide-gap theorem gives
the literal Boolean incidence graph with

\[
 L=B^-,\qquad R=Q,\qquad D=d-3,
\]

and exact hypotheses

\[
 |Q|\ge |B^-|+1,
 \qquad
 d_{B^-}(U)\ge D\quad(U\in Q).
\]

Consequently `|E|>=D|Q|`, and the strict peeling corollary applies once
`d-3>=2`.  The ambient wide-gap theorem assumes `d to infinity`, so this
holds for every sufficiently large parameter in its stated asymptotic
scope.  Substitution gives

\[
 |B^-|\ge
 \binom{d-2}{\lfloor(d-2)/2\rfloor}
 =\Theta\!\left(\frac{2^{d-2}}{\sqrt d}\right)
 =2^{\Omega(\sqrt m)}.
\]

No capacity multiplicity is being mistaken for a Boolean owner here:
`Q` is the set of positive-capacity owners, each such owner is one
rank-`m` set, and its unweighted incidence degree into `B^-` is at least
`d-3`.

## 4. Exact boundary of the sharper conjecture

If both original shores had minimum degree at least `D`, the section
theorem with `(a,b)=(D,D)` would immediately give

\[
 |\mathcal A|,|\mathcal C|
 \ge\binom{2D-1}{D-1}.
\]

Under the actual one-sided assumptions, only

\[
 \min_{C\in\mathcal C}d(C)\ge D,
 \qquad
 \frac{|E|}{|\mathcal A|}\ge D
\]

is known.  Peeling certifies a core whose two degree thresholds sum to
`D+1`, or to `D+2` under strict imbalance.  It does not certify a
`(D,D)` core.  Thus the central-`D` bound is unconditional, while

\[
 \left.
 \begin{array}{c}
  |\mathcal C|\ge|\mathcal A|,\\
  d_{\mathcal A}(C)\ge D\quad(C\in\mathcal C)
 \end{array}
 \right\}
 \stackrel{?}{\Longrightarrow}
 |\mathcal A|\ge\binom{2D-1}{D-1}
\]

remains a genuinely Boolean threshold-shadow problem.  The equality
model is the pair of consecutive levels `b-1,b` in a
`(2D-1)`-coordinate subcube.  The current proof neither assumes nor
derives the missing lower-shore minimum degree.

## 5. Scope conclusion

The audited result is a lower bound on the size of any surviving optional
bootstrap obstruction.  It neither removes that obstruction nor proves a
new universal-word upper bound.  It is compatible with, but does not
settle, the sharper `binom(2D-1,D-1)` conjecture.
