# The ternary-carry factor has a common-order shadow-Gram obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or generic
nibble theorem is used.

## 0. Verdict

Let

\[
 W=\binom{2m}{m},
 \qquad H=o(m),
 \qquad H\le t,
\]

We use the even SCI normalization.  In the odd convention
\(n=2m+1\), \(W=\binom{2m+1}{m}\), the common-order theorem below is
unchanged.  The two first-\(t\) densities differ from (0.1) by
\(O(1/m)\), which does not change any asymptotic conclusion.

Consider the phase-dense ternary-carry factor on the canonical
first-\(t\)-eligible macrocells \(\mathcal V^t\).  The middle factor,
ternary seam fusion, and cyclic \(H\)-geodesicity may all be granted exactly.
The labelled shadows nevertheless have a statewise support obstruction.

There is an order-free obstruction before the first-\(t\) quotient is even
used.  Let \(G=W-e^{-\Omega(m)}W\) be the good middle mass and let
\(\mathcal F_0\) be the static all-new-shore factor from which the carry
factor is obtained.  Since every \(Q_h\)-cell of \(\mathcal F_0\) has one
doubled direction order, its total depth-\(q\) physical support is at most

\[
                         {Gh\over2^q}.                \tag{0.0a}
\]

The carry construction changes exactly

\[
 E={3(1-3^{-t})\over4h}G                              \tag{0.0b}
\]

outgoing edges.  A changed edge can affect at most \(q\) starts at depth
\(q\).  Hence, for both signs,

\[
 \boxed{
 R_q^\pm:=\#\{S:r_q^\pm(S)>0\}
 \le {Gh\over2^q}+qE.}                               \tag{0.0c}
\]

At

\[
                         q_* =\lceil2\log_2h\rceil,   \tag{0.0d}
\]

the right side is \(O(W\log h/h)=o(W)\), while
\(N_{q_*}=(1-o(1))W\).  Thus, whenever \(q_*\le H\),

\[
 \boxed{M_{q_*}^-=(1-o(1))W,
        \qquad M_{q_*}^+=(1-o(1))W.}                 \tag{0.0e}
\]

This already kills the present factor and is invariant under arbitrary
permutations of the selected blocks inside their one-order cells.

There is also an independent canonical-quotient obstruction.  For its
statement, label the first \(t\) selected blocks in increasing physical
order, as in the monotone realization.

For either sign, if a depth-\(q\) target occurs, then its \(q\) touched
eight-blocks occupy a cyclic interval among the macrocell's ordered first
\(t\) eligible blocks.  Every target block already belonging to
\(\mathcal V\) is forced into that list.  It follows that at least
\(\lceil q/2\rceil\) touched, locally completable blocks lie in one gap
between consecutive \(\mathcal V\)-blocks of the target.

For a uniform target of rank \(m-q\) or \(m+q\), delete all block types
other than

* \(A\): a literal \(\mathcal V\)-block; and
* \(B^\pm\): a one-coordinate lower/upper completion of a
  \(\mathcal V\)-block.

Under the matching product measure before rank conditioning, the resulting
word is Bernoulli, with exact \(B\)-density

\[
 \boxed{
 \rho_q={5(m+q)\over 8m+2q}.}
 \tag{0.1}
\]

Consequently the reached fraction of either physical target layer is at
most

\[
 \boxed{
 C\sqrt m\,(t+1)\rho_q^{\lceil q/2\rceil}.}
 \tag{0.2}
\]

This bound is completely statewise: it holds for every syndrome translate,
every binary orbit label, every ternary digit vector, and every legal choice
of carry matchings.

Take

\[
                         q_m=\lceil20\log m\rceil.
 \tag{0.3}
\]

Here and below \(\log\) is natural.  Whenever \(q_m\le H\le t\le m/4\),
one has \(\rho_{q_m}\le2/3\), and the right side of (0.2) is \(o(1)\).
Moreover

\[
 \binom{2m}{m-q_m}=(1-o(1))W.
\]

Thus the ternary-carry factor has

\[
 \boxed{
 M_{q_m}^-= (1-o(1))W,
 \qquad
 M_{q_m}^+=(1-o(1))W.}
 \tag{0.4}
\]

In particular,

\[
 \sum_{q\le H}(M_q^-+M_q^+)\ne o(W).
\]

The base-three carry fuses components and changes the fine port code, but it
changes too few edges to repair the one-order support loss; in the monotone
realization it also leaves the ordered block-support word unchanged.  The
current ternary-carry factor does not prove SCI or coefficient one.

## 1. The local frame and its two one-step boundaries

In one labelled eight-block write

\[
 A_0=\{a,b,c,d\},\qquad A_1=\{u,v\},\qquad A_2=\{w,x\},
\]

and put

\[
 \mathcal V=
 \left\{V\subseteq A_0\dot\cup A_1\dot\cup A_2:
 (|V\cap A_0|,|V\cap A_1|,|V\cap A_2|)=(2,1,1)
 \right\}.
 \tag{1.1}
\]

Hence \(|\mathcal V|=\binom42\cdot2\cdot2=24\).

Define the physical one-step boundaries

\[
 \partial^-\mathcal V
 =\{R:|R|=3,\ R\subset V\text{ for some }V\in\mathcal V\},
 \tag{1.2}
\]

\[
 \partial^+\mathcal V
 =\{R:|R|=5,\ V\subset R\text{ for some }V\in\mathcal V\}.
 \tag{1.3}
\]

### Lemma 1.1 (exact local boundary sizes)

One has

\[
                         |\partial^-\mathcal V|
 =|\partial^+\mathcal V|=40.                         \tag{1.4}
\]

More precisely, the lower members have profiles

\[
 (1,1,1),\qquad(2,0,1),\qquad(2,1,0),                 \tag{1.5}
\]

in numbers \(16,12,12\), respectively.  A member of the first class has
three extensions in \(\mathcal V\), and a member of either other class has
two.

#### Proof

A three-set is extendible to (1.1) precisely when none of its three class
counts exceeds \((2,1,1)\).  Since its counts sum to three, the only
possibilities are (1.5).  Their numbers are

\[
 \binom41\binom21\binom21=16,
 \quad
 \binom42\binom20\binom21=12,
 \quad
 \binom42\binom21\binom20=12.
\]

The extension counts are immediate.  Complementation preserves
\(\mathcal V\) and exchanges (1.2) with (1.3), proving the upper count.
\(\square\)

## 2. Canonical macrocells and the exact carry-coordinate trace map

Partition all but at most seven ground coordinates into ordered blocks

\[
                         B_1<B_2<\cdots<B_s,
 \qquad s=\lfloor m/4\rfloor.
 \tag{2.1}
\]

For a middle owner \(X\), a block is eligible when
\(X\cap B_i\in\mathcal V\).  On the good owner set, let

\[
                         I(X)=(i_1<\cdots<i_t)
 \tag{2.2}
\]

be the first \(t\) eligible blocks and freeze the exterior

\[
                         E=X\cap\left([2m]\setminus
                                      \bigcup_{i\in I(X)}B_i\right).
 \tag{2.3}
\]

The macrocell is

\[
 \mathcal P(E,I)
 =\left\{E\cup V_1\cup\cdots\cup V_t:
                    V_r\in\mathcal V_{i_r}\right\}
 \cong\mathcal V^t.                                  \tag{2.4}
\]

Variation inside (2.4) preserves (2.2), so distinct macrocells are
owner-disjoint.

The ternary-carry normal form parametrizes the starts in one macrocell by

\[
 \mathscr U
 =\mathbb Z_2^t\times\mathbb Z_3^t\times K\times\mathbb Z_{4t},
 \qquad |K|={2^{2t}\over4t}.                          \tag{2.5}
\]

Indeed,

\[
 |\mathscr U|
 =2^t3^t{2^{2t}\over4t}(4t)=24^t.                    \tag{2.6}
\]

Write \(\Xi_{E,I}(u)\) for the physical middle owner represented by
\(u=(b,z,k,j)\), and write \(\Phi\) for the ternary-carry successor.
The carry rule makes \(z\) advance by one in base three after a complete
\(4t\)-step macroperiod, while the phase word has block-index sequence

\[
                         1,2,\ldots,t
 \quad\text{repeated four times}.                     \tag{2.7}
\]

For \(q\le t\), define the exact physical traces

\[
 \Lambda^-_{E,I,q}(u)
 =\bigcap_{r=0}^{q}\Xi_{E,I}(\Phi^ru),                \tag{2.8}
\]

\[
 \Lambda^+_{E,I,q}(u)
 =\bigcup_{r=0}^{q}\Xi_{E,I}(\Phi^ru).                \tag{2.9}
\]

The cyclic \(H\)-geodesicity theorem gives their ranks \(m-q\) and
\(m+q\).  Define the macrocell incidence vector

\[
 a_{E,I,q}^\epsilon(S)
 =\#\{u\in\mathscr U:\Lambda^\epsilon_{E,I,q}(u)=S\}.
 \tag{2.10}
\]

In general (2.10) is a multiplicity, not an indicator.  The proved local
edge injectivity and affine-face-to-target injectivity inside one fixed
product cell do not imply packetwise start-to-shadow injectivity after the
\(6^t\) cells and carry fibres are combined.  Indeed, Theorem 3A.3 below
forces large packetwise repetitions.

For the full macrocell atlas \(\mathfrak P\), the exact physical target
load is

\[
 \boxed{
 r_q^\epsilon(S)
 =\sum_{(E,I)\in\mathfrak P}a_{E,I,q}^\epsilon(S).}
 \tag{2.11}
\]

The exact physical Gram kernel is

\[
 \boxed{
 \begin{aligned}
 K_q^\epsilon((E,I),(E',I'))
 &=\langle a_{E,I,q}^\epsilon,a_{E',I',q}^\epsilon\rangle\\
 &=\sum_{u,v\in\mathscr U}
   {\bf1}_{\{\Lambda^\epsilon_{E,I,q}(u)
             =\Lambda^\epsilon_{E',I',q}(v)\}}.
 \end{aligned}}
 \tag{2.12}
\]

In particular,

\[
 \boxed{
 \sum_{P,P'\in\mathfrak P}K_q^\epsilon(P,P')
 =\sum_Sr_q^\epsilon(S)^2.}                           \tag{2.13}
\]

Equations (2.8)--(2.12) include the full binary orbit, syndrome, physical
row labels, ternary digits, and carry chronology.  We next factor out the
coarser support condition which every nonzero summand must satisfy.

## 3. Exact block-support factor of the load

For a physical target \(S\), define

\[
 \mathcal A(S)=\{i:S\cap B_i\in\mathcal V_i\},        \tag{3.1}
\]

\[
 \mathcal B^-(S)=\{i:S\cap B_i\in\partial^-\mathcal V_i\},
 \qquad
 \mathcal B^+(S)=\{i:S\cap B_i\in\partial^+\mathcal V_i\}.
 \tag{3.2}
\]

For \(I=(i_1<\cdots<i_t)\), let

\[
 D_I^\epsilon(S)
 =\{r\in[t]:i_r\in\mathcal B^\epsilon(S)\}.          \tag{3.3}
\]

Write

\[
 J_I^\epsilon(S)=\{i_r:r\in D_I^\epsilon(S)\},
 \qquad
 \operatorname {Ext}_I(S)
 =S\cap\left([2m]\setminus\bigcup_{i\in I}B_i\right).
 \tag{3.3a}
\]

Let \(\operatorname {CycInt}(t,q)\) be the \(t\) cyclic intervals of
length \(q\) in \(\mathbb Z_t\).

### Proposition 3.1 (exact load factorization)

For every macrocell \(P=(E,I)\), sign \(\epsilon\), and \(q\le t\),

\[
\begin{aligned}
 a_{P,q}^\epsilon(S)
 ={}&{\bf1}_{\{\operatorname {Ext}_I(S)=E\}}
     {\bf1}_{\{I\setminus J_I^\epsilon(S)\subseteq\mathcal A(S)\}}
     {\bf1}_{\{D_I^\epsilon(S)\in\operatorname {CycInt}(t,q)\}}
     \eta_{P,q}^\epsilon(S),                         \tag{3.4}
\end{aligned}
\]

where \(\eta_{P,q}^\epsilon(S)\in\mathbb Z_{\ge0}\) is precisely the
number of \(u=(b,z,k,j)\in\mathscr U\) satisfying
\(\Lambda_{P,q}^\epsilon(u)=S\).  It is the exact residual
syndrome/row/carry multiplicity.  Consequently
the pairwise Gram entry is exactly

\[
\begin{aligned}
 K_q^\epsilon(P,P')
 =\sum_S{}&
 {\bf1}_{\{\operatorname {Ext}_I(S)=E\}}
 {\bf1}_{\{\operatorname {Ext}_{I'}(S)=E'\}}\\
 &\cdot{\bf1}_{\{I\setminus J_I^\epsilon(S)\subseteq\mathcal A(S)\}}
 {\bf1}_{\{I'\setminus J_{I'}^\epsilon(S)\subseteq\mathcal A(S)\}}\\
 &\cdot{\bf1}_{\{D_I^\epsilon(S)\in\operatorname {CycInt}(t,q)\}}
 {\bf1}_{\{D_{I'}^\epsilon(S)\in\operatorname {CycInt}(t,q)\}}\\
 &\cdot\eta_{P,q}^\epsilon(S)\eta_{P',q}^\epsilon(S).
                                                               \tag{3.5}
\end{aligned}
\]

#### Proof

By (2.7), a \(q\)-step window touches \(q\) distinct selected blocks and
their positions in \(I\) form a cyclic interval.  In a lower trace, one
coordinate is deleted in every touched block; in an upper trace, one is
adjoined.  Thus touched restrictions belong to (1.2) or (1.3), while every
untouched selected restriction remains literally in \(\mathcal V\).  The
exterior is constant throughout the macrocell.  These are the first three
indicators in (3.4).  All finer restrictions are, by definition, the exact
multiplicity \(\eta\) from the carry-coordinate trace map.  This proves (3.4),
and substitution into (2.12) proves (3.5). \(\square\)

The important point is that the base-three carry occurs only in \(\eta\).
It can delete a coarse candidate but cannot create one that violates the
cyclic-interval indicator.

## 3A. The order-free common-order perturbation cut

The preceding kernel contains a simpler global support bound which does not
use the physical ordering of the selected blocks.

### Lemma 3A.1 (one-order cell support)

Let one physical \(Q_h\)-cell be factored into \(C_{2h}\)'s, all with one
doubled direction order \(\sigma\sigma\).  At either signed depth
\(q<h\), the factor reaches at most

\[
                         h2^{h-q}                     \tag{C.1}
\]

distinct physical targets.

#### Proof

A length-\(q\) window has one of the \(h\) cyclic \(q\)-intervals of
\(\sigma\) as its direction set.  For a fixed direction set, a lower trace
is determined by the choices on the remaining \(h-q\) active pairs, so
there are at most \(2^{h-q}\) traces.  The same statement holds above by
complementation inside the active cell.  Multiplication by the \(h\)
possible direction intervals proves (C.1). \(\square\)

The static all-new factor partitions the good owner set into \(G/2^h\)
physical \(Q_h\)-cells.  Summing (C.1), without assuming that different
cells have disjoint target images, gives

\[
 \boxed{
 |\operatorname {supp}r_{0,q}^\pm|
 \le {G\over2^h}h2^{h-q}={Gh\over2^q}.}              \tag{C.2}
\]

Here \(r_{0,q}\) denotes the static factor's load.  Notice that (C.2)
allows a different permutation \(\sigma\) in every cell.

### Lemma 3A.2 (sparse successor perturbations)

Let \(F_0,F\) be two successor permutations of the same finite owner set,
and put

\[
                         \Delta=\{x:F_0(x)\ne F(x)\}.
\]

If \(|\Delta|=E\), then at either sign and depth \(q\), all but at most
\(qE\) starting owners have the same \(q\)-trace under \(F_0\) and \(F\).
Consequently

\[
 |\operatorname {supp}r_{F,q}^\pm|
 \le |\operatorname {supp}r_{F_0,q}^\pm|+qE.         \tag{C.3}
\]

#### Proof

If

\[
 x,F_0x,\ldots,F_0^{q-1}x
\]

avoids \(\Delta\), induction gives \(F^jx=F_0^jx\) for
\(0\le j\le q\), so the two intersections and the two unions agree.
For each \(y\in\Delta\) and each \(0\le j<q\), the bijection \(F_0\)
has exactly one start \(x=F_0^{-j}y\).  Hence at most \(qE\) starts are
exceptional.  Every exceptional start creates at most one new target,
which proves (C.3). \(\square\)

### Theorem 3A.3 (the carry factor has logarithmic-depth linear holes)

For the ternary-carry successor \(F\) and its static all-new predecessor
\(F_0\), the exact changed-tail count is

\[
 \boxed{
 E={3(1-3^{-t})\over4h}G.}                            \tag{C.4}
\]

Therefore

\[
 \boxed{
 R_q^\pm\le {Gh\over2^q}
       +{3q(1-3^{-t})\over4h}G.}                     \tag{C.5}
\]

At \(q_*=\lceil2\log_2h\rceil\), provided \(q_*\le H\),

\[
 R_{q_*}^\pm
 \le {G\over h}+O\left({G\log h\over h}\right)
 =o(W).                                               \tag{C.6}
\]

Since \(h\le2m\), one has \(q_*=O(\log m)\), and hence

\[
                         N_{q_*}=(1-o(1))W.            \tag{C.7}
\]

It follows that \(M_{q_*}^\pm=(1-o(1))W\).
Moreover, the exact Gram identity (2.13) and Cauchy--Schwarz give

\[
 \boxed{
 \sum_{P,P'}K_{q_*}^\pm(P,P')
 \ge {G^2\over R_{q_*}^\pm}
 =\Omega\left({Wh\over\log h}\right).}               \tag{C.8}
\]

Thus the failure is a quantitatively coherent cross-macrocell collision
kernel.

There is also an exact macrocell multiplicity ledger.  Put

\[
 d_q^\pm(S)=\#\{P\in\mathfrak P:a_{P,q}^\pm(S)>0\}.
\]

Then (C.5), summed macrocell by macrocell, gives

\[
 \boxed{
 \sum_Sd_q^\pm(S)
 =\sum_P|\operatorname {supp}a_{P,q}^\pm|
 \le G\left(h2^{-q}
       +{3q(1-3^{-t})\over4h}\right).}               \tag{C.9}
\]

Since every retained owner contributes exactly one occurrence,

\[
 \boxed{
 \sum_{P,S}(a_{P,q}^\pm(S)-1)_+
 =G-\sum_Sd_q^\pm(S).}                               \tag{C.10}
\]

At \(q=q_*\), the right side of (C.10) is \((1-o(1))G\).  Thus almost
all occurrence mass is already duplicate mass within individual
macrocells.  Cross-macrocell coincidences can only reduce the global target
support further.

Even crediting accidental concatenation-boundary witnesses changes this by
only \(O(q_*C_{\rm comp})=o(W)\), because ternary fusion has
\(C_{\rm comp}=o(W/H)\) and \(q_*\le H\).  Crediting each of the
\(u=e^{-\Omega(m)}W\) omitted middle owners with an additional fresh target
also changes the support by only \(o(W)\).

#### Proof

In the base-three addition schedule, digit \(s\) triggers on the fraction
\(3^{-(s-1)}\) of row states.  Summing

\[
 \sum_{s=1}^t3^{-(s-1)}={3\over2}(1-3^{-t})
\]

over the one relevant port per digit and normalizing by the \(2h\) phase
positions gives the already certified exact tail count (C.4).  Apply
Lemma 3A.2 to (C.2) to obtain (C.5).  Since \(2^{q_*}\ge h^2\), (C.6)
follows.  Finally, the central-binomial product used in (6.4), with
\(q_*=O(\log m)\), proves (C.7).  Equation (C.8) is (2.13) followed by
Cauchy--Schwarz on the support of \(r_{q_*}^\pm\).  The boundary estimate
uses at most \(O(q_*)\) crossing windows per component.  Equation (C.9)
is the sum of (C.5) over macrocells.  Finally,
\(\sum_Sa_{P,q}^\pm(S)=|P|\) for each macrocell, so subtracting one from
every positive entry and summing proves (C.10). \(\square\)

This theorem is stronger than the monotone first-\(t\) cut below.  It uses
neither the first-eligible convention nor a common direction order across
different cells.  It uses only one order inside each static cell and the
fact that ternary fusion is an \(O(G/h)\)-edge perturbation of that factor.

## 4. The first-\(t\) interval lemma

Read the physical blocks from left to right and retain only the letters

\[
 A\quad(i\in\mathcal A(S)),
 \qquad
 B\quad(i\in\mathcal B^\epsilon(S)).                 \tag{4.1}
\]

All other block types are erased.  An \(A\)-letter is automatically
eligible in every middle completion of \(S\).  A \(B\)-letter becomes
eligible only if it is one of the touched blocks and its missing/excess
coordinate is completed.

### Lemma 4.1 (statewise long-gap cut)

If \(r_q^\epsilon(S)>0\), then among the first \(t+1\) gaps of
\(B\)-letters between consecutive \(A\)-letters in (4.1), some gap has
length at least

\[
                         \left\lceil{q\over2}\right\rceil.
 \tag{4.2}
\]

#### Proof

Choose an occurrence in a macrocell with ordered selected list
\(I=(i_1<\cdots<i_t)\), and mark a selected block by \(B\) when it is
touched and by \(A\) otherwise.  By Proposition 3.1 this cyclic selected
word has exactly \(q\) consecutive \(B\)'s and \(t-q\) \(A\)'s.

The selected list is the first \(t\) eligible list of the completed middle
owner.  Hence no \(A\)-block of the target can be skipped before the last
selected physical block.

If the cyclic \(B\)-interval does not cross the end of the selected word,
all its \(q\) blocks lie between two consecutive \(A\)-blocks of the
target.  That gap has length at least \(q\).

If it crosses the end, write it as a terminal run of length \(q-a\) and an
initial run of length \(a\).  The initial run lies before the first selected
\(A\); the terminal run lies after the last of the \(t-q\) selected
\(A\)'s and before the next \(A\).  One of these two gaps has length at
least \(\lceil q/2\rceil\).  Both are among the first \(t+1\) gaps.
\(\square\)

This lemma is statewise and precedes local port legality.  In particular it
is unchanged by the carry digits \(z\), syndrome translate \(k\), orbit
label \(b\), or phase-dependent shore matching.

## 5. Exact gap law in a physical target layer

First take a lower target from the product Bernoulli law with coordinate
density

\[
                         p_-={m-q\over2m}.
 \tag{5.1}
\]

On one block, Lemma 1.1 gives

\[
 \alpha_q=\Pr(A)=24p_-^4(1-p_-)^4,                   \tag{5.2}
\]

\[
 \beta_q^-=\Pr(B)=40p_-^3(1-p_-)^5.                 \tag{5.3}
\]

After erasing all other letters, the probability that the next retained
letter is \(B\) equals

\[
 {\beta_q^-\over\alpha_q+\beta_q^-}
 ={5(m+q)\over8m+2q}=\rho_q.                         \tag{5.4}
\]

For an upper target use

\[
                         p_+={m+q\over2m}.
\]

Then

\[
 \alpha_q=24p_+^4(1-p_+)^4,
 \qquad
 \beta_q^+=40p_+^5(1-p_+)^3,                         \tag{5.5}
\]

and the quotient \(\beta_q^+/(\alpha_q+\beta_q^+)\) is again exactly
\(\rho_q\).  Thus the same law holds for both signs.

In the erased word, a \(B\)-gap before the next \(A\) has geometric tail

\[
                         \Pr\{G\ge d\}=\rho_q^d.      \tag{5.6}
\]

The block laws are independent before conditioning on total target size.
The union bound and Lemma 4.1 therefore give

\[
 \Pr_p\{r_q^\epsilon(S)>0\}
 \le(t+1)\rho_q^{\lceil q/2\rceil}.                  \tag{5.7}
\]

The product law in (5.1) has mean exactly \(m-q\), and the one in (5.5)
has mean exactly \(m+q\).  Uniformly for \(q=o(m)\), Stirling's formula
gives

\[
 \Pr_p\{|S|=m\pm q\}\ge {c\over\sqrt m}.            \tag{5.8}
\]

Conditioning on this event produces the uniform physical target layer.
Dividing (5.7) by (5.8) proves the following theorem.

### Theorem 5.1 (physical support bound)

For either sign and every \(q\le t\) with \(q=o(m)\),

\[
 \boxed{
 {\#\{S\in\binom{[2m]}{m\pm q}:r_q^\pm(S)>0\}
  \over \binom{2m}{m-q}}
 \le C\sqrt m\,(t+1)\rho_q^{\lceil q/2\rceil}.}       \tag{5.9}
\]

Here the two signed layers have the same size
\(\binom{2m}{m-q}\), and \(C\) is absolute.

## 6. A logarithmic-depth linear hole theorem

Assume the phase-dense parameters

\[
                         q_m=\lceil20\log m\rceil
 \le H\le t\le m/4.                                  \tag{6.1}
\]

Because \(H=o(m)\), eventually \(q_m\le m/11\), and (0.1) gives

\[
                         \rho_{q_m}\le{2\over3}.      \tag{6.2}
\]

Thus (5.9) is at most

\[
 C m^{3/2}\left({2\over3}\right)^{10\log m}=o(1).   \tag{6.3}
\]

The exact central-binomial ratio is

\[
 {N_{q_m}\over W}
 =\prod_{j=0}^{q_m-1}{m-j\over m+j+1}
 =\exp\left(-{q_m^2\over m}+O(q_m/m+q_m^3/m^2)\right)
 =1-o(1).                                             \tag{6.4}
\]

Equations (5.9), (6.3), and (6.4) prove (0.4).

This remains true if one credits every accidental witness crossing a
concatenation boundary.  The fused construction has
\(C_{\rm comp}=o(W/H)\) components, and one boundary participates in at
most \(O(q_m)\) windows of length \(q_m+1\).  Hence all component boundaries
together add at most

\[
                         O(q_mC_{\rm comp})=o(W)
 \tag{6.4a}
\]

extra depth-\(q_m\) targets.  The exponentially small middle leave and its
singleton repairs contribute \(o(W)\) more.  Neither can repair the linear
deficit.

The same conclusion has a Gram formulation.  Let

\[
 R_q^\epsilon
 =\#\{S:r_q^\epsilon(S)>0\},
 \qquad
 G=\sum_Sr_q^\epsilon(S)=W-e^{-\Omega(m)}W.           \tag{6.5}
\]

By Cauchy--Schwarz and (2.13),

\[
 \boxed{
 \sum_{P,P'}K_q^\epsilon(P,P')
 =\sum_Sr_q^\epsilon(S)^2
 \ge {G^2\over R_q^\epsilon}.}                       \tag{6.6}
\]

At \(q=q_m\), Theorem 5.1 gives \(R_q^\epsilon=o(W)\), so the total
physical Gram mass is \(\omega(W)\).  Equivalently, the centered energy

\[
 \sum_S\left(r_q^\epsilon(S)-{G\over N_q}\right)^2
 =\sum_{P,P'}K_q^\epsilon(P,P')-{G^2\over N_q}       \tag{6.7}
\]

is \(\omega(W)\).  This is coherent cross-macrocell collision, not a
diagonal or seam error.

## 7. Consequence and exact escape

The SCI near-factor normal form requires both

\[
 \sum_X|r_0(X)-1|=o(W)
\]

and

\[
 \sum_{q\le H}(M_q^-+M_q^+)=o(W).
\]

The ternary-carry factor satisfies the first condition and has \(o(W)\)
seam, but Theorem 3A.3 gives a single depth with \((2-o(1))W\) signed
holes (and Section 6 gives an independent monotone-order proof).
It therefore fails the second condition.

The independent first-\(t\) obstruction uses exactly two structural facts:

1. a macrocell consists of the first \(t\) physically ordered eligible
   blocks; and
2. a shallow window touches a cyclic interval in that same order.

Changing port holonomy, the ternary carry schedule, binary orbit labels, or
syndrome translations preserves both facts.  A macrocell-dependent
permutation of the selected blocks can escape this monotone quotient cut,
but it does not escape Theorem 3A.3: every resulting cell still has only one
doubled direction order.

The exact remaining escapes from the stronger obstruction are therefore:

1. replace the static one-order \(Q_h\)-factor by a genuinely many-order
   factor whose depth-\(q_*\) physical support is \(\Theta(W)\);
2. replace the sparse carry by a dense perturbation changing
   \(\Omega(W/q_*)\) successor tails; or
3. construct nonlocal cross-cell traces not obtainable as a sparse
   perturbation of the static cell factor.

All three require a new factor theorem.  Reordering canonical blocks,
changing ternary digit priorities, or altering the seam concatenation is
insufficient.
