# Defect-router Hall gate and the ordered `m=5` three-`C10` relay

Date: 2026-07-31  
Status: exact static max-flow theorem, complete literal `m=5` root-router
census, and exact separation from state-dependent physical topology; no
uniform repair-packet theorem

## 0. Verdict

A turn-palette repair packet has a small assignment skeleton.  If every
candidate macro gains one missing lower colour and one missing upper colour,
and protected-colour losses have already been made automatic by private
reserves, then selecting a complete set of macros is exactly bipartite
matching.  For lower defects `L0`, upper defects `U0`, and router multigraph
`R`, the exact condition is

\[
             |N_R(X)|\ge |X|\qquad(X\subseteq L_0).              \tag{0.1}
\]

At the transparent standard `m=5` root,

\[
 L_0=\{73,146,292\},\qquad U_0=\{219,365,438\}.
\]

The complete root-Hamilton-safe optimum-`C10` router has 31 labelled edges,
with multiplicity matrix (columns `219,365,438`)

\[
 \begin{array}{c|ccc}
       &219&365&438\\ \hline
 73    &1&10&0\\
 146   &12&0&0\\
 292   &0&0&8
 \end{array}.                                                   \tag{0.2}
\]

It has rank three and a unique endpoint-level perfect matching

\[
             73\leftrightarrow365,qquad
             146\leftrightarrow219,qquad
             292\leftrightarrow438.                             \tag{0.3}
\]

There are `10*12*8=960` labelled static matchings realizing (0.3).  This is
**not** a count of physical repair packets.  Static Hall does not know whether
the selected circuits remain alternating, whether their toggles have a
Hamilton-safe order, or whether the final augmented common core, private
sockets, and gap forest survive.

The frozen forced-port/private packet makes this distinction literal.  Its
three router edges are exactly (0.3), its signed colour banks are private and
support-monotone, and the ordered staircase is

\[
       (3,3,3)\to(2,2,2)\to(1,1,1)\to(0,0,0).
\]

But its third macro alone splits the root into components `36+216`; it is
Hamilton-safe only after the first two macros.  It is a state-dependent relay,
not a root-safe edge certified by (0.1).

## 1. Static unit-router model

Fix one factor state `F`.  Let

\[
 \mu_L(c),\quad \mu_U(c)
\]

be its lower- and upper-turn multiplicities, and let `L0,U0` be the zero
classes.  A **unit router macro** `t` has declared endpoints

\[
             \ell(t)\in L_0,qquad u(t)\in U_0,                  \tag{1.1}
\]

and frozen signed turn derivatives

\[
             \Delta^L_t(c),\qquad \Delta^U_t(c).                \tag{1.2}
\]

It adds one occurrence of each endpoint and does not remove another defect.
The derivatives must superpose for the label sets under consideration.  This
holds, for example, for pairwise vertex-disjoint physical circuits.

For binary choices `x_t`, exact static palette repair is the system

\[
 \sum_{t:\ell(t)=\ell}x_t=1\quad(\ell\in L_0),\qquad
 \sum_{t:u(t)=u}x_t=1\quad(u\in U_0),                            \tag{1.3}
\]

together with the protected-support inequalities

\[
 \mu_s(c)+\sum_t\Delta^s_t(c)x_t\ge1
 \quad(s\in\{L,U\},\ c\notin D_s),                             \tag{1.4}
\]

where `D_L=L0,D_U=U0`.  Equation (1.4), not individual safety of each macro,
is the exact aggregate monotonicity condition.

### Private protected-bank hypothesis

The router becomes ordinary matching when (1.4) is redundant for every
endpoint matching.  A concrete sufficient condition is:

1. every negative derivative is `-1` on a colour of initial multiplicity at
   least two;
2. negative banks of distinct selected macros are disjoint on each shore;
3. no macro removes another macro's defect gain.

More generally one may preallocate private loss capacity below
`mu_s(c)-1`.  Without such a hypothesis, (1.3)--(1.4) is matching with
additional resource rows.  Those rows need not be totally unimodular, and
plain Hall inequalities are no longer sufficient.

## 2. Exact max-flow and Hall theorem

After protected monotonicity is compiled away, make the bipartite multigraph

\[
 R=(L_0,U_0;\{e_t:t\in T\}),\qquad
 e_t=\ell(t)u(t).                                               \tag{2.1}
\]

Build the network

\[
 s\longrightarrow L_0\longrightarrow U_0\longrightarrow z,    \tag{2.2}
\]

with unit capacities on the outer arcs and one unit-capacity middle arc for
each labelled macro.  Parallel arcs retain macro identity.

The max-flow/min-cut value is the usual matching rank

\[
 \nu(R)=\min_{X\subseteq L_0}
          \bigl(|L_0\setminus X|+|N_R(X)|\bigr).                 \tag{2.3}
\]

Thus `nu(R)=r` is exactly (0.1).

### Theorem 2.1 (static defect-router theorem)

Assume `|L0|=|U0|=r`, frozen derivatives superpose, and every endpoint
matching is protected-monotone.  The following are equivalent:

1. `r` macros cover every lower and every upper defect exactly once;
2. the network (2.2) has integral flow `r`;
3. `R` has matching number `r`;
4. the Hall inequalities (0.1) hold for every `X` contained in `L0`.

Under these conditions a selected flow repairs both static palettes without
destroying an originally present colour.

#### Proof

An integral unit of flow uses one labelled middle arc, hence one macro, and
the outer capacities make its lower and upper endpoints unique.  Conversely
an endpoint-disjoint macro set gives the corresponding integral flow.
Integral max flow is bipartite matching, and Hall's theorem gives (0.1).
The private protected-bank hypothesis supplies (1.4), so the chosen endpoint
matching completes both palettes.  \(\square\)

Multiplicity of parallel router edges affects the number or cost of labelled
solutions, but not Hall feasibility.  A minimum-cost choice among a static
catalogue is an ordinary min-cost flow.

## 3. What static Hall does not certify

The theorem is deliberately static.  A physical circuit is evaluated in a
factor state, and after earlier toggles any of the following may change:

* which circuit edges are in the factor, hence whether it still alternates;
* the number and sizes of factor components after the toggle;
* the signed turn derivative if supports overlap;
* the remaining protected multiplicity reserve;
* the augmented common graph and its exposed sources;
* the private-port, gap-forest, trace, and socket state.

Therefore (0.1) is necessary for a unit-gain defect assignment and, under
the hypotheses of Theorem 2.1, sufficient for **static palette completion**.
It is not sufficient for an ordered Hamilton repair.  That stronger claim
also needs:

1. an ordering in the state-transition graph for which every next circuit is
   alternating and every intermediate toggle has the declared component
   behavior;
2. a final perfect augmented matching, or equivalently a complete linkage
   relative to the common graph after all deletions;
3. the required gap/private/socket checks.

Encoding state-dependent topology by simply deleting root-unsafe labels is
also incomplete: a relay may be unsafe at the root and become safe after a
prefix.  One must either supply an explicit ordered packet, or expand the
catalogue state so labels are attached to their actual predecessor states.

## 4. Literal root-safe `m=5` router

The complete one-switch census at the transparent standard root has `1,592`
alternating `C10`s, `654` Hamilton-safe toggles, and exactly `31` outcomes
with lower deficit two, upper deficit two, and augmented deficiency two.
Every one fills one old lower hole and one old upper hole without creating a
new hole.  Their endpoint multiplicities are exactly (0.2).

The complete Hall table is

\[
\begin{array}{c|c|c}
X&N(X)&|N(X)|-|X|\\ \hline
\varnothing&\varnothing&0\\
73&219,365&1\\
146&219&0\\
292&438&0\\
73,146&219,365&0\\
73,292&219,365,438&1\\
146,292&219,438&0\\
73,146,292&219,365,438&0
\end{array}.                                                   \tag{4.1}
\]

The tight singleton rows force `146->219` and `292->438`; then `73->365`
is forced.  The extra edge `73->219` can occur in no perfect router matching.
This proves rank three and the labelled count `10*12*8=960`.

## 5. The frozen ordered private packet

Use the three cyclic circuit orders

```text
C1 = 15 79 77 109 105 361 329 331 267 271
C2 = 147 155 154 218 216 248 240 241 209 211
C3 = 141 173 172 188 180 436 420 421 389 397
```

Their router endpoints and negative protected banks are

\[
\begin{array}{c|c|c|c}
 &\ell\to u& B_L^-&B_U^-\\ \hline
C_1&73\to365&11,104,321&125,335,489\\
C_2&146\to219&26,131,208&159,249,467\\
C_3&292\to438&13,416&175,500
\end{array}.                                                   \tag{5.1}
\]

Every colour in the two negative-bank columns has root multiplicity exactly
two, and the banks are pairwise disjoint on each shore.  Thus all negative
colours retain multiplicity one.  The positive nondefect banks are also
disjoint, and the three desired gains give the forced router matching (0.3).
This proves protected palette monotonicity directly, without using Hall as a
surrogate for multiplicity accounting.

The topology is not static:

* `C1` alone and `C2` alone are Hamilton-safe;
* `C3` alone gives components of sizes `36,216`;
* in the order `C1,C2,C3`, all three intermediate states are Hamilton and the
  final augmented matching has size `210/210`.

Relative to the original and final augmented graphs, the frozen private
packet's common graph has matching size `197`, deficiency `13`, and the final
perfect matching supplies thirteen vertex-disjoint augmenting paths.  The
forced-port audit separately verifies the two private attachment paths.  None
of these facts follows from the three-by-three Hall table.

After this mandatory prefix is fully discharged, the repaired `120+132`
factor and its postrepair gluing labels may enter the private/aligned
graphic--gammoid face.  Router debt must not be silently carried into that
postrepair matroid ground.

## 6. Minimality scope

The finite audits prove:

* no single Hamilton-safe `C6`, `C8`, or `C10` completes the canonical root;
* no Hamilton-safe incidence-hex (`C6`) sequence of depth at most three
  completes it; and
* the displayed ordered three-`C10` packet succeeds.

A separate declared common-exterior two-switch frontier contains no complete
repair.  That frontier is not the class of all overlapping or state-dependent
two-switch sequences.  Consequently the safe conclusion is **three switches
are sufficient in the displayed bounded catalogue**, not that three are
globally minimal among every possible nonstandard repair.

## 7. Audit

Run

```text
python3 scratch/audit_catalan_m5_defect_router_hall_20260731.py
```

The audit reconstructs all `1,592` root-alternating `C10`s, the `654`
Hamilton-safe toggles, all `31` static router macros, the parallel signature
matrix, every Hall row, the unique endpoint matching and `960` labelled
choices.  Separately it replays the frozen packet's signed banks, private
loss reserves, component profiles, defect staircase, final `210/210`
matching, and the authenticated common-core certificate.

Its frozen output is

```text
scratch/catalan_m5_defect_router_hall_20260731.audit.json
```
