# Parity-complete adjacent-deletion orientations: an explicit dyadic recursion and its Gaussian trace obstruction

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, or
probabilistic independence surrogate is used.

## 0. Exact outcome

Let \(r=2s\) be a power of two. Split the \(r\) coarse coordinates into
two halves \(L,R\), let \(F_r\) be the recursive isometric
\(C_{2r}\)-factor of \(Q_r\), and write \(\delta_r(y)\) for its outgoing
direction at \(y\). Let \(\rho\) be any coordinate permutation which
exchanges \(L\) and \(R\). For every even parity context \(p\), define

\[
             \boxed{d_p(x)=\delta_r(x\oplus\rho p).}             \tag{0.1}
\]

This is an explicit recursive solution of both adjacent-deletion
orientation equations:

\[
 x\longmapsto x\oplus e_{d_p(x)}
 \quad\hbox{is a permutation for every fixed }p,                 \tag{0.2}
\]

and

\[
 p\longmapsto p\oplus e_{d_p(x)}:
 Q_r^{\rm even}\longrightarrow Q_r^{\rm odd}
 \quad\hbox{is a bijection for every fixed }x.                   \tag{0.3}
\]

Every cycle in (0.2) is an isometric \(C_{2r}\) with a doubled
permutation direction word. Thus parity-complete ownership and the
coarse-cycle requirement are simultaneously feasible, integrally and
pointwise.

The same recursion nevertheless fails the erased-context trace gate.
Let an aligned window make \(d\) coarse moves, hence \(2d\) physical
moves after the adjacent-pair lift. Its lower and upper physical traces
have the same code

\[
 \mathcal C_d(p,x)=
 \bigl(J_{p,d}(x),x|_{J_{p,d}(x)^c},p|_{J_{p,d}(x)^c}\bigr).      \tag{0.4}
\]

For dyadic \(2\le t\le s/2\), take \(d=2t\). Put

\[
                         \lambda={t^2\over s},
 \qquad                   \theta=1-{2\over t}+{1\over s}.        \tag{0.5}
\]

For either signed aligned trace map, on its domain of

\[
                         N_r=2^{2r-1}                             \tag{0.6}
\]

starts, the exact distinct-target deficit satisfies

\[
 \boxed{
 {\operatorname {Exc}_{r,2t}^{\pm}\over N_r}
 \ge {\theta^2\lambda^2
          \over2(\lambda^2+4\lambda+2)}.}                       \tag{0.7}
\]

Consequently, if this \(r\)-pair factor lies in \(2m\) physical
coordinates, \(H=\lfloor A\sqrt m\rfloor\), and

\[
                         H\le r\le m,                             \tag{0.8}
\]

then some aligned physical depth \(q\le H\) has

\[
 \boxed{
 \liminf_{m\to\infty}{\operatorname {Exc}^{\pm}(q)\over N_r}
 \ge c_A:={1\over2}
 { (A^2/32)^2
   \over (A^2/32)^2+4(A^2/32)+2}
 = {A^4\over2(A^4+128A^2+2048)}>0.}                             \tag{0.9}
\]

Thus every fixed half-exchange recursion (0.1) has
\(\Omega_A(N_r)\) aligned trace excess at Gaussian depth. Its direction
sets do not encode the erased \(p_J\) and \(x_J\) data with negligible
loss.

There are two independent sharper census statements.

1. At \(d=r/2\), the recursive factor has at most \(2^{r/2}\) possible
   supports, and therefore

   \[
   \operatorname {Exc}_{r,r/2}^{\pm}
   \ge 2^{2r-1}-2^{3r/2}.                           \tag{0.10}
   \]

2. For every parity-complete construction whatsoever, not only (0.1),

   \[
   \operatorname {Exc}_{r,r/2}^{\pm}
   \ge 2^{2r-1}-\binom r{r/2}2^r
   =\bigl(1-O(r^{-1/2})\bigr)2^{2r-1}.              \tag{0.11}
   \]

The obstruction in (0.7)--(0.9) is the relevant stronger statement: it
persists when \(H=o(r)\). It rules out the entire half-exchanging
double-factor recursion, but it does not rule out a genuinely nonlinear
orientation in which the column certificate is not a fixed coordinate
permutation of the row direction.

## 1. The two orientation equations

Let

\[
 E_r=\{p\in Q_r:|p|\equiv0\pmod2\},\qquad
 O_r=Q_r\setminus E_r.                              \tag{1.1}
\]

For a direction table \(d:E_r\times Q_r\to[r]\), put

\[
 z_{p,x,i}=\mathbf1_{\{d_p(x)=i\}}.                 \tag{1.2}
\]

The pointwise choice, row-permutation, and column-complete-mapping
conditions are respectively

\[
 \sum_i z_{p,x,i}=1,                                \tag{1.3}
\]

\[
 \sum_i z_{p,y\oplus e_i,i}=1,                     \tag{1.4}
\]

and

\[
 \sum_i z_{u\oplus e_i,x,i}=1                      \tag{1.5}
\]

for every even \(p\), every \(x,y\), and every odd \(u\). Equation
(1.4) says that every target \(y\) has one row predecessor. Equation
(1.5) says that every odd context \(u\) has one column predecessor.
These are exactly the two simultaneous adjacent-deletion orientations;
there is no fractional relaxation in them.

### Proposition 1.1 (basis-displacement Latin-square form)

Identify each parity shore of \(Q_r\) with \(E_r\) by writing

\[
 x=z\oplus\varepsilon e_1,
 \qquad z\in E_r,\quad\varepsilon=|x|\pmod2.         \tag{1.6}
\]

Put

\[
 u^\varepsilon(p,z)=e_1\oplus
        e_{d_p(z\oplus\varepsilon e_1)}\in
 \mathcal B:=\{0,e_1\oplus e_2,\ldots,e_1\oplus e_r\},           \tag{1.7}
\]

and

\[
 L^\varepsilon(p,z)=p\oplus z\oplus u^\varepsilon(p,z).         \tag{1.8}
\]

For a fixed \(\varepsilon\), equations (1.4) and (1.5) hold if and only
if \(L^\varepsilon\) is a Latin square on the group \(E_r\): every row
and every column is a permutation. Its displacement from the group
table is constrained to the affine basis \(\mathcal B\).

#### Proof

If the physical direction is \(i\), then after changing shores the
coordinate \(z\) becomes

\[
 z\oplus e_1\oplus e_i=z\oplus u^\varepsilon(p,z).  \tag{1.9}
\]

Thus, at fixed \(p\), the row move is bijective precisely when
\(z\mapsto z\oplus u^\varepsilon(p,z)\) is bijective. After identifying
an odd output context \(p\oplus e_i\) with the even vector
\(p\oplus e_i\oplus e_1=p\oplus u^\varepsilon(p,z)\), the column move is
bijective precisely when \(p\mapsto p\oplus u^\varepsilon(p,z)\) is
bijective. Adding the fixed row label \(p\), or the fixed column label
\(z\), turns these two maps into the rows and columns of (1.8). \(\square\)

If \(A_p(z)=z\oplus u^0(p,z)\) and
\(B_p(z)=z\oplus u^1(p,z)\), the two-step return of the row permutation
to the even shore is \(B_pA_p\). Hence a \(C_{2r}\)-factor requires the
cycles of \(B_pA_p\) to have length \(r\), together with the doubled
direction condition. Proposition 1.1 shows that the ownership equations
alone have no parity obstruction; the extra burden is the row-cycle and
visible-support code.

## 2. The recursive coarse factor

For powers of two \(n\), define \(F_n\) recursively. Let \(F_1\) toggle
its sole coordinate. If \(n=2h\), write
\(y=(u,v)\in Q_h^L\times Q_h^R\) and put

\[
 F_{2h}(u,v)=
 \begin{cases}
   (F_hu,v),&|u|+|v|\equiv0\pmod2,\\
   (u,F_hv),&|u|+|v|\equiv1\pmod2.
 \end{cases}                                        \tag{2.1}
\]

Let \(\delta_n(y)\) be the changed coordinate. Directly from (2.1),

\[
 F_{2h}^{\,2a}(u,v)=(F_h^au,F_h^av)                 \tag{2.2}
\]

for every integer \(a\).

### Lemma 2.1 (cycle and window structure)

Every \(F_n\)-cycle has length \(2n\), is isometric, and has direction
word \(\pi\pi\) for a permutation \(\pi\) of \([n]\). Moreover, if
\(t\le n\) is a power of two, every \(t\)-move window contains exactly
one direction from each member of the canonical partition
\(\mathcal P_{n,t}\) of \([n]\) into \(t\) dyadic blocks of size \(n/t\).

If \(U\) is uniform on \(Q_n\), the chosen coordinate in each block is
independent and uniform. Thus its \(t\)-window support is uniform over
all transversals of \(\mathcal P_{n,t}\). The same assertions hold for
reverse windows.

#### Proof

Induct on \(n\). Equation (2.2) shows that an \(F_{2h}\)-orbit returns
after \(4h\) moves. An earlier even return would give an earlier return
in both \(F_h\)-coordinates. At an odd time the two child move counts
differ by one, whereas two multiples of the child cycle length \(2h\)
cannot differ by one; hence an odd return is also impossible. During the first \(2h\) moves, each
half makes \(h\) moves and, by induction, uses each of its directions
once. The second \(2h\) moves repeat the order. This proves the cycle,
doubled-word, and isometry assertions.

For \(t=1\), every outgoing direction occurs equally often: every
\(C_{2n}\)-component uses every direction twice. Hence the selected
coordinate is uniform on the one block \([n]\). For \(t\ge2\), write
\(t=2a\). A \(t\)-window of \(F_{2h}\) contains exactly \(a\) moves in
each half, and (2.2) identifies their supports with the \(a\)-windows
starting at \(u\) and \(v\). For uniform \((u,v)\), these two child
starts are independent and uniform. The induction hypothesis gives
one independent uniform choice in each of the \(a\) child blocks in
each half. These are precisely the \(t\) blocks of
\(\mathcal P_{2h,t}\). Reversing the permutation gives the same
induction. \(\square\)

In particular, for \(t=n/2\), there is one choice from each of \(n/2\)
bottom sibling pairs. Therefore the number of half-window supports is
at most \(2^{n/2}\) (in fact it is exactly this number).

## 3. Explicit parity-complete recursion

Fix \(r=2s\ge2\), and let \(\rho\) be a coordinate permutation satisfying

\[
                         \rho(L)=R,\qquad\rho(R)=L.  \tag{3.1}
\]

Define (0.1), and put

\[
                         F_p(x)=x\oplus e_{d_p(x)},\qquad
                         T_x(p)=p\oplus e_{d_p(x)}.  \tag{3.2}
\]

For the standard half swap
\(\rho(p_L,p_R)=(p_R,p_L)\), formula (0.1) is the literal recursion

\[
 d^{(2s)}_{(p_L,p_R)}(x_L,x_R)=
 \begin{cases}
   \delta_s(x_L\oplus p_R),&
      |x_L|+|x_R|\equiv0\pmod2,\\
   s+\delta_s(x_R\oplus p_L),&
      |x_L|+|x_R|\equiv1\pmod2.
 \end{cases}                                        \tag{3.3}
\]

Indeed \(p\) is even, so \(x\oplus\rho p\) has the same total parity
as \(x\). Together with (2.1), this gives \(d_p(x)\) recursively down to
the one-coordinate base without any choice or rounding.

### Theorem 3.1 (half-exchange parity complete mapping)

For every \(p\in E_r\), \(F_p\) is a translation-conjugate of \(F_r\).
For every \(x\in Q_r\), \(T_x:E_r\to O_r\) is a bijection. Hence the
adjacent-pair physical lift is an exact \(C_{4r}\)-factor, and every
coarse component is an isometric \(C_{2r}\) with a doubled-permutation
direction word.

#### Proof

Put \(c=\rho p\) and \(y=x\oplus c\). Then

\[
 F_p(x)=x\oplus e_{\delta_r(y)}
       =c\oplus F_r(y).                              \tag{3.4}
\]

Thus \(F_p=\tau_cF_r\tau_c\), where \(\tau_c\) is translation by \(c\).
Translation preserves every labelled direction, proving the row and
cycle assertions.

For the column assertion, fix \(x\) and use the coordinate

\[
                         B_x(p)=x\oplus\rho p.        \tag{3.5}
\]

It maps \(E_r\) onto the parity shore of \(x\), and \(O_r\) onto the
opposite shore. Furthermore,

\[
 B_x(T_xp)=B_x(p)\oplus e_{\rho\delta_r(B_xp)}.      \tag{3.6}
\]

It remains to prove that

\[
                         G_r(y)=y\oplus e_{\rho\delta_r(y)}       \tag{3.7}
\]

bijects the two parity shores. If \(y=(u,v)\) is even, then
\(\delta_r(y)\) is a left direction determined by the unchanged \(u\),
and \(G_r\) toggles its \(\rho\)-image in the right half. Hence an odd
target \((u',v')\) has the unique even predecessor obtained by leaving
\(u'\) fixed and toggling in \(v'\) the \(\rho\)-image of
\(\delta_s(u')\). If \(y\) is odd, the symmetric statement holds: the
right half is unchanged, and an even target has a unique odd predecessor
obtained by toggling in its left half the \(\rho\)-image of the direction
determined by its right half. Thus (3.7), and consequently (3.6), is
bijective. \(\square\)

No cycle assertion about \(G_r\) is used or needed. It is only the
pointwise certificate for the column orientation.

Finally, a factor of \(Q_r\) entirely into \(C_{2r}\)'s requires

\[
                         2r\mid2^r.                  \tag{3.8}
\]

Thus \(r\) must itself be a power of two (apart from the trivial
\(r=1\) case). The dyadic restriction in Theorem 3.1 is therefore
forced by the requested uniform cycle length, not merely by the chosen
recursion.

## 4. The exact support-alphabet cut

For an aligned \(d\)-coarse-step window, let

\[
 J_{p,d}(x)=\{d_p(x),d_p(F_px),\ldots,
                    d_p(F_p^{d-1}x)\}.              \tag{4.1}
\]

Because the coarse cycle is isometric for \(d\le r\), the \(d\)
directions in (4.1) are distinct. In the physical paired lift, both
bits of every pair in \(J\) are erased by the lower intersection and
filled by the upper union. Every untouched pair records its physical
state, equivalently \(x_i,p_i\). Hence (0.4) is the exact fibre code for
both signs.

Define

\[
 \mathscr J_d=\{J_{p,d}(x):(p,x)\in E_r\times Q_r\},
 \qquad K_d=|\mathscr J_d|.                          \tag{4.2}
\]

### Theorem 4.1 (visible-support entropy requirement)

For every direction table, whether or not it satisfies the ownership
equations,

\[
 |\operatorname {im}\mathcal C_d|
 \le K_d\,2^{2(r-d)},                               \tag{4.3}
\]

and therefore

\[
 \boxed{
 \operatorname {Exc}_{r,d}^{\pm}
 :=2^{2r-1}-|\operatorname {im}\mathcal C_d^\pm|
 \ge2^{2r-1}-K_d2^{2(r-d)}.}                       \tag{4.4}
\]

Exact injectivity requires

\[
                         K_d\ge2^{2d-1},             \tag{4.5}
\]

and \(o(2^{2r})\) excess requires

\[
                         K_d\ge(1-o(1))2^{2d-1}.     \tag{4.6}
\]

#### Proof

Once \(J\) is fixed, the code retains only \(r-d\) bits of \(x\) and
\(r-d\) bits of \(p\), giving at most \(2^{2(r-d)}\) values. Summing
over the \(K_d\) visible supports gives (4.3). The domain has size
\(|E_r|2^r=2^{2r-1}\), proving the rest. \(\square\)

Since \(K_d\le\binom rd\), (4.4) gives the universal bound

\[
 \operatorname {Exc}_{r,d}^{\pm}
 \ge2^{2r-1}-\binom rd2^{2(r-d)}.                   \tag{4.7}
\]

At \(d=r/2\), the surviving image proportion is at most

\[
                         2^{1-r}\binom r{r/2}
 \sim\sqrt{8\over\pi r},                             \tag{4.8}
\]

which proves (0.11). For the recursive \(F_r\), Lemma 2.1 gives the
sharper \(K_{r/2}\le2^{r/2}\), proving (0.10). In this recursion the
support label carries only \(r/2\) bits at depth \(r/2\), while the
inside \((p,x)\)-data have \(r-1\) degrees of freedom after the parity
equation. The average nonempty fibre therefore has size at least
\(2^{r/2-1}\).

## 5. Invisible toggles in a shallow recursive window

For (0.1), put

\[
                         y=x\oplus\rho p.             \tag{5.1}
\]

Equation (3.4) gives

\[
 J_{p,d}(x)=J_d^{F_r}(y).                            \tag{5.2}
\]

If \(a\in E_r\) satisfies

\[
                         \operatorname {supp}a\subseteq J,
 \qquad \operatorname {supp}(\rho a)\subseteq J,    \tag{5.3}
\]

then

\[
                         (p,x)\longmapsto
                         (p\oplus a,x\oplus\rho a)   \tag{5.4}
\]

fixes \(y\), fixes \(J\), and fixes both outside restrictions in (0.4).
It is therefore an invisible free action inside every physical trace
fibre.

Take a dyadic \(2\le t\le s/2\) and \(d=2t\). By (2.2), a \(2t\)-window of
\(F_{2s}\) has support

\[
                         J=L A\ \dot\cup\ R B,        \tag{5.5}
\]

where \(A\) and \(B\) are the \(t\)-window supports of the two \(F_s\)
coordinates. Under a uniform start \(y=(u,v)\), Lemma 2.1 says that
\(A,B\) are independent uniform transversals of the same partition into
\(t\) blocks of size

\[
                         \ell={s\over t}.             \tag{5.6}
\]

Uniform counting on the original domain gives exactly this law: for
each \(y\in Q_r\), there are \(|E_r|\) pairs \((p,x)\) satisfying
\(y=x\oplus\rho p\). Thus \(y\), and hence its two halves \(u,v\), are
uniform when starts are counted with their physical multiplicity.

Let \(g=\rho|_L:L\to R\), and define

\[
                         X=|g(A)\cap B|.              \tag{5.7}
\]

Every member \(i\in A\) counted by \(X\) satisfies
\(i\in J\) and \(\rho i\in J\). If \(X\ge2\), two such members give a
nonzero even vector \(a=e_i\oplus e_j\) satisfying (5.3). Thus every
trace fibre whose support has \(X\ge2\) has size at least two.

### Lemma 5.1 (uniform factorial-moment bound)

For every half-exchanging permutation \(\rho\), if

\[
                         \lambda={t^2\over s},
 \qquad                   \theta=1-{2\over t}+{1\over s},         \tag{5.8}
\]

then, for every \(k\ge1\),

\[
                         \mathbb E(X)_k\le\lambda^k,              \tag{5.9}
\]

and

\[
                         \mathbb E(X)_2\ge\theta\lambda^2.       \tag{5.10}
\]

#### Proof

Write \(X=\sum_{i\in L}I_i\), where \(I_i\) is the event that \(A\)
chooses \(i\) and \(B\) chooses \(g(i)\). For an ordered \(k\)-tuple of
distinct coordinates, the joint event is impossible if two source
coordinates lie in one \(A\)-block or two images lie in one \(B\)-block.
Otherwise its probability is exactly \(\ell^{-2k}\). There are at most
\(s^k\) ordered tuples, so

\[
 \mathbb E(X)_k\le s^k\ell^{-2k}
                  =(t^2/s)^k=\lambda^k.             \tag{5.11}
\]

For \(k=2\), among the \(s(s-1)\) ordered distinct pairs, at most
\(s(\ell-1)\) share a source block and at most \(s(\ell-1)\) have images
sharing a target block. Hence at least

\[
 s(s-1)-2s(\ell-1)=s(s-2\ell+1)                    \tag{5.12}
\]

ordered pairs are admissible. Multiplying by \(\ell^{-4}\) gives

\[
 \mathbb E(X)_2\ge s(s-2\ell+1)\ell^{-4}
 =\left(1-{2\over t}+{1\over s}\right){t^4\over s^2},            \tag{5.13}
\]

which is (5.10). \(\square\)

For an exact audit of the lower bound, let \(n_{ab}\) be the size of the
intersection of source block \(a\) with the pullback under \(g\) of
target block \(b\). Inclusion--exclusion gives

\[
 {\mathbb E(X)_2\over\lambda^2}
 =1-{2\over t}+{1\over s}
   +{1\over s^2}\sum_{a,b}(n_{ab})_2.                \tag{5.14}
\]

Thus (5.10) remains valid for the most adversarial cross-half
permutation; no hypergeometric or random-\(\rho\) assumption is hidden
in it.

### Theorem 5.2 (Gaussian collision obstruction)

For every dyadic \(2\le t\le s/2\), (0.7) holds for both aligned signs.

#### Proof

Let \(Y=\binom X2\). The exact identity

\[
                         Y^2=6\binom X4+6\binom X3+\binom X2      \tag{5.15}
\]

and (5.9) give

\[
 \mathbb EY^2
 \le {\lambda^4\over4}+\lambda^3+{\lambda^2\over2}.              \tag{5.16}
\]

By (5.10), \(\mathbb EY\ge\theta\lambda^2/2\). Paley--Zygmund at
level zero therefore gives

\[
 \Pr(X\ge2)=\Pr(Y>0)
 \ge {\theta^2\lambda^2\over\lambda^2+4\lambda+2}.               \tag{5.17}
\]

The value of \(X\) is determined by \(J\), hence is constant on each
trace fibre. On the union of fibres with \(X\ge2\), the free action
(5.4) has orbits of size at least two. At most half of those starts can
give distinct trace values. Subtracting image size from the total
number of starts yields

\[
 {\operatorname {Exc}_{r,2t}^{\pm}\over N_r}
 \ge {1\over2}\Pr(X\ge2),                            \tag{5.18}
\]

and (0.7) follows. \(\square\)

To prove (0.9), take the largest power of two \(t\le H/4\). Then

\[
 t>{H\over8},\qquad t\le {r\over4}={s\over2},
 \qquad
 \lambda={2t^2\over r}>{H^2\over32r}\ge {H^2\over32m}.           \tag{5.19}
\]

For \(H=\lfloor A\sqrt m\rfloor\), one has
\(\theta\to1\), while
\(\lambda^2/(\lambda^2+4\lambda+2)\) is increasing in \(\lambda>0\).
The aligned physical depth is \(q=2d=4t\le H\). Equations
(5.18)--(5.19) prove (0.9).

If instead \(r<H\), the aligned choice \(d=r/2\) has physical depth
\(q=r\le H\), and (0.10) gives

\[
 {\operatorname {Exc}_{r,r/2}^{\pm}\over N_r}
 \ge1-2^{1-r/2}.                                    \tag{5.20}
\]

Thus every sequence of half-exchange recursions with \(r\to\infty\)
fails the protected-window gate whether \(r\ge H\) or \(r<H\). The
Gaussian constant (0.9) is the nontrivial branch in which the packet is
much wider than the protected window.

### Corollary 5.3 (sharper corresponding-half constant)

Suppose \(\rho\) pairs corresponding coordinates and preserves the
canonical \(t\)-block alignment. Then

\[
                         X\sim\operatorname {Bin}(t,t/s).         \tag{5.21}
\]

The full invisible even-subspace orbit gives the sharper exact bound

\[
 {\operatorname {Exc}_{r,2t}^{\pm}\over N_r}
 \ge1-2\left(1-{3t\over4s}\right)^t
       +\left(1-{t\over s}\right)^t                              \tag{5.22}
\]

and hence

\[
 {\operatorname {Exc}_{r,2t}^{\pm}\over N_r}
 \ge {1\over2}\left[1-
             \exp\left(-{t^2\over s}\right)\right].              \tag{5.23}
\]

#### Proof

In each canonical block, \(A\) and \(B\) make independent uniform
choices, so their match indicators are independent Bernoulli variables
of mean \(t/s\). Conditional on \(X=c\ge1\), the even vectors supported
on the resulting \(2c\) matched physical coordinates form a free group
of size \(2^{2c-1}\). For \(c=0\), the orbit has size one. Therefore
the surviving image fraction is at most

\[
 \Pr(X=0)+\sum_{c\ge1}2^{1-2c}\Pr(X=c)
 =2\mathbb E4^{-X}-\Pr(X=0),                        \tag{5.24}
\]

which gives (5.22). Finally, with \(z=1-t/s\), convexity of
\(w\mapsto w^t\) gives

\[
 4\left({1+3z\over4}\right)^t\le1+3z^t.             \tag{5.25}
\]

Substitution in (5.22), followed by
\((1-t/s)^t\le e^{-t^2/s}\), gives (5.23). \(\square\)

## 6. Audited boundary

The proved statements have the following exact scope.

1. **Ownership and cycle structure are solved.** Formula (0.1) satisfies
   both integral orientation equations for every state, and every row is
   an exact \(C_{2r}\)-factor. No common-owner averaging is used.

2. **The obstruction is literal.** The collision pairs in (5.4) have
   identical completed direction support and identical retained physical
   coordinates. They therefore give the same literal lower intersection
   and upper union, not merely the same histogram.

3. **Aligned failure is sufficient.** The proof treats even-time
   windows completing \(d=2t\) physical pairs. It does not enumerate
   odd-time or half-step codes. A construction required to protect all
   \(q\le H\) already fails because the aligned depth \(q=4t\le H\) has
   the positive excess (0.9).

4. **The decisive constants were checked in two ways.** The factorial
   moments give the arbitrary-\(\rho\) constant (0.7); for the canonical
   involution the exact binomial census gives (5.22). The factor \(1/2\)
   in (0.7) is necessary because a two-point fibre can contribute one
   distinct target.

5. **This is a class obstruction, not a universal shallow no-go.** The
   proof uses the invariant \(x\oplus\rho p\) and a fixed half-exchanging
   coordinate permutation. A genuinely state-dependent column
   orientation can evade (5.4). Any such escape must nevertheless meet
   the universal visible-support quota

   \[
                         K_d\ge(1-o(1))\,2^{2d-1}                  \tag{6.1}
   \]

   at every protected aligned depth, while retaining the two Latin-square
   orientation equations and \(r\)-cycle return maps. The affine,
   common-clock, and bounded-order-library bounds are proved separately
   in
   \( \texttt{MATH\_THEOREM\_AFFINE\_PARITY\_COMPLETE\_MAPPING\_CLASSIFICATION\_20260726.md}\);
   Theorem 5.2 here closes the half-exchange recursion.

6. **No constant-one conclusion is claimed.** Even a future nonlinear
   solution of the local code would still have to be coupled across the
   outer exact-factor packets and their suffix/leave interfaces. This
   note closes only the explicit adjacent-deletion recursion (0.1) and
   isolates the exact nonlinear escape.
