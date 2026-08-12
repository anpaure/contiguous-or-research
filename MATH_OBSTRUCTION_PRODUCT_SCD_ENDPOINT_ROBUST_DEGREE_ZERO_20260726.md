# A six-coordinate cut makes the product-SCD endpoint robust degree zero

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Result

The proposed uniform endpoint-mixing statement is false, already for the
standard recursive BTK/Greene--Kleitman symmetric-chain decomposition.
The failure is much stronger than a loss of the desired exponent.

Let the two coordinate halves have size `m`, and form the usual rank-`m`
diagonal paths in products of two BTK chains.  There is a product path
`P` of length

\[
                         h=(1+o(1))\sqrt m                         \tag{0.1}
\]

and one of its endpoints `X` with the following properties.

1. `X` has at least

   \[
             2r(m-r)={m^2-h^2\over2}
                    =\left({1\over2}+o(1)\right)m^2               \tag{0.2}
   \]

   Johnson-adjacent endpoints of product-SCD paths, where
   `r=(m-h)/2`.
2. There is a set `Z` of exactly six physical coordinates such that every
   product-SCD path having an endpoint Johnson-adjacent to `X` uses an
   active direction in `Z`.

Consequently the endpoint graph has raw degree `Omega(m^2)` at `X`, but
its degree after retaining only paths whose complete active-direction set
avoids `Z` is exactly zero.

In fact, if `U_A,U_B` are the two length-`h` active alphabets of `P`, then
**every** set

\[
             Z=Z_A\mathbin{\dot\cup}Z_B,
             \qquad Z_A\in\binom{U_A}{3},\quad
                    Z_B\in\binom{U_B}{3},                         \tag{0.3}
\]

is such a cut.  Thus the obstruction is a structured family, not one
exceptional choice.

For

\[
                         H=\sqrt m\log\log m,                     \tag{0.4}
\]

we have `h=o(H)` and `|Z|=6=O(H)`.  Hence there can be no positive
polynomial lower bound, uniform over all forbidden sets of size `O(H)`,
for this concrete product-SCD endpoint graph.

The BTK decomposition is invariant under reverse-complement, which is the
strong complement symmetry possible for one coordinate-ordered SCD.  Raw
set complementation cannot permute the chains of *any* SCD when `m>=2`;
this elementary point is proved in Section 6.  Thus a request for a
literally raw-complement-stable single SCD is inconsistent.  The usual
raw-complement construction uses the two SCDs `D_m,D_m^c`; the theorem
below closes the robust-degree claim for either fixed product-SCD colour.
It does not assert a common six-coordinate cut after arbitrary switching
between unrelated colours.

## 1. The concrete BTK decomposition

Represent a subset of `[m]` by a zero-one word.  Regard `0` as an opening
parenthesis and `1` as a closing parenthesis, and perform the usual greedy
noncrossing matching.  After all possible pairs have been removed, the
unmatched word has the form

\[
                              1^p0^{h-p}.                         \tag{1.1}
\]

Indeed, an unmatched `0` to the left of an unmatched `1` would itself be
an available pair.

Fix the matched pairs and their zero/one values, and let

\[
                         u_1<\cdots<u_h                           \tag{1.2}
\]

be the unmatched positions.  The corresponding BTK chain consists of
the `h+1` words whose restrictions to these positions are

\[
               0^h,\quad 10^{h-1},\quad 1^20^{h-2},\quad\ldots,
               \quad 1^h.                                       \tag{1.3}
\]

All matched coordinates remain fixed.  The set

\[
                         U(C)=\{u_1,\ldots,u_h\}                  \tag{1.4}
\]

is the active alphabet of the chain.

### Lemma 1.1 (self-contained SCD audit)

The classes (1.3) partition the Boolean lattice into saturated symmetric
chains.  A chain with active alphabet of size `h` has minimum rank

\[
                              r={m-h\over2}                       \tag{1.5}
\]

and maximum rank `m-r`.

#### Proof

Greedy matching is unique, and (1.1) shows that every word occurs in
exactly one class (1.3).  Consecutive words in (1.3) differ by changing
one zero to one, so the class is a saturated chain.  Every matched pair
contains one one, and there are `(m-h)/2` pairs.  The all-zero unmatched
state therefore has rank `(m-h)/2`; the all-one unmatched state has rank
`(m-h)/2+h=m-(m-h)/2`.  Hence the chain is symmetric.  \(\square\)

Let `rho(i)=m+1-i` and put

\[
                         \kappa(S)=\rho([m]\setminus S).          \tag{1.6}
\]

### Lemma 1.2 (reverse-complement symmetry)

The involution `kappa` permutes the BTK chains, reversing every chain it
maps.  If it sends `C` to `C'`, then

\[
                         U(C')=\rho(U(C)).                        \tag{1.7}
\]

#### Proof

A matched pattern `0...1` is sent by reverse-complement to another
matched pattern `0...1`, with both positions reflected.  The unmatched
word `1^p0^{h-p}` is sent to `1^{h-p}0^p`.  Thus an entire class (1.3)
is sent to another such class, in reverse rank order, and its unmatched
positions are reflected.  \(\square\)

## 2. The active-alphabet containment law

The obstruction rests on a monotonicity special to this concrete SCD.
For a top word, all unmatched coordinates are ones, and they are exactly
the active alphabet.  For a bottom word, all unmatched coordinates are
zeros.

### Lemma 2.1 (top containment)

Let `T` and `T'` be tops of BTK chains `C,C'`.

1. If `T'=T-x`, then

   \[
                              U(C')\subseteq U(C).                \tag{2.1}
   \]

2. If `T'=T+y`, then

   \[
                              U(C)\subseteq U(C').                \tag{2.2}
   \]

#### Proof

For a zero-one word `w`, define

\[
 s_0=0,
 \qquad
 s_j=\#\{i\le j:w_i=0\}-\#\{i\le j:w_i=1\}.                    \tag{2.3}
\]

A one at position `j` is unmatched precisely when `s_j` is a new strict
minimum of the prefix walk.  This is the standard stack description of
unmatched closing parentheses.

Changing a one at `x` to zero adds two to every `s_j` with `j>=x`.
It cannot create a new strict-minimum time: before `x` nothing changes,
and after `x` the whole suffix is translated upward by two.  Hence every
unmatched one of `T-x` was already an unmatched one of `T`, proving
(2.1).

Changing a zero at `y` to one subtracts two from the same suffix.  Every
old strict-minimum time before `y` is unchanged.  Every old strict-minimum
time after `y` remains below all earlier suffix values, which are shifted
by the same amount, and remains below the unshifted prefix even more
strongly.  Thus no old unmatched one is lost, proving (2.2).  \(\square\)

Reverse-complement gives the bottom version.

### Lemma 2.2 (bottom containment)

Let `B,B'` be bottoms of BTK chains `D,D'`.

1. If `B'=B+y`, then `U(D')\subseteq U(D)`.
2. If `B'=B-x`, then `U(D)\subseteq U(D')`.

#### Proof

Apply Lemma 2.1 after the involution `kappa` of Lemma 1.2.  A bottom is
sent to a top; adding a coordinate before complementation becomes deleting
one after complementation, and conversely.  Reflection does not affect
set containment.  \(\square\)

There is an exact two-coordinate consequence.  If `C` has minimum rank
`r` and `C'` has minimum rank `r+1`, then their active alphabet sizes are
`h=m-2r` and `h-2`.  Therefore, whenever their tops differ by deleting
one coordinate,

\[
                    U(C')\subset U(C),
                    \qquad |U(C)\setminus U(C')|=2.              \tag{2.4}
\]

The same statement holds for adjacent bottoms.  Moving from minimum
`r` to `r-1` instead gives containment in the other direction and adds
exactly two active coordinates.

## 3. Product diagonals and their endpoints

Take disjoint halves `A,B`, each identified with `[m]`, and use the BTK
decomposition on each half.  If chains `C,D` have minimum ranks `a,b`,
put

\[
                         s=\max(a,b),
                         \qquad \ell=m-2s.                       \tag{3.1}
\]

Their rank-`m` product diagonal is

\[
 Q(C,D)=
   \bigl(C_{s+t}\cup D_{m-s-t}:0\le t\le\ell\bigr).             \tag{3.2}
\]

Its low and high endpoints have `A`-ranks `s` and `m-s`.  Its active
direction set is the union of the chain increments used between ranks
`s` and `m-s` in the two halves.  In particular, if `a=s`, its active
`A`-directions are the whole set `U(C)`; if `b=s`, its active
`B`-directions are the whole set `U(D)`.

Choose an integer `h` of the same parity as `m` such that

\[
                         h=\sqrt m+O(1),\qquad h\ge6,             \tag{3.3}
\]

and put `r=(m-h)/2`.  There is an explicit BTK chain of minimum `r`:
its bottom and top words are

\[
                         (01)^r0^h,
                         \qquad (01)^r1^h.                       \tag{3.4}
\]

The first `2r` coordinates are greedily matched in adjacent pairs, and
the last `h` coordinates form its active alphabet.

Take copies `C,D` of this chain in `A,B`, and let `P=Q(C,D)`.  Write

\[
                         U_A=U(C)\subset A,
                         \qquad U_B=U(D)\subset B.                \tag{3.5}
\]

Both sets have size `h`.  The high endpoint of `P` is

\[
                         X=T(C)\cup B(D),                         \tag{3.6}
\]

where `T(C)` is the chain top and `B(D)` its chain bottom.  Thus

\[
                         |X\cap A|=m-r,
                         \qquad |X\cap B|=r.                     \tag{3.7}
\]

Fix arbitrary three-subsets

\[
                         Z_A\subset U_A,
                         \qquad Z_B\subset U_B,                  \tag{3.8}
\]

and put `Z=Z_A\cup Z_B`.

## 4. Exact zero robust degree

Every middle owner belongs to a unique pair of BTK chains, so if it is a
product-diagonal endpoint, its product path is unique.  Denote that path
by `Q_Y`.

### Theorem 4.1 (six-coordinate endpoint cut)

If `Y` is any product-SCD path endpoint Johnson-adjacent to `X`, then

\[
                         \operatorname{Act}(Q_Y)\cap Z\ne\varnothing. \tag{4.1}
\]

Consequently

\[
 \#\{Y:Y\sim_J X,\ Y\text{ a product endpoint},\
                \operatorname{Act}(Q_Y)\cap Z=\varnothing\}=0.  \tag{4.2}
\]

#### Proof

Johnson adjacency changes the `A`-rank by at most one.  By (3.7),

\[
 |Y\cap A|\in\{m-r-1,m-r,m-r+1\}.                              \tag{4.3}
\]

Because `h>=6`, the smallest number in (4.3) is greater than `m/2`.
The low endpoint of every product diagonal has `A`-rank at most `m/2`.
Hence `Y` must be a high endpoint.  If its product path has level `s`,
then `|Y\cap A|=m-s`, so

\[
                              s\in\{r-1,r,r+1\}.                 \tag{4.4}
\]

We treat the three cases.

**Case 1: `s=r`.**  The Johnson exchange preserves the `A`-rank, so
both exchanged coordinates lie in the same half.  If they lie in `A`,
then the `B`-component of `Y` is still the bottom `B(D)`.  Since `D` has
minimum `r`, the path `Q_Y` uses every direction of `U_B`, and therefore
uses `Z_B`.  If the exchange lies in `B`, the unchanged `A`-component is
the top `T(C)`, and `Q_Y` uses every direction of `U_A`, hence `Z_A`.

**Case 2: `s=r+1`.**  The exchange deletes one `A`-coordinate and adds
one `B`-coordinate.  Let `a',b'` be the minimum ranks of the two chains
containing the components of `Y`.  Since the product level is `r+1`,

\[
                         \max(a',b')=r+1.                         \tag{4.5}
\]

If `a'=r+1`, the `A`-component of `Y` is the top of its chain and is
obtained from `T(C)` by deleting one coordinate.  Lemma 2.1 and (2.4)
give an active alphabet `U_A'` satisfying

\[
                         U_A'\subset U_A,
                         \qquad |U_A\setminus U_A'|=2.           \tag{4.6}
\]

Since `|Z_A|=3`, (4.6) implies `U_A'\cap Z_A` is nonempty.  This whole
alphabet is used by `Q_Y`, because its chain minimum equals the product
level.

If `a'<r+1`, then (4.5) forces `b'=r+1`.  Now the `B`-component is the
bottom of its chain and is obtained from `B(D)` by adding one coordinate.
Lemma 2.2 gives the identical conclusion with `U_B,Z_B` in place of
`U_A,Z_A`.

**Case 3: `s=r-1`.**  The exchange deletes one `B`-coordinate and adds
one `A`-coordinate.  At least one component chain has minimum `r-1`.
If it is the `A`-chain, Lemma 2.1 gives an active alphabet containing
`U_A`, hence meeting `Z_A`.  If it is the `B`-chain, Lemma 2.2 gives an
active alphabet containing `U_B`, hence meeting `Z_B`.  Again that whole
alphabet is used because this component chain realizes the product level.

All possibilities in (4.4) meet `Z`, proving (4.1)--(4.2).  \(\square\)

The theorem is orientation-independent: reversing `Q_Y` reverses the
order of its active directions but does not change their set.  It also
remains true if avoiding `Z` is imposed on the seam directions as well,
because an internal active direction already lies in `Z`.

## 5. The raw degree is quadratic

The zero in (4.2) is not caused by an endpoint of small ordinary degree.

### Proposition 5.1 (explicit raw endpoint degree)

The endpoint `X` has at least

\[
                         2r(m-r)={m^2-h^2\over2}                 \tag{5.1}
\]

Johnson-adjacent product-SCD endpoints.

#### Proof

Exchange one of the `m-r` coordinates of `X\cap A` with one of the `r`
coordinates of `A\setminus X`.  The `B`-component remains `B(D)`, whose
chain has minimum `r`; hence the new owner is the high endpoint of its
product diagonal at level `r`.  This gives `(m-r)r` endpoints.

The same argument for exchanges wholly inside `B`, now keeping `T(C)`
fixed, gives another `r(m-r)` endpoints.  The two families are disjoint,
which proves (5.1).  \(\square\)

With `h=\sqrt m+O(1)`, (5.1) is `(1/2+o(1))m^2`, while the robust degree
against any cut (0.3) is zero.

## 6. Complement scope

The reverse-complement symmetry in Lemma 1.2 is an exact symmetry of the
chosen coordinate-ordered SCD.  Raw complementation alone cannot have the
same property.

### Lemma 6.1 (raw-complement obstruction)

For `m>=2`, no symmetric-chain decomposition of `2^[m]` is permuted as a
collection of chains by `S\mapsto[m]\setminus S`.

#### Proof

The unique chain containing the empty set also contains `[m]`.  Its
complement image contains both sets, so invariance would force this chain
to map to itself.  If its rank-one member is `{x}`, complement symmetry
would make its rank-`(m-1)` member `[m]\setminus\{x\}`.  But a saturated
increasing chain containing `{x}` has `x` in every later member, a
contradiction.  \(\square\)

Thus one must distinguish three notions:

1. the ordinary rank symmetry of every SCD;
2. reverse-complement equivariance, supplied here by BTK; and
3. a two-colour raw-complement pair `D_m,D_m^c`.

Theorem 4.1 applies verbatim to either fixed colour after complementing
all words.  A construction allowed to choose a different colour at every
endpoint is a larger mixed-colour graph and needs a separate common-cut
audit.  For coordinate-conjugate BTK colours, however, the following
stronger record-tail argument gives a common cut.

### Lemma 6.2 (bounded edit of a BTK central active tail)

Fix any ordering of the \(m\) coordinates and the BTK decomposition in
that order.  Let \(w,w'\) be the \(A\)-restrictions of two
Johnson-adjacent middle owners.  Suppose \(|w|=k>m/2\), put
\(h=2k-m\), and let \(I_h(w)\) be the coordinates used by the chain
segment between ranks \(m-k\) and \(k\).  If \(w'\) has corresponding
positive length \(h'\), then

\[
                         |I_h(w)\cap I_{h'}(w')|\ge h-4.         \tag{6.1}
\]

#### Proof

In the chosen coordinate order put

\[
 D_w(t)=\sum_{i\le t}(2w_i-1).
\]

The unpaired one-positions are exactly the strict ascending record times
of \(D_w\): a one is unmatched precisely when no preceding unmatched
zero is available, equivalently when its height exceeds every previous
prefix height.  If the maximum height is \(M\), then the chain minimum
is \(k-M\).  The rank-\(k\) word uses the first \(M\) unpaired
positions, whereas the rank-\((m-k)\) word uses the first

\[
                         m-k-(k-M)=M-h
\]

of them.  Thus \(I_h(w)\) is the terminal \(h\)-set of the ordered
record-time set.

If the Johnson edge is internal to \(A\), two opposite bits are
exchanged.  Between their positions the two prefix walks differ by the
constant \(2\) or \(-2\) and agree again afterwards.  During the
translated interval, only the first visits to the two newly exposed
height levels can be added to the record set.  After the walks reunite,
the altered previous maximum can suppress only the first two subsequent
record levels.  Interchanging the two walks gives

\[
                  |\mathcal R(w)\mathbin\triangle\mathcal R(w')|\le4.
\]

If the edge is internal to \(B\), the two \(A\)-words agree.  If it is
cross-half, one \(A\)-bit changes, so one suffix of the prefix walk is
translated by two forever.  This adds or suppresses at most the first two
record levels, and hence the record-set symmetric difference is at most
two.

Finally, if ordered sets differ in at most \(d\) elements, their
terminal tails of lengths \(h,h'\) satisfy

\[
 |T_h(E)\setminus T_{h'}(E')|
       \le d+(h-h')_+.
\]

This follows by first shortening the first tail to length \(h'\) and
then performing the at most \(d\) insertions/deletions.  In the internal
cases \(h'=h\) and \(d\le4\); in the cross case
\(|h-h'|=2\) and \(d\le2\).  Equation (6.1) follows.  \(\square\)

### Corollary 6.3 (common cut for a small transverse frame catalogue)

Let \(\mathfrak F\) be a family of \(K\) coordinate-conjugate BTK
decompositions on the \(A\)-half.  Product paths may choose any member
of \(\mathfrak F\), independently of their \(B\)-half decomposition.
For a high-rank owner \(X\) of excess \(h\ge5\), define

\[
                         Z_{\mathfrak F}(X)
                         =\bigcup_{\mathcal D\in\mathfrak F}
                                      I_h^{\mathcal D}(X\cap A). \tag{6.2}
\]

Then

\[
                         |Z_{\mathfrak F}(X)|\le Kh,             \tag{6.3}
\]

and every Johnson-adjacent product-path endpoint from every frame in
\(\mathfrak F\) has an active direction in \(Z_{\mathfrak F}(X)\).

#### Proof

As in Theorem 4.1, every adjacent endpoint remains on the high side when
\(h\ge5\).  If it uses frame \(\mathcal D\), Lemma 6.2 shows that its
active \(A\)-tail meets the particular set
\(I_h^{\mathcal D}(X\cap A)\) in (6.2).  The size bound is immediate.
\(\square\)

Because reverse-complement preserves BTK, its raw complementary SCD is
just the coordinate-reversed BTK decomposition.  Thus Corollary 6.3
includes the standard two-colour pair \(\mathcal D_m,\mathcal D_m^c\).
More generally, at \(h=(1+o(1))\sqrt m\) and
\(H=\sqrt m\log\log m\), it rules out every fixed catalogue of
\(K=O(\log\log m)\) coordinate-conjugate BTK frames: its common
forbidden set still has size \(O(H)\).

## 7. Consequence at the requested scale

Take

\[
                         H=\lceil\sqrt m\log\log m\rceil.        \tag{7.1}
\]

The choice (3.3) satisfies `h=o(H)`.  All directions of a candidate
atomic path therefore occur before an incoming `H`-memory queue can
expire.  Nevertheless a forbidden queue support of only six coordinates
kills every endpoint continuation from `X` in the fixed product-SCD
endpoint graph.

Hence the exact proposed statement

> every forbidden set `Z` of size `O(H)` leaves polynomially many
> Johnson-adjacent endpoint blocks whose active directions avoid `Z`

is false.  It fails with robust degree zero despite ordinary degree
`Theta(m^2)`.

The minimal statement not excluded by this theorem must change at least
one quantifier.  Viable possibilities include:

* average over the incoming queue state rather than uniformity in `Z`;
* permit genuinely mixed SCD colours and prove a common-cut expansion
  theorem for their union;
* split a path before exposing its whole active alphabet; or
* use endpoint blocks whose active alphabets are not nested under the
  top/bottom parent relation.

No coefficient-one conclusion follows.  The proved result is the exact
structured counter-cut requested for the fixed concrete product-SCD lane.
