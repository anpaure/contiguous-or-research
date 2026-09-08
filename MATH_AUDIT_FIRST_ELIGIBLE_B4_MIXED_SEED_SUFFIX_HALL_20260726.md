# Mixed-seed first-eligible `B_4` packets: the suffix Hall cut and the meaning of phase density

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Conclusion

Fix one ordered atlas of four-coordinate blocks.  Consider a
context-stable first-eligible packet construction in which, at each scan
stage, the requested local square may be any one of the three cyclic
`B_4` seed supports.  The seed may depend on all previously frozen data
and may change at every stage.  Let the packet dimension be

\[
                         h=2r,
 \qquad r=o(m),\qquad r\to\infty .                 \tag{0.1}
\]

Assume the retained packet supports partition all but
`exp(-Omega(m)) W` middle owners, and install arbitrary literal cycles
inside the packets.  Then, for every fixed `A>0` and

\[
 q=\lfloor A\sqrt m\rfloor\le \min\{H,r\},          \tag{0.2}
\]

there is a constant `kappa_A>0` such that

\[
 \boxed{
 M_q^-\ge(\kappa_A-o(1))W,
 \qquad
 M_q^+\ge(\kappa_A-o(1))W .}                       \tag{0.3}
\]

Here `M_q^\pm` is the number of physical signed depth-`q` targets not hit
even once.  In particular the balanced Hall/overload defect is also
linear, and its aggregate through `q\le H` is not `o(W)`.

The obstruction is independent of the number of seed changes.  The
layer-balanced hashed three-seed construction may use `Theta(h)`
nonbaseline local seeds on almost every packet, far more than the
necessary scalar rate `Omega(h/sqrt(m))`, and (0.3) still applies.

The exact interpretation of that scalar rate is the following.  For the
Hall cut below, a successful construction needs

\[
 \Omega(W/\sqrt m)
\]

transition sites which physically disturb the designated suffix, or
`Omega(h/sqrt(m))` such sites per `C_{2h}` on average.  A seed change
inside an early four-block is not such a site.  Thus density of local
mixed-frame labels alone is not sufficient.

This refutes the proposed gate for the fixed-block, first-eligible
specialization.  An escape has to change the ambient block order/support
or transport coordinates into the frozen suffix; it cannot consist only
of choosing the three `B_4` seeds more densely.

## 1. The three local supports and a context-stability rigidity lemma

Let the three perfect matchings of `K_4` be `M_0,M_1,M_2`, and put

\[
 \mathcal A_c=\binom{[4]}2\setminus M_c
 \qquad(c=0,1,2).                                  \tag{1.1}
\]

Thus every `\mathcal A_c` is a four-state physical square, and

\[
 |\mathcal A_c\cap\mathcal A_d|=2
 \qquad(c\ne d).                                   \tag{1.2}
\]

At one stage of a sequential scan, freeze all information preceding the
current block.  A deterministic local decision rule is a map

\[
 \psi:2^{[4]}\longrightarrow\{\bot,0,1,2\},         \tag{1.3}
\]

where `psi(S)=c` means that the block is selected with seed `c`, and
`psi(S)=bot` means that it is skipped.

The rule is **packet-stable** when

\[
 \psi(S)=c
 \quad\Longrightarrow\quad
 S\in\mathcal A_c
 \ \hbox{ and }\ 
 \psi(S')=c\quad(S'\in\mathcal A_c).               \tag{1.4}
\]

Condition (1.4) is forced by literal packet ownership: after the block is
selected with seed `c`, its local state is varied through all four members
of `\mathcal A_c`, and neither the selected index nor the seed is allowed
to change.

### Lemma 1.1 (one predictable seed at every scan state)

The image of a packet-stable rule contains at most one member of
`{0,1,2}`.  If the stage is a first-eligible stage, there is therefore a
unique seed `c`, determined before the current block is exposed, and the
block is selected exactly when its local state belongs to
`\mathcal A_c`.

#### Proof

Suppose both `c` and `d`, `c\ne d`, occur in the image.  By (1.4), the
rule is identically `c` on `\mathcal A_c` and identically `d` on
`\mathcal A_d`.  Their intersection is nonempty by (1.2), a
contradiction.  Hence at most one seed can occur.  In a first-eligible
stage one seed is requested, and (1.4) makes its whole support, and only
its support, the success set.  \(\square\)

Consequently the seed may adapt to an anchor and to previously skipped
blocks, but it is predictable with respect to the fresh block.  Under
independent fair coordinate bits its conditional success probability is
always

\[
                         |\mathcal A_c|/16=1/4.       \tag{1.5}
\]

The conclusion does not require a fixed seed word.

## 2. A common frozen suffix

Let

\[
 B_1<\cdots<B_b,
 \qquad b=(1/2+o(1))m,                              \tag{2.1}
\]

be the ordered complete four-blocks; an anchor and the bounded remainder
occupy `o(m)` further coordinates.  Put

\[
 j=\lfloor b/4\rfloor,
 \qquad
 R=\bigcup_{i=b-j+1}^bB_i,
 \qquad
 s=|R|,
 \qquad
 \gamma_m={s\over2m}\longrightarrow {1\over4}.     \tag{2.2}
\]

Call a packet normal when all of its `r` selected blocks precede `R`.

### Lemma 2.1 (uniform localization for arbitrary seed schedules)

The number `U_m` of middle owners which are outside the retained packet
partition or lie in a nonnormal packet satisfies

\[
                         U_m\le e^{-c m}W             \tag{2.3}
\]

for some absolute `c>0` and all sufficiently large `m`.

#### Proof

Condition on the anchor and expose the first `b-j` blocks sequentially.
Lemma 1.1 says that, conditional on the complete past, the next success
probability is `1/4`.  The success count therefore has the binomial law

\[
                    \operatorname {Bin}(b-j,1/4).    \tag{2.4}
\]

Its mean is `(3/32+o(1))m`, whereas `r=o(m)`.  A Chernoff bound gives
probability `e^{-Omega(m)}` of fewer than `r` successes before `R`.
The same estimate covers failure to find `r` successes in the full atlas.

Conditioning the independent bits on middle rank costs at most

\[
 {2^{2m}\over\binom{2m}m}=O(\sqrt m),               \tag{2.5}
\]

which is absorbed by the exponential.  Packet stability makes the
selected list, hence normality, constant throughout a packet.  Adding the
assumed exponentially small owner leave proves (2.3).  \(\square\)

### Lemma 2.2 (suffix conservation)

Every vertex of every literal component contained in a normal packet has
the same restriction to `R`.  Hence for every start `X`, every depth, and
both signs,

\[
 \tau_q^-(X)\cap R=X\cap R,
 \qquad
 \tau_q^+(X)\cap R=X\cap R.                         \tag{2.6}
\]

#### Proof

Every local seed change is confined to a selected four-block.  A normal
packet has no selected block in `R`, and all exterior coordinates are
frozen.  Intersections and unions of consecutive vertices retain this
common restriction.  \(\square\)

Notice that neither the cycle order nor intrapacket injectivity enters
this lemma.

## 3. The exact Hall cut

For an integer `a`, define

\[
\begin{aligned}
 \mathcal Z_{q,a}^-
 &=\{T\in\tbinom{[2m]}{m-q}:|T\cap R|\le a\},\\
 \mathcal Z_{q,a}^+
 &=\{T\in\tbinom{[2m]}{m+q}:|T\cap R|\ge s-a\},     \tag{3.1}
\end{aligned}
\]

and

\[
 B_a=\bigl|\{X\in\tbinom{[2m]}m:|X\cap R|\le a\}\bigr|.
                                                               \tag{3.2}
\]

Middle complementation shows that `B_a` is also the number of middle
owners satisfying `|X cap R| >= s-a`.

### Proposition 3.1 (component Hall inequality)

For every integral exact-owner choice of whole packet components,

\[
 M_q^\pm
 \ge |\mathcal Z_{q,a}^\pm|-B_a-U_m.                \tag{3.3}
\]

The identical inequality is valid for a fractional component cover with
unit total weight at every owner.

#### Proof

For a normal component, (2.6) says that a lower occurrence lands in
`\mathcal Z_{q,a}^-` precisely when its starting owner belongs to the
middle event in (3.2).  Summing one occurrence per owner gives capacity
at most `B_a`.  The same statement above uses the complementary middle
event.  Give every exceptional owner the most favorable possible
occurrence; this adds at most `U_m`.  Repeated occurrences of one target
do not increase the number of distinct targets hit.  This proves (3.3).

For a fractional cover, sum first over components.  At each owner the
component weights total one, so exactly the same owner-side capacity
bound results.  \(\square\)

## 4. Evaluation at Gaussian depth

Fix `A>0`, take `q=floor(A sqrt(m))`, and put

\[
                         v={3\over32}.                \tag{4.1}
\]

For a fixed `x>0`, set

\[
 a_m=\left\lfloor {s\over2}-x\sqrt{vm}\right\rfloor.       \tag{4.2}
\]

The exact cardinalities are

\[
\begin{aligned}
 B_{a_m}
 &=\sum_{t\le a_m}\binom st\binom{2m-s}{m-t},\\
 |\mathcal Z_{q,a_m}^-|
 &=\sum_{t\le a_m}\binom st\binom{2m-s}{m-q-t}.    \tag{4.3}
\end{aligned}
\]

Also `|\mathcal Z_{q,a_m}^+|=|\mathcal Z_{q,a_m}^-|` by
complementation.  Stirling's formula, equivalently the elementary
hypergeometric central limit theorem, gives

\[
\begin{aligned}
 {B_{a_m}\over W}&\longrightarrow\Phi(-x),\\
 {|\mathcal Z_{q,a_m}^\pm|\over W}
 &\longrightarrow e^{-A^2}\Phi(d-x),
 \qquad d=A\sqrt{2/3}.                              \tag{4.4}
\end{aligned}
\]

Indeed, the middle suffix mean is `s/2`, the lower suffix mean is
`s/2-(A/4+o(1))sqrt(m)`, and both variances are `(v+o(1))m`; the upper
calculation is complementary.  Moreover

\[
 {\binom{2m}{m-q}\over\binom{2m}m}\longrightarrow e^{-A^2}. \tag{4.5}
\]

There exists `x=x_A` for which

\[
 e^{-A^2}\Phi(d-x)>\Phi(-x).                        \tag{4.6}
\]

To see this, let `x>d` tend to infinity and use Mills' ratio:

\[
 {\Phi(d-x)\over\Phi(-x)}
 ={x\over x-d}
   \exp\{xd-d^2/2+o(1)\}\longrightarrow\infty.     \tag{4.7}
\]

Fix such an `x_A` and define

\[
 \kappa_A=e^{-A^2}\Phi(d-x_A)-\Phi(-x_A)>0.         \tag{4.8}
\]

Equations (2.3), (3.3), and (4.4) prove (0.3).

## 5. Exceptional windows and the sharp meaning of the density bound

The preceding cut has a useful form which does not assume a packet
construction.  For an arbitrary exact middle cycle factor, call a
depth-`q` start **`R`-exceptional** when its `q+1` consecutive middle
vertices do not all have the same restriction to `R`.  Let `E_{R,q}` be
the number of such starts.

### Proposition 5.1 (exceptional-window inequality)

For the threshold chosen in Section 4,

\[
 \boxed{
 M_q^-\ge(\kappa_A-o(1))W-E_{R,q},
 \qquad
 M_q^+\ge(\kappa_A-o(1))W-E_{R,q}.}                 \tag{5.1}
\]

If `T_R` is the number of transition positions whose endpoints have
different restrictions to `R`, then

\[
                         E_{R,q}\le qT_R.            \tag{5.2}
\]

#### Proof

Delete the `R`-exceptional starts.  Every remaining start obeys the same
owner-event identity used in Proposition 3.1, so its capacity in the cut
is at most `B_a`.  Restoring one deleted start can hit at most one new
target of either sign, proving (5.1).

Every exceptional `q`-window contains a transition which changes the
`R`-restriction.  A fixed transition belongs to exactly `q` cyclic
windows of `q` transitions.  The union bound proves (5.2).  \(\square\)

Suppose the factor has

\[
 |\mathcal F|={W\over2h}+o(W/h)                     \tag{5.3}
\]

cycles.  If either signed defect in (5.1) is `o(W)`, then

\[
 T_R\ge(\kappa_A-o(1)){W\over q}
       =\Omega(W/\sqrt m),                          \tag{5.4}
\]

and hence

\[
 {T_R\over|\mathcal F|}=\Omega(h/\sqrt m).          \tag{5.5}
\]

This proves necessity, not sufficiency.  It is crucial that `T_R` counts
physical suffix-disturbing transitions.  Three-seed changes inside the
same early active blocks contribute zero to `T_R`, no matter how many are
made.  By Lemma 2.1 the first-eligible factor has

\[
                         E_{R,q}\le U_m=o(W),         \tag{5.6}
\]

so it fails (5.1) even if its internal seed-switch density is maximal.

## 6. Concrete application to the hashed three-seed atlas

In the hashed construction, an anchor assigns a word

\[
                         \theta\in\{0,1,2\}^r,       \tag{6.1}
\]

and the scan requests `\mathcal A_{\theta_j}` at stage `j`.  This is
exactly the predictable class of Lemma 1.1.  Its packet supports are
owner-disjoint, every packet is a `Q_{2r}`, and the recursive factor is
two-sided trace-injective through depth `r`.

The layer-balanced anchor makes `theta` exponentially close to uniform
in owner mass.  Therefore, relative to any fixed baseline seed, all but
`e^{-Omega(r)}W` owner mass has at least `r/2` nonbaseline entries, by a
binomial Chernoff bound.  Thus the construction has `Theta(r)=Theta(h)`
mixed-seed activity on almost every packet.  Nevertheless (0.3) applies,
because all but `e^{-Omega(m)}W` packets complete their scan before `R`.

This gives an explicit exact-owner, intrapacket-rainbow example showing
that the scalar density requirement (5.5) cannot be replaced by a count
of local seed labels.

### 6.1 The completed 24-owner common carrier

The same argument applies to the genuine common-owner completion of the
three seeds.  One completed carrier uses eight coordinates and has local
owner set

\[
 \mathcal V=\binom{[4]}2\mathbin\square Q_2,
 \qquad |\mathcal V|=24.                            \tag{6.2}
\]

Each of its three seed resolutions is an exact factor of the same 24
owners into six physical `C_4`'s.  Tensoring `r` carriers gives the common
support `\mathcal V^r`; every seed field resolves it into `6^r` physical
`Q_{2r}` cells, so exact owner preservation and dense seed choice are both
available.

This completion does not alter the suffix argument.  Under independent
fair bits an eight-block is `\mathcal V`-eligible with probability

\[
                         {24\over2^8}={3\over32}.     \tag{6.3}
\]

There are `b=(1/4+o(1))m` complete eight-blocks.  Before their terminal
quarter, the expected number of eligible blocks is

\[
 {3\over4}b\,{3\over32}
 =\left({9\over512}+o(1)\right)m.                  \tag{6.4}
\]

Thus the first `r=o(m)` eligible carriers again precede the terminal
quarter except on `e^{-Omega(m)}W` middle owners.  That quarter still
contains `s=(1/2+o(1))m` physical coordinates, so the hypergeometric
calculation (4.4) is unchanged.  Every one of the `6^r` cells and every
completed seed trade in a normal packet freezes the suffix.  Hence (0.3)
holds for the exact 24-owner common-support construction as well.

Equivalently, the inseparable antipodal completion is block diagonal with
respect to the projection \(X\mapsto X\cap R\): every owner component of
the three-way overlay lies in one `R`-fibre.  Passing from raw four-owner
seed cells to their 24-owner completed quartets therefore resolves the
local owner equation but leaves the Hall support function in (3.3)
unchanged.

## 7. Audit correction for the enlarged cross-seed packet menu

There is one scope issue in the earlier frozen-suffix proof.  If a
component associated with an original seed packet is allowed to use a
different seed support, some of its vertices need not be owners of that
original packet.  Therefore the contribution of components associated
with nonnormal packets is not bounded literally by the number `U_m` of
nonnormal original owners.

The conclusion survives in the mesoscopic range, with the following
correct envelope bound.  An original packet has `4^r` owners.  Across all
independent choices of the three seed supports on its `r` active blocks,
the union of possible owner states has size at most

\[
                         6^r.                        \tag{7.1}
\]

If `U_m^{bad}` original owners lie in nonnormal packets, the union of all
cross-seed component vertices associated with those packets has size at
most

\[
 {U_m^{bad}\over4^r}6^r
 =\left({3\over2}\right)^rU_m^{bad}.                \tag{7.2}
\]

For one whole seed choice per packet the sharper multiplier is at most
three.  Under `r=o(m)` and `U_m^{bad}\le e^{-cm}W`, (7.2) is still
`e^{-Omega(m)}W`.  In a fractional exact owner cover, the total weight of
bad-associated occurrences is at most the size of this union, because
the total component weight at each owner is one.

Thus Proposition 3.1 remains valid for the enlarged menu after replacing
`U_m` by

\[
 U_m^{leave}+\left({3\over2}\right)^rU_m^{bad}
 =e^{-\Omega(m)}W.                                  \tag{7.3}
\]

The uncorrected bound by `U_m` itself is not justified for owner-importing
cross-seed components.

## 8. Exact boundary

The proved no-go covers every fixed ordered block atlas in which:

1. packet stages are genuinely first-eligible and context-stable;
2. local alternatives are the three `B_4` seed squares on the currently
   scanned block;
3. complete components remain inside their packet active coordinates; and
4. `r=o(m)`.

It is insensitive to exact owner rounding, fractional mixing, local
orientation, recursive order, intrapacket shadow injectivity, and the
number of internal seed changes.

It does not rule out a construction that uses many ambient block orders,
or a nonlocal owner trade whose components physically move through every
positive-density coordinate suffix.  Such a construction must prove the
hereditary version of (5.4), not merely the scalar count (5.5).
