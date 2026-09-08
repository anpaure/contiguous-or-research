# An Optimal Eight-Bit Threshold Cover and a General Staircase Transfer

Date: 2026-09-06. Supplemental proof, suffix `c58e2`. The unconditional
coefficient is integrated into `../MASTER_HANDOFF.md`, Appendix A.7, with
a local row compiler that pays all closing positions without a catalogue.

## 1. Results and Status

**Unconditional finite result.** Fourteen products of two ordered
quadruple-prefix chains cover all 256 subsets of an eight-set. Fourteen is
optimal. The explicit witness below is independently verified, not merely
a reported solver status. It is obtained from an archived three-rank factor
by changing only two families.

**Unconditional compiler result.** The half-threshold staircase on `ell`
equal coordinate chains of length `2s` has an explicit symmetric chain
partition of width `s^(ell-1)`, in every `ell,s>=1`. This is proved by
actual chains, not inferred from its rank polynomial.

**Unconditional asymptotic consequence.** The eight-bit cover gives

\[
 \boxed{\nu(k)\le(c_9+o(1))W(k),\qquad
 c_9=\frac{564480\pi^2-1105440\pi^4+723296\pi^6-62475\pi^8}{393216}
 <\frac{118071}{100000}=1.18071.}                       \tag{1}
\]

Here `c_9` is approximately `1.18070380384713`. A simpler, independent
upper evaluation of the same construction is

\[
                  c_9\le\frac{35}{32}\sqrt{3\pi/8}<1.188.         \tag{2}
\]

**Conditional general result.** If optimal `Cat_ell` threshold covers
exist for unbounded `ell`, the same proved compiler yields

\[
                         \nu(k)\le(2/\sqrt3+o(1))W(k). \tag{3}
\]

Existence of that unbounded family is **not proved here**. The canonical
MSW family fails the required off-middle condition. A natural stronger
attempt, using only noncrossing swap matchings in one fixed coordinate
order, is ruled out for every `ell>=3` by a short degree argument below.
These restrictions do not rule out general Dyck-indexed constructions.

The asymptotic transfer in Sections 5--7 uses padding and a line fallback.
It does not assume an unequal-staircase width formula or the numerical
coefficient of the seven-accumulator theorem being audited.

## 2. The Binary Cover Problem

For two ordered disjoint `ell`-tuples
`A=(a_1,...,a_ell)` and `B=(b_1,...,b_ell)` partitioning `[2ell]`, put

\[
 \mathcal F(A,B)=\{A_i\cup B_j:0\le i,j\le\ell\},
 \quad A_i=\{a_1,...,a_i\},\quad B_j=\{b_1,...,b_j\}.  \tag{4}
\]

Equivalently, the membership bits are nonincreasing in each of the two
listed orders. A column has `(ell+1)^2` targets, and its rank polynomial
is `(1+z+...+z^ell)^2`. Its middle rank contains `ell+1` targets.
Consequently every cover needs at least

\[
                         \frac1{\ell+1}\binom{2\ell}{\ell}
                           =\operatorname{Cat}_\ell              \tag{5}
\]

columns. At equality, ranks `ell-1,ell,ell+1` are each covered exactly
once, since a column has respectively `ell,ell+1,ell` targets there.

The middle targets of a column form the complementary Johnson geodesic

\[
                         M_j=A_{\ell-j}\cup B_j,
                              \quad0\le j\le\ell.     \tag{6}
\]

For `q>=1`, its rank-`ell+q` targets are the unions of `q+1`
consecutive vertices of (6); its rank-`ell-q` targets are the
corresponding consecutive intersections. Indeed

\[
 \bigcup_{j=u}^v M_j=A_{\ell-u}\cup B_v,
 \qquad
 \bigcap_{j=u}^v M_j=A_{\ell-v}\cup B_u.               \tag{7}
\]

Thus a three-rank antipodal-geodesic factor is necessary at equality, but
it is not the whole covering requirement.

## 3. A Complete Fourteen-Family Witness

Coordinates are `0,...,7`; strings in the table are ordered quadruples,
not integer masks. Use the following fourteen columns (4):

| Row | A | B |
|---:|---|---|
| 0 | `0461` | `5723` |
| 1 | `0473` | `2651` |
| 2 | `0674` | `3152` |
| 3 | `0726` | `1435` |
| 4 | `1507` | `4263` |
| 5 | `1605` | `7432` |
| 6 | `2104` | `6375` |
| 7 | `2150` | `7463` |
| 8 | `3206` | `7154` |
| 9 | `3210` | `4567` |
| 10 | `3617` | `5204` |
| 11 | `4302` | `6157` |
| 12 | `5034` | `6721` |
| 13 | `5426` | `7301` |

### Exact Coverage Certificate

Taking all 25 prefix unions in each row gives this complete load census:

| Rank | Number of Targets at Each Multiplicity |
|---:|---|
| 0 | 1 at multiplicity 14 |
| 1 | 4 at multiplicity 3; 4 at multiplicity 4 |
| 2 | 14 at multiplicity 1; 14 at multiplicity 2 |
| 3 | 56 at multiplicity 1 |
| 4 | 70 at multiplicity 1 |
| 5 | 56 at multiplicity 1 |
| 6 | 14 at multiplicity 1; 14 at multiplicity 2 |
| 7 | 1 at multiplicity 2; 3 at multiplicity 3; 3 at multiplicity 4; 1 at multiplicity 5 |
| 8 | 1 at multiplicity 14 |

There are no zero loads. This is a finite certificate: the accompanying
dependency-free verifier checks all 256 bit patterns directly using the
two order inequalities, independently of the solver's prefix enumeration.
It also reconstructs all fourteen geodesics and verifies the 70 middle
vertices and both 56-element adjacent palettes.

The total rank occurrence vector is

\[
                         14,28,42,56,70,56,42,28,14.  \tag{8}
\]

Its total is 350, with excess 94 over the 256 distinct targets. At equal
half cuts the continuous excess volume is therefore `94s^8`, or `47/128`
of the whole eight-chain box. This overlap is retained and charged.

The byte encoding consisting of the 112 coordinate labels in table order
has SHA-256

```
31c468fbb9a3e32910c9409c4273af293430da1037bf506f1ed1191856aa3c08
```

### Relation to the Archived Factor

Proposition 3.4 of
`../MATH_THEOREM_CATALAN_INDEPENDENT_FILLER_GUARD_FACTORIZATION_20260731.md`
already supplies fourteen complementary geodesics with exact ranks 3, 4,
and 5. Its complete prefix-product inventory, however, misses masks

\[
                         132=\{2,7\},\qquad
                         246=[8]\setminus\{0,3\}.      \tag{9}
\]

Replace just these two archived paths:

```
39 166 150 154 216        99 195 210 212 156
```

by

```
39 166 150 212 216        99 195 210 154 156.
```

That is, exchange their penultimate middle vertices. In tuple form the
replacement is

\[
\begin{array}{c|c}
\text{old}&\text{new}\\ \hline
(1250\mid7436)&(2150\mid7463)\\
(6105\mid7423)&(1605\mid7432).
\end{array}                                                   \tag{10}
\]

The exact occurrence delta on the whole eight-cube is

\[
 +4+132+219+246+251\ -64-190-191-192-215,              \tag{11}
\]

where a mask in (11) denotes one unit of target multiplicity, not set
addition. Every negative target had old multiplicity at least two:
the old loads were respectively `4,2,4,2,2` for
`64,190,191,192,215`. Thus no old target is lost, and (9) is repaired.
All other twelve archived columns remain unchanged.

Within the two-tuple-column model, two is the minimum number of changed
columns in a nontrivial repair preserving an optimal middle cover.
A complementary geodesic's unordered
middle footprint determines its unique complementary endpoint pair, and
then each vertex's distance from one endpoint determines its order.
The two tuple orders follow from the entering and leaving labels. Hence
one column cannot be replaced by a different column with the same middle
footprint. With all other columns fixed, middle exactness would require
precisely that equality.

### A Reusable Two-Row Identity

Let `x,y,z,t` be four distinct coordinates, and let `F,F'` and `Z,Z'`
be permutations of two further disjoint `(ell-2)`-sets. The substitution

\[
\begin{array}{c|c}
(x,y,F\mid Z,z,t)&(y,x,F\mid Z,t,z)\\
(t,x,F'\mid Z',y,z)&(x,t,F'\mid Z',z,y)
\end{array}                                                   \tag{12}
\]

preserves the complete occurrence multisets at ranks
`ell-1,ell,ell+1`, and preserves the endpoint pairs and each row's swap
matching: it commutes the last two disjoint swaps. Only prefix lengths
one on the first rail and `ell-1` on the second rail change. The two
changed middle targets exchange. The four affected lower targets are
`Z+x,Z+y,Z+z,Z+t` in either arrangement; the affected upper targets are
`Z` together with each of the four three-subsets of `{x,y,z,t}`.
Here `Z,Z'` denote the same underlying set in these three-rank statements.

The orders of the fillers still affect farther ranks. Equation (10) is a
specific instance where their changes repair the remaining holes. This
identity is not a theorem that all far-rank holes of arbitrary factors
can be repaired.

## 4. Actual Staircase Partitions in Every Length

For `ell,s>=1`, define

\[
 \mathcal S_{\ell,s}=
 \{\mathbf x\in[0,2s)^\ell:
       \mathbf1_{x_1\ge s}\ge\cdots\ge\mathbf1_{x_\ell\ge s}\}.
                                                               \tag{13}
\]

Its rank polynomial is indeed

\[
 (1+z+\cdots+z^{s-1})^\ell
       (1+z^s+\cdots+z^{\ell s})
 =\frac{(1-z^{(\ell+1)s})(1-z^s)^{\ell-1}}{(1-z)^\ell}.          \tag{14}
\]

We do not infer a chain partition or a poset isomorphism from (14).
Here is the actual partition.

Start with the chain of all first-coordinate values. Inductively every
current chain `E=(E_0,...,E_{L-1})` has exactly `s` terminal members whose
last coordinate is at least `s`. When adjoining another coordinate, the
allowed points of `E x [0,2s)` form

\[
                     H(L,2s;L-s,s).
\]

For `0<=j<s`, use the explicit chain

\[
 ((E_0,j),\ldots,(E_{L-1-j},j),
         (E_{L-1-j},j+1),\ldots,(E_{L-1-j},2s-1)).     \tag{15}
\]

These are the first `s` outer chains of the rectangle and partition that
hook: the point `(E_i,y)` belongs to the unique chain
`j=min(y,L-1-i)`, and the hook condition makes `j<s`.
Every new chain again has exactly `s` terminal members above the new
cut, so the induction continues.

The numbers of chains and memberships in (13) are respectively

\[
 \boxed{R_{\ell,s}=s^{\ell-1},\qquad
        V_{\ell,s}=(\ell+1)s^\ell}                    \tag{16}
\]

More explicitly, the chains are indexed by
`j_2,...,j_ell in {0,...,s-1}` and have lengths

\[
               2\ell s-(\ell-1)-2\sum_{i=2}^\ell j_i. \tag{17}
\]

Their bottom and top index ranks sum to `ell(2s-1)`. Thus they are
symmetric and all cross the same middle rank. This proves that their
number `s^(ell-1)` is the exact width. Their minimum length is
`2s+ell-1`. Mapping coordinates into ascending set chains on disjoint
supports makes them actual ascending set chains.

For `ell=4`, (16) gives volume `5s^4` and width `s^3`. The fourteen
products in Section 3 therefore have exact equal-side principal charge

\[
                  14\cdot2(5s^4)(s^3)=140s^7
                         =\frac{35}{32}(2s)^7.        \tag{18}
\]

## 5. Padding Transfer and the Line Fallback

This section applies to any verified optimal threshold cover for a fixed
`ell`, not just the eight-bit witness. Write

\[
 m=2\ell,\qquad d=m+1,\qquad
 \alpha_m=\frac{4\binom{2\ell}{\ell}}{4^\ell}\le2.     \tag{19}
\]

For equal lengths `a=2s`, the `Cat_ell` staircase products have principal
charge `alpha_m a^(m-1)`. Every family and every overlap contributes to
this charge.

### Unequal Factors Without a Width Assumption

Given `d` ascending set chains on disjoint supports, set aside a shortest
chain of length `r`. Let the other lengths be
`a_1<=...<=a_m`. Choose the even integer

\[
                       A=2\lceil a_m/2\rceil.
\]

Pad each of these `m` chains to `A` formal positions by repeating its last
member. The product of padded chains maps surjectively onto the actual
product. Apply the verified binary cover and the staircase partitions
(15) in the formal indices. After mapping to actual sets, remove repeated
consecutive members of each chain. The image families cover every actual
target; they may overlap further, which is harmless and is not subtracted
from the cost.

Retain the image chains as an indexed family: all volumes here count
chain memberships with multiplicity. Apply subsequent product SCDs only
after consecutive repetitions have been removed. Padding introduces no
physical coordinates.

For a staircase shore, its number of image chains is at most its formal
count `R`, and their total length is at most its formal volume `V`.
Adjoin the set-aside chain to the first shore of each product using a
complete product SCD. If its image chains are `E`, the new total length
and chain count satisfy

\[
                 V'\le rV,\qquad
                 R'=\sum_E\min(r,|E|)\le rR.           \tag{20}
\]

Consequently the actual paired-rectangle main charge is at most

\[
                         r\alpha_m A^{m-1}.            \tag{21}
\]

This is an actual word upper charge, not normalization by a fictitious
padded volume. Below we always divide by the **actual** product volume
`r prod a_i`.

For a uniform domination, there is a second complete cover. Put one of the
two longest chains on the first shore. Partition the product of the other
`m-1` chains into lines along the second longest chain, fixing every other
coordinate. Adjoin the shortest chain by complete product SCDs as in
(20). Its main charge is at most

\[
                      r(a_m+a_{m-1})\prod_{i=1}^{m-2}a_i.         \tag{22}
\]

Choose the construction with the smaller displayed integer upper charge.
In the continuum, the resulting normalized upper function is

\[
 \boxed{\Phi_m(\mathbf y)=
    \min\left\{\frac{\alpha_m y_m^{m-1}}{\prod_i y_i},
                         \frac1{y_m}+\frac1{y_{m-1}}\right\},
       \qquad0<y_1\le\cdots\le y_m.}                 \tag{23}
\]

It is continuous, homogeneous of degree minus one, and satisfies

\[
         \Phi_m(a,...,a)=\alpha_m/a,\qquad
                          \Phi_m(\mathbf y)\le2/y_1.  \tag{24}
\]

The fallback is important: the padded expression alone has no useful
uniform reciprocal domination when the lengths are far apart.

### Literal Positions and Every Closing

For a strict ascending set chain `C=(C_0,...,C_{q-1})` on support `U`, use

\[
 \beta_U(C)=(C_0,C_1\setminus C_0,...,
                    C_{q-1}\setminus C_{q-2},U\setminus C_{q-1}),
                                                               \tag{25}
\]

with empty letters deleted. Prefixes realize `C`; suffixes realize its
complements. For a terminal paired rectangle `(C,D)` on complementary
supports `U,V`, put both directed arcs between `(U,C)` and `(V,D^c)`,
where `D^c` is increasingly ordered. The two bridge boundaries realize
`C x D` and its full complement by literal suffix/prefix unions.

Euler-assemble each connected component and include one closing bridge.
If `M` is the sum of the actual strict chain lengths over terminal paired
rectangles, `E` is their number, and `V_cat` counts possible bridge vertices,
then

\[
                     |W|\le M+2E+(K+1)V_{\rm cat}.     \tag{26}
\]

Repetitions removed after padding can reduce `M`; they cannot make it
exceed (21). No uncharged initialization or row closing is used.

## 6. General Accumulator Transfer

Fix `ell` and a verified optimal binary cover. Fix another integer `n>=d`
and split `K=nh` coordinates into `n` pivoted blocks. Take an SCD in each
block minus its pivot, use the `2^(n-1)` signed complementary product pairs,
and keep all their members. This is the usual exact ownership partition:
the pivots choose the signs and global complement, and the SCDs choose the
chain owners.

Put the first `d=2ell+1` chains in labeled accumulators. Read the remaining
chains in their fixed order. Merge the next chain into a currently shortest
accumulator by a complete product SCD, retaining every child and continuing
at every child. The choice of accumulator does not inspect the unread
chain's length. At the terminal `d`-tuple, use the smaller of (21)-(22),
then compile all terminal rectangles by (26).

For fixed `n,ell`, put `L=sum a_i` at an initial tuple. Every merge has
at most `L` children. Each terminal construction has `O_ell((L+1)^(d-2))`
paired rectangles and main charge `O_ell((L+1)^(d-1))`. Thus the full
initial tuple has `O_{n,ell}((L+1)^(n-2))` terminal pairs and
`O_{n,ell}((L+1)^(n-1))` main charge. SCD moment bounds give

\[
                        E=O_{n,\ell}(2^{nh}/h)=o(W(nh)).           \tag{27}
\]

Every bridge has support in a proper union of original blocks. For fixed
`n,ell`, its construction is specified by finitely many grouping choices,
its input chains and signs, and a bounded number of integer child indices.
Padding requires one additional integer `A<=nh+1`; it does not require a
new arbitrary chain order. Thus a catalogue bound of the form

\[
          V_{\rm cat}\le C_{n,\ell}(nh+1)^{C_{n,\ell}}
                                      2^{(n-1)h}                 \tag{28}
\]

is sufficient. Equations (26)-(28) charge every nonprincipal position at
`o(W(nh))`. Both the leading overlap and the extra padding are included in
the main upper charge.

### Volume Bias and the Limiting Kernel

An initial SCD chain length divided by `sqrt(h)`, when sampled with weight
equal to its length, converges to

\[
              Z\sim\chi_3,
        \qquad g(z)=\sqrt{2/\pi}\,z^2e^{-z^2/2}.        \tag{29}
\]

This follows from the standard chain inventory
`binom(h-1,i)-binom(h-1,i-1)`: the unweighted limit is Rayleigh, and
length bias produces (29). Complete product SCD children have lengths
`|a-b|+1, |a-b|+3,...,a+b-1` and sum of lengths `ab`. Hence a
volume-biased child has continuum kernel

\[
                 K(a,b;dt)=\frac{t}{2ab}
                                 \mathbf1_{|a-b|<t<a+b}\,dt.     \tag{30}
\]

No volume bias is taken after the overlapping terminal cover or after
padding. Its charge is divided by the actual pre-cover volume, as in
(23).

Run the same `d`-slot minimum-update process on `n` inputs `Z/sqrt(n)`
with kernel (30), and let `Y_{1,n}<=...<=Y_{m,n}` be the largest `m=d-1`
final radii. The fixed-`n` word bound has principal upper limit

\[
              Q_{n,\ell}=\sqrt{\pi/8}\,
                              \mathbb E\Phi_m(Y_{1,n},...,Y_{m,n}).
                                                               \tag{31}
\]

Let `P` be the sum of the smaller numerical upper bounds (21)-(22) over
all complete-SCD branches of an initial tuple. It bounds the actual main
charge even when padding collapses repeated sets. To check the
normalization, the signed main upper charge is exactly
`2^(nh-1) E_volume[P/prod a_i]`, and

\[
                   \frac{2^{nh-1}}{\sqrt h\,W(nh)}
                                  \longrightarrow\sqrt{\pi n/8}.
\]

The extra `1/sqrt(n)` scaling and degree minus one in (23) give (31).
These are fixed-`n,ell` limits. The even rounding changes `A` by at most
one and its terminal charge by `O_ell((L+1)^(m-1))`, one degree below the
main term. After scaling it disappears. The limiting unweighted terminal
upper function is the minimum of `r alpha_m (max a_i)^(m-1)` and the
polynomial in (22); it is continuous, including at zero lengths, and
homogeneous of degree `d-1`.
Subsequent mesh-two sums are ordinary half integrals. Ties between shortest
slots give the same numerical length multiset. Polynomial domination and
the Gaussian SCD tails justify the Riemann limits without assuming a rate
uniform in `n` or `ell`.

### Balancing All But the Active Minimum

For clarity, the probabilistic limit used here can be checked directly.
Take `d` independent standard three-dimensional Brownian paths, each with
its own mesh clock. At each of `n` updates advance a currently shortest
path by time `1/n`. The first `d` updates seed distinct paths almost surely.
The next unrevealed increment is an independent `N(0,I_3/n)` vector.
Its norm and its uniform angular cosine give exactly (29)-(30).

Let `omega_n` be the largest continuous vector increment over any one
mesh interval of any of the `d` paths on `[0,1]`. Let `A_n` be the
largest current radius, `B_n` the second smallest, and `H_i` each path's
largest sampled radius so far. Minimum updates imply

\[
 A_n=\max_i H_i,\qquad A_n-B_n\le\omega_n,
                      \qquad A_n-\omega_n\le H_i\le A_n.          \tag{32}
\]

Indeed the untouched `d-1` radii already have spread at most `omega_n`;
a new value entering that group is at most the old minimum plus
`omega_n`. At the update attaining the eventual maximum, every old radius
was at least that maximum minus `omega_n`, proving the history bound.

Let `tau_i(a)` be first hitting time of radius `a`, put
`sigma(a)=sum_i tau_i(a)`, and set

\[
                       A=\sup\{a:\sigma(a)\le1\}.      \tag{33}
\]

First hitting times are strictly increasing and left-continuous in the
level. By (32), each path has reached `(A_n-omega_n)_+` by its allocated
time, and its continuous past has not reached `A_n+2omega_n`. Clock
times sum to one, so

\[
 \sigma((A_n-\omega_n)_+)\le1<\sigma(A_n+2\omega_n),
        \qquad Y_{i,n}\longrightarrow A\quad\text{a.s.}           \tag{34}
\]

If `tau` is first exit from the unit ball in dimension three and
`S_d=tau_1+...+tau_d` for independent copies, scaling gives

\[
                         A^{-2}\overset d=S_d,
                         \qquad\mathbb E S_d=d/3.      \tag{35}
\]

The mean follows by stopping `|W_t|^2-3t`; stopping at `tau wedge t`
first also proves integrability. The exact inverse event is
`A<a iff sigma(a)>1`. Fixed-level hitting times have no atoms, since
hitting exactly at a fixed time places a Gaussian vector on a sphere.

Here is explicit reciprocal control. The exit-time mean from any point in
the unit ball is at most `1/3`. The Markov property in blocks `2/3` gives
`Pr(tau>=t)<=2^(-floor(3t/2))`. A reflection bound gives

\[
 \Pr(\omega_n>\epsilon)\le12dn e^{-n\epsilon^2/6},
 \qquad
 \Pr(A\le r)\le d\,2^{-\lfloor3/(2dr^2)\rfloor}.       \tag{36}
\]

The second smallest radius never decreases under minimum updates. After
the first `d` updates the radii are independent `chi_3/sqrt(n)`; since
`E chi_3^(-2)=1`, one has `E B_n^(-2)<=dn`.
For `epsilon=n^(-1/4)`, on
`G_n={omega_n<=epsilon,A>6epsilon}` equations (24) and (34) give
`Phi_m(Y_n)<=4/A`, an integrable domination. On the complement the
expectation is at most

\[
 2\sqrt{dn\Pr(G_n^c)},\qquad
 \Pr(G_n^c)\le12dn e^{-n\epsilon^2/6}
                     +d\,2^{-\lfloor1/(24d\epsilon^2)\rfloor},
\]

which tends to zero at fixed `d`. Therefore

\[
 \boxed{Q_{n,\ell}\longrightarrow
     c_\ell^{\rm th}:=\alpha_{2\ell}\sqrt{\pi/8}\,
                                 \mathbb E\sqrt{S_{2\ell+1}}.}    \tag{37}
\]

This controls the actual reciprocal, not just a weak limit.

For each fixed `ell`, choose the shortest candidate over all
`d<=n<=floor(sqrt(k))`, with block size `floor(k/n)`. For a word `w` of
length `N`, adjoining a fresh coordinate `p` by `w, {p}, w^{+p}` preserves
old targets and realizes every old nonempty target with `p` adjoined. Its
length is `2N+1`. After `t<n` splices the length is `2^t(N+1)-1`, and
`2^t W(nh)/W(nh+t)->1` for each fixed `n`. Use the all-subsets word when
the candidate range is empty. Every fixed `n` is eventually available.
Equations (26)-(37)
therefore give `nu(k)<=(c_ell^th+o(1))W(k)` in every dimension whenever
that particular finite threshold cover is verified.

## 7. The New Nine-Accumulator Coefficient

For the explicit eight-bit template, `alpha_8=35/32` and `d=9`.
The exit-time transform is

\[
                    \mathbb E e^{-s\tau}
                           =\frac{\sqrt{2s}}{\sinh\sqrt{2s}}.
\]

It follows from the regular radial solution of `u''/2+u'/r=s u` with
`u(1)=1`, evaluated at zero; stopping that solution at the exit time
justifies the transform. Tonelli and `x=sqrt(2s)` give

\[
 c_9=\frac{35}{64}I_9,\qquad
 I_9=\int_0^\infty\left(\frac1{x^2}-\frac{x^7}{\sinh^9x}\right)dx.
                                                               \tag{38}
\]

For an exact evaluation, let `f=csch x` and `D=d/dx`. Repeated use of
`(csch^p x)''=p^2 csch^p x+p(p+1)csch^(p+2)x` gives

\[
 \operatorname{csch}^9x=
        \frac{D^8-84D^6+1974D^4-12916D^2+11025}{40320}f.         \tag{39}
\]

Integrate against `x^7` on `[epsilon,infinity)` by parts. The eighth
derivative contributes `1/epsilon+O(epsilon)` after division by 40320.
All other boundary terms vanish. There is no hidden finite boundary term:
`csch x` has an odd Laurent expansion, and the only nonvanishing boundary
power here is `epsilon^(-1)`. If
`J_q=int_0^infinity x^q/sinh x dx`, the remaining terms give

\[
                  I_9=\frac{21}{2}J_1-\frac{329}{8}J_3
                             +\frac{3229}{240}J_5-\frac{35}{128}J_7.
                                                               \tag{40}
\]

The nonnegative exponential expansion of `csch x` and the even-zeta
evaluations give

\[
             J_1=\pi^2/4,\quad J_3=\pi^4/8,\quad
             J_5=\pi^6/4,\quad J_7=17\pi^8/16.
\]

For example, the last uses `zeta(8)=pi^8/9450`, which also follows by
Parseval applied to `x^4`, after the evaluations for powers two, four,
and six. Substitution in (38)-(40) proves (1).

The rational certificate uses Machin's identity with 40 alternating
arctangent terms at `1/5` and eight at `1/239`. The resulting rational
pi enclosure, with signs treated separately in the polynomial, proves

\[
        1.1807038038<c_9<1.1807038039<1.18071.          \tag{41}
\]

All comparisons in (41) use `Fraction` arithmetic. Independently,
floating-point quadrature of (38) agreed within `1e-12`; that diagnostic
is not used for the inequality. Jensen in (35) already proves (2), so
the construction improves the previous seven-accumulator coefficient even
without evaluating the cancellation-sensitive polynomial.

## 8. What the General Catalan Construction Would Give

The staircase compiler is unconditional in every `ell`. If optimal
threshold covers exist for unbounded `ell`, (37) yields the sequence

\[
 c_\ell^{\rm th}
 =\frac{4\binom{2\ell}{\ell}}{4^\ell}\sqrt{\pi/8}\,
                                      \mathbb E\sqrt{S_{2\ell+1}}.
\]

Stirling gives `binom(2ell,ell)/4^ell ~ 1/sqrt(pi*ell)`.
The exit time has an exponential tail, so the law of large numbers and
uniform integrability give
`E sqrt(S_d/d) -> 1/sqrt(3)`. Hence

\[
                         c_\ell^{\rm th}\longrightarrow2/\sqrt3.
                                                               \tag{42}
\]

The order of limits is fixed `ell`, then fixed `n` word limits in `h`,
then `n -> infinity`, and finally verified template sizes `ell -> infinity`.
A finite shortest-candidate construction implements the corresponding
diagonal selection. No uniform large-rank matching theorem is hidden in
(42).

**The unproved antecedent is the binary cover itself for unbounded
`ell`.** It is not supplied by the rank polynomial, the staircase SCD,
or the known MSW middle factor.

## 9. Existing Facts and Tested General Routes

### Why Canonical MSW Is Insufficient

The repository's MSW/Catalan wreath and complementary-geodesic notes supply
the middle partition and upper adjacent palette, not the full condition
(4). The prefix-product dictionary (7) makes the distinction exact.
Direct inventories of the canonical construction give:

| ell | Families | Total Holes | Holes at Rank ell-1 |
|---:|---:|---:|---:|
| 2 | 2 | 0 | 0 |
| 3 | 5 | 2 | 2 |
| 4 | 14 | 19 | 12 |
| 5 | 42 | 118 | 54 |
| 6 | 132 | 623 | 222 |

The failure at the lower adjacent rank is hereditary. For a Dyck suffix
`V` of semilength `ell-3`, let `T` be its set of one-coordinates, shifted
by six. The canonical roots `111000V` and `110100V` begin with middle
owners

\[
 (7+T,37+T,41+T),\qquad(11+T,35+T,49+T),              \tag{43}
\]

where `+T` denotes union with the disjoint spectator set. Both second
lower intersections are `33+T`. This follows directly from the canonical
flip-permutation recursion and its concatenation on Dyck factors. Different
suffixes give distinct repeated targets. There are exactly
`ell Cat_ell=binom(2ell,ell-1)` lower occurrences, so canonical MSW misses
at least `Cat_(ell-3)` lower targets for every `ell>=3`.

This is the existing hereditary obstruction, reproduced here in the
threshold-cover dictionary. The archived lower-turn and all-width MSW
notes already warn against inferring the needed simultaneous cover.

### A General Obstruction to Noncrossing Swap Matchings

There is also a short obstruction to assigning the Catalan columns only
noncrossing swap matchings in a fixed circular coordinate order.

More generally, suppose all swaps in an optimal cover cross one fixed
balanced bipartition `U dotcup V`, `|U|=|V|=ell`. Middle exactness makes
the middle set `U` a vertex of only one selected geodesic. For every
`x in U`, the lower target `U-{x}` must be an intersection of an adjacent
middle pair. A swap crossing `U,V` and having that intersection must add
the only available `U`-coordinate `x` on one endpoint; hence that endpoint
is exactly `U`. The `ell` distinct lower targets therefore require `ell`
distinct selected edges incident to `U`, whose path degree is at most two.
This is impossible when `ell>=3`.

Every noncrossing perfect matching on a fixed cyclically ordered `2ell`-set
joins opposite position parities: either open arc between matched endpoints
contains an even number of vertices. Thus it has exactly the forbidden
common balanced bipartition. At the optimal `Cat_ell` column count, the
proposed noncrossing-swap construction therefore fails for all `ell>=3`,
even if noncrossing matchings may be reused in different columns.
This obstruction is to the optimal count; it does not exclude covers
using more than `Cat_ell` columns.

This does **not** rule out indexing a successful construction by Dyck
objects while using different, crossing swap matchings. It rules out the
specific geometric identification of the row's swaps with a noncrossing
matching.

The exact solver corroborated this at `ell=3,4` using respectively 120 and
2,688 columns and one column per noncrossing matching. A fractional packing
relaxation even gave exactly verified rational dual values `13/3<5` and
`13<14`. The degree proof above is stronger in scope and does not depend
on these solver outcomes.

### A Small Cyclic Attempt

An exhaustive test also excluded a fourteen-column cover invariant under
a seven-cycle on seven coordinates fixing the eighth. All 20,160 columns
have orbit seven, so such a cover would comprise two orbits. Covering the
fixed-coordinate singleton and co-singleton requires one orbit with that
coordinate first in its tuple and another with it last. Of 2,880 column
orbits, 564 are internally simple on the three tight ranks; no
endpoint-compatible pair has complementary tight-rank footprints.
This is a finite, scoped exclusion of that two-orbit symmetry, not of the
unrestricted fourteen-column cover already exhibited.

No general Dyck/Catalan construction of the required all-rank covers has
been established in this work. The two-row identity (12) supplies a legal
far-rank adjustment inside a tight three-rank factor, but no global
availability or termination theorem for such adjustments is asserted.

## 10. Reproduction

Only these uniquely named scratch files were added:

- `catalan_threshold_cover_20260906_c58e2.py`: explicit witness, MSW comparison, two-row identities, complete finite-column model, and scoped symmetry experiments.
- `eight_threshold_staircase_verify_20260906_c58e2.py`: independent truth-table/geodesic verification, actual staircase partitions, padding/line compilers, and the exact constant certificate.
- This proof note.

The dependency-free checks are

```sh
python3 -B scratch/catalan_threshold_cover_20260906_c58e2.py
python3 -B scratch/eight_threshold_staircase_verify_20260906_c58e2.py
```

The positive exact model has one Boolean variable for every one of the
`8!/2=20160` columns, requires fourteen selected columns, and imposes
coverage on all 256 targets. The three tight ranks are constrained to
load exactly one, which follows from optimal cardinality and is not an
extra assumption. An unrestricted run was feasible; an archive-assisted
run with at least eleven old columns retained found the displayed solution
retaining twelve. With OR-Tools installed, the latter can be rerun using

```sh
python3 -B scratch/catalan_threshold_cover_20260906_c58e2.py \
  --solve --l 4 --seconds 120 --keep-at-least 11
```

Solver trajectories may differ; the explicit witness is fixed and its
independent verification has no solver dependency.

Observed additional checks include 18 actual staircase partitions through
`ell=6`, 120 general two-row trades, 65 hereditary MSW collision instances,
100,000 nine-slot invariant checks, and 120 exact volume-normalization tests.
Both padding and fallback branches were checked by all required literal
interval unions. One deliberately unequal padded instance had formal
principal bound 17,920 but actual strict-chain main charge 17,408;
the reduction is charged correctly, rather than treating the formal
padding as extra physical coordinates.

The full-cube word checks gave:

| Blocks | Dimension | Word Length | Actual Main | Endpoint Letters | Closing Letters |
|---|---:|---:|---:|---:|---:|
| nine 2s | 18 | 84,980 | 71,680 | 13,216 | 84 |
| ten 2s | 20 | 535,752 | 399,360 | 136,304 | 88 |
| eight 2s and one 3 | 19 | 263,824 | 199,680 | 64,056 | 88 |
| seven 2s and two 3s | 20 | 532,475 | 393,216 | 139,248 | 11 |

Every nonempty target was checked by actual interval unions. These words
test the compiler and all closing costs; they are not finite-optimum
improvements. The unconditional improvement is the asymptotic theorem (1).

An independent proof audit checked the all-rank template, padding with
indexed multiplicities, absorption, Brownian reciprocal limit, exact integral,
and all-dimension conclusion. The checker was corrected to allow a strict
chain containing both empty and full endpoints: its bridge can have one
fewer letter than chain members. A new unpivoted nine-factor regression
checks that case, and a separate literal row assembler checks the local
closing ledger used in the integrated proof. Neither correction changes
the asymptotic coefficient.

The integrated local-row proof also passed a separate audit. Direct
per-terminal, per-family row words, without global Euler assembly, were
independently checked in dimensions 18, 20, and 22, with lengths 105,952,
676,072, and 2,374,344. All interval unions were verified. Their main
charges were 71,680, 399,360, and 1,400,832, respectively, and every
remaining position fits the displayed row overhead. These checks are
corroboration of the general proof, not finite-optimum claims.
