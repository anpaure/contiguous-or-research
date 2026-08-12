# Pin survival in an ordered orthogonal-chain pair

This note isolates the coordinate-pinning part of the global normal form in
`GLOBAL_FLAG_RIGIDITY.md`.  Everything stated as a theorem or lemma below is
proved.  No finite-`k` search or conjectural chain construction is used.

Let two orthogonal chain partitions of the punctured Boolean lattice be
ordered by positions `1,...,n`.  A mask `S` occupies the unique cell

\[
   (\ell(S),r(S)),\qquad \ell(S)\le r(S),
\]

and is assigned the interval

\[
   I_S=[\ell(S),r(S)].
\]

For a coordinate `b`, call `S` **positive** if `b in S` and **negative** if
`b notin S`.  Pinning is coordinatewise, so throughout Sections 1--6 one
coordinate is fixed.

## 1. Clean diagonal cuts: an exact graph/order criterion

Regard every occupied cell `(p,q)` as an edge from the `p`-th left chain to
the `q`-th right chain.  For `j in [n]`, the **diagonal cut at `j`** consists
of the left-chain prefix `1,...,j` and the right-chain suffix `j,...,n`.
An edge `(p,q)` crosses this cut exactly when

\[
   p\le j\le q.
\]

Call the cut **`b`-clean** when no negative edge crosses it.

### Theorem 1 (clean-cut criterion)

The prescribed intervals are pinnable in coordinate `b` if and only if every
positive edge `(p,q)` spans a `b`-clean cut:

\[
   b\in S
   \quad\Longrightarrow\quad
   \text{there is }j\in[p,q]\text{ crossed by no negative edge}.       \tag{1.1}
\]

Equivalently, define the negative frontier

\[
 H_b(j)=\max\bigl(\{r(S):b\notin S,\ \ell(S)\le j\}\cup\{0\}\bigr).
                                                                    \tag{1.2}
\]

Then

\[
   j\text{ is `b`-clean}\quad\Longleftrightarrow\quad H_b(j)<j,       \tag{1.3}
\]

and pin survival is

\[
   \min\{j\ge p:H_b(j)<j\}\le q
   \quad\text{for every positive cell }(p,q).                         \tag{1.4}
\]

#### Proof

A position `j` is forbidden for `b` precisely when it lies in a selected
negative interval.  Such an interval contains `j` precisely when its edge
crosses the diagonal cut at `j`.  Thus the clean positions are exactly

\[
 Z_b=[n]\setminus\bigcup_{S:b\notin S}I_S.
\]

A positive interval can contain `b` without contaminating a negative interval
exactly when it meets `Z_b`.  This proves (1.1).  A negative interval crosses
`j` exactly when its left endpoint is at most `j` and its right endpoint is at
least `j`; maximizing the latter gives (1.3), and (1.4) is merely (1.1) with
the first clean cut written explicitly.  QED.

This is a useful translation: the pin problem is not an additional SAT
problem on arbitrary subsets.  It is a clean-diagonal-cut problem in an
ordered bipartite incidence graph.

## 2. Exact compression to one switch per left chain

Along one left chain, masks increase with the right endpoint.  Membership of
`b` can therefore change from zero to one at most once.

For each row `p`, define

\[
 a_p(b)=\max\bigl(\{q:(p,q)\text{ is occupied and negative}\}\cup\{p-1\}\bigr)
                                                                    \tag{2.1}
\]

and

\[
 c_p(b)=\min\bigl(\{q:(p,q)\text{ is occupied and positive}\}\cup\{+\infty\}\bigr).
                                                                    \tag{2.2}
\]

If both kinds occur in the row, then `a_p(b)<c_p(b)`.  All negative intervals
in row `p` have union `[p,a_p(b)]`, and every positive interval in that row
contains the shortest positive transition interval `[p,c_p(b)]`.

### Theorem 2 (row-transition compression)

For a fixed coordinate `b`, the following are equivalent.

1. Every positive assigned interval survives.
2. For every row with `c_p(b)<+infinity`,

   \[
      [p,c_p(b)]\cap Z_b\ne\varnothing.                              \tag{2.3}
   \]

3. For every such row,

   \[
      \min\{j\ge p:H_b(j)<j\}\le c_p(b).                            \tag{2.4}
   \]

Moreover,

\[
 Z_b=[n]\setminus\bigcup_{p:a_p(b)\ge p}[p,a_p(b)],                 \tag{2.5}
\]

so the exponentially many masks have been compressed to at most `n` negative
row barriers and at most `n` positive row transitions.

#### Proof

Nestedness in a left chain proves the descriptions of `a_p` and `c_p`.
Replacing all negative intervals with their row-wise union does not change
their total union, proving (2.5).  In a fixed row, if the shortest positive
interval meets `Z_b`, every longer positive interval meets it; conversely the
shortest positive interval itself must meet it.  This proves the equivalence
of 1 and 2.  Theorem 1 proves the equivalence with 3.  QED.

There is a dual column statement.  Along a right chain, inclusion grows as
the left endpoint decreases.  Let `s_q(b)` be the minimum left endpoint of a
negative cell in column `q`, and let `t_q(b)` be the maximum left endpoint of
a positive cell, with the natural empty conventions.  For a proposed pin set
`P_b`, put

\[
 z^+_b(p)=\min(P_b\cap[p,n]),\qquad z^-_b(q)=\max(P_b\cap[1,q]).
\]

Then `P_b` realizes the bit labels exactly if and only if the following local
switch inequalities hold wherever the displayed pin exists:

\[
   a_p(b)<z^+_b(p)\le c_p(b)                                        \tag{2.6}
\]

for every row having a positive cell, with only the left inequality required
for a negative-only row, and dually

\[
   t_q(b)\le z^-_b(q)<s_q(b)                                        \tag{2.7}
\]

for every column having a positive cell.  If a row has a positive cell, its
next pin must exist; if a column has a positive cell, its previous pin must
exist.  These inequalities are simply the statement that the next/previous
pin lies after the zero-to-one switch and inside the first positive interval.

### Corollary 3 (canonical sparse pins)

Assume pin survival.  A minimum-cardinality pin set for coordinate `b` is
obtained canonically as follows.

1. Compute the clean set `Z_b` from (2.5).
2. Sort the transition intervals `[p,c_p(b)]` by increasing right endpoint.
3. On encountering an interval not hit by an earlier chosen pin, choose its
   rightmost point in `Z_b`.

The resulting set `P_b subseteq Z_b` hits every positive assigned interval,
avoids every negative interval, and uses the minimum possible number of
occurrences of bit `b`.

#### Proof

By Theorem 2, every transition interval contains an allowed point.  The
standard right-endpoint greedy proof for interval stabbing applies even after
restricting possible points to `Z_b`: if an optimal solution hits the earliest
finishing unhit interval at `y`, replace `y` by its rightmost legal point `z`.
Then `y<=z` and every remaining interval has right endpoint at least that of
the current interval, so any remaining interval hit only by `y` is also hit by
`z`.  Induction proves optimality.  Since every other positive interval
contains a transition interval, all positive cells are hit.  QED.

Thus, once the two chain orders are known, there is no further ambiguity about
how to obtain a sparse factor: each coordinate has a deterministic greedy pin
assignment.

## 3. Exact forbidden certificates

The union of integer intervals has components that are integer intervals.
Here two intervals belong to the same component when they overlap or abut
(for example `[1,2]` and `[3,5]` leave no legal integer position between
them).

### Theorem 4 (negative-bridge certificate)

Pinning fails for a positive cell `S` in coordinate `b` if and only if there
are negative masks `T_1,...,T_h`, ordered after deletion of redundancies, such
that

\[
\begin{aligned}
 &\ell(T_1)<\ell(T_2)<\cdots<\ell(T_h),\\
 &r(T_1)<r(T_2)<\cdots<r(T_h),\\
 &\ell(T_1)\le\ell(S),\qquad r(T_h)\ge r(S),\\
 &\ell(T_{i+1})\le r(T_i)+1\quad(1\le i<h).                          \tag{3.1}
\end{aligned}
\]

In words: a monotone, overlapping-or-abutting path of negative edges bridges
the entire positive edge.

#### Proof

If (3.1) holds, the negative intervals cover every integer position from
`ell(S)` through `r(S)`, so `I_S cap Z_b` is empty.  Conversely, if `I_S` is
covered by negative intervals, take an inclusion-minimal finite subcover and
order it by left endpoint.  Delete any interval contained in another.  The
left and right endpoints are then both strictly increasing.  Minimal coverage
forces the first interval to begin no later than `ell(S)`, the last to end no
earlier than `r(S)`, and consecutive intervals to overlap or abut.  QED.

The certificate can be arbitrarily long; row/column chain monotonicity does
not reduce pinning to two-cell diamonds.

### Proposition 5 (no bounded local-cover reduction)

For every `h>=2` there is a partial ordered, triangular, orthogonal-chain
incidence pattern satisfying interval-containment monotonicity in which a
positive interval has a unique minimum negative cover of size `h`.

#### Proof

Use positions `1,...,h` and ground elements `b,1,...,h`.  Assign

\[
  T_i=\{i\}\longleftrightarrow[i,i]\quad(1\le i\le h),
  \qquad
  S=\{b,1,...,h\}\longleftrightarrow[1,h].                           \tag{3.2}
\]

The first row is the chain `{1} subset S`, the last column is the chain
`{h} subset S`, and every other used row and column is a singleton chain.
No cell is repeated, all cells are triangular, and whenever one displayed
interval contains another, the corresponding masks are nested in the same
direction.  The positive interval `[1,h]` is covered by the `h` negative
singleton intervals, and every one is necessary.  QED.

Consequently, ordinary orthogonality, endpoint-chain order, and even global
interval-containment monotonicity do not imply pin survival.  A genuinely
global separator, closure, or growth-diagram property is required.

## 4. A proved pairwise/local sufficient rule

Although arbitrary failure certificates can be long, a strong local closure
property collapses them.

Call an assigned interval system **containment-monotone** when

\[
   I_X\subseteq I_Y\quad\Longrightarrow\quad X\subseteq Y.           \tag{4.1}
\]

For a coordinate `b`, call it **negative-hull closed** when, whenever two
assigned negative intervals overlap or abut, there is an assigned negative
mask `Z` such that

\[
   \operatorname{hull}(I_X\cup I_Y)\subseteq I_Z.                    \tag{4.2}
\]

### Theorem 6 (hull-closure sufficient criterion)

If the interval system is containment-monotone and is negative-hull closed
for every coordinate, then it is pinnable.

#### Proof

Suppose pinning fails for a positive mask `S` and bit `b in S`.  Take the
negative bridge `T_1,...,T_h` from Theorem 4.  Apply (4.2) to the first two
members.  It gives a negative assigned interval containing their hull.  This
new interval overlaps or abuts `I_{T_3}`, so repeat.  Inductively one obtains
a negative assigned interval `I_Z` containing the hull of the entire bridge,
hence containing `I_S`.  Containment monotonicity gives `S subseteq Z`, which
is impossible because `b in S` and `b notin Z`.  QED.

This condition is deliberately strong, but it is a genuine two-interval rule
that proves all global pin constraints at once.  It identifies what a local
diamond construction must arrange: negative adjacent pieces must have a
negative hull available before they can form a long barrier.

## 5. Boolean growth diagrams: exact local equivalence

Let

\[
   \Delta_n=\{(p,q):1\le p\le q\le n\}
\]

be the full triangular interval grid.  A set-valued Boolean join growth
diagram is a map `F:Delta_n -> 2^[k]` satisfying the local diamond rule

\[
   F(p,q)=F(p,q-1)\cup F(p+1,q)\qquad(p<q).                           \tag{5.1}
\]

### Theorem 7 (growth-diagram completion theorem)

For a partial assignment `I_S=[p,q] -> S`, the following are equivalent.

1. The assigned intervals are pinnable.
2. Their labels extend to a set-valued growth diagram on all of `Delta_n`.
3. For every coordinate `b`, the prescribed zero/one labels extend to a
   Boolean growth diagram

   \[
      x_b(p,q)=x_b(p,q-1)\vee x_b(p+1,q).                            \tag{5.2}
   \]

#### Proof

If an array `A_1,...,A_n` realizes the assignments, set

\[
   F(p,q)=A_p\cup\cdots\cup A_q.
\]

This gives (5.1) and the required labels.  Conversely, induction on `q-p`
in (5.1) gives

\[
   F(p,q)=\bigcup_{j=p}^q F(j,j).
\]

Thus `A_j=F(j,j)` realizes every assigned interval.  The coordinatewise
version is identical and coordinates can be combined independently.  QED.

There is a canonical maximal completion test.  Define

\[
   K_j=\bigcap_{S:j\in I_S}S,                                       \tag{5.3}
\]

with `[k]` as the empty-intersection convention, and put

\[
   F^{\max}(p,q)=\bigcup_{j=p}^qK_j.                                \tag{5.4}
\]

Then `b in K_j` exactly when `j` is `b`-clean.  Every possible realizing
entry satisfies `A_j subseteq K_j`, while putting `A_j=K_j` is safe against
every negative interval.  Therefore:

### Corollary 8 (canonical maximal factor)

The assignment is pinnable if and only if

\[
   F^{\max}(\ell(S),r(S))=S\qquad\text{for every assigned }S.        \tag{5.5}
\]

Equivalently, the canonical maximal diagonal `A_j=K_j` realizes all labels.

Theorem 7 is the exact local-diamond answer.  Long negative bridges are
precisely chains of local zero information that force a zero at a cell which
was prescribed positive.  Proposition 5 explains why those intermediate
diamond cells cannot simply be ignored.

### Corollary 9 (short-strip local rule)

Suppose labels have been assigned to some intervals of lengths at most `d+1`.
If the unassigned cells in that strip can be filled so that (5.1) holds and
all assigned labels are respected, then the singleton diagonal realizes every
assigned short interval.  In particular, whenever every cell of lengths at
most `d` is assigned, the diamond identities in that strip are necessary and
sufficient for the lower part of the construction.

This gives a rigorous local construction rule: complete the band to a Boolean
join growth diagram; the diagonal is then the desired factor, with no further
pin SAT instance.

## 6. Fixed delay: central runs, lower constraints, and automatic upper rows

The general criterion specializes cleanly to the usual central-row ansatz.
Let `T_1,...,T_M` be prescribed at the fixed intervals

\[
   [i,i+d],\qquad 1\le i\le M,
\]

and define the maximal central envelopes

\[
 E_j=\bigcap_{i=\max(1,j-d)}^{\min(M,j)}T_i,
 \qquad 1\le j\le M+d.                                               \tag{6.1}
\]

### Lemma 10 (run-factorization theorem)

The maximal factor satisfies

\[
   T_i=E_i\cup\cdots\cup E_{i+d}\quad(1\le i\le M)                 \tag{6.2}
\]

if and only if, for every coordinate, every internal run of ones in its
incidence word on `T_1,...,T_M` has length at least `d+1`.  Runs meeting either
boundary may be shorter.

#### Proof

Fix a coordinate and an internal positive run `[u,v]`.  Formula (6.1) permits
that coordinate exactly at factor positions `[u+d,v]`; this is nonempty
exactly when `v-u+1>=d+1`.  A left-boundary run `[1,v]` permits positions
`[1,v]`, and a right-boundary run `[u,M]` permits `[u+d,M+d]`, so every
nonempty boundary run has a pin.  These allowed positions hit exactly the
positive central windows, proving both directions.  QED.

For `i<=j`, define the upper join diagram

\[
   U(i,j)=T_i\cup T_{i+1}\cup\cdots\cup T_j.                         \tag{6.3}
\]

Any factor of the central row automatically has

\[
   A_i\cup\cdots\cup A_{j+d}=U(i,j),                                \tag{6.4}
\]

and `U` satisfies the diamond rule

\[
   U(i,j)=U(i,j-1)\cup U(i+1,j).                                    \tag{6.5}
\]

Thus upper shadows and upper pinning are the same object: once their assigned
cell labels agree with (6.3), they impose no additional coordinate-pinning
constraints.

Indeed, an upper interval negative in `b` is a union of negative central
windows and is already forbidden by them.  An upper interval positive in `b`
contains a positive central window and therefore contains its pin.

Now assign lower masks `S` to intervals `J_S` of length at most `d`.  The only
new effect is deletion from the central envelopes.  Put

\[
 Z_b'=\{j:b\in E_j\}\setminus
       \bigcup_{S:\,b\notin S}J_S.                                  \tag{6.6}
\]

### Theorem 11 (exact fixed-delay lower gate)

Assume the run condition and assign every desired upper label according to
(6.3).  A factor realizing the lower, central, and upper assignments exists
if and only if

\[
   J_S\cap Z_b'\ne\varnothing
   \quad(S\text{ lower},\ b\in S),                                  \tag{6.7}
\]

and

\[
   [i,i+d]\cap Z_b'\ne\varnothing
   \quad(b\in T_i).                                                  \tag{6.8}
\]

When these hold, putting `b` at every position of `Z_b'` gives a factor.

#### Proof

Central negative intervals are already accounted for in `E`; lower negative
intervals delete exactly the second term of (6.6).  Conditions (6.7) and
(6.8) are respectively the positive lower and positive central clean-cut
conditions.  The preceding observation makes every upper condition
redundant.  Theorem 1 then proves necessity and sufficiency.  QED.

This separates the construction task sharply:

* the upper half is the join growth diagram of `T`;
* the lower half is a short-strip growth-diagram/pin-survival completion.

## 7. Where the rank-slack formula comes from

Fix rank `r`, put

\[
   M=\binom{k}{r},\qquad
   L=\sum_{s=1}^{r-1}\binom{k}{s},\qquad n=M+d.                      \tag{7.1}
\]

Choose one interval for each rank-`r` mask and order them by left endpoint:

\[
   I_i=[p_i,q_i],\qquad 1\le i\le M.
\]

Equal-rank incomparability makes both endpoint sequences strictly increasing.
Since each is an `M`-subset of `[M+d]`,

\[
   i\le p_i\le q_i\le i+d.                                         \tag{7.2}
\]

Consequently, every physical interval of length at least `d+1` contains a
selected rank-`r` interval, and therefore has rank at least `r`.  Every lower
mask must occupy an interval of length at most `d`.

The short triangular strip contains exactly

\[
\begin{aligned}
 C_d(n)
 &=\sum_{h=1}^d(n-h+1)\\
 &=dn-\binom d2\\
 &=dM+\binom{d+1}{2}.                                                \tag{7.3}
\end{aligned}
\]

cells.  Hence

\[
   L\le dM+\binom{d+1}{2}.                                          \tag{7.4}
\]

The least possible delay is exactly

\[
 \tau_{k,r}=\min\left\{d\ge0:
 L\le dM+\binom{d+1}{2}\right\},                                   \tag{7.5}
\]

which is the rank-slack term in `B(k)`.

In the ordered-chain language, the `M` masks of rank `r` occupy `M` distinct
left chains and `M` distinct right chains.  Thus `d` left chains and `d` right
chains skip rank `r`; these are precisely the blank-chain slack that permits
the band displacement (7.2).  The arithmetic residual

\[
   \sigma_{k,r}(d)=dM+\binom{d+1}{2}-L                              \tag{7.6}
\]

is the number of short cells left after placing all lower masks.

This gives a more precise meaning to the conjecture `nu(k)=B(k)`: at a
maximizing rank, order the two orthogonal chain decompositions using exactly
`d=tau_{k,r}` blank chains, inject all lower masks into the short strip, and
use the `sigma` remaining short cells as growth-diagram completion cells.
Pin survival is exactly the assertion that these blank cells can be filled so
that the local join diamonds close.

When `sigma=0`, there is no freedom: every short interval has a different
lower-mask label, and all local diamond identities are forced.  When
`sigma>0`, the blank cells are not mere counting waste; they are the only
local absorbers available to repair incompatible zero barriers.

For the current `k=14,r=7,d=2` target,

\[
 M=3432,\qquad L=6475,\qquad C_2(M+2)=6867,
\]

so `sigma=392`.  This is exactly the previously observed count of unused
singleton/pair slots.  The equality is structural, not accidental.

## 8. Consequences for the all-`k` program

The pinning part of the global construction can now be stated without SAT
terminology.

1. Order a known orthogonal pair of chain decompositions in the triangular
   band allowed by `d=tau_{k,r}`.
2. For each coordinate, compute the row switches `a_p(b),c_p(b)`.
3. The order is pinnable exactly when every transition interval reaches a
   clean diagonal cut, or equivalently when no negative bridge from Theorem 4
   covers it.
4. If feasible, Corollary 3 gives canonical minimum-occurrence coordinate
   pins.
5. A sufficient wholly local construction theorem would be to arrange
   containment monotonicity and negative-hull closure, or more flexibly to
   complete the `sigma` blank band cells to the join growth diagram of
   Theorem 7.

The main unresolved mathematical statement is therefore not abstract
orthogonality.  It is an **ordered growth-diagram completion theorem**:

> Can a known orthogonal symmetric-chain pair, after adding exactly the
> rank-slack blank chains, be triangularly ordered so that every coordinate's
> zero cells admit no negative bridge across a positive transition (equivalently,
> so that the partial cell labels extend to a Boolean join growth diagram)?

Theorems 1--11 give several equivalent forms in which to attack that question:
clean diagonal cuts, row-switch inequalities, forbidden monotone bridges,
pairwise hull closure, and local Boolean diamonds.
