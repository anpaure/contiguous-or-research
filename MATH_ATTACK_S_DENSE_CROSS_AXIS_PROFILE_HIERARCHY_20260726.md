# Dense cross-axis height-profile recursion: exact local matching, audited Hall toll, and the remaining SCD gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

This note continues the SCD/promotion lane after the fixed-quartet
\(\frac14W\) flux obstruction.  It combines four exact facts.

1. The common-radius two-scale construction in
   `MATH_ATTACK_S_TWO_SCALE_COMMON_RADIUS_PROMOTION_20260726.md` is sound.
   It sits inside one literal full product SCD and satisfies

   \[
      G_t(z_{R,j})=z_{R,j+t},\qquad
      G_1(G_tz_{R,j})=G_{t+1}z_{R,j}                 \tag{0.1}
   \]

   with the literal deletion and insertion tails.  In four copies of
   \(B_{2s}\) it covers

   \[
      \Theta\!\left(\binom{8s}{4s}/\sqrt s\right)    \tag{0.2}
   \]

   middle owners and has \(\Theta(\binom{8s}{4s}/s)\) induced path
   components.  Every nonterminal top-scale move crosses the two parent
   carriers.  This is an exact dense-cross-axis SCD sector, but its density
   is still \(o(1)\).

2. The claimed Gaussian Hall cut for the complete block-internal quartet
   atlas has been independently checked.  At
   \(q=A\sqrt m+O(1)\), the number of full quartets is conserved on the
   lower side, and at

   \[
      k={m\over32}-{A\over4}\sqrt m+O(1)             \tag{0.3}
   \]

   the exact middle-source/target ratio tends to

   \[
                         e^{-A^2/11}.                 \tag{0.4}
   \]

   A positive fraction of the target layer lies in a fixed-width
   \(\sqrt m\)-window around (0.3).  Hence every successful factor has
   \(\Omega_A(W)\) depth-\(q\) windows containing a physically
   cross-quartet axis.  In a \(Q_r\) packet this forces the weighted mean

   \[
      {1\over W}\sum_Ps(P)|P|=\Omega_A(r/q),          \tag{0.5}
   \]

   where \(s(P)\) is the number of crossing axes.  The upper statement is
   the complementary empty-quartet statement.

3. The proposed cross-half graph supplies the required owner-scale density.
   In a \(2d\)-coordinate block \(A\dot\cup B\), the cross-exchange graph
   on every rank has a matching saturating its smaller
   \(|X\cap A|\)-parity shore.  A first-split involution proves this
   exactly.  Tensoring logarithmic blocks and allowing the local bijection
   \(A\to B\) to depend on the local rank gives an integral owner-disjoint
   near-tiling by \(Q_r\)'s with

   \[
      r=\Theta(m/\log m),\qquad
      L\le 2^{m+o(m)}=o(W/H),                         \tag{0.6}
   \]

   and all \(r\) axes of every retained packet crossing the original
   quartet partition.  Thus every protected nonzero window is a crossing
   window, far exceeding the necessary scale (0.5).

4. The next obstruction is exact.  If the same cross-half bijection is
   used at every local rank, all axes lie in one global perfect matching,
   and the fixed-pair Gaussian Hall cut remains linear.  Rank-dependent
   bijections remove this invariant and can make the used local edge union
   the full \(K_{d,d}\).  A remaining common invariant—full logarithmic
   macroblocks below and empty macroblocks above—is asymptotically too weak
   to yield a Gaussian Hall cut.  What remains is the actual all-depth
   target-load covariance and, separately, the laminar SCD resource
   selection.  Neither follows from owner density or crossing-axis density.

Consequently this note proves a new owner-dense full-cross carrier and an
exact positive SCD sector, but not one full cyclic SCD and not constant one.

## 1. Audit of the complete internal-quartet Hall cut

Fix an old partition of \([2m]\) into \(c=m/2\) quartets.  For a set
\(S\), let

\[
                         F(S)=\#\{C:C\subseteq S\}.   \tag{1.1}
\]

### Lemma 1.1 (full-quartet conservation)

If \(T\) is the lower intersection of a return-free window all of whose
physical axes lie inside old quartets, and \(X\) is any owner in that
window, then

\[
                         F(T)=F(X).                   \tag{1.2}
\]

#### Proof

Every transition inside a quartet preserves its local cardinality.  A full
quartet has no internal Johnson move, hence is inactive and remains full
throughout the window.  A nonfull quartet has local cardinality at most
three in every owner, so its intersection cannot be full.  Thus precisely
the same inactive quartets are full in \(X\) and \(T\). \(\square\)

This proof allows every one-factor of \(J(4,1),J(4,2),J(4,3)\), arbitrary
active quartets, and arbitrary return-free orders.  It is not restricted to
the old three-edge mosaic.

Put

\[
 h(z)=(1+z)^4-z^4=1+4z+6z^2+4z^3.                  \tag{1.3}
\]

The exact target and source profile counts are

\[
\begin{aligned}
 T_{q,k}&=\binom ck[z^{m-q-4k}]h(z)^{c-k},\\
 X_k&=\binom ck[z^{m-4k}]h(z)^{c-k}.                \tag{1.4}
\end{aligned}
\]

Let \(J\) have law

\[
 \Pr(J=j)={\binom4j\over15},\qquad 0\le j\le3.      \tag{1.5}
\]

Direct calculation gives

\[
 \mu={28\over15},\qquad \sigma^2={176\over225}.     \tag{1.6}
\]

Take

\[
 q=A\sqrt m+O(1),\qquad k={m\over32}+y\sqrt m+O(1). \tag{1.7}
\]

With \(d=c-k\),

\[
 \sigma^2d={11m\over30}+O(\sqrt m),                 \tag{1.8}
\]

and the target and source deviations from \(\mu d\) are

\[
 \left(-A-{32y\over15}\right)\sqrt m+O(1),\qquad
 -{32y\over15}\sqrt m+O(1).                         \tag{1.9}
\]

The span-one local central limit theorem therefore gives

\[
 \log {X_k\over T_{q,k}}
 ={15A^2+64Ay\over11}+o(1).                          \tag{1.10}
\]

At \(y=-A/4\), this is \(-A^2/11+o(1)\).  If

\[
 |y+A/4|\le A/128,                                   \tag{1.11}
\]

then (1.10) is at most \(-A^2/22+o(1)\), uniformly.

For completeness, under uniform rank \(m-q\), the number of full quartets
has mean

\[
 {m\over32}-{A\over8}\sqrt m+O(1)                   \tag{1.12}
\]

and conditional variance

\[
 {11\over512}m+o(m).                                 \tag{1.13}
\]

Indeed, at density one half a quartet has
\(\operatorname{Var}(\mathbf1_{K=4})=15/256\),
\(\operatorname{Cov}(\mathbf1_{K=4},K)=1/8\), and
\(\operatorname{Var}(K)=1\); conditioning on total rank subtracts
\((1/8)^2\).  The \(O(m^{-1/2})\) density displacement changes only the
\(o(m)\) term.  Thus (1.11) is a fixed nonzero normal window, and it has
target mass \((c_A+o(1))N_q\) for a constant \(c_A>0\).

Since different \(k\)'s have disjoint source families, Lemma 1.1 and
(1.10) give at least

\[
 (c_A-o(1))(1-e^{-A^2/22})N_q                       \tag{1.14}
\]

lower holes for an all-internal factor.  Finally,

\[
 {N_q\over W}\longrightarrow e^{-A^2},              \tag{1.15}
\]

so (1.14) is \((\delta_A-o(1))W\), for example with any

\[
 0<\delta_A<c_A(1-e^{-A^2/22})e^{-A^2}.              \tag{1.16}
\]

Complementation replaces full lower quartets by empty upper quartets and
proves the upper cut.  This is the only wording correction needed in the
source theorem: the upper conserved statistic is the empty-quartet count,
not literally (1.1).

### Corollary 1.2 (crossing-axis toll)

Every successful lower factor has \(\Omega_A(W)\) depth-\(q\) roots whose
window contains an axis meeting two old quartets.

Indeed, in each profile \(k\), internal roots draw from the disjoint source
family \(X_k\), so at most \(|X_k|\) targets of that profile can be covered
internally.  The excess counted in (1.14) must therefore be covered by
crossing windows, one target per rooted window.

If a \(Q_r\) packet has \(s(P)\) such axes and is factored into isometric
\(C_{2r}\)'s, one axis occurs at two antipodal phases and lies in exactly
\(2q\) of the \(2r\) rooted \(q\)-windows on each cycle.  Hence at most

\[
                         {s(P)q\over r}|P|            \tag{1.17}
\]

packet roots see a crossing axis.  Summing (1.17) proves (0.5).  The union
bound remains valid when its right side exceeds \(|P|\).

## 2. What the two-sign \(13/32\) shores do and do not supply

On the two-quartet sectors \(k=2,3\), denote the large internal, cross,
and small internal shores by \(B,C,S\).  Relative to \(B\), their profile
effects have the exact schematic form

\[
 \begin{array}{c|c|c}
       &\text{lower profile changed}&\text{upper profile changed}\\ \hline
 B&0&0\\
 C&0&1\\
 S&1&1.
 \end{array}                                           \tag{2.1}
\]

The intersection sectors \(k=2,3\) have local owner mass

\[
 2\left(\binom42\binom41+\binom43\binom42\right)=96, \tag{2.2}
\]

or \(3/8\) of all eight-coordinate states.  The \(k=1\) upper-only and
\(k=4\) lower-only end sectors have mass eight each, or \(1/32\) each.
Consequently the two separate \(13/32\) statements are correct, but on
most of their support they are not independent decisions: one owner packet
must choose one of the three states in (2.1).

There is also an exact all-depth coupling.  Place the distinguished local
axis at one abstract phase of an isometric \(C_{2r}\), and let
\(I_q(t)\) indicate that the rooted \(q\)-window at phase \(t\) contains
it.  For \(q\le r\),

\[
 \sum_t I_q(t)=2q,\qquad I_q(t)\le I_{q+1}(t),        \tag{2.3}
\]

and

\[
 I_{q+1}(t)-I_q(t)
 =\mathbf1\{\text{the direction at phase }t+q
              \text{ is the distinguished axis}\}. \tag{2.4}
\]

Thus one shore choice has one nested response vector through every depth;
it does not provide a fresh signing at each \(q\).  A bounded number of
one-axis rounds changes only \(O(qW/r)=o(W)\) occurrences at a Gaussian
depth \(q\le H=o(r)\), even after both \(13/32\) constants are retained.
This is incompatible with Corollary 1.2.  The local theorem is a valid
router, but `HCRT` needs \(\Omega(r/q)\) such axes per typical packet and
one common choice satisfying the floor-energy derivative at all depths.

## 3. Exact cross-half parity matching

Let \(A,B\) be disjoint \(d\)-sets.  On
\(\binom{A\cup B}{k}\), join two vertices when one is obtained from the
other by deleting an occupied coordinate in one half and inserting an
unoccupied coordinate in the other.  This graph is bipartite by the parity
of \(|X\cap A|\).

### Theorem 3.1 (smaller-shore saturation)

For every \(d\) and \(0\le k\le2d\), the cross-exchange graph has a
matching saturating its smaller parity shore.  For odd \(k\) it is perfect.
For \(k=2j\), it leaves exactly

\[
                         \binom dj                   \tag{3.1}
\]

vertices, all on the parity shore \(|X\cap A|\equiv j\pmod2\).

#### Proof

The signed shore imbalance is

\[
 \sum_a(-1)^a\binom da\binom d{k-a}
 =[z^k](1-z)^d(1+z)^d=[z^k](1-z^2)^d.               \tag{3.2}
\]

It is zero for odd \(k\), and equals
\((-1)^j\binom dj\) for \(k=2j\).

Fix a bijection \(\pi:A\to B\) and order its pairs.  In a subset \(X\),
call a pair empty, full, or split according as it contains zero, two, or
one selected endpoint.  If a split pair exists, toggle both endpoints of
the first split pair.  This swaps its occupied endpoint across the halves,
is a legal cross-exchange edge, reverses \(|X\cap A|\)-parity, and leaves
the first split pair first.  It is therefore a fixed-point-free involution.

The unmatched states have no split pair.  They exist only at rank
\(k=2j\), are unions of \(j\) full pairs, number \(\binom dj\), and have
\(|X\cap A|=j\).  They are exactly the forced majority-shore excess in
(3.2). \(\square\)

Summing over all ranks, the unmatched local states are the \(2^d\) unions
of fixed pairs.  Thus a uniformly random local subset is eligible with
probability

\[
                         1-2^{-d}.                   \tag{3.3}
\]

The theorem remains true if a different bijection and pair order is used
at every local rank, because the ranks are disjoint and an exchange
preserves local rank.

## 4. A rank-dependent logarithmic-block near-tiling with every axis cross-quartet

The old quartet partition can be respected literally.  Fix a constant
\(C>1/2\), and choose a multiple of four

\[
                         d=C\log_2m+O(1).             \tag{4.0}
\]

Apart from fewer than \(2d\)
residual coordinates, group the old quartets into macroblocks

\[
 D_i=A_i\dot\cup B_i,\qquad |A_i|=|B_i|=d,           \tag{4.1}
\]

with each half a union of whole old quartets.  Therefore every
\(A_i\)-to-\(B_i\) exchange meets two different old quartets.

For each local rank \(k\), choose a bijection

\[
                         \pi_{i,k}:A_i\to B_i         \tag{4.2}
\]

and apply Theorem 3.1.  The resulting local edges and unmatched singletons
partition every local rank.  Tensor these partitions over the

\[
                         c=\lfloor m/d\rfloor         \tag{4.3}
\]

macroblocks and freeze the residual coordinates.  A product cell with
\(e\) matched local factors is a physical \(Q_e\).  If \(e\ge r\), take
the first \(r\) active blocks and partition \(Q_e\) into parallel
\(Q_r\)'s by freezing its other axes.  Local rank, eligibility, and the
first-\(r\) list are constant on each cell, so the packets are exactly
owner-disjoint.

Choose \(r\) to be a power of two satisfying

\[
                         c/4<r\le c/2.               \tag{4.4}
\]

Such a choice exists for all sufficiently large \(c\).  An exact
isometric \(C_{2r}\)-factor may then be installed in every packet.

### Theorem 4.1 (owner-dense full-cross packet tiling)

The retained packets partition all but

\[
                         L\le(2m+1)e^{-c/8}W          \tag{4.5}
\]

middle owners.  Every active axis crosses two old quartets, and every
nonzero protected window in every installed row contains only such axes.

#### Proof

Before conditioning on total rank, different macroblocks are independent,
and (3.3) shows that their eligibility indicators have mean at least
\(3/4\) for \(d\ge2\).  Hoeffding's inequality gives

\[
 \Pr\{e<c/2\}\le e^{-c/8}.                           \tag{4.6}
\]

The central-rank event has probability at least \(1/(2m+1)\), since the
largest of the \(2m+1\) binomial coefficients is central.  Conditioning
therefore gives (4.5).  The remaining assertions follow from the exact
product partition and the construction of the halves. \(\square\)

For \(d=\Theta(\log m)\), (4.5) is
\(\exp(-\Theta(m/\log m))W=o(W/H)\) for every polynomial \(H\), while

\[
                         r=\Theta(m/\log m).          \tag{4.7}
\]

Thus any \(H=\sqrt m\,\omega(m)=o(m/\log m)\) lies in the sparse-depth
range \(H=o(r)\).

For each packet row \(P\), define its private trace flags by the literal
successive swaps.  Every interval of at most \(r\) transitions is
geodesic, so

\[
                         G_t(X)=P^tX,qquad
                         G_1(G_tX)=G_{t+1}X           \tag{4.8}
\]

through the geodesic half.  Equation (4.8) is an exact rotor power law.  It
is not yet an SCD power law, because no laminar choice of these private
flags has been shown to use every Boolean rank resource once.

### 4.1 Eliminating a hidden fixed matching

Label each half by \(\mathbb Z/d\mathbb Z\).  There are exactly \(d\) odd
local ranks in \(\{1,\ldots,2d-1\}\).  Assign the \(d\) cyclic-shift
bijections

\[
                         a_x\mapsto b_{x+s}           \tag{4.9}
\]

bijectionally to those odd ranks; use arbitrary bijections at even ranks.
At an odd rank, every prescribed pair occurs as the sole split pair of an
appropriate local state, so every edge of \(K_{d,d}\) is actually used by
some local matching.  Hence the *local library* edge union in a macroblock
is the connected graph \(K_{d,d}\), not one perfect matching.

This corrects a harmless parity restriction in the simplest cyclic formula:
one does not need \(d\) odd.  Taking \(d\) divisible by four lets the two
halves be unions of old quartets while retaining the full shift library.

The local statement also literalizes on retained middle packets.

### Lemma 4.2 (middle extension of every library edge)

For all sufficiently large \(c\), every edge of every odd-rank matching
in (4.9) occurs as an active axis of some retained middle-layer packet.

#### Proof

Fix a desired edge at local odd rank \(k\) in block \(i\).  Choose its
local state so that this is its sole split pair, using
\((k-1)/2\) full pairs.  In a second block choose local rank \(2d-k\),
which is also odd and hence automatically eligible.  Give every other
macroblock local rank \(d\).  At rank \(d\) there are both eligible states
and ineligible no-split states, because \(d\) is even.  The two exceptional
ranks sum to \(2d\), so the macroblock ranks sum to \(cd\); choose exactly
half of the residual coordinates to obtain global rank \(m\).

Now prescribe eligibility at the rank-\(d\) filler blocks so that the
desired block is among the first \(r\) eligible blocks.  If \(i\ge r\),
put exactly \(r-1\) eligible fillers before it; if \(i<r\), use the
available fillers after it to bring the total to \(r\).  The one forced
eligible compensating block can be placed on whichever side is needed.
Since \(r\le c/2\), there are enough fillers for all sufficiently large
\(c\).  The resulting middle owner belongs to a retained packet and has
the desired active axis. \(\square\)

## 5. Capacity audit of the logarithmic-block construction

### 5.1 A fixed local bijection fails linearly

If \(\pi_{i,k}\) is independent of \(k\), all axes lie in one global
perfect matching \(M\).  Let \(F_M(S)\) be the number of full \(M\)-pairs
in \(S\).  Every lower trace preserves \(F_M\).

The exact number of middle sources and lower targets with \(f\) full pairs
is

\[
\begin{aligned}
 V_f&={m!\over f!^2(m-2f)!}\,2^{m-2f},\\
 T_{f,q}&={m!\over f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.  \tag{5.1}
\end{aligned}
\]

Thus

\[
 {V_f\over T_{f,q}}
 =2^q{(f+q)!\over f!}{(m-2f-q)!\over(m-2f)!}.        \tag{5.2}
\]

For

\[
 q=A\sqrt m+O(1),\qquad
 f={m\over4}+y\sqrt m+O(1),                          \tag{5.3}
\]

expanding the product in (5.2) gives

\[
 \log {V_f\over T_{f,q}}=3A^2+8Ay+o(1).             \tag{5.4}
\]

The target full-pair count has mean
\(m/4-A\sqrt m/2+O(1)\) and variance \(m/16+o(m)\).
At \(y=-A/2\), the ratio in (5.4) is \(e^{-A^2+o(1)}\).
A fixed \(\sqrt m\)-window around this value has positive target mass and
ratio uniformly below one.  Hence a fixed-bijection version of Theorem 4.1
has a linear Gaussian Hall deficit.  Crossing the old quartets is not by
itself sufficient.

### 5.2 Rank dependence removes that invariant

With the schedule (4.9), no single perfect matching contains all used
axes.  Toggling preserves the local rank, so the rank-dependent frame is
stable throughout each packet.  The fixed-\(M\) statistic in Section 5.1
is therefore unavailable.

Every active edge nevertheless stays inside one macroblock.  Hence the
number of full macroblocks is conserved below, and the number of empty
macroblocks is conserved above.  These are frame-independent invariants of
the displayed macro architecture, but they need not be the only remaining
status or chronology invariants.

A macroblock has size \(2d\).  At exact middle rank the expected number of
full macroblocks is

\[
 \lambda_X=c{(m)_{\underline{2d}}\over(2m)_{\underline{2d}}}
 ={m\over d}2^{-2d}\bigl(1+O(d^2/m)\bigr).           \tag{5.5}
\]

At rank \(m-A\sqrt m\), the exact expectation is

\[
 \lambda_T=c{(m-A\sqrt m+O(1))_{\underline{2d}}
                  \over(2m)_{\underline{2d}}}
 =\lambda_X
   \exp\!\left(-{2Ad\over\sqrt m}+o(d/\sqrt m)\right).          \tag{5.6}
\]

For the choice (4.0),

\[
 \lambda_X=O\!\left({m^{1-2C}\over\log m}\right)=o(1),
 \qquad \lambda_T\le(1+o(1))\lambda_X=o(1).          \tag{5.7}
\]

Markov's inequality now shows that both the middle source and lower target
have zero full macroblocks with probability \(1-o(1)\).  The complementary
argument gives zero empty macroblocks at the upper side with probability
\(1-o(1)\).  Thus these particular conserved statistics cannot isolate a
positive-mass Gaussian Hall deficit.  This conclusion deliberately uses
\(C>1/2\); it avoids inferring distributional contiguity merely from a
small standardized mean shift.  It does not rule out a different
rank-dependent status or chronology cut.

### 5.3 The exact remaining priority kernel

The first-split construction has a useful exact shadow formula.  Fix the
ordered pairs used at source local rank \(k\).  For a \((k-1)\)-set \(T\),
let \(\sigma(T)\) be the first split-pair index, with \(d+1\) if no pair
is split, and put

\[
 a_k^-(T)=\#\{j<\sigma(T):\text{pair }j\text{ is empty in }T\}. \tag{5.8}
\]

For a \((k+1)\)-set \(U\), define

\[
 a_k^+(U)=\#\{j<\sigma(U):\text{pair }j\text{ is full in }U\}. \tag{5.9}
\]

### Lemma 5.1 (local shadow multiplicities)

The number of selected local matching edges of source rank \(k\) whose
intersection is \(T\) equals \(a_k^-(T)\).  The number whose union is
\(U\) equals \(a_k^+(U)\).

#### Proof

An edge with intersection \(T\) must toggle an empty pair \(j\), giving
endpoints \(T+a_j\) and \(T+b_j\).  It is selected by the first-split rule
exactly when no earlier pair is split in \(T\), namely when
\(j<\sigma(T)\).  This proves (5.8).  The union proof is dual: delete one
or the other endpoint of a full pair \(j\), and require that no earlier
pair be split. \(\square\)

For an unconditioned random local subset, the number of nonsplit pairs
before the first split is geometric with success probability \(1/2\), and
its empty/full types are fair.  In particular a block has
\(a_k^->0\) with limiting probability \(1/3\), and the same holds above.
Since the number of macroblocks is \(\Theta(m/\log m)\gg q\), this local
support statistic does not itself create Gaussian-scale holes.  Its full
product distribution, coupled to the first-\(r\) packet rule and the common
compiler phases, is the exact unresolved target-capacity kernel.

There is an exact potential-coverage consequence.  It concerns the union
of legal packet options, not one owner-disjoint choice.

### Proposition 5.2 (the full rank-dependent catalogue has negligible immutable holes)

Let \(c=\lfloor m/d\rfloor\), let \(r\le c/2\), and suppose

\[
                         H=o(c),\qquad H^2/m=o(c).     \tag{5.10}
\]

Allow, for each product cell, every \(r\)-subset of its eligible axes and
every cube-affine conjugate of one exact compiler.  Uniformly for
\(q\le H\), all but \(e^{-\Omega(c)}N_q\) lower targets and the same number
of upper targets occur in at least one legal packet option.

#### Proof

For a uniformly random unconditioned local subset, fix temporarily one
pair order.  The event \(a_k^->0\) says that an empty pair occurs before
the first split pair.  Summing over the possible first such empty pair
gives

\[
 p_d^-={1\over3}(1-4^{-d}).                           \tag{5.11}
\]

The same calculation with full in place of empty gives
\(p_d^+=p_d^-\).  Although the pair order in the construction depends on
local rank, every two choices are conjugate under a permutation of the
\(2d\) local coordinates.  Hence the number of good subsets at each fixed
rank, and therefore the unconditioned probability (5.11), is unchanged.

Different macroblocks are independent before global rank conditioning.
Chernoff's inequality therefore says that, with failure
\(e^{-\Omega(c)}\), a target has at least \(c/4\) lower-good blocks and at
least \(c/4\) upper-good blocks.  Independently, its number of locally
eligible blocks is at least \(3c/4\) with the same error, by (3.3).
Conditioning on rank \(m\pm q\) costs
\(\exp(O(q^2/m+\log m))=e^{o(c)}\) under (5.10), so the conditional error
remains \(e^{-\Omega(c)}\).

For a good lower target \(T\), choose \(q\) lower-good macroblocks.  In
each, Lemma 5.1 supplies a selected local edge of source rank one larger
whose intersection is the prescribed local target; choose either endpoint
as the source state.  Leave every other block unchanged.  The resulting
global source has rank \(m\), and at least \(3c/4-q+q\ge r\) eligible
blocks.  Extend the chosen \(q\) axes to any eligible \(r\)-set.  A cube
translation, coordinate permutation, and phase shift put those \(q\)
axes first in one compiler row, so its literal intersection is \(T\).
The union proof is dual using \(a_k^+\). \(\square\)

Proposition 5.2 is only a support theorem.  Different targets generally
use overlapping owner packets and different compiler conjugates.  It gives
neither an integral owner resolution nor the negative target covariance
needed for floor balance.

## 6. Relation to the actual SCD promotion problem

The owner-dense construction in Section 4 and the actual-SCD construction
in (0.1)--(0.2) solve different halves of the problem.

For four child chains of radii \(a,b,c,d\), the two first-scale rectangle
decompositions have common carrier radii

\[
 R_-\le R\le R_+,qquad
 R_-=\max(|a-b|,|c-d|),\quad
 R_+=\min(a+b,c+d).                                  \tag{6.1}
\]

If \(A_R=(A_0<\cdots<A_{2R})\) and
\(B_R=(B_0<\cdots<B_{2R})\), the second-scale square chains have centers

\[
                         z_{R,j}=A_{2R-j}\cup B_j.   \tag{6.2}
\]

Their lower and upper tails give

\[
 G_t(z_{R,j})=A_{2R-j-t}\cup B_{j+t}=z_{R,j+t},      \tag{6.3}
\]

which independently verifies (0.1).  Every successor in (6.3) deletes a
fresh coordinate from the first carrier and inserts a fresh coordinate
from the second, so all its protected windows are densely cross-carrier.
The exact Boolean aggregation is (0.2), and the induced component count is
\(\Theta(\binom{8s}{4s}/s)\).  Abstract endpoint closure is not a literal
Johnson seam.

The vanishing \(s^{-1/2}\) density is a corner-equality limitation: the
middle of a rectangle product of carrier radii \(R,S\) is a turn only when
\(R=S\).  Any fixed finite pairing library therefore remains
\(O(\binom{8s}{4s}/\sqrt s)\).  Section 4 supplies a growing,
height-dependent cross-frame library on almost all owners, but does not
prove that its private trace diamonds can be selected as one full SCD.

There are two further exact warnings.

* Once an owner successor \(P=G_1\) is fixed, power consistency forces
  \(G_q=P^q\) and fixes every literal trace target.  Reframing the same
  \(P\) is gauge and cannot improve target multiplicities.
* In the serial-central quartet grammar, the successor frame pairs the
  staggered flag carriers.  Through depth \(H\), the aggregate number of
  new quartet blocks is at least

  \[
     \sum_{j=1}^{\lfloor H/2\rfloor}\binom{2m}{m-(2j+1)}.       \tag{6.4}
  \]

  Thus a bounded-local frame update covers only \(o(W)\) owners.  The
  logarithmic-block construction is appropriately dense, but (6.4) is not
  itself an SCD existence theorem.

## 7. Exact remaining gate

The following statements are now proved.

1. A literal full product SCD contains a power-consistent, off-centre,
   densely cross-carrier sector of size
   \(\Theta(\binom{8s}{4s}/\sqrt s)\).
2. The complete old-quartet-internal atlas has a linear Gaussian Hall
   deficit, with audited exponent \(-A^2/11\).
3. Successful packets need the weighted crossing-axis supply (0.5).
4. Rank-dependent logarithmic cross-half matchings give an exact
   owner-near-tiling in which every packet has \(s(P)=r\), so owner and
   crossing-axis supply are no longer obstructions.
5. A fixed cross matching still fails linearly; a rank-dependent shift
   library removes that fixed-pair invariant, and the remaining
   full/empty-macroblock invariant is asymptotically weak.

What is not proved is precisely the conjunction below.

* Choose the rank-dependent local matchings and one common packet compiler
  so that, for every signed depth \(q\le H\), the literal target loads have
  aggregate floor energy \(o(W)\).  Explicitly, put

  \[
     {W\over N_q}=c_q+\theta_q,qquad
     Q_q^\epsilon=\sum_T
        (Z_{q,T}^\epsilon-c_q)(Z_{q,T}^\epsilon-c_q-1).          \tag{7.2}
  \]

  A trade with target-load change \(\delta\) has the exact derivative

  \[
     \Delta Q_q^\epsilon
      =2\sum_T(Z_{q,T}^\epsilon-c_q-\tfrac12)\delta_T
        +\sum_T\delta_T^2.                            \tag{7.3}
  \]

  Thus owner density and the separate \(13/32\) sign supplies say nothing
  about the sign of the decisive first term.  In the diffuse symmetric
  packet formulation, if
  \(K_q(P,P')\) is the number of common depth-\(q\) targets and \(I_P\)
  is the packet indicator, the pointwise covariance target is

  \[
   \sum_{P\ne P'}K_q(P,P')\operatorname{Cov}(I_P,I_{P'})
    =-N_q(c_q+\theta_q^2)+o(W/H).                     \tag{7.4}
  \]

  The aggregate version sums the corresponding residual over both signs
  and all \(q\le H\) and asks for \(o(W)\).  A single owner-disjoint law
  must realize these equations at every depth; independent shore choices
  have zero off-diagonal covariance and fail.
* From the resulting owner rotor, choose nested active roots with the exact
  SCD census

  \[
      |\mathcal A_q|=\binom{2m}{m-q}                 \tag{7.5}
  \]

  so that both trace maps are the lower and upper rank bijections of one
  laminar full SCD and the shift identities hold on every retained root.
* Close the remaining induced paths by literal Johnson/OR seams; the
  abstract component counts alone do not provide those seams.

Thus the lane has advanced from a bounded one-axis router to an explicit
owner-dense all-cross hierarchy.  The surviving obstruction is not a
crossing-axis count.  It is the common all-depth target covariance together
with the laminar SCD selection for the same integral rotor.
