# Two-colour product-SCD cross atlas and the ordered-HCRT boundary

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

The proposed finite local obstruction does **not** persist for nonlinear
cross matchings.

Fix a split `A\dot\cup B`, with `|A|=|B|=d`, and symmetric-chain
decompositions of `2^A` and `2^B`. In every product of two chains, the
rank-`k` vertices form a path of legal cross exchanges. Alternating the
edges of every such path gives two partial matchings

\[
                         M_{d,k}^0,M_{d,k}^1.       \tag{0.1}
\]

Their union has all of the following exact properties.

1. Every nonboundary lower shadow occurs once.
2. Every nonboundary upper shadow occurs once.
3. Every nonendpoint middle owner is matched once in each colour.
4. One selector bit works simultaneously at every local rank; the colour
   of a shadow common to source ranks `k` and `k+2` is identical.
5. At a central local rank the owner and shadow leave is
   `O(d^{-1/2})`.

Thus two nonlinear shores whose union is an owner-simple path atlas solve
the local adjacent-shadow problem up to a vanishing boundary. Their union
is not itself one matching or an installed exact factor. In particular,
bounded first-split
and Latin-priority no-go theorems do not extend to arbitrary nonlinear
matchings.

The construction also has an exact all-depth extension. A monotone
`h`-edge rectangle segment has lower and upper flags

\[
 L_t=C_i\cup D_{j+h-t},\qquad
 U_t=C_{i+t}\cup D_{j+h},                           \tag{0.2}
\]

and gives a bijection between lower corners with `h` successors in both
chain factors and upper corners with `h` predecessors in both factors.
However, the edge colours along this segment alternate. Therefore this
all-depth theorem belongs to the **union path**, not to either matching in
(0.1).

Tensoring one fixed colour per logarithmic block does give near-spanning
owner-disjoint `Q_r` packets with

\[
 d=C\log m,qquad r=\Theta(m/\log m),qquad
 {W-G\over W}
 =\exp\!\left[-\Omega\!\left(
 {m\log\log m\over\log m}
 \right)\right].                                   \tag{0.3}
\]

This tensor does **not** inherit (0.2). Its neutral full-face menu has an
irreducible even-load covariance loss, and every polynomial family of
fixed selector/order templates misses `1-o(1)` of the targets at
`q=A\sqrt m`. Traversing the union paths instead is also insufficient:
every globally commonly oriented monotone path cover has at least

\[
 \binom m{\lfloor m/2\rfloor}^{\!2}
 =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}
                                                               \tag{0.4}
\]

components. Hence it cannot give `o(W/H)` components when
`H/\sqrt m\to\infty`.

The surviving gate is consequently not a finite local matching lemma. It
is a state-dependent, mixed-colour product-grid cycle/path theorem with
full ordered target columns. No such theorem is proved here, and no
coefficient-one conclusion is claimed.

## 1. Product-chain notation

Let

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{d-a}
                                                               \tag{1.1}
\]

be a chain in a fixed symmetric-chain decomposition of `2^A`, where the
subscript is cardinality. Write a chain of `2^B` as

\[
 D_b\subset D_{b+1}\subset\cdots\subset D_{d-b}.    \tag{1.2}
\]

Every SCD has exactly

\[
                         c_d=\binom d{\lfloor d/2\rfloor}       \tag{1.3}
\]

chains. The products `C\times D` partition `2^{A\cup B}` into
rectangles.

For `i+j=k-1`, with `i<d-a` and `j<d-b`, define the rank-`k`
cross edge

\[
 e_{i,j}=
 \left\{C_{i+1}\cup D_j,\ C_i\cup D_{j+1}\right\}. \tag{1.4}
\]

Its exact lower and upper shadows are

\[
 R_{i,j}=C_i\cup D_j,
 \qquad
 U_{i,j}=C_{i+1}\cup D_{j+1}.                      \tag{1.5}
\]

Indeed, writing

\[
 \alpha_i=C_{i+1}\setminus C_i,qquad
 \beta_j=D_{j+1}\setminus D_j,                     \tag{1.6}
\]

the two middle endpoints differ by deleting `\beta_j\in B` and inserting
`\alpha_i\in A`.

## 2. The nonlinear two-colour atlas

Choose a phase `\varepsilon_{C,D}\in\{0,1\}` for every product
rectangle, fixed for all ranks. Colour (1.4) by

\[
 \chi_k(e_{i,j})
 =i+\left\lfloor{k\over2}\right\rfloor
   +\varepsilon_{C,D}\pmod2.                       \tag{2.1}
\]

Let `M_{d,k}^c` be the set of edges of colour `c`.

### Theorem 2.1 (two-colour owner/shadow resolution)

For every `d,k` and either choice of rectangle phases:

1. `M_{d,k}^0` and `M_{d,k}^1` are matchings on the rank-`k`
   cross-exchange graph.
2. Their union labels every lower `(k-1)`-set exactly once unless its
   `A`-component or `B`-component is the top of its SCD chain.
3. Their union labels every upper `(k+1)`-set exactly once unless one of
   its two components is a chain bottom.
4. Each colour misses only endpoints of the rank-`k` rectangle paths.

Consequently, for each sign,

\[
 \#\{\text{rank-}k\text{ shadow holes}\}\le2c_d^2, \tag{2.2}
\]

and

\[
 \#\{X:|X|=k,\ X\text{ unmatched in }M_{d,k}^c\}
 \le2c_d^2.                                         \tag{2.3}
\]

#### Proof

In a fixed rectangle and rank, the middle vertices occur along one
anti-diagonal. Consecutive vertices on that anti-diagonal are precisely
the edges (1.4). Thus they form one path. Consecutive edges have `i`-indices
differing by one, so (2.1) alternates. Each colour is therefore a
matching.

Every lower set `R` belongs to unique chains `C,D` and has unique ranks
`i,j`. If neither component is a chain top, (1.4) is defined and has
lower shadow `R`. No other product rectangle or square can have the same
lower corner. This proves the lower assertion. The upper assertion is the
same argument with unique predecessors.

Within one path, every internal vertex meets one edge of each colour.
Only its two endpoints can be missed by a fixed colour. Every product
rectangle contributes at most two lower boundary points, two upper
boundary points, and two unmatched middle endpoints. There are `c_d^2`
rectangles, proving (2.2)--(2.3). `\square`

At a central local rank

\[
                         k=d+x\sqrt d+O(1),         \tag{2.4}
\]

Stirling's formula gives

\[
 {2c_d^2\over\binom{2d}k}
 \le {4e^{x^2}+o(1)\over\sqrt{\pi d}}.             \tag{2.5}
\]

Across all ranks, one sign has at most

\[
                         2c_d2^d                   \tag{2.6}
\]

shadow holes. A fixed colour has at most `4c_d2^d` unmatched middle
sets. To see the latter bound, every unmatched rectangle-path endpoint
has at least one component at a top or bottom of its SCD chain. There are
at most `2c_d` such subsets in either half, and the other half is arbitrary.

### Proposition 2.2 (exact rank-ladder colour coherence)

If `U_{i,j}` in (1.5) is regarded as the lower corner of the square at
source rank `k+2`, its colour is unchanged.

#### Proof

The new lower indices are `(i+1,j+1)`. Hence

\[
 i+1+\left\lfloor{k+2\over2}\right\rfloor
 \equiv i+\left\lfloor{k\over2}\right\rfloor\pmod2. \tag{2.7}
\]

The rectangle phase is fixed across ranks. `\square`

Thus the same selector bit defines both matchings at every local rank and
is exactly coherent on each same-sign `k,k+2,k+4,\ldots` target ladder.

### Proposition 2.3 (simultaneous phase balance)

The rectangle phases can be chosen so that, for every rank `k`,

\[
 \bigl||M_{d,k}^0|-|M_{d,k}^1|\bigr|
 \le2c_d\sqrt{\log(8d)}.                            \tag{2.8}
\]

#### Proof

At a fixed rank, each rectangle path contributes a colour discrepancy in
`\{-1,0,1\}`. Flipping its phase changes the sign. Choose all phases
independently and uniformly. Hoeffding's inequality, with at most `c_d^2`
nonzero summands, gives

\[
 \Pr\left(
 \left|\sum_{C,D}\delta_{C,D,k}\right|>
 2c_d\sqrt{\log(8d)}
 \right)<{1\over2d+1}.                              \tag{2.9}
\]

A union bound over the `2d+1` ranks leaves a positive-probability phase
choice satisfying all inequalities. `\square`

For each eligible shadow the union contains one edge and hence two middle
starts. Giving the two colours fractional weight `1/2` therefore gives
exact start load one simultaneously on every eligible lower and upper
shadow. This is a fractional consequence only; Theorem 2.1 itself is
integral and owner-simple.

## 3. Exact all-depth flags of the union paths

The local construction is stronger setwise than its two matchings, but
the distinction is essential.

Fix chains (1.1)--(1.2). For integers `i,j,h\ge0`, with `0\le h\le d`,
satisfying

\[
 i+j=k-h,qquad i+h\le d-a,qquad j+h\le d-b,       \tag{3.1}
\]

define

\[
                         V_t=C_{i+t}\cup D_{j+h-t},qquad0\le t\le h.
                                                               \tag{3.2}
\]

### Theorem 3.1 (ordered product-SCD flag bijection)

The sequence (3.2) is a literal geodesic cross-exchange path. Its ordered
lower and upper prefix flags are

\[
 L_t=\bigcap_{u=0}^tV_u=C_i\cup D_{j+h-t},          \tag{3.3}
\]

\[
 U_t=\bigcup_{u=0}^tV_u=C_{i+t}\cup D_{j+h}.        \tag{3.4}
\]

In particular,

\[
                         L_h=C_i\cup D_j,qquad
 U_h=C_{i+h}\cup D_{j+h}.                           \tag{3.5}
\]

Consequently (3.5) is a bijection between:

* lower targets whose two SCD positions each have `h` successors; and
* upper targets whose two SCD positions each have `h` predecessors.

At a fixed local rank, each sign has at most

\[
                         2h\,c_d^2                 \tag{3.6}
\]

missing targets. Summed over all local ranks, each sign has at most

\[
                         2h\,c_d2^d                \tag{3.7}
\]

missing targets.

#### Proof

At step `t`, for `0\le t<h`, (3.2) deletes
`D_{j+h-t}\setminus D_{j+h-t-1}` and inserts
`C_{i+t+1}\setminus C_{i+t}`. All deletion coordinates and all insertion
coordinates are distinct. Thus every subpath is geodesic. Nestedness of
the two chains gives (3.3)--(3.4).

A lower target determines its two SCD chains and ranks, hence determines
`i,j`, the unique path (3.2), and the opposite upper target. The converse
and the upper statement are identical. In one product rectangle, at most
`h` points on either end of a diagonal fail the two-successor condition.
This proves (3.6). Across all ranks, the number of subsets of one half in
the top `h` positions of its chains is at most `hc_d`; the other half is
arbitrary. The union bound over the two halves gives (3.7). `\square`

There is an exact all-rank census. Let `E_{d,h}` be the number of subsets
of a `d`-set having `h` SCD successors. If

\[
 n_a=\binom da-\binom d{a-1}                       \tag{3.8}
\]

is the number of chains beginning at rank `a`, then

\[
 E_{d,h}=\sum_a n_a(d-2a+1-h)_+.                   \tag{3.9}
\]

Writing `t=\lfloor(d-h)/2\rfloor`, telescoping gives

\[
 E_{d,h}=
 \begin{cases}
 \displaystyle\binom dt+2\sum_{a<t}\binom da,
       &d-h=2t,\\[6pt]
 \displaystyle2\sum_{a\le t}\binom da,
       &d-h=2t+1.
 \end{cases}                                        \tag{3.10}
\]

The exact number of represented lower targets over all local ranks is
`E_{d,h}^2`, and the upper count is the same. Hence, for fixed `x\ge0`,

\[
 {E_{d,h}\over2^d}\longrightarrow2\Phi(-x),
 \qquad h=x\sqrt d+O(1),                            \tag{3.11}
\]

and the represented density tends to `4\Phi(-x)^2`. If
`1\le h=o(\sqrt d)`,
the hole fraction is

\[
 \left(2\sqrt{2/\pi}+o(1)\right){h\over\sqrt d}.   \tag{3.12}
\]

Here `\Phi` is the standard normal distribution function.

### Decisive colour caveat

The colours of the edges in (3.2) are

\[
 \chi_t=i+t+\left\lfloor{k\over2}\right\rfloor
          +\varepsilon_{C,D}\pmod2.                \tag{3.13}
\]

They alternate. Neither `M^0` nor `M^1` contains even a two-edge segment
of (3.2). Theorem 3.1 is therefore a theorem about the **union path**. It
does not compose with a tensor using one frozen colour per block.

Orientation is also load-bearing. Reversing (3.2) preserves the full core
and hull but changes every proper prefix to

\[
 L_t^{\rm rev}=C_{i+h-t}\cup D_j,qquad
 U_t^{\rm rev}=C_{i+h}\cup D_{j+t}.                 \tag{3.14}
\]

Thus setwise corner bijection is not ordered-port synchronization.

## 4. Tensoring one colour: owner packets only

Partition all but fewer than `2d` ambient coordinates into

\[
                         b=\lfloor m/d\rfloor       \tag{4.1}
\]

blocks `A_s\dot\cup B_s` of size `2d`. In the owner partition, include
every residual subset as a singleton label and keep that label frozen
inside its product cell.
Choose one colour `\sigma_s\in\{0,1\}` in each block. At every local
rank use the matching `M_{d,k}^{\sigma_s}` and regard its unmatched
vertices as singleton cells.

### Theorem 4.1 (near-spanning fixed-colour packetization)

The Cartesian product of these local edge/singleton partitions is an
exact owner partition into physical `Q_S` cells. If

\[
                         p_d={4c_d\over2^d}=O(d^{-1/2}),        \tag{4.2}
\]

then the fraction of Boolean owners with fewer than `b/2` edge factors is
at most

\[
                         2^bp_d^{\,b/2}.            \tag{4.3}
\]

After conditioning on global rank `m`, the exceptional middle-owner count
is at most

\[
                         (2m+1)2^bp_d^{\,b/2}W.     \tag{4.4}
\]

Choose `r=4\cdot2^a` largest subject to `r\le b/2`. Every `Q_S`,
`S\ge r`, partitions into `Q_r` cells by retaining predetermined `r`
axes and taking all `2^{S-r}` assignments of the remaining axes. For
`d=C\log m`,

\[
 {W-G\over W}
 =\exp\!\left[-\Omega\!\left(
 {m\log\log m\over\log m}
 \right)\right],
 \qquad r=\Theta(m/\log m).                         \tag{4.5}
\]

#### Proof

The local matchings and singletons partition every local Boolean cube, so
their products partition all owners. Under independent fair-bit sampling,
the blocks are independent and (2.6) bounds the singleton probability by
`p_d`. Fewer than `b/2` edge factors requires at least `b/2` singleton
blocks, giving (4.3). The central rank has probability at least
`1/(2m+1)`, proving (4.4). The exact subcube subdivision and (4.5) follow
as in Theorem 3.1 of the preceding dense-cross packet report. `\square`

Installing the known isometric `C_{2r}` factors in the retained `Q_r`
cells gives literal integral rows. The exponentially small leave can be
covered by a literal baseline at `o(W)` cost.

This theorem has only an owner-side conclusion. It uses one colour in
each block and therefore cannot invoke Theorem 3.1 at depth greater than
one. It also escapes the hypotheses of the earlier hard one-hot
`J=K_{\mathcal R}K_{\mathcal C}` obstruction, because its cells are
general product-SCD cross squares rather than the four complementary-core
eight-grid cells. This does not prove that `J`, or every other joint
profile, is balanced after tensor selection.

## 5. Exact local cuts and why the nonlinear atlas is necessary

### 5.1 Bounded first-priority families have common holes

Consider `L` fixed pair frames, each with an ordered first-split matching.
Let `e_\ell` be the first `A`--`B` pair of frame `\ell`.

### Theorem 5.1 (common first-pair obstruction)

At either central shadow rank, a fraction at least

\[
                         2^{-2L}-o(1)               \tag{5.1}
\]

is absent from the support of every one of the `L` matchings.

#### Proof

The distinct first pairs form a bipartite graph `H` with at most `L`
edges and at most `2L` vertices. Require every edge of `H` to be split by
the target. Because `H` is bipartite, each connected component has two
opposite `0/1` assignments. Every fixed assignment on `v(H)` coordinates
has central-slice density `2^{-v(H)}+o(1)`. Thus the split event has density
at least `2^{-2L}-o(1)`.

For a lower target, a first-split matching uses it only if an empty pair
precedes the first split pair. For an upper target, a full pair must
precede the first split pair. On the event above the first priority pair
is already split in every frame, so both multiplicities vanish. `\square`

Hence bounded Latin shifts and all bounded first-priority variants are
linearly dead locally. Theorem 2.1 evades this by choosing cross axes
nonlinearly from product-chain geometry.

### 5.2 Exact `A`-projection curvature

For any cross edge `e=\{X,Y\}`, put `R=X\cap Y` and `U=X\cup Y`. Then

\[
 \{R\cap A,U\cap A\}=\{X\cap A,Y\cap A\}           \tag{5.2}
\]

as multisets.

Let `M_1,\ldots,M_L` be cross matchings at rank `k`. Let `\mu(S)` count
lower and upper shadow occurrences across their union, and let `u_I` be
the number of unmatched middle occurrences whose `A`-projection is
`I\subseteq A`. From (5.2),

\[
 \sum_{S:S\cap A=I}\mu(S)
 =L\binom d{k-|I|}-u_I.                             \tag{5.3}
\]

A simultaneous one-hot lower/upper resolution demands

\[
 \tau_I=\binom d{k-1-|I|}+\binom d{k+1-|I|}.        \tag{5.4}
\]

Therefore

\[
 \sum_S|\mu(S)-1|
 \ge\sum_{I\subseteq A}
 \left|L\binom d{k-|I|}-u_I-\tau_I\right|.         \tag{5.5}
\]

If every matching is owner-complete up to `o(\binom{2d}d)` unmatched
vertices, then at `k=d` asymptotically one-hot total mass forces `L=2`.
Put
`C_i=\binom di`. Even allowing unmatched vertices, the number of holes is
at least

\[
 H_d\ge\sum_i C_i(C_{i-1}+C_{i+1}-2C_i)_+.         \tag{5.6}
\]

The exact curvature is

\[
 {C_{i-1}+C_{i+1}-2C_i\over C_i}
 ={(2i-d)^2-(d+2)\over(i+1)(d-i+1)}.                \tag{5.7}
\]

If `\phi` and `\overline\Phi` are the standard normal density and upper
tail, the hypergeometric local limit theorem gives

\[
 H_d\ge
 \left[
 4\bigl(\sqrt2\,\phi(\sqrt2)-\overline\Phi(\sqrt2)\bigr)
 +o(1)\right]{\binom{2d}d\over d}.                 \tag{5.8}
\]

#### Proof of the constant

Under weights `C_i^2/\binom{2d}d`,

\[
                         Z={2i-d\over\sqrt{d/2}}
 \Longrightarrow N(0,1).                           \tag{5.9}
\]

Equation (5.7) equals `(2/d)(Z^2-2)+o(d^{-1})` in the central window.
Thus the normalized positive curvature tends to

\[
 {2\over d}\mathbb E(Z^2-2)_+
 ={4\over d}
 \bigl(\sqrt2\phi(\sqrt2)-\overline\Phi(\sqrt2)\bigr). \tag{5.10}
\]

Gaussian tails justify truncation. `\square`

The `\Omega(1/d)` defect is genuine but sublinear. It is compatible with
the `O(d^{-1/2})` boundary of Theorem 2.1 and is not a coefficient-scale
global obstruction.

### 5.3 Abstract target-simple common flags

For completeness, there is no local target-capacity obstruction at the
fractional/common-flag level. Fix `i` and define

\[
\begin{aligned}
 \mathcal L_{k,i}
 &=\{R:|R|=k-1,\ |R\cap A|=i-1\},\\
 \mathcal U_{k,i}
 &=\{U:|U|=k+1,\ |U\cap A|=i\}.
\end{aligned}                                        \tag{5.11}
\]

Join `R` to `U` when `U\setminus R` contains one coordinate from each
half. The two degrees are

\[
 D_L=(d-i+1)(d-k+i),qquad
 D_U=i(k+1-i),                                      \tag{5.12}
\]

and

\[
                         D_U-D_L=(k-d)(d+1).        \tag{5.13}
\]

Each graph is biregular, so Hall's theorem saturates its smaller shore.
Since the sign in (5.13) is independent of `i`, their union misses exactly

\[
                         \left|\binom{2d}{k-1}-\binom{2d}{k+1}\right|  \tag{5.14}
\]

shadows. It is perfect at `k=d` and has relative leave
`O(|k-d|/d)` in the central band. These flags are target-simple but need
not be owner-simple: several selected flags may share a middle endpoint.
Theorem 2.1 supplies the owner-simple near-resolution.

## 6. Ordered-column failures of naive composition

### 6.1 Frozen-colour elementary-symmetric loss

Restrict first to nonboundary targets, or grant a one-colour boundary
completion, and consider the complete distinct-block
`q`-face menu of the fixed-colour tensor. For a lower target `T`, let

\[
 w_s(T)=
 \begin{cases}
 2,&\text{the frozen colour in block }s\text{ equals the unique local
 shadow colour},\\
 0,&\text{otherwise}.
 \end{cases}                                        \tag{6.1}
\]

If `g(T)=\#\{s:w_s(T)=2\}`, its exact menu multiplicity is

\[
 Z_q(T)=e_q(w_1,\ldots,w_b)=2^q\binom{g(T)}q.       \tag{6.2}
\]

Under the explicit neutral-product concentration hypothesis
`g=b/2+\delta`, `\delta=o(q)`, one has deterministically

\[
 \log{Z_q(T)\over\binom bq}
 =-{q(q-1)\over2b}
  +O\!\left({q|\delta|\over b}+{q^3\over b^2}\right). \tag{6.3}
\]

At

\[
 d=C\log m,qquad b\sim m/d,qquad q=A\sqrt m,      \tag{6.4}
\]

the principal term is

\[
                         -\left({A^2C\over2}+o(1)\right)\log m. \tag{6.5}
\]

This is the minimal even-load covariance loss: the local load is `0/2`
rather than one. It rigorously disproves the neutral independent Cartesian
mixture. It is **not** a universal Hall cut against a correlated selector:
`Z_q` is menu degree, not neighborhood capacity, and a state-dependent
law may concentrate atypical columns. A physical cyclic order uses only
cyclic intervals and has an even smaller menu.

### 6.2 A true bounded-template support cut

The following restricted ordered theorem is a genuine Hall/support
obstruction.

### Theorem 6.1 (bounded-template entropy cut)

Suppose a compiler repeats only `L` frozen **effective** templates.
Template `\ell` includes its active block set, one selector vector on that
set, and one cyclic order of that set. Distinct active sets or restricted
orders count as distinct templates. Assume the balanced rectangle phases
make an unconditional Bernoulli target compatible with either fixed colour
with probability at most `1/2+\varepsilon_d`, where
`\varepsilon_d=O(d^{-1/2})`; include every boundary state in this upper
bound.

Then a random target is reachable at depth `q` with probability at most

\[
                         Lb(1/2+\varepsilon_d)^q     \tag{6.6}
\]

before exact-rank conditioning, and at most

\[
                         (2m+1)Lb(1/2+\varepsilon_d)^q          \tag{6.7}
\]

after conditioning. Hence every polynomial `L` has `1-o(1)` target holes
when `d=C\log m` and `q=A\sqrt m`.

#### Proof

For a fixed template and cyclic `q`-interval `I`, the target's required
colour syndrome must equal `\sigma^\ell` on all blocks of `I`. Under the
unconditioned Bernoulli law of density `(m\pm q)/(2m)`, disjoint blocks are
independent, so this has probability at most
`(1/2+\varepsilon_d)^q`. Proposition 2.3 bounds the signed eligible-colour
imbalance by `\operatorname{poly}(d)2^{-d}`, while the probability of a
chain-boundary state is `O(d^{-1/2})`; hence the displayed compatibility
hypothesis holds. There are at most `b` intervals in each effective
template. The union bound gives (6.6). Conditioning this Bernoulli law on
its mean rank costs `O_A(\sqrt m)`, and the cruder factor `2m+1` gives
(6.7). Finally,

\[
 (1/2+O(d^{-1/2}))^q=2^{-(1-o(1))q},                \tag{6.8}
\]

which dominates every polynomial prefactor. `\square`

Cell-dependent orders can generate `2^{\Omega(q)}` effective templates
and lie outside this theorem. Thus (6.7) identifies required order entropy;
it is not a no-go against statewise mixed-colour chronology.

## 7. Exact global monotone width obstruction

Split the even residual coordinate set as `R_A\dot\cup R_B` with equal
sizes, and let

\[
 A_* =\bigcup_sA_s,qquad B_* =\bigcup_sB_s,qquad
 |A_*|=|B_*|=m.                                    \tag{7.1}
\]

Orient every rectangle edge from `B_*` toward `A_*` and put

\[
                         P(X)=|X\cap A_*|.          \tag{7.2}
\]

Every forward product-SCD edge increases `P` by one.

### Theorem 7.1 (sharp coordinate-monotone path width)

If `r_0` middle owners are discarded and the remaining owners are covered
by `p` paths which are all monotone in the orientation (7.2), then

\[
                         p+r_0\ge
 \binom m{\lfloor m/2\rfloor}^{\!2}.                \tag{7.3}
\]

In the full commonly oriented cross-exchange graph, without exceptions,
the bound is attained by the global product-SCD diagonal path cover.
Consequently

\[
 \operatorname{pc}_{\rm mon}
 =\binom m{\lfloor m/2\rfloor}^{\!2}
 =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}. \tag{7.4}
\]

#### Proof

A monotone path meets every `P`-level at most once. The level
`P=p_0` contains

\[
                         \binom m{p_0}^2             \tag{7.5}
\]

middle owners. At the largest level, at most `r_0` vertices are discarded
and every path covers at most one remaining vertex, proving (7.3).

For equality in the full cross-exchange graph, fix SCDs of `2^{A_*}` and
`2^{B_*}`. Every ordered pair of
chains has one nonempty rank-`m` diagonal path, and these paths partition
the middle layer. The number of chain pairs is the square in (7.4).
Stirling's formula gives its asymptotic value. The fixed logarithmic-block
product-grid subgraph inherits the lower bound, but equality in that
smaller graph is not asserted. `\square`

The standard independent flush/reload compiler has exact length

\[
                         W+(2H+1)(p+r_0).           \tag{7.6}
\]

Therefore global monotonicity cannot satisfy `p+r_0=o(W/H)` when
`H/\sqrt m\to\infty`. Its relative toll is at least

\[
                         \left({4\over\sqrt\pi}+o(1)\right)
 {H\over\sqrt m}.                                   \tag{7.7}
\]

This theorem does not cover state-dependent mixed orientations, delayed
reversals using fresh axes, or nonmonotone seams. Such mechanisms can meet
the central `P`-level repeatedly and are the only remaining product-grid
escape.

## 8. Proved boundary and the remaining lemma

Proved:

1. Two nonlinear product-SCD shores give a near-spanning owner-simple path
   atlas whose union is target-one-hot for both local signs at every rank.
2. Their colour is exactly coherent on common-target `k\mapsto k+2`
   ladders, and rectangle phases can be balanced simultaneously over all
   ranks.
3. The union paths have exact ordered flags at every local depth and an
   exact boundary census.
4. One fixed colour per logarithmic block tensors into owner-disjoint
   `Q_r` packets with exponentially small leave.
5. Every bounded first-priority/Latin atlas has a constant-density common
   hole set.
6. Two owner-complete matchings obey the exact `A`-projection curvature
   cut (5.8), but that cut is only `O(1/d)` relative.
7. Neutral fixed-colour Cartesian mixing has the exact covariance loss
   (6.3); bounded frozen order templates are genuinely ruled out by
   (6.7).
8. Every globally commonly oriented monotone fusion is ruled out at the
   Gaussian tail-killing scale by (7.3).

Not proved:

* a single integral selection which traverses both checkerboard colours;
* a state-dependent product-grid cycle/path factor with no repeated
  physical axis inside any protected `H`-window;
* simultaneous floor-balanced lower and upper target loads for every
  `q\le H`;
* `o(W/H)` path components after all delayed reversals and seams; or
* compatibility with the full HCRT selector, tag, cone, cycle-congruence,
  and SCD-tail interfaces.

The exact successor is therefore:

> **Mixed-colour ordered product-grid lemma.** In the product of the local
> SCD rectangle paths, construct an owner-simple literal cycle/path factor
> whose chronology uses both edge colours according to local path parity,
> supplies the state-dependent order diversity required beyond the frozen
> template model, repeats no
> physical axis within `H` steps, has `o(W/H)` components including the
> exceptional leave, and has `o(W)` aggregate lower and upper floor defect
> simultaneously over all protected depths.

Theorem 2.1 shows that this is not blocked by the bounded first-shadow or
priority obstructions proved here. It does not rule out every joint-profile
invariant. Theorems 6.1 and 7.1 show that fixed order
templates and common monotone orientation cannot prove it. A successful
proof must use genuinely state-dependent mixed-colour chronology.
