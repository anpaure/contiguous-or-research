# Proportional atoms: the vertical-absorption split fails on the central ladder

Date: 2026-07-25

This note audits the proposed two-stage inference

1. absorb all interval pairs with \(a+c=1\) by an exact nested
   Hall/symmetric-chain flow;
2. round physical long-row bundles using only the alleged residual
   \(a+c\ge2\) overlap, whose normalized row sum is \(O(m^{-2})\).

The numerical \(O(m^{-2})\) estimate is correct after literally deleting
**every** \(a+c=1\) slot pair.  The proposed decomposition is nevertheless
invalid.  Same-start vertical chains delete only one of the two adjacent
Boolean parents of a central interval.  The other parent joins consecutive
starts and retains normalized codegree \((1+o(1))/m\).  If both parents are
absorbed, their transitive closure is the entire physical atom, leaving no
independent columns to round.

## 1. The tail with \(a+c\ge2\)

For designated intervals \(P,Q\), put

\[
 a=|P\setminus Q|,\qquad c=|Q\setminus P|.
\]

The exact conditional probability calculation gives the row-sum majorant

\[
 \sum_{a+c\ge1}
 \frac{(a+c+1)^2}{\binom r a\binom{n-r}c},
 \qquad r,n-r=m+o(m).
\tag{1.1}
\]

The terms \((a,c)=(1,0),(0,1)\) have order \(m^{-1}\).  After deleting
them, the three smallest denominators are

\[
 \binom r2,\qquad r(n-r),\qquad\binom{n-r}2,
\]

and all are \(\Theta(m^2)\).  Successive terms have ratio \(o(1)\)
uniformly through \(a,c\le b+2H=o(m)\).  Hence

\[
 \boxed{
 \sum_{a+c\ge2}
 \frac{(a+c+1)^2}{\binom r a\binom{n-r}c}
 =O(m^{-2}).}
\tag{1.2}
\]

Thus the numerical tail claimed in the proposed inference is sound.  The
question is whether an exact chain flow actually removes all of the two
terms excluded from (1.2).

## 2. Exact central first-collision identity

At ranks \(m\) and \(m+1\), the proportional profile has
\(b_0=b_1=b\).  Consequently every start occurs in both ranks.  Write the
position intervals

\[
 P_j=[j,j+m-1],\qquad Q_j=[j,j+m],
 \qquad 0\le j<b.
\tag{2.1}
\]

There are two distinct \(a+c=1\) containments:

\[
 P_j\subset Q_j
 \quad\hbox{(same-start/right extension)},
\tag{2.2}
\]

and

\[
 P_j\subset Q_{j-1}\quad(1\le j<b)
 \quad\hbox{(adjacent-start/left extension)}.
\tag{2.3}
\]

The multiradius symmetric chain at start \(j\) uses (2.2).  It does not
absorb (2.3).

### Proposition 2.1 (the surviving first collision)

Let \(v\) be an \(m\)-set and \(w\) an \((m+1)\)-set with \(v\subset w\).
In the labelled proportional-atom multihypergraph,

\[
 \boxed{
 \frac{\deg(v,w)}{\deg(v)}
 =\frac{2b-1}{b(m+1)}.}
\tag{2.4}
\]

Of this quantity, the same-start pairs (2.2) contribute exactly

\[
 \frac1{m+1},
\tag{2.5}
\]

and the adjacent-start pairs (2.3) contribute exactly

\[
 \boxed{
 \frac{b-1}{b(m+1)}=\frac{1+o(1)}m.}
\tag{2.6}
\]

#### Proof

Let \(D\) be the number of labelled injective words in which the coordinate
set on one specified interval \(P_j\) is \(v\).  It is independent of
\(j\).  Equal-length distinct intervals in an injective word give distinct
sets, so the events that \(v\) occupies the \(b\) central slots are
disjoint.  Therefore

\[
 \deg(v)=bD.
\tag{2.7}
\]

Conditioned on \(v\) occupying \(P_j\), a prescribed one-element extension
\(w\) occupies either containing interval with exact probability

\[
 \frac1{\binom m0\binom{m+1}1}=\frac1{m+1}.
\tag{2.8}
\]

For every \(j\), the same-start interval \(Q_j\) is available.  For
\(1\le j<b\), the adjacent-start interval \(Q_{j-1}\) is also available.
The two events are disjoint because their added position coordinates are
distinct.  There are therefore \(b+(b-1)=2b-1\) contributing ordered slot
pairs, each with \(D/(m+1)\) completions.

There are no other contributions: since \(|v\cap w|=m\), the position
intervals must have intersection size \(m\), hence the length-\(m\)
interval must be contained in the length-\((m+1)\) interval.  Equations
(2.4)--(2.6) follow. \(\square\)

Thus contracting or exactly matching the same-start vertical chain removes
(2.5) but leaves (2.6).  The residual conditional overlap is still
\(\Theta(1/m)\), not \(O(m^{-2})\).

## 3. Absorbing both parents collapses the atom

Let \(G_{\mathrm{slot}}\) be the graph whose vertices are all designated
slots of one proportional atom and whose edges join interval pairs with
\(a+c=1\).

### Proposition 3.1 (central-ladder connectedness)

The graph \(G_{\mathrm{slot}}\) is connected.

#### Proof

The central slots contain the alternating path

\[
 P_0-Q_0-P_1-Q_1-\cdots-P_{b-1}-Q_{b-1}.
\tag{3.1}
\]

Indeed \(P_j\subset Q_j\), and \(P_{j+1}\subset Q_j\) for
\(0\le j<b-1\).  Hence all \(2b\) central slots lie in one component.

Under the proportional multiradius profile, if start \(i\) has radius
\(d\), its designated ranks are the consecutive interval

\[
 -d,-d+1,\ldots,d+1.
\]

Successive same-start slots differ by one position coordinate, so every
noncentral designated slot connects vertically to \(P_i\) or \(Q_i\).
Thus every slot lies in the central component. \(\square\)

There is consequently an exact dichotomy.

* If stage one contracts only the same-start symmetric chains, the
  adjacent-start contribution (2.6) remains, and the input to stage two is
  still an \(O(1/m)\) overlap system.
* If stage one absorbs the complete \(a+c=1\) relation, Proposition 3.1
  makes the absorbed component one whole atom.  Selecting compatible
  components is then the original physical-row problem, not a lower-rank
  residual rounding problem.

## 4. Why quotienting does not repair the inference

Contracting a same-start chain to a formal column vertex changes the
resource system.  Two distinct formal chains can contain the same Boolean
target, so disjointness of formal chain labels does not imply disjointness
of the original atom edges.  One must do one of the following.

1. Retain every Boolean target capacity.  Then the original
   \(\Theta(1/m)\) first-collision cliques, including (2.6), remain.
2. First choose a vertex-disjoint chain pool, for example from a symmetric
   chain decomposition.  Then candidate rows must be restricted to bundles
   lying entirely in that pool.  The unconditioned labelled degree and
   codegree calculations no longer apply: an arbitrary exact chain pool
   need not contain a regular, or even nonempty, family of long physical
   rows.

This is a conditioning issue, not a parallel-word bookkeeping issue.  The
\(O(m^{-2})\) estimate (1.2) is averaged over unrestricted injective words.
Exact prior selection of all vertical chain successors can make the
conditional physical-row degree zero for some columns and can make the
remaining compatibility deterministic for others.  No inequality in the
proportional-atom note bounds these conditioned degrees.

An equivalent way to see the problem is that a symmetric-chain flow chooses
one upper successor of a central \(m\)-set.  A tight row simultaneously
contains the two-parent diamond

\[
 P_j\subset Q_j\supset P_{j+1}.
\tag{4.1}
\]

The left edge of (4.1) can be declared vertical, but the right edge then
couples two nominal columns.  Choosing both edges coherently along (3.1)
is precisely the physical FIFO row law that stage two was meant to prove.

## 5. Audited conclusion

The inference

\[
 \text{exact SCD/Hall absorption of }a+c=1
 \quad+\quad O(m^{-2})\text{ residual overlap}
 \quad\Longrightarrow\quad
 p-o(p/\sqrt m)\text{ physical atoms}
\]

is invalid.

The first exact unsuppressed collision is already the central
adjacent-start pair (2.3), with normalized mass (2.6).  Eliminating that
pair as well makes the entire slot system connected and therefore assumes
the common physical row compatibility rather than deriving it.  A valid
two-stage theorem would need a new **row-compatible chain-flow lemma**:
it must choose the exact nested chain pool while simultaneously preserving
near-regular conditioned degrees of complete tight rows.  Neither Boolean
Hall/SCD feasibility nor the unrestricted \(O(m^{-2})\) tail proves such a
lemma.
