# Independent cross-audit of the long-component MTF construction

Date: 2026-07-25

Audited sources:

* `LONG_COMPONENT_MTF_CONSTRUCTION_20260725.md`;
* `LONG_COMPONENT_MTF_CONSTRUCTION_SELF_AUDIT_20260725.md`;
* the already-audited quantitative strip-matching and canonical-MTF results
  imported by those notes.

## Verdict

**PASS AFTER LOCAL PATCHES.**

The projected-strip construction is mathematically valid.  It gives, for

\[
 H\to\infty,
 \qquad
 H=o(\log m/\log\log m),
\]

a literal word of length \(W+o(W)\) covering ranks \(m\) and \(m+H\),
with the selected states lying on \(o(W/H)\) residual-consuming components
of length \(\omega(H)\).  The symmetric three-rank statement and the
sparse-row interpolation are also valid.  The fixed-kernel translation
tiling obstruction is valid in its now-explicit global-owner scope.

No claim here proves a Gaussian window or simultaneous distinct support at
all intermediate depths.

I made the following fully justified patches during the audit.

1. In the proof-method ceiling, the source had silently replaced \(D_0\)
   by \((1-o(1))D\).  I inserted the missing implication: applicability of
   the quoted matching theorem makes its permitted relative degree error
   \(o(1)\), and its near-regularity hypothesis therefore forces
   \(D_0=(1-o(1))D\).
2. The global clause of Theorem 9.1 now explicitly assumes that the
   fixed-kernel product extensions contain \(W-o(W)\) middle owners.  This
   is exactly what is needed to sum the local support bound, and it holds in
   the cited prescribed-scale outer construction.
3. I corrected several harmless TeX transcription errors, including the
   missing `\left\lfloor` in Theorem 4.4 and the missing `\qquad` in the
   three-rank display.
4. At the lead agent's request I inserted and independently checked the two
   product-box consequences, Theorems 7.1 and 7.2.  Their proofs are
   recorded and audited in Section 8 below.

## 1. Projected strip simplicity

For a strip, the middle row is

\[
 \{C\cup I_\gamma(i,\ell):i\in\mathbb Z_{2\ell}\}.
\]

Its total intersection is \(C\), and its total union is \(C\cup R\).
Thus it recovers both ordered cores \(C\) and
\(D=[2m]\setminus(C\cup R)\).  Two row members are Johnson-adjacent
exactly when their cyclic starts differ by one.  Hence the induced Johnson
graph is the cycle \(C_{2\ell}\).  Following the successive one-element
differences recovers the coordinate cycle on \(R\), up to rotation and
reversal, precisely the equivalence already built into an undirected cyclic
order.  Therefore the middle row alone recovers the strip, and projection
onto any collection of rows containing the middle row creates no parallel
hyperedges.

This remains true for the two-row, three-row, and general sparse-row
projections.

## 2. Exact edge and degree counts

The number of strips is

\[
 \binom{2m}{m-\ell}
 \binom{m+\ell}{m-\ell}
 \frac{(2\ell-1)!}{2}
 =\frac{(2m)!}{4\ell(m-\ell)!^2}.
\]

Every selected rank contributes \(2\ell\) distinct row masks.  Incidence
double counting in rank \(m+d\) gives

\[
 D_d
 =\frac{(m+d)!(m-d)!}{2(m-\ell)!^2}.
\]

The maximum over \(|d|\le H\) is \(D_H=D_{-H}\), and the minimum is
\(D_0\).  Moreover

\[
 \frac{D_H}{D_0}
 =\frac{(m+H)!(m-H)!}{m!^2}
 \le \exp\!\left(\frac{H^2}{m-H}\right),
\]

and for \(\ell=o(m)\),

\[
 \log D_H=(2+o(1))\ell\log m.
\]

All factors of two in the source are correct.

## 3. Orbit codegree bound

Fix a first vertex \(X\).  Under its coordinate stabilizer, the orbit of a
second mask \(Y\) has size

\[
 \binom{|X|}{|X\setminus Y|}
 \binom{2m-|X|}{|Y\setminus X|}.
\]

For the selected ranks, every orbit of size greater than one has size at
least \(m-H\).  The only additional orbit-one candidate is the complement
of a middle mask.  It has codegree zero, because every two masks in one
strip contain the nonempty core \(C\).

One edge through \(X\) contains at most \(2\ell\) masks in the rank of
\(Y\).  Stabilizer double counting therefore gives

\[
 \deg(X,Y)\le\frac{2\ell\deg(X)}{m-H}
 \le\frac{2\ell D_H}{m-H}.
\]

This proves the quoted uniform codegree bound for every sparse-row
projection, including cross-rank pairs.

## 4. Quantitative near-regular matching theorem

The imported result is exactly the growing-uniformity matching form already
audited in `RAINBOW_MULTIDEPTH_STRIP_MATCHING_AUDIT_20260724.md`: for a
simple \(K\)-uniform hypergraph with maximum degree \(D\), codegree
parameter \(C\), and minimum degree at least

\[
 D-20(D^2C\log D)^{1/3},
\]

its leave is

\[
 O\!\left(
 K\left(\frac{C\log(1+C)}D\right)^{1/(K-1)}|V|
 \right)
\]

under the displayed hypotheses.  Thus the source does not use a
fixed-uniformity theorem outside its scope.

For the two-row choice

\[
 \ell=\left\lfloor\frac{\log m}
 {32\log\log m}\right\rfloor,
 \qquad K=4\ell,
\]

take

\[
 C_*=\left\lceil\frac{2\ell D}{m-H}\right\rceil.
\]

Since \(D\) is superpolynomial, the ceiling is negligible, and

\[
 \eta:=\frac{C_*\log(1+C_*)}{D}
 =O\!\left(\frac{\ell^2\log m}{m}\right),
 \qquad
 \log\eta=-\log m+O(\log\log m).
\]

As

\[
 K=(1+o(1))\frac{\log m}{8\log\log m},
\]

we obtain

\[
 \eta^{1/(K-1)}=(\log m)^{-8+o(1)}.
\]

The degree spread \(O(H^2/m)\) is smaller than
\((C_*\log D/D)^{1/3}\).  Also \(K=o(\log D)\),
\(K>4\), the permitted error is \(o(D)\), and

\[
 \log\!\left(e^{2K}\frac{C_*\log D}{D}\right)
 =-\log m+\frac{\log m}{4\log\log m}
  +O(\log\log m)\to-\infty.
\]

Hence every required hypothesis holds.  Multiplication by
\(K|V|=O(KW)\) gives the claimed leave

\[
 U\le W(\log m)^{-7+o(1)}=o(W).
\]

## 5. Matching and support ledgers

If the matching contains \(p\) strips, then

\[
 u_0=W-2\ell p,
 \qquad
 u_H^+=N_H-2\ell p,
 \qquad
 u_0+u_H^+=U=o(W).
\]

Thus

\[
 2\ell p=W-o(W)=N_H-o(W),
 \qquad
 p=(1-o(1))\frac W{2\ell}.
\]

Because the upper row is a vertex part of the matching, this is a
distinct-support statement, not merely an occurrence count.

The same calculation works for the three-row and sparse-row projections.
For a selected depth set \(\mathcal D_m\) of size \(r\), choosing

\[
 \ell=\left\lfloor
 \frac{\log m}{16r\log\log m}\right\rfloor
\]

makes \(K=2\ell r=(1+o(1))\log m/(8\log\log m)\).  The condition

\[
 \frac{rH\log\log m}{\log m}\to0
\]

gives \(H/\ell\to0\), admissible degree spread, and
\(r=o(\log m/\log\log m)\).  Since
\(|V|\le rW\), the leave is

\[
 O(r(\log m)^{-7+o(1)}W)=o(W).
\]

This verifies Theorem 4.4 and both endpoint specializations stated after
it.

## 6. Virtual cyclic MTF closure and residual consumption

The cut cycle has transitions

\[
 p_i=z_i,
 \qquad q_i=z_{i+\ell}=p_{i+\ell}.
\]

Thus an arriving active coordinate cannot delete one of the preceding
\(H\) departure markers when \(H<\ell\).  With the initial queue

\[
 (\{z_{2\ell-1}\},\ldots,\{z_{2\ell-H}\},R_0),
\]

the first \(H\) markers at state \(i\) are exactly

\[
 z_{i-1},z_{i-2},\ldots,z_{i-H}.
\]

Their union with \(T_i\) is

\[
 C\cup I_\gamma(i-H,\ell+H),
\]

including at the left boundary.  The audited terminal dummy list similarly
supplies the lower cyclic flags at the right boundary.  Therefore cutting
loses no selected cyclic row mask.  Every positive coordinate run has
length \(\ell>H\), so the canonical trajectory is legal.

The active part of

\[
 R_0=D\cup\{z_\ell,\ldots,z_{2\ell-H-1}\}
\]

has size \(\ell-H\), and every one of those coordinates arrives before the
terminal state.  No coordinate of \(D\) arrives.  Hence the terminal
residual is exactly \(D\), of size \(m-\ell<m-H\).  Every selected
component is genuinely residual-consuming.

## 7. Portal and literal-word accounting

One path has \(2\ell\) middle states and canonical word length

\[
 2\ell+2H+1.
\]

Independent exact initialization of \(p\) paths therefore has portal excess
\((2H+1)p\).  Since \(H/\ell\to0\),

\[
 (2H+1)p=o(W),
 \qquad
 p=o(W/H),
 \qquad
 2\ell/H\to\infty.
\]

Appending the unmatched middle and upper masks gives exact length

\[
 p(2\ell+2H+1)+u_0+u_H^+
 =W+(2H+1)p+u_H^+
 =W+o(W).
\]

All initialization blocks and appended masks are nonempty.  The canonical
MTF theorem supplies the literal suffix-OR certificates.  The symmetric
three-rank and sparse-row versions have the same baseline/repair ledger:
the middle row plus its unmatched literals costs exactly \(W\), while the
portal term and the total leave are \(o(W)\).

The depletion lower bound \(2Hp+1\) differs from the independent-reset
upper bound \((2H+1)p\) by relative \(O(1/H)\), so the note does not hide
an unproved cheap-bridge assumption.

## 8. Product-box consequences

Theorem 7.1 is valid.  In one saturated radius-\(H\) flag, there are
\(2H+1-g\) pairs at rank distance \(g\).  Under one uniform common
coordinate relabeling, the higher member of such a nested pair is uniform
among at least \(\binom{m-H}{g}\) extensions of the lower member.  A
three-chain product box contains at most \(\binom{g+2}{2}\) such
extensions.  Therefore the expected collision-pair count per endpoint is

\[
 \sum_{g=1}^{2H}(2H+1-g)
 \frac{\binom{g+2}{2}}{\binom{m-H}{g}}
 =O(H/m).
\]

There are at most \(W\) selected endpoints, so one common relabeling has
aggregate collision-pair count \(O(HW/m)=o(W)\).  Every non-box-rainbow
flag contributes a collision pair, proving the stated exceptional-endpoint
bound.  One relabeling preserves both the matching and the MTF trajectory.

The stronger dominant-family Theorem 7.2 is also valid in its stated
\(2m=3s\) scope.  Each dominant product box has plateau half-width at least
\(0.4\sqrt s\), at least \(s\) masks in every plateau layer, and the number
of such boxes is
\((\kappa_L^2\kappa_H+o(1))W_s^3\).  Since
\(sW_s^3/W\) tends to a positive constant, every rank
\(m+d\), \(|d|\le H=o(\sqrt m)\), contains \(\Omega(W)\) masks of the
fixed target family.

Consequently a random common relabeling sends \(\Omega(HW)\) endpoint-mask
occurrences into that family in expectation.  The variable is bounded by
\(O(HW)\), so it exceeds a fixed positive fraction of this scale with
fixed positive probability.  Markov's inequality for the collision count
has a compatible positive-probability event.  One relabeling therefore has
\(\Omega(HW)\) target occurrences and \(O(HW/m)\) collisions.  Replacing
repeated occurrences in one endpoint/box by one incidence loses at most
the number of collision pairs, leaving \(\Omega(HW)\) distinct
endpoint--target-box incidences.  Since every endpoint has degree
\(O(H)\), \(\Omega(W)\) endpoints have degree \(\Omega(H)\).

This is aggregate incidence, not a simultaneous globally distinct-target
resolution at the intermediate ranks.

## 9. Proof-method ceiling

For a fixed middle mask, every containing strip supplies its two cyclic
Johnson neighbours.  Stabilizer transitivity on the \(m^2\) such neighbours
gives the exact adjacent-pair codegree

\[
 \frac{2D_0}{m^2}.
\]

As patched in the source, applicability of the matching theorem forces
\(D_0=(1-o(1))D\).  Any admissible codegree parameter therefore satisfies

\[
 C\ge(2-o(1))D/m^2.
\]

The displayed leave certificate is consequently bounded below, up to
logarithmic factors which only strengthen the obstruction, by

\[
 K\exp\!\left(-(2+o(1))\frac{\log m}{K}\right),
 \qquad K=4\ell.
\]

For this certificate itself to tend to zero, it is necessary that

\[
 \frac{\log m}{2\ell}-\log\ell\to+\infty,
\]

and hence \(\ell=O(\log m/\log\log m)\).  Positive-density middle coverage
with independent initialization costs asymptotically \(HW/\ell\), so
portal excess \(o(W)\) additionally forces \(H/\ell\to0\).  This proves
the stated ceiling

\[
 H=o(\log m/\log\log m)
\]

for this certificate and reset architecture only.

## 10. Translation-kernel upper-shadow collapse

Let \(\ell=2^t\), let \(K=\ker\phi\) have codimension \(t+1\), and fix
one directed cycle position \(p\).  The preceding \(H<\ell\) flips form an
\(H\)-set \(J(p)\).  Its canonical upper pair-mask is the affine face

\[
 p+V_{J(p)}.
\]

Two translates at that position give the same face exactly when their
translation difference lies in \(V_{J(p)}\).  The dimension formula gives

\[
 \dim(K\cap V_{J(p)})
 \ge (\ell-t-1)+H-\ell=H-t-1.
\]

Thus every fixed-position face has at least
\(2^{\max(0,H-t-1)}\) translation preimages.  Since the tiling has
\(2\ell|K|=2^\ell\) state occurrences, its total upper-face support is at
most

\[
 2^\ell\min\{1,2\ell/2^H\}.
\]

Cartesian extension multiplies both occurrence count and this bound by
\(2^{s-\ell}\).  Summing over orientation strata can only overcount global
Boolean masks.  Therefore, whenever these product extensions contain
\(W-o(W)\) middle owners and \(H-\log_2\ell\to\infty\), their upper support
is \(o(W)\); an \(o(W)\) omitted or repaired owner set changes this by at
most \(o(W)\).  This verifies the patched global clause.

At \(H\asymp\sqrt{m\log m}\), \(\ell\asymp m^{3/4}\),

\[
 \frac{2\ell2^{-H}W}{N_H}
 =\exp\{-H\log2+H^2/m+O(\log\ell)+o(1)\}=o(1),
\]

and the same is true at fixed Gaussian depth \(H=A\sqrt m\).  The
obstruction concerns the unchanged fixed-kernel translation tiling.  It
does not rule out varying kernels, active frames, or nonlinear cycle
factors.

## 11. Exact remaining scope

The audited construction proves genuine long residual-consuming MTF
components, nearly complete distinct support in one selected deep row, and
strong aggregate product-box incidence at a growing polylogarithmic depth.
It does not prove any of the following:

* simultaneous globally distinct support in all intermediate rows;
* a Gaussian-window projected-strip matching;
* a prescribed integral target assignment inside the product boxes;
* PTAD, a trace-repair theorem, or the coefficient-one conjecture.

Within those limits, every theorem and ledger in the source is valid.
