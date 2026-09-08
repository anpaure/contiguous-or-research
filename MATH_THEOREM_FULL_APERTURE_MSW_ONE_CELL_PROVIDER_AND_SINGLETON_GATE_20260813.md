# Exact one-cell providers for the full-aperture MSW factor, and the singleton gate

**Date:** 2026-08-13  
**Status:** unconditional local compiler theorem for the exact
full-aperture owner factor.  It computes the exact optional union `U_C`
and mandatory mask `M_C` for every strict-lower cell.  It proves that the
unchanged full-aperture chronology cannot realize singleton targets.

## 1. Odd ambient dimension

Put

\[
 k=2m+1,\qquad R=m+1,\qquad q=d+1,
 \qquad a=m-q+2=R-d,                                \tag{1.1}
\]

and assume

\[
 2\le q,\qquad m\ge2q-2.                            \tag{1.2}
\]

Fix one cyclic order

\[
 \sigma=(x_0,\ldots,x_{2m})
\]

from the full-aperture MSW factor.  Index intervals by their first
coordinate and use the maximal source antecedent

\[
 P_j=\{x_j,x_{j+1},\ldots,x_{j+a-1}\}.              \tag{1.3}
\]

Its `q`-fold owner unions are the `(m+1)`-windows.

Let `C=[i,i+ell-1]` be a cyclic source cell of length

\[
 1\le\ell\le d=q-1.                                 \tag{1.4}
\]

Define the optional union and mandatory mask as in the exact one-cell
compiler theorem:

\[
 U_C=\bigcup_{j\in C}P_j,                            \tag{1.5}
\]

and `M_C` is the set of coordinates for which all carriers in at least
one owner window lie inside `C`.

### Theorem 1.1 (exact odd provider formula)

One has

\[
 \boxed{
 U_C=I_i^{a+\ell-1}
     =I_i^{m-q+\ell+1},}                             \tag{1.6}
\]

and

\[
 \boxed{
 M_C=I_i^\ell\ \dot\cup\ I_{i+a-1}^\ell.}          \tag{1.7}
\]

In particular,

\[
 |U_C|=m-q+\ell+1,
 \qquad |M_C|=2\ell.                                \tag{1.8}
\]

A nonempty strict-lower target `S` can be realized on `C` by some source
antecedent which preserves the entire owner row and agrees with the
maximal antecedent outside `C` if and only if

\[
 \boxed{M_C\subseteq S\subseteq U_C.}               \tag{1.9}
\]

The same inclusions are necessary for **any** antecedent inducing the
fixed owner row, even if it is also changed outside `C`.

#### Proof

The union of `ell` consecutive `a`-windows is the interval of length
`a+ell-1`, proving (1.6).

Fix a coordinate `x_t`.  Its safe source-carrier positions form the
cyclic interval

\[
 E_t=[t-a+1,t].                                     \tag{1.10}
\]

The coordinate is mandatory in `C` precisely when some `q`-window of
source positions has a nonempty intersection with `E_t` wholly contained
in `C`.  Since `q+a=m+2<2m+1`, such an intersection is one interval.  It
can lie wholly in `C` if and only if `C` contains an endpoint of `E_t`:
necessity follows because an interval cut out of `E_t` by a crossing
`q`-window is an initial or terminal segment, and sufficiency follows by
choosing a `q`-window whose overlap is that endpoint alone.  Therefore

\[
 t\in C\quad\text{or}\quad t-a+1\in C,
\]

which is exactly (1.7).  Condition (1.2) makes the two displayed
`ell`-intervals disjoint for every `ell<=q-1`, proving (1.8).

The general exact one-cell theorem says that capping `P_j` to
`P_j cap S` on `C` works if and only if

\[
 S\subseteq U_C,\qquad M_C\subseteq S,
 \qquad P_j\cap S\ne\varnothing\quad(j\in C).       \tag{1.11}
\]

Here the last condition is automatic from `M_C subseteq S`, because
`x_j in M_C cap P_j` for each `j in C`.  This proves sufficiency and the
first necessity assertion.

For the stronger necessity, every source letter of an arbitrary
antecedent inducing the same owner row lies inside its safe envelope
`P_j`; hence a target on `C` lies inside `U_C`.  Moreover, the first and
last positive owner occurrences of `x_t` force emissions at the two
endpoints of the safe interval (1.10).  If either endpoint lies in `C`,
that forced coordinate belongs to the cell union.  Thus `M_C subseteq S`
for every antecedent.  `square`

### Corollary 1.2 (rank feasibility)

If `|S|=s` and `S` is realized on a length-`ell` cell, necessarily

\[
 2\ell\le s\le m-q+\ell+1.                          \tag{1.12}
\]

Equivalently, a feasible cell length must lie in

\[
 \max\{1,s-m+q-1\}
 \le\ell\le
 \min\{q-1,\lfloor s/2\rfloor\}.                   \tag{1.13}
\]

These scalar inequalities are not sufficient without the literal
containments (1.9).

At `ell=q-1`, (1.6) is an `m`-window and the exact MSW factor supplies
every rank-`m` target once.  At `ell=q-h-1`, the optional union has rank
`m-h`; a target of that rank is realized with no capping exactly when it
occurs as the corresponding cyclic interval.  Coverage of all such
shorter intervals by one MSW factor is a separate design question.

## 2. The singleton obstruction is chronology-level

### Corollary 2.1

No nonempty source interval of any antecedent inducing this fixed
full-aperture owner cycle can have singleton union.

#### Proof

Every strict-lower interval has some length `ell>=1`.  Its union contains
the mandatory set `M_C`, whose size is `2ell>=2`.  `square`

The reason is structural.  Each coordinate has a positive owner run of
length `m+1>q`.  Its first positive owner forces one source emission at
the left endpoint of its safe-carrier interval, and its last positive
owner forces another at the right endpoint.  At every source position,
one coordinate is forced there as a left endpoint and another distinct
coordinate as a right endpoint.

Thus the exact MSW owner factor does not by itself realize the `k`
singleton targets.  This does **not** refute the global construction:
one may replace a controlled set of components by minimal-run rails, fuse
runs through chronology-changing trades, or use boundary/terminal
gadgets.  But a claim that all strict-lower targets follow from the
unchanged full-aperture factor is false.

## 3. Even ambient dimension

Let

\[
 k=2m,qquad R=m,qquad T=[k]\setminus\{x\},
 \qquad |T|=2m-1,                                   \tag{3.1}
\]

and assume `m>=2q-1`.  For one MSW order on `T`, the no-`x` source has

\[
 P_j^0=I_j^{m-q+1},                                  \tag{3.2}
\]

and the with-`x` source has

\[
 P_j^1=\{x\}\cup I_j^{m-q}.                         \tag{3.3}
\]

For a length-`ell` cell `C=[i,i+ell-1]`, the same proof gives

\[
 \boxed{
 U_C^0=I_i^{m-q+\ell},
 \qquad
 M_C^0=I_i^\ell\dot\cup I_{i+m-q}^\ell,}           \tag{3.4}
\]

and

\[
 \boxed{
 U_C^1=\{x\}\cup I_i^{m-q+\ell-1},
 \qquad
 M_C^1=\{x\}\cup I_i^\ell
                    \dot\cup I_{i+m-q-1}^\ell.}     \tag{3.5}
\]

The exact provider conditions are respectively

\[
 M_C^0\subseteq S\subseteq U_C^0,                   \tag{3.6}
\]

and

\[
 M_C^1\subseteq S\subseteq U_C^1.                   \tag{3.7}
\]

In particular the mandatory sizes are

\[
 |M_C^0|=2\ell,
 \qquad |M_C^1|=1+2\ell.                            \tag{3.8}
\]

At `ell=q-1`, the no-`x` optional unions are the original exact
MSW `(m-1)`-set factor.  At the second shadow `ell=q-2`, the two optional
rows are

\[
 I^{m-2},qquad \{x\}\cup I^{m-3}.                  \tag{3.9}
\]

Their complete named-target coverage is not a consequence of the MSW
owner factor and remains an explicit lower-design gate.

## 4. Consequence for the proof architecture

The full-aperture theorem closes exact positive owner rounding and, in odd
dimension, the immediate lower row.  The present theorem shows precisely
what remains below it:

1. choose or modify the MSW factor so the interval families in the
   remaining ranks admit a left-perfect provider matching under (1.9);
2. introduce chronology-changing gadgets that create run length exactly
   `q` and hence singleton-capable source positions; and
3. perform those changes while retaining owner exactness, residence,
   fusion, upper witnesses, and cap tickets.

The lower gate is therefore no longer an unspecified Ferrers capacity
problem.  It is the explicit interval-containment system

\[
 M_C\subseteq S\subseteq U_C
\]

with (1.6)--(1.8) and (3.4)--(3.5).

