# Eight-block-rotation-equivariant `B_4` packets and the exact quartet-occurrence obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Verdict

The exact 24-owner three-shore associator and the audited recursive
context-array compiler do produce a genuine **eight-block-rotation-
equivariant, cellwise typed-frame** packet catalogue with all of the
following properties.

1. It retains
   \[
                         G=W-e^{-\Omega(m)}W,
   \qquad                 W=\binom{2m}{m},
   \tag{0.1}
   \]
   middle owners.
2. A positive density of disjoint eight-coordinate carriers is active.
3. On every active carrier all three perfect matchings of its special
   quartet are available on the same 24 owners as three complete six-cell
   shore resolutions. A shore is not one ambient perfect matching common
   to all 24 owners: four cells use the selected special matching and two
   cells use the reservoir frame.
4. The three-shore cell-incidence union is connected inside every local
   carrier, and its tensor union is connected at packet scale.
5. Every packet has size `24^r=o(W/H)` for every `H=O(\sqrt m\,\omega(m))`
   with `\log\omega=o(m)`, while the number of packets is exponential.
6. Every selected resolution is an integral exact factor. The verified
   context array installs physical long cycles and gives both signed trace
   injectivity inside every selected cube cell through every fixed Gaussian
   window.

Thus neither rotation equivariance, owner integrality, positive matching
action density, raw component size, nor local trace injectivity is the
failure.

The failure is an exact occurrence invariant of the paired physical lift.
Fix the underlying partition of the coordinates into four-sets and put

\[
 K(S)=\#\{B:|S\cap B|=3\}.                           \tag{0.2}
\]

For one signed depth-`q` occurrence, let `t` be the number of four-sets in
which the window uses exactly one of the two local directions. If `L` and
`U` are its literal lower and upper traces, then

\[
                         \boxed{K(U)=K(L)+t.}         \tag{0.3}
\]

This identity is independent of the chosen shore, the context, the row,
the cycle phase, and every componentwise shore choice.

The audited canonical paired context compiler places the two directions of
every local four-set consecutively. Therefore every cyclic interval has

\[
                              t\le2.                 \tag{0.4}
\]

At `q=\lfloor A\sqrt m\rfloor`, the uniform rank-`m-q` and rank-`m+q`
target laws have `K`-centres separated by `q/2+O_A(1)` and common standard
deviation `\sqrt m/4+o(\sqrt m)`. The exact two-sign threshold cut below
therefore gives

\[
 \boxed{
 M_q^-+M_q^+
 \ge
 \left(2e^{-A^2}\Phi(A)-1-o(1)\right)W.}             \tag{0.5}
\]

The coefficient in (0.5) is positive for every sufficiently small fixed
`A>0`. Hence this moving-frame atlas has a linear simultaneous Hall
deficit. The result concerns actual literal target occurrences, not
coordinate or frame marginals.

The construction above is equivariant under cyclic permutation of the
eight-blocks (an eight-coordinate shift on the clean subsequence), not
under one-coordinate or one-original-pair rotation. It therefore does not
construct the fully rotation-equivariant overlapping ambient-frame atlas
asked for in the strongest formulation. The obstruction is sharp in
scope. To escape it one must do at least one
of the following.

* Replace the paired context compiler by a legal all-depth compiler whose
  actual windows realize the full `K`-class transport centred at `t=q/2`,
  rather than merely balancing direction marginals.
* Change the underlying four-set partition on a positive fraction of all
  occurrences by a genuinely joint overlapping-carrier construction.

The second operation is not supplied by the existing 24-owner atom.
Adjacent overlapping atoms have non-laminar supports, and the recursive
context array factors a cube only after its owner cell has been chosen. It
does not construct their common-support closure. The projected first
overlap on the six special coordinates already has a 16-owner active
component and frozen central sectors, as proved in Section 7; a physical
component size additionally depends on the reservoir-overlap architecture.

No universal no-go for every moving-frame catalogue is claimed. Averaging
whole coordinate conjugates gives an exact symmetric fractional cover, so
no partition-independent fractional Hall cut can exist. The theorem closes
the literal disjoint-24-carrier plus paired-context-array route and isolates
the exact additional object needed to go further.

## 1. The 24-owner three-shore carrier

Let `A` and `R` be disjoint four-sets. Write

\[
 A=\{1,2,3,4\},\qquad R=\{u,v,w,x\},                 \tag{1.1}
\]

and put

\[
 \mathcal Y=\{uw,vw,vx,ux\},\qquad
 \mathcal V=\binom A2\times\mathcal Y.              \tag{1.2}
\]

Thus `\mathcal V` consists of 24 rank-four owners. Let

\[
 M_0=12\mid34,\qquad
 M_1=13\mid24,\qquad
 M_2=14\mid23                                      \tag{1.3}
\]

be the three perfect matchings of `A`. For `c\in\{0,1,2\}`, set

\[
 A_c=\binom A2\setminus M_c.                         \tag{1.4}
\]

The six `Q_2` cells of shore `c` are

\[
 H_{c,y}=A_c\times\{y\}\quad(y\in\mathcal Y),
 \qquad
 V_e=\{e\}\times\mathcal Y\quad(e\in M_c).         \tag{1.5}
\]

The four horizontal cells use the two matched-pair orientation directions
of `M_c`; the two vertical cells use the two reservoir directions. These
six cells partition the common owner set `\mathcal V`.

### Lemma 1.1 (exact local overlap)

For distinct shores `c,d`, order the cells as the four horizontal cells
followed by the two vertical cells. Their owner-intersection matrix is

\[
 B_{cd}=
 \begin{pmatrix}
 2I_4&J_{4,2}\\
 J_{2,4}&0
 \end{pmatrix}.                                      \tag{1.6}
\]

In particular the bipartite cell-overlap graph of any two shores is
connected.

#### Proof

The matchings `M_c,M_d` are disjoint and together use four of the six
edges of `K_4`. Hence

\[
 |A_c\cap A_d|=2,qquad M_d\subset A_c,qquad
 M_c\subset A_d,qquad M_c\cap M_d=\varnothing.      \tag{1.7}
\]

Horizontal cells with different reservoir states are disjoint, while
equal reservoir states meet in the two special edges in `A_c\cap A_d`.
Every horizontal cell of one shore meets both vertical cells of the other
shore in one owner. Vertical cells belonging to distinct matchings are
disjoint. This is exactly (1.6).

Moreover

\[
 B_{cd}B_{cd}^{\mathsf T}
 =
 \begin{pmatrix}
 4I_4+2J_4&2J_{4,2}\\
 2J_{2,4}&4J_2
 \end{pmatrix},                                      \tag{1.8}
\]

which is entrywise positive. Any two cells on one shore therefore have a
common neighbour on the other shore. The overlap graph is connected.
`\square`

### Lemma 1.2 (tensor component law)

On `\mathcal V^r`, compare two shore vectors which differ in exactly `d`
coordinates. Their raw cell-overlap graph has exactly

\[
                              6^{r-d}                \tag{1.9}
\]

components. Every component has

\[
                24^d4^{r-d}=4^r6^d                 \tag{1.10}
\]

owners. Allowing all three shores in those `d` coordinates gives the same
components. In particular, if every coordinate is flexible, the raw
cell-resolution union is connected on all `24^r` packet owners.

#### Proof

In every unchanged coordinate the common cell label is fixed, giving six
choices and four owners. In every changed coordinate Lemma 1.1 gives one
connected 24-owner overlap component. Cartesian products give (1.9) and
(1.10). Since every pair of distinct local shores already connects all of
`\mathcal V`, adding the third shore does not refine a component.
`\square`

This is a statement about the complete owner cells. A later long-cycle
factor may refine a raw overlap component into smaller cycle-overlay
components; that only increases choice granularity. No assertion that one
fixed finite context subcatalogue has a connected long-cycle overlay is
needed below.

## 2. An eight-block-rotation-equivariant dispersed packet selector

Assume first that `4\mid m`. Partition the `2m` coordinates cyclically into

\[
                         b=m/4                     \tag{2.1}
\]

ordered eight-blocks

\[
                         C_i=A_i\dot\cup R_i,
 \qquad i\in\mathbb Z_b,                            \tag{2.2}
\]

with `|A_i|=|R_i|=4`. Put a copy `\mathcal V_i` of (1.2) in every block.
Call block `i` eligible for a middle owner `X` when

\[
                         X\cap C_i\in\mathcal V_i.  \tag{2.3}
\]

Let `e(X)\in\{0,1\}^{\mathbb Z_b}` be the eligibility word and let `E(X)`
be its number of ones. Under independent fair-bit sampling, the block
eligibility events are independent and have probability

\[
                         p_0={24\over2^8}={3\over32}.\tag{2.4}
\]

Choose an allowed context dimension

\[
                         r=4\cdot2^a                \tag{2.5}
\]

to be the largest such integer satisfying

\[
                         r\le {p_0b\over2}.          \tag{2.6}
\]

For all large `m`,

\[
                  {p_0b\over4}<r\le {p_0b\over2},   \tag{2.7}
\]

so a positive density of the eight-blocks is active.

If `e(X)` is aperiodic, root its cyclic word at its unique
lexicographically least rotation. List the eligible positions in cyclic
order from that root as

\[
                         a_0,a_1,\ldots,a_{E-1}.     \tag{2.8}
\]

When `E\ge r`, select

\[
 I(X)=
 \left\{a_{\lfloor jE/r\rfloor}:0\le j<r\right\}.   \tag{2.9}
\]

The floor indices in (2.9) are distinct because `E/r\ge1`.

Freeze `X` outside the selected blocks and allow every selected block to
range through its common 24-owner carrier:

\[
 \mathcal P(X)=
 \left\{Y:
 \begin{array}{l}
 Y\setminus\bigcup_{i\in I(X)}C_i
 =X\setminus\bigcup_{i\in I(X)}C_i,\\
 Y\cap C_i\in\mathcal V_i\quad(i\in I(X))
 \end{array}
 \right\}.                                          \tag{2.10}
\]

### Theorem 2.1 (exact eight-block-equivariant packet partition)

After duplicate names are identified, the sets `\mathcal P(X)` partition
all middle owners for which `e(X)` is aperiodic and `E(X)\ge r`. Every
packet has exactly

\[
                         |\mathcal P|=24^r           \tag{2.11}
\]

owners. The partition is equivariant under cyclic permutation of the
eight-blocks. This is the rotation group generated by an eight-coordinate
block shift, not the full one-coordinate cyclic group.

#### Proof

Every state of `\mathcal V_i` remains eligible. All unselected blocks are
frozen. Therefore varying the selected carriers leaves the entire binary
word `e(X)` unchanged, not just its number of ones. Its canonical root,
the list (2.8), and the systematic sample (2.9) are unchanged. Hence every
owner of `\mathcal P(X)` names the same packet. Two packets which meet are
therefore equal, and every retained owner lies in its own packet. The
selected blocks vary independently over 24 states, proving (2.11).

Cyclic rotation shifts the unique least-rotation root, the ordered eligible
list, and the selected block set by the same amount. It also conjugates
the frozen exterior. Thus it maps packets to packets.
`\square`

### Theorem 2.2 (exponentially small leave)

The retained owner count satisfies

\[
                         G=W-e^{-\Omega(m)}W.         \tag{2.12}
\]

#### Proof

Before rank conditioning, `E\sim\operatorname{Bin}(b,p_0)`. By (2.6), a
Chernoff bound gives

\[
                         \Pr(E<r)\le e^{-c_1b}        \tag{2.13}
\]

for an absolute `c_1>0`.

For a proper cyclic period `d\mid b`, put `k=b/d\ge2`. A Bernoulli-`p_0`
word with period dividing `d` has probability

\[
                         (p_0^k+(1-p_0)^k)^d.         \tag{2.14}
\]

Monotonicity of finite `\ell_s` norms gives

\[
 (p_0^k+(1-p_0)^k)^{1/k}
 \le(p_0^2+(1-p_0)^2)^{1/2}<1.                       \tag{2.15}
\]

Summing (2.14) over the at most `b` proper periods gives `e^{-c_2b}` for
an absolute `c_2>0`.

Finally

\[
 \Pr_{1/2}(|X|=m)=4^{-m}W\ge {1\over2m+1}.           \tag{2.16}
\]

Conditioning on the middle rank therefore costs only the factor `2m+1`.
Equations (2.13)--(2.16) prove (2.12).
`\square`

The construction is also genuinely dispersed rather than a rotating
first-eligible arc. If `J` is any cyclic interval of block positions and
`E_J` is its number of eligible positions, then the systematic sample
obeys the deterministic discrepancy bound

\[
 \left||I(X)\cap J|-{rE_J\over E}\right|\le2.        \tag{2.17}
\]

Indeed the eligible ranks belonging to `J` form at most two cyclic rank
intervals, and the Beatty sample `\{\lfloor jE/r\rfloor\}` has discrepancy
at most one on each rank interval. Uniform Hoeffding bounds over the at
most `b^2` cyclic intervals then show that, outside `o(W)` owners,

\[
 |I(X)\cap J|
 ={r|J|\over b}+O(\sqrt{b\log b})                   \tag{2.18}
\]

simultaneously for all `J`. Thus no fixed positive-density arc contains
all active carriers.

For general `m`, use `\lfloor m/4\rfloor` full eight-blocks and freeze the
fewer than eight remaining coordinates. The same packet and leave proof
applies in each fixed remainder context, with unchanged asymptotic
estimates. Rotation then means the abstract cyclic permutation of the full
blocks fixing the remainder. The exact quartet formulas in Sections 4--6
are stated on the clean subsequence `4\mid m`; a bounded remainder changes
their means and variances by `O(1)` and leaves every limiting Hall constant
unchanged.

## 3. Integral packet factors and component scale

Fix one packet. Before applying the compiler, identify the two `Q_2`
directions of carrier `i` with the adjacent ordered physical pair
`(b_i,a_i)` belonging to coarse context direction `i`. This prescribed
carrier-pair identification is part of the catalogue. Arbitrary direction
permutations which separate `a_i` from `b_i` are not included.

A shore vector

\[
                         \theta\in\{0,1,2\}^r       \tag{3.1}
\]

partitions it into `6^r` cells, each isomorphic to `Q_{2r}`. By (2.5), the
audited recursive context-array theorem, followed by its paired physical
lift, installs an exact physical `C_{4r}`-factor in every cell. Its two
directions belonging to one carrier are consecutive, and both lower and
upper literal traces are injective for every physical depth

\[
                         q\le r/2-1.                 \tag{3.2}
\]

This uses one whole shore resolution before compiling the cell. It does
not require the nonexistent common four-phase colouring of all three
shores.

The packet catalogue therefore contains `3^r` integral exact resolutions,
and it permits a positive density of its carrier matchings to differ from
the base shore. Lemma 1.2 shows that its complete raw resolution union is
connected on the packet.

The largest possible interaction component is bounded by the packet size
`24^r`. From (2.1), (2.4), and (2.6),

\[
                         r\le {3m\over256}.          \tag{3.3}
\]

Consequently

\[
 {24^r\over W}
 \le
 \exp\left[-\left(\log4-{3\log24\over256}-o(1)\right)m\right]
 =e^{-\Omega(m)}.                                    \tag{3.4}
\]

In particular `24^r=o(W/H)` for every `H=e^{o(m)}`, and there are
exponentially many independently selectable packets. If `H` is also the
protected trace radius, the compiler additionally requires
`H\le r/2-1`; every `H=O(\sqrt m\,\omega(m))` with
`\omega=m^{o(1)}` satisfies this for all large `m`. This verifies the
component scale in the certified range. The Hall failure below persists
even if the compiled cycle overlay fragments into still smaller selectable
pieces.

## 4. The exact quartet ledger

Sections 4--6 are stated on the clean subsequence `4\mid m`, so all `2m`
coordinates lie in the quartets below. This already suffices to disprove a
purported all-`m` construction in the stated architecture. As noted after
Theorem 2.2, a bounded remainder changes no limiting conclusion.

The eight-block partition gives a fixed partition of the coordinates into

\[
                         m/2                         \tag{4.1}
\]

quartets: the special and reservoir quartet of every carrier block. In a
chosen shore cell, precisely one of those two quartets supplies the two
active physical directions; the other is fixed. Every active quartet has
middle occupancy two.

Consider one isometric depth-`q` window with `q\le2r`. Since no physical
direction repeats, let

\[
 d_B\in\{0,1,2\}                                    \tag{4.2}
\]

be the number of its two directions from quartet `B` which occur in the
window, and put

\[
                         t=\#\{B:d_B=1\}.            \tag{4.3}
\]

Let `L` be the intersection and `U` the union of the consecutive middle
states in the window.

### Lemma 4.1 (statewise quartet identity)

For every literal occurrence,

\[
                         K(U)-K(L)=t.                \tag{4.4}
\]

#### Proof

On an active quartet the local path is a geodesic in `Q_2`. Its local
intersection and union sizes are

\[
\begin{array}{c|ccc}
d_B&0&1&2\\ \hline
|L\cap B|&2&1&0\\
|U\cap B|&2&3&4.
\end{array}                                          \tag{4.5}
\]

Thus the local contribution to `K(U)-K(L)` is respectively `0,1,0`.
Every inactive quartet is fixed along the window and contributes equally
to `K(L)` and `K(U)`. Summing (4.5) proves (4.4).
`\square`

The lemma does not mention a matching. It therefore survives all three
shores, every coarse carrier order which keeps each prescribed carrier
pair consecutive, cycle rotations and reversals, affine translations, and
choices made independently on raw or refined overlay components. An
arbitrary direction conjugation which separates the two directions of a
carrier lies outside the paired catalogue and need not satisfy (4.6).

### Corollary 4.2 (paired and sibling extremes)

In the paired context-array lift,

\[
                              t\le2.                 \tag{4.6}
\]

In a one-direction-per-carrier sibling schedule,

\[
                              t=q                   \tag{4.7}
\]

through its certified shallow range.

#### Proof

In the paired lift the two directions of every active quartet are adjacent
in the cyclic direction word. A cyclic interval contains complete adjacent
pairs except possibly at its two boundary cuts, proving (4.6). In the
sibling shallow schedule every touched carrier contributes exactly one
direction, proving (4.7).
`\square`

## 5. The target `K` law

Write `\Phi` and `\phi` for the standard normal distribution function and
density.

Let `T_k` be uniformly distributed on `\binom{[2m]}k`, where the coordinates
are partitioned into `m/2` quartets. Put

\[
                         \mu_k=\mathbb E K(T_k).      \tag{5.1}
\]

### Lemma 5.1 (exact mean)

For every `k`,

\[
 \mu_k=
 {k(k-1)(k-2)(2m-k)
  \over(2m-1)(2m-2)(2m-3)}.                         \tag{5.2}
\]

For `k=m\pm q`,

\[
 \mu_{m+q}-\mu_{m-q}
 ={2q(m^2-q^2)\over(2m-1)(2m-2)}.                   \tag{5.3}
\]

If `q=O_A(\sqrt m)`, then

\[
 \mu_{m\pm q}={m\over8}\pm{q\over4}+O_A(1),
 \qquad
 \mu_{m+q}-\mu_{m-q}={q\over2}+O_A(m^{-1/2}).       \tag{5.4}
\]

#### Proof

A fixed quartet has three selected coordinates with probability

\[
 4{\binom{2m-4}{k-3}\over\binom{2m}k}
 ={4(k)_3(2m-k)\over(2m)_4}.                         \tag{5.5}
\]

Multiplying by `m/2` and cancelling `2m` gives (5.2).

Write `k=m+x`. The numerator of (5.2) is

\[
 (m^2-x^2)\bigl((m+x)^2-3(m+x)+2\bigr).             \tag{5.6}
\]

Its odd part is `(m^2-x^2)(2m-3)x`. Subtracting the values at `x=q`
and `x=-q` cancels the factor `2m-3` in the denominator and gives (5.3).
Expansion gives (5.4).
`\square`

### Lemma 5.2 (conditional Gaussian law)

If

\[
                         {q\over\sqrt m}\longrightarrow A,
 \qquad A\ge0,                                      \tag{5.7}
\]

then, for either sign,

\[
 {K(T_{m\pm q})-\mu_{m\pm q}\over\sqrt m/4}
 \Longrightarrow N(0,1).                            \tag{5.8}
\]

#### Proof

Under independent fair-bit sampling, let `Y_i` be the number of selected
coordinates in quartet `i` and let `I_i={\bf1}_{\{Y_i=3\}}`. The pairs
`(Y_i,I_i)` are independent and

\[
\begin{aligned}
 \mathbb EY_i&=2,& \operatorname{Var}Y_i&=1,\\
 \mathbb EI_i&={1\over4},&
 \operatorname{Var}I_i&={3\over16},\\
 \operatorname{Cov}(Y_i,I_i)&={1\over4}.
\end{aligned}                                        \tag{5.9}
\]

Conditioning on `\sum_iY_i=k` gives the uniform rank-`k` law. The support
points `(0,0),(1,0),(2,0),(3,1),(4,0)` generate the full lattice
`\mathbb Z^2`. The bivariate lattice local central limit theorem therefore
applies uniformly when `k-m=O(\sqrt m)`. For completeness, it follows by
Fourier inversion: on a fixed neighbourhood of the origin, the logarithm
of the joint characteristic function is its quadratic covariance form
plus `O(|\theta|^3)`; outside that neighbourhood its modulus is uniformly
less than one by the full-lattice support; splitting the inversion integral
at radius `m^{-2/5}` makes the cubic term `o(1)` and the outer integral
exponentially small.

The conditional variance per quartet is the Schur complement

\[
 {3\over16}-{(1/4)^2\over1}={1\over8}.               \tag{5.10}
\]

There are `m/2` quartets, so the conditional variance is
`m/16+o(m)`. The conditional regression shift is

\[
 {\operatorname{Cov}(I,Y)\over\operatorname{Var}Y}(k-m)
 ={k-m\over4},                                      \tag{5.11}
\]

in agreement with (5.4). The conditional local limit obtained from the
same Fourier integral yields (5.8).
`\square`

Finally, with

\[
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q},                \tag{5.12}
\]

the product formula gives

\[
 {N_q\over W}\longrightarrow e^{-A^2}.              \tag{5.13}
\]

Indeed

\[
 \log{N_q\over W}
 =\sum_{j=0}^{q-1}\log{m-j\over m+j+1}
 =-{q^2\over m}+o(1).                               \tag{5.14}
\]

## 6. The two-sign Gaussian Hall cut

Let an integral middle factor give one lower and one upper depth-`q` trace
from every middle owner. Let `M_q^-` and `M_q^+` be the numbers of literal
rank-`m-q` and rank-`m+q` targets, respectively, which receive no
occurrence.

### Theorem 6.1 (low-`t` cut)

Suppose `q/\sqrt m\to A>0` and every occurrence satisfies

\[
                         t\le t_m,
 \qquad {t_m\over\sqrt m}\longrightarrow\tau<{A\over2}.       \tag{6.1}
\]

Then

\[
 \boxed{
 M_q^-+M_q^+
 \ge
 \left(2e^{-A^2}\Phi(A-2\tau)-1-o(1)\right)W.}      \tag{6.2}
\]

#### Proof

Put

\[
                         a_m=\left\lfloor{m\over8}
                         -{\tau\sqrt m\over2}\right\rfloor.   \tag{6.3}
\]

Consider the two target families

\[
\begin{aligned}
 \mathcal A^-&=\{T\in\tbinom{[2m]}{m-q}:K(T)\le a_m\},\\
 \mathcal A^+&=\{T\in\tbinom{[2m]}{m+q}:K(T)\ge a_m+t_m+1\}.
\end{aligned}                                        \tag{6.4}
\]

No owner occurrence can hit one target in each family. Otherwise (4.4)
would give `t\ge t_m+1`.

By (5.4), (5.8), and (6.3),

\[
 {a_m-\mu_{m-q}\over\sqrt m/4}\longrightarrow A-2\tau,        \tag{6.5}
\]

and

\[
 {a_m+t_m+1-\mu_{m+q}\over\sqrt m/4}
 \longrightarrow 2\tau-A.                           \tag{6.6}
\]

Thus

\[
 |\mathcal A^-|+|\mathcal A^+|
 =\left(2\Phi(A-2\tau)+o(1)\right)N_q.              \tag{6.7}
\]

There are `W` owner occurrences, and each covers at most one member of
the disjoint test union in (6.4). At most `W` of its targets can therefore
be hit. Hence

\[
 M_q^-+M_q^+
 \ge |\mathcal A^-|+|\mathcal A^+|-W.                \tag{6.8}
\]

Equations (5.13), (6.7), and (6.8) give (6.2).
`\square`

### Theorem 6.2 (high-`t` cut)

If instead

\[
                         t\ge t_m,
 \qquad {t_m\over\sqrt m}\longrightarrow\tau>{A\over2},       \tag{6.9}
\]

then

\[
 \boxed{
 M_q^-+M_q^+
 \ge
 \left(2e^{-A^2}\Phi(2\tau-A)-1-o(1)\right)W.}      \tag{6.10}
\]

#### Proof

Use the same `a_m` as in (6.3), but take

\[
 \mathcal B^-=\{K(L)\ge a_m\},
 \qquad
 \mathcal B^+=\{K(U)\le a_m+t_m-1\}.                \tag{6.11}
\]

Equation (4.4) makes the two events incompatible for one occurrence.
The two standardized thresholds now give probability
`\Phi(2\tau-A)+o(1)` on each target layer. The counting proof of Theorem
6.1 applies verbatim.
`\square`

### Corollary 6.3 (the paired context compiler fails simultaneous Hall)

There exists an absolute `A_0>0` such that, for every fixed
`0<A<A_0` and `q=\lfloor A\sqrt m\rfloor`, every completion of a retained
packet factor from Sections 2--3 on its exponentially small exceptional
owner set satisfies

\[
 M_q^-+M_q^+
 \ge
 \left(c_A-o(1)\right)W,
 \qquad
 c_A=2e^{-A^2}\Phi(A)-1>0.                           \tag{6.12}
\]

#### Proof

Since `r=\Theta(m)`, the chosen `q=\lfloor A\sqrt m\rfloor` satisfies
`q\le r/2-1` for all large `m`. Corollary 4.2 gives `t_m=2`, hence
`\tau=0`. Apply the proof of Theorem 6.1 to the `G` retained occurrences.
Each of the `E=W-G` arbitrary completion occurrences can hit both test
families, so the bound loses at most `E=e^{-\Omega(m)}W=o(W)`. This gives
(6.12). The function `g(A)=2e^{-A^2}\Phi(A)-1` satisfies

\[
                         g(0)=0,
 \qquad                 g'(0)=2\phi(0)>0.           \tag{6.13}
\]

It is therefore positive on some interval `(0,A_0)`.
`\square`

If `E=o(W)` exceptional owners use arbitrary factors, they can hit both
test families and change (6.2) by at most `E`. In the packet construction
`E=e^{-\Omega(m)}W`, so (6.12) is unchanged. More generally, suppose a
fraction `1-\eta_m` of the occurrences uses the fixed quartet partition
and satisfies the low-`t` hypothesis, while the remaining `\eta_m`
fraction is arbitrary. Genuinely different quartet partitions are one
source of such exceptions. Then the robust bound is

\[
 M_q^-+M_q^+
 \ge
 \left(2e^{-A^2}\Phi(A-2\tau)-1-\eta_m-o(1)\right)W. \tag{6.14}
\]

Indeed a good occurrence can hit at most one test target, while an
exceptional occurrence can hit at most two.

The centre `q/2` is exact, not a heuristic based on marginals. If `N_q`
owner occurrences biject simultaneously onto both complete target layers,
summing (4.4) and using Lemma 5.1 forces

\[
 {1\over N_q}\sum t
 =\mu_{m+q}-\mu_{m-q}
 ={2q(m^2-q^2)\over(2m-1)(2m-2)}
 ={q\over2}+o(\sqrt m).                              \tag{6.15}
\]

Theorems 6.1--6.2 say more: a uniform macroscopic displacement of the
actual `t` profile to either side of this centre creates a literal linear
two-sign cut.

## 7. Why overlapping associators are a new theorem

The fixed-quartet cut can only be escaped by changing the quartet
partition on enough occurrences, or by constructing windows with the
correct internal `t` profile. It is tempting to overlap adjacent 24-owner
associators to move the partition. Their supports do not tensor.

Let `A,B,C` now denote three base coordinate pairs. An associator on
`A\cup B` requires

\[
                         |X\cap(A\cup B)|=2,         \tag{7.1}
\]

besides its split reservoir condition. A second associator on `B\cup C`
requires the analogous equality. Fix `|X\cap C|=1`. Inside the connected
rank-two `A\cup B` carrier, the occupancy of `B` takes the values `0,1,2`.
Consequently `|X\cap(B\cup C)|` takes `1,2,3`. Eligibility of the second
carrier is not constant on the first carrier. Thus the two support
predicates are non-laminar and cannot serve as independent tensor
coordinates.

The smallest overlap can be classified exactly after projecting away the
reservoir coordinates. At total special-coordinate occupancy three, write

\[
                         (a,b,c)=
 (|X\cap A|,|X\cap B|,|X\cap C|).                   \tag{7.2}
\]

The `AB` relation acts when `a+b=2`; the `BC` relation acts when `b+c=2`.
The five count classes

\[
                         111,\quad021,\quad201,\quad102,\quad120     \tag{7.3}
\]

form one component. Their physical owner counts are respectively

\[
                         8,2,2,2,2,                 \tag{7.4}
\]

so this projected component has 16 special-coordinate owners. If both
moves use one common split four-state reservoir and no other reservoir
edges merge it, it lifts to 64 owners; two private four-state reservoirs
give the Cartesian size 256. Other reservoir-overlap architectures can
produce other physical components and must be audited separately. The
remaining projected central count words

\[
                         012,qquad210               \tag{7.5}
\]

admit neither projected move. Their two special-coordinate orientations
give four projected singleton states. This proves non-laminarity, but it
does not assert a reservoir-independent physical component size. In
particular, connectedness of the union of coordinate matching edges does
not by itself prove connectedness of the actual 24-carrier owner overlap.

For contrast, suppose one postulates the strictly stronger *full-status
closure*: every orientation cell of every admitted matching is available.
Let `G` be the union graph of all matching edges and let its coordinate
components be `D_1,\ldots,D_s`. Then the exact middle-owner components are

\[
 \mathcal U_{\boldsymbol\kappa}
 =\left\{X:|X\cap D_j|=\kappa_j\text{ for all }j\right\},
 \qquad
 |\mathcal U_{\boldsymbol\kappa}|
 =\prod_j\binom{|D_j|}{\kappa_j}.                    \tag{7.6}
\]

Necessity follows from occupancy conservation. Sufficiency follows because
the exclusion graph on the `k`-subsets of a connected graph is connected:
move particles along a spanning tree to a fixed canonical `k`-set.

A connected chain on `v` base pairs would therefore have a central
full-status component of size

\[
                         \binom{2v}{v}
 \sim {4^v\over\sqrt{\pi v}}.                       \tag{7.7}
\]

In particular a globally connected matching atlas has the whole middle
layer as one component. But (7.6)--(7.7) must not be attributed to the
24-owner atom: the 16-state projected component and the frozen projected
sectors (7.3)--(7.5) show that the atom does not supply the missing status
strata.

The recursive context array does not repair this defect. It produces an
exact factor and trace code on a fixed active cube after the cube has been
selected. It neither makes the predicates (7.1) laminar nor supplies an
integral joint factor on their union.

## 8. Independently audited implication boundary

The following statements are unconditional.

1. The dispersed selector of Section 2 is an exact eight-block-rotation-
   equivariant partition with exponential leave.
2. Every packet admits all `3^r` whole three-shore resolutions.
3. The raw cell-resolution union is packetwise connected and every owner
   interaction component is contained in a packet of size `24^r=o(W/H)`.
4. The audited context-array theorem compiles every chosen `Q_{2r}` cell
   integrally and gives both signed local trace injectivity in the required
   range.
5. The literal identity (4.4), the exact means (5.2)--(5.4), the Gaussian
   law (5.8), and the Hall cuts (6.2), (6.10) hold for actual occurrences.
6. Therefore the paired context-array, cellwise three-shore atlas has the
   linear simultaneous deficit (6.12).
7. Adjacent overlapping 24-owner carriers do not compose as independent
   Cartesian coordinates under the packetization of Section 2; their first
   special-coordinate support projection is exactly (7.3)--(7.5), while
   physical component sizes depend on reservoirs. A different joint factor
   is not ruled out.

The following statements are **not** proved and are not used.

* Compiled long-cycle overlays need not have the same components as raw
  cell overlays.
* Coordinate-edge connectedness does not imply actual 24-carrier owner
  connectedness.
* A sequence of local matching switches does not by itself give a common
  owner partition on all matching status strata.
* Balanced frame, coordinate, or shore marginals do not imply the required
  targetwise occurrence loads.
* The fixed-quartet Hall cut does not apply after a large fraction of
  genuinely different quartet partitions has been integrally installed.

Indeed the full `S_{2m}` average of whole legal atlases gives every signed
target at depth `q` the exact fractional load `W/N_q`. Thus a universal
partition-independent fractional obstruction would be false.

The shortest live successor is consequently one of the following exact
lemmas.

> **Joint overlapping-carrier lemma.** Construct a common-owner integral
> factor for a growing connected family of overlapping `B_4` supports,
> together with a shore-stable rotation-equivariant selector, packet
> components `o(W/H)`, complete lower/upper crossing collars, and actual
> all-depth target histograms.

or

> **Centred-`t` context compiler lemma.** On the disjoint packet atlas,
> construct integral long factors whose common lower/upper occurrence
> coupling realizes the full quartet-profile transport around
> `t=q/2+o(\sqrt m)` simultaneously for every `q\le A\sqrt m`, while
> retaining trace injectivity and `o(W)` aggregate literal holes.

Either lemma would evade the theorem. Neither follows from the present
24-owner associator or the verified paired context-array compiler.
