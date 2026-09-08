# Lane R: root-scale \(H_r\)-conjugated leaf graph

Date: 2026-07-26

Method: pure mathematics only; no finite search, computation, or external
sources.

## 0. Exact outcome

For \(r\geq 1\), let \(\mathcal D_r\) be the Dyck words of length \(2r\),
with `1` an up-step and `0` a down-step, and put

\[
 H_r=\langle(2\ 3),(4\ 5),\ldots,(2r-2\ 2r-1)\rangle
     \cong (C_2)^{r-1}.
 \tag{0.1}
\]

Let \(G_r\) have vertex set \(\mathcal D_r\).  Its edges are all
\(H_r\)-translates of all contextual certified leaf-rotation edges

\[
                 C[1100R]\longleftrightarrow C[1010R].
 \tag{0.2}
\]

Thus the hypothesis throughout is that the context-closed edge family in
(0.2) is the leaf family being conjugated.  If the physically certified
library is a proper aligned subfamily, its graph is a subgraph of \(G_r\),
so the disconnection conclusion below remains valid, while the exact
component classification applies to the context-closed graph \(G_r\).

The root-scale conjugation does not give an all-rank Catalan conveyor.

### Theorem A (connectivity and complete components)

\[
 \boxed{G_r\text{ is connected if and only if }r\leq 3.}
 \tag{0.3}
\]

For every \(r\), the components have the following complete normal form.
Pair the coordinates

\[
                 (2,3),(4,5),\ldots,(2r-2,2r-1),
 \tag{0.4}
\]

and encode the pairs by

\[
             11\mapsto U,\qquad 00\mapsto D,
             \qquad 10\mapsto H_0,\qquad 01\mapsto H_1.
 \tag{0.5}
\]

After colours are omitted, this is a Motzkin excursion of length \(r-1\).
Replace every adjacent \(UD\) by \(HH\).  These replacements are disjoint
and create no new \(UD\), so they produce a unique peakless excursion
\(N\).

Call a level position of \(N\) **rigid** when it is isolated and

\[
 \bigl(\text{its preceding step is }D\bigr)
 \quad\text{or}\quad
 \bigl(\text{its following step is }U\bigr).
 \tag{0.6}
\]

The two boundary sentinels are compatible: the left sentinel is not
\(D\), and the right sentinel is not \(U\).  Two roots lie in the same
component of \(G_r\) if and only if they have the same peakless excursion
\(N\) and the same \(0/1\) colour at every rigid level position of \(N\).

If \(\rho(N)\) is the number of rigid positions and
\(c_r=|\pi_0(G_r)|\), then

\[
 \boxed{
 c_r=
 \sum_{\substack{N\text{ Motzkin excursion}\\
                  |N|=r-1,\ UD\not\subset N}}
       2^{\rho(N)}.}
 \tag{0.7}
\]

The ordinary generating function

\[
                   F(z)=\sum_{n\geq0}c_{n+1}z^n
 \tag{0.8}
\]

is the unique formal power series with constant term one satisfying

\[
 \boxed{
 F(z)=\frac1{1-z}+\frac{Q(z)^2A(z)}{1-Q(z)A(z)},
 \qquad
 A(z)=z^2(F(z)-1),
 \qquad
 Q(z)=1+2z+\frac{z^2}{1-z}.}
 \tag{0.9}
\]

Equivalently, with

\[
 P(z)=\frac z{1-z},
 \qquad
 \mathcal N(x,t)=
 \sum_{k\geq1}\sum_{p=1}^k
 \frac1k\binom{k}{p}\binom{k}{p-1}x^kt^p,
 \tag{0.10}
\]

one has the explicit Narayana form

\[
 \boxed{
 F(z)=\frac1{1-z}
       +Q(z)\mathcal N\!\left(z^2Q(z)^2,\frac{P(z)}{Q(z)}\right).}
 \tag{0.11}
\]

Here

\[
 \mathcal N(x,t)=
 \frac{1-x(1+t)-
 \sqrt{1-2x(1+t)+x^2(1-t)^2}}{2x}.
 \tag{0.12}
\]

The initial component counts are

\[
       c_1,c_2,c_3,c_4,c_5,c_6,c_7,\ldots
       =1,1,1,2,6,13,28,\ldots .
 \tag{0.13}
\]

Consequently the edge transpositions generate exactly

\[
 \boxed{
 \left\langle(x\ y):xy\in E(G_r)\right\rangle
   =\prod_{K\in\pi_0(G_r)}\operatorname{Sym}(K).}
 \tag{0.14}
\]

They generate \(\operatorname{Sym}(\mathcal D_r)\) exactly for
\(r\leq3\).

## 1. Decorated-Motzkin orbit dictionary

Every \(w\in\mathcal D_r\) has the form

\[
 w=1\,(b_1c_1)(b_2c_2)\cdots(b_nc_n)\,0,
 \qquad n=r-1.
 \tag{1.1}
\]

Set

\[
 d_i=b_i+c_i-1\in\{-1,0,1\}.
 \tag{1.2}
\]

Interpret \(1,0,-1\) as \(U,H,D\), respectively, retaining the colour
of a zero step according as \((b_i,c_i)=10\) or \(01\).

### Lemma 1.1 (exact orbit quotient)

The uncoloured word \(d_1\cdots d_n\) is a Motzkin excursion.  Conversely,
every two-coloured Motzkin excursion of length \(n\) gives one Dyck word by
(1.1).  Two Dyck words are in the same \(H_r\)-orbit if and only if their
uncoloured Motzkin excursions agree.  An excursion with \(f\) level steps
has an \(H_r\)-orbit of size \(2^f\).

#### Proof

Let \(q_i=\sum_{j=1}^id_j\).  Immediately after the initial `1` and the
first \(i\) pairs, the Dyck height is

\[
                             1+2q_i.
 \tag{1.3}
\]

It is a positive odd integer, so \(q_i\geq0\); immediately before the
terminal `0` it equals one, so \(q_n=0\).  Hence the pair-sum word is a
Motzkin excursion.

Conversely, at every pair boundary a Motzkin excursion gives height at
least one.  A \(D=00\) step starts only above Motzkin height zero, so its
two down-steps remain nonnegative.  A level pair `01` at Motzkin height
zero merely touches Dyck height zero after its first bit; all other cases
are immediate.  The final `0` returns height one to zero.  Thus both
orientations of every level step are Dyck.

The generators of \(H_r\) independently swap the two bits in each pair.
They fix `11` and `00` and interchange `10` and `01`, which proves all
orbit claims. \(\square\)

The use of these coordinate permutations on the exact factor is justified
by the problem's stated Chung--Feller-layer preservation premise.  The
orbit dictionary itself needs only the Dyck nonnegativity argument above.

## 2. Exact image of every conjugated leaf edge

Only the parity of the first coordinate of the local `1100` block matters.

### Lemma 2.1 (parity-exhaustive local moves)

Under (0.5), the edges of \(G_r\) are exactly the following decorated
Motzkin moves.

1. At an even start, for every \(a,b\in\{0,1\}\),

   \[
                         UD\longleftrightarrow H_aH_b.
   \tag{2.1}
   \]

2. At an odd start, the skeleton is fixed and one level colour toggles:

   \[
                         H_0\longleftrightarrow H_1.
   \tag{2.2}
   \]

   A toggle at position \(i\) exists exactly when

   \[
   H_i=H,\qquad
   (i=1\text{ or }M_{i-1}\neq D),\qquad
   (i=n\text{ or }M_{i+1}\neq U).
   \tag{2.3}
   \]

All colours outside the displayed positions may be prescribed arbitrarily
and are unchanged across the edge.

#### Proof

If the leaf block starts at coordinate \(2i\), its two complete pair
blocks are

\[
                       (11)(00)\longleftrightarrow(10)(10).
 \tag{2.4}
\]

This is \(UD\leftrightarrow HH\).  The two corresponding generators of
\(H_r\) fix the `11`,`00` endpoint and independently choose either colour
on each level step at the other endpoint.  Generators on all other level
pairs prescribe arbitrary common outside colours.  This proves (2.1).

If the leaf block starts at coordinate \(2i-1\), the two changed middle
bits form exactly pair \(i\), and

\[
                         1(10)0\longleftrightarrow1(01)0.
 \tag{2.5}
\]

The required preceding outer `1` can be placed in its prescribed
coordinate by a swap in pair \(i-1\) exactly when that pair contains a
`1`, equivalently when \(M_{i-1}\neq D\); the initial `1` handles
\(i=1\).  Similarly, the following outer `0` can be placed correctly
exactly when pair \(i+1\) contains a `0`, equivalently when
\(M_{i+1}\neq U\); the terminal `0` handles \(i=n\).  This proves the
necessity and sufficiency of (2.3), as well as (2.2).

Conversely, every occurrence \(UD\) supplies the literal block `1100`.
It is a Dyck subexcursion and hence a node-aligned instance of (0.2).
Conjugating independently in the displayed pairs realizes all four
right-hand colours.  For (2.2), the choices just described put the needed
outer `1` and `0` into the preimage leaf block.  Thus every listed move is
an \(H_r\)-translate of a leaf edge.  Odd and even starts exhaust all
possibilities. \(\square\)

## 3. The uncoloured peak-erasure normal form

Orient (2.1) by

\[
                              UD\longrightarrow HH.
 \tag{3.1}
\]

### Lemma 3.1 (one-sweep confluence)

Every Motzkin excursion has a unique normal form \(\nu(M)\), obtained by
simultaneously replacing all its adjacent \(UD\)'s by \(HH\).  Two
uncoloured excursions are joined by moves \(UD\leftrightarrow HH\) if and
only if their normal forms agree.

#### Proof

Two `UD` factors cannot overlap: the common letter would have to be both
`D` and `U`.  Replacing one by `HH` cannot create a new `UD` across either
boundary.  Hence all reductions commute and one sweep reaches a unique
\(UD\)-free result.  Both sides of every undirected move reduce to that
same result, so \(\nu\) is invariant.  Conversely, each excursion is
joined to its normal form by its reductions. \(\square\)

An occasionally useful strengthened observation is the following.

### Lemma 3.2 (all preimages of a normal skeleton)

If \(N\) is \(UD\)-free, then \(\nu(M)=N\) if and only if \(M\) is
obtained from \(N\) by replacing a collection of pairwise disjoint `HH`
factors by `UD`.

#### Proof

The reverse construction plainly reduces back to \(N\).  In the other
direction, the original `UD` factors of \(M\) are disjoint, no new factor
is created during reduction, and exactly their two positions become
`HH` in \(N\). \(\square\)

## 4. The surviving colours

Let \(N\) be \(UD\)-free.  A level step \(N_i=H\) is isolated when
neither existing neighbour is \(H\).  It is rigid precisely under (0.6).

By Lemma 3.2, an isolated level position of \(N\) remains a level position
in every \(M\) with \(\nu(M)=N\): it belongs to no `HH` factor available
for reversal.  Its colour is therefore well-defined throughout that
normal-form fibre.

### Lemma 4.1 (rigid colours are invariant)

If \(N=\nu(M)\) and position \(i\) is rigid in \(N\), the colour at
position \(i\) is constant on the component of \(M\) in \(G_r\).

#### Proof

An even-start move acts on two positions which are adjacent `HH` in
\(N\), so it cannot include an isolated position.  By Lemma 3.2, the
nonlevel neighbours of the rigid position in \(N\) are unchanged in every
preimage skeleton.  Condition (0.6) is exactly an obstruction to one of
the two inequalities in (2.3), so an odd-start colour toggle at that
position is impossible.  All other moves leave its pair coordinates
fixed. \(\square\)

### Lemma 4.2 (every nonrigid colour is flexible)

Fix a \(UD\)-free skeleton \(N\).  All decorations of \(N\) which agree
at its rigid positions lie in one component of \(G_r\).

#### Proof

Consider a maximal run of at least two level steps.  At every adjacent
pair, (2.1) gives

\[
 H_aH_b\longrightarrow UD\longrightarrow H_{a'}H_{b'}
 \tag{4.1}
\]

for arbitrary old and new colours.  In particular, either member of an
adjacent pair can be toggled while the other is restored, so the whole run
can be recoloured arbitrarily without changing outside positions.

Now let \(H_i\) be isolated and nonrigid.  Its previous step is not \(D\)
and its following step is not \(U\), with the boundary convention in
(2.3).  Hence (2.2) toggles it.  In a Motzkin excursion this is equivalently
the consecutive internal pattern \(UHD\), apart from the one-step
excursion \(H\), which is also togglable by the two sentinels.  Thus every
nonrigid colour is independently adjustable. \(\square\)

### Theorem 4.3 (complete normal form)

Two roots \(w,w'\in\mathcal D_r\) are joined in \(G_r\) if and only if

1. \(\nu(M(w))=\nu(M(w'))=:N\); and
2. their colours agree at every rigid position of \(N\).

#### Proof

Necessity follows from Lemmas 3.1 and 4.1.  For sufficiency, reduce both
skeletons to \(N\).  At every erased `UD`, (2.1) permits arbitrary colours
on the resulting adjacent level pair.  Rigid positions are isolated and
therefore are not touched by these reductions.  Lemma 4.2 then removes all
remaining colour differences. \(\square\)

This theorem gives (0.7) immediately: each \(UD\)-free skeleton supports
one component for every binary assignment to its rigid positions.

## 5. Exact connectivity threshold and generated group

For \(r=1\), the graph has one vertex.  For \(r=2\), its two roots are the
two colours of the one-step excursion \(H\), joined by (2.2).  For
\(r=3\), the possible uncoloured excursions are \(HH\) and \(UD\); both
reduce to \(HH\), and a two-step level run has no rigid colour.  Hence
\(G_r\) is connected for \(r\leq3\).

For \(r\geq4\), put \(n=r-1\geq3\).  The two excursions

\[
                              H^n,\qquad UH^{n-2}D
 \tag{5.1}
\]

are valid, \(UD\)-free, and distinct.  They are therefore in different
components by Theorem 4.3.  This proves (0.3).

For any finite graph, its edge transpositions generate the full symmetric
group on each connected component: along a path, conjugating consecutive
edge transpositions produces the transposition of either endpoint with
the initial vertex, and these star transpositions generate the component's
full symmetric group.  No edge transposition crosses a component.  This
proves (0.14).

## 6. Recursive component generating function

This section proves (0.9) without an appeal to coefficient extraction.

Use the complete normal form of Theorem 4.3 and reset every flexible level
colour to zero.  In a non-all-level peakless excursion, the top-level
decomposition is a nonempty sequence of primitive excursions

\[
                         U\,P\,D,
 \tag{6.1}
\]

separated and surrounded by top-level level runs.

A top-level gap has the following component weights:

* an empty gap has weight \(1\);
* a singleton level has weight \(2z\), because at a boundary it is next
  to \(U\), at the other boundary it is preceded by \(D\), and between
  primitives it is both preceded by \(D\) and followed by \(U\); hence
  it is rigid;
* a run of length at least two has one colour component and weight
  \(z^2/(1-z)\).

Thus its generating series is

\[
                         Q(z)=1+2z+\frac{z^2}{1-z}.
 \tag{6.2}
\]

In (6.1), \(P\) must be nonempty, since \(UD\) is forbidden.  The outer
\(U,D\) contribute \(z^2\), and their boundary effects on \(P\) are
exactly the compatible sentinels used in Theorem 4.3: the preceding
\(U\) is not \(D\), and the following \(D\) is not \(U\).  Therefore a
primitive has series

\[
                         A(z)=z^2(F(z)-1).
 \tag{6.3}
\]

All-level paths, including the empty path, contribute \(1/(1-z)\).  Paths
with exactly \(k\geq1\) primitives contribute \(Q^{k+1}A^k\).  Summing
over \(k\) gives

\[
 F(z)=\frac1{1-z}+\sum_{k\geq1}Q(z)^{k+1}A(z)^k
     =\frac1{1-z}+\frac{Q(z)^2A(z)}{1-Q(z)A(z)},
 \tag{6.4}
\]

which is (0.9).  Since the right-hand occurrence of \(F-1\) is multiplied
by \(z^2\), coefficient recursion determines a unique formal solution
with constant term one.

## 7. Narayana form and independent generating-function audit

Delete all level steps from a non-all-level peakless normal excursion.
The result is a nonempty Dyck path of some semilength \(k\).  Suppose it
has \(p\) peaks.  Reinsert level runs in the \(2k+1\) gaps before, between,
and after its nonlevel steps.

At either boundary, or at any internal gap other than a peak gap, the
allowed component series is \(Q(z)\): the gap may be empty; a singleton is
rigid and has two colours; and a longer run has one flexible colour
component.  At each of the \(p\) peak gaps, the gap must be nonempty to
avoid an adjacent \(UD\).  Its series is

\[
                         P(z)=z+\frac{z^2}{1-z}
                             =\frac z{1-z}.
 \tag{7.1}
\]

A Dyck path of semilength \(k\) with \(p\) peaks therefore contributes

\[
 z^{2k}Q(z)^{2k+1-p}P(z)^p
 =Q(z)\,[z^2Q(z)^2]^k[P(z)/Q(z)]^p.
 \tag{7.2}
\]

The number of such Dyck paths is the Narayana number

\[
                         \frac1k\binom{k}{p}\binom{k}{p-1}.
 \tag{7.3}
\]

Summing (7.2) over \(k,p\), and adding the all-level contribution
\(1/(1-z)\), proves (0.11).

For a direct algebraic audit of the equivalence between (0.9) and (0.11),
put

\[
 x=z^2Q^2,\qquad t=P/Q,\qquad
 Y=\frac{F-1/(1-z)}{Q}.
 \tag{7.4}
\]

Equation (0.9) gives

\[
              \frac{Y}{1+Y}=QA=z^2Q(P+QY)=x(t+Y),
 \tag{7.5}
\]

or

\[
                         Y=x(1+Y)(t+Y).
 \tag{7.6}
\]

The unique solution with zero constant term is exactly
\(Y=\mathcal N(x,t)\), whose quadratic solution is (0.12).  This proves
that the two enumerations agree coefficient by coefficient.

Expanding only by the formal recurrence gives

\[
 F(z)=1+z+z^2+2z^3+6z^4+13z^5+28z^6+O(z^7),
 \tag{7.7}
\]

which proves (0.13) with the indexing in (0.8).  If components are indexed
directly by semilength, their ordinary series is \(zF(z)\).

## 8. Decisive-step audit and exact scope

The proof has four possible failure points; each is closed above.

1. **Missing conjugated moves.**  Lemma 2.1 is parity-exhaustive and proves
   both directions: every graph edge has one of the two displayed forms,
   and every displayed move has an actual leaf-edge preimage under
   \(H_r\).
2. **A hidden peak created during reduction.**  An `HH` replacement has
   neither a terminal \(U\) nor an initial \(D\), so it cannot create a
   cross-boundary `UD`.  Lemmas 3.1--3.2 therefore give a literal,
   one-sweep normal form.
3. **A supposedly rigid colour becoming movable in a nonnormal
   representative.**  Lemma 3.2 shows that an isolated normal-form level
   and its nonlevel neighbours occur unchanged in every representative.
   Hence the failed toggle inequality remains failed, and no reverse
   two-level move can touch the position.
4. **Overcounting colour components in the generating function.**  A
   singleton gap has weight two exactly when it is rigid.  Singleton peak
   gaps are \(UHD\) and have weight one; all other singleton insertion
   gaps have a preceding \(D\) or following \(U\) and have weight two.
   This is why \(P(z)\), not \(Q(z)\), occurs at peak gaps.  The recursive
   and Narayana derivations independently yield the same algebraic series.

Therefore the negative conclusion is exact for the graph stated in the
problem: root-scale \(H_r\) conjugation merges all old leaf components at
semilength three but fails from semilength four onward.  The complete
obstruction is not merely the uncoloured peakless skeleton; it also
retains the colours of precisely the rigid isolated level positions.

No claim is made here that a larger nonleaf associator packet preserves
this invariant.  Indeed, any successful all-rank conveyor must add a
literal exact-factor trade that changes the peak-erasure skeleton or a
rigid colour, or must couple these components by a different exact
port-factor mechanism.
