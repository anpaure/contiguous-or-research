# The retained-annulus rotor forest requires dense surgery from every paired scaffold

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, web input,
or probabilistic black box is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\tag{0.1}
\]

and fix

\[
 0<a<b,\qquad q_0=\lceil a\sqrt m\rceil,
 \qquad H=\lfloor b\sqrt m\rfloor.
\tag{0.2}
\]

One full SCD, after retaining its chains of native radius at least \(q_0\),
supplies exactly \(N_{q_0}\) owner-simple providers and every signed
annular target through \(H\) exactly once by its designated tag class. A
radius-\(H\) rotor path forest with \(p\) paths therefore compiles at
length

\[
 W+2Hp.
\tag{0.3}
\]

The desired condition is \(p=o(W/H)\).

This note attacks the proposed noncanonical/local-surgery construction. It
does not refute a densely rebuilt noncanonical SCD. It proves a sharp
obstruction to every sparse surgery around a stationary coordinate-pair
scaffold.

Fix a perfect matching \(\mathcal P\) of the \(2m\) coordinates. Call a
selected radius-\(H\) port system **fully \(\mathcal P\)-paired** when the
complete central word-set

\[
 Z_H(\omega)=\{z_1,\ldots,z_{2H}\}
\tag{0.4}
\]

of every retained state is a union of \(H\) pairs of \(\mathcal P\).
Call its SCD **projectively \(\mathcal P\)-paired** when, for every
\(q_0\le q\le H\), the radius-\(q\) central difference of every chain
reaching depth \(q\) is a union of \(q\) pairs. The stationary-pair
product construction is the motivating example.

No two distinct paired states are joined by a rotor edge: a radius-\(q\)
rotor replaces one coordinate of the \(2q\)-set \(Z_q\), whereas two
unions of matching pairs have even intersection size. This elementary
parity fact combines with a sharp edit lemma.

Let \(M\) be the number of complete retained port states in a proposed
construction which are absent from a fixed fully paired baseline. Then:

1. If the proposed states have a genuine radius-\(H\) rotor path forest
   with \(p\) paths, then
   \[
   \boxed{p+2M\ge N_{q_0}.}
   \tag{0.5}
   \]
   Hence \(p=o(W/H)\) forces
   \[
   \boxed{
   M\ge\left(\frac12e^{-a^2}-o(1)\right)W
    =\left(\frac12-o(1)\right)N_{q_0}.}
   \tag{0.6}
   \]

2. Even if promotion arcs are admitted, the full-top fibre cut gives
   \[
   \boxed{p+2M\ge N_H,}
   \tag{0.7}
   \]
   and therefore
   \[
   M\ge\left(\frac12e^{-b^2}-o(1)\right)W.
   \tag{0.8}
   \]

3. At every threshold \(q\), let \(M_q\) be the number of radius-\(q\)
   truncated high-tag states absent from the paired baseline. Every
   bridge-one path cover obeys
   \[
   \boxed{
   2M_q\ge\bigl(2N_q-N_{q_0}-p\bigr)_+.}
   \tag{0.9}
   \]
   Thus, for \(q=c\sqrt m+O(1)\),
   \[
   M_q\ge
   \left(e^{-c^2}-\frac12e^{-a^2}-o(1)\right)W
   \tag{0.10}
   \]
   whenever \(c^2-a^2<\log2\).

4. In the stronger length-\(2m\) packet form, put
   \[
   K=\left\lfloor\frac{N_{q_0}}{2m}\right\rfloor,
   \qquad \rho=N_{q_0}-2mK.
   \tag{0.11}
   \]
   If \(2mK\) retained states lie in genuine rotor cycles of length
   \(2m\), and \(M^{\rm cyc}\) of those states are absent from the paired
   baseline, then
   \[
   \boxed{2M^{\rm cyc}\ge2mK=N_{q_0}-\rho.}
   \tag{0.12}
   \]
   Hence asymptotically one must replace at least half of all used
   providers. If bridge-one cycles are allowed instead, full-top density
   still gives
   \[
   \boxed{
   2M^{\rm cyc}\ge N_H-\rho-K.}
   \tag{0.13}
   \]

A one-pass length-\(2m\) rotor cycle has a separate exact residence
ledger. Every coordinate spends \(2H\) states in the singleton queue; its
lower and residual residence times \(\ell(c),r(c)\) satisfy

\[
 \ell(c)+r(c)=2(m-H),
 \qquad
 \frac1{2m}\sum_c\ell(c)
 =\frac1{2m}\sum_cr(c)=m-H.
\tag{0.14}
\]

It is the ordinary cyclic-order packet exactly when all these residence
times equal \(m-H\). Thus cycle length alone does not collapse the dense
route back to the canonical packet: variable residence remains a genuine
noncanonical option.

These bounds count complete provider states, including any changed middle
corner, inner order, or outer collar. They therefore include port-only
surgery as well as chain rebundling. A bounded local move changes only a
bounded number of such states, so any collection of moves whose union has
\(o(W)\) provider support fails.

The owner ledger is neutral, not hidden. Both the baseline and proposed
port systems are required to have distinct middle owners. Replacing
\(M\) states vacates at most \(M\) old owners and introduces at most
\(M\) new owners; it does not add paid occurrences. Dense surgery is thus
necessary but is not, by itself, a coefficient obstruction. The surviving
positive route is a genuinely dense, jointly owner-transversal SCD
rebuilding, or a direct all-tag packet factor. No sparse local correction
of a paired scaffold can work.

## 1. Retained SCD providers and exact owner cost

Let \(\mathcal D\) be a full SCD of \(B_{2m}\). A chain of radius \(d\)
has one member at every rank from \(m-d\) through \(m+d\). Retain

\[
 \Omega(\mathcal D)=\{C\in\mathcal D:\operatorname{rad}(C)\ge q_0\}.
\tag{1.1}
\]

Since rank \(m-q\) is partitioned by precisely the chains reaching that
rank,

\[
 |\{C:\operatorname{rad}(C)\ge q\}|=N_q.
\tag{1.2}
\]

In particular, \(|\Omega|=N_{q_0}\). Choose one annular-compatible
radius-\(H\) port for every retained chain. Its middle owner is

\[
 X(\omega)=L+\{z_1,\ldots,z_H\}.
\tag{1.3}
\]

The original SCD middle members give one owner-simple port transversal, and
alternate annular corners are legal provided all chosen owners remain
distinct.

Every designated lower and upper target at depth \(q\) belongs to its
unique chain of tag at least \(q\). Therefore a path forest on all selected
ports already carries every annular target. A path containing \(t\) states
has an exact hard-started word of length \(t+2H\). Summing over \(p\)
paths and appending the \(W-N_{q_0}\) unused middle owners gives (0.3).

For later use, a genuine full rotor successor is

\[
 \begin{aligned}
 &(L;z_1,\ldots,z_{2H};R)\\
 &\quad\longrightarrow
 (L-x+y;x,z_1,\ldots,z_{2H-1};R-y+z_{2H}),
 \end{aligned}
\tag{1.4}
\]

where \(x\in L\), \(y\in R\). At the middle owner level it induces

\[
 \boxed{X(\omega')=X(\omega)-z_H+y.}
\tag{1.5}
\]

Thus a rotor forest is literally a Johnson path forest on the chosen,
distinct paid owners. No owner multiplicity is concealed by the state
notation.

## 2. A sharp graph-theoretic edit lemma

Let \(G\) be any directed graph. For a finite vertex set \(V\), let
\(\lambda_G(V)\) be the maximum number of edges in a directed
vertex-disjoint linear forest contained in \(G[V]\).

### Lemma 2.1 (two edges per changed state)

Let \(V_0,V\) have the same cardinality, and put

\[
 M=|V\setminus V_0|=|V_0\setminus V|.
\tag{2.1}
\]

Then

\[
 \boxed{
 \lambda_G(V)\le\lambda_G(V_0)+2M.}
\tag{2.2}
\]

Equivalently, if \(V\) has a spanning linear forest with \(p\)
components, then

\[
 \boxed{
 p+2M\ge |V|-\lambda_G(V_0).}
\tag{2.3}
\]

#### Proof

Take a maximum linear forest \(F\) on \(V\). Delete the \(M\) vertices
in \(V\setminus V_0\) and every incident forest edge. Since a linear
forest has total degree at most two at each vertex, at most \(2M\) edges
are deleted. The surviving forest lies on \(V\cap V_0\), hence is also a
forest in \(G[V_0]\) after the unused baseline vertices are added as
singletons. Therefore

\[
 |E(F)|-2M\le\lambda_G(V_0),
\]

which proves (2.2). A spanning forest on \(V\) has \(|V|-p\) edges,
giving (2.3). \(\square\)

The coefficient two is sharp as a graph statement: changed and unchanged
vertices may alternate along a path, so every changed vertex can support
two new edges.

### Lemma 2.2 (cycle version)

Suppose \(G[V_0]\) is edgeless, \(V'\) is the vertex set of a directed
cycle factor in \(G\), and put \(M'=|V'\setminus V_0|\). Then

\[
 \boxed{
 |V'|\le2M'.}
\tag{2.4}
\]

#### Proof

Every one of the \(|V'|\) cycle-factor edges has at least one endpoint in
\(V'\setminus V_0\), since \(G[V_0]\) has no edge. Their number is at
most the total cycle degree \(2M'\). \(\square\)

## 3. Paired central labels contain no rotor edge

Fix a perfect matching \(\mathcal P\) on \([2m]\). At radius \(q\), put

\[
 \mathcal U_q(\mathcal P)
 =\left\{\bigcup_{e\in J}e:
          J\subseteq\mathcal P,\ |J|=q\right\}.
\tag{3.1}
\]

### Lemma 3.1 (pair parity)

The family \(\mathcal U_q(\mathcal P)\) is independent in the Johnson
graph \(J(2m,2q)\).

#### Proof

The intersection of two unions of matching pairs is itself a union of
matching pairs and therefore has even cardinality. Johnson adjacency would
require intersection size \(2q-1\), which is odd. \(\square\)

For a radius-\(q\) state

\[
 \theta=(A;w_1,\ldots,w_{2q};B),
\]

put \(Z_q(\theta)=\{w_1,\ldots,w_{2q}\}\). Under a rotor move,

\[
 Z_q(\theta')=Z_q(\theta)-w_{2q}+x,
\tag{3.2}
\]

so the two central labels are adjacent in \(J(2m,2q)\).

### Proposition 3.2 (paired rotor-free baseline)

Let \(V_{0,q}\) be a set of distinct radius-\(q\) states satisfying

\[
 Z_q(\theta)\in\mathcal U_q(\mathcal P)
 \qquad(\theta\in V_{0,q}).
\tag{3.3}
\]

Then the induced radius-\(q\) rotor graph on \(V_{0,q}\) is edgeless.

#### Proof

Equation (3.2) makes the central labels of a rotor edge Johnson adjacent,
contrary to Lemma 3.1. \(\square\)

At full radius \(H\), this applies to every fully \(\mathcal P\)-paired
port system. At every lower threshold it applies to the forced truncations
of every projectively \(\mathcal P\)-paired SCD. Inner reordering cannot
change the set \(Z_q\), so port permutations do not evade the obstruction.

## 4. Genuine rotor forests require half-density rebuilding

Let \(V_0\) be the \(N_{q_0}\) complete states of a fully paired,
owner-simple baseline port system, and let \(V\) be another owner-simple
set of \(N_{q_0}\) retained complete states. Put

\[
 M=|V\setminus V_0|.
\tag{4.1}
\]

### Theorem 4.1 (sharp genuine-rotor surgery bound)

If \(V\) has a spanning genuine radius-\(H\) rotor path forest with
\(p\) paths, then

\[
 \boxed{p+2M\ge N_{q_0}.}
\tag{4.2}
\]

#### Proof

Proposition 3.2 says the full rotor graph induced by \(V_0\) is edgeless,
so \(\lambda(V_0)=0\). Apply Lemma 2.1 to the intrinsic full rotor graph.
\(\square\)

More generally, for an arbitrary owner-simple baseline \(B\), put

\[
 \lambda_H(B)=\lambda_{\mathfrak R_H}(B),
\]

where \(\mathfrak R_H\) is the intrinsic full rotor graph. The same proof
gives the exact stability inequality

\[
 \boxed{
 p+2|V\setminus B|\ge N_{q_0}-\lambda_H(B).}
\tag{4.3}
\]

Thus sparse surgery is excluded around any baseline whose full-rotor linear
forest has deficit \(\Omega(W)\), not only around the paired example.

If \(p=o(W/H)\), then \(p=o(W)\), while

\[
 \frac{N_{q_0}}W=e^{-a^2+o(1)}.
\tag{4.4}
\]

This proves (0.6). Relative to the paid provider mass, the exact conclusion
is

\[
 \frac{M}{N_{q_0}}\ge\frac12-o(1).
\tag{4.5}
\]

Thus changing only collars, only middle corners, or only a sparse set of
whole chains cannot produce the requested rotor forest. At least half the
complete retained state system must leave the paired catalogue.

## 5. Bridge-one forests still require full-top dense surgery

The bridge-one graph also contains promotion arcs. A promotion preserves
the full top fibre

\[
 U_H(\omega)=L+\{z_1,\ldots,z_{2H}\},
\tag{5.1}
\]

whereas a genuine full rotor changes it. The retained SCD contains one
forced top-tag anchor in each of the \(N_H\) rank-\((m+H)\) fibres.

Let \(F\) be a bridge-one spanning linear forest on \(V\), with \(p\)
components, and let \(r_{\rm full}\) be its number of genuine full rotor
edges. Deleting these edges produces \(p+r_{\rm full}\) promotion-only
components. Distinct top anchors lie in distinct fibres, so

\[
 p+r_{\rm full}\ge N_H.
\tag{5.2}
\]

Every full rotor edge of \(F\) has at least one endpoint in
\(V\setminus V_0\), because the full rotor graph on \(V_0\) is empty.
The full-rotor edges form a subgraph of a linear forest, so

\[
 r_{\rm full}\le2M.
\tag{5.3}
\]

### Theorem 5.1 (full-top surgery bound)

Every bridge-one path cover satisfies

\[
 \boxed{p+2M\ge N_H.}
\tag{5.4}
\]

For an arbitrary baseline \(B\), the same deletion argument gives

\[
 \boxed{
 p+\lambda_H(B)+2|V\setminus B|\ge N_H.}
\tag{5.5}
\]

For \(p=o(W/H)\), this is (0.8), since

\[
 N_H/W=e^{-b^2+o(1)}.
\tag{5.6}
\]

Unlike the top-to-top run cut, this obstruction holds for every fixed
\(0<a<b\). Promotions may supply projected shallow rotors, but they cannot
move between the forced full-top fibres.

## 6. The multiscale dense-edit profile

For \(q_0\le q\le H\), let \(V_q\) be the radius-\(q\) truncations of
the target SCD chains of native radius at least \(q\), and let \(V_{0,q}\)
be the corresponding truncation set of a projectively paired baseline.
Both have size \(N_q\). Put

\[
 M_q=|V_q\setminus V_{0,q}|.
\tag{6.1}
\]

### Theorem 6.1 (all-threshold surgery bound)

If the target full states have a bridge-one spanning path forest with
\(p\) paths, then, simultaneously for every \(q_0\le q\le H\),

\[
 \boxed{
 2M_q\ge\bigl(2N_q-N_{q_0}-p\bigr)_+.}
\tag{6.2}
\]

#### Proof

Mark the \(N_q\) target vertices whose chains have native radius at least
\(q\). Along all \(p\) paths, the number of nonempty marked runs is at
most

\[
 (N_{q_0}-N_q)+p.
\]

Hence at least

\[
 N_q-(N_{q_0}-N_q+p)=2N_q-N_{q_0}-p
\tag{6.3}
\]

selected path edges have two marked endpoints. Absorbing the outer
\(H-q\) collar coordinates projects every such bridge edge to a genuine
radius-\(q\) rotor edge between the distinct truncations. These projected
edges form a directed linear forest on \(V_q\).

The paired baseline rotor graph on \(V_{0,q}\) is empty by Proposition
3.2. Lemma 2.1 therefore bounds the projected forest by \(2M_q\), proving
(6.2). \(\square\)

Let \(q=c\sqrt m+O(1)\), where \(a\le c\le b\). Uniformly on this fixed
window,

\[
 \frac{N_q}{W}=e^{-c^2+o(1)}.
\tag{6.4}
\]

Since \(p=o(W/H)=o(W)\), equation (6.2) gives (0.10). The coefficient is
positive exactly for \(c^2-a^2<\log2\).

There is also a cumulative edit-volume consequence. Put

\[
 c_*=\min\{b,\sqrt{a^2+\log2}\}.
\tag{6.5}
\]

Then

\[
 \boxed{
 \sum_{q=q_0}^{H}M_q
 \ge\left(
  \int_a^{c_*}\left(e^{-x^2}-\frac12e^{-a^2}\right)dx-o(1)
 \right)W\sqrt m.}
\tag{6.6}
\]

Indeed, sum (6.2) over the positive range. The Gaussian estimate is uniform
there and gives the Riemann sum. The accumulated \(p\)-term is
\(O(Hp)=o(W)\), negligible even compared with the displayed
\(W\sqrt m\) scale.

Equation (6.6) does not multiply the number of distinct changed providers
by \(\sqrt m\): one dense whole-chain surgery may alter every truncation of
that chain. It does show that a bounded-depth or one-threshold correction
cannot meet all protected rotor cuts simultaneously.

## 7. The length-\(2m\) cycle and residence ledger

Put \(K,\rho\) as in (0.11). Suppose a target construction selects
\(2mK\) retained complete states, with distinct middle owners, and
partitions them into \(K\) genuine radius-\(H\) rotor cycles of length
\(2m\). Let \(V'\) be their state set, and put

\[
 M^{\rm cyc}=|V'\setminus V_0|.
\tag{7.1}
\]

Every one of the \(2mK\) cycle edges is a full rotor edge. Since the
baseline full rotor graph is empty, every cycle edge has a nonbaseline
endpoint. The sum of cycle degrees over the \(M^{\rm cyc}\) nonbaseline
vertices is \(2M^{\rm cyc}\), proving (0.12).

The physical owner route is exact: (1.5) makes every cycle a Johnson cycle
on its \(2m\) distinct middle owners. Cutting and hard-starting the cycles
costs

\[
 (2m+2H)K.
\tag{7.2}
\]

Appending the other \(W-2mK\) middle owners and repairing the designated
targets of the \(\rho\) omitted providers gives total length at most

\[
 \boxed{
 W+2HK+2\rho(H-q_0+1).}
\tag{7.3}
\]

Both extra terms are \(o(W)\). Thus the dense-edit obstruction is not an
owner-cost lower bound: if the required dense cycle factor exists, it still
has coefficient one.

There is an additional residence audit. Write the departure and arrival
labels of a full rotor cycle as \(x_t\in L_t\) and \(y_t\in R_t\), with
\(t\in\mathbb Z_{2m}\). Call the cycle **one-pass** if the departure word
\((x_t)\) is a permutation of \([2m]\). State closure then makes the
arrival word a permutation as well.

### Lemma 7.1 (exact one-pass residence ledger)

In a one-pass length-\(2m\) rotor cycle, every coordinate spends exactly
\(2H\) consecutive states in the ordered singleton queue. If
\(\ell(c)\) and \(r(c)\) denote its numbers of states in the lower and
residual blocks between its unique passages, then

\[
 \boxed{
 \ell(c)+r(c)=2m-2H=2(m-H),}
\tag{7.4}
\]

and

\[
 \boxed{
 \sum_c\ell(c)=\sum_cr(c)=2m(m-H).}
\tag{7.5}
\]

The coordinate belongs to exactly \(\ell(c)+H\) of the \(2m\) middle
owners in the packet. Consequently the following are equivalent:

1. every coordinate occurs in exactly \(m\) packet owners;
2. \(\ell(c)=r(c)=m-H\) for every coordinate;
3. after a cyclic shift of indices,
   \[
   y_{t+m+H}=x_t;
   \tag{7.6}
   \]
4. the packet is the ordinary cyclic-order interval packet generated by
   the departure order \((x_t)\).

#### Proof

Summing the indicator recurrence
\(1_{\{c\in L_{t+1}\}}-1_{\{c\in L_t\}}
=-1_{\{x_t=c\}}+1_{\{y_t=c\}}\) around the closed cycle shows that
every coordinate has equally many departures and arrivals. Thus the
one-pass departure hypothesis also makes the arrival word a permutation.

The queue recurrence in (1.4) gives

\[
 (z_{t,1},\ldots,z_{t,2H})
 =(x_{t-1},x_{t-2},\ldots,x_{t-2H}).
\tag{7.7}
\]

Thus a departed coordinate advances through the queue for exactly \(2H\)
states, then enters \(R\), later moves from \(R\) to \(L\) at its unique
arrival, and later departs \(L\) at its next-period departure. These three
residences partition the \(2m\)-state period, proving (7.4).

At every time \(|L_t|=|R_t|=m-H\). Double counting coordinate-state
incidences in these two blocks proves (7.5). A coordinate remains in the
middle owner throughout its lower-block residence and throughout the first
\(H\) positions of its queue residence, giving owner multiplicity
\(\ell(c)+H\). This proves the equivalence of items 1 and 2.

If \(x_t=c\), then \(c\) enters \(R\) immediately after transition
\(t+2H\). A residual residence of \(m-H\) states makes its arrival occur
at transition \(t+m+H\), proving item 3. Under (7.6), the lower block,
queue, residual block, middle owner, and every displayed chain mask are
consecutive windows of the single cyclic order \((x_t)\). This proves
item 4. The ordinary interval packet plainly has these constant
residences, proving the converse. \(\square\)

Thus length \(2m\) plus one-pass usage does not force the canonical packet:
the vectors \((\ell(c),r(c))\) may fluctuate subject to (7.4)--(7.5).
Variable residence is a genuine noncanonical freedom. Any positive dense
construction may exploit it, but it must still maintain owner simplicity
and all SCD mask disjointness. The local-surgery obstruction above does not
assume constant residence.

If the cycles may use promotions, let \(r_{\rm full}^{\rm cyc}\) be their
number of genuine full rotor edges. Cut one edge in every cycle. At most
\(K\) full rotor edges and at most \(\rho\) top anchors are lost. The
full-top fibre argument gives

\[
 r_{\rm full}^{\rm cyc}\ge N_H-\rho-K.
\tag{7.8}
\]

Every one of these edges touches a nonbaseline state, and the cycle degree
bound gives \(r_{\rm full}^{\rm cyc}\le2M^{\rm cyc}\). This proves
(0.13).

## 8. Consequence for local surgery templates

Consider any sequence of exact SCD/port surgeries beginning at the paired
baseline. Let \(S_i\) be the set of retained complete states changed by
move \(i\), and put

\[
 S=\bigcup_iS_i.
\tag{8.1}
\]

States touched and later restored to their original complete port do not
belong to the final edit set; every final nonbaseline state does belong to
\(S\). Hence \(M\le|S|\), and Theorems 4.1 and 5.1 give the following
necessary conditions.

### Corollary 8.1 (no sparse local surgery)

For a genuine rotor forest with \(p=o(W/H)\),

\[
 |S|\ge\left(\frac12e^{-a^2}-o(1)\right)W.
\tag{8.2}
\]

For a bridge-one forest,

\[
 |S|\ge\left(\frac12e^{-b^2}-o(1)\right)W.
\tag{8.3}
\]

If every surgery touches at most \(s=s(m)\) retained states, the number of
moves is at least \(|S|/s\). In particular, bounded-template surgery needs
\(\Omega(W)\) effective moves, and any family of moves supported on
\(o(W)\) total provider mass fails.

The same conclusion applies to a library of pair-frame changes, tail swaps,
leaf rectangles, adjacent-chain splices, or local product-box phase changes:
their detailed legality is irrelevant until their union changes a linear
number of complete retained states. Overlapping the moves cannot evade the
bound, because only their final state union enters (2.1).

## 9. Exact scope and surviving construction

Proved here:

1. the exact two-edge Lipschitz bound for changes of the retained port set;
2. rotor-freeness of every fixed-pair central-label scaffold at every
   protected radius;
3. the half-density rebuilding requirement for a genuine rotor forest;
4. the full-top dense-edit requirement even with promotions;
5. the simultaneous all-threshold edit profile and its Gaussian integral;
6. the length-\(2m\) cycle version; and
7. the exact owner and omitted-provider compiler ledger after dense edits.

Not proved here:

1. an integral dense rebuilding of one SCD;
2. a jointly owner-simple port transversal for such a rebuilding;
3. a length-\(2m\) rotor cycle factor; or
4. coefficient one.

The obstruction is sharp for the stated local route. The factor \(2\) in
the edit lemma cannot be improved without using more geometry, and all
Gaussian coefficients come from exact SCD tag counts. It does not say that
dense surgery costs a linear number of word letters: owner mass remains
exactly \(N_{q_0}\), and the compiler ledger (7.3) is still
\(W+o(W)\). It says instead that the successful construction, if it exists,
must be globally noncanonical on positive provider mass. The next positive
lemma cannot be a sparse correction theorem; it must be a dense packet
packing or a dense owner-correlated SCD resolution.
