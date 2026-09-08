# Lane H: a vanishing critical-scale zero-winding sector

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
web search is used.

## 0. Result

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,
 \qquad H_A=\lceil A\sqrt r\rceil .
\]

For a genuine first zero-winding quotient return, let \(h\) be its
duration, equivalently its Dyck height.  Write

\[
 D^{(j)}=\partial^jD,\qquad
 r_j=|D^{(j)}|/2,
\]

and let

\[
 \ell=\min\{j:r_j=h-j\},\qquad q=h-\ell .
\]

Thus \(D^{(\ell)}=1^q0^q\) is the first mountain in the pruning tower.

### Theorem 0.1 (saturated Gaussian top segment)

Fix \(A>0\) and \(\varepsilon>0\).  The number of genuine first
zero-winding starts satisfying

\[
 h\le A\sqrt r,\qquad q\ge\varepsilon\sqrt r,
 \qquad \ell\ge2q                                      \tag{0.1}
\]

is

\[
 \boxed{o_{A,\varepsilon}(B_r/\sqrt r).}              \tag{0.2}
\]

Consequently every quotient-edge-disjoint packing restricted to this
sector also has size \(o_{A,\varepsilon}(B_r/\sqrt r)\).

This is at the corrected coefficient-one scale.  It is a start-count
theorem, hence is stronger than the needed packing assertion on this
sector.  It uses only actual zero-winding returns and the audited wrapped
Pascal fan; it never uses the false converse from \(d(D)=1\).

There is also a chronology-free small-height deletion:

### Theorem 0.2 (sub-Gaussian height sector)

If \(\overline\nu_{\le a\sqrt r}\) denotes the quotient packing of all
returns whose Dyck height is at most \(a\sqrt r\), then

\[
 \boxed{
 \lim_{a\downarrow0}\limsup_{r\to\infty}
 {\sqrt r\over B_r}\overline\nu_{\le a\sqrt r}=0.}    \tag{0.3}
\]

The residual zero-winding sector has Gaussian height, but either
\(q=o(\sqrt r)\) or \(\ell<2q\).  It includes the bounded-\(q\)
complete-persistent boundary.  The exact obstacle there is transported
phase saturation, stated in Section 4.

## 1. The two exact fibre factors

Fix a complete pruning-rank profile

\[
 \mathbf r=(r_0,r_1,\ldots,r_{\ell+1})
\]

ending at the mountain \(1^q0^q\).  The unrestricted number of inverse
towers over this fixed bottom root is

\[
 \mathcal F(\mathbf r)
 =\prod_{j=1}^{\ell}
   \binom{r_{j-1}+r_{j+1}}{2r_j}.                 \tag{1.1}
\]

Indeed, at level \(j\) the free mass

\[
 y_j=r_{j-1}-2r_j+r_{j+1}\ge0
\]

is distributed among \(2r_j+1\) cyclic child slots.

For an actual zero-winding return, the wrapped Pascal fan fixes

\[
 t_j=\min\{j,2r_j\}
\]

independent degrees at inverse level \(j\).  Conditional multiplication
therefore bounds the compatible fraction by

\[
 \widehat Q_\ell(\mathbf r)
 =\prod_{j=1}^{\ell}
 \frac{\binom{r_{j-1}+r_{j+1}-t_j}{2r_j-t_j}}
      {\binom{r_{j-1}+r_{j+1}}{2r_j}}.            \tag{1.2}
\]

We use two disjoint groups of factors in (1.2).

First fix an integer \(K\).  Call the initial profile \(K\)-good when

\[
 r_j={r\over j+1}(1+\theta_j),\qquad
 |\theta_j|\le K^{-4}\quad(0\le j\le K+1).        \tag{1.3}
\]

For fixed \(K\), all but \(o_K(B_r)\) Dyck roots are \(K\)-good.  This
is the audited fixed-depth harmonic concentration theorem.  Moreover, for
all sufficiently large fixed \(K\), the first \(K\) fan factors of a
good profile satisfy

\[
 \prod_{j=1}^{K}
 \frac{\binom{r_{j-1}+r_{j+1}-j}{2r_j-j}}
      {\binom{r_{j-1}+r_{j+1}}{2r_j}}
 \le {2e\over K+1}.                               \tag{1.4}
\]

Second, assume \(\ell\ge2q\).  At the first mountain,

\[
 r_\ell=q,\qquad r_{\ell+1}=q-1.
\]

Minimality of \(\ell\) gives

\[
 r_{\ell-1}\ge q+2,
\]

and consequently

\[
 y_\ell=r_{\ell-1}-2q+(q-1)\ge1.                 \tag{1.5}
\]

Because \(t_\ell=2q\), all independent degrees of the final weak
composition are fixed.  Its factor in (1.2) is therefore at most

\[
 {1\over\binom{2q+y_\ell}{2q}}
 \le {1\over2q+1}.                                \tag{1.6}
\]

When (0.1) holds and \(K\) is fixed, \(\ell>K\) for all sufficiently
large \(r\).  Thus (1.4) and (1.6) are distinct conditional factors and
may be multiplied.

## 2. Proof of Theorem 0.1

Fix \(K\), and first sum over the \(K\)-good profiles satisfying (0.1).
For each profile, (1.4), (1.6), and the fact that all omitted factors in
(1.2) are at most one give

\[
 \#\{\hbox{compatible towers over }\mathbf r\}
 \le {2e\over(K+1)(2q+1)}\,\mathcal F(\mathbf r)
 \le {e\over\varepsilon(K+1)\sqrt r}
       \mathcal F(\mathbf r).                     \tag{2.1}
\]

There is no multiplicity in this sum.  Every Dyck root has one pruning
profile, one first mountain depth, and one rooted bottom mountain.
Conversely (1.1) is the exact unrestricted tower capacity for the fixed
profile and bottom.  Hence the unrestricted capacities over any selected
set of profiles sum to at most \(B_r\).  Equation (2.1) yields

\[
 Z^{\rm good}_{r,A,\varepsilon}
 \le {e\over\varepsilon(K+1)}{B_r\over\sqrt r}.   \tag{2.2}
\]

For the bad profiles use only the final factor (1.6).  If

\[
 \eta_{r,K}B_r
\]

is the total unrestricted capacity of the bad initial profiles, fixed-
depth concentration says \(\eta_{r,K}\to0\) as \(r\to\infty\), for each
fixed \(K\).  Therefore

\[
 Z^{\rm bad}_{r,A,\varepsilon}
 \le {\eta_{r,K}B_r\over2\varepsilon\sqrt r}.     \tag{2.3}
\]

Combining (2.2)--(2.3) gives

\[
 \limsup_{r\to\infty}
 {\sqrt r\over B_r}Z_{r,A,\varepsilon}
 \le {e\over\varepsilon(K+1)}.                   \tag{2.4}
\]

Now let the fixed integer \(K\to\infty\).  This proves (0.2).

The order of quantifiers is essential: \(A,\varepsilon,K\) are fixed
before \(r\to\infty\), and only after that limsup is taken is
\(K\to\infty\).  No concentration estimate uniform at a growing pruning
depth is used.

## 3. Proof of Theorem 0.2

Let \(b_{r,h}\) be the number of Dyck roots of exact height \(h\), and
let \(F_r(t)=\sum_{h\le t}b_{r,h}\).  The height-gap theorem and
edge-disjointness give

\[
 \overline\nu_{\le a\sqrt r}
 \le\sum_{h\le a\sqrt r}{b_{r,h}\over h+2}.       \tag{3.1}
\]

The path-graph estimate is

\[
 F_r(t)\le
 C B_r\left({\sqrt r\over t+2}\right)^3
 \exp\!\left(-c{r\over(t+2)^2}\right)            \tag{3.2}
\]

for \(t\le\sqrt r\).  Summation by parts in (3.1), followed by the
change of scale \(x=(t+2)/\sqrt r\), gives

\[
 \sum_{h\le a\sqrt r}{b_{r,h}\over h+2}
 \le {CB_r\over\sqrt r}\rho(a),                  \tag{3.3}
\]

where, for suitable absolute \(c,C>0\), one may take

\[
 \rho(a)=C\left(
 a^{-4}e^{-c/a^2}
 +\int_0^a x^{-5}e^{-c/x^2}\,dx\right).           \tag{3.4}
\]

The function \(\rho(a)\) tends to zero as \(a\downarrow0\).  Equations
(3.1)--(3.4) prove (0.3).

## 4. Exact surviving obstruction

It is tempting to multiply the fan fraction by trace length for every
zero-winding return.  The capacitated projection theorem shows precisely
why that is not automatic.

Over a fixed reduced edge \(e\), a parent edge is the pair consisting of
\(e\) and one inverse-tower slot vector.  For a fixed start phase the fan
selects a cylinder of relative size at most \(Q\).  At trace offset
\(t\), however, PBBS transport sends it to a generally different cylinder
over the current reduced edge.  Edge-disjointness says that the transported
slot vectors are distinct, but the presently proved bounds give only

\[
 L_e\le
 \min\left\{\mathcal F_e,
             \sum_{t=0}^{h}Q_t\mathcal F_e\right\}. \tag{4.1}
\]

On the critical harmonic profiles, \(Q_t=\Theta(1/h)\) and there are
\(\Theta(h)\) offsets.  Thus (4.1) permits \(L_e=\Theta(\mathcal F_e)\):
the fan factor and reciprocal-height factor cancel exactly.  Replacing
the right side by \(o(\mathcal F_e)\) requires a theorem about overlap or
noncoverage of the **genuinely transported** cylinders.  It does not
follow from their one-phase cardinalities.

The smallest residual zero-winding lemma at the corrected scale can
therefore be stated as follows.

> **Bounded-top translated-fan non-saturation -- UNPROVED.**  In the
> residual Gaussian sector \(q=o(\sqrt r)\) (in particular bounded
> \(q\), including the complete-persistent boundary), the aggregate load
> of the actual transported fan cylinders over every reduced edge is
> \(o(\mathcal F_e)\), after summing with the exact inverse-Pascal
> capacities.

Such a statement, combined with the universal projected-edge volume,
would give \(o(B_r/\sqrt r)\).  A one-parent, one-phase, or isolated-reset
argument cannot replace it.

## 5. Adversarial audit

1. Every fan factor is conditioned on a genuine zero-winding return.
   Neither \(d(D)=1\) nor a primitive root is treated as a converse.
2. The factor \((2q+1)^{-1}\) is used only when \(\ell\ge2q\), exactly
   the wrapped saturation condition.
3. The first \(K\) and final factors are distinct because
   \(q\ge\varepsilon\sqrt r\) and \(\ell\ge2q\), while \(K\) is fixed.
4. Bad profiles are not discarded at density \(o(1)\) alone.  They still
   receive the final \(O(r^{-1/2})\) saturated factor, which is why their
   contribution is \(o(B_r/\sqrt r)\).
5. The proof bounds starts.  Passing to an edge-disjoint packing only
   decreases cardinality.
6. Theorem 0.2 uses only the height-gap theorem and exact edge volume, so
   it applies to every winding sector.
7. Equation (4.1) is a proof-method ceiling, not a constructed PBBS
   saturation family.  No counterexample to the corrected packing gate is
   claimed.

