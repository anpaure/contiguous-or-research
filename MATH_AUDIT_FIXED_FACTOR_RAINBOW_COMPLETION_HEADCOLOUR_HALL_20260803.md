# Audit of the fixed-factor rainbow-completion min-max

**Date:** 2026-08-03  
**Status:** independent symbolic audit; PASS.  No computation is used.

The audited theorem is

```text
1a81158093019185be41d12012c5ae4287e971dc07119ddfe819107f7b6a25ed
  MATH_THEOREM_FIXED_FACTOR_RAINBOW_COMPLETION_HEADCOLOUR_HALL_AND_NONMATROID_GATE_20260803.md
```

## 1. Base-master criterion

A selected column `(T,R)` records a fixed head and colour, with predecessor
fibre

\[
                         P(T,R)=\{S:ST\in E_R\}.
\]

If a column set `D` uses every colour once and every head at most once, a
matching from `D` to its predecessor tails is exactly a rainbow base: the
column matching gives distinct heads and colours, while the predecessor
matching gives distinct tails.

Hall on the column shore is

\[
              \left|\bigcup_{a\in D'}P(a)\right|\ge|D'|
                         \qquad(D'\subseteq D).          \tag{1.1}
\]

For a tail set `X`, define `B_X={a:P(a) subseteq X}`.  If (1.1) fails, put
`X=union_(a in D')P(a)`; then `D' subseteq D cap B_X`, so
`|D cap B_X|>|X|`.  Conversely, `|D cap B_X|>|X|` itself violates Hall.
Thus the upper-cut form

\[
                         |D\cap B_X|\le|X|              \tag{1.2}
\]

is exactly equivalent.  This verifies Theorem 1.1.

## 2. Fixed-base residual formula

After a rainbow base `Q` is removed, both residual vertex shores have size
`C`.  A head-colour partial matching `J` has distinct residual heads and
distinct colours.  Join a residual tail `S` to `(T,R) in J` precisely when
`ST` is a residual edge of colour `R`.

A matching in this tail-to-column graph is exactly a residual rainbow
matching: its three coordinates are the matched tail, the head stored by the
column, and the colour stored by the column.  Conversely every residual
rainbow matching produces such a column matching.

For fixed `J`, defect Hall gives

\[
 \nu_J=C-\max_{X\subseteq L_Q}
       \bigl(|X|-|N_J(X)|\bigr).                         \tag{2.1}
\]

The maximum is nonnegative because `X=emptyset` is allowed.  Maximizing
`nu_J` over all head-colour matchings `J`, then subtracting from `C`, gives
exactly

\[
 C-\nu_{\rm rb}(H-V(Q))
 =\min_J\max_X\bigl(|X|-|N_J(X)|\bigr).                 \tag{2.2}
\]

At `X=L_Q`, the inner inequality `|N_J(X)|>=|X|` forces `|J|=C`; hence a
zero-defect `J` automatically covers every residual head and uses `C`
distinct colours.  This verifies both the min-max formula and the exact
all-subset completion criterion.

## 3. Combination with the rainbow decomposition

The previously audited decomposition says that a cap-two perfect matching
is exactly a disjoint union

\[
                              F=Q\mathbin{\dot\cup}P,
\]

where `Q` is one-per-colour rainbow and `P` is a rainbow perfect matching
of the residual shores.  Section 1 characterizes `Q`, and Section 2
characterizes `P` after `Q`.  Therefore the nested existential/all-subset
criterion in equation (0.8) of the theorem is necessary and sufficient.

## 4. Matroid boundary

On the residual head-colour column ground set:

* tail liftability is a transversal matroid, with the standard rank formula
  displayed in the theorem;
* distinct heads form a partition matroid;
* distinct colours form a second partition matroid.

Thus residual rainbow matching is exactly common independence in three
matroids.  Fixing the head-colour matching leaves one ordinary transversal-
matroid Hall problem.  Without that fixing, ordinary two-matroid
intersection does not apply.

The three-edge witness

\[
 (s_0,t_0,a),\qquad(s_0,t_1,b),\qquad(s_1,t_0,c)
\]

is an exact augmentation failure: `{a}` and `{b,c}` are rainbow-matchable,
but neither `{a,b}` nor `{a,c}` is.  Hence the colour-task independence
system is not a matroid in general.

The even-parity four-atom witness has two permutation-functional colour
classes and perfect two-coordinate projections but no rainbow perfect
matching.  Its two possible head-colour masters fail the tail Hall cut on
opposite singleton fibres.  Both examples are correctly scoped as abstract
functional systems, not Boolean fixed-factor counterexamples.

## 5. Boolean specialization

For an upper colour `R`, with facets `S_b=R-{b}`, the contracted colour map
is

\[
                         S_b\longmapsto S_{p_R(b)}.
\]

Therefore the predecessor fibre of column `(S_c,R)` is exactly

\[
                         \{S_b:p_R(b)=c\}.              \tag{5.1}
\]

Restricting (5.1) to unused tails gives the residual fibres.  The all-subset
conditions are therefore literal statements about the globally correlated
Boolean maps `p_R`; no abstract occurrence relation is hidden.

The audit does not prove those cuts hold for any all-parameter Boolean
factor.  It verifies the exact frontier:

\[
 \boxed{
 \text{choose a base head-colour master and tail Hall lift, then choose a
 residual head-colour master satisfying residual tail Hall}.}
\]

Functionality and pairwise marginal Hall do not prove either joint choice.
