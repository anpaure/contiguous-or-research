# K17 bottom-token perfect matching and compound relay circuits

**Date:** 2026-08-02  
**Status:** exact static-table sharpening of
`MATH_THEOREM_K17_COMPOUND_RELAY_PATH_COLUMN_AND_INTERNAL_STATE_CANCELLATION_20260802.md`.
That theorem already proves the donor-assignment/path normal form and the
authenticated compound path.  The new content here is the square augmented
perfect-matching equivalence, its dummy-free TU formulation, exact Hall
cuts, additive min-cost interface, and the all-dimensional movable-bottom
lemma.  It does **not** prove a common-state `1S` cycle cover,
residence, upper coverage, topology, a compiler, or a `24313` word.

## 0. Result

The current three-level K17 table has the following mutable rows.

* `1748` singleton rows
  \[
                         f:(R_f),\qquad f\in\mathcal F.
  \]
* `18646` eligible hard rows
  \[
                  a:(B_a,M_a,R_a),\qquad a\in\mathcal H,
  \]
  with
  \(B_a\subsetneq M_a\subsetneq R_a\).

The `17` rank-one-bottom long rows and the `3899` old length-two rows are
fixed and are not members of \(\mathcal H\).

Ordinary recoupling moves one bottom target \(B_a\) from its hard row to a
singleton row.  A status relay moves a bottom target from one hard slot to
another.  The older atomic outer master represented only pairwise
row-disjoint moves.  The compound-relay theorem removes that restriction by
donor paths.  The present formulation contracts the entire donor path/cycle
language into one ordinary perfect matching.

Create an augmented bipartite graph \(G_{\rm bot}\) with left shore

\[
              L=\{b_a:a\in\mathcal H\}\mathbin{\dot\cup}\mathcal U,
              \qquad |\mathcal U|=1748,
\]

and right shore

\[
              R=\mathcal F\mathbin{\dot\cup}\mathcal H^{\rm slot}.
\]

Thus both shores have size

\[
                         18646+1748=20394.             \tag{0.1}
\]

The vertices \(b_a\) are the named bottom targets.  The vertices in
\(\mathcal U\) are indistinguishable dummy tokens.  Put in exactly the
following edges:

\[
\begin{aligned}
 b_a f&\in E &&\Longleftrightarrow B_a\subsetneq R_f,\\
 b_a v&\in E &&\Longleftrightarrow B_a\subsetneq M_v,\\
 u v&\in E &&(u\in\mathcal U,\ v\in\mathcal H^{\rm slot}),
\end{aligned}                                           \tag{0.2}
\]

and no dummy is adjacent to a singleton row.

### Main theorem

Perfect matchings of \(G_{\rm bot}\), modulo permutation of the dummy
tokens, are in bijection with all exact static bottom-relocated K17 tables.
Every such table has chain histogram

\[
                         (x_1,x_2,x_3)=(0,7395,16915), \tag{0.3}
\]

keeps every owner and root on its original physical row, and partitions all
named lower targets exactly once.

Consequently the complete outer payload face is an ordinary bipartite
perfect-matching polytope.  It is integral.  Atomic status relays are
alternating four-cycles involving one dummy; arbitrary compound relay paths
and cycles are ordinary alternating matching circuits.

The common-state/socket master must still be built over these matching
edges.  Integrality of the outer matching does not imply integrality, or
even feasibility, after literal state records are imposed.

## 1. Materialization map

Let \(P\) be a perfect matching of \(G_{\rm bot}\).

* If \(P\) contains \(b_a f\), replace singleton row \(f\) by
  \[
                              (B_a,R_f).              \tag{1.1}
  \]
* If \(P\) contains \(b_a v\), replace hard row \(v\) by
  \[
                              (B_a,M_v,R_v).          \tag{1.2}
  \]
* If the hard slot \(v\) is matched to a dummy, replace it by
  \[
                              (M_v,R_v).              \tag{1.3}
  \]

All fixed rows are retained literally.

### Theorem 1.1 (exact materialization)

The materialized rows form an exact strict-chain target partition, retain
the original owner/root assignment of every physical row, and have the
histogram (0.3).

#### Proof

No dummy is adjacent to \(\mathcal F\).  Hence every one of the `1748`
singleton rows is matched to exactly one real bottom token and becomes a
length-two row of the form (1.1).

Every real bottom token \(b_a\) is matched once.  It therefore occurs
exactly once, either in (1.1) or in (1.2).  Every hard slot is matched once;
it is long when matched to a real token and short when matched to a dummy.
There are `1748` dummies, so exactly `1748` eligible hard rows are short and

\[
                         18646-1748=16898             \tag{1.4}
\]

are long.  Each \(M_v\) and \(R_v\) stays on row \(v\) exactly once.  The
input table was a target partition, so these observations prove exact use of
every named target.

The edge tests (0.2) give

\[
 B_a\subsetneq R_f
 \quad\hbox{or}\quad
 B_a\subsetneq M_v\subsetneq R_v,                    \tag{1.5}
\]

so every new row is a strict chain.  Its maximum, root and owner remain
those of the receiving physical row; (1.5) keeps every moved bottom inside
that row's old maximum and hence inside its owner.

The length-two rows are the `3899` fixed rows, the `1748` rows in
\(\mathcal F\), and the `1748` dummy-matched hard rows.  Thus

\[
                         3899+1748+1748=7395.          \tag{1.6}
\]

The length-three rows are the `16898` real-matched eligible hard rows plus
the `17` fixed rank-one-bottom rows, giving

\[
                         16898+17=16915.               \tag{1.7}
\]

There are no remaining singleton rows.  This proves (0.3).  \(\square\)

## 2. Converse and uniqueness

Call a table **bottom-relocated** when:

1. every \(R_f,M_v,R_v\), fixed row, owner and root remains on its original
   physical row;
2. each named \(B_a\) occurs exactly once, either immediately below one
   \(R_f\) or immediately below one \(M_v\);
3. all resulting rows are strict; and
4. exactly `1748` eligible hard rows have no bottom.

### Theorem 2.1 (converse)

Every bottom-relocated table determines a perfect matching of
\(G_{\rm bot}\), unique up to permutation of \(\mathcal U\).

#### Proof

Match \(b_a\) to the unique row containing \(B_a\).  Strictness gives the
corresponding edge of (0.2).  Every singleton row contains one bottom, so
every vertex of \(\mathcal F\) is matched.  Every long hard slot contains
one bottom and is matched to its token.  Match the `1748` remaining hard
slots bijectively to the dummies.  All vertices are covered exactly once.
Only the arbitrary names of the dummies are undetermined.  \(\square\)

### Corollary 2.2 (the payload outer polytope is integral)

The convex hull of bottom-relocated tables is the projection of a bipartite
perfect-matching polytope.  In particular its degree formulation is totally
unimodular, every fractional outer payload point rounds integrally, and a
protected set of fixed/forbidden bottom placements is feasible exactly when
the corresponding residual bipartite graph has a perfect matching.

This is only an outer-payload statement.  Literal flags, common five-cell
sockets, directed state balance and connected topology add further rows
which need not preserve total unimodularity.

### Corollary 2.3 (dummy-free implementation)

The dummy vertices need not be materialized.  Use one binary variable
\(z_{a,w}\) for every legal edge from a real bottom token \(b_a\) to a
right vertex \(w\in\mathcal F\dot\cup\mathcal H^{\rm slot}\), and impose

\[
\begin{aligned}
 \sum_w z_{a,w}&=1 &&(a\in\mathcal H),\\
 \sum_a z_{a,f}&=1 &&(f\in\mathcal F),\\
 \sum_a z_{a,v}&\le1 &&(v\in\mathcal H^{\rm slot}).
\end{aligned}                                             \tag{2.1}
\]

Then exactly `16898` hard slots are occupied by real bottoms and exactly
`1748` are empty.  Put

\[
                  s_v=1-\sum_a z_{a,v};                       \tag{2.2}
\]

the bit \(s_v\) is precisely the short-mode selector.  System (2.1) is the
bipartite matching formulation obtained by quotienting the dummy symmetry;
it remains integral.  This is the preferable outer implementation because
it avoids the complete `1748 x 18646` dummy edge bank.

### Corollary 2.4 (exact outer Hall cuts)

For \(X\subseteq\mathcal H\), let \(N_F(X)\) and \(N_H(X)\) be the free-row
and hard-slot neighbours of the real bottom tokens indexed by \(X\).  A
bottom-relocated table exists if and only if, for every \(X\),

\[
\boxed{
 \begin{aligned}
 |N_F(X)|+|N_H(X)|&\ge |X|,\\
 |N_F(X)|&\ge |X|-16898.
 \end{aligned}}                                           \tag{2.3}
\]

#### Proof

Apply Hall to the augmented square graph.  A left subset containing no dummy
gives the first inequality.  If it contains \(t\ge1\) dummies, its
neighbourhood contains all `18646` hard slots, so Hall reads

\[
             18646+|N_F(X)|\ge |X|+t.                 \tag{2.4}
\]

The strongest choice is \(t=1748\), which is the second inequality in
(2.3).  These exhaust all left subsets of the augmented graph.  \(\square\)

The second row is the exact large-set quota forcing every free row to be
filled; the first is ordinary placement Hall.  Neither row includes literal
state compatibility.

### Corollary 2.5 (prescribed admissible short bank)

Let \(A\subseteq\mathcal H^{\rm slot}\) be a bank in which all short rows
must lie.  Replace the complete dummy-to-hard menu by the complete
dummy-to-\(A\) menu.  The restricted outer table exists if and only if
\(|A|\ge1748\) and, for every real-token family \(X\),

\[
\begin{aligned}
 |N_F(X)|+|N_H(X)|&\ge |X|,\\
 |N_F(X)|+|N_H(X)\cup A|&\ge |X|+1748.
\end{aligned}                                             \tag{2.5}
\]

#### Proof

Apply Hall to the restricted augmented graph.  A left subset with no dummy
gives the first row.  Every nonempty dummy subset has hard neighbourhood
exactly \(A\); the strongest case again contains all `1748` dummies and
gives the second row.  The dummy-only case is \(|A|\ge1748\).  \(\square\)

This is a proof-safe first-stage filter when \(A\) is a globally computed
superset of slots capable of participating in a literal common-state socket.
It does not assert that choosing all shorts inside \(A\) makes their socket
choices mutually compatible.

### Corollary 2.6 (exact additive seeding)

Any additive cost on donor placements, long bottom placements, or chosen
short slots can be optimized exactly by one min-cost bipartite matching.
In particular, assigning cost \(c_v\) to a dummy edge incident with hard
slot \(v\) selects a globally optimal outer table for the additive short-slot
score \(\sum_{v\text{ short}}c_v\).  Socket degree or flag diversity may be
used as a seed cost, but only the later literal oracle can certify `1S`.

### Theorem 2.7 (outer-feasible short sets are matroid bases)

Let \(M\) be the transversal matroid on
\(\mathcal F\dot\cup\mathcal H^{\rm slot}\) induced by the real bottom
tokens: a right-vertex set is independent when it can be matched to distinct
real tokens through the containment edges.  Assume the outer table is
feasible, so \(\mathcal F\) is independent.  Put

\[
                   M_{\rm short}=(M/\mathcal F)^*             \tag{2.6}
\]

on ground set \(\mathcal H^{\rm slot}\).

Then a set \(S\subseteq\mathcal H^{\rm slot}\) is the set of short hard
rows of an exact bottom-relocated table if and only if \(S\) is a basis of
\(M_{\rm short}\).  This matroid has rank `1748`.

#### Proof

The real-token matching in a table occupies exactly

\[
                \mathcal F\mathbin{\dot\cup}
                (\mathcal H^{\rm slot}\setminus S),            \tag{2.7}
\]

a set of size \(1748+18646-1748=18646\), equal to the number of real
tokens.  Such a matching exists exactly when (2.7) is a basis of the
transversal matroid \(M\).  Bases of \(M\) containing \(\mathcal F\)
correspond after contraction to bases
\(\mathcal H^{\rm slot}\setminus S\) of \(M/\mathcal F\).
Taking complements is precisely matroid duality, proving that \(S\) is a
basis of (2.6).  Its rank is
\(18646-(18646-1748)=1748\).  \(\square\)

This gives a proof-safe exchange language directly on the chosen short-row
set.  Its fundamental circuits are the alternating-path exchanges of the
bottom matching.

For later pricing, its rank has the explicit matching formula

\[
 r_{M_{\rm short}}(S)
 =|S|-18646
  +r_M\!\left(\mathcal F\cup
       (\mathcal H^{\rm slot}\setminus S)\right),             \tag{2.8}
\]

where the final term is an ordinary maximum bipartite-matching rank.  This
is the standard dual/contraction identity
\(r_{N^*}(S)=|S|-r_N(E)+r_N(E\setminus S)\) with
\(N=M/\mathcal F\).  Thus rank and fundamental-circuit separation require
no new SAT oracle.

### Corollary 2.8 (conditional socket common-base criterion)

Suppose a separately proved matroid \(M_{\rm sock}\) on the hard slots has
as its rank-`1748` bases exactly the short-row sets admitting a complete
private socket-ticket assignment.  Then an outer-feasible socket-complete
short set exists if and only if

\[
 r_{M_{\rm short}}(X)
 +r_{M_{\rm sock}}(\mathcal H^{\rm slot}\setminus X)
 \ge1748
 \qquad(X\subseteq\mathcal H^{\rm slot}).                    \tag{2.9}
\]

This is Edmonds' common-base criterion.  A bipartite bank of genuinely
private socket tickets gives one valid transversal choice for
\(M_{\rm sock}\).

The actual `1S` socket system has shared long-tail/head degree, flag and
common-cell constraints; no theorem currently shows that its feasible
short sets form a matroid.  Therefore (2.9) is a conditional interface, not
a claim that the K17 state gate has already reduced to matroid intersection.

### Proposition 2.9 (socket-colour exchange can fail)

Even before flags or common-cell histories are imposed, the family of short
labels representable by a matching of long tail/head resources need not be
a matroid.  Let the tail and head shores both be \(\{1,2\}\), and give three
short labels the singleton socket menus

\[
                    a:\{(1,1)\},\qquad
                    b:\{(1,2)\},\qquad
                    c:\{(2,1)\}.                            \tag{2.10}
\]

Then \(\{a\}\) and \(\{b,c\}\) are representable, while neither
\(\{a,b\}\) nor \(\{a,c\}\) is.  The basis-exchange augmentation axiom
fails from \(\{a\}\) toward \(\{b,c\}\).

Thus ordinary occurrence-labelled socket matchability is not automatically
the matroid \(M_{\rm sock}\) required by Corollary 2.8.  A positive
common-base proof must exhibit a genuinely private/transversal ticket face,
or use a stronger hypergraph/configuration theorem.

## 3. Ordinary recoupling and relay circuits

An ordinary recoupling matching is the special perfect matching in which:

* \(b_d\) is matched to \(f\) when singleton \(f\) chooses donor \(d\);
* every non-donor token \(b_a\) is matched to its native hard slot \(a\);
* every donor hard slot is matched to a dummy.

Suppose a current long hard slot \(A\) contains \(B_a\), and a current short
slot \(D\) contains a dummy \(u\).  When
\(B_a\subsetneq M_D\), the status relay

\[
       A:(B_a,M_A,R_A)\mapsto(M_A,R_A),\qquad
       D:(M_D,R_D)\mapsto(B_a,M_D,R_D)                \tag{3.1}
\]

is exactly the alternating four-cycle switch

\[
                    b_a-A-u-D-b_a                    \tag{3.2}
\]

in \(G_{\rm bot}\).  The singleton/free row used to establish the ordinary
donor assignment is unchanged by (3.2).

### Theorem 3.1 (compound relay circuit normal form)

The symmetric difference of any two bottom-relocated tables is a disjoint
union of alternating even circuits in \(G_{\rm bot}\).  Flipping any one
such circuit gives another exact bottom-relocated table and preserves the
complete target partition and histogram.

#### Proof

This is the standard symmetric-difference theorem for two perfect matchings.
An alternating circuit exchange is again a perfect matching.  Apply Theorem
1.1.  \(\square\)

Thus a row which is first a relay destination and later a relay source is
not a payload conflict.  It is an internal vertex of one longer alternating
circuit.  Pairwise row-disjoint atomic columns describe only the four-cycle
subface of the exact outer matching fibre.

This theorem does **not** say that every long circuit decomposes into the
previously audited atomic four-cycles: the required chords may be absent.
The proof-safe options are either to select the final perfect matching
directly, or to add the complete alternating circuit as one compound outer
column.

## 4. Exact interface to the state/socket oracle

For a selected matching \(P\), regenerate modes literally:

* edge \(b_a f\) activates the short chain \((B_a,R_f)\);
* edge \(b_a v\) activates every legal long-state record for
  \((B_a,M_v,R_v)\);
* edge \(u v\) activates every legal short-state record for
  \((M_v,R_v)\).

Every direct transition and every common-state socket must imply the matching
edges which activate all incident row modes.  The shared in/out flag rows,
one-short degree rows, reset balance, subtour rows and final literal replay
remain exactly as in the proof-safe `1S-ROTS` audit.

The native round-47 table having relaxed union-projection defect zero but
`5969` socketless shorts shows that outer matching feasibility is far from
sufficient.  The gain here is narrower and exact: the outer master no longer
needs pairwise-disjoint relay columns or a special exception for a row reused
inside a relay path.  It can search the full static bottom-relocation fibre
with ordinary matching degree rows and regenerate the literal oracle at each
candidate.

## 5. All-dimensional movable-bottom lemma

The matching reduction is not special to the K17 numbers.

Let \(\mathcal B\) be \(n\) distinct named bottom targets.  Let
\(\mathcal F\) be \(f\) required free receivers with fixed maxima \(R_j\),
and let \(\mathcal H\) be \(n\) physical chain slots, each with a fixed
strict nonempty suffix

\[
                  M_v\subsetneq S_{v,2}\subsetneq\cdots.      \tag{5.1}
\]

A bottom may enter receiver \(j\) when \(B\subsetneq R_j\), and may enter
slot \(v\) when \(B\subsetneq M_v\).  Require every bottom once, every free
receiver filled, and exactly \(f\) bottomless chain slots.

### Theorem 5.1 (movable-bottom integrality)

The complete movable-bottom table class is in bijection, modulo dummy
labels, with perfect matchings between

\[
             \mathcal B\mathbin{\dot\cup}[f]
       \quad\hbox{and}\quad
             \mathcal F\mathbin{\dot\cup}\mathcal H,         \tag{5.2}
\]

where real-bottom edges are the two containment menus above and every dummy
is adjacent to every chain slot but no free receiver.  Its polytope is
integral, and its exact Hall inequalities are obtained from (2.3) by
replacing `16898` with \(n-f\).

#### Proof

The proofs of Theorems 1.1 and 2.1 use only exact bottom use, containment,
and the equality between the number of free receivers and bottomless slots.
They apply verbatim.  \(\square\)

Thus moving one complete rank/profile layer against a frozen suffix is
always a bipartite-matching problem.  Any genuine nonintegrality in a
general triangular chain table must enter through simultaneous movement of
at least two suffix levels, or through the later literal-state, upper, or
topology rows.

Only the explicitly frozen suffix resources are protected by this lemma.
An auxiliary resource derived jointly from the moved bottom and the suffix
(for example, the second middle endpoint of a Boolean diamond) generally
moves with the bottom.  Preserving such a resource occurrencewise is an
additional matching/state row and is not part of Theorem 5.1.

## 6. Scope boundary

The theorem proves:

* exact named-target partition under arbitrary bottom relocation;
* exact chain histogram;
* owner/root containment on every materialized row;
* an integral outer payload polytope; and
* the correct compound-circuit language for serial relay lineages.

It does not prove:

* that the round-47 matching, or any matching, has a `1S` common-state cycle
  cover;
* that a matching valid on one carrier owner phase remains valid after
  carrier transport;
* residence or arbitrary-upper coverage;
* a connected literal chronology;
* common-cap compilation; or
* \(\nu(17)=24313\).

The immediate finite target is therefore a Benders search whose outer object
is a perfect matching of \(G_{\rm bot}\), not a packing of disjoint atomic
relays, and whose exact inner oracle is the full common-state configuration
master.
