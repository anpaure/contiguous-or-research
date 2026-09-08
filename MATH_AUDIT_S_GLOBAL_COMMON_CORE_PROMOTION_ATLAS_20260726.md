# Audit of the global common-core promotion atlas

Date: 2026-07-26

Source audited:
`MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md`.

## 0. Verdict

The random-core caps, all clone-Hall arguments, the signed-rank hole
ledger, and the literal core-safe path are correct under the displayed
critical-scale hypotheses.  The claimed conclusion remains only a
rankwise/integral and globally/fractional atlas; it does not produce one
integral path per top with a common history.

There is one formal gap in Section 4 of the source, but it is repairable
without a new hypothesis:

1. the catalogue \(\mathscr P(U)\) is defined there as an untagged path
   catalogue, whereas its signed-rank claims require tagged options; and
2. the exact transitivity proof averages over all possible cores, not over
   the fixed core assignment supplied by Theorem 3.1.

After adjoining a nested tag profile to each option, the source's exact
all-core symmetric fractional point is valid.  More strongly, the *same
fixed cores* from Theorem 3.1 admit a common fractional configuration
point with every target load at most one.  The latter follows directly
from the degree caps and is proved in Section 5 below.

Thus the strongest valid conclusion is:

> At critical height, there is one fixed \(2H\)-core in every top such
> that every signed rank separately has the asserted integral clone
> matching with aggregate \(o(W)\) holes; every top admits literal
> \(L\)-phase core-safe paths; and the full tagged path configuration LP
> for those same fixed cores is feasible.  What remains unproved is the
> integral common-history/tight-path fusion.

## 1. Parameter and random-core audit

Write

\[
 M=m+H,\qquad s=m-H,\qquad L=m-3H+1,
 \qquad \Lambda={W\over N_H}.
\]

The assumptions imply \(L<\Lambda=\Theta(m)\) and
\(N_H=\Theta(W/m)\).  For a fixed middle owner \(X\), the number of
tops \(U\supset X\) whose random core lies in \(X\) is binomial with
mean

\[
 \binom mH {\binom m{2H}\over\binom M{2H}}
 ={(m!)^2\over H!(m-2H)!M!}
 ={1\over\Lambda}\binom sH={d_0\over\Lambda}.
\]

At the threshold \(d_0/L\), the relative excess is
\(\delta_0=\Lambda/L-1=\Theta(H/m)\), with the stated one-sided
constant bounds.  Hence the Chernoff exponent is

\[
 \Omega\left({d_0H^2\over m^3}\right).
\]

Because \(d_0=\binom sH\) is superpolynomial enough that this quantity
is \(\exp(\Omega(\sqrt m\,\log^{3/2}m))\) up to harmless lower-order
changes in the exponent, it is much larger than \(m\).  The union bound
over fewer than \(4^m\) owners is therefore \(o(1)\), not merely less
than one.

For signed rank \(r\), a fixed target \(Y\) has binomial degree with
mean

\[
 \binom{m-r}{H-r}{\binom{m+r}{2H}\over\binom M{2H}}
 ={d_r\over\Lambda_r},\qquad
 d_r=\binom s{H-r},\quad
 \Lambda_r={N_{|r|}\over N_H}.
\]

If \(b_{|r|}>0\), then \(b_{|r|}\le\Lambda_r-1\).  Writing
\(b=b_{|r|}\) and \(\Lambda'=\Lambda_r\), the exact Chernoff exponent
at \(d_r/b\) is bounded below by

\[
 {d_r(\Lambda'-b)^2\over
   \Lambda'b(\Lambda'+b)}
 \ge {d_r\over2(\Lambda')^3}.
\]

For \(r=q>0\), \(\Lambda_r\ge2\) implies
\(H-q=\Omega(m/H)\) by the exact product for \(N_q/N_H\).  For
\(r=-q\), one has \(H-r\ge H\).  Since \(H=o(m)\), for all sufficiently
large \(m\) the relevant binomial coefficients lie on the increasing
side and

\[
 {d_r\over\Lambda_r^3}
 \ge {1\over O(m^3)}
       \binom{s}{\lceil c m/H\rceil}
 \gg m.
\]

The simultaneous union bound over \(O(HW)\) signed targets is therefore
valid.  The only presentational qualification is that the monotonicity of
the binomial coefficient used here requires, say, \(m>5H\); this follows
automatically for all sufficiently large \(m\) from the asymptotic
hypothesis, even though the source displays only \(m>4H\).

## 2. Clone-Hall audit

The completion-to-full-fibres sentence in Theorems 1.2 and 3.2 is valid.
For an arbitrary set \(S\) of clones, let \(\mathcal A\) be the tops
whose clone fibres meet \(S\).  Identical clones give

\[
 N(S)=N(\mathcal A),\qquad |S|\le b|\mathcal A|.
\]

The incidence count and the maximum right degree give

\[
 |N(\mathcal A)|
 \ge {d_r|\mathcal A|\over d_r/b}
 =b|\mathcal A|\ge |S|.
\]

This proves Hall for arbitrary clone subsets, not only complete fibres.
Consequently the middle \(L\)-clone matching and every signed
\(b_q\)-clone matching are integral and correct for one common fixed core
assignment.

## 3. Physical core-safe path audit

For a cyclic order whose displayed blocks are \((Q,S)\), the exact
full-top promotion-ring formula is

\[
 C_i(r)=U\setminus
 I(i+H+r,H-r).
\]

The phases whose full \(2H\)-word lies in the linear \(S\)-block have
the \(L=s-2H+1\) consecutive starts.  At every active rank \(r<H\),
their omitted intervals are nonempty proper intervals of one injective
linear word, with distinct starting positions; hence their masks are
distinct.  At \(r=H\), the omitted interval is empty and every mask is
the top \(U\), so the condition that at most one retained phase have tag
\(H\) is exactly what is needed.  Different ranks have different set
sizes.

Every omitted interval lies in \(S=U\setminus Q\), so every retained
mask contains \(Q\).  At the middle rank the omissions are precisely

\[
 \{t_{j+H},\ldots,t_{j+2H-1}\},\qquad1\le j\le L,
\]

the consecutive \(H\)-windows of the injective word
\((t_{H+1},\ldots,t_s)\).  Theorem 2.1 is therefore a literal promotion
path, not merely a support statement.

This audit also confirms the stated incompatibility: an arbitrary
integral middle Hall matching need not form these consecutive windows.

## 4. Signed-rank and aggregate ledger audit

The profile

\[
 b_0=L,\qquad
 b_q=\min\{L-1,\max\{0,\lfloor N_q/N_H\rfloor-1\}\}
\]

is nonincreasing and fits into \(L\) nested phase thresholds.  In an
uncapped positive depth, and also when \(b_q=0\),

\[
 0\le N_q-b_qN_H<2N_H.
\]

If the cap \(L-1\) is active, then
\(N_q/N_H\ge L\).  Since \(\Lambda=m+O(H)\),
\(L=m-3H+1\), and

\[
 {N_q\over N_H}
 =\Lambda\exp\left(-{q^2\over m}
 +O\left({q\over m}+{q^4\over m^3}\right)\right),
\]

this forces \(q=O(\sqrt H)\).  At each capped depth the deficit is
\(O(HN_H)\).  Thus both signs, the middle rank, and the two exceptional
boundary ranks have total holes

\[
 O(H^{3/2}N_H)+O(HN_H)+O(N_H)
 =O(H^{3/2}N_H)=o(W),
\]

because \(H^{3/2}/m=o(1)\) at the calibrated height.  Charging an
\(O(H)\)-mask literal collar to every boundary exception remains
\(O(HN_H)=o(W)\).

These counts are separate-rank counts only.  They do not identify common
phases or impose nesting on the chosen integral matchings.

## 5. Repaired and strengthened fractional configuration theorem

Fix the particular core assignment \((Q_U)_U\) supplied by Theorem 3.1.
For every top \(U\), independently choose a uniformly random ordering of
the tail \(S_U=U\setminus Q_U\), and take its literal \(L\)-phase
core-safe path.  Put \(b_H=0\).  Choose, independently of the tail order,
a uniformly random placement on the \(L\) phases of any nested tag
multiset satisfying

\[
 \#\{\hbox{tags at least }q\}=b_q,
 \qquad0\le q\le H.
\]

Such a multiset exists because the \(b_q\)'s are nonincreasing; explicitly
there are \(b_q-b_{q+1}\) tags equal to \(q\).  It has no tag \(H\), so
the local disjointness condition is automatic.

Fix signed rank \(r\), put \(q=|r|\), and let
\(Y\) satisfy \(Q_U\subset Y\subset U\).  Its deleted set has size
\(H-r\).  At every fixed eligible phase, a uniform tail order makes that
deleted set uniform among the

\[
 d_r=\binom{s}{H-r}

possible sets.  The exchangeable tag placement activates each of the
\(L\) phases with probability \(b_q/L\).  Since distinct phases of one
path have distinct masks at this rank,

\[
 \Pr_U(Y\hbox{ is used at rank }r)={b_q\over d_r}.
\]

At the middle rank the same formula is \(L/d_0\).  Consequently the
total fractional load of any target is bounded by the fixed-core degree
cap:

\[
 {b_q\over d_r}\deg_r(Y)\le1,
 \qquad
 {L\over d_0}\deg_0(X)\le1.
\]

Therefore these distributions, one per top and summing to one, form one
fractional matching in the *tagged literal-path configuration
hypergraph*, simultaneously respecting every signed target capacity for
the same fixed cores.

This also proves the combined nonnegative weighted-cut statement.  For
any nonnegative weights on any collection of signed ranks, the minimum
cost option for each top is at most its expectation under the common
distribution above.  Summing over tops and using the target loads at
most one bounds the result by the total target weight.

If instead one averages over all cores, orders, and exchangeable tag
placements, coordinate transitivity gives the exact loads stated in the
source,

\[
 \rho_0={LN_H\over W},\qquad
 \rho_q={b_qN_H\over N_q}.
\]

That exact equality is correct, but it concerns the unrestricted
all-core catalogue.  The fixed-core result above is the form that
actually joins Sections 1--3 to Section 4.

## 6. Exact strongest surviving theorem

Under (0.3)--(0.4), for all sufficiently large \(m\), there is one core
assignment \((Q_U)_U\) with all of the following properties.

1. The middle clone graph has an integral matching assigning \(L\)
   distinct core-compatible owners to every top.
2. At every internal signed rank \(m+r\), there is separately an integral
   matching assigning \(b_{|r|}\) distinct core-compatible targets to
   every top.
3. The aggregate number of targets not assigned in these separate
   matchings, including both exceptional boundaries, is
   \(O(H^{3/2}N_H)=o(W)\).
4. Every top supports literal \(L\)-phase core-safe promotion paths whose
   masks at every active rank contain its fixed core.
5. The tagged literal-path configuration hypergraph for these same fixed
   cores has an explicit fractional matching saturating every top root
   and loading every target by at most one.  Hence every combined
   nonnegative additive configuration-Hall cut passes.

None of these statements supplies an integral selection of one path per
top.  The exact remaining theorem is to fuse the separately integral
rank assignments into one ordered tail and one nested tag history per
top while keeping aggregate collisions and literal repair cost \(o(W)\).
This common-history assertion is not a consequence of Hall, symmetry, or
the fractional point above.
