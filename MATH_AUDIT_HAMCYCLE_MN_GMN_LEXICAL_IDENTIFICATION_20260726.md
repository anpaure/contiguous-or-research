# Audit of the `HamCycle`–lexical-factor identification

## 1. Question and verdict

Fix $r\ge 1$, and let

\[
G_r=Q_{2r+1}(r,r+1),\qquad
F_{\rm lex}=M^0\cup M^1
\]

denote the middle-levels graph and the standard $0/1$-lexical cycle
factor, with the harmless bit-reversal convention understood.  The
question is whether the edge set emitted by

`tmp/cos/code/bits/mlc_hamcycle.cpp`

is proved by the local source bundle to have the form

\[
F_{\rm lex}\mathbin\triangle
   \bigtriangleup_{e\in T_r} C_6(e),                 \tag{1.1}
\]

where $T_r$ is a spanning tree of the plane-tree component graph and
the $C_6(e)$ are the compatible alternating hexagons of the
Gregor--Mütze--Nummenpalo construction.

**Verdict.**  The local sources give strong evidence for (1.1), and the
path-flip code can be checked directly to perform one alternating
hexagon switch.  They do **not**, however, contain a self-contained
proof of the two global identifications needed for (1.1):

1. that the unflipped MN path system $H_r$ is exactly the $0/1$-lexical
   path system; and
2. that `is_flip_tree_tau()` selects a spanning tree in precisely the
   GMN flippable-pair graph, with the required global compatibility.

Thus (1.1) is a precise, standard-looking **provenance lemma**, but it
must be imported from the cited MN/GMN papers or proved separately.  It
does not follow merely from the fact that the program outputs a middle
levels Hamilton cycle, nor from the Gregor copyright line in the
adapted `bits` file.

## 2. What the local sources establish

The following attributions are explicit.

* `mlc_hamcycle.cpp`, lines 26--29, says that its functions are taken
  from Mütze--Nummenpalo, *A constant-time algorithm for middle levels
  Gray codes*, with straightforward adaptations.
* `mlc_tree.hpp`, lines 25--29, and `mlc_vertex.hpp`, lines 24--28, make
  the same MN attribution, in the latter two cases without changes.
* `mlc_vertex.hpp`, lines 59--80, identifies the two path systems as
  $P_r\subset H_r$ and
  \(\overline{\operatorname{rev}}(P_r)\subset
  \overline{\operatorname{rev}}(H_r)\), and identifies the recursion
  with the MN rule \(\sigma\).
* `mlc_tree.hpp`, lines 50--55 and 120--124, says that
  `is_flip_tree_tau()` recognizes edges of a canonical spanning tree in
  the auxiliary graph from the MN paper.
* `tmp/cos/web/middle/info.html`, lines 5--8, likewise attributes the
  executable construction to the MN constant-time algorithm, not to
  the later short proof.

On the other hand, `tmp/central/gmlc2.tex`, lines 625--627, explicitly
states that the $\ell=1$ factors in Mütze's 2016 proof and in the 2018 GMN
short proof are the union of all $0$- and $1$-lexical edges, up to
bit reversal.  Lines 686 and 997--1014 attribute, respectively, the
plane-tree component description and the compatible flipping-$6$-cycle
facts to GMN.

These statements place the two constructions extremely close, but no
local line says that the MN object called $H_r$, or the particular
canonical tree recognized by `is_flip_tree_tau()`, is the corresponding
GMN lexical object.

## 3. Direct audit of one coded path flip

There is nevertheless an exact local fact that needs no external
paper.

### Proposition 3.1 (the coded `flip=true` operation is one $C_6$ switch)

Let $x$ be a first path vertex whose rooted tree is a
`tau`-preimage, and let $y=\tau(x)$.  Suppressing all unchanged
coordinates, their first three bits are

\[
x=110\cdots,\qquad y=101\cdots .                 \tag{3.1}
\]

Let $b\ge3$ be the first-touchdown coordinate of $x$.  Replacing the
two unflipped paths by the two paths generated with `flip=true` changes
their union by symmetric difference with exactly one alternating
$6$-cycle.

#### Proof

For $x$, lines 204--220 generate the unflipped sequence.  In the
`tau` situation, the first six entries are, as recorded and asserted at
line 256,

\[
(b,0,2,1,0,2).                                  \tag{3.2}
\]

For $y$, the prefix $10$ makes its unflipped path the two-step path
with flip sequence $(1,0)$.  Lines 227--232 replace the $x$-path by
the two-step sequence $(2,0)$.  Lines 234--263 replace the first six
entries of the $y$-path by

\[
(b,0,1,2,0,1),                                  \tag{3.3}
\]

after which it follows the same remaining recursion as the old long
path.

Write only the coordinates $(0,1,2,b)$.  The old long path begins

\[
1100,1101,0101,0111,0011,1011,1001,             \tag{3.4}
\]

whereas the new long path begins

\[
1010,1011,0011,0111,0101,1101,1001.             \tag{3.5}
\]

Their four middle edges agree, in reverse order.  The old and new short
paths are

\[
1010,1110,0110
   \quad\hbox{and}\quad
1100,1110,0110,                                  \tag{3.6}
\]

so their last edge also agrees.  Cancelling all common edges, the old
three edges and new three edges alternate on

\[
1100-1101-1001-1011-1010-1110-1100.             \tag{3.7}
\]

All omitted coordinates are fixed.  Hence (3.7) is a literal cube
$6$-cycle and the replacement is its symmetric difference. □

This calculation proves that the implementation is not using an
arbitrary large rerouting at each selected tree edge.  It does **not**
by itself prove that all selected hexagons are the globally compatible
GMN family or that their quotient edges form a spanning tree.

## 4. Exact conditional identification

The missing statement can be isolated without ambiguity.

### Provenance lemma $\mathrm{MN}\Rightarrow\mathrm{GMN}_{\rm lex}$

For every $r$:

1. with every call to `compute_flip_seq_0` made with `flip=false`, the
   two MN path shores together with the last-coordinate seams have edge
   set $F_{\rm lex}$, up to one fixed coordinate reversal; and
2. the undirected `tau` pairs accepted by `is_flip_tree_tau()` are the
   edges of a spanning tree $T_r$ of the GMN plane-tree auxiliary
   graph, and the corresponding hexagons from Proposition 3.1 form a
   compatible GMN switching family.

### Theorem 4.1 (conditional source identification)

If the provenance lemma holds, then the implemented `HamCycle` has
edge set (1.1), is a Hamilton cycle obtained from the standard lexical
factor, and uses exactly

\[
|T_r|=p_r-1\le \operatorname{Cat}_r-1             \tag{4.1}
\]

hexagon switches, where $p_r$ is the number of plane-tree components
of $F_{\rm lex}$.

#### Proof

Part 1 of the provenance lemma identifies the initial factor.  By
Proposition 3.1 every accepted tree edge performs the corresponding
alternating $C_6$ symmetric difference.  Part 2 makes these switches
compatible and makes their quotient edges a spanning tree.  Each switch
therefore joins two current factor components, so $p_r-1$ switches
produce one spanning cycle.  Finally every plane-tree component has at
least one rooted plane-tree representative, of which there are
$\operatorname{Cat}_r$, proving $p_r\le\operatorname{Cat}_r$. □

## 5. Consequence for the opposite-triple defect

Let

\[
W_r=\binom{2r+1}{r}=(2r+1)\operatorname{Cat}_r.
\]

The audited lexical-factor theorem gives the initial opposite-triple
defect

\[
\delta(F_{\rm lex})
=W_r\frac{r+1}{2(2r-1)}
=\left(\frac14+O(r^{-1})\right)W_r.              \tag{5.1}
\]

One alternating $C_6$ replaces three factor edges, so it can change
at most three opposite triple occurrences.  Under the provenance lemma,
(4.1) therefore gives

\[
\delta(\mathrm{HamCycle}_r)
\ge \delta(F_{\rm lex})-3(p_r-1)
=\left(\frac14-o(1)\right)W_r.                  \tag{5.2}
\]

Thus the new linear-defect conclusion transfers immediately **if** the
provenance lemma is imported.  Without that lemma, (5.2) should not be
asserted for this executable merely from its Hamiltonicity or its file
attribution.

## 6. Sharp audit boundary

The strongest unconditional local conclusion is Proposition 3.1: each
MN `tau` path replacement is literally an alternating hexagon.  The
smallest remaining source-identification task is to prove the two-part
provenance lemma above.  No evidence in the local source bundle points
to a counterexample; the issue is absence of the exact edge-level
bridge, not contrary evidence.
