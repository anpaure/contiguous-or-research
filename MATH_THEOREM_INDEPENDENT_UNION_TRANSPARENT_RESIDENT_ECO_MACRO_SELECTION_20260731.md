# Compressed-deck-transparent resident ECO macros: exact quadratic-list and linear-conflict theorem

Date: 2026-07-31  
Lane: independent `B(k)+O(1)` packet synthesis  
Status: exact conditional macro theorem, exact selector bounds, and exact deterministic obstruction.  The missing assertion is a uniform small-star-cover/deck theorem on the actual retained Catalan paths; no unconditional additive-constant upper bound is claimed.

## 0. Verdict

The contracted all-six ECO audit supplies a real local core for the lean
packet route:

* one literal twelve-owner Johnson packet has identical full prefix/suffix
  OR signatures in its two phases;
* its internal interval-OR supports are equal, so internal-union dominance
  holds in both directions; and
* its internal interval-intersection supports are equal as a separate unary
  coverage certificate.

This closes the **local matching geometry**.  It does not automatically
close residence or the lift through the six retained path interiors.  The
coverage-level interface is weaker than the ordered signature: it requires
only old-to-new inclusion of the distinct prefix, suffix, and internal OR
decks, plus equality of the total OR.  Even under this weakening, a
fourteen-owner legal Johnson detour destroys every one of the `784` possible
old/new comparisons in both directions.  Therefore constant support and the
positive contracted connector do not imply a quadratic eligible list.

There is nevertheless one stronger positive lift.  Subdivide all six edges
of the good connector by the canonical midpoint
`Z_XY=(X union Y)-q`.  The resulting eighteen-owner old/new cycles have equal
external signatures, equal internal OR and intersection supports, and no
positive singleton runs.  Their opening boundary records differ, and six
`q`-runs have length exactly two, so this closes the intrinsic no-singleton
macro but not the exterior-independent or growing-`d` residence row.

The strongest proof-safe result is the following.  For one `m by m` menu of
labelled choices `(b,c)`, put every failure of

1. the retained-fragment compressed prefix/suffix deck test,
2. residence and its clipped boundary state,
3. internal-union dominance,
4. fixed connector/topology compatibility, or
5. the fixed unused-cell compiler condition

into one bipartite **unary bad graph** on the `b`- and `c`-labels.  If that
graph has a vertex cover of size at most `K d`, then at least

\[
                             m^2-Kmd                         \tag{0.1}
\]

complete union-transparent resident macros remain.  If every macro has at
most `s d+s_0` conflict-bearing tokens and each token has external load at
most `kappa m`, then

\[
                  \Delta\le \kappa m(sd+s_0)=O(md).          \tag{0.2}
\]

Thus quadratic lists beat the conflict row whenever `d=o(m)`.  For a fixed
number `H` of reachable tasks, elementary greedy selection already suffices;
for a dispersed task family, the aggregate load version gives Haxell.

The exact missing deterministic theorem is now narrow:

> prove that the actual retained-path deck/residence/fixed-basis
> failures have one global `O(d)` star cover at every reachable anchor, and
> that the assigned anchors obey the external token-load code.

Neither statement follows from the all-six ECO genealogy, common endpoint
set, or `O(d)` support.

## 1. The local core supplied by the six-seam audit

Use the twelve owners and the common Johnson connector `M_*` of
`MATH_THEOREM_INDEPENDENT_ECO_SIXSEAM_SIGNATURE_CONNECTOR_AND_FRAGMENT_LIFT_20260731.md`.
After cutting one common connector edge, its old and new words `W_0,W_1`
have length twelve, the same first and last owners, and

\[
                          \Sigma_\vee(W_0)=\Sigma_\vee(W_1).   \tag{1.1}
\]

Moreover

\[
                    \operatorname{Int}_\vee(W_0)
                     =\operatorname{Int}_\vee(W_1),            \tag{1.2}
\]

and the analogous sets of internal interval intersections agree.  Equation
(1.2) is stronger than the one-way internal dominance required by the lean
packet theorem.  It is only a support equality: OR multiplicities exchange
five units and intersection multiplicities exchange two units.

Every coordinate relabelling and fixed common suspension preserves
(1.1)--(1.2).  Hence every coherent all-six atom for which the six connector
edges are available has one raw union-transparent core of this type.  This
does not say those edges are simultaneously free in one prepared forest or
that the twelve-letter core is resident at the required erosion depth.

## 2. Exact lift through retained path interiors

Delete the six changed seams from a common pre/post connector chronology.
The common part consists of six retained paths paired on the twelve changed
owners.  After choosing a linear opening, split one path if the opening lies
inside it.  The old and new slots have the form

\[
 X_i=F_{\pi_i(1)}^{\epsilon_{i,1}}\cdots
     F_{\pi_i(s)}^{\epsilon_{i,s}},\qquad i=0,1,      \tag{2.1}
\]

with `s=6` or `7`.  The fragments are common; only their order and
orientation differ.

For every coordinate `z`, an oriented fragment may export its length and

\[
 f_F(z)=\text{first occurrence},\qquad
 \ell_F(z)=\text{last occurrence}.                   \tag{2.2}
\]

Offset these times by the total lengths of preceding fragments and take the
minimum and maximum over all fragments.  Call the resulting global pair
`tau_i(z)`.  The exact occurrence-time theorem gives

\[
                     \Sigma_\vee(X_0)=\Sigma_\vee(X_1)
       \quad\Longleftrightarrow\quad
                     \tau_0(z)=\tau_1(z)\quad\text{for every }z. \tag{2.3}
\]

Thus pointwise arbitrary-width crossing transport reduces to one finite
unary test on the supplied retained paths.  It is sufficient but stronger
than coverage requires.

For the sharp coverage-level interface, define the distinct decks

\[
\begin{aligned}
 \mathcal P(X)&=\{X_1\cup\cdots\cup X_j:1\le j\le |X|\},\\
 \mathcal S(X)&=\{X_j\cup\cdots\cup X_{|X|}:1\le j\le |X|\},\\
 \mathcal I(X)&=\{X_i\cup\cdots\cup X_j:1\le i\le j\le |X|\}.
                                                               \tag{2.4}
\end{aligned}
\]

The compressed-deck replacement theorem says that every old interval-union
value survives in every exterior context provided

\[
 \mathcal P(X_0)\subseteq\mathcal P(X_1),\quad
 \mathcal S(X_0)\subseteq\mathcal S(X_1),\quad
 \mathcal I(X_0)\subseteq\mathcal I(X_1),\quad
 \bigcup X_0=\bigcup X_1.                           \tag{2.5}
\]

This discards plateau timings.  The two nested external decks have at most
`O(|X_i|)` distinct values, while the potentially `Theta(|X_i|^2)` internal
test is unary and contributes no cross-packet conflict token.

### Lemma 2.1 (one arbitrary retained path is externally free)

The explicit connector `M_*` has one distinguished common edge `X_cV_c`
which occurs in the same position and orientation in the two words.  Replace
that edge by **any** common owner path

\[
                         F=(X_c,\ldots,V_c).           \tag{2.6}
\]

Define

\[
\begin{aligned}
 W_0(F)={}&(U_{ab},V_b,Y_{bc})\,F\,
   (U_{bc},U_{ca},V_a,Y_{ca},X_a,X_b,Y_{ab}),\\
 W_1(F)={}&(U_{ab},V_a,Y_{ca})\,F\,
   (U_{ca},U_{bc},V_b,Y_{bc},X_b,X_a,Y_{ab}).        \tag{2.7}
\end{aligned}
\]

Then

\[
                         \Sigma_\vee(W_0(F))
                          =\Sigma_\vee(W_1(F))        \tag{2.8}
\]

for every `F`, even when its interior uses fresh coordinates.

#### Proof

Before `F`, the two prefix chains are respectively generated by

\[
 (U_{ab},V_b,Y_{bc})\quad\hbox{and}\quad
 (U_{ab},V_a,Y_{ca}),                                \tag{2.9}
\]

and direct union gives the same value at each of the three positions.  At
and inside `F`, the entering union is therefore equal and the same oriented
prefix of `F` is added.  The first owner `X_c` supplies the sole missing
active label `d`, so after entering `F` the accumulated union contains every
owner in either displayed suffix; later prefixes are equal as well.

From the right, the two seven-owner suffixes in (2.7) have identical ordered
suffix-union chains by the literal table in the six-seam audit.  At and
inside `F`, the same oriented suffix of `F` is added to equal entering
unions.  Before `F`, its total union plus the suffix total masks the remaining
prefix difference.  This proves (2.8).  \(\square\)

Lemma 2.1 removes the external-deck test for one of the six retained paths.
It does **not** imply internal dominance: intervals beginning on different
sides of `F` see different local contexts.  The aligned fresh-marker detour
retains the pointwise external signature but fails the internal deck row.
Nor does one padded path alone force residence of every active coordinate.

### Proposition 2.2 (fresh padding and internal dominance coexist)

The preceding failure is not universal.  In the rank-four model on the
eight coordinates

\[
                       \{e,a,b,c,d,\infty,q,p\},       \tag{2.9a}
\]

enumerate simple Johnson paths from `X_c` to `V_c` which avoid the other ten
fixed packet owners.  There are `29` such paths of three edges and `280` of
four edges.  Respectively `15` and `192` use the fresh coordinate `p` in an
interior owner.  Among the fresh paths, no three-edge path satisfies internal
old-to-new deck dominance, while exactly `24` four-edge paths do.  For
example,

\[
  F=(\mathtt{0x59},\mathtt{0x1d},\mathtt{0x2d},
       \mathtt{0xa9},\mathtt{0x69})                    \tag{2.9b}
\]

is a Johnson path from `X_c` to `V_c`, uses `p`, and gives

\[
 \mathcal I(W_0(F))\subseteq\mathcal I(W_1(F)),
 \qquad |\mathcal I(W_0(F))|=35,
 \quad |\mathcal I(W_1(F))|=36.                       \tag{2.9c}
\]

Here the displayed `I` decks are the full distinct interval-OR decks; Lemma
2.1 supplies equality of the ordered external prefix and suffix chains, so
(2.9c) is exactly the remaining unary internal row.  Thus U1 and U2 can hold
simultaneously on a nontrivial retained path with fresh support.

There is also a sharper warning.  Six of these `24` paths are themselves
minimum-run-two clean (they have no internal positive singleton), so padding
and its deck are not the obstruction.  Rather, in **both** packet phases the
seven fixed owners to
the right of `F` have coordinate-`c` pattern

\[
                              1101000.                \tag{2.9d}
\]

The isolated fourth `1` is an internal singleton independently of the length
and contents of `F`.  Consequently no choice of this **single** padded edge
can make (2.7), with its other connector edges contracted, satisfy even the
no-singleton part of U3.  Longer `F` cannot fix it; one must additionally
expand the relevant suffix connector edge, or change the connector, opening,
or surrounding anchor pattern.  This is a no-go for the one-padded template,
not for the full `m by m` ECO menu.

### Proposition 2.3 (a closed union-transparent no-singleton macro)

The obstruction in (2.9d) disappears when all six common connector edges are
lifted coherently.  Suspend every contracted owner by one common coordinate
`q`.  For every edge `XY` of the literal connector `M_*`, subdivide it by

\[
                         Z_{XY}=(X\cup Y)\setminus\{q\}.       \tag{2.9e}
\]

Every `X,Z_{XY},Y` is a Johnson two-edge path: `X` and `Y` differ in one
non-`q` coordinate, while `Z_{XY}` exchanges `q` with the coordinate present
at the other endpoint.  The six midpoints are distinct.  Cutting the common
half-edge from `U_{ab}` to `Z_{U_{ab}Y_{ab}}` gives the following old and new
words, in hexadecimal coordinates ordered as
`(e,a,b,c,d,infinity,q,p)`:

```text
old = 27 47 55 17 53 4b 2b 63 6a 2e 6c 69 39 59 4d 2d 65 66
new = 27 47 53 17 55 4d 2d 65 6c 2e 6a 69 39 59 4b 2b 63 66
```

All eighteen owners are distinct rank-four sets and consecutive cyclic pairs
are Johnson-adjacent.  The two linear words have identical ordered
prefix/suffix OR signatures.  Their full distinct interval-OR supports are
equal (size `32`), and their full interval-intersection supports are equal
(size `48`).  In each cyclic word every positive coordinate run has length at
least two.  Explicitly, the old run-length multisets are

```text
e: 6,8       a: 7,3       b: 2,8       c: 2,8
d: 3,2       infinity: 7,4             q: 2,2,2,2,2,2
```

and the new word swaps the `a` and `b` profiles while leaving the others
unchanged.  Hence this is a literal dimension-uniform (under common
suspension) union-transparent, internally bank-transparent,
minimum-run-two ECO macro.

It is not on the strong unary U3 face.  Across every resident
deck-dominating opening in the complete one-midpoint catalogue, the clipped
old/new boundary records differ.  For the displayed opening, a common
predecessor containing `infinity` and a common successor containing `a,b`
complete both boundary runs; cyclic closure is the simplest such joint
interface.  Thus Proposition 2.3 satisfies the more general tokenized-halo
version of U3 using two boundary requirements, not exterior-independent
off-state equality.

Nor does it scale to the actual growing residence depth.  In particular `q`
has six positive runs of length exactly two.  Merely lengthening the
`q`-free midpoint detours leaves those six runs unchanged.  A scalable macro
must put `q` into the connector interiors or braid several changed-endpoint
pairs into one longer resident rail.  This is now the exact local
construction target; crossing-union and internal-bank compatibility are no
longer the obstruction at minimum run two.

For residence depth `d`, define the **resident boundary state** of a word to
contain, for every coordinate:

1. every internal positive run of length at most `d`;
2. the positive prefix-run length clipped at `d+1`; and
3. the positive suffix-run length clipped at `d+1`.

A candidate is resident relative to the fixed exterior exactly when it has
no forbidden internal run and its two clipped boundary states are compatible
with the fixed exterior runs.  Equality with the off-state boundary record
is a convenient stronger sufficient condition.  This test is also unary
once the exterior and opening are fixed.

The physical support is `O(d)` only under an explicit length/ticket bound:

\[
                |X_0|=|X_1|\le s_wd+s_w^0,qquad
                |\operatorname{Tok}(X_0,X_1)|\le s_td+s_t^0.  \tag{2.10}
\]

Neither occurrence-time nor deck compression shortens a long retained path.
If (2.10) is absent, the macro is not a bounded-support packet even though its
boundary decks can be stored compactly.  Per-coordinate residence metadata
and the unary internal-deck computation may have larger certificate size;
`Tok` counts only resources that can conflict with another packet.

## 3. Complete unary macro predicate

Fix one task anchor with parameter sets `B,C`, each of order `m`.  For every
`(b,c) in B times C`, let `(X^0_bc,X^1_bc)` be a proposed expanded ECO
packet relative to one common off-state.  Call it **UTR-lean eligible** when
all of the following hold.

**U1 (compressed external decks).**  The two slots have equal length, obey
(2.10), have equal total union, and satisfy

\[
          \mathcal P(X^0_{bc})\subseteq\mathcal P(X^1_{bc}),\qquad
          \mathcal S(X^0_{bc})\subseteq\mathcal S(X^1_{bc}).     \tag{3.1}
\]

**U2 (internal upper dominance).**

\[
          \mathcal I(X^0_{bc})\subseteq\mathcal I(X^1_{bc}).    \tag{3.2}
\]

An optional internal-intersection bank is recorded separately; it is not
inferred from U1.

**U3 (residence-neutral boundary).**  The on-slot has no forbidden internal
positive run.  For every coordinate, its leading and trailing positive-run
lengths clipped at `d+1`, its two boundary bits, and its whole-fragment flag
equal the off-slot records.  This stronger equality makes residence compose
against every fixed exterior.  More general merely compatible boundary
records require pairwise-disjoint `d`-halos or an explicitly tokenized joint
interface and are outside this unary face.

**U4 (subset-closed common topology).**  Both phases have the same typed
boundary relation and belong to one prescribed connector/path cube in which
**every subset** of selectable slot replacements is a legal forest/path with
the declared endpoints.  Equivalently one may supply a separate exact global
graphic certificate.  Pairwise-safe connectors alone do not satisfy U4,
since three such connectors can form a cycle.

**U5 (lean common cap).**  One fixed trace-guarded compiler matching `M_0`
covers all required targets.  The packet changes no incidence of `M_0` and
deletes only one named cell in its unused-cell dual basis.  The deletion-cell
name is exported as a conflict token.

U1--U5 are unary relative to the fixed off-state and fixed subset-closed
skeleton.  For pairwise-disjoint slots, distinct deletion cells, and the
declared interface guards, the lean composition theorem then preserves every
old upper target, residence, topology, and the matching `M_0`.

Let `G_bad` be the bipartite graph on `B sqcup C` whose edges are exactly the
pairs failing at least one of U1--U5.  This union is important: separate
`O(d)` exceptional label sets for the five rows do not help unless their
union is still `O(d)`.

### Theorem 3.1 (exact quadratic eligible list)

If

\[
                         \tau(G_{bad})\le Kd,          \tag{3.3}
\]

then the eligible macro list has size at least `m^2-Kmd`.  In particular,
for `d=o(m)` it has size `(1-o(1))m^2`.

The hypothesis is checkable exactly by a maximum matching in `G_bad`.

#### Proof

By Koenig's theorem, (3.3) gives a vertex cover `Q` of at most `Kd` labels.
Every bad pair is incident with `Q`, and every label is incident with at most
`m` pairs.  Hence

\[
                         |E(G_{bad})|\le m|Q|\le Kmd. \tag{3.4}
\]

Delete those pairs from the `m^2` raw choices.  \(\square\)

A convenient stronger certificate is to exhibit global label sets
`F_B,F_C` with total size at most `Kd` such that every pair outside

\[
                 (F_B\times C)\cup(B\times F_C)       \tag{3.5}
\]

passes all five rows.  In deck language, this says that every missing
prefix/suffix/internal value, every short-run failure, and
every fixed-basis/topology failure is charged to one common active label
set.  It is the exact profile analogue of the protected-ray star-cover
criterion.

## 4. Cross-list row energy and selection

Let there be packet lists `P_1,...,P_H`, already pruned by Theorem 3.1.  Put

\[
                          S_d=s_td+s_t^0.             \tag{4.1}
\]

Every packet uses at most `S_d` conflict-bearing tokens, including its
physical slot, external deck values, interface state, and unused-cell
deletion token.  The internal deck comparison is unary and is not tokenized.
Source-fixed tokens are assumed private between different lists.

The tokenization is **complete**: after U1--U5 and the subset-closed skeleton
have removed every higher-order row, every incompatible pair of options from
different lists shares at least one counted token.  Without this hypothesis
the union bounds below control only a subgraph of the true conflict graph.

### Theorem 4.1 (bounded-task row)

Assume that, for every token `r` used by a packet in list `i` and every
other list `j`, at most `kappa m` members of `P_j` use `r`.  Then

\[
 \delta_{ij}:=\max_{p\in P_i}|N(p)\cap P_j|
       \le \kappa mS_d,                              \tag{4.2}
\]

and the external row energy of list `i` is at most

\[
 R_i={1\over|P_i|}\sum_{p\in P_i}\deg_{ext}(p)
       \le(H-1)\kappa mS_d.                          \tag{4.3}
\]

Consequently a greedy transversal exists whenever

\[
              m^2-Kmd>(H-1)\kappa m(s_td+s_t^0).     \tag{4.4}
\]

For fixed `H,K,kappa,s_t,s_t^0` and `d=o(m)`, (4.4) holds eventually.

#### Proof

For one packet, take the union of the at-most-`kappa m` conflicting choices
in list `j` contributed by each of its at-most `S_d` tokens.  This proves
(4.2).  Sum over the `H-1` other lists and average to get (4.3).  After
`r<H` greedy choices, fewer than `r kappa mS_d` members have been deleted
from the next list, so (4.4) leaves a choice.  \(\square\)

### Theorem 4.2 (dispersed-task/Haxell row)

Assume instead the stronger aggregate load condition: every token in one
packet occurs in at most `kappa m` choices over **all other lists combined**.
Then the complete conflict graph has

\[
                        \Delta\le\kappa mS_d=O(md),   \tag{4.5}
\]

and every list has the same upper bound on its external row energy.  Haxell
selects one macro per list whenever

\[
                       m^2-Kmd\ge2\kappa mS_d.        \tag{4.6}
\]

Again `d=o(m)` makes (4.6) automatic eventually.

#### Proof

The token union bound gives (4.5).  Apply the independent-transversal theorem
to the complete fixed-skeleton conflict graph.  \(\square\)

The aggregate premise is precisely where the weighted anchor code is used:
source-fixed roles must be private, one-free roles occur at `O(1)` selected
anchors, and zero-free roles at `O(m)` selected anchors.  Local ECO geometry
does not prove that code for cap or topology tokens.  On the UTR-lean face,
one common connector and one fixed `M_0` remove the global cap-path choice;
only the named deletion-cell capacity remains.

## 5. Exact deterministic obstruction from a legal retained detour

The star-cover/profile hypothesis cannot be deleted.  Start from the
explicit positive connector `M_*`.  Choose

\[
                   q\in H-\{e\},\qquad
                   p\notin H\cup\{a,b,c,d\},          \tag{5.1}
\]

with `p` distinct from the distinguished `infinity` coordinate.  This is
possible from side parameter `m>=4`.  Replace the common connector edge

\[
                         V_bY_{bc}                    \tag{5.2}
\]

by the common retained Johnson path

\[
 V_b,\quad V_b-q+p,\quad Y_{bc}-q+p,\quad Y_{bc}.   \tag{5.3}
\]

Every step in (5.3) exchanges one coordinate.  Both old and new phases are
still Hamilton cycles on the same fourteen owners, use the same retained
path, and differ only in the six ECO seams.

Nevertheless there is no cut and no orientation for which the old compressed
prefix, suffix, and internal decks are contained in the new decks--and none
in the reverse direction.  There are `28` linearizations of each cycle; the
dependency-free audit checks all `28^2=784` directed pairs in both directions.
In particular every pair also fails the stronger pointwise signature and
differs in the first/last occurrence time of at least one of

\[
                       e,a,b,c,d,\infty,q,p.           \tag{5.4}
\]

Thus one legal constant-length common-path expansion destroys the contracted
signature completely.  The endpoint matching, degree vector, support size,
and changed-seam count are unchanged.  This proves:

\[
 \boxed{\text{contracted deck transparency + }O(d)\text{ support}
        \not\Longrightarrow\text{U1}.}               \tag{5.5}
\]

Two other unary implications also fail independently.

* Equal boundary signatures do not imply internal dominance:
  `(1,2,1)` and `(1,3,1)` have the same prefix/suffix OR chains but lose the
  internal singleton target `2`.
* U1 and U2 do not imply residence: a positive coordinate run of length at
  most `d` wholly inside the common retained path rejects the candidate in
  every exterior context.

Accordingly, the exact deterministic obstruction to Theorem 3.1 is a large
matching in the **union** of the five unary bad graphs.  By Koenig, a
matching of order `omega(d)` proves that no `O(d)` star-cover certificate
exists.  Current Catalan/ECO theory gives neither a bound on this matching
nor a counterexample of that order in the actual reachable atlas.

## 6. Implication for the additive-constant program

Combine Theorems 3.1 and 4.1 with a bounded phase-resolved task ledger and a
regenerative bounded sidecar.  If every reachable task has the UTR-lean
star-cover certificate, the same fixed connector and trace-guarded matching,
and the per-other-list token bound, then every step has quadratic menus,
`O(md)` exclusions, and a literal compatible macro choice.  The lean packet
composition theorem preserves upper coverage and the common cap.  The
existing bounded-sidecar induction then gives `B(k)+O(1)` along the covered
spine.

Alternatively, Theorems 3.1 and 4.2 feed the dispersed-task route after a
weighted-code task-to-anchor assignment.

No premise in that implication is silently supplied here.  In particular,
the note does not prove:

1. that every reachable ECO occurrence admits a deck-dominating resident
   `O(d)` expansion;
2. the global `O(d)` star cover across U1--U5;
3. a common trace-guarded compiler matching with enough distinct unused
   deletion cells; or
4. the complete external token-load code on the actual assigned anchors.

The gain is that these are now the only quantitative packet rows.  Arbitrary
upper widths no longer occur in the conflict degree once U1 and U2 hold.

## 7. Frozen audit

The contracted positive core and its complete connector census are audited
by

```text
scratch/audit_independent_eco_sixseam_signature_connectors_20260731.py
```

The retained-path obstruction is independently replayed by

```text
scratch/audit_independent_eco_signature_marker_detour_20260731.py
```

which reports

```text
PASS_ECO_MARKER_DETOUR_COMPRESSED_DECK_NOGO
```

and writes

```text
scratch/independent_eco_signature_marker_detour_20260731.audit.json
```

with canonical payload SHA-256

```text
717b3c39b979d247126a495f9090eb907ea4b90da7b8544cd5d14f8ac815e7df
```

Frozen file SHA-256 values are

```text
scratch/audit_independent_eco_signature_marker_detour_20260731.py
  8d85300da50327a0b99d830b044270287b4d816bc1914a8a9f4e42bbd74b7c17
scratch/independent_eco_signature_marker_detour_20260731.audit.json
  3fcd63c04916fe8ed5e3f6b560e778bee9db68723e2d632db25e0504c5912789
```

The positive aligned-padding calibration is replayed by

```text
scratch/audit_independent_eco_aligned_padding_channel_20260801.py
  dc1dc72e8a013ad2f51e47a6af4e981d60e127cae27644d1133703e33806936f
scratch/independent_eco_aligned_padding_channel_20260801.audit.json
  8b2d1db0d737161a3ee7a3179e464f06bdf415e2fa15e81c1e7802bd9a720504
```

It reports `PASS_ECO_ALIGNED_PADDING_EXTERNAL_SIGNATURE`, finds the two
reverse-equivalent pointwise external-signature witnesses, and confirms that
the same fresh-marker padding has zero directed internal-deck dominations.
Its canonical payload SHA-256 is
`1d9e0fde8f7664ba48cecb7189fa032dd1886df5884389f8bf235dbc7f5e8b19`.

The complete short-path census behind Proposition 2.2 is replayed by

```text
scratch/audit_independent_eco_aligned_internal_dominance_paths_20260801.py
  b5709057670b0318129c987f90b598eb1068e4e0f75dddd5669389ea194489e2
scratch/independent_eco_aligned_internal_dominance_paths_20260801.audit.json
  7b2ee90103baec91e13327bf2c85da6ea46951c34a61521dd0f6d9fdc1e2a41b
```

It reports `PASS_ECO_ALIGNED_INTERNAL_DOMINANCE_PATH_CENSUS`.  Of the
`280` safe four-edge paths, `192` use the fresh coordinate and `24` give
old-to-new full interval-OR deck dominance.  Six of those paths are
minimum-run-two clean internally, but the invariant fixed-suffix pattern
`1101000` forces the one-padded macro to fail residence for every `F`.  Its
canonical payload SHA-256 is
`2f2552f0f6a4dcd7c851b94fa9e39b9322561fc0c9da319f885ba5aa98cbf4ae`.

The complete one-midpoint expansion of all six literal connectors, including
Proposition 2.3, is replayed by

```text
scratch/audit_independent_eco_sixedge_midpoint_resident_macro_20260801.py
  aec0d460bedbc1efa5f4db2678d61756e823a69816d08baac1e92c3ce3c84857
scratch/independent_eco_sixedge_midpoint_resident_macro_20260801.audit.json
  e7b305162bd729d220d6a83e068f28d5eb279d9da4fae01c9ad9f3e6123188d6
```

It reports `PASS_ECO_SIXEDGE_MIDPOINT_RESIDENT_TRANSPARENT_MACRO`.  Connector
rows `1,3,5` each have eight cyclically no-singleton midpoint assignments;
all eight admit exact external signatures and equal OR banks, six also have
equal intersection banks, and none has equal strong clipped boundary state.
Its canonical payload SHA-256 is
`e714224fb15088381b341a22ecfe8daa07986b60c214f268c29cb2e6b5f15129`.

Dependencies:

* `MATH_THEOREM_INDEPENDENT_ECO_SIXSEAM_SIGNATURE_CONNECTOR_AND_FRAGMENT_LIFT_20260731.md`;
* `MATH_THEOREM_COMPRESSED_PREFIX_SUFFIX_DECK_TRANSPARENCY_20260801.md`;
* `MATH_THEOREM_FULL_PREFIX_SUFFIX_UNION_BOUNDARY_SIGNATURE_20260731.md`;
* `MATH_THEOREM_A_BUFFERED_HEX_UPPER_RAY_STAR_COVER_AND_S1_CALIBRATION_20260731.md`;
* `MATH_THEOREM_R_BUFFERED_C6_WEIGHTED_ANCHOR_AND_TOKEN_LOAD_20260731.md`;
* `MATH_SYNTHESIS_BUFFERED_C6_TWO_ROUTE_O1_20260731.md`.
