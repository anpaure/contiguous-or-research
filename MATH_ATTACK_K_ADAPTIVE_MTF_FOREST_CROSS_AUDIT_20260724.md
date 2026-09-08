# Cross-audit of line K: adaptive-MTF Johnson forests

Date: 2026-07-24

Audited source:
\[
\text{MATH\_ATTACK\_K\_ADAPTIVE\_MTF\_FOREST\_20260724.md}.
\]

Method: independent theorem-proof reconstruction.  No web search, finite
search, probabilistic experiment, or solver was used.  The source's internal
audit record was not used as evidence.

## 0. Corrected verdict

The main proved claims of line K survive:

1. the virtual cyclic-cut closure is exact, including both flags crossing
   the cut;
2. the full-strip matching argument proves the adaptive-MTF forest theorem
   for every
   \[
   H=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right);
   \]
3. the strip degrees, codegree bound, quantitative matching hypotheses, and
   uncovered-vertex ledger have the stated constants;
4. the interval-transversal theorem and the colour-aware post-cut ledger are
   correct;
5. an integral decorated-atom matching with middle leave
   \[
   \Lambda=o(W/H)
   \]
   implies the literal fixed-window \(W+o(W)\) bound.

No Gaussian integral matching theorem is proved.  The following scope
corrections are required.

- The source uses \(L\) both for \(\log m\) and for the middle leave.  In
  this audit
  \[
  \mathscr L=\log m,\qquad \lambda=\log\mathscr L,\qquad
  \Lambda=W-(m+1)|\mathcal M|.
  \]
- The decorated-atom and hybrid-strip systems are not bipartite.  Their
  symmetric weightings prove fractional vertex-capacity feasibility only;
  they do not prove an integral Hall theorem or any part of the missing
  rounding statement.
- The threshold \(\Lambda=o(W/H)\) is sufficient and sharp for the displayed
  completion in which every uncovered middle mask becomes a singleton
  component.  It is not proved necessary for an architecture that connects
  or absorbs the leave.
- The factor-two transversal result is sharp for preserving each prescribed
  certified cut-edge occurrence by its own canonical boundary flag.  It is
  not an unrestricted lower bound for global colour support, because the
  same label may occur incidentally elsewhere.
- At \(q=1\), the decorated-atom instruction “choose \(s_1\) slots” already
  means choosing all \(m\) actual colours.  The following bullet mentioning
  all actual colours is redundant and must not be read as a second copy of
  those vertices.
- All fixed-window implications require one common oriented atom matching,
  including one simultaneous slot choice at every depth and sign.  Separate
  depthwise matchings do not suffice.

Subject to these corrections, I found no false theorem in the requested
parts.

## 1. Exact cyclic-cut closure

Let
\[
T_i=C\cup I_\gamma(i,\ell),\qquad i\in\mathbb Z_{2\ell},
\]
where \(H<\ell<m\).  The cyclic transition is
\[
p_i=z_i,\qquad q_i=z_{i+\ell}.                              \tag{1.1}
\]
Cut the edge from \(T_{2\ell-1}\) to \(T_0\).

### Theorem 1.1 (audited cyclic closure)

With terminal departures
\[
p_{2\ell-1+r}=z_{2\ell-1+r\pmod{2\ell}},
\qquad 0\le r<H,
\]
and initial queue
\[
\Theta_0=
(\{z_{2\ell-1}\},\{z_{2\ell-2}\},\ldots,
 \{z_{2\ell-H}\},R_0),
\]
where
\[
R_0=T_0^c\setminus\{z_{2\ell-1},\ldots,z_{2\ell-H}\},
\]
the canonical flags satisfy, for every \(0\le i<2\ell\) and
\(1\le q\le H\),
\[
P^-_{i,q}=C\cup I_\gamma(i+q,\ell-q),                       \tag{1.2}
\]
\[
P^+_{i,q}=C\cup I_\gamma(i-q,\ell+q).                       \tag{1.3}
\]

#### Proof

The continued departures are distinct.  At the terminal state
\[
T_{2\ell-1}
=C\cup\{z_{2\ell-1},z_0,\ldots,z_{\ell-2}\},
\]
the first \(H\) of them are present, and after each one is deleted the next
one remains present.  This uses \(H<\ell\).

The first \(H\) entries in \(\Theta_0\) lie in \(T_0^c\), and
\[
|R_0|=m-H>0.                                                \tag{1.4}
\]
For every \(i\), the arrival \(q_i=z_{i+\ell}\) is different from the
preceding \(H\) departures
\[
z_{i-1},z_{i-2},\ldots,z_{i-H},
\]
again because \(H<\ell\).  Hence the MTF update
\[
\Theta_{i+1}=(\{p_i\},\Theta_i\setminus\{q_i\})
\]
does not disturb those leading markers.  Induction gives
\[
\text{first \(q\) markers of }\Theta_i
=z_{i-1},z_{i-2},\ldots,z_{i-q}.                            \tag{1.5}
\]
Removing the next \(q\) departures from \(T_i\) proves (1.2), and adjoining
the markers (1.5) proves (1.3).

For \(i=2\ell-1\), (1.2) recovers the lower flag belonging to the deleted
cycle edge; for \(i=0\), (1.3) recovers its upper flag.  Thus the claim is
not merely an equality away from the cut.

Every moving coordinate has a cyclic positive run of length exactly
\(\ell>H\).  Cutting either leaves that run internal and long or splits it
into boundary runs.  The constant core is a boundary-to-boundary run, and
the unused core is absent throughout.  Hence no illegal internal short
positive run is introduced. \(\square\)

The backward index in (1.3) is necessary: \(P^+_{i,q}\) is the union window
ending at state \(i\).  As \(i\) ranges cyclically, it still enumerates the
whole upper strip row.

The source's stated generalization to other cyclic Johnson walks is valid
provided its disjoint-transition-support hypothesis is retained and
\(H<m\) is also understood.  The support hypothesis supplies both the
presence of the continued departures and the stability of the first
\(H\) queue markers; \(H<m\) supplies the nonempty residual.

## 2. Full-strip geometry, degrees, and codegrees

Put
\[
W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}.
\]
For disjoint \(C,D\) of size \(m-\ell\), and an undirected cycle on the
remaining \(2\ell\) coordinates, the strip contains
\[
C\cup I_\gamma(t,\ell+d),
\qquad -H\le d\le H,\quad t\in\mathbb Z_{2\ell}.
\]
Its rank is
\[
R=2\ell(2H+1).                                              \tag{2.1}
\]

The lowest row has interval length \(a=\ell-H\ge2\).  Its total intersection
is \(C\), its total union is \(C\cup R_\gamma\), and hence it recovers both
cores.  In a \(2\ell\)-cycle, adjacent coordinates occur together in
exactly \(a-1\) cyclic \(a\)-intervals, whereas a nonadjacent pair occurs
together at most \(a-2\) times.  Therefore the lowest row also recovers the
undirected cycle.  The strip hypergraph is simple.

Counting choices gives
\[
|E|=
\binom{2m}{m-\ell}
\cdot\binom{m+\ell}{m-\ell}
\cdot
\frac{(2\ell-1)!}{2},
\]
that is,
\[
|E|=\frac{(2m)!}{4\ell(m-\ell)!^2}.                         \tag{2.2}
\]
Double counting the \(2\ell\) incidences in rank \(m+d\) gives
\[
D_d=
\frac{(m+d)!(m-d)!}{2(m-\ell)!^2}.                          \tag{2.3}
\]
Thus \(D_0\) is the minimum, \(D=D_H=D_{-H}\) is the maximum, and
\[
\frac D{D_0}
=\frac{(m+H)!(m-H)!}{m!^2}
=\exp(O(H^2/m)),                                            \tag{2.4}
\]
\[
\log D=(2+o(1))\ell\log m.                                  \tag{2.5}
\]

For distinct band masks \(X,Y\), the stabilizer of \(X\) has orbit size
\[
\binom{|X|}{|X\cap Y|}
\cdot\binom{2m-|X|}{|Y\setminus X|}.                        \tag{2.6}
\]
Every nontrivial such product is at least \(m-H\).  The only rank-compatible
trivial-orbit candidate is \(X^c\), but it cannot share a strip with \(X\):
every member of a strip contains the same nonempty core \(C\).  A strip
through \(X\) has only \(2\ell\) vertices in the rank of \(Y\).  Orbit
double counting therefore gives
\[
\boxed{\frac{\Gamma}{D}\le\frac{2\ell}{m-H}.}               \tag{2.7}
\]
The use of the maximum degree \(D\), rather than \(D_{|X|-m}\), only weakens
the bound and is valid.

## 3. Quantitative matching constants

This section audits the application of the stated quantitative
near-regular hypergraph matching theorem.  The literature theorem itself is
used as a premise; none of line K's internal audits is used.

Let
\[
\mathscr L=\log m,\qquad \lambda=\log\mathscr L,
\]
\[
H=\left\lfloor
\sqrt{\frac{\mathscr L}{64\omega\lambda}}
\right\rfloor,\qquad
\ell=\lceil\omega H\rceil,
\]
where
\[
\omega\to\infty,\qquad \omega=o(\mathscr L/\lambda).
\]
Then \(H,\ell\to\infty\),
\[
\ell H=(1+o(1))\frac{\mathscr L}{64\lambda},
\]
and hence
\[
\boxed{
R=(1+o(1))\frac{\mathscr L}{16\lambda}.}                    \tag{3.1}
\]

Set
\[
C_*=\left\lceil\frac{2\ell D}{m-H}\right\rceil,\qquad
\eta=\frac{C_*\log(1+C_*)}{D}.
\]
Equations (2.5) and (2.7) give
\[
\frac{C_*\log D}{D}
=\Theta\!\left(\frac{\ell^2\mathscr L}{m}\right),            \tag{3.2}
\]
\[
\eta=\Theta\!\left(\frac{\ell^2\mathscr L}{m}\right),        \tag{3.3}
\]
and, because \(\ell\) is polylogarithmic and \(C_*\to\infty\),
\[
\log\eta=-\mathscr L+O(\lambda).                            \tag{3.4}
\]
Combining (3.1) and (3.4),
\[
\boxed{
\eta^{1/(R-1)}
\le \mathscr L^{-16+o(1)}.}                                 \tag{3.5}
\]

The matching theorem's side conditions check as follows:
\[
\frac{R}{\log D}=O(H/\mathscr L)=o(1),                      \tag{3.6}
\]
so \(R\le\frac12\log D\);
\[
\log\!\left(
e^{2R}\frac{C_*\log D}{D}
\right)
=-\mathscr L+2R+O(\lambda)
=-\mathscr L+o(\mathscr L),                                 \tag{3.7}
\]
so the growing-rank codegree condition holds; and
\[
\frac{H^2}{m}
=o\!\left[
\left(\frac{\ell^2\mathscr L}{m}\right)^{1/3}
\right],                                                    \tag{3.8}
\]
so the relative degree defect in (2.4) is below the theorem's permitted
defect.  Also
\[
\left(\frac{C_*\log D}{D}\right)^{1/3}
=O\!\left(
\left(\frac{\ell^2\mathscr L}{m}\right)^{1/3}
\right)=o(1),                                               \tag{3.9}
\]
which verifies the small-defect condition.

The matching conclusion leaves
\[
U=O\!\left(R\eta^{1/(R-1)}|V|\right)
\]
band vertices.  Since
\[
|V|\le(2H+1)W,\qquad R(2H+1)\le\mathscr L^{3/2+o(1)},
\]
(3.5) yields
\[
\frac UW\le\mathscr L^{-14.5+o(1)}
\le\mathscr L^{-10}                                        \tag{3.10}
\]
for all sufficiently large \(m\).  Thus the exponent \(10\) and the
constant \(64\) are conservative and valid.

### The arbitrary prescribed-\(H\) quantifier

The source's proof after its equation (3.30) is terse but repairable.  If
\[
H=o\!\left(\sqrt{\frac{\mathscr L}{\lambda}}\right),
\]
put
\[
g=\frac{\mathscr L}{\lambda H^2}\longrightarrow\infty
\]
and choose \(\alpha\to\infty\) with \(\alpha=o(g)\); for example, take a
sufficiently small rounded version of \(\sqrt g\).  Let
\[
\ell=\lceil\alpha H\rceil.
\]
Then
\[
\frac{\ell}{H}\to\infty,\qquad
\ell H=o(\mathscr L/\lambda),                               \tag{3.11}
\]
and one may make \(\ell H\le\mathscr L/(64\lambda)\) eventually.
The preceding estimates give
\[
R=o(\mathscr L/\lambda),\qquad
U=W\mathscr L^{-\omega(1)},                                 \tag{3.12}
\]
while \(H/\ell\to0\).  This proves the full quantified claim, including
bounded prescribed \(H\).

## 4. Exact strip-to-forest ledger

Suppose the matching selects \(p\) strips and write \(s=2\ell\).  The exact
uncovered counts are
\[
u_0=W-sp,\qquad u_q^-=u_q^+=N_q-sp,
\]
\[
U=u_0+\sum_{q=1}^H(u_q^-+u_q^+).                            \tag{4.1}
\]
Cut every selected middle cycle once, use Theorem 1.1, and add each
uncovered middle mask as an isolated component.  Then
\[
c=p+u_0,\qquad \rho_H=0.                                    \tag{4.2}
\]

Each selected path has \(s-1\) actual edges.  The matching makes both
depth-one strip rows separately rainbow, so all these actual edges can be
certified:
\[
e=p(s-1).                                                    \tag{4.3}
\]
Therefore
\[
N_1-e=N_1-sp+p=u_1^-+p
\le U+\frac W{2\ell}=o(W).                                  \tag{4.4}
\]
The virtual closure recovers all \(s\) cyclic flags at every depth, and
matching disjointness makes them globally distinct.  Thus
\[
\widetilde M_q^\pm\le u_q^\pm.                              \tag{4.5}
\]
Consequently
\[
\begin{aligned}
Hc+\sum_{q=2}^H(\widetilde M_q^-+\widetilde M_q^+)
&\le \frac{HW}{2\ell}+(H+1)U\\
&=\frac{H}{2\ell}W+o(W)
=o(W).                                                       \tag{4.6}
\end{aligned}
\]
This proves the advertised near-square-root-log theorem.

The cyclic closure is exactly what changes the old cube-root restriction:
one now needs only \(\ell/H\to\infty\), rather than paying
\(\Theta(H^2p)\) for independently lost boundary windows.

## 5. Gaussian reductions and common ownership

The full-rainbow strip obstruction is correct.  If
\(q=t\sqrt m+o(\sqrt m)\), then
\[
\frac{N_q}{W}\to e^{-t^2}<1.
\]
A family covering \((1-o(1))W\) middle masks cannot use the same number of
distinct rank-\((m-q)\) labels.  Thus a Gaussian construction must use
rank-dependent certification or controlled repeated labels.

The odd-factor cut is also correctly normalized.  It gives
\[
B=\frac W{m+1}
\]
complementary geodesics, each with \(m+1\) middle states.  Removed
coordinates do not return and inserted coordinates are not removed, so
\[
c=B,\qquad \rho_H=0,\qquad Hc=O_A(W/\sqrt m).
\]
The queue and dummy orders in the source yield
\[
P^-_{t,q}=I_w(t+q,m-q),\qquad
P^+_{t,q}=I_w(t-q,m+q),                                     \tag{5.1}
\]
including boundary states.  The actual upper edge colours partition rank
\(m+1\); this follows by removing the cut coordinate from the
middle intervals of the odd factor that contain it and then complementing
inside the remaining \(2m\) coordinates.

Accordingly, the support bounds labelled Missing Theorem 5.1 are genuinely
sufficient.  They remain **UNPROVED**.

## 6. Certified-slot atoms and the fractional ledger

Put
\[
K=m+1,\qquad r_q=\frac{N_q}{W},\qquad
s_q=\lfloor Kr_q\rfloor.
\]
The recurrence
\[
r_{q+1}=r_q\frac{m-q}{m+q+1}
\]
and \(r_1=(K-1)/K\) prove inductively that
\[
s_q\le K-q,\qquad s_1=K-1=m.                                \tag{6.1}
\]
Uniformly for \(q\le A\sqrt m\),
\[
r_q=\exp(-q^2/m+O_A(m^{-1/2})),\qquad
s_q=\Theta_A(K).                                            \tag{6.2}
\]

Every decorated atom contains one common oriented complementary geodesic,
all its \(K\) middle states, and one simultaneous selection of \(s_q\)
internal flags of each sign at every depth.  For its internal fragments,
\[
D^-_{i,q}=P^-_{i,q},\qquad
D^+_{i,q}=P^+_{i+q,q}.                                      \tag{6.3}
\]
Thus the atom definition preserves common ownership and one MTF state; it
does not optimize the depths separately.

Let \(D_0,D_q^\pm\) be the part degrees in the full invariant decorated
family.  Incidence double counting gives
\[
D_0W=|E|K,\qquad D_q^\pm N_q=|E|s_q.
\]
Hence
\[
\frac{D_q^\pm}{D_0}
=\frac{s_qW}{KN_q}\le1,                                    \tag{6.4}
\]
with equality at \(q=1\), and
\[
1-O_A(1/m)\le\frac{D_q^\pm}{D_0}\le1                       \tag{6.5}
\]
uniformly on the Gaussian window.

Weighting every decorated atom by \(1/D_0\) is therefore a fractional
matching: it saturates the middle part and respects every certified-colour
capacity.  Its total mass is \(W/K\), and the unused capacity in either
signed depth-\(q\) part is
\[
\epsilon_q
:=N_q-\frac WKs_q,\qquad
0\le\epsilon_q<\frac WK.                                   \tag{6.6}
\]
Thus
\[
2\sum_{q=1}^H\epsilon_q<\frac{2HW}{K}
=O_A(W/\sqrt m).                                            \tag{6.7}
\]

This proves exact fractional feasibility only.  No total-unimodularity,
matching-polytope cut theorem, or integral Hall condition is established.
The high-precision atom rounding statement remains **UNPROVED**.

## 7. The sharpened middle-leave implication

This is the most important quantitative audit.  Let an integral decorated
atom matching have \(p\) atoms and define
\[
\Lambda=W-Kp.                                               \tag{7.1}
\]
Use the \(p\) geodesics as path components and the \(\Lambda\) uncovered
middle masks as singleton components.  Then exactly
\[
c=p+\Lambda
=\frac WK+\left(1-\frac1K\right)\Lambda,                    \tag{7.2}
\]
\[
\rho_H=0,\qquad e=mp,\qquad
N_1-e=\frac{m\Lambda}{K}.                                   \tag{7.3}
\]
For every \(q\ge2\) and either sign, the matching supplies \(ps_q\)
distinct canonical flags, so
\[
\begin{aligned}
\widetilde M_q^\pm
&\le N_q-ps_q\\
&=\epsilon_q+\frac{\Lambda}{K}s_q
<\frac WK+\Lambda.                                          \tag{7.4}
\end{aligned}
\]

Substitution into the literal forest word ledger gives the explicit bound
\[
\boxed{
\mathcal L_{\rm band}-W
<(4H-1)\frac WK+(4H+1)\Lambda.}                             \tag{7.5}
\]
Indeed, the component term contributes
\[
(2H+1)\left[\frac WK+\left(1-\frac1K\right)\Lambda\right],
\]
the first-shadow term contributes \(2m\Lambda/K\), and the two signed deep
towers contribute less than
\[
2(H-1)(W/K+\Lambda).
\]

For \(H=\lceil A\sqrt m\rceil\),
\[
\frac{HW}{K}=O_A(W/\sqrt m)=o(W).
\]
Therefore
\[
\boxed{\Lambda=o(W/H)\Longrightarrow
\mathcal L_{\rm band}=W+o(W).}                              \tag{7.6}
\]
Equivalently, it gives \(N_1-e=o(W)\), \(Hc=o(W)\), and total deep defect
\(o(W)\).

There is no omitted cut, seam, or reset charge.  A complementary geodesic
has no internal positive re-exit, so \(\rho_H=0\); this construction performs
no cuts or splices; and every singleton is already charged by
\((2H+1)c\).  When \(m\ge2H\), one may take initial singleton markers
\[
b_{m-1},b_{m-2},\ldots,b_{m-H},
\]
the remaining \(b\)'s as residual, and terminal dummy departures
\[
b_0,b_1,\ldots,b_{H-1}.
\]
These choices do not alter the certified internal identities (6.3).

The exact quantifier is:

> For every fixed \(A>0\), for all sufficiently large \(m\), one common
> decorated matching, with one orientation and simultaneous slot choices at
> every signed depth, satisfies \(H\Lambda/W\to0\).

The rate may depend on \(A\).  Separate matchings at different depths do not
give (7.4).

The little-oh is sharp for this singleton completion.  If
\(\Lambda\sim cW/H\) with \(c>0\), the singleton component term alone is
\[
(2H+1)\Lambda\sim2cW.
\]
A generic \(\Lambda=o(W)\) guarantee is likewise insufficient; for example,
\(\Lambda=W/\sqrt H\) is \(o(W)\) but has \(H\Lambda\gg W\).
This is not a lower bound against an absorber that joins the leave into
longer paths.

## 8. Hybrid strip packing/covering

The alternative strip reduction is correctly normalized.  If \(p\) strips
have disjoint middle and signed depth-one rows and
\[
\delta=N_1-2\ell p=o(W/H),
\]
then
\[
u_0=W-2\ell p=(W-N_1)+\delta,
\]
\[
c=p+u_0,\qquad \rho_H=0,\qquad
N_1-e=\delta+p.
\]
Under \(H\ll\ell=o(m)\),
\[
Hc\le\frac{HW}{2\ell}+\frac{HW}{m+1}+H\delta=o(W).          \tag{8.1}
\]

Weighting every strip by
\[
\frac{\alpha}{D_0},\qquad \alpha=\frac{N_1}{W},
\]
gives middle load \(\alpha<1\), signed depth-one load one, and
signed depth-\(q\) load
\[
\alpha\frac{D_q}{D_0}=\frac{N_1}{N_q}\ge1.
\]
This is a fractional certificate for a hybrid packing/covering problem, not
a fractional matching in an ordinary capacity-one hypergraph.  It supplies
no integral conclusion.  The corresponding integral strip lemma remains
**UNPROVED**.

## 9. Projected defects

For one sign and one depth \(q\), the projected multigraph has
\(W-C\) edge occurrences.  After deleting its \(\ell_q\) loops, let it have
\(d_q\) connected components and cyclomatic number
\[
\beta_q=(W-C-\ell_q)-|V(\Gamma_q)|+d_q.
\]
With \(\mu_q=C-d_q\),
\[
\begin{aligned}
\widetilde M_q
&=N_q-|V(\Gamma_q)|\\
&=\ell_q+\beta_q+\mu_q-(W-N_q).                             \tag{9.1}
\end{aligned}
\]
This is an exact algebraic identity.

For lower flags,
\[
P^-_{i+1,q}=P^-_{i,q}-\{p_{i+q}\}+\{q_i\}.
\]
It is a loop precisely when the entering coordinate \(q_i\) exits within
\(q\le H\) transitions, or when an illegal dummy repeats it.  The former
short-run interval is hit; after splitting and recanonicalizing, that exit is
no longer within the same component's canonical \(q\)-horizon.  The latter
case is excluded by compatible dummy legality.  Thus the lower tower has no
loops.  On the upper side, if \(s_i\) is the pre-update queue
position of \(q_i\), the step is a loop exactly when \(s_i\le q\).  Hence
\[
\ell_q^+=|\{i:s_i\le q\}|,
\]
and the source's summed loop formula follows.  These statements describe
the defect but do not bound \(\beta_q\) or \(\mu_q\).

## 10. Interval transversals and the exact cut ledger

Represent a short positive run entering at transition \(a\) and exiting at
transition \(b\) by the closed edge interval
\[
I_x=[a,b],\qquad b-a\le H.
\]
A cut set removes every internal short run if and only if it meets every
such interval.  Earliest-right-endpoint greedy selection proves
\[
\boxed{
\tau_H=
\max\{\text{number of pairwise edge-disjoint short-run intervals}\}.}     \tag{10.1}
\]
Every transition belongs to at most \(H+1\) short-run intervals: their
entry edges are distinct and lie among the preceding \(H+1\) positions.
Therefore
\[
\boxed{\frac{\rho_H}{H+1}\le\tau_H\le\rho_H.}               \tag{10.2}
\]
The source's sliding family
\[
[1+t,H+1+t],\qquad 0\le t\le H,
\]
is realizable by a simple Johnson path and has
\(\rho_H=H+1,\tau_H=1\), so the lower constant is sharp.

Let \(C\) be a transversal in a forest with \(c\) components and \(e\)
certified edges.  The post-cut component count is \(c+|C|\).  At a certified
cut edge, the upper colour is always recovered on the right by placing the
removed coordinate first in the initial complement queue.  The prescribed
lower colour fails at the left terminal boundary exactly when the removed
coordinate entered within the previous \(H\) transitions and the exit edge
is the unique cut in that short-run interval.  Thus the bad-occurrence count
\(b_H(C)\) in the source is exact, and
\[
\begin{aligned}
\mathcal L_{\rm band}\le{}&
W+(2H+1)(c+|C|)+2(N_1-e)+b_H(C)\\
&+\sum_{q=2}^H
(\widetilde M_{q,C}^-+\widetilde M_{q,C}^+).                \tag{10.3}
\end{aligned}
\]
The deep defects in (10.3) must be recomputed from this same cut set and its
one compatible boundary assignment.

Since \(b_H(C)\le|C|\), a minimum transversal replaces the reset-scale term
based on \(\rho_H\) by
\[
H(c+\tau_H)                                                  \tag{10.4}
\]
up to absolute constants.  Taking every greedy right endpoint together with
the left endpoint of its witness interval gives
\[
|C|\le2\tau_H,\qquad b_H(C)=0.                              \tag{10.5}
\]
The sliding example has a unique one-point transversal, and that point is a
bad exit for one certified witness.  Thus factor two is sharp for the
guarantee \(b_H(C)=0\).  It is not proved sharp for preservation of global
support, because another occurrence may carry the same lower label.

## 11. Seam and component claims

The exact seam formula is valid.  A seam can create a short run only by:

1. closing the terminal run of the removed coordinate;
2. opening the initial run of the inserted coordinate; or
3. fusing terminal and initial boundary runs of a common coordinate.

These cases are disjoint and yield exactly the three terms in the source's
\(\eta_H(P,Q)\).  Among common coordinates, terminal numeric ages are
distinct; since both fused ages are at least one, at most \(H-1\) common
coordinates can contribute.  Together with the two endpoint indicators,
\[
\eta_H(P,Q)\le H+1.
\]

The static composition theorem is also correctly scoped.  A new run crossing
at least two seams contains every middle state of an intervening
degree-two base block, so it is longer than \(H\); a short new run crosses
one seam and is counted locally.

Under the source's strong endpoint-safety hypothesis, greedy splicing leaves
an endpoint set \(S\) with \(|S|=2c\) and at most \(c\) induced Johnson
edges.  The least-eigenvalue inequality for \(J(2m,m)\),
\[
2e(S)\ge
\frac{(m^2+m)|S|^2}{W}-m|S|,
\]
then gives
\[
c\le\frac{W}{2m}.
\]
This is a conditional component/run theorem only; it does not control the
deep projected supports.

## 12. Final logical status

The following statements are proved by the audited line:

- exact virtual cyclic closure;
- the adaptive-MTF forest theorem through
  \(H=o(\sqrt{\log m/\log\log m})\);
- the exact strip and transversal ledgers;
- fractional feasibility of the decorated-atom and hybrid-strip
  formulations;
- the implication
  \[
  \Lambda=o(W/H)\Longrightarrow\mathrm{AD}_A
  \]
  for the singleton-leave decorated-atom architecture;
- the projected-defect and seam identities.

The following remain **UNPROVED**:

1. the odd-cut support theorem;
2. high-precision integral atom rounding;
3. the integral hybrid strip packing/covering lemma;
4. any alternative augmentation theorem controlling all deep supports.

The smallest exact missing lemma for the decorated-atom lane is:

> For every fixed \(A>0\), with \(H=\lceil A\sqrt m\rceil\), select one
> family of pairwise middle-disjoint oriented complementary geodesics and,
> on each selected geodesic, \(s_q\) internal flags of each sign at every
> \(q\le H\), such that the selected labels are pairwise distinct inside
> every signed rank and the uncovered middle count \(\Lambda\) satisfies
> \[
> H\Lambda=o(W).
> \]

This is exactly the integral statement hidden in the source's equation
(6.20), with all ownership quantifiers made explicit.  It is sufficient but
not known necessary outside the singleton-leave architecture.

Accordingly, line K contains a valid non-Gaussian theorem and valid exact
Gaussian reductions, but no proof of the Gaussian theorem or of the final
conjecture.
