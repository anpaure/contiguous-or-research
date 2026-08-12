# First drift-coherence cycle in the repaired-ring catalogue

Date: 2026-07-27

Scope: the predictable drift of the high influence moment after the first
column-energy theorem.

**Qualification (2026-07-27).** The \(m^{-2}\) gain below is a
time-zero statement, and at a stopped time it is conditional on the
same dynamically normalized two-column mesh. It is not a consequence
of the one-column influence cap alone. A literal restricted
repaired-ring family violating that implication, the exact starred
generator, and the separate legal resource endpoint are proved in
MATH_THEOREM_STARRED_C4_COIN_ENDPOINT_AND_EDGE_ONLY_WEIGHTED_GATE_20260727.md.
The conclusions below should be read with that qualification.

## 0. Verdict

Let

\[
 a(e)=a_X(e),\qquad b(e,g)=b_X(e,g),qquad
 L=K\Delta_t,qquad d_X=d_t(X).
\tag{0.1}
\]

The first pair-coherence term in the drift of

\[
                         Y_J=\sum_ea(e)^J
\tag{0.2}
\]

is

\[
 \mathcal C_J(X)
 =\sum_{e,g}^{*}a(e)^{J-2}b(e,g)^2.
\tag{0.3}
\]

The star restricts to the disjoint protected/next-edge regime; terms with
\(e\cap g\ne\varnothing\) are already paid by deletion of the protected
index \(e\).

At time zero, and conditionally at any stopped time at which the same
mesh scale holds, put

\[
                    \alpha={A\over d_X}.
\tag{0.4}
\]

Then

\[
 \boxed{
 \sum_{e,g}^{*}b(e,g)^2
 \le C L^2d_X^2\alpha^2,}
\tag{0.5}
\]

and, if \(a(e)\le A\),

\[
 \boxed{
 \mathcal C_J(X)
 \le C L^2d_X^J\alpha^J.}
\tag{0.6}
\]

With reference

\[
                    y_J=Ld_X^J\alpha^{J-1},
\tag{0.7}
\]

the contribution of all leaf--leaf pairs to the normalized drift is at
most

\[
              {\binom J2\mathcal C_J(X)\over Ly_J}
              \le C J^2\alpha.
\tag{0.8}

For \(J=C_0\log m\) and
\(\alpha=O_z((\log m)^{O(1)}/m^2)\), this is \(o(1)\).

The centre--leaf overlap is larger.  Its natural scale is

\[
                         O(\Delta_tY_J),
\tag{0.9}

so after division by the main drift scale \(LY_J=K\Delta_tY_J\), all
\(J\) centre--leaf pairs cost

\[
                          O(J/K)=o(1).
\tag{0.10}

This \(1/m\) term is forced by the one resource shared by a protected
edge and each link row; it is not an error in the estimate.

Thus the first \(4\)-cycle does **not** obstruct self-correcting drift.
It does, however, require the dynamic version of (0.5).  The time-zero
mesh theorem proves (0.5) only initially.  Regeneration of this weighted
\(C_4\) energy is the next level of the hierarchy.

## 1. The unicyclic witness graph

Expand

\[
                  \sum_{e,g}^{*}b(e,g)^2.
\tag{1.1}
\]

It chooses two link options \(f_1,f_2\in\mathcal F_X\), each conflicting
with both protected edges \(e,g\).  Its row--column incidence graph is

\[
                         K_{2,2},
\tag{1.2}
\]

the first unicyclic diagram.  A spanning tree of this diagram would cost
only one transverse factor: with left degree at most \(L\) and right
degree at most \(A=d_X\alpha\), the tree bound is

\[
                         O(L^2d_X^2\alpha).
\tag{1.3}
\]

Closing the fourth incidence of the cycle forces one additional endpoint
gap in the repaired cyclic path.  The disjoint path-mesh estimate with

\[
       j=2,qquad(c_1,c_2)=(1,1),qquad s=2,qquad h=2
\tag{1.4}
\]

gives exactly

\[
 \sum_{e,g}^{*}
 \left(B_X^{(1,1)}(e,g)\right)^2
 \le
 (L)^2d_X^2
 \left({C\,2^4\over m^2u_t^2}\right)^{4-2}.
\tag{1.5}

Since \(b(e,g)\le B_X^{(1,1)}(e,g)\), equation (1.5) is (0.5), after
absorbing the fixed power of \(2\) and the density factor into
\(\alpha\).

This calculation explains the scale: every nonempty protected column has
one free incidence, the two second incidences cost two independent
endpoint factors, and the exponent is \(2\), not \(1\).

Multiplying (0.5) by

\[
                         \max_ea(e)^{J-2}\le A^{J-2}
\]

proves (0.6), and (0.8) follows by substitution.

### Long common path segments

Pairs of link rows which share a long owner segment can have highly
overlapping conflict neighbourhoods.  They do not break (0.5): the
multiplicity-aware endpoint exposure in (1.5) counts such pairs with
their full multiplicity.  A long common segment saves endpoint choices
inside one row pair, but the closing incidence of the disjoint
\(K_{2,2}\) still forces the second transverse endpoint gap.  Thus no
literal long-segment family removes the extra \(m^{-2}\) in (0.5).

The bound is critical in the sense relevant to the hierarchy: it supplies
exactly one additional \(m^{-2}\) factor beyond a spanning-tree count.
No stronger factor is used below.

## 2. Centre--leaf common-neighbourhood term

For current catalogue edges \(p,q\), write

\[
             c(p,q)=
             |\operatorname{Conf}(p)\cap
               \operatorname{Conf}(q)|.
\tag{2.1}
\]

The centre--leaf correction in the union bound for a star configuration
is

\[
 \mathcal P_J(X)
 =\sum_ea(e)^{J-1}\sum_{f\in N_X(e)}c(e,f),
\tag{2.2}
\]

where \(N_X(e)=\{f\in\mathcal F_X:f\sim e\}\).

Let

\[
 M_2(e)=\sum_{f\in N_X(e)}\binom{|e\cap f|}{2}.
\tag{2.3}
\]

Since \(t\le1+\binom t2\) for every integer \(t\ge1\),

\[
 \sum_{f\in N_X(e)}|e\cap f|
 \le a(e)+M_2(e).
\tag{2.4}
\]

The two-witness path-mesh bound gives

\[
                         M_2(e)\le C d_X\alpha^2.
\tag{2.5}
\]

Moreover, by choosing one resource in \(e\) and one in \(f\),

\[
 c(e,f)
 \le
 \Delta_t|e\cap f|
 +\sum_{\substack{v\in e,\ w\in f\\v\ne w}}d_t(v,w).
\tag{2.6}
\]

On the stopped repaired-ring core, the second term in (2.6) is
\(O(\Delta_t)\): there are at most \(K^2\) pairs and the normalized
pair codegree is \(O(m^{-2})\); root pairs are smaller.  Hence

\[
 \sum_{f\in N_X(e)}c(e,f)
 \le C\Delta_t\bigl(a(e)+M_2(e)\bigr).
\tag{2.7}
\]

To sum the \(M_2\)-term, split at \(A/2\), where \(A=d_X\alpha\).
For \(a(e)\ge A/2\), (2.5) gives

\[
                         M_2(e)\le C\alpha a(e).
\tag{2.8}
\]

For \(a(e)<A/2\), use
\(\sum_ea(e)\le d_XL\) to get

\[
\begin{aligned}
 \sum_{a(e)<A/2}a(e)^{J-1}M_2(e)
 &\le Cd_X\alpha^2(A/2)^{J-2}\sum_ea(e)\\
 &\le C\alpha\,2^{-(J-2)}y_J.
\end{aligned}
\tag{2.9}
\]

Equations (2.7)--(2.9) prove, whenever \(Y_J\le Cy_J\),

\[
                         \mathcal P_J(X)\le C\Delta_t y_J.
\tag{2.10}
\]

Multiplying by the \(J\) choices of the leaf and dividing by \(Ly_J\)
gives (0.10).

The order \(\Delta_t y_J\) is unavoidable: every pair \(e\sim f\)
shares at least one resource, and every catalogue edge through that
resource belongs to both conflict neighbourhoods.  Thus the leading
centre--leaf overlap is a forced \(1/K\) correction, whereas the
leaf--leaf cycle is a transverse \(m^{-2}\) correction.

## 3. Drift consequence

Expand \(Y_J\) into star configurations

\[
                         (e;f_1,\ldots,f_J).
\tag{3.1}
\]

Assume the current conflict neighbourhood of every active catalogue edge
has size

\[
                         (1+o(1))L.
\tag{3.2}
\]

The kill set of (3.1) is the union of the conflict neighbourhoods of
\(e,f_1,\ldots,f_J\).  Repeated \(f_i\)'s contribute at most

\[
              O(J^2/A)+O(2^{-J})
\tag{3.3}
\]

of the mass at the upper boundary \(Y_J\asymp y_J\): split at \(A/2\)
as in Section 2, and on the upper half use that the fraction of repeated
ordered \(J\)-tuples is \(O(J^2/a(e))\).

For distinct rows, Bonferroni, (0.8), and (0.10) give average union size

\[
 L\left((J+1)-O(J^2\alpha)-O(J/K)-o(1)\right).
\tag{3.4}
\]

At selection rate \(1/L\), the predictable upper drift of \(Y_J\) is
therefore

\[
 {\mathcal L Y_J\over Y_J}
 \le
 -(J+1)+O(J^2\alpha)+O(J/K)+o(1).
\tag{3.5}

This matches the logarithmic derivative of the product-density reference
\(Ld_X^J\alpha^{J-1}\), up to the same negligible errors.  Consequently
the first coherence cycle and the forced centre--leaf overlap are both
compatible with stopped self-correction.

Equation (3.5) is conditional on the dynamic versions of (0.5), (2.5),
and the pair-codegree/core-degree estimates.  It is an exact consumer of
those estimates, not a proof that they regenerate.

## 4. Compensation-resource analogue

In the compensated-bite process, a compensation coin at a resource
\(v\) deletes every configuration using \(v\).  The analogue of a common
selected-edge column is therefore a common **resource column**.

The coin at \(X\) itself terminates the stopped owner observable and is
part of its reference hazard.  For \(v\ne X\), the number of link rows
through both \(X\) and \(v\) is

\[
                         d_t(X,v).
\tag{4.1}
\]

On the stopped repaired-ring core,

\[
             {d_t(X,v)\over d_X}
             \le O_z\left({1\over m^2}\right)
\tag{4.2}
\]

for owner resources, while root resources have a superpolynomially
smaller ratio.  Thus the tree resource-column moments have the same
\(m^{-2}\) factor as Section 2 of the companion column theorem.

The first resource \(4\)-cycle is two link rows sharing two compensated
resources.  It is bounded by

\[
             \sum_{v,w}d_t(X,v,w)^2,
\tag{4.3}
\]

the literal two-resource version of (0.5), and receives the same extra
endpoint factor.  Forced shared resources (the common \(X\), and the one
witness in every \(e\)--\(f_i\) incidence) contribute only
\(O(J/K)\) to the compensation drift because every compensation coin has
probability \(O(\gamma/K)\).

Therefore compensation introduces no new scale at the first coherence
level.  It does require the dynamic resource analogue of (0.5) and
(2.5); the one-bite compensation calculation does not by itself prove
that regeneration.

## 5. Status

Proved:

1. the first disjoint leaf--leaf coherence diagram is unicyclic;
2. its extra cycle supplies an additional \(m^{-2}\) endpoint factor;
3. its total drift cost is \(O(J^2\alpha)\);
4. the forced centre--leaf overlap costs \(O(J/m)\); and
5. the compensation-resource analogue has the same two scales.

Still open:

\[
\boxed{
 \text{dynamic regeneration of the }C_4\text{ and two-witness
 multiplicity energies after previous restrictions.}
}
\]

Thus truncation plus the tree column theorem passes the first cyclic
test, but it has not yet removed the need for a finite coherence
hierarchy.
