# Gaussian Hall cut for the full block-internal quartet atlas

Date: 2026-07-26

## 0. Result

Let (m) be even, put (c=m/2), and partition ([2m]) into (c)
labelled quartets.  Allow the complete block-internal atlas: in every
quartet one may use every one-factor of (J(4,1)), (J(4,2)), or
(J(4,3)), tensor these choices across quartets, choose active quartets
arbitrarily, and install any return-free packet compiler.  No active
coordinate pair is allowed to meet two different quartets.

The old two-parameter ratio

\[
 {2^q\binom gq\over\binom{u+q}q}
\]

does not count this enlarged atlas.  Nevertheless the enlarged atlas has
a different exact Hall obstruction.

### Theorem 0.1 (full internal-atlas Hall deficit)

Fix (A>0) and let (q=\lfloor A\sqrt m\rfloor).  There is
(\delta_A>0) such that every middle-owner factor whose depth-(q)
windows use only block-internal coordinate pairs misses at least

\[
                         (\delta_A-o(1))W,
 \qquad W=\binom{2m}m,                              \tag{0.1}
\]

lower targets.  By complementation, the same bound holds for upper
targets.

More precisely, if (F(S)) denotes the number of quartets completely
contained in (S), then every internal lower realization (T\subset X)
satisfies

\[
                         F(T)=F(X).                  \tag{0.2}
\]

For

\[
 k={m\over32}-{A\over4}\sqrt m+O(1),               \tag{0.3}
\]

the exact profile counts obey

\[
 {\#\{X\in\binom{[2m]}m:F(X)=k\}
  \over
  \#\{T\in\binom{[2m]}{m-q}:F(T)=k\}}
 \longrightarrow e^{-A^2/11}.                     \tag{0.4}
\]

A window of (k)-values of width (\Theta_A(\sqrt m)) around (0.3)
contains a positive fraction of the target layer and has ratio uniformly
bounded below one.  Summing its Hall deficits proves (0.1).

Consequently, any successful packet construction must use
(\Omega_A(W)) depth-(q) windows containing a physically cross-quartet
axis.  If a (Q_r) packet has (s) such axes, at most (sq/r) of its
start fraction sees one.  Therefore a successful construction with
(q\le H=o(r)) must have

\[
                {1\over W}\sum_{P}s(P)|P|
                    =\Omega_A(r/q),                \tag{0.5}
\]

equivalently (\Omega_A(r/q)) crossing axes on average over owner
occurrences.  A bounded number of one-cross-axis rounds cannot suffice.

The independent audit
`MATH_AUDIT_FULL_INTERNAL_QUARTET_HALL_AND_DENSE_CROSS_AXIS_SCHEDULING_20260726.md`
verifies the invariant, coefficient ratio, Gaussian exponent, positive-mass
step, and physical-crossing consequence.  It also records the scope of the
last implication: the weighted axis toll assumes an owner-disjoint
(Q_r)-packet decomposition with isometric (C_{2r}) factors and (q<r).
The architecture-free conclusion is the (\Omega_A(W)) number of
cross-quartet based windows.

## 1. The invariant

Let (T\in\binom{[2m]}{m-q}) be the lower intersection of a return-free
length-(q) window contained in a product of block-internal Johnson
edges, and let (X\in\binom{[2m]}m) be any owner in that window.

In an inactive quartet, (T) and (X) have the same local subset.  In
an active quartet, the packet uses one edge of (J(4,j)) for some
(j\in\{1,2,3\}); the local source has size (j), while the local
intersection has size (j-1\le2).  In particular an active quartet is
never full in either (T) or (X).  Hence the full quartets are exactly
the same inactive quartets on both sides.  This proves (0.2).

The argument permits every local one-factor, every choice of active
quartets, every axis order, and every compiler conjugate.  It is therefore
uniform over the complete block-internal option atlas, not merely the old
three-edge (Q_4) mosaic.

For (k\in\{0,\ldots,c\}), put

\[
 \mathcal T_{q,k}=\{T\in\tbinom{[2m]}{m-q}:F(T)=k\},\qquad
 \mathcal X_k=\{X\in\tbinom{[2m]}m:F(X)=k\}.       \tag{1.1}
\]

Every compatible source of a target in (\mathcal T_{q,k}) belongs to
(\mathcal X_k).  Since one middle owner supplies only one start
occurrence at a fixed signed depth, every internal factor has at least

\[
                    (|\mathcal T_{q,k}|-|\mathcal X_k|)_+     \tag{1.2}
\]

holes in this profile.  Distinct (k)-profiles use disjoint source
families, so their deficits add.

## 2. Exact profile counts

Write

\[
                    h(z)=1+4z+6z^2+4z^3=(1+z)^4-z^4.          \tag{2.1}
\]

After choosing the (k) full quartets, every remaining quartet is a
proper subset and contributes the corresponding coefficient of (h).
Therefore

\[
\begin{aligned}
 |\mathcal T_{q,k}|
   &=\binom ck[z^{m-q-4k}]h(z)^{c-k},\\
 |\mathcal X_k|
   &=\binom ck[z^{m-4k}]h(z)^{c-k}.
\end{aligned}                                                   \tag{2.2}
\]

The binomial prefactor is identical and cancels in the ratio.

Let (J) be the span-one random variable

\[
 \Pr(J=j)={\binom4j\over15},\qquad j=0,1,2,3.       \tag{2.3}
\]

Its mean and variance are

\[
                       \mu={28\over15},\qquad
                       \sigma^2={176\over225}.       \tag{2.4}
\]

If (d=c-k), then

\[
             [z^s]h(z)^d=15^d\Pr(J_1+\cdots+J_d=s).             \tag{2.5}
\]

## 3. The Gaussian ratio

Take

\[
 q=A\sqrt m+O(1),\qquad
 k={m\over32}+y\sqrt m+O(1),                       \tag{3.1}
\]

where (A,y) are fixed.  Then

\[
 d={15m\over32}-y\sqrt m+O(1),qquad
 \sigma^2d={11m\over30}+O(\sqrt m).                \tag{3.2}
\]

For the target and source coefficient indices

\[
 s_T=m-q-4k,qquad s_X=m-4k=s_T+q,                 \tag{3.3}
\]

direct substitution gives

\[
\begin{aligned}
 s_T-\mu d
   &=\left(-A-{32y\over15}\right)\sqrt m+O(1),\\
 s_X-\mu d
   &=-{32y\over15}\sqrt m+O(1).
\end{aligned}                                                   \tag{3.4}
\]

The lattice local central limit theorem, uniformly for fixed compact
sets of (A,y), now yields

\[
 \log{|\mathcal X_k|\over|\mathcal T_{q,k}|}
 =-{(s_X-\mu d)^2-(s_T-\mu d)^2\over2\sigma^2d}+o(1)
 ={15A^2+64Ay\over11}+o(1).                        \tag{3.5}
\]

At (y=-A/4), equation (3.5) is

\[
              \log{|\mathcal X_k|\over|\mathcal T_{q,k}|}
                 =-{A^2\over11}+o(1),              \tag{3.6}
\]

which proves (0.4).

For definiteness, restrict (y) to

\[
             \left[-{A\over4}-{A\over128},
                    -{A\over4}+{A\over128}\right].             \tag{3.7}
\]

Then (3.5) is at most (-A^2/22+o(1)), uniformly in the
corresponding integer (k)-window.

## 4. Positive target mass

Under the product Bernoulli law of parameter

\[
                     p={m-q\over2m}
                       ={1\over2}-{A\over2\sqrt m}+O(m^{-1}),   \tag{4.1}
\]

conditioning on total rank (m-q) gives the uniform target layer.  The
number of full quartets has central value

\[
 cp^4={m\over32}-{A\over8}\sqrt m+O(1)             \tag{4.2}
\]

and variance of order (m) after the rank conditioning.  The conditional
bivariate local central limit theorem (equivalently Stirling's formula
summed over the window (3.7)) therefore gives a constant (c_A>0) such
that

\[
 \sum_{k\text{ in }(3.7)}|\mathcal T_{q,k}|
                       \ge(c_A-o(1))N_q.            \tag{4.3}
\]

Equations (1.2), (3.5), and (4.3) imply at least

\[
 (c_A-o(1))(1-e^{-A^2/22})N_q                     \tag{4.4}
\]

lower holes.  Finally

\[
                         {N_q\over W}\longrightarrow e^{-A^2},           \tag{4.5}
\]

so (0.1) holds, for example with

\[
             \delta_A={c_A\over2}(1-e^{-A^2/22})e^{-A^2}>0.   \tag{4.6}
\]

For reference, the conditional variance can be read off explicitly.  In
one Bernoulli-(p) quartet let (K) indicate fullness and let (L) be the local
rank.  The Gaussian conditional variance per quartet is

\[
 p^4(1-p^4)-4p^7(1-p).                              \tag{4.7}
\]

At (p=1/2) this is (11/256), so after conditioning the (c=m/2) blocks on
total rank,

\[
                         \operatorname{Var}(F)
 ={11m\over512}+O(\sqrt m).                         \tag{4.8}
\]

Thus the window (3.7) has a fixed positive width on the conditional
standard-deviation scale, justifying the positive constant in (4.3).

Complementation turns full quartets in a lower target into empty quartets
in the corresponding upper target and preserves the entire argument.

## 5. Crossing-occurrence toll

Take the full internal atlas as the baseline.  Changing one depth-(q)
start occurrence changes only one literal lower target, so it can fill at
most one hole from (0.1).  Therefore a successful construction must alter
(\Omega_A(W)) lower occurrences using windows which are not wholly
block-internal.  Every such window contains a physically cross-quartet
axis.

In a (Q_r) packet whose factor cycles are isometric (C_{2r})'s, every
axis occurs twice in a direction word of length (2r), and exactly (2q)
cyclic starts have that occurrence in a length-(q) window.  Thus one
axis lies in exactly a (q/r) fraction of all packet starts.  If (s(P))
axes of packet (P) cross quartets, the union bound gives at most

\[
                         {s(P)q\over r}|P|           \tag{5.1}
\]

noninternal occurrences.  Summing (5.1) and comparing with (0.1) proves
(0.5).

## 6. Audited boundary

Proved:

* a linear Gaussian Hall deficit uniform over the complete
  block-internal quartet atlas;
* the exact invariant causing it;
* a separate lower and upper deficit; and
* the occurrence-scale crossing-axis toll (0.5).

Not proved:

* a disjoint owner tiling with a linear fraction of crossing axes per
  large packet;
* a common all-depth compiler after accumulating those axes; or
* the hierarchical floor-energy/circulation theorem `HCRT`.

The correct next construction target is therefore no longer a bounded
one-cross-axis trade round.  It is a dense cross-frame packet mosaic in
which typical (Q_r) packets contain enough cross-quartet axes to meet
(0.5), while the owner tiling and one common all-depth compiler remain
exact.
