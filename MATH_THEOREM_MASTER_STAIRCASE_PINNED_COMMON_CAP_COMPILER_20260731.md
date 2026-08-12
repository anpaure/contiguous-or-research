# Master staircase--pin--common-cap compiler theorem

Date: 2026-07-31  
Status: proved conditional interface; no uniform lift asserted  
Scope: finite Boolean lattices and linear contiguous-OR words

## 1. Purpose and dependency boundary

This note is the construction interface.  It contains no finite-search
claim.  Its input is a rank-\(r\) carrier, a variable staircase schedule,
optional positional pins, and one integral target--cell assignment.  Its
output is a universal word.

The statements labelled **Lemma** or **Theorem** below are proved
equivalences or implications.  The statements labelled **construction
hypothesis** are the data that a separate construction must supply.  In
particular, this theorem does not assert that a suitable carrier, reroot,
schedule, pin, or matching exists in every dimension.

Throughout, a word is a finite sequence

\[
 Q=(Q_0,\ldots,Q_{L-1}),\qquad
 \varnothing\ne Q_p\subseteq[k].
\]

Here and below, an interval is nonempty.  The value of an interval
\(J\subseteq[0,L-1]\) is
\(\bigcup_{p\in J}Q_p\).  Let \(\nu(k)\) be the minimum length of a word
whose interval values contain every nonempty subset of \([k]\).

## 2. Carrier and reroot interface

Fix \(1\le r\le k\), and let

\[
 T=(T_0,\ldots,T_{W-1}),\qquad |T_i|=r,
\]

be a linear chronology.

### Construction hypothesis C1 (owner-exact upper carrier)

The chronology \(T\) satisfies both:

1. \(i\mapsto T_i\) is a bijection from \([0,W-1]\) to
   \({[k]\choose r}\), so \(W={k\choose r}\);
2. for every \(U\subseteq[k]\) with \(|U|>r\), there is a row interval
   \([a,b]\) such that
   \[
     U=\bigcup_{i=a}^{b}T_i.
     \tag{2.1}
   \]

The first clause is exact middle ownership.  The second is arbitrary-width
upper completeness; it must not be replaced by fixed-width witnesses.

### Lemma 2.1 (oriented-block boundary localization)

Partition a chronology into consecutive blocks and concatenate chosen
orientations of those blocks.  Reversing a block preserves the value of
every row interval wholly inside that block.  For an oriented block \(C\),
write \(\operatorname{Int}(C)\), \(\operatorname{Pref}(C)\), and
\(\operatorname{Suf}(C)\) for its internal, nonempty-prefix, and
nonempty-suffix union families, and write \(\operatorname{Tot}(C)\) for its
whole-block union.  For the
new order \(C_1\Vert\cdots\Vert C_t\), the interval-value set is exactly

\[
 \bigcup_j\operatorname{Int}(C_j)
 \ \cup\!
 \bigcup_{a<b}
 \left\{
 S\cup\bigcup_{a<j<b}\operatorname{Tot}(C_j)\cup P:
 S\in\operatorname{Suf}(C_a),\ P\in\operatorname{Pref}(C_b)
 \right\}.
 \tag{2.2}
\]

Consequently a proposed endpoint reroot or block braid satisfies the upper
part of C1 if and only if its cross-boundary intervals supply every upper
target not already supplied internally.

#### Proof

Reversal bijects the intervals of a block with themselves and preserves the
union of every such interval.  Every cross-boundary interval is uniquely a
suffix of its first block, all intervening whole blocks, and a prefix of its
last block.  This proves (2.2) and the final equivalence.  \(\square\)

Lemma 2.1 is an exact audit reduction, not an existence theorem for a good
reroot.

## 3. Variable staircase schedules and pins

A variable staircase schedule consists of nonempty physical intervals

\[
 I_i=[s_i,d_i]\subseteq[0,L-1]\qquad(0\le i<W)
 \tag{3.1}
\]

whose starts and deadlines are strictly increasing.  It is
**chain-aligned** when

\[
 J_{a,b}:=\bigcup_{i=a}^{b}I_i
 \tag{3.2}
\]

is a physical interval for every \(0\le a\le b<W\).

Because starts and deadlines are increasing, this is equivalent to

\[
 s_{i+1}\le d_i+1\qquad(0\le i<W-1).
 \tag{3.3}
\]

Define the maximal middle envelope

\[
 E_p=\bigcap_{i:p\in I_i}T_i,
 \tag{3.4}
\]

where an empty intersection is \([k]\).  A family of positional caps is a
sequence

\[
 \varnothing\ne\Gamma_p\subseteq E_p.
 \tag{3.5}
\]

At unpinned positions one normally takes \(\Gamma_p=E_p\).
Here \(\Gamma_p\) is an upper-bound cap on the eventual letter.  It is not
an exact non-singleton letter prescription.  Exact target-cell pins are the
map \(M_0\) in (4.6); a singleton cap is exceptional because nonemptiness
then forces equality.

### Lemma 3.1 (maximal envelope and exact cap criterion)

There exists a nonempty word subordinate to \(E\) that realizes every
middle row on its prescribed interval if and only if

\[
 E_p\ne\varnothing\quad\text{for all }p,
 \qquad
 \bigcup_{p\in I_i}E_p=T_i\quad\text{for all }i.
 \tag{3.6}
\]

When these conditions hold, \(E\) itself is a realization.  Starting from
such an exact envelope, caps \(\Gamma\) preserve every middle row if and
only if

\[
 \bigcup_{p\in I_i}\Gamma_p=T_i
 \qquad(0\le i<W).
 \tag{3.7}
\]

For one cap \(\Gamma_p=C\subseteq E_p\), condition (3.7) need only be
checked on rows containing \(p\), where it is

\[
 C\cup\bigcup_{q\in I_i\setminus\{p\}}E_q=T_i.
 \tag{3.8}
\]

#### Proof

Every word subordinate to \(E\) is contained in every active middle row.
It can realize that row only if the union of the maximal allowed letters is
the whole row; this proves necessity in (3.6), while \(Q=E\) proves
sufficiency.  The same containment argument makes capped equality precisely
(3.7).  With only one changed position it becomes (3.8), and rows not
containing that position remain exact by (3.6).  \(\square\)

A singleton retiming is the special case \(C=\{z\}\).  It is exact if and
only if \(z\in E_p\) and every other required bit of every row containing
\(p\) occurs at another position of that row.  Any interval with value
\(\{z\}\) consists entirely of singleton letters \(\{z\}\), so requiring a
one-position singleton witness loses no generality.  If \(\{p\}\) is
assigned to the lower target \(\{z\}\), the cap and fixed assignment must be
installed before the residual target--cell graph is formed.

Individually admissible caps need not compose.  Multiple pins are legal
exactly when their combined envelope passes (3.7); every fixed
non-singleton target-cell pin must also retain its positive OR obligation in
the common-cap equations.

### Construction hypothesis C2 (admissible pinned staircase)

The schedule is chain-aligned, its uncapped envelope satisfies (3.6), and
the chosen caps satisfy (3.5) and (3.7).

## 4. Complete lower-cell atlas

Let

\[
 \mathcal L_{<r}=\{S\subseteq[k]:1\le |S|<r\}
 \tag{4.1}
\]

and define the schedule's full lower-cell atlas

\[
 \mathcal C(I)=
 \{J\subseteq[0,L-1]:J\text{ is an interval and }
                      I_i\nsubseteq J\text{ for every }i\}.
 \tag{4.2}
\]

### Lemma 4.1 (atlas completeness)

If a word realizes \(T_i\) on \(I_i\), every interval witnessing a target
in \(\mathcal L_{<r}\) belongs to \(\mathcal C(I)\).  Moreover different
lower targets require different witness intervals.

#### Proof

An interval containing a complete \(I_i\) has value containing the rank-
\(r\) set \(T_i\), so it cannot equal a target of rank below \(r\).  A fixed
interval has only one value and therefore cannot witness two distinct
targets.  \(\square\)

Thus (4.2) is the canonical complete atlas.  Any compressed description of
it, including a proper-prefix formula for a P/Q schedule, is valid only
after proving equality with (4.2), including all omitted-start and boundary
cells.

For the monotone staircase (3.1), put

\[
 \tau(x)=\min\{d_i:s_i\ge x\},
 \tag{4.3}
\]

with \(\tau(x)=L\) if the set is empty.  Then the cells in the full atlas
starting at \(x\) are exactly

\[
 [x,t]\quad\text{with}\quad x\le t<\tau(x).
 \tag{4.4}
\]

Indeed, the first row interval whose start is not before \(x\) has the first
deadline that can be wholly contained in an interval starting at \(x\).
This gives proper prefixes at selected starts.  At omitted starts it gives a
first-delivery cutoff, not an automatic uniform depth bound.

For fixed caps \(\Gamma\), define the exact locally feasible edge set

\[
 \mathcal E_\Gamma=
 \left\{(S,J)\in\mathcal L_{<r}\times\mathcal C(I):
 \begin{array}{l}
   \Gamma_p\cap S\ne\varnothing\quad(p\in J),\\
   S\subseteq\displaystyle\bigcup_{p\in J}\Gamma_p
 \end{array}
 \right\}.
 \tag{4.5}
\]

These two conditions are necessary and sufficient for letters subordinate
to \(\Gamma\), considered on \(J\) alone, to have union \(S\).  Global row
and overlap compatibility is deliberately deferred to the common-cap
condition below.

Optional preassigned pins are an injective partial map

\[
 M_0:\mathcal L_0\longrightarrow\mathcal C(I),
 \qquad (S,M_0(S))\in\mathcal E_\Gamma,
 \tag{4.6}
\]

for some \(\mathcal L_0\subseteq\mathcal L_{<r}\).  Their cells are removed
from the residual matching domain.  A pinned singleton is included here,
not duplicated in the residual target set.

## 5. The maximal-common-cap equivalence

Let

\[
 M:\mathcal L_{<r}\longrightarrow\mathcal C(I)
 \tag{5.1}
\]

be an injective extension of \(M_0\), with
\((S,M(S))\in\mathcal E_\Gamma\) for every \(S\).  Define

\[
 A_p(M)=
 \Gamma_p\cap
 \bigcap_{S:\,p\in M(S)}S.
 \tag{5.2}
\]

The empty inner intersection is \([k]\), so if no assigned cell contains
\(p\), then \(A_p(M)=\Gamma_p\).

### Theorem 5.1 (maximal-common-cap compiler, iff)

There exists a word \(Q\) satisfying

\[
 \varnothing\ne Q_p\subseteq\Gamma_p,
 \tag{5.3}
\]

\[
 \bigcup_{p\in I_i}Q_p=T_i\quad(0\le i<W),
 \tag{5.4}
\]

and

\[
 \bigcup_{p\in M(S)}Q_p=S
 \quad(S\in\mathcal L_{<r})
 \tag{5.5}
\]

if and only if

\[
 A_p(M)\ne\varnothing\quad(0\le p<L),
 \tag{5.6}
\]

\[
 \bigcup_{p\in I_i}A_p(M)=T_i\quad(0\le i<W),
 \tag{5.7}
\]

and

\[
 \bigcup_{p\in M(S)}A_p(M)=S
 \quad(S\in\mathcal L_{<r}).
 \tag{5.8}
\]

When these conditions hold, \(Q=A(M)\) is the unique coordinatewise
maximal realizing word for the fixed assignment \(M\).

#### Proof

If \(Q\) realizes the assignment, then for every \(p\),
\(Q_p\subseteq\Gamma_p\).  Whenever \(p\in M(S)\), equation (5.5) also
gives \(Q_p\subseteq S\).  Hence \(Q_p\subseteq A_p(M)\).  Enlarging
\(Q\) to \(A(M)\) cannot add a coordinate forbidden by an active middle
row or assigned lower target, while it cannot lose a coordinate already
supplied by \(Q\).  Thus (5.6)--(5.8) hold.

Conversely, (5.2) excludes every forbidden coordinate, and
(5.6)--(5.8) supply all required coordinates with nonempty letters.
Therefore \(A(M)\) realizes (5.3)--(5.5).  Every other realization is
coordinatewise contained in it by the first paragraph.  \(\square\)

The theorem explains why marginal Hall is only necessary: a matching in
\(\mathcal E_\Gamma\) may fail because its overlapping cells make some
maximal cap empty or delete a required middle or lower coordinate.

### Corollary 5.2 (exact integral selection model)

For every edge \((S,J)\in\mathcal E_\Gamma\) introduce a Boolean selector
\(y_{S,J}\).  Fix each edge of \(M_0\) to one, fix every competing edge at
its target or reserved cell to zero, and leave the residual edges variable.
Enforce exactly one selected edge at each target and at most one at each
cell.  For every
\(b\in\Gamma_p\), introduce \(q_{p,b}\) with the equivalence

\[
 q_{p,b}\ \Longleftrightarrow\
 \bigwedge_{(S,J):\,p\in J,\ b\notin S}\neg y_{S,J}.
 \tag{5.9}
\]

An empty conjunction in (5.9) is true.

Add the three coverage families

\[
 \bigvee_{b\in\Gamma_p}q_{p,b}\quad(p<L),
 \tag{5.10}
\]

\[
 \bigvee_{p\in I_i:\,b\in\Gamma_p}q_{p,b}\quad(b\in T_i),
 \tag{5.11}
\]

and

\[
 y_{S,J}\Longrightarrow
 \bigvee_{p\in J:\,b\in\Gamma_p}q_{p,b}
 \quad((S,J)\in\mathcal E_\Gamma,\ b\in S).
 \tag{5.12}
\]

This finite Boolean system is feasible if and only if an integral extension
\(M\) satisfying Theorem 5.1 exists.  It is exact only when the edge set is
the complete set (4.5), or when every omitted edge has been excluded by a
proved safe condition.

#### Proof

Under the matching constraints, (5.9) is precisely the bitwise definition
of (5.2).  Conditions (5.10), (5.11), and (5.12) are respectively (5.6),
(5.7), and (5.8).  Conversely these equations reconstruct the selected
injection and its maximal common cap.  \(\square\)

No fractional rounding occurs in Corollary 5.2.

## 6. Exact conflicts and noncircular selection certificates

Theorem 5.1 is an exact terminal test.  This section separates two useful
ways of proving that its integral assignment exists from a strong
Cartesian reformulation which merely hides the assignment in its premise.

### 6.1. Residualization and the exact conflict clutter

First absorb the fixed target-cell pins into

\[
 \overline\Gamma_p=
 \Gamma_p\cap
 \bigcap_{S\in\mathcal L_0:\,p\in M_0(S)}S,
 \tag{6.1}
\]

using \([k]\) for an empty inner intersection.  Before any residual choice,
check

\[
 \overline\Gamma_p\ne\varnothing,
 \qquad
 \bigcup_{p\in I_i}\overline\Gamma_p=T_i,
 \qquad
 \bigcup_{p\in M_0(S)}\overline\Gamma_p=S.
 \tag{6.2}
\]

If (6.2) fails, further intersections cannot repair it.  Otherwise put

\[
 \mathcal R=\mathcal L_{<r}\setminus\mathcal L_0,
 \qquad
 \mathcal C_0=\mathcal C(I)\setminus M_0(\mathcal L_0),
 \tag{6.3}
\]

and rebuild the complete residual candidate graph from
\(\overline\Gamma\), not from the pre-pin envelope.  For any physical
interval \(J\) and bit \(b\), write

\[
 H_{J,b}=\{p\in J:b\in\overline\Gamma_p\}.
 \tag{6.4}
\]

Choose one candidate edge \(e=(S,J)\) for each \(S\in\mathcal R\).  The
complete matching-compatible bad-event clutter consists of the
inclusion-minimal families of the following five types:

1. two distinct targets choosing the same cell;
2. an empty position: all chosen cells contain \(p\) and their labels have
   empty intersection with \(\overline\Gamma_p\);
3. a lost middle bit: labels omitting \(b\) have cells covering
   \(H_{I_i,b}\);
4. a lost selected-lower bit: an anchor \(e_0=(S_0,J_0)\), a bit
   \(b\in S_0\), and chosen labels omitting \(b\) whose cells cover
   \(H_{J_0,b}\);
5. a lost protected-pin bit: for \(S_0\in\mathcal L_0\) and \(b\in S_0\),
   chosen labels omitting \(b\) whose cells cover
   \(H_{M_0(S_0),b}\).

Only assignment-compatible events, using at most one candidate from each
target part, need be retained.

### Lemma 6.1 (exact conflict-transversal equivalence)

An integral one-candidate-per-target selection extends \(M_0\) to a
common-cap compiler if and only if it contains no bad event of types 1--5.

#### Proof

Type 1 is exactly failure of cell injectivity.  Types 2--5 are respectively
failure of nonemptiness, a middle-row equation, a selected residual-lower
equation, and a fixed-pin equation for the maximal cap.  Thus avoiding every
type gives all equations of Theorem 5.1.  Conversely, any failed maximal-cap
equation has a finite blocker family; taking an inclusion-minimal subfamily
produces one of the displayed events.  \(\square\)

This is an exact finite formulation.  Bounded event rank or physical span
does not by itself bound event dependency or prove that a transversal
exists.

### 6.2. Why strong Cartesianity is not the positive invariant

For a residual edge set \(H\), define

\[
 K_p(H)=\overline\Gamma_p\cap
        \bigcap_{(S,J)\in H:\,p\in J}S.
 \tag{6.5}
\]

Call \(H\) **strong Cartesian** when \(K(H)\) is nonempty, preserves every
middle and protected-pin row, and realizes every edge of \(H\).

### Proposition 6.2 (strong Cartesian factorization is an exact restatement)

A common-cap compiler exists if and only if a strong Cartesian \(H\)
contains a residual lower-perfect matching.

#### Proof

The forward implication takes \(H\) to be the realizing matching itself;
the reverse implication uses \(K(H)\).  \(\square\)

This proposition is not an existence theorem.  If two edges of a strong
Cartesian \(H\) put distinct labels \(S\ne T\) on the same physical cell,
that cell would have to have union both \(S\) and \(T\), which is
impossible.  Once every target is incident, distinct-target cell collisions
have therefore already been eliminated.  Strong Cartesianity has encoded
essentially the whole compiler before Hall is invoked.

### 6.3. Guarded fractional Hall

The useful weaker object protects only edges that a matching can select
together.  Let \(G'\) be any subgraph of the rebuilt residual candidate
graph.  It is
**co-selectable guarded** if one can choose:

- a position guard \(a_p\in\overline\Gamma_p\) for every \(p\);
- a row guard \(r(i,b)\in H_{I_i,b}\) for every \(b\in T_i\);
- a protected-pin guard \(u(S,b)\in H_{M_0(S),b}\) for every
  \(S\in\mathcal L_0\), \(b\in S\); and
- an edge guard \(g(e,b)\in H_{J,b}\) for every
  \(e=(S,J)\in G'\), \(b\in S\),

such that every \(f=(T,D)\in G'\) satisfies

\[
 p\in D\Longrightarrow a_p\in T,
 \tag{6.6}
\]

\[
 r(i,b)\in D\Longrightarrow b\in T,
 \qquad
 u(S_0,b)\in D\Longrightarrow b\in T,
 \tag{6.7}
\]

and, for every ordered pair of edges \(e=(S,J)\), \(f=(T,D)\) with
distinct targets and distinct cells,

\[
 g(e,b)\in D\Longrightarrow b\in T
 \qquad(b\in S).
 \tag{6.8}
\]

### Theorem 6.3 (guarded fractional-Hall compiler)

Suppose \(G'\) is co-selectable guarded and there are weights \(x_e\ge0\)
such that

\[
 \sum_{e\in G'(S)}x_e=1\quad(S\in\mathcal R),
 \qquad
 \sum_{e\text{ using }J}x_e\le1\quad(J\in\mathcal C_0).
 \tag{6.9}
\]

Then an integral common-cap extension of \(M_0\) exists.

#### Proof

For every \(\mathcal A\subseteq\mathcal R\), summing (6.9) gives
\(|\mathcal A|\le|N_{G'}(\mathcal A)|\).  Hall therefore supplies an
integral matching.  Conditions (6.6)--(6.8) make its position, middle,
protected-pin, and selected-edge guards survive every co-selected cap.
Hence none of the five exact bad-event types occurs, and Lemma 6.1 gives the
compiler.  \(\square\)

A directly checkable specialization takes

\[
 x_{S,J}=\frac1{\deg_{G'}(S)}
 \tag{6.10}
\]

and verifies, for every cell \(J\),

\[
 \sum_{S:(S,J)\in G'}\frac1{\deg_{G'}(S)}\le1.
 \tag{6.11}
\]

Unlike strong Cartesianity, (6.6)--(6.11) contain neither an integral
matching nor a completed physical word.

### 6.4. Atomic lopsided-LLL alternative

Guarding every co-selectable pair may be too rigid.  After exact unary
propagation, retain the complete bad-event family from Lemma 6.1, including
same-cell collisions.  Assume every remaining event has size at least two
and uses at most one candidate of each residual target.  Independently
choose one candidate for each target, with probabilities \(\pi_S\).

For an atomic bad event \(B\), put

\[
 p_B=\prod_{e\in B}\pi(e).
 \tag{6.12}
\]

For a candidate \(e\), let \(\mathcal A(e)\) be the bad events prescribing
a different candidate in the target part of \(e\).

### Theorem 6.4 (atomic lopsided common-cap criterion)

If numbers \(c_e\ge1\) and \(0\le y_B<1\) satisfy

\[
 p_B\le\frac{y_B}{\prod_{e\in B}c_e}
 \qquad(B),
 \tag{6.13}
\]

and

\[
 \prod_{B\in\mathcal A(e)}(1-y_B)\ge c_e^{-1}
 \qquad(e\text{ of positive probability}),
 \tag{6.14}
\]

then an integral common-cap extension of \(M_0\) exists.

#### Proof

Use the lopsided dependency graph joining atomic events only when they
prescribe different values of a common target variable.  Every lopsided
neighbor of \(B\) lies in \(\mathcal A(e)\) for some \(e\in B\).  Hence
(6.13)--(6.14) imply the asymmetric lopsided-LLL inequalities.  An outcome
avoiding all events is cell-injective and avoids the complete conflict
clutter, so Lemma 6.1 applies.  \(\square\)

The local-lemma hypotheses are literal pressure inequalities, not
consequences of bounded depth, bounded conflict rank, or large candidate
lists.  Collision events and protected multi-cell pin events may not be
omitted.

## 7. Upper transfer

### Lemma 7.1 (chain-aligned upper transfer)

Suppose \(Q_p\subseteq\Gamma_p\subseteq E_p\), and (5.4) holds.  If
\(U=\bigcup_{i=a}^{b}T_i\), then on the physical interval
\(J_{a,b}\) from (3.2),

\[
 \bigcup_{p\in J_{a,b}}Q_p=U.
 \tag{7.1}
\]

#### Proof

Every \(p\in J_{a,b}\) lies in some \(I_i\) with \(a\le i\le b\), so
\(Q_p\subseteq E_p\subseteq T_i\subseteq U\).  Conversely
\(I_i\subseteq J_{a,b}\), and (5.4) supplies every coordinate of every
\(T_i\) on that physical interval.  \(\square\)

## 8. Fixed-fibre equivalence and master construction theorem

### Theorem 8.1 (exact fixed-fibre equivalence)

Fix a chronology satisfying C1 and a pinned schedule satisfying C2.  Among
words subordinate to \(\Gamma\), realizing the prescribed middle rows on
\(I_i\), and respecting \(M_0\), meaning

\[
 \bigcup_{p\in M_0(S)}Q_p=S\qquad(S\in\mathcal L_0),
\]

the following are equivalent:

1. there is a universal word;
2. \(M_0\) extends to an injection satisfying Theorem 5.1;
3. the complete integral system of Corollary 5.2 is feasible.

#### Proof

The equivalence of 2 and 3 is Corollary 5.2.  If 1 holds, choose one literal
witness interval for every lower target not already pinned.  Lemma 4.1 puts
every chosen witness in the full atlas, and distinct target values make the
choice injective.  Theorem 5.1 applied to the witnessing word proves 2.
Conversely 2 gives all lower and middle targets by Theorem 5.1, and every
upper target by C1 and Lemma 7.1.  \(\square\)

### Construction hypothesis C3 (integral pinned common-cap assignment)

The preassignment \(M_0\) extends to an injection \(M\) satisfying the
equivalent conditions of Theorem 5.1.  Equivalently, the exact integral
system of Corollary 5.2 is feasible.

This is the exact terminal construction hypothesis, not the preferred
inductive invariant: it already contains the integral selector.

### Theorem 8.2 (master staircase--pin--common-cap construction)

Assume C1, C2, and C3.  Then

\[
 Q_p=A_p(M)\qquad(0\le p<L)
 \tag{8.1}
\]

is a length-\(L\) universal contiguous-OR word on \([k]\).

If an independent lower-bound theorem gives \(\nu(k)\ge L\), then

\[
 \nu(k)=L.
 \tag{8.2}
\]

#### Proof

Theorem 5.1 gives nonempty letters and exact witnesses for every lower and
rank-\(r\) target.  For an upper target, C1 supplies a consecutive carrier
block and Lemma 7.1 supplies a physical interval with the same value.  These
three rank ranges partition all nonempty subsets of \([k]\), so \(Q\) is
universal.  It has exactly \(L\) nonempty positions.  The final assertion
follows from the independent lower bound.  \(\square\)

### Corollary 8.3 (two noncircular sufficient routes)

In Theorem 8.2, C3 may be replaced by either:

1. a co-selectable guarded graph and fractional flow satisfying
   Theorem 6.3; or
2. a complete post-closure bad-event family, candidate distributions, and
   pressure witnesses satisfying Theorem 6.4.

Each alternative implies C3 without assuming an integral matching or a
physical word.

## 9. Minimal noncircular lift invariant and remaining gate

Within this proof architecture, the smallest presently proved modular
positive package consists of:

1. **Carrier/closure datum:** C1, together with a chosen physical row-block
   witness \(\omega(U)=[a_U,b_U]\) for every upper target.  A one-step
   application uses only these witnesses.  A recursive Pascal/odd--even
   lift must additionally retain the tagged homogeneous pieces, strict
   ports and run check, occurrence-level all-depth flag ledger, and the
   residual link data actually used to regenerate the child witness map.
   Those decorations serve closure only; they are not compiler hypotheses.
2. **Pinned staircase:** C2, followed by the fixed-pin replay (6.2); every
   non-singleton pin remains a protected positive row.  The canonical full
   atlas and residual occurrence relation are recorded, although a positive
   proof may retain a smaller proved-sound covering subatlas.
3. **Noncircular selection certificate:** a sound subatlas covering every
   residual lower target, together with either
   - the guards and fractional flow of Theorem 6.3, or
   - the complete relative conflict clutter and atomic pressure witnesses of
     Theorem 6.4.

The full atlas (4.2) is required for the fixed-fibre equivalence and for
negative claims.  A positive construction may use any sound subatlas that
covers all residual targets.  The third item cannot be weakened to an
unguarded fractional matching: the guards are what preserve the common cap.
Nor can bounded conflict rank replace the atomic pressure inequalities.

This package contains neither an integral matching nor a source word, so it
is noncircular.  Strong Cartesianity is deliberately excluded because
Proposition 6.2 can always obtain it after the fact by taking \(H=M\).

To call the package **regenerative**, attach a nonempty decorated joint
action fibre: the same boundary action must be carrier/occurrence-safe,
schedule-and-pin-safe, and compatible with the retained rounding
certificate.  This object is more accurately a complex--clutter residual
link than a safe-cut complex.  Negative safety is downward-closed, whereas
positive occurrence, selector, and guard requirements have the opposite
monotonicity; separately nonempty sector fibres need not intersect.

For an actual induction, a lift theorem would have to map a parent package
to a child package by proving three separate closure statements:

- \(L_C\): regenerate exact child ownership, the named upper-witness map,
  and every port/run/safe-cut occurrence needed for another lift;
- \(L_S\): construct the child optimal-length staircase, prove its baseline
  envelope exact before capping, install the caps jointly, and identify its
  atlas; and
- \(L_R\): regenerate either the guarded fractional certificate or the
  atomic pressure certificate on the actual capped child atlas.

These three constructions must use one action in the decorated joint fibre,
and the child must inherit a nonempty joint fibre for the following step.

A parent universal word, integral matching, scalar area estimate, or owner
deck alone supplies none of \(L_C,L_S,L_R\).  No uniform theorem proving
these three closure statements is claimed here.  In particular,
Hamiltonicity, trace-two owner dimension, and an already selected deep
matching are not fields of this minimal package; they are optional devices
for constructing one of its three blocks.

The dependency order is strict:

\[
 T,\omega
 \longrightarrow I
 \longrightarrow E\text{ and baseline replay}
 \longrightarrow \Gamma,M_0\text{ jointly}
 \longrightarrow \overline\Gamma\text{ and the capped residual graph}
 \longrightarrow \text{FH or atomic LLL}.
\]

Thus the three blocks are modular but not independently choosable.  In a
lift they must all refer to the same child braid and boundary action.

The dependency chain is therefore

\[
 \boxed{\text{carrier C1}}
 \longrightarrow
 \boxed{\text{staircase and pins C2}}
 \longrightarrow
 \boxed{\text{guarded flow or atomic LLL}}
 \longrightarrow
 \boxed{\text{integral common cap C3}}
 \longrightarrow
 \boxed{\text{universal word}},
\]

with optimality supplied only by an external lower bound.  This is a
dimension-free conditional interface, not an all-\(k\) construction.
