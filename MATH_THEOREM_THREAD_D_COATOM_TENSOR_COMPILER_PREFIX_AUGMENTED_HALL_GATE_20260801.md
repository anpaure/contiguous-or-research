# Coatom tensor versus the compiler prefix: the exact augmented-Hall gate

Date: 2026-08-01  
Lane: Thread D, additive-constant transparent packets  
Status: exact reduction and exact fail-closed obstruction for the currently
exported macro interface; **not** a physical no-go for an embedded tensor

## 0. Verdict

The coatom-screen tensor closes the local owner, Johnson, both immediate
palettes, upper-union and residence rows.  Specifically, it uses union
screens at the zero-based transitions

\[
                              \{1,3,5,7\}                         \tag{0.0}
\]

and lower intersection screens elsewhere; all owners are then distinct.
This authoritative mixed-screen packet, however, does not name a literal
compiler cell.  In particular, the coordinate labels deleted on Johnson
transitions are not cells of the staircase compiler.

Consequently the present macro does not yet exhibit a member of a fixed
unused compiler basis, and it does not yet define a joint
lower-target--packet matching instance with a positive packet degree.  Under
the mandatory fail-closed interpretation, its exported packet list is

\[
                              A_\tau=\varnothing .                 \tag{0.1}
\]

The packet singleton is then an exact Hall cut of deficiency one:

\[
                  |N(\{\tau\})|=0<1=|\{\tau\}|.                  \tag{0.2}
\]

This is an interface obstruction, not a theorem that no physical embedding
can work.  The missing data are a global staircase address, a phase-common
trace-guarded target--cell bank, and a nonempty list of physically certified
deletion cells.

This note gives the exact test once those data are supplied.  It is a single
ordinary augmented matching at the componentwise worst residence frontier.

## 1. The two resource types must not be identified

Let the filler set of the tensor be

\[
 F=\{f_0,\ldots,f_{n-1}\},\qquad C_i=F-\{f_i\}.
\]

The Johnson transitions have coordinate deletion/insertion labels.  For
example, inside a coatom block the transition `C_i -> C_(i+1)` deletes
`f_(i+1)` and inserts `f_i`.  At an intersection screen the left transition
deletes the departing active coordinate and inserts `f_(n-1)`, while the
right transition deletes `f_0` and inserts the entering active coordinate.
The union-screen repair merely interchanges these two kinds of bridge.

A compiler cell is instead a physical interval/address object such as

\[
                         C_{s,\ell}=[s,s+\ell-1],                 \tag{1.1}
\]

together with the literal capped value and its trace guard.  A coordinate
`f_i`, an active deletion label, a screen owner, and a compiler cell are four
different resource types.  No map from a tensor transition to a cell
`C_(s,ell)` is present in the tensor theorem or its audits.  In particular,
the facts that `f_i` is absent once per block and that the two phases have the
same owner set do not certify an unused compiler cell.

The same warning applies to the superseded all-intersection version's four
repeated screens.  They were rank-`r` owner defects, not four lower-compiler
deletion tasks.  The fixed schedule (0.0) repairs them locally with zero
sidecar, but it does not create a compiler-cell label.

## 2. The exact phase-common bank

Suppose a physical embedding of the macro is now fixed.  For the moment also
assume a **shared-bank menu**: there is one option-independent guarded bank
such that every candidate option preserves every one of its edges and trace
guards off that option's named cell.  Let

\[
                        H^\epsilon=(\mathcal L,C;E^\epsilon),
                        \qquad \epsilon\in\{0,1\},                \tag{2.1}
\]

be this bank in the two phases.  An edge `(T,c)` is in
`E^epsilon` only when the literal cell `c` caps the lower target `T` and the
full trace guard is valid in that phase.  Define the phase-common bank

\[
                          H^\cap=(\mathcal L,C;
                          E^0\cap E^1).                            \tag{2.2}
\]

This edgewise intersection is the exact object for a *single fixed matching
surviving both phases*.  Deleting every cell which has even one changed
incidence is a sound but generally stronger coarse relaxation; it is not the
exact test.

Let `R` be the finite reachable family of residence states, including both
macro phases and every allowed exterior state.  Put

\[
   \rho^*_\ell=\max_{\rho\in R}\rho_\ell,
   \qquad D^*=D(\rho^*),
   \qquad H^*=H^\cap[\mathcal L,C-D^*].                           \tag{2.3}
\]

The tensor's equal clipped boundary states imply that its two local phases
do not enlarge `rho*` relative to one another.  The exterior and the global
staircase schedule still have to be included in `R`.

Finally let

\[
                            A_\tau\subseteq C                      \tag{2.4}
\]

be the **physically certified** deletion list of the embedded packet.  A
cell belongs to `A_tau` only if the option literally deletes/reserves that
cell and preserves the declared option-independent bank off that cell in
both phases.  Put

\[
                            A^*=A_\tau-D^*.                        \tag{2.5}
\]

## 3. Exact one-packet theorem

### Theorem 3.1 (common-phase augmented Hall)

The following are equivalent.

1. There is a literal packet cell `beta in A*` and one trace-guarded
   matching which saturates every lower target in both phases, dominates
   every frontier in `R`, and does not use `beta`.
2. For some `beta in A*`,

   \[
        \nu\bigl(H^\cap[\mathcal L,
               C-(D^*\cup\{\beta\})]\bigr)=|\mathcal L|.         \tag{3.1}
   \]

3. The augmented graph `G_tau` with left shore
   `mathcal L disjoint union {tau}`, right shore `C-D*`, target edges from
   `H*`, and packet edges `tau--A*` has a matching of size
   `|mathcal L|+1`.
4. For every `X subseteq mathcal L`, both exact Hall families hold:

   \[
   \begin{aligned}
      |N_{H^\cap}(X)-D^*|&\ge |X|,\\
      |(N_{H^\cap}(X)\cup A_\tau)-D^*|&\ge |X|+1.
   \end{aligned}                                                  \tag{3.2}
   \]

#### Proof

The residence frontier theorem says that one matching works for every
`rho in R` exactly when it avoids `D*`.  Being an edge of `H^cap` says
literally that the same selected incidence and trace guard work in both
phases.  Thus item 1 is precisely item 2.

Match `tau` to `beta` and the lower targets to the matching in (3.1).  This
gives item 3; restriction of a matching in item 3 gives the converse.
Every left subset of `G_tau` is either `X` or `X union {tau}`.  Hall's
theorem therefore gives exactly the two rows in (3.2).  \(\square\)

The exact deficiency is

\[
\begin{aligned}
 \delta_\tau
 &=|\mathcal L|+1-\nu(G_\tau)\\
 &=\max\Bigl\{0,
      \max_{X\subseteq\mathcal L}
       (|X|-|N_{H^\cap}(X)-D^*|),\\
 &\hspace{39mm}
      \max_{X\subseteq\mathcal L}
       (|X|+1-|(N_{H^\cap}(X)\cup A_\tau)-D^*|)
             \Bigr\}.                                            \tag{3.3}
\end{aligned}
\]

Thus a failed computation has a literal alternating-reachability Hall
witness, not merely a scalar-capacity deficit.

If the baseline bank `H*` is feasible, the one-task deficiency is either
zero or one.  Moreover failure has the particularly sharp form

\[
   \exists X\subseteq\mathcal L:\qquad
   |N_{H^*}(X)|=|X|\quad\hbox{and}\quad A^*\subseteq N_{H^*}(X). \tag{3.4}
\]

Indeed baseline Hall gives `|N(X)|>=|X|`; the packet row can fail only when
equality holds and every packet option is trapped in that tight shore.  This
is the exact nontrivial obstruction to seek after a physical embedding.  It
is equivalently a dual-rank-zero cut: every element of `A*` is a loop of
`M_(H*)^*`, equivalently a coloop of the primal transversal matroid.

### Corollary 3.2 (literal fixed-unused-basis test)

Assume a particular matching `M_0 subseteq E(H^cap)` saturates
`mathcal L` and avoids `D*`.  Put

\[
             B^*=(C-D^*)-\operatorname{cells}(M_0).               \tag{3.5}
\]

The literal same `M_0` survives both phases and the packet if and only if

\[
                              A_\tau\cap B^*\ne\varnothing.       \tag{3.6}
\]

Any `beta` in this intersection is the requested unused-cell deletion
label.

#### Proof

Such a `beta` is outside the residence ideal and unused by `M_0`; packet
bank-transparency leaves every selected incidence and trace guard unchanged.
Conversely any named packet cell avoided by the fixed matching lies in
`B*`.  \(\square\)

Before fixing `M_0`, the fixed-basis test (3.6) is replaced by the one-task
dual-Rado condition

\[
                         r_{M_{H^*}^*}(A^*)\ge1.                  \tag{3.7}
\]

For several packets, replace `{tau}` by the task set and apply the full
dual-Rado/augmented-Hall inequalities.  Nothing new is gained by treating
the two phases separately when one common matching is required.

The whole-cell set called `D_mac` in the companion tensor/interface note is
not a substitute for `A_tau`.  `D_mac` is a conservative bank of cells to be
avoided because some incidence may change; `A_tau` is a list of literal
packet resources from which one cell is deliberately selected.  If a future
construction wants the selected packet cell also to pay a residence or
invariance reservation, it needs an explicit shared-deletion theorem.
Under the present distinct-reservation convention one must use
`A*=A_tau-D*` exactly as above.

The shared-bank quantifier is load-bearing.  If candidate `b` has its own
phase-common bank `H_b^cap`, then lists from different candidates may not be
merged into one augmented task row.  The exact general menu test is instead

\[
 \exists b\in A_\tau:\qquad
 \nu\bigl(H_b^\cap[\mathcal L,C-(D^*\cup\{b\})]\bigr)
       =|\mathcal L|.                                             \tag{3.8}
\]

The augmented graph of Theorem 3.1 is exact precisely on the stronger
shared-bank face stated at the start of Section 2.

## 4. Application to the current tensor export

The current tensor artifacts contain:

* the two local rank-`r` owner words;
* common endpoints and Johnson adjacency;
* exact prefix/suffix and internal interval-OR data;
* clipped residence state and internal run certificates; and
* an exact simple owner path with no owner sidecar.

They do not contain:

* a global staircase start for the fragment;
* a physical cell set `C` or maximal envelopes;
* the lower target shore `mathcal L`;
* phase-labelled target--cell incidences and their trace guards; or
* a packet-to-cell list `A_tau`.

Accordingly no literal `beta` can be extracted from the present theorem.
The fail-closed exported list is (0.1).  Taking `X=emptyset` in the second
row of (3.2) gives precisely (0.2).  If the baseline worst-frontier bank is
feasible, then (3.3) gives

\[
                              \delta_\tau=1.                      \tag{4.1}
\]

If the baseline bank is itself deficient, the isolated packet row adds one
to that baseline obstruction.  This statement is exact for the exported
interface and makes no claim about a future physical embedding.

## 5. Minimal positive certificate still needed

One physicalized tensor packet closes the compiler gate by exporting only
the following finite certificate.

1. One global placement and its literal staircase cell catalogue `C`.
2. The common guarded edge bank `H^cap`, shared by every candidate option
   off its named cell, or option-indexed banks `H_b^cap`; alternatively one
   fixed matching `M_0` whose selected incidences are individually replayed
   in both phases and under the chosen option.
3. The reachable worst frontier `rho*`.
4. A nonempty packet list `A_tau` with a replay proving, for every listed
   cell, physical deletion and bank-transparency.
5. Either one `beta in A_tau cap B*` or a matching/Hall certificate for
   `G_tau`.

For the desired strongest route, item 5 is a single fixed matching and one
literal cell.  No new compiler theorem is required.  The unresolved work is
constructing these physical data for the coatom macro.

## 6. Scope audit

The lightweight audit

```text
python3 scratch/audit_threadD_coatom_tensor_compiler_prefix_gate_20260801.py
```

records the dependency hashes, replays the isolated packet Hall row, and
checks the conditional fixed-basis and augmented-matching examples.  Its
empty exported list is the declared fail-closed interpretation of the
theorem's explicit U5-open scope, not a computed physical no-go.  The audit
does not manufacture a cell label.

Dependencies:

* `MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md`;
* `MATH_THEOREM_INDEPENDENT_COATOM_SCREEN_TENSOR_ZERO_DEFECT_AND_COMPILER_INTERFACE_20260801.md`;
* `MATH_THEOREM_INDEPENDENT_UNUSED_BASIS_FRONTIER_MATCHING_AND_MOBILITY_20260731.md`;
* `MATH_THEOREM_PROSPECTIVE_COMMON_BASIS_AVOIDANCE_AND_COMPILER_DUAL_RADO_20260731.md`; and
* `MATH_THEOREM_O1_TRANSPARENT_PACKET_UNUSED_BASIS_COMPOSITION_20260731.md`.
