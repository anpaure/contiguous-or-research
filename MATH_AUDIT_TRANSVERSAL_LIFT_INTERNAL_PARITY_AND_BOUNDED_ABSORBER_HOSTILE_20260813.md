# Hostile audit: transversal-lift parity and the bounded pair-cell absorber question

**Date:** 2026-08-13  
**Verdict on the audited parity theorem:** **PASS as a necessary obstruction,
but materially nonsharp.**  The proof of its stated parity implication is
correct.  Its suggested bounded conformal escape does not survive the full
incidence audit, and the fixed pair structure actually forces exponentially
many nonlift cross-cell edges.

**Audited source:**
`MATH_OBSTRUCTION_TRANSVERSAL_LIFT_PLUS_INTERNAL_PAIR_CELL_FACTOR_HAS_INFINITE_PARITY_FAILURE_20260813.md`  
**Audited source SHA-256:**
`6c2750503dd3aed8009d879782ecab5454aa046d52738d670f68b727d5166d2e`

**Strengthened theorem:**
`MATH_THEOREM_PAIR_CELL_PARITY_CHARGE_TRIANGLE_AND_EXPONENTIAL_CROSS_EDGE_LOWER_BOUND_20260813.md`  
**Strengthened theorem SHA-256:**
`f89034566a28883910566016cff373166ef80131cba894c44b4e269b6f241f78`

**Verifier:** `verify_pair_cell_parity_charge_triangle.py`  
**Verifier SHA-256:**
`2e143f89219877d8c057f9c91311fdff34de7d51c4797835c0430bf3e529bbdf`

## 1. Hostile replay of the parity proof

The exact residual selection system is correctly formulated.  A residual
internal edge of colour `L` is uniquely of the form

\[
 \{L\cup\{a_i\},L\cup\{b_i\}\}
\]

for an empty pair `P_i`, and every nontransversal lower colour has at least
one such option.  The transversal lift saturates each of its owners to degree
two, so all residual owner capacities are zero or two.

For a fixed `a_i`, summing residual degrees over owners containing `a_i`
has even right side.  An internal direction-`i` edge contributes once and
every other internal direction contributes zero modulo two.  Hence each
direction count is even.  Their sum is the residual colour count
`W-2^p`.  Lucas's theorem gives

\[
 \binom{2p+1}{p+1}\equiv1\pmod2
 \quad\Longleftrightarrow\quad p=2^s-1,
\]

so the contradiction is valid for the claimed infinite sequence.  No Gray
direction-balance assumption is hidden in this subtraction.

## 2. The missing stronger obstruction

The same residual equations already contain a simpler owner-row failure.
An owner with no singleton matched pair lies in a `Q_0` pair cell and is
incident with no internal edge.  It is not a lifted owner, since every lifted
owner has `p-1` singleton pairs.  Its residual degree equation therefore has
left side zero and right side two.  Thus an all-internal residual completion
fails for every `p>=3`, not only for the Lucas sequence.

More quantitatively, a `Q_0` owner needs two cross incidences and a `Q_1`
owner needs at least one, because a simple factor can use its unique internal
edge at most once.  If `C_res` is the nonlift cross-edge bank, then

\[
 2|C_{\rm res}|\ge2N_0+N_1.                            \tag{2.1}
\]

For odd `p`, direct occupancy counting gives

\[
 N_0=\binom p{(p-1)/2},\qquad
 N_1=2p\binom{p-1}{(p-1)/2},                           \tag{2.2}
\]

and hence

\[
 \boxed{
 |C_{\rm res}|\ge
 \binom p{(p-1)/2}+p\binom{p-1}{(p-1)/2}
 =\Theta(\sqrt p\,2^p).}                              \tag{2.3}
\]

This lower bound applies in particular to every `p=2^s-1`.  Therefore a
bounded cross-cell bank cannot make the remaining fixed-structure edges
internal in a global exact factor.

## 3. Exact answer to the trade question

For an edge which exchanges `u,v`, define the vector

\[
 \alpha_i=\mathbf1_{\{a_i\in\{u,v\}\}},
 \qquad \eta=1+\sum_i\alpha_i\pmod2.                  \tag{3.1}
\]

Every exact residual factor obeys `sum alpha=0`.  On the Lucas sequence it
also obeys `sum eta=1`.  Internal edges have `eta=0`; the parity-active cross
classes are exactly

\[
 \{a_i,a_j\},\qquad \{b_i,b_j\}\quad(i\ne j),
 \qquad \{z,b_i\}.                                    \tag{3.2}
\]

If two relative configurations use the same colours and have the same owner
degree vector, their sums of `alpha` agree by the coordinate-cut identity.
They also have the same number of edges, so their sums of `eta` agree.  Thus:

\[
 \boxed{
 \text{no owner/lower-conformal relative trade of any size changes the
 parity charge.}}                                      \tag{3.3}
\]

This is an impossibility theorem, not a failure to find a small example.

There is nevertheless a smallest **closed carrier** for the parity bit.
Choose `a_1,a_2,a_3` from distinct pairs, choose a `(p-1)`-set `B` disjoint
from them and containing `z`, put

\[
 U=B\cup\{a_1,a_2,a_3\},\qquad T_i=U-\{a_i\},
\]

and use the triangle on `T_1,T_2,T_3`.  Its three colours are the three
pairwise intersections.  They are distinct, every owner has degree two,
all three edges are cross-cell with `eta=1`, and the bank is disjoint from
the lift because all its owners and colours contain `z`.  A simple closed
factor bank cannot have one or two edges.  Every lower-injective Johnson
triangle is of this bottom form, so three is the exact minimum.

Freezing the triangle changes the complement colour count from odd to even
and removes the scalar parity contradiction.  It is not a conformal switch
from internal edges, does not solve the remaining exact-cover equations, and
does not evade `(2.3)`.

## 4. Verifier replay and scope

The command

```text
python3 verify_pair_cell_parity_charge_triangle.py
```

returned `PASS`.  It checked `p=3,4,5,7`; verified the reflected-Gray lift,
the exact internal degree `m(T)` of every owner, the `N_0,N_1` formulas, the
canonical triangle incidences and parity signatures, and disjointness of the
triangle from the lift.  It also exhaustively classified all Johnson triangles
at `p=3`:

\[
 350\text{ Johnson triangles},\qquad
 210\text{ lower-injective bottom triangles},\qquad
 120\text{ all-cross bottom triangles}.
\]

The resulting nonlift cross-edge lower bounds were `9` at `p=3` and `175`
at `p=7`, matching `(2.3)`.

The verifier is a finite identity checker.  It is not a SAT/ILP proof of a
residual completion, a chronology test, an upper-support check, or an
asymptotic substitute for the written proofs.

## 5. Frozen prerequisite ledger

| Role | File | SHA-256 |
|---|---|---|
| transversal lower obstruction and lift | `MATH_THEOREM_PAIR_CELL_TRANSVERSAL_LOWER_OBSTRUCTION_AND_LONG_RUN_EDGE_LIFT_ABSORBER_20260813.md` | `7dd84b2dbd830f0a52b772a02467e15b92f5c52cc8f99e3f63a8d0a4dcafb852` |
| coloured owner/lower factor gate | `MATH_REDUCTION_PAIR_CELL_CYCLES_VERSUS_PROTECTED_MSW_ROWS_EXACT_COLORED_F_FACTOR_GATE_20260813.md` | `742b63d17c0c092557483066c81ee4aecfff95cfe4d7e5beab18a204bebcfdcb` |
| arbitrary transversal-lift extension | `MATH_THEOREM_PAIR_CELL_TRANSVERSAL_LIFT_EXTENDS_TO_EXACT_OWNER_LOWER_FACTOR_20260813.md` | `29ad86c5c2e1c9052e37721441e20da974bb331ea140181c74c7024b8313bd14` |
| pair-cell occupancy and low-cell leave | `MATH_THEOREM_PAIR_CELL_LONG_RUN_Q_WINDOW_CLOCK_EXPLICIT_LEAVE_AND_EXACT_SPLICE_CAP_20260813.md` | `32640d876fb9f1e7f28758a22c238723a2fd76d43f12de64473de94e59f9098d` |

The strengthened result is compatible with arbitrary protected-Ore
extension: that theorem permits many cross-cell edges.  It rules out only
the much stronger hope that the lift plus `O(1)` cross-cell repairs and an
otherwise fixed-pair internal factor could be exact.

