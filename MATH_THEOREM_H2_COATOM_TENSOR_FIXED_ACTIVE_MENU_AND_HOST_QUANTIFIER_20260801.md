# Fixed-active coatom menus: quadratic boundary atlas, exact resource cuts, and the incumbent-host obstruction

Date: 2026-08-01  
Lane: H2, independent resource/exclusion audit for the additive-constant route  
Status: exact conditional menu theorem and exact quantifier obstruction.  No
arbitrary-Pascal-task embedding, compiler deletion label, or `B(k)+O(1)`
conclusion is asserted.

## 0. Verdict

The mixed-screen tensor has a genuine quadratic **common-boundary atlas**.
Fix its six active labels and vary two ordered filler labels.  At owner rank
`r` and residence depth `delta`, the exact menu size is

\[
 q(q-1),\qquad q=r-\delta-2.                                  \tag{0.1}
\]

Every physical owner is common, `u`-only, or `v`-only.  The only genuinely
two-label immediate resources are twelve block-internal intersections, and
each fixed value occurs for at most the two orders of one unordered pair.
Consequently every forbidden noncommon owner or immediate-palette value has
bipartite label-cover number at most two.  If `t` such values are forbidden,
then at least

\[
       q(q-1)-2t(q-1)=(q-2t)(q-1)                         \tag{0.2}
\]

options survive.  Thus `t=O(delta)` and `delta=o(r)` leave
`(1-o(1))r^2` candidates, proving the desired `O(delta r)` loss **on this
conditional fibre**.

There are two exact qualifications.

1. The packet has `12delta+11` owner values, `12delta-2` lower-palette
   values, and `20` upper-palette values common to every option.  If even one
   required freshness/protection row forbids a common value, the whole
   quadratic menu dies.  These resources must be incumbent-safe or
   task-private, including across different task lists.
2. The atlas does not consist of many replacements of one incumbent word.
   The ordered filler pair is recoverable from the old physical word, so a
   fixed incumbent has certified fibre at most one.  The theorem in the
   source note compares `X(u,v)` only with `Y(u,v)`; it gives no
   cross-parameter comparison `X(u0,v0)->Y(u,v)`.

Hence the mixed screens remove the old four-owner sidecar, and no hidden
quadratic loss occurs inside the literal owner/q1 resource ledger.  The
remaining obstruction is the host/task/compiler quantifier: an arbitrary
Pascal task is not yet proved to expose the candidate-dependent old phases
or a common unused-basis deletion cell.

## 1. Fixed-active common-boundary atlas

Work in `J(2r,r)`.  Fix a set

\[
                         H\in{\Omega\choose r-2},                \tag{1.1}
\]

an active label `e in H`, and distinct fixed labels
`a,b,c,z,infinity,g` outside the places in which the tensor requires them.
Fix `h in H-{e}` and an ordered set

\[
 S\subset H-\{e,h\},\qquad |S|=\delta-2,                       \tag{1.2}
\]

so this presentation applies for `delta>=2`.  Put

\[
 R=H-\bigl(\{e,h\}\cup S\bigr),\qquad |R|=q=r-\delta-2.        \tag{1.3}
\]

For every ordered pair `(u,v)` of distinct members of `R`, take the ordered
filler and core

\[
 F_{uv}=(g,S,u,v,h),\qquad
 K_{uv}=H-\bigl(\{e,h,u,v\}\cup S\bigr).                       \tag{1.4}
\]

Then `|F|=delta+2` and `|K|=r-delta-4`, exactly as required by the
mixed-screen theorem.  Use the fixed active relabelling

\[
                  (e,a,b,c,d,\infty)=(e,a,b,c,z,\infty).        \tag{1.5}
\]

### Theorem 1.1 (exact common-boundary fibre)

Every ordered `u!=v` gives one legal mixed-screen packet of length
`12delta+35`.  All `q(q-1)` packets have the same ordered endpoints

\[
 L=(H-e)+\{\infty,a,b\},\qquad
 R_0=(H-h)+\{g,a,b\}.                                           \tag{1.6}
\]

For each parameter pair the two phases are simple Johnson paths, have the
same owner set, prefix/suffix signatures, internal OR-support deck,
immediate lower/upper palette multisets, and clipped residence state.

#### Proof

All hypotheses of the mixed-screen theorem follow directly from (1.2)--
(1.5).  At the first block the omitted filler is `g`, so

\[
 K_{uv}\cup(F_{uv}-g)=H-e.
\]

At the last block the omitted filler is `h`, and the active last triple
contains `e,a,b`, giving the second endpoint in (1.6).  Neither endpoint
contains `u` or `v`.  The remaining assertions are the literal
mixed-screen theorem under this relabelling. \(\square\)

For a Pascal convention whose child owner rank is `r=m+1`, (0.1) becomes

\[
                         (m-\delta-1)(m-\delta-2).               \tag{1.7}
\]

Using `r` avoids an otherwise harmless one-unit parameter ambiguity.
The zero-defect tensor itself also exists at `delta=1`; only this particular
two-variable planting with both endpoints fixed uses `delta>=2`.  The
bounded `delta=1` interface is therefore a separate base case.

## 2. Exact owner and palette dependence

### Theorem 2.1 (resource normal form)

Across the fixed-active atlas, the `12delta+35` owner addresses split as

\[
 \begin{array}{c|ccc}
   &\text{common}&u\text{-only}&v\text{-only}\\ \hline
 \text{owners}&12\delta+11&12&12.
 \end{array}                                                    \tag{2.1}
\]

The `12delta+34` adjacent intersections and unions split addresswise as

\[
 \begin{array}{c|rrrr}
   &\text{common}&u\text{-only}&v\text{-only}&(u,v)\text{-joint}\\ \hline
 \text{intersection}&12\delta-2&12&12&12\\
 \text{union}&12\delta+34&0&0&0.
 \end{array}                                                    \tag{2.2}
\]

After equal values at different addresses are identified, there are exactly
`12delta+11` common owner values, `12delta-2` common intersection values,
and `20` common union values.  For any fixed noncommon owner or intersection
value, its occurrence graph on the ordered-pair ground has vertex-cover
number at most two.  There is no noncommon union value.

#### Proof

In every active block, the coatom positions omitting `g`, a member of `S`,
or `h` are independent of `(u,v)`.  There are exactly `delta` such positions
per block.  The positions omitting `u` and `v` depend only on the respective
label.  This gives `12delta,12,12` block owners.  Every lower screen uses

\[
                     K_{uv}\cup F_{uv}=H-e+g,
\]

and every upper screen uses

\[
                     K_{uv}\cup F_{uv}^{\circ}=H-\{e,h\},
\]

so all eleven screens are common, proving (2.1).

The same coatom calculation on consecutive block cells proves (2.2).
Only the edge between the `u`-omitting and `v`-omitting coatoms depends on
both labels; there is one in each of the twelve blocks.  Its value determines
the unordered pair `{u,v}`, hence occurs for at most `(u,v)` and `(v,u)`.
A noncommon owner can occur in the `u` and `v` roles for one recovered label,
so its graph is covered by the two corresponding shore vertices.  All
unions of consecutive coatoms contain the full filler, and the screen-edge
unions have the same cancellation, so they are common.  Direct substitution
of the twelve fixed active triples identifies the displayed common-value
counts. \(\square\)

Equivalently, if `C` is the common owner bank and `T_t` is the twelve-owner
bank at the coatom position omitting `t`, then

\[
       \mathcal O_{u,v}=\mathcal C\;\dot\cup\;\mathcal T_u
                                  \;\dot\cup\;\mathcal T_v,
       \qquad |\mathcal C|=12\delta+11,quad |\mathcal T_t|=12. \tag{2.4}
\]

The banks `T_t` are pairwise disjoint.  This is the owner-level reason that
there is no hidden joint `(u,v)` token.

### Corollary 2.2 (protected-resource pruning)

Let `T` be a bank of forbidden exact owner, adjacent-intersection, or
adjacent-union values.

* If `T` meets the common bank of Theorem 2.1, no option survives.
* Otherwise, if `|T|=t`, the union bad graph has vertex-cover number at most
  `2t`, so (0.2) holds.

In particular, for `t<=A delta+B`,

\[
 |\mathcal L_{\rm good}|
 \ge (r-\delta-3)\bigl(r-\delta-2-2A\delta-2B\bigr).            \tag{2.3}
\]

This is quadratic whenever `delta=o(r)`.  The same conclusion covers unary
coordinate-label exclusions.  It does **not** cover an arbitrary Boolean
predicate on `(u,v)`.

## 3. Exact host and task obstruction

### Theorem 3.1 (fixed incumbent fibre one)

The map

\[
                         (u,v)\longmapsto X_\delta(u,v)          \tag{3.1}
\]

from ordered filler pairs to old physical words is injective.  Therefore a
fixed incumbent slot agrees with at most one certified old phase, although
all candidates have the common boundary (1.6).

#### Proof

Inside every active block, the fixed coatom order contains consecutive
addresses whose omitted filler labels are `u` and then `v`.  The physical
sets at those addresses recover the two missing members relative to the
fixed task frame, in order.  Hence the word recovers `(u,v)`. \(\square\)

As an unordered owner set the exact fibre is `{(u,v),(v,u)}` by (2.4);
chronology removes that ambiguity.  More importantly, the source theorem
proves only

\[
                       X_\delta(u,v)\leftrightarrow Y_\delta(u,v),             \tag{3.2}
\]

not `X_delta(u0,v0)->Y_delta(u,v)`.  Thus Theorem 1.1 is a quadratic atlas
for joint old-host/packet selection, not yet a quadratic replacement list at
one already fixed word slot.

The same quantifier remains at the prescribed-task level.  The active ECO
toggle is fixed, but no current theorem proves that every nonexceptional
Pascal defect exposes one of the old phases (3.2).  Likewise U5 is absent:
no map from `(u,v)` to a cell unused by one trace-guarded compiler matching
has been constructed.  A task guard or U5 guard not reducible to the exact
resources in Theorem 2.1 may have an arbitrary bipartite bad graph, including
a linear matching or a complete rectangle.  Such a row can remove
`Theta(r^2)` choices and is not bounded by (2.3).

Finally, common resources must be private between task lists.  If two tasks
regard the same common owner as a conflicting new resource, every option in
one list conflicts with every option in the other.  The resulting complete
bipartite conflict is another literal quadratic obstruction.  Task-private
frames or declared incumbent sharing are therefore hypotheses, not
consequences of label abundance.

## 4. Complementary active-label orbit

There is a second useful but weaker calibration.  Fix `D subset H` with
`|D|=delta+1`, a fresh `f`, and set

\[
 F=D+f,\qquad K_e=H-(D+e).
\]

Vary `e in H-D` and the external active label `z`, using `d=z`.  On
`J(2r,r)` the exact raw count is

\[
                    (r-\delta-3)(r-3).                         \tag{4.1}
\]

Every owner and immediate-palette address is constant, `e`-only, or
`z`-only.  The owner counts are

\[
          6\delta+17,quad3\delta+10,quad3\delta+8,             \tag{4.2}
\]

and the intersection/union counts are respectively

\[
 (6\delta+17,3\delta+11,3\delta+6),\qquad
 (6\delta+16,3\delta+8,3\delta+10).                            \tag{4.3}
\]

Every fixed nonconstant resource has cover number one, so `t` protected
nonconstant values lose at most `rt` options.  This is an exact star-pruning
calibration.  It does not solve the host problem: the first endpoint recovers
`e`, leaving only `r-3` choices at a fixed boundary, and the full old word
recovers both labels, leaving at most one at a fixed incumbent.

## 5. Audit

The dependency-free finite replay is

```text
scratch/audit_h2_coatom_tensor_pascal_menu_20260801.py
scratch/h2_coatom_tensor_pascal_menu_20260801.audit.json
```

It instantiates both fibres over a range of ranks and depths, reconstructs
both tensor phases from literal sets, and checks Johnson legality, simple
owners, owner current, prefix/suffix signatures, internal OR decks,
immediate palettes, exact resource-dependence tables, fixed-resource cover
numbers, boundary fibres, and incumbent fibres.  Its status is

```text
PASS_CONDITIONAL_STAR_MENU_FIXED_HOST_OBSTRUCTION
```

A second independent bit-mask replay is

```text
scratch/audit_h2_coatom_fixed_active_quadratic_menu_20260801.py
scratch/h2_coatom_fixed_active_quadratic_menu_20260801.audit.json
```

It verifies (2.4), the common endpoints, fixed-word fibre one and
fixed-owner-set fibre two over 42 `(r,delta)` instances.  Its status is

```text
PASS_FIXED_BOUNDARY_FORMAL_MENU_WITH_COMMON_INCUMBENT_GATE
```

The finite replay supports the symbolic calculations; it is not evidence
that an arbitrary Pascal task supplies the required old host or compiler
cell.
