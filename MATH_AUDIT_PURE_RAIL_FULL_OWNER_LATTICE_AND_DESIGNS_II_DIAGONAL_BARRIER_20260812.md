# Independent audit: pure-rail full owner lattice and the diagonal Designs II barrier

**Date:** 2026-08-12
**Audited source:**
`MATH_THEOREM_PURE_RAIL_FULL_OWNER_LATTICE_AND_DESIGNS_II_DIAGONAL_BARRIER_20260812.md`
**Method:** line-by-line integral replay and smallest-parameter calibration;
no solver or numerical search
**Verdict:** **PASS after one cosmetic TeX correction.**  The adjacent
toggle identity, exact-distance connectivity, integral generation of
\(\ker_{\mathbb Z}P_R\), and point-image congruence argument are all valid
under the displayed hypotheses.  No missing congruence or small admissible
counterexample was found.  The result is strictly a signed-lattice theorem;
none of the arguments proves positive semigroup normality.

## 1. Parameter audit

The definitions give

\[
 q=d+1,\qquad c=R-q,\qquad M=k-c=k-R+q.
\]

The main assumption

\[
 M-2\ge2(q+1)
\]

is stronger than the consequence printed in the source.  In fact it gives

\[
 k-R=M-q\ge q+4=d+5,
\]

and hence certainly \(k-R\ge d+3\).  Therefore both periods
\(M-1,M-2\) are legal and nonmaximal, and every complement used in the
connectivity proof has more than the required number of points.

The smallest admissible calibration is

\[
 d=1,quad q=2,quad c=1,quad R=3,quad M=8,quad k=9.
\tag{1.1}
\]

Here the two periods used by the point-image proof are \(7\) and \(6\),
both in the legal interval \([6,8]\).

## 2. Adjacent-toggle current

Let \(L,S\) be ordered blocks of length \(d=q-1\), and use the cyclic
order

\[
 L,x,y,S,E,
\]

where every extra toggle lies in the exterior block \(E\).  Since
\(N\ge2q+2\), \(E\) has at least two elements.  Swapping adjacent
\(x,y\) leaves every cyclic \(q\)-window unchanged as a set except:

\[
 L+x,quad y+S
 \quad\longleftrightarrow\quad
 L+y,quad x+S.
\]

After adjoining the core \(C=A\cap B\), the old-minus-new column current is

\[
 e_{A+x}+e_{B+y}-e_{A+y}-e_{B+x}
 =\delta_{xy}(A)-\delta_{xy}(B).
\]

The toggle complement has size \(M\), while the prescribed local bank has
size \(2d+2=2q\); hence the asserted extension to every legal \(N\) is
available.  Both orders are legitimate pure rails.  Thus Lemma 2.1 is an
exact column-difference identity, not merely a projected current identity.

At the boundary instance (1.1), take the order
\(\ell,x,y,s,u,v\).  Its two changed 2-windows are exactly
\(\ell x,ys\), replaced by \(\ell y,xs\), confirming the formula at the
smallest allowed period.

## 3. Exact-distance context graph

For a Johnson edge

\[
 A=H+a,qquad B=H+b,qquad |H|=R-2,
\]

one may choose \(C_0\subset H\) of size
\(c=R-d-1\), since \(d\ge1\).  The complement of \(A\cup B\) inside
\([k]\setminus\{x,y\}\) has size

\[
 k-R-2\ge d+1.
\]

Choose a disjoint \(d\)-set \(D\) and put \(Z=C_0\cup D\).  Then

\[
 |Z|=R-1,qquad |A\cap Z|=|B\cap Z|=c.
\]

Thus every ordinary Johnson edge is replaced by a length-two path in the
exact-distance graph.  Since the Johnson graph is connected, so is
\(G_{xy}\).  No parity assumption or hidden requirement that \(c=0\) is
used.

For (1.1), the context graph is the graph on 2-subsets of seven points in
which two contexts meet in exactly one point: the line graph of \(K_7\),
which is connected.  Hence the smallest admissible case exhibits no
exception.

## 4. Integral point-kernel generation

Connectivity makes the quotient class of \(\delta_{xy}(A)\) independent
of \(A\).  A common context avoiding \(x,y,z\) exists because
\(k-R\ge2\), and gives the exact cocycle

\[
 \delta_{xy}+\delta_{yz}=\delta_{xz}.
\]

After choosing a base point, the quotient class of an owner has the affine
form

\[
 [A]=\alpha+\sum_{x\in A}\gamma_x.
\]

If \(z\in\ker_{\mathbb Z}P_R\), then its point equations vanish and

\[
 R\sum_Az_A=sum_x(P_Rz)_x=0.
\]

Because this equality is in \(\mathbb Z\), \(\sum_Az_A=0\).  Substitution
in the affine quotient formula kills both the constant and point terms.
No division is made inside the possibly torsion-bearing quotient group.
Therefore the proof establishes the integral inclusion

\[
 \ker_{\mathbb Z}P_R\subseteq\mathcal L_{\rm own}
\]

exactly as claimed.

The only source correction needed here was typographical:
`mathbb Z` was changed to `\mathbb Z` in the definition of the quotient.

## 5. Point image and congruence

Every toggle point lies in exactly \(q\) cyclic windows, and every core
point lies in all \(N\).  Hence

\[
 P_Rf=N\mathbf1_C+q\mathbf1_T.
\]

For period \(N=M-1\) or \(M-2\), there is both a core role and an unused
role.  Placing arbitrary distinct \(x,y\) in those roles and exchanging
them changes the point image by

\[
 N(e_x-e_y).
\]

The two periods therefore supply both
\((M-1)(e_x-e_y)\) and \((M-2)(e_x-e_y)\).  Bézout applies in the signed
lattice because the periods are consecutive, yielding every unit
difference and hence the complete zero-sum lattice.

A period-\((M-1)\) column minus a period-\((M-2)\) column has total point
sum \(R\).  Combining one such vector with the zero-sum lattice produces
every vector whose total coordinate sum is divisible by \(R\).  The
reverse containment follows because every rail column has total point sum
\(RN\).  Thus Lemma 3.1 is exact.

Lifting this point image and then subtracting uses the already-proved point
kernel, so Theorem 3.2 follows without a saturation assumption.  In
particular, obtaining an individual owner vector uses signed combinations;
it does not imply a positive owner-disjoint decomposition.

## 6. Designs II and exact scope

The almost-spanning coordinate molecule has

\[
 U=c+N\in\{k-2,k-1,k\},
\]

so the fixed-molecule hypothesis does not apply diagonally.  In the full
injection complex, after pinning \(U-1\) coordinate labels, exactly
\(k-U+1\le3\) choices remain.  This is incompatible with the required
positive-density extension count for large \(k\).  Therefore the note's
conclusion is appropriately negative: *Designs II* is not an available
black box here.  This external-theorem discussion is not used in the
owner-lattice proof.

The proved result eliminates signed modular characters only in the stated
owner/lower/zero-boundary projection.  It leaves untouched:

1. holes in the nonnegative affine semigroup;
2. pairwise owner-disjoint realization;
3. compulsory palette, upper-ticket, phase/socket, and common-cap rows; and
4. connectivity of the selected positive support.

Those limitations are explicitly retained in the source, so no scope
correction is required.
