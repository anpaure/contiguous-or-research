# Multistage shadow extension from the depth-one cloned matching

## Verdict

Let

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q},\qquad
 \rho_q=N_q/W.                                             \tag{0.1}
\]

`ASYMPTOTIC_MATCHING.md` proves a `W+o(W)` middle row with complete
two-sided depth-one shadows.  `FIXED_DEPTH_SHADOWS.md` extends this to every
fixed depth.  Neither result currently extends, by iteration or by a known
matching theorem, to

\[
 H/\sqrt m\longrightarrow\infty.                            \tag{0.2}
\]

The obstruction is now quite precise.

* At each **individual** depth, the natural positional-clone hypergraph has
  exceptionally small codegrees.  For fixed `q`, an almost-perfect marginal
  matching follows from the ordinary nibble.
* These marginal matchings have no reason to overlap by shifts.  Positive
  overlap, rather than pair codegree, is the missing condition needed to put
  their windows into one word.
* If one instead keeps the already assembled depth-one forest, its induced
  depth-`q` shadow graph has average degree only `1+O(q^2/m)` in the shallow
  range.  Almost every target occurrence is forced.  Generic expansion,
  Poisson coverage, and a macroscopic absorber reservoir are therefore the
  wrong models.
* A direct conflict-free extension fails the exact
  `Delta_(2q,q)` hypothesis, as proved in `FIXED_DEPTH_SHADOWS.md`.
* An `o(1)` relative defect in the whole central band is not enough: the band
  has `Theta(W sqrt(m))` vertices and the permitted total repair is only
  `o(W)`.

This note derives the exact marginal degrees and codegrees, the exact
component/duplicate/Hall defect ledger, and the switch and absorber budgets.
It ends with a strictly weaker successor lemma than the nested-SCD theorem:
the matchings at different depths need not be nested.  Proving that lemma is
enough for `nu(2m)=W+o(W)`.

No growing-depth construction is claimed here.

## 1. The positional-clone hypergraph at one depth

Write `(x)_q=x(x-1)...(x-q+1)`.  A directed Johnson path

\[
 P=(X_0,X_1,\ldots,X_q)                                  \tag{1.1}
\]

is geodesic if every transition removes a new element of `X_0` and inserts a
new element outside `X_0`.  Equivalently,

\[
 L(P):=\bigcap_{i=0}^qX_i\in\binom{[2m]}{m-q},\qquad
 U(P):=\bigcup_{i=0}^qX_i\in\binom{[2m]}{m+q}.             \tag{1.2}
\]

Define the `(q+3)`-uniform hypergraph `Q_q` with vertex classes

\[
 \mathcal L_q,\quad\mathcal U_q,\quad
 \mathcal M^0,\ldots,\mathcal M^q,                       \tag{1.3}
\]

where the last `q+1` classes are positional clones of the middle layer.  A
directed geodesic path contributes the edge

\[
 \{L(P),U(P),X_0^0,\ldots,X_q^q\}.                       \tag{1.4}
\]

There are exactly

\[
 |E(Q_q)|=W(m)_q^2                                      \tag{1.5}
\]

edges: choose `X_0`, an ordered list of `q` removed elements, and an ordered
list of `q` inserted elements.

### Theorem 1 (exact marginal degrees)

Every lower or upper target has degree

\[
 D_T=(m+q)_{2q}=(m)_q(m+1)_q,                            \tag{1.6}
\]

and every positional middle clone has degree

\[
 D_M=(m)_q^2.                                           \tag{1.7}
\]

Consequently

\[
 \frac{D_T}{D_M}=\frac1{\rho_q}.                        \tag{1.8}
\]

#### Proof

Fix `L`.  Choose the `2q` elements of `U-L` from the `m+q` elements outside
`L`; after that, choose and order the `q` initially present elements and the
`q` inserted elements.  This gives

\[
 \binom{m+q}{2q}(2q)!=(m+q)_{2q}.
\]

The upper calculation is complementary.  The symmetric group is transitive
on each positional middle class, so (1.5), divided by `W`, gives (1.7).
Finally

\[
 \rho_q=\frac{(m)_q}{(m+1)_q},
\]

which proves (1.8).  QED.

### Theorem 2 (exact pair codegrees)

The only nonzero pair codegrees, apart from symmetric copies, are:

\[
\begin{array}{c|c|c}
\text{pair}&\text{compatibility}&\text{codegree}\\ \hline
L,U&L\subset U&(2q)!\\
L,X^t&L\subset X&(m)_q q!\\
U,X^t&X\subset U&(m)_q q!\\
X^s,Y^t&s<t,\ d_J(X,Y)=t-s=d&(m-d)_{q-d}^2(d!)^2.
\end{array}                                                   \tag{1.9}
\]

In particular, relative to the minimum degree `D_M`, the three possible
ratios are

\[
 \frac{(2q)!}{(m)_q^2},\qquad
 \frac1{\binom mq},\qquad
 \frac1{\binom md^2}.                                    \tag{1.10}
\]

Thus

\[
 \frac{\Delta_2(Q_1)}{D_M}=\frac1m,qquad
 \frac{\Delta_2(Q_q)}{D_M}=O(m^{-2})\qquad
 (2\le q=o(m)).                                           \tag{1.11}
\]

#### Proof

For fixed `L subset U`, the `2q` elements of `U-L` may be placed in the
ordered removal and insertion lists in `(2q)!` ways.

Fix `L subset X` and position `t`.  Partition the `q` elements of `X-L`
according to whether they were initially present or already inserted, choose
the complementary `q` active elements outside `X`, and order both halves.
The resulting count is independent of `t` and equals

\[
 \binom mq(q!)^2=(m)_q q!.
\]

Finally fix `X` at position `s` and `Y` at position `t`, with `d=t-s`.
Geodesicity forces `d_J(X,Y)=d`.  The `d` swaps between them may be ordered in
`(d!)^2` ways.  The `q-d` swaps before and after this fixed segment use
disjoint elements of the `m-d` common and `m-d` outside coordinates, giving
`(m-d)_(q-d)^2` choices.  Division by (1.7) gives (1.10).  For
`2<=q=o(m)`, the first ratio is exponentially small in `q` once `q` grows,
the second is at most `2/(m(m-1))`, and the third is maximized at `d=1`.
QED.

The formulas were exhaustively checked for all `m<=4` and all `q<=m` by
direct enumeration of every directed geodesic path.

### Corollary 3 (every fixed marginal depth is easy)

For each fixed `q`, `rho_q=1+O_q(1/m)`, the uniformity `q+3` is fixed, and
(1.11) is `o(1)`.  The Pippenger--Frankl--Rodl theorem therefore gives a
matching in `Q_q` of size

\[
 N_q-o_q(W)=W-o_q(W).                                    \tag{1.12}
\]

It consists of geodesic depth-`q` windows with distinct lower shadows,
distinct upper shadows, and no repeated middle set in any fixed positional
role.

This is only a **marginal** theorem.  It does not produce one middle word.

## 2. The shift-overlap obstruction

For a geodesic `q`-window, call

\[
 (X_0,\ldots,X_{q-1})\quad\text{its prefix history},\qquad
 (X_1,\ldots,X_q)\quad\text{its suffix history}.           \tag{2.1}
\]

Two selected windows can be consecutive in one word only when the suffix
history of the first equals the prefix history of the second.  There are

\[
 H_{q-1}=W(m)_{q-1}^2                                    \tag{2.2}
\]

directed geodesic histories of `q-1` transitions.

Given a matching `M subset Q_q`, form its shift graph `Sigma(M)`: its vertices
are the selected windows and `P->P'` when the suffix of `P` is the prefix of
`P'`.  Every assembly of the selected windows into words is a path/cycle
packing in `Sigma(M)`.  If such a packing uses `a` shift adjacencies, it has
at least `|M|-a` components.

The ordinary nibble controls intersections of hyperedges; it supplies no
lower bound on `a`.  In the uniform independent-history benchmark,

\[
 \mathbb E a\asymp\frac{|M|^2}{H_{q-1}}
 =\frac{W}{(m)_{q-1}^2}\quad(|M|\asymp W).             \tag{2.3}
\]

Already for `q=2`, this is only `Theta(W/m^2)`, whereas one word needs
`W-o(W)` shift adjacencies.  Equation (2.3) is a benchmark rather than a
statement about every nibble output, but it identifies the missing positive
constraint exactly.  Post-processing independent marginal matchings cannot
be justified by pair-codegree estimates.

Equivalently, a word is not an arbitrary matching of `Q_q`; it is a
shift-closed matching.  If `f` denotes its middle successor map, its selected
windows must be

\[
 (X,fX,\ldots,f^qX),                                    \tag{2.4}
\]

and hence obey the de-Bruijn-type recurrence described in
`PARTIAL_BLOCK_MULTISCALE.md`.  This is the same positive constraint that
appears as shift compatibility of SCD flags.

Cloning the rank targets can balance the scalar degree ratio (1.8) at large
`q`: one gives each target approximately `W/N_q` occurrence clones.  It does
not create any of the shift adjacencies (2.1).  Target cloning therefore
removes degree imbalance but not the assembly obstruction.

## 3. What the depth-one forest supplies

Let `F` be a spanning linear forest on the `W` middle sets.  Write its path
orders as

\[
 P_1,\ldots,P_c,qquad |V(P_i)|=v_i.                       \tag{3.1}
\]

Suppose its number of edges is

\[
 |E(F)|=N_1-e.                                           \tag{3.2}
\]

Since

\[
 K:=W-N_1=\frac{W}{m+1}=\operatorname{Cat}_m,             \tag{3.3}
\]

the number of components is exactly

\[
 c=W-|E(F)|=K+e.                                         \tag{3.4}
\]

The number of internal subpaths of `q` transitions is

\[
 P_q(F)=\sum_{i=1}^c(v_i-q)_+
       =W-\sum_{i=1}^c\min(v_i,q)
       \ge W-qc.                                         \tag{3.5}
\]

There is a useful exact binomial comparison.

### Lemma 4 (the Catalan component loss fits the rank shrinkage)

For every `1<=q<=m`,

\[
 \rho_q\le1-\frac{q}{m+1},qquad
 N_q\le W-qK.                                           \tag{3.6}
\]

Consequently

\[
 P_q(F)\ge N_q-qe.                                      \tag{3.7}
\]

#### Proof

The first assertion is equality for `q=1`.  If it holds at `q-1`, multiply
by

\[
 \rho_q/\rho_{q-1}=\frac{m-q+1}{m+q}.
\]

The desired induction step reduces, after cancelling the positive factor
`m+1-q`, to `m+2-q<=m+q`, which holds.  Equations (3.3)--(3.5) then give
(3.7).  QED.

Thus the unavoidable `K` components of an exact depth-one rainbow forest do
**not** create a slot-count obstruction at greater depths.  Their `qK` lost
boundary windows are already paid for by the decrease from `W` to `N_q`.
Only the extra depth-one deficit `e` contributes the worst-case shortage
`qe`.

Summed through depth `H`, this elementary capacity loss is at most

\[
 e\sum_{q=1}^Hq=\frac{eH(H+1)}2.                         \tag{3.8}
\]

Hence the rate-free statement `e=o(W)` in `ASYMPTOTIC_MATCHING.md` is not
uniformly strong enough for (0.2).  The forest count alone would need

\[
 e=o(W/H^2)                                              \tag{3.9}
\]

unless additional connectors or a favourable component-size distribution
recover the lost windows.

When `e=0` and all components are at least `q+1` vertices long, the raw
surplus of internal windows over targets is

\[
 S_q=W-qK-N_q
    =W\left(1-\frac q{m+1}-\rho_q\right).                \tag{3.10}
\]

For `q=o(sqrt(m))`,

\[
 S_q=\left(q^2-q+o(q^2+1)\right)\frac Wm.                \tag{3.11}
\]

This small surplus is the complete flexibility budget available at shallow
depth.

## 4. Geodesicity is a genuinely new condition at depth three

The two-sided depth-one rainbow property automatically makes every two-edge
subpath geodesic.  If consecutive swaps are `a->b` and `c->d`, then `c=b`
repeats the lower edge colour and `d=a` repeats the upper edge colour.

It does not imply depth-three geodesicity.  For example, starting from

\[
 X_0=\{a,c,e\}
\]

perform

\[
 a\mapsto b,\qquad c\mapsto d,\qquad b\mapsto f.          \tag{4.1}
\]

The three lower edge colours are

\[
 \{c,e\},\ \{b,e\},\ \{d,e\},
\]

and the three upper edge colours are also distinct, but `b` is inserted and
then removed inside the three-edge window.  Its intersection and union do
not have the required ranks.

Call a path **H-geodesic** if every subpath of at most `H` transitions is
geodesic.  This is equivalent to saying that no coordinate is changed twice
within `H` transitions.  In particular, every internal positive coordinate
run has length at least `H+1`, exactly the delay-`H` factorability condition.

The depth-one theorem proves neither `H`-geodesicity nor a quantitative
bound on the number of transitions that must be removed to obtain it.

## 5. The exact duplicate-defect ledger

Assume first that `F` is `H`-geodesic.  At depth `q`, each internal `q`-path
gives an edge

\[
 L_q(P)U_q(P)                                             \tag{5.1}
\]

of a bipartite multigraph `Gamma_q(F)` between the rank-`m-q` and
rank-`m+q` target classes.  It has

\[
 E_q=P_q(F)                                               \tag{5.2}
\]

labelled edges.

For either sign, let `mu_q(S)` be the occurrence multiplicity, let

\[
 M_q=N_q-|\{S:\mu_q(S)>0\}|                              \tag{5.3}
\]

be the number of missing targets, and let

\[
 D_q=\sum_S(\mu_q(S)-1)_+                                \tag{5.4}
\]

be the linear duplicate excess.

### Lemma 5 (exact defect identity)

For each sign and depth,

\[
 \boxed{\quad M_q=D_q-(E_q-N_q).\quad}                   \tag{5.5}
\]

#### Proof

If `C_q=N_q-M_q` targets occur, then

\[
 D_q=\sum_{\mu_q(S)>0}(\mu_q(S)-1)=E_q-C_q
    =E_q-N_q+M_q.
\]

QED.

Thus the exact all-depth objective on one assembled forest is

\[
 \sum_{q=1}^H\sum_{\epsilon\in\{-,+\}}
 \left[D_q^\epsilon-(E_q-N_q)\right]=o(W).              \tag{5.6}
\]

This is the correct linear energy.  Quadratic collision energy is impossible
in the outer central band because multiplicities much larger than two are
then forced.

If some internal windows are non-geodesic, let `B_q` be their number and put
`E_q=P_q(F)-B_q`; identity (5.5) remains exact for the remaining correct-rank
windows.  From (3.7), their pure capacity shortage is at most

\[
 (N_q-E_q)_+\le qe+B_q.                                 \tag{5.7}
\]

Therefore any proposed extension must also control

\[
 eH^2+\sum_{q<=H}B_q.                                   \tag{5.8}
\]

## 6. The independent-depth matching certificate

Let

\[
 \kappa_q=N_q-\nu(\Gamma_q(F)),                          \tag{6.1}
\]

where `nu` is maximum matching size.  A matching of size `N_q-kappa_q`
certifies that at least that many lower and upper targets occur.  Hence

\[
 M_q^-,M_q^+\le\kappa_q.                                \tag{6.2}
\]

The matchings used for different `q` need not be nested.  This is strictly
weaker than the nested-radius/SCD normal form in `MSW_ATOM_FLOW.md` and is all
that OR coverage asks for.

The graph is nevertheless almost degree one in the shallow range.  If `z_q`
vertices on one side are isolated, then

\[
 \sum_{\deg(v)>0}(\deg(v)-1)=E_q-N_q+z_q.                \tag{6.3}
\]

Consequently

\[
 |\{v:\deg(v)>=2\}|\le E_q-N_q+z_q.                     \tag{6.4}
\]

When `M_q=z_q=o(W)` and `q=o(sqrt(m))`, (3.10)--(3.11) show that only
`O(q^2W/m)+o(W)` targets on either side can have a second occurrence.  Almost
every occurrence is forced.

This is why a random sparse graph is the wrong extension model.  Its mean
degree is approximately one and the Poisson benchmark leaves an
`e^(-1)+o(1)` isolated fraction.  The desired graph must be deliberately
organized as a near-permutation, not merely be expanding on average.

## 7. Exact rigidity of the nested matching route

The nested construction in `MSW_ATOM_FLOW.md` is stronger but gives an even
sharper audit.  Suppose the previous certified set has exactly `N_(q-1)`
starts.  The depth-`q` extension graph has `N_q` vertices on either side and
exactly `N_(q-1)` labelled edges.  Put

\[
 \Delta_q=N_{q-1}-N_q,\qquad
 \frac{\Delta_q}{N_q}=\frac{2q-1}{m-q+1}.                \tag{7.1}
\]

If the graph has a perfect matching, then at most `Delta_q` vertices on
either side have degree at least two.  Moreover, any two perfect matchings
differ on at most `Delta_q` matched edges.

Indeed, the sum of `deg(v)-1` on either side is exactly `Delta_q`.  Every
vertex at which two perfect matchings differ has degree at least two.

Thus a shallow exact extension contains only `O(qW/m)` vertices at which the
matching choice can change.  There is no linear-size absorber reservoir.

For an approximate tower, suppose the previous set has
`N_(q-1)-d_(q-1)` starts and the chosen depth-`q` matching has size
`N_q-d_q`.  Pure edge capacity gives

\[
 d_q\ge(d_{q-1}-\Delta_q)_+.                             \tag{7.2}
\]

Define the additional Hall loss by the exact recurrence

\[
 d_q=(d_{q-1}-\Delta_q)_++h_q,qquad h_q\ge0.             \tag{7.3}
\]

Then, crudely but usefully,

\[
 \sum_{q=1}^H d_q
 \le Hd_0+\sum_{q=1}^H(H-q+1)h_q.                       \tag{7.4}
\]

An unweighted assertion `h_q=o(W)` at every stage is therefore insufficient.
The Hall losses must satisfy a cumulative `o(W)` budget, and the choice of a
perfect matching at one stage controls every later `h_q`.

This proves that sequential Hall is an exact formulation, not a generic
rounding theorem.  Near-unit mean degree leaves almost no freedom with which
to correct a bad earlier choice.

## 8. Local switching and absorption budgets

### Lemma 6 (multistage switch locality)

Re-splicing fixed path blocks so that `s` adjacency transitions change
changes at most `qs` old depth-`q` windows
and at most `qs` new depth-`q` windows.  It can newly cover at most `qs`
targets of either sign.  Summed through depth `H`, the improvement in the
two-sign missing count is at most

\[
 2s\sum_{q=1}^Hq=sH(H+1).                               \tag{8.1}
\]

In particular, repairing `cW` missing targets at one fixed shallow depth
`q` requires `Omega(W/q)` changed transitions.  A depth-two constant-density
defect cannot be repaired by an `o(W)` local switch phase.

#### Proof

A fixed transition belongs to at most `q` windows of `q` transitions.  Take
a union bound over the changed transitions in the old and new rows.  QED.

Absorption has the same shallow scarcity.  A target can support two
alternative representatives only if its multiplicity is at least two.  By
(5.5)--(6.4), the number of such targets at depth `q=o(sqrt(m))` is at most

\[
 E_q-N_q+M_q=O(q^2W/m)+M_q                              \tag{8.2}
\]

in the ideal component regime.  Hence a bounded-size target-rooted absorber
system has at most this many disjoint roots.  It can clean an already small
defect; it cannot convert a Poisson-scale `Theta(W)` miss into a near-rainbow
layer.

## 9. Why the four proposed mechanisms stop

### 9.1 Cloned hypergraphs

The exact counts (1.6)--(1.11) show that marginal degree and codegree are
excellent.  For fixed `q`, Corollary 3 solves the marginal matching problem.
For growing `q`, target occurrence clones can also correct the scalar ratio
`1/rho_q`.

What cloning does not encode is the positive shift equation (2.1).  The
prefix/suffix history space is larger than the selected family by a factor
`(m)_(q-1)^2`.  A generic marginal matching is therefore not stitchable.

### 9.2 Conflict-free matching on the depth-one edges

`FIXED_DEPTH_SHADOWS.md` proves the exact obstruction.  After fixing all `q`
arcs of one geodesic path with lower shadow `S`, there remain
`Theta_q(D^q)` disjoint geodesic `q`-paths with the same `S`.  Thus

\[
 \Delta_{2q,q}\ge c_qD^q,                                \tag{9.1}
\]

while the Delcourt--Postle theorem needs `D^(q-beta)`.  Adding deeper colour
collisions as forbidden configurations cannot extend the depth-one proof.

### 9.3 Alternating switches and absorption

Lemma 6 makes a fixed shallow defect expensive, while (8.2) bounds the
number of shallow absorber roots.  These tools are suitable only after the
near-permutation structure has been built globally.

### 9.4 Nested bipartite matchings

The formulation is exact, but (7.1) says that almost every shallow edge is
forced.  Ordinary expansion has essentially no margin, and stagewise
`o(W)` errors accumulate according to (7.4).  Furthermore nesting is stronger
than OR coverage: independent matchings in the already assembled graphs
`Gamma_q(F)` suffice by (6.2).

## 10. Relation to partial blocks and the atom-flow program

`FIXED_DEPTH_SHADOWS.md` packages an entire cyclic pair-flip block as one
fixed-uniformity hyperedge.  This bypasses (9.1) and proves every fixed depth.
`PARTIAL_BLOCK_MULTISCALE.md` gives its growing-depth fractional form.

For a physical block of length `R=2ell`, the middle-only relative pair
codegree is at most

\[
 2/m^2.                                                   \tag{10.1}
\]

Once the shallow shadow classes are included, a middle/facet pair restores
the worst relative codegree to order `1/m`.  More importantly, the radius
typed edge has average size

\[
 R\left(1+2\sum_{q<=H}\rho_q\right)
 =(\sqrt\pi+o(1))R\sqrt m,                               \tag{10.2}
\]

and maximum size `R(1+2H)`.

The complete central band contains

\[
 W+2\sum_{q=1}^HN_q=\Theta(W\sqrt m)                    \tag{10.3}
\]

vertices once `H/sqrt(m)->infinity`.  A matching theorem leaving merely an
`o(1)` fraction of this hypergraph uncovered may leave `o(W sqrt(m))`
targets, much more than the `o(W)` repair budget.  The required relative
error is

\[
 o(1/\sqrt m).                                           \tag{10.4}
\]

The typed fractional matching closes all degree and divisibility equations,
but neither (10.1) nor a standard almost-perfect matching theorem supplies
(10.4) together with shift overlap.

The atom-flow theorem reaches the same conclusion from the other side:
successive exact graphs have mean degree `1+O(q/m)` and are almost
bijections.  The difficulty is coherent near-bijectivity, not fractional
mass.

## 11. The weakest sufficient extension lemma

Choose

\[
 H/\sqrt m\longrightarrow\infty,qquad H=o(m^{2/3}),       \tag{11.1}
\]

slowly enough for the tail construction in `TRUNCATED_IDEAL_PRODUCT.md`.

### Conjecture A (low-collision `H`-geodesic forest)

There is a spanning linear forest `F_m` of middle sets such that:

1. `F_m` is `H`-geodesic;
2. if `c_m` is its number of components, then
   \[
   Hc_m=o(W);                                             \tag{11.2}
   \]
3. its actual missing shadows satisfy
   \[
   \sum_{q=1}^H(M_q^-(F_m)+M_q^+(F_m))=o(W).             \tag{11.3}
   \]

This is the literal weakest row-level statement needed by the erosion
construction.

For matching-based work, the following stronger but independently checkable
version is enough.

### Conjecture B (independent-depth matching extension)

Under (1)--(2), the induced shadow graphs satisfy

\[
 \boxed{\qquad\sum_{q=1}^H\kappa_q(F_m)=o(W).\qquad}      \tag{11.4}
\]

No nesting of the matchings witnessing `kappa_q` is required.

### Theorem 7 (either extension lemma gives asymptotic optimality)

Conjecture A implies

\[
 \nu(2m)=W+o(W).                                         \tag{11.5}
\]

Conjecture B implies Conjecture A by (6.2), so it has the same consequence.

#### Proof

Treat every path component separately.  `H`-geodesicity implies that every
internal positive coordinate run has length at least `H+1`, so the maximal
delay-`H` factor exists on that component.  Factoring a component of `v`
middle states costs `v+H` entries.  Summing over the components gives

\[
 W+Hc_m=W+o(W).                                          \tag{11.6}
\]

The erosion identity turns all lower intersection shadows into short OR
windows of the factor; derivative composition turns all upper union shadows
into longer OR windows.  Append every central-band mask missing in (11.3).
This costs `o(W)`.  Under Conjecture B, (6.2) proves (11.3).

Finally append the two truncated-ideal tail words outside the band.  Under
(11.1), `TRUNCATED_IDEAL_PRODUCT.md` gives total tail length `o(W)`.  Delete
any zero factor entries; this preserves every nonzero interval OR.  The final
nonzero word has length `W+o(W)` and covers every nonempty mask.  The Boolean
width lower bound gives the reverse asymptotic inequality.  QED.

If one insists on obtaining `F_m` by deleting edges from the particular
depth-one matching proof, (3.8), (5.7), and (11.2) show the quantitative
targets that proof would have to meet:

\[
 e=o(W/H^2),\qquad
 \sum_{q<=H}B_q=o(W),\qquad
 Hc_m=o(W),                                             \tag{11.7}
\]

followed by the duplicate-excess equality (5.6).  None follows from the
current rate-free `o(W)` theorem.

## 12. Precise next theorem

The depth-one cloned matching should not be treated as a frozen skeleton and
then repaired one rank at a time.  The calculations above point to a joint
construction with the following priorities.

1. Build shift overlap from the outset: select a partial Johnson permutation
   `f`, not independent windows.
2. Enforce `H`-geodesicity as a positive spacing rule on the transition
   labels.
3. Optimize the exact linear energy (5.6), not quadratic collision counts.
4. Use alternating switches and absorbers only on the
   `O(q^2W/m)` shallow flexible core.
5. Prove total defect `o(W)`, not merely relative defect `o(1)` in the
   `Theta(W sqrt(m))` band.

Equivalently, the clean successor theorem is:

> Construct an `H`-geodesic partial permutation of the middle layer whose
> induced bipartite shadow graphs `Gamma_q`, independently at every
> `1<=q<=H`, have cumulative maximum-matching deficiency `o(W)`, and whose
> path/cycle count is `o(W/H)`.

This is weaker than a wreath-resolved SCD and stronger than unrelated cloned
matchings.  It exactly isolates the positive shift structure absent from all
four failed black-box extensions.

## 13. Ledger

### Proved here

* exact one-depth positional-clone degrees (1.6)--(1.8);
* exact pair codegrees (1.9)--(1.11);
* an independent marginal near-perfect matching for every fixed depth;
* the exact shift-history assembly obstruction;
* exact component and internal-window formulas (3.4)--(3.7);
* exact duplicate-defect identity (5.5);
* exact shallow degree-one and nested-choice rigidity;
* exact Hall-defect recurrence (7.3)--(7.4);
* exact multistage switch locality (8.1); and
* the sufficient extension theorem, Theorem 7.

### Not proved

* a common row realizing the marginal matchings;
* `H`-geodesicity at `H/sqrt(m)->infinity`;
* cumulative shadow defect `o(W)` at that depth;
* a growing-uniformity typed matching with absolute defect `o(W)`; or
* the all-`k` exact formula.

The conclusion is therefore negative for post-hoc extension of the current
depth-one theorem, but positive as a reduction: the remaining asymptotic
problem is no longer a nested tower of perfect matchings.  It is the weaker
shift-resolved, independent-depth deficiency bound (11.4).
