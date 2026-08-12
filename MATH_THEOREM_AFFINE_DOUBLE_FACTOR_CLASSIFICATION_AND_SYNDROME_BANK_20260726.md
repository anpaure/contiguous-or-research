# Affine double-factor classification, the overlap-kernel test, and a finite-field syndrome bank

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

> **Full-code census strengthening.**  The fixed-`x` bound in Section 7
> is valid but not sharp for the physical code.  The exact joint law and
> uniform long-sector fibre degree are proved in
> `MATH_OBSTRUCTION_AFFINE_PARITY_LIFT_ERASURE_CENSUS_20260726.md`.

## 0. Verdict

The affine ansatz

\[
 y=Ap+Bx+c
\tag{0.1}
\]

can be classified completely in the nondegenerate full-direction case.
Here \(p\) ranges over the even shore of \(Q_r\), \(x\in Q_r\), and

\[
 d_p(x)\in[r],\qquad
 F_p(x)=x+e_{d_p(x)},\qquad
 T_x(p)=p+e_{d_p(x)}.
\tag{0.2}
\]

Suppose the row and column maps are both obtained from neighbor
permutations after the same affine change (0.1):

\[
\begin{aligned}
 Ap+B F_p(x)+c&=G_B(y),\\
 A T_x(p)+Bx+c&=G_A(y).
\end{aligned}
\tag{0.3}
\]

Assume \(A,B\) are invertible and every direction occurs. Then:

1. \(A\) and \(B\) are coordinate-permutation matrices;
2. writing their coordinate permutations as
   \(\alpha,\beta\in S_r\), there is one direction coloring
   \(\delta:Q_r\to[r]\) such that
   \[
   \delta_A(y)=\alpha\delta(y),\qquad
   \delta_B(y)=\beta\delta(y);
   \tag{0.4}
   \]
3. every affine solution is
   \[
   \boxed{
   d_p(x)=\delta(Ap+Bx+c),}
   \tag{0.5}
   \]
   where both twisted maps
   \[
   y\longmapsto y+e_{\alpha\delta(y)},\qquad
   y\longmapsto y+e_{\beta\delta(y)}
   \tag{0.6}
   \]
   are neighbor permutations.

Thus the exact parameter space is a direction coloring \(\delta\) together
with two members of its twist bank

\[
 \mathcal K(\delta)=
 \left\{\sigma\in S_r:
 y\mapsto y+e_{\sigma\delta(y)}
 \text{ is a permutation}\right\}.
\tag{0.7}
\]

This is the full generalization of the earlier double-factor lemma.

There is also a sharp affine collision test. Put

\[
 \tau=B^{-1}A,
\tag{0.8}
\]

viewed as a coordinate permutation. If \(J=J_{p,d}(x)\) is a completed
coarse-direction set of an aligned window and

\[
 k=|J\cap\tau^{-1}J|,
\tag{0.9}
\]

then the physical trace has multiplicity at least

\[
 \boxed{2^{k-1}}
\tag{0.10}
\]

inside the affine fibre whenever \(k\ge1\). In particular, trace
injectivity requires

\[
 \boxed{|J\cap\tau^{-1}J|\le1}
\tag{0.11}
\]

for every protected window.

A growing algebraic family exists. Let \(r=2^s\), index the coordinates
by \(\mathbb F_{2^s}\), and put

\[
 \Sigma(y)=\sum_{z\in\mathbb F_{2^s}}y_z z.
\tag{0.12}
\]

For \(c\notin\{0,1\}\), define

\[
 \delta_c(y)=c\Sigma(y),\qquad
 G_c(y)=y+e_{c\Sigma(y)}.
\tag{0.13}
\]

Then \(G_c\) is a neighbor permutation. For every
\(a\in\mathbb F_{2^s}^{*}\) with \(ac\ne1\), multiplication by \(a\)
induces a coordinate permutation \(P_a\), and

\[
 y=P_ap+x,\qquad
 d_p(x)=c\Sigma(P_ap+x)
\tag{0.14}
\]

solves both row and column bijections using the pair

\[
 G_B=G_c,\qquad G_A=G_{ac}.
\tag{0.15}
\]

This gives \(r-2\) affine forms, or \(r-3\) genuinely nonidentity forms.
If \(g=1+c\) is primitive, all nonzero-syndrome components are isometric
\(C_{2(r-1)}\)'s; only the \(1/r\) zero-syndrome fraction lies in
\(C_2\)'s.

The bank can avoid the kernel obstruction (0.11). If
\(a=g^k\) and every protected depth is at most \(H\), then

\[
 H\le k\le r-1-H
\tag{0.16}
\]

makes \(J\cap P_a^{-1}J=\varnothing\) for every nonzero-syndrome window
of depth at most \(H\). There are \(r-2H+O(1)\) such forms.

Nevertheless this bank does **not** solve the requested trace hash. At a
fixed depth it has only \(r-1\) possible window supports:

\[
 J_d(u)=cu\{1,g,\ldots,g^{d-1}\},
\qquad u\in\mathbb F_{2^s}^{*}.
\tag{0.17}
\]

For fixed \(x\), the complete support code
\((J,p|_{J^c})\) has too few values to distinguish the even contexts once

\[
 2^{d-1}>r.
\tag{0.18}
\]

The finite-field family removes the affine-kernel collision but has only
\(\log_2 r\) bits of support entropy.  In fact, for the full physical code
and `d\ge s=\log_2r`, every long-sector fibre has degree

\[
                         {4^d\over2r}.                \tag{0.19}
\]

A Gaussian-depth solution needs a
direction coloring whose twist bank and window-support catalogue grow
exponentially in the protected depth, not merely linearly in \(r\).

## 1. The general row-column equations

Work over \(\mathbb F_2\). Let

\[
 E=\{p\in Q_r:|p|\equiv0\pmod2\},
\qquad
 O=\{p\in Q_r:|p|\equiv1\pmod2\}.
\tag{1.1}
\]

Let \(A,B\in GL(r,2)\), \(c\in Q_r\), and define \(y\) by (0.1).
For every \(p\in E\), suppose \(F_p\) is a neighbor permutation with
direction \(d_p(x)\). Suppose also that \(T_x:E\to O\) from (0.2) is a
bijection for every \(x\).

Assume the two bijections are represented by neighbor permutations

\[
 G_A(y)=y+e_{\delta_A(y)},\qquad
 G_B(y)=y+e_{\delta_B(y)}
\tag{1.2}
\]

through (0.3).

### Theorem 1.1 (classification of nondegenerate affine double factors)

If the values \(d_p(x)\) range over all of \([r]\), then \(A\) and \(B\)
are coordinate-permutation matrices. If their index permutations are
\(\alpha,\beta\), then

\[
 \alpha^{-1}\delta_A(y)
 =\beta^{-1}\delta_B(y)
 =d_p(x)
\tag{1.3}
\]

whenever \(y=Ap+Bx+c\).

Conversely, let \(\delta:Q_r\to[r]\) and let
\(\alpha,\beta\in\mathcal K(\delta)\). Put

\[
 A=P_\alpha,\qquad B=P_\beta,
\qquad d_p(x)=\delta(Ap+Bx+c).
\tag{1.4}
\]

Then every \(F_p\) is a neighbor permutation and every \(T_x:E\to O\)
is a bijection.

#### Proof

Subtract \(y\) from the two identities in (0.3). For every attained
direction \(i=d_p(x)\),

\[
 B e_i=e_{\delta_B(y)},\qquad
 A e_i=e_{\delta_A(y)}.
\tag{1.5}
\]

Thus every column of \(A\) and \(B\) is a standard basis vector. Their
invertibility makes those columns distinct, so both matrices are
coordinate permutations. Equation (1.3) follows immediately.

For the converse, fix \(p\) and use the affine bijection

\[
 \phi_p(x)=Ap+Bx+c.
\]

Then

\[
\begin{aligned}
 \phi_p(F_p(x))
 &=y+B e_{\delta(y)}\\
 &=y+e_{\beta\delta(y)}
 =G_B(y).
\end{aligned}
\tag{1.6}
\]

Hence \(F_p=\phi_p^{-1}G_B\phi_p\) is a permutation.

For fixed \(x\), the affine map

\[
 \psi_x(p)=Ap+Bx+c
\]

maps \(E\) bijectively to one parity shore. Moreover

\[
\begin{aligned}
 \psi_x(T_x(p))
 &=y+A e_{\delta(y)}\\
 &=y+e_{\alpha\delta(y)}
 =G_A(y).
\end{aligned}
\tag{1.7}
\]

The neighbor permutation \(G_A\) bijects the two parity shores, so
\(T_x\) is a bijection \(E\to O\). \(\square\)

The constant \(c\) only changes which affine parity shore occurs and has
no effect on the classification.

## 2. Exact classification of the twist bank

Let

\[
 C_i=\{y:\delta(y)=i\}.
\tag{2.1}
\]

The sets \(C_i\) partition \(Q_r\). For \(\sigma\in S_r\), define

\[
 G_\sigma(y)=y+e_{\sigma(i)}
\quad(y\in C_i).
\tag{2.2}
\]

### Proposition 2.1 (translated-color partition criterion)

\[
 \boxed{
 \sigma\in\mathcal K(\delta)
 \iff
 \{C_i+e_{\sigma(i)}:i\in[r]\}
 \text{ partitions }Q_r.}
\tag{2.3}
\]

Equivalently, for every \(z\in Q_r\),

\[
 \boxed{
 \sum_{i=1}^r
 \mathbf1_{\{\delta(z+e_{\sigma(i)})=i\}}=1.}
\tag{2.4}
\]

#### Proof

The image of the color class \(C_i\) under \(G_\sigma\) is exactly
\(C_i+e_{\sigma(i)}\). Thus \(G_\sigma\) is bijective precisely when
these images form a partition. A point \(z\) lies in the \(i\)-th image
exactly when \(z+e_{\sigma(i)}\in C_i\), which is (2.4). \(\square\)

This criterion is finite, exact, and contains no cycle-order assumption.
It classifies every admissible pair \((G_A,G_B)\): choose any two
\(\alpha,\beta\in\mathcal K(\delta)\).

## 3. The affine overlap-kernel obstruction

Fix an affine solution from Theorem 1.1 and put

\[
 \tau=B^{-1}A=P_{\beta^{-1}\alpha}.
\tag{3.1}
\]

For an even context \(p\), a phase \(x\), and an aligned coarse window of
depth \(d\), let

\[
 J=J_{p,d}(x)
\tag{3.2}
\]

be its set of completed coarse directions.

The physical trace records \(p|_{J^c}\), \(x|_{J^c}\), and \(J\).

### Theorem 3.1 (affine-fibre collision multiplicity)

Let

\[
 K=J\cap\tau^{-1}J,\qquad k=|K|.
\tag{3.3}
\]

For every even vector \(v\) supported in \(K\), put

\[
 p'=p+v,\qquad x'=x+\tau v.
\tag{3.4}
\]

Then \((p',x')\) has the same aligned physical trace as \((p,x)\).
Consequently the trace multiplicity is at least \(2^{k-1}\) when
\(k\ge1\).

#### Proof

Since \(v\) is even, \(p'\) remains on the even shore. Also

\[
\begin{aligned}
 Ap'+Bx'+c
 &=Ap+Av+Bx+B\tau v+c\\
 &=Ap+Bx+c,
\end{aligned}
\tag{3.5}
\]

because \(B\tau=A\) and the two copies of \(Av\) cancel.

The row conjugacy (1.6) therefore gives the same \(G_B\)-trajectory and
the same direction window \(J\) from both starts. The difference
\(p'-p=v\) is supported in \(J\), while
\(x'-x=\tau v\) is supported in \(J\) by the definition of \(K\).
Hence the two starts agree in both recorded outside restrictions.

The even vectors supported on a \(k\)-set form a subspace of size
\(2^{k-1}\) for \(k\ge1\). \(\square\)

For \(k=0\) or \(1\), the only even vector supported in \(K\) is zero.
Thus (0.11) is the sharp condition for eliminating this particular
affine-kernel collision.

### Corollary 3.2 (half-depth boundary)

If \(d>(r+1)/2\), then every \(d\)-set \(J\) satisfies

\[
 |J\cap\tau^{-1}J|\ge2,
\tag{3.6}
\]

so no affine double factor can be trace-injective beyond half depth.

#### Proof

Both \(J\) and \(\tau^{-1}J\) have size \(d\), hence their intersection
has size at least \(2d-r\). \(\square\)

The protected range \(d\le r/2\) is exactly the range in which a
near-disjoint affine pairing remains possible.

## 4. A finite-field family of double factors

Let

\[
 \mathbb F=\mathbb F_{2^s},\qquad r=|\mathbb F|=2^s,
\]

and index the \(r\) cube coordinates by \(z\in\mathbb F\). Define the
linear syndrome

\[
 \Sigma(y)=\sum_{z\in\mathbb F}y_z z.
\tag{4.1}
\]

For \(c\in\mathbb F\setminus\{0,1\}\), define \(G_c\) by (0.13).

### Lemma 4.1 (linear syndrome neighbor permutation)

The map \(G_c\) is a permutation of \(Q_r\), and

\[
 \Sigma(G_cy)=(1+c)\Sigma(y).
\tag{4.2}
\]

#### Proof

Toggling coordinate \(c\Sigma(y)\) adds that field label to the syndrome,
which proves (4.2).

Given \(z=G_cy\), equation (4.2) recovers

\[
 \Sigma(y)=(1+c)^{-1}\Sigma(z).
\]

The toggled coordinate \(c\Sigma(y)\) is then known, and

\[
 y=z+e_{c\Sigma(y)}
\]

is the unique preimage. \(\square\)

For \(a\in\mathbb F^*\), let \(P_a\) be the coordinate permutation

\[
 P_a e_z=e_{az}.
\tag{4.3}
\]

It obeys

\[
 \Sigma(P_ay)=a\Sigma(y).
\tag{4.4}
\]

### Theorem 4.2 (linear-size affine double-factor bank)

Fix \(c\notin\{0,1\}\). For every \(a\in\mathbb F^*\) with \(ac\ne1\),
put

\[
 A=P_a,\qquad B=I,\qquad
 d_p^{(a)}(x)=c\Sigma(P_ap+x).
\tag{4.5}
\]

Then all row maps \(F_p^{(a)}\) are affine conjugates of \(G_c\), and all
column maps are affine conjugates of \(G_{ac}\). In particular the parity
complete-mapping equations hold exactly.

#### Proof

The row increment in the \(y=P_ap+x\) coordinate is

\[
 e_{c\Sigma(y)},
\]

so the row map is \(G_c\).

The column increment is

\[
 P_a e_{c\Sigma(y)}
 =e_{ac\Sigma(y)},
\]

so the column map is \(G_{ac}\), which is a permutation by Lemma 4.1
because \(ac\notin\{0,1\}\). Theorem 1.1 applies. \(\square\)

There are \(r-2\) allowed values of \(a\): all \(r-1\) nonzero field
elements except \(c^{-1}\). Excluding \(a=1\) leaves \(r-3\) nonidentity
forms.

## 5. Cycle structure and the zero-syndrome quarantine

Put

\[
 g=1+c.
\tag{5.1}
\]

Assume \(g\) is primitive in \(\mathbb F^*\), so it has order \(r-1\).

### Proposition 5.1 (exact orbit structure)

On the zero-syndrome fibre, \(G_c\) consists of \(C_2\)'s in coordinate
\(0\). On every nonzero-syndrome fibre orbit, it consists of isometric
\(C_{2(r-1)}\)'s with first-half direction word

\[
 cu,cgu,\ldots,cg^{r-2}u
\tag{5.2}
\]

for some \(u\in\mathbb F^*\).

The zero-syndrome fibre has size \(2^r/r\), a fraction \(1/r\) of the
cube.

#### Proof

If \(\Sigma(y)=0\), the selected coordinate is \(0\), whose field label
does not change the syndrome. Toggling it twice returns, giving \(C_2\)'s.

If \(\Sigma(y)=u\ne0\), (4.2) makes the successive syndromes

\[
 u,gu,\ldots,g^{r-2}u.
\]

The corresponding directions are (5.2), which runs through every
nonzero coordinate exactly once. After \(r-1\) steps the syndrome returns,
but every nonzero coordinate has been toggled once, so the vertex has not
returned. The second traversal toggles them all again and returns after
\(2(r-1)\) steps. The first half uses distinct directions, proving
isometry.

The linear map \(\Sigma:Q_r\to\mathbb F\) is surjective, so every fibre
has size \(2^{r-s}=2^r/r\). \(\square\)

Thus the algebraic bank gives asymptotically full long-cycle ownership,
but not a literal spanning \(C_{2r}\)-factor. The exceptional \(1/r\)
sector must be quarantined or separately resolved.

## 6. Eliminating the affine-kernel overlap

For \(1\le d<r-1\), a nonzero-syndrome \(d\)-window of \(G_c\) has support

\[
 J_d(u)=cu\{1,g,\ldots,g^{d-1}\}.
\tag{6.1}
\]

For the form indexed by \(a\), the relative permutation in (0.8) is
\(\tau=P_a\).

### Theorem 6.1 (many overlap-free affine forms)

Let \(a=g^k\). If

\[
 d\le k\le r-1-d,
\tag{6.2}
\]

then

\[
 J_d(u)\cap P_a^{-1}J_d(u)=\varnothing
\tag{6.3}
\]

for every \(u\ne0\).

Consequently, if every protected depth satisfies \(d\le H\), every

\[
 H\le k\le r-1-H
\tag{6.4}
\]

eliminates the affine-kernel collision simultaneously at all protected
depths. This supplies \(r-2H+O(1)\) forms, subject only to excluding
\(a=c^{-1}\) and, if desired, \(a=1\).

#### Proof

After dividing (6.1) by \(cu\), the two sets in (6.3) are cyclic intervals

\[
 \{g^0,\ldots,g^{d-1}\},
\qquad
 \{g^{-k},\ldots,g^{d-1-k}\}
\]

in the cyclic group of order \(r-1\). They are disjoint exactly under
(6.2). The uniform statement follows from \(d\le H\). \(\square\)

This is a genuine growing family satisfying both exact bijection equations
and the sharp overlap test.

## 7. Why the syndrome bank does not hash \(p_J\)

For fixed \(c\) and \(d\), equation (6.1) gives only \(r-1\) distinct
window supports. In fact, for \(1\le d<r-1\), the set \(J_d(u)\) determines
\(u\): it is one labelled cyclic interval in the primitive \(g\)-order.

Fix \(x\). The syndrome map

\[
 p\longmapsto\Sigma(P_ap+x)
\tag{7.1}
\]

from the even shore onto \(\mathbb F\) has equal fibres: parity and
syndrome are independent linear functionals because the coordinate
labelled \(0\) changes parity without changing syndrome. Hence exactly

\[
 \frac{r-1}{r}\,2^{r-1}
\tag{7.2}
\]

even contexts have nonzero syndrome.

### Theorem 7.1 (support-entropy obstruction)

The finite-field syndrome bank cannot make the complete erased-context
code

\[
 p\longmapsto
 \bigl(J_{p,d}(x),p|_{J_{p,d}(x)^c}\bigr)
\tag{7.3}
\]

injective once

\[
 2^{d-1}>r.
\tag{7.4}
\]

This remains true for every one of the overlap-free choices in
Theorem 6.1.

#### Proof

On the nonzero-syndrome contexts, there are at most \(r-1\) possible
supports. For each support \(J\), the recorded restriction \(p|_{J^c}\)
has at most \(2^{r-d}\) values. Thus the code range has size at most

\[
 (r-1)2^{r-d}.
\tag{7.5}
\]

Injectivity on the domain (7.2) would imply

\[
 \frac{r-1}{r}2^{r-1}
 \le (r-1)2^{r-d},
\]

or \(2^{d-1}\le r\). This contradicts (7.4). \(\square\)

Allowing \(L\) genuinely different syndrome multipliers or primitive
orders enlarges the union of support catalogues to at most \(L(r-1)\).
Thus the necessary entropy condition is

\[
 Lr\ge2^{d-1}.
\tag{7.6}
\]

For Gaussian \(d\), a polynomial-size algebraic bank cannot suffice.

### Corollary 7.2 (full physical-code catalogue cut)

Let `R_d` be the number of distinct depth-`d` supports available to the
construction.  The full aligned code

\[
                         (J,p|_{J^c},x|_{J^c})       \tag{7.7}
\]

has at most `R_d\,4^{r-d}` values.  Hence near-injectivity on the
`2^{2r-1}` even-time starts requires

\[
                         R_d\ge(1-o(1))2^{2d-1}.      \tag{7.8}
\]

For one syndrome order, `R_d=r-1`; for `L` genuinely different support
catalogues, `R_d\le L(r-1)`.  Therefore the necessary condition is

\[
                         L(r-1)\ge(1-o(1))2^{2d-1}.  \tag{7.9}
\]

When `r=2^s` and `d\ge s`, the exact census in the note cited above shows
that every used long-sector code has degree `2^{2d-s-1}=4^d/(2r)`.
Thus (7.8) is not merely an alphabet estimate for this bank: its fibres
are exactly uniform.

## 8. Exact successor target

The affine classification separates the two remaining requirements.

1. **Ownership:** choose a direction coloring \(\delta\) with a nontrivial
   twist bank \(\mathcal K(\delta)\). Theorem 1.1 then solves all row and
   column bijections.
2. **Hashing:** for \(\tau=\beta^{-1}\alpha\), every protected support
   must first satisfy
   \[
   |J\cap\tau^{-1}J|\le1,
   \]
   and the support labels must distinguish at least `2^{|J|-1}` erased
   parity contexts in every fixed-phase test.  Globally, the full physical
   code requires at least `(1-o(1))2^{2|J|-1}` realized supports by (7.8).

The finite-field syndrome construction solves item 1 with
\(\Theta(r)\) simultaneous forms and solves the overlap part of item 2
through half depth. It fails only the final entropy count.

The smallest replacement lemma is therefore:

> **Exponential trace-hash twist bank — open.** Construct a direction
> coloring \(\delta:Q_r\to[r]\), a set
> \(\mathcal L\subseteq\mathcal K(\delta)^2\), and protected window
> factors such that:
>
> * the intrinsic depth-`d` support catalogue has size at least
>   `(1-o(1))2^{2d-1}` for every protected `d` (and in particular is
>   `2^{\Omega(H)}` at the largest depth);
> * every relative permutation
>   \(\tau=\beta^{-1}\alpha\) obeys
>   \(|J\cap\tau^{-1}J|\le1\) on its protected windows;
> * the window support determines the erased parity context \(p|_J\);
> * the neighbor components are isometric long cycles on
>   \(1-o(1)\) of the cube.

No further complete-mapping equation is hidden: Theorem 1.1 is the exact
algebraic solution. The surviving obstruction is support entropy.

## 9. Audit checklist

1. Both matrices in the affine form are forced to be coordinate
   permutations only under the stated invertibility and full-direction
   hypotheses.
2. The row auxiliary permutation is indexed by \(B\); the column auxiliary
   permutation is indexed by \(A\).
3. The collision perturbation uses
   \(x'=x+B^{-1}Av\), so its support condition is exactly
   \(v\subseteq J\cap\tau^{-1}J\).
4. The parity constraint removes one binary degree of freedom and gives
   \(2^{k-1}\), not \(2^k\).
5. The field coordinate \(0\) is real and is responsible for the
   \(1/r\) short-cycle sector.
6. Avoiding the overlap kernel is necessary but not sufficient for trace
   injectivity; the syndrome bank demonstrates the distinction.
