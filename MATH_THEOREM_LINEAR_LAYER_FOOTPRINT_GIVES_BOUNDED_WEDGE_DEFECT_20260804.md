# A linear cap footprint gives only bounded protected-wedge defect

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional endpoint-factorized bounded-defect theorem.  It
does not require rank-monotone compensation paths.  It reduces the
one-coordinate cap gate to a linear total footprint on the owner and q1
terminal layers.  The present Pascal construction does not yet prove that
footprint or its regeneration.

## 0. Main result

Fix distinct required lower turns

\[
                         L_1,\ldots,L_p\in\mathcal L
 ={[2m-1]\choose m-1},
\qquad 1\le p\le m-1.
\]

Assume one raw endpoint-factorized cap state: before the frozen background
is deleted, every direct branch

\[
 L_i\longrightarrow L_i+a\longrightarrow L_i+a+b
\tag{0.1}
\]

is present, typed legal, completion-stable, and has no unpriced hidden
capacity.  Different owner and q1-terminal values use distinct physical
capacities.

Let

\[
 D_{\mathcal U}\subseteq{[2m-1]\choose m},
 \qquad |D_{\mathcal U}|=f,
\]

be the owner values made unavailable by the frozen background, and let

\[
 D_Z\subseteq{[2m-1]\choose m+1},
 \qquad |D_Z|=g,
\]

be the unavailable q1 terminal values.  Required lower source occurrences
are protected.

For each \(i\), put

\[
 r_i=|D_{\mathcal U}\cap N(L_i)|,
\tag{0.2}
\]

where \(N(L_i)\) is its \(m\)-element owner star.  Define

\[
 T={m-p+1\choose2},
\tag{0.3}
\]

and, when \(g<T\), let

\[
 \rho=\min\left\{r\ge0:{r\choose2}+g\ge T\right\}.
\tag{0.4}
\]

Finally put

\[
 \Phi(f,p)=
 {f+\sqrt{f^2+4fp(p-1)}\over2}.
\tag{0.5}
\]

### Theorem

All but at most

\[
 \boxed{
 C_{\rm cap}
 =\left\lfloor{\Phi(f,p)\over\rho}\right\rfloor
 }
\tag{0.6}
\]

required lower turns admit a simultaneous protected active-wedge
selection and pairwise private direct routing.

In particular, fix constants \(A,G,C\).  If

\[
 f\le Am,\qquad g\le Gm,\qquad p\le C\sqrt m,
\tag{0.7}
\]

then for all sufficiently large \(m\),

\[
 \boxed{
 C_{\rm cap}
 \le
 \left\lfloor
 A+\sqrt{A^2+4AC^2}
 \right\rfloor.
 }
\tag{0.8}
\]

Thus a total owner/q1 footprint linear in \(m\) causes only \(O(1)\)
one-coordinate cap casualties, even when one frozen path visits
\(\Theta(m)\) owner vertices.

## 1. Exact active menu at one source

A wedge at \(L_i\) is unusable through endpoints only when:

1. both of its owner values lie in \(D_{\mathcal U}\); or
2. its q1 terminal value lies in \(D_Z\).

There are exactly \({r_i\choose2}\) pairs of the first type.  At most \(g\)
additional pairs have a forbidden terminal.  Hence

\[
 |W_i^c|
 \ge {m\choose2}-{r_i\choose2}-g.
\tag{1.1}
\]

The exact packing threshold for all \(p\) tasks is

\[
 B_{p-1}(m)
 ={m\choose2}-{m-p+1\choose2}
 ={m\choose2}-T.
\tag{1.2}
\]

Therefore

\[
 {r_i\choose2}+g<T
 \quad\Longrightarrow\quad
 |W_i^c|>B_{p-1}(m).
\tag{1.3}
\]

By definition of \(\rho\), every source with \(r_i<\rho\) satisfies
(1.3).  Call a source **owner-heavy** when \(r_i\ge\rho\).

## 2. The owner-star incidence bound

Two distinct lower turns have at most one common rank-\(m\) owner.  For
each damaged owner \(U\in D_{\mathcal U}\), put

\[
 d_U=|\{i:L_i\subset U\}|.
\]

Then

\[
 \sum_{U\in D_{\mathcal U}}{d_U\choose2}
 \le {p\choose2}.
\tag{2.1}
\]

Indeed, every pair \(L_i,L_j\) is counted at most once.

Let

\[
                         I=\sum_{i=1}^p r_i
                          =\sum_{U\in D_{\mathcal U}}d_U.
\tag{2.2}
\]

By Cauchy--Schwarz and (2.1),

\[
\begin{aligned}
 {I^2\over f}
 &\le\sum_Ud_U^2\\
 &=I+2\sum_U{d_U\choose2}\\
 &\le I+p(p-1).
\end{aligned}
\tag{2.3}
\]

When \(f=0\), \(I=0\).  For \(f>0\), solving the quadratic inequality gives

\[
                         \boxed{I\le\Phi(f,p).}
\tag{2.4}
\]

Every owner-heavy source contributes at least \(\rho\) to \(I\).  Hence
their number is at most (0.6).

## 3. Pack and route every nonheavy source

Every nonheavy source has an active menu larger than
\(B_{p-1}(m)\), by (1.3).  Delete the owner-heavy sources and apply the
exact active-wedge packing theorem to the remaining menus.  Its actual
threshold for the smaller family is no larger than \(B_{p-1}(m)\), so the
selection is valid.

The selected wedges have pairwise distinct owners and q1 terminal values.
Every selected wedge has at least one owner outside
\(D_{\mathcal U}\) and terminal outside \(D_Z\); choose such an owner side.
The endpoint-factorized premise and automatic-private-routing theorem give
pairwise disjoint typed direct routes.

The omitted owner-heavy sources form a sidecar of size at most
\(C_{\rm cap}\).

## 4. Asymptotic constant evaluation

Assume (0.7).  For all sufficiently large \(m\),

\[
                         p\le {m\over4}
\]

and

\[
 {\lfloor m/2\rfloor\choose2}+Gm
 <
 {m-p+1\choose2}=T.
\tag{4.1}
\]

Thus

\[
                         \rho>{m\over2}.
\tag{4.2}
\]

Also \(p(p-1)\le C^2m\), so

\[
\begin{aligned}
\Phi(f,p)
 &\le
 {Am+\sqrt{A^2m^2+4Am\cdot C^2m}\over2}\\
 &=
 {m\over2}\left(A+\sqrt{A^2+4AC^2}\right).
\end{aligned}
\tag{4.3}
\]

Divide (4.3) by (4.2) to obtain (0.8).

The constant \(G\) changes only the finite threshold beyond which
\(\rho>m/2\); it does not enter the displayed asymptotic casualty bound.

## 5. Extension to hidden wedge holes and source casualties

Let \(H_i\) be the set of additional wedge terminal pairs whose complete
branch menus are killed by explicitly priced hidden resources, after owner
and q1-terminal deletions are accounted for.  Replace \(g\) in (1.1) by

\[
                         g_i=|D_Z|+|H_i|.
\]

The same proof works with

\[
 \rho_i=
 \min\left\{r:{r\choose2}+g_i\ge T\right\}.
\]

A uniform lower bound \(\rho_i\ge\rho_*\) yields

\[
                         C_{\rm cap}\le
 \left\lfloor{\Phi(f,p)\over\rho_*}\right\rfloor.
\tag{5.1}
\]

If \(c\) required source occurrences are themselves deleted, add \(c\) to
the sidecar and apply the theorem to the surviving sources.  This is
necessary: one source deletion kills every wedge at that source.

## 6. Sharp scale and the snake obstruction

The constant conclusion is of the correct scale.  To make one source
owner-heavy requires \(\Theta(m)\) damaged owner incidences.  Because
different lower stars overlap in at most one owner, damaging \(b\)
well-separated sources requires \(\Theta(bm)\) owner footprint.  Thus a
linear footprint can genuinely force a positive constant number of
casualties, but not an unbounded number in the regime (0.7).

The known snake-path obstruction permits one compensation path to visit
arbitrarily many owner capacities.  It does not contradict the theorem:
when its relevant owner-layer footprint is \(f=\Theta(m)\), it can destroy
one or another constant number of fixed source stars.  To create unbounded
sidecar growth it must have superlinear relevant footprint or exploit an
unpriced hidden capacity shared across many branch menus.

## 7. Regenerative linear-footprint lemma

The one-coordinate cap row is bounded if the same-parity construction
proves the following state invariant.

> **Regenerative LLF.**  There are absolute constants \(A,G,C,C_0\) such
> that every transition exposes at most \(p\le C\sqrt m\) protected wedge
> tasks in one endpoint-factorized cap state; after freezing the transported
> background, its distinct owner and q1-terminal footprints satisfy
> \(f\le Am,g\le Gm\); hidden/source casualties add at most \(C_0\); and the
> resulting bounded sidecar is transported without accumulation.

The theorem proves that this invariant contributes only

\[
 C_0+
 \left\lfloor A+\sqrt{A^2+4AC^2}\right\rfloor
\]

terminal casualties per regenerated state.  Combined with the other
bounded-defect carrier/compiler/topology rows, Regenerative LLF would imply
\(B(k)+O(1)\).

The current record does not yet prove endpoint factorization, the linear
physical footprint, or nonaccumulation.

## 8. Exact scope

The theorem proves bounded protected-wedge defect from a linear owner/q1
deletion footprint.  It replaces the stronger bounded-per-path
rank-crossing condition when exact zero defect is unnecessary.

It does not prove the LLF invariant, bound hidden branch killers from
physical path length, authenticate transported phase one, or solve
two-coordinate product closure, topology, upper decoration, residence, or
compiler regeneration.

## 9. Dependencies

| role | file |
|---|---|
| exact active-menu packing | MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md |
| endpoint-only cap count | MATH_THEOREM_ENDPOINT_ONLY_ACTIVE_WEDGE_MARGIN_20260804.md |
| paired hidden-capacity casualty | MATH_THEOREM_PAIRED_TURN_DIAMOND_DELETION_AND_MINIMAL_OCCURRENCE_LIFT_20260804.md |
| snake-path obstruction | MATH_THEOREM_BOOLEAN_JOHNSON_PRIVATE_SUFFIX_RADO_ROUTER_20260803.md |
