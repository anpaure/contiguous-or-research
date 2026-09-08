# Critical PBBS packing: the one-defect terminal rotor and the first cross-level carry

Date: 2026-07-25

Method: pure mathematics only. No finite search, solver, computation, or
external input is used.

## 0. Outcome

Let a genuine first zero-winding PBBS return have height/duration \(s\),
ambient Dyck semilength \(r\), first-mountain pruning depth \(p\), and

\[
q=s-p,\qquad b=2q-p+1.
\]

Throughout the unsaturated sector \(p<2q\), one has \(b\ge2\). This note
settles the terminal part of the coefficient-one-critical window
\(p\asymp q\asymp\sqrt r\).

1. For every fixed \(\varepsilon>0\), the profiles with
   \(p\ge\varepsilon\sqrt r\) and final curvature \(y_p\ge2\) have total
   capacity

   \[
   O_{A,\varepsilon}(4^r/r^{5/2})
   =o(\operatorname {Cat}_r/\sqrt r).
   \]

   Together with the separately proved two-limit deletion of
   \(p=o(\sqrt r)\), this is negligible. The sector \(b=o(p)\) is also
   negligible in the required two-limit sense. The actual terminal PBBS
   theorem below then forces all terminal fan values to be zero. Thus the
   sole capacity-critical terminal state is

   \[
   p,q,b\asymp\sqrt r,\qquad y_p=1,
   \qquad\hbox{all \(p\) terminal fan values equal zero}.       \tag{0.1}
   \]

2. The residual terminal fibre is an exact actual-PBBS rotor. The
   \(2q+1\) inverse lifts of the mountain \(M_q=1^q0^q\) form one
   \(\tau\)-cycle. All but one rotor state start the exact tight
   zero-winding return of duration \(q+1\), and every such return has
   endpoint excess zero. Requiring the \(p\) terminal descendants of the
   outer fan leaves exactly

   \[
   2q+1-p=b
   \]

   rotor states. Hence the all-zero terminal fan envelope is attained by
   genuine PBBS chronology. There is no terminal profile--boundary saving.

3. Two starts on one common inverse tower force literal cyclic slot
   blocks. Their union size, common-fibre capacity, and overlapping-slot
   local-time equations are exact. Starts locked in the same bottom
   residue class acquire an exact \(+2k\) next-level carry after
   \(k(2q+1)\) phases.

4. A phase-union theorem proves that any upper transport periodic with
   period \(d=o(b)\) already gives the required little-oh. More generally,
   a saturating obstruction must have bounded weighted phase multiplicity:
   the union of the transported phase sets must have the same order as
   the sum of their sizes.

Coefficient one is **not** proved. Every positive endpoint boundary is
created strictly above the terminal rotor. The exact residual is a
low-overlap upper-inverse boundary/rotor non-tiling theorem. The outer
\(\Lambda=0\) sector already has the proved stronger
\(O_A(\operatorname {Cat}_r/r)\) quotient bound, so only positive outer
boundary is retained below.

## 1. The profile series

Put

\[
Q_0(z)=Q_1(z)=1,\qquad
Q_{j+1}(z)=Q_j(z)-zQ_{j-1}(z),\qquad
C_j(z)=\frac{Q_j(z)}{Q_{j+1}(z)}.
\]

The audited full-depth zero-value fan-capacity series is

\[
\mathscr F^\star_{s,p}(z)
=\frac{C_p(z)^b}{Q_p(z)^3}
\left[1-\left(1-\frac{z^p}{Q_p(z)^2}\right)^b\right],          \tag{1.1}
\]

and

\[
\mathcal E_{r;s,p}=[z^{r-s}]\mathscr F^\star_{s,p}(z).         \tag{1.2}
\]

For a profile, let \(y_j=r_{j-1}-2r_j+r_{j+1}\). At the terminal level
\(y_p\ge1\). Put

\[
t=t_p(z)=\frac{z^p}{Q_p(z)^2},\qquad
\mathscr F_{<p}(z)=\frac{C_{p-1}(z)^{b+3}}{Q_{p-1}(z)^3}.
\]

Then

\[
\mathscr F^\star_{s,p}
=\mathscr F_{<p}\big((1-t)^{-b}-1\big).           \tag{1.3}
\]

At \(z=1/4\),

\[
Q_j(1/4)=\frac{j+1}{2^j},\qquad t_p(1/4)=\frac1{(p+1)^2}.       \tag{1.4}
\]

## 2. Only one terminal unit remains critical

### Theorem 2.1

Fix \(A>0\).

1. For every \(\varepsilon>0\), the total envelope with

   \[
   s\le A\sqrt r,\qquad p\ge\varepsilon\sqrt r,\qquad y_p\ge2
   \]

   is \(O_{A,\varepsilon}(4^r/r^{5/2})\).

2. For fixed \(\varepsilon,\delta>0\), the zero-value envelope with
   \(p\ge\varepsilon\sqrt r\) and \(b<\delta p\) is at most

   \[
   C_{A,\varepsilon}\delta^2\frac{4^r}{r^2}
   +O_{A,\varepsilon}(4^r/r^{5/2}).               \tag{2.1}
   \]

Thus, after the \(r\to\infty\) limsup and then
\(\delta\downarrow0\), the proved two-limit deletion of
\(p=o(\sqrt r)\) leaves only (0.1).

#### Proof

The exact \(y_p\ge2\) series is

\[
\mathscr F_{\ge2}
=\mathscr F_{<p}\big((1-t)^{-b}-1-bt\big).        \tag{2.2}
\]

Let \(x=(p+1)^{-2}\). Normalizing \((1-t)^{-b}\) at \(1/4\), its count
variable \(Y\) is negative-binomial, so

\[
\Pr(Y\ge2)
\le\frac12\mathbb E[Y(Y-1)]
=\frac{b(b+1)x^2}{2(1-x)^2}.                     \tag{2.3}
\]

The unconditioned critical prefactor is

\[
4^{-s}\mathscr F_{<p}(1/4)(1-x)^{-b}
=\frac{2}{(p+1)^3}
 \left(\frac{p+1}{p+2}\right)^b
\le\frac{2}{(p+1)^3}.                             \tag{2.4}
\]

On \(p\ge\varepsilon\sqrt r\),
\(b\le2A\sqrt r\le(2A/\varepsilon)p\). Hence

\[
4^{-s}\mathscr F_{\ge2}(1/4)
\le C_{A,\varepsilon}p^{-5}.                     \tag{2.5}
\]

We check the coefficient tilt rather than comparing coefficients from
(2.5). Let

\[
T_b(u)=(1-u)^{-b}-1-bu.
\]

For \(0\le u<1\),

\[
\binom{b+1}{2}u^2
\le T_b(u)
\le\binom{b+1}{2}u^2(1-u)^{-b-2}.                \tag{2.6}
\]

At

\[
z_p=\frac14\left(1+\frac{\kappa}{p^2}\right)
\]

with fixed sufficiently small \(\kappa>0\), the continuant root formula
gives \(t_p(z_p)\asymp p^{-2}\). Since \(b=O_{A,\varepsilon}(p)\),
(2.6) makes the terminal tail partition ratio \(O_{A,\varepsilon}(1)\).
The remaining \(\mathscr F_{<p}\) ratio is
\(\exp(O(1+b/p))=O_{A,\varepsilon}(1)\), and its independent
\(1/Q_{p-1}\) factor has largest normalized tilted atom \(O(p^{-2})\).
As \(r-s\ge r/2\) for large \(r\), coefficient tilting yields

\[
[z^{r-s}]\mathscr F_{\ge2}
\le C_{A,\varepsilon}4^r p^{-7}e^{-cr/p^2}.       \tag{2.7}
\]

There are \(O_A(r)\) pairs \((s,p)\), and
\(p\ge\varepsilon\sqrt r\); summing (2.7) proves part 1.

Finally, the proved cell estimate is

\[
\mathcal E_{r;s,p}
\le C_A4^r\frac{b}{(p+1)^7}
\exp\left(-\frac{cr}{p^2}+\frac{Cb}{p}\right).    \tag{2.8}
\]

In the present \(p\)-range the exponential is bounded in terms of
\(A,\varepsilon\), and

\[
\sum_{b<\delta p}b\le\frac12\delta^2p^2+O(\delta p).
\]

Summing \(p^{-5}\) over \(O(\sqrt r)\) values \(p\asymp\sqrt r\)
proves part 2. Since \(p<2q\), the residual also has
\(q\ge p/2\asymp\sqrt r\). \(\square\)

For clarity, a fixed nonzero prescription vector in the \(y_p=1\)
simplex has one completion rather than \(b\), but summing over the \(p\)
possible unit vectors can lose that factor. No aggregate estimate is
claimed from this observation. Theorem 3.0 instead proves dynamically
that an actual terminal tight fan has zero prescriptions.

## 3. The exact one-defect mountain rotor

### Theorem 3.0 (the full terminal simplex is a PBBS rotor)

Fix \(q\ge1\) and \(y\ge1\). The inverse lifts of \(M_q\) having free
mass \(y\) are naturally the weak compositions

\[
\mathbf z=(z_0,\ldots,z_{2q})\in\mathbb Z_{\ge0}^{\,2q+1},
\qquad \sum_i z_i=y.                              \tag{3.0a}
\]

In these coordinates, \(\tau\) rotates the vector by one cyclic place.
A state starts a tight zero-winding return of duration \(q+1\), below its
parent circumference, if and only if

\[
z_0=0.                                            \tag{3.0b}
\]

At phase \(t\), the corresponding condition is that the exposed rotation
of \(z_0\) vanish. Hence \(p\) consecutive terminal descendant returns
are equivalent to one cyclic block of \(p\) zero coordinates. Their exact
number in the terminal inverse fibre is

\[
\boxed{\binom{y+(2q+1-p)-1}{(2q+1-p)-1}
=\binom{y+b-1}{b-1}.}                             \tag{3.0c}
\]

Every return in (3.0b) has endpoint excess zero.

#### Proof

Write the inverse lift in ordered slot coordinates as

\[
\begin{aligned}
D(\mathbf a,c,\mathbf b)
={}&(10)^{a_0}1(10)^{a_1}1\cdots
(10)^{a_{q-1}}1(10)^{c+1}0\\
&\quad (10)^{b_{q-1}}0\cdots0(10)^{b_0},
\end{aligned}                                     \tag{3.0d}
\]

where

\[
\sum_i a_i+c+\sum_i b_i=y.
\]

The factor \((10)^{c+1}\) includes the one mandatory new leaf at the old
leaf of the path tree. Put

\[
\mathbf z=(b_0,a_0,\ldots,a_{q-1},c,
            b_{q-1},\ldots,b_1),                  \tag{3.0e}
\]

with the final tail empty when \(q=1\). Direct substitution of (3.0d) in
the canonical map \(\tau D=S1P0R\) gives a lift with slot vector

\[
z'_0=z_{2q},\qquad z'_i=z_{i-1}\quad(1\le i\le2q),             \tag{3.0f}
\]

so (3.0e) rotates by one place, last coordinate to first.

The same canonical factorization gives

\[
d(D)=1+2z_0,\qquad
\delta(D)=q+1+2\sum_{i=1}^{q}z_i.                 \tag{3.0g}
\]

During \(h=q+1\) successive rotations,

\[
\sum_{j=0}^{q}d(\tau^jD)
=q+1+2\left(z_0+\sum_{i=q+1}^{2q}z_i\right),      \tag{3.0h}
\]

whereas

\[
\delta(\tau^{q+1}D)
=q+1+2\sum_{i=q+1}^{2q}z_i.                      \tag{3.0i}
\]

Thus the exact zero-winding ledger holds if and only if \(z_0=0\).
Every lift has height \(q+1\). Its semilength is \(q+1+y\), so the gap
\(2q+3\) is below the circumference
\(2q+2y+3\); the height-gap theorem then makes the return first and
consecutive. The critical first-mountain condition has \(y=y_p\ge1\), so
this is the only case used below.

At phase \(t\), rotation exposes one cyclic coordinate. Requiring \(p\)
successive returns therefore fixes \(p\) distinct coordinates to zero.
Stars and bars on the remaining \(2q+1-p=b\) coordinates proves (3.0c).

Finally, when \(z_0=0\), (3.0g) and its \(q+1\)-shift give

\[
\delta(D)+\delta(\tau^{q+1}D)
=2(q+1)+2\sum_{i=0}^{2q}z_i
=2(q+1+y),
\]

twice the parent semilength. Thus the endpoint excess is zero. \(\square\)

### Theorem 3.1

The inverse peak-deletion fibre over \(M_q=1^q0^q\) with free mass
\(y=1\) consists of the following \(2q+1\) rank-\((q+2)\) words:

\[
A_i=1^i10\,1^{q+1-i}0^{q+1}\quad(0\le i\le q),                  \tag{3.1}
\]

\[
B_i=1^{q+1}0^{q+1-i}10\,0^i\quad(0\le i<q).                    \tag{3.2}
\]

They form the single cycle

\[
A_0\to A_1\to\cdots\to A_q\to
B_{q-1}\to\cdots\to B_0\to A_0.                 \tag{3.3}
\]

Every state except \(B_0\) starts a genuine first zero-winding return of
duration \(h=q+1\), gap \(2q+3\), and endpoint excess zero.

#### Proof

The path tree \(M_q\) has one old leaf. One new leaf is mandatory there,
and the one free leaf may occupy any of \(2q+1\) ordered child slots.
These are exactly (3.1)--(3.2). Direct simultaneous deletion of the two
new peaks gives \(M_q\), so the fibre list is exhaustive.

For the canonical factorization \(D=P1R0S\),

\[
\tau D=S1P0R,\qquad \delta(D)=|P|+1,\qquad d(D)=|S|+1.          \tag{3.4}
\]

It gives

\[
\tau A_i=A_{i+1}\ (i<q),\qquad
\tau A_q=B_{q-1},\qquad
\tau B_i=B_{i-1}\ (i\ge1),\qquad
\tau B_0=A_0,
\]

which proves (3.3). All words have height \(q+1\), and

\[
\begin{array}{c|c|c}
\text{state}&\delta&d\\ \hline
A_i,\ 0\le i<q&q+3&1\\
A_q&q+1&1\\
B_i,\ 1\le i<q&q+1&1\\
B_0&q+1&3.
\end{array}                                                       \tag{3.5}
\]

A zero-winding return after \(h\) quotient phases obeys the exact integer
ledger

\[
\sum_{j=0}^{h-1}d(\tau^jD)=\delta(\tau^hD).       \tag{3.6}
\]

For starts \(A_0,\ldots,A_{q-1}\), the \(q+1\)-term deficit block avoids
\(B_0\), has sum \(q+1\), and ends in the \(\delta=q+1\) arc. For starts
\(A_q,B_{q-1},\ldots,B_1\), it contains \(B_0\) once, has sum \(q+3\),
and ends in the \(\delta=q+3\) arc. Starting at \(B_0\), the sum is
\(q+3\) but the endpoint is \(A_q\), where \(\delta=q+1\).
Thus (3.6) holds exactly off \(B_0\).

The parent circumference is \(2q+5\), while the gap is \(2q+3\), so
there is no wrap. The height-gap theorem gives the same \(2q+3\) as a
lower bound; every return is therefore first and consecutive. Its endpoint
\(\delta\)-sum is

\[
(q+3)+(q+1)=2(q+2),
\]

so its endpoint excess is zero. \(\square\)

### Corollary 3.2

An outer return with first-mountain depth \(p<2q\) and \(y_p=1\) requires
the \(p\) consecutive level-\((p-1)\) starts
\(X,\tau X,\ldots,\tau^{p-1}X\). They exist exactly when this block avoids
the unique bad state \(B_0\). Hence exactly

\[
(2q+1)-p=b                                             \tag{3.7}
\]

rotor phases survive. These are precisely the \(b\) placements of the
unique unit outside the \(p\) terminal zero coordinates.

The quotient packing of these terminal returns on the rotor is exactly
one: every valid interval uses \(q+1\) consecutive edges of a cycle of
length \(2q+1\), and any two such intervals intersect because
\(2(q+1)>2q+1\).

In particular, every positive common endpoint boundary of the outer
return is created at a strictly higher inverse level.

## 4. Two starts: exact cyclic blocks

Let \(T<U\) be two phases on one \(\tau\)-cycle which start genuine
zero-winding returns with the same rank profile. Put \(N_j=2r_j+1\).
At level \(j\), let \(\xi_j(t)\in\mathbb Z_{N_j}\) be the fan anchor.
Exact deficit transport gives

\[
\xi_j(t+1)-\xi_j(t)
\equiv-d(\tau^tD^{(j)})\pmod {N_j}.               \tag{4.1}
\]

Indeed, the even omitted-label formula is
\(\xi_j(t)=\xi_j(0)-\sum_{v<t}d(\tau^vD^{(j)})\) modulo \(N_j\).

The level-\(j\) fan at \(T\) fixes the cyclic block

\[
\mathcal B_j(T)
=\{\xi_j(T),\xi_j(T)-1,\ldots,\xi_j(T)-j+1\}.     \tag{4.2}
\]

The labels are distinct because, for \(j\le p\),

\[
N_j-j\ge2s-3j+1\ge2s-3p+1=b\ge2.                 \tag{4.3}
\]

Put

\[
\rho_j\equiv-\sum_{t=T}^{U-1}d(\tau^tD^{(j)})
\pmod {N_j},\qquad0\le\rho_j<N_j.                \tag{4.4}
\]

### Theorem 4.1

The exact union size of the two blocks is

\[
u_j=2j-(j-\rho_j)_+-(j-(N_j-\rho_j))_+.           \tag{4.5}
\]

With \(\widehat u_j=\min(u_j,N_j-1)\), the common inverse-tower capacity
over a fixed bottom core and profile is at most

\[
\boxed{\prod_{j=1}^p
\binom{r_{j-1}+r_{j+1}-\widehat u_j}
      {2r_j-\widehat u_j}.}                       \tag{4.6}
\]

Whenever a slot occurring in both blocks is used by the two tight
gap-one fan equations, it also satisfies an exact equal-local-time
equation between those phases.

#### Proof

Two length-\(j\) cyclic intervals displaced by \(\rho_j\) have forward
overlap \((j-\rho_j)_+\) and wrap overlap
\((j-(N_j-\rho_j))_+\), proving (4.5).

At level \(j\), the free mass \(y_j\) is a weak composition into \(N_j\)
slots. If the union fixes \(u_j<N_j\) variables with total \(w\), the
number of completions is at most

\[
\binom{y_j-w+N_j-u_j-1}{N_j-u_j-1}
\le\binom{y_j+N_j-u_j-1}{N_j-u_j-1}.             \tag{4.7}
\]

If all coordinates occur, \(N_j-1\) of them and the known total determine
the last. Substituting \(N_j=2r_j+1\) and multiplying conditional bounds
proves (4.6).

For the chronology statement, the transported spacing of slot \(i\) at
ordinary time \(v\) is

\[
\Delta_i(v)=1+\varepsilon_i+2z_i+n_i(v)-n_{i-1}(v),             \tag{4.8}
\]

where \(n_i(v)\) counts selections of persistent particle \(i\) before
\(v\). In general, subtraction gives the difference of the two prescribed
spacings. For the tight fan both spacings equal one, and therefore

\[
n_i(v_2)-n_i(v_1)=n_{i-1}(v_2)-n_{i-1}(v_1).      \tag{4.9}
\]

\(\square\)

At the terminal mountain every prescribed value is literally zero. If
\(v_p=N_p-u_p\), the common bottom fibre therefore has exact size

\[
\binom{y_p+v_p-1}{v_p-1}                          \tag{4.10}
\]

for \(v_p\ge1\), and is empty for \(v_p=0\).

## 5. The first cross-level carry

### Lemma 5.1

Suppose a level-\(j\) PBBS phase returns after \(L\) quotient moves with
the same **persistent-labelled** particle order, recorded bits, and
integer relative physical gaps, not merely the same normalized unlabelled
root. Every one of its \(N_j\) particles has then been selected

\[
c=\frac{2L}{N_j}\in\mathbb Z_{\ge0}               \tag{5.1}
\]

times. In the level-\((j-1)\) physical system all equality particles are
translated by \(c\) edges; the normalized root repeats and its omitted
anchor advances by \(c\pmod {N_{j-1}}\).

#### Proof

Persistent equality particles never overtake. Return of all relative gaps
forces all particle displacements, hence all selection counts, to agree.
There are \(2L\) one-step selections, so their common count is (5.1).
The equality-particle skew system moves exactly the selected equality
particle one outer edge. Thus all outer equality particles receive the
same translation \(c\), while their order and recorded bits return.
\(\square\)

For completeness, the persistent-labelled hypothesis holds at \(M_q\).
Its recorded particle word is

\[
w=0\,1^q0^q.
\]

If the currently selected persistent label is \(\kappa_u\), one PBBS
update changes the word in the old frame to \(0^{q+1}1^q\). Its new
unmatched zero is at relative label \(q\), and rerooting there restores
\(w\). Hence

\[
\kappa_{u+1}=\kappa_u+q\pmod {N_p},\qquad N_p=2q+1.             \tag{5.2a}
\]

Because \(\gcd(q,2q+1)=1\), the \(2N_p\) one-step updates in \(N_p\)
quotient moves select every persistent particle exactly twice. Every
outer equality particle is translated twice, all relative gaps return,
and the recorded bits return as well. Lemma 5.1 therefore gives

\[
\boxed{\xi_{p-1}(T+kN_p)-\xi_{p-1}(T)
\equiv2k\pmod {N_{p-1}}.}                         \tag{5.2}
\]

Bottom residue locking is thus not an isolated reset. However, an
edge-disjoint pair needs only \(kN_p\ge s=p+q\); under \(p<2q\), the
least \(k\) is \(1\) or \(2\). The first carry may add only two or four
upper slots, so it supplies no uniform pairwise vanishing factor.

## 6. Exact phase-union packing and the residual

Fix a full critical profile with \(y_p=1\), and index the penultimate
rotor by \(X_x\), \(x\in\mathbb Z_N\), where \(N=2q+1\) and
\(\tau X_x=X_{x+1}\). Let

\[
\mathcal T_x=\{D:\partial^{p-1}D=X_x
\text{ and \(D\) has the fixed profile}\}.
\]

Commutation \(\partial\tau=\tau\partial\) makes
\(\tau:\mathcal T_x\to\mathcal T_{x+1}\) a bijection. Let
\(\mathcal R_x\subseteq\mathcal T_x\) be the genuine top starts of duration
\(s\). Corollary 3.2 gives \(\mathcal R_x=\varnothing\) outside one cyclic
interval \(I\) of \(b\) consecutive residues. Lift it as
\(I=\{0,\ldots,b-1\}\), and transport all starts to one fibre:

\[
\mathcal A_x=\tau^{-x}\mathcal R_x\subseteq\mathcal T_0.       \tag{6.1}
\]

### Theorem 6.1 (phase-union bound)

Every quotient-edge-disjoint subfamily of
\(\bigcup_{x\in I}\mathcal R_x\) has size at most

\[
2\left|\bigcup_{x\in I}\mathcal A_x\right|.        \tag{6.2}
\]

If, for some \(d\), one has

\[
\mathcal A_{x+d}=\mathcal A_x
\quad\hbox{whenever }x,x+d\in I,                  \tag{6.3}
\]

then, for \(b\ge2d\), the packing is at most

\[
\frac{4d}{b}\sum_{x\in I}|\mathcal R_x|.          \tag{6.4}
\]

#### Proof

Fix \(E\in\mathcal T_0\). The indices \(x\) for which
\(E\in\mathcal A_x\) correspond to return intervals on the single top
\(\tau\)-orbit of \(E\), starting at phases contained in a span of
\(b-1\). Each uses \(s\) consecutive quotient edges, and

\[
b=2q-p+1<2(p+q)=2s.
\]

Hence at most two can be edge-disjoint. Summing over \(E\) proves (6.2).

Under (6.3), every distinct transported set is repeated at least
\(\lfloor b/d\rfloor\) times. Therefore

\[
\left|\bigcup_x\mathcal A_x\right|
\le\frac{\sum_x|\mathcal A_x|}{\lfloor b/d\rfloor}.
\]

Since \(|\mathcal A_x|=|\mathcal R_x|\), (6.2) and
\(\lfloor b/d\rfloor\ge b/(2d)\) prove (6.4). \(\square\)

Thus every uniform transported period \(d=o(b)\) is negligible relative
to the critical start envelope. In particular, full residue locking
\(d=1\) gives a \(2/b\) phase-union factor.

The exact general consequence is weighted, not a claim about the number
of distinct set-values. Put

\[
S=\sum_{x\in I}|\mathcal A_x|,
\qquad U=\left|\bigcup_{x\in I}\mathcal A_x\right|.             \tag{6.5}
\]

If a subfamily has packing comparable to \(S\), then (6.2) forces
\(U=\Omega(S)\); equivalently its average phase multiplicity \(S/U\) is
bounded. Failure of every short exact period does not by itself imply
this: even two set-values can be arranged aperiodically. The genuine
critical obstruction is therefore weighted low overlap, not merely many
distinct phase sets.

The smallest remaining statement is therefore:

> **Upper-boundary transported-union lemma -- UNPROVED.**
> After summing over \(s\le A\sqrt r\), the profiles in (0.1), and their
> terminal rotor fibres, the actual positive-boundary transported sets
> obey
> \[
> \sum_{\text{critical fibres}}
> \left|\bigcup_{x\in I}\mathcal A_x\right|
> =o_A(4^r/r^2).                                   \tag{6.6}
> \]

This is strictly narrower than the former generic profile--boundary
coupling request. Terminal curvature, terminal fan values, terminal
chronology, and periodic residue locking are all decided. Theorem 6.1
shows that (6.6) directly implies the required packing little-oh.

## 7. Adversarial audit

1. The profile series is a capacity envelope; the rotor theorem is a
   separate exact actual-PBBS statement.

2. The \(y_p\ge2\) coefficient estimate uses its own positive subseries
   and tilt. It does not infer coefficientwise smallness from a
   \(z=1/4\) ratio.

3. The \(p=o(\sqrt r)\) and \(b=o(p)\) deletions are two-limit statements,
   not uniform pointwise assertions.

4. The rotor period is \(2q+1\), but its parent physical circumference is
   \(2q+5\). The return gap \(2q+3\) is below that circumference.

5. The terminal fan imposes \(p\), not \(p+1\), slot equations. Hence its
   exact survivor count is \(2q+1-p=b\).

6. Terminal endpoint excess zero does not imply outer endpoint excess
   zero. It localizes every positive boundary creation above the rotor.

7. Formula (4.6) is an upper bound; conflicting prescriptions only reduce
   it. Formula (4.10) is exact at the terminal mountain.

8. The \(+2k\) carry is genuine global cross-phase sharing, but a nearest
   edge-disjoint pair can pay only \(O(1)\) new slots.

9. The periodic phase-union theorem is conditional on the literal equality
   (6.3); PBBS does not presently force that periodicity. Absence of a
   short period does not imply many distinct sets. The exact surviving
   obstruction is the weighted condition \(U=\Omega(S)\).

10. No critical PBBS counterexample and no coefficient-one proof is
    claimed. The exact proved/conditional boundary is (6.6).
