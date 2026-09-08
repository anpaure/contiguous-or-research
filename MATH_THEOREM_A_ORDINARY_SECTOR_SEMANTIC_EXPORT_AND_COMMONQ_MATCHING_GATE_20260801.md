# Ordinary Pascal sectors export the old lower ideal semantically, while literal Ferrers transport is exactly a common-source matching problem

Date: 2026-08-01  
Lane: A, K2 global transport / ordinary-child-sector escape  
Status: exact semantic export theorem; exact obstruction to direct source
reassembly; conditional jump-time full-block exporter; necessary-and-sufficient
sector-coupled matching/common-`Q` criterion.  No bounded-defect Pascal
recurrence is claimed.

## 0. Verdict

The ordinary-child-sector escape has a positive part and a sharp remaining
physical gate.

* Given an integral parent chain partition, the four-sector Pascal factor
  exports every nonempty old-ground target of rank at most `m` exactly
  once.  In particular, every displaced plateau lower-`q1` target and
  every lower member of the jump Ferrers bank has a canonical abstract
  child slot.  Existence of the required integral parent is not proved here.
* This export is already **sector-coupled**: the minimum of every
  top-containing parent chain lies at the first vertex of its `R` piece,
  while the rest of that chain lies in `Q^0`.  The two pieces cannot be
  directly joined by the residual endpoint-containment rule.  Thus the
  theorem does not export a literal parent source word or the higher members
  of the Ferrers decks.
* At a deadline jump, a literal parent source block would export the entire
  old interval deck.  It is locally a nonrepeating child Johnson owner walk
  precisely when consecutive parent turns have no immediate
  delete/reinsert; global simplicity additionally requires distinct upper
  colours.  Its signed residence requires two units of parent zero-gap
  slack.  The current four-sector factor does not supply such a block.
* Without a full-block certificate, the exact remaining theorem is not
  marginal Hall.  One must choose distinct ordinary-sector cells and pass
  one simultaneous frozen-prefix maximal-word test.  Theorem 5.1 below is
  the necessary-and-sufficient finite criterion, including mixed boundary
  rows.  Its coordinatewise positive-cover cuts give an exact separation
  oracle.

Consequently the standalone Ferrers sidecar is not needed if a
matching-closed ordinary full block can be constructed.  What is proved here
is the exact interface that such a construction must satisfy, not its
existence in every Pascal child.

## 1. The four-sector normal form

Let `|Omega|=2m-1`.  Assume an integral parent chain partition of the
nonempty strict lower ideal.  Fix a perfect inclusion matching

\[
 \mu:\binom{\Omega}{m-1}\longrightarrow\binom{\Omega}{m},
 \qquad A\subset\mu(A).                                  \tag{1.1}
\]

For a top-containing parent chain

\[
 C=(S_1\subsetneq\cdots\subsetneq S_\ell=A),
 \qquad |A|=m-1,
\]

the standard four-sector lift contains

\[
\begin{aligned}
 Q_C^0&=(S_2,\ldots,S_\ell,\mu(A)),\\
 Q_C^x&=(S_1+x,\ldots,S_\ell+x),\\
 Q_C^y&=(S_1+y,\ldots,S_\ell+y),\\
 R_C&=(S_1,S_1+xy,\ldots,S_{\ell-1}+xy).
                                                        \tag{1.2}
\end{aligned}
\]

For a top-free parent chain, retain its four vertical tagged copies; write
`C^0` for the untagged copy.

### Theorem 1.1 (exact old-ground semantic export)

The following child chain slots are a bijection onto all nonempty old-ground
sets of ranks at most `m`:

1. for every top-containing `C`, the first vertex `S_1` of `R_C`, all old
   vertices `S_2,...,S_ell` of `Q_C^0`, and its last vertex `mu(A)`;
2. for every top-free `C`, every vertex of `C^0`.

In particular, every displaced plateau lower-`q1` target and every jump
casualty of old-ground rank at most `m` has one canonical abstract child
slot.

#### Proof

The parent chains partition every nonempty old-ground set of rank at most
`m-1`.  Formula (1.2) sends `S_1` to the first vertex of `R_C` and sends
`S_i`, `i>=2`, to `Q_C^0`.  A top-free chain appears unchanged in `C^0`.
These slots are disjoint because the parent partition is disjoint.

The last vertices `mu(A)` of the `Q_C^0` pieces range bijectively over all
rank-`m` old-ground sets by (1.1), and their rank separates them from the
parent strict lower ideal.  This proves the claim. \(\square\)

The scope is important.  Theorem 1.1 is a statement about selected chain
vertices.  It does not by itself give source intervals, a common source
word, or any old target of rank at least `m+1`.  Moreover `Q^0` alone misses
exactly

\[
 \{S_1(C):C\text{ is top-containing}\};                 \tag{1.3}
\]

those targets are supplied by the first vertices of the `R` pieces.  Even
the semantic lower export is therefore coupled across two sectors.

## 2. The standard pieces do not reassemble a parent source trace

### Proposition 2.1 (direct endpoint-join obstruction)

For every top-containing chain of length `ell>=2`, neither direct residual
endpoint join between `R_C` and `Q_C^0` is legal:

\[
 \max R_C=S_{\ell-1}+xy\not\subseteq S_2=\min Q_C^0,    \tag{2.1}
\]

\[
 \max Q_C^0=\mu(A)\not\subseteq S_1=\min R_C.          \tag{2.2}
\]

#### Proof

The new coordinates `x,y` in the left side of (2.1) are absent from `S_2`.
For (2.2), `S_1` is a proper subset of `A`, while `A` is a proper subset of
`mu(A)`; hence the reverse containment is impossible. \(\square\)

For `ell=1`, the isolated inclusion \(S_1\subset\mu(S_1)\) is legal, but
there is no nontrivial parent chain to reconstruct.  Proposition 2.1 shows
that the standard residual-forest theorem does not turn Theorem 1.1 into a
literal parent-shaped source block.

The inherited K2 jump word displays the same obstruction at source level:

\[
 [\gamma]E^-\;[\alpha]A^-\;[X]\;A^+[\gamma]\;E^+[\alpha].
                                                               \tag{2.3}
\]

The inserted `alpha` and `gamma` destroy the clean `E^-|A^-` and
`A^+|E^+` adjacencies.  Thus the complete suffix/prefix signature rails
from the parent word are not literally present inside the K2 packet.

## 3. What a literal ordinary rail would solve

### Lemma 3.1 (clean-splice Ferrers realization)

Let a source word contain adjacent blocks `U|V`.  Suppose selected suffixes
of `U` have OR values

\[
 L_1\supseteq\cdots\supseteq L_p,
\]

and selected prefixes of `V` have OR values

\[
 P_1\subseteq\cdots\subseteq P_q.
\]

Then every value `L_a union P_b` occurs on the interval from the start of
the selected suffix `a` to the end of the selected prefix `b`.  Distinct
ordered endpoint pairs give distinct physical cells.

#### Proof

The crossing interval is the disjoint concatenation of the selected suffix
and prefix, so its OR is their union.  Its two endpoints recover `(a,b)`.
\(\square\)

This is the literal row/column export missing from (2.3).

### Theorem 3.2 (full-block ordinary-sector export)

Let an old source word `A=(A_1,...,A_n)` carry an injective selected
target-to-interval matching containing one defining occurrence for every
displaced target under consideration.  Suppose an ordinary child sector replaces
each `A_i` by a nonempty consecutive block

\[
 B_i=(B_{i,1},\ldots,B_{i,t_i}),
 \qquad \bigcup_j B_{i,j}=A_i,                         \tag{3.1}
\]

with the blocks in parent order.  Assume:

1. every transported old interval remains inside its declared deadline and
   guard class;
2. the child source satisfies all owner, point-cap, mixed-boundary and
   residence rows; and
3. every hard row meeting this sector either contains whole blocks `B_i` or
   is separately included in the common-source test of Section 5.

Then the full-block map transports the entire old matching injectively and
preserves every old interval OR.  Hence it simultaneously exports the
plateau lower-`q1` antichain, both jump Ferrers decks, their inherited
collision quotient, and every other selected old target, at zero extra
source length beyond the already-budgeted ordinary sector.  This assertion
does not bound \(\sum_i(t_i-1)\); those positions are part of the
hypothesized ordinary-sector budget.

#### Proof

Map `[i,j]` to the interval containing all of
`B_i,B_{i+1},...,B_j`.  Ordered disjoint blocks make this map injective, and
(3.1) gives

\[
 \bigcup_{u=i}^j\bigcup_v B_{u,v}
   =\bigcup_{u=i}^j A_u.                               \tag{3.2}
\]

Thus every transported target row remains exact.  The three hypotheses say
precisely that these cells are still physically admissible and compatible
with all rows not implied by (3.2). \(\square\)

Theorem 3.2 is a sufficient escape from the standalone-sidecar lower bound.
It is conditional: the abstract four-sector factor in Section 1 does not
supply the ordered blocks (3.1).

## 4. A sharp jump-time literal-block criterion

There is one setting in which an unchanged parent source is rank-correct in
the child.  Let `A_0,...,A_N` be a parent source block at depth `h`, and put

\[
 O_i=\bigcup_{p=i}^{i+h}A_p.                            \tag{4.1}
\]

Here \(0\le i\le N-h\).  Assume the `O_i` form a simple rank-`r`
Johnson path.  At a deadline jump the child depth is `H=h+1`, and the same
source letters have owner windows

\[
 V_i=\bigcup_{p=i}^{i+h+1}A_p=O_i\cup O_{i+1}.          \tag{4.2}
\]

Here \(0\le i\le N-h-1\).  Write

\[
 d_i=O_i\setminus O_{i+1},
 \qquad e_{i+1}=O_{i+2}\setminus O_{i+1}.              \tag{4.3}
\]

### Theorem 4.1 (jump turn-lift)

Every `V_i` has rank `r+1`, and consecutive `V_i,V_{i+1}` are distinct
Johnson neighbours with intersection `O_{i+1}` iff

\[
 d_i\ne e_{i+1}                                       \tag{4.4}
\]

for \(0\le i\le N-h-2\).  Under (4.4), the unchanged parent source is a
locally nonrepeating child Johnson walk and preserves every internal parent
interval OR literally.  It is a globally simple child owner path iff the
upper colours

\[
                    \{O_i\cup O_{i+1}:0\le i\le N-h-1\}
                                                               \tag{4.5}
\]

are pairwise distinct.

For one coordinate, let the parent owner trace have an internal positive
run of length `a` and an internal zero gap of length `b`.  Its child trace
is \(v_i=o_i\vee o_{i+1}\); hence the corresponding lengths are `a+1` and
`b-1`.  Therefore child signed threshold `h+2` holds internally provided

\[
 a\ge h+1,
 \qquad b\ge h+3.                                     \tag{4.6}
\]

Clipped boundary runs still require compatible exterior continuation.

#### Proof

Since adjacent parent owners are rank-`r` Johnson neighbours,

\[
 V_i=O_{i+1}+d_i,
 \qquad V_{i+1}=O_{i+1}+e_{i+1}.                       \tag{4.7}
\]

They coincide exactly when `d_i=e_{i+1}`; otherwise they share exactly the
rank-`r` set `O_{i+1}` and exchange one coordinate.  Pairwise
distinctness of all `V_i` is exactly pairwise distinctness of the upper
colours in (4.5).  Formula (4.2) proves the source and OR claims.  Applying
adjacent Boolean OR to an internal maximal trace run enlarges a positive
run by one in total and removes one position from a zero gap, giving (4.6).
\(\square\)

Condition (4.4) is the exact no-immediate-delete/reinsert condition.  On a
plateau the child depth remains `h`, so the unchanged source still has the
rank-`r` windows (4.1), not the required rank `r+1`.  Coning or tagging the
block fixes owner rank only by adding the fresh tag to old untagged target
rows.  Thus the unchanged-literal-block mechanism is jump-only.  Even on a
jump, (4.4), (4.6), the endpoint collars, and global owner uniqueness must
all be checked.

## 5. Exact sector-coupled matching/common-`Q` theorem

Let \(\mathcal T\) be the distinct-value quotient of the displaced plateau
and chosen jump target bank.  If a target requires multiplicity `b_T`,
replace it by `b_T` labelled clones and use the same symbol
\(\mathcal T\) for the resulting left-vertex set; ordinary coverage has
`b_T=1`.

Fix one proposed ordinary child-sector source line with position set `P`.
Let \(F\subseteq P\) be frozen positions with letters `A_p`, and let `V=P-F` be
free positions.  At every position let `C_p` be its point cap and `D_p` a
mandatory subset.  A hard row is a triple

\[
 R=(I_R,E_R,S_R),                                     \tag{5.1}
\]

where \(I_R\subseteq P\) is the sector interval, `E_R` is the already-frozen
exterior OR, and the required equation is

\[
 E_R\cup\bigcup_{p\in I_R}Q_p=S_R.                    \tag{5.2}
\]

The hard family `H` includes the OR-equality forms of owner rows, protected
upper and lower rows, terminal rows, and every mixed exterior guard.
Deadline eligibility, Johnson simplicity, residence and topology are
nonlinear structural predicates; they must be fixed or prefiltered
independently and are not encoded by (5.2).  A candidate occurrence
`e=(T,c)` assigns target `T` to an unreserved structurally legal physical
interval cell `c`, with sector positions `I_c` and frozen exterior
contribution `E_c`; its row is

\[
 E_c\cup\bigcup_{p\in I_c}Q_p=T.                      \tag{5.3}
\]

A selection `M` is an occurrence matching: one candidate for each selected
target clone and at most one target per physical cell.

For fixed `M` and free `p`, define

\[
 K_p(M)=C_p
 \cap\!\!\bigcap_{R\in\mathcal H:p\in I_R}S_R
 \cap\!\!\bigcap_{(T,c)\in M:p\in I_c}T.             \tag{5.4}
\]

At a frozen position put `K_p(M)=A_p`.

### Theorem 5.1 (matching plus common-source equivalence)

The matching `M` is realized by one nonzero source word satisfying all
point caps, mandatory subsets and hard OR-equality rows iff all of the
following hold:

\[
 D_p\subseteq A_p\ne\varnothing,\qquad A_p\subseteq C_p
  \cap\!\!\bigcap_{R:p\in I_R}S_R
  \cap\!\!\bigcap_{(T,c)\in M:p\in I_c}T
 \quad(p\in F),                                       \tag{5.5}
\]

\[
 D_p\subseteq K_p(M)\ne\varnothing
 \quad(p\in V),                                       \tag{5.6}
\]

\[
 E_R\cup\bigcup_{p\in I_R}K_p(M)=S_R
 \quad(R\in\mathcal H),                              \tag{5.7}
\]

and

\[
 E_c\cup\bigcup_{p\in I_c}K_p(M)=T
 \quad((T,c)\in M).                                   \tag{5.8}
\]

When these conditions hold, `Q_p=K_p(M)` is the unique
componentwise-largest feasible source with the frozen letters fixed.

#### Proof

Every feasible free letter is contained in its point cap and in the target
of every exact row using that position.  It is therefore contained in
`K_p(M)`.  Fixed letters must satisfy (5.5).  Thus `K(M)` is the
componentwise-largest possible word.  The intersections in (5.4) prevent
row overflow.  If this maximal word misses a coordinate required in one of
(5.7) or (5.8), no smaller feasible word can restore it.  Conversely,
(5.5)--(5.8) say directly that `K(M)` is nonzero, cap-legal, respects every
mandatory subset, and realizes every hard and selected row. \(\square\)

This is an exact finite criterion.  In particular, Hall in a union of
different cap states is invalid.

### Corollary 5.2 (fixed-source Hall min-max form)

Let \(\mathfrak Q_{\mathcal H}\) be the set of source words satisfying the
frozen letters, point caps, mandatory subsets and hard rows.  For
\(Q\in\mathfrak Q_{\mathcal H}\), form the occurrence
graph `G_Q` from target clones to unreserved cells, with

\[
 T\sim_Q c
 \quad\Longleftrightarrow\quad
 E_c\cup\bigcup_{p\in I_c}Q_p=T                       \tag{5.9}
\]

and all edge-local structural guards satisfied.  Every global pairwise or
higher conflict is assumed already represented by physical-cell capacity or
the hard state.  Under this hypothesis, the minimum sector transport defect
is exactly

\[
 \delta_{\rm sec}
 =\min_{Q\in\mathfrak Q_{\mathcal H}}
   \max_{Y\subseteq\mathcal T}
       \bigl(|Y|-|N_{G_Q}(Y)|\bigr).                  \tag{5.10}
\]

Thus, provided \(\mathfrak Q_{\mathcal H}\ne\varnothing\), zero-defect
transport is equivalent to one hard-feasible source `Q` whose occurrence
graph satisfies every Hall cut.  If
\(\mathfrak Q_{\mathcal H}=\varnothing\), set
\(\delta_{\rm sec}=+\infty\).

#### Proof

For fixed `Q`, ordinary bipartite matching leaves
`max_Y(|Y|-|N(Y)|)` target clones unmatched.  Minimize over the one common
hard-feasible source.  Conversely, any feasible matching from Theorem 5.1
uses such a source and appears in its graph. \(\square\)

## 6. Exact positive-cover separation

For a free position put

\[
 P_p=C_p\cap\bigcap_{R\in\mathcal H:p\in I_R}S_R.      \tag{6.1}
\]

For a proposed matching `M`, a coordinate `z` survives at a free position
exactly on

\[
 A_z(M)=\{p\in V:z\in P_p\}
 \setminus
 \bigcup_{(T,c)\in M:z\notin T} I_c.                  \tag{6.2}
\]

### Proposition 6.1 (coordinatewise iff and Benders cores)

For a hard row and a selected row, respectively, define their fixed
contributions

\[
 E_R^F=E_R\cup\bigcup_{p\in I_R\cap F}A_p,\qquad
 E_c^F=E_c\cup\bigcup_{p\in I_c\cap F}A_p.          \tag{6.3}
\]

Assume (5.5).  Equations (5.6)--(5.8) are equivalent to all of the
following statements.

1. \(E_R^F\subseteq S_R\) for every hard row and
   \(E_c^F\subseteq T\) for every selected row.
2. Every required coordinate \(z\) of a hard row not in \(E_R^F\), and of
   a selected row not in \(E_c^F\), has its sector interval meet
   \(A_z(M)\).
3. At every free position at least one coordinate of \(P_p\) survives all
   selected negative rows, and every mandatory coordinate survives there.

For the overall test, before imposing that assumption, a failed matching
has one of the following exact certificates:

* failure of the fixed compatibility test (5.5);
* a hard or selected frozen/exterior overflow in item 1;
* a static mandatory-cap failure \(D_p\nsubseteq P_p\);
* a selected row through \(p\) which deletes a coordinate of \(D_p\);
* a family of selected \(z\)-negative rows covers all possible
  \(z\)-positions
  of a hard positive row;
* together with one selected positive row, \(z\)-negative selected rows
  cover all its possible \(z\)-positions; or
* selected negative rows collectively delete every coordinate of \(P_p\) at
  one free position.

For binary selection variables, each minimal covering family gives the
corresponding inequality “not all members of this family may be selected”;
for a selected-positive-row cover core, that positive row is included in
the forbidden family.
The mandatory-deletion item is a singleton forbidden-selection cut.
Minimal cores suffice.  If fixed/exterior overflow, (5.5), static
mandatory-cap failures and mandatory-deleting candidate edges are all
prefiltered, only the final three positive-cover/empty-position core types
remain.

#### Proof

Formula (6.2) is exactly the coordinatewise expansion of (5.4): a selected
row containing \(p\) removes \(z\) precisely when its target omits \(z\).
Equations (5.7) and (5.8) first require no fixed overflow and then fail
positively exactly when every possible free position is removed.
Equation (5.6) fails either statically, by mandatory deletion, or because
all coordinates at one position are removed.  These alternatives are
exactly the displayed list. \(\square\)

The smallest collective obstruction already has two positions.  Let

\[
 C_1=\{z,a\},\qquad C_2=\{z,b\},                       \tag{6.4}
\]

require the background row on both positions to equal `{z,a,b}`, and
select the two singleton rows `{a}` at position 1 and `{b}` at position 2.
The occurrence matching is perfect and each singleton is individually
legal, but

\[
 K_1=\{a\},\qquad K_2=\{b\},                          \tag{6.5}
\]

so the background row loses `z`.  This is a literal two-pin
positive-cover core and proves that marginal target Hall is insufficient.

## 7. When Hall compresses, and when it does not

### Proposition 7.1 (interval-convex occurrence graphs)

Fix one common source and linearly order the available cells.  If every
target neighborhood is an interval `[l_T,r_T]`, Hall is equivalent to

\[
 \sum_{T:N(T)\subseteq[a,b]}b_T\le b-a+1
 \qquad(1\le a\le b\le N).                            \tag{7.1}
\]

#### Proof

If Hall fails, decompose the union of the offending interval neighborhoods
into disjoint interval components.  Each target neighborhood lies wholly
inside one component, so one component violates (7.1).  The converse is
immediate. \(\square\)

### Proposition 7.2 (private row/column rails)

Suppose a casualty grid \(\mathcal E\subseteq[p]\times[q]\) has row pools
and column pools which are mutually pairwise disjoint, with capacities
`rho_a` and `kappa_b`, and task
`(a,b)` may use exactly its row pool or its column pool.  A saturating
matching exists iff

\[
 |\mathcal E\cap(A\times B)|
 \le\sum_{a\in A}\rho_a+\sum_{b\in B}\kappa_b
 \quad(A\subseteq[p],\ B\subseteq[q]).                \tag{7.2}
\]

#### Proof

For a task family, let \(A,B\) be its exact row and column projections.
Its neighborhood is then the union of precisely those row and column pools.
Completing it to \(\mathcal E\cap(A\times B)\) does not enlarge that
neighborhood and only increases demand.  Hence the rectangular cuts are
equivalent to all Hall cuts. \(\square\)

Ferrers indexing of the target values alone implies neither proposition.
At `h=2`, let the four targets be the Boolean diamond, with
\(Z\ne\varnothing\),

\[
 Z,\quad Z+a,\quad Z+b,\quad Z+a+b.                    \tag{7.3}
\]

Give four one-cell slots the menus

\[
\begin{array}{c|c}
 c_1&Z,Z+a,Z+b,Z+a+b\\
 c_2&Z,Z+a\\
 c_3&Z+a+b\\
 c_4&Z+a+b.
\end{array}                                            \tag{7.4}
\]

Every individual, row, column, and whole-grid cardinality cut passes, but
`{Z,Z+a,Z+b}` has neighborhood `{c_1,c_2}`.  Thus an `L`-shaped Hall cut
fails.  These menus are literal one-position cap intervals: their
(cap, mandatory-subset) pairs are

\[
 c_1:(Z+a+b,Z),\quad c_2:(Z+a,Z),\quad
 c_3,c_4:(Z+a+b,Z+a+b).                               \tag{7.5}
\]

Thus (7.4) is an exact common-cap example, not only an abstract graph.

## 8. Sharp remaining theorem

The standard child factor has now been separated into three levels.

1. **Abstract lower slots:** Theorem 1.1 is unconditional for an integral
   triangular parent and its standard four-sector lift.
2. **Literal all-deck export:** Theorem 3.2 is sufficient, and Theorem 4.1
   gives a sharp jump-time realization criterion for a parent source block.
   Neither is supplied by the current four-sector factor.
3. **General physical export:** Theorems 5.1 and 6.1 are exact, and Ferrers
   target shape alone gives no further Hall simplification.  One must
   construct a matching avoiding every positive-cover and empty-position
   core, or prove the actual ordinary-sector occurrence graph is
   interval-convex/private-rail.
   All structural residence, topology, simplicity and deadline predicates
   remain separate prefilters.

The remaining bounded-defect hypothesis can therefore be stated without a
standalone sidecar:

> At every same-parity Pascal step, the displaced target quotient admits an
> occurrence matching into already-budgeted ordinary child-sector cells
> with `delta_sec=O(1)`, and the chosen cells pass (5.5)--(5.8) together with
> the owner, upper, residence and mixed-boundary rows.

For an exact `B(k)` recurrence replace `O(1)` by zero, unless the terminal
triangular boundary explicitly absorbs the residual clones.  Independently,
the inherited K2 shared-bank residence horizon still forces regeneration
after finitely many deadline jumps.  The ordinary-sector transport theorem
proved here does not remove that separate obstruction.
