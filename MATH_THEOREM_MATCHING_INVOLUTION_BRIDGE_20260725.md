# Perfect-matching involution bridges

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Put \(n=2m+1\), and let \({\mathscr I}_m\) be the conjugacy class of
coordinate involutions with cycle type

\[
                         2^m1.
\]

These bridges combine two properties which transpositions do not:

1. their class average mixes every central rank up to an exact
   \(1/n\) error; and
2. each individual bridge fixes only \(2^{m+o(m)}=o(W)\) central target
   sets.

For a hole family \({\cal Z}\subseteq\binom{[n]}r\), with
\(h=|{\cal Z}|\) and \(N=\binom nr\), some
\(\sigma\in{\mathscr I}_m\) satisfies

\[
 \boxed{
 |{\cal Z}\setminus\sigma{\cal Z}|
 \ge\left(1-{1\over n}\right){h(N-h)\over N}.}
\tag{0.1}
\]

The same \(\sigma\) can be selected simultaneously for any nonnegative
weighted collection of ranks.

This gives essentially full-relabel hole-to-covered opportunity while
retaining an involutive two-factor coupling.  It does not prove useful
component switching: a productive member of the class may still have a
connected or expanding owner overlay.  The precise remaining joint gate is
to obtain (0.1) together with fragmented or low-conductance ownership
geometry.

## 1. Fixed subsets of a matching involution

Let \(\sigma\in{\mathscr I}_m\).  A set fixed by \(\sigma\) is a union of
some of its \(m\) transposition pairs, with the unique fixed coordinate
optionally included.  Hence the number of fixed \(j\)-sets is

\[
 F_j(\sigma)
 =[x^j](1+x)(1+x^2)^m
 =\binom m{\lfloor j/2\rfloor}.
\tag{1.1}
\]

In particular, uniformly for ranks \(r=m-q\) in any \(o(m)\) central
window,

\[
 F_r(\sigma)\le2^m=o\!\left(\binom{2m+1}{m-q}\right).
\tag{1.2}
\]

Thus no bridge in this class has a positive-density setwise-fixed target
family.  This removes the frozen-hole mechanism which closes many
transposition cubes.

## 2. Exact class spectrum

Let

\[
 V_r=\mathbb R^{\binom{[n]}r}
 =U_0\oplus U_1\oplus\cdots\oplus U_s,
 \qquad s=\min(r,n-r),
\tag{2.1}
\]

be the multiplicity-free Johnson decomposition, where \(U_j\) is the
Specht module of shape \((n-j,j)\).  Let

\[
 K={1\over|{\mathscr I}_m|}
   \sum_{\sigma\in{\mathscr I}_m}P_\sigma .
\tag{2.2}
\]

### Theorem 2.1

The eigenvalues of \(K\) are

\[
 \boxed{
 \theta_0=1,\qquad
 \theta_{2a+1}=0,\qquad
 \theta_{2a}={\binom ma\over\binom{2m+1}{2a}}
 \quad(a\ge1).}
\tag{2.3}
\]

Moreover,

\[
                         0\le\theta_j\le {1\over n}
 \qquad(j\ge1).
\tag{2.4}
\]

#### Proof

The permutation character on \(j\)-subsets is \(F_j(\sigma)\).
Young's rule gives

\[
 F_j=\sum_{i=0}^j\chi^{(n-i,i)},
\]

so the character of \(U_j\) at \(\sigma\) is

\[
 \chi^{(n-j,j)}(\sigma)=F_j(\sigma)-F_{j-1}(\sigma).
\tag{2.5}
\]

For \(j=2a+1\), (1.1) makes this difference zero.  For \(j=2a\),

\[
 F_{2a}-F_{2a-1}
 =\binom ma-\binom m{a-1}.
\tag{2.6}
\]

The dimension of \(U_{2a}\) is

\[
 \binom n{2a}-\binom n{2a-1}.
\tag{2.7}
\]

Since \(n=2m+1\), the common factor

\[
 {m-2a+1\over m-a+1}
\]

cancels between (2.6) and (2.7), giving (2.3).

For \(a=1\), (2.3) is \(1/n\).  Consecutive even eigenvalues satisfy

\[
 {\theta_{2a+2}\over\theta_{2a}}
 ={2a+1\over2m+1-2a}\le1
\]

through the available Johnson range.  This proves (2.4). \(\square\)

## 3. Hole crossing

Let \(z=\mathbf1_{\cal Z}\), and decompose

\[
 z={h\over N}\mathbf1+\sum_{j\ge1}z_j,
 \qquad z_j\in U_j.
\tag{3.1}
\]

For \(\sigma\in{\mathscr I}_m\), put

\[
 A_\sigma({\cal Z})
 =|{\cal Z}\setminus\sigma{\cal Z}|
 =h-\langle z,P_\sigma z\rangle.
\tag{3.2}
\]

By (2.3)--(2.4),

\[
\begin{aligned}
 \mathbb E_\sigma\langle z,P_\sigma z\rangle
 &= {h^2\over N}+\sum_{j\ge1}\theta_j\|z_j\|_2^2\\
 &\le {h^2\over N}
   +{1\over n}\left(h-{h^2\over N}\right).
\end{aligned}
\tag{3.3}
\]

Substitution in (3.2) proves

\[
 \boxed{
 \mathbb E_{\sigma\in{\mathscr I}_m}A_\sigma({\cal Z})
 \ge\left(1-{1\over n}\right){h(N-h)\over N}.}
\tag{3.4}
\]

Equation (0.1) follows by averaging.

### Corollary 3.1 (one bridge for many depths)

For hole families \({\cal Z}_q\), sizes \(h_q\), ambient layer sizes
\(N_q\), and arbitrary weights \(w_q\ge0\), some one
\(\sigma\in{\mathscr I}_m\) satisfies

\[
 \boxed{
 \sum_qw_q|{\cal Z}_q\setminus\sigma{\cal Z}_q|
 \ge\left(1-{1\over n}\right)
 \sum_qw_q{h_q(N_q-h_q)\over N_q}.}
\tag{3.5}
\]

#### Proof

Average the left side over the same conjugacy class at every depth, apply
(3.4), sum, and choose an outcome attaining at least the mean. \(\square\)

## 4. Relation to the MSW recursion

One representative of \({\mathscr I}_m\) is the parallel-pair bridge

\[
 \vartheta=(2\ 3)(4\ 5)\cdots(2m\ 2m+1),
\tag{4.1}
\]

with coordinate \(1\) fixed.  Its first \(m-1\) transpositions are exactly
the recursion-adjacent coordinate pairs which support the contextual MSW
\(C_8\) charts.

This makes (4.1) an algebraically natural candidate for fragmentation.
However, (3.5) is a conjugacy-class average and does not imply that this
particular representative has large hole crossing.  Conversely, a member
of the class selected by (3.5) need not preserve the recursive component
geometry of (4.1).

The surviving theorem is therefore a joint selection statement:

\[
 \boxed{
 \text{find }\sigma\in{\mathscr I}_m
 \text{ with both the opportunity in (3.5) and a productive
 fragmented/low-conductance owner overlay}.}
\tag{4.2}
\]

The class spectrum proves that target mixing is abundant; the missing
information is its correlation with ownership geometry.
