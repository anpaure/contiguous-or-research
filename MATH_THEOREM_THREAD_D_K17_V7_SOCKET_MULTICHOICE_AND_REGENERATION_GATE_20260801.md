# The k=17 v7 compact-socket bank: raw support, contextual zeros, and the exact multi-choice regeneration gate

> **Independent referee companion.**  The consolidated authoritative
> formulation, including exact cut-OR and option-dependent baseline rows, is
> `MATH_THEOREM_THREAD_D_K17_V7_SOCKET_MULTICHOICE_AND_REGENERATIVE_GATE_20260801.md`.
> This file is retained as an independent derivation/audit; use the
> consolidated note if wording differs.

**Date:** 2026-08-01  
**Scope:** pure mathematics and solver-free audit of the authenticated finite
`m=9` catalogue.  This note proves an exact catalogue-relative selector and a
rank-ten regeneration lemma.  It does **not** prove that the selector is
feasible, construct a Hamilton path, close ranks eleven through fifteen, or
solve common cap/compiler constraints.

The noncanonical pivot-rich geodesic packet is treated as proved and
available.  Nothing below calls that packet missing.  The issue here is the
simultaneous physical placement of compact facet sockets, guards, component
options, lower colours, and upper witnesses.

## 1. Rebase from v5 to v7

The earlier v5 result concerned one frozen bank of thirty sockets and `6252`
intact pieces.  Its raw endpoint zeros and immutable lower repeats remain
correct on that fixed face.  They are not invariants of the socket method.

The authoritative v7 bank instead has

\[
 38\text{ sockets},\qquad 6258\text{ resident pieces},\qquad
 24310\text{ distinct rank-nine owners}.
\]

The pieces have no internal positive coordinate run of length below four.
Their internal upper-hole counts at ranks ten through fifteen are

\[
          1485,2454,1593,553,99,9.                 \tag{1.1}
\]

The exact two-piece census has zero raw-support rows at none of these ranks.
After imposing the necessary context-extendability test, however, the zero
counts become

\[
             100,4,0,0,0,0.                       \tag{1.2}
\]

The four rank-eleven zeros are

\[
             32244,32377,72511,73451.              \tag{1.3}
\]

Thus v7 removes the v5 raw rank-ten obstruction, but it does not remove the
residence-compatible placement obstruction.

## 2. Why raw support and contextual support differ

### Lemma 2.1 (rank-ten seam locality)

Let \(T_i,\ldots,T_j\) be a nontrivial consecutive interval of distinct
rank-nine Johnson neighbours.  If its union is a rank-ten set \(U\), then

\[
                    T_k\cup T_{k+1}=U
       \qquad(i\leq k<j).                           \tag{2.1}
\]

#### Proof

Every \(T_k\) is a rank-nine subset of \(U\).  Two distinct rank-nine
subsets of a ten-set omit different coordinates, so their union is the
whole ten-set. \(\square\)

Consequently rank-ten coverage is an edge-colour condition.  This is the
reason the rank-ten child ledger below is linear.

### Lemma 2.2 (the extendability test is necessary)

Let \(P,Q\) be two oriented resident pieces.  For coordinate \(b\), write
\(s_P(b)\) for the terminal one-run length of \(P\), \(p_Q(b)\) for the
initial one-run length of \(Q\), and \(a_P(b),a_Q(b)\) for the indicators
that the corresponding whole piece is constantly one in coordinate \(b\).
If \(P\mid Q\) lies in a chronology with minimum positive run four, then:

* if both seam endpoints contain \(b\) and
  \(s_P(b)+p_Q(b)<4\), at least one of \(a_P(b),a_Q(b)\) is one;
* if only the left endpoint contains \(b\) and \(s_P(b)<4\), then
  \(a_P(b)=1\);
* if only the right endpoint contains \(b\) and \(p_Q(b)<4\), then
  \(a_Q(b)=1\).

#### Proof

If neither relevant piece is constantly one, the short run is bracketed by
literal zeros inside the two pieces.  Exterior pieces cannot lengthen it.
The one-sided cases are identical. \(\square\)

Passing this test is not sufficient: a constantly-one piece transfers the
unfinished run obligation to its other boundary.  The whole selected path
must still pass the run automaton.  But failure is an absolute local
obstruction.  Hence the 100 rows in (1.2) cannot be repaired by any ordinary
pairwise seam between the frozen v7 pieces, despite their raw seams.

## 3. The individual L3 sockets and their first cascade

For every one of the 100 context-zero rank-ten targets, the frozen catalogue
contains an individually resident compact three-facet socket with two guard
states.  The sum of its individually additional cuts is

\[
                         213.                       \tag{3.1}
\]

Ninety-nine rows have no unsupported child colour relative to the
extendable prebank atlas.  The sole exceptional row is

\[
             75749\longrightarrow14309,             \tag{3.2}
\]

while its other exported child `91109` has ordinary extendable support.
The target `14309` itself has compact clean sockets.

This closes the **setwise dependency depth**, not the physical selector.
In particular, the first generation-3 L3 and L4 sockets for `14309` use
right guard segment `755`, which is already the left guard segment of the
frozen v7 socket `69605`.  They therefore cannot coexist with that frozen
socket.  A different round-one L3 row, with facets

\[
                       14308,13285,10213,             \tag{3.3}
\]

is clean and compatible with the frozen 38, but it shares facet `10213`
with the displayed L3 parent socket for `75749`.  Thus it does not close
the displayed parent-child pair.  The generation-3 L5 socket

\[
 14308,14277,14245,14181,14053                       \tag{3.4}
\]

uses guard segments `558,798`, has seven additional cuts, has no
unsupported child, and is disjoint from every frozen v7 socket in the three
audited elementary resource classes: facet occurrences, guard segments, and
fixed minimum component-option conflicts.  Thus the child is not an
intrinsic obstruction, but its repair already requires a genuine
multi-choice catalogue with variable socket length.

### Proposition 3.1 (the displayed representatives are not a packing)

Choosing the one displayed L3 row for each of the 100 targets uses 300 facet
occurrences but only 290 distinct facets.  The repeat excess is ten.
Moreover thirteen original components are assigned two or more different
minimum residence options.

Relative to the frozen 38-socket bank, 62 of the 100 rows have at least one
elementary incompatibility: 45 reuse a frozen facet, 12 reuse a frozen guard
segment, and 34 demand a different minimum option on a frozen component.
These classes overlap.

#### Proof

This is direct incidence counting in the literal catalogue.  A facet owner
is a physical occurrence and has capacity one.  A guard segment cannot be
simultaneously embedded into two different macro words.  Finally a frozen
component cannot realize two distinct minimum cut options at once. \(\square\)

The option conflict is scoped: a nonminimum union of cuts or a different
old-socket choice may resolve it.  Proposition 3.1 therefore refutes only
independent installation of the displayed rows.  It is not a no-go for the
full multi-choice problem.

There are two stronger finite confirmations of that scope.

* Freezing the 38 old sockets plus one advertised child row and allowing
  only the published one-L3/one-L4 menu gives 88 locally dead targets; the
  resulting CNF is UNSAT by propagation.  With the compatible L5 child and
  physical conflicts alone, 87 targets still have no row.  This proves that
  the sockets cannot simply be bolted onto v7.
* A richer individual L3 enumeration has `283836` rows.  Against one frozen
  39-row bank it still has five zero targets

  \[
                   70650,75749,77748,81081,81578.     \tag{3.5}
  \]

  This remains a frozen-bank statement, not a no-go after reselecting the
  old sockets.  It does prove that old-socket reselection is necessary in
  that catalogue.

## 4. The lower repeat ledger must be reselected too

The 6258 intact v7 pieces contain

\[
 18052\text{ internal edges},\quad17974\text{ distinct rank-eight colours},
 \quad78\text{ repeat units on }77\text{ colours}.             \tag{4.1}
\]

A Hamilton path on the pieces has only 6257 external seams.  Even if all
those seams supply new lower colours, it uses at most

\[
                       17974+6257=24231
\]

of the 24310 lower colours.  Thus an intact-piece path has at least 79
lower holes.  At least 78 repeated internal occurrences must be released
or otherwise rethreaded before the single forced path-boundary hole is
possible.

This is the v7 replacement for the old v5 repeat ledger.  The 213 individual
socket cuts are ample only in scalar count; their colours and mutually
compatible component options have to be selected jointly.

## 5. Exact rank-ten multi-choice formulation

Let \(\mathcal C\) be the original component set.  For each component
\(C\), let \(\Omega_C\) be its allowed residence-cut options.  Let
\(\mathcal S_U\) be the literal compact-socket options serving rank-ten
target \(U\), and let \(\mathcal A\) be the allowed oriented external seam
arcs after fragmentation.

Each socket option \(s\) records:

1. its ordered facet occurrences and two guard states;
2. the required option/cuts in each touched component;
3. every lower colour removed and inserted;
4. its rank-ten service multiset \(G_s\) and casualty multiset \(L_s\);
5. its complete rank-eleven--fifteen accumulated-union transfer relation;
6. its run-automaton input/output state, endpoint tickets, and common-cap
   state.

Use binary variables \(x_s\), \(y_{C,\omega}\), and \(e_a\) for sockets,
component options, and external arcs.  The exact elementary rows are

\[
 \sum_{\omega\in\Omega_C}y_{C,\omega}=1,             \tag{5.1}
\]

\[
 x_s\leq y_{C,\omega_C(s)}quad(C\text{ touched by }s),          \tag{5.2}
\]

\[
 sum_{s:f\in F(s)}x_s\leq1                         \tag{5.3}
\]

for every physical facet occurrence \(f\), together with the analogous
guard-state and owner-partition rows.

Let \(m_T^{\rm int}(x,y)\) denote the multiplicity of rank-ten edge colour
\(T\) in the literal selected atomic and macro words before external seams.
This is a linear column sum once every local replacement column contains its
complete removed/inserted edge ledger.  Equivalently, on a disjoint
reference face it is the reference multiplicity plus the signed
\(G_s-L_s\) columns.  By Lemma 2.1 the exact rank-ten row is

\[
 m_T^{\rm int}(x,y)
       +\sum_{a\in\mathcal A:\,\operatorname{up}(a)=T}e_a\geq1. \tag{5.4}
\]

No proxy child-support row is needed once (5.4) is imposed literally;
the child language is a sparse Benders decomposition of this equation.

For every rank-eight colour \(K\), exact lower q1 is

\[
 m_K^{\rm int}(x,y)+
 \sum_{a:\,\operatorname{low}(a)=K}e_a
       =1-\mathbf1_{K=K_*},                          \tag{5.5}
\]

where \(K_*\) is the unique linear-boundary colour.  The coordinatewise
repeat-upper cocycle is a consequence of (5.5), the owner deck and the two
endpoint owners, but is useful as an eager redundant row.

Degree at most one at every selected piece/macro endpoint, total edge count,
and graphic acyclicity give a single Hamilton path.  The full run automaton,
not merely Lemma 2.2, enforces residence.

### Theorem 5.1 (catalogue-relative exactness)

There is a resident Hamilton owner path obtainable from the stated atomic
and socket catalogues, with exact lower q1 and complete rank-ten coverage,
if and only if the binary system (5.1)--(5.5), the owner/resource partition,
endpoint degree, graphic, and run-automaton rows has a solution.

#### Proof

A physical path selects one literal component option, every socket it uses,
and all external successor arcs; reading these choices gives the binary
solution.  Conversely, the owner partition and capacity rows make the
selected macro words disjoint, the degree and graphic rows order them into
one path, and the run automaton proves residence.  Equations (5.4) and
(5.5), using Lemma 2.1, are exactly the two q1 palette statements. \(\square\)

## 6. Regenerative child closure

For a selected socket \(s\), draw a directed dependency \(U\to V\) whenever
\(s\) serves parent \(U\) and creates one unit of rank-ten casualty \(V\)
not assigned to a selected ordinary seam.  Suppose:

1. the selected socket words and ordinary services satisfy all resource,
   option, degree and residence rows;
2. every initial zero target is served by a selected socket;
3. every dependency has either a selected child socket or a selected
   ordinary service; and
4. the dependency digraph admits a potential strictly decreasing along
   every socket-to-socket dependency.

Then all rank-ten rows (5.4) hold.

#### Proof

Process the dependency vertices in increasing potential.  A terminal debt
has its selected ordinary service.  Inductively, the selected child socket
replaces the demanded colour, and all casualties it exports have already
been discharged.  Since the resource rows make these literal witnesses
simultaneous, no witness is counted twice. \(\square\)

For the present individual census the abstract dependency depth is only two:
the unique unsupported arrow is (3.2), and (3.4) is child-clean.  Proposition
3.1 shows exactly why this does not yet meet hypothesis 1.

## 7. Ranks eleven through fifteen

Ranks above ten are not edge colours.  If the final owner word is
\(T_1,\ldots,T_N\), let \(\mathcal E_i\) be the set of unions of intervals
ending at \(i\), truncated above rank fifteen.  The exact recurrence is

\[
 \mathcal E_i=\{T_i\}\cup
 \{A\cup T_i:A\in\mathcal E_{i-1},\ |A\cup T_i|\leq15\}.       \tag{7.1}
\]

Recording every state of ranks eleven through fifteen gives complete
arbitrary-width separation.  A socket macro has a finite transfer relation
obtained by composing (7.1) through its literal word.  The exact upper rows
require every target to be recorded at least once.

The four masks in (1.3) have no context-extendable two-piece service in the
frozen bank.  The present rank-ten L3 table does not record enough transfer
data to claim that its selected macros cover them.  They and all remaining
rank-eleven--fifteen targets must therefore stay in the joint selector via
(7.1).

## 8. Exact surviving gate

The finite obstruction is no longer raw rank-ten incidence and is not the
pivot-rich packet.  It is the following correlated choice:

* reselect the old 38 sockets and choose one compatible macro service for
  each of the 100 contextual rank-ten zeros;
* include a compatible clean realization of the `75749 -> 14309` cascade;
* release the v7 lower repeat units and satisfy the complete lower equations;
* select one residence-valid graphic successor path;
* satisfy the accumulated-union recurrence at ranks eleven through fifteen;
* then satisfy common cap and the lower compiler.

Pairwise socket existence proves none of these correlations.  Conversely,
Theorem 5.1 and recurrence (7.1) isolate a proof-safe exact master; an UNSAT
result for any smaller frozen-row face must remain scoped to that face.
