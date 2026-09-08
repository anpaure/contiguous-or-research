# Positive-density typed wedge baselines survive bounded layer energy

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional menu-stability theorem.  It shows that the typed
prospective atlas need only have fixed positive density, not near-full
density.  The current construction still has to prove that its prospective
coatom/turn certificates form one completion-stable typed baseline and that
the resulting state regenerates.

## 0. Setting

Fix distinct lower turns `L_1,...,L_p` with

\[
 p\le\left\lfloor{m+1\over4}\right\rfloor.
\]

For source `i`, let `T_i` be a prospective baseline menu of full wedges.
Every wedge in `T_i` carries one distinguished owner side certified to be:

1. typed and legal in one fixed cap/guard/phase state;
2. stable under the unprotected part and orientation of any compatible
   factor completion containing the wedge; and
3. private from every other owner/terminal-distinct selected certificate,
   apart from explicitly priced dynamic resources.

The baseline is chosen before the frozen dynamic background is applied.
After that background is fixed, let `A_i subseteq T_i` be the surviving
active menu and put

\[
                         ell_i=|T_i\setminus A_i|.
\tag{0.1}
\]

Assume every baseline has already discarded wedges whose two incidence
edges are not degree-compatible with the incumbent protected bank `P_*`,
and that

\[
                         |P_*|+2p\le m-2.
\tag{0.1a}
\]

Because the selected wedges will have distinct lower turns and globally
distinct owners, individual compatibility with `P_*` implies compatibility
of their union.  Equation (0.1a) is the protected-factor edge budget; typed
menu abundance does not imply either premise.

Define the active cycle-alignment threshold

\[
 K_p=B_{p-1}(m)+2(p-1).
\tag{0.2}
\]

## 1. Exact casualty bound from total dynamic loss

### Theorem 1.1

Let

\[
 M_*:=\min_i|T_i|,
 \qquad
 L:=\sum_i\ell_i.
\]

If `M_*>K_p`, then all but at most

\[
 \boxed{
 C_{\rm typed}
 =\left\lfloor{L\over M_*-K_p}\right\rfloor
 }
\tag{1.1}
\]

sources satisfy `|A_i|>K_p`.  The retained sources therefore admit the
complete active-wedge--Hamilton-linkage--protected-factor materialization
under (0.1a).

#### Proof

A bad source has

\[
 |A_i|\le K_p,
\]

and hence

\[
 ell_i=|T_i|-|A_i|\ge M_*-K_p.
\]

Summing this inequality over the bad sources proves (1.1).  For the
retained smaller family the required active-cycle threshold is no larger
than `K_p`, so the active cycle-aligned theorem applies.  \(\square\)

This result counts only losses relative to the typed baseline.  Wedges
which were never typed members of `T_i` cost nothing.

## 2. Dynamic layer-energy bound

Suppose dynamic unavailability at source `i` is described by:

- an owner-side set `R_i` of size `r_i`;
- a q1-terminal pair set `S_i`; and
- an explicitly priced hidden dynamic pair set `H_i`.

Assume every lost baseline certificate lies in

\[
 W_i(R_i)\cup S_i\cup H_i,
\tag{2.1}
\]

where `W_i(R_i)` is the set of baseline wedges whose distinguished typed
owner side lies in `R_i`.  Since one owner side belongs to at most `m-1`
full wedges,

\[
                         |W_i(R_i)|\le(m-1)r_i.
\tag{2.1a}
\]

Put

\[
 I=\sum_i r_i,
 \qquad
 J=\sum_i\bigl(|S_i|+|H_i|\bigr).
\tag{2.2}
\]

Then

\[
\begin{aligned}
 L
 &\le(m-1)\sum_i r_i+J\\
 &=(m-1)I+J.
\end{aligned}
\tag{2.3}
\]

Combining (1.1) and (2.3) gives the exact bound

\[
 \boxed{
 C_{\rm typed}
 \le
 \left\lfloor{(m-1)I+J\over M_*-K_p}\right\rfloor.
 }
\tag{2.4}
\]

If every baseline wedge has both owner sides typed and remains usable when
at least one side survives, replace `W_i(R_i)` by `C(R_i,2)`.  Then the
sharper numerator `C(I,2)+J` from the two-sided theorem is valid.  The main
statement deliberately allows only one distinguished typed side and hence
uses the linear star loss `(m-1)I`.

## 3. Fixed-density corollary

### Corollary 3.1

Fix positive constants `alpha,A,D,C`.  Suppose

\[
 |T_i|\ge\alpha m^2,
 \qquad
 p\le C\sqrt m,
 \qquad
 I\le Am,
 \qquad
 J\le Dm^2.
\tag{3.1}
\]

Then, for all sufficiently large `m`, all but at most

\[
 \boxed{
 \left\lfloor{2(A+D)\over\alpha}\right\rfloor
 }
\tag{3.2}
\]

sources have active menus above `K_p` and admit the complete active
cycle-aligned factor materialization.

#### Proof

Since `p=O(sqrt(m))`,

\[
 K_p=O(pm)=O(m^{3/2})=o(m^2).
\]

Therefore eventually

\[
 M_*-K_p\ge{\alpha m^2\over2}.
\]

Also

\[
 (m-1)I+J
 \le(A+D)m^2.
\]

Substitute these two rows into (2.4).  \(\square\)

The constant is deliberately coarse.  The exact formula (2.4) retains the
actual baseline floor and dynamic energy.

## 4. Why this is weaker than the former hidden-hole invariant

A baseline of density `alpha` may omit a fixed positive fraction of all
`C(m,2)` wedges at every source.  Across `p=Theta(sqrt(m))` sources, counting
those static omissions as hidden holes would cost `Theta(m^(5/2))` and fail
the previous aggregate `O(m^2)` row.

Theorem 1.1 does not charge them.  It requires only:

1. `Theta(m^2)` completion-stable typed certificates per source before the
   dynamic background; and
2. `O(m^2)` total additional loss from owner, terminal and hidden dynamic
   resources.

Because the required selection threshold is only `O(m^(3/2))`, this leaves
quadratic slack at every nonexceptional source.

## 5. Interface with owner-area rounding

If the frozen dynamic background is obtained from a one-state fractional
current of owner load `O(m)`, the min-cost owner-area theorem gives an
integral background with linear owner projection.  Its ordinary q1
projection is quadratic, modulo the terminal-only exception bank.

The audited owner/terminal incidence estimates then give

\[
                         I=O(m),\qquad J=O(m^2),
\]

provided separately priced dynamic hidden losses are also quadratic.
Corollary 3.1 consequently leaves only an absolute typed-wedge sidecar.

This produces the proof-safe chain

\[
 \begin{gathered}
 \text{positive-density completion-stable typed atlas}\\
 +\ \text{one-state fractional owner current of load }O(m)\\
 \Longrightarrow\ \text{bounded active-linkage-factor casualties}.
 \end{gathered}
\tag{5.1}
\]

No per-path monotonicity, full typed wedge menu, or pre-materialized factor
occurrence atlas is required.

## 6. Regenerative positive-density target

For an additive-constant induction it is sufficient that every same-parity
transition export, with uniform constants:

1. a prospective typed baseline satisfying `|T_i|>=alpha m^2`;
2. a one-state fractional background current of owner load at most `Am`;
3. at most `Dm^2` terminal-only and dynamic hidden loss energy;
4. the active cycle-aligned protected-factor edge budget; and
5. a fresh child state of the same kind, not the union of all ancestral
   footprints.

Together with the remaining upper, residence, topology, compiler and
two-coordinate product rows, this target implies `nu(k)<=B(k)+O(1)`.

## 7. Exact scope

The theorem does not construct the positive-density typed atlas.  In
particular, a prospective algebraic menu before the host/off-state is fixed
cannot be cited unless its certificates are selected jointly with that host
and remain valid after factor completion.

It also does not prove the one-state fractional owner current, bound
terminal-only exceptions, or establish regeneration.  Separate phase
currents and marginal type counts do not satisfy the hypotheses.

## 8. Dependencies

- `MATH_THEOREM_ACTIVE_CYCLE_ALIGNED_WEDGE_LINKAGE_AND_LAYER_ENERGY_20260804.md`
- `MATH_THEOREM_MIN_COST_OWNER_AREA_ROUNDING_AND_Q1_PROPAGATION_20260804.md`
- `MATH_THEOREM_TWO_LAYER_FOOTPRINT_GIVES_BOUNDED_WEDGE_DEFECT_20260804.md`
