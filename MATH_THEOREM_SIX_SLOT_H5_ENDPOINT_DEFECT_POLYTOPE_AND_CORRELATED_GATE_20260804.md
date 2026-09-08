# Six-slot `h=5`: endpoint-defect polytope and a closed correlated gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It derives the
exact physical shift geometry of the canonical six-generator,
seven-entry `h=5` branch and reduces every inert endpoint face to one
closed correlated gate.  The geometry is not the `h=4` additive
rectangle: it is two deficient complementary pairs and one deficient
midpoint, coupled by one endpoint-minimum condition and four internal
superadditivity inequalities.  The resulting gate is not signed here, so
complete `h=5` positivity is not claimed.  No search or sampled
computation is used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
 \qquad
 C(\tau)=F_\tau(0).
\tag{0.1}
\]

Let

\[
 (c_0,c_1,\ldots,c_6),\qquad c_0=0,
\tag{0.2}
\]

be a canonical first-crossing, endpoint-saturated table assigned to the
least maximum-density branch `h=5`.  Write

\[
                         P=c_5=5a,
 \qquad
                         \tau=c_6.
\tag{0.3}
\]

### Lemma 0.1 (threshold face)

If `tau=A`, then

\[
                         \Phi>{163\over70000}>0.
\tag{0.4}
\]

#### Proof

The literal endpoint-period comparison gives

\[
 \Phi\ge C(A)+\sum_{i=1}^{5}F_A(c_i).
\tag{0.5}
\]

Endpoint superadditivity gives

\[
 c_1+c_5\le A,
 \qquad c_2+c_4\le A,
 \qquad 2c_3\le A.
\tag{0.6}
\]

The table is nondecreasing, so the frozen subcomplementary-pair bound
applies to `(c_1,c_5)` and `(c_2,c_4)`, while the frozen half-band bound
gives `F_A(c_3)>0`.  Together with `C(A)>43/1000`, this yields

\[
 \Phi>{43\over1000}-2{8541\over420000}
      ={163\over70000}>0.
\]

No maximum-density assumption is used in this threshold argument.
\(\square\)

Henceforth we work on an inert face, so `tau>A`.

## 1. Density-defect coordinates

Define

\[
\boxed{
\begin{aligned}
 q_1&=6a-\tau,\\
 r&=a-c_1,\\
 q_2&=2a-c_2,\\
 q_3&=3a-c_3,\\
 q_4&=4a-c_4.
\end{aligned}}
\tag{1.1}
\]

Maximum density, first crossing, and endpoint superadditivity give

\[
\boxed{
\begin{gathered}
 A<\tau<{6A\over5},
 \qquad
 {\tau\over6}\le a<{A\over5},\\
 0\le q_1\le a,
 \quad0\le r\le a,
 \quad0\le q_2\le2a,
 \quad0\le q_3\le3a,
 \quad0\le q_4\le4a.
\end{gathered}}
\tag{1.2}
\]

For the literal least-maximizer `h=5` stratum, `r,q_2,q_3,q_4` are
strictly positive.  Passing also from `a<A/5` to `a<=A/5` and allowing
these four defects to vanish gives a compact closure.  Enlarging to that
closure is useful for a sufficient gate.

Indeed, maximum density gives `tau<=6a` and
`c_j<=ja` for `j=2,3,4`.  Internal superadditivity gives
`c_1<=c_2/2<=a`.  First crossing gives `5a=c_5<A`, while endpoint
superadditivity gives `tau>=c_5=5a`.  These are exactly the bounds in
(1.2).  If any of `q_2,q_3,q_4` vanished, then a size smaller than five
would attain the maximum density, contrary to the least-maximizer rule.
Finally, `q_2<=2r` below then makes `r` strictly positive as well.

### Lemma 1.1 (internal physical polytope)

Internal superadditivity is equivalent to

\[
\boxed{
 q_2\le2r,
 \qquad
 q_3\le r+q_2,
 \qquad
 q_4\le r+q_3,
 \qquad
 q_4\le2q_2.}
\tag{1.3}

The remaining two inequalities at capacity five are automatic from
nonnegativity of the defects.

#### Proof

Substitute (1.1) into

\[
 c_2\ge2c_1,
 \quad
 c_3\ge c_1+c_2,
 \quad
 c_4\ge c_1+c_3,
 \quad
 c_4\ge2c_2.
\]

They become exactly (1.3).  Moreover

\[
 P-(c_1+c_4)=r+q_4\ge0,
 \qquad
 P-(c_2+c_3)=q_2+q_3\ge0,
\]

so no further capacity-five row remains. \(\square\)

## 2. Three endpoint defects

Define

\[
\boxed{
 \alpha=r-q_1,
 \qquad
 \beta=q_2+q_4-q_1,
 \qquad
 \gamma=2q_3-q_1.}
\tag{2.1}
\]

### Lemma 2.1 (exact endpoint geometry)

Endpoint superadditivity and saturation are equivalent to

\[
\boxed{
 \alpha,\beta,\gamma\ge0,
 \qquad
 \min\{\alpha,\beta,\gamma\}=0.}
\tag{2.2}

The three zero-defect faces are exactly

\[
\begin{array}{c|c|c}
\text{face}&\text{defect equality}&\text{endpoint equality}\\ \hline
\mathrm X&\alpha=0&c_6=c_1+c_5,\\
\mathrm Y&\beta=0&c_6=c_2+c_4,\\
\mathrm Z&\gamma=0&c_6=2c_3.
\end{array}
\tag{2.3}

#### Proof

The three endpoint deficits are literally

\[
\begin{aligned}
 \tau-(c_1+c_5)
 &=(6a-q_1)-\{(a-r)+5a\}=r-q_1=\alpha,\\
 \tau-(c_2+c_4)
 &=(6a-q_1)-\{(2a-q_2)+(4a-q_4)\}=\beta,\\
 \tau-2c_3
 &=(6a-q_1)-2(3a-q_3)=\gamma.
\end{aligned}
\tag{2.4}

Superadditivity gives nonnegativity.  Since `tau>A`, endpoint saturation

\[
 \tau=\max\{A,c_1+c_5,c_2+c_4,2c_3\}
\]

forces at least one of the three deficits to vanish.  The converse is
immediate. \(\square\)

Thus the inert endpoint set is one correlated union of three faces, not
three independent pair minima.

## 3. Exact physical shifts

For `d>=0`, define the deficient complementary-pair train

\[
 \boxed{
 J_\tau(s,d)=F_\tau(s)+F_\tau(\tau-d-s).}
\tag{3.1}

The density-defect coordinates give

\[
\begin{aligned}
 c_1&=a-r,
 &c_5&=5a=\tau-\alpha-c_1,\\
 c_2&=2a-q_2,
 &c_4&=4a-q_4=\tau-\beta-c_2,\\
 c_3&=3a-q_3={\tau-\gamma\over2}.
\end{aligned}
\tag{3.2}

Consequently the literal endpoint-period expression is exactly

\[
\boxed{
\begin{aligned}
 \mathscr E_5={}&C(\tau)
 +J_\tau(a-r,\alpha)
 +J_\tau(2a-q_2,\beta)\\
 &+F_\tau\left({\tau-\gamma\over2}\right).
\end{aligned}}
\tag{3.3}

This is the true `h=5` analogue of the `h=4` correlated gate:

* pair one has total shift `tau-alpha`;
* pair two has total shift `tau-beta`;
* the midpoint is displaced from `tau/2` by `gamma/2`;
* at least one of the three displacements is zero;
* all three share the same physical defects constrained by (1.3).

There is no additive four-point rectangle.

## 4. Literal endpoint-period comparison

### Lemma 4.1

Every inert canonical `h=5` table satisfies

\[
                         \boxed{\Phi\ge\mathscr E_5.}
\tag{4.1}
\]

#### Proof

At capacity `6q+j`, use `q` copies of the endpoint configuration of
capacity six and one size-`j` generator.  The candidate value is

\[
                         q\tau+c_j.
\]

For `q=0`, internal superadditivity gives `V_j=c_j`.  For `q>=1`, both
the candidate and the Bellman optimum lie in `[A,infinity)`, where `K` is
increasing.  Hence

\[
                         K(V_{6q+j})\ge K(q\tau+c_j).
\]

Sum over `j=0,...,5` and `q>=0`, then use (3.2).  This gives (4.1).
\(\square\)

On each inert face the endpoint generator is also literally redundant:
replace it by `(1,5)`, `(2,4)`, or `(3,3)` according to (2.3).  Thus the
comparison is compatible with the delayed five-generator interpretation
of this branch; it does not rely on a fictitious endpoint symbol.

## 5. The closed correlated gate before analytic minimization

For fixed `tau` with `A<tau<6A/5`, let
`overline P_5(tau)` be the set of

\[
                         (a,r,q_2,q_3,q_4)
\]

satisfying the closed version of (1.2), namely

\[
 {\tau\over6}\le a\le {A\over5},
\tag{5.1}
\]

together with every other weak inequality in (1.2)--(1.3), with

\[
                         q_1=6a-\tau,
\]

and satisfying (2.2).  This is a compact semialgebraic set containing
the image of every literal physical `h=5` table.  Define

\[
\boxed{
 \mathfrak R_5(\tau)
 =\inf_{(a,r,q_2,q_3,q_4)\in\overline{\mathcal P}_5(\tau)}
 \mathscr E_5.}
\tag{5.2}

Equivalently, split `overline P_5(tau)` into the three generically
four-dimensional faces
`alpha=0`, `beta=0`, and `gamma=0`, retaining their intersections.
The variable `q_1` is determined by `(tau,a)`, and one endpoint equality
removes one of the remaining five scalar degrees.  No pair split is
minimized independently.

### Theorem 5.1 (complete `h=5` correlated reduction)

Every canonical inert `h=5` table satisfies

\[
                         \boxed{\Phi\ge\mathfrak R_5(\tau).}
\tag{5.3}

Consequently the complete inert branch is positive if

\[
 \boxed{
 \mathfrak R_5(\tau)>0
 \qquad(A<\tau<6A/5).}
\tag{5.4}

Conversely, a nonpositive physical table gives a point of its own exact
face with \(\mathscr E_5\le0\), and hence forces
\(\mathfrak R_5(\tau)\le0\).  The reverse implication is not asserted,
because the closed gate deliberately includes boundary points from the
adjacent strata.

#### Proof

The physical table maps into `overline P_5(tau)` by Lemmas 1.1 and 2.1.
Lemma
4.1 then gives

\[
 \Phi\ge\mathscr E_5\ge\mathfrak R_5(\tau).
\]

The remaining assertions are immediate. \(\square\)

The gate (5.2) bypasses the thirteen stabilized Apéry forms and their
finite availability head: on inert endpoint faces, the literal
endpoint-period chronology is already available.  The thirteen-form
theorem remains useful for analytic refinements and the strict threshold
chamber, but it is not needed to state the exact correlated physical
gate.

## 6. Exact scope

This theorem proves:

1. the exact five-variable density-defect description of the physical
   stratum at fixed endpoint period, together with its explicit compact
   closure;
2. the exact two-pair/one-midpoint shift decomposition;
3. the exact identification of the three inert endpoint faces;
4. one generically four-dimensional correlated gate on each face;
5. a literal lower comparison with no availability correction.

It does not sign \(\mathfrak R_5\), prove complete six-slot `h=5`
positivity, extend the result to larger generator tables, or prove an
OR-word upper bound.

## 7. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| canonical six-slot/least-density branch | `MATH_THEOREM_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md` | `3b537980a6f18aae936979335cc6756079ff10b92a80019acf3a97df8be9bede` |
| thirteen-form `h=5` reduction | `MATH_THEOREM_SIX_SLOT_H5_RESIDUE_DOMINANCE_17_FORM_AND_HEAD_DICHOTOMY_20260804.md` | `b6a98dbf45f239f68f934ac0c14318ff8f5faa6b69d78cbad7796b46ee283024` |
| endpoint threshold closure | `MATH_THEOREM_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_20260804.md` | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |
