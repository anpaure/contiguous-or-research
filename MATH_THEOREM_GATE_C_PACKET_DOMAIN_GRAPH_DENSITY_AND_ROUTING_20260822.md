# Gate C: packet-domain graph density and exact routing conditions

**Status (2026-08-22).**  Every theorem below is proved.  The labelled
permutation graph of the `2b^2`-vertex binary absorber domains has diameter
at most two for every odd `b>=11`; the complement-doubled domain graph has
the same property.  On any genuinely disjoint domain atlas, the local
three-to-three transporter swaps generate every permutation of the packet
hole states.  A precise bipartite Hall condition is given for routing an
external packet family into an absorber atlas.

These are algebraic routing theorems, not a near-factor.  Dense adjacency
in the full labelled orbit does not by itself produce a large family of
simultaneously disjoint domains, nor does it ensure that an arbitrary leave
is tiled by the packet shapes.

## 1. Abstract binary domains

Let

\[
 b=2h+1\ge5,
 \qquad
 \mathcal V={\Omega\choose b},
 \qquad
 W=|\mathcal V|={2b\choose b}.                        \tag{1.1}
\]

A **binary absorber domain** is a set `D subset mathcal V` of size

\[
                              s=2b^2                  \tag{1.2}
\]

with two atom-matching states:

\[
 \text{off state }\{T\},
 \qquad
 \text{on state }\{U_0,U_1\},                        \tag{1.3}
\]

such that

\[
 D=T\dot\cup P=U_0\dot\cup U_1,
 \qquad |T|=|P|=|U_0|=|U_1|=b^2.                    \tag{1.4}
\]

Here `T,U_0,U_1` are genuine all-split product atoms and `P` is the packet
left uncovered in the off state.  The explicit deck construction in the
cross-split transporter theorem supplies such a domain for every odd
`b>=5`; only (1.2)--(1.4) are used below.

Retain all permutation labels: the placement indexed by `g` has support
`gD`.  Thus equal supports arising from different labels remain distinct
vertices.  Write this labelled orbit as

\[
 \mathfrak D=\{(g,gD):g\in\operatorname{Sym}(\Omega)\}. \tag{1.5}
\]

The **domain graph** has these labelled placements as vertices, with two
labels adjacent precisely when their domain sets are disjoint.

## 2. Density and diameter

### Lemma 2.1 (uniform intersection bound)

For every fixed domain placement `D_0`, a uniformly random labelled orbit
placement `gD` satisfies

\[
 \Pr(D_0\cap gD\ne\varnothing)
                         \le {s^2\over W}={4b^4\over W}.           \tag{2.1}
\]

#### Proof

For fixed middle vertices `S,T`, transitivity of the symmetric group gives

\[
                              \Pr(gS=T)={1\over W}.    \tag{2.2}
\]

Consequently

\[
 \mathbb E|D_0\cap gD|
 =\sum_{T\in D_0}\sum_{S\in D}\Pr(gS=T)
 ={s^2\over W}.                                      \tag{2.3}
\]

If the intersection is nonempty its size is at least one, so Markov's
inequality proves (2.1).  \(\square\)

Thus every labelled domain-graph vertex has non-neighbour proportion at
most `4b^4/W`.

### Theorem 2.2 (diameter two)

For every odd `b>=11`, any two labelled domain placements have a third
placement disjoint from both.  Hence the domain graph is connected and has
diameter at most two.

#### Proof

For fixed placements `D_1,D_2`, Lemma 2.1 and a union bound give

\[
 \Pr(gD\text{ meets }D_1\text{ or }D_2)
                         \le {8b^4\over W}.            \tag{2.4}
\]

At `b=11`,

\[
 {22\choose11}=705432>8\cdot11^4=117128.              \tag{2.5}
\]

Moreover

\[
 {{2b+2\choose b+1}\over{2b\choose b}}
 =4-{2\over b+1}
 >\left(1+{1\over b}\right)^4                       \tag{2.6}
\]

for `b>=11`; the left side increases and the right side decreases.  Thus
`W/b^4` is increasing from `b=11` onward.  The right side of (2.4) is
strictly less than one, so a common disjoint placement exists.  \(\square\)

The same proof gives a useful many-target form.

### Corollary 2.3 (common hub)

Any family of `q` labelled domain placements has a common disjoint orbit
placement whenever

\[
                              4qb^4<W.                 \tag{2.7}
\]

No disjointness among the original `q` domains is required for this
existence assertion.

#### Proof

Union-bound (2.1) over the `q` prescribed domains.  \(\square\)

## 3. Complement-symmetric domain graph

For the explicit product domain, `D` and its coordinate complement
`overline D` are disjoint.  Define the doubled domain

\[
                         H=D\dot\cup\overline D,
 \qquad |H|=4b^2.                                     \tag{3.1}
\]

Retain all labelled permutation copies of `H` and join disjoint copies.

### Theorem 3.1 (doubled diameter and hubs)

For every odd `b>=11`, the doubled-domain graph has diameter at most two.
More generally, `q` prescribed doubled domains have a common disjoint copy
whenever

\[
                             16qb^4<W.                 \tag{3.2}
\]

#### Proof

Replace `s` by `4b^2` in (2.3).  One prescribed doubled domain is met with
probability at most `16b^4/W`, and two are met with probability at most
`32b^4/W`.  At `b=11`,

\[
                       705432>32\cdot11^4=468512.      \tag{3.3}
\]

Monotonicity (2.6) propagates the inequality.  The `q`-domain assertion is
the corresponding union bound.  \(\square\)

Every doubled-domain state and every swap below can be performed together
with its coordinate complement, so this graph is the appropriate routing
object when terminal holes are required to remain complement-closed.

## 4. Exact state routing on a disjoint atlas

Let `D_1,...,D_m` be pairwise disjoint binary absorber domains.  In each
domain choose state `0` (off) or `1` (on).  Because the domains are
disjoint, every state vector

\[
                         \varepsilon\in\{0,1\}^m       \tag{4.1}
\]

defines an atom matching.  Its uncovered packet set inside the atlas is

\[
                         \mathop{\dot\bigcup}_{i:\varepsilon_i=0}P_i.       \tag{4.2}
\]

### Theorem 4.1 (binary-state permutation routing)

If two state vectors have the same number of `1` entries, their matchings
are connected by a sequence of three-to-three transporter trades, all
supported inside `D_1 dotcup ... dotcup D_m`.  Equivalently, the hole
packets can be permuted arbitrarily among the domains without changing the
number of atoms or holes.

#### Proof

If `epsilon_i=0,epsilon_j=1`, the states on `D_i,D_j` use respectively one
and two atoms.  Interchanging the states replaces three atoms by three
atoms and changes the covered packet from `P_j` to `P_i`; this is exactly
the transporter identity on two disjoint domains.  Transpositions of a
zero and a one generate every permutation of a binary vector with fixed
Hamming weight.  \(\square\)

If the domains use different coordinate splits, the corresponding swap is
a genuine cross-split trade.  The complement-doubled version permutes
complement-paired hole packets in exactly the same way.

The diameter theorem in Section 2 concerns the full orbit graph and must
not be confused with Theorem 4.1: a length-two graph path proves that an
intermediate disjoint placement exists, but all domains used by a
simultaneous atlas must still be pairwise disjoint from the rest of the
ambient matching.

## 5. Hall condition for an external packet family

Let `S_1,...,S_m` be structured hole packets which one wants to route, and
let `D_1,...,D_m` be pairwise disjoint absorber domains available as target
ports.  Form a bipartite graph `Gamma` with source packets on the left and
target domains on the right.  Join `S_i` to `D_j` when there is a certified
transporter placement which exchanges `S_i` with the packet `P_j` of
`D_j`.

Call the instance **support-compatible** if every graph matching in
`Gamma` has the following additional property: the transporter supports
assigned to its edges are pairwise disjoint outside their designated
source and target packets, and are disjoint from the fixed ambient
matching.  A pre-certified transporter atlas has exactly this property.

### Theorem 5.1 (exact packet-routing criterion)

In a support-compatible instance, if `Gamma` has a matching saturating all
source packets, the corresponding transporters route the entire source
family into distinct absorber ports.  Each target port starts in its on
state; accepting a source hole moves that hole to the port packet and puts
the port in its off state.  Toggling all ports back on then reduces the
leave by exactly `mb^2` vertices.  A saturating matching exists if and only
if

\[
                         |N_\Gamma(X)|\ge|X|
 \quad\text{for every source subfamily }X.            \tag{5.1}
\]

#### Proof

A saturating matching assigns a distinct target domain to every source.
Support compatibility says the selected transporter trades can be
performed without collision.  Each source packet is replaced by the off
packet at its assigned port; toggling that port from off to on covers the
port packet by the one-to-two absorber.
Every operation concerns disjoint certified supports, so their union is an
atom matching and covers `mb^2` previously uncovered vertices.  The final
equivalence is Hall's theorem.  \(\square\)

Without support compatibility, ordinary Hall expansion is not sufficient:
two graph edges chosen by a matching could still have colliding auxiliary
atoms.  The general problem would then be a matching problem with an edge
conflict system, rather than ordinary bipartite flow.

### Corollary 5.2 (a convenient dense-graph sufficient condition)

Suppose `Gamma` is a fixed balanced bipartite graph with `m` vertices on
each shore and every vertex has degree at least `m/2`.  Then it has a
perfect matching, and Theorem 5.1 applies.

#### Proof

For `|X|<=m/2`, the neighbourhood of any member of `X` has size at least
`m/2>=|X|`.  For `|X|>m/2`, if some right vertex lay outside `N(X)`, it
would have more than `m/2` non-neighbours and hence degree less than
`m/2`, a contradiction.  Thus Hall's condition holds.  \(\square\)

## 6. Exact remaining blocker

Theorems 2.2 and 3.1 prove that isolated packet transport has no global
orbit-connectivity obstruction: any two ports have a common disjoint
intermediate port once `b>=11`.  Theorem 4.1 gives complete routing inside
a disjoint atlas, and Theorem 5.1 identifies the exact Hall gate for
feeding external packets into that atlas.

What is still missing is a **simultaneous** construction with all three
properties:

1. a preliminary atom matching whose leave is, up to `o(W)`, tiled by the
   permitted packet shapes;
2. a near-spanning collection of pairwise compatible transporter and
   absorber supports; and
3. Hall expansion (5.1) between the actual leave packets and absorber
   ports.

Full-orbit density alone proves none of these simultaneous assertions.  It
does, however, reduce the positive Gate-C problem from finding a local
cross-split move—the move now exists—to constructing a global disjoint
packet-routing atlas.
