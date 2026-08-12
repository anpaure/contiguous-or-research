# Same-parity pure-sector splitting, the plateau receiver conservation law, and the complete-old-hex gate

**Date:** 2026-08-02  
**Status:** exact split normal form, exact scalar receiver conservation, exact
accepted-supercolumn formulation, and an exact prospective one-zero/one-`xy`
Boolean-hex
receiver.  The current frozen corpus does not contain an integral `m=9`
triangular parent, a typed `k=17 -> 19` receiver bank, or an accepted bulk
supercolumn.  No resident factor, word, all-dimensional source, or compiler is
claimed.

## 0. Verdict

The `1156` mixed-tag cut rules out the unchanged indivisible four-sector
interface, but it does not rule out a split recurrence.  There is an exact
local replacement.  For every top-containing parent chain

\[
 C=(S_1\subsetneq\cdots\subsetneq S_\ell=A),
\]

separate the old mixed piece into the untagged foot and the pure-`xy` head

\[
 F_C=(S_1),\qquad
 H_C=(S_1+xy,\ldots,S_{\ell-1}+xy).
\]

When `ell+1<=d'`, prepend `F_C` to `Q_C^0`; on a saturated plateau
`d'=d, ell=d`, retain `Q_C^0,F_C,H_C` as three pieces.  This preserves every
target and every child top exactly and leaves no **residual** piece with an
internal `0 -> xy` transition.  The saturated three-piece recut is locally
sharp.  A class-`B` singleton instead saves one piece because `H_C` is empty.

The redesign exposes a stronger global conservation law.  The untagged sector
has mass `Lambda+W`, only `W` untagged top roots, and at most the child boundary
capacity `tau_(d')`.  Therefore the exact two-sector scalar-relaxation mass
which must still cross
from tag `0` into a nonzero-tag path is

\[
 \boxed{\Delta_0=
 [\Lambda+W-d'W-\tau_{d'}]_+
 =\begin{cases}
   [W-\sigma]_+,&d'=d,\\
   0,&d'=d+1.
  \end{cases}}                                      \tag{0.1}
\]

At the current `m=9` plateau,

\[
 \Delta_0=24310-7401=16909.                         \tag{0.2}
\]

Every nonzero-root path contains at least one nonzero target, so at capacity
`d'=3` at least

\[
                         \left\lceil{16909\over2}\right\rceil=8455
                                                               \tag{0.3}
\]

native child-root paths must carry untagged mass when no exterior zero-only
root capacity is added.  These are baseline receiver paths, not
`8455` exported tasks.  The standard unsplit class-`A` roots already carry one
such foot apiece, namely `19448-gamma` cells.  Their scalar excess above (0.2)
is

\[
                         2539-\gamma.                \tag{0.4}
\]

Thus (0.2) is a conservation law, not a new current scalar contradiction.
The global receiver ledger must preserve these baseline crossings; for
example, a balanced one-pair column can replace one existing class-`A`
crossing by one class-`B` foot/head crossing.  It must not charge (0.2) and
the class-`B` absorption again.

Indiscriminately splitting every class-`A` root is also impossible at small
raw-address cost.  On the current depth-three plateau the exact parent-slack
identity forces at least `16909` additional residual pieces in the all-split
normal form.  Selective receiver activation is therefore essential.

For a fixed literal bank, the exact completion problem is a replayed
accepted-supercolumn optimization built over a binary column set partition.  A
column places the zero foot and the
pure-`xy` head, chooses every root and intervening residual piece, respects
path capacity, and records its exact state word; the replayed supercolumn
returns the complete owner/palette/history/cap/`J`/topology/voltage/star/
protected state.  Separate zero-shore and `xy`-shore Hall
tests are necessary projections but are not sufficient.

A complete old Boolean hex planted prospectively has exactly one independently
exposed zero role and one independently exposed `xy` role.  After specializing
its two active labels to `x,y`, its six owner
roles have tags

\[
                         xy,x,y,0,y,x.                \tag{0.5}
\]

There is exactly one `xy` role and one `0` role.  With the third fragment as
the corridor anchor, its ternary switch takes

\[
       \text{anchor}+\text{one `xy` head}+\text{one zero foot}
                         \longrightarrow\text{one component}. \tag{0.6}
\]

It is therefore arity one in the conservative one-head/one-foot-per-role
projection.  Comparable heads and feet can instead be prepacked into the two
payload paths, so this is not a general one-pair theorem.  In the one-head-per-
root projection, if hexes are the only added/activated receiver capacity, a
bank of `h` such hexes must obey

\[
 h\ge[n_B-(d+d')-LdH_0]_+,
\]

and hence at `m=9`

\[
 \boxed{h\ge[1156+\gamma-3LH_0]_+.}                 \tag{0.7}
\]

For zero exported ticket capacity the one-head projection needs at least
`1156` hexes.  Other activated roots contribute additively to the left side of
(0.7); they cannot be omitted and still call `h` a hex lower bound.

Once multihead paths are allowed, one must restart from head mass rather than
divide the one-head deficit in (0.7).  Put
`M_B=sum_(C in B_+)|H_C|>=n_B`.  On the native hex-only compound-path
projection, grant the unchanged standard bank the upper payload
`d(d'-1)+tau_(d')`, grant exterior tickets the upper payload `d'LdH_0`, and
grant each hex one native `xy` root path with payload at most `d'-1`.  Then

\[
 h\ge
 \left\lceil{
 [n_B-d(d'-1)-\tau_{d'}-d'LdH_0]_+
       \over d'-1}\right\rceil.                                  \tag{0.8}
\]

At `m=9,gamma=H_0=0`, (0.8) gives `575`.  Additional activated roots require
an explicit additional capacity term.  No packing above one pair is proved.
There is no owner-layer **scalar** obstruction to a Catalan-sized prospective
bank, but no theorem in the frozen corpus packs and binds that bank.  The
smallest remaining obstruction is already a three-role one: a global perfect
matching can use only cyclic cross-role edges while every prescribed
within-role table is empty.  For a fixed candidate the exact added expansion
hypothesis is the block-Hall family

\[
                         |D_3(S)|\le\kappa_3(S)
                         \qquad(S\subseteq L_0^{(3)}),             \tag{0.9}
\]

together with the full accepted-column replay.  Fixed role names and corridor
order do not imply (0.9).

The fixed-`z` seven-ear atlas and twisted `C6` remain terminal tools, not this
bulk bank.  At child `(k,r,d)=(19,10,3)` the pump condition `r>=3d+4=13`
fails, the explicit two-bank collar count contains `(3)_4=0`, and the small
protected theorem cannot plant more than one closure-only hex even before
history collars.  Their authenticated preterminal receiver capacity is zero.

## 1. Setup and the four parent classes

Let

\[
 k=2m-1,\quad W={2m-1\choose m},\quad
 c=\operatorname{Cat}_m,\quad
 \Lambda=4^{m-1}-1,\quad \tau_q={q+1\choose2},
\]

and let `d` be minimal with `dW+tau_d>=Lambda`.  Put

\[
                         \sigma=dW+\tau_d-\Lambda.
\]

Assume `d>=2`, which includes the current lane.  The exceptional depth-one
initial step must be treated separately; the singleton and saturated recuts
below are not asserted there.

For the child `k'=2m+1`, write its depth as `d'`; the Pascal recurrence gives
`d' in {d,d+1}`.  Assume the integral triangular parent required by the
four-sector theorem.  Its `W+d` chains partition every nonempty old target of
rank at most `m-1`.

With `gamma=|C|`, the four parent classes have sizes

\[
 |A|=W-c-\gamma,\qquad |B|=c+\gamma,
 \qquad |C|=\gamma,\qquad |D|=d-\gamma.              \tag{1.1}
\]

Classes `A,B` contain a rank-`(m-1)` target, classes `A,C` contain a
rank-`(m-2)` target, and `C,D` are top-free.  For a top-containing chain

\[
 C=(S_1\subsetneq\cdots\subsetneq S_\ell=A),
\]

the two relevant standard pieces are

\[
 \begin{aligned}
 Q_C^0&=(S_2,\ldots,S_\ell,\mu(A)),\\
 R_C&=(S_1,S_1+xy,\ldots,S_{\ell-1}+xy).
 \end{aligned}                                      \tag{1.2}
\]

Each has length `ell`; `mu(A)` is the matched child rank-`m` target.

Write `B_+` for the class-`B` chains of length at least two and
`n_B=|B_+|`.  Write `b_1` for the class-`B` singletons, `b_d` for the
class-`B` chains of length `d`, and `a_d(E)` for the length-`d` members of a
selected family `E subseteq A`.

## 2. Exact pure-sector split normal form

Define

\[
 F_C=(S_1),\qquad
 H_C=(S_1+xy,\ldots,S_{\ell-1}+xy).                  \tag{2.1}
\]

The head is empty exactly when `ell=1`.

### Theorem 2.1 (capacity-correct split)

For every top-containing parent chain the following replacements are exact.

1. If `ell+1<=d'`, replace `(Q_C^0,R_C)` by

   \[
       \widehat Q_C^0=(S_1,S_2,\ldots,S_\ell,\mu(A)),
       \qquad H_C,                                   \tag{2.2}
   \]

   deleting `H_C` when it is empty.

2. If `d'=d` and `ell=d`, replace `(Q_C^0,R_C)` by

   \[
                         Q_C^0,\qquad F_C,\qquad H_C. \tag{2.3}
   \]

The target multiset and total mass are unchanged.  Every displayed piece has
length at most `d'`.  The number and identity of child rank-`m` top targets are
unchanged.  Every newly exported residual piece is tag-homogeneous.

Within the homogeneous interface, (2.3) is piece-count minimal: a saturated
split needs at least three pieces.  For a class-`B` singleton, (2.2) instead
replaces two nonempty pieces by one.

#### Proof

The disjoint target identity is

\[
 Q_C^0\mathbin{\dot\cup}R_C
  =\{S_1,\ldots,S_\ell,\mu(A)\}
      \mathbin{\dot\cup}
    \{S_1+xy,\ldots,S_{\ell-1}+xy\}.                 \tag{2.4}
\]

The first set is the chain `widehat Q_C^0` of length `ell+1`; the second is
`H_C` of length `ell-1`.  This proves (2.2), its capacity statement, and mass
conservation.  On a plateau the only failure of `ell+1<=d'` is `ell=d`.
Separating the first set into `Q_C^0` and `F_C` gives (2.3), with lengths
`d,1,d-1`.

For class `A`, `S_{\ell-1}` has rank `m-2`, so `H_C` retains the old `xy`
rank-`m` top.  For class `B`, `H_C` contains no rank-`m` target.  In both
classes `Q_C^0` or `widehat Q_C^0` retains `mu(A)`.  Thus all top identities
are unchanged.

For minimality on a plateau, `Q_C^0 union F_C` consists of `d+1` untagged
targets and cannot fit in one capacity-`d` path.  The nonempty `H_C` must be
separate if exported pieces are to remain tag-homogeneous.  Hence at least two
untagged pieces plus `H_C` are required; (2.3) attains three.  If `ell=1`,
then `H_C` is empty and
`F_C\mathbin{\circ}Q_C^0=(S_1,\mu(A))`, proving the singleton
saving. \(\square\)

An unsplit class-`A` piece `R_C` is allowed to remain mixed: it is already a
child-top sink.  The theorem removes mixed transitions from the **residual
shore** by splitting all class-`B` chains; it does not require splitting every
class-`A` root.

### Corollary 2.2 (exact raw address change)

If every class-`B` chain and precisely the class-`A` chains in `E` are split,
put

\[
              \eta={\bf1}_{d'=d}\bigl(b_d+a_d(E)\bigr)-b_1.       \tag{2.5}
\]

Then the inherited residual-piece ledger and its raw contraction ledger are

\[
               c+4d+\eta,
               \qquad c+4d-d'+\eta,                  \tag{2.6}
\]

respectively.

#### Proof

A nonsaturated non-singleton split replaces two pieces by two.  Every
saturated split replaces two by three and creates one residual address.  A
class-`B` singleton replaces the top piece and its one residual singleton by
one top piece.  No other four-sector piece changes.  Starting from the exact
`c+4d` residual ledger and retaining `d'` boundary roots proves (2.6).
\(\square\)

### Corollary 2.3 (all-split plateau address floor)

Suppose every class-`A` and class-`B` chain is split, and put
`s=a_d(A)+b_d`.  The exact parent capacity slack satisfies

\[
 \sigma=\sum_{C\text{ anchored}}(d-\ell_C)
          +\sum_{i=1}^d(i-\ell_{\partial_i}).          \tag{2.7}
\]

Consequently

\[
 \sigma\ge W-s+(d-2)b_1,
 \qquad
 \eta=s-b_1\ge W-\sigma+(d-3)b_1.                    \tag{2.8}
\]

In particular, on the current `d=3` plateau,

\[
                              \eta\ge W-\sigma=16909. \tag{2.9}
\]

#### Proof

Equation (2.7) is total capacity minus the exact parent mass.  Each of the
`W-s` nonsaturated anchored chains contributes at least one slack cell.  A
class-`B` singleton contributes `d-1`, namely another `d-2` beyond that first
cell.  This gives the first inequality in (2.8); subtracting `b_1` gives the
second. \(\square\)

The quantity `eta` counts raw inherited pieces/contractions, not accepted
tasks.  Equation (2.9) says that the correct redesign must activate a selected
receiver subbank or close a bulk supercolumn; it must not materialize the
all-split bank as independent residual addresses.

## 3. The pure-`xy` truncation and the remaining path forest

If all class-`A` and class-`B` chains are split, their heads, together with
the `xy` copies of the top-free chains, are exactly the restrictions of all
parent chains to old ranks at most `m-2`, with `xy` adjoined.

### Proposition 3.1 (exact `xy` ledger)

After deleting empty class-`B` heads, the pure-`xy` sector has the following
raw labelled-address ledger:

\[
 \begin{array}{c|c}
 \text{quantity}&\text{value}\\ \hline
 \text{target mass}&\Lambda-W\\
 \text{rank-`m` roots}&|A|+|C|=W-c\\
 \text{raw residual address labels}&n_B+|D|=n_B+d-\gamma\\
 \text{scalar root surplus}&d'(W-c)-(\Lambda-W).
 \end{array}                                                   \tag{3.1}
\]

At `m=9,d'=3`, these are mass `41225`, roots `19448`, capacity `58344`,
and surplus

\[
                              17119.                  \tag{3.2}
\]

#### Proof

The old targets through rank `m-2` have mass `Lambda-W`.  A truncated chain
is rooted exactly when it contains a rank-`(m-2)` target, namely in classes
`A,C`; (1.1) gives `W-c` roots.  Precisely the `B_+` restrictions are the
nonempty class-`B` residuals.  Every class-`D` address is a raw unrooted label,
although its selected chain can be empty.  This gives the raw residual count.
Multiplying the root count by `d'` and subtracting the mass gives the scalar
surplus. \(\square\)

A class-`D` boundary address can select an empty chain.  Such an address stays
in the raw ledger in (3.1) but is deleted from the nonempty physical
set-partition bank.  Thus `n_B+d-gamma` is not asserted to be the number of
nonempty `xy` pieces without an additional nonemptiness antecedent.

The positive surplus in (3.2) does **not** prove the path forest.  It ignores
endpoint containment, root capacity sharing, foot placement, and every lifted
acceptance row.

## 4. Plateau receiver conservation and the saturated-foot obstruction

The split cannot make all four tag sectors independent on a plateau.

### Theorem 4.1 (exact native scalar cross-tag minimum)

In the native child scalar projection, with no newly planted exterior zero-only
root capacity, the minimum number of untagged target cells that must be placed
on paths containing a nonzero tag is (0.1).  If `d'>1`, the number of such
receiver paths is at least

\[
                              \left\lceil{\Delta_0\over d'-1}\right\rceil.
                                                               \tag{4.1}
\]

#### Proof

The untagged child targets are all `Lambda` old nonempty targets and the `W`
matched tops `mu(A)`, hence have mass `Lambda+W`.  There are exactly `W`
untagged top roots.  Even assigning the entire boundary triangle to this
sector, zero-only paths hold at most `d'W+tau_(d')` targets.  The excess is
the first expression in (0.1).  On a jump it is attained by the local split:
every anchored zero chain has length `ell+1<=d+1`, and the `d` old top-free
zero copies retain their parent boundary capacities inside the `d+1` child
boundary slots.  Thus no zero target is forced across a tag.

On a plateau with `Delta_0>0`, the bound is attained in the two-sector scalar
relaxation because the remaining child root capacity differs from the
remaining target mass by the global child slack.  Explicitly, the nonzero-tag
target mass is `3Lambda-W+3`, its root capacity is `d'(3W-c)`, and

\[
 d'(3W-c)-(3\Lambda-W+3+\Delta_0)
 =d'W'+\tau_{d'}-(4\Lambda+3)=\sigma'\ge0.          \tag{4.1a}
\]

If a plateau has `Delta_0=0`, then `sigma>=W`, and the missing tagged-capacity
check is

\[
 \begin{aligned}
 d(3W-c)-(3\Lambda-W+3)
   &=W-dc-3\tau_d+3\sigma-3\\
   &\ge4W-dc-3\tau_d-3>0.                            \tag{4.1b}
 \end{aligned}
\]

Indeed `d<=m-1`, `c=2W/(m+1)`, and `2W>3tau_d+3` for `m>=3`.
Thus the nonzero sector also fits in this final scalar case.

This is scalar attainment only; it does not supply endpoint-containment or
accepted product-state columns.

On a plateau, substitute `Lambda=dW+tau_d-sigma`.  On a jump use
`tau_(d+1)=tau_d+d+1`; the untruncated difference is `-sigma-d-1`.  This proves
the second expression in (0.1).

A path counted by the excess contains at least one nonzero target, so at most
`d'-1` of its cells are untagged.  Summing over such paths proves (4.1).
\(\square\)

More generally, if newly planted exterior zero-only chains have total capacity
`kappa_0`, the exact necessary tradeoff is

\[
                    (d'-1)R_{\rm cross}+\kappa_0\ge\Delta_0,       \tag{4.2}
\]

where `R_cross` counts native paths containing both zero and nonzero targets.
If there are `q_0` exterior chains each of capacity at most `d'`, one may use
`kappa_0<=d'q_0`.  Thus `8455` is an internal-root lower bound on the
`kappa_0=0` face, never a compound-task lower bound.

### Corollary 4.2 (the current baseline is not double-charged)

At `m=9`, equations (0.2)--(0.4) hold.  In particular, the unsplit class-`A`
roots alone provide more one-cell crossings than the scalar minimum:

\[
 |A|-\Delta_0=(W-c-\gamma)-(W-\sigma)
                         =\sigma-c-\gamma=2539-\gamma.          \tag{4.3}
\]

This margin permits that many crossings to be removed in the scalar ledger,
but does not prove literal receiver choices.  A coupled receiver which replaces
an `A` foot by a `B` foot preserves one baseline crossing and consumes none of
the margin.

### Proposition 4.3 (forced saturated class-`B` feet)

On a plateau every integral parent obeys

\[
                              b_d\ge[c+\gamma-\sigma]_+.          \tag{4.4}
\]

Thus the aggregate scalar ledger permits every class-`B` chain to be short
only if `sigma>=c+gamma`.  This is not an integral chain-exchange theorem.

#### Proof

The mass strictly below ranks `m-2,m-1` is

\[
                         L=\Lambda-2W+c.
\]

Every class-`A` chain and every nonsaturated class-`B` chain contributes at
most `d-2` members of this mass; a saturated class-`B` chain contributes at
most `d-1`.  The boundary addresses contribute at most `tau_d-gamma` after
their `gamma` rank-`(m-2)` targets are removed.  Therefore

\[
 L\le(d-2)W+b_d+\tau_d-\gamma.
\]

Substitution of `Lambda=dW+tau_d-sigma` gives (4.4). \(\square\)

For `m=9`, (4.4) forces nothing because `7401>4862+gamma`.  On the next
`d=3` plateau, `m=10`, it forces

\[
                              b_d\ge1799+\gamma,       \tag{4.5}
\]

because `c=16796` and `sigma=14997`.  Those feet must either be placed in
typed zero slots or carried through coupled receiver columns.

### Corollary 4.4 (saturated-`B` receiver-path bank)

On a plateau `d'=d>=3`, a saturated class-`B` head has length `d-1` and is
not top-rooted.  After any nonempty `xy` top piece is appended, the path is
full.  Hence two saturated heads cannot share one capacity-`d` root path, and
the head cannot carry its foot on a native nonempty-top-root path.  A boundary
or exterior root can instead carry the old length-`d` mixed piece; those
exceptional paths are subtracted below.  On the standard-plus-new-root
projection,

\[
 R_{\rm act}+R_{\rm new}
   \ge[b_d-(d+d')-LdH_0]_+.                           \tag{4.6}
\]

At the `m=10` plateau this gives

\[
 R_{\rm act}+R_{\rm new}
   \ge[1793+\gamma-3LH_0]_+.                         \tag{4.7}
\]

These are internal/exterior root paths.  If planted in the baseline they are
not compound-task births.

#### Proof

The length statement follows from (2.1).  A root piece is nonempty, so one
saturated head plus that piece uses at least `(d-1)+1=d` cells.  Capacity
excludes a second head or its untagged foot.  The unchanged standard bank has
at most `d+d'` root paths and the exported tickets at most `LdH_0` independent
root sockets.  Subtracting these from the `b_d` distinct heads gives (4.6);
(4.4) at `m=10` gives (4.7). \(\square\)

## 5. Exact accepted-column formulation

The two split shores cannot be optimized independently.  Let `P` be the
occurrence-labelled primitive bank consisting of:

* every unchanged four-sector piece;
* every selected zero trunk `Q_C^0`, foot `F_C`, and head `H_C`;
* every selected activated class-`A` root fragment;
* the three newborn targets; and
* every declared terminal sidecar occurrence.

Delete empty primitives.  Let `R` be the occurrence-labelled child top and
boundary root slots, with their true path capacities.  Let `T` be the complete
typed resource universe: owner, lower facet, immediate and deeper upper,
positive and negative history, cap current and prefix debt, physical exterior
`J`, topology, voltage, star, and protected/private occurrences.

A **receiver column** `j` is a finite occurrence-labelled object which:

1. covers a specified subset `P_j subseteq P` exactly once;
2. partitions those targets into monotone paths, each join satisfying
   `max P subseteq min Q` and each path obeying its root capacity;
3. uses a specified set of root slots `R_j` at most once;
4. records every foot and head placement appearing in the column;
5. has a literal occurrence-resource vector on `T`; and
6. records its exact ordered product-state word.

Let `e_j` be the number of exterior receiver sockets exported by the column.
Write `a_(pj),r_(uj),q_(tj)` for primitive, root, and typed-resource incidence.
Normally the local split patterns are fixed before `P` is formed.  If the
optimization is also to choose them, introduce `z_(C,p)` and, for each
top-containing chain, choose exactly one local pattern

\[
 \{Q_C^0,R_C\},\qquad
 \{\widehat Q_C^0,H_C\},\qquad\text{or}\qquad
 \{Q_C^0,F_C,H_C\},                                  \tag{5.1}
\]

where the middle pattern is available only when `ell+1<=d'`, the last only
for a saturated plateau, and empty `H_C` is deleted.  A pattern variable links
the coverage of every variant piece `q` it creates by

\[
 \sum_p z_{C,p}=1,qquad
 \sum_{j:q\in P_j}a_{qj}x_j=z_{C,p(q)}.               \tag{5.1a}
\]

Unchanged primitives retain right side one, and underlying target occurrences
are covered exactly once.  This is necessary because a
nonsaturated split changes `Q_C^0` itself; linking only `R_C` against `F_C,H_C`
would be incorrect.  The pattern rows co-select the split shores, but do not
require them to lie on one monotone path.  If a repair must be
terminal-atomic, its catalogue must contain a paired placement ticket carrying
both placements and their joint return.

For the compound-task convention used here, every activated class-`B` origin
is either discharged wholly inside the declared baseline, or is assigned once
to such a paired macro (possibly using two chain paths).  Counting its foot and
head as separate exported tickets is forbidden.  A supercolumn may place them
in separate internal columns only when its exact union replay certifies their
internal cancellation and exports no split half as a task.

Ignoring the final noncommutative replay for one moment, the column master is

\[
 \begin{aligned}
 \rho_{\rm col}^*=\min\;&\sum_j e_jx_j\\
 \text{subject to }&\sum_j a_{pj}x_j=1 &&(p\in P\text{ for fixed patterns}),\\
                   &\sum_j r_{uj}x_j\le1 &&(u\in R),\\
                   &\sum_j q_{tj}x_j\le b_t &&(t\in T),\\
                   &x_j\in\{0,1\},                 \tag{5.2}
 \end{aligned}
\]

with the optional local pattern-linking equations (5.1a).  Equality rows
replace the resource inequalities for exact palettes.  Root/gap alternatives
sharing one physical path are one capacity slot, not cloned neighbours.

The master (5.2) alone is not the exact product-state problem.  Individually
acceptable cap/history columns need not commute, and their union can fail
`J`, topology, voltage, star, or exact selected-union replay.  Let
`mathfrak F` be the set of **accepted supercolumns**.  An element
`Phi in mathfrak F` consists of

* one complete integral solution of (5.1a)--(5.2), or of (5.2) after the
  patterns have been fixed;
* an order on its terminal-atomic tickets;
* the exact union of all occurrence resources; and
* a replay of that whole union returning every state in `T`.

Put

\[
 H_{\rm exact}=\min_{\Phi\in\mathfrak F}h(\Phi),
 \qquad\min\varnothing=\infty,                       \tag{5.3}
\]

where `h(Phi)` is the number of exported completed tickets.

### Theorem 5.1 (exactness of the supercolumn formulation)

For exhaustive literal path and ticket catalogues, `H_exact=q` if and only if
the split bank has a complete child path forest with `q` exported completed
tickets satisfying every state in `T`.

#### Proof

Decompose a physical solution into its root paths and terminal-atomic macros,
retain their literal order, and replay their union.  This is an element of
`mathfrak F`.  Conversely, an element of `mathfrak F` contains by definition
an exact target partition, capacity-valid roots, compatible physical
resources, and a successful whole-union replay, so it is the required forest.
\(\square\)

Because a column may contain several pure-`xy` heads, (5.2) is a set-partition
or hypergraph problem in general, not ordinary min-cost circulation.  A lifted
DAG/min-cost-flow reduction is exact only for a declared one-head-per-root or
otherwise capacity-faithful column family.  Even then it solves the full task
only when a commuting-atlas theorem makes the supercolumn replay automatic.

### Proposition 5.2 (scalar state does not bound accepted task count)

Holding `W,c,Lambda,d,sigma,d'`, every length histogram, `eta`, `Delta_0`, the
pure-`xy` scalar ledger, and all root capacities fixed, the abstract lifted
bank can have `H_exact=0` or `H_exact=infinity`.

#### Proof

For the first bank, give every required primitive a compatible containment
column and declare their exact union an internally accepted supercolumn.  It
exports no ticket.  For the second, retain all primitives, lengths, endpoints,
and scalar capacities, but give one required origin only product-state columns
whose physical `J` (or cap/history) terminal value is rejected.  Then every
scalar and rank-marginal row is unchanged while `mathfrak F` is empty.
\(\square\)

This is a countermodel to deduction from the scalar recurrence, not a claimed
literal Pascal instance.  A positive task lower bound requires independently
exported sockets and their per-ticket support bound; a finite task upper bound
requires a nonempty accepted supercolumn family.

### Necessary one-head projection

In the conservative family in which each complete final root path accepts at
most one member of `B_+`, every shore `X subseteq B_+` must
satisfy

\[
 |X|\le \operatorname{cap}N_{\rm std}(X)
       +\operatorname{cap}N_{\rm act}(X)
       +\operatorname{cap}N_{\rm new}(X)+LdH_0.       \tag{5.4}
\]

Here `N_std` is only the unchanged top-free/boundary bank, whose total
capacity is at most `d+d'`.  Every class-`A` root made pure-`xy` by a split,
and every other split-created slot, is charged explicitly to `N_act` or
`N_new`; the old `d+d'` bound does not apply to that enlarged bank.  Taking
`X=B_+` gives

\[
 \operatorname{cap}N_{\rm act}(B_+)
 +\operatorname{cap}N_{\rm new}(B_+)
 \ge n_B-(d+d')-LdH_0.                               \tag{5.5}
\]

The rank-capacity theorem gives `n_B>=1162+gamma` at `m=9`, so (5.5) becomes

\[
 \operatorname{cap}N_{\rm act}(B_+)
 +\operatorname{cap}N_{\rm new}(B_+)
 \ge1156+\gamma-3LH_0.                               \tag{5.6}
\]

Equations (5.4)--(5.6) count receiver incidences in this projection, not
compound tasks.  A multihead column can bundle incidences, but must then appear
literally in the exhaustive family of (5.2) and pass (5.3).

## 6. A prospectively planted complete old Boolean hex

Let the child owner rank be `r=m+1`.  Choose an old rank-`(r-1)` set `L`,
`b in L`, and an old label `c notin L`.  With `x,y` the two new labels, the
specialized Cartesian Boolean hex has owners

\[
 \begin{array}{lll}
 A=L-b+x+y &(xy),& B=L-b+x+c &(x),\\
 C=L-b+c+y &(y),& D=L+c &(0),\\
 E=L+y &(y),& F=L+x &(x).
 \end{array}                                                   \tag{6.1}
\]

Its old and rotated phases are

\[
 O=\{A\to B,C\to D,E\to F\},\qquad
 N=\{A\to F,C\to B,E\to D\}.                       \tag{6.2}
\]

### Theorem 6.1 (exact exposed-socket arity and component action)

Suppose the three old seams in (6.2) lie on three distinct directed
components (cycles in the closed old phase).  Open them into three protected
fragments and assign them by corridor order to an anchor role, a pure-`xy`
receiver role, and a pure-zero receiver role.  Then the switch `O -> N`:

* preserves the exact owner/tail/head, lower-facet, and immediate-cap
  multisets;
* has coherent signed switch charge zero;
* merges the three ordered components to one; and
* exposes exactly one independently rooted pure-`xy` fragment role and one
  independently rooted pure-zero fragment role.

Thus it has one-pair arity on the declared one-head/one-foot-per-role face.
Outside that face it may carry several origins already prepacked into its two
payload paths.  For a compound column carrying a set `X` of split pairs,
capacity alone forces

\[
 |X|\le d'-1,qquad
 1+\sum_{C\in X}|H_C|\le d'.                         \tag{6.3}
\]

Comparability and the full state rows can only reduce this ceiling.

#### Proof

The tags are read from (6.1).  Intersections on the old seams have tag
multiset `{x,0,0}` and their unions have `{xy,y,xy}`; the new seams have the
same two multisets.  Tail and head sets are also merely permuted.  This is the
Boolean-hex four-resource identity.  In one coherent physical lift the signed
edge potentials telescope, so the phase difference is zero.

Deleting the three old seams leaves three directed fragments.  The three new
seams act on their ends by a 3-cycle, hence return one component.  The unique
`xy` owner `A` and unique zero owner `D` prove the exposed socket count.  If
each split pair remains two separate fragments, only one pair plus the anchor
can occupy the three roles.  If several comparable heads and feet are first
concatenated into one `xy` path and one zero path, the switch still sees three
components.  Every nonempty head occupies at least one cell and its native
receiver path contains a mandatory top target, giving (6.3); the zero path
gives the same or a weaker capacity row. \(\square\)

This theorem is at the owner-tag level.  A literal thickening which binds a
triangular target head to `A` and its foot to `D`, while preserving occurrence
IDs and containment paths, is an additional row of (5.2)--(5.3).

### 6.1 Scale and current arithmetic

One old hex uses six owner endpoints, three lower facets, three immediate
caps, and three projected old seams (six incidence edges).  A complete old/new
collision footprint has six projected seams (twelve incidence edges).  A bank
of `h` pairwise resource-disjoint hexes has exactly `h` exposed zero roles and
`h` exposed `xy` roles.  Equation (0.7) follows from (5.6) only in the
one-head projection; on the same hex-only native-root projection the coarse
capacity-only compound lower bound is (0.8).

This is not a layer-size obstruction.  The identity

\[
                              W'=(2m+1)c               \tag{6.4}
\]

shows that a full `c`-bank uses

\[
                  6c={6W'\over2m+1}\quad\text{owners},
                  \qquad3c={3W'\over2m+1}
                         \quad\text{lower facets/caps}.             \tag{6.5}
\]

At `m=9`, `c=4862` and `W'=92378`, so these counts are `29172` and
`14586`.  A `1156`-hex bank uses `6936` owners and `3468` lower facets/caps.
The coarse compound-path lower bound of `575` hexes uses `3450` owners and
`1725` lower facets/caps.  Neither count is an existence certificate.
The tag strata also fit separately.  A `c`-bank uses `c` zero, `c` `xy`, and
`2c` each `x,y` owners, whose available strata have sizes
`W-c,W,W,W`.  It uses `2c` zero and `c` `x` lower facets, in strata of size
`W,W`, and `2c` `xy` and `c` `y` caps, in strata of size `W,W-c`.  Since

\[
                              c={2W\over m+1},         \tag{6.6}
\]

all these scalar inequalities hold for `m>=3`.  There is scalar room;
disjoint typed packing is unproved.

For one fixed target core at child `r=10`, the tag-specific Cartesian fan has

\[
                              (r-1)(r-2)=72            \tag{6.7}
\]

raw label options.  This is a menu, not a matching.  The small protected
extension allows only `r-2=8` protected incidence edges.  One closure-only
old hex costs six and meets this scalar budget; two cost twelve and do not.
Endpoint-history collars and a bulk bank require a new global completion
theorem.

### 6.2 Exact state ledger

Prospective planting settles only part of the state.

| row | exact local effect | remaining requirement |
|---|---|---|
| owner/lower/immediate cap | exact phase identity | occurrence-disjoint bulk host |
| positive/negative history | three new seams | three positive and three negative connector tests |
| cap current/debt | zero terminal delta as one simultaneous atom | actual prefix debt for any serialization |
| topology | `3 -> 1` for three distinct ordered roles | role-separated global completion |
| voltage | coherent switch charge zero | the two nonanchor old components, including closures `o_1,o_2`, must have zero total voltage to retain an anchor `+/-1` |
| exterior `J` | unchanged only if carried on the anchor | literal `J` binding and return |
| protected/private | local list is finite | disjoint bulk packing and private-edge avoidance |
| star/deep upper/source/compiler | not supplied | full accepted replay in (5.3) |

The hex preserves the sum of the three completed old-component voltages; it
does not generate a unit.  If its anchor is a twisted pump, the two nonanchor
old components, including their old closures, must sum to zero.  Bare open-path
voltage is gauge-dependent and is not the correct invariant.

## 7. The exact new expansion hypothesis and its smallest obstruction

Pre-fixing `e,o_1,o_2` removes post-hoc partner discovery and fixes component
roles, but it does not prove the residual ordered corridors.  For one fixed
hex, remove the three terminal tails and initial heads, partition the residual
fragments into the three required roles, and retain only capacity-faithful
forward joins within a role.  Let the resulting raw table be
`B_0^(3)=(L_0^(3),R_0^(3),E_0^(3))`.  For `S subseteq L_0^(3)`, let `D_3(S)`
be the raw neighbours for which every occurrence option is rejected by the
typed state, and put

\[
                         \kappa_3(S)=|N_0^{(3)}(S)|-|S|.            \tag{7.1}
\]

For a fixed capacity-faithful candidate, Hall's theorem gives the exact
criterion (0.9).  Adding the old seams then makes three components and the
rotated seams make one.

The following three-by-three counterexample is minimal for the prescribed
three roles.  Take left roles `ell_i`, right roles `r_i`, and only the cyclic
cross-role edges

\[
                              \ell_i r_{i+1}
                              \qquad(i\in\mathbb Z_3).              \tag{7.2}
\]

The unrestricted table has a perfect matching, has no charge or history
defect, and can respect one global forward order.  Every within-role table is
empty, so a singleton shore violates (0.9).  Therefore scalar capacity,
ordinary Hall, role names, and corridor order do not imply the receiver
supercolumn.

For many hexes, the exact added hypothesis is the capacity-faithful
multi-block analogue of (0.9), plus the accepted-column resource rows and
supercolumn replay in (5.2)--(5.3).  Proving this for an equivariant
Catalan-scale bank would make the bank
part of the baseline and would export only its outer product state.  Without
that union-supercolumn theorem, the `Theta(c)` literal hex records are
`Theta(c)` capacity-one occurrence rows/payload incidences; they may be bundled
only by the missing bulk supercolumn.  The Catalan mismatch has otherwise moved from
the old class-`B` shore to the planted anchors.

## 8. Fixed-`z`, seven-ear, and twisted-`C6` scope

The frozen packet families do not supply the bulk hypothesis of Section 7.

1. A closed fixed-`z` seven-ear packet consumes all fourteen far sockets in
   seven ears.  Opening one ear exposes the one ordered ambient corridor pair;
   it is not a surplus preterminal receiver bank.
2. Its current depth-three two-bank count is zero both at `(17,9,3)` and
   `(19,10,3)`, because the exterior factors are `(2)_4` and `(3)_4`.
3. The explicit fourteen-socket closure requires `k-r>=2d+12`; it fails at
   `k=19,r=10,d=3`.
4. The twisted pump requires `r>=3d+4=13`; it fails at child `r=10`.
5. Neither schema contains the occurrence-labelled lower-to-rank-`m` ears
   binding the split primitives of Section 5.  Their authenticated
   preterminal capacity is therefore zero.

They remain appropriate **after** a bulk receiver theorem: a fixed-`z`
seven-ear ticket can close bounded topology/history/cap/`J` residue, and one
twisted `C6` can provide the child-native unit voltage when its larger-parameter
planting hypotheses hold.  They cannot be counted as the `h` columns in
(0.7) without the missing binding and multi-block completion.

The older mixed bulk-compiler theorem has the correct exponential source
scale but leaves its functional compiler theorem unproved and exposes source
occurrences rather than the triangular path/root columns of (5.2).  It is a
candidate ingredient, not a proved receiver factor.

## 9. Current provenance and exact conclusion

The current frozen `final2754.factor.tsv` is an authenticated `k=17`
middle-layer factor with positive residence `2754`, exact immediate gates, and
deep holes `1853/357/0` at ranks `11/12/13`; it remains
`NONRESIDENT/NEED_CEGAR`.  It has no `m=9` triangular ancestry, new labels
`x,y`, split primitives, or `k=19` root table.  It cannot instantiate
(5.2)--(5.3).

No finite search is proof-safe before those literal typed rows exist.  The
strongest present result is therefore:

* a positive exact split normal form on every deadline jump;
* a sharp plateau baseline of `Delta_0` cross-tag cells and (4.1) receiver
  paths;
* a positive one-zero/one-`xy` exposed-socket old-hex receiver with no scalar
  layer-size wall; and
* a sharp three-role Hall obstruction and exact accepted-column hypothesis
  for the missing bulk theorem.

This is a redesign of the recurrence, not a refinement of the dead
indivisible-piece face.  It does not yet close a bounded-state regenerative
recurrence because the neutral Catalan-scale receiver supercolumn has not been
proved.
