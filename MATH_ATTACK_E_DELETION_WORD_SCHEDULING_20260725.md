# Deletion-word scheduling and cyclic packetization

Date: 2026-07-25  
Line: E — cyclic synchronization by deletion-word scheduling

## Verdict

This route does **not** prove the contiguous-OR width conjecture, nor the
strong labelled common-owner synchronization theorem.

It does give three exact advances.

1. There is a necessary-and-sufficient packetization theorem for truncated
   deletion words.  Besides the visible successor identities, it contains an
   unavoidable length-`m` **coordinate-residence law**.
2. A locally compatible cyclic schedule is exactly an arrival-to-departure
   matching.  Ordinary Hall, even in radius-one departure intervals, does not
   force residence length `m`.
3. For every `m>=10` and every `1<=K<=m-1`, there is an explicit protected
   two-cycle word system which has the correct cycle length, rainbow first
   labels, exact two-packet point margins at every depth, exact deletion-position
   margins, all consecutive-block stationarity laws, and a unique local
   successor cover, but neither cycle is a wreath packet.

There is also a clean positive theorem: a shadow-clean cyclic schedule with
total residence defect `o(W/sqrt(m))` gives the desired `o(W)` labelled loss on
the window `K<=A sqrt(m)`.  The unproved replacement lemma at the end asks for
exactly such a schedule.  This is a strictly stronger labelled sufficient
statement; no equivalence with the unlabelled overload problem is claimed.

## 1. Setup and notation

Put

\[
 n=2m+1,\qquad \Omega=\binom{[n]}m,\qquad
 W=|\Omega|,\qquad B=\frac Wn.
\]

For `q>=1`, also put

\[
 N_q=\binom n{m-q},\qquad c_q=\left\lfloor\frac W{N_q}\right\rfloor.
\tag{1.0}
\]

Let

\[
 P_0(X)=X\supset P_1(X)\supset\cdots\supset P_K(X)
 \qquad (X\in\Omega)
\]

be one integral common nested resolution.  Its labelled deletion prefix is

\[
 d_t(X)=P_{t-1}(X)\setminus P_t(X),\qquad 1\le t\le K.
\tag{1.1}
\]

Thus the `d_t(X)` are distinct members of `X`.  The fiber-balance assumptions
on the maps `P_q` mean that every rank-`(m-q)` target has `c_q` or `c_q+1`
owners.  They are retained throughout, although the structural theorems below
apply to any labelled nested flags.

For a proposed successor permutation `sigma` of the owners, write

\[
 \ell(X)=d_1(X).
\tag{1.2}
\]

The orientation convention is that `sigma X` is the next middle owner.  In a
genuine row, `ell(sigma X)` is the coordinate which enters the next middle
window.

For an oriented exact factor `F`, let `L_q^F(X)` be its canonical lower state
owned by `X`, and put

\[
 e_q(F,P)=|\{X\in\Omega:P_q(X)\ne L_q^F(X)\}|.
\tag{1.3}
\]

## 2. Exact packetization theorem

### Theorem 2.1 (exact truncated-word packet criterion)

The flags `P_0,...,P_K` are exactly the first `K` canonical lower levels of
one oriented exact middle wreath factor if and only if there is a permutation
`sigma` of `Omega` with the following properties.

1. Every orbit of `sigma` has length `n`.
2. On every orbit, `ell` is a bijection onto `[n]`.
3. Every owner obeys the length-`m` residence identity

   \[
   X=\{\ell(X),\ell(\sigma^{-1}X),\ldots,
           \ell(\sigma^{-(m-1)}X)\}.
   \tag{2.1}
   \]

4. The visible deletion prefix obeys

   \[
   d_t(X)=\ell(\sigma^{-(t-1)}X),
   \qquad 1\le t\le K.
   \tag{2.2}
   \]

In particular, exact packetization is not characterized by the `K-1`
one-step overlap identities alone when `K<m`.

#### Proof

First suppose an oriented factor is given.  On one row choose a cyclic
coordinate order `z_0,...,z_{n-1}` and write its middle owners as

\[
 X_j=\{z_j,z_{j+1},\ldots,z_{j+m-1}\}.
\]

Let `sigma X_j=X_{j+1}`.  Its first canonical deletion is
`ell(X_j)=z_{j+m-1}`.  Hence `ell` runs through all coordinates once on the
row,

\[
 \{\ell(X_j),\ell(X_{j-1}),\ldots,\ell(X_{j-m+1})\}
 =\{z_j,\ldots,z_{j+m-1}\}=X_j,
\]

and

\[
 d_t(X_j)=z_{j+m-t}=\ell(X_{j-t+1}).
\]

This proves necessity.

Conversely, enumerate a `sigma`-orbit as `X_j=sigma^jX_0`, with indices in
`Z_n`, and define

\[
 z_{j+m-1}=\ell(X_j).
\tag{2.3}
\]

Property 2 makes `z_0,...,z_{n-1}` a cyclic permutation of `[n]`.  Property
3 gives

\[
 X_j=\{z_j,z_{j+1},\ldots,z_{j+m-1}\},
\]

and property 4 gives

\[
 d_t(X_j)=z_{j+m-t}.
\]

Thus this orbit is an oriented wreath row with precisely the prescribed
flags through depth `K`.  The `sigma`-orbits partition `Omega`, so all rows
together are an exact factor.  QED.

The new clause is (2.1).  It is invisible in a prefix of length `K<m`: a
coordinate can obey every displayed shift identity and nevertheless remain
in the middle owners for `m-1` or `m+1` steps instead of `m`.

## 3. Arrival-departure normal form

Fix one proposed orbit of length `n`, written

\[
 X_j\quad(j\in\mathbb Z_n),
\]

and put `g_j=d_1(X_j)`.  Assume

\[
 j\longmapsto g_j
\quad\hbox{is a bijection onto }[n]
\tag{3.1}
\]

and

\[
 X_j\setminus X_{j-1}=\{g_j\}.
\tag{3.2}
\]

Thus coordinate `g_j` arrives at transition `j`.

### Theorem 3.1 (exact residence classification)

Under (3.1)-(3.2), there are unique integers

\[
 1\le r_i\le n-1
\]

such that

\[
 g_i\in X_j
 \quad\Longleftrightarrow\quad
 j\in\{i,i+1,\ldots,i+r_i-1\}\pmod n.
\tag{3.3}
\]

The departure map

\[
 \tau(i)=i+r_i\pmod n
\tag{3.4}
\]

is a permutation of `Z_n`, and

\[
 \sum_{i\in\mathbb Z_n}r_i=nm.
\tag{3.5}
\]

Conversely, suppose integers `r_i` in `[1,n-1]` satisfy (3.5) and the map
(3.4) is a permutation.  Defining

\[
 X_j=\{g_i: j-i\pmod n\in\{0,1,\ldots,r_i-1\}\}
\tag{3.6}
\]

produces `m`-sets satisfying (3.2).  The truncated words

\[
 d_t(X_j)=g_{j-t+1},\qquad 1\le t\le K,
\tag{3.7}
\]

are legal deletion prefixes if and only if

\[
 \min_i r_i\ge K.
\tag{3.8}
\]

Finally, this orbit is a genuine wreath packet if and only if

\[
 r_i=m\qquad\hbox{for every }i.
\tag{3.9}
\]

#### Proof

By (3.2), every coordinate enters exactly once.  After a coordinate has left,
it cannot re-enter: a re-entry would be another transition at which that
coordinate is the unique new member, contradicting the bijectivity in
(3.1).  It therefore occupies one nonempty proper cyclic interval of owner
positions, giving (3.3).  Since one coordinate enters at every transition and
all owners have the same size, exactly one coordinate leaves at every
transition.  The departure times are consequently distinct, proving that
`tau` is a permutation.  Double-counting coordinate-owner incidences gives

\[
 \sum_i r_i=\sum_j|X_j|=nm.
\]

Conversely, (3.6) makes `g_j` enter at transition `j`.  Bijectivity of `tau`
makes exactly one coordinate leave there.  Thus all `|X_j|` are equal, and
their average is `sum_i r_i/n=m`; hence they are all `m`-sets and (3.2)
holds.

For (3.7), the coordinate `g_{j-t+1}` has age `t-1` in `X_j`.  It belongs to
`X_j` exactly when `r_{j-t+1}>=t`.  Thus every displayed letter is legal for
all `t<=K` exactly when (3.8) holds.  The letters are distinct by (3.1).

If every `r_i=m`, then

\[
 X_j=\{g_j,g_{j-1},\ldots,g_{j-m+1}\},
\]

which is a cyclic `m`-window, and (3.7) is its canonical deletion word.
Conversely, every coordinate in a wreath row lies in exactly `m` consecutive
middle windows, proving necessity of (3.9).  QED.

### Corollary 3.2 (what interval Hall does and does not certify)

For prescribed allowed residence sets
`R_i\subseteq\{K,\ldots,n-1\}`, form the
bipartite graph whose left vertices are arrivals `i`, whose right vertices
are departure slots `j`, and where

\[
 i\sim j
 \quad\Longleftrightarrow\quad
 j=i+r\pmod n\text{ for some }r\in R_i.
\tag{3.10}
\]

The departure part of a local schedule is exactly a perfect matching in this
graph, together with the scalar incidence condition `sum_i r_i=nm`.  If the
`R_i` are cyclic intervals, ordinary interval Hall is therefore an exact
criterion for choosing distinct departure slots.  It is not a criterion for
a wreath: the wreath matching is the single diagonal choice `r_i=m` for
every `i`.

This follows immediately from Theorem 3.1 and Hall's theorem.  Notice that
the sum condition is automatic when one starts from actual `m`-sets, but not
when one starts from an abstract departure matching.

### Corollary 3.3 (point margins and interval defect)

For `q<=K`, coordinate `g_i` occurs in exactly

\[
 r_i-q
\tag{3.11}
\]

of the depth-`q` states `P_q(X_j)`.  Thus packetwise point regularity forces
`r_i=m`, but global point regularity over several candidate cycles permits
positive and negative residence defects to cancel.

Let

\[
 W_j=\{g_j,g_{j-1},\ldots,g_{j-m+1}\}
\tag{3.12}
\]

be the canonical shadow of the orbit.  Then

\[
 \boxed{
 \sum_j|X_j\mathbin\triangle W_j|
 =\sum_i|r_i-m|.}
\tag{3.13}
\]

Consequently, if

\[
 \Delta=\frac12\sum_i|r_i-m|,
\tag{3.14}
\]

then at most `Delta` owner slots satisfy `X_j!=W_j`.

#### Proof

Coordinate `g_i` is deleted at positions `1,...,q` in the `q` owners
`X_i,...,X_{i+q-1}`.  These are contained in its residence interval because
`r_i>=K`, proving (3.11).  The actual and canonical incidence intervals of
`g_i` have the same first position and respective lengths `r_i` and `m`, so
their symmetric difference has size `|r_i-m|`.  Summing first over
coordinates and then over owners proves (3.13).  Two distinct `m`-sets have
symmetric difference at least two, giving (3.14).  QED.

## 4. A radius-one, exact-margin obstruction

The next construction is the decisive obstruction on the fixed Gaussian
window.  It does not merely fail an unlabelled test: it preserves labelled
owners, uses exact nested deletion prefixes, and has a unique local successor
cover.

For clarity, the depth-`K` local successor digraph used below has an arc
`Y\to X` exactly when

\[
 X\setminus Y=\{d_1(X)\},\qquad
 d_{t+1}(X)=d_t(Y)\quad(1\le t<K).
\tag{4.0}
\]

### Theorem 4.1 (protected two-cycle residence obstruction)

Let `m>=10`, `n=2m+1`, and `1<=K<=m-1`.  There is a family of `2n` distinct
labelled `m`-set owners, split into two directed `n`-cycles, with the following
properties.

1. Every first-label cycle is a bijection onto `[n]`.
2. Every intended transition satisfies the owner arrival law (3.2) and all
   deletion-word successor identities through depth `K`.
3. In the induced local successor graph, including the owner support law,
   these two cycles are the unique cycle cover.  Thus every local Hall
   inequality holds with equality.
4. Every coordinate occurs exactly twice at every deletion position and
   exactly `2(m-q)` times among the depth-`q` states, for every `q<=K`.
5. Every consecutive deletion-block histogram is independent of the starting
   depth.
6. Both departure matchings have radius one about the canonical matching.
7. Neither directed `n`-cycle is a wreath packet.

#### Construction

Work in `Z_n`.  Take the two cyclic coordinate orders

\[
 h^A=(0,1,2,\ldots,2m)
\tag{4.1}
\]

and

\[
 h^B=(1,0,2,4,\ldots,2m,3,5,\ldots,2m-1).
\tag{4.2}
\]

For either order `h=(h_j)`, let

\[
 W_j^h=\{h_{j-m+1},\ldots,h_j\}.
\tag{4.3}
\]

Define the actual owners by

\[
 X_j^h=W_j^h\quad(j\ne m),
 \qquad
 X_m^h=(W_m^h\setminus\{h_1\})\cup\{h_0\},
\tag{4.4}
\]

and define their deletion prefixes by

\[
 d_t(X_j^h)=h_{j-t+1},\qquad 1\le t\le K.
\tag{4.5}
\]

#### Proof: legality and residence

In arrival-index coordinates the exceptional support is

\[
 J=\{0,2,3,\ldots,m\}
\tag{4.6}
\]

instead of the canonical interval `I_m={1,...,m}`.  Thus all letters in
(4.5) are present even at the exceptional owner precisely through
`K=m-1`; the missing `m`th letter is `h_1`.

Swapping the canonical departure slots of arrival positions `0` and `1`
gives

\[
 r_0=m+1,\qquad r_1=m-1,\qquad r_i=m\ (i\ne0,1).
\tag{4.7}
\]

Equivalently,

\[
 \tau(0)=m+1,\qquad \tau(1)=m,
 \qquad \tau(i)=i+m\ (i\ne0,1).
\tag{4.8}
\]

This is a permutation, its residence sum is `nm`, and every departure moves
by at most one from the canonical slot.  Theorem 3.1 proves (4.5), all
successor identities, and the radius-one assertion.  It also proves that the
row is not a wreath, because (4.7) is not constant.

Within one row, all supports are distinct.  The canonical supports are the
distinct cyclic `m`-intervals, while `J` is not a cyclic interval: it contains
positions `0` and `2` but not `1`, and the other arc from `2` to `0` is too
long to fit in an `m`-interval.

#### Proof: the two rows do not interact

For a coordinate set `S`, let `e(S)` be the number of ordinary cyclic edges

\[
 \{x,x+1\}\quad(x\in\mathbb Z_n)
\]

contained in `S`.  Every actual `A`-owner satisfies

\[
 e(S)\ge m-2:
\tag{4.9}
\]

a canonical interval has `m-1` internal ordinary edges, and the exceptional
set has exactly `m-2`.

In the order (4.2), the smaller cyclic positional distances between the
endpoints of ordinary coordinate edges are as follows:

\[
\begin{array}{c|c}
\text{ordinary edge}&\text{positional distance in }h^B\\ \hline
\{0,1\}&1\\
\{1,2\}&2\\
\{2r-1,2r\},\ 2\le r\le m&m-1\\
\text{all remaining ordinary edges}&m.
\end{array}
\tag{4.10}
\]

A cyclic `B`-window of `m` positions can contain the endpoints of both short
edges and of at most one distance-`m-1` edge.  Indeed, a pair at distance
`m-1` must be the two endpoints of that window.  Hence every canonical
`B`-owner has

\[
 e(S)\le3.
\tag{4.11}
\]

The exceptional owner is obtained by one Johnson swap; adding one coordinate
can create at most two ordinary edges, so it has `e(S)<=5`.

One Johnson swap changes `e(S)` in absolute value by at most two: the removed
coordinate destroys at most two cycle edges and the added coordinate creates
at most two, so the net change lies in `[-2,2]`.  For `m>=10`, (4.9)-(4.11)
therefore imply that no actual `A`-owner equals or is Johnson-adjacent to an
actual `B`-owner.  In particular, no local successor edge can run between the
two rows.

#### Proof: the successor cover is forced inside each row

Again use arrival-index coordinates.  Write

\[
 I_j=\{j-m+1,\ldots,j\}.
\]

For canonical intervals, `I_i` and `I_j` are Johnson-adjacent only when
`i=j-1` or `i=j+1`.  Of these two possible predecessors of `I_j`, only
`I_{j-1}` satisfies

\[
 I_j\setminus I_{j-1}=\{j\}=\{d_1(I_j)\}.
\tag{4.12}
\]

The only canonical intervals Johnson-adjacent to the exceptional `J` are
`I_{m-1},I_m,I_{m+1}`.  Indeed, if such an interval omits `0` from `J`, it
must contain the consecutive block `2,\ldots,m` and can only extend it by
`1` or `m+1`; if it contains `0`, direct inspection of the two arcs from `0`
to that block leaves only `I_{m-1}`.  The interval `I_m` is absent from the
actual row.  The remaining
exceptional differences are

\[
\begin{aligned}
 J\setminus I_{m-1}&=\{m\} &&\text{(the intended edge)},\\
 J\setminus I_{m+1}&=\{0\} &&\text{(wrong first label)},\\
 I_{m+1}\setminus J&=\{m+1\} &&\text{(the intended edge)},\\
 I_{m-1}\setminus J&=\{1\}\ne\{m-1\} &&(m\ge3).
\end{aligned}
\tag{4.13}
\]

Thus the support/first-label rule alone, already at `K=1`, forces the intended
predecessor at every owner.  For `K>1`, (4.5) also gives

\[
 d_{t+1}(X_j^h)=d_t(X_{j-1}^h),
\]

so all intended edges remain legal.  The induced successor graph is exactly
the disjoint union of the two displayed `n`-cycles.  Its bipartite Hall graph
is one-regular and has a unique perfect matching.

#### Proof: exact margins and block laws

In row `A`, coordinate `0` has residence `m+1` and coordinate `1` has
residence `m-1`.  In row `B`, the index-`0` coordinate is `1` and the
index-`1` coordinate is `0`, so the two defects cancel.  Every coordinate
therefore occurs in exactly `2m` of the `2n` middle owners.  By (3.11), it
occurs in exactly

\[
 2m-2q=2(m-q)
\]

depth-`q` states.

For each fixed deletion position `t`, (4.5) runs once through every coordinate
in each row, so every coordinate occurs exactly twice.  More generally, for
`t+s-1<=K`, the block

\[
 (d_t,\ldots,d_{t+s-1})(X_j^h)
 =(h_{j-t+1},h_{j-t},\ldots,h_{j-t-s+2})
\tag{4.14}
\]

runs through the same reverse cyclic `s`-blocks as `j` varies, independently
of `t`.  This proves every claimed fixed-block stationarity law and completes
the proof.  QED.

### Scope of Theorem 4.1

The theorem is an induced, protected `2n`-owner obstruction.  It proves that

\[
 \begin{gathered}
 \text{local Hall} + \text{correct }n\text{-cycles}+
 \text{rainbow labels}+\text{radius-one departures}\\
 +\text{all two-packet coordinate margins and fixed-block laws}
 \end{gathered}
\]

do not imply exact wreath packetization of the fixed deletion words.

It is **not** a completed counterexample on all `W` owners.  External owners
could create additional successor edges, and no simultaneous extension of
this block to a globally fiber-balanced nested resolution is proved here.
Also, the obstruction is cheap to repair locally: it has only two units of
the defect (3.14).  It therefore refutes an exact local theorem, not the
desired asymptotic alignment bound.

For every fixed `A`, the obstruction applies on `K=ceil(A sqrt(m))` once `m`
is large enough, because then `K<=m-1`.

## 5. A positive low-residence theorem

The residence normal form does yield an exact sufficient theorem with all
estimates exposed.

### Theorem 5.1 (shadow-clean low-defect scheduling)

Suppose all owners in `Omega` are partitioned into `B` proposed cycles

\[
 (X_{p,j})_{j\in\mathbb Z_n},\qquad 1\le p\le B,
\]

such that on each cycle:

1. `g_{p,j}=d_1(X_{p,j})` is a bijection onto `[n]`;
2. `X_{p,j}\setminus X_{p,j-1}={g_{p,j}}`;
3. `d_t(X_{p,j})=g_{p,j-t+1}` for every `t<=K`.

Let `r_{p,i}` be the residence lengths and set

\[
 \Delta=\frac12\sum_{p=1}^B\sum_{i\in\mathbb Z_n}|r_{p,i}-m|.
\tag{5.1}
\]

Define the canonical shadows

\[
 W_{p,j}=\{g_{p,j},g_{p,j-1},\ldots,g_{p,j-m+1}\}.
\tag{5.2}
\]

If all `W_{p,j}` are pairwise distinct, then they form an exact oriented
wreath factor `F`, and for every `q<=K`,

\[
 e_q(F,P)\le\Delta.
\tag{5.3}
\]

Consequently, with

\[
 S_K=\sum_{q=1}^K\frac1{c_q},
\]

one has

\[
 \boxed{
 \sum_{q=1}^K\frac{e_q(F,P)}{c_q}
 \le \Delta S_K\le\Delta K.}
\tag{5.4}
\]

In particular, for fixed `A` and `K<=A sqrt(m)+1`, the desired labelled loss
is `o(W)` whenever

\[
 \Delta=o\!\left(\frac W{\sqrt m}\right).
\tag{5.5}
\]

#### Proof

For fixed `p`, the sets (5.2) are the `n` cyclic `m`-windows of the coordinate
order `g_{p,0},...,g_{p,n-1}`.  There are `Bn=W` shadows.  Pairwise
distinctness therefore says that they cover every member of `Omega` exactly
once, so they are an exact wreath factor.

By (3.13), the number of slots with `X_{p,j}!=W_{p,j}`, summed over all rows,
is at most `Delta`.  At every other slot, condition 3 says that the actual
flag deletes

\[
 g_{p,j},g_{p,j-1},\ldots,g_{p,j-q+1},
\]

which is exactly the canonical depth-`q` deletion prefix of the shadow row.
An owner occupying a good actual slot cannot occur at a different shadow
slot, because both the actual owners and the shadows are pairwise distinct.
Thus only the at most `Delta` owners occupying bad slots can contribute to
`e_q`, proving (5.3).  Summing (5.3) gives the first inequality in (5.4); `c_q>=1` gives the
second.  Finally `K=O_A(sqrt(m))`, so (5.5) implies `Delta K=o(W)`.  QED.

The pairwise-shadow condition cannot simply be discarded.  Without it,
different proposed cycles can generate the same canonical middle owner, and
the shadow rows need not be an exact factor even when their total residence
defect is small.

## 6. Full words: local Hall still leaves a subtour problem

The residence obstruction disappears when the complete deletion word is
known, but a second obstruction remains: ordinary Hall chooses a cycle cover,
not an `n`-cycle factor.

Extend every flag to the empty set and write

\[
 w_X=(d_1(X),\ldots,d_m(X)).
\]

Define the ordered overlap states

\[
 H(w)=(d_1,\ldots,d_{m-1}),\qquad
 T(w)=(d_2,\ldots,d_m).
\tag{6.1}
\]

A full-word successor satisfies

\[
 T(w_Y)=H(w_X),
\tag{6.2}
\]

equivalently

\[
 w_Y=(y,d_1(X),\ldots,d_{m-1}(X))
\]

with `y` outside the support of `X`.

### Proposition 6.1 (exact local Hall condition, `m>=2`)

For every ordered `(m-1)`-tuple `s`, put

\[
 \mathcal H_s=\{X:H(w_X)=s\},\qquad
 \mathcal T_s=\{Y:T(w_Y)=s\}.
\]

The full-word successor bipartite graph has a perfect matching if and only if

\[
 \boxed{|\mathcal H_s|=|\mathcal T_s|\quad\text{for every }s.}
\tag{6.3}
\]

Each choice of statewise bijections induces a successor permutation of the
owners.  It gives a wreath factor if and only if every orbit has length `n`.

#### Proof

The successor graph is the disjoint union, over `s`, of the complete
bipartite graphs `\mathcal H_s\times\mathcal T_s`.  Equality (6.3) is therefore
necessary and sufficient for a perfect matching.

There is no hidden support exception.  If

\[
 w_X=(s_1,\ldots,s_{m-1},x),\qquad
 w_Y=(y,s_1,\ldots,s_{m-1}),
\]

then `x,y` lie outside the state `s`.  If `x=y`, the supports coincide, hence
`X=Y`; but then `H(w_X)=T(w_X)`, impossible for a word of distinct letters.
Thus `y` is outside `X`, as required.

It remains to justify the orbit-length assertion.  On a matched orbit write
`g_j=d_1(X_j)`.  Repeated use of (6.2) gives

\[
 w_{X_j}=(g_j,g_{j-1},\ldots,g_{j-m+1}).
\tag{6.4}
\]

Suppose the orbit has length `n` and `g_i=g_j`.  Since every word has distinct
letters, both circular separations between the two occurrences are at least
`m`.  As `n=2m+1`, one separation is exactly `m`.  Then two consecutive
supports in (6.4) are equal: the shifted window removes and inserts the same
coordinate.  This contradicts distinct ownership.  Hence the `n` first
letters are all distinct, so they are all coordinates, and (6.4) is exactly a
wreath row.  The converse is immediate.  QED.

Thus ordinary Hall solves only the overlap matching.  The remaining
constraint is a rainbow `n`-cycle-factor, equivalently a perfect matching in
the hypergraph of compatible `n`-cycles.

### Proposition 6.2 (closed full-word subtour obstruction)

For every `m>=3`, there is a closed family of `2n` distinct full owner words
such that:

1. (6.3) holds with every nonempty state class of size one;
2. every coordinate appears exactly twice in every deletion position and
   exactly `2(m-q)` times at every depth `q`;
3. every fixed consecutive-block histogram is depth-stationary;
4. the unique successor permutation has orbit lengths

   \[
   m+1,\quad m+1,\quad 2m,
   \tag{6.5}
   \]

   and hence there is no partition into two wreath packets.

#### Proof

Partition the coordinates as

\[
 [n]=R\sqcup S\sqcup\{z\},\qquad |R|=|S|=m,
\]

and choose cyclic sequences

\[
 A=(s_1,\ldots,s_m,z),\qquad
 B=(r_1,\ldots,r_m,z),
\]

and

\[
 C=(r_1,s_1,r_2,s_2,\ldots,r_m,s_m).
\]

For any one of these cyclic sequences `D=(u_i)` define all reverse
`m`-windows

\[
 w_i^D=(u_{i+m-1},u_{i+m-2},\ldots,u_i).
\tag{6.6}
\]

The corresponding owner is the support of the word.  The total word count is

\[
 (m+1)+(m+1)+2m=2n.
\]

All supports are distinct.  An `A`-support is an `m`-subset of
`S\cup\{z\}`, a `B`-support is an `m`-subset of `R\cup\{z\}`, and a
`C`-support contains
both an `R`- and an `S`-coordinate.  Within each cyclic sequence, different
proper cyclic intervals give different supports.

Within one sequence, (6.2) forces `w_i^D` to be followed by `w_{i+1}^D`.
There are no cross-sequence overlaps.  An `A`-`B` overlap of length `m-1>=2`
would have to lie in `A\cap B=\{z\}`.  An `A`-`C` overlap would be a
consecutive alternating `C`-segment of length at least two lying wholly in
`S`, which is impossible; the `B`-`C` case is symmetric.  Hence the successor
graph is exactly the three cycles in (6.5), and every local Hall state has one
head and one tail.

At any fixed word position, a coordinate occurs once among the words from
each cyclic sequence containing it.  Every coordinate belongs to exactly two
of `A,B,C`, so it occurs exactly twice at every deletion position.  It belongs
to `m` middle windows from each of those two sequences, hence to `2m` owners;
after the first `q` deletion positions it remains in `2(m-q)` states.  The
same shift argument applied to a block of word positions shows that every
fixed consecutive-block histogram is independent of its starting depth.

None of the three forced orbit lengths equals `n=2m+1`.  Equivalently, the
unique successor permutation is odd,

\[
 (-1)^{m+m+(2m-1)}=-1,
\]

whereas a product of two odd-length `n`-cycles is even.  QED.

This is a closed fixed-word block, not a theorem that the block extends to a
balanced resolution on all of `Omega`.  External words could add overlap
states unless closure is protected in the completion.

## 7. Exact obstruction and smallest replacement lemma

The scheduling problem has two independent global requirements.

1. **Residence:** a matched coordinate must leave exactly `m` owner steps
   after it enters.  Interval Hall only makes the departures distinct.
2. **Packet subtours and exact cover:** the chosen successor cover must consist
   of `n`-cycles, and their canonical shadows must cover every middle owner
   exactly once.

Theorem 4.1 shows that even correct `n`-cycles, exact aggregate point margins,
and radius-one departures do not imply the first requirement.  Proposition
6.2 shows that complete words and all first-order coordinate laws do not imply
the second.

The smallest clean sufficient statement exposed by this route is the
following.  It is unproved.

### Unproved lemma SCR-A (shadow-clean low-residence scheduling)

For every fixed `A` and all sufficiently large `m`, one can choose an integral
fiber-balanced common nested resolution through

\[
 K=\lceil A\sqrt m\rceil
\]

and partition its labelled owners into `B=W/n` locally compatible rainbow
`n`-cycles satisfying the three hypotheses of Theorem 5.1, such that:

1. all canonical shadows (5.2) are pairwise distinct; and
2. their total residence defect satisfies

   \[
   \Delta=o\!\left(\frac W{S_K}\right).
   \tag{7.1}
   \]

By Theorem 5.1, SCR-A implies

\[
 \sum_{q\le K}\frac{e_q}{c_q}=o(W)
\]

with one exact factor and the original labelled common nested resolution.
No fractional balancing, separate depthwise factor, or relabelling of owners
is used.

The exact-factor part of SCR-A is indispensable: small residence defect alone
does not prevent duplicate canonical shadows.  The residence part is also
indispensable: Hall and all aggregate point equations permit defects of
opposite signs to cancel between cycles.

## 8. Adversarial audit

The main claims were rechecked independently against the following failure
modes.

1. **Successor convention.**  The legal full-word move is

   \[
   (a_1,\ldots,a_m)\longmapsto(y,a_1,\ldots,a_{m-1}),
   \]

   so `T(next)=H(current)`.  Reversing `H` and `T` would reverse every stated
   orbit.  The proofs above use the displayed convention consistently.
2. **Truncation endpoint.**  The radius-one gadget requires `K<=m-1`.
   Its missing last deletion letter is exactly the coordinate whose residence
   was shortened.  It is not a full-word counterexample.
3. **Small `m`.**  The two-row separation proof uses `m>=10`.  The closed
   three-subtour construction uses `m>=3`; at `m=2`, length-one overlap states
   create cross compatibilities and that obstruction fails.
4. **Point margins.**  In Theorem 4.1, the `+1` residence defect of coordinate
   `0` in row `A` is cancelled by its `-1` defect in row `B`, and conversely
   for coordinate `1`.  Formula (3.11) then gives the exact depthwise point
   margin `2(m-q)`, not merely an average over depths.
5. **Owner distinctness and cross edges.**  The ordinary-edge invariant
   proves more than disjointness of the two rows: it proves no cross Johnson
   adjacency, so no external edge *within the induced block* can satisfy the
   owner arrival law.  It says nothing about owners outside the block.
6. **Shadow-clean hypothesis.**  The estimate (5.4) is invalid without global
   distinctness of the canonical shadows.  This condition is stated
   explicitly and is part of the unproved lemma.
7. **Balance and completion.**  Neither obstruction is claimed to be a full
   fiber-balanced resolution on all `W` owners.  Therefore this report gives
   no counterexample to the conjecture and no counterexample to a theorem
   exploiting additional exact-factor structure.
8. **Asymptotic implication.**  The only estimate used in Theorem 5.1 is
   `S_K<=K=O_A(sqrt(m))`, which follows from `c_q>=1`.  Thus
   `Delta=o(W/sqrt(m))` really does imply `Delta S_K=o(W)`.

The audit therefore accepts Theorems 2.1, 3.1, 4.1, and 5.1 with the stated
scope.  The route is exhausted at SCR-A: proving it requires a genuinely
global exact-cover/absorber theorem which simultaneously controls residence
defect and shadow collisions.  Neither ordinary Hall nor bounded departure
displacement can supply that theorem.
