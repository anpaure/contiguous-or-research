# Audit: weakest even-terminal tap and closed-splice parity toll

**Date:** 2026-08-04  
**Scope:** pure mathematics only; no computation, solver output, or search
evidence.

## 0. Frozen theorem and verdict

The audited theorem is
`MATH_THEOREM_WEAKEST_EVEN_TERMINAL_TAP_AND_CLOSED_SPLICE_PARITY_TOLL_20260804.md`
at SHA-256

```text
d704f94ea276934f0b9fba4d4b6e58a3757d97110805338cd40cc284c699144e
```

Verdict: **GO as an exact conditional implication and charge ledger**.
It proves no even-tap existence theorem and no new bound on `nu(k)`.

The theorem correctly separates three assertions.

1. One bounded-charge even terminal certificate on every state of one
   selected compatible odd spine is sufficient; an even regenerative chain
   is unnecessary.
2. The closed splice has an unbounded even parity toll
   `chi_K=2d_(K-1)-d_K` and therefore is not such a bounded-charge tap.
3. The even bilayer router and boundary formulas are conditional resources,
   not a terminal word or a chronology-existence theorem.

## 1. Terminal-charge audit

For a fixed scaffold `Z` in dimension `k`, let

\[
 c=|Z|-B(k),
 \qquad \tau=c+R({\cal H}(Z)).                       \tag{1.1}
\]

The shortest repair word may be appended as a new terminal block.  Every
previous witness remains in the unchanged prefix, while every member of
`H(Z)` has a witness wholly in the repair block.  Hence the final physical
length is exactly

\[
                      B(k)+\tau.                     \tag{1.2}
\]

No compiler deficit, dummy port, or owner-surplus count is subtracted from
this identity.  This verifies the charge convention.

Under the current `c>=0` scaffold convention, the integers `c,R>=0` obey

\[
                       c+R\le1                       \tag{1.3}
\]

exactly in the three cases `(0,0)`, `(0,1)`, and `(1,0)`.  A one-letter
repair word has only one nonempty interval, so the `(0,1)` case can repair
at most one distinct omitted target.  If `c=1`, (1.3) forces `R=0`, hence
the omitted family is empty.  This confirms the theorem's distinction
between a `B+1` pivot scaffold and a separate length-`B` even tap.

## 2. Quantifier and compatibility audit

The sufficient outer quantifier is

\[
 \exists(g_m,O_m,E_m)_{m\ge m_0}\quad\forall m\ge m_0, \tag{2.1}
\]

where the `g_m` form one compatible odd path.  Applying (1.2) to `O_m`
and `E_m` separately gives

\[
 \nu(2m+1)\le B(2m+1)+q_o,
 \qquad
 \nu(2m+2)\le B(2m+2)+q_e.                           \tag{2.2}
\]

Thus the all-dimensional constant is `max(q_o,q_e)`, not their sum.  The
even terminal repair is not exported and is not paid at the next level.
For the sharp constant one, any finite prefix before the spine starts must
be checked at `B+1` separately; it cannot be hidden by enlarging the
constant while retaining the same sharp statement.

The following stronger conditions are not used:

* a tap on every admissible state;
* compatibility between taps at different levels;
* one common odd/even terminal chronology, cap, or compiler;
* an even successor state or an even same-parity induction; or
* zero terminal defect when only an additive-constant conclusion is sought.

The meeting condition is exact: an even tap may choose its own terminal-only
data, but any choice that changes the persistent source or exported child
must be bundled into the odd arrow.  Separate existential witnesses on a
shared persistent choice would not establish (2.1).

Calling this the “weakest tap” is scoped to a tap-decorated odd-spine
architecture.  Independent even certificates unrelated to `g_m` would be
logically weaker still, but their existence is precisely the independent
even upper-bound problem and supplies no transition mechanism.

## 3. Closed-splice arithmetic audit

Let `K` be even and let `X` be a universal word on `K-1` coordinates with

\[
                        |X|=B(K-1)+q.                 \tag{3.1}
\]

The self-splice theorem gives a universal `K`-coordinate word of length
`2|X|`.  Since

\[
 w_K={K\choose K/2}
     =2{K-1\choose K/2}=2w_{K-1},                    \tag{3.2}
\]

its excess is

\[
 \begin{aligned}
 2|X|-B(K)
 &=2(w_{K-1}+d_{K-1}+q)-(w_K+d_K)\\
 &=2q+2d_{K-1}-d_K.                                  \tag{3.3}
 \end{aligned}
\]

The proved even depth dichotomy

\[
                  d_K\le d_{K-1}\le d_K+1           \tag{3.4}
\]

has only two integral cases.  Therefore

\[
 \chi_K:=2d_{K-1}-d_K
     =d_K\quad\hbox{or}\quad d_K+2.                  \tag{3.5}
\]

The established asymptotic `d_K=sqrt(pi K/8)+O(1)` makes `chi_K`
unbounded.  Hence even `q=0` gives only `B(K)+Theta(sqrt K)` through the
unmodified splice.  This disproves the *implication from the splice*, not
the existence of some unrelated constant-additive even word.

If the odd terminal scaffold first needed repair charge `tau_o`, the
repaired odd word has `q=tau_o`; splicing that actual word counts its repair
positions twice.  The theorem correctly treats any avoidance of this
duplication as part of a later physical saving, rather than erasing it from
the baseline.

## 4. Net-saving sign audit

Let the proposed tap word `Y` have signed physical saving

\[
                         s=|S_z(X)|-|Y|.              \tag{4.1}
\]

Using (3.3),

\[
 |Y|=B(K)+2q+\chi_K-s.                               \tag{4.2}
\]

If its exact omitted family is `H`, appending a shortest repair word gives

\[
 |Y|+R({\cal H})
  =B(K)+2q+\chi_K-s+R({\cal H}).                     \tag{4.3}
\]

Thus this construction has length at most `B(K)+Q` exactly when

\[
                    s-R({\cal H})
                    \ge2q+\chi_K-Q.                 \tag{4.4}
\]

The signs and sharp specializations are:

\[
\begin{array}{c|c}
\text{input and requested output}&\text{required net saving}\\ \hline
q=1,\ Q=1&s-R({\cal H})\ge\chi_K+1,\\
q=0,\ Q=1&s-R({\cal H})\ge\chi_K-1,\\
q=O(1),\ Q=O(1)&s-R({\cal H})\ge\chi_K-O(1).
\end{array}                                           \tag{4.5}
\]

These are identities for a materialized `Y`.  They do not assert that a
subsequence, collar, owner rethread, or even diagonal row meeting them
exists.

## 5. Even-bilayer nonpromotion audit

For `K=2r`, the conditional bilayer theorem starts with a cyclic literal
diagonal owner row already enumerating all `W=binom(2r,r)` owners.  If its
lower q1 row is surjective, it has `W-C_r` distinct lower target values and
`C_r=W/(r+1)` occurrence-labelled dummies.  After linearization there are
`W+1` physical lower ports, forcing at least `C_r+1` unused lower-port
cells in an injective exact-lower compiler.

The zero-overload two-phase router additionally assumes one compatible
unused typed socket per owner.  Neither the row nor those sockets are
constructed.  The safe opening and typed terminal cut are also conditional
on the fixed face and resource semantics.  In particular:

\[
 \text{conditional dummy/slack count}
 \not\Longrightarrow
 \text{physical saving }s,                            \tag{5.1}
\]

and

\[
 \text{zero-overload addressed router}
 \not\Longrightarrow
 \text{complete even terminal certificate}.          \tag{5.2}
\]

The theorem under audit therefore does not promote conditional even
chronology accounting to existence.

The one-pivot fixed-fibre component-parity invariant is also scoped
correctly.  Closed `C6` switches preserve parity on that frozen fibre, but
a fresh host or an authenticated odd actuator lies outside the obstruction.
It is not a global parity no-go for even taps.

## 6. Final scope

The exact proof-safe frontier is:

* `tau_ev<=1` is sufficient for an all-dimensional `B+1` conclusion once
  the compatible odd `B+1` spine exists;
* `sup tau_ev<infinity` is sufficient for `B+O(1)` once the bounded-charge
  odd spine exists;
* an unmodified closed splice has charge `2q+chi_K` and fails the latter
  test because `chi_K` is unbounded; and
* the existing even bilayer and boundary ledgers do not prove the missing
  even certificates.

Accordingly the frozen theorem is a rigorous implication/obstruction
ledger with no existence overclaim.

## 7. Audited dependency digests

```text
072daa9a76e4d2fccb9fa39f5bb59f3c90e0012147ea871d14ebde18d45cc9e6  MATH_THEOREM_EVEN_DIAGONAL_BILAYER_LITERAL_ROUTER_AND_BOUNDARY_LEDGER_20260803.md
2635e32142db89714177e0b017a5f98d2e20fb91e11864cf22905b4ec40efcdd  MATH_THEOREM_BPLUS1_ONE_TOKEN_REGENERATIVE_OVERLAY_AND_FIXED_FIBRE_OBSTRUCTION_20260803.md
0959212ab0d1b945b560ee578b856304496aaec0cddd116d755b031b7ee3ab77  MATH_SYNTHESIS_EXACT_B_BPLUS1_ZERO_CHARGE_COINSTANTIATION_20260803.md
67a6ffaf8e3a193b654ae2faa0cef5963274be811bec233d37e0cb2a4beffaaa  MATH_THEOREM_R_EVEN_CLOSED_SPLICE_THREE_DELETION_AND_18CELL_COLLAR_20260731.md
659779fbf1236344a84734ec01b36de50b75a351e7e57f3646946b96eb9118d0  MATH_THEOREM_EVEN_SPLICE_EXCESS_TWO_RANK_CARRIER_GATE_20260731.md
25bca7bdaba8ce5ec9334fcd74cbfaf71874e7d5f43e4d1764ade0d467d426e2  MATH_THEOREM_UNIFORM_COINSTANTIATED_BOUNDED_CHARGE_RESET_SPINE_REDUCTION_20260803.md
a07ac985c4d2c28918efe09db311f463bcf461f0d5999edb85536bc3d9a875c6  MATH_THEOREM_EQUIVARIANT_SAME_PARITY_TAP_DECORATED_ORBIT_FLOW_INDUCTION_20260803.md
```
