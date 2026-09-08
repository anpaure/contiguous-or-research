# Self-audit of the odd adjacent-depth capacity-`D` absorber

**Date:** 2026-08-05  
**Method:** independent algebraic re-derivation; no computation or search  
**Audited file:**
`MATH_THEOREM_ODD_ADJACENT_DEPTH_CAPACITY_D_ABSORBER_20260805.md`

## 1. Socket indices

In `B_(2r-1)`, an SCD has `H_s=C_s-C_(s-1)` chains born at rank `s`, for
`s<=r-1`, and none born at rank `r`.  At old bottom `t=r-D`, a chain born
at `t+g` uses ranks `t+g,...,r-1`, namely `D-g` lower targets, leaving
capacity `g`.  Therefore `g<=D-1` and

\[
 \sum_{g=q}^{D-1}H_{t+g}=C_{r-1}-C_{t+q-1}.
\]

At new bottom `b=t-1`, the same calculation gives capacities `g<=D` and

\[
 \sum_{g=q}^{D}H_{b+g}=C_{r-1}-C_{b+q-1}.
\]

Subtracting gives `H_(t+q-1)`.  At `q=D`, this is `H_(r-1)`, and

\[
 H_{r-1}=C_{r-1}\left(1-{r-1\over r+1}\right)
 ={2W\over r+1}.
\]

PASS.

## 2. Exceptional size and capacity

The old row `K_D=0` forces every positive configuration to have zero
`D`-tail.  It is therefore a zero row on the positive support, leaving at
most `D-1` independent aggregate rows and hence at most `D-1` fractional
whole jobs at an extreme point.  Using `D` is safe.

Terminal deletion removes the old top singleton jobs and shortens every
other job once.  Every descendant is then fragmented into pieces of length
at most `D`; no exceptional piece needs capacity `D+1`.  Since
`L_max<=t-2`,

\[
 D\lceil L_{\max}/D\rceil<L_{\max}+D\le r-2<r.
\]

PASS.

## 3. Reserve inequalities

Removing `h` exact capacity-`D` occurrences subtracts `h` from every tail
`q<=D`.  Removing `Delta_g` exact capacity-`g` occurrences subtracts
`sum_(g>=q)Delta_g`.  The new-minus-old margin at exactly that tail is
`H_(t+q-1)`.  Hence (3.2) is precisely the finite sorted-tail sufficient
condition, including the last row `h+Delta_D<=H_(r-1)`.  PASS.

## 4. Named containment degree

Every fragment top has rank at most `b-1`; a capacity-`g` socket begins at
rank `u_g=b+g`.  The minimum number of containing starts is therefore

\[
 {2r-1-(b-1)\choose (b+g)-(b-1)}
 ={2r-b\choose g+1}=d_g.
\]

The MLD marks are fixed before path realization.  The final matching chooses
names only afterward, so no adaptive-colour quantifier is reversed.  A
perfect matching between the equal middle levels completes every selected
rank-`r-1` start to a distinct rank-`r` owner.  PASS.

## 5. Asymptotic reserve

For `u<=r-1`,

\[
 H_u={2(r-u)\over2r-u}{2r-1\choose u}.
\]

On the `Theta(sqrt(r))` collar this is at least
`H_(r-1)=2W/(r+1)`.  The first spread reserve has order
`Wr^(-3/4)`, whereas `H_t` has order `Wr^(-1/2)`, and the binomial
containment-degree ratio makes subsequent reserve terms geometrically
smaller relative to their corresponding margins.  Thus the reserve is
`o(H)` uniformly, while `h=O(r)`.  PASS.

## 6. Implication scope

The result is conditional on the odd residual all-price configuration LP.
It does not include an independently priced endpoint/Ferrers bank.  It
constructs an occurrence-labelled Boolean collar forest, not one physical
upper-complete resident OR word.  Therefore its valid conclusion is the
conditional odd `B+1` reduction, not an unconditional `B+1`, `B+O(1)`, or
coefficient-one theorem.  PASS.

