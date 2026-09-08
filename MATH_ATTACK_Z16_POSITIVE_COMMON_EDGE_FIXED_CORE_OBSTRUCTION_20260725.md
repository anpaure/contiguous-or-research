# Positive-winding quotient packing: internal near-height charge, corner absorption, and the endpoint obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome and exact scope

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,
 \qquad H_A=\lceil A\sqrt r\rceil .
\]

The newly audited critical-corner argument uses the following exact
packing principle.  If every interval in a quotient-edge-disjoint family
contains a distinguished quotient edge, then charging to that edge is
injective.  In the critical corner family the distinguished root is

\[
 1^s0^K Y0^s,
\]

it is independent of the phase pair, and its deterministic collars make
the set of possible charged roots exponentially smaller than
\(B_r/\sqrt r\).

There is also a new genuinely chronological positive result.  Every
nonempty lag-two cell forces a near-equal-height Dyck split at one of its
three even phases.  Consequently the complete lag-two positive-cell
sector has size

\[
 \boxed{O(B_r/r^{3/4})=o(B_r/\sqrt r).}
 \tag{0.0}
\]

The proof is an exact word calculation inside \(D_1,D_2,D_3\).  It uses
neither transported token labels nor the retracted same-label
maximal-overlap argument.  The same calculation iterates: every fixed lag
is negligible.  More strongly, for every deterministic

\[
 L=o\!\left(\sqrt{r/\log(r+2)}\right),
\]

the aggregate quotient packing of all nonempty cells with lag at most
\(L\) is \(o(B_r/\sqrt r)\).  The charge is one actual intervening root
whose canonical Dyck split has heights within \(L\); it is injective
across the packing.  Thus the unresolved positive sector may be restricted
to genuinely large, near-Gaussian lags.

This note proves a sharp obstruction to extending that argument from the
fixed-core endpoint square alone.

It also gives one positive closure which is directly relevant to the
positive-winding line.  A positive-winding parent may contain a nested
simple zero-winding return.  If that nested return belongs to the audited
critical-corner family, the same corner edge charges the **parent** after
the exact even/odd containment split.  Thus the critical-corner bound
removes all positive-winding parents which contain a Gaussian-size member
of that family; positivity of the parent's winding creates no escape from
the common edge.

### Theorem B (nested critical corners absorb arbitrary parents)

Fix \(0<\alpha<A<\infty\).  Let \(\mathcal P\) be a pairwise
quotient-edge-disjoint family of nonwrapping PBBS return intervals of gap
at most \(2H_A-1\), with arbitrary winding.  Suppose every
\(I\in\mathcal P\)
contains a chronological return subinterval \(J_I\) from the audited
critical-corner family, with corner parameter

\[
 \alpha\sqrt r\le s(J_I)\le A\sqrt r.
\]

Then

\[
 \boxed{
 |\mathcal P|
 \le {4\over3}\,4^r4^{-\lceil\alpha\sqrt r\rceil}
 =o_{\alpha,A}(B_r/\sqrt r).}
 \tag{0.3}
\]

In particular (0.3) applies when every member of \(\mathcal P\) has
positive winding.  This is a genuine quotient-packing theorem; it does
not count physical labels or use the retracted same-label overlap kernel.

### Theorem A (every Dyck root has a Gaussian-size core-swap mate)

Let \(D\) be a Dyck word of semilength \(r\) and height \(h\), and put

\[
 s=h.
\]

There is a Dyck word \(D^\#\) of semilength \(r\) such that

1. \(D\) and \(D^\#\) agree in exactly \(2s\) positions;
2. among the agreeing positions, exactly \(s\) carry the bit one and
   exactly \(s\) carry the bit zero; and
3. at every other position their bits are complementary.

Consequently \((D,D^\#)\) is the pair of boundary roots of an exact
fixed-core simple Kneser return of gap \(2s+1\), with inactive cores of
size \(r-s\).  All labels in its half-open omitted-label word are
pairwise distinct.

Moreover, for every fixed \(A>0\), at least

\[
 \boxed{c_A B_r}
 \tag{0.1}
\]

Dyck roots occur as the first boundary root of such a square with

\[
 s+1\le H_A
\]

for all sufficiently large \(r\), where \(c_A>0\) depends only on
\(A\).  In particular

\[
 {c_AB_r\over B_r/\sqrt r}=c_A\sqrt r\longrightarrow\infty.
 \tag{0.2}
\]

Thus neither the fixed-core normal form, the endpoint core-swap square,
nor the fact that the two endpoint roots are complementary off
\(O_A(\sqrt r)\) coordinates can furnish an
\(o(B_r/\sqrt r)\) endpoint charge.  The successful critical-corner
argument uses strictly more information: one internal \(\tau\)-phase is
common to all phase choices, and its word has uniquely parseable long
collars.

Theorem A is **not** a positive-winding PBBS counterexample.  The
intermediate owners form a literal integral Kneser return path, but their
ordered roots are not asserted to satisfy the canonical recursion

\[
 D_{j+1}=\tau D_j.
\]

The construction now has \(s=h\), so its gap \(2h+1\) meets the known
PBBS height--gap lower bound exactly.  However, it is not asserted that
\(D^\#\) has the same height as \(D\); actual \(\tau\)-orbit endpoints
do have equal invariant height.  Equal endpoint height and internal
\(\tau\)-chronology are therefore additional restrictions not refuted by
Theorem A.

Accordingly the exact positive-winding quotient-packing gate remains
open.  The theorem decisively closes only the route which tries to derive
the needed common edge or its rarity from fixed-core endpoint data
without using internal literal PBBS chronology.

## 1. The exact common-edge packing lemma

For a quotient return interval \(I\), let \(Q(I)\) denote its full
quotient-edge support, including both boundary edges.

### Lemma 1.1 (literal support charge)

Let \(\mathcal P\) be pairwise quotient-edge-disjoint.  Suppose a map
\(\chi\) assigns to every \(I\in\mathcal P\) a root \(\chi(I)\) such
that

\[
 e_{\chi(I)}\in Q(I).
 \tag{1.1}
\]

Then \(\chi\) is injective.  Hence, if every charged root lies in a set
\(\mathcal C_r\),

\[
 \boxed{|\mathcal P|\le |\mathcal C_r|.}
 \tag{1.2}
\]

#### Proof

If \(\chi(I)=\chi(J)\), then the quotient edge
\(e_{\chi(I)}\) belongs to both supports.  Edge-disjointness gives
\(I=J\).  This is exactly injectivity, and (1.2) follows. \(\square\)

The critical-corner theorem is a particularly strong application of
Lemma 1.1.  Its internal edge is independent of the two phase parameters,
and the root itself recovers \((s,K,Y)\).  Both properties matter.  A
common reduced edge, a common unlabelled core, or an endpoint relation
which still allows Catalan-many full roots does not imply (1.2) with a
small set \(\mathcal C_r\).

### Proof of Theorem B

Lift one parent interval \(I\) to ordinary chronological indices, and
let \(a(I)\) be the number of one-step PBBS edges from the beginning of
\(I\) to the beginning of the chosen subreturn \(J_I\).  The exact
subreturn-containment theorem gives

\[
 Q(J_I)\subseteq Q(I)\quad\hbox{if }a(I)\text{ is even},
 \tag{1.3}
\]

and

\[
 Q(J_I)\subseteq \mathsf TQ(I)\quad\hbox{if }a(I)\text{ is odd},
 \tag{1.4}
\]

where \(\mathsf T\) is the global one-edge translate.  The map
\(\mathsf T\) is a bijection of the full quotient-edge set.

Split \(\mathcal P\) according to the parity of \(a(I)\).  In the even
class the parent supports \(Q(I)\) are pairwise disjoint.  In the odd
class the translated supports \(\mathsf TQ(I)\) are pairwise disjoint.
For the audited critical-corner subreturn, the literal root

\[
 C(s,K,Y)=1^s0^KY0^s
 \tag{1.5}
\]

belongs to \(Q(J_I)\), is independent of the phase pair, and uniquely
recovers \((s,K,Y)\).  Lemma 1.1 applied separately to (1.3) and (1.4)
therefore bounds each parity class by the number of possible corner
roots.

The audited fixed-rank estimate for those roots is

\[
 \#\{C(s,K,Y):\alpha\sqrt r\le s\le A\sqrt r\}
 \le {2\over3}\,4^r4^{-\lceil\alpha\sqrt r\rceil}.
 \tag{1.6}
\]

Adding the two parity classes proves the first inequality in (0.3).
Finally the elementary Catalan lower bound

\[
 B_r\ge {4^r\over(r+1)(2r+1)}
\]

shows that the ratio of the right side of (0.3) to \(B_r/\sqrt r\)
tends to zero. \(\square\)

## 2. A canonical near-complement Dyck mate

Write the increments of \(D\) as

\[
 x_i=\begin{cases}1,&D_i=1,\\-1,&D_i=0,\end{cases}
 \qquad
 H_t=\sum_{i=1}^t x_i,
 \qquad 0\le t\le2r.
 \tag{2.1}
\]

Thus \(H_0=H_{2r}=0\), every \(H_t\ge0\), and
\(h=\max_tH_t\).  Put \(s=h\).

For \(1\le k\le h\), let \(u_k\) be the first up-step

\[
 k-1\longrightarrow k,
 \tag{2.2}
\]

and let \(v_k\) be the last down-step

\[
 k\longrightarrow k-1.
 \tag{2.3}
\]

All these steps exist.  Their chronological order is

\[
 u_1<u_2<\cdots<u_h<v_h<\cdots<v_2<v_1.
 \tag{2.4}
\]

Indeed, reaching the maximum forces all the first upcrossings, and after
the last downcrossing of a level the path can never reach that level
again.

Let

\[
 \Gamma=\{u_1,\ldots,u_h,v_1,\ldots,v_h\},
 \tag{2.5}
\]

and define a second increment word by

\[
 x_i^\#=
 \begin{cases}
  x_i,&i\in\Gamma,\\
 -x_i,&i\notin\Gamma.
 \end{cases}
 \tag{2.6}
\]

### Lemma 2.1 (first-up/last-down reflection)

The word \(x^\#\) is a Dyck path.  Its agreement set with \(x\) is
exactly \(\Gamma\).

#### Proof

Put

\[
 A_t=\sum_{\substack{i\le t\\i\in\Gamma}}x_i.
 \tag{2.7}
\]

The height of the new path is

\[
 H_t^\#=\sum_{i=1}^t x_i^\#=2A_t-H_t.
 \tag{2.8}
\]

We claim that

\[
 H_t\le A_t
 \qquad(0\le t\le2r).
 \tag{2.9}
\]

Before \(u_1\), both sides are zero.  Between \(u_k\) and
\(u_{k+1}\), one has \(A_t=k\), while the definition of the first
upcrossing \(u_{k+1}\) gives \(H_t\le k\).  Between \(u_h\) and
\(v_h\), one has \(A_t=h\) and \(H_t\le h\).

After \(v_{k+1}\) and before \(v_k\), one has \(A_t=k\).  Since
\(v_{k+1}\) was the last downcrossing from \(k+1\) to \(k\), the
path cannot subsequently reach \(k+1\): otherwise it would have to
cross downward through the same edge once more before ending at zero.
Thus \(H_t\le k\).  Immediately after \(v_k\), both quantities drop
to

\[
 A_t=k-1,\qquad H_t=k-1,
\]

and the same argument continues.  This proves (2.9).

Equation (2.8) now gives \(H_t^\#\ge0\).  There are exactly \(h=s\)
selected up-steps and \(h=s\) selected down-steps, so
\(A_{2r}=0\).  Since \(H_{2r}=0\), equation (2.8) gives
\(H_{2r}^\#=0\).  Hence \(x^\#\) is Dyck.  Formula (2.6) makes its
agreement set exactly \(\Gamma\). \(\square\)

Lemma 2.1 proves the first part of Theorem A.  The selected upcrossings
are \(h=s\) common ones, the selected downcrossings are \(h=s\) common
zeroes, and every unselected bit is complemented.

## 3. Exact fixed-core realization of the endpoint pair

Regard the \(2r\) bit positions as physical coordinates other than a
new coordinate \(a_0\).  Partition them according to the ordered bit
pair \((D_i,D_i^\#)\):

\[
\begin{aligned}
 U&=\{i:(D_i,D_i^\#)=(1,1)\},\\
 V&=\{i:(D_i,D_i^\#)=(0,0)\},\\
 K&=\{i:(D_i,D_i^\#)=(1,0)\},\\
 K'&=\{i:(D_i,D_i^\#)=(0,1)\}.
\end{aligned}
 \tag{3.1}
\]

The preceding section gives

\[
 |U|=|V|=s,
 \qquad |K|=|K'|=r-s.
 \tag{3.2}
\]

Choose arbitrary enumerations

\[
 U=\{b_0,\ldots,b_{s-1}\},
 \qquad V=\{a_1,\ldots,a_s\}.
 \tag{3.3}
\]

For \(0\le j\le s\), define

\[
 X_{2j}=K\cup\{a_0,\ldots,a_{j-1}\}
              \cup\{b_j,\ldots,b_{s-1}\},
 \tag{3.4}
\]

and

\[
 X_{2j+1}=K'\cup\{b_0,\ldots,b_{j-1}\}
                \cup\{a_{j+1},\ldots,a_s\}.
 \tag{3.5}
\]

Finally put

\[
 X_{2s+2}=K\cup V.
 \tag{3.6}
\]

### Lemma 3.1 (literal simple return)

The consecutive pairs \(X_tX_{t+1}\), \(0\le t\le2s+1\), are Kneser
edges.  Their omitted labels are

\[
 a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1},a_s,a_0.
 \tag{3.7}
\]

The first and last boundary edges, oriented as displayed, have roots
\(D\) and \(D^\#\), respectively.

#### Proof

Every displayed owner has size \(r\).  Equations (3.4)--(3.5) show
that \(X_{2j}\) and \(X_{2j+1}\) are disjoint and their union contains
every physical coordinate except \(a_j\).  Likewise
\(X_{2j+1}\) and \(X_{2j+2}\) are disjoint and omit exactly \(b_j\).
At the terminal boundary, \(X_{2s+1}=K'\cup U\) and
\(X_{2s+2}=K\cup V\), so their union omits exactly \(a_0\).
This proves (3.7) and all Kneser incidences.

The first edge is

\[
 (K\cup U,K'\cup V),
\]

whose bit pairs are exactly those of \(D\).  The last edge is

\[
 (K'\cup U,K\cup V),
\]

whose bit pairs are exactly those of \(D^\#\).  Finally, all entries in
the half-open list in (3.7) are distinct. \(\square\)

This is precisely the fixed-core core-swap normal form, now constructed
in the reverse direction for every Dyck root.

### Lemma 3.2 (the endpoint pair parses the sector; one endpoint does not)

For a labelled simple sector put

\[
 E^-=(K\cup U,K'\cup V),
 \qquad E^+=(K'\cup U,K\cup V).
 \tag{3.8}
\]

The ordered pair \((E^-,E^+)\) uniquely determines its four parts:

\[
\begin{aligned}
 U&=(K\cup U)\cap(K'\cup U),&
 V&=(K'\cup V)\cap(K\cup V),\\
 K&=(K\cup U)\cap(K\cup V),&
 K'&=(K'\cup V)\cap(K'\cup U).
\end{aligned}
\tag{3.9}
\]

By contrast, one directed boundary edge \((X,Y)\), with its omitted
coordinate fixed, has exactly

\[
 \boxed{\binom rs^2}
 \tag{3.10}
\]

labelled fixed-core decompositions of active size \(s\): choose
\(U\in\binom Xs\), \(V\in\binom Ys\), and put
\(K=X\setminus U\), \(K'=Y\setminus V\).

#### Proof

The intersections in (3.9) follow from the disjoint partition

\[
 [N]\setminus\{a_0\}=K\sqcup K'\sqcup U\sqcup V.
\]

Conversely, the two choices in (3.10) are independent, their complements
have size \(r-s\), and distinct choices give distinct labelled
four-part partitions. \(\square\)

On a nonwrapping quotient cycle the two boundary edges are distinct.
Therefore endpoint incidence alone gives only

\[
 \boxed{2|\mathcal P|\le B_r,}
 \tag{3.11}
\]

a factor \(\Theta(\sqrt r)\) above the coefficient-one scale.  Parsing
the endpoint *pair* does not repair this: its first entry is already one
of the \(B_r\) quotient edges, and Theorem A gives a legal parsed mate
for a Catalan-density set of first entries.

## 4. Catalan density in every fixed Gaussian cutoff

Let \(M_{r,L}\) be the number of Dyck paths of semilength \(r\) and
height at most \(L\).  The path-graph spectral decomposition gives the
exact formula

\[
 M_{r,L}
 ={2\over L+2}\sum_{j=1}^{L+1}
  \sin^2\!\left({\pi j\over L+2}\right)
  \left(2\cos {\pi j\over L+2}\right)^{2r}.
 \tag{4.1}
\]

All summands are nonnegative.  Retaining \(j=1\), and using for all
large \(L\)

\[
 \sin x\ge {2x\over\pi},
 \qquad \log\cos x\ge-x^2
 \qquad(0\le x\le1/2),
 \tag{4.2}
\]

gives

\[
 M_{r,L}
 \ge {8\over(L+2)^3}\,4^r
      \exp\!\left(-{2\pi^2r\over(L+2)^2}\right).
 \tag{4.3}
\]

Take

\[
 L=H_A-1.
 \tag{4.4}
\]

Then \(L\asymp_A\sqrt r\), so (4.3) is at least

\[
 c_A{4^r\over r^{3/2}}.
 \tag{4.5}
\]

The elementary Wallis bound

\[
 \binom{2r}{r}\le {4^r\over\sqrt{r+1}}
 \tag{4.6}
\]

implies

\[
 B_r={1\over r+1}\binom{2r}{r}
 \le {4^r\over(r+1)^{3/2}}.
 \tag{4.7}
\]

Therefore (4.5) is at least \(c'_AB_r\), proving (0.1).  For every
root counted here,

\[
 s=h
 \le H_A-1,
\]

and hence its simple return has positive residence \(s+1\le H_A\).

## 5. Lag two: a genuine internal near-height edge charge

Let

\[
 D_i=\tau^iD_0=P_i1R_i0S_i,
 \qquad c_i=|S_i|+1,
 \tag{5.1}
\]

be one genuine PBBS trajectory, with the canonical first-maximum
factorization at every phase.  Its height \(h\) is invariant.  Let
\(T_i\) be the canonical dual Dyck word, so that

\[
 S_i1P_i=P_{i+1}1\overline T_i,
 \qquad \widehat c_i=|T_i|+1.
 \tag{5.2}
\]

After translating a cell with left phase \(j\) to \(j=0\), the exact
lag-two scalar coordinate is

\[
 x_2=a_2-c_1,
 \qquad a_i=|P_i|+1,
 \tag{5.3}
\]

and the two cell intervals are

\[
 (0,c_0],
 \qquad (x_2-\widehat c_2,x_2].
 \tag{5.4}
\]

### Theorem 5.1 (lag-two near-height alternative)

Assume \(h\ge3\).  If the two intervals in (5.4) have nonempty
intersection, then at least one of

\[
 \boxed{
 \operatorname {ht}(S_0)\ge h-2,
 \qquad
 \operatorname {ht}(S_1)\ge h-1,
 \qquad
 \operatorname {ht}(S_2)=h}
 \tag{5.5}
\]

holds.

#### Proof

Suppose that the second and third alternatives fail.  Since every
terminal canonical suffix has height at most the height of the full root,
this means

\[
 \operatorname {ht}(S_1)\le h-2,
 \qquad
 \operatorname {ht}(S_2)\le h-1.
 \tag{5.6}
\]

The canonical prefix \(P_1\) starts at height zero, ends at height
\(h-1\), and never exceeds height \(h-1\).  Factor it uniquely as

\[
 P_1=X\,1\,Y,
 \tag{5.7}
\]

where the displayed \(1\) is the last step of the shortest prefix of
\(P_1\) which reaches height \(h-1\).  Thus \(X\) ends at height
\(h-2\), no prefix of \(X\) exceeds \(h-2\), and \(Y\) has net zero
and nonpositive relative prefixes.

Now use the literal trajectory word

\[
 D_2=S_1\,1\,P_1\,0\,R_1
    =S_1\,1\,X\,1\,Y\,0\,R_1.
 \tag{5.8}
\]

The word \(S_1\) returns to height zero and, by (5.6), stays below
height \(h-1\).  After it, the displayed \(1\) in front of \(X\)
raises the base height to one.  While \(X\) is read, the absolute height
is at most \(h-1\); the following displayed \(1\) is therefore the
first step of \(D_2\) which reaches height \(h\).  Hence the canonical
prefix of \(D_2\) is exactly

\[
 \boxed{P_2=S_1\,1\,X.}
 \tag{5.9}
\]

Because \(h\ge3\), the path \(X\) reaches height \(h-2\) by an up-step.
Factor it uniquely as

\[
 X=U\,1\,V,
 \tag{5.10}
\]

where \(U1\) is the shortest prefix of \(X\) which reaches height
\(h-2\).  Thus \(U\) ends at height \(h-3\), and \(V\) has net zero
and nonpositive relative prefixes.

Apply the trajectory identity once more.  Equations (5.9)--(5.10) give

\[
 D_3
 =S_2\,1\,P_2\,0\,R_2
 =S_2\,1\,S_1\,1\,U\,1\,V\,0\,R_2.
 \tag{5.11}
\]

The first block \(S_2\) stays below height \(h\).  The block \(S_1\),
read from base height one, stays at height at most \(h-1\).  After the
next displayed \(1\), the word \(U\) is read from base height two;
the defining property of \(U1\) says that it stays below \(h\), and
the following displayed \(1\) reaches \(h\) for the first time.  Thus

\[
 \boxed{P_3=S_2\,1\,S_1\,1\,U.}
 \tag{5.12}
\]

Substitute (5.9), (5.10), and (5.12) into the exact local dual identity
at phase two:

\[
 S_2\,1\,P_2=P_3\,1\,\overline T_2.
 \tag{5.13}
\]

Both sides are literal words.  Cancelling their common prefix gives

\[
 S_2\,1\,S_1\,1\,U\,1\,V
 =S_2\,1\,S_1\,1\,U\,1\,\overline T_2,
\]

and hence

\[
 \boxed{\overline T_2=V.}
 \tag{5.14}
\]

It remains to audit the appended separator and the cell coordinates.
From (5.9),

\[
 a_2=|P_2|+1=|S_1|+|X|+2,
 \qquad c_1=|S_1|+1,
\]

so

\[
 \boxed{x_2=|X|+1.}
 \tag{5.15}
\]

Equations (5.10), (5.14), and
\(\widehat c_2=|T_2|+1\) now identify the second interval in (5.4) as

\[
 (x_2-\widehat c_2,x_2]
 =(|U|+1,|X|+1].
 \tag{5.16}
\]

This interval spells the literal block \(V1\) in \(D_1\): the word
\(V\) is the terminal part of \(X\), and the appended \(1\) is the
displayed step immediately after \(X\) in (5.7).  Independently,

\[
 D_1=S_0\,1\,P_0\,0\,R_0
 \tag{5.17}
\]

shows that the first interval \((0,c_0]=(0,|S_0|+1]\) spells
\(S_01\), with the same origin at the beginning of \(D_1\).  There is
no unfolded history word and no transported-label identification in this
argument.

The two half-open intervals in (5.16)--(5.17) intersect only if

\[
 |U|+1<|S_0|+1,
 \qquad\text{that is,}\qquad |U|<|S_0|.
 \tag{5.18}
\]

But both \(U1\) and \(S_0\) are literal prefixes of the same root
\(D_1\).  Therefore (5.18) says that \(S_0\) contains the complete
prefix \(U1\).  By construction that prefix reaches height \(h-2\), so

\[
 \operatorname {ht}(S_0)\ge h-2.
\]

This is the first alternative in (5.5), and proves the theorem.
\(\square\)

### Corollary 5.2 (complete lag-two packing bound)

The number of roots \(D_0\in\mathcal D_r\) which support a nonempty
lag-two cell is

\[
 \boxed{O(B_r/r^{3/4}).}
 \tag{5.19}
\]

Consequently every quotient-edge-disjoint family of genuine return
intervals, each equipped with a lag-two cell, has the same bound.  In
particular its contribution is \(o(B_r/\sqrt r)\).  No lower bound on
the cell length and no macroscopic-carrier hypothesis is needed.

#### Proof

For each phase put

\[
 U_i:=P_i1R_i0.
 \tag{5.20}
\]

The word \(U_i\) is Dyck of height exactly \(h\), the word \(S_i\) is
Dyck of height at most \(h\), their semilengths sum to \(r\), and the
map

\[
 D_i\longmapsto(U_i,S_i)
 \tag{5.21}
\]

is injective because \(D_i=U_iS_i\).  Each alternative in (5.5)
therefore gives a pair of Dyck words whose heights differ by at most two.
The fixed height-collision convolution, Lemma 7.2 of
`MATH_ATTACK_Z15_P_CELL_LITERAL_OVERLAP_RENEWAL_OBSTRUCTION_20260725.md`,
gives

\[
 \sum_{u+v=r}
 \#\{(U,V)\in\mathcal D_u\times\mathcal D_v:
       |\operatorname {ht}(U)-\operatorname {ht}(V)|\le2\}
 =O(B_r/r^{3/4}).
 \tag{5.22}
\]

Apply (5.22) at phase zero, one, or two according to (5.5).  Since every
\(\tau^i\) is a bijection of \(\mathcal D_r\), rephasing does not change
the count.  A union bound over the three phases proves (5.19).

For a quotient-edge-disjoint family, choose the even carrier root at the
left side of each lag-two cell.  These roots are pairwise distinct because
they belong to the disjoint even supports.  The root count (5.19) therefore
bounds the family.  The bounded-height cases \(h<3\), if retained, are
exponentially smaller than \(B_r/\sqrt r\) by the standard finite-height
Dyck estimate. \(\square\)

The lag-two proof is the first nontrivial instance of an exact nested
first-hit calculation.

### Theorem 5.3 (all bounded lags)

Fix an integer \(\ell\) with

\[
 1\le\ell<h.
 \tag{5.23}
\]

If the normalized chronological cell

\[
 (0,c_0]\cap(x_\ell-\widehat c_\ell,x_\ell]
 \tag{5.24}
\]

is nonempty, where

\[
 x_\ell=a_\ell-\sum_{i=1}^{\ell-1}c_i,
 \tag{5.25}
\]

then

\[
 \boxed{
 \text{there is an }i\in\{0,1,\ldots,\ell\}
 \text{ such that }
 \operatorname {ht}(S_i)\ge h-\ell+i.}
 \tag{5.26}
\]

#### Proof

Assume the contrary.  Since heights are integral,

\[
 \operatorname {ht}(S_i)\le h-\ell+i-1
 \qquad(0\le i\le\ell).
 \tag{5.27}
\]

Starting with \(X_0:=P_1\), recursively define words
\(X_t,V_t\), \(1\le t\le\ell\), by

\[
 \boxed{X_{t-1}=X_t\,1\,V_t,}
 \tag{5.28}
\]

where \(X_t1\) is the shortest prefix of \(X_{t-1}\) which reaches
height \(h-t\).  This recursion is well defined.  Indeed \(X_0=P_1\)
ends at height \(h-1\) and never exceeds it.  Inductively, \(X_t\)
ends at height \(h-t-1\), never exceeds that height before its final
displayed up-step, and \(V_t\) has net zero and nonpositive relative
prefixes.  The restriction \(t\le\ell<h\) ensures that every target
height \(h-t\) is positive and is first reached by an up-step.

We claim inductively that

\[
 \boxed{
 P_{t+1}=S_t1S_{t-1}1\cdots S_11X_t
 \qquad(1\le t\le\ell).}
 \tag{5.29}
\]

For the induction step, suppose

\[
 P_t=S_{t-1}1\cdots S_11X_{t-1}.
\]

Then

\[
 D_{t+1}=S_t1P_t0R_t
 =S_t1S_{t-1}1\cdots S_11X_t1V_t0R_t.
 \tag{5.30}
\]

Before \(X_t1\), the block \(S_i\) is read from base height \(t-i\).
Equation (5.27) gives

\[
 (t-i)+\operatorname {ht}(S_i)
 \le h-(\ell-t)-1<h.
 \tag{5.31}
\]

The word \(X_t\) is read from base height \(t\), stays below absolute
height \(h\), and its following displayed \(1\) reaches \(h\) for the
first time.  Thus (5.29) is exactly the canonical first-maximum prefix,
not merely a formal factorization.

The base case \(t=1\) is the same argument applied to
\(D_2=S_11P_10R_1\).  This proves (5.29) for every \(t\le\ell\).
Substitute (5.28)--(5.29) into the local dual identity at phase \(t\):

\[
 S_t1P_t=P_{t+1}1\overline T_t.
 \tag{5.32}
\]

Literal cancellation gives

\[
 \boxed{\overline T_t=V_t
 \qquad(1\le t\le\ell).}
 \tag{5.33}
\]

For the terminal phase \(t=\ell\), equation (5.29) gives the exact
length identity

\[
\begin{aligned}
 a_\ell
 &=|P_\ell|+1\\
 &=\sum_{i=1}^{\ell-1}(|S_i|+1)
      +|X_{\ell-1}|+1,
\end{aligned}
 \tag{5.34}
\]

and hence

\[
 \boxed{x_\ell=|X_{\ell-1}|+1.}
 \tag{5.35}
\]

Since

\[
 X_{\ell-1}=X_\ell1V_\ell,
 \qquad \overline T_\ell=V_\ell,
\]

the odd interval in (5.24) is

\[
 (x_\ell-\widehat c_\ell,x_\ell]
 =(|X_\ell|+1,|X_{\ell-1}|+1].
 \tag{5.36}
\]

It spells \(V_\ell1\) inside the single root \(D_1\).  To check the
appended separator, iterating (5.28) gives

\[
 P_1=X_\ell1V_\ell1V_{\ell-1}\cdots1V_1;
 \tag{5.37}
\]

when \(\ell=1\), the final appended \(1\) is instead the canonical
maximum-reaching step immediately after \(P_1\).  In both cases it is
the literal symbol immediately following \(V_\ell\) in \(D_1\).

On the other hand \(D_1=S_01P_00R_0\), so the even interval
\((0,c_0]\) spells \(S_01\) from the same origin.  Nonempty intersection
of these half-open intervals forces

\[
 |X_\ell|+1<|S_0|+1.
 \tag{5.38}
\]

Thus \(S_0\), which is also a literal prefix of \(D_1\), contains the
complete prefix \(X_\ell1\).  By construction this prefix reaches height
\(h-\ell\).  Hence

\[
 \operatorname {ht}(S_0)\ge h-\ell,
\]

contradicting (5.27) at \(i=0\).  This proves (5.26). \(\square\)

### Corollary 5.4 (fixed-lag packing is negligible)

For every fixed positive integer \(L\), the total number of roots
supporting a nonempty cell of any lag

\[
 1\le\ell\le L<h
\]

is

\[
 \boxed{O_L(B_r/r^{3/4})=o_L(B_r/\sqrt r).}
 \tag{5.39}
\]

The same bound holds for a quotient-edge-disjoint family equipped with
such cells.

#### Proof

For a lag \(\ell\le L\), Theorem 5.3 supplies a phase
\(0\le i\le\ell\) for which the canonical split

\[
 D_i=(P_i1R_i0)S_i
\]

has component heights differing by at most \(\ell-i\le L\).  Apply the
fixed height-collision convolution with \(q=L\), rephase by the bijection
\(\tau^i\), and take the finite union over \((\ell,i)\).  The selected
left carrier roots in an edge-disjoint family are distinct, exactly as in
Corollary 5.2. \(\square\)

The restriction \(\ell<h\) is substantive.  If \(\ell\ge h\), the
\(i=0\) alternative in (5.26) becomes the tautology
\(\operatorname {ht}(S_0)\ge h-\ell\), and the nested first-hit recursion
reaches level zero.  No root-count gain for that sector is claimed here.

The preceding fixed-\(L\) statement admits a uniform version which removes
a genuinely growing lag window.

### Lemma 5.5 (uniform near-height collision)

There are absolute constants \(c_0,C>0\) such that, for all sufficiently
large \(r\) and every integer

\[
 0\le q\le c_0r^{1/4},
 \tag{5.40}
\]

one has

\[
\boxed{
 \sum_{u+v=r}
 \#\{(U,V)\in\mathcal D_u\times\mathcal D_v:
       |\operatorname {ht}(U)-\operatorname {ht}(V)|\le q\}
 \le C(q+1){(\log(r+2))^2\over r}B_r.}
\tag{5.41}
\]

#### Proof

Write \(e_{n,a}\) for the number of semilength-\(n\) Dyck paths of
exact height \(a\).  The audited exact-height atom and height tails give
absolute \(c,C>0\) such that

\[
 \sup_a e_{n,a}\le C{\operatorname {Cat}_n\over\sqrt{n+1}},
 \tag{5.42}
\]

and, with the usual harmless polynomial prefactors absorbed whenever the
displayed exponent is large,

\[
 \Pr_n\{\operatorname {ht}\ge t\}
 \le C e^{-ct^2/n},
 \qquad
 \Pr_n\{\operatorname {ht}\le t\}
 \le C\left({\sqrt n\over t+1}\right)^3
          e^{-cn/(t+1)^2}.
 \tag{5.43}
\]

Here \(\Pr_n\) is uniform on \(\mathcal D_n\).  Formula (5.42) is
Lemma 7.1 of the Z15 report, while (5.43) is the standard audited
path-graph spectral pair used in its Lemma 7.2.

Choose a sufficiently small absolute \(\kappa>0\), and put

\[
 \eta={\kappa\over(\log(r+2))^2}.
 \tag{5.44}
\]

First suppose \(u,v\ge\eta r\).  For fixed \(u,v\), sum over the height
of \(U\) and use (5.42) on \(V\).  This gives

\[
 \#\{(U,V):|\operatorname {ht}(U)-\operatorname {ht}(V)|\le q\}
 \le {C(q+1)\operatorname {Cat}_u\operatorname {Cat}_v
          \over\sqrt{\eta r}}.
 \tag{5.45}
\]

Uniform Catalan bounds and an integral comparison give

\[
 \sum_{\eta r\le u\le(1-\eta)r}
  \operatorname {Cat}_u\operatorname {Cat}_{r-u}
 \le {CB_r\over\sqrt{\eta r}}.
 \tag{5.46}
\]

Thus the central range contributes at most

\[
 {C(q+1)B_r\over\eta r}.
 \tag{5.47}
\]

Now take \(1\le u<\eta r\) and \(v=r-u\).  Put

\[
 t=(uv)^{1/4}.
\]

After decreasing \(c_0\), condition (5.40) gives \(q\le t/2\).  A
height collision implies either

\[
 \operatorname {ht}(U)\ge t
 \quad\hbox{or}\quad
 \operatorname {ht}(V)\le t+q\le3t/2.
\]

The two estimates in (5.43) therefore bound the pair count by

\[
 C\operatorname {Cat}_u\operatorname {Cat}_v
   \exp\!\left(-c\sqrt{v/u}\right).
 \tag{5.48}
\]

Since

\[
 {\operatorname {Cat}_u\operatorname {Cat}_{r-u}\over B_r}
 \le {C\over(u+1)^{3/2}}
 \qquad(u\le r/2),
\]

integral comparison, with \(y=\sqrt{r/u}\), gives

\[
 \sum_{1\le u<\eta r}(u+1)^{-3/2}
       e^{-c\sqrt{r/u}}
 \le Cr^{-1/2}e^{-c'/\sqrt\eta}.
 \tag{5.49}
\]

Choose \(\kappa\) so small that the right side of (5.49) is
\(O(r^{-3})\).  The symmetric tail is identical.  If \(u=0\) or
\(v=0\), collision forces the nonempty path to have height at most
\(q\); the lower-tail estimate in (5.43), together with
\(q\le c_0r^{1/4}\), is exponentially smaller than \(B_r/r\).

Finally substitute (5.44) into (5.47) and absorb the two tails.  This
proves (5.41). \(\square\)

The logarithmic cutoff in Lemma 5.5 can be chosen adaptively.  The next
form is what is needed for the largest growing-lag range reached here.

### Lemma 5.5A (adaptive near-height collision)

For integers \(1\le q<\sqrt r/8\), put

\[
 R={r\over q^2}.
\]

There are absolute \(c,C>0\) such that, whenever

\[
 32{q^4\over r^2}\le\eta\le{1\over4},
 \tag{5.50a}
\]

the left side of (5.41) is at most

\[
 \boxed{
 CB_r\left{
 {q+1\over\eta r}
 +r^{-1/2}e^{-c/\sqrt\eta}
 +(1+R)^2e^{-cR}
 \right}.}
 \tag{5.50b}
\]

#### Proof

The central calculation (5.45)--(5.47) is unchanged and gives the first
term in (5.50b).  For a tail with \(1\le u<\eta r\) and
\(v=r-u\), put

\[
 u_0={32q^4\over r}.
\]

If \(u_0\le u<\eta r\), then

\[
 t=(uv)^{1/4}\ge2q.
\]

The same height dichotomy as in (5.48) and the same integral comparison
as in (5.49) give

\[
 CB_rr^{-1/2}e^{-c/\sqrt\eta}.
\]

If \(0\le u<u_0\), a \(q\)-collision implies either

\[
 \operatorname {ht}(U)\ge q
 \quad\hbox{or}\quad
 \operatorname {ht}(V)<2q.
\]

When \(u=0\), the first alternative is empty and the second is the whole
condition.

The two height tails (5.43) have exponents at least

\[
 {q^2\over u}\ge {r\over32q^2}={R\over32},
 \qquad
 {v\over(2q+1)^2}\ge cR,
\]

respectively.  Their polynomial prefactors are at most a fixed power of
\(1+R\), and lowering \(c\) absorbs all but the displayed factor
\((1+R)^2\).  Finally

\[
 \sum_{u<u_0}{\operatorname {Cat}_u\operatorname {Cat}_{r-u}\over B_r}
 \le C\sum_{u\ge0}(u+1)^{-3/2}\le C.
\]

This gives the last term in (5.50b).  The opposite tail is symmetric.
Condition (5.50a) is exactly \(u_0\le\eta r\), so the ranges cover all
semilength splits. \(\square\)

### Theorem 5.6 (growing-lag quotient packing)

Let \(L=L(r)\) be a deterministic integer sequence satisfying

\[
 \boxed{L=o\!\left(\sqrt{r/\log(r+2)}\right).}
 \tag{5.50}
\]

Let \(\mathcal P\) be a quotient-edge-disjoint family of genuine
nonwrapping return intervals, and equip every member with one nonempty
chronological cell whose lag obeys \(1\le\ell\le L\).  Then

\[
 \boxed{
 |\mathcal P|=o(B_r/\sqrt r).}
 \tag{5.51}
\]

#### Proof

For each selected interval, rephase the left side of its cell to phase
zero.  If its invariant height satisfies \(h>\ell\), Theorem 5.3 supplies
an index \(0\le i\le\ell\) for which

\[
 |\operatorname {ht}(P_i1R_i0)-\operatorname {ht}(S_i)|
 \le\ell-i.
 \tag{5.52}
\]

If \(h\le\ell\), the weaker inequality

\[
 |\operatorname {ht}(P_01R_00)-\operatorname {ht}(S_0)|\le L
 \tag{5.53}
\]

already holds with \(i=0\), since the first height is \(h\) and the
second lies in \([0,h]\).  Choose the least admissible \(i\) in the first
case, so the choice is deterministic, and charge the interval to the
literal internal support edge \(e_{D_i}\).  In both cases the injective
split

\[
 D_i=(P_i1R_i0)S_i,
\]

has component-height difference at most \(L\).

Every charged edge belongs to its parent support.  Hence all charged roots
are distinct, even when the lags and witness phases differ.  It follows
that \(|\mathcal P|\) is at most the single near-height collision count in
Lemma 5.5A with \(q=L+1\) (replacing \(L\) by \(L+1\) only handles the
possibility \(L=0\)).

Put

\[
 \delta={L+1\over\sqrt r},
 \qquad \eta=\sqrt\delta,
 \qquad R={r\over(L+1)^2}=\delta^{-2}.
 \tag{5.54}
\]

Condition (5.50) gives \(\delta\to0\),

\[
 L+1<\sqrt r/8
\]

for all sufficiently large \(r\), and

\[
 32{(L+1)^4\over r^2}=32\delta^4\le\sqrt\delta=\eta
\]

eventually, and

\[
 {R\over\log(r+2)}\longrightarrow\infty.
 \tag{5.55}
\]

Thus Lemma 5.5A applies.  After division by \(B_r/\sqrt r\), its three
terms are at most

\[
 C\sqrt\delta,
 \qquad
 Ce^{-c\delta^{-1/4}},
 \qquad
 C\sqrt r\,(1+R)^2e^{-cR},
 \tag{5.56}
\]

respectively.  The first two vanish because \(\delta\to0\); the last
vanishes by (5.55).  This proves (5.51). \(\square\)

### Corollary 5.7 (quantitative reduction of \(P_{\rm cell}\))

Put

\[
 L_r=\left\lfloor{\sqrt r\over\log(r+2)}\right\rfloor.
 \tag{5.57}
\]

For every fixed \(A,K,\varepsilon\), the subfamily in the positive
residual \(P_{\rm cell}\) whose selected cell has lag at most \(L_r\)
has cardinality

\[
 \boxed{o_{A,K,\varepsilon}(B_r/\sqrt r).}
 \tag{5.58}
\]

Consequently the still-unproved part of that residual may be restricted
to cells with

\[
 \boxed{
 {\sqrt r\over\log(r+2)}<k-j\le H_A.}
 \tag{5.59}
\]

#### Proof

The ratio of \(L_r\) to \(\sqrt{r/\log(r+2)}\) is
\(1/\sqrt{\log(r+2)}\), so Theorem 5.6 applies.  Its hypotheses use only
genuine chronology, nonempty cells, and quotient-edge disjointness; the
additional macroscopic-carrier and bounded-winding restrictions defining
\(P_{\rm cell}\) only pass to a subfamily.  Negative lags are impossible,
and the diagonal lag is independently negligible, leaving (5.59).
\(\square\)

## 6. Consequence for the positive-winding common-edge route

The exact critical-corner theorem remains fully valid.  Its strength is
not the abstract core-swap square; it is the conjunction of

1. a literal internal root contained in every phase-parametrized support;
2. independence of that root from the phase pair; and
3. uniquely parseable deterministic collars of length
   \(\Theta(\sqrt r)\), which force exponentially small root mass.

Theorem A shows that none of these three conclusions follows from the
fixed-core endpoint square or near-complementarity.  At the accepted
coefficient-one scale, the endpoint-eligible set is not merely critical:
it has size \(\Omega_A(B_r)\), a factor \(\Theta(\sqrt r)\) larger than
\(B_r/\sqrt r\).

For the positive-winding residual \(P_{\rm cell}\), a sufficient theorem
must therefore be genuinely internal and chronological.  One exact form
would be a map \(I\mapsto C(I)\) such that

\[
 e_{C(I)}\in Q(I),
 \qquad
 |\{C(I):I\text{ is an admissible positive cell}\}|
   =o_A(B_r/\sqrt r),
 \tag{6.1}
\]

where the definition of \(C(I)\) uses the iterated literal identities
between the selected phases.  The endpoint core-swap root cannot serve as
\(C(I)\).  Nor does Theorem A exclude (6.1): the constructed intermediate
path is not asserted to be a \(\tau\)-orbit, and no winding is assigned to
it.

Theorems 5.1 and 5.3 supply precisely such an internal support edge for
every lag below the height: one of the intervening \(D_i\)'s is forced into
a near-height collision set.  If \(\ell\ge h\), the starting split itself
has height difference at most \(\ell\).  Lemma 5.5A and Theorem 5.6 then
turn these alternatives into one injective internal-edge charge across
all lags

\[
 1\le\ell\le L=o\!\left(\sqrt{r/\log(r+2)}\right).
\]

This is stronger than a parseable-collar count and is fully chronological.
It does not presently reach lags of order
\(\sqrt{r/\log r}\) or larger, in particular the full Gaussian lag
window.

Thus the precise proved/conditional boundary is:

\[
 \boxed{
 \begin{array}{c}
 \text{common internal edge plus parseable collars gives the required
 packing gain;}\\[1mm]
 \text{fixed-core endpoints and Gaussian near-complementarity are
 Catalan-dense;}\\[1mm]
 \text{every window }1\le\ell\le L(r),\quad
 L=o(\sqrt{r/\log r}),\text{ has an injective internal-edge charge;}\\
 \text{the remaining near-Gaussian lags are unproved.}
 \end{array}}
 \tag{6.2}
\]

## 7. Independent audit of the decisive steps

The following points were checked independently against the literal word
and support conventions.

1.  **Nested-corner containment.**  An even-offset subreturn support lies
    in its parent support; an odd-offset one lies in the global one-edge
    translate.  Splitting by offset parity therefore preserves
    edge-disjointness and gives the factor two, hence the constant
    \(4/3\), in Theorem B.

2.  **Endpoint repair.**  In Lemma 2.1 the selected first-up and last-down
    steps satisfy \(H_t\le A_t\) in every chronological region, so
    \(H_t^\#=2A_t-H_t\ge0\).  Selecting all levels gives \(s=h\), meeting
    the PBBS height--gap lower bound.  Equal endpoint height and
    \(\tau\)-chronology are still not supplied, exactly as stated.

3.  **Nested first hits.**  Under the contrary height bounds in Theorem
    5.3, every block \(S_i\) stays strictly below the next global record at
    its actual base height.  Thus (5.29) is the canonical prefix, not only
    a formal concatenation, and free-word cancellation in (5.32) is legal.

4.  **No duplicated labels.**  Equations (5.35)--(5.38) put both cell
    intervals into the ordinary position coordinates of the single root
    \(D_1\).  The argument compares literal bits in that root and never
    identifies unfolded separator tokens or transported physical labels.

5.  **Adaptive collision tails.**  Above \(u_0=32q^4/r\), the threshold
    \((uv)^{1/4}\) is at least \(2q\).  Below \(u_0\), a collision forces
    either a height-\(q\) upper tail in the small factor or a height-\(2q\)
    lower tail in the large factor, both with exponent
    \(\Omega(r/q^2)\).  These are exactly the three terms in (5.50b).

6.  **Packing injectivity.**  The witness root \(D_i\) chosen in Theorem
    5.6 is an actual edge of its parent interval.  Parent support
    disjointness therefore makes all charges distinct across different
    witness phases and different lags; no union loss is needed.

The report proves no estimate for the complementary lag range in (5.59),
does not turn the endpoint construction into a PBBS orbit, and does not
claim the full positive-winding gate or coefficient one.
