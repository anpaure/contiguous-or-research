# Fixed-annulus cyclic packets: coloured resolution and the critical leave scale

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Fix \(0<a<b\), and put

\[
n=2m,\qquad q_0=\lceil a\sqrt m\rceil,\qquad
H=\lfloor b\sqrt m\rfloor,\qquad R=m-q_0,
\]

\[
W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}.
\]

A packet is a directed cyclic order of \([n]\), modulo rotation. Its
rank-\(s\) trace consists of its \(n\) cyclic intervals of length \(s\).
Write

\[
D_d=(R-d)!(n-R+d)!,\qquad 0\le d\le H-q_0,                 \tag{0.1}
\]

for the number of directed packets through one rank-\((R-d)\) target.

The outcome has one positive reduction and one rigorous no-go.

1. There is an exact coloured-resolution system \(\mathrm{CR}(C)\).
   It colours the whole packet catalogue with \(C\) colours. At every
   colour, entrance targets and middle complementary pairs have capacity
   one, while every deeper annular target has demand one. Its uniform
   fractional point is feasible exactly in the window

   \[
   \boxed{D_0\le C\le D_1},\qquad
   \frac{D_1}{D_0}
    =1+\frac{2q_0+1}{m-q_0}
    =1+\frac{2a+o(1)}{\sqrt m}.                              \tag{0.2}
   \]

   If \(\mathrm{CR}(C)\) is integral for any integer in this window,
   one colour gives, after harmless packet-count completion,

   \[
   C_{\rm mid}+\sum_{q=q_0}^{H}h_q
   \le
   2N_{q_0}\left(1-\frac{D_0}{C}\right)
   =O_a(W/\sqrt m)=o(W).                                    \tag{0.3}
   \]

   Thus this single coloured factor theorem would close the fixed
   annulus at coefficient one. Upper-target holes have the same counts by
   packetwise complementation, so they change only the harmless factor
   two in the literal repair ledger.

2. The interval adjacency skeleton contracts exactly. If \(T\) has
   depth \(d\), its aligned owned-extension count in any packet family is

   \[
   \boxed{E_d(T)=(d+1)\mu_d(T).}                             \tag{0.4}
   \]

   Hence the adjacent-rank relative codegree \(2/R=\Theta(m^{-1})\)
   is a compulsory two-edge thread, not a collision. Same-rank maximum
   relative codegree is only \(2/[R(n-R)]=\Theta(m^{-2})\).

3. Ordinary \(o(N)\) leave is the wrong conclusion. The lower annular
   shores have total size

   \[
   \sum_{q=q_0}^{H}N_q
   =
   W\left(\sqrt m\int_a^b e^{-x^2}\,dx+O_{a,b}(1)\right).    \tag{0.5}
   \]

   A relative coloured leave \(\eta_m\) implies aggregate \(o(W)\)
   only if

   \[
   \boxed{\eta_m=o(m^{-1/2}).}                               \tag{0.6}
   \]

4. Exact codegrees do not support arbitrary residual regeneration.
   Every balanced coordinate bipartition \(B\sqcup B^c=[2m]\) gives a
   coordinate-regular, packet-free residual of density
   \(1-\Theta(m^{-1/2})\). This strengthens the parity-holonomy no-go:
   even density \(1-o(1)\), exact point margins, and the visible
   adjacency skeleton do not force one residual packet.

No integral solution of \(\mathrm{CR}(C)\) is proved here. Conversely,
the residual obstruction below is not a Hall cut against a deliberately
balanced global resolution. The exact open gate is the integrality of
\(\mathrm{CR}(C)\).

## 1. Exact interval and thread kernels

Let \(\Omega\) be the set of directed cyclic orders of \([n]\), modulo
rotation, so \(|\Omega|=(n-1)!\). For \(\pi\in\Omega\), put

\[
I_\pi(j,s)=\{\pi_j,\pi_{j+1},\ldots,\pi_{j+s-1}\},
\qquad j\in\mathbb Z_n.                                    \tag{1.1}
\]

Contracting a prescribed \(s\)-interval to one cyclic block gives its
packet degree

\[
D(s)=s!(n-s)!.                                              \tag{1.2}
\]

This proves (0.1), as well as

\[
\frac{D_d}{D_0}
=\frac{N_{q_0}}{N_{q_0+d}}
=\prod_{j=1}^{d}\frac{n-R+j}{R-j+1}.                        \tag{1.3}
\]

In particular \(D_d\) increases with \(d\), and

\[
\frac{D_1}{D_0}=\frac{n-R+1}{R}
=\frac{m+q_0+1}{m-q_0}.                                    \tag{1.4}
\]

If \(A,A'\in\binom{[n]}R\) have Johnson distance
\(t=|A\setminus A'|<R\), the four Venn cells occur as four consecutive
blocks. Therefore

\[
\frac{D(A,A')}{D_0}
=\frac{2}{\binom Rt\binom{n-R}t}.                           \tag{1.5}
\]

For disjoint \(A,A'\),

\[
\frac{D(A,A')}{D_0}
=\frac{n-2R+1}{\binom{n-R}R}.                               \tag{1.6}
\]

At \(R=m-\Theta(\sqrt m)\), (1.5) is maximized at \(t=1\), while
(1.6) is stretched-exponentially smaller. Hence

\[
\frac{\Delta_2}{D_0}
=\frac{2}{R(n-R)}=(2+o(1))m^{-2}.                           \tag{1.7}
\]

The mixed-rank coefficient is larger for a structural reason. If
\(T\subset A\), \(|A|=R\), and \(|T|=R-d\), direct block counting gives

\[
\frac{D(A,T)}{D_0}
=\frac{d+1}{\binom Rd}.                                     \tag{1.8}
\]

For \(d=1\), this is \(2/R\).

Now fix a packet \(\pi\). Its entrance trace

\[
A_j=I_\pi(j,R),\qquad j\in\mathbb Z_n,                      \tag{1.9}
\]

is a directed \(n\)-cycle in \(J(n,R)\), and

\[
T_{j,d}=I_\pi(j+d,R-d)
=\bigcap_{u=0}^{d}A_{j+u}.                                 \tag{1.10}
\]

Thus depth-\(d\) targets are the intersection colours of directed
\(d\)-paths in the entrance cycle.

For a packet family \(\mathcal F\), let \(\mu_d(T)\) be the number of
packets in which \(T\) occurs at rank \(R-d\). Let \(E_d(T)\) count
owned entrance intervals \(A\) for which \(T\) is obtained by deleting
a prefix and suffix of total length \(d\).

### Lemma 1.1 (exact thread multiplicity)

For every \(T\), equation (0.4) holds.

#### Proof

Fix one occurrence \(T=I_\pi(j,R-d)\). The aligned entrance intervals
containing it start at \(j-u\), \(0\le u\le d\). These are \(d+1\)
distinct extensions, and every aligned extension arises uniquely this
way. Sum over occurrences. \(\square\)

The identity holds colour by colour. At depth one, \(E_1(T)\) is even
and target coverage is the threshold \(E_1(T)\ge2\), not \(E_1(T)>0\).
At depth \(d\), the threshold is \(d+1\). This divisibility is lost if
all annular ranks are inserted as unrelated matching vertices.

## 2. The coloured-resolution system

Let

\[
\mathcal P_m=\{\{X,X^c\}:X\in\tbinom{[n]}m\}.
\]

A packet uses \(m\) members of \(\mathcal P_m\). A fixed member has
directed packet degree \(D_m=(m!)^2\), and

\[
\frac{D_m}{D_0}=\frac{N_{q_0}}W=e^{-a^2+o(1)}<1.            \tag{2.1}
\]

For an integer \(C\ge1\), introduce
\(x_{\pi,c}\in\{0,1\}\), \(\pi\in\Omega\), \(1\le c\le C\).
The system \(\mathrm{CR}(C)\) is

\[
\sum_{c=1}^{C}x_{\pi,c}=1
\qquad(\pi\in\Omega),                                      \tag{2.2}
\]

\[
\sum_{\pi:A\in E_R(\pi)}x_{\pi,c}\le1
\qquad(A\in\tbinom{[n]}R),                                 \tag{2.3}
\]

\[
\sum_{\pi:P\in E_m(\pi)/\pm}x_{\pi,c}\le1
\qquad(P\in\mathcal P_m),                                  \tag{2.4}
\]

and, for \(1\le d\le H-q_0\),

\[
\sum_{\pi:T\in E_{R-d}(\pi)}x_{\pi,c}\ge1
\qquad(T\in\tbinom{[n]}{R-d}).                              \tag{2.5}
\]

Equations (2.3)--(2.5) hold for each colour \(c\).

### Theorem 2.1 (exact fractional window)

The uniform point \(x_{\pi,c}=1/C\) satisfies the linear relaxation of
\(\mathrm{CR}(C)\) if and only if (0.2) holds.

#### Proof

The entrance load is \(D_0/C\), so (2.3) requires \(C\ge D_0\).
The middle load is \(D_m/C<D_0/C\). At depth \(d\), the demand load is
\(D_d/C\). Since \(D_d\) increases with \(d\), all deeper demands hold
exactly when \(C\le D_1\). \(\square\)

There is a floor condition not seen by the star loads. Put

\[
K_+=\left\lfloor\frac{N_{q_0}}n\right\rfloor,\qquad
K_-=\left\lceil\frac{N_{q_0+1}}n\right\rceil,\qquad
\mathcal E=|\Omega|=(n-1)!.
\]

Every integral colour class has size between \(K_-\) and \(K_+\).
Consequently

\[
\boxed{CK_-\le\mathcal E\le CK_+.}                          \tag{2.6}
\]

The left inequality follows because one colour must cover all
\(N_{q_0+1}\) first-shadow targets using \(n\) occurrences per packet.
The right follows from entrance disjointness.

The integer \(C\)-window defined jointly by (0.2) and (2.6) is nonempty
for all sufficiently large \(m\). Indeed,

\[
\mathcal E=\frac{N_{q_0}D_0}{n}
=\frac{N_{q_0+1}D_1}{n}.                                   \tag{2.7}
\]

If \(N_{q_0}=nK_++\rho\), \(0\le\rho<n\), and
\(nK_-=N_{q_0+1}+\sigma\), \(0\le\sigma<n\), then

\[
\frac{\mathcal E}{K_+}
=D_0\left(1+O\!\left(\frac n{N_{q_0}}\right)\right),
\qquad
\frac{\mathcal E}{K_-}
=D_1\left(1-O\!\left(\frac n{N_{q_0+1}}\right)\right).
\tag{2.8}
\]

The interval
\[
\left[\max\!\left\{D_0,\left\lceil\frac{\mathcal E}{K_+}\right\rceil\right\},
\ \min\!\left\{D_1,\left\lfloor\frac{\mathcal E}{K_-}\right\rfloor\right\}\right]
\]
therefore has length
\((D_1-D_0)(1-o(1))=\Theta(D_0/\sqrt m)\), and contains an integer.

These are necessary scalar conditions, not a proof of common integral
colouring.

### Theorem 2.2 (integral resolution implies coefficient one)

If \(\mathrm{CR}(C)\) has an integral solution for some \(C\) satisfying
(0.2), then there is a \(K_+\)-packet family satisfying (0.3).

#### Proof

Let \(\mathcal F_c\) be the family of colour \(c\), and choose a largest
colour. By (2.7),

\[
|\mathcal F_c|\ge\frac{\mathcal E}{C}
=\frac{N_{q_0}D_0}{nC}.                                    \tag{2.9}
\]

It is an entrance matching, so its entrance leave is at most

\[
h_{q_0}
=N_{q_0}-n|\mathcal F_c|
\le N_{q_0}\left(1-\frac{D_0}{C}\right).                    \tag{2.10}
\]

It has no middle collision by (2.4), and (2.5) gives \(h_q=0\) for
every \(q>q_0\).

If \(|\mathcal F_c|<K_+\), add arbitrary packets until the packet count
is \(K_+\). If \(t\) packets are added, then

\[
nt\le N_{q_0}-n|\mathcal F_c|=h_{q_0}.                      \tag{2.11}
\]

Adding packets cannot create holes. It creates at most \(nt\) repeated
physical middle-owner occurrences. Thus the final defect is at most
\(h_{q_0}+nt\le2h_{q_0}\). Finally, \(C\le D_1\) and (1.4) give

\[
1-\frac{D_0}{C}\le\frac{D_1-D_0}{D_0}
=\frac{2q_0+1}{m-q_0}=O_a(m^{-1/2}),
\]

which proves (0.3). \(\square\)

This is a genuine joint statement: no marginal target probabilities
are multiplied. Packetwise complementation identifies the corresponding
upper occurrence supports, so the same \(o(W)\) conclusion holds
two-sidedly. The remaining problem is the integrality of one explicit
configuration system.

## 3. The aggregate leave threshold

Uniformly for \(q=x\sqrt m+O(1)\), \(a\le x\le b\),

\[
\frac{N_q}{W}
=\prod_{j=1}^{q}\frac{m-j+1}{m+j}
=e^{-x^2+O_{a,b}(m^{-1/2})}.                               \tag{3.1}
\]

Euler summation proves (0.5). Therefore a black-box factor theorem with
relative leave \(\eta_m\) on the disjoint union of annular target shores
has absolute guarantee

\[
\eta_m W\left(\sqrt m\int_a^b e^{-x^2}\,dx+O(1)\right).
\]

This is \(o(W)\) exactly under (0.6). Merely \(\eta_m=o(1)\) is
insufficient.

The same threshold appears in an entrance-first proof. A compatible
nested flag assignment which charges at most one hole at each of
\(\Theta(\sqrt m)\) depths to each uncovered entrance target turns
entrance leave \(L_0\) into \(O(\sqrt m\,L_0)\) aggregate leave. Such a
route needs

\[
L_0=o(W/\sqrt m),                                          \tag{3.2}
\]

not merely \(o(N_{q_0})\). Theorem 2.2 avoids this multiplication by
making every deeper leave zero.

## 4. A critical projection trap

Fix \(B\subset[2m]\), \(|B|=m\), and define

\[
\mathcal C_B=
\left\{A\in\binom{[2m]}R:|2|A\cap B|-R|\le1\right\}.        \tag{4.1}
\]

### Theorem 4.1 (central-slice transversal)

Every cyclic rank-\(R\) packet meets \(\mathcal C_B\). Hence

\[
\mathcal U_B:=\binom{[2m]}R\setminus\mathcal C_B
\qquad\text{satisfies}\qquad
\mathcal H_R[\mathcal U_B]=\varnothing.                     \tag{4.2}
\]

#### Proof

For a cyclic order \(\pi\), put

\[
f_j=|I_\pi(j,R)\cap B|.
\]

Every element of \(B\) lies in exactly \(R\) of the \(n\) windows, so

\[
\frac1n\sum_{j=0}^{n-1}f_j=\frac R2.                        \tag{4.3}
\]

Also \(|f_{j+1}-f_j|\le1\). If \(R\) is even, the mean identity and
unit-step property force some \(f_j=R/2\). If \(R\) is odd, they force
one of \((R-1)/2,(R+1)/2\). This is precisely membership in
\(\mathcal C_B\). \(\square\)

### Theorem 4.2 (size and exact point balance)

One has

\[
|\mathcal C_B|=
\begin{cases}
\binom{m}{R/2}^{2},&R\ \text{even},\\[2mm]
2\binom{m}{(R-1)/2}\binom{m}{(R+1)/2},&R\ \text{odd},
\end{cases}                                                \tag{4.4}
\]

and

\[
\frac{|\mathcal C_B|}{N_{q_0}}=
\begin{cases}
\dfrac{2+o(1)}{\sqrt{\pi m}},&R\ \text{even},\\[2mm]
\dfrac{4+o(1)}{\sqrt{\pi m}},&R\ \text{odd}.
\end{cases}                                                \tag{4.5}
\]

Both \(\mathcal C_B\) and \(\mathcal U_B\) are exact \(1\)-designs on
the \(2m\) coordinates.

#### Proof

Equation (4.4) follows by choosing intersections with \(B\) and \(B^c\).
For a uniform \(R\)-set \(A\), \(Z=|A\cap B|\) is hypergeometric with

\[
\mathbb EZ=R/2,\qquad
\operatorname{Var}Z
=\frac{R(2m-R)}{4(2m-1)}
=\frac m8+O_a(1).                                          \tag{4.6}
\]

Stirling's formula in (4.4) gives mass
\((2+o(1))/\sqrt{\pi m}\) at the mean, and the same mass at each of the
two nearest integers in the odd case. This proves (4.5).

Permutations within \(B\), permutations within \(B^c\), and interchange
of \(B,B^c\) act transitively on all coordinates and preserve both
families. Their point degrees are therefore constant. \(\square\)

The trap is at the exact scale relevant to an entrance-first proof. For
an entrance matching \(\mathcal F\), put

\[
z_B(\pi)=|E_R(\pi)\cap\mathcal C_B|.
\]

Disjointness gives

\[
|\mathcal C_B\cap\operatorname{Leave}(\mathcal F)|
=|\mathcal C_B|-\sum_{\pi\in\mathcal F}z_B(\pi).            \tag{4.7}
\]

Double counting packet--slice incidences gives

\[
\mathbb E_{\pi\in\Omega}z_B(\pi)
=\frac{n|\mathcal C_B|}{N_{q_0}}
=
\begin{cases}
(4/\sqrt\pi+o(1))\sqrt m,&R\ \text{even},\\
(8/\sqrt\pi+o(1))\sqrt m,&R\ \text{odd}.
\end{cases}                                                \tag{4.8}
\]

Thus a matching with leave \(o(W/\sqrt m)\) must reproduce a
\(\Theta(\sqrt m)\) central local time per chosen packet. The statement
that every packet has at least one central visit is short by a factor
\(\Theta(\sqrt m)\). Pair codegrees and exact point margins do not force
(4.8).

Theorem 4.1 is a rigorous no-go for a density-only residual lemma:
\(\mathcal U_B\) has density \(1-\Theta(m^{-1/2})\), is exactly
point-balanced, and contains no packet. It does not show that
\(\mathcal U_B\) is reached by a particular greedy process, and it does
not obstruct a global integral solution of \(\mathrm{CR}(C)\).

## 5. Exact remaining theorem

The interval degrees, pair codegrees, nested coefficients, path-thread
multiplicity, scalar window, floor window, and absolute leave threshold
are now exact. The remaining statement is:

> For some integer \(C\) satisfying (0.2) and (2.6), integrally colour
> the directed cyclic packet catalogue so that entrance and middle stars
> are colour-injective and every deeper annular target star is
> colour-surjective; or exhibit a configuration Hall cut for this system.

An integral colouring proves \(o(W)\) aggregate defect by Theorem 2.2.
An ordinary \(o(N)\) factor does not. The central-slice residuals rule out
generic hereditary regeneration, but they are not a global Hall
obstruction. No coefficient-one conclusion is claimed without the
integral coloured resolution.
