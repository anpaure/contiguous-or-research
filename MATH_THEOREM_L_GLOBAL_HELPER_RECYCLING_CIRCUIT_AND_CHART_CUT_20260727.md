# Global helper recycling: a literal tetrahedral circuit and the fixed-chart cut

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\tag{0.1}
\]

and assume \(H\ge3\), \(M\ge8H+1\). This note compares the four-top
left-shift recharge from
MATH_THEOREM_L_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_LOCAL_REUSE_20260727.md
with the squarefree three-top recharge from
MATH_THEOREM_THREE_TOP_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_RECHARGE_20260727.md.

There are four exact conclusions.

### Theorem A (helpers can recycle in a literal closed circuit)

Fix one \((M-2)\)-core \(C\), four outside labels \(x,y,a,b\), and the
two positional bases \(\omega,\eta\) of the three-top theorem. On the
six tops

\[
 C+xy,\ C+ab,\ C+xa,\ C+ya,\ C+xb,\ C+yb
\tag{0.2}
\]

there is a four-packet chronology

\[
 (xya)^+,\qquad (xyb)^-,\qquad (abx)^+,\qquad (aby)^-
\tag{0.3}
\]

in which every packet is a literal three-top recharge, outputs of the
earlier packets are exact sources for later packets, and all six top
words return to their initial states. Every protected trace is
preserved after every packet.

Thus the companion paths of the three-top theorem are not intrinsically
one-use resources. A genuine closed helper-recycling network exists.
The six-top union is not asserted to be globally owner-squarefree;
squarefreeness is certified packetwise, as in the three-top theorem.

### Theorem B (fixed-chart global cut)

For a fixed core and rooted two-base chart, write
\(\epsilon_{uv}\in\mathbb F_2\) for the orientation of the two
placeholder labels on top \(C+\{u,v\}\). A three-top recharge on
\(\{u,v,w\}\) adds the three-edge vector of that triangle. Hence, for
every outside label \(u\),

\[
 \boxed{\chi_u=\sum_{v\ne u}\epsilon_{uv}\pmod2}
\tag{0.4}
\]

is invariant. These are the complete linear invariants: the recharge
image is the cycle space of the complete graph on the outside labels.

In particular, each fixed rooted chart on one top has only two physical
states. No closed network confined to a bounded number of charts per top
can produce \(\Theta(m)\) independent rectangle directions per top,
regardless of how often its helpers are recycled.

### Theorem C (global position-three token conservation)

The fixed-chart parity is not the only useful ledger. Across arbitrary
cores and arbitrary instances of the three-top theorem, define

\[
 P_\lambda=
 \#\{U:\text{the rooted word selected on \(U\) has label
 \(\lambda\) in position \(3\)}\}.
\tag{0.5}
\]

Every three-top recharge preserves the complete integer vector

\[
                         \boxed{(P_\lambda)_{\lambda\in[2m]}.}
\tag{0.6}
\]

The two-top boundary rectangle also preserves it, because it swaps only
positions one and two. Therefore (0.6) is a global invariant of every
network built solely from the three-top recharges and the collar-neutral
rectangles, even when the common core changes between packets.

The invariant says that recharge packets route position-three label
tokens; they never create or destroy them. It does not by itself forbid
a Latin-type circulation in which every token visits many tops.

### Theorem D (necessary chart breadth)

If a top supports \(r_U\) linearly independent boundary-rectangle
directions along a helper-recycled chronology, then it must visit at
least

\[
                         \boxed{\left\lceil r_U/2\right\rceil}
\tag{0.7}
\]

distinct rooted placeholder charts. Consequently average
\(\Theta(m)\) direction rank on \(N\) tops requires
\(\Omega(mN)=\Omega(W)\) top-chart incidences.

The four-face circuit proves that helper recycling is possible, but
Theorems B--D prove that recycling inside one fixed-core atlas cannot
amplify the direction rank. A successful global construction must
simultaneously:

1. recycle helpers;
2. transport the position-three tokens subject to (0.6); and
3. move through \(\Theta(m)\) distinct rooted charts on a typical top.

No such global chart-changing factor is constructed here. Conversely,
there is no all-core no-go: the four-top shift recharge changes the
position-three census and therefore lies outside invariant (0.6).

## 1. The three-top packet as a triangle flip

Fix \(C\), \(|C|=M-2\), and let

\[
                         Q=[2m]\setminus C,
 \qquad |Q|=m-H+2.
\tag{1.1}
\]

For \(u,v\in Q\), write

\[
                         U_{uv}=C\cup\{u,v\}.
\tag{1.2}
\]

The two positional states on \(U_{uv}\) interchange the occupants of
the two placeholder slots. Relative to an arbitrary canonical
orientation of the unordered pair \(\{u,v\}\), denote them by
\(\epsilon_{uv}=0,1\).

For distinct \(u,v,w\), the three-top theorem replaces the three plus
states on

\[
                         U_{uv},\quad U_{uw},\quad U_{wv}
\tag{1.3}
\]

by their minus states. At the orientation level it acts as

\[
 (\epsilon_{uv},\epsilon_{uw},\epsilon_{wv})
 \longmapsto
 (\epsilon_{uv}+1,\epsilon_{uw}+1,\epsilon_{wv}+1).
\tag{1.4}
\]

The inverse packet has the same mod-two action. Equation (1.4) forgets
the \(\omega/\eta\) source-type requirement; Section 2 supplies one
nontrivial circuit in which those literal types and all intermediate
orientations match exactly.

The rooted phase cuts in the three-top theorem put one placeholder in
position three. For a forward packet with labels \(u,w,v\), the
position-three labels on the three source words are

\[
                         (u,w,v),
\tag{1.5}
\]

while on the three target words they are

\[
                         (v,u,w).
\tag{1.6}
\]

Thus the packet performs a three-cycle of position-three tokens.

## 2. A literal four-face helper-recycling circuit

Partition the four outside labels into two ordered pairs

\[
                         X=(x,y),\qquad A=(a,b).
\tag{2.1}
\]

Use the \(\omega\) base on the two within-pair tops \(U_{xy},U_{ab}\)
and the \(\eta\) base on the four cross tops.

For a cross top \(U_{zc}\), with \(z\in\{x,y\}\) and
\(c\in\{a,b\}\), declare bit zero to mean the state
\(\eta^+(z,c)\); bit one is its minus state. On \(U_{xy}\) and
\(U_{ab}\), bit zero is the displayed-order \(\omega^+\) state and bit
one its minus state.

Install the initial orientation vector

\[
 \begin{array}{c|cccccc}
 \text{top}&xy&ab&xa&ya&xb&yb\\ \hline
 \epsilon&0&0&0&1&1&0.
 \end{array}
\tag{2.2}
\]

### Theorem 2.1 (tetrahedral four-packet circuit)

The following four packets are successively applicable:

\[
 \begin{array}{c|c|c}
 \text{step}&\text{packet direction}&\text{three source bits}\\ \hline
 1&(x,y,a)\text{ forward}&(xy,xa,ya)=(0,0,1),\\
 2&(x,y,b)\text{ inverse}&(xy,xb,yb)=(1,1,0),\\
 3&(a,b,x)\text{ forward}&(ab,xa,xb)=(0,1,0),\\
 4&(a,b,y)\text{ inverse}&(ab,ya,yb)=(1,0,1).
 \end{array}
\tag{2.3}
\]

After Step 4 every bit in (2.2), and hence every one of the six literal
top words, is restored.

#### Proof

Step 1 flips \(xy,xa,ya\), giving

\[
                         xy=1,\quad xa=1,\quad ya=0.
\tag{2.4}
\]

The untouched values \(xb=1,yb=0\) make the inverse \(xyb\) source
available. Step 2 flips those three bits and leaves

\[
                         xy=0,\quad xb=0,\quad yb=1.
\tag{2.5}
\]

Now \(ab=0,xa=1,xb=0\), which is exactly the forward \(abx\) source.
Step 3 gives

\[
                         ab=1,\quad xa=0,\quad xb=1.
\tag{2.6}
\]

Finally \(ab=1,ya=0,yb=1\) is the inverse \(aby\) source. Step 4
restores

\[
                         ab=0,\quad ya=1,\quad yb=0.
\tag{2.7}
\]

Together with (2.5)--(2.6), this is exactly (2.2).

It remains to audit the base types. Every face in (2.3) has one
within-pair edge, carrying the \(\omega\) word, and two cross edges,
carrying the \(\eta\) words. The source bits in the table are precisely
the plus shore for a forward packet and the minus shore for an inverse
packet. Thus each step is the literal three-top theorem, not merely its
orientation projection.

Every packet has zero aggregate derivative at every protected length.
Therefore the chronology preserves all protected traces after every
step. Since the endpoint bit and base on each top are restored, all six
literal words are restored. \(\square\)

The circuit is nontrivial: Steps 2--4 use states produced earlier.
It is the smallest natural closed helper-recycling network on the four
faces of a Johnson tetrahedron. Its endpoint trace is zero because it
is a circuit; its purpose is to prove reusable source compatibility,
not middle displacement.

## 3. The complete fixed-chart cut invariant

Let \(E(K_Q)\) be the set of tops \(U_{uv}\). Regard an orientation
state as

\[
                         \epsilon\in\mathbb F_2^{E(K_Q)}.
\tag{3.1}
\]

For \(u\in Q\), define

\[
                         \chi_u(\epsilon)
 =\sum_{v\in Q\setminus\{u\}}\epsilon_{uv}\pmod2.
\tag{3.2}
\]

### Theorem 3.1 (triangle image equals the cycle space)

Every fixed-chart three-top recharge preserves every \(\chi_u\).
Moreover two orientation states are connected by a formal sum of
triangle recharges if and only if their difference has even degree at
every vertex:

\[
 \epsilon'-\epsilon\in
 \ker\!\left(
 \mathbb F_2^{E(K_Q)}
 \longrightarrow\mathbb F_2^Q
 \right).
\tag{3.3}
\]

#### Proof

A triangle has degree two at each of its three vertices and degree zero
elsewhere, so its incidence vector lies in the kernel in (3.3). This
proves invariance.

Conversely, an even graph is a disjoint mod-two sum of cycles. In a
complete graph, every cycle

\[
                         v_1v_2\cdots v_kv_1
\tag{3.4}
\]

is the mod-two sum of the triangles

\[
                         v_1v_iv_{i+1},
 \qquad2\le i\le k-1.
\tag{3.5}
\]

Thus triangle vectors span the complete cycle space. \(\square\)

The \(|Q|\) characters in (3.2) have one dependency, their total sum
being zero. They give the expected codimension \(|Q|-1\).

Theorem 3.1 is an orientation-flow theorem. Literal chronological
applicability additionally requires the \(\omega/\eta\) source types.
Theorem 2.1 shows that the cut is not merely formal: it supports a
nontrivial literal circuit.

## 4. Integer position-three token conservation

The fixed-chart parity disappears when a top is reinterpreted with a
different core or arm system. A simpler integer invariant survives all
such reinterpretations as long as every recharge is an instance of the
three-top theorem.

### Theorem 4.1 (global token census)

For any literal table, define \(P_\lambda\) by (0.5). Every three-top
recharge preserves \(P_\lambda\) for every ground label \(\lambda\).
Every two-top boundary rectangle preserves the same vector.

#### Proof

For one three-top packet, equations (1.5)--(1.6) show that the multiset
of position-three labels is \(\{u,v,w\}\) on both shores. All untouched
tops make identical contributions. Hence every \(P_\lambda\) is
unchanged.

A boundary rectangle interchanges the first two letters on each of its
two tops and fixes the third letter. It therefore preserves
\((P_\lambda)\) top by top. Composition proves the theorem. \(\square\)

### Corollary 4.2 (every closed network is a token circulation)

In any helper-recycled network made from these two move types, the
position-three labels follow disjoint directed token trajectories. A
closed network permutes the tokens among tops but has the same number
of tokens of every label at every time slice.

This is an integer conservation law, not only a parity character. It
does not forbid one token from visiting many tops or one top from
receiving many different tokens over time.

## 5. Direction rank per rooted chart

Fix a top \(U=C+\{u,v\}\), a rooted phase cut, a core order, and the
two placeholder slots. Call this data one **rooted chart**. Recharges
using this chart can only interchange \(u,v\). Thus the physical option
set in the chart is

\[
                         \{p,\tau p\},\qquad \tau=(u\ v).
\tag{5.1}
\]

At these two options, the first-two boundary swap supplies at most two
middle unit directions.

### Theorem 5.1 (chart-breadth lower bound)

Suppose a chronology exposes \(r_U\) linearly independent focal
boundary-swap directions on one top \(U\), and suppose its recharges
visit \(q_U\) distinct rooted charts on \(U\). Then

\[
                         r_U\le2q_U.
\tag{5.2}
\]

#### Proof

Partition the advertised directions by the chart in which their source
option occurs. A fixed chart has only the two options in (5.1), hence
at most two boundary-swap directions. The span of the union of
\(q_U\) sets, each of size at most two, has rank at most \(2q_U\).
\(\square\)

### Corollary 5.2 (global incidence requirement)

If a family of \(N\) tops has average independent direction rank at
least \(r\), then

\[
                         \sum_Uq_U\ge {rN\over2}.
\tag{5.3}
\]

At \(r=\Theta(m)\) and \(N=(1+o(1))W/m\), this is

\[
                         \sum_Uq_U=\Omega(mN)=\Omega(W).
\tag{5.4}
\]

Thus a bounded collection of fixed-core tetrahedral circuits cannot
meet the dense-recycling scale. The network must change rooted charts
on a linear proportion of its visits.

Equation (5.4) is a necessary incidence count, not a word-length lower
bound. A successful factor could in principle reuse the same physical
top through \(\Theta(m)\) charts without paying a new top.

## 6. Comparison with the four-top shift recharge

The three-top theorem is stronger than the four-top shift in two ways:

1. it uses only three tops; and
2. both middle shores are squarefree with exactly the same owner set.

The four-top shift has a different advantage: it is universal for an
arbitrary current focal word and changes the rooted position-three
census.

In the four-top construction, the alternating filler blocks are

\[
                         F_0=F_2=A,\qquad F_1=F_3=B.
\tag{6.1}
\]

Before left rotation, the four position-three labels consist of two
copies of the second label of \(A\) and two copies of the second label
of \(B\). After rotation they consist of two copies of the third label
of \(A\) and two copies of the third label of \(B\). Since these labels
are distinct,

\[
                         (P_\lambda)_{\rm after}
 \ne
                         (P_\lambda)_{\rm before}.
\tag{6.2}
\]

Thus the four-top shift is not generated by any network of the
three-top recharges and boundary rectangles. It crosses the global cut
(0.6).

This comparison explains the current frontier:

- the three-top packet has exact squarefree helper recycling but is
  constrained to route a conserved position-three token population;
- the four-top packet crosses that token cut but currently consumes
  fresh helper states in the proved linear local schedule.

## 7. Consequence for the average-reuse gate

Theorem 2.1 positively answers the first helper question:

\[
 \boxed{\text{outputs of recharge packets can be exact later sources.}}
\tag{7.1}
\]

However, the closed circuit stays inside one chart on each top and
therefore has only \(O(1)\) boundary-direction rank per top. Repeating
it cannot accumulate new independent directions.

Theorems 4.1 and 5.1 identify the two simultaneous requirements on a
global \(\Theta(m)\)-reuse construction:

1. a token-routing schedule preserving the global integer census
   \((P_\lambda)\); and
2. a chart-routing schedule visiting \(\Theta(m)\) distinct rooted
   charts on a typical top.

The local three-top theorem supplies both operations separately: its
packet routes three tokens, and changing the remote placeholder on a
focal top changes its chart. What is not supplied is a single
coefficient-one factor of packets satisfying both global schedules.

Accordingly the present result is a **global fixed-chart obstruction**,
not an all-core impossibility theorem. It rules out every proposal which
recycles helpers inside only \(O(1)\) core/port charts per top. A
successful construction must use the full \(\Omega(W)\) chart-incidence
scale in (5.4).

## 8. Independent audit

Three checks are decisive.

### 8.1 Literal source compatibility in the circuit

The source triples in (2.3) alternate plus and minus exactly. Every
shared top has the orientation output by its previous use. The within
edges always carry \(\omega\), and the cross edges always carry
\(\eta\). Hence no face silently changes its positional base.

### 8.2 Completeness of the cut

The triangle incidence vectors generate all even graphs by the explicit
triangulation (3.5). Thus (0.4) is not merely a family of invariants; it
is the complete mod-two quotient of the fixed-chart orientation system.

### 8.3 Token signs

On the plus shore, the position-three tokens are \(u,w,v\); on the
minus shore they are \(v,u,w\). Each label occurs once on both shores.
Therefore (0.6) is exact over \(\mathbb Z\), independent of orientation,
core choice, or packet direction.

## 9. Exact boundary

Proved:

1. a nontrivial four-packet literal circuit which restores all six top
   words and reuses earlier helper outputs as later sources;
2. the complete fixed-chart cut quotient;
3. global integer conservation of position-three label tokens for the
   three-top-plus-rectangle move library;
4. a rank bound of two boundary directions per rooted chart;
5. the necessary \(\Omega(W)\) chart-incidence scale for
   \(\Theta(m)\) average direction rank; and
6. separation of the four-top shift from the three-top move library by
   the token census.

Not proved:

1. a global factor routing the conserved tokens through
   \(\Theta(m)\) charts per top;
2. a larger closed circuit which changes charts rather than merely
   orientations;
3. a globally squarefree owner realization even for the six-top
   circuit, or an \(o(W)\)-repeat resolution for a larger one;
4. a theorem that the master-order low-collision target violates the
   position-three census; or
5. coefficient one.

The helper-recycling question is therefore partly closed. Recycling
itself is possible and has an exact six-top circuit. The remaining
problem is chart-changing circulation at linear average depth, subject
to the global token cut.
