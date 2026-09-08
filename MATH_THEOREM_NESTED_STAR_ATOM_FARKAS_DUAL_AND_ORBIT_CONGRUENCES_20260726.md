# Nested-star atoms: exact owner--\(BA\)-flow Farkas dual and integral orbit congruences

Date: 2026-07-26

Method: finite-dimensional linear programming and exact orbit counting.  No
computation, search, or solver is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad
 W=\binom{n}{m},
 \qquad
 C=BA.
\]

Let \(\mathcal A\) be the fully labelled catalogue of canonical nested-star
atoms from
`MATH_THEOREM_NESTED_STAR_ATOM_OWNER_NIBBLE_AND_FLOW_GATE_20260726.md`.
Every atom has six distinct middle-owner fibres, three source states, and
three forced \(A\)-successor states.  Its three nested Johnson divergences
cancel at every depth.  The remaining signed equations are the de Bruijn
flow equations pairing its source set with its \(C=BA\) image.

This note proves four exact statements.

1.  The owner-leave and signed-flow problem is the finite LP

    \[
    Ax+\ell={\bf1},
    \qquad
    Dx=r,
    \qquad
    {\bf1}^{\mathsf T}\ell\le L,
    \qquad
    \frac12\lVert r\rVert_1\le\Delta,
    \tag{0.1}
    \]

    with \(x,\ell\ge0\).  The corresponding ILP has
    \(x\in\{0,1\}^{\mathcal A}\) and
    \(\ell\in\{0,1\}^{\binom{[n]}m}\).

2.  Its exact Farkas dual is as follows.  For an owner potential \(u\)
    and a state potential \(\phi\), suppose that every atom \(\alpha\)
    satisfies

    \[
      \sum_{X\in\Omega(\alpha)}u_X
      +
      \sum_{e\in I(\alpha)}(\phi_e-\phi_{Ce})\le0.
    \tag{0.2}
    \]

    Then (0.1) is feasible if and only if every such pair obeys

    \[
    \boxed{
      \sum_Xu_X
      \le
      L\max\{0,\max_Xu_X\}
      +\Delta\max_{Q\in\mathcal E/\langle C\rangle}
                   \operatorname{osc}_{Q}(\phi).}
    \tag{0.3}
    \]

    Thus the exact dual norm of signed \(BA\)-flow error is not a global
    sup norm.  It is the largest oscillation on one \(BA\)-orbit.

3.  The uniform fractional point satisfies the owner and flow equations
    with zero leave and zero signed divergence.  Averaging (0.2) against
    it gives the stronger conclusion

    \[
                         \sum_Xu_X\le0.
    \tag{0.4}
    \]

    Hence there is no fractional Farkas obstruction, for any
    \(L,\Delta\ge0\).

4.  For a Boolean owner packing, the signed flow norm has an exact orbit
    interpretation: it is the number of cyclic selected intervals on all
    partially used \(BA\)-orbits.  Exact flow therefore forces full
    \(BA\)-orbits of length \(m(m+1)\).  If \(\ell\) owners are left and
    flow is exact, then necessarily

    \[
      W-\ell\equiv0\pmod 6,
      \qquad
      W-\ell\equiv0\pmod{2m(m+1)}.
    \tag{0.5}
    \]

    In particular exact owner coverage and exact flow fail for every
    prime \(m=p>2\), since
    \(\binom{2p+1}{p}\equiv2\pmod p\).  These congruences are genuine
    exact-rounding obstructions, but their combined modulus is
    \(O(m^2)\).  They do not by themselves exclude an \(o(W)\) leave.

The desired approximate integral rounding is therefore reduced exactly,
but not solved by LP duality: choose an owner packing covering
\(W-o(W)\) fibres for which the source phases form only \(o(W)\) cyclic
intervals on the \(BA\)-orbits.

## 1. Atom columns

Let

\[
 \mathcal O=\binom{[n]}m
\]

be the owner set and let \(\mathcal E\) be the permutation-state set.
For a fully labelled atom \(\alpha\), write

\[
 I(\alpha)=\{e_1,e_2,e_3\},
 \qquad
 O(\alpha)=A I(\alpha),
 \qquad
 \Omega(\alpha)=
 \{\kappa(e):e\in I(\alpha)\cup O(\alpha)\}.
\tag{1.1}
\]

The nested-star construction gives \(|\Omega(\alpha)|=6\).  Define the
owner column and source column by

\[
 a_\alpha(X)={\bf1}_{\{X\in\Omega(\alpha)\}},
 \qquad
 s_\alpha(e)={\bf1}_{\{e\in I(\alpha)\}}.
\tag{1.2}
\]

The signed de Bruijn-flow column is

\[
 d_\alpha=s_\alpha-C s_\alpha,
 \qquad
 d_\alpha(e)=
 {\bf1}_{\{e\in I(\alpha)\}}
 -{\bf1}_{\{e\in C I(\alpha)\}}.
\tag{1.3}
\]

Here \((Cs)(e)=s(C^{-1}e)\), so the second formula fixes the convention.
Let \(A\) and \(D\) be the matrices with columns \(a_\alpha\) and
\(d_\alpha\), respectively.  Every \(D\)-column sums to zero on every
\(C\)-orbit.

The exact atom circulation equations are

\[
                         Ax={\bf1},
 \qquad
                         Dx=0.
\tag{1.4}
\]

Indeed, the first equation selects one state from each owner fibre.  The
second says that the aggregate source multiplicity at each state equals
the aggregate multiplicity arriving from forced \(A\)-successors by a
\(B\)-transition.  Equivalently, it is equation
\(S=BA(S)\) when \(x\) is Boolean.

## 2. The LP and ILP with error budgets

Fix real budgets \(L,\Delta\ge0\).  Define \(P(L,\Delta)\) to be the
system

\[
\begin{aligned}
 Ax+\ell&={\bf1},\\
 Dx&=r,\\
 x&\ge0,\qquad \ell\ge0,\\
 \sum_{X\in\mathcal O}\ell_X&\le L,\\
 \frac12\sum_{e\in\mathcal E}|r_e|&\le\Delta.
\end{aligned}
\tag{2.1}
\]

This is an LP: write \(r=p-q\), with \(p,q\ge0\), and impose
\({\bf1}^{\mathsf T}(p+q)\le2\Delta\).

For the integral problem require

\[
 x_\alpha\in\{0,1\},
 \qquad
 \ell_X\in\{0,1\}.
\tag{2.2}
\]

No explicit inequality \(x_\alpha\le1\) is needed in the relaxation:
every atom has an owner in its support, and the corresponding row of
\(Ax\le{\bf1}\) already gives it.  In the ILP, (2.1) says precisely that
the selected atoms are owner-disjoint, leave at most \(L\) owners, and
have signed \(BA\)-flow error at most \(\Delta\).

For a \(C\)-orbit \(Q\), put

\[
 \operatorname{osc}_Q(\phi)
 =\max_{e\in Q}\phi_e-\min_{e\in Q}\phi_e,
 \qquad
 \operatorname{Osc}_C(\phi)
 =\max_Q\operatorname{osc}_Q(\phi).
\tag{2.3}
\]

## 3. Exact Farkas dual

### Theorem 3.1 (owner-leave/flow-error Farkas theorem)

The LP \(P(L,\Delta)\) is feasible if and only if the following holds.
For every \(u\in\mathbb R^{\mathcal O}\) and
\(\phi\in\mathbb R^{\mathcal E}\) satisfying

\[
 \boxed{
 \sum_{X\in\Omega(\alpha)}u_X
 +
 \sum_{e\in I(\alpha)}(\phi_e-\phi_{Ce})\le0
 \quad(\alpha\in\mathcal A),}
\tag{3.1}
\]

one has

\[
 \boxed{
 \sum_{X\in\mathcal O}u_X
 \le
 L\,u_{\max}^{+}
 +\Delta\,\operatorname{Osc}_C(\phi),}
\tag{3.2}
\]

where

\[
                         u_{\max}^{+}
 =\max\{0,\max_Xu_X\}.
\]

#### Proof

First suppose (2.1) is feasible.  Multiply (3.1) by \(x_\alpha\) and
sum over the atoms.  Using \(Ax={\bf1}-\ell\) and \(Dx=r\) gives

\[
 \sum_Xu_X-u\mathbin\cdot\ell+\phi\mathbin\cdot r\le0.
\tag{3.3}
\]

The leave term satisfies

\[
 u\mathbin\cdot\ell
 \le L\max\{0,\max_Xu_X\}.
\tag{3.4}
\]

Moreover \(r=Dx\) has sum zero on every \(C\)-orbit.  On each orbit we
may subtract the midpoint of the maximum and minimum of \(\phi\) without
changing \(\phi\mathbin\cdot r\).  Hence

\[
 -\phi\mathbin\cdot r
 \le \frac12\operatorname{Osc}_C(\phi)\lVert r\rVert_1
 \le \Delta\operatorname{Osc}_C(\phi).
\tag{3.5}
\]

Equations (3.3)--(3.5) prove (3.2).

For sufficiency, linearize \(r=p-q\) as above, and add nonnegative
slack variables to the two budget inequalities.  Apply the ordinary
equality-form Farkas lemma.  If \(P(L,\Delta)\) is infeasible, there are
free equality multipliers \(y_X,\psi_e\) and nonnegative budget
multipliers \(\sigma,\tau\) such that

\[
\begin{aligned}
 A^{\mathsf T}y+D^{\mathsf T}\psi&\ge0,\\
 y_X+\sigma&\ge0,\\
 -\psi_e+\tau&\ge0,\qquad \psi_e+\tau\ge0,
\end{aligned}
\tag{3.6}
\]

but

\[
                         \sum_Xy_X+L\sigma+2\Delta\tau<0.
\tag{3.7}
\]

Set \(u=-y\) and \(\phi=-\psi\).  The first line of (3.6) becomes
(3.1), while

\[
 \sigma\ge u_{\max}^{+},
 \qquad
 \tau\ge\lVert\phi\rVert_\infty.
\tag{3.8}
\]

Adding an arbitrary constant to \(\phi\) on each \(C\)-orbit does not
change (3.1).  Center each orbit at its midrange.  The smallest possible
global sup norm is exactly

\[
             \frac12\operatorname{Osc}_C(\phi).
\tag{3.9}
\]

Thus (3.7) supplies a violation of (3.2).  Conversely, a violation of
(3.2), after the same centering and with
\(\sigma=u_{\max}^{+}\),
\(\tau=\operatorname{Osc}_C(\phi)/2\), gives (3.6)--(3.7).
This proves equivalence. \(\square\)

### Remark 3.2 (the two support functions are sharp)

The two error terms in (3.2) cannot be decreased.  Indeed

\[
 \sup_{\substack{\ell\ge0\\\|\ell\|_1\le L}}u\mathbin\cdot\ell
 =L u_{\max}^{+}.
\tag{3.10}
\]

Also, if \(V_C\) is the subspace of vectors summing to zero on every
\(C\)-orbit, then

\[
 \sup_{\substack{r\in V_C\\\|r\|_1\le2\Delta}}
       (-\phi\mathbin\cdot r)
 =\Delta\operatorname{Osc}_C(\phi).
\tag{3.11}
\]

For (3.11), put positive mass \(\Delta\) at a minimum point and negative
mass \(\Delta\) at a maximum point of an orbit attaining the largest
oscillation.

## 4. The uniform fractional point

The unlabelled owner degree of the canonical atom catalogue is

\[
 D_{\rm own}=m^2(m+1)(m-1)^3.
\tag{4.1}
\]

Each canonical owner tuple has
\(2((m-1)!)^4\) labelled realizations.  Thus the labelled owner degree
is

\[
 \widehat D
 =2((m-1)!)^4m^2(m+1)(m-1)^3.
\tag{4.2}
\]

### Proposition 4.1 (exact uniform circulation)

The assignment

\[
                         x_\alpha^*=\frac1{\widehat D}
 \qquad(\alpha\in\mathcal A)
\tag{4.3}
\]

satisfies

\[
                         Ax^*={\bf1},
 \qquad
                         Dx^*=0.
\tag{4.4}
\]

Its total atom mass and total source mass are

\[
 \sum_\alpha x_\alpha^*=\frac W6,
 \qquad
 \sum_\alpha3x_\alpha^*=\frac W2.
\tag{4.5}
\]

Every state has the same fractional source load

\[
 \rho=\frac1{2m!(m+1)!}.
\tag{4.6}
\]

#### Proof

Exact owner regularity gives the first equation in (4.4).  A fixed state
is a source of

\[
 d_{\rm state}=(m-1)^3((m-1)!)^2
\tag{4.7}
\]

labelled atoms.  Hence its source load is

\[
 \frac{d_{\rm state}}{\widehat D}
 =\frac1{2m^2(m+1)((m-1)!)^2}
 =\frac1{2m!(m+1)!},
\tag{4.8}
\]

independent of the state.  This constant load is \(C\)-invariant, so
the second equation in (4.4) follows from \(D=(I-C)s\).  Finally each
atom has six owner incidences and three source incidences, giving
(4.5). \(\square\)

### Corollary 4.2 (no fractional dual obstruction)

If \((u,\phi)\) satisfies (3.1), then

\[
                         \boxed{\sum_Xu_X\le0.}
\tag{4.9}
\]

#### Proof

Multiply (3.1) by \(x_\alpha^*\) and sum.  Proposition 4.1 turns the
left side into

\[
 u\mathbin\cdot Ax^*+\phi\mathbin\cdot Dx^*
 =\sum_Xu_X.
\]

It is nonpositive. \(\square\)

Thus every obstruction to the requested rounding is an integer-hull or
quantitative orbit-assembly obstruction.  It cannot be a fractional
Farkas/Hall cut of the atom-column system.

## 5. Exact integral orbit form

Let \(x\) be Boolean and satisfy the owner equations with a leave.
Because two selected atoms cannot share a source owner, their source
states are distinct.  Define

\[
                         S_x=\bigsqcup_{\alpha:x_\alpha=1}I(\alpha).
\tag{5.1}
\]

Then

\[
                         Dx={\bf1}_{S_x}-{\bf1}_{C S_x}.
\tag{5.2}
\]

### Proposition 5.1 (boundary-run identity)

For a \(C\)-orbit \(Q\), let \(r_Q(S_x)\) be the number of cyclic
intervals of \(S_x\cap Q\), with the convention that it is zero when
the intersection is empty or all of \(Q\).  Then

\[
 \boxed{
 \frac12\lVert Dx\rVert_1
 =\sum_{Q\in\mathcal E/\langle C\rangle}r_Q(S_x).}
\tag{5.3}
\]

In particular,

\[
                         Dx=0
 \quad\Longleftrightarrow\quad
 S_x\text{ is a union of full \(C\)-orbits}.
\tag{5.4}
\]

#### Proof

On one orbit, list the states cyclically and write the indicator of
\(S_x\) as a cyclic binary word.  Formula (5.2) is its first cyclic
difference.  Every nonconstant selected interval has one \(+1\) and
one \(-1\) boundary, and there are no other nonzero entries.  Its
half-\(\ell^1\) norm is therefore the number of selected intervals.
Summing over the orbits proves (5.3), and (5.4) follows. \(\square\)

This identity is stronger than the statement that the flow error has
even \(\ell^1\)-norm: it identifies exactly what an \(o(W)\) signed
error means.  It permits only \(o(W)\) cyclic source intervals over all
partially occupied \(BA\)-orbits.

## 6. Divisibility, parity, and prime obstructions

The coordinate permutation \(C=BA\) has one cycle of length \(m\) and
one of length \(m+1\).  Since all state entries are distinct, every
state orbit has length

\[
                         L_C=m(m+1).
\tag{6.1}
\]

Let

\[
 t=\sum_\alpha x_\alpha,
 \qquad
 \ell=\sum_X\ell_X.
\tag{6.2}
\]

Summing the owner equations and counting source states gives

\[
                         6t=W-\ell,
 \qquad
                         |S_x|=3t.
\tag{6.3}
\]

### Theorem 6.1 (exact orbit congruences)

Every Boolean owner packing satisfies

\[
                         \ell\equiv W\pmod6.
\tag{6.4}
\]

If in addition \(Dx=0\), then

\[
                         \ell\equiv W\pmod{2m(m+1)}.
\tag{6.5}
\]

Equivalently,

\[
 W-\ell\equiv0
 \pmod{\operatorname{lcm}(6,,2m(m+1))}.
\tag{6.6}
\]

#### Proof

Equation (6.4) is immediate from the first identity in (6.3).  Under
exact flow, Proposition 5.1 makes \(S_x\) a union of full \(C\)-orbits,
so (6.1) divides \(|S_x|=3t\).  Therefore

\[
                         2m(m+1)\mid6t=W-\ell,
\]

which is (6.5).  Combining the two divisibilities gives (6.6).
\(\square\)

### Corollary 6.2 (an infinite exact-rounding obstruction)

For every prime \(m=p>2\), there is no Boolean atom solution with zero
owner leave and zero signed flow.

#### Proof

In \(\mathbb F_p[x]\),

\[
 (1+x)^{2p+1}
 \equiv(1+x)(1+x^p)^2.
\tag{6.7}
\]

The coefficient of \(x^p\) is therefore \(2\), so

\[
                         W=\binom{2p+1}{p}\equiv2\pmod p.
\tag{6.8}
\]

But (6.5) with \(\ell=0\) requires \(p\mid W\), a contradiction.
\(\square\)

There is also a simple parity family.  If \(m=2^k-1\), adding \(m\)
and \(m+1\) in base two creates no carry.  Hence Lucas' theorem gives

\[
                         \binom{2m+1}{m}\equiv1\pmod2.
\tag{6.9}
\]

Exact owner coverage by six-owner atoms is then impossible even before
flow is imposed.

There is an exact congruence which retains the signed flow rather than
setting it to zero.  Give every \(C\)-orbit an arbitrary cyclic indexing

\[
                         Q=(e_0,e_1,\ldots,e_{L_C-1}),
 \qquad Ce_j=e_{j+1}.
\tag{6.10}
\]

### Proposition 6.3 (flow-moment congruence)

For every Boolean owner packing,

\[
 \boxed{
 W-\ell
 +2\sum_Q\sum_{j=0}^{L_C-1}j(Dx)_{e_j}
 \equiv0\pmod{2L_C}.}
\tag{6.11}
\]

The residue in (6.11) is independent of the chosen origins on the
orbits.  Moreover

\[
 \#\{e:(Dx)_e=1\}
 =\#\{e:(Dx)_e=-1\}
 =\frac12\lVert Dx\rVert_1.
\tag{6.12}
\]

#### Proof

On one orbit put \(s_j={\bf1}_{S_x}(e_j)\).  Formula (5.2) gives

\[
                         (Dx)_{e_j}=s_j-s_{j-1}.
\tag{6.13}
\]

Therefore

\[
 \sum_{j=0}^{L_C-1}j(Dx)_{e_j}
 =-|S_x\cap Q|+L_Cs_{L_C-1}
 \equiv-|S_x\cap Q|\pmod{L_C}.
\tag{6.14}
\]

Sum (6.14) over the orbits, use
\(|S_x|=3t\) and \(W-\ell=6t\), and multiply by two.  This gives
(6.11).  Shifting an orbit origin changes the weighted sum by a
multiple of the orbit sum of \(Dx\), which is zero.  Finally a cyclic
binary word has equally many \(0\)-to-\(1\) and \(1\)-to-\(0\)
boundaries.  Equations (5.2) and (5.3) give (6.12). \(\square\)

Setting \(Dx=0\) in (6.11) recovers (6.5).  Conversely, one nonconstant
cyclic interval can have any length from \(1\) to \(L_C-1\), so its two
boundary entries can change the moment in (6.14) by any nonzero residue
modulo \(L_C\).  Hence the exact mod-\(p\) constraints alone cannot force
more than a constant signed-flow error once nonzero error is allowed.

These are exact integer-hull obstructions, not asymptotic no-go
theorems.  The modulus in (6.6) is at most \(6m(m+1)=O(m^2)\), whereas
\(W\) is exponential in \(m\).  Every residue class consequently has a
nonnegative representative below \(O(m^2)=o(W)\).  Arithmetic alone
therefore leaves open the requested \(o(W)\)-leave rounding.

## 7. Exact surviving statement

The owner-only nibble theorem supplies a Boolean packing with
\(\ell=o(W)\), but it gives no control of (5.3).  The uniform atom point
supplies exact owner balance and exact flow, but is fractional.  The
Farkas theorem proves that no linear fractional cut lies between them.

Consequently the remaining integral theorem is precisely:

> **Orbit-interval atom rounding problem.**  Select an owner-disjoint
> family of canonical nested-star atoms covering \(W-o(W)\) owners such
> that, on all \(BA\)-orbits together, their source phases form only
> \(o(W)\) cyclic intervals.

By Proposition 5.1 this is equivalent, without hidden constants, to

\[
                         \ell=o(W),
 \qquad
                         \frac12\lVert Dx\rVert_1=o(W).
\tag{7.1}
\]

The elementary square and braid commutators do not provide such a
rounding: the former has a nonzero protected divergence and the latter
violates owner transversality.  This agrees with
`MATH_THEOREM_BINARY_ROTOR_PERMUTAHEDRON_COMMUTATOR_NO_GO_20260726.md`.
The present theorem shows more specifically that the needed advance is
an integer orbit-assembly theorem for the atom columns, rather than a
stronger fractional Hall inequality.
