# Hamilton-anchored matching repair gives polynomially many completion cycles

**Date:** 2026-08-06  
**Method:** middle-level Hamilton anchoring, the Johnson spectral surplus,
the balanced sharp partial-shadow threshold, and short alternating-cycle
repairs; no computation or finite search  
**Status:** unconditional graph theorem using the standard middle-level
Hamilton-cycle theorem.  A polynomial protected path forest with
an all-occurrence sub-half exposure cap can be inserted into the two
alternating halves of one Hamilton cycle while changing only polynomially
many incidences.  The resulting coloured two-matching completion has only
polynomially many components.  This closes the *number of completion
components* row.  It does not by itself remove common edges, pack arbitrary
component-to-code boundary arms, plant one literal PBBS antecedent, or prove
the occurrence-labelled typed suffix rank.

## 1. Setting and the prefix-safe cap

Put

\[
 \mathcal L={ [2r-1]\choose r-1},\qquad
 \mathcal U={ [2r-1]\choose r},\qquad
 W=|\mathcal L|=|\mathcal U|,
\tag{1.1}
\]

and let `G` be the inclusion graph between the two shores.  It is
`r`-regular.  Fix a Hamilton cycle

\[
                         \mathcal H=H_0\mathbin{\dot\cup}H_1
\tag{1.2}
\]

of `G`, with its two alternating perfect matchings `H_0,H_1`.  Existence of
such a cycle is the middle-levels theorem.

Let `F` be a matching, with lower endpoint set `Z` and upper endpoint set
`Y`.  In addition to the residual-domain exposure used by the polynomial
matching-extension theorem, define the stronger all-occurrence exposures

\[
 \widehat\alpha(F)=
   \max_{x\in\mathcal L}|N_G(x)\cap Y|,
 \qquad
 \widehat\beta(F)=
   \max_{U\in\mathcal U}|N_G(U)\cap Z|.
\tag{1.3}
\]

The hat on `alpha` is load-bearing.  The old definition omits the lower
vertices already used by `F`; a vertex used by a *later* edge is still
unmatched at an earlier insertion prefix.  Condition (1.3) makes every
ordering of the protected occurrences prefix-safe.  More generally, all
arguments below need only an ordering whose every prefix has the stated two
exposure bounds.

Fix constants `C<infinity` and `epsilon>0`.  Throughout Sections 2--5 assume

\[
 |F|=f\le r^C,
 \qquad
 \widehat\alpha(F),\widehat\beta(F)
       \le(1/2-\epsilon)r.
\tag{1.4}
\]

All conclusions are for sufficiently large `r`, depending only on
`C,epsilon`.

## 2. Every protected-prefix residual graph is elementary

Order the edges of `F` and let `F_j` be the first `j` edges.  Delete the
endpoints of `F_j` and write

\[
 B_j=G[\mathcal L\setminus Z_j,\mathcal U\setminus Y_j].
\tag{2.1}
\]

The polynomial matching-extension theorem guarantees a perfect matching of
`B_j`.  We need the stronger fact that its alternating exchange digraph has
small directed diameter.

Put

\[
 D_*=r-\widehat\alpha(F),
 \qquad
 K(D')={2D'-1\choose D'}.
\tag{2.2}
\]

Thus `D_*` is an integer and
`D_* >= (1/2+epsilon)r`.

### Lemma 2.1 (connected prefix residual)

Every `B_j`, `0<=j<=f`, is connected.

#### Proof

Suppose `B_j` is disconnected and choose a component with lower shore
`A` and upper shore `C` of minimum size.  A perfect matching of `B_j`
restricts to every component, so

\[
                         |A|=|C|=:a,
 \qquad a\le(W-j)/2<W/2.
\tag{2.3}
\]

Since all old neighbours of `A` lie in `C union Y_j`,

\[
 |N_G(A)|-|A|\le j.
\tag{2.4}
\]

The Johnson spectral-surplus inequality gives

\[
 |N_G(A)|-|A|
 \ge {2r-1\over r^2}{a(W-a)\over W}
 \ge {2r-1\over2r^2}a.
\tag{2.5}
\]

Consequently

\[
                         a\le {2r^2\over2r-1}j<2rj.
\tag{2.6}
\]

On the other hand, every `x in A` has at least

\[
 r-|N_G(x)\cap Y_j|
 \ge r-\widehat\alpha(F)=D_*
\tag{2.7}
\]

neighbours in `C`.  Complement `A` and `C` in `[2r-1]`.  This gives a
balanced adjacent-rank pair `(\mathcal J,\mathcal F)` with
`|\mathcal J|=|\mathcal F|=a`, in which every member of the rank-`r` family
`\mathcal J` contains at least `D_*` members of the rank-`r-1` family
`\mathcal F`.  The balanced form of the sharp partial-shadow theorem yields

\[
                         a\ge K(D_*).
\tag{2.8}
\]

But

\[
 \log_2K(D_*)\ge(1+2\epsilon)r-O(\log r),
\tag{2.9}
\]

whereas `2rj<=2r^(C+1)`.  Equations (2.6) and (2.8) contradict one another
for sufficiently large `r`.  Thus `B_j` is connected. \(\square\)

### Lemma 2.2 (every residual edge is allowed)

Every edge of `B_j` belongs to a perfect matching of `B_j`.

#### Proof

Let `e` be an edge of `B_j`.  The matching `F_j+e` has polynomial size.
Its two residual-domain exposures are at most

\[
 \widehat\alpha(F)+1,\qquad \widehat\beta(F)+1,
\tag{2.10}
\]

which, for sufficiently large `r`, are at most
`(1/2-epsilon/2)r`.  Apply the polynomial partial-matching extension
theorem to `F_j+e`.  Removing `F_j` from the resulting perfect matching
gives a perfect matching of `B_j` containing `e`. \(\square\)

Fix a perfect matching `N` of `B_j`.  Contract its edges and use the lower
vertices as labels.  Define the directed exchange graph `D_N` by

\[
 x\longrightarrow z
 \quad\Longleftrightarrow\quad
 xN(z)\in E(B_j).
\tag{2.11}
\]

Every vertex has a loop, corresponding to its edge of `N`.

### Lemma 2.3 (strong exchange connectivity)

The digraph `D_N` is strongly connected.

#### Proof

By Lemma 2.2 every edge `e` of `B_j` belongs to some perfect matching
`N_e`.  The symmetric difference `N \mathbin\triangle N_e` is a union of alternating
cycles, and the cycle containing `e` shows that the corresponding arc of
`D_N` lies on a directed cycle.  After contracting `N`, the underlying
undirected graph is connected by Lemma 2.1.  If the strong-component
condensation had an edge, that edge could not lie on a directed cycle.
Hence the condensation has no edge and, by connectedness, has one vertex.
\(\square\)

The proof used both sharp inputs for distinct purposes: spectral surplus
localizes a hypothetical residual component to polynomial size, while the
balanced partial-shadow theorem says that such a component must have
exponential size.  Hall extension alone does not imply Lemma 2.1.

## 3. Polynomial directed diameter

### Lemma 3.1 (explicit alternating diameter)

For every perfect matching `N` of `B_j`,

\[
 \operatorname {diam}^{\to}(D_N)
 \le 8rj+16r\log W+4
 \le 8rj+32r^2+4.
\tag{3.1}
\]

#### Proof

Let `X=\mathcal L-Z_j`, and identify the upper shore with `X` through `N`.
For `S\subseteq X`, equation (2.11) gives

\[
 |\Gamma^+(S)|=|N_G(S)\setminus Y_j|.
\tag{3.2}
\]

If `|S|<=W/2`, the spectral-surplus inequality gives

\[
 \begin{aligned}
 |\Gamma^+(S)|-|S|
 &\ge {2r-1\over r^2}{|S|(W-|S|)\over W}-j\\
 &\ge {|S|\over2r}-j.
 \end{aligned}
\tag{3.3}
\]

Also `S subseteq Gamma^+(S)` because of the matching loops.  By strong
connectivity, the inclusion is strict whenever `S` is nonempty and proper.
Thus a forward ball grows by at least one vertex per step until its size is
`4rj`; thereafter (3.3) gives

\[
                         |\Gamma^+(S)|
                         \ge(1+1/(4r))|S|
\tag{3.4}
\]

until the ball has more than `W/2` vertices.  Since
`log(1+1/(4r))>=1/(8r)`, this takes at most

\[
                         4rj+8r\log W+2
\tag{3.5}
\]

steps.

The complement map interchanges the two middle shores and preserves
incidence.  Applying the same argument to upper families, with the `j`
deleted lower vertices charged in place of `Y_j`, gives the identical
bound for a backward ball from any target.  Two subsets of `X` having more
than `W/2` members intersect.  Joining at an intersection gives the first
inequality of (3.1).  Finally `W<2^(2r-1)` gives
`16r log W<32r^2` when the logarithm is natural. \(\square\)

The `O(rj)` term is deliberately crude.  It is polynomial for every
protected prefix and is enough for the component theorem.

## 4. Local insertion into an arbitrary base matching

### Theorem 4.1 (polynomial-damage matching repair)

Let `H` be any perfect matching of `G`.  Under (1.4), there is a perfect
matching `M` containing `F` such that

\[
 |M\mathbin\triangle H|
 \le \rho(r,f):=8rf^2+64r^2f+10f.
\tag{4.1}
\]

Every edge of `F` is retained as its literal protected incidence, not merely
by colour or endpoint type.

#### Proof

Start with `M_0=H`.  Inductively suppose `M_j` contains `F_j`.  If the next
edge `e=xN(y)` already lies in `M_j`, do nothing.  Otherwise remove the
edges of `F_j` from `M_j`; the remainder `N` is a perfect matching of
`B_j`, and `e` is the arc `x\longrightarrow y` of `D_N`.

By Lemma 3.1 there is a directed path from `y` back to `x` of length at most

\[
                         8rj+32r^2+4.
\tag{4.2}
\]

Together with `x\longrightarrow y` it is a directed cycle.  Switch `N` around the
corresponding alternating cycle.  This inserts `e`, changes no endpoint of
`F_j`, and produces `M_(j+1)` containing `F_(j+1)`.  The matching symmetric
difference used at this step has at most twice the number of directed-cycle
arcs.  Therefore

\[
 \begin{aligned}
 |M_f\triangle H|
 &\le 2\sum_{j=0}^{f-1}(8rj+32r^2+5)\\
 &\le8rf^2+64r^2f+10f.
 \end{aligned}
\tag{4.3}
\]

Take `M=M_f`. \(\square\)

This theorem is stronger than bare extension in exactly the needed way:
the completion can be chosen in a polynomial Hamming ball around a prescribed
perfect matching.

## 5. Polynomial cycle count for the two PBBS roles

Let `P` be an occurrence-labelled protected owner-path forest.  Orient every
component and alternately colour its incidence edges `0,1`; call the colour
classes `F_0,F_1`.  They are matchings.  Assume, for `i=0,1`,

\[
 f_i=|F_i|\le r^C,
 \qquad
 \widehat\alpha(F_i),\widehat\beta(F_i)
        \le(1/2-\epsilon)r.
\tag{5.1}
\]

### Theorem 5.1 (Hamilton-anchored polynomial-component completion)

There are perfect matchings \(M_i\supseteq F_i\) such that the coloured
multigraph

\[
                         \mathcal K=M_0\mathbin\uplus_{\rm col}M_1
\tag{5.2}
\]

contains every protected path with its prescribed orientation and satisfies

\[
 \boxed{
 c(\mathcal K)
 \le 1+{\rho(r,f_0)+\rho(r,f_1)\over2}
 =r^{O(1)}.}
\tag{5.3}

Moreover, unless `mathcal K=mathcal H`, every component of `mathcal K`
contains an incidence in the polynomial damage set

\[
 \mathcal R=(M_0-H_0)\mathbin\uplus_{\rm col}(M_1-H_1).
\tag{5.4}
\]

#### Proof

Apply Theorem 4.1 to `(H_i,F_i)` separately.  This gives perfect matchings
`M_i` with the required protected incidences and

\[
 |M_i-H_i|={1\over2}|M_i\triangle H_i|
          \le\rho(r,f_i)/2.
\tag{5.5}

If a component of `mathcal K` contains no coloured edge outside its
corresponding `H_i`, it is a cycle subgraph of the single simple cycle
`mathcal H`.  The only such cycle is all of `mathcal H`.  Thus either
`mathcal K=mathcal H`, or every component contains a distinct edge of
`mathcal R`.  Equations (5.3)--(5.4) follow. \(\square\)

### Corollary 5.2 (one completion matching already fixed)

Suppose `M_0` is already fixed and, for one Hamilton decomposition (1.2),

\[
                         h=|M_0\triangle H_0|=r^{O(1)}.
\tag{5.6}
\]

Then `F_1` has an extension `M_1` for which

\[
 c(M_0\mathbin\uplus_{\rm col}M_1)
 \le1+{h+\rho(r,f_1)\over2}=r^{O(1)}.
\tag{5.7}

Thus the fixed-matching statement is valid with the exact load-bearing
hypothesis that the fixed matching has polynomial Hamilton distance.  An
arbitrary earlier extension is not covered.  For PBBS one should choose the
first extension by Theorem 4.1 rather than freeze an uncontrolled extension.

### Corollary 5.3 (common-edge debt is also polynomial)

The number of incidences common to `M_0` and `M_1` is at most

\[
                         |\mathcal R|
 \le {\rho(r,f_0)+\rho(r,f_1)\over2}.
\tag{5.8}

#### Proof

The Hamilton halves `H_0,H_1` are edge-disjoint.  Hence any edge common to
`M_0,M_1` is outside at least one corresponding Hamilton half and is counted
in `mathcal R`. \(\square\)

This does **not** remove the common edges.  It reduces the simple-factor debt
from an uncontrolled number to a polynomial bank of explicit occurrences.

## 6. Why unweighted random matching is the wrong measure

Let `M_0` be any fixed perfect matching of `G`, and choose `M_1` uniformly
from all perfect matchings of `G`.  The middle-level incidence graph is
edge-transitive, so every edge has marginal `1/r`.  Therefore

\[
 \mathbb E|M_0\cap M_1|={W\over r}.
\tag{6.1}
\]

Every common incidence is a coloured two-cycle component.  Thus the uniform
measure satisfies

\[
                         \mathbb E c(M_0\uplus_{\rm col}M_1)
                         \ge W/r,
\tag{6.2}
\]

and has exponentially large expected component count.  The same warning
applies to any weighted law whose fixed-matching edges retain comparable
marginals.  Setting those weights to zero removes this first moment, but an
ordinary product of edge weights does not encode the nonlocal number of
successor cycles.  A cycle-fugacity or switching argument would still need a
separate theorem.

Hamilton anchoring avoids this trap: it constructs both extensions inside a
polynomial damage ball around a one-component factor.

## 7. Consequence for the PBBS backup forest

The stretched role-zero macros, immediate two-palette backups, and
rank-stratified arbitrary-upper backups form a polynomial protected path
forest.  Once their two alternating occurrence matchings satisfy the
prefix-safe version of (5.1), Theorem 5.1 gives a directed coloured
completion with polynomially many components while retaining literally:

1. every protected role-`0` half-history incidence;
2. every immediate lower- and upper-palette backup incidence;
3. every rank-stratified upper-backup path; and
4. the chosen orientation of every protected path.

For the advertised `r/3` exposure target one may take any fixed
`epsilon<1/6`, provided that `r/3` is verified on the all-occurrence or
prefix-safe domains of (1.3), not only on the final residual domain.

The completion support outside the Hamilton backbone is polynomial and hits
every completion component.  Thus there is no longer an exponential census
obstruction to assigning component roots or port signatures.

## 8. Polynomial separable tags: what now follows and what does not

Let the bound in (5.3) be at most `r^A`, for fixed `A`.  Choose the
Reed--Solomon tag-code degree so that `d+1>A`.  The separable-tag theorem then
provides, in a linear tag reservoir, distinct codes for every component root
and every common-edge repair, with all unordered pair unions distinct.
Consequently:

* there are enough physical signatures for the whole completion bank;
* once each rooted component is brought to its assigned coded port, the
  central portions of all pair connectors are mutually resource-disjoint;
  and
* an ordering of the polynomial components can be fused algebraically by
  the pair-coded connectors.

This is a signature/count corollary, not yet an unconditional physical
fusion theorem.  The coded-port theorem leaves `O(d)` partial-tag boundary
stages only when both ends are already coded ports.  The roots in (5.4) are
arbitrary middle-level incidences.  A simultaneous, low-exposure packing of
the root-to-coded-port arms is still required.  The theorem above supplies a
polynomial rooted list for that packing; it does not silently manufacture
those arms.

## 9. Typed occurrence cap remains explicit

All matchings and switches above are physical incidence statements.  They do
not imply that a chosen port survives the compensation linkage and the typed
common-cap suffix.

After materializing the histories and fixing every phase/guard state, let
`P_conn` be the occurrence-labelled connector port set and let
`Gamma_suf^type` be the residual typed strict gammoid.  The one-system exact
deficiency remains

\[
 \kappa_{\rm cap}
 =|P_{\rm conn}|-
   r_{\Gamma_{\rm suf}^{\rm type}}(P_{\rm conn}).
\tag{9.1}
\]

For the two occurrence coordinates, the common Rado/Edmonds all-subset
inequality is required; two separate rank equalities are not enough.  In the
private-list formulation, the still-sufficient quantitative row is

\[
                         \min_p|C_p|\ge2\Delta,
\tag{9.2}
\]

where `C_p` is the set of clean arms carrying a complete legal typed suffix
for port `p`, and `Delta` is the maximum cross-list conflict multiplicity of
one accepted arm.

The cycle-count theorem changes `|P_conn|` from potentially exponential to
polynomial.  It gives no lower bound on the rank in (9.1), no positive-density
bound on `|C_p|`, and no upper bound on `Delta`.

## 10. Exact new PBBS frontier

The large completion forest is no longer an uncontrolled topological object.
Under the explicit prefix-safe exposure cap it admits a completion with:

\[
 \text{polynomial matching damage},\qquad
 \text{polynomial component count},\qquad
 \text{polynomial common-edge debt},
\tag{10.1}
\]

and every component has a polynomially listed repair root.

The remaining fusion/lift rows are exactly:

1. pack root-to-coded-port arms and the partial-tag boundary stages with
   sub-half all-occurrence exposure;
2. remove or detour the polynomial common-edge bank if a simple factor is
   required;
3. plant one biresident literal antecedent through the protected macros and
   the selected repair support; and
4. prove the typed Rado/gammoid suffix condition (9.1)--(9.2).

In particular, neither arbitrary unweighted matching nor the bare
polynomial matching-extension theorem should be cited for a few-cycle
conclusion.  The Hamilton anchor and the prefix-safe cap are the two new
load-bearing inputs.

## 11. Dependencies

The proof uses:

* the middle-level Hamilton-cycle theorem for (1.2);
* Lemma 2.1 and Theorem 5.1 of
  `MATH_THEOREM_POLYNOMIAL_PARTIAL_MATCHING_EXTENSION_AND_DIRECTED_FOREST_COVER_20260806.md`;
* the balanced sharp partial-shadow threshold in
  `MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md`;
* the polynomial pair-union code in
  `MATH_THEOREM_POLYNOMIAL_MANY_SEPARABLE_TAG_PORTS_20260806.md`; and
* the typed-rank audit in
  `MATH_THEOREM_TAGGED_CONNECTOR_ANTECEDENT_SCHEDULING_AND_CAP_OBSTRUCTION_20260806.md`.
