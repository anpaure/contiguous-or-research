# `k=15`: exact seam obligations for the nine-cycle all-shadow factor

Date: 2026-07-29

Status: theorem-level opening reduction plus independently replayed input
factor.  This note does **not** claim an optimal word.  It explains exactly
why the new nine-cycle factor is close, why arbitrary concatenation is not
enough, and what the final finite search must certify.

## 1. New audited input

The retained factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    u2u3l3_s801.engine.json
```

has the following independently replayed properties:

```text
middle vertices                         6435, each once
lower-q1 colours                        6435, each once
physical components                     9
component lengths        1890, 774^5, 555, 75, 45
minimum cyclic coordinate run            4
residence violations                     0
all lower targets, every depth        complete
all upper targets, every rank         complete
Xi                                        9
```

The exact physical replay is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    u2u3l3_s801.audit.json
```

and a second independent factor audit is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    u2u3l3_s801.independent.factor.audit.json.
```

Their source-candidate SHA-256 is

```text
886877094a3eaba8950136728d131782141a4b6f882d570ecb3791827da98f83.
```

Thus the carrier geometry, residence, and every cyclic shadow deck are now
simultaneously solved.  Only linear opening/splicing and the exact lower
compiler remain.

## 2. General opening notation

Let `C_1,...,C_c` be disjoint directed cycles whose vertices partition the
rank-`r` layer.  Assume their edge colours

\[
 \chi(U,V)=U\cap V\in\binom{[k]}{r-1}
\]

form a bijection onto the entire rank-`r-1` layer.  This holds for the new
factor with `(k,r,c)=(15,8,9)`.

Choose one directed cut edge

\[
 e_j=(Z_j,A_j)
\]

in each cycle and read the resulting path from `A_j` to `Z_j`.  Choose an
orientation and an order of the `c` paths and concatenate them to form a
linear middle word

\[
 T=(T_0,\ldots,T_{W-1}).
\]

Let

\[
 R=\{\chi(e_1),\ldots,\chi(e_c)\}.              \tag{1}
\]

The cut colours are distinct because the original lower-q1 deck is exact.
All `W-c` uncut internal adjacencies retain the other `W-c` colours.

## 3. Exact lower-q1 current and source-boundary absorption

The first version of this note incorrectly treated the two global boundary
capacities as values of `Y=D^(d-1)A`.  They are not.  For the maximal
depth-three erosion `P` of `T`,

\[
 P_0=T_0,\qquad P_1=T_0\cap T_1,
\]

and consequently `(D^2P)_0=T_0`, of rank eight, not rank seven.  A deleted
rank-seven colour can instead be installed as a literal **source** letter
`A_0` or `A_(W+2)`, subject to the one-core equation `DA=DP`.

Let the eight new seams be Johnson edges, and let

\[
 Q=\{Z_j\cap B_j:1\le j\le8\}
\]

denote their set of distinct lower colours (with multiplicity forgotten).
The internal adjacent-intersection support of the spliced middle path is
exactly

\[
 \left(\binom{[15]}7\setminus R\right)\cup Q.  \tag{2}
\]

Thus its exact lower-q1 hole set is

\[
 H=R\setminus Q.                               \tag{3}
\]

In particular `H` is nonempty, because a path has only `W-1` adjacent
windows.  It has size one exactly when the eight seam colours are eight
distinct members of the nine-colour cut palette.  A seam may recycle the
cut colour of a third component: requiring it to equal one of its two
incident cut colours is a useful sufficient subcatalogue, not a necessary
condition.

### Lemma 3.1 (erosion grading and the two boundary channels)

For every depth-three-resident Johnson path, its maximal erosion has rank
profile

\[
 8,7,6,\underbrace{5,\ldots,5}_{W-3\text{ entries}},6,7,8.    \tag{4}
\]

Moreover, if `A` is any antecedent with `D^3A=T`, every rank-seven interval
of `A` which does not meet a global source boundary is one of the adjacent
intersection colours already present in the middle path.  Consequently a
colour in `H` can be realized only through the left or right global source
boundary, at most one distinct rank-seven target per side.

**Proof.**  An internal erosion letter is the intersection of four
consecutive middle states.  Across their three Johnson transitions, the
three deleted coordinates are distinct and all belong to the first state:
repeating a deletion would require a reinsertion followed by deletion in at
most three steps, and deleting a newly inserted coordinate would create a
positive run of length at most three.  Both contradict residence.  Hence
the internal intersection has rank `8-3=5`.  The three truncated letters at
each end give the displayed ranks.

Every antecedent satisfies \(A_p\subseteq P_p\).  An interval of at least four
source letters contains a four-letter window equal to a rank-eight middle
state, so it cannot have rank seven.  For intervals of at most three letters
away from the global ends, their maximal envelopes are values of `P`, `DP`,
or `D^2P`.  The only rank-seven values among these are

\[
 (D^2P)_i=T_{i-1}\cap T_i\qquad(1\le i\le W-1),               \tag{5}
\]

and the two adjacent truncated copies of the first or last retained edge
colour.  If a union of source letters has rank seven inside a rank-seven
envelope, it equals that envelope.  Thus it is an existing path-edge
colour, never a member of `H`.

At either global boundary the source intervals of lengths one, two, and
three are nested.  Distinct nested sets of the same rank cannot occur, so
that side can realize at most one rank-seven target.  \(\square\)

It follows immediately from (3) and Lemma 3.1 that

\[
 |H|\le2,
 \qquad |R\cap Q|\ge7.                         \tag{6}
\]

Thus at least seven of the eight seam colours must be distinct members of
the removed palette.  This is a genuine necessary condition, not a scalar
slack heuristic.

### Lemma 3.2 (exact source-endpoint eligibility)

Let `P` be the maximal depth-three erosion of a resident Johnson path `T`.
Leave every source letter equal to `P` except possibly the left endpoint.
For a rank-seven target `S`, replacing `P_0` by `S` preserves the first
one-core equation `DA=DP` if and only if

\[
 S\subset T_0,\qquad T_0\setminus T_1\subseteq S.              \tag{7}
\]

At the right endpoint the corresponding condition is

\[
 S\subset T_{W-1},\qquad
 T_{W-1}\setminus T_{W-2}\subseteq S.                          \tag{8}
\]

**Proof.**  At the left boundary \(P_0=T_0\) and
\(P_1=T_0\cap T_1\).  The only changed adjacent union is therefore

\[
 S\cup P_1=P_0\cup P_1=T_0.
\]

This equality is equivalent to (7).  The proof of (8) is the reversed
argument.  Notice that the target is the source value `A_0`; it is generally
not a value of `D^2A`.  \(\square\)

Define a two-vertex bipartite graph from `H` to `{L,R}` using (7) and (8).
An injection in this graph is exactly a boundary-only realization of the
q1 holes, provided those source positions are frozen in the compiler (or,
equivalently, the adjacent `DA=DP` equations are retained in the joint
compiler model).  Hence boundary-only repair requires `|H|<=2`.

There is a useful automatic case.  If the unrecycled colour is the cut
colour of the component placed first, it is eligible at `L`; similarly the
cut colour of the last component is eligible at `R`.  Indeed, at the first
middle vertex the retained and deleted factor edges have distinct lower
colours.  Their two deleted coordinates are therefore distinct, so the
coordinate forced by (7) belongs to the cut facet.  This proves:

### Corollary 3.3 (endpoint cut-colour absorption)

If the seam palette leaves at most two cut colours unrecycled and their
components are assigned injectively to the two global ends, those colours
have legal literal source-boundary pins.  In particular, eight distinct
recycled cut colours plus the remaining component at either global end give
an exact q1 repair.

The bound of seven useful seams is necessary by Lemma 3.1; the endpoint SDR
is the remaining exact realization test in the two-hole case.  The scalar
lower-array slack remains

\[
 3\binom{15}{8}+\binom42-\sum_{j=1}^7\binom{15}j=2928,          \tag{9}
\]

but it is only cardinality slack, not a compiler-Hall certificate.

## 4. Residence collar theorem

Every coordinate run internal to one opened path is inherited from a cyclic
run and already has length at least four.  Only prefixes and suffixes at the
chosen cuts can change.

For a path `P`, let `p_x(P)` and `s_x(P)` be the positive prefix and suffix
lengths of coordinate `x` (zero if the endpoint omits `x`).  At a seam
`P -> Q`:

* if both endpoint bits are one, the new run has length `s_x(P)+p_x(Q)`;
* if only the left endpoint bit is one, its suffix becomes an internal run
  of length `s_x(P)`;
* if only the right endpoint bit is one, its prefix becomes an internal run
  of length `p_x(Q)`.

Thus the seam is depth-three resident exactly when every nonzero length in
the preceding list is at least four.  The two global boundary fragments are
not internal and need no length lower bound.  These are finite collar tests
depending on at most three vertices on either side of a seam.

## 5. Exact one-seam shadow ledger

Literal replay gives two additional seed-specific facts:

\[
 \bigcup_{X\in C_i}X=[15],\qquad
 \bigcap_{X\in C_i}X=\varnothing                \tag{10}
\]

for each of the nine physical components.  Their minimum length is `45`,
which is greater than every audited depth `q<=7`.

For an oriented cut state `p`, let \(I_{p,q}^+(U)\) and
\(I_{p,q}^-(L)\) be the numbers of wholly internal `(q+1)`-state windows
having union `U` and intersection `L`.  For an oriented seam `a:p->p'`,
let \(G_{a,q}^+(U)\) and \(G_{a,q}^-(L)\) be the corresponding numbers of
windows crossing that seam.  If `o_p` selects ports and `z_a` selects seams,
then the new fixed-window multiplicities are exactly

\[
 m_q^\pm(S)=
 \sum_p I_{p,q}^\pm(S)o_p+
 \sum_a G_{a,q}^\pm(S)z_a.                     \tag{11}
\]

Consequently fixed-depth support is preserved exactly when

\[
 m_q^\pm(S)\ge1                                \tag{12}
\]

for every prescribed target `S`.  For lower q1, (12) must be replaced by
the exact residual ledger (2)--(3), because a linear middle path cannot
have all `W` lower-q1 colours in only `W-1` internal windows.

Equation (11) is exact, not merely sufficient: a window of at most eight
vertices cannot meet two seams because every intervening segment has at
least 45 vertices.  The same locality remains true for intervals of
arbitrary width and proper upper targets.  An interval crossing two seams
contains a whole intervening component, and therefore has union `[15]` by
(10).  Thus every proper upper witness is either internal to one opened
component or crosses exactly one seam.  If `I_p^+(U)` and `G_a^+(U)` denote
the corresponding arbitrary-width occurrence indicators, exact upper
coverage is

\[
 \boxed{\sum_p I_p^+(U)o_p+
        \sum_a G_a^+(U)z_a\ge1}
 \qquad(8<|U|<15).                              \tag{13}
\]

The full target `[15]` is already witnessed inside every component.  Dually,
because every component has empty total intersection, every nonempty lower
interval witness also meets at most one seam.  Formulae (11)--(13) therefore
contain the complete shadow ledger; no multi-seam shadow automaton is needed
for this seed.

The exact port topology is the usual integral path flow.  There are
`2*6435=12870` oriented cut states.  Select exactly one state on each of the
nine components, give every selected state indegree and outdegree one except
for one global start and end, select eight arcs, and impose the component
subtour inequalities.  Retain only Johnson and depth-three collar-compatible
arcs.  These equations are necessary and sufficient for one resident
Johnson chronology once the local collar test of Section 4 is imposed.

## 6. Exact compiler coupling

Let `T` be a chronology accepted by the port and shadow rows, and let its
maximal depth-three erosion be

\[
 P_j=\bigcap_{\max(0,j-3)\le i\le\min(W-1,j)}T_i,
 \qquad 0\le j\le W+2.                          \tag{14}
\]

The residence condition and Johnson transitions imply that every `P_j` is
nonempty and

\[
 D^3P=T.                                        \tag{15}
\]

Let `supp(R)` denote the set of values occurring in a row `R`, and define
the literal residual family

\[
 \mathcal F(P)=
 \bigcup_{s=1}^{5}\binom{[15]}s
 \ \cup\
 \left(\binom{[15]}6\setminus\operatorname{supp}(DP)\right)
 \ \cup\
 \left(\binom{[15]}7\setminus\operatorname{supp}(D^2P)\right).
                                                               \tag{16}
\]

In particular, every q1 hole in (3) belongs to the last term of (16).  It
is a literal source target, not a missing value to be inserted into `D^2A`.

### Theorem 6.1 (exact adaptive one-core compiler)

There is an adaptive one-core source word `A` with `DA=DP` which realizes
every target in (16) as a distinct literal source letter if and only if there
is a (possibly empty-lettered) core word `C` satisfying

\[
 C_p\subseteq P_p,
 \qquad C_p\cup C_{p+1}=P_p\cup P_{p+1}         \tag{17}
\]

and the bipartite graph

\[
 S\sim p\quad\Longleftrightarrow\quad
 C_p\subseteq S\subseteq P_p                   \tag{18}
\]

has a matching saturating \(\mathcal F(P)\).  Equivalently, for this `C`,

\[
 |N_C(X)|\ge |X|\qquad(X\subseteq\mathcal F(P)).               \tag{19}
\]

If source-boundary pins from Corollary 3.3 are used, their target-position
edges are fixed in this matching; (19) is then imposed on the remaining
targets and unreserved positions.  The endpoint equations (7)--(8), or the
same adjacent-union equations inside (17), must also be retained.

**Proof.**  Given `C` and a matching, put `A_p=S` at a position matched to
`S` and put `A_p=P_p` at every unmatched position.  Then

\[
 C\subseteq A\subseteq P,
 \qquad DC=DP,
\]

so \(DP=DC\subseteq DA\subseteq DP\); hence `DA=DP` and, by (15),
`D^3A=T`.  Every residual target is a literal source letter.  Conversely,
an adaptive one-core realization supplies its core `C`, with
\(C\subseteq A\subseteq P\) and `DC=DP`, and its distinct
target positions, which give (17)--(19).  Hall's theorem gives the
equivalence of (18) and (19).  \(\square\)

Targets of ranks six and seven outside (16) already occur in `DP` or
`D^2P`.  Every middle target occurs in `T`; every upper target supplied by
(13) is a union of a contiguous interval of `T`, hence of the corresponding
expanded interval of `A`.  Therefore port flow, residence, (13), and
Theorem 6.1 together are an exact sufficient consumer for a 6438-letter
literal OR word.

## 7. The smallest remaining finite gate

For the retained nine-factor it is enough, and within the direct-Johnson
one-cut-per-component/adaptive-one-core architecture it is necessary, to
find:

1. one oriented cut state on each physical cycle and eight arcs satisfying
   the integral nine-component path equations;
2. the eight local residence-collar tests;
3. the targetwise fixed-shadow rows (11)--(12), or the weaker exact
   arbitrary-width upper rows (13), together with the q1 residual ledger
   (2)--(3);
4. one core `C` and one physical matching satisfying (16)--(19), including
   any chosen source-boundary pins; and
5. a retained 6438-letter word passing the independent literal verifier.

The full-union/empty-intersection facts (10) eliminate every longer-history
shadow state.  Thus the finite gate is a labelled Hamilton path on nine
selected ports followed by one exact physical core-Hall instance.  The
existing endgame program's restriction that every recycled seam colour be
incident to that seam is a sound sufficient search subfamily but is not the
whole gate.  Failure of that subfamily, one cut portfolio, or one path order
is not a nonexistence theorem.
