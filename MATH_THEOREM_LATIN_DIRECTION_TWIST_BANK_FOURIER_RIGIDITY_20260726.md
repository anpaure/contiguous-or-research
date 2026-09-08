# Fourier rigidity of Latin direction twist banks

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let

\[
E=\{p\in\mathbb F_2^r:|p|\equiv0\pmod2\},\qquad
V=\mathbb F_2^r .
\]

For a direction array

\[
d_p(x)\in[r]\qquad(p\in E,\ x\in V),
\]

write \(F_p(x)=x+e_{d_p(x)}\) and
\(T_x(p)=p+e_{d_p(x)}\).  This note proves four exact facts.

1. The three families saying “one direction per cell”, “every \(F_p\)
   is a permutation”, and “every \(T_x:E\to V\setminus E\) is a
   bijection” have an exact Fourier normal form.  At each nonconstant
   mode the direction vector is orthogonal to only three sign vectors.
   Hence the real relaxation has abundant freedom; the genuine issue is
   simultaneous \(0\)-\(1\) integrality and whole-cycle chronology.

2. For an affine double-factor colouring
   \(\delta:V\to[r]\), define its twist bank

   \[
   \mathcal K(\delta)=
   \{\sigma\in S_r:y\mapsto y+e_{\sigma\delta(y)}
                         \text{ is a permutation}\}.
   \]

   If \(C_i=\delta^{-1}(i)\) and

   \[
   \widehat f_i(A)=2^{-r}\sum_y
      \mathbf1_{C_i}(y)(-1)^{|A\cap\operatorname{supp}y|},
   \]

   then every valid twist satisfies

   \[
   \boxed{\sum_{i\in\sigma^{-1}A}\widehat f_i(A)=0}
   \tag{0.1}
   \]

   for every \(\varnothing\ne A\subsetneq[r]\).

3. Consequently a full-direction \(C_{2r}\)-factor colouring has no
   twist bank containing a coset of \(A_r\) when \(r\ge4\).  More
   generally, a \(k\)-homogeneous bank coset annihilates every
   weight-\(k\) Fourier coefficient.  Thus a successful large
   orthomorphism bank must be strongly non-homogeneous on subsets.

4. If the completed-support map at aligned depth \(d\) takes only \(L\)
   values, then the trace collision excess is at least

   \[
   \boxed{\bigl(2^{2r-1}-L\,2^{2(r-d)}\bigr)_+.}
   \tag{0.2}
   \]

   Near-injectivity requires
   \(L\ge(1-o(1))2^{2d-1}\).  A one-symbol complete mapping on a group
   of polynomial order in \(r\) therefore cannot reach Gaussian depth.
   At least \(2d-1-o(d)\) physically visible support bits are necessary.

These are sharp obstructions to classical algebraic complete mappings.
They do not rule out a multilevel nonlinear Latin array.

## 1. Direct Fourier normal form of the two-dimensional equations

Put

\[
z_i(p,x)=\mathbf1_{\{d_p(x)=i\}}.
\tag{1.1}
\]

Identify the odd shore with \(E\) by writing \(o=q+e_1\), and put

\[
t_i=e_1+e_i\in E.
\tag{1.2}
\]

The exact local equations are

\[
\begin{aligned}
\sum_i z_i(p,x)&=1,\\
\sum_i z_i(p,x+e_i)&=1,\\
\sum_i z_i(p+t_i,x)&=1.
\end{aligned}
\tag{1.3}
\]

Indeed, the second equation counts the predecessors of \(x\) under
\(F_p\), and the third counts the even predecessors of \(q+e_1\) under
\(T_x\).

Characters of \(E\) are indexed by
\(a\in V/\langle\mathbf1\rangle\), while characters of \(V\) are
indexed by \(b\in V\).  At a Fourier mode \((a,b)\), put

\[
v_i=\widehat z_i(a,b),\qquad
s_a(i)=(-1)^{a_i},\qquad s_b(i)=(-1)^{b_i}.
\tag{1.4}
\]

### Theorem 1.1 (three-vector Fourier system)

At every nonconstant mode \((a,b)\ne(0,0)\), equations (1.3) are
equivalent to

\[
\boxed{
\langle v,\mathbf1\rangle
=\langle v,s_a\rangle
=\langle v,s_b\rangle=0.}
\tag{1.5}
\]

At the constant mode the common equation is \(\sum_i v_i=1\).

#### Proof

The first equation of (1.3) gives the first inner product.  Translation
of \(x\) by \(e_i\) multiplies the coefficient by \((-1)^{b_i}\),
giving the third.

Translation of \(p\) by \(t_i=e_1+e_i\) multiplies it by
\((-1)^{a_1+a_i}\).  Discarding the common factor
\((-1)^{a_1}\) gives the middle inner product.  Fourier inversion proves
the converse. \(\square\)

For a generic mode the three sign vectors have rank three, leaving
dimension \(r-3\).  In particular, whenever
\(w\perp\{\mathbf1,s_a,s_b\}\),

\[
z_i(p,x)=\frac1r+\varepsilon w_i(-1)^{a\cdot p+b\cdot x}
\tag{1.6}
\]

is a nonnegative fractional solution for sufficiently small real
\(\varepsilon\).  Thus neither Fourier diagonalization nor the separate
row and column transportation polytopes can prove Boolean integrality.

## 2. Exact Fourier equations for an algebraic twist bank

Let \(\delta:V\to[r]\), let \(C_i=\delta^{-1}(i)\), and put
\(f_i=\mathbf1_{C_i}\).  For \(\sigma\in S_r\), define

\[
G_\sigma(y)=y+e_{\sigma\delta(y)}.
\tag{2.1}
\]

The image of \(C_i\) is \(C_i+e_{\sigma(i)}\), so

\[
\sigma\in\mathcal K(\delta)
\iff
\sum_{i=1}^r f_i(z+e_{\sigma(i)})=1
\quad(z\in V).
\tag{2.2}
\]

For \(A\subseteq[r]\), translation by \(e_{\sigma(i)}\) multiplies the
\(A\)-Fourier coefficient by
\((-1)^{\mathbf1_{\{\sigma(i)\in A\}}}\).  Therefore, at nonempty
\(A\),

\[
\sum_i(-1)^{\mathbf1_{\{\sigma(i)\in A\}}}
                  \widehat f_i(A)=0.
\tag{2.3}
\]

The original colour partition gives

\[
\sum_i\widehat f_i(A)=0.
\tag{2.4}
\]

Subtracting (2.3) from (2.4) proves (0.1).

### Theorem 2.1 (Fourier-incidence criterion)

For fixed nonempty proper \(A\), put

\[
v_A=(\widehat f_1(A),\ldots,\widehat f_r(A)).
\]

Then

\[
v_A\perp\mathbf1_{\sigma^{-1}A}
\quad(\sigma\in\mathcal K(\delta)),
\qquad
v_A\perp\mathbf1.
\tag{2.5}
\]

Thus the possible weight-\(|A|\) Fourier vector lies in the orthogonal
complement of the incidence span of

\[
\{\sigma^{-1}A:\sigma\in\mathcal K(\delta)\}.
\tag{2.6}
\]

This is an exact finite-rank audit for any proposed algebraic twist bank.

## 3. Homogeneous-bank collapse

A group \(\Gamma\le S_r\) is \(k\)-homogeneous if it is transitive on
\(\binom{[r]}k\), and set-homogeneous if this holds for every
\(1\le k\le r-1\).

### Lemma 3.1

If \(1\le k\le r-1\) and \(v\in\mathbb C^r\) satisfies

\[
\sum_{i\in B}v_i=0
\qquad(B\in\binom{[r]}k),
\tag{3.1}
\]

then \(v=0\).

#### Proof

Comparing two \(k\)-sets with a common \((k-1)\)-subset gives
\(v_i=v_j\) for arbitrary \(i,j\).  All coordinates equal a constant
\(c\), and then \(kc=0\). \(\square\)

### Theorem 3.2 (homogeneous twist-bank rigidity)

If a left or right coset of a \(k\)-homogeneous group is contained in
\(\mathcal K(\delta)\), then

\[
\widehat f_i(A)=0
\tag{3.2}
\]

for every \(i\) and every \(A\) of size \(k\).

If the group is set-homogeneous, there are directions \(a,b\)
(possibly equal) such that

\[
\delta(y)=a\quad(|y|\text{ even}),\qquad
\delta(y)=b\quad(|y|\text{ odd}).
\tag{3.3}
\]

#### Proof

The coset orbit in (2.6) is all of \(\binom{[r]}k\), so Lemma 3.1
proves (3.2).  If this holds at every nontrivial weight, Fourier
inversion shows that every \(f_i\) has Fourier support contained in
\(\{\varnothing,[r]\}\).  Hence \(f_i\) is constant on each parity
shore.  Since the \(f_i\)'s are \(0\)-\(1\)-valued and partition each
shore, one colour occurs on each shore. \(\square\)

The map in (3.3) alternates between at most two directions.  Its cycles
have length at most four, so it cannot be a full-direction isometric
\(C_{2r}\)-factor when \(r>2\).

For \(r\ge4\), \(A_r\) is \(k\)-homogeneous for every \(k\).  Hence:

### Corollary 3.3

No full-direction \(C_{2r}\)-factor colouring has a twist bank
containing a coset of \(A_r\).  In particular, the bank cannot contain
\(A_r\) or \(S_r\).

This rules out the maximally symmetric orthomorphism answer, but not a
large sparse code in \(S_r\).

## 4. Local transposition rigidity

The same translated-colour equation yields a pointwise stabilizer law.

### Theorem 4.1

Suppose

\[
\sigma,\ \sigma(a\ b)\in\mathcal K(\delta)
\tag{4.1}
\]

for distinct colours \(a,b\).  Put

\[
h=e_{\sigma(a)}+e_{\sigma(b)}.
\]

Then

\[
\boxed{C_a+h=C_a,\qquad C_b+h=C_b.}
\tag{4.2}
\]

#### Proof

The two translated partitions agree outside colours \(a,b\).
Translating their remaining equality by \(e_{\sigma(a)}\) gives

\[
C_a\mathbin{\dot\cup}(C_b+h)
=(C_a+h)\mathbin{\dot\cup}C_b.
\tag{4.3}
\]

If \(x\in C_a\), equality and disjointness of \(C_a,C_b\) force
\(x\in C_a+h\).  Thus \(C_a\subseteq C_a+h\), and cardinality gives
equality.  The proof for \(C_b\) is identical. \(\square\)

### Corollary 4.2

Assume \(\mathrm{id}\in\mathcal K(\delta)\), and let \(D\) be a graph
on \([r]\) such that every edge transposition \((i\ j)\) belongs to the
bank.  Then

\[
C_i+\operatorname{span}\{e_i+e_j:ij\in E(D)\}=C_i
\tag{4.4}
\]

and

\[
2^{\deg_D(i)}\mid |C_i|.
\tag{4.5}
\]

If every colour is used and

\[
\delta(D)>r-\log_2r,
\tag{4.6}
\]

no such bank exists.

#### Proof

The star vectors at \(i\) are linearly independent.  Theorem 4.1 gives
invariance under each one, proving (4.4)-(4.5).  Under (4.6), every
nonempty colour class has size \(>2^r/r\), so \(r\) disjoint nonempty
classes cannot fit inside \(V\). \(\square\)

Thus a dense bank generated by local braid transpositions creates large
translation kernels in its colour fibres.  Those kernels are exactly the
kind of invisible subspaces which survive an erased physical trace.

## 5. Universal visible-state lower bound

Return to an arbitrary parity-complete array whose rows are
doubled-permutation \(C_{2r}\)-factors.  At aligned depth \(d<r\), let

\[
J_{p,d}(x)\in\binom{[r]}d
\]

be the completed direction support.  The physical trace is

\[
\mathcal C_d(p,x)=
\bigl(J_{p,d}(x),x|_{J_{p,d}(x)^c},
                    p|_{J_{p,d}(x)^c}\bigr).
\tag{5.1}
\]

### Theorem 5.1 (support-library capacity)

If the support map takes at most \(L\) values, then

\[
|\operatorname{im}\mathcal C_d|
\le L\,2^{2(r-d)}
\tag{5.2}
\]

and the collision excess is at least (0.2).

Consequently \(o(2^{2r})\) collision excess requires

\[
L\ge(1-o(1))2^{2d-1}.
\tag{5.3}
\]

#### Proof

For each fixed \(J\), the two exterior restrictions in (5.1) have at
most \(2^{2(r-d)}\) values.  There are \(2^{2r-1}\) aligned starts.
Subtract the number of used codes from the number of starts. \(\square\)

### Corollary 5.2 (small-state algebraic no-go)

Suppose \(J_{p,d}(x)\) is a function of a state

\[
\Theta(p,x)\in\Omega,\qquad |\Omega|=M.
\]

Then near-injectivity requires

\[
\log_2M\ge2d-1-o(1).
\tag{5.4}
\]

In particular, a one-symbol orthomorphism on a group of order
\(r^{O(1)}\) fails when \(d-C\log r\to\infty\).  Reaching
\(d=\Theta(\sqrt r)\) requires a multilevel nonlinear state carrying
\(\Omega(\sqrt r)\) physically visible bits.

## 6. Exact surviving target

A successful algebraic direction array must satisfy two competing
requirements.

1. Its twist bank must be rich enough to solve the row-column Latin
   equations, but it cannot be set-homogeneous.  Bank elements differing
   by local transpositions create the explicit periods (4.2).
2. Its completed-support library must expose at least
   \(2d-1-o(d)\) bits at every protected depth.  This information cannot
   be stored in one field/group symbol of polynomial size.

Thus the remaining object is not a classical complete mapping of one
group.  It must be a multilevel nonlinear Latin array whose subset action
stays deliberately non-homogeneous while its window support reveals
approximately two new context bits per completed pair.  Equations (0.1)
and (5.3) are exact audits for the ownership and trace halves,
respectively.

