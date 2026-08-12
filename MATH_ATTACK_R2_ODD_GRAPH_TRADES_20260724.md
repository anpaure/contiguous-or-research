# Second-wave R: odd-graph trades and the first nonlocal partial Haar composite

Date: 2026-07-24

## 1. Verdict

Put

\[
n=2m+1.
\]

The requested all-\(m\) circuit **inside one exact wreath-factor fibre** is not proved.  The lane nevertheless reaches two sharp new conclusions, one positive and one negative.

1. For every

   \[
   \boxed{m\ge 510}
   \]

   there is a nonzero squarefree six-for-six partial wreath bitrade \(Z\) such that

   \[
   \boxed{B_mZ=B_{m-1}Z=0,\qquad B_{m-2}Z\ne0.}
   \]

   Both signs are genuine middle-wreath packings.  This is an all-sufficiently-large, packing-compatible depth-two Haar composite.  It is obtained from three independently dispersed universal two-for-two trades by a probabilistic argument with an explicit union bound.

   This theorem stops one logical step short of the requested exact-factor theorem: it does not prove that the negative partial packing is contained in any exact factor.  It is also a conformal sum of three legal trades on disjoint middle supports, not a connected Graver circuit.

2. No single common-core alternating cycle can give the missing exact-factor circuit.  More precisely, for \(m\ge3\), if \(F\) and \(F\triangle Z\) are both exact \(C_n\)-factors of the odd graph and \(Z\) is one clean common-core alternating cycle, then their first-shadow histograms are different.  Since every alternating \(C_8\) in the odd graph has the common-core normal form,

   \[
   \boxed{\text{no exact-wreath-preserving alternating }C_8
   \text{ is first-shadow neutral}.}
   \]

Thus the first exact depth-two circuit, if it exists in every dimension, must be genuinely nonlocal in two senses: it must couple several first-shadow cores, and its old side must be completed inside one exact factor.  A longer one-core cycle, a same-context eight-order identity, or a conformal packing of already legal local switches cannot supply a connected circuit.

The report also proves the exact signed filtration, an arbitrary-depth linear suspension, an exact transposition-component criterion, and several no-go theorems.  There is no signed-lattice obstruction.  The remaining obstruction is integral exact-factor completion and adaptive component geometry.

No web search, finite search, or certificate computation is used below.

## 2. Four levels which must not be conflated

Let \(\Omega_m\) be the unoriented cyclic orders of \([n]\).  For \(C\in\Omega_m\), let

\[
B_re_C=\sum_{I\in\mathcal W_r(C)}e_I
\]

be the incidence vector of its \(n\) cyclic intervals of length \(r\).  The every-other-position omitted-label convention is equivalent to the ordinary consecutive-interval convention because multiplication by two permutes \(\mathbb Z_n\).

There are four distinct notions.

1. A **signed middle relation** is an integral vector \(z\) with \(B_mz=0\).
2. A **support-feasible partial bitrade** is

   \[
   z=\mathbf1_P-\mathbf1_N,
   \]

   where \(P,N\) are middle-wreath packings and \(B_m\mathbf1_P=B_m\mathbf1_N\).
3. Such a bitrade is **exact-factor realizable** when there is a common residual packing \(H\) such that

   \[
   H\mathbin{\dot\cup}N,\qquad H\mathbin{\dot\cup}P
   \]

   are exact factors.
4. An exact-factor move is a **connected circuit** when its middle-ownership overlay is connected.  These are the conformally indecomposable, squarefree Graver moves of the exact fibre.

The positive theorem in Section 7 reaches level 2.  The assigned target asks for level 3, and the word “circuit” naturally asks for level 4.  Nothing below promotes the partial theorem past these distinctions.

## 3. The colored-cycle deck formulation

Let one wreath be written in ordinary interval order as

\[
A_j=I_C(j,m),\qquad j\in\mathbb Z_n.
\]

The \(A_j\)'s form the natural point-regular \(C_n\) in the Johnson graph.  Color its edge \(A_{j-1}A_j\) by

\[
S_j=A_{j-1}\cap A_j=I_C(j,m-1).
\]

For every \(h\in\{1,\ldots,m-1\}\),

\[
\boxed{
I_C(j,m-h)
=S_{j-h+1}\cap\cdots\cap S_j
=A_{j-h}\cap\cdots\cap A_j.
}
\tag{3.1}
\]

Consequently the depth-\(h\) shadow \(B_{m-h}F\) of an exact wreath factor is exactly the histogram of intersections of \(h\) consecutive edge colors over its derived Johnson cycles.

Conversely, no relaxation is hidden here.  In a point-regular Johnson \(n\)-cycle, the cyclic membership word of each coordinate has exactly \(m\) ones and hence at least one \(1\to0\) transition.  Every Johnson edge has exactly one departing coordinate, so there are \(n\) departure transitions in total.  There are also \(n\) coordinates, forcing exactly one departure, and hence exactly one entry, for each coordinate.  Each coordinate therefore occupies one cyclic run of \(m\) vertices.  Ordering the coordinates by their departure positions reconstructs the cyclic order whose middle windows are the given cycle.

The second-wave target is therefore a colored-cycle deck trade:

> rebundle the middle vertices into point-regular Johnson \(n\)-cycles so that the \(h\)-block intersection decks agree for \(1\le h<q\), while the \(q\)-block deck changes.

This formulation is lossless.  It also explains why a seam argument is delicate.  A cut-and-splice changes only blocks crossing a seam, but every seam affects up to \(h-1\) starts at depth \(h\), and the same splicing must remain a collection of point-regular length-\(n\) cycles.

### 3.1 Centered first-shadow colors

For an odd-graph factor \(F\), let \(Y_F(X),Z_F(X)\) be the two factor neighbors of a middle vertex \(X\), and define

\[
\gamma_F(X)=Y_F(X)\cap Z_F(X).
\tag{3.2}
\]

Over each wreath, the values of \(\gamma_F\) are exactly its rank-\((m-1)\) cyclic intervals, up to a cyclic shift.  Hence the histogram of \(\gamma_F\) is \(B_{m-1}F\).

There is pointwise rigidity.  If \(\gamma_F(X)=S\), then

\[
X^c\setminus S=\{a,b\},
\]

and necessarily

\[
\boxed{
\{Y_F(X),Z_F(X)\}=\{S\cup\{a\},S\cup\{b\}\}.
}
\tag{3.3}
\]

Thus \(\gamma_F=\gamma_G\) pointwise implies \(F=G\).  The unlabelled equality

\[
B_{m-1}F=B_{m-1}G
\]

is much weaker: it permits the colors to be reassigned among centers.

This centered labeling is not the common-owner map \(L_1(X)\subset X\) in labelled synchronization.  On an oriented wreath it is a shifted occurrence of that shadow, and the shift depends on the factor orientation.  Pointwise rigidity of \(\gamma\) must therefore not be advertised as a no-go theorem for SYNC.

## 4. There is no signed-lattice obstruction

Let \(U_r\) be the point-versus-\(r\)-set incidence matrix.  For

\[
1\le q\le m-1,
\]

define

\[
\mathcal K^{(q)}=ker_{\mathbb Z}B_m
\cap\bigcap_{s=m-q+1}^{m-1}\ker_{\mathbb Z}B_s.
\tag{4.1}
\]

The empty intersection is understood when \(q=1\).

### Theorem 4.1 — exact integral shallow filtration

For \(1\le q\le m-2\),

\[
\boxed{
B_{m-q}:\mathcal K^{(q)}\twoheadrightarrow
\ker_{\mathbb Z}U_{m-q},
}
\tag{4.2}
\]

and

\[
\boxed{
\ker\bigl(B_{m-q}|_{\mathcal K^{(q)}}\bigr)
=\mathcal K^{(q+1)}.
}
\tag{4.3}
\]

Consequently

\[
\boxed{
\mathcal K^{(q)}/\mathcal K^{(q+1)}
\cong\ker_{\mathbb Z}U_{m-q},
}
\tag{4.4}
\]

a free abelian group of rank

\[
\boxed{
\binom{2m+1}{m-q}-(2m+1).
}
\tag{4.5}
\]

The short exact sequence splits noncanonically.

#### Proof

For any signed middle relation \(z\), summing the rows of \(B_mz=0\) gives \(\sum_Cz_C=0\).  Every coordinate occurs in exactly \(r\) cyclic \(r\)-intervals of one order, so

\[
U_rB_rz=r\left(\sum_Cz_C\right)\mathbf1=0.
\]

Thus the image in (4.2) lies in \(\ker_{\mathbb Z}U_{m-q}\).

The latter lattice is generated integrally by the octahedral rectangles

\[
e_{Kac}-e_{Kbc}-e_{Kad}+e_{Kbd}.
\]

Every such rectangle has a coefficient-one Petr–Turek lift which vanishes at the middle rank and at every lower rank other than the selected one.  Summing those lifts proves surjectivity while staying in \(\mathcal K^{(q)}\).  The kernel statement is exactly the definition of the next filtration term.  Since \(\ker_{\mathbb Z}U_{m-q}\) is primitive and free, the quotient is free and the sequence splits.  The point-incidence matrix has rank \(n\) in the present range, giving (4.5).  The construction survives projection from oriented to unoriented orders.  ∎

Thus pure-depth signed vectors exist for every admissible \(m,q\).  Any obstruction to the assigned theorem is a packing, exact-completion, or connectedness obstruction.

## 5. Universal legal two-for-two trades

Assume \(m\ge3\).

Fix distinct labels \(\alpha,\beta,\gamma,\delta\).  Let \(E\) and \(O\) be ordered lists of the remaining labels of lengths

\[
|E|=m-1,\qquad |O|=m-2.
\]

In ordinary cyclic-interval readout, put

\[
\begin{aligned}
C  &=(\delta,\gamma,E,\beta,\alpha,O),\\
D  &=(\beta,\delta,E,\alpha,\gamma,O),\\
C' &=(\delta,\beta,E,\gamma,\alpha,O),\\
D' &=(\gamma,\delta,E,\alpha,\beta,O),
\end{aligned}
\tag{5.1}
\]

and

\[
z(E,O)=e_{C'}+e_{D'}-e_C-e_D.
\tag{5.2}
\]

For a set \(H\) avoiding \(\beta,\gamma\), write

\[
\partial H=e_{H\cup\{\gamma\}}-e_{H\cup\{\beta\}}.
\tag{5.3}
\]

### Lemma 5.1 — universal support feasibility

For every ordering of \(E,O\), both \(\{C,D\}\) and \(\{C',D'\}\) are middle-wreath packings and

\[
\boxed{B_m(C+D)=B_m(C'+D').}
\tag{5.4}
\]

Hence every \(z(E,O)\) is a legal partial two-for-two trade.

#### Proof

For completeness, suppress the common \(E/O\) core of each middle window.  The four boundary classes in the universal cut table have the following exceptional-label multisets on the old and new diagonals:

\[
\begin{array}{c|c|c}
\text{window class}&C,D&C',D'\\ \hline
\text{first exceptional-pair boundary}
 &\{\delta\gamma,\beta\delta\}
 &\{\delta\beta,\gamma\delta\}\\
\text{all-}E\text{ boundary singletons}
 &\{\gamma,\beta,\delta,\alpha\}
 &\{\beta,\gamma,\delta,\alpha\}\\
\text{second exceptional-pair boundary}
 &\{\beta\alpha,\alpha\gamma\}
 &\{\gamma\alpha,\alpha\beta\}\\
\text{all-}O\text{ boundary pairs}
 &\binom{\{\alpha,\beta,\gamma,\delta\}}2
 &\binom{\{\alpha,\beta,\gamma,\delta\}}2.
\end{array}
\]

Thus the two diagonal unions have identical middle incidence, proving (5.4).  It remains to audit internal disjointness, since equality of signed incidence alone would not prove it.

For a word

\[
Q=(a_1,a_2,E,b_1,b_2,O),
\]

the pair \((I\cap E,I\cap O)\) of a middle interval determines its start, except for the two intervals containing all of \(E\) and the three containing all of \(O\).  Every other interval uses a uniquely determined proper prefix or suffix of each ordered list; two distinct proper prefixes and suffixes of a list of distinct labels cannot agree as sets.

For \(C\), the two all-\(E\) additions are \(\gamma,\beta\); for \(D\), they are \(\delta,\alpha\).  The three all-\(O\) added pairs are respectively

\[
\{\alpha\beta,\alpha\delta,\delta\gamma\}
\quad\text{and}\quad
\{\alpha\gamma,\beta\gamma,\beta\delta\}.
\]

These are the complementary triples of edges of the \(K_4\) on the exceptional labels.  The mixed boundary additions also differ: they use \(\delta\gamma\) versus \(\beta\delta\), or \(\alpha\beta\) versus \(\alpha\gamma\), with the ordered-list part already determining the boundary.  Therefore \(C,D\) share no middle interval.

The left side of (5.4) is consequently a \(0/1\) vector on \(2n\) targets.  Equality forces the right side to be the same \(0/1\) vector, so \(C',D'\) are disjoint as well.

The two signs have no common column.  Let \(\tau=(\beta\ \gamma)\), so \(C'=\tau C\) and \(D'=\tau D\).  Every cyclic order has a middle interval fixed by \(\tau\): the total number of incidences of \(\beta,\gamma\) among its \(n\) middle intervals is \(2m=n-1\), so not every interval contains exactly one of them.  A single transposition cannot stabilize an unoriented odd cyclic order, since a nontrivial rotation fixes no label and a reflection has cycle type \(1\,2^m\).  If \(\tau C=D\) or \(\tau D=C\), the fixed middle interval would be common to \(C,D\), contradicting their disjointness.  Thus (5.2) really is a squarefree two-for-two trade.  ∎

### Lemma 5.2 — exact all-rank action

For \(2\le r\le m-1\), with \(\ell=r-1\),

\[
\boxed{
B_rz(E,O)=
\partial\operatorname{suf}_{\ell}(O)
+\partial\operatorname{suf}_{\ell}(E)
-\partial\operatorname{pre}_{\ell}(E)
-\partial\operatorname{pre}_{\ell}(O).
}
\tag{5.5}
\]

Moreover

\[
B_1z(E,O)=B_mz(E,O)=0.
\tag{5.6}
\]

#### Proof

In the step-two word, the four exceptional positions form two adjacent pairs.  A rank-\(r\) window with \(r<m\) cannot meet both pairs.  Windows meeting neither pair, or both positions of one pair, cancel between the four terms.  The four windows containing exactly one exceptional position have the four cores in (5.5), with the indicated signs.  At rank one the four copies cancel, while the middle cut table gives (5.6).  ∎

If

\[
E=(u,K,v),\qquad |K|=m-3,
\]

then (5.5) gives the elementary first-shadow rectangle

\[
\boxed{
B_{m-1}z(E,O)=\partial(K\cup\{v\})-\partial(K\cup\{u\}).
}
\tag{5.7}
\]

## 6. The natural formal alternating eight-switch fails exactly

Fix \(2\le q\le m-2\).  Let

\[
O=(o_0,\ldots,o_{m-3})
\]

and let \(O'\) be obtained by swapping \(o_{q-2}\) and \(o_{q-1}\), with \(E\) unchanged.  Put

\[
w_q=z(E,O)-z(E,O').
\tag{6.1}
\]

### Proposition 6.1 — formal depth isolation

If

\[
\boxed{m\ge2q,}
\]

then

\[
\boxed{
B_mw_q=B_{m-1}w_q=\cdots=B_{m-q+1}w_q=0,
\qquad B_{m-q}w_q\ne0.
}
\tag{6.2}
\]

For \(m>2q\), putting

\[
R=\{o_q,\ldots,o_{m-3}\},
\]

the surviving part is

\[
\partial(R\cup\{o_{q-1}\})-
\partial(R\cup\{o_{q-2}\}).
\tag{6.3}
\]

At the boundary \(m=2q\), write

\[
O=(P,a,b,S),\qquad |P|=|S|=q-2.
\]

Then the surviving image is

\[
\boxed{
\partial(bS)-\partial(aS)-\partial(Pa)+\partial(Pb),
}
\tag{6.4}
\]

which is nonzero; for \(q=2\) it is \(2(\partial b-\partial a)\).

#### Proof

At depth \(j\), formula (5.5) sees only the first and last \(j-1\) entries of \(O\).  For \(j<q\), the swap is on neither boundary, provided \(m\ge2q\).  At \(j=q\), the first boundary separates \(a,b\), giving (6.3); when \(m=2q\), the last boundary separates them as well and gives (6.4).  The displayed cores are distinct, so the image is nonzero.  If \(q+2\le m<2q\), the last boundary changes already at depth \(m-q<q\), so the claimed filtration is false there.  ∎

This is the most economical formal alternating eight-order construction.  Its literal four-versus-four presentation has an exact packing obstruction.

### Theorem 6.2 — same-\(E\) two-mask obstruction in the literal presentation

Let \(T,T'\) be contexts with the same underlying \(E\)-set and the same four exceptional labels.  In the unreduced four-positive/four-negative presentation of

\[
z_T-z_{T'}
\]

neither sign is a middle packing.

#### Proof

On its positive side, the two orders

\[
C'_T=(\delta,\beta,E_T,\gamma,\alpha,O_T),
\qquad
C_{T'}=(\delta,\gamma,E_{T'},\beta,\alpha,O_{T'})
\]

both contain the middle masks

\[
E\cup\{\beta\},\qquad E\cup\{\gamma\}.
\]

Likewise \(D'_T,D_{T'}\) share

\[
E\cup\{\delta\},\qquad E\cup\{\alpha\}.
\]

The negative presentation has the analogous collisions between \(C_T,C'_{T'}\) and between \(D_T,D'_{T'}\).  Internal permutations of \(E\) or \(O\) do not change these four set equalities.  ∎

Thus every same-first-rectangle difference of these universal lifts has literal same-sign middle collisions.  The theorem is deliberately about the eight displayed columns.  If a special choice creates opposite-sign column identities, the vector must first be reduced; this lemma alone does not classify every such exceptional reduction.  The randomized construction below avoids the issue by proving all twelve of its columns distinct.

## 7. A packing-compatible depth-two partial bitrade for all large \(m\)

The same-context obstruction can be escaped by dispersing the three rectangle contexts independently.

### Theorem 7.1 — probabilistic nonlocal partial Haar trade

For every

\[
\boxed{m\ge510,}
\]

there is a nonzero squarefree support-feasible six-for-six partial bitrade \(Z\) satisfying

\[
\boxed{
B_mZ=B_{m-1}Z=0,\qquad B_{m-2}Z\ne0.
}
\tag{7.1}
\]

#### Construction

Put

\[
k=m-3.
\]

Partition the ground set as

\[
[n]=\{\beta,\gamma,x,y,z\}
\mathbin{\dot\cup}K
\mathbin{\dot\cup}Q_0,
\tag{7.2}
\]

where

\[
|K|=k,\qquad |Q_0|=m-1.
\]

For each ordered endpoint pair

\[
uv\in\{xy,yz,xz\},
\]

let \(w\) be the unused member of \(\{x,y,z\}\), and put

\[
Q_{uv}=Q_0\cup\{w\}.
\]

Independently for the three contexts, choose

1. a uniform ordering \(K_{uv}\) of \(K\); and
2. a uniform full ordering of \(Q_{uv}\), whose first two entries are called \(\delta_{uv},\alpha_{uv}\), with the remaining ordered list called \(O_{uv}\).

Set

\[
E_{uv}=(u,K_{uv},v)
\]

and let \(z_{uv}=z(E_{uv},O_{uv})\), using the common axes \(\beta,\gamma\) and the context-dependent \(\alpha_{uv},\delta_{uv}\).  Define

\[
\boxed{Z=z_{xy}+z_{yz}-z_{xz}.}
\tag{7.3}
\]

Every \(z_{uv}\) is individually a legal two-for-two trade by Lemma 5.1.  Formula (5.7) gives

\[
B_{m-1}z_{uv}
=\partial(K\cup\{v\})-
\partial(K\cup\{u\}).
\]

Therefore

\[
B_{m-1}Z=0
\]

by telescoping around \(x\to y\to z\), and \(B_mZ=0\) termwise.

#### Packing probability

In every one of the twelve cyclic orders appearing in the six-order-per-sign presentation, the labels of \(K\) form one consecutive block of length \(k\).  For a middle interval, let \(a\) be the number of its \(K\)-positions.  The exact number \(N_a\) of middle intervals of one order with that value is

\[
\boxed{
N_0=5,\qquad N_k=4,\qquad N_a=2\quad(1\le a\le k-1).
}
\tag{7.4}
\]

Indeed, the complement of the \(K\)-block has length \(m+4\), giving five windows avoiding \(K\); a length-\(m\) window containing all \(k=m-3\) positions has four placements; every proper nonempty intersection enters from one of the two block boundaries.

Call the two ordinary word templates in one selected diagonal \(C\)-type and \(D\)-type.  Across both global signs and across different contexts, there are exactly

\[
6\ C/C\text{ pairs},\qquad
12\ C/D\text{ pairs},\qquad
6\ D/D\text{ pairs}.
\tag{7.5}
\]

For \(1\le a\le k-1\), expose one context first.  In the other context, the required \(a\)-subset of \(K\) and the required subset of its \(Q\)-pool are unique if they exist.  Every such interior window uses a nonempty proper \(Q\)-subset.  Hence one prescribed pair of windows has probability at most

\[
\binom ka^{-1}\binom m{b}^{-1}
\le \frac1m\binom ka^{-1},
\]

where \(b\) is the number of randomized \(Q\)-positions on the side exposed second.  Reversing the exposure when necessary handles the fact that \(x,y,z\) change between fixed and randomized roles.  Summing the four window pairs for each \(a\), and then all twenty-four order pairs, gives

\[
24\cdot\frac4m
\sum_{a=1}^{k-1}\binom ka^{-1}
<\frac{384}{mk}.
\tag{7.6}
\]

Here

\[
\sum_{a=1}^{k-1}\binom ka^{-1}<\frac4k:
\]

the two endpoint terms contribute \(2/k\), while each of the remaining \(k-3\) terms is at most \(\binom k2^{-1}\).

At \(a=0\), the five windows of a \(C\)-type order omit respectively

\[
0,1,1,2,2
\]

labels from its \(m\)-element \(Q\)-pool; for a \(D\)-type order the deficits are

\[
1,1,2,2,2.
\]

Full-\(Q\) windows from different contexts are the distinct sets \(Q_{uv}\).  For every other pair, expose a side with a nonempty proper \(Q\)-subset second.  The resulting bounds for one order pair are

\[
\begin{array}{c|c}
\text{type}&a=0\text{ contribution}\\ \hline
C/C&8/m+16/\binom m2\\
C/D&6/m+19/\binom m2\\
D/D&4/m+21/\binom m2.
\end{array}
\tag{7.7}
\]

At \(a=k\), the four windows of a \(C\)-type order use

\[
0,0,1,1
\]

randomized \(Q\)-labels, while all four windows of a \(D\)-type order use one.  The zero-\(Q\) additions on either global sign are precisely

\[
\{\beta,u,v\},\qquad\{\gamma,u,v\},
\qquad uv\in\{xy,yz,xz\},
\]

and these six sets are distinct.  One-sided exposure of every remaining pair gives

\[
\begin{array}{c|c}
\text{type}&a=k\text{ contribution}\\ \hline
C/C&12/m\\
C/D&16/m\\
D/D&16/m.
\end{array}
\tag{7.8}
\]

Multiplying (7.7)--(7.8) by the pair counts (7.5), and adding (7.6), gives the exact audited union bound

\[
\boxed{
\Pr(\text{at least one sign is not a middle packing})
\le
\frac{504}{m}
+\frac{450}{\binom m2}
+\frac{384}{m(m-3)}.
}
\tag{7.9}
\]

The two orders within one context need no probability estimate: they are already disjoint by Lemma 5.1.

#### The next shadow survives

Let \(A_{uv}\) and \(B_{uv}\) be the first and last entries of the random ordering \(K_{uv}\).  At rank \(m-2\), formula (5.5) shows that the two \(E\)-cores are

\[
\partial\bigl((K\setminus\{A_{uv}\})\cup\{v\}\bigr),
\qquad
-\partial\bigl((K\setminus\{B_{uv}\})\cup\{u\}\bigr).
\tag{7.10}
\]

In \(B_{m-2}Z\), the only \(E\)-cores whose outside endpoint is \(y\) are

\[
+\partial\bigl((K\setminus\{A_{xy}\})\cup\{y\}\bigr)
\]

and

\[
-\partial\bigl((K\setminus\{B_{yz}\})\cup\{y\}\bigr).
\]

Every \(O\)-core contains no \(K\)-label, whereas these cores contain \(k-1\) of them.  The other \(E\)-cores carry outside endpoint \(x\) or \(z\).  Finally, the vectors \(\partial H\), over distinct cores avoiding \(\beta,\gamma\), are linearly independent: their two-point supports \(\{H\cup\{\gamma\},H\cup\{\beta\}\}\) are pairwise disjoint.  Therefore

\[
B_{m-2}Z=0
\quad\Longrightarrow\quad
A_{xy}=B_{yz}.
\]

The two entries are independent and uniform in \(K\), so

\[
\boxed{
\Pr(B_{m-2}Z=0)\le\frac1k.
}
\tag{7.11}
\]

No independence from the packing event is needed.  For \(m\ge510\),

\[
\frac{450}{\binom m2}\le\frac2m,
\qquad
\frac{384}{m(m-3)}\le\frac1m,
\qquad
\frac1{m-3}\le\frac2m.
\]

By (7.9), (7.11), and the union bound, the total bad probability is therefore at most

\[
\frac{504+2+1+2}{m}=\frac{509}{m}<1.
\tag{7.12}
\]

Choose one successful outcome.  Its twelve columns are all distinct.  Within one context, a positive column is the \((\beta\ \gamma)\)-image of a negative one.  A transposition cannot stabilize an unoriented odd cyclic order, and if it carried one old column to the other old column, those two columns would share a transposition-fixed middle interval, contradicting Lemma 5.1.

Across two contexts, the \(K\)-labels form one intrinsic maximal consecutive block in every column, and its unordered pair of cyclic boundary labels is exactly \(\{u,v\}\).  The three endpoint pairs \(xy,yz,xz\) are different, so columns from different contexts cannot coincide even after rotation or reversal.  Thus the successful outcome is genuinely six-for-six and squarefree, and (7.1) holds.  ∎

### 7.1 Why independent dispersion is essential

If the three rectangle lifts share one common filler \(H\), one common exceptional pair \(\alpha,\delta\), and the naive endpoint tails

\[
E_{uv}=(u,K,v),\qquad O_{uv}=(w,H),
\]

then every sign orientation of the three-edge telescope has a middle collision.

On either selected diagonal of one universal trade, one order has initial exceptional pair \(\{\beta,\delta\}\), and one has \(\{\gamma,\delta\}\).  For either such pair \(A\), the order contains both masks

\[
H\cup\{s\}\cup A,\qquad H\cup\{w\}\cup A,
\]

where \(s\) is its first \(E\)-endpoint and \(w\) is the unused member of \(\{x,y,z\}\).  Thus each lifted edge supplies a two-subset \(\{s,w\}\) of a three-set.  Any two such two-subsets meet, giving the same-sign common mask.  Randomizing the long contexts in Theorem 7.1 is not cosmetic; it removes this exact obstruction.

## 8. Why the positive theorem is not yet an exact-factor circuit

Theorem 7.1 gives two partial middle packings \(N,P\) with the same middle union.  It would become an exact-factor theorem if one could prove the existence of a residual packing \(H\) with

\[
\boxed{
B_m\mathbf1_H=\mathbf1-B_m\mathbf1_N.
}
\tag{8.1}
\]

Then the same \(H\) would complete \(P\), because \(B_m\mathbf1_P=B_m\mathbf1_N\).  No theorem in the current framework says that an arbitrary fixed-size partial wreath packing extends to an exact factor, and the probabilistic construction does not correlate its six old rows with a known exact factor.

The exact missing completion statement can be isolated without ambiguity:

> **Specific six-row extension lemma — unproved.**  For every sufficiently large \(m\), at least one successful outcome in the probability space of Theorem 7.1 has its negative side contained in an exact middle wreath factor.

This is weaker than asserting that every six-wreath packing extends.  It is exactly enough for an exact depth-two factor pair.

There is also a connectedness obstruction.

### Proposition 8.1 — conformal legal sums cannot become one circuit

Let

\[
z_i=\mathbf1_{P_i}-\mathbf1_{N_i}
\]

be nonzero support-feasible trades.  Suppose

\[
Z=\sum_i z_i
\]

is conformal, with every \(P_i\) on the positive sign and every \(N_i\) on the negative sign, and suppose \(Z\) itself is support feasible.  Then the middle-support sets

\[
M_i=B_m\mathbf1_{P_i}=B_m\mathbf1_{N_i}
\]

are pairwise disjoint.

#### Proof

If \(M_i\cap M_j\ne\varnothing\), a middle target in the intersection is covered by one order of \(P_i\) and one order of \(P_j\), contradicting that the global positive side is a packing.  ∎

Therefore the ownership overlay of \(Z\) is the disjoint union of the overlays of the \(z_i\).  Theorem 7.1 is a conformal sum of three nonzero trade overlays on pairwise disjoint middle supports, so it has at least three connected components whose first-shadow effects cancel globally.  It is not a connected Graver circuit.  A genuine connected circuit cannot be obtained merely by placing already legal local trades conformally side by side; it must arise as one nonlocal ownership component or use cancellations among individually infeasible signed cells.

## 9. No one-core alternating cycle can be first-shadow neutral

We now return to actual exact odd-graph factors.

Let \(F\) be an exact \(C_n\)-factor of \(O_m=KG(n,m)\).  Consider a simple clean \(F\)-alternating cycle

\[
Z=A_0C_0A_1C_1\cdots A_{k-1}C_{k-1}A_0
\tag{9.1}
\]

in the common-core normal form

\[
A_i=K\cup\{u_i\},
\qquad
C_i=B\setminus\{u_i,u_{i+1}\},
\tag{9.2}
\]

where

\[
|K|=m-1,\qquad B=[n]\setminus K,
\]

and the \(u_i\)'s are distinct.  Indices are cyclic.  Take \(A_iC_i\) as the removed factor edge and \(C_iA_{i+1}\) as the added edge.

Let \(r_i\) be the omitted label on the untouched factor edge at \(A_i\), and \(s_i\) the omitted label on the untouched factor edge at \(C_i\).  Cleanliness gives

\[
r_i\in B\setminus\{u_{i-1},u_i,u_{i+1}\},
\qquad
s_i\in K.
\tag{9.3}
\]

The old and new centered first-shadow colors are

\[
\begin{array}{c|c|c}
\text{center}&\text{old color}&\text{new color}\\ \hline
A_i&B\setminus\{u_i,u_{i+1},r_i\}
   &B\setminus\{u_{i-1},u_i,r_i\}\\[1mm]
C_i&(K\setminus\{s_i\})\cup\{u_i\}
   &(K\setminus\{s_i\})\cup\{u_{i+1}\}.
\end{array}
\tag{9.4}
\]

### Theorem 9.1 — common-core exact-factor no-go

Assume \(m\ge3\), \(k\ge3\), and both

\[
F,\qquad F'=F\triangle Z
\]

are exact wreath factors.  Then

\[
\boxed{B_{m-1}F'\ne B_{m-1}F.}
\tag{9.5}
\]

#### Proof

Suppose the histograms were equal.  The colors at the \(A_i\)'s lie wholly in \(B\).  Every color at a \(C_i\) contains \(m-2\ge1\) elements of \(K\).  Thus the two sectors in (9.4) cannot cancel each other, and the old and new \(C\)-sector multisets must agree separately.

Each \(C\)-sector color uniquely records the pair \((s,u)\): it has the single \(B\)-label \(u\) and omits the single \(K\)-label \(s\).  Matching the unique occurrence with \(B\)-label \(u_i\) on the two sides gives

\[
s_i=s_{i-1}
\]

for every \(i\).  Hence all \(s_i\) equal one label \(s\in K\).

The \(k\) untouched factor edges at the vertices \(C_i\) are distinct.  Indeed, for \(i\ne j\),

\[
|C_i\cap C_j|\ge |B|-4=m-2>0,
\]

so two such edges cannot be the same edge with endpoints exchanged.  All \(k\) edges have omitted label \(s\).

In any length-\(n\) odd-graph cycle, every omitted edge label occurs exactly once.  To see this without choosing a cyclic-order representation, let \(k_a\) count edges omitting label \(a\), and let \(d_a\) count cycle vertices containing \(a\).  Counting incidences of \(a\) at edge endpoints gives

\[
2d_a=n-k_a.
\]

Thus every \(k_a\) is a positive odd integer.  Since \(\sum_a k_a=n\) over the \(n\) labels, all \(k_a=1\).  Therefore the \(k\) distinct label-\(s\) edges above lie in \(k\) distinct old wreaths.  If \(r\) is the number of old components touched by \(Z\), then

\[
r\ge k.
\tag{9.6}
\]

Deleting the \(k\) old edges leaves \(k\) residual paths.  Let \(s'\) be the number of new components after reconnection.  Contract each residual path to one edge.  The connected alternating cycle remains connected after this contraction; its old and new monochromatic edge-components are exactly the old and new touched cycles.  Hence the bipartite incidence graph whose vertices are those cycles and whose edges are the residual paths is connected.  Therefore

\[
r+s'\le k+1.
\tag{9.7}
\]

Both factorizations consist of length-\(n\) cycles on the same touched vertex set, so

\[
r=s'.
\]

Equations (9.6)--(9.7) give

\[
2k\le2r=r+s'\le k+1,
\]

impossible for \(k\ge2\).  ∎

### Lemma 9.2 — every odd-graph \(C_8\) has a common-core parity

In every simple \(C_8\) of \(KG(2m+1,m)\), one of its two parity classes has the form

\[
K\cup\{u_0\},\ K\cup\{u_1\},\ K\cup\{u_2\},\ K\cup\{u_3\}
\]

with \(|K|=m-1\) and four distinct \(u_i\).

#### Proof

Write the two parity classes as \(A_i,C_i\).  The two consecutive sets \(A_i,A_{i+1}\) are distinct \(m\)-subsets of the \((m+1)\)-set \(C_i^c\), so they meet in \(m-1\) points.  Hence the \(A_i\)'s form a simple four-cycle in the Johnson graph.

The four upper unions \(A_i\cup A_{i+1}\) are also distinct, because their complements are the four distinct vertices \(C_i\).  This removes the chorded Johnson four-walks which would repeat a \(C_i\).

Compare the opposite vertices \(A_0,A_2\).  If their Johnson distance is one, write them as \(K\cup\{a\}\) and \(K\cup\{c\}\).  A common Johnson neighbor which does not contain \(K\) has the form

\[
(K\setminus\{x\})\cup\{a,c\}.
\]

Using it as \(A_1\) would give

\[
A_0\cup A_1=A_1\cup A_2=K\cup\{a,c\},
\]

and hence repeat a \(C\)-vertex.  Thus both \(A_1,A_3\) contain \(K\), so all four \(A_i\)'s have the desired common core.

If \(A_0,A_2\) have Johnson distance two, write

\[
A_0=L\cup\{a,c\},\qquad A_2=L\cup\{b,d\},
\]

where \(|L|=m-2\).  Their common Johnson neighbors choose one label from each displayed pair.  Unless \(A_1,A_3\) are the two opposite choices, two consecutive upper unions coincide.  Distinctness of the \(C_i\)'s therefore forces, after relabeling, the cyclic list

\[
Lac,\quad Lbc,\quad Lbd,\quad Lad.
\]

In the second case

\[
C_i=[n]\setminus(A_i\cup A_{i+1}).
\]

All four \(C_i\)'s therefore contain the common set

\[
[n]\setminus(L\cup\{a,b,c,d\}),
\]

whose size is \(m-1\), and each adds one distinct member of \(\{a,b,c,d\}\).  Thus the other parity class has the required form.  ∎

After swapping the two parity classes if necessary, every simple alternating \(C_8\) therefore has (9.2) with \(k=4\).  Consequently:

### Corollary 9.3 — no depth-two alternating \(C_8\)

For every \(m\ge3\), no single alternating \(C_8\) can take one exact wreath factor to another while preserving \(B_{m-1}\).  In particular, no depth-\(q\) exact circuit with \(q\ge2\) is one balanced two-wreath eight-switch.

This is the sharp obstruction to the targeted shortest eight-switch.  It does not rule out several alternating cycles whose first-shadow effects cancel across different cores.

### 9.1 Cross-core locality

Every changed first-shadow color in a common-core switch with core \(K\) belongs to

\[
\Sigma(K)=
\left\{
T\in\binom{[n]}{m-1}:
|T\cap K|\in\{0,m-2\}
\right\}.
\tag{9.8}
\]

If

\[
\Sigma(K)\cap\Sigma(K')\ne\varnothing,
\]

then

\[
\boxed{
|K\cap K'|\le1
\quad\text{or}\quad
|K\cap K'|\ge m-4.
}
\tag{9.9}
\]

Indeed, if a common target is a Johnson neighbor of both cores, their intersection is at least \(m-3\).  If it is disjoint from both, their union fits in a set of size \(m+2\), giving intersection at least \(m-4\).  If it is a neighbor of one core and disjoint from the other, only the one deleted core label can lie in the other core, giving intersection at most one.

Thus multi-core first-shadow cancellation can pass tokens only between very close cores or near-disjoint cores.  Cores with

\[
2\le|K\cap K'|\le m-5
\]

have disjoint first-shadow support and cannot cancel each other.

## 10. A second architecture obstruction: two-seam derived-cycle splicing

This section concerns the derived Johnson cycles of Section 3, not paths in the original odd-graph cycle.

Let \(P=(A_0,\ldots,A_{\ell-1})\) be \(\ell\) consecutive middle windows of one ordinary cyclic order, with \(1\le\ell\le m\).  Let

\[
d_P(x)=|\{i:x\in A_i\}|
\]

be its coordinate-load vector.

### Lemma 10.1 — central-overlap reconstruction

The vector \(d_P\) determines the central middle vertex when \(\ell\) is odd, and the unordered pair of central middle vertices when \(\ell\) is even.

#### Proof

The \(m-\ell+1\) coordinates common to all windows have load \(\ell\).  For every \(t=1,\ldots,\ell-1\), exactly two boundary coordinates have load \(t\): one leaves after \(t\) windows and one enters for the last \(t\) windows.

If \(\ell=2h+1\), the central window consists of the full-load core together with both coordinates in every load pair with \(t\ge h+1\).  If \(\ell=2h\), the two central windows have the common core formed by the full-load coordinates and all pairs with \(t\ge h+1\), and differ by the two coordinates in the load-\(h\) pair.  ∎

Hence two equal-load segments of the same length at most \(m\) necessarily share a central middle vertex.

### Corollary 10.2 — no two-cycle, two-seam cross-splice

Two disjoint old wreaths cannot be cut twice in their derived Johnson orders and cross-spliced into two new point-regular wreaths.

#### Proof

Let the old cycles be \(P_1P_2\) and \(Q_1Q_2\), and suppose the proposed new cycles are \(P_1Q_2\) and \(Q_1P_2\).  Length \(n\) of all four cycles gives \(|P_1|=|Q_1|\).  Point regularity of the old and new cycles gives

\[
d_{P_1}=d_{Q_1}.
\]

Choose the shorter complementary pair, so their common length is at most \(m\).  Lemma 10.1 forces a common middle vertex, contradicting disjointness of the two old wreaths.  ∎

This rules out the simplest color-preserving two-seam architecture.  It is not a statement about a \(22\)-cut shape in the original odd-graph order; the two cyclic orders have different step sizes, and that distinction is essential.

## 11. Exact transposition-component criterion

Let \(F\) be an exact factor and let \(\tau=(u\ v)\) be a coordinate transposition.  Form the ownership overlay between \(F\) and \(\tau F\).

Every cyclic order \(C\) has a middle interval fixed as a set by \(\tau\).  Indeed, \(u,v\) have a total of \(2m=n-1\) incidences among the \(n\) middle intervals.  If every interval contained exactly one of them, the total would be \(n\).  Thus some interval contains both or neither.  It joins the left row \(C\) to the right row \(\tau C\) in the overlay.

Consequently, for every overlay component \(K\), its right row set is exactly the \(\tau\)-image of its left row set.  Let \(L\) be any union of left component sides.  Then

\[
z_L=\mathbf1_{\tau L}-\mathbf1_L
\tag{11.1}
\]

is a legal exact-factor move, and

\[
\boxed{
B_rz_L=(\tau-I)B_r\mathbf1_L.
}
\tag{11.2}
\]

### Theorem 11.1 — exact component-subset test

Fix \(1\le q\le m-1\).

The move \(z_L\) preserves the first \(q-1\) shadows if and only if, for every \(1\le j<q\), every \((m-j-1)\)-set \(R\) avoiding \(u,v\),

\[
\boxed{
\mu_{L,m-j}(R\cup\{u\})
=\mu_{L,m-j}(R\cup\{v\}).
}
\tag{11.3}
\]

It changes depth \(q\) if and only if (11.3) fails for at least one \(R\) at rank \(m-q\).

#### Proof

Equation (11.2) says that preservation at rank \(r\) is exactly \(\tau\)-invariance of the partial histogram of \(L\).  Targets containing both or neither of \(u,v\) are fixed.  Every nontrivial \(\tau\)-orbit is the displayed pair, so (11.3) is necessary and sufficient.  ∎

This is a complete criterion for the transposition-cube route.  The signed surjectivity theorem by itself supplies no \(0/1\) union of ownership components satisfying these equations.  In the fixed MSW \((2\ 3)\)-cube, the proved first-shadow pivots are linearly independent, so the only first-shadow-neutral component selection is empty.  Any route starting from that fixed cube and using those local components must first leave it and recompute; this is not a theorem about every factor or transposition.

## 12. Exact linear suspension at arbitrary depth

There is an all-dimensional signed suspension, but its natural integral realization is not a packing.

Start with an oriented cyclic order \(C\) on \(n=2m+1\) labels.  Add new labels \(x,y\).  For each gap \(i\in\mathbb Z_n\), insert \(x\) in gap \(i\) and \(y\) in gap \(i+m\); call the result \(E_iC\).  Define

\[
P_me_C=\sum_{i\in\mathbb Z_n}e_{E_iC}.
\tag{12.1}
\]

For

\[
h_m(\ell)=(\ell-m)_++(\ell-(m+1))_+,
\]

a direct gap count gives, for \(3\le r\le m+1\), a new rank-\(r\) target \(T\), and \(t=|T\cap\{x,y\}|\),

\[
(B_rP_me_C)_T=
\begin{cases}
h_m(n-r+1)\,\mathbf1\{T\text{ is an old }r\text{-interval}\},&t=0,\\
(r-h_m(r-1))\,\mathbf1\{T\setminus\{x\}\text{ is an old }(r-1)\text{-interval}\},&T\cap\{x,y\}=\{x\},\\
(r-h_m(r-1))\,\mathbf1\{T\setminus\{y\}\text{ is an old }(r-1)\text{-interval}\},&T\cap\{x,y\}=\{y\},\\
h_m(r-1)\,\mathbf1\{T\setminus\{x,y\}\text{ is an old }(r-2)\text{-interval}\},&t=2,
\end{cases}
\tag{12.2}
\]

### Theorem 12.1 — depth-preserving suspension

Let \(2\le q\le m-2\).  If

\[
B_mz=B_{m-1}z=\cdots=B_{m-q+1}z=0,
\qquad B_{m-q}z\ne0,
\tag{12.3}
\]

then on \(2m+3\) labels

\[
\boxed{
B_{m+1}P_mz=B_mP_mz=\cdots=B_{m-q+2}P_mz=0,
}
\tag{12.4}
\]

while

\[
\boxed{
B_{m-q+1}P_mz
=(m+1-q)(\iota_x+\iota_y)B_{m-q}z\ne0.
}
\tag{12.5}
\]

Here \(\iota_x\) adjoins \(x\) to every target.

#### Proof

At new depth \(j\), put \(r=m+1-j\).  Then

\[
h_m(n-r+1)=h_m(m+1+j)=2j+1,
\qquad
h_m(r-1)=h_m(m-j)=0.
\]

Thus the no-new sector uses old rank \(m+1-j\), and each one-new sector uses old rank \(m-j\) with coefficient \(m+1-j\); the both-new sector vanishes.  For \(j<q\), both old rows vanish by (12.3), using complementation of \(B_m\) when \(j=0\).  At \(j=q\), the no-new row is \(B_{m-q+1}z=0\), while the one-new rows give (12.5).  ∎

Iteration gives signed pure-depth vectors in every larger dimension.  It does not give factor trades.

### 12.1 Integral suspension obstruction

For one old order \(C\), any two distinct antipodal pointings \(E_iC,E_jC\) share a new middle interval.  For a fixed old middle interval \(A\), the pointing phases which expose \(A\cup\{x\}\) form one cyclic block of \(m+1\) residues, and those which expose \(A\cup\{y\}\) form another cyclic block of \(m+1\); the blocks meet in their unique boundary phase and cover all \(n\) residues.  Any two residues of a \((2m+1)\)-cycle lie in some translate of an \((m+1)\)-block.  Rotating the start of \(A\) supplies that translate, so the two pointed extensions contain a common one-new middle target.  Therefore the \(n\) extensions in \(P_me_C\) cannot lie on one sign of a partial factor.

More generally, call a multiset \(D\subseteq\mathbb Z_n\) of pointing offsets **phase oblivious** if the complete new-middle incidence signature it assigns to an old interval is independent of that interval's cyclic start.  In this signature, the no-new target complementary to the old interval is attained at one unique boundary offset.  At start phase \(s\), its multiplicity is therefore one translate \(\operatorname{mult}_D(s-c)\).  Phase independence forces this number to be constant in \(s\), so every residue occurs in \(D\) with the same multiplicity.  A nonempty phase-oblivious gadget uses all \(n\) pointings and is incompatible with packing.

Thus the clean linear suspension has no phase-oblivious, one-wreath-at-a-time integral refinement.  An arbitrary owner-mixing refinement is not ruled out.

### 12.2 Common-context metric obstruction

Let \(d_\circ(C,D)\) be cyclic adjacent-swap distance.  One adjacent swap changes at most two middle intervals, so

\[
|\mathcal W_m(C)\cap\mathcal W_m(D)|
\ge n-2d_\circ(C,D).
\tag{12.6}
\]

Hence two distinct orders on one sign of a partial factor satisfy

\[
\boxed{d_\circ(C,D)\ge m+1.}
\tag{12.7}
\]

Now consider any proposed lift \(C,D\mapsto\Phi_t(C),\Phi_t(D)\) from dimension \(m_0\) to \(m_0+t\) for which one has the explicit distance bound

\[
d_\circ(\Phi_t(C),\Phi_t(D))
\le d_\circ(C,D)+e_t.
\]

Combining this with (12.7), packing requires

\[
\boxed{
e_t\ge m_0+t+1-d_\circ(C,D).
}
\tag{12.8}
\]

A literal common prefix/suffix lift has \(e_t=0\) whenever the chosen old adjacent-swap path preserves the marked insertion gap; such a fixed-cut lift therefore fails in all sufficiently large dimensions.  A common inserted block need not preserve the *minimum* cyclic distance if every shortest path crosses that gap, so (12.8), rather than an unconditional distance equality, is the precise statement.  Every successful recursive suspension must either create linearly growing order-dependent dispersion or leave this bounded-distance architecture.

## 13. Exact remaining theorem

The lane leaves two nested targets.

### Target A — exact completion of the partial depth-two composite

Prove the specific extension lemma (8.1) for at least one successful dispersed triangle from Theorem 7.1.  This would give, for every sufficiently large \(m\), two exact factors \(F,G\) with

\[
B_mF=B_mG=\mathbf1,
\qquad
B_{m-1}F=B_{m-1}G,
\qquad
B_{m-2}F\ne B_{m-2}G.
\]

It would necessarily retain at least three mutually disconnected changed ownership blocks: Proposition 8.1 makes their middle supports disjoint, and adding one common residual completion cannot create overlay edges between them.  It would nevertheless be a valid exact-factor endpoint trade.

### Target B — connected adaptive component splitting

One viable architecture for a genuine nonlocal circuit is to start from one exact factor, perform preparatory component switches, recompute the next ownership components after every switch, and create one final component \(L\) satisfying the exact invariance equations (11.3) at all shallower ranks but not at the desired rank.  The finite commutator model uses at least two transpositions, but no theorem here says that every possible construction must do so.

The following routes are now rigorously excluded:

1. one Petr–Turek square or the standard parity cube generated by pairwise disjoint adjacent swaps;
2. the literal unreduced same-\(E\) alternating eight-order presentation;
3. the common-\(H\), common-\(\{\alpha,\delta\}\), naive endpoint telescope of Section 7.1;
4. a conformal packing of legal local trades as one connected circuit;
5. one common-core alternating cycle, in particular one balanced \(C_8\);
6. a two-cycle, two-seam splice in the derived Johnson order;
7. an orderwise phase-equivariant antipodal suspension;
8. a literal common prefix/suffix lift with bounded order-dependent motion; and
9. a first-shadow-neutral selection from the fixed MSW local component hierarchy.

The following are **not** ruled out:

1. completion of the partial dispersed triangle inside one exact factor;
2. cancellation among several close or near-disjoint first-shadow cores;
3. a longer overlay with several alternating cycles and changing cores;
4. an adaptive sequence whose components are recomputed after every switch; or
5. a new direct construction of two exact factors with identical shallow decks.

## 14. Audit ledger and implication scope

The decisive statements were independently rederived with the following checks.

1. The universal four-letter words were converted from step-two to ordinary cyclic order, and every exceptional middle-window class was checked symbolically.  This validates individual two-for-two legality.
2. The formal depth-\(q\) range is \(m\ge2q\), including the separate boundary formula at \(m=2q\).  The weaker inequality \(m>2q\) is unnecessary; for \(m<2q\), an earlier last-boundary leakage really occurs.
3. The randomized proof was audited against the fact that \(x,y,z\) switch between fixed and randomized roles.  The proof uses one-sided exposure separately for each window pair; it does not assume a common \(Q\)-count across contexts.
4. The \(6,12,6\) cross-context \(C/C,C/D,D/D\) pair counts, the collision bound

   \[
   \frac{504}{m}+\frac{450}{\binom m2}+\frac{384}{m(m-3)},
   \]

   and the next-shadow failure probability \(1/(m-3)\) were independently recomputed.  Their sum is at most \(509/m<1\) for the stated \(m\ge510\).
5. The sign telescope is

   \[
   z_{xy}+z_{yz}-z_{xz},
   \]

   and its only possible cancellation of the displayed \(y\)-endpoint witness requires equality of two independent boundary labels.
6. The common-core no-go uses the \(C_i\)-sector alone, the one-use-per-label law inside a wreath, and the connected residual-path incidence graph.  Its contradiction is \(2k\le k+1\).
7. The endpoint pair adjacent to the intrinsic \(K\)-block recovers the context, so the twelve successful columns are distinct and the trade is exactly six-for-six.  It is not proved extendible, exact-factor realizable, conformally indecomposable, or all-\(m\).

Accordingly this report proves neither MWB nor labelled synchronization.  Even a completed depth-two circuit would be a local structural advance, not a fixed-Gaussian balancing theorem.  The frozen implication scope remains unchanged: unlabelled shallow-histogram trades do not supply a common-owner nested coupling.

## Final conclusion

The algebraic part of Second-wave R is solved: pure-depth directions exist integrally and suspend to every larger dimension.  The first packing-compatible depth-two composite also exists for every \(m\ge510\).  What fails is precisely the step demanded by the frozen logic—placing its old side inside one exact factor—and a conformal sum of legal pieces can never become one connected circuit.

At the exact-factor level the targeted eight-switch is ruled out: no alternating \(C_8\), and more generally no one-core alternating cycle, can preserve the first shadow.  A successful all-dimensional theorem must be multi-core and exact-factor realizable.  Adaptive recomputation is one viable mechanism, but a direct construction of two shallow-deck-equivalent exact factors remains explicitly unruled out.
