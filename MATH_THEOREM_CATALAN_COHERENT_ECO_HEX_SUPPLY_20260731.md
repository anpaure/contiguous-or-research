# Coherent ECO hexagons span the MMM plane-tree components

Date: 2026-07-31  
Status: exact all-dimension component-supply theorem and exact obstruction
to the standard-label-only strengthening; no simultaneous compatible,
private, decorated gluing-tree claim

## 0. Verdict

Use the paper parameter `n`, so the middle-levels graph has ground size
`2n+1`, shore ranks `n,n+1`, and the components of the canonical MMM factor
are indexed by plane trees with `n` edges.

There are two sharply different statements.

1.  A standard MMM gluing label

    \[
       x=110u0v,\qquad y=101u0v                         \tag{0.1}
    \]

    is all-six coherent in the sense of
    `MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md`
    **if and only if** `u` is empty.  In plane-tree language, coherence
    permits exactly the pull of a leaf through a degree-two parent.
    Consequently the standard coherent labels alone are disconnected from
    `n=5` onward.  They cannot contain a component-spanning tree for all
    dimensions.

2.  The full alternating-incidence catalogue contains an explicit coherent
    ECO family.  For every Dyck word

    \[
                         D=1u0v\in {\cal D}_{n-1},       \tag{0.2}
    \]

    put

    \[
                         h(D)=1u000v0.                   \tag{0.3}
    \]

    Let `H` be the support of `h(D)`, and let `a,b,c` be the three
    consecutive positions of the displayed `000`.  The incidence hexagon

    \[
    \begin{array}{lll}
       L_a=H+a,&L_b=H+b,&L_c=H+c,\\
       U_{ab}=H+a+b,&U_{bc}=H+b+c,&U_{ca}=H+c+a
    \end{array}                                         \tag{0.4}
    \]

    is alternating with the canonical factor and coherent.  Its three old
    factor edges lie in the components obtained by inserting one new leaf
    into three consecutive corners of the parent plane tree `D`.

    Every standard MMM plane-tree edge is co-contained in one such ECO
    hexagon, possibly together with a third component.  Since the standard
    MMM auxiliary graph is connected, the two-section of the coherent ECO
    component hypergraph is connected for every `n`.

Thus coherent component supply is unconditional once nonstandard incidence
hexagons are admitted.  What remains open is the correlated selection of a
compatible physical hypertree with a joint decoration, private or laminar
router state, residence, deeper shadows, sockets/voltage, and compiler
state.  Static hypergraph connectivity does not imply those rows.

## 1. Exact external-label calculation for a standard label

Append the terminal zero used by the middle-levels factor to (0.1), and use
the canonical coordinate positions `0,...,2n`.  The physical standard
hexagon is

\[
              (x_0,x_1,x_6,x_5,y_0,y_1),              \tag{1.1}
\]

where `x_i=f^i(x0)` and similarly for `y`.  Direct substitution in the MMM
word map `f` gives the following external factor-edge labels.

More explicitly, the six relevant external edges are

\[
\begin{array}{c|c}
\text{port}&\text{external neighbour}\\ \hline
x_0=110u0v0&110u0v1\\
y_0=101u0v0&101u0v1\\
x_1=110u1v0&010u1v0\\
x_5=101u1v0&001u1v0\\
y_1=111u0v0&011u0v0.
\end{array}                                           \tag{1.1a}
\]

The remaining lower port is `x_6=100u1v0`.  If `u=1p0q` with `1p0`
its first primitive factor, its external neighbour is obtained by changing
that displayed primitive-closing zero to one.  If `u` is empty, the
external neighbour instead changes the final zero to one.  This literal
table gives the following labels.

* At all three upper ports the nonhexagon edge deletes coordinate `0`:

  \[
                         e_{ab}=e_{bc}=e_{ca}=0.        \tag{1.2}
  \]

* At the lower ports `x_0` and `y_0` the nonhexagon edge inserts coordinate
  `2n`.  At the remaining lower port it inserts `2n` when `u` is empty.  If
  `u` is nonempty, write its first primitive factor as `1p0`, and put
  `ell(u)=|1p0|`; the remaining insertion coordinate is `ell(u)+2`.  Hence,
  as a multiset,

  \[
   \{d_a,d_b,d_c\}=
   \begin{cases}
      \{2n,2n,2n\},&u=\varnothing,\\
      \{2n,2n,\ell(u)+2\},&u\ne\varnothing.
   \end{cases}                                         \tag{1.3}
  \]

Because a nonempty Dyck word `u` has `ell(u)<=|u|<=2n-4`, its exceptional
label `ell(u)+2` is different from `2n`.  The coherent-hex criterion is
exactly equality of the three `d` labels and equality of the three `e`
labels.
Equations (1.2)--(1.3) therefore prove

\[
       \boxed{\text{standard label coherent}\iff u=\varnothing.}       \tag{1.4}
\]

The local lower-tube statement for a general standard label remains true;
it is simply weaker than all-six fixed-decoration coherence.  In
particular, the private triples of Proposition 8.2 in the gap-Hall note do
not imply (1.4).

## 2. Plane-tree classification of the standard coherent labels

Under the contour-word/plane-tree bijection, (0.1) pulls the leftmost leaf
child of the first root child up to the root.  The word `u` is the ordered
forest of the remaining children of that first child.  Thus `u` is empty
exactly when the pulled leaf has a degree-two parent.

Orient a coherent pull toward `y`.  On the unrooted plane tree it replaces

\[
                         z--p--\ell
       \quad\longmapsto\quad
                         z--p,\ z--\ell,              \tag{2.1}
\]

where `ell` is a leaf and `deg(p)=2`.  The old vertex `p` becomes another
leaf adjacent to `z`.  For `n>=3`, (2.1) strictly decreases the number of
degree-two vertices.

### Theorem 2.1 (normal-form classification)

For `n>=3`, every connected component of the standard coherent-label graph
contains a unique plane tree with no degree-two vertex adjacent to a leaf.
Equivalently, two plane trees are connected by standard coherent labels if
and only if their repeated reductions (2.1) have the same irreducible
normal form.

#### Proof

Termination follows from the strict decrease in the number of degree-two
vertices.  Two reductions with disjoint supports commute.  Reductions which
share only their attachment vertex also commute.  The only remaining
critical overlap has two adjacent degree-two vertices, each with a leaf on
its other side; the whole local tree is the four-vertex path.  Reducing from
either end gives the same three-leaf plane star.  Hence the terminating
rewrite system is locally confluent.  Newman's lemma gives a unique normal
form.  Reversing reductions gives the component statement.  \(\square\)

For every `n>=5` there are at least two irreducibles: the `n`-edge star and
the double star whose adjacent centres carry respectively `2` and `n-3`
leaf neighbours.  Neither contains a degree-two vertex, and their degree
sequences differ.  Therefore:

\[
 \boxed{\text{the standard coherent-label graph is disconnected for every
        }n>=5.}                                        \tag{2.2}
\]

At `n=5` the six plane-tree components split exactly into two standard
coherent components of order three:

\[
\begin{split}
 &\{1010101010,1010101100,1011001100\},\\
 &\{1010110100,1010111000,1011110000\}.               \tag{2.3}
\end{split}
\]

The five coherent standard labels give two three-vertex paths (one edge is
represented twice).  The potential-decreasing source `1010110100` has only
the noncoherent option

\[
                    1101001010\longleftrightarrow1011001010.          \tag{2.4}
\]

Thus even the canonical potential-decreasing arborescence cannot be made
all-six coherent at this first obstructed dimension.

## 3. The coherent ECO atom

Let `D=1u0v` be any Dyck word of semilength `n-1`, and construct (0.3)--
(0.4).  Written as binary words, the six ports are

\[
\begin{array}{lll}
  L_a=1u100v0,&L_b=1u010v0,&L_c=1u001v0,\\
  U_{ab}=1u110v0,&U_{bc}=1u011v0,&U_{ca}=1u101v0.
\end{array}                                           \tag{3.1}
\]

Direct application of `f` shows that the old factor matching is

\[
                 L_aU_{ca},\qquad L_bU_{ab},\qquad L_cU_{bc}.          \tag{3.2}
\]

The other factor edge at every lower port inserts the final coordinate
`d=2n`; the other factor edge at every upper port deletes the initial
coordinate `e=0`.  Hence

\[
                         d_a=d_b=d_c=2n,qquad
                         e_{ab}=e_{bc}=e_{ca}=0,       \tag{3.3}
\]

so the hexagon is coherent.  Cyclic coordinate rotation gives `2n+1`
copies with `(d,e)=(j-1,j)` modulo `2n+1`.

The central `000` in (0.3) is the three-corner leaf-insertion window.  If
one deletes the newly inserted leaf from any of the three old matching
edges in (3.2), the underlying pointed plane tree is `D`.  The three factor
components incident with the atom are therefore the (not necessarily
distinct) unrooted plane trees obtained by inserting a leaf in the three
consecutive corners at the distinguished root edge of `D`.

There are `Cat_{n-1}` atoms with fixed `(d,e)=(2n,0)` and

\[
                         (2n+1)\operatorname{Cat}_{n-1}               \tag{3.4}
\]

coordinate-rotated atoms in this explicit family.

Their forced owner triples are, in the notation of the coherent-hex
theorem,

\[
 \{H+d+a+b,H+d+b+c,H+d+c+a\},\qquad
 \{H-e+a,H-e+b,H-e+c\}.                               \tag{3.5}
\]

Formula (3.5) is local.  It does not assert cross-atom occurrence privacy
or a joint SDR.

### Theorem 3.1 (the fixed-rotation forced-face overlap is a path forest)

Assume `n>=3` and restrict to the `Cat_{n-1}` atoms with
`(d,e)=(2n,0)`.  Every physical port
and every forced owner colour in (3.5) occurs in at most two atoms.  The
physical-port collision graph and the two owner-colour collision graphs are
all identical.  Their directed edges are exactly

\[
 D=1p\,10\,0v
       \quad\longrightarrow\quad
 D'=1p\,0\,10v,                                      \tag{3.6}
\]

where `p,v` are Dyck words of total semilength `n-3`.  The atoms share the
physical ports `L_b(D)=L_a(D')` and `U_ab(D)=U_ca(D')`.  The corresponding
lower-owner collision has roles `b,a`, and the upper-owner collision has
roles `ab,ca`.

Consequently this common collision graph is a disjoint union of directed
paths and has exactly `Cat_{n-2}` edges.

#### Proof

For `D=1u0v`, the three lower-port words are the first row of (3.1), and
the three lower owner words, in roles `a,b,c`, are

\[
                0u100v0,\qquad0u010v0,\qquad0u001v0.  \tag{3.7}
\]

The three upper owner words have the same variable cores with the fixed
initial/final owner bits added.  Equality of two words in (3.7) is
impossible except between a role-`b` word and a role-`a` word.  Unique Dyck
factorization then gives

\[
                 u=p10,quad u'=p,quad v'=10v,       \tag{3.8}
\]

which is precisely (3.6).  The same word equality in (3.1) gives the two
shared physical ports, and substitution in the upper owner words gives the
same pair and roles `ab,ca`.  No other role pair has compatible fixed
prefixes.  The move decreases the semilength of the first child forest `u`
by one.  It has at most one predecessor and at most one successor, so the
collision graph is an acyclic graph of maximum degree two, hence a path
forest.  Finally `(p,v)` range over pairs of Dyck words of total semilength
`n-3`; Catalan convolution gives `Cat_{n-2}` edges.
\(\square\)

Thus one independent set in this path forest simultaneously makes the
selected ECO hexagons vertex-disjoint and removes all forced-owner
repetitions on both shores.  This is stronger than three unrelated conflict
systems, but repeated physical occurrences outside the six ports can still
share a router bottleneck.  Hence (3.6) does not by itself prove
occurrence-router resilience.

For `n<=2` the fixed-rotation collision system is empty or trivial and is
checked directly.  The `Cat_{n-2}` edge formula is asserted only for
`n>=3`.

## 4. Every standard edge is shadowed by a coherent ECO atom

### Theorem 4.1 (leaf-deletion shadow)

Let `x=110u0v,y=101u0v` be any standard MMM gluing pair, coherent or not.
The plane-tree components `[x]` and `[y]` both occur among the old matching
components of one coherent ECO atom.

#### Proof

In the rooted plane-tree interpretation, (0.1) moves one distinguished leaf
across the edge joining its parent to the root.  Delete that distinguished
leaf on both sides.  The two results are the same unrooted plane tree,
represented by the Dyck word

\[
                              D=1u0v.                 \tag{4.1}
\]

Root `D` at the corner immediately preceding the moved edge.  The two
positions of the leaf before and after the pull are two of the three
consecutive insertion corners in the ECO atom (0.3)--(0.4).  Thus two of
the old factor edges in that atom lie in `[x]` and `[y]`; the third may lie
in either of these components or in a third component.  This is invariant
under choosing another rooted rotation of `D`.  \(\square\)

### Corollary 4.2 (all-dimension coherent component supply)

Let `A_n` be the standard MMM auxiliary graph on the `n`-edge plane-tree
components, and let `E_n` be the hypergraph whose hyperedges are the sets of
factor components touched by the coherent ECO atoms.  Then the two-section
of `E_n` contains `A_n`.  In particular it is connected for every `n`.

#### Proof

Theorem 4.1 shadows every edge of `A_n`.  The standard potential-decreasing
MMM arborescence proves that `A_n` is connected.  \(\square\)

This is a static supply theorem.  A family of hyperedges which is connected
in the component two-section need not be simultaneously toggleable.  A
physical proof still has to choose an ordered Berge tree or hypertree whose
old port edges remain present, control overlaps/interleaving, and carry the
same joint decoration and router state throughout.

## 5. Finite calibration and scope

The lightweight literal audit reconstructs the canonical factor and all
incidence hexagons through `n=7`.  It verifies:

* the standard criterion (1.4) on every standard label;
* the normal-form component counts

  \[
               1,1,1,2,3,6\quad(n=2,3,4,5,6,7);       \tag{5.1}
  \]

* every literal ECO atom (0.3)--(0.4), including (3.2)--(3.3);
* co-containment of every standard auxiliary edge and connectivity of the
  coherent component hypergraph; and
* the common forced-owner path-forest law (3.6); and
* for `n=3,4,5,6,7`, existence inside one fixed coordinate rotation of a
  coherent hypertree with pairwise-disjoint physical ports and pairwise-
  disjoint forced owner triples on both shores, whose simultaneous symmetric
  difference with the base factor is one Hamilton cycle.

The final bullet is finite evidence, not the all-`n` compatibility theorem.
It also says nothing about a common alternating SDR, forced-port gap Hall,
router resilience, residence, deeper shadows, or the lower compiler.

Run

```text
python3 scratch/audit_catalan_coherent_eco_hex_supply_20260731.py
```

The frozen output is

```text
scratch/catalan_coherent_eco_hex_supply_20260731.audit.json
```
