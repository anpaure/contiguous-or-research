# The pair-cell transversal lift extends to an exact owner/lower factor

**Date:** 2026-08-13  
**Status:** unconditional asymptotic incidence theorem.  The long-run
transversal lift has exponential size, but its two protected shore exposures
are exactly at most two.  The sharp protected-Ore localization therefore
still embeds the whole lift in a spanning middle-levels two-factor.  The
completion supplied here is not asserted to be resident, upper-surjective, or
connected.

## 1. Setting

Put

\[
 n=2r-1,\qquad
 \mathcal L={{[n]}\choose {r-1}},\qquad
 \mathcal U={{[n]}\choose r},\qquad
 W=|\mathcal L|=|\mathcal U|.                         \tag{1.1}
\]

Write \(p=r-1\), distinguish a coordinate \(z\), and partition the other
\(2p\) coordinates into pairs \(P_i=\{a_i,b_i\}\).  For
\(x\in\{0,1\}^p\), let

\[
 L_x=\{a_i:x_i=0\}\cup\{b_i:x_i=1\}.                \tag{1.2}
\]

Fix any cyclic Hamilton Gray code

\[
 x_0,x_1,\ldots,x_{2^p-1},x_{2^p}=x_0               \tag{1.3}
\]

of \(Q_p\), and let \(d_t\) be the direction of \(x_tx_{t+1}\).  Define

\[
 D_t=L_{x_t}\cup L_{x_{t+1}}.                        \tag{1.4}
\]

The transversal-lift theorem gives a simple Johnson cycle on the owners
\((D_t)\), with

\[
 D_{t-1}\cap D_t=L_{x_t}.                             \tag{1.5}
\]

Let \(P\) be its alternating incidence lift in the bipartite graph
\(G=(\mathcal L,\mathcal U;\subset)\).  Thus its protected lower and owner
shores are

\[
 Z=\{L_x:x\in\{0,1\}^p\},\qquad
 Y=\{D_t:0\le t<2^p\},                               \tag{1.6}
\]

and \(P\) is one cycle with

\[
 |Z|=|Y|=2^p=2^{r-1},\qquad |E(P)|=2^r.              \tag{1.7}
\]

## 2. Exact exposure

### Lemma 2.1

The all-occurrence shore exposures of \(P\) satisfy

\[
 \max_{L\in\mathcal L}|N(L)\cap Y|\le2,
 \qquad
 \max_{U\in\mathcal U}|N(U)\cap Z|\le2.             \tag{2.1}
\]

#### Proof

Every member of \(Y\) omits \(z\), is double on exactly one matched pair,
and is singleton on all other pairs.

If \(L\in\mathcal L\) contains \(z\), it lies below no member of \(Y\).  If
\(z\notin L\), then a member of \(Y\) containing \(L\) can occur only in
one of two cases.  When \(L\) is a transversal, the possible selected
owners are exactly the two Hamilton-cycle edges incident with its cube
vertex.  When \(L\) has one double and one empty pair, the only possible
owners are obtained by filling one of the two coordinates of that empty
pair.  All other occupancy profiles have no such owner.  This proves the
first inequality.

For the second inequality, an owner containing \(z\) contains at most the
one transversal obtained by deleting \(z\).  An owner omitting \(z\)
contains a transversal facet only when it has exactly one double pair and
no empty pair, in which case deleting either endpoint of its double pair
gives the only two.  Hence the maximum is two.  \(\square\)

For a protected incidence bank, write 

\[
 \lambda_P(A)=
 \sum_{U\in\mathcal U}
 \bigl(\min\{2,a_U\}-\min\{2-p_U,a_U\}\bigr),        \tag{2.2}
\]

where \(a_U=|N(U)\cap A|\) and
\(p_U=e_P(U,\mathcal L\setminus A)\).  Also put

\[
 \sigma(A)=\sum_U\min\{2,a_U\}-2|A|.                \tag{2.3}
\]

The exact protected-Ore criterion is
\(\lambda_P(A)\le\sigma(A)\) for every residual lower shore \(A\).

### Lemma 2.2 (linear protected loss)

For every \(A\subseteq\mathcal L\setminus Z\),

\[
                         \lambda_P(A)\le2|A|.        \tag{2.4}
\]

#### Proof

Consider one protected owner \(U\in Y\).  If neither protected edge at
\(U\) leaves \(A\), its summand in (2.2) is zero.  If both leave, every
member of \(A\cap N(U)\) is an unprotected facet of \(U\), and the loss is
at most the number of those facets, capped at two.  If exactly one leaves,
positive loss requires \(a_U\ge2\); besides the protected facet in \(A\),
there is then an unprotected facet of \(A\cap N(U)\) to which the unit loss
can be charged.

Thus all loss injects into incidences from \(A\) to \(Y\) which are not
edges of \(P\).  By Lemma 2.1 each lower vertex has at most two incidences
to \(Y\), proving (2.4).  \(\square\)

## 3. Spanning-factor extension

### Theorem 3.1

For all sufficiently large \(r\), the incidence cycle \(P\) is contained
in a simple spanning two-factor of \(G\).  Equivalently, there is a simple
Johnson two-factor on every rank-\(r\) owner which contains the entire
transversal lift and uses every rank-\((r-1)\) lower colour exactly once.

#### Proof

Assume a residual Ore shore \(A\subseteq\mathcal L\setminus Z\) fails.
The sharp protected-Ore small/co-small localization theorem, together
with (1.7), gives

\[
 \min\{|A|,W-|A|\}
 <{r(r-1)\over2r-1}|E(P)|
 <r2^{r-1}.                                           \tag{3.1}
\]

First suppose \(|A|<r2^{r-1}\).  Complement \(A\) to an \(r\)-uniform
family and write \(|A|={x\choose r}\) in the real-binomial convention.
Stirling's formula gives

\[
 {\lfloor13r/10\rfloor\choose r}>r2^{r-1}            \tag{3.2}
\]

for all sufficiently large \(r\), because

\[
 \left({(13/10)^{13/10}\over(3/10)^{3/10}}\right)>2.
\]

Hence \(x<13r/10\).  Kruskal--Katona and the capped-shadow slack bound
give

\[
 { |N(A)|\over|A|}\ge {r\over x-r+1}
 >{r\over3r/10+1},                                   \tag{3.3}
\]

and

\[
 \sigma(A)\ge {r-2\over r-1}(|N(A)|-|A|)>2|A|        \tag{3.4}
\]

eventually.  This contradicts Lemma 2.2.

It remains to exclude the co-small alternative.  Put

\[
 X=\mathcal L\setminus Z,\qquad B=X\setminus A.
\]

Then (3.1) implies \(|B|<r2^{r-1}\).  If the optional deficiency of \(B\)
were positive, choose its inclusion-minimal positive Dulmage--Mendelsohn
core \(B^-\), with positive owner family \(Q\).  The exact optional-core
ledger gives \(|Q|>|B^-|\).  Lemma 2.1 gives every owner optional gap at
least \(r-2\); residual owner capacity is at most two.  The sharp
one-sided partial-shadow theorem therefore forces every member of \(Q\)
to contain at least \(r-3\) members of \(B^-\), and hence

\[
 |B^-|\ge {2r-7\choose r-4}+1.                       \tag{3.5}
\]

The right side is \(2^{2r-o(r)}\), whereas
\(|B^-|\le|B|<r2^{r-1}\), a contradiction.

No protected Ore shore fails.  Bipartite \(b\)-matching integrality now
extends \(P\) to a spanning two-factor.  Projecting through the lower
shore gives the claimed exact owner/lower Johnson factor.  \(\square\)

## 4. Residence and topology scope

If the cube Hamilton cycle in (1.3) has repeated-direction gap at least
\(q+1\), the protected transversal component is itself \(q\)-biresident.
Theorem 3.1 does **not** make the other factor components resident.  It
also keeps \(P\) as a closed saturated component, so it does not fuse it
to the complement.  Opening the lift and transporting its missing one or
two lower colours through a resident connector is a separate, genuinely
chronological theorem.

Thus the former top-cell-complement question is not an incidence
obstruction: arbitrary cross-cell completion exists.  The surviving
problem is to choose that completion and the necessary openings so that
residence, upper support, source tickets, and final fusion coexist.
