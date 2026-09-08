# Contextual moving-frame \(B_4\) recursion: rigidity, provider failure, and the growing-span boundary

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

Imported exact input: the maximum-isometric \(C_{2h}\)-factor of \(Q_h\)
for dyadic \(h\), with sibling-labelled two-sided trace injectivity through
depth \(h/2\), as proved in
`MATH_THEOREM_FIRST_ELIGIBLE_B4_SCD_PACKET_FACTOR_20260726.md`, Theorem
3.1 and Section 4.  This is the only nonstandard construction imported;
the analytic proof also uses the standard uniform bivariate lattice local
central-limit theorem and Stirling's formula.

## 0. Verdict

The three bounded contextual \(B_4\)/SCD grammars analyzed below do not
escape the direct product obstruction.  Their superficially different
forms of frame motion can be classified exactly.

1. **Full-face packet recursion is rigid.**  If an owner packet is a
   literal \(Q_h\), every cube edge is a Johnson edge, and every cube
   two-face is a geodesic central \(B_4\) square, then there are fixed
   disjoint pairs

   \[
       \{a_i,b_i\}\qquad(1\le i\le h)
   \]

   such that the entire packet is the one status cube

   \[
       X-\{a_i:i\in S\}+\{b_i:i\in S\},
       \qquad S\subseteq[h].
   \]

   Thus contextual \(B_4\) charts cannot genuinely change the physical
   pair frame inside a cubical packet.  They can only regroup the already
   fixed pair directions.  The same conclusion holds on every complete
   isometric \(C_{2h}\): its physical cycle uniquely determines one
   \(h\)-pair frame.
2. **A large contextual catalogue exists but still fails providers.**
   An explicit logarithmic frozen anchor chooses among \(n\) cyclic-shift
   perfect matchings on \(2n=2m-O(\log m)\) bulk coordinates.  The union
   of these matchings is \(K_{n,n}\); every individual matching carries
   \(\Theta(W/n)\) owner mass; first-eligible \(B_4\) packets cover
   \(W-e^{-\Omega(m)}W\) owners; and the factor can be made exactly
   complement-equivariant.  Nevertheless, at every

   \[
       q=\lfloor A\sqrt m\rfloor\le r,\qquad A>0,
   \]

   it has, at each sign,

   \[
       \boxed{
       M_q^\pm\ge(\delta_A-o(1))W,\qquad
       \delta_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.}
   \]

   Conditioning on the trace-visible anchor freezes one matching, and
   the fixed-pair full-pair statistic gives the displayed Gaussian Hall
   cut.  Bulk-projection-free union of the contextual frames, apart from
   the \(O(\log m)\) anchor, does not couple the frozen target sectors.
3. **Maximal chart motion is pure gauge.**  On every physical
   \(C_{2h}\), even \(h\ge4\), the two staggered pairings of consecutive
   swap carriers give a contextual central-\(B_4\) frame at every vertex.
   All \(h\) carriers change quartet partner at every step, and the atlas
   is complement-symmetric.  The successor permutation \(P\) is unchanged,
   so every trace

   \[
       L_q(X)=\bigcap_{j=0}^qP^jX,\qquad
       U_q(X)=\bigcup_{j=0}^qP^jX
   \]

   is unchanged.  This is positive-density frame motion, but not a shadow
   repair.
4. **Existential provider union is insufficient.**  Take the complete
   coordinate-conjugacy orbit of the preceding complement-symmetric
   factor.  It contains a provider for every complete two-sided nested
   \(H\)-flag.  At one depth, every target has exactly the same positive
   number of provider states.  Yet every individual state retains the
   linear Gaussian deficit above.  The failed implication is

   \[
       \forall T\ \exists\text{ a state providing }T
       \quad\not\Longrightarrow\quad
       \exists\text{ one state providing almost every }T.
   \]

5. **Short closed routers obey a sharp recurrence cut.**  For a full
   middle-layer cycle factor whose components have length at least \(2q\),
   let \(A_D\) count coordinate recurrence arcs of cyclic span at most
   \(D\).  If \(M_q^\pm\) are the two signed depth-\(q\) target holes,
   then, for \(D<q\),

   \[
   \boxed{
   A_D\le
   \frac{4q}{q-D}(W-N_q)
   +\frac{2q}{q-D}(M_q^-+M_q^+),
   \qquad N_q=\binom{2m}{m-q}.}
   \]

   In particular, at \(q=2D\le H\),

   \[
       \frac{A_D}{W}
       \le \frac{32D^2}{m}
          +4\frac{M_q^-+M_q^+}{W}.
   \]

   Therefore an \(o(W)\)-hole factor cannot have a positive density of
   bounded-witness-multiplicity genuine frame changes of span
   \(D=o(\sqrt m)\).  Under exact depth-\(2D\) coverage, repair on the
   \(\Omega(W/\sqrt m)\) scale already requires
   \(D=\Omega(m^{1/4})\).  Fixed positive-density genuine motion requires
   \(\Omega(\sqrt m)\) temporal span.  In models assigning a distinct
   live token to each open twist, it also requires
   \(\Omega(\sqrt m)\) average live storage.

Thus three precise bounded grammars are refuted: complete full-face cube
recursion, fixed-\(P\) frame decoration, and bounded-temporal-span genuine
routers with an \(O(1)\)-to-one twist-witness map.  A bounded seed used
with long delayed restitution is not refuted; it belongs to the surviving
path-only, exterior-moving route with genuinely growing temporal span.
That route must change the actual successor \(P\), not merely its quartet
description, and must then solve the correlated integral all-depth
configuration-Hall problem.  No constant-one conclusion is asserted.

## 1. Contextual \(B_4\) charts are edgewise universal

Let \(V=[2m]\) and let \(X\to Y\) be a directed Johnson edge.  Write

\[
 a=X\setminus Y,\qquad b=Y\setminus X,\qquad
 R=X\cap Y,\qquad D=V\setminus(X\cup Y).
 \tag{1.1}
\]

Then

\[
 |R|=|D|=m-1.
 \tag{1.2}
\]

### Lemma 1.1 (exact number of central-\(B_4\) edge charts)

Every directed Johnson edge has exactly \((m-1)^2\) contextual
central-\(B_4\) embeddings.

#### Proof

Choose \(s\in R\) and \(c\in D\).  On

\[
 B=\{a,b,s,c\}
\]

use the central square

\[
 sa\longrightarrow sb\longrightarrow cb
 \longrightarrow ca\longrightarrow sa.
 \tag{1.3}
\]

Its omitted matching is

\[
 ab\mid sc.
\]

After adjoining the fixed set \(R\setminus\{s\}\), the first edge of
(1.3) is precisely

\[
 R+a=X\longrightarrow R+b=Y.
\]

Conversely, a central-\(B_4\) chart containing \(X\to Y\) must choose one
additional coordinate of \(X\cap Y\) and one of
\(V\setminus(X\cup Y)\), so it determines \(s,c\) uniquely.  There are
\((m-1)^2\) choices. \(\square\)

Complementation exchanges the roles of \(s\) and \(c\) and reverses the
membership roles of \(a,b\).  Hence these charts can always be paired
complement-equivariantly.

Lemma 1.1 is a warning: the phrase “every selected edge lies in a
contextual \(B_4\)” imposes no restriction on the edge rule.  Whole-cell
closure and the actual successor permutation are the substantive data.

## 2. Isometric-cube rigidity

Write \(Q_h=2^{[h]}\).  A map

\[
 \varphi:Q_h\longrightarrow\binom Vm
\]

is called **two-face physical** when it is injective, every cube edge maps
to a Johnson edge, and the endpoints of every two-edge cube geodesic have
Johnson distance two.  Equivalently, every cube two-face is a geodesic
central \(B_4\) square.

### Lemma 2.1 (unique opposite corner)

Let

\[
 Y_1=X-a_1+b_1,\qquad
 Y_2=X-a_2+b_2,
\]

where \(a_1,a_2\in X\), \(b_1,b_2\notin X\), and the four labels are
distinct.  The unique \(m\)-set \(Z\) satisfying

\[
 d_J(X,Z)=2,\qquad d_J(Y_1,Z)=d_J(Y_2,Z)=1
\]

is

\[
 Z=X-\{a_1,a_2\}+\{b_1,b_2\}.
 \tag{2.1}
\]

#### Proof

Write \(Z=X-A+B\), with \(A\subset X\), \(B\subset V\setminus X\) and
\(|A|=|B|=2\).  Direct comparison gives

\[
 d_J(Z,Y_i)=3-\mathbf1_{\{a_i\in A\}}
               -\mathbf1_{\{b_i\in B\}}.
\]

For this distance to equal one, both indicators must equal one.  This for
\(i=1,2\) forces

\[
 A=\{a_1,a_2\},\qquad B=\{b_1,b_2\}.
\]

\(\square\)

### Theorem 2.2 (full-face contextual cube rigidity)

Let \(\varphi:Q_h\to J(V,m)\) be two-face physical and put
\(X=\varphi(\varnothing)\).  There are pairwise distinct

\[
 a_1,\ldots,a_h\in X,\qquad
 b_1,\ldots,b_h\in V\setminus X
\]

such that, for every \(S\subseteq[h]\),

\[
 \boxed{
 \varphi(S)
 =X-\{a_i:i\in S\}+\{b_i:i\in S\}.}
 \tag{2.2}
\]

Consequently the image is one status cube for the fixed matching

\[
 M_\varphi=\{\{a_i,b_i\}:1\le i\le h\}.
 \tag{2.3}
\]

#### Proof

For a coordinate neighbour write

\[
 \varphi(\{i\})=X-a_i+b_i.
\]

For \(i\ne j\), the distance between these two neighbours is two.
Therefore \(a_i\ne a_j\) and \(b_i\ne b_j\); deletion and insertion
labels are automatically disjoint because they lie on opposite sides of
\(X\).

We prove (2.2) by induction on \(|S|\).  It holds for \(|S|\le1\).
For \(|S|\ge2\), choose distinct \(i,j\in S\) and put
\(T=S\setminus\{i,j\}\).  By induction, the three already determined
vertices of the \(ij\)-face based at \(T\) are

\[
\begin{aligned}
 X_T&=X-\{a_k:k\in T\}+\{b_k:k\in T\},\\
 X_{T+i}&=X_T-a_i+b_i,\\
 X_{T+j}&=X_T-a_j+b_j.
\end{aligned}
\]

Lemma 2.1 forces the fourth corner to be

\[
 X_T-\{a_i,a_j\}+\{b_i,b_j\},
\]

which is (2.2). \(\square\)

### Corollary 2.3 (no genuine moving frame inside a full packet)

Any recursive \(B_4\) construction retaining a complete \(Q_h\) owner
packet and making **every abstract cube two-face** a two-sided geodesic
central square has one fixed physical pair frame throughout that packet.
A context rule may change orientations, roots, or the way consecutive
fixed pairs are grouped into quartets, but cannot change the pairs (2.3).
Geodesicity only along one selected cycle is not enough for this
conclusion.

A genuine moving-frame construction must therefore leave the full-face
cube grammar: it must use path-only routers, overlapping packet changes,
or exterior-moving transitions.

### Theorem 2.4 (isometric-strand frame rigidity)

Let

\[
 C=(X_0,X_1,\ldots,X_{2h-1})\subseteq J(V,m),\qquad h\ge2,
\]

be an isometric cycle.  Then there are a unique frozen core \(K\) and,
after fixing the displayed root and orientation, unique distinct labels
\(z_0,\ldots,z_{2h-1}\) such that

\[
 X_i=K\mathbin{\dot\cup}
       \{z_i,z_{i+1},\ldots,z_{i+h-1}\}
 \qquad(i\bmod 2h).
 \tag{2.4}
\]

In particular, the physical edge supports of \(C\) are the fixed matching

\[
 \big\{\{z_i,z_{i+h}\}:0\le i<h\big\},
 \tag{2.5}
\]

each used twice.  Thus a genuine frame change cannot occur inside one
isometric strand.

#### Proof

The opposite vertices satisfy \(d_J(X_0,X_h)=h\).  Put

\[
 K=X_0\cap X_h,\qquad A=X_0\setminus X_h,
 \qquad B=X_h\setminus X_0.
\]

The first half is a geodesic, so in chronological order it removes the
distinct labels \(a_0,\ldots,a_{h-1}\in A\) and inserts the distinct labels
\(b_0,\ldots,b_{h-1}\in B\).  The first edge of the second half removes
some \(b'_0\in B\) and inserts some \(a'_0\in A\).  Isometry of the shifted
opposite pair \((X_1,X_{h+1})\) forces their intersection to be exactly
\(K\); hence \(a'_0=a_0\) and \(b'_0=b_0\).  Shifting the same argument by
\(i\) shows that edge \(h+i\) reverses exactly edge \(i\).

Set \(z_i=a_i\) and \(z_{h+i}=b_i\).  The chronological geodesic formulas
now give (2.4), and the edge supports give (2.5).  They determine the
active matching uniquely; also \(K=\bigcap_iX_i\), so the core is unique.
\(\square\)

The path-only escape named above therefore means a splice of proper
geodesic segments with a moving exterior/collar, not a contextual
re-pairing along one complete isometric cycle.

## 3. A complement-equivariant bulk-moving contextual atlas

The preceding theorem does not force the same fixed matching in different
packets.  We now construct an atlas with many packet frames and then prove
that its provider union still fails.

Choose an even integer

\[
 d=\log_2m+O(1)
 \tag{3.1}
\]

such that

\[
 n=m-\frac d2
 \]

is even and

\[
 n\le2^{d-1}<32n.
 \tag{3.2}
\]

For all sufficiently large \(m\), such a \(d\) exists with the displayed
constant.  Namely, take the least integer \(d\equiv2m\pmod4\) for which
\(2^{d-1}\ge m\).  Then \(n\) is even, the preceding admissible integer
\(d-4\) gives \(2^{d-5}<m\), and hence

\[
 n<m\le2^{d-1}<16m<32n.
\]

Split

\[
 V=A\mathbin{\dot\cup}L\mathbin{\dot\cup}R,
 \qquad |A|=d,\quad |L|=|R|=n,
 \tag{3.3}
\]

and index \(L,R\) by \(\mathbb Z_n\).

For \(x=(x_1,\ldots,x_d)\in2^A\), put

\[
 u(x)=(x_1\oplus x_d,\ldots,x_{d-1}\oplus x_d)
       \in\mathbb F_2^{d-1}.
 \tag{3.4}
\]

Then

\[
 u(\bar x)=u(x).
 \tag{3.5}
\]

Choose a balanced surjection

\[
 \tau:\mathbb F_2^{d-1}\longrightarrow\mathbb Z_n
 \tag{3.6}
\]

whose fibres have size at most thirty-two, and define the perfect matching

\[
 M_x=
 \big\{\{L_i,R_{i+\tau(u(x))}\}:i\in\mathbb Z_n\big\}.
 \tag{3.7}
\]

Equations (3.5)--(3.7) give

\[
 M_{\bar x}=M_x,\qquad
 \bigcup_{x\in2^A}M_x=K_{L,R}.
 \tag{3.8}
\]

For each shift \(\tau(u(x))\), fix a pairing of the \(n\) edges of
\(M_x\) into \(n/2\) ordered pairs, using the identical pairing for the
complementary anchors \(x,\bar x\).  Each pair of matching edges is a
four-coordinate block.  Its four orientations, taking
one endpoint from each edge, are the central \(B_4\) square; the two
matching edges themselves are the two singleton middle chains of the
local \(B_4\) SCD.

Assume \(H=o(n)\), and fix

\[
 H\ll r\le n/16,\qquad r=o(n),
 \tag{3.9}
\]

with \(r\) a power of two.  In anchor sector \(x\), scan the \(n/2\)
quartets and select the first \(r\) whose local state is in the central
square.  Freeze every other coordinate.

Within each selected quartet, relabel its two physical status directions
into the sibling positions required by the established recursive
trace-injective \(Q_{2r}\)-factor.  This ordering is part of the
construction: an arbitrary isometric factor of the packet would not by
itself imply all-depth trace injectivity.

The parameter choice is nonempty: a power of two in
\([\sqrt{Hn},2\sqrt{Hn})\) has \(H/r=o(1)\), \(r=o(n)\), and
\(r\le n/16\) for all sufficiently large \(m\).

### Theorem 3.1 (contextual packet factor)

The construction above partitions all but

\[
                         e^{-\Omega(m)}W
 \tag{3.10}
\]

middle owners into \(Q_{2r}\)-packets.  It admits an integral physical
\(C_{4r}\)-factor in every packet with both signed trace maps injective
inside the packet through every \(q\le r\).  The global retained factor
can be chosen to satisfy

\[
                         P(X^c)=P(X)^c.
 \tag{3.11}
\]

Moreover every one of the \(n\) matchings in (3.7) carries
\(\Theta(W/n)\) retained owners, while their bulk union graph is
\(K_{n,n}\).

#### Proof

Changing the four orientations in a selected quartet leaves it eligible
and changes neither the anchor nor the matching \(M_x\).  Earlier skipped
quartets and every later quartet are frozen.  Hence the selected indices
and the packet are constant throughout the packet.  Distinct packets are
disjoint by the usual first-eligible equivalence-class argument, and each
packet is

\[
 (Q_2)^r=Q_{2r}.
\]

Before conditioning the total rank, a quartet is eligible with probability
\(4/16=1/4\).  There are \(n/2\) quartets, so the mean eligible count is
\(n/8\), at least twice \(r\).  Chernoff's exponential-moment bound gives
probability \(e^{-\Omega(n)}\) of fewer than \(r\) eligible quartets.
For a fixed anchor \(x\), the bulk rank is

\[
 k=m-|x|=n+O(d).
\]

Uniformly in \(x\),

\[
 2^{-2n}\binom{2n}{k}=\Theta(n^{-1/2}),
\]

so conditioning on that rank changes the exponential bound only by a
polynomial factor.  Summing the anchor sectors proves (3.10).

The established exact isometric \(Q_{2r}\)-factor gives the physical
cycles and intrapacket trace injectivity.  Complement preserves the anchor
code, the matching, quartet eligibility, and the central square.  Pair
complementary packets; choose a factor on one packet and define the factor
on its companion by (3.11).

Finally, (3.2) and the balanced choice of \(\tau\) give between one and
thirty-two \(u\)-codes, hence between two and sixty-four anchor words, per
shift.  The \(2^d\) anchor sectors have asymptotically equal
middle-owner masses because \(d=O(\log m)=o(\sqrt m)\).  Thus a fixed
shift matching carries \(\Theta(W/n)\) owners; the exponentially small
uniform packet leave does not change this estimate.  Equation (3.8)
proves the union claim. \(\square\)

This is a genuine contextual frame catalogue on \(1-o(1)\) owner mass.
Its bulk frame union has no surviving positive-density coordinate
projection; only the \(O(\log m)\)-coordinate anchor is fixed.  The next
section shows why this is still not an all-depth provider theorem.

## 4. The frozen-context Gaussian Hall cut

Fix an anchor \(x\), put

\[
 k=m-|x|,
\]

and for a bulk set \(S\subseteq L\cup R\) let

\[
 F_x(S)=\#\{e\in M_x:e\subseteq S\}.
 \tag{4.1}
\]

At every middle vertex, each active matching edge remains split, while
every frozen matching edge retains its empty, split, or full status.  In
a lower trace, a touched split edge becomes empty and a full edge stays
full.  Therefore every lower trace \(T\) rooted at \(X\) satisfies

\[
                         F_x(T)=F_x(X).
 \tag{4.2}
\]

For a uniform \(k\)-subset of \(2n\) coordinates, the number of sets with
exactly \(f\) full matching edges is

\[
 S_{k,f}
 =
 \frac{n!}{f!\,(n-k+f)!\,(k-2f)!}\,2^{k-2f}.
 \tag{4.3}
\]

For a target of bulk rank \(k-q\), the corresponding count is

\[
 T_{k-q,f}
 =
 \frac{n!}{f!\,(n-k+q+f)!\,(k-q-2f)!}\,2^{k-q-2f}.
 \tag{4.4}
\]

### Lemma 4.1 (uniform full-pair central limit)

Let \(k=n+O(\log n)\) and

\[
 q=A\sqrt n+O(1),\qquad A>0\text{ fixed}.
\]

For a uniform \(k\)-subset, the full-pair count \(F\) has

\[
 \mu_{n,k}:=\mathbb EF
 =\frac{k(k-1)}{2(2n-1)},
 \tag{4.5}
\]

and

\[
 \frac{F-\mu_{n,k}}{\sqrt n/4}
 \Longrightarrow N(0,1)
 \tag{4.6}
\]

uniformly in the displayed range of \(k\).  Also

\[
 \frac{\binom{2n}{k-q}}{\binom{2n}{k}}
 \longrightarrow e^{-A^2},
 \tag{4.7}
\]

and

\[
 \mu_{n,k}-\mu_{n,k-q}
 =\frac q2+O(1).
 \tag{4.8}
\]

#### Proof

Under independent fair bits on each matching pair, let \(Y_i\) be the
local rank and \(I_i=\mathbf1_{\{Y_i=2\}}\).  Then

\[
\begin{aligned}
 \mathbb EY_i&=1,&\operatorname {Var}Y_i&=\frac12,\\
 \mathbb EI_i&=\frac14,&\operatorname {Var}I_i&=\frac3{16},\\
 \operatorname {Cov}(Y_i,I_i)&=\frac14.
\end{aligned}
\]

The Schur complement of the limiting covariance matrix is

\[
 \frac3{16}-\frac{(1/4)^2}{1/2}=\frac1{16}.
\]

Consequently, conditioning on \(\sum_iY_i=k\), the bivariate lattice
local central-limit theorem gives

\[
 \operatorname {Var}\!\left(F\mid\sum_iY_i=k\right)
 =\frac n{16}+o(n)
\]

and the conditional normal limit (4.6).  Uniformity for
\(k-n=O(\log n)\) follows from the uniform local theorem in an
\(o(\sqrt n)\) window.  Direct indicator counting gives (4.5):

\[
 \mathbb EF=n\frac{(k)_2}{(2n)_2}.
\]

Equation (4.8) follows by subtraction from (4.5).  Finally, writing
\(k=n+s\), \(s=O(\log n)\), Stirling's formula gives

\[
 \log\frac{\binom{2n}{n+s-q}}{\binom{2n}{n+s}}
 =-\frac{q^2}{n}+\frac{2sq}{n}+o(1)
 =-A^2+o(1),
\]

which proves (4.7). \(\square\)

### Theorem 4.2 (linear provider failure in every contextual sector)

Put

\[
 q=\lfloor A\sqrt m\rfloor,\qquad A>0,
 \tag{4.9}
\]

and assume \(q\le r\), so that the packet factor is protected through
this depth.

\[
 f_*=\left\lfloor\mu_{n,k}-\frac{3q}{8}\right\rfloor.
 \tag{4.10}
\]

Uniformly over all anchor sectors,

\[
\begin{aligned}
 \frac{\sum_{f\le f_*}S_{k,f}}{\binom{2n}k}
     &\longrightarrow\Phi(-3A/2),\\
 \frac{\sum_{f\le f_*}T_{k-q,f}}{\binom{2n}{k-q}}
     &\longrightarrow\Phi(A/2).
\end{aligned}
 \tag{4.11}
\]

Consequently the contextual atlas of Theorem 3.1 satisfies

\[
 \boxed{
 M_q^-\ge(\delta_A-o(1))W,\qquad
 M_q^+\ge(\delta_A-o(1))W,}
 \tag{4.12}
\]

where

\[
 \boxed{
 \delta_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.}
 \tag{4.13}
\]

#### Proof

The threshold in (4.10) is \(3A/2+o(1)\) standard deviations below the
source mean.  By (4.8), it is \(A/2+o(1)\) standard deviations above the
target mean.  Lemma 4.1 gives (4.11).

All lower occurrences in the tail \(f\le f_*\) come from source owners in
the same tail, by (4.2).  One source occurrence covers at most one target.
Thus the missing lower targets in anchor sector \(x\) are at least

\[
 \sum_{f\le f_*}T_{k-q,f}
 -
 \sum_{f\le f_*}S_{k,f}
 -
 e^{-\Omega(m)}\binom{2n}k.
 \tag{4.14}
\]

Equations (4.7) and (4.11) turn (4.14) into

\[
 (\delta_A-o(1))\binom{2n}k.
\]

The constant is positive for every \(A>0\).  Indeed the elementary
Gaussian bound

\[
 \Phi(-z)\le\frac12e^{-z^2/2}\qquad(z\ge0)
\]

gives

\[
 \Phi(-3A/2)<\frac12e^{-A^2}
 <e^{-A^2}\Phi(A/2).
\]

Summing over \(x\) and using Vandermonde,

\[
 \sum_{x\in2^A}\binom{2n}{m-|x|}
 =\binom{2m}m=W,
\]

proves the lower assertion in (4.12).  Complement equivariance (3.11)
bijects lower and upper holes and proves the upper assertion.
\(\square\)

The proof allows arbitrary cycle orders and arbitrary correlations between
packet choices inside an anchor sector.  It uses only that the anchor is
trace-visible and fixes one matching within that sector.

## 5. Maximal staggered chart motion is gauge

We now show that positive-density contextual \(B_4\) motion is easy if the
successor permutation is not changed.

Let

\[
 X_t=K\cup\{z_t,z_{t+1},\ldots,z_{t+h-1}\},
 \qquad t\pmod{2h},
 \tag{5.1}
\]

be a physical \(C_{2h}\), with even \(h\ge4\).  Its edge at time \(t\) has
swap carrier

\[
 E_t=\{z_t,z_{t+h}\},\qquad E_{t+h}=E_t.
 \tag{5.2}
\]

The \(h\) distinct carriers form a cyclic list.  Define the two perfect
matchings of this carrier cycle by

\[
\begin{aligned}
 \mathcal Q^0&=\{\{E_{2i},E_{2i+1}\}:0\le i<h/2\},\\
 \mathcal Q^1&=\{\{E_{2i+1},E_{2i+2}\}:0\le i<h/2\},
\end{aligned}
 \tag{5.3}
\]

with indices modulo \(h\).

At vertex \(X_t\), use the frame

\[
                         \mathcal Q^{\,t-1\pmod2}.
 \tag{5.4}
\]

It groups the incoming carrier \(E_{t-1}\) with the outgoing carrier
\(E_t\).  The triple

\[
 X_{t-1}\longrightarrow X_t\longrightarrow X_{t+1}
\]

is therefore three consecutive middle vertices of the central \(B_4\)
square on \(E_{t-1}\cup E_t\).

### Proposition 5.1 (maximal complement-symmetric chart motion)

The frame in (5.4) changes every carrier's quartet partner at every step.
It is invariant under the half-turn \(t\mapsto t+h\).  Hence the atlas is
complement-symmetric on a complement-paired physical strip family.

#### Proof

The two matchings in (5.3) are the two disjoint alternating perfect
matchings of an even cycle.  Moving one step switches between them, so
every carrier changes partner.  Since \(h\) is even, \(t\) and \(t+h\)
have the same parity, proving half-turn invariance. \(\square\)

Let \(P\) be the physical successor.  The frames (5.3)--(5.4) do not alter
\(P\).  Therefore they do not alter any literal trace:

\[
 L_q(X)=\bigcap_{j=0}^qP^jX,\qquad
 U_q(X)=\bigcup_{j=0}^qP^jX.
 \tag{5.5}
\]

This is the exact frame-gauge obstruction.  The construction has maximal
chart-frame density and zero shadow effect.

Complementation gives a useful one-sign reduction.  If \(C(X)=V\setminus
X\), then

\[
\begin{aligned}
 CP=PC
 &\Longrightarrow U_q(CX)=C L_q(X),\\
 CPC=P^{-1}
 &\Longrightarrow U_q(CP^qX)=C L_q(X).
\end{aligned}
 \tag{5.6}
\]

Thus a complement-equivariant factor has isomorphic lower and upper
collision/provider systems.

## 6. Existential all-depth provider union does not compose

Let \(\mathcal U_H\) be the complete typed target-token universe through
depth \(H\), with signs fused by complementation.  A legal global state
\(\omega\) has literal support

\[
                         J^\omega\subseteq\mathcal U_H.
\]

For a finite legal state library \(Z\), define the provider set of a token
\(T\) by

\[
                         S_T=\{\omega\in Z:T\in J^\omega\}.
 \tag{6.1}
\]

Then the average number of holes is exactly

\[
 \boxed{
 \frac1{|Z|}\sum_{\omega\in Z}
       |\mathcal U_H\setminus J^\omega|
 =
 \sum_{T\in\mathcal U_H}
       \left(1-\frac{|S_T|}{|Z|}\right).}
 \tag{6.2}
\]

Thus mere provider union, \(S_T\ne\varnothing\) for every \(T\), has no
deterministic consequence.  The stronger averaged-density condition

\[
 \sum_T(|Z|-|S_T|)=o(W|Z|).
 \tag{6.3}
\]

is sufficient, by averaging, for the existence of an \(o(W)\)-hole
state.  It is not asserted to be necessary.

### Theorem 6.1 (maximally symmetric provider-union counterexample)

Let \(F\) be the complement-equivariant contextual factor of Theorem 3.1,
equipped with the staggered charts of Section 5, and take its
group-indexed coordinate-conjugacy library

\[
                         Z=(\sigma F:\sigma\in S_{2m}),
 \tag{6.4}
\]

Assume \(H\le r\).

This library has all of the following properties.

1. Every state is integral and owner-disjoint.
2. Every state has positive-density contextual \(B_4\) frames and exact
   complement symmetry.
3. Every prescribed complete two-sided nested literal \(H\)-flag occurs
   in at least one state.
4. If \(j_q\) is the number of distinct lower depth-\(q\) targets in one
   state, then every target of that rank has exactly

   \[
                         \frac{|S_{2m}|\,j_q}{N_q}
   \tag{6.5}
   \]

   provider indices, with repetitions from automorphisms retained.
5. For every fixed \(A>0\) with
   \(q=\lfloor A\sqrt m\rfloor\le r\), every state has

   \[
                         N_q-j_q\ge(\delta_A-o(1))W
   \tag{6.6}
   \]

   lower holes and the same number of upper holes.

#### Proof

Items 1--2 follow from Theorem 3.1 and Proposition 5.1 and are preserved
by conjugacy.  An \(H\)-safe row start determines an ordered partition of
the coordinates into

\[
 \begin{array}{c|c}
 \text{part}&\text{size}\\ \hline
 \text{persistent inside core}&m-H\\
 \text{ordered deletion queue}&H\\
 \text{ordered insertion queue}&H\\
 \text{persistent outside set}&m-H.
 \end{array}
 \tag{6.7}
\]

The symmetric group is transitive on all ordered data of these sizes.
Therefore the conjugacy orbit of any one protected row start contains
every prescribed complete two-sided nested \(H\)-flag, proving item 3.

For item 4, double-count pairs \((\sigma,T)\) with \(T\) a target in the
support of \(\sigma F\).  There are \(|S_{2m}|j_q\) such pairs.  Transitivity
on the target layer makes their number independent of \(T\), giving
(6.5).  Item 5 is Theorem 4.2 applied after conjugating its anchor and
matching. \(\square\)

This theorem refutes the implication from existential all-depth provider
union—even uniform provider density and full nested-flag union—to one
simultaneously good integral state.

Independent diffuse packet choices also cannot repair the quantifier.  If
independent fused groups cover target \(T\) with probabilities
\(p_{gT}\le\delta<1\), put

\[
 \lambda_T=\sum_gp_{gT}.
\]

Since

\[
 \log(1-p)\ge-\frac p{1-\delta}\qquad(0\le p\le\delta),
\]

\[
 \Pr(T\text{ is missed})
 =\prod_g(1-p_{gT})
 \ge\exp\left(-\frac{\lambda_T}{1-\delta}\right).
\]

Convexity and the occurrence budget
\(\sum_T\lambda_T\le W\) yield

\[
 \sum_T\Pr(T\text{ is missed})
 \ge
 N_q\exp\left(-\frac{W}{N_q(1-\delta)}\right).
 \tag{6.8}
\]

At \(q=A\sqrt m+O(1)\), this is

\[
 \left[
 e^{-A^2}
 \exp\left(-\frac{e^{A^2}}{1-\delta}\right)-o(1)
 \right]W.
 \tag{6.9}
\]

Success therefore needs near-deterministic homes or a globally correlated
integral Hall selection, not diffuse independent frame choices.

## 7. Exact cross-packet collision criterion

For a packet \(p\), let \(A_p\subseteq V\) be its active carrier, let
\(C_p\subseteq V\setminus A_p\) be its frozen exterior, and let

\[
 \mathcal L_{p,q}\subseteq2^{A_p}
\]

be its selected local lower trace family.  Its physical target image is

\[
 J_{p,q}=\{C_p\cup S:S\in\mathcal L_{p,q}\}.
 \tag{7.1}
\]

### Proposition 7.1 (packet fibre-product test)

For two packets \(p,r\), one has \(J_{p,q}\cap J_{r,q}\ne\varnothing\)
if and only if

1. \(C_p\) and \(C_r\) agree on \(V\setminus(A_p\cup A_r)\);
2. there are \(S\in\mathcal L_{p,q}\),
   \(S'\in\mathcal L_{r,q}\) such that

   \[
   \begin{aligned}
    S|_{A_p\setminus A_r}&=C_r|_{A_p\setminus A_r},\\
    S'|_{A_r\setminus A_p}&=C_p|_{A_r\setminus A_p},\\
    S|_{A_p\cap A_r}&=S'|_{A_p\cap A_r}.
   \end{aligned}
   \tag{7.2}
   \]

#### Proof

If \(T=C_p\cup S=C_r\cup S'\), restriction to the three disjoint regions
outside the overlap gives 1 and (7.2).  Conversely those agreements patch
to one set \(T\) with both representations. \(\square\)

Thus global trace injectivity is exactly intrapacket injectivity plus
emptiness of every cross-packet fibre product (7.2).  No frame marginal or
one-target provider count implies this.

If \(n_q\) selected starts emit depth-\(q\) targets with multiplicities
\(\mu(T)\), let

\[
 M_q=\sum_T(1-\mu(T))_+,\qquad
 C_q=\sum_T(\mu(T)-1)_+.
\]

Then the exact forced-baseline identity is

\[
                         M_q=C_q-(n_q-N_q).
 \tag{7.3}
\]

Indeed, sum \(\mu(T)-1\) separately over the positive and negative parts.
This is the floor correction which any proposed provider-union descent
must retain.

## 8. A recurrence-potential obstruction to genuine moving edges

Let \(P\) be a cycle factor of the complete middle layer
\(\binom Vm\).  Assume every component has length at least \(2q\).  Write
its cyclic transitions as

\[
 X_{t+1}=X_t-d_t+a_t,\qquad e_t=\{d_t,a_t\}.
 \tag{8.1}
\]

For every occurrence of a coordinate in some \(e_t\), join it to its next
cyclic occurrence on the same component.  The forward edge-position
distance is its **recurrence span**.  Let \(a_\ell\) be the number of
recurrence arcs of span \(\ell\), and put

\[
                         A_D=\sum_{\ell\le D}a_\ell.
 \tag{8.2}
\]

At depth \(q\), let \(B_q^-\) and \(B_q^+\) count starts whose intersection
and union, respectively, have ranks different from \(m-q\) and \(m+q\).
Let \(M_q^\pm\) be the numbers of missing targets in those two rank layers.

### Theorem 8.1 (recurrence-potential inequality)

\[
 \boxed{
 \sum_{\ell<q}(q-\ell)a_\ell
 \le
 4q(W-N_q)+2q(M_q^-+M_q^+).}
 \tag{8.3}
\]

Consequently, for \(D<q\),

\[
 \boxed{
 A_D\le
 \frac{4q}{q-D}(W-N_q)
 +\frac{2q}{q-D}(M_q^-+M_q^+).}
 \tag{8.4}
\]

#### Proof

A recurrence arc of span \(\ell<q\) has both endpoints in exactly
\(q-\ell\) cyclic \(q\)-edge windows.  In every such window a coordinate
occurs at least twice among the \(2q\) deletion/insertion events.  If both
the intersection and union had the correct ranks, the \(q\) deletions
would be distinct coordinates present at the start, the \(q\) insertions
would be distinct coordinates absent at the start, and the two lists
would be disjoint.  Thus at least one signed rank is wrong.

A fixed \(q\)-window contains at most \(2q\) recurrence-arc starts whose
next occurrence also lies in the window.  Double counting gives

\[
 \sum_{\ell<q}(q-\ell)a_\ell
 \le2q(B_q^-+B_q^+).
 \tag{8.5}
\]

There are \(W-B_q^\pm\) rank-valid occurrences of sign \(\pm\).  To cover
\(N_q-M_q^\pm\) distinct targets one needs

\[
 W-B_q^\pm\ge N_q-M_q^\pm,
\]

or

\[
 B_q^\pm\le W-N_q+M_q^\pm.
\]

Substitution into (8.5) proves (8.3).  Since every summand with
\(\ell\le D\) has weight at least \(q-D\), (8.4) follows. \(\square\)

The elementary product bound

\[
 \frac{N_q}{W}
 =\prod_{j=0}^{q-1}\frac{m-j}{m+j+1}
\]

gives

\[
 1-\frac{N_q}{W}
 \le\sum_{j=0}^{q-1}\frac{2j+1}{m+j+1}
 \le\frac{q^2}{m}.
 \tag{8.6}
\]

Taking \(q=2D\le H\) in (8.4) yields

\[
 \boxed{
 \frac{A_D}{W}
 \le\frac{32D^2}{m}
 +4\frac{M_{2D}^-+M_{2D}^+}{W}.}
 \tag{8.7}
\]

### Corollary 8.2 (bounded-router no-go)

Put \(q=2D\le H\), assume every component has length at least \(4D\),
and suppose

\[
 M_{2D}^-+M_{2D}^+=o(W),\qquad D=o(\sqrt m).
\]

Then

\[
                         A_D=o(W).
 \tag{8.8}
\]

Suppose, more specifically, that a family of genuine frame-change events
has an assignment to recurrence twists of span at most \(D\), with at
most \(K=O(1)\) events assigned to any one twist.  Then (8.8) rules out a
positive density of such events.  Under the sharper error hypothesis

\[
 M_{2D}^-+M_{2D}^+=o(W/\sqrt m)
 \tag{8.9}
\]

--in particular, under exact depth-\(2D\) coverage--the presence of
\(\Omega(W/\sqrt m)\) such events forces

\[
                         D=\Omega(m^{1/4}).
 \tag{8.10}
\]

Under the same bounded-multiplicity witness assignment, positive-density
motion with \(o(W)\) holes forces \(D=\Omega(\sqrt m)\).

A bounded-duration closed or restituting router, in which both the
partner change and its restitution occur inside one fixed chronological
block, has \(D=O(1)\) once its changes admit the bounded-multiplicity
witness assignment above.  A fixed seed whose restitution is delayed is
outside this corollary.  Complementation maps a witness twist to an
equal-span twist, possibly the same twist; in either case it cannot cancel
the nonnegative count \(A_D\).

### Corollary 8.3 (open-twist concurrency lower bound)

Fix \(\delta>0\), suppose a distinguished family contains at least
\(\delta W\) recurrence twists, and put

\[
                         D_0=\left\lfloor\frac{\sqrt{\delta m}}8\right\rfloor.
\]

Assume \(2D_0\le H\), every component has length at least \(4D_0\), and
there is exact signed target coverage at depth \(2D_0\).  Equation (8.7)
shows that at least \(\delta W/2\) distinguished twists have span greater
than \(D_0\).  Summing their interval lengths and averaging over the \(W\)
owner cuts gives at least

\[
 \left(\frac{\delta^{3/2}}{16}-o(1)\right)\sqrt m
 \tag{8.11}
\]

simultaneously open twist intervals at an average cut.  If every start is
\(H\)-safe, every recurrence span is at least \(H\), improving (8.11) to
\(\delta H\).

This is an exact open-concurrency obstruction, not merely an edge-count
obstruction.  It becomes a storage lower bound only for a router model
that assigns at least one distinct live state token to each simultaneously
open twist.

## 9. The four-child SCD profile gate

The same boundary can be stated directly inside a four-child product SCD.
Fix four disjoint child chains \(C_i(k_i)\), with
\(-r_i\le k_i\le r_i\), where increasing \(k_i\) moves one rank upward in
the child chain.  A parent middle state has profile

\[
                         k_1+k_2+k_3+k_4=0.
 \tag{9.1}
\]

Every internal Johnson edge is

\[
                         k\longmapsto k-e_i+e_j,
 \tag{9.2}
\]

using the next literal downward label of child \(i\) and upward label of
child \(j\).

### Proposition 9.1 (monotone-profile criterion)

A \(q\)-edge parent window is two-sided geodesic if and only if every
coordinate trajectory \(k_i(t)\) is monotone on that window.  In that
case its lower and upper child profiles are the componentwise minima and
maxima.

#### Proof

If a trajectory reverses direction, it traverses some edge of its child
chain in both directions, so the same physical child label occurs twice.
One of the two signed ranks is then wrong.  Conversely, a monotone child
trajectory traverses each of its chain edges at most once.  Different
children have disjoint coordinates, so all deletion/insertion labels are
distinct and both signed ranks are correct.  The intersection and union
take the lowest and highest visited child member, respectively. \(\square\)

Group children \(1,2\), put

\[
                         s=k_1+k_2,
\]

and let \(h^-\) be the number of downward steps taken in children \(1,2\)
inside a monotone \(q\)-window.  Its lower target has pair sum

\[
                         t=s-h^-.
 \tag{9.3}
\]

Thus every possible provider of a target in lower sector \(t\) starts in
one of the sectors

\[
                         s=t,t+1,\ldots,t+q.
 \tag{9.4}
\]

Not every displayed sector need be feasible for every target.  The point
is that solving trace injectivity separately inside each fixed
\(s\)-sector does
not give global provider union.  A successful moving-profile recursion
must select the transports \(h^-\) integrally and consistently across the
\(q+1\) overlapping sectors, simultaneously at every depth and under
complementation.  This is the exact cross-sector gate left after the
bounded \(B_4\) recursion is removed.

## 10. Audited boundary

The decisive implications were checked independently.

Proved:

1. every Johnson edge has \((m-1)^2\) contextual central-\(B_4\) charts;
2. full cubical \(B_4\) closure with every abstract two-face geodesic, and
   separately every complete isometric strand, force one fixed physical
   pair matching;
3. a complement-equivariant, bulk-projection-free contextual matching
   atlas covers \(1-e^{-\Omega(m)}\) of the middle owners;
4. its frozen context leaves
   \((\delta_A-o(1))W\) holes at each sign and every fixed Gaussian depth;
5. maximal staggered chart motion is complement-symmetric but leaves every
   trace unchanged;
6. even uniform full nested-flag provider union over a transitive state
   library does not yield one good state;
7. the exact fibre-product collision and floor-baseline identities;
8. the recurrence-potential and open-twist concurrency lower bounds; and
9. the exact cross-sector profile gate in a four-child SCD parent.

Not proved:

1. a no-go for path-only routers with \(\Omega(\sqrt m)\) temporal span;
2. a no-go for a growing exterior-moving packet mosaic whose frame state
   is itself erased within every Gaussian window;
3. the correlated integral configuration-Hall theorem for such a mosaic;
4. coefficient one.

Therefore bounded contextual moving-frame \(B_4\)/SCD constructions in
the three grammars named in Section 0 are closed, while the genuinely
growing exterior-moving route remains open.
