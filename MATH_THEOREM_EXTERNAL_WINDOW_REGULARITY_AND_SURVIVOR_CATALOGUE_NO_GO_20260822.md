# External-window regularity and the survivor-catalogue no-go

**Date:** 2026-08-22  
**Status:** unconditional benchmark theorem and stopped-law reduction.  The
note proves that the rooted boundary-polymer method extends to shallow
external windows under product and uniform two-slice residual laws.  Its
conclusion is negative for the most direct cover-down proposal: the complete
surviving catalogue has essentially uniform external degrees, whereas the
cover-down floor needs a factor \(1/x\) of positive hole bias.  Thus a proof
for the actual stopped residual must establish a new hole--degree Palm bias,
or construct long hole-rich flag arcs.  No assertion about the unresolved
stopped law is made here.

## 1. External stars and their exact normalization

Put

\[
 b=2r+1,\qquad
 A=\binom br,\qquad
 L=\binom b{r-1}={r\over r+2}A,\qquad
 B={A\over b}=\operatorname {Cat}_r.                 \tag{1.1}
\]

For a permutation \(w=(w_0,\ldots,w_{b-1})\), write

\[
 I_j^w(s)=\{w_s,\ldots,w_{s+j-1}\}                  \tag{1.2}
\]

cyclically.  Its directed punctured configuration is

\[
 E(w)=\{I_r^w(s):s\ne0\}\mathbin{\dot\cup}
      \{I_{r-1}^w(s):s\ne0\}.                       \tag{1.3}
\]

Layer tags are understood.  Thus \(E(w)\) has \(2r\) targets on each
shore.  For \(2\le q\le r-1\), put

\[
 k_q=r-q,\qquad B_q=\binom b{k_q}.                   \tag{1.4}
\]

For a lower \(k_q\)-set \(T\), or an upper
\((b-k_q)\)-set \(T\), let

\[
 \Omega_q(T)=\{w:T\text{ is a full cyclic window of }w\}.       \tag{1.5}
\]

For an upper target one may equivalently use its \(k_q\)-set complement.
A proper subset occurs at a unique start of a fixed cyclic row.  Hence

\[
 \boxed{D_q:=|\Omega_q(T)|
       =b\,k_q!(b-k_q)!={b\,b!\over B_q}.}           \tag{1.6}
\]

Independently retain every lower target with probability \(x\) and every
middle target with probability \(y\ge x\).  Let \(\mathcal C\) be the
labelled catalogue of configurations all of whose targets in (1.3) are
retained, and put

\[
 Z=|\mathcal C|,\qquad
 X_{q,T}=|\mathcal C\cap\Omega_q(T)|,\qquad
 \rho=x^{2r}y^{2r}.                                 \tag{1.7}
\]

The word *labelled* matters only in that two puncture origins of the same
full cyclic row are still two configurations.  We will also treat the
coalesced physical catalogue.  A physical row has either zero, one, or all
\(b\) of its puncture origins surviving: if two distinct origins survive,
their omitted target pairs are different, so all \(b\) middle and all
\(b\) lower windows must be retained.

Every \(E(w)\) has \(4r\) distinct target variables.  Therefore

\[
 \boxed{\mathbb EZ=b!\rho,\qquad
        \mu_q:=\mathbb EX_{q,T}=D_q\rho,\qquad
        {\mathbb EZ\over\mu_q}={B_q\over b}.}         \tag{1.8}
\]

There is also the deterministic incidence identity

\[
 \boxed{\sum_{T\in\binom{[b]}{k_q}}X_{q,T}=bZ}       \tag{1.9}
\]

and the identical upper-shore formula.  Equations (1.8)--(1.9) are the
normalization which will force the no-go theorem.

For later reference, let \(Z^\circ\) count distinct physical rows having
at least one surviving origin, and let \(X^\circ_{q,T}\) count such rows
which contain \(T\).  Under product retention, the survival probability of
one physical row is exactly

\[
 p^\circ=x^{b-1}y^{b-1}\bigl[b-(b-1)xy\bigr].       \tag{1.10}
\]

Indeed, either every window is retained, or the missing middle/lower
windows are confined to one common origin.  Consequently

\[
 \mathbb EZ^\circ=(b-1)!p^\circ,\qquad
 \mathbb EX^\circ_{q,T}={b!\over B_q}p^\circ,\qquad
 {\mathbb EZ^\circ\over\mathbb EX^\circ_{q,T}}={B_q\over b}.    \tag{1.11}
\]

Moreover,

\[
 {\,\mathbb E(Z-Z^\circ)\over\mathbb EZ}=O(xy),\qquad
 X^\circ_{q,T}\le X_{q,T}.                          \tag{1.12}
\]

The same \(O(xy)\) estimate holds in the uniform two-slice model by the
falling-factorial formula: the surplus \(Z-Z^\circ\) is exactly \(b-1\)
times the number of physical rows whose complete two cyclic decks are
retained.  More explicitly, its expectation divided by \(\mathbb EZ\) is

\[
 {b-1\over b}\,
 {m_L-b+1\over L-b+1}\,
 {m_M-b+1\over A-b+1}=O(xy).                       \tag{1.13}
\]

## 2. A shallow external-root boundary theorem

We need one extension of the punctured boundary count.  It is included
here because replacing it by an appeal to ordinary target-degree
concentration would miss the external root.

Fix \(F=E(w)\), and suppose that \(T=I_{k_q}^w(s)\).  Put a cut between
successive positions of \(w\).  Multiplication of cut labels by \(2\)
modulo \(b\) turns the boundary pairs of the middle and lower targets of
\(F\) into edges of lengths \(1\) and \(3\).  They form a subgraph

\[
 \mathcal B_F\subseteq
 \operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\})                 \tag{2.1}
\]

with two edges deleted.  The boundary pair \(R_q\) of the external root
\(T\) has length \(2q+1\).  For \(S\subseteq E(F)\), let

\[
 v_q(S)=|V(R_q\cup\partial S)|,                    \tag{2.2}
\]

where \(\partial S\subseteq\mathcal B_F\) is the set of boundary edges of
the targets in \(S\).  Finally let

\[
 d_q(T,S)=|\{G:T\text{ is a full window of }G, S\subseteq E(G)\}|.
                                                               \tag{2.3}
\]

### Lemma 2.1 (mixed external-root codegree)

There is an absolute \(C\) such that, whenever

\[
 2\le q\le {\sqrt r\over4},\qquad \varnothing\ne S\subseteq E(F),
                                                               \tag{2.4}
\]

one has

\[
 \boxed{{d_q(T,S)\over D_q}
       \le C^{|S|}r^{\,2-v_q(S)}.}                 \tag{2.5}
\]

The same estimate holds for an upper external target after taking its
complement.

#### Proof

We give the gap count, including the point at which the growing distance
\(q\) disappears.  Anchor the external interval \(T\).  Its two boundary
gaps have sizes

\[
                         r-q\quad\hbox{and}\quad r+1+q.         \tag{2.6}
\]

Expose the intervals in \(S\), and list all distinct boundary cuts in the
reference word.  If their positive elementary gaps are
\(g_1,\ldots,g_v\), then

\[
 \sum_i g_i=b,qquad 1\le g_i\le r+1+q.             \tag{2.7}
\]

For a fixed positional realization, labels may be assigned independently
inside its labelled Venn cells.  Let \(V\) be the product of their
factorials.  The following anchored refinement inequality is the needed
count:

\[
 P_q(S)V
 \le C^{|S|}(r-q)!(r+1+q)!\,r^{\,2-v_q(S)},        \tag{2.8}
\]

where \(P_q(S)\) is the number of relative positional realizations with
the prescribed labelled Venn signature, the start of \(T\) being fixed.

Here is a direct verification of (2.8).  Refining the two root cells by
the membership vectors of \(S\) gives

\[
 {V\over(r-q)!(r+1+q)!}
 ={1\over
   \binom{r-q}{(n_\sigma)_{\sigma:T=1}}
   \binom{r+1+q}{(n_\sigma)_{\sigma:T=0}}}.         \tag{2.9}
\]

Here \(\binom n{(n_i)_i}=n!/\prod_i n_i!\), with zero cells omitted.

Put \(G=\prod_i g_i!\).  We track simultaneously the positional
multiplicity and the refinement ratio \(V/G\).  If the two new cuts lie
in distinct old gaps, fixing the labels outside those gaps injects the
gap choices into the Venn-cell choices, so \(V/G\) does not increase.  If
both cuts lie in one ordinary gap, write its three pieces as \(u,m,v\).
The middle piece, or its complement, has size in
\(\{r-1,r,r+1,r+2\}\).  Since an ordinary gap has size at most \(r+2\),
the two outside pieces have total size at most three.  Thus the possible
merging loss in \(V/G\) is at most
\(\binom{u+v}{u}\le2^3\).

The only new case is a root-descended gap of size \(g\ge r-1\).  Put
\(d=u+v=g-m\le q+2\).  The possible merging loss in \(V/G\) is at most
\(\binom du\), and there are at most \(d+1\) corresponding positional
splits.  On the other hand this gap refinement changes \(G\) by the exact
factor

\[
 {u!m!v!\over g!}
 ={1\over\binom gd\binom du}.                       \tag{2.10}
\]

The merging and positional factors therefore leave only

\[
 {d+1\over\binom gd}.                               \tag{2.11}
\]

For \(2\le d\le q+2\le\sqrt r/2\), this quantity decreases with \(d\):
the ratio of its \((d+1)\)-st term to its \(d\)-th term is
\((d+2)/(g-d)\le1\).  Hence

\[
 {d+1\over\binom gd}
 \le {3\over\binom g2}\le {16\over r^2}.           \tag{2.12}
\]

For \(d=0,1\), respectively zero or one genuinely new boundary cut is
created, and the factors are \(1\) or at most \(4/r\).

It remains only to record the ordinary gap majorization used by this
iteration.  Log-convexity of factorials, (2.7), and
\((n)_j\ge(n/e)^j\) give

\[
 {G\over(r-q)!(r+1+q)!}
 \le C^{v_q(S)}r^{\,2-v_q(S)}.                     \tag{2.13}
\]

For \(v_q(S)\le r-q+1\), the maximizing gap list is bounded by
\((r+1+q)!(r-q-v_q(S)+2)!\), so (2.13) follows directly from
\((r-q)_{v_q(S)-2}\).  For larger \(v_q(S)\), the same transfers leave
one gap of size \(b-v_q(S)+1\) and all other gaps of size one; the same
falling-factorial inequality is stronger.

The falling-factorial inequality used here follows from
\(\binom nj\ge(n/j)^j\) and \(j!\ge(j/e)^j\); the first is obtained by
comparing ordered samples with samples allowing repetition, and the
second by the elementary integral bound for \(\log(j!)\).

We now make the positional-branch multiplication precise.  Fix an ordering
\(S_1,\ldots,S_t\), and retain \(S_1\) as a positional anchor after the
first level.  The **exposure tree** at level \(i\) has as nodes all
relative start tuples for \(T,S_1,\ldots,S_i\) with the prescribed
labelled Venn signature; the start of \(T\) is fixed.  A node is weighted
by the number \(V_i\) of labelings of its Venn cells.  Therefore the sum
of the level-\(t\) node weights is exactly \(P_q(S)V\).

Consider one old Venn cell \(C\), of size \(n_C\), which is a disjoint
union of old elementary gaps \(H\).  If the new target takes \(p_H\)
labels from \(H\) and \(p_C=\sum_Hp_H\), then

\[
 \prod_{H\subseteq C}\binom{|H|}{p_H}
 \le\binom{n_C}{p_C}.                               \tag{2.13b}
\]

For one fixed positional child this is an injection: independently chosen
subsets in the gaps have disjoint union a \(p_C\)-subset of \(C\), and
intersecting that union back with each gap recovers both the allocation and
every chosen subset.  Summing over allocations for that child gives the
Vandermonde identity
\[
 \sum_{\sum p_H=p_C}\prod_H\binom{|H|}{p_H}
 =\binom{n_C}{p_C}.                                 \tag{2.13c}
\]
Different positional children can use different ordered endpoint gaps.
At the first level their number is the \(d+1\) root-relative multiplicity
already charged in (2.11).  At every later level, once the start of
\(S_1\) is fixed, the elementary two-arc formula gives at most four starts
for \(S_i\) having its prescribed intersection size with \(S_1\).
Therefore (2.13b)--(2.13c), with one additional factor at most four, bound
the **sum over all children**, not just one chosen positional branch.  The
argument remains valid when one Venn cell is a union of noncontiguous
root-descended gaps; those gaps enter the single Vandermonde sum, rather
than contributing a product of their number.

Apply this injection independently in every old Venn cell.  If the two
new cuts are in distinct gaps, all child multiplicity is absorbed by
(2.13b)--(2.13c).  If they are in one ordinary gap, the only information
forgotten by the union map is the division of at most three outside
positions, giving the factor \(2^3\) above.  In a root-descended gap, the
forgotten division is \(\binom du\), while the \(d+1\) possible placements
are paid by the exact gap factor (2.10); their net contribution is
(2.11), bounded in (2.12) by one factor \(4/r\) per new reference
boundary cut.  Coincident old cuts cost one.  These cases exhaust the
children because an interval has exactly two boundary cuts.

To state the induction invariant explicitly, let \(v_i^*\) be the number
of boundary cuts of \(T,S_1,\ldots,S_i\) in the fixed reference word.
After summing the weights of all level-\(i\) nodes and retaining their
current elementary-gap factorial products, the invariant is

\[
 \sum_{\eta\text{ at level }i}V_i(\eta)
 \le C^i(r-q)!(r+1+q)!\,r^{\,2-v_i^*}.             \tag{2.13d}
\]

At level zero this is equality.  For the induction step, a coincident
reference cut uses no power of \(r\).  A reference cut in a distinct gap
uses one of the injective binomial choices in (2.13b); summing over all
gaps is (2.13c), and the terminal factorial envelope (2.13) supplies its
factor \(r^{-1}\).  If both cuts are in one reference gap, (2.10)--(2.12)
supply exactly \(r^{-1}\) or \(r^{-2}\) according as one or two reference
cuts are new.  This remains true when an alternative child makes one of
those cuts coincident: that child is one of the \(d+1\) placements already
summed in (2.11), rather than a new multiplicity.  Thus every child in the
exposure tree is counted once and the induction proves (2.13d).

Gap refinements telescope from \((r-q)!(r+1+q)!\) to the terminal \(G\);
(2.13) is exactly the envelope used at the distinct-gap steps.  The at
most two orientations and two layer lengths at each level are absorbed
into \(C^i\).  Finally \(v_q(S)\le2|S|+2\), so the factor
\(C^{v_q(S)}\) implicit in (2.13) is absorbed into one absolute base to
the power \(|S|\).  At \(i=t\), (2.13d) is

\[
 P_q(S){V\over(r-q)!(r+1+q)!}
 \le C^{|S|}r^{\,2-v_q(S)},                        \tag{2.13a}
\]

which is (2.8).  Notice that (2.10)--(2.12), not the crude bound
\(2^d\), is what makes the constant independent of the growing \(q\).

There are \(b\) choices for the anchored start of \(T\).  Multiplying
(2.8) by \(b\), and dividing by
\(D_q=b(r-q)!(r+1+q)!\), proves (2.5).  Disallowing the punctured start can
only reduce the count.  Complementation preserves boundary pairs, proving
the upper-shore assertion.  \(\square\)

### Lemma 2.2 (two-root polymer sum)

For a sufficiently small absolute \(c_0>0\), uniformly in the range
(2.4) and \(0\le z\le c_0\sqrt r\),

\[
 \sum_{\varnothing\ne S\subseteq E(F)}
 z^{|S|}r^{\,2-v_q(S)}
 =O\left({z\over r}+{z^3\over r}+{z^4\over r^2}\right).       \tag{2.14}
\]

#### Proof

The graph \(\mathcal B_F\) has maximum degree four.  Every \(m\)-edge
subgraph with \(v\) nonisolated vertices satisfies

\[
                         m\le2(v-1).               \tag{2.15}
\]

For completeness, the full circulant is the union of the step-\(1\) and
step-\(3\) two-factors.  Every proper nonempty vertex set has at least two
step-\(1\) boundary edges.  If it also cuts a step-\(3\) cycle, it has at
least two boundary edges there.  Otherwise it is a union of step-\(3\)
cycles.  This is impossible when \(\gcd(3,b)=1\), and when
\(\gcd(3,b)=3\) a nontrivial union of residue classes has at least four
step-\(1\) boundary edges.  Thus every proper cut has size at least four,
so its induced edge count is at most \(2v-2\).  On all \(b\) vertices,
the two deleted edges leave \(2b-2\) edges.  This proves (2.15).

It is triangle-free for all sufficiently large \(r\); the finite
exceptions alter only the absolute constants: a three-step signed sum
from \(\{1,3\}\) has odd absolute value at most nine and cannot vanish
modulo \(b\ge11\).  Adding the fixed chord
\(R_q\) raises the maximum degree by at most one.  It creates no triangle:
two signed elements of \(\{1,3\}\) have integer sum in
\(\{0,\pm2,\pm4,\pm6\}\).  For \(q=2\), the root length is \(5\); for
\(q\ge3\), it is at least \(7\).  In the range (2.4) there is no modular
wrap, so neither can be such a sum.

Decompose \(S\) into connected components in \(\mathcal B_F\).  Components
meeting neither endpoint of \(R_q\) have total activity

\[
 \eta_0=O(z/r+z^4/r^2).                             \tag{2.16}
\]

Indeed, a connected \(m\)-edge subgraph has at most \(C_0^m\) exploration
words from a prescribed root; use two, three, and at least four vertices
for \(m=1,2,3\), and (2.15) thereafter.  This is the usual unrooted
boundary-polymer calculation.

A component meeting a prescribed endpoint of \(R_q\) has activity

\[
 O(z/r+z^2/r^2+z^3/r+z^4/r^2).                    \tag{2.17}
\]

The first two terms use triangle-freeness; (2.15) and a geometric tail
give the last two.  There are only two root endpoints.  Dropping
disjointness between all other components multiplies their contribution by
at most \(e^{\eta_0}\).  Subtracting the empty family and absorbing
\(z^2/r^2\) proves (2.14).  \(\square\)

## 3. External degrees concentrate at the uniform scale

### Theorem 3.1 (product external-degree variance)

Let \(x\ge r^{-\alpha}\), where \(\alpha<1/3\) is fixed, and let
\(y\ge x\).  Uniformly for

\[
                         2\le q\le{\sqrt r\over4},              \tag{3.1}
\]

and every external target on either shore,

\[
 \boxed{
 {\operatorname {Var}X_{q,T}\over\mu_q^2}
 \le {1\over\mu_q}+O\left({1\over rx^3}\right)=o(1).}         \tag{3.2}
\]

#### Proof

Write \(I_F\) for the event that \(F\in\mathcal C\).  If
\(t(F,G)=|E(F)\cap E(G)|\), then

\[
 {\mathbb E(I_FI_G)\over\mathbb EI_F\,\mathbb EI_G}
 \le x^{-t(F,G)}.                                   \tag{3.3}
\]

Put \(a=x^{-1}-1\).  For \(F\in\Omega_q(T)\),

\[
 x^{-t(F,G)}-1
 =\sum_{\varnothing\ne S\subseteq E(F)\cap E(G)}a^{|S|}.
                                                               \tag{3.4}
\]

Separate the diagonal variance, sum (3.4) over \(G\in\Omega_q(T)\), and
double-count the configurations containing \(T\cup S\).  Lemma 2.1 gives

\[
 {\operatorname {Var}X_{q,T}\over\mu_q^2}
 \le {1\over\mu_q}+
 \max_{F\in\Omega_q(T)}
 \sum_{\varnothing\ne S\subseteq E(F)}
       (Ca)^{|S|}r^{\,2-v_q(S)}.                  \tag{3.5}
\]

Apply Lemma 2.2 with \(z=Ca\).  Since
\(a=O(x^{-1})=o(\sqrt r)\), its right side is

\[
 O\left({a\over r}+{a^3\over r}+{a^4\over r^2}\right)
 =O\left({1\over rx^3}\right).                    \tag{3.6}
\]

Finally,

\[
 \mu_q\ge (r-q)!(r+1+q)!\,x^{4r}
          =\exp((2-4\alpha+o(1))r\log r),          \tag{3.7}
\]

so \(1/\mu_q=o(1)\).  \(\square\)

The exact first-overlap calculation is a useful check on the scale.  If a
full \(h\)-window \(S\), \(h\in\{r-1,r\}\), meets a fixed \(k_q\)-window
in \(a\) elements, then, conditional on the latter being a window of a
uniform cyclic row,

\[
 \Pr(S\text{ is also a window})
 ={m_{k_q,h}(a)\over
   \binom{k_q}a\binom{b-k_q}{h-a}},                 \tag{3.8}
\]

where

\[
 m_{k,h}(a)=
 \begin{cases}
 b-k-h+1,&a=0,\\
 2,&0<a<\min(k,h),\\
 |k-h|+1,&a=\min(k,h).
 \end{cases}                                       \tag{3.9}
\]

Summing (3.8) over the two complete \(q=1\) decks of a reference row gives

\[
 \kappa_q=
 \sum_{h\in\{r-1,r\}}\sum_{a=0}^{k_q}
 {m_{k_q,h}(a)^2\over
  \binom{k_q}a\binom{b-k_q}{h-a}}.                 \tag{3.10}
\]

For \(q=2\), the containment term \(h=r-1,a=k_q\) is
\(4/(r+3)\).  The two endpoint terms in the other layer are \(O(r^{-2})\)
and \(O(r^{-3})\), and the remaining reciprocal-binomial terms total
\(O(r^{-2})\).  Hence
\(\kappa_2=4/r+O(r^{-2})\), agreeing with the linear \(a/r\) term in the
deliberately uniform bound (3.6).

## 4. Exact-size residual shores do not change the conclusion

Let \(R_L\) be a uniformly random \(m_L\)-subset of the lower shore and
\(R_M\) an independent uniformly random \(m_M\)-subset of the middle
shore.  Put

\[
 x={m_L\over L},\qquad y={m_M\over A},              \tag{4.1}
\]

and let \(\mathcal C,X_{q,T},Z\) be defined by containment in
\(R_L\dot\cup R_M\).  The exact common survival probability of one
configuration is

\[
 \rho_*= {(m_L)_{2r}\over(L)_{2r}}
          {(m_M)_{2r}\over(A)_{2r}}.               \tag{4.2}
\]

Thus (1.8) remains exact with \(\rho_*\) in place of \(\rho\).

### Theorem 4.1 (uniform two-slice external regularity)

Assume \(x,y\ge r^{-\alpha}\) for fixed \(\alpha<1/3\).  Uniformly in
(3.1),

\[
 {\operatorname {Var}X_{q,T}\over(D_q\rho_*)^2}
 \le O\left({1\over rx^3}\right)+e^{-\Omega(r)}.   \tag{4.3}
\]

#### Proof

For \(u\le4r\) and \(m/N\ge r^{-\alpha}\),

\[
 {(m)_u\over(N)_u}
 =\left({m\over N}\right)^u
   \exp\left(O\left({u^2\over m}\right)
             +O\left({u^2\over N}\right)\right).  \tag{4.4}
\]

Both shore sizes are exponential in \(r\), so the exponential factor in
(4.4) is \(1+e^{-\Omega(r)}\), uniformly in every union of two
configurations.  Consequently the first and second moments in the uniform
two-slice model equal their product-measure counterparts, with relative
error \(e^{-\Omega(r)}\).  Apply Theorem 3.1.  \(\square\)

Thus exact shore cardinalities are not a source of the desired \(1/x\)
external bias.

## 5. The full surviving catalogue cannot satisfy the cover-down floor

Take

\[
 Q=\left\lfloor{\sqrt{rx}\over4}\right\rfloor,     \tag{5.1}
\]

and assume

\[
              x=o(1),\qquad rx^3\longrightarrow\infty.         \tag{5.2}
\]

For example, (5.2) holds when \(x=r^{-\alpha}\) with fixed
\(\alpha<1/3\).  For \(q\le Q\),

\[
 {B_q\over L}\ge1-{(q-1)(q+2)\over r}\ge1-{x\over8}.          \tag{5.3}
\]

Suppose \(\mathcal H_q^\pm\) are any, possibly residual-dependent,
shore-tagged target sets satisfying the punctured-bank capacity lower
bound

\[
 \sum_{q=2}^Q(|\mathcal H_q^-|+|\mathcal H_q^+|)
 \ge c_0xAQ                                           \tag{5.4}
\]

for some fixed \(c_0>0\).  Removing \(q=1\) changes the usual lower bound
only by \(O(xA)\), so (5.4) holds for the actual shallow holes with, say,
any fixed \(c_0<7/4\) and all sufficiently large \(r\).

### Theorem 5.1 (uniform-slice survivor-catalogue no-go)

Fix \(K>0\).  In either the product model of Section 1 or the uniform
two-slice model of Section 4, with probability \(1-o(1)\) there do not
exist \(D_0>0\) and an exceptional set \(\mathcal E\) of \(o(A)\) tagged
targets such that

\[
 X_{q,T}\ge D_0
 \quad(T\in\mathcal H_q^\pm\setminus\mathcal E),
 \qquad {Z\over D_0}\le KxB.                       \tag{5.5}
\]

The same assertion holds with \(Z^\circ,X^\circ_{q,T}\) in place of
\(Z,X_{q,T}\).  Thus neither all labelled survivors nor all distinct
surviving physical rows satisfy the external-window floor.  This remains
true even if the putative hole sets are selected after the residual shores
are revealed.

#### Proof

Let

\[
                         \eta={C\over rx^3}+e^{-\Omega(r)}.     \tag{5.6}
\]

At \(q=2\), Chebyshev and Theorems 3.1--4.1 show that the expected number
of lower targets with \(X_{2,T}<\mu_2/2\) is at most
\(4\eta B_2=o(B_2)\).  With probability \(1-o(1)\), at least \(B_2/2\)
targets are not of this type.  The exact identity (1.9) then gives

\[
 Z\ge {B_2\mu_2\over4b}={\mathbb EZ\over4},         \tag{5.7}
\]

where \(\mu_q=D_q\rho\) or \(D_q\rho_*\), as appropriate.

For the coalesced catalogue, (1.12), its uniform-slice analogue, and
Markov's inequality give

\[
                         Z^\circ\ge{\mathbb EZ\over8}            \tag{5.7a}
\]

with probability \(1-o(1)\).  Also \(X^\circ_{q,T}\le X_{q,T}\).  Hence
the rest of the argument below applies simultaneously to the labelled and
coalesced catalogues, after changing one absolute constant.

On the event (5.7), the second inequality in (5.5) would imply

\[
 D_0\ge {Z\over KxB}
 \ge {\mathbb EZ\over4KxB}
 ={B_q\over4KxA}\,\mu_q
 \ge {c_1\over Kx}\mu_q                       \tag{5.8}
\]

for every \(2\le q\le Q\), using (5.3) and \(L/A\to1\).

Call a tagged target \(K\)-enriched if

\[
                         X_{q,T}\ge {c_1\over Kx}\mu_q.        \tag{5.9}
\]

For large \(r\), the threshold in (5.9) is at least twice the mean.
Chebyshev gives, uniformly in \(q\le Q\),

\[
 \Pr(T\text{ is }K\text{-enriched})
 \le C_Kx^2\eta
 =O_K\left({1\over rx}\right).                    \tag{5.10}
\]

There are at most \(2QA\) tagged targets in the band.  If \(N_K\) is the
number of enriched ones, then

\[
                         \mathbb EN_K
 \le {C_KQA\over rx}.                              \tag{5.11}
\]

Since \(rx^2\to\infty\), Markov's inequality yields

\[
                         N_K=o(xAQ)                 \tag{5.12}
\]

with probability \(1-o(1)\).  But (5.2) also gives

\[
 {xAQ\over A}=xQ=(1+o(1)){\sqrt r\,x^{3/2}\over4}\longrightarrow\infty.
                                                               \tag{5.13}
\]

Thus an exceptional \(o(A)\) set removes only \(o(xAQ)\) members of
(5.4).  Equations (5.8)--(5.9) would make all remaining
\(\Omega(xAQ)\) holes enriched, contradicting (5.12).  \(\square\)

The proof also records a quantitative event bound.  For the labelled
catalogue, the probability that (5.5) holds is at most

\[
 O_K\left({1\over rx^3}+{1\over rx^2}\right)=o(1).              \tag{5.14}
\]

For the coalesced catalogue add \(O(xy)\), the probability cost in
(1.12).  No independence between the residual-dependent hole sets and the
external degrees was used.

The theorem is not a no-go for a hole-dependent **subcatalogue** or a
nonuniform positive weighting.  It says precisely that such a selection
must create the missing factor \(1/x\); it cannot be obtained by assigning
one common weight to every survivor.

## 6. Exact stopped statistic which remains open

Let \(\mathcal P\) now be the actual matching produced by the stopped
isolated-edge process, let \(\mathcal C(\mathcal P)\) be its surviving
configuration catalogue, and let \(Z(\mathcal P)\) and
\(X_{q,T}(\mathcal P)\) be defined as above.

First, there is a useful stopped-event obstruction to trying to
prove ordinary external-degree regularity along the trajectory.

### Theorem 6.1 (bounded external hazard leaves macroscopic holes)

At round \(j\), let \(\mathcal C_j\) be the surviving configuration
catalogue, \(Z_j=|\mathcal C_j|\), \(M_j\) the residual middle shore, and

\[
 p_j={\gamma\over r\bar d_j^M}
     ={\gamma|M_j|\over2r^2Z_j}                    \tag{6.H.1}
\]

the independent marking rate.  Fix one depth \(q\ge2\), and let
\(X_{q,j}(T)\) be the number of configurations in \(\mathcal C_j\) whose
full row contains \(T\).  Stop at the first cap/bite failure or at the
desired density threshold.  Suppose every pre-stopping good state obeys

\[
 X_{q,j}(T)\le K_E{bZ_j\over B_q}\quad\hbox{for every tagged }T,
 \qquad B_q\ge c_BA,                                \tag{6.H.2}
\]

and every good trajectory obeys

\[
 p_j\le{1\over2},\qquad
 \sum_{j<\tau}{|M_j|\over A}\le C_0r.              \tag{6.H.3}
\]

Then an absolute \(c=c(\gamma,K_E,c_B,C_0)>0\) satisfies

\[
 \boxed{\Pr(\text{a cap/bite failure occurs before the threshold, or }
             T\text{ is a full-bank hole at the threshold})\ge c}       \tag{6.H.4}
\]

for every tagged target \(T\) at that depth.

#### Proof

Conditional on the history before round \(j\), the probability that none
of the \(X_{q,j}(T)\) configurations in the external star of \(T\) is
marked is

\[
                         (1-p_j)^{X_{q,j}(T)}.       \tag{6.H.5}
\]

The first part of (6.H.3) and
\(\log(1-p_j)\ge-2p_j\) give the product lower bound below.
Equations (6.H.1)--(6.H.3) also give, on every good
trajectory,

\[
 \sum_{j<\tau}p_jX_{q,j}(T)
 \le {\gamma K_Eb\over2r^2B_q}\sum_{j<\tau}|M_j|
 \le {\gamma K_EC_0b\over2c_Br}=O_{\gamma,K_E,c_B,C_0}(1).      \tag{6.H.6}
\]

For completeness, let \(A_j\) be the event that no external-star
configuration has been marked before round \(j\), and put
\(\Lambda_j=\sum_{i<j}p_iX_{q,i}(T)\) up to the stopping time.  From
(6.H.5),

\[
 \mathbb E\!\left[
  \mathbf1_{A_{j+1}}e^{2\Lambda_{j+1}}
  \,\middle|\,\mathcal F_j\right]
 \ge \mathbf1_{A_j}e^{2\Lambda_j}.                  \tag{6.H.7}
\]

Thus the stopped variables on the left form a nonnegative submartingale.
The deterministic trajectory bound (6.H.6) is at most some constant
\(\Lambda\), so

\[
 1\le
 \mathbb E[\mathbf1_{A_\tau}e^{2\Lambda_\tau}]
 \le e^{2\Lambda}\Pr(A_\tau).                       \tag{6.H.8}
\]

Hence \(\Pr(A_\tau)\ge e^{-2\Lambda}\).  On \(A_\tau\), either the stopped
process encounters a declared failure, or no accepted configuration can
have a full-row occurrence of \(T\).  This is (6.H.4).  No conditioning
on the future event of cap persistence is used.  \(\square\)

The geometric descent has (6.H.3): a constant-order \(1/r\) fractional
decrease per good round makes the sum of the successive middle densities
\(O(r)\), even though the number of rounds is \(O(r\log r)\).  Therefore,
if cap/bite failure has probability \(o(1)\), (6.H.4) implies

\[
                         \mathbb Eh_q^\pm=\Omega(B_q)=\Omega(A)          \tag{6.H.9}
\]

under an all-target external cap such as (6.H.2).  Thus ordinary quenched
external-degree regularity would be actively incompatible with the
capacity-minimal \(O(xA)\) hole profile.  A successful stopped law must
instead create substantial external inhomogeneity and align its
high-degree portion with the holes.

We now state that exact alignment statistic:

\[
 \mathfrak N_K(\mathcal P)=
 \sum_{q=2}^Q\sum_{\pm}
 \left|\left\{T\in\mathcal H_q^\pm(\mathcal P):
 X_{q,T}(\mathcal P)
 \ge {Z(\mathcal P)\over KxB}\right\}\right|.       \tag{6.1}
\]

The preceding proof gives the following deterministic implication:

\[
 \boxed{
 \begin{array}{c}
 \text{the full surviving catalogue satisfies the external floor outside}
 \ o(A)\text{ holes}
 \end{array}
 \Longrightarrow
 \mathfrak N_K(\mathcal P)=\Omega(xAQ).}            \tag{6.2}
\]

For a uniform residual two-slice of the same shore sizes, Theorem 5.1
instead gives

\[
                         \mathfrak N_K=o(xAQ)        \tag{6.3}
\]

with high probability, even if the candidate hole sets are chosen after
the slice.  Therefore the desired stopped theorem is not an ordinary
de-Poissonization or degree-regularity transfer.  It must prove a genuine
history-induced **hole--high-degree alignment** of order \(1/x\).

The rooted boundary-polymer method controls \(X_{q,T}\) after a fixed
external root and proves (6.3) at the uniform benchmark.  It does not by
itself control the joint Palm statistic

\[
 \mathbb E\left[
  \mathbf1_{\{T\in\mathcal H_q^\pm(\mathcal P)\}}
  X_{q,T}(\mathcal P)
 \right],                                           \tag{6.4}
\]

because the hole event records accepted configurations throughout the
history, not merely the final two shore cardinalities.  Equation (6.4),
or a positive hole-dependent subcatalogue producing the same factor, is
the sharp new probabilistic input.

## 7. The separate long-flag-arc input

For a full row \(C\) and a cyclic interval \(J\) of \(L_0\) starts, put

\[
 S(C,J)=\sum_{s\in J}\sum_{q=2}^Q
 \left(
  \mathbf1_{\{I_{r-q}^C(s)\in\mathcal H_q^-\}}
 +\mathbf1_{\{I_{r+1+q}^C(s)\in\mathcal H_q^+\}}
 \right).                                          \tag{7.1}
\]

If \(M=O(xA/L_0)\) such arcs cover all but \(o(A)\) shallow holes, then
the same occurrence count as in (5.4) forces

\[
 \boxed{\sum_{j=1}^M S(C_j,J_j)=\Omega(xAQ),
 \qquad {1\over M}\sum_{j=1}^M S(C_j,J_j)
        =\Omega(L_0Q).}                             \tag{7.2}
\]

Thus a successful arc family must have constant-density hole flags, not
the \(O(x)\)-density supplied by a uniform row.  If the arcs are required
to lie in surviving configurations, the missing stopped statistic is

\[
 \mathbf1_{\{C\in\mathcal C(\mathcal P)\}}
 \mathbf1_{\{S(C,J)\ge cL_0Q\}}.                   \tag{7.3}
\]

The external-degree theorem neither proves nor disproves that tail for the
actual history.  It shows why target-retention polymer estimates alone are
insufficient: a long-arc theorem must couple survival to the previous
accepted-bank hole field.

## 8. Verdict

The same rooted boundary geometry **does** extend to all shallow external
windows needed by the capacity obstruction.  At the product and uniform
two-slice benchmarks it proves external-degree regularity, not the desired
cover-down bias.  Consequently:

1. the complete surviving catalogue cannot satisfy the \(O(xB)\)
   degree-floor interface;
2. exact-size conditioning does not repair it;
3. any positive continuation must construct a hole-biased subcatalogue or
   weighting, prove the stopped Palm alignment (6.2), or prove the separate
   long-flag-arc tail (7.3).

This removes “apply the existing polymer bound to every external degree”
as a possible completion.  The remaining issue is a specific
history-dependent positive-correlation theorem, not another marginal
degree estimate.
