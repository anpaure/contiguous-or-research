# Cross-quartet shores as a common-block Latin array: exact kernel identities and the occurrence-scale gate

Date: 2026-07-26

Method: pure mathematics only.  This note uses the literal big, cross, and
small shores from
`MATH_THEOREM_TWO_SIGN_CROSS_QUARTET_PROFILE_TRANSPORT_20260726.md` and a
single certified context-array factor on every physical cube.  No crossed
recursion is used.

## 0. Verdict

The two-sign cross-quartet packet does pass the first two requirements of a
common-block Latin construction.

1.  The big, cross, and small states can be completed to three integral
    packet tilings of one and the same owner macroblock.  A single state
    choice installs a whole factor and is therefore common to every signed
    depth \(q\le H\).
2.  After averaging only a finite local group—permutations inside the two
    quartets and reversal of the carrier cube axis—the literal target kernels
    satisfy, simultaneously for every \(q\),

    \[
       \overline d^{q,-}_{\rm big}=\overline d^{q,-}_{\rm cross},
       \qquad
       \overline d^{q,+}_{\rm small}=\overline d^{q,+}_{\rm cross}.
    \tag{0.1}
    \]

    Thus the advertised one-sign profile equalities can be upgraded to exact
    averaged **literal-kernel** equalities.  The same finite conjugation is
    used at all depths; there is no chronology mismatch.

This still does not verify the floor-covariance inequality.  There are two
precise reasons.

* One elementary cross packet has only one crossing axis.  Exactly a
  \(q/r\) fraction of its depth-\(q\) starts see that axis.  Consequently a
  single disjoint cross-quartet layer changes only \(O(qW/r)=o(W)\)
  occurrences when \(q\le H=o(r)\).  It cannot remove a Gaussian
  \(\Theta(W)\) profile cut.
* The local theorem determines orbit sums of the incidence array
  \(d_{ia}^{q,T}\), but the Latin floor covariance depends on its joined
  literal squares
  \(\sum_Ts_{a;q,T}^2\) and \(\sum_{i,a,T}(d_{ia}^{q,T})^2\).  These are not
  determined by the density \(13/32\), or by (0.1).

The exact necessary scale is now clear.  Tensor \(u\) disjoint three-shore
carrier slots in one \(Q_r\) packet, and suppose an integral state selects
the genuinely cross shore \(X\) in exactly \(s\) of them.  Average those
\(s\) placements among the \(r\) compiler axes.  The fraction of depth-
\(q\) windows seeing at least one physical cross-quartet axis is

\[
                     p_{r,q,s}=1-{\binom{r-s}q\over\binom rq}.
\tag{0.2}
\]

Hence any repair of a profile deficit \(\delta W\) on an owner density
\(\rho\) needs

\[
                         s\ge {\delta+o(1)\over2\rho}{r\over q}.
\tag{0.3}
\]

For Gaussian depths this is \(s=\Omega_A(r/H)\).  Tensor products of the
three shores provide integral common-block options with that many available
slots.  Crucially, a big/small-only
state has \(s=0\): both of those shores are physically internal to the old
quartets.  Selecting \(X\) densely closes that quartet-scale toll, but one
fixed paired-quartet decomposition still has a coarser full-eight-block Hall
cut (Theorem 4.4).  The remaining construction must combine transverse
paired decompositions or a hierarchy and then prove the joined literal
target-square estimate (5.4).

## 1. One common three-shore owner macroblock

Let \(A,B\) be disjoint four-sets and

\[
 V_k^+=\binom Ak\times\binom B{k-1},\qquad
 V_k^-=\binom A{k-1}\times\binom Bk,qquad
 U_k=V_k^+\mathbin{\dot\cup}V_k^-.
\tag{1.1}
\]

Write \(X_k\) for a fixed cross perfect matching \(\Xi_k\) on \(U_k\).
Define three perfect matchings on \(U_k\) by

\[
\begin{array}{c|ccc}
 &k=1&k=2,3&k=4\\ \hline
 B_k&\Lambda_k^{\rm big}&\Lambda_k^{\rm big}&X_4\\
 X_k&X_1&X_k&X_4\\
 S_k&X_1&\Lambda_k^{\rm small}&\Lambda_4^{\rm small}.
\end{array}
\tag{1.2}
\]

Thus the unavailable small shore at \(k=1\), and the unavailable big shore
at \(k=4\), are padded by a duplicate of the cross shore.  This is an
integral option, not a fractional convention.

For every \(k\), tensor every edge with a common physical
\(Q_{r-1}\) reservoir in the complementary rank sector.  Different \(k\)'s
may require different frozen reservoir ranks; their owner sets are disjoint.
Taking their disjoint union gives three packet tilings

\[
                         \mathcal R_B,\quad\mathcal R_X,
                         \quad\mathcal R_S
\tag{1.3}

of one common owner macroblock.  Each packet is a literal \(Q_r\).

### Proposition 1.1 (simultaneous integral legality)

Every state in (1.3) is an integral tiling of exactly the same owners by
whole \(Q_r\) packets.  Installing one certified factor in every packet
defines all its lower and upper target kernels simultaneously for every
\(q\le H\).  In particular, choosing among \(B,X,S\) is one common choice
across all depths.

#### Proof

Every entry in (1.2) is a perfect matching of \(U_k\).  An edge times
\(Q_{r-1}\) is a \(Q_r\), and either matching partitions the same Cartesian
owner set.  The four \(k\)-sectors and their frozen reservoir tags are
disjoint.  Their union proves the first statement.  A compiler state is a
whole factor on a selected packet, not a depth-indexed object, so it supplies
all protected traces at once. \(\square\)

The local owner mass on which \(B\) and \(X\) differ is

\[
 2\sum_{k=1}^3\binom4k\binom4{k-1}=104,
\tag{1.4}
\]

and the same count holds for \(S\) versus \(X\).  Relative to all \(256\)
local subsets this is \(13/32\); relative to the common odd-rank macroblock,
whose local mass is \(112\), it is \(13/14\).  The simultaneous \(B\)-versus-
\(S\) effect exists on the \(k=2,3\) sectors, of ambient density
\(96/256=3/8\).  This last big/small comparison changes finer block-size
profiles but uses no physical cross-quartet edge; it therefore cannot change
the full/empty-quartet Hall invariant proved in Theorem 4.1.

## 2. Exact literal-kernel relations after finite local symmetrization

Let

\[
                         G=S_A\times S_B.
\tag{2.1}
\]

For \(\sigma\in\{B,X,S\}\), \(g\in G\), and \(\eta\in\{0,1\}\), conjugate
the shore by \(g\), identify its carrier edge with abstract cube axis one,
and translate the certified cube factor by \(\eta e_1\).  The translation
reverses the two physical endpoints of every carrier edge while preserving
the whole factor.  Denote the resulting integral target kernel by

\[
                         d_{\sigma,g,\eta}^{q,\epsilon}(T).
\tag{2.2}

Define its finite local average

\[
 \overline d_{\sigma}^{q,\epsilon}(T)
 ={1\over2|G|}\sum_{g\in G}\sum_{\eta=0}^1
 d_{\sigma,g,\eta}^{q,\epsilon}(T).
\tag{2.3}

### Theorem 2.1 (all-depth triangular literal identities)

For every protected \(q\), with the same average (2.3),

\[
 \boxed{
 \overline d_B^{q,-}=\overline d_X^{q,-},
 \qquad
 \overline d_S^{q,+}=\overline d_X^{q,+}.}
\tag{2.4}

Moreover, \(\overline d_B^{q,+}-\overline d_X^{q,+}\) and
\(\overline d_S^{q,-}-\overline d_X^{q,-}\) are supported on compiler
records whose depth-\(q\) window contains carrier axis one.

#### Proof

Fix one abstract compiler start and its next \(q\) distinct directions.
First suppose axis one is absent.  Translation by \(e_1\) pairs this record
with the record having the opposite carrier endpoint and the same reservoir
target.  Across the two values of \(\eta\), every physical matching edge
therefore contributes both endpoints, with the same outside target data.
Every shore in (1.2) is a perfect matching of the same local owner set, so
the resulting non-hit kernel is independent of \(\sigma\).

Now suppose axis one is present.  The local lower target is the intersection
of the two endpoints of the carrier edge, and the local upper target is their
union.  Translation by \(e_1\) does not change either set.  In sector \(k\),
the big and cross edges have the same lower profile \((k-1,k-1)\).  They also
have the same number of edges.  The group \(G\) is transitive on all local
subsets with this profile, so averaging over \(g\) makes their literal lower
intersection multisets identical.  At \(k=4\) the shores are identical by
definition.  This proves the first equality in (2.4).

The small and cross edges analogously have the same upper profile \((k,k)\),
and at \(k=1\) they are identical.  The same transitivity argument proves the
second equality.  Only hit records were used in either possible difference,
which proves the support statement. \(\square\)

The finite average is important.  Without it, equal block-size profiles do
not imply equal literal kernels: a particular one-factor may concentrate its
intersections on a proper subset of the profile orbit.  Thus (2.4) is not a
statement about one raw shore pair.

### Corollary 2.2 (exact two-sign simplex)

Let \(p_B,p_X,p_S\ge0\) sum to one, and choose the three locally
symmetrized shores with these probabilities.  Put

\[
 \Delta_q^-:=\overline d_S^{q,-}-\overline d_X^{q,-},
 \qquad
 \Delta_q^+:=\overline d_B^{q,+}-\overline d_X^{q,+}.
\tag{2.5}
\]

Then, simultaneously at every depth,

\[
 \boxed{
 \overline d_p^{q,-}=\overline d_X^{q,-}+p_S\Delta_q^- ,
 \qquad
 \overline d_p^{q,+}=\overline d_X^{q,+}+p_B\Delta_q^+.}
\tag{2.6}
\]

Thus the lower mean is insensitive to how the remaining mass is divided
between big and cross, while the upper mean is insensitive to how it is
divided between small and cross.  The only local common-choice constraint is

\[
                         p_B+p_S\le1.
\tag{2.7}
\]

The same statement tensorizes: after local symmetrization, the lower kernel
of a shore word \(\boldsymbol\sigma\in\{B,X,S\}^t\) is unchanged by replacing
any \(B\)-letter by \(X\), and its upper kernel is unchanged by replacing any
\(S\)-letter by \(X\).

#### Proof

Equation (2.6) is immediate from (2.4) and linearity.  For a tensor shore,
condition on every abstract compiler record and apply the relevant equality
of local kernels in the changed coordinate; all other local and reservoir
factors are common. \(\square\)

This proves that there is no hidden demand for two different depthwise shore
choices.  It does not say that the particular target corrections required by
the global floor ledger lie in the simplex (2.7); that is a genuine signed
Hall condition which must be checked from the literal derivatives.

## 3. Exact occurrence scale

An isometric \(C_{2r}\) in \(Q_r\) has each direction twice, with its two
occurrences cyclically separated by \(r\).  Hence, for \(q<r\), exactly
\(2q\) of its \(2r\) starts have a forward depth-\(q\) window containing a
fixed direction.  The same count holds in every cycle of a vertex factor.

### Lemma 3.1 (one-axis derivative bound)

Let \(U\) be the owner mass of any union of whole packets on one shore.
For either sign,

\[
 \#\{\hbox{starts whose target profile can change}\}={q\over r}U,
\tag{3.1}
\]

and the \(\ell^1\)-norm of the corresponding target-load derivative is at
most

\[
                         2{q\over r}U.
\tag{3.2}
\]

#### Proof

The cycle count above proves (3.1), packet by packet.  Replacing one target
occurrence deletes one unit at its old target and adds one at its new target,
which costs at most two in \(\ell^1\). \(\square\)

For the big/cross upper transport, and the small/cross lower transport, one
may put \(U=(13/32+o(1))W\) in a complete disjoint paired-quartet layer.
Even the weaker bound \(U\le W\) shows that the layer changes only
\(O(qW/r)\) profile occurrences.

### Theorem 3.2 (single-layer Gaussian obstruction)

Suppose a target-profile Hall cut has deficit \(D_q=\delta W+o(W)\), where
\(\delta>0\), before applying one disjoint cross-quartet layer.  Then after
arbitrary choices of its big, cross, and small shores, the same cut has
deficit at least

\[
                         D_q-2{q\over r}W.
\tag{3.3}
\]

In particular, at \(q=A\sqrt m+o(\sqrt m)\), one layer leaves
\((\delta-o(1))W\) deficit whenever \(H=o(r)\).

#### Proof

Only an occurrence whose profile changes can increase the amount of supply
entering the deficient side of the cut.  Relative to the owner-profile
baseline, each of the two compared shores modifies at most \(qW/r\)
occurrences.  Their union therefore has size at most \(2qW/r\), and each
changed occurrence repairs at most one unit. \(\square\)

For the finite locally symmetrized big/cross or small/cross comparison of
Theorem 2.1, the two hit measures have equal total mass and the sharper
total-variation bound \(qW/r\) is available.  The factor two in (3.3) is
retained because the theorem permits arbitrary integral shore phases.

This applies both to the fixed-frame Gaussian cut and to any fixed-quartet
capacity cut which is expressed only in block profiles.  Changes of literal
targets inside one unchanged profile cell do not affect its dual score.

## 4. Tensoring enough carrier slots and selecting enough cross shores

Take \(u\) disjoint paired-quartet macroblocks of Section 1 and a common
\(Q_{r-u}\) reservoir.  For every word

\[
                         \boldsymbol\sigma\in\{B,X,S\}^u,
\tag{4.1}

the tensor product of the corresponding local matching edges with the
reservoir gives an integral tiling of the same owners by \(Q_r\) packets.
Thus the cross-quartet library really does provide \(3^u\) integral
common-block options, one option simultaneously valid at all depths.

Only an \(X\)-letter is a physically cross-quartet axis.  A \(B\)- or
\(S\)-letter is an internal Johnson edge in one of the two old quartets.  If
\(s=s(\boldsymbol\sigma)\) is the number of \(X\)-letters, average the
placement of those \(s\) axes uniformly among the \(r\) abstract compiler
axes.  Every depth-\(q\) window uses \(q\) distinct axes, so the exact hit
probability is (0.2).

For one fixed integral direction word, axis count alone is not enough.  List
the \(2s\) occurrences of the crossing axes cyclically in the isometric
\(C_{2r}\) word, and let \(g_1,\ldots,g_{2s}\) be the cyclic gaps following
them.  The exact hit fraction is

\[
                         \phi_q={1\over2r}
                         \sum_{j=1}^{2s}\min(g_j,q).
\tag{4.1a}
\]

Indeed the starts in the gap of length \(g_j\) which see its preceding
marked occurrence are exactly the last \(\min(g_j,q)\) positions of that
gap.  Thus the occurrences must also be dispersed; placing the \(s\) axes
quasi-uniformly in the permutation half of a standard \(\pi\pi\) word
attains the optimal scale.  Formula (0.2) is the exact average of this
quantity under uniform axis placement.

### Theorem 4.1 (physical cross-shore toll)

Fix the underlying partition into quartets.  In a final owner-disjoint
\(Q_r\)-packet resolution, let \(s(P)\) be the number of axes of packet
\(P\) on which the selected shore is \(X\).  If the resolution has
\(o(W)\) lower and upper holes at
\(q=A\sqrt m+O(1)\), then

\[
 \boxed{
 {1\over W}\sum_Ps(P)|P|=\Omega_A(r/q).}
\tag{4.1b}
\]

In particular, an outcome using only \(B\)- and \(S\)-letters retains
\(\Omega_A(W)\) holes.  The conclusion is independent of how densely its
big/small variables are distributed.

#### Proof

Both \(B\) and \(S\) use coordinate exchanges internal to one old quartet;
only \(X\) exchanges a coordinate between the paired quartets.  Let
\(F(Y)\) be the number of old quartets fully contained in \(Y\).  Along a
lower window with no \(X\)-axis, every local quartet rank is constant, and a
full quartet has no incident internal Johnson edge.  Hence its lower target
\(T\) and every owner \(Y\) in the window satisfy

\[
                         F(T)=F(Y).
\tag{4.1c}
\]

For upper windows, complementation gives the identical invariant for empty
quartets.

This invariant has a Gaussian Hall deficit.  If there are \(c=m/2\)
quartets and

\[
                         h(z)=1+4z+6z^2+4z^3,
\]

then the numbers of lower targets and middle owners with \(k\) full
quartets are exactly

\[
 \binom ck[z^{m-q-4k}]h(z)^{c-k},
 \qquad
 \binom ck[z^{m-4k}]h(z)^{c-k}.
\tag{4.1d}
\]

At
\(k=m/32-(A/4)\sqrt m+O(1)\), their source/target ratio tends to
\(e^{-A^2/11}<1\).  A \(\Theta_A(\sqrt m)\)-window of these \(k\)'s has
positive target mass by the span-one local central limit theorem.  Thus
windows with no \(X\)-axis leave at least \(\delta_AW+o(W)\) holes for some
\(\delta_A>0\).  Every window containing an \(X\)-axis repairs at most one,
so a successful resolution needs \(\Omega_A(W)\) such windows.

Packet \(P\) has at most \(s(P)q|P|/r\) starts whose depth-\(q\) window sees
one of its \(X\)-axes, by the one-axis count and the union bound.  Summing
over the owner-disjoint packets and comparing with \(\Omega_A(W)\) proves
(4.1b). \(\square\)

### Corollary 4.2 (necessary selected-cross-axis count)

If only an owner proportion \(\rho+o(1)\) carries the relevant sign's
profile-changing shore, then a deficit \(\delta W+o(W)\) cannot be repaired
unless

\[
 2\rho\left(1-{\binom{r-s}q\over\binom rq}\right)
 \ge\delta-o(1).
\tag{4.2}
\]

In particular,

\[
                         \boxed{
 s\ge {\delta-o(1)\over2\rho}{r\over q},}
\tag{4.3}
\]

because each of the two shores can modify only its hit set and
\(p_{r,q,s}\le sq/r\).  Under the locally symmetrized comparison, the factor
two can again be deleted.

For the broad block-size profiles, the separate big/cross upper and
small/cross lower transports have \(\rho=13/32\).  For the decisive
full/empty-quartet cut in Theorem 4.1, the relevant density is only
\(\rho=1/32\) per sign: the upper empty-quartet count changes in sector
\(k=1\), of local mass \(8\), and the lower full-quartet count changes in
sector \(k=4\), also of mass \(8\).  Choosing the \(X\)-shore handles these
two disjoint sectors in one common state.  The raw big-versus-small
comparison on the common \(k=2,3\) sectors has density \(3/8\), but it has
no \(X\)-axis in either state and therefore does not enter (4.2); Theorem
4.1 rules it out as a repair of the decisive cut.

The scale (4.3) is compatible with one common all-depth choice.  Indeed the
Gaussian fixed-frame deficit satisfies \(\delta(a)=O_A(a)\) uniformly for
\(0\le a\le A\), where \(a=q/\sqrt m\), because

\[
 \delta(a)=e^{-a^2}\Phi(a/2)-\Phi(-3a/2),
 \qquad \delta(0)=0,
\tag{4.4}
\]

and \(\delta\) is continuously differentiable.  Hence
\(s=C_A r/H\) passes the occurrence-count lower bound simultaneously for
all \(q\le H=A\sqrt m\) if \(C_A\) is sufficiently large.  This is not a
proof of covariance contraction; it only shows that chronology imposes no
larger scale at the counting level.

### Theorem 4.3 (dense-cross-axis owner near-resolution)

Assume first that \(8\mid2m\), and partition the coordinates into
\(B=m/4\) ordered pairs of quartets.  Call one eight-block eligible when its
local owner pattern lies in \(U_1\cup U_4\).  There are exactly

\[
                         |U_1|+|U_4|=8+8=16
\tag{4.5}
\]

eligible patterns out of \(256\).  Let \(r=o(m)\).  There is an exact
owner-disjoint near-resolution by physical \(Q_r\) packets such that every
axis of every retained packet uses the \(X\)-shore and hence crosses its
paired quartets.  Its owner leave satisfies

\[
 \boxed{
 L_r\le\sum_{e<r}\binom Be16^e240^{B-e}
 =2^{(\log_2(240)/4+o(1))m}=o(W/H).}
\tag{4.6}
\]

For every retained packet and every \(1\le q<r\), every depth-\(q\) window
contains exactly \(q\) physical cross-quartet axes.  The same conclusion,
up to an absolute factor in (4.6), holds when at most seven leftover
coordinates are frozen.

#### Proof

For each owner with at least \(r\) eligible eight-blocks, take the first
\(r\) eligible blocks in the fixed block order.  Record, at each active
block, whether its invariant sector is \(k=1\) or \(k=4\); freeze the exact
local subset at every inactive block.  On an active block use the fixed
cross perfect matching \(X_k\) of \(U_k\).  A cross edge stays inside the
same \(U_k\), so it preserves eligibility, the sector value \(k\), and the
first-active list.  Products of one matching edge at each of the \(r\)
active blocks are therefore disjoint literal \(Q_r\)'s and exhaust that
owner region.  Different sector records and inactive tags are disjoint,
proving exact ownership.

Ignoring the global rank condition only enlarges the leave.  Choose the
\(e<r\) eligible blocks, their \(16\) patterns, and arbitrary ineligible
patterns on the remaining blocks.  This gives the first expression in
(4.6).  Since \(r=o(B)\), the sum is
\(240^B\exp(o(m))\).  Now \(\log_2(240)/4<2\), whereas
\(W=2^{2m-o(m)}\), proving the last equality and the required ledger.

Every packet axis is one of the selected cross edges.  A protected compiler
window uses \(q\) distinct packet axes, proving the final assertion.  Frozen
leftover coordinates contribute only an absolute multiplicative factor to
the leave count. \(\square\)

Theorem 4.3 closes the physical occurrence and dispersion requirements much
more strongly than (4.3): the cross fraction is one.  It also retains common
integral alternatives.  At a \(k=1\) active slot one may replace \(X\) by
\(B\), and at a \(k=4\) slot one may replace \(X\) by \(S\), without changing
the owner region.  Thus every product region carries a common all-depth
binary-cube of shore options around the dense \(X\) state.  What remains is
whether transverse copies of those alternatives can first escape the
coarser invariant and then be selected with the floor covariance (5.4).

### Theorem 4.4 (the coarser eight-block obstruction)

The dense-cross-axis resolution of Theorem 4.3 does not by itself remove
the Gaussian Hall cut.  Every one of its axes remains internal to one fixed
eight-block.  At \(q=A\sqrt m+O(1)\), every factor with this property has
\(\Omega_A(W)\) lower holes and \(\Omega_A(W)\) upper holes.

More exactly, let \(F_8(Y)\) be the number of the \(B=m/4\) eight-blocks
which are full in \(Y\), and put

\[
 h_8(z)=(1+z)^8-z^8.
\tag{4.7}
\]

The target and source counts at full-block profile \(k\) are

\[
 \binom Bk[z^{m-q-8k}]h_8(z)^{B-k},
 \qquad
 \binom Bk[z^{m-8k}]h_8(z)^{B-k}.
\tag{4.8}
\]

For

\[
 k={m\over1024}-{255A\over1024}\sqrt m+O(1),
\tag{4.9}
\]

their source/target ratio tends to

\[
                         \boxed{e^{-255A^2/247}<1.}
\tag{4.10}
\]

#### Proof

If every exchanged coordinate pair lies in one eight-block, local rank in
that block is constant along the owner window.  A full block has no internal
Johnson edge.  Thus a lower target and its owner have the same value of
\(F_8\); complementation gives the empty-block upper invariant.  Equations
(4.8) follow by choosing the full blocks and allowing a proper subset in
every other block.

Normalize the coefficients of \(h_8\) by the span-one variable

\[
 \Pr(J=j)={\binom8j\over255},\qquad0\le j\le7.
\]

Direct differentiation of \((1+z)^8-z^8\) at \(z=1\) gives

\[
 \mu={1016\over255},
 \qquad
 \sigma^2={126464\over65025}.
\tag{4.11}
\]

Write \(k=m/1024+y\sqrt m+O(1)\) and \(d=B-k\).  Then

\[
 \sigma^2d={247\over510}m+O(\sqrt m),
\tag{4.12}
\]

while the source and target coefficient deviations from \(\mu d\) are

\[
 -{1024\over255}y\sqrt m+O(1),
 \qquad
 \left(-A-{1024\over255}y\right)\sqrt m+O(1).
\tag{4.13}
\]

At \(y=-255A/1024\), these are respectively \(A\sqrt m+O(1)\) and
\(O(1)\).  The lattice local central limit theorem therefore gives

\[
 \log{\text{source}\over\text{target}}
 =-{A^2m\over2(247m/510)}+o(1)
 =-{255A^2\over247}+o(1),
\]

which is (4.10).  Finally, under the exact rank conditioning the full-
eight-block count has variance

\[
 {m\over4}\left({1\over256}-{9\over256^2}\right)+O(\sqrt m)
 ={247m\over262144}+O(\sqrt m)>0.
\tag{4.14}
\]

Hence a \(\Theta_A(\sqrt m)\)-window around (4.9) has positive target
mass.  Summing its source deficits proves the lower Hall bound; complement
proves the upper bound. \(\square\)

Thus Theorem 4.3 closes the *quartet* occurrence toll but exposes the same
invariant at the paired-block scale.  A successful Latin atlas must also
move axes between different eight-blocks—by a transverse family of pairings
or a genuine hierarchy.  Dense use of one fixed paired-quartet decomposition
is not enough.

### Corollary 4.5 (every fixed bounded block scale has the same cut)

Let a fixed partition of \([2m]\) into blocks of any fixed size \(b\ge2\)
be given, with divisibility errors frozen.  Every factor whose physical axes
remain inside those blocks has \(\Omega_{A,b}(W)\) lower and upper holes at
\(q=A\sqrt m+O(1)\).

#### Proof

Put \(D_b=2^b-1\),
\(h_b(z)=(1+z)^b-z^b\), and let

\[
 \Pr(J_b=j)={\binom bj\over D_b},\qquad0\le j<b.
\]

Write \(\mu_b=\mathbb EJ_b\), \(\sigma_b^2=\operatorname {Var}J_b>0\),
and

\[
 a_b=b-\mu_b={b2^{b-1}\over D_b},
 \qquad
 v_b={2(1-2^{-b})\over b}\sigma_b^2>0.
\tag{4.15}
\]

There are \(2m/b\) blocks.  At full-block count

\[
 k={m\over b2^{b-1}}-{A\over a_b}\sqrt m+O(1),
\tag{4.16}
\]

the source coefficient deviation in the analogue of (4.13) is
\(A\sqrt m+O(1)\), while the target deviation is \(O(1)\), and
\(\sigma_b^2d=v_bm+O(\sqrt m)\).  Hence the exact source/target ratio tends
to

\[
                         e^{-A^2/(2v_b)}<1.
\tag{4.17}
\]

The fixed-rank full-block count has nonzero conditional variance of order
\(m\), since the full-block indicator is not an affine function of local
rank.  The bivariate span-one local central limit theorem gives positive
target mass in a \(\Theta_{A,b}(\sqrt m)\)-window around (4.16).  The same
profile-invariance argument as in Theorem 4.4 completes the proof.
\(\square\)

Thus a finite-depth hierarchy ending at a bounded block size is always
obstructed.  The hierarchy depth or the transverse overlap of its block
partitions must grow with \(m\); this conclusion is independent of the local
shore densities.

## 5. Insertion into the Latin covariance formula

Group disjoint owner macroblocks into batches indexed by \(i\in[b]\).  Give
every block the same list of \(b\) integral tensor-shore/conjugation states,
indexed by \(a\in[b]\), and define

\[
 d_{ia}^{q,T}
 =\#\{\hbox{depth-}q\hbox{ occurrences of literal target }T
       \hbox{ in option }a\hbox{ on block }i\}.
\tag{5.1}
\]

Choosing option \(\pi(i)\) for a permutation \(\pi\in S_b\) is
owner-perfect.  Put

\[
 S_{q,T}=\sum_{i,a}d_{ia}^{q,T},\quad
 r_{i;q,T}=\sum_a d_{ia}^{q,T},\quad
 s_{a;q,T}=\sum_i d_{ia}^{q,T}.
\tag{5.2}

The exact expected factorial collision count is

\[
 \mathbb E_\pi[Z_{q,T}(Z_{q,T}-1)]
 ={S_{q,T}^2-\sum_i r_{i;q,T}^2-\sum_a s_{a;q,T}^2
       +\sum_{i,a}(d_{ia}^{q,T})^2\over b(b-1)}.
\tag{5.3}

Thus, with \(c_q=\lfloor W/N_q\rfloor\), the exact remaining condition is

\[
\boxed{
 \sum_{q,\epsilon,T}\left[
 {S_{q,T}^2-\sum_i r_{i;q,T}^2-\sum_a s_{a;q,T}^2
       +\sum_{i,a}(d_{ia}^{q,T})^2\over b(b-1)}
 -2c_q{S_{q,T}\over b}+c_q(c_q+1)
 \right]=o(W).}
\tag{5.4}
\]

Theorem 2.1 supplies exact linear identities among the local-group averages
of the columns in (5.1).  It does not determine either square term in
(5.4).  In particular, two local one-factors can have the same intersection
profile while concentrating on different literal subsets of that profile
orbit.  The choice of cross one-factor \(\Xi_k\), packet phase, and joined
reservoir trace affects those squares.

There is a concrete consequence for the first-eligible additive resolution
in
`MATH_THEOREM_AFFINE_TRANSVERSE_FRAME_PROFILE_CANCELLATION_AND_FLOOR_COVARIANCE_GAP_20260726.md`.
That resolution leaves only one distinguished big/small carrier variable in
each final \(Q_r\) region, but it never selects the cross shore.  It is the
case \(s(P)=0\), not the case of one physical crossing axis.  Its fixed-slice
covariance identity is correct, but every one of its outcomes obeys the
full/empty-quartet invariant (4.1c) and hence has \(\Omega_A(W)\) Gaussian
holes.  Consequently its displayed centered-scatter sufficient inequality
cannot hold.  The additive construction must first admit actual \(X\)-shore
states and select \(\Omega_A(r/H)\) dispersed crossing axes per final packet
on average.

Therefore the density \(13/32\) cannot certify (5.4).  What remains is a
growing-slot joined-kernel theorem: after selecting
\(s\gg r/H\) locally symmetrized \(X\)-axes in typical final packets, prove
that the two negative
without-replacement square terms in (5.4) reduce the total variance to the
integer floor baseline.  Alternatively, an explicit literal-target cut for
that tensor array would close the lane negatively.

## 6. Precise proved boundary

The cross-quartet input is stronger than a density statement:

* it gives three integral options on common owner blocks;
* the options are common to all depths;
* finite local symmetrization gives the exact literal-kernel identities
  (2.4);
* tensoring \(u\) carrier slots produces \(3^u\) integral common-block
  states.

It is nevertheless not yet a floor-covariance theorem.  One elementary
layer is rigorously too weak by Theorem 3.2, while a big/small-only layer is
ruled out exactly by Theorem 4.1.  The first scale not excluded selects
\(s=\Theta_A(r/H)\) actual cross shores per typical packet, and vanishing
contraction will likely require \(sH/r\to\infty\).  A fixed dense \(X\)
decomposition is then ruled out at the next block scale by Theorem 4.4.
After a transverse/hierarchical escape from that invariant, the remaining
quantity is the joined literal target-square ledger (5.4).
