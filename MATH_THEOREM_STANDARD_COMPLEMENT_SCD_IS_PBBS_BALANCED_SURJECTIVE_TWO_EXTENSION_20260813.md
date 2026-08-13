# The standard/complement SCD central factor is exactly the PBBS balanced-surjective two-extension

**Date:** 2026-08-13  
**Status:** unconditional all-parameter identification.  It closes the
owner/lower/upper **support** rows for the odd central three-layer factor.
It does not linearize or Hamiltonize the factor, impose long residence, or
provide the final rail chronology.

## 0. Outcome

Fix `r>=2`, put

\[
 n=2r-1,
 \qquad
 \mathcal L={ [n]\choose r-1},\quad
 \mathcal M={ [n]\choose r},\quad
 \mathcal U={ [n]\choose r+1}.
\tag{0.1}
\]

Let `D` be the standard Greene--Kleitman symmetric-chain decomposition of
the Boolean lattice on `[n]`, and let `D^*` be its set-complement
decomposition.  For every `L in mathcal L`, let

\[
 a(L)=\text{the rank-}r\text{ successor of }L\text{ in }D,
 \qquad
 b(L)=\text{the rank-}r\text{ successor of }L\text{ in }D^*.
\tag{0.2}
\]

Then the Johnson edges

\[
                         a(L)b(L),\qquad L\in\mathcal L,
\tag{0.3}
\]

have all of the following properties.

1. Their intersection labels are exactly `mathcal L`, once each.
2. Every owner in `mathcal M` has degree exactly two.
3. Their union labels cover every member of `mathcal U`; every upper label
   occurs with multiplicity `1`, `2`, or `3`.
4. The owner graph is the projected PBBS factor.  Its successor permutation
   is conjugate to the inverse step-two PBBS map `p^(-2)`.
5. It has at most `Cat_(r-1)` connected components.

Thus the standard Greene--Kleitman decomposition and its set-complement
partner do more than supply a lower matching.  In odd dimension their
central projection is exactly the known PBBS balanced-surjective
two-extension.  The remaining issue is topology and physical chronology,
not immediate lower or upper support.  No appeal to an abstract
Shearer--Kleitman orthogonality theorem is needed for this identification.

## 1. The two SCD successors

Use `0` as an opening parenthesis and `1` as a closing parenthesis.  Let
`gk_up(L)` change the leftmost unmatched zero of `L` to one, and let
`gk_down(X)` change the last unmatched one of `X` to zero.  Then

\[
 a(L)=\operatorname {gk\_up}(L),
 \qquad
 b(L)=[n]\setminus
       \operatorname {gk\_down}([n]\setminus L).
\tag{1.1}
\]

Because `n=2r-1` is odd, every symmetric chain contains one member of each
of the two equally large central ranks `r-1` and `r`.  Hence both maps in
`(0.2)` are bijections:

\[
 |\mathcal L|=|\mathcal M|={2r-1\choose r-1}.
\tag{1.2}
\]

The literal PBBS identity in Lemma 2.1 below gives `a(L) != b(L)`: equality
would make `p^2(L)=L`, whereas every PBBS orbit has length at least
`n=2r-1` (the case `r=2` is also immediate directly).

Consequently `(0.3)` is a simple Johnson edge with intersection `L`.
The union of the two successor bijections gives every owner degree two.
Thus the whole owner graph is 2-regular before any PBBS theorem is invoked.

## 2. Identification with the PBBS map

Put

\[
                         m=r-1,
 \qquad n=2m+1.
\tag{2.1}
\]

Let `p` be the canonical cyclic-parenthesis/PBBS permutation on

\[
                         { [n]\choose m}=\mathcal L.
\tag{2.2}
\]

For `L in mathcal L`, let `rho_+(L)` and `rho_-(L)` be its unique forward-
and reverse-cyclic unmatched zeros.  The standard PBBS formulas are

\[
 p(L)=L^c\setminus\{\rho_+(L)\},
 \qquad
 p^{-1}(L)=L^c\setminus\{\rho_-(L)\}.
\tag{2.3}
\]

Complementing gives two rank-`r` neighbours

\[
 p(L)^c=L+\rho_+(L),
 \qquad
 p^{-1}(L)^c=L+\rho_-(L).
\tag{2.4}
\]

### Lemma 2.1 (literal successor identity)

For every `L in mathcal L`, up to interchanging the two shores,

\[
 \boxed{
 \{a(L),b(L)\}
 =\{p(L)^c,p^{-1}(L)^c\}.}
\tag{2.5}
\]

#### Proof

In the ordinary fixed linear scan, delete all matched `01` pairs.  Because
`L` has one more zero than one, the unmatched symbols have the form

\[
                         1^s0^{s+1}.
\tag{2.5a}
\]

Cyclic cancellation pairs the `s` terminal unmatched zeros with the `s`
initial unmatched ones and leaves the first of those zeros.  This is exactly
the leftmost linearly unmatched zero.  Hence the standard GK successor is
`L+rho_+(L)=p(L)^c`.

Applying the same statement after set complementation and reversing the
chain direction identifies the successor in `D^*` with
`L+rho_-(L)=p^(-1)(L)^c`.  This is `(2.5)`.  The names `rho_+` and `rho_-`
may exchange under the opposite cyclic-cut convention, but the unordered
pair is invariant.  \(\square\)

Therefore `(0.3)` is literally the balanced two-extension edge

\[
 \boxed{
 e_L=\{p(L)^c,p^{-1}(L)^c\}.}
\tag{2.6}
\]

No new factor has been discovered: the SCD-pair and PBBS descriptions are
two coordinate systems for the same owner graph.  In particular this is the
same PBBS projection used in
`MATH_THEOREM_PBBS_PAIRED_MATCHING_C6_POTENTIAL_AND_CONNECTOR_GATE_20260726.md`,
not the distinct lexical Middle-Levels factor.

## 3. Exact lower, owner, and upper ledgers

The lower ledger is immediate:

\[
 p(L)^c\cap p^{-1}(L)^c=L.
\tag{3.1}
\]

Indeed the two endpoints are distinct rank-`r` extensions of `L`.

Both endpoint maps in `(2.6)` are injective, since `p` and complementation
are bijections.  Thus every owner occurs once on each matching shore and
has total degree two.

The upper label is

\[
\begin{aligned}
 \sigma(L)
 &=p(L)^c\cup p^{-1}(L)^c\\
 &=L+\rho_+(L)+\rho_-(L)\\
 &=\bigl(p^{-1}(L)\cap p(L)\bigr)^c.
\end{aligned}
\tag{3.2}
\]

The audited PBBS angle theorem says that every rank-`(m-1)` set occurs as

\[
                         p^{-1}(L)\cap p(L)
\tag{3.3}
\]

for between one and three values of `L`.  Complementing `(3.3)` proves:

### Theorem 3.1 (upper support and sharp fibre bound)

For every `U in mathcal U`,

\[
 1\le
 \bigl|\{L\in\mathcal L:\sigma(L)=U\}\bigr|
 \le3.
\tag{3.4}
\]

In particular `sigma` is surjective.  Since

\[
 |\mathcal L|-|\mathcal U|
 =\frac{2}{r+1}{2r-1\choose r-1},
\tag{3.5}
\]

upper repetitions are arithmetically unavoidable; `(3.4)` is the sharp
bounded-fibre support statement, not an upper-exact matching statement.

## 4. Exact owner permutation and components

Orient `(2.6)` from

\[
                         p(L)^c\longrightarrow p^{-1}(L)^c.
\tag{4.1}
\]

Write `A=p(L)^c`.  Then

\[
                         L=p^{-1}(A^c),
\tag{4.2}
\]

and the head is

\[
 p^{-1}(L)^c
 =p^{-2}(A^c)^c.
\tag{4.3}
\]

Hence the owner successor permutation is

\[
 \boxed{
 g_{\rm SCD}(A)=c\,p^{-2}c(A),}
\tag{4.4}
\]

where `c` denotes set complementation between the two adjacent central
layers.  Thus `g_SCD` is conjugate to `p^(-2)`.

If a `p`-orbit has length `ell*n`, it contributes

\[
                         \gcd(2,\ell n)=\gcd(2,\ell)
\tag{4.5}
\]

cycles to `(4.4)`.  PBBS site homomesy gives

\[
                         \sum_{p\text{-orbits}}\ell
                         =\operatorname {Cat}_{m}.
\tag{4.6}
\]

Consequently

\[
 \boxed{
 c(g_{\rm SCD})
 =\sum_{p\text{-orbits}}\gcd(2,\ell)
 \le\operatorname {Cat}_{r-1}.}
\tag{4.7}
\]

Every component has length at least `n=2r-1`.

## 5. Exact relation to earlier routes

This theorem resolves three possible confusions.

1. **Two orthogonal SCDs are insufficient in general.**  An arbitrary
   orthogonal pair supplies the two successor injections but need not have
   a surjective union map; explicit `Q_4` examples fail.  The positive
   theorem uses the special standard/complement pair and its PBBS identity.

2. **This is not the cyclic three-triangle selector.**  That restricted
   family chooses only three local diamonds under each upper and is
   capacity-impossible for `r>=14`.  Here every lower chooses its two
   canonical SCD/PBBS extensions; upper support follows from the global
   angle theorem.

3. **The factor is not yet a linear forest.**  Equation `(4.7)` may grow
   with `r`.  Indeed this is exactly the existing PBBS component problem.
   A Hamiltonization theorem must use factor-alternating switches that
   preserve the lower ledger and do not destroy the upper support needed by
   the compiler.

4. **The upper row is support, not exact occurrence load.**  The raw factor
   has exactly one lower occurrence per `L` but generally repeats an upper
   label two or three times.  A theorem asking for every upper target merely
   to be witnessed is satisfied.  A theorem asking for upper load exactly
   one still requires thinning/reassignment and must preserve owner degree.

5. **Pure exact-upper thinning is already impossible.**  Choosing one
   occurrence from every upper fibre of `sigma` is, under complementation,
   exactly a one-occurrence PBBS q1 section.  The forced single-soliton
   theorem proves that every such section contains one whole PBBS component
   for `m>=3`.  It is therefore cyclic.  No representative choice inside
   the fixed factor yields an upper-exact acyclic forest; an ambient
   incidence-hexagon or longer alternating-circuit surgery is necessary.

Thus the exact surviving spine is

\[
 \boxed{
 \text{standard/complement SCD}
 =\text{PBBS balanced-surjective two-extension}
 \longrightarrow
 \text{protected component fusion / residence}.}
\tag{5.1}
\]

## 6. Reproducible finite audit

The independent enumerator

```text
scratch/audit_odd_gk_complement_scd_diamond_selector_20260813.py
```

implements `(1.1)` directly, without calling a PBBS routine.  On `h100`,
for `2<=r<=11`, it verifies:

* zero missing upper labels;
* upper fibre multiplicities only `1,2,3`;
* the owner graph is a permutation cycle factor; and
* the component counts

\[
 1,2,3,6,12,26,73,146,360,1408.
\tag{6.1}
\]

The audit is corroborative only.  Lemma 2.1 and Theorems 3.1 and `(4.7)`
are solver-free and hold for every `r`.

The PBBS inputs used here are already frozen in

```text
MATH_THEORY_K_ALL_BALANCED_TWO_EXTENSION_HEXAGON_AND_O1_REDUCTION_20260731.md
MATH_THEOREM_PBBS_PAIRED_MATCHING_C6_POTENTIAL_AND_CONNECTOR_GATE_20260726.md
MATH_THEOREM_PBBS_SINGLE_SOLITON_FORCED_CYCLE_OBSTRUCTION_20260805.md
```
