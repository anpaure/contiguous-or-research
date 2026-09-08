# QST two-seam transfer kernel: the diagonal Green mode and the exact condition that removes it

Date: 2026-07-25  
Method: pure mathematics only; no computation, search, or solver

Throughout, \(B_m=\operatorname{Cat}_m=(m+1)^{-1}\binom{2m}{m}\).

## 0. Outcome

Put

\[
 F_0(z)=F_1(z)=1,
 \qquad F_{j+1}(z)=F_j(z)-zF_{j-1}(z),
\]

and, in step variable \(x\),

\[
 A_j(x)={x^j\over F_j(x^2)},
 \qquad
 G_j(x)={x^j\over F_{j+1}(x^2)}.
\]

The one-intermediate-phase chart for zero-winding returns of height and
duration \(s\) is

\[
 H_{s,t}(x)=A_t(x)A_{s-t}(x)G_s(x).
 \tag{0.1}
\]

This note proves the following exact statements and isolates one
conditional gate.

1. Adding only the next canonical suffix cap gives another three-strip
   kernel, not a four-strip kernel:

   \[
   H^+_{s,t}(x)
   =A_tA_{s-t}A_sC_t
   =A_{s-t}A_sG_t,
   \tag{0.2}
   \]

   where \(C_t=F_t/F_{t+1}\).  If \(t/s\) stays in a fixed compact
   subinterval of \((0,1)\), then on every fixed Gaussian height band,
   both \(H^+_{s,t}\) and \(H_{s,t}\) have coefficient order
   \(4^m s^{-5}\).  Thus an adjacent second chart supplies no vanishing
   factor.

2. The genuinely separated, one-crossing terminal seam has kernel

   \[
   K^\times_{s,t,u}(x)
   =A_tA_{s-t}G_{s-u}\,x\,G_{u-1}
   ={x^{2s}\over
      F_tF_{s-t}F_{s-u+1}F_u},
   \tag{0.3}
   \]

   with every \(F\) evaluated at \(x^2\).  If \(t,u,s-t,s-u\) are all
   proportional to \(s\), then

   \[
   [x^{2m}]K^\times_{s,t,u}(x)
   =\Theta(4^m s^{-6})
   \tag{0.4}
   \]

   uniformly for \(s\) in a fixed Gaussian band.  Summing such a chart
   over the band gives \(O(B_m/m)=o(B_m/\sqrt m)\).

3. The full corridor differs from the one-crossing corridor by the exact
   seam-renewal factor

   \[
   \mathcal R_{s,u}(x)
   ={F_{s-u+1}(x^2)F_u(x^2)\over F_{s+1}(x^2)}
   ={1\over1-\rho_{s,u}(x)},
   \tag{0.5}
   \]

   where

   \[
   \rho_{s,u}(x)
   =x^2{F_{s-u}(x^2)\over F_{s-u+1}(x^2)}
        {F_{u-1}(x^2)\over F_u(x^2)}.
   \tag{0.6}
   \]

   The coefficients of \(\rho_{s,u}\) and \(\mathcal R_{s,u}\) are
   nonnegative.  At the Catalan critical point,

   \[
   \mathcal R_{s,u}(1/2)
   ={(s-u+2)(u+1)\over s+2}.
   \tag{0.7}
   \]

   Hence a central seam carries mass \(\Theta(s)\).  This is exactly the
   factor which changes \(s^{-6}\) back to the critical \(s^{-5}\).

4. If, for deterministic central seams, the actual PBBS subset is
   coefficientwise dominated by

   \[
   K^\times_{s,t_s,u_s}(x)\Psi_{s,u_s}(x),
   \qquad \Psi_{s,u_s}(1/2)=o(s)
   \]

   uniformly on a fixed Gaussian band, then it has vanishing density in
   the one-phase chart and satisfies the zero-winding contribution to the
   fixed-band form of \(QST_A\).
   In particular, allowing at most \(L_m=o(\sqrt m)\) extra seam-crossing
   pairs is sufficient.

5. A pointwise sublinear bound on the recrossing count is false.  There
   are genuine zero-winding roots of Gaussian height with \(\Theta(m)\)
   central recrossing pairs.  Nevertheless, the exact renewal layers decay as
   \(\exp(-\Theta(k/s))\), so both \(k=o(s)\) and \(k/s\to\infty\) are
   aggregately negligible.  Only the window \(k=\Theta(s)\) can remain
   critical.

6. The tempting one-block carrier localization is false even for a
   genuine first zero-winding return: Proposition 4.2 gives an exact
   \((m,s,\Lambda)=(8,4,4)\) orbit whose mandatory copied word crosses a
   dual-block separator.  The synchronized transfer must retain at least
   the unmatched height and the current block index.  Bounding this
   two-dimensional carrier automaton by critical mass \(o(s)\) is the
   exact remaining gate.

The pointwise sublinear-recrossing shortcut is false: Proposition 2.1
constructs genuine Gaussian-height roots with arbitrarily large central
recrossing count.  The missing PBBS theorem is instead an
**aggregate** assertion that the high-renewal strata have vanishing
Catalan density or cannot form a critical edge-disjoint packing.  It is not
implied by writing the free-monoid seam identity at two phases: those
identities are algebraically equivalent under the exact
\(\tau\)-transition equations.  No genuine Catalan-density PBBS saturator
is constructed here, so this note does not refute \(QST_A\).

## 1. Finite-path normalizations

The bounded-height Dyck generating function is

\[
 C_j(z)={F_j(z)\over F_{j+1}(z)}.
 \tag{1.1}
\]

At \(z=1/4\),

\[
 F_j(1/4)={j+1\over2^j},
 \tag{1.2}
\]

and therefore

\[
 A_j(1/2)={1\over j+1},
 \qquad
 G_j(1/2)={2\over j+2},
 \qquad
 C_j(1/4)={2(j+1)\over j+2}.
 \tag{1.3}
\]

For later use, normalize coefficients by

\[
 a_j(n)=2^{-n}[x^n]A_j(x),
 \qquad
 g_j(n)=2^{-n}[x^n]G_j(x).
\]

The path-graph spectral expansion, paired at short times by the two-wall
reflection identity, gives absolute constants \(c,C>0\) such that

\[
 \|a_j\|_1={1\over j+1},
 \qquad
 \|g_j\|_1={2\over j+2},
 \tag{1.4}
\]

and

\[
 a_j(n)\le {C\over(j+1)^3}
       \exp\!\left(-{cn\over(j+1)^2}\right),
 \qquad
 g_j(n)\le {C\over(j+2)^3}
       \exp\!\left(-{cn\over(j+2)^2}\right).
 \tag{1.5}
\]

The bounds in (1.5) remain valid at times below the square of the strip
width because the reflection formula gives

\[
 C(n+1)^{-3/2}
 \exp\!\left(-c{(j+1)^2\over n+1}\right)
 \le C'(j+1)^{-3}.
\]

For fixed \(0<a<b<\infty\) and \(\epsilon>0\), the corresponding local
lower estimates imply the following.  Uniformly when

\[
 a\sqrt m\le s\le b\sqrt m,
 \qquad
 \epsilon s\le j\le(1-\epsilon)s,
\]

every convolution of three endpoint kernels of widths proportional to
\(s\) has coefficient \(\Theta_{a,b,\epsilon}(4^m s^{-5})\), and every
convolution of four such kernels has coefficient
\(\Theta_{a,b,\epsilon}(4^m s^{-6})\).  For the upper bounds, one factor
carries at least one third, respectively one fourth, of the elapsed time;
apply (1.5) to it and (1.4) to the others.  For the lower bounds, restrict
all elapsed times to fixed positive multiples of \(s^2\), use the positive
finite-path heat-kernel lower bound there, and count the
\(\Theta(s^4)\), respectively \(\Theta(s^6)\), parity-compatible time
splittings.  All constants are uniform on the displayed compact parameter
set.

## 2. Why the adjacent second seam is critical, not vanishing

Fix a genuine zero-winding return of duration \(s\), and view its phase
\(t\) root.  The intermediate chart gives the two first-passage prefix
kernels \(A_tA_{s-t}\).  Write the terminal corridor after the first
height-\(s\) attainment as the first passage from height \(s\) to zero,
followed by the terminal Dyck suffix \(S_t\).  The first-passage part has
generating function \(A_s\): this is the endpoint entry of the resolvent
on states \(1,\ldots,s\), followed by the last step from \(1\) to zero.

The exact zero-winding staircase gives

\[
 \operatorname{ht}(S_t)\le t.
 \tag{2.1}
\]

Consequently every actual phase-\(t\) root lies in the language with
generating function

\[
 \begin{aligned}
 H^+_{s,t}(x)
 &=A_t(x)A_{s-t}(x)A_s(x)C_t(x^2)\\
 &=A_{s-t}(x)A_s(x)G_t(x)\\
 &={x^{2s}\over
 F_{s-t}(x^2)F_s(x^2)F_{t+1}(x^2)}.
 \end{aligned}
 \tag{2.2}
\]

The cancellation in the second line is exact:

\[
 A_t(x)C_t(x^2)
 ={x^t\over F_t(x^2)}{F_t(x^2)\over F_{t+1}(x^2)}
 =G_t(x).
\]

At the critical point,

\[
 H^+_{s,t}(1/2)
 ={2\over(s-t+1)(s+1)(t+2)},
 \tag{2.3}
\]

whereas

\[
 H_{s,t}(1/2)
 ={2\over(t+1)(s-t+1)(s+2)}.
 \tag{2.4}
\]

Their critical-mass ratio is

\[
 {H^+_{s,t}(1/2)\over H_{s,t}(1/2)}
 ={(t+1)(s+2)\over(t+2)(s+1)}.
 \tag{2.5}
\]

In particular, for \(t/s\) in a compact subinterval of \((0,1)\), this
ratio tends to one.  More importantly, (2.2) is still a convolution of
exactly three proportional-width endpoint kernels.  Hence, on every fixed
Gaussian band,

\[
 [x^{2m}]H^+_{s,t}
 =\Theta(4^m s^{-5}),
 \qquad
 [x^{2m}]H_{s,t}
 =\Theta(4^m s^{-5}).
 \tag{2.6}
\]

Thus the next suffix cap does not give an \(o(1)\) factor.

There is also an exact algebraic reason not to multiply phase charts.
Suppose the phase data obey

\[
 Q_{j+1}=S_j1Q_j,
 \qquad
 V_j=V_{j+1}1\overline T_j,
 \tag{2.7}
\]

and the literal local transition identity

\[
 S_j1P_j=P_{j+1}1\overline T_j.
 \tag{2.8}
\]

Then

\[
 \boxed{
 P_j=Q_jV_j
 \quad\Longleftrightarrow\quad
 P_{j+1}=Q_{j+1}V_{j+1}.}
 \tag{2.9}
\]

Indeed, substitute either factorization into (2.8), use (2.7), and cancel
the common left word \(S_j1\) or the common right word
\(1\overline T_j\) in the free monoid.  Iteration proves that the seam
factorizations at any two phases are algebraically equivalent once all
intervening local transition identities are retained.  A second phase can
contribute only a new geometric/canonical restriction; its displayed word
equality itself contributes no entropy.

There is one nonredundant transported tail equation.  Iterating the exact
dual-tail identity

\[
 \overline T_j0R_j=R_{j+1}0S_{j+1}
\]

from \(j=t\) through \(j=u-1\) gives

\[
 \boxed{
 \mathcal A_{t,u}R_t=R_u\mathcal C_{t,u},}
 \tag{2.10}
\]

where

\[
 \mathcal A_{t,u}
 = (\overline T_{u-1}0)\cdots(\overline T_t0),
 \qquad
 \mathcal C_{t,u}
 = (0S_u)\cdots(0S_{t+1}).
 \tag{2.11}
\]

Equation (2.10) is the exact two-phase carrier equation.  Unlike (2.9),
it couples the terminal words at the two phases.  However, it is an overlap
equation, not a one-crossing assertion: its formal solution language has
overlap/renewal sectors, and no implication bounding their excursion count
follows from free-monoid cancellation.  A synchronized product automaton
can retain (2.10), but reducing that automaton to the one-dimensional
finite-path kernels requires precisely a bound on the unmatched overlap
carrier.  Such a PBBS bound is not presently proved.

The overlap sector is genuinely nonempty for every duration, not merely a
formal artifact.

For the rest of the report, write

\[
 \Lambda=\delta(D_0)+\delta(D_s)-2m
 \tag{2.12a}
\]

for the endpoint-overlap excess of an actual duration-\(s\) zero return.

### Proposition 2.1 (genuine arbitrarily long central recrossers)

For every \(s\ge3\) and \(k\ge1\), put

\[
 X=(1100)^k,\qquad \overline X=(0011)^k,\qquad
 m=s+2k,\qquad N=2m+1,
 \tag{2.12}
\]

and define

\[
 D_0=1^{s-1}\overline X\,1\,0^s.
 \tag{2.13}
\]

Then \(D_0\) starts a consecutive zero-winding PBBS return of duration
\(s\), hence odd gap \(2s+1<N\).  Its exact \(\tau\)-orbit through the
endpoint is

\[
 D_h=1^s0^{h-1}\overline X\,0^{s-h+1}
 \quad(1\le h\le s-2),
 \tag{2.14}
\]

\[
 D_{s-1}=1^s0^sX,
 \qquad
 D_s=X1^s0^s.
 \tag{2.15}
\]

At phase \(t=\lfloor s/2\rfloor\), put

\[
 u=s-t.
\]

The terminal corridor crosses the central edge
\(\{u-1,u\}\) exactly \(2k+1\) times, and hence has \(k\) extra crossing
pairs.  Its endpoint-overlap parameter is

\[
 \boxed{\Lambda=4k.}
 \tag{2.16}
\]

#### Proof

The word \(D_0\) is Dyck: \(\overline X\) consists of \(k\) excursions
which descend two levels and return, based at height \(s-1\), and the next
up-step first reaches height \(s\).  Its block rotation gives \(D_1\).
For \(1\le h\le s-2\), the first maximum of \(D_h\) is the last step of
its initial block \(1^s\), and its first later return to zero is the final
step.  The literal block rotation therefore sends (2.14) at index \(h\)
to (2.14) at index \(h+1\).  At the last such transition use the word
identity

\[
 \overline X\,00=00X
 \tag{2.17}
\]

to obtain \(D_{s-1}=1^s0^sX\).  Its first descent \(0^s\) returns to zero
and leaves terminal suffix \(X\), so one more block rotation gives
\(D_s=X1^s0^s\).

For \(D_0,D_1,\ldots,D_{s-2}\), the terminal Dyck suffix is empty, so the
deficit is one.  For \(D_{s-1}\), the terminal suffix is \(X\), so the
deficit is \(4k+1\).  Hence

\[
 \sum_{h=0}^{s-1}d(D_h)=(s-1)+(4k+1)=s+4k.
 \tag{2.18}
\]

The first maximum of \(D_s\) occurs in the terminal mountain, at position
\(4k+s\).  This is (2.18), proving zero winding.  For
\(1\le h<s\), the first-maximum position of \(D_h\) is \(s\), while the
accumulated deficit is \(h\).  All proper first-passage differences are
positive, so the return is consecutive.

At phase \(t\), the corridor after the first maximum is

\[
 0^{t-1}(0011)^k0^{s-t+1}.
 \tag{2.19}
\]

After its initial descent it is at height \(u+1\).  Every \(0011\) block
crosses \(\{u-1,u\}\) once downward and once upward, while the final
descent crosses it once downward.  This gives exactly \(2k+1\) crossings.
Finally,

\[
 \delta(D_0)=\delta(D_s)=s+4k,
 \qquad 2m=2s+4k,
\]

which proves (2.16).  \(\square\)

Taking \(s\asymp\sqrt m\) makes \(k=(m-s)/2=\Theta(m)\), so no pointwise
sublinear-recrossing theorem can hold even in the Gaussian height regime.
There is still only one displayed root for each pair \((s,k)\); this is
not a Catalan-density or edge-disjoint-packing saturator.  The example
therefore forces an aggregate density theorem rather than a universal
one-crossing or bounded-renewal theorem.

## 3. The exact one-crossing transfer matrix

Fix \(1\le u\le s-1\).  In the terminal corridor, mark the horizontal
edge between heights \(u\) and \(u-1\).  Require the corridor to cross
this edge exactly once, downward.  Before that crossing it stays in
\([u,s]\), and after that crossing it stays in \([0,u-1]\).  The unique
decomposition at the crossing gives

\[
 \begin{aligned}
 K^\times_{s,t,u}(x)
 &=A_tA_{s-t}G_{s-u}\,x\,G_{u-1}\\
 &={x^{2s}\over
 F_t(x^2)F_{s-t}(x^2)
 F_{s-u+1}(x^2)F_u(x^2)}.
 \end{aligned}
 \tag{3.1}
\]

The exact critical ratio to the unrestricted chart is

\[
 \boxed{
 {K^\times_{s,t,u}(1/2)\over H_{s,t}(1/2)}
 ={s+2\over(s-u+2)(u+1)}.}
 \tag{3.2}
\]

Thus a seam separated by distances proportional to \(s\) from both walls
gives the desired \(\Theta(1/s)\) factor.

More generally, put

\[
 q=\min(u+1,s-u+2).
\]

Fix \(0<a<b<\infty\) and \(\epsilon>0\).  Uniformly for

\[
 a\sqrt m\le s\le b\sqrt m,
 \qquad
 \epsilon s\le t\le(1-\epsilon)s,
\]

the estimates (1.4)--(1.5) give

\[
 [x^{2m}]K^\times_{s,t,u}(x)
 \le C_{a,b,\epsilon}{4^m\over s^5q}.
 \tag{3.3}
\]

To prove (3.3), three of the four strip widths are \(\Theta(s)\), while
the fourth has width \(\Theta(q)\).  If one of the wide strips carries at
least a quarter of the elapsed time, use its \(O(s^{-3})\) pointwise bound,
the two other wide \(O(s^{-1})\) masses, and the \(O(q^{-1})\) narrow
mass.  If the narrow strip carries that much time, its contribution is

\[
 O(q^{-3}s^{-3})\exp(-cm/q^2).
\]

Since \(m/s^2\) lies in a fixed compact subinterval of \((0,\infty)\),

\[
 (s/q)^2\exp(-cm/q^2+c'm/s^2)=O_{a,b}(1),
\]

which gives the same right side after reducing \(c'\) if necessary.

If also

\[
 \epsilon s\le u\le(1-\epsilon)s,
\]

then the finite-path lower bound and (3.3) give

\[
 \boxed{
 [x^{2m}]K^\times_{s,t,u}(x)
 =\Theta_{a,b,\epsilon}(4^m s^{-6}).}
 \tag{3.4}
\]

## 4. The seam-renewal factor and its diagonal Green mode

The unrestricted corridor is the one-crossing corridor followed by an
arbitrary sequence of extra crossing pairs.  Let

\[
 \rho_{s,u}(x)
 =x^2
 {F_{s-u}(x^2)\over F_{s-u+1}(x^2)}
 {F_{u-1}(x^2)\over F_u(x^2)}.
 \tag{4.1}
\]

The first fraction is the diagonal resolvent at the lower endpoint of the
upper path \([u,s]\); the second is the diagonal resolvent at the upper
endpoint of the lower path \([0,u-1]\).  Thus \(\rho_{s,u}\) counts one
lower boundary loop, one upcrossing, one upper boundary loop, and one
downcrossing.  It has nonnegative coefficients, and renewal gives

\[
 \mathcal R_{s,u}(x)
 =\sum_{j\ge0}\rho_{s,u}(x)^j.
 \tag{4.2}
\]

The continuant identity

\[
 F_{a+b}=F_aF_b-zF_{a-1}F_{b-1}
 \tag{4.3}
\]

with \(a=s-u+1\), \(b=u\), proves

\[
 \boxed{
 \mathcal R_{s,u}(x)
 ={F_{s-u+1}(x^2)F_u(x^2)\over F_{s+1}(x^2)}.}
 \tag{4.4}
\]

Consequently

\[
 \boxed{H_{s,t}(x)=K^\times_{s,t,u}(x)\mathcal R_{s,u}(x).}
 \tag{4.5}
\]

At \(x=1/2\),

\[
 \rho_{s,u}(1/2)
 ={u(s-u+1)\over(u+1)(s-u+2)},
 \tag{4.6}
\]

and hence

\[
 1-\rho_{s,u}(1/2)
 ={s+2\over(u+1)(s-u+2)},
 \qquad
 \mathcal R_{s,u}(1/2)
 ={(u+1)(s-u+2)\over s+2}.
 \tag{4.7}
\]

For a central seam, \(\rho(1/2)=1-\Theta(1/s)\), so the unrestricted
renewal sequence has critical mass \(\Theta(s)\).  Marking a seam but
retaining its arbitrary recrossings therefore loses the entire putative
\(1/s\) gain.

At the midpoint \(s=2q,u=q\), the same mode is, up to a bounded endpoint
factor, the diagonal path resolvent

\[
 \mathcal D_q(z)={F_{q+1}(z)^2\over F_{2q+1}(z)}.
 \tag{4.8}
\]

It has nonnegative coefficients and

\[
 \boxed{
 \mathcal D_q(1/4)
 ={(q+2)^2\over4(q+1)}\sim {q\over4}.}
 \tag{4.9}
\]

The continuant identity also gives the exact decomposition

\[
 \mathcal D_q(z)
 =1+{z^2F_{q-1}(z)^2\over F_{2q+1}(z)}.
 \tag{4.9a}
\]

Thus the constant term is the algebraic zero-loop term and the second term
is a positive path-Green sector; the latter carries asymptotically all of
the critical mass.

For coefficientwise positivity, assume first that \(q\ge2\), and let
\(M=I-xA(P_{2q})\), where the path vertices are
\(1,\ldots,2q\).  Cramer's rule for the entry three places off the
diagonal gives

\[
 (M^{-1})_{q-1,q+2}
 ={x^3F_{q-1}(x^2)^2\over F_{2q+1}(x^2)}.
 \tag{4.9b}
\]

Since \(M^{-1}=\sum_{n\ge0}x^nA(P_{2q})^n\), this entry has nonnegative
coefficients.  Equation (4.9a) is

\[
 \mathcal D_q(x^2)=1+x(M^{-1})_{q-1,q+2},
\]

which proves the claimed positivity.  At \(x=1/2\), the Green entry in
(4.9b) is exactly \(q^2/(2(q+1))\), so the added term is
\(q^2/(4(q+1))\), as required by (4.9).  For \(q=1\), positivity follows
directly from

\[
 \mathcal D_1(z)=1+{z^2\over1-2z}.
\]

Indeed,

\[
 \mathcal D_q
 ={F_{q+1}\over F_q}\mathcal R_{2q,q},
\]

and \(F_{q+1}(1/4)/F_q(1/4)\to1/2\).

This diagonal mode already occurs in the audited exact
\(\Lambda=0\) calculation.  In semilength variable \(z\), the central
one-seam ambient kernel and the genuine \(\Lambda=0\) kernel are

\[
 J_{2q,q}(z)
 ={z^{2q}\over F_q(z)^2F_{2q+1}(z)},
 \qquad
 E_{2q}(z)
 ={z^{2q}\over F_q(z)^2F_{q+1}(z)^2}.
 \tag{4.10}
\]

Therefore

\[
 {J_{2q,q}(z)\over E_{2q}(z)}=\mathcal D_q(z).
 \tag{4.11}
\]

The genuine \(\Lambda=0\) compatibility removes the diagonal Green mode
and gains the exact critical factor \(\Theta(1/q)\).  The remaining
\(\Lambda>0\) problem is exactly whether actual chronology or
edge-disjointness suppresses this mode aggregately.

### 4.1 A soft second seam retains the same spectral scale

There is a direct transfer-matrix audit which rules out a gain from merely
marking a second separated seam while allowing arbitrary returns to both
seams.  Let \(P_L\) be simple random walk on
\(\{1,\ldots,L-1\}\), killed on hitting \(0\) or \(L\).  Its critical
Green matrix is

\[
 \Gamma_L(i,j)
 :=\sum_{n\ge0}P_L^n(i,j)
 ={2\min(i,j)(L-\max(i,j))\over L}.
 \tag{4.12}
\]

For \(1\le i<j\le L-1\),

\[
 \det
 \begin{pmatrix}
  \Gamma_L(i,i)&\Gamma_L(i,j)\\
  \Gamma_L(j,i)&\Gamma_L(j,j)
 \end{pmatrix}
 ={4i(j-i)(L-j)\over L}.
 \tag{4.13}
\]

Consequently, if

\[
 \epsilon L\le i<j\le(1-\epsilon)L,
 \qquad j-i\ge\epsilon L,
\]

then both eigenvalues of this two-seam Green matrix lie between
\(c_\epsilon L\) and \(C_\epsilon L\).  In particular, the cross Green
entry, both diagonal entries, and both spectral modes retain order \(L\).
No \(o(1)\) factor follows from these two soft central seam projectors.

Equation (4.12) follows by solving the discrete harmonic equation away
from \(j\), with zero boundary values and the unit Green jump at \(j\).
Equation (4.13) is direct substitution.  The trace is \(\Theta_\epsilon(L)\)
and the determinant is \(\Theta_\epsilon(L^2)\), proving the eigenvalue
claim.

Thus the relevant distinction is not one seam versus two seams.  It is
an unrestricted Green seam versus an absorbing, truncated, or
chronologically cancelled seam.  A successful PBBS two-seam theorem must
remove the renewal mode, not just record a second visit to it.

### 4.2 Separator-spanning carriers defeat the one-block localization

The endpoint words

\[
 \mathcal A=(\overline T_{s-1}0)\cdots(\overline T_00),
 \qquad
 \mathcal C=(0S_s)(0S_{s-1})\cdots(0S_1)
 \tag{4.14}
\]

satisfy

\[
 \mathcal A=R_sO,\qquad \mathcal C=OR_0.
 \tag{4.15}
\]

It is tempting to assert that the mandatory prefix \(0S_s0\) of a
positive-overlap word \(O\) lies inside one complemented dual block.  That
assertion is false: the copied word may cross one or more separators
between dual blocks.

### Proposition 4.2 (genuine separator-spanning counterexample)

There is a genuine first zero-winding return with

\[
 s=4,\qquad m=8,\qquad\Lambda=4,
\]

whose carrier data are

\[
 T_0=T_1=S_3=S_4=1100
\]

and all other \(T_j,S_j\), including \(S_0\), empty.  Explicitly,

\[
 \mathcal A=000011000110,\qquad
 \mathcal C=011000110000,
\]

\[
 R_s=R_0=000,\qquad O=011000110.
 \tag{4.16}
\]

The mandatory prefix

\[
 0S_40=011000
\]

is the suffix \(011\) of \(\overline T_1=0011\), followed by its separator
zero and then the first two zeros of \(\overline T_0=0011\).  Thus it
spans two dual blocks.  In particular, neither \(T_0\) nor \(T_1\), both
of length four, can contain a factor
\(1\overline S_41\), which has length six.

The exact quotient roots are

\[
\begin{aligned}
 D_0&=1100111001110000,\\
 D_1&=1110011100110000,\\
 D_2&=1111001100011000,\\
 D_3&=1111000110001100,\\
 D_4&=1100111100001100.
\end{aligned}
 \tag{4.17}
\]

Direct canonical block rotation gives \(\tau D_j=D_{j+1}\).  Their
first-maximum positions are

\[
 (12,8,4,4,8),
\]

and their first four deficits are

\[
 (1,1,1,5).
\]

The proper accumulated deficits are \(1,2,3\), strictly below the
corresponding terminal first-maximum positions, while the final sum is
\(8=\delta(D_4)\).  Hence this is a consecutive zero-winding return.
Also

\[
 \Lambda=\delta(D_0)+\delta(D_4)-2m=12+8-16=4.
 \qquad\square
\]

Therefore the proposed one-block two-first-hit localization, its
\(O(\log s)\) critical-mass sum, and the associated raw
outer-carrier product are invalid.  The exact synchronized transfer state
must retain both the unmatched height and the current \(S/T\)-block index.
This is a genuinely two-dimensional automaton, and an independent
lower/upper Green factor can re-enter whenever the copied carrier crosses
a separator.  In particular, replacing
\(\rho=x^2C_{s-u}C_{u-1}\) by the tempting synchronized factor
\(x^2C_{\min(s-u,u-1)}\) is unsupported.

A coefficientwise domination

\[
 \mathcal Z_s^+(x)
 \preceq K^\times_{s,t_s,u_s}(x)\Psi_s(x),
 \qquad \Psi_s(1/2)=o(s),
 \tag{OCR_s}
\]

for deterministic central seams \(t_s,u_s\), would still suffice by
Corollary 5.2 below.  No such bound is proved here.

## 5. A sufficient sublinear-renewal theorem

For \(L\ge0\), truncate the recrossing sequence at \(L\) extra crossing
pairs:

\[
 \mathcal R^{(L)}_{s,u}(x)
 =\sum_{j=0}^{L}\rho_{s,u}(x)^j.
 \tag{5.1}
\]

Because all coefficients are nonnegative,

\[
 \mathcal R^{(L)}_{s,u}(1/2)\le L+1.
 \tag{5.2}
\]

Assume \(t\) and \(u\) are both separated by at least \(\epsilon s\) from
their two walls.  From (1.4)--(1.5), the normalized coefficient sequence
of \(K^\times_{s,t,u}\) satisfies the uniform bound

\[
 \sup_n 2^{-n}[x^n]K^\times_{s,t,u}(x)
 \le C_\epsilon s^{-6}.
 \tag{5.3}
\]

### Lemma 5.1 (exact renewal-layer decay)

For every integer \(k\ge0\), put

\[
 K^{(k)}_{s,t,u}(x)
 =K^\times_{s,t,u}(x)\rho_{s,u}(x)^k.
 \tag{5.3a}
\]

This is exactly the generating function for chart words whose terminal
corridor has \(k\) extra crossing pairs at the marked seam.  There are
constants \(c_\epsilon,C_\epsilon>0\) such that, for every \(m,s,k\),

\[
 \boxed{
 [x^{2m}]K^{(k)}_{s,t,u}(x)
 \le C_\epsilon4^m s^{-6}
       \exp\!\left(-c_\epsilon{k\over s}\right).}
 \tag{5.3b}
\]

Moreover, for every integer \(L\ge0\),

\[
 \boxed{
 [x^{2m}]
 K^\times_{s,t,u}(x)\sum_{k\ge L}\rho_{s,u}(x)^k
 \le C_\epsilon4^m s^{-5}
       \exp\!\left(-c_\epsilon{L\over s}\right).}
 \tag{5.3c}
\]

#### Proof

At the critical point, (4.7) and the centrality of \(u\) give

\[
 {c_\epsilon\over s}
 \le1-\rho_{s,u}(1/2)
 \le {C_\epsilon\over s}.
 \tag{5.3d}
\]

The normalized \(\ell^1\)-mass of \(\rho^k\) is
\(\rho(1/2)^k\), which is at most
\(\exp(-c_\epsilon k/s)\).  Convolve this with (5.3) to prove
(5.3b).  Summing the geometric tail and using
\((1-\rho(1/2))^{-1}\le C_\epsilon s\) proves (5.3c).  \(\square\)

Convolving (5.3) with (5.2) gives the exact packet-mass estimate

\[
 \boxed{
 [x^{2m}]
 K^\times_{s,t,u}(x)\mathcal R^{(L)}_{s,u}(x)
 \le C_\epsilon(L+1)4^m s^{-6}.}
 \tag{5.4}
\]

More generally, (5.4) holds with \(L+1\) replaced by
\(\Psi_{s,u}(1/2)\) for every nonnegative seam-transfer series
\(\Psi_{s,u}\) which coefficientwise bounds the actual allowed renewal
words.

### Corollary 5.1 (only the linear recrossing window can be critical)

Fix \(0<a<A<\infty\) and deterministic seams \(t_s,u_s\) satisfying

\[
 \epsilon s\le t_s,u_s\le(1-\epsilon)s.
\]

For \(0<\eta<1<M\), the total number of words in the formal charts with

\[
 a\sqrt m\le s\le A\sqrt m
\]

and recrossing count either at most \(\eta s\) or at least \(Ms\) is at
most

\[
 \boxed{
 C_{a,A,\epsilon}
 \left(\eta+{1\over\sqrt m}+e^{-c_\epsilon M}\right)
 {B_m\over\sqrt m}.}
 \tag{5.4a}
\]

The same bound therefore holds for every actual-start subset and every
quotient-edge-disjoint packing.

#### Proof

For the low-renewal part, use (5.4) with
\(L=\lfloor\eta s\rfloor\).  For the high-renewal part, use (5.3c) with
\(L=\lceil Ms\rceil\).  Each fixed \(s\) contributes at most

\[
 C4^m s^{-5}
 \left(\eta+s^{-1}+e^{-c_\epsilon M}\right).
\]

There are \(O_{a,A}(\sqrt m)\) heights and
\(s\asymp_{a,A}\sqrt m\); summing and using
\(B_m\asymp4^m m^{-3/2}\) proves (5.4a).  A packing is a subset of the
start set.  \(\square\)

Thus, after first taking \(m\to\infty\), then
\(\eta\downarrow0\) and \(M\uparrow\infty\), every possible critical
near-saturator is forced into the linear renewal window

\[
 \eta s<k<Ms.
 \tag{5.4b}
\]

In particular, the long-recrossing family in Proposition 2.1, for which
\(k/s\to\infty\) in the Gaussian choice \(s\asymp\sqrt m\), lies in a
formally negligible high-renewal tail despite disproving every pointwise
recrossing bound.

### Corollary 5.2 (fixed-band zero-winding QST contribution from sublinear seam mass)

Fix \(0<a<A<\infty\) and \(\epsilon>0\).  For each \(s\), choose
deterministic seams \(t_s,u_s\) with

\[
 \epsilon s\le t_s,u_s\le(1-\epsilon)s.
\]

Suppose every actual zero-winding start under consideration, transported
to phase \(t_s\), belongs to a seam-transfer language bounded by

\[
 K^\times_{s,t_s,u_s}(x)\Psi_{s,u_s}(x),
\]

where the coefficients of \(\Psi\) are nonnegative and

\[
 \eta_m:=\sup_{a\sqrt m\le s\le A\sqrt m}
 {\Psi_{s,u_s}(1/2)\over s}\longrightarrow0.
 \tag{5.5}
\]

Then the number of these starts in the fixed Gaussian band is

\[
 o_{a,A}(B_m/\sqrt m).
 \tag{5.6}
\]

The same bound holds for every quotient-edge-disjoint packing of their
return intervals.

#### Proof

By (5.3), for each \(s\) the number of starts is at most

\[
 C\Psi_{s,u_s}(1/2)4^m s^{-6}
 \le C\eta_m4^m s^{-5}.
\]

There are \(O_{a,A}(\sqrt m)\) heights in the band, and
\(s\asymp_{a,A}\sqrt m\).  Hence the total is

\[
 O_{a,A}(\eta_m4^m m^{-2})
 =O_{a,A}(\eta_m B_m/\sqrt m)
 =o_{a,A}(B_m/\sqrt m).
\]

A packing is a subset of the start set, so the same estimate includes
edge-disjoint packing without an independence multiplication.  \(\square\)

In particular, if every relevant central corridor has at most
\(L_m=o(\sqrt m)\) extra crossing pairs, take
\(\Psi=\mathcal R^{(L_m)}\).  Equation (5.2) verifies (5.5).

## 6. Exact proved and conditional boundary

Proved:

1. The next suffix cap produces (2.2), another critical three-strip
   kernel.  It does not provide an \(o(1)\) factor.
2. The phase seam equations \(P_j=Q_jV_j\) are algebraically redundant
   across \(\tau\)-transitions in the precise sense of (2.9).
3. A literal one-crossing central seam has the four-kernel transfer
   (3.1), coefficient order \(4^m s^{-6}\), and Gaussian-band total
   \(O(B_m/m)\).
4. Arbitrary seam recrossings restore the exact renewal/diagonal Green
   factor (4.4), whose central critical mass is \(\Theta(s)\).
5. The genuine audited \(\Lambda=0\) kernel removes this diagonal mode
   exactly, as shown by (4.10)--(4.11).
6. Two soft separated seam projectors retain Green
   eigenvalues of order \(s\); merely marking a second seam cannot supply
   a vanishing factor.
7. Proposition 2.1 gives genuine Gaussian-height roots with
   \(\Theta(m)\) central recrossing pairs.  Hence no pointwise
   sublinear-renewal theorem is possible.
8. The exact renewal-layer estimate forces every possible critical
   near-saturator into the window \(k=\Theta(s)\), in the iterated
   \(\eta\downarrow0\), \(M\uparrow\infty\) sense of Corollary 5.1.
9. Proposition 4.2 is a genuine separator-spanning carrier.  It disproves
   the one-block localization and shows that the exact synchronized state
   must retain both unmatched height and block index; the proposed
   one-dimensional carrier product is invalid.
10. Sublinear central renewal mass on a specified subclass implies the fixed-band quotient packing
   bound by Corollary 5.2, with packing included directly as a subset of
   starts.

Unproved:

1. The pointwise assertion that all genuine zero-winding PBBS returns have
   \(o(s)\) central recrossing pairs is false by Proposition 2.1.  What
   remains unproved is an aggregate Catalan-density or
   edge-disjoint-packing suppression of the linear-renewal
   positive-overlap/\(\Lambda>0\) sector.
2. Merely imposing a second phase chart does not establish the needed
   one-crossing or sublinear-renewal condition.  A PBBS-specific
   compatibility theorem across the transported terminal corridor is
   still required.
3. The coefficientwise two-dimensional carrier bound \((OCR_s)\) is
   unproved.  Its hypothesis must control separator-spanning copied words,
   and must give a nonnegative synchronized transfer series of critical
   mass \(o(s)\) for deterministic central \(t_s,u_s\).  Proposition 4.2
   rules out the proposed reduction to one bounded-height excursion.
4. No genuine PBBS family saturating the full diagonal Green mode in an
   edge-disjoint Gaussian packing is constructed.  Therefore the result
   is a sharp reduction and a solved transfer-matrix calculation, not a
   counterexample to \(QST_A\).

## 7. Independent audit of the decisive steps

The two places where a spurious factor of \(s\) can enter were checked
independently.

1. **Renewal indices.**  With \(a=s-u+1\), \(b=u\), the continuant
   identity

   \[
    F_{a+b}=F_aF_b-zF_{a-1}F_{b-1}
   \]

   gives exactly

   \[
    1-\rho_{s,u}
    ={F_{s+1}\over F_{s-u+1}F_u}.
   \]

   At \(x=1/2\), this yields

   \[
    1-\rho_{s,u}(1/2)
    ={s+2\over(u+1)(s-u+2)}.
   \]

   Thus the central renewal mass is \(\Theta(s)\), not \(\Theta(1)\)
   or \(\Theta(s^2)\).

2. **Resolvent index shift.**  The positivity proof for
   \(\mathcal D_q\) uses the path \(P_{2q}\) and the entry
   \((q-1,q+2)\), as written in (4.9b).  Using \(P_{2q+1}\) would shift
   the denominator to \(F_{2q+2}\) and is incorrect.  The corrected
   Cramer minor gives the critical added mass
   \(q^2/(4(q+1))\), which together with the constant term equals
   \((q+2)^2/(4(q+1))\).

3. **No rarity-times-length multiplication.**  Equations (5.3b)--(5.4a)
   are coefficient bounds on complete start languages.  Passing to a
   quotient-edge-disjoint packing only takes a subset; no independent
   interval factor is multiplied into a start probability.

4. **Genuine pointwise obstruction.**  Proposition 2.1 was checked by
   literal canonical block rotation, including the last identity
   \((0011)^k00=00(1100)^k\).  Its proper accumulated deficits are
   strictly below the corresponding first-maximum positions, so the
   displayed equality at time \(s\) is the first zero-winding return.

5. **Genuine carrier obstruction.**  Every word and every endpoint
   position in Proposition 4.2 was checked directly.  The copied word
   \(0S_40\) really crosses the \(T_1/T_0\) separator.  Consequently no
   theorem or conditional estimate in this report uses the retracted
   one-block localization or its former \(O(\log s)\) mass.

6. **Quantifier order.**  Corollary 5.1 first fixes
   \(0<\eta<1<M\), then lets \(m\to\infty\), and only afterward sends
   \(\eta\downarrow0\), \(M\uparrow\infty\).  It isolates the possible
   critical window \(k=\Theta(s)\); it does not prove that the actual
   PBBS mass in that window vanishes.
