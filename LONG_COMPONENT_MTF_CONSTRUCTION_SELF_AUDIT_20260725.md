# Self-audit of the long-component projected-strip theorem

Date: 2026-07-25

Audited source: `LONG_COMPONENT_MTF_CONSTRUCTION_20260725.md`.

## Verdict

**INTERNAL PASS, pending independent cross-audit.**

The projected hypergraph count, orbit codegree, quantitative matching
parameters, virtual cyclic closure, residual depletion, support ledger,
literal word length, and proof-method ceiling are reconstructed below.

## 1. Projected strip geometry

For fixed disjoint cores (C,D) of size (m-\ell), the active set has
size (2\ell).  The (2\ell) cyclic half-intervals have common
intersection (C), common union (C\cup R), and induced Johnson graph
(C_{2\ell}).  Hence their unordered middle row recovers (C,D), and the
active cyclic order up to reversal.  Projecting a full strip to the middle
and one upper row therefore introduces no parallel edges.

The number of undirected strips is

\[
 \frac{(2m)!}{4\ell(m-\ell)!^2}.
\]

Multiplication by (2\ell) row incidences and division by the appropriate
rank size gives

\[
 D_d=\frac{(m+d)!(m-d)!}{2(m-\ell)!^2}.
\]

Thus the degree formula and its factor (1/2) are correct.

For a fixed first vertex (X), codegree is constant on every stabilizer
orbit of a second vertex (Y).  The orbit size is the product of the two
binomial coefficients in the source.  In the two selected ranks, every
nontrivial orbit has size at least (m-H).  The only size-one possibility
inside the vertex set is the complement of a middle set; its codegree is
zero because one strip has a nonempty common core.  Since an edge through
(X) has only (2\ell) vertices in the second rank,

\[
 \deg(X,Y)\le\frac{2\ell\deg(X)}{m-H}
 \le\frac{2\ell D}{m-H}.
\]

This verifies the codegree bound without using the sharper unaudited
constant.

## 2. Matching exponent

Let

\[
 L=\log m,
 \quad \lambda=\log L,
 \quad \ell=\lfloor L/(32\lambda)\rfloor,
 \quad K=4\ell.
\]

With (C_*=\lceil2\ell D/(m-H)\rceil), the fact that (D) is
superpolynomial makes the ceiling negligible, and

\[
 \frac{C_*\log(1+C_*)}{D}
 =O(\ell^2L/m).
\]

Its logarithm is (-L+O(\lambda)).  Since

\[
 K=(1+o(1))L/(8\lambda),
\]

raising to (1/(K-1)) gives

\[
 \exp(-(8+o(1))\lambda)=L^{-8+o(1)}.
\]

Multiplication by (K) leaves (L^{-7+o(1)}), as claimed.

The maximum/minimum degree ratio has logarithm at most (H^2/(m-H)).
Under (H=o(L/\lambda)), this is far below

\[
 (C_*\log D/D)^{1/3}=m^{-1/3+o(1)}.
\]

Also (K=o(\log D)), and

\[
 \log(e^{2K}C_*\log D/D)
 =-L+L/(4\lambda)+O(\lambda),
\]

which tends to (-\infty).  Every displayed hypothesis of the imported
quantitative matching theorem is therefore satisfied.

The two parts have sizes (W) and (N_H=W(1-o(1))).  A matching leaves

\[
 u_0=W-2\ell p,
 \qquad
 u_H^+=N_H-2\ell p,
\]

whose sum is (o(W)).  Hence (2\ell p=W-o(W)=N_H-o(W)).

## 3. Exact MTF boundary data

The transition schedule is

\[
 p_i=z_i,
 \qquad q_i=z_{i+\ell}.
\]

Thus an arriving active coordinate departs exactly \(\ell\) steps later.
Because \(H<\ell\), the path satisfies the audited no-short-positive-run
criterion.

At time zero the first upper singleton blocks are

\[
 z_{2\ell-1},\ldots,z_{2\ell-H}.
\]

The arrival at any later update is never one of the last \(H\) departures.
Induction in the queue recurrence therefore makes the first \(H\) upper
singletons at state (i)

\[
 z_{i-1},\ldots,z_{i-H}.
\]

Their union with the middle interval is the cyclic interval of length
(\ell+H) starting at (i-H).  This remains true at the left boundary by
the chosen initial queue, and at the right boundary because no future upper
queue is needed there.  The terminal dummy departures are needed for the
lower flags, and are compatible with the same cyclic schedule.  Hence no
upper depth-(H) mask is lost by cutting.

The initial residual has active part

\[
 z_\ell,\ldots,z_{2\ell-H-1},
\]

of size \(\ell-H\).  These are exactly the first \(\ell-H\) arrivals.
They are all deleted from the initial residual, while the opposite core
(D) never arrives.  Thus the terminal residual is (D), of size
(m-\ell<m-H).  Every selected component genuinely lies on the consuming
side of the depletion dichotomy.

## 4. Portal and word ledgers

One selected path has (2\ell) middle states and literal canonical word
length (2\ell+2H+1).  With independent exact resets, (p) paths have
portal excess ((2H+1)p).  Since (p\le W/(2\ell)) and (H/\ell\to0),
this is (o(W)).

Appending the (u_0) missing middle masks and (u_H^+) missing upper masks
gives exact total length

\[
 p(2\ell+2H+1)+u_0+u_H^+
 =W+(2H+1)p+u_H^+
 =W+o(W).
\]

The depletion lower bound for these (p) consuming components is

\[
 2H+1+2H(p-1)=2Hp+1.
\]

The ratio of the explicit reset upper bound to this lower bound tends to
one because (H\to\infty).  Hence the theorem does not depend on an
unproved cheap-bridge assertion.

## 5. Scope of the ceiling

For adjacent middle masks, stabilizer transitivity gives exact codegree

\[
 2D_0/m^2.
\]

Therefore the residual expression of the displayed quantitative matching
theorem is at least

\[
 K\exp(-(2+o(1))\log m/K).
\]

Its convergence to zero forces

\[
 \log m/(2\ell)-\log\ell\to+\infty,
\]

and in particular \(\ell=O(\log m/\log\log m)\).  Portal excess for a
positive-density family of consuming strips forces (H/\ell\to0).  The
resulting (H=o(\log m/\log\log m)) ceiling concerns only this quantitative
certificate and exact-reset strip architecture.  It is not asserted as a
matching or MTF nonexistence theorem.

The sparse-row interpolation has the same parameter check.  For (r)
selected rows and

\[
 \ell=\lfloor L/(16r\log L)\rfloor,
\]

the uniformity remains (K=2\ell r=(1+o(1))L/(8\log L)).  Its total vertex
count is at most (rW), so the matching leave is

\[
 O(rL^{-7+o(1)}W)=o(W)
\]

whenever (rH\log L/L\to0).  That condition also gives (H/\ell\to0),
which is exactly the portal and super-(H)-length requirement.  Thus the
interpolation theorem introduces no hidden dependence on the number of
selected rows.

## 6. Final audit status

The translation-kernel obstruction is also exact.  A depth-(H) upper
pair-mask is an (H)-face (p+V_J).  For a translation subgroup of
codimension (t+1=\log_2(2\ell)), every (H)-coordinate subspace meets the
kernel in dimension at least (H-t-1).  Hence each fixed-position face has
at least (2^H/(2\ell)) translation preimages, and the support fraction is
at most (2\ell/2^H).  This argument is invariant under cyclic phase and
reversal because the complete cyclic upper-row family is unchanged.  Its
scope is the fixed-kernel translation tiling, not arbitrary pair-flip cycle
factors.

The report proves a genuine growing-depth construction and a literal
two-rank (or, after the stated three-row modification, three-rank) OR word.
It does not prove simultaneous intermediate-rank coverage, trace entropy,
product-box incidence correlation, the Gaussian window, PTAD, or the full
coefficient-one theorem.
