# A three-direction cross-sector double carrier, its exact tensor kernel, and the surviving window bound

Date: 2026-07-26

Method: pure mathematics only.

**Scope correction.**  The sixteen-owner `Q_3` packet below is minimal
only within its three-direction realization.  It is not the absolutely
smallest cycle packet.  The sharper eight-owner `C_4` rectangle theorem,
including absolute minimality, is
`MATH_THEOREM_MINIMAL_CROSS_SECTOR_RECTANGLE_CARRIER_20260726.md`.

## 0. Outcome

The octahedral packet on four special coordinates has a genuine local
defect: above a fixed singleton target there are only three middle
extensions, and any two carrier edges meet.  One literal
three-direction way to break that defect is the following pair of
disjoint physical `Q_3` cells on eight coordinates:

\[
 \begin{aligned}
 C_0&=\{a\}*\{b,c\}*\{u,v\}*\{w,x\},\\
 C_1&=\{u\}*\{v,x\}*\{a,b\}*\{w,d\},
 \end{aligned}                                                     \tag{0.1}
\]

whose common rank-three lower target

\[
                         \tau=\{a,u,w\}                             \tag{0.2}
\]

has one carrier in each cell.  The two carriers use the disjoint extension
pairs

\[
                         \{b,c\},\qquad \{v,x\}.                    \tag{0.3}
\]

Thus `C_0 dot-union C_1` is an exact sixteen-owner packet in which the
local target carrier is genuinely nonunique.  Placing the four extension
coordinates in different coarse macroblocks makes (0.3) an actual
cross-sector kernel, not a relabelling inside one macroprofile.

Tensoring `r` copies gives an exact partition into `2^r` cells `Q_(3r)`.
After adjoining `d` spectator axes so that

\[
                         h=3r+d
\]

is a power of two, every cell is a `Q_h`.  A fine target touching a fixed
set `I` of `q` local packets has exactly `2^q` pairwise owner-disjoint
carrier cells.

There is a useful strengthening of the syndrome-cycle theorem.  If

\[
                 q\ge \log _2 h+1,\qquad q<h,                       \tag{0.4}
\]

then the syndrome factor can be chosen so that **every** face with one
prescribed `q`-set of directions is a consecutive window, exactly

\[
                         {2^q\over h}                               \tag{0.5}
\]

times.  Applying this independently in the tensor cells gives one exact
cycle factor which, for a fixed touched set `I`, covers every fine target
in all its carrier cells, hence exactly

\[
                         \boxed{{4^q\over h}}                       \tag{0.6}
\]

times.

This is positive cross-sector capacity, but it does not remove the full
fine-window obstruction.  In the natural class in which every `Q_h` cell
uses a doubled-permutation factor with one common direction order, the
fraction of the fine targets over all `I in binom([r],q)` which can be
reached is at most

\[
 \boxed{
   \min\left\{1,
       {2^q(r-q+1)\over\binom rq}
       \right\}.}                                                   \tag{0.7}
\]

There is an exact physical random construction reaching at least

\[
 \boxed{
 1-\left(1-{1\over\binom rq}\right)^{2^q}.}                         \tag{0.8}
\]

Consequently, when `q=o(r)`, the upper and lower bounds have the same
logarithmic exponent, up to `O(log r)`:

\[
 \log \rho_{r,q}
 =-q\log(r/q)+(\log2-1)q
   +O\left({q^2\over r}+\log r+\log q\right).                       \tag{0.9}
\]

In particular, for `q=A sqrt(m)+O(1)` and `r/q -> infinity`, the reached
fraction is `o(1)`.  Even if arbitrary cycle words are allowed inside
each cell, the owner-start count gives the unconditional packet bound

\[
 \boxed{
  \rho^{\rm arbitrary}_{r,q}
  \le \min\left\{1,{16^q\over\binom rq}\right\},}                  \tag{0.10}
\]

which is still `o(1)` when `r/q -> infinity`.

The exact tensor transport polynomial is also explicit.  If the two
carrier pairs are assigned to macroprofile increments `A_i` and `B_i`,
then the carrier-cell kernel at touched block `i` is

\[
                         z_{A_i}+z_{B_i},                            \tag{0.11}
\]

and its `q`-fold tensor is

\[
                         \prod_{i\in I}(z_{A_i}+z_{B_i}).           \tag{0.12}
\]

Thus all `2^q` binary source macroprofiles occur integrally.  Formula
(0.12) is a genuine subkernel of the inclusion flow `F_(k,l)`, but a
bounded two-branch kernel cannot realize the whole flow at the intended
scale.  A tensor kernel with at most `t` disjoint local carriers has the
same bound with `2^q` replaced by `t^q`; hence it needs

\[
 t\ge
 \exp\left({\log\binom rq-\log(r-q+1)\over q}\right)
 =(e-o(1)){r\over q}                                      \tag{0.13}
\]

when `q=o(r)`.  The next exact constructive lemma is therefore a
**growing**, floor-weighted carrier bank with `t=Omega(r/q)`, not another
bounded associator.

The theorem is local/tensorial.  It proves positive labelled capacity and
a sharp failure of the bounded tensor lift.  It does not turn the
sectorwise failure into an ambient `Omega(W)` obstruction, because the
ambient macroprofile flow may use packets outside this tensor family.

## 1. The sixteen-owner packet

For pairwise disjoint sets `P_1,...,P_s`, write

\[
 F*P_1*\cdots*P_s
 =\{F\cup\{p_1,\ldots,p_s\}:p_i\in P_i\}.
\]

On the eight coordinates

\[
                         a,b,c,d,u,v,w,x
\]

define `C_0,C_1` by (0.1).  Each consists of eight rank-four sets.  Its
three displayed two-element factors are disjoint coordinate pairs, so
each is a literal physical `Q_3`.

### Lemma 1.1 (exact disjointness)

The cells `C_0` and `C_1` are disjoint.

#### Proof

Suppose `S` belonged to both.  Since every member of `C_0` contains `a`,
the `\{a,b\}` choice in `C_1` would have to be `a`; hence `b` would not
belong to `S`.  The `\{b,c\}` choice in `C_0` would then have to be `c`.
But no member of `C_1` contains `c`, a contradiction.  \(\square\)

Consequently

\[
                         \mathcal P=C_0\mathbin{\dot\cup}C_1       \tag{1.1}
\]

is an exact partition of its sixteen-owner support into two cubes.

### Lemma 1.2 (two literal carriers)

The target `tau` in (0.2) is the lower face of

\[
 \{a,b,u,w\}\leftrightarrow\{a,c,u,w\}              \tag{1.2}
\]

in `C_0`, and of

\[
 \{a,u,v,w\}\leftrightarrow\{a,u,x,w\}              \tag{1.3}
\]

in `C_1`.  The four middle endpoints in (1.2)--(1.3) are distinct.

#### Proof

The edge (1.2) flips the active pair `\{b,c\}` while the other two
active pairs are fixed at `u,w`; its endpoint intersection is `tau`.
The edge (1.3) flips `\{v,x\}` while the other active pairs are fixed at
`a,w`; it has the same intersection.  Their added-coordinate sets are
the disjoint pairs in (0.3).  \(\square\)

This already distinguishes the packet from the old
`J(4,2) square Q_2` cells.  There the three extensions of a singleton
form a triangle, so two carrier edges necessarily share an owner.  Here
the five coordinates outside `tau` contain a matching of size two.

### Proposition 1.3 (minimal extension count)

Let a rank-`s` target `T` have `v` available rank-`s+1` middle extensions
`T union {x}` inside an exact owner packet.  Pair-flip edge carriers of
`T` form a matching on these `v` extensions.  Hence at most

\[
                         \left\lfloor {v\over2}\right\rfloor       \tag{1.4}
\]

can occur in pairwise owner-disjoint cells.  In particular, nonunique
carriage requires `v>=4`; the four extensions used in (1.2)--(1.3)
attain the minimum.

#### Proof

Every carrier edge has endpoints `T union {x}` and `T union {y}` for
two distinct extensions `x,y`.  Two such edges can lie in disjoint owner
cells only if their endpoint pairs are disjoint.  They therefore form a
matching on the extension set, proving (1.4).  \(\square\)

The unused fifth extension `d` is forced only by the convenient rank-four,
three-direction realization (0.1); the double carrier itself uses the
minimum four extensions.

## 2. It is genuinely cross-sector

Fix a coarse coordinate partition into macroblocks.  Let `ell` be the
macroprofile of `tau` together with any fixed exterior core.

If `b,c` lie in one coarse block `A` and `v,x` in another coarse block
`B`, then every endpoint of (1.2) has source profile

\[
                         k^{(0)}=\ell+e_A,                         \tag{2.1}
\]

whereas every endpoint of (1.3) has source profile

\[
                         k^{(1)}=\ell+e_B.                         \tag{2.2}
\]

Thus the two physical carrier cells feed the same labelled target from
two different source macroprofiles.

Alternatively put `b,c,v,x` in four different coarse blocks.  Then each
carrier edge itself joins two source macroprofiles.  Reflecting the
oriented cycle interchanges which endpoint is the start, so all four
one-coordinate increments are physically available.  Either placement
breaks the assertion that every allowed cycle must remain in one middle
macroprofile.

At the carrier-cell level the first placement has generating polynomial

\[
                         K_i(\mathbf z)=z_{A_i}+z_{B_i}.             \tag{2.3}
\]

At the middle-extension level it is

\[
                         \widehat K_i(\mathbf z)
                         =2z_{A_i}+2z_{B_i},                       \tag{2.4}
\]

because each carrier edge has two endpoints.  Both are integral kernels.

For comparison, at depth one the abstract macroprofile inclusion flow has
row-normalized local weight

\[
 {F_{\ell+e_j,\ell}\over V_{\ell+e_j}}
 ={1\over\binom m1}\binom{\ell_j+1}{\ell_j}
 ={\ell_j+1\over m}.                                  \tag{2.5}
\]

For a bank rooted at one fixed target, the target normalization is the
relevant one.  The binomial identity

\[
 \binom8{\ell_j+1}\binom{\ell_j+1}{\ell_j}
 =\binom8{\ell_j}(8-\ell_j)
\]

gives

\[
 {F_{\ell+e_j,\ell}\over T_\ell}={8-\ell_j\over m}.               \tag{2.6}
\]

Thus an exact target-rooted local bank must assign carrier extensions
proportionally to `8-ell_j`, subject to physical pairing of their middle
owners.  The two equal branches in (2.3) realize a positive two-sector
subkernel, but not the complete weighted support.

## 3. Tensoring and exact counts

Take `r` coordinate-disjoint copies `mathcal P_i` of (1.1).  Adjoin `d`
disjoint spectator pairs and choose `d` so that

\[
                         h=3r+d=2^t.                              \tag{3.1}
\]

Choosing one endpoint from every spectator pair gives a `Q_d` factor.
The full packet is

\[
                         \mathcal P^{(r,d)}
                         =\mathcal P_1\times\cdots\times
                           \mathcal P_r\times Q_d.                 \tag{3.2}
\]

It is partitioned by the cells

\[
 C_\varepsilon
 =C_{\varepsilon_1}^{(1)}\times\cdots\times
  C_{\varepsilon_r}^{(r)}\times Q_d,
 \qquad \varepsilon\in\{0,1\}^r.                                \tag{3.3}
\]

Every cell is a physical `Q_h`.  The ledger is

\[
\begin{array}{c|c}
\text{packet owners}&16^r2^d\\
\text{cells}&2^r\\
\text{owners per cell}&2^{3r+d}=2^h,
\end{array}                                                       \tag{3.4}
\]

and `2^r2^h=16^r2^d`, as required.

Fix `I subseteq [r]`, `|I|=q`.  Define `mathcal T_I` by putting the local
restriction equal to `tau_i` in every `i in I`, choosing an arbitrary
owner of `mathcal P_i` in every `i notin I`, and choosing an arbitrary
spectator orientation.  A fixed exterior core may be adjoined to place
these sets in any desired ambient middle rank.  The exact count is

\[
                         |\mathcal T_I|=16^{r-q}2^d.                \tag{3.5}
\]

The union over all touched sets is disjoint and has size

\[
                         |\mathcal T_{r,q}|
                         =\binom rq16^{r-q}2^d.                    \tag{3.6}
\]

### Lemma 3.1 (exact carrier multiplicity)

Every target in `mathcal T_I` is a lower `q`-face in exactly `2^q` cells
of (3.3).

#### Proof

In a touched packet, Lemma 1.2 permits either local cell.  In an untouched
packet the prescribed middle owner belongs to exactly one of the disjoint
cells `C_0,C_1`.  The choices are independent over the `q` touched
packets, giving `2^q`.  Different choices give different cells of the
partition and are therefore owner-disjoint.  \(\square\)

At the macroprofile level, tensoring (2.3) gives precisely

\[
                         K_I(\mathbf z)
                         =\prod_{i\in I}
                           (z_{A_i}+z_{B_i}).                        \tag{3.7}
\]

Every binary choice of source increments occurs with coefficient one.
The extension-level polynomial is `2^q K_I`.  Thus the carrier
multiplicity is not a fractional or averaged statement: all its columns
are present as disjoint physical cells.

## 4. A full-face syndrome factor

The next lemma is useful beyond this packet.

### Lemma 4.1 (prescribed-direction full-face factor)

Let `h=2^t`, let `D` be a prescribed `q`-subset of the directions of
`Q_h`, and assume

\[
                         t+1\le q<h.                               \tag{4.1}
\]

There is a vertex partition of `Q_h` into isometric `C_(2h)` cycles such
that

1. every cycle has one common doubled-permutation transition word;
2. `D` is a cyclic interval of that permutation; and
3. every `D`-face occurs as a consecutive lower window exactly
   `2^q/h` times.

#### Proof

Write `U=F_2^t` and `Sigma=U direct-sum <v>`.  Order the cube directions
so that the cyclic interval `D` contains positions

\[
                         h,1,2,\ldots,t.                            \tag{4.2}
\]

Choose a listing `u_0,...,u_(h-1)` of `U` with

\[
 u_0=0,\qquad
 u_j=e_1+\cdots+e_j\quad(1\le j\le t),                         \tag{4.3}
\]

and fill the remaining positions by the unused elements of `U` in any
order.  Define a syndrome map `phi:F_2^h -> Sigma` by

\[
 \phi(e_j)=u_j+u_{j-1}\quad(1\le j<h),\qquad
 \phi(e_h)=v+u_{h-1}.                                  \tag{4.4}
\]

For the standard doubled-permutation cycle, its first-half prefix
syndromes are the `u_j`, and its second-half prefix syndromes are
`v+u_j`.  They exhaust `Sigma` exactly once.  Therefore the translates
of this cycle by

\[
                         K=\ker\phi                               \tag{4.5}
\]

partition `Q_h` into isometric `C_(2h)` cycles.

By (4.3),

\[
 \phi(e_j)=e_j\quad(1\le j\le t),                              \tag{4.6}
\]

while `phi(e_h)` has nonzero `v`-component.  Hence

\[
                         \phi(F_2^D)=\Sigma.                       \tag{4.7}
\]

Projection of `K` onto the coordinates outside `D` is consequently
surjective.  Indeed, for any outside vector `y`, (4.7) supplies a vector
`z` supported on `D` with `phi(z)=phi(y)`, and then `y+z in K` projects
to `y`.

Fix a `D`-face, equivalently its outside orientation.  At either of the
two occurrences of the interval `D` in the doubled word, the translates
whose window has that outside orientation form one fibre of this
projection.  Its size is

\[
 |K\cap F_2^D|
 =2^{q-(t+1)}.                                        \tag{4.8}
\]

There are exactly two interval occurrences because `q<h`.  Thus the
face multiplicity is

\[
                         2\cdot2^{q-t-1}
                         ={2^q\over h}.                           \tag{4.9}
\]

The doubled-permutation word is isometric because every cyclic arc of at
most `h` transitions uses distinct directions.  \(\square\)

### Theorem 4.2 (simultaneous fixed-profile positive capacity)

Under (3.1) and (4.1), for every fixed `I in binom([r],q)` there is one
exact factor of `mathcal P^(r,d)` into physical isometric `C_(2h)` cycles
such that every target in `mathcal T_I` occurs exactly `4^q/h` times as a
lower consecutive `q`-window.

#### Proof

In every tensor cell, take for `D` the `q` local carrier directions in
the blocks of `I`.  Apply Lemma 4.1 independently in that cell.  Every
`D`-face in the cell is then present `2^q/h` times.  The cells are
owner-disjoint, so the union of these factors is one exact factor of the
whole packet.

By Lemma 3.1, a target in `mathcal T_I` determines one `D`-face in each
of exactly `2^q` cells.  No other cell contains all its required local
owners.  Its total multiplicity is therefore

\[
                         2^q{2^q\over h}={4^q\over h}.              \tag{4.10}
\]

The construction in each cell covers all its `D`-faces, so this holds for
all targets in `mathcal T_I` simultaneously.  \(\square\)

If `q=A sqrt(m)+O(1)` and `log h=o(sqrt(m))`, condition (4.1) holds and

\[
 {4^q\over h}
 =\exp\bigl(A(\log4)\sqrt m-\log h+o(\sqrt m)\bigr).                \tag{4.11}
\]

Thus lack of local multiplicity is decisively not the problem after one
touched macroprofile is fixed.

## 5. All touched profiles: an exact physical lower bound

The preceding factor depends on `I`.  We now choose one factor and ask
how much of the union (3.6) it reaches.

Independently for every tensor cell, choose a uniform

\[
                         J\in\binom{[r]}q.                            \tag{5.1}
\]

Use Lemma 4.1 with the `q` local carrier directions indexed by `J`.
These independent choices do not affect ownership because they occur in
disjoint cells.

Fix `T in mathcal T_I`.  It has `2^q` candidate cells.  In each candidate
cell it is covered whenever the independent choice (5.1) equals `I`, and
then Lemma 4.1 covers its exact face.  Therefore

\[
 \Pr(T\hbox{ is missed})
 =\left(1-{1\over\binom rq}\right)^{2^q}.                         \tag{5.2}
\]

Summing over `T` and taking expectations proves:

### Theorem 5.1 (one-factor positive fraction)

There is one exact cycle factor of the tensor packet which reaches at
least the fraction

\[
                         1-\left(1-{1\over\binom rq}\right)^{2^q} \tag{5.3}
\]

of the fine targets in (3.6).

This is a literal target statement, not only a direction-support
statement.  The use of expectation is only an existence proof for a
finite family of independently chosen exact cell factors.

## 6. The surviving common-order window bound

Consider any factor assembled by putting in each tensor `Q_h` cell a
doubled-permutation syndrome factor with one common cyclic order for all
cycles of that cell.  The order may depend arbitrarily on the cell.

Mark in the order the one local carrier direction belonging to each of
the `r` base packets.  There are `r` marked directions and at least
`h-r>=2r` unmarked directions.  Break the marked positions into cyclic
runs of lengths `s_1,...,s_j`.  The number of length-`q` intervals using
only marked directions is

\[
 \sum_{a=1}^j(s_a-q+1)_+
 \le r-q+1.                                                       \tag{6.1}
\]

For every supported touched set `I`, one cell can carry at most

\[
                         8^{r-q}2^d                               \tag{6.2}
\]

members of `mathcal T_I`: the touched local target is fixed, every
untouched local cube has eight vertices, and the spectator orientation is
arbitrary.  Since there are `2^r` cells, the number of distinct reached
targets is at most

\[
                         2^r(r-q+1)8^{r-q}2^d.                     \tag{6.3}
\]

Dividing by (3.6) gives (0.7).

Let `rho_(r,q)` be the optimum reached fraction in this common-order cell
class.  If `2^q/binom(r,q)=o(1)`, Theorem 5.1 and (0.7), together with
`1-(1-x)^N=(1+o(1))Nx` for `Nx=o(1)`, give

\[
 {2^q\over\binom rq}(1-o(1))
 \le\rho_{r,q}
 \le {2^q(r-q+1)\over\binom rq}.                                \tag{6.4}
\]

For `q=o(r)`, Stirling's formula gives

\[
 \log\binom rq
 =q\log(r/q)+q
  +O\left({q^2\over r}+\log q\right).                            \tag{6.5}
\]

Equations (6.4)--(6.5) prove the logarithmic asymptotic (0.9).  In
particular, at `q=A sqrt(m)+O(1)` with `r/q -> infinity`,

\[
 \log\rho_{r,q}
 \le-A\sqrt m\log\left({r\over A\sqrt m}\right)
      +O_A(\sqrt m+\log r),                                      \tag{6.6}
\]

so the fraction tends to zero.

## 7. A factor-independent owner-start bound

Drop the common-order hypothesis and allow arbitrary isometric-cycle
factors inside every tensor cell.  Every middle owner is one directed
start and supplies only one depth-`q` lower window.  Hence the total
number of distinct reached targets is at most the number of packet owners,
namely `16^r2^d`.  Dividing by (3.6) gives

\[
 \rho^{\rm arbitrary}_{r,q}
 \le {16^q\over\binom rq},                                      \tag{7.1}
\]

with the right side truncated at one.  For `q=o(r)`,

\[
 \log\rho^{\rm arbitrary}_{r,q}
 \le-q\log(r/q)+(\log16-1)q
   +O\left({q^2\over r}+\log q\right).                            \tag{7.2}
\]

Thus arbitrary variation of the cycle order cannot rescue this bounded
packet when `r/q -> infinity`.

This is still a packet-sector theorem.  The target family (3.6) is not
asserted to have positive density in the complete ambient rank layer.
Accordingly (7.1) is not an ambient coefficient-one obstruction.

## 8. The exact dispersion property required by `F_(k,l)`

The construction exposes the general algebra cleanly.  Suppose a local
target of macroprofile `ell` has a disjoint bank of carrier cells.  Classify
the cells by their source-profile increment `alpha` and write

\[
                         n_\ell(\alpha)
                         =\#\{\hbox{local carriers of type }\alpha\}.
                                                                    \tag{8.1}
\]

Its carrier polynomial is

\[
                         P_\ell(\mathbf z)
                         =\sum_\alpha n_\ell(\alpha)\mathbf z^\alpha.
                                                                    \tag{8.2}
\]

For coordinate-disjoint local packets, tensoring is literal and the exact
number of carrier cells with total increment `alpha` is

\[
                         [\mathbf z^\alpha]
                         \prod_iP_{\ell^{(i)}}(\mathbf z).          \tag{8.3}
\]

There is no rounding error in (8.3).  Formula (3.7) is the special case
`P_i=z_(A_i)+z_(B_i)`.

For the macroprofile inclusion flow

\[
 F_{k,\ell}
 ={V_k\over\binom mq}\prod_j\binom{k_j}{\ell_j},                 \tag{8.4}
\]

the row-side deletion coefficients are

\[
                         \prod_j\binom{k_j}{\ell_j}.                \tag{8.5}
\]

For the target-rooted carrier bank, put `d_j=k_j-ell_j` and use

\[
 \binom8{k_j}\binom{k_j}{\ell_j}
 =\binom8{\ell_j}\binom{8-\ell_j}{d_j}.                            \tag{8.6}
\]

Consequently the exact physical extension coefficients required around
one target are proportional to

\[
                         \prod_j\binom{8-\ell_j}{d_j},             \tag{8.7}
\]

not to (8.5) without the source-orbit factor.  Equations
(8.2)--(8.7) are the exact dispersion property that a target-rooted
local-factor library must satisfy.  Marginal balance alone does not imply
the needed physical pairing.

Finally suppose every touched local target has at most `t` pairwise
owner-disjoint carrier cells.  Repeating the argument of Section 6 gives

\[
                         \rho_{r,q}
                         \le {t^q(r-q+1)\over\binom rq}.            \tag{8.8}
\]

To keep the right side bounded away from zero one needs

\[
 t\ge
 \exp\left({\log\binom rq-\log(r-q+1)+O(1)\over q}\right).        \tag{8.9}
\]

Using (6.5),

\[
                         t\ge(e-o(1)){r\over q}                    \tag{8.10}
\]

when `q=o(r)` and `log r=o(q)`, in particular in the Gaussian regime.
Proposition 1.3 then forces at least `2t` available
middle extensions of each local target.  Therefore every bounded-width
carrier atlas, including the double carrier above, is quantitatively
insufficient in the regime `r/q -> infinity`.

## 9. Proved boundary

The positive statements are exact:

* sixteen owners already support two disjoint `Q_3` carriers of one
  labelled target;
* the carriers can be put in distinct macroprofile sectors;
* their tensor realizes the integral polynomial (3.7);
* for one fixed touched macroprofile, a physical cycle factor covers every
  labelled target with multiplicity `4^q/h`;
* one factor simultaneously reaches the positive fraction (5.3).

The negative statement is equally exact: bounded local carrier branching
does not absorb the entropy of all `q`-block windows when `r/q` grows.
The next construction must supply a growing carrier bank whose endpoint
matching has size `Omega(r/q)`, whose target-rooted type multiplicities
satisfy (8.6)--(8.7), and whose upper-window action is coupled compatibly.  Merely
tensoring the smallest nonunique carrier does not close coefficient one.
