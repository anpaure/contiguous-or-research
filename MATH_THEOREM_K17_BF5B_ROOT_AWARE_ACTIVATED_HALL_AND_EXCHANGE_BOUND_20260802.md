# K17 `bf5b` root-aware activated Hall cuts and the exchange-distance boundary

**Date:** 2026-08-02  
**Status:** exact Boolean/Hall theorem and read-only audit of the fixed-root
deficiency-40 certificate.  No solver or proof checker was launched.  The
fixed 5,228-mode result is a supplier-projection optimum on the individually
common-declared-state screened face.  It is not a simultaneous two-phase
occurrence packing, chronology, residence, upper, compiler, or word theorem.

**Authoritative consumer rebase, 2026-08-03.**  The general Boolean/Hall
theorems below remain valid, but every numerical parent, prospective mode ID,
and parent-local cut before Section 10.5 is historical calibration.  Forward
consumer work must use compressed parent `e878bf19654d...`, final parent
`fa49188250bf...`, and the canonical catalogue frozen under
`/home/amodo/or15/work/k17_drop12_canonical_consumer_catalogue_20260803`.
In particular, every `dd608ae5...` prospective ID is stale.

## 1. Frozen frontier and exact scope

The compressed parent is

```text
bf5b946f9e1cd5165ba323c894208e9370e7a2b671578ef2a6231535c2ba3241
```

with zero LLR overlays.  The freshly generated structural catalogue has
115,086 modes.  Its one-transfer two-phase screens contain

```text
marginal positive in both phases             5,821 modes
one declared (q,alpha,beta) state in common  5,228 modes
endpoint-row-disjoint rank                     208
```

The 5,228-row face is SHA-bound below.  `common declared state` means that
the two phase menus contain the same `(q,alpha,beta)` label; predecessor and
successor physical rows may differ.  Every mode was priced with its donor
removed, its LLR host created, and all 7,213 protected rows excluded.  This is
an exact one-transfer screen, not a proof that several selected witnesses
coexist.

On the fixed literal `bf5b` presentation, the exact mode-only supplier
optimum on this face is

\[
                 16858/16898,\qquad \delta=40.             \tag{1.1}
\]

A ten-mode table attains (1.1).  Target deficiency 39 is represented by a
17,361-variable, 31,591-clause CNF with a stored DRAT proof and an explicit
`s VERIFIED` transcript.  The proof contains no root, common-basis, or
representing-matching variables.

The attaining global fresh-catalogue edge indices are

```text
29162 47595 58729 77643 81966
82676 112912 113721 114811 114957
```

## 2. Exact outer/root state atoms

Expose the outer completion instead of treating it as hidden recourse.  Let

\[
 x_{mr}=1 \quad(m\to r),\qquad
 y_{lv}=1 \quad(l\to v),\quad v\in M\mathbin{\dot\cup}R,       \tag{2.1}
\]

with the exact compressed-normal matching/common-basis equations.  Put

\[
 d_m \longleftrightarrow \neg\bigvee_l y_{lm}.                \tag{2.2}
\]

Before LLR modes, the row rooted at `r` has the exact state atoms

\[
\begin{aligned}
 B_{r;(l,m,r)} &\longleftrightarrow y_{lm}\wedge x_{mr},\\
 B_{r;(m,r)}   &\longleftrightarrow d_m\wedge x_{mr},\\
 B_{r;(l,r)}   &\longleftrightarrow y_{lr}.                    \tag{2.3}
\end{aligned}
\]

The outer equations make the applicable row states one-hot.  If the root
grammar has additional actions `rho`, replace (2.3) by the complete signed
DNF

\[
 B_{i\sigma}
 \longleftrightarrow
 \bigvee_{c\in\mathcal R(i,\sigma)}
 \left(
   \bigwedge_{a\in F_c^+}a
   \wedge
   \bigwedge_{a\in F_c^-}\neg a
 \right),                                                    \tag{2.4}
\]

where the primary atoms include every relevant `x`, `y`, and `rho` literal.
Both directions of every AND and OR are required.  A positive-only footprint
is exact only if the outer matching equations prove that all omitted choices
are false.

## 3. Root-aware mode DNFs and final row states

Let a prospective mode `e` transform an LMR donor `(l,m,r)` and an LR host
`(u,q)`.  A branch `c` contains its complete paired phase state, flags,
occurrence resources, and root prerequisites.  Define

\[
 G_{e,c}
 \longleftrightarrow
 z_e\wedge B_{r;(l,m,r)}\wedge B_{q;(u,q)}\wedge C_{e,c},
 \qquad
 G_e\longleftrightarrow\bigvee_cG_{e,c},
 \qquad z_e\longleftrightarrow G_e.                         \tag{3.1}
\]

`C_(e,c)` is a complete signed conjunction.  It may be `1` only for a pure
union-projection calculation.  In a selected common state it must include
the actual paired phase-ticket/flag/resource atoms.  Equivalently introduce
ticket variables `lambda_(e,c)` and require

\[
 \sum_c\lambda_{e,c}=z_e,qquad
 \lambda_{e,c}\Longrightarrow
 B_{r;(l,m,r)}\wedge B_{q;(u,q)}\wedge C_{e,c}.              \tag{3.2}
\]

Row-disjointness is

\[
                         \sum_{e\ni i}z_e\le1.               \tag{3.3}
\]

The final states are exact DNFs.  On the LLR grammar they include

\[
\begin{aligned}
 S_{r;(l,m,r)}
 &\longleftrightarrow
 B_{r;(l,m,r)}\wedge\neg\bigvee_{e:\,D(e)=(l,m,r)}G_e,\\
 S_{q;(u,q)}
 &\longleftrightarrow
 B_{q;(u,q)}\wedge\neg\bigvee_{e:\,H(e)=(u,q)}G_e,\\
 S_{r;(m,r)}
 &\longleftrightarrow
 B_{r;(m,r)}\vee\bigvee_{e:\,D(e)=(l,m,r)}G_e,\\
 S_{q;(l,u,q)}
 &\longleftrightarrow
 \bigvee_{e:\,D_{\rm low}(e)=l,\ H(e)=(u,q)}G_e.            \tag{3.4}
\end{aligned}
\]

Alternative branches producing the same literal row state are ORed.  The
general definition is

\[
 S_{i\sigma}
 \longleftrightarrow
 \bigvee_{c\in\mathcal C(i,\sigma)}
 \bigwedge_{a\in A_c}a,qquad
                         \sum_\sigma S_{i\sigma}=1.           \tag{3.5}
\]

The fixed 5,228 catalogue is not a variable-root catalogue.  Once `x`, `y`,
or `rho` varies, (3.1)--(3.5) must use a complete state-expanded catalogue or
fresh parent-local regeneration.  Old mode availability bits cannot simply
be transported.

## 4. Head requirements and supplier-row changes

For a final row state `tau`, let `Hard(tau)` be the literal hard-head
predicate: here the row has length three and its lower target is not a
singleton.  Let `req(tau)` be its complete four-permutation head requirement.
Define

\[
 D_{h\tau}=S_{h\tau}\,Hard(\tau),\qquad
 a_h=\bigvee_\tau D_{h\tau},\qquad
 R_{h\eta}=\bigvee_{\tau:\,req(\tau)=\eta}D_{h\tau}.          \tag{4.1}
\]

Thus a root move can retire a hard head by setting `a_h=0`, or change its
requirement by moving the true `R_(h,eta)` atom.

For supplier row `u` and a complete flag/menu label `phi`, put

\[
 M_{u\phi}
 =\bigvee_{\sigma:\,\phi\in Flags(\sigma)}S_{u\sigma}.        \tag{4.2}
\]

Equation (4.2) is correct for the complete union `6/9/4` projection.  If a
selected common state fixes one flag, use the exact
`S_(u,sigma) AND chosen_flag` guard instead.  Let
`kappa(phi,eta)` be the literal compatibility predicate.  For `u != h`,

\[
 C_{u\phi,h\eta}
 \longleftrightarrow M_{u\phi}\wedge R_{h\eta}
 \quad\text{when }\kappa(\phi,\eta)=1.                       \tag{4.3}
\]

For a fixed set `X` of physical potential-head rows, the neighbor bit is

\[
 n_u^X
 \longleftrightarrow
 \bigvee_{\substack{h\in X,\phi,\eta\\
                     u\ne h,\ \kappa(\phi,\eta)=1}}
 C_{u\phi,h\eta}.                                            \tag{4.4}
\]

The OR in (4.4) is by supplier identity.  Multiple flags, requirements, or
head incidences at row `u` still pay only one Hall unit.

## 5. Activated Hall/Benders theorem

### Theorem 5.1

At every integral assignment satisfying the exact state definitions,

\[
 \delta
 =K-\nu(G)
 =\max_{X}
 \left(\sum_{h\in X}a_h-\sum_u n_u^X\right),
 \qquad K=\sum_h a_h.                                       \tag{5.1}
\]

Consequently target deficiency at most `Delta` is exactly the family

\[
 \boxed{
 \sum_{h\in X}a_h-\sum_u n_u^X\le\Delta
 }
 \qquad(X\subseteq\widehat H).                              \tag{5.2}
\]

Equivalently, in the inactive-head cardinality form used by the fixed driver,

\[
 \boxed{
 \sum_{h\in X}(1-a_h)+\sum_u n_u^X\ge |X|-\Delta.
 }                                                           \tag{5.3}
\]

An exact matching-rank epigraph is

\[
 \boxed{
 \Theta\le K-\sum_{h\in X}a_h+\sum_u n_u^X.
 }                                                           \tag{5.4}
\]

#### Proof

Fix an integral outer/mode/ticket assignment.  Equations (2.3)--(4.4)
evaluate to its literal final supplier graph.  For active heads in `X`,
`sum_u n_u^X` is exactly the number of distinct neighbors.  Hall's deficiency
form gives (5.1); rearrangement gives (5.2)--(5.4).  Because every Boolean is
an exact function of `x,y,rho,z,lambda`, the inequalities remain valid after
root and common-basis changes.  QED.

This gives an exact Benders scheme: materialize an integral master state,
compute one maximum supplier matching and its alternating Hall shore `X`,
then add (5.2) with all root-aware DNFs exposed.  One failed arbitrary root
completion is not a no-good for a transfer set while root completion remains
unresolved recourse.

## 6. Terminal fixed-face obstruction

The terminal target-39 shore has 50 potential heads.  On the fixed `bf5b`
5,228-mode face its activated cut reduces exactly to

\[
\begin{aligned}
 3+I_{14797}
 &+N_{2793}+N_{5895}+N_{6540}\\
 &+N_{6560}+N_{12586}+N_{14851}
 \ \ge\ 50-d,                                               \tag{6.1}
\end{aligned}
\]

where

\[
\begin{aligned}
 I_{14797}&=\neg z_{52448},\\
 N_{2793}&=B_{2793},\\
 N_{5895}&=\bigvee z_{\{6027,6067,6145,6221,6729,14431,27300,58729\}},\\
 N_{6540}&=\bigvee z_{\{15229,16138,17781,21688,29162\}},\\
 N_{6560}&=B_{6560}\vee z_{15001}\vee z_{15032},\\
 N_{12586}&=B_{12586},\\
 N_{14851}&=B_{14851}.                                      \tag{6.2}
\end{aligned}
\]

Here `B_u` denotes the fixed-face base-state atom for row `u`.  The three
constant supplier credits are `12973 -> 12948`, `13581 -> 13561`, and
`20737 -> 7736`.  The subscripts on `z` in (6.2) are global fresh-catalogue
edge indices.
There are only seven dynamic Boolean terms, so the left side of (6.1) is at
most `3+7=10`.  Target `d=39` requires eleven.  The generated CNF therefore
contains complementary units on variable `17361`; its DRAT proof is the
empty-clause derivation.  Target `d=40` requires ten and the ten-mode witness
attains it.

For variable roots the exact lift of this same physical-row template is not
(6.1).  It is

\[
 \boxed{
 \Gamma_P(\xi)
 :=\sum_{p\in P}(1-a_p(\xi))
   +\sum_{u=0}^{24309}n_u^P(\xi)
 \ge50-d,
 }                                                           \tag{6.3}
\]

using all supplier identities and the complete state DNFs of Sections 2--4.
Previously absent identities may become neighbors and old constant neighbors
may disappear.

## 7. What is actually required to escape deficiency 40

The fixed face has exact maximum `Gamma_P=10`.  Hence every root-variable
state reaching deficiency at most `d <= 39` must satisfy

\[
 \boxed{\Gamma_P(\xi)-10\ge40-d.}                            \tag{7.1}
\]

Therefore:

* beating deficiency 40 requires at least **one net new `P`-shore Hall
  credit**;
* supplier perfection requires at least **40 net new credits**.

A credit is either retirement of one active `P` head or activation of one
new distinct supplier identity into `P`; losing an old credit is charged
negatively.  Forty credits are not forty root exchanges.

Define literal presentation distance from the fixed completion by

\[
 d_{\rm pres}(\xi,\xi_0)
 =\sum_{a:\xi_0(a)=1}(1-\xi(a))
  +\sum_{a:\xi_0(a)=0}\xi(a),                               \tag{7.2}
\]

over the exposed root/common-basis representation literals.  Within the same
5,228-mode grammar, (7.1) proves

\[
                d_{\rm pres}(\xi,\xi_0)\ge1                 \tag{7.3}
\]

for every `d <= 39` escape: the identical literal presentation is exactly
the DRAT-closed face.  If differences of representing matchings are counted
as alternating-component exchanges, at least one nontrivial component must
change.  Under a root-retirement-only augmentation, at least one exchange
incident with `P` or its supplier-state DNFs is necessary, not sufficient.

Now let `B_0` be a receiver/common basis and use element distance

\[
                  d_B(B,B_0)=|B_0\setminus B|.               \tag{7.4}
\]

The present artifacts serialize neither `B_0` nor its representing matchings
`mu_7,mu_L`.  Another representation of the same basis can change many row
states while `d_B=0`.  Consequently the strongest unconditional bound on
ordinary common-basis **element** exchanges is only

\[
                         \boxed{d_B\ge0.}                    \tag{7.5}
\]

If the literal `bf5b` representation is proved unique at `B_0`, or a
radius-zero joint representation model is DRAT-UNSAT, (7.3) upgrades to one
basis exchange, equivalently \(\lvert B\mathbin{\triangle}B_0\rvert\ge2\).
Neither certificate is present.

More generally, if an independent audit proves that one basis exchange adds
at most `lambda > 0` net credits to (7.1), then

\[
 d_B\ge
 \left\lceil\frac{40-d}{\lambda}\right\rceil
 \quad(d\le39),
 \qquad
 d_B\ge\left\lceil\frac{40}{\lambda}\right\rceil
 \quad(d=0).                                                 \tag{7.6}
\]

No such `lambda` bound is presently certified.  Marginal one-exchange tests
are insufficient because alternating representations and mode DNFs can have
compound activation.

## 8. Guarded reuse when the root-state catalogue is incomplete

A Hall shore from one root completion is not automatically a cut on its
whole root fibre.  Either expose a complete state-expanded DNF model as
above, or let `gamma` be an exact branch literal under which every state of
the shore heads and every supplier state capable of entering the shore has
been completely enumerated.  Then the safe guarded cut is

\[
 \gamma\Longrightarrow
 \left(\sum_{h\in X}a_h-\sum_u n_u^X\le\Delta\right),        \tag{8.1}
\]

or

\[
 \sum_{h\in X}(1-a_h)+\sum_u n_u^X
 +( |X|-\Delta)(1-\gamma)
 \ge |X|-\Delta.                                            \tag{8.2}
\]

Unioning neighbors from incompatible outer completions is not an exact
lift.  With unpriced states, use explicitly optimistic unknown-neighbor bits
or leave the branch `UNKNOWN`; silently omitting possible neighbors would
make the cut invalid.

## 9. Proof boundary

The fixed optimum proves a lower bound of 40 for the screened supplier
relaxation.  It does not prove simultaneous two-phase occurrence feasibility
of the ten-mode witness.  The stored DRAT authenticates the generated CNF,
but no independent generator replay or unified manifest currently binds the
source, all cut-support semantics, CNF, proof, and witness.  There is also no
root/common-basis action catalogue or exchange-to-credit incidence ledger.

Accordingly, the strongest promoted conclusions are (5.2), the literal
fixed-face obstruction (6.1), the net-credit bound (7.1), literal
presentation distance at least one, and no positive common-basis element
distance without further certification.

## 10. Allowed-edge-gated singleton root columns

This section records the 2026-08-03 sharpening supplied by
`MATH_THEOREM_K17_SINGLETON_ROOT_ACTION_ALLOWED_EDGE_SCC_20260803.md`.
It separates three statements that the earlier free `rho` relaxation had
conflated: structural allowedness, retirement of the named frozen head, and
net gain in the activated Hall cut.

Fix a presentation face `F`: the parent, protected presentation edges,
selected transfer modes, and every occurrence edge imposed on this face are
all literal pins.  Delete pinned endpoints, expand the dummy bank into unit
copies, and let `M_F` be one perfect matching of the residual graph.  For a
candidate root `rho_i`, let `U_F(i)` say that the root and its action
endpoints are unpinned.  Its exact singleton-allowedness bit is

\[
 \chi_F(i)=U_F(i)\wedge
 \bigvee_{e=(\ell,\rho_i)\in E_{\rm low}^F(\rho_i)}
 \left(
   [e\in M_F]\vee
   [\operatorname{SCC}_F(\ell)=\operatorname{SCC}_F(\rho_i)]
 \right).                                                   \tag{10.1}
\]

The first disjunct in (10.1) is essential: a matched bridge is allowed even
when its endpoints do not share an SCC under the unmatched `A -> B`, matched
`B -> A` orientation.  For an unmatched edge, the SCC equality is equivalent
to an alternating cycle through that edge.  Thus `chi_F(i)=1` if and only if
the direct-low action has a perfect presentation completion on `F`.
An exact face-local master must at least impose

```text
rho_i <= chi_F(i).
```

If the low edge is itself a master choice, replace `rho_i` by edge-witness
columns whose sum is `rho_i` and force every column with a non-allowed edge
to zero.

Whenever `chi_F(i)=1`, every such direct-low completion turns the named
frozen LMR row into an LR row.  Hence it supplies one exact **gross**
inactive-head term,

\[
        \rho_i\Longrightarrow 1-a_{h_i}=1.                 \tag{10.2}
\]

It does not follow that the total shore value rises by one.  If `T_i` is a
complete materialized singleton child and `T_F` the parent table, then

\[
 \Gamma_P(T_i)-\Gamma_P(T_F)
 =1+\Delta_i^{\rm other\ heads}+\Delta_i^{\rm neighbors}.  \tag{10.3}
\]

The two correction terms in (10.3) must be obtained from the complete table:
an alternating completion can change other head states, lose an old supplier
identity, or add a new one.  SCC allowedness proves structural feasibility,
not a supplier edge and not a net Hall credit.

### 10.1 Exact calibration on the ten-mode structural face

Let `F_10^str` pin the `bf5b946f...` parent, all 7,213 protected rows, and
the ten fixed deficiency-40 LLR modes, but no phase-occurrence `BASE_LMR`
rows.  The parent shore has

\[
                         \Gamma_P(T_0)=10.                  \tag{10.4}
\]

Exact singleton completion data on this face gives

\[
 \chi_{F_{10}^{str}}(i)=1\quad(0\le i<27),                 \tag{10.5}
\]

and, for the exact materialized child attached to each action,

\[
 \Gamma_P(T_i)=
 \begin{cases}
  10,&h_i=6553,\\
  11,&h_i\ne6553.
 \end{cases}                                                \tag{10.6}
\]

Therefore 26 named child columns are exact net `+1` witnesses for the
target-39 shore, while the audited row-6553 child is structural but has zero
net gain.  In particular, at least one exact root credit is realizable on
`F_10^str`; the stronger exact count is 26 witnessed children.

For a disjunctive singleton master, let `b_i` select exactly the authenticated
child table `T_i`, not merely request the root action, and impose
`sum_i b_i <= 1`.  On the finite family consisting of `T_0` and these 27
children, (10.6) gives the exact value equation

\[
 \Gamma_P=10+\sum_{i:h_i\ne6553}b_i.                       \tag{10.7}
\]

Thus the target-39 shore cut on this disjunction is

\[
                 \boxed{\sum_{i:h_i\ne6553}b_i\ge1}.       \tag{10.8}
\]

Equation (10.8) is not valid with `b_i` replaced by a free root-level
Boolean whose low child and alternating completion remain unspecified.  A
failure of the one recorded row-6553 child also does not prove that every
possible row-6553 completion has value ten unless a constrained oracle has
maximized `Gamma_P` over that entire root branch.

In a larger master, let `gamma_10` be the exact guard for this finite
disjunction and add a baseline column `b_0`, with

```text
b_0 + sum_i b_i = gamma_10.
```

The globally safe guarded form is

\[
 \boxed{
 \sum_{i:h_i\ne6553}b_i+(1-\gamma_{10})\ge1.
 }                                                           \tag{10.9}
\]

This guard prevents a child coefficient from being reused after any parent,
mode, occurrence, low-edge, or alternating-completion literal leaves the
authenticated branch.

### 10.2 Phase-occurrence boundary

The common-valid face is a stricter face
`F_10^occ(omega_0,omega_1)` obtained by pinning one simultaneous physical
occurrence choice for every selected mode in both phases.  Those extra pins
can delete an allowed edge or split an alternating SCC.  Consequently neither
(10.5) nor the materializations in (10.6) transport automatically to the
occurrence-pinned face.  Individual common-declared-state menu support is not
a substitute for a simultaneous paired occurrence assignment.

This gap is now closed for two literal singleton branches.  The authenticated
face has ten phase tickets in each phase, twenty distinct long rows per phase,
seventeen rows shared across phases, and twenty-three `BASE_LMR` rows in the
union.  Action 0, at row 130 and root 1935, has an exact residual presentation
matching on this face and produces

\[
 \operatorname{SHA}(T_{\{0\}})
 =\mathtt{88f0a5fc4f2a98db59450e95b06e1a4123caaeaaba40ec80db92ec74fbdde79d},
 \qquad \delta(T_{\{0\}})=39.                              \tag{10.10}
\]

The supplier projection has 74,573 edges, rank 16,859 of 16,898, 32 zero
heads, and an alternating Hall shore of size `47/8`.  All 7,213 protected
rows, all twenty selected-mode endpoints, and all twenty-three occurrence
rows remain literal.  Independently, action 1 at row 146 and root 1995 gives

\[
 \operatorname{SHA}(T_{\{1\}})
 =\mathtt{9c02bd5450209f8652208905bf78176d24e8348c18f4e8b30b92e40b1c6ea9fb},
 \qquad \delta(T_{\{1\}})=39.                              \tag{10.11}
\]

Thus occurrence-pinned common validity is proved for these two singleton
children.  The fixed-root optimum 40 shows that zero named root actions do
not reach deficiency 39, while either child uses one.  If `r_39` counts named
direct-root actions together with their complete compensating presentation
rematching, then

\[
                         \boxed{r_{39}=1}.                  \tag{10.12}
\]

This is one authenticated root/common-basis **presentation exchange**.  It
does not mean one changed table row, one presentation-edge Hamming unit, or
one ordinary common-basis element replacement; for example the action-0
alternating completion changes four compressed rows.

### 10.3 Multi-action boundary

For a set `S` of requested direct-root actions, singleton SCC bits cannot be
added.  Form the one joint residual presentation instance by forbidding every
rank-seven-middle-to-root arc

\[
          m\longrightarrow\rho_i
          \qquad(i\in S,\ m\in M_{\rm out})                \tag{10.13}
\]

that survives the pins.  The set `S` is structurally legal exactly when this
joint graph has a perfect matching; then materialize that one matching and
evaluate the complete `Gamma_P`.  This joint oracle is necessary even when
all members of `S` pass (10.1) separately, because their allowed edges can
share a low endpoint or require incompatible alternating cycles.  No
multi-action Hall gain is certified by summing the 26 singleton values.

The noncomposition statement is a warning about inference, not a claim that
every particular set fails.  The full set

\[
                         S_{27}=\{0,1,\ldots,26\}
\]

has now been checked by one joint occurrence-pinned presentation oracle.  It
simultaneously forbids every surviving `M_out -> rho_i` arc for all 27 roots,
and its residual matching is exactly `29256/29256`.  All 27 requested roots
are direct-low in the same completion.  After the ten fixed LLR overlays, the
joint child is

\[
 \operatorname{SHA}(T_{27})
 =\mathtt{dd608ae5aa28c98fd8cfa26bc5bfe66916e2d12b77a89796a9ed11dde7aaaf97}.
                                                               \tag{10.14}
\]

Its exact supplier projection has 74,932 edges, rank 16,876 of 16,898,
deficiency 22, 21 zero heads, and an alternating Hall shore of size `23/1`.
This is a joint witness for this particular 27-set; it is not obtained by
adding singleton SCC or singleton-gain certificates and does not make
singleton allowedness compositional in general.

### 10.4 Historical target-21 calibration on `T_27` (superseded)

This subsection records the exact `dd608ae5...` calibration but is not an
authoritative consumer cut after the canonical rebase in Section 10.5.

The old 50-head shore `P_0` is not the next separator.  Evaluated on `T_27`,
it has 28 changed/inactive frozen heads and five old-shore supplier neighbors,
so its value is 33.  It already satisfies the target-21 right-hand side
`50-21=29`, even though the exact global deficiency is 22.  In particular,
the stored `all27.shore.*` files are an evaluation of the historical shore,
not the regenerated target-21 cut.

Regenerate from the exact supplier matching of `T_27`.  Its new alternating
head shore is

\[
\begin{split}
 P_{27}=\{&1154,1160,1490,3078,5831,5916,6301,6426,8827,11752,12310,\\
           &12691,12693,12816,14449,14785,15103,15484,16378,16506,\\
           &17140,18494,22839\},
\end{split}                                                   \tag{10.15}
\]

and its current distinct-neighbor set is `{14851}`.  Compile the head-state
and supplier-neighbor DNFs afresh against parent `T_27`.  The exact
parent-local target-21 Hall cut is

\[
 \boxed{
 \Gamma_{P_{27}}^{(27)}(\eta)
 =\sum_{h\in P_{27}}(1-a_h^{(27)}(\eta))
  +\sum_{u=0}^{24309}n_u^{P_{27},(27)}(\eta)
 \ge 23-21=2.
 }                                                            \tag{10.16}
\]

At `T_27`, all 23 shore heads are active and only row 14851 contributes a
neighbor, so the left side is one and (10.16) separates by exactly one.  In a
larger master it must be guarded by the complete `T_27` parent-local face,

\[
 \Gamma_{P_{27}}^{(27)}+2(1-\gamma_{27})\ge2.               \tag{10.17}
\]

The general Hall theorem (5.2)--(5.3) remains valid, and a fully lifted old
cut may remain in a cut pool.  But the old fixed-face literals, shore,
neighbor support, SCCs, and singleton gains cannot substitute for separation
on `T_27`.  Any further descent must regenerate those objects on the new
parent; merely changing the old right-hand side is unsound as a parent-local
oracle.

### 10.5 Authoritative canonical consumer rebase and target-20 cut

The canonical consumer parent is the occurrence-pinned 26-action child that
drops action 12 (row 12948) from the earlier 27-action set.  Its exact states
are

\[
\begin{aligned}
 \operatorname{SHA}(C_{\rm can})
   &=\mathtt{e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb},\\
 \operatorname{SHA}(T_{\rm can})
   &=\mathtt{fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c}.
\end{aligned}                                                  \tag{10.18}
\]

The augmented presentation matching is exact on the fixed ten-mode,
two-phase occurrence face: all 7,213 protected rows and all 23 coalesced
occurrence rows remain literal.  The complete `6/9/4` supplier replay has

```text
graph edges       74,935
hard heads        16,898
matching          16,877
deficiency            21
zero heads             19
Hall shore            23/2
semantic FNV64   f80fe0c9b65f2471
```

An independent replay is byte-identical.  Thus the next supplier target is
deficiency 20, not 21.

Let `Q_can` be the new parent Hall shore

\[
\begin{split}
 Q_{\rm can}=\{&1154,1160,1490,3078,5831,5916,6301,6426,8827,11752,\\
 &12310,12691,12693,12816,12948,13148,15103,15484,16378,16506,\\
 &17140,18494,22839\}.
\end{split}                                                    \tag{10.19}
\]

For a candidate table `T` materialized from this canonical parent, let
`A_h(T)=1` exactly when row `h` retains its frozen `fa491882...` head state,
and put `D_h(T)=1-A_h(T)`.  For each physical supplier row `u`, define one
distinct-identity bit

\[
 N_u^{Q_{\rm can}}(T)
 \longleftrightarrow
 \bigvee_{\substack{h\in Q_{\rm can}\\u\ne h}}
 \left(
   A_h(T)\wedge
   \operatorname{Compatible}_{6/9/4}
   (\operatorname{State}_T(u),\operatorname{Req}_{\rm can}(h))
 \right).                                                     \tag{10.20}
\]

The self-edge guard `u != h` and both directions of the Boolean equivalence
are required.  Multiple compatible flags or head incidences at the same
physical row still pay one Hall unit.  The exact canonical target-20 cut is

\[
 \boxed{
 \sum_{h\in Q_{\rm can}}D_h(T)
 +\sum_{u=0}^{24309}N_u^{Q_{\rm can}}(T)
 \ge |Q_{\rm can}|-20=3.
 }                                                            \tag{10.21}
\]

At `T_can`, every frozen head state is active and the distinct neighbor set
is exactly `{12973,14851}`.  Hence the current left side is two, and (10.21)
separates by exactly one.  Any target-20 child needs at least one **net** new
credit: a deactivated frozen head or a new distinct supplier identity, after
charging every lost current neighbor.  The two current neighbors are
calibration values, not a closed future-neighbor menu.  In a larger master,
(10.21) must be guarded by the complete canonical parent-local face or added
lazily after exact materialization.

### Canonical prospective catalogue

The only authoritative prospective IDs are in the new catalogue with SHA
`790fae940cd80c05e35656027dcb57139180b54c77f567c9b5333ab5d4581434`:

```text
fresh structural modes                              114,594
native phase-0 marginal-positive modes               15,659
native phase-0 declared-state witness records        17,351
transported phase-1 marginal-positive modes           17,779
transported phase-1 declared-state witness records    19,859
common declared-state modes / records             5,126 / 6,344
common declared-state modes pin-safe                   3,494
selected-witness strict tuple-equal modes              3,037
selected-witness strict tuple-equal modes pin-safe     2,813
```

`common declared state` is an exact intersection of `(q,alpha,beta)` keys;
the physical predecessor/successor rows remain phase-specific and their
literal union is coalesced.  The strict tuple-equal count filters the frozen
selected witnesses and is not an exhaustive search over alternative tuples
for the same state.

For a direct one-mode consumer, use the pin-safe common catalogue.  A
multi-mode consumer may use the full coalesced catalogue only while enforcing
endpoint and witness-row capacities jointly with the incumbent 23-row pin
union.  Phase prices and catalogue rows are one-mode marginal records; no
supplier gain follows by adding them.  Every new claim must bind both states
in (10.18), materialize all selected modes and occurrence witnesses
simultaneously, and replay the complete supplier projection.  Old `bf5` and
`dd608ae5...` IDs are lineage-only and must never be submitted as canonical
prospective IDs.

The authoritative H100 freeze has 50 manifest records and SHA
`b54013519c97e24ee35de8db0033afff9b407f7e6daf47cfdff89ddbe7420d93`.
Its human handoff SHA is `360b294e6d...` and its machine consumer-manifest
SHA is `95e6f5b38c...`.  These hashes, rather than an unfrozen path or an old
edge number, define the forward consumer contract.

### 10.6 Exact one-mode Hall filter and the mutual-support pair boundary

Let `C_pin` be the 3,494 pin-disjoint exact-common records on the canonical
parent, and let `C_ind` be the 3,483-record literal one-mode pool after the 11
incumbent-endpoint conflicts are removed.  For `e in C_pin`, let `F(e)`
contain its two endpoints and its
selected native-phase-0 and transported-phase-1 predecessor/successor rows.
The exact downstream audit gives

\[
 F(e)\cap\bigl(Q_{\rm can}\cup Z_{19}\bigr)=\varnothing
 \qquad(e\in C_{\rm pin}).                                  \tag{10.22}
\]

Consequently a literal one-mode overlay changes no current shore-head state:
`D_h(T_e)=0` for every `h in Q_can` and every `e in C_ind`.  Put

\[
 S_0=\{12973,14851\},\qquad
 G_e=\{u\notin S_0:N_u^{Q_{\rm can}}(T_e)=1\},\qquad
 L_e=\{u\in S_0:N_u^{Q_{\rm can}}(T_e)=0\}.
\]

Then the canonical cut has the exact gain--loss form

\[
 \Gamma_{Q_{\rm can}}(T_e)=2-|L_e|+|G_e|,
 \qquad
 \delta_{Q_{\rm can}}(T_e)=21+|L_e|-|G_e|,                 \tag{10.23}
\]

so every target-20 child necessarily satisfies

\[
 \boxed{|G_e|\ge 1+|L_e|.}                                 \tag{10.24}
\]

The literal shore geometry is especially small.  It is the disjoint union of
19 isolated zero heads and the two incidence paths

```text
13148 -- 12973 -- 12948
15103 -- 14851 -- 1490.
```

Here the middle vertices are physical supplier rows.  Thus an ordinary
record would have to create a third distinct physical supplier identity;
changing a flag or incidence at row 12973 or 14851 does not create a third
identity.  The unique record whose endpoint/witness footprint meets the
current neighbor set is edge 52847, with LR host 14851 and donor 1198.  It
destroys both shore incidences carried by row 14851, which is one lost
physical-identity credit, so its specialized Boolean filter is

\[
 \boxed{
   \sum_{u\notin\{12973,14851\}}N_u^{Q_{\rm can}}(T_e)
   \ge 1+\mathbf 1[e=52847].
 }                                                           \tag{10.25}
\]

The exact endpoint-incidence replay is stronger than this necessary bound:
none of the 3,483 incumbent-disjoint literal common modes creates any new
shore supplier.  Ordinary modes therefore have credit zero.  Edge 52847 has
`G_e=0` and `L_e=1`, hence credit minus one and is an exact singleton Hall
rejection.  Equations (10.23)--(10.25) are parent-shore filters, not
substitutes for the complete supplier matching.

Fresh edge 193, candidate 0 in the structural supplier screen, illustrates
the other term of (10.21).  It changes donor/head row 12948, so
`D_12948=1`, retains both old shore neighbors, and has exact matching
`16878/16898`, deficiency 20.  Its supplier positivity is therefore paid by
retiring a current shore head, not by the common-bank third-identity route.
Both canonical phase ledgers give edge 193 `exists=0`; it has no canonical
native/transported common occurrence state and is not a member of `C_pin`.
It is a structural projection calibration, not an occurrence-valid child.

The complete current one-mode supplier screen has 515 shore survivors and
468 exact rank-16,878 children.  For every one of those 468, exact
candidate-local pricing---including the newly created LLR host as an
available long witness---has

\[
 K_e^0\cap K_e^1=\varnothing,                               \tag{10.26}
\]

where `K_e^0` and `K_e^1` are the supported declared-state keys in native
phase 0 and transported phase 1.  This is the exact
`raw_common_state = 0` statement.  Since occurrence validity first requires
a common key, alternative predecessor/successor choices inside a key cannot
repair (10.26).  Hence none of the 468 known supplier-improving one-mode
children is occurrence-common on the literal canonical one-mode face, even
with new-host self-support.

This negative singleton fact must not be transported coordinatewise to a
pair.  A second mode changes another long row state and can create a common
state for a 468-source mode; the first mode can symmetrically create support
for the second.  Therefore the complete live pair domain must contain at
least one coordinate from the 468-source set and enumerate a second
structural mode/changed long state capable of such mutual support.  The exact
source/helper-pool join is

\[
 C_{\rm ind}\cap R_{468}=\varnothing.                       \tag{10.27}
\]

The exact resource-disjoint common/common pair census is

```text
credit  0       5,219,031
credit -1           2,287
positive credit         0
total            5,221,318.
```

The minus-one pairs are precisely the compatible common/common pairs in
which edge 52847 removes row 14851; no pair changes a shore head or creates a
new shore supplier.  Every common/common pair therefore violates (10.21).
The face `C_ind x C_ind` is exactly dead for target 20 and may be frozen, not
searched.  It would also exclude every presently known supplier-improving
source and is not a complete two-mode target-20 domain.

Row capacity is not the immediate obstruction: each of the 468 sources has
3,477--3,483 row-safe helpers in `C_ind` (2,802--2,807 in the strict
two-row subface), giving 1,629,622 total ordered source/helper seeds.  These
are resource-safe seeds only.  The unresolved exact incidence is the directed
changed-long-state rescue relation: after both donors are removed and both
new LLR hosts are installed, does the helper create a native/transported
common key for the source, and does the source/helper pair simultaneously
supply a capacity- and flag-consistent ticket for the helper?

For a proposed pair `(e,f)`, both modes must first be materialized together.
Only on that joint child may one build the complete phase menus
`W_e^i(k;T_{e,f})` and `W_f^i(k;T_{e,f})`, choose one common key per mode,
pack both phase-specific witnesses together with all incumbent tickets, and
enforce cross-phase flag consistency.  The same joint child must then receive
a complete self-excluding supplier replay.  Frozen singleton occurrence bits
and singleton supplier gains are not additive certificates.  The exact
5,221,318-row common/common no-go may be reused only on this SHA-bound
canonical face; it does not reject a source/helper pair because the source's
new long state is outside the individually-common face.
