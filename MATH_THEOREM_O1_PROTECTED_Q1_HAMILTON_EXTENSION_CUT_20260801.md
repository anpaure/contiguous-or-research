# Protected q1 Hamiltonization is a rooted-target problem: an exact four-atom cut

Date: 2026-08-01  
Lane: additive-constant regeneration, protected q1/upper interface  
Status: exact conditional positive theorem and exact finite obstruction.  The
unqualified finite-`H` extension statement is false.

## 0. Outcome

The complete-host alternating-circuit reset has an exact protected form, but
its hypothesis is a rooted Hamilton extension and cannot be deleted.

Let `F` be a q1-rainbow spanning two-factor in `J(2m-1,m)`, and let `P` be a
set of factor edges to be fixed.  If a Middle Levels Hamilton cycle contains
the two-incidence lift of every edge in `P`, then the symmetric difference
with the incidence lift of `F` decomposes into alternating circuits avoiding
all those incidences.  Toggling the circuits serially Hamiltonizes `F` while
fixing `P`.  If named upper witnesses are represented by edges common to the
initial and terminal factors, they are preserved at every intermediate
state.  With

\[
                  N={2m-1\choose m},\qquad p=|P|,
\]

one may use at most

\[
                         \left\lfloor {2(N-p)\over3}\right\rfloor
\tag{0.1}
\]

simple alternating circuits.  This improves the generic length-four count
because the Middle Levels incidence graph has girth six.

However, a rooted target need not exist.  Already in `J(5,3)` there is a
q1-rainbow factor consisting of two five-cycles and four protected physical
edges whose

* eight owners are distinct;
* four lower q1 colours are distinct; and
* four upper union colours are distinct,

but no q1-rainbow Hamilton cycle contains all four edges.  The protected
incidence-factor fibre has exactly two elements.  Its only nonzero circuit
direction is one alternating `C8`, and both endpoints of that toggle are two
five-cycles.

Thus deleting `O(H)` incidences does not by itself leave a Hamiltonizing
alternating-circuit basis, even for absolute `H`.  The bounded regenerative
absorber needs one of the following additional inputs:

1. a **protected rooted Middle Levels extension theorem** for the selected
   private packet bank; or
2. a packet-selection rule which chooses the protected atoms and the terminal
   Hamilton cycle jointly.

The counterexample's four old atoms can be partitioned into two legal Boolean
hex `O^-` pairs.  Their `O^-` atoms jointly form a four-resource matching, but
the two complete hex supports are not resource-disjoint.  Consequently the
cut refutes an inference from a planted old matching to protected
Hamiltonization; it does not refute the stronger prospective disjoint-menu
hypothesis in the ternary-absorber theorem.  It also does not refute a rooted
extension theorem stated only above a dimension threshold depending on `H`.

## 1. Protected circuits are equivalent to a rooted Hamilton target

Let `Gamma` have size `2m-1`.  Write

\[
 {\cal U}={\Gamma\choose m},\qquad
 {\cal L}={\Gamma\choose m-1},\qquad
 N=|{\cal U}|=|{\cal L}|.
\]

The Middle Levels graph `ML(Gamma)` is the incidence graph between `L` and
`U`.  A Johnson edge `AB` has lower colour `A intersection B` and upper colour
`A union B`.  Its incidence lift is the two-edge path

\[
                    A-(A\cap B)-B.                         \tag{1.1}
\]

As in the unprotected reset theorem, q1-rainbow Johnson two-factors are in
bijection with incidence two-factors.

### Theorem 1.1 (exact protected-target equivalence)

Let `F` be a q1-rainbow spanning two-factor and let `P subset F`.  The
following are equivalent.

1. There is a q1-rainbow Hamilton cycle `C` containing every edge of `P`.
2. There is a sequence of incidence-factor alternating-circuit toggles from
   `F` to a Hamilton factor such that no toggle uses either incidence of any
   edge in `P`.

If these conditions hold, the circuits may be chosen edge-disjoint and
simple.  If `c` incidence edges are common to the initial and terminal
incidence factors, the number `t` of circuits satisfies

\[
              t\le \left\lfloor {4N-2c\over6}\right\rfloor
                \le \left\lfloor {2(N-|P|)\over3}\right\rfloor .
\tag{1.2}
\]

Every intermediate projection is a q1-rainbow spanning two-factor containing
`P`.

#### Proof

The reverse implication is immediate from the terminal state.

For the forward implication, lift `F` and `C` to incidence two-factors
`\widehat F,\widehat C`.  Delete their common incidences and colour the
remaining `\widehat F` edges red and the remaining `\widehat C` edges blue.
At every incidence
vertex the red and blue degrees agree.  Pair red and blue half-edges at each
vertex.  Following these pairings decomposes the symmetric difference into
closed alternating trails.  If a trail repeats a vertex, the subtrail
between two consecutive repetitions has even length, hence is itself
alternating and closed.  Splitting repeatedly gives edge-disjoint simple
alternating cycles.

Every incidence of every protected edge is common, so no circuit uses it.
Toggling the circuits in any order preserves degree two at every owner and
lower-colour vertex.  Projection therefore gives a q1-rainbow Johnson
two-factor after every toggle, and the terminal factor is `C`.

Each incidence factor has `2N` edges, so the symmetric difference has
`4N-2c` edges.  The Middle Levels graph has no four-cycle: two distinct
rank-`m-1` sets have at most one common rank-`m` superset.  Hence its girth is
at least six, and every simple circuit consumes at least six difference
edges.  Finally, every edge of `P` contributes two common incidences, so
`c>=2|P|`.  This proves (1.2).  \(\square\)

### Corollary 1.2 (the clean upper-witness interface)

Let `R_1,...,R_h` be named rank-`m+1` upper colours.  Suppose the rooted
Hamilton target `C` in Theorem 1.1 contains, for each `R_j`, a Johnson edge
`w_j` which is also in `F` and satisfies

\[
                            \bigcup w_j=R_j.                \tag{1.3}
\]

Add the distinct `w_j` to `P`.  Then every named upper witness is present in
every intermediate factor.  If `p'` is the number of distinct protected and
witness edges, (1.2) holds with `p'` in place of `p`.

If the terminal witness is not common to `F` and `C`, Theorem 1.1 guarantees
only terminal recreation.  Preservation during the serial toggle then
requires an additional circuit-order condition: the circuit(s) installing a
replacement must be toggled before the first circuit destroying its last old
witness.  This dependency can contain a directed cycle for several named
upper colours.  It is not implied by balanced incidence degrees.

#### Proof

The two incidences of every `w_j` are common and therefore outside the
symmetric difference.  All circuit toggles retain them.  The final statement
is the literal distinction between a common incidence and a red-to-blue
replacement.  \(\square\)

Theorem 1.1 is the strongest conclusion supplied by circuit algebra alone.
It converts a rooted Hamilton target into a protected route; it does not
construct the rooted target.

There is one further orientation row for ordered Boolean atoms.  Theorem 1.1
fixes undirected physical edges.  If a planted old atom also prescribes its
tail and head, the terminal Hamilton cycle must admit one global cyclic
orientation agreeing with every such prescription.  This coherence is
necessary and is not implied by undirected containment of `P`.  Serial
preservation of the directed assignments likewise requires an aligned
orientation record on every intermediate component.

## 2. A four-atom protected cut in `J(5,3)`

Use ground set `{0,1,2,3,4}` and concatenate digits for subsets.  Consider
the q1-rainbow two-factor

\[
\begin{aligned}
 C_0={}&(012,014,134,034,024,012),\\
 C_1={}&(013,023,234,124,123,013).
\end{aligned}                                               \tag{2.1}
\]

Protect the four edges

\[
 P=\{012\!-\!024,\ 013\!-\!023,\
       124\!-\!234,\ 034\!-\!134\}.                         \tag{2.2}
\]

Their lower and upper colours are, respectively,

\[
\begin{array}{c|c|c}
e&A\cap B&A\cup B\\ \hline
012-024&02&0124\\
013-023&03&0123\\
124-234&24&1234\\
034-134&34&0134.
\end{array}                                                  \tag{2.3}
\]

Thus the lower colours and upper colours are separately injective, and the
eight owner endpoints are distinct.  Orienting the four edges in the
Boolean roles of Section 3 gives distinct tails and distinct heads as well.

This is not an unrelated factor fixture.  The coordinate permutation

\[
                       (0,1,2,3,4)\longmapsto(0,3,4,2,1)
\]

maps (2.1) edge-for-edge to the authenticated two-component `J(5,3)` factor
used by the unprotected alternating-reset replay.

### Theorem 2.1 (exact protected-fibre obstruction)

Exactly two q1-rainbow spanning two-factors of `J(5,3)` contain `P`, and
neither is Hamilton.  They are the factor (2.1) and

\[
\begin{aligned}
 C'_0={}&(012,123,134,034,024,012),\\
 C'_1={}&(013,023,234,124,014,013).
\end{aligned}                                               \tag{2.4}
\]

Their incidence lifts differ by one alternating `C8`.  Consequently no
alternating-circuit sequence avoiding the eight protected incidences can
Hamiltonize (2.1).

#### Proof

`ML(5)` is cubic.  The complement of an incidence two-factor is therefore a
perfect matching.  At a protected lower vertex, the two protected incidences
force the third incidence into this complementary matching.  From (2.2) the
four forced matching edges are

\[
 02-023,\qquad03-034,\qquad24-024,\qquad34-234.             \tag{2.5}
\]

After deleting their endpoints, the lower vertices are

\[
                  01,04,12,13,14,23
\]

and the upper vertices are

\[
                  012,013,014,123,124,134.
\]

The vertex `04` is forced to `014`, and `23` is forced to `123`.  What
remains is the eight-cycle

\[
 01-012-12-124-14-134-13-013-01.                            \tag{2.6}
\]

It has exactly two perfect matchings.  Taking complements gives precisely
(2.1) and (2.4), each with two five-cycle components.  Switching the two
perfect matchings toggles exactly the alternating incidence `C8` (2.6).
There is no third protected factor and hence no protected Hamilton target.
\(\square\)

This is stronger than saying that one unfortunate circuit decomposition
fails: the complete protected degree-two fibre has been exhausted.

### Finite sharpness at `m=3`

The replay exhausts all `60` perfect matchings of `ML(5)`.  Their complements
are `24` Hamilton factors and `36` factors of profile `5+5`.  Among protected
sets which

1. are subsets of some q1-rainbow factor,
2. have pairwise-disjoint owner endpoints, and
3. have distinct lower and distinct upper colours,

every set of size at most three extends to a Hamilton factor, while (2.2) is
a size-four obstruction.  Thus (2.2) is the smallest literal obstruction in
this fully resource-injective `m=3` class.

If upper-colour injectivity is dropped, size two already fails: the edges

\[
                      012-013,\qquad023-123                 \tag{2.7}
\]

belong to a q1-rainbow factor but no q1-rainbow Hamilton factor contains
both.  They repeat the upper colour `0123`.

The finite sharpness statement is an exhaustive fact at `m=3`, not an
all-dimension classification.  In particular an asymptotic private-bank
theorem may legitimately add `m>=m_0(H)`; it still needs a proof not supplied
by the ordinary Middle Levels Theorem or by alternating-circuit balance.

## 3. Alignment with the ternary Boolean hexagon

The protected set (2.2) is not foreign to the local absorber.  Put

\[
\begin{array}{c|ccccc|c}
 &S&a&b&c&d&O^-\\ \hline
X&0&3&4&2&1&\{013-023,012-024\}\\
Y&4&2&0&3&1&\{124-234,134-034\}.
\end{array}                                                  \tag{3.1}
\]

Substitution in the six-atom formula of the ternary-absorber theorem shows
that both rows are legal `O^-` pairs.  Their missing target atoms are,
respectively,

\[
                         014-034,\qquad014-024.              \tag{3.2}
\]

The four old atoms themselves form a four-resource matching, by (2.3) and
owner disjointness.  The two **complete** packet supports are not private.
For the rows `X,Y`, their typed support sets intersect as follows:

\[
\begin{array}{c|c}
\text{resource type}&\text{common resources}\\ \hline
\text{lower}&04\\
\text{upper}&0124,0134\\
\text{tail}&014\\
\text{head}&024,034.
\end{array}                                                  \tag{3.3}
\]

There is a second legal partition of the four old atoms,

\[
 \{012-024,124-234\}\quad\dot\cup\quad
 \{013-023,034-134\},                                      \tag{3.4}
\]

but its two complete supports are also not resource-disjoint.  The replay
enumerates every Boolean-hex representation of all three pair partitions;
there is no partition into two complete typed-resource-disjoint supports on
this ground set.

Therefore Theorem 2.1 applies literally to two already planted old pairs,
but it does not contradict the prospective quadratic-fan packing theorem,
which chooses complete packet supports disjointly before the bulk matching
is frozen.

## 4. Exact counting facts which do not supply the rooted target

Two nearby hosts and two different notions of an upper witness must be kept
separate.

### Proposition 4.1 (the odd-host raw Cartesian fan)

Assume `m>=3`.

The ternary-absorber theorem is stated on an even ground set `Omega` of size
`2m`.  For one target atom, its displayed raw fan has `(m-1)^2` choices:
`b` has `m-1` choices in the lower set and `c` has `m-1` choices outside the
upper set.

On the odd Middle Levels ground set `Gamma` of size `2m-1`, the same literal
formula instead has

\[
                            (m-1)(m-2)                       \tag{4.1}
\]

choices, because now `|Gamma-U|=m-2`.  A fixed non-target typed resource
occurs in at most `m-1` choices.  Therefore deleting `z` forbidden typed
resources leaves at least

\[
                  \max\{0,(m-1)(m-2-z)\}                    \tag{4.2}
\]

raw choices.

Moreover,

\[
 {2m-1\choose m+1}<{2m-1\choose m}=N,                    \tag{4.3}
\]

so a spanning q1 factor on the odd host cannot be globally injective on the
adjacent-upper shore.  Here `upper witness` can only mean a named supported
colour (or a fixed witnessing edge), not a second spanning matching palette.

This is only a menu count.  It does not say that the two old atoms `O^-` of
one surviving choice are present in the frozen factor, nor that its physical
toggle has the required component topology.  Those are precisely the
planting and rooted-extension rows.

#### Proof

The choices are indexed by `b in L` and `c notin U`.  In the eight
non-target resource formulas, fixing one of the entries either fixes both
indices, fixes `b` and leaves at most `m-2` choices for `c`, or fixes `c` and
leaves at most `m-1` choices for `b`.  Union-bound the deleted choices over
the `z` forbidden typed resources.  \(\square\)

### Proposition 4.2 (exact pure-forbidden incidence fraction)

Assume `m>=2`.  Let `B` be a set of `b` literal incidence edges of
`ML(2m-1)`, and let
`\mathcal H` be the set of all undirected Hamilton cycles of that graph.
Then

\[
 {|\{C\in{\cal H}:C\cap B=\varnothing\}|\over|{\cal H}|}
          \ \ge\ 1-{2b\over m}.                             \tag{4.4}
\]

In particular, if `b<m/2`, at least one Hamilton cycle avoids every edge in
`B`.

#### Proof

The symmetric group on the ground coordinates is transitive on incidence
edges.  Every Hamilton cycle has `2N` edges, whereas the Middle Levels graph
has `mN` edges.  Double-counting pairs `(C,e)` with `e in C` shows that a
fixed incidence edge belongs to exactly the fraction `2/m` of all Hamilton
cycles.  The union bound over `B` proves (4.4).  \(\square\)

Proposition 4.2 handles **pure forbiddance** only.  Requiring even one
two-incidence Johnson path conditions on a much smaller family; edge
transitivity gives no bound on how another required path is distributed
inside that family.  Theorem 2.1 is the literal failure at four required
paths.

### Corollary 4.3 (an unconditional pure-forbidden circuit bank)

Let `F` be a q1-rainbow factor which uses no incidence in `B`.  If
`|B|<m/2`, choose a Hamilton target avoiding `B` by Proposition 4.2 and
decompose its symmetric difference with `F`.  This gives a Hamiltonizing
alternating-circuit family none of whose edges lies in `B`, using at most
`floor(2N/3)` circuits.

This is the genuine unconditional finite-forbidden theorem.  It does not
fix a required Johnson edge: a protected edge is present in both factors,
whereas a forbidden incidence is absent from both.  Nor can an entire lower
colour or owner be declared forbidden, since every spanning incidence
factor necessarily visits every such vertex.

Finally, the `upper` resource of a Boolean atom with physical edge `AB` is
the adjacent rank-`m+1` occurrence `A union B`.  It is not an arbitrary-width
interval OR witness of the eventual word.  Fixing `AB` preserves this
immediate union.  Preserving a longer interval OR additionally constrains
the chronology between its endpoints and is outside Theorem 1.1 and
Corollary 1.2.

## 5. Exact remaining protected theorem

For the bounded regenerative absorber, the q1/upper row can now be stated
without conflating two different claims.

> **Private rooted-extension gate.**  Select the `O(1)` packet options and a
> Middle Levels Hamilton target jointly so that the target contains every
> physical edge required to remain fixed and contains one common realizing
> edge for every named upper witness.  If the protected atoms are ordered,
> require one global orientation of the target to agree with all their
> tail/head directions.

Once this gate holds, Theorem 1.1 and Corollary 1.2 give all protected q1
occurrence routing, upper-witness preservation and the circuit bound (1.2)
for free.  Without it, constant cardinality, lower/upper injectivity and a
complete-host cycle space do not suffice, by Theorem 2.1.

The theorem is only about the owner/q1/immediate-upper occurrence layer.  It
does not preserve residence, deeper upper intervals, prefix/suffix OR decks,
or a common compiler cap.  Those guards must either be part of the rooted
target or be included in a stronger private packet interface.

## 6. Replay

Run

```text
python3 scratch/audit_o1_protected_q1_hamilton_extension_cut_20260801.py
```

The dependency-free audit checks the two displayed factors, the forced
perfect-matching proof, all `60` perfect matchings of `ML(5)`, finite
sharpness through protected size four, both Boolean `O^-` partitions and
the failure of complete-support privacy.  It also checks the protected
alternating-circuit theorem and the girth-six circuit count over every pair
of the `60` incidence factors and `24` Hamilton targets.

Dependencies, used at their exact scopes:

* `MATH_THEOREM_O1_FOUR_SECTOR_Q1_ALTERNATING_CIRCUIT_RESET_20260801.md`;
* `MATH_THEOREM_BOOLEAN_HEX_TERNARY_FOUR_RESOURCE_ABSORBER_20260801.md`.
