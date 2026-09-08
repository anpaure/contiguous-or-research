# Dense cross-exchange packets: exact parity Hall, owner cubes, and the next profile cut

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

The proposed cross-exchange matching exists with the best possible Hall
deficiency, and it tensorizes into a near-spanning family of large
owner-disjoint physical cubes.

Let `A={a_1,\ldots,a_d}` and `B={b_1,\ldots,b_d}`. On the rank-`k`
subsets of `A\dot\cup B`, join two sets when one is obtained from the other
by deleting one selected coordinate in one half and inserting one
unselected coordinate in the other half. Bipartition this graph by the
parity of `|X\cap A|`. Then

\[
 |E_{d,k}|-|O_{d,k}|
 =\begin{cases}
 0,&k\text{ odd},\\
 (-1)^s\binom ds,&k=2s.
 \end{cases}                                        \tag{0.1}
\]

There is an explicit matching which leaves exactly the unavoidable
vertices in (0.1) and saturates the smaller parity shore. Pair
`a_i\leftrightarrow b_i`, find the first column split by `X`, and exchange
its selected endpoint. The only unmatched sets have every column empty or
full.

Now partition the ambient coordinates into `b=m/d` disjoint `2d`-blocks
and apply this local matching in every local rank. Products of its edges
and singleton remainders partition the whole middle layer into cubes of
variable dimension `S`. For an allowed

\[
 r=4\cdot2^j\le b/2,
 \tag{0.2}
\]

subdivide every `Q_S`, `S\ge r`, into `Q_r`'s, taking all assignments of
the discarded axes. If `S<r`, leave it aside.
For `d\ge4`, the leave is

\[
                         e^{-\Omega(m)}W,
 \qquad W=\binom{2m}{m}.                            \tag{0.3}
\]

Taking `d=C\log m` gives

\[
 r=\Theta(m/\log m),\qquad |Q_r|=2^r=e^{o(m)},       \tag{0.4}
\]

and the usual depth-`H` cutting toll is `O(HW/r)=o(W)` whenever
`H\log m=o(m)`. If each half `A,B` is a union of fixed quartets, every
active axis crosses that quartet partition. Thus the construction meets,
with enormous slack, the **raw geometric** crossing-axis occurrence toll
forced by the audited complete-internal-atlas theorem. It does not yet
make those axes instances of the sign-specific three-shore profile trade.

This does **not** yet prove target Hall.

For the explicit first-split matching, all active axes belong to the one
fixed perfect matching

\[
                         P=\{a_i b_i:1\le i\le d}
 \tag{0.5}
\]

in every macroblock. Every product cube is a status cell of the resulting
global matching. Hence lower windows preserve the number of full `P`-pairs
and upper windows preserve the number of empty `P`-pairs. At
`q=A\sqrt m`, either sign has the old exact deficit

\[
 {M_q^\pm\over W}
 \ge
 e^{-A^2}\Phi(A/2)-\Phi(-3A/2)-o(1)>0.              \tag{0.6}
\]

Here and below `\Phi` is the standard normal distribution function.

So the simplest Hall-saturating matching is closed by the fixed-pair cut,
despite the fact that every one of its axes crosses the old quartet
partition.

An arbitrary saturating matching of the cross-exchange graph need not lie
in one fixed coordinate-pair frame, so (0.6) is not a universal no-go for
the proposal. The first surviving capacity gate is then critical rather
than deficient. If `\mathcal M_{d,k}` is such a matching and

\[
 \ell_{d,k}(R)=
 \#\{e\in\mathcal M_{d,k}:\bigcap e=R\},
 \qquad |R|=k-1,                                    \tag{0.7}
\]

with the analogous upper multiplicity `u_{d,k}`, then

\[
 \sum_R\ell_{d,k}(R)=\sum_Uu_{d,k}(U)
 ={1\over2}\left(\binom{2d}k-
 \mathbf 1_{2\mid k}\binom d{k/2}\right).          \tag{0.8}
\]

For central `k=d+O(\sqrt d)`, the mean owner-start loads

\[
 {2\sum_R\ell_{d,k}(R)\over\binom{2d}{k-1}},
 \qquad
 {2\sum_Uu_{d,k}(U)\over\binom{2d}{k+1}}            \tag{0.9}
\]

are both `1+O(d^{-1/2})`, with an exponentially small correction from the
parity imbalance. Away from `k=d+O(1)`, one has a systematic positive
`\Theta(d^{-1/2})` drift and the other a negative drift. Thus there is no
constant local slack. More sharply, one matching supports at most
`|\mathcal M_{d,k}|` distinct lower shadows and the same number of upper
shadows. At central rank it therefore misses asymptotically one half of
each local shadow layer, even in the ideal collision-free case. These
depth-one multiplicities and support cuts are a necessary first capacity
test; they are not the full multidepth HCRT columns. Parity Hall alone
supplies none of the required multi-tag common-column control.

The newly supplied two-sign cross-quartet profile theorem is valid and
fits this boundary exactly. It transports upper profiles on
`13/32+o(1)` owner density against the large-layer shore and lower profiles
on the same density against the small-layer shore. But those are two
different comparisons, and one crossing axis is visible in only a `q/r`
fraction of a `Q_r` packet's depth-`q` starts. The dense packet above
solves only the raw geometric crossing-axis count; it does not prove that
those axes are eligible for the three-shore trade, choose the two shore
comparisons with one common chronology, or control the full ordered flags
extending (0.7)--(0.9).

Finally, centring only the first-order crossed quartet counts is not
enough. There is a near-spanning exact complementary-core packetization
which centres the two statistics `K_R,K_C`, but its one-hot middle
profiles preserve

\[
                         J=K_RK_C                 \tag{0.10}
\]

on every lower trace, while uniform rank-`m-q` targets require a
`q/4+O_A(1)` shift in `J`. This gives another linear Hall cut. A successful
dense hierarchy must therefore vary pair frames and transport joint
profiles, not merely match parity shores or first moments.

The precise remaining theorem must be stated on full columns, not just on
the depth-one arrays. It is a rank-, selector-, tag-, and chronology-
dependent catalogue of cross-exchange matchings whose complete labelled
lower/upper flags admit one common integral choice with `o(W)` aggregate
floor defect, while satisfying the common-run, cone, cycle-congruence,
SCD, and literal-seam constraints. That is the current dense
HCRT/floor-covariance gate.

## 1. Independent audit of the complete internal-quartet Hall cut

Assume first that `m` is even, partition `[2m]` into `c=m/2` fixed
quartets, and let

\[
                         F(S)=\#\{Q:Q\subseteq S\}.  \tag{1.1}
\]

If every physical axis of a return-free window is internal to one
quartet, then

\[
                         F(T)=F(X)                  \tag{1.2}
\]

for its middle owner `X` and lower intersection `T`. Indeed an active
quartet has middle rank `1,2`, or `3`, and its lower intersection is not
full; an inactive quartet is unchanged. This argument permits every
one-factor of `J(4,1)`, `J(4,2)`, and `J(4,3)`, arbitrary active blocks,
and arbitrary internal axis orders.

The exact profile counts are

\[
\begin{aligned}
 |\mathcal T_{q,k}|
 &=\binom ck[z^{m-q-4k}]h(z)^{c-k},\\
 |\mathcal X_k|
 &=\binom ck[z^{m-4k}]h(z)^{c-k},\\
 h(z)&=1+4z+6z^2+4z^3.
\end{aligned}                                        \tag{1.3}
\]

Normalize the coefficients by the random variable

\[
 \Pr(J=j)={\binom4j\over15},\quad0\le j\le3,
 \qquad
 \mathbb EJ={28\over15},\quad
 \operatorname{Var}J={176\over225}.                 \tag{1.4}
\]

Put

\[
 q=A\sqrt m+O(1),qquad
 k={m\over32}+y\sqrt m+O(1).                         \tag{1.5}
\]

With `d_0=c-k`, the target and source coefficient indices satisfy

\[
\begin{aligned}
 s_T-\mathbb EJ\,d_0
 &=\left(-A-{32y\over15}\right)\sqrt m+O(1),\\
 s_X-\mathbb EJ\,d_0
 &=-{32y\over15}\sqrt m+O(1),\\
 \operatorname{Var}J\,d_0
 &={11m\over30}+O(\sqrt m).
\end{aligned}                                        \tag{1.6}
\]

The lattice local central limit theorem therefore gives

\[
 \log{|\mathcal X_k|\over|\mathcal T_{q,k}|}
 ={15A^2+64Ay\over11}+o(1).                         \tag{1.7}
\]

At `y=-A/4`, this is `-A^2/11+o(1)`. On the window

\[
 \left|y+{A\over4}\right|\le {A\over128},           \tag{1.8}
\]

it is at most `-A^2/22+o(1)` uniformly. The target distribution of `F`
has mean

\[
                         {m\over32}-{A\over8}\sqrt m+O(1)       \tag{1.9}
\]

and conditional variance `\Theta(m)`, so (1.8) carries a positive
`A`-dependent fraction of the target layer. Summing its typewise Hall
deficits proves a linear lower deficit. Complementation gives the upper
deficit.

The crossing-axis toll also checks. For `q\le r`, in an isometric
`C_{2r}` row an axis occurs twice, and each occurrence belongs to exactly
`q` cyclic depth-`q` starts. Thus one cross axis is visible in a `q/r`
fraction of all starts. For owner-disjoint `Q_r` packets, apart from a
negligible exceptional owner set, if packet `P` has `s(P)` cross axes,
successful Hall requires

\[
 {1\over W}\sum_Ps(P)|P|=\Omega_A(r/q).             \tag{1.10}
\]

This independently verifies the theorem
`MATH_THEOREM_FULL_INTERNAL_QUARTET_ATLAS_GAUSSIAN_HALL_CUT_20260726.md`
and fixes its scope: it rules out every completely internal atlas, but not
dense cross-axis packets.

For odd `m`, freeze one residual coordinate pair and condition on its
occupancy. The coefficient indices in (1.3) change by `O(1)` only; the
uniform local limit estimate, positive target window, and linear Hall cut
are unchanged. Thus the asymptotic no-go is not a parity-subsequence
artifact.

## 2. Exact Hall theorem for the cross-exchange graph

Fix a bijection `a_i\leftrightarrow b_i` only for the proof below. For a
`k`-set `X`, call column `i` split when exactly one of `a_i,b_i` belongs to
`X`.

### Theorem 2.1 (Hall-sharp parity matching)

The cross-exchange graph has a matching saturating its smaller parity
shore. More precisely, all vertices can be paired except that, when
`k=2s`, exactly `\binom ds` vertices remain unmatched, all on parity
shore `s\pmod2`.

#### Proof

If `X` has a split column, let `i(X)` be its least split index and put

\[
                         M(X)=X\triangle\{a_{i(X)},b_{i(X)}\}.  \tag{2.1}
\]

This is a legal cross exchange. It leaves the set of split columns
unchanged, so `i(M(X))=i(X)` and `M^2(X)=X`. It changes `|X\cap A|` by
one, hence pairs opposite parity shores.

An unmatched set has no split column. Every column is then empty or full.
Such a set exists only at even rank `k=2s`, and it is the union of exactly
`s` full columns. There are `\binom ds` such sets, and every one has
`|X\cap A|=s`. This proves the matching assertion.

Independently, the signed shore difference is

\[
\begin{aligned}
 |E_{d,k}|-|O_{d,k}|
 &=\sum_i(-1)^i\binom di\binom d{k-i}\\
 &=[z^k](1-z)^d(1+z)^d\\
 &=[z^k](1-z^2)^d.
\end{aligned}                                        \tag{2.2}
\]

Equation (2.2) is zero at odd `k` and equals
`(-1)^s\binom ds` at `k=2s`. Thus the unmatched vertices are exactly the
unavoidable cardinality excess, and the opposite shore is saturated.
`\square`

Summing the unavoidable excess over all local ranks gives

\[
                         \sum_{s=0}^d\binom ds=2^d.  \tag{2.3}
\]

Thus the union over all ranks partitions `4^d-2^d` local subsets into
physical cross-exchange edges and leaves `2^d` singleton subsets.

## 3. Near-spanning dense-cross-axis packetization

Assume first that `d\mid m` and split the `2m` coordinates into

\[
                         b={m\over d}               \tag{3.1}
\]

disjoint macroblocks `\Omega_j=A_j\dot\cup B_j`, each of size `2d`.
Choose one Hall-sharp matching independently in every local rank of every
macroblock. Include its unmatched vertices as singleton local cells.

Taking Cartesian products over the `b` macroblocks partitions the entire
middle layer. If `S` local factors are edges and `b-S` are singletons, the
product cell is a literal physical `Q_S`; every edge preserves its local
rank, so the whole cube remains in the middle layer.

Choose `r=4\cdot2^a` largest subject to `r\le b/2`. If `S\ge r`, choose
in advance which `r` axes to retain and take **all** `2^{S-r}` assignments
of the other axes. These `Q_r` subcubes partition `Q_S`. Leave only the
cells with `S<r`.

### Theorem 3.1 (dense cross-axis packets)

For `d\ge4`, the retained middle owner count obeys

\[
 W-G\le(2m+1)2^{-(1/2-1/d)m}W=e^{-\Omega(m)}W.       \tag{3.2}
\]

Every retained packet is a physical `Q_r`, every one of its axes crosses
one cut `A_j|B_j`, and

\[
                         {b\over4}<r\le {b\over2}.   \tag{3.3}
\]

#### Proof

Under independent fair-bit sampling, a macroblock is a singleton cell with
probability

\[
                         {2^d\over4^d}=2^{-d}.       \tag{3.4}
\]

The macroblocks are independent, so

\[
                         S\sim\operatorname{Bin}(b,1-2^{-d}).  \tag{3.5}
\]

Since `r\le b/2`, the event `S<r` requires at least `b/2` singleton
blocks. Hence

\[
 \Pr(S<r)
 \le2^b(2^{-d})^{b/2}
 =2^{-(d/2-1)b}=e^{-\Omega(m)}.                    \tag{3.6}
\]

Conditioning on total rank `m` costs at most `2m+1`, giving (3.2).
Product cells are owner-disjoint by construction, and taking every frozen
assignment partitions each `Q_S` exactly into `Q_r` subcubes. Every local
matching edge exchanges one `A_j` coordinate with one `B_j` coordinate,
so every retained cube axis is cross-block. Finally, consecutive allowed
values `4\cdot2^a` differ by a factor two, proving (3.3).
`\square`

For arbitrary `m`, round `d=C\log m` to a multiple of four, use
`b=\lfloor m/d\rfloor` complete macroblocks, and freeze the fewer than
`2d` residual coordinates separately in every cell. The same conditioning
argument gives (3.2) with `m` replaced by `bd=m-O(d)`, so every asymptotic
conclusion below holds without passing to a divisibility subsequence.

If

\[
                         d=C\log m                 \tag{3.7}
\]

with any fixed positive `C`, then

\[
 r=\Theta(m/\log m),qquad
 2^r=\exp(\Theta(m/\log m))=e^{o(m)}.                \tag{3.8}
\]

After installing the known isometric `C_{2r}` factor in each `Q_r`, the
retained factor has `G/(2r)` cycles. The standard common
depth-`H` collar charge is

\[
                         O(HG/r)=O(HW\log m/m).      \tag{3.9}
\]

It is `o(W)` whenever `H\log m=o(m)`, in particular throughout the usual
Gaussian regime `H=\sqrt m\,\omega(m)` with
`\omega(m)\log m=o(\sqrt m)`.

Because `d` was rounded to a multiple of four, partition each `A_j` and
`B_j` internally
into quartets. Every active axis then meets two distinct quartets. A packet
has `s(P)=r` crossing axes, so the left side of the occurrence requirement
is `r`, far above the necessary `\Omega_A(r/q)` for every `q\to\infty`.

After the `C_{2r}` factors are installed, the retained construction is
integral packetwise and directly gives literal isometric rows. It is not a
fractional owner assignment and uses no conflict-free matching assumption.
The exceptional owners may be covered by any literal baseline at cost
`O(m(W-G))=o(W)`. This proves raw cross-axis abundance, not
target-labelled Hall or a new global exact-factor splice.

## 4. The fixed-pair obstruction for the explicit matching

Return to the matching (2.1). Across all macroblocks, let

\[
 P=\bigcup_j\{\{a_{j,i},b_{j,i}\}:1\le i\le d\}.     \tag{4.1}
\]

In the all-`m` residual construction following Theorem 3.1, extend `P` by
an arbitrary perfect matching on the even residual coordinate set. Those
coordinates are frozen in every packet, so the invariant below is
unchanged and `P` is a perfect matching of all `2m` coordinates.

Every local edge varies the orientation of one split `P`-pair. All other
`P`-pair statuses and orientations are fixed in that edge. Consequently
every product `Q_r` lies in one status cell of the single global matching
`P`.

Let `f_P(S)` be the number of full `P`-pairs in `S`. If `T` is a lower
trace of an owner `X` in one of these cells, then

\[
                         f_P(T)=f_P(X).              \tag{4.2}
\]

Dually, upper traces preserve the number of empty `P`-pairs.

For type `f`, the exact middle-source and lower-target counts are

\[
\begin{aligned}
 V_f&={m!\over f!^2(m-2f)!}\,2^{m-2f},\\
 T_{f,q}&={m!\over f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.
\end{aligned}                                        \tag{4.3}
\]

Here `T_{f,q}=0` unless `0\le f\le\lfloor(m-q)/2\rfloor`.

Therefore every such factor has at least

\[
                         D_{m,q}=\sum_f(T_{f,q}-V_f)_+          \tag{4.4}
\]

lower holes. At `q=A\sqrt m+o(\sqrt m)`, the local central limit theorem
gives

\[
 {D_{m,q}\over W}
 \longrightarrow
 \delta_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.           \tag{4.5}
\]

Complementation gives the same upper obstruction. This proves (0.6).

The conclusion is deliberately scoped. The abstract graph has many
Hall-sharp matchings, and a matching can use different coordinate pairs in
different owner cells. Equations (4.1)--(4.5) close the explicit
first-split witness and every catalogue supported in one global pairing;
they do not close a rank- or tag-varying catalogue of cross matchings.

## 5. The critical lower/upper shadow ledger

Let `\mathcal M_{d,k}` be any matching saturating the smaller parity shore.
Its size is forced by (0.1):

\[
 |\mathcal M_{d,k}|
 ={1\over2}\left(\binom{2d}k-
 \mathbf 1_{2\mid k}\binom d{k/2}\right).          \tag{5.1}
\]

For every `(k-1)`-set `R` and `(k+1)`-set `U`, define the actual shadow
multiplicities

\[
\begin{aligned}
 \ell_{d,k}(R)
 &=\#\{\{X,Y\}\in\mathcal M_{d,k}:X\cap Y=R\},\\
 u_{d,k}(U)
 &=\#\{\{X,Y\}\in\mathcal M_{d,k}:X\cup Y=U\}.
\end{aligned}                                        \tag{5.2}
\]

Every matching edge contributes one lower and one upper shadow, so

\[
                         \sum_R\ell_{d,k}(R)
 =\sum_Uu_{d,k}(U)=|\mathcal M_{d,k}|.               \tag{5.3}
\]

Both endpoints of an edge are middle starts with the same depth-one lower
and upper shadows. Thus the mean start-loads on the two local target
layers are

\[
\begin{aligned}
 \bar\lambda^-_{d,k}
 &={2|\mathcal M_{d,k}|\over\binom{2d}{k-1}},\\
 \bar\lambda^+_{d,k}
 &={2|\mathcal M_{d,k}|\over\binom{2d}{k+1}}.
\end{aligned}                                        \tag{5.4}
\]

If `k=d+O(\sqrt d)`, Stirling's formula and (5.1) give

\[
 \varepsilon_{d,k}
 =\mathbf 1_{2\mid k}{\binom d{k/2}\over\binom{2d}k}
 =O(e^{-c d}),                                      \tag{5.5}
\]

uniformly in that band, for an absolute `c>0`, and

\[
\bar\lambda^-_{d,k}
 ={2d-k+1\over k}\,(1-\varepsilon_{d,k}),
 \qquad
 \bar\lambda^+_{d,k}
 ={k+1\over2d-k}\,(1-\varepsilon_{d,k}).            \tag{5.6}
\]

At `k=d+O(1)`, both are `1+O(1/d)`; across the natural
`O(\sqrt d)` band they are `1+O(d^{-1/2})`. More precisely, at
`k=d+c_0\sqrt d+O(1)`, the lower mean is
`1-2c_0d^{-1/2}+O(d^{-1})` and the upper mean is
`1+2c_0d^{-1/2}+O(d^{-1})`, up to (5.5). Thus a tensor catalogue must
compensate systematic rank drift as well as multiplicity concentration.

Equations (5.2)--(5.6) are only the first unavoidable, depth-one local
data. A chronology on an installed `C_{2r}` produces ordered nested flags
at all depths, together with selector, tag, and compiler-state labels.
Those complete target-labelled columns, not `\ell,u` alone, enter the
HCRT positive-part floor functional. Flat depth-one arrays are necessary
but neither equivalent nor sufficient.

There is also an exact support cut which does not use concentration. Since
`\ell,u` are nonnegative integers and have sums `|\mathcal M_{d,k}|`,

\[
\begin{aligned}
 \#\{R:\ell_{d,k}(R)=0\}
 &\ge\binom{2d}{k-1}-|\mathcal M_{d,k}|
  =\binom{2d}{k-1}\left(1-{\bar\lambda^-_{d,k}\over2}\right),\\
 \#\{U:u_{d,k}(U)=0\}
 &\ge\binom{2d}{k+1}-|\mathcal M_{d,k}|
  =\binom{2d}{k+1}\left(1-{\bar\lambda^+_{d,k}\over2}\right).
\end{aligned}                                       \tag{5.7}
\]

For `k=d+O(\sqrt d)`, both missing proportions are
`1/2+O(d^{-1/2})`. Equality in (5.7) means every used shadow has
multiplicity one, so its owner-start load is two and every unused shadow
has load zero. Thus no single matching/tag can approximate local load one;
several selector-compatible matchings must interlace their supports before
the all-depth floor problem even becomes meaningful.

The lower and upper atlases are also coupled by an exact type-shift
invariant. Put

\[
 L_i=\sum_{|R\cap A|=i}\ell_{d,k}(R),
 \qquad
 U_j=\sum_{|U\cap A|=j}u_{d,k}(U).                  \tag{5.8}
\]

Every cross edge with lower `A`-count `i` has upper `A`-count `i+1`, so

\[
                         L_i=U_{i+1}                \tag{5.9}
\]

for every `i`, for every matching, before any averaging. Yet the two type
capacities have ratio

\[
 {\binom d{i+1}\binom d{k-i}
  \over
  \binom di\binom d{k-1-i}}
 ={(d-i)(d-k+1+i)\over(i+1)(k-i)}.                 \tag{5.10}
\]

At `k=d` this ratio is exactly one, so (5.9) is not by itself a central
no-go. Off centre it is the exact transportation constraint behind the
opposite systematic drifts in (5.6). Consequently lower and upper shadow
supports cannot be designed or rounded independently, even at depth one.

## 6. Incorporating the two-sign cross-quartet profile trade

For disjoint four-sets `A,B`, put

\[
 V_k^+=\binom Ak\times\binom B{k-1},
 \qquad
 V_k^-=\binom A{k-1}\times\binom Bk.                 \tag{6.1}
\]

The cross graph between them is `k(5-k)`-regular and has a perfect
matching `\Xi_k`. Its edges have lower and upper block profiles

\[
                         (k-1,k-1),\qquad(k,k).       \tag{6.2}
\]

There are two exact internal comparison shores.

* The large-layer shore exists for `k=1,2,3`. It has the same lower
  profile as (6.2) and a different upper profile.
* The small-layer shore exists for `k=2,3,4`. It has the same upper
  profile as (6.2) and a different lower profile.

Their exact owner masses are, separately,

\[
 2\sum_{k=1}^3\binom4k\binom4{k-1}
 =2\sum_{k=2}^4\binom4k\binom4{k-1}
 =104,                                               \tag{6.3}
\]

or `13/32` of the local Boolean cube. Tensoring an edge with a disjoint
`Q_{r-1}` gives a whole `Q_r` owner trade with no seam.

This independently verifies
`MATH_THEOREM_TWO_SIGN_CROSS_QUARTET_PROFILE_TRANSPORT_20260726.md`.
Its correct implication is local and sign-separated. The cross shore must
be compared with the large shore to move upper profiles and with the small
shore to move lower profiles. A density statement does not select these
two comparisons simultaneously.

Furthermore, one elementary trade contributes one crossing axis, visible
in only a `q/r` fraction of packet starts. Section 3 supplies `r` **raw**
cross-half axes per packet, so it removes the purely geometric crossing
count obstruction. It does not prove that those axes occur at eligible
quartet ranks or carry the required cross/large/small common-owner shore
options. That usable-profile density, and a common integral choice
controlling every protected depth and its positive-part floors, remain
unproved.

## 7. A next joint-profile obstruction after first-order `K`

Let an eight-set be partitioned into four coordinate pairs
`P_{00},P_{01},P_{10},P_{11}`. Its row and column quartet partitions are

\[
\begin{aligned}
 \mathcal R&=\{P_{00}\cup P_{01},P_{10}\cup P_{11}\},\\
 \mathcal C&=\{P_{00}\cup P_{10},P_{01}\cup P_{11}\}.
\end{aligned}                                        \tag{7.1}
\]

For a subset `S` of this eight-set, define

\[
\begin{aligned}
 K_{\mathcal R}(S)
 &=\mathbf1_{|S\cap(P_{00}\cup P_{01})|=3}
   +\mathbf1_{|S\cap(P_{10}\cup P_{11})|=3},\\
 K_{\mathcal C}(S)
 &=\mathbf1_{|S\cap(P_{00}\cup P_{10})|=3}
   +\mathbf1_{|S\cap(P_{01}\cup P_{11})|=3}.
\end{aligned}                                        \tag{7.2}
\]

Choose a bijection `\pi:P_{10}\to P_{01}`. For `u\in P_{10}`, put
`v=\pi(u)` and

\[
                         F_u=\{u,v\}\cup P_{11}.     \tag{7.3}
\]

There are two physical `Q_2` cells for this `u`. The plus cell is the
complementary-core subcell of the interval

\[
 L_u^+=P_{00},\qquad U_u^+=P_{00}\cup F_u,           \tag{7.4}
\]

whose four middle owners are `P_{00}\cup\{a,s\}` for
`a\in\{u,v\}` and `s\in P_{11}`. The minus cell is its complement, with

\[
 L_u^-=\Omega\setminus U_u^+,
 \qquad U_u^-=\Omega\setminus P_{00}.                \tag{7.5}
\]

The two values of `u` and two signs give four pairwise owner-disjoint
`Q_2` cells. They partition sixteen hard middle owners. Every such owner
has local profile

\[
 (K_\mathcal R,K_\mathcal C)=(1,0)
 \quad\text{or}\quad(0,1).                         \tag{7.6}
\]

Both lower cores have profile `(0,0)`. A plus upper endpoint has profile
`(2,2)`, while a minus upper endpoint has `(0,0)`. Hence equal plus/minus
cell mass centres both first-order `K` coordinates on the lower and upper
sides of completed squares. Define the next profile

\[
                         J(S)=\sum_g
 K_{\mathcal R}^{(g)}(S)K_{\mathcal C}^{(g)}(S),     \tag{7.7}
\]

where `g` runs over disjoint eight-blocks.

### Lemma 7.1 (near-spanning hard-cell packetization)

Assume first that `4\mid m` and partition the coordinates into
`B=m/4` ordered eight-grids. Call a grid hard-eligible for an owner when
its restriction is one of the sixteen owners in the four `Q_2` cells
above. Let

\[
 t=2\cdot2^a\le B/32                                      \tag{7.8}
\]

be largest. Select the first `t` eligible grids, freeze every other grid,
and in each selected grid use the unique one of the four `Q_2` cells
containing the owner. This partitions all but

\[
 (2m+1)e^{-m/512}W                                      \tag{7.9}
\]

middle owners into physical `Q_{2t}` packets. Here
`2t=4\cdot2^a` is an allowed factor dimension. On every lower face of
every retained packet,

\[
                         J(L)=J(X).                    \tag{7.10}
\]

#### Proof

The sixteen hard restrictions form four disjoint `Q_2` cells, so under
uniform Boolean sampling a grid is eligible with probability `1/16`.
The number `Z` of eligible grids is `\operatorname{Bin}(B,1/16)`.
Since `t\le B/32`, the multiplicative Chernoff bound gives

\[
 \Pr(Z<t)\le\Pr(Z<B/32)\le e^{-B/128}=e^{-m/512}.   \tag{7.11}
\]

Conditioning on total rank `m` costs at most `2m+1`, proving (7.9).
Varying an owner inside its selected local `Q_2` never changes eligibility,
the selected-grid list, or the local cell label. Hence fixing the exterior
and taking the product of all selected cells gives an owner-disjoint
`Q_{2t}` partition.

On an active grid the local product
`K_{\mathcal R}K_{\mathcal C}` is zero at the middle owner and remains
zero after either deletion, in either order, down to the local core. On a
frozen grid its contribution is unchanged. Summing over grids proves
(7.10), even under arbitrary interleaving of active-grid directions.
`\square`

For arbitrary `m`, take `B=\lfloor m/4\rfloor` grids and freeze the fewer
than eight residual coordinates. Then `4B=m+O(1)`, (7.9) changes only by
an `e^{O(1)}` factor, and the expectation calculation below has `4B` in
place of `m`. All conclusions, including the derivative
`1/4+O_A(m^{-1/2})`, remain valid.

### Proposition 7.2 (one-hot lower obstruction)

Install an isometric factor in every packet of Lemma 7.1 and allow at most
one arbitrary lower occurrence from each exceptional owner. Then, for all
sufficiently small fixed `A>0`, at `q=A\sqrt m+O(1)` the resulting full
occurrence system has at least `c_AW` lower holes for some `c_A>0` and all
sufficiently large `m`. In particular, no exact-factor or literal
completion of the exceptional set can repair this packet architecture.

Indeed, on every retained lower trace, at every intermediate depth and
under arbitrary interleaving of different cells,

\[
                         J(L)=J(X).                  \tag{7.12}
\]

Uniform target layers instead satisfy

\[
 \mathbb E_mJ-\mathbb E_{m-q}J={q\over4}+O_A(1).     \tag{7.13}
\]

#### Proof

In one hard cell the middle profile is one of the two vectors in (7.6).
Along either possible deletion order to its lower core, the local profile
remains one-hot or becomes `(0,0)`. Its product is therefore always zero.
Frozen blocks retain their original contribution, whether or not it is
zero. This reproves (7.12) without a clustered-square assumption.

For a uniform rank-`k` set, one row quartet and one column quartet overlap
in two coordinates. They both have occupancy three in exactly

\[
 2\binom{2m-6}{k-5}+4\binom{2m-6}{k-4}              \tag{7.14}
\]

sets: the common pair contributes respectively one or two selected
coordinates. There are `m` ordered row-column pairs across all grids, so

\[
 \mathbb E_kJ
 =m\,
 {2\binom{2m-6}{k-5}+4\binom{2m-6}{k-4}
  \over\binom{2m}k}.                                 \tag{7.15}
\]

Expanding (7.15) at `k=m+O_A(\sqrt m)` gives derivative
`1/4+O_A(m^{-1/2})` and proves (7.13).

For completeness, `J` has the following uniform slice concentration:
for `k=m+O_A(\sqrt m)`,

\[
 \Pr_k(|J-\mathbb E_kJ|>x)\le2e^{-x^2/(C m)}.       \tag{7.16}
\]

Indeed a selected/unselected coordinate swap changes at most two grid
summands, each lying in `[0,4]`, so it changes `J` by at most eight.
Expose a uniform rank-`k` set by a random ordering and couple two
completions after each exposure by one swap. The Doob differences are
bounded by eight; Azuma's inequality proves (7.16), after enlarging the
absolute constant `C`.

Integrating (7.16) gives the trimming bound: if a subset of a central
layer has relative size at least `1-\alpha`, `0<\alpha\le1/2`, then its
mean differs from the full-layer mean by at most

\[
 C_1\alpha\sqrt{\log(e/\alpha)}\sqrt m.             \tag{7.17}
\]

Suppose there are `h\le c_AW` holes and choose one source occurrence for
each covered target. Distinct targets use distinct source occurrences.
Discard the at most `(2m+1)e^{-m/512}W` chosen pairs whose sources are
exceptional; this changes all following fractions by `e^{-\Omega(m)}`.
For every remaining pair, (7.12) makes the source and target `J`-values
identical. Since

\[
 {\binom{2m}{m-q}\over W}=e^{-A^2+o(1)},            \tag{7.18}
\]

the chosen sources omit a fraction
`1-e^{-A^2}+O(c_A)+o(1)=O(A^2+c_A)` of the middle
layer, while the covered targets omit `O(c_A)` of their layer. The
exceptional owners in (7.9) are exponentially negligible. Applying
(7.17) on both layers shows that their two selected means can differ from
the full means by at most

\[
 C_2\{(A^2+c_A)\sqrt{\log(e/(A^2+c_A))}
      +c_A\sqrt{\log(e/c_A)}\}\sqrt m.              \tag{7.19}
\]

Choose an absolute `A_0>0` so the `A^2` term is below `A/16` for
`0<A\le A_0`, and then choose `c_A>0` so the remaining terms are below
`A/16`. Equations (7.12)--(7.13) require equality of the selected means
up to `o(\sqrt m)` from the exceptional owners, whereas (7.13) separates
the full means by
`A\sqrt m/4+O_A(1)`. This contradiction proves `h>c_AW`.
`\square`

This obstruction is scoped to the one-hot hard resolution. It does not
apply to the full `13/32` profile library, which contains other block
profiles. It shows why matching first-order `K` is not a substitute for
the common full-profile Hall theorem.

## 8. Exact implication boundary

The following statements are proved.

1. The complete internal-quartet Gaussian Hall cut, including the constant
   point ratio `e^{-A^2/11}`, the uniform-window bound
   `e^{-A^2/22}`, and the crossing-axis toll, passes independent audit.
2. The cross-exchange parity shores have the exact imbalance (0.1), and
   Theorem 2.1 saturates the smaller shore for every `d,k`.
3. The local matchings tensor integrally into near-spanning `Q_r` packets
   with `r=\Theta(m/\log m)`, subexponential packet size, exponentially
   small leave, and only cross-block axes. Installing the known
   `C_{2r}` factors gives literal rows on the retained owner set; the leave
   has `o(W)` literal baseline cost.
4. The explicit first-split realization is nevertheless killed by the
   fixed-pair Gaussian Hall cut (4.5).
5. For arbitrary saturating matchings, the critical depth-one capacity
   data are the lower/upper arrays (5.2); the full gate uses complete
   ordered target-labelled columns.
6. The two sign-specific `13/32` cross-profile trades are exact, but their
   density alone supplies no common all-depth packet selection.
7. The one-hot two-layer resolution admits its own near-spanning exact
   packetization, but is killed by the joint profile `J`.

Not proved:

* a rank-, selector-, and tag-varying family of saturating cross matchings
  with both shadow arrays sufficiently flat and with controlled ordered
  continuations at every protected depth;
* a componentwise integral choice realizing the large- and small-layer
  sign transports with one common chronology;
* control of the positive-part floors of the complete target-labelled
  multidepth columns extending (5.2); or
* literal target Hall after installing the context-array factor at every
  protected depth.

The shortest viable successor is therefore the following genuinely
stronger, conditional sufficient lemma:

> **Dense full-column HCRT lemma.** For `d=C\log m`, choose physical
> Hall-sharp cross matchings in every local rank, frozen-selector fibre,
> and tag class, and equip their tensor packets with target-labelled
> ordered lower/upper flags. These packet options admit one common
> integral selection with `o(W)` aggregate floor loss at every protected
> depth; one active option is used per selector fibre; the options share a
> common run and satisfy the `L,C,S` cone and cylinder-cycle congruences;
> the laminar SCD tails and all physical seams are literal; and the
> selected owner components have size `e^{o(m)}`.

This lemma is strictly stronger than parity-shore Hall and than the
`13/32` density statement. It is narrower than MWB only after all of its
listed interfaces are proved: owner integrality, packet size, raw
cross-axis supply, and two useful local profile moves are explicit here,
but usable-trade density and the full common-column selection are not.
