# K17 PBBS-U singleton absorption and the exact alternating-girth-five gate

## 0. Scope

This note concerns only the authenticated PBBS-U fragment atlas

`scratch/k17_pbbs_u_deadport_absorbed_20260731.fragments`

and its explicit singleton-absorbed child

`scratch/k17_pbbs_u_singleton_absorbed_20260731.fragments`.

It also concerns one fixed, independently decoded disconnected degree cover of
the child: a path on 551 fragments and cycles of sizes

\[
                 91,43,22,9,8,8,4.                 \tag{0.1}
\]

There is no Hamilton-path assertion and no unrestricted K17 assertion here.

## 1. The singleton absorption

In the parent atlas the three participating fragments are

\[
\begin{aligned}
L&=(1e5b,1d5b,395b,3b5a,735a,7752,6772,6676),\\
S&=(667a),\\
R&=(663b,467b,06fb,0efa,1ef2,3ee2,7ec2,7e86,7c8e,
      789e,70be,62be,46be,4ebc).
\end{aligned}                                      \tag{1.1}
\]

Split `L` after `p=0x6772`, retain the suffix `(0x6676)`, and replace the
other three fragments by

\[
 (1e5b,1d5b,395b,3b5a,735a,7752,
   6772,667a,663b,467b,\ldots,4ebc).                \tag{1.2}
\]

### Theorem 1.1 (lossless singleton absorption)

The operation (1.2) preserves the 5,005-cell rank-nine partition, Johnson
adjacency, intersection-colour simplicity, residence, and all upper interval
targets.  It reduces the fragment count from 737 to 736.

#### Proof

The two new Johnson differences and colours are

\[
\begin{array}{c|c|c}
\text{edge}&\text{XOR}&\text{intersection}\cr
6772\!\to\!667a&0108&6672\cr
667a\!\to\!663b&0041&663a.
\end{array}                                        \tag{1.3}
\]

Both XORs have weight two.  Cutting `6772 -> 6676` removes colour `6672`,
and the first new edge restores it.  Colour `663a` was not internal in the
parent.  Thus the new internal-colour set is exactly

\[
             C_{\rm new}=C_{\rm old}\cup\{663a\},
             \qquad |C_{\rm old}|=4268,\quad |C_{\rm new}|=4269.       \tag{1.4}
\]

This is precisely why the old bottleneck disappears: both exposed ports of
the singleton previously had only colour-`663a` seams, whereas (1.2) consumes
that colour once as an internal edge and removes the singleton's two exposed
ports.

Every old fragment is unchanged or split, so only windows crossing a new edge
need a residence check.  The complete length-four collar is contained in

\[
 (735a,7752,6772,667a,663b,467b,06fb),              \tag{1.5}
\]

whose fifteen bit traces contain neither `010` nor `0110`.

The only old upper witnesses which can be destroyed cross the cut
`6772 | 6676`.  Their five distinct OR values are

\[
             6776,\quad7776,\quad777e,\quad7f7e,\quad7f7f.              \tag{1.6}
\]

They retain the following unaffected witnesses in the child, using
zero-based `(fragment,start,end)` coordinates:

\[
\begin{array}{c|c|l}
6776&(221,11,12)&6376,6766\cr
7776&(101,4,6)&5736,7734,7674\cr
777e&(116,10,14)&573a,567a,367a,7672,7666\cr
7f7e&(39,4,8)&0f7a,1f72,3f62,7f42,7e46\cr
7f7f&(7,0,6)&6e59,6d59,6b59,4b5b,5b53,1b57,1a77.
\end{array}                                        \tag{1.7}
\]

All other old interval witnesses lie wholly inside an unchanged piece.
Equations (1.3)--(1.7), together with the literal component-multiset replay,
prove the theorem.  \(\square\)

## 2. Alternating exchanges in the decoded cover

Represent every selected seam by an edge of a matching `M` on oriented
fragment ports.  A legal unused seam joining ports `p,q` gives the transition

\[
                  p\longmapsto M(q).                \tag{2.1}
\]

Deleting `k` selected seams and inserting `k` seams while preserving the two
unmatched ports is therefore a simple
`M`-alternating cycle of length `2k`; after contracting selected seams, it is
a simple closure of length `k` under (2.1).  This is the standard exact
port-matching normal form for a `k`-edge exchange.  It already includes
reversal of every opened segment.

This endpoint convention loses no exchanges in the present atlas.  The two
unmatched ports `(596,1)` and `(731,0)` both have degree zero in the complete
6,521-edge oriented-port seam quotient.  Hence an endpoint-changing
alternating path cannot exist.

The four-fragment target cycle is

\[
 ((81,0),(179,0),(567,1),(225,0)),                  \tag{2.2}
\]

with selected physical port seams

\[
\begin{array}{c|c}
(163,358)&1373\cr
(359,1135)&2177\cr
(1134,450)&0dd9\cr
(451,162)&5179.
\end{array}                                        \tag{2.3}
\]

The exact directed-state seam catalogue has 9,188 arcs.  After identifying
opposite directed descriptions, and using the singleton orientation quotient
of this decoded cover, it has 6,521 oriented-port seam pairs.

### Theorem 2.1 (alternating girth five)

No exchange deleting at most four selected seams can touch the cycle (2.2).
In particular every two-edge splice and every three-edge/3-opt normal form is
impossible even before colour simplicity, the residence DFA, or component
connectivity is imposed.

The bound is sharp at the port-incidence level: the first simple alternating
closures have length five.

#### Proof

Start (2.1) at either endpoint of each seam in (2.3), never revisiting a
contracted selected seam.  The complete rooted closure census is

\[
\begin{array}{c|rrrrrrrr|r}
\text{start port}&163&358&359&1135&1134&450&451&162&\text{total}\cr
k=2&0&0&0&0&0&0&0&0&0\cr
k=3&0&0&0&0&0&0&0&0&0\cr
k=4&0&0&0&0&0&0&0&0&0\cr
k=5&10&10&2&2&0&0&8&8&40.
\end{array}                                        \tag{2.4}
\]

Reversal and change of the root identify the forty oriented rows into
eighteen physical alternating cycles.  Equation (2.4) is a direct adjacency
replay of (2.1), not a SAT result.  Together with the two zero endpoint
degrees, it proves the lower bound for every exchange and its sharpness.
\(\square\)

## 3. The unique literal-safe rainbow length-five exchange

Of the eighteen length-five physical closures, exactly two obey global seam
colour simplicity.  Exactly one of those two also passes complete linear and
cyclic residence replay.

It deletes

\[
\begin{array}{c|c}
(163,358)&1373\cr
(435,314)&5372\cr
(538,752)&4376\cr
(113,1136)&2736\cr
(359,1135)&2177
\end{array}                                        \tag{3.1}
\]

and inserts

\[
\begin{array}{c|c}
(163,435)&5372\cr
(314,752)&4b72\cr
(538,113)&4736\cr
(1136,359)&2376\cr
(1135,358)&3173.
\end{array}                                        \tag{3.2}
\]

Literal replay of (3.1)--(3.2) gives the same two dead ports as before,

\[
                    (596,1),\quad(731,0),            \tag{3.3}
\]

a path on 279 fragments, and resident cycles of sizes

\[
                    367,43,22,9,8,8.                 \tag{3.4}
\]

All 735 selected seam colours remain distinct and disjoint from the 4,269
internal colours.  Thus this is an exact residence-safe bridge reducing the
cycle count from seven to six.  It is not a Hamilton path and does not improve
the longest-path count.

### Corollary 3.1 (rooted alternating-girth gate)

For any decoded physical-port degree cover with forced degree-zero endpoints,
contract its selected matching edges and direct each legal unused seam by

\[
                       p\longmapsto M(q).
\]

For a subtour `T`, let `g(T)` be the shortest simple directed closure rooted
at a selected edge of `T`.  Every endpoint-preserving seam toggle which
touches `T` deletes at least `g(T)` selected seams.  Filtering the closures of
length `g(T)` first by the partition matroid on seam colours and then by full
linear/cyclic DFA replay is exact.

This gives a proof-safe subtour score:

1. maximize the minimum rooted alternating girth only after confirming that
   at least one shortest closure is rainbow and DFA-safe;
2. prefer a closure reducing the number of components of the degree cover;
3. use current main-path length only as a later tie-breaker.

The order matters here: the unique safe shortest closure decreases the cycle
count but shortens the displayed path from 551 to 279 components.  A
longest-path-only heuristic would reject the only minimal exact escape.

## 4. Authentication

Primary audit:

`scratch/audit_k17_pbbs_u_singleton_absorption_c6_girth5_20260731.py`

SHA-256
`7a0d9d1d70e2dc82a3b5ee5e9a1fdf9ec2cd66310556679f300ad216a64e4ba9`.

Audit JSON:

`scratch/k17_pbbs_u_singleton_absorption_c6_girth5_20260731.audit.json`

SHA-256
`0470ff016bbadf7a44d3a692a13f690c080bcf48f5616bdf7bc235ca8f6f6319`,
payload SHA-256
`708aa2dea0baf9882c1e0d7a11225879cf860eba36f1bf2193ca22feab763df5`.

The authenticated inputs are:

* parent atlas SHA-256
  `0bcd678828c8d258b6976aa2831a250dd3650c395bf9d3864df1415ee5961a6b`;
* singleton-absorbed atlas SHA-256
  `3b1a277fa10d2152a9f0d217fa9ff47c0a1ce3ca648321f9ac65af289d87e465`;
* decoded cover SHA-256
  `da350de3a8c5e78d3b791d0d74cc76610b5eeaae79355e8f79844f2af6ddef6c`.

No handoff or research-index entry is made by this note's audit lane.
