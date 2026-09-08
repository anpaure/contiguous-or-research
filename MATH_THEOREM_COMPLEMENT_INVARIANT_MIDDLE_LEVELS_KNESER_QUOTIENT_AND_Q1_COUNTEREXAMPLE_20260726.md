# Complement-invariant Middle Levels cycles: dihedral action, Kneser quotient, and the depth-one colour counterexample

Date: 2026-07-26

Method: pure mathematics.  The finite examples below are complete symbolic
certificates; their verification uses only the displayed set identities.

## 0. Verdict

Let

\[
 \Omega=[2m+1],\qquad
 W=\binom{2m+1}{m},
\]

and let `ML_m` be the subgraph of the Boolean cube induced by ranks `m`
and `m+1`.  Write `c(S)=\Omega\setminus S`.

The exact conclusions are as follows.

1. If a Hamilton cycle of `ML_m` is invariant under plain complement,
   complement cannot act as a reflection.  It fixes neither a Middle
   Levels vertex nor a Middle Levels edge setwise.  Therefore it acts as
   the half-turn of the abstract cycle.
2. The half-turn advances by `W` edges and must interchange the two
   shores.  Consequently `W` is odd, equivalently

   \[
                              m=2^a-1.                         \tag{0.1}
   \]

3. In the surviving parity case, complement-invariant Hamilton cycles of
   `ML_m` are exactly lifts of Hamilton cycles of the odd Kneser graph

   \[
                              KG(2m+1,m).                      \tag{0.2}
   \]

4. For the rank-`m` Johnson projection, complement does **not** pair its
   rank-`(m-1)` intersection colours with its rank-`(m+1)` union colours.
   It pairs those intersections with the rank-`(m+2)` unions of the
   opposite-shore Johnson projection.  This is an off-diagonal duality,
   not a two-sided-rainbow theorem for one owner cycle.
5. Literal two-sided rainbowness of the full projected Hamilton cycle is
   already cardinality-impossible: it has `W` edges but only

   \[
       N_-=\binom{2m+1}{m-1}=\frac{m}{m+2}W<W                 \tag{0.3}
   \]

   lower colours.
6. Even the weaker, coefficient-one relevant assertion that every lower
   colour must occur is false.  An explicit complement-invariant Hamilton
   cycle of `ML_3` is given in Section 6; its projected cycle never uses
   the lower colour `36`, while `27` and `34` each occur three times.

Thus plain complement symmetry neither proves nor forces a doubly-rainbow
depth-one cycle.  It is compatible with a best-possible `1/2` lower load
ledger in a different `m=3` example (Section 7), so the obstruction is not
that symmetry forbids balance.  The choice of the Kneser quotient cycle,
not complement symmetry, decides the missing lower shadow.

## 1. Middle Levels chronology and its two Johnson projections

Let a Hamilton cycle be written

\[
 X_0,Y_0,X_1,Y_1,\ldots,X_{W-1},Y_{W-1},X_0,                \tag{1.1}
\]

where

\[
 |X_i|=m,\qquad |Y_i|=m+1,\qquad
 X_i\subset Y_i\supset X_{i+1}.                              \tag{1.2}
\]

All subscripts in this note are cyclic.  The two rank-`m` neighbours of
`Y_i` are distinct facets of it, and hence

\[
 Y_i=X_i\cup X_{i+1},\qquad
 L_i:=X_i\cap X_{i+1}\in\binom\Omega{m-1}.                  \tag{1.3}
\]

Thus `X_0,...,X_{W-1}` is a Hamilton cycle of `J(2m+1,m)`.  Its edge
intersection and edge-union colours are

\[
 I_i^X=X_i\cap X_{i+1}=L_i,
 \qquad
 U_i^X=X_i\cup X_{i+1}=Y_i.                                 \tag{1.4}
\]

Because (1.1) uses every upper vertex, the `U_i^X` are all the members of
`\binom\Omega{m+1}`, exactly once.  Nothing in Hamiltonicity alone controls
the multiplicities of the `I_i^X`.

There is simultaneously an opposite-shore Johnson cycle

\[
 Y_0,Y_1,\ldots,Y_{W-1},Y_0                                  \tag{1.5}
\]

in `J(2m+1,m+1)`.  Its colours are

\[
 I_i^Y=Y_i\cap Y_{i+1}=X_{i+1},
 \qquad
 U_i^Y=Y_i\cup Y_{i+1}\in\binom\Omega{m+2}.                \tag{1.6}
\]

The distinction between (1.4) and (1.6) is essential below.

## 2. Exact dihedral classification

### Theorem 2.1 (plain complement is necessarily the half-turn)

Assume `m>=1` and that the edge set of the Hamilton cycle (1.1) is
invariant under `c`.  Then complement acts on the abstract cycle
`C_{2W}` as its half-turn.  In particular `W` is odd.

#### Proof

Complement fixes no vertex because it exchanges ranks `m` and `m+1`.
It also fixes no Middle Levels edge setwise.  Indeed, if an unordered edge
`{A,B}` were fixed, rank considerations would force

\[
                              B=A^c.                           \tag{2.1}
\]

But `A` and `A^c` differ in all `2m+1>1` coordinates, whereas a Middle
Levels edge changes one coordinate.

A nonidentity involutive automorphism of an even abstract cycle is one of:

* the half-turn;
* a reflection through two opposite vertices; or
* a reflection through two opposite edges.

The vertex-axis reflection is impossible because it fixes two vertices.
The edge-axis reflection is impossible because it fixes two unordered
cycle edges setwise, contradicting (2.1).  Only the half-turn remains.

The half-turn of `C_{2W}` advances by `W` edges.  Complement exchanges the
two ranks, so this advance must reverse parity in the alternating listing
(1.1).  Hence `W` is odd. `\square`

Equivalently, if `\sigma` is the oriented successor map of (1.1), then

\[
                              c=\sigma^W,
 \qquad c\sigma=\sigma c.                                    \tag{2.2}
\]

A reflection would instead satisfy `c\sigma c=\sigma^{-1}`.  That second
index law is not physically available for plain complement.

This does not rule out reflections for a different involution such as
coordinate-reversal composed with complement: such an involution may fix a
Middle Levels edge.  Reverse-complement symmetry must therefore not be
reported as plain-complement symmetry.

### Corollary 2.2 (Mersenne parity gate)

A plain-complement-invariant Hamilton cycle can exist only when

\[
                              m=2^a-1.                         \tag{2.3}
\]

#### Proof

Kummer's parity criterion gives

\[
 \binom{2m+1}{m}\equiv1\pmod2
 \quad\Longleftrightarrow\quad
 m\mathbin{\&}(m+1)=0.                                      \tag{2.4}
\]

Two consecutive positive integers have disjoint binary supports exactly
when the smaller is a string of ones.  This is (2.3). `\square`

The corollary is a necessary condition, not an assertion here that every
Mersenne parameter has such a cycle.

## 3. Exact Kneser quotient normal form

Let `\mathcal O` be the set of complement orbits on the vertices of
`ML_m`.  Every orbit has the form

\[
                              [A]=\{A,A^c\},
 \qquad A\in\binom\Omega m.                                  \tag{3.1}
\]

Two such orbits are joined by a Middle Levels edge precisely when their
rank-`m` representatives are disjoint:

\[
 A\subset B^c
 \quad\Longleftrightarrow\quad A\cap B=\varnothing.          \tag{3.2}
\]

Hence the orbit graph is exactly `KG(2m+1,m)`.

### Theorem 3.1 (quotient/lift bijection)

Suppose `W` is odd.  Plain-complement-invariant Hamilton cycles of `ML_m`,
up to the choice of a starting point and orientation, correspond to
Hamilton cycles

\[
 A_0,A_1,\ldots,A_{W-1},A_0                                  \tag{3.3}
\]

of `KG(2m+1,m)`.

Given (3.3), the lifted chronology is

\[
 V_j=
 \begin{cases}
 A_j,&j\text{ even},\\
 A_j^c,&j\text{ odd},
 \end{cases}
 \quad(0\le j<W),
 \qquad
 V_{j+W}=V_j^c.                                               \tag{3.4}
\]

#### Proof

For an invariant Middle Levels cycle, Theorem 2.1 says that its first `W`
vertices contain exactly one vertex from every complement orbit.  Replacing
each by the rank-`m` representative gives all `W` members of
`\binom\Omega m` once.  Consecutive orbit representatives are disjoint by
(3.2), including the seam between positions `W-1` and `0`.  This gives
(3.3).

Conversely, consecutive `A_j,A_{j+1}` in (3.3) are disjoint, so the
alternating sets in (3.4) are adjacent in `ML_m`.  Since `W` is odd,
`W-1` is even; the first seam is

\[
                              A_{W-1}\ --\ A_0^c,             \tag{3.5}
\]

which is an edge by disjointness.  Complementing gives all edges in the
second half and the closing seam.  The first half uses one vertex from
each of the `W` complement orbits and the second half uses the other one,
so (3.4) visits all `2W` vertices exactly once. `\square`

The quotient is therefore an odd Kneser cycle, not a complement-invariant
Johnson cycle on the same shore.  Complement acts trivially on quotient
orbits; it is the half-turn only after the two-sheeted lift (3.4).

## 4. Exact half-turn indices and colour coupling

Write

\[
                              W=2h+1.                          \tag{4.1}
\]

In the chronology (1.1), the half-turn identities are

\[
                              X_i^c=Y_{i+h},
 \qquad                       Y_i^c=X_{i+h+1}.                 \tag{4.2}
\]

The one-index stagger in (4.2) is forced by the odd half-length.  In
particular there is no meaningful same-shore formula
`X_{i+W/2}=X_i^c`.

Complement maps the `i`-th edge of the `X`-projection to the
`(i+h)`-th edge of the `Y`-projection.  De Morgan's laws and (4.2) give
the exact colour identities

\[
 \boxed{(I_i^X)^c=U_{i+h}^Y},
 \qquad
 \boxed{(U_i^X)^c=I_{i+h}^Y}.                                \tag{4.3}
\]

Indeed,

\[
 (X_i\cap X_{i+1})^c
 =Y_{i+h}\cup Y_{i+h+1},                                    \tag{4.4}
\]

while

\[
 (X_i\cup X_{i+1})^c
 =Y_i^c
 =X_{i+h+1}
 =Y_{i+h}\cap Y_{i+h+1}.                                    \tag{4.5}
\]

Consequently the only nontrivial multiplicity identity is

\[
 \#\{i:I_i^X=S\}
 =\#\{i:U_i^Y=S^c\}
 \qquad(S\in\tbinom\Omega{m-1}).                            \tag{4.6}
\]

There is no identity between the multiplicity of `S` among `I_i^X` and
the multiplicity of any rank-`(m+1)` colour among `U_i^X`.  The latter
multiset is already exactly the full upper layer, independently of
complement.

The Kneser normal form makes the same fact especially transparent.  In
the lift (3.4), the lower and upper vertices in (1.1) are

\[
 X_t=A_{2t},
 \qquad
 Y_t=A_{2t+1}^c,                                              \tag{4.7}
\]

with indices modulo `W`.  Since multiplication by two is a permutation
modulo odd `W`, both sequences visit their full shores.  Moreover

\[
 \begin{aligned}
 U_t^X&=X_t\cup X_{t+1}=A_{2t+1}^c,\\
 I_t^X&=X_t\cap X_{t+1}=A_{2t}\cap A_{2t+2}.
 \end{aligned}                                                \tag{4.8}
\]

If

\[
                              C_j=A_{j-1}\cap A_{j+1},        \tag{4.9}
\]

then

\[
                              I_t^X=C_{2t+1}.                 \tag{4.10}
\]

Thus the missing lower-shadow problem is exactly the length-two overlap
ledger of the chosen Hamilton cycle in the Kneser quotient.  Complement
places no further restriction on this ledger.

## 5. What “doubly rainbow” can and cannot mean here

The projected Johnson Hamilton cycle has `W` edges.  Its union colours
are all `W` members of `\binom\Omega{m+1}`, once each.  There are only
`N_-` lower colours as in (0.3).  Hence its lower colours cannot be
pairwise distinct.  Literal two-sided rainbowness of the **full** Hamilton
projection is impossible before symmetry is considered.

For `m>=2`, the strongest natural full-cycle depth-one target is instead:

* every lower colour occurs; and
* every lower load is one or two.

If this holds, exactly

\[
                              W-N_-=\frac{2W}{m+2}             \tag{5.1}
\]

lower colours have load two.  This is the best possible lower ledger and
is asymptotically coefficient one.  Section 6 shows that complement does
not force even the first bullet.

This odd-ground statement must not be conflated with an even-ground
cycle in `J(2m,m)`.  On even ground complement preserves the owner rank
and directly exchanges the rank-`(m-1)` and rank-`(m+1)` edge colours of
one complement-invariant Johnson cycle.  On the odd ground here,
complement exchanges owner shores, and (4.3), rather than same-cycle
duality, is the correct identity.

## 6. Exact `m=3` counterexample: complement symmetry with a lower hole

Take `\Omega=[7]`.  The following cyclic list contains all `35` triples
exactly once, and every two consecutive triples are disjoint, including
the last and first:

\[
\begin{array}{c|rrrrrrrrrrrr}
j&0&1&2&3&4&5&6&7&8&9&10&11\\ \hline
A_j&123&467&125&367&145&267&135&247&356&124&567&134
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrrrr}
j&12&13&14&15&16&17&18&19&20&21&22&23\\ \hline
A_j&257&346&127&456&237&146&235&147&236&157&246&357
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrrr}
j&24&25&26&27&28&29&30&31&32&33&34\\ \hline
A_j&126&345&167&234&156&347&256&137&245&136&457
\end{array}                                                   \tag{6.1}
\]

Here, for example, `123` denotes `{1,2,3}`.  Thus (6.1) is a Hamilton
cycle of `KG(7,3)`.  Applying (3.4) gives an exact complement-invariant
Hamilton cycle of `ML_3`; this formula is the full `70`-vertex chronology,
not merely a quotient certificate.

For direct verification of the projected colour ledger, its lower owner
chronology `X_t=A_{2t}` is

\[
\begin{split}
&123,125,145,135,356,567,257,127,237,235,236,246,126,167,156,\\
&256,245,457,467,367,267,247,124,134,346,456,146,147,157,357,\\
&345,234,347,137,136.
\end{split}                                                   \tag{6.2}
\]

The consecutive intersections in this exact cyclic order are

\[
\begin{split}
&12,15,15,35,56,57,27,27,23,23,26,26,16,16,56,25,45,47,\\
&67,67,27,24,14,34,46,46,14,17,57,35,34,34,37,13,13.
\end{split}                                                   \tag{6.3}
\]

Their complete multiplicity table is

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrrrrr}
S&12&13&14&15&16&17&23&24&25&26&27&34&35&36&37&45&46&47&56&57&67\\ \hline
\mu(S)&1&2&2&2&2&1&2&1&1&2&3&3&2&0&1&1&2&1&2&2&2.
\end{array}                                                   \tag{6.4}
\]

In particular `36` is absent, while `27` and `34` occur three times.
Every projected union colour is nevertheless present exactly once by
(4.8).  This is a direct counterexample to each assertion that plain
complement invariance forces lower saturation, forces `1/2` lower loads,
or forces a two-sided-rainbow depth-one projection.

No computational premise is hidden in the certificate: the claims needed
for Hamiltonicity are exactly that (6.1) lists `\binom73=35` distinct
triples and that consecutive entries are disjoint; the colour claim is
the displayed intersection list (6.3).

## 7. Symmetry permits, but does not cause, the optimal lower ledger

For completeness, complement symmetry itself is not an obstruction to the
best possible full-cycle lower ledger at `m=3`.  The following is another
cyclic Hamilton cycle of `KG(7,3)`:

\[
\begin{split}
&123,467,125,367,145,267,135,247,136,245,167,345,127,456,237,\\
&146,235,147,356,124,567,234,156,347,126,357,246,137,256,134,\\
&257,346,157,236,457.
\end{split}                                                   \tag{7.1}
\]

Again all consecutive entries, including the wrap, are disjoint.  Its
length-two overlap multiplicities are

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrrrrr}
S&12&13&14&15&16&17&23&24&25&26&27&34&35&36&37&45&46&47&56&57&67\\ \hline
\mu(S)&1&2&2&2&2&1&2&2&1&2&2&2&1&1&2&2&1&1&2&2&2.
\end{array}                                                   \tag{7.2}
\]

Thus all `21` lower colours occur, seven once and fourteen twice, exactly
as forced by (5.1).  Lifting (7.1) by (3.4) yields a complement-invariant
Middle Levels Hamilton cycle with optimal lower saturation and exact upper
rainbowness.

Equations (6.4) and (7.2) settle the logical question sharply: complement
symmetry allows both behaviours.  It supplies the Kneser quotient and the
off-diagonal identities (4.3), but it does not select a quotient Hamilton
cycle with any prescribed length-two overlap ledger.

The good ledger (7.2) is still not a literal two-sided-rainbow Hamilton
cycle, because fourteen lower colours necessarily repeat.  Nor does
choosing one edge of each lower colour automatically leave a cycle.  Any
shorter exact two-sided-rainbow core still needs a separate chronological
selection theorem.

## 8. Consequence for the coefficient-one route

Plain complement symmetry pays only the following exact items:

* a two-sheeted half-turn lift;
* the Mersenne parity gate;
* an odd-Kneser Hamilton quotient; and
* the cross-shore colour dualities (4.3).

It does not pay lower-shadow coverage of the rank-`m` Johnson projection.
That remaining task is precisely a constraint on

\[
                 \{A_{j-1}\cap A_{j+1}:0\le j<W\}            \tag{8.1}
\]

inside a Hamilton cycle of `KG(2m+1,m)`.  Any constant-one argument using
Middle Levels complement symmetry must therefore prove an additional
balanced length-two-overlap theorem for the Kneser quotient (or introduce
an independent repair).  A half-turn or reflection slogan cannot replace
that theorem.
