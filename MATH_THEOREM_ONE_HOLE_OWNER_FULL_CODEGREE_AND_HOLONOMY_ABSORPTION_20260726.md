# One-hole promotion rings: full-codegree precision and holonomy-safe absorption

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Use

\[
H=\lfloor\sqrt{m\log m}\rfloor,\qquad
M=m+H,\qquad s=m-H,
\]

\[
W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
q_0=\lceil m^{1/4}\rceil.
\]

In the one-hole owner hypergraph, an edge is a top \(U\), a directed
cyclic frame on \(U\), and one marked phase; it contains the top marker
and the other \(M-1\) middle owners.

There are two different meanings of root leave.

* The strict capacity-one fractional matching number is

  \[
  \nu^*=\frac{W}{M-1}.                                     \tag{0.1}
  \]

  Thus the total number of unused tops is at least
  \(N_H-\nu^*\). This deterministic term is unrelated to nibble error.

* The relevant **owner-factor defect** is

  \[
  \operatorname{def}(\mathcal M)=\nu^*-|\mathcal M|.       \tag{0.2}
  \]

  The exact retained-tag packet count is

  \[
  K_0=\left\lfloor\frac{N_{q_0}-N_H}{M-2}\right\rfloor,
  \]

  and

  \[
  \boxed{\nu^*-K_0=(1+o(1))\frac{N_H}{\sqrt m}.}           \tag{0.3}
  \]

  Therefore

  \[
  \boxed{\operatorname{def}(\mathcal M)
  =o(N_H/\sqrt m)}                                        \tag{0.4}
  \]

  is exactly the precision needed to obtain at least \(K_0\) disjoint
  owner rings and then trim to the tag census.

The full-codegree calculation gives an exact criterion for (0.4). Let
\(\mathfrak B_H^-\) be the Gould--Kelly bottleneck of the one-hole
hypergraph. A diagonal theorem with owner leave
\[
W(\mathfrak B_H^-)^{-1+o(1)}
\]
would give (0.4) precisely when

\[
\boxed{(\mathfrak B_H^-)^{1-o(1)}\gg\sqrt m.}              \tag{0.5}
\]

The pair term is favorable:

\[
\sqrt{\frac{D_{\min}}{C_2}}
=(1+o(1))\frac m{\sqrt2}.                                 \tag{0.6}
\]

For all higher codegrees there is an exact marked-breakpoint formula.
What is not proved is the uniform extremal inequality

\[
C_j^-\le D_{\min}m^{-(1/2+\varepsilon)(j-1)}
\quad(4\le j\le M)                                       \tag{0.7}
\]

for some \(0<\varepsilon<1/2\). This is sufficient for (0.5).
Consequently the full codegree sequence is not known to obstruct the
requested leave, but it is not yet proved to permit it either.

Even if (0.7) is granted, current nibble theorems do not attain (0.4):
their edge-uniformity hierarchy is fixed before \(m\to\infty\), and
their \((\log D)^A\) loss is already larger than the required
\(W/\sqrt m\) owner-vertex leave.

The minimal replacement is a holonomy-safe absorber which turns the
valid first bites into a matching with (0.4), while keeping parity,
mod-three, and all fixed finite-character residual coefficients small.
It is stated exactly in Section 6.

If “root leave” instead means literal unused tops rather than (0.2),
then a capacity-one matching cannot remove the deterministic
\(N_H-\nu^*\) term. The correct model is the load-\(\{1,2\}\) owner
resolution of the companion promotion-ring holonomy-resolution note,
which absorbs the scalar excess as second middle copies.

## 1. Exact owner arithmetic

Let \(\mathcal R^-\) be the one-hole hypergraph. Its vertices are the
top set

\[
\mathcal U=\binom{[2m]}M
\]

and the middle owner set

\[
\mathcal X=\binom{[2m]}m.
\]

Every top has degree

\[
D_U=M!,                                                   \tag{1.1}
\]

because it has \((M-1)!\) directed cyclic frames and \(M\) choices of
marked phase.

Every middle owner has degree

\[
D_X=\frac{(m!)^2(M-1)}{s!}.                               \tag{1.2}
\]

Indeed, choose its \(H\)-set complement inside the top, choose a frame
in which that complement is an \(H\)-window, and mark any of the other
\(M-1\) phases.

Moreover

\[
\frac{D_X}{D_U}=\frac{M-1}{\lambda_H}=1+O(H/m),            \tag{1.3}
\]

and \(D_U\) is the smaller degree in the covering-side calibration.
Giving every edge weight \(1/D_X\) loads every owner exactly once and
every top by \(D_U/D_X<1\). Owner capacity gives the converse upper
bound, proving (0.1).

The expansion

\[
\frac{N_{q_0}}W
=1-\frac1{\sqrt m}+O(m^{-3/4})                            \tag{1.4}
\]

and direct subtraction give (0.3). Hence an owner matching whose defect
is little-oh of the scale in (0.3) contains at least \(K_0\) edges.

In owner-vertex language, (0.4) is equivalent to

\[
W-(M-1)|\mathcal M|=o(W/\sqrt m).                         \tag{1.5}
\]

This is the absolute leave which a matching/absorption theorem must
prove.

## 2. Pair codegrees and the valid first bite

Let \(X,Y\in\mathcal X\) have Johnson distance \(d\).
For \(1\le d<H\),

\[
\frac{D^-(X,Y)}{D_X}
=\frac{2(M-2)}{(M-1)\binom md^2}.                         \tag{2.1}
\]

At \(d=H\),

\[
\frac{D^-(X,Y)}{D_X}
=\frac{(M-2)(s+1)}{(M-1)\binom mH^2},                     \tag{2.2}
\]

and at \(d>H\) the codegree is zero.

A top--owner pair has codegree \(H!m!(M-1)\), which is
superpolynomially smaller than either incident degree; two top vertices
have codegree zero. Therefore

\[
\frac{C_2}{D_U}=\frac{2+o(1)}{m^2},                       \tag{2.3}
\]

which proves (0.6).

Inside one repaired ring edge, the exact normalized unordered pair mass
is

\[
\frac1{D_U}\sum_{\{v,w\}\subset e}D^-(v,w)
=\frac2m+O(m^{-2}).                                      \tag{2.4}
\]

Thus a fresh isolated bite is efficient: its internal collision
correction is \(o(1)\). The unresolved issue is regeneration and
terminal absorption, not the first bite.

## 3. Exact marked full-codegree formula

Let \(C_j^-\) be the maximum number of one-hole edges containing a fixed
\(j\)-set of augmented vertices.

Any set containing two top vertices has codegree zero. Suppose first
that \(Y_1,\ldots,Y_j\) are distinct middle owners. For a common carrier
complement \(A=[2m]\setminus U\), put

\[
I_i=Y_i\setminus A.
\]

These must be \(H\)-windows in one cyclic order of \(U\). Let
\(c_U(I_1,\ldots,I_j)\) denote the number of such directed cyclic
orders, modulo rotation. Since the marked phase must avoid the \(j\)
prescribed owner phases,

\[
\boxed{
D^-(Y_1,\ldots,Y_j)
=(M-j)
\sum_{\substack{A\subseteq\cap_iY_i\\|A|=s}}
c_{A^c}(Y_1\setminus A,\ldots,Y_j\setminus A)}
\tag{3.1}
\]

for \(1\le j\le M-1\).

If one prescribed vertex is a top \(U\) and the other \(j-1\) vertices
are owners \(Y_i\subset U\), then

\[
\boxed{
D^-(U,Y_1,\ldots,Y_{j-1})
=(M-j+1)c_U(U\setminus Y_1,\ldots,U\setminus Y_{j-1}).}
\tag{3.2}
\]

Otherwise this codegree is zero.

The unmarked cyclic coefficient has the exact breakpoint formula. Put

\[
a_J=\#\{u\in U:\{i:u\in I_i\}=J\},
\]

and, for starts \(t=(0,t_2,\ldots,t_j)\), put

\[
c_J(t)=\#\{z\in\mathbb Z_M:
              \{i:z\in[t_i,t_i+H)\}=J\}.
\]

Then

\[
\boxed{
c_U(I_1,\ldots,I_j)
=
\sum_{\substack{t_2,\ldots,t_j\ {\rm distinct}\\
                 c_J(t)=a_J\ \forall J}}
\prod_{J\subseteq[j]}a_J!.}
\tag{3.3}
\]

Equations (3.1)--(3.3) are the complete full-codegree sequence. The
remaining problem is the extremal optimization over realizable circular
profiles.

Define

\[
\mathfrak B_H^-=
\min\left\{
\sqrt{\frac{D_U}{C_2^-}},
\min_{4\le j\le M}
\left(\frac{D_U}{C_j^-}\right)^{1/(j-1)}
\right\}.                                                \tag{3.4}
\]

The pair calculation gives the first term
\((1+o(1))m/\sqrt2\). Thus (0.7), or any bound implying
\(\mathfrak B_H^-/\sqrt m\to\infty\), is the exact unresolved
higher-codegree inequality.

## 4. Exact conversion from codegree leave to owner-factor leave

Suppose a group-respecting diagonal matching theorem gives owner-vertex
leave

\[
\ell_X\le W(\mathfrak B_H^-)^{-1+o(1)}.                   \tag{4.1}
\]

Since every selected edge uses \(M-1\) owner vertices,

\[
\operatorname{def}(\mathcal M)
=\frac{\ell_X}{M-1}.                                      \tag{4.2}
\]

Using \(W/(M-1)=(1+o(1))N_H\),

\[
\operatorname{def}(\mathcal M)
\le N_H(\mathfrak B_H^-)^{-1+o(1)}.                       \tag{4.3}
\]

Therefore (0.4) follows exactly under (0.5).

This calculation also shows why an ordinary \(o(W)\) leave is not
enough. The theorem must give the sharper absolute owner leave
\(o(W/\sqrt m)\).

The present full-codegree nibble theorem has formal leftover

\[
V(\mathfrak B_H^-)^{-1+\gamma}(\log D_U)^A,               \tag{4.4}
\]

under

\[
\frac1{D_U}\ll\frac1A\ll\gamma\ll\frac1M.
\]

Here

\[
\log D_U=\Theta(m\log m),\qquad
\mathfrak B_H^-\le O(m).
\]

Thus (4.4) is not \(o(W/\sqrt m)\) in the diagonal \(M\sim m\), even
if the optimal-looking bound \(\mathfrak B_H^-=\Theta(m)\) is assumed.
Current nibble technology therefore cannot provide the required owner
precision.

## 5. Finite-character safety

For \(2\le\ell\le K\), \(1\le a<\ell\), and a balanced
\(B\subset[2m]\), define

\[
\chi_{B,\ell,a}(X)
=\exp\!\left(\frac{2\pi ia}{\ell}|X\cap B|\right).         \tag{5.1}
\]

For an owner residual \(\mathcal Z\subseteq\mathcal X\), put

\[
\|\mathcal Z\|_{\mathrm{hol},K}
=
\max_{B,\ell,a}
\left|
\sum_{X\in\mathcal Z}\chi_{B,\ell,a}(X)
-\frac{|\mathcal Z|}{W}
\sum_{X\in\mathcal X}\chi_{B,\ell,a}(X)
\right|.                                                  \tag{5.2}
\]

Define the root version analogously on \(\binom{[2m]}M\).
Parity and mod-three traps have holonomy of the same order as their
mass, despite exact point balance.

A nibble trajectory is \(K\)-safe down to scale \(W/\sqrt m\) if every
owner residual \(\mathcal Z\) of size at least \(W/\sqrt m\) and its
corresponding root residual satisfy

\[
\|\mathcal Z\|_{\mathrm{hol},K}=o(|\mathcal Z|).           \tag{5.3}
\]

This is a deterministic residual condition, not a marginal probability
claim.

## 6. Minimal absorption statement

The following is sufficient and strictly stronger than the valid
first-bite estimate, while avoiding a generic hereditary hypothesis.

### One-hole holonomy-safe absorption theorem \(\mathrm{OHSA}_K\)

For every fixed \(K\ge3\), the one-hole promotion hypergraph contains a
reserved family \(\mathscr A_m\) of alternating marked-frame trades using

\[
o(W/\sqrt m)                                              \tag{6.1}
\]

owner vertices, with this universal property.

There is a steering of the valid isolated bites outside the reservoir
such that, at every intermediate time:

1. the root and owner residuals are \(K\)-safe in the sense of (5.3);
2. their normalized degrees and full codegrees remain within
   \(1+o(1)\) of the binomially thinned values down to the bottleneck
   \(\mathfrak B_H^-\); and
3. no reservoir vertex is used.

This steered trajectory reaches owner residual size

\[
W(\mathfrak B_H^-)^{-1+o(1)},                             \tag{6.2}
\]

and switches supported on \(\mathscr A_m\) then produce a matching
\(\mathcal M\) satisfying

\[
W-(M-1)|\mathcal M|=o(W/\sqrt m),                         \tag{6.3}
\]

\[
\operatorname{def}(\mathcal M)=o(N_H/\sqrt m),            \tag{6.4}
\]

and the final owner and root residuals remain \(K\)-safe.

For the nested promotion problem, the same switches must preserve the
contracted chain atoms and make the two depth-\(q_0\) trace maps
injective up to \(o(W)\); deeper tag thresholds are then handled by the
nested quota absorber.

### Why this is minimal

1. Equation (2.4) already validates the first bite, so another local
   pair estimate adds nothing.
2. Equation (4.3) shows that the stopping scale must beat
   \(W/\sqrt m\), equivalently (0.5).
3. Without finite-character safety, coordinate-balanced packet-free
   residuals invalidate arbitrary regeneration.
4. The reservoir budget in (6.1) is necessary not to consume the
   entire slack (0.3) between fractional owner capacity and the desired
   tag census.
5. The depth-\(q_0\) two-sided colours are fixed when owner rings are
   chosen; no later tag assignment can repair their collisions.

A stronger resolution theorem may replace \(\mathrm{OHSA}_K\): an
edge-colouring of the marked-frame catalogue whose colour classes are
owner matchings of size

\[
\frac{W}{M-1}-o(N_H/\sqrt m)
\]

and whose residuals satisfy (5.3). Such a resolution immediately
supplies the absorber output by choosing one colour.

## 7. Boundary

The exact state is:

* first-bite overlap \(2/m+O(m^{-2})\): proved;
* fractional owner factor \(W/(M-1)\): proved;
* slack to the retained-tag count:
  \((1+o(1))N_H/\sqrt m\): proved;
* all marked higher codegrees: reduced exactly to (3.1)--(3.3);
* codegree condition for the target:
  \((\mathfrak B_H^-)^{1-o(1)}\gg\sqrt m\): proved;
* a sufficient profile inequality (0.7): open;
* diagonal conversion by current nibble theorems: unavailable;
* minimal missing result: \(\mathrm{OHSA}_K\).

Thus the valid first bite should be retained, but its iteration must be
coupled to a prebuilt, finite-character-safe marked-frame absorber. A
generic residual-regeneration theorem is both stronger than necessary
and false.
