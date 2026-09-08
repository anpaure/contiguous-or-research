# Balanced-core owner-interval Hall and exact multiboundary erosion

**Date:** 2026-08-02
**Status:** unconditional exact compression of invariant chronological Hall
to owner intervals, and an unconditional exact telescoping identity for
overlap erosion across chronology blocks. The first canonical-serpent
obstruction is identified at K9 and the K46 interior obstruction is
recomputed in the same language. A bounded-component literal palette
sidecar is ruled out quantitatively. Existence of adaptive menus satisfying
the inequalities for every \(k\) remains explicitly **unproved**.

## 0. Verdict

Preserve a ground-set bipartition \(H\dot\cup K\), with
\[
 |H|=h,\qquad |K|=\ell,
\]
setwise. A target orbit type is
\[
 u=(i,j),\qquad
 {\cal O}_{i,j}=\{S:|S\cap H|=i,\ |S\cap K|=j\},
 \qquad w(i,j)={h\choose i}{\ell\choose j}.          \tag{0.1}
\]

Fix an owner rank \(R\). The owner types lie on one line, indexed by
\[
 p\in P_R=[p_-,p_+]_{\mathbb Z},\qquad
 p_-:=\max(0,R-\ell),\quad p_+:=\min(h,R),            \tag{0.2}
\]
with capacities
\[
 c_p={h\choose p}{\ell\choose {R-p}}.                \tag{0.3}
\]

The owner types containing a target type \(u=(i,j)\) form the integer
interval
\[
 I(u)=
 [\max(i,p_-),\ \min(R-j,p_+)]_{\mathbb Z}.          \tag{0.4}
\]
Thus every invariant exposed-root problem on the two-dimensional product
quotient has a one-dimensional interval owner shadow.

The exact Hall test is:

> For every invariant chronological upset \(U\) and every owner interval
> \(J\subseteq P_R\), the total mass of exposed-root types
> \(u\in R_\tau(U)\) satisfying \(I(u)\subseteq J\) is at most the owner
> capacity of \(J\).

This is equivalent to global Hall, not merely sufficient. The types with
\(I(u)\subseteq J=[a,b]\) form a clipped northeast rectangle:
\[
 I(i,j)\subseteq[a,b]
 \quad\Longleftrightarrow\quad
 \begin{cases}
   a=p_-\ \text{or}\ i\ge a,\\
   b=p_+\ \text{or}\ j\ge R-b.
 \end{cases}                                         \tag{0.5}
\]
The endpoint alternatives in (0.5) are essential. In particular, the
unclipped formula \(i\ge a,\ j\ge R-b\) is false at a clipped endpoint.

For one upset, split its roots into chronology banks. If \(A_t\) is the
owner-coordinate palette of the roots at time \(t\), put
\[
 \rho_t=\operatorname{cap}(A_t)-w(R_t),\qquad
 \varepsilon_t=
 \operatorname{cap}\!\left(A_t\cap\bigcup_{s>t}A_s\right).   \tag{0.6}
\]
Then the Hall deficiency is exactly
\[
 w(R_\tau(U))-\operatorname{cap}\!\left(\bigcup_tA_t\right)
       =\sum_t(\varepsilon_t-\rho_t).                \tag{0.7}
\]
Hence local bank expansion does not add independently: overlap with the
already carried owner palette is an exact erosion charge. Formula (0.7)
is the desired multiboundary telescoping law and needs no connected-palette
assumption.

At K9, each of the two root banks passes its individual owner-shadow test:
\[
 125\le125,\qquad 5\le21.
\]
Their owner palettes overlap in capacity \(20\), while their total local
reserve is only \(16\). Equation (0.7) gives the exact global deficiency
\(20-16=4\). This is the first failed canonical diagonal serpent and the
smallest exact obstruction to any rule which certifies chronology banks
independently while forgetting owner-palette overlap.

At K46, the two root banks have reserves
\[
 1\,488\,213\,570\,689,\qquad 2\,251\,954\,787\,055,
\]
but their palettes overlap in capacity
\[
 3\,804\,801\,426\,540.
\]
The excess erosion is exactly \(64\,633\,068\,796\), the previously found
interior Hall deficiency.

## 1. Orbit and vertex meanings

Let the chronology \(\tau\) be constant on every orbit (0.1). The target
types are partially ordered by product containment and weak time:
\[
 (i,j)\preceq_\tau(i',j')
 \Longleftrightarrow
 (i,j)=(i',j')\ \text{or}\
 \bigl(i\le i',\ j\le j',\ \tau(i,j)\le\tau(i',j')\bigr).    \tag{1.1}
\]
An invariant upset is a union of whole target orbits and an upset for
(1.1). Its exposed-root types are
\[
 R_\tau(U)=\{u\in U:
   \text{there is no }v\in U\text{ with }v<u
   \text{ and }\tau(v)<\tau(u)\}.                    \tag{1.2}
\]
Here \(v<u\) means strict product containment. Because every nonempty
compatible orbit incidence is biregular, one compatible earlier type below
\(u\) gives an earlier subset to every vertex in the orbit of \(u\).
Consequently (1.2) is exactly the exposed-root set of the invariant vertex
upset, not an averaged surrogate.

For every type family \(F\), write
\[
                         w(F)=\sum_{u\in F}w(u).       \tag{1.3}
\]

The prior chronological-upset theorem says that an invariant chronology
has a left-saturating **vertex** successor matching if and only if
\[
                    w(R_\tau(U))\le |\Gamma_R(U)|     \tag{1.4}
\]
for every invariant upset \(U\). Invariance loses no Hall witness: a
maximum-deficiency upset can be made invariant by unions of group
translates, using supermodularity. Equivalently, the finite weighted type
flow is exact; biregular incidence lifts a type transport fractionally and
bipartite integrality returns a vertex matching. The theorem below is a
further exact compression of (1.4). It does not assert vertex Hall for an
arbitrary non-invariant chronology.

## 2. Owner intervals and clipped rectangles

### Lemma 2.1 (exact owner interval)

For a target type \(u=(i,j)\), its rank-\(R\) owner shadow is the union of
the owner orbits indexed by \(p\in I(u)\), where \(I(u)\) is (0.4).
Moreover, if \(u\le v\) in product order, then
\[
                         I(v)\subseteq I(u).          \tag{2.1}
\]

#### Proof

An owner of type \(p\) has \(p\) points in \(H\) and \(R-p\) in \(K\).
It contains a member of type \((i,j)\) exactly when
\[
                         i\le p,\qquad j\le R-p.      \tag{2.2}
\]
Intersecting (2.2) with the feasible owner range (0.2) gives (0.4).
For every feasible \(p\), the corresponding incidence is nonempty and
biregular, so the entire owner orbit occurs in the shadow. Increasing
either target coordinate raises the left endpoint or lowers the right
endpoint, proving (2.1). \(\square\)

For \(J=[a,b]\subseteq P_R\), define
\[
                Q_J=\{u:I(u)\subseteq J\}.           \tag{2.3}
\]
By (2.1), \(Q_J\) is a product-order upset. Directly expanding its two
clipped endpoints gives (0.5). Thus \(Q_J\) is a northeast rectangle when
\(a>p_-\) and \(b<p_+\), with the corresponding inequality deleted at a
clipped endpoint.

### Lemma 2.2 (roots generate the owner shadow)

For every invariant chronological upset \(U\),
\[
       \Gamma_R(U)=\Gamma_R(R_\tau(U))
       =\bigcup_{u\in R_\tau(U)} I(u)                \tag{2.4}
\]
at owner-type level.

#### Proof

If \(u\in U\) is not a root, there is an earlier strict lower type
\(v\in U\). Repeat from \(v\). Rank strictly falls at every step, so the
process terminates at a root \(z\le u\). Lemma 2.1 gives
\(I(u)\subseteq I(z)\). Thus every owner orbit in the shadow of \(U\) is
already in the shadow of a root. The reverse inclusion is immediate.
\(\square\)

## 3. Exact interval/rectangle Hall compression

### Theorem 3.1 (owner-interval Hall theorem)

The invariant successor graph has a matching saturating every target
vertex if and only if, for every invariant chronological upset \(U\) and
every integer interval \(J\subseteq P_R\),
\[
 \sum_{\substack{u\in R_\tau(U)\\ I(u)\subseteq J}}w(u)
       \le \operatorname{cap}(J),
 \qquad
 \operatorname{cap}(J):=\sum_{p\in J}c_p.            \tag{3.1}
\]

#### Proof

Assume first that the matching exists. Put
\[
                         U_J=U\cap Q_J.              \tag{3.2}
\]
Both factors in (3.2) are upsets, so \(U_J\) is an upset. Restriction can
create new roots, but it cannot remove any root of \(U\) which lies in
\(Q_J\):
\[
 R_\tau(U)\cap Q_J\subseteq R_\tau(U_J).             \tag{3.3}
\]
Every owner interval of a type in \(U_J\) lies in \(J\). Applying the
exposed-root inequality (1.4) to \(U_J\) gives
\[
 \sum_{u\in R_\tau(U)\cap Q_J}w(u)
 \le w(R_\tau(U_J))
 \le |\Gamma_R(U_J)|
 \le\operatorname{cap}(J),
\]
which is (3.1). The possible new roots in (3.3) therefore help the
necessity argument; equality of the two root sets is neither claimed nor
needed.

Conversely, fix an upset \(U\). Decompose the discrete owner-coordinate
set
\[
                  \bigcup_{u\in R_\tau(U)}I(u)       \tag{3.4}
\]
into its maximal interval components \(J_1,\ldots,J_s\). Every root
interval lies in exactly one component. Apply (3.1) to \(U,J_a\) and sum
over the disjoint components. Lemma 2.2 yields
\[
 w(R_\tau(U))
 \le\sum_{a=1}^s\operatorname{cap}(J_a)
 =|\Gamma_R(U)|.
\]
Thus (1.4) holds for every invariant upset, and the prior exact
chronological Hall theorem gives the vertex matching. \(\square\)

Theorem 3.1 reduces arbitrary owner-shadow geometry to \(O(h^2)\) owner
intervals and their clipped rectangles (0.5). It does **not** remove the
quantifier over chronological upsets.

### Corollary 3.2 (exact interval expansion profile)

For \(J\subseteq P_R\), define
\[
 E_\tau(J)=
 \max\{w(R_\tau(V)):
       V\subseteq Q_J\text{ is an invariant chronological upset}\}. \tag{3.5}
\]
Then the invariant successor graph has a saturating matching if and only if
\[
                         E_\tau(J)\le\operatorname{cap}(J)
                         \qquad(J\subseteq P_R\text{ an interval}). \tag{3.6}
\]

#### Proof

If Theorem 3.1 holds, apply (3.1) with \(U=V\subseteq Q_J\); every root
interval is contained in \(J\), giving (3.6). Conversely, for arbitrary
\(U,J\), the upset \(V=U\cap Q_J\) obeys
\[
 R_\tau(U)\cap Q_J\subseteq R_\tau(V).
\]
Thus (3.6) implies (3.1), and Theorem 3.1 applies. \(\square\)

Corollary 3.2 is the weakest exact balanced-core expansion target exposed
here: construct a capacity-\(d+O(1)\) chronology for which all
\(O(k^2)\) interval profiles satisfy (3.6). Computing or bounding
\(E_\tau(J)\) still contains the unresolved chronological-upset
optimization.

### Proposition 3.3 (full rectangles do not suffice)

For the K9 canonical serpent, every one of the fifteen complete clipped
rectangles \(Q_J\) satisfies
\[
                         w(R_\tau(Q_J))
                         \le\operatorname{cap}(J).    \tag{3.7}
\]
The exact root-mass/capacity pairs, grouped by the left endpoint of \(J\),
are
\[
\begin{array}{c|ccccc}
a\backslash b&0&1&2&3&4\\ \hline
0&0/1&5/21&10/81&60/121&125/126\\
1&&0/20&40/80&40/120&100/125\\
2&&&0/60&60/100&36/105\\
3&&&&0/40&25/45\\
4&&&&&1/5.
\end{array}                                         \tag{3.8}
\]
Nevertheless the proper upset
\[
 U=\{(3,0)\}\cup\{(i,4-i):0\le i\le4\}
 \subsetneq Q_{[0,4]}                               \tag{3.9}
\]
has exposed-root mass \(130\), while
\(\operatorname{cap}([0,4])=126\).

Thus replacing the maximum in (3.5) by the single full-rectangle state
\(V=Q_J\) is false already at the first canonical-serpent failure. Any
compression or uncrossing proof must control proper chronological upsets
inside the rectangle.

#### Proof

The fifteen entries in (3.8) follow by applying (0.4)--(0.5) to the
fourteen K9 target types and reading their three serpent times. They are
independently reconstructed by the audit script. For (3.9), the roots and
their masses are computed in Section 5, where they sum to \(125+5=130\).
\(\square\)

### Lemma 3.4 (exact adversarial root-menu recursion)

Fix an owner interval \(J\), put \(Q=Q_J\), and write
\[
                         Q_t=\{u\in Q:\tau(u)=t\}.
\]
Every chronological upset \(V\subseteq Q\) is obtained uniquely by the
following recursion. Start with \(B_0=\varnothing\). At time \(t\), let
\[
 F_t=\{y\in Q_t:\text{some }x\in B_t\text{ satisfies }x<y\}  \tag{3.10}
\]
be the slice forced by earlier selections. Choose any upper set \(A_t\)
of the induced product poset \(Q_t\setminus F_t\), and put
\[
 V_t=F_t\dot\cup A_t,\qquad
 B_{t+1}=B_t\cup V_t.                                \tag{3.11}
\]
Then
\[
                         R_\tau(V)\cap Q_t=A_t,       \tag{3.12}
\]
and consequently
\[
 E_\tau(J)=
 \max_{\text{legal recursion }(3.10)\text{--}(3.11)}
                         \sum_t w(A_t).              \tag{3.13}
\]

#### Proof

The set \(F_t\) is an upper set inside \(Q_t\). Hence
\(F_t\cup A_t\) is upper in the whole time slice. Any later type above a
selected type is placed in the appropriate future forced set. Therefore
the union of (3.11) is a chronological upset. Every type in \(F_t\) has an
earlier strict lower selected type, while no type in \(A_t\) does; same-time
lower types do not destroy exposed-root status. This proves (3.12).

Conversely, given a chronological upset \(V\), take
\(B_t=V\cap\{\tau<t\}\). Upset closure forces \(F_t\subseteq V\).
The residual set \(A_t=(V\cap Q_t)\setminus F_t\) is upper in
\(Q_t\setminus F_t\), and the construction recovers \(V\) uniquely.
Maximizing (3.12) proves (3.13). \(\square\)

Thus the all-\(k\) problem is a weighted adversarial menu process on a
two-dimensional staircase state. Proposition 3.3 shows why selecting the
entire residual slice is not optimal for the adversary: omitting a light
early root can expose heavier later roots.

## 4. Exact multiboundary erosion

Fix one invariant chronological upset \(U\). Write its root banks as
\[
 R_t=R_\tau(U)\cap\tau^{-1}(t),\qquad
 A_t=\bigcup_{u\in R_t}I(u).                         \tag{4.1}
\]
For an arbitrary owner-coordinate set \(A\subseteq P_R\), extend
\(\operatorname{cap}\) additively. Scan times from late to early and put
\[
 S_q=\varnothing,\qquad S_t=A_t\cup S_{t+1},         \tag{4.2}
\]
where times are \(0,\ldots,q-1\). Define the signed local reserve and the
overlap erosion by
\[
 \rho_t=\operatorname{cap}(A_t)-w(R_t),\qquad
 \varepsilon_t=\operatorname{cap}(A_t\cap S_{t+1}). \tag{4.3}
\]

### Theorem 4.1 (erosion telescoping identity)

For every \(U\), without any connectedness or monotonicity hypothesis on
the palettes \(A_t\),
\[
 \boxed{
 w(R_\tau(U))-|\Gamma_R(U)|
       =\sum_{t=0}^{q-1}(\varepsilon_t-\rho_t).}      \tag{4.4}
\]
Consequently global Hall is equivalent to
\[
                    \sum_t\varepsilon_t
                    \le\sum_t\rho_t                 \tag{4.5}
\]
for every invariant chronological upset. In particular, checking only
\(\rho_t\ge0\) for each bank is insufficient.

#### Proof

The new owner capacity introduced when bank \(t\) is added to the carried
suffix palette is
\[
 \operatorname{cap}(S_t)-\operatorname{cap}(S_{t+1})
 =\operatorname{cap}(A_t)-\varepsilon_t.             \tag{4.6}
\]
Summing (4.6) telescopes to \(\operatorname{cap}(S_0)\). By Lemma 2.2,
\(\operatorname{cap}(S_0)=|\Gamma_R(U)|\). Substitute
\(w(R_t)=\operatorname{cap}(A_t)-\rho_t\) and rearrange to obtain (4.4).
The equivalence (4.5) follows from the exposed-root theorem. \(\square\)

Equivalently, the exact carried scalar debt satisfies
\[
 D_q=0,\qquad
 D_t=D_{t+1}+\varepsilon_t-\rho_t,                   \tag{4.7}
\]
and Hall asks for \(D_0\le0\) for every upset. The geometric part of the
carried state is \(S_{t+1}\). If every suffix palette has at most \(C_0\)
interval components, then it can be recorded by at most \(2C_0\) endpoints
plus the scalar debt. Proving a uniform component bound and \(D_0\le0\)
for an adaptive menu construction would therefore give a genuinely
bounded-state multiboundary certificate. Proposition 4.2 below shows that
the first assertion is impossible when required literally for every upset.
Any bounded-state proof must instead aggregate the palette or use the
interval-local profiles of Corollary 3.2.

For two banks, (4.4) is the inclusion--exclusion formula
\[
\begin{split}
 w(R_0\dot\cup R_1)-\operatorname{cap}(A_0\cup A_1)
 ={}&[w(R_0)-\operatorname{cap}(A_0)]\\
   &+[w(R_1)-\operatorname{cap}(A_1)]
     +\operatorname{cap}(A_0\cap A_1).              \tag{4.8}
\end{split}
\]
Thus the intersection is precisely the casualty which separate local
bank tests omit.

### Proposition 4.2 (exact component-count obstruction)

Use the balanced bipartition
\[
 h=\lfloor k/2\rfloor,\qquad \ell=k-h,
\]
the complete strict-lower target ideal, and owner rank
\[
 R=\left\lceil k/2\right\rceil.
\]
For **every** orbit chronology using \(q\) time blocks, some invariant
chronological upset has a root-owner palette with at least
\[
             \left\lceil {1\over3}
             \left\lceil {R\over q}\right\rceil\right\rceil  \tag{4.9}
\]
interval components.

Consequently, if \(q=d(k)+O(1)=\Theta(\sqrt{k})\), the maximum required
number of literal palette components is \(\Omega(\sqrt{k})\). In
particular no proof can carry the exact suffix palette for every upset by
\(O(1)\) interval endpoints.

#### Proof

The top target diagonal has rank \(R-1\) and exactly \(R\) balanced-core
types
\[
                         u_i=(i,R-1-i),
                         \qquad 0\le i\le R-1.        \tag{4.10}
\]
Their owner intervals are
\[
 I(u_i)=[i,\min(i+1,p_+)]\qquad(0\le i<R).           \tag{4.11}
\]
Thus every interval uses at most two consecutive owner coordinates; in the
odd case only the final interval is clipped to a singleton.

Some time block contains a set \(T\) of at least \(\lceil R/q\rceil\) of
these indices. Greedily take the least remaining index and discard it and
the next two integer positions. This selects a subset \(F\subseteq T\) of
size at least
\[
                         \left\lceil |T|/3\right\rceil,       \tag{4.12}
\]
whose distinct indices differ by at least three. Hence their intervals
in (4.11) lie in distinct discrete components.

The family \(U=\{u_i:i\in F\}\) is an invariant chronological upset:
distinct top-target types are incomparable and there is no higher target
rank. Every member is an exposed root because all lie at the same time.
Its palette therefore has \(|F|\) components, proving (4.9). The
asymptotic consequence uses the established
\(d(k)=\Theta(\sqrt{k})\). \(\square\)

This obstruction concerns a literal component list, not the scalar debt
identity and not the \(O(k^2)\) interval-profile test. It does not refute
an aggregate-history or interval-by-interval proof.

## 5. The first exact local-bank obstruction: K9

Take \(h=4,\ell=5,R=5\), so the owner capacities indexed by
\(p=0,1,2,3,4\) are
\[
                         (1,20,60,40,5),             \tag{5.1}
\]
with total \(W=126\). Use the canonical diagonal serpent from the
balanced-core theorem. Its loads are \(125,125,5\). The exact Hall upset
consists of the complete rank-four target layer together with type
\((3,0)\).

Its roots occur in two banks:
\[
\begin{aligned}
 R_1&=\{(3,0)\}\cup\{(i,4-i):1\le i\le4\},\\
 R_2&=\{(0,4)\}.                                    \tag{5.2}
\end{aligned}
\]
Their masses and palettes are
\[
\begin{array}{c|c|c|c}
 t&w(R_t)&A_t&\operatorname{cap}(A_t)\\ \hline
 1&125&[1,4]&125\\
 2&5&[0,1]&21.
\end{array}                                         \tag{5.3}
\]
Thus each bank passes its local shadow inequality. Their overlap is the
owner type \(p=1\), of capacity \(20\). The total reserve is \(0+16\), so
(4.8) gives
\[
                         20-16=4.                    \tag{5.4}
\]
This is the exact global Hall deficiency. The exhaustive companion audit
for the canonical serpent passes \(3\le k\le8\), so K9 is the first
failure in that specified chronology. Equation (5.4) refutes only
independent local-bank certification; an adaptive overlap-aware menu is
not refuted.

## 6. The K46 interior erosion

Take \(h=\ell=23,R=23\) and the monotone increasing diagonal order with
the complete rank-twenty-two target layer separated. For the exact upset
already used in the K46 boundary-staircase obstruction, the root banks are
\[
\begin{aligned}
 R_1={}&\{(9,10),(10,9)\}
       \cup\{(i,20-i):0\le i\le11\},\\
 R_2={}&\{(i,20-i):12\le i\le20\}
       \cup\{(i,21-i):13\le i\le21\}.               \tag{6.1}
\end{aligned}
\]
Direct binomial summation gives
\[
\begin{array}{c|r|c|r|r}
 t&w(R_t)&A_t&\operatorname{cap}(A_t)&\rho_t\\ \hline
1&6\,433\,303\,219\,651&[0,14]&7\,921\,516\,790\,340
 &1\,488\,213\,570\,689\\
2&1\,864\,760\,576\,745&[12,23]&4\,116\,715\,363\,800
 &2\,251\,954\,787\,055.
\end{array}                                         \tag{6.2}
\]
Again both individual root banks have positive reserve. Their overlap is
\([12,14]\), with capacity
\[
                         3\,804\,801\,426\,540.       \tag{6.3}
\]
It exceeds the sum of the two reserves by
\[
 3\,804\,801\,426\,540
 -1\,488\,213\,570\,689
 -2\,251\,954\,787\,055
 =64\,633\,068\,796.                                 \tag{6.4}
\]
The palettes cover the complete owner line, whose capacity is
\[
                         W=8\,233\,430\,727\,600.     \tag{6.5}
\]
Thus (6.4) is exactly the previously certified global min-cut deficiency,
now decomposed into multiboundary overlap erosion. The adaptive five-orbit
K46 menu changes the root banks and eliminates the full-flow deficiency;
the present identity explains what that repair must pay, but does not
generalize the menu to all \(k\).

## 7. Proof-safe frontier

Theorem 3.1 and Theorem 4.1 sharpen the remaining all-\(k\) static clause:

1. owner-side Hall cuts need only be tested on \(O(k^2)\) intervals and
   their clipped northeast rectangles;
2. across chronology blocks, every failure is exactly local reserve minus
   overlap erosion; and
3. an exact palette endpoint list cannot be a bounded carried state at
   depth \(d+O(1)\); Corollary 3.2's interval-local aggregate profile is
   the surviving weaker route.

The following remain **UNPROVED**:

* an adaptive balanced-core chronology with \(d(k)+O(1)\) blocks which
  satisfies (3.1) for every chronological upset;
* a menu-selection theorem forcing the final debt in (4.7) to be
  nonpositive; and
* every literal serialization, protected-host, address/history, residence,
  compiler, and regenerative conclusion.

In particular, this note proves neither an all-\(k\) anchored factor nor
\(\nu(k)\le B(k)+O(1)\).

## 8. Replay

Run

    python3 scratch/audit_balanced_core_multiboundary_erosion_20260802.py

The script reconstructs both chronologies from binomial coefficients,
checks the asserted upsets and exposed-root banks, computes every palette
and reserve in Sections 5--6, and verifies the two erosion identities.
