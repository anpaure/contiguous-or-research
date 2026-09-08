# Gate C: the Greene--Kleitman flag factor contains no coherent tour

**Status (2026-08-22).**  Everything below is proved.  The exact
three-rank flag matching supplied by an ordered Greene--Kleitman symmetric
chain decomposition cannot be rounded into coherent FIFO tours: it contains
not one whole coherent tour, for any odd \(b\ge3\).  Thus starting from the
specific exact SCD used in Appendix D is a sharp dead end for the proposed
tour grouping.  An arbitrary, non-Greene--Kleitman SCD is not ruled out.

The proof has two independent parts.  Every coherent tour projects its
\(b(b-1)\) internal flags onto \((b-1)/2\) parallel copies of a directed
Hamilton cycle on the \(2b\) ground symbols.  Every middle flag of an
ordered Greene--Kleitman SCD projects strictly backwards in one fixed total
order.  A directed Hamilton cycle cannot be strictly decreasing.

Throughout, \(|\Omega|=2b\) and \(b\ge3\) is odd.

## 1. The arc projection of a middle flag

A three-rank flag is

\[
                         L\subset C\subset U,
 \qquad |L|=b-1,\quad |C|=b,\quad |U|=b+1.           \tag{1.1}
\]

Attach to it the ordered pair of ground symbols

\[
 p(L,C,U)=C\setminus L,qquad
 q(L,C,U)=U\setminus C,                                \tag{1.2}
\]

and regard the flag as a directed arc \(p\to q\) on \(\Omega\).

For consecutive middle windows
\(C_{i-1},C_i,C_{i+1}\) in a literal word, the designated flag at
\(C_i\) is

\[
 L_i=C_{i-1}\cap C_i,qquad U_i=C_i\cup C_{i+1}.       \tag{1.3}
\]

Thus \(p_i\) is the symbol which entered when the word moved from
\(C_{i-1}\) to \(C_i\), and \(q_i\) is the symbol which enters on the
next move.  In particular,

\[
                         q_i=p_{i+1}                    \tag{1.4}
\]

whenever both consecutive starts are retained.

## 2. Exact Hamilton projection of a coherent tour

Write the coordinate pairs of a coherent tour as

\[
 P_j=\{a_j^0,a_j^1\},\qquad j\in\mathbb Z_b,
\]

in their directed cyclic order.  Relabelling inside the pairs lets us take
the initial state to be zero.  Let \(Q_s\) be the ordered boundary queue at
stage \(s\), beginning with the special pair \(P_s\).  If
\(j\in\{0,\ldots,b-1\}\), the selected bit before stage \(s\) is

\[
 \eta_s(j)=s+\mathbf1_{j<s}\pmod2,                       \tag{2.1}
\]

because each of the first \(s\) packets flips that coordinate except its
own special packet.  Hence

\[
 Q_s=\bigl(a_s^{\eta_s(s)},a_{s+1}^{\eta_s(s+1)},\ldots,
            a_{s+b-1}^{\eta_s(s+b-1)}\bigr),             \tag{2.2}
\]

with pair subscripts read modulo \(b\).

In one packet, write its middle windows as
\(C_0,C_1,\ldots,C_b\).  Its \(b-1\) retained internal flags are those at
\(C_1,\ldots,C_{b-1}\).  By (1.2)--(1.4), their arcs are precisely the
\(b-1\) consecutive arcs between entries of the packet's ending boundary
queue.  As the stage runs through \(\mathbb Z_b\), those ending queues are
just \(Q_0,\ldots,Q_{b-1}\) in cyclically shifted order.

Put \(h=(b-1)/2\).  For \(0\le j<b-1\), the pair-coordinate adjacency
\(j\to j+1\) occurs in every \(Q_s\) except \(Q_{j+1}\).  In all retained
occurrences the two bits in (2.1) agree; exactly \(h\) occurrences have
bit zero and \(h\) have bit one.  The wrap adjacency
\((b-1)\to0\) occurs in every \(Q_s\) except \(Q_0\).  Its two bits are
opposite, with each orientation occurring \(h\) times.  Therefore the arc
multiset of all \(b(b-1)\) internal flags is exactly \(h\) copies of

\[
 \boxed{
 a_0^0\to a_1^0\to\cdots\to a_{b-1}^0\to
 a_0^1\to a_1^1\to\cdots\to a_{b-1}^1\to a_0^0.}       \tag{2.3}
\]

This is one directed Hamilton cycle on \(\Omega\).  The count is exact:
\(2b h=b(b-1)\).

### Corollary 2.1 (general necessary condition)

Let \(\mathscr F\) be any disjoint three-rank flag family and let
\(D(\mathscr F)\) be its directed arc multigraph from (1.2).  If a retained
subfamily is partitioned into \(T\) whole coherent tours, then its arc
multigraph is a sum of \(T\) directed Hamilton cycles, each with
multiplicity \(h\).  Consequently every ground symbol has retained
indegree and outdegree exactly

\[
                             hT.                         \tag{2.4}
\]

Every retained arc lies in a strongly connected spanning subgraph.  In
particular, if \(m_{xy}\) is the multiplicity of arc \(x\to y\), the
threshold digraph

\[
 G_h(\mathscr F)=\{x\to y:m_{xy}\ge h\}                  \tag{2.4a}
\]

must contain a directed Hamilton cycle before even one tour is possible.
If \(D(\mathscr F)\) is acyclic, no flag can belong to a whole tour.
More quantitatively, for every nonempty proper \(S\subset\Omega\), each
projected Hamilton cycle crosses the cut at least once in each direction.
Thus, if \(R\) flags can be grouped,

\[
 |\delta^+_{D(\mathscr F)}(S)|,
 |\delta^-_{D(\mathscr F)}(S)|\ge {R\over2b},
 \qquad
 R\le2b\min_S\min\{|\delta^+(S)|,|\delta^-(S)|\}.       \tag{2.4b}
\]

For a partition into \(r\ge2\) nonempty parts, the total number of retained
cross-part arcs is at least \(rR/(2b)\).  Finally, if \(d^+,d^-\) are the
original degrees, then

\[
 R=b(b-1)T,qquad
 {R\over2b}=hT,qquad
 |\mathscr F|-R\ge {1\over2}
       \sum_{v\in\Omega}|d^+(v)-d^-(v)|.                 \tag{2.5}
\]

The last inequality holds because deleting one arc changes the total
absolute imbalance by at most two, while a union of Hamilton cycles is
balanced.  These conditions are necessary, not sufficient: the middle-set
incidences and the division of each Hamilton projection into its \(b\)
FIFO packets still have to agree.

## 3. Ordered Greene--Kleitman flags are acyclic

Fix any total order

\[
                         \omega_1<\omega_2<\cdots<\omega_{2b}             \tag{3.1}
\]

and form the Greene--Kleitman SCD in that coordinate order.  In its usual
bracketing, scan the zero--one membership word from left to right and pair
each zero with the latest unpaired one to its left.  Once the paired
coordinates are fixed, the unpaired coordinates consist of a block of
zeros followed by a block of ones.  Moving the cut through them is the
corresponding saturated symmetric chain.

Consider a chain which crosses all three ranks \(b-1,b,b+1\), and let
\(L\subset C\subset U\) be its middle flag.  At rank \(b\), its unpaired
word has at least one zero and one one.  The edge from \(L\) to \(C\)
flips the **leftmost unpaired one**, while the edge from \(C\) to \(U\)
flips the **rightmost unpaired zero**.  Since every unpaired zero precedes
every unpaired one,

\[
                         q(L,C,U)<p(L,C,U).             \tag{3.2}
\]

Thus every arc (1.2) of the Greene--Kleitman middle-flag factor points
strictly backwards in the one fixed order (3.1).  Its arc multigraph is a
DAG.

The SCD has exactly

\[
 N=\binom{2b}{b-1}={b\over b+1}\binom{2b}{b}             \tag{3.3}
\]

such flags: every rank-\((b-1)\) set lies on a unique chain, and that chain
also crosses ranks \(b,b+1\).  The flags are disjoint in all three ranks.
Only
\(\binom{2b}{b}/(b+1)\) singleton middle chains are omitted, an
\(O(1/b)\) middle fraction.

### Theorem 3.1 (zero-tour obstruction)

No coherent \(b\)-packet tour has all of its \(b(b-1)\) internal flags in
one ordered Greene--Kleitman SCD.  Hence no positive number of the exact
flags in (3.3), let alone all but \(o(N)\), can be grouped into whole
coherent tours.

#### Proof

If such a tour existed, (2.3) would put a directed Hamilton cycle inside
the arc multigraph of the SCD flag factor.  Equation (3.2) makes that
multigraph acyclic.  Equivalently, following (2.3) would give the impossible
strict cycle

\[
 a_0^0>a_1^0>\cdots>a_{b-1}^0>a_0^1>\cdots>
 a_{b-1}^1>a_0^0.
\]

This contradiction proves the theorem. \(\square\)

The argument is invariant under an arbitrary relabelling or reversal of
the total coordinate order.  It therefore rules out every ordered or
relabeled Greene--Kleitman SCD, not only the displayed standard order.

### Corollary 3.2 (minimum flag-changing scale)

Suppose coherent tours are allowed to use both Greene--Kleitman flags and
exceptional replacement flags.  Every directed Hamilton cycle has at
least one arc which is not strictly decreasing in (3.1).  By (2.3), that
arc occurs with multiplicity \(h=(b-1)/2\) inside its tour, and none of
those \(h\) flags can be a Greene--Kleitman flag.  Therefore \(T\)
vertex-disjoint tours require at least \(hT\) exceptional flags.  If their
internal flag count is \(R=b(b-1)T\), then

\[
 \boxed{\#\{\text{exceptional flags}\}\ge {R\over2b}.}    \tag{3.4}
\]

Thus a repair covering \((1-o(1))N\) flags must change at least
\((1-o(1))N/(2b)\) of them.  This is a genuine lower bound but still
\(o(N)\), so it does not rule out a carefully organized vanishing-fraction
switching repair.

## 4. What this does and does not close

The obstruction is stronger than a bad codegree estimate: the relevant
tour hypergraph induced on the Greene--Kleitman flag factor has no edges.
Consequently the exact alternating GK retirement theorem cannot be used as
the flag factor and then rounded wholesale into coherent tours.  Its
abstract all-offset assignment remains valid, but the physical lift must
change the flags themselves.

Corollary 2.1 gives the correct first audit for another SCD.  Its middle
flag arc multigraph must contain an almost-spanning, almost-regular
decomposition into \(h\)-fold directed Hamilton cycles.  Even that would
only close the emission-label projection.  One must still prove that the
flags on each Hamilton projection have the exact middle sets and packet
order of a coherent tour, and then control all deeper SCD members as
literal offset windows.

This theorem does not rule out a deliberately non-Greene--Kleitman SCD,
an exact three-rank flag matching not extended to a full SCD, a mixture of
different SCDs followed by trades, or changing an \(o(N)\) set of flags
*after* a separate coherent-tour packing has been found.  Corollary 3.2
shows that the last option costs at least \(\Omega(N/b)\).  The theorem shows
that the most direct order-fixed SCD-first route has zero, rather than
merely insufficient, support.

The arbitrary-SCD caveat is real, rather than formal.  On
\(\{0,1,2,3\}\), the following six chains form an SCD:

\[
\begin{gathered}
 \varnothing\subset0\subset03\subset023\subset0123,\\
 1\subset01\subset013,\qquad
 2\subset12\subset012,\qquad
 3\subset23\subset123,\\
 02,\qquad13.
\end{gathered}                                             \tag{4.1}
\]

Here strings denote their sets of digits.  The four three-rank flags have
arcs \(3\to2,0\to3,1\to0,2\to1\), which form the directed Hamilton cycle
\(0\to3\to2\to1\to0\).  Hence acyclicity is a special consequence of the
single ordered Greene--Kleitman construction, not an invariant of all
symmetric chain decompositions.  Example (4.1) is only a scope witness at
\(b=2\), not a construction for the odd-\(b\) tour problem.

## 5. Finite audit

The companion checker

`scratch/verify_gate_c_gk_scd_coherent_tour_obstruction_20260822.py`

enumerates the Greene--Kleitman middle flags for \(2\le b\le10\), verifies
their exact count, disjointness, and strict order descent, and constructs
the coherent-tour arc multiset for every odd \(3\le b\le31\), verifying
that it is exactly \((b-1)/2\) copies of (2.3).  It also verifies the full
SCD and Hamilton flag projection in (4.1).  The checker is
confirmatory; all proofs are contained above.
