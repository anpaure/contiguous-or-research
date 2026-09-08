# Promotion-ring columns: exact high-harmonic covariance, top-degree concentration, and a load-only LM no-go

Date: 2026-07-26

Method: pure mathematics. No computation or external search is used.

## 0. Outcome

Let

\[
 n=2m,\qquad M=m+H,\qquad 2\le H<m,
 \qquad B=\binom MH,\qquad p={M\over B}.
\]

Inside one rank-\(M\) top, identify a selected middle \(m\)-set with
the complementary omitted \(H\)-set.  One cyclic frame is therefore the
incidence vector of the \(M\) cyclic \(H\)-windows of an \(M\)-cycle.

This note proves four facts.

1.  The exact covariance of a uniform cyclic-frame column is diagonal on
    the Johnson harmonics.  Its eigenvalues are given by the triangular
    recursion (2.6) below.  In particular the degree-two eigenvalue is

    \[
    \boxed{
    \kappa _2
      ={p(M-2)\bigl((2H-1)(M-1)-3H(H-1)\bigr)
        \over3(M-H)(M-H-1)}.}
    \tag{0.1}
    \]

    If \(H\to\infty\), \(H=o(M)\), then, for every fixed \(j\ge2\),

    \[
    \boxed{\kappa_j=\left({2\over j+1}+o_j(1)\right)Hp.}
    \tag{0.2}
    \]

2.  Nevertheless the covariance is overwhelmingly not of bounded
    degree.  If \(a_j\) is the squared norm of one centered column in
    local Johnson degree \(j\), then the exact first spectral-moment
    identity is

    \[
    \boxed{
      \sum_{j=2}^{H}j(M-j+1)a_j=M(mH-2).}
    \tag{0.3}
    \]

    Consequently

    \[
    \boxed{
    \sum_{j=2}^{H-1}(H-j)(m+1-j)a_j
      =M\bigl(H+2-pH(m+1)\bigr),}
    \tag{0.4}
    \]

    and hence

    \[
    \boxed{
    a_H\ge M(1-p)-{M(H+2)\over m-H+2}.}
    \tag{0.5}
    \]

    Thus, for \(H=o(m)\), one physical cyclic column has

    \[
                       a_H=M-O(H),
    \tag{0.6}
    \]

    so a \(1-O(H/m)\) fraction of its centered squared norm lies in the
    *highest* local harmonic \(E_H\).  At the tuned critical height, every
    fixed collection of Johnson degrees carries \(o(1)\) of the column
    norm.

3.  For one frame per top, this produces a statewise diagonal restitution
    of \((1-o(1))W\), already in the local \(E_H\) pieces.  It is not an
    aggregate separation: the floor-corrected collision is small exactly
    when cross-top inner products cancel this diagonal by
    \(-(1/2+o(1))W\).  Local projectors \(E_H(U)\) depend on the top \(U\),
    so (0.5) supplies no sign for these cross terms.

4.  There is a sharp no-go for every **load-only** local-minimum
    inequality based on actual cyclic-frame scores.  In the exact tuned
    floor and point-margin affine lattice there is an integral load
    \(\mu\) with

    \[
       \Psi(\mu)=2\binom{2m-4}{m-2}
                 =\left({1\over8}+o(1)\right)W,
    \tag{0.7}
    \]

    while its total one-top cyclic-score spread is \(o(W)\).  Therefore
    no inequality of the form

    \[
        \Psi(\mu)\le C\sum_U
        \left(\mathbb E_\pi\langle\mu,v_{U,\pi}\rangle
             -\min_\pi\langle\mu,v_{U,\pi}\rangle\right)+o(W)
    \tag{0.8}
    \]

    can hold on the exact floor/point-margin lattice, for any fixed
    \(C\).  This counterexample is in fact not the load of an integral
    one-frame-per-top selection when \(H=o(m)\): every physical selection
    has only \(O(HN)=o(W)\) correlation with its defining four-coordinate
    harmonic, whereas this load has \((1/4+o(1))W\) correlation.  The
    distinction is decisive:
    replacing \(\mu\) by the external load \(\mu-v_U\) adds the exact
    self-column spread \(M(1-p)\) in every fibre, totalling
    \((1+o(1))W\).

The proved conclusion is therefore a reduction, not a constant-one
theorem and not a physical bad local minimum.  Bounded Johnson degree and
load-only score spread cannot obstruct.  A surviving positive-cut theorem
must be owner-sensitive and must control cross-fibre correlations in the
growing local degrees \(j=H-O(1)\), using legal compound exchanges that
remove the \((1-o(1))W\) self-column restitution.

## 1. One-top column and harmonic notation

Fix an \(M\)-set \(U\).  For an oriented cyclic order \(\pi\) on \(U\),
let \(\mathcal D_\pi\subseteq\binom UH\) be its \(M\) cyclic
\(H\)-windows and put

\[
        c_\pi=\mathbf1_{\mathcal D_\pi},\qquad
        z_\pi=c_\pi-p\mathbf1,\qquad p={M\over B}.
\tag{1.1}
\]

Complementation identifies this with the vector of the \(M\) selected
middle \(m\)-windows.  Let

\[
 \mathbb R^{\binom UH}=E_0\perp E_1\perp\cdots\perp E_H
\tag{1.2}
\]

be the multiplicity-free Johnson decomposition, and write

\[
 d_j=\dim E_j=\binom Mj-\binom M{j-1},\qquad
 a_j=\|P_jc_\pi\|_2^2.
\tag{1.3}
\]

The number \(a_j\) does not depend on \(\pi\).  Since every coordinate
of \(U\) lies in exactly \(H\) members of \(\mathcal D_\pi\),

\[
 a_0={M^2\over B},\qquad a_1=0,
 \qquad \|z_\pi\|_2^2=M-{M^2\over B}=M(1-p).
\tag{1.4}
\]

Define the uniform centered covariance

\[
             K=\mathbb E_\pi z_\pi z_\pi^{\mathsf T}.
\tag{1.5}
\]

The average is invariant under \(S_U\).  Schur's lemma in the
multiplicity-free decomposition (1.2) gives

\[
 K|_{E_0}=K|_{E_1}=0,
 \qquad
 \boxed{K|_{E_j}=\kappa_j I_{E_j},\quad
        \kappa_j={a_j\over d_j}\quad(2\le j\le H).}
\tag{1.6}
\]

This is an averaged covariance identity.  It does not say that the
harmonic coordinates of two independently chosen legal replacements can
be chosen separately.

## 2. Exact covariance recursion

For \(1\le \ell\le H\), let \(I_{\ell,H}\) be the inclusion matrix from
\(H\)-sets to \(\ell\)-sets, and put

\[
 T_\ell=\|I_{\ell,H}c_\pi\|_2^2
 =\sum_{A,B\in\mathcal D_\pi}\binom{|A\cap B|}{\ell}.
\tag{2.1}
\]

Because \(2H<M\), two cyclic \(H\)-windows have intersection size
\(H-d\) for the two shifts of distance \(d\), \(1\le d<H\), and are
disjoint for all remaining shifts.  Hence the hockey-stick identity gives

\[
 \boxed{
 T_\ell=M\left(\binom H\ell+2\binom H{\ell+1}\right)
 \quad(1\le\ell\le H).}
\tag{2.2}
\]

Also \(T_0=M^2\).

The elementary up-down calculation for the Boolean inclusion matrices
gives

\[
 I_{\ell,H}^{\mathsf T}I_{\ell,H}|_{E_j}
   =\gamma_{\ell j}I_{E_j},
 \qquad
 \gamma_{\ell j}
   =\binom{H-j}{\ell-j}
      \binom{M-\ell-j}{H-\ell}
 \quad(0\le j\le\ell).
\tag{2.3}
\]

Indeed, the left side has kernel \(\binom{|A\cap B|}{\ell}\); applying
one down operator successively to a degree-\(j\) harmonic gives the two
falling-factorial multipliers in (2.3).  Therefore

\[
 T_\ell=\sum_{j=0}^{\ell}\gamma_{\ell j}a_j.
\tag{2.4}
\]

Since

\[
 \gamma_{\ell\ell}=\binom{M-2\ell}{H-\ell}>0,
\tag{2.5}
\]

(2.2)--(2.4) give the exact triangular recursion

\[
 \boxed{
 a_\ell={
 M\left(\binom H\ell+2\binom H{\ell+1}\right)
 -\sum_{j=0}^{\ell-1}
   \binom{H-j}{\ell-j}
   \binom{M-\ell-j}{H-\ell}a_j
 \over
 \binom{M-2\ell}{H-\ell}}.}
\tag{2.6}
\]

Together with (1.4), this determines every covariance eigenvalue exactly.
For \(\ell=2\), direct simplification gives

\[
 a_2={M H(H-1)A\over
       6(M-1)\binom{M-4}{H-2}},
 \qquad
 A=(2H-1)(M-1)-3H(H-1).
\tag{2.7}
\]

Since \(d_2=M(M-3)/2\) and

\[
 \binom{M-4}{H-2}
 =B\,{H(H-1)(M-H)(M-H-1)
       \over M(M-1)(M-2)(M-3)},
\tag{2.8}
\]

(2.7) is exactly (0.1).

For completeness, fix \(j\ge2\) and let \(H\to\infty\), \(H=o(M)\).
Then

\[
 T_j=\left({2\over(j+1)!}+o_j(1)\right)MH^{j+1},
\qquad
 \gamma_{jj}=(1+o_j(1))B\left({H\over M}\right)^j.
\tag{2.9}
\]

Inductively, \(a_i=O_i(M^{i+1}H/B)\) for fixed \(2\le i<j\).
The \(i\)-term in (2.4) is then smaller than \(T_j\) by
\(O_j((H/M)^{j-i})\); the \(i=0\) term is smaller by
\(O_j((H/M)^{j-1})\), and \(a_1=0\).  Thus

\[
 a_j=\left({2\over(j+1)!}+o_j(1)\right){M^{j+1}H\over B}.
\tag{2.10}
\]

Since \(d_j=(1+o_j(1))M^j/j!\), equation (0.2) follows.

## 3. The covariance mass is at degree \(H\)

Let \(\tau\) range over the unordered coordinate transpositions of \(U\).
On \(E_j\), the transposition Laplacian is

\[
 \sum_\tau(I-\tau)=j(M-j+1)I.
\tag{3.1}
\]

Equivalently, this is the usual Johnson Laplacian: a transposition crossing
an \(H\)-set and its complement gives one Johnson neighbour, while the
other transpositions are self-loops.  Therefore

\[
 \sum_\tau\|\tau z_\pi-z_\pi\|_2^2
 =2\sum_{j=2}^Hj(M-j+1)a_j.
\tag{3.2}
\]

The same sum has a direct cyclic count.  Fix one window \(A\).  There are
\(H(M-H)=Hm\) transpositions exchanging one element of \(A\) with one
outside it.  Exactly two produce another cyclic \(H\)-window, namely the
two neighbouring windows.  Thus there are \(Hm-2\) transpositions sending
\(A\) outside the deck.  Summing over the \(M\) windows and remembering
that the squared distance of two zero-one vectors is their symmetric
difference gives

\[
 \sum_\tau\|\tau z_\pi-z_\pi\|_2^2=2M(Hm-2).
\tag{3.3}
\]

Equations (3.2)--(3.3) prove (0.3).

Now \(j\mapsto j(M-j+1)\) is increasing for \(j\le H<M/2\), and

\[
 H(M-H+1)-j(M-j+1)=(H-j)(M+1-H-j)
                         =(H-j)(m+1-j).
\tag{3.4}
\]

Using \(\sum_{j=2}^Ha_j=M(1-p)\) and subtracting (0.3) from
\(H(m+1)M(1-p)\) gives the exact identity (0.4).  For \(j\le H-1\),

\[
 (H-j)(m+1-j)\ge m-H+2.
\tag{3.5}
\]

Hence

\[
 \sum_{j=2}^{H-1}a_j
 \le {M\bigl(H+2-pH(m+1)\bigr)\over m-H+2}
 \le {M(H+2)\over m-H+2},
\tag{3.6}
\]

which proves (0.5)--(0.6).

This also quantifies why any fixed-order harmonic attack misses the
physical column.  At the critical height \(B\) dominates every fixed
power of \(M\), so (2.10) gives

\[
             \sum_{j=2}^{J}a_j=o_J(1)
\tag{3.7}
\]

for every fixed \(J\), whereas (0.6) gives \(a_H=(1-o(1))M\).

### 3.1 The full top-harmonic bundle has an enormous exact kernel

The concentration in \(E_H\) does not create a PSD gap.  For every top
\(U\), identify \(g_U\in E_H(U)\) with the global middle-layer function

\[
 \widetilde g_U(X)=
 \begin{cases}
   g_U(U\setminus X),&X\subseteq U,\ |X|=m,\\
   0,&X\not\subseteq U.
 \end{cases}
\tag{3.8}
\]

Let

\[
 \mathcal T:\bigoplus_{U\in\binom{[2m]}M}E_H(U)
       \longrightarrow\mathbb R^{\binom{[2m]}m},
 \qquad
 \mathcal T((g_U)_U)=\sum_U\widetilde g_U.
\tag{3.9}
\]

Now

\[
 d_H=B-\binom M{H-1}
    =B\left(1-{H\over m+1}\right),
\tag{3.10}
\]

and the flag count

\[
 NB=\binom{2m}{M}\binom MH
    =\binom{2m}m\binom mH
    =W\binom mH
\tag{3.11}
\]

is exact.  Since the codomain of \(\mathcal T\) has dimension \(W\),

\[
 \boxed{
 \dim\ker\mathcal T\ge
 W\left[\binom mH\left(1-{H\over m+1}\right)-1\right].}
\tag{3.12}
\]

Thus the high-harmonic direct-sum bundle has a huge exact nullspace.  In
addition, for every fixed top,

\[
       \mathbb E_\pi P_H^Uz_\pi=0,
\tag{3.13}
\]

so the origin belongs to the convex hull of the projected physical-column
orbit in each fibre.  Consequently every relaxation which replaces a
physical projected column by an arbitrary point of its fibrewise convex
hull has the exact zero global point.  No linear separator and no PSD
coercivity inequality on that convexified bundle can produce an
\(\Omega(W)\) gap.

This does not settle the product of the **integral** orbits
\(\{P_H^Uz_{U,\pi}:\pi\}\).  It proves that a successful higher-harmonic
argument must use a nonlinear integral property of those orbits; the
ambient high-harmonic bundle and its averaged covariance have no gap.

## 4. Global diagonal restitution and the exact covariance demand

Now take all

\[
             N=\binom{2m}{M}
\tag{4.1}
\]

tops and choose one cyclic frame in each.  Let \(v_U\) be its middle
incidence vector, extended by zero outside \(\binom Um\), and put

\[
 b_U=p\mathbf1_{\{X:X\subseteq U,\ |X|=m\}},
 \qquad z_U=v_U-b_U.
\tag{4.2}
\]

Then

\[
 \sum_Ub_U=\theta\mathbf1,qquad
 \theta={MN\over W},\qquad
 \mu=\sum_Uv_U,qquad
 x=\mu-\theta\mathbf1=\sum_Uz_U.
\tag{4.3}
\]

Every \(z_U\) has zero total and zero point margins.  Also

\[
 D:=\sum_U\|z_U\|_2^2=NM(1-p)=L(1-p),
 \qquad L=MN.
\tag{4.4}
\]

By (0.5), the invariant diagonal mass in the highest *local* harmonics is

\[
\begin{aligned}
 D_H^{\rm loc}
   &:=\sum_U\|P_H^Uz_U\|_2^2\\
   &\ge N\left(M(1-p)-{M(H+2)\over m-H+2}\right).
\end{aligned}
\tag{4.5}
\]

If \(H=o(m)\), \(L=(1+o(1))W\), then

\[
                  D_H^{\rm loc}=W-o(W).
\tag{4.6}
\]

This is a genuine statewise invariant of the actual columns.  It is only
a diagonal invariant.  Indeed

\[
 \|x\|_2^2=D+2\sum_{U<V}\langle z_U,z_V\rangle.
\tag{4.7}
\]

Assume the covering-side tuning

\[
                     L=W+s,qquad 0\le s=o(W).
\tag{4.8}
\]

For the exact floor-corrected collision

\[
 \Psi(\mu)=\sum_X\binom{\mu_X}{2}-s,
\tag{4.9}
\]

one has

\[
 \boxed{2\Psi(\mu)=\|x\|_2^2-s+{s^2\over W}.}
\tag{4.10}
\]

Combining (4.4), (4.7), and (4.10), a state with
\(\Psi=o(W)\) must satisfy

\[
             \sum_{U<V}\langle z_U,z_V\rangle
                     =-\left({1\over2}+o(1)\right)W.
\tag{4.11}
\]

There is no contradiction between (4.6) and (4.11): the spaces
\(E_H(U)\) are different overlapping subspaces of the global middle
layer.  Positivity of each one-top covariance says nothing about the sign
of the cross-top terms.

The usual one-block averaging stops exactly at this diagonal.  Let
\(r_U=\mu-v_U\) be the external load.  If the current frame is a minimum
against every other frame in its top, then comparison with the uniform
frame gives

\[
                   \langle r_U,z_U\rangle\le0.
\tag{4.12}
\]

Summing and using \(\langle v_U,z_U\rangle=\|z_U\|^2\) gives

\[
 \sum_U\langle r_U,z_U\rangle=\|x\|^2-D\le0,
 \qquad\text{hence}\qquad \|x\|^2\le D=(1+o(1))W.
\tag{4.13}
\]

The new spectral calculation shows more precisely that almost all of the
fatal right side of (4.13) is top-degree local harmonic restitution.  It
does not improve the \(\Theta(W)\) ceiling.

### 4.1 Exact normal-cone ray

There is a statewise dual formulation of the same obstruction.  In one
top, let

\[
 \mathcal O(c)=\{gc:g\in S_U\},\qquad
 \mathcal N(c)=\{w:\langle w,gc-c\rangle\ge0
                         \text{ for every }g\in S_U\}
\tag{4.14}
\]

be the physical cyclic-column orbit and its minimization normal cone at
the current column.  Then

\[
                       \boxed{-z\in\mathcal N(c).}
\tag{4.15}
\]

Indeed, constants pair to zero with every \(gc-c\), and

\[
 \langle-c,gc-c\rangle=M-\langle c,gc\rangle\ge0.
\tag{4.16}
\]

By (0.5), this universal normal-cone ray satisfies

\[
 \|P_H(-z)\|^2=M-O(H).
\tag{4.17}
\]

The actual block-locality condition is exactly

\[
                         r_U=\mu-v_U\in\mathcal N(v_U).
\tag{4.18}
\]

Thus every fibre contains a compulsory owner-specific stabilizing ray
whose total top-harmonic squared norm is \(W-o(W)\).  Adding an affine
slice function does not change the cone inequalities; in particular
\(\mathbf1-v_U\) is a nonnegative representative of the same ray.  This
is an exact dual obstruction to any proof that replaces the external load
by the aggregate load or discards the current owner column.

It is not a physical bad state: the vectors \(r_U\) for different tops
must arise from one common aggregate \(\mu\).  A compound positive-cut
theorem would have to prove that, when \(\Psi=\Omega(W)\), those common
load contributions cannot leave all \(r_U\)'s inside their respective
normal cones after the self-rays are cancelled jointly.

## 5. Exact floor-corrected load-only no-go

This section proves (0.7)--(0.8).  It deliberately uses the exact cyclic
frame columns in the seminorm.  It also proves that the constructed load
is excluded by an actual-column correlation bound; its role is to close
the load-only affine-lattice argument, not to give a physical bad state.

Choose four distinct coordinates \(a,b,c,d\in[2m]\) and define on the
middle layer

\[
 h(X)=\bigl(\mathbf1_{a\in X}-\mathbf1_{b\in X}\bigr)
      \bigl(\mathbf1_{c\in X}-\mathbf1_{d\in X}\bigr).
\tag{5.1}
\]

This is a degree-two slice harmonic.  Direct transposition symmetry gives

\[
       \sum_Xh(X)=0,qquad
       \sum_{X\ni y}h(X)=0\quad(y\in[2m]).
\tag{5.2}
\]

Moreover \(h=1\) on exactly

\[
                         2\binom{2m-4}{m-2}
\tag{5.3}
\]

middle sets, and the same is true of \(h=-1\).  Also
\(h(X^c)=h(X)\).

The central binomial coefficient \(W=\binom{2m}{m}\) is even.  The exact
point census of any one-frame-per-top state is \(L/2\), so \(L\) is even;
hence \(s=L-W\) is even.  Since \(s=o(W)\), choose \(s/2\) complementary
pairs \(\{X,X^c\}\) from the family \(h(X)=0\), and let \(b\) be the
indicator of their union.  Then

\[
 \sum_Xb(X)=s,qquad
 \sum_{X\ni y}b(X)=s/2,qquad b(X)h(X)=0.
\tag{5.4}
\]

Put

\[
                         \mu_X=1+h(X)+b(X).
\tag{5.5}
\]

This is a nonnegative integer vector with the exact state totals

\[
             \sum_X\mu_X=L,qquad
             \sum_{X\ni y}\mu_X=L/2\quad(y\in[2m]).
\tag{5.6}
\]

The load is two on the family \(h=1\) and on the \(s\) selected zero
sets, zero on \(h=-1\), and one elsewhere.  Therefore

\[
 \Psi(\mu)
 =\sum_X\binom{\mu_X}{2}-s
 =2\binom{2m-4}{m-2},
\tag{5.7}
\]

proving (0.7).

For any real middle-layer function \(f\), define its actual-column cyclic
spread by

\[
 \mathfrak S(f)=\sum_{U\in\binom{[2m]}M}
 \left(
   \mathbb E_\pi\sum_{X\in\mathcal D_m(U,\pi)}f(X)
   -\min_\pi\sum_{X\in\mathcal D_m(U,\pi)}f(X)
 \right),
\tag{5.8}
\]

where \(\mathcal D_m(U,\pi)\) is the deck of the \(M\) cyclic
\(m\)-windows.  This functional is subadditive, and affine slice
functions have zero spread because every deck has \(M\) members and
every point of \(U\) occurs in exactly \(m\) of them.

More generally, let \(Q\subseteq[2m]\), \(|Q|=t\), and let
\(f(X)=F(X\cap Q)\) with \(\|f\|_\infty\le1\).  In a fixed top, all but
at most \(tH\) omitted windows avoid \(U\cap Q\), and hence give one
fixed membership pattern on \(Q\).  It follows that the range of the
cyclic-frame score of \(f\) is at most \(4tH\).  If additionally
\(\sum_Xf(X)=0\), then the same uniform-mean argument as below proves the
actual-state bound

\[
 \boxed{
   |\langle\mu^F,f\rangle|\le4tHN
   \quad\text{for every physical frame selection }F.}
\tag{5.8a}
\]

Thus every such test is automatically \(o(W)\)-correlated whenever

\[
                         {tH\over m}\longrightarrow0.
\tag{5.8b}
\]

At the tuned critical height, a coherent junta obstruction therefore
needs support \(t=\Omega(m/H)=\Omega(\sqrt{m/\log m})\).  Any physical
\(\Omega(W)\) obstruction must be diffuse in its coordinate support, not
merely of algebraic degree at least two.

Fix a top \(U\).  Away from the omitted \(H\)-windows meeting
\(U\cap\{a,b,c,d\}\), the four-coordinate membership pattern of a middle
window is constant.  Each of the at most four distinguished coordinates
lies in exactly \(H\) omitted windows.  Since \(|h|\le1\), every frame
score of \(h\) lies within \(8H\) of one frame-independent value.  Hence

\[
   \max_\pi\sum_{X\in\mathcal D_m(U,\pi)}h(X)
   -\min_\pi\sum_{X\in\mathcal D_m(U,\pi)}h(X)
   \le16H.
\tag{5.9}
\]

Thus

\[
                         \mathfrak S(h)\le16HN.
\tag{5.10}
\]

There is also an actual-state consequence.  Let \(\mu^F\) be the load of
an arbitrary physical choice of one frame in every top.  The uniform
frame means satisfy

\[
 \sum_U\mathbb E_\pi
       \sum_{X\in\mathcal D_m(U,\pi)}h(X)
 =\left\langle\sum_Ub_U,h\right\rangle
 =\theta\langle\mathbf1,h\rangle=0.
\tag{5.11}
\]

For each top, its chosen score differs from its uniform mean by at most
the range in (5.9).  Therefore every physical state obeys

\[
                         \boxed{|\langle\mu^F,h\rangle|\le16HN=o(W).}
\tag{5.12}
\]

On the other hand, the load (5.5) has

\[
 \langle\mu,h\rangle=\|h\|_2^2
 =4\binom{2m-4}{m-2}
 =\left({1\over4}+o(1)\right)W,
\tag{5.13}
\]

because \(\langle\mathbf1,h\rangle=0\) and \(bh=0\).  Thus (5.5) is
provably outside the physical cyclic-frame load set for all sufficiently
large \(m\) with \(H=o(m)\).  This shows simultaneously that a coherent
fixed-coordinate degree-two spike cannot be the missing physical
obstruction: any \(\Omega(W)\) physical collision must be diffuse over a
growing family of harmonic directions.

Because \(b\ge0\), its spread in one top is at most its mean score.
Every fixed middle set lies in \(\binom mH\) eligible tops and, in each,
is selected with probability \(p\).  Since

\[
                  \binom mH p={MN\over W}=\theta,
\tag{5.14}
\]

double counting gives

\[
                         \mathfrak S(b)\le\theta s.
\tag{5.15}
\]

The constant function has zero spread, so subadditivity yields

\[
 \boxed{
 \mathfrak S(\mu)\le16HN+\theta s
                 =16{H\over M}L+\theta s=o(W).}
\tag{5.16}
\]

Equations (5.7) and (5.16) disprove (0.8).

The physical ownership caveat can be quantified exactly.  In a fixed top,
for its current column \(v_U\),

\[
\begin{aligned}
 &\mathbb E_\pi\langle -v_U,v_{U,\pi}\rangle
 -\min_\pi\langle -v_U,v_{U,\pi}\rangle\\
 &\hspace{35mm}=M-pM=M(1-p).
\end{aligned}
\tag{5.17}
\]

Indeed the mean overlap is \(pM\), while the maximum overlap is \(M\),
attained by the current deck.  Summing (5.17) over all tops gives exactly
the diagonal \(D=L(1-p)=(1+o(1))W\).  Therefore the no-go (5.16) cannot
be promoted from the load \(\mu\) to the external loads \(\mu-v_U\)
without solving the owner-sensitive cross-fibre cancellation problem.

## 6. Exact proved boundary

Proved:

1. the complete one-top covariance recursion (2.6);
2. the exact degree-two eigenvalue (0.1) and every fixed-degree asymptotic
   (0.2);
3. the exact transposition moment (0.3);
4. the top-degree concentration identity and bound (0.4)--(0.6);
5. the global diagonal/cross-covariance identity (4.7)--(4.11);
6. the exact \(\Theta(W)\) one-block local-minimum ceiling (4.13), now
   localized to the highest local harmonic; and
7. the exact floor- and point-margin load (5.5) showing that actual-column
   load-only cyclic score has no \(\Omega(W)\) coercivity; and
8. the actual-column correlation bound (5.12), which proves that (5.5)
   itself is not physically decomposable and excludes every coherent
   fixed four-coordinate harmonic spike.

Not proved:

1. a physical integral state with \(\Psi=\Omega(W)\) that is locally
   minimal under all legal compound exchanges;
2. that the cross-top covariance in (4.11) is impossible; or
3. a positive-cut theorem forcing a compound improving exchange.

The smallest surviving hypothesis is now explicit.

> **Owner-sensitive top-harmonic positive-cut gate.**  For every physical
> one-frame-per-top state with \(\Psi=\Omega(W)\), there is a legal
> compound exchange of whole cyclic frames whose cross-top Gram gain is
> larger than its external-load node toll after the common
> \((1-o(1))W\) local \(E_H\) self-restitution is cancelled.

Any proof confined to bounded Johnson degree, to a state-independent PSD
average, or to the aggregate load \(\mu\) cannot establish this gate.
The remaining information is integral, owner-indexed, and concentrated at
growing harmonic degree \(H-O(1)\).
