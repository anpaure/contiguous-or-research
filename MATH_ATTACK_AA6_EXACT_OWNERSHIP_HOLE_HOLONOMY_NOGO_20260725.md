# Lane AA6: exact-middle hole holonomy and a constant integrality gap

Date: 2026-07-25

Method: pure mathematics only.  No search, computation, solver, or
probabilistic experiment is used.

## 0. Outcome

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn=\operatorname{Cat}_m.
\]

This report isolates the exact one-sided target objective on a genuine
two-factor ownership cube.  It then proves a constant integrality gap for
the abstract data retained by every black-box component-signing argument.

1.  For each target, common component signing is exactly a signed
    not-all-equal constraint.  Targets present on both sides of one
    component are automatically safe; targets supported on zero or one
    one-sided component have an immutable floor; every other target is one
    signed NAE hyperedge.  Consequently

    \[
    \min_\varepsilon
    \bigl(M(F_\varepsilon)+M(F_{-\varepsilon})\bigr)
    =\iota+\operatorname{fr}_{\rm NAE}.
    \tag{0.1}
    \]

    Here \(M\) is the number of holes in the controlled target layer,
    \(\iota\) is the exact immutable floor, and
    \(\operatorname{fr}_{\rm NAE}\) is the minimum number of monochromatic
    signed hyperedges under one common signing.

2.  There is an explicit abstract two-rank ownership system with all of the
    following properties.

    * Every row owns exactly \(n\) middle symbols and \(n\) target symbols.
    * Every legal component signing is one integral factor owning every one
      of the \(W\) middle symbols exactly once.
    * The target universe has the exact depth-one cardinality
      \(N_1=\binom n{m-1}\).
    * The targets may be taken to be the actual \((m-1)\)-subsets of
      \([n]\), and every integral child has the exact factor point margins
      at that rank.
    * The uniform fractional average of the integral factors has a perfectly
      balanced floor/ceiling target-load vector: \(W-N_1\) targets have
      fractional load two and every other target has fractional load one.
    * Nevertheless every integral common signing has at least

      \[
      \left(\frac14-o(1)\right)W
      \tag{0.2}
      \]

      target holes.

    In the preliminary unlabeled construction, before its harmless
    \(o(W)\)-sized cardinality correction, every target has fractional load
    exactly one.  In the stronger actual-label construction no quotienting
    is used: every constraint target has fractional load one and local NAE
    floor zero, while the prescribed \(W-N_1\) upper-quota targets have
    fixed load two.

3.  Therefore exact middle ownership, equal row sizes, exact rank mass,
    perfect fractional target coverage, targetwise local minimization, and
    arbitrary correlated common signs do **not** imply an \(o(W)\)-hole
    integral child.  A theorem rounding the fractional rotor/wreath orbit
    cover must use a genuinely cyclic fact which rules out linear signed-NAE
    holonomy.  It cannot follow from the ownership cube and its target
    marginals alone.

The construction below is deliberately not claimed to be realizable by
cyclic-interval wreath rows.  Its point is a sharp method boundary: unlike
the earlier formal signed-row arrays, it has literal exact middle ownership
for every integral child.  Thus the next missing statement is precisely a
cyclic-realizability theorem, not another generic discrepancy inequality.

## 1. Exact hole formula on a two-factor component cube

Let \(F^+,F^-\) be two colored exact middle factors, and let
\(\mathscr K\) be the connected components of their middle-ownership
overlay.  A common signing \(\varepsilon\in\{\pm1\}^{\mathscr K}\)
chooses the \(+\)-side or the \(-\)-side of every component and produces
one exact factor \(F_\varepsilon\).  The opposite signing produces the
complementary exact factor \(F_{-\varepsilon}\).

Fix one controlled target \(a\).  For a component \(K\), let

\[
u_{aK}=\#\{\text{rows on the \(+\)-side of }K\text{ owning }a\},
\]

\[
v_{aK}=\#\{\text{rows on the \(-\)-side of }K\text{ owning }a\}.
\tag{1.1}
\]

Call \(a\) **two-sided safe** if \(u_{aK},v_{aK}>0\) for some \(K\).
Otherwise put

\[
I_a=\{K:u_{aK}+v_{aK}>0\}
\tag{1.2}
\]

and, for \(K\in I_a\), define the unique owning-side sign

\[
s_{aK}=
\begin{cases}
+1,&u_{aK}>0,\\
-1,&v_{aK}>0.
\end{cases}
\tag{1.3}
\]

The definition is valid because a target which is not two-sided safe has
at most one positive side in every component.

### Theorem 1.1 (exact signed-NAE hole identity)

Let

\[
h_a(\varepsilon)
=\mathbf1_{\{a\notin F_\varepsilon\}}
 +\mathbf1_{\{a\notin F_{-\varepsilon}\}}.
\]

Then:

* if \(a\) is two-sided safe, \(h_a(\varepsilon)=0\);
* if \(I_a=\varnothing\), \(h_a(\varepsilon)=2\);
* if \(I_a\ne\varnothing\),

  \[
  \boxed{
  h_a(\varepsilon)
  =\mathbf1_{\{\varepsilon_K=-s_{aK}\ \forall K\in I_a\}}
   +\mathbf1_{\{\varepsilon_K=s_{aK}\ \forall K\in I_a\}}.}
  \tag{1.4}
  \]

In particular, \(|I_a|=1\) gives the immutable value one.  If
\(|I_a|\ge2\), equation (1.4) is exactly the violation indicator of the
signed NAE hyperedge \((I_a,s_a)\).

#### Proof

If some component has positive load on both sides, whichever side is
selected contains an owner of \(a\); the opposite side also contains an
owner.  This proves the safe case.  If \(I_a\) is empty, neither factor can
contain an owner, proving the second case.

Assume now that \(I_a\ne\varnothing\) and that the target is not safe.
The selected factor misses \(a\) exactly when it selects the nonowning side
in every active component, namely when
\(\varepsilon_K=-s_{aK}\) for all \(K\in I_a\).  The complementary
factor misses \(a\) exactly when the original selection chooses the owning
side in every active component, namely when
\(\varepsilon_K=s_{aK}\) for all \(K\in I_a\).  This is (1.4).  If the
edge has at least two vertices, the two displayed events are disjoint and
are precisely the two monochromatic signed patterns. \(\square\)

Let \(\mathcal H\) be the signed hypergraph consisting of the targets with
\(|I_a|\ge2\), after removing the two-sided safe targets.  Put

\[
\iota
=2\#\{a:I_a=\varnothing\}
 +\#\{a:|I_a|=1\}.
\tag{1.5}
\]

Let \(\operatorname{fr}_{\rm NAE}(\mathcal H)\) be the minimum number of
signed hyperedges of \(\mathcal H\) which are monochromatic under one
vertex signing.

### Corollary 1.2 (exact hole holonomy)

\[
\boxed{
\min_\varepsilon
\bigl(M(F_\varepsilon)+M(F_{-\varepsilon})\bigr)
=\iota+\operatorname{fr}_{\rm NAE}(\mathcal H).}
\tag{1.6}
\]

For independent fair component signs,

\[
\mathbb E
\bigl(M(F_\varepsilon)+M(F_{-\varepsilon})\bigr)
=\iota+
\sum_{a:\,|I_a|\ge2}2^{1-|I_a|}.
\tag{1.7}
\]

#### Proof

Sum Theorem 1.1 over all targets and minimize.  For (1.7), each of the two
monochromatic patterns on an edge of size \(d\) has probability \(2^{-d}\).
\(\square\)

Thus the exact target-specific obstruction is signed hypergraph holonomy,
not quadratic load variance.  Multiplicity inside one side is irrelevant to
the hole event once positivity is known.

## 2. An exact-middle ownership cube

We now construct the promised integrality gap.  The construction is an
abstract incidence system; all middle symbols may be identified bijectively
with the actual \(m\)-subsets of \([n]\).

Put

\[
J=\left\lfloor\frac B8\right\rfloor,
\qquad
t=\left\lfloor\frac n3\right\rfloor,
\qquad
f=2n-6t\in\{0,2,4\}.
\tag{2.1}
\]

There are \(J\) active blocks.  One block has four ownership components,
indexed by \(v\in[4]\).  Component \(v\) has two rows on each side,

\[
L_v^0,L_v^1
\qquad\text{and}\qquad
R_v^0,R_v^1.
\]

Allocate \(2n\) private middle symbols to this component.  Partition them
into four cells \(M_v^{ab}\), \(a,b\in\{0,1\}\), of sizes

\[
\begin{pmatrix}
m+1&m\\
m&m+1
\end{pmatrix}.
\tag{2.2}
\]

Let \(L_v^a\) own the union of row \(a\) of (2.2), and let \(R_v^b\)
own the union of column \(b\).  Every row owns exactly \(n\) middle
symbols.  Each middle symbol has one left and one right owner, and all four
left-right intersections are nonempty.  Hence the ownership overlay on
these four rows is connected and is exactly one component.

Different components use disjoint middle symbols.  The remaining
\(B-8J<8\) rows are common fixed rows, each owning \(n\) new middle
symbols.  Thus each source side has \(B\) rows and partitions a middle
universe of size

\[
nB=W.
\tag{2.3}
\]

Choosing one complete side of each active component, together with the
fixed rows, therefore gives one literal integral exact-middle factor for
every sign vector.

## 3. Doubled \(K_4\) target constraints

Fix one active block.  For every unordered pair \(\{u,v\}\subset[4]\)
and every \(a\in[t]\), create two constraint gadgets, denoted \(+\) and
\(-\).  Each gadget has two new targets:

\[
(x_{uv,a}^{+},y_{uv,a}^{+}),
\qquad
(x_{uv,a}^{-},y_{uv,a}^{-}).
\]

For the \(+\)-gadget, the left side of each endpoint component \(u,v\)
owns \(x^+\), and its right side owns \(y^+\).  For the \(-\)-gadget,
the left side owns \(y^-\), and the right side owns \(x^-\).  No other
component owns these four targets.

At a fixed component vertex there are three neighbours and two gadgets for
each of the \(t\) copies, so these constraints use \(6t\) target
occurrences on each side.  Add \(f=2n-6t\) private neutral targets to the
component, each owned once on both sides.  The side now has exactly \(2n\)
distinct target occurrences; split them arbitrarily into two sets of size
\(n\), one for each row.  Hence every row owns exactly \(n\) target
symbols.

One block contains

\[
6\cdot2t\cdot2+4f
=24t+4f
=8n
\tag{3.1}
\]

distinct target symbols.  Give every residual common row \(n\) private
neutral targets.  The uncompressed target universe consequently has size

\[
8nJ+n(B-8J)=nB=W.
\tag{3.2}
\]

### Lemma 3.1 (perfect fractional target coverage)

Under the uniform distribution on all component signings, every
uncompressed target has expected load exactly one in the selected integral
factor.

#### Proof

A neutral target has load one for every signing.  A constraint target is
owned by exactly two endpoint components, and each endpoint independently
selects its owning side with probability \(1/2\).  Its expected load is
therefore \(2\cdot(1/2)=1\). \(\square\)

Thus the convex average of these exact-middle factors is an exact
fractional target resolution, not merely a lower cover.

### Lemma 3.2 (the integral hole lower bound)

Every component signing has at least \(4tJ\) holes in the uncompressed
target universe.

#### Proof

For either gadget on a component pair \(\{u,v\}\), both targets are
covered exactly when the two component signs differ.  If the signs agree,
one target has load two and the other has load zero.  Hence each gadget
contributes one hole precisely on a monochromatic edge of the signed
\(K_4\).

Every two-colouring of \(K_4\) has at most four bichromatic edges, so at
least two of its six edges are monochromatic.  There are \(2t\) parallel
gadgets on each edge.  One active block therefore has at least
\(2\cdot2t=4t\) holes.  Sum over the \(J\) disjoint blocks. \(\square\)

The bound is sharp inside each block: a two-two split of the four component
signs has exactly two monochromatic vertex pairs.

Notice that every constraint pair is separately perfectible.  Its two
targets are both covered when its endpoint signs differ.  The loss in
Lemma 3.2 is wholly common-sign holonomy.

## 4. Exact depth-one target count and balanced quotas

The actual depth-one layer has

\[
N_1=\binom n{m-1}
=\frac m{m+2}W.
\tag{4.1}
\]

Put

\[
D=W-N_1=\frac{2W}{m+2}.
\tag{4.2}
\]

We reduce the \(W\) abstract target symbols to exactly \(N_1\) symbols by
merging \(D\) disjoint pairs.  The pairs can be chosen so that no source
row on either side contains both members.

### Lemma 4.1 (noncoincident merging)

For all sufficiently large \(m\), there are \(D\) disjoint pairs of target
symbols such that the two members of every pair occur together in no source
row.

#### Proof

Form the conflict graph on the \(W\) uncompressed target symbols, joining
two symbols when some source row contains both.  Every target occurs in at
most two source rows, and every row contains \(n\) targets.  Hence the
conflict degree is at most \(2(n-1)\).

Choose pairs greedily.  After \(j<D\) pairs have been removed, at least
\(W-2j\) vertices remain.  Pick one remaining vertex.  It has at most
\(2(n-1)\) forbidden partners, so another permissible vertex exists if

\[
W-2j>2n-1.
\]

At the last step it is enough that

\[
W-2D+2>2n-1.
\]

By (4.2), the left side is
\(W(1-4/(m+2))+2\), which exceeds \(2n-1\) for all sufficiently large
\(m\). \(\square\)

Identify the two symbols in each selected pair.  Because paired symbols
never co-occur in one row, every row still owns exactly \(n\) distinct
targets.  The quotient target universe has size \(W-D=N_1\).

In the uniform fractional average, an unmerged target has load one and a
merged target has load two.  There are exactly \(D=W-N_1\) merged targets.
Thus this is precisely a balanced floor/ceiling load vector for total mass
\(W\) on \(N_1\) targets: the floor is one and the number of upper cells is
\(D\).

Merging one pair can reduce the hole count of an integral factor by at most
one.  Indeed, if the old loads are \(x,y\), then

\[
\mathbf1_{\{x=0\}}+\mathbf1_{\{y=0\}}
-\mathbf1_{\{x+y=0\}}\le1.
\tag{4.3}
\]

Consequently every integral signing in the compressed instance has at
least

\[
4tJ-D
=4\left\lfloor\frac n3\right\rfloor
  \left\lfloor\frac B8\right\rfloor
  -\frac{2W}{m+2}
\tag{4.4}
\]

holes.  Since \(nB=W\),

\[
4tJ
=\frac16W+O(B+n),
\qquad
D=O(W/n),
\tag{4.5}
\]

and therefore (4.4) is

\[
\boxed{\left(\frac16-o(1)\right)W.}
\tag{4.6}
\]

This proves the promised constant gap with the exact depth-one layer
cardinality and the exact balanced fractional quota count.

## 4A. Actual rank labels and exact point margins

The preceding compression already proves the black-box no-go.  We now give
a stronger realization in which the target symbols are the actual members
of

\[
\mathcal T=\binom{[n]}r,
\qquad r=m-1,
\qquad |\mathcal T|=N_1,
\tag{4A.1}
\]

and every integral child has the exact coordinate point margins forced by a
collection of \(B\) cyclic rows.  The rows themselves are still not claimed
to be cyclic interval systems.

### Lemma 4A.1 (regular upper family)

There is a family \(\mathcal U\subseteq\mathcal T\) of size

\[
D=W-N_1
\tag{4A.2}
\]

such that every coordinate belongs to exactly \(rD/n\) members of
\(\mathcal U\).

#### Proof

First,

\[
\frac{rD}{n}
=\frac{rW}{n}-\frac{rN_1}{n}
=rB-\binom{n-1}{r-1}
\tag{4A.3}
\]

is an integer.

Among all \(D\)-element subfamilies of \(\mathcal T\), choose one minimizing
the sum of squares of its coordinate degrees.  If two coordinates \(x,y\)
have degrees differing by at least two, consider members containing \(x\)
but not \(y\).  Swapping \(x\) for \(y\) is a bijection from all such
\(r\)-sets to the \(r\)-sets containing \(y\) but not \(x\).  If the swap
of every former member also belonged to the family, the degree of \(y\)
outside the common \(x,y\)-part would be at least the degree of \(x\), a
contradiction.  Hence some swap leaves the family simple.  Performing it
decreases the degree-square sum whenever
\(\deg(x)\ge\deg(y)+2\), contradicting minimality.

All degrees therefore differ by at most one.  Their average is the integer
\(rD/n\), so all are equal to that value. \(\square\)

### Lemma 4A.2 (near-complete rectangle packing)

All but \(o(W)\) members of \(\mathcal T\) can be partitioned into
four-sets

\[
\{C_0\cup\{x\},C_0\cup\{y\},
  C_1\cup\{x\},C_1\cup\{y\}\},
\tag{4A.4}
\]

where \(x\ne y\), neither belongs to \(C_0,C_1\), and
\(|C_0|=|C_1|=r-1\).  After discarding every rectangle meeting the regular
family \(\mathcal U\), the number of remaining rectangles is still

\[
\left(\frac14-o(1)\right)W.
\tag{4A.5}
\]

#### Proof

Partition \(2m\) of the \(n=2m+1\) coordinates into ordered pairs
\(P_i=\{x_i,y_i\}\), \(1\le i\le m\), leaving one coordinate unpaired.
For every \(S\in\mathcal T\) which meets some \(P_i\) in exactly one point,
let \(i(S)\) be the least such index.  Swapping \(x_i,y_i\) is a
fixed-point-free involution on the class with first unequal pair \(i\).
Pair its two-cycles arbitrarily in twos.  Every resulting four-set has form
(4A.4), with exchange direction \(x_i-y_i\).  At most one two-cycle, hence
at most two sets, is left over for each \(i\).

The sets not assigned to any first unequal pair meet every \(P_i\) in zero
or two points.  Such a set is determined by a subfamily of the \(m\) pairs
and the choice of whether to use the unpaired coordinate.  There are at
most \(2^{m+1}\) of them.  Thus at most

\[
2^{m+1}+2m=o(W)
\tag{4A.6}
\]

sets are unpacked.

The rectangles are disjoint.  Deleting every rectangle which meets
\(\mathcal U\) removes at most \(D\) rectangles and at most \(4D=o(W)\)
additional targets.  Since \(N_1=(1-o(1))W\), (4A.5) follows. \(\square\)

Let \(Q\) be the number of rectangles remaining after Lemma 4A.2, and keep

\[
J=\left\lfloor\frac B8\right\rfloor,
\qquad
t_*=\min\left\{\left\lfloor\frac n3\right\rfloor,
                 \left\lfloor\frac{Q}{6J}\right\rfloor\right\}.
\tag{4A.7}
\]

Then

\[
t_*=\frac n3+O(1),
\qquad
f_*=2n-6t_*=O(1).
\tag{4A.8}
\]

More precisely, the proof of Lemma 4A.2 gives

\[
Q=\frac{N_1}{4}+O(D+2^m+m)
=\frac W4+O(W/n),
\]

while \(J=B/8+O(1)\).  Hence \(Q/(6J)=n/3+O(1)\).  The minimum in
(4A.7) also makes \(f_*\ge0\).

Assign a different rectangle to every tuple consisting of an active block,
one of its six component pairs, and one of \(t_*\) copies.  If the rectangle
is written as in (4A.4), use

\[
(x^+,y^+)=(C_0\cup\{x\},C_0\cup\{y\}),
\]

\[
(x^-,y^-)=(C_1\cup\{x\},C_1\cup\{y\})
\tag{4A.9}
\]

for the doubled constraint gadget of Section 3.  The number of constraint
targets used is \(24t_*J\).  At each component, put \(3t_*\) of its
\(6t_*\) constraint occurrences in each of its two rows.  This is possible
because \(3t_*\le n\), and it leaves \(n-3t_*\) neutral slots in each row.

There are exactly

\[
W-24t_*J
\tag{4A.10}
\]

neutral row slots left.  Use every target of \(\mathcal T\) not already in
a constraint rectangle once in those slots, and use every target of
\(\mathcal U\) once more.  This is the correct number of occurrences,
because

\[
(N_1-24t_*J)+D=W-24t_*J.
\]

All rectangles used for constraints avoid \(\mathcal U\).  Distribute the
neutral occurrences among the available row slots, putting the two copies
of a member of \(\mathcal U\) in different rows.  Here is a direct Hall
proof that this is possible.  First place one copy of every remaining
target in distinct neutral slots, leaving exactly \(D\) slots.  Match the
second copies of the \(D\) members of \(\mathcal U\) to those slots, with a
copy forbidden only from the row containing its first copy.  Every row has
at most \(n\) slots and, for large \(m\), \(D>2n\).  If a set of second
copies has all first copies in one row, it has size at most \(n\) and sees
at least \(D-n\ge n\) allowed slots.  If its first copies occupy at least
two rows, every remaining slot is allowed to at least one member of the
set, so its neighborhood has size \(D\).  Hall's condition follows.  The
two source sides use the same neutral assignment.  Thus every row still
owns \(n\) distinct actual targets.

### Theorem 4A.3 (one-design exact-ownership gap)

The resulting instance has all of the following properties.

1. Every legal child owns every middle symbol exactly once.
2. Its target labels are exactly \(\binom{[n]}{m-1}\), and every row owns
   \(n\) distinct such labels.
3. The uniform fractional average has load two on \(\mathcal U\) and load
   one elsewhere, hence is an exact balanced floor/ceiling target vector.
4. Every integral child has coordinate point degree exactly \(rB\) at the
   target rank.
5. Every integral child has at least

   \[
   4t_*J=\left(\frac16-o(1)\right)W
   \tag{4A.11}
   \]

   target holes.

#### Proof

Items 1 and 2 follow from Sections 2--3 and the actual-label assignment
above.  A constraint target has expected load one, every ordinary neutral
target has fixed load one, and every member of \(\mathcal U\) has fixed
load two.  This proves item 3.

For item 4, compare the two sides of one component on one doubled gadget.
By (4A.9),

\[
\mathbf1_{x^+}-\mathbf1_{y^+}
=\mathbf1_{x^-}-\mathbf1_{y^-}
=e_x-e_y.
\tag{4A.12}
\]

The \(+\)- and \(-\)-gadgets use opposite side orientations, so their
coordinate-incidence differences cancel exactly.  Neutral occurrences are
identical on the two sides.  Hence every component switch preserves every
coordinate point degree.

At the all-left corner, the contribution of one rectangle is
\(2\mathbf1_{x^+}+2\mathbf1_{y^-}\).  Its difference from using all four
rectangle targets once is

\[
(\mathbf1_{x^+}-\mathbf1_{y^+})
 +(\mathbf1_{y^-}-\mathbf1_{x^-})=0
\tag{4A.13}
\]

by (4A.12).  Therefore the all-left point-degree vector is the degree vector
of the complete rank-\(r\) layer, plus one extra copy of \(\mathcal U\).
By Lemma 4A.1, its value at every coordinate is

\[
\binom{n-1}{r-1}+\frac{rD}{n}
=\frac{rN_1}{n}+\frac{rD}{n}
=\frac{rW}{n}
=rB.
\tag{4A.14}
\]

All component switches preserve this vector, proving item 4.

Finally, the doubled-\(K_4\) argument of Lemma 3.2 gives \(4t_*\) holes per
active block.  Equations (4A.7)--(4A.8) and \(J=B/8+O(1)\) yield (4A.11).
\(\square\)

Thus even literal target labels and exact factor point margins do not make
black-box common-sign rounding possible.  The missing condition is narrower
still: the \(n\) targets owned by each individual row must arise as the
cyclic intervals of one coordinate order, coherently with that row's
middle windows.

## 4B. Optimizing the holonomy block

The doubled \(K_4\) block was chosen for a short first proof.  Using a
doubled complete graph on \(n\) component vertices raises the gap from
\(1/6\) to \(1/4\) while retaining every property of Theorem 4A.3.

Keep the regular upper family \(\mathcal U\) and the \(Q\) actual-target
rectangles from Lemmas 4A.1--4A.2.  Put

\[
J_*=\min\left\{
 \left\lfloor\frac{B}{2n}\right\rfloor,
 \left\lfloor\frac{Q}{\binom n2}\right\rfloor
 \right\}.
\tag{4B.1}
\]

One active block now has \(n\) ownership components, with two rows on each
side of every component.  Its middle symbols are assigned componentwise by
the connected \(2\)-by-\(2\) construction (2.2).  Thus one block uses
\(2n\) rows per source factor.  Different blocks use disjoint middle
symbols.  The remaining \(B-2nJ_*\) rows are common fixed rows, each with
\(n\) new middle symbols, exactly as in Section 2.  Consequently both
source sides still have \(B\) rows and every component signing partitions
all
\[
2n^2J_*+n(B-2nJ_*)=nB=W
\]
middle symbols.

For every pair of component vertices, assign one unused rectangle and use
its two parallel directions as the \(+\)- and \(-\)-gadgets in (4A.9).
There are therefore two target constraints on every edge of \(K_n\).  A
component is incident with

\[
2(n-1)
\tag{4B.2}
\]

constraint occurrences, leaving two neutral target slots among its two
rows' total capacity \(2n\).  Split the constraint occurrences evenly,
\(n-1\) per row, and leave one neutral slot per row.

Use all actual targets not assigned to a constraint rectangle once in the
neutral slots, and use every member of \(\mathcal U\) once more.  The count
again matches exactly:

\[
W-4J_*\binom n2
=\left(N_1-4J_*\binom n2\right)+D.
\tag{4B.2a}
\]

The left side is the number of neutral row slots and the right side counts
one copy of every unused actual target plus the second copies of
\(\mathcal U\).  To make the assignment explicit, first inject one copy of
every unused target into distinct neutral slots; exactly \(D\) slots
remain.  Match the second copy of every member of \(\mathcal U\) to a
remaining slot outside the row of its first copy.  If a subfamily has all
first copies in one row, its size is at most \(n\), while its
neighbourhood has size at least \(D-n\ge n\) for all large \(m\).  If its
first copies occupy at least two rows, every remaining slot is adjacent to
some member, so its neighbourhood has size \(D\).  Hall's theorem gives
the matching.  Use the same neutral assignment on both source sides.
Thus every row owns \(n\) distinct actual targets.  Rectangle effects
cancel componentwise by (4A.12), so every child has the exact point margins
(4A.14).

### Theorem 4B.1 (optimized exact-ownership gap)

The construction above has literal exact middle ownership, the actual
rank-\((m-1)\) target universe, exact balanced fractional target loads,
and exact global point margins in every integral child.  Nevertheless every
integral common signing has at least

\[
2m^2J_*
=\left(\frac14-o(1)\right)W
\tag{4B.3}
\]

target holes.

#### Proof

A signing cuts at most \(\lfloor n^2/4\rfloor=m(m+1)\) edges of
\(K_n\).  Since

\[
\binom n2=m(2m+1),
\]

at least \(m^2\) component pairs are monochromatic.  Each monochromatic
pair carries two constraint gadgets, and each gadget contributes one hole.
Thus one active block has at least \(2m^2\) holes.

Lemma 4A.2 and \(D=O(W/n)\) give

\[
Q=\frac W4+O(W/n).
\]

Therefore

\[
J_*
=\left(1+O(n^{-1})\right)\frac{B}{2n}.
\tag{4B.4}
\]

Using \(W=nB\) and \(n=2m+1\),

\[
\frac{2m^2J_*}{W}
=\left(1+O(n^{-1})\right)\frac{m^2}{n^2}
=\frac14+o(1).
\]

All ownership, load, and point-margin statements follow exactly as in
Theorem 4A.3, since only the signed constraint graph has changed. \(\square\)

The constant \(1/4\) is the ceiling of this precise doubled-simple-graph
template.  Indeed, for a constraint graph on \(p\) components, a random
two-colouring has expected \(|E|/2\) monochromatic edges, so some signing
has at most \(|E|/2\).  Each monochromatic edge gives two holes.  The two
gadgets on an edge use two target occurrences at each endpoint; the
per-component capacity \(2n\) therefore gives \(\deg(v)\le n\) and
\(|E|\le pn/2\).  Thus the minimum hole count is at most
\(|E|\le pn/2\), whereas the block has \(2np\) target slots.  Its gap ratio
cannot exceed \(1/4\).  The complete graph \(K_n\) attains this bound
asymptotically.

## 5. What this rules out

Consider any proposed theorem whose hypotheses use only the following
data:

1. two exact middle factors and their genuine ownership components;
2. equal side cardinalities and \(n\) target incidences per row;
3. a convex combination of legal integral component signings whose target
   load is an exact balanced floor/ceiling vector;
4. exact global point margins at the controlled target rank;
5. targetwise local signs or any correlated law on one common final sign
   vector.

The optimized refined construction of Section 4B satisfies all five items,
yet every integral outcome has \((1/4-o(1))W\) holes.  Because every probability law
on legal outcomes is a convex combination of these integral signings, no
SDP rounding, partial coloring, conditional-expectation scheme, or other
correlated-sign rule can improve this lower bound without using an
additional hypothesis.

This obstruction is not an invariant-target packet argument.  Every
constraint target is switchable and has targetwise local floor zero; the
actual-label refinement in Section 4A requires no target merging.  It also
assumes no bounded coordinate support.  Hence the nonaligned logarithmic-support escape from
`NONALIGNED_REFLECTION_SUPPORT_SEED_ESCAPE_20260725.md` does not address
this static common-sign gap.

Conversely, this construction is not a dynamic path obstruction.  Changing
the overlay can change the signed NAE hypergraph, just as nonaligned
multistep switching can destroy a static invariant-seed certificate.  No
claim is made against a genuinely cyclic adaptive trajectory.

## 6. The next exact statement

For a genuine cyclic-wreath ownership overlay \(\mathcal O\), form the
signed target hypergraph \(\mathcal H_H(\mathcal O)\) of Theorem 1.1
simultaneously over the desired depth window (the disjoint union of the
layerwise target hypergraphs).  Write \(M_H(F)\) for the total number of
missing designated targets over all controlled layers, rather than a
per-layer maximum.  For a particular common signing \(\varepsilon\), write

\[
v_H(\mathcal O,\varepsilon)
=\#\{e\in\mathcal H_H(\mathcal O):e
       \text{ is NAE-violated by }\varepsilon\}.
\tag{6.1}
\]

Thus \(\operatorname{fr}_{\rm NAE}\) is the minimum of \(v_H\), but the
minimizer is part of the data and must not be discarded.  Let
\(C_H(\mathcal O,\varepsilon)\ge 0\) denote the minimum literal
initialization-plus-connector excess for traversing the rows of the
selected child \(F_\varepsilon\) in the audited fixed-window architecture,
with the traversal realizing the same designated controlled-target
incidences and owner witnesses used to define \(\mathcal H_H(\mathcal O)\).
The resulting pre-repair word has length \(W+C_H\).

The exact target-specific geometric statement now required is:

> **Joint cyclic low-holonomy lemma \(\mathrm{JCLH}_A\) -- UNPROVED.**  For
> every fixed \(A>0\), with \(H=\lceil A\sqrt m\rceil\), there are an
> actual cyclic-wreath exact-middle overlay \(\mathcal O\) and one common
> signing \(\varepsilon\), used at every depth \(q\le H\), such that
> \[
> \boxed{
> \iota_H(\mathcal O)+v_H(\mathcal O,\varepsilon)
>       +C_H(\mathcal O,\varepsilon)=o(W).}
> \tag{6.2}
> \]

The common quantifier in (6.2) is essential.  A signing minimizing holes
and a different signing minimizing reset toll do not compose.

By Theorem 1.1, summed over the disjoint layer union,

\[
M_H(F_\varepsilon)+M_H(F_{-\varepsilon})
=\iota_H+v_H(\mathcal O,\varepsilon).
\]

Hence (6.2), with no symmetry assumption, already gives
\(M_H(F_\varepsilon)=o(W)\).  Traverse this same child, then append one
literal entry for each missing controlled target.  Its length is

\[
W+C_H+M_H(F_\varepsilon)=W+o(W).
\tag{6.3}
\]

The audited fixed-window diagonalization and outer tails then give the
constant-one theorem.

For a full \(Q_m\)-color rotor resolution the corresponding quantifier is
also joint: one final integral resolution and its re-Eulerized chronology
must satisfy

\[
\sum_{c=1}^{Q_m}
   \bigl(M_c+C_c\bigr)=o(Q_mW).
\tag{6.4}
\]

Only then does averaging select one color with
\(M_c+C_c=o(W)\).  Minimizing the hole total and the chronology total over
different resolutions is invalid.  In the frozen packet language, the
candidate bound \(\sum_{d\le H}2d\,V_d^*=o(Q_mW)\) must therefore be
proved for the same final exact color resolution and chronology; the direct
one-color alternative is the already isolated rotor-SCD statement
\(\Phi_H=o(W)\).

The abstract gap proves that \(\mathrm{JCLH}_A\) cannot be obtained from
fractional balance or exact ownership alone.  A proof must use a cyclic
restriction strong enough to exclude the positive-density doubled-complete-
graph holonomy of Section 4B (or otherwise neutralize it dynamically) while
retaining exact middle ownership and one common chronology.

## 7. Scope audit

1. **Exact middle ownership is literal.**  Every child partitions all
   \(W\) middle symbols exactly once; no fractional middle object is called
   a factor.
2. **The target fractional point is exact.**  In Sections 4A--4B it is the
   balanced \(\{1,2\}\) floor/ceiling histogram on the actual rank layer,
   with exactly \(W-N_1\) upper cells and no target quotienting.
3. **Actual labels and point margins are available.**  Sections 4A--4B use the
   literal rank-\((m-1)\) target layer and gives every integral child point
   degree \((m-1)B\) at every coordinate.
4. **All terminal objects are integral.**  The lower bound holds for every
   common component sign vector and therefore for every correlated law.
5. **The asymptotic gap is at the \(W\)-scale.**  The optimized block count
   is \(J_*=(1+O(1/n))B/(2n)\), so its floor and rectangle-packing losses
   are absorbed in the displayed \(o(W)\); no loss is hidden in a
   fractional terminal object.
6. **No cyclic realization is asserted.**  The rows are abstract
   \(n\)-by-\(n\) incidence blocks.  The theorem closes the black-box
   discrepancy lane, not the genuine wreath-geometry lane.
7. **No bounded-support claim is used.**  The newest nonaligned support
   escape and the present holonomy gap address different mechanisms.
8. **No multistage no-go is claimed.**  A successful dynamic theorem must
   control the joint quantity in (6.2), or a stronger potential, as the
   ownership overlay is recomputed.

The stable conclusion is that one-sided holes expose the exact obstruction
more cleanly than quadratic energy: it is signed NAE holonomy.  Perfect
fractional target coverage and exact middle ownership coexist with a
\((1/4-o(1))W\) common-sign gap.  The remaining theorem must therefore be
cyclic and target-geometric, not a generic signing theorem.
