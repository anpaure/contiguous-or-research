# Reduced-scale short promotion paths: exact quotient degrees, codegrees, and the variable-rank nibble failure

Date: 2026-07-27

Method: pure mathematics. No finite search, computation, solver, or web
input is used.

All logarithms are natural.

## 0. Verdict

Put

\[
 H=\left\lfloor\sqrt{m\log\log m}\right\rfloor,
 \qquad M=m+H,
\]

\[
 W=\binom{2m}{m},\qquad
 N=N_H=\binom{2m}{m-H},\qquad
 \lambda=\lambda_H={W\over N}.
\tag{0.1}
\]

Then

\[
 \lambda=\log m+o(1).
\tag{0.2}
\]

Let \(r\) be an integer with

\[
 2\le r\le\min\{H,\lfloor\lambda\rfloor\},
 \qquad r\sim\lambda\sim\log m.
\tag{0.3}
\]

For each rank-\((m-H)\) root, retain \(r\) consecutive owners from one
promotion ring. Quotienting the cyclic-order presentations gives a simple
\((r+1)\)-uniform rooted hypergraph. Its physical representation
multiplicity is

\[
 \boxed{\mu_r=2(H-r+1)!(m-r+1)!.}
\tag{0.4}
\]

The extra factor \((H-r+1)!\) is essential. It is absent in the previously
audited long-path formula because that formula was used in the regime
\(r>H\). At the present reduced scale, the common intersection of the
retained \(H\)-windows is a second unordered block.

After quotienting by (0.4), the root and owner degrees are

\[
 \boxed{
 D_R={M!\over\mu_r},
 \qquad
 D_O={r(m!)^2\over(m-H)!\mu_r},
 \qquad
 {D_O\over D_R}={r\over\lambda}=:\rho.}
\tag{0.5}
\]

The exact maximum pair codegree is the Johnson-distance-one owner pair:

\[
 \boxed{
 {\Delta_2\over D_R}
 ={2\rho(r-1)\over r m^2}
 ={2+o(1)\over m^2}.}
\tag{0.6}
\]

Thus the attractive scalar

\[
 (r+1){\Delta_2\over D_R}\log(W+N)
 =(4\log2+o(1)){\log m\over m}\longrightarrow0
\tag{0.7}
\]

is genuine. It nevertheless does **not** imply an \(o(N)\) root leave by
any audited published nibble theorem.

The only audited theorem whose statement genuinely allows growing
uniformity is the matching theorem of Alon--Bollobas--Kim--Vu (ABKV). With
edge size

\[
 K=r+1,\qquad C=\Delta_2,\qquad D=D_R,
\]

its formal codegree hypothesis contains

\[
 e^{2K}{C\log D\over D}=o(1).
\tag{0.8}
\]

Here

\[
 \log D=(1+o(1))H\log{m\over H},
 \qquad
 \log\log D=\left({1\over2}+o(1)\right)\log m,
\tag{0.9}
\]

and therefore, uniformly under (0.3),

\[
 \boxed{
 \log\left(e^{2K}{C\log D\over D}\right)
 =\left({1\over2}+o(1)\right)\log m.}
\tag{0.10}
\]

The left side of (0.8) is \(m^{1/2+o(1)}\), not \(o(1)\). For the
canonical choice \(r=\lfloor\lambda\rfloor\), the sharper estimate is

\[
 2e^{-o(1)}\log D
 \le e^{2K}{C\log D\over D}
 \le(2e^2+o(1))\log D.
\tag{0.11}
\]

Even if (0.8) were ignored, the displayed ABKV unmatched-vertex factor is

\[
 B_m
 =K\left({C\log(1+C)\over D}\right)^{1/(K-1)}
 =\boxed{(e^{-3/2}+o(1))\log m},
\tag{0.12}
\]

which diverges instead of tending to zero. The Kostochka--Rodl, Grable,
Vu, and Pippenger--Spencer statements either fix uniformity first or have,
on formal diagonal substitution, a best pair-gap residual factor tending
to \(e^{-2}\), not zero.

Hence the answer to the proposed black-box audit is **no**. The exact
failed hypothesis is (0.8), and the exact failed conclusion scale is
(0.12). A published theorem has not produced an \(o(N)\) leave here.

There is a second, independent physical gate. A hypothetical matching of
\(N-o(N)\) short paths supplies
\((1+o(1))N=(1+o(1))W/\log m\) selected path blocks. If those blocks are
compiled separately, the established endpoint-capped open-path compiler
pays \(H\) initialization letters per block (and a full two-sided cyclic
wrap pays \(2H\)). Thus even the smaller separate-block charge is

\[
 (1+o(1)){H\over\log m}W=\omega(W).
\tag{0.13}
\]

Thus even a new short-path matching theorem would still require a global
endpoint fusion which reduces the final compiled component count to
\(o(W/H)\). Distinct selected paths might already have spliceable endpoints;
the statement is not an architecture-independent lower bound on their
ambient Johnson component count. The matching and collar gates are both
open; the collar is not yet the sole remaining issue.

## 1. Reduced calibration

The exact ratio is

\[
 \lambda_H
 =\prod_{i=1}^{H}{m+i\over m-i+1}.
\tag{1.1}
\]

For \(i\le H=o(m)\), Taylor expansion with a uniform remainder gives

\[
 \log{m+i\over m-i+1}
 ={2i-1\over m}+O\left({i^2\over m^2}+{1\over m^2}\right).
\tag{1.2}
\]

Summing (1.2), and using \(\sum_{i=1}^H(2i-1)=H^2\), yields

\[
 \log\lambda_H
 ={H^2\over m}+O\left({H^3\over m^2}+{H\over m^2}\right).
\tag{1.3}
\]

The floor in the definition of \(H\) changes \(H^2/m\) from
\(\log\log m\) by \(O(H/m)\). Hence

\[
 \log\lambda_H
 =\log\log m
 +O\left({H\over m}+{H^3\over m^2}\right).
\tag{1.4}
\]

The error in (1.4), multiplied by \(\log m\), tends to zero. Exponentiating
proves the sharper form

\[
 \boxed{\lambda_H=\log m+o(1),}
\tag{1.5}
\]

not merely \(\lambda_H\sim\log m\).

For the canonical integer choice

\[
 r_0=\lfloor\lambda_H\rfloor,
\tag{1.6}
\]

one therefore has

\[
 -1+o(1)<r_0-\log m\le o(1).
\]

This is the corresponding one-unit exponential window.

## 2. The physical short-path hypergraph

Let

\[
 \mathcal A=\binom{[2m]}{m-H},
 \qquad
 \mathcal X=\binom{[2m]}m.
\tag{2.1}
\]

For \(A\in\mathcal A\), put

\[
 U_A=[2m]\setminus A,\qquad |U_A|=M.
\tag{2.2}
\]

Choose a directed cyclic order \(\pi\) on \(U_A\), modulo rotation. For
\(i\in\mathbb Z_M\), let \(I_\pi(i,H)\) be the length-\(H\) cyclic
interval beginning at \(i\), and define the middle owner

\[
 X_i(A,\pi)=A\cup I_\pi(i,H).
\tag{2.3}
\]

Choose a cyclic interval \(J\subset\mathbb Z_M\) of \(r\) consecutive
phases and form the rooted physical support

\[
 e(A,\pi,J)
 =\{A\}\mathbin{\dot\cup}\{X_i(A,\pi):i\in J\}.
\tag{2.4}
\]

It has exactly one root and \(r\) distinct owners, hence uniformity

\[
 K=r+1.
\tag{2.5}
\]

Initially there are \((M-1)!\) cyclic orders and \(M\) starts of \(J\),
so every root has \(M!\) formal presentations.

### Lemma 2.1 (short-path representation multiplicity)

Assume \(2\le r\le H\). Every physical support (2.4) has exactly

\[
 \mu_r=2(H-r+1)!(m-r+1)!
\]

formal presentations.

#### Proof

The Johnson-distance-one graph on the retained owners is a path. Thus their
order is recovered up to reversal. Fix one of its two orientations and
write the corresponding residual \(H\)-windows as

\[
 I_0,I_1,\ldots,I_{r-1}.
\]

For \(0\le i\le r-2\), the differences

\[
 I_i\setminus I_{i+1}=\{c_i\},
 \qquad
 I_{i+1}\setminus I_i=\{c_{i+H}\}
\tag{2.6}
\]

recover the labels in positions \(0,\ldots,r-2\) and
\(H,\ldots,H+r-2\) individually. The labels in

\[
 \bigcap_{i=0}^{r-1}I_i
 =\{c_{r-1},\ldots,c_{H-1}\}
\tag{2.7}
\]

form a known set of size \(H-r+1\), but their internal order is invisible.
Likewise, the labels outside the union of the windows occupy

\[
 \{c_{H+r-1},\ldots,c_{M-1}\},
\tag{2.8}
\]

a known set of size \(m-r+1\) with invisible internal order. The two
orders may be chosen independently, giving
\((H-r+1)!(m-r+1)!\) presentations for the fixed path orientation.
Reversal supplies the factor two. No other position is free. \(\square\)

The factor \((H-r+1)!\) is the short-path correction. When a retained path
is longer than \(H\), the common intersection in (2.7) disappears; that is
why the earlier long-path multiplicity has only one invisible block.

Quotient all formal presentations by Lemma 2.1. The result is a simple
physical rooted hypergraph \(\mathcal G_{H,r}\).

## 3. Exact degrees

### Theorem 3.1 (root and owner degrees)

Every root and every owner of \(\mathcal G_{H,r}\) have the degrees in
(0.5). Moreover, for an incident pair \(A\subset X\),

\[
 \boxed{
 d(A,X)
 ={rH!m!\over\mu_r},
 \qquad
 {d(A,X)\over D_R}
 ={r\over\binom MH}.}
\tag{3.1}
\]

If \(A\nsubseteq X\), then \(d(A,X)=0\).

#### Proof

The root formula follows from the \(M!\) formal presentations and Lemma
2.1. Fix an owner \(X\). There are \(\binom mH\) roots \(A\subset X\).
For one such root, exactly \(H!m!\) directed cyclic orders make
\(X\setminus A\) an \(H\)-window, and exactly \(r\) retained phase blocks
contain that window. Division by \(\mu_r\) proves (3.1), and multiplication
by \(\binom mH\) gives

\[
 d(X)
 ={r\over\mu_r}\binom mH H!m!
 ={r(m!)^2\over(m-H)!\mu_r}.
\]

Finally,

\[
 \lambda_H={M!(m-H)!\over(m!)^2},
\]

so \(D_O/D_R=r/\lambda_H\). \(\square\)

For \(r=\lfloor\lambda\rfloor\),

\[
 0\le1-\rho={\lambda-r\over\lambda}<{1\over\lambda}
 =(1+o(1)){1\over\log m}.
\tag{3.2}
\]

This is ordinary \(1+o(1)\) near-regularity, but ABKV uses a much narrower
degree window; see Section 6.3.

## 4. Exact pair-codegree profile

### Theorem 4.1 (all physical pair codegrees)

Two distinct roots have codegree zero. A root--owner pair has (3.1).
Let owners \(X,Y\) have Johnson distance

\[
 d=|X\setminus Y|=|Y\setminus X|.
\]

Then

\[
 \boxed{
 d(X,Y)=
 \begin{cases}
 \displaystyle
 {2(r-d)(d!)^2((m-d)!)^2\over(m-H)!\mu_r},
     &1\le d<r,\\[2mm]
 0,&d\ge r.
 \end{cases}}
\tag{4.1}
\]

Equivalently,

\[
 \boxed{
 {d(X,Y)\over D_O}
 ={2(r-d)\over r\binom md^2}
 \quad(1\le d<r).}
\tag{4.2}
\]

#### Proof

If \(d\le H\), a common root can be chosen in

\[
 \binom{m-d}{H-d}
\tag{4.3}
\]

ways. For a fixed common root, the two residual \(H\)-sets occur as cyclic
windows at separation \(d\) in

\[
 2(d!)^2(H-d)!(m-d)!
\tag{4.4}
\]

directed cyclic orders. A retained interval of \(r\) phases contains both
starts in exactly \(r-d\) positions for each represented orientation when
\(d<r\), and in none when \(d\ge r\). Multiplying (4.3), (4.4), and
\(r-d\), then dividing by \(\mu_r\), gives (4.1). Division by the owner
degree in (0.5) gives (4.2). If \(d>H\), no common root exists; since
\(r\le H\), this is already included in the zero line. \(\square\)

The sequence in (4.2) is maximized at \(d=1\). The root--owner ratio in
(3.1) is exponentially smaller than \(m^{-2}\), because
\(H\to\infty\) and \(H=o(m)\). Therefore

\[
 \Delta_2=d(X,Y)\big|_{d=1}
\]

for all sufficiently large \(m\), and (0.6) follows.

## 5. What an almost-perfect matching would give

Let \(t\) be the size of a matching in \(\mathcal G_{H,r}\), and put

\[
 s_R=N-t.
\]

It misses exactly \(s_R\) roots and leaves

\[
 W-rt
 =N(\lambda-r)+rs_R
\tag{5.1}
\]

middle owners uncovered. Since \(r\sim\lambda\to\infty\),

\[
 s_R=o(N)\quad\Longrightarrow\quad W-rt=o(W).
\tag{5.2}
\]

Conversely, the total number of uncovered vertices of the rooted
hypergraph is

\[
 \begin{aligned}
 L_V
 &=(N+W)-(r+1)t\\
 &=(r+1)(N-t)+N(\lambda-r).
 \end{aligned}
\tag{5.3}
\]

Because \(|V|=(1+\lambda)N=(1+o(1))rN\) and
\(0\le\lambda-r=O(1)\) for the canonical floor choice,

\[
 \boxed{
 L_V=o(|V|)
 \quad\Longleftrightarrow\quad
 N-t=o(N).}
\tag{5.4}
\]

Thus a genuine almost-perfect matching theorem would have exactly the right
owner-leave strength. The failure below is theorem applicability, not a
normalization mismatch.

## 6. Published variable-rank theorem audit

### 6.1 The tempting but insufficient scalar

Since

\[
 \log(W+N)=2m\log2+O(\log m),
\]

(0.6) gives (0.7). This moves the short-path catalogue strictly inside the
frequently quoted scalar boundary

\[
 K\Delta_2\log|V|/D=o(1).
\]

That scalar is not, by itself, a published diagonal theorem with an
\(o(|V|)\) conclusion. Pippenger--Spencer, the classical quantitative
Grable/Kostochka--Rodl statements, and the modern fixed-rank theorems place
the uniformity above the asymptotic degree parameter. Their constants and
error exponents are not uniform under \(K\to\infty\).

For example, the formal pair-gap leftover in the Kostochka--Rodl/Vu scale
contains

\[
 \left({D\over C}\right)^{-1/(K-1)}.
\]

Here

\[
 \log{D\over C}=2\log m-\log2+o(1),
 \qquad K-1=r\sim\log m,
\]

and hence

\[
 \boxed{
 \left({D\over C}\right)^{-1/(K-1)}\longrightarrow e^{-2}.}
\tag{6.1}
\]

Even the formal substitution leaves a positive fraction.

### 6.2 The genuine ABKV growing-uniformity hypothesis

Theorem 3.9 and equation (8) of Alon--Bollobas--Kim--Vu,
*Economical covers with geometric applications*, permit nonconstant \(K\).
In the notation used in that matching statement, the pair-codegree
hypothesis is

\[
 e^{2K}C\log D=o(D).
\tag{6.2}
\]

We now evaluate it without suppressing the decisive constant.

From (0.4)--(0.5),

\[
 D
 ={(m+H)!\over2(H-r+1)!(m-r+1)!}.
\tag{6.3}
\]

Factoring out \(\binom{m+H}{H}\) and using \(r=O(\log m)=o(H)\),

\[
 \begin{aligned}
 \log D
 &=\log\binom{m+H}{H}
   +\log{H!\over(H-r+1)!}
   +\log{m!\over(m-r+1)!}-\log2\\
 &=H\log{m\over H}+H+O(H^2/m+r\log m)\\
 &=(1+o(1))H\log{m\over H}.
 \end{aligned}
\tag{6.4}
\]

Therefore

\[
 \log\log D
 =\log H+\log\log(m/H)+o(1)
 =\left({1\over2}+o(1)\right)\log m.
\tag{6.5}
\]

By (0.6),

\[
 \begin{aligned}
 \log\left(e^{2K}{C\log D\over D}\right)
 &=2(r+1)-2\log m+\log\log D+\log2+o(1)\\
 &=\left({1\over2}+o(1)\right)\log m,
 \end{aligned}
\tag{6.6}
\]

because \(r\sim\log m\). This proves (0.10).

If \(r=\lfloor\lambda\rfloor\), then (1.5) gives

\[
 -o(1)<r+1-\log m\le1+o(1).
\]

Substitution into (6.6) before taking logarithms gives (0.11). Thus the
failure is not a hidden constant in an \(o(1)\): the required quantity
diverges at least as fast as \(2\log D\).

### 6.3 The ABKV degree window is also not automatic

The ABKV degree hypothesis is

\[
 D-f(D)\le d(v)\le D,
 \qquad
 f(D)=20(D^2C\log D)^{1/3}.
\tag{6.7}
\]

Its auxiliary size hypotheses also hold here: \(K>4\),
\(K\le\frac12\log D\), and \(f(D)\le D/10\) for all sufficiently large
\(m\). They are not the source of failure.

With \(D=D_R\), the relative allowance is

\[
 {f(D)\over D}
 =20\left({C\log D\over D}\right)^{1/3}
 =m^{-1/2+o(1)}.
\tag{6.8}
\]

The actual owner deficit is

\[
 1-\rho={\lambda-r\over\lambda}.
\tag{6.9}
\]

For \(r=\lfloor\lambda\rfloor\), (6.7) would require the fractional part
\(\lambda-r\) to be \(m^{-1/2+o(1)}\log m=o(1)\). There is no uniform
arithmetic estimate of this kind. Thus the narrow degree window is a second
unverified hypothesis. One could try to balance lengths \(r,r+1\), split
vertices, or sparsify the two shores; none of those changes the decisive
uniformity and pair-codegree calculation (6.6).

### 6.4 The displayed ABKV leave is quantitatively nonvanishing

The ABKV matching conclusion charges, up to an absolute constant and any
exceptional low-degree vertices, the fraction

\[
 B_m
 =K\left({C\log(1+C)\over D}\right)^{1/(K-1)}.
\tag{6.10}
\]

Since \(C=Dm^{-2+o(1)}\),

\[
 \log(1+C)=\log D+O(\log m)=(1+o(1))\log D.
\]

Equations (6.4)--(6.5) give

\[
 \begin{aligned}
 \log\left({C\log(1+C)\over D}\right)
 &=-2\log m+\log\log D+\log2+o(1)\\
 &=-\left({3\over2}+o(1)\right)\log m.
 \end{aligned}
\tag{6.11}
\]

Dividing by \(K-1=r\sim\log m\) and multiplying by
\(K\sim\log m\) proves (0.12). In particular, the theorem's displayed
upper bound does not even give a vanishing vertex fraction after a
hypothetical repair of (6.2) and (6.7).

### Theorem 6.1 (black-box audit conclusion)

For every integer sequence \(r\sim\lambda_H\), the exact short-path
hypergraph \(\mathcal G_{H,r}\) does not satisfy the ABKV growing-uniformity
condition, and the ABKV displayed leave factor does not tend to zero.
No other audited published theorem has a uniform-in-\(r\) conclusion which
implies \(N-\nu(\mathcal G_{H,r})=o(N)\).

This is a theorem-applicability statement. It does not prove that the
physical hypergraph lacks a matching of size \(N-o(N)\).

## 7. Exact collar and component consequence

Assume conditionally that some new argument finds a matching of size

\[
 t=N-o(N).
\tag{7.1}
\]

Then (5.1) gives \(o(W)\) middle leave. The matching supplies \(t\)
owner-disjoint physical path blocks, each with only \(r\sim\log m\)
retained owners. If they are compiled separately, the established
endpoint-capped open-path implementation pays \(H\) initialization letters
per block. If every block is instead fully wrapped, the charge is \(2H\).
Hence the established separate-block charge lies between

\[
 Ht=(1+o(1)){H\over\lambda}W
 \quad\hbox{and}\quad
 2Ht=(2+o(1)){H\over\lambda}W.
\tag{7.2}
\]

At the reduced scale,

\[
 {H\over\lambda}
 =(1+o(1)){\sqrt{m\log\log m}\over\log m}\longrightarrow\infty.
\tag{7.3}
\]

Thus (7.2) is \(\omega(W)\). Equivalently,

\[
 {t\over W/H}
 =(1+o(1)){H\over\log m}\longrightarrow\infty.
\tag{7.4}
\]

The compiler needs \(o(W/H)\) final compiled components, whereas the
unfused short-path matching presents \(\Theta(W/\log m)\) blocks. This does
not exclude endpoint adjacencies or direct splices between distinct selected
paths; exploiting them is exactly the required fusion theorem.

A positive route would therefore need both:

1. a new object-specific matching or absorber giving \(o(N)\) root leave;
2. an endpoint fusion/circulation which concatenates a diverging number of
   matched short paths per final component while preserving owner and trace
   disjointness.

No such fusion follows from the matching incidence calculation. Therefore
the reduced scale does not isolate the collar as the sole gate: the
published matching theorem already fails first.

## 8. Exact proved/conditional boundary

Proved:

1. \(\lambda_H=\log m+o(1)\) at
   \(H=\lfloor\sqrt{m\log\log m}\rfloor\);
2. the corrected short-path multiplicity (0.4);
3. the exact physical degrees (0.5), root--owner codegree (3.1), and all
   owner-pair codegrees (4.1);
4. the sharp maximum relative pair codegree (0.6);
5. an almost-perfect vertex matching would be equivalent to an \(o(N)\)
   root leave and would give \(o(W)\) middle leave;
6. the genuine ABKV growing-uniformity hypothesis fails by (0.10), its
   narrow degree window is unverified, and its displayed residual factor is
   (0.12);
7. separate literal compilation would pay the superlinear collar (0.13).

Not proved:

1. a lower bound excluding a matching of size \(N-o(N)\);
2. a catalogue-specific nibble, absorber, or deterministic flow finding
   such a matching;
3. a global endpoint fusion reducing \(\Theta(W/\log m)\) matched paths to
   \(o(W/H)\) components;
4. simultaneous signed-rank trace disjointness after such a fusion.

Accordingly this reduced scale is a useful exact test case, but it is not a
published-nibble shortcut to constant one.

## 9. Independent audit record

An independent derivation verified:

1. the two invisible-block multiplicity
   \(2(H-r+1)!(m-r+1)!\);
2. every root, owner, root--owner, and owner--owner incidence formula;
3. \(\lambda_H=\log m+o(1)\), including the floor in \(H\);
4. the ABKV formal-hypothesis exponent
   \((\frac12+o(1))\log m\);
5. the leave factor \((e^{-3/2}+o(1))\log m\); and
6. the conditional separate-block collar \(Ht=\omega(W)\).

The audit supplied the nonincident root--owner zero case, the corrected
floor inequality before (0.11), the auxiliary ABKV size checks in Section
6.3, and the separate-block qualification in Section 7. All are incorporated
above. No fatal error remains in the stated theorem-applicability result.
