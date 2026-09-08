# The terminal PBBS coefficient is the reflection of a nonnegative mean-D ballot profile

**Date:** 2026-08-07
**Status:** unconditional exact normal form for every terminal even volume
seed (with the depth-one endpoint handled separately).  The theorem turns
the full all-price question into one explicit fractional fragmentation
kernel between the two sides of a single nonnegative ballot distribution.
It does not construct that kernel and therefore does not prove the
all-depth configuration inequality.

## 1. Terminal volumes and a ratio below two

Put

\[
 C_r={2r\choose r},\qquad
 V_{r,D}=D C_r-\sum_{s=1}^{r-1}{2r\choose s}.
\tag{1.1}
\]

By symmetry,

\[
 \boxed{V_{r,D}=\left(D+{1\over2}\right)C_r-2^{2r-1}+1.}
\tag{1.2}
\]

Let \(r=r_D\) be terminal:

\[
 V_{r,D}>0,\qquad V_{r+1,D}\le0.
\tag{1.3}
\]

For \(D\ge2\), one has

\[
 \boxed{r\ge\max\{D(D+1),\,2D+3\}.}
\tag{1.4}
\]

Indeed, write \(R_m=4^m/C_m\).  The exact recurrence is

\[
 {R_{m+1}\over R_m}={2m+2\over2m+1}.
\tag{1.5}
\]

The base inequality

\[
 R_7={2048\over429}<5
\tag{1.6}
\]

and

\[
 (2D+1){(4D+8)(4D+10)\over(4D+7)(4D+9)}<2D+3
\tag{1.7}
\]

show inductively that

\[
 R_{2D+3}<2D+1\qquad(D\ge2).
\tag{1.8}
\]

Substitution in

\[
 {V_{m,D}\over C_m}=D+{1\over2}-{R_m\over2}+{1\over C_m}
\tag{1.9}
\]

gives \(V_{2D+3,D}>0\), proving the linear half of (1.4).

For completeness, the quadratic half of (1.4) is equally elementary.
The recurrence (1.5) proves inductively that

\[
 R_m\le2\sqrt m,
\tag{1.9a}
\]

with strict inequality for \(m>1\), because

\[
 \left({2m+2\over2m+1}\right)^2\le {m+1\over m}.
\tag{1.9b}
\]

At \(m=D(D+1)\),

\[
 R_m<2\sqrt{D(D+1)}<2D+1.
\tag{1.9c}
\]

Equation (1.9) again gives \(V_{m,D}>0\), hence
\(r\ge D(D+1)\).

The terminal condition has a second consequence which will be decisive.

### Lemma 1.1 (terminal weight positivity)

For every terminal pair with \(D\ge2\),

\[
 \boxed{
 0<{V_{r,D}\over V_{r-1,D}}<2,
 \qquad
 U_{r,D}:=2V_{r-1,D}-V_{r,D}>0.}
\tag{1.10}
\]

#### Proof

Only the upper bound needs proof.  Put \(d=D+1/2\) and
\(C=C_{r-1}\).  Since

\[
 {C_r\over C}=4-{2\over r},
\tag{1.11}
\]

equation (1.2) gives

\[
 2V_{r-1,D}-V_{r,D}
 =4^{r-1}+1-{2(r-1)\over r}dC.
\tag{1.12}
\]

Terminality at \(r+1\) gives

\[
 d\le {2\cdot4^r-1\over C_{r+1}}.
\tag{1.13}
\]

Moreover,

\[
 {C_{r+1}\over C}
 ={4(4r^2-1)\over r(r+1)}.
\tag{1.14}
\]

Consequently the last term in (1.12) is at most

\[
 {(r^2-1)(2\cdot4^r-1)\over2(4r^2-1)}
 <4^{r-1}+1.
\tag{1.15}
\]

The strict inequality follows after clearing the positive denominator;
the right side minus the left side has numerator

\[
 6\cdot4^{r-1}+9r^2-3>0.
\tag{1.16}
\]

Thus (1.12) is positive.  Positivity of both terminal volumes gives the
lower bound in (1.10). \(\square\)

## 2. The modified ballot profile

Let

\[
 H_s^{(2m)}={2m\choose s}-{2m\choose s-1}.
\tag{2.1}
\]

The PBBS rank-one convention is encoded by the finite profile

\[
 b_m(j)=
 \begin{cases}
 H_{m-j}^{(2m)},&0\le j\le m-2,\\
 2m,&j=m-1,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{2.2}
\]

For a terminal parent \(r\), define

\[
 \boxed{
 \mathcal A_j
 =V_{r-1,D}b_r(j)-V_{r,D}b_{r-1}(j)
 \qquad(0\le j\le r-1).}
\tag{2.3}
\]

Thus the child term at \(j=r-1\) is genuinely zero; it is not an
artificial rank-zero ballot term.  At \(j=r-2\), the child term is the
modified rank-one value \(2r-2\).

### Theorem 2.1 (nonnegative centered ballot profile)

For every terminal pair with \(D\ge2\),

\[
 \boxed{\mathcal A_j>0\qquad(0\le j\le r-1).}
\tag{2.4}
\]

#### Proof

Write

\[
 \lambda={V_{r,D}\over V_{r-1,D}}<2.
\tag{2.5}
\]

For \(0\le j\le r-3\), put \(s=r-j\), so \(3\le s\le r\).  The exact
two-row ballot ratio is

\[
 {H_s^{(2r)}\over H_{s-1}^{(2r-2)}}
 ={(2r)(2r-1)\over s(2r+1-s)}.
\tag{2.6}
\]

The denominator increases on \(s\le r\), so the last ratio is at least

\[
 {2(2r-1)\over r+1}>2
\tag{2.7}
\]

because \(r\ge2D+3\ge7\).  Equations (2.3), (2.5), and (2.6) prove
positivity on this range.

At the penultimate index the modified child boundary gives

\[
 {\mathcal A_{r-2}\over V_{r-1,D}}
 =H_2^{(2r)}-\lambda(2r-2)
 >r(2r-3)-2(2r-2)>0.
\tag{2.8}
\]

Finally,

\[
 \mathcal A_{r-1}=2rV_{r-1,D}>0.
\tag{2.9}
\]

This includes both rank-one support conventions exactly. \(\square\)

The interior profile has a second global shape property.

### Proposition 2.2 (strict interior log-concavity)

The unmodified segment

\[
 \mathcal A_0,\mathcal A_1,\ldots,\mathcal A_{r-3}
\tag{2.10}
\]

is strictly log-concave:

\[
 \boxed{
 \mathcal A_j^2>mathcal A_{j-1}\mathcal A_{j+1}
 \qquad(1\le j\le r-4).}
\tag{2.11}
\]

In particular, because \(2D\le r-3\), every pair of profile values
\(\mathcal A_{D-L},\mathcal A_{D+L}\) with \(1\le L\le D\) lies inside
one positive log-concave segment.

#### Proof

Put

\[
 h_j=H_{r-j}^{(2r)},\qquad
 \beta={\lambda\over2r(2r-1)},\qquad
 \alpha=1-\beta r(r+1).
\tag{2.12}
\]

The ratio (2.6) gives, for \(0\le j\le r-3\),

\[
 {\mathcal A_j\over V_{r-1,D}}
 =h_j f_j,
 \qquad
 f_j=\alpha+\beta j(j+1).
\tag{2.13}
\]

Since \(0<\lambda<2\),

\[
 \alpha>{r-2\over2r-1},
 \qquad
 {\beta\over\alpha}<{1\over r(r-2)}.
\tag{2.14}
\]

A direct multiplication gives

\[
 f_{j-1}f_{j+1}
 =f_j^2+2\beta\bigl(\alpha-\beta j(j+1)\bigr)
 \le f_j^2\left(1+{2\beta\over\alpha}\right).
\tag{2.15}
\]

On the other hand,

\[
 {h_{j+1}\over h_j}
 ={(2j+3)(r-j)\over(2j+1)(r+j+2)},
\tag{2.16}
\]

and therefore

\[
\begin{aligned}
 {h_j^2\over h_{j-1}h_{j+1}}
 &={ (2j+1)^2(r-j+1)(r+j+2)
     \over
     (2j-1)(2j+3)(r-j)(r+j+1)}\\
 &>1+{1\over r}
 \ge1+{2\over r(r-2)}.
\end{aligned}
\tag{2.17}
\]

Combine (2.14)--(2.17).  The strict log-concavity margin of \(h_j\)
dominates the possible log-convexity of \(f_j\), proving (2.11).
\(\square\)

## 3. Exact reflection and exact mean

Let \(\nu_{r,D}(L)\) be the complete PBBS birth row in dimension \(2r\):

\[
 \nu_{r,D}(L)
 =\mathbf1_{1\le L\le D}H_{r-D+L}^{(2r)}
  -\widetilde H_{r-D-L}^{(2r)}
\tag{3.1}
\]

on \(1\le L\le r-D-1\), and zero outside that range, where
\(\widetilde H_1^{(2r)}=2r\).  Define the scaled volume-normalized
coefficient

\[
 \widehat\mu_L
 =V_{r-1,D}\nu_{r,D}(L)
  -V_{r,D}\nu_{r-1,D}(L).
\tag{3.2}
\]

### Theorem 3.1 (reflected-profile identity)

With \(\mathcal A_j=0\) outside \(0\le j\le r-1\), one has, for every
\(L\ge1\),

\[
 \boxed{
 \widehat\mu_L
 =\mathbf1_{L\le D}\mathcal A_{D-L}
  -\mathcal A_{D+L}.}
\tag{3.3}
\]

Moreover,

\[
 \boxed{
 \sum_{j=0}^{r-1}(j-D)\mathcal A_j=0,
 \qquad
 {\sum_jj\mathcal A_j\over\sum_j\mathcal A_j}=D.}
\tag{3.4}
\]

#### Proof

For the positive birth in (3.1), set \(j=D-L\).  For the negative birth,
set \(j=D+L\).  Equation (2.2) reproduces the ordinary ballot terms, the
modified child rank-one term at \(j=r-2\), the modified parent rank-one
term at \(j=r-1\), and the child's absent rank-zero term.  This proves
(3.3), including both support endpoints.

The birth-volume identity gives

\[
 \sum_LL\widehat\mu_L=0.
\tag{3.5}
\]

Insert (3.3) and change variables on its two sides:

\[
 \sum_{j<D}(D-j)\mathcal A_j
 =\sum_{j>D}(j-D)\mathcal A_j.
\tag{3.6}
\]

The central term \(j=D\) has zero coefficient, so (3.6) is exactly
(3.4). \(\square\)

Thus the signed PBBS coefficient is not an opaque two-row difference.  It
is the reflection, about the exact mean \(D\), of one nonnegative
integer-valued profile.

## 4. Pascal and Catalan first-return forms

Let

\[
 B_j=H_{r-1-j}^{(2r-2)}.
\tag{4.1}
\]

Away from the two rank-one endpoints, two-step Pascal gives

\[
 \boxed{
 \mathcal A_j
 =V_{r-1,D}B_{j-1}
  +U_{r,D}B_j
  +V_{r-1,D}B_{j+1}
 \qquad(1\le j\le r-3),}
\tag{4.2}
\]

where every coefficient is positive by Lemma 1.1.  Thus the whole
interior profile is a positive \((1,\rho,1)\) mixture of one child ballot
row, with

\[
 \rho={U_{r,D}\over V_{r-1,D}}=2-\lambda>0.
\tag{4.3}
\]

Let \(C(z)=1+zC(z)^2\) be the Catalan generating function.  The standard
forest identity is

\[
 H_{r-j}^{(2r)}=[z^{r-j}]C(z)^{2j+1}.
\tag{4.4}
\]

Hence, again away from the modified rank-one endpoint,

\[
 \boxed{
 \mathcal A_j
 =V_{r-1,D}[z^{r-j}]
 C(z)^{2j+1}(1-\lambda z).}
\tag{4.5}
\]

Equations (4.2) and (4.5) are the exact first-return hook.  A ballot path
ending at height \(2j\) is an ordered forest of \(2j+1\) plane trees;
the desired all-depth proof must use that forest structure to transport
the right-of-mean objects to partitions of left-of-mean deficits.

There is a sharper bilateral form.  Put

\[
 X=C(z)-1=zC(z)^2,
 \qquad M=r-D,
\tag{4.6}
\]

and define the Laurent coefficient functional

\[
 \mathscr L(F)
 =V_{r-1,D}[z^M]
 C(z)^{2D+1}(1-\lambda z)F(X).
\tag{4.7}
\]

For every index \(j=D+k\) at which neither rank-one modification is
active,

\[
 \boxed{\mathcal A_{D+k}=\mathscr L(X^k).}
\tag{4.8}
\]

Indeed, \(X^k=z^kC^{2k}\), so (4.8) is exactly (4.5) after shifting the
coefficient by \(k\).  Thus left deficits and right excesses are the
negative and positive Laurent moments of one Catalan coefficient
functional:

\[
 s_i=\mathscr L(X^{-i}),
 \qquad d_L=\mathscr L(X^L),
\tag{4.9}
\]

apart from the two explicitly known terminal rank-one corrections.

The Catalan change of variables

\[
 z={X\over(1+X)^2}
\tag{4.10}
\]

turns (4.7) into ordinary coefficient extraction:

\[
 \boxed{
 {\mathcal A_{D+k}\over V_{r-1,D}}
 =[X^{M-k}](1-X)(1+X)^{2r-2}
       (1+\rho X+X^2),}
\tag{4.11}
\]

again off the two modified endpoints, where
\(\rho=2-\lambda>0\).  The factor

\[
 Q(X)=(1+X)^{2r-2}(1+\rho X+X^2)
\tag{4.12}
\]

is positive-coefficient and palindromic.  Hence the centered ballot law
is the lower-half discrete gradient of one symmetric weighted-binomial
row.  Formula (4.11) makes the involution \(X\leftrightarrow X^{-1}\)
behind the desired first/last-return coupling completely explicit; what
is still missing is a positivity-preserving disintegration of its
positive Laurent moments into the negative ones with the partition
marginals (5.5).

## 5. Exact primal fragmentation gate

For a nonnegative closed min-plus price \(\psi\), equation (3.3) gives

\[
\boxed{
 \sum_L\widehat\mu_L\psi(L)
 =\sum_{i=1}^{D}\mathcal A_{D-i}\psi(i)
  -\sum_{L\ge1}\mathcal A_{D+L}\psi(L).}
\tag{5.1}
\]

Define the left supplies and right jobs

\[
 s_i=\mathcal A_{D-i}\quad(1\le i\le D),
 \qquad
 d_L=\mathcal A_{D+L}\quad(L\ge1).
\tag{5.2}
\]

Their exact volumes agree:

\[
 \boxed{\sum_{i=1}^{D}is_i=\sum_{L\ge1}Ld_L.}
\tag{5.3}
\]

Let \(\mathscr P_D(L)\) be the finite set of integer partitions of
\(L\) into parts in \(\{1,\ldots,D\}\), and let \(m_i(\pi)\) be the
multiplicity of part \(i\) in \(\pi\).  An explicit fractional
first-return kernel would be a family

\[
 x_{L,\pi}\ge0
 \qquad(L\ge1,\ \pi\in\mathscr P_D(L))
\tag{5.4}
\]

satisfying

\[
 \boxed{
 \sum_{\pi\in\mathscr P_D(L)}x_{L,\pi}=d_L,
 \qquad
 \sum_{L,\pi}m_i(\pi)x_{L,\pi}=s_i
 \quad(1\le i\le D).}
\tag{5.5}
\]

The second equality could be weakened to \(\le s_i\): by (5.3), exact
job coverage forces every inequality back to equality.

If (5.5) holds, then subadditivity gives the termwise certificate

\[
\begin{aligned}
 \sum_L\widehat\mu_L\psi(L)
 &=\sum_{L,\pi}x_{L,\pi}
   \left(\sum_{i=1}^{D}m_i(\pi)\psi(i)-\psi(L)\right)\\
 &\ge0.
\end{aligned}
\tag{5.6}
\]

Equivalently, (5.6) is a nonnegative decomposition into general partition
atoms

\[
 \sum_i m_i(\pi)[i]-[L].
\tag{5.7}
\]

Binary refinement would further decompose each of these into atoms
\([a]+[b]-[a+b]\).

There is an equivalent ordered-composition DAG with fewer indices.  Its
vertices are the nonnegative residual lengths.  For

\[
 1\le i\le\min(D,u),
\tag{5.8}
\]

let \(y_{u,i}\ge0\) be the flow on the edge

\[
 u\longrightarrow u-i.
\tag{5.9}
\]

Then (5.5) is equivalent to the existence of a flow satisfying

\[
 \boxed{
 \sum_{i\le\min(D,u)}y_{u,i}
 -\sum_{i=1}^{D}y_{u+i,i}=d_u
 \qquad(u\ge1),}
\tag{5.10}
\]

and the global edge-type marginals

\[
 \boxed{
 \sum_{u\ge i}y_{u,i}=s_i
 \qquad(1\le i\le D).}
\tag{5.11}
\]

Indeed, every ordered partition of \(L\) is a directed path from \(L\)
to zero.  Conversely, the graph is acyclic, so every nonnegative flow
with sources \(d_L\) decomposes fractionally into such paths.  Forgetting
the order on each path gives (5.4)--(5.5).  This is the most economical
form in which a Catalan first-return branching rule could be written: one
needs nonnegative \(y_{u,i}\) whose divergence is the positive Laurent
moment \(\mathscr L(X^u)\) and whose total flow of step length \(i\) is
the negative Laurent moment \(\mathscr L(X^{-i})\).

### Proposition 5.1 (the homogeneous renewal kernel is already false)

A particularly attractive rank-one specialization of the DAG does not
work.  Pointwise cancel common supply and demand at the same length, and
write the residual vectors again as \(s_i,d_L\).  Put

\[
 S=\sum_i s_i,qquad B=\sum_Ld_L,qquad
 P(z)={1\over S}\sum_i s_i z^i,qquad
 D(z)=\sum_Ld_Lz^L.
\tag{5.12}
\]

If

\[
 G(z)={B-D(z)\over1-P(z)}=\sum_{t\ge0}g_tz^t
\tag{5.13}
\]

had nonnegative coefficients, then the state-independent forward flow

\[
 t\longrightarrow t+i
 \quad\text{of size}\quad
 g_t{s_i\over S}
\tag{5.14}
\]

would terminate mass \(d_t\) at state \(t\).  Equal volume gives, by the
limit at \(z=1\),

\[
 \sum_tg_t=S,
\tag{5.15}
\]

so its global step-\(i\) marginal would be exactly \(s_i\).  This would
solve (5.10)--(5.11) with one state-independent step law.

It fails at the first nontrivial terminal example.  For \(D=2,r=7\),

\[
 (V_{6,2},V_{7,2})=(263,389)
\tag{5.16}
\]

and direct substitution in (2.3) gives

\[
 (\mathcal A_0,\ldots,\mathcal A_6)
 =(61479,147730,156288,107625,50793,15583,3682).
\tag{5.17}
\]

Hence

\[
 (\widehat\mu_1,\widehat\mu_2,
   \widehat\mu_3,\widehat\mu_4)
 =(40105,10686,-15583,-3682).
\tag{5.18}
\]

Thus

\[
 (s_1,s_2)=(40105,10686),
 \quad(d_3,d_4)=(15583,3682),
 \quad(S,B)=(50791,19265).
\tag{5.19}
\]

The recurrence

\[
 g_t={40105\over50791}g_{t-1}
     +{10686\over50791}g_{t-2}-d_t,
 \qquad g_0=19265,
\tag{5.20}
\]

has

\[
\boxed{
 g_4=
 {-423057099229214929752\over50791^4}<0.}
\tag{5.21}
\]

The numerator in (5.21) is the exact integer

\[
\begin{aligned}
 &B(s_1^4+3s_1^2s_2S+s_2^2S^2)\\
 &\hspace{18mm}-d_3s_1S^3-d_4S^4.
\end{aligned}
\tag{5.22}
\]

There is no numerical optimization in this obstruction.  The depth-two
configuration inequality itself is true; (5.21) proves only that its
fragmentation cannot use the iid/state-independent renewal law (5.14).
A successful first-return kernel must be state-dependent or multitype.
For comparison, an exact state-dependent fragmentation at these same
numbers is

\[
\begin{array}{c|c|r}
L&\text{partition}&\text{mass}\\ \hline
4&2+2&3682\\
3&1+2&3322\\
3&1+1+1&12261.
\end{array}
\tag{5.23}
\]

It uses

\[
 3322+3(12261)=40105
\tag{5.24}
\]

parts of size one and

\[
 3322+2(3682)=10686
\tag{5.25}
\]

parts of size two.  Thus the no-go is sharply about homogeneous renewal,
not about the DAG formulation or the underlying PBBS inequality.

This is the exact remaining constructive theorem.  Positivity and the
mean identity of \(\mathcal A\) prove only the scalar capacity balance;
they do not by themselves produce the integer-partition marginals in
(5.5).  The Catalan forest representation (4.4), rather than generic
mean or one-crossing information, is the available extra structure.

## 6. Equivalent clock/compression target

Put

\[
 G(q)=\sum_{L\ge q}\widehat\mu_L
 =\sum_{j\le D-q}\mathcal A_j
  -\sum_{j\ge D+q}\mathcal A_j.
\tag{6.1}
\]

For \(a_q=\psi(q)-\psi(q-1)\), summation by parts gives

\[
 \sum_L\widehat\mu_L\psi(L)=\sum_{q\ge1}G(q)a_q.
\tag{6.2}
\]

After integer quantization, the Stieltjes atoms of a closed subadditive
price occur at positions \(1+x_0,1+x_1,\ldots\), where

\[
 0=x_0\le x_1\le\cdots,
 \qquad x_{m+n}\ge x_m+x_n.
\tag{6.3}
\]

Thus the same missing theorem is

\[
 \boxed{
 \sum_{n\ge0}G(1+x_n)\ge0
 \quad\text{for every nondecreasing superadditive clock }x.}
\tag{6.4}
\]

Arithmetic clocks \(x_n=nh\) are precisely the one-denomination ceiling
prices.  An objective-specific compression to arithmetic clocks would
prove (6.4), but strict TP2 of the two raw ballot rows supplies only the
one-crossing property of \(\widehat\mu\); it does not itself justify such
a nonlinear clock compression.

## 7. Honest frontier

The unconditional gain is global and exact:

1. the rank-one conventions fit one reflected profile, rather than being
   exceptional signed errors;
2. terminality supplies the positive middle Pascal weight
   \(U_{r,D}>0\) for every depth;
3. the entire coefficient measure is the reflection of a positive ballot
   law with exact mean \(D\); and
4. the configuration theorem is reduced to the explicit marginal system
   (5.5), or equivalently the clock inequality (6.4).

What remains is not another sign scan or a finite-residue calculation.  It
is a genuine Catalan first-return/last-return coupling, or an
objective-specific compression theorem strong enough to imply (6.4).
