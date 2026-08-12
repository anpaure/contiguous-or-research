# A Catalan-size long alternating braid from Mütze--Weber to MSW

## 1. Outcome

Let

\[
 n\ge2,\qquad C_n=\operatorname {Cat}_n.
\]

In the middle layer `Q_(2n)(n,n+1)`, let

* `H_0` be the all-zero Mütze--Weber dangling-path factor; and
* `H_CF` be the canonical Mütze--Standke--Wiechert Chung--Feller factor,
  with one geodesic path `P(w)` from each Dyck root `w` to `bar(w)`.

The edge symmetric difference is large, but its *topological complexity* is
only Catalan.

### Theorem 1 (three crossings per root)

Every canonical path `P(w)` has exactly three edges in common with `H_0`.
Consequently

\[
 \boxed{|H_0\cap H_{CF}|=3C_n},
 \qquad
 \boxed{|H_0\triangle H_{CF}|=2(2n-3)C_n}.            \tag{1.1}
\]

### Theorem 2 (Catalan alternating decomposition)

The signed difference `H_0 triangle H_CF` is the edge-disjoint union of at
most

\[
                              4C_n                     \tag{1.2}
\]

alternating trails and alternating circuits.  At most `C_n` of them are
open trails; the others are circuits.  Equivalently, the canonical
antipodal factor is reachable from the published factor by a Catalan-size
family of *long* signed-`T`-join pieces.

This corrects the interpretation of the super-Catalan edge-support bound.
The canonical target is not a sparse-edge refinement, but it remains a
sparse-*component* refinement.  It is therefore still viable for a
long-segment braid, provided the pieces have acceptable two-copy provenance
and can be scheduled without creating forbidden intermediate components.

## 2. The two matchings of the MW factor

Let

\[
 R_n=\operatorname {rev}(LM_{2n}(n,n+1))              \tag{2.1}
\]

be the middle matching of the reversed Greene--Kleitman SCD.  The
Mütze--Weber relation-to-lexicographic-matchings theorem gives

\[
                         R_n\subseteq H_0.             \tag{2.2}
\]

Along every dangling path, the edges alternate between `R_n` and the
complementary matching

\[
                         K_n=H_0\setminus R_n.         \tag{2.3}
\]

The first edge of every oriented MW path lies in `K_n`.  Both matchings
saturate the upper rank; `R_n` leaves the first lower endpoints unmatched,
whereas `K_n` leaves the last lower endpoints unmatched.

For `w in D_n`, write the first-return decomposition

\[
                         w=1u0v,
 \qquad \mu(u)=\overline{\operatorname {rev}(u)}.      \tag{2.4}
\]

Number the `2n` edges of `P(w)` from zero.

## 3. Exact crossing recurrences

Define `a(w)` for every nonempty Dyck word recursively by

\[
\begin{aligned}
 a(10v)&=1,\\
 a(1u0v)&=1+a(\mu(u))\qquad(u\ne\epsilon).
\end{aligned}                                         \tag{3.1}
\]

For semilength at least two, define `b(w)` by

\[
\begin{aligned}
 b(10v)&=2+a(v) &&(v\ne\epsilon),\\
 b(1100v)&=3,\\
 b(1u0v)&=1+b(\mu(u)) &&(|u|\ge4).
\end{aligned}                                         \tag{3.2}
\]

The cases in (3.2) are disjoint and exhaustive.  They also show inductively

\[
                         0<a(w)<b(w)<2n.              \tag{3.3}
\]

### Lemma 3 (crossing classification)

For every `w in D_n`, `n>=2`,

\[
 E(P(w))\cap R_n=\{e_{a(w)}\},
 \qquad
 E(P(w))\cap K_n=\{e_0,e_{b(w)}\}.                  \tag{3.4}
\]

### Proof

The reversed-GK matching has the following stack test.  Match `10` pairs in
the lower word, through already matched blocks.  An upward edge flipping
coordinate `q` lies in `R_n` exactly when the corresponding coordinate in
the reversed lower word is the first unmatched zero.

The MSW flip-coordinate recursion is

\[
 \rho(1u0v)=
 (d,\ d-\rho(\mu(u)),\ 1,\ d+\rho(v)),
 \qquad d=|u|+2.                                      \tag{3.5}
\]

Substituting (3.5) into the stack test gives the exact `R` table:

* if `u` is empty, only the coordinate-`1` edge, at index one, passes;
* if `u` is nonempty, the only passing edge is the mirrored copy of the
  unique passing edge of `P(mu(u))`, shifted by one position.

This is precisely recurrence (3.1).  It proves the first equality in
(3.4) by induction, starting with the path of `10`.

For `K_n`, use the all-zero MW induction simultaneously with (3.5).  The
four flip blocks give the following exhaustive table.

\[
\begin{array}{c|c|c}
\text{first-return case}&\text{initial }K\text{ edge}
                         &\text{second }K\text{ edge}\\ \hline
 w=10v,\ v\ne\epsilon&e_0&
       \text{the }R\text{ edge of }P(v),\text{ shifted by }2\\
 w=1100v&e_0&e_3\\
 w=1u0v,\ |u|\ge4&e_0&
       \text{the second }K\text{ edge of }P(\mu(u)),
       \text{ shifted by }1.
\end{array}                                           \tag{3.6}
\]

Here the first column is the explicit first edge `F(P)S(P)` of the MW
dangling path.  In the second column, (3.6) follows directly from the three
terms of `(ind-step2-P)`: the empty-inner case enters the suffix copy in the
opposite matching phase, the minimal inner word `10` is the central splice,
and every larger inner word stays in the mirrored old central copy.  The
outer, separator, and unused suffix blocks have the wrong appended-bit
sector and contribute no additional `K` edge.  Deleting the fixed outer
tags leaves respectively the `R(v)` or `K(mu(u))` membership test literally
unchanged.

The three rows of (3.6) are exactly recurrence (3.2).  The induction basis
`n=2` consists of roots `1100` and `1010`, with second indices three in
both cases.  Thus the second equality in (3.4) follows.  The two recurrences
also prove (3.3).  \(\square\)

The proof uses the actual Mütze--Weber recursion.  It does not identify it
with the later Mütze--Nummenpalo transition code.

## 4. Proof of Theorem 1

Lemma 3 gives three distinct common edges on each of the `C_n` edge-disjoint
MSW paths, proving the first identity in (1.1).

Both factors have `C_n` components and partition both middle ranks, so

\[
 |H_0|=|H_{CF}|
 ={2n\choose n}+{2n\choose n+1}-C_n
 =2nC_n.                                               \tag{4.1}
\]

Therefore

\[
 |H_0\triangle H_{CF}|
 =2(2nC_n-3C_n)=2(2n-3)C_n,                           \tag{4.2}
\]

which completes the proof.  \(\square\)

## 5. Only Catalan-many support components

Colour edges of `H_0 minus H_CF` red and edges of
`H_CF minus H_0` blue.  On every MSW path, the common edges have indices

\[
                         0<a(w)<b(w).                 \tag{5.1}
\]

Removing them leaves at most three nonempty blue path segments.  Hence the
blue subgraph has at most

\[
                              3C_n                     \tag{5.2}
\]

connected components.

At every upper vertex, both original factors have degree two.  Consequently

\[
                         d_{red}(z)=d_{blue}(z)        \tag{5.3}
\]

for every upper vertex `z`.  In particular, every red edge has an upper
endpoint incident with a blue edge.  Every connected component of the full
red-blue support therefore contains a blue component.  Adding red edges can
only merge blue components, so

\[
 \boxed{\#\operatorname{comp}(H_0\triangle H_{CF})\le3C_n.}     \tag{5.4}
\]

## 6. Directed alternating Euler decomposition

Orient every red edge from the lower rank to the upper rank, and every blue
edge from the upper rank to the lower rank.  At every upper vertex indegree
equals outdegree by (5.3).  At a lower vertex the difference is zero unless
that vertex is an endpoint of exactly one factor, in which case it is
`+1` or `-1`.

The two factors have `2C_n` endpoints each and share all `C_n` Dyck-root
first endpoints.  Hence their endpoint symmetric difference has at most

\[
                              2C_n                     \tag{6.1}
\]

vertices.  There are therefore at most `C_n` sources and the same number
of sinks.

Apply the standard directed Euler decomposition separately in every weak
component:

* a component with `s>0` sources is the edge-disjoint union of `s` directed
  Euler trails, obtained by adjoining `s` dummy sink-to-source arcs, taking
  one Euler circuit, and deleting the dummy arcs;
* a balanced component is one directed Euler circuit.

The orientations alternate red and blue automatically.  Combining (5.4)
and (6.1), the total number of pieces is at most

\[
 {1\over2}|T(H_0)\triangle T(H_{CF})|
 +\#\operatorname{comp}(H_0\triangle H_{CF})
 \le C_n+3C_n=4C_n.                                  \tag{6.2}
\]

This proves Theorem 2.  \(\square\)

## 7. What this proves, and what it does not

The full collection of pieces in Theorem 2 is an exact integral signed
`T`-join.  Toggling all of them gives `H_CF`, whose endpoint pairs are
complementary and whose augmented cycles contain exactly one antipodal edge.
Thus there is no Catalan *component-count* obstruction.

There is also an immediate factor-segment ledger.  Cutting the `C_n` MW
paths at all `3C_n` common edges leaves at most `4C_n` maximal red path
sections.  On the MSW side, the first common edge is always edge zero, so
the other two cuts leave at most three nonempty blue sections per root,
hence at most `3C_n` blue sections.  Therefore the simultaneous replacement
has at most

\[
                         7C_n                           \tag{7.1}
\]

maximal monochromatic factor sections.  This is a stronger provenance
count than the raw `Theta(nC_n)` edge support, although it is not yet a
fixed-coordinate shadow-provenance theorem.

Three additional statements are still required before this becomes the
desired OR lift.

1. **Dynamic legality.**  Toggling the pieces sequentially preserves the
   degree equations, but an intermediate factor may contain closed
   components or paths with the wrong endpoint pairing.
2. **Fixed-coordinate provenance.**  The total number of old/new factor
   sections is `O(C_n)`, but an MSW blue section inherits its parent after
   deleting a path-dependent ECO coordinate pair.  Targetwise old masks do
   not yet land in a bounded number of common coordinate sections.
3. **Recursive coordinate control.**  The canonical MSW factor uses
   path-dependent ECO insertion coordinates.  The long braid must still
   be shown to transport old shadow targets into a bounded number of common
   coordinate sections.

The correct next object is therefore the explicit directed support graph in
Section 6 together with the ECO coordinate-deletion labels, not a sparse-edge
`T`-join and not a loose tree of isolated alpha switches.  Euler transition
pairing controls endpoint trails, while the section ledger (7.1) controls
topological cuts; these should not be conflated.  The remaining theorem must
globalize the locally varying deleted coordinate pair on the blue sections.

## 8. Verification

`mw_msw_difference_probe.cpp` independently constructs both published
factors and checks the two crossing recurrences root by root.  Remote runs
through semilength eight verify every identity above; larger aggregate runs
through semilength eleven verify (1.1).  These computations are checks of
the symbolic recurrences, not the basis of the proof.

## 9. A fixed top-level sector-local Euler refinement

The degree-four transition pairing need not be chosen recursively merely to
control the two new coordinate sectors.  Sector changes can be charged to
physical tag-flipping edges, independently of the Euler pairing.

Consider the MW induction from `2n-2` to `2n` coordinates, and use the final
two coordinates as fixed tags.

### Lemma 4 (tag-edge ledger)

The all-zero MW factor `H_0` has at most

\[
                         3C_{n-1}                     \tag{9.1}
\]

edges which flip one of the final two tags.  The canonical factor `H_CF`
has exactly

\[
                         2C_n                         \tag{9.2}
\]

such edges.

### Proof

In the MW central recursion, the two literal old-family copies have constant
tags.  In the mixed family, `M^S` contributes one final-coordinate edge per
old central path, hence `C_(n-1)` edges.  The cut odd 2-factor contains the
`M^{FL}` edges at the first and last endpoint of every old central path,
hence `2C_(n-1)` first-new-coordinate edges.  There are no other tag edges,
which proves (9.1).

Every MSW path flips every one of the `2n` coordinates exactly once.  There
are `C_n` paths, so each of the two fixed tags contributes exactly `C_n`
edges, proving (9.2).  \(\square\)

### Theorem 5 (sector-local Catalan decomposition)

There is an alternating decomposition of `H_0 triangle H_CF` into
`O(C_n)` pieces such that every piece either

1. lies wholly in one of the four fixed two-bit sectors; or
2. consists of one tag-flipping edge.

An explicit bound is

\[
 4C_n+2(2C_n+3C_{n-1})\le11C_n.                       \tag{9.3}
\]

### Proof

Start with the at-most-`4C_n` directed Euler trails/circuits from Theorem 2.
As a trail moves from one fixed tag sector to another, at least one of its
two incident factor edges flips a tag.  Cut every trail immediately before
and after every tag-flipping edge.  The crossing edge becomes a one-edge
alternating trail, and every remaining subtrail has constant tags.

By Lemma 4 there are at most `2C_n+3C_(n-1)` possible crossing edges.  Two
cuts per edge give (9.3).  Splitting a directed alternating trail preserves
alternation, so the resulting pieces still form an edge-disjoint signed
decomposition.  \(\square\)

The theorem gives exactly the requested `O(C_n)` top-level provenance cuts,
for **any** Euler transition pairing at degree-four vertices.  It does not
yet prove old-target inheritance inside an MSW constant-tag piece: deleting
the fixed final pair need not turn that piece into a segment of one old MSW
path, because the ECO-inserted coordinate pair is path-dependent.  Thus
recursive transition pairing is not the top-level bottleneck; the surviving
gate is coordinate-consistent projection within the blue constant-tag
pieces.

## 10. Pure cut-and-reconnect provenance is impossible

The sector-local theorem must not be mistaken for ordinary seam-halo
inheritance.

### Proposition 6 (bulk-transition no-go)

Any transformation which obtains its new paths only by cutting old MW paths
at `s` places and reconnecting the resulting old path segments preserves all
but at most `s` old internal edges.  Therefore obtaining `H_CF` from `H_0`
in this manner requires at least

\[
                         (2n-3)C_n                    \tag{10.1}
\]

cuts.

### Proof

Every old edge not selected as a cut remains internal to one retained path
segment and therefore remains in the new factor.  Theorem 1 gives

\[
 |H_0\setminus H_{CF}|=2nC_n-3C_n=(2n-3)C_n.          \tag{10.2}
\]

Every one of these edges must consequently be a cut in a literal
cut-and-reconnect construction.  \(\square\)

Thus the `O(C_n)` long alternating pieces are not retained old segments:
they replace `Theta(nC_n)` adjacent transitions in bulk.  To be useful for
shadow inheritance, every long blue section needs a nontrivial certified
map carrying its internal windows to old windows.  Without such a map,
`O(C_n)` topological sections do not imply an `O(HC_n)` halo bound.  The
path-dependent ECO deletion is the available local map; globalizing it over
the fixed-coordinate sectors is now the exact missing theorem.
