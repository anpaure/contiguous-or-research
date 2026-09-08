# Dynamic TRP temporal propagation: exact invariant and finite-lookahead theorem

Date: 2026-07-25

This note continues the dynamic round analysis of
`DYNAMIC_TRP_ROUND_HALL_AND_FLAG_OBSTRUCTION_20260725.md`.

## 0. Outcome

There is more propagation than the one-round obstruction initially
suggests.  Every arrival-star base in the next round is exactly a current
flag one depth farther from the middle:

\[
 B_0=L_1,
 \qquad B^-_q=L_{q+1},
 \qquad B^+_q=U_{q-1}.                              \tag{0.1}
\]

Consequently a current layer which is collision-free in every row cannot
produce the identical common-star fibre from Theorem 5.1 in the next
round.  The bad fibre necessarily already has a collision in the adjacent
current row.

The surviving temporal statistic is second order.  Many *distinct* current
flags can be different facets of the same next target.  Define their
facet congestion by (2.2) below.  A small weighted maximum facet congestion,
together with positive residual option density and the deepest-lower Hall
condition, is a rigorous one-round continuation invariant.

A finite-lookahead version can be proved unconditionally from a fresh
uniform state ensemble.  If

\[
 \ell^2 {1+2\sum_{q\le Q}\lambda_q\over\lambda_H}=o(1),
 \tag{0.2}
\]

then all but \(o(N_H)\) carriers admit length-\(\ell\) rotor paths whose
owners and every controlled flag are pairwise distinct across every
carrier and every one of the \(\ell\) times.  In particular this holds for

\[
 \ell=o\!\left(
   \sqrt{Q\over\lambda_Q}
 \right)
 =m^{1/4}(\log\log m)^{1/4}
   (\log m)^{-1/2-o(1)}.
 \tag{0.3}
\]

This is the strongest direct multi-round consequence of the fresh-state
LLL currently proved here.  The method has an exact square-horizon loss:
the option-conflict ratio is multiplied by \(\ell^2\).  At the required
\(\ell=M\asymp m\) it is enormous.  Moreover the independent-transversal
output is not known to preserve facet congestion at its endpoint.  Thus a
local fresh-round LLL cannot simply be iterated \(M\) times; a genuine
second-order propagation theorem or a global capacitated path matching is
still needed.

## 1. Adjacent-depth transport of candidate bases

For a current state

\[
 \omega=(L;z_1,\ldots,z_{2Q};R)
\]

and a transition chosen by \(x\in L\), \(y\in R\), recall

\[
 \omega'=(L-x+y;x,z_1,\ldots,z_{2Q-1};R-y+z_{2Q}).
\]

The current flags are

\[
 L_q(\omega)=L\cup\{z_1,\ldots,z_{Q-q}\},
\]

\[
 U_q(\omega)=L\cup\{z_1,\ldots,z_{Q+q}\}.
\]

Put \(U_0=L_0=X\).  The exact successor formulas may then be rewritten
without auxiliary bases:

\[
 \boxed{X(\omega')=L_1(\omega)+y,}                 \tag{1.1}
\]

\[
 \boxed{L_q(\omega')=L_{q+1}(\omega)+y
 \quad(1\le q<Q),}                                 \tag{1.2}
\]

\[
 \boxed{U_q(\omega')=U_{q-1}(\omega)+y
 \quad(1\le q\le Q),}                             \tag{1.3}
\]

and

\[
 \boxed{L_Q(\omega')=L_Q(\omega)-x+y.}            \tag{1.4}
\]

Thus the arrival-controlled rows are successive upper shadows of current
adjacent flags.  The only current row not transported in this form is the
deepest lower row, where the \(m-Q\) choices of \(x\) remain visible.

### Lemma 1.1 (distinct bases have at most one common extension)

Let \(B,B'\) be distinct \((r-1)\)-sets, and let \(R,R'\) be disjoint from
\(B,B'\), respectively.  Then

\[
 \bigl|\{B+y:y\in R\}\cap\{B'+y':y'\in R'\}\bigr|
 \le1.                                               \tag{1.5}
\]

Indeed an equality \(B+y=B'+y'\) determines
\(y\in B'\setminus B\) and \(y'\in B\setminus B'\), unless \(y=y'\), in
which case it forces \(B=B'\).  Hence at most one pair can work.

It follows from (1.1)--(1.3) that if current flags in every row are
pairwise distinct across carriers, then any two next-round arrival stars
intersect in at most one target at each row.  In particular the common
upper-star construction of Theorem 5.1 has

\[
 U_{Q-1}(\omega_i)=B
\]

for every carrier in its bad fibre.  It cannot be reached as a
collision-free current layer.

Pairwise star intersection at most one is helpful, but is not a Hall
theorem: up to \(r\) distinct \((r-1)\)-facets may still point to one
rank-\(r\) target.

## 2. The exact low-conflict invariant

Index the arrival-controlled successor rows by

\[
 \mathcal R_{\rm arr}
 =\{0\}\cup\{-1,\ldots,-(Q-1)\}
       \cup\{+1,\ldots,+Q\}.
\]

For carrier \(i\), let \(B_{i,\rho}\) be the current adjacent flag which
serves as the base in row \(\rho\), as specified by (1.1)--(1.3).  For a
target \(S\) in that successor row define the exact candidate-facet
congestion

\[
 \kappa_\rho(S)
 =\#\left\{i:
 B_{i,\rho}\subset S,
 \ S\setminus B_{i,\rho}\in R_i
 \right\}.                                         \tag{2.1}
\]

If an arrival option \((i,y)\) produces target
\(S=B_{i,\rho}+y\), then exactly
\(\kappa_\rho(S)-1\) other carrier-arrival options collide with it in
that row.  Therefore the maximum degree \(\Delta_{\rm arr}\) of the full
arrival-column conflict graph obeys

\[
 \boxed{
 \Delta_{\rm arr}
 \le
 \max_{i,y}
 \sum_{\rho\in\mathcal R_{\rm arr}}
 \bigl(\kappa_\rho(B_{i,\rho}+y)-1\bigr)_+ .}
 \tag{2.2}
\]

This is the precise second-order statistic missing from rowwise Hall.
Current row distinctness only gives the deterministic bound
\(\kappa_\rho(S)\le |S|=O(m)\), far too weak for the arrival part size
\(a=H-Q\).  Section 2.2 below shows that this bound is essentially sharp
even when *every* current controlled row is collision-free.  Thus maximum
\(\kappa\) is not itself a viable invariant.

Let \(s_i\) be the number of arrivals at carrier \(i\) whose entire
arrival column has positive residual capacity.  The local-lemma round
criterion from the preceding note now says:

### Proposition 2.1 (one-round quasirandom continuation)

If

\[
 \min_i s_i=s,
 \qquad
 s^2\ge e(2a\Delta_{\rm arr}+1),                   \tag{2.3}
\]

and the deepest-lower capacitated Hall inequalities hold after the
arrivals are selected, then the current layer extends by one round without
exceeding any residual quota.

Thus a clean, but deliberately strong, temporal invariant consists of:

1. **column availability:** \(s_i\ge s\) for almost every carrier;
2. **facet quasirandomness:** the right side of (2.2) is
   \(O(s^2/a)\);
3. **deep-lower Hall:** the \(m-Q\)-choice system (DH);
4. **exception budget:** if \(B\) is the total number of exceptional
   carrier-round state slots, then

   \[
   B=o(MN_H/Q)=o(W/Q).
   \]

Indeed one exceptional state slot can lose one target in each of the
\(2Q+1\) controlled rows, so its aggregate repair charge is \(O(Q)\).
The displayed total bound, equivalently an average exceptional fraction
\(o(1/Q)\) per round, makes this charge \(o(W)\); a merely uniform
\(o(1)\) exceptional fraction does not suffice when \(Q\to\infty\).

The difficult clause is (2).  Equations (1.1)--(1.3) identify the next
bases with the flags selected now, but collision-free selection controls
only equality of those bases, not their incidence with all one-element
extensions \(S\).

### 2.2 Collision-free rows can have \(\kappa\asymp m\)

The maximum-congestion version of clause (2) is false even for a perfectly
collision-free current layer.

Fix an \(m\)-set \(S\).  Choose a fixed \((Q-1)\)-set \(P\subset S\), a
fixed \((H-1)\)-set \(C\subset[2m]\setminus S\), and put

\[
 D\subset S\setminus P,
 \qquad |D|=m-H+1.                                  \tag{2.4}
\]

The complement of \(S\cup C\) also has size \(m-H+1\); biject it with
\(D\), writing its elements as \(e_d\), \(d\in D\).  For each \(d\),
take the distinct top

\[
 U_d=S\cup C\cup\{e_d\}.                            \tag{2.5}
\]

Build a state as follows:

\[
 L_d=S\setminus(P\cup\{d\}),                       \tag{2.6}
\]

order \(P\) as \(z_1,\ldots,z_{Q-1}\), put
\(z_Q=e_d\), order \(Q\) elements of \(C\) as
\(z_{Q+1},\ldots,z_{2Q}\), and let

\[
 R_d=\{d\}\cup
 \bigl(C\setminus\{z_{Q+1},\ldots,z_{2Q}\}\bigr).
 \tag{2.7}
\]

The last set has size \(1+(H-1-Q)=H-Q=a\), so these are legitimate
states.

Every current lower flag is distinguished by the missing coordinate
\(d\): explicitly it has the form

\[
 S\setminus\bigl(\{d\}\cup P_q\bigr)               \tag{2.8}
\]

for a fixed tail \(P_q\subseteq P\).  Every current owner and upper flag
contains the private coordinate \(e_d\), and hence those rows are also
pairwise distinct.  Thus all controlled current flags are collision-free
across the \(|D|\) carriers.

But the next-owner base is

\[
 L_1(\omega_d)=S-d,                                 \tag{2.9}
\]

and \(d\in R_d\).  Therefore every one of these distinct bases has \(S\)
as an allowed next owner:

\[
 \boxed{\kappa_0(S)=m-H+1=(1-o(1))m.}              \tag{2.10}
\]

So current collision-freeness recursively forbids identical-star clusters,
but it does **not** prevent an almost maximal cluster of distinct facets.

This example also identifies the correct weakening.  Only the single
arrival \(y=d\) at carrier \(d\) participates in the heavy target \(S\).
It is harmless to delete one option from each part because \(a\to\infty\).
For an arrival option put

\[
 d(i,y)=
 \sum_{\rho\in\mathcal R_{\rm arr}}
 \bigl(\kappa_\rho(B_{i,\rho}+y)-1\bigr)_+.         \tag{2.11}
\]

For a threshold \(\delta a\), define the truncated bad-option mass

\[
 \mathcal B_\delta
 =\#\{(i,y):d(i,y)>\delta a\}.                      \tag{2.12}
\]

The pruning/LLL argument needs only

\[
 \mathcal B_\delta=o(aN_H)                          \tag{2.13}
\]

for some fixed sufficiently small \(\delta>0\), together with the
condition that only \(o(N_H)\) carriers lose more than half their options.
It does not need \(\max\kappa=o(a/Q)\).  The configuration above has huge
maximum \(\kappa\) but loses only a \(1/a=o(1)\) fraction of its options.

Accordingly the realistic facet-propagation invariant is the **truncated
mass** (2.12), plus residual option density, rather than a uniform maximum
bound.

### 2.3 Exact delayed-choice light cone

The large number \(b=m-Q\) of delayed-departure choices does not mix all
rows in the next round.  Its influence has an exact triangular shape.

Fix one carrier at time zero and, for \(s\le Q\), write

\[
 F_j(s)=L_s\cup\{z_1(s),\ldots,z_j(s)\},
 \qquad 0\le j\le2Q.                                \tag{2.14}
\]

Thus \(j<Q,j=Q,j>Q\) are lower, owner, and upper rows.  Let \(x_0\in L_0\)
be the departure programmed at time zero.  During the first \(s\) shifts,
\(x_0\) is in queue position \(s\).  Consequently

\[
 \boxed{
 F_j(s)\text{ depends on }x_0
 \quad\Longleftrightarrow\quad j<s
 \qquad(1\le s\le Q).}                             \tag{2.15}
\]

When \(j\ge s\), the removal of \(x_0\) from \(L\) is cancelled by its
presence in the queue prefix.  When \(j<s\), it is not restored.  In
particular, no owner or upper-row base can be influenced by \(x_0\) during
these \(Q\) rounds.

If the intervening arrivals and the other programmed departures are fixed
compatibly, then for every affected pair \((s,j)\), \(j<s\), the map

\[
 x_0\longmapsto F_j(s;x_0)                           \tag{2.16}
\]

is injective: the target records which element of the common prospective
set was omitted.  One delayed choice therefore controls

\[
 R_Q:=\sum_{s=1}^{Q}s={Q(Q+1)\over2}                \tag{2.17}
\]

future lower-row flags.

This gives an exact potential-minimization statement.  Give an affected
future flag any nonnegative penalty \(w_{s,j}(x)\) when the programmed
choice is \(x\).  Some \(x\in L_0\) satisfies

\[
 \boxed{
 \sum_{s\le Q}\sum_{j<s}w_{s,j}(x)
 \le {1\over b}
 \sum_{x'\in L_0}\sum_{s\le Q}\sum_{j<s}w_{s,j}(x').}
 \tag{2.18}
\]

Thus delayed-choice averaging gains exactly a factor \(1/b\), but it must
pay for \(R_Q\) future constraints.  At the TRP scale,

\[
 {R_Q\over b}
 =(1+o(1)){Q^2\over2m}
 =(1/2+o(1))(\log\log m+\gamma(m)),                 \tag{2.19}
\]

which diverges.  Generic order-one penalty per affected flag is therefore
not contracted by the delayed choices.

There is also a sharp abstract quota obstruction.  Since \(R_Q>b\) for all
large \(m\), assign the \(b\) elements of \(L_0\) injectively to \(b\) of
the affected pairs, and let \(D_{s,j}\) be the resulting singleton or empty
part.  By injectivity (2.16), declare exactly the targets

\[
 \{F_j(s;x):x\in D_{s,j}\}                          \tag{2.20}
\]

saturated at that future row and time.  Every individual constraint blocks
at most one choice, namely a fraction

\[
 {1\over b}=O(1/m)                                  \tag{2.21}
\]

of the \(b\) available choices, yet their union blocks every
\(x\in L_0\).  These quota sets are adversarial and need not arise from a
balanced TRP history, so this is not a counterexample to TRP.  It proves
that separate per-row concentration estimates, even when every constraint
blocks only an \(O(1/m)\) fraction, cannot establish delayed-choice
propagation.  The residual
quotas must themselves be aligned along the triangular light cones.

## 3. A finite-lookahead path catalogue

Let

\[
 A=(m-Q)(H-Q)
\]

be the outdegree of every carrier state, and let \(\ell\ge1\).  At every
top choose an independent uniform initial state and expose the catalogue
of all \(A^\ell\) directed length-\(\ell\) rotor paths from that state.
Each path option supplies \(\ell\) successor flags in every controlled
row.

Join two path options from distinct carriers when, at any two of their
\(\ell\) times, they use the same target in the same row.  Thus an
independent transversal is globally collision-free throughout the whole
block, not merely separately at equal times.

### Theorem 3.1 (fresh length-\(\ell\) block)

Put

\[
 \Lambda_Q=1+2\sum_{q=1}^{Q}\lambda_q.             \tag{3.1}
\]

If

\[
 \boxed{\ell^2\Lambda_Q/\lambda_H=o(1),}           \tag{3.2}
\]

and \(\ell\le Q+1\),

then there is a deterministic choice of initial states and a subfamily of
\((1-o(1))N_H\) carriers which admits one length-\(\ell\) path per carrier
such that all flags in every controlled row are pairwise distinct across
all retained carriers and all \(\ell\) times.

#### Proof

Write \(P=A^\ell\) for the path-part size.  Fix a row of rank
\(r=m\pm q\), two distinct carriers, and two times in their path options.
Under a uniform initial state and a uniform path option, the state at each
fixed time is uniform, by regularity of the rotor.  The expected number of
path options using a fixed \(S\in\binom Ur\) at a fixed time is therefore

\[
 P/\binom Mr.                                       \tag{3.3}
\]

There are \(\ell^2\) ordered time pairs.  Repeating the containment count
from the one-round theorem gives an expected row-conflict count at most

\[
 {\ell^2P^2N_H^2\over2\binom{2m}r}.                \tag{3.4}
\]

Summing over the controlled rows and dividing twice the edge count by the
total option count \(PN_H\), the expected average conflict degree is at
most

\[
 P\,{\ell^2\Lambda_Q\over\lambda_H}=o(P).          \tag{3.5}
\]

Choose a realization satisfying this estimate.  Delete options of degree
larger than \(\delta P\), where \(\delta=o(1)\) but
\(\ell^2\Lambda_Q/(\delta\lambda_H)=o(1)\).  Only \(o(PN_H)\) options are
deleted.  Delete carriers losing more than \(P/2\) options; only
\(o(N_H)\) carriers are lost.  The remaining parts have size at least
\(P/2\), and the induced conflict graph has maximum degree at most
\(\delta P\).  The symmetric local lemma applies because

\[
 {P^2\over4}\ge e(2\delta P^2+1)                  \tag{3.6}
\]

for all large \(m\).  Its independent transversal is the desired path
family. \(\square\)

There are no hidden same-carrier collisions in this range.  It is useful to
record the exact nonreturn argument.  Write a row flag as

\[
 F_j=L\cup\{z_1,\ldots,z_j\},\qquad 0\le j\le2Q,
\]

where \(j=Q-q,Q,Q+q\) gives the lower, owner, and upper rows.  For
\(j\ge1\), one transition replaces \(z_j\) by the arrival \(y\); for
\(j=0\), it replaces the chosen \(x\) by \(y\).  To return to the old set,
the removed element must reenter from \(R\), while \(y\) must leave the
row.  For \(j\ge1\), these require at least \(2Q-j+2\) and \(j+2\)
states, respectively.  Their maximum is at least \(Q+2\).  For \(j=0\),
the removed \(x\) must traverse the whole queue and likewise cannot
reenter before state \(2Q+2\).  Thus no controlled row repeats during
\(Q+1\) successive transitions.  The independent transversal therefore
is also collision-free within each selected carrier path.

For the TRP parameters, the Gaussian endpoint sum is

\[
 \boxed{
 \sum_{q=1}^{Q}\lambda_q
 =\Theta\!\left({m\over Q}\lambda_Q\right).}       \tag{3.7}
\]

Indeed, uniformly for \(q\le Q=o(m^{2/3})\),

\[
 \log\lambda_q={q^2\over m}+o(1).
\]

Writing \(q=Q-s\), the ratio \(\lambda_{Q-s}/\lambda_Q\) is bounded
above and below by constant multiples of \(\exp(-2Qs/m)\) throughout the
terminal window \(s=O(m/Q)\).  This window contributes
\(\Theta((m/Q)\lambda_Q)\), and the preceding geometric tail is no larger.

Consequently

\[
 \Lambda_Q=\Theta\!\left({m\over Q}\lambda_Q\right),
 \qquad \lambda_H\sim m,
\]

while

\[
 \lambda_Q
 =\exp(Q^2/m+o(1))=(\log m)^{1+o(1)}.              \tag{3.8}
\]

Thus (3.2) is equivalent up to constants to

\[
 \ell=o\!\left(\sqrt{Q\over\lambda_Q}\right),    \tag{3.9}
\]

which is (0.3).

This range is \(o(Q)\), so the auxiliary hypothesis \(\ell\le Q+1\) is
automatic.

## 4. Quantitative failure of direct temporal iteration

Theorem 3.1 identifies the exact loss in the fresh-catalogue LLL.  One
path option has \(\ell\) occurrences in each row, so two path options have
\(\ell^2\) possible cross-time collisions.  Consequently the normalized
conflict parameter is

\[
 \eta_\ell
 =\ell^2{\Lambda_Q\over\lambda_H}.                \tag{4.1}
\]

For one round,

\[
 \eta_1={\Lambda_Q\over\lambda_H}=o(1),            \tag{4.2}
\]

which is the fresh-round theorem.  At the full required horizon
\(\ell=M\sim m\),

\[
 \eta_M
 \ge {M^2\lambda_Q\over\lambda_H}
 \asymp m\lambda_Q\longrightarrow\infty.           \tag{4.3}
\]

Hence neither pruning a vanishing option fraction nor the symmetric local
lemma can select full paths from the raw catalogue.

One might split the horizon into blocks of length satisfying (3.8).
However the endpoint distribution of the selected block is conditioned by
all its collision-avoidance events.  Theorem 3.1 gives no bound on the
endpoint facet congestion (2.2), nor on alignment with residual quotas.
The common-star theorem shows what can go wrong for arbitrary endpoints;
the adjacent-depth identities show that equality collisions themselves are
not the issue.  What is missing is precisely a conditional estimate of the
form

\[
 \#\left\{(i,y):
 \sum_\rho
 \bigl(\kappa^{\rm next}_\rho
 (B^{\rm next}_{i,\rho}+y)-1\bigr)_+
 >\delta(H-Q)
 \right\}
 =o((H-Q)N_H)                                       \tag{4.4}
\]

after each selected block, together with positive residual column density.
Section 2.2 proves that replacing (4.4) by a maximum bound would be false.

This is a second-order, history-dependent statement.  Uniform one-time
marginals do not imply it, and current flag distinctness gives only the
weak worst-case bound \(O(Qm)\).  Therefore the exact remaining temporal
gate is:

> **TRP facet-propagation theorem.** Select each block so that its flags
> respect residual balanced quotas and its endpoint carrier states retain
> the truncated facet-congestion invariant (2.12)--(2.13), with total
> exceptional carrier-round count \(o(MN_H/Q)\).

The finite-lookahead theorem proves this at time zero for blocks satisfying
(3.9).  No argument here propagates it through \(M\) rounds.

## 5. The LLL distribution is not the main source of temporal bias

One possible concern is that conditioning the product choice on being an
independent transversal may by itself destroy all endpoint
quasirandomness.  In the sparse regime this is not the obstruction.

Consider carrier parts of sizes between \(A/2\) and \(A\), and a conflict
graph of maximum degree at most \(\delta A\).  Choose one option uniformly
and independently from every part.  A conflict-edge event has probability
at most

\[
 p={4\over A^2},                                    \tag{5.1}
\]

and is dependent on at most

\[
 d\le2\delta A^2                                    \tag{5.2}
\]

other conflict events.  For sufficiently small fixed \(\delta\), the
symmetric local lemma holds with witness

\[
 x={8\over A^2}.                                    \tag{5.3}
\]

The standard conditional form of the local lemma says that for any event
\(E\),

\[
 \Pr(E\mid\hbox{no conflict})
 \le \Pr(E)
 \prod_{B\sim E}(1-x)^{-1}.                         \tag{5.4}
\]

For completeness, (5.4) follows by the usual induction on a set of bad
events: expose the events not adjacent to \(E\), apply the local-lemma
witness inequality to the adjacent ones, and divide the resulting upper
bound for \(\Pr(E\cap\bigcap\bar B)\) by the corresponding lower bound for
\(\Pr(\bigcap\bar B)\).

If \(E\) depends on at most \(k\) carrier parts, it is adjacent to at most
\(kA(\delta A)\) bad events.  Therefore

\[
 \boxed{
 \Pr(E\mid\hbox{no conflict})
 \le e^{16k\delta+o(1)}\Pr(E).}                    \tag{5.5}
\]

In particular, every nonnegative statistic which is a sum of terms
depending on at most two selected carriers has conditioned expectation at
most

\[
 e^{32\delta+o(1)}                                  \tag{5.6}
\]

times its product-measure expectation.

For a fresh round, write

\[
 \eta={\Lambda_Q\over\lambda_H}=o(1).              \tag{5.7}
\]

The average option degree is \(O(\eta A)\).  Prune at threshold
\(\delta A\) with \(\delta=\sqrt\eta\).  Only \(O(\sqrt\eta)\) of the
options, and hence only \(O(\sqrt\eta)\) of the carrier parts after the
usual half-part deletion, are exceptional.  Equation (5.6) is then a
\(1+o(1)\) distortion bound for all pairwise endpoint statistics.

Thus sparse LLL conditioning can preserve a pairwise quasirandom estimate
that is already known under the product transition kernel.  What is absent
is a closed product-kernel drift inequality for the facet potential.

### 5.1 Exact continuation-energy hierarchy

Let \(\Phi_1(\Omega)\) be the total conflict-edge count in the one-step
option catalogue of a deterministic carrier-state ensemble \(\Omega\).
For \(h\ge2\), let \(\Phi_h(\Omega)\) count, with multiplicity, collisions
between two length-\(h\) continuation options at any specified pair of
future times and in any controlled row.  Equivalently, it is the weighted
conflict count used in the proof of Theorem 3.1.

If one independent uniform transition is taken at every carrier, then the
expected one-step conflict energy of the endpoint ensemble is a normalized
tail of \(\Phi_2\):

\[
 \mathbb E_{\rm prod}\Phi_1(\Omega_1)
 ={1\over A^2}\Phi^{\rm tail}_2(\Omega),            \tag{5.8}
\]

where \(\Phi^{\rm tail}_2\) retains the collision pairs belonging to the
second continuation step.  More generally,

\[
 \mathbb E_{\rm prod}\Phi_h(\Omega_1)
 ={1\over A^2}\Phi^{\rm tail}_{h+1}(\Omega).        \tag{5.9}
\]

These identities are immediate by grouping length-\((h+1)\) path pairs
according to their first transition pair.

Consequently a bound on \(\Phi_1\) alone gives no product-kernel drift
bound for \(\Phi_1\); one needs \(\Phi_2\).  Propagating that bound needs
\(\Phi_3\), and so on.  The fresh uniform ensemble supplies the complete
hierarchy, but its normalized size at horizon \(h\) is exactly of order

\[
 h^2\Lambda_Q/\lambda_H,                            \tag{5.10}
\]

the parameter already isolated in (4.1).  The hierarchy ceases to be
sparse at the scale in Theorem 3.1 and is overwhelmingly nonsparse by
h=M\).

This locates the temporal failure precisely:

* LLL conditioning costs only \(1+o(1)\) on pair statistics in one sparse
  round;
* delayed choices do not close the drift, because they have the triangular
  light cone of Section 2.3;
* closing the drift by raw lookahead recreates the \(h^2\) horizon loss.

A successful proof must therefore find a new potential whose product-kernel
drift closes at bounded order, or exploit aligned residual quotas so that
the full continuation hierarchy telescopes rather than accumulates.

## 6. Abstract temporal quotas can be scheduled through all \(M\) rounds

There is a stronger all-round theorem if only the rotor-adjacency condition
between consecutive states is removed.  It shows that residual quota
alignment and one-state-per-top-per-round scheduling are not independent
obstructions.

Use the integral balanced top-rooted flag flow: there are exactly \(M\)
nested flag columns assigned to every top, hence \(T=MN_H\) columns in
total, and at every controlled rank \(r\) each target has total load

\[
 b_r(S)\in
 \left\{\left\lfloor{T\over N_r}\right\rfloor,
              \left\lceil{T\over N_r}\right\rceil\right\}.
 \tag{6.1}
\]

Every nested column inside one top is a legitimate radius-\(Q\) carrier
state.  What is not known is whether the \(M\) states belonging to one top
can be ordered as one rotor path.

Independently at every top, uniformly permute its \(M\) columns into time
slots \(1,\ldots,M\).  Thus every round contains exactly one state from
every top.

### Theorem 6.1 (all-round abstract flag schedule)

There is such a schedule for which the total number of same-round collision
pairs, summed over all controlled ranks and all \(M\) rounds, is

\[
 \boxed{O(W\lambda_Q/Q)=o(W).}                     \tag{6.2}
\]

Consequently marking \(o(W)\) scheduled state columns leaves all unmarked
columns pairwise distinct in every controlled row of every round.  The
original, undeleted schedule retains the exactly balanced total rank loads
from (6.1).

#### Proof

Fix a rank \(r\) and a target \(S\) of total multiplicity \(b_r(S)\).
Two occurrences owned by the same top are automatically placed in distinct
rounds.  Two occurrences owned by different tops have independent uniform
time slots and coincide with probability \(1/M\).  Hence the expected
number of same-round pairs at \(S\) is at most

\[
 {1\over M}\binom{b_r(S)}2.                        \tag{6.3}
\]

Write

\[
 K_r=\left\lceil{T\over N_r}\right\rceil.
\]

Since \(b_r(S)\le K_r\) and \(\sum_Sb_r(S)=T\),

\[
 \sum_S\binom{b_r(S)}2
 \le {K_r-1\over2}T.                               \tag{6.4}
\]

The expected collision count in that rank is therefore at most

\[
 {T(K_r-1)\over2M}
 ={N_H(K_r-1)\over2}.                              \tag{6.5}
\]

At the owner rank \(K_m=1\), so the contribution is zero.  At ranks
\(m\pm q\),

\[
 K_{m\pm q}\le\lambda_q+1.
\]

Summing (6.5) over both sides of the controlled band and using (3.7),

\[
\begin{aligned}
 \mathbb E C
 &\le O\left(N_H\sum_{q=1}^{Q}\lambda_q\right)\\
 &=O\left({W\over m}{m\over Q}\lambda_Q\right)
 =O(W\lambda_Q/Q)=o(W),                            \tag{6.6}
\end{aligned}
\]

because \(\lambda_Q=(\log m)^{1+o(1)}\) while
\(Q=\sqrt{m\log\log m+o(m\log\log m)}\).
Some deterministic schedule attains this bound.

For every target in every round retain one of its occurrences and mark the
others.  The number marked is at most the number of collision pairs, since
\(d-1\le\binom d2\).  Mark every state column carrying a marked occurrence.
At most \(C=o(W)\) columns are marked, and all unmarked columns are pairwise
distinct in every row of every round. \(\square\)

The columns should not actually be deleted from the balanced schedule: a
literal deletion could lose one flag in every row and introduce an unwanted
factor \(Q\).  The marked columns are an \(o(W)\) exceptional set only for
the purpose of the temporal quasirandom invariant.  The undeleted schedule
retains every state column and hence every balanced total quota; no deletion
is needed for TRP coverage.

The theorem resolves, outside the rotor constraint:

1. exact balanced residual quotas through all \(M\) rounds;
2. one state per carrier in every round;
3. simultaneous per-round row collision mass \(o(W)\).

The sole missing compatibility is now stark.  For each top, the random
permutation of its \(M\) balanced states is almost never a directed rotor
path.  The dynamic TRP theorem asks for the balanced flag flow and the
all-round schedule to be chosen so that all \(M-1\) consecutive pairs at
every top are legal rotor successors, while preserving the global
\(o(W)\) collision ledger.  This is an integral path-factorization problem,
not a marginal quota or temporal coloring problem.

### 6.2 Oriented balance propagates the truncated facet invariant

The preceding schedule balances the flags themselves.  There is a natural
one-step strengthening which also resolves the facet-congestion invariant
through all rounds.

For a state column \(c\), a row \(\rho\in\mathcal R_{\rm arr}\), and a
target \(S\) in the successor rank, say that \(c\) **offers** \(S\) when

\[
 B_\rho(c)\subset S,
 \qquad S\setminus B_\rho(c)\in R(c).              \tag{6.7}
\]

Thus every column offers exactly \(a=H-Q\) targets in each
arrival-controlled row.  Across the complete multiset of \(T\) columns put

\[
 D_\rho(S)=\#\{c:c\text{ offers }S\}.              \tag{6.8}
\]

The symmetric fractional value is

\[
 {aT\over N_\rho}.                                  \tag{6.9}
\]

Assume the abstract state resolution has, for one absolute constant \(C\),

\[
 \boxed{
 D_\rho(S)\le C{aT\over N_\rho}
 \quad\hbox{for every }\rho,S.}                    \tag{OB}
\]

This is an oriented one-step balance condition; it is stronger than the
balanced flag marginals (6.1).

The proof needs only the weaker factorial-energy condition

\[
 \boxed{
 \sum_{\rho\in\mathcal R_{\rm arr}}
 \sum_S\binom{D_\rho(S)}2
 \le C a^2T\Lambda_Q.}                             \tag{OB2}
\]

Indeed (OB) implies (OB2), because
\(\sum_SD_\rho(S)=aT\) and

\[
 \sum_S\binom{D_\rho(S)}2
 \le {\max_SD_\rho(S)\over2}\,aT
 =O\left({a^2T^2\over N_\rho}\right).
\]

Condition (OB2) is the natural oriented collision baseline and permits a
small family of highly congested targets.

### Theorem 6.2 (all-round truncated-congestion schedule)

Under (OB2), the independent random permutation of the \(M\) columns at
every top has a deterministic realization for which:

1. the total same-round flag collision count is \(o(W)\), as in Theorem
   6.1;
2. after deleting high-conflict arrival options, only \(o(W)\)
   carrier-rounds lose more than half of their \(a\) options;
3. on every remaining carrier-round, the pruned arrival conflict graph has
   maximum degree \(\delta a\), where
   \(\delta=o(1)\), and hence admits a simultaneous rowwise independent
   transversal by the local lemma (not necessarily one landing on the
   column scheduled in the following round).

#### Proof

For a fixed \(\rho,S\), let \(\kappa_{t,\rho}(S)\) be the number of columns
scheduled at time \(t\) which offer \(S\).  Two offering occurrences owned
by different tops occupy the same round with probability \(1/M\), while
two from one top never do.  Therefore

\[
 \mathbb E\sum_{t=1}^{M}
 \binom{\kappa_{t,\rho}(S)}2
 \le {1\over M}\binom{D_\rho(S)}2.                \tag{6.10}
\]

Sum over \(\rho,S\) and use (OB2).  The left side counts conflict edges
between arrival options.  Hence

\[
 \mathbb E E_{\rm arr}
 \le {1\over M}
 \sum_{\rho,S}\binom{D_\rho(S)}2
 =O\left({a^2T\over M}\Lambda_Q\right).            \tag{6.11}
\]

There are exactly \(aT\) arrival option-round pairs.  Hence their expected
average conflict degree is

\[
 O\left(a{\Lambda_Q\over M}\right).                \tag{6.12}
\]

By (3.7),

\[
 \zeta:={\Lambda_Q\over M}
 =\Theta(\lambda_Q/Q)=o(1).                        \tag{6.13}
\]

Choose \(\delta=\sqrt\zeta\).  In a realization satisfying (6.12), the
number of options of degree larger than \(\delta a\) is
\(O(\sqrt\zeta\,aT)=o(aT)\).  Mark every carrier-round which loses more
than \(a/2\) options.  There are only
\(O(\sqrt\zeta\,T)=o(W)\) marked carrier-rounds.  Every unmarked part has
size at least \(a/2\), and the pruned conflict graph has maximum degree
\(\delta a\).  Since \(\delta=o(1)\), the local-lemma inequality

\[
 {a^2\over4}\ge e(2\delta a^2+1)                  \tag{6.14}
\]

holds eventually.  This proves the second and third assertions.  Intersect
this positive-probability choice of schedule with the expectation bound in
Theorem 6.1 (or minimize the sum of the two nonnegative ledgers) to obtain
both assertions simultaneously. \(\square\)

Theorem 6.2 is an all-round **state-ensemble** propagation theorem,
conditional on the static oriented resolution (OB2) and still without rotor
adjacency.  It certifies a good one-step transition system from almost every
scheduled carrier-round, but it does not certify that those transitions
land on the independently scheduled next columns.
It cleanly separates three levels:

* balanced flag marginals give exact TRP coverage abstractly;
* oriented collision balance (OB2) gives all-round truncated facet
  quasirandomness;
* legal rotor adjacency between the scheduled columns is the remaining
  dynamical compatibility.

The uniform fractional state measure satisfies (OB2) at its natural
baseline.  No integral theorem is presently proved which combines (OB2), the balanced
flag loads, exactly \(M\) columns per top, and one directed rotor path per
top.
