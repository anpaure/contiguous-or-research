# The residence-stratum plateau for multikernels in the first-eligible \(B_4\) atlas

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Fix the ordered first-eligible \(B_4\) packet atlas with local owner square

\[
             \mathcal A=\{14,12,23,34\}.
\tag{0.1}
\]

Let the number of selected four-blocks be \(r=r(m)\), put

\[
h=2r,\qquad r\longrightarrow\infty,\qquad r=o(m),
 \qquad r\le m/16,
\tag{0.2}
\]

and assume \(h\) is a power of two when the certified multikernel factor is
invoked.

and let \(V=4^r=2^h\) be the owner mass of one packet.  The exponentially
small first-eligible leave is always absorbed in an \(o(W)\) error, where

\[
                         W=\binom{2m}{m}.
\tag{0.3}
\]

Internal trace injectivity does not solve the outer packet problem.  There
is an exact first-eligible **residence stratum** which no internal block
permutation, affine phase, multikernel choice, or correlation between
packet labels can change.

For a fixed \(c>0\), take

\[
                         q=c\sqrt r+o(\sqrt r).
\tag{0.4}
\]

If every retained depth-\(q\) window is block-simple--it uses at most one
of the two cube directions in every physical four-block--then each sign
misses at least

\[
 \boxed{
 M_q^\pm\ge \bigl(\delta(c)+o(1)\bigr)W,
 \qquad
 \delta(c)=2\Phi(c/\sqrt2)-1.}
\tag{0.5}
\]

This is a deterministic Hall deficit.  It applies to arbitrary correlated
one-factor-per-packet schedules and even to arbitrary ownerwise radius
subsets.  It is not the independent-choice Poisson bound.

More generally, let \(E_q^\pm\) be the number of selected signed
depth-\(q\) occurrences whose direction support contains both directions
of at least one physical four-block.  Then

\[
 \boxed{
 M_q^\pm\ge
 \bigl(\delta(c)+o(1)\bigr)W-E_q^\pm.}
\tag{0.6}
\]

The trace-rainbow multikernel factor has an almost-uniform direction-set
census.  For it,

\[
 {E_q^\pm\over W}
 \le
 1-{2^q\binom rq\over\binom{2r}q}+o(1)
 \longrightarrow 1-e^{-c^2/4}.
\tag{0.7}
\]

Combining (0.5)--(0.7) gives the residual multikernel plateau

\[
 \boxed{
 M_q^\pm\ge
 \left(e^{-c^2/4}-2\Phi(-c/\sqrt2)+o(1)\right)W.}
\tag{0.8}
\]

The constant in (0.8) is strictly positive for every \(c>0\).  In the
notation requested for the cube scale, take

\[
                         q=\lfloor A\sqrt h\rfloor,
 \qquad c=A\sqrt2.
\tag{0.9}
\]

Then

\[
 \boxed{
 M_q^\pm\ge(\kappa_A+o(1))W,
 \qquad
 \kappa_A=e^{-A^2/2}-2\Phi(-A)>0.}
\tag{0.10}
\]

If \(N_q+o(W)\) starts are retained at this depth, where

\[
                         N_q=\binom{2m}{m-q},
\tag{0.11}
\]

then \(N_q=(1-o(1))W\), and the duplicate-occurrence excess is also at
least \((\kappa_A-o(1))W\).  Because the packet trace maps are internally
injective, all of this duplicate excess is cross-packet.  Consequently the
aggregate cross-packet collision excess through \(q\le A\sqrt h\) is not
\(o(W)\).

The exact escape is also quantified.  At depth \(c\sqrt r\), any repair of
the fixed first-eligible residence cut must devote at least

\[
                         (\delta(c)-o(1))W
\tag{0.12}

occurrences to non-block-simple faces, or it must move owners between
first-eligible packet fibres.  The direction-uniform multikernel supplies
only \((1-e^{-c^2/4}+o(1))W\) such occurrences, which is strictly less
than (0.12).  Merely correlating the packet labels cannot change either
side of this inequality.

## 1. The packet and target residence levels

Partition the ambient coordinates into ordered four-blocks

\[
                         B_1<\cdots<B_b,
 \qquad b=\lfloor m/2\rfloor,
\tag{1.1}
\]

plus at most three unused coordinates.  A block is eligible when its
middle restriction lies in \(\mathcal A\).  A retained packet \(P\) has
selected indices

\[
                         i_1<\cdots<i_r,
\tag{1.2}
\]

the first \(r\) eligible indices.  All states outside these blocks are
frozen throughout \(P\).

For the lower sign write

\[
 \mathcal C^-={1,2,3,4\},
\tag{1.3}
\]

the four singleton local traces.  For the upper sign let \(\mathcal C^+\)
be the four triples of a four-block.  If the next exterior eligible block
\(i_{r+1}\) exists, define

\[
 b^\epsilon(P)=
 \#\{j<i_{r+1}:j\notin\{i_1,\ldots,i_r\},
                 P\cap B_j\in\mathcal C^\epsilon\}.
\tag{1.4}
\]

If there is no \((r+1)\)-st eligible block, use the formal position
\(b+1\), after the last physical block, as the stopping point.  This
terminal convention makes all statements below exact, including the rare
terminal packets.

For a target \(T\) at signed depth \(q\), scan its block restrictions and
let \(a_{r-q+1}(T)\) be its \((r-q+1)\)-st \(\mathcal A\)-block.  Put

\[
 D_q^\epsilon(T)=
 \#\{\mathcal C^\epsilon\text{-blocks before }a_{r-q+1}(T)\},
 \qquad
 \beta_q^\epsilon(T)=D_q^\epsilon(T)-q.
\tag{1.5}
\]

When the stopping block is absent, use the end of the list and admit the
target only when it has exactly \(r-q\) eligible blocks.  Targets with
fewer than \(r-q\) eligible blocks have no block-simple candidate and may
only increase the missing count.

### Lemma 1.1 (residence conservation)

Let a signed depth-\(q\) window in packet \(P\) use \(q\) distinct
physical four-blocks.  If its trace is \(T\), then

\[
                         \boxed{\beta_q^\epsilon(T)=b^\epsilon(P).}
\tag{1.6}
\]

#### Proof

Before taking the trace, the selected blocks are all in \(\mathcal A\).
The \(q\) touched blocks become singleton blocks below, respectively
triple blocks above.  The other \(r-q\) selected blocks remain in
\(\mathcal A\).  Hence the packet's next exterior eligible block is
exactly the target's \((r-q+1)\)-st eligible block.  Before it, the target
has the \(b^\epsilon(P)\) frozen exterior \(\mathcal C^\epsilon\)-blocks
and the \(q\) newly traced blocks.  Thus

\[
                         D_q^\epsilon(T)=b^\epsilon(P)+q,
\]

which is (1.6).  The terminal convention gives the same identity when
there is no next eligible block. \(\square\)

The proof used neither a common direction order nor a probabilistic packet
choice.  It is invariant under every permutation of the selected blocks,
every local square automorphism, and every context-dependent correlation of
such choices across packets.

## 2. Exact candidate degree and biregularity

### Lemma 2.1 (candidate packets stay in one residence component)

If \(D=D_q^\epsilon(T)\), the number of block-simple first-eligible packets
in which \(T\) is the signed trace of a physical \(q\)-face is

\[
                         \boxed{d_q^\epsilon(T)=\binom Dq.}
\tag{2.1}
\]

Every one of those packets has residence level \(D-q\).

#### Proof

Choose \(q\) of the \(D\) boundary blocks before the stopping eligible
block.  Each singleton determines one unique undirected local lower edge
of the square (0.1), and each triple determines one unique undirected upper
edge.  (The edge has two directed endpoints, but it is one affine
one-face.)  Lift the chosen blocks to these local edges.  Together with the
first \(r-q\) eligible blocks of
\(T\), they are precisely the first \(r\) eligible blocks of the completed
middle face, so they determine one canonical packet and one physical face.

Conversely, every block-simple candidate identifies its \(q\) traced
boundary blocks, all of which must precede the target stopping block.
This recovers the chosen \(q\)-subset.  The unchosen \(D-q\) boundary
blocks remain frozen exterior blocks of the packet, so its residence level
is \(D-q\). \(\square\)

Let \(\mathscr P_b^\epsilon\) be the packets of sign-\(\epsilon\) residence
level \(b\), and let

\[
 \mathscr T_{q,b}^\epsilon
 =\{T:\beta_q^\epsilon(T)=b\}.
\tag{2.2}
\]

One packet contains exactly

\[
                         V\binom rq
\tag{2.3}
\]

block-simple physical \(q\)-faces: choose the \(q\) touched four-blocks,
and then choose the local edge/vertex data, of which there are \(4^r=V\)
for every block support.  The physical trace determines the face uniquely.

Double counting the packet--face--target incidences in one residence level
therefore gives the exact biregular identity

\[
 \boxed{
 |\mathscr T_{q,b}^\epsilon|\binom{b+q}q
 =|\mathscr P_b^\epsilon|V\binom rq.}
\tag{2.4}
\]

Equivalently, if

\[
 G_b^\epsilon=|\mathscr P_b^\epsilon|V,
 \qquad
 L_{r,q}(b)={\binom{b+q}q\over\binom rq},
\tag{2.5}
\]

then

\[
                         G_b^\epsilon
 =|\mathscr T_{q,b}^\epsilon|L_{r,q}(b).
\tag{2.6}
\]

This is stronger than a first-moment candidate-degree formula.  It says
that the complete packet--target incidence graph is a disjoint union of
residence components, with a fixed source-to-target mass ratio in every
component.

## 3. The deterministic residence Hall cut

Consider an arbitrary schedule of exact factors inside the packets.  It
may choose its multikernel, affine phase, local automorphisms, and block
permutation as an arbitrary joint function of all packet contexts.  It may
also retain an arbitrary ownerwise radius subset at depth \(q\).

If an occurrence is block-simple, Lemma 1.1 confines it to its packet's
residence component.  There are at most \(G_b^\epsilon\) occurrences
available from component \(b\), even under the deliberately favorable
relaxation in which every packet start is offered to that component.
Therefore the block-simple shortage is at least

\[
\begin{aligned}
 \Delta_{r,q}^\epsilon
 &:=\sum_b
    \left(|\mathscr T_{q,b}^\epsilon|-G_b^\epsilon\right)_+\\
 &=\sum_b|\mathscr T_{q,b}^\epsilon|
    \left(1-{\binom{b+q}q\over\binom rq}\right)_+.
\end{aligned}
\tag{3.1}
\]

A non-block-simple occurrence can hit at most one target left by this cut.
Consequently every schedule satisfies the literal Hall inequality

\[
                         \boxed{M_q^\epsilon
                         \ge\Delta_{r,q}^\epsilon-E_q^\epsilon-o(W).}
\tag{3.2}
\]

The \(o(W)\) term is only the exponentially small packet leave and the
terminal exceptional set.  No independence is assumed in (3.2).

## 4. The critical physical target law

We evaluate (3.1) under the uniform rank-\((m-q)\) and rank-\((m+q)\)
target layers.  The two signs have the same law.

Under product density

\[
 p_-={m-q\over2m},\qquad p_+={m+q\over2m},
\tag{4.1}
\]

erase every block which is neither eligible nor in
\(\mathcal C^\epsilon\).  In either sign, the conditional probability
that the next retained block is a boundary block is

\[
                         \rho_q={m+q\over2m}.
\tag{4.2}
\]

Thus, before fixed-rank conditioning, the number
\(D=D_q^\epsilon(T)\) of boundary blocks before
\(k=r-q+1\) eligible blocks has the negative-binomial law

\[
 \Pr(D=z)=\binom{k+z-1}z(1-\rho_q)^k\rho_q^z.
\tag{4.3}
\]

Because \(r=o(m)\), the stopped word examines at most \(Cr\) blocks with
probability \(1-e^{-\Omega_C(r)}\), for a sufficiently large fixed \(C\).
To justify fixed-rank conditioning, expose these \(s\le4Cr\) coordinates
under the product law of density \(p=p_\epsilon\).  Restrict to prefix
cardinality deviation

\[
                         |a-sp|\le K_m\sqrt r,
\tag{4.3a}
\]

where \(K_m\to\infty\) slowly enough that \(K_m^2r/m\to0\).  Product
concentration makes the complement of (4.3a) \(o(1)\).  For every exposed
configuration in (4.3a), its exact conditional-to-product likelihood ratio
is the ratio of the appropriate binomial point probabilities on the
remaining \(2m-s\) coordinates to the full \(2m\)-coordinate point
probability.  Stirling's formula gives logarithm

\[
 O\left({s\over m}+{(a-sp)^2\over m}\right)=o(1)
\tag{4.3b}
\]

uniformly on this set.  Hence the stopped eligible/boundary word has total
variation distance \(o(1)\) from (4.3) after exact-rank conditioning.  It
follows that, for (0.4),

\[
 {D-(r-q)\over\sqrt{2r}}\Longrightarrow N(0,1).
\tag{4.4}
\]

Writing

\[
 D=r-q+\sqrt{2r}\,N_r+o_p(\sqrt r),
\]

a direct Taylor expansion gives

\[
\begin{aligned}
 \log {\binom Dq\over\binom rq}
 &=\sum_{j=0}^{q-1}\log {D-j\over r-j}\\
 &=-c^2+\sqrt2cN_r+o_p(1).
\end{aligned}
\tag{4.5}

Therefore

\[
 \boxed{
 {\binom{D_q^\epsilon(T)}q\over\binom rq}
 \Longrightarrow e^{-c^2+\sqrt2cN}.}
\tag{4.6}
\]

The function \(x\mapsto(1-x)_+\) is bounded and continuous.  Applying
(4.6) to (3.1) gives

\[
 {\Delta_{r,q}^\epsilon\over N_q}
 \longrightarrow
 \mathbb E(1-e^{-c^2+\sqrt2cN})_+
 =2\Phi(c/\sqrt2)-1.
\tag{4.7}
\]

Finally, \(q^2/m=c^2r/m+o(1)=o(1)\), so

\[
                         {N_q\over W}\longrightarrow1.
\tag{4.8}

Equations (3.2), (4.7), and (4.8) prove (0.5)--(0.6).

## 5. What the multikernel direction census can repair

Call a \(q\)-subset of the \(2r\) packet directions block-simple if it
contains at most one direction from each of the \(r\) physical
four-blocks.  The exact proportion of block-simple direction sets is

\[
                         \rho_{r,q}
 = {2^q\binom rq\over\binom{2r}q}.
\tag{5.1}
\]

For \(q=c\sqrt r+o(\sqrt r)\),

\[
\begin{aligned}
 \log\rho_{r,q}
 &=\sum_{j=0}^{q-1}
   \log {2(r-j)\over2r-j}\\
 &=-{q(q-1)\over4r}+O(q^3/r^2)
 \longrightarrow-{c^2\over4}.
\end{aligned}
\tag{5.2}

The trace-rainbow multikernel theorem gives an almost-uniform occurrence
load on all but an \(o(1)\) proportion of the direction sets, and its bad
direction sets carry only \(o(V)\) starts in one packet.  Summing over the
class (5.1), and then over all packets, proves

\[
 {E_q^\epsilon\over W}
 \le1-\rho_{r,q}+o(1)
 =1-e^{-c^2/4}+o(1).
\tag{5.3}
\]

This estimate remains valid after arbitrary correlated block permutations
or coordinate conjugations of the certified multikernel factors.  A
block-pair permutation preserves the simple family pointwise.  An
unrestricted element of \(S_{2r}\) need not preserve that family
pointwise; it sends it to a family of the same cardinality.  The certified
direction occurrence measure is \(o(1)\)-close to uniform in every such
family sum (the exceptional direction sets carry only \(o(V)\) starts), so
the relabelled family still has mass \(\rho_{r,q}+o(1)\).  More generally,
(0.6) remains valid without (5.3); (5.3) is the specific supply supplied by
the direction-uniform multikernel schedule.

Substitution of (4.7) and (5.3) into (3.2) gives (0.8).

To verify strict positivity, put \(x=c/\sqrt2\) and define

\[
 g(x)=e^{-x^2/2}-2\Phi(-x).
\tag{5.4}
\]

Then \(g(0)=0\), \(g(x)\to0\) as \(x\to\infty\), and

\[
 g'(x)=e^{-x^2/2}\left(\sqrt{2/\pi}-x\right).
\tag{5.5}
\]

Thus \(g\) first increases and then decreases to zero, so

\[
                         g(x)>0\qquad(x>0).
\tag{5.6}

This proves \(\kappa_A>0\) in (0.10) for every fixed \(A>0\).

## 6. Conversion to cross-packet collision excess

Let \(\mathcal X_q\) be the selected signed depth-\(q\) starts, let

\[
 A_q=|\mathcal X_q|=N_q+e_q,
 \qquad e_q=o(W),
\tag{6.1}
\]

and let \(n_T\) be the resulting target loads.  Write

\[
 M_q=N_q-|\{T:n_T>0\}|,
 \qquad
 X_q=\sum_T(n_T-1)_+.
\tag{6.2}
\]

The exact identity

\[
                         X_q-M_q=A_q-N_q=e_q
\tag{6.3}

gives, from (0.10),

\[
                         X_q\ge(\kappa_A-o(1))W.
\tag{6.4}

Also

\[
                         \sum_T\binom{n_T}2\ge X_q.
\tag{6.5}

If packetwise trace injectivity holds on the selected set, one packet
contributes at most one occurrence to a fixed target.  Therefore every
duplicate in (6.4), and every pair counted in (6.5), is cross-packet.  For
the audited trace-rainbow multikernel repair, this assertion holds after
discarding the \(o(W)\) spine-bad occurrences from the internal quarantine
theorem.  Those discarded occurrences can account for only \(o(W)\)
duplicate mass, so (6.4)--(6.5) still leave
\((\kappa_A-o(1))W\) cross-packet excess.  A single depth already has
linear excess, so summing over signs and depths cannot give \(o(W)\).

## 6A. The complementary linear-packet regime

Assumption \(r=o(m)\) was used only to obtain the critical residence law
(4.6).  It is not an escape from the fixed first-eligible atlas.

Suppose instead that, along a subsequence,

\[
                         {r\over m}\longrightarrow\alpha>0.
\tag{6A.1}
\]

At the same requested depth \(q=\lfloor A\sqrt h\rfloor\),

\[
                         {q\over\sqrt m}
 \longrightarrow A\sqrt{2\alpha}>0.
\tag{6A.2}
\]

Take \(R\) to be the union of the last quarter of the ordered physical
four-blocks.  Since \(r\le m/16\), all but \(e^{-\Omega(m)}W\) middle
owners have their first \(r\) eligible blocks before \(R\).  Every
component internal to such a packet fixes its full restriction to \(R\),
independently of its multikernel or coordinate order.  The one-sided
hypergeometric suffix cut therefore gives a constant \(\kappa_{A,\alpha}>0\)
and

\[
                         M_q^\pm
 \ge(\kappa_{A,\alpha}-o(1))W.
\tag{6A.3}
\]

For completeness, if \(\gamma=|R|/(2m)\to1/4\), the middle suffix-count
variance is \((3/32+o(1))m\), while passing to rank \(m-q\) shifts its
mean by \(q/4\).  A threshold \(|T\cap R|\le |R|/2-x\sqrt{3m/32}\)
has target-to-owner gap

\[
 e^{-B^2}\Phi\bigl(B\sqrt{2/3}-x\bigr)-\Phi(-x),
 \qquad B=A\sqrt{2\alpha}.
\tag{6A.4}
\]

Mills' ratio makes (6A.4) positive for a sufficiently large fixed \(x\).
Complementation gives the upper cut.

Consequently no choice of packet scale avoids the obstruction.  Given any
sequence \(r\to\infty\), \(r\le m/16\), extract a subsequence on which
\(r/m\) converges.  Limit zero is closed by (0.10); every positive limit
is closed by (6A.3).  Thus the fixed ordered first-eligible atlas has
linear collision excess along every possible asymptotic packet-scale
regime.

## 7. Exact scope and surviving escape

### Closed schedule class

The theorem closes every construction with all of the following features:

1. middle owners are partitioned by one fixed ordered first-eligible
   \(B_4\) atlas;
2. every component stays inside one such packet;
3. the packet factors have the verified internal trace injectivity;
4. the schedule uses sibling/block permutations, or uses the
   direction-uniform trace-rainbow multikernel factor; and
5. arbitrary correlations between all packet labels and all depths are
   allowed, but the physical packet fibres are not changed.

In particular, the obstruction is not an independence artefact.  The
first-eligible residence decomposition is a deterministic common mode of
the physical overlap kernel.

### Not ruled out

The proof does not rule out a new exact factor which does at least one of
the following:

1. uses at least \((\delta(c)-o(1))W\) depth-\(q\) windows which double-touch
   physical four-blocks, thereby abandoning the direction-uniform
   multikernel census at this scale;
2. makes a positive density of components move coordinates outside their
   original first-eligible blocks;
3. mixes genuinely different ambient block orders by an exact
   owner-preserving repacketization; or
4. constructs nonlocal ownership trades which transport occurrences
   between the residence components (2.4).

Choosing packet labels more cleverly, using dependent rather than
independent signs, or permuting only the already selected blocks does none
of these.  Those operations leave (1.6) and (2.4) unchanged.

## 8. Independent audit notes

The decisive step was audited in two independent forms.

* The target-side audit recovers the exact candidate degree
  \(\binom{D_q^\epsilon(T)}q\), including the terminal stopping convention,
  and the negative-binomial/lognormal law (4.3)--(4.7).
* The packet-side audit recovers residence conservation (1.6) and the
  exact biregular identity (2.4).  This is the step which upgrades the
  previously known barycentric lower tail into a schedule-independent Hall
  cut.

There is also an independent ambient-Gaussian frozen-suffix obstruction for
the same fixed atlas.  Its strongest enlarged-menu statement needs the
following scope correction: support-changing local \(B_4\) relabelings are
covered either under \(r=o(m)\), as assumed here, or after their imported
owner mass is included explicitly.  Support-preserving packet
automorphisms and all internal multikernel/block permutations require no
correction.  This issue does not enter the residence proof above, which
works inside one fixed owner atlas.

## 9. Final boundary

The trace-rainbow repair succeeds at its intended internal task: it removes
same-packet trace collisions.  When transplanted into the first-eligible
\(B_4\) atlas, however, the physical basepoint problem does not become a
free packet-signing problem.  First-eligible chronology partitions the
physical incidence graph into residence components whose critical loads
have a lognormal spread.  The uniformly distributed non-block-simple
windows of the multikernel are quantitatively insufficient to bridge those
components.

Therefore the proved boundary is

\[
 \boxed{
 \text{internal traces injective, but }
 \text{cross-packet collision excess}\ge
 (\kappa_A-o(1))W,
 \quad
 \kappa_A=e^{-A^2/2}-2\Phi(-A)>0.}
\tag{9.1}
\]

No coefficient-one conclusion follows from the first-eligible packet
schedule.  The next admissible operation must be an exterior-moving or
owner-repacketizing construction, not another dependent choice of factors
inside the same packet fibres.
