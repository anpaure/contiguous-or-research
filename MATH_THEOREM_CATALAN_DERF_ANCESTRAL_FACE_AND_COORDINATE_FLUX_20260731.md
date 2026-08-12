# DERF ancestral faces, component births, and coordinate flux

Date: 2026-07-31  
Status: dimension-free structural theorem; independently replayed on the
authenticated strict chain at child parameters `n=3,4,5`.  This does not
prove that the strict coupled side certificate exists in every dimension.

## 0. Result

The strict direct-edgewise lift has a stronger recursive normal form than
the one-step trace-block ledger suggests.

If `F_n` is the child Catalan linear forest and `F_(n+1)` is any valid
strict lift using the new coordinates `(c,z)`, then

\[
 F_{n+1}=(c+F_n)\;\dot\cup\;B_{n+1}.                 \tag{0.1}
\]

Here `c+F_n` is the whole selected-support face `(c,z)=(1,0)`, no selected
edge leaves that face, and `B_(n+1)` is a path forest with exactly

\[
 \operatorname {Cat}_{n+1}-\operatorname {Cat}_n     \tag{0.2}
\]

components.  All choices of `Q`, all direct lift/projection labels, both
side forests, and all collar seams live in `B_(n+1)`.

Consequently a chain has a canonical **component-birth decomposition**.
Every component born at one step is translated unchanged through every
later `(c,z)=(1,0)` face.  The graphic condition factors onto the newborn
complement, canonical component roots translate, and every internal
residence motif is inherited literally forever.  Thus strict DERF alone
cannot repair a nonresident ancestor: flat residence must hold separately
on the base and on every newborn bank, or a non-strict/internal/nonflat
actuator is necessary.

There is also an exact coordinate-flux row.  Direct occurrence labels `x`
are constant on their physical edge and disappear from this row.  Only the
parent-edge multiplicities, the retained bank, and the oriented head labels
of `Q` remain.  This is a dimension-free quotient of the coupled search;
it is necessary, but it does not replace the palette or graphic rows.

After a role-safe side shore has been selected, it has a second canonical
normalization which is genuinely invariant under relabelling.  Orient its
components by their selected tail/head roles and delete the first arc out of
the source anchor of every two-anchor path.  The resulting **source-ear
kernel** has a forced rooted-tree-plus-free-path form.  All side residence
motifs are then either kernel-internal or the unique prefix motif of one
source ear.  This deterministic rule extracts and transfers state; it does
not choose `Q` or the shore representatives.

The finite witness contains no stronger canonical choice pattern.  At
child `n=5`, every one of the six immediately preceding sector types
contains both selected and retained `Q` edges, and both side SDRs use old,
previous-`c`, and previous-`z` lift labels.  In particular, neither a
sector-only `Q` rule nor an always-new-coordinate lift rule is supported.

## 1. Parameters and strict support

Write

\[
\begin{aligned}
 M&=\binom{2n}{n},&N&=\binom{2n}{n-1},
 &P&=\binom{2n}{n-2},\\
 K&=\operatorname {Cat}_n=M-N,
 &C&=\operatorname {Cat}_{n+1}=M-P,
 &H&=C-K=N-P,
 &R&=N-C=P-K.
\end{aligned}                                         \tag{1.1}
\]

Let the oriented child atoms be

\[
 q=(L_q,U_q,t_q,h_q),\qquad
 L_q=t_q\cap h_q,\quad U_q=t_q\cup h_q.              \tag{1.2}
\]

A strict certificate chooses a common bank `Q`, `|Q|=C`, `P` upper direct
lifts and `P` lower direct projections.  Its physical support consists of

* every child edge as `c+t_q -- c+h_q`;
* the selected upper edges `t_q+x -- h_q+x`;
* the selected lower edges `t_q-x -- h_q-x`;
* for `q notin Q`, the central edge `z+t_q -- z+h_q`;
* for `q in Q`, the two seams

\[
 U_q\;--\;(z+t_q),\qquad
 (z+h_q)\;--\;(c+z+L_q).                              \tag{1.3}
\]

The exact outer palettes, inherited punctures, role caps, and acyclicity
are the strict DERF conditions from the parent theorem.

## 2. Ancestral-face factorization

### Theorem 2.1 (isolated ancestral face)

Let `A` be the rank-`n+1` vertex face with `(c,z)=(1,0)`.  In every strict
lift,

\[
 F_{n+1}[A]=c+F_n,\qquad \delta_{F_{n+1}}(A)=\varnothing. \tag{2.1}
\]

This is an induced-face statement for the selected physical support, not
for the ambient Johnson graph.

#### Proof

The copied child edges have both endpoints in collar sector `10`.  Upper
direct edges are in `00`, central edges in `01`, and lower direct edges in
`11`.  The two seams in (1.3) join `00--01` and `01--11`.  Hence no support
edge other than a copied child edge is incident with sector `10`, and no
support edge crosses its boundary.  Removing the constant label `c` from
the copied edges recovers `F_n` literally.  \(\square\)

### Corollary 2.2 (newborn complement and graphic factorization)

The complementary support `B_(n+1)` has

\[
 |V(B_{n+1})|=2N+M,\qquad
 |E(B_{n+1})|=2P+2C+(N-C),                            \tag{2.2}
\]

and, whenever the complete strict support is a Catalan linear forest,

\[
 c(B_{n+1})=H=C-K.                                    \tag{2.3}
\]

Moreover, since `c+F_n` is already a linear forest and has no boundary
edge, the complete degree/acyclicity row holds if and only if it holds on
`B_(n+1)`.

#### Proof

The active collar sectors `00,01,11` contain respectively `N,M,N`
vertices.  Their edges are the two `P`-edge direct sides, the `2C` seams,
and the `N-C` retained central edges, proving (2.2).  The complete output
has `C` components and its isolated ancestral summand has `K`; subtraction
gives (2.3).  Degree and cycle rank add across a disjoint union. \(\square\)

### Proposition 2.3 (contracted rooted-path normal form)

Contract the `H` upper-side components, the `C+K` retained-central
components, and the `H` lower-side components before adding the seams.
The active contraction has

\[
 3C-K\text{ vertices},\qquad 2C\text{ edges}.         \tag{2.4}
\]

Every contracted vertex has degree at most two.  Therefore the active
graphic row is exactly the assertion that this contraction is an
`H`-component path forest.  A rooted-tree representative is consequently
only a choice of one endpoint of each contracted path; there is no hidden
branching state.

#### Proof

The vertex count is

\[
 H+(C+K)+H=3C-K.
\]

Every side block is a path and an anchor already carrying a seam has side
degree at most one, so only its two endpoints can be seam anchors.  Every
retained central block is a segment of a child path cut at `Q`, and again
has at most two exposed ends.  Hence contracted degree is at most two.
There are two seams for each member of `Q`.  If the contraction is acyclic,
its component count is `(3C-K)-2C=C-K=H`; conversely a cycle there is a
cycle after expansion. \(\square\)

For a labelled deterministic normalization, root each contracted path at
its least encoded endpoint.  For the inherited paths, root at the least of
the two physical endpoints.  The latter root translates from `r` to `c+r`
because adjoining the same high bit preserves the endpoint order.  This
normalizes a given certificate; it does not choose or prove a certificate.

### Proposition 2.4 (canonical source-ear rooted-defect normal form)

Let one selected side forest have `e` anchor-free components.  Then its
anchor-load profile is forced:

\[
 c_0=e,\qquad c_1=C-2K-2e,\qquad c_2=K+e.             \tag{2.5}
\]

Role injectivity orients each nontrivial component as a directed path.  In
every two-anchor path, one anchor is its source and one its sink.  Delete
the first directed edge leaving the source anchor.  The result consists of

* exactly `C` one-anchor rooted paths;
* exactly `e` unrooted paths; and
* exactly `R-e` retained kernel edges and `K+e` deleted ears, the latter
  forming a matching between the rooted paths.

After identifying all `C` roots, the rooted kernel is a tree.  The deletion
rule depends only on directed roles and anchor incidence, so it commutes
with every coordinate relabelling and child-component reordering.  In
particular it is a dimension-free deterministic normalization of a supplied
side forest; numeric mask order is not used.

#### Proof

There are `H` side components and `C` distinct anchors.  An anchor has side
degree at most one, so a path component has at most two anchors.  Hence

\[
 c_0+c_1+c_2=H=C-K,\qquad c_1+2c_2=C,
\]

which gives (2.5).  Degree/role safety and acyclicity make each nontrivial
component a consistently directed path.  Its two degree-one anchors are
therefore its source and sink.  Deleting the source arc creates a singleton
source-rooted path and a sink-rooted remainder.  Every former one-anchor
path is unchanged and every empty path remains unrooted.  Therefore the
rooted count is `c_1+2c_2=C`, the unrooted count is `e`, and the ear count
is `c_2=K+e`; the retained count is `P-(K+e)=R-e`.  Distinct deleted edges
came from disjoint old components, so
no new rooted component is incident with two ears.  Finally, identifying
the unique root of each of `C` disjoint rooted trees gives one tree.
\(\square\)

### Corollary 2.5 (source-ear residence factorization)

For one side path, call a three-edge window bad for coordinate `i` when its
four consecutive vertex bits are `0,1,1,0`.  If `B`, `B_ker`, and `B_ear`
count all bad side windows, kernel-internal bad windows, and bad windows
meeting a source ear, respectively, then

\[
 B=B_{\rm ker}+B_{\rm ear},\qquad B_{\rm ear}\le K+e. \tag{2.6}
\]

More precisely, a bad window meeting an ear is the unique prefix
three-edge window of its original path, and each ear supplies at most one
such bad coordinate.

#### Proof

A source ear is the first edge of its directed path, so any three-edge
window meeting it must be the first window.  Every other window is wholly
kernel-internal.  A Johnson edge inserts one coordinate; the first bit
change in a `0,1,1,0` word must be that inserted coordinate, so the prefix
window is bad for at most one coordinate.  \(\square\)

### Proposition 2.6 (alternating central quotient)

Let `e^-` and `e^+` be the upper and lower anchor-free counts.  Suppress
all one-anchor side paths as leaves.  Each two-anchor upper path becomes
one upper link between two retained-central components, and each
two-anchor lower path becomes one lower link.  The two link banks have
sizes

\[
 K+e^-,\qquad K+e^+,                                  \tag{2.7}
\]

and are matchings.  Their union is an alternating path forest on the
`C+K` central components.  If the complete support is acyclic, it has

\[
 H-e^--e^+                                             \tag{2.8}
\]

quotient paths.  Adding the `e^-+e^+` pure side paths and the `K` copied
child paths gives exactly `C` ambient components.

#### Proof

Removing `Q` from an oriented child path leaves oriented segments.  At
most one upper seam is exposed at the outgoing end of a segment and at
most one lower seam at its incoming end.  Thus no central component is
incident twice to the same shore, so each link bank is a matching and link
labels alternate.  Its edge count is (2.7) by Proposition 2.4.  Acyclicity
then gives

\[
 (C+K)-(2K+e^-+e^+)=H-e^--e^+
\]

components.  The displayed ambient ledger follows by addition. \(\square\)

This is the sharp rooted-tree state exposed by the witnesses.  It reduces
the active topology to two coloured matchings on central roots; it does
not prove that representatives realizing the required matchings exist.

## 3. Iterated component births

For a strict step `j -> j+1`, let `B_(j+1)` denote the active complement
from Corollary 2.2 and let `iota_j(S)=S+{c_j}`.  Repeated use of Theorem 2.1
gives the literal disjoint union

\[
 F_N=\iota_{n,N}(F_n)\;\dot\cup\!
 \coprod_{j=n}^{N-1}\iota_{j+1,N}(B_{j+1}),           \tag{3.1}
\]

where `iota_(a,N)` adjoins every later `c` and no later `z`.  Its component
counts telescope:

\[
 \operatorname {Cat}_n+
 \sum_{j=n}^{N-1}
   (\operatorname {Cat}_{j+1}-\operatorname {Cat}_j)
 =\operatorname {Cat}_N.                              \tag{3.2}
\]

Thus every final component has a unique birth level.  `Q`, lift labels,
and contracted roots at later levels cannot change any earlier cohort.
This is the strongest deterministic recursive pattern present in the
strict construction: inheritance is forced, while every genuine choice is
confined to the new birth bank.

There is also a canonical six-bank provenance partition of the next child
edge set:

\[
 (\text{copied},\text{upper},\text{lower},\text{retained center},
   \text{upper seam},\text{lower seam})
 =(N,P,P,N-C,C,C).                                    \tag{3.3}
\]

It is preserved as a labelled decomposition at every step.  It is useful
for recursive state transfer, but Section 6 shows that the next `Q` is not
a union of provenance banks in the authenticated chain.

## 4. Exact residence factorization

Call an internal positive-run event any positive coordinate run lying
strictly between both endpoints of one path; fix any forbidden length
threshold `d+1`.

### Theorem 4.1 (birthwise residence if and only if)

Under the decomposition (3.1), the internal-run event set of `F_N` is the
disjoint translated union of the event sets present in `F_n` and in the
birth banks `B_(j+1)` at their birth.  In particular,

\[
 F_N\text{ is internally depth-}d\text{ resident}
 \iff F_n\text{ and every }B_{j+1}\text{ are.}        \tag{4.1}
\]

#### Proof

Translation by a later `c` changes no old coordinate word.  The new `c`
word is constant one along the whole path, so its sole positive run meets
both path endpoints and is not internal.  The new `z` word is constant
zero.  The component is isolated by Theorem 2.1, so neither endpoint nor
path order is later altered.  Apply this independently to every cohort in
(3.1). \(\square\)

This is stronger than a one-step inheritance warning.  It is a sharp
obstruction: no future strict choice can pay an old residence debt.  A
flat all-dimension proof must either construct each birth bank resident
jointly with its palettes, begin from a resident base, or leave strict DERF
through an interior rethread, facet actuator, or nonflat compiler.

### Theorem 4.2 (exact new-coordinate motifs)

Within the newborn complement:

1. internal positive runs of the new coordinate `c` are in bijection with
   the **double-anchor lower-side components**; the run length is exactly
   the number of vertices in that lower path;
2. internal positive runs of the new coordinate `z` are exactly the
   maximal weighted corridors of `z` and `cz` blocks lying between two
   upper `0` blocks; their length is the sum of the block orders in the
   corridor.

Hence new-`c` depth-`d` residence is equivalent to every double-anchor
lower component having order at least `d+1`.  New-`z` residence is
equivalent to every internal upper-to-upper corridor having total order at
least `d+1`.

#### Proof

The coordinate `c` is one exactly in sectors `c` and `cz`.  A copied `c`
path is a whole isolated component, so its all-one run is not internal.
In the active complement the one-blocks are precisely lower `cz` paths.  A
zero-, one-, or two-anchor lower component is respectively a pure output
component, a terminal block, or a block flanked by central `z` blocks.
Only the last is internal, and translation does not change its order.

The coordinate `z` is one exactly in sectors `z` and `cz`.  Its maximal
positive runs are therefore the maximal consecutive `z/cz` corridors.
Such a corridor is internal precisely when an upper `0` block lies on both
sides.  Length is additive over its trace blocks. \(\square\)

In the authenticated chain, the depth-two event genealogy is

\[
\begin{array}{c|rrrr|r}
\text{birth parameter}&3&4&5&6&\text{final total}\ \hline
\text{components}&5&9&28&90&132\\
\text{internal runs of length}<3&5&12&27&100&144.
\end{array}                                           \tag{4.2}
\]

Every one of the `5+12+27` earlier events is replayed literally in the
parameter-six forest; the final `100` are born at the last step.

The same replay gives new-`c` minimum internal run two at all three steps,
with length profiles

\[
 2^5,\qquad 2^8 3^7,\qquad 2^{19}3^{13}4^8 5^4,       \tag{4.3}
\]

and new-`z` minimum corridor length four at all three steps.  These are
finite measurements, not a propagation theorem.  In particular, the
frozen strict chain is not depth-two resident even though its component
topology is exact.

The canonical source-ear split gives the following literal side-residence
ledger; each last entry is `all = kernel + ear-prefix`:

\[
\begin{array}{c|c|r|r|r|c}
n&\text{shore}&e&\text{ears}&\text{kernel edges}&\text{bad windows}\\ \hline
3&\text{upper}&0&5&1&0=0+0\\
3&\text{lower}&0&5&1&0=0+0\\
4&\text{upper}&0&14&14&0=0+0\\
4&\text{lower}&1&15&13&0=0+0\\
5&\text{upper}&0&42&78&3=2+1\\
5&\text{lower}&2&44&76&8=4+4.
\end{array}                                           \tag{4.4}
\]

So the upper shores happen to stay on the rooted-tree face while the lower
defect is `0,1,2`.  Neither sequence is an invariant.  The independent
strict, nonchained fixture
`catalan_direct_edgewise_side_lift_n3_n5_20260731.witness.json` has
`e=3` on both shores at `n=5`; its upper/lower side ledgers are respectively
`0=0+0` and `5=2+3`.  This remains true despite facet slacks at least five,
so a positive facet-slack bound does not imply no-empty topology.

## 5. Coordinate-flux quotient

For an exact Catalan linear matching `F` at parameter `n`, let
`kappa_i(F)` count physical edges whose endpoints differ in coordinate
`i`.

### Lemma 5.1 (Catalan crossing load)

For every coordinate,

\[
 \kappa_i(F)=
 \binom{2n-1}{n}-\binom{2n-1}{n-2}
 =\operatorname {Cat}_n.                              \tag{5.1}
\]

#### Proof

An edge with lower and upper colours `L subset U` crosses `i` exactly when
`i in U\L`.  Because both colour palettes are bijective, the count is the
number of rank-`n+1` upper colours containing `i` minus the number of
rank-`n-1` lower colours containing `i`.  These are the two binomial terms
in (5.1), whose difference is the Catalan number. \(\square\)

For a child edge `q`, write

\[
 \sigma_q=t_q\mathbin\triangle h_q=\{a_q,b_q\},
 \qquad b_q\in h_q\setminus t_q.                      \tag{5.2}
\]

Let `m_q^-` and `m_q^+` be the numbers of selected upper and lower direct
occurrences with parent `q`, and put `r_q=1` when `q notin Q`.

### Theorem 5.2 (strict old-coordinate flux)

For every old coordinate `i`, every valid strict certificate satisfies

\[
\boxed{
 C=K+
 \sum_q(m_q^-+m_q^++r_q)\,[i\in\sigma_q]
 +2\sum_{q\in Q}[i=b_q].}
                                                               \tag{5.3}
\]

The two new coordinates each have crossing load exactly `C`.

#### Proof

The isolated child copy contributes `K` by Lemma 5.1.  A direct lift has
`x notin U_q`, so `x` is one on both lifted endpoints; a direct projection
has `x in L_q`, so `x` is zero on both projected endpoints.  In either
case its swap pair remains exactly `sigma_q`, giving the two `m` terms.
Each retained central edge also retains `sigma_q`.

For `q in Q`, orient the child edge from `t_q` to `h_q`.  The first seam in
(1.3) swaps `b_q` with `z`; the second swaps `b_q` with `c`.  Thus the two
seams contribute twice to old coordinate `b_q` and once to each new
coordinate.  Summing gives the right side of (5.3), and Lemma 5.1 applied
to the output makes it `C`.  Since `|Q|=C`, each new coordinate has load
`C`. \(\square\)

Equation (5.3) is a useful deterministic pre-quotient: the individual
lift coordinates `x` can be postponed while testing parent multiplicities,
`Q`, orientations, and aggregate residence boundary supply.  It remains
only a necessary projection.  The selected physical vertices, exact outer
palettes, side acyclicity, component order, and short-run locations still
depend on the actual `x` representatives.

### Theorem 5.3 (spectator-zipper normal form)

Every direct side path has an exact representation as a sequence

\[
 (q_1,x_1),(q_2,x_2),\ldots,(q_s,x_s)                 \tag{5.4}
\]

of parent edges with spectator labels.  Between two consecutive rows, let
`v` and `w` be the touching parent endpoints.

* On the upper side, if `x=y` then `v=w`; if `x!=y`, then

  \[
  w=(v-y)+x.                                           \tag{5.5}
  \]

* On the lower side, if `x=y` then `v=w`; if `x!=y`, then

  \[
  w=(v-x)+y.                                           \tag{5.6}
  \]

Thus equal consecutive spectators are identity joins, while unequal
spectators are one explicit virtual Johnson connector.  Conversely, a
parent-edge/spectator sequence satisfying the appropriate validity and
(5.5) or (5.6) lifts to one physical side path.

#### Proof

On the upper side the shared physical vertex satisfies
`v+x=w+y`, with `x` absent from `v` and `y` absent from `w`.  For `x=y`
cancellation gives `v=w`.  Otherwise the common set contains both labels,
so `y in v`, `x in w`, and (5.5) follows.  On the lower side the equality
is `v-x=w-y`, with the two labels present before deletion.  Cancellation
or restoring the two different labels gives (5.6).  Each implication is
reversible. \(\square\)

This is the strongest canonical pattern carried by the literal `x` data:
the lift coordinate is a spectator on each selected edge but a controlled
zipper label between consecutive edges.  The finite identity/swap connector
counts `(upper;lower)` are

\[
 n=3:(0/0;0/0),\quad
 n=4:(4/5;3/5),\quad
 n=5:(17/34;23/32).                                   \tag{5.7}
\]

No uniform choice of the spectator sequence is inferred from these counts.

## 6. What the finite chain does and does not canonize

Reconstructing the immediately preceding six sector classes gives:

\[
\begin{array}{c|rrrrrr}
 &0&0z&c&z&zcz&cz\\ \hline
n=4:\ |E|&6&14&15&1&14&6\\
n=4:\ |Q|&4&10&11&1&12&4\\
n=5:\ |E|&28&42&56&14&42&28\\
n=5:\ |Q|&19&21&37&8&29&18.
\end{array}                                           \tag{6.1}
\]

At `n=5`, every entry has `0<|Q intersection sector|<|sector|`.  Hence a
rule depending only on the preceding sector label is already incompatible
with this authenticated chain.

The conclusion survives the canonical source-ear refinement.  For the
`n=4 -> 5` transition, the exact `Q/total` counts are

\[
\begin{array}{c|rrrrrrrrr}
&c{:}Q&c{:}\bar Q&U_E&U_K&L_E&L_K&z&0z&zcz\\ \hline
|Q|/|E|&27/42&10/14&9/14&10/14&10/15&8/13&8/14&21/42&29/42.
\end{array}                                           \tag{6.2}
\]

Here `c:Q,c:bar Q` split copied-child provenance by membership in the
previous bank, `U_E,U_K,L_E,L_K` are source-ear/kernel classes on the two
shores, `z` is the punctured center, and `0z,zcz` are the two seam banks.
All nine cells are mixed.  Thus even the rooted source-ear state and one
generation of `Q` ancestry do not determine the next `Q`.

The chosen lift-coordinate classes are

\[
\begin{array}{c|rrr}
&\text{old}&c_{\rm previous}&z_{\rm previous}\\ \hline
n=4\text{ upper}&17&7&4\\
n=4\text{ lower}&16&5&7\\
n=5\text{ upper}&97&12&11\\
n=5\text{ lower}&90&16&14.
\end{array}                                           \tag{6.3}
\]

At `n=4` and `n=5`, both shores in fact use every available coordinate.
Thus no always-old, always-new, or reserved-coordinate lift-label recursion
is present.  The
contracted newborn graphs are paths, but their maximum numbers of trace
blocks are `7,12,20`; the witness gives no bounded-size rooted shape.  What
is canonical is the ancestral face, the birth level, root translation,
and the flux ledger—not the solver's particular `Q`, `x`, or newborn path
shape.

This noncanonicity is literal, not merely a histogram observation.  Apply a
coordinate reversal and reverse the order of the child components, with the
induced edge-id map.  Exact replay preserves every coordinate-free theorem
row above, while the raw `Q` symmetric differences are `2,22,94` at
`n=3,4,5` and the absolute lift-coordinate histograms change in every case.
Likewise, the unlabelled feature `(path order, unoriented distance from an
end)` is internally `Q`-mixed in `1/8,10/19,32/59` feature classes.  Raw
edge ids, numeric coordinates, and path shape alone are therefore not
inputs to an isomorphism-invariant deterministic rule.

There is one instructive `Q`/residence separation.  Relative to the old
short-run motifs, the three selected banks hit respectively

\[
 5/5,\qquad 17/17,\qquad 42/44.                        \tag{6.4}
\]

Even a perfect hit in the punctured central copy does not repair one old
motif globally, because Theorem 2.1 retains the untouched ancestral copy.
Thus a `Q`-hitting invariant is useful only for the newborn bank and cannot
serve as the recursive residence invariant by itself.

## 7. Independent audit

The standard-library consumer

```text
scratch/audit_catalan_derf_ancestral_face_flux_20260731.py
```

authenticates the frozen source payload and reconstructs every child atom,
direct occurrence, physical edge, path component, ancestral face, active
contraction, coordinate-flux row, nested birth cohort, and depth-two run
event.  It writes

```text
scratch/catalan_derf_ancestral_face_flux_20260731.audit.json
```

with status

```text
PASS_INDEPENDENT_DERF_ANCESTRAL_FACE_AND_FLUX
```

and canonical payload

```text
e3427f38a9bca95ae6cf015b91b9c8282d4fc0e4c87e846f925206e5d4934172
```

The independently written complementary consumer

```text
scratch/audit_catalan_derf_recursive_pattern_state_20260731.py
```

reconstructs the rooted-defect side kernel, alternating central quotient,
six-bank provenance, and the exact new-`c`/new-`z` residence motifs.  Its
output

```text
scratch/catalan_derf_recursive_pattern_state_20260731.audit.json
```

has status `PASS_INDEPENDENT_DERF_RECURSIVE_PATTERN_STATE` and canonical
payload

```text
90d74c7987304624cbb1cee9f151a42bddf3f74f59d41d442824c070f321283d
```

That consumer uses an independent lexicographic separating-ear
normalization for its quotient reconstruction.  A third consumer uses the
literal source-ear rule of Proposition 2.4, checks Corollary 2.5, transports
the chain through a coordinate/component isomorphism, and audits the
nonchained `e=3,3` counterfixture:

```text
scratch/audit_catalan_derf_recursive_pattern_referee_20260731.py
scratch/catalan_derf_recursive_pattern_referee_20260731.audit.json
```

Its status is `PASS_INDEPENDENT_DERF_PATTERN_REFEREE` and its canonical
payload is

```text
d9826468a634a61e5b23eec1a26b8a18c1ed35993d067045469122a35fb0548c
```

Frozen SHA-256 values at this audit are

```text
1fd49d57277a6bd7357816b5861ba370d26b4b863a570e35202c9801a0585c20  scratch/catalan_direct_edgewise_side_lift_recursive_n3_n5_20260731.witness.json
c162288ba634e4613bd27f39dd15ad825de07d85650f747744fea83d437b3454  scratch/audit_catalan_derf_ancestral_face_flux_20260731.py
26cfec09e8f3eb936169d0de7ce3efae9d4124fe433a30c3d8aa821050bab419  scratch/catalan_derf_ancestral_face_flux_20260731.audit.json
448db9915488c93e28e36f1837267e03f7e1220e69c8b82e981cffb8e6c7c27d  scratch/audit_catalan_derf_recursive_pattern_state_20260731.py
d0dfb14680b6272e64e4cc9e6fd74ceebecbff389a2c5e26c31a7010f7dc5f15  scratch/catalan_derf_recursive_pattern_state_20260731.audit.json
4e9300e8416014d04b371704e732b1f4991e7a8f10e33cddab5314e43087edfe  scratch/audit_catalan_derf_recursive_pattern_referee_20260731.py
c75cc0791053677711593831210f425cf5be219d50a4ddc0a4a79c4262803da2  scratch/catalan_derf_recursive_pattern_referee_20260731.audit.json
0cef794e33d0996bbd7d73168568e9c2613e3c06f12499751a685ac69fe554b3  scratch/catalan_direct_edgewise_side_lift_n3_n5_20260731.witness.json
```

The replay is exact only for the frozen `n=3,4,5` chain.  The ancestral
face, birth decomposition, graphic factorization, residence factorization,
and flux identities are proved for every strict DERF certificate.  No
all-`n` existence of the newborn certificate, joint palette matching,
resident birth bank, deep-shadow support, or compiler is claimed.
