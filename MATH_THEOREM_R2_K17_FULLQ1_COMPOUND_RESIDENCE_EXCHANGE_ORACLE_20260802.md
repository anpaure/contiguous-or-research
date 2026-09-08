# R2 theorem: exact full-q1 compound residence-exchange oracle

**Date:** 2026-08-02  
**Status:** exact terminal-batch/joint-column and fail-closed Benders
formulation, calibrated at the current full-q1 residence-2018 factor and its
positive neutral-bridge/ordered-quench predecessor packet.  This note does not
assert that the declared primitive catalogue is complete, that the packet
regenerates uniformly, or that a resident/source/compiler word has been
constructed.

## 1. Literal base and acceptance objective

Let `F0` be the current connected normalized h1 factor

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  escape_s2_quench.best.model
SHA-256 c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d
```

Its frozen passive replay gives, for the two topology-derived licensed
openings,

```text
orientation 0: short-run histogram (length 2,3) = (1277,741), total 2018
orientation 1: short-run histogram (length 2,3) = (1276,742), total 2018
rank-10 holes in either orientation = 0
```

The hard face in this theorem consists of the exact incidence degrees, the
normalized protected `M/D` boundary, all 16,261 frozen guard clauses, one
connected augmented-incidence component, and all 19,448 opened rank-ten
targets in **each** of the two licensed orientations.

For a connected final factor `F`, reconstruct the `M`-to-`D` tail and the two
cycle branches.  They determine two opened owner words `T^(0)(F),T^(1)(F)`;
they are not inherited from the incumbent.  Let

\[
 R_o(F)=\#\{\hbox{literal internal maximal positive owner runs of length at
 most three in }T^{(o)}(F)\}.                         \tag{1.1}
\]

This is the already frozen literal opened-run convention: endpoint-clipped
runs are treated by the boundary decoder, and no ordinary-component proxy is
substituted.  At `F0`, `R_0=R_1=2018`.

For the existential construction objective put

\[
                         R_{\min}(F)=\min(R_0(F),R_1(F)). \tag{1.2}
\]

If the intended contract instead protects both residence profiles, retain
the complete vector `(R_0,R_1)` and require componentwise nonincrease with at
least one strict decrease, or minimize its sorted pair.  The q1 gate below is
two-orientation in either policy.  A column must store both literal scores;
coordinatewise minima from different openings are forbidden.

## 2. Exact fixed-base composition with overlapping roots

Let `E` be the incidence-option universe and write `y^0_e=1[e in F0]`.
A fixed-base primitive `q` declares two sets

\[
       D_q\subseteq F_0,\qquad A_q\subseteq E\setminus F_0. \tag{2.1}
\]

The semantics in this section is **set-union terminal batch semantics**.  A
selected family need not give a factor at any proper prefix.  For primitive
selectors `lambda_q`, introduce union indicators

\[
 d_e\longleftrightarrow\bigvee_{q:e\in D_q}\lambda_q,
 \qquad
 a_e\longleftrightarrow\bigvee_{q:e\in A_q}\lambda_q,    \tag{2.2}
\]

and materialize

\[
                         y_e=y^0_e-d_e+a_e.                \tag{2.3}
\]

The standard fail-closed CNF channel for the first equivalence is

```text
(-lambda_q or d_e)        for every q with e in D_q,
(-d_e or lambda_q1 or ... or lambda_qt),
```

and analogously for `a_e`.  Empty disjunctions fix the indicator to zero.
Thus two primitives may share a root or the same removed row; the common
operation is applied once.  Root overlap is decided by the final degree
rows, not by adding two independently computed root deltas.

If the intended semantics counts repeated operations rather than taking
their union, replace (2.2) by an integer signed sum and enforce that (2.3) is
binary.  If primitives are state-relative and ordered, neither static rule is
complete: regenerate the catalogue after every materialized prefix and use
the ordered lifted builder.  These three semantics may not be mixed.

### Theorem 2.1 (exact overlap materialization)

Under (2.1)--(2.3), every Boolean primitive selection has exactly the final
row set

\[
 F(\lambda)=\bigl(F_0\setminus\bigcup_{q:\lambda_q=1}D_q\bigr)
             \cup\bigcup_{q:\lambda_q=1}A_q.             \tag{2.4}
\]

Conversely every terminal union rewrite from the declared primitive family
is represented by (2.2)--(2.3).  Therefore all root-overlap, cancellation,
and collision questions are settled exactly by replaying the final Boolean
state.  No claim about a legal order of its primitives follows.

#### Proof

The two OR channels are precisely the characteristic vectors of the two
unions in (2.4).  Their supports lie on opposite sides of `F0`, so (2.3) is
the characteristic vector of (2.4).  The converse selects the primitives in
the declared union. \(\square\)

## 3. Final degree, pair, topology, and two-opening q1 rows

On the augmented h1 incidence graph impose

\[
 \sum_{T\supset L}y_{L,T}=
 \begin{cases}
 1,&L=M,\\
 3,&L=D,\\
 2,&L\notin\{M,D\},
 \end{cases}
 \qquad
 \sum_{L\subset T}y_{L,T}=2.                            \tag{3.1}
\]

Fix every protected incidence and impose every frozen guard on the final
assignment.  For each ordinary root channel its unique owner pair by

\[
 p_{L,\{T,H\}}\longleftrightarrow y_{L,T}\wedge y_{L,H}. \tag{3.2}
\]

Let `S` be the complete licensed semantic seam-state set.  A state `s`
records the final tail incidence at `D` and its two cycle branches.  Use a
one-hot `sigma_s`, channel it to `y`, and denote its two internal opened seam
colours by `I_(s,0),I_(s,1)`.  Connectivity and tail correctness are either
encoded eagerly or separated from the final integral graph.  In particular,
`sigma` may not reuse the incumbent tail after a topology-changing batch.

For every `U in C([17],10)` and both `o in {0,1}`, impose

\[
 \boxed{
 \sum_{\substack{L\notin\{M,D\},\{T,H\}\\T\cup H=U}}
     p_{L,\{T,H\}}
 +\sum_{s\in S}\sigma_s\mathbf 1[I_{s,o}=U]\ \ge 1.}    \tag{3.3}
\]

There are 19,448 logical rows in each frame.  The physical closing seam is
not adjacent in an opened chronology and is absent from (3.3).

### Theorem 3.1 (exact terminal acceptance)

A selected primitive family is an accepted terminal compound packet exactly
when its materialized `y` satisfies (3.1), every protection and guard row,
the augmented graph is connected with a licensed decoded seam state, all
channels (3.2) are rebuilt, and every row (3.3) holds.  It is a strict
existential residence improvement exactly when, in addition,

\[
                            R_{\min}(F(\lambda))<2018.    \tag{3.4}
\]

For the two-profile policy replace (3.4) by its declared vector comparison.

#### Proof

Equations (3.1) are exactly the final incidence degrees, and (3.2) identifies
every ordinary consecutive-owner diamond.  A connected graph with these
degrees is the licensed lollipop, so its tail and two orientations are
literal.  Rank-ten intervals are exactly adjacent-owner unions; hence (3.3)
is necessary and sufficient for opened q1 in the corresponding orientation.
Finally (1.1) is the literal score of the materialized opening, so (3.4) is
equivalent to strict improvement. \(\square\)

Notice that the full q1 property is not imposed only at the terminal
orientation chosen by (1.2): both rows of (3.3) remain hard.

## 4. Joint columns and exact pricing

A **joint column** `P` is identified by its canonical final pair

\[
 D(P)=F_0\setminus F_P,\qquad A(P)=F_P\setminus F_0,     \tag{4.1}
\]

not by a multiset of primitive names.  Its certificate stores:

1. the final selected-incidence bitset and rebuilt ordinary-pair bitset;
2. the final tail and the unordered pair of licensed orientations;
3. all two-opening q1 multiplicities in (3.3);
4. the exact pair `(R_0(F_P),R_1(F_P))`; and
5. the degree, protection, guard, and connectivity verdicts.

Deduplicate columns by the canonical final bitset (and by an explicit
orientation choice only if the objective chooses, rather than minimizes
over, an orientation).  Two different primitive descriptions of the same
final factor are one column.

Let `P*` be the accepted columns after Theorem 3.1's hard tests, and include
the no-op.  The one-hot master

\[
 \sum_{P\in\mathcal P^*}\eta_P=1,
 \qquad
 \min\sum_{P\in\mathcal P^*}
       \bigl(R_{\min}(F_P)-R_{\min}(F_0)\bigr)\eta_P      \tag{4.2}
\]

is the exact minimum residence delta in the declared materialized catalogue.
If hard tests are deferred, attach the binary coefficient

\[
 A_{o,U,P}=\mathbf1[m^{open}_{o,U}(F_P)>0]               \tag{4.3}
\]

and add `sum_P A_(o,U,P) eta_P >= 1` for every `(o,U)`, plus analogous
one-hot validity rows.  Because exactly one complete final-state column is
chosen, these rows are exact.

With master rows `sum_P A_(r,P) eta_P>=b_r`, dual weights `pi_r>=0`, and
one-hot multiplier `mu`, the pricing convention

\[
 \bar c(P)=c(P)-\sum_r\pi_r A_{r,P}+\mu                 \tag{4.4}
\]

is exact provided every `A_(r,P)` and `c(P)` is computed from the complete
final state.  A negative reduced-cost primitive signature is not a column
until it has been materialized and certified.

### Corollary 4.1 (what multi-column selection means)

Whole-factor columns in (4.2) are alternatives and must not be selected in
parallel.  To combine several primitive proposals, either:

1. use the OR materialization (2.2)--(2.3) and rebuild the final state;
2. introduce their simultaneous union as one joint column; or
3. prove that their supports, q1 channels, topology interfaces, and residence
   halos are separable, in which case their certified signatures may be
   added.

Root disjointness alone does not imply item 3: two distant incidence moves
can interlace on the same owner chronology and create a residence cross term.

## 5. Fail-closed Benders decision and optimization loop

For an exact strict-improvement query set the residence bound `B=2017`.
The master contains (2.2)--(3.3), the hard guards, and every accumulated
connectivity/topology cut.  For each integral candidate perform this
transaction.

1. Rebuild `y` from the selected primitive set and independently rebuild all
   `p` channels.  Reject any mismatch.
2. Replay (3.1), protection, and all frozen guards.
3. If the augmented graph is disconnected, add a standard incidence cut
   crossing a decoded non-root component.  If its semantic tail cannot be
   certified by a stronger global row, add the complete factor no-good.
4. Reconstruct the final tail and both licensed orientations.  For every
   missing `(o,U)`, add the exact row (3.3).  Never count the closing seam.
5. Run the literal opened residence decoder on both complete owner words.  If
   the declared score is at most `B`, accept.  Otherwise add an exact
   final-factor no-good and continue.

Every feasible factor has the same selected-incidence cardinality.  Hence
for a rejected factor `F*` the selected-only clause

\[
                         \bigvee_{e\in F^*}\neg y_e       \tag{5.1}
\]

excludes exactly that factor: any feasible factor retaining all its selected
incidences has no cardinality left with which to differ.  If orientation is
an explicit decision rather than the minimum in (1.2), include its orientation
literal in the no-good.

For an epigraph variable `theta>=0`, the conditional cut

\[
 \theta\ge R_{\min}(F^*)-
 R_{max}\sum_{e\in F^*}(1-y_e),                         \tag{5.2}
\]

where `R_max` is any valid global upper bound, is also sound.  It is exact at
`F*` and vacuous after any selected incidence changes.  A full no-good is
usually stronger for the decision bound.

For the special target `R=0`, a decoded internal short coordinate component
`C` disjoint from the seam bank also yields the stronger persistence cut

\[
 \bigvee_{e\in E(C)}\neg p_e\ \vee
 \bigvee_{f\in\delta_x(C)}p_f\ \vee
 \bigvee_{\substack{T\in C\\D\subset T}}y_{D,T}.        \tag{5.3}
\]

It says that the retained internal spanning edges, absence of an external
`x`-edge, and absence of a newly activated `D` seam cannot coexist.  Cut
(5.3) is not valid as an unconditional strict-descent cut when `B>0`: an
improving factor may legitimately retain this short run while destroying
more others.  Use (5.1), an exact age/history encoding, or blocker indicators
with a final literal replay for positive bounds.

### Theorem 5.1 (soundness and scoped completeness)

The loop above accepts only a hard-valid, two-opening-full-q1 factor whose
literal declared residence score is at most `B`.  If the declared fixed-base
primitive family is finite, repeated exact separation terminates.  A
proof-verified UNSAT final master certifies that no terminal union batch in
that declared family attains the bound.

#### Proof

Every structural or q1 row is necessary for an accepted factor.  Every
semantic no-good removes only a state independently decoded to fail, and
(5.1) removes exactly one final factor.  Thus no accepted state is cut.
Conversely, every candidate is either accepted or removed, and there are
finitely many final Boolean states. \(\square\)

The UNSAT scope is the declared primitive universe and union semantics.  It
does not cover a state-relative primitive enabled only after a prefix, a
larger support envelope, or a different protected boundary face.

Clause files must be normalized as sets of signed literals: delete repeated
literals, reject tautologies, sort, and hash the normalized vectors.  Retain
the provenance list `(row type, orientation, target, candidate hash)` even
when two logical rows deduplicate to the same literal vector.  Never merge
two seam frames merely because their incumbent colours agree.

## 6. Safe and unsafe local deltas

The following quantities are additive or otherwise safe under their stated
hypotheses.

1. **Incidence currents.** Degree and protected-row changes are linear in the
   exact final signed incidence vector, provided (2.3) is binary.
2. **Ordinary q1 multiplicities.** They are linear in the rebuilt pair vector
   `p`.  For a single switch retaining its other endpoint, the usual
   root-local old/new colour formula is exact.  If two switches touch the same
   root or replace both endpoints, rebuild `p`; the two base-local formulas
   need not add.
3. **A fixed primary residual shore.** Once a primary selector, boundary
   capacities, and actual provider channels are fixed, its closed-shore
   current is linear.  The maximum-flow *gain* is not additive, because a
   different shore may become maximum; one fresh min-cut is the acceptance
   rule.
4. **Ordered endpoint differences.** Along a materialized strict path,
   `R(F_i)-R(F_(i-1))` telescopes to the exact terminal difference.  Every
   prefix must be a literal factor in the hard face.
5. **Residence on proved separated halos.** Additivity is valid only when the
   retained-path/trace interfaces are disjoint in the sense of the circuit
   transfer theorem, or when all relevant pair/triple Moebius interaction
   terms have themselves been obtained from literal subset commits.

The following shortcuts are unsound.

1. Summing singleton residence deltas for overlapping roots, or for
   root-disjoint moves whose chronology halos interlace.
2. Substituting the ordinary-component score `2016` for the current literal
   opened score `2018`.
3. Adding support/hole indicators instead of provider multiplicities; losing
   the last provider is nonlinear.
4. Reusing the incumbent `D` tail or seam colours after a topology-changing
   batch.
5. Adding component counts, voltage labels, or guard-safe verdicts of
   separately feasible moves.
6. Testing q1 in only one opening, or using the physical closing seam in an
   opened row.
7. Accepting a move because it improves the current maximum residual shore
   or kills more incumbent short runs than it creates locally.  A new shore
   or a new cross-boundary run may dominate.
8. Treating an empty prefiltered pair list as a compound no-go.

These distinctions are exactly why pricing may use cheap local scores, while
acceptance must use the materialized final state.

## 7. Algebraic neutral-bridge/atomic-quench pattern

Let `A` be the root--owner degree matrix.  For an ordered materialized bridge
`b_i` put

\[
 z_i=y(H_i)-y(H_{i-1}),
\]

and for a terminal atomic batch at the last bridge state put

\[
 z_Q=y(G)-y(H_m).
\]

The aggregate current is

\[
 z=z_1+\cdots+z_m+z_Q=y(G)-y(H_0),\qquad Az=0.          \tag{7.1}
\]

Equivalently, for every root `L` and owner `T`,

\[
 \sum_{H\supset L}z_{L,H}=0,
 \qquad
 \sum_{L\subset T}z_{L,T}=0.                           \tag{7.2}
\]

Repeated roots are allowed.  A root touched by both bridge and quench can
have two old and two new incidences in the aggregate while its row sum in
(7.2) remains zero.  If a bridge-added row is later removed, its two signed
occurrences cancel in (7.1); this is exact for the final state but cannot be
represented as a fixed-base deletion set satisfying (2.1).  Use the ordered
bridge plus a batch based at `H_m`, or canonicalize the whole result as the
single final symmetric difference (4.1).

Equation (7.1) is necessary, not sufficient.  It forgets binary prefixes,
which circuit schemas are alternating after the bridge, the rebuilt pair
variables at a repeated root, q1 last-provider loads, guards, and topology.
Indeed, if bridge and quench currents at one root are `z_b,z_q`, then the
quadratic pair channel has the exact cross term

\[
 \Delta p_{b+q}=\Delta p_b+\Delta p_q+C(z_b,z_q),\qquad
 C_{\{u,v\}}=z_b(u)z_q(v)+z_q(u)z_b(v).                \tag{7.2a}
\]

It is nonzero when the bridge and quench turn over complementary slots, as
at the two repeated roots of the finite packet.  Thus zero aggregate degree
current does not authorize adding base-local q1 or pair deltas.

### Theorem 7.1 (enabled-schema rule)

Let `Q(F)` be the complete declared primitive catalogue regenerated from the
literal state `F`.  A bridge--quench packet

\[
 H_0\xrightarrow{b_1}\cdots\xrightarrow{b_m}H_m
       \xrightarrow{\text{atomic }Q}G                  \tag{7.3}
\]

is certified when every bridge prefix is a hard-valid factor, every member
of the terminal batch belongs to `Q(H_m)`, and the jointly materialized `G`
passes Theorem 3.1.  It is not necessary that an arbitrary ordering of the
members of `Q` give connected or q1-complete intermediate factors.  Conversely,
cataloguing `Q` only at `H0` can be incomplete; it is incomplete whenever
`Q(H_m)\Q(H_0)` contains a schema needed by the packet.

Under strict continuation semantics replace the atomic last arrow by

\[
 H_m=K_0\xrightarrow{q_1}K_1\xrightarrow{q_2}\cdots
 \xrightarrow{q_t}K_t=G,qquad q_j\in Q(K_{j-1}),       \tag{7.3a}
\]

and require every `K_j` to be hard valid.  A schema enabled only after
`q_1,...,q_(j-1)` need not belong to `Q(H_m)`; regeneration at every prefix
is the completeness-safe rule.

#### Proof

The forward assertion is the definition of ordered-prefix plus atomic-commit
semantics and Theorem 3.1.  For the converse, alternation is a predicate of
the current selected incidence bitset.  Changing that bitset can create or
destroy a schema, so `Q(H0)` need not equal `Q(Hm)`.  A changed incidence does
not by itself prove strict inclusion; the two catalogues must be compared.
For (7.3a), current-state membership and hard validity at every displayed
prefix are plainly necessary and, by materialization, sufficient.
\(\square\)

For any declared literal objective `Phi` (`R_min` here), fixed bridge length
and terminal support bounds also give an exact pricing network.  Its layered
vertices are the materialized hard-valid bridge states.  Bridge arcs have
cost zero.  From every retained `H_m`, attach one
commit arc for each jointly materialized terminal batch, with cost

\[
                              \Phi(G)-\Phi(H_0).          \tag{7.4}
\]

The shortest root-to-commit path is therefore the minimum literal final
delta over the declared hybrid catalogue.  Equivalently, charge telescoping
literal bridge differences and the last endpoint difference.  Network-flow
integrality is exact after the state graph has been built; it does not make
the catalogue polynomial in the carrier size or permit a commit cost made
from singleton deltas.

There are therefore two distinct preservation contracts.

* **Strict-prefix preservation:** every primitive prefix, including every
  member of the quench, must satisfy both 19,448-row opened q1 frames,
  connectivity, guards, and degrees.
* **Bridge/terminal preservation:** every bridge prefix and the final joint
  commit satisfy those rows.  Internal partial quench states receive no
  factor, topology, q1, or residence claim.

The general terminal-batch oracle permits the second contract.  The stronger
positive finite packet below has now been independently replayed under the
first, strict-prefix contract.

### Theorem 7.2 (proof-safe sufficient regeneration lemma)

Let `X` be a finite hard class satisfying degrees, guards, protected rows,
connectivity, and both complete opened q1 frames.  Let `Phi:X->Z_(>=0)` be a
literal final score, here `R_min`.  Suppose there are fixed integers
`ell,h,B>=0` and `epsilon>=1` such that for every `F in X` with `Phi(F)>0`
there is a packet of the form (7.3), with `H_0=F`, satisfying:

1. `m<=ell`, every bridge prefix lies in `X`, and
   `Phi(H_i)<=Phi(F)+B`;
2. the terminal batch is generated at `H_m`, has union support at most `h`,
   and its materialized endpoint `G` lies in `X`; and
3. `Phi(G)<=Phi(F)-epsilon`.

Then repeated bridge/terminal commits reach `Phi=0` after at most

\[
                         \left\lceil\Phi(F_{start})/\epsilon\right\rceil
                                                                  \tag{7.5}
\]

packets, never leaving `X` at a claimed factor state.

#### Proof

Every committed endpoint again belongs to `X`, so the hypothesis regenerates.
The nonnegative integer `Phi` decreases by at least `epsilon` at each commit.
It can therefore support at most the number of commits in (7.5).  If a
terminal endpoint had positive score, the hypothesis would supply another
packet, so termination occurs at zero. \(\square\)

This is a sufficient regeneration theorem, not a consequence of the current
packet.  Establishing it requires a uniform enabled-schema/return statement
over every positive-score state in `X`.

## 8. Current finite calibration and plateau scope

The predecessor `strict17` factor and its singleton census have hashes

```text
fullq1_strict17.best.model     5499b2fb492a6307e531bf33f20341a3e1c89c44cd45e0ee88ae6a8556c5e4fa
fullq1_strict17.extended.model 47deb8628c43290608f320c59debbd48c1a8920c381f78d79ec3faef4dc19ab6
fullq1_strict17.audit.json     07910032872f507b1f093b97d58a752ebd17ab6080154e15d26541d6b63f69e0
fullq1_strict17.passive.audit  914be37333d831dd503344684a72a8f213a5062d1a3deef15377f2fac1f7d658
fullq1_strict18.audit.json     14b0d6e09eb6b72ea0d4dbf741dc1815421910323d0df731c4a46131afd78f74
fullq1_strict18.best.model     5499b2fb492a6307e531bf33f20341a3e1c89c44cd45e0ee88ae6a8556c5e4fa
```

The `strict18` audit reports, at the `strict17` factor, a complete current
state census of 46,735 alternating unprotected C6 geometries and 55,260
alternating unprotected star-C8 geometries, with 14,119 guard-safe moves and
zero lossless residence-improving singleton.  Its pair branch reports

```text
pair_candidates=0, pairs_tested=0.
```

Inspection of the frozen builder shows that this pair list is seeded only by
moves with a nonempty q1-gain set.  At a full-q1 factor there are no missing
q1 targets, so the empty list is not an exhaustive test of neutral/worsening
first moves, synergistic root-disjoint pairs, or root-overlapping packets.
It is therefore a singleton plateau plus an empty gain-seeded pair branch,
not a compound no-go.

The positive escape is a neutral C6 bridge followed by an ordered three-C8
quench.  The bridge is catalogue row 2508:

```text
roots 15672,15768,16152
old   25943,26169,26860
new   26167,26862,25944
```

The terminal quench, regenerated after that bridge, uses rows
`2446,12688,2243`.  Its three root sets are

```text
15129,16152,15130,47896
104210,112386,104226,120578
13625,13626,15672,79160
```

Thus the quench circuits are root-disjoint from each other, but the complete
bridge--quench packet repeats roots `16152` and `15672`.  Rows 12688 and 2243
are disconnected when applied singly to the immediate post-bridge state.
Nevertheless the independently replayed order

```text
2446 -> 12688 -> 2243
```

keeps all guards, a positive ordinary q1 minimum, both opened q1 hole counts
zero, the protected boundary, and one augmented component after every prefix.
Thus this witness is strict-prefix legal; its weaker atomic terminal commit
would also be accepted by Sections 2--5.

The aggregate toggles 15 old and 15 new incidences on 13 distinct roots; its
root and owner degree currents are identically zero.  The bridge row has
ordinary residence delta zero, while the final literal replay improves both
opened scores from the predecessor's 2025 to 2018.  The exact final replay
also reports two-opening q1 holes `[0,0]`, one connected lollipop, all frozen
guards, and deeper holes `(1518,278,4)` in either orientation.

The promoted artifacts are

```text
escape_s2_bridge.best.model     748bc5cfe639028fd6642f044249740f333e5849556c9684af551e4f7356ef64
escape_s2_bridge.audit.json     77cbcd9cff041446208984d0b6a8b5e6b6e9c281f62ed81cfc2e4b1bc152e28e
escape_s2_bridge.catalogue.tsv  50f2375697cc07e66b9cae4277b4b446e8396b863e388336f30e3c7d5935d63b
escape_s2_quench.best.model     c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d
escape_s2_quench.extended.model 956f147f3ec77b118cfd99e699fdb73f2d3d49604fb7966cd81e2deb40e89ab2
escape_s2_quench.audit.json     8976bfd4854338672de88dfe0036cdddf46c46095c164d836056e1be1890d280
escape_s2_quench.passive.audit  ea24de7b229b572ad2f25a3a03f96230b29266daf56c2daf5ce92435b2f331ec
escape_s2_quench.catalogue.tsv  53267516d1af6fa7f029af3e8aa4153035b06edb076a8e795a928c77a2b1ad92
strict-prefix independent audit 4d0cac9a426125da2cbb5a3134b9b4b64f64cccbdd01f4907e7829c2575d3063
strict-prefix verifier source   46e0ddaa3ccca27bc853d8ab27d9094614f900c81cf071cd09c0953978d8a22e
strict-prefix move ledger       8ae21b56cec03e04386b3c2f8aad441ec1421e5c9f3387d3da744a4aaf9d2488
terminal independent checkpoint 885f62c5b7689ada00970688a9771a5bcaa543657e3fae3d065aed3d1f41cb9d
pair-cross-term audit theorem   5f4b8bd99fc1e173513eba52c16013f8c3d4b0d159acc04b492c8ee75aaf1cdc
```

This is a positive four-primitive strict hybrid packet, not a uniform
regeneration theorem and not evidence that four is minimal.

## 9. Exact scope

This theorem supplies an exact terminal acceptance and pricing contract for
compound fixed-base batches, including root overlap, and a finite fail-closed
Benders procedure.  The ordered strict-prefix theorem remains the correct
contract for state-relative packets.

Nothing here proves residence zero, ranks 11--17, a source antecedent, lower
or terminal compiler, exterior opening windows, regeneration, a length-24,313
word, or `nu(17)=24313`.  A no-improvement result is global only for the
explicitly frozen primitive envelope and composition semantics whose final
master receives a proof-verified UNSAT verdict.
