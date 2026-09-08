# Density-only OR constructions: a bridge frontier and two surviving walls

Date: 2026-09-05. Independent scratch note; no master or index edits.

## 1. Status and relation to the new target

The unrestricted target remains open: no family of words of length
`(1+o(1)) W(k)` with `o(2^k)` literal interval-union holes is constructed
here. In particular, this is not a proof of coefficient one for `nu(k)`.

The positive result is a deterministic family with

\[
 n_k=(1+o(1))W(k),\qquad
 |\mathcal U(A_k)|\ge(p_*+o(1))2^k,                 \tag{1}
\]

where `p_*` is defined by explicit integrals below. Numerical quadrature gives

\[
 p_*\approx0.841485839042.
\]

Thus this improves the `2/pi` cube-density guarantee of the handoff's
narrow-band bridge word, but still has a positive missing fraction. The
decimal is diagnostic; the exact theorem uses the integral definition.

Two density-specific negative results explain why the most direct further
steps do not close the problem:

1. A linear or cyclic word made of full-half fixed-split blocks, even with
   arbitrary internal letters and orders, still needs coefficient at least
   `sqrt(2)` to have vanishing hole density. At coefficient one it misses at
   least `0.125185394217...` of the cube.
2. The unrestricted dominant-product-box endpoint obstruction survives
   density-only coverage. A word of length `(1+o(1))(s+1)^2` in
   `[0,s] x [0,s] x [0,3s]` misses at least `1/216-o(1)` of that box.

The synchronous tensor law is also stated exactly. It does not amplify
independent near-width inputs: balanced fixed-factor products have too few
physical endpoints and cover only a vanishing fraction of the larger cube.

Inputs read include `MASTER_HANDOFF.md`, its main Sections 1--8 and Appendix
A, the expanded 2026-09-05 cylinder-completion note, the product-box and
subcritical-aggregation reductions, the compact three-box endpoint proof,
the audited three/four-box barriers, the two-block FIFO product construction,
the fixed-split Lipski obstruction, and the random nested-schedule and
cool-lex/central-ucycle barriers. No tour selector or punctured process is
used. The cylinder lemma is not reproved.

## 2. A literal selected-pair bridge construction

Let `k=2b`, and split the coordinates as

\[
 P=P_0\mathbin{\dot\cup}\{z\},\quad |P_0|=b-1,
 \qquad |Q|=b.
\]

Take any SCD `C` of `2^{P_0}` and any SCD `D` of `2^Q`. Write

\[
 A=|\mathcal C|=W(b-1),\qquad B=|\mathcal D|=W(b).
\]

For a chain `E_0 < ... < E_{a-1}` in a universe `U`, use the nonzero bridge

\[
 \beta_U(E)=(E_0,E_1\setminus E_0,\ldots,
 E_{a-1}\setminus E_{a-2},U\setminus E_{a-1}),       \tag{2}
\]

with empty entries omitted. It has `a+O(1)` letters and at most `a+1`.
Every chain member is a prefix union and its complement in `U` is a suffix
union. Empty prefixes or suffixes are allowed as parts of a witness, but
the final witnessing interval must be nonempty.

Choose any set `E` of left-right chain pairs. For every chosen pair `(C,D)`,
put both arcs `C -> D` and `D -> C` in a bipartite directed graph. Every
nonisolated connected component is Eulerian. Along an Euler circuit,
output the bridge of the tail of every arc, then one additional copy of
the starting bridge. Do this for each component, with one full-set letter
between successive component words.

If `a=|C|` and `c=|D|`, both of the following complete rectangles are
literally witnessed:

\[
 \{X\cup(Q\setminus Y):X\in C,Y\in D\},\qquad
 \{(P\setminus X)\cup Y:X\in C,Y\in D\}.             \tag{3}
\]

For the first use the suffix `Q\Y` of `beta_Q(D)` followed immediately
by the prefix `X` of `beta_P(C)` across `D -> C`. For the second use the
suffix `P\X` followed by the prefix `Y` across `C -> D`. The appended
starting bridge handles the closing arc. Except for the empty target,
at least one part is nonempty; removing empty bridge letters preserves
contiguity and the displayed unions. No required witness crosses a
component join.

The bit `z` distinguishes the two rectangles. The SCD owners are unique,
so rectangles from different selected pairs are disjoint. Consequently
the intended number of targets, including a possible empty target, is

\[
                         2\sum_{(C,D)\in E}ac.       \tag{4}
\]

This is an actual, not just designated, density census up to `O(2^b)`.
To see this, exclude targets empty or full in either half, of which there
are at most `4*2^b`. Any other witnessing interval crosses exactly one
bridge boundary: crossing none misses a half, while crossing two contains
an entire intervening bridge and fills a half. The proper prefixes and
suffixes of (2) are exactly its chain members and their complements.
Thus every nonexceptional realized target belongs to (3) for an actual
selected edge. Full-set separators create no nonexceptional targets.
Hence

\[
 |\mathcal U(A_E)|=2\sum_E ac+O(2^b).                 \tag{5}
\]

Each edge contributes exactly `|beta_P(C)|+|beta_Q(D)|` to the primary
length. If `v` is the number of nonisolated components, the additional
copies and separators cost at most `(b+2)v`, with `v<=A+B`. Therefore

\[
 |A_E|=\sum_E(a+c)+O(AB+b(A+B)).                     \tag{6}
\]

Both error terms are `o(W(2b))`. This charges every literal position,
including Euler cuts, and does not charge rectangle area as word length.

## 3. The density-per-letter threshold

Fix `tau>=0` and select precisely the pairs satisfying

\[
                   {ac\over a+c}>\tau\sqrt b.       \tag{7}
\]

This is deterministic once the SCDs are fixed. Its nonisolated graph is
connected: the selection condition increases with either length, so an
edge remains selected when either endpoint is replaced by a longest
chain. Thus this particular construction only needs one Euler cut and
one extra bridge, although the more general bound (6) already suffices.

For independently uniform SCD chains, the scaled lengths converge to
independent standard Rayleigh variables `X,Y`, with density

\[
                        f(x)=xe^{-x^2/2},\quad x>0.  \tag{8}
\]

For clarity, this input does not depend on the SCD choice: the number of
chains of bottom rank `i` is `binom(n,i)-binom(n,i-1)`. For `u>=1`,
telescoping gives
`Pr(L_n>=u)=binom(n,floor((n+1-u)/2))/W(n)`, whose limit is `exp(-x^2/2)`
at length `x sqrt(n)`. The same adjacent-binomial products give uniform
Gaussian tails, hence convergence of the polynomially weighted
expectations below. The boundary in (7) has zero limiting measure.

The central-binomial estimates give

\[
 {AB\sqrt b\over W(2b)}\longrightarrow{1\over\sqrt\pi},
 \qquad {2ABb\over4^b}\longrightarrow{2\over\pi}.
\]

Consequently (5)--(7) prove the exact limiting frontier

\[
 {n_b(\tau)\over W(2b)}\longrightarrow C(\tau)
 ={1\over\sqrt\pi}\mathbb E\left[(X+Y)
   \mathbf1_{XY>\tau(X+Y)}\right],                   \tag{9}
\]

\[
 {|\mathcal U(A_b(\tau))|\over4^b}\longrightarrow D(\tau)
 ={2\over\pi}\mathbb E\left[XY
   \mathbf1_{XY>\tau(X+Y)}\right].                   \tag{10}
\]

The function `C` is continuous and strictly decreasing, with
`C(0)=sqrt(2)` and `C(tau)->0`. Thus there is a unique positive `tau_*`
such that

\[
                       C(\tau_*)=1,
 \qquad p_*:=D(\tau_*).                             \tag{11}
\]

This proves (1) in even dimensions, with the stronger density equality.
One ordinary partial top-bit lift gives the stated density lower bound
in odd dimensions at the same asymptotic length ratio. Explicitly, for a
nonempty linear word `A_1,...,A_n`, its lift is
`A_1,...,A_n,{z},A_1 union {z},...,A_{n-1} union {z}`.
Every old witnessed target `T` and `T union {z}` persists, as verified in
the handoff. Its length is `2n`, and
`W(2b+1)/W(2b)=(2b+1)/(b+1)->2`.

### A precise restricted optimality statement

For any measurable fractional whole-pair selection `0<=g(X,Y)<=1` with
`E[(X+Y)g]<=E[(X+Y)g_tau]`, where
`g_tau=1_{XY>tau(X+Y)}`, one has

\[
                         \mathbb E[XYg]\le\mathbb E[XYg_\tau].     \tag{12}
\]

Indeed `(XY-tau(X+Y))(g-g_tau)<=0` pointwise, and integrating proves
(12). Thus (9)--(10) give the optimum limiting density under this
whole-pair selection and charged bridge-cost model. This is not an
optimality theorem for unrestricted words, arbitrary cross-split
constructions, or bridge systems with other occurrence sharing.

There is no hidden assumption that a varying finite selection has a
limiting density function. At finite `b` the same pointwise argument is
`sum ac(g-g_tau)<=tau sqrt(b) sum (a+c)(g-g_tau)`. If a competing
selected-pair word has length at most `W(2b)+o(W(2b))`, (6) bounds its
right side above by `o(4^b)` at `tau=tau_*`. Equation (5) then gives density at
most `p_*+o(1)` directly.

There is also a rigorous strict improvement over `2/pi`, without using
decimals. Put `m=min(X,Y)`. A centered square of side `m` has cost
`2m` and area `m^2`, with

\[
 \mathbb E(2m)=\sqrt\pi,\qquad \mathbb E(m^2)=1.
\]

On the rectangle `[0,X] x [0,Y]`, the bilinear function
`uv-tau(u+v)` has maximum
`max(0,XY-tau(X+Y))` at a corner. This dominates
`m^2-2tau m`, strictly on a positive-measure set when `tau>0`.
At `tau=tau_*` the expected cost difference is zero by (11), giving
`E[XY g_tau_*]>1`, and hence `p_*>2/pi`.

### Explicit one-dimensional integrals

For `0<theta<pi/2`, put

\[
 a_\tau(\theta)={\tau(\cos\theta+\sin\theta)
                         \over\cos\theta\sin\theta}.
\]

Polar integration of (8) gives

\[
 C(\tau)={1\over\sqrt\pi}\int_0^{\pi/2}
 (\cos\theta+\sin\theta)\cos\theta\sin\theta
 I_4(a_\tau(\theta))\,d\theta,                       \tag{13}
\]

\[
 D(\tau)={2\over\pi}\int_0^{\pi/2}
 \cos^2\theta\sin^2\theta I_5(a_\tau(\theta))\,d\theta,             \tag{14}
\]

where elementary integration by parts gives

\[
 I_4(a)=(a^3+3a)e^{-a^2/2}
                  +3\sqrt{\pi/2}\operatorname{erfc}(a/\sqrt2),
 \quad I_5(a)=(a^4+4a^2+8)e^{-a^2/2}.
\]

The checker reports `tau_*=0.476179109655...` and
`p_*=0.841485839042...` at both 2,048 and 8,192 Simpson panels.
These computations are not used to establish (9)--(12).

## 4. The fixed-split wall survives density holes

Here letters and internal orders are arbitrary; no SCD is assumed.
Let a linear or cyclic nonzero word on two disjoint `b`-sets `P,Q` consist
of alternating half-supported blocks, every maximal block having union
of size at least `u`. Suppose the word has `n` letters and `h` nonempty
holes. Put

\[
 K_u=\sum_{j=1}^{u-1}\binom bj.
\]

For every nonempty `J subseteq {1,...,u-1}`,

\[
 \boxed{h\ge K_u\sum_{s\in J}\binom bs-|J|n.}         \tag{15}
\]

Proof: restrict targets to those having between `1` and `u-1` coordinates
in each half. Give such a target weight
`1_{|S intersect P| in J}+1_{|S intersect Q| in J}`. The total required
weight is `2 K_u sum_{s in J} binom(b,s)`. Missing targets remove at most
`2h` of this weight.

A witness for such a target contains no complete block, since a complete
block supplies at least `u` coordinates in one half. It must therefore
cross exactly one boundary. At a boundary between blocks of lengths
`a,c`, distinct suffix unions on one side and distinct prefix unions on
the other are chains. At most `|J|` distinct suffix unions have a rank
in `J`, and each combines with at most `c` prefix unions. The opposite
weight contributes at most `|J|a`. Thus the boundary supplies weight at
most `|J|(a+c)`. Each physical position is charged at most twice over
all boundaries, including for a cyclic word. This bounds covered weight
by `2|J|n` and proves (15).

For full-half blocks take `u=b`. If `n/W(2b)->c`, `0<c<sqrt(2)`, take
`J={s: |s-b/2|<=v sqrt(b)}`. The binomial local limit and its Riemann sum
give

\[
 \liminf {h\over4^b}\ge
 \operatorname{erf}(\sqrt2v)-{2cv\over\sqrt\pi}.     \tag{16}
\]

Its maximizing value is
`v=sqrt(log(sqrt(2)/c)/2)`, so

\[
 \boxed{\liminf {h\over4^b}\ge
 \operatorname{erf}\sqrt{\log(\sqrt2/c)}
 -{\sqrt2c\over\sqrt\pi}\sqrt{\log(\sqrt2/c)}.}      \tag{17}
\]

At `c=1` this is `0.125185394217...`. In particular vanishing hole
density forces `n>=(sqrt(2)-o(1))W(2b)` in this entire architecture.
The proof is insensitive to missing complete ranks: (15) charges the
aggregate holes only once, before choosing a growing rank window.

There is a useful extension to genuinely incomplete blocks. If
`u=b/2+gamma sqrt(b)+o(sqrt(b))`, with `gamma>0`, then
`K_u/2^b->Phi(2gamma)`. Letting a symmetric rank window shrink in scaled
width after taking the limit in (15), vanishing hole density forces

\[
                  \liminf {n\over W(2b)}\ge\sqrt2\Phi(2\gamma).    \tag{18}
\]

Thus even incomplete fixed-split blocks cannot work at coefficient one
if every block union exceeds
`b/2 + (Phi^{-1}(1/sqrt(2))/2 + epsilon) sqrt(b)`.
Mixed-support letters and blocks with substantially smaller supports
remain outside this wall.

## 5. A hole-robust product-box endpoint inequality

This addresses the possibility that the old private-box obstruction could
be broken by omitting only a few whole local ranks.

Consider

\[
 Q=\prod_{i=1}^{d-1}[0,p_i]\times[0,r],\quad
 P=\sum_{i<d}p_i,\quad H=r-P>0,\quad
 V=\prod_{i<d}(p_i+1),\quad P\ge1.
\]

Its plateau layers of ranks `P+j`, `0<=j<=H`, each have `V` points.
Let a literal coordinatewise-maximum word have `n` positions and miss
`h_j` targets of layer `j`. For `0<=a<b<=H` put `D=b-a` and
`M=sum_{j=a}^b h_j`. Then

\[
 \boxed{DV\le2(D+P)(n-V)+4M
                      +2(P-1)(h_a+h_b).}             \tag{19}
\]

Choose one actual interval for each realized target in these layers.
Common-left and common-right endpoint classes are orthogonal chain
partitions. Consider either partition, with `C<=n` nonempty chains.
Across layers `j,j+1`, at least
`2V-C-h_j-h_{j+1}` chains meet both layers; these pairs are cover edges.
Summing supplies at least

\[
                   D(2V-C)-2M+h_a+h_b               \tag{20}
\]

cover edges. Use the monotone potential `phi=sum_{i<d} x_i`, whose range
is `[0,P]`. Its total over either full endpoint plateau layer is the
same. Removing the missing bottom/top points changes the endpoint
potential difference by at most `P h_a`. At most `C-V+h_b` chains end
internally, each contributing at most `P`; internal starts have
nonnegative potential. Therefore total potential increase along all
chains is at most

\[
                       P(C-V+h_a+h_b).              \tag{21}
\]

Every nonvertical cover raises the potential by one. Subtracting (21)
from (20), each endpoint partition contains at least

\[
 DV-(D+P)(C-V)-2M-(P-1)(h_a+h_b)
\]

vertical covers. No vertical cover can belong to both endpoint
partitions, by orthogonality. There are only `DV` available vertical
covers. Adding the two bounds and using `C<=n` proves (19), even when
`n<V` or the individual lower bounds are negative.

Now let `h=sum_{j=0}^H h_j`. Choose `a` from the first quarter of plateau
indices and `b` from the last quarter so that
`h_a,h_b<=4h/H`. There are at least `H/4` choices in each quarter.
Then `D>=H/2`, `D+P<=r`, and (19) gives

\[
 \boxed{h\ge
 {HV/2-2r(n-V)_+\over4+16P/H}.}                     \tag{22}
\]

For `[0,s] x [0,s] x [0,3s]`, this implies

\[
 n\le(1+o(1))(s+1)^2
 \quad\Longrightarrow\quad
 h\ge(1/72-o(1))s(s+1)^2.                            \tag{23}
\]

The whole box has `(s+1)^2(3s+1)` targets. Thus at least
`1/216-o(1)` of the box is missing. This is an unrestricted local-word
bound, not just a bound on canonical SCD witnesses. Arbitrary ambient
set-valued letters do not avoid it: projection onto the ordered chain
increments followed by prefix closure is join-preserving and retains
every locally realized box target as a coordinatewise-maximum witness.

Its global scope must remain limited. The result excludes a density-one
local near-width theorem for these private boxes. It does not exclude
sharing positions or decisive intervals between different boxes, and no
sum of local word lengths is asserted against such a shared construction.

## 6. Exact synchronous tensor law and its cost

Let `A^(i)` be periodic set-words on disjoint coordinate blocks, with
pairwise coprime periods `m_i`. Define the synchronous word

\[
 C_j=\bigcup_i A^{(i)}_{j\bmod m_i},\qquad
                         N=\prod_i m_i.             \tag{24}
\]

Let `U_l(A)` be the targets obtained by cyclic windows of exactly length
`l` in the periodic extension. The Chinese remainder theorem gives the
literal identity

\[
 \mathcal U(C)=\bigcup_{l=1}^{N}
 \left\{\bigcup_i T_i:T_i\in U_l(A^{(i)})\right\}.   \tag{25}
\]

For fixed `l`, a prescribed tuple of local starting residues has a common
global starting position. Its length-`l` interval has precisely the
displayed union. Conversely every global interval projects to these
local windows. All factors must use the same `l`; replacing the right
side by the Cartesian product of unrestricted local union families is
incorrect. For `l>=max_i m_i` every local union is already its full
support, so the length union can be truncated there.

Moreover the physical cost is `N`, not a normalized seed score. For a
fixed number `d>=2` of balanced growing blocks `k_i=Theta(K)`, and
`m_i=O(W(k_i))`,

\[
 {N\over W(K)}=O(K^{-(d-1)/2}).                      \tag{26}
\]

A word of `N` positions realizes at most `min(N,binom(K,s))` targets at
rank `s`. Taking a central rank window of width
`O(sqrt(K log K))` and a binomial tail outside gives

\[
 { |\mathcal U(C)|\over2^K}
       =O(K^{-(d-1)/2}\sqrt{\log K})=o(1).           \tag{27}
\]

For example choose half-width
`sqrt((d+1)K log K)`; the endpoint contribution has the displayed
order and the elementary exponential-moment tail is smaller. No local
universality assumption overrides this global endpoint count. If the
periods are not coprime the attainable phase tuples are fewer; taking
the product of periods as a possibly redundant period only weakens the
same upper bound. Asynchronous products, new phase schedules, and
controlled additional letters are different constructions and need their
own length and coverage proofs.

## 7. Remaining construction gap

The threshold family supplies about `84.15%`, not `1-o(1)`, of the cube.
Using the cylinder-completion theorem on this family therefore does not
prove coefficient one. Nothing here promotes a fixed finite seed to a
growing almost-cover family.

The fixed-split wall shows that reselecting, reordering, or randomly
relabeling bridges while keeping one full-half split cannot finish the
job, even under the new aggregate-hole budget. The box calculation shows
that omission of a vanishing local density does not rescue the uniform
private three-box theorem. The synchronous tensor formula exposes the
missing common-length constraint rather than furnishing amplification.

A surviving construction must introduce a mechanism not covered by these
walls, such as genuine mixed-support interval sharing, low-support
fixed-split blocks, or cross-box/asynchronous assembly with a proved
global interval census. No such near-width density-one assembly is proved
in this note.

## 8. Reproducible checks

Run `python3 scratch/density_bridge_frontier_20260905_c71e4.py`.
The checker has no third-party dependencies and does not read seed files.
It checks:

- All 68 selected-edge graphs at `b=2,3`, including disconnected graphs.
- Threshold and random selections through `b=6`, with every actual interval
  union enumerated, exact primary/seam position counts, and the exact
  nonexceptional target census.
- 1,300 instances of (19) on random literal range-maximum words.
- 800 instances of (15) on random full-half block words.
- 60 exact synchronous tensor identities with coprime periods.
- The finite SCD histogram sums in (9)--(10) through `b=2048`.
- The numerical integrals (13)--(14) at two quadrature resolutions.

These are corroborating finite checks. The proofs and exact definitions,
not the numerical experiments, establish the asymptotic statements.
