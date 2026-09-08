# Independent fractional tube rounding does not close the integral gate

Date: 2026-09-07. This note concerns one explicitly specified rounding rule,
not arbitrary integral covers and not unrestricted OR words.

The quaternary fractional certificate in
`q4d6_fractional_template_20260906_c52e9.py` has charge 1248. The tube
amplification lemma applies directly to integral templates; substituting
fractional template weights into that lemma requires a new rounding theorem.
The most direct independent lane selection fails by a quantified amount.

## 1. Model and conclusion

Let the fourteen certificate rows be indexed by `i`. Their integer
numerators are `n_i`, their rectangles are `R_i=C_i x D_i`, and their weights
before symmetry development are `n_i/15`. Develop each row under the indexed
group of all six-coordinate permutations and simultaneous reflection. This
group has size `G=1440`; duplicate developed supports remain separate indexed
objects. Each developed object has weight

\[
p_i=\frac{n_i}{21600}<1.
\]

For each developed rectangle, apply the literal tube partition independently
on its two shores. This gives exactly `m^4` fine rectangles covering its
blown-up support in `[4m]^6`, without internal duplication. Select each fine
rectangle independently with probability `p_i`. Let `Q_m` be the selected
principal charge, the sum of the two chain lengths of every selected pair.
Let `Z_m` be the number of missed points on the central fine-grid rank

\[
\{x\in[4m]^6:\ \sum x_j=12m-3\}.
\]

Then, in probability,

\[
\frac{Q_m}{m^5}\longrightarrow1248,
\qquad
\frac{Z_m}{m^5}\longrightarrow
z_*=203.252334552913\ldots.                         \tag{1}
\]

If the selected family is completed by adding any other chain-pair
rectangles on complementary coordinate shores, the final principal charge
is therefore at least

\[
\boxed{(1248+2z_*-o(1))m^5
       =(1654.504669105826\ldots-o(1))m^5}
                                                               \tag{2}
\]

with probability tending to one. The additional rectangles may change
coordinate splits and use arbitrary strict chains. The original integral
1280 template, by comparison, amplifies to charge exactly `1280 m^5`.

Thus independent fractional lane selection followed by additive repair is
not a competitive rounding rule. This does not exclude correlated selection,
rerouting, replacing the selected rectangles, or a different compiler.

## 2. Exact hole probabilities

For a macro point `v in [4]^6`, let `O(v)` denote its orbit under the group
above, and write

\[
N_o=|o|,\qquad c_i(o)=|R_i\cap o|,
\qquad a_i(o)=\frac{1440c_i(o)}{N_o}.
\]

Transitivity shows that `a_i(o)` is an integer: it counts indexed group
elements whose image of `R_i` contains one specified point in `o`.
Every fine point over `v` belongs to exactly one fine rectangle in each
such developed template. Its probability of being missed is consequently

\[
\delta_o=\prod_{i=1}^{14}
\left(1-\frac{n_i}{21600}\right)^{a_i(o)}.             \tag{3}
\]

This probability is independent of the fine point's position within its
macro cell, and of the routing choices used in the tube partitions.

For an integer `r`, put

\[
H_r=\sum_{\substack{v\in[4]^6\\\sum v_j=r}}\delta_{O(v)}.
\]

The exact coefficient in (1) is

\[
\boxed{
z_*=\frac{H_7+26H_8+66H_9+26H_{10}+H_{11}}{120}.}    \tag{4}
\]

All quantities in (3)--(4) are rational. The displayed decimal is only a
convenient rendering; the companion checker certifies `z_*>203.25` using
integer lower bounds, with no floating-point assumption in that inequality.

To prove (4), write a fine point as `mv+y`, where `y in [m]^6`.
Its central-rank constraint becomes

\[
\sum y_j=12m-3-m\sum v_j.
\]

For fixed integer `r`, the number of these fine points in a macro cell of
rank `r`, divided by `m^5`, tends to

\[
f_6(12-r),\qquad
f_6(t)=\frac1{120}\sum_{j=0}^6(-1)^j\binom6j(t-j)_+^5.
\]

This follows directly by inclusion--exclusion for bounded compositions.
At the relevant integer arguments the nonzero values are

\[
f_6(1),\ldots,f_6(5)=\frac1{120}(1,26,66,26,1).
\]

Linearity of expectation now proves `E Z_m=(z_*+o(1))m^5`.
Likewise, the tube charge identity and the fractional certificate give
`E Q_m=1248m^5` exactly.

## 3. Concentration and the repair lower bound

There are `20160m^4` independent Bernoulli decisions. A fine chain on a
shore of `s` coordinates has length at most `s(4m-1)+1`, since it is strict
in the product order. Hence changing one decision changes `Q_m` by at most
`24m`.

A product of two strict chains meets any fixed total-rank layer in at most
the minimum of their lengths: fixing one chain member determines at most
one compatible member of the other chain. Changing one decision therefore
changes `Z_m` by at most `24m` as well. The elementary independent-variable
variance bound gives

\[
\operatorname{Var}Q_m+\operatorname{Var}Z_m=O(m^6).
\]

Dividing by `m^10` and applying Chebyshev proves (1). No independence of
different missed-point indicators is asserted or needed.

Finally, a new chain-pair rectangle with shore lengths `a,b` covers at most
`min(a,b)` of the missing central points and costs `a+b>=2 min(a,b)`.
Summing over all added rectangles shows that their principal charge is at
least `2Z_m`, even if they overlap. This proves (2).

## 4. Scope of the remaining rounding problem

A common informal proposal is to reserve different microscopic color
classes for different fractional template copies. For such an argument to
work without cutting lanes, the color must be constant on every fine
rectangle it may select. There is no universal nonconstant selector of
this kind: the admissible template pool includes products of two parallel
coordinate lines, namely two-dimensional coordinate planes with the other
coordinates fixed. Constancy on all these planes forces constancy along
every coordinate line, hence on the entire microcube.

This observation rules out a universal selector that is invariant under
every possible tube rectangle. It does not rule out a selector adapted to
a much smaller compatible family, nor any other correlated integral lift.

The open task remains an actual coordinated selection or routing theorem;
fractional multiplicities and the tube partition alone do not provide it.
