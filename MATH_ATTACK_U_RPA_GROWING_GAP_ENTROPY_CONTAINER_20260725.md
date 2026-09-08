# U: the RP\(_A\) growing-gap entropy/container gate

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
web access is used.

All logarithms are natural.

## 0. Outcome

Put

\[
 N=2m+1,
 \qquad B=\operatorname{Cat}_m,
 \qquad H_A=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\). Let \(p_{m,H}\) be the maximum number of pairwise
quotient-edge-disjoint, nonwrapping PBBS return intervals of residence at
most \(H\) on the long \(\tau=\phi^2\) quotient cycles. The exact deck
reduction says

\[
 Np_{m,H}\le \nu_H(P_m)
 \le 2Np_{m,H}+NZ_H,
 \tag{0.1}
\]

where

\[
 Z_H\le(2H+2)N^{2H+2}.
 \tag{0.2}
\]

For \(H=H_A\), (0.2) is \(\exp(o(m))=o(B/N)\). Hence

\[
 \boxed{
 (\mathrm{RP}_A)
 \quad\Longleftrightarrow\quad
 p_{m,H_A}=o_A(B/N).}
 \tag{0.3}
\]

The requested entropy/container theorem is not proved here. Four exact
advances delimit it.

1. If the next omitted-label gap is at most \(2H-1\), the start root has
   height at most \(H-1\), and therefore the number of possible starts is
   at most

   \[
    \left(2\cos\frac{\pi}{H+1}\right)^{2m}.
    \tag{0.4}
   \]

   Thus every fixed gap is exponentially harmless. The exact base-two
   count is presently proved only for gap seven; it must not be asserted
   for every fixed gap.

2. There is a sharpened, literal growing-gap family of actual returns.
   For every fixed \(A>0\),

   \[
   \boxed{
    p_{m,H_A}
    \ge B\exp\left[-\left(
       3(\pi\log2)^{2/3}+o(1)
       \right)m^{1/3}\right].}
   \tag{0.5}
   \]

   Its gap is \(4L+1\), with

   \[
    L=\left(\frac{\pi^2m}{\log2}\right)^{1/3}+O(1).
   \]

   This improves the former mountain-tower constant
   \(3(\pi\log4)^{2/3}\). In particular, no uniform estimate of the form

   \[
    p_{m,H_A}\le B\exp[-\omega(m^{1/3})]
   \]

   can hold.

3. Height and prescribed Pascal slots do not themselves give the needed
   little-oh. For every fixed \(A>0\), there are constants
   \(a_A,\eta_A>0\) and at least

   \[
    \eta_AB
    \tag{0.6}
   \]

   height-\(\le A\sqrt m\) primitive roots with
   \(a_A\sqrt m+O(1)\) successive final root slots equal to zero. These
   roots are not asserted to be PBBS returns. They show that even a
   Gaussian-length slot tower has no entropy contraction without the
   predecessor chronology.

4. The actual predecessor chronology supplies a new branching statistic.
   At a nonwrapping reduced passage of rank \(d\ge2\), if the realized
   prescribed slot is \(z\), then the passage contains \(z+1\) pairwise
   edge-disjoint child returns. The corresponding algebraic
   Pascal-weighted local kernel, before restricting to dynamically realized
   slot values, is

   \[
   \boxed{
    \frac1P\sum_{z=0}^{y}\frac{K_z}{z+1}
    =\frac{2d}{y+1}
       \bigl(H_{y+2d}-H_{2d-1}\bigr),}
   \tag{0.7}
   \]

   where

   \[
    P=\binom{y+2d}{2d},
    \qquad
    K_z=\binom{y-z+2d-1}{2d-1}.
   \]

   This is a genuine chronology-sensitive contraction when \(y/d\) is
   large. It has not been globalized because exponentially many outer
   Pascal lifts may project onto the same child trace.

Consequently the natural exponent-order target is

\[
 \boxed{
 p_{m,H_A}\le B e^{-c_A'm^{1/3}}
 }
 \tag{0.8}
\]

for some \(c_A'>0\). It would prove (0.3), and (0.5) shows that the power
\(m^{1/3}\) is the largest possible power in a uniform
stretched-exponential upper bound. A matching upper bound is not proved;
the true packing could be much larger than the family in (0.5).

---

## 1. Exact normalization and the entropy deficit

A consecutive omitted-label return of odd gap

\[
 g=2\ell-1
\]

has projected residence \(\ell\), and its quotient interval contains

\[
 L_g=\ell+1=\frac{g+3}{2}
 \tag{1.1}
\]

consecutive quotient transition edges. Edge-disjointness always refers to
these edge sets.

Define the quotient packing entropy deficit

\[
 \mathcal E_A(m)
 =\log\frac{B}{p_{m,H_A}}.
 \tag{1.2}
\]

Equation (0.3) is equivalently

\[
 \boxed{
 (\mathrm{RP}_A)
 \quad\Longleftrightarrow\quad
 \mathcal E_A(m)-\log N\longrightarrow+\infty.}
 \tag{1.3}
\]

The best unconditional height/edge split gives

\[
 p_{m,H}
 \le\left(\frac{\sqrt2}{\pi}+o(1)\right)
 B\sqrt{\frac{\log m}{m}}
 \tag{1.4}
\]

uniformly in \(H\). Thus the currently proved lower bound on the deficit is
only

\[
 \mathcal E_A(m)
 \ge\frac12\log\frac{m}{\log m}-O(1),
 \tag{1.5}
\]

whereas (1.3) needs more than \(\log m\). The actual-return construction
of Section 4 gives the opposite inequality

\[
 \mathcal E_A(m)
 \le
 \left(3(\pi\log2)^{2/3}+o(1)\right)m^{1/3}.
 \tag{1.6}
\]

This is the present rigorous entropy window.

For completeness, (1.4) follows directly from the two resources used
below. Choose

\[
 L=\left(\frac{\pi}{\sqrt2}-o(1)\right)
       \sqrt{\frac m{\log m}},
\]

where the \(o(1)\) tends to zero slowly enough that the spectral term is
\(o(B/L)\). Intervals of residence at most \(L\) have start height at most
\(L-1\), so Theorem 2.1 bounds their number by \(o(B/L)\). Every remaining
member of an edge-disjoint family uses at least \(L+2\) of the \(B\)
quotient edges, and hence there are at most \(B/(L+2)\) of them. Substitution
of \(L\) gives (1.4), including its leading constant.

---

## 2. Uniform fixed-gap entropy

Let \(R_{\le 2H-1}(m)\) denote the set of normalized Dyck roots whose
next omitted-label return has gap at most \(2H-1\).

### Theorem 2.1 -- ballot/spectral bound

For every \(m\ge1\) and \(H\ge1\),

\[
 \boxed{
 |R_{\le2H-1}(m)|
 \le\left(2\cos\frac{\pi}{H+1}\right)^{2m}.}
 \tag{2.1}
\]

Consequently

\[
 \boxed{
 \frac{|R_{\le2H-1}(m)|}{B}
 \le(\sqrt\pi+o(1))m^{3/2}
   \exp\left[-\frac{\pi^2m}{(H+1)^2}\right].}
 \tag{2.2}
\]

#### Proof

The PBBS height-gap theorem gives

\[
 \operatorname{ht}(D)\le H-1
\]

for every root in the left side of (2.1). Dyck words of semilength \(m\)
and height at most \(H-1\) are length-\(2m\) closed walks from zero in the
path graph on

\[
 \{0,1,\ldots,H-1\}.
\]

Its adjacency spectral radius is

\[
 2\cos\frac{\pi}{H+1}.
\]

The diagonal walk count is at most the \(2m\)-th power of the operator
norm, proving (2.1). Since

\[
 \cos x\le e^{-x^2/2}
\]

and

\[
 B=\frac{4^m}{\sqrt\pi m^{3/2}}(1+o(1)),
\]

(2.2) follows. \(\square\)

For one fixed odd gap bound \(G\), put \(H=(G+1)/2\). Formula (2.1) has
exponential base

\[
 \boxed{
 4\cos^2\frac{2\pi}{G+3}<4.}
 \tag{2.3}
\]

Thus every fixed-gap family is \(o(B/N)\). The two exact first cases are

\[
 R_5(m)=m-1,
 \qquad
 R_7(m)=2^{m-1}-m.
 \tag{2.4}
\]

Only the second is an exact base-two family. Formula (2.3), not a claimed
universal base-two classification, is the correct fixed-gap theorem.

The same calculation shows that total starts are \(o(B/m)\) whenever

\[
 \frac{\pi^2m}{H^2}-\frac52\log m\longrightarrow+\infty.
 \tag{2.5}
\]

It stops strictly below a Gaussian window.

---

## 3. Exact one-level passage certificate

Let \(D\in\mathcal D_m\), put

\[
 E=\partial D\in\mathcal D_d,
 \qquad k=\operatorname{pk}(E),
 \qquad p=2d+1,
 \qquad y=m-d-k.
 \tag{3.1}
\]

The inverse leaf-pruning fibre is the weak-composition simplex of \(y\)
free leaves in \(p\) ordered slots, and hence has size

\[
 P_m(E)=\binom{y+2d}{2d}.
 \tag{3.2}
\]

Let \(\kappa_t(E)\in\mathbb Z_p\) be the reduced PBBS omitted-particle
label, normalized by \(\kappa_0=0\), and put

\[
 n_j(g)=|\{0\le t<g:\kappa_t(E)=j\}|.
 \tag{3.3}
\]

For \(g<N\), the root \(D\) starts a consecutive physical return of gap
\(g\) if and only if

\[
 \kappa_g(E)=-1,
 \qquad
 \min\{t>0:\kappa_t(E)=0\}<g,
 \tag{3.4}
\]

\[
 n_{-1}(g)=2z+1,
 \qquad
 z_*(D)=z,
 \tag{3.5}
\]

where \(z_*(D)\) is the final root-slot occupancy. For fixed \((E,g)\),
the number of permitted lifts is exactly

\[
 K_m(E,g)
 =\binom{y-z+2d-1}{2d-1}.
 \tag{3.6}
\]

This certificate contains two logically different restrictions:

* the Pascal condition fixes one slot;
* the dynamical condition specifies an ordered
  \(0\cdots0\cdots(-1)\) predecessor passage.

Section 5 proves that the first condition alone cannot close (0.3).
Section 6 extracts a new packing consequence from the second.

---

## 4. A sharpened growing-gap family of actual returns

This section proves (0.5).

Choose integers

\[
 L\longrightarrow\infty,
 \qquad
 Q=\lfloor\sqrt L\rfloor,
 \qquad
 2L+Q(2L-Q-1)<m.
 \tag{4.1}
\]

The last inequality holds for the optimized \(L=\Theta(m^{1/3})\).

### 4.1 The decorated terminal-spine family

Construct a rooted plane tree as follows.

1. Begin with a distinguished last-child spine of length \(2L\).
2. At the root, before the spine child, insert an arbitrary ordered forest
   all of whose branches have height at most \(L\).
3. At each spine vertex of depths

   \[
    1,2,\ldots,2L-Q-1,
   \]

   before its last spine child, insert an arbitrary ordered forest of total
   edge size at most \(Q\).
4. Leave the last \(Q\) spine vertices undecorated.

The conservative upper depth \(2L-Q-1\) gives strict height separation:
every small side forest has height at most \(Q\), while the remaining spine
has height greater than \(Q\). Thus the distinguished spine and every
decoration are uniquely recoverable. Different choices give different
Dyck roots.

Every small decoration disappears in fewer than \(L\) simultaneous leaf
prunings. The root forest has height at most \(L\), so it also disappears
after \(L\) prunings. The last \(L\) spine edges disappear, leaving

\[
 \boxed{\partial^L D=1^L0^L.}
 \tag{4.2}
\]

The contour still ends in the uninterrupted descent

\[
 0^{2L}.
 \tag{4.3}
\]

The terminal-tower flux lemma therefore applies with compressed mountain
rank \(d=L\). In that mountain PBBS, particle \(-L\) is selected first at
time \(2L\) and for the second time at

\[
 (2L+1)+2L=4L+1.
\]

No overtaking is possible, and \(4L+1<N\). Hence every constructed root
starts a consecutive return of the exact gap

\[
 \boxed{g=4L+1.}
 \tag{4.4}
\]

Its residence is \(2L+1\), and its quotient interval has exactly

\[
 2L+2
 \tag{4.5}
\]

edges.

### 4.2 Exact count

Let \(C_L(z)\) be the generating function of ordered forests whose branch
height is at most \(L\); equivalently it is the height-\(L\) Catalan
generating function. Put

\[
 F_Q(z)=\sum_{j=0}^{Q}\operatorname{Cat}_jz^j,
 \qquad
 s=2L-Q-1,
 \qquad
 M=m-2L.
 \tag{4.6}
\]

The root forest contributes \(C_L(z)\), each of the \(s\) small-decoration
sites contributes \(F_Q(z)\), and the spine contributes \(2L\) fixed
edges. Therefore the number of constructed semilength-\(m\) roots is
exactly

\[
 \boxed{
 a_m(L,Q)=[z^M]C_L(z)F_Q(z)^s.}
 \tag{4.7}
\]

Put

\[
 \theta=\frac{\pi}{L+2},
 \qquad
 \lambda=2\cos\theta,
 \qquad
 \rho=\lambda^{-2},
 \tag{4.8}
\]

and

\[
 \alpha_L=\frac4{L+2}\sin^2\theta.
 \tag{4.9}
\]

The two extreme eigenmodes of the path graph on
\(\{0,1,\ldots,L\}\) give, for every \(n\ge0\),

\[
 [z^n]C_L(z)\ge\alpha_L\lambda^{2n}.
 \tag{4.10}
\]

Since \(sQ<M\), convolution in (4.7) and (4.10) gives

\[
 \boxed{
 a_m(L,Q)
 \ge\alpha_L\lambda^{2M}F_Q(\rho)^s.}
 \tag{4.11}
\]

Now

\[
 \rho=\frac14\left(1+O(L^{-2})\right).
\]

Uniformly for \(0\le j\le Q=\sqrt L+O(1)\),

\[
 (4\rho)^j=1+o(1).
\]

Also

\[
 \sum_{j>Q}\operatorname{Cat}_j4^{-j}=O(Q^{-1/2}).
\]

Consequently

\[
 F_Q(\rho)=2-o(1),
 \qquad
 s\log F_Q(\rho)=2L\log2+o(L).
 \tag{4.12}
\]

Finally,

\[
 \log\lambda^2
 =\log4-\frac{\pi^2}{L^2}+O(L^{-3}),
 \tag{4.13}
\]

where replacing \((L+2)^{-2}\) by \(L^{-2}\) changes the final expression
by \(o(L)\) in the range used below. Equations (4.11)--(4.13), together
with \(B=4^m m^{-3/2+o(1)}\), yield

\[
 \boxed{
 \log\frac{B}{a_m(L,Q)}
 \le2L\log2+\frac{\pi^2m}{L^2}+o(L).}
 \tag{4.14}
\]

The right side is minimized when

\[
 L^3=\frac{\pi^2m}{\log2}.
 \tag{4.15}
\]

For

\[
 L=\left\lfloor
 \left(\frac{\pi^2m}{\log2}\right)^{1/3}
 \right\rfloor,
 \tag{4.16}
\]

we obtain

\[
 \boxed{
 \log\frac{B}{a_m(L,Q)}
 \le
 \left(3(\pi\log2)^{2/3}+o(1)\right)m^{1/3}.}
 \tag{4.17}
\]

### 4.3 Edge-disjoint extraction

Discard constructed starts lying on quotient cycles of length at most
\(H_A+1\), as required by the definition of \(p_{m,H_A}\). Their number is
at most \(Z_{H_A}=\exp(o(m))\), whereas
\(a_m(L,Q)=\exp(m\log4-o(m))\). Thus the discarded fraction is \(o(1)\).

All remaining intervals have the common length \(2L+2\). One such interval
can meet intervals whose start lies in at most

\[
 2(2L+2)-1=4L+3
\]

positions on its quotient cycle. Greedy selection therefore gives

\[
 p_{m,H_A}
 \ge\frac{a_m(L,Q)-Z_{H_A}}{4L+3}.
 \tag{4.18}
\]

Because \(2L+1=o(\sqrt m)\), the residence lies below \(H_A\) for every
fixed \(A>0\) and all sufficiently large \(m\). The polynomial divisor in
(4.18) is absorbed by the \(o(m^{1/3})\) term. Equations (4.17)--(4.18)
prove (0.5). \(\square\)

---

## 5. Slot-only containers fail at the target scale

Let \(\mathcal D_{m,h}\) be the set of semilength-\(m\) Dyck paths of
height at most \(h\), viewed as rooted plane trees. Cyclically rotate the
ordered list of root children. Each orbit has size at most the root degree,
hence at most \(m\). Every orbit has a representative whose last root child
has maximum height.

Let \(\mathcal Z_{m,h}\) contain one such representative from every orbit.
Then

\[
 |\mathcal Z_{m,h}|\ge\frac{|\mathcal D_{m,h}|}{m}.
 \tag{5.1}
\]

Put

\[
 \theta_h=\frac{\pi}{h+2}.
\]

Keeping the two extreme eigenmodes in the path-graph walk formula gives

\[
 |\mathcal D_{m,h}|
 \ge\frac4{h+2}\sin^2\theta_h
       (2\cos\theta_h)^{2m}.
 \tag{5.2}
\]

For \(h=\lfloor A\sqrt m\rfloor\), Catalan asymptotics turn (5.1)--(5.2)
into

\[
 \boxed{
 |\mathcal Z_{m,h}|
 \ge(c_A+o(1))\frac{B}{m},
 \qquad
 c_A=\frac{4\pi^{5/2}}{A^3}e^{-\pi^2/A^2}.}
 \tag{5.3}
\]

It remains to identify the slots. Write the root-child heights of a tree in
\(\mathcal Z_{m,h}\) as

\[
 H_1,\ldots,H_s,
 \qquad H_s=\max_iH_i.
\]

After \(j\) peak-deletion rounds, precisely the original root children of
height greater than \(j\) survive. At every level at which the next pruned
tree is nonempty, the last original child remains last and nonleaf. Hence no
new leaf child lies after it in the inverse-pruning description. The final
root slot is zero at every nonterminal level.

Therefore Gaussian height plus prescribing zero throughout every available
nonterminal slot tower still permits at least \(\Omega_A(B/m)\) roots. This does
not disprove (\(\mathrm{RP}_A\)), because no return chronology has been
proved for \(\mathcal Z_{m,h}\). It proves that the chronology cannot be
discarded in a valid container theorem.

The loss of the factor \(m\) in (5.1) is unnecessary if one asks for a
linearly long slot tower.

### Theorem 5.1 -- positive Catalan mass with Gaussian many zero slots

For every fixed \(A>0\), there are constants

\[
 0<a_A<A,
 \qquad \eta_A>0
\]

such that, for all sufficiently large \(m\), at least \(\eta_AB\)
primitive semilength-\(m\) Dyck roots have height at most \(A\sqrt m\)
and have final root slot zero at every one of their first

\[
 \lfloor a_A\sqrt m\rfloor-2
 \tag{5.4}
\]

peak-deletion levels.

#### Proof

Write a primitive root as

\[
 D=1E0,
 \qquad E\in\mathcal D_{m-1}.
\]

Let \(C_{n,h}\) denote the number of semilength-\(n\) Dyck paths of height
at most \(h\). The exact path-graph expansion is

\[
 C_{n,h}
 =\frac2{h+2}\sum_{j=1}^{h+1}
   \sin^2\frac{j\pi}{h+2}
   \left(2\cos\frac{j\pi}{h+2}\right)^{2n}.
 \tag{5.5}
\]

At \(h=\lfloor A\sqrt m\rfloor-1\), retaining the two extreme modes as in
(5.2) gives

\[
 \liminf_{m\to\infty}
 \frac{C_{m-1,h}}B
 \ge
 \frac{\pi^{5/2}}{A^3}e^{-\pi^2/A^2}
 =:L_A>0.
 \tag{5.6}
\]

On the other hand, (5.5), together with

\[
 \sin x\le x,
 \qquad
 |\cos x|^{2m}\le e^{-c m\,\operatorname{dist}(x,\pi\mathbb Z)^2},
\]

gives, for \(h=\lfloor a\sqrt m\rfloor\),

\[
 \limsup_{m\to\infty}\frac{C_{m-1,h}}B
 \le
 C a^{-3}\sum_{j\ge1}j^2e^{-c'j^2/a^2}
 =:U(a),
 \tag{5.7}
\]

for absolute positive \(C,c'\). In particular \(U(a)\to0\) as
\(a\downarrow0\). Choose \(a_A<A\) so that \(U(a_A)<L_A/2\). Equations
(5.6)--(5.7) show that at least

\[
 (L_A/2+o(1))B
\]

choices of \(E\) have height between \(a_A\sqrt m\) and
\(A\sqrt m-1\). Their primitive suspensions \(D=1E0\) have height at most
\(A\sqrt m\).

The root of every such tree has one child. Before that child subtree is
extinguished, every pruned tree again has one last root child and no new
leaf child after it. Hence every nonterminal final root slot is zero. The
lower height bound supplies at least (5.4) such levels. Taking, for example,
\(\eta_A=L_A/4\) for all sufficiently large \(m\) proves the theorem.
\(\square\)

Theorem 5.1 is a purely structural no-go. None of its primitive roots is
claimed to satisfy a predecessor passage.

---

## 6. The predecessor chronology branches

We now use information absent from Section 5.

### Theorem 6.1 -- one passage contains \(z+1\) disjoint child returns

Let \(E\in\mathcal D_d\), with \(d\ge2\), satisfy the reduced predecessor
passage criterion at time \(g\), and assume

\[
 g<2d+1.
\]

Suppose

\[
 n_{-1}(g)=2z+1.
\]

List all occurrences of the predecessor label \(-1\) before and at the
final time as

\[
 u_1<u_2<\cdots<u_{2z+1}<u_{2z+2}=g.
 \tag{6.1}
\]

Then:

1. each interval \([u_i,u_{i+1}]\) is a consecutive same-label PBBS
   return;
2. every gap \(u_{i+1}-u_i\) is odd and at least five;
3. the alternating family

   \[
    [u_1,u_2], [u_3,u_4],\ldots,
    [u_{2z+1},u_{2z+2}]
   \]

   gives \(z+1\) pairwise step-two-edge-disjoint child residence intervals;
4. all child gaps are at most \(g\), and

   \[
    \boxed{5(2z+1)\le g.}
    \tag{6.2}
   \]

#### Proof

The times in (6.1) are consecutive occurrences of one omitted particle
label, so every successive difference is a consecutive same-label gap.
All such gaps are odd. The no-gap-three theorem applies in rank \(d\ge2\),
so every difference is at least five.

For the gap \([u_i,u_{i+1}]\), the exact projected transition-edge set is

\[
 I_i=\{u_i-1,u_i+1,\ldots,u_{i+1}\}.
\]

For selected indices \(i,i+2\), the intervening gap is at least five, so

\[
 \min I_{i+2}=u_{i+2}-1
 \ge u_{i+1}+4>\max I_i.
\]

The hypothesis \(g<2d+1\) excludes a reduced-cycle wrap. Hence the
alternating family is pairwise step-two-edge-disjoint and has \(z+1\)
members. Finally,

\[
 \sum_{i=1}^{2z+1}(u_{i+1}-u_i)=g-u_1\le g.
\]

Each summand is at least five, proving (6.2). \(\square\)

The theorem explains why a large prescribed slot is not merely a Pascal
choice: it certifies many disjoint child returns in the reduced chronology.
The gap-seven obstruction is one exact example on the boundary \(z=0\).
In particular, every nonwrapping rank-\(d\ge2\) passage obeys the exact
horizon consequence

\[
 \boxed{z\le\left\lfloor\frac{g-5}{10}\right\rfloor.}
 \tag{6.3a}
\]

### Theorem 6.2 -- exact harmonic Pascal kernel

Fix a rank-\(d\) core, where \(d\ge1\), and let \(y\) be its free-leaf count in an outer
inverse fibre. Put

\[
 P=\binom{y+2d}{2d},
 \qquad
 K_z=\binom{y-z+2d-1}{2d-1}
 \quad(0\le z\le y).
 \tag{6.3}
\]

Then

\[
 \boxed{
 \frac1P\sum_{z=0}^{y}\frac{K_z}{z+1}
 =\frac{2d}{y+1}
   \bigl(H_{y+2d}-H_{2d-1}\bigr).}
 \tag{6.4}
\]

#### Proof

Define

\[
 S_{d,y}=\sum_{z=0}^{y}\frac{K_z}{z+1}.
\]

With \(x\) formal,

\[
\begin{aligned}
 \sum_{y\ge0}S_{d,y}x^y
 &=\left(\sum_{t\ge0}\binom{t+2d-1}{2d-1}x^t\right)
   \left(\sum_{z\ge0}\frac{x^z}{z+1}\right)\\
 &=(1-x)^{-2d}\frac{-\log(1-x)}x.
\end{aligned}
 \tag{6.5}
\]

Coefficient extraction, or differentiation of
\((1-x)^{-a}\) in \(a\), gives

\[
 S_{d,y}
 =\binom{y+2d}{2d}
   \frac{2d}{y+1}
   (H_{y+2d}-H_{2d-1}),
\]

which is (6.4). \(\square\)

In particular,

\[
 \frac{S_{d,y}}P
 \sim\frac{2d}{y}\log\left(1+\frac y{2d}\right)
 \qquad(y/d\to\infty).
 \tag{6.6}
\]

Thus large-free-leaf fibres genuinely contract after weighting a slot-\(z\)
passage by the reciprocal of its \(z+1\) disjoint child returns. At the
already-audited outer Pascal saddle

\[
 d\sim m/2,
 \qquad y\sim m/3,
\]

(6.4) tends to

\[
 3\log(4/3)<1.
 \tag{6.7}
\]

This is a real one-level gain, unlike the unweighted slot ratio.

### Why this does not yet prove RP\(_A\)

Peak deletion semiconjugates the traces but has exponential projection
congestion: different outer Pascal vectors can collapse onto the same
ordered child intervals. Theorem 6.1 gives disjoint children inside each
one reduced trace; it does not make child traces belonging to different
outer lifts distinct in the unlabelled reduced quotient. To iterate (6.4),
one needs either

* a capacitated clone space retaining the transported outer slot vector;
  or
* a theorem that different saddle fibres decorrelate across the two-label
  passage genealogy.

Neither has been proved. Moreover, on the already-audited harmonic saddle
profile, \(y_j/d_j=O(j^{-2})\), so the product of the local factors in
(6.4) need not vanish automatically. The global contraction must use the
actual ordered child passages, not only their number.

---

## 7. Exact pruning-profile container

There is a useful closed product on which a future dynamic container can be
built.

Let

\[
 D^{(j)}=\partial^jD,
 \qquad
 r_j=\text{semilength}(D^{(j)}),
 \qquad
 \ell_j=r_j-r_{j+1}.
 \tag{7.1}
\]

Then \(\ell_j=\operatorname{pk}(D^{(j)})\). Peak deletion semiconjugates
PBBS, and peak count is PBBS-invariant at every rank, so the whole profile

\[
 \ell_0\ge\ell_1\ge\cdots>0,
 \qquad
 \sum_j\ell_j=m,
 \tag{7.2}
\]

is a quotient-orbit invariant.

The monotonicity in (7.2) is elementary: every leaf created by pruning is
the parent of at least one leaf deleted in that round, and distinct new
leaves have disjoint deleted child sets. Hence the number of leaves cannot
increase under pruning.

Fix such a finite profile, ending in its unique terminal star. The exact
number of Dyck roots with that profile is

\[
 \boxed{
 M(\boldsymbol\ell)
 =\prod_{j=0}^{h-2}
   \binom{\ell_j-\ell_{j+1}+2r_{j+1}}{2r_{j+1}}.}
 \tag{7.3}
\]

Indeed, in the inverse step \(D^{(j+1)}\mapsto D^{(j)}\), the number of
free leaves is

\[
 r_j-r_{j+1}-\operatorname{pk}(D^{(j+1)})
 =\ell_j-\ell_{j+1},
\]

and there are \(2r_{j+1}+1\) slots.

If \(0\le L\le h-1\) and the final slots at levels \(j<L\) are prescribed to be \(z_j\), the
exact profile-container count is

\[
 \boxed{
 M(\boldsymbol\ell;\mathbf z)
 =\prod_{j=0}^{L-1}
   \binom{\ell_j-\ell_{j+1}-z_j+2r_{j+1}-1}
         {2r_{j+1}-1}
 \prod_{j=L}^{h-2}
   \binom{\ell_j-\ell_{j+1}+2r_{j+1}}
         {2r_{j+1}},}
 \tag{7.4}
\]

with inadmissible factors interpreted as zero.

The formula is exact even after summing over all shapes lower in the tower,
because every factor depends only on adjacent profile ranks. Actual returns
choose the \(z_j\)'s state-dependently through predecessor passages. The
remaining problem is therefore a dynamic restriction on which pairs

\[
 (g_{j+1},z_j)
 \tag{7.5}
\]

are realizable along one invariant profile; (7.3)--(7.4) alone do not
restrict them enough.

---

## 8. Exact proved and unproved boundary

### Proved

1. The quotient normalization (0.3).
2. The fixed-gap spectral base (2.3), including the exact special counts
   (2.4).
3. The decorated terminal-spine return theorem, exact gap \(4L+1\), exact
   coefficient (4.7), entropy constant
   \(3(\pi\log2)^{2/3}\), and edge-disjoint extraction (4.18).
4. The slot-only obstructions (5.3) and Theorem 5.1, the latter giving
   positive Catalan mass with \(\Theta_A(\sqrt m)\) successive zero slots.
5. The \(z+1\) disjoint-child theorem and horizon bound (6.2).
6. The harmonic Pascal kernel (6.4), including the saddle contraction
   \(3\log(4/3)\).
7. The invariant pruning-profile products (7.3)--(7.4).

### Not proved

1. A global clone/capacity induction which iterates (6.4).
2. Passage decorrelation across the dangerous Pascal saddle.
3. Any bound of the form (0.8).
4. \((\mathrm{RP}_A)\), and therefore the constant-one theorem through
   this route.

The exact remaining entropy statement is not merely that growing-gap roots
have sub-Catalan exponential rate; (0.5) disproves that. It is the
polynomially normalized, chronology-sensitive container

\[
 \boxed{
 p_{m,H_A}=o_A(B/N),}
\]

or the stronger exponent-order estimate (0.8). Height, peak-deletion rank,
pruning profile, and prescribed slots are all insufficient separately. The
new local statistic which a successful proof must globalize is the ordered
family of predecessor child returns certified by Theorem 6.1.

---

## 9. Independent audit

The decisive decorated-family argument was checked independently in four
places.

1. **Pruning:** every side decoration has height below \(L\); after \(L\)
   rounds the remaining core is exactly the length-\(L\) mountain.
2. **Chronology:** the terminal descent supplies the required adjacent
   equality particles, and the compressed mountain selects particle
   \(-L\) at times \(2L\) and \(4L+1\). Thus the latter is the first outer
   re-entry.
3. **Enumeration:** the last-child spine is recoverable, (4.7) is an exact
   coefficient, and the two extreme path-graph eigenmodes give (4.10) with
   the displayed prefactor.
4. **Asymptotics and packing:** \(F_Q(\rho)=2-o(1)\), the optimized constant
   is \(3(\pi\log2)^{2/3}\), short cycles have negligible mass, and an
   interval of \(2L+2\) edges has conflict neighbourhood at most
   \(4L+3\).

The child-return and harmonic-kernel proofs were separately derived from
the exact predecessor occurrence list and the weak-composition generating
function. No implication from these local facts to (\(\mathrm{RP}_A\)) is
claimed.
