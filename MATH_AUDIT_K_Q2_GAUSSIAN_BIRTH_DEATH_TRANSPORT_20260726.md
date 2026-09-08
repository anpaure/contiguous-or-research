# Exact Gaussian pair-type transport and the two-layer Q2 gate

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, solver, or
web input is used.

## 0. Verdict

Put

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
 \qquad N_j=\binom{2m+1}{m-j}.
\tag{0.1}
\]

Relative to a fixed pairing of the first \(2m\) coordinates, a rank
\(m-j\) set has type \((\varepsilon,f)\), where \(\varepsilon\) records
the unpaired coordinate and \(f\) is the number of full pairs.  There are
three distinct conclusions.

1. The complete target type laws are joined by an exact, coherent
   pure-death chain.  From rank \(m-j\),

   \[
   (\varepsilon,f)\longmapsto(\varepsilon,f-1)
       \quad\hbox{with probability }{2f\over m-j},
   \tag{0.2}
   \]

   and, when \(\varepsilon=1\),

   \[
   (1,f)\longmapsto(0,f)
       \quad\hbox{with probability }{1\over m-j}.
   \tag{0.3}
   \]

   The remaining probability is a hold.  This chain is realized by a
   uniform nested deletion ordering, so one process gives the correct
   marginal at every \(j\) simultaneously.  Its pair-type transport
   demand in step \(j\) is exactly

   \[
     {m-j-1\over2m+1}\,W=(1/2+o(1))W,                 \tag{0.4}
   \]

   while the total unpaired-coordinate demand through
   \(j\le A\sqrt m\) is only \(O_A(W/\sqrt m)\).

2. An unbiased coordinate recoupling is the wrong operator.  Conditional
   on \(\varepsilon\), its exact birth and death probabilities are

   \[
   b_{j,\varepsilon}(f)
    ={\binom{m-j-\varepsilon-2f}{2}
       \over2\binom m2},
   \qquad
   d_{j,\varepsilon}(f)
    ={f(f+j+\varepsilon)\over\binom m2}.              \tag{0.5}
   \]

   Its linear relaxation eigenvalue is

   \[
        1-\gamma_m,
        \qquad
        \gamma_m={2m-1\over m(m-1)}.                 \tag{0.6}
   \]

   Hence its relaxation time is \(\Theta(m)\), and
   \(O(\sqrt m)\) unbiased recouplings do not move the Gaussian centre.
   At \(j=A\sqrt m+O(1)\), their output stays a positive total-variation
   distance from the target law.

3. The exact signed Q2 packet has the orbit-ledger move

   \[
       16e_{f-1}+8e_f\longmapsto24e_{f-1}.            \tag{0.7}
   \]

   Thus one fully exposed packet layer moves only one third of its active
   occurrences down one type.  A one-seed tensor layer consequently has
   an all-depth drift ceiling \(j/3\), whereas the exact target centre has
   moved \(j/2+O_A(1)\).  One Q2 tensor seed is therefore closed at
   Gaussian depth.

   Two fresh signed exposures have maximum death probability

   \[
                 1-(2/3)^2=5/9,                     \tag{0.8}
   \]

   and the required probability \(2f/(m-j)=1/2+o(1)\) lies strictly
   below this throughout a central band carrying \(1-o(1)\) of every
   target law.  The exact 8:16 collateral inequalities also have a
   uniform \(1/4+o(1)\) slack after splitting the required death flow
   equally between two layers.  Thus there is **no Gaussian statewise
   capacity obstruction to two overlapping signed Q2 layers**.

The remaining obstruction is literal rather than probabilistic.  Reusing
one Q2 shore gives an involution, not a second one-way exposure.  Two
automatically commuting tensor banks would have to be coordinate-fresh;
freshness and \(o(W)\) seam cost are numerically incompatible at
\(\Theta(\sqrt m)\) layers.  Therefore a viable construction must provide
a jointly completed, overlapping two-seed factor atlas.  Neither the
one-packet associator theorem nor ordinary tensorization supplies that
atlas.

## 1. Exact target type laws

Fix pairs \(P_1,\ldots,P_m\) on \([2m]\), leaving one coordinate
\(\infty\).  A rank-\(m-j\) target of type \((\varepsilon,f)\) has

\[
 \begin{array}{c|cccc}
 &\infty&\text{full pairs}&\text{empty pairs}&\text{split pairs}\\ \hline
 &\varepsilon&f&f+j+\varepsilon&m-j-\varepsilon-2f.
 \end{array}
\tag{1.1}
\]

Consequently its orbit size is

\[
 T_{j}(\varepsilon,f)
  ={2^{m-j-\varepsilon-2f}m!
    \over
    f!(f+j+\varepsilon)!(m-j-\varepsilon-2f)!}.
\tag{1.2}
\]

Write

\[
 \pi_j(\varepsilon,f)={T_j(\varepsilon,f)\over N_j}.
\tag{1.3}
\]

This is exactly the type law of a uniform \((m-j)\)-subset.  In
particular,

\[
 \mathbb E_{\pi_j}f
  =m{(m-j)_2\over(2m+1)_2}
  ={(m-j)(m-j-1)\over2(2m+1)},                       \tag{1.4}
\]

and

\[
 \mathbb E_{\pi_j}\varepsilon={m-j\over2m+1}.        \tag{1.5}
\]

The exact displacement of the pair-type centre from the middle law is

\[
 \Delta_j
 :=\mathbb E_{\pi_0}f-\mathbb E_{\pi_j}f
 ={j(2m-j-1)\over2(2m+1)}
 ={j\over2}+O\!\left({j^2+j\over m}\right).          \tag{1.6}
\]

Thus \(j=A\sqrt m+O(1)\) requires a displacement
\((A/2+o(1))\sqrt m\), not merely an \(O(1)\) correction.

## 2. The exact coherent deletion operator

Let \(S_j\) be uniform in \(\binom{[2m+1]}{m-j}\), and delete one
uniformly chosen member of \(S_j\).  The result is uniform in
\(\binom{[2m+1]}{m-j-1}\): for each fixed \(R\) of the latter rank,
there are \(m+j+2\) supersets \(R\cup\{x\}\), all with the same ordered
deletion weight.  Hence this operation sends \(\pi_j\) exactly to
\(\pi_{j+1}\).

If \(S_j\) has type \((\varepsilon,f)\), then its selected coordinates
consist of

* \(2f\) coordinates in full pairs;
* \(m-j-\varepsilon-2f\) coordinates in split pairs; and
* \(\varepsilon\) copies of \(\infty\).

Deleting from a full pair decreases \(f\) by one.  Deleting from a split
pair is a hold in \((\varepsilon,f)\).  Deleting \(\infty\) changes
\(\varepsilon=1\) to zero.  This proves (0.2)--(0.3), with hold
probability

\[
 {m-j-\varepsilon-2f\over m-j}.                      \tag{2.1}
\]

### Theorem 2.1 (simultaneous fractional target-law transport)

Choose a uniform middle set and then a uniform ordering of its selected
coordinates.  After its first \(j\) deletions, the remaining set is
uniform of rank \(m-j\).  Consequently one nested process realizes all
the laws \(\pi_j\), \(0\le j\le A\sqrt m\), simultaneously.

This is an exact finite identity.  It is stronger than matching the
Gaussian mean and does not use an entropy approximation.

The expected pair-death mass in one step is, by (1.4),

\[
 \sum_{\varepsilon,f}\pi_j(\varepsilon,f){2f\over m-j}
 ={m-j-1\over2m+1}.                                  \tag{2.2}
\]

The expected infinity-death mass is

\[
 \sum_f\pi_j(1,f){1\over m-j}={1\over2m+1}.           \tag{2.3}
\]

Equations (2.2)--(2.3) prove (0.4) and show that the essential transport
is pair-type transport on a positive density of all starts at every
depth.  The infinity correction summed through \(A\sqrt m\) is
\(O_A(W/\sqrt m)\).

The theorem is fractional at the labelled quota level.  It does not
round the common deletion ordering to one integral balanced factor.
By complementation the same construction gives the exact upper target
type laws, with the orbit parameter interpreted as the number of empty
pairs.  This proves separate lower/upper fractional compatibility.  It
does not couple the two chains as the intersection and union shadows of
one literal Johnson path; that coupling is included in the chronology
gate of Section 5.

## 3. The unbiased recoupling birth-death chain

Fix \(j,\varepsilon\), put

\[
 a=j+\varepsilon,
 \qquad h=m-a-2f,
 \qquad e=f+a.                                        \tag{3.1}
\]

Choose two old coordinate pairs uniformly from the \(m\) pairs and then
choose uniformly one of the two non-old pairings on their four
coordinates.

The formulas below apply on the eligible state space
\(m-j-\varepsilon-2f\ge0\).  When the initial law is the middle source
law rather than the target law, its ineligible mass is
\(e^{-\Omega_A(m)}\); it may be adjoined as a cemetery state exactly as
in the fixed-frame capacity theorem.  This correction is suppressed in
the asymptotic statements below.

* If the selected old pairs are one full and one empty pair, either new
  pairing turns them into two split pairs.  This is a death.  There are
  \(fe=f(f+a)\) such choices.
* If both selected old pairs are split, exactly one of the two new
  pairings joins their selected endpoints and creates one full and one
  empty pair.  This is a birth.  There are \(\binom h2\) choices and the
  successful recoupling has probability \(1/2\).
* Every other case is a hold.

This proves (0.5).  The target law \(\pi_j(\cdot\mid\varepsilon)\) is
stationary, as also follows by applying a random coordinate permutation
to a uniform target.

The drift is exactly affine.  Indeed,

\[
\begin{aligned}
 b_{j,\varepsilon}(f)-d_{j,\varepsilon}(f)
 &={h(h-1)/4-f(f+a)\over\binom m2}\\
 &=-\gamma_m\bigl(f-\bar f_{j,\varepsilon}\bigr),
\end{aligned}                                         \tag{3.2}
\]

where

\[
 \gamma_m={2m-1\over m(m-1)},
 \qquad
 \bar f_{j,\varepsilon}
 ={(m-j-\varepsilon)(m-j-\varepsilon-1)\over4m-2}.
\tag{3.3}
\]

Thus the centred linear statistic is an exact eigenfunction:

\[
 \mathbb E[f_{t+1}-\bar f_{j,\varepsilon}\mid f_t]
 =(1-\gamma_m)(f_t-\bar f_{j,\varepsilon}).           \tag{3.4}
\]

On the Gaussian coordinate

\[
                 z={4(f-\bar f_{j,\varepsilon})\over\sqrt m},      \tag{3.4a}
\]

the central birth and death probabilities are both \(1/8+o(1)\).
Consequently, for every smooth compactly supported test function
\(\varphi\), the one-step operator \(K_{j,\varepsilon}\) satisfies

\[
 m(K_{j,\varepsilon}-I)\varphi(z)
   \longrightarrow
       2\varphi''(z)-2z\varphi'(z).                  \tag{3.4b}
\]

Thus the Gaussian recoupling limit is the Ornstein--Uhlenbeck operator
with invariant law \(N(0,1)\).  Formula (3.4b) makes the scale separation
transparent: nontrivial mixing uses \(t=\Theta(m)\), while
\(t=O(\sqrt m)\) has vanishing OU time.

For comparison, if the moving coordinate

\[
                 z_j={4(f-\mathbb E_{\pi_j}f)\over\sqrt m}         \tag{3.4c}
\]

is used for the deletion chain of Section 2, its centred one-step
operator has the same leading diffusion and restoring terms, but its
centre itself translates by \(-1/2+O_A(m^{-1/2})\) in \(f\) per rank.
This moving-centre translation is exactly what the unbiased fixed-rank
recoupling lacks.

### Theorem 3.1 (the \(O(\sqrt m)\) unbiased-mixing obstruction)

Let \(j=A\sqrt m+O(1)\), with \(A>0\), and start the chain from the
eligible middle source law conditional on \(\varepsilon\), placing the
exponentially small ineligible remainder in a cemetery state.  If
\(t\le B\sqrt m\), where \(B\) is fixed, then

\[
 {f_t-f_0\over\sqrt m}\longrightarrow0
 \quad\hbox{in probability}.                         \tag{3.5}
\]

#### Proof

Put \(Y_t=f_t-\bar f_{j,\varepsilon}\), and write

\[
 Y_{t+1}=(1-\gamma_m)Y_t+\xi_{t+1},                  \tag{3.6}
\]

where \((\xi_t)\) is a martingale-difference sequence and
\(|\xi_t|\le2\).  Iteration gives

\[
 Y_t=(1-\gamma_m)^tY_0
   +\sum_{s=1}^t(1-\gamma_m)^{t-s}\xi_s.             \tag{3.7}
\]

Under the middle hypergeometric law, \(Y_0=O_{\mathbb P}(\sqrt m)\).
Since \(t\gamma_m=O(m^{-1/2})\), the first term differs from \(Y_0\)
by \(O_{\mathbb P}(1)\).  The martingale term has second moment at most
\(4t=O(\sqrt m)\), hence divided by \(\sqrt m\) it tends to zero in
probability.  This proves (3.5). \(\square\)

The fixed-pair local central limit theorem gives

\[
 {4(f_0-\mathbb E f_0)\over\sqrt m}\Longrightarrow N(0,1),
 \qquad
 {4(f-\mathbb E f_0)\over\sqrt m}\Bigm|_{\pi_j}
       \Longrightarrow N(-2A,1).                     \tag{3.8}
\]

Therefore

\[
 \liminf_{m\to\infty}
 d_{\rm TV}\bigl(\mathcal L(f_t),\pi_j(f)\bigr)
 \ge 2\Phi(A)-1>0.                                   \tag{3.9}
\]

The bounded infinity bit changes neither limit.  Thus the phrase
``\(O(\sqrt m)\) recoupling layers mix the types'' is false for an
unbiased or frame-symmetric recoupling.  A signed orientation is
essential.

## 4. Exact signed Q2 packet capacity

For a spectator core containing \(f-1\) full old-frame pairs, the lower
shadow table of the exact Q2 associator is

\[
 \text{old shore}:16e_{f-1}+8e_f,
 \qquad
 \text{new shore}:24e_{f-1}.                         \tag{4.1}
\]

Thus one switched packet contributes

\[
             8(e_{f-1}-e_f).                         \tag{4.2}
\]

This has two consequences which should not be conflated.

### 4.1 One-third drift ceiling

Only eight of the packet's 24 lower occurrences move.  In a product
tensor, every touched local Q2 block has the same enumerators

\[
 L_d^0(z)=16+8z,
 \qquad L_d^1(z)=24,
 \qquad d=1,2.                                        \tag{4.3}
\]

If a depth-\(j\) window touches \(J\) local associator blocks, changing
every available shore decreases its aggregate type by at most \(J/3\).
Since \(J\le j\),

\[
             \boxed{\text{one Q2 tensor seed has mean drift at most }j/3.}
\tag{4.4}
\]

By (1.6), the complete target law requires \(j/2+O_A(1)\).  At
\(j=A\sqrt m+O(1)\), one seed leaves a centre error

\[
                  {A\over6}\sqrt m+O_A(1).           \tag{4.5}
\]

The input hypergeometric law has variance \((1+o(1))m/16\), and a
\(j\)-window Q2 action changes the type pointwise by at most \(j\).
The corresponding second moments remain \(O_A(m)\).  Truncation and
Cauchy--Schwarz therefore turn (4.5) into a positive total-variation
gap.  In the fully product-transversal model, the ordinary local CLT gives
the sharper limiting lower bound

\[
                    2\Phi(A/3)-1.                    \tag{4.6}
\]

The precise constant (4.6) is model-specific; the positive gap from
(4.4)--(4.5) is the invariant conclusion.

The bounded suspension of one isolated Q2 packet is still weaker: it has
only eight signed depth-one occurrences among \(12h\) starts, a fraction
\(2/(3h)\).  Macroscopic signed action with long cycles therefore really
requires the tensor/packed use of Q2 blocks; suspension alone does not
provide it.

### 4.2 The exact collateral inequality

Suppose a packet layer acts on a type histogram \((M_f)\), and let \(x_f\)
be the mass it moves from \(f\) to \(f-1\).  Formula (4.1) says that every
unit of moved type-\(f\) mass requires two unchanged type-\((f-1)\)
occurrences in its packet.  Ignoring labels but retaining exact state
counts, a disjoint packet layer must satisfy

\[
                  \boxed{x_f+2x_{f+1}\le M_f.}        \tag{4.7}
\]

This is the correct coarse capacity inequality; the scalar bound
\(\sum_fx_f\le(1/3)\sum_fM_f\), obtained by summing (4.7), loses the
adjacent-type collateral.

For the deletion transport at rank \(m-j\), put

\[
 M_{\varepsilon,f}=W\pi_j(\varepsilon,f),
 \qquad
 x_{\varepsilon,f}={2f\over m-j}M_{\varepsilon,f}.    \tag{4.8}
\]

From (1.2), with

\[
 h=m-j-\varepsilon-2f,
\tag{4.9}
\]

one has the exact adjacent ratio

\[
 {M_{\varepsilon,f+1}\over M_{\varepsilon,f}}
 ={h(h-1)\over4(f+1)(f+j+\varepsilon+1)}.            \tag{4.10}
\]

Consequently

\[
 {x_{\varepsilon,f+1}\over M_{\varepsilon,f}}
 ={h(h-1)\over
   2(m-j)(f+j+\varepsilon+1)}.                        \tag{4.11}
\]

On the central band

\[
 |f-\bar f_{j,\varepsilon}|\le m^{2/3},              \tag{4.12}
\]

uniformly for \(j\le A\sqrt m\), equations (4.8) and (4.11) give

\[
 {x_{\varepsilon,f}\over2M_{\varepsilon,f}}
       ={1\over4}+o(1),
 \qquad
 {x_{\varepsilon,f+1}\over M_{\varepsilon,f}}
       ={1\over2}+o(1).                               \tag{4.13}
\]

Split every required flow equally between two packet layers.  In either
layer the type-\(f\) consumption is

\[
 {x_{\varepsilon,f}\over2}+x_{\varepsilon,f+1}
       =\left({3\over4}+o(1)\right)M_{\varepsilon,f}. \tag{4.14}
\]

Thus (4.7) holds with \(1/4+o(1)\) slack.  After the first half-flow, the
current type-\(f\) mass is

\[
 M'_{\varepsilon,f}
 =M_{\varepsilon,f}-{x_{\varepsilon,f}\over2}
                 +{x_{\varepsilon,f+1}\over2}
 =(1+o(1))M_{\varepsilon,f},                          \tag{4.15}
\]

so the same slack holds for the second layer.

At the fractional orbit level, (4.7) is also sufficient for the local
packet inventory in the central range.  For fixed
\((j,\varepsilon,f)\), take every coordinate embedding of the Q2 frame
whose death occurrences have type \(f\), and average it under the fixed
pair wreath group.  Transitivity makes its death marginal constant on
the type-\(f\) orbit and its collateral marginal constant on the
type-\((f-1)\) orbit; (4.1) makes the two marginal masses occur in the
exact ratio \(1:2\).  Superposing these averaged packet families over
\(f\) uses a type-\(f\) occurrence to total weight
\(x_f+2x_{f+1}\).  Hence (4.7) is precisely the fractional vertex-capacity
condition.  Central states have linearly many full, empty, and split
pairs, so all required local embeddings exist.  This averaging does not
produce disjoint literal packets; that is the completion gate in Section
5.

The complement of (4.12) has mass at most
\(2\exp(-c_Am^{1/3})\) by bounded-difference concentration for a uniform
subset.  Summing it through \(A\sqrt m\) depths is still \(o(W)\).

Equivalently, at the one-owner level a fully exposed Q2 layer has death
probability \(1/3\).  Two fresh exposures can realize any tagged death
probability at most \(5/9\): after exposing one third, expose a suitable
fraction of the survivors in the second layer.  Since

\[
 {2f\over m-j}={1\over2}+o(1)<{5\over9}              \tag{4.16}
\]

on (4.12), this is the same central feasibility statement as
(4.14), with (4.14) additionally retaining the packet collateral.

### Theorem 4.1 (coarse two-layer feasibility, exact boundary)

At the wreath-orbit fractional level, two fresh signed Q2 exposures per
physical deletion phase have enough statewise capacity to implement the
pair-death part of the exact nested kernel at every
\(j\le A\sqrt m\), after discarding total mass \(o(W)\).  One exposure
does not: its \(1/3\) ceiling is separated from the required central rate
\(1/2+o(1)\).

The theorem asserts fractional type capacity, not a literal factor.  Its
word ``fresh'' includes the unproved requirement that the second Q2
packetization be available on the survivors and collateral after the
first factor switch.

The mean-sharp cumulative visibility count can also be stated exactly.
Conditional on the infinity bit \(\varepsilon\), the paired source and
depth-\(j\) target centres differ by

\[
 \Delta_{\varepsilon,j}
 ={j(2m-2\varepsilon-j-1)\over2(2m-1)}.               \tag{4.17}
\]

Since every effective Q2 exposure contributes mean drift \(1/3\), the
required visible-layer count is

\[
 L^*_{\varepsilon,j}=3\Delta_{\varepsilon,j},
 \qquad
 L^*_{\varepsilon,j+1}-L^*_{\varepsilon,j}
 ={3(m-\varepsilon-j-1)\over2m-1}
 ={3\over2}+O_A(m^{-1/2}).                            \tag{4.18}
\]

Thus one may thin the two available exposures so that each physical depth
uses one or two, with asymptotic average \(3/2\).  Equations
(4.14)--(4.16) show that this sharp thinning has coarse central capacity.
They do not turn it into one literal chronological factor.

## 5. Seam arithmetic and the first exact failure

An \(h\)-direction tensor cell has physical cycles of length \(2h\), so a
near-spanning tensor factor has \(O(W/h)\) components.  If
\(L=O_A(\sqrt m)\) recoupling layers could be composed with an additive
constant number of cuts per component per layer, their numerical toll
would be

\[
                       O_A\!\left({W\sqrt m\over h}\right).        \tag{5.1}
\]

Choosing, for example, a power of two

\[
                    m^{2/3}\le h<2m^{2/3}             \tag{5.2}
\]

makes (5.1) \(o(W)\), while the canonical tensor-packet leave remains
exponentially small.  Thus seam **arithmetic** does not obstruct the
birth-death plan.

It does not follow that the existing Hamming rows pass.  If a
\(C_{2h}\) row is contained in a pair frame at matching-switch distance
at most \(t\) from the base frame, then every depth-\(j\) window has the
exact transport ceiling

\[
                 \mathsf W_1(\nu_j,V)
                    \le {2tj\over h}\,W.             \tag{5.2a}
\]

Indeed at most \(2t\) active matching edges are nonbase; each occurs twice
in the Hamming direction word and lies in exactly \(j\) cyclic
\(j\)-windows.  The Gaussian source and target laws have
\(\Theta_A(W\sqrt m)\) truncated one-Lipschitz transport distance at
\(j=A\sqrt m\).  Hence the current pair-geodesic Hamming architecture
requires \(t/h=\Omega_A(1)\).  With \(t=O(\sqrt m)\), the choice
\(h\gg\sqrt m\) which makes (5.1) small violates this action condition.
Thus (5.1) shows only that a genuinely overlapping non-Hamming braid has
no scalar seam-budget obstruction; it does not rescue a final row lying
in one radius-\(t\) frame.

Coordinate-fresh automatic commutation does obstruct the easy
realization.  A tensor layer of dimension \(h=2r\) uses \(r\) disjoint
eight-coordinate Q2 blocks, hence \(4h\) coordinates.  If \(L\) layers
are mutually coordinate-disjoint, then

\[
                         4hL\le2m+1.                 \tag{5.3}
\]

For \(L=\Theta(\sqrt m)\), (5.3) forces \(h=O(\sqrt m)\), whereas
\(o(W)\) in (5.1) requires \(h/\sqrt m\to\infty\).  Therefore fresh
disjoint tensor banks cannot meet both demands.

Reusing the same Q2 packet also fails: the local resolution has only two
shores, so a second application reverses the first rather than giving a
second independent death exposure.  The statewise feasibility from
Theorem 4.1 consequently requires genuinely overlapping, nonidentical
frames.

The first unresolved exact statement is the following.

### Overlapping two-seed completion gate

Construct on one common near-spanning middle support two oriented Q2
packetizations such that

1. every one of their four joint resolution states is a literal completed
   long-cycle factor;
2. the second signed exposure is fresh on the first layer's survivors and
   supplies the collateral ledger (4.7);
3. a single physical depth-\(j\) window sees the two micro-exposures in the
   chronological order required by (0.2), simultaneously for every
   \(j\le A\sqrt m\); and
4. the full joint factors retain \(O(W/h)\), rather than a product number,
   of physical components.

Ordinary tensorization proves each one-seed factor separately.  It does
not prove these four joint corners when the two packetizations overlap.
Conversely, the exact orbit laws, the Gaussian birth-death calculation,
and the Q2 8:16 ledger give no statewise obstruction to such a joint
atlas.

## 6. Constant-one implication

The fixed-pair Gaussian quota obstruction requires \(\Theta_A(W)\)
cross-type starts.  Equation (2.2) identifies an exact coherent transport
which supplies them.  Equations (4.4) and (4.14) sharpen the architectural
boundary:

\[
 \boxed{
 \begin{array}{c}
 \text{one reciprocal Q2 tensor seed: insufficient drift;}\\
 \text{two fresh overlapping signed seeds: fractionally sufficient;}\\
 \text{unbiased recouplings: relaxation time }\Theta(m);\\
 \text{literal overlapping completion: open.}
 \end{array}}
\tag{6.1}
\]

Accordingly this audit neither proves coefficient one nor gives a new
Gaussian no-go for the intended signed architecture.  It closes the
unbiased and one-seed versions and reduces the positive route to a precise
two-seed long-cycle completion theorem, with all type capacities and seam
scales already compatible.
