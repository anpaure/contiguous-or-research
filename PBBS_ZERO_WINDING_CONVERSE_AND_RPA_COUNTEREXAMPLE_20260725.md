# RETRACTED: proposed PBBS zero-winding converse

> **AUDIT WARNING (2026-07-25).**  The sector-shift lemma and the asserted
> converse are false.  In particular the primitive root
> \(1111100001110000\) has height five and deficit one but does not return
> at gap eleven.  See
> `PBBS_ZERO_WINDING_CONVERSE_AUDIT_20260725.md`.  The claimed
> falsification of \((RP_A)\) is therefore withdrawn.

Date: 2026-07-25

> **RETRACTED (2026-07-25).**  The converse in Theorem 3.1 is false.
> The primitive height-three word \(1110011000\) has \(d(D)=1\), but its
> exact \(\tau\)-orbit has deficit sequence \((1,5,1)\), returns to the
> same root after three rotations, and satisfies
> \(1+5+1=7\ne3=\delta(D)\pmod {11}\).  Lemma 2.1 overlooks an
> off-spine forest after it is transported into a positive-depth
> \(A\)-sector, where it can attain the global height before the displayed
> spine.  Therefore Sections 3--6 and the claimed disproof of \((RP_A)\)
> are invalid.  See
> `PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md` for the literal
> factorizations and exact diagnosis.  The text below is retained only as
> an audit trail.

**RETRACTED after independent audit.  Do not cite any theorem or
consequence below.**

The failure is in Lemma 2.1: after sector transport, an (A_i)-forest can
become the first deepest sector, so the displayed spine need not remain the
first deepest spine.  The claim remains false even on primitive roots.  An
explicit primitive counterexample is

\[
 D=1111100001110000
\]

of semilength (8), height (5), and (d(D)=1); its five-step deficit
sum does not equal the terminal first-maximum position, so it has no claimed
gap-(11) return.  See
`PBBS_ZERO_WINDING_CONVERSE_AUDIT_20260725.md` for the independent audit.

The endpoint-order counterexample in Section 7 is independent of the false
converse and remains valid.

The text below is retained only as an audit trail of the failed argument.

## 0. Outcome

Put

\[
 N=2r+1,
 \qquad B_r=\operatorname{Cat}_r,
 \qquad \tau=\phi^2
\]

for the normalized PBBS quotient on semilength-\(r\) Dyck roots.
For

\[
 D=P\,1\,R\,0\,S
\]

at the first up-step attaining the global maximum, with the displayed zero
the first subsequent return to height zero, recall

\[
 d(D)=|S|+1,
 \qquad
 \delta(D)=|P|+1,
 \qquad
 \tau D=S\,1\,P\,0\,R.
\]

The previously proved zero-winding theorem says that a zero-winding return
forces

\[
 d(D)=1,
 \qquad
 g=2\operatorname{ht}(D)+1.
\]

The converse is also true.

> **Exact zero-winding classification.**  Every Dyck root with \(d(D)=1\)
> starts a consecutive omitted-label return of exact gap
> \[
>  2\operatorname{ht}(D)+1.
> \]

This has a decisive consequence.  For every fixed \(A>0\), with

\[
 H_A=\lceil A\sqrt r\rceil,
\]

the physical PBBS residence packing satisfies

\[
 \boxed{
   \nu_{H_A}(P_r)\ge c_A B_r\sqrt r
 }
\]

for some \(c_A>0\) and all sufficiently large \(r\).  In particular

\[
 \nu_{H_A}(P_r)\ne o_A(B_r).
\]

Thus the fixed-window sparse-residence hypothesis \((RP_A)\) in Section 22
of `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` is false.  The conditional
implication from \((RP_A)\) to coefficient one remains correct, but PBBS
Gaussian residences cannot be handled by cutting or hitting all short
positive runs.  A successful PBBS proof now needs a seam/fusion mechanism
which shares the repair cost across this dense, highly structured family.

## 1. First-deepest-spine sectors

Let \(T(D)\) be the contour plane tree of \(D\), of height \(h\).  Along
the path from the root to the first deepest leaf, write \(A_i\) for the
ordered child forest before the spine child and \(B_i\) for the ordered
child forest after it, at depth \(i\), \(0\le i<h\).  Then

\[
 D=A_0 1 A_1 1\cdots 1A_{h-1}1
       0B_{h-1}0\cdots0B_1 0B_0,
 \tag{1.1}
\]

where \(A_{h-1}=\varnothing\).  The exact sector-transport formula is

\[
 \tau D
 =B_0 1A_0 1A_1 1\cdots1A_{h-1}
       0 0B_{h-1}0\cdots0B_1.
 \tag{1.2}
\]

Moreover

\[
 d(D)=2|B_0|+1,
 \qquad
 \delta(D)=h+2\sum_{i=0}^{h-1}|A_i|,
 \tag{1.3}
\]

where forest size means number of edges.

Thus \(d(D)=1\) is exactly the condition

\[
 B_0=\varnothing.
 \tag{1.4}
\]

Equivalently, the primitive component which first attains the global
height is the final primitive component of \(D\).

## 2. Exact sector shift through one height cycle

Assume (1.4), and put

\[
 D_j=\tau^jD,
 \qquad 0\le j\le h.
\]

### Lemma 2.1 (sector shift)

Every \(D_j\) has height \(h\), and its first-deepest-spine sectors are

\[
 B_i^{(j)}=
 \begin{cases}
  B_{i+j},&i+j<h,\\
  \varnothing,&i+j\ge h,
 \end{cases}
 \tag{2.1}
\]

and

\[
 A_i^{(j)}=
 \begin{cases}
  B_{j-1-i},&0\le i<j,\\
  A_{i-j},&j\le i<h.
 \end{cases}
 \tag{2.2}
\]

### Proof

Formula (1.2) gives the one-step update

\[
 A_0'=B_0,
 \qquad A_i'=A_{i-1}\ (1\le i<h),
 \tag{2.3}
\]

and

\[
 B_i'=B_{i+1}\ (0\le i<h-1),
 \qquad B_{h-1}'=\varnothing.
 \tag{2.4}
\]

It remains to justify that the displayed spine stays the first deepest
spine, so that (2.3)--(2.4) may be iterated.  A tree in the original
forest \(B_j\), rooted at depth \(j\), has relative height at most
\(h-j\).  When that forest reaches the root seam after \(j\) shifts, its
height is therefore at most \(h-j<h\) for \(j\ge1\).  The only possible
height-\(h\) forest at the first shift is \(B_0\), and this is empty by
(1.4).  Hence none of the transported prefix forests reaches height \(h\)
before the displayed spine.  The spine itself still reaches height \(h\),
so it remains first deepest.  Iterating (2.3)--(2.4) gives (2.1)--(2.2).
\(\square\)

## 3. Exact first return

Let

\[
 C_j=\sum_{t=0}^{j-1}d(D_t),
 \qquad C_0=0.
 \tag{3.1}
\]

Equations (1.3) and (2.1) give, for \(0\le j<h\),

\[
 d(D_j)=2|B_j|+1,
 \qquad
 C_j=j+2\sum_{t=0}^{j-1}|B_t|.
 \tag{3.2}
\]

Equations (1.3) and (2.2) give

\[
 \delta(D_j)
 =h+2\sum_{t=0}^{j-1}|B_t|
    +2\sum_{i=0}^{h-j-1}|A_i|.
 \tag{3.3}
\]

Consequently, for every \(0\le j<h\),

\[
 \boxed{
 \delta(D_j)-C_j
 =h-j+2\sum_{i=0}^{h-j-1}|A_i|>0.
 }
 \tag{3.4}
\]

At \(j=h\), (2.2) says that the \(A\)-sectors of \(D_h\) are precisely
the old \(B\)-sectors in reverse order.  Therefore

\[
 \boxed{
 \delta(D_h)
 =h+2\sum_{t=0}^{h-1}|B_t|
 =C_h.
 }
 \tag{3.5}
\]

### Theorem 3.1 (converse zero-winding theorem)

If \(d(D)=1\), then the omitted coordinate at \((u,D)\) has its next
occurrence at time

\[
 \boxed{g=2h+1,\qquad h=\operatorname{ht}(D).}
 \tag{3.6}
\]

The return has zero winding.

### Proof

After \(j\) applications of the even-time skew product, the spatial root
is \(u-C_j\pmod N\).  The following odd step adds \(\delta(D_j)\).
Thus the time-\((2j+1)\) omitted coordinate equals \(u\) precisely when

\[
 C_j\equiv\delta(D_j)\pmod N.
 \tag{3.7}
\]

At \(j=h\), (3.5) gives literal equality, so there is a zero-winding
return at time \(2h+1\).

For \(j<h\), (3.4) is positive.  Both \(C_j\) and \(\delta(D_j)\) are
strictly below \(N\): indeed \(C_j<C_h=\delta(D_h)\le2r=N-1\), while
\(\delta(D_j)\) is a position in a length-\(2r\) word.  Hence (3.7)
fails.  At positive even time \(2j\le2h\), equality with the initial root
would require \(C_j\equiv0\pmod N\), impossible because
\(0<C_j<C_h<N\).  Thus no earlier occurrence exists.  This proves
(3.6). \(\square\)

Together with the already proved necessity, this gives the exact
classification

\[
 \boxed{
 \text{zero-winding consecutive return}
 \quad\Longleftrightarrow\quad d(D)=1,
 }
 \tag{3.8}
\]

and its gap is always \(2\operatorname{ht}(D)+1\).

## 4. A Catalan-positive Gaussian family

Let \(C_L(n)\) denote the number of semilength-\(n\) Dyck paths of height
at most \(L\).  Fix \(A>0\), put

\[
 H=\lceil A\sqrt r\rceil,
 \qquad L=H-2,
 \tag{4.1}
\]

and consider the primitive paths

\[
 \mathcal U_{r,A}
 =\{,1E0:E\in\mathcal D_{r-1},\ operatorname{ht}(E)\le L,\}.
 \tag{4.2}
\]

Every member has \(d(D)=1\) and height at most \(H-1\).  Theorem 3.1
therefore gives a physical omitted-label return of gap at most \(2H-1\),
hence a projected positive residence of length at most \(H\).  Moreover

\[
 |\mathcal U_{r,A}|=C_L(r-1).
 \tag{4.3}
\]

### Lemma 4.1 (fixed-Gaussian Catalan mass)

For every fixed \(A>0\), there is \(c_A>0\) such that

\[
 \boxed{C_{\lceil A\sqrt r\rceil-2}(r-1)\ge c_A\operatorname{Cat}_r}
 \tag{4.4}
\]

for all sufficiently large \(r\).

### Proof

Closed walks in the path graph on \(\{0,1,\ldots,L\}\) give the exact
spectral formula

\[
 C_L(n)
 =\frac{2}{L+2}\sum_{j=1}^{L+1}
   \sin^2\!\frac{\pi j}{L+2}
   \left(2\cos\frac{\pi j}{L+2}\right)^{2n}.
 \tag{4.5}
\]

Every term is nonnegative.  Keeping \(j=1\), using
\(L=A\sqrt r+O(1)\), \(n=r-1\), and the elementary estimates
\(\sin x\ge2x/\pi\) on \([0,\pi/2]\) and
\(\log\cos x\ge-x^2\) for small \(x\), gives

\[
 C_L(r-1)
 \ge c A^{-3}r^{-3/2}4^{r-1}e^{-2\pi^2/A^2}
 \tag{4.6}
\]

for an absolute \(c>0\).  Since
\(\operatorname{Cat}_r\asymp4^r r^{-3/2}\), (4.4) follows after
absorbing the fixed positive \(A\)-dependent factor. \(\square\)

## 5. Physical packing lower bound

Let \(R_H^{\rm long}\) be the number of quotient roots on quotient cycles
longer than \(H+1\) which start a residence of length at most \(H\).
The short-cycle estimate gives

\[
 Z_H\le(2H+2)N^{2H+2}=\exp(o(r))=o(B_r).
 \tag{5.1}
\]

By (4.2)--(4.4),

\[
 R_H^{\rm long}\ge c_A B_r-Z_H\ge\frac{c_A}{2}B_r
 \tag{5.2}
\]

for all sufficiently large \(r\).

On a long quotient cycle, greedily choosing one start and deleting every
start whose interval meets it loses at most \(2H+1\) starts.  Hence

\[
 \overline\nu_H
 \ge\frac{R_H^{\rm long}}{2H+1}
 \ge c_A'\frac{B_r}{\sqrt r}.
 \tag{5.3}
\]

Every selected nonwrapping quotient interval has \(N\) mutually disjoint
spatial lifts, and lifts over quotient-edge-disjoint intervals remain
disjoint.  Therefore the deck lower bound gives

\[
 \boxed{
 \nu_H(P_r)
 \ge N\overline\nu_H
 \ge c_A'' B_r\sqrt r.
 }
 \tag{5.4}

This disproves \((RP_A)\), and in fact misses it by a factor of order
\(\sqrt r\).

## 6. Consequence for coefficient one

The all-depth PBBS support theorem remains valid.  What fails is the plan
of making its consecutive-shadow windows physical by cutting every short
positive coordinate residence.  The obstruction is not an exceptional
low-defect family: primitive roots alone have Catalan-positive mass and,
on the Gaussian window, generate the maximum natural order
\(B_r\sqrt r\) of disjoint physical short residences.

Accordingly, coefficient one can only survive in this lane through a
support-preserving shared seam/fusion theorem which handles many crossing
residences at once.  Any theorem whose cost is bounded below by the short-
residence packing or transversal number cannot have \(o(W)\) overhead.

## 7. No-overtaking does not monotonically pair seam endpoints

A natural proposed linear seam would sort the short positive runs crossing
one transition edge by their left endpoints and hope that their right
endpoints are monotone.  This is false in the exact PBBS, already at
\(r=3\).

Take the quotient three-cycle

\[
 D_0=110100,
 \qquad D_1=101100,
 \qquad D_2=110010.
\]

Its one-step voltages are \((2,4,2)\) modulo \(7\).  Starting the omitted
label at zero gives

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrrrrr}
t&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16&17&18&19&20\\ \hline
\lambda_t&0&2&6&1&3&0&2&4&1&3&5&2&4&6&3&5&0&4&6&1&5.
\end{array}
\tag{7.1}
\]

In the complement-projected even-time cycle, an occurrence at odd time
inserts its label and the next, necessarily even, occurrence removes it.
Thus the following three positive residence intervals all contain the
projected transition edge indexed by \(8\):

\[
\begin{array}{c|c|c}
\text{label}&\text{omitted-label times}&
 \text{projected transition-edge interval}\\ \hline
1&3\longrightarrow8&\{2,4,6,8\}\\
0&5\longrightarrow16&\{4,6,8,10,12,14,16\}\\
4&7\longrightarrow12&\{6,8,10,12\}.
\end{array}
\tag{7.2}
\]

Their left endpoints are

\[
 2<4<6,
\]

whereas their paired right endpoints are

\[
 8,16,12.
\]

This order is neither increasing nor decreasing.  Hence equality-particle
no-overtaking does not imply a monotone or laminar pairing of all residence
endpoints across a seam.  A linear-cost seam, if it exists, must use more
than endpoint order.
