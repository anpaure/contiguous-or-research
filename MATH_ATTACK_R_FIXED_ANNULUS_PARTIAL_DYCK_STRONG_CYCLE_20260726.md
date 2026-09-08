# Lane R: corrected fixed-annulus partial rethreading, mesoscopic Dyck circuits, and strong-cycle cuts

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, web
input, or fixed-uniformity matching theorem is used.

## 0. Outcome and exact scope

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 q_0=\lceil a\sqrt m\rceil,\qquad H=\lfloor b\sqrt m\rfloor,
\tag{0.1}
\]

where \(0<a<b\) are fixed, and write

\[
 N_q=\binom{2m}{m-q},\qquad
 K=\left\lfloor\frac{N_{q_0}}{2m}\right\rfloor,
 \qquad M=2mK=N_{q_0}-\rho,\quad 0\le\rho<2m.
\tag{0.2}
\]

Thus

\[
 \frac{M}{W}=e^{-a^2}+o(1),\qquad
 \frac{K}{\operatorname {Cat}_m}=\frac{e^{-a^2}}2+o(1).
\tag{0.3}
\]

Only these \(M\) paid middle occurrences need cyclic rethreading.  This
invalidates one conclusion of the earlier full-factor lane: components
longer than \(2m\) are not needed.  The \(K\) ordinary packet collars cost

\[
 2HK=O_{a,b}(W/\sqrt m)=o(W).
\tag{0.4}
\]

The present note gives four new exact conclusions and audits two positive
families.

1.  There is an architecture-free successor cut.  At every controlled
    depth (q), any successful packet family contains at least

    \[
    2N_q-M-h_q^--h_q^+-2C_0
    \tag{0.5}
    \]

    successor edges whose lower tails and upper heads are injectively
    represented on their respective sides, with owner-simple tails and
    owner-simple heads.  A stronger same-state version
    contains a triple-rainbow directed linear forest of size at least

    \[
    4N_q-3M-2(h_q^-+h_q^+)-2C_0-K.
    \tag{0.6}
    \]

    Hence at (q=x\sqrt m+O(1)) the required capacities are respectively

    \[
    \bigl(2e^{-x^2}-e^{-a^2}-o(1)\bigr)W
    \tag{0.7}
    \]

    and

    \[
    \bigl(4e^{-x^2}-3e^{-a^2}-o(1)\bigr)W.
    \tag{0.8}
    \]

    The first is positive for (x^2-a^2<\log2); the second is positive
    for (x^2-a^2<\log(4/3)).

2.  The cuts are genuinely multidepth.  For every

    \[
    a<c<\min\{b,\sqrt{a^2+\log(4/3)}\},
    \tag{0.9}
    \]

    a positive linear number of physical successor edges must be
    triple-rainbow at a positive multiple of (sqrt m) different depths.
    Exact constants are given in Theorem 3.1.  Marginal packet supply at
    each depth is therefore not enough; one common strong-cycle bank must
    carry Gaussian-many colours per edge.

3.  A forest of one-splice successor switches only coarsens the old
    wreath-row partition.  Selecting its final components gives only
    unions of complete old rows, so it cannot improve the optimum of any
    arc-local lower-prefix partial-selection problem.  In particular the
    earlier positive-density
    (1100R\leftrightarrow1010R) one-splice bank is irrelevant to the
    corrected gate: it saves an already-(o(W)) collar term but creates no
    new packet-selection mobility.

4.  Every proper one-hole/contiguous-carrier Catalan family has too little
    action to repair a specified linear tight-layer plateau.  If each of
    the (K) selected packet rows may be
    changed only inside a common contiguous carrier of (b) positions,
    the two signed tight-layer hole counts can change in total by at most

    \[
    4bK=\frac{4bM}{n}.
    \tag{0.10}
    \]

    Repairing a fixed positive (W)-scale plateau forces (b=\Omega(m)).
    Thus every one-hole lift with (b=o(m)), including all
    (b=\Theta(\sqrt m)) local carriers, is statewise insufficient as a
    repair of such a baseline at one Gaussian layer.  This does not rule
    out a library which already contains an independently good row
    family.

The exact mesoscopic two-packet switch from
`MATH_THEOREM_FIXED_ANNULUS_MESOSCOPIC_TWO_PACKET_SWITCH_20260726.md`
escapes Item 4 in the only possible way: it preserves the tight deck
exactly and acts at later depths.  For width (t=\Theta(\sqrt m)) it has
\(\Theta(W)\) aggregate annular variation over \(K/2\) components.  The
audit below improves its protected-orbit relative pair-codegree to

\[
 \frac{5+o(1)}{m^2}
\tag{0.11}
\]

at the tight rank, independently of (t=O(\sqrt m)).  Nevertheless, at
one fixed depth all component bits together change only (O(W/\sqrt m)).
Therefore this family is a final correlated (O(W))-residual orienter,
not a construction of the protected base.  That base must already have
(o(W)) holes at every depth.

Independently, an extensive reciprocal-\(C_8\) cube with
\(\Theta(m)\) disjoint Dyck slots gives \(2^{\Theta(m)}\) literal
anchored exact factors, changes all but \(O(\operatorname {Cat}_m/m)\)
rows, and has exact edit mass
\((\alpha_0/4+o(1))W\).  This is a genuine root-scale non-row-power
family and is the first Catalan construction not excluded by the local
action theorem.  Its productive row selection remains open.

No coefficient-one construction is claimed.  No universal obstruction is
proved for the complete ordinary-cyclic-order catalogue: its fractional
capacities and its ungrouped integral provider supply remain feasible.
What is now ruled out is forest fusion as a source of arc-local selection
mobility and sublinear contiguous carriers as repairs of a linearly
deficient baseline; what survives is a whole-row or dispersed
multi-hole strong-cycle design satisfying the common multidepth cuts.

## 1. Packet occurrence ledgers

Let (mathcal F) be a family of (K) directed cyclic orders on
([n]).  Its occurrence set is

\[
 \Omega=\{(\pi,j):\pi\in\mathcal F,\ j\in\mathbb Z_n\},
 \qquad |\Omega|=M.
\tag{1.1}
\]

Let

\[
 \sigma(\pi,j)=(\pi,j+1)
\tag{1.2}
\]

be the packet successor permutation.  It consists of exactly (K)
directed (n)-cycles.

For (q_0\le q\le H), define

\[
 \ell_q(\pi,j)=I_\pi(j,m-q),\qquad
 u_q(\pi,j)=I_\pi(j,m+q),\qquad
 o(\pi,j)=I_\pi(j,m).
\tag{1.3}
\]

Write

\[
 h_q^-=N_q-|\ell_q(\Omega)|,\qquad
 h_q^+=N_q-|u_q(\Omega)|,
\tag{1.4}
\]

and

\[
 C_0=M-|o(\Omega)|.
\tag{1.5}
\]

For ordinary packets complementation gives (h_q^-=h_q^+), but keeping
the two signs separate makes the successor cuts transparent and permits
use inside asymmetric restricted catalogues.

The corrected literal compiler ledger is

\[
 L\le W+2HK+C_0+\sum_{q=q_0}^H(h_q^-+h_q^+)+O(m).
\tag{1.6}
\]

Thus the desired hypotheses are

\[
 C_0=o(W),\qquad
 \sum_{q=q_0}^H(h_q^-+h_q^+)=o(W).
\tag{1.7}
\]

At the entrance rank, if (c_{q_0}) is the repeat excess, occurrence
conservation gives

\[
 c_{q_0}-h_{q_0}^-=M-N_{q_0}=-\rho,
 \qquad h_{q_0}^-=c_{q_0}+\rho.
\tag{1.8}
\]

No independence assumption is made anywhere below.

## 2. The two-sided successor and strong-cycle cuts

Choose a set (A_q\subseteq\Omega) containing exactly one occurrence of
every covered lower target.  Choose (B_q\subseteq\Omega) analogously
for the upper targets, and choose (O\subseteq\Omega) containing exactly
one occurrence of every distinct middle owner.  Then

\[
 |A_q|=N_q-h_q^-,\qquad |B_q|=N_q-h_q^+,
 \qquad |O|=M-C_0.
\tag{2.1}
\]

### Theorem 2.1 (owner-simple two-sided successor matching cut)

The selected packet cycles contain at least

\[
 \boxed{
 2N_q-M-h_q^--h_q^+-2C_0}
\tag{2.2}
\]

successor edges \(v\to\sigma v\) such that

\[
 v\in A_q\cap O,\qquad \sigma v\in B_q\cap O.
\tag{2.3}
\]

Their tails have pairwise distinct lower colours and pairwise distinct
middle owners; their heads have pairwise distinct upper colours and
pairwise distinct middle owners.  A head of one edge may equal the tail
of another edge.  Thus this is a matching between left and right copies
of the occurrence set, but not necessarily a vertex-disjoint matching in
the physical successor cycles.  Negative right sides are read as the
trivial bound zero.

#### Proof

Put

\[
 X=A_q\cap O,qquad Y=\sigma^{-1}(B_q\cap O).
\]

Since \(|\Omega\setminus O|=C_0\),

\[
 |X|\ge |A_q|-C_0,qquad |Y|\ge |B_q|-C_0.
\]

Therefore

\[
 |X\cap Y|
 \ge |A_q|+|B_q|-2C_0-M,
\]

which is (2.2).  Every \(v\in X\cap Y\) supplies the edge in (2.3).
The representative definitions make the asserted colours injective on
each side.  If a physical vertex-disjoint matching is desired, every
directed path or cycle of selected successor edges has a matching of at
least half its edges.  Extracting these componentwise gives at least half
of (2.2), and then all physical endpoint owners are pairwise distinct.
\(\square\)

For a restricted legal packet/trade catalogue, let
\(\kappa_q^{\rm own}\) be the largest left/right-copy successor matching
having the sidewise injectivity properties in Theorem 2.1.  Every successful
selection necessarily satisfies

\[
 \boxed{
 \kappa_q^{\rm own}
 \ge2N_q-M-h_q^--h_q^+-2C_0.}
\tag{2.4}
\]

This is a statewise catalogue obstruction, not a fractional degree test.

### Theorem 2.2 (triple-rainbow strong-cycle forest cut)

Let (lambda_q^{\rm str}) be the maximum number of arcs in a directed
linear forest of packet successor arcs whose vertices have pairwise
distinct lower, upper, and middle-owner labels.  Then

\[
 \boxed{
 \lambda_q^{\rm str}
 \ge4N_q-3M-2(h_q^-+h_q^+)-2C_0-K.}
\tag{2.5}
\]

#### Proof

Put

\[
 S_q=A_q\cap B_q\cap O.
\]

The three-set inclusion bound gives

\[
 |S_q|
 \ge |A_q|+|B_q|+|O|-2M
 =2N_q-M-h_q^--h_q^+-C_0.
\tag{2.6}
\]

Because (sigma) is a permutation of an (M)-set,

\[
 |S_q\cap\sigma^{-1}S_q|\ge2|S_q|-M.
\tag{2.7}
\]

These are the successor arcs with both endpoints in (S_q).  They form
a disjoint union of directed paths and directed cycles.  A directed cycle
can occur only when (S_q) contains an entire one of the (K) packet
cycles.  Delete one arc from each such cycle.  The resulting directed
linear forest has at least

\[
 2|S_q|-M-K
 \ge4N_q-3M-2(h_q^-+h_q^+)-2C_0-K
\]

arcs.  Membership in (A_q,B_q,O) gives the three injective vertex
labels.  \(\square\)

### Corollary 2.3 (Gaussian constants)

If (q=x\sqrt m+O(1)), with fixed (x\in[a,b]), and (1.7) holds, then

\[
 \kappa_q^{\rm own}
 \ge\bigl(2e^{-x^2}-e^{-a^2}-o(1)\bigr)W,
\tag{2.8}
\]

and

\[
 \lambda_q^{\rm str}
 \ge\bigl(4e^{-x^2}-3e^{-a^2}-o(1)\bigr)W.
\tag{2.9}
\]

#### Proof

Uniformly at fixed Gaussian (x),

\[
 \frac{N_q}{W}=e^{-x^2}+o(1),\qquad
 \frac{M}{W}=e^{-a^2}+o(1).
\]

Every individual hole count is (o(W)) under (1.7), while
(C_0=o(W)) and (K=O(W/m)=o(W)).  Substitute in (2.4) and (2.5).
\(\square\)

The positivity thresholds in (0.7)--(0.8) follow immediately.  The
strong-cycle threshold (log(4/3)) is weaker than the SCD top-tag
threshold (log2), because a common SCD identifies the designated
lower and upper provider states.  No such identification is available in
an arbitrary packet family.

## 3. Positive-density multidepth strong edges

The preceding cuts cannot be met independently at each depth.

Fix (c) as in (0.9), and set

\[
 \alpha=e^{-a^2},\qquad \ell=c-a,
\tag{3.1}
\]

\[
 J_4(a,c)=\int_a^c\left(4e^{-x^2}-3e^{-a^2}\right)\,dx.
\tag{3.2}
\]

The choice (0.9) makes (J_4(a,c)>0), and
(J_4(a,c)<\alpha\ell).

For each (q_0\le q\le\lfloor c\sqrt m\rfloor), choose the
representatives in Section 2, and call a physical successor edge
(q)-strong when both endpoints lie in (S_q=A_q\cap B_q\cap O).

### Theorem 3.1 (Gaussian multidepth strong-cycle bank)

Assume (1.7).  Put

\[
 \eta_{a,c}=\frac{J_4(a,c)}{2e^{-a^2}},\qquad
 \delta_{a,c}=\frac{J_4(a,c)}{2(c-a)}.
\tag{3.3}
\]

Then, for all sufficiently large (m), at least

\[
 \boxed{(\delta_{a,c}-o(1))W}
\tag{3.4}
\]

physical successor edges are (q)-strong for at least

\[
 \boxed{(\eta_{a,c}-o(1))\sqrt m}
\tag{3.5}
\]

different depths (q\in[q_0,\lfloor c\sqrt m\rfloor]).

The same conclusion holds with (q)-strong linear-forest arcs after
changing the (o(1)) terms; deleting at most one edge per packet cycle
at each depth costs only (K\,O(\sqrt m)=o(W\sqrt m)) total
edge-depth incidences.

#### Proof

By (2.6)--(2.7), the number (s_q) of (q)-strong successor edges is at
least

\[
 s_q\ge
 4N_q-3M-2(h_q^-+h_q^+)-2C_0.
\tag{3.6}
\]

Summing (3.6) and using the Gaussian Riemann sum gives

\[
 \sum_{q=q_0}^{\lfloor c\sqrt m\rfloor}s_q
 \ge\bigl(J_4(a,c)+o(1)\bigr)W\sqrt m.
\tag{3.7}
\]

Indeed, the aggregate hole subtraction is (o(W)), the (C_0)
subtraction is (o(W)O(\sqrt m)=o(W\sqrt m)), and the endpoint rounding
is (o(W\sqrt m)).

Let (g(e)) be the number of these depths at which physical successor
edge (e) is strong.  There are (M=(\alpha+o(1))W) physical successor
edges in total, and

\[
 g(e)\le(\ell+o(1))\sqrt m.
\]

Let (R) be the set of edges with
(g(e)\ge(\eta_{a,c}-o(1))\sqrt m).  Then

\[
 \sum_eg(e)
 \le |R|(\ell+o(1))\sqrt m
      +M(\eta_{a,c}+o(1))\sqrt m.
\tag{3.8}
\]

Combine (3.7)--(3.8) and use
(alpha\eta_{a,c}=J_4(a,c)/2).  This gives

\[
 |R|\ge
 \left(\frac{J_4(a,c)}{2\ell}-o(1)\right)W,
\]

which is (3.4).  For the forest form, apply the deletion in Theorem 2.2
at each depth.  Its total loss is at most

\[
 K(\ell+o(1))\sqrt m=O(W/\sqrt m)=o(W\sqrt m),
\]

and absorb it into (3.7).  \(\square\)

This theorem is the promised dependency statement.  It does not assign
independent cube signs to depths.  One fixed positive-density bank of
physical successor edges must simultaneously carry a positive fraction of
the Gaussian depth interval.

## 3.2 SCD endpoint antipode: an exact cycle-monodromy obstruction

The common-SCD scaffold has an additional obstruction which is absent
from the path formulation.  Let

\[
 \Omega_{\rm SCD}=\mathcal D_{\ge q_0},
\qquad
 D(C)=C_{-q_0},\qquad E(C)=C_{q_0}.
\tag{3.9}
\]

Both endpoint maps are bijections onto their Boolean ranks.  Define the
permutation \(\iota\) of \(\Omega_{\rm SCD}\) by

\[
 D(\iota C)=E(C)^c.
\tag{3.10}
\]

### Theorem 3.2 (endpoint antipode law)

If SCD providers \(C_t\) are placed at the phases of a literal
length-\(2m\) cyclic packet while preserving both prescribed
depth-\(q_0\) endpoints, then

\[
 \boxed{C_{t+m}=\iota(C_t).}
\tag{3.11}
\]

Consequently every selected provider satisfies

\[
 \boxed{\iota^2(C)=C.}
\tag{3.12}
\]

If all but the floor remainder \(\rho\) of the \(N_{q_0}\) providers are
put in ordinary packets, at most \(\rho\) vertices of \(\iota\) may lie
outside its two-cycles.

#### Proof

Write one physical cyclic order as
\(z_0,\ldots,z_{2m-1}\).  Its lower and upper depth-\(q_0\) endpoints at
phase \(t\) are

\[
 D_t=\{z_{t+q_0},\ldots,z_{t+m-1}\},
\qquad
 E_t=\{z_t,\ldots,z_{t+m+q_0-1}\}.
\]

At the antipodal phase,

\[
 D_{t+m}=E_t^c.
\]

The definition of \(\iota\) and injectivity of the SCD lower-endpoint map
give (3.11).  Apply the half-turn twice to obtain (3.12).  No fixed point
is possible because \(D(C)\subset E(C)\), whereas \(E(C)^c\) is disjoint
from \(E(C)\).  Therefore every selected provider lies in a genuine
two-cycle, and omitting only \(\rho\) providers proves the final claim.
\(\square\)

This is a sharp strong-cycle obstruction for an arbitrary SCD followed by
cycle closure.  It is not an obstruction to the run-compressed path
compiler in Section 7.5, which deliberately has no antipodal closure.

## 4. Exact degree-two frustration in a restricted Catalan catalogue

Let \(\mathscr C\) be any finite catalogue of legal ordinary packets.  At
the entrance rank (m-q_0), every packet contains a target at most once.
Form the multigraph (G_2(\mathscr C)) whose vertices are catalogue
packets and whose edges are those entrance targets which occur in exactly
two catalogue packets.  Parallel edges are retained because they are
different literal targets.

For (x\in\{0,1\}^{\mathscr C}), an edge (uv) is satisfied exactly
when

\[
 x_u\oplus x_v=1.
\tag{4.1}
\]

Let

\[
 \tau_K(G_2)=min_{x:\,\sum x=K}
 |\{uv:x_u=x_v\}|.
\tag{4.2}
\]

### Theorem 4.1 (tight-layer frustration obstruction)

Every \(K\)-packet selection from \(\mathscr C\) has entrance hole count

\[
 \boxed{
 h_{q_0}^-\ge\frac{\tau_K(G_2)+\rho}{2}.}
\tag{4.3}
\]

In particular, if (G_2) contains (t) edge-disjoint odd cycles, then

\[
 \boxed{h_{q_0}^-\ge\frac{t+\rho}{2}.}
\tag{4.4}
\]

#### Proof

For a degree-two target (T) on edge (uv), its selected load is
(x_u+x_v).  If (4.1) fails, this load is zero or two, and (T)
contributes exactly one to the sum

\[
 h_{q_0}^-+c_{q_0}.
\]

All other targets contribute nonnegatively, so

\[
 h_{q_0}^-+c_{q_0}\ge\tau_K(G_2).
\]

Equation (1.8) says (c_{q_0}=h_{q_0}^--\rho).  Rearrangement proves
(4.3).  Every binary labelling violates an edge of each odd cycle, and
edge-disjoint cycles force distinct violated target edges, proving
(4.4).  \(\square\)

Degree-one targets give pins (x_u=1).  Degree-two middle-owner overlaps
give not-both clauses (x_u+x_v\le1) if middle collision is to vanish.
Thus the degree-one/two part of a restricted Catalan catalogue is an exact
signed frustration network, not a marginal-density problem.  Targets of
degree at least three give exact-one hypergraph clauses and must be kept;
the graph theorem deliberately makes no claim about them.

No available PBBS/MSW multiplicity theorem proves that a proposed
Catalan catalogue has \(\Omega(W)\) degree-two targets or an
\(\Omega(W)\) edge-disjoint odd-cycle packing.  Therefore Theorem 4.1 is
an exact obstruction test, not an unconditional no-go for the complete
catalogue.

## 5. Why forest successor fusion gives no corrected mobility

Start with directed wreath rows (R_1,\ldots,R_s), each a circuit of
ordered owner arcs.  A one-splice successor switch between two rows
crosses their successor pairings at one common ordered state and changes
no arc.

### Theorem 5.1 (forest fusion only coarsens rows)

Suppose one performs one such splice for every edge of a forest (F) on
the original row set, at distinct physical cut incidences.  Then every
final circuit is the disjoint union of the complete arc sets of all old
rows in one connected component of (F).  Consequently, for every
arc-local target map \(\phi\), the target histogram of a selected family
of final circuits is the histogram of a union of complete original rows.

In particular,

\[
 \min_{\text{selected final components}}
  h(\phi)
 \ge
 \min_{\text{arbitrary selected original rows}}
  h(\phi)
\tag{5.1}
\]

at the corresponding allowed occurrence mass.

#### Proof

Order the forest edges so that each new edge joins two previously
different forest components.  Initially every graph component is one
row circuit.  A successor transposition between two different directed
circuits merges them into one directed circuit and retains every arc.
Induction shows that after processing a forest component, its unique
circuit contains exactly all arcs of its row vertices.  Different forest
components remain disjoint.  Selecting final circuits therefore selects
unions of full original rows.  Since arbitrary original-row selection
allows at least these unions, (5.1) follows.  \(\square\)

Every lower prefix of an ordered owner arc is arc-local.  Hence the
positive (1100R\leftrightarrow1010R) bank in the predecessor report,
whose switch graph is a matching, cannot improve the corrected lower
partial-design optimum.  For ordinary complete cyclic packets, upper
support is the complement image of lower support, so an upper-only choice
cannot rescue a bad lower floor.  The theorem by itself makes no statement
about a different non-arc-local upper functional attached to a merged
singleton circuit.  Its component merging was valuable only when a linear
collar count was feared.  Equation (0.4) removes that motive.

Genuine partial-design mobility requires a switch circuit: at least two
cuts in a connected row bundle, arranged so that segments rather than
whole rows are exchanged.  This is a necessary condition, not a claim
that every switch circuit is legal or useful.

## 6. Contiguous-carrier action and the root-scale no-go

### Lemma 6.1 (one contiguous carrier changes few intervals)

Let two cyclic orders \(\pi,\pi'\) have the same exterior order and the
same set of labels in one contiguous block of (b) positions, differing
only in the internal order of that block.  If

\[
 b\le r\le n-b,
\tag{6.1}
\]

then at most (2(b-1)) start positions have different length-(r)
interval sets in \(\pi\) and \(\pi'\).

#### Proof

An interval is unchanged if it contains none or all of the carrier.
Every changed interval has exactly one of its two boundary cuts strictly
inside the carrier.  There are (b-1) internal cuts, and either boundary
may use one.  Condition (6.1) prevents an interval or its complement from
using both carrier boundary arcs, so this count is valid.  \(\square\)

Changing one interval occurrence changes a hole count by at most one.
Complementation gives the same bound at the opposite sign.

### Theorem 6.2 (sublinear contiguous-carrier no-go)

Suppose a (K)-packet family is assembled from packet options which, row
by row, differ from a fixed baseline only inside a contiguous
(b)-position carrier with the same carrier label set.  At every depth
where (6.1) holds,

\[
 |h_q^-(\mathrm{new})-h_q^-(\mathrm{base})|
 \le2bK,
\tag{6.2}
\]

and

\[
 |(h_q^-+h_q^+)(\mathrm{new})
   -(h_q^-+h_q^+)(\mathrm{base})|
 \le4bK=\frac{4bM}{n}.
\tag{6.3}
\]

If the baseline has a two-sign hole excess at least \(\varepsilon W\)
at one fixed Gaussian depth and the output has \(o(W)\) holes there, then

\[
 \boxed{
 b\ge\left(\frac{\varepsilon}{4e^{-a^2}}-o(1)\right)n.}
\tag{6.4}
\]

#### Proof

Apply Lemma 6.1 to each of the (K) rows and sum the occurrence-change
bounds.  Equation (6.3) and (M/W=e^{-a^2}+o(1)) give (6.4).
\(\square\)

Thus a proper one-hole Dyck lift of carrier width (b=o(m)) has only
(o(W)) fixed-depth action even when supplied at every selected row.
This is stronger than an aggregate (H)-depth action count: overlapping
seam influence cannot be charged independently at one layer.  A viable
family must use an essentially whole-row carrier or several separated,
exterior-moving holes whose total fixed-depth influence is \(\Theta(m)\)
per selected packet.

## 7. The mesoscopic protected switch: exact escape and exact limit

The protected two-packet component has shores

\[
 \mathcal A=\{UP,JVQ\},\qquad
 \mathcal B=\{VP,JUQ\},
\tag{7.1}
\]

with block width (2\le t<q_0), as defined in the cited mesoscopic
theorem.  Its exact identities are

\[
 \mathbf I_m(\mathcal A)=\mathbf I_m(\mathcal B),\qquad
 \mathbf I_{m-q_0}(\mathcal A)=
 \mathbf I_{m-q_0}(\mathcal B).
\tag{7.2}
\]

At offset (s\ge1), its signed lower change has

\[
 \|d_{q_0+s}^-\|_1=4\min\{s,t-1\},
\tag{7.3}
\]

and the upper change is the complement image.  Therefore (K/2+O(1))
components of width \(t=\Theta(\sqrt m)\) have \(\Theta(W)\) aggregate
variation through the annulus.

At one fixed offset, however, all component bits together change the
two-sign hole count by at most

\[
 2K\min\{s,t-1\}=O_{a,b}(W/\sqrt m)=o(W).
\tag{7.4}
\]

This is the decisive scope boundary.  A protected-base selection with a
linear hole plateau at even one depth cannot be repaired by these bits.

The original protected-orbit audit bounded the tight relative codegree by
(O(m^{-3/2})).  The following interval lemma removes the spurious factor
(t).

### Lemma 7.1 (three adjacent intervals in a foreign deck)

Let \(2<r<n/2\), fix \(S\in\binom{[n]}r\), and let \(\tau\) be any cyclic
order on \([n]\).  At most three members \(T\in\mathcal I_r(\tau)\)
satisfy

\[
 |S\setminus T|=|T\setminus S|=1.
\tag{7.5}
\]

#### Proof

Any two such intervals (T,T') have Johnson distance at most two by the
triangle inequality through (S).  For (r<n/2), two cyclic
(r)-intervals whose starts have circular distance (d\le r) have
Johnson distance (d); if their circular start distance exceeds (r),
they are disjoint and have distance \(r>2\).  Hence all relevant starts
are pairwise within circular distance two.  On a cycle of length
\(n>6\), such a set has at most three starts.  \(\square\)

### Theorem 7.2 (sharp distance-one codegree of a two-deck orbit)

Let

\[
 \mathcal R=\mathcal I_r(\pi)\cup\mathcal I_r(\tau),
 \qquad \varrho=|\mathcal R|,
\tag{7.6}
\]

and assume \(\varrho=(2-o(1))n\).  In the complete labelled coordinate orbit
of \(\mathcal R\), the normalized codegree of two distinct rank-\(r\)
targets at Johnson distance one is at most

\[
 \boxed{
 \frac{10n}{\varrho\,r(n-r)}
 =\frac{5+o(1)}{r(n-r)}.}
\tag{7.7}
\]

In particular, for \(r=m-q_0\),

\[
 \boxed{
 \frac{\Delta_2}{D}\le\frac{5+o(1)}{m^2}.}
\tag{7.8}
\]

#### Proof

Inside one cyclic deck there are exactly (2n) ordered distance-one
pairs, one for each start and each direction.  The two within-deck
contributions therefore total (4n).  By Lemma 7.1, a fixed interval in
the first deck has at most three distance-one partners in the second;
this gives at most (3n) ordered cross pairs in one direction and (3n)
in the other.  Thus the template has at most (10n) ordered
distance-one pairs.

For a transitive coordinate orbit, double counting ordered template pairs
gives

\[
 \frac{\operatorname {codeg}(S,T)}{D}
 =\frac{A_1}{\varrho\,r(n-r)},
\]

where \(A_1\) is the template ordered-pair count.  Substitute
\(A_1\le10n\).  At \(r=m-q_0\),
\(r(n-r)=m^2-q_0^2=(1-o(1))m^2\).
\(\square\)

For completeness, distance one is the worst nontrivial stratum at the
tight rank.  If \(2\le d\le r\), the crude template bound
\(A_d\le\varrho^2=O(m^2)\) and orbit double counting give

\[
 \frac{\lambda_d}{D}
 \le
 \frac{\varrho}{\binom rd\binom{n-r}d}.
\tag{7.8a}
\]

The denominator is log-concave in \(d\), so its minimum on
\(\{2,\ldots,r\}\) is attained at an endpoint.  At \(d=2\) it is
\(\Theta(m^4)\), while at \(d=r=m-q_0\) it equals
\(\binom{m+q_0}{2q_0}\), which is superpolynomial.  Hence every
distance-\(d\ge2\) ratio is \(O(m^{-3})\).  At the middle rank,
complement contraction identifies \(d=m-1\) with the distance-one
stratum and \(d=m\) with the same atom; all remaining strata obey the
same \(O(m^{-3})\) estimate.

The protected component has

\[
 \varrho\ge2n-(2q_0+4t-2)=(2-o(1))n
\]

for (t=O(\sqrt m)), so Theorem 7.2 applies.  At the middle rank one
first contracts complementary owners; the same argument, allowing both
representatives of a complement atom, gives an (O(m^{-2})) normalized
codegree.  Mixed middle--entrance codegrees remain

\[
 \exp[-\Theta_a(\sqrt m\log m)].
\tag{7.9}
\]

There is also a useful conditioned second-moment bound at the entrance
rank \(r=m-q_0\).  Put

\[
 D_d=\binom rd\binom{n-r}d,\qquad
 g_d=A_d/\varrho.
\]

Thus \(g_d\) is the average number of other template targets at Johnson
distance \(d\).  For two independent uniform labelled-orbit blocks,
conditioned to contain a fixed entrance target, distance transitivity
gives the exact expected additional intersection

\[
 \Gamma
 =\sum_{d=1}^{r}
   \frac{g_d^2}{\binom rd\binom{n-r}d}.
\tag{7.10}
\]

Here \(g_1\le5+o(1)\) and \(g_d\le\varrho=O(m)\).  To sum the
remaining strata, note the exact ratio

\[
 \frac{D_{d+1}}{D_d}
 =\frac{(r-d)(n-r-d)}{(d+1)^2}.
\tag{7.10a}
\]

For \(2\le d\le r/4\), this ratio is bounded below by an absolute
constant greater than one for all large \(m\).  Hence the reciprocal
sum on this range is \(O(D_2^{-1})=O(m^{-4})\).  On
\(r/4\le d\le r\), log-concavity makes the minimum occur at an
endpoint; \(D_{r/4}\) is exponentially large and

\[
 D_r=\binom{m+q_0}{2q_0}
     =\exp(\Theta_a(\sqrt m\log m)).
\]

The tail reciprocal sum is therefore \(o(m^{-4})\).  It follows that
the \(d\ge2\) contribution to (7.10) is
\(O(m^2)\,O(m^{-4})=O(m^{-2})\), while the \(d=1\) contribution is
also \(O(m^{-2})\).  Consequently

\[
 \boxed{\Gamma=O(m^{-2}).}
\tag{7.11}
\]

Equation (7.11) is deliberately restricted to the entrance rank.  For
an uncontracted middle deck, complement closure would contribute one at
distance \(m\); no raw-middle version is asserted.  Equations (7.8) and
(7.11) show that neither entrance pair codegrees nor entrance local
overlap moments obstruct the protected-deck matching.  They do not prove
it.  The edge size grows like (m), and the same favorable pair geometry
already occurs in the unresolved ordinary tight-cycle packet hypergraph.
A hereditary residual-regeneration or interval-specific matching theorem
is still required.

## 7.3 A genuine extensive Catalan bank

The strongest presently certified growing Dyck family is the extensive
reciprocal-\(C_8\) cube in
MATH_ATTACK_K_CATALAN_EXTENSIVE_C8_ANNULUS_PACKET_GATE_20260726.md.
Choose

\[
 u=\lfloor\alpha_0m\rfloor,\qquad 0<\alpha_0<1/2,
\tag{7.12}
\]

pairwise disjoint four-position slots in a Dyck word, and at every
chosen slot use the sealed reciprocal replacement

\[
 1100\longleftrightarrow1010.
\tag{7.13}
\]

For every global mask \(A\subseteq[u]\), the row-dependent substitution

\[
 F^A(x)=h_{A,x}F(h_{A,x}x)
\tag{7.14}
\]

is a literal anchored exact factor.  If \(h\) prescribed slots are
active, their common row support has exact size

\[
 2^h\operatorname {Cat}_{m-2h}.
\tag{7.15}
\]

For the all-on state, the total adjacent-order edit mass is

\[
 \boxed{
 D_{\rm edit}=4u\operatorname {Cat}_{m-2}
 =\left(\frac{\alpha_0}{4}+o(1)\right)W.}
\tag{7.16}
\]

Moreover all but \(O_{\alpha_0}(\operatorname {Cat}_m/m)\) rows change.
This is a genuine non-row-power, root-dependent, dispersed Catalan
family.  Its \(\Theta(W)\) edit mass meets the necessary fixed-depth
scale in Theorem 6.2; it is not a sublinear-carrier repair.

Cutting the distinguished infinity coordinate from every anchored row
gives \(\operatorname {Cat}_m\) ordinary cyclic packets on \([2m]\).
For any anchored exact factor \(F\), the infinity cut has a loopless
\((m-1)\)-regular complement multigraph \(G_F\) on the row set, and every
selected row set \(S\) obeys the exact identity

\[
 \boxed{
 C_0(\{\pi_x:x\in S\})=2e_{G_F}(S).}
\tag{7.17}
\]

Indeed, the \(m+1\) nonwrapping primary owners in every row partition the
entire even middle layer.  The remaining \(m-1\) cyclic windows are the
complements of the nonport primary owners; an internal edge of \(G_F\)
creates exactly the two reciprocal duplicates.

Consequently this extensive family reduces the cyclic corrected-annulus
problem to the literal row-selection gate

\[
 |S|=K,\qquad e_{G_{F^A}}(S)=o(W),
\tag{7.18}
\]

\[
 \sum_{q=q_0}^{H}
 \left[
 N_q-\left|\bigcup_{x\in S}E_{m-q}(\pi_x^{A})\right|
 \right]=o(W).
\tag{7.19}
\]

Equations (7.18)--(7.19) are not proved.  Edit mass is only mobility:
it does not imply that one common mask and row set orient the changes
productively.  The construction is nevertheless the requested growing
Catalan/Dyck trade family at the first scale not excluded by locality.
It supplies exact factor legality, positive root density, and root-scale
action; the remaining obstruction is precisely the coloured
strong-cycle selection developed in Sections 2--4.

## 7.4 Private-primary path escape, with the support bridge isolated

There is a useful path alternative to the full infinity-cut cycles.  It
removes the complement graph exactly, although it does not yet prove the
annular provider theorem.

Write one anchored shortest row, cut at infinity, as

\[
 r_x=(\infty,a_{x,1},\ldots,a_{x,2m}),
\tag{7.20}
\]

and retain only its \(m+1\) nonwrapping middle states

\[
 P_{x,j}=\{a_{x,j},\ldots,a_{x,j+m-1}\},
 \qquad1\le j\le m+1.
\tag{7.21}
\]

Across all \(\operatorname {Cat}_m\) rows, these states partition
\(\binom{[2m]}m\).  Hence selecting arbitrary complete primary rows is
middle-collision-free.

Each primary row has two genuine radius-\(H\) rotor orientations.  With
\(I_x(s,t)\) denoting the corresponding length-\(t\) interval, their
rooted flags are

\[
 L^{\rm f}_{j,q}=I_x(j+q,m-q),\qquad
 U^{\rm f}_{j,q}=I_x(j,m+q),
\tag{7.22}
\]

\[
 L^{\rm b}_{j,q}=I_x(j,m-q),\qquad
 U^{\rm b}_{j,q}=I_x(j-q,m+q).
\tag{7.23}
\]

For \(H\le m-2\), their transition supports are disjoint at cyclic
distances at most \(H+1\), so the paths are strongly \(H\)-safe.  Put

\[
 D_i=\bigcap_{r=0}^{H}P_{x,i+r}.
\tag{7.24}
\]

Every \(D_i\) has size \(m-H>0\).  The explicit set-valued word

\[
 D_{1-H},D_{2-H},\ldots,D_{m+1+H}
\tag{7.25}
\]

has length \(m+1+2H\) and realizes all flags in (7.22), or after
reversal all flags in (7.23).  Explicitly,

\[
 D_i=I_x(i+H,m-H),
\]

and for every \(1\le j\le m+1\), \(0\le q\le H\),

\[
 \bigcup_{i=j+q-H}^{j}D_i
 =I_x(j+q,m-q)=L^{\rm f}_{j,q},
\qquad
 \bigcup_{i=j-H}^{j+q}D_i
 =I_x(j,m+q)=U^{\rm f}_{j,q}.
\tag{7.25a}
\]

Both are contiguous subwords of (7.25).  This is the hard-started
rotor-path realization, not a formal state ledger.

Put

\[
 K_{\rm path}=
 \left\lfloor\frac{N_{q_0}}{m+1}\right\rfloor,
 \qquad
 M_{\rm path}=(m+1)K_{\rm path}
 =N_{q_0}-\rho_{\rm path},
 \quad0\le\rho_{\rm path}<m+1.
\tag{7.26}
\]

Then

\[
 K_{\rm path}
 =(e^{-a^2}+o(1))\operatorname {Cat}_m,
\tag{7.27}
\]

and any selected oriented-row family has exact literal ledger

\[
 \boxed{
 L\le
 W+2HK_{\rm path}
 +\sum_{q=q_0}^{H}(h_q^-+h_q^+),}
\tag{7.28}
\]

with \(2HK_{\rm path}=O(W/\sqrt m)\) and no middle collision term.

The provider union is also classified exactly.  At lower depth \(q\),
the two orientations together expose precisely all infinity-avoiding
length-\((m-q)\) intervals present in the anchored factor: backward
starts cover \(1,\ldots,m+1\), while forward starts cover
\(q+1,\ldots,m+q+1\).  At upper depth \(q\), every
infinity-avoiding length-\((m+q)\) interval of the factor occurs in both
orientation catalogues, forward at \(j=s\) and backward at \(j=s+q\).

Orientation has only fringe-scale action.  The common lower deck of one
row has starts

\[
 q+1,q+2,\ldots,m+1
\tag{7.29}
\]

and size \(m-q+1\).  Forward orientation adds the \(q\) right-fringe
starts \(m+2,\ldots,m+q+1\), while backward orientation adds the
\(q\) left-fringe starts \(1,\ldots,q\).  The common upper deck has
starts \(1,\ldots,m-q+1\), again with \(q\) orientation-dependent
fringe starts on either side.  Therefore, for any fixed selected row set
\(\mathcal S\),

\[
 h_q^-\ge
 N_q-\left|\bigcup_{x\in\mathcal S}C_{x,q}^-\right|-qK_{\rm path},
\qquad
 h_q^+\ge
 N_q-\left|\bigcup_{x\in\mathcal S}C_{x,q}^+\right|-qK_{\rm path},
\tag{7.30}
\]

where \(C_{x,q}^{\pm}\) are the orientation-independent central decks.
At \(q=q_0\),

\[
 q_0K_{\rm path}=O_a(W/\sqrt m)=o(W).
\tag{7.31}
\]

Thus path reversal cannot manufacture the protected entrance base: a
successful atlas already needs one common row set whose two central decks
cover \(N_{q_0}-o(W)\) targets on each sign.  On the other hand the exact
two-sign \(\ell^1\) distance between the two orientations at depth \(q\)
is \(4q\) per row.  Summed through the fixed annulus and over
\(K_{\rm path}\) rows, this is \(\Theta_{a,b}(W)\).  Like the mesoscopic
two-packet switch, path orientation can only be a correlated residual
orienter after the common base exists.

This does **not** prove complete provider support for the MSW primary
paths.  The audited PBBS all-depth theorem concerns the distinct PBBS
factor, whereas the \(\operatorname {Cat}_m\) anchored shortest rows are
the MSW/lexical factor.  No theorem transfers the PBBS histograms to these
rows.  Thus completeness of (7.28) is conditional on a new restricted
MSW support theorem, or on a PBBS-to-anchored transfer.  Unconditionally,
the primary construction removes the middle complement-graph obstruction
and leaves one common coloured row/orientation selection.  It is a
hard-started path compiler, not the cyclic rethreading requested in the
main gate.

## 7.5 Run-compressed primary selection

Whole primary rows are not required for the path compiler.  In anchored
row \(x\), choose any subset \(A_x\subseteq\{1,\ldots,m+1\}\), decompose
it into \(r_x\) disjoint intervals of primary indices, and orient each
interval independently.  Put

\[
 M_*=\sum_x|A_x|,\qquad R_*=\sum_xr_x.
\tag{7.32}
\]

### Theorem 7.3 (exact run-compressed primary ledger)

For every such selection, there is a literal word covering all selected
middle owners and all flags assigned to the selected runs, of length at
most

\[
 \boxed{
 W+2HR_*+
 \sum_{q=q_0}^{H}(h_q^-+h_q^+).}
\tag{7.33}
\]

Here the \(W\) term assumes \(M_*\le W\) and appends every one of the
\(W-M_*\) unselected middle owners once.  In particular one may take
\(M_*=N_{q_0}\) exactly.  Coefficient one would follow from a provider
selection satisfying

\[
 R_*=o(W/H),\qquad
 \sum_{q=q_0}^{H}(h_q^-+h_q^+)=o(W).
\tag{7.34}
\]

#### Proof

A run of \(s\) consecutive primary states is a subpath of (7.25) and
therefore has a hard-started realization of length \(s+2H\), in either
orientation.  The primary-owner partition makes the selected middle
owners distinct across every row and run.  Concatenating the \(R_*\)
run words costs \(M_*+2HR_*\).  Append the \(W-M_*\) unselected middle
owners and then one literal repair for each signed hole.  The total is
(7.33).  \(\square\)

Since

\[
 \operatorname {Cat}_m=\Theta(W/m),\qquad
 \frac{W/H}{\operatorname {Cat}_m}
 =\Theta_{a,b}(\sqrt m),
\tag{7.35}
\]

the average allowed run count is \(o(\sqrt m)\) per Catalan row, not one
complete \(2m\)-cycle per selected packet.  This is a strictly weaker
grouping gate than cyclic rethreading and bypasses the complement graph.
It remains conditional on the missing common all-depth provider
assignment; it does not transfer PBBS support to MSW rows.

There is nevertheless a sharp clustering requirement.  If
\(M_*=(e^{-a^2}+o(1))W\) and (7.34) holds, then for every fixed
\(C>0\), the total selected owner mass lying in runs of length at most
\(CH\) is bounded by

\[
 CHR_*=o(W).
\tag{7.36}
\]

Thus all but \(o(W)\) selected primary owners must lie in runs whose
length divided by \(H\) tends beyond every fixed constant, in the
mass-weighted sense.  In particular, a bank of \(O(H)\)-length local
fragments cannot close the path gate even though arbitrary subsets of
primary owners are collision-free.  The surviving provider assignment
must be clustered into super-Gaussian row segments or essentially whole
rows.

## 8. Exact surviving gate

The corrected fixed-annulus lane has now separated into two integral
tasks.

### Gate A: coloured protected strong-cycle selection

Select (K/2+O(1)) protected two-packet components, or (K) ordinary
packets, so that

\[
 C_0=o(W),\qquad h_q^-+h_q^+=o(W)\quad
 \text{for every }q_0\le q\le H,
\tag{8.1}
\]

and

\[
 \sum_{q=q_0}^H(h_q^-+h_q^+)=O(W)
\tag{8.2}
\]

before final orientation.  It must satisfy the successor capacities
(2.4), the strong-cycle capacities (2.5), and the multidepth conclusion
of Theorem 3.1.  In a restricted Catalan catalogue it must also defeat
the frustration network of Theorem 4.1.

### Gate B: common signed reserve orientation

Orient the mesoscopic component shores so that the (O(W)) residual in
(8.2) becomes (o(W)), without creating a linear defect at any one
depth.  The exact Farkas and literal reserve inequalities in the
mesoscopic theorem remain the correct criterion.  Independent signs are
not justified.

If Gates A and B hold, the literal compiler ledger (1.6) gives

\[
 L=W+o(W).
\]

What is proved here is not either gate, but a sharp classification of the
trade scales which can possibly meet them:

* one-splice forests do not enlarge the partial-selection space;
* every sublinear contiguous one-hole carrier has (o(W)) action at one
  depth and is impossible against a linear plateau;
* width-\(\Theta(\sqrt m)\) protected two-packet circuits have the correct
  aggregate action and pair geometry, but only after a common coloured
  base already solves every depth to (o(W)); and
* every successful base contains a positive-density bank of successor
  edges carrying \(\Theta(\sqrt m)\) simultaneous triple-rainbow colours.

Thus the remaining positive object cannot be a local correction of a
diffuse factor.  It must be a root-scale or genuinely dispersed
multi-hole Catalan/Dyck strong-cycle design selected jointly across all
Gaussian depths.

## 9. Audited claims, corrections, and unproved lemmas

Proved in this note:

1. The sidewise owner-simple successor cut (2.2)--(2.4), with the
   explicit factor-two extraction for a physical vertex matching.
2. The triple-rainbow linear-forest cut (2.5).
3. The positive-density multidepth strong-edge theorem (3.4)--(3.5),
   with exact constants.
4. The SCD endpoint-antipode law (3.11)--(3.12).
5. The degree-two frustration bound (4.3) and odd-cycle consequence
   (4.4).
6. The forest-fusion coarsening theorem (5.1).
7. The contiguous-carrier fixed-depth action bound (6.2)--(6.4).
8. The two-deck distance-one count and improved relative codegree
   (7.7)--(7.8), plus the entrance-conditioned \(O(m^{-2})\) overlap
   moment.
9. The private-primary owner partition, explicit \(m+1+2H\) path word,
   path compiler ledger (7.28), and orientation-fringe bound (7.30).
10. The run-compressed ledger (7.33) and its super-Gaussian mass
   clustering consequence (7.36).

Used as audited input from the cited mesoscopic theorem:

1. the exact two-shore physical packets (7.1);
2. protected middle and entrance identities (7.2);
3. the triangular literal direction (7.3);
4. the within-component protected collision bound; and
5. the complete-orbit fractional loads.

Used as audited input from the extensive reciprocal-\(C_8\) theorem:

1. the \(2^u\) literal anchored exact-factor cube;
2. the exact support census \(2^h\operatorname {Cat}_{m-2h}\);
3. the edit mass \(4u\operatorname {Cat}_{m-2}\);
4. the infinity-cut complement graph and collision identity (7.17); and
5. the fact that all but \(O(\operatorname {Cat}_m/m)\) rows change in
   the all-on state.

Corrections to earlier Lane R conclusions:

1. The corrected target requires (K=\Theta(W/m)) ordinary components,
   and their Gaussian collars are already (o(W)); no
   (omega(m))-long component theorem is required.
2. The (1100R\leftrightarrow1010R) one-splice bank is a legal
   rethreading, but it cannot improve an arc-local partial selection.
3. In SCD terminology the protected top class is
   (mathcal D_{\ge H}), of size (N_H), not the exact-tag-(H) class.
4. No claim that clipped BTK has an empty top-tag rotor graph is used.

Unproved:

1. a protected-deck matching meeting (8.1)--(8.2);
2. a common signed orientation reducing its aggregate residual to
   (o(W));
3. a linear odd-cycle packing in the degree-two graph of any concrete
   PBBS/MSW Catalan catalogue; or
4. complete annular provider support for the MSW private-primary path
   atlas, or a transfer of PBBS all-depth support to anchored shortest
   rows; or
5. coefficient one for the fixed annulus or for the full contiguous-OR
   width theorem.

The decisive boundary is therefore exact: scalar Catalan supply passes,
bounded and sublinear-carrier repair cannot cure a linear plateau, an
extensive root-scale Catalan factor and a mesoscopic protected circuit
both exist, and the sole remaining construction is a correlated coloured
strong-cycle selection with root-scale multidepth coherence.
