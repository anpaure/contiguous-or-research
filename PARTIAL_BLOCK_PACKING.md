# Partial pair-flip blocks: the correct growing-depth Stage A

This note replaces the unnecessarily rigid full `2m`-block in
`RANK_BALANCED_BLOCKS.md` by a partial block of length `2 ell`.  The change is
substantive:

* no two middle vertices are forced to occur together;
* the exact relative pair-codegree is `2/m^2`, rather than a merely coarse
  `O(1/m)` estimate;
* one may choose

  \[
     \sqrt{m\log m}\ll \ell\ll m,
  \]

  so seam padding is `o(W)` while the block rank remains sublinear; and
* Stage A no longer asks for an approximate tight-Hamilton decomposition of
  the complete central uniform hypergraph.

No growing-uniformity matching theorem is claimed here.  The note proves the
exact block geometry and isolates a strictly weaker quantitative matching
lemma which would suffice.

Throughout,

\[
  W=\binom{2m}{m}.
\]

## 1. The partial block

Fix `1 <= ell <= m`.  Choose

* a middle set `S in binom([2m],m)`;
* an ordered `ell`-tuple `a=(a_1,...,a_ell)` of distinct members of `S`; and
* an ordered `ell`-tuple `b=(b_1,...,b_ell)` of distinct members of `S^c`.

Starting at `T_0=S`, perform the transitions

\[
 a_1\to b_1,\ldots,a_\ell\to b_\ell,
 b_1\to a_1,\ldots,b_\ell\to a_\ell.                 \tag{1.1}
\]

The `2 ell` states before the return to `T_0` form the cyclic partial
pair-flip block

\[
 B(S;a,b)=\{T_0,T_1,\ldots,T_{2\ell-1}\}.             \tag{1.2}
\]

All states are distinct.  The active coordinates occur in `ell` disjoint
pairs `{a_i,b_i}`; every inactive member of `S` is present throughout and
every inactive member of `S^c` is absent throughout.

### Lemma 1 (local geodesy and runs)

Every cyclic transition window of length `q<ell` flips `q` different active
pairs.  Consequently

\[
 \left|\bigcap_{j=0}^{q}T_{i+j}\right|=m-q,
 \qquad
 \left|\bigcup_{j=0}^{q}T_{i+j}\right|=m+q,           \tag{1.3}
\]

and, for fixed `q`, the `2 ell` lower colours and the `2 ell` upper colours
in one block are separately distinct.  Every nonconstant coordinate
incidence word has its zero-runs and one-runs of length exactly `ell`.

#### Proof

The two transitions involving one active pair are separated cyclically by
exactly `ell` steps.  A window of fewer than `ell` transitions therefore
meets every pair at most once.  Each transition removes one previously
present coordinate and introduces one previously absent coordinate, giving
(1.3).  Two starts with the same lower or upper colour would force the same
set of crossed active pairs and the same orientation; on this cycle that
forces the same start.  Finally, each active coordinate is present for one
of the two arcs of length `ell` between its two transitions.  QED.

Thus a block supports every derivative depth `q<h` whenever `h<ell`, and it
automatically satisfies the delay-`h` run condition away from seams.

## 2. Exact degree and codegree

Regard the triples `(S;a,b)` as parameterized hyperedges on vertex set
`binom([2m],m)`.  Repeated copies of one unparameterized block are harmless;
all multiplicities are constant by symmetry and may be divided out.

### Theorem 2 (exact local statistics)

The parameterized block hypergraph is `2 ell`-uniform and regular of degree

\[
 D=2\ell\,(m)_\ell^2,                                  \tag{2.1}
\]

where `(m)_ell=m(m-1)...(m-ell+1)`.

Let `X,Y` be two middle sets at Johnson distance

\[
 q=|X\setminus Y|=|Y\setminus X|.
\]

If `1<=q<ell`, their codegree is

\[
 \lambda_q=4\ell\,(q!)^2(m-q)_{\ell-q}^2,             \tag{2.2}
\]

and hence

\[
 \boxed{\frac{\lambda_q}{D}
       =\frac{2}{\binom mq^2}}.                         \tag{2.3}
\]

For `q=ell`,

\[
 \frac{\lambda_\ell}{D}=\frac{1}{\binom m\ell^2},     \tag{2.4}
\]

and for `q>ell` the codegree is zero.  In particular,

\[
 \boxed{\frac{\Delta_2}{D}=\frac{2}{m^2}}              \tag{2.5}
\]

for `1<ell<m`.

#### Proof

Fix a state `X` and one of its `2 ell` cyclic positions.  Looking forward
`ell` transitions, choose the ordered departing coordinates from `X` and the
ordered arriving coordinates from `X^c`; this gives `(m)_ell^2` parameters
and proves (2.1).

Suppose first `q<ell`.  In a block containing `X,Y`, their cyclic positions
are separated by either `q` or `2ell-q` transitions.  Choose the position of
`X` in `2ell` ways and the orientation in two ways.  The `q` coordinates of
`X-Y` and the `q` coordinates of `Y-X` may each be ordered in `q!` ways.  The
remaining active departures and arrivals are ordered choices of `ell-q`
coordinates from the two residual sets of size `m-q`.  This proves (2.2).
Dividing by (2.1) and using

\[
 (m)_\ell=(m)_q(m-q)_{\ell-q},\qquad (m)_q=q!\binom mq,
\]

gives (2.3).  At `q=ell` the two cyclic separations coincide, removing the
factor two.  A block has diameter `ell`, proving the final assertion.  QED.

### Why the full block had a false obstruction

At `ell=m`, every block contains `X^c` whenever it contains `X`; therefore
the unquotiented maximum codegree is `D`.  Quotienting by antipodal pairs
restores relative codegree `2/m^2`, but leaves an `m`-uniform matching
problem.  Partial blocks avoid the twins entirely and allow sublinear rank.

Also, a full block is a tight Hamilton cycle of `K_{2m}^{(m)}`: its states
are the `2m` cyclic intervals of length `m` in an ordering of `[2m]`.  It
should not be called a Katona wreath in the non-coprime case
`gcd(2m,m)=m`; those notions coincide only in the coprime convention used in
the wreath literature.

## 3. The sufficient Stage-A lemma is now weaker

Let `H_{m,ell}` be the simple hypergraph of partial blocks.  A matching which
covers all but `o(W)` middle vertices yields a list of

\[
 \frac{W}{2\ell}+o\left(\frac W\ell\right)             \tag{3.1}
\]

blocks.  Concatenate their cyclic state lists, repair the `o(W)` omitted
middle masks explicitly, and pad each seam by `O(h)` states.  The total seam
cost is

\[
 O\left(\frac{hW}{\ell}\right).                         \tag{3.2}
\]

Consequently any choice

\[
 h\ll\ell\ll m                                           \tag{3.3}
\]

makes the seam cost `o(W)`.  For example,

\[
 h=(1+\varepsilon)\sqrt{m\log m},\qquad
 \ell=m^{3/4}                                             \tag{3.4}
\]

has this property.  At the same time, with block rank `r=2ell`,

\[
 r\frac{\Delta_2}{D}=O\left(\frac\ell{m^2}\right)=o(1),
 \qquad
 r^2\frac{\Delta_2}{D}=O\left(\frac{\ell^2}{m^2}\right)=o(1).  \tag{3.5}
\]

This motivates the exact missing lemma.

### Partial-block matching lemma

If `ell -> infinity` and `ell=o(m)`, then `H_{m,ell}` has a matching covering
`(1-o(1))W` middle vertices.

The lemma is much weaker than an approximate tight-Hamilton decomposition.
Standard Pippenger--Spencer statements fix the edge rank and therefore do not
prove it verbatim.  However, unlike the full-block formulation, the sharp
statistics (2.5) satisfy even the natural `r^2 Delta_2/D=o(1)` scale.  A
quantitative random-greedy theorem specialized to this transitive Boolean
hypergraph is now a credible target.

## 4. Stage B is coverage, not quota matching

A matching of middle blocks is not by itself enough.  For every `q<h`, the
union of the lower `q`-window colours must cover `binom([2m],m-q)` and the
union of the upper colours must cover `binom([2m],m+q)`, up to a total
`o(W)` repair family.

There is no physical quota or Hall coupling between different depths: every
available window may be used, and the same block may supply all of its
windows at every depth.  The exact requirement is therefore

\[
 \sum_{q<h}\left(M_q^-+M_q^+\right)=o(W),               \tag{4.1}
\]

where `M_q^pm` is the number of missing colours at that depth and sign.

For `q=o(sqrt(m))`, a completely unstructured random block family misses a
constant fraction of the `q`-th layer, so Stage B must be built into the
selection.  The fixed-depth block theorem already does this for every fixed
`q`.  The remaining theorem is a two-sided multiscale version, with strong
near-rainbow control for shallow `q` and progressively more collision slack
as

\[
 \rho_q=\frac{\binom{2m}{m-q}}{W}
\]

decays.

Copying the first `h` states after every cyclic block preserves every cyclic
window through depth `h` and costs (3.2).  Hence block cuts introduce no
additional asymptotic coupling.

## 5. Ledger

Proved here:

* exact partial-block geometry and run length;
* exact regular degree and every pair-codegree;
* removal of the antipodal-twin obstruction;
* the `h << ell << m` seam ledger; and
* the strictly weaker Stage-A matching target.

Still missing:

* a quantitative growing-rank near-matching theorem for `H_{m,ell}`;
* a joint selection with summed two-sided shadow deficit `o(W)` through
  `h=Theta(sqrt(m log m))`; and
* the resulting pin-surviving OR factor.

This is nevertheless a real reduction: the earlier full tight-Hamilton
decomposition was stronger than necessary and introduced an avoidable
antipodal codegree obstruction.
