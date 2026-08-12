# Parity-complete paired-order lift: exact endgame interface and SCD-prefix audit

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Let

\[
                         W=\binom{2m}m.
\]

A successful parity-complete paired-order factor plugs into the established
factor-blind endgame with **no new collar**. If its good middle-owner mass
`G` is partitioned into physical `C_(4r)` cycles, if `H<2r`, and if

\[
 \Delta_H=\sum_{q=1}^H(M_q^-+M_q^+)=o(W)             \tag{0.1}
\]

is the actual aggregate signed target-hole count, then the exact finite
bound is

\[
 \boxed{
 \nu(2m)\le
 W+{H\over2r}G+\Delta_H+L_m(m-H-1).}                 \tag{0.2}
\]

The term `HG/(2r)` is exactly `2H` per physical `C_(4r)`. Adjacent
`b_i,a_i` pair boundaries, even/odd coarse phases, packet boundaries, and
the central-to-tail join contribute zero additional letters. The omitted
middle owners are appended once and cancel the middle leave exactly.

The complete-word trimmed lift gives

\[
 \boxed{
 \nu(2m+1)\le
 2\left[W+{H\over2r}G+\Delta_H+L_m(m-H-1)\right].}    \tag{0.3}
\]

Thus `H/sqrt(m)->infinity`, `H/r->0`, and (0.1) imply constant one in
both parities.

Two scope corrections are essential.

1. The aligned code displayed in the paired-order theorem, at the same
   nominal coarse depth, does not by itself certify every physical cyclic
   window. There are four start-parity/window-parity cases. In a
   coordinate-disjoint Johnson cell all four reduce, by deterministic
   boundary completion, to aligned codes through one coarse depth farther.
   Thus aligned control through
   `floor(H/2)+1` is sufficient and no separate physical collar is needed.
   Without that direction decoder, all four classes must be stated.
2. Even perfect injectivity inside every paired packet does not imply
   (0.1). Cross-packet repetitions remain, and their exact conversion to
   holes is given in Section 3. A local theorem plugs into the endgame only
   after this outer target deficit is controlled.

There is a positive SCD-prefix ownership construction. For any neighbor
permutation `G` of `Q_r`, with direction function `delta`,

\[
 \boxed{d_p(x)=\delta(p\oplus x)}                    \tag{0.4}
\]

satisfies every parity complete-mapping equation. Taking `G` from an
SCD-derived matching gives a literal SCD construction; taking `G` from a
long doubled-prefix factor also gives the required `C_(2r)` coarse cycles.
However, (0.4) has aligned trace multiplicity at least `2^(d-1)` after `d`
completed pairs, so it cannot solve the local trace-code theorem.

The nontrivial affine twist

\[
                         d_p(x)=\delta_0(Sp\oplus x) \tag{0.5}
\]

avoids that universal diagonal form, but has its own exact collision
invariant. If `J` is a completed-direction support, the aligned trace has
multiplicity at least

\[
 2^{|J\cap S^{-1}J|-1}                               \tag{0.6}
\]

when the intersection is nonempty. Hence injectivity requires
`|J cap S^(-1)J|<=1` for every protected prefix support. In particular,
the existing `Q_4` seed with `S=(2 4)` already has a collision at three
completed pairs, i.e. physical length six.

There is also an explicit growing non-diagonal prefix construction.  From
any doubled-permutation `C_(2s)` factor it builds a doubled-permutation
`C_(4s)` factor on two coordinate blocks, and the root-block swap supplies
the second neighbor permutation required by (0.5).  Iterating from `Q_1`
solves all ownership equations for every power-of-two coarse dimension.
However, its aggregate aligned trace collision excess through physical
depth `H` is

\[
                         \Omega\!\left({H^2\over r}\right)       \tag{0.7}
\]

times the local owner mass.  It therefore requires `H=o(sqrt(r))`, exactly
opposite to the factor-blind tail regime `H/sqrt(m)->infinity` when
`r=Theta(m)`.

No growing SCD-prefix solution of the full trace theorem is proved here.
The audit reduces it to an exact target: a twisted common-phase SCD factor
pair satisfying complete mappings, aligned trace control through
`floor(H/2)+1` (or all four codes explicitly), the full punctured-prefix
separation criterion in Section 6, and the outer packet deficit (0.1).

## 1. Exact physical geometry of the paired lift

Write the `2r` physical cube coordinates as pairs

\[
                         (a_i,b_i),\qquad i\in[r],     \tag{1.1}
\]

and represent a physical vertex by

\[
                         x_i=a_i,
 \qquad p_i=a_i\oplus b_i.                            \tag{1.2}
\]

For every even context `p`, let

\[
 F_p(x)=x\oplus e_{d_p(x)}                            \tag{1.3}
\]

be a neighbor permutation of `Q_r`. Assume the pointwise complete-mapping
equations

\[
 \boxed{
 T_x:p\longmapsto p\oplus e_{d_p(x)}
 \text{ is a bijection }Q_r^{\rm even}\to Q_r^{\rm odd}}
                                                               \tag{1.4}
\]

for every `x`. The paired lift first toggles `b_i`, changing `p`, and then
toggles `a_i`, performing the coarse `x`-move. Its square on an even
context is

\[
                         \widetilde F^2(p,x)=(p,F_p(x)).          \tag{1.5}
\]

Suppose every cycle of every `F_p` has length `2r` and doubled-permutation
direction word

\[
                         \pi_p\pi_p.                  \tag{1.6}
\]

Then every lifted cycle has length `4r` and physical direction word

\[
 \rho_p\rho_p,
 \qquad
 \rho_p=(b_{\pi_{p,1}},a_{\pi_{p,1}},\ldots,
         b_{\pi_{p,r}},a_{\pi_{p,r}}).               \tag{1.7}
\]

Every direction occurs exactly once in `rho_p`. In a coordinate-disjoint
Johnson embedding, a physical direction exchanges the two members of one
fixed ground-coordinate pair, and distinct cube directions use disjoint
pairs. Therefore every positive coordinate run has exactly `2r` states.
For

\[
                              H<2r,                   \tag{1.8}
\]

the lifted cycle is cyclically delay-`H` safe in the exact OR sense: every
positive run has at least `H+1` states, and every flag through depth `H`
has ranks `m-q,m+q`.

Define the physical delay atoms on one cycle by

\[
                         B_j=\bigcap_{s=0}^HX_{j-s}.  \tag{1.9}
\]

The standard coordinate-run identities give

\[
 X_i=\bigcup_{j=i}^{i+H}B_j,                         \tag{1.10}
\]

\[
 \bigcap_{s=0}^qX_{i+s}
 =\bigcup_{j=i+q}^{i+H}B_j,                           \tag{1.11}
\]

and

\[
 \bigcup_{s=0}^qX_{i+s}
 =\bigcup_{j=i}^{i+q+H}B_j                            \tag{1.12}
\]

for `0<=q<=H`. Repeating the first `2H` atoms linearizes every cyclic
witness. Thus one physical `C_(4r)` compiles in exact constructed length

\[
                              4r+2H.                  \tag{1.13}
\]

This proof is performed after the paired lift, on the actual physical state
cycle. It neither sees nor charges the internal boundaries between
`b_i,a_i` moves. That is the precise reason there is no paired-order collar
in addition to `2H`.

## 2. Exact factor-blind endgame theorem

Let a set of `G=W-u` distinct middle owners be partitioned by the paired
factor into physical `C_(4r)` cycles. The cycle count is

\[
                              K={G\over4r}.            \tag{2.1}
\]

For each cyclic start and `1<=q<=H`, take the actual physical lower and
upper flags

\[
 L_{i,q}=\bigcap_{s=0}^qX_{i+s},
 \qquad
 U_{i,q}=\bigcup_{s=0}^qX_{i+s}.                     \tag{2.2}
\]

Let `M_q^-` and `M_q^+` count the physical targets in ranks `m-q` and
`m+q` absent from all these flags, and define `Delta_H` by (0.1).

### Theorem 2.1 (paired-order factor-blind compiler)

For every `1<=H<2r` one has the exact finite bounds

\[
 \boxed{
 \begin{aligned}
 \nu(2m)
 &\le W+2HK+\Delta_H+L_m(m-H-1)\\
 &=W+{H\over2r}G+\Delta_H+L_m(m-H-1),
 \end{aligned}}                                      \tag{2.3}
\]

and

\[
 \boxed{
 \nu(2m+1)\le
 2\left[W+{H\over2r}G+\Delta_H+L_m(m-H-1)\right].}   \tag{2.4}
\]

#### Proof

By (1.13), the retained cycles contribute

\[
 K(4r+2H)=G+2HK.                                     \tag{2.5}
\]

Append the `u` omitted middle masks once. The base term becomes exactly

\[
                         G+u=W,                       \tag{2.6}
\]

so there is no `Hu` leave charge. Append every missing signed target once,
at cost `Delta_H`. The resulting central word covers every rank in
`[m-H,m+H]`.

Append the one product-SCD exterior word of length `L_m(m-H-1)`. It covers
both ranks at most `m-H-1` and ranks at least `m+H+1`. Every certified
witness stays inside one cycle word, singleton, or exterior gadget, so all
concatenation seams cost zero. This proves (2.3).

Apply the trimmed one-coordinate lift to the complete even word. If its
length is `N`, the lift

\[
 Q_1,\ldots,Q_N,\{z\},Q_1\cup\{z\},\ldots,Q_{N-1}\cup\{z\}
                                                               \tag{2.7}
\]

has exactly `2N` letters and is universal. This proves (2.4).
\(\square\)

With

\[
 W_o=\binom{2m+1}m=2W-{W\over m+1},                 \tag{2.8}
\]

the exact odd excess form is

\[
 \nu(2m+1)-W_o
 \le {W\over m+1}+{H\over r}G+2\Delta_H
       +2L_m(m-H-1).                                 \tag{2.9}
\]

There is no extra odd collar or `+1` term. Lifting the whole word also
automatically supplies the two boundary half-layers which the lifted
central piece alone would miss.

## 3. What the local trace theorem must actually prove

Fix an even-time coarse start and write its successive coarse directions as

\[
                         i_0,i_1,i_2,\ldots .          \tag{3.1}
\]

A physical coarse move expands as `b_(i_j),a_(i_j)`. Every cyclic physical
window belongs to one of four classes:

\[
\begin{array}{c|c|c|c}
\text{class}&\text{start}&\text{length}&\text{pair inventory}\\ \hline
A&\text{even}&2d&i_0,\ldots,i_{d-1}\text{ complete}\\
B&\text{even}&2d+1&i_0,\ldots,i_{d-1}\text{ complete; terminal }b_{i_d}\\
C&\text{odd}&2d+1&\text{initial }a_{i_0};
                  i_1,\ldots,i_d\text{ complete}\\
D&\text{odd}&2d&\text{initial }a_{i_0};
                  i_1,\ldots,i_{d-1}\text{ complete; terminal }b_{i_d}.
\end{array}                                           \tag{3.2}
\]

Class `A` is the aligned code displayed in the paired-order theorem:

\[
 \mathcal C_d(p,x)=
 \bigl(J_{p,d}(x),x|_{J^c},p|_{J^c}\bigr),
 \qquad J=\{i_0,\ldots,i_{d-1}\}.                   \tag{3.3}
\]

Classes `B` and `C` each have one partial boundary pair. Class `D` has two
partial boundary pairs and is not literally one of the two one-boundary
half-step cases. The wording of the current open theorem therefore leaves
`D` unstated. In the intended coordinate-disjoint Johnson embedding,
however, all three unaligned classes reduce to aligned ones by the following
explicit decoder.

### Lemma 3.1 (physical direction decoder and boundary completion)

In a coordinate-disjoint Johnson cube, either signed literal trace identifies
exactly which physical cube directions varied. A varied direction contributes
zero endpoints of its ground-coordinate swap pair to a lower intersection
and both endpoints to an upper union; an untouched direction contributes
exactly one endpoint to either sign. The untouched endpoint also records its
orientation bit.

Consequently an aligned trace determines the code (3.3). Moreover:

* a `B_d` trace can be extended by the missing terminal `a_(i_d)` move to
  an aligned `A_(d+1)` trace;
* a `C_d` trace can be extended backwards by the missing initial
  `b_(i_0)` move to an aligned `A_(d+1)` trace; and
* a `D_d` trace can be extended at both ends by those two missing moves to
  an aligned `A_(d+1)` trace.

For the lower sign, extension deletes the currently recorded endpoint of
each newly varied swap pair. For the upper sign, it adjoins that endpoint's
mate. Thus the extended target is a deterministic function of the original
signed target. Equal unaligned traces therefore give equal aligned extended
traces; aligned injectivity recovers the extended start and hence the
original start.

The four classes have distinct coarse pair-count profiles whenever their
start/length parities differ: `A` has only counts zero or two, `D` has two
count-one boundary pairs, while `B` and `C` have respectively an unpaired
`b`-direction and an unpaired `a`-direction. Hence there is no cross-class
collision. \(\square\)

It follows that, for every physical depth `q<=H<2r`, it is enough to prove
aligned signed trace injectivity through coarse depth

\[
                         D_* =\left\lfloor{H\over2}\right\rfloor+1
                         \le r.                       \tag{3.4}
\]

There is no half-step collar: boundary completion is a proof operation on
targets, not an insertion of letters into the OR word. Without the
coordinate-disjoint direction decoder—or when several local cell labels
can produce the same physical swap-pair profile—the unaligned classes must
instead be included explicitly in the local collision ledger.

The same implication is quantitative, but initially only inside one packet
or cell carrying one fixed, target-decodable swap-pair frame.  Fix such a
packet `P`.  Let `E_(P,d)^pm` be the aligned depth-`d` collision excess on
its even-start shore, and let `Exc_(P,q)^pm` be the collision excess over
both physical start parities in `P` at depth `q`.  The variation patterns
of the relevant classes are disjoint, and refinement by deterministic
boundary completion cannot increase image size.  Hence

\[
 E_{P,d}^{\pm}={|P|\over2}
 -\left|\operatorname {Im}\tau_{P,2d,A}^{\pm}\right|,
 \qquad
 \operatorname {Exc}_{P,q}^{\pm}=|P|
 -\left|\operatorname {Im}\tau_{P,q}^{\pm}\right|.              \tag{3.5a}
\]

Here the subscript `A` means the aligned even-start class.  One has

\[
 \boxed{
 \begin{aligned}
 \operatorname {Exc}_{P,2d}^{\pm}
   &\le E_{P,d}^{\pm}+E_{P,d+1}^{\pm},\\
 \operatorname {Exc}_{P,2d+1}^{\pm}
   &\le 2E_{P,d+1}^{\pm}.
 \end{aligned}}                                                    \tag{3.5}
\]

Thus aggregate aligned collision excess `o` of the local owner mass through
depth `D_*`, summed over decoder packets, transfers to the corresponding
sum of packetwise physical collision excesses through `H`.  This is the
exact approximate-code interface.  It does not control repetitions between
different packets.  If a larger packet contains several local frames whose
labels can be erased by completed pairs, collisions between those frames
must also be added to `Gamma`; (3.5) does not reclassify them as `Omega`.

Failure of any code does not change (2.3); it merely increases the actual
hole ledger. A proposed proof of `Delta_H=o(W)` must use one simultaneous
factor choice and sum over all depths and both signs.

### 3.1 Exact local/outer duplicate identity

Let `P` range over the retained first-eligible packets and let

\[
 I_{P,q}^{\pm}=\operatorname{Im}\tau_{P,q}^{\pm},
 \qquad
 \gamma_{P,q}^{\pm}=|P|-|I_{P,q}^{\pm}|.             \tag{3.6}
\]

Put

\[
 \Gamma_q^\pm=\sum_P\gamma_{P,q}^\pm,
 \qquad
 \Omega_q^\pm=
 \sum_P|I_{P,q}^\pm|-\left|\bigcup_PI_{P,q}^\pm\right|.          \tag{3.7}
\]

Here `Gamma` is all within-packet collision loss and `Omega` is overlap
between different packet images. Since the total owner occurrence mass is
`G`, one has the exact identity

\[
 \boxed{
 M_q^\pm=N_q-G+\Gamma_q^\pm+\Omega_q^\pm,
 \qquad N_q=\binom{2m}{m-q}.}                        \tag{3.8}
\]

Indeed, the global image size is

\[
 G-\Gamma_q^\pm-\Omega_q^\pm,
\]

and subtracting it from `N_q` proves (3.8).

Thus local trace injectivity only makes `Gamma_q^pm=0`; it does not control
`Omega_q^pm`. Also, when `G>N_q`, at least `G-N_q` repetitions are forced,
so raw global duplicate mass is not expected to be `o(W)`. The exact outer
target is the actual deficit

\[
 \boxed{
 \sum_{q=1}^H\sum_{\pm}
 \left(N_q-\left|\bigcup_PI_{P,q}^\pm\right|\right)=o(W).}        \tag{3.9}
\]

All depths and both signs must use the same selected paired factor in each
packet. Separate depthwise solutions do not define one successor
permutation.

For the direct first-eligible `B_4` SCD packet, one packet is itself the
whole `Q_(2r)`, so the decoder above is packet-wide. If the paired lift is
installed separately in many `Q_(2r)` cells inside a larger multi-shore
packet, completed pairs can erase the old cell label. Such cross-cell
collisions belong in `Gamma`, not automatically in the outer term `Omega`.

## 4. Quantitative plug-in at the constant-one scale

The preceding compiler has the right asymptotics with the canonical
first-eligible packet parameters.  This statement is conditional only on
the trace/outer-hole gate; no further geometric interface is hidden in it.

### Theorem 4.1 (asymptotic paired-order plug-in)

Let `r=r(m)` be a power of two satisfying

\[
                         {m\over32}<r\le {m\over16},              \tag{4.1}
\]

and put

\[
                         H=\left\lceil\sqrt{m\log m}\right\rceil. \tag{4.2}
\]

Suppose the retained first-eligible packets have owner-disjoint mass

\[
                         G=W-e^{-\Omega(m)}W,                     \tag{4.3}
\]

and admit one parity-complete paired-order factor whose actual aggregate
signed deficit satisfies `Delta_H=o(W)`.  Then

\[
                         \nu(2m)=(1+o(1))W                       \tag{4.4}
\]

and

\[
 \nu(2m+1)=(1+o(1))\binom{2m+1}m.                               \tag{4.5}
\]

#### Proof

The largest power of two not exceeding `m/16` satisfies (4.1), for all
sufficiently large `m`.  Equations (4.1)--(4.2) give

\[
 {H\over r}=O\!\left(\sqrt{{\log m\over m}}\right)=o(1),
 \qquad H<2r.                                                     \tag{4.6}
\]

The factor-blind product-tail estimate is

\[
 {L_m(m-H-1)\over W}
 \le C_0\exp\!\left(-{H^2\over8m}\right)
 \le C_0m^{-1/8}.                                                \tag{4.7}
\]

Substitution in (2.3) proves the upper half of (4.4).  The middle-layer
endpoint injection gives the matching lower bound.  Equation (2.9),
together with `W/(m+1)=o(W)`, gives (4.5).  \(\square\)

The hypothesis in Theorem 4.1 is exactly (3.9) after all intrapacket and
interpacket collisions are combined.  It is not supplied merely by solving
the pointwise complete-mapping equations below.

## 5. Complete mappings as two exact systems, and the direct SCD attempts

For fixed `x`, parity completeness says that the edges

\[
 \left\{\{p,p\oplus e_{d_p(x)}\}:p\in Q_r^{\rm even}\right\}    \tag{5.1}
\]

form a perfect matching of `Q_r`.  Equivalently, for every odd `o`,

\[
 \boxed{
 \sum_{i=1}^r
  \mathbf{1}\{d_{o\oplus e_i}(x)=i\}=1.}                       \tag{5.2}
\]

For a fixed even `p`, the row map `F_p` is a permutation exactly when,
for every `y`,

\[
 \boxed{
 \sum_{i=1}^r
  \mathbf{1}\{d_p(y\oplus e_i)=i\}=1.}                         \tag{5.3}
\]

These are the row and column equations of the required integral
three-index array.

### Theorem 5.1 (universal shifted-prefix complete mapping)

Let

\[
                         G(y)=y\oplus e_{\delta(y)}               \tag{5.4}
\]

be any neighbor permutation of `Q_r`.  Define, for every even `p`,

\[
 \boxed{d_p(x)=\delta(p\oplus x).}                               \tag{5.5}
\]

Then every `F_p` is conjugate to `G`, and every `T_x` is a parity-shore
bijection.  Explicitly,

\[
 p\oplus F_p(x)=G(p\oplus x),
 \qquad
 T_x(p)\oplus x=G(p\oplus x).                                   \tag{5.6}
\]

#### Proof

Both identities follow by substituting (5.5).  The affine map
`x -> p xor x` conjugates `F_p` to `G`; for fixed `x`, the affine map
`p -> p xor x` conjugates `T_x` between the two parity shores to `G`.
Thus (5.2)--(5.3) hold.  \(\square\)

This is a genuine prefix construction: any cyclic factor obtained by
stitching SCD rows may be used as `G`.  It nevertheless fails the trace
gate maximally.

### Theorem 5.2 (diagonal trace kernel)

Let `d>=1`, and let an aligned window in (5.5) complete the distinct coarse
directions `J`, with `|J|=d`.  For every even vector `z` supported on `J`,

\[
                         (p,x)\longmapsto(p\oplus z,x\oplus z)   \tag{5.7}
\]

preserves the entire signed literal trace.  Hence every nonempty aligned
trace fibre has size at least

\[
                              2^{d-1}.                            \tag{5.8}
\]

#### Proof

The quantity `p xor x`, and therefore the whole `G`-trajectory and its
direction support `J`, is unchanged by (5.7).  Outside `J`, both `p` and
`x` are unchanged.  On `J`, both physical directions of every completed
coarse pair have varied, so the signed trace records no initial orientation.
Finally, even `z` preserves the requirement that `p` be even.  There are
exactly `2^(d-1)` such vectors.  \(\square\)

There is also a sharp obstruction to interpreting an ordinary SCD itself
as the long cyclic row factor.  A symmetric chain beginning at rank `k`
has

\[
                              r-2k+1                              \tag{5.9}
\]

vertices.  When `r` is even every such number is odd, so chain-internal
edges cannot even give a perfect matching.  More generally, the union of
the disjoint SCD paths is a forest; a neighbor permutation supported only
on its edges can have only directed two-cycles, because a longer directed
cycle would create an undirected cycle in that forest.  For odd `r`, the
chains have even order and pairing consecutive vertices does give an
SCD-derived neighbor involution, but it still has only `C_2` rows.

This short-cycle issue cannot be avoided at the relevant exact-factor
sizes.  A `C_(2r)`-factor of `Q_r` requires

\[
                              2r\mid2^r,                            \tag{5.10}
\]

so every nontrivial admissible `r` is a power of two and hence even.  A
literal unstitched SCD is therefore not a candidate for item 1 of the local
trace theorem.

For completeness, an SCD has

\[
                    \binom r{\lfloor r/2\rfloor}                 \tag{5.11}
\]

chains.  Distinguished forward prefixes of length `H` fail only within
`H` positions of a chain endpoint, so the crude endpoint count is at most

\[
 2H\binom r{\lfloor r/2\rfloor}
 =O\!\left({H\over\sqrt r}2^r\right).                            \tag{5.12}
\]

This is useful only for `H=o(sqrt(r))`; the constant-one endgame needs
`H/sqrt(m)->infinity` with `r=Theta(m)`.  Consequently a successful SCD
realization must genuinely stitch the rows into cyclic rotors.  Theorem
5.2 then shows that using the same shifted rotor on every context is still
insufficient.

## 6. Twisted affine factors: exact trace criterion

Let `S` permute the `r` coordinates, and suppose

\[
 G_0(y)=y\oplus e_{\delta_0(y)},
 \qquad
 G_1(y)=y\oplus e_{S\delta_0(y)}                    \tag{6.1}
\]

are both neighbor permutations.  Then

\[
                         d_p(x)=\delta_0(Sp\oplus x)              \tag{6.2}
\]

solves (5.2)--(5.3): `F_p` is conjugate to `G_0`, while `T_x` is
conjugate to `G_1`.

Writing `D_i=delta_0^{-1}(i)`, the two permutation requirements in (6.1)
are exactly that both translated families

\[
             \{D_i\oplus e_i:i\in[r]\},
 \qquad
             \{D_i\oplus e_{Si}:i\in[r]\}                       \tag{6.3}
\]

partition `Q_r`.  An SCD rotor supplies only the first partition; the
second is the extra twisted-complete-mapping condition.

For a coarse depth `d`, let `J_d(y)` be the direction support of the first
`d` steps of `G_0` from `y`, and put

\[
                         Y_J=\{y:J_d(y)=J\}.                       \tag{6.4}
\]

### Theorem 6.1 (full affine aligned-collision criterion)

Two aligned starts with the same support `J` collide if and only if there
are `y,y' in Y_J`, an even vector `e`, and a vector `z` such that

\[
 \operatorname{supp}e\subseteq J,qquad
 \operatorname{supp}z\subseteq J,qquad
                         y\oplus y'=z\oplus Se.                  \tag{6.5}
\]

In particular, the fixed-`y` subkernel has size at least

\[
 \boxed{
 2^{\max\{|J\cap S^{-1}J|-1,0\}}.}                              \tag{6.6}
\]

#### Proof

Let `e=p xor p'`.  Equality of the two codes outside `J` says exactly
that `e` is even and supported on `J`, and that `z=x xor x'` is supported
on `J`.  Since `y=Sp xor x`,

\[
                         y\oplus y'=Se\oplus z,                  \tag{6.7}
\]

which proves necessity.  Reversing these implications proves sufficiency,
because a completed pair erases every orientation bit on `J`.

For `y=y'`, equation (6.7) permits every even `e` supported on
`J cap S^(-1)J`, with `z=Se`.  The space of even vectors on a nonempty
set of size `c` has dimension `c-1`; for `c=0` it contains only zero.
This proves (6.6).  \(\square\)

Thus `|J cap S^(-1)J|<=1` for every protected prefix is necessary but not
sufficient.  Even when this fixed-point kernel vanishes, different fibres
`Y_J` may collide through (6.5).  The exact surviving target is the
following quantified punctured-prefix condition:

\[
 \boxed{
 \begin{gathered}
 y,y'\in Y_J,\quad |e|\equiv0\pmod2,\quad
 \operatorname{supp}e,\operatorname{supp}z\subseteq J,\\
 y\oplus y'=z\oplus Se
 \quad\Longrightarrow\quad
 y=y',\ e=0,\ z=0.
 \end{gathered}}                                                   \tag{6.8}
\]

Equivalently, one must impose both the fixed-fibre condition
`|J cap S^(-1)J|<=1` and disjointness of the nonzero difference set
`(Y_J xor Y_J)\{0}` from the right-hand family in (6.5).  Merely writing
that the two unpunctured sets intersect in `{0}` would be insufficient,
because a nonzero fixed-`y` kernel also represents the zero difference.

The saved common-phase `Q_4` seed with `S=(2 4)` fails already in the
fixed-`y` subkernel.  At depth three take, for example,

\[
 J=\{1,2,3\},\qquad S^{-1}J=\{1,3,4\}.                           \tag{6.9}
\]

Then `e=e_1 xor e_3` is a nonzero kernel vector.  Hence that exact
complete-mapping seed is not a local trace-code seed through physical
depth six.  The full audited fibres are even larger; (6.9) alone is enough
to refute injectivity.

### Lemma 6.2 (even-orbit obstruction for a coset common phase)

Suppose a doubled-permutation `C_(2r)` factor has all `2r` phase classes
of the form

\[
                         P_j\oplus K,\qquad j\in\mathbb Z_{2r},  \tag{6.10}
\]

for one subgroup `K`, where `P_j` is the length-`j` prefix of the word
`pi pi`.  Suppose also that its `S`-twist advances the same phase classes.
Then

\[
                         e_i\oplus e_{Si}\in K                    \tag{6.11}
\]

for every coordinate `i`.  Consequently `S` must have an odd orbit.  In
particular, no fixed-point-free involution `S` can occur in such a coset
common-phase pair.

#### Proof

At the phase whose outgoing untwisted direction is `i`, both adding `e_i`
and adding `e_(Si)` reach the same next coset.  Their difference lies in
`K`, proving (6.11).  In the quotient by `K`, all coordinate vectors on
one `S`-orbit are therefore equal.  If every orbit has even size, their
sum is zero, so

\[
                         \bigoplus_{i=1}^r e_i=P_r\in K.          \tag{6.12}
\]

But then the half-cycle phase `P_r xor K` equals the initial phase `K`,
contradicting the assumed `2r` distinct phase classes.  \(\square\)

Thus the tempting antipodal choice of `S`, which would separate every
short prefix from its image, cannot be combined with the simplest linear
coset phase factor.  A successful factor must have an odd `S`-orbit or a
noncoset, state-dependent phase refinement.

There is a small algebraic near-miss showing that the fixed-`y` condition
is not intrinsically impossible.  In `Q_4`, let

\[
 L=\langle e_2\oplus e_4,e_1\oplus e_3\rangle,
\]

and let `delta_0=i` respectively on

\[
 L,\quad e_1\oplus L,\quad e_1\oplus e_2\oplus L,\quad
 e_1\oplus e_2\oplus e_3\oplus L.                               \tag{6.13}
\]

Then `G_0` advances these four cosets in order with word `1234 1234`.
For `S=(1 3)(2 4)`, the map `G_1` advances the same cosets with word
`3412 3412`; indeed the four translated cosets are successively the next
ones.  Therefore (6.2) is an exact nonconstant complete mapping.  Every
cyclic prefix of `1234` of length at most two is disjoint from its
`S`-image, so (6.6) is trivial through depth two.  The full condition
(6.8), and any growing version, remain unproved; this finite example is
not claimed as a trace factor.

## 7. A non-diagonal SCD/rotor recursion, and its Gaussian trace obstruction

The twisted equations do admit a clean prefix recursion.  It is stronger
than the diagonal construction of Theorem 5.1, but still fails
quantitatively at the endgame scale.

### Theorem 7.1 (block-alternating double-factor recursion)

Let `G` be a `C_(2s)`-factor of `Q_s`, every cycle having a
doubled-permutation direction word, and let `delta` be its direction
function.  On \(Q_s^A\times Q_s^B\), write a vertex as `(u,v)` and define

\[
 \delta_0(u,v)=
 \begin{cases}
 A\delta(u),&|u|+|v|\equiv0\pmod2,\\
 B\delta(v),&|u|+|v|\equiv1\pmod2.
 \end{cases}                                                       \tag{7.1}
\]

Let `G_0(y)=y xor e_(delta_0(y))`, and let `S` exchange the `A` and `B`
coordinate blocks.  Then:

1. `G_0` is a `C_(4s)`-factor of `Q_(2s)`, and every cycle has a
   doubled-permutation direction word on the `2s` coordinates;
2. `G_1(y)=y xor e_(S delta_0(y))` is a neighbor permutation; and
3. the affine rule (6.2), now with coarse dimension `r=2s`, satisfies
   every parity complete-mapping equation and has `C_(2r)` rows.

#### Proof

Starting at even total parity, successive `G_0` moves update `u` by `G`,
then `v` by `G`, and repeat.  Thus

\[
                         G_0^2(u,v)=(G(u),G(v)).                  \tag{7.2}
\]

Both coordinates first return after `2s` applications of `G`, so the
`G_0` cycle has length `4s`.  In any `s` consecutive steps of a base
doubled-permutation word, every base direction occurs once, and the next
`s` directions repeat in the same order.  Interleaving the `A` and `B`
words therefore gives one permutation of all `2s` directions followed by
the same permutation.  Odd total parity gives the same argument with the
two blocks interchanged.

For `G_1`, an even source updates `v` in the direction determined by its
unchanged `u`.  Hence an odd target has the unique predecessor obtained by
reversing that same `v`-edge.  An odd source similarly updates `u` in the
direction determined by its unchanged `v`, so every even target also has
a unique predecessor.  Thus `G_1` is a permutation.  The affine theorem
of Section 6 proves item 3.  \(\square\)

Starting with the unique `C_2` factor on `Q_1` and iterating Theorem 7.1
gives an explicit solution for every `r=2^t`.  Label the `r` coordinates by
binary words of length `t`.  The resulting direction function is a rooted
prefix descent: at a binary coordinate node, descend to its left child when
the parity of the current subtree word is even and to its right child when
it is odd.  For the paired ownership code, perform this descent on
`Sp xor x`, where `S` flips the first address bit.  This is an exact
prefix-derived `d_p(x)`, not an existence-by-matching argument.

This construction can take a stitched cyclic SCD rotor as its base.  Its
prefix supports nevertheless force too many fixed-`y` trace collisions.

### Theorem 7.2 (aggregate square-root obstruction for the recursion)

Let `N=2^(2r-1)` be the number of aligned even-context starts in the
coarse paired system supplied by Theorem 7.1, where `r=2s`.  Let `E_d` be
the aligned trace collision excess at coarse depth `d`, for either sign.
For every `1<=t<=s`,

\[
 \boxed{E_{2t}\ge {t\over2s}N.}                                  \tag{7.3}
\]

Consequently, for every `T<=s`,

\[
 \boxed{
 \sum_{t=1}^T E_{2t}
 \ge {T(T+1)\over4s}N.}                                         \tag{7.4}
\]

In particular, aligned control through depth `D` cannot have aggregate
collision excess `o(N)` when `D/sqrt(r)` is bounded away from zero, and
fails by an unbounded factor when `D/sqrt(r)->infinity`.

#### Proof

For a base state `w`, let `P_t(w)` be the set of the first `t` directions
of its `G`-trajectory.  At depth `2t`, (7.1) gives

\[
 J=A P_t(u)\ \dot\cup\ B P_t(v),
\quad
 J\cap S^{-1}J=
 A(P_t(u)\cap P_t(v))\ \dot\cup\
 B(P_t(u)\cap P_t(v)).                                         \tag{7.5}
\]

For uniform `w`, each coordinate belongs to `P_t(w)` with probability
exactly `t/s`: on every `2s`-cycle its two occurrences lie in exactly
`2t` of the cyclic length-`t` windows.  For independent uniform `u,v`, if

\[
                         C=|P_t(u)\cap P_t(v)|,                  \tag{7.6}
\]

then

\[
                         \mathbb EC={t^2\over s}.                 \tag{7.7}
\]

Since `C<=t`,

\[
                         \Pr(C>0)\ge {t\over s}.                  \tag{7.8}
\]

Whenever `C>0`, (7.5)--(6.6) give a nonzero even fixed-`y` kernel.  For
that `y=(u,v)`, the kernel acts freely on all `2^(r-1)` even choices of
`p`, so at most half as many distinct traces remain.  The affine variable
`y=Sp xor x` is uniform, with exactly `2^(r-1)` aligned starts above every
`y`.  Summing the within-`y` collision excess, and observing that collisions
between different `y` can only increase it, proves (7.3).  Summation gives
(7.4).  \(\square\)

At the constant-one choice `r=Theta(m)` and
`H/sqrt(m)->infinity`, the required aligned depth is
`D_*=floor(H/2)+1`; taking `T=floor(D_*/2)` in (7.4) gives

\[
 {1\over N}\sum_{d\le D_*}E_d
                         =\Omega\!\left({H^2\over r}\right),    \tag{7.9}
\]

which is not `o(1)`.  Thus this natural non-diagonal SCD/rotor recursion
solves exact ownership and long cycles but definitively does not solve the
required low-loss local trace theorem.

This is a no-go for the strong labelled/local-code route, not an actual-hole
lower bound for the resulting global factor.  At ranks `m-q` and `m+q`, the owner
mass can exceed `N_q`, so some trace repetitions are unavoidable and can in
principle be absorbed without creating a missing target.  Ruling out that
possibility would require inserting the excess from (7.4) into the exact
identity (3.8), with the forced term `G-N_q` and all outer overlaps retained.
No such global obstruction is claimed here.

## 8. Exact proved/conditional boundary

The following implication is proved without qualification:

> A cyclic parity-complete paired-order factor with physical delay `H`,
> aligned signed trace control through `floor(H/2)+1`, and actual aggregate
> target deficit `Delta_H=o(W)` enters the factor-blind central/tail compiler
> with exactly `2H` letters per physical cycle and no other collar.  With
> `r=Theta(m)` and `sqrt(m)<<H<<r`, it yields the constant-one theorem in
> both parities.

The following construction results are also exact.

* The shifted SCD/rotor rule (5.5) solves every complete-mapping equation,
  but has trace multiplicity `2^(d-1)`.
* The affine double-factor rule is governed exactly by (6.3) and the full
  trace criterion (6.5)--(6.8).
* The block-alternating recursion of Theorem 7.1 gives long rows and exact
  complete mappings, but Theorem 7.2 rules out its Gaussian low-loss trace
  use.

What remains unproved in the strong trace-code route is a growing twisted
SCD-prefix pair satisfying the punctured condition (6.8) with aggregate
local loss `o(2^(2r))`, together with the outer simultaneous target deficit
(3.9).  Neither condition may be replaced by ordinary SCD transversality,
pointwise parity matching, or separate depthwise choices.  They form a
sufficient labelled route only.  The sole factor-blind compiler gate is the
actual deficit `Delta_H=o(W)`; a future argument could conceivably prove it
by balancing nonzero local collision against the forced global duplicate
mass.  In either formulation there is no additional parity, pair-boundary,
seam, or product-tail gate.

An independent adversarial audit verified the constants in (2.3), (2.9),
the four-class depth indexing, the affine kernel (6.6), the divisibility
obstruction (5.10), and the constants in (7.3)--(7.4).  It also forced the
packetwise scope in (3.5); no global collision-transfer claim is being made
there.
