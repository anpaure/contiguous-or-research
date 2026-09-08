# Ternary-carry factors: the exact macrocell run obstruction to labelled shadows

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The phase-dense ternary-carry factor solves owner grouping and seam length,
but its canonical first-\(t\)-eligible-block quotient does **not** cover
all but \(o(W)\) signed targets.

The obstruction is already combinatorial and is independent of the
base-three voltage calculation.  In one eight-block let

\[
 \mathcal V
 =\left\{
 X\cup Y:
 X\in\binom{\{a,b,c,d\}}2,\quad
 Y\in\{uw,ux,vw,vx\}
 \right\},
 \qquad |\mathcal V|=24.
\tag{0.1}
\]

An untouched selected block of a lower target has a local four-set in
\(\mathcal V\).  A touched block has the intersection of two adjacent
\(\mathcal V\)-owners.  Even after allowing **every** possible local
pair frame, there are only

\[
 |\mathcal C^-|=40
\tag{0.2}
\]

such local three-sets.  The upper union family \(\mathcal C^+\) also has
size \(40\).

For a uniform random target, one block is therefore

\[
 E\text{-type with probability }{24\over256}={3\over32},
 \qquad
 C\text{-type with probability }{40\over256}={5\over32}.
\tag{0.3}
\]

After neutral blocks are suppressed, the \(C\)-probability is exactly
\(5/8\).

Every depth-\(q\) carry window touches \(q\) cyclically consecutive members
of the owner's first \(t\) eligible blocks.  Hence every covered target
must contain either

* one \(C\)-run of length at least \(q\), or
* two boundary \(C\)-runs whose lengths sum to at least \(q\).

This gives the following uniform bound.  If \(N_q=\binom{2m}{m-q}\), then
for either sign the number of rank-\((m\pm q)\) targets coverable by
**any collection of carry factors using one fixed eight-block partition
and the same first-\(t\) macrocell rule** is at most

\[
 \boxed{
 \varepsilon_{m,q}N_q,\qquad
 \varepsilon_{m,q}
 \le C m^{5/2}(q+1)
       \exp\!\left({2q^2\over m}\right)
       \left({5\over8}\right)^q.}
\tag{0.4}
\]

The exponentially small bad-owner leave adds only \(o(W)\).

Consequently, whenever

\[
 {q\over\log m}\to\infty,
 \qquad
 q=O(\sqrt{m\log m}),
\]

\[
 M_q^-+M_q^+
 \ge (2-o(1))N_q.
\tag{0.5}
\]

In particular, at \(q=A\sqrt m\) with fixed \(A>0\),
\(N_q=(e^{-A^2}+o(1))W\), and the forced flags miss a positive fraction
of all signed targets:

\[
 \boxed{M_q^-+M_q^+\ge
 (2e^{-A^2}-o(1))W.}
\tag{0.6}
\]

Thus the required sum of holes is not \(o(W)\).

Changing only shores, ternary phases, carry predicates, Hamming translates,
or component choices inside the same canonical macrocell atlas cannot
help: (0.4) used the union of all locally possible frames already.
The atlas itself must change.

If \(R\) factors use \(R\) different coordinate blockings or macrocell
atlases, a union bound gives coverable fraction at most
\(R\varepsilon_{m,q}\).  Therefore positive-density coverage at depth
\(q\) requires

\[
 \boxed{
 R\ge
 {1\over C m^{5/2}(q+1)}
 \exp\!\left(-{2q^2\over m}\right)
 \left({8\over5}\right)^q.}
\tag{0.7}
\]

For \(q=A\sqrt m\),

\[
 \boxed{
 R\ge
 \exp\!\left((A\log(8/5)+o(1))\sqrt m\right).}
\tag{0.8}
\]

This is still \(W^{o(1)}\), but it is exponentially larger than a bounded
or polynomial menu.  It is a necessary count, not a sufficiency theorem.

Finally, whole-component selection does not turn aggregate factor
histograms into Hall loads.  For two factors, the exact component-overlap
graph shows that every connected overlap component has only the two
monochromatic choices.  Thus fine target correction requires many
overlap components with the correct signed incidence vectors, or a new
multi-factor absorption theorem.  Neither follows from the ternary carry.

## 1. The local admissible target alphabets

Separate the eight coordinates into the special shore

\[
 A=\{a,b,c,d\}
\]

and the reservoir shore

\[
 R=\{u,v,w,x\}.
\]

Every member of \(\mathcal V\) has exactly two special coordinates and
two reservoir coordinates, the latter consisting of one member of
\(\{u,v\}\) and one member of \(\{w,x\}\).

Let

\[
 \mathcal C^-
 =\{X\cap X':
 X,X'\in\mathcal V,\ |X\triangle X'|=2\}.
\tag{1.1}
\]

This is an upper envelope for the lower shadows of every possible physical
pair-frame edge whose endpoints stay in \(\mathcal V\).  It may be larger
than the shadow alphabet of one particular carry factor, which only
strengthens the obstruction below.

### Lemma 1.1 (exact local alphabet)

\[
 |\mathcal C^-|=40.
\tag{1.2}
\]

More precisely,

\[
 \mathcal C^-
 =
 \left\{
 \{a_0\}\cup Y:
 a_0\in A,\ Y\in\{uw,ux,vw,vx\}
 \right\}
\tag{1.3}
\]

disjointly unioned with

\[
 \left\{
 X\cup\{r_0\}:
 X\in\binom A2,\ r_0\in R
 \right\}.
\tag{1.4}
\]

#### Proof

Two \(\mathcal V\)-members at symmetric-difference two exchange one
coordinate.  Since both have special/reservoir count \((2,2)\), the
exchange occurs within one shore.

If the special coordinate changes, the reservoir orientation is fixed.
The intersection has one special coordinate and one of the four reservoir
orientations, giving \(4\cdot4=16\) sets in (1.3).

If the reservoir coordinate changes, the special two-set is fixed.  The
intersection has that special pair and one arbitrary reservoir coordinate,
giving \(6\cdot4=24\) sets in (1.4).  The two displayed families have
different shore counts and are disjoint. \(\square\)

Let

\[
 \mathcal C^+
 =\{X\cup X':
 X,X'\in\mathcal V,\ |X\triangle X'|=2\}.
\tag{1.5}
\]

Complementation inside the eight-block preserves \(\mathcal V\) and sends
intersections to complements of unions.  Hence

\[
 |\mathcal C^+|=40.
\tag{1.6}
\]

The eligibility alphabet is

\[
 \mathcal E=\mathcal V,\qquad|\mathcal E|=24.
\tag{1.7}
\]

The three alphabets have different local ranks:
\(\mathcal C^-\) consists of three-sets, \(\mathcal E\) of four-sets,
and \(\mathcal C^+\) of five-sets.

## 2. The deterministic run lemma

Partition all but at most seven ground coordinates into an ordered list
of eight-blocks.  For an owner \(X\), call a block eligible when its local
restriction lies in \(\mathcal E\).  A good owner has at least \(t\)
eligible blocks; its canonical macrocell uses the first \(t\).

The only properties of the ternary-carry factor used below are:

1. every transition changes one selected block between two local owners
   in \(\mathcal V\);
2. every \(q\le t\) consecutive transitions touch \(q\) distinct,
   cyclically consecutive selected blocks.

These are exactly the local-support and \(H\)-geodesicity properties of
the carry construction.

For a lower target \(T\), mark a block \(E\) when its local restriction
lies in \(\mathcal E\), mark it \(C\) when it lies in
\(\mathcal C^-\), and otherwise mark it neutral.  Suppress neutral blocks.
Use \(\mathcal C^+\) for an upper target.

### Lemma 2.1 (macrocell run condition)

If a signed depth-\(q\) target is produced by a carry-factor window from
a good owner, its suppressed \(E/C\) word contains either

1. one run of at least \(q\) consecutive \(C\)'s; or
2. two \(C\)-runs whose total length is at least \(q\).

#### Proof

Let

\[
 B_1<\cdots<B_t
\]

be the starting owner's first \(t\) eligible blocks.  On a nonwrapping
window, the \(q\) touched blocks form one consecutive interval among the
\(B_i\)'s.  In the target, each touched local owner edge becomes a member
of \(\mathcal C^\pm\), while every untouched selected block remains a
member of \(\mathcal E\).

Between two successive touched \(B_i\)'s there can be no \(E\)-block of
the target.  Such a block is unchanged from the owner, would be eligible
there, and would therefore occur between them in the ordered eligible
list.  Neutral blocks and additional unchosen \(C\)-blocks do not break
a \(C\)-run.  Hence the target contains one \(C\)-run of length at least
\(q\).

If the cyclic window wraps from \(B_t\) to \(B_1\), split it into its
terminal and initial pieces.  The same argument puts each piece inside a
\(C\)-run.  Their lengths sum to \(q\). \(\square\)

Notice that the lemma uses the maximal alphabets (1.1) and (1.5).
Changing the local pair frame, shore, or carry state cannot evade it.

Equivalently, let \(r_1^\pm(T)\ge r_2^\pm(T)\) be the two largest
\(C\)-run lengths in the appropriate suppressed word, and let
\(d_{\mathfrak A,q}^\pm(T)\) be the total multiplicity of \(T\) across
all frame-labelled carry factors built on this fixed atlas.  Then the
macrocell quotient gives the exact support statement

\[
 \boxed{
 r_1^\pm(T)+r_2^\pm(T)<q
 \quad\Longrightarrow\quad
 d_{\mathfrak A,q}^\pm(T)=0.}
\tag{2.1}
\]

Thus the obstruction concerns zero target multiplicity across different
canonical macrocells, not merely duplicate occurrences within one
macrocell.

## 3. Probability of the run event

First expose a Bernoulli-\(1/2\) subset of the \(2m\) coordinates.  On
each complete eight-block the local subset is uniform among its \(256\)
possibilities.  Therefore, for either sign,

\[
 p_E={24\over256}={3\over32},
 \qquad
 p_C={40\over256}={5\over32}.
\tag{3.1}
\]

After neutral blocks are suppressed, the remaining letters are independent
and

\[
 \Pr(C\mid E\text{ or }C)={p_C\over p_E+p_C}={5\over8}.
\tag{3.2}
\]

Let \(n\le m/4\) be the number of complete blocks.

### Lemma 3.1 (two-run probability)

Under the product measure, the probability that the suppressed word has
two \(C\)-runs whose total length is at least \(q\) is at most

\[
 n^2(q+1)\left({5\over8}\right)^q.
\tag{3.3}
\]

#### Proof

Choose the starts of the two runs and split \(q=a+(q-a)\), with
\(0\le a\le q\).  For a prescribed choice, at least \(q\) specified
successive nonneutral letters must be \(C\), with probability
\((5/8)^q\).  There are at most \(n^2(q+1)\) choices.  The case of one
run is included by taking one part empty.  A union bound proves (3.3).
\(\square\)

Now condition the Bernoulli subset to have rank \(m-q\).  Its conditioning
probability is

\[
 {N_q\over4^m}.
\tag{3.4}
\]

Uniformly for \(q=O(\sqrt{m\log m})\), Stirling's formula gives

\[
 {N_q\over4^m}
 \ge c m^{-1/2}\exp\!\left(-{2q^2\over m}\right)
\tag{3.5}
\]

after weakening the Gaussian constant.  Dividing (3.3) by (3.5) and using
\(n\le m/4\) proves (0.4).  Complementation proves the upper statement.

No independence after slice conditioning is asserted; conditioning is
handled only through the exact denominator (3.4).

## 4. The signed hole theorem

Let \(u\) be the number of owners with fewer than \(t\) eligible blocks.
The ternary-carry theorem gives

\[
 u\le e^{-cm}W.
\tag{4.1}
\]

A bad owner contributes at most one signed target occurrence at a fixed
depth.  Hence Lemmas 2.1--3.1 imply:

### Theorem 4.1 (single-atlas labelled-shadow obstruction)

For every \(q\le t\),

\[
 M_q^\pm
 \ge (1-\varepsilon_{m,q})N_q-u,
\tag{4.2}
\]

with \(\varepsilon_{m,q}\) as in (0.4).

The same inequality holds after arbitrary whole-component selection from
any number of carry factors that share the ordered eight-block partition,
the support \(\mathcal V\), and the first-\(t\) eligibility rule.

#### Proof

Every target emitted from a good-owner component satisfies Lemma 2.1, so
at most \(\varepsilon_{m,q}N_q\) physical targets can occur.  The bad
owners add at most \(u\) further distinct targets.  Component selection
cannot create a target outside the union of all candidate components, and
Lemma 2.1 applied to the maximal local alphabet already contains that
union. \(\square\)

For \(q=A\sqrt m\), (0.4) gives

\[
 \varepsilon_{m,q}
 \le \exp\bigl(-A\log(8/5)\sqrt m+O(\log m)\bigr)=o(1).
\tag{4.3}
\]

The local central limit estimate

\[
 N_q=(e^{-A^2}+o(1))W
\tag{4.4}
\]

then proves (0.6).

## 5. How many transverse carry atlases are necessary?

Let \(\mathfrak A_1,\ldots,\mathfrak A_R\) be carry atlases with arbitrary
coordinate relabellings and ordered eight-block partitions.  Each atlas
obeys Theorem 4.1 after relabelling.  Therefore their union covers at most

\[
 R\varepsilon_{m,q}N_q+Ru
\tag{5.1}
\]

signed targets at depth \(q\).  When \(Ru=o(N_q)\), positive-density
coverage forces

\[
 R\varepsilon_{m,q}=\Omega(1),
\tag{5.2}
\]

which is (0.7).

This count is only necessary.  Reaching it does not produce an exact
owner partition or any target Hall inequality.

## 6. Whole-component choices and the exact overlap rigidity

There is a second obstruction after enough transverse atlases have been
provided.

Let \(\mathcal F_0,\mathcal F_1\) be two partitions of one owner set into
whole carry components.  Form their bipartite overlap multigraph
\(\Gamma\): its left and right vertices are components of the two factors,
and every owner is an edge joining its two component owners.

Choose binary variables \(z_C\) indicating selected whole components.
Exact owner coverage is equivalent to

\[
 z_L+z_R=1
\qquad(LR\in E(\Gamma)).
\tag{6.1}
\]

### Theorem 6.1 (two-factor component rigidity)

On every connected component of \(\Gamma\), (6.1) has exactly two
solutions: select all left components or select all right components.
Consequently the complete solution set has size \(2^{c(\Gamma)}\).

#### Proof

Along an overlap edge, the two endpoint variables are complementary.
Along a length-two path, variables on the same shore are equal.  Connectivity
therefore makes every left variable equal and every right variable its
complement.  Both choices work.  Different connected components are
independent. \(\square\)

Thus a convex average of two factor target histograms cannot generally be
rounded componentwise.  It can only be rounded in the coarse packets
given by connected overlap components.  For three or more factors the
owner equations form an \(R\)-partite hypergraph exact-cover system and
are no longer a network matrix; odd-set and determinant obstructions may
occur.

The exact whole-component Hall system is

\[
 \sum_{C\ni X}z_C=1
 \qquad(X\in\mathcal M),
\tag{6.2}
\]

\[
 \sum_C a_{C,q}^\pm(T)z_C\ge1
 \qquad(T\in\mathcal L_q^\pm,\ q\le H).
\tag{6.3}
\]

The scalar \(W_1\) inequality of the ternary-carry theorem is a projection
of (6.3); it supplies none of the subset cuts of this exact-cover system.

## 7. Exact surviving route

The canonical phase-dense carry factor therefore has the following status.

1. Exact middle ownership, cyclic \(H\)-geodesicity, exponentially long
   components, \(o(W)\) seams, and sufficient scalar Gaussian transport
   remain valid.
2. Its first-\(t\) macrocell quotient forces an exponentially unlikely
   \(C\)-run on every deep labelled target.
3. No number of shore/carry/frame variants inside one fixed atlas changes
   that quotient obstruction.
4. Escaping requires at least

   \[
    \exp((\log(8/5)-o(1))q)
   \]

   genuinely transverse block atlases at depth \(q\).
5. Even after supplying them, a separate component-overlap matching
   theorem is needed to satisfy (6.2)--(6.3).

Hence the phase-dense ternary carry is a seam-fusion theorem, not a
labelled-shadow theorem.  The smallest possible positive successor is:

> **Transverse-atlas component Hall theorem.**  Construct
> \(R=\exp(O(H))=W^{o(1)}\) coordinate-transverse carry atlases whose
> component overlap hypergraph has an integral exact owner cover satisfying
> every signed target inequality (6.3), with total residual \(o(W)\).

Neither the existing carry factor nor its whole-component phase choices
prove this successor.
