# Large-overlap pruning-strip collision for zero-winding PBBS returns

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or web
search is used.

## 0. Result and notation

Put

\[
B_r=\operatorname{Cat}_r.
\]

Consider a genuine first zero-winding PBBS return based at a Dyck root of
semilength \(r\). Let

\[
s=\text{its duration}=\text{its Dyck height},
\qquad \lambda=\Lambda/2
\]

where \(2\lambda\) is its endpoint excess. Write

\[
D^{(j)}=\partial^jD,
\qquad r_j=|D^{(j)}|/2,
\]

and define the first-mountain pruning depth

\[
p=\min\{j:r_j=s-j\},
\qquad q=s-p.
\]

Thus

\[
\partial^pD=M_q:=1^q0^q.
\]

The letters \(p\) and \(\lambda\) are kept separate throughout: \(p\) is a
pruning depth, whereas \(\lambda\) is endpoint half-overlap.

Let \(z_{r,s,2\lambda,p}\) count genuine first zero-winding starts with these
exact parameters.

### Theorem 0.1 (unsaturated pruning-strip collision)

There are absolute constants \(c,C>0\) such that, whenever

\[
p<2q,
\qquad q=s-p,
\qquad \lambda>0,
\]

one has

\[
\boxed{
z_{r,s,2\lambda,p}
\le
C4^r\frac{(\lambda+2)^2}{s^6}
\frac1{\sqrt{\lambda+1}}
\exp\!\left(-\frac{c\lambda}{(p+1)^2}\right).}
\tag{0.1}
\]

### Corollary 0.2 (large-overlap sub-sector removed)

For every fixed \(A>0\), there is an absolute sufficiently large constant
\(K\) such that

\[
\boxed{
\#\left\{D:
s\le A\sqrt r,
\ p<2q,
\ \lambda\ge K(p+1)^2\log r
\right\}
=o_A(B_r/\sqrt r).}
\tag{0.2}
\]

This is a start-count theorem, so it also holds for every
quotient-edge-disjoint packing in this sector.

Section 11 proves a second, genuinely packing-level consequence. If

\[
\frac{(P(r)+1)\log r}{\sqrt r}\longrightarrow0,
\]

then every quotient-edge-disjoint positive-overlap family with
\(p\le P(r)\) and \(s\le A\sqrt r\) has size
\(o_A(B_r/\sqrt r)\), with no restriction on \(\lambda\).

Consequently, after the already proved shared-boundary deletion of

\[
0<\lambda=o(r^{1/5})
\]

at packing level, every potentially non-negligible unsaturated return in the
large-overlap residual obeys

\[
\boxed{
\frac{r^{1/5}}{\log r}\lesssim\lambda
<K(p+1)^2\log r,
\qquad
p+1\gtrsim\frac{r^{1/10}}{\log r}.}
\tag{0.3}
\]

The lower endpoint in (0.3) is written in the weaker start-count scale used
in the assignment. At quotient-packing level the audited shared-boundary
theorem removes the stronger range \(\lambda=o(r^{1/5})\).

These theorems do **not** prove coefficient one. Sections 7 and 11 state
the exact surviving sector, and Section 8 gives a genuine obstruction to
the stronger pointwise dichotomy.

## 1. Audited inputs

We use the following previously proved facts.

1. Peak deletion commutes with the two-step quotient map:

   \[
   \partial\tau=\tau\partial.
   \tag{1.1}
   \]

   Every mountain is fixed by \(\tau\).

2. A genuine zero-winding return of duration \(s\) and endpoint excess
   \(2\lambda\) has the shared-boundary identities

   \[
   U=(0S_{s-1})\cdots(0S_1)=ER_0,
   \tag{1.2}
   \]

   \[
   V=(\overline T_{s-1}0)\cdots(\overline T_00)
   =R_s(0S_s)E,
   \tag{1.3}
   \]

   where \(E\) is one balanced word of length \(2\lambda\).

3. The forward and dual array caps are

   \[
   \operatorname{ht}(S_j)\le\min(j,s-j+\lambda),
   \tag{1.4}
   \]

   \[
   \operatorname{ht}(T_j)\le\min(s-1-j,j+1+\lambda).
   \tag{1.5}
   \]

4. At critical Boltzmann parameter \(z=1/4\), a capped Dyck block of cap
   \(a\) has partition function

   \[
   C_a(1/4)=\frac{2(a+1)}{a+2}.
   \tag{1.6}
   \]

5. The normalized coefficient distribution of

   \[
   \prod_{j=1}^{J}C_j(z)=\frac1{Q_{J+1}(z)}
   \tag{1.7}
   \]

   has largest atom \(O(J^{-2})\). This is the audited first-passage
   kernel estimate.

No assertion derived from the retracted primitive-height converse is used.

## 2. Pruning confines the common boundary to a strip

### Lemma 2.1

Under the hypotheses of Theorem 0.1, every prefix height of the common
boundary word \(E\) lies in \([-p,p]\).

### Proof

Put \(D_j=\tau^jD\). From (1.1),

\[
\partial^pD_j
=\tau^j\partial^pD
=\tau^jM_q
=M_q.
\tag{2.1}
\]

Use the canonical first-maximum factorization

\[
D_j=(P_j1R_j0)S_j.
\tag{2.2}
\]

The displayed word is a concatenation of a nonempty first Dyck component
and the terminal Dyck forest \(S_j\). Simultaneous peak deletion is
componentwise across this concatenation. The first component has height
\(s\), so after \(p<s\) deletions it remains nonempty. The result (2.1) is
the single primitive mountain \(M_q\). Therefore the terminal forest must
have vanished:

\[
\partial^pS_j=\varnothing.
\]

Equivalently,

\[
\boxed{\operatorname{ht}(S_j)\le p.}
\tag{2.3}
\]

Now parse the balanced prefix \(E\) of (1.2) at its successive strict
record minima. If

\[
a=-\min_{0\le t\le2\lambda}
\operatorname{net}(E[1,t]),
\]

then uniquely

\[
E=(0D_1)\cdots(0D_{a-1})0P,
\tag{2.4}
\]

where the \(D_i\) are complete Dyck words and \(P\) is a nonnegative
prefix of the next Dyck block. Since \(E\) is balanced, \(P\) ends at
relative height \(a\). It lies in a block of height at most \(p\), so

\[
a\le p.
\tag{2.5}
\]

Inside the \(i\)-th parsed block, every prefix height of \(E\) has the form

\[
-i+u,
\qquad 0\le u\le p.
\]

Because \(i\le a\le p\), these values lie in \([-p,p]\). This proves the
claim. \(\square\)

### Audit note

One must not assert that the dual terminal words \(T_j\) vanish after
\(p\) deletions. That statement is neither needed nor supplied by (1.1).
Since \(E\) is balanced, the height at time \(t\) in its reversed word is
the negative of the height at time \(2\lambda-t\) in \(E\). Thus reversal
of the already proved forward strip confinement gives the required dual
record-depth bound directly.

## 3. Pointwise probabilities and the strip collision

### Lemma 3.1 (uniform pointwise boundary bound)

For every possible fixed balanced boundary word \(e\) arising under the
hypotheses of Theorem 0.1,

\[
\Pr(U[1,2\lambda]=e)\le C4^{-\lambda},
\tag{3.1}
\]

and

\[
\Pr(V[|V|-2\lambda+1,|V|]=e)\le C4^{-\lambda}.
\tag{3.2}
\]

### Proof

Let \(a\) be the record depth in (2.4). The first \(a\) forward blocks
have caps

\[
h_i=\min(s-i,i+\lambda),
\qquad1\le i\le a.
\]

Since \(a\le p\),

\[
s-i\ge s-p=q,
\qquad i+\lambda\ge\lambda+1.
\]

Hence

\[
h_i\ge b:=\min(q,\lambda+1).
\tag{3.3}
\]

The standard record-minimum calculation, using total critical completion
weight at most \(2^{1-|P|}\), gives

\[
\Pr(U[1,2\lambda]=e)
\le
2^{1-2\lambda+a}
\prod_{i=1}^{a-1}\frac1{C_{h_i}(1/4)}.
\tag{3.4}
\]

From (1.6),

\[
\frac1{C_{h_i}(1/4)}
=\frac12\left(1+\frac1{h_i+1}\right)
\le\frac12\exp\!\left(\frac1b\right).
\]

Substitution in (3.4) yields

\[
\Pr(U[1,2\lambda]=e)
\le4\,4^{-\lambda}\exp(a/b).
\tag{3.5}
\]

If \(b=q\), then

\[
a/b\le p/q<2.
\]

If \(b=\lambda+1\), then the elementary bound \(a\le\lambda\) gives

\[
a/b<1.
\]

This proves (3.1). Reverse \(e\) and use the dual ordered caps. By Lemma
2.1 and the audit note, its record depth is again at most \(p\), and the
same lower bound (3.3) applies. This proves (3.2). \(\square\)

### Lemma 3.2 (Hadamard collision inside the pruning strip)

Under the critical independent array laws,

\[
\Pr(\text{the two boundary words agree and are balanced})
\le
C4^{-\lambda}(\lambda+1)^{-1/2}
e^{-c\lambda/(p+1)^2}.
\tag{3.6}
\]

### Proof

Let \(\mathcal B_{\lambda,p}\) be the balanced length-\(2\lambda\) walks
confined to \([-p,p]\), and let \(A_p\) be the adjacency matrix of the
path on the \(2p+1\) states \(-p,-p+1,\ldots,p\). The exact eigen-expansion
at the central state is

\[
\frac{|\mathcal B_{\lambda,p}|}{4^\lambda}
=
\frac1{p+1}
\sum_{\substack{1\le k\le2p+1\\k\ \mathrm{odd}}}
\cos^{2\lambda}\!\left(\frac{k\pi}{2p+2}\right).
\tag{3.7}
\]

Pair the terms at the two ends of the spectrum and use

\[
|\cos x|
\le
\exp\!\left(-c\,\operatorname{dist}(x,\pi\mathbb Z)^2\right).
\]

Then

\[
\frac{|\mathcal B_{\lambda,p}|}{4^\lambda}
\le
\frac C{p+1}
\sum_{j\ge0}
\exp\!\left(-\frac{c\lambda(2j+1)^2}{(p+1)^2}\right).
\tag{3.8}
\]

For \(x>0\), splitting at \(x=1\) gives the elementary Gaussian-sum
bound

\[
\sum_{j\ge0}e^{-cx(2j+1)^2}
\le Cx^{-1/2}e^{-c'x}.
\tag{3.9}
\]

Indeed, for \(x\le1\) compare with a Gaussian integral, while for
\(x\ge1\) factor out the first term and sum a geometric tail. Substituting
\(x=\lambda/(p+1)^2\) in (3.8) yields the single heat-kernel estimate

\[
|\mathcal B_{\lambda,p}|
\le
C4^\lambda(\lambda+1)^{-1/2}
\exp\!\left(-\frac{c\lambda}{(p+1)^2}\right).
\tag{3.10}
\]

Thus the central-binomial and strip-spectral gains multiply; they are not
being multiplied as unrelated upper bounds. For each common word, multiply
(3.1) and (3.2), then sum using (3.10). This proves (3.6). \(\square\)

## 4. Conditional anti-concentration for every overlap size

### Lemma 4.1

After conditioning on any fixed common boundary word \(E=e\), the largest
atom of the total remaining forward-plus-dual semilength is \(O(s^{-2})\),
uniformly in \(\lambda\).

### Proof

Let \(a\) be the forward record depth. Conditioning on \(E=e\) fixes the
complete terminal blocks it crosses and a prefix of the final crossed
block. The untouched forward array contains

\[
S_1,\ldots,S_{s-a-1}.
\]

Put

\[
J=\min\!\left\{
s-a-1,
\left\lfloor\frac{s+\lambda}{2}\right\rfloor
\right\}.
\tag{4.1}
\]

For \(j\le J\), the cap of \(S_j\) is exactly \(j\). Thus the conditional
generating function contains the independent factor

\[
\prod_{j=1}^{J}C_j(z)=\frac1{Q_{J+1}(z)}.
\tag{4.2}
\]

Because \(a\le p\) and \(p<2q\),

\[
q=s-p>s/3,
\]

and therefore

\[
s-a-1\ge q-1>s/3-1.
\]

The second entry in (4.1) is at least \(s/2-1\). Hence

\[
J+1\ge c_0s
\tag{4.3}
\]

for an absolute \(c_0>0\), after absorbing finitely many small \(s\).
The audited first-passage kernel estimate for (4.2) now gives largest
normalized atom

\[
O(J^{-2})=O(s^{-2}).
\]

All other conditional pieces enter by convolution, which cannot increase
the largest atom. \(\square\)

This proof deliberately does not invoke the older anti-concentration lemma
whose statement assumed \(\lambda\le cs\); (4.2) works uniformly for all
\(\lambda\).

## 5. Critical telescope, including \(\lambda\ge s\)

Define

\[
F_{s,\lambda}(z)
=\prod_{j=1}^{s-1}
C_{\min(j,s-j+\lambda)}(z)
\tag{5.1}
\]

and

\[
u=\min\!\left\{
s-1,
\left\lfloor\frac{s+\lambda}{2}\right\rfloor
\right\}.
\]

At \(z=1/4\), direct telescoping of the increasing and decreasing cap
segments gives

\[
\boxed{
F_{s,\lambda}(1/4)
=
\frac{2^s(\lambda+2)}
{(u+2)(s+\lambda-u+1)}.}
\tag{5.2}
\]

Both denominator factors are at least a fixed positive multiple of \(s\),
so

\[
F_{s,\lambda}(1/4)
\le
C2^s\frac{\lambda+2}{s^2}.
\tag{5.3}
\]

For clarity, when \(\lambda\ge s-2\), one has \(u=s-1\) and every cap in
(5.1) equals \(j\). Hence exactly

\[
F_{s,\lambda}(z)=\prod_{j=1}^{s-1}C_j(z)=\frac1{Q_s(z)},
\]

and

\[
F_{s,\lambda}(1/4)=\frac{2^s}{s+1}.
\tag{5.4}
\]

Thus no small-overlap hypothesis is hidden in (5.3).

## 6. Proof of Theorem 0.1 and Corollary 0.2

The exact rank identity for the two arrays is

\[
r=s+\sum_{j=1}^{s-1}|S_j|_e
+\sum_{j=0}^{s-1}|T_j|_e-\lambda.
\tag{6.1}
\]

By Lemma 3.2, the critical normalized mass of the shared-boundary event is
at most

\[
C4^{-\lambda}
(\lambda+1)^{-1/2}
e^{-c\lambda/(p+1)^2}.
\tag{6.2}
\]

By Lemma 4.1, the required total-semilength coefficient has normalized
mass at most \(Cs^{-2}\). Coefficient tilting at \(1/4\), (6.1), and
(5.3) therefore give

\[
\begin{aligned}
z_{r,s,2\lambda,p}
&\le
C4^{r-s+\lambda}s^{-2}
\left[
4^{-\lambda}
(\lambda+1)^{-1/2}
e^{-c\lambda/(p+1)^2}
\right]
F_{s,\lambda}(1/4)^2\\
&\le
C4^r\frac{(\lambda+2)^2}{s^6}
(\lambda+1)^{-1/2}
e^{-c\lambda/(p+1)^2}.
\end{aligned}
\]

This proves Theorem 0.1.

For Corollary 0.2, put \(a=p+1\). A standard geometric-tail comparison
gives, for every sufficiently large fixed \(K\),

\[
\sum_{\lambda\ge Ka^2\log r}
(\lambda+2)^2e^{-c\lambda/a^2}
\le
Ca^6(\log r)^2r^{-cK/2}.
\tag{6.3}
\]

Indeed, after writing \(x=\lambda/a^2\), the sum is bounded by a constant
times

\[
a^6\int_{K\log r-O(1)}^\infty(x+1)^2e^{-cx}\,dx,
\]

which is at most the right side of (6.3).

Now sum (0.1), using its exponential term, over \(p<s\) and
\(s\le A\sqrt r\). Since

\[
\sum_{p<s}(p+1)^6\le Cs^7,
\]

(6.3) gives

\[
\begin{aligned}
\sum_{s\le A\sqrt r}
\sum_{p<s}
\sum_{\lambda\ge K(p+1)^2\log r}
z_{r,s,2\lambda,p}
&\le
C4^r(\log r)^2r^{-cK/2}
\sum_{s\le A\sqrt r}s^{-6}s^7\\
&\le
C_A4^r r(\log r)^2r^{-cK/2}.
\end{aligned}
\tag{6.4}
\]

Choose \(K\) so that \(cK/2>3\). Then (6.4) is

\[
o_A(4^r/r^2)=o_A(B_r/\sqrt r).
\]

This proves Corollary 0.2. Finally, if

\[
\lambda\ge r^{1/5}/\log r
\]

but the return is not in the negligible sector (0.2), then

\[
K(p+1)^2\log r>\lambda
\ge\frac{r^{1/5}}{\log r},
\]

so

\[
p+1>K^{-1/2}\frac{r^{1/10}}{\log r}.
\]

This proves (0.3).

## 7. Residual after the saturated-top theorem and Theorem 0.1

The audited saturated-top theorem says that, for fixed
\(A,\varepsilon>0\) and fixed \(\Delta\ge0\), the genuine zero-winding
starts satisfying

\[
s\le A\sqrt r,
\qquad q\ge\varepsilon\sqrt r,
\qquad p\ge2q-\Delta
\]

have cardinality

\[
o_{A,\varepsilon}(B_r/\sqrt r).
\tag{7.1}
\]

Combining (7.1), the shared-boundary theorem, and Corollary 0.2 leaves in
the Gaussian-\(q\) lane only

\[
\boxed{
s\le A\sqrt r,
\quad q\ge\varepsilon\sqrt r,
\quad p<2q-\Delta,
\quad
\frac{r^{1/5}}{\log r}\lesssim\lambda
<K(p+1)^2\log r.}
\tag{7.2}
\]

At packing level, the lower overlap threshold is handled by a two-limit
split: first remove \(\lambda\le \eta(r)r^{1/5}\) for a sufficiently slow
\(\eta(r)\downarrow0\) using the audited shared-boundary theorem, and then
analyze the complementary sector
\(\lambda>\eta(r)r^{1/5}\). No fixed positive lower constant is asserted.

The independent residual \(q=o(\sqrt r)\) is not addressed by the
saturated-top theorem and remains a transported-fan problem.

Section 11 subsequently removes every
\(p=o(\sqrt r/\log r)\) range at packing level. Thus (7.2) is an
intermediate residual; the authoritative final residual of this report is
(11.19).

## 8. Genuine obstruction to the stronger local dichotomy

Large overlap does not force \(p\ge2q\), even when \(q\) is Gaussian, and
does not force a pointwise \(o(r^{-1/2})\) Pascal-fan fraction.

Fix \(n\ge3\), \(M\ge0\), put \(F=(10)^M\), and define

\[
D_{n,M}
=1^{3n+1}0^n1^{2n-1}0^{4n-1}F0.
\tag{8.1}
\]

Its semilength is

\[
R=M+5n.
\]

An exact literal quotient trace is

\[
\begin{aligned}
D_0&=1^{3n+1}0^n1^{2n-1}0^{4n-1}F0,\\
D_1&=1^{3n+2}0^n1^{2n-2}0^{4n}F,\\
D_j&=1^{j-2}F1^{3n+3}0^n1^{2n-1-j}0^{4n},
&&2\le j\le n-1,\\
D_{n-1+k}
&=1^{n-3+k}F1^{3n+3-k}0^{n+k}1^n0^{4n-k},
&&0\le k\le3n,\\
D_{4n}&=1^n0^n1^{4n-2}F1^20^{4n}.
\end{aligned}
\tag{8.2}
\]

Factoring at the canonical first height-\(4n\) step verifies each
transition \(\tau D_j=D_{j+1}\). The only nonempty terminal suffixes are

\[
S_1=F,
\qquad S_{4n-1}=1^n0^n.
\tag{8.3}
\]

Thus

\[
\sum_{j<4n}d(D_j)=4n+2M+2n=6n+2M.
\tag{8.4}
\]

If \(C_j=\sum_{i<j}d(D_i)\), then

\[
C_1=1,
\qquad C_j=2M+j\quad(2\le j\le4n-1),
\qquad C_{4n}=2M+6n.
\]

The first-maximum positions read from (8.2) are

\[
\delta(D_0)=\delta(D_1)=6n,
\]

\[
\delta(D_j)=6n+2M
\quad(2\le j\le n-2),
\]

\[
\delta(D_j)=4n+2M
\quad(n-1\le j\le4n-1),
\]

and

\[
\delta(D_{4n})=6n+2M.
\]

Therefore

\[
C_j<\delta(D_j)\quad(0<j<4n),
\qquad C_{4n}=\delta(D_{4n})<2R+1.
\]

This proves that (8.1) starts a genuine first zero-winding return of
duration \(4n\). Its endpoint excess is

\[
\Lambda
=\delta(D_0)+\delta(D_{4n})-2R
=2n,
\]

so

\[
\lambda=n.
\tag{8.5}
\]

Substitution in the shared-boundary identities gives the literal common
word

\[
E=0\,1^n0^{n-1}.
\tag{8.6}
\]

Peak deletion is explicit:

\[
\partial^jD_{n,M}
=1^{3n+1-j}0^{n-j}1^{2n-1-j}0^{4n-j},
\qquad1\le j\le n.
\tag{8.7}
\]

Hence

\[
p=n,
\qquad \partial^nD_{n,M}=1^{3n}0^{3n},
\qquad q=3n,
\tag{8.8}
\]

so \(p<2q\).

The inverse-Pascal curvatures are

\[
y_1=M,
\qquad y_j=0\ (2\le j<n),
\qquad y_n=1.
\tag{8.9}
\]

At level one, the unique prescribed fan slot is zero because
\(S_0=\varnothing\). All intermediate levels have zero free mass. At level
\(n\), the bottom mountain is \(\tau\)-fixed and the \(y_n=1\) fibre has
\(6n+1\) lifts. Each transported phase-local terminal-zero condition
contains exactly \(6n\) lifts. On the one-unit simplex a coordinate-value
condition has \(6n\) solutions only when its prescribed value is zero; a
prescribed value one has only one solution. Hence all \(n\) independent
terminal fan conditions prescribe distinct zero coordinates.

The exact direct fan fraction is consequently

\[
\boxed{
Q_{n,M}
=
\frac{10n-4}{M+10n-4}
\frac{5n+1}{6n+1}.}
\tag{8.10}
\]

For fixed \(A>0\), choose \(c>A^{-2}\) and

\[
M=\left\lceil c(4n)^2\right\rceil.
\]

Then, as \(n\to\infty\),

\[
4n\le A\sqrt R,
\qquad
\lambda=n\gg\frac{R^{1/5}}{\log R},
\qquad
\frac q{\sqrt R}\longrightarrow\frac{3}{4\sqrt c}>0,
\]

but \(p<2q\) and

\[
\boxed{
\sqrt R\,Q_{n,M}
\longrightarrow
\frac{25}{12\sqrt c}>0.}
\tag{8.11}
\]

This family lies inside the structural residual rather than the
strip-negligible sector, because

\[
\lambda=n\ll p^2\log R.
\]

It is a pointwise obstruction, not a packing lower bound. It proves that
the surviving little-oh cannot be obtained from a deterministic local fan
factor depending only on large endpoint overlap and the pruning ranks.

## 9. Precise proved/conditional boundary

What is proved:

1. In the unsaturated sector \(p<2q\), the common endpoint boundary is
   confined to the exact strip \([-p,p]\).
2. This yields the uniform start-count estimate (0.1), including all
   \(\lambda\ge s\).
3. The sector \(\lambda\ge K(p+1)^2\log r\) is
   \(o_A(B_r/\sqrt r)\) even before quotient packing is used.
4. Large overlap does not imply pruning saturation or a pointwise
   \(o(r^{-1/2})\) fan factor.
5. Every positive-overlap packed sector with
   \(p\le P(r)=o(\sqrt r/\log r)\) is
   \(o_A(B_r/\sqrt r)\), uniformly over \(\lambda\).

After also applying the packing-level strengthening in Section 11, what
remains unproved in the Gaussian-\(q\) lane is the following packing
statement.

> **Residual chronology-sensitive packing lemma -- UNPROVED.** For fixed
> \(A,\varepsilon,K>0\), every quotient-edge-disjoint family of genuine
> first zero-winding returns satisfying
> \[
> s\le A\sqrt r,
> \quad q\ge\varepsilon\sqrt r,
> \quad p<2q,
> \quad p>\sqrt r/(\omega(r)\log r),
> \quad r^{1/5}/\omega_1(r)<\lambda<K(p+1)^2\log r
> \]
> has cardinality \(o_A(B_r/\sqrt r)\).

Here \(\omega,\omega_1\to\infty\) are sufficiently slow diagonal
envelopes.

The obstruction in Section 8 shows that a proof must use aggregate
cross-phase overlap, coefficient cancellation, or actual circular-interval
packing. A one-root or isolated-phase fan estimate cannot suffice.

## 10. Independent audit

The proof was independently reconstructed and passed after two local
scope corrections:

1. Dual strip confinement is obtained by reversing the already confined
   balanced word \(E\), not by claiming \(\partial^pT_j=\varnothing\).
2. Uniform conditional anti-concentration for arbitrary \(\lambda\) uses
   the untouched factor \(1/Q_{J+1}\), rather than the older lemma stated
   only for \(\lambda\le cs\).

The audit also checked the path-graph eigenvalue, both alternatives in the
pointwise cap estimate, the exact \(\lambda\ge s-2\) telescope, the
geometric-tail summation in (6.3), and the literal obstruction trace.

The stronger heat-kernel product and the one-sided pruning-cap theorem in
Section 11 were then independently audited. They passed after one notation
correction: the dual record depth is denoted \(d^\vee\) and need not equal
the forward record depth \(d\). Both are bounded by the same strip radius.

## 11. Packing-level strengthening from the full one-sided pruning cap

The strip theorem used \(\operatorname{ht}(S_j)\le p\) only to confine the
copied boundary. In fact the same inequality holds for every forward block,
so the complete forward partition function may be truncated. This gives a
second factor which removes every pruning range
\(p=o(\sqrt r/\log r)\) at packing level, irrespective of the overlap size.

### Theorem 11.1 (one-sided pruning-cap collision, uniform over \(p\le P\))

Let \(Z_{\le P}(r,s,2\lambda)\) count genuine first zero-winding starts of
semilength \(r\), duration \(s\), endpoint half-overlap \(\lambda>0\), and
first-mountain depth \(p\le P\). Assume

\[
P\ge1,
\qquad 3P<2s.
\tag{11.1}
\]

Put

\[
a_j=\min(j,s-j+\lambda),
\qquad b_j=\min(a_j,P),
\]

\[
F_{s,\lambda}(z)=\prod_{j=1}^{s-1}C_{a_j}(z),
\qquad
F^{(P)}_{s,\lambda}(z)=\prod_{j=1}^{s-1}C_{b_j}(z),
\]

and

\[
\mathcal R_{s,\lambda,P}
=
\frac{F^{(P)}_{s,\lambda}(1/4)}
{F_{s,\lambda}(1/4)}.
\tag{11.2}
\]

Define

\[
M_{s,\lambda,P}
=
\left[
s-4P-3+\min(\lambda,2P+1)
\right]_+.
\tag{11.3}
\]

Then absolute constants \(c,C>0\) satisfy

\[
\boxed{
Z_{\le P}(r,s,2\lambda)
\le
C4^r
\frac{(\lambda+2)^2}{s^6\sqrt{\lambda+1}}
\exp\!\left(-\frac{c\lambda}{(P+1)^2}\right)
\mathcal R_{s,\lambda,P},}
\tag{11.4}
\]

and

\[
\boxed{
\mathcal R_{s,\lambda,P}
\le
\exp\!\left(
-\frac{M_{s,\lambda,P}}{2(P+2)}
\right).}
\tag{11.5}
\]

### Proof

For every counted return, \(p\le P\). Equation (2.3), applied at each
phase, gives

\[
\operatorname{ht}(S_j)\le p\le P.
\tag{11.6}
\]

Thus the actual forward arrays form a subset of the independent array
model whose \(j\)-th cap is \(b_j\). The dual array is deliberately left
unchanged.

Condition (11.1) implies

\[
p\le P<2(s-P)\le2(s-p),
\]

so every counted return lies in the unsaturated sector. Its common boundary
is confined to \([-p,p]\subseteq[-P,P]\).

Let \(d\) be the forward record depth of a fixed possible boundary word.
Then

\[
d\le p\le P,
\qquad d\le\lambda.
\tag{11.7}
\]

Under the truncated forward law, every crossed cap is at least

\[
b=\min(s-P,\lambda+1,P).
\]

The calculation in Lemma 3.1 gives

\[
\Pr_{\rm fwd}(E=e)
\le4\,4^{-\lambda}e^{d/b}.
\]

If the displayed minimum is \(P\) or \(\lambda+1\), then \(d/b\le1\).
If it is \(s-P\), then (11.1) gives

\[
\frac d b\le\frac P{s-P}<2.
\]

Therefore

\[
\Pr_{\rm fwd}(E=e)\le C4^{-\lambda}.
\tag{11.8}
\]

Reverse \(e\), and denote its record depth by \(d^\vee\). Forward strip
confinement implies

\[
d^\vee\le p\le P.
\]

The unchanged dual caps are bounded below by
\(\min(s-P,\lambda+1)\), so the identical argument proves

\[
\Pr_{\rm dual}(E=e)\le C4^{-\lambda}.
\tag{11.9}
\]

No pruning assertion about the dual \(T_j\) is used.

Apply the heat-kernel estimate (3.10) with strip radius \(P\). Multiplying
(11.8) and (11.9) and summing over the common word gives collision
probability

\[
C4^{-\lambda}(\lambda+1)^{-1/2}
\exp\!\left(-\frac{c\lambda}{(P+1)^2}\right).
\tag{11.10}
\]

Conditional anti-concentration is now taken from the unchanged dual array.
After reversing that array, conditioning on \(E=e\) consumes at most
\(d^\vee\le P\) blocks. The untouched product contains

\[
\prod_{j=1}^{J}C_j(z)=\frac1{Q_{J+1}(z)},
\]

where

\[
J=\min\!\left\{
s-d^\vee-1,
\left\lfloor\frac{s+\lambda}{2}\right\rfloor
\right\}.
\]

By (11.1), \(s-d^\vee-1>s/3-1\), while the other entry is at least
\(s/2-1\). Hence \(J+1\gg s\), and the audited kernel estimate gives an
\(O(s^{-2})\) largest normalized atom.

Coefficient tilting now yields

\[
\begin{aligned}
Z_{\le P}(r,s,2\lambda)
&\le
C4^{r-s+\lambda}s^{-2}
4^{-\lambda}(\lambda+1)^{-1/2}
e^{-c\lambda/(P+1)^2}
F^{(P)}_{s,\lambda}(1/4)F_{s,\lambda}(1/4).
\end{aligned}
\tag{11.11}
\]

Using (11.2) and

\[
4^{-s}F_{s,\lambda}(1/4)^2
\le C\frac{(\lambda+2)^2}{s^4}
\]

proves (11.4).

It remains to estimate \(\mathcal R_{s,\lambda,P}\). The indices satisfying

\[
j\ge2P+2,
\qquad s-j+\lambda\ge2P+2
\tag{11.12}
\]

form the integer interval

\[
2P+2
\le j\le
\min(s-1,s+\lambda-2P-2).
\]

Its exact cardinality is \(M_{s,\lambda,P}\) from (11.3). At every such
index, \(a_j\ge2P+2\) and \(b_j=P\). Since

\[
C_h(1/4)=2\left(1-\frac1{h+2}\right),
\]

for every \(a\ge2P+2\),

\[
\begin{aligned}
\log\frac{C_a(1/4)}{C_P(1/4)}
&=
\log\!\left(1-\frac1{a+2}\right)
-\log\!\left(1-\frac1{P+2}\right)\\
&\ge
\frac1{P+2}-\frac1{a+2}\\
&\ge\frac1{2(P+2)}.
\end{aligned}
\]

All other factors in \(\mathcal R_{s,\lambda,P}\) are at most one.
Multiplication over the indices (11.12) proves (11.5). \(\square\)

### Corollary 11.2 (summed positive overlap)

Under (11.1), put

\[
Z^+_{\le P}(r,s)
=\sum_{\lambda\ge1}Z_{\le P}(r,s,2\lambda).
\]

Then

\[
\boxed{
Z^+_{\le P}(r,s)
\le
C4^r\frac{(P+1)^5}{s^6}
\exp\!\left(
-\frac{[s-4P-3]_+}{2(P+2)}
\right).}
\tag{11.13}
\]

Indeed,

\[
M_{s,\lambda,P}\ge[s-4P-3]_+,
\]

and comparison with a Gamma integral gives

\[
\sum_{\lambda\ge1}
\frac{(\lambda+2)^2}{\sqrt{\lambda+1}}
e^{-c\lambda/(P+1)^2}
\le C(P+1)^5.
\]

### Corollary 11.3 (packing-level shallow-pruning deletion)

Fix \(A>0\), and let \(P=P(r)\) be an integer sequence satisfying

\[
\boxed{
\frac{(P(r)+1)\log r}{\sqrt r}\longrightarrow0.}
\tag{11.14}
\]

Every quotient-edge-disjoint family \(\mathcal P_r\) of genuine first
zero-winding returns satisfying

\[
s\le A\sqrt r,
\qquad \lambda>0,
\qquad p\le P(r)
\]

has

\[
\boxed{
|\mathcal P_r|=o_A(B_r/\sqrt r).}
\tag{11.15}
\]

### Proof

For \(P=0\), Lemma 2.1 makes the positive-overlap sector empty. Assume
\(P\ge1\). Fix \(a\in(0,A)\). The audited sub-Gaussian height-packing
theorem gives

\[
\lim_{a\downarrow0}\limsup_{r\to\infty}
\frac{\sqrt r}{B_r}
|\mathcal P_r(s\le a\sqrt r)|=0.
\tag{11.16}
\]

For fixed \(a\), condition (11.14) implies eventually

\[
P\le\frac{a\sqrt r}{8}.
\]

Thus every \(s>a\sqrt r\) satisfies (11.1), and

\[
[s-4P-3]_+\ge c_as.
\]

Summing (11.13) over at most \(A\sqrt r\) values of \(s\) gives

\[
|\mathcal P_r(s>a\sqrt r)|
\le
C_{a,A}4^r(P+1)^5r^{-5/2}
\exp\!\left(-\frac{c_a\sqrt r}{P+2}\right).
\tag{11.17}
\]

Because \(B_r/\sqrt r\asymp4^r/r^2\), the ratio of (11.17) to the target
scale is at most

\[
C_{a,A}(P+1)^5r^{-1/2}
\exp\!\left(-\frac{c_a\sqrt r}{P+2}\right).
\tag{11.18}
\]

Writing

\[
g_r=\frac{\sqrt r}{(P+2)\log r},
\]

(11.14) gives \(g_r\to\infty\). Also
\((P+1)^5r^{-1/2}\le r^2\) eventually, so (11.18) is at most

\[
C_{a,A}r^{2-c_ag_r}\longrightarrow0.
\]

First take \(r\to\infty\) for fixed \(a\), and then take \(a\downarrow0\)
in (11.16). This proves (11.15). \(\square\)

### Updated residual

After Corollary 11.3, the shared-boundary packing theorem, Corollary 0.2,
and the saturated-top theorem are combined, the unsaturated Gaussian
large-overlap residual may be restricted, after choosing arbitrarily slow
divergent envelopes, to

\[
\boxed{
p>\frac{\sqrt r}{\omega(r)\log r},
\qquad
q>p/2,
\qquad
\lambda>\frac{r^{1/5}}{\omega_1(r)},
\qquad
\lambda<K(p+1)^2\log r,}
\tag{11.19}
\]

where \(\omega,\omega_1\to\infty\) may be taken sufficiently slowly.
The exact family in Section 8 has \(p=s/4\) and \(\lambda=p\), so it lies
inside (11.19): its pruning-cap factor and direct fan factor are only of
critical order. Thus (11.15) is a genuine packing-level little-oh for a
broad pruning sector, but not a proof of the complete coefficient-one
gate.

## 12. Why the cap factor does not yet extend from \(p=o(s/\log r)\) to \(p=o(s)\)

Every selected interval of duration \(s\) and pruning depth \(p\) contains
\(\Theta(s)\) distinct interior phase roots whose surrounding terminal
suffixes all have height at most \(p\). Thus a natural packing completion
would be the following open-run estimate:

\[
\boxed{
\#\left\{
D:\operatorname{ht}S(\tau^iD)\le p
\text{ for every }|i|\le c s
\right\}
=o(B_r)}
\tag{12.1}
\]

uniformly for \(s\asymp\sqrt r\) and \(p=o(s)\). If (12.1) held, then
edge-disjointness and the \(\Theta(s)\) distinct interior roots supplied by
each interval would immediately give \(o(B_r/s)=o(B_r/\sqrt r)\).

Statement (12.1) is **unproved**. The factor

\[
\frac{F^{(P)}_{s,\lambda}(1/4)}{F_{s,\lambda}(1/4)}
\le e^{-\Omega(s/P)}
\]

in Section 11 is a conditional ratio for a *closed return array*. Its
derivation uses the common balanced endpoint boundary, the dual array, and
the rank identity

\[
r=s+\sum|S_j|_e+\sum|T_j|_e-\lambda.
\]

A centered open run has none of these closure data. Its suffix tuple does
not reconstruct the root: the two unconstrained endpoint words can carry
arbitrary Catalan mass. Shifting one closed interval through its interior
also reuses the same capped blocks, so the \(s\) copies of the cap ratio
cannot be multiplied.

Therefore Section 11 rigorously reaches \(p=o(s/\log r)\) by making its
closed-array start count smaller than \(B_r/s\). Reaching all \(p=o(s)\)
requires the genuinely new open-run estimate (12.1), or another
cross-phase packing theorem. No rarity-times-length multiplication is
claimed.
