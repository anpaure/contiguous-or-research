# K17 OPTIMAL28: exact component/cap physicalization and the immutable-complement obstruction

Date: 2026-07-31  
Status: exact reduction and solver-free obstruction for the fixed-component
face; no K17 word is claimed

## 1. Frozen input and verdict

The connected completion in
`scratch/ad_k17_opt28_residual_connected_bflow_20260731.json` has one
literal rank-nine owner cycle, every rank-eight lower colour exactly once,
and a contiguous marked bank

\[
       P=(P_1,\ldots,P_a),\qquad a=4108.
\]

The complementary bank has `20202` owners.  The direct two-bank row would
have

\[
 Z=P\,\Vert\,F,qquad |F|=20203,qquad |Z|=24311,
\]

and therefore exact short-cell slack

\[
 48625-(41224+a)=3293.
\]

Topology, middle ownership, and lower-q1 are closed.  They do not imply
physicalizability.  In fact the face which varies only the residual
pairing, component order, and component reversal is empty.

The literal zipper row from the saved one-cycle completion has no empty
maximal-envelope position, but it is not a `D2` row of any nonempty word:

```text
strict D2 runs below three             1025 of length1 + 1367 of length2
failed D2 row equations                                             3568
upper holes, ranks 10/11/12                                 1900/911/128
upper holes, ranks 13,...,17                                          0.
```

Thus the current row fails before the common-cap matching.  The upper repair
must fill the first three upper ranks while explicitly retaining the already
complete higher ranks.

After the `106` marked and `28` optional OPTIMAL28 components are removed,
the `4871` residual fixed forest components contain the following strict
internal owner-coordinate runs:

```text
length 2                         320 runs
length 3                         404 runs
total length below 4             724 runs
components supporting them       257
```

The weaker threshold-three ledger already has `320` invariant defects in
`82` components.  These are component-interior defects, not seams of the
currently saved cycle.

There is also a port-splitting-resistant atomic floor.  Among the unselected
macro owner words, `141` macros contain `227` strict internal runs, all of
length three and all on old coordinates.  Hence splitting components only at
their existing macro ports still leaves `227` forced length-two facet runs.

### Theorem 1.1 (immutable-complement obstruction)

No re-pairing of the `4872` residual U owners, no ordering of the residual
fixed components, and no reversal of those components can make the
OPTIMAL28 two-bank row satisfy exact D2 inversion.

#### Proof

Let `q_j,...,q_(j+l-1)` be any one of the `724` strict internal positive
runs, with `l` equal to two or three, inside one fixed complementary owner
word.  Its two neighbouring owner rows in that same component omit the
coordinate.  In the facet word

\[
              f_i=q_i\cap q_{i+1},
\]

the run becomes a strict internal positive run of length `l-1`, hence of
length one or two.  Reversing the component preserves this statement, and
changing either outside connector cannot touch either internal zero
boundary.  The exact D2 inversion theorem requires every strict internal
run of `Z` to have length at least three.  Thus any one of these runs is an
obstruction; there are `724` of them.  \(\square\)

Consequently the next model must contain genuine internal rethread or
occurrence-variant columns.  If the owner bank is held at exactly `4108`
tokens, every residual component stays in the facet bank, and every actuator
is confined to one old component, at least one nonidentity option is required
in each of the `257` defective components.  If the authenticated packet need
only remain an intact subpath and the owner bank may grow, a length-three-only
component can instead be migrated wholesale into the owner bank; the exact
scalar relaxation then gives the separate `106`-variant floor described
below.  Neither lower bound is asserted for partial-macro or multi-component
actuators.

### Corollary 1.2 (slot-neutral/wholesale scalar floor)

Of the `257` components, `82` contain a length-two run and hence fail in
either bank; they require a genuine variant.  There are `175` further
components having length-three but no length-two run.  Moving all `175`
unchanged into one enlarged owner path costs

\[
 \sum_C(|w_C|+1)=4928
\]

owner slots: `|w_C|` owner tokens and one new connector for each added
component.  Only `7401-4108=3293` slots are available.  Thus at least `1635`
cost must instead be removed by variants.  The 23 largest component costs
sum to `1598`, while the 24 largest sum to `1637`.  Therefore at least

\[
                         82+24=106
\]

components require variants in this relaxed component-local model.

This is an exact necessary scalar floor, not a sufficiency statement.  It
optimistically assumes that every wholesale migration can be joined
residence-safely and spends no short cell on an auxiliary pin.  Connector,
upper-shadow, or common-cap constraints can only increase the floor.  If the
owner bank must remain exactly the frozen `4108` tokens, the applicable floor
is `257`, not `106`.

## 2. The minimal exact directed component master

The formulation below is useful after an admissible regenerated component
atlas has been supplied.  Contract the fixed marked packet path to a
distinguished component `C_*`.  Every component `C` has two occurrence
half-sockets `H(C)`.  Isolated port components have two distinct socket
occurrences with the same rank-eight label.  Write `lambda(h)` for the
physical port label of a socket.

For each residual owner `U` and ordered socket pair `(h,h')`, make a binary
column

\[
 x_{U,h\to h'}
\]

exactly when `lambda(h)` and `lambda(h')` are distinct facets of `U`.
The owner label is then forced:

\[
             U=\lambda(h)\cup\lambda(h').                 \tag{2.1}
\]

Use the rows

\[
 \sum_{h,h'}x_{U,h\to h'}=1                              \tag{2.2}
\]

for every residual owner,

\[
 \sum_{U,h'}\bigl(x_{U,h\to h'}+x_{U,h'\to h}\bigr)=1    \tag{2.3}
\]

for every socket occurrence, and

\[
 \sum_{h\in H(C),U,h'}x_{U,h'\to h}=1,
 \qquad
 \sum_{h\in H(C),U,h'}x_{U,h\to h'}=1                   \tag{2.4}
\]

for every component.  At `C_*`, fix which marked endpoint is the incoming
socket and which is the outgoing socket; solve the globally reversed marked
orientation as the second case.  Finally impose the directed subtour cuts

\[
 \sum_{\substack{h\in H(C),\ C\in X\\h'\in H(D),\ D\notin X\\U}}
        x_{U,h\to h'}\ge1
 \quad(\varnothing\ne X\subsetneq\mathcal C).             \tag{2.5}
\]

Rows (2.2)--(2.5) are an exact directed Hamilton-cycle model on contracted
components.  No position or ordering variables are required.  Removing
`C_*` from a feasible solution gives the oriented complementary component
path, and the orientation of every component is forced by its incoming
socket.

For a regenerated atlas, add component-option variables `v_(C,theta)` and
one-choice rows.  Every owner, lower-colour, occurrence, and optional-macro
resource changed by an option must also have an exact set-partition row.
This is necessary: marginally legal variants can otherwise reuse one owner
or one lower colour.  Socket columns are guarded by their selected option.

## 3. Facet-block factorization

For an oriented nonempty component owner word

\[
 q_1,\ldots,q_s
\]

with entry and exit ports `t_0,t_s`, define

\[
 \Phi(C)=
 (t_0,q_1\cap q_2,\ldots,q_{s-1}\cap q_s,t_s).            \tag{3.1}
\]

For an isolated component at port `t`, put `Phi(C)=(t)`.  If the residual
component order is `C_1,...,C_4871`, then the complementary facet bank is

\[
 F=(t_*^{out})\,\Vert\,\Phi(C_1)\,\Vert\cdots\Vert
      \Phi(C_{4871})\,\Vert\,(t_*^{in}).                  \tag{3.2}
\]

### Lemma 3.1 (connector-label elimination)

Formula (3.2) is exact and is independent of the extra coordinate of each
selected residual owner.  The connector labels enter only through the
legality and all-different rows (2.1)--(2.2).

#### Proof

At a nonempty component boundary, a connector owner and the first or last
component owner are distinct rank-nine sets sharing the indicated
rank-eight port, so their intersection is that port.  At an isolated
component, its two distinct incident connector owners share exactly the
same rank-eight port.  This gives (3.1)--(3.2).  \(\square\)

This factorization is the reason the directed component master is the
smallest useful outer model: once its arcs are chosen, the entire literal
row `Z=P||F`, not merely the owner cycle, is determined.

## 4. Exact local and lazy rows

### 4.1 Eager/internal rows

Reject every component option whose `Phi` block already has a strict
internal coordinate run of length below three, or whose internal maximal
three-window envelope is empty or fails replay.  Theorem 1.1 says the
current fixed atlas is rejected here.

For surviving options, concatenate by (3.2).  Across selected seams enforce

\[
 E_p=\bigcap_{i:\,i\le p\le i+2}Z_i\ne\varnothing,
 \qquad E_i\cup E_{i+1}\cup E_{i+2}=Z_i.                  \tag{4.1}
\]

These are bounded-collar constraints.  Equivalently, use the four-state
per-coordinate run automaton `0,1,2,3+`, together with the literal
three-token nonempty-intersection test.  A violating run has a `0-1-0` or
`0-1-1-0` collar and therefore yields a local guarded no-good.

There is no independent D3 master row: exact D2 replay (4.1) implies that
every strict internal run in `DZ` has length at least four.  D3 replay is a
useful audit but is redundant in the smallest exact model.

### 4.2 Lazy upper-shadow rows

For every target `S` of rank at least ten, scan `Z` with the deterministic
accumulated-union automaton

\[
 r\mapsto
 \begin{cases}
  \varnothing,&z\not\subseteq S,\\
  r\cup z,&z\subseteq S,
 \end{cases}                                             \tag{4.2}
\]

with an absorbing accepting state when `r=S`.  A consecutive interval has
union `S` if and only if this automaton accepts: every such interval lies in
one maximal run of tokens contained in `S`, and conversely the accumulated
union of such a run supplies an interval once it first reaches `S`.

Each oriented `Phi` block has a precomputable transfer map for (4.2).
Install the product-flow/table rows only for targets missed by the current
incumbent.  This is an exact arbitrary-width separator; replacing it by
fixed q-edge witnesses is not valid.

Concretely, for an installed target use one state-labelled variable
`eta_(e,r)` on every selected directed component arc and one local turn
variable `w_(C,e,f,r)` for an arc `e` entering `C`, an arc `f` leaving `C`,
and input state `r`.  Marginalizing `w` gives the selected incoming and
outgoing arc variables, while its output state is forced to
`delta_(S,C,orientation(e))(r)` and equals the state label carried by `f`.
The source state is the result of scanning the fixed marked prefix and the
first cross facet; the sink state, after the final cross facet, must be
accepting.  These are ordinary flow/table equalities on the component path.
They are complete because (2.5) leaves one directed path after `C_*` is
removed.

### 4.3 Exact common-cap recourse

Once an outer solution fixes `Z`, compute its maximal envelope `E` and any
short prepins.  Here the direct rank-eight palette has `20203` distinct
rows, the residual lower family has `45332` targets, and there are `48625`
singleton/adjacent-pair cells.

For every individually feasible target--cell incidence `(S,J)`, introduce
`y_(S,J)`.  Impose one incidence per target, at most one per cell, and every
bad-pair/bad-triple row from the exact rank-three common-cap obstruction
clutter.  This recourse is necessary and sufficient; ordinary marginal
Hall is not.

The proof-safe decomposition is therefore:

1. directed component/variant master (2.2)--(2.5);
2. local D2-envelope separation (4.1);
3. arbitrary-width upper automata (4.2);
4. exact rank-three cap recourse.

If cap recourse fails, a full outer-selector no-good is always sound.  A
smaller generalized Benders row is sound only when every position/envelope
literal used by the extracted cap core is guarded by the component and seam
columns that determine it.  No equivariant or aggregate compiler covariance
may be assumed.

## 5. Conditional physicalization theorem

### Theorem 5.1

Assume a regenerated complementary component atlas and selections `v,x,y`
satisfy all exact resource rows, (2.2)--(2.5), (4.1), every upper automaton,
and the exact common-cap recourse.  Assume the fixed marked bank remains the
authenticated `4108`-owner OPTIMAL28 bank.

Then the maximal cap word has length

\[
                         24313.
\]

It covers every nonempty subset of `[17]`: rank-nine owners are split
between the direct marked bank and `DZ` on the complement; all rank-eight
targets are either direct facet rows or residual common-cap targets; all
lower ranks are covered by the same injective cap matching; and every upper
rank is covered by an interval fixed by `Z`.  Thus, together with the known
lower bound, it is an optimal K17 word.

#### Proof

Rows (2.2)--(2.5) produce one literal lower-rainbow owner cycle with the
marked bank contiguous.  Lemma 3.1 gives the exact two-bank zipper row.
Equation (4.1) gives its maximal nonempty physical cap and makes every
length-at-least-three interval depend only on `Z`.  The upper automata cover
all such targets.  Exact cap recourse covers every remaining singleton/pair
target without destroying `Z`, the prepins, or its selected lower witnesses.
These target families partition all nonempty Boolean masks.  \(\square\)

The theorem is conditional.  The new substantive gate is a regenerated
component atlas which removes the `724` immutable facet-run defects while
retaining enough socket arcs to satisfy the directed owner rows, upper
automata, and one asymmetric common-cap recourse.  Direct radius-two
occurrence changes are a valid fallback source of such atlas columns; the
saved connected pairing by itself is not.

## 6. Frozen provenance

```text
scratch/ad_k17_opt28_residual_connected_bflow_20260731.json
SHA-256 b3cbb0663409463cb24a2ed78db154cc88a042b633e979cba3506ba74e610ef6
payload a117a304f277a7746405814786fd3f593dffe5073443431582eb711641e7319a

scratch/k17_opt28_connected_owner_cycle_20260731.word
SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa

scratch/k17_opt28_connected_owner_cycle_20260731.audit.json
SHA-256 f28924a629a6e858571119538639adf3ecbd4d186c1014a475e353fe5b719280
payload 6988b37a414a516e4645f81b1dac87618c1949bc636a1190462c5f8520639d7a

scratch/ad_k17_opt28_twobank_d2_row_20260731.zrow
SHA-256 18675acb0083aa7fea8e1505f871cc70b23a9261e6f59662cb9df87ca703a211

scratch/ad_k17_opt28_twobank_d2_row_20260731.audit.json
SHA-256 81f0e403367ee0e32c0ac63404cebd2e87a3a2a9602475b01b3a3927c4c9cf20
payload 591ef216c6c4d818e604ccad9d149ab6ab66c0fa6a124a3d8bc5382c2185726d

scratch/audit_threadD_k17_opt28_component_cap_floor_20260731.py
SHA-256 5408ce116710f37c5f812f5707f0f6603e730142149ac24b8b8b045ee393f3f1

scratch/threadD_k17_opt28_component_cap_floor_20260731.audit.json
SHA-256 48bc1e3302e8b05b7d320f78454e63a8bd71268358655a503c2a9b525d25eeda
payload 98753c506595f0b0cf3978d03b315b08b9b6c31d9ab9da40e94cf6033e0f8b3e
```

The `724/257` invariant was obtained by a literal scan of the `4871`
unselected `owner_word` arrays in
`scratch/k17_sixswap_macro_forest_20260731.flow.json`, after removing
`marked_component_ids` and the `28` `optional_components` in the saved
OPTIMAL28 path result.  The scan is linear in the `19305` stored macro-owner
tokens and uses no search.
