# Buffered hexagons: exact upper-ray cuts, the star-cover theorem, and the `s=1` calibration

Date: 2026-07-31  
Lane: A, arbitrary-width upper witnesses  
Status: exact cut criterion and conditional `O(md)` theorem proved; the
support-only claim is refuted; no all-parameter buffered atlas or new upper
bound is claimed

## 0. Verdict

An `O(d)`-support three-rail packet does **not**, by support size alone,
exclude only `O(md)` of the `m^2` standard hexagon choices `(b,c)`.
Arbitrary-width upper service is controlled by interval rays, not by the
five-row depth-two compiler halo.  A common anchor can meet the last old
witness of one target for all `m^2` choices.

There is, however, an exact positive theorem.  For one anchor, form the
bipartite graph whose edge `bc` means that packet `P_(b,c)` destroys every
old witness of some protected upper target and creates no replacement.
If this **global** bad-pair graph has a vertex cover of size at most `K d`,
then at most

\[
                         K m d                                      \tag{0.1}
\]

choices are forbidden.  More generally it is enough that the individual
protected-ray bad graphs have vertex covers whose total size is at most
`K d`.  This is a proof-safe, maximum-matching-checkable hypothesis by
König's theorem.  Separate `O(d)` exceptional sets chosen independently for
every target do not suffice unless their union still has size `O(d)`.

The standard incidence hexagon also gives a sharp obstruction.  If a
replacement ray for

\[
                 Y=C\cup\{a\}\cup E,\qquad |E|=q-1,                 \tag{0.2}
\]

must traverse a `c`-bearing packet atom, then the no-spill row forces
`c in E`.  Of the `m^2` pairs, at least

\[
                         m(m-q+1)                                   \tag{0.3}
\]

are forbidden.  For `q <= d=o(m)` this is `Theta(m^2)`: only `O(md)`
choices survive, the reverse of the proposed conclusion.

The current `k=17`, cyclic-cut `s=1` seed calibrates the obstruction rather
than bypassing it.  Its fixed base consists of 3,640 dominoes and protects
only width two/rank eight.  It has no inherited rank-nine-or-higher upper
bank.  The exact upper state of a completed tail is a complement clean-run,
or equivalently prefix/suffix interval, state.  A literal q8/q9-admissible
`B-U-U-U-B` collar has fresh rank-eight colours and distinct rank-nine turns
but four equal rank-ten windows.  Thus local hexagon legality does not even
force the first nontrivial upper plateau row.

## 1. Exact interval-cut ledger

Let

\[
                     T=(T_0,\ldots,T_{N-1})                         \tag{1.1}
\]

be a set chronology.  For a nonempty interval `I=[i,j]`, put

\[
 \operatorname{OR}_T(I)=\bigcup_{p=i}^jT_p,
 \qquad
 \partial I=\{i,i+1,\ldots,j-1\}.                                  \tag{1.2}
\]

For an upper target `Y`, retain the occurrence labels and define its old
witness bank

\[
 {\cal H}_T(Y)=\{(I,\partial I):\operatorname{OR}_T(I)=Y\}.          \tag{1.3}
\]

Let a packet `P_(b,c)` cut the old adjacency set `D_(b,c)`, transport the
resulting fragments, and insert new seams.  Let `X_(b,c)` be the set of OR
values of all intervals in the new chronology that cross at least one new
seam.

### Theorem 1.1 (exact last-witness criterion)

For every required upper target `Y`, packet `P_(b,c)` preserves `Y` if and
only if

\[
 \begin{split}
 &\text{some }(I,H)\in{\cal H}_T(Y)\text{ has }H\cap D_{b,c}=\varnothing,
 \\
 &\hspace{35mm}\text{or}\qquad Y\in X_{b,c}.                       \tag{1.4}
 \end{split}
\]

Equivalently, define

\[
 {\cal B}_Y=\{(b,c):
 D_{b,c}\cap H\ne\varnothing\text{ for every }(I,H)\in{\cal H}_T(Y),
 \quad Y\notin X_{b,c}\}.                                         \tag{1.5}
\]

Then a specified packet `P_(b,c)` preserves the complete protected upper
bank exactly when

\[
                         (b,c)\notin\bigcup_Y{\cal B}_Y.              \tag{1.6}
\]

At least one safe packet choice exists exactly when
\(\bigcup_Y{\cal B}_Y\ne B\times C\); every choice is safe exactly when the
union is empty.

An old hole has empty witness bank, so the universal quantifier in (1.5)
is vacuous and the formula correctly requires a new crossing witness.

#### Proof

An old interval is transported inside one fragment precisely when none of
its internal adjacencies is cut.  Orientation reversal preserves its union.
These intervals give the first line of (1.4).  Every other interval in the
new chronology crosses a new seam and is, by definition, recorded in
`X_(b,c)`.  The two classes partition all new intervals.  This proves
(1.4), and (1.5)--(1.6) are its negation target by target.  \(\square\)

For final oriented fragments `F_1,...,F_s`, the crossing deck in Theorem
1.1 is literal.  An interval beginning in `F_i` and ending in `F_j`, `i<j`,
has union

\[
 S\ \cup\!\bigcup_{i<h<j}w(F_h)\ \cup P,                            \tag{1.7}
\]

where `S` is a nonempty suffix union of `F_i`, `P` a nonempty prefix union
of `F_j`, and `w(F_h)` the whole-fragment union.  Reversal interchanges the
prefix and suffix chains and preserves the internal deck.  Thus (1.5) is a
finite exact separator, not an average-multiplicity condition.

### Lemma 1.2 (one candidate ray: no spill and no deficit)

Suppose a proposed replacement interval for `Y` consists of an unchanged
part with union `O` and packet-dependent letters with union `N_(b,c)`.
It witnesses `Y` exactly when

\[
               N_{b,c}\subseteq Y,
 \qquad        Y\setminus O\subseteq N_{b,c}.                         \tag{1.8}
\]

The first row is no spill and the second no deficit.

#### Proof

The interval union is `O union N_(b,c)`.  Equality with `Y` is equivalent
to its being both a subset and a superset of `Y`, which is precisely (1.8).
\(\square\)

## 2. Exact ray form on a Johnson segment

Let a rank-`r` Johnson segment be

\[
 V_{t+1}=V_t-\{\beta_t\}+\{\alpha_t\}.                              \tag{2.1}
\]

Fix a start \(p\) with \(V_p\subseteq Y\).  For a coordinate
\(x\notin V_p\), let \(\tau_p(x)\) be its first later addition time, with
value \(\infty\) if it is never added.

### Lemma 2.1 (first-arrival ray criterion)

Some interval starting at `p` has union `Y` if and only if

\[
 \max_{x\in Y\setminus V_p}\tau_p(x)
       <
 \min_{z\notin Y}\tau_p(z).                                        \tag{2.2}
\]

The maximum over the empty set is the start time and the minimum over an
empty set is \(\infty\).

#### Proof

The interval may stop immediately after the last required coordinate has
first arrived.  It has union exactly `Y` precisely when no forbidden
coordinate has arrived by then.  Deletions after a coordinate first arrives
are irrelevant to an accumulated union.  This is (2.2).  \(\square\)

Consequently an upper-ray guard is a comparison system between required and
forbidden first arrivals.  A bounded number of changed physical seams does
not bound the number of changed comparisons: transposing two arrival blocks
of linear size uses three cuts but reverses a quadratic rectangle of
comparisons.

## 3. The star-cover theorem

Fix one standard-hex anchor and parameter sets `B,C` with

\[
                         |B|,|C|\le m.                              \tag{3.1}
\]

Regard each set `B_Y` in (1.5) as the edge set of a bipartite graph on
\(B\sqcup C\); let \(G_{\rm bad}\) be their union.  Its edges are exactly the packet
choices forbidden by the complete protected witness bank.

### Definition 3.1 (star-cover protected-ray bank)

The witness bank is `SCPR(K,d)` if the union bad graph \(G_{\rm bad}\) has
a vertex cover of size at most \(Kd\).  Equivalently, there are global sets
\(F_B\subseteq B\), \(F_C\subseteq C\) such that

\[
 G_{\rm bad}\subseteq(F_B\times C)\cup(B\times F_C),
 \qquad |F_B|+|F_C|\le Kd.                                          \tag{3.2}
\]

A stronger sufficient certificate, sometimes easier to construct ray by
ray, is to give a vertex cover \(Q_Y\) of every target graph with

\[
                         \sum_Y|Q_Y|\le Kd.                           \tag{3.3}
\]

Indeed, \(\bigcup_YQ_Y\) is then a global cover.  The converse need not
hold because one global cover vertex may serve many target graphs and would
be counted repeatedly in (3.3).

### Theorem 3.2 (`O(md)` upper-guard loss)

Under `SCPR(K,d)`, at most `Kmd` choices `(b,c)` are forbidden.  Moreover
the minimum size of a global star cover is exactly the maximum matching
number of `G_bad`.

#### Proof

Let \(Q\) be a global cover of size at most \(Kd\).  Every vertex of the
bipartite parameter graph is incident with at most `m` edges, so

\[
 |E(G_{\rm bad})|\le\sum_{v\in Q}\deg(v)\le m|Q|\le Kmd.             \tag{3.4}
\]

König's theorem identifies the minimum vertex-cover size with the maximum
matching size.  \(\square\)

### Corollary 3.3 (order-stable ray bank)

Suppose every failed first-arrival comparison in (2.2), over the complete
protected bank, has at least one endpoint in one global active label set
`F` of size at most `Kd`.  If `b,c` are the two comparison labels, then
`G_bad` is covered by the corresponding `F`-vertices and (3.4) applies.

This is the rigorous form of the proposed cylinder calculation.  The set
`F` is common to the whole bank.  Having `O(d)` exceptional labels for each
target separately is insufficient if their union is large.

## 4. Constant support does not imply `SCPR`

For the standard incidence hexagon, fix

\[
                  C\subset C+a,\qquad |C|=m,                        \tag{4.1}
\]

and take `b in C`, `c notin C+a`.  Its circuit is

\[
 C,\ C+a,\ C-b+a,\ C-b+a+c,\ C-b+c,\ C+c.                          \tag{4.2}
\]

There are exactly `m^2` choices, and each circuit has constant support.
They also all contain the same anchor incidence `C subset C+a`.

### Proposition 4.1 (common-anchor quadratic obstruction)

Assume the anchor incidence belongs to the toggled old phase, lies in every
old witness of one protected target `Y`, and none of the packet phases
regenerates `Y`.  Then

\[
                  G_{\rm bad}=K_{m,m},qquad
                  |E(G_{\rm bad})|=m^2,qquad
                  \tau(G_{\rm bad})=m.                              \tag{4.3}
\]

Thus even constant support does not imply an `O(md)` forbidden set when
`d=o(m)`.

#### Proof

Every packet cuts the common last-witness anchor and, by hypothesis, creates
no replacement.  Theorem 1.1 makes every pair bad.  The edge count and
vertex-cover number of \(K_{m,m}\) are \(m^2\) and \(m\).  \(\square\)

This is not an artificial multiplicity objection.  A literal unique-witness
word realizes the premise: take two adjacent rank-`r` letters with union
`Y`, and make every other letter contain a marker outside `Y`.  Their
adjacency is the unique `Y`-interval.  Any boundary-equivalent packet which
cuts that adjacency and whose new crossing intervals retain the marker loses
`Y`.

### Proposition 4.2 (standard-hex no-spill obstruction)

Let the protected target be (0.2), where

\[
 E\subseteq[2m+1]\setminus(C+a),\qquad |E|=q-1.                     \tag{4.4}
\]

Assume its last old witness is cut and every available replacement interval
for packet `(b,c)` traverses at least one `c`-bearing atom of (4.2), with no
alternative private witness.  Then safety forces `c in E`.  Consequently

\[
 |E(G_{\rm bad})|\ge m(m-q+1),
 \qquad \tau(G_{\rm bad})\ge m-q+1.                                \tag{4.5}
\]

For `q<=d=o(m)`, the forbidden family is quadratic and the safe family has
size at most `m(q-1)=O(md)`.

#### Proof

Because `c notin C+a`, a `c`-bearing replacement atom spills outside `Y`
unless `c in E`.  This is the first row of (1.8).  There are `m-q+1`
choices of `c` outside `E`, and every one is bad for all `m` choices of
\(b\).  These edges contain \(K_{m,m-q+1}\), whose minimum vertex cover has
size \(m-q+1\).  \(\square\)

The hypothesis about traversing a `c`-bearing atom is deliberately explicit.
A private packet phase that recreates `Y` without that atom defeats this
particular obstruction; it is exactly the replacement-witness token required
by the composable buffered-hex theorem.

## 5. What the five-row halo does prove

For a depth-two nonflat row, replacing seam rows `I` changes maximal
envelopes only on

\[
                         J=I+\{0,1,2\}                              \tag{5.1}
\]

and replay equations only on

\[
                         H=I+\{-2,-1,0,1,2\}.                       \tag{5.2}
\]

This is the exact five-row common-cap transport theorem.  With `m` seams
and depth `d`, its direct collar generalization has `O(md)` row data.  It is
not an upper-witness theorem.  A prefix or suffix union may stay on a
low-rank plateau for arbitrarily many rows, so the exact upper state remains
the prefix/suffix interval-union monoid of (1.7).  The `O(md)` in (5.1)--
(5.2) must not be reused as the number of forbidden hexagon choices without
Theorem 3.2's separate `SCPR` certificate.

Also, `O(md)` forbidden packet choices is list pruning, not terminal defect.
The additive-constant spine theorem still requires a selected compatible
packet family whose carried defect and terminal completion charge are
bounded absolutely.

## 6. Finite `s=1` calibration

The current adjacent-cut `k=17` base is a matching of 3,640 rank-seven
dominoes.  Its only protected internal upper values are the 3,640 rank-eight
edge unions.  In particular it has no old rank-nine-or-higher bank to which
Theorem 3.2 could be applied; those targets must be regenerated by the
selected ears and their global order.

Exactly 572 direct ears can be selected with the certified fresh q8/q9 and
endpoint conditions.  If the remaining ears are restricted to the two
adjacent edge lengths four and five, the resulting scalar shell is forced to
have

\[
                  x_1=572,\qquad x_4=2637,\qquad x_5=430,            \tag{6.1}
\]

where `x_l` counts ears with `l` new edges.  The direct-ear floor is
unconditional for the immutable `s=1` seed and sharp at that layer; the
restriction to residual lengths four and five is a proposed scalar shell,
not a normal-form theorem.  In that shell 3,067 long ears and 9,631 internal
owners remain to choose.  This is a carrier/palette result, not an upper
bank.

For a completed tail path `X_0,...,X_16910` of rank-seven owners, put
\(Z_i=[17]\setminus X_i\).  Call a run \(C\)-clean when
\(C\subseteq Z_i\) at every position of the run.  For
\(U=[17]\setminus C\), \(10\le |U|\le16\), the exact tail-only criterion is

\[
 U\text{ has a witness}
 \quad\Longleftrightarrow\quad
 \text{some maximal }C\text{-clean run }R
 \text{ satisfies }\bigcap_{i\in R}Z_i=C.                          \tag{6.2}
\]

Equivalently, the corresponding run of the `X`-path has union `U`.  This is
the finite complement form of Theorem 1.1 and must be composed with the
prefix and the physical boundary-gap bank.

The first missing local propagation row already appears in a literal
endpoint-conditioned ear.  In hexadecimal notation take the seven rank-seven
owners

\[
 (\mathtt{e829},\mathtt{e82a},\mathtt{e02e},\mathtt{e01e},
  \mathtt{e01d},\mathtt{e815},\mathtt{e834}).                         \tag{6.3}
\]

The core is a legal `B-U-U-U-B` ear; its two `B` endpoints lie in distinct
`s=1` dominoes and the three inner owners lie outside the base.  Its four new
rank-eight unions are

\[
 \mathtt{e82e},\ \mathtt{e03e},\ \mathtt{e01f},\ \mathtt{e81d},      \tag{6.4}
\]

and its five collar rank-nine turns are

\[
 \mathtt{e82f},\ \mathtt{e83e},\ \mathtt{e03f},
 \ \mathtt{e81f},\ \mathtt{e83d}.                                  \tag{6.5}
\]

All labels in each displayed list are distinct, and the four labels in
(6.4) are fresh relative to the old base bank.  Nevertheless all four
consecutive four-owner unions are

\[
                              \mathtt{e83f}.                         \tag{6.6}
\]

Thus the exact endpoint-conditioned q8/q9 rows do not regenerate even a
rank-ten rainbow.  This does not rule out a globally ordered long-ear
solution.  It proves that such a solution needs the clean-run/prefix-suffix
state and cannot be certified by an `O(d)` local hex collar.  The example is
not asserted to survive the active supported-ear peel or to satisfy the
lower-provider, quotient-topology, repeat-decoration or compiler rows.

## 7. Precise remaining theorem

The buffered-hex `B(k)+O(1)` route survives under the following additional
upper hypothesis, and not from packet support alone:

> At every private anchor, the complete protected arbitrary-width witness
> bank has an `SCPR(K,d)` certificate after accounting for common anchor
> tokens and explicit private replacement rays.  These certificates are
> global across all targets and coexist with the common-cap, topology,
> residence and task-to-anchor load tokens.

Together with the already stated global token-load and composition rows,
this yields `m^2-O(md)` upper-safe choices per anchor.  Neither the present
general theory nor the `s=1` calibration proves this hypothesis.  In the
`s=1` lane the immediate finite gate is stronger: first choose and order the
3,067 long ears so that (6.2), the prefix crossing bank and the exceptional
physical gap cover the full upper tower while retaining q8/q9 and the lower
compiler data.
