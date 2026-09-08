# Six Staircase Factors and Seven Accumulators Give a Coefficient Below 1.1883

Date: 2026-09-06. New scratch work only, suffix `91bc7`.

## 1. Result

Let `W(k)=binom(k,floor(k/2))`, and let `nu(k)` be the minimum length of a
nonzero set-word realizing every nonempty subset of `[k]` by a nonempty
contiguous interval union. Then

\[
 \boxed{\nu(k)\le(c_{\rm st}+o(1))W(k),\qquad
 c_{\rm st}=
 \frac{225\pi^6-2590\pi^4+4200\pi^2}{4608}
 <\frac{11883}{10000}=1.1883.}                         \tag{1}
\]

The exact constant is approximately `1.18822944031087`. Even without the
integral evaluation, the same construction proves the simpler bound

\[
 \boxed{c_{\rm st}\le\sqrt{\frac{175\pi}{384}}<1.197.} \tag{2}
\]

The new terminal object is a cover of a **six-chain product by five products
of two three-chain staircases**. At six equal lengths `a=2s`, its exact
principal charge is `5a^5/4=40s^5`. A seventh chain is absorbed into one
shore with at most a proportional increase in principal charge. Seven
minimum-updated accumulators make the other six asymptotically equal.

This is distinct from a four-accumulator/four-hook calculation and from an
audit of the three-accumulator theorem. Existing ingredients reused are the
pivot ownership partition, complete product-SCD kernel, and Euler bridge
compiler. The new ingredients are the six-factor threshold cover, its
staircase chain decompositions, the seventh-factor absorption bound, and the
resulting seven-clock coefficient. The required analytic and literal
arguments are given below rather than inferred from a rank profile.

There is a leading overlap of one quarter of the six-factor volume at
equal half cuts. It is retained and fully charged. No partition theorem,
independent coupon sampler, or growing-rank matching theorem is used.
Coefficient one and finite optimality are not claimed.

## 2. Five Threshold Products

Given six bits `b_0,...,b_5`, let an ordered triple `(i,j,l)` impose

\[
                         b_i\ge b_j\ge b_l.            \tag{3}
\]

Take the following five pairs of triples:

| Family | First Triple | Second Triple |
|---:|---|---|
| 0 | `(0,1,2)` | `(3,4,5)` |
| 1 | `(1,2,4)` | `(3,5,0)` |
| 2 | `(1,4,3)` | `(5,2,0)` |
| 3 | `(0,4,1)` | `(2,3,5)` |
| 4 | `(4,2,3)` | `(5,0,1)` |

### Lemma 2.1

Every six-bit pattern satisfies both triple conditions in at least one row.
Every pattern of weight two, three, or four satisfies exactly one row.
Five is the minimum possible number of products of two ordered
three-coordinate threshold chains covering all patterns.

**Proof.** For ordered triples `(a,b,c)` and `(d,e,f)`, the supported
two-sets are `ab,ad,de`, and the supported three-sets are
`abc,abd,ade,def`. The complements of the supported four-sets are
`cb,cf,fe`. For the displayed five rows these lists are:

| Family | Two-Sets | Three-Sets | Complements of Four-Sets |
|---:|---|---|---|
| 0 | `01,03,34` | `012,013,034,345` | `12,25,45` |
| 1 | `12,13,35` | `124,123,135,035` | `24,04,05` |
| 2 | `14,15,25` | `134,145,125,025` | `34,03,02` |
| 3 | `04,02,23` | `014,024,023,235` | `14,15,35` |
| 4 | `24,45,05` | `234,245,045,015` | `23,13,01` |

The columns exhaust respectively all 15 pairs, 20 triples, and 15 pairs
without repetition. Singletons supported by a row are its two first
coordinates; the five rows include every coordinate. The missing coordinate
of a supported five-set is one of the row's two last coordinates; these also
include every coordinate. Both constant patterns occur in every row.
This proves coverage. Each such product contains only four three-sets, so
covering all 20 requires at least five rows.

The exact rank occurrence inventory is

\[
                         5,10,15,20,15,10,5.           \tag{4}
\]

For actual ascending chains of lengths `a_i`, choose cuts `0<=u_i<=a_i`
and put `b_i=1_{x_i>=u_i}` at an index tuple. Lemma 2.1 therefore covers
the **actual product of chains**, for every choice of the cuts.

### Exact Overlap

The constant patterns have multiplicity five. Singletons and co-singletons
at the four coordinates `L={0,1,3,5}` have multiplicity two; all other
nonconstant patterns have multiplicity one. Thus the excess volume is

\[
\begin{split}
 4\left(\prod_i u_i+\prod_i(a_i-u_i)\right)
 +\sum_{i\in L}\left((a_i-u_i)\prod_{j\ne i}u_j
                   +u_i\prod_{j\ne i}(a_j-u_j)\right). \tag{5}
\end{split}
\]

At half cuts it equals `prod(a_i)/4`. In particular, the main charge below
does not treat these five products as a partition.

## 3. Explicit Staircase Chains

For lengths `a,b` and cuts `u,v`, the directed hook is

\[
 H(a,b;u,v)=\{(x,y):0\le x<a,\ 0\le y<b,
                              \ x\ge u\text{ or }y<v\}.
\]

Here is an explicit chain partition, also useful for unequal cuts.
The standard outer chains of the whole rectangle are

\[
 C_j=((0,j),\ldots,(a-1-j,j),
               (a-1-j,j+1),\ldots,(a-1-j,b-1)),
 \quad 0\le j<\min(a,b).                               \tag{6}
\]

They have lengths `a+b-1-2j` and partition the rectangle. Put
`h=a-u` and `p=min(h,v)`. Retain the first `p` outer chains. If `h>v`,
the remainder of the hook is the rectangle

\[
                       [u,a-v)\times[v,b);
\]

if `v>h`, it is

\[
                       [0,a-h)\times[h,v).
\]

Partition that remaining rectangle by translated copies of (6). This
partitions the hook into exactly

\[
                  \max\{\min(a,v),\min(a-u,b)\}        \tag{7}
\]

chains. For the construction below the partition, not an abstract width
claim, is what is used.

### A General Balanced Path

Let `v_1,...,v_{d+1}` be positive integers, set
`a_i=v_i+v_{i+1}`, and cut coordinate `i` at `v_i`. Consider the staircase

\[
 \mathcal S_d=\{\mathbf x:\mathbf1_{x_1\ge v_1}
             \ge\cdots\ge\mathbf1_{x_d\ge v_d}\}.     \tag{8}
\]

### Lemma 3.1

The staircase has an explicit symmetric chain partition with

\[
 \boxed{R_d=\prod_{i=2}^d v_i,\qquad
        V_d=R_d\sum_{i=1}^{d+1}v_i.}                  \tag{9}
\]

Its chains, indexed by `0<=j_i<v_i` for `2<=i<=d`, have lengths

\[
             \sum_{i=1}^d a_i-(d-1)-2\sum_{i=2}^d j_i. \tag{10}
\]

In particular `R_d` is the exact width, not just a bound.

**Proof.** Start with the first coordinate chain. Its terminal segment
above its cut has length `v_2`. Inductively, suppose each current chain has
a terminal segment of length `v_i` above the cut of its last coordinate.
Joining coordinate `i`, the required condition is a hook on that chain
and the new coordinate chain. Its right-strip width and bottom-strip
height are both `v_i`. Its partition is therefore precisely the first
`v_i` outer chains (6), with no surplus rectangle. Each resulting chain
has a terminal segment of length `a_i-v_i=v_{i+1}` above the new cut.
This proves the induction and the index set in (10).

Every hook step is a disjoint partition and consists of literal increasing
index tuples. Thus the final chains partition (8). Their bottom ranks are
`sum j_i`, their top ranks are `sum(a_i-1)-sum j_i`, and hence they are
symmetric and all cross the same middle rank. Counting chains proves the
width statement. Summing (10) gives (9).

At three equal lengths `a=2s`, with half cuts, this specializes to

\[
 \boxed{V_3=4s^3=a^3/2,\qquad R_3=s^2=a^2/4.}        \tag{11}
\]

The shortest such chain has length `2s+2=a+2`.

### Arbitrary Three-Factor Inputs

For lengths `(a,b,c)` and cuts `(u,v,z)`, first partition
`H(a,b;u,v)` as above. In a resulting chain `E`, let `t_E` be its number
of points with second coordinate at least `v`. Those points are a terminal
segment. Join the third coordinate using

\[
                  H(|E|,c;|E|-t_E,z).                 \tag{12}
\]

This is an explicit chain partition of `b_1>=b_2>=b_3`, at arbitrary
lengths and cuts. Its volume is exactly

\[
                    V=avz+(a-u)(b-v)c.                \tag{13}
\]

The partition may also be applied to the reversed, complemented three axes
and transported back. Take the partition with fewer chains, breaking ties
by the first choice. No minimum-width assertion is needed for unequal cuts.

For reference, its continuum chain-count formula is explicit. Define

\[
 \Gamma(a,b,c)=xy-\tfrac14(x+y-z)_+^2,
 \quad x\le y\le z\text{ the sorted }a,b,c,
\]

\[
 F_p(a,b,w)=pw-\tfrac14\{(w-a-b+2p)_+^2-(w-a-b)_+^2\}.
                                                               \tag{14}
\]

Write `h=a-u`, `p=min(h,v)`, and `w=max(z,min(b-v,c))`. The forward
partition has leading chain count

\[
 R^{\to}=F_p(a,b,w)+
 \begin{cases}
   \Gamma(h-v,b-v,c),&h\ge v,\\
   \Gamma(a-h,v-h,z),&h<v.
 \end{cases}                                            \tag{15}
\]

Indeed, each retained outer chain has length `a+b-1-2j` and high segment
`b-v`, so (12) uses `min(a+b-1-2j,w)` chains. The surplus rectangle is
either wholly high or wholly low. Its product with the third coordinate is
respectively a full three-box or a three-box with third length `z`.
The mesh-two sums give (14)-(15). Take the smaller of this formula and
its reversed-complemented counterpart to define `R`.

These functions are continuous and homogeneous of degrees three for
volume and two for chain count. The integer formula differs from its
scaled continuum version by `O((a+b+c+1))` in chain count, with the
usual corresponding `O((a+b+c+1)^2)` volume error from rounding cuts.
There are only finitely many min/max pieces, so the estimates are uniform.

## 4. Six-Factor Main Charge

Use the five rows in Section 2, with a common cut on each axis. For an
ordered triple `I`, let `V_I,R_I` be its staircase volume and the number
of chains in the selected explicit partition. Put

\[
 P_6(\mathbf a)=\sum_{(I,J)\text{ in the five rows}}
                         (V_I R_J+R_I V_J),             \tag{16}
\]

using half cuts `floor(a_i/2)` in the integer construction. In the
continuum use exactly `a_i/2`; denote the homogeneous degree-five
continuum expression by `p_6` and put

\[
                         T_6(\mathbf a)=p_6(\mathbf a)/\prod_i a_i.
                                                               \tag{17}
\]

Equation (11) proves the key identity

\[
 \boxed{P_6(a,a,a,a,a,a)=5a^5/4\quad(a\text{ even}),\qquad
        T_6(a,a,a,a,a,a)=\frac5{4a}.}                   \tag{18}
\]

For comparison, the paired middle width of six equal long chains is
`(11/10+o(1))a^5`. Thus the local principal charge divided by that
paired width tends to `25/22`, approximately `1.13636`. The plain
three-versus-three full-box compiler charges `(3/2+o(1))a^5`.

There is also a useful domination. The first hook partition uses at most
`min(a,b)` chains; every subsequent hook in (12) uses at most `c`.
Thus a triple's chain count is at most `c min(a,b)`. At half cuts its
continuum volume is `abc/2`. Consequently

\[
        0\le T_6(\mathbf a)\le\frac5{\min_i a_i}.       \tag{19}
\]

The six-factor cover itself does not require equal lengths. Equality is
used only to evaluate its terminal limiting charge.

## 5. Absorbing a Seventh Factor

Let `C` be another ascending chain of length `r` on a disjoint support.
In each of the five products, replace its first staircase chain partition
`E` by complete product SCDs of `E x C`. The other staircase partition
`D` is unchanged. If the first staircase has volume `V` and `R` chains,
the new first family has volume `rV` and chain count

\[
                     R'=\sum_E\min(|E|,r)\le rR.      \tag{20}
\]

Therefore its actual paired-rectangle principal charge satisfies

\[
 \boxed{P_7(r,\mathbf a)\le rP_6(\mathbf a).}          \tag{21}
\]

This inequality holds for every positive integer `r`, not just for a
small one. It is a comparison of fully specified chain partitions. The
new product SCD children are all retained, so there is no lost seventh-axis
coverage. After division by total product volume, the upper charge in
(21) is independent of `r`.

For six equal even lengths `a` and `r<=a`, equality holds in (21), because
the staircase chains in (11) have length at least `a+2`. This supplies
additional finite checks, but only the inequality is needed below.

### Literal Boundaries

For an ascending set chain `E=(E_0,...,E_{t-1})` on `U`, use

\[
 \beta_U(E)=(E_0,E_1\setminus E_0,\ldots,
              E_{t-1}\setminus E_{t-2},U\setminus E_{t-1}),        \tag{22}
\]

deleting empty letters. Prefix unions realize `E`, suffix unions realize
its complements in `U`, and the bridge has at most `t+1` letters.

For a terminal pair `(C,D)` on complementary supports `U,V`, put both
directed arcs between bridge vertices `(U,C)` and `(V,D^c)`, where
`D^c=(V\D)` is ordered increasingly. At the boundary `D^c -> C`, a suffix
and a prefix realize `X union Y`, `X in C,Y in D`. At the reverse boundary
they realize its full complement. These are actual contiguous intervals.
An empty piece of a witness is simply omitted; both pieces are empty only
for the unrequired empty target.

Collect all terminal pairs as a directed multigraph. In each connected
component take an Euler circuit and output the bridge of each successive
vertex, including one closing copy of the first bridge. With `E` terminal
paired rectangles, main charge `M=sum(|C|+|D|)`, and at most `V_cat`
bridge vertices, the full word obeys

\[
                  N\le M+2E+(k+1)V_{\rm cat}.         \tag{23}
\]

Every overlap and every parallel edge is charged. No witness must cross a
component join. In particular (16) and (21) are not substitutes for unpaid
row closings; (23) pays all such positions globally.

## 6. The Finite Policy

Fix an integer `n>=7` first, and split `nh` coordinates into `n` blocks
of size `h`. In each block choose one pivot and a Boolean SCD on the
remaining `h-1` coordinates. For each tuple of chains and each of
`2^(n-1)` sign patterns, fixing the first sign, pair the signed product
with its full complement. A negative factor is a reversed blockwise
complemented chain.

These paired products partition the cube: the first pivot chooses global
complementation, the other pivots choose the remaining signs, and the SCDs
choose the unique chains.

Within each initial tuple execute this deterministic policy:

1. Put its first seven factors in labeled accumulator slots.
2. Read the other factors in their fixed order. Merge the next factor into
   a currently shortest slot using a complete product SCD. Retain every
   child and continue the policy at that child. Break ties by slot label.
3. At a terminal seven-tuple, set aside a shortest chain. Sort the other
   six by length, with slot labels breaking ties, and apply the five-row
   staircase cover with half cuts. Adjoin the set-aside chain to the first
   shore of each row as in Section 5.
4. Euler-assemble all resulting paired rectangles globally as in (23).

The choice in step 2 is made without consulting the unread factor's
length. This is important for the independent-increment analysis.

### All Nonprincipal Positions Are Lower Order

For an initial tuple let `L=sum a_i`. Each of its `n-7` accumulator merges
has at most `L` children. A terminal staircase on three axes has at most
`L^2` chains. Adjoining the seventh factor adds at most a factor `L` to
one shore's count. Hence the number of terminal paired rectangles is at
most `5L^(n-2)` per tuple, and the main charge is at most `10L^(n-1)`.
The fixed-`n` SCD chain-count and moment bounds therefore give

\[
                      E=O_n(2^{nh}/h)=o(W(nh)).         \tag{24}
\]

Every bridge support is a proper union of original blocks. For a fixed
such union, a produced chain is specified by its input SCD chains, signs,
binary grouping history, staircase order, and a bounded number (depending
only on `n`) of integer child indices and cuts, each at most `nh`.
There are finitely many grouping histories for fixed `n`. Input-chain
choices on `j` blocks number at most `2^{j(h-1)}`. Thus for a constant
`C_n` one may use the explicit type of catalogue bound

\[
             V_{\rm cat}\le C_n(nh+1)^{C_n}2^{(n-1)h}. \tag{25}
\]

This includes all choices made in other components or by external length
comparisons; it does not assume a fixed order chosen in advance. Equations
(23)-(25) make every endpoint and closing cost `o(W(nh))` at fixed `n`.

## 7. Correct Probability Normalization

A uniform SCD chain length divided by `sqrt(h)` converges to a standard
Rayleigh variable, with density `x exp(-x^2/2)` and uniform Gaussian tails.
This follows from the inventory
`binom(h-1,i)-binom(h-1,i-1)` of chains with bottom rank `i`. Biasing by
chain length gives

\[
 Z\sim\chi_3,\qquad
 g_Z(z)=\sqrt{2/\pi}\,z^2e^{-z^2/2}.                  \tag{26}
\]

A complete product SCD of lengths `a,b` has child lengths
`|a-b|+1, |a-b|+3,...,a+b-1`. Their volumes sum to `ab`, and a
volume-biased child has probability `r/(ab)`. The continuum kernel is

\[
 K(a,b;dr)=\frac r{2ab}\mathbf1_{|a-b|<r<a+b}\,dr.     \tag{27}
\]

Use the same minimum-slot policy on `n` independent inputs `Z/sqrt(n)`
with kernel (27). At the end let
`Y_{1,n}<=...<=Y_{6,n}` be the six largest radii. Define the principal
upper value

\[
                Q_n=\sqrt{\pi/8}\,
                     \mathbb E T_6(Y_{1,n},...,Y_{6,n}).           \tag{28}
\]

Then the literal policy above satisfies

\[
                   \limsup_{h\to\infty}
                   \frac{\nu(nh)}{W(nh)}\le Q_n.       \tag{29}
\]

Here are the normalization and limit details. If `P` is an initial tuple's
principal upper charge, the total signed principal bound is exactly

\[
       2^{nh-1}\,\mathbb E_{\rm volume}
                         \frac{P(a_1,...,a_n)}{\prod_i a_i}.       \tag{30}
\]

Every accumulator merge is a complete partition, so finite normalized
branch averaging uses child probabilities `r/(ab)`, whose limit is (27).
At the terminal tuple, (21) bounds the normalized charge by
`P_6(a)/(prod a_i)`, not pointwise by its continuum limit `T_6`. The rounding
estimates give `P_6(a)=p_6(a)+O((1+sum a_i)^4)`. After multiplication by
the seventh length and summation over the at most `L^(n-7)` accumulator
branches, the discrepancy is `O_n((L+1)^(n-2))`. Its total signed SCD
average is `O_n(2^(nh)/h)=o(W(nh))`. Thus the limiting terminal upper
value is `T_6` on the six largest factors. Also

\[
             \frac{2^{nh-1}}{\sqrt h\,W(nh)}
                  \longrightarrow\sqrt{\pi n/8}.      \tag{31}
\]

The further `1/sqrt(n)` scaling gives (28), since `T_6` is homogeneous
of degree minus one.

For fixed `n`, these are genuine Riemann limits, not uniform-in-`n`
claims. The unweighted terminal upper cost is `r p_6` and is continuous
even at `r=0`; it has homogeneous degree six. Each additional mesh-two
merge becomes a half integral and increases the degree by one. At a tie
between shortest slots the two choices give the same numeric length
multiset, so the continuation is continuous. The finite chain-count
formulas (14)-(15), the bound `10L^(n-1)`, and uniform SCD polynomial
moments justify truncation and dominated convergence. Thus the normalized
singular expression in (30) has not been used without its volume weights.

## 8. Seven Balanced Clocks

Let `W_1,...,W_7` be independent standard three-dimensional Brownian motions
started at zero. On the mesh `j/n`, advance the clock of a currently
shortest-radius path by `1/n` at each of `n` updates. Only the new point of
the chosen path is revealed. Ties are broken by label.

The first seven updates seed different paths almost surely. Each next
unrevealed increment is an independent `N(0,I_3/n)` vector. Its norm has
law (26) divided by `sqrt(n)`, and its angle with a fixed current vector
has uniform cosine on `[-1,1]`. The norm of their sum consequently has
kernel (27). This proves that the final six largest radii have the law
used in (28). It is an analysis of volume-biased branches; the word
construction still retains all children.

Set

\[
 \omega_n=\max_{i\le7,\ 0\le j<n}
       \sup_{j/n\le t\le(j+1)/n}|W_i(t)-W_i(j/n)|.
\]

Let `A_n` be the largest current radius and `B_n` the **second smallest**
current radius, namely the smallest of the six largest. Let `H_i` be the
largest sampled radius of path `i` up to its allocated time. The following
deterministic invariants hold:

\[
 A_n=\max_i H_i,\qquad 0\le A_n-B_n\le\omega_n,
                   \qquad A_n-\omega_n\le H_i\le A_n. \tag{32}
\]

For the first assertion, updating a minimum cannot destroy the maximum.
For the second, the six untouched radii already lie in an interval of
length `omega_n`; if the new value enters their top-six group, it is at
most the old minimum plus `omega_n`. Induction preserves the top-six
spread bound. For the last assertion, consider the update first attaining
the final maximum: its old minimum, and hence all other radii then, was
at least `A_n-omega_n`.

Define first hitting times and their sum by

\[
 \tau_i(a)=\inf\{t:|W_i(t)|=a\},\qquad
 \sigma(a)=\sum_{i=1}^7\tau_i(a),\qquad
 A=\sup\{a:\sigma(a)\le1\}.                           \tag{33}
\]

These hitting times are strictly increasing and left-continuous in the
level. The generalized inverse is intentional. Every path has reached
`(A_n-omega_n)_+` by its allocated clock time, and has not reached
`A_n+2omega_n`: its continuous radius before that time is at most
`A_n+omega_n`. Since the seven allocated times sum to one,

\[
 \sigma((A_n-\omega_n)_+)\le1<\sigma(A_n+2\omega_n).
\]

It follows that

\[
     A_n-\omega_n\le A\le A_n+2\omega_n,
                   \qquad Y_{i,n}\longrightarrow A\quad\text{a.s.} \tag{34}
\]

The final assertion uses uniform continuity of the seven paths on `[0,1]`.

### Reciprocal Control

Let `tau` be first exit from the unit ball by standard three-dimensional
Brownian motion, and let `S_7=tau_1+...+tau_7` for independent copies.
Brownian scaling and (33) give

\[
                     A^{-2}\overset d=S_7,\qquad
                         \mathbb E S_7=7/3.            \tag{35}
\]

Indeed `A<a` is equivalent to `sigma(a)>1`, and
`sigma(a)` has law `a^2 S_7`. Fixed-level hitting times have no atoms,
since hitting exactly at time `t` entails a Gaussian vector on a fixed
sphere. The mean exit time from a point `x` is `(1-|x|^2)/3`, by stopping
`|W_t|^2-3t`; stopping first at `tau wedge t` also proves integrability.

The Markov property in time blocks `2/3` gives

\[
 \Pr(\tau\ge t)\le2^{-\lfloor3t/2\rfloor},\qquad
 \Pr(A\le r)\le7\,2^{-\lfloor3/(14r^2)\rfloor}.       \tag{36}
\]

A reflection bound and a union bound over 21 coordinate paths and `n`
mesh intervals give

\[
                    \Pr(\omega_n>\epsilon)
                       \le84n e^{-n\epsilon^2/6}.      \tag{37}
\]

The second smallest current radius never decreases under minimum updates.
After seven updates the radii are independent `chi_3/sqrt(n)`, and
`E chi_3^{-2}=1`. Therefore

\[
                           \mathbb E B_n^{-2}\le7n.    \tag{38}
\]

Take `epsilon=n^(-1/4)` and
`G_n={omega_n<=epsilon,A>6epsilon}`. By (34), on this event
`B_n>=A/2`, so (19) gives the integrable domination `T_6(Y_n)<=10/A`.
On its complement, (19) and Cauchy--Schwarz bound the expectation by

\[
 5\sqrt{7n\Pr(G_n^c)},\qquad
 \Pr(G_n^c)\le84n e^{-n\epsilon^2/6}
                +7\,2^{-\lfloor1/(168\epsilon^2)\rfloor}.
                                                               \tag{39}
\]

This tends to zero. The modulus bound in (37), at this choice of epsilon,
is summable, so its good event holds eventually almost surely; also `A>0`
almost surely. Equations (18), (34), and dominated convergence on
`G_n` now prove, without a weak-limit reciprocal shortcut,

\[
 \boxed{Q_n\longrightarrow
       \frac54\sqrt{\pi/8}\,\mathbb E\sqrt{S_7}.}       \tag{40}
\]

Jensen's inequality in (35) already gives (2). Its strict rational endpoint
uses `pi<22/7` and `275/192 < (1197/1000)^2`.

## 9. Exact Evaluation

The unit-ball exit-time transform is

\[
          \mathbb E e^{-s\tau}
                     =\frac{\sqrt{2s}}{\sinh\sqrt{2s}}.           \tag{41}
\]

For completeness, the regular radial solution of
`u''/2+u'/r=s u`, with `u(1)=1`, is
`sinh(r sqrt(2s))/(r sinh(sqrt(2s)))`. Applying Ito's formula up to the
exit time gives (41), including its limit at `r=0`.

Tonelli's theorem gives

\[
 \mathbb E\sqrt X=\frac1{2\sqrt\pi}
         \int_0^\infty(1-\mathbb E e^{-sX})s^{-3/2}\,ds.
\]

Using (41) to the seventh power and substituting `x=sqrt(2s)`, the right
side of (40) is

\[
 c_{\rm st}=\frac58 I_7,\qquad
 I_7=\int_0^\infty\left(\frac1{x^2}
                            -\frac{x^5}{\sinh^7x}\right)dx.      \tag{42}
\]

Here is an exact evaluation, including the cancellation at zero. Let
`f(x)=csch(x)` and `D=d/dx`. The identity

\[
 (\operatorname{csch}^p x)''
    =p^2\operatorname{csch}^p x+p(p+1)\operatorname{csch}^{p+2}x
\]

implies

\[
 \operatorname{csch}^7x
            =\frac{D^6-35D^4+259D^2-225}{720}\,f(x).  \tag{43}
\]

Integrate (43) against `x^5` on `[epsilon,infinity)` by parts. The
sixth-derivative boundary contribution is `1/epsilon+O(epsilon)` after
division by 720; the fourth- and second-derivative boundary contributions
tend to zero. To see that no finite constant is hidden here, use
`f(x)=x^{-1}+O(x)` with its odd Laurent expansion. Every resulting
boundary power is odd; the only nonvanishing one is `epsilon^{-1}`.
Its coefficient is one, either directly from the six terms of the
sixfold integration by parts or from the leading term in (43).

Writing `J_q=int_0^infinity x^q/sinh(x) dx`, the remaining bulk terms give

\[
                        I_7=\frac{35}{6}J_1
                                  -\frac{259}{36}J_3
                                  +\frac5{16}J_5.     \tag{44}
\]

The nonnegative series `1/sinh x=2 sum_{j>=0} exp(-(2j+1)x)` gives

\[
                  J_1=\pi^2/4,\qquad
                  J_3=\pi^4/8,\qquad J_5=\pi^6/4.     \tag{45}
\]

These use the elementary evaluations
`zeta(2)=pi^2/6`, `zeta(4)=pi^4/90`, `zeta(6)=pi^6/945`; they also
follow directly from Parseval applied successively to `x,x^2,x^3` on
`[-pi,pi]`. Substituting (45) in (42)-(44) proves the exact expression
in (1).

The numerical upper endpoint in (1) is certified with rational arithmetic.
Use the alternating arctangent sums with 40 terms at `1/5` and eight terms
at `1/239`, together with
`pi=16 arctan(1/5)-4 arctan(1/239)`. For the resulting rational interval
`l<pi<u`, the checker bounds (1) above by

\[
                  \frac{225u^6-2590l^4+4200u^2}{4608}
                         <11883/10000.                 \tag{46}
\]

It also certifies the lower endpoint `1188229/1000000`. No floating-point
quadrature is used in these inequalities. Independently, numerical
quadrature of (42) agreed with (1) within `6e-13`; that comparison is
corroboration only.

## 10. Every Dimension

For each fixed `n>=7`, (23)-(31) give universal words in dimensions `nh`
with limiting ratio at most `Q_n`. At most `n-1` ordinary top-bit splices
transfer them to other dimensions, with a width correction tending to one.

An explicit diagonal construction is: for each sufficiently large `k`,
construct the word for every integer `7<=n<=floor(sqrt(k))`, using
`h=floor(k/n)`, then splice each to dimension `k` and retain a shortest
candidate. For the remaining finite dimensions, use the word listing all
nonempty subsets. This is a finite deterministic construction, not an
efficiency assertion. Every fixed `n` is eventually a candidate, so

\[
       \limsup_{k\to\infty}\frac{\nu(k)}{W(k)}
                         \le\inf_{n\ge7}Q_n
                         \le\lim_{n\to\infty}Q_n=c_{\rm st}.
\]

This proves (1) for all dimensions. No estimate uniform in a growing
number of original blocks was assumed in the word compiler.

## 11. Checks and Scope

New reproducible files:

- `threshold_cycle_cover_20260906_91bc7.py`: exact threshold cover search and six-cycle residual census.
- `six_staircase_cover_20260906_91bc7.py`: explicit staircase partitions, finite counts, and optional noncertified cut optimization.
- `seven_accumulator_staircase_verify_20260906_91bc7.py`: rational constant certificate, general balanced-path checks, and literal seven-accumulator words.

Run the last two with `python3 -B`. Observed exact checks:

- 2,744 three-factor staircase partitions, including degenerate cuts and both transported orientations.
- 150 balanced paths of lengths two through six, checking support, counts, saturation, and symmetric endpoints.
- 100,000 integer minimum-update checks of the seven-slot invariants.
- 180 exact rational volume-weighted recurrences, checking the complete-branch normalization and the seventh-factor cancellation.
- 35 literal terminal seven-factor paired-box words, including unequal lengths, with every required target checked by actual interval union.
- All 64 threshold patterns, their exact occurrence profile (4), and the full excess volume.
- The rational enclosure (46) and the simpler Jensen certificate.

The global Euler compiler produced these full-cube regressions:

| Block Sizes | Dimension | Word Length | Main Charge | Endpoint Letters | Closing Letters |
|---|---:|---:|---:|---:|---:|
| seven 2s | 14 | 6,225 | 5,120 | 1,080 | 25 |
| eight 2s | 16 | 25,970 | 20,992 | 4,928 | 50 |
| nine 2s | 18 | 106,212 | 85,504 | 20,624 | 84 |
| six 2s and one 3 | 15 | 12,930 | 10,496 | 2,384 | 50 |
| five 2s and two 3s | 16 | 27,641 | 22,144 | 5,400 | 97 |
| seven 2s and one 3 | 17 | 51,815 | 41,984 | 9,776 | 55 |

Every word realizes all `2^k-1` nonempty targets. These are compiler
regressions, not finite-optimum improvements.

For comparison, the naive two alternating perfect matchings of a directed
six-cycle leave 12 threshold patterns. They split into three disjoint
two-dimensional subcubes, obtained by choosing a red edge and its disjoint
opposite blue edge as simultaneous strict increases. Exhaustive enumeration
of all 280,840 triples from the 120 oriented perfect matchings also found
no three-matching cover. This negative search is not a premise of (1).
The positive five-row cover has the self-contained certificate in Section 2.

More generally, a product from an oriented perfect matching on `2r`
bits has rank polynomial `(1+z+z^2)^r`. Thus any such full cover needs
at least

\[
       \max_s\frac{\binom{2r}{s}}{[z^s](1+z+z^2)^r}
       \ge\frac{\binom{2r}{r}}{[z^r](1+z+z^2)^r}
       =\left(\frac2{\sqrt3}+o(1)\right)(4/3)^r
\]

members at the central lower-bound scale. Merely increasing the matching
size is not the successful mechanism here. The ordered-path staircases
compress an entire monotone sequence of threshold states into explicit
long chains, and the seventh-factor argument uses those chains physically.

The centered and moving-center **partition** barriers are not contradicted:
(5) is a leading overlap, and all its word costs remain in (16) and (23).
The result is an unconditional asymptotic upper bound below 1.23, not a
claim that larger threshold covers already reach coefficient one.
