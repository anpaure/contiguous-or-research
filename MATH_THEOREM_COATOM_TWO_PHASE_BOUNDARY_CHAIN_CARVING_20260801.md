# Prepared coatom endpoints carve both phase-swapped lower chains exactly

Date: 2026-08-01  
Lane: boundary-chain exterior return bank for the endpoint-planted coatom packet  
Status: exact local two-phase antecedent theorem and exact scope boundary.  This
does **not** prove that the prepared endpoint blocks occur in every recursive
host, nor that the unused `q1` address is a programmable packet-task socket.

## 0. Result

Endpoint containment by itself is not enough to carve a nested lower chain.
The missing condition is a coordinatewise trace condition: the coordinate
first appearing in the prefix of length `h` must survive through carrier
owner `h-1`.

The coatom endpoint order supplies exactly that trace.  Consequently, if a
carrier has the prepared coatom fragments described below at its two global
ends, then its maximal erosion can be replaced at the boundary so that, in
one literal common-cap word,

\[
 L_h^0=B_1\cup\{f_1,\ldots,f_h\},\qquad
 L_h^1=B_0\cup\{f_1,\ldots,f_h\},
\]

and

\[
 R_h^0=B_0\cup\{f_{d-h+1},\ldots,f_d\},\qquad
 R_h^1=B_1\cup\{f_{d-h+1},\ldots,f_d\}.                 \tag{0.1}
\]

for every `1<=h<=d-1`.  Both phase words still satisfy `D^d A^epsilon =
T^epsilon` exactly.  Thus the two global boundary banks give literal return
columns for all `2(d-1)` deep old/new chain targets.  This is not merely a
cap-containment or marginal-Hall statement.

There are two useful choices at `h=d`.

1. **Native-`q1` duplicate.**  The boundary value is the corresponding
   native packet `q1` target.  If the native `q1` hinge is used in the
   compiler matching, one boundary address on each shore may be left unused.
2. **Fresh-`q1` transport.**  Replace the last endpoint filler by a fresh
   coordinate.  The same proof transports a new phase-swapped `q1` pair,
   but the boundary address is then consumed by that target.

The first alternative gives an unused **matching address**, not yet a free
programmable hard-task socket.  Its source positions overlap the deep chain
cells and its exact cap is fixed.  A packet task can use it only after a
separate trace-guard check says that this fixed address is an admissible
representative.

There is nevertheless one unconditional matching consequence.  For a
single packet, combine its native deep cells with these boundary cells.  In
phase zero match the native cells to the phase-zero chain targets and the
boundary cells to the phase-one chain targets; in phase one swap those two
assignments.  Both matchings are literal in their respective antecedents.
Thus the one-packet deep return deficiency is zero under the
**terminal-state** quantifier.  This is not one matching common to both
phases, and it does not give disjoint global boundary banks for an
unbounded number of simultaneous packets.

## 1. One exact left boundary

Fix `d>=2`.  Let

\[
 F=\{f_0,f_1,\ldots,f_d\},
\]

and let `C` be disjoint from `F`.  Choose two bases `B_0,B_1 subseteq C`.
Suppose the first `d+2` carrier owners are

\[
 T_i=C\cup(F-\{f_i\})\quad(0\le i\le d),\qquad
 T_{d+1}=(C-\{z\})\cup F                                  \tag{1.1}
\]

for some `z in C`.  These owners form a Johnson path: the first `d` steps
exchange consecutive omissions and the last step inserts `f_d` while
deleting `z`.

Let `P` be the maximal depth-`d` erosion of the whole carrier,

\[
 P_j=\bigcap_{\max(0,j-d)\le i\le\min(j,N-1)}T_i.          \tag{1.2}
\]

Assume `P_j` is nonempty, as it is whenever the carrier has a nonzero
depth-`d` antecedent.  For `epsilon in {0,1}`, define

\[
\begin{aligned}
 A_0^\epsilon&=B_\epsilon\cup\{f_1\},\\
 A_j^\epsilon&=\{f_{j+1}\} &&(1\le j\le d-2),\\
 A_{d-1}^\epsilon&=\{f_d\},\\
 A_d^\epsilon&=C,\\
 A_j^\epsilon&=P_j &&(j\ge d+1).
\end{aligned}                                               \tag{1.3}
\]

### Theorem 1.1 (trace-exact left transporter)

For both phases,

\[
                         D^dA^\epsilon=T.                    \tag{1.4}
\]

Moreover, for every `1<=h<=d`, the global left boundary cell in row
`D^(h-1) A^epsilon` has the literal value

\[
       \bigcup_{j=0}^{h-1}A_j^\epsilon
          =B_\epsilon\cup\{f_1,\ldots,f_h\}.                \tag{1.5}
\]

All values (1.5) coexist in the same antecedent.  In particular, their
common-cap compatibility is proved by the word itself.

#### Proof

For `0<=j<=d`, direct intersection of (1.1) gives

\[
       P_j=C\cup\{f_{j+1},\ldots,f_d\}.                      \tag{1.6}
\]

Hence every replacement in (1.3) is a nonempty subset of `P_j`.  Therefore
`D^d A^epsilon subseteq D^dP=T`; no carrier coordinate can be introduced.

At owner zero, the window `A_0,...,A_d` contains `C` from `A_d` and each
of `f_1,...,f_d` once.  Its union is exactly `T_0`.

Fix `1<=i<=d`.  The source `A_d=C` lies in the owner-`i` window and supplies
all of `C`.  If `j>i`, then `f_j` is supplied by `A_(j-1)`, which lies in
that window.  The coordinate `f_i` is absent from every source in the
window, because each such source is contained in `T_i` and `T_i` omits
`f_i`.  Finally, if `j<i`, maximal erosion reconstructs `f_j in T_i` from
some `P_s` with `i<=s<=i+d`.  No `s<=d` can contain `f_j`, by (1.6), since
`s>=i>j`.  Thus that witness has `s>=d+1` and was not changed in (1.3).
The identical argument applies to `f_0`.  Hence the owner-`i` union is
exactly `T_i`.

Every later carrier window starts after source position `d`, so it is
unchanged from the maximal erosion.  This proves (1.4).  Formula (1.5) is
the direct union of the first `h` displayed sources.  \(\square\)

The proof explains why `A_d=C` is useful: the phase changes only `A_0`.
No phase-dependent compensating active letter is needed at source `d-1`.

## 2. The mirrored right boundary

Apply Theorem 1.1 to the reversed carrier.  Relabel its local fillers by

\[
       g_0=f_0,\qquad g_i=f_{d+1-i}\quad(1\le i\le d).       \tag{2.1}
\]

Thus, read from the right global endpoint inward, its coatom omissions are

\[
                         f_0,f_d,f_{d-1},\ldots,f_1.          \tag{2.2}
\]

Use base `B_(1-epsilon)` in the reversed copy of (1.3).  If the source word
has length `M`, then its last-`h` union is

\[
 \bigcup_{j=M-h}^{M-1}A_j^\epsilon
   =B_{1-\epsilon}\cup\{f_{d-h+1},\ldots,f_d\},             \tag{2.3}
\]

for `1<=h<=d`.  Reversal commutes with `D^d`, so the same proof gives the
right half of (0.1) and exact carrier replay.

Equations (1.5) and (2.3) describe one orientation of the two shores.  The
carrier boundary is phase independent, so either occurrence of
`epsilon` may be replaced by `1-epsilon`.  For the return orientation
(0.1), use `B_(1-epsilon)` on the left and `B_epsilon` on the right.

When `N>=d+2`, the modified left source positions `0,...,d` and modified
right positions `N-1,...,N+d-1` are disjoint.  The two constructions may
therefore be made simultaneously.  Every modified source on one shore lies
outside every carrier window touched by the other shore.  This proves the
claimed two-phase global carve.

### Corollary 2.1 (one-packet terminal return is exact)

Let the packet's native prefix/suffix columns at each `h<d` realize
`(B_epsilon+prefix, B_(1-epsilon)+suffix)` in phase `epsilon`.  Assume the
packet lies away from the two global source boundaries, so the native and
boundary cell addresses are distinct.  Then each phase has a matching of
all four deep targets at every depth:

\[
\begin{array}{c|cc}
 &\text{native cells}&\text{boundary cells}\\ \hline
 \epsilon=0&\text{phase-zero chains}&\text{phase-one chains}\\
 \epsilon=1&\text{phase-one chains}&\text{phase-zero chains}.
\end{array}                                                   \tag{2.4}
\]

These are genuine common-cap matchings within each phase, because their
native values come from maximal erosion and their boundary values occur in
the single literal word constructed above.  Therefore the residual
one-packet return graph has terminal deficiency zero.

The two rows of (2.4) are different matchings in different legal cap
states.  Corollary 2.1 does not assert membership in the edgewise
phase-common graph `H^0 cap H^1`; that stronger fixed-basis interface is
unnecessary for terminal-only compilation and remains false locally.

## 3. Native and fresh `q1` faces

In the native face, keep `F={f_0,...,f_d}`.  Equation (1.5) at `h=d` is

\[
                         Q_\epsilon=B_\epsilon\cup
                                      \{f_1,\ldots,f_d\}.     \tag{3.1}
\]

For the mixed coatom packet these are exactly its two native `q1` hinge
colours.  The packet's two native cells already saturate `Q_0,Q_1` in both
phases.  Hence the two boundary cells (3.1) can be omitted from the target
matching while the `h<d` cells route all deep targets.  The unused cells
remain fixed-cap addresses; this observation alone does not put a hard
packet-task edge on them.

For the fresh face, replace the last filler in the left endpoint block by a
fresh `x`.  Use

\[
 F_x=\{f_0,f_1,\ldots,f_{d-1},x\},
\]

with omission order `f_0,f_1,...,f_(d-1),x`.  Then (1.5) for `h<d` is the
same deep prefix chain, while

\[
             \bigcup_{j=0}^{d-1}A_j^\epsilon
             =B_\epsilon\cup\{f_1,\ldots,f_{d-1},x\}.         \tag{3.2}
\]

The right shore has the symmetric replacement at its unused extreme.  This
is useful only when (3.2) is a named missing `q1` colour already contained
in the prepared endpoint owner.  It is not a general `q1` regeneration
theorem.

## 4. Endpoint containment alone is false

The first nonvacuous obstruction is `d=3`.  Let

\[
 S_1=B\cup\{f_1\},\qquad S_2=B\cup\{f_1,f_2\}.              \tag{4.1}
\]

If the first two prefix cells have values `S_1,S_2`, then

\[
                         A_0=S_1,qquad f_2\in A_1.           \tag{4.2}
\]

But every legal antecedent source satisfies

\[
                         A_1\subseteq T_0\cap T_1.            \tag{4.3}
\]

Thus an endpoint owner `T_0` may contain the whole chain while a next owner
`T_1` omitting `f_2` makes the carve impossible.  The coatom order in
(1.1) avoids this obstruction sharply: `f_h` persists through owner
`h-1`, exactly long enough to be placed at source `h-1`.

More generally, for any exact nested prefix chain, every increment
`S_h-S_(h-1)` must lie in

\[
                         P_{h-1}=T_0\cap\cdots\cap T_{h-1}.   \tag{4.4}
\]

This is the coordinatewise trace guard missing from endpoint containment.

## 5. What this closes, and what it does not

This theorem closes the local exterior **return-bank** problem for the two
nested packet chains, conditional on two prepared global endpoint coatom
blocks.  It improves the empty local return graph: the boundary cells give
`2(d-1)` literal phase-switched return columns in one exact antecedent.
For one packet, Corollary 2.1 makes the terminal deep-chain deficiency
exactly zero.

It does not yet prove an additive bound.

* Preparing the two endpoint owner blocks without adding `Theta(d)` owners
  is a host/planting theorem, not part of the carve.
* The rest of the lower target matching must coexist with these fixed source
  letters.  The present theorem proves joint compatibility of the chain
  cells, not Hall for all other targets.
* A duplicate `q1` cell is an unused matching address, not automatically a
  representative for the typed packet task.
* The construction is basis-preserving chain transport.  It becomes an
  open exterior ear only after a separate hard-task trace edge into one of
  the two fixed spare addresses is certified.

## 6. Audit

The dependency-free audit reconstructs maximal erosion and checks both
phases literally for every `2<=d<=40`, including reversal and both `q1`
faces.  It also exhausts the `d=3` endpoint-containment obstruction.

```text
scratch/audit_coatom_two_phase_boundary_chain_carving_20260801.py
scratch/coatom_two_phase_boundary_chain_carving_20260801.audit.json
```

It reports

```text
PASS_TWO_PHASE_BOUNDARY_CHAIN_CARVING_WITH_TRACE_GUARD
```

with canonical payload SHA-256

```text
6fb79dc35945a05f29ee039f783ce66800a95750d1609708f4a6339627e8b5bd
```

Dependencies:

* `MATH_THEOREM_K_ZERO_OWNER_COATOM_U5_REGENERATIVE_RECURRENCE_20260801.md`;
* `MATH_THEOREM_THREAD_D_COATOM_U5_NATIVE_COLUMNS_AND_RETURN_HALL_20260801.md`;
* `MATH_THEOREM_COATOM_ENDPOINT_PLANTING_FIXED_SLOT_HALL_CORRECTION_20260801.md`.
