# Augmented-orbit stalling and the soft-trace redirect

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

For one coordinate orbit of a full floor-calibrated multirank template,
the usual product-survival trajectory has no surviving edge after consuming
more than order

\[
 O(\log m/\sqrt m)
\]

of every protected resource stratum.  This is an exact upper survival scale
for the product model, not merely a failure of a particular
fixed-uniformity matching theorem.  It does **not** rule out a correlated
integral construction or a union of vastly many template types.  A matching
lower survival scale would require a second-moment or structural theorem.

The correct redesign is to keep only middle ownership as a hard matching
constraint and treat lower/upper traces by a global additive defect
functional.  At depth one that soft defect is exactly the number of
rank-\((m-1)\) targets absent from the chosen exact factor.  The canonical
MSW factor has an already audited positive-density defect, so it cannot be
repaired by choosing phases inside its unchanged wreaths.

## 1. Product-survival stalling

Let \({\cal O}\) be the simple \(S_n\)-orbit of one augmented template.
Write

\[
 M=|{\cal O}|\le n!,
 \qquad K=|e|\quad(e\in{\cal O}).
\]

Suppose a residual set retains every resource independently with
probability \(z\).  Then an orbit edge survives with probability \(z^K\),
and hence

\[
 \boxed{\mathbb E|{\cal O}_{\rm live}|=Mz^K.}
 \tag{1.1}
\]

In particular, if

\[
 \log(1/z)>\frac{\log M}{K},
\]

then the expected live catalogue is smaller than one.  Markov's inequality
also gives

\[
 \Pr({\cal O}_{\rm live}\ne\varnothing)\le Mz^K.
 \tag{1.2}
\]

For the symmetric floor calibration in \(n=2m+1\), one template uses

\[
 K=n+2\sum_{q\le Q}a_q,
 \qquad
 a_q=\left\lfloor\frac{nN_q}{W}\right\rfloor,
\]

and, once \(Q/\sqrt m\to\infty\),

\[
 K=(1+o(1))n\sqrt{\pi m}.
 \tag{1.3}
\]

Since \(\log M\le\log(n!)=(1+o(1))n\log n\), the product threshold obeys

\[
 \log(1/z_*)\le(1+o(1))\frac{\log n}{\sqrt{\pi m}}.
 \tag{1.4}
\]

Thus

\[
 1-z_*=O(\log m/\sqrt m).
\]

The direction of (1.4) is important: \(M\le n!\) gives an upper bound on
how deep a single coordinate orbit can possibly survive in the product
model.  For the full labelled orbit \(M\) has factorial order and the
displayed scale is sharp up to \(1+o(1)\) in the exponent.

This does not prove that every matching algorithm stalls there.  A
correlated residual need not have product edge-survival probability, and a
catalogue containing many genuinely different template orbits can have
many more than \(n!\) indexed choices.  What (1.1) rules out is precisely
the standard pseudorandom/product trajectory for one giant hard edge.

## 2. Hard middle, soft protected traces

The middle-only edge rank is \(n\), and the same calculation gives the much
deeper product threshold \(z\asymp1/m\).  Moreover the MSW theorem already
provides an exact middle factor.  Therefore lower/upper targets should not
all be inserted as hard matching vertices.  For an exact middle factor
\(F\), define instead

\[
 H_q(F)=N_q-
 \left|\bigcup_{\pi\in F}
 \{I_\pi(j,m-q):j\in\mathbb Z_n\}\right|.
 \tag{2.1}
\]

The intact cyclic-block word has the exact central-band bound

\[
 L_{[m-Q,m+Q+1]}
 \le T(n+2Q+1)+2\sum_{q=0}^QH_q(F),
 \tag{2.2}
\]

where \(T=W/n\) and \(H_0=0\).  Hence the direct deterministic target is

\[
 \boxed{\sum_{q\le Q}H_q(F)=o(W),}
 \tag{2.3}
\]

or one of the already audited entropy-compressed variants.  Equation
(2.3) is a budgeted discrepancy requirement, not a hard multirank matching.

## 3. The exact depth-one statistic

For \(R\in\binom{[n]}{m-1}\), define

\[
 e_F(R)=\#\{x\notin R:
 x\text{ is an endpoint of }R\cup\{x\}
 \text{ in its unique owning wreath of }F\}.
 \tag{3.1}
\]

Every cyclic occurrence of \(R\) belongs to exactly two owning middle
extensions, obtained by adjoining its predecessor or successor.  Therefore

\[
 \boxed{\mu_{F,1}(R)=\frac12e_F(R),}
 \qquad
 \boxed{\sum_Re_F(R)=2W.}
 \tag{3.2}
\]

In particular \(e_F(R)\) is even and

\[
 \boxed{H_1(F)=\#\{R:e_F(R)=0\}.}
 \tag{3.3}
\]

If \(h_1=H_1(F)\), then

\[
 \#\{R:e_F(R)\ge4\}
 \le W-N_1+h_1
 =\frac{2W}{m+2}+h_1.
 \tag{3.4}
\]

Indeed the right side is the total duplicate excess
\(\sum_R(\mu_{F,1}(R)-1)_+\), and every term with \(e_F(R)\ge4\) contributes
at least one.

For literal support, (3.3) is the whole depth-one condition:
\(H_1(F)=o(W)\).  It is **not** sufficient for a prescribed constant
left-degree trace assignment.  That stronger assignment is a bipartite
\(b\)-matching and still has subset Hall cuts.

The canonical MSW factor is already known to violate (3.3) at coefficient
scale:

\[
 H_1(F_m^{\rm MSW})\ge(1/16-o(1))W.
 \tag{3.5}
\]

Thus no choice of certified phases inside its unchanged wreaths can solve
the first soft trace.  A successful MSW-started construction must perform
positive-density exact-factor trades.

## 4. Exact Hall-defect identity for a fixed factor

At depth \(q\), let \(G_q(F)\) be the bipartite graph from wreath rows to
their cyclic rank-\((m-q)\) intervals.  Every left degree is \(n\).  For a
desired left quota \(a_q\), the maximum number of selected incidences has
defect

\[
 \boxed{
 D_q(F)=\max_{A\subseteq F}
       \bigl(a_q|A|-|N_q(A)|\bigr)_+.}
 \tag{4.1}
\]

This is the max-flow/min-cut formula.  Put \(c_q=n-a_q\), let
\(h_q=N_q-|N_q(F)|\), and let \(B=F\setminus A\).  Since adding the rows
of \(B\) introduces at most \(n|B|\) targets,

\[
 |N_q(A)|\ge N_q-h_q-n|B|.
\]

If \(a_qT=N_q-\delta_q\), then every cut satisfies

\[
 \boxed{
 a_q|A|-|N_q(A)|
 \le h_q-\delta_q+c_q|B|.}
 \tag{4.2}
\]

Equation (4.2) is useful for quarantining a small complement of
pathological rows, but it does not make the full Hall condition a function
of \(h_q\) alone.

## 5. Scope of the large-depth heuristic

For \(|R|=m-q\), let \(\operatorname{ext}_q(R)\) count middle extensions
whose owning wreath displays \(R\) as an interval.  Then

\[
 \mu_{F,q}(R)=\frac{\operatorname{ext}_q(R)}{q+1},
 \qquad
 \sum_R\operatorname{ext}_q(R)=(q+1)W.
 \tag{5.1}
\]

The exact identity in (5.1) says that the `q+1` extensions belonging to one
displayed lower interval arrive as one indivisible cluster.  Consequently
the plausible independent-occurrence Poisson prediction is

\[
 \Pr(\operatorname{ext}_q=0)\approx
 e^{-W/N_q},
\]

not `exp(-(q+1)W/N_q)`.  In particular, for `q=o(sqrt(m))` one has
`W/N_q=1+o(1)`, so this corrected zero probability remains near `e^{-1}`.
Equation (5.1) alone does not prove even the corrected heuristic: an average
gives no upper bound on the zero mass.  Any reduction of the full Gaussian
band to slowly growing depth must therefore establish an anticoncentration
or extension-spread theorem for the exact factor.  Until then, no
exponential depth tail is a structural reduction.
