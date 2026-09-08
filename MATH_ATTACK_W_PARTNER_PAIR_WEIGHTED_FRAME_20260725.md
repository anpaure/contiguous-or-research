# Partner-pair interval charts: a quantitative star frame and the common-base obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom nm,
 \qquad R_m=\operatorname {Cat}_{m-1}
 =\frac1{2m-1}\binom{2m-1}{m-1}.
\]

There are two distinct compatibility questions for the pair-omission
interval charts.

1. **Factor compatibility.**  Can one attach one fixed exact local factor
   to every omitted pair so that many pair exchanges are coordinate
   conjugacies of one factor?
2. **Common-matching compatibility.**  Do all of the resulting interval
   cubes have the same old integral token matching, including the tokens
   outside the exchanged stratum?

This note proves a positive answer to the first question, with an explicit
weighted frame, and a negative answer to the currently available
fixed-partition route.  The second question remains unproved and is exactly
where the desired physical frame fails.

Fix a two-set \(A=\{a,b\}\), order the remaining coordinates as

\[
 R=[n]\setminus A=\{r_1<\cdots<r_{n-2}\},
\]

and, for \(B=\{r_i,r_j\}\), \(i<j\), put

\[
 \theta_B=(a\ r_i)(b\ r_j).
\tag{0.1}
\]

Write \(c=r_1,d=r_{n-2}\), and retain the linear-size subfamily

\[
 \mathscr B_0={B\in\tbinom R2:c\in B\text{ or }d\in B\},
 \qquad |\mathscr B_0|=2n-7.
\tag{0.1a}
\]

Unless a full star is explicitly mentioned, every unqualified sum over
partner pairs below is over \(\mathscr B_0\).

Choose one exact local factor \(F_A\), and set

\[
 F_B=\theta_BF_A
 \qquad(B\in\tbinom R2).
\tag{0.2}
\]

There is only one factor for each unordered pair \(B\); no two typed
copies or two inconsistent bijections are used.  Already the involutions
with \(B\in\mathscr B_0\) generate \(A_n\).  More quantitatively, if
\(P_B=(I+\theta_B)/2\) acts on any nontrivial subset layer and \(v\) is
centered, then

\[
 \boxed{
 \sum_{B\in\mathscr B_0}\|(I-P_B)v\|_2^2
 \ge \frac1{288(n-1)^2}\|v\|_2^2.}
\tag{0.3}
\]

The same inequality holds on an arbitrary nonnegatively weighted direct
sum of subset layers.  Therefore, if one had an upper physical chart and
a lower-dual physical chart realizing the two signed copies of every
\(P_B\), their coherent signals would satisfy

\[
 \boxed{
 \sum_B(A_B^++A_B^-)
 \ge \frac1{72(n-1)^2}\|v\|_w^2.}
\tag{0.4}
\]

This is the requested representation-theoretic frame, with all constants
proved below.

The existing literal interval charts do not instantiate (0.4).

* A fixed disjoint-pair priority atlas generates only pair-block
  permutations and fixes the unpaired coordinate.  The nonzero centered
  mode
  \[
    v_z(U)={\bf1}_{\{z\in U\}}-|U|/n
  \]
  is killed by every such chart, on every nontrivial rank.  Adding a
  lower-dual copy with the same coordinate transports does not remove this
  kernel.
* The spanning star (0.2) includes pairs containing the old unpaired
  coordinate and removes the algebraic kernel.  But its direct old sides
  cannot have one common matching background.  The full star is impossible for
  \(m\ge6\), and already the reduced frame family \(\mathscr B_0\) is
  impossible for \(m\ge8\); Theorem 6.1 gives the exact owner-capacity
  contradiction.
* Each one of the star charts has at most \(2R_m\) source intervals and is
  individually within the required boundary scale:
  \[
   \frac{2HR_m}{W}
   =\frac{H(m+1)}{(2m-1)(2m+1)}=o(1)
   \qquad(H=o(m)).
  \tag{0.5}
  \]
  In contrast, putting the \(2n-7\) frame charts into one joint product
  catalog uses at least \((2n-7)R_m=\Theta(W)\) nonempty physical row
  intervals.  The full \(\binom{n-2}{2}\)-chart star uses
  \(\Theta(mW)\).
  Thus (0.3) is a menu frame, not an \(o(W/H)\)-boundary joint cube.

There is a second, independent gap between coherent harmonic signal and
actual interval descent.  If a physical chart decomposes its coherent
signal into interval innovations \(z_{B,I}\), put

\[
 A_B=\left\|\sum_Iz_{B,I}\right\|_w^2,
 \qquad V_B=\sum_I\|z_{B,I}\|_w^2.
\]

The exact floor-Haar descent is \((A_B-V_B)/4\), not \(A_B/4\).  The frame
gives only

\[
 \boxed{
 \sum_B(A_B^++A_B^- -V_B^+-V_B^-)
 \ge \frac1{72(n-1)^2}\|v\|_w^2
      -\sum_B(V_B^++V_B^-).}
\tag{0.6}
\]

An \(o(W/H)\) count of physical boundaries alone does not make the final
variance term smaller than the framed signal.  A long interval may have
only two boundaries while carrying nonzero endpoint-strip action at every
depth.  Hence the required charged frame inequality is **not proved** by
(0.3); the direct common-base realization of this frame is in fact
impossible, and any different realization would still need a lower-dual
chart theorem and a variance/curvature estimate.  The fixed-partition
version is independently refuted by the mode \(v_z\).

There is also an exact lower-dual atom in the coordinate-orbit token
system.  It fixes the lower root, middle owner, every upper flag, and every
lower depth except one prescribed \(q\ge2\); at that depth its innovation
is one Johnson-graph edge.  All such atoms span the centered lower layer.
However, a joint binary cube with \(B\) lower-dual interval atoms has
lower-depth-two affine span at most \(B\).  Since

\[
 \binom n{m-2}-1=(1-o(1))W,
\]

no binary catalog with \(B=o(W/H)\) can frame every lower-depth-two mode.
This refutes the literal **joint binary-catalog** interpretation of the
requested frame.  It does not refute a state-adaptive menu or a genuinely
multiway moving-seam chart whose many threshold states are paid by the same
two physical boundaries.

No constant-one conclusion is claimed.

## 1. The compatible one-factor star

Let \(X=[n]\), fix \(A=\{a,b\}\), and put

\[
 R=X\setminus A=\{r_1<\cdots<r_s\},
 \qquad s=n-2.
\]

For \(1\le i<j\le s\), define the even involution

\[
 \theta_{ij}=(a\ r_i)(b\ r_j).
\tag{1.1}
\]

It exchanges the two coordinate pairs \(A\) and
\(B_{ij}=\{r_i,r_j\}\), and maps

\[
 Q_A=X\setminus A
 \quad\hbox{bijectively onto}\quad
 Q_{B_{ij}}=X\setminus B_{ij}.
\]

### Lemma 1.1 (one fixed factor per omitted pair)

If \(F_A\) is an exact local middle-wreath factor on \(Q_A\), then

\[
 F_{B_{ij}}:=\theta_{ij}F_A
\tag{1.2}
\]

is an exact local factor on \(Q_{B_{ij}}\).  The definition is compatible
for all \(B_{ij}\): each unordered pair receives exactly one factor.

#### Proof

A coordinate bijection takes every cyclic row to a cyclic row and carries
the exact partition of the rank-\(m\) middle sets of \(Q_A\) to the exact
partition of the rank-\(m\) middle sets of \(Q_{B_{ij}}\).  The imposed
order on \(R\) chooses exactly one of the two bijections
\(B_{ij}\to A\), so (1.2) never assigns two factors to the same omitted
pair. \(\square\)

The order in (1.1) is not cosmetic.  Allowing both bijections for every
\(B\) gives an immediate group frame, but would require two generally
different factors attached to the same omitted pair.  The next section
shows that one orientation per pair is already enough.

## 2. The star involutions generate \(A_n\) with linear diameter

Put

\[
 c=r_1,\qquad d=r_s,
\]

and define

\[
 U=X\setminus\{a,c\}=\{b\}\cup(R\setminus\{c\}),
 \qquad
 V=X\setminus\{b,d\}=\{a\}\cup(R\setminus\{d\}).
\tag{2.1}
\]

### Lemma 2.1 (two large alternating subgroups)

For \(n\ge7\), the group

\[
 \Gamma_0=\langle\theta_B:B\in\mathscr B_0\rangle
\]

contains \(A_U\) and \(A_V\).

#### Proof

For distinct \(y,z\in R\setminus\{c\}\), the two generators using
\(\{c,y\}\) and \(\{c,z\}\) have the common transposition \((a\ c)\).
Their product is, up to orientation, the three-cycle

\[
 (b\ y)(b\ z).
\tag{2.2}
\]

Thus \(\Gamma_0\) contains every three-cycle on \(\{b,y,z\}\) with
\(y,z\in R\setminus\{c\}\).  These generate \(A_U\).

Similarly, for distinct \(y,z\in R\setminus\{d\}\), the generators
using \(\{y,d\}\) and \(\{z,d\}\) share \((b\ d)\), and their product
is, up to orientation,

\[
 (a\ y)(a\ z).
\tag{2.3}
\]

These three-cycles generate \(A_V\). \(\square\)

### Lemma 2.2 (overlapping alternating groups)

If \(|U\cap V|\ge2\), then

\[
 \langle A_U,A_V\rangle=A_{U\cup V}.
\tag{2.4}
\]

Moreover, every three-cycle on \(U\cup V\) is a product of at most three
three-cycles, each supported wholly in \(U\) or wholly in \(V\).

#### Proof

Three-cycles generate the alternating group.  A three-cycle supported in
one of \(U,V\) is already available.  Otherwise it contains some
\(x\in U\setminus V\) and \(y\in V\setminus U\).  Choose distinct
\(p,q\in U\cap V\).

If its third point is \(p\), then the identity

\[
 (x\ y\ p)=(y\ p\ q)(x\ q\ p)
\tag{2.5}
\]

expresses it as one \(V\)-cycle followed by one \(U\)-cycle.  If the
third point \(z\) also belongs to \(U\setminus V\), use

\[
 (x\ y\ z)=(x\ p\ z)(x\ y\ p)
\tag{2.6}
\]

and then (2.5).  The case \(z\in V\setminus U\) is symmetric.  These
identities also prove the claimed factor count. \(\square\)

Here \(U\cup V=X\) and

\[
 |U\cap V|=n-4\ge3.
\]

Hence Lemmas 2.1--2.2 give \(\Gamma_0=A_n\).

### Lemma 2.3 (word diameter)

Every element of \(A_n\) is a word of length at most

\[
 D_n=12(n-1)
\tag{2.7}
\]

in the involutions \(\theta_B\), \(B\in\mathscr B_0\).

#### Proof

Every three-cycle in \(A_U\) is a product of at most two three-cycles
rooted at \(b\).  A rooted three-cycle is a product of two generators by
(2.2).  Thus every three-cycle in \(A_U\) has generator length at most
four.  The same argument using (2.3) applies to \(A_V\).  Lemma 2.2 now
gives generator length at most twelve for an arbitrary three-cycle on
\(X\).

It remains to count three-cycles.  Write an even permutation as a product
of \(L\le n-1\) transpositions, where \(L\) is even, and pair consecutive
transpositions.  Two transpositions with one common point form one
three-cycle.  Two disjoint transpositions form two three-cycles; explicitly,

\[
 (x\ y)(u\ v)=(x\ u\ y)(x\ u\ v).
\tag{2.8}
\]

Thus the permutation is a product of at most \(L\le n-1\) three-cycles,
and (2.7) follows. \(\square\)

## 3. Exact quantitative frame

Let \(\mathcal H_k\) be the real permutation module on
\(\binom Xk\), \(1\le k\le n-1\).  Coordinate permutations act
orthogonally by

\[
 (gv)(S)=v(g^{-1}S).
\]

For an involution \(g\), put \(P_g=(I+g)/2\).

### Theorem 3.1 (partner-pair star frame)

For every centered \(v\in\mathcal H_k\),

\[
 \boxed{
 \sum_{B\in\mathscr B_0}
 \|(I-P_B)v\|_2^2
 \ge\frac1{288(n-1)^2}\|v\|_2^2.}
\tag{3.1}
\]

The same estimate holds after summing arbitrary finite nonnegative weights
over any collection of nontrivial subset layers.

#### Proof

The group \(A_n\) is transitive on the \(k\)-subsets for
\(1\le k\le n-1\).  Indeed, if a permutation taking one \(k\)-set to
another is odd, compose it with a transposition within the image set or
within its complement; at least one of these has size at least two.
Therefore the \(A_n\)-average of a centered vector is zero, and

\[
 \frac1{|A_n|}\sum_{h\in A_n}\|v-hv\|_2^2=2\|v\|_2^2.
\tag{3.2}
\]

Let

\[
 \mathcal E(v)=
 \sum_{B\in\mathscr B_0}\|v-\theta_Bv\|_2^2.
\]

By Lemma 2.3, write \(h=g_1\cdots g_\ell\) with
\(\ell\le D_n\).  Telescoping and Cauchy--Schwarz give

\[
 \|v-hv\|_2^2
 \le \ell\sum_{t=1}^{\ell}\|v-g_tv\|_2^2
 \le D_n^2\mathcal E(v).
\tag{3.3}
\]

For the last inequality, each word-step square
\(\|v-g_tv\|_2^2\) is one nonnegative summand of
\(\mathcal E(v)\).  Hence the inner sum is at most
\(\ell\mathcal E(v)\), and its prefactor \(\ell\) gives
\(\ell^2\mathcal E(v)\le D_n^2\mathcal E(v)\).

Average (3.3), use (3.2), and substitute
\(D_n=12(n-1)\):

\[
 \mathcal E(v)
 \ge\frac{2}{144(n-1)^2}\|v\|_2^2
 =\frac1{72(n-1)^2}\|v\|_2^2.
\tag{3.4}
\]

Finally

\[
 I-P_{\theta_{ij}}=\frac{I-\theta_{ij}}2,
\]

so division by four proves (3.1).  Applying (3.1) separately on each
layer and summing its nonnegative weight proves the direct-sum assertion.
\(\square\)

### Corollary 3.2 (formal signed-depth frame)

Let

\[
 \mathcal H_w=
 \bigoplus_{q=1}^H
 \left(\mathcal H_{m-q}^-\oplus\mathcal H_{m+q}^+\right)
\]

with arbitrary finite nonnegative weights \(w_q^\pm\), and let
\(v=(v^-,v^+)\) be centered on every summand.  Define the formal upper
and lower operators

\[
 \begin{aligned}
  P_{B}^{+}(v^-,v^+)&=(v^-,P_Bv^+),\\
  P_{B}^{-}(v^-,v^+)&=(P_Bv^-,v^+).
 \end{aligned}
\tag{3.5}
\]

Then

\[
 \boxed{
 \sum_B\left(
 \|(I-P_B^+)v\|_w^2+
 \|(I-P_B^-)v\|_w^2\right)
 \ge\frac1{288(n-1)^2}\|v\|_w^2.}
\tag{3.6}
\]

If literal chart endpoints had coherent differences

\[
 z_B^+=(\theta_B-I)v^+,
 \qquad z_B^-=(\theta_B-I)v^-,
\tag{3.7}
\]

on their respective sectors, and if
\(A_B^\pm=\|z_B^\pm\|_w^2\), then (3.6) becomes

\[
 \boxed{
 \sum_B(A_B^++A_B^-)
 \ge\frac1{72(n-1)^2}\|v\|_w^2.}
\tag{3.8}
\]

This corollary is algebraic.  It deliberately does not assert that the
formal lower operators in (3.5) have literal token-chart realizations.

## 4. Exact kernel of the fixed-partition menu

Return to a fixed partition

\[
 X=P_1\sqcup\cdots\sqcup P_m\sqcup\{z\}.
\]

Every adjacent-priority transport in the audited interval construction
exchanges two whole pair blocks and fixes \(z\).  The same is true after
composing such exchanges, allowing all partner-pair swaps, or adding
internal coordinate flips within the \(P_i\)'s.

### Proposition 4.1 (unpaired-coordinate invariant)

Fix \(1\le k\le n-1\), and define

\[
 h_{z,k}(U)={\bf1}_{\{z\in U\}}-\frac kn,
 \qquad U\in\binom Xk.
\tag{4.1}
\]

Then \(h_{z,k}\) is centered and nonzero, and every coordinate transport
which fixes \(z\) satisfies

\[
 gh_{z,k}=h_{z,k}.
\tag{4.2}
\]

In particular no positive frame inequality on the whole centered layer can
hold for fixed-partition partner charts.  A lower-dual chart using the same
transports has the identical kernel.

#### Proof

Exactly \(\binom{n-1}{k-1}=(k/n)\binom nk\) rank-\(k\) sets contain
\(z\), so (4.1) is centered.  Both values in (4.1) occur because
\(0<k<n\), so it is nonzero.  Any permutation fixing \(z\) preserves the
predicate \(z\in U\), proving (4.2). \(\square\)

There is also a kernel witness which is not a degree-one coordinate mode.
For \(2\le k\le n-2\), put

\[
 h_{\rm pair,k}(U)
 =\#\{i:P_i\subseteq U\}
  -m\frac{k(k-1)}{n(n-1)}.
\tag{4.3}
\]

The second term is the exact uniform-layer mean of the first, so
\(h_{\rm pair,k}\) is centered.  It is nonzero because rank-\(k\) sets
can have two different numbers of completely occupied priority pairs.
Every pair-block permutation and every internal flip preserves that number,
and therefore fixes \(h_{\rm pair,k}\).  This degree-two witness remains
after one removes the universal degree-zero and degree-one constraints
known for exact-factor load vectors.  Its occurrence as a nonzero component
of some prepared exact-factor load is not asserted here.

There are many further invariant modes: the pair-block group preserves the
number of completely occupied pairs, the number of singly occupied pairs,
and membership of \(z\).  Proposition 4.1 is the smallest exact witness.

The star in Section 1 necessarily uses omitted pairs which cut across the
fixed partition, including pairs containing \(z\).  This is why it
generates the transitive group \(A_n\) and why a fixed partition cannot
replace it.

There is nevertheless a genuine positive compatibility result inside the
fixed partition.  With recursively conjugate factors

\[
 F_{j+1}=\theta_jF_j\qquad(1\le j<m),
\]

all adjacent blocks may be activated simultaneously, including overlapping
odd and even blocks.  Their changed lower domains are disjoint, the
meet/avoid filtration excludes every cross-block owner collision, and the
total maximal-interval count is

\[
 O\!\left(\frac{W\log^2m}{m}\right)=o(W/H)
 \qquad\bigl(H=O(\sqrt m)\bigr).
\]

Thus common-base upper-chart compatibility itself is not the missing fact
for the fixed chain.  What fails is the all-mode frame: every one of those
transports fixes the modes (4.1) and (4.3), and every lower flag is fixed.
Neighboring-block cross-Grams give additional positive joined-target
curvature, including at first upper depth, but no lower bound of that joined
census by the invariant excess modes is known.

## 5. Physical interval count and the joint-catalog obstruction

Fix one \(B\in\binom R2\), and compare the two priority orders
\((A,B,\ldots)\) and \((B,A,\ldots)\), using the conjugate factors
\(F_B=\theta_BF_A\).  The changed lower roots in the first block are

\[
 \mathcal D_B=\left\{S\in\binom X{m-1}:S\cap(A\cup B)=\varnothing\right\}.
\tag{5.1}
\]

In one row of \(F_A\), the starts whose length-\((m-1)\) window avoids
the two coordinates of \(B\) form at most two cyclic intervals.  They form
at least one nonempty interval: deleting the two \(B\)-positions leaves
two arcs of total length \(2m-3\), one of which has length at least
\(m-1\).

Since \(F_A\) has exactly \(R_m\) rows, the interval count \(r_B\)
satisfies

\[
 \boxed{R_m\le r_B\le2R_m.}
\tag{5.2}
\]

The audited interval theorem makes every independent interval corner a
literal lower-saturating, middle-simple matching relative to the common
background of this one adjacent chart, and adds at most \(2r_B\) selected
row runs.  Moreover

\[
 \frac{R_m}{W}
 =\frac{m+1}{2(2m-1)(2m+1)}.
\tag{5.3}
\]

Consequently every individual star chart obeys

\[
 \frac{H(2r_B)}W
 \le\frac{2H(m+1)}{(2m-1)(2m+1)}=o(1)
\tag{5.4}
\]

whenever \(H=o(m)\).

The reduced frame family has \(|\mathscr B_0|=2n-7\) generators.  If all
of their physical intervals are charged in one joint product catalog, then
(5.2) gives

\[
 \boxed{
 \sum_{B\in\mathscr B_0}r_B
 \ge(2n-7)R_m
 =\Theta(W).}
\tag{5.5}
\]

The full \(\binom{n-2}{2}\)-generator star has total interval count at
least \(\binom{n-2}{2}R_m=\Theta(mW)\).  Thus even the reduced star frame
cannot be installed as one joint
\(o(W/H)\)-boundary cube by the direct interval construction.  It can only
be used as a menu in which one chart is selected and paid for at a time.

This is not an artifact of the chosen frame family.

### Proposition 5.1 (support-cover boundary lower bound)

Let \(s\) common-\(A\) partner-pair transports be offered jointly.  If
their coordinate actions have no common nonzero mode of the form
\(h_{z,k}\) in (4.1), then

\[
 \boxed{s\ge m,
 \qquad
 \sum_{\ell=1}^sr_{B_\ell}\ge mR_m.}
\tag{5.6}
\]

Moreover

\[
 \frac{mR_m}{W}
 =\frac{m(m+1)}{2(2m-1)(2m+1)}\longrightarrow\frac18.
\tag{5.7}
\]

Thus every joint common-\(A\) coordinate-transport catalog capable even of
removing all fixed-coordinate kernels already has \(\Omega(W)\) physical
intervals, not \(o(W/H)\).

#### Proof

Each transport moves the two coordinates of \(A\) and the two coordinates
of one partner \(B_\ell\).  If some \(z\in R\) belongs to no
\(B_\ell\), every transport fixes \(z\), and Proposition 4.1 supplies the
common mode \(h_{z,k}\).  Therefore the \(s\) two-sets \(B_\ell\) must
cover all \(|R|=2m-1\) coordinates, forcing \(2s\ge2m-1\), hence
\(s\ge m\).  Equation (5.2) gives \(r_{B_\ell}\ge R_m\) for each chart,
and (5.3) gives (5.7). \(\square\)

If the omitted pair \(A\) is also allowed to vary, every double
transposition moves at most four coordinates.  The same fixed-coordinate
argument forces at least \(\lceil n/4\rceil\) transports before a full
coordinate frame is possible; under the same first-position interval
implementation this again costs \(\Omega(W)\) intervals.

This distinction is logically important.  A menu frame suffices for a
state-adaptive descent iteration only if every chart is available at the
same current state and every chosen endpoint again belongs to a class on
which the menu can be renewed.  The audited pair-omission construction
proves neither condition for the star (0.2).

## 6. Why factor compatibility is not common-matching compatibility

For one fixed \(B\), the order \((A,B,\ldots)\) uses the factor \(F_A\)
on every lower root avoiding \(A\).  A lower root which meets \(A\) but
avoids \(B\) is assigned to \(F_B\), and the rest of the matching is
completed using a pairing of the remaining coordinates.  If \(B\) is
changed, this background assignment changes.

The legality proof for one interval corner uses both coherent endpoint
matchings:

* every old choice coexists with the common background in the first
  endpoint;
* every new choice coexists with the same background in the second
  endpoint.

This proves that a changed token cannot collide with that chart's
background.  It does not compare a \(B\)-alternate with the background of
a different \(B'\)-chart.  Equation (0.2) alone gives no such exclusion.

In fact the natural common-base statement is impossible.

Put

\[
 A_m=\binom{2m-1}{m-1},
 \qquad T=\binom n{m-1}=\frac{m}{m+2}W.
\tag{6.1}
\]

### Theorem 6.1 (star common-base capacity obstruction)

Suppose one matching offers, over one common unchanged background, the old
\(F_A\)-side and every interval replacement for every partner \(B\) in a
family \(\mathscr B\).  In particular, whenever a root belongs to a
changed domain \(\mathcal D_B\), its common old token is its \(F_A\)-token.

For the full family \(\mathscr B=\binom R2\), this is impossible for
\(m\ge6\).  It is already impossible for the reduced spanning frame family
\(\mathscr B=\mathscr B_0\) for \(m\ge8\).

#### Proof

The predecessor-owner map of the exact factor \(F_A\) is a bijection

\[
 S\longmapsto Y(S)=S\cup\{p(S)\}
 \quad\text{from }\binom R{m-1}\text{ to }\binom Rm.
\tag{6.2}
\]

Indeed it is injective by exact middle ownership, and its domain and range
both have size \(A_m\).

First take the full star.  For each \(S\), choose
\(r\in R\setminus Y(S)\) and set

\[
 B(S)=\{p(S),r\}.
\tag{6.3}
\]

Then \(S\cap B(S)=\varnothing\), so this root belongs to
\(\mathcal D_{B(S)}\).  Its alternate middle owner is

\[
 Z(S):=\theta_{B(S)}Y(S)=S\cup\{\alpha_S\},
 \qquad \alpha_S\in A.
\tag{6.4}
\]

The owners \(Z(S)\) are pairwise distinct, because
\(Z(S)\cap R=S\).  They are also disjoint from the old owners \(Y(S)\),
because the former meet \(A\) and the latter avoid \(A\).  Thus the common
matching contains \(A_m\) distinct old owners and must reserve \(A_m\)
further distinct alternate owners.  Its remaining \(T-A_m\) tokens have at
most \(W-2A_m\) available owners.  Necessarily

\[
 T-A_m\le W-2A_m,
 \qquad\text{or equivalently}\qquad
 A_m\le W-T.
\tag{6.5}
\]

But

\[
 \frac{A_m}{W}=\frac{m+1}{2(2m+1)},
 \qquad
 \frac{W-T}{W}=\frac2{m+2}.
\tag{6.6}
\]

Inequality (6.5) is equivalent to
\(m^2-5m-2\le0\), and therefore fails for every \(m\ge6\).

For the reduced family \(\mathscr B_0\), the same construction works for
every \(S\) which does not contain both \(c,d\).  Every such root belongs
to the changed domain of its witnessing pair, so the common old-side
hypothesis forces its \(F_A\)-token.  If \(c\notin S\), use
a pair in the \(c\)-star: take \(B=\{c,p(S)\}\) when \(p(S)\ne c\),
and take \(B=\{c,r\}\), \(r\notin Y(S)\), when \(p(S)=c\).  If
\(c\in S,d\notin S\), use the symmetric \(d\)-star choice.  In every case
the alternate owner again has the form (6.4), and the injection by
intersection with \(R\) remains valid.

The number of forced old owners, and also of distinct reserved alternate
owners, is therefore

\[
 \begin{aligned}
 L_m
 &=A_m-\binom{2m-3}{m-3}\\
 &=\frac{3m}{2(2m-1)}A_m,
 \end{aligned}
\tag{6.7}
\]

The remaining \(T-L_m\) tokens have at most \(W-2L_m\) owners, so
common-background capacity requires \(L_m\le W-T\).  Using
(6.6), this becomes

\[
 3m(m+1)(m+2)\le8(2m-1)(2m+1).
\tag{6.8}
\]

The difference between the left and right sides is

\[
 3m^3-23m^2+6m+8,
\]

which is positive at \(m=8\) and strictly increasing thereafter.
Therefore (6.8) fails for every \(m\ge8\). \(\square\)

The full-star argument forces all \(F_A\)-tokens because its changed-domain
union is \(\binom R{m-1}\).  The reduced argument uses only the roots not
containing both \(c,d\), so it does not assume an \(A\)-first assignment on
the remaining roots.  A recoding can evade the theorem only by changing
the common old side on some exposed roots, releasing owners, or abandoning
the direct partner conjugacies.

The existing adjacent-priority theorem remains valid separately for every
\(B\), with a \(B\)-dependent background.  Theorem 6.1 proves that these
separate cubes cannot be promoted to the natural common-base spanning menu.

## 7. Coherent frame versus charged interval curvature

Let \(v\) be the centered stacked load at a common state.  Suppose, purely
formally, that the upper and lower star endpoints have coherent signals
as in (3.7).  Decompose each signal into its physical interval atoms:

\[
 z_B^\pm=\sum_{I}z_{B,I}^\pm,
\]

and put

\[
 A_B^\pm=\|z_B^\pm\|_w^2,
 \qquad
 V_B^\pm=\sum_I\|z_{B,I}^\pm\|_w^2.
\tag{7.1}
\]

For fair independent interval signs, the exact floor identity is

\[
 \mathbb E\mathcal Q_w
 =\frac{\mathcal Q_w(M_B^0)+\mathcal Q_w(M_B^1)}2
  -\frac{A_B^\pm-V_B^\pm}{4}.
\tag{7.2}
\]

Every corner has the same rankwise mass, so the adjacent-integer floor is a
constant translate of the centered square.  No floor error is hidden in
(7.2).

Combining (3.8) and (7.1) gives the exact inequality

\[
 \boxed{
 \sum_B\bigl[(A_B^+-V_B^+)+(A_B^--V_B^-)\bigr]
 \ge
 \frac1{72(n-1)^2}\|v\|_w^2
 -\sum_B(V_B^++V_B^-).}
\tag{7.3}
\]

If

\[
 \mathcal Q_w(v)=\|v\|_w^2-\beta_w^{\rm fl},
\]

then equivalently

\[
 \sum_B\bigl[(A_B^+-V_B^+)+(A_B^--V_B^-)\bigr]
 \ge
 \frac{\mathcal Q_w(v)+\beta_w^{\rm fl}}
      {72(n-1)^2}
 -\sum_B(V_B^++V_B^-).
\tag{7.4}
\]

The desired charged frame would require the right side to be a positive
fraction of \(\mathcal Q_w(v)-C_AH\operatorname{Cat}_m\) whenever that
quantity is positive.  Nothing in the boundary count (5.4) implies this.
The count controls the number of physical seams; it does not control the
square action of the depth strips carried by a seam.  In the aligned
reverse chart one interval path has \(O(q)\) signed occurrences at depth
\(q\), and therefore \(O(H^2)\) unweighted square action through depth
\(H\), despite only two new runs.  In the orientation-preserving chart,
the same collar count gives the same critical \(H^2\)-scale after summing
depths.

Thus an \(o(W/H)\) boundary catalog is compatible with a variance toll as
large as \(o(WH)\); at Gaussian depth this is far above the desired
\(o(W)\) floor excess.  A separate positive-curvature or variance-routing
estimate is indispensable.

There is an exact first-upper witness to this distinction.  In one
fixed-partition adjacent block, two distinct occurrences of the same
depth-one upper target have disjoint two-point collars: a common collar
coordinate would identify an adjacent middle window, contradicting exact
middle ownership.  Two movable occurrences for the same partner pair
would both have to contain a partner coordinate in their collars.
Therefore the activated multiplicity satisfies

\[
 \mu_{j,1,U}\le1,
 \qquad
 A_{j,1}-V_{j,1}=0
\tag{7.5}
\]

for every adjacent partner chart.  Every pure lower-dual atom fixes all
upper flags, so adjoining them does not change (7.5).

On the other hand, the first priority phase has
\(A_m=\binom{2m-1}{m-1}\) depth-one upper occurrences but only

\[
 \binom{2m-1}{m+1}
 =\frac{m-1}{m+1}A_m
\]

possible local targets.  Its collision excess is therefore at least

\[
 A_m-\binom{2m-1}{m+1}
 =\frac{2A_m}{m+1}
 =\frac W{2m+1}=\operatorname {Cat}_m.
\tag{7.6}
\]

Thus the partner-plus-pure-lower menu has zero charged depth-one frame on
a genuine exact token state with nonzero depth-one excess.  This does not
contradict a contraction theorem which explicitly absorbs
\(O_A(H\operatorname {Cat}_m)\) into its stopping baseline, but it rules
out an unqualified positive comparison with the entire floor excess.  It
also concerns the sum of within-block interval gaps.  The separately proved
overlapping adjacent-layer cube has negative neighboring-block cross-Grams
which can charge joined depth-one targets; no uniform lower bound for that
joined census is currently known.

## 8. Exact lower-dual atoms and the binary-catalog rank obstruction

The partner-pair chart fixes all lower flags because its exchanged lower
root avoids both partner pairs.  There is nevertheless a completely local
dual atom if coordinate-orbit copies of a local factor are allowed.

Let

\[
 e=(P,\pi,i),
 \qquad \pi=(x_t)_{t\in\mathbb Z_{2m-1}}
\]

be a token with

\[
 S_i=I_\pi(i,m-1),
 \qquad Y_i=I_\pi(i-1,m).
\]

Fix \(2\le q\le H\), put

\[
 b=x_{i+q-2},
 \qquad a=x_{i+q-1},
 \qquad \tau=(a\ b),
\tag{8.1}
\]

and compare \(e\) with the coordinate-conjugate token \(\tau e\).
Both \(a,b\) lie in \(S_i\), so \(\tau\) fixes \(S_i\) and \(Y_i\) as
sets.

### Theorem 8.1 (one-depth pure lower atom)

The two tokens \(e,\tau e\) have identical lower root and middle owner.
Every upper flag agrees.  Every lower flag except depth \(q\) agrees, and
at depth \(q\)

\[
 \boxed{
 L_q(\tau e)=L_q(e)-\{a\}+\{b\}.}
\tag{8.2}
\]

Thus the complete signed-depth innovation is the single Johnson edge

\[
 \boxed{
 d_{e,q}=\delta_{L_q-a+b}-\delta_{L_q}.}
\tag{8.3}
\]

Any collection of such old/dual alternatives on distinct lower roots of a
middle-simple matching is centrally compatible: every alternative keeps
its old middle owner.

#### Proof

Every upper flag contains the whole lower root \(S_i\), and hence contains
both \(a,b\); transposing them fixes the flag as a set.  A lower depth
\(p\) flag starts at \(x_{i+p-1}\) and ends at \(x_{i+m-2}\).  If
\(p<q\), it contains both \(b,a\).  If \(p=q\), it contains \(a\) but
not its immediate predecessor \(b\).  If \(p>q\), it contains neither.
This proves (8.2)--(8.3).

The transposition fixes \(S_i\) and \(Y_i\).  Therefore choosing either
token at a lower root neither changes that root nor its middle owner.
Distinct roots in the old matching have distinct owners, so arbitrary
choices remain lower-saturating and middle-simple. \(\square\)

The qualifier “coordinate-orbit” is necessary, and for a nonzero atom the
fixed-factor version is impossible.  Since \(a,b\in Q_P\), the
transposition fixes the omitted pair \(P\) and sends the row to a row of
\(\tau F_P\).  If both distinct occurrences belonged to one fixed exact
factor \(F_P\), that factor would contain the same middle owner \(Y_i\)
twice, contrary to exact middle ownership.  They cannot be the identical
pointed occurrence, because their depth-\(q\) lower flags differ.  Hence a
nontrivial depth-isolated atom intrinsically uses typed conjugate factors;
it cannot be installed inside the same fixed \(F_P\).

### Corollary 8.2 (algebraic lower span)

For fixed \(q\ge2\), the vectors (8.3), over the coordinate-orbit token
system, span the whole centered space on
\(\binom X{m-q}\).

#### Proof

The graph whose vertices are the rank-\((m-q)\) subsets and whose edges
replace one coordinate by one outside coordinate is the Johnson graph.  It
is connected: replace the elements of \(S\setminus T\) one at a time by
the elements of \(T\setminus S\).  Oriented incidence vectors of the edges
of any connected graph span the codimension-one zero-sum subspace.

Every such edge is a coordinate image of (8.3): place its deleted and
inserted coordinates in the adjacent positions \(a,b\), place the common
core in the remaining \(m-q-1\) lower-window positions, and complete the
cyclic row arbitrarily.  The coordinate-orbit token system contains the
resulting row. \(\square\)

### Theorem 8.3 (joint binary-catalog no-frame theorem)

The boundary interpretation has an exact telescoping form.  For
consecutive lower roots in one oriented physical row,

\[
 \boxed{L_q(i)=\bigcap_{h=0}^{q-1}S_{i+h}.}
\tag{8.3a}
\]

Consequently, suppose the two phases of one interval block list the same
lower roots \(S_u,S_{u+1},\ldots,S_v\) in the same orientation.  Every
switched token whose next \(q-1\) roots remain inside the block has the
same lower depth-\(q\) flag in both phases.  Only the final \(q-1\) token
positions can change.  At \(q=2\), one such binary block therefore changes
at most one lower occurrence and has innovation support at most two.

Indeed, the intersection of the length-\((m-1)\) windows beginning at
\(i,i+1,\ldots,i+q-1\) is exactly the length-\((m-q)\) window beginning
at \(i+q-1\), proving (8.3a).  The endpoint-strip assertion follows from
equality of the ordered roots inside the two phases.

Consider one common state and a joint binary chart cube with \(B\) bits.
Assume each lower-dual bit has two coherent sides and is a union of
endpoint-aligned same-orientation physical intervals; assume the upper
partner bits fix all lower loads.  Then the affine span of all lower
depth-two load vectors in the cube has dimension at most \(B\).

Consequently, if

\[
 B<\binom n{m-2}-1,
\tag{8.4}
\]

there is a nonzero centered lower-depth-two mode invariant under every
corner difference.  No strictly positive frame inequality on all weighted
excess modes can hold for that cube.  In particular this applies for all
sufficiently large \(m\) whenever

\[
 B=o(W/H),\qquad H\ge2.
\tag{8.5}
\]

#### Proof

A binary cube with bits \(1,\ldots,B\) has load vectors of the form

\[
 x_0+\sum_{j=1}^B\varepsilon_jd_j,
 \qquad \varepsilon_j\in\{0,1\},
\]

on every linear target ledger.  Hence its affine difference space is
contained in \(\operatorname{span}\{d_1,\ldots,d_B\}\) and has dimension
at most \(B\).  At lower depth two the ambient centered layer has dimension
\(N_2-1\), where

\[
 N_2=\binom n{m-2}
 =\frac{m(m-1)}{(m+2)(m+3)}W
 =(1-o(1))W.
\tag{8.6}
\]

If (8.4) holds, choose a nonzero centered vector perpendicular to every
\(d_j\).  Every upper partner bit has zero lower projection, so this vector
is invisible to the entire cube.  Finally (8.5) implies
\(B=o(W)<N_2-1\) for all sufficiently large \(m\). \(\square\)

For the pure atoms of Theorem 8.1 the obstruction is even more literal:
at \(q=2\), one binary atom supplies exactly one Johnson-edge direction.
Thus an algebraically spanning binary subdictionary requires at least
\(N_2-1=\Theta(W)\) atoms.  If every atom is inserted into its conjugate
source row separately, it also costs order \(W\) physical row
initializations.

Theorem 8.3 has a precise scope.  It does not rule out:

1. a menu from which only one low-boundary cube is chosen adaptively at a
   time;
2. repeated endpoint-stable renewal, so that the visible span rotates with
   the state;
3. a multiway threshold variable on one long path, whose many possible
   seam positions have affine span much larger than one although any one
   chosen state has only two boundaries.

None of these three escapes is supplied by the current pair-omission
interval theorem.

The multiway escape can also be excluded for a one-shot universal
load-space theorem, although not by rank.

### Theorem 8.4 (multiway depth-two capacity obstruction)

Fix one reference threshold on each of \(B\) reverse paths, and allow an
arbitrary legal threshold on each path.  Also allow endpoint-aligned
same-orientation lower intervals, counting every independently chosen
interval among the \(B\) objects.  If \(x\) and \(y\) are respectively
the reference and corner lower-depth-two loads, then

\[
 \boxed{
 \sum_R(y_R-x_R)_+\le B.}
\tag{8.8}
\]

Consequently there is, for every sufficiently large \(m\), an integral
load \(x\) of the correct token-core mass \(T=\binom n{m-1}\) and with
\(R_0=\Theta(W)\) lower-depth-two holes such that every corner has
undoubled factorial-floor excess at least

\[
 \boxed{R_0-B.}
\tag{8.9}
\]

Thus \(B=o(W/H)\) leaves \(\Theta(W)\) excess on this ambient integral
profile even when every path has all of its threshold states.

#### Proof

For a reverse path, changing from one threshold to another switches one
consecutive interval \(I=[u,v]\).  At depth two its exact telescoping
innovation is

\[
 E_{m-2}(I)-E_{m-2}(I+1)
 =\delta_{I_\pi(u,m-2)}-
  \delta_{I_\pi(v+1,m-2)}.
\tag{8.10}
\]

It has positive \(\ell_1\)-mass one.  The same-orientation collar identity
(8.3a) gives at most one substitution for an aligned interval.  Positive
variation is subadditive under summation, proving (8.8).  Upper
partner-pair intervals have zero lower projection and change nothing.

Put \(N=N_2^-=\binom n{m-2}\).  The exact token-core ratio is

\[
 \frac TN=\frac{m+3}{m-1}=1+\frac4{m-1}.
\tag{8.11}
\]

For \(m\ge6\), the two balanced integral levels are one and two.  Start
with load two at

\[
 \delta=T-N=\frac4{m-1}N
\]

targets and load one elsewhere.  On
\(R_0=\lfloor(N-\delta)/2\rfloor=\Theta(W)\) disjoint pairs of the
load-one targets, replace \((1,1)\) by \((2,0)\).  This preserves mass and
creates exactly \(R_0\) holes.  For

\[
 e_1(t)=\frac12(t-1)(t-2),
\]

each hole contributes one and every coordinate contributes
nonnegatively.  A hole stops contributing only if it receives positive
load.  Inequality (8.8) allows this for at most \(B\) holes, proving
(8.9). \(\square\)

The profile in Theorem 8.4 is an abstract integral flag-load vector.  Its
realization as the lower-depth-two load of one literal prepared factor is
not proved.  Therefore the theorem refutes an unrestricted weighted-mode
frame, while a factor-restricted structural theorem or repeatedly renewed
moving-seam process remains logically possible.

## 9. Certified boundary

The following statements are proved.

1. One can attach one fixed conjugate factor to every partner pair in a
   spanning star, with no duplicate factor type.
2. The \(2n-7\) transports in \(\mathscr B_0\) already generate \(A_n\)
   with word diameter at most \(12(n-1)\).
3. They satisfy the exact weighted frame (3.1), and the formal
   upper-plus-lower frame (3.6), with constant
   \(1/[288(n-1)^2]\).
4. Fixed-partition adjacent partner charts do not frame all modes; the
   unpaired-coordinate mode (4.1) is an exact common kernel.
5. Every one-star-generator interval chart has \(O(W/m)=o(W/H)\)
   boundaries for \(H=o(m)\), whereas the reduced joint frame catalog has
   \(\Theta(W)\) intervals and the full star has \(\Theta(mW)\).
6. The exact harmonic-to-Haar inequality is (7.3); its variance term cannot
   be omitted or bounded from the seam count alone.
7. Pure one-depth lower-dual Johnson atoms exist in the coordinate-orbit
   token system and span every centered lower layer, but no nonzero such
   parallel atom can lie wholly inside one fixed exact local factor.
8. A joint binary catalog with \(o(W/H)\) bits cannot frame the
   \(\Theta(W)\)-dimensional lower-depth-two layer.
9. The full star has no common direct-old-side matching for \(m\ge6\), and
   the reduced spanning family already has none for \(m\ge8\).
10. Even multiway reverse-path thresholds have only one unit of positive
    depth-two capacity per path; a universal ambient integral profile keeps
    \(\Theta(W)\) excess under \(o(W/H)\) paths.

The following statements are unproved and are necessary for composition
into constant one.

* a different nonparallel lower-dual construction inside the same fixed
  local factors; the pure atoms of Theorem 8.1 provably require conjugate
  typed copies;
* endpoint closure/renewability after choosing a chart;
* a charged curvature estimate making the sum of \(V_B^\pm\) subordinate
  to the framed excess above \(O_A(H\operatorname{Cat}_m)\).
* if a factor-restricted theorem is sought despite Theorems 8.3--8.4, a
  new structural result forcing every prepared lower-depth-two load to have
  only \(o(W/H)\) dispersed holes outside the adaptive collars.

Hence the representation-theoretic span is now proved.  The required
physical charged frame under one joint binary \(o(W/H)\)-boundary catalog
is refuted by Theorem 8.3.  The fixed-partition menu is independently
refuted by Proposition 4.1, and the natural spanning-star common base is
impossible by Theorem 6.1.  A surviving route must use a non-
\(A\)-first recoding with released owners, a repeatedly renewed menu, or
genuinely nonlocal lower circuits, together with the fixed-factor and
curvature lemmas stated above.

## 10. Audit of the decisive constants

Three independent checks isolate all constants used in the no-go.

1. The group calculation uses only the \(c\)-star and \(d\)-star
   generators.  A rooted three-cycle costs two generators, an arbitrary
   three-cycle costs at most twelve, and an even permutation costs at most
   \(n-1\) three-cycles.  Thus \(D_n=12(n-1)\), giving raw energy constant
   \(2/D_n^2=1/[72(n-1)^2]\) and projection constant one quarter of this,
   namely \(1/[288(n-1)^2]\).
2. In the reduced owner obstruction,
   \[
    \frac{\binom{2m-3}{m-3}}{A_m}
    =\frac{m-2}{2(2m-1)},
   \]
   so the exposed fraction is exactly \(3m/[2(2m-1)]\).  The capacity
   polynomial is \(3m^3-23m^2+6m+8\), negative at \(m=7\), positive at
   \(m=8\), and increasing thereafter.
3. At lower depth two, the reverse-path formula is the literal telescoping
   sum
   \[
    \sum_{i=u}^v\delta_{I_\pi(i,m-2)}
    -\sum_{i=u+1}^{v+1}\delta_{I_\pi(i,m-2)},
   \]
   leaving exactly one positive and one negative endpoint.  Thus the rank
   and positive-capacity bounds use one unit per path, with no hidden
   factor two.

These checks do not use probabilistic, asymptotic, or completion
assumptions.  The only explicitly nonphysical witness is the ambient
integral load profile in Theorem 8.4, whose factor realizability is marked
as unproved.
