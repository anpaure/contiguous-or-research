# Born-linear \(Q_0\): Hamilton birth, the Latin pair-cover gate, and cyclic obstructions

Date: 2026-08-01  
Lane: prospective \(M_0/Q_0\) construction / upper-exact Catalan forest  
Status: exact prospective reduction and exact counterexamples to two simple
rule families.  No all-\(m\) upper-surjective Hamilton cycle is claimed.

## 0. Outcome

Work in the middle-levels incidence graph

\[
 {\rm ML}_m=
 \binom{[2m-1]}{m-1}\ \cup\ \binom{[2m-1]}m .
\]

Put

\[
 W=\binom{2m-1}m,\qquad
 U=\binom{2m-1}{m+1},\qquad
 C=W-U=\operatorname {Cat}_m.                         \tag{0.1}
\]

This note proves four exact statements.

1. **Hamilton birth.**  Any Hamilton cycle whose upper turns cover all
   rank-\((m+1)\) sets contains an upper-exact rooted Catalan forest
   \(Q_0\).  If a protected pivot path has distinct upper colours, it may be
   forced into \(Q_0\).  A redundant upper occurrence outside the pivot
   opens the cycle into the exact \(B+1\) Hamilton-path certificate.
2. **Latin pair-cover form.**  Relative to a proper \(m\)-edge-colouring of
   \({\rm ML}_m\), upper coverage by a fixed pair of colour classes is
   exactly the requirement that the same unordered colour pair appear in
   every local opposite-dart table.  At each upper set the colour-pair
   multigraph is \((m+1)\)-regular on \(m\) colours.
3. **Smallest local Latin obstruction.**  Local row-Latin and opposite-dart
   inequalities force pair coverage for \(m\le3\), but not for \(m=4\).
   The cyclic-difference table on \(K_5\) is a literal legal local table
   whose ten darts use only the colour pairs \(\{1,4\}\) and \(\{2,3\}\).
   Hence no proof using only the independent local Latin axioms can supply
   a universal fixed pair.
4. **Cyclic representative obstruction.**  A fully rotation-equivariant
   \(Q_0\) is impossible whenever \(3\mid(2m-1)\): its incidence edges have
   free orbits, while the upper layer has order-three short orbits and
   \(Q_0\to\binom{[2m-1]}{m+1}\) is an equivariant bijection.  The maximal
   subgroup of order prime to three has no such arithmetic obstruction, but
   existence in its quotient remains open.

Together with the existing lexical-capacity theorem, these results rule out
three tempting shortcuts:

* select \(Q_0\) by a fully cyclic representative rule;
* infer a good fixed factor pair from local Latin properness alone; or
* repair the standard lexical/parenthesis factor by only the canonical GMN
  pull tree.

The weakest surviving prospective owner theorem is now simply:

> construct an upper-turn-surjective Middle Levels Hamilton cycle containing
> the correlated tight-pivot path.

The Catalan representative forest and its safe opening then cost no further
integrality theorem.

## 1. Hamilton-cycle birth of the rooted Catalan forest

Write a Hamilton cycle as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{W-1},B_{W-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1},                 \tag{1.1}
\]

where indices are cyclic, \(|A_i|=m-1\), and \(|B_i|=m\).  Let

\[
 M_0=\{A_iB_i:i\in\mathbb Z_W\},\qquad
 M_1=\{A_{i+1}B_i:i\in\mathbb Z_W\}.                  \tag{1.2}
\]

These are the two perfect matching classes of the cycle.  The upper turn at
\(A_i\) is

\[
                         u_i=B_{i-1}\cup B_i.          \tag{1.3}
\]

Rooting at \(M_0\), the incidence \(A_iB_{i-1}\in M_1\) contracts to the
directed link \(A_i\to A_{i-1}\), and its upper label is \(u_i\).

### Theorem 1.1 (upper-surjective cycle \(\Rightarrow\) born-linear \(Q_0\))

Assume

\[
                    \{u_i:i\in\mathbb Z_W\}
                      =\binom{[2m-1]}{m+1}.            \tag{1.4}
\]

Choose one occurrence \(i(R)\) of every upper colour \(R\), and put

\[
                  Q_0=\{A_{i(R)}B_{i(R)-1}:R\}.        \tag{1.5}
\]

Then:

1. \(Q_0\subseteq M_1\) is a matching;
2. its upper-label map is a bijection onto all \(U\) upper colours;
3. its rooted links form a spanning forest; and
4. it has exactly \(C=W-U\) components, including isolates.

If a protected set \(P_1\subseteq M_1\) has pairwise distinct upper labels,
then the representatives in (1.5) may be chosen so that
\(P_1\subseteq Q_0\).

#### Proof

Every subset of the matching \(M_1\) remains a matching.  The rooted links
of all of \(M_1\) form one directed \(W\)-cycle.  Since \(U<W\), the proper
subset \(Q_0\) omits at least one cycle edge and therefore is a forest.
It has \(U\) edges on \(W\) spanning rooted vertices, hence \(W-U=C\)
components.  The representative choice gives upper bijectivity.

For a protected edge, choose its occurrence as the representative of its
upper colour.  Pairwise distinct protected labels make these choices
compatible; all other colours are then chosen arbitrarily.  \(\square\)

This theorem bypasses the fixed-\(M_0\) rainbow-hypergraph integrality gate:
\(M_0\), all heads, all tails, and the forest topology are born together
inside one Hamilton cycle.

### Theorem 1.2 (safe opening outside a protected pivot)

Let

\[
 \mu(R)=|\{i:u_i=R\}|
\]

be the upper multiplicities, and let

\[
 \mathcal D=\{i:\mu(u_i)\ge2\}                         \tag{1.6}
\]

be the redundant-provider occurrences.  Under (1.4),

\[
                         |\mathcal D|\ge C+1.           \tag{1.7}
\]

Consequently, if \(|P_1|<C+1\), there is an edge
\(e\in M_1-P_1\) such that deleting \(e\) opens (1.1) into a Hamilton path,
preserves upper surjectivity, and retains a protected upper-exact
\(Q_0\supseteq P_1\).  The remainder

\[
                 Q_1=(M_1-\{e\})-Q_0
\]

has size \(C-1\) and joins the \(C\) components of \(Q_0\) into the
directed free-port Hamilton path required by the \(B+1\) certificate.

#### Proof

Surjectivity and \(\sum_R\mu(R)=W\) give

\[
 \sum_R(\mu(R)-1)=W-U=C.                               \tag{1.8}
\]

If \(r_+\) upper colours are repeated, then

\[
 |\mathcal D|
   =\sum_{\mu(R)\ge2}\mu(R)
   =C+r_+\ge C+1.                                      \tag{1.9}
\]

Thus one redundant-provider edge lies outside \(P_1\).  Deleting it leaves
another occurrence of its colour and hence preserves (1.4); deleting one
edge of \(M_1\) from an alternating Hamilton cycle leaves an alternating
Hamilton path whose \(M_0\) class is still perfect.

Apply Theorem 1.1 inside the remaining \(M_1\)-path, retaining \(P_1\).
The full rooted link set \(M_1-\{e\}\) is one spanning directed path.
Deleting the \(Q_0\) edges contracts its \(C\) \(Q_0\)-components in their
path order, so the \(C-1\) remaining links are precisely a directed
free-port component path.  \(\square\)

For a tight pivot, \(|P_1|=3d=O(\sqrt m)\), while \(C\) is exponential.
Thus safe opening is automatic for all sufficiently large \(m\) once the
upper-surjective protected Hamilton cycle exists.

## 2. Latin pair-cover formulation

Let

\[
                    \chi:E({\rm ML}_m)\longrightarrow[m]         \tag{2.1}
\]

be a proper \(m\)-edge-colouring.  Every colour class \(M_c\) is a perfect
matching.  Fix distinct colours \(p,q\).  Their union is a spanning
two-factor.

For \(R\in\binom{[2m-1]}{m+1}\), make a complete graph \(K_R\) on vertex
set \(R\).  Its vertex \(a\in R\) represents the middle owner
\(T_a=R-\{a\}\).  On the dart \(a\to b\), put

\[
       \chi_R(a,b)=
       \chi\bigl(R-\{a,b\},\,R-\{a\}\bigr).             \tag{2.2}
\]

### Proposition 2.1 (opposite-dart Latin table)

For every \(R\):

1. for fixed \(a\), the map \(b\mapsto\chi_R(a,b)\) is a permutation of
   \([m]\); and
2. \(\chi_R(a,b)\ne\chi_R(b,a)\).

Define the loopless colour-pair multigraph \(G_R\) on vertex set \([m]\) by
labelling the local edge \(\{a,b\}\) with

\[
                    \{\chi_R(a,b),\chi_R(b,a)\}.       \tag{2.3}
\]

Then \(G_R\) is \((m+1)\)-regular, and the multiplicity of the colour edge
\(\{p,q\}\) is exactly the number of lower turns of \(M_p\cup M_q\) whose
upper colour is \(R\).

#### Proof

At owner \(T_a\), the \(m\) incident inclusion edges have all \(m\) colours,
giving Item 1.  The two darts of \(\{a,b\}\) are the two incidences at the
same lower vertex \(R-\{a,b\}\), so properness gives Item 2.

Every colour occurs once among the darts leaving each of the \(m+1\) local
vertices; hence its degree in \(G_R\) is \(m+1\).  Finally, the two
matchings \(M_p,M_q\) meet at lower vertex \(R-\{a,b\}\) with owner union
\(R\) exactly when the two dart colours on \(\{a,b\}\) are \(p,q\).
\(\square\)

### Corollary 2.2 (exact fixed-pair target)

The two-factor \(M_p\cup M_q\) is upper-turn-surjective exactly when

\[
                         pq\in E(\operatorname {supp}G_R)
              \qquad\text{for every }R.               \tag{2.4}
\]

If this two-factor is one Hamilton cycle and contains the protected pivot
in the \(p/q\) phase, Theorems 1.1--1.2 construct the protected
\(Q_0,Q_1\) certificate immediately.

Thus a prospective Latin construction needs only one globally good colour
pair, not simultaneous perfection of every pair.

### Proposition 2.3 (pair-complete local normal form)

Every unordered colour pair occurs at least once in \(G_R\) if and only if

\[
                              G_R=K_m+C_R,             \tag{2.5}
\]

where \(C_R\) is a spanning 2-regular multigraph on the \(m\) colours
(parallel edges are allowed).

#### Proof

The simple complete graph contributes degree \(m-1\) at every colour.
Since \(G_R\) is \((m+1)\)-regular, removing one copy of every colour pair
leaves degree two at every colour.  Conversely, (2.5) plainly contains
every pair and has the required degree.  \(\square\)

This is the strongest clean local target: a 1-factorization satisfying
(2.5) for every \(R\), with one pair forming a Hamilton cycle, solves the
owner-layer problem.  It is stronger than necessary and is not proved.

## 3. The smallest local Latin obstruction

The two axioms of Proposition 2.1 do not force (2.4).

### Theorem 3.1

For \(m=2,3\), every opposite-dart Latin table contains every unordered
colour pair.  For \(m=4\), there is a legal table omitting four of the six
colour pairs.  Hence \(m=4\) is the smallest local obstruction.

#### Proof

For \(m=2\), the loopless \(3\)-regular multigraph on two colours can use
only their unique pair.

For \(m=3\), write \(x_{12},x_{13},x_{23}\) for the pair multiplicities.
The \(4\)-regularity equations are

\[
 x_{12}+x_{13}=4,\quad
 x_{12}+x_{23}=4,\quad
 x_{13}+x_{23}=4.
\]

They force \(x_{12}=x_{13}=x_{23}=2\).

For \(m=4\), identify the five local vertices with \(\mathbb Z_5\) and the
four colours with the nonzero residues.  Define

\[
                         \chi(a,b)=b-a\pmod5.          \tag{3.1}
\]

For fixed \(a\), the four outgoing values are \(1,2,3,4\), while opposite
darts have colours \(c,-c\), which are distinct modulo five.  Thus this is
a legal opposite-dart Latin table.

Edges of cyclic difference \(\pm1\) carry pair \(\{1,4\}\), and edges of
difference \(\pm2\) carry pair \(\{2,3\}\).  Each pair occurs five times;
the other four colour pairs do not occur.  \(\square\)

The \(m=4\) table is a *local* obstruction.  It is not asserted to extend
to one global edge-colouring of \({\rm ML}_4\).  Its force is logical: row
Latinness, opposite-dart inequality, and the exact regular degree ledger do
not imply fixed-pair upper coverage.  A positive proof must use the overlap
correlation between different upper intervals.

## 4. Exact cyclic-equivariance obstruction

Let \(n=2m-1\), and let a cyclic subgroup \(H\le\mathbb Z_n\) of odd order
\(h\) act by coordinate rotation.

The action on rank \(m-1\) and rank \(m\) sets is free: a nontrivial orbit
length dividing \(n\) cannot divide either \(m-1\) or \(m\).  Hence the
action on incidence edges is also free.

### Theorem 4.1 (clean-subgroup necessity)

Suppose \(M_0\) and an upper-exact rooted Catalan forest \(Q_0\) are both
\(H\)-invariant.  Then:

1. the action of \(H\) on rank-\((m+1)\) upper colours is free;
2. \(3\nmid h\); and
3. \(h\mid C=\operatorname {Cat}_m\).

In particular a fully \(\mathbb Z_{2m-1}\)-equivariant \(Q_0\) is impossible
whenever \(3\mid(2m-1)\).  The first substantive failure is \(m=5\),
where the full group has order nine.

#### Proof

The upper-label map

\[
                  \operatorname {up}:Q_0
                     \longrightarrow\binom{[n]}{m+1}             \tag{4.1}
\]

is an equivariant bijection.  Every edge orbit in \(Q_0\) is free, so every
upper-colour orbit must be free as well.

If \(3\mid h\), the order-three subgroup rotates the coordinates in
3-cycles.  Since \(3\mid n\) implies \(m\equiv2\pmod3\), the rank \(m+1\)
is divisible by three.  A union of \((m+1)/3\) coordinate 3-cycles is an
upper set fixed by that subgroup, contradicting freeness.  Thus
\(3\nmid h\).

Finally \(Q_0\) is an \(H\)-invariant forest on a free vertex set.  A
nontrivial odd-order stabilizer of a tree would fix its centre vertex
(an edge centre would require an involution), contradicting vertex
freeness.  Hence its components occur in free \(H\)-orbits.  Since their
number is \(C\), one has \(h\mid C\).  \(\square\)

For the maximal three-free subgroup

\[
 h={2m-1\over 3^{v_3(2m-1)}},                         \tag{4.2}
\]

the exact Catalan identity

\[
 (m^2-1)\operatorname {Cat}_m
   =2(2m-1)\binom{2m-2}{m-2}                          \tag{4.3}
\]

and \(\gcd(h,m^2-1)=1\) give \(h\mid C\).  Thus (4.2) is the largest cyclic
symmetry scale with no immediate shore/component divisibility obstruction.
It still does not construct the quotient forest.

An invariant construction also cannot retain one isolated literal pivot
ticket: containing one incidence edge forces its whole \(h\)-edge orbit.
Hence a single protected pivot naturally requires either explicit symmetry
breaking or a quotient construction whose entire pivot orbit is budgeted.

## 5. Parenthesis/lexical rules and the live target

The standard \(0/1\)-lexical parenthesis factor is not a viable all-\(m\)
base.  The existing exact defect theorem gives a linear number of missing
upper turns, while a canonical GMN pull spanning tree changes at most three
turn values per pull.  For \(m\ge12\), even the best correlated canonical
pull tree leaves a positive certified upper defect; at \(m=12\) the exact
lower bound is \(1941\).

Therefore:

* full cyclic \(Q_0\) symmetry fails on the order-three dimensions;
* local Latin properness alone fails beginning at \(m=4\); and
* the canonical lexical/GMN parenthesis family fails for every \(m\ge12\).

None of these statements refutes a nonlexical, symmetry-broken Hamilton
cycle with upper-turn surjectivity.  By Theorems 1.1--1.2, that is now the
smallest exact born-linear target:

\[
\boxed{
\begin{gathered}
\text{find a Hamilton cycle of }{\rm ML}_m
\text{ containing the correlated tight-pivot path,}\\
\text{whose lower-shore upper-turn map is surjective.}
\end{gathered}}                                                     \tag{5.1}
\]

Once (5.1) is supplied, \(Q_0\), the protected representative choices, the
safe opening, and the \(C-1\) component path \(Q_1\) are all explicit and
integral.  Residence, deeper upper shadows, the nonflat \(B+1\) source row,
and the lower compiler remain downstream gates.

