# Annular shared-leave repeat excess: exact fresh-target drift, synchronized greedy criterion, and the PBBS corridor gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad r=m-q_0,\qquad
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),
\]

where \(0<a<b\) are fixed.  Write

\[
 W=\binom{2m}{m}.
\]

Put \(J=H-q_0\).  At annular depth
\(d\), write

\[
 V_d=\binom{[n]}{r-d},\qquad N_d=|V_d| \qquad(0\le d\le J).
\]

The conclusions are as follows.

1. There is an exact synchronized one-step identity which is sharper
   than quadratic or higher falling-moment energy.  If \(t\) cyclic
   packets have already been selected, \(G_t=nt\) is their occurrence
   mass at every depth, \(H_{d,t}\) is the number of depth-\(d\) holes,
   and a legal next packet \(e\) hits \(Z_{d,t}(e)\) of those holes, then

   \[
   \boxed{
   \widetilde E_{d,t+1}-\widetilde E_{d,t}
    =c_{d,t}-Z_{d,t}(e),}
   \tag{0.1}
   \]

   where

   \[
   c_{d,t}=(N_d-G_t)_+-(N_d-G_t-n)_+
           =\min\{n,(N_d-G_t)_+\}.
   \tag{0.2}
   \]

   Consequently

   \[
   \boxed{
   \sum_{d=0}^{J}\widetilde E_{d,s}
   =\sum_{t=0}^{s-1}
      \left(\sum_{d=0}^{J}c_{d,t}
             -\sum_{d=0}^{J}Z_{d,t}(e_{t+1})\right).}
   \tag{0.3}
   \]

   This is an equality, with the integer floor already subtracted.

2. Formula (0.3) gives a deterministic conditional-expectation theorem.
   If at every stage there is a probability distribution on extendible
   legal next packets whose expected aggregate fresh-target score is at
   least

   \[
       \sum_d c_{d,t}-\varepsilon_t,
   \]

   then one may choose a single legal packet at that stage so that

   \[
       \sum_d\widetilde E_{d,s}\le\sum_t\varepsilon_t.
   \tag{0.4}
   \]

   Thus \(\sum_t\varepsilon_t=o(W)\) is an exact sufficient
   synchronized process theorem.  No rankwise nibble occurs in this
   statement.

3. At the critical size \(s=(1+o(1))N_0/n=\Theta(W/n)\), condition
   (0.4) permits average deficit only \(o(n)\) per chosen packet.  While
   \(\Theta(\sqrt m)\) depths remain below their scalar saturation
   points, a packet has \(\Theta(n\sqrt m)\) relevant target slots.
   Hence the required average *net* fresh-score deficit, relative to that
   benchmark, is \(o(m^{-1/2})\).  Raw collisions at unsaturated depths
   may be offset by filling holes at already saturated depths; the exact
   signed form is (2.7) below.

4. An unbiased packet law has the wrong drift.  In the complete cyclic
   catalogue,

   \[
      \mathbb E Z_{d,t}(e)=\frac{nH_{d,t}}{N_d}.
   \tag{0.5}
   \]

   Even at an ideal unsaturated state
   \(H_{d,t}=N_d-G_t\) and \(G_t\le N_d-n\), its expected one-step
   excess is

   \[
      c_{d,t}-\mathbb E Z_{d,t}(e)
      =\frac{nG_t}{N_d}.
   \tag{0.6}
   \]

   This is order \(n\), not \(o(n)\), when \(G_t=\Theta(N_d)\).
   Ordinary local pseudorandomness therefore drives the Poisson regime;
   it does not prove (0.4).

5. The domino-twin catalogue is an exact obstruction to deriving the
   missing drift from entrance legality or entrance degree/codegree data.
   Its second component is entrance-disjoint from its first but incurs
   fresh-target deficit exactly \(n/2\) at the first deeper rank.  A
   critical near-factor by such atoms would have

   \[
      \widetilde E_1\ge(1/4-o(1))N_0=\Theta(W).
   \tag{0.7}
   \]

6. The corrected lower PBBS windows do have a strong simultaneous feature:
   their correct-start domains are nested in the depth, and the full
   corrected lower deck has zero floor-correct excess at each depth
   separately.
   They nevertheless do not supply (0.4).  To use one constant-mass set
   of PBBS starts throughout \([q_0,H]\), all chosen starts must lie in
   the deepest correct domain.  The audited PBBS support theorem neither
   proves that this domain projects onto almost all entrance targets nor
   proves the first two-level Hall condition.  Moreover PBBS starts are
   not grouped into literal cyclic packets.  The exact first missing
   condition is displayed in Section 6.

7. After dropping the one-common-factor requirement, the nested quota
   problem is exactly solvable.  Hall-surjective facet maps give one
   all-depth lower flag per entrance target with zero excess, and on the
   even ground set a perfect lower/upper entrance pairing plus lower and
   upper surjections gives a two-sided strongly geodesic atlas with

   \[
      \widetilde E_q^- =\widetilde E_q^+=0
      \qquad(q_0\le q\le H).
   \]

   Every lower flag is realizable in some coordinate conjugate of PBBS.
   The conjugate and path depend on the entrance target, so this is an
   integral atlas but not one exact middle factor or a literal packet
   family.

Thus the shared scalar leave is fully synchronized, but the repeat term
is not automatic.  The exact positive route is the fresh-target drift
(0.4).  The PBBS corridor is an abstract nested support certificate, not
yet a legal process satisfying that drift.

## 1. Loads, holes, and the exact integer floor

For a cyclic packet \(e\), let \(e_d\subset V_d\) be its deck of the
\(n\) cyclic intervals of length \(r-d\).  These \(n\) targets are
distinct.  Let

\[
 e_1,e_2,\ldots,e_s
\tag{1.1}
\]

be an entrance matching, meaning that the decks \((e_t)_0\) are pairwise
disjoint.  After the first \(t\) packets define

\[
 \mu_{d,t}(T)=|\{j\le t:T\in(e_j)_d\}|,
 \qquad G_t=nt,
\tag{1.2}
\]

\[
 H_{d,t}=|\{T\in V_d:\mu_{d,t}(T)=0\}|,
 \qquad
 E_{d,t}=\sum_{T\in V_d}(\mu_{d,t}(T)-1)_+.
\tag{1.3}
\]

The occurrence identity \(\sum_T\mu_{d,t}(T)=G_t\) gives

\[
 E_{d,t}=G_t-N_d+H_{d,t}.
\tag{1.4}
\]

Subtract the forced repeat floor:

\[
 \widetilde E_{d,t}
 =E_{d,t}-(G_t-N_d)_+.
\tag{1.5}
\]

Then (1.4) is equivalent to the exact shared-leave identity

\[
 \boxed{
 \widetilde E_{d,t}=H_{d,t}-(N_d-G_t)_+.}
\tag{1.6}
\]

Equivalently, if
\(K_{d,t}=|\{T:\mu_{d,t}(T)>0\}|=N_d-H_{d,t}\), then

\[
 \boxed{
 \widetilde E_{d,t}=\min\{N_d,G_t\}-K_{d,t}.}
\tag{1.7}
\]

This formula covers both regimes.  Before scalar saturation, excess
repeats equal holes beyond the forced leave; after saturation, excess
repeats equal holes themselves.

## 2. The zeroth-factorial Lyapunov identity

For a legal next packet \(e\), put

\[
 Z_{d,t}(e)=|e_d\cap\{T:\mu_{d,t}(T)=0\}|.
\tag{2.1}
\]

Because \(e_d\) has no repeated target,

\[
 H_{d,t+1}=H_{d,t}-Z_{d,t}(e).
\tag{2.2}
\]

Also put

\[
 c_{d,t}=(N_d-G_t)_+-(N_d-G_t-n)_+.
\tag{2.3}
\]

### Theorem 2.1 (exact synchronized fresh-target drift)

Equations (0.1) and (0.3) hold for every ordered entrance matching.

#### Proof

Subtract (1.6) at times \(t+1\) and \(t\), use (2.2), and note that
\(G_{t+1}=G_t+n\).  This gives

\[
 \widetilde E_{d,t+1}-\widetilde E_{d,t}
 =-Z_{d,t}(e)+c_{d,t}.
\]

At time zero both sides of (1.6) vanish.  Sum over \(t\) and \(d\) to
obtain (0.3). \(\square\)

The two sides telescope separately:

\[
 \sum_{t=0}^{s-1}c_{d,t}=\min\{N_d,G_s\},\qquad
 \sum_{t=0}^{s-1}Z_{d,t}(e_{t+1})=K_{d,s}.
\tag{2.3a}
\]

Thus (0.3) is also the incremental form of the exact support deficit
(1.7).

The terminology “zeroth-factorial” refers to
\(H_{d,t}=\sum_T1_{\{\mu_{d,t}(T)=0\}}\).  Unlike quadratic pair energy,
it is not merely a sufficient surrogate: after the scalar floor is
subtracted, it is exactly the desired objective.

For comparison, the higher falling moments

\[
 F^{(j)}_{d,t}=\sum_T(\mu_{d,t}(T))_j
\]

obey

\[
 F^{(j)}_{d,t+1}-F^{(j)}_{d,t}
 =j\sum_{T\in e_d}(\mu_{d,t}(T))_{j-1}.
\tag{2.4}
\]

They may help certify a candidate distribution, but they do not improve
the exact terminal ledger (1.6).

There is a useful signed reformulation.  Let

\[
 \mathcal O_{d,t}=\{T:\mu_{d,t}(T)>0\},\qquad
 C_{d,t}(e)=|e_d\cap\mathcal O_{d,t}|=n-Z_{d,t}(e).
\tag{2.5}
\]

Partition the depths according to the position of the next scalar step:

\[
 \mathcal U_t=\{d:G_t+n\le N_d\},\qquad
 \mathcal S_t=\{d:N_d\le G_t\},
\tag{2.6}
\]

and let \(\mathcal B_t=\{d:G_t<N_d<G_t+n\}\).  Direct substitution in
(0.1) gives

\[
\boxed{
 \begin{aligned}
 \sum_d(\widetilde E_{d,t+1}-\widetilde E_{d,t})
 ={}&\sum_{d\in\mathcal U_t} C_{d,t}(e)\\
 &+\sum_{d\in\mathcal B_t}
   \bigl(C_{d,t}(e)-(G_t+n-N_d)\bigr)\\
 &-\sum_{d\in\mathcal S_t} Z_{d,t}(e).
 \end{aligned}}
\tag{2.7}
\]

Thus the precise synchronized mechanism is collision-to-hole
compensation: collisions before scalar saturation are debits, fresh holes
filled after saturation are credits, and the boundary depth pays only
collisions above its newly forced repeat floor.  Since \(N_d\) is strictly
decreasing, \(\mathcal U_t\), \(\mathcal B_t\), and \(\mathcal S_t\) occur
in this order along the annulus.  In the Gaussian range
\(N_d-N_{d+1}\gg n\), so \(|\mathcal B_t|\le1\) for all sufficiently
large \(m\).

## 3. A deterministic synchronized selection theorem

Call a packet \(e\) *legal at time \(t\)* if its entrance deck is
disjoint from the entrance decks already selected.  Fix a desired final
size \(s\).  Call it *extendible* if, after adding it, the current partial
matching is contained in some entrance matching of size \(s\).

### Theorem 3.1 (conditional-expectation fresh-score theorem)

Suppose that for every extendible partial entrance matching of size
\(t<s\) there is a probability distribution \(\pi_t\), supported on
packets which are legal there and leave an extendible state, such that

\[
 \mathbb E_{e\sim\pi_t}
    \sum_{d=0}^{J}Z_{d,t}(e)
 \ge
 \sum_{d=0}^{J}c_{d,t}-\varepsilon_t,
 \qquad \varepsilon_t\ge0.
\tag{3.1}
\]

Then there is an entrance matching of size \(s\) satisfying (0.4).

#### Proof

Some packet in the support of \(\pi_t\) has fresh score at least its
mean.  Choose such a packet.  Extendibility guarantees that the induction
can continue.  Apply (0.3) and sum (3.1). \(\square\)

The theorem remains true with lower and upper target decks included as
separate indices.  It also applies to a random decision tree when (3.1)
holds at every node in its support and every positive-probability child
remains in that support; choosing a child with score at least the
conditional mean then gives the same deterministic induction.  A
time-zero expectation alone is not sufficient.

At critical leave

\[
 ns=N_0-O(N_0/\sqrt m),
 \qquad s=\Theta(W/n).
\tag{3.2}
\]

Therefore \(\sum_t\varepsilon_t=o(W)\) requires

\[
 \frac1s\sum_t\varepsilon_t=o(n).
\tag{3.3}
\]

Before a given depth saturates, \(c_{d,t}=n\), except possibly in its
single final partial step.  When \(\Theta(\sqrt m)\) depths are active,
the benchmark in (3.1) is \(\Theta(n\sqrt m)\).  Thus (3.3) is a
relative aggregate error \(o(m^{-1/2})\), not merely an \(o(1)\) error.

## 4. Why an unbiased packet process misses the benchmark

Choose a uniformly random cyclic packet from the complete catalogue,
temporarily ignoring entrance conflicts.  Every target in \(V_d\) occurs
in the same number of packets and every packet has \(n\) depth-\(d\)
targets.  Hence

\[
 \Pr(T\in e_d)=\frac n{N_d}
\]

and (0.5) follows by summing over the hole set.

If the state is floor-perfect and unsaturated, then

\[
 H_{d,t}=N_d-G_t,
 \qquad c_{d,t}=n
\]

provided \(G_t\le N_d-n\).  Substitution proves (0.6).  Thus ordinary
uniformity repels neither previously occupied targets nor their nested
descendants strongly enough.

The terminal calculation says the same thing.  For \(s\) independent
uniform packets,

\[
 \mathbb E H_{d,s}
 =N_d\left(1-\frac n{N_d}\right)^s.
\tag{4.1}
\]

If \(G_s/N_d\to\lambda\in(0,\infty)\), then

\[
 \frac1{N_d}\mathbb E\widetilde E_{d,s}
 \longrightarrow
 \begin{cases}
 e^{-\lambda}-1+\lambda,&0<\lambda\le1,\\
 e^{-\lambda},&\lambda\ge1.
 \end{cases}
\tag{4.2}
\]

Both expressions are positive for fixed \(\lambda>0\), apart from the
trivial limit \(\lambda\downarrow0\).  At a macroscopic Gaussian annular
depth, \(N_d=\Theta_{a,b}(W)\) and \(\lambda=\Theta_{a,b}(1)\).  Hence
an unbiased process has \(\Theta(W)\) excess at one depth and
\(\Theta(W\sqrt m)\) across a positive fraction of the annulus.

Entrance conditioning can change (4.1), but entrance matching alone does
not force the favorable change.  The next section gives an exact literal
reason.

## 5. Twin obstruction and convex-potential toll

Assume the entrance rank \(r\) is odd.  For a cyclic order \(P\), let
\(P^\tau\) be obtained by swapping every consecutive position pair.  The
audited domino-twin identities are

\[
 P_0\cap(P^\tau)_0=\varnothing,
 \qquad
 |P_1\cap(P^\tau)_1|=\frac n2.
\tag{5.1}
\]

In fact, throughout the annulus the complete parity-resolved table is

\[
 |P_d\cap(P^\tau)_d|
 =\begin{cases}
 0,&d\text{ even},\\
 n/2,&d\text{ odd},
 \end{cases}
\tag{5.1a}
\]

because the interval length \(r-d\) is even exactly when \(d\) is odd.

After selecting \(P\), every member of \((P^\tau)_1\) outside this
intersection is fresh.  Since \(N_1\) is exponential and \(2n<N_1\),
the scalar benchmark for the second packet is \(c_{1,1}=n\), whereas

\[
 Z_{1,1}(P^\tau)=n-\frac n2=\frac n2.
\tag{5.2}
\]

Thus the second legal packet incurs fresh-score deficit exactly \(n/2\)
at this depth.

More strongly, immediately after \(P\), all annular scalar benchmarks are
still \(n\), and (5.1a) gives

\[
 \sum_{d=0}^{J}\bigl(c_{d,1}-Z_{d,1}(P^\tau)\bigr)
 =\frac n2\left\lfloor\frac{J+1}{2}\right\rfloor
 =\Theta_{a,b}(n\sqrt m).
\tag{5.2a}
\]

This disproves any *statewise* synchronized fresh-score lower bound based
on entrance legality alone.  Later packets can in principle repair this
early deficit, so (5.2a) by itself is not a final critical-leave lower
bound; the conditional final obstruction is (5.4).

More generally, let \(\varphi:\mathbb Z_{\ge0}\to\mathbb R\) be a
separable convex load potential.  Relative to a second depth-one deck
disjoint from the first, the twin second deck pays exactly

\[
 \frac n2\bigl(\varphi(2)+\varphi(0)-2\varphi(1)\bigr)
 =\frac n2\Delta^2\varphi(0).
\tag{5.3}
\]

Thus changing from holes to a strictly convex polynomial, entropy, or
falling-moment potential does not make the twin disappear.  Such a
potential merely records its linear toll in another coordinate system.

If \(T\) entrance-disjoint twin superpackets are selected, their internal
depth-one duplicates imply

\[
 \widetilde E_1
 \ge \frac{nT}{2}-(2nT-N_1)_+.
\tag{5.4}
\]

At critical entrance leave \(2nT=N_0-O(N_0/\sqrt m)\),

\[
 N_0-N_1
 =N_0\frac{n-2r+1}{n-r+1}
 =O_a(N_0/\sqrt m).
\tag{5.5}
\]

Equations (5.4)--(5.5) give (0.7).  Consequently no theorem based only
on entrance regularity, entrance pair codegrees, or entrance
edge-collision energy can establish (3.1) uniformly over locally
favorable packet catalogues.  A positive process for ordinary packets
must actively break these deeper twin correlations.

## 6. What corrected PBBS windows do, and do not, synchronize

This section audits the lower deck on the native PBBS ground set
\([2m+1]\).  On an oriented step-two PBBS component write its middle
states as \(A_i\), and put

\[
 W^+=\binom{2m+1}{m}
 =\frac{2m+1}{m+1}W.
\tag{6.0}
\]

Thus \(o(W)\) and \(o(W^+)\) are equivalent asymptotic requirements.
Put

\[
 I_q(i)=\bigcap_{h=0}^{q}A_{i+2h}.
\tag{6.1}
\]

Call \(i\) correct at depth \(q\) if

\[
 |I_q(i)|=m-q,
\]

and denote the correct domain by \(\Omega_q\).

### Lemma 6.1 (correct domains are nested)

\[
 \boxed{\Omega_{q+1}\subseteq\Omega_q.}
\tag{6.2}
\]

#### Proof

The step-two PBBS transition changes one coordinate.  Hence passing from
\(I_q(i)\) to \(I_{q+1}(i)\) removes at most one coordinate.  Also a
\(q\)-edge Johnson path can remove at most \(q\) coordinates from its
first state, so \(|I_q(i)|\ge m-q\).  If
\(|I_{q+1}(i)|=m-q-1\), the first observation gives
\(|I_q(i)|\le m-q\); the second gives the reverse inequality.  Thus
\(|I_q(i)|=m-q\). \(\square\)

Let

\[
 \mu_q(S)=|\{i\in\Omega_q:I_q(i)=S\}|.
\tag{6.3}
\]

In this section only, write

\[
 \mathcal V_q^{\rm PBBS}=\binom{[2m+1]}{m-q},\qquad
 N_q^{\rm PBBS}=|\mathcal V_q^{\rm PBBS}|.
\tag{6.3a}
\]

The audited global-maximum corridor theorem says

\[
 1\le\mu_q(S)\le\binom{2q+1}{q}
 \qquad
 \left(S\in\binom{[2m+1]}{m-q}\right).
\tag{6.4}
\]

Therefore the full corrected deck has no holes.  If
\(M_q=|\Omega_q|=\sum_S\mu_q(S)\), then necessarily
\(M_q\ge N_q^{\rm PBBS}\), and its repeat count is exactly
\(M_q-N_q^{\rm PBBS}\).  After subtraction of this forced floor,

\[
 \boxed{\widetilde E_q^{\rm PBBS}=0}
\tag{6.5}
\]

at every depth separately.  Equations (6.2) and (6.5) are genuine
simultaneous structure, not independent-depth existence.

They still do not produce the annular packet process.  There are three
exact gaps.

First, the masses \(M_q\) in (6.5) depend on \(q\).  A cyclic packet
family contributes one fixed occurrence mass at every depth.  To use one
set \(\mathcal S\) of PBBS starts throughout \(q_0\le q\le H\), one
must at least take

\[
 \mathcal S\subseteq\Omega_H.
\tag{6.6}
\]

Near-complete entrance coverage would require

\[
 \left|\{I_{q_0}(i):i\in\Omega_H\}\right|
 \ge N_{q_0}^{\rm PBBS}-o(W).
\tag{6.7}
\]

The support theorem at depth \(H\) gives only
\(|\Omega_H|\ge N_H^{\rm PBBS}\).  At Gaussian-separated depths,
\[
 \frac{N_H^{\rm PBBS}}{N_{q_0}^{\rm PBBS}}
 =\exp\left(-\frac{H^2-q_0^2}{m}+o(1)\right)
 =e^{-(b^2-a^2)+o(1)},
\tag{6.7a}
\]
which tends to a constant strictly below one.  Thus (6.7) does not
follow even at the scalar level.

There is nevertheless an exact dropout bound for the unthinned deepest
domain.  Let \(\nu_{q,H}\) be the depth-\(q\) load obtained by retaining
all starts in \(\Omega_H\).  Its occurrence mass is the same number
\(M_H\) at every \(q\le H\).

### Lemma 6.2 (deepest-domain dropout bound)

For every \(q\le H\),

\[
 H_q(\Omega_H)\le M_q-M_H
\tag{6.7b}
\]

and hence

\[
 \boxed{
 \widetilde E_q(\Omega_H)
 \le M_q-M_H-(N_q^{\rm PBBS}-M_H)_+
 =M_q-\max\{N_q^{\rm PBBS},M_H\}.}
\tag{6.7c}
\]

#### Proof

The full domain \(\Omega_q\) covers every depth-\(q\) target.  Passing to
\(\Omega_H\subseteq\Omega_q\) removes exactly \(M_q-M_H\) occurrences.
Every target which becomes a hole consumes at least one removed
occurrence, proving (6.7b).  Apply the exact floor identity (1.6), with
constant mass \(M_H\), and simplify. \(\square\)

Thus

\[
 \sum_{q=q_0}^{H}
 \bigl(M_q-\max\{N_q^{\rm PBBS},M_H\}\bigr)=o(W)
\tag{6.7d}
\]

would be a sufficient abstract all-depth PBBS dropout estimate.  No such
estimate is currently proved, and even (6.7d) would not make the
depth-\(q_0\) targets injective or group the starts into literal packets.

Equivalently, define the correct lifetime

\[
 \ell(i)=\max\{q:i\in\Omega_q\}.
\]

Nestedness gives the exact layer-cake identity

\[
 \boxed{
 \sum_{q=q_0}^{H}(M_q-M_H)
 =\sum_{i\in\Omega_{q_0}\setminus\Omega_H}
   (\ell(i)-q_0+1).}
\tag{6.7e}
\]

Thus retaining only histories which survive to \(H\) converts the
simultaneous PBBS question into a weighted lifetime/dropout estimate,
before either entrance thinning or literalization is attempted.

Second, already for two adjacent depths define a bipartite graph
\(G_q\) with left shore \(\mathcal V_q^{\rm PBBS}\), right shore
\(\mathcal V_{q+1}^{\rm PBBS}\), and an edge
\(S\!\sim\!T\) when some \(i\in\Omega_{q+1}\) has

\[
 I_q(i)=S,\qquad I_{q+1}(i)=T.
\tag{6.8}
\]

Every edge satisfies \(T\subset S\), \(|S\setminus T|=1\).

### Lemma 6.3 (exact first PBBS entrance-Hall gate)

Assume every left vertex of \(G_q\) has a neighbour.  One can choose one
correct PBBS occurrence from every left entrance target and cover every
right target if and only if

\[
 \boxed{|N_{G_q}(U)|\ge|U|
        \quad\text{for every }U\subseteq\mathcal V_{q+1}^{\rm PBBS}.}
\tag{6.9}
\]

#### Proof

Necessity is Hall's condition.  Conversely, Hall gives distinct left
representatives for all right vertices.  Choose the corresponding
occurrence at each used left vertex, then choose an arbitrary occurrence
at every unused left vertex. \(\square\)

More quantitatively, let \(\nu(G_q)\) be the maximum matching size and
put

\[
 \Delta_q^{\rm Hall}
 =\max_{U\subseteq\mathcal V_{q+1}^{\rm PBBS}}
   \bigl(|U|-|N_{G_q}(U)|\bigr).
\tag{6.10}
\]

Then the maximum possible number of covered right targets after choosing
at most one occurrence at each left target is exactly

\[
 \nu(G_q)=N_{q+1}^{\rm PBBS}-\Delta_q^{\rm Hall}.
\tag{6.11}
\]

Indeed, one chosen occurrence per left contains a matching saturating its
covered-right set after retaining one distinct preimage for each covered
right.  Conversely a maximum matching realizes all of its right
endpoints, and the Hall deficiency theorem gives (6.11).  Thus the exact
first quantitative PBBS condition is

\[
 \Delta_q^{\rm Hall}=o(W)
\tag{6.12}
\]

together with \(o(W)\) isolated or deliberately omitted left targets.

The PBBS support theorem proves only that every right vertex has positive
degree.  The Lovasz--Kruskal--Katona Hall theorem applies to the full
facet-containment graph, not automatically to its chronology-restricted
PBBS subgraph \(G_q\).  Thus it does not prove (6.9).

Third, even all the two-level Hall inequalities would not by themselves
select one common PBBS history across all depths.  That is a path-choice
problem in the layered chronology graph.  Moreover the PBBS components
are not already grouped into length-\((2m)\) cyclic packet rows on the
even ground set.  Cutting or regrouping them exposes the previously
audited residence and boundary-window costs.

The exact all-depth lower-deck configuration deficit can be stated
without approximation.  For an integer \(M\), define

\[
 \begin{aligned}
 \mathfrak D_{q_0,H}^{\rm PBBS}(M)
 =\min_{\mathcal S}\sum_{q=q_0}^{H}
 \left(
  \min\{N_q^{\rm PBBS},M\}
  -|\{I_q(i):i\in\mathcal S\}|
 \right),
 \end{aligned}
\tag{6.13}
\]

where the minimum is over \(\mathcal S\subseteq\Omega_H\) with
\(|\mathcal S|=M\) and with the entrance map
\(i\mapsto I_{q_0}(i)\) injective.  If there is no such family, set
\(\mathfrak D_{q_0,H}^{\rm PBBS}(M)=+\infty\).

### Theorem 6.4 (exact PBBS corridor-configuration objective)

For every admissible \(\mathcal S\), the summand in (6.13) is exactly its
floor-correct repeat excess at depth \(q\).  Consequently an abstract
constant-mass, entrance-injective PBBS corridor selection has aggregate
lower repeat excess \(o(W)\) if and only if

\[
 \mathfrak D_{q_0,H}^{\rm PBBS}(M)=o(W)
\tag{6.14}
\]

for some \(M=N_{q_0}^{\rm PBBS}-o(W)\).

#### Proof

The selected occurrence mass is \(M\) at every depth, while the number
of covered targets is
\(C_q=|\{I_q(i):i\in\mathcal S\}|\).  Hence the hole count is
\(N_q^{\rm PBBS}-C_q\).  Subtracting the scalar floor
\((N_q^{\rm PBBS}-M)_+\) gives

\[
 N_q^{\rm PBBS}-C_q-(N_q^{\rm PBBS}-M)_+
 =\min\{N_q^{\rm PBBS},M\}-C_q.
\]

Sum over \(q\). \(\square\)

The variables in (6.13) are whole histories, so this is not a sum of
rankwise matchings.  The two-level Hall conditions are necessary
projections of (6.14), not a proof of it.

If one enlarges from one fixed PBBS factor to the catalogue of **all
coordinate conjugates**, then the lower configuration problem has an
exact solution.  This separates the nested-flag issue from the common-
factor issue.

### Theorem 6.5 (all-conjugate exact lower flag selection)

There is one strict descending flag

\[
 X=X_{q_0}\supset X_{q_0+1}\supset\cdots\supset X_H,
 \qquad |X_q|=m-q,
\tag{6.14a}
\]

for every entrance target
\(X\in\mathcal V_{q_0}^{\rm PBBS}\), such that, for every
\(q_0\le q\le H\), the map \(X\mapsto X_q\) is surjective onto
\(\mathcal V_q^{\rm PBBS}\).  Hence this family is entrance-injective and
has

\[
 \boxed{\widetilde E_q=0\qquad(q_0\le q\le H).}
\tag{6.14b}
\]

Moreover every individual flag (6.14a) is the lower intersection flag of
an \(H\)-correct path in a coordinate conjugate of the canonical PBBS
factor.

#### Proof

For \(1\le k\le m\), consider the facet-containment graph from the
\(k\)-sets on the left to the \((k-1)\)-sets on the right.  If
\(\mathcal U\) is a family on the right, double counting its incidence
edges gives

\[
 k|N(\mathcal U)|
 \ge(n-k+1)|\mathcal U|
 >k|\mathcal U|,
\tag{6.14c}
\]

because here \(n=2m+1\) and \(k\le m\).  Hall therefore gives a matching
saturating the right shore.  Direct the matched left set to its matched
facet and direct every unmatched left set to an arbitrary facet.  This
produces a surjection

\[
 f_k:\binom{[2m+1]}k\longrightarrow
     \binom{[2m+1]}{k-1},
 \qquad f_k(Y)\subset Y.
\tag{6.14d}
\]

Choose such an \(f_k\) for every
\(m-H+1\le k\le m-q_0\), and iterate them from every entrance target.
Compositions of surjections are surjective, proving the first assertion.
The occurrence mass at every depth is
\(M=N_{q_0}^{\rm PBBS}\ge N_q^{\rm PBBS}\), and every target is hit.
Thus repeats equal \(M-N_q^{\rm PBBS}\), exactly the forced floor,
proving (6.14b).

For the PBBS assertion, fix one audited strongly geodesic
\(H\)-step global-maximum PBBS corridor and take all its prefix
intersections.  They form one complete strict flag from rank \(m\) to
rank \(m-H\).  Extend (6.14a) upward arbitrarily from rank \(m-q_0\) to
rank \(m\).  The symmetric group is transitive on complete flags of the
same ranks, so some coordinate permutation carries the fixed PBBS flag
to this extended flag.  Conjugating the PBBS factor and its corridor by
that permutation realizes (6.15). \(\square\)

The conjugating permutation in this proof depends on the entrance target.
Therefore Theorem 6.5 does **not** put the selected histories in one exact
middle factor, does not synchronize the complementary upper flags, and
does not group \(2m\) phase histories into one ordinary cyclic packet.
Those common-frame requirements are precisely what prevents (6.14b) from
being a constant-one construction.

For comparison, on the original even ground set the same Hall idea solves
both signs simultaneously at the level of independent histories.

### Theorem 6.6 (abstract two-sided zero-excess nested atlas)

On \([2m]\), put

\[
 \mathcal V_q^- =\binom{[2m]}{m-q},\qquad
 \mathcal V_q^+ =\binom{[2m]}{m+q},\qquad
 |\mathcal V_q^-|=|\mathcal V_q^+|=N_q.
\tag{6.14e}
\]

There are \(M=N_{q_0}\) strongly geodesic \(H\)-step Johnson paths
\(\Gamma_S=(B_{S,0},\ldots,B_{S,H})\), indexed by
\(S\in\mathcal V_{q_0}^-\), such that

\[
 \bigcap_{t=0}^{q_0}B_{S,t}=S,
\tag{6.14f}
\]

and, for every \(q_0\le q\le H\), both maps

\[
 S\longmapsto\bigcap_{t=0}^{q}B_{S,t},
 \qquad
 S\longmapsto\bigcup_{t=0}^{q}B_{S,t}
\tag{6.14g}
\]

are surjective onto \(\mathcal V_q^-\) and \(\mathcal V_q^+\),
respectively.  At \(q=q_0\) they are bijections, so the abstract atlas
has an exact two-sided entrance matching.  Consequently it has

\[
 \boxed{\widetilde E_q^- =\widetilde E_q^+=0
        \qquad(q_0\le q\le H).}
\tag{6.14h}
\]

#### Proof

The containment graph between \(\mathcal V_{q_0}^-\) and
\(\mathcal V_{q_0}^+\) is regular with equal shores: both degrees equal
\(\binom{m+q_0}{2q_0}\).  It therefore has a perfect matching
\(S\mapsto U(S)\), with \(S\subset U(S)\).

Repeat the proof of (6.14d) on \([2m]\) below the middle to choose strict
lower flags \(L_{S,q}\), starting at \(L_{S,q_0}=S\), which are
surjective at every rank.  Above the middle, the same double count, with
the arrows reversed,
gives surjections from the \(k\)-sets to containing \((k+1)\)-sets for
every \(k\ge m\).  Iterate them from \(U(S)\) to obtain strict upper
flags \(U_{S,q}\), also surjective at every rank.  Containment persists:

\[
 L_{S,q}\subset S\subset U(S)\subset U_{S,q}.
\]

Choose an \(m\)-set \(X_S\) strictly between \(S\) and \(U(S)\).
Order the \(q_0\) elements of \(X_S\setminus S\) as the first deletion
labels and the \(q_0\) elements of \(U(S)\setminus X_S\) as the first
insertion labels.  The later deletion labels are the successive
differences of the lower flag; the later insertion labels are the
successive differences of the upper flag.  These \(2H\) labels are
pairwise distinct.  If they are \(d_1,\ldots,d_H\) and
\(a_1,\ldots,a_H\), define

\[
 B_{S,t}=X_S-\{d_1,\ldots,d_t\}
              +\{a_1,\ldots,a_t\}.
\]

This is a strongly geodesic Johnson path, with lower intersections
\(L_{S,q}\) and upper unions \(U_{S,q}\).  Surjectivity proves complete
support on both shores.  Since \(M=N_{q_0}\ge N_q\), every repeat above
one is forced by the layer-size floor, proving (6.14h). \(\square\)

The paths in Theorem 6.6 are independent.  Their initial owners may
repeat, their successor histories do not form one permutation, and they
are not the phase windows of cyclic packets.  The theorem proves that
integral two-sided quotas, strict chronology, and all-depth nesting are
mutually compatible; it does not preserve one exact middle factor.

There is also an exact obstruction to choosing those histories
independently entrance-fibre by entrance-fibre.  Let
\(\mathcal L\subseteq\mathcal V_{q_0}^{\rm PBBS}\) be a set of \(M\)
entrance targets.  For
each \(S\in\mathcal L\), choose independently a random history from

\[
 F_S=\{i\in\Omega_H:I_{q_0}(i)=S\},
\]

according to an arbitrary distribution.  Put

\[
 p_{S,q}(T)=\Pr(I_q(i_S)=T),\qquad
 \lambda_q(T)=\sum_{S\in\mathcal L}p_{S,q}(T).
\tag{6.15}
\]

### Theorem 6.7 (synchronized independent-fibre Poisson gate)

At every depth \(q\), the expected hole count is exactly

\[
 \boxed{
 \mathbb E H_q
 =\sum_{T\in\mathcal V_q^{\rm PBBS}}
   \prod_{S\in\mathcal L}(1-p_{S,q}(T)).}
\tag{6.16}
\]

If, for some \(\delta>0\),

\[
 \max_{S,T}p_{S,q}(T)\le1-\delta,
\tag{6.17}
\]

then

\[
 \boxed{
 \mathbb E H_q
 \ge N_q^{\rm PBBS}
      \exp\left(-\frac{M}{\delta N_q^{\rm PBBS}}\right).}
\tag{6.18}
\]

In particular, if \(M/N_q^{\rm PBBS}=\Theta(1)\), the expectation is
\(\Theta(N_q^{\rm PBBS})\).  Moreover

\[
 \Pr\left(H_q\le\frac12\mathbb EH_q\right)
 \le\exp\left(-\frac{(\mathbb EH_q)^2}{2M}\right),
\tag{6.19}
\]

so at a Gaussian depth this independent synchronized-history process has
\(\Theta(W)\) holes with probability \(1-e^{-\Theta(W)}\).
If \(q-q_0=c\sqrt m+O(1)\) with fixed \(c>0\) and
\(M=N_{q_0}^{\rm PBBS}-O(W/\sqrt m)\), then
\(M>N_q^{\rm PBBS}\) for large \(m\).  At such a depth the scalar floor
in (1.6) is zero and these holes are exactly
\(\widetilde E_q=\Theta(W)\).

#### Proof

A target \(T\) is missed precisely when every independent entrance-fibre
choice avoids it, proving (6.16).  Under (6.17),

\[
 \log(1-p)\ge-\frac p\delta
 \qquad(0\le p\le1-\delta).
\]

Thus the product in (6.16) is at least
\(e^{-\lambda_q(T)/\delta}\).  Since

\[
 \sum_T\lambda_q(T)=M,
\]

convexity of \(x\mapsto e^{-x/\delta}\) gives (6.18).  Changing one
selected history changes the number of covered depth-\(q\) targets, and
hence \(H_q\), by at most one.  The bounded-differences inequality gives

\[
 \Pr(H_q\le\mathbb EH_q-u)\le e^{-2u^2/M}.
\]

Set \(u=\mathbb EH_q/2\) to get (6.19). \(\square\)

Thus even choosing whole nested histories, rather than nibbling the
ranks independently, remains Poisson unless the entrance fibres contain
near-deterministic descendant assignments or the choices are coupled
globally.  Condition (6.17) is not currently verified for PBBS; the
theorem is a sharp dichotomy, not a claim that PBBS lies on its diffuse
side.

The deterministic/diffuse dichotomy can be made quantitative.  Let
\(\mathcal L_{\rm det}\) be the entrance fibres on which the chosen law
is a point mass, let \(D_q\) be the set of their deterministic
depth-\(q\) targets, and put
\(\mathcal L_{\rm dif}=\mathcal L\setminus\mathcal L_{\rm det}\).  If

\[
 \max_{S\in\mathcal L_{\rm dif},T}p_{S,q}(T)\le1-\delta,
\]

then the proof of (6.18), restricted to targets outside \(D_q\), gives
(when \(|D_q|<N_q^{\rm PBBS}\))

\[
 \boxed{
 \mathbb EH_q
 \ge (N_q^{\rm PBBS}-|D_q|)
 \exp\left(
  -\frac{|\mathcal L_{\rm dif}|}
         {\delta(N_q^{\rm PBBS}-|D_q|)}
 \right).}
\tag{6.20}
\]

Consequently, when \(|\mathcal L_{\rm dif}|=O(N_q^{\rm PBBS})\), an
independent-history process can avoid a linear expected hole set only if
either

\[
 |D_q|=N_q^{\rm PBBS}-o(W)
\tag{6.21}
\]

or its non-point-mass fibres themselves become asymptotically
near-deterministic, \(\delta=o(1)\).  Alternative (6.21) is already an
almost-surjective deterministic descendant skeleton; proving it is a
substantive positive theorem, not generic randomness.

Finally, the uncut-versus-literal distinction has a simple exact ledger.
Suppose the oriented PBBS factor has \(p\) components and one cuts each
component once.  At depth \(q\), at most \(q\) cyclic starts per cut cross
the cut.  Deleting those starts from the full corrected deck can create at
most one hole per deleted correct occurrence.  Therefore the lower
floor-correct excess created by all cuts obeys

\[
 \widetilde E_q^{\rm cut}\le pq,
 \qquad
 \sum_{q=q_0}^{H}\widetilde E_q^{\rm cut}
 \le\frac p2\bigl(H(H+1)-(q_0-1)q_0\bigr).
\tag{6.22}
\]

The complementary upper deck has the same bound.  Thus the uncut PBBS
windows really do serve all depths simultaneously, while the displayed
worst-case direct cut-without-crossing-repair guarantee is \(o(W)\) only
under \(pH^2=o(W)\).  A coherent seam may improve this ledger; (6.22) is
a sufficient cut bound, not an unavoidable lower toll.

Hence PBBS gives the correct model for the desired non-Poisson
correlation, but the corrected windows cannot yet be inserted into
Theorem 3.1.

The complementary upper deck has the analogous rankwise statements after
the audited cross-shore shift.  This does **not** prove that its deepest
correct domain is the same as the lower domain \(\Omega_H\), or that one
set of starts satisfies both lower and upper Hall systems.  The literal
two-sided packet theorem therefore contains this additional common-history
intersection gate.

## 7. Exact proved and open boundary

Proved here:

1. the exact all-depth fresh-target drift identity (0.1)--(0.3);
2. its exact signed collision-to-hole compensation form (2.7);
3. a deterministic synchronized conditional-expectation theorem with
   cumulative error \(\sum_t\varepsilon_t\);
4. the sharp critical requirement of average \(o(n)\) net deficit per
   packet;
5. the exact unbiased drift (0.5)--(0.6) and its Poisson terminal cost;
6. the linear twin toll for holes and for every strictly convex separable
   potential;
7. nestedness of the lower PBBS correct domains and the deepest-domain
   dropout/lifetime bounds;
8. zero floor-correct repeat for the full corrected lower PBBS deck at
   every depth;
9. the exact first PBBS two-level Hall deficiency (6.10)--(6.12);
10. the exact all-depth corridor-configuration objective (6.13); and
11. the all-conjugate zero-excess lower flag selection and the abstract
    two-sided zero-excess strongly geodesic atlas; and
12. the synchronized independent-fibre Poisson gate (6.16)--(6.19).

Not proved:

1. a legal ordinary-packet distribution satisfying (3.1) with
   \(\sum_t\varepsilon_t=o(W)\);
2. the deep-to-entrance PBBS projection estimate (6.7);
3. the PBBS chronology Hall inequalities (6.9), let alone their
   all-depth path-compatible strengthening;
4. verification or refutation of the diffuse-fibre hypothesis (6.17) for
   PBBS;
5. a common lower/upper deepest-history selection;
6. a literal cyclic-packet grouping of the selected PBBS histories; or
7. coefficient one.

The precise positive boundary is therefore:

\[
 \boxed{
 \text{construct one extendible entrance-matching trajectory whose
 cumulative fresh-target score deficit in (0.3) is }o(W).}
\]

Entrance matching plus unbiased regeneration cannot supply this.  The
corrected PBBS deck demonstrates that the required nested correlation is
mathematically possible before entrance thinning and literal packet
grouping, but those two operations are exactly where the theorem is
still missing.
