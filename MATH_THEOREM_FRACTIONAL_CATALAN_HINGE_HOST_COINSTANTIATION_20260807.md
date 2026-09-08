# Exact fractional coinstantiation of the Catalan hinge bank, host, and palette

**Date:** 2026-08-07  
**Method:** uniform averaging over the complete hinge catalogue  
**Status:** unconditional fractional theorem for every `m>=3`.  It proves
that omission, private-hinge resource capacities, the residual degree-two
host, and intersection-colour coverage have one simultaneous fractional
point.  It does not round that point or impose one Hamilton component.

## 1. Catalogue and variables

Use the setting and ordered hinge catalogue of
`MATH_THEOREM_CATALAN_PRIVATE_HINGE_BANK_AND_LINEAR_RESIDUAL_DEGREE_20260807.md`.
Thus

\[
 |\Omega|=2m,qquad
 W={2m\choose m},qquad C={W\over m+1},qquad
 V={2m\choose m-1}=mC,
\]

and every omitted rank-`m` set has

\[
                         g=m^2(m-1)^2
\]

ordered hinges.  Give every catalogue member `gamma` weight

\[
                         z_\gamma={1\over(m+1)g}.     \tag{1.1}
\]

The total hinge mass is

\[
                         Wg z_\gamma={W\over m+1}=C. \tag{1.2}
\]

For a rank-`m` set `U`, let `o_U` be the total weight of candidates in
which `U` has the omitted role.  For an incidence edge `e` between ranks
`m-1` and `m`, let `p_e` be the total weight of hinge paths using `e`.

## 2. Exact uniform marginals

For every `U`, its `g` candidates give

\[
                         o_U={1\over m+1}.            \tag{2.1}
\]

The symmetric group on `Omega` is transitive on the incidence edges.  The
catalogue has total hinge-edge mass `4C`, while the incidence graph has

\[
                         V(m+1)=mC(m+1)
\]

edges.  Therefore

\[
                         p_e={4\over m(m+1)}          \tag{2.2}
\]

for every incidence edge `e`.

The exact role loads from the catalogue census are:

\[
 \begin{array}{c|c}
 \text{resource}&\text{total hinge weight}\ \hline
 \text{fixed rank-`m` set, one specified role}
   &1/(m+1)\\
 \text{fixed rank-`(m-1)` set, one specified role}
   &1/m\\
 \text{fixed rank-`(m-2)` hinge colour}
   &(m+2)/(m(m-1)).
 \end{array}                                           \tag{2.3}
\]

Thus the combined three-role loads are `3/(m+1)` on rank `m` and
`3/m` on rank `m-1`, both at most one for `m>=3`; the colour load is also
at most one.  Hence all private-resource packing rows are fractionally
feasible at once.

The omission load at every rank-`(m-1)` facet is exactly one:

\[
 \sum_{U\supset B}o_U={m+1\over m+1}=1.              \tag{2.4}
\]

So the fractional residual incidence degree is exactly `m` at every
facet.

## 3. One residual diamond current closes degree and palette rows

A Boolean diamond is a pair

\[
 (a,U),\qquad a\in{\Omega\choose m-2},\quad
 U\in{\Omega\choose m},\quad a\subset U.             \tag{3.1}
\]

It selects the Johnson edge between the two rank-`(m-1)` facets of `U`
which contain `a`.  There are `binom(m,2)` diamonds below every `U`, and
`binom(m+2,2)` above every `a`.

Every hinge contains two selected diamonds, both with its private colour
`a`.  By symmetry, their fractional load on any fixed diamond is

\[
 h_{a,U}={2C\over W{m\choose2}}
 ={4\over m(m-1)(m+1)}.                              \tag{3.2}
\]

Put the constant residual diamond weight

\[
 r_{a,U}={2(m-2)\over m(m-1)(m+1)}                  \tag{3.3}
\]

on every diamond.  The total diamond weight is therefore

\[
 w_{a,U}=h_{a,U}+r_{a,U}
 ={2\over(m-1)(m+1)}.                               \tag{3.4}
\]

At a rank-`m` set `U`,

\[
 {m\choose2}w_{a,U}={m\over m+1}=1-o_U.             \tag{3.5}
\]

Thus exactly one diamond is selected in the fraction in which `U` is not
omitted.

A fixed rank-`(m-1)` facet belongs to `(m+1)(m-1)` diamonds: choose its
rank-`m` extension and then the other deleted element.  Hence its degree is

\[
 (m+1)(m-1)w_{a,U}=2.                               \tag{3.6}
\]

Finally every intersection colour receives load

\[
 {m+2\choose2}w_{a,U}={m+2\over m-1}>1.             \tag{3.7}
\]

Thus all intersection colours are fractionally covered with the exact
global repeat surplus.

## 4. Incidence-current projection

Project the diamond current to the two incidence edges of each diamond.
The hinge part gives the load (2.2).  A fixed incidence edge belongs to
`m-1` diamonds, so the residual projection has the constant weight

\[
                         y_e={2(m-2)\over m(m+1)}     \tag{4.1}
\]

on every incidence edge.

At a rank-`(m-1)` vertex, the hinge catalogue contributes degree `4/m`:
central-role mass `1/m` has hinge degree two, and the two outer-role masses
`1/m` have degree one.  The residual current contributes

\[
                         (m+1)y_e={2(m-2)\over m}.
\]

Their sum is exactly two.

At a rank-`m` vertex, the two visited roles each have weight `1/(m+1)`
and hinge degree two, for total hinge degree `4/(m+1)`.  The residual
current contributes

\[
                         my_e={2(m-2)\over m+1}.
\]

The sum is

\[
                         {2m\over m+1}=2(1-o_U),      \tag{4.2}
\]

which is exactly degree two times the fraction in which `U` is not
omitted.

Finally every physical incidence edge respects its availability capacity:

\[
 p_e+y_e
 ={4+2(m-2)\over m(m+1)}
 ={2\over m+1}
 \le {m\over m+1}=1-o_U.                            \tag{4.3}
\]

Thus the omitted-colour choice, all private-hinge roles, and a degree-two
residual host share one literal fractional solution.

## 5. Consequence and scope

There is no fractional separator involving only:

* total Catalan omission mass;
* the seven private hinge resources;
* facet/upper degree balance;
* physical incidence-edge capacity; or
* the residual degree-two factor equations; and
* fractional coverage of every intersection colour.

Any obstruction to the protected hinge host must therefore use an
integral correlation or connectedness/subtour constraint.  The theorem
does not prove an integral two-factor, a Hamilton cycle, an integral
palette-safe cycle, the exterior forest,
residence, deeper upper coverage, or a compiler.
