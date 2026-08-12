# Bank-flexible edge-aligned cover-down: residual semigroup, density, and guarded one-chain induction

Date: 2026-07-31
Status: exact semigroup and leave equations, exact bank-flexible density
lemma, exact endpoint-state preservation and occurrence non-preservation for
the standard AGCF absorber, and a conditional one-chain recursion theorem.
A positive-density aligned-bank theorem is not proved.

## 0. Verdict

The arbitrary-common-basis Delcourt--Postle theorem and item `2300A` may be
used with the correct existential quantifiers:

\[
 \exists\text{ parent bank }E\quad
 \exists Q\in\mathcal Q(E)\quad
 \exists\text{ DP colour record}.                    \tag{0.1}
\]

No assertion for every `Q`, or for every parent AGCF, is needed.  Uniformity
of the `P-o(P)` theorem means that choosing the recursive bank and a
compatible favourable `Q` first costs no asymptotic side density.

The remaining exact condition is not another flux equation.  The **whole**
three-sector leave must lie in the nonnegative incidence semigroup generated
by complete residual complement-geodesic paths.  Intermediate sector leaves
need not lie in this semigroup.  They may carry signed debt; only the final
three-sector sum is required to be candidate-aligned.  The signed-newborn and
four-sector theorems then give an exact cumulative acceptance test for the
oriented terminal state.

There is a useful quantitative reduction.  If, among all compatible
bank--`Q` states and their padded DP colours, guard-safe semigroup-aligned
records have density `a_n`, then one such record has post-pruning deficiency
at most

\[
                         {\eta_n\over a_n}\,P.         \tag{0.2}
\]

This is bank-flexible: the winning bank may be exceptional.  It does not
prove `a_n>0`.

Two exact warnings remain load-bearing.

* A side-host DP leave of deficiency `delta` has `delta` lower and `delta`
  upper holes.  A union of `t` parameter-`n` AGCF candidates has `nt` holes
  on each outer shore.  Hence any **literal** palette bridge requires

  \[
                              n\mid\delta.             \tag{0.3}
  \]

  Flux/lattice validity does not imply this congruence, much less labelled
  semigroup membership.
* The standard identity `A+B=C+D` preserves the oriented endpoint bank when
  `C` is oriented as `A` and `D` as `B`.  It therefore preserves the terminal
  part of signed flux on every fixed middle subset.  It can nevertheless
  change the direct occurrence graphs, the half-slack `h`, and the
  four-sector `sigma/omega` rows.  SBE preservation requires either literal
  occurrence transparency or a fresh cumulative-reserve audit after the
  completed packet bank and at any state exported recursively.

Local Boolean common cap is automatic after exact outer saturation, slot
feasibility, and physical acyclicity.  A downstream word-compiler guard is
not: it must be protected or have zero packet displacement.

## 1. The complete residual-path semigroup

Fix a parameter-`n` parent AGCF, choose an orientation transversal `E`, and
form the three-sector residual catalogue `R_n(E)` in the recursion from
parameter `n` to `n+1`.  A residual candidate `r` is a complement geodesic
with tag trace

\[
                 00\cdots00,\quad01\cdots01,\quad11\cdots11. \tag{1.1}
\]

Let `V_n(E)` be the union of all remaining middle, lower-turn, and upper-turn
resources, and let

\[
 A=A_n(E)\in\{0,1\}^{V_n(E)\times R_n(E)}              \tag{1.2}
\]

be the literal resource-incidence matrix.  Define the candidate residual
semigroup

\[
 \mathsf S_n(E)=\{Ax:x\in\mathbb Z_{\ge0}^{R_n(E)}\}. \tag{1.3}
\]

### Theorem 1.1 (binary-semigroup equivalence)

For a binary resource vector `ell`,

\[
             \ell\in\mathsf S_n(E)                   \tag{1.4}
\]

if and only if `ell` is the disjoint resource union of a family of complete
residual candidates.

#### Proof

One implication is immediate.  Conversely suppose `Ax=ell` with
`x>=0` integral and `ell` binary.  Every candidate column is nonzero, so
`x_r>=2` would make every resource of `r` have load at least two.  Thus
`x_r` is zero or one.  If two selected columns shared a resource, that row
of `Ax` would again have load at least two.  Hence the selected candidates
are resource-disjoint. \(\square\)

Thus no separate matching constraint is hidden in (1.4).  Binary membership
in the positive semigroup is already the exact matching condition.  It is a
stronger requirement than membership in the affine integer lattice and may
not be replaced by the latter; the parameter-three AGCF hole gives an exact
failure of that inference in the full candidate host.

## 2. Exact leave equations and the saturated numerical projection

A residual candidate at this step has `n+2` middle resources, `n+1` lower
turns, and `n+1` upper turns.  Its three internal tag-block lengths form a
weak composition

\[
                         (a,b,c),\qquad a+b+c=n-1.     \tag{2.1}
\]

It also has exactly one seam of each of the two tag-change types.

### Proposition 2.1 (necessary equations for an aligned leave)

If `ell=Ax` and `t=sum_r x_r`, then

\[
 |\ell_M|=(n+2)t,\qquad |\ell_L|=|\ell_U|=(n+1)t,   \tag{2.2}
\]

and, for every coordinate `u` of the child ground set,

\[
             m_u(\ell)=u_u(\ell)=\ell_u(\ell)+t.     \tag{2.3}
\]

If `d_0,d_1,d_2` count the internal leave edges in the three tag sectors and
`s_1,s_2` count the two seam types, then

\[
       s_1=s_2=t,\qquad d_0+d_1+d_2=(n-1)t.         \tag{2.4}
\]

Writing

\[
 h_{abc}=\sum_{r:\operatorname{type}(r)=(a,b,c)}x_r, \tag{2.5}
\]

the more precise equations are

\[
 \sum h_{abc}=t,\qquad
 (d_0,d_1,d_2)=\sum h_{abc}(a,b,c).                   \tag{2.6}
\]

#### Proof

Equations (2.2) and (2.4) count the resources of each selected residual
path.  Equation (2.3) is the pathwise AGCF coordinate-flux identity at child
parameter `n+1`, summed over the `t` selected paths.  Equation (2.6) is the
definition of the type histogram. \(\square\)

The numerical type condition contains no further holes.

### Proposition 2.2 (saturation of the unrestricted type semigroup)

The semigroup generated by

\[
       \{(1,a,b,c):a,b,c\ge0,\ a+b+c=n-1\}           \tag{2.7}
\]

is exactly

\[
 \{(t,d_0,d_1,d_2)\in\mathbb Z_{\ge0}^4:
                  d_0+d_1+d_2=(n-1)t\}.              \tag{2.8}
\]

#### Proof

Necessity follows by summing the generators.  Conversely, take a word with
`d_0` symbols `0`, `d_1` symbols `1`, and `d_2` symbols `2`.  Its length is
`(n-1)t`.  Split it into `t` consecutive blocks of length `n-1`; the symbol
counts of each block are one generator in (2.7), and their sum is the given
quadruple. \(\square\)

This is only the **unrestricted numerical projection**.  A fixed endpoint
bank `E` may not contain labelled candidates of all types, and even the
correct type histogram need not satisfy the resource equations `Ax=ell`.
The remaining obstruction is labelled correlation, not a scalar Catalan
quota.

### Corollary 2.3 (literal DP-to-AGCF divisibility gate)

Choose and protect a slot set `S_0` whose **cardinality** is the forced
affine baseline, and work in the normalized capacity-slot host with those
slots deleted.  The location of `S_0` is a bank choice, not a universal
consequence of the count.  A side matching with deficiency `delta` then has
leave signature

\[
                         (\delta,\delta,2\delta).      \tag{2.9}
\]

If its two outer leaves are literally the lower and upper resources of a
union of `t` parameter-`n` AGCF candidates, then

\[
                         \delta=nt.                  \tag{2.10}
\]

In particular `n|delta` is necessary.  After cycle pruning the same statement
holds with `delta` replaced by `delta+z`.  For a literal whole-path leave in
the `n -> n+1` residual catalogue, the corresponding total outer count is
instead `(n+1)t`, as in (2.2).

This is a necessary outer-palette test only.  The AGCF and capacity-slot
hosts are different incidence systems; divisibility does not construct the
missing bridge.

## 3. Bank-flexible density extraction

Fix a cycle cutoff `L`, and put

\[
 D=2(n+1)(n+2),\qquad s=\lceil D^{1-\alpha}\rceil,\qquad
 K_D=D+s,\qquad
 \rho_n={s+16n+16+4/n\over D+s}.                     \tag{3.1}
\]

Let `\mathcal B_n` be any nonempty finite family of recursive bank states.
A state includes
an endpoint/orientation bank `E`, a compatible admissible common basis `Q`,
and any already fixed protected reserve.  Let `Z_b` be its forbidden host
resources and `R_b` its additionally forbidden atoms.  Colour the reduced
host and **pad to exactly `K_D` colours**, retaining empty colour classes.
For every padded colour fix one legal one-edge-per-cycle pruning, and let

\[
                  \widehat\delta_{b,i}=P-|F_{b,i}|.   \tag{3.2}
\]

Put

\[
 z_n=\max_b|Z_b|,\qquad r_n=\max_b|R_b|
\]

and

\[
 \eta_n=\rho_n+{Dz_n+r_n\over K_D P}+{1\over L+1}.  \tag{3.3}
\]

The whole-colouring ledger, protected-reserve deletion bound, and cycle
pruning give, uniformly for every bank state,

\[
 {1\over K_D}\sum_{i=1}^{K_D}\widehat\delta_{b,i}
       \le \eta_nP.                                  \tag{3.4}
\]

Indeed, deleting `Z_b,R_b` removes at most `D|Z_b|+|R_b|` host atoms.
The item-`2300A` padded deficiency numerator is at most

\[
 (s+16n+16+4/n)P+D|Z_b|+|R_b|,
\]

and pruning loses at most `P/(L+1)` atoms in each padded class.  Thus a
protected `o(P)` reserve, including the affine slot baseline, contributes
only `o(P)` to the selected-class loss.

Call a pair `(b,i)` **aligned** when its chosen forest, together with its
preloaded off-state packets, has a binary full three-sector leave in
`S_n(E_b)` and passes all declared slot, graphic, terminal-reserve, and
protected-guard rows.  Let

\[
 a_n={|\mathcal A_n|\over|\mathcal B_n|K_D}.          \tag{3.5}
\]

### Theorem 3.1 (bank-flexible aligned-density lemma)

If `a_n>0`, some aligned pair satisfies

\[
             \widehat\delta_{b,i}\le {\eta_n\over a_n}P. \tag{3.6}
\]

For `r` fixed side rows selected simultaneously, if aligned bank--colour
tuples have density `a_n` in the corresponding product palette, then some
aligned tuple has total deficiency at most

\[
                         {r\eta_n\over a_n}P.         \tag{3.7}
\]

#### Proof

Multiply (3.4) by `K_D` and sum over all bank states.  The sum of the
nonnegative deficiencies on
the aligned subset is at most the total sum, so its minimum is at most the
total divided by `|A_n|`, proving (3.6).  For (3.7), choose the `r` colours
independently and sum their deficiencies.  The average is at most
`r eta_n P`; condition on the aligned subset exactly as before. \(\square\)

The theorem needs positive density, not alignment for every bank.  In
particular a family containing bad fixed common bases is harmless if a
positive fraction of the joint bank--`Q` states are favourable.  Conversely,
the crown obstruction in item `2300A` proves that (3.4), exact one-resource
incidences, flux, and ubiquitous balanced rectangles alone do not imply
`a_n>0`.

In the asymptotic regime, if `z_n=o(P)`, `r_n=o(K_D P)`, `L` tends
slowly to infinity, and

\[
                         a_n\gg\eta_n,               \tag{3.8}
\]

then the selected aligned record has deficiency `o(P)`.  This is exactly
the scale at which a protected packet bank may coexist with the arbitrary-
`Q` Delcourt--Postle bulk.

If a protected absorber bank can finish every aligned record of deficiency
at most `b_n`, the exact quantitative payoff is

\[
                         {\eta_n\over a_n}P\le b_n.   \tag{3.9}
\]

The structured AGCF absorber packing bounds may be substituted for `b_n`
only after a legal fixed-`Q` packet realization has been supplied.

## 4. Endpoint-preserving absorbers and the exact reserve scope

The standard AGCF absorber is

\[
                              A+B=C+D.                \tag{4.1}
\]

In the explicit six-coordinate identity, `A,C` have the same complementary
global endpoint pair and `B,D` have the same complementary global endpoint
pair.  The suspension to every `n>=3` retains this property.

### Proposition 4.1 (oriented endpoint-state preservation)

Orient `C` as `A` and `D` as `B`.  Then the two phases `A+B` and `C+D` have
the same unordered endpoint pairs and the same selected terminal at each
pair.  Consequently, for every fixed middle subset `W`, they have identical
endpoint incidence `delta_B(W)`, terminal count `t_B(W)`, and signed terminal
flux

\[
                         \phi_B(W)=2t_B(W)-\delta_B(W). \tag{4.2}
\]

#### Proof

The endpoint pairs agree path by path, and the prescribed orientations
choose the same member of each pair.  Each statistic in (4.2) depends only
on these oriented endpoint pairs. \(\square\)

This proposition is not an SBE-transparency theorem.  Although (4.1)
preserves the sets of middle, lower, and upper resources, it can re-pair a
turn colour with different middle occurrences.  Therefore it can change
the direct occurrence graphs and hence the neighborhood sets, `h(W)`, and
the sector terms `sigma_i,omega_e`.

Two proof-safe packet guards are available here.

1. **Occurrence transparency:** the packet preserves both direct occurrence
   bipartite graphs, the oriented endpoint bank, and the pointwise physical
   forest-degree profile.  Then every signed-flux and cumulative-reserve row
   is literally unchanged.
2. **Boundary re-audit:** after the simultaneous cover-down packet (and at
   any deliberately exported recursive macro-boundary), recompute the
   occurrence graphs and require, on both shores, every sector-prefix
   reserve

   \[
       \rho_0,\rho_1,\rho_2,\rho_3\ge0                \tag{4.3}
   \]

   along the upper path `0-2-3-1` and lower path `1-0-2-3`.

The terminal terms in this re-audit are already controlled by Proposition
4.1, but the occurrence/overlap terms are not.  The internal trades of a
simultaneous packet need not be valid recursive states, and no individual
edge or individual candidate is required to pay an overlap charge.

## 5. Common-cap guard and host separation

The AGCF resource hypergraph and the fixed-`Q` capacity-slot hypergraph are
different hosts.  A packet used in the following theorem must therefore
carry an explicit realization in the normalized side host

\[
                         \widehat G_Q=G_Q-S_0.        \tag{5.1}
\]

For the simultaneous packet bank, and for any macro-prefix deliberately
exported as a recursive state, require:

1. the selected side atoms have the stated lower and upper loads;
2. their occurrence slots respect ordinary cap two and every cap-one seam
   anchor; and
3. after contracting the retained central-plus-side forest, the new physical
   ears are loopless and graphic-independent.

At the completed bank, exact outer saturation plus these slot and graphic rows
imply the local Boolean common cap automatically: the selected atom at
`D subset V` already specifies the two opposite intermediate corners with
intersection `D` and union `V`.  No pointwise cap map need be frozen.

If a protected bottom bank has a prescribed cap map, every nonparallel
outer alternating circuit must avoid it.  Freezing the entire pointwise map
is generally fatal because it freezes the unlabelled physical support.

The eventual word compiler uses a stronger same-cell/maximal-envelope cap.
It is not a vertex of `G_Q`.  Every packet must therefore either avoid its
protected trace bank or have exactly zero displacement in the separately
declared compiler state.  Local Boolean common-cap closure does not prove
this downstream row.

## 6. Conditional one-chain theorem

### Theorem 6.1 (bank-flexible guarded edge-aligned recursion)

Assume a valid parent state at parameter `n`.  Suppose one can choose:

1. an orientation bank `E` and a compatible admissible common basis `Q`
   whose fixed host passes every required capacity cut (in particular the
   exact fractional dummy-capacity obstruction is zero);
2. a slot baseline `S_0` and a closed-support-private off-state packet bank;
3. DP forest records in the punctured sector hosts outside that bank such
   that the **combined** binary residual leave is

   \[
                              \ell=A_n(E)x             \tag{6.1}
   \]

   for an integral nonnegative `x`;
4. for every selected column of `x`, a private,
   **residual-face-internal**, endpoint-preserving absorber and a legal
   fixed-`Q` side realization, with the completed packet choices satisfying
   the outer-load, slot, contracted-graphic, and final exact outer-saturation
   rows of Section 5;
5. either occurrence transparency, or the exact two-shore cumulative
   reserve audit (4.3), after the completed packet bank and at each state
   deliberately exported to the next recursive stage; and
6. the exact residual topology row: after the final switches every augmented
   directed cycle contains exactly one complementary endpoint-pair reset;
   and
7. zero displacement on every declared downstream compiler guard, or a
   separately proved regeneration of that guard.

Then the packet switches fill the residual leave exactly, produce the
parameter-`n+1` residual complement-geodesic factor, retain an accepted
oriented terminal bank, and give exact local Boolean common caps on the
realized side rows.  The resulting endpoint bank may be carried as the next
recursive state.

If such a transition exists from one chosen state at every parameter,
starting at an authenticated base, then induction gives one infinite
bank-flexible chain.  No extension theorem for every parent or every `Q` is
required.

#### Proof

By Theorem 1.1, (6.1) is a disjoint family of complete residual paths.
Private absorber switches cover precisely those resources, while the
off-state/resource identities leave every previously covered resource
covered once.  Face-internality preserves the prescribed tag trace, and
hypothesis 6 supplies the one-reset component correlation.  Therefore the
completed residual union consists of complement geodesics and its union
with the extended child paths is the next AGCF by the exact three-sector
recursion theorem.

Endpoint matching in Proposition 4.1 gives the declared oriented terminal
state.  Hypothesis 5, rather than endpoint matching alone, proves the
signed-flux/four-sector acceptance rows.  Hypothesis 4 proves physical slot
and graphic legality.  Exact outer saturation then invokes automatic
Boolean common-cap closure.  Hypothesis 7 supplies the logically separate
compiler row.  These arguments are preserved under iteration. \(\square\)

## 7. Exact remaining gate

The theorem localizes the missing all-parameter statement to a positive
selection problem:

> Along one recursively chosen family of endpoint banks, prove that
> guard-safe semigroup-aligned bank--`Q`--DP records have positive density
> `a_n` large enough for (3.9), or give a protected many-colour recolouring
> which moves one record into the semigroup without violating the cumulative
> reserve and graphic rows.

The following weaker data do not imply it:

* `P-o(P)` for every fixed `Q`;
* the complete DP deficiency and one-resource incidence ledgers;
* affine lattice/coordinate-flux validity;
* balanced `2<->2` trades;
* half-endpoint or four-sector reserve inequalities alone; or
* local Boolean common-cap feasibility.

The congruence (0.3), the parameter-three AGCF semigroup hole, and the odd
crown colouring are three independent reasons that marginal data cannot be
silently promoted to edge alignment.  The theorem is therefore conditional
but exact, and it uses precisely the bank-flexible quantifier permitted by
the known recursive endpoint classification.

## 8. Independent finite calibrations

The literal fixed-`Q`, parameter-three minus-side capacity-slot host has
`P=6`, `22` atoms, and a proper conflict-free colouring with class-size
multiset

\[
                             \{6,6,1^{10}\}.          \tag{8.1}
\]

Its deficiency multiset is therefore

\[
                             \{0,0,5^{10}\},          \tag{8.2}
\]

whose sum is `50=12P-22`.  Ten colour leaves fail the necessary
parameter-three congruence `3|delta`.  The two perfect classes show why this
is only a per-colour obstruction and not a refutation of bank-flexible
existence.

The separate literal AGCF catalogue gives the stronger positive-semigroup
obstruction.  A parameter-three near-cover leaves resource profile
`M/L/U=4/3/3`, satisfies every coordinate-flux row, and contains no complete
candidate.  Exhaustive replay finds no `1->2` repair, exactly six `2->3`
repairs, and four of those six preserve every old middle cap.  Thus even the
correct divisibility and flux rows do not replace labelled semigroup
membership; in this smallest fixture a nonzero-boundary radius-two packet is
both necessary and available.

The independent suspended-trade replay at parameters `3,...,8` verifies
endpoint-pair, middle-degree, and separate lower/upper palette preservation,
while the paired turns and both strict occurrence graphs change.  At
parameter `n`, the replay gives `2n-4` common paired turns and four removed
plus four added paired turns; the occurrence-labelled symmetric difference
on each shore is `8(n-1)` in every tested row.  Finite replay is used only to
authenticate the nontransparency warning; Proposition 4.1 is proved
directly and does not rely on extrapolation.

Artifacts:

```text
scratch/audit_h2_catalan_agcf_trade_occurrence_reserve_gate_20260731.py
  SHA 0c2a2e81726978389025a4a6f5e3eeab67d6051dbe59711e11d8db73a062bc45
scratch/h2_catalan_agcf_trade_occurrence_reserve_gate_20260731.audit.json
  SHA 2d4286e0382ab531f31a68be7aac9542662464911083a566be818833e8c8d81b
  payload 66a65611f3f04a956c2acb1dc097e0e94581a25df81c95a42e6cdbfdef295ec7
scratch/audit_catalan_dp_coloring_locked_c6_n3_20260731.py
  SHA fd8c1fe7f1a9ceb8a0f9cbcb8c7b42bfdf6cc42cd41945466e28d16a50b7707b
scratch/catalan_dp_coloring_locked_c6_n3_20260731.audit.json
  SHA 0100493c01c6642eab2abbb79eafa47b10e083ca0de59d9bff89b5bfb7d40a75
  payload f7b524358355207a201626841c677bf5eecc07b28b029b4012d6f629688a771a
scratch/audit_h2_catalan_bank_flexible_semigroup_20260731.py
  SHA 816c919909180d6ac2c3d143aef1d9b7cd21614b9d970fed25ff51b76e08ce5a
scratch/h2_catalan_bank_flexible_semigroup_20260731.audit.json
  SHA d83a02aacb3f996dc1b33b0abb2e0df493bef569d07204340f6892a840e139f9
  payload 6d94c07474e3f534b696b65b08d4222acac592f8622069b2271433d11fb5ade9
```

Authoritative inputs used here, authenticated at freeze time, are:

```text
MATH_THEOREM_CATALAN_ARBITRARY_COMMON_BASIS_PHYSICAL_FOREST_20260731.md
  SHA 19df1c335b08d01057b1a8ab67a569a2c2a5224083da04f358ed5642ddd4d43c
THREAD_A_CATALAN_FULL_DP_COLORING_LEAVE_LATTICE_AND_COVERDOWN_GATE_20260731.md
  SHA 05076aad999e486383c1df63c04ef3676d2b946d7464235c81d92557b70e0176
MATH_THEOREM_H2_CATALAN_DERF_ABSORBING_NEWBORN_FLUX_AND_SECTOR_RESERVE_20260731.md
  SHA 5faa1e1bfa40b23205ea1fe87d70f4b5d23236543de5c6a39bc5b4ffa3c45a37
MATH_THEOREM_AD_AGCF_DP_PROTECTED_RESERVE_AND_NONZERO_BOUNDARY_COVERDOWN_20260731.md
  SHA 7b7cdc853a6956f9923fa60af344a184f0aa544fc9d0345aae867a5ae92d2eb0
MATH_THEOREM_CATALAN_THREE_SECTOR_FIXED4_ATOMS_AND_COVERDOWN_GATE_20260731.md
  SHA dc77e030bc1b8f2fb5f4f64cc59d7582b8c270b62996ba6491be7ffedea41df0
MATH_THEOREM_CATALAN_FULL_COLOUR_COVERDOWN_COMMON_CAP_GATE_20260731.md
  SHA e8ab994c0a5ef631f99abeb433e0362c4752e0d5bb50b142be70ba0aa17b07d0
```
