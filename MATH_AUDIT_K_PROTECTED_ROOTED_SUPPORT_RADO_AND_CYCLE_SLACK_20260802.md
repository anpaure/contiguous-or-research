# Audit of the protected rooted-support Rado and cycle-slack theorem

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_K_PROTECTED_ROOTED_SUPPORT_RADO_AND_CYCLE_SLACK_20260802.md`  
**Theorem SHA-256:**
`ce88f85184d1467bede84382cc80934e8c5ae332a1088cb1a064aa0463f20ed2`  
**Verdict:** PASS after the scope corrections recorded below

## 1. Graphic contraction, including parallel opposite arcs

For `e=LV` outside `M_0`, the rooted occurrence

\[
                         \lambda(e)=L M_0^{-1}(V)
\]

determines `L` and `V`, so `lambda` is injective.  An incidence matching
has distinct `L` and distinct `V`, hence its rooted multigraph has
outdegree and indegree at most one.  Opposite directed occurrences between
the same two roots are distinct parallel graphic elements and form a
length-two multigraph cycle.  The graphic rank formula

\[
 r(E)=W-c(E)
\]

continues to hold for such a multigraph.  Since the forced bank `F` is a
forest, `r(F)=|F|`, and therefore

\[
 r_{M_{\rm gr}/F}(E(A))
   =r_{M_{\rm gr}}(F\cup E(A))-|F|
   =|E(A)|-\kappa_F(A).
\]

Thus Theorem 3.1's contraction, cycle-nullity, and component-cut forms are
identical and exact.

## 2. Rado deficiency sign

For families indexed by `mathcal R`, the maximum independent partial
transversal has size

\[
 \min_{A\subseteq\mathcal R}
 \left(|\mathcal R\setminus A|+r_{M_{\rm gr}/F}(E(A))\right).
\]

Substituting the preceding rank formula gives

\[
 |\mathcal R|-
 \max_{A\subseteq\mathcal R}
 \left(|A|-|E(A)|+\kappa_F(A)\right).
\]

Hence the sign in (3.8)--(3.10) is correct.  The empty index family gives
zero, so the displayed maximum is nonnegative.

## 3. Hamilton-cycle edge case with protected-colour duplicates

Corollary 4.3 remains correct when a non-`F` edge repeats a colour already
represented by `F`.  Such an edge is excluded from every residual family,
so `F union E(A)` cannot equal the full rooted cycle; its nullity is then
zero.  If full-cycle activation does occur, every non-`F` edge is eligible,
availability forces `A=mathcal R`, and

\[
 |E(A)|-|A|=(W-|F|)-(U-|F|)=W-U=C\ge1,
\]

which pays the sole cycle.  This exhausts both cases.

## 4. Replay-bound equivalence

The implication `PRS => Q_0` is valid because choosing the Rado
transversal only marks occurrences already present in `A_src`; it performs
no rethreading or address identification.  The reverse implication via
`S=Q_0` is exact only when the right-hand side quantifies the same literal
chronology `A_src`, global-address quotient, accepted histories, endpoint
aperture, and protected witness closure.  The theorem now states that pair
explicitly in (5.1).  An abstract rooted forest cannot manufacture a
source antecedent.

The omitted-root guard

\[
                         o\subset s\quad\hbox{or}\quad o\subset t
\]

and the one-credit aperture equation remain hypotheses on `A_src`; no
graphic rank inequality implies either one.  Similarly, replay inheritance
ends when the selected components are subsequently reordered or opened.
That later operation still needs `GOP/PHWC` and the sequential all-width
ledger.

## 5. Exact `k=17` scope

The current connected `h=1` augmented factor is not itself the incidence
matching support `S` in Theorem 3.1.  To enter this theorem one must still:

1. choose an alternating perfect predecessor matching `M_0`;
2. delete the appropriate residual `D`-tail edge to obtain the successor
   incidence matching support; and
3. verify omitted-root endpoint containment and literal replay for that
   phase.

Consequently the certified ordinary holes are only a calibration of empty
task families, not an unconditional value of `delta_F(S)`.

The shore arithmetic is:

\[
 |\mathcal U|=19,448,\qquad
 |\mathcal U_{\rm non-D}|=19,412,\qquad
 W=24,310.
\]

The three-hole checkpoint is certified on the restricted non-`D` shore.
Its literal rank-10 replay has `25=3+22` holes.  A restricted forest would
have `24,310-19,412=4,898` components, not the full Catalan count
`24,310-19,448=4,862`.  The one-hole checkpoint at mask `32058` has a
reported independent replay, but the theorem correctly makes no
authoritative fixed-support promotion; it retains the `22` exceptional
boundary/`D` tickets.

## 6. Scope retained

The theorem closes exactly the protected upper-exact marking problem on a
replay-bound matching support.  It does not construct that support, select
the later Catalan component order, replay nonadjacent overlaps after a
rethread, preserve a cut's exterior long windows, supply the terminal
common cap, or regenerate the next prepared aperture.  Therefore it is a
proof-safe smaller equivalent clause of `PCPS`, not a proof of `PCPS`.

