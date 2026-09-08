# Three-level saturation: the opposite-colour gate and a linear GJM obstruction

Date: 2026-07-26

## 0. Verdict

Let

\[
 n=2m+1,\qquad
 W=\binom{n}{m},\qquad
 N=\binom{n}{m-1}=\frac{m}{m+2}W,
 \qquad d=W-N=\frac{2W}{m+2}.
\]

A saturating cycle in the three levels (m-1,m,m+1) does project to a
Hamilton cycle on all (W) middle (m)-sets.  At every projected edge it
certifies **one** of the two colours (intersection or union), and all the
certified colours are distinct.  The exact total two-sided missing count is

\[
 \boxed{M^-+M^+=N-|Z\setminus Y|,}                    \tag{0.1}
\]

where (Y) is the set of the (W) certified outer vertices and (Z) is
the multiset of the opposite colours.  Thus the desired conclusion is
equivalent to the additional assertion

\[
 \boxed{|Z\setminus Y|=N-o(W).}                       \tag{0.2}
\]

Corollary 2 of Gregor--Mička--Mütze supplies no estimate of (0.2).

For the explicit Gregor--Jäger--Mütze--Sawada--Wille (GJM) middle-four-level
lexical construction there is a sharper negative result.  Its
lower-colour-perfect contracted Johnson forest has duplicate upper-colour
excess at least

\[
 \boxed{
 \delta_m\ge \binom{2m-1}{m-2}
 =\left(\frac14-o(1)\right)W.}                        \tag{0.3}
\]

Consequently that forest misses a linear fraction of the upper colours.
The local six-cycle operations used in the published Hamiltonicity proof
lie entirely in the upper two levels, so they do not alter this lower
lexical forest.  Therefore the published four-level construction cannot be
projected to the requested two-sided q=1 owner cycle while retaining all but
(o(W)) of its lower-contraction edges.  It would require a genuinely
linear-size rerouting.

This does **not** disprove the existence of some specially constructed
three-level saturating cycle satisfying (0.2).  It proves that neither the
abstract three-level Corollary nor the direct GJM lexical projection gives
it for free.

## 1. Exact projection of a three-level saturating cycle

In the graph induced by levels (m-1,m,m+1), the bipartition class formed
by rank (m) has size (W), while the other class has size (W+N).
Hence a saturating cycle has the form

\[
 X_0,Y_0,X_1,Y_1,\ldots,X_{W-1},Y_{W-1},X_0,          \tag{1.1}
\]

where the (X_i)'s are all (m)-sets and the (Y_i)'s are (W) distinct
sets, each of rank (m-1) or (m+1).

Put

\[
 R_i=X_i\cap X_{i+1},
 \qquad U_i=X_i\cup X_{i+1}.                          \tag{1.2}
\]

If (Y_i) has rank (m-1), then (Y_i\subset X_i,X_{i+1}), and the two
middle sets are distinct, so

\[
 Y_i=R_i,qquad |R_i|=m-1,qquad |U_i|=m+1.            \tag{1.3}
\]

If (Y_i) has rank (m+1), the dual argument gives (Y_i=U_i).
In either case (X_i,X_{i+1}) are Johnson adjacent.  Therefore (1.1)
projects to a Hamilton cycle of (J(n,m)).

Define its certified and opposite outer colours by

\[
 (Y_i,Z_i)=
 \begin{cases}
 (R_i,U_i),&|Y_i|=m-1,\\
 (U_i,R_i),&|Y_i|=m+1.
 \end{cases}                                          \tag{1.4}
\]

The (Y_i)'s are pairwise distinct by simplicity of the saturating cycle.
No corresponding assertion holds for the (Z_i)'s.

Let

\[
 {\cal O}=\binom{[n]}{m-1}\ \dot\cup\ \binom{[n]}{m+1}.
\]

The signed first-shadow targets present in the projected owner cycle are
exactly (Y\cup Z), where (Y=\{Y_i\}) and (Z=\{Z_i\}), with (Z)
understood through its distinct support.  Since (|{\cal O}|=W+N) and
(|Y|=W),

\[
 \begin{aligned}
 M^-+M^+
 &=|{\cal O}\setminus(Y\cup Z)|\\
 &=W+N-\bigl(W+|Z\setminus Y|\bigr)\\
 &=N-|Z\setminus Y|.
 \end{aligned}                                        \tag{1.5}
\]

This proves (0.1).

Equivalently, define the opposite-colour waste

\[
 \Omega=W-|Z\setminus Y|.                             \tag{1.6}
\]

There are only (N) outer targets outside (Y), so the forced minimum is
(Omega\ge W-N=d), and

\[
 \boxed{M^-+M^+=\Omega-d.}                            \tag{1.7}
\]

Thus three-level saturation pays the injectivity of (Y) exactly, but
merely relocates the two-sided problem to the opposite-colour waste.

### Sign-count form

If (a) transitions use lower vertices and (b) use upper vertices, then

\[
 a+b=W,qquad a\le N,qquad b\ge d.                   \tag{1.8}
\]

If the cycle uses every lower vertex, then (a=N,b=d), its lower ledger is
perfect, and (0.2) says precisely that the unions on the other transitions
must add (N-o(W)) new upper colours.  At the opposite extreme, every
middle-level Hamilton cycle between ranks (m,m+1) is an all-upper witness
to the three-level saturating theorem; then (0.2) is exactly the unproved
near-cover statement for its lower intersections.  This shows directly why
the abstract Corollary cannot supply the missing estimate.

## 2. Tight enumeration does not remove the gate

The same Corollary also supplies a tight enumeration, but it is not an
owner-cycle projection theorem.

### Lemma 2.1 (shape of a three-level tight enumeration)

Every tight enumeration of the three levels has exactly (N) transitions
between two outer-class vertices, each of Hamming distance two; all its
other transitions are cube edges between an outer vertex and a middle
vertex, and it has no middle--middle transition.

#### Proof

There are (W+N) outer vertices and (W) middle vertices.  In any cyclic
ordering, at least (N) adjacencies join two outer vertices.  Each such
transition has even positive Hamming distance and therefore costs at least
two flips; every cross-class transition costs at least one.  The definition
of tight enumeration allows exactly (N) flips above the number of listed
vertices.  Hence equality holds throughout: there are exactly (N)
outer--outer transitions, each of distance two, no middle--middle
transition, and every remaining transition has distance one.  \(□\)

Between consecutive middle vertices the enumeration may contain a run of
several outer vertices.  The two middle endpoints of such a run need not be
Johnson adjacent.  Even when they are, shortcutting the run requires one
outer vertex adjacent to both endpoints, which tightness does not force.
Thus the tight-enumeration half of Corollary 2 also does not imply (1.1) or
(0.2) without an additional local shortcut theorem.

## 3. The GJM lower lexical map

We now use the notation of the GJM construction in dimension (2m+1).
Suppressing every lower outer vertex (rank (m-1)) in the two lexical
matchings (M^m_{2m+1,m-1}\cup M^{m+1}_{2m+1,m-1}) gives a spanning linear
forest (F_-) on rank-(m) sets.  It has one edge for every

\[
 x\in L_{2m+1,m-1}:={x\in\{0,1\}^{2m+1}:|x|=m-1\}.
\]

Interpret (1) as an up-step and (0) as a down-step.  Since such an (x)
has (m+2) zeros and ends at height (-3), the extension (x^\uparrow) in
the lexical-matching definition equals (x) itself.  Scan its down-steps
row-wise from top to bottom and from right to left within a row.  The two
forest neighbours are obtained by flipping scan indices (m) and (m+1),
i.e. the last two down-steps in this order.  Consequently the upper union
colour of the contracted edge is the word

\[
 \psi(x)=x\text{ with those last two down-steps changed to up-steps}.
 \tag{3.1}
\]

Its duplicate excess is

\[
 \delta_m=|L_{2m+1,m-1}|-|\psi(L_{2m+1,m-1})|.         \tag{3.2}
\]

## 4. A linear family of disjoint lexical collisions

### Theorem 4.1

For every (m\ge2), the fibres of (psi) contain at least

\[
 \binom{2m-1}{m-2}                                    \tag{4.1}
\]

pairwise disjoint colliding pairs.  Hence (0.3) holds.

#### Proof

Take an arbitrary word

\[
 y\in\{0,1\}^{2m-1},\qquad |y|=m-2.                  \tag{4.2}
\]

Its lattice path ends at height (-3).  Let the displayed zero in

\[
 y=A,0,B                                             \tag{4.3}
\]

be the step at which the path first attains its global minimum, say height
(h).  Thus the path (A) ends at height (h+1); no earlier zero ends at
height (h); and the suffix (B), started at height (h), never goes below
(h).

Form

\[
 x=A,010,B,qquad x'=A,001,B.                     \tag{4.4}
\]

Both words have length (2m+1), weight (m-1), and hence index edges of
(F_-).

In (x=A010B), the first and third zeros of the displayed block both start
at height (h+1).  No zero starts lower.  Among all zeros starting at
height (h+1), these are the two leftmost: the first is the step that first
reaches height (h), while any return to (h) inside (B) occurs later.
Because equal-height steps are scanned from right to left, these two zeros
are exactly the last two steps in lexical order.

In (x'=A001B), the second displayed zero starts at height (h) and is the
unique zero starting that low; it is last in lexical order.  The first
displayed zero is the leftmost zero starting at height (h+1), so it is
second last.  Therefore (3.1) gives

\[
 \psi(x)=A,111,B=\psi(x').                           \tag{4.5}
\]

The pairs in (4.4) are disjoint as (y) varies.  Indeed, the two lexical
steps selected from a word are intrinsic.  In the (010) case they are the
two zeros at distance two, and in the (001) case they are the adjacent
zeros; these positions determine the displayed three-bit block and deleting
its final two positions recovers the unique word (y=A0B).

Thus (4.2) supplies (inom{2m-1}{m-2}) disjoint pairs in fibres of
(psi).  Every disjoint colliding pair lowers image size by at least one,
even if several pairs share the same image.  This proves (4.1) and (0.3).
\(□\)

The scale is explicitly

\[
 \frac{\binom{2m-1}{m-2}}{W}
 =\frac{m-1}{2(2m+1)}
 =\frac14+O(m^{-1}).                                  \tag{4.6}
\]

Since the forest has (N) edges, its number of missing upper colours is

\[
 (W-N)+\delta_m
 \ge \frac{2W}{m+2}+\binom{2m-1}{m-2}
 =\left(\frac14-o(1)\right)W.                         \tag{4.7}
\]

In particular, the earlier Catalan-size collision subfamily is only a
small subset of the hereditary first-minimum family above.

## 5. Consequence for the full four-level construction

A Hamilton cycle in four or more central levels has no direct Johnson
projection in the first place.  Between two consecutive visits to rank
(m), the cycle may make an excursion through ranks (m+1,m+2,ldots) (or
dually downward).  The two rank-(m) endpoints of an excursion of length
greater than two need not be Johnson adjacent.  Deleting all non-middle
vertices therefore produces a cyclic ordering of the middle owners, but not
in general a cycle of (J(n,m)).  A projection theorem would additionally
have to cut or reroute every non-Johnson excursion.  The abstract central
levels theorem contains no bound on the resulting number of breaks or on
their opposite colours.

For the explicit GJM four-level construction this general issue can be
sharpened as follows.

The GJM Hamilton cycle is obtained from its explicit cycle factor by
symmetric differences with selected six-cycles.  Those joining six-cycles
lie entirely between levels (m+1) and (m+2).  Hence the two lexical
matchings between levels (m-1) and (m), and therefore their contracted
forest (F_-), are unchanged in the final Hamilton cycle.

Any owner-cycle projection which retains all but (s) edges of (F_-)
still has upper duplicate excess at least

\[
 \delta_m-s.                                          \tag{5.1}
\]

Indeed, deleting one forest edge can reduce duplicate excess by at most
one, and adding connector edges cannot remove a duplicate among retained
edges.  By (0.3), achieving (o(W)) upper missing mass therefore forces

\[
 s\ge\left(\frac14-o(1)\right)W.                      \tag{5.2}
\]

Thus neither orienting the existing lower forest nor joining only its
(O(W/m))-scale component boundary can yield the desired two-sided q=1
cycle.  The direct GJM projection needs a linear rerouting, not a
Catalan-scale endpoint repair.

This conclusion is deliberately scoped.  A different three-level
saturating cycle may have small opposite-colour waste, and a projection
which discards a linear portion of the GJM lower forest is not ruled out.
What is ruled out is the hoped-for black-box implication from the published
three-/four-level constructions to a two-sided near-rainbow owner cycle.

## 6. Source interface

The two published facts used above are:

1. Gregor--Mička--Mütze, *On the central levels problem*, Corollary 2:
   every consecutive level interval has a saturating cycle and a tight
   enumeration, <https://tmuetze.de/papers/gmlc2.pdf>.
2. Gregor--Jäger--Mütze--Sawada--Wille, *Gray codes and symmetric chains*:
   the lower outer part uses the (m)- and ((m+1))-lexical matchings, and
   the six-cycles joining the factor lie entirely in the upper two levels,
   <https://arxiv.org/pdf/1802.06021>.
