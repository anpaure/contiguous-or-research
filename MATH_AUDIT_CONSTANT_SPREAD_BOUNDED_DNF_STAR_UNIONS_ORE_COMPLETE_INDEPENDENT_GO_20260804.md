# Independent GO audit: bounded/log-width DNF star-union Ore closure

**Date:** 2026-08-04  
**Method:** independent symbolic and asymptotic derivation; no computation,
search, or solver  
**Theorem SHA-256:**
`26dd7101b25bd4b1ddc6bd8daace1620cfb5805b0e58828b5180d1b70967e1e2`

## Verdict

**GO after scope and premise corrections.**  The local fibre/current law,
slack inclusion--exclusion, quantitative condition

\[
 4^h(h+\log m)=o(m),
\]

the half-logarithmic corollary, and the singleton Hamming-tail obstruction
all replay correctly.  No mathematical counterexample was found.

The patched theorem now defines `mu_P=sigma-lambda` before use, states the
needed frozen premise `d=O(sqrt(m))`, replaces the unsupported word “sharp”
by “quantitative,” and says that widths outside the growth condition—not all
unbounded widths—remain open.  It also records the exact tail ratio.

## 1. Fibre and current

At an owner `U`, deleting `x` satisfies clause `C_i` exactly when
`C_i subseteq U` and `x notin C_i`.  The union of accepted deletions is

\[
 \bigcup_{i\in I(U)}(U\setminus C_i)
 =U\setminus\bigcap_{i\in I(U)}C_i=U\setminus J_U.
\]

Thus `a_U=m-|J_U|`.  Every active core has size at most `m-2`, so every
nonzero fibre is at least two.  The exact local loss consists of protected
deletions in `J_U`.  Such a deletion is counted by every active individual
star, proving current domination (1.4).  Counting it `h_U(x)` times in the
individual rows and once precisely when `h_U(x)=|I(U)|` proves the exact
cancellation formula (1.5).

## 2. Inclusion--exclusion

Since active fibres are at least two,

\[
 \sigma(\mathcal A)/2=|N(\mathcal A)|-|\mathcal A|.
\]

Intersections of principal stars have core `Q_I=union_(i in I)C_i` on both
shores.  Inclusion--exclusion therefore gives (2.4), including core ranks
`m` and larger through the stated endpoint convention.

Direct binomial division gives

\[
 \delta_q={q\over m-q}{2m-1-q\choose m-q-1},
 \qquad
 {\delta_{q+1}\over\delta_q}
 ={(m-q)(q+1)\over q(2m-q-1)}\le1.
\]

The last inequality is equivalent to `m<=qm`; `delta_m=1<=m-1` closes the
endpoint.  The two-core margin identity follows by subtracting the exact
cancellation current from the exact slack overlap.

## 3. High-core case

After deleting redundant clauses, every even inclusion--exclusion union
strictly enlarges each assigned participating core.  Monotonicity and the
ratio above give

\[
 \delta(Q_I)\le\delta_{c_i+1}
 \le {2\rho_i\over m}\delta_i.
\]

At most `2^(h-1)` even terms are charged to one core.  With
`alpha_h=min(1/17,2^(-(h+1)))`, their total is at most half the singleton
sum.  Hence

\[
 \sigma\ge\sum_i\delta_i
 \ge16\sum_iA_i\ge16|\mathcal A|.
\]

With at least two irredundant clauses, `|A|>=2m+1`; therefore the frozen
`15|A|+2m` bound closes this case.

## 4. Entropic case and variable width

Choosing one coordinate from each core leaves every lower set avoiding the
chosen set outside the DNF.  Because the width condition implies `h=o(m)`,

\[
 {W-|A|\over W}
 \ge\prod_{j=0}^{h-1}{m-j\over2m-1-j}\ge3^{-h}.
\]

The Johnson spectral inequality gives

\[
 \sigma(A)\ge {4\,3^{-h}\over m}A_*.
\]

For `alpha=rho_*/m<=1/2`, comparison of
`A_*=binom(m+rho_*-1,rho_*-1)` with
`H_(rho_*)(m)<=(rho_*+1)binom(m,rho_*)` has binary entropy gap

\[
 g(\alpha)=(1+\alpha)\log_2(1+\alpha)
 +(1-\alpha)\log_2(1-\alpha)
 \ge {\alpha^2\over\ln2}.
\]

For `alpha>=1/2`, comparison with `H_rho<=2^m` gives an absolute linear
gap.  Since `alpha>alpha_h`, uniformly

\[
 \log_2(A_*/N_*)\ge\kappa m/4^h-O(\log m).
\]

The condition also gives `rho_*>>sqrt(m)>=d`, so `H_(rho_*)` absorbs the
frozen high-tail term.  Finally,

\[
 {m/4^h\over h+\log m}\longrightarrow\infty,
\]

which dominates exactly the required `hm3^h` prefactor and proves
`sigma>2hN_*>=lambda`.

If `h<=(1/2-epsilon)log_2m`, then

\[
 4^h(h+\log m)\le m^{1-2\varepsilon}O(\log m)=o(m),
\]

so the logarithmic-width corollary is correct.

## 5. Hamming-tail obstruction

For `h` singleton cores with coordinate set `R`, complementation gives

\[
 \sigma(A_h)={2h\over m}{2m-1-h\choose m-1}.
\]

The next singleton adds exactly

\[
 {2m-2-h\choose m-2}
 ={m-1\over2m-1-h}{2m-1-h\choose m-1}
\]

lower vertices.  Since the protected margin cannot exceed `sigma`, the
largest possible radius certified by the frozen `(2m+2)`-Lipschitz theorem
is at most

\[
 {h\over m(m+1)}{2m-1-h\choose m-1}.
\]

The exact ratio of the next term to this upper bound is

\[
 {m(m+1)(m-1)\over h(2m-1-h)}=\Theta(m^2/h)
\]

for `h=o(m)`.  Therefore geometric decay alone cannot justify an
`O(log m)` head plus unstructured Hamming tail.

## 6. Scope

The theorem proves all DNF widths satisfying the displayed growth condition
for the one frozen reservoir.  It does not prove wider DNFs, unbounded
Macaulay generator lists, component placement, residence beyond the frozen
input, or common-cap compatibility.  The tail result rules out only the
generic Lipschitz-tail strategy; it is not an obstruction to direct
cancellation-aware analysis of wider ordered DNFs.
