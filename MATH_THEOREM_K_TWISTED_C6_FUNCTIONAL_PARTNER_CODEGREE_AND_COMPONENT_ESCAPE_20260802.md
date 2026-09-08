# Twisted `C6` pump: functional partner codegree, history guards, and component escape

**Date:** 2026-08-02  
**Lane:** K, prospective ternary fusion of the unit pump  
**Status:** exact partner normal form, exact resource and component criteria,
and a quantitative conditional asymptotic theorem. Raw Boolean degree,
fan size, near-perfectness, and bounded collar length are proved
insufficient. A Boolean-specific construction of positive functional
codegree is not claimed.

## 0. Verdict

Fix one nonprivate edge of the developed twisted pump. Its Cartesian
Boolean-hex fan has `(r-1)(r-2)` raw labelled options, but an oriented
owner factor can retain only a **partial matching** of those options.
The two required old partner roles define partial maps

\[
              \phi:b\longmapsto c,\qquad
              \psi:c\longmapsto b,                    \tag{0.1}
\]

and a hex is present exactly at a mutual two-cycle

\[
                         \phi(b)=c,\qquad\psi(c)=b.     \tag{0.2}
\]

The exact partner codegree is therefore

\[
                \kappa_e=|\{b:\psi(\phi(b))=b\}|\le r-2. \tag{0.3}
\]

This is the first nonautomatic row. Both marginal maps may cover their
entire available shores while `kappa_e=0`, by a cyclic derangement. Hence
raw fan size, owner degree two, and separate old-role availability cannot
prove even one partner pair.

Once a mutual pair exists, every non-target owner/lower/upper/tail/head
resource is injective across the mutual-pair family. Thus a forbidden typed
resource deletes at most one candidate, a considerable strengthening of
the raw fan load `r-1`.

History and topology still matter. If `g_e` mutual pairs fail the exact
six directed-history seam tests, `t_e` fail the required component routing,
and `q_e` meet another forbidden resource, then the union bound

\[
                         \kappa_e>g_e+t_e+q_e,          \tag{0.4}
\]

is sufficient for a usable pump/corridor fusion. The exact criterion is
the nonempty set difference in Theorem 5.1; the three bad sets may overlap.
For a prepared common-collar bank the variable-label history loss is at
most `4d`; bounded collar length alone does **not** imply this bound because
the collar may depend on `(b,c)`.

A quantitative sufficient form is the following. If, for one pump edge,

* `kappa_e>=eta r`;
* at least a `zeta` fraction of those pairs route one partner through A's
  component and the other through a third component;
* total history/resource loss is at most `C d+C_0`;

then a coherent ternary fusion exists whenever

\[
                         \zeta\eta r>C d+C_0.          \tag{0.5}
\]

For `d<=K sqrt(r)` this holds for all

\[
 r>\max\left\{\left({2CK\over\zeta\eta}\right)^2,
                    {2C_0\over\zeta\eta}\right\}.     \tag{0.6}
\]

Every literal physical Boolean hex satisfying these rows is automatically
zero-charge. No separate voltage density loss occurs. The missing
all-dimensional theorem is now sharply one of **correlated partner
codegree plus component escape**, not raw `C6` abundance.

## 1. Cartesian fan through one pump edge

Let the target pump atom be

\[
 e=(L,U,E,F),\qquad E=L\cup\{d_0\},\quad
 F=L\cup\{a_0\},\quad U=L\cup\{a_0,d_0\},             \tag{1.1}
\]

where `|L|=r-1`. Put

\[
                  B=L,\qquad C=[k]\setminus U.         \tag{1.2}
\]

At `k=2r-1`,

\[
                         |B|=r-1,\qquad |C|=r-2.       \tag{1.3}
\]

For `(b,c) in B times C`, put `S=L-{b}`. The two old partner
atoms are

\[
\begin{aligned}
 o_1(b,c)&:A_b\longrightarrow B_{bc},\\
 A_b&=S\cup\{a_0,d_0\}=U-\{b\},\\
 B_{bc}&=S\cup\{a_0,c\},                              \tag{1.4}\\
 o_2(b,c)&:C_{bc}\longrightarrow D_c,\\
 C_{bc}&=S\cup\{c,d_0\},\\
 D_c&=S\cup\{b,c\}=L\cup\{c\}.                     \tag{1.5}
\end{aligned}
\]

Together with `e=E->F`, their opposite Boolean-hex phase is

\[
             A_b\to F,\qquad C_{bc}\to B_{bc},
                         \qquad E\to D_c.              \tag{1.6}
\]

All six atoms are literal ordered diamonds and old/new have identical
lower, upper, tail and head resource multisets.

## 2. Functional partner theorem

Let `M` be an oriented owner factor: every owner has one selected outgoing
and one selected incoming projected Johnson edge. Define partial maps

\[
\begin{aligned}
 \phi_M(b)=c
   &\quad\Longleftrightarrow\quad o_1(b,c)\in M,\\
 \psi_M(c)=b
   &\quad\Longleftrightarrow\quad o_2(b,c)\in M.       \tag{2.1}
\end{aligned}
\]

Undefined values are denoted by `bot`.

### Theorem 2.1 (exact mutual-two-cycle normal form)

The set of Cartesian options whose two old partner atoms both belong to
`M` is

\[
 {cal A}_e(M)=
 \{(b,c)\in B\times C:\phi_M(b)=c,\ \psi_M(c)=b\}.     \tag{2.2}
\]

It is a matching in the complete bipartite graph `B times C`. In
particular

\[
                         |{\cal A}_e(M)|=\kappa_e\le r-2. \tag{2.3}
\]

#### Proof

For fixed `b`, the tail owner `A_b` in (1.4) is fixed, while the heads
`B_bc` are distinct as `c` varies. Its unique selected outgoing edge
therefore defines at most one `phi_M(b)`. For fixed `c`, the head owner
`D_c` in (1.5) is fixed, while the tails `C_bc` are distinct as `b`
varies. Its unique selected incoming edge defines at most one
`psi_M(c)`. Both old atoms occur exactly under the conjunction (2.2).
No two such pairs share `b` or `c`, proving the matching assertion and
(2.3). \(\square\)

### Proposition 2.2 (marginal degree does not force a partner)

For `|B|,|C|>=2`, both maps in (2.1) can be defined on arbitrarily large
subsets, including all of `C` and at least `|C|` members of `B`, while
`kappa_e=0`.

#### Proof

Choose distinct `b_0,...,b_(s-1)` and
`c_0,...,c_(s-1)`, where `2<=s<=|C|`. Put

\[
          \phi(b_i)=c_i,\qquad
          \psi(c_i)=b_{i+1\pmod s}.                   \tag{2.4}
\]

Then both marginal role tables are complete on the displayed shores, but
no pair is mutual. Every atom in (2.4) is a legal Boolean atom from
(1.4)--(1.5). Their role-tail sets and role-head sets are separately
distinct: the first role is indexed by distinct `b_i`, the second by
distinct `c_i`, and a cross-role equality would require the outside labels
`a_0` and `d_0` to agree. The lower and upper resources are likewise
separately distinct: same-role equality recovers its displayed index or
index pair, while cross-role equality would respectively identify
`a_0` with a `c_i` or delete `a_0` and an element of `L` simultaneously.
Thus all four local matching rows pass.
\(\square\)

At `s=2`, (2.4) is the smallest obstruction: the two role matchings are
the opposite diagonals of one `2 by 2` table. It is a local functional
obstruction, not by itself a theorem that an arbitrarily prescribed global
factor realizes all those rows. It proves that owner degrees and separate
role projections contain no implication of (0.2).

The existing hex-free near-factor theorem gives the complementary global
warning: even a near-perfect four-resource body with a protected cycle and
large girth can be chosen with no applicable old Boolean-hex phase. Its
even-band setting is not silently promoted to the present odd host, but it
rules out using generic near-perfectness or high girth as the missing
correlation theorem.

## 3. Resource load collapses after functional intersection

### Lemma 3.1 (mutual-pair resource simplicity)

Across the options in `A_e(M)`, every non-target typed owner, lower,
upper, tail, and head resource in (1.4)--(1.6) occurs at most once.

#### Proof

The mutual-pair family has distinct `b` and distinct `c`. A resource
depending only on `b`, such as `A_b` or `L-{b}+{a_0}`, is therefore
unique; so is a resource depending only on `c`, such as `D_c` or
`U-{a_0}+{c}`. A mixed resource recovers both coordinates from its
intersection with `L` and its unique outside label. A resource from the
`a_0` type cannot equal one from the `c` type because `a_0 in U` while
`c notin U`. Thus cross-type equality is also impossible. \(\square\)

### Corollary 3.2 (exact forbidden-resource loss)

If `Q` is any bank of forbidden non-target typed resources, at most

\[
                              q_e\le |Q|                \tag{3.1}
\]

members of `A_e(M)` meet `Q`.

This is stronger than the raw Cartesian-fan bound `|Q|(r-1)`. Bare
coordinate labels are not capacity-one typed resources and are handled by
the history/coordinate guards below.

### Theorem 3.3 (a linear prospective mutual bank is resource-feasible)

Choose `t<=r-2` distinct labels `b_1,...,b_t in B` and distinct labels
`c_1,...,c_t in C`.  The bank

\[
 {cal P}_t=\{o_1(b_i,c_i),o_2(b_i,c_i):1\le i\le t\} \tag{3.2}
\]

has `2t` projected Johnson edges, `4t` middle-levels incidence edges,
maximum incidence degree two, and pairwise-distinct lower, upper, tail and
head resources.  Any factor containing `P_t` has

\[
                              \kappa_e\ge t.            \tag{3.3}
\]

Consequently, for any additional disjoint 2-bounded protected bank of
`L_0` incidence edges, the current small protected-factor theorem plants
the union in a pump-free owner/lower factor whenever

\[
                              L_0+4t\le r-2.            \tag{3.4}
\]

#### Proof

Distinct `(b_i,c_i)` form a matching.  Lemma 3.1 gives all four resource
injections; in particular all owner endpoints and lower facets of the
projected edges are distinct between options.  The incidence lift is
therefore a disjoint union of two-edge paths, proving its edge count and
degree bound.  Both old roles of every displayed option are selected, so
(3.3) follows from Theorem 2.1.  Equation (3.4) is exactly the hypothesis
of the small protected-factor theorem applied to the disjoint union.
\(\square\)

This closes the **local resource cost** of imposing linear functional
codegree: at most one quarter of the available incidence budget per mutual
option.  It does not plant the developed pump, whose `6k` incidences remain
outside that theorem, and it does not control which components contain the
two old roles after completion.  Applying (3.2) beside the pump therefore
still requires the residual Ore--Ryser theorem from item 2648K.

## 4. Exact history loss and why collar length alone is insufficient

For `(b,c) in A_e(M)`, delete the three old edges. Write

\[
 P_1(b,c):B_{bc}\leadsto A_b,\quad
 P_2(b,c):D_c\leadsto C_{bc},\quad
 P_3:F\leadsto E                                      \tag{4.1}
\]

for the resulting paths; `P_3` is the fixed opened pump component. The
new phase is biresident exactly when, for `nu=+,-`,

\[
\begin{aligned}
 G_d^\nu(P_1,A_b\to F,P_3),\\
 G_d^\nu(P_3,E\to D_c,P_2),\\
 G_d^\nu(P_2,C_{bc}\to B_{bc},P_1)                    \tag{4.2}
\end{aligned}
\]

all hold. Let `g_e` be the number of mutual pairs failing (4.2).

### Lemma 4.1 (prepared common-collar bound)

Assume all fixed connector-label tests and all triangular old-collar tests
in (4.2) pass throughout `A_e(M)`. Assume further that the two
option-dependent variable-label failure sets have common envelopes:

\[
\begin{aligned}
 |\{b:b\in D^+(P_3)\text{ or }b\in I^-(P_1(b,\phi(b)))\}|&\le2d,\\
 |\{c:c\in D^+(P_2(\psi(c),c))\text{ or }c\in I^-(P_3)\}|&\le2d.
                                                               \tag{4.3}
\end{aligned}
\]

Then

\[
                              g_e\le4d.                \tag{4.4}
\]

#### Proof

The new seams insert, in cyclic order, `b,c,a_0` and all delete `d_0`.
Under the fixed tests in the hypothesis, the only remaining variable
failures are precisely those displayed in (4.3). Since `A_e(M)` is a
matching, each forbidden `b` and each forbidden `c` deletes at most one
option. The union bound gives (4.4). \(\square\)

The common-envelope hypothesis is load-bearing. Although every individual
collar has length `d`, the collar attached to `A_b` or `D_c` may depend on
the option. It is consistent with all marginal collar-length bounds that
every `b` belongs to its own `I^-(P_1)`; then every mutual pair fails.
Thus bounded history state gives a finite test, not an `O(d)` aggregate
loss theorem. A node-private reset, common collar bank, or an independently
proved normalized load bound is required for (4.4).

## 5. Exact component escape

Let `Gamma_P` be the pump component and `Gamma_A` the component containing
A's opened protected path after the prospective residual completion. For
an option in `A_e(M)`, put

\[
 \gamma_1(b,c)=\operatorname{comp}(o_1(b,c)),\qquad
 \gamma_2(b,c)=\operatorname{comp}(o_2(b,c)).           \tag{5.1}
\]

Define the A-targeted escape set

\[
 {\cal E}_e^A=\left\{(b,c)\in{\cal A}_e(M):
   \begin{array}{l}
   \text{exactly one of }\gamma_1,\gamma_2\text{ equals }\Gamma_A,\\
   \text{the other lies outside }\{\Gamma_A,\Gamma_P\}
   \end{array}\right\}.                                \tag{5.2}
\]

### Theorem 5.1 (necessary and sufficient topology row)

A mutual option merges the pump component, A's component, and one third
component into one directed cycle if and only if it belongs to
`E_e^A`. After imposing histories and forbidden resources, a usable
fusion exists if and only if

\[
 {\cal E}_e^A\setminus({\cal G}_e\cup{\cal Q}_e)
                         \ne\varnothing,               \tag{5.3}
\]

where `G_e` and `Q_e` are respectively the exact history-failure and
resource-failure sets.

#### Proof

The ternary fusion theorem merges three old edges to one cycle precisely
when they lie on three distinct old cycles. One edge is on `Gamma_P`.
Condition (5.2) says the other two are on `Gamma_A` and on a third cycle.
The history and resource rows are independently necessary and sufficient
for the literal switch, giving (5.3). \(\square\)

This component condition is not implied by a maximum component-size bound.
Even if every component contains only the two partner edges of one option,
all options may have `gamma_1=gamma_2` and hence be unusable. The exact
collapsed component graph has one edge
`gamma_1(b,c) gamma_2(b,c)` per mutual pair; the obstruction is that every
such edge is a loop or misses `Gamma_A` (or is incident with `Gamma_P`).

## 6. Conditional asymptotic partner theorem

### Theorem 6.1 (positive functional codegree plus guarded escape)

Suppose one nonprivate pump edge satisfies, for constants
`eta,zeta>0` and `C,C_0>=0`,

\[
\begin{aligned}
 \kappa_e&\ge\eta r,\\
 |{\cal E}_e^A|&\ge\zeta\kappa_e,\\
 |({\cal G}_e\cup{\cal Q}_e)\cap{\cal E}_e^A|
     &\le C d+C_0.                                     \tag{6.1}
\end{aligned}
\]

Then a history-compatible, resource-safe A-targeted ternary fusion exists
whenever

\[
                         \zeta\eta r>C d+C_0.          \tag{6.2}
\]

If `d<=K sqrt(r)`, the explicit sufficient range (0.6) implies (6.2).

#### Proof

The first two inequalities leave at least `zeta eta r` structurally
correct options. The last removes at most `Cd+C_0`. Strict inequality
leaves an option in (5.3). If `d<=K sqrt(r)`, the two bounds in (0.6)
make `CK sqrt(r)` and `C_0` each smaller than half of
`zeta eta r`. \(\square\)

Under Lemma 4.1 and Corollary 3.2 one may take

\[
                         C=4,qquad C_0=|Q|             \tag{6.3}
\]

when `Q` has bounded size and every Q-collision is represented by one typed
resource. More general occurrence guards simply add their proved load to
the third line of (6.1).

Theorem 6.1 is genuinely stronger than a fan-count statement and weaker
than an unproved universal host theorem. Its two structural hypotheses are
exactly the missing correlated rows: mutual role overlap and component
escape.

## 7. Coherent zero charge is automatic after literal selection

### Theorem 7.1 (no separate holonomy loss for a physical hex)

For every literal physical Boolean hex selected by Theorem 5.1,

\[
 \delta(A_b,F)+\delta(C_{bc},B_{bc})+\delta(E,D_c)
 =\delta(A_b,B_{bc})+\delta(C_{bc},D_c)+\delta(E,F).   \tag{7.1}
\]

Hence the fusion preserves the sum of the three old component voltages.
If the two nonpump old totals sum to zero, the merged component retains the
pump voltage `+1` or `-1` exactly.

#### Proof

In one physical lift, write `lambda(V)` for the phase of owner occurrence
`V`. Every direct seam has

\[
                         \delta(X,Y)=\lambda(Y)-\lambda(X).
\]

The old and new hex phases have the identical tail multiset
`{A_b,C_bc,E}` and identical head multiset `{B_bc,D_c,F}`. Summing the
potentials proves (7.1). \(\square\)

For a free equivariant factor, selecting the relevant edge orbits includes
all their developed translates, so a quotient mutual pair determines the
coherent physical hex at every phase. For periodic or independently
canonicalized occurrence states, the literal phase/lift field must remain
in the option; orbit-level marginal availability does not prove (7.1).

## 8. Sharp remaining theorem

No unconditional asymptotic partner theorem follows from the currently
proved host rows.

* Raw fan size `(r-1)(r-2)` collapses to the mutual functional codegree
  `kappa_e<=r-2`.
* Full separate role degrees allow the derangement (2.4) with
  `kappa_e=0`.
* Individual collar length `d` allows every row-dependent option to fail.
* Positive functional codegree allows every option to be component-diagonal
  or to miss A's component.
* Generic near-perfect/high-girth bodies can be Boolean-hex-free in the
  already proved four-resource model.

Thus the weakest useful prospective hypothesis is not a generic degree
bound. It is the three-line condition (6.1), or an explicit construction
implying it. A recursive all-`r` proof must jointly select the owner factor
so that one pump target has linear mutual two-cycle count, a positive
A-component escape fraction, and a node-private/common-envelope history
bank. Once those are supplied, Theorem 6.1 and the automatic charge
identity complete the pump/A topology fusion. Deeper upper shadows,
source/envelope transport, exterior all-width windows and the terminal
common-cap/compiler remain separate.
