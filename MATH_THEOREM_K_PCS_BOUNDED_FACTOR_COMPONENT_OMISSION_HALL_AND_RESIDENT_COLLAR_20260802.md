# `PCS` Row 2: bounded factors, component-omission Hall, and the resident pivot collar

**Date:** 2026-08-02  
**Lane:** K, Protected Catalan--pivot / simultaneous Row-2 host  
**Status:** exact factor-first equivalence and an unconditional protected-factor
start.  No all-parameter upper-covering factor, globally resident chronology,
deeper-shadow, compiler, or regeneration theorem is claimed.

## 0. Verdict

Put

\[
 \Omega=[2m-1],\qquad
 \mathcal L={\Omega\choose m-1},\quad
 \mathcal V={\Omega\choose m},\quad
 \mathcal U={\Omega\choose m+1},
\]

\[
 W=|\mathcal L|=|\mathcal V|,\qquad
 U=|\mathcal U|,\qquad
 C=W-U=\operatorname {Cat}_m.                         \tag{0.1}
\]

There is a necessary syntax correction to any simultaneous theorem.
An upper-exact rooted Catalan **forest** has `U` edges on `W` rooted
vertices, and therefore has exactly

\[
                              W-U=C                     \tag{0.2}
\]

components.  Hence its own component count cannot be bounded independently
of `m`.  The bounded object must instead be an ambient turn factor (or the
factor obtained after transparent pulls) which contains the Catalan forest.

On that corrected face, the exact remaining extraction obstruction is a
small capacitated Hall system on **factor components versus repeat colours**.
Let `F` be a full-immediate-upper spanning turn factor containing the
protected pivot collar.  Some turns may be declared ineligible for the full
task shore.  Delete every ineligible turn, and for each upper task `R` delete
all but one of its eligible occurrences.  The retained turns are the desired
upper-exact Catalan forest precisely when those deletions meet every factor
cycle.

This is equivalent to the cut system

\[
 \boxed{
 |X|\le
 \sum_{R:\,N_R\cap X\ne\varnothing}(\lambda_R-1)
 \qquad(X\subseteq\mathcal K_0),}                     \tag{0.3}
\]

where `mathcal K_0` consists of factor components not already hit by an
ineligible turn, `lambda_R` is the eligible multiplicity of task `R`, and
`N_R` is the set of components containing an unprotected eligible
occurrence of `R`.  Formula (0.3) is necessary and sufficient, not a scalar
surplus estimate.

Consequences:

* for a one-cycle upper-covering factor, (0.3) is automatic;
* for a factor with at most `s` components, it is an exact finite interface
  of at most `2^s-1` cuts;
* a capacity-respecting assignment of a repeated colour to every component
  is a simple sufficient certificate; and
* upper coverage plus `c(F)<=C` is not sufficient: repeat surplus can be
  trapped away from one factor component.

The sharp pivot incidence path embeds in some spanning two-factor whenever
`6d<=m-2`.  This unconditionally preserves its internal depth-`d`
residence.  It does not make that factor upper-covering, bound its component
count, or accept the two exterior collar-run states.  Thus the smallest
remaining all-`m` statement is an upper-covering bounded-factor theorem with
(0.3) and two literal residence-boundary guards.  It is strictly smaller
than `PCS(m,d)`.

The authenticated K17 trajectory is positive evidence for compatibility,
not a proof of that statement.  One guarded augmented factor has full
`19,448/19,448` opened immediate-upper coverage, and a protected
strict/neutral packet walk reduces the opened residence debt from `5,588`
to an independently replayed `2,018` without losing that row.
The final debt is nonzero and the object has an exceptional `h=1` lollipop
degree pattern, so it is not silently promoted to the ordinary turn-factor
theorem below.

## 1. Turn factors and the protected collar

Fix a spanning Middle Levels two-factor

\[
                        F=M_0\mathbin{\dot\cup}M_1,    \tag{1.1}
\]

where `M_0,M_1` are its alternating perfect matchings.  Orient every factor
component so `M_0` is the predecessor phase.  Suppressing each lower root
turns `M_1` into a directed cycle cover on the `W` rooted vertices.  Denote
its component set by `mathcal K`.

At each lower root `L`, its two incident owners determine one Johnson turn
`e_L`; its immediate-upper value is their union.  To include literal
boundary/`D` restrictions, assign to every turn either one eligible task
label

\[
                         u(e_L)\in\mathcal U            \tag{1.2}
\]

or the ineligible symbol `bot`.  Put

\[
 \lambda_R=|\{e:u(e)=R\}|,
 \qquad q=|\{e:u(e)=\bot\}|.                           \tag{1.3}
\]

The factor is **full-shore upper-covering** when

\[
                         \lambda_R\ge1
                         \qquad(R\in\mathcal U).       \tag{1.4}
\]

Counting the eligible occurrences gives the exact repeat identity

\[
       \sum_{R\in\mathcal U}(\lambda_R-1)
       =(W-q)-U=C-q.                                   \tag{1.5}
\]

Let `P` be the `3d`-turn pivot successor path.  Its turns have pairwise
distinct upper labels.  We require

\[
              P\subseteq M_1,qquad u(e)\ne\bot\ (e\in P),          \tag{1.6}
\]

and require its predecessor incidences to lie in `M_0`.  This is the
phase-aligned protected collar.

If accepted collar residence uses exterior factor turns (at most the bounded
prefix/suffix history needed by its two interfaces), include all such literal
turn occurrences in a protected closure `P_*`.  Require

\[
 P\subseteq P_*\subseteq M_1,qquad
 P_*\text{ is a rooted forest},qquad
 u|_{P_*}\text{ is injective and eligible}.            \tag{1.6a}
\]

Any load-bearing boundary source occurrence which is not a turn is frozen
separately.  The purpose of `P_*` is to ensure that the later Catalan-forest
marking does not delete a turn needed by the residence certificate.  When
only internal collar residence is asserted, take `P_*=P`.

The literal pivot theorem gives every nonclipped positive coordinate run
inside `P` length at least `d+1`.  Completing `P` to `F` cannot change an
internal pivot turn.  It can, however, close a clipped endpoint run through
the exterior factor.  Therefore distinguish:

1. **internal collar residence**, which follows from (1.6); and
2. **accepted collar residence**, which additionally requires the two
   exported capped prefix/suffix run states to accept the two exterior
   neighbours supplied by `F`.

Only the second statement makes the collar resident in the complete factor
chronology.  It is a finite two-boundary predicate, not a consequence of
upper coverage.

### Proposition 1.1 (unconditional protected-factor start)

If

\[
                              6d\le m-2,                \tag{1.7}
\]

the complete incidence lift of the pivot collar is contained in a spanning
Middle Levels two-factor.  The factor retains the phase-aligned pivot and
its internal depth-`d` residence.

#### Proof

The pivot has `3d` Johnson turns, hence its alternating incidence lift is a
maximum-degree-two path with `6d` incidence edges.  The small
protected-factor theorem extends every maximum-degree-two protected
subgraph having at most `m-2` edges to a spanning two-factor.  Apply it to
this lift.  Every internal pivot vertex already has degree two, so the
completion cannot alter the collar internally.  The explicit pivot run
calculation therefore survives.  No claim about its two exterior run states
is made.  \(\square\)

Proposition 1.1 supplies neither (1.4) nor a useful bound on
`|mathcal K|`.  The generic component estimate is only `|mathcal K|<=W/3`,
because a simple Middle Levels factor component has at least six incidence
vertices.

## 2. The component-omission graph

Assume (1.4)--(1.6a).  For every upper task put

\[
                              b_R=\lambda_R-1.          \tag{2.1}
\]

Thus `b_R` is the exact number of eligible occurrences of `R` which must be
deleted if one occurrence is to remain.

Write

\[
                             \mathcal T(F)=M_1          \tag{2.1a}
\]

for the rooted **turn set** of the oriented factor.  All selections and
deletions below take place in `mathcal T(F)`, not in the full incidence set
`M_0 dotunion M_1`; deleting a predecessor incidence would change the fixed
rooting and is outside this theorem.

Every ineligible turn must also be deleted.  Let

\[
 \mathcal K_0=\{K\in\mathcal K:
                   K\text{ contains no ineligible turn}\}.          \tag{2.2}
\]

The other factor components are already broken by the forced deletion.

For `R\in\mathcal U`, define

\[
 N_R=\{K\in\mathcal K_0:
       K\text{ contains an occurrence of }R\text{ outside }P_*\}.   \tag{2.3}
\]

An occurrence in `P_*` is not deletable.  Since its upper labels are
distinct, each task has at most one protected occurrence.  Consequently
there are always at least `b_R` deletable occurrences of `R`: there are
exactly `b_R` if its protected occurrence is present, and `b_R+1`
otherwise.

Make a bipartite multicapacity graph with left shore `mathcal K_0`, right
shore the tasks, adjacency `K--R` iff `K in N_R`, unit demand at every
component, and capacity `b_R` at task `R`.

## 3. Exact omission Hall theorem

### Theorem 3.1 (component-omission Hall)

For a full-shore upper-covering protected factor `F`, the following are
equivalent.

1. There is a set `Q_0` of turns such that
   * `P_*\subseteq Q_0`;
   * `Q_0` contains exactly one eligible occurrence of every
     `R\in\mathcal U`;
   * `Q_0` contains no ineligible turn; and
   * the rooted graph `Q_0` is a forest.
2. There is a deletion set `Z\subseteq \mathcal T(F)-P_*` such that
   * every ineligible turn lies in `Z`;
   * `|Z\cap u^{-1}(R)|=b_R` for every `R`; and
   * `Z` meets every factor component.
3. The capacitated component--task graph satisfies
   \[
    |X|\le
    \sum_{R:\,N_R\cap X\ne\varnothing} b_R
                 \qquad(X\subseteq\mathcal K_0).       \tag{3.1}
   \]

Whenever these conditions hold, every resulting `Q_0` is an upper-exact
rooted Catalan forest containing the complete protected closure `P_*`, and it has
exactly `C` directed-path components.

#### Proof

Items 1 and 2 are complements inside the rooted turn shore: take
`Z=\mathcal T(F)-Q_0`.  Exact upper
representation forces deletion of all ineligible turns and exactly
`lambda_R-1=b_R` eligible occurrences of each task.  A subset of a directed
cycle cover is acyclic if and only if at least one edge is deleted from
every cycle.  Hence the last clauses are equivalent.

It remains to prove Items 2 and 3 equivalent.  Components outside
`mathcal K_0` are already hit by an ineligible turn.  For every component
in `mathcal K_0`, designate one deletable eligible occurrence which will
break it.  A task `R` can supply at most `b_R` such designated deletions,
and it can supply one to `K` exactly when `K in N_R`.  This is a bipartite
`b`-matching which saturates the component shore.  The capacitated Hall
theorem gives exactly (3.1).

After choosing the designated deletions, extend them task by task to
exactly `b_R` deletions.  This is always possible: as observed after (2.3),
task `R` has at least `b_R` unprotected occurrences in total.  There is no
upper capacity on the number of additional deletions in one component.
This gives `Z`.  Conversely, choosing one member of `Z` from every
previously unhit component gives the saturating `b`-matching and hence
(3.1).

Finally `Q_0` has exactly `U` edges on all `W` rooted vertices and is a
forest of maximum indegree and outdegree one.  It therefore has
`W-U=C` directed-path components.  \(\square\)

### Corollary 3.2 (one-cycle factor)

If `F` has one component, is full-shore upper-covering, and contains a
protected closure `P_*` satisfying (1.6a), then `Q_0` exists.

#### Proof

If an ineligible turn exists, its forced deletion breaks the cycle.  If all
turns are eligible, (1.5) gives total repeat supply `C>=1`.  Therefore the
only nonempty Hall shore `X={K}` satisfies (3.1).  Apply Theorem 3.1.
Equivalently, choose the protected occurrence for every colour represented
in `P_*` and
one occurrence of every other colour; the resulting `U<W` turns are a
proper subset of the one cycle and hence a forest.  \(\square\)

### Corollary 3.3 (bounded-component finite interface)

If `F` has at most `s` components, extraction of the upper-exact protected
Catalan forest is decided by at most `2^s-1` inequalities (3.1).  A simple
sufficient certificate is a matching which assigns to every component in
`mathcal K_0` a repeated task occurring there outside `P_*`, using task `R`
at most `b_R` times.

This is the exact sense in which bounded component count gives a bounded
Row-2 state.  The Catalan forest itself still has `C` components by (0.2).

## 4. Transparent pulls and the simultaneous host theorem

A strict one-phase pull changes only the nonpredecessor factor phase.  Call
it **task-transparent** when it preserves the complete eligible task
multiplicity vector, including the ineligible marker, and **collar-safe**
when its complete support is disjoint from `P_*` and from every nonturn
literal boundary-state occurrence certifying accepted collar residence.

### Theorem 4.1 (bounded-factor simultaneous Row-2 host)

Suppose, for some `s`, there is a spanning factor `F` such that

1. `F` contains a protected closure `P_*` satisfying (1.6a);
2. the collar's two exterior run states accept, so it is resident in `F`;
3. `F` is full-shore upper-covering;
4. `|mathcal K(F)|<=s`; and
5. the component-omission inequalities (3.1) hold.

Then `F` contains an upper-exact rooted Catalan forest `Q_0` containing
`P_*`.  In particular the same tuple retains the protected depth-`d`
resident collar: its load-bearing turn guards occur in `Q_0`, and any
nonturn boundary occurrences remain frozen in `F`.  The ambient carrier has
at most `s` components and `Q_0` has exactly `C` components.

Alternatively, condition 4--5 may be replaced by a pairwise
incidence-disjoint, collar-safe, task-transparent strict pull incidence tree
which merges `F` to one factor cycle.  The same conclusion then follows
from Corollary 3.2.

#### Proof

Under conditions 1--5 apply Theorem 3.1.  Selecting `Q_0` only marks turns
already present in `F`; it does not change the physical factor chronology or
either protected boundary state.  Hence the collar certificate survives.

For the alternative, process the strict pull incidence tree from its leaves.
Every pull merges distinct current cycles, preserves the entire task
multiplicity vector, and leaves the collar and its guards unchanged.  One
upper-covering factor cycle remains.  Apply Corollary 3.2.  \(\square\)

The theorem is simultaneous at the owner/immediate-upper/local-residence
level.  It does not order the `C` Catalan components as a physical source,
identify their ordered `d`-letter histories, or prove residence away from the
protected collar.

## 5. Sharpness of the omission row

The scalar conditions

\[
                  |\mathcal K(F)|\le C,qquad
                  \sum_R b_R=C-q                         \tag{5.1}
\]

do not imply (3.1).  The obstruction is localization, not total supply.

For an abstract sharp example, take one directed three-cycle with labels
`a,b,c` and one directed four-cycle with labels `d,d,d,e`.  There are seven
occurrences, five represented tasks, repeat excess `C=2`, and two factor
components.  Thus the full task shore is covered and `|mathcal K|=C`, but for the
singleton shore consisting of the first component the right side of (3.1)
is zero.  Every exact one-per-colour selection retains that whole first
cycle.

This example is a sharp obstruction to deriving component breaking from
global Catalan slack.  It is not asserted to be a Boolean nonexistence
example: Boolean structure may guarantee (3.1) for a prospectively chosen
factor, which is precisely the remaining positive theorem.

There is a second sharp separation.  Proposition 1.1 can embed the resident
pivot collar in a factor, but an explicit `m=4` factor in the repository
covers only `20/21` upper colours.  Thus protected-factor extension does not
imply condition 3 of Theorem 4.1.  Conversely, full upper coverage does not
certify either accepted collar boundary states or global residence.

## 6. Relation to the forward atlas and protected graphic--Rado

The protected forward-atlas theorem starts from a fixed predecessor matching
`M_0`.  It chooses a potential increasing along the pivot and retains every
forward rooted arc.  Every full upper-colour fibre contains a directed cycle,
so the atlas contains the pivot and at least one occurrence of every upper
colour.  This proves complete **occurrence availability**.

It does not prove a factor: several atlas arcs may share a rooted tail or
head, and choosing one occurrence per colour need not give a permutation.
Thus the forward atlas supplies the correct candidate ground for a
prospective construction of `M_1`, but it does not imply hypotheses 3--5 of
Theorem 4.1.

After a factor `F` has been selected, all tail and head capacities are fixed
once and for all.  The protected rooted-support Rado theorem then says that
one may choose one occurrence per upper task precisely when the duplicate
occurrences pay every rooted cycle activated by a colour family.  Theorem
3.1 is the exact component-side dual of that criterion for a cycle cover:
instead of testing every colour family, distribute the forced repeat
deletions so every factor cycle is hit.  For `|mathcal K(F)|<=s`, the whole
graphic--Rado row therefore compresses to the `2^s-1` component cuts (3.1).

The general common-matroid forest theorem without a fixed factor does not
impose tail/head degree one and need not retain the pivot.  Conversely, a
transparent pull tree acts only after the factor exists.  These are three
successive quantifiers:

\[
 \text{forward occurrence atlas}
 \longrightarrow
 \text{balanced upper-covering factor}
 \longrightarrow
 \text{omission Hall / transparent pull}.             \tag{6.1}
\]

The unresolved Boolean step is the middle arrow together with bounded
components and the two collar boundary guards.

## 7. Complementary forest-first connector deficiency

The omission theorem extracts `Q_0`; it does not connect its `C` path
components.  There is nevertheless an exact order-free connector statement
on the **edge-separable port face** once the component states have been
fixed.  Here edge-separable means that a connector set is accepted exactly
when it is a port matching and every chosen connector passes its own listed
state predicate.  A nonlocal common-cap, global-address, or shared-witness
constraint belongs to this face only after a separate product/private-state
theorem proves that it factors in this way.

Let `mathcal C` be the `C` components of `Q_0`, with distinguished pivot
component `K_*`.  Choose an injective component potential `phi` with
`phi(K_*)` minimum.  Split every component into one outgoing and one incoming
port.  Let `G_phi` join `K_out` to `L_in` precisely when

1. `phi(K)<phi(L)`;
2. the free rooted ports form a legal Johnson connector; and
3. the declared **edge-local** history and protected-collar state accepts
   that connector.

Delete `K_*^in` from the right shore.  Put

\[
       \delta(G_\phi)=\max_{X\subseteq\mathcal C}
                         (|X|-|N_{G_\phi}(X)|).          \tag{7.1}
\]

### Proposition 7.1 (exact forward path-cover deficiency)

There is a state-compatible directed path cover of the components with at
most `b` paths, one beginning at `K_*`, if and only if

\[
                              \delta(G_\phi)\le b.       \tag{7.2}
\]

#### Proof

A matching of size `C-b` in `G_phi` uses every component as at most one
connector tail and at most one connector head.  Since every selected arc
strictly increases `phi`, the resulting component digraph has no directed
cycle.  It is therefore a path cover with `C-(C-b)=b` paths, and the deleted
right vertex forces `K_*` to have indegree zero.  Conversely, the connectors
of any such path cover form a matching of size at least `C-b` in `G_phi`.
The deficiency form of Hall's theorem says that the maximum matching size is
`C-delta(G_phi)`, proving (7.2).  \(\square\)

Proposition 7.1 is downstream of Theorem 3.1 and orthogonal to the bounded
ambient factor.  It proves no bound on `delta(G_phi)`: the state-compatible
port graph must still be constructed.  In particular, abstract free-port
containment does not imply its history/collar rows.  Nor does Proposition
7.1 discharge a nonseparable global address, witness, or common-cap row;
those rows remain outside the edge-local graph unless a product theorem has
first been supplied.

Since the right shore omits `K_*^in`, one always has
`delta(G_phi)>=1`.  Thus `delta(G_phi)=1` is exactly the one-path connector
criterion, while `delta(G_phi)<=b` is the exact bounded-`b` component
criterion after connector selection.  This is the forest-first counterpart
of the factor-first component budget in Theorem 4.1.

## 8. K17 calibration

The independently replayed full-immediate-upper model is

```text
/home/amodo/or15/work/root_k17_fullq1_ordinary_circulation_20260802/
    fullq1_13.best.model
SHA-256 e7ea3841cde04129e3b0af008da0ab2ca2deb8936f09ae22d43a9174ac888a31
```

Its ordinary diamonds cover all `19,448/19,448` rank-ten tasks, and both
licensed linear openings and cyclic seam palettes retain all
`19,448/19,448`.  The augmented incidence graph is connected; the ordinary
contracted turn support has two components.  It has the exceptional
`h=1` lollipop degree pattern (`M` has degree one and `D` degree three), so
it is not literally the ordinary two-perfect-matching factor of Section 1.
In particular, Theorem 3.1 is not applied to it without first extracting
and authenticating such a turn factor.

One independently frozen strict full-q1 descendant is

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
    checkpoint_fullq1_res2169/model
SHA-256 3107fc58bbf222bb5e00e6ff9ceb79d23623a156811591a033912f90ab29354d
```

It retains both opened `19,448/19,448` palettes and has opened profile

\[
       (\text{residence debt},h_{11},h_{12},h_{13})
                         =(2169,1516,267,4).             \tag{6.1}
\]

The short-run histogram is `(1361,808)` at lengths one and two.  This
authenticates a descent from `5,588` to `2,169` without immediate-upper
loss and shows that the upper row and substantial residence repair are
compatible in one finite state.  It does not give zero residence, an
ordinary factor satisfying (3.1), or an all-`m` construction.

A later strict-plus-neutral escape is independently replayed at

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
    checkpoint_fullq1_escape_res2018/model
SHA-256 c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d
independent audit SHA-256
    885f62c5b7689ada00970688a9771a5bcaa543657e3fae3d065aed3d1f41cb9d
```

It retains one augmented component, all `16,261` guards, and zero opened
rank-ten holes in both orientations.  Its opened length-`1,2` histograms are
`(1277,741)` and `(1276,742)`, so the best opened residence debt is `2,018`;
its deep-hole profile is `(1518,278,4)` at ranks `11,12,13`.  This strengthens
the finite compatibility evidence and still leaves every general existence
claim open.

The escape is state-relative and genuinely serial: one residence-neutral
`C6` bridge enables an ordered three-`C8` quench; all four strict prefixes
retain both opened q1 palettes, the guards, protected boundary, and augmented
connectivity.  The complete packet reuses two roots, so it is not a
root-disjoint batch and is not an instance of an a priori commuting pull
tree.  Its proof-safe interpretation here is evidence that transparent
preparation can unlock later residence descent, not a monotone or
all-dimensional termination theorem.  The frozen compound theorem is
`MATH_THEOREM_R2_K17_FULLQ1_COMPOUND_RESIDENCE_EXCHANGE_ORACLE_20260802.md`,
SHA-256
`9ffa6a7a374cfa04e564ab6fc5a76f0e6bcf277afa565f6f99b98380747f84c7`.

## 9. K17 lower named-target allocation is a closed static row

The independently audited theorem
`MATH_THEOREM_K17_THREE_LEVEL_NORMAL_CHAINIZATION_20260802.md` partitions
all `65,535` nonempty lower targets of ranks one through eight into exactly
`24,310` inclusion chains, each of size at most three and with exactly one
rank-eight top.  Its proof compresses ranks one through six to one level,
uses uniform containment couplings through ranks seven and eight, derives a
three-level LYM inequality, and applies Dilworth.

Consequently, for **any** perfect rank-eight--rank-nine incidence matching,
the chain at a rank-eight top can be assigned to its matched rank-nine
owner; all earlier members remain proper subsets of that owner.  The
authenticated K17 lollipop also has such a matching: the leaf forces
alternation along its entire tail and the residual even cycle then
alternates.

Thus, at the K17 depth `d=3`, equitable allocation of all named lower
targets is no longer a missing finite row.  The theorem is static: it does
not realize each chosen chain as the suffix states of one literal
chronology.  The remaining finite lower-side interface is the common
chronology/state-balance problem, still coupled to upper coverage and
residence.  Pivot addresses, common cap, and compiler extraction are also
not supplied.

The chainization theorem has SHA-256
`6fa4056052919edabd0914c8744b5dc137f2c8f9dff54ed313ecf0e58af57279`;
its independent audit
`MATH_AUDIT_K_K17_THREE_LEVEL_NORMAL_CHAINIZATION_20260802.md` has SHA-256
`bd42e50191df8353b19a51ed0a3de18ee573705ea7c975003eea208e9ffff47d`.
The abstract partition has also been materialized on the residence-2018
lollipop phase and replayed by an independent parser.  The frozen table

```text
scratch/k17_exact_depth3_owner_payload_table_20260802/
    k17_depth3_owner_payload.tsv
SHA-256 029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1
```

has `24,310` rows and chain-length histogram

\[
                     (n_1,n_2,n_3)=(1748,3899,18663).       \tag{9.1}
\]

The independent replay checks strict nesting, all `65,535` lower targets
exactly once, every rank-eight root and rank-nine owner exactly once, and
membership of all `24,310` root--owner assignments in the selected
`48,620`-incidence factor.  Its audit JSON has SHA-256
`b9a50eb60bf338e7750404a77be85fcb9aba15ef8676e53dc3d9b0ae75567e1c`.
Thus the static lower allocation is not merely existential: it coexists on
one frozen incidence phase with the K17 full-q1/residence-2018 calibration.
It still does not turn the assigned chains into literal suffix histories,
so no chronology, state balance, residence, upper, or compiler implication
is drawn from this coexistence.

The first literal chronology face is now exactly closed negatively.  In the
old canonical payload-transparent depth-three hinge, every head state has
rank-eight union, while every tail belonging to a chain of length one or two
has the rank-nine owner as its union.  Any K17 partition into chains of
length at most three has slot deficit

\[
          3(24310)-65535=7395
\]

and hence at least `ceil(7395/2)=3698` such short roles.  Therefore no table
on this old hinge face can balance.  On the frozen table the independently
replayed compatibility matching is exactly `1/24310`; the unique edge is
one-way between two different roles, so there is no nonempty balanced
canonical subcollection.  Allowing every filler singleton or every
right-aligned guard/filler unsaturated hinge still leaves matching one.

The first tested effective enrichment splits the last marked layer across
two terminal letters, raising the projected matching to `888`; it remains
far from complete and does not enforce the same-role rectangle choice.
Moreover, if menus of only `q` frozen roles are changed, the one-edge old
graph gives the exact lower bound `24310<=2q+1`, hence `q>=12155`.
Thus the live chronology row requires a positive-density split--reinsertion
state class, not a bounded hinge sidecar.  This audit is frozen in
`MATH_AUDIT_K_K17_HINGE_RECTANGLE_BALANCE_INDEPENDENT_20260802.md`,
SHA-256
`c9bc857fd81be1b168f0bcbb51b54822fb2bf08a6d8f916dda4df360e61dfb69`.

The audit also checks that the analogous K19 compression already loses the
top-largest inequality (`94,183>92,378`), so this is not promoted to an
all-`m` chainization recurrence.

## 10. The exact remaining all-`m` lemma

For a chosen component budget `s=s(d)`, define `PBCOH_s(m,d)` to assert the
existence of a phase-aligned factor satisfying the five hypotheses of
Theorem 4.1.  The useful targets are an absolute `s`, `s=O(d)`, or the
strong one-cycle case `s=1`.

Theorem 4.1 proves

\[
 \boxed{
  \operatorname {PBCOH}_s(m,d)
  \Longrightarrow
  \begin{array}{c}
  \text{upper-exact rooted Catalan forest,}\\
  \text{ambient component count at most }s,\\
  \text{protected depth-}d\text{ resident collar.}
  \end{array}}                                           \tag{10.1}
\]

Within the factor-subset face, Theorem 3.1 makes the omission-Hall part
necessary as well as sufficient.  Thus (10.1) is not hiding another colour
selection or graphic theorem.

`PBCOH_s` is strictly smaller than `PCS(m,d)`.  It contains no:

* global source/address or ordered-history quotient;
* residence assertion outside the protected collar;
* upper witness of width beyond the immediate turn;
* Catalan-component physical connector chronology;
* endpoint aperture/common-cap compiler; or
* Pascal regeneration state.

The strongest unconditional all-parameter part currently proved is
Proposition 1.1.  What remains is exactly to strengthen that protected
factor completion so it is upper-covering, has bounded components (or a
collar-safe transparent pull tree), accepts the two collar boundary states,
and satisfies (3.1).  The K17 factors show that these requirements are not
numerically incompatible, but they do not prove this Boolean all-`m` lemma.
