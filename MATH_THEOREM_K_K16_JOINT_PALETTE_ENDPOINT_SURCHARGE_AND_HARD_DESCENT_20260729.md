# The `k=16` joint-palette endpoint surcharge and the hard descent potential

Date: 2026-07-29  
Lane: K  
Status: **exact internal radius-98 obstruction; unconditional global potential theorem; exterior radius-98 portal tier still open**

## 0. Result and scope

All numerical `k=16` statements below use the **loopless `C_15` quotient
catalogue** of the frozen model.  Quotient loops and non-equivariant physical
edges lie outside their scope.  Let `F_1` be the audited re-centered quotient
factor

```
scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json
SHA-256 d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8.
```

Its positive short-residence motif hypergraph has ordinary transversal and
packing number

\[
 \tau(F_1)=\nu(F_1)=97.
\tag{0.1}
\]

There are then two different one-unit surcharges.

1. At radius 97, every minimum motif cut deletes edge `22511`, the unique
   represented provider of upper-q1 colour `(1,1907)`.  Retaining that edge
   raises the minimum internal motif cut from 97 to 98.
2. At internal radius 98, all 85 overlap-component domains and all 7,761
   internal seams have now been solved exactly.  Degree alone is feasible;
   degree plus the lower palette is feasible; degree plus the upper palette
   is feasible.  Degree plus both palettes is infeasible even when top
   residence is removed.  Thus the second surcharge is a genuinely joint
   lower/upper endpoint-conditioned obstruction, not another unique row,
   not either palette separately, and not top chronology.

Writing `rho_LU^int` for the one-step current-motif-hitting completion radius
restricted to this 466-node internal atlas, the exact conclusion is

\[
 \boxed{\rho_{LU}^{\rm int}(F_1)\ge99.}
\tag{0.2}
\]

This does **not** yet prove the loopless-quotient global inequality
`rho_LU(F_1)>=99`.  Every global radius-98 repair omitted by the internal product lies in one
explicit exterior-provider tier.  It cuts `22511`, spends the one surplus
cut outside the 390-edge motif union, and uses one of 14 q1 replacement
providers crossing to one of seven outside nodes.  Each outside node has two
possible incident source cuts, giving 28 provider/cut portal incidences.
That finite tier remains unsolved.

The precise loopless-quotient global statement currently proved is therefore

\[
 \boxed{\rho_{LU}(F_1)\ge98,}
\tag{0.3}
\]

together with (0.2) on the internal branch.  Here a completion only cuts
every **current** motif; it may create fresh motifs and require another CEGAR
round.  The phrase “full-hard radius at
least 99” is valid only with the superscript `int` until the portal tier is
closed.

## 1. Endpoint-conditioned palette deficiency

Let `F` be an exact degree-two factor in a fixed finite edge universe.  Every
edge has a lower q1 label `lambda(e)` and an upper q1 label `upsilon(e)`.
For a source cut `D subseteq F`, define its endpoint deficit

\[
 b_D(v)=d_D(v).
\tag{1.1}
\]

Let

\[
 \mathcal B_F(D)=\{A\subseteq E^+_F:
 d_A(v)=b_D(v)\text{ for every }v\}
\tag{1.2}
\]

be the family of off-factor seam sets restoring every endpoint degree.
The equality in (1.2) automatically gives `|A|=|D|`.

Let the lower and upper row universes consist only of rows represented by
the source `F`, with the palette tag retained.  The genuinely lost lower and
upper row sets are

\[
 L_D=\{\ell:P_F(\ell)\subseteq D\},
 \qquad
 U_D=\{u:P_F(u)\subseteq D\},
\tag{1.3}
\]

where `P_F(q)` is the selected provider set of row `q`.  Put

\[
 \delta_{LU}(D)=
 \min_{A\in\mathcal B_F(D)}
 \bigl(
 |L_D\setminus\lambda(A)|+
 |U_D\setminus\upsilon(A)|
 \bigr),
\tag{1.4}
\]

with value infinity if `B_F(D)` is empty.  Define `delta_L` and `delta_U`
by retaining only the corresponding term.

For radius `r`, let `D_r(F)` be all size-`r` source cuts hitting every
current residence motif, and set

\[
 \Delta_{LU}(r;F)=
 \min_{D\in\mathcal D_r(F)}\delta_{LU}(D).
\tag{1.5}
\]

### Theorem 1.1 (exact coloured b-factor criterion)

A degree-two, both-q1-preserving current-motif-hitting rethread of radius `r`
exists if and only if

\[
 \Delta_{LU}(r;F)=0.
\tag{1.6}
\]

Consequently

\[
 \rho_{LU}(F)=
 \min\{r\ge\tau(F):\Delta_{LU}(r;F)=0\}.
\tag{1.7}
\]

#### Proof

If `F'=(F\setminus D)\cup A` is a degree-two completion, its deleted and
added incidences agree pointwise, so `A in B_F(D)`.  A q1 row can disappear
only if all its source providers lie in `D`; these are exactly the rows in
(1.3).  Both palettes survive precisely when every row in `L_D` and `U_D`
is represented by `A`, which is `delta_LU(D)=0`.

Conversely, if `D` hits all motifs and `A in B_F(D)` attains zero in (1.4),
then the endpoint equations make `(F-D) union A` degree two and the zero
deficiency restores every genuinely lost lower and upper row.  This proves
(1.6), and minimizing the radius gives (1.7).  QED.

An equivalent maximum-coverage form is useful.  Let `Q_L` and `Q_U` be
disjointly palette-tagged copies of the complete source-represented lower and
upper row universes.  For `Q subseteq Q_L disjoint-union Q_U` put

\[
 \operatorname{rk}_r(Q)=
 \max_{\substack{D\in\mathcal D_r(F)\\A\in\mathcal B_F(D)}}
 \sum_{q\in Q}
 \mathbf1[(F\setminus D)\cup A\text{ represents }q].
\tag{1.8}
\]

Then radius `r` works exactly when

\[
 \operatorname{rk}_r(Q_L\cup Q_U)=|Q_L|+|Q_U|.
\tag{1.9}
\]

This is the exact endpoint-conditioned coloured-b-factor coverage invariant
behind the second surcharge.  “Hall--Tutte” is descriptive here: (1.8) is
not asserted to be submodular or a matroid rank.  Separate feasibility of the endpoint
`b`-factor, of the lower deck, and of the upper deck does not imply (1.9).

There is also an exact scalar endpoint invariant.  If `d_AA,d_AB,d_BB` and
`a_AA,a_AB,a_BB` are the deleted and added sector counts, then counting
deficit incidences separately on the two shores gives

\[
 2a_{AA}+a_{AB}=2d_{AA}+d_{AB},
 \qquad
 2a_{BB}+a_{AB}=2d_{BB}+d_{AB}.
\tag{1.10}
\]

Therefore

\[
 a_{AA}-d_{AA}=a_{BB}-d_{BB}
 =-\frac{a_{AB}-d_{AB}}2,
\tag{1.11}
\]

and in particular `a_AB` and `d_AB` have the same parity.  Every feasible
relaxation witness obeys (1.10).  These scalar identities do not explain the
joint no-go: they are already enforced by the full endpoint equations in
all four diagnostic models.

## 2. A solver-free collision inequality

For a fixed cut `D`, let `C_D` be the bipartite compatibility graph on
`L_D union U_D`: join `ell` to `u` if some allowed seam carrying the pair
`(ell,u)` can occur in an endpoint-restoring `b_D`-factor.  For
`L' subseteq L_D` and `U' subseteq U_D`, let

\[
 \kappa_D(L',U')
\tag{2.1}
\]

be the maximum size of a label matching among seams of one
endpoint-restoring completion whose two labels lie in `L' times U'`.

### Lemma 2.1 (endpoint-conditioned collision bound)

If `r` seams restore every row in `L' union U'`, then

\[
 \boxed{|L'|+|U'|\le r+\kappa_D(L',U').}
\tag{2.2}
\]

#### Proof

Choose one provider seam for every row of `L'` and every row of `U'`.
Within each palette these witnesses may be chosen injectively because one
seam has only one label of that palette.  The two witness images are subsets
of the same `r` seams, so they overlap in at least

\[
 |L'|+|U'|-r
\]

seams.  On the overlap, both lower and upper witness maps are injective;
hence those seams give a matching in `C_D`.  This proves (2.2).  QED.

A violation of (2.2) is a solver-free Hall certificate.  Satisfaction of
all such elementary collision inequalities need not be sufficient: the
chosen double-provider seams must still coexist in one exact endpoint
`b`-factor.  The complete invariant remains (1.4) or (1.8).

No smaller named-row violation of (2.2) has yet been extracted from the
radius-98 transcript.  The proved finite obstruction should therefore be
described as a **global coloured b-factor rank defect**, not as a presently
known small ordinary Hall set.

This distinction is substantive rather than terminological.  A claimed
equivalent 8,024-variable internal encoding has a feasible 1,597-row GLOP
relaxation.  Its frozen floating-status summary reports 533 variables
strictly fractional at tolerance `1e-7`.  No fractional vector is stored,
and the 1,597-row LP proto has not been diffed constraint-by-constraint
against the 1,525-row CP diagnostic.  This is therefore a trusted floating
diagnostic, not a rigorous certificate.  It says only that this displayed
LP supplies no Farkas no-go; it does not exclude a valid integral blossom
inequality.  The number 533 is not an invariant or a rational denominator.

## 3. Exact internal radius-98 ladder

The motif-intersection graph has 85 components with disjoint edge supports.
After forbidding deletion of the locked provider `22511`, their local
minimum transversal domains have

\[
 \sum_i|\mathcal D_i|=262,
 \qquad
 \max_i|\mathcal D_i|=8,
\tag{3.1}
\]

and domain-size histogram

\[
 1^{10}2^{17}3^{31}4^{21}5^1 6^2 8^3.
\tag{3.2}
\]

The number 262 is the sum of local domain sizes, not the number of global
cuts.  Their Cartesian product contains exactly

\[
 32814901619680178026914088287480053760
\tag{3.3}
\]

cut banks.  The compressed model quantifies over this entire product.

Every cut has size 98.  The union of all local option edges has size 267;
the full current motif union has size 390 and touches 466 quotient nodes.
There are 7,761 loopless off-factor seams on those nodes.

The exact relaxation ladder is:

| hard rows | result | final lower support | final upper support |
|---|---:|---:|---:|
| degree only | feasible | 707 | 706 |
| degree + lower q1 | feasible | 764 | 710 |
| degree + upper q1 | feasible | 715 | 764 |
| degree + both q1, top relaxed | infeasible | -- | -- |
| degree + both q1 + top | infeasible | -- | -- |

The three positive rows are literal selected factors, independently replayed
against the catalogue.  Their cut/lost-row counts are respectively

\[
\begin{array}{c|c|c|c}
 & |D| & |L_D| & |U_D|\\ \hline
\text{degree only}&98&73&71\\
\text{lower hard}&98&67&75\\
\text{upper hard}&98&69&71.
\end{array}
\tag{3.4}
\]

Thus, in the rank notation of (1.8),

\[
 \operatorname{rk}_{98}^{\rm int}(Q_L)=|Q_L|,
 \qquad
 \operatorname{rk}_{98}^{\rm int}(Q_U)=|Q_U|,
\tag{3.5}
\]

but the joint infeasibility gives

\[
 \operatorname{rk}_{98}^{\rm int}(Q_L\cup Q_U)
 \le |Q_L|+|Q_U|-1.
\tag{3.6}
\]

Equation (3.6) is exactly the invariant that costs the second extra unit.
It proves a lower bound, not feasibility at radius 99.

The top-relaxed compressed transcript has 8,024 variables and 1,525
constraints; the frozen solve reports `INFEASIBLE`.  The full top model has
23,980 variables and 18,411 constraints and also reports `INFEASIBLE` in
its first round.  These are trusted exact CP-SAT transcripts, but neither
has a separately checked proof log.  The model-to-combinatorics reduction is
literal and independently replayed; the infeasibility status retains this
solver-trust qualification.

## 4. Complete radius-98 tier decomposition

Let the disjoint motif-component edge supports be `E_i`, let

\[
 E=\bigcup_iE_i,
\]

and let `tau_i` be the ordinary local transversal number.  Since
`sum_i tau_i=97`, every motif-hitting cut `D` satisfies the identity

\[
 \boxed{
 |D|-97
 =|D\setminus E|
  +\sum_i\bigl(|D\cap E_i|-\tau_i\bigr).
 }
\tag{4.1}
\]

Every term is nonnegative.  Hence a radius-98 cut spends exactly one surplus
unit in exactly one of two ways.

### Branch A: internal lock-safe product

Retain `22511`.  The exceptional overlap component then needs two cuts,

\[
 \{22520,22692\}
 \quad\text{or}\quad
 \{22520,25634\},
\tag{4.2}
\]

instead of its ordinary one.  No cut lies outside `E`.  This is precisely
the 85-domain, 262-local-value product closed by (3.6).

### Branch B: one exterior provider portal

Cut `22511` at the ordinary local minimum and spend the unique surplus unit
on one source edge outside `E`.  The locked colour `(1,1907)` has 36 global
provider edges, only one selected in `F_1`, and no alternative whose two
endpoints both lie in the 466-node internal atlas.  Exactly 14 alternatives
have one endpoint inside and one endpoint outside.  Their seven outside
nodes are

\[
 97,490,502,546,581,620,623.
\tag{4.3}
\]

Each has exactly two incident selected source edges outside `E`; these 14
exterior cut choices are

\[
\begin{array}{c|c}
97&4228,4936\\
490&18085,18185\\
502&18647,18659\\
546&20328,20359\\
581&21573,21581\\
620&22775,22790\\
623&22847,22858.
\end{array}
\tag{4.4}
\]

The remaining 21 alternative providers have both endpoints outside the
internal atlas.  A single exterior cut supplies the only two outside
endpoint deficits.  Such a provider could occur only if its endpoint pair
were exactly the endpoint pair of that cut; the literal census contains no
such pair.  Hence the 14 crossing providers above are the complete
one-exterior-cut replacement bank.

Thus the first portal index has 28 incident provider/cut choices.  The
remaining degree and palette choices are still coupled to the 85 ordinary
component domains, so 28 is not the total number of global completions.

There are four literal degree-balanced two-edge portal switches.  They do
restore `(1,1907)`, but lose respectively

\[
 \text{upper }(1,4979),
\tag{4.5}
\]

\[
 \text{lower }(1,1139)\text{ and upper }(1,3699),
\tag{4.6}
\]

\[
 \text{upper }(1,5747),
\tag{4.7}
\]

and

\[
 \text{upper }(1,2033).
\tag{4.8}
\]

These switches prove that the portal tier is genuine; they do not close it,
because the other 96 motif cuts and seams can participate in a global
palette repair.

Equations (4.1)--(4.4) are the exact next finite master.  A
loopless-quotient global radius-98 no-go requires solving or proving
infeasible every Branch-B portal submodel.

For completeness, the loopless-quotient global radius-97 lower bound in
(0.3) is solver-free.  Every radius-97 motif hitter is minimum in each
disjoint overlap component and therefore lies in the motif union.  Its
exceptional local minimum cuts `22511`.  Endpoint balance confines all added
endpoints to the 466 motif nodes, where `(1,1907)` has no alternative
provider.  Hence no radius-97 degree/q1 completion exists.

## 5. The correct iterative hard potential

The internal 466-node atlas is source-centered and is not reverse closed.
It therefore cannot itself serve as a Lyapunov domain after re-centering.
The correct potential is global.

Fix a reverse-closed class `W` of equal-size exact factors on one physical
edge universe.  It may impose degree two, both q1 palettes, top residence,
or any larger fixed wrapper.  For `F in W`, define

\[
 \Phi_{\mathfrak W}(F)=
 \min\bigl\{|F\setminus G|:
 G\in\mathfrak W,
 F\setminus G\text{ hits every motif of }F
 \bigr\},
\tag{5.1}
\]

with value infinity if no such completion exists.

### Theorem 5.1 (hard re-centering Lyapunov theorem)

If `G` attains (5.1), then

\[
 \boxed{\Phi_{\mathfrak W}(G)\le\Phi_{\mathfrak W}(F).}
\tag{5.2}
\]

Moreover, `Phi_W(F)=0` if and only if `F` is resident.  If equality holds in
(5.2), the reverse transition is also an exact minimum; hard plateaux are
symmetric.

#### Proof

Put `D=F-G` and `A=G-F`.  Since `D` hits every old motif, common-collar
inheritance says that every motif of `G` meets `A`: a motif using only common
edges would already be an uncut motif of `F`.  Replacing `A` by `D` returns
the wrapper-valid factor `F`, so the reverse transition is admissible in
(5.1).  Therefore

\[
 \Phi_{\mathfrak W}(G)\le|A|=|D|=\Phi_{\mathfrak W}(F).
\]

If `F` is resident its motif family is empty and `G=F` gives value zero.
If it is nonresident, every admissible cut hits a nonempty motif and has
positive size.  Equality in (5.2) makes the reverse bank an admissible cut
of the same minimum size, proving the plateau statement.  QED.

This is the potential required for iterative descent.  Neither the static
lock-safe number nor the surcharge

\[
 \Phi_{\mathfrak W}(F)-\tau(F)
\]

is separately monotone.  Nor is the hard radius generally equal to
`tau+delta`: one extra cut can change several endpoint and palette
capacities at once.  The exact hierarchy at the present internal state is

\[
 97=\tau(F_1)
 <98=\widehat\tau_{\rm lock}^{\rm int}(F_1)
 <\rho_{LU}^{\rm int}(F_1),
\tag{5.3}
\]

where the last quantity is at least 99.  Globally, only the first strict
inequality has been proved because Branch B remains open.

## 6. Sharp remaining theorem

The next theorem is no longer another local motif-transversal calculation.
It is exactly one of the following.

1. **Portal closure:** prove every one-exterior-cut Branch-B coloured
   `b`-factor has positive joint deficiency, yielding the global bound
   `rho_LU(F_1)>=99`.
2. **Portal construction:** find one Branch-B factor with
   `delta_LU=0`, then impose top residence and separate its new motifs.

If radius 99 is then tested, its full tier decomposition must be rebuilt;
the present result gives no assertion that radius 99 is feasible.  For
iteration, every accepted transition must minimize the global potential
(5.1), not merely the source-centered internal relaxation.

## 7. Frozen artifacts

Internal product and exterior-tier independent replay:

```
scratch/audit_k16_r98_joint_endpoint_surcharge_20260729.py
SHA-256 a8b203927432cda93f0b63b2ecc3bda6a8c71328f3c2d8e3bf33b47fd52c00e4

scratch/k16_r98_joint_endpoint_surcharge_20260729.audit.json
SHA-256 000ed4e05ea3942e97d24a842e3c1c2dbf216352b781e617b6dc654bf58a2841
```

The audit performs no optimization.  It reconstructs all 147 motifs, all 85
components and 262 local values, literally replays the three feasible
relaxation witnesses, checks both infeasibility transcripts' model scope and
censuses, and enumerates the 14-provider/seven-node portal tier and four
degree-balanced two-switches.

Full internal q1/top transcript:

```
scratch/threadD_k16_r98_options_exact_s16852_final_20260729.json
SHA-256 36ddffda58aed8623ea29d1180ec2d84335db558760d9e9906582173668d97d9

scratch/threadD_k16_r98_options_exact_s16852_final_20260729.log
SHA-256 46071f21b70042b64b16a5e84fd1faa7201fdd32e1d4983b00f940c2f87c8c35

scratch/threadD_k16_r98_options_exact_s16852_final_20260729.model.pb
SHA-256 f795d28db81c6e6573a1846e4954270c3ef1b31b0c6ac3f7c6ffe60d87ed41c6
```

Top-relaxed ladder:

```
scratch/r98_option_ladder_20260729/k16_r98_options_diag_degree.json
SHA-256 bff16a435317fe28d0305944fc4c4ca1c80858d38ac15a895d24cd3efaecf5f4

scratch/r98_option_ladder_20260729/k16_r98_options_diag_lower.json
SHA-256 f280e237915877c9514f5e66c486634140d3424fa12c7147c641b244e567957d

scratch/r98_option_ladder_20260729/k16_r98_options_diag_upper.json
SHA-256 4607b330d5ad88ac1066373a6391d3a285db7a087001e457e81980144343de04

scratch/r98_option_ladder_20260729/k16_r98_options_diag_both.json
SHA-256 3cb81acedba9ae8e17ead1128087619d4667bf915234ea84c0f9c411263e0815
```

Feasible joint LP relaxation:

```
scratch/k16_r98_both_lp_relaxation_20260729.audit.json
SHA-256 658af1a808fd2369a9a51fbbb9a452947fb7da296d9bdedeeaf847fe47ccf586

scratch/threadD_k16_r98_toggle_both_s16853_20260729.model.pb
SHA-256 f34110ade1ea754159e1d91a19a6d0541fb18ce81a6b86e5dbdb825c1d991811
```

The internal no-go has no independently checked proof log.  The LP statement
is likewise only a trusted floating transcript without a stored primal
vector.  All positive witnesses, combinatorial reductions, tier counts, and
portal switches are literal and independently replayed.
