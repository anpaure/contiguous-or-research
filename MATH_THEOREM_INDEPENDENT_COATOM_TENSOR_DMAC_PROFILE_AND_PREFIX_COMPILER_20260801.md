# Coatom tensors and the compiler: exact disturbance profiles and a one-prefix sufficient theorem

Date: 2026-08-01  
Status: unconditional exact flat-incidence theorem; conditional common-compiler theorem  
Scope: the transparent-packet route to `nu(k)<=B(k)+O(1)`, not an all-`k` construction

## 0. Outcome

The zero-owner-defect coatom tensor has a sharply bounded lower-compiler
footprint once the compiler is physicalized by maximal erosion.

For the complete flat maximal-envelope compiler, the phase-sensitive
**incidence** footprint can be computed exactly.  Among the three
one-cross-per-repeated-pair patterns, `1100` is incidence-smallest.  Its width-`h`
row has

\[
                         6d+20+4h                               \tag{0.1}
\]

changed incidence columns, and therefore

\[
                         |D_{inc}|=8d^2+22d.                    \tag{0.2}
\]

They form four explicit left-expanding bands.  Their smallest single
Ferrers-prefix hull has length `12d+33` in every row.

For the full packet, q1 preservation restricts the admissible patterns to
`0110,1011`.  Each then has `8d^2+24d` sensitive cells; `1011` retains the
same shortest prefix hull `12d+33`.  Thus `1011`, not incidence-minimal
`1100`, is the preferred U1--U5 pattern.

This gives a concrete bounded-task construction target.  Put the packet at
the left endpoint and reserve that prefix.  If one trace-guarded compiler
matching has

\[
                  u_h\ge\max\{\rho_h^*,12d+33\},                \tag{0.3}
\]

then the literal same matching works in both phases, provided the selected
trace guards are also phase invariant outside the footprint.

The exact, non-wasteful object is the guarded common-edge bank

\[
                  H^\cap_{a,\eta}=H^0_{a,\eta}\cap H^1_{a,\eta}, \tag{0.4}
\]

where `a` is the physical placement and `eta` the screen pattern.  Jointly
choosing packet and compiler succeeds exactly when

\[
       \min_{a,\eta}\delta_{H^\cap_{a,\eta}}(D(\rho^*))=0.       \tag{0.5}
\]

The generic host supplies neither these guarded banks nor this Hall row.
Equal incidence predicates do not certify equal global trace guards, while
a changed predicate can retain useful common edges.  Thus (0.5), rather
than scalar slack, is the sharp remaining quantifier.

## 1. Physical maximal-erosion compiler

Let

\[
           T^\epsilon=(T_0^\epsilon,\ldots,T_{N-1}^\epsilon),
           \qquad \epsilon\in\{0,1\},                            \tag{1.1}
\]

be the two phases of a zero-defect coatom tensor at depth `d`.  Thus

\[
                              N=12d+35.                           \tag{1.2}
\]

The two phases have the same first `d+2` owners and at least the same last
`d+2` owners.  Consequently every erosion window crossing an exterior
boundary is phase invariant.

Index source-envelope positions by `p` and define

\[
       E_p^\epsilon=\bigcap\{T_i^\epsilon:i\le p\le i+d\}.       \tag{1.3}
\]

For an owner-bit occurrence `(i,x)`, its maximal-envelope carrier is

\[
       R_{i,x}^\epsilon=\{p\in[i,i+d]:x\in E_p^\epsilon\}.       \tag{1.4}
\]

Let `c=[s,s+h)` be a width-`h` proper-prefix cell.  Its allowed and mandatory
masks are

\[
 A_c^\epsilon=\bigcup_{p\in c}E_p^\epsilon,qquad
 M_c^\epsilon=\bigcup\{\{x\}:R_{i,x}^\epsilon\subseteq c\}.      \tag{1.5}
\]

After removing hit conditions already met by `M_c`, retain the
inclusion-minimal masks among `{E_p:p in c}`.  The exact individual-incidence
predicate is

\[
 \Gamma^\epsilon(c)=\{S:
       M_c^\epsilon\subseteq S\subseteq A_c^\epsilon,
       \quad S\cap E_p^\epsilon\ne\varnothing\ (p\in c)\}.      \tag{1.6}
\]

The target-rank restrictions are fixed and suppressed.  Formula (1.6) is
the canonical allowed/mandatory/minimal-hit representation of the flat
maximal-envelope compiler: it is equivalent to literal realizability of the
target in `c` while every source letter is nonempty and every owner bit is
replayed.

Define

\[
          D_{inc}=\{c:\Gamma^0(c)\ne\Gamma^1(c)\}.               \tag{1.7}
\]

The fixed core `K` does not change this set: every predicate difference has
a witness avoiding `K`, while `K` is common to both phases.

## 2. Exact fixed-address disturbance

Use the zero-defect screen pattern `1100`, equivalently union screens at
zero-based transition positions

\[
                             \{3,4,7,10\}.                        \tag{2.1}
\]

### Theorem 2.1 (exact individual-incidence profile)

Place the macro at owner start `a`.  For every width `1<=h<=d`, the cells in
`D_inc` for pattern `1100` are exactly those for which `s-a` lies in one of

\[
\begin{aligned}
 &[d+2-h,\,3d+7],\\
 &[6d+15-h,\,6d+16],\\
 &[7d+19-h,\,10d+28],\\
 &[11d+31-h,\,12d+32].                              \tag{2.2}
\end{aligned}
\]

The four intervals are disjoint and

\[
                       |D_{inc,h}|=6d+20+4h.                      \tag{2.3}
\]

Thus

\[
                           |D_{inc}|=8d^2+22d.                    \tag{2.4}
\]

The formula is identical for all three authenticated connector rows.

#### Proof

Block `j` begins at `b_j=j(d+3)` and its screen is at
`q_j=(j+1)(d+3)-1`.  Substitute the coatom block masks and the four
union-screen positions (2.1) into (1.3)--(1.6).  Changes in the allowed and
minimal-hit masks occur at the screen breakpoints; changes in a completely
contained carrier shift the left breakpoint by `0,...,h-1`.  Canonicalizing
the result gives exactly the four intervals in (2.2).  Their lengths are

\[
         2d+6+h,\quad h+2,\quad3d+10+h,\quad d+2+h,
\]

which proves (2.3)--(2.4).  The active table is finite on six coordinates;
inserting one additional filler inserts one coatom in every block and shifts
each `b_j,q_j` by the displayed affine amount, so the calculation is
symbolic for every `d`.  The audit independently compares the complete
truth-table predicates for `d<=5` and the canonical signatures for all three
rows through `d=20`.  \(\square\)

### Corollary 2.2 (screen-choice range)

Patterns `0110` and `1011` each have

\[
                         |D_{inc,h}|=6d+22+4h,
             \qquad |D_{inc}|=8d^2+24d.                          \tag{2.5}
\]

Across the three patterns,

\[
 \left|\bigcup_\eta D_{inc}(\eta)\right|=8d^2+26d,
 \qquad
 \left|\bigcap_\eta D_{inc}(\eta)\right|=8d^2+21d.             \tag{2.6}
\]

Thus choosing the screen pattern moves only `5d` incidence columns; a
quadratic common core remains phase sensitive.

If both q1 palettes must be preserved, only `0110,1011` remain.  Their
union and intersection have sizes

\[
                 8d^2+25d,\qquad8d^2+23d,                       \tag{2.7}
\]

respectively.  Their choice moves only `2d` columns.

### Corollary 2.3 (minimal one-prefix hull)

For patterns `1100` and `1011`, the smallest single prefix containing every
row of `D_inc` has threshold

\[
                         \rho^{mac}_h=a+12d+33.                  \tag{2.8}
\]

For `0110` it is `a+12d+34`.  The four-band set (2.2) is much smaller than
its prefix hull, but the hull is a legal Ferrers ideal.  Minimality follows
from the final cell at relative start `12d+32`.

## 3. One-prefix common compiler

Embed the tensor at the left endpoint of the linear owner chronology.  Let
`H^epsilon_(a,eta)` be the forced-core-contracted, fully trace-guarded bank
in phase `epsilon`, placement `a`, and screen pattern `eta`.  Put

\[
                 H^\cap_{a,\eta}=H^0_{a,\eta}\cap H^1_{a,\eta}. \tag{3.1}
\]

Let `rho*` be the componentwise worst reachable residence frontier.

### Theorem 3.1 (exact joint packet/compiler criterion)

A placement, screen pattern and one literal compiler matching common to both
phases exist if and only if

\[
       \boxed{\min_{a,\eta}
          \delta_{H^\cap_{a,\eta}}(D(\rho^*))=0.}                \tag{3.2}
\]

Replacing zero by an absolute constant `c`, together with a literal
terminal repair of the omitted lower targets, is sufficient for an `O(1)`
compiler contribution.

#### Proof

An edge of `H^cap` is exactly an incidence whose complete trace guard is
valid in both phases.  The fixed-frontier matching theorem says that one
matching survives every reachable frontier exactly when it avoids
`D(rho*)`; its deficiency is the displayed quantity.  Minimizing over the
finite packet choices gives (3.2).  \(\square\)

For a simpler sufficient face, assume that every trace guard outside
`D_inc` is certified invariant.  Use the q1-admissible pattern `1011` at
`a=0` and define

\[
                 \widehat\rho_h=\max\{\rho_h^*,12d+33\}.         \tag{3.3}
\]

The vector `widehat rho` is nondecreasing, so `D(widehat rho)` is one
ordinary Ferrers ideal.

### Corollary 3.2 (endpoint-gauged fixed-basis criterion)

If `M_0` is a target-saturating trace-guarded matching in `H` with

\[
                       u_h(M_0)\ge\widehat\rho_h
                       \qquad(1\le h\le d),                       \tag{3.4}
\]

then the literal same matching is valid in both coatom-tensor phases and
against every reachable residence frontier.  The macro exports no compiler
cell and no compiler state.

Before choosing `M_0`, such a matching exists exactly when

\[
                         \delta_H(D(\widehat\rho))=0.             \tag{3.5}
\]

If the deficiency in (3.5) is at most an absolute constant `c` and a
terminal module literally realizes the omitted `c` lower obligations, the
compiler contribution is `O(1)`.

#### Proof

Condition (3.4) says that `M_0` uses no cell in `D(widehat rho)`.  By
Corollary 2.3 this ideal contains every cell whose incidence predicate can
change, and it also contains every residence-deleted cell.  The additional
trace-invariance hypothesis makes every selected guard literally unchanged
between phases.  The fixed-unused-basis frontier theorem proves (3.5) and
the bounded-deficiency statement.  \(\square\)

This is a genuine joint design: choose the packet at the endpoint and solve
the compiler matching only after reserving its one common prefix.  It is
strictly stronger than first choosing an arbitrary matching and hoping that
its unused cells happen to contain four disconnected disturbance bands.

For `q=O(1)` consecutive endpoint packets, the still simpler coarse reserve

\[
                  a_h=q(12d+35)                                  \tag{3.6}
\]

contains every phase-dependent cell.  Thus a bounded regenerative state
costs only `O(d^2)` reserved cell addresses, not an accumulated owner
sidecar.

### Scalar calibration

The maximal lower-atlas capacity at excess `e` is

\[
                         eW+{e+1\choose2}.                         \tag{3.7}
\]

Increasing `e=d` to `d+1` adds

\[
                              W+d+1                               \tag{3.8}
\]

cells, whereas the constant prefix (3.3) reserves only

\[
                           d(12d+33).                              \tag{3.9}
\]

Thus one unit of additive word length has more than enough *scalar* capacity
for the reserve whenever

\[
                         W\ge12d^2+32d-1.                         \tag{3.10}
\]

This holds eventually because `W` is central-binomial while `d=O(sqrt k)`.
It is not a Hall or trace-guard proof; it only shows that the proposed
`B+O(1)` reserve is not blocked by the lower-atlas count.

## 4. Occurrence-transport alternative

If the compiler is allowed to transport occurrence-labelled cells on common
owner fragments and rematch only in closed local reservations, pattern
`1011` is preferable.  Its common-edge graph has component sizes

\[
  1^2,\quad(d+2)^5,\quad(d+3),\quad(2d+6),\quad(2d+7)^2,          \tag{4.1}
\]

and exactly ten old-only and ten new-only seams.

A width-`h` compiler cell has owner-seam dependency span

\[
                              s_h=d+h-1.                           \tag{4.2}
\]

The exact number of nontransported starts in either phase is

\[
 b_h=\sum_Q\min\{s_h,|Q|\}-s_h
 =\begin{cases}
      8d+8h-6,&1\le h\le3,\\
      8d+13+2h,&4\le h\le d.
   \end{cases}                                                    \tag{4.3}
\]

For `d>=3`,

\[
                         \sum_{h=1}^db_h=9d^2+14d-21.             \tag{4.4}
\]

This is the sharp closed-reservation footprint before inspecting incidence
edges.  It does not give a literal fixed-address matching: transported cells
may move to different addresses.  It is therefore an interface for the
closed local-rematching theorem, while Sections 2--3 are the interface for
the lean same-`M_0` theorem.

## 5. Why locality must be a hypothesis

No statement about the owner word alone can bound `D_mac` for an arbitrary
trace-guarded compiler.  For example, attach to every cell the guard

\[
       g_c(T)=\mathbf1\{\text{the active owner at one changed tensor
                              position has phase-0 label}\}.      \tag{5.1}
\]


Every local cell value away from the tensor may be unchanged, yet every
selected guard flips.  Then `D_mac=C`.  This artificial example is enough
to show that a phase-common trace locality certificate, or a literal replay
of the chosen matching, is logically necessary.

There is also a smallest fixed-anchor obstruction to the wholesale-deletion
test.  Choose one cell in the three-pattern intersection in (2.6), give one
lower target that cell as its sole neighbour, and add arbitrarily many
irrelevant unused cells.  The baseline bank is matchable, but deleting the
complete incidence-sensitive footprint has deficiency one for every screen
pattern.  This does not say that the real common-edge bank fails: a changed
cell can retain the selected edge.  It says exactly that pattern choice and
scalar surplus cannot replace Hall in (3.2).

### 5.1 Dense-use limitation of one wholesale-unused basis

At coefficient one, the total number of unused proper-prefix cells is

\[
        \sigma=dW+{d+1\choose2}-\Lambda<W+d,                     \tag{5.2}
\]

where the strict inequality follows from the minimality of `d`.  If `q`
address-disjoint tensors are all handled by deleting every phase-sensitive
cell, then even after choosing the best q1-admissible screen independently,
(2.7) forces

\[
                   q(8d^2+23d)\le\sigma.                         \tag{5.3}
\]

Hence this coarse same-basis strategy supports only `O(W/d^2)` disjoint
macros, not the `Theta(W/d)` macros in the density-matched bulk reset.  At
length `B+C` for fixed `C`, the scalar slack is still only

\[
           <(C+1)\left(W+d+{C\over2}\right)=O_C(W),              \tag{5.4}
\]

so the conclusion is unchanged.  This is a no-go only for disjoint
whole-cell reservation.  Shared footprints, common edges inside `D_inc`,
or closed local rematching can evade it.  A bounded regenerative family of
`O(1)` packets remains scalar-feasible because its reserve is only
`O(d^2)=o(W)`.

### 5.2 Architectural consequence

The quadratic footprint favours the serial safe-move reduction.  A serial
sequence of owner/upper/residence-transparent tensor moves need not carry a
compiler through its intermediate vertices; it solves the compiler once at
the final carrier.  In that architecture `D_inc` is diagnostic search data,
not a reserved bank.  By contrast, any parallel transparent-packet theorem
which insists on one fixed `M_0` throughout must prove the common-edge Hall
row (3.2), use closed local rematching, or restrict itself to a bounded
number of packets.  Whole-cell avoidance cannot close its dense regime.

The generic host currently exports neither that local trace bank nor a
matching satisfying (3.2).  Therefore this note does not claim
`nu(k)<=B(k)+O(1)`.  It replaces the undefined `D_mac` by one exact physical
target and shows that an endpoint-gauged prefix, rather than four owner
repairs, is the right compiler object.

## 6. Audit

Run

```bash
python3 scratch/audit_coatom_screen_tensor_dmac_profile_20260801.py
```

The audit reconstructs all three authenticated connector rows for every
`1<=d<=20` and all three zero-defect screen patterns.  It checks the exact
allowed/mandatory/minimal-hit incidence signatures and the four bands in
Theorem 2.1, their union/intersection, the narrower erosion-tuple and
internal-value calibrations, and the common-fragment formula (4.1)--(4.4).

It deliberately constructs no target--cell graph and makes no matching
claim.
