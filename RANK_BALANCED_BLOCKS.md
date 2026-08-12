# Rank-balanced long blocks: an auxiliary exact-once formulation

This note continues `FIXED_DEPTH_SHADOWS.md`.  It does not claim a growing-
depth construction.  It proves the exact rank-capacity law for the auxiliary
formulation in which shadow colours are retained essentially once, an exact
fractional balancing theorem, and a cut-capacity lemma.

The later audit in `SHADOW_SLOT_HALL.md` shows that this is stronger than the
physical OR problem: windows do not consume capacity, so without artificial
per-block quotas Stage B asks only for union coverage.  Moreover,
`PARTIAL_BLOCK_PACKING.md` replaces full `2m` blocks by sublinear partial
blocks and removes their antipodal-twin codegree obstruction.  The calculations
below remain valid as a collision/capacity ledger, but Sections 4--5 are no
longer the preferred theorem target.

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}=\binom{2m}{m+q},
 \qquad \rho_q=N_q/W.                                      \tag{0.1}
\]

Use the pair-flip cycle from `FIXED_DEPTH_SHADOWS.md` with all `m` coordinate
pairs active.  Its length is

\[
 R=2m.                                                       \tag{0.2}
\]

Every cyclic `q`-window, `1<=q<m`, is geodesic and therefore has one lower
colour of rank `m-q` and one upper colour of rank `m+q`.  For fixed `q` the
`R` colours of either kind are distinct within one block.

## 1. The capacity law is forced

Suppose `t` disjoint blocks cover all but `o(W)` middle sets.  Then

\[
 tR=W-o(W).                                                  \tag{1.1}
\]

If the selected depth-`q` windows cover every lower target exactly once up to
`o(W)` omissions and repetitions, the average number `c_q` selected per block
must satisfy

\[
 tc_q=N_q-o(W).
\]

Combining this with (1.1) gives the forced law

\[
 \boxed{c_q=R\rho_q+o(R).}                                  \tag{1.2}
\]

The same law holds independently for upper colours.  In particular, retaining
all `R` windows at every depth is balanced only for fixed `q`; it overfills a
rank by the factor `1/rho_q` when `q` grows.

The total average number of vertices carried by one fully rank-balanced
decorated block is exactly

\[
\begin{aligned}
 r_{\rm bal}
   &=R\left(1+2\sum_{q=1}^{m}\rho_q\right)\\
   &=R\frac{2^{2m}}{W}.                                     \tag{1.3}
\end{aligned}
\]

Indeed

\[
 W+2\sum_{q=1}^{m}N_q=2^{2m}.
\]

By Stirling,

\[
 r_{\rm bal}
   =(2\sqrt\pi+o(1))m^{3/2}.                               \tag{1.4}
\]

Thus the natural all-rank object has growing, but only polynomial, local
complexity.  The equal-occupancy block from the fixed-depth theorem has the
wrong rank profile; (1.2) is the unique correct first-order profile.

## 2. Exact fractional balancing

Let `mathcal B` be the symmetric multiset of all parameterized full pair-flip
blocks.  Every block has `R` middle slots and `R` lower and upper slots at
each depth.  Let `E=|mathcal B|`, counted with parameter multiplicity.
Double counting gives the full-slot degrees

\[
 d_M=\frac{ER}{W},\qquad
 d_q=\frac{ER}{N_q}=\frac{d_M}{\rho_q}.                    \tag{2.1}
\]

Decorate a parameter block by retaining every individual lower and upper
depth-`q` slot independently with probability `rho_q`, while retaining every
middle slot.  Regard all decorations as a weighted edge family, with their
product Bernoulli probabilities as weights.

### Theorem 1 (common fractional degree)

In the weighted decorated-block hypergraph, every vertex in every rank class
has weighted degree exactly `d_M`.

#### Proof

A middle vertex is always retained, so its degree is `d_M`.  A fixed
rank-`m-q` or rank-`m+q` vertex has full-slot degree `d_q`; each occurrence is
retained with probability `rho_q`.  Its decorated degree is therefore

\[
 \rho_qd_q=d_M.
\]

QED.

The expected decorated edge size is precisely (1.3).  Hence all class-size
and degree equations admit a completely symmetric fractional solution.
There is no linear-density obstruction to the rank-balanced construction.
The missing statement is integral: select essentially disjoint decorated
blocks covering essentially every vertex in every class.

Integer counts cause no asymptotic problem.  Across many blocks one may mix
`floor(R rho_q)` and `ceil(R rho_q)` retained slots in the proportions needed
to total `N_q+o(W)`.  What is not automatic is choosing the blocks and the
actual slots without collisions.

## 3. Linear cuts have enough capacity

To turn cyclic blocks into an ordinary sequence, cut each `R`-cycle once.
A depth-`q` window survives without copying a prefix if its start avoids the
last `q` cyclic positions, leaving `R-q` admissible starts.

### Lemma 2 (rank demand fits after a cut)

For every `1<=q<=m-1`,

\[
 R\rho_q\le R-q.                                           \tag{3.1}
\]

#### Proof

Every factor in

\[
 \rho_q=\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}
\]

is at most `m/(m+1)`.  Therefore

\[
 \rho_q\le\left(\frac{m}{m+1}\right)^q.
\]

Using `(1-x)^q<=1/(1+qx)` with `x=1/(m+1)` gives

\[
 1-\rho_q\ge\frac{q}{m+1+q}\ge\frac{q}{2m},
\]

because `q<=m-1`.  Multiplication by `R=2m` proves (3.1).  QED.

Thus the forced average number of designated windows can be placed wholly
away from a chosen cut.  If only depths `q<=h=o(m)` are used, endpoint run
padding of `h` copies per block costs

\[
 O\left(\frac{h}{R}W\right)=o(W).                          \tag{3.2}
\]

Taking `h` on the order of `sqrt(m log m)` also makes the literal masks
outside the central band total `o(W)`.  Consequently neither cyclic
linearization nor raw slot capacity is the growing-depth obstruction.

## 4. Why the fixed-uniformity nibble cannot simply be quoted

For fixed block length, `FIXED_DEPTH_SHADOWS.md` used a fixed-uniformity
Pippenger--Frankl--Rodl theorem.  Here the balanced edge size is
`Theta(m^(3/2))`.  The undecorated full middle-block hypergraph has
uniformity `R=2m`, degree

\[
 D=R(m!)^2
\]

with parameter multiplicity.  In the unquotiented hypergraph complementary
middle sets are forced twins and have codegree `D`.  After quotienting by
antipodal pairs, the exact maximum relative codegree is `2/m^2`.

There is a cleaner growing-band successor.  Replace the full cycle by a
partial pair-flip cycle of length `R=2ell`, where

\[
 h\ll\ell\ll m.
\]

It has no antipodal twins, and its middle-block hypergraph has the exact
parameters

\[
 D=2\ell(m)_\ell^2,
 \qquad \frac{\Delta_2}{D}=\frac2{m^2}.
\]

Thus even `R^2 Delta_2/D=o(1)`.  The exact count, the higher-codegree spread,
and the quantitative theorem audit are proved in `GROWING_NIBBLE.md`.

These numerical facts do not by themselves imply a near-perfect matching
when the uniformity grows.  Fixed-uniformity is essential in the quoted
nibble theorem.  More generally, regularity plus `Delta_2=o(D)` is
insufficient for growing-uniformity hypergraphs (finite projective planes are
the standard warning: they have a perfect fractional matching and small
relative codegree but no large matching).

The sharpened partial-block statistics still do not meet any audited
growing-uniformity black box.  They instead isolate an object-specific
near-factor lemma, or a uniform full-codegree nibble exploiting the entire
pair-flip link sequence, as the missing Stage-A theorem.

## 5. Exact two-stage integral target

The all-rank problem may be separated into two statements.

### Stage A: middle block factor

Find `W/R+o(W/R)` pair-flip blocks whose middle vertex sets are disjoint and
cover all but `o(W)` middle sets.

### Stage B: simultaneous shadow b-matchings

For every `q<=h`, assign to each selected block an integer number of surviving
starts, averaging `R rho_q`, so that the chosen lower colours cover every
rank-`m-q` target and the chosen upper colours cover every rank-`m+q` target,
with only `o(W)` total repair cost.  Equivalently, after Stage A, solve one
capacitated bipartite matching from each shadow layer to the physical
`(block,start)` slots, coupled across ranks only by the common block cuts and
run padding.

The one-stage decorated-hypergraph formulation and this two-stage formulation
have the same capacity ledger.  The two-stage form isolates two possible
proof methods:

* an explicit resolvable decomposition of the middle layer into locally
  geodesic blocks followed by Hall expansion; or
* a growing-uniformity absorption/nibble theorem using the special Johnson
  geometry, not just degree and codegree.

If Stages A and B hold through, for example,

\[
 h=(1+\varepsilon)\sqrt{m\log m}
\]

with `o(W)` loss, the block linearization, run padding, maximal-factor
identity, and literal-tail estimate complete a universal OR sequence of
length `W+o(W)`.  This displayed constant is deliberately nonsharp; the
structural point is the `Theta(sqrt(m log m))` scale.

## 6. Ledger

Proved here:

* the forced rank-dependent capacity (1.2);
* the exact total balanced size (1.3);
* exact symmetric fractional degree balance;
* enough nonwrapping capacity after one cut; and
* the precise two-stage integral target.

Not proved:

* a near-factor of the growing-uniformity middle-block hypergraph;
* simultaneous integral shadow assignments; or
* the resulting all-rank `W+o(W)` OR construction.

The next theorem must be integral and Boolean-specific.  Further fractional
averaging cannot close this gap.
