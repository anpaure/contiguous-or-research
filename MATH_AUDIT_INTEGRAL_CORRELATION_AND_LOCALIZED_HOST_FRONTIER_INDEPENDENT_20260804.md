# Independent audit: integral correlation and localized-host frontier

**Date:** 2026-08-04  
**Audited synthesis:**
`MATH_SYNTHESIS_INTEGRAL_CORRELATION_AND_LOCALIZED_HOST_FRONTIER_20260804.md`  
**Audited synthesis SHA-256:**
`90e637fb9c380cadea67206716f71da68fc493811dc83bd10684e26f7e1d20af`

## Verdict

**PASS after four scope/notation corrections applied to the synthesis.**

No unconditional all-dimensional upper bound follows.  The synthesis
correctly leaves `k=17` open and reduces the displayed programme to one
correlated integral, occurrence-labelled host choice.  The corrections do
not weaken any proved theorem; they prevent four summaries from ranging
beyond their actual hypotheses:

1. the strict raw two-SCD socket reserve is proved asymptotically for even
   dimensions, not uniformly in both parities;
2. a bounded total seam footprint extends only for a nonempty local state
   and when both Johnson-slice margins are large enough;
3. the pair-stratified residence theorem is an even-ground-dimension,
   almost-spanning **cycle-factor** theorem, not a global carrier theorem;
4. the degree-weighted router requires one common residual state, private
   occurrence lifts, and compatible terminal types.

The product-Johnson variables `A,B,h,ell` were also defined explicitly in
the synthesis, and the terminal implication was attributed jointly to the
charge ledger and the private-pushout composition theorem.

## 1. Endpoint and lower-chain ledger

For `n=W+h`, the right-endpoint capacities are exactly

\[
  (h^{W+1},h-1,\ldots,1),
  \qquad \sum c_j=hW+{h+1\choose2}.
\]

The rank-slot max-flow cuts reduce to unions of the largest strict-lower
ranks, and the strong-Sperner bounds prove all of them.  The uniform-cap
fractional optimum is

\[
 \max\left\{{k\choose r-1},\Lambda/h\right\};
\]

at `h=d>=1`, `W+d` exceeds it by at least `(d-1)/2`.  The complete-
multipartite example really has fractional feasibility in the triangular
slots but integral requirement `n+1`, so no generic perfect-graph rounding
is being inferred.

For independent symmetric slot sampling, a fixed top lower target is missed
with probability at least `(1-1/a)^a>=1/4`.  McDiarmid with one-slot
Lipschitz constant one gives

\[
 \Pr(Z<a/8)\le \exp(-a^2/(32n)).
\]

Thus the product-rounding obstruction and its `Omega(W)` alteration claim
have the correct direction and scope.

## 2. Two-SCD constants and threshold obstruction

With `t=r-d`, collar socket capacity `u` occurs

\[
 {k\choose t+u}-{k\choose t+u-1}
\]

times, including `W-{k\choose r-1}` full-capacity empty owner sockets.
Total residual vacancy is exactly

\[
 dW+{d+1\choose2}-\Lambda.
\]

For even `k=2m`, `d^2/m -> pi/4`; hence

\[
 S/W\to1-e^{-\pi/4}>0.544,
 \qquad
 P/W\to\sum_{q\ge1}e^{-\pi q^2/4}<0.501.
\]

The aggregate threshold system is exactly

\[
 \sum_s\sum_{a\ge q}A_{s,a}
 \le W-{k\choose t+q-1}+d-q+1.
\]

Maximal `d`-slabs fail its `q=d` cut by linear mass.  The two Gaussian-limit
inequalities in the common-slab theorem are incompatible on the forced
interval, so the synthesis correctly concludes only that common rank grids
fail; chain-dependent cutting and literal containment Hall remain open.

## 3. Upper occurrence section

The `R,A,R,B` four-cycle is a valid abstract obstruction: either target is
individually realizable and every colour section breaks the cycle, but the
two targets force distinct `R` occurrences.  The target-choice natural join
is exactly equivalent to a rainbow witness selector.  Semijoin pruning is
complete on a running-intersection tree.  Immutable reserve Hall is
sufficient, and selector-independent, only relative to the full declared
menu envelope; the synthesis does not promote it to a universal Boolean
factor theorem.  The blocker LLL retains its explicit colour-disjoint-menu
and dependency hypotheses.

## 4. Seam and router

Writing

\[
 A=H-F,\quad B=H^c-F,\quad
 h=D-1-|F\cap H|,\quad \ell=D-1,
\]

the eligible tokens are exactly `binom(A,h) x binom(B,ell)`.  For a fixed
total footprint `U,V`, each allowed state `(S,T)` has exactly

\[
 { |A|-|U|\choose h-|S|}
 { |B|-|V|\choose\ell-|T|}
\]

extensions.  The occurrence-exception subtraction, cylinder weights, and
rare-defect/transversal criteria all follow with the displayed directions.
The unary-hole and singleton-occurrence covers correctly rule out a
scope-only LLL.

For the degree-weighted cascade, weight `1/(hq)` on each incidence chain.
Claim, prefix, port, suffix, and sink loads are respectively

\[
 1,\quad1/h,\quad d_p/h,\quad d_p/(hq),\quad
 (hq)^{-1}\sum_{f=ps}d_p.
\]

The sink premise bounds the last load by one, and integral node-split max
flow gives distinct typed sinks.  This is a valid claim-level certificate;
it is not inferred from abstract factors without their common physical
lift.

## 5. Residence and final implication

Pair cells in `J(2r,r)` are induced cubes `Q_m`.  On cells with

\[
 m\ge L+\lceil3\log_2r\rceil,
\]

the Goddyn--Gvozdjak bound separates repeated transitions of every varying
coordinate by at least `L`.  The omitted owner fraction is at most

\[
 (2r+1)2^{-r}\left({er\over
 L+\lceil3\log_2r\rceil}\right)^{L+\lceil3\log_2r\rceil}
 =e^{-\Omega(r)}
\]

when `L=Theta(sqrt(r))`.  This is not additive-small and not spanning;
small cells force cross-cell work.  The explicit `J(5,2)` Hamilton cycle
indeed has maximal compression/one-track balance but minimum run one, so
those invariants do not replace transition separation.

Finally, a materialized localized host whose complete replay has charge at
most `C`, together with the odd regeneration and terminal even-tap rows,
has terminal charge at most `C`.  The existing charge ledger then gives
`nu(k)<=B(k)+C`.  This is a proved conditional implication, not an
existence claim for the host.

## 6. Frozen input ledger

```text
12b6934ab7cca5c714bc4f19117da6d044f9a2e6370528e0e51426989c121c7a  MATH_THEOREM_ENDPOINT_TRIANGULAR_BOUNDED_CHAIN_FRACTIONAL_EXACTNESS_20260804.md
97aeefcc4e59c0fa639ea0dfd578ae451ab12478ffbfee24bc469f4a7c71552f  MATH_AUDIT_ENDPOINT_TRIANGULAR_BOUNDED_CHAIN_FRACTIONAL_EXACTNESS_20260804.md
bf4035986a30e154fd8cdc66e1b906409470328b746ef1f6d8dcc0288ff3558e  MATH_THEOREM_BOOLEAN_ENDPOINT_PRODUCT_ROUNDING_NOGO_AND_TWO_SCD_SOCKET_LEDGER_20260804.md
3e136079c1a583c052bcf9c69f1569b29a25c6b68ec738aa5093f9291bdd0494  MATH_AUDIT_BOOLEAN_ENDPOINT_PRODUCT_ROUNDING_NOGO_AND_TWO_SCD_SOCKET_LEDGER_20260804.md
1d0056b9574e6363a19040d3dbd51d5893cc8fa1c2ecff245604bab4df35269b  MATH_THEOREM_MULTI_SLAB_CROSS_SCD_EXACT_HALL_AND_TOP_SLAB_CUT_20260804.md
ddf9fa4cdab47d2b03904977ee6bacee2095ab07ed028fa268015f91faa2285e  MATH_AUDIT_MULTI_SLAB_CROSS_SCD_EXACT_HALL_AND_TOP_SLAB_CUT_20260804.md
9e329db1beeb6614a7ea43e5e18b72fea9619c2c57882b010d977376b49677b9  MATH_THEOREM_BPLUS1_OCCURRENCE_SECTION_DUAL_JOIN_TREE_RESERVE_HALL_AND_BLOCKER_LLL_20260804.md
89bdcdde7ea20a36aa2a93fa31b6cab5e646115673c024d87560dfb830c082a8  MATH_AUDIT_BPLUS1_OCCURRENCE_SECTION_DUAL_JOIN_TREE_RESERVE_HALL_AND_BLOCKER_LLL_INDEPENDENT_20260804.md
575a89720b723b6d5f3c42c147d4c808aae667bc9856b037e9a9db5eeba33e01  MATH_THEOREM_TOKEN_SPHERE_LAMINAR_PRIVATE_PIVOT_HOST_COINSTANTIATION_20260804.md
769b7fa3a8051f0b69309046707c984077c3299bd4b4857d170421b6d17d2389  MATH_AUDIT_TOKEN_SPHERE_LAMINAR_PRIVATE_PIVOT_HOST_COINSTANTIATION_20260804.md
8b41c84ce5d39fb8c16aff7a285a5644c66f2a5dabb71935bf71f65f0b76858a  MATH_THEOREM_PRODUCT_JOHNSON_SEAM_LOCAL_EXTENSION_AND_RARE_DEFECT_CONTAINERS_20260804.md
d0166cd689a85f367de47286e82cda3186adb71df21c31bfcb63a269516809a4  MATH_AUDIT_PRODUCT_JOHNSON_SEAM_LOCAL_EXTENSION_AND_RARE_DEFECT_CONTAINERS_20260804.md
7f53a75a509cbff1e3cfdc95b9b76a794ebaa4e0690d4e952705a1cb86d3027e  MATH_THEOREM_TWO_REGULAR_FACTOR_PRIVATE_ROUTER_COMPOSITION_20260804.md
4d45d5f84e317f445191af7a4ec8ccf0ce64ff0f83b706bf6810c21b8a2bf521  MATH_AUDIT_TWO_REGULAR_FACTOR_PRIVATE_ROUTER_COMPOSITION_20260804.md
d4982696d75449f8b93e70d4c4e958648ee2d34dc299c5cfb2a91fd2cd9393bb  MATH_THEOREM_PAIR_STRATIFIED_LONG_RUN_JOHNSON_FACTOR_20260804.md
1b7d8b8d940b8c5bd13f1db5c39b8fd248919cb35570d3d1ca7f9181db843414  MATH_AUDIT_HAMILTON_COMPRESSION_TRACK_BALANCE_VS_RESIDENCE_20260804.md
704a81661b39593adcfdcb9c21f9cd2e76e0db9c6860d52c1ff35a4340dd4c0e  MATH_SYNTHESIS_PPC1_PCC0_EXACT_CUT_FRONTIER_20260804.md
3095236b375b17cd98614b91fcc93317e91702c830c3e7dc93f52465347ba280  MATH_AUDIT_PPC1_PCC0_EXACT_CUT_FRONTIER_INDEPENDENT_20260804.md
```

No finite search, solver, or computational candidate is used in this
audit.
