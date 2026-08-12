# Ordinary promotion frames: the exact finite pair-column cutoff and a literal pair-star residual

Date: 2026-07-27

Scope: the unseeded ordinary-frame owner near-resolution hypergraph and
the ordered pair-column backward tower.  All arguments are purely
combinatorial.

## 0. Verdict

Put

\[
 n=2m,\qquad M=m+H,\qquad r=M+1,
 \qquad H=(1+o(1))\sqrt{m\log m},
\]

and let \(\mathcal H_{m,H}\) be the hypergraph whose edge is one
rank-\(M\) top together with the \(M\) cyclic rank-\(m\) windows of a
cyclic order on that top.  The ordered pair-column proposal has a valid
finite-cutoff version, but only under a genuinely dynamic whole-arm
common-event estimate.

More precisely, let \(B=C_0(\log m)^2\), let

\[
 \alpha={C(\log m)^{O(1)}\over m^2z^2}
        =m^{-19/10+o(1)},\qquad z=m^{-1/20},
 \tag{0.1}
\]

and let \(T=r\log(1/z)=O(m\log m)\).  Suppose the corrected tower,
including row--column and column--column pairs, is initialized through
level \(B\), and suppose every two equality-resolved displayed arms
have common edge-clock mass at most

\[
 \beta_t\le {(\log m)^{O(1)}\over m^2u(t)^2}.          \tag{0.2}
\]

Then a finite backward potential closes the tower.  If the top state has
\(p=O((\log m)^2)\) displayed nonprivate arms, its uncancelled top
growth has integrated size

\[
 Q\le C T p^2\sup_t\beta_t=m^{-9/10+o(1)}=o(1),      \tag{0.3}
\]

while

\[
 A\alpha=O(T\alpha)=m^{-9/10+o(1)}.                  \tag{0.4}
\]

Consequently the cutoff remainder is

\[
 \exp(Q){(A\alpha)^B\over B!}
 =\exp[-(9/10+o(1))B\log m]
 =\exp[-\Theta((\log m)^3)].                          \tag{0.5}
\]

This is an exact conditional repair; an all-order initializer is not
needed.

The condition is not supplied by the known degree and higher-codegree
geometry.  At time zero the proved owner-versus-frame influence bound
does give (0.2).  But there is a literal edge-deletion residual of
\(\mathcal H_{m,H}\) containing two frame arms \(f,f'\) for which

\[
 { |\{g:g\cap f\ne\varnothing,\ g\cap f'\ne\varnothing\}|
   \over r\Delta_{\rm res}}
 \ge c_0>0.                                             \tag{0.6}
\]

The construction is deterministic and uses only complete physical
frames.  Thus no pointwise \(m^{-2+o(1)}\) estimate can be hereditary
under arbitrary binary edge deletion.  Proving it, or its aggregate
incidence-weighted substitute, along the actual random trajectory is
exactly a form of HCE/ADLE, not a consequence of the static full
higher-codegree table.

There are also three precise corrections to the proposed cutoff audit.

1. A level-\(B\) initializer for base excess \(s\) requires
   \(2(s+B)\le L_{\rm pm}\), not \(s+B\le L_{\rm pm}\).
2. The tail parameter must include all \(O(p^2)\) protected arm pairs.
   A bound for one prescribed pair cannot be inserted without this
   multiplicity.
3. The claimed stopped one-row path-mesh input in the later additive
   closure note is not proved elsewhere.  Applying static row
   exploration to a current endogenous residual is the missing dynamic
   assertion itself.

The residual in (0.6) is an obstruction to this proof mechanism, not a
macroscopic matching obstruction: its common edges themselves form a
large matching.  Hence the ordinary-frame near-resolution remains open.

## 1. The finite-cutoff lemma

The following abstract statement isolates exactly what a pointwise
common-event estimate would buy.

### Lemma 1.1 (finite backward tower)

Let \(F_0,\ldots,F_B\) be nonnegative stopped observables on a time
interval \([t_0,t_1]\).  After including the exact moving-base
integrating factor, suppose

\[
 (\partial_t+\mathcal L_t)F_j\le \kappa(t)F_{j+1}
       \quad(0\le j<B),                                  \tag{1.1}
\]

and

\[
 (\partial_t+\mathcal L_t)F_B\le q(t)F_B.                \tag{1.2}
\]

Put

\[
 A(t)=\int_t^{t_1}\kappa(u)\,du,
 \qquad
 Q=\int_{t_0}^{t_1}q(u)\,du.                             \tag{1.3}
\]

Then there is a nonnegative stopped supermartingale

\[
 \Phi(t)=\sum_{j=0}^{B-1}{A(t)^j\over j!}F_j(t)
          +c_B(t)F_B(t),                                  \tag{1.4}
\]

where

\[
 c_B(t)=\int_t^{t_1}
  \kappa(u){A(u)^{B-1}\over(B-1)!}
  \exp\!\left(\int_t^u q(v)\,dv\right)du,               \tag{1.5}
\]

and

\[
                         c_B(t)\le e^Q{A(t)^B\over B!}.   \tag{1.6}
\]

If, at \(t_0\),

\[
                         \mathbb EF_j(t_0)
             \le C\alpha^{s+j}\quad(0\le j\le B),       \tag{1.7}
\]

then

\[
 \mathbb E\Phi(t_0)
 \le C\alpha^s\left[
       \sum_{j=0}^{B-1}{(A(t_0)\alpha)^j\over j!}
       +e^Q{(A(t_0)\alpha)^B\over B!}\right].            \tag{1.8}
\]

#### Proof

For \(j<B\), differentiation of \(A^j/j!\) cancels the term
\(\kappa A^{j-1}F_j/(j-1)!\) coming from (1.1) at the previous level.
Differentiating (1.5) gives

\[
 c_B'(t)=-\kappa(t){A(t)^{B-1}\over(B-1)!}-q(t)c_B(t).
\]

This cancels both the incoming level-\(B-1\) term and (1.2).  Hence
\((\partial_t+\mathcal L_t)\Phi\le0\).  Removing the exponential from
the integrand of (1.5) at cost \(e^Q\), followed by
\(dA=-\kappa\,dt\), proves (1.6).  Finally insert (1.7) into (1.4) and
use (1.6). \(\square\)

The exact numerical criterion is

\[
 Q+B\log(A\alpha)-\log(B!)\longrightarrow-\infty.        \tag{1.9}
\]

In the present problem, \(A=O(m\log m)\) and (0.1) gives

\[
 \log(A\alpha)=-(9/10+o(1))\log m.                        \tag{1.10}
\]

Thus any \(Q=o(B\log m)\) suffices.

## 2. What the required pointwise bound actually is

For two displayed, fully equality-resolved physical arms \(a,b\), let

\[
 \beta_t(a,b)=\nu_t
 |\{g:g\cap a\ne\varnothing,\ g\cap b\ne\varnothing\}|,
 \qquad \nu_t={1\over r\Delta_t}.                         \tag{2.1}
\]

All already shared physical resources are counted once in the union
reference.  Therefore a compensation clock on such a resource produces
no positive cross term.  If one works before complete equality
resolution, its common-coin mass must be added to (2.1); it cannot be
discarded by sign.

Suppose a cutoff state has \(p\) marginally counted nonprivate arms and

\[
                         \beta_t(a,b)\le\beta_m(t)         \tag{2.2}
\]

for every pair.  If a future event hits \(t_g\) arms, its exact union
defect is \((t_g-1)_+\).  The pair-column domination

\[
                         (t_g-1)_+\le\binom{t_g}{2}         \tag{2.3}
\]

therefore gives

\[
                         q(t)\le\binom p2\beta_m(t).       \tag{2.4}
\]

Core compression gives \(p=O(s+B)\).  Equations (2.4) and
\(T=O(m\log m)\) prove (0.3) under (0.2).

The full multiplicity in (2.4) matters.  If one knows only current pair
spread

\[
                         d_t(x,y)\le\delta_t\Delta_t,       \tag{2.5}
\]

then two arms of size at most \(r\) satisfy only

\[
 \beta_t(a,b)
 \le {r^2\delta_t\Delta_t\over r\Delta_t}
 =r\delta_t.                                               \tag{2.6}
\]

At the sharp static pair scale \(\delta_t=\Theta(m^{-2})\), (2.6) is
only \(\Theta(m^{-1})\).  With \(p,B=\Theta((\log m)^2)\), its
integrated top rate is

\[
 Q=O(Tp^2/m)=O((\log m)^5),                                \tag{2.7}
\]

whereas the available static cutoff credit is only
\(\Theta(B\log m)=\Theta((\log m)^3)\).  Thus pair codegree, even if
preserved pointwise, is not the requested sharp common-event input.

The correct time-zero statistic is stronger.  The proved ordinary/
repaired promotion-frame influence estimate says that, for an owner
\(X\) and a frame \(e\) not containing it,

\[
 |\{g:X\in g,\ g\cap e\ne\varnothing\}|
 \le {20+o(1)\over m^2}d(X).                               \tag{2.8}
\]

Summing (2.8), with \(e\) equal to the second arm, over the at most
\(r\) owner resources of the first arm and dividing by \(r\Delta\)
gives

\[
                         \beta_0(a,b)\le{20+o(1)\over m^2} \tag{2.9}
\]

on the degree-regular initial catalogue.  This is exactly strong enough
for (0.3).  Its dynamic analogue is the whole-arm common-event condition

\[
 \boxed{
 \beta_t(a,b)\le {(\log m)^{O(1)}\over m^2u(t)^2}
 \quad\hbox{outside aggregate owner/root incidence }o(E_t).}
                                                               \tag{HCE}
\]

HCE is an aggregate/trajectory regeneration assertion.  The complete
static higher-codegree table does not make it hereditary.

The top resource in an arm does not alter (2.9).  A fixed compatible
top--owner incidence has normalized codegree
\(\binom mH^{-1}\), and summing over the \(M\) owners of the other arm
is \(m^{-\omega(1)}\) in the Gaussian regime.  Two distinct top
resources have codegree zero.

## 3. Exact higher-codegree lemma for a distance-one pair

The residual obstruction below uses the following elementary fact.

### Lemma 3.1 (third-resource diffusion in a distance-one link)

Let \(X,Y\) be owners at Johnson distance one, and let
\(D_1=d_{\mathcal H}(X,Y)\).  For every owner or top vertex
\(v\notin\{X,Y\}\),

\[
 d_{\mathcal H}(X,Y,v)
 \le {20\over(m-1)^2}D_1                                  \tag{3.1}
\]

for all sufficiently large \(m\) and \(H\ge3\).

#### Proof

For owners at Johnson distance \(d<H\), the exact pair codegree is

\[
 D_d={2(d!)^2(m-d)!^2\over(m-H)!}.                         \tag{3.2}
\]

Hence

\[
                         {D_2\over D_1}={4\over(m-1)^2}.    \tag{3.3}
\]

The sequence decreases for \(2\le d<H\).  The disjoint-interval
boundary \(d=H\) has codegree

\[
                         H!^2(m-H+1)!,                      \tag{3.4}
\]

whose ratio to \(D_1\) is at most \(20/(m-1)^2\) for
\(H\ge3\) and all sufficiently large \(m\).
Indeed, if this ratio is denoted by \(R_H\), then

\[
 {R_{H+1}\over R_H}
 ={(H+1)^2\over(m-H+1)(m-H)}=o(1)
\]

uniformly in the present Gaussian range.  At \(H=3\),
\(R_3=18/[(m-1)^2(m-2)]\), proving the stated bound for every
\(H\ge3\).

It remains to rule out a third owner \(Z\) with all three pairwise
distances one.  A triangle in a Johnson graph is either three
\(m\)-sets with a common \((m-1)\)-subset or three \(m\)-subsets of a
common \((m+1)\)-set.  In either case, inside a common top their
three complementary \(H\)-sets would be three distinct cyclic
\(H\)-intervals pairwise at Johnson distance one.  Two such intervals
have starts differing by \(1\) or \(-1\).  Three distinct starts cannot
be pairwise separated by one on a cycle of length \(M>3\).  Thus the
triple codegree is zero in this case.  Otherwise one of
\(d(X,Z),d(Y,Z)\) is at least two, and the triple codegree is at most
the corresponding pair codegree, so (3.2)--(3.4) prove (3.1).

For a top vertex \(U\), all common tops of \(X,Y\) contribute equally,
and their number is \(\binom{m-1}{H-1}\).  Thus fixing \(U\) costs the
factor \(\binom{m-1}{H-1}^{-1}\le20/(m-1)^2\). \(\square\)

## 4. A literal \(\Theta(1)\) pair-star residual

### Theorem 4.1 (ordinary-frame pair-star)

For some absolute \(c>0\) and all sufficiently large \(m\), there is
an edge-deletion subhypergraph \(\mathcal R\subseteq\mathcal H_{m,H}\)
and two edges \(f,f'\in\mathcal R\) such that

\[
                         \Delta(\mathcal R)=2               \tag{4.1}
\]

and at least \(\lfloor cm\rfloor\) other edges of \(\mathcal R\)
meet both \(f\) and \(f'\).  Consequently

\[
 \beta_{\mathcal R}(f,f')
 :={|\{g\in\mathcal R:g\cap f\ne\varnothing,
                         g\cap f'\ne\varnothing\}|\over
       r\Delta(\mathcal R)}
 \ge {c+o(1)\over2}.                                      \tag{4.2}
\]

#### Proof

Choose a set \(C\) of size \(M-1\) and two labels
\(a,b\notin C\).  Put

\[
                         U=C\cup\{a\},\qquad
                         U'=C\cup\{b\}.                    \tag{4.3}
\]

Take a cyclic order on \(U\), and obtain the order on \(U'\) by
replacing \(a\) by \(b\) in the same position.  Let \(f,f'\) be the
two complete frame edges.  Exactly \(m\) cyclic \(m\)-windows contain
that position.  Pairing corresponding windows gives distinct owners

\[
                         (Y_i,Z_i),\qquad1\le i\le m,        \tag{4.4}
\]

with \(d_J(Y_i,Z_i)=1\).  The remaining \(H=M-m\) windows avoid the
special position and are shared physical owners of \(f,f'\).  Notice
that using two tops differing in one label, rather than a transposition
inside one fixed top, is essential: an internal transposition changes
only \(O(H)\), not \(\Theta(m)\), of these nearly-full windows.

We greedily choose \(\ell=\lfloor cm\rfloor\) frames \(g_i\), where
\(g_i\) contains \(Y_i,Z_i\).  When \(g_i\) is chosen, forbid

1. every vertex of \(f\cup f'\) other than \(Y_i,Z_i\);
2. every vertex used by a previous \(g_j\); and
3. every designated endpoint \(Y_j,Z_j\) with \(j\ne i\).

At step \(i\), the forbidden set has size at most

\[
 (i-1)r+2r+2\ell\le (2c+o(1))m^2.                         \tag{4.5}
\]

The link of \(Y_i,Z_i\) has size \(D_1\).  By Lemma 3.1, each
forbidden vertex lies in at most \(20D_1/(m-1)^2\) members of that
link.  The union bound therefore deletes at most

\[
                         (40c+o(1))D_1.                     \tag{4.6}
\]

Choose, for example, \(c=1/100\).  Then (4.6) is smaller than
\(D_1\), so a permissible \(g_i\) exists at every step.

The frames \(g_i\) are pairwise vertex-disjoint.  Each meets \(f\)
only in \(Y_i\) and \(f'\) only in \(Z_i\).  No \(g_i\) contains an
endpoint assigned to another channel.  In the subhypergraph with edge
set

\[
                         \{f,f',g_1,\ldots,g_\ell\},         \tag{4.7}
\]

every vertex consequently has degree at most two, and the \(H\) common
owners of \(f,f'\) have degree exactly two.  This proves (4.1).  All
\(g_i\) are common events for \(f,f'\), so (4.2) follows. \(\square\)

The construction uses actual ordinary frames and only deletes edges.
It does not assert that the compensated random-greedy trajectory enters
this state with appreciable probability.  Its exact force is that HCE
cannot be deduced from static codegrees plus the statement
\(\mathcal H_t\subseteq\mathcal H_0\).

## 5. Audit of the two proposed repairs

### 5.1 The ordered tower

The formal infinite cancellation is correct, but the original tower
omits positive normalized hazards involving a protected prefix column,
an earlier selected-edge column, or an unresolved common compensation
resource.  A corrected tower must include those states before Lemma 1.1
can be applied.

For a core of excess \(s+j\), private-column elimination leaves at most
\(2(s+j)\) witness incidences.  The static row-exploration theorem is
certified only when

\[
                         2(s+j)\le L_{\rm pm}.               \tag{5.1}
\]

Thus a cutoff at \(B\) requires \(2(s+B)\le L_{\rm pm}\).  The stated
one-row input through order \(2L+2\) allows only \(B\le1\) for a base
type of excess \(s=L\); it does not initialize a
\(B=\Theta((\log m)^2)\) tail.  One would have to certify the local
endpoint theorem through \(2(L+B)\) with separate constant room.

Even after doing so, a prescribed-pair estimate must be multiplied by
the number of protected arm pairs as in (2.4).  Equations (0.2)--(0.5)
show that the sharp whole-arm scale is sufficient.  Formula (2.6) shows
that maximum pair codegree alone is not.

### 5.2 The additive one-child note

The claimed inequality

\[
 {\nu_t\,\mathsf X_{\tau}(t)\over Y_\tau(t)}
 \le (\log m)^{O(1)}\alpha^{\rho+1}                         \tag{5.2}
\]

is conditional on a stopped current one-row path-mesh maximum through
order \(2L+2\).  No independent theorem in the current file set proves
that stopped dynamic input; the only occurrences state it as an
assumption.

Static row exploration counts the full catalogue at time zero.  It
cannot be reapplied with \(D_t,\Delta_t\) to an endogenous residual.
Stopping a parent row variable below its envelope does not control its
common-event child: Theorem 4.1 has bounded degrees and a common-event
fraction bounded below by a constant.  Thus the assertion that the
one-row estimate is deterministic before its crossing is false.

The proposed bootstrap is circular.  The top-strip affine estimate uses
the stopped one-row child bound, while the claimed proof of the stopped
one-row bound invokes the graded/top-strip hierarchy to charge its
crossing.  A finite cutoff plus HCE would break this circle; the current
static inputs do not.

## 6. Exact remaining statement

The finite-cutoff algebra, the static initialization in its certified
range, and the time-zero whole-arm influence are all valid.  They reduce
the owner near-resolution route to the following trajectory statement:

> Along the compensated ordinary-frame process down to
> \(z=m^{-1/20}\), outside aggregate owner/root incidence \(o(E_t)\),
> every pair of displayed arms in every corrected cutoff state has
> common edge-clock mass
> \(m^{-2}u(t)^{-2}(\log m)^{O(1)}\), with complete physical equality
> resolution.

This HCE statement implies the finite tower by Sections 1--2 and hence
the advertised top-strip first-moment control.  Theorem 4.1 proves that
HCE is not deletion-hereditary.  Its aggregate trajectory version is a
specialized form of ADLE/ACLE and remains unproved.

No near-perfect matching, no macroscopic odd-set obstruction, and no
coefficient-one theorem follows from the present audit.
