# The antipodal-geodesic resource hypergraph: exact codegrees, flux lattice, and the cover-down gate

Date: 2026-07-31  
Status: exact all-parameter counting, exact pair-codegrees and maximum,
exact coordinate-flux/divisibility laws, exact small-set expansion, and an
all-parameter two-by-two absorber.  The final edge-aligned cover-down theorem
is not proved, and no all-parameter perfect matching is claimed.

## 0. Result and verdict

Let `Omega` have size `2n`.  The resource hypergraph `H_n` has three shores

\[
 {cal M}=\binom\Omega n,\qquad
 {cal L}=\binom\Omega{n-1},\qquad
 {cal U}=\binom\Omega{n+1}.
\]

An edge is one unoriented complement geodesic

\[
 X_0,X_1,\ldots,X_n=\overline {X_0}
\]

together with its `n+1` middle vertices, its `n` lower turns
`X_(i-1) cap X_i`, and its `n` upper turns `X_(i-1) cup X_i`.
Thus `H_n` is `(3n+1)`-uniform, and a perfect matching is exactly an
antipodal-geodesic Catalan filler.

The exact new conclusions are as follows.

1. Every resource has degree

   \[
                 D={n+1\over2}(n!)^2.
   \]

2. Every pair-codegree has a closed factorial formula depending only on
   the two shore types and the intersection size.  In particular

   \[
        \boxed{\Delta _2(H_n)={2D\over n+1}=(n!)^2.}
   \]

   Equality is attained by a complementary pair of middle vertices, by an
   incident lower-middle pair, and by an incident middle-upper pair.

3. Every candidate obeys, for every coordinate `x`,

   \[
        m_x=u_x=\ell_x+1,                                  \tag{0.1}
   \]

   where the three letters count selected resources containing `x` on the
   three shores.  Consequently every absorbable leave of `t` candidates
   must obey

   \[
      |R_M|=(n+1)t,\quad |R_L|=|R_U|=nt,\quad
      m_x(R)=u_x(R)=\ell_x(R)+t.                            \tag{0.2}
   \]

   The complete resource vector satisfies these identities with
   `t=Cat_n`.  A matching process automatically preserves them, but an
   absorber cannot be asked to absorb an arbitrary class-balanced leave.

4. The codegree theorem gives a rigorous small-set expansion statement.  If
   `S` is any set of resource vertices and `N(S)` is the set of candidates
   meeting it, then

   \[
       |N(S)|\ge
       {D|S|\over 1+2(|S|-1)/(n+1)}.                         \tag{0.3}
   \]

   Also, after forbidding `s` additional resources, every fixed resource
   retains at least

   \[
                         D\left(1-{2s\over n+1}\right)       \tag{0.4}
   \]

   candidates (when the right side is positive).  This is genuine local
   resilience, but it controls only `O(n)` forbidden resources, not a
   macroscopic cover-down.

5. For every `n>=3`, every candidate edge belongs to an explicit
   two-by-two trade

   \[
                         A+B=C+D,                            \tag{0.5}
   \]

   where `A,B` are resource-disjoint and `C,D` are resource-disjoint.
   Therefore the one-edge matching `{B}` absorbs the complete resource edge
   `A`, switching to `{C,D}`.  This supplies a uniform absorber for every
   **candidate-shaped** leave.

6. The remaining theorem is now sharply isolated:

   > **Edge-aligned cover-down.** Reserve vertex-disjoint instances of
   > (0.5), and find a matching on the remaining hypergraph whose leave is
   > a disjoint union of the designated candidate edges `A_i`.

   The switches then finish a perfect matching.

The raw hypergraph is unusually promising—uniform fractional matching,
normalized pair-codegree `2/(n+1)`, exact flux divisibility, and ubiquitous
absorbers—but no standard matching/design theorem currently proves this
cover-down.  The usual theorems either fix the uniformity, give only an
almost-perfect matching, require dense minimum codegrees, or require a
power-saving codegree.  Here the uniformity is `3n+1` and
`Delta_2=D*Theta(1/n)`, not `D^(1-gamma)`.

## 1. Permutation and pointed-wreath normal form

Orient a candidate.  It is uniquely specified by an initial `n`-set and
two orders

\[
 a_1,\ldots,a_n\quad\hbox{and}\quad b_1,\ldots,b_n
\]

of the initial set and its complement, with

\[
 X_i=X_{i-1}-a_i+b_i.                                      \tag{1.1}
\]

Reversal identifies the two orientations, so the number of candidates is

\[
                     |E(H_n)|={(2n)!\over2}.                 \tag{1.2}
\]

Equivalently put the symbols in the pointed cyclic order

\[
       (a_1,\ldots,a_n,b_1,\ldots,b_n,\infty).               \tag{1.3}
\]

After cutting at `infinity`, the resource windows in the linear word
`x_1...x_(2n)` are

\[
\begin{array}{c|c|c}
\text{shore}&\text{window length}&\text{allowed starts}\\ \hline
M&n&1,\ldots,n+1\\
L&n-1&2,\ldots,n+1\\
U&n+1&1,\ldots,n.
\end{array}                                                  \tag{1.4}
\]

The `M` windows are the middle vertices.  Complements of the `U` windows,
after adjoining `infinity`, are the point-containing middle intervals.
Thus exactness of `M+U` is precisely the pointed exact wreath factor already
provided by MSW.  The `L` windows are the additional transverse rainbow.

This dictionary is also the shortest proof of all the codegree formulae.

## 2. Exact pair-codegrees

Fix two resources `A,B` of sizes `s,t`.  Suppose their windows occupy
position intervals `I,J` in (1.4), and put

\[
                         q=|A\cap B|.
\]

There are no compatible permutations unless `|I cap J|=q`.  For one
compatible ordered pair of starts, the four position atoms may be filled in

\[
             q!(s-q)!(t-q)!(2n-s-t+q)!                      \tag{2.1}
\]

ways.  Sum over compatible starts and divide by two for reversal.

The result is the following complete table.  Unlisted intersection sizes
have codegree zero.

\[
\begin{array}{c|c|c}
\text{types}&q&\deg(A,B)\\ \hline
L,L&0\le q\le n-2&(q+1)q!(q+2)!(n-1-q)!^2\\
M,M&0\le q\le n-1&(q+1)(q!)^2(n-q)!^2\\
U,U&2\le q\le n&(q-1)q!(q-2)!(n+1-q)!^2\\
L,M&0\le q\le n-1&(q+1)q!(q+1)!(n-1-q)!(n-q)!\\
M,U&1\le q\le n&q\,q!(q-1)!(n-q)!(n+1-q)!\\
L,U&1\le q\le n-2&q(q!)^2(n-1-q)!(n+1-q)!\\
L,U&q=n-1&(3n-2)(n-1)!^2.
\end{array}                                                   \tag{2.2}
\]

For example, the number of compatible **ordered** start pairs is

\[
\begin{array}{c|c}
LL,MM,LM&2(q+1)\\
UU&2(q-1)\\
MU&2q\\
LU,\ q\le n-2&2q\\
LU,\ q=n-1&3n-2.
\end{array}                                                   \tag{2.3}
\]

This proves (2.2) directly.

### Theorem 2.1 (sharp maximum)

For every `n>=2`,

\[
                \Delta_2(H_n)=(n!)^2={2D\over n+1}.          \tag{2.4}
\]

#### Proof

For two middle resources, (2.2) normalizes to

\[
 {\deg(A,B)\over D}
 = {2(q+1)\over(n+1)\binom nq^2}.                            \tag{2.5}
\]

Its maximum is `2/(n+1)` at `q=0`, i.e. complementary middle
sets.  The `LM` and `MU` rows normalize respectively to

\[
 {2(q+1)\over(n+1)\binom nq\binom n{q+1}},\qquad
 {2q\over(n+1)\binom nq\binom n{q-1}},                      \tag{2.6}
\]

and attain the same maximum at `q=n-1` and `q=n`, i.e. at
containment.  The `LL` and `UU` rows are shifted copies of the `MM`
row and are smaller.  For the exceptional `LU` containment row the ratio
is

\[
                     {2(3n-2)\over n^2(n+1)},                \tag{2.7}
\]

which is smaller for `n>=3` (and ties at `n=2`).  The remaining `LU`
values are smaller by the displayed binomial factors.  This proves (2.4).
`square`

The high pairs are sparse *inside one candidate*: it contains one
complementary `MM` pair, `2n` incident `LM` pairs, and `2n` incident `MU`
pairs.  Thus the `Theta(1/n)` maximum is carried by only `Theta(n)` of the
`Theta(n^2)` resource pairs in an edge.  Any successful nibble should use
this structure rather than treating every pair as worst-case.

## 3. Exact flux and divisibility

For a coordinate `x`, let `m_x,l_x,u_x` be the number of resources in one
candidate which contain `x` on the three shores.

### Theorem 3.1 (pathwise coordinate flux)

Every candidate satisfies

\[
                         m_x=u_x=l_x+1.                       \tag{3.1}
\]

#### Proof

If `x=a_i` is removed at time `i`, it belongs to exactly the first `i`
middle states, exactly the first `i` upper turns, and the first `i-1`
lower turns.  If `x=b_i` is inserted at time `i`, the three counts are
`n-i+1,n-i+1,n-i`.  These are all coordinates.  `square`

Consequently a union of `t` disjoint candidate edges satisfies (0.2).  The
complete resource vector does too, since

\[
\binom{2n-1}{n-1}=\binom{2n-1}n,
\quad
\binom{2n-1}{n-1}-\binom{2n-1}{n-2}=C_n.                    \tag{3.2}
\]

The coarse class divisibility is

\[
 |{cal M}|=(n+1)C_n,qquad |{cal L}|=|{cal U}|=nC_n,      \tag{3.3}
\]

and (3.1) is the finer coordinate lattice.

There are `4n` evident independent homogeneous real relations: two shore
count relations and two copies of the standard `(2n-1)`-dimensional
coordinate module obtained by subtracting (3.1) for two coordinates.  The
complete catalogue incidence matrices have exactly this nullity over
`F_2,F_3,F_5`, and `F_1000003` at `n=2,3,4`.  This is strong evidence that
there is no additional linear or modular obstruction, but an all-parameter
Smith-normal-form theorem is not claimed here.

The practical absorption warning is exact: a class-balanced arbitrary leave
need not satisfy (3.1).  On the other hand, the leave of **any actual
matching** does satisfy it, because both the complete vector and every
chosen candidate do.

## 4. Robust local expansion

Let `d_S(e)=|e cap S|`.  Double counting and (2.4) give

\[
 \sum_e d_S(e)=D|S|,
\]

and

\[
 \sum_e d_S(e)^2
 =D|S|+2\sum_{\{x,y\}\subset S}\deg(x,y)
 \le D|S|+{2D\over n+1}|S|(|S|-1).                          \tag{4.1}
\]

Cauchy--Schwarz on candidates meeting `S` proves (0.3).  Similarly, for a
fixed resource `v`, the union bound over a forbidden set `S` gives

\[
 \#\{e\ni v:e\cap S=\varnothing\}
 \ge D-\sum_{w\in S}\deg(v,w)
 \ge D\left(1-{2|S|\over n+1}\right),                       \tag{4.2}
\]

which is (0.4).

These estimates are sufficient for bounded local surgery and for choosing
many disjoint constant-size absorbers.  They are not a macroscopic
extendability theorem: (4.2) becomes vacuous after `Theta(n)` forbidden
resources, whereas a cover-down manipulates exponentially many resources.

## 5. A universal candidate-edge absorber

On the six active coordinates `0,...,5`, write sets by concatenating their
elements.  Consider the four paths

\[
\begin{array}{c|cccc}
A&012&123&235&345\\
B&234&134&135&015\\
C&012&123&134&345\\
D&234&235&135&015.
\end{array}                                                   \tag{5.1}
\]

The two paths in each row-pair `{A,B}` and `{C,D}` are resource-disjoint.
Their middle-resource multisets agree.  Their common lower multiset is

\[
                  \{12,23,35,34,13,15\},                     \tag{5.2}
\]

and their common upper multiset is

\[
          \{0123,1235,2345,1234,1345,0135\}.                 \tag{5.3}
\]

Therefore

\[
                         \chi_A+\chi_B=\chi_C+\chi_D.         \tag{5.4}
\]

### Theorem 5.1 (all-parameter embedded trade)

For every `n>=3`, (5.4) embeds in `H_n`; moreover every candidate of
`H_n` can play the role of `A` in such an embedded trade.

#### Proof

Split the remaining `2n-6` coordinates into complementary `(n-3)`-sets
`F,G`.  Adjoin `F` to every state in (5.1), perform the three displayed
active exchanges, and then use the same fixed order to remove `F` and
insert `G`.  The `A,C` tails are identical, as are the `B,D` tails, so all
tail resources cancel across (5.4).  In the active block, adjoining the
same `F` preserves (5.2)--(5.4).  Within each side of the trade the two
small active parts are distinct/complementary, so no resource collision is
introduced.  Every extended path is a length-`n` complement geodesic.

Finally, the coordinate group is transitive on oriented complement
geodesics: map the ordered removal list and ordered insertion list of the
embedded `A` to those of any prescribed candidate.  Reversal handles the
unoriented convention.  `square`

If `T=V(A)`, reserve the one-edge matching `{B}`.  It covers a set disjoint
from `T`; when `T` must be absorbed, replace `{B}` by `{C,D}`.  Hence the
absorber is as small as possible after the flux constraint: one edge versus
two.

This does **not** absorb an arbitrary admissible resource set.  It absorbs a
leave already partitioned into candidate edges.  The gap between those two
statements is exactly the cover-down theorem in Section 0.

## 6. Why no black-box theorem finishes the matching

The exact facts above pass the first tests of an absorption proof, but the
available general theorems do not imply a perfect matching here.

* Frankl--Rödl--Pippenger and Kahn convert a fractional matching with small
  pair load into an almost-perfect integral matching with the rank fixed.
  Here the rank is `3n+1`.  Their qualitative fixed-rank quantifiers cannot
  be evaluated merely from `2/(n+1) -> 0`.
* Quantitative modern nearly-perfect results generally assume a fixed
  uniformity or a power-saving codegree such as
  `Delta_2 <= D^(1-gamma)`.  Here

  \[
                        \Delta_2={2D\over n+1},               \tag{6.1}
  \]

  which fails every fixed power saving because `D` is superexponential in
  `n`.
* Dense perfect-matching theorems require large minimum collective degrees.
  Most pairs in `H_n` have codegree zero, so this is not a dense Dirac
  instance.
* General design-existence theorems keep the pattern ranks fixed while the
  host grows.  Here both the candidate size and the underlying pointed
  wreath grow with `n`.
* Even an almost-perfect matching would not by itself solve the exact row.
  Its leave has the flux identities (3.1), but one still needs to push that
  leave onto the candidate-edge template absorbed by (5.4).

Thus the hypergraph route has not failed; it has reached the same precise
kind of final gate as modern design proofs:

1. structured nibble respecting the sparse high-codegree flags;
2. a vortex or cover-down which makes the final leave candidate-aligned;
3. the explicit two-trades of Theorem 5.1.

Steps 1--2 are a new theorem for this growing-rank pointed-wreath
hypergraph.  Theorem 5.1 means no further absorber search is needed once
edge alignment is proved.

## 7. Independent finite audit

Run

```text
python3 scratch/audit_catalan_agcf_resource_hypergraph_codegrees_lattice_trade_20260731.py
```

It exhausts the complete candidate catalogues at `n=2,3,4` (respectively
`12,360,20160` candidates) and verifies:

* exact regular degree;
* every entry of the pair-codegree table (2.2);
* the sharp maximum (2.4);
* the pathwise flux identities (3.1);
* incidence rank `|V|-4n` over four finite fields; and
* the embedded two-trade for every `3<=n<=8`.

It writes

```text
scratch/catalan_agcf_resource_hypergraph_codegrees_lattice_trade_20260731.audit.json
```

The finite rank and trade audits support, but do not replace, the
all-parameter proofs above.
