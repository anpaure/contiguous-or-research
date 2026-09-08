# A `D_4`-port factor transferring one first-insertion unit from pair 2 to pair 3

Date: 2026-07-26

The certificate below was found by a finite exact-cover exploration.  Its
proof is the literal inspection of the displayed `X`- and `Y`-ledgers and
does not depend on the search.

## 0. Result

Put

\[
 J=[8],\qquad
 E_0=\{1,8\},\quad E_1=\{2,3\},\quad
 E_2=\{4,5\},\quad E_3=\{6,7\}.                       \tag{0.1}
\]

There is a `D_4`-port-rooted exact `C_9`-factor `G` whose first-insertion
target counts on these four coordinate pairs are

\[
                 \boxed{(h_0,h_1,h_2,h_3)(G)=(5,5,1,3).} \tag{0.2}
\]

For the canonical MSW factor `G_MSW`, the corresponding vector is

\[
                 (h_0,h_1,h_2,h_3)(G_{\rm MSW})=(5,5,2,2). \tag{0.3}
\]

Consequently the signed difference has the pure pair-class effect

\[
            \boxed{(h_i(G)-h_i(G_{\rm MSW}))_{i=0}^3
                         =(0,0,-1,+1).}                \tag{0.4}
\]

Thus first-insertion pair totals are **not** an invariant of complete
`D_4`-port-transversal factors.  The missing pair-2-to-pair-3 bridge exists
already at semilength four.

## 1. The fourteen rooted paths

A string such as `1234` denotes the set `\{1,2,3,4\}`.  The row label is
its prescribed Dyck port `P=X_0`; the five entries are
`X_0,X_1,X_2,X_3,X_4`.

\[
\begin{array}{c|ccccc|c}
P&X_0&X_1&X_2&X_3&X_4&\theta(P)\\ \hline
1234&1234&1238&1368&1568&5678&8\\
1235&1235&1358&1378&1678&4678&8\\
1236&1236&1267&1467&4567&4578&7\\
1237&1237&1278&1268&1468&4568&8\\
1245&1245&2345&3456&3567&3678&3\\
1246&1246&2346&2368&2378&3578&3\\
1247&1247&2347&2348&2358&3568&3\\
1256&1256&1567&1367&3467&3478&7\\
1257&1257&2357&3457&3458&3468&3\\
1345&1345&1456&2456&2567&2678&6\\
1346&1346&1348&1458&1578&2578&8\\
1347&1347&1478&1248&1258&2568&8\\
1356&1356&2356&2367&2467&2478&2\\
1357&1357&1457&2457&2458&2468&4
\end{array}                                             \tag{1.1}
\]

Here

\[
                         \theta(P)=X_1\setminus X_0      \tag{1.2}
\]

is the first inserted coordinate.  It is also the unique coordinate in
`X_1 intersect X_2 intersect X_3 intersect X_4`.

### Lemma 1.1 (row legality and ports)

Every consecutive pair in (1.1) is a Johnson edge, and every last state is
the complement in `[8]` of its first state.  The first states are exactly
the fourteen members of `D_4`.

#### Proof

Consecutive entries in every row have three common coordinates.  Reading
the endpoints gives

\[
\begin{gathered}
1234\leftrightarrow5678,\ 1235\leftrightarrow4678,\
1236\leftrightarrow4578,\ 1237\leftrightarrow4568,\\
1245\leftrightarrow3678,\ 1246\leftrightarrow3578,\
1247\leftrightarrow3568,\ 1256\leftrightarrow3478,\\
1257\leftrightarrow3468,\ 1345\leftrightarrow2678,\
1346\leftrightarrow2578,\ 1347\leftrightarrow2568,\\
1356\leftrightarrow2478,\ 1357\leftrightarrow2468.
\end{gathered}                                          \tag{1.3}
\]

The left endpoints are the standard Catalan family `D_4`. \(\square\)

## 2. Exact `X`-ledger

### Lemma 2.1

The seventy entries in (1.1) are all distinct.  Hence they enumerate
`binom([8],4)` exactly once.

#### Proof

The twenty-eight endpoints in (1.3) are distinct.  The forty-two internal
states are

\[
\begin{aligned}
\{&1267,1367,1456,1457,1467,1567,
2345,2346,2347,2356,2357,2367,\\
&2456,2457,2467,2567,3456,3457,3467,3567,4567,\\
&1238,1248,1258,1268,1278,1348,1358,1368,1378,
1458,1468,1478,\\
&1568,1578,1678,2348,2358,2368,2378,2458,3458\}.
\end{aligned}                                          \tag{2.1}
\]

They are distinct and none is an endpoint in (1.3).  Thus (1.1) contains
seventy distinct four-sets, the full cardinality of `binom([8],4)`.
\(\square\)

## 3. Exact `Y`-ledger

Put `Y_t=X_t union X_(t+1)`.  The four adjacent-union colours in the
fourteen rows are

\[
\begin{array}{c|cccc}
1234&12348&12368&13568&15678\\
1235&12358&13578&13678&14678\\
1236&12367&12467&14567&45678\\
1237&12378&12678&12468&14568\\
1245&12345&23456&34567&35678\\
1246&12346&23468&23678&23578\\
1247&12347&23478&23458&23568\\
1256&12567&13567&13467&34678\\
1257&12357&23457&34578&34568\\
1345&13456&12456&24567&25678\\
1346&13468&13458&14578&12578\\
1347&13478&12478&12458&12568\\
1356&12356&23567&23467&24678\\
1357&13457&12457&24578&24568
\end{array}                                             \tag{3.1}
\]

### Lemma 3.1

The fifty-six entries in (3.1) are all distinct.  Hence they enumerate
`binom([8],5)` exactly once.

#### Proof

Sorting (3.1) gives

\[
\begin{aligned}
\{&12345,12346,12347,12348,12356,12357,12358,12367,
12368,12378,\\
&12456,12457,12458,12467,12468,12478,12567,12568,
12578,12678,\\
&13456,13457,13458,13467,13468,13478,13567,13568,
13578,13678,\\
&14567,14568,14578,14678,15678,23456,23457,23458,
23467,23468,\\
&23478,23567,23568,23578,23678,24567,24568,24578,
24678,25678,\\
&34567,34568,34578,34678,35678,45678\}.
\end{aligned}                                          \tag{3.2}
\]

This is the complete list of the fifty-six five-subsets of `[8]`.
\(\square\)

### Theorem 3.2 (exact port factor)

The paths in (1.1) give a `D_4`-port-rooted exact `C_9`-factor of
`KG([8] union {9},4)`.

#### Proof

Between `X_t` and `X_(t+1)` insert the odd-graph vertex

\[
                 Z_t=\{9\}\cup([8]\setminus Y_t).       \tag{3.3}
\]

Lemma 1.1 gives fourteen legal complementary Johnson paths.  Lemma 2.1
enumerates every odd-graph vertex avoiding `9` once.  Lemma 3.1 and the
bijection in (3.3) enumerate every vertex containing `9` once.  Hence the
resulting `C_9` cycles form an exact factor.

Every member of `D_4` is already used once as a first state.  Exactness
therefore prevents a second Dyck state anywhere else.  Thus every row has
its displayed first state as its unique Dyck port. \(\square\)

## 4. The pair-2-to-pair-3 bridge

Reading the last column of (1.1), the new target multiset is

\[
             5e_8+e_2+4e_3+e_4+e_6+2e_7.              \tag{4.1}
\]

Therefore its totals on `(E_0,E_1,E_2,E_3)` are `(5,5,1,3)`.

For comparison, applying the canonical MSW flip recursion to the same
ordered Dyck roots gives the first-insertion targets

\[
\begin{array}{c|cccccccccccccc}
P&1234&1235&1236&1237&1245&1246&1247&1256&1257&1345&1346&1347&1356&1357\\ \hline
\theta_{\rm MSW}(P)&8&8&8&6&8&8&6&4&4&2&2&2&2&2.
\end{array}                                             \tag{4.2}
\]

Its pair totals are `(5,5,2,2)`.  Subtracting proves (0.4).  In
particular this bridge changes the pair totals left invariant by every
fixed-slab rooted-pentagon combination and reaches the pair class not
reached by the elementary leaf rectangle.

## 5. Scope

The theorem settles the finite existence gate only.  The full
fourteen-for-fourteen replacement is already a finite rooted trade.  What
it does not yet give is a proper smaller-support/common-completion
subtrade, a uniformly root-scale recursive all-`m` suspension, or a
quantitative PCap signing theorem.  Its exact structural consequence is
that there is no pair-total invariant blocking the missing
pair-2-to-pair-3 direction inside the full `D_4`-port-transversal fibre.

## 6. The complete carrier-resolved one-hole action

The path table determines more than the marked first insertion.  For a
rooted path write

\[
 X_t=(P\setminus\{a_1,\ldots,a_t\})
        \cup\{b_1,\ldots,b_t\},\qquad0\le t\le4,       \tag{6.1}
\]

and define its oriented local coordinate word by

\[
                         q(P)=(a_1,a_2,a_3,a_4,
                                  b_1,b_2,b_3,b_4,9).    \tag{6.2}
\]

The old and new words are as follows.

\[
\begin{array}{c|c|c}
P&q_{\rm MSW}(P)&q_G(P)\\ \hline
1234&243186579&423186579\\
1235&235184679&253187649\\
1236&623187459&321674589\\
1237&231764589&372186459\\
1245&452186739&124536789\\
1246&642187539&146238759\\
1247&421765389&174238569\\
1256&216543879&251673489\\
1257&215743689&127534869\\
1345&145328679&314562789\\
1346&164328759&634185729\\
1347&143726589&374182569\\
1356&136524879&153627489\\
1357&135724689&317542869
\end{array}                                             \tag{6.3}
\]

For `1<=ell<=8` and `j in Z_9`, put

\[
 I_{\ell,j}(q)=\{q_j,q_{j+1},\ldots,q_{j+\ell-1}\},
\]

with cyclic indices, and define the signed carrier profile

\[
 \boxed{
 \Delta_{\ell,j}
  =\sum_{P\in\mathcal D_4}
       \left(e_{I_{\ell,j}(q_G(P))}
             -e_{I_{\ell,j}(q_{\rm MSW}(P))}\right).}   \tag{6.4}
\]

### Theorem 6.1 (closed-slab one-hole carrier functor)

Let `C[ ]` be an aligned one-hole context, let `iota` be its affine
labelling of the nine local positions, and fix one ambient window profile.
Suppose its intersection with the local coordinate word is the cyclic
segment `(ell,j)` and its exterior intersection is the same set `O` on
every row.  Replacing the canonical local factor by `G` changes the target
histogram by exactly

\[
                     \boxed{O\cup\iota(\Delta_{\ell,j}).} \tag{6.5}
\]

For a general ambient window family, its total signed effect is the sum of
(6.5) over its carrier profiles.  Thus (6.3)--(6.4) determine the action at
**every** affected depth and offset, including all collar terms.

#### Proof

The two exact `X/Y` ledgers proved in Sections 2--3, together with the
fixed rowwise ports `X_0=P,X_4=[8]\setminus P`, make the substitution
legal in the corrected Section-17 **closed-slab** interface: all four
internal state edges belong to the substituted slab and unchanged outer
row pieces attach only at `X_0,X_4`.  In a rooted wreath, a target's local
coordinates form a cyclic interval of (6.2).  Coordinates outside the
hole are fixed by the context, so the old and new physical targets are
respectively `O union iota(I_(ell,j)(q_MSW(P)))` and
`O union iota(I_(ell,j)(q_G(P)))`.  Summing over the fourteen rows gives
(6.5), and then summing carrier classes proves the last assertion.
\(\square\)

This theorem is the precise functorial statement: the marked target
calculation is one column of a finite tensor, not a claim that collars are
absent.

The closed-slab qualification is essential.  Fixed ports do not preserve
the oriented cyclic seam `b_4,9,a_1`, and therefore do not by themselves
justify a half-edge attachment, an overlapping or nested substitution, or
preservation of a later necklace partition.  Such a use requires the full
outer `X/Y` ledger (for exact ownership) and the literal positional tensor
`D_A` (for crossing shadows).  Changing `a_1` or `b_4` does not break the
closed-slab middle join: the outer incident edges meet the unchanged
endpoints, while the changed internal edges are already included in the
complete `X/Y` ledgers.

## 7. Exact audit of every local depth

At singleton length, write `delta_j=Delta_(1,j-1)` for positions
`j=1,...,9` of (6.2).  Directly from (6.3),

\[
\begin{array}{c|l|c}
j&\delta_j&\|\delta_j\|_1/2\\ \hline
1&-3e_2+5e_3-e_4-e_6&5\\
2&2e_2-3e_3-3e_4+2e_5-e_6+3e_7&7\\
3&-e_2+4e_4-4e_5-e_6+2e_7&6\\
4&2e_2-2e_3+2e_5+3e_6-5e_7&7\\
5&-4e_2+4e_3-e_4-e_6+2e_7&6\\
6&3e_2-e_3-2e_4&3\\
7&-e_3+2e_4-3e_6+2e_7&4\\
8&e_2-2e_3+e_4+4e_6-4e_7&6\\
9&0&0
\end{array}                                             \tag{7.1}
\]

Position five is `b_1`, so (7.1) refines the pair bridge:

\[
 \delta_{b_1}=4(e_3-e_2)-e_4-e_6+2e_7,\qquad
 \bigl(\delta_{b_1}(E_0),\ldots,\delta_{b_1}(E_3)\bigr)
                         =(0,0,-1,+1).                  \tag{7.2}
\]

The other singleton carriers repay it in aggregate:

\[
                              \sum_{j=1}^9\delta_j=0.   \tag{7.3}
\]

Put `Delta_ell=sum_j Delta_(ell,j)`.  Exact middle ownership and
coordinate regularity give

\[
                 \Delta_1=\Delta_4=\Delta_5=\Delta_8=0. \tag{7.4}
\]

The only nonzero lower aggregate profiles are

\[
\begin{aligned}
\Delta_2={}&
 2e_{14}+e_{25}+e_{26}+3e_{27}+e_{36}+e_{37}
 +2e_{47}+e_{48}+e_{58}+3e_{39}+3e_{69}\\
&-e_{12}-e_{13}-e_{23}-e_{24}-2e_{34}-e_{35}
 -2e_{46}-e_{56}-e_{67}-e_{68}-e_{78}-2e_{29}-4e_{79},
                                                               \tag{7.5}\\
\Delta_3={}&
 e_{127}+2e_{147}+e_{236}+e_{247}+e_{257}+e_{267}+e_{367}
 +e_{148}+e_{258}+e_{348}+e_{389}+e_{489}\\
&+2e_{259}+2e_{369}+e_{379}+e_{479}+e_{159}+e_{569}+e_{169}\\
&-e_{124}-e_{125}-e_{136}-e_{235}-e_{246}-e_{346}-e_{357}
 -e_{567}-e_{178}-e_{368}-e_{478}\\
&-e_{289}-e_{589}-e_{179}-e_{239}-2e_{279}-e_{349}
 -e_{149}-e_{459}-2e_{679}.                            \tag{7.6}
\end{aligned}
\]

Their positive masses are

\[
                         \|\Delta_2\|_1/2=19,\qquad
                         \|\Delta_3\|_1/2=22.          \tag{7.7}
\]

The upper profiles are their complements:

\[
 \Delta_{9-\ell,j+\ell}(J\setminus S)
                         =\Delta_{\ell,j}(S),           \tag{7.8}
\]

so `Delta_7` and `Delta_6` have masses 19 and 22 respectively.

For reference, let

\[
                 m_{\ell,j}=\|\Delta_{\ell,j}\|_1/2.   \tag{7.9}
\]

The complete start-resolved mass table is

\[
\begin{array}{c|c|c}
\ell&\|\Delta_\ell\|_1/2&(m_{\ell,0},\ldots,m_{\ell,8})\\ \hline
1&0 &(5,7,6,7,6,3,4,6,0)\\
2&19&(7,6,9,4,7,6,6,6,5)\\
3&22&(6,7,6,5,8,6,6,9,7)\\
4&0 &(0,3,3,2,0,6,9,10,6)\\
5&0 &(6,9,10,6,0,3,3,2,0)\\
6&22&(6,9,7,6,7,6,5,8,6)\\
7&19&(6,5,7,6,9,4,7,6,6)\\
8&0 &(0,5,7,6,7,6,3,4,6).
\end{array}                                             \tag{7.10}
\]

Equations (6.4), (7.1), and (7.10) are independently checkable directly
from the two word columns in (6.3); no asymptotics enter.

## 8. Actual conveyor capacity and exact cap accounting

Distinct aligned size-four contexts at one recursive scale have disjoint
row slabs.  Hence their old/new choices commute.  Their number is

\[
 H_{m,4}={1\over2}\binom{2(m-4)}{m-4}
          =\left({1\over1024}+o(1)\right)W.             \tag{8.1}
\]

Therefore (1.1) supplies an actual binary cube of exact factors with
`H_(m,4)` independently selectable pair-2-to-pair-3 marked transfers.  It
is not merely a signed span.  The port automorphism group

\[
 \langle(2\ 3),(4\ 5),(6\ 7)\rangle\cong C_2^3         \tag{8.2}
\]

orients the labels inside the three pairs.  At pair-class level, the
present bridge together with any certified pair-1-to-pair-2 bridge spans
the full zero-sum lattice on `(E_1,E_2,E_3)`.  Thus the early-scale
pair-class graph is connected.

This is a carrier conveyor, not yet a cap-descent theorem.  For one pushed
carrier profile, let `u` be its old load, `beta` the ambient background,
and `c=(p-beta)_+` its residual capacity.  The exact overload change is

\[
 \boxed{
 \Delta K_{\ell,j}
   =\sum_S\left[(u(S)+\Delta_{\ell,j}(S)-c(S))_+
                         -(u(S)-c(S))_+\right].}         \tag{8.3}
\]

Since every `Delta_(ell,j)` has total zero,

\[
                         -m_{\ell,j}
                    \le\Delta K_{\ell,j}
                    \le m_{\ell,j}.                    \tag{8.4}
\]

In particular the marked `b_1` sector can improve or worsen cap overload
by at most six, and has no state-independent sign.  For a whole ambient
profile, push forward (8.3) and add over its carrier classes; (7.10) gives
the corresponding sharp triangle-inequality bound.

There is an exact cancellation at the first matched singleton scale.
Every exact size-four factor has the same complete singleton point margin,
and all slots outside the installed parent are fixed.  Hence the full
affected singleton histogram, including collars, is identical before and
after substitution.  For every residual background,

\[
                   \boxed{\Delta K_{\rm matched}=0,
                          \qquad\Delta M_{\rm matched}=0.} \tag{8.5}
\]

Thus (7.2) is repaid by the other carrier positions at this first scale.
After one additional outer lift the protected targets are no longer
singletons, so point-margin rigidity no longer forces (8.5); Theorem 6.1
then gives the exact full profile that must be routed.  Establishing a
favourable simultaneous sign for those pushed profiles is the remaining
PCap problem.

## 9. Dense fringe deployment has exactly the plateau scale

The fixed size-four atom can be deployed densely inside a growing Dyck
hole.  Let `a_r` be the number of ordered binary trees of size `r` which
contain no fringe subtree of size four, and put

\[
                         A(z)=\sum_{r\ge0}a_rz^r.
\]

There are `Cat_4=14` trees of size four.  The root decomposition therefore
gives

\[
                         A(z)=1+zA(z)^2-14z^4,           \tag{9.1}
\]

and hence

\[
 A(z)={1-\sqrt{1-4z+56z^5}\over2z}.                    \tag{9.2}
\]

At `z=1/4` the discriminant is `7/128>0`.  Since the coefficients of
`A` are nonnegative, Pringsheim's theorem implies that its radius of
convergence is strictly larger than `1/4`.  Consequently

\[
                         {a_r\over\operatorname {Cat}_r}=o(1)              \tag{9.3}
\]

exponentially fast.

For every tree not counted by `a_r`, choose its first size-four fringe
subtree in preorder.  Replacing that subtree by any of the fourteen size-
four trees does not move the chosen fringe root and does not change which
size-four fringe root is first.  The nonavoiding trees consequently split
into exact classes of fourteen fillings.  On each class one may install
either `G_MSW` or `G`, independently of all other classes.  Hence a
size-`r` hole contains

\[
 \boxed{
 P_r^{(23)}={\operatorname {Cat}_r-a_r\over14}
             =\left({1\over14}+o(1)\right)
                         \operatorname {Cat}_r}          \tag{9.4}
\]

pair-2-to-pair-3 switches with disjoint row support.

Across all aligned size-`r` holes in semilength `m`, the number of
independent marked transfers is

\[
 H_{m,r}P_r^{(23)}.
\]

Uniformly for \(r=o(\sqrt m)\), the Catalan and central-binomial asymptotics
give

\[
 \boxed{
 H_{m,r}P_r^{(23)}
   =\left({1\over56\sqrt\pi}+o(1)\right)
                         {W\over r^{3/2}}.}              \tag{9.5}
\]

Thus at the fatal scale `r=Theta(log p)` the new bridge has raw marked
capacity

\[
                         \Theta\!\left({W\over(\log p)^{3/2}}\right),       \tag{9.6}
\]

exactly the hereditary-plateau order.  The leading supply constant is
\(1/(56\sqrt\pi)\).

The complete carrier disturbance has the same order.  For example, the
largest row sum in the local table (7.10) is sixty.  Therefore a triangle-
inequality bound over the entire dense bank is

\[
 \left({60\over56\sqrt\pi}+o(1)\right){W\over r^{3/2}}. \tag{9.7}
\]

This is a capacity comparison, not a sign theorem: the collars are a
constant-factor larger than the one-unit marked transport.  A successful
PCap proof must exploit their two-boundary correlations rather than charge
all sixty units adversarially.

## 10. A literal two-boundary Boolean square

The aggregate bridge (0.4) is witnessed by useful rowwise changes, not by
an inseparable cancellation.  Comparing (4.2) with the last column of
(1.1) gives, among others,

\[
             \theta(1256):4\longrightarrow7,\qquad
             \theta(1345):2\longrightarrow6.            \tag{10.1}
\]

The two switched coordinate pairs

\[
                         \{4,7\},\qquad\{2,6\}           \tag{10.2}
\]

are disjoint.  Install two independently selectable copies of the factor
pair at the left and right boundary of one protected window, with the two
marked rows in (10.1) surviving through the common interior core `K`.
The four exact-factor choices give the four targets

\[
 \boxed{
 K\cup\{4,2\},\quad K\cup\{4,6\},\quad
 K\cup\{7,2\},\quad K\cup\{7,6\}.}                     \tag{10.3}
\]

They are pairwise distinct, since intersection with each pair in (10.2)
recovers the corresponding boundary bit.  Adjoining a common exterior set
does not change this conclusion.

Thus the factor pair supplies a literal port-valid realization of the
two-boundary Boolean-square label required by the early-scale capacity
theorem.  If `s` is minimal with `Cat_s>=p`, then `Cat_s<4p`, so four cells
have enough scalar capacity for the canonical size-`s` fibre.

What is not yet proved is **balanced four-cell realizability** for all
occurrences simultaneously.  One D4 packet bit acts on all fourteen local
roots at once, and the packet partitions induced at the two window
boundaries need not coincide.  The remaining local theorem is therefore a
joint contingency-table statement for the two dense packet partitions,
not existence of four distinct physical labels; (10.3) settles the latter.
