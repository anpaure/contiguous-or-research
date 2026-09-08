# The coatom-order breaker has a `2d+2`-cell marginal footprint; compiler monotonicity is exactly an `ell-alpha` condition

Date: 2026-08-01  
Status: exact local compiler-footprint lemma, exact state-optimized matching
criterion, and smallest literal common-cap counterexample.  The result does
not prove global planting, a common cap for the breaker, or bounded terminal
deletion.

## 0. Scope and conclusion

Use the authoritative endpoint-planted old/new coatom words and change only
the label-attached `Ica` block by interchanging the adjacent omission owners
`C_(f_1),C_(f_2)` in both phases.  Relative to the untwisted word, this
changes the complete flat **individual-incidence signature** on exactly

\[
                              2d+2
\]

physical cells in each phase.  It changes no physical cell and no terminal
target obligation.  The two phase footprints occur at different addresses.

This small marginal footprint does not imply a common-cap compiler move.
After optimizing over all legal terminal cap states, nonworsening is
equivalent to one exact condition: some legal new state must contain at
least as many vertex-disjoint augmenting paths as the number of old matched
edges lost in that state.  Quadratic occurrence span gives no lower bound on
this augmenting-linkage number.

## 1. Conventions and the exact footprint

Index owners and maximal-envelope positions from zero, with no exterior
padding.  For a rank-`r` owner word `W=(W_0,...,W_(N-1))`, put

\[
 E_p(W)=\bigcap_{\max(0,p-d)\le i\le\min(p,N-1)}W_i,
 \qquad 0\le p<N+d.                                      \tag{1.1}
\]

A width-`h` compiler cell is the half-open envelope interval

\[
                              c=[s,s+h),\qquad 1\le h\le d. \tag{1.2}
\]

For an owner-coordinate occurrence `(i,z)`, let

\[
 R_{i,z}(W)=\{p\in[i,i+d]:z\in E_p(W)\}.                 \tag{1.3}
\]

The complete flat individual-incidence signature is

\[
\begin{aligned}
 A_W(c)&=\bigcup_{p\in c}E_p(W),\\
 M_W(c)&=\bigcup\{\{z\}:R_{i,z}(W)\subseteq c\},          \tag{1.4}
\end{aligned}
\]

together with the inclusion-minimal members of
`{E_p(W):p in c}` not already hit by `M_W(c)`.  A target `S` is individually
incident to `c` exactly when it is contained in `A_W(c)`, contains
`M_W(c)`, and hits every remaining minimal envelope.

Let `W^0` be either untwisted phase and let `W^*` be the corresponding
twisted phase.  If `m` is the position of `C_(f_1)` in `W^0`, then

\[
                   (W_m^0,W_{m+1}^0)
          =(C_{f_1},C_{f_2}),\qquad
                   (W_m^*,W_{m+1}^*)
          =(C_{f_2},C_{f_1}).                              \tag{1.5}
\]

All fixed core and active labels are suppressed.

### Lemma 1.1 (two changed maximal envelopes)

The maximal erosions of `W^0,W^*` agree except possibly at

\[
                              p=m,\qquad p=m+d+1.          \tag{1.6}
\]

Only the coordinates `f_1,f_2` can differ there.  Their local projections,
writing `12` for `{f_1,f_2}`, are

\[
\begin{array}{c|ccccc}
 p&m-1&m&m+1,\ldots,m+d&m+d+1&m+d+2\\ \hline
 W^0&12&2&\varnothing&1&12\\
 W^*&12&1&\varnothing&2&12.
\end{array}                                                \tag{1.7}
\]

#### Proof

Owner `W_i` contributes to exactly the envelope positions
`i,...,i+d`.  The coverage intervals of positions `m,m+1` have symmetric
difference `{m,m+d+1}`.  At every other envelope position either both
swapped coatoms occur in the intersection or neither occurs, so their order
is irrelevant.  The two coatoms differ only on `f_1,f_2`.

At `m-1` the erosion window ends immediately before the two omissions; at
`m+d+2` it starts immediately after them.  The planted screens omit only
the two extreme fillers, not `f_1,f_2`.  Hence both fillers occur at those
two positions.  Between the two exceptional endpoints, every erosion
window contains both omission coatoms and hence contains neither filler.
This gives (1.7).  \(\square\)

### Theorem 1.2 (exact `2d+2` individual-incidence footprint)

Let

\[
 \mathcal D_h(m)=\{s:\Gamma_{W^0}([s,s+h))
                         \ne\Gamma_{W^*}([s,s+h))\}.        \tag{1.8}
\]

Then

\[
\boxed{
\begin{aligned}
 \mathcal D_1(m)&=\{m-1,m,m+d+1,m+d+2\},\\
 \mathcal D_h(m)&=\{m,m+d+2-h\},\qquad 2\le h\le d.
\end{aligned}}                                               \tag{1.9}
\]

Consequently

\[
                  \sum_{h=1}^d|\mathcal D_h(m)|
                       =4+2(d-1)=2d+2.                       \tag{1.10}
\]

For the planted packet, the zero-based positions are

\[
             m_{old}=6(d+3)+1=6d+19,
       \qquad m_{new}=5(d+3)+1=5d+16.                        \tag{1.11}
\]

An exterior owner offset or padding amount `a` adds `a` to every start in
(1.9)--(1.11).

#### Proof

Only `f_1,f_2` need be checked.  Substitute the five local regimes in
(1.7) into (1.4).

For `h>=2`, a cell meeting `E_m` but starting before `m` also contains
`E_(m-1)`, whose filler projection is `12`; this masks the transposition in
the allowed mask, and the complete-carrier and minimal-hit rows agree.
Thus the left exceptional cell is exactly the cell starting at `m`.
Symmetrically, a cell meeting `E_(m+d+1)` but ending after it contains
`E_(m+d+2)` and is unchanged.  The right exceptional cell is the one ending
at `m+d+2`, namely the start `m+d+2-h`.

For `h=1`, the two changed envelopes give starts `m,m+d+1`.  In addition,
moving the complete `f_1` and `f_2` occurrence carriers across the two cuts
changes the mandatory mask of the adjacent singleton cells at
`m-1,m+d+2`.  No other carrier endpoint changes a singleton signature.
The complete changed-cell table, projected to `{f_1,f_2}`, is

```text
width/start          A^0  M^0   A^*  M^*
1, m-1               12   12    12    2
1, m                  2    2     1    1
1, m+d+1              1    1     2    2
1, m+d+2             12   12    12    1
2 <= h <= d, m        2    2     1    1
2 <= h <= d,
  m+d+2-h             1    1     2    2
```

The other-coordinate projections agree, and the reduced minimal-hit family
is empty on every listed cell.  At every unlisted start the allowed mask,
mandatory mask, and reduced minimal-hit family are identical.  This proves
(1.9).  Finally, every block
has `d+2` owners and every preceding block contributes one screen, so block
`j` starts at `j(d+3)`.  `Ica` has block index six in the old active word
and five in the new active word, while the first transposed owner has local
index one.  This proves (1.11).  \(\square\)

The theorem concerns the complete marginal predicate `Gamma`.  Restricting
the target ranks can only remove changed marginal edges.  More importantly,
the exact common-cap compiler is a disjunction over legal cap states; its
conflict clutter can change even when the marginal neighbour sets outside
(1.9) do not.  Thus (1.10) is not an `ell` bound and supplies no `alpha`
bound.

## 2. Exact state-optimized `ell-alpha` criterion

Let `T^- -> T^+` be the breaker, a multi-packet twist, or any terminal safe
transition.  Identify the fixed lower-obligation shore `L` and physical-cell
shore `C`, and assume both carriers have at least one legal complete cap
state.  For a legal complete cap state `theta`, let `G_theta(T)` be the
address-labelled bipartite incidence graph and put

\[
 \delta_\theta(T)=|L|-\nu(G_\theta(T)),\qquad
 \lambda(T)=\min_{\theta\in\Theta(T)}\delta_\theta(T).       \tag{2.1}
\]

### Theorem 2.1 (optimization over the new cap state)

Choose an old optimizing state `theta^-` and a maximum matching `M` of
`G_(theta^-)(T^-)`, so `|L|-|M|=lambda(T^-)`.  For each legal new state
`theta^+`, delete from `M` every edge absent from `G_(theta^+)(T^+)`.  Call
the remaining matching `M_0(theta^+)` and put

\[
 \ell(\theta^+)=|M|-|M_0(\theta^+)|.                         \tag{2.2}
\]

Let `alpha(theta^+)` be the maximum number of pairwise vertex-disjoint
`M_0(theta^+)`-augmenting paths in `G_(theta^+)(T^+)`.  Then

\[
\boxed{
 \lambda(T^+)-\lambda(T^-)
   =\min_{\theta^+\in\Theta(T^+)}
       \bigl(\ell(\theta^+)-\alpha(\theta^+)\bigr).}          \tag{2.3}
\]

In particular,

\[
\begin{aligned}
 \lambda(T^+)\le\lambda(T^-)
 &\Longleftrightarrow
 \exists\theta^+\in\Theta(T^+):\alpha(\theta^+)\ge\ell(\theta^+),\\
 \lambda(T^+)<\lambda(T^-)
 &\Longleftrightarrow
 \exists\theta^+\in\Theta(T^+):\alpha(\theta^+)>\ell(\theta^+).
                                                               \tag{2.4}
\end{aligned}
\]

Thus (2.4) is the weakest exact one-transition linkage condition.  Requiring
`theta^+=theta^-` to be legal on both carriers is a stronger fixed-common-
state certificate, not a necessity.

#### Proof

For a fixed `theta^+`, the symmetric difference of `M_0(theta^+)` with a
maximum matching of the new graph contains exactly

\[
 \nu(G_{\theta^+}(T^+))-|M_0(\theta^+)|
\]

pairwise vertex-disjoint `M_0`-augmenting paths.  Conversely, augmenting on
any vertex-disjoint family increases the matching by its cardinality.
Hence

\[
 \nu(G_{\theta^+}(T^+))=|M|-\ell(\theta^+)+\alpha(\theta^+).
\]

Subtract `|L|-|M|=lambda(T^-)` from the new state deficiency and minimize
over all legal new states.  This gives (2.3), and (2.4) follows. \(\square\)

For a prepared twist it is enough to apply Theorem 2.1 directly from the
initial carrier to the terminal carrier; no intermediate compiler state is
required.  A full labelled compiler-structure isomorphism is a convenient
way to force `ell=0`, but it is much stronger than (2.4).  Equality of lower
occurrence counters or full quadratic span does not even imply that one
augmenting path exists.

## 3. Smallest literal counterexample

Take two source positions `0,1` with maximal pinned envelopes

\[
                   \bar E_0=\bar E_1=T=\{o,a,x\}.              \tag{3.1}
\]

Protect the two-position row by requiring the final cap word to satisfy

\[
                              A_0\cup A_1=T.                    \tag{3.2}
\]

Use the two singleton cells `c_0={0},c_1={1}` and the two lower targets

\[
                              S_0=\{o\},\qquad S_1=\{o,x\}.    \tag{3.3}
\]

### Proposition 3.1 (marginal `K_(2,2)` but no common-cap matching)

Every one of the four incidences `S_i ~ c_j` is individually exact, so the
marginal incidence graph is `K_(2,2)` and contains both perfect matchings.
Their difference is the elementary four-cycle/Pluecker relation.  However,
no legal complete cap state contains a perfect matching.  The exact
common-cap matching rank is one and the deficiency is one.

#### Proof

For one selected incidence `S_i~c_j`, set `A_j=S_i` and leave the other
position at `T`.  The selected singleton cell is exactly `S_i`, all source
letters are nonempty, and (3.2) holds.  Hence every marginal edge is exact.

A perfect matching assigns `S_0,S_1` to the two positions in some order.
The coordinatewise largest cap word compatible with that selection is
therefore `(S_0,S_1)` in some order, whose protected union is

\[
                              S_0\cup S_1=\{o,x\}\ne T.
\]

The protected coordinate `a` is lost, and decreasing either cap cannot
restore it.  Thus neither perfect matching belongs to a legal common state.
One edge is feasible, so the exact rank is one. \(\square\)

This is shore-minimal: a nonzero matching four-cycle requires at least two
targets and two cells.  Therefore neither the breaker's alternating
quadratic square nor the twisted cube's coefficientwise occurrence
cancellation implies compiler linkage.  The missing datum is precisely the
state-coexistent augmenting linkage in (2.4).

## 4. Consequence for the breaker catalogue

The adjacent-order breaker removes the common-order reflected quadratic
invariant and changes only `2d+2` marginal compiler columns per phase.  What
it does **not** provide is a sign for terminal `lambda`:

1. the old and new `Ica` footprints are at the distinct addresses (1.11);
2. the changed cells can destroy old matched edges, contributing `ell`;
3. their new edges improve the compiler only when they enter disjoint
   augmenting paths, contributing `alpha`; and
4. all chosen edges must coexist in one legal new complete cap state.

Accordingly, a rigorous breaker/twist actuator theorem must prove (2.4), or
a stronger transparent address transport implying it.  Quadratic span,
point-degree balance, equal unaddressed counters, and marginal Hall in the
union over cap states are insufficient.

## 5. Dependency-free replay

The standard-library-only replay reconstructs both planted phases, checks
the complete individual-incidence signatures for every `2<=d<=32`, and
exhausts the literal two-target/two-cell common-cap example:

```text
scratch/audit_coatom_order_breaker_compiler_footprint_and_linkage_20260801.py
scratch/coatom_order_breaker_compiler_footprint_and_linkage_20260801.audit.json
```

It reports

```text
PASS_COATOM_ORDER_BREAKER_COMPILER_FOOTPRINT_AND_LINKAGE
```

with canonical payload SHA-256

```text
3d9d14fa6b9a2f769f21e09917b0f988bb364eb31eb405cf8f3be9fb52de6b1c
```
