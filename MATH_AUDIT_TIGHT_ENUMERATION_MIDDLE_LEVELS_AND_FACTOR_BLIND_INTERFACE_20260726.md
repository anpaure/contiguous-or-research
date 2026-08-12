# Tight enumerations, Middle Levels projection, complement symmetry, and the factor-blind compiler

Date: 2026-07-26

Scope: complete audit of the five literature/interface claims in the
latest note.

Primary sources checked:

* P. Gregor, O. Mička, T. Mütze,
  [*On the central levels problem*](https://arxiv.org/abs/1912.01566),
  Corollary 2.
* T. Mütze,
  [*Proof of the middle levels conjecture*](https://arxiv.org/abs/1404.4442).
* P. Gregor, T. Mütze, J. Nummenpalo,
  [*A short proof of the middle levels theorem*](https://arxiv.org/abs/1710.08249).

## 0. Verdict

The five claims divide as follows.

1. **Tight two-level enumeration:** correct.  For levels \(m-1,m\) in
   \(Q_{2m+1}\), tightness forces exactly \(W-N\) direct rank-\(m\)
   transitions, all of Hamming distance two, and contraction gives a
   Hamilton cycle of \(J(2m+1,m)\) covering every lower target.
2. **Literal OR interface:** not exact as stated.  The contracted cycle
   may use the same intersection facet on both sides of an owner.  The bad
   owners are, however, confined to endpoints of the direct transitions,
   so there are at most \(2(W-N)=O(W/m)\) of them.  Literal appending
   repairs the word at \(o(W)\) cost.  The separate saturating-cycle output
   actually gives the cleaner one-sided word of length \(W+1\).
3. **Middle Levels union projection:** correct.  Contracting the upper
   shore of a Middle Levels Hamilton cycle gives a Hamilton cycle of
   \(J(2m+1,m)\) whose adjacent unions are all \((m+1)\)-sets exactly once.
   It is a literal OR word of length \(W+1\) for ranks \(m,m+1\).
4. **Complement symmetry:** the proposed even-\(W\) edge-axis reflection
   is impossible for plain complementation.  No Middle Levels edge is
   fixed setwise by complement.  A complement-invariant Hamilton cycle can
   therefore exist only when
   \[
                         W=\binom{2m+1}{m}\ \text{is odd},
   \]
   equivalently \(m=2^a-1\), and complement must then act as the
   half-turn.  Even in that case it does not couple the missing lower
   \((m-1)\)-shadow to the already-perfect upper \((m+1)\)-shadow of the
   same projected owner cycle.
5. **SCD and factor-blindness:** an SCD partitions every rank exactly and
   supplies one nested flag per central chain.  It does not supply the
   required cyclic chronology.  The proved factor-blind compiler genuinely
   accepts non-wreath cycles of arbitrary length; it bypasses the wreath
   condition, but not the integral synchronization problem.  It still
   requires physical two-sided safety, small actual target deficit,
   negligible owner overload/leave, and \(o(W/H)\) components or safe cuts.

Thus the literature pays two exact one-sided central interfaces, one lower
and one upper, but in generally different cycles.  It does not prove their
simultaneous realization.

## 1. Tight enumeration of levels \(m-1,m\)

Work in \(Q_{2m+1}\), and put

\[
 W=\binom{2m+1}{m},\qquad
 N=\binom{2m+1}{m-1}={m\over m+2}W,
\]

\[
 E=W-N={2W\over m+2}.                                         \tag{1.1}
\]

Gregor--Mička--Mütze define a tight enumeration of a bipartite cube
subgraph to be a cyclic listing of every vertex whose total number of
flipped bits is the number of vertices plus the difference between the two
bipartition sizes.  Here that number is

\[
                         (W+N)+(W-N)=2W.                        \tag{1.2}
\]

Let \(a,b,c\) be the numbers of cross-rank, lower--lower, and
middle--middle adjacencies in the cyclic listing.  Counting the two cyclic
incidences at each listed vertex gives

\[
                         2N=a+2b,\qquad 2W=a+2c.                \tag{1.3}
\]

Every cross-rank step costs at least one flip, and every same-rank step
costs at least two.  Therefore

\[
 \text{total flips}\ge a+2b+2c=2W+2b.                         \tag{1.4}
\]

Tightness and (1.2) force equality throughout.

### Theorem 1.1 (forced-step projection)

Every tight enumeration of levels \(m-1,m\) in \(Q_{2m+1}\) has:

* no lower--lower adjacency;
* exactly \(2N\) cross-rank adjacencies, each a cube edge;
* exactly \(E=W-N\) middle--middle adjacencies, each of Hamming distance
  two.

Deleting every lower vertex from the cyclic listing gives a Hamilton cycle

\[
                         X_0X_1\cdots X_{W-1}X_0               \tag{1.5}
\]

of \(J(2m+1,m)\).  Every \((m-1)\)-set occurs at least once among

\[
                         B_i=X_{i-1}\cap X_i.                  \tag{1.6}
\]

#### Proof

Equation (1.4) forces \(b=0\), hence \(c=E\), and equality in every local
distance lower bound.  Thus a lower vertex is flanked by two incident
middle vertices, whose intersection is that lower vertex.  A direct
middle--middle pair differs in exactly two coordinates and is a Johnson
edge.  Deleting the lower vertices therefore gives (1.5), and every listed
lower vertex supplies one colour in (1.6). \(\square\)

This proves the first literature claim exactly.  It does **not** assert
that the additional \(E\) intersection occurrences are distinct or
balanced.

## 2. The precise literal OR interface

The word of intersection colours is

\[
                         B_0,B_1,\ldots,B_{W-1},B_0.            \tag{2.1}
\]

At owner \(X_i\), both \(B_i\) and \(B_{i+1}\) are facets of \(X_i\).
Consequently

\[
 B_i\ne B_{i+1}\quad\Longrightarrow\quad
                         B_i\cup B_{i+1}=X_i.                  \tag{2.2}
\]

Equality of the two facets is possible: three distinct owners in one
Johnson clique \(K_R\) give two consecutive cycle edges with the same
intersection \(R\).  Tightness does not rule this out.

Call \(X_i\) bad when \(B_i=B_{i+1}\).

### Theorem 2.1 (all literal failures lie at forced direct steps)

The number \(b_{\rm lit}\) of bad owners satisfies

\[
                         b_{\rm lit}\le2E={4W\over m+2}.        \tag{2.3}
\]

Hence there is a literal OR word of length

\[
                         W+1+b_{\rm lit}
                         \le W+1+{4W\over m+2}                 \tag{2.4}
\]

that covers every rank-\((m-1)\) and every rank-\(m\) target.

#### Proof

If neither of the two owner-cycle edges incident with \(X_i\) arose from a
direct middle--middle step, then both arose by suppressing two lower
vertices of the original enumeration.  Those two listed vertices are
distinct, so \(B_i\ne B_{i+1}\).  Thus every bad owner is incident with at
least one of the \(E\) direct transitions.  Each direct transition has two
endpoints, proving (2.3).

The word (2.1) contains every lower target as a letter.  By (2.2), it
realizes every good owner as the union of two consecutive letters.  Append
each bad owner once as a literal letter; concatenation preserves all
existing witnesses and proves (2.4). \(\square\)

This is the strongest automatic compiler statement from the tight
enumeration.  It is already coefficient one, but it is only one-sided.

There is also a cleaner route: the **separate** saturating cycle supplied
by the same Corollary projects to a length-\(N\) lower-rainbow owner cycle.
Its lower-colour word has length \(N+1\), and appending the \(E\) omitted
owners gives length

\[
                         N+1+E=W+1.                            \tag{2.5}
\]

Therefore the tight enumeration does not improve the one-sided literal
length unless one proves an additional distinct-facet theorem.

## 3. Middle Levels gives the exact upper projection

Now let \(C\) be any Hamilton cycle in the Middle Levels graph induced by
ranks \(m,m+1\) of \(Q_{2m+1}\).  Write it as

\[
 X_0,U_0,X_1,U_1,\ldots,X_{W-1},U_{W-1},X_0,                  \tag{3.1}
\]

where \(|X_i|=m\) and \(|U_i|=m+1\).  Then

\[
                         X_i\subset U_i\supset X_{i+1}.        \tag{3.2}
\]

The two rank-\(m\) neighbours of \(U_i\) are distinct facets, so

\[
                         U_i=X_i\cup X_{i+1}.                  \tag{3.3}
\]

### Theorem 3.1 (exact union projection)

The contraction

\[
                         X_0X_1\cdots X_{W-1}X_0              \tag{3.4}
\]

is a Hamilton cycle of \(J(2m+1,m)\), and its union colours are every
member of \(\binom{[2m+1]}{m+1}\), exactly once.

Consequently

\[
                         X_0,X_1,\ldots,X_{W-1},X_0            \tag{3.5}
\]

is a literal OR word of length \(W+1\) covering ranks \(m,m+1\) exactly.

This is an unconditional theorem-level interface from the Middle Levels
theorem.  Its lower intersections

\[
                         R_i=X_{i-1}\cap X_i                    \tag{3.6}
\]

are not controlled by Hamiltonicity.

### Rank-indexing table

\[
\begin{array}{c|c|c|c}
\text{ground}&\text{cube levels}&\text{projected owners}
 &\text{automatic colour ledger}\\ \hline
2m+1&m-1,m&m&\text{all lower }(m-1)\text{ targets}\\
2m+1&m,m+1&m&\text{all upper }(m+1)\text{ targets}\\
2m&m-1,m&m&\text{all lower }(m-1)\text{ targets}
\end{array}                                                   \tag{3.7}
\]

The second row is the standard Middle Levels theorem. The first and third
rows use the GMM saturating/tight-enumeration theorem. On an even
\(2m\)-ground there is only one central rank, so there is no equal-shore
Middle Levels Hamilton cycle on levels \(m-1,m\). Complementation does
preserve the rank-\(m\) owner layer there and swaps its lower and upper
colour ledgers, but it generally produces a different owner cycle.

### The strongest even-ground quotient of one Middle Levels cycle

There is a useful stronger statement obtained without pretending that the
odd and even ground sets are the same. Fix one coordinate \(z\), put
\(Y=[2m]\), and decompose the Middle Levels graph according to whether a
set contains \(z\). Its nonvertical edges form two copies:

\[
 \binom Ym\leftrightarrow\binom Y{m+1},
 \qquad
 \binom Y{m-1}\leftrightarrow\binom Ym,                        \tag{3.8}
\]

and the vertical perfect matching is

\[
                         A\longleftrightarrow A\cup\{z\}
                         \qquad(A\in\tbinom Ym).                \tag{3.9}
\]

Put

\[
 \widehat W=\binom{2m}{m},\qquad
 \widehat N=\binom{2m}{m-1},\qquad
 K=\widehat W-\widehat N=\operatorname {Cat}_m.                \tag{3.10}
\]

Every Middle Levels Hamilton cycle uses exactly \(2K\) vertical edges.
Deleting those edges and suppressing the two outer shores in (3.8) gives
two spanning Johnson linear forests \(F_+,F_-\) on
\(\binom Ym\), with:

* exactly \(\widehat N\) edges and \(K\) path components each;
* the same set of \(2K\) endpoints;
* every rank-\((m+1)\) union colour exactly once in \(F_+\);
* every rank-\((m-1)\) intersection colour exactly once in \(F_-\).

This is the strongest valid “one Middle Levels object supplies both
ledgers” statement. The ledgers occur in **different forests**. A single
factor-blind chronology would need one forest (or a controlled fusion) to
carry both.

For completeness, the count is forced. In either copy, every one of its
\(\widehat N\) outer vertices has Hamilton degree two. A middle-copy vertex
has internal degree two unless its vertical edge is used, when it has
internal degree one. Therefore

\[
                         2\widehat W-|V_z|=2\widehat N,
\]

so \(|V_z|=2K\). After deleting the vertical edges, neither copy can
contain a cycle component, since that would already be a component of the
original Hamilton cycle. Hence each copy is a union of \(K\) paths with
common endpoint set \(V_z\), and suppressing each outer vertex gives the
claimed Johnson forests and colour labels.

## 4. Plain complement symmetry: exact parity and action

Let \(c(S)=[2m+1]\setminus S\).  It is a fixed-point-free involution of the
Middle Levels graph, interchanging the two shores.  It also fixes no graph
edge setwise: a fixed unordered edge would have to be

\[
                         \{S,S^c\},                             \tag{4.1}
\]

but \(S\) and \(S^c\) differ in all \(2m+1\) coordinates, not one.

Suppose a Middle Levels Hamilton cycle is invariant under **plain**
complementation.  Complement induces an involutive automorphism of the
abstract cycle \(C_{2W}\).  Such an involution is a half-turn, a
vertex-axis reflection, or an edge-axis reflection.

* A vertex-axis reflection fixes two vertices, impossible.
* An edge-axis reflection fixes two cycle edges setwise, impossible by
  (4.1).
* Hence only the half-turn remains.

The half-turn shifts the cyclic index by \(W\).  Since complement exchanges
the two shores, this shift must reverse index parity.  Therefore \(W\) must
be odd.

### Theorem 4.1 (no even-\(W\) reflection escape)

A plain-complement-invariant Middle Levels Hamilton cycle can exist only
if

\[
                         W=\binom{2m+1}{m}\ \text{is odd},      \tag{4.2}
\]

equivalently

\[
                         m=2^a-1.                              \tag{4.3}
\]

When it exists, complement necessarily acts as the half-turn.  For even
\(W\), the proposed edge-axis reflection is impossible.

#### Proof of the parity equivalence

Lucas' theorem gives

\[
 \binom{2m+1}{m}\equiv1\pmod2
 \quad\Longleftrightarrow\quad
                         m\mathbin{\&}(m+1)=0.
\]

Two consecutive nonnegative integers have disjoint binary supports exactly
when the smaller is a string of ones, i.e. \(m=2^a-1\). \(\square\)

This statement concerns plain complementation.  Some Middle Levels
constructions use **reverse-complement** (a coordinate reversal composed
with complement) in their two-copy description.  That is a different
involution; a fixed edge for it is not excluded by (4.1).  Reverse-
complement symmetry must not be cited as plain complement invariance.

## 5. Why the half-turn still does not couple the required shadows

Assume \(W=2s+1\) and a plain-complement-invariant Hamilton cycle exists.
Index (3.1) so that the half-turn gives

\[
                         U_{i+s}=X_i^c,\qquad
                         X_{i+s+1}=U_i^c.                       \tag{5.1}
\]

The rank-\(m\) projection \(X_0,\ldots,X_{W-1}\) already has every
rank-\((m+1)\) union \(U_i\), by Theorem 3.1.  Its unproved lower colours
remain the \(R_i\) from (3.6).

Consider also the projected rank-\((m+1)\) owner cycle
\(U_0,\ldots,U_{W-1}\).  Its intersections are

\[
                         U_{i-1}\cap U_i=X_i,                   \tag{5.2}
\]

whereas its unions

\[
                         T_i=U_{i-1}\cup U_i                   \tag{5.3}
\]

have rank \(m+2\).  Equations (5.1) give

\[
                         R_i^c=T_{i+s}.                         \tag{5.4}
\]

Thus complement symmetry relates:

\[
 \text{lower rank \(m-1\) of the \(X\)-projection}
 \quad\longleftrightarrow\quad
 \text{upper rank \(m+2\) of the \(U\)-projection}.            \tag{5.5}
\]

It does **not** relate the missing lower rank \(m-1\) targets to the
already-perfect upper rank \(m+1\) targets of the same \(X\)-projection.
Consequently complement symmetry does not repair the missing half of the
depth-one owner ledger.

In the even-ground quotient (3.8)--(3.10), the corresponding statement is

\[
                         F_-=c(F_+),                            \tag{5.6}
\]

with the endpoint pairings conjugate under \(c\). Again this is duality
between the two forests, not diagonal equality and not two-sided colour
perfection of either forest. Even forcing \(F_+=F_-\) would initially give
\(K\) doubled path cycles after the vertical lift, not one Hamilton cycle;
colour-preserving component switches would still be required.

## 6. Exact SCD statement and the remaining bundling

An SCD of \(Q_{2m+1}\) has exactly

\[
                         \binom{2m+1}{m}=W
\]

chains, and every chain crosses both central ranks \(m,m+1\).  For each
\(q\ge0\), exactly

\[
                         N_q=\binom{2m+1}{m-q}
                             =\binom{2m+1}{m+1+q}               \tag{6.1}
\]

chains reach the paired ranks \(m-q,m+1+q\).  Since the chains partition
the Boolean lattice, the sets at every rank are covered exactly once.

For \(Q_{2m}\), there are \(\binom{2m}{m}\) chains, each with one central
rank-\(m\) owner; exactly \(\binom{2m}{m-q}\) chains reach each of ranks
\(m-q,m+q\).

This is exact integral nested-flag ownership.  It is not cyclic ownership:

* a chain supplies one nested flag, not the \(2m\) or \(2m+1\) rotated
  flags of a cyclic order;
* it supplies no successor permutation on the middle owners;
* it supplies neither physical \(H\)-safe chronology nor small
  cross-chain target collision.

Hence traditional wreath bundling remains open.  More precisely, there
are now two alternative open routes:

1. bundle the flags into exact cyclic wreath rows; or
2. bypass wreaths and organize them into the safe owner cycles/packets
   accepted by the factor-blind compiler.

Saying merely “bundling is open” hides this second route.

## 7. Does the factor-blind compiler really bypass wreaths?

Yes.  Its proof emits a literal OR word from arbitrary Johnson cycles; it
does not use cycle length \(2m\), a cyclic coordinate order, or a wreath
factorization.

For an owner-disjoint family of cycles with total good mass \(G=W-u\), the
proved finite compiler has the schematic bound

\[
 \nu(2m)
 \le W+2HK+\Delta_H+\operatorname{Tail}(m,H),                  \tag{7.1}
\]

where:

* \(K\) is the number of retained cycles;
* every cycle has the required physical \(G_H+P_H\) safety (or the
  stronger no-repeated-coordinate condition through \(H+1\) transitions);
* \(\Delta_H\) is the **actual** aggregate missing lower/upper target count;
* the owner leave \(u\) is appended literally and cancels against the
  retained base mass; and
* the product-SCD exterior tail is \(o(W)\) once \(H/\sqrt m\to\infty\).

Thus \(\Theta(m)\)-length cycles give

\[
                         K=O(W/m),\qquad
                         2HK=O(HW/m)=o(W)                       \tag{7.2}
\]

whenever \(H=o(m)\).  Their not being wreaths is irrelevant.

There are, however, four load-bearing qualifications.

1. “\(H\)-safe” must mean the physical two-sided condition needed by the
   delay word.  Ordinary geodesicity \(G_H\) gives only the
   \(P_{H-1}\) dwell condition; \(H+1\) no-repeat safety is a convenient
   sufficient hypothesis.
2. Safety gives correct target **ranks**, not target coverage.
   One still needs \(\Delta_H=o(W)\).
3. Duplicate owner use contributes explicit middle overload; the clean
   cancellation in (7.1) assumes an owner-disjoint near-factor.
4. Unsafe exceptional windows must be hit by \(o(W/H)\) cuts.  Merely
   having \(o(W)\) bad starts is insufficient because each cut costs an
   \(H\)-collar.

Therefore the factor-blind compiler genuinely bypasses the wreath
condition, but it does not bypass the core simultaneous-integrality
problem.  It replaces “package balanced flags into wreaths” by “package
them into few safe owner cycles with small actual shadow deficit.”

## 8. Strongest valid combined theorem

The literature yields the following unconditional pair of one-sided
constant-one statements on \(Q_{2m+1}\).

### Theorem 8.1 (two exact one-sided central words)

There exist:

1. a literal OR word of length \(W+1\) covering every rank-\((m-1)\) and
   rank-\(m\) set (from the GMM saturating cycle plus literal owner leave);
2. a literal OR word of length \(W+1\) covering every rank-\(m\) and
   rank-\((m+1)\) set (from any Middle Levels Hamilton cycle).

The first word and the second word need not be the same.  Neither GMM
Corollary 2, the Middle Levels theorem, reversal, plain complement, nor
reverse-complement proves the existence of one length-\(W+o(W)\) word
having both properties.

Equivalently, the exact remaining depth-one theorem is:

> Construct one Hamilton (or \(W-o(W)\)-owner) Johnson chronology whose
> lower intersections cover all but \(o(W)\) rank-\((m-1)\) targets and
> whose upper unions cover all but \(o(W)\) rank-\((m+1)\) targets, with
> the distinct-facet/literal interface failing at only \(o(W)\) owners.

For the full constant-one theorem, the same chronology must be replaced by
the all-depth factor-blind hypotheses in Section 7.  No cited literature
result supplies that simultaneous theorem.
