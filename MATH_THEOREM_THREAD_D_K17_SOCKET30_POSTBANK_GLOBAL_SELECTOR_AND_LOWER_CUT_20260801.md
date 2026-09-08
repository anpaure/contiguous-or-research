# The frozen k=17 socket-30 postbank has an exact global selector, but its
# immutable lower repeat current forbids a compiler-ready seam-only path

Date: 2026-08-01  
Lane: D / resident facet socket / postbank completion  
Status: **exact selector equivalence and a solver-free obstruction for the
fixed 6,252-piece bank.  No obstruction is asserted after internal
component splitting or rethreading, and no k=17 word is claimed.**

## 1. Frozen data

Use the authenticated v5 bank of
`MATH_THEOREM_K17_SCD_COMPACT_SOCKET_BANK_AND_UPPER_CASUALTY_LEDGER_20260801.md`.
After the 30 sockets are installed, the rank-nine owner set is partitioned
into

\[
                 P=6252
\]

internally resident directed-path pieces.  The pieces contain all

\[
                 W={17\choose8}=24310
\]

owners exactly once.  Reversing a piece changes its endpoint state, but not
the multiset of its internal rank-eight intersections or rank-ten unions.

## 2. The exact global selector

For each piece \(p\) and orientation \(\epsilon\), write
\(s=(p,\epsilon)\), and let

\[
 w(s)=(X^s_0,\ldots,X^s_{\ell_s-1}).
\]

Let \(a(s),b(s)\) be its first and last owner.  A directed seam
\(e=(s,t)\) is Johnson-legal when

\[
 |b(s)\mathbin\triangle a(t)|=2.                              \tag{2.1}
\]

Its lower and immediate-upper colours are

\[
 \lambda(e)=b(s)\cap a(t),\qquad \upsilon(e)=b(s)\cup a(t).   \tag{2.2}
\]

For each coordinate, a five-state automaton \(0,1,2,3,4\) records the
current positive-run length, capped at four.  A transition from state
\(1,2,3\) to a zero is forbidden.  Every oriented piece induces a
deterministic transformation of these 17 automata.  Hence composition of
the piece transformations is **equivalent**, not merely sufficient, to
depth-three residence (with the declared clipping convention at the two
global endpoints).

For an upper target \(T\), define the accumulated-union automaton

\[
 A\longmapsto
 \begin{cases}
   A\cup X,&X\subseteq T,\\
   \varnothing,&X\not\subseteq T,
 \end{cases}                                                   \tag{2.3}
\]

while scanning the owner cells.  It accepts once \(A=T\).

### Lemma 2.1 (arbitrary-width exactness)

For every target \(T\) of rank 10 through 15, (2.3) accepts if and only if
some nonempty consecutive owner interval has union exactly \(T\).

#### Proof

Every witnessing interval consists only of owners contained in \(T\), so
it lies in one maximal consecutive \(T\)-compatible block.  The union of
that maximal block contains \(T\) and is contained in \(T\), hence equals
\(T\).  Conversely, an accepting maximal block is itself a witness.
\(\square\)

Thus the exact integer selector consists of:

1. one orientation for every piece;
2. one incoming and one outgoing seam at every nonterminal piece and one
   missing incidence at each of the two terminals;
3. \(P-1\) seams and graphic acyclicity, equivalently one directed
   Hamilton path on the pieces;
4. the 17 residence automata;
5. the accumulated-union acceptance row (2.3) for every missing target of
   ranks 10 through 15;
6. the lower-colour and common-cap rows required by the compiler.

This is a finite exact formulation.  A one-seam suffix/prefix atlas is a
valid provider subcatalogue, but is not complete for ranks 11 through 15:
their witness interval may cross several seams.  The automaton (2.3) is
the required proof-safe replacement.

The selector is not a network matrix.  Even after fixing orientations and
removing rows 4--6, choosing coloured seams with distinct tails and heads
is a rainbow matching in a bipartite graph; adding the underlying graphic
row is a third independence system.  Therefore ordinary max-flow/TU is
not justified.  Rows 4 and 5 add shared-history coupling.

## 3. Exact rank-ten repeat cocycle

The fixed pieces contain 18,058 internal edges.  Their rank-ten union
multiset has

\[
 17990\text{ distinct colours},\qquad 68\text{ repeat units},
\]

and therefore 1,458 holes among the \({17\choose10}=19448\) rank-ten
targets.

A Hamilton concatenation adds 6,251 seams.  If its rank-ten deck is
complete, exactly 1,458 selected seams are first providers of the internal
holes, and its forced seam repeat quota is

\[
 6251-1458=4793.                                               \tag{3.1}
\]

Together with the 68 internal repeats this gives

\[
 4793+68=(W-1)-{17\choose10}=4861,                             \tag{3.2}
\]

the exact endpoint cocycle.  Thus the parent repeats are not fungible
child providers: every rank-ten hole still needs its named first-provider
seam, while all other seams are forced into the repeat ledger.

There is also a coordinatewise form which is the correct repeat-cocycle
row for a nonexact lower deck.  Let \(\mathcal H\) be the multiset of
missing rank-eight colours, let \(\mathcal L\) be the excess-occurrence
multiset beyond the first copy of each present rank-eight colour, and let
\(\mathcal R\) be the excess-occurrence multiset beyond the first copy of
each rank-ten colour.  If the rank-ten deck is complete, edge count gives

\[
                       |\mathcal H|=|\mathcal L|+1,             \tag{3.3}
\]

and for every coordinate \(q\),

\[
 \boxed{d_{\mathcal R}(q)
 =2860+d_{\mathcal H}(q)-d_{\mathcal L}(q)
       -\mathbf1_{q\in T^-}-\mathbf1_{q\in T^+}.}              \tag{3.4}
\]

Here \(T^-,T^+\) are the two endpoint owners and
\(2860=2\operatorname{Cat}_8\).

Indeed every Johnson edge \(XY\) satisfies

\[
 \mathbf1_{X\cap Y}+\mathbf1_{X\cup Y}
 =\mathbf1_X+\mathbf1_Y.
\]

Sum over the path, substitute one copy of the complete lower and upper
palettes, and use that every coordinate belongs to
\({16\choose8}=12870\) owners and to \({16\choose7}=11440\) members of
each colour shore.  This proves (3.4).  The scalar quota (3.2) is only its
cardinality projection.  Thus lower releases, endpoint choice, and upper
repeat placement have to be selected jointly.

The internal missing counts at ranks 10 through 15 are respectively

\[
                 1458,2429,1583,549,101,10.                   \tag{3.5}
\]

For ranks 11--15 these are acceptance demands in (2.3), not independent
one-seam colours.

### Theorem 3.1 (seven intact-piece upper obstructions)

If a rank-ten target \(T\) is the union of a nontrivial consecutive block
of rank-nine Johnson owners, then an adjacent pair in that block has union
\(T\).  Consequently an internally missing rank-ten target can be covered
after concatenating intact pieces only if two endpoint facets of \(T\)
occur on distinct pieces.

For the frozen postbank, exhaustive endpoint incidence (with both
orientations allowed and with residence ignored) gives exactly seven
rank-ten holes with no such ordered pair:

\[
 \boxed{20427,69555,70910,72414,72566,73649,83946.}             \tag{3.6}
\]

#### Proof

Every owner in a witnessing interval is a rank-nine subset of \(T\).
Distinct rank-nine subsets of a ten-set omit different coordinates and
therefore have union \(T\).  In particular the first adjacent pair already
has union \(T\).  Internal pairs were included in the frozen internal
deck, so a remaining witness must be an inter-piece endpoint pair.  The
finite endpoint census checks all \(2P\) oriented states and all ordered
adjacencies of distinct pieces and returns (3.6). \(\square\)

Each target in (3.6) has only one currently exposed endpoint facet.  The
only possible sharing of a newly exposed facet is

\[
                 69555\cap73649=69553
\]

of rank nine.  Hence at least six new endpoint owners, and therefore at
least three internal cuts, are necessary before all seven rows can acquire
even raw seam support.  This lower bound ignores residence and is allowed
to overlap the 53 lower-release cuts below.

The row 69555 is itself in the socket bank's named child-colour ledger.
Thus “an extendable provider existed in the prebank atlas” is not a
postbank selection theorem: after the 30 macros and their component options
are materialized into intact pieces, that child has no raw endpoint-pair
provider.  It has to be exposed again by a prospective split/rethread.

Thus the intact-piece selector is already infeasible on rank ten alone.
Ranks 11--15 remain governed by the automaton (2.3) after prospective
splitting; they are not implicated in this rank-ten no-go.

## 4. The immutable lower-current obstruction

Let \(m^-_L\) be the number of internal edges of the frozen pieces having
rank-eight colour \(L\), and put

\[
 R^-:=\sum_L(m^-_L-1)_+.
\]

### Theorem 4.1 (fixed-piece lower cut)

For every ordering and orientation of \(P\) fixed pieces, joined by one
Johnson seam between consecutive pieces, the number of absent rank-eight
colours is at least

\[
                         R^-+1.                                \tag{4.1}
\]

If \(b\) additional nonowner boundary transitions are permitted, the
bound is \((R^-+1-b)_+\).

#### Proof

There are \(W-P\) internal edges.  Their number of distinct lower colours
is \(W-P-R^-\).  Reversal preserves every internal intersection.  The
\(P-1\) inter-piece seams can contribute at most \(P-1\) further colours,
so the complete chronology has at most

\[
 (W-P-R^-)+(P-1)=W-1-R^-
\]

distinct rank-eight colours out of the universe of size \(W\).  Each
extra boundary transition raises this upper bound by at most one.
\(\square\)

For the v5 postbank the audit gives

\[
 \#\{\text{internal lower colours}\}=18005,
 \qquad R^-=18058-18005=53.                                   \tag{4.2}
\]

Consequently every seam-only Hamilton path on the frozen pieces misses at
least

\[
                         54                                   \tag{4.3}
\]

rank-eight colours.  Even one terminal nonowner transition leaves at
least 53 holes.

All 53 repeated colours have multiplicity exactly two.  If internal edges
are prospectively released, cutting a unique-colour edge both deletes one
internal colour and creates one extra seam slot, for net lower gain zero.
Cutting one occurrence of a duplicated colour preserves that internal
colour and creates one extra seam slot, for net gain one.  Cutting its
second occurrence again has net gain zero.  Hence any exact repair must
satisfy the 53 literal rows

\[
 \boxed{\sum_{e\in E^{\rm int}_L}d_e\ge1
        \quad\text{for every internally duplicated lower colour }L,}    \tag{4.4}
\]

where every \(E^{\rm int}_L\) in (4.4) has size two.  In particular,
53 internal releases are necessary, and one release from each pair is the
unique minimum-cardinality lower repair pattern at the level of colours.
The audit JSON records the 53 pairs with their piece, offset, and lost
rank-ten union.

There is no background-only escape.  Of the 53 duplicate rows,

\[
 52\text{ consist of one residual edge and one socket edge},\qquad
 1\text{ consists of two socket edges}.                         \tag{4.5}
\]

The socket--socket row has lower colour 31968 and lies in the sockets with
targets 31988 and 97508.  Therefore preserving all 30 socket pieces intact
is already incompatible with the exact lower palette: at least one socket
must itself be split, or a nonstandard physical lower provider must be
added.  If socket internals are protected, the 52 other rows force their
residual counterpart edges to be released, exporting the corresponding 52
named rank-ten unions.  This is the literal child-provider correlation that
an aggregate repeat count misses.

This obstruction is independent of the candidate seam catalogue,
residence, topology, and every upper target at ranks 10--15.  Therefore
the full compiler-ready selector on the frozen 6,252 pieces is infeasible.
At least 53 internal repeat units must be released by component splitting,
internal rethreading, or an equally large bank of additional physical
transitions.  The theorem does **not** rule out a resident Hamilton path
when the lower palette is ignored, nor a repaired postbank in which those
internal edges are released.

## 5. Sharp surviving gate

The next proof-safe model must make the release variables prospective and
install (4.4) eagerly.
For every released internal edge, its lost upper occurrences at ranks
10--15 and its lower colour enter one signed column; replacement seams or
hyperarcs enter the opposite column.  The selector must then enforce:

* elimination of all 53 lower repeat units and restoration of the released
  lower colours;
* the rank-ten first-provider/repeat cocycle (3.1)--(3.2);
* accumulated-union acceptance (2.3) at ranks 11--15;
* owner/head capacity, residence, and graphic/path rows.

This is the precise correlated child-provider/repeat-cocycle problem left
by the v5 bank.  Solving only the frozen seam ordering cannot close it.

## Artifacts

* `scratch/k17_socket30_postbank_pieces_20260801.json`;
* `scratch/k17_socket30_postbank_piece_deck_20260801.audit.json`;
* `scratch/audit_threadD_k17_socket30_rank10_zero_rows_20260801.py`;
* `scratch/threadD_k17_socket30_rank10_zero_rows_20260801.audit.json`;
* `scratch/audit_threadD_k17_socket30_postbank_selector_20260801.py`;
* `scratch/threadD_k17_socket30_postbank_selector_20260801.audit.json`;
* `scratch/audit_threadD_k17_socket30_postbank_global_selector_20260801.py`;
* `scratch/threadD_k17_socket30_postbank_global_selector_20260801.audit.json`.
