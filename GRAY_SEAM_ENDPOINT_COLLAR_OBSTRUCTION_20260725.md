# Gray-seam endpoints: a collar count and a two-junta obstruction

Date: 2026-07-25

## 0. Outcome

This note addresses only the long-collar Gray-seam gate in
`RECURSIVE_PAIR_OMISSION_PASCAL_RECURRENCE_20260725.md`.

Two exact facts emerge.

1.  Collar failures are globally sparse.  In the full four-partite
    Boolean-diamond incidence system, arbitrary length-`H` endpoint
    collars delete only an `O(H/s)` fraction of all diamonds on a
    `(2s+1)`-set.
2.  This global fact is not enough at the required endpoint density
    `Theta(1/H)`.  There are endpoint families of that density, with
    **empty collars**, for which every relative coordinate relabelling
    leaves `(1/2-o(1))` of one endpoint family unmatched already at the
    first `E-A` containment seam.

Consequently a fixed four-uniform Gray-seam matching cannot be deduced
from endpoint cardinalities, orientations, collars, and one global
coordinate relabelling alone.  A positive recursive proof needs an
additional anti-junta endpoint theorem, or it must retain many independently
choosable interior cut positions per child component.

No assertion about constant one is made here.

## 1. The endpoint diamond and its collars

Let `Q` have size `v=2s+1`, and first take the central parameter `k=s`.
The four role-labelled parts are

\[
 \mathcal E={Q\choose k+1},\qquad
 \mathcal A={Q\choose k},\qquad
 \mathcal D={Q\choose k-1},\qquad
 \mathcal B={Q\choose k}.
\]

An oriented Boolean diamond is determined by a triple

\[
 (D,u,v),\qquad D\in {Q\choose k-1},\quad
 u,v\in Q\setminus D,\quad u\ne v,
\]

and has

\[
 A=D\cup\{u\},\qquad B=D\cup\{v\},\qquad
 E=D\cup\{u,v\}.
\tag{1.1}
\]

This is exactly the set-level pattern of the Gray order

\[
 E\longrightarrow aA\longrightarrow abD\longrightarrow bB
 \longrightarrow E.
\]

For each role-labelled endpoint `X`, let

\[
 F_X^-,F_X^+\subseteq Q,
 \qquad |F_X^-|,|F_X^+|\le H,
\tag{1.2}
\]

be the residual coordinates used in its backward and forward `H`-collars.
The diamond (1.1) is collar-clean when

\[
\begin{array}{ll}
 v\notin F_E^-\cup F_A^+,&
 u\notin F_A^-\cup F_D^+,\\[1mm]
 v\notin F_D^-\cup F_B^+,&
 u\notin F_B^-\cup F_E^+.
\end{array}
\tag{1.3}
\]

The precise assignment of the signs is immaterial for the count below;
what matters is that each of the eight collar tests asks whether one of
the two exchanged coordinates belongs to a set of size at most `H`.

### Lemma 1.1 -- exact global collar charge

Let `\mathcal X` be the multiset of all oriented diamonds (1.1), and let
`\mathcal X_{\rm bad}` be the diamonds failing at least one test in (1.3).
Then

\[
 \boxed{|\mathcal X_{\rm bad}|\le 8H(s+2)N,}
 \qquad N={2s+1\choose s}.
\tag{1.4}
\]

Since

\[
 |\mathcal X|={2s+1\choose s-1}(s+2)(s+1)
              =\Theta(Ns^2),
\tag{1.5}
\]

one has

\[
 \boxed{\frac{|\mathcal X_{\rm bad}|}{|\mathcal X|}
        =O(H/s).}
\tag{1.6}
\]

The same conclusion holds uniformly for `k=s+o(s)`.

#### Proof

Charge a failed test to a pair `(X,x)`, where `X` is the endpoint whose
collar contains the exchanged coordinate `x`.

For a fixed `E` and fixed `x\in E`, at most `k` oriented diamonds incident
with `E` use `x` as the prescribed one of `u,v`: choose the other element
of `E\setminus\{x\}`.  For a fixed `D` and fixed `x\notin D`, there are at
most `v-k+1` choices of the other outside element.  For a fixed middle
endpoint `A`, a fixed inside coordinate can be its `u` in at most `v-k`
diamonds, and a fixed outside coordinate can be its `v` in at most `k`
diamonds.  The same bounds hold for `B`.

Every one of these numbers is at most `s+2`.  There are eight collar sets,
each of size at most `H`, and every role part has at most `N` vertices.
The union bound therefore gives (1.4).  Equation (1.5) follows by choosing
`D` and the ordered pair `(u,v)`.  This proves (1.6).  The calculation for
`k=s+o(s)` changes every factor by `1+o(1)`.  \(\square\)

### Corollary 1.2 -- the critical exceptional scale

The total degree deficit caused by collars is `O(NHs)`.  Hence the number
of endpoints whose clean degree is zero is at most

\[
 \boxed{O(NH/s).}
\tag{1.7}
\]

At `H\asymp\sqrt s`, this upper bound is `O(N/H)`, exactly the endpoint
leave scale required in the recursive theorem, rather than `o(N/H)`.

Thus even the global collar estimate has no spare asymptotic factor at the
critical square-root scale.

## 2. A two-junta obstruction with empty collars

We now show that collars are not the only issue.  Put

\[
 b=2^t,\qquad t\longrightarrow\infty,qquad t=o(\sqrt s).
\tag{2.1}
\]

The intended application has `b\asymp H` polynomial in `s`, so these
conditions hold.  For a set `R\subseteq Q`, write

\[
 \mathcal S_r(R)=\{X\in {Q\choose r}:R\subseteq X\}.
\tag{2.2}
\]

Choose disjoint `(t+1)`-sets `T_1,T_2`.  Define the rank-`k` family

\[
 \mathcal A_*=\mathcal S_k(T_1)\cup\mathcal S_k(T_2).
\tag{2.3}
\]

Let `\mathcal E_*` be a rank-`k+1` star with a `t`-element core.  The
sizes obey

\[
 |\mathcal E_*|=(1+o(1))\frac{N}{b},
 \qquad
 |\mathcal S_k(T_i)|=(1+o(1))\frac{N}{2b},
\tag{2.4}
\]

and the intersection of the two branches in (2.3) is `o(N/b)`.  Thus,
after deleting `o(N/b)` arbitrary vertices, the two families may be made
equal in size

\[
 J=(1+o(1))N/b,
\tag{2.5}

while each branch of `\mathcal A_*` still has `(1/2-o(1))J` vertices.

### Theorem 2.1 -- no relabelling repairs the two-junta seam

For every pair of coordinate permutations `\pi_A,\pi_E`, the bipartite
containment graph

\[
 A\subset E,qquad
 A\in\pi_A\mathcal A_*,\quad E\in\pi_E\mathcal E_*,
\tag{2.6}
\]

has matching number at most

\[
 \boxed{(1/2+o(1))J.}
\tag{2.7}
\]

Equivalently, every such matching leaves `(1/2-o(1))J` members of the
rank-`k` endpoint family unmatched.  This remains true when all collars
are empty.

#### Proof

Only the relative permutation matters.  After relabelling, let `T` be the
`t`-element core of the upper star and retain the notation `T_1,T_2` for
the two disjoint lower cores.  Since

\[
 |T\cap T_1|+|T\cap T_2|\le t,
\]

there is an index `i` for which

\[
 a:=|T\cap T_i|\le t/2.
\tag{2.8}
\]

If `A\in\mathcal S_k(T_i)` is contained in some
`E\in\mathcal S_{k+1}(T)`, then `E\setminus A` has one element, so

\[
 |T\setminus A|\le1.
\tag{2.9}
\]

Put `R=T\setminus T_i`, so `|R|=t-a\ge t/2`.  Condition (2.9) says that
`A` contains at least `|R|-1` elements of `R`.

Choose `A` uniformly from `\mathcal S_k(T_i)`.  For any fixed
`R'\subseteq R` of size `|R|-1`,

\[
 \Pr(R'\subseteq A)
 =\frac{(k-t-1)_{|R|-1}}{(v-t-1)_{|R|-1}}
 \le\left(\frac{k}{v-t-|R|}\right)^{|R|-1}
 \le (1/2+o(1))^{|R|-1}.
\tag{2.10}
\]

There are `|R|` choices for the possibly omitted member, plus the case in
which none is omitted.  A union bound and (2.8) give

\[
 \Pr(|T\setminus A|\le1)
 \le(t+1)(1/2+o(1))^{t/2-1}=o(1).
\tag{2.11}
\]

Therefore only `o(|\mathcal S_k(T_i)|)=o(J)` members of the entire `i`-th
branch have even one neighbour in the upper endpoint family.  The branch
itself contains `(1/2-o(1))J` retained vertices.  All but `o(J)` of them
are necessarily unmatched, proving (2.7).  \(\square\)

### Remarks on sharpness

1. A single lower `t`-star is not an obstruction: its core can be aligned
   with the upper core.  The obstruction begins with two macroscopically
   large, mutually distant junta branches.
2. The leave in Theorem 2.1 is `Theta(N/b)`.  Taking `b\asymp H` makes it
   exactly `Theta(N/H)`, whereas the Gray-seam resolution requires
   `o(N/H)`.
3. The proof permits independent global relabellings of both child systems.
   Randomizing those relabellings cannot help, since (2.7) holds pointwise
   for every outcome.

## 3. Consequence for the recursive gate

Lemma 1.1 proves a useful positive fact: over the **whole** Boolean diamond
system, long collars cost only `O(H/s)`.  Theorem 2.1 proves that a sparse
endpoint selector of density `Theta(1/H)` can nevertheless be concentrated
on a two-junta and have a linear matching defect at its own scale.

Therefore the long-collar Gray-seam theorem needs at least one of the
following genuinely new inputs.

* **Endpoint anti-concentration.**  Every child path partition admits an
  orientation/cutting for which its first and last endpoint families have
  no macroscopic separated junta branches (a quantitative shadow-expansion
  condition is enough).
* **Many-choice cuts.**  A component offers `\omega(1)` collar-separated
  interior cut positions, and the matching selects the cut jointly with
  the other three components.  A theorem of this form is not a matching of
  four already fixed endpoint families.
* **Cross-node transport.**  Endpoint deficits of one pair node can be
  routed into different first-deviation cells before the four-block match.

Without one of these additions, fixed four-uniform endpoint matching is
false even before upper/lower target service and before any collar is
imposed.

## 4. A positive many-choice theorem for one Gray seam

The preceding obstruction disappears completely if a child block offers
all of its vertices as possible seam ports.  The following deterministic
statement is useful because it needs neither random relabelling nor endpoint
pseudorandomness.

Let

\[
 G_r\subseteq {Q\choose r}\times {Q\choose r+1}
\]

be the inclusion graph.  Its two degrees are

\[
 d_r=v-r,\qquad d_{r+1}=r+1.
\tag{4.1}
\]

Give every rank-`r` and rank-`r+1` vertex one forbidden set of size at most
`H`.  Declare an incidence `A\subset E` dirty when the exchanged coordinate
`E\setminus A` belongs to either endpoint's forbidden set.  There are at
most

\[
 H\left({v\choose r}+{v\choose r+1}\right)
\tag{4.2}
\]

dirty incidences.

Partition each rank into arbitrary blocks of exactly `b` vertices (discard
one remainder block in each rank).  Contract every block to one vertex,
retaining parallel inclusion incidences.

### Theorem 4.1 -- arbitrary-block one-seam matching

Let `\mathcal C_-` be the block family on the smaller of the two Boolean
ranks, and let `N=\max\{\binom vr,\binom v{r+1}\}`.  The clean contracted
multigraph has a matching which leaves at most

\[
 \boxed{
 O\left(\frac{NH}{b\min(d_r,d_{r+1})}\right)+O(1)
 }
\tag{4.3}
\]

blocks of `\mathcal C_-` unmatched.  Uniformly for `r=v/2+o(v)`, this is

\[
 O(NH/(bv))+O(1).
\tag{4.4}

In particular, if `b\asymp H`, `H\to\infty`, and `H=o(v)`, the leave is

\[
 O(N/v)=o(N/H).
\tag{4.5}

#### Proof

Suppose for definiteness that rank `r` is the smaller rank; the other case
is identical.  Biregularity gives

\[
 {v\choose r}d_r={v\choose r+1}d_{r+1}.
\]

Hence `d_r\ge d_{r+1}`.  Let `\mathcal S` be any set of rank-`r` blocks,
and suppose its clean neighbourhood has size

\[
 |N_c(\mathcal S)|=|\mathcal S|-t.
\]

Before dirty incidences are removed, exactly `bd_r|\mathcal S|` incidence
edges leave `\mathcal S`.  At most

\[
 bd_{r+1}(|\mathcal S|-t)
\]

clean incidence edges can land in its clean neighbour blocks.  Therefore
the total number `B_{\rm bad}` of dirty incidences satisfies

\[
\begin{aligned}
 B_{\rm bad}
 &\ge bd_r|\mathcal S|-bd_{r+1}(|\mathcal S|-t)\\
 &\ge bd_{r+1}t.
\end{aligned}
\tag{4.6}

By (4.2),

\[
 t\le \frac{B_{\rm bad}}{b\min(d_r,d_{r+1})}
 =O\left(\frac{NH}{b\min(d_r,d_{r+1})}\right).
\tag{4.7}
\]

The deficiency form of Hall's theorem says that the maximum number of
unmatched vertices on the smaller side is the maximum such `t`.  Remainder
blocks cost `O(1)`, proving (4.3).  Equations (4.4)--(4.5) are immediate.
\(\square\)

### Interpretation

Theorem 4.1 is already at the exact recursive leave scale.  It says that
**one** adjacent-rank Gray seam is not a matching obstruction if each
length-`b` child block supplies `b` independently selectable ports.  It is
also robust against completely adversarial collars and completely arbitrary
block contents.

What it does not do is choose the two ports of the same child block
coherently.  In a four-block Gray braid, a child participates in two seams,
and its chosen incoming and outgoing ports must be the actual two ends of
one retained long path segment.  Applying Theorem 4.1 independently to the
four adjacent pairs may choose incompatible ports.  Thus the live local
problem is now sharply separated:

* fixed endpoint families are false by Theorem 2.1;
* one seam with many-choice blocks is solved by Theorem 4.1;
* the remaining theorem is a **two-port, four-partite compatibility
  matching**, not endpoint abundance for one containment graph.

## 5. The regular two-port problem has an exact solution

There is a clean positive theorem once the four contracted seam graphs are
regular.  This is the fixed-uniformity core which the recursive construction
should aim to instantiate.

Let `\mathcal C_0,\ldots,\mathcal C_3` be four block families of the same
size `J`, cyclically indexed.  Every block has a cyclically ordered list of
`b` possible ports.  Assume the following **two-port rerouting property**:
whenever two ports have cyclic distance at least `H` in both directions,
the whole block has a spanning physical child path, using every owner of the
block once, with those two ports as its ordered endpoints and with clean
`H`-collars there.  A single fixed cycle does not by itself have this
property: cutting it at two ports and retaining one cyclic arc would lose
the complementary arc.

For each `i`, let `G_i` be a `D_i`-regular bipartite
multigraph from `\mathcal C_i` to `\mathcal C_{i+1}`.  An edge records a
valid adjacent-rank containment and records one port at each endpoint.
Assume that, at every endpoint block, every one of its `b` ports occurs on
exactly `D_i/b` incident edges of `G_i` (and analogously on the other side).
Parallel edges are allowed.

Mark an arbitrary set `\mathcal B_i\subseteq E(G_i)` of dirty collar
incidences.

### Theorem 5.1 -- regular four-seam two-port resolution

There are perfect matchings `M_i\subseteq G_i` such that, after deleting

* every selected dirty seam, and
* every block whose selected incoming and outgoing ports have cyclic
  distance less than `H` in either direction,

the remaining four-layer graph is a disjoint union of physically
long-collar Gray paths and cycles.  The total number of deleted blocks and
selected dirty seams is at most

\[
 \boxed{
 \sum_{i=0}^3\frac{|\mathcal B_i|}{D_i}
 +\frac{8HJ}{b}.
 }
\tag{5.1}
\]

Deleting the bad objects increases the final path-component ledger by at
most a constant multiple of (5.1).

#### Proof

By König's line-colouring theorem, each `D_i`-regular bipartite
multigraph is the disjoint union of `D_i` perfect matchings.  Choose one of
these perfect matchings uniformly, independently for the four values of
`i`.

Every edge of `G_i` is selected with probability `1/D_i`.  Hence the
expected number of selected dirty edges is

\[
 |\mathcal B_i|/D_i.
\tag{5.2}
\]

At a fixed block, the selected incoming edge and selected outgoing edge
come from two independent random factor choices.  The port-balance
hypothesis makes each of their port labels uniform on the `b` cyclic
positions.  Therefore the probability that either oriented cyclic distance
between the two ports is less than `H` is at most

\[
 2H/b.
\tag{5.3}
\]

Summing (5.2)--(5.3) over four seam graphs and four block parts gives an
expected bad-object count bounded by (5.1).  Some deterministic four-tuple
of factor choices attains this bound.

Before deletion, the union of the four perfect matchings is a disjoint
union of cycles whose layer order is `0,1,2,3,0`.  At every retained block,
the two-port rerouting hypothesis supplies a spanning physical path with the
selected endpoints.  The seam edges are collar-clean, and the layer order
is exactly the Gray order.  Lemma 4.1 of the recursive-pair note therefore
makes every remaining concatenation physical through depth `H`.  Deleting
a bad block or seam cuts only a bounded number of these cycles, proving the
final component assertion. \(\square\)

### Corollary 5.2 -- the required asymptotic scale

Suppose `D_i=\Theta(bm)` and the collar charge has the natural bound

\[
 |\mathcal B_i|=O(JbH).
\tag{5.4}
\]

Then (5.1) is

\[
 O(JH/m)+O(JH/b).
\tag{5.5}

If `J=\Theta(N/b)`, `H=o(m)`, and

\[
 \boxed{b/H\longrightarrow\infty,}
\tag{5.6}

this is `o(N/H)` provided, for example, `H=O(\sqrt m)` and
`b=H\,\omega(1)` with `b=o(m)`.

Thus the two-port matching has no probabilistic loss once the blocks are
two-port reroutable and the contracted seam graphs are regular and
port-balanced.  The unresolved instantiation issues are exact:

1. construct two-port reroutable physical child blocks; and
2. make their contracted adjacent-rank incidence multigraphs admit regular
   port-balanced spanning subgraphs (or a fractional analogue which can be
   decomposed into perfect matchings).

The second item can in fact be removed for complete adjacent-rank
inclusion resources.  Exact regularity is obtained by a dummy completion.

### Theorem 5.3 -- automatic block regularization

Let two adjacent Boolean ranks of sizes \(N_-,N_+\) be partitioned into
the same number \(J\) of full blocks, of sizes

\[
 b_-=\lfloor N_-/J\rfloor,\qquad
 b_+=\lfloor N_+/J\rfloor,
\]

and one remainder of size less than \(J\) on each side.  Discard the two
remainders and contract the full blocks in the complete inclusion graph.
There is a regular bipartite multigraph completion of the contracted graph
with degree

\[
 \boxed{D=\Theta(bm),\qquad b=\min(b_-,b_+),}
\tag{5.7}
\]

using only

\[
 \boxed{O(Jm)}
\tag{5.8}

dummy parallel edges.  If a uniformly random one-factor of this regular
completion is selected, then

1. a real incidence edge is selected with probability \(1/D\);
2. a fixed real port is selected with probability \(O(1/b)\);
3. the expected number of selected dummy edges is \(O(J/b)\).

Consequently Theorem 5.1 remains valid without an assumed regular or
port-balanced subgraph, with the right side of (5.1) enlarged by only

\[
 \boxed{O(J/b).}
\tag{5.9}

#### Proof

Let \(d_-,d_+\) be the two inclusion degrees.  The full incidence count
is

\[
 T=N_-d_-=N_+d_+.
\]

Deleting the two remainders removes at most \(O(Jm)\) incidences.  Every
full block on the two sides has degree at most \(b_-d_-\) or \(b_+d_+\),
and each of these is at most \(T/J\) and differs from it by \(O(m)\).
Choose \(D\) to be the maximum real block degree.  The sums of the degree
deficits on the two sides are both \(JD-|E_{\rm real}|\), and

\[
 JD-|E_{\rm real}|=O(Jm).
\]

Pair the two multisets of deficit stubs arbitrarily.  The resulting dummy
parallel edges make the graph \(D\)-regular.  König's line-colouring
theorem decomposes it into \(D\) perfect matchings, so a uniformly selected
factor contains each edge with probability \(1/D\).

A real port is one Boolean set and is incident with at most \(m+O(1)\)
real inclusion edges.  Hence its selection probability is
\(O(m/D)=O(1/b)\).  Finally (5.8) divided by \(D=\Theta(bm)\) gives
(5.9).  \(\square\)

For arbitrary \(H\)-collars, the total number of dirty real incidences in
one seam graph is \(O(NH)\).  Theorem 5.3 therefore gives the completely
explicit four-seam loss

\[
\boxed{
 O(J/b)+O(JH/m)+O(JH/b).}
\tag{5.10}
\]

Here the three terms are respectively dummy selections, dirty collars, and
too-close incoming/outgoing ports.  If \(b/H\to\infty\), \(H=o(m)\), and
\(J=\Theta(N/b)\), then both the component cost and the \(H\)-fold crossing
window loss from (5.10) are \(o(N/H)\) and \(o(N)\), respectively.

Thus after packetization the matching uniformity is genuinely independent
of \(H\): it is four ordinary bipartite one-factor choices (uniformity two),
or a fixed four-layer cycle resolution if packaged together.  No
growing-\(H\) codegree estimate remains.  The only unresolved local input
is now the two-port spanning reroute itself.

## 6. Exact status

Proved here:

* the `O(H/s)` global collar-deletion fraction (1.6);
* the critical `O(NH/s)` completely-bad-endpoint scale (1.7);
* the two-junta matching obstruction (2.7), with leave
  `(1/2-o(1))N/H` at endpoint density `1/H`.
* the arbitrary-block, arbitrary-collar one-seam matching theorem (4.3),
  whose leave is `o(N/H)` for block length `b\asymp H`.
* the regular, port-balanced four-seam theorem (5.1) for two-port reroutable
  blocks, including the exact `O(JH/m+JH/b)` loss ledger.
* automatic dummy regularization (5.7)--(5.10), removing the separate
  regular/port-balanced-subgraph hypothesis for complete inclusion resources.

Not proved here:

* that the two-junta families arise as the two endpoint sets of the specific
  recursive child path partitions under consideration;
* a simultaneous four-seam many-choice interior-cut matching;
* two-port reroutability of the actual child blocks;
* the long-collar Gray-seam resolution or constant one.

The first caveat is important: Theorem 2.1 refutes a theorem based only on
endpoint cardinality, collars, orientation, and global relabelling.  A
positive proof may still exploit additional structure of the actual child
paths.
