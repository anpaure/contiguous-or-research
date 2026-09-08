# R2 theorem: K17 residence-1994 neutral-bridge/state-relative-quench oracle

**Date:** 2026-08-02  
**Status:** exact sufficient one-step and uniform-regeneration criteria, with
a fail-closed finite state/Benders interface.  A separately generated and
independently replayed two-primitive instance reaches residence 1993 on the
same hard face.  It is not resident and carries no source, compiler, or word
claim.

## 1. Frozen root and hard face

Let `F_*` be the independently replayed factor

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_fullq1_escape_res1994/model
SHA-256 127f97f02d238215367a1d5291853e0dd7ecb6d2d227cfcfed1c365e68d5ebcd
```

Both topology-derived openings have literal residence 1994 and opened
rank-ten holes zero.  The ordinary non-`D` provider palette is
`19,412/19,412`; all 16,261 guards, the protected normalized boundary, exact
incidence degrees, and one augmented-incidence component pass.  Its local
current four-entry checkpoint manifest has SHA-256
`0dc6f0fbba8b9d8e509811b329e02bd35ec6493d1b82c92cf28969bc26aef714`;
its current independent audit has SHA-256
`6bae984f36d2d72ca65af39e2e8438ef488404f21d8446e487c034037783e148`.
The manifest correction note and machine-readable correction have SHA-256,
respectively,
`83b95d373ad4203e58f73b345923f5f4927f4923a7f34e8e7b3044e8e06873af`
and
`1011bcf451a9b0ab0c5262eb40911bbf3cbce1d8fc20cb8aca7518e5daedab90`.
The earlier value `76e29482...` is retained only as the hash of the historical
seven-entry manifest snapshot and is not a present-tense checkpoint binding.

Let `X` denote exactly this hard face: binary incidence degrees, protected
boundary, all frozen guards after rebuilding the ordinary pair channel, one
connected lollipop, all 19,412 ordinary necessary providers, and all 19,448
opened rank-ten targets in each of the two decoded orientations.  For
`F in X`, let

\[
             \Phi(F)=\min\{R_0(F),R_1(F)\},             \tag{1.1}
\]

where each `R_o` is decoded from one complete opening.  Coordinatewise
mixing between orientations is forbidden.  The immediate target is

\[
                              \Phi(F)\le 1993.           \tag{1.2}
\]

## 2. Exact pair-channel current at every prefix

Fix an ordinary root `L`.  Abbreviate incidence variables `y_(L,T)` by
`y_T` and write

\[
                       p_{\{T,H\}}=y_Ty_H.              \tag{2.1}
\]

For one materialized transition `y'=y+z`, the exact pair current is

\[
 \boxed{
 p'_{\{T,H\}}-p_{\{T,H\}}
 =y_Tz_H+y_Hz_T+z_Tz_H.}                               \tag{2.2}
\]

Thus an ordered packet `F_0,F_1,...,F_t` obeys

\[
 p(F_t)-p(F_0)=
 \sum_{i=1}^t\left(
 y^{i-1}_Tz^i_H+y^{i-1}_Hz^i_T+z^i_Tz^i_H
 \right).                                             \tag{2.3}
\]

Equation (2.3) automatically contains every cross-term caused by a repeated
root.  It is generally different from the sum of all primitive deltas
computed against `F_0`.  In particular, if a bridge switches `a -> a'` and
a later quench switches the complementary slot `b -> b'`, then

\[
              \Delta p=[a',b']-[a,b],                  \tag{2.4}
\]

not the sum of the two base-local singleton formulas.

For implementation, (2.2) is best enforced by rebuilding the pair one-hot
state after every incidence transition.  In CNF the exact rows are

```text
(-p_T_H or y_T), (-p_T_H or y_H),
(p_T_H or -y_T or -y_H).
```

Only roots touched by the transition need new pair variables; untouched pair
states are carried by equality.  A full checksum rebuild at each accepted
prefix is the fail-closed audit.

## 3. Neutral bridges and strict quench paths

Let `C(F)` be the complete declared ordinary-root catalogue regenerated from
the literal factor `F`.  In the minimal envelope below, `C` consists of all
current-state alternating C6 and rank-seven-core star-C8 schemas.  A selected
schema is applied only if every removed incidence is selected and every
inserted incidence is absent in the current state.  M/D-root moves and any
move deleting a protected incidence are excluded.

For integers `b,q,D >= 0`, define `B_b^D(F)` to be the factors `G` reachable
from `F` by one to `b` state-relative primitives such that

1. every materialized prefix belongs to `X`;
2. every prefix has `Phi <= Phi(F)+D`; and
3. the bridge endpoint is residence-neutral:

   \[
                              \Phi(G)=\Phi(F).           \tag{3.1}
   \]

For `G in B_b^D(F)`, define `Q_q(G;F)` to be the factors `H` reachable by at
most `q` further state-relative primitives, every prefix again in `X`, with

\[
                       \Phi(H)\le\Phi(F)-1.              \tag{3.2}
\]

The word **strict** here refers to literal hard-face preservation at every
quench prefix.  It does not assume that residence decreases at every
primitive; only the materialized endpoint inequality (3.2) is required.

### Theorem 3.1 (one-step sufficient condition below 1994)

If

\[
 B_b^D(F_*)\ne\varnothing
 \quad\hbox{and}\quad
 \exists G\in B_b^D(F_*):Q_q(G;F_*)\ne\varnothing,     \tag{3.3}
\]

then there is a connected, guard-valid, protected, full-two-opening-q1
factor with literal residence at most 1993.

#### Proof

Every bridge and quench prefix lies in `X`, so all hard claims hold
literally.  The endpoint `H` supplied by (3.3) satisfies (3.2), and
`Phi(F_*)=1994`.  Hence `Phi(H)<=1993`. \(\square\)

Condition (3.3) is sufficient, not necessary: a direct improving primitive,
a nonneutral bridge, an octahedral or longer circuit, or an atomic
terminal-only batch may escape even when this declared oracle is empty.

## 4. Minimal successful and calibration-covering finite envelopes

### 4.1 The smallest nonempty neutral-bridge/quench envelope

The first nonempty strict phase convention has one positive-length bridge
and one positive-length quench.  Thus no envelope smaller than

\[
                    \mathcal E_{1,1}^0(F_*)
 =\bigcup_{G\in B_1^0(F_*)}Q_1(G;F_*)                 \tag{4.1}
\]

can contain a neutral bridge followed by a strict quench.  This smallest
envelope is now witnessed exactly by

```text
step 1  C6       core 7946  labels 4,14,7
step 2  star-C8  core 5914  labels 11,14,15,13.
```

The first circuit is neutral in both openings, `1994 -> 1994`.  It creates
incidence `11158` at the shared root `7962`, thereby activating the second
circuit, which is not applicable at `F_*`.  The second circuit gives
`1994 -> 1993` in both openings.  Both prefixes preserve exact degrees and
owners, the protected boundary, all 16,261 frozen guards, all 19,412 ordinary
non-`D` q1 colours, all 19,448 opened rank-ten targets in both orientations,
and one connected augmented lollipop.  Deeper holes change `1795 -> 1796`.

The compact audit binding is

```text
true_compound_pair.summary.audit.json
  236691b41a13487e897c893e3dd1eceffe55ebe8a6514e81ce6533d004eb3642
activated-pair audit note
  1d47ee73c21c58a0368e92920d48b3d9cbaeedc6954b0214701f1b173a55c53e
KEY_MANIFEST.sha256
  6e128005525605df0f6e54386598a1e5602ce7c39fe5861a1c60242c0b916f34
packet
  415240ce187d0e2caadcbb3d5c7f43ce92914a19d08352444c579664d59b7538
independent materializer audit
  b7b8f48a1029b38cf77753bdaaee2fbb3eba5bda32756d14e562a137616e15b3
prefix-1 model / independent audit
  a73b5fe36e4bd7944c275ffefed5181d502370e9d08ef059c834f39b9fa8142b
  934dbf0d9ff2b908d9b783c10bf1999eb02a1ca82df434db1edd4891119bc4d7
prefix-2 model / independent audit
  a9f0d53bdee43fc5db770ecac57781899c4d0f4fbed3b83ca0ac8b6af00008dd
  eb54a9bd5a06e32878d8c9c3f7415c9ab97e5199848c653e7c8f4e3947ca6874
complete-DIMACS replay at each prefix
  777306ca8ae7cb641d9dc98522b8fa797d9088679764d593d007e169b4e0c224
```

The independent materializer proves the circuit formula, order, applicability,
and literal prefix models.  Each prefix then passes the complete 7,163,170-
clause DIMACS replay and a separate semantic replay.  Hence this is an
independently replayed instance of Theorem 3.1, not a sampled-miss inference.
The terminal is still nonresident; arbitrary-width upper completeness,
source, compiler, and word claims remain excluded.

### Corollary 4.1 (strict carrier improvement)

There exists a factor in `X` with `Phi=1993`, reached from `F_*` by a neutral
C6 bridge followed by one activated star-C8 quench.  In particular,
`E_(1,1)^0(F_*)` is nonempty and successful.

#### Proof

The prefix-1 replay puts its model in `B_1^0(F_*)`.  The prefix-2 replay puts
the terminal in `Q_1(prefix_1;F_*)` and reports `[R_0,R_1]=[1993,1993]`.
Apply Theorem 3.1. \(\square\)

### 4.2 Smallest rectangular envelope covering the authenticated history

The authenticated bridge/quench phase lengths in the earlier macro lineage
are

```text
1+3, 2+3, 3+5, 5+4.
```

Consequently the componentwise smallest rectangular phase-depth envelope
containing every one of those authenticated macros is

\[
                         \boxed{b=5,\qquad q=5.}         \tag{4.2}
\]

Both C6 and star-C8 are required: the frozen lineage contains each family in
bridge and quench phases.  The calibration-covering regenerative test is

\[
                    \mathcal E_{5,5}^D(F_*)
 =\bigcup_{G\in B_5^D(F_*)}Q_5(G;F_*).                 \tag{4.3}
\]

For a literally neutral/nonworsening bridge search take `D=0`; a later run
may enlarge `D` without changing the theorem.  The adjective *smallest* in
(4.2) is calibration-relative only.  It is not a theorem that every next escape
has these bounds.

This is distinct from a fixed-base depth-three compound census:

- primitive activity is regenerated after every prefix;
- roots may be revisited and pair cross-terms use (2.2);
- the phase depth is up to ten physical primitives; and
- states are deduplicated by their full incidence bitset, not by primitive
  subsets, root masks, residence totals, or local defect counts.

The current local state-relative sampler
`scratch/k17_h1_fullq1_escape_res1994_compound_20260802/search_k17_h1_fullq1_overlap_packet_20260802.cpp`
has SHA-256
`ef43457a3d18fd04de9a319b783f38a9d894043c18a45d10e3170a7b218ae592`.
It is a useful witness finder, but its random-trial miss is not the exhaustive
algorithm of Section 5.

A proof-safe collision-free Markov key is

```text
(phase, bridge_depth, quench_depth, complete y bitset).
```

All other acceptance data are deterministic decodes of `y`, but the complete
pair, guard, provider, seam, topology, and residence replays must accompany
every retained node.  Hashes may index states; equality and deduplication
must compare the literal bitsets to remain collision-free.

## 5. Exact exhaustive state-graph algorithm

The following algorithm decides (3.3) for the declared finite envelope.

1. Insert `(bridge,0,0,F_*)` into a collision-checked state table.
2. At every bridge node of depth below five, regenerate all C6/star-C8
   schemas from its current incidence assignment.  Materialize every
   alternating candidate, rebuild its pair state, and retain it exactly when
   it lies in `X` and respects the debt bound.  Every retained neutral node
   of positive bridge depth is copied across the zero-cost phase switch to
   quench and also remains eligible to continue the bridge while depth
   remains.  A nonneutral retained node may only take the latter continuation.
3. At every quench node of depth below five, regenerate the catalogue again,
   materialize every candidate, and retain every hard-valid prefix.  Accept
   immediately when the decoded endpoint satisfies `Phi<=1993`.
4. Deduplicate only identical literal states at the same phase/depth.  Every
   retained bridge path has already passed the pathwise debt test, and all
   future legality is a function of the keyed state, so one predecessor and
   primitive suffice for a witness.
5. If the entire frontier is exhausted, report a no-go only for
   `E_(5,5)^D`, the declared primitive families, strict-prefix semantics, and
   the frozen boundary face.

Every accepted transition is independently replayed from its predecessor.
Completeness inside the envelope requires enumerating all geometric schemas
at every retained node; random trials, a fixed root catalogue, or an empty
gain-seeded pair list do not certify exhaustion.

### Theorem 5.1 (algorithm correctness)

The algorithm returns a witness if and only if `E_(5,5)^D(F_*)` contains a
factor satisfying (3.2).  Exhaustion without acceptance proves that no
neutral-bridge/strict-quench packet in this finite envelope reaches residence
below 1994.

#### Proof

Induct on the two phase depths.  The root is present.  Complete current-state
catalogue generation and literal acceptance retain exactly every legal next
prefix.  Bitset deduplication merges equal Markov states and no unequal
states.  Therefore all and only paths in (4.3) are represented.  The terminal
decoder tests (3.2) exactly. \(\square\)

## 6. Fail-closed SAT/Benders integration

Let `C_all` be the complete finite global universe of oriented ordinary-root
C6 and star-C8 geometries on the frozen boundary face.  It is not the root
catalogue `C(F_*)`: current applicability is imposed by (6.1), so activated
geometries such as the witnessed second star-C8 remain present.  A lazy
column implementation is exact only if its pricing/exhaustion certificate
proves that no geometry of `C_all` was omitted.

An equivalent layered SAT/ILP uses one selector from `C_all` per active
physical transition.  State layer `i` is *before* primitive `i+1`; a phase
bit, bridge/quench counters, an active bit, a phase-switch bit, and a terminal
bit implement the following deterministic control automaton:

1. the initial phase is bridge, with both counters zero;
2. a selected bridge or quench primitive increments only its own counter;
3. a phase switch consumes no primitive layer, is allowed only at a neutral
   bridge state of positive bridge depth, and is irreversible;
4. termination is allowed only after positive quench depth and only at a
   target state; and
5. inactive padding copies the entire incidence, pair, and semantic seam state.

For an exact ten-transition implementation, let `a_i` mark an active slot,
`q_i<=a_i` mark that slot as quench, and set `a_0=1`, `a_10=0`,
`a_(i+1)<=a_i`, `q_0=0`.  Impose

\[
 \sum_{c\in C_{all}}\lambda_{i,c}=a_i,qquad
 q_{i+1}\ge q_i+a_{i+1}-1,                            \tag{6.0}
\]

and let `s_i` be exactly `q_i AND not q_(i-1)` (`s_0=0`), while
`t_i=a_(i-1)-a_i` for `1<=i<=10`.  The unary or integer counters

\[
 b_i=\sum_{j<i}(a_j-q_j),\qquad r_i=\sum_{j<i}q_j
\]

obey `b_i<=5`, `r_i<=5`; `s_i` implies `b_i>=1` and neutrality of state
`i`, while `t_i` implies `r_i>=1` and the terminal target.  The switch is
unique because quench mode is irreversible on active slots.  When `a_i=0`,
(6.2) copies `y`, and explicit equivalences copy `p` and `sigma`.  These are
the selector partition, irreversible phase recurrence, counter update, and
absorbing padding rows; standard sequential counters give their literal CNF.

Thus a neutral bridge state is represented in both successor modes rather
than being forced to switch, and five bridge plus five quench primitives use
ten physical transitions, not eleven.  If `lambda_(i,c)` selects oriented
schema `c` with delete/add sets `D_c,A_c`, impose

\[
 \lambda_{i,c}\Rightarrow y^i_e=1\ (e\in D_c),\qquad
 \lambda_{i,c}\Rightarrow y^i_e=0\ (e\in A_c),         \tag{6.1}
\]

\[
 y^{i+1}_e=y^i_e-
       \sum_c\lambda_{i,c}\mathbf1[e\in D_c]
       +\sum_c\lambda_{i,c}\mathbf1[e\in A_c],        \tag{6.2}
\]

with exactly one schema selected on every active physical transition.  A
switch is a control transition at a state and a stop begins equality-padding;
neither is inserted into (6.2).  Every active state rebuilds `p` by the AND
rows after (2.2), then enforces all frozen guards, the relevant depth bound,
and the control implications above.

The remaining exact lazy separators are:

1. **Connectivity.**  Let `E_fix` be the fixed selected augmented incidences
   and `E_var` the allowed binary incidences.  If a decoded layer has a
   nontrivial component shore `S`, then no edge of `E_fix` crosses `S`; add

   \[
             \sum_{e\in\delta(S)\cap E_{var}}y^i_e\ge1. \tag{6.3}
   \]

   An empty left side is an exact infeasibility row.  More generally, before
   emitting a cut for an arbitrary shore, subtract the number of fixed
   selected crossings from the right side.

2. **Opened q1.**  Reconstruct the seam state.  For a missing target `U` in
   orientation `o`, add the exact provider row

   \[
   \sum_{\substack{L\notin\{M,D\},\{T,H\}\\T\cup H=U}}
       p^i_{L,\{T,H\}}
   +\sum_s\sigma^i_s\mathbf1[I_{s,o}=U]\ge1.          \tag{6.4}
   \]

   Emit (6.4) for every missing pair `(o,U)`.  Here `sigma^i` is one-hot and
   is exactly channelled to the exceptional incidences and decoded
   tail/branch roles of layer `i`.  The physical closing seam is absent.  If
   `U` does not contain `D`, every `I_(s,o)` contains `D`, so the seam term is
   zero.  These rows therefore include, rather than replace, all 19,412
   ordinary non-`D` provider predicates in `X`.
3. **Semantic seam or decoder failure.**  Add a complete layer-state
   no-good on `(y^i,sigma^i)` unless uniqueness of `sigma^i` as a function of
   `y^i` has been proved, or unless a stronger proved semantic row is
   available.  With one-hot `sigma` and selected seam state `s_*`, the exact
   selected-only form is

   \[
       \neg\sigma^i_{s_*}\ \vee\
       \bigvee_{e\in F\cap E_{var}}\neg y^i_e.          \tag{6.5}
   \]

4. **Residence phase rule.**  Decode both complete openings.  A bridge state
   violating its debt bound receives the phase-conditioned selected-state
   no-good

   \[
       \neg\beta_i\ \vee\ \neg\sigma^i_{s_*}\ \vee\
       \bigvee_{e\in F\cap E_{var}}\neg y^i_e,          \tag{6.6}
   \]

   where `beta_i` means that state layer `i` is in bridge phase (`r_i=0`).
   If physical bridge and quench layers are statically separated, `beta_i` is fixed true on
   a bridge layer and may be dropped there.  It must not be dropped in the
   variable-switch formulation: the same factor can be debt-illegal as a
   bridge state yet legal as a quench prefix.

   After fixed incidences are removed, all degree-valid factors have the same
   variable-incidence cardinality, so the state part of (6.6) identifies
   exactly `F` at that layer.  Neutrality is required only when the bridge
   phase is exited, and the residence target is required only when a quench
   terminal/stop is declared.  Therefore a nonneutral bridge state or a
   nontarget quench prefix must remain available for continuation.  If `a_i` is the
   corresponding phase-switch or terminal literal, use instead

   \[
       \neg a_i\ \vee\ \neg\sigma^i_{s_*}\ \vee\
       \bigvee_{e\in F\cap E_{var}}\neg y^i_e.          \tag{6.7}
   \]

   If an explicit orientation is a decision rather than the minimum in
   (1.1), include that orientation literal as well.

Normalize every emitted clause as a set of signed literals, reject
tautologies, sort, and deduplicate by the normalized vector while retaining
provenance `(layer, phase, row type, shore/target/state hash)`.  A final UNSAT
claim additionally requires the complete layered formula, proof, checker,
and an independently replayed manifest; a timeout or sampled miss is
`UNKNOWN`.

## 7. Uniform regenerative specialization

If legality has persistent data not determined by the factor, lift to the
state space `Xhat={(F,rho): F in X and rho is the complete persistent
resource record}`.  Define `Phi(F,rho)=Phi(F)` and define `Bhat,Qhat` by the
same literal-prefix rules as `B,Q`, while updating `rho` exactly.  Let
`Y subseteq Xhat` be endpoint-closed.  Temporary masks may be cleared at a
commit only under a proved reset rule; one-use tickets and consumed budgets
remain coordinates of `rho`.  In the factor-Markov case take `rho` empty.
Assume that for every `x in Y` with `Phi(x)>0` there are

\[
 g\in \widehat B_b^D(x),\qquad
 h\in \widehat Q_q(g;x)\cap Y,\qquad
                         \Phi(h)\le\Phi(x)-\epsilon      \tag{7.1}
\]

for fixed `b,q,D` and integer `epsilon>=1`.

### Theorem 7.1 (regenerative bridge descent)

Under (7.1), repeated literal regeneration reaches `Phi=0` after at most

\[
                         \left\lceil
                         \frac{\Phi(F_{start})}{\epsilon}
                         \right\rceil                  \tag{7.2}
\]

commits.  Every committed endpoint lies in `Y`; every claimed packet prefix
lies in `Xhat`.

#### Proof

Every committed endpoint lies in `Y`, so (7.1) applies again while its nonnegative
integer score is positive.  Every commit decreases that score by at least
`epsilon`, proving (7.2). \(\square\)

The authenticated macros above 1994 prove several instances of (7.1), not
the universal quantifier.  Corollary 4.1 proves one pointwise transition from
`F_*`, not renewal or the universal condition.  Neither outcome establishes source, compiler, deeper-
upper completeness, a resident factor, or a word.
