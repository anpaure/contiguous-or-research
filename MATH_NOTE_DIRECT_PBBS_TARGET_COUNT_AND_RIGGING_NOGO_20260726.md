# Direct PBBS dynamics: exact window counts and the rigging-randomization no-go

Date: 2026-07-26

Pure mathematics only. No computation or web search is used.

## 0. Verdict

Let

\[
 n=2m+1,\qquad \mathcal M=\binom{[n]}m,\qquad
 W=|\mathcal M|=\binom{2m+1}m.
\]

The literal Gaussian-window target proposed in the prompt is impossible,
independently of PBBS.  If \(q/\sqrt m\to a>0\), then the numbers of lower
and upper targets are

\[
 N_q^- = \binom{2m+1}{m-q},\qquad
 N_q^+ = \binom{2m+1}{m+q},
\]

and

\[
 \frac{W}{N_q^-}=e^{a^2+o(1)},\qquad
 \frac{W}{N_q^+}=e^{a^2+o(1)}.
\tag{0.1}
\]

Thus a middle-owner permutation supplies \(W\) based windows to a layer
having only \((e^{-a^2}+o(1))W\) targets.  The exact identity proved below is

\[
 \boxed{b_q^\pm+e_q^\pm=W-N_q^\pm+h_q^\pm,}
\tag{0.2}
\]

where \(b_q^\pm\) is the number of wrong-rank windows, \(h_q^\pm\) is the
number of uncovered correct-rank targets, and

\[
 e_q^\pm=\sum_S(\mu_q^\pm(S)-1)_+
\]

is the total overload above raw load one.  Consequently, at every nonzero
Gaussian depth, wrong-rank mass and overload above one cannot both be
\(o(W)\).  If all correct targets occur, then

\[
 b_q^\pm+e_q^\pm
 =\bigl(1-e^{-a^2}+o(1)\bigr)W.
\tag{0.3}
\]

There is also a separate dynamical no-go.  Translating riggings, changing
the time origin on a PBBS orbit, permuting equal-amplitude riggings, or
applying any other angle-torus translation does not change the successor
map and does not change even one aggregate target statistic.  The full
middle layer already contains every phase.  Randomizing a global coordinate
order makes the expected load target-uniform, but merely permutes the
existing load vector in every realization; it cannot reduce holes,
collisions, or wrong-rank mass.

Therefore soliton phases do not provide a coefficient-one averaging
resource.  A genuine recoupling that changes target counts must replace
PBBS successor arcs (or repartition the owner set among differently
conjugated PBBS components).  That is a new global exact-cover/path-legality
problem, not direct PBBS dynamics.

The correct Gaussian target is not raw unit load.  It is floor/ceiling
balance about the mean \((W-b_q^\pm)/N_q^\pm\), together with small
wrong-rank mass.  The canonical PBBS all-depth corridor gives support, but
rigging randomization cannot prove the still-missing floor-completion
estimate.

## 1. Exact PBBS chronology

Let \(f\) be the cyclic parenthesis/PBBS permutation.  On an oriented
\(f\)-component write

\[
 A_i=f^i(A_0),
\]

and let \(\lambda_i\) be the unique omitted coordinate on the odd-graph
edge \(A_iA_{i+1}\).  Thus

\[
 A_{i+1}=[n]\setminus(A_i\cup\{\lambda_i\}).
\tag{1.1}
\]

Applying (1.1) twice gives the exact step-two identity

\[
 \boxed{A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}.}
\tag{1.2}
\]

Put \(g=f^2\), fix a parity, and set

\[
 B_t=A_{i+2t},\qquad
 d_t=\lambda_{i+2t+1},\qquad
 a_t=\lambda_{i+2t}.
\]

Then the exact directed Johnson chronology is

\[
 \boxed{B_{t+1}=B_t-\{d_t\}+\{a_t\},}
\qquad d_t\in B_t,\quad a_t\notin B_t.
\tag{1.3}
\]

For the \(q\)-edge window based at \(B_0\), define

\[
 I_q=\bigcap_{t=0}^qB_t,
 \qquad
 U_q=\bigcup_{t=0}^qB_t.
\]

The chronology (1.3) gives the set identities

\[
 \boxed{
 I_q=B_0\setminus
       \{d_t:d_t\in B_0,\ 0\le t<q\},}
\tag{1.4}
\]

and

\[
 \boxed{
 U_q=B_0\cup
       \{a_t:a_t\notin B_0,\ 0\le t<q\}.}
\tag{1.5}
\]

Indeed, an original coordinate leaves the intersection precisely when it is
deleted for the first time, and a nonoriginal coordinate enters the union
precisely when it is inserted for the first time.  Later returns do not undo
either event.

It follows that

\[
 |I_q|=m-q
\quad\Longleftrightarrow\quad
 d_0,\ldots,d_{q-1}
 \text{ are distinct elements of }B_0,
\tag{1.6}
\]

and

\[
 |U_q|=m+q
\quad\Longleftrightarrow\quad
 a_0,\ldots,a_{q-1}
 \text{ are distinct elements of }[n]\setminus B_0.
\tag{1.7}
\]

Thus PBBS soliton returns are exactly the obstruction to correct rank in
these two ledgers.  No independence assumption is present.

There is also an exact cross-shore identity.  From (1.1)--(1.2),

\[
 A_{j+1}=[n]\setminus(A_j\cup A_{j+2}).
\tag{1.8}
\]

Therefore, for every \(q\ge1\),

\[
 \boxed{
 [n]\setminus\bigcup_{h=0}^q A_{i+2h}
 =\bigcap_{h=0}^{q-1}A_{i+2h+1}.}
\tag{1.9}
\]

Indeed, intersect (1.8) for \(j=i,i+2,\ldots,i+2q-2\) and apply De
Morgan's law.  Consequently the complete PBBS upper histogram at depth
\(q\) is the complemented lower histogram at depth \(q-1\) on the
opposite step-two phase:

\[
 \boxed{
 \mu_{P,q}^+(S)=\mu_{P,q-1}^-(S^c),\qquad
 b_{P,q}^+=b_{P,q-1}^-.}
\tag{1.10}
\]

The ranks agree because

\[
 |S|=m+q
 \quad\Longleftrightarrow\quad
 |S^c|=m+1-q=m-(q-1).
\]

This also explains the exact equality \(N_q^+=N_{q-1}^-\) and the shifted
exponent \(q(q-1)/m\) in the upper Gaussian count.

## 2. A universal target-count identity

The following theorem applies to every permutation of the middle layer, not
only PBBS.

### Theorem 2.1 (defect--hole--overload conservation)

Let \(T\) be a permutation of \(\mathcal M\).  For each based \(q\)-window

\[
 X,T X,\ldots,T^qX,
\]

form its intersection and union.  For \(\varepsilon=-\), call a window
good when its intersection has rank \(m-q\); for \(\varepsilon=+\), call
it good when its union has rank \(m+q\).  Let

\[
 b_q^\varepsilon
 =W-\#\{\text{good based windows}\}.
\]

For a target \(S\) in the corresponding rank layer, let
\(\mu_q^\varepsilon(S)\) be its number of good occurrences.  Define

\[
 h_q^\varepsilon
 =\#\{S:\mu_q^\varepsilon(S)=0\},
 \qquad
 e_q^\varepsilon
 =\sum_S(\mu_q^\varepsilon(S)-1)_+.
\]

Then

\[
 \boxed{
 b_q^\varepsilon+e_q^\varepsilon
 =W-N_q^\varepsilon+h_q^\varepsilon.}
\tag{2.1}
\]

#### Proof

Every good based window contributes to exactly one target, so

\[
 \sum_S\mu_q^\varepsilon(S)=W-b_q^\varepsilon.
\tag{2.2}
\]

There are \(N_q^\varepsilon-h_q^\varepsilon\) targets of positive load.
Writing each positive load as one plus its excess gives

\[
 \sum_S\mu_q^\varepsilon(S)
 =N_q^\varepsilon-h_q^\varepsilon+e_q^\varepsilon.
\tag{2.3}
\]

Equating (2.2) and (2.3) proves (2.1).  \(\square\)

This identity is stronger than an expectation argument.  In particular,
complete support \(h_q^\varepsilon=0\) forces

\[
 b_q^\varepsilon+e_q^\varepsilon=W-N_q^\varepsilon.
\tag{2.4}
\]

## 3. Exact Gaussian asymptotics

Direct factorial cancellation gives

\[
 \frac{W}{N_q^-}
 =\prod_{i=1}^q
   \frac{m+i+1}{m-q+i},
\tag{3.1}
\]

and

\[
 \frac{W}{N_q^+}
 =\prod_{i=1}^q
   \frac{m+i}{m+2-i}.
\tag{3.2}
\]

Uniformly for \(q\le A\sqrt m\), Taylor expansion of the logarithms gives

\[
 \log\frac{W}{N_q^-}
 =\frac{q(q+1)}m+O_A(m^{-1/2}),
\tag{3.3}
\]

and

\[
 \log\frac{W}{N_q^+}
 =\frac{q(q-1)}m+O_A(m^{-1/2}).
\tag{3.4}
\]

For example, in (3.1) the first-order difference of the numerator and
denominator offsets is \(q+1\) in every factor, giving \(q(q+1)/m\);
the sum of all quadratic remainders is \(O_A(q^3/m^2)=O_A(m^{-1/2})\).
The upper calculation is identical.

Hence, if \(q/\sqrt m\to a>0\),

\[
 N_q^\pm=(e^{-a^2}+o(1))W.
\tag{3.5}
\]

Combining (2.1) and (3.5) proves

\[
 b_q^\pm+e_q^\pm-h_q^\pm
 =\bigl(1-e^{-a^2}+o(1)\bigr)W.
\tag{3.6}
\]

Two consequences should not be conflated.

1. If \(b_q^\pm=o(W)\) and \(h_q^\pm=o(W)\), then raw overload above
   one is necessarily

   \[
   e_q^\pm
   =\bigl(1-e^{-a^2}+o(1)\bigr)W.
   \tag{3.7}
   \]

2. If the loads are one apart from \(o(W)\) total exceptions, so that
   \(e_q^\pm=o(W)\), and there are \(o(W)\) holes, then

   \[
   b_q^\pm
   =\bigl(1-e^{-a^2}+o(1)\bigr)W.
   \tag{3.8}
   \]

Thus literal unit load can be bought only by discarding a constant fraction
of all based windows as wrong-rank windows.  This is fatal for a
coefficient-one band transfer.

## 4. What “balanced load” can mean at Gaussian depth

Assume \(b_q^\pm=o(W)\).  The mean good load is

\[
 \overline\lambda_q^\pm
 =\frac{W-b_q^\pm}{N_q^\pm}
 =e^{a^2}+o(1).
\tag{4.1}
\]

The integral optimum is therefore a floor/ceiling vector around
\(\overline\lambda_q^\pm\), not a vector of ones.  Even the normalized
pointwise statement

\[
 \mu_q^\pm(S)/\overline\lambda_q^\pm=1+o(1)
\tag{4.2}
\]

cannot hold uniformly for a generic fixed \(a\): if \(e^{a^2}\) stays a
positive distance from the integers, integrality prevents every load from
approaching that number.  The stable integral formulation is that all but
few targets have one of the two values

\[
 \lfloor\overline\lambda_q^\pm\rfloor,
 \qquad
 \lceil\overline\lambda_q^\pm\rceil,
\]

with a small floor-corrected collision excess.

Accordingly, (3.7) is not by itself an obstruction to coefficient one; it
is the unavoidable background multiplicity.  What (3.7) disproves is the
raw unit-load formulation in the prompt.

## 5. Rigging shifts cannot alter the target histogram

Write the periodic box-ball inverse-scattering decomposition abstractly as

\[
 \mathcal M=\bigsqcup_\alpha\Omega_\alpha,
\]

where \(\alpha\) is the conserved action/soliton content and the PBBS map on
an angle component is a translation

\[
 T_\alpha:z\longmapsto z+h_\alpha.
\tag{5.1}
\]

A change of rigging origin is another translation

\[
 R_\alpha:z\longmapsto z+v_\alpha.
\tag{5.2}
\]

Translations commute, so

\[
 R^{-1}TR=T.
\tag{5.3}
\]

The same conclusion holds for a permutation of equal-amplitude riggings:
PBBS adds the same velocity to all riggings of that amplitude, so the
permutation commutes with the evolution.  Orbitwise time changes
\(R(x)=T^{c(C)}x\) are a still more elementary special case.

There are two possible interpretations of phase randomization, and both
are inert.

* If it is used to conjugate the dynamics, (5.3) says that the dynamics is
  unchanged.

* If it is used only to choose new starting phases, then \(R\) is a
  bijection of the full middle layer.  For any window statistic \(\Phi_q\),

  \[
  \sum_{x\in\mathcal M}\delta_{\Phi_q(Rx)}
  =\sum_{y\in\mathcal M}\delta_{\Phi_q(y)}.
  \tag{5.4}
  \]

  Thus its complete target-count measure is exactly unchanged.

This is the finite-ensemble point missed by a heuristic appeal to random
scattering phases: a coefficient-one middle-owner permutation uses every
owner, hence every available phase, once already.  There is no unaveraged
phase reservoir left.

Reversing a PBBS component is equally inert for intersection/union counts.
The backward window

\[
 x,T^{-1}x,\ldots,T^{-q}x
\]

is the same unordered family of owners as the forward window based at
\(T^{-q}x\).  Therefore reversal preserves both complete histograms.

## 6. Coordinate-order randomization gives only a first moment

There is one genuine target-transitivity statement, but it does not produce
a better factor.

### Theorem 6.1 (global-conjugation averaging)

Let \(\sigma\in S_n\), and conjugate a middle-owner permutation by

\[
 T^\sigma=\sigma T\sigma^{-1}.
\]

Then, for either sign,

\[
 \boxed{
 \mu_{T^\sigma,q}^\pm(S)
 =\mu_{T,q}^\pm(\sigma^{-1}S).}
\tag{6.1}
\]

In particular, if \(\sigma\) is uniform in \(S_n\), then

\[
 \boxed{
 \mathbb E_\sigma\mu_{T^\sigma,q}^\pm(S)
 =\frac{W-b_q^\pm}{N_q^\pm}}
\tag{6.2}
\]

for every target \(S\).  Nevertheless, every realization has exactly the
same multiset of target loads, the same number of holes, and the same
floor-corrected collision energy as \(T\).

#### Proof

Intersection and union commute with \(\sigma\).  A \(T^\sigma\)-window
based at \(x\) is the \(\sigma\)-image of the \(T\)-window based at
\(\sigma^{-1}x\), proving (6.1).  The symmetric group is transitive on
each rank layer, so averaging (6.1) and using the total good mass gives
(6.2).  Equation (6.1) also proves every asserted histogram invariance.
\(\square\)

The cyclic rotation group used by one fixed PBBS order is transitive only
inside a target necklace.  It therefore yields equality within necklaces,
not between them.  This is exactly why the PBBS Gaussian collision gate is
a conditional-completion theorem on target necklaces.  Randomly rotating
the order cannot change a necklace fibre.  Randomly choosing one global
order merely relabels the full histogram as in Theorem 6.1.

## 7. Why a nonlocal recoupling is a different problem

For the fixed PBBS map, every owner has one prescribed successor.  Keeping
all direct PBBS arcs keeps the same permutation.  Translating or scattering
riggings only reindexes its invariant angle tori, by Section 5.

There are two ways to obtain genuinely new counts.

1. Replace the velocity \(h_\alpha\) by a different box-ball flow.  This is
   not a phase randomization.  It must separately prove that every physical
   successor is a one-deletion/one-insertion Johnson edge; a general PBBS
   time advance does not supply that property.

2. Put different coordinate conjugations on different components and then
   repartition the middle owners among their images.  Independently
   conjugated components generally overlap and leave holes.  Making their
   images form an exact owner partition is precisely a global exact-cover
   assignment, and the connecting arcs must again be checked physically.

Thus a successful nonlocal recoupling may exist, but neither conserved
riggings nor soliton scattering gives it for free.  It lies outside the
“use PBBS directly” lane.

## 8. Consequence for the constant-one gate

For the canonical step-two PBBS map, the all-depth corridor theorem already
gives at least one correct lower occurrence for every rank-\((m-q)\)
target.  Hence \(h_q^-=0\), and Theorem 2.1 specializes exactly to

\[
 b_q^-+e_q^-=W-\binom{2m+1}{m-q}.
\tag{8.1}
\]

By (1.9)--(1.10), the same theorem at lower depth \(q-1\) gives complete
upper support at depth \(q\), and

\[
 \boxed{
 h_q^+=0,\qquad
 b_q^++e_q^+=W-\binom{2m+1}{m+q}.}
\tag{8.2}
\]

This support theorem does not control Gaussian floor balance.  The needed
quantity is the excess above the floor/ceiling optimum, not \(e_q^-\),
which includes the unavoidable mean-density contribution in (3.7).

Moreover, Sections 5 and 6 show that all ordinary rigging, scattering-phase,
orbit-origin, reversal, and global-order randomizations preserve that
floor-corrected excess.  Consequently the proposed PBBS outer gate has the
following sharp boundary:

\[
\boxed{
\begin{array}{l}
\text{Raw load }1+o(1)\text{ at nonzero Gaussian depth is impossible;}\\[2mm]
\text{phase/rigging randomization cannot improve the canonical histogram;}\\[2mm]
\text{only a genuinely new, physically legal global recoupling could do so.}
\end{array}}
\]

No invariant proved here rules out every possible noncommuting recoupling.
It does rule out the proposed direct-dynamics and randomized-rigging
mechanisms, and it identifies floor-completion rather than unit load as the
only correctly calibrated remaining target theorem.
