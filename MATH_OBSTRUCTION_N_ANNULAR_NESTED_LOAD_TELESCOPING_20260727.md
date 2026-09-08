# Annular nested packet loads: exact support identity, domino-twin non-telescoping, and the PBBS simultaneous flag gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Result and scope

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 r=m-q_0,\qquad J=H-q_0,
 \qquad N_d=\binom n{r-d}\quad(0\le d\le J).
\tag{0.1}
\]

Let \(\mathcal M\) be a family of cyclic-order packets whose length-
\(r\) entrance decks are pairwise disjoint. If \(s=|\mathcal M|\), put

\[
                         G=ns.
\tag{0.2}
\]

At depth \(d\), let \(\mu_d(R)\) be the number of occurrences of the
length-\((r-d)\) target \(R\), and let \(b_d=|\operatorname {supp}
\mu_d|\). The exact floor-correct repeat excess is

\[
 \boxed{\widetilde E_d=\min\{G,N_d\}-b_d.}
\tag{0.3}
\]

The conclusions of this note are these.

1. The cyclic intersection identity gives a single nested occurrence
   process, but the equality partitions of its occurrences are not nested.
   There is an exact summation-by-parts formula, (2.5), whose increments
   have no sign.
2. On every parameter subsequence on which \(r\) is odd, there are two
   literal packets with disjoint entrance decks for which

   \[
    \widetilde E_d=
    \begin{cases}
      n/2,&d\text{ odd},\\
      0,&d\text{ even}.
    \end{cases}
   \tag{0.4}
   \]

   Consequently

   \[
    \boxed{
    \sum_{d=0}^{J}\widetilde E_d
      ={n\over2}\left\lceil{J\over2}\right\rceil.}
   \tag{0.5}
   \]

   The example satisfies the exact nested intersections, all extension
   incidences, all point margins, correct rank at every depth, and the
   exact pair-energy floor. Thus none of those local identities can yield
   a positive cross-depth telescope.
3. The obstruction scales to

   \[
       g=(1+o(1)){N_0\over8n^2}
   \tag{0.6}
   \]

   mutually entrance-disjoint twin gadgets by a direct greedy relabelling
   argument. Their selected occurrence mass is

   \[
       G_{\rm sel}=(1+o(1)){N_0\over4n},
   \tag{0.7}
   \]

   while their aggregate repeat excess through \(J\) is at least

   \[
       (1+o(1)){N_0J\over32n}.
   \tag{0.8}
   \]

   This disproves every density-blind additive estimate of order
   \(O(G_{\rm sel})\), but (0.8) is only \(\Theta(W/\sqrt m)=o(W)\)
   when \(J=\Theta(\sqrt m)\). It is not a critical-leave counterexample.
4. If the top targets are free, the full layered containment network does
   admit \(M\) distinct-top flags which are simultaneously floor/ceiling
   balanced at every depth; this follows exactly from a uniform fractional
   flow and integral network-flow total unimodularity. The statement fails
   for prescribed top families without additional Hall cuts.
5. A strongly two-sided PBBS fan of length \(H\) does provide one correct
   nested flag through all smaller depths and extends individually to an
   ordinary packet. The proved PBBS support theorem, however, is

   \[
       \forall q\ \forall S\ \exists A=A(q,S),
   \tag{0.9}
   \]

   whereas the annular gate requires one common integral family of starts,
   one common even-ground projection, and one common packetization whose
   histograms work for every \(q_0\le q\le H\). No proved PBBS statement
   permits this exchange of quantifiers. Correctness alone cannot do so,
   because the packets in (0.4) are correct at every depth.

Thus the shared leave removes the scalar floor, but neither nesting,
shadows, point margins, extension capacities, nor presently proved PBBS
correct-window support forces

\[
                         \sum_d\widetilde E_d=o(W).
\tag{0.10}
\]

The critical-leave existence theorem remains open. Any positive proof
must use a genuinely density-sensitive, colour-biased selection invariant
or a global PBBS flag SDR; it cannot be a sum of local packet inequalities.

## 1. Exact nested occurrence and extension identities

Write a directed cyclic packet as

\[
                         P=(x_i)_{i\in\mathbb Z_n}.
\tag{1.1}
\]

Its entrance window and its depth-\(d\) descendant are

\[
 E_i(P)=\{x_i,x_{i+1},\ldots,x_{i+r-1}\},
\tag{1.2}
\]

\[
 R_{i,d}(P)=\{x_{i+d},x_{i+d+1},\ldots,x_{i+r-1}\}.
\tag{1.3}
\]

Indices are cyclic. The fundamental identity is

\[
 \boxed{
 R_{i,d}(P)=\bigcap_{t=0}^{d}E_{i+t}(P).}
\tag{1.4}
\]

As \(i\) varies, (1.3) is exactly the deck of all cyclic
\((r-d)\)-intervals of \(P\). Thus (1.4) loses no starts.

There is an exact incidence form. Join an entrance target \(T\) to a
depth-\(d\) target \(R\) when they occur in one selected packet and
\(R\subset T\) as one of the consecutive subintervals in (1.4). Every
entrance occurrence has degree \(d+1\). Every occurrence of \(R\) also
has \(d+1\) entrance extensions. Since entrance targets never repeat,
this is a simple bipartite incidence graph and

\[
 \deg(R)=(d+1)\mu_d(R).
\tag{1.5}
\]

In particular,

\[
 \boxed{
 (d+1)\mu_d(R)
   \le \binom{n-r+d}{d}.}
\tag{1.6}
\]

Between two adjacent depths, every interval occurrence has precisely two
immediate parents and two immediate children. These exact shadow
incidences are stronger than mere first moments, but they impose no
monotonicity on equality of targets: equal parents may delete different
endpoints, while different parents may delete to the same child.

Finally, every coordinate belongs to exactly \(r-d\) cyclic
\((r-d)\)-intervals of one packet. Hence the exact point margins are

\[
 \boxed{
 \sum_{R\ni x}\mu_d(R)=s(r-d)
 ={G(r-d)\over n}\qquad(x\in[n]).}
\tag{1.7}
\]

## 2. The support identity and why it does not telescope

Every depth contains exactly \(G\) occurrences, so

\[
 \sum_R(\mu_d(R)-1)_+=G-b_d.
\tag{2.1}
\]

Subtracting the unavoidable repeat floor \((G-N_d)_+\) proves (0.3):

\[
 \begin{aligned}
 \widetilde E_d
  &=G-b_d-(G-N_d)_+\\
  &=\min\{G,N_d\}-b_d.
 \end{aligned}
\tag{2.2}
\]

This is also the exact hole count when \(G\ge N_d\).

Put

\[
                         c_d=\min\{G,N_d\},
 \qquad h_d=c_d-b_d=\widetilde E_d.
\tag{2.3}
\]

Entrance disjointness gives \(h_0=0\). Define the signed support defect
created at step \(d\) by

\[
 \gamma_d=(c_d-c_{d-1})-(b_d-b_{d-1})=h_d-h_{d-1}.
\tag{2.4}
\]

Summation by parts gives the only automatic cross-depth telescope:

\[
 \boxed{
 \sum_{d=0}^{J}\widetilde E_d
   =\sum_{t=1}^{J}(J-t+1)\gamma_t.}
\tag{2.5}
\]

The coefficients are favorable, but the increments \(\gamma_t\) have no
sign. A merger creates positive \(\gamma_t\), and different endpoint
deletions can split that same equality class at the next step, creating
negative \(\gamma_{t+1}\). Thus (2.5) is an occupation-time identity,
not a boundary estimate.

The pair-energy version has the same limitation. Put

\[
 P_d=\sum_R\binom{\mu_d(R)}2.
\tag{2.6}
\]

If \(G=u_dN_d+v_d\), \(0\le v_d<N_d\), its exact integer floor is

\[
 P_d^{\min}=N_d\binom{u_d}{2}+u_dv_d,
 \qquad \Phi_d=P_d-P_d^{\min}\ge0.
\tag{2.7}
\]

The elementary floor inequality gives

\[
 \widetilde E_d\le {\Phi_d\over\kappa_d},
 \qquad
 \kappa_d=
 \begin{cases}
 1,&u_d=0,\\
 \binom{u_d+1}{2},&u_d\ge1.
 \end{cases}
\tag{2.8}
\]

No cross-depth decay of \(\Phi_d\) follows from (1.4)--(1.7). The next
section gives exact alternating equality in (2.8).

There is, however, one useful exact synchronized process identity. It
does not prove the desired estimate by itself, but it is the correct
interface for a colour-biased packet process.

### Theorem 2.1 (all-depth fresh-score telescope)

Order the selected packets as \(P_1,\ldots,P_s\). After \(t\) packets,
put

\[
 G_t=nt,\qquad
 \mathcal S_{d,t}=\bigcup_{j\le t}\mathcal I_{r-d}(P_j),
 \qquad b_{d,t}=|\mathcal S_{d,t}|.
\tag{2.9}
\]

For a candidate next packet \(P\), define its depth-\(d\) fresh score

\[
 Z_{d,t}(P)
 =|\mathcal I_{r-d}(P)\setminus\mathcal S_{d,t}|,
\tag{2.10}
\]

and define the exact increase of the integer capacity floor by

\[
 \begin{aligned}
 C_{d,t}
 &=\min\{G_t+n,N_d\}-\min\{G_t,N_d\}\\
 &=(N_d-G_t)_+-(N_d-G_t-n)_+.
 \end{aligned}
\tag{2.11}
\]

Then

\[
 \boxed{
 \widetilde E_{d,t+1}-\widetilde E_{d,t}
   =C_{d,t}-Z_{d,t}(P_{t+1}).}
\tag{2.12}
\]

Consequently

\[
 \boxed{
 \sum_{d=0}^{J}\widetilde E_{d,s}
 =\sum_{t=0}^{s-1}
   \left(
     \sum_{d=0}^{J}C_{d,t}
       -\sum_{d=0}^{J}Z_{d,t}(P_{t+1})
   \right).}
\tag{2.13}
\]

#### Proof

After \(t\) packets, (0.3) is

\[
 \widetilde E_{d,t}=\min\{G_t,N_d\}-b_{d,t}.
\tag{2.14}
\]

Adding \(P_{t+1}\) raises the first term by \(C_{d,t}\) and raises the
support by exactly \(Z_{d,t}(P_{t+1})\). This proves (2.12). Sum first
over \(d\) and then over \(t\); the initial excess is zero. \(\square\)

Thus a sufficient adaptive invariant is

\[
 \sum_{t=0}^{s-1}
 \left(
  \sum_d C_{d,t}-\sum_dZ_{d,t}(P_{t+1})
 \right)_+=o(W).
\tag{2.15}
\]

There are \(s=\Theta(W/n)\) packets at the corrected annular density, so
an occurrencewise nonnegative-deficit implementation must have average
positive deficit \(o(n)\) per packet. Formula (2.13) permits negative
later increments to repair earlier deficits; (2.15) is sufficient, not
necessary. The decisive missing theorem is a lower bound for the
*synchronized* fresh score \(\sum_dZ_{d,t}(P)\) among entrance-compatible
candidates. Rankwise independent choices do not address (2.13).

## 3. A literal domino-twin non-telescoping packet

Fix a cyclic order

\[
 P=(x_0,x_1,\ldots,x_{n-1})
\tag{3.1}
\]

and let \(\tau\) swap every adjacent position pair:

\[
 \tau=(0\ 1)(2\ 3)\cdots(n-2\ n-1).
\tag{3.2}
\]

Define

\[
 P^\tau=(x_1,x_0,x_3,x_2,\ldots,x_{n-1},x_{n-2}).
\tag{3.3}
\]

### Lemma 3.1 (exact common-interval deck)

For every \(2\le\ell\le n-2\),

\[
 |\mathcal I_\ell(P)\cap\mathcal I_\ell(P^\tau)|
 =
 \begin{cases}
 n/2,&\ell\text{ even},\\
 0,&\ell\text{ odd}.
 \end{cases}
\tag{3.4}
\]

#### Proof

Identify positions with \(\mathbb Z_n\). A \(P^\tau\)-interval with
position set \(I\) has the same label set as the \(P\)-position set
\(\tau I\).

If \(\ell\) is even and \(I\) starts at an even position, then \(I\) is
a union of complete dominoes and \(\tau I=I\). There are \(n/2\) such
intervals. If an even interval starts at an odd position, its two boundary
dominoes are cut. Swapping their singleton positions creates two gaps, so
\(\tau I\) is not a cyclic interval.

If \(\ell\) is odd, exactly one domino is cut. Swapping its singleton
position moves that endpoint one step across the boundary while every
complete interior domino stays fixed. For \(1<\ell<n-1\), the image has
one gap and is not a cyclic interval. The excluded lengths \(1,n-1\) are
exactly the singleton/complement exceptions. This proves (3.4). \(\square\)

### Theorem 3.2 (exact alternating repeat excess)

Assume \(r\) is odd and \(2\le r-J\le r\le n-2\). Then
\(\{P,P^\tau\}\) is an entrance matching and (0.4)--(0.5) hold.

#### Proof

At the entrance length \(r\), Lemma 3.1 gives no common target. At depth
\(d\), the interval length \(r-d\) is even exactly when \(d\) is odd.
Thus the two packets have \(n/2\) common targets at odd depths and none
at even depths.

Here \(G=2n<N_d\). Every common target has load two and all other targets
have load one, so the forced floor is zero and

\[
 \widetilde E_d=P_d=\Phi_d
 =|\mathcal I_{r-d}(P)\cap\mathcal I_{r-d}(P^\tau)|.
\tag{3.5}
\]

This proves (0.4), and summing over the odd integers in \([1,J]\) proves
(0.5). \(\square\)

For this example, \(h_d=n/2\) at odd \(d\) and zero at even \(d\).
Hence

\[
 \gamma_d=
 \begin{cases}
 +n/2,&d\text{ odd},\\
 -n/2,&d\text{ even}.
 \end{cases}
\tag{3.6}
\]

This makes the failure of a boundary telescope literal. Notice also that
the construction consists of honest cyclic packets. It therefore obeys
the nested identity (1.4), the extension graph (1.5), the cap (1.6), the
point margins (1.7), and correct lower and complementary-upper ranks at
every depth. The obstruction is not a wrong-rank or shadow-lock artifact.

It also gives the sharp local failure of the fresh-score route. Insert
\(P\) first and \(P^\tau\) second while the process is still below every
capacity floor. For the second insertion,

\[
 Z_{d,1}(P^\tau)=
 \begin{cases}
  n/2,&d\text{ odd},\\
  n,&d\text{ even},
 \end{cases}
 \qquad C_{d,1}=n.
\tag{3.7}
\]

Thus the synchronized fresh deficit is exactly

\[
 {n\over2}\left\lceil{J\over2}\right\rceil.
\tag{3.8}
\]

Nesting does not align freshness across depths. At critical density,
later packets could still fill these holes, so (3.8) is a local process
obstruction and not a final-hole lower bound.

For comparison, two independent random packets have expected total
common-target count through the displayed annulus at most

\[
 \sum_{d=0}^{J}{n^2\over N_d}=o(1).
\tag{3.9}
\]

Thus, for all sufficiently large \(m\), there is also a two-packet family
with the same \(G\), the same scalar leave, and no repeat at any displayed
depth. The scalar leave and the exact point margins do not distinguish
these two opposite behaviours.

## 4. A scalable entrance-disjoint obstruction

The preceding gadget is not confined to two packets.

### Theorem 4.1 (greedy packing of twin gadgets)

Assume \(r\) is odd. There is a family of

\[
 g=\left\lfloor{N_0\over8n^2}\right\rfloor
\tag{4.1}
\]

coordinate relabellings of the domino-twin gadget such that all \(2g\)
packet entrance decks are mutually disjoint.

#### Proof

Suppose \(t<g\) gadgets have been chosen. Their entrance decks use
exactly \(2nt\) rank-\(r\) targets. Apply a uniformly random coordinate
permutation to one new twin gadget. Each one of its \(2n\) entrance
targets is uniformly distributed over the \(N_0\) rank-\(r\) targets.
The union bound gives

\[
 \Pr(\text{an entrance collision})
 \le {2n\cdot2nt\over N_0}
 ={4n^2t\over N_0}<\frac12.
\tag{4.2}
\]

Hence a collision-free relabelling exists. Induction proves the theorem.
\(\square\)

### Corollary 4.2 (aggregate repeat lower bound)

In the fixed Gaussian window

\[
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),
 \qquad0<a<b,
\tag{4.3}
\]

the family in Theorem 4.1 has zero forced floor at every displayed depth
and

\[
 \sum_{d=0}^{J}\widetilde E_d
 \ge {gn\over2}\left\lceil{J\over2}\right\rceil
 =(1+o(1)){N_0J\over32n}.
\tag{4.4}
\]

#### Proof

The selected occurrence mass is

\[
 G_{\rm sel}=2ng=(1+o(1)){N_0\over4n}.
\tag{4.5}
\]

Uniformly through the fixed Gaussian annulus, \(N_d/N_0\) is bounded
below by a positive constant depending only on \(a,b\). Hence
\(G_{\rm sel}<N_d\) for all large \(m\), so every forced floor is zero.

At an odd depth, each twin contributes \(n/2\) internally duplicated
targets. If several twins duplicate the same target, a target receiving
\(2k\) such occurrences contributes \(2k-1\ge k\) to repeat excess.
Thus internal twin contributions cannot be cancelled by coincidences
between gadgets, and

\[
                         \widetilde E_d\ge gn/2
\tag{4.6}
\]

at every odd depth. Summation proves (4.4). \(\square\)

The ratio of (4.4) to (4.5) is asymptotically \(J/8\). Thus no estimate

\[
                         \sum_d\widetilde E_d=O(G_{\rm sel})
\tag{4.7}
\]

can follow from packet-local nested identities with an absolute constant.
At \(J=\Theta(\sqrt m)\), however, (4.4) is only
\(\Theta(W/\sqrt m)\). Extending the gadgets to a critical-leave matching
would require an integral near-resolution of their \(2n\)-uniform
entrance superpacket hypergraph. That theorem is not proved here.

## 4A. The free-top TU theorem and the exact common-top obstruction

There is a strong abstract positive theorem which must not be confused
with packetization. Let the full layered containment network have vertex
layers

\[
 V_d=\binom{[n]}{r-d}\qquad(0\le d\le J)
\tag{4A.1}
\]

and arcs \(T\to R\) exactly when \(R\subset T\) and
\(|T\setminus R|=1\).

### Theorem 4A.1 (free-top simultaneous balanced nested flags)

For every integer \(0\le M\le N_0\), there are \(M\) nested flags

\[
 T_{i,0}\supset T_{i,1}\supset\cdots\supset T_{i,J},
 \qquad |T_{i,d}|=r-d,
\tag{4A.2}
\]

whose top members \(T_{i,0}\) are distinct and whose load at every
\(R\in V_d\) belongs to

\[
 \left\{left\lfloor{M\over N_d}\right\rfloor,
             \left\lceil{M\over N_d}\right\rceil\right\}.
\tag{4A.3}
\]

In particular, the abstract flag family has

\[
                         \widetilde E_d=0
 \qquad(0\le d\le J).
\tag{4A.4}
\]

#### Proof

Split every vertex \(R\in V_d\) into an in-node and an out-node. Give
its splitting arc the integral lower and upper capacities

\[
 \left\lfloor{M\over N_d}\right\rfloor,
 \qquad
 \left\lceil{M\over N_d}\right\rceil.
\tag{4A.5}
\]

Add a source, a sink, and require total flow \(M\). At the top, the
upper capacity in (4A.5) is one because \(M\le N_0\), so integral flow
will use distinct top vertices.

The network has a fractional flow. Put node flow \(M/N_d\) at every
vertex in layer \(d\). Between layers \(d\) and \(d+1\), put the same
amount

\[
 {M\over N_d(r-d)}
 ={M\over N_{d+1}(n-r+d+1)}
\tag{4A.6}
\]

on every containment arc. The equality is the usual incidence identity

\[
                         N_d(r-d)
 =N_{d+1}(n-r+d+1).
\tag{4A.7}
\]

Thus all node balances and all bounds (4A.5) hold.

A directed network with integral lower and upper capacities has an
integral feasible flow whenever it has a fractional one. Decompose the
resulting integral acyclic flow of value \(M\) into unit source--sink
paths. These are the flags (4A.2), and (4A.3) is exactly the node-capacity
condition. A floor/ceiling load has full possible support when
\(M\ge N_d\) and has \(M\) distinct targets when \(M<N_d\), proving
(4A.4). \(\square\)

The freedom to choose the top layer is essential.

### Proposition 4A.2 (prescribed-top Hall failure)

Assume \(n\ge2r+2\) and \(r\ge2\). There is a distinct top family
\(\mathcal A\subset V_0\), of size \(M\le N_1\), for which no collection
of nested flags starting at every member of \(\mathcal A\) has balanced
zero--one load at depth one.

#### Proof

Fix a \(2r\)-set \(X\subset[n]\) and take

\[
                         \mathcal A=\binom Xr,
 \qquad M=\binom{2r}r.
\tag{4A.8}
\]

For \(n\ge2r+2\), one has \(M\le\binom n{r-1}=N_1\); the closest case
\(n=2r+2\) follows from

\[
 {\binom{2r+2}{r-1}\over\binom{2r}r}
 ={(2r+2)(2r+1)r\over(r+3)(r+2)(r+1)}\ge1,
\tag{4A.9}
\]

with equality only at \(r=2\), and the ratio increases with \(n\).
Hence balance at depth one requires \(M\) distinct facets.

But every available facet lies in \(X\), and the complete neighbor set
has size

\[
 \left|\binom X{r-1}\right|
 =\binom{2r}{r-1}
 ={r\over r+1}M<M.
\tag{4A.10}
\]

Hall's condition fails. \(\square\)

Thus total unimodularity solves the free-top abstract problem, not the
common-owner or common-PBBS entrance problem. For a prescribed entrance
family, the exact missing hypothesis is feasibility of every cut in the
induced layered containment network.

There is also a useful exact comparison inequality. Let \(\mu\) be any
nonnegative integer load vector of total mass \(M\) on \(N\) targets,
and let \(b\) be any balanced vector of the same mass, with entries
\(u=\lfloor M/N\rfloor\) or \(u+1\). Then

\[
 \boxed{
 \widetilde E(\mu)
 \le {\|\mu-b\|_1\over2\max\{1,u\}}
 \le {1\over2}\|\mu-b\|_1.}
\tag{4A.11}
\]

Indeed, if \(u=0\), the balanced support has size \(M\), and the deficit
mass needed to reach it is at least \(M-|\operatorname {supp}\mu|),
which is \(\widetilde E(\mu)\). If \(u\ge1\), then
\(\widetilde E(\mu)\) is the number of zero cells, and each such cell is
short of \(b\) by at least \(u\). Equal total masses identify this total
deficit with \(\|\mu-b\|_1/2\), proving (4A.11).

Finally, if actual flags \((T_{i,d})\) and balanced flags
\((B_{i,d})\) are paired, their histograms satisfy

\[
 {1\over2}\|\mu_d-b_d\|_1
 \le|\{i:T_{i,d}\ne B_{i,d}\}|.
\tag{4A.12}
\]

Therefore

\[
 \boxed{
 \sum_d\widetilde E_d(\mu)
 \le\sum_{d,i}\mathbf1_{\{T_{i,d}\ne B_{i,d}\}}.}
\tag{4A.13}
\]

The inequality is valid; the existence of an \(o(W)\)-mismatch coupling
whose top layer agrees with the actual entrance family is not automatic.
Proposition 4A.2 shows that even exact agreement can be impossible.

## 5. Audit of the presently proved PBBS corrected windows

The PBBS all-depth support theorem lives naturally on \(2m+1\)
coordinates. For a based step-two orbit fan

\[
                         A,gA,\ldots,g^qA,
\tag{5.1}
\]

write

\[
 \Theta_q^-(A)=\bigcap_{t=0}^{q}g^tA,
 \qquad
 \Theta_q^+(A)=\bigcup_{t=0}^{q}g^tA.
\tag{5.2}
\]

Two separate statements must be distinguished.

### Proposition 5.1 (what one long correct fan supplies)

If (5.1) is strongly two-sided geodesic through depth \(H\), then the
same start supplies correct nested lower and upper targets at every
\(q\le H\). It also extends individually to an ordinary cyclic packet on
\(2m\) coordinates after deleting any coordinate outside its union.

#### Proof

Strong two-sided geodesicity says that the \(H\) deleted coordinates and
the \(H\) inserted coordinates are all distinct. Every prefix inherits
this property, so its intersection and union have ranks \(m-q\) and
\(m+q\). The fan union has size \(m+H\), leaving
\(m+1-H>0\) unused coordinates on the odd ground set. Delete one unused
coordinate. Ordering the departure coordinates first, then the common
core, then the arrival coordinates, and finally the unused complement
extends the displayed path to a cyclic order. \(\square\)

Thus there is no one-fan simultaneity obstruction.

### Proposition 5.2 (the quantifier and packetization gap)

The proved PBBS support statements do not imply a common annular packet
family with \(\sum_d\widetilde E_d=o(W)\).

#### Proof audit

The proved lower support statement is pointwise:

\[
 \forall q\le m\ \forall S\in\binom{[2m+1]}{m-q}\quad
 \exists A=A(q,S):\ \Theta_q^-(A)=S.
\tag{5.3}
\]

The upper statement is obtained from the shifted cross-shore identity

\[
 [2m+1]\setminus\Theta_q^+(A_i)
     =\Theta_{q-1}^-(A_{i+1}).
\tag{5.4}
\]

Neither assertion chooses one family of starts simultaneously across
depths. The needed conclusion would have to provide, in one construction:

1. one common coordinate deletion and relabelling to \([2m]\);
2. enough starts which are strongly two-sided correct through \(H\);
3. an integral grouping of those starts into ordinary cyclic packets;
4. an injective or near-injective entrance histogram at \(q_0\); and
5. support deficiency \(o(W)\) after summing every deeper histogram.

Pointwise surjectivity in (5.3) proves none of items 1--5. In particular,
choosing one depth-\(H\) fan for each depth-\(H\) target gives only
\(N_H\) seeds, and gives no control of their depth-\(q_0\) histogram.
Choosing one seed in each of the approximately \(N_{q_0}/n\) required
ordinary packets certifies only a \(1/n\) fraction of their starts.

Correct-rank sets also vary with depth. Every centered PBBS start is
correct through depth two, while the audited gap-five family supplies
exactly \((2m+1)(m-1)\) physical wrong-rank depth-three starts. Thus even
prefix correctness at one depth cannot be silently extended to the next.
Finally, the literal packets in Theorem 3.2 are correct at every depth
but have the bad alternating histogram (0.4), so replacing PBBS support
by the stronger phrase “all selected windows are correct” would still
not prove histogram balance. \(\square\)

The required PBBS statement is therefore a global flag-SDR or
colour-biased packet theorem. One clean formulation is: choose one common
family \(\mathcal A\) of strongly \(H\)-correct starts, with a common
even projection and ordinary-packet grouping, such that

\[
 \sum_{q=q_0}^{H}
 \left(
   \min\{|\mathcal A|,N_q\}
   -|\{\Theta_q^-(A):A\in\mathcal A\}|
 \right)=o(W),
\tag{5.5}
\]

and likewise on the complementary upper shore. Formula (5.5) is exactly
the PBBS version of (0.3), not an additional relaxation.

## 6. Audited boundary

Proved here:

1. the exact support/floor formula (0.3);
2. the exact signed summation-by-parts identity (2.5);
3. the exact nested, extension, shadow, and point-margin identities;
4. a literal two-packet alternating merger/reset construction with exact
   repeat total (0.5);
5. a greedy exponentially large family of mutually entrance-disjoint twin
   gadgets and the exact-scale bound (4.4); and
6. the precise PBBS quantifier and packetization gap.

Not proved here:

1. a critical-leave matching with \(\Omega(W)\) aggregate repeat excess;
2. a universal critical-leave theorem forcing \(o(W)\) excess;
3. a PBBS global flag SDR satisfying (5.5); or
4. coefficient one.

The decisive negative conclusion is deliberately narrower: the proposed
cross-depth telescope does not exist at the level of nested interval
identities, extension incidences, shadows, point margins, pair-energy
floors, or correct-rank windows. The positive theorem, if true, must see
the global density and must bias packet selection using the deeper target
loads themselves.
