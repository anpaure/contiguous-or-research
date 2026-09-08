# Audit of the raw switch four-role coefficient

**Date:** 2026-08-06  
**Method:** exact operator-index, coefficient, multiplicity, and static-ledger
audit; no computation or search  
**Verdict:** **FAIL / DO NOT CITE**  
**Audited file:**
`MATH_THEOREM_RAW_SWITCH_FOUR_ROLE_COEFFICIENT_AND_UNANCHORED_CHANGE_OBSTRUCTION_20260806.md`  
**Audited SHA-256:**
`57a0c4ac657ef13228a1afc053836fc4a95ff90c423bb9e1d7dbea61f5dec4fb`

The audited bytes retain the candidate argument but now prepend an explicit
`UNVERIFIED CANDIDATE -- DO NOT CITE` warning and point to a separate
composite-switch reduction.  The warning agrees with this audit.

The rewrite correctly repairs two defects of the retracted first draft: it
does not discard changed resources missed by the first blocker, and it does
not assume that a fixed root is invariant under a coordinate transposition.
Its load-bearing coefficient (2.5), however, is not a coefficient of the
actual stopped operator.

## 1. The actual operator has no independent candidate `C`

The parent joint-Lyapunov note defines the row set of the stopped incidence
operator explicitly.  At a fixed state,

\[
 \mathfrak A_i\ni A=(Q,E,F),\qquad
 \mu_A=c_i(Q,E,F)R_i(E,F;Q),
\]

and

\[
 (K_Tf)(A)=\sum_{x\in U_A^\circ\cap T}f_x.
\]

Thus a switch candidate for this operator is the **composite row**
`A=(Q,E,F)` (or a specified component switch inside that row).  There is
no additional independently sampled atomic edge `C` with coefficient

\[
                         \gamma_i(C)={a_C(i)\over X(i)}.
\]

This leaves three possible interpretations, all incompatible with (2.5).

1. If `C` means the composite row `A`, then `a_C` is undefined: `A` is not
   an atomic clock edge.
2. If `C` means one of `E,F`, its atomic rate is already present in
   `c_i(Q,E,F)` through `xi_E xi_F`; multiplying by `gamma_i(C)` counts
   that candidate a second time.
3. If `C` is a genuinely independent atomic edge, it does not index a row
   of `K_T` and its square difference is not the stopped boundary term
   appearing in `(JSEC)`.

Therefore the assertion that

\[
 \kappa_k{a_G\over X}\gamma_i^+(C;G)c_iR_i
\tag{A1}
\]

is the **true expected bare coefficient** is false under every available
interpretation.  No expansion of the actual Bellman payment is supplied
which produces (A1).

This is the same algebraic-degree diagnostic recorded in Proposition 5.2
of the joint-Lyapunov note.  The stopped scalar numerator is fourth order
because two rows `A,A'` each already contain a future pair.  Introducing a
new independent `C` changes rather than resolves that degree structure.

## 2. The valid switch must transport the composite row

For a literal coordinate transposition the natural complete-orbit move is

\[
 (Q,E,F)\longmapsto(\tau Q,\tau E,\tau F).
\tag{A2}
\]

Alternatively one must specify and derive a switch of one component of
the row while holding the others fixed.  In either case the proof must
start from `mu_A(K_Tf)(A)^2`, not from an independent `gamma_C` average.

The rewrite's statement that root transport is harmless is directionally
correct, but it does not define the stopped availability of the composite
row, its first blocker, or the equality/inequality between the two actual
row coefficients `mu_A` and `mu_(tau A)`.  Atomic equality
`a_C=a_(tau C)` does not fill this gap.

## 3. Summing out `G` cannot repair an incorrect coefficient

The inequality

\[
 \sum_{G:\text{boundary birth}}{a_G\over X}\le1
\]

is correct.  The one-birth lemma and
`kappa_k=1/binom(k,2)` also correctly prevent a raw time/transposition
occupation factor **once a valid boundary summand has been derived**.

But applying these facts to (A1) only bounds the invented four-role
quantity.  It does not turn it into the boundary of the three-index row
`A=(Q,E,F)`.  The four-to-three collapse in (3.2) therefore has no
implication for `(JSEC)`.

## 4. Full changed-set polarization is conditionally sound but unattached

Sections 4--5 improve on the retracted draft by retaining the full changed
set and using

\[
 \|Z_C-Z_{\tau C}\|_R^2
 \le2\|Z_C\|_R^2+2\|Z_{\tau C}\|_R^2.
\]

As an abstract inequality this is valid.  It would be useful after a
correct operator row and coefficient were fixed.  In the present proof the
two shores are indexed by the nonexistent independent row `C`, so the
polarization is not yet an expansion of the actual Bellman term.

There are two further normalization gaps even conditionally.

### 4.1 Occurrences versus resource vertices

`(FE3.3)` uses

\[
 j(H;E,F)=|H\cap(E\cup F)\cap
   (\mathcal L\mathbin{\dot\cup}\mathcal R)|,
\]

a count of resource vertices in a hyperedge.  Equation (5.3) instead uses
a multiset of literal occurrences.  Equality requires a proof that the
candidate word is resource-simple on every counted type, or an
occurrence-labelled version of `(FE3)`.  The rewrite explicitly declares
the occurrence multiplicity load-bearing but supplies neither statement.

### 4.2 The time-to-kernel identity is omitted

To derive (5.5), one must write the complete identity taking

\[
 \sum_i {a_H(i)\over X(i)}c_i(Q,E,F)R_i(E,F;Q)
\]

to

\[
 \omega_E\omega_F\omega_Hp_*^{-m(E,F;Q)}
 {j(H;E,F)\choose2}K_{p_*}(j).
\]

The global-rate reconstruction makes this plausible for a genuine atomic
third edge `H`, but it does not identify the invented `C` with such a row
of the actual operator.  The displayed conclusion (5.5) is asserted rather
than derived with the `p`, `p_s`, `X`, one-step, and time-multiplicity
factors.

## 5. The one-entry scale would be absorbable, but is not proved here

Retaining the full changed shore can create `O(d)` diagonal one-entry
terms.  If each had a valid injection into `(ROc)`, their total factor
would be

\[
 O(d)\,{C\over p d^2}=O(1)
 \qquad(p\ge c/d).
\]

Thus an `O(d)` multiplicity is not by itself fatal: it is absorbable as a
constant multiple of the static `S_2=O(M/d^4)` budget.  The rewrite says
instead that the occurrence sum is already inside the rooted
normalization, without displaying either this `O(d)` calculation or the
literal rooted tuple map.  Hence even this otherwise plausible row remains
unproved.

The marked size-two/three statement is also only asserted in one sentence.
Transporting `Q` is not a replay of the cluster normalization, especially
when the switch acts on a component rather than the whole composite row.

## 6. Consequence

The corrected note does **not** establish

\[
 V(S_0)=O(M/d^4),
 \qquad
 \mathbb E(B_0+B_1)=O(M/d^2).
\]

The raw Johnson-switch coefficient row remains open.  A valid next proof
must begin by expanding the actual row

\[
             \mu_A(K_Tf)(A)^2,
             \qquad A=(Q,E,F),
\]

under a precisely defined composite or one-component coordinate switch.
Only after that expansion may the first blocker be summed out and the
full changed-resource energy be compared with `(ROc)` and `(FE3)`.

Until that derivation is supplied, Sections 3--6 of the audited theorem are
**DO NOT CITE**.
