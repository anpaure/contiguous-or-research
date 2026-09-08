# Ordered-diamond cover-down: packet Hall, q1 opening flow, and the octagon cut

Date: 2026-08-01
Status: exact conditional cover-down theorem and exact finite obstructions;
no unconditional all-parameter packing claim

## 0. Outcome

There is a clean combinatorial interface for upgrading an ordered
four-resource matching of size `N-o(N)` to one of size `N-O(1)`.

1. Pair the unmatched lower and upper colours in a compatibility graph.
   The number of pairs which must be left unresolved is exactly its Hall
   deficiency.
2. For each chosen residual pair, regard every complete alternating
   absorber as one bounded **packet footprint**.  Aharoni--Haxell's
   hypergraph Hall condition on these footprints packs one packet for every
   chosen pair.  A simple degree condition and a stronger elementary
   deletion-resilience condition are recorded below.
3. Carry the q1 data as an occurrence-labelled rainbow-factor/opening
   sidecar.  After a factor frame with source-private seam slots is fixed,
   recycling interior cut colours is an ordinary bipartite max-flow.  Its
   exact deficit is

   \[
     \max_{S\subseteq Q_{\rm int}}(|S|-|N(S)|).
   \]

   A robust Hall surplus survives a prescribed number of packet-induced
   seam deletions.

These three conditions are sufficient, and none is implied merely by the
four marginal resource counts.  The eight-atom Johnson octagon is an exact
finite cut: one parity is valid on lower--tail--head and the other is valid
on upper--tail--head, but no parity is valid on all four shores.  Its local
rank is three although the natural half-vector has mass four.  Independently,
two explicit paths in `J(5,3)` have the same four endpoint counts and the
same zero top deficiency, but only one has the required inverse opening to a
q1-rainbow factor.  Thus the q1 sidecar cannot be replaced by those counts.

The result below is a verification target, not a proof that the Boolean
catalogue satisfies it.  In particular, the currently proved alternating
inclusion absorbers have `O(m)` resource footprint, and no required packet
Hall inequality is presently known for an arbitrary nibble leave.

## 1. Four-resource alternating packets

Let

\[
 \mathscr R=\mathcal L\sqcup\mathcal U\sqcup
             \mathcal T\sqcup\mathcal H
\]

be four typed resource shores.  An ordered atom `e` has resources

\[
 r(e)=(\lambda(e),\upsilon(e),\tau(e),\eta(e))\in\mathscr R.
\]

For Boolean diamonds these are the lower colour, upper colour, tail port,
and head port.  A four-resource matching is a set of atoms with no repeated
typed resource.

Fix such a matching `M`.  Let `L_0` and `U_0` be its unmatched lower and
upper colours.  They have the same size

\[
                         |L_0|=|U_0|=s.
\tag{1.1}
\]

### Definition 1.1 (an `M`-alternating packet)

For `(L,U) in L_0 times U_0`, an augmenting packet is a pair

\[
                         A=(A^-,A^+)
\tag{1.2}
\]

with the following properties.

1. `A^-` is a submatching of `M`, `A^+` is a four-resource matching, and

   \[
                       |A^+|=|A^-|+1.
   \tag{1.3}
   \]

2. On the two outer shores its incidence difference is exactly the target:

   \[
   V_{\mathcal L}(A^+)=V_{\mathcal L}(A^-)\sqcup\{L\},\qquad
   V_{\mathcal U}(A^+)=V_{\mathcal U}(A^-)\sqcup\{U\}.
   \tag{1.4}
   \]

3. `A^+` is disjoint in every typed resource from `M minus A^-`.

Its protected footprint is

\[
       R(A)=\bigcup_{e\in A^-\cup A^+}
       \{\lambda(e),\upsilon(e),\tau(e),\eta(e)\}.
\tag{1.5}
\]

The packet has rank at most `b` when `|R(A)|<=b`.  Extra physical guards,
factor-edge occurrences, or opening sockets are included as additional
typed footprint vertices whenever disjointness of those objects is needed.

The replacement

\[
                         M\longmapsto (M-A^-)\cup A^+
\tag{1.6}
\]

is then a four-resource matching of size `|M|+1` covering `L` and `U`.
The alternating inclusion paths proved in
`MATH_THEOREM_CATALAN_CRITICAL_RESERVE_ABSORBER_AND_BTK_TAIL_GATE_20260731.md`
and
`MATH_THEOREM_CATALAN_INDEPENDENT_BOUNDARY_ABSORBER_20260731.md`
are concrete packet templates once their off states occur in `M`.

In fact (1.4) makes the deletion exact.  Every atom of `A^-` has a lower
resource used by `A^+`, while item 3 excludes every other old conflict.
Hence

\[
                         N_M(A^+)=A^-.
\tag{1.6a}
\]

So a packet is a gain-one exchange, not a replacement with redundant
deletions.

Two packets with disjoint protected footprints commute.  Indeed neither
positive state can use a resource in either negative state or positive
state of the other, so all removals and insertions in (1.6) may be made
simultaneously.

If physical acyclicity is required, one may impose the following sufficient
condition on the complete candidate catalogue.  There is one potential
`phi` on physical middle vertices such that

\[
                  \phi(\tau(e))<\phi(\eta(e))
\tag{1.7}
\]

for every retained atom and every possible positive packet atom.  Then no
simultaneous selection can create a directed cycle.  Without (1.7), the
contracted attachment graph needs a separate graphic-matroid cut; four
resource disjointness alone does not prove acyclicity.

### Proposition 1.2 (exact unrestricted exchange normal form)

For any outside matching `S`, put

\[
 N_M(S)=\{e\in M:e\text{ shares a typed resource with some }f\in S\}
\tag{1.8}
\]

and

\[
                         M\star S=(M-N_M(S))\cup S.
\tag{1.9}
\]

Then `M star S` is a matching and its gain is exactly

\[
                         g_M(S)=|S|-|N_M(S)|.
\tag{1.10}
\]

Moreover, the maximum order of any host matching is

\[
                         |M|+\max_S g_M(S),
\tag{1.11}
\]

where the maximum is over outside matchings `S`.  If a protected bank
`Z subseteq M` must survive, restrict to `N_M(S) cap Z=empty`.

If the physical projection of `M` together with a fixed scaffold is a
forest, the toggle remains a forest exactly when the projected edges of
`S` are loopless and graphic-independent after contracting the components
of the retained forest `M-N_M(S)` and the scaffold.

#### Proof

The definition of `N_M(S)` makes (1.9) a matching and gives (1.10).  For
the reverse bound, let `T` be any matching and take `S=T-M`.  Every member
of `N_M(S)` is absent from `T`, so

\[
 |T|\le |M|-|N_M(S)|+|S|.
\]

Taking maxima proves (1.11), with the same argument under protection.
Adding edges to a forest creates no cycle exactly when their images are
independent in the graphic matroid after its components are contracted.
`square`

Closed four-resource alternating circuits are the zero-gain instances
whose two phases have the same typed incidence.  Definition 1.1 is a
factorized gain-one instance.  Proposition 1.2 is exact but not by itself a
packing theorem: a profitable `S` may be one branching exchange rather than
a disjoint union of bounded packets.

## 2. The two Hall gates

For `(L,U) in L_0 times U_0`, let `mathcal A_(L,U)` be the family of
available `M`-alternating packets.  Form the outer compatibility graph `B`
with shores `L_0,U_0` and

\[
                 LU\in E(B)\quad\Longleftrightarrow\quad
                 \mathcal A_{L,U}\ne\varnothing.
\tag{2.1}
\]

### Proposition 2.1 (exact outer-pair flow)

Put

\[
       \delta_{\rm out}(B)=
       \max_{S\subseteq L_0}\bigl(|S|-|N_B(S)|\bigr).
\tag{2.2}
\]

Then `B` has a matching of size exactly `s-delta_out(B)`.  In particular,
all but `C_0` outer colours can be paired if and only if

\[
                         \delta_{\rm out}(B)\le C_0.
\tag{2.3}
\]

#### Proof

This is the deficiency form of Hall's theorem, equivalently the min-cut
formula in the unit-capacity network

```text
source -> L_0 -> U_0 -> sink.
```

For a cut determined by `S subseteq L_0`, the lost flow relative to `s` is
`|S|-|N_B(S)|`; maximizing gives (2.2). `square`

Fix a matching `P` in `B`, and regard each edge `p=(L,U) in P` as one
target.  Let

\[
            \mathcal F_p=\{R(A):A\in\mathcal A_{L,U}\}
\tag{2.4}
\]

be its footprint hypergraph.  Repeated identical footprints may be retained
as occurrence-labelled copies, or merged if the corresponding packets are
interchangeable.

### Theorem 2.2 (packet-Hall cover-down)

Assume every footprint in (2.4) has size at most `b`, and for every
nonempty `I subseteq P`,

\[
 \boxed{
   \nu\!\left(\bigcup_{p\in I}\mathcal F_p\right)
                         > (2b-3)(|I|-1).}
\tag{2.5}
\]

Then one may choose packets `A_p in mathcal A_p` for all `p in P` with
pairwise disjoint protected footprints.  Simultaneously toggling them gives
a four-resource matching of size

\[
                              |M|+|P|.
\tag{2.6}
\]

If (1.7) holds, the resulting physical support is acyclic.  If each packet
is transparent for one fixed occurrence-labelled q1 factor/opening sidecar,
the same sidecar survives all toggles.

Consequently, if `|M|=N-s`, (2.3) and (2.5) give a matching of size at least

\[
                              N-C_0.
\tag{2.7}
\]

#### Proof

Condition (2.5) is the Aharoni--Haxell rainbow-matching condition for
hypergraphs of rank at most `b`; the coefficient is `2b-3`, not `b` (the
two agree only in rank three).  It supplies disjoint footprints, one from
each family (2.4).  Choose their associated packets.  Definition 1.1 and
footprint disjointness show that all toggles commute and each adds one atom,
which proves (2.6).  The potential (1.7) excludes directed cycles.
Occurrence-labelled sidecar transparency also composes on disjoint
supports.  Finally Proposition 2.1 gives `|P|>=s-C_0`, proving (2.7).
`square`

Condition (2.5) is deliberately stronger than four separate marginal Hall
conditions.  It measures a matching number in the **joint packet footprint**.

There are two elementary sufficient forms.

### Corollary 2.3 (degree certificate)

Suppose every target family has at least `delta` distinct footprints, one
footprint occurs in at most `mu` target families, and the union footprint
hypergraph has maximum resource degree `Delta`.  Then (2.5) follows from

\[
              \boxed{\delta\ge
                 (2b-3)\mu\,(b\Delta-b+1).}
\tag{2.8}
\]

#### Proof

For `|I|=t`, the union in (2.5) has at least `delta t/mu` distinct edges.
A greedy matching loses at most

\[
                         1+b(\Delta-1)=b\Delta-b+1
\]

edges at each choice.  Its matching number is therefore at least

\[
             {\delta t\over\mu(b\Delta-b+1)}
                  \ge(2b-3)t>(2b-3)(t-1),
\]

which is (2.5). `square`

### Lemma 2.4 (elementary deletion-resilient packing)

Let `t=|P|`.  Suppose that for every target `p`, and every typed resource
set `Z` of size at most `b(t-1)`, some packet in `mathcal A_p` has footprint
disjoint from `Z`.  Then the packets can be chosen pairwise footprint-
disjoint.

#### Proof

Order the targets arbitrarily.  After at most `t-1` choices, the union of
the chosen footprints has size at most `b(t-1)`.  The hypothesis supplies a
packet for the next target avoiding that union.  Greedy induction finishes.
`square`

This condition is stronger than (2.5), but it is often the most direct
meaning of a robust absorber bank.  It also makes the quantitative gap
plain: a local packet for every pair is not enough; each pair needs a packet
after all resources used by the other residual repairs have been deleted.

## 3. The q1 rainbow-factor/opening sidecar is a second flow

Let `F` be a q1-rainbow factor, with components put in an order.  Cut one
edge in every component, with distinct q1 colours

\[
                         q_1,\ldots,q_c.
\tag{3.1}
\]

The two outer cuts `q_1,q_c` lie in their respective global endpoints.
Put

\[
                         Q_{\rm int}=\{q_2,\ldots,q_{c-1}\}.
\tag{3.2}
\]

Fix a bank `G` of pairwise physically compatible seam slots.  Every slot
has at least one legal baseline alternative, and may have several
preverified alternatives.  Choices at distinct slots are assumed mutually
independent; after the flow choices are made, every unassigned slot is
filled by a baseline alternative.  Join `q in Q_int` to `g in G` when slot
`g` has an alternative of lower colour `q`.  Any tail/head or guard needed
to guarantee the asserted compatibility is part of the slot footprint.
Call the resulting bipartite graph `Sigma`.

### Theorem 3.1 (exact opening-sidecar min-cut)

The minimum possible number of unrecycled interior cut colours is

\[
\begin{aligned}
 h_{\rm int}
  &=|Q_{\rm int}|-\nu(\Sigma)\\
  &=\max_{S\subseteq Q_{\rm int}}
                   \bigl(|S|-|N_\Sigma(S)|\bigr).
\end{aligned}
\tag{3.3}
\]

For every realized matching of seam alternatives, the exact cut/seam
palette ledger gives

\[
       \mathcal H_1(T)={q_1,\ldots,q_c\}
          \setminus\operatorname{supp}\{\hbox{selected seam colours}\}.
\tag{3.4}
\]

Hence, whenever the endpoint bank size `d` satisfies `d>=h_int+2`, the
opened path has

\[
                         \delta_{\rm top}(T)\le h_{\rm int}.
\tag{3.5}
\]

#### Proof

A matching of `Sigma` assigns distinct seam slots to distinct interior cut
colours and realizes exactly those recycled colours.  Thus the maximum
number recycled is `nu(Sigma)`.  The second equality in (3.3) is the
deficiency form of Hall's theorem.  Equation (3.4) is the exact
rainbow-factor cut/seam ledger.  The two outer unrecycled cuts cost no
frozen top deficiency because each is contained in its corresponding global
endpoint; substituting the `h_int` interior holes in the frozen boundary
formula gives (3.5). `square`

The flow network is simply

```text
source -> interior cut colours -> seam slots -> sink,
```

with unit capacities.  It is occurrence-labelled: two slots realizing the
same set colour remain different physical choices.

### Corollary 3.2 (robust sidecar Hall surplus)

Suppose the packet selection may destroy at most `rho` seam slots.  If,
before those deletions,

\[
             |N_\Sigma(S)|\ge |S|+\rho-C
             \qquad(S\subseteq Q_{\rm int}),
\tag{3.6}
\]

then after any such deletion the remaining sidecar has

\[
                         h_{\rm int}\le C,
                         \qquad\delta_{\rm top}\le C
\tag{3.7}
\]

for `d>=C+2`.

#### Proof

Deleting `rho` right vertices decreases every neighbourhood by at most
`rho`, so the surviving graph satisfies

\[
                         |N(S)|\ge|S|-C.
\]

Apply (3.3) and (3.5). `square`

For fully sidecar-transparent packets one takes `rho=0`.  Alternatively,
(3.6) is a precise way to budget a controlled amount of packet interference.
If the sidecar is a q1-rainbow Hamilton cycle, opening one edge is already
the exact B1 state; this is the special one-component reset and requires no
interior flow.

There is a strictly more general exact form.  Expand every labelled seam
alternative to a provider atom and suppose the simultaneously usable
provider sets are the independent sets of a matroid `M_q`.  Rado's theorem
then replaces (3.3) by

\[
 \boxed{
 h_{\rm int}=\max_{S\subseteq Q_{\rm int}}
       \bigl(|S|-r_{M_q}(N(S))\bigr).}
\tag{3.8a}
\]

The private-slot flow above is the partition-matroid special case.  This
qualification is load-bearing.  Crossing slot and resource capacities need
not form a matroid: the three alternatives with `(slot,resource)` pairs

```text
(s1,r1), (s1,r2), (s2,r1)
```

already violate the exchange axiom.  In that case neither the ordinary
flow nor (3.8a) is sound until the crossing conflicts are absorbed into the
joint packet footprint or another valid compatibility system is proved.

Combining Theorem 2.2 with Corollary 3.2 gives the promised sufficient
cover-down certificate:

\[
\boxed{
 \begin{array}{c}
 \delta_{\rm out}\le C_0,\\
 \text{packet matching-number Hall (2.5)},\\
 \text{q1 seam Hall surplus (3.6)},\\
 \text{one common physical potential, or a separate graphic certificate}
 \end{array}}
 \Longrightarrow
 \boxed{
 \begin{array}{c}
 \text{four-resource matching size }N-C_0,\\
 \delta_{\rm top}\le C.
 \end{array}}
\tag{3.8}
\]

All constants in (3.8) are terminal charges.  The statement makes no claim
that the Boolean near-factor supplied by the nibble is automatically
correlated with such a packet bank.

### 3A. Complete-host q1 circuits versus protected-host flow

The sidecar flow is the exact restricted-host statement when opened factor
interiors are frozen and only certified seam providers may change.  On the
complete Middle Levels incidence host there is a stronger owner/q1 fact.

Let `F` be a q1-rainbow spanning two-factor and let `e` be one protected
edge.  Lift `F` to its incidence two-factor.  A Middle Levels Hamilton cycle
can be chosen through the two incidences of `e`.  After deleting common
incidences, the red/blue symmetric difference of the two factors is
balanced at every owner and every q1-colour vertex, and hence decomposes
into closed alternating incidence circuits.  Toggling those circuits one
at a time preserves every owner degree and every q1 occurrence, never
deletes `e`, and ends at a q1-rainbow Hamilton cycle.  Opening `e` gives an
exact B1 sidecar.

This unrestricted reset does not make (3.3) obsolete.  Its circuits may use
incidences outside the protected four-resource catalogue and may change
upper colours, typed tail/head roles, residence guards, or the common-cap
state.  It is a legal postprocess of Theorem 2.2 only when every circuit
resource needed by those rows is included in the protected packet footprint
or a separate protected-incidence theorem is proved.  Thus there are two
honest positive interfaces:

* a complete-host closed-circuit reset, exact at owner/q1 level; or
* the protected-host seam flow/Rado certificate (3.3) or (3.8a).

One cannot silently combine the freedom of the first with the protected
rows of the second.

## 4. A finite four-resource cut: the Johnson octagon

Work first at `m=3` on `[6]`.  Consider the physical Johnson octagon

\[
 123,124,246,245,125,126,146,134,123.
\tag{4.1}
\]

Orient every edge from its even-position endpoint to its odd-position
endpoint.  The eight ordered atoms have resources

\[
\begin{array}{c|c|c|c|c}
i&\tau_i&\eta_i&\lambda_i&\upsilon_i\\ \hline
0&123&124&12&1234\\
1&246&124&24&1246\\
2&246&245&24&2456\\
3&125&245&25&1245\\
4&125&126&12&1256\\
5&146&126&16&1246\\
6&146&134&14&1346\\
7&123&134&13&1234
\end{array}
\tag{4.2}
\]

### Proposition 4.1 (opposite-shore parity cut)

Every four-resource matching in the support (4.2) has at most three atoms:

\[
                         \sum_{i=0}^7 z_i\le3.
\tag{4.3}
\]

Nevertheless `z_i=1/2` satisfies every individual lower, upper, tail, and
head capacity row and has total mass four.  More strongly:

* the even tail--head parity
  `\{e_0,e_2,e_4,e_6\}` has four distinct upper colours, but repeats lower
  colour `12`;
* the odd tail--head parity
  `\{e_1,e_3,e_5,e_7\}` has four distinct lower colours, but repeats upper
  colour `1246`.

Thus the lower--tail--head subsystem and the upper--tail--head subsystem
each have an integral size-four solution, but their joint four-resource
system does not.

#### Proof

Four atoms respecting tail and head capacity would be a perfect matching of
the physical octagon, hence one of its two alternating parities.  The
displayed repeated colours kill the two parities separately.  Three atoms,
for example `e_0,e_2,e_6`, are compatible, so the rank is exactly three.
Every typed resource occurs at most twice in (4.2), proving feasibility of
the half-vector. `square`

Adjoining a common `(m-3)`-set to every displayed middle vertex and leaving
a disjoint `(m-3)`-set unused suspends (4.2)--(4.3) to every `m>=3`.

This is the first relevant finite cut for a circuit-based cover-down.  A q1
sidecar which only enforces lower-colour injectivity selects the odd parity,
where the upper collision remains; an upper-flow selects the even parity,
where the q1/lower collision remains.  Therefore four marginal flows, or a
physical alternating-cycle flow plus a separate q1 check, cannot replace
the joint packet Hall condition.  A global construction may escape the
octagon through atoms outside this support, but it must explicitly provide
that escape.

Disjoint abstract copies of the octagon give an arbitrarily large aggregate
rank deficit.  Consequently a theorem based only on the local degree and
one-shore Hall data cannot guarantee `O(1)` leave; it needs a hypothesis
excluding, crossing, or paying these correlated rank cuts.  No claim is
made here that an arbitrary number of copies can be embedded as mutually
resource-disjoint suspended Boolean minors in one fixed dimension.

## 5. A finite sidecar-state obstruction in `J(5,3)`

The occurrence-labelled q1 sidecar in Section 3 is also necessary.  The two
Hamilton paths

\[
\begin{aligned}
T_{\rm good}={}&123,125,145,124,234,345,134,135,235,245,\\
T_{\rm bad}={}&145,134,345,135,125,245,235,234,124,123
\end{aligned}
\tag{5.1}
\]

have the identical endpoint state

\[
                         (z,\ell,\rho,b)=(0,1,1,0),
                         \qquad\delta_{\rm top}=0.
\tag{5.2}
\]

For `T_good`, the holes are `23,45` and the repeated colour is `34`.
Deleting `234-345` and closing the two pieces installs `23` and `45`, giving
a q1-rainbow two-factor.

For `T_bad`, the holes are `45,13` and the repeated colour is `25`, on
`125-245` and `245-235`.  Deleting the first occurrence gives no two legal
closures.  Deleting the second closes with colours `45,23`, not `45,13`.
Deleting any uniquely coloured edge creates another hole.  Hence there is
no inverse of the same one-cut/two-closure form.

Therefore the scalars (5.2), even with zero frozen deficiency, do not tell a
cover-down argument whether the rainbow-factor opening sidecar exists.  The
state passed to (3.8) must contain the actual factor/cut/seam occurrence
relation, or a certificate such as the flow in Section 3.  This witness does
not rule out a more global repair of `T_bad`.

## 6. Exact remaining verification target

For a near-perfect ordered-diamond matching, the missing deterministic
input is now the following concrete alternative.

*Positive route:* exhibit an outer compatibility graph with `O(1)` Hall
deficiency, packet families satisfying (2.5) (or Lemma 2.4), and a protected
q1 opening graph satisfying (3.6).  The packet definition must include every
tail/head and physical guard actually used.

*Cut route:* find a residual family for which either the outer deficiency
(2.2), the packet matching-number cut (2.5), or the sidecar deficiency (3.3)
grows.  The octagon proves that checking the four shores separately cannot
exclude the middle alternative.

The local independent-boundary absorber theorem supplies many candidates
for the packet families, but it does not verify their joint matching number.
That is the precise combinatorial cover-down step between the existing
`N-o(N)` matching and an `N-O(1)` matching.

There is also a quantitative reserve caveat.  If every installed negative
state has `a` atoms and the states are disjoint, a bank for `s` residual
pairs already occupies `as` matching atoms.  An unspecified `s=o(N)` is
enough when `a` is an absolute constant, but not when the known packet has
`a=Theta(m)`: one then needs at least `ms=O(N)`, and normally
`s=o(N/m)`, before a disjoint installed bank can be inferred from scale
alone.  Thus “bounded packet” must state whether the bound is absolute or
depends on the Boolean parameter.
