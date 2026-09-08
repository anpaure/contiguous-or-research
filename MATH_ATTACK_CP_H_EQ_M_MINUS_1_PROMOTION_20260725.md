# The depth \(H=m-1\) promotion gate: maximal-chain MTF traces

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, web input,
or unproved generic rounding theorem is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad H=m-1.
\]

At this depth the covering-prefix gate has an exact maximal-chain form.
There are only \(2m\) promotion fibres,

\[
 U_r=[2m]\setminus\{r\}\qquad(r\in[2m]),
\]

and a full useful state in the fibre \(U_r\) is exactly a permutation of
\(U_r\).  Its middle owner is the set of its first \(m\) letters.  A
distinct-owner promotion is exactly a move-to-front operation on a letter
currently after position \(m\).

Consequently, if one can choose one such permutation over every middle
owner so that

1. every nonempty proper mask is a prefix of at least one selected
   permutation; and
2. the selected permutations form \(p=o(W/m)\) promotion paths,

then the useful-prefix word has length

\[
 W+2(m-1)p=W+o(W).                                \tag{0.1}
\]

If there is one path per fibre, the reset toll is at most

\[
 2(m-1)(2m)=4m(m-1)=O(m^2)=o(W).                 \tag{0.2}
\]

The reduction is sound, but the required integral object is not proved or
refuted here.  It is much stronger than a Hamilton path in a Johnson graph
and much stronger than choosing maximal extensions of an SCD.  The exact
equivalent object is an all-ranks universal recency-word decomposition:
the length-\(m\) recent-letter windows must partition the middle layer,
and the recent-letter prefixes of every other length must cover every
other proper rank.

Two sharp warnings are proved.

* The ambient bridge degree gives no Hall expansion after one state per
  owner is selected.  In one top fibre an owner has
  \(m!(m-1)!\) maximal-chain states, whereas one selected state has only
  \(m-1\) promotion successors.
* Every promotion path all of whose owners contain one fixed coordinate
  has at most \(m\) vertices.  Hence every canonical fixed-core partition,
  including the natural "first missing coordinate" partition, needs
  \(\Omega(W/m)\) paths and cannot meet the strict \(o(W/m)\) target.

Thus the \(H=m-1\) route survives the reset and capacity audit, but only
through genuinely noncanonical, exponentially long move-to-front traces
whose owners have no persistent core.  Canonical Gray/SCD grouping and
ordinary degree/Hall arguments do not prove it.

## 1. Exact maximal-chain representation

At \(H=m-1\), a full radius-\(H\) useful state is

\[
 \omega=(L;z_1,\ldots,z_{2m-2};R),
 \qquad |L|=|R|=1.                                \tag{1.1}
\]

Write

\[
 L=\{\ell\},\qquad R=\{r\},
\]

and define

\[
 p(\omega)=(p_1,\ldots,p_{2m-1})
 =(\ell,z_1,\ldots,z_{2m-2}).                    \tag{1.2}
\]

Then \(p(\omega)\) is a permutation of

\[
 U_r=[2m]\setminus\{r\}.                         \tag{1.3}
\]

The useful prefixes are exactly

\[
 P_k(\omega)=\{p_1,\ldots,p_k\}
 \qquad(1\le k\le2m-1),                          \tag{1.4}
\]

and the middle owner is

\[
 X(\omega)=P_m(\omega).                          \tag{1.5}
\]

Conversely, every permutation of one \(U_r\) defines one full useful
state by (1.1)-(1.2).  Thus selecting one state over a middle owner \(X\)
means choosing

* a residual coordinate \(r\notin X\);
* an ordering of \(X\); and
* an ordering of \(U_r\setminus X\).

For fixed \((X,r)\), the number of such states is

\[
 \boxed{F_m=m!(m-1)!.}                             \tag{1.6}
\]

Condition (i) in Section 0 is exactly

\[
 \boxed{
 \{P_k(\omega_X):X\in\tbinom{[2m]}m\}
 \supseteq\tbinom{[2m]}k
 \quad(1\le k\le2m-1).}                          \tag{1.7}
\]

There is no scalar shortage: at every rank \(k\), the number of selected
states is \(W\), while \(\binom{2m}{k}\le W\).

Condition (1.7) alone is feasible.  Indeed, take any Boolean SCD.  Every
one of its chains has one middle owner, and extend it arbitrarily downward
to a singleton and upward to a coatom.  The resulting \(W\) maximal
proper chains cover every nonempty proper mask.  This observation proves
only coverage; it gives no promotion chronology.

## 2. Promotion is exactly move-to-front

Fix a source permutation

\[
 p=(p_1,\ldots,p_{2m-1})
\]

of \(U_r\).  The bridge classification says that a promotion chooses the
unique element \(x=p_1\) of the lower block and one singleton \(z_j\).
The middle owner changes exactly when \(j>H=m-1\), equivalently when

\[
 b:=z_j=p_{j+1}
\]

lies strictly after position \(m\).  The target permutation is

\[
 \boxed{
 M_b(p)=(b,p_1,\ldots,p_j,p_{j+2},\ldots,p_{2m-1}).} \tag{2.1}
\]

This is literally move-to-front.  It preserves \(U_r\), and its middle
owner is

\[
 X(M_b(p))=X(p)-p_m+b.                            \tag{2.2}
\]

Hence a selected state has exactly

\[
 \boxed{m-1}                                      \tag{2.3}
\]

distinct-owner promotion successors, one for each coordinate in
\(U_r\setminus X\).  They all delete the same scheduled coordinate
\(p_m\).

For comparison, the full bridge graph also has one rotor successor owner
obtained by inserting the residual coordinate \(r\); that move changes
the top and is excluded from a promotion-only path.  Thus the
owner-changing bridge degree \(m\) at \(H=m-1\) splits as

\[
 (m-1)\text{ promotions}+1\text{ rotor direction}. \tag{2.4}
\]

### Proposition 2.1 (exact fibre-to-fibre arc count)

Let \(X,Y\subset U_r\) be adjacent middle owners, and write

\[
 X-Y=\{a\},\qquad Y-X=\{b\}.
\]

The number of promotion arcs from the full-state fibre over \(X\) to the
full-state fibre over \(Y\) is exactly

\[
 \boxed{((m-1)!)^2.}                               \tag{2.5}
\]

#### Proof

The source permutation must have \(a\) in position \(m\), while the
other \(m-1\) elements of \(X\) may be ordered freely in the first
\(m-1\) positions.  Its final \(m-1\) positions are an arbitrary
ordering of \(U_r\setminus X\), which contains \(b\).  Moving that copy
of \(b\) to the front produces the unique target state.  The two free
orders give (2.5). \(\square\)

Although (2.5) is large, its ratio to the source-fibre size is only

\[
 {((m-1)!)^2\over m!(m-1)!}={1\over m}.           \tag{2.6}
\]

More importantly, after a transversal chooses one target state over each
owner, a fixed source state has only the \(m-1\) literal successors in
(2.3), among \(F_m\) possible states at each target owner.  A uniformly
chosen target transversal therefore has expected selected successor count

\[
 {m-1\over F_m}=o(1).                              \tag{2.7}
\]

This is the precise degree-collapse hidden by the ambient formula
\(1+m^2-H^2=2m\).  At \(H=m-1\), that formula consists of identity,
same-owner promotions, distinct-owner promotions, and one rotor direction;
it is not a Hall degree on the selected owner transversal.

## 3. Exact word/window form of a promotion path

Let

\[
 p^{(0)}\longrightarrow p^{(1)}\longrightarrow\cdots
 \longrightarrow p^{(s-1)}                              \tag{3.1}
\]

be a promotion path in one top \(U_r\).  Let \(b_i\) be the coordinate
moved to the front in the transition \(p^{(i)}\to p^{(i+1)}\).
Because \(b_i\) lies after position \(m\), it is not in the current
owner.

After the harmless initial prefix is included in the notation, there is a
word

\[
 w=w_1w_2\cdots w_{s+m-1}\qquad(w_i\in U_r)       \tag{3.2}
\]

such that

\[
 \boxed{
 X_i=\{w_i,w_{i+1},\ldots,w_{i+m-1}\}
 \quad(0\le i<s),}                                \tag{3.3}
\]

and every length-\(m\) block in (3.2) has distinct letters.  The next
letter \(w_{i+m}\) is outside the current block, so (3.3) changes by one
Johnson exchange.

Conversely, every word satisfying this distinct-window rule lifts to a
promotion path: order the initial owner in reverse chronological order,
put the other \(m-1\) letters of \(U_r\) behind it in any order, and at
each step move the next word letter to the front.  It is outside the first
\(m\) positions exactly when required.

For every nonboundary state and \(k\le m\), its rank-\(k\) prefix is the
set of its \(k\) most recently moved letters.  In the word notation this
is a consecutive \(k\)-block:

\[
 \boxed{
 P_k(p^{(i)})
 =\{w_{i+m-k},\ldots,w_{i+m-1}\}.}                \tag{3.4}
\]

For \(k>m\), the prefix is the current owner together with the first
\(k-m\) letters of the move-to-front cache.  Equivalently, its complement
consists of the fixed residual \(r\) and the \(2m-1-k\) least recently
used letters of \(U_r\).

Thus the full \(H=m-1\) problem is an all-ranks recency design, not merely
a middle-level Gray code.

### Theorem 3.1 (exact universal-recency reformulation)

The construction in Section 0 exists if and only if there are promotion
words \(w^{(1)},\ldots,w^{(p)}\), each omitting one fixed residual
coordinate \(r_j\), such that:

1. every length-\(m\) window has distinct letters;
2. the sets of all length-\(m\) windows, over all words, are exactly
   \(\binom{[2m]}m\), each once;
3. the recency prefixes of the induced MTF permutations cover
   \(\binom{[2m]}k\) for every \(1\le k\le2m-1\); and
4. \(p=o(W/m)\).

#### Proof

Sections 1-3 send every promotion path to one such word.  Owner
transversality is exactly item 2, while useful-prefix coverage is exactly
item 3.  Conversely, lift every word by the construction after (3.4).
Its states are promotion-adjacent, its middle owners are the prescribed
windows, and its prefixes are precisely the prescribed recency sets.
Item 2 chooses one state per owner, and item 4 gives (0.1). \(\square\)

This theorem cleanly distinguishes the route from an ordinary universal
cycle for \(m\)-subsets.  A universal \(m\)-window word would address
items 1-2 in one top.  It would not by itself prove the simultaneous
prefix coverage in item 3, especially on the upper side where least-recent
cache order matters.

## 4. A sharp fixed-core obstruction

Canonical chain and first-missing-coordinate partitions group many owners
which share a persistent core.  Promotion chronology is incompatible with
long paths of that form.

### Lemma 4.1 (complete eviction in \(m\) moves)

Let \(p^{(0)}\to\cdots\to p^{(m)}\) be \(m\) consecutive promotion
moves at \(H=m-1\).  Every coordinate in the initial owner
\(X(p^{(0)})\) is absent from at least one of the later owners
\(X(p^{(1)}),\ldots,X(p^{(m)})\).

#### Proof

A move-to-front operation on a letter after position \(m\) shifts every
letter currently in the first \(m\) positions one position to the right,
except for letters which have already left that prefix.  Therefore the
initial letters in positions

\[
 m,m-1,\ldots,1
\]

leave the middle prefix in this order during the first \(m\) moves.  A
letter may later be moved back to the front, but at the state immediately
after its exit it is absent from the owner. \(\square\)

### Corollary 4.2 (fixed-core path bound)

If every owner on a promotion path contains one fixed coordinate, then the
path has at most \(m\) vertices.  More generally, the same conclusion
holds whenever all owners lie in any family with nonempty common
intersection.

#### Proof

A path with \(m+1\) vertices contains \(m\) consecutive moves.  Apply
Lemma 4.1 to the asserted common coordinate. \(\square\)

Now color each middle owner \(X\) by its first missing coordinate in a
fixed linear order.  The color-\(r\) class consists of owners which omit
\(r\) and contain every smaller coordinate.  Except for the first class,
it has a nonempty fixed core.  By Corollary 4.2, partitioning these classes
into promotion paths uses at least

\[
 {W-O(\binom{2m-1}{m})\over m}
\]

paths in any version in which a positive fraction of the owners remains in
fixed-core classes.  In particular every fixed-core decomposition of
\(\Theta(W)\) owners requires \(\Omega(W/m)\) paths, not
\(o(W/m)\).

The important point is structural, not the particular first-missing rule:
an admissible solution must mix every coordinate into and out of almost
every long component.  It cannot inherit a persistent base set from an
SCD template, a lexicographic top assignment, or a fixed-core cube.

## 5. First-band consequence of any successful construction

Let a selected promotion path contain consecutive owners \(X\to Y\).  If
the source permutation is \(p\), then (2.2) gives

\[
 P_{m-1}(p)=X\cap Y.                               \tag{5.1}
\]

The target's rank-\((m+1)\) prefix is

\[
 P_{m+1}(M_b(p))=X\cup Y.                         \tag{5.2}
\]

Thus a \(p\)-path solution gives a Johnson linear forest with \(W-p\)
edges.  The full-prefix cover contains every lower and upper first-band
color.  Since

\[
 N_1=\binom{2m}{m-1}={m\over m+1}W,              \tag{5.3}
\]

the total duplicate excess among the selected lower first-band prefixes is

\[
 W-N_1={W\over m+1},                              \tag{5.4}
\]

and the same holds above the middle.

Delete all but one forest edge carrying each repeated lower color, then do
the same for the upper colors.  At most \(2W/(m+1)\) edges are deleted.
Therefore:

### Proposition 5.1 (quantitative two-sided-rainbow shadow)

Every successful \(H=m-1\) construction with \(p\) promotion paths
contains a two-sided-rainbow Johnson linear subforest with at least

\[
 \boxed{
 W-p-{2W\over m+1}}                               \tag{5.5}
\]

edges.  In particular, the desired \(p=o(W/m)\) would imply a
two-sided-rainbow linear forest with

\[
 W-(2+o(1)){W\over m}                             \tag{5.6}
\]

edges.

This does not contradict the obvious rank capacity \(N_1\), but it is much
stronger quantitatively than the presently proved unparameterized
\(W-o(W)\) two-sided-rainbow forest.  Any proof of the maximal-chain route
must therefore solve a sharp first-band matching problem before its
all-depth benefits can be used.

## 6. All-depth window identities

The first-band statement has an exact higher-depth analogue.  Along a
promotion path, for every \(q\le m-1\) and every start having \(q\)
successive arcs available,

\[
 P_{m-q}(p^{(i)})
 =\bigcap_{j=0}^{q}X(p^{(i+j)}).                  \tag{6.1}
\]

This is immediate from the length-\((m-q)\) window formula (3.4).  The
upper prefix remains the literal MTF-cache prefix; it is not generally the
union of \(q+1\) consecutive owners because a cached coordinate may be
promoted after a shorter absence.

If there are \(p\) paths, at most \(qp\) states lie within \(q\) positions
of a terminal boundary.  Hence almost every selected lower depth-\(q\)
prefix is forced by a \((q+1)\)-owner window.  In particular a solution
must hit every rank-\((m-q)\) mask by these windows except for at most
\(qp\) masks which can be supplied by boundary completions.

At \(p=o(W/m)\), this boundary allowance is \(o(qW/m)\).  Thus the
proposal is a simultaneous path-hitting theorem through all depths, not a
rank-by-rank extension problem.

## 7. What remains possible

None of the proved obstructions bounds an owner-simple promotion path in a
top \(U_r\) by a polynomial length.  Such a path is a distinct-window word
over an alphabet of size \(2m-1\), and in principle it may contain an
exponential number of the \(\binom{2m-1}{m}=W/2\) owners available in that
top.  Therefore the fixed-core lemma does not refute the noncanonical
route.

The clean remaining theorem is the following.

> **Maximal-chain promotion theorem \((\mathrm{MCP}_{m-1})\).** Partition
> all middle owners into \(o(W/m)\) distinct-window words, each word
> omitting one fixed residual coordinate, so that the associated MTF
> recency permutations cover every nonempty proper mask as a prefix.

By Theorem 3.1 and (0.1), this theorem implies a \(W+o(W)\) contiguous-OR
construction.

A useful two-stage attack would be:

1. first construct a promotion-word partition of all middle owners with
   \(o(W/m)\) paths; and
2. strengthen the word choice so that all recent and least-recent prefix
   sets cover their ranks.

Even stage 1 is not an ordinary Johnson Hamilton decomposition.  The
departing coordinate is the oldest member of an ordered FIFO middle
window, and every component must omit one fixed coordinate.  Stage 2 is
strictly stronger still.

## 8. Audit ledger

### Proved

1. At \(H=m-1\), full useful states are maximal proper chains, equivalently
   permutations of one coatom \(U_r\).
2. Promotion is exactly move-to-front from after the middle position and
   preserves \(U_r\).
3. One selected state has only \(m-1\) promotion successors, despite the
   larger ambient bridge-degree formula.
4. Promotion paths are exactly distinct length-\(m\)-window words, with
   lower flags equal to recent-letter windows and upper flags equal to
   recency-cache prefixes.
5. The desired construction is exactly the all-ranks universal-recency
   theorem in Theorem 3.1.
6. A coordinate common to every owner limits a promotion path to at most
   \(m\) vertices.  Hence fixed-core and first-missing-coordinate
   decompositions cannot reach \(o(W/m)\) paths.
7. Any solution forces the quantitative two-sided-rainbow subforest
   (5.5), and the higher-depth window identities (6.1).
8. With \(p=o(W/m)\), the reset toll is \(o(W)\); with one path per top it
   is only \(O(m^2)\).

### Not proved

1. A promotion-word partition of all middle owners into \(o(W/m)\)
   owner-simple paths.
2. Simultaneous lower and upper prefix coverage along such paths.
3. Therefore \((\mathrm{MCP}_{m-1})\) and coefficient one by this route.

The new depth removes every Gaussian top-count obstruction.  What remains
is a genuinely global universal-cycle problem with recency order, and the
free choice of maximal-chain extensions is exactly the freedom it uses.
