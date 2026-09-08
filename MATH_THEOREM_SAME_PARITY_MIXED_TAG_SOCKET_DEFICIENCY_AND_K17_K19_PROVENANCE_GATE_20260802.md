# Same-parity Pascal mixed-tag deficiency and the `k=17 -> 19` provenance gate

**Date:** 2026-08-02  
**Status:** exact conditional Hall obstruction for the standard indivisible
four-sector recurrence; exact audit of the frozen `m=9 -> 10` provenance;
no authenticated literal `k=17 -> 19` residual bank, integral triangular
parent, completed ticket, resident word, or compiler is claimed.

## 0. Verdict

The scalar four-sector recurrence does not merely fail to prove a small
socket bound.  On its standard **indivisible-piece** face it has a large
structural Hall cut.

Let `B_+` be the class-`B` parent chains of length at least two.  Every
residual piece `R_C` with `C in B_+` starts without either new coordinate
and ends with both.  Such a `0 -> xy` piece cannot share a monotone child
path with another `0 -> xy` piece.  It also cannot enter a `0`, `x`, or `y`
root, or an unsplit mixed root.  After all alternative gaps on one root are
collapsed to their single path-capacity slot, its projected successor
neighbourhood has capacity at most

\[
                         d+d'.                         \tag{0.1}
\]

The first `d` slots are the `xy` copies of the `d` top-free parent
addresses; the last `d'` are the declared child boundary roots.  Product
state and protected-resource rows can only delete these projected options.

For an integral triangular parent, put

\[
 W={2m-1\choose m},\qquad c=\operatorname {Cat}_m,
 \qquad \Lambda=4^{m-1}-1,
 \qquad \sigma=dW+\binom{d+1}{2}-\Lambda,              \tag{0.2}
\]

and let `gamma=|C|` be the number of top-free parent chains containing a
rank-`(m-2)` target.  Then

\[
 |B_+|\ge
 \max\left\{0,
 c+\gamma-\left\lfloor{\sigma\over d-1}\right\rfloor
 \right\}.                                             \tag{0.3}
\]

Consequently the capacity-correct endpoint projection and the exact lifted
chain-column optimum obey

\[
 \boxed{
 \underline\kappa_{\rm sock}\ge
 \left[
 c+\gamma-\left\lfloor{\sigma\over d-1}\right\rfloor
       -d-d'
 \right]_+,
 \qquad
 \kappa_{\rm sock}^*\ge\underline\kappa_{\rm sock}.}  \tag{0.4}
\]

At the current scalar calibration `m=9`,

\[
 W=24310,\quad c=4862,\quad d=d'=3,\quad\sigma=7401,
                                                               \tag{0.5}
\]

and `0<=gamma<=3`.  Thus

\[
 |B_+|\ge1162+\gamma,
 \qquad
 \boxed{\underline\kappa_{\rm sock}\ge1156+\gamma\ge1156.}
                                                               \tag{0.6}
\]

If a completed ticket carries at most `Ld=3L` independent physical
sockets, the standard whole-piece lift therefore needs

\[
                         H_{\rm res}\ge
             \left\lceil{1156\over3L}\right\rceil.     \tag{0.7}
\]

This is not a frozen-instance numerical replay.  The local repository
authenticates (0.5), but it contains no integral `m=9` triangular parent and
therefore no literal `4874`-piece endpoint/state bank.  Formula (0.6) is an
unconditional implication **if such a standard parent is supplied**.  It
must not be reported as an authenticated counterexample or as the exact
value of `kappa_sock^*` for the current `final2754` factor.

There is nevertheless an all-parameter architectural consequence.  At
every deadline jump `d'=d+1`, the exact jump criterion gives

\[
 4\sigma<dc+3\binom{d+1}{2}+3.                        \tag{0.8}
\]

Combining (0.3)--(0.4) with (0.8) gives

\[
 \underline\kappa_{\rm sock}
   \ge {3d-4\over4(d-1)}c-O(d).                       \tag{0.9}
\]

Since `d` has infinitely many jumps and `c/d -> infinity`, an
all-dimensional standard indivisible-piece construction, if it supplied an
integral parent at every step, could not have
`kappa_sock^*=O(d)`.  This conclusion is conditional on those integral
parents; it is a no-go for that proposed recurrence interface, not a proof
that the presently open parents exist.

The dominant necessary expansion cut is now sharp.  Before endpoint matching, a
new recurrence must split/recut/macro-absorb almost all class-`B`
`0 -> xy` transitions, or plant a comparably large bank of new independent
internal receiver slots, and must return the complete capacity, cap-debt,
bi-history, exterior-`J`, topology, voltage, and star state.  If `a_B`
mixed pieces are absorbed internally and `r_B` genuinely new internal
receiver slots are made available to the others, a necessary current-step
row is

\[
 a_B+r_B\ge |B_+|-(d+d')-LdH_0;                       \tag{0.10}
\]

in particular `a_B+r_B>=1156-3LH_0` at `m=9`.  On the
no-new-receiver face `r_B=0`, this is the original absorption bound.  Raw
central ticket abundance implies neither term.  The exact projected
expansion hypothesis is the full capacity-Hall family in Section 5, and
full acceptance additionally needs the lifted chain/supercolumn rows.

## 1. Integral parent and four-sector classes

Assume the antecedent of the odd triangular recurrence: `W` anchored
chains of capacity `d` and `d` boundary addresses of capacities
`1,...,d` partition every nonempty old target of rank at most `m-1`.
Every anchored chain ends at a distinct rank-`(m-1)` target.

The four classes satisfy

\[
 |A|+|B|=W,\qquad |A|+|C|=W-c,\qquad |C|+|D|=d.       \tag{1.1}
\]

Writing `gamma=|C|` gives

\[
 |A|=W-c-\gamma,\qquad |B|=c+\gamma,
 \qquad |D|=d-\gamma.                                 \tag{1.2}
\]

Class `A` contains ranks `m-1,m-2`; class `B` contains rank `m-1` but not
rank `m-2`; class `C` is top-free and contains rank `m-2`; class `D`
contains neither.

Let `B_+` be the members of `B` whose selected parent chain has length at
least two, and put `n_B=|B_+|`.

## 2. The rank-capacity lower bound

### Theorem 2.1 (forced nontrivial class-`B` population)

For `d>=2`, equation (0.3) holds.

#### Proof

The number of old targets in ranks at most `m-3` is

\[
 L=\Lambda-W-(W-c)=\Lambda-2W+c.                     \tag{2.1}
\]

An `A` chain has already spent two positions on its rank-`(m-1)` and
rank-`(m-2)` targets, so it contains at most `d-2` members counted by
`L`.  A nontrivial `B` chain contains at most `d-1` such members, while a
singleton `B` chain contains none.  The boundary addresses have total
capacity

\[
 \tau_d=1+\cdots+d=\binom{d+1}{2};                    \tag{2.2}
\]

their `gamma` class-`C` rank-`(m-2)` targets leave at most
`tau_d-gamma` positions for (2.1).  Therefore

\[
 L\le(d-2)(W-c-\gamma)+(d-1)n_B+\tau_d-\gamma.        \tag{2.3}
\]

Using `Lambda=dW+tau_d-sigma`, rearrangement gives

\[
 (d-1)n_B\ge(d-1)(c+\gamma)-\sigma.                  \tag{2.4}
\]

Taking the nonnegative integer ceiling proves

\[
 n_B\ge
 \max\left\{0,c+\gamma-\left\lfloor{\sigma\over d-1}\right\rfloor
 \right\}.\qquad\square
\]

For `m=9`, ranks `1,...,6` contain

\[
 17+136+680+2380+6188+12376=21777                   \tag{2.5}
\]

targets.  Here `|A|=19448-gamma`, the three boundary capacities total six,
and (2.3) specializes to

\[
 21777\le(19448-\gamma)+2n_B+(6-\gamma),              \tag{2.6}
\]

so `n_B>=1162+gamma` directly.

## 3. The mixed-tag capacity cut

For a top-containing parent chain

\[
 C=(S_1\subsetneq\cdots\subsetneq S_\ell=A),          \tag{3.1}
\]

the fourth four-sector piece is

\[
 R_C=(S_1,S_1+xy,\ldots,S_{\ell-1}+xy).               \tag{3.2}
\]

If `C in B_+`, then `ell>=2`, so

\[
 x,y\notin\min R_C,qquad x,y\in\max R_C.             \tag{3.3}
\]

Call (3.3) a **mixed transition**.

The endpoint projection used below is capacity-correct.  Different
possible gaps on one child root are alternative placements sharing one
root-path capacity; they are not cloned into independent right-shore
sockets.  Equivalently, use a capacitated bipartite graph or expand each
root only into its genuine number of independent path slots.

### Lemma 3.1 (one mixed transition per monotone path)

An increasing child chain contains at most one whole piece `R_C` with
`C in B_+`.

#### Proof

Suppose two distinct mixed pieces have untagged minima `S` and `T`.  They
are distinct old targets because the parent chains partition the old ideal.
If one child chain contained both pieces, it would contain both `S` and
`T`, so they would be comparable; swap their names so that
\(S\subsetneq T\).  The same child chain would also contain the first tagged
member \(S+xy\).  But \(S+xy\) is incomparable with `T`: it has `x,y`, which
`T` omits, while \(T-S\) is nonempty.  This contradicts the child chain being
totally ordered. \(\square\)

### Lemma 3.2 (the only projected receiving capacity)

In the standard whole-piece four-sector bank, the total successor/root
capacity adjacent to `B_+` is at most `d+d'`.

#### Proof

The maximum in (3.3) cannot lie below the entry of a `0`, `x`, or `y`
piece because that entry omits at least one of the two new coordinates.

An `A`-type mixed top root has one initial gap

\[
                         T_1<T_1+xy.                   \tag{3.4}
\]

Inserting `R_C` whole into this gap would require

\[
 T_1\subseteq S_1\subseteq S_{\ell-1}\subseteq T_1,   \tag{3.5}
\]

after deleting `x,y`.  Hence equality holds throughout, placing the same
old target in two distinct parent chains, contrary to the parent
partition.  Before (3.4) the successor is untagged, and after (3.4) the
predecessor already contains `x,y`; either case is incompatible with
(3.3).  The same argument excludes insertion into another unsplit mixed
piece.

The only inherited pieces whose entry can receive a mixed maximum without
an earlier tagged predecessor are the `xy` copies of the top-free parent
chains.  There are at most `d` of them, including both class `C` top roots
and class `D` residual adapters.  Each is one chain-capacity slot even if
several literal gaps are feasible; empty top-free copies are deleted and
only lower this count.  The construction additionally declares only `d'`
independent boundary-root slots.  The newborn `{x}` and `{y}` pieces omit a
required tag, while `{x,y}` cannot contain
\(\max R_C=S_{\ell-1}+xy\) because \(S_{\ell-1}\) is a nonempty old target.  Thus
the three newborns add no receiving capacity even if tested rather than
kept as separate insertion obligations.  These are all neighbours in the
standard endpoint bank, proving the bound. \(\square\)

### Theorem 3.3 (mixed-tag Hall cut)

Equations (0.4) and (0.6) hold.

#### Proof

Take the left set `X=B_+` in the capacity form of Hall's theorem.  Lemma
3.2 gives `cap(N(X))<=d+d'`, and hence

\[
 |X|-\operatorname {cap}N(X)\ge n_B-d-d'.             \tag{3.6}
\]

The maximum capacity deficiency is the least number of exterior unit
sockets in the endpoint projection.  Theorem 2.1 proves (0.4).  At `m=9`,
substitution gives

\[
 1162+\gamma-3-3=1156+\gamma.                         \tag{3.7}
\]

Every exact lifted chain cover projects to this endpoint assignment, so
forgetting capacity/product-state rows proves
`kappa_sock^*>=underline kappa_sock`. \(\square\)

This is already a negative Farkas/Hall certificate on the scalar-free
endpoint face.  Cap, history, topology, voltage, protected-resource, or
fixed-`z` acceptance cannot repair it without changing the column family.

## 4. Deadline jumps exclude a uniform whole-piece bound

### Theorem 4.1 (conditional regenerative no-go)

Suppose the standard indivisible four-sector architecture supplies an
integral triangular parent at every sufficiently large parameter.  Then
`kappa_sock^*` is not `O(d)`.

#### Proof

The scalar theorem gives `d'-d in {0,1}` and `d=Theta(sqrt(m))`, so `d`
has infinitely many jump indices.  At a jump, the negation of the plateau
criterion is (0.8).  From Theorem 2.1,

\[
 n_B>
 c+\gamma-{dc+3\tau_d+3\over4(d-1)}.                 \tag{4.1}
\]

Theorem 3.3 and `d'=d+1` then give

\[
 \underline\kappa_{\rm sock}>
 {3d-4\over4(d-1)}c
 -{3\tau_d+3\over4(d-1)}-2d-1.                       \tag{4.2}
\]

The coefficient of `c` is at least `1/2` for `d>=2`, while the remaining
terms are `O(d)`.  Catalan growth gives `c/d -> infinity`.  Hence the ratio
`underline kappa_sock/d`, and therefore `kappa_sock^*/d`, is unbounded on
the jump subsequence. \(\square\)

The antecedent is deliberately the proposed all-dimensional standard
construction.  The theorem does not manufacture the integral parents whose
existence is open.

## 5. Exact expansion needed to escape

Let an enlarged recurrence internally absorb `a_B` members of `B_+` before
forming its exterior-socket endpoint problem.  An absorption may split
(3.2) at its `0 -> xy` transition, recut and interleave its two sides with
tag-homogeneous pieces, or use a matching-closed compound macro.  Merely
renaming several mixed pieces as one task is not absorption: their
independent path capacities remain visible in the cut.  Separately, let
`r_B` be the total capacity of genuinely new internal receiving slots
adjacent to the unabsorbed mixed pieces, beyond the standard `d+d'` bank.

Applying Theorem 3.3 to the unabsorbed pieces gives

\[
 \underline\kappa_{\rm sock}\ge
                         n_B-a_B-r_B-d-d'.             \tag{5.1}
\]

Thus `kappa_sock^*<=LdH_0` requires (0.10).  A proof-safe absorber or new
receiver bank must also emit accepted lifted columns whose ordered products
return

\[
 (\text{owner/boundary capacity};z,\beta;
   \mathcal R^+,\mathcal R^-;J;\text{topology};
   \text{voltage};\text{star};\text{protected resources}).   \tag{5.2}
\]

Endpoint splitting or extra receiver capacity without (5.2) proves only a
scalar Hall repair.  It does not prove full acceptance.

More exactly, let \(A_B\subseteq B_+\) be the absorbed mixed pieces, let
`N_0` be the standard capacity-collapsed successor relation, and let `N_U`
be the relation to newly planted internal receivers.  The exact projected
mixed-sector condition is

\[
 |X|-\operatorname {cap}N_0(X)-\operatorname {cap}N_U(X)
       \le LdH_0
       \qquad(X\subseteq B_+\setminus A_B).            \tag{5.3}
\]

The coarse choice `X=B_+\setminus A_B` yields (0.10); it is not sufficient
for all smaller shores.  The complete endpoint projection must impose the
analogous cut for every subset of every unabsorbed residual piece, not only
the mixed sector.

A balanced duplicate-cap backup counts toward `r_B` only when it exposes an
occurrence-labelled successor/root slot adjacent to the relevant piece and
has one genuinely independent path-capacity unit.  Duplicate cap
multiplicity or zero cap current alone supplies no receiver.  Its column
must still pass (5.2), including both boundary histories and topology.  On
the endpoint face, (5.3) plus the all-piece cuts is exact by capacitated
Hall/max flow; on the lifted face it remains only a projection of the
chain-column and replayed-supercolumn integer program.

## 6. Relation to the fixed-`z` completed-ticket atlas

At sufficiently large parameters satisfying its stated bank-separation
inequalities, the fixed-`z` two-bank collar theorem supplies a prospective
local subatlas for one already rooted task: `Theta(k^7)` central/collar
choices, `O(d)` support, and `O(k^6)` load on every nonprivate local
resource.  Calling these **completed tickets** still requires that theorem's
one-cycle exposure and exterior-acceptance hypotheses.  It does **not**
currently provide:

1. a binding from a ticket to literal `k=17 -> 19` residual-piece and root
   IDs;
2. the absorption/new-receiver count (0.10);
3. exterior far-socket acceptance and old-seam exposure;
4. total sidecar displacement, deep upper, source/compiler, aperture, and
   child-native voltage return; or
5. exact replay of a union of several selected tickets.

Its explicit two-disjoint-bank sufficient construction is asymptotic and is
not instantiated at the current dimensions.  For the natural central ranks,
`(k,r,d)=(17,9,3)` gives `(k-r-2d)_4=(2)_4=0`, and the child
`(19,10,3)` gives `(3)_4=0`.  Thus even the local two-bank completed-collar
subatlas supplies no current `k=17 -> 19` column; only its general interface
and future large-parameter load theorem are being used here.

Accordingly the atlas is a candidate service family **after** a mixed-tag
absorber or internal receiver expansion has reduced the socket cut.  Its polynomial abundance cannot
change (0.6): many choices for one local ticket are not one internal path
for many independent mixed pieces.  Even after a projected matching is
found, full acceptance still requires a replayed supercolumn or a prepared
commuting subatlas.  Scalar Hall projection and full acceptance remain
strictly different gates.

## 7. Frozen `k=17 -> 19` provenance audit

The authenticated scalar row is:

\[
\begin{array}{c|r}
 W&24310\\
 \Lambda&65535\\
 d&3\\
 \sigma&7401\\
 c&4862\\
 W'&92378\\
 d'&3\\
 \sigma'&14997\\
 W'+d'&92381\\
 c+4d&4874\\
 c+4d-d'&4871\\
 d(c+4d)+3&14625.
\end{array}                                             \tag{7.1}
\]

Only the class parameter is known:

\[
 \gamma\in\{0,1,2,3\},\qquad
 |A|=19448-\gamma,\quad |B|=4862+\gamma,
 \quad |D|=3-\gamma.                                  \tag{7.2}
\]

No frozen file fixes `gamma`, the chain lengths, or a single residual
endpoint.  In particular the repository lacks:

* an integral `m=9` triangular parent partition of the `65535` old targets;
* the selected matching `mu` and literal `Q_C^0,Q_C^x,Q_C^y,R_C` rows;
* occurrence-labelled successor, gap, top, and boundary ports;
* a capacity-correct residual endpoint graph or Hall witness;
* the three newborn insertion addresses and a child baseline chronology;
* chain columns carrying (5.2); and
* fixed-`z` completed tickets bound to those columns with exact union
  replay.

The nearby authenticated artifacts are type-incompatible.

* `scratch/ad_k17_k15_four_sector_factor_20260731.json` is a
  `K15 -> K17` middle-layer Johnson two-factor, not a lower-ideal
  triangular parent.
* `final2754.factor.tsv` contains only lower colour, two rank-nine owners,
  cap, and protection fields.  It assigns none of the other `41225` strict
  lower targets to triangular addresses and has no `K19` annotation.
* The `m=9` rotation forest authenticates `4862` topological components on
  ground 18, but explicitly carries no depth-three lower-chain addresses,
  source chronology, exterior tickets, or compiler cells.
* Files whose names contain `k17_m9_residual19` concern nineteen residual
  rank-ten masks inside `k=17`; `19` is a count, not the child dimension.

Therefore no exact max-flow or product-state run is proof-safe yet.  A
program could only invent the absent bank.  The first executable artifact
must materialize and audit the integral parent and literal residual
piece/port table.  Once that exists, the set `B_+` and its capacity-collapsed
neighbourhood give a direct checkable Hall certificate before the full
chain-column solver is invoked.

### 7.1 Fail-closed exact auditor contract

The eventual auditor has three strictly separated stages.

1. **Derive and validate the bank.**  Read `24310` anchored parent rows and
   three boundary rows, verify their capacities and disjoint exact cover of
   all `65535` old targets, verify the rank-eight anchors and `mu`, and
   derive the four child pieces itself.  It must not trust supplied
   `A/B/C/D`, endpoint, or tag fields without replay.
2. **Projected max flow.**  Create one left unit for every nonempty residual
   piece and one right unit for every successor copy or independent root
   path slot.  Alternative literal gaps on one slot share its capacity
   vertex.  The network

   \[
     s\longrightarrow\mathcal P^-
       \longrightarrow V^+
       \longrightarrow t                             \tag{7.3}
   \]

   has unit piece arcs and the declared slot capacities.  If its value is
   `nu`, the projected deficiency is `|P|-nu`; the reachable shore of the
   final residual network is an exact min-cut/Hall witness.  The auditor
   must separately emit the `B_+` cut of Theorem 3.3.
3. **Lifted product state.**  Enumerate only capacity-valid acyclic chain
   columns, composing `z,beta,R^+,R^-` in order and replaying `J`, topology,
   voltage, star, and protected resources.  Cover every residual piece
   exactly once with accepted columns and then replay the selected ticket
   union as one supercolumn.  This last set-partition problem is not in
   general a min-cost circulation or a totally-unimodular flow.  A projected
   max-flow witness is therefore never labelled full acceptance.

The program must fail closed if any parent target, piece endpoint, capacity
slot, state transition, resource occurrence, or replay row is absent.  This
contract explains why compiling an `O3` flow program against the current
scalar JSON would not be an audit: stages 1 and 3 have no input.

There is likewise no smaller **authenticated residual-bank** counterexample
to report from the frozen corpus.  The solver-free `k=5,d=2` all-high audit
authenticates a two-cycle/private-socket closure obstruction, and the
decorated `m=2` trace authenticates a port-Hall obstruction, but neither is
an instantiated triangular residual bank and neither disproves an `O(d)`
socket bound.  They remain correctly scoped warnings only.  The mixed-tag
theorem above is stronger but conditional on the missing integral-parent
antecedent.

## 8. Reproducibility and scope

Frozen input hashes at the time of this note are recorded in
`scratch/k17_k19_compound_socket_provenance_and_mixed_tag_20260802.audit.json`.
The scalar theorem and audit establish (7.1).  The fractional triangular
theorem and the exchange/contraction theorem both explicitly leave integral
rounding open.

No SSH, finite search, Python search, GPU, SAT solve, or H100 computation was
used.  No claim is made that `final2754` is resident, that a `k=19` child
exists, that the fixed-`z` exterior gate accepts, or that a word/compiler has
been constructed.
