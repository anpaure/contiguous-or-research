# Audit of PBBS prefix switching, component packets, and Pascal transfer

Date: 2026-07-30

Files audited:

1. `MATH_THEOREM_R_ALLK_PBBS_PREFIX_SWITCHING_SOCKET_OBSTRUCTION_AND_RETURN_GATE_20260730.md`;
2. `MATH_THEOREM_R_ALLK_PBBS_COMPONENT_SIGNATURE_PACKETS_AND_TWO_SHORE_TRAPS_20260730.md`;
3. `MATH_AUDIT_R_PASCAL_TRANSFER_OF_PERMANENT_SWITCHING_AND_COMPONENT_PRESSURE_20260730.md`;
4. the permanent-switching interface in
   `MATH_THEOREM_R_ALLK_PBBS_SHALLOW_UNIT_CASCADE_PERMANENT_SWITCHING_AND_CAPPED_RUN_GUARD_20260730.md`;
5. the stated Pascal facet/union and promoted-collar interfaces.

Method: independent hand derivation only.  No finite search, SAT, remote
computation, or web access was used.

The theorem files were corrected during this audit.  The verdicts below
refer to their final corrected statements; the listed corrections explain
why the narrower hypotheses are necessary.

## 0. Audit outcome

The following claims are valid.

1. The same-component permanent inequality from item 1997 is exact.
2. The weighted `K_(2,2)`, uniform `K_(2,n)`, and arbitrary uniform
   two-row socket formulas are correct.
3. The reciprocal PBBS four-edge sandwich and the post-prefix isolation
   criterion are exact.
4. The `Q,rho,b,eta` master-bank lemma gives the stated deletion-stable
   prefix estimate.
5. The return-free flat-hull link rigidity theorem is correct on the flat
   interior and intentionally excludes erosion ramps.
6. The component-cube cylinder identity is exact when common edges are
   removed from the exponent.
7. The signature-packet theorem, minimum/average repair inequalities, and
   target-disjoint trap theorem are correct.
8. A Pascal pressure bound of the form `g 2^h Pi_parent+L` is correct under
   a bounded target-projection fibre and a per-child-target lifted-load
   hypothesis.

The following corrections or scope restrictions are necessary.

1. A `K_(2,2)` with both shores conflicting has no row-degree unit, but
   complete failed-literal/arc-consistency lookahead rejects every
   candidate.  It is an abstract cube/permanent obstruction, not a proved
   survivor of the strongest possible PBBS closure.
2. A dead reciprocal rectangle is minimal relative to its two residual
   edges after the fixed background is contracted.  To call its lift an
   inclusion-minimal physical conflict, one must choose an inclusion-minimal
   forced-background subfamily.
3. For a packing lower bound, target-disjointness must include those lifted
   forced-background target sets.  Disjoint residual pairs `{S,R}` alone do
   not suffice, because deletion of one shared forced anchor can hit many
   lifted conflicts.
4. In the Pascal theorem, bounding the number of lifted packets or the
   descendants of each individual packet--target incidence is not enough:
   capping occurs only after all incidences charging one target are summed.
   The corrected theorem uses a child-to-parent target projection of fibre
   at most `g` and bounds each child target's total lifted load by `2^h`
   times the total load at its projected parent target.
5. Current PBBS/Pascal theorems verify none of the global `O(k)` pressure,
   master-bank, component-merger, or promoted-collar hypotheses.  No
   unconditional `B(k)+O(k)` theorem follows.
6. Excluding reciprocal `K_(2,2)` or terminal two-row sockets is not a
   sufficient substitute for the master-bank condition.  An even cycle
   `C_(2n)`, already `C_6`, is rectangle-free but has only two saturating
   shores and the same factor-two obstruction.
7. The reciprocal sandwich equivalence is exact in the raw mandatory-core
   envelope graph, or after vertex-only endpoint deletion.  After arbitrary
   physical candidate-edge pruning, the inclusions remain necessary but
   explicit survival of all four edges must be added.
8. An injective Pascal lift of switch certificates is not enough even when
   supports avoid new collar vertices.  A common outside matching can occupy
   a lifted parent column introduced by a switch output.  Protected transfer
   must require disjointness from the entire common outside matching, or
   directly require that every lifted certificate is a legal child switch
   fixing all outside edges.

## 1. Permanent inequality and switch-bank audit

### 1.1 Same-component injection

For nonexceptional `(M_11,M_00)`, the components containing `e` and `f`
are distinct.  Swapping the `f`-component produces a unique pair in
`Omega_10 times Omega_01` and preserves the product of edge weights.  The
map is inverted by swapping the component containing `f` back.  Therefore

\[
 Z_{11}Z_{00}\le Z_{10}Z_{01}+\mathfrak B_H(e,f).                 \tag{1.1}
\]

The algebraic identity

\[
 Z_{11}Z-(Z_{11}+Z_{10})(Z_{11}+Z_{01})
 =Z_{11}Z_{00}-Z_{10}Z_{01}                                     \tag{1.2}
\]

then gives the claimed pair factor.  **Verdict: valid.**  No negative
association is used.

### 1.2 Fault-tolerant prefix bank

Fix one exceptional full input pair and its master catalogue.  A common
prefix `Theta` of size `h` has `2h` endpoints.  If each endpoint belongs to
at most `rho` certificate supports, at most `2rho h` certificates are
destroyed.  At least `Q-2rho h` descend.  Weighted incidence counting gives

\[
 [Q-2\rho h]\eta\,\mathfrak B_{H\ominus\Theta}(e,f)
 \le bZ_{10}^{\Theta}Z_{01}^{\Theta}.                             \tag{1.3}
\]

The common factor `w(Theta)^2` cancels.  Taking `h=d-1` proves the displayed
condition

\[
 [Q-2\rho(d-1)]\eta\ge bd/\gamma.                                \tag{1.4}
\]

**Verdict: valid**, subject to the explicit hypotheses that support contains
every changed/introduced endpoint, output congestion counts switch
incidences with multiplicity, and no extra non-endpoint pruning is inserted
without rechecking the bank.  For `gamma=0`, one must prove
`mathfrak B=0` directly.

The theorem genuinely removes the need to rebuild a bank after every
prefix only when the catalogue is chosen for the full input before the
common prefix is specified.  If a catalogue is allowed to depend on the
prefix, the statement remains true but no quantifier has been eliminated.

## 2. Socket formulas and reciprocal PBBS criterion

### 2.1 Minimal socket

On weighted `K_(2,2)`, let the two shore products be `A,B` and
`p=A/(A+B)`.  A shore pair has joint probability and both marginals equal
to `p`, hence cylinder ratio `1/p`; the other shore has ratio `1/(1-p)`.
Their maximum is at least two.  Cross statuses `10,01` are absent and no
separating switch exists.  **Verdict: valid and minimal** among simple
bipartite graphs with two disjoint selected edges, two saturating matchings,
and no degree-one target row.

This does not assert a PBBS occurrence.  If both shores are physical
conflicts, failed-literal lookahead detects the isolated core even though
ordinary row-degree unit propagation does not.

The rectangle is only the smallest obstruction.  For every `n>=3`, the
cycle `C_(2n)` is row-degree two and has exactly two saturating matchings.
For two same-shore edges its two marginals and joint probability are all
`1/2`, so the cylinder ratio is two and `Z_10Z_01=0`.  The cycle `C_6` has
no `K_(2,2)` subgraph and no isolated terminal two-row component.  Therefore
excluding (2.3) or checking (2.4) below cannot replace pair control for all
relevant alternating components.

### 2.2 Complete and arbitrary two-row sockets

Uniform `K_(2,n)` has `n(n-1)` saturating matchings.  Direct counting gives

\[
 Z_{11}=1,\quad Z_{10}=Z_{01}=n-2,\quad
 Z_{00}=n^2-3n+3,                                                 \tag{2.1}
\]

and the avoiding matching joins both distinguished edges in one component
iff it uses at least one cross edge.  Inclusion--exclusion gives

\[
                         \mathfrak B=2n-3.                         \tag{2.2}
\]

The exact cylinder ratio is `n/(n-1)`.  **Verdict: valid.**

For two row neighborhoods `A,B`, with `a=|A|`, `b=|B|`, and
`c=|A cap B|`, there are `ab-c` saturating matchings.  For distinct
cross-closed columns, the marginal numerators are `b-1,a-1` and the joint
numerator is one.  Thus

\[
 {\Pr(e,f)\over\Pr(e)\Pr(f)}
 ={ab-c\over(a-1)(b-1)}
 =1+{|A\cup B|-1\over(a-1)(b-1)}.                                \tag{2.3}
\]

**Verdict: valid.**  It is a necessary test on an exposed two-row component,
not a sufficient permanent-expansion theorem for a larger component.

### 2.3 Reciprocal sandwich and isolation

For distinct strict lower targets `S,R` and distinct columns `I,J`, the
four candidates exist in the raw envelope graph iff

\[
 F(I)\cup F(J)\subseteq S\cap R,
 \qquad S\cup R\subseteq P(I)\cap P(J).                           \tag{2.4}
\]

This follows by intersecting the four lower inclusions and uniting the four
upper inclusions, with the converse immediate.  The four vertices form an
isolated rectangle after a vertex-only prefix exactly when their two row and
two column neighborhoods are the displayed pairs.  **Verdict: valid in the
raw/endpoint-deleted envelope graph.**  If closure has pruned individual
candidate edges for physical reasons, (2.4) is only necessary and all four
survival statements must be separately imposed.

The abstract choice `F(I)=F(J)={1}`, `P(I)=P(J)={1,2,3}` with targets
`{1,2},{1,3}` realizes only the sandwich table.  It does not prove that one
PBBS chronology realizes those data or that the rectangle is isolated.

## 3. Dead rectangles and forced-background scope

Let the contracted fixed negative background be `D_x^0` and put

\[
 U=(E_x\cap[t,t+d])\setminus D_x^0.                               \tag{3.1}
\]

Here `D_x^0` must be induced by the compatible forced family of the closed
face, and the four residual rectangle candidates must actually have
survived all prior pruning.

If both labels omit `x`, `U subseteq I union J`, and neither `I` nor `J`
alone contains `U`, each diagonal is a minimal central-run conflict with
respect to its two residual edges.  Swapping the two labels leaves the
interval union and omitted coordinate unchanged.  **Verdict: valid in the
contracted face.**

Two qualifications are essential.

1. The whole deterministic family need not be an inclusion-minimal lift.
   To obtain a minimal physical conflict, choose an inclusion-minimal
   forced-background subfamily which covers the relevant part of
   `D_x^0`.
2. If these rectangles are used for a target-hitting lower bound, the
   target sets of the chosen lifted conflicts, including forced anchors,
   must be pairwise disjoint.  Pairwise disjoint residual target pairs do
   not prevent one shared forced target from hitting many conflicts.

Inside a face where the forced background is held immutable, an isolated
dead rectangle has no physically compatible shore.  In the global literal
alteration problem, deleting a forced-background target is another possible
repair and must be included in the hitting ledger.

## 4. Return-free flat-hull theorem

Suppose `I=[a,b]`, `J=[c,e]` lie in one flat hull and share a candidate.  If
`a<c`, choose `x in P_a setminus P_(a+1)`.  Mandatory cores put `x` in
`F(I)`, while common candidacy puts it in `P(J)`.  Hence it is present at
`a`, absent at `a+1`, and present again in `J`, contradicting return-free
support.  Thus the left endpoints agree.  If `b<e`, the symmetric use of
`P_e setminus P_(e-1)` forces an earlier occurrence, then absence at `e-1`,
then occurrence at `e`; hence the right endpoints agree.

**Verdict: valid when both columns and their convex hull lie in the same
return-free flat interior.**  On a clipped erosion ramp one of
the differences can be empty, so ramp-touching columns require the separate
endpoint ledger.  Deletion cannot create a common candidate, hence the
rigidity conclusion is deletion-stable.

The theorem supplies a genuine PBBS structural restriction: every distinct
external link needs a return, a ramp, or departure from the return-free
hull.  It gives no lower or upper bound on the global number or congestion
of such return links.

## 5. Component-rank cylinder audit

Let `E_0=Theta_0 union (M^0 cap M^1)`.  For a shore-consistent partial
matching `F`, let

\[
 n(F)=|F\setminus E_0|,
 \qquad \rho(F)=\#\{\text{touched alternating components}\}.      \tag{5.1}
\]

The event fixes exactly one fair bit on each touched component, so

\[
 \Pr(F)=2^{-\rho(F)},\qquad
 \prod_{e\in F}x_e=2^{-n(F)},                                    \tag{5.2}
\]

and therefore

\[
 \boxed{\Pr(F)=2^{n(F)-\rho(F)}\prod_{e\in F}x_e.}                \tag{5.3}
\]

**Verdict: valid.**  Replacing `n(F)` by `|F|` in the exact exponent would
be false when `F` contains common or forced edges, whose marginal is one.
The coarse `C_0=2` bound remains valid because
`n(F)-rho(F)<=|F|`.

Conditioning a positive consistent prefix fixes every touched bit and
leaves the other bits independent.  A consistent continuation on a fixed
component contributes ratio one; an inconsistent one has probability
zero.  If common endpoint deletion restricts both shores and the remaining
noncommon components split, the identity applies anew and component rank
can only improve for a retained event.  This is the exact scope of the
deletion-stability assertion.

## 6. Signature packets, repair, and traps

### 6.1 Packet theorem

The packet condition must be

\[
                         \sigma_a\subseteq\sigma_F,                \tag{6.1}
\]

not the reverse: occurrence gives `z supseteq sigma_F`, which must imply
activation `z supseteq sigma_a`.  With this direction and
`H_a cap T(F) ne emptyset`, the activated deletion set hits every occurring
conflict.  Its expected size is exactly the Boolean-cylinder union pressure.

**Verdict: valid.**  No independence between packet activations is used.
The floor follows because deletion-set size is integral.

### 6.2 Exact repair hierarchy

For each cube point let `tau(z)` be the target hitting number of its
occurring conflict hypergraph.  Then

\[
 \tau_\triangle:=\min_z\tau(z)
 \le 2^{-|\mathcal K|}\sum_z\tau(z)
 \le\Pi(\mathcal P).                                               \tag{6.2}
\]

**Verdict: valid.**  The minimum, not the average, is the exact existential
repair invariant for the fixed overlay; average repair and packet pressure
are upper certificates.

### 6.3 Traps

If one component has a shore-0 conflict and a shore-1 conflict, each with
no other noncommon component bit, the selected shore conflict occurs at
every cube point.  Target-disjoint traps force one target per trap.
**Verdict: valid.**

The abstract four-edge core is the smallest shore-changing cube
counterexample without a fixed common conflict.  It has no row-degree unit,
but complete failed-literal/arc-consistency closure rejects it.  It must not
be promoted to an actual fully closed PBBS rectangle without checking
candidate sandwiches, physical pair conditions, extendability, and the
chosen meaning of closure.

## 7. Pascal constants and implication scope

Suppose transported child targets have a projection `pi` to parent targets
with fibres of size at most `g`.  Suppose, for every child target `S'`, the
sum of all its lifted packet-cylinder weights is at most `2^h` times the
full packet load at `pi(S')`, and genuinely new child conflicts have
union-bound pressure `L`.
Then

\[
 \boxed{
 \Pi_{child}\le\overline\Pi_{child}
 \le g\,2^h\overline\Pi_{parent}+L.}                            \tag{7.1}
\]

Indeed each child capped load is bounded by the projected parent load with
factor `2^h`, there are at most `g` children over one parent, and
`min(1,2^hu)<=2^h min(1,u)`.

**Verdict: valid with the displayed projection/load hypotheses.**  Merely
bounding the number of lifted packets, or descendants per individual
incidence, is insufficient if their target channels vary across packets.

For an ordinary one-coordinate Pascal projection, a parent lower target has
at most two set-theoretic child lifts, `S` and `S union {z}`.  Thus `g<=2`
is the natural interior target-projection fibre.  This observation does not
bound the aggregate component-signature load at one child target; that is
the separate per-target hypothesis in (7.1), or must be charged to `L`.

If a child overlay is a component-faithful lift followed by `h` binary
component mergers, a signature rank drops by at most `h`; component splits
only help.  The proved Pascal identities establish envelope and mandatory-
port transport on unbraided interiors.  They do not establish:

1. a component-faithful lift through all cross shores;
2. bounded merger loss at promoted collars;
3. bounded signature-variant multiplicity; or
4. `L=O(k)` for new mixed-shore run/guard conflicts.

The protected switch-bank transfer needs a stronger hypothesis than an
injective candidate/certificate map.  A child input pair must have the form

\[
 (\phi(M_{11})\cup N,\ \phi(M_{00})\cup N),                       \tag{7.2}
\]

where `N` is the same outside matching on both shores, and every lifted
switch support is vertex-disjoint from `V(N)`; equivalently, one may assume
directly that every lifted certificate is a legitimate child switch fixing
all outside edges.  Otherwise an outside edge can occupy an old lifted
right column which a switch output tries to introduce, even if the support
avoids all newly named collar vertices.  Under the protected-extension,
no-new-preimage, and weight hypotheses, the parameters are preserved.  The
child deadline inequality `d'<=d` then preserves the numerical bank
condition.  The opposite Pascal direction can have `d'=d+1` and needs its
own slack check.

All inequalities containing `d/gamma` require `gamma>0`.  For `gamma=0`
one must prove zero same-component exceptional mass.  The actual Pascal
identities alone transport candidate envelopes and ports; they do not
establish a protected switch bank, so even the parent-image preservation
statement remains conditional on the hypotheses just listed.

### 7.1 Safe-column and mixed-depth audit

For an interval of length `a` in an envelope of depth `h`, one cut lies in
exactly `h+a-1` dependency footprints.  Therefore

\[
 Q(h,A)=Ah+{A(A-1)\over2}.
\]

The odd-to-even facet chart has `Q(D+1,D)=D(3D+1)/2`.  Charging both
oriented sides of `c` cuts gives `|U|<=cD(3D+1)` unsafe columns.  Each of
two supplied matchings uses each such column at most once, so omitting every
target incident with `U` on either shore costs at most

\[
                         2|U|\le2cD(3D+1).                         \tag{7.3}
\]

After deletion, fragments of one old alternating component must retain one
tied old bit.  Independently resampling split fragments can create new
hybrid conflicts.  With tied bits, safe-sector signature probabilities are
unchanged.  **Verdict: valid.**  For `c=O(1)` and `D^2=O(k)`, this is an
`O(k)` transfer toll, conditional on the complete mixed-depth sector
pressure being `O(k)`.

The mixed run polynomial is not termwise dominated by the standard one.  On
the odd-to-even facet shore, the envelope has depth `D+1` but the child
physical run horizon is `D`.  A positive envelope component of exactly
`D+1` positions, supplied at its positions by distinct positive-marginal
singleton candidates, contributes one child run term and no standard
depth-`D+1` parent run term.  This does not prove that the full standard
run-plus-guard pressure is zero or rule out a separate aggregate charging
theorem; it proves that the current standard theorem supplies no termwise
comparison.  The `K_(2,N)` deletion example separately proves that endpoint-
prefix permanent control is not right-column-deletion hereditary.  These
are exact logical counterexamples, not assertions that a particular PBBS
lift realizes their full local tables.

## 8. Final boundary

The permanent inequality, socket formulas, return gate, component-cylinder
law, packet theorem, and conditional Pascal ledgers are rigorous.  They do
not prove an unconditional additive theorem.

The remaining positive PBBS obligations are now explicit:

1. close the forced unit cascade with `O(k)` omissions;
2. either provide direct prefix control/a master return--guard bank
   satisfying (1.4) for every relevant pair in every alternating component,
   or build two closed matchings with
   `tau_triangle=O(k)` / packet pressure `O(k)`;
3. exclude or jointly hit every superlinear reciprocal-trap and common-run
   packing, with forced-background targets included; and
4. preserve the chosen certificate through Pascal with bounded
   packet--target multiplicity, component merger loss, and new-collar
   pressure.

None is currently proved for the actual all-`k` PBBS/Pascal chronology.
Accordingly the correct conclusion remains conditional; no
`B(k)+O(k)` theorem is claimed.

**Final verdict on the corrected files:** valid under their displayed
conditional hypotheses.  **Unsupported:** existence of the required PBBS
master bank, an `O(k)` component-packet repair bound, and preservation of
either property by the actual all-`k` Pascal braid.
