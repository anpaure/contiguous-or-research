# Audit of the PBBS pentagon common-history and companion theorem

**Date:** 2026-08-05  
**Method:** independent line-by-line symbolic audit against the PBBS exchange
test, common-history interval proof, gap-potential rule, and reflected
anti-conjugacy theorem; no computation or search  
**Audited file:**
`MATH_THEOREM_PBBS_PENTAGON_THREE_SCREEN_COMMON_HISTORY_AND_UPPER_CURRENT_GATE_20260805.md`

## 1. Verdict

The theorem is **PASS at its stated conditional scope**.

The substantive new implication is

\[
 \text{prospectively planted three-screen histories}
 \Longrightarrow
 \lambda_{\rm lower}^{\rm terminal}=0.                    \tag{1.1}
\]

It does **not** prove

\[
 \min_{\mathcal M}e_H(\mathcal M)=0,                      \tag{1.2}
\]

because `e_H` is the raw number of old matched cells crossing deleted
edges.  Instead it proves that every such old cell has a named transported
replacement.  This distinction is explicit in the theorem and is
load-bearing.

The companion audit is negative:

* rotation only conjugates the upper current;
* complement sends upper OR to lower intersection on the opposite shore;
* value-preserving complete reflection cancels the current but
  anti-conjugates the successor permutation and preserves cycle type;
* a second value-identical reflected copy repeats owner sets, while a
  nontrivial relabelling cancels only up to that relabelling.

Thus no canonical phase/complement companion simultaneously supplies exact
all-width cancellation, owner-once simplicity, and topology gain.

## 2. Head-ring normal form audit

For one directed exchange arrow `Z_i -> Z_(i+1)`, the old lower incidence is

\[
 \ell_i=f(Z_i)=Q_i-\{p_+(Z_i)\}.
\]

The exchange test says exactly `ell_i subset Q_(i+1)`.  Since both owners
have rank `R`,

\[
 \ell_i=Q_i\cap Q_{i+1}.
\]

Holding `M_0` fixed gives the old/new contracted edges

\[
 P_iQ_i\longleftrightarrow P_iQ_{i+1}.
\]

For the height pentagon, every `Q_i` contains

\[
 G_h=[n]\setminus(L_h\cup\{z_0,z_1,c,a,z_2\}),
 \qquad |G_h|=R-3.
\]

The table of forward survivors lies in the displayed five-set, so `ell_i`
and therefore `P_i` also contain `G_h`.  The screen ranks are exactly three.
No assumption about the uncomputed extra coordinate of `P_i` is made.

**Verdict:** PASS.

## 3. Interval-cell transport audit

With `G_h=C_1 dotcup ... dotcup C_d`, the two length-`d+1` windows in

\[
 (X_i,C_1,\ldots,C_d,Y_i)
\]

are `P_i=G_h+X_i` and `Q_i=G_h+Y_i`.  Any source interval meeting both
screens contains `P_i` and has rank at least `R`.  Hence a strict-lower
interval meets at most one screen.  Left cells are fixed; right cells move
with the complete head context; history-only cells are fixed.  These cases
give a literal value-, width-, and occurrence-bijection.

This proof does not require screen rank two, pairwise-disjoint screen
labels, q2 neutrality, or an upper-palette identity.

The hypothesis that all histories and moved contexts coexist in one source
antecedent is not derived from disjoint exchange vertices.  It remains
explicit.

**Verdict:** PASS, conditional on prospective source realization.

## 4. Gap-selected cut audit

For

\[
 Z_h^1=0_\rho1^s0^s(10)^{r-s},\qquad s=h+1,
\]

delete the last up-step `p` of the first mountain.  The later unit factors
cancel in both directions.  The forward survivors of the q1 core are

\[
 \rho,v_{s-1},v_s,
\]

and the reverse survivors are

\[
 p,v_1,v_2.
\]

The expanded `C,A` convention gives gap counts `(0,0,3)`, hence potential
values `(0,-1,-2)`.  The unique selected boundary is

\[
 K+p\longrightarrow K+\rho,
\]

the outgoing edge at `Z_h^1`.  One such deleted edge occurs for every
`h=2,...,H-1`.

The statement about the ordinary source compiler additionally invokes the
maximal-antecedent row identity and therefore belongs to the same
`d`-resident source-realization face as Section 3.

**Verdict:** PASS.

## 5. Upper-current and counterexample audit

Cutting at the five old edges leaves directed arcs.  Old one-cut intervals
have diagonal exterior pairing `A_i(u) union B_i(v)`; the head rethread has
the shifted pairing `A_i(u) union B_(i+1)(v)`.  Arc-internal intervals are
fixed.  Multi-cut intervals require the complete intervening-arc tensor and
cannot be dropped without a shield theorem.  This is exact reassembly
bookkeeping.

For the arbitrary-exterior counterexample, the five tail screens use at
most five coordinates of `L_h`; for sufficiently large `r`, five unused
coordinates remain for private markers.  Distinct old/new owners above the
same facet have different extra coordinates, so the privately marked full
fragment values differ.  The argument is deliberately only a
context-free-theorem obstruction, not a claim about canonical PBBS holes.

**Verdict:** PASS at the stated scope.

## 6. Companion audit

The rotation identity is equivariance.  De Morgan duality proves the
complement boundary.  For a complete typed reflection `eta`, the terminal
successor relation is

\[
 s^\dagger=\eta s^{-1}\eta.
\]

Every old cycle is therefore paired with its reversed cycle of the same
length.  All cyclic interval values transport, but component cycle type is
unchanged.  Since width-one occurrences are part of the complete state, a
literal value-preserving reflected copy repeats the same owner sets and
cannot be occurrence-disjoint in an owner-once factor.

This no-go applies only to bijective two-copy cancellation with no external
witness reservoir.  It does not exclude a PBBS-specific alternative
corridor, a non-bijective absorber, a globally accepted coordinate twist,
or a larger packet whose upper support is supplied elsewhere.

**Verdict:** PASS.

## 7. Exact surviving lemma

After the new reduction the PBBS ladder needs:

1. prospective simultaneous planting of the rank-three histories;
2. a biresident seam realization;
3. a typed-cap map extending the cell bijections; and
4. a PBBS-specific alternative-witness or non-bijective circulation making
   all but `O(1)` negative exterior targets of the complete upper tensor
   survive.

The first and fourth rows are not consequences of the current canonical
PBBS factor.  The theorem removes the lower compiler cut-avoidance row but
does not prove `B(k)+O(1)`.
