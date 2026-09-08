# A linear-size Boolean C14 reservoir; only named linkage remains

## Status

The one-label `C14` buffer is a fixed-size literal gadget: seven
rank-`(r-1)` roots, seven rank-`r` owners, and four sequential Boolean
`C6` flips between its two perfect-matching phases.  The complete orbit of
these gadgets contains a resource-disjoint bank of size at least `W/98`,
where

\[
                         W=\binom{2r-1}{r}.                \tag{0.1}
\]

The same remains true after avoiding any `o(W)` protected resource bank.
Thus a terminal demand of size `O(W/sqrt r)` is not limited by the number
of disjoint sequential buffers.

This does not route a named defect into a chosen anonymous buffer.  The
remaining theorem is an all-cut linkage from defect circuits to the
linear-size bank, with the lower flags carried along.  Capacity and local
sequentiality are now unconditional.

## 1. The gadget orbit

Put `n=2r-1`.  Choose

\[
 X\in\binom{[n]}{r-3}                                     \tag{1.1}
\]

and five distinct labels `a,b,c,d,e` outside `X`.  Use the roots

\[
 \begin{array}{lllllll}
 A=X+a+b,&B=X+a+c,&C=X+c+d,&D=X+b+d,\\
 P=X+a+d,&E=X+d+e,&F=X+b+e
 \end{array}                                               \tag{1.2}
\]

and owners

\[
 \begin{array}{lllllll}
 U=X+a+b+c,&V=X+a+c+d,&W=X+b+c+d,&Y=X+a+b+d,\\
 T=X+a+d+e,&Z=X+b+d+e,&K=X+a+b+e.
 \end{array}                                               \tag{1.3}
\]

They form the incidence cycle

\[
 A-U-B-V-C-W-D-Y-P-T-E-Z-F-K-A.                           \tag{1.4}
\]

The two alternating matchings of (1.4) are connected by the four literal
`C6` flips

\[
 (D,P,E),\quad(A,B,P),\quad(A,D,F),\quad(P,C,D).           \tag{1.5}
\]

This is Theorem 4.1 of
`MATH_THEOREM_BOOLEAN_INCIDENCE_C6_LATTICE_AND_SEQUENTIAL_C8_GATE_20260806.md`.

Let `mathcal H_14` be the labelled multihypergraph whose vertex set is the
disjoint union

\[
 \binom{[n]}{r-1}\ \dot\cup\ \binom{[n]}r                \tag{1.6}
\]

and whose edges are the fourteen resource sets (1.2)--(1.3), over all
choices of the labelled data.  Keeping labelled copies only strengthens
the counting statement; a matching never selects two copies with the same
physical resources.

### Lemma 1.1 (exact regularity)

`mathcal H_14` is `14`-uniform and regular.  If its common degree is
`D_14`, then

\[
                         |E(\mathcal H_{14})|
                              ={W D_{14}\over7}.           \tag{1.7}
\]

#### Proof

Ground-set permutations are transitive separately on each Boolean shore,
so the degree is constant on each shore.  Every gadget has seven vertices
on each shore, and the two shores both have cardinality `W`.  Double
counting incidences shows that the two constant degrees are equal; call
the value `D_14`.  Counting all fourteen incidences gives

\[
 14|E|=2W D_{14},                                         \tag{1.8}
\]

which is (1.7).  `square`

## 2. Linear-size disjoint bank

### Theorem 2.1 (anonymous C14 reservoir)

The gadget orbit contains a resource-disjoint matching of size at least

\[
                         {W\over98}.                       \tag{2.1}
\]

More generally, let `Z` be any protected collection of root/owner
resources.  There is a resource-disjoint gadget bank avoiding `Z` of size
at least

\[
                         {W\over98}-{|Z|\over14}.           \tag{2.2}
\]

#### Proof

Delete every gadget meeting `Z`.  Each protected resource belongs to
`D_14` labelled gadgets, so at most `|Z|D_14` edges are deleted.  The
remaining multihypergraph has at least

\[
                         D_{14}(W/7-|Z|)                   \tag{2.3}
\]

edges and maximum degree at most `D_14`.

Take a maximal matching `M`.  One selected `14`-edge meets at most

\[
                         14D_{14}                          \tag{2.4}
\]

labelled edges, by summing the degrees of its resources.  Maximality says
these neighbourhoods cover every remaining edge.  Hence

\[
 |M|\ge {D_{14}(W/7-|Z|)\over14D_{14}}
       ={W\over98}-{|Z|\over14}.                          \tag{2.5}
\]

For `Z` empty this is (2.1).  `square`

### Corollary 2.2 (mesoscopic capacity margin)

For every fixed `c` and all sufficiently large `r`, the orbit contains a
resource-disjoint bank of

\[
                         cW/\sqrt r                        \tag{2.6}

\]

sequential `C14` buffers, even after avoiding an `o(W)` protected bank.

Every buffer may carry fixed lower flags ending at its seven roots; both
phases cover those flags identically.

## 3. Prescribed circuits versus anonymous capacity

Theorem 2.1 chooses anonymous Boolean squares.  A prescribed terminal
`C8` circuit has only `Theta(r)` one-label `C14` extensions: its four main
roots and four main owners fix `X,a,b,c,d`, and only `e` varies.  A naive
greedy assignment of extensions to prescribed circuits therefore handles
only `O(r)` adversarial tasks.

There is a genuine concentration obstruction.  Distinct prescribed
squares may have the same diagonal pivot

\[
                         P=X+a+d.                           \tag{3.1}
\]

Every one-label extension then uses the same root `P`, so no two of those
extensions are resource-disjoint.  The linear anonymous bank does not by
itself resolve this pivot hotspot.

Thus the correct mesoscopic interface is not a raw count of gadgets.  Let
`mathcal D` be the family of terminal defect circuits and `mathcal B` a
fixed disjoint bank from Theorem 2.1.  Build a linkage graph in which a
defect is adjacent to a bank gadget when a sequence of protected
same-rank Johnson switches and Boolean `C6` transports moves its root/owner
circulation into that gadget while preserving its lower flags.  The exact
missing condition is

\[
                         |N_{\mathcal B}(\mathcal X)|
                           \ge|\mathcal X|
        \qquad(\mathcal X\subseteq\mathcal D).             \tag{3.2}
\]

Under (3.2), Hall assigns distinct resource-disjoint `C14` buffers to all
defects, and the four-flip theorem processes them independently.

## 4. Consequence for the global absorber

At the natural cover-down scale there are `O(W/sqrt r)` owner/root
defects.  Theorem 2.1 supplies `Omega(W)` disjoint terminal circuits, a
factor `Omega(sqrt r)` more than necessary.  The local Boolean trade
lattice is complete, and every square circuit has a sequential buffer.

Therefore the q1 terminal absorber has only one remaining non-scalar row:

> prove the all-cut protected linkage (3.2), or construct the cover-down
> so that its defect pivots are already dispersed across the anonymous
> C14 bank.

No further fixed-size-gadget packing theorem is needed.  Any failure of
the terminal route must be a named linkage/pivot concentration failure,
not a shortage of disjoint Boolean buffers.
