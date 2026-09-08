# Protected extraction of resident facet sockets: exact coloured branching,
# bounded-load selection, and the remaining absorber gate

Date: 2026-08-01  
Lane: R / all-`k` `B+O(1)` and `B+1`  
Status: unconditional coloured extraction ledger, unconditional
Catalan-reservoir and bare-branching obstructions, exact Haxell and guard
criteria, and a conditional regenerative theorem.  Automatic protected
extraction from an arbitrary Catalan forest is false; no contiguous-OR word
is claimed.

Throughout the socket statements, `h>=1` and `r>=2h+1`, and `U` is a
rank-`(r+1)` target on the ambient `(2r-1)`-coordinate ground set.  Any
additional restriction is stated where it is used.

## 0. Outcome

The compact socket of
`MATH_THEOREM_RESIDENT_FACET_SOCKET_20260801.md` is an exact local accepting
block: `h+1` facets of one rank-`(r+1)` target `U` form a resident owner path
with `h` distinct lower colours.  It is not a free global repair.

Three different quantities must not be conflated.

1. The `h` internal socket edges are `h` occurrences of the **same** colour
   `U`.  Their `h-1` surplus copies are label-locked and cannot cover a
   different colour destroyed by extraction.
2. A Catalan path forest has exactly four endpoint-slot incidences per upper
   target on average.  This neither disperses the endpoints nor aligns their
   intersections with the missing lower palette.
3. Owner-facet and internal-lower conflicts are sparse when a demand bank is
   genuinely bounded-load and `h=o(sqrt(r))`; guard occurrences and coloured
   casualty restoration remain independent rows.

The strongest unconditional casualty statement is this, conditional only
on having chosen a pairwise-owner-disjoint socket bank.  For a Catalan-scale
upper leave `ell=t=C`, such bare compact sockets destroy at least

\[
                         C(h-3)+1                         \tag{0.1}
\]

distinct old immediate-upper witnesses.  Hence for every `h>=4` they create
more child demands than they repair, before guard or compiler constraints.

The exact positive target is a hereditary, occurrence-labelled absorber:
every reachable child family must admit compatible complete packets whose
weighted residual child potential contracts by a dimension-uniform factor
`rho<1`.  Endpoint count or one-target probability is insufficient.

## 1. Exact occurrence ledger

Let `\mathcal U` be the immediate-upper colour set.  For a current physical
support, let `n_V` be the number of occurrences of `V\in\mathcal U`.
Select a family `\mathcal S` of compact sockets.  Let `D` be the **union** of
old physical occurrences deleted by the selected sockets, so a shared cut
is counted once.  Let `A` be the multiset of added exterior occurrences,
excluding the internal socket edges.  For `V`, write `D_V,A_V` for the
corresponding colour fibres.

### Theorem 1.1 (coloured extraction equation)

After installing the sockets,

\[
 n'_V=n_V-|D_V|+|A_V|
       +h\,|\{s\in\mathcal S:U_s=V\}|.                 \tag{1.1}
\]

Consequently immediate-upper closure is exactly `n'_V>=1` for every `V`.
If

\[
 b_V=(1-n_V)_+,\qquad p_V=(n_V-1)_+,
\]

then the same row is

\[
 b_V+|D_V|\le p_V+|A_V|
             +h\,|\{s:U_s=V\}|.                       \tag{1.2}
\]

The signed scalar identity is

\[
 \sum_V(b'_V-p'_V)-\sum_V(b_V-p_V)
        =|D|-|A|-h|\mathcal S|.                       \tag{1.3}
\]

#### Proof

Every selected old occurrence is removed once, every exterior occurrence is
added once, and each compact socket contributes its `h` internal seams of
colour `U_s`; this proves (1.1).  Since `n_V-1=p_V-b_V`, (1.2) is a
rearrangement.  Finally `b_V-p_V=1-n_V`; summing (1.1) proves (1.3).
\(\square\)

Equation (1.2), not (1.3), is the load-bearing statement.  Surplus copies of
`U_s` occur only in the `U_s` row.  They cannot pay a child colour
`V!=U_s`.  Thus any uncoloured argument pooling `h-1` socket repeats is
invalid.

For the frozen `k=17`, `h=3`, fourteen-target calibration, the compact
sockets delete `28` distinct child colours, none a parent target.  The
scalar balance

\[
                       14+28-3\cdot14=0
\]

holds, yet the literal result has `28` child holes and `28` unusable
parent-colour repeat copies.  Only `19/28` children have even individually
projected extendable one-seam support; simultaneous segment, orientation,
degree and graphic compatibility was not proved.

## 2. Bare extraction has a sharp global branching lower bound

Put

\[
 W={2r-1\choose r},\quad
 D={2r-1\choose r+1},\quad
 C=W-D=\operatorname {Cat}_r.                         \tag{2.1}
\]

Let `F` be an upper-injective spanning path forest on the `W` rank-`r`
owners with `D-ell` edges.  It has `C+ell` components and `ell` missing
upper colours.  Choose `1<=t<=ell` missing targets and, for each, `h+1` of its
facets, with all selected owner facets pairwise distinct.  Let `S` be their
union.  Extracting the sockets removes every old edge incident with `S`.

For `v`, put `delta(v)=2-d_F(v)`, and let
`\delta_F(S)=\sum_{v\in S}\delta(v)`.

### Theorem 2.1 (bare casualty cut)

The number `B(S)` of distinct present immediate-upper witnesses destroyed by
the extraction is exactly

\[
 B(S)=2|S|-\delta_F(S)-e_F(S),                         \tag{2.2}
\]

and therefore

\[
 \boxed{B(S)\ge t(h+1)-2(C+\ell)+1.}                  \tag{2.3}
\]

All these colours are distinct and lie outside the selected missing target
family.

#### Proof

Because a selected target `U` is missing, no two selected facets of that
same `U` are adjacent in `F`: their union would be `U`.  Cross-target edges
inside `S` are allowed.  The degree sum on `S` is

\[
 2|S|-\delta_F(S)=2e_F(S)+|\partial_F(S)|.
\]

The number of incident edges removed is
`e_F(S)+|partial_F(S)|`, which is (2.2).  Upper injection makes their colours
distinct and present.  Since `F[S]` is a forest,
`e_F(S)<=|S|-1`, while

\[
 \delta_F(S)\le\sum_v(2-d_F(v))=2(C+\ell).
\]

Using `|S|=t(h+1)` proves (2.3). \(\square\)

Bare recursion can have fewer children than parents only if

\[
                         th<2(C+\ell)-1.               \tag{2.4}
\]

For the natural Catalan-scale leave `t=ell=C`, (2.3) becomes (0.1), so
every `h>=4` is solver-free supercritical.  A positive construction must
recreate at least `B(S)-t+1` casualty colours merely to obtain strict
contraction, and all `B(S)` to close the upper palette.  This restoration
must use exact colours in (1.2); aggregate occurrence capacity is irrelevant.

## 3. What the Catalan endpoint reservoir actually supplies

An exact Catalan forest has `C` components and `2C` endpoint slots.  Every
rank-`r` owner is a facet of exactly `r-1` upper targets.  Hence, if `K_R`
is the number of endpoint slots among the `r+1` facets of `R`,

\[
                    \sum_{R\in\mathcal U}K_R=4D.      \tag{3.1}
\]

The mean is exactly four.  It follows only that

\[
 { |\{R:K_R\ge h+1\}|\over D}\le {4\over h+1}.        \tag{3.2}
\]

Thus an already exposed `h+1`-facet endpoint socket has vanishing density
when `h` grows.  For a uniform `2C`-subset of owners,
`K_R` tends to `Poisson(4)` and

\[
 \Pr(K_R\ge2)\to1-5e^{-4}=0.908421\ldots.             \tag{3.3}
\]

This is only a raw two-facet seed.  Let `\mathcal M` be the missing lower
bank.  For `L\in\mathcal M`, let

\[
 A_L=\{x:L+x\text{ is an endpoint owner}\},quad a_L=|A_L|,
\]

and let `b_L` count forest components whose two endpoints intersect in
`L`.  The exact number of direct endpoint connectors which simultaneously
use a missing lower and merge components is

\[
 T_{\rm dir}=\sum_{L\in\mathcal M}
                    \left({a_L\choose2}-b_L\right).             \tag{3.4}
\]

In the full random model in which the endpoints form a uniform `2C`-element
owner set, are paired uniformly into `C` component pairs, and the missing
lower bank is an independent uniform `C`-subset, one has

\[
                  {\mathbb E T_{\rm dir}\over D}
                     ={16+o(1)\over r}.               \tag{3.5}
\]

So raw endpoint support can be constant while palette-legal direct support
vanishes.  Endpoint count, coordinate transitivity and one-point marginals
do not imply the needed correlation.  The full proof and the isolate-slot
scope are in
`MATH_THEOREM_R_CATALAN_FACET_ENDPOINT_SUPPORT_DISPERSION_AND_BRANCHING_GATE_20260801.md`.

## 4. A protected-coordinate inheritance lemma

There is one useful positive restriction.  Suppose `a in U` and choose the
socket labels

\[
                         v_0,\ldots,v_h\in U-\{a\}.    \tag{4.1}
\]

Then every socket owner facet, every internal lower colour, and every old
upper witness destroyed at a socket owner contains `a`.  Hence all child
upper demands inherit `a`.

If a child target also has a fresh incoming label `y`, choose the labels in
`U-{a,y}`.  Then every socket owner and internal lower contains both `a`
and `y`.  If the parent packet used no `y`, the child owner/lower resources
are automatically disjoint from the parent resources.  The numbers of
ordered choices are respectively

\[
                         (r)_{h+1},\qquad (r-1)_{h+1}. \tag{4.2}
\]

The assumed rank bound `r>=2h+1` makes both positive.  The coordinates
`a,y` have all-one traces through the socket, so they create no new
residence obligation; the remaining labels retain exactly the guards of
the resident-socket theorem.

#### Proof

Every selected facet is `U-v_j` and contains each excluded protected label.
An old edge incident to that facet has union containing the facet.  Internal
lowers delete two selected `v` labels and also retain the protected labels.
The choice counts and trace statement are immediate. \(\square\)

This removes the one-stratum coordinate-zero shore along a tagged branch,
but not its occurrence conflicts.  In the mixed-head SCD bank with active
pair `(a,z)`, every target containing `a` has source degree `r` or `r-2`.
Assume here `r>=7`, equivalently `C<=N`, and keep a uniformly random
`C`-subset from its bank of

\[
                         N={2r-3\choose r-2}
\]

providers, define

\[
 q_d={ {N-d\choose C}\over {N\choose C}}.             \tag{4.3}
\]

For every fixed tagged child, its source-support probability is at least
`1-q_(r-2)`, and

\[
                         q_{r-2}\longrightarrow e^{-8}.         \tag{4.4}
\]

Without the inherited tag, the expected supported fraction over all upper
targets is exactly

\[
 { {2r-3\choose r}\over D}(1-q_r)
 +{ {2r-3\choose r-1}\over D}(1-q_{r-2})
 \longrightarrow {1-e^{-8}\over2}.                   \tag{4.5}
\]

Equations (4.4)--(4.5) are **source-only marginals**.  They do not give an
adaptive matching.  In particular a target containing both `a,z` has the
forced new-owner ticket `R-z`; if its two slots are unavailable, every
source provider is physically blocked.

## 5. Exact deterministic absorbing theorem

Let a residual state record the complete occurrence-labelled owner, lower,
upper, guard and component resources, together with every deeper-shadow and
common-`Q`/compiler resource required by the intended conclusion.  A
complete packet for demand `R` specifies its socket/exterior rethread and
its resulting child multiset `\partial p`.

### Theorem 5.1 (weighted regenerative closure)

Suppose there are constants `rho<1` and `K<infinity`, and weights satisfying

\[
                         1\le w(R)\le K,               \tag{5.1}
\]

such that in **every finite reachable residual state**, each active demand
`R` has a complete legal packet `p` jointly compatible with the already
fixed resources and obeying

\[
                  \sum_{V\in\partial p}w(V)\le\rho w(R).       \tag{5.2}
\]

Then every initial family of total weight `W_0` closes after at most

\[
                         {W_0\over1-\rho}              \tag{5.3}
\]

packet installations.  In particular `H` initial demands use at most
`KH/(1-rho)` packets.

#### Proof

Replacing `R` decreases the active potential by at least
`(1-rho)w(R)>=1-rho`.  The potential is nonnegative, so (5.3) follows.
All legality is included in the packet hypothesis, hence the terminal state
is physical rather than a rankwise marginal. \(\square\)

There is also a useful uniform matching form.  Suppose each unsupported
socket has at most `b` children and, after every finite resource history,
the complete packet hypergraph has a matching which absorbs, by terminal
zero-child packets, all but at most a `beta` fraction of every attainable
child family.  If

\[
                              b\beta<1,                \tag{5.4}
\]

then generation sizes contract by `b beta`, and `H` initial demands expose
at most `H/(1-b beta)` tasks in total.  The quantifier after **every**
residual history is essential; one-target marginals do not imply it.

For the preliminary `k=17` fourteen-target row, the projected ratio
`beta=9/28,b=2` gives `b beta=9/14<1`.  This is not a theorem for that
fixture: the nineteen advertised providers were only individual projections
and share physical resources.  The exact-19 positive-current row is sharper
but critical: it has seven child colours, six projected providers, and one
unsupported child, while also exporting three repeat/component units.

There is also a nearby exact positive finite exterior-absorber example,
which must not be identified with the present compact socket.  In the
`m=9`, finite-`L=3` convention of
`MATH_THEOREM_K17_SCD_COMPACT_SOCKET_BANK_AND_UPPER_CASUALTY_LEDGER_20260801.md`,
a correlated bank of thirty guarded three-facet/two-seam macros closes its
entire immediate child cascade.  By contrast, the present `h=3` compact
socket has four facets and three seams.  Thus the finite bank does not
instantiate Theorems 2.1 or 6.1 here.  After guard rechoices it uses ninety
distinct facets, sixty disjoint exposed guards and eighty-one extra cuts,
and leaves no residual immediate child.  Its exterior providers and
rethreads explicitly recreate the relevant casualty colours, so it is
evidence that correlated absorption is possible in a nearby macro class,
not evidence for an independent one-target probability or for this exact
socket family.  The same literal bank still leaves respectively
`1458,2429,1583,549,101,10` internal upper holes at ranks `10,...,15`.
Thus even this successful immediate-layer absorber does not establish the
all-depth hereditary hypothesis of Theorem 5.1.

## 6. Owner/lower conflict graph and Haxell selection

For one demand `U`, let `Sigma_U` be all ordered injective `(h+1)`-tuples
from `U`; put

\[
                         M=|\Sigma_U|=(r+1)_{h+1}.      \tag{6.1}
\]

A candidate `s=(U;v_0,...,v_h)` uses owner facets

\[
 O(s)=\{U-v_i:0\le i\le h\}
\]

and internal lowers

\[
 L(s)=\{U-\{v_{i-1},v_i\}:1\le i\le h\}.
\]

For a demand family `\mathcal D`, let `\lambda_F` and `\lambda_G` be the
numbers of targets containing a rank-`r` facet `F` and a rank-`(r-1)` set
`G`, respectively.

### Theorem 6.1 (exact candidate pressure)

For fixed `F\subset U`, exactly

\[
 A_O=(h+1)(r)_h=M{h+1\over r+1}                       \tag{6.2}
\]

orders use `F`.  For fixed `G\subset U`, exactly

\[
 A_L=2h(r-1)_{h-1}=M{2h\over r(r+1)}                  \tag{6.3}
\]

orders use `G` as an internal lower.  Therefore the degree of `s` in the
multipartite owner/lower conflict graph satisfies

\[
 {d(s)\over M}\le
 {h+1\over r+1}\sum_{F\in O(s)}(\lambda_F-1)
 +{2h\over r(r+1)}\sum_{G\in L(s)}(\lambda_G-1).      \tag{6.4}
\]

If `\lambda_F\le\Lambda_1`, `\lambda_G\le\Lambda_2` and

\[
 \Psi={ (\Lambda_1-1)(h+1)^2\over r+1}
      +{2(\Lambda_2-1)h^2\over r(r+1)}<\frac12,       \tag{6.5}
\]

then Haxell's independent-transversal theorem selects one socket per demand
with pairwise disjoint owners and internal lowers.

#### Proof

Equations (6.2)--(6.3) follow by choosing the position of the fixed omitted
label, or the oriented adjacent position of the fixed omitted pair, and
then filling the remaining positions injectively.  Summing all candidates
conflicting with one resource gives (6.4).  Under (6.5), every part has
size `M>2 Delta`, where `Delta` is the conflict-graph maximum degree;
Haxell applies. \(\square\)

For every `G`, the exact shadow identity

\[
                2\lambda_G=\sum_{F\supset G}\lambda_F          \tag{6.6}
\]

shows that `\lambda_F\le L` implies `\lambda_G\le rL/2`.  Hence any genuinely
constant-load demand bank admits simultaneous owner/lower sockets for
`h=o(sqrt(r))`, before guards.

The tempting perfect load `\lambda_F=2` at `|\mathcal D|=C` is impossible for
every `r>=4`.  Average facet load is exactly two, so a maximum of two would
force equality everywhere.  Complementing targets gives

\[
                   W_{r-2,r-1}x=2\mathbf1.             \tag{6.7}
\]

The inclusion matrix has full column rank over `Q` (its Gram eigenvalues
are `(r-1-i)(r+1-i)>0`, `0<=i<=r-2`).  Since
`W_{r-2,r-1}\mathbf1=(r-1)\mathbf1`, the unique real solution is
`x=2/(r-1)\mathbf1`, not binary.  Thus even the best-looking balanced bank
has a genuine integral-correlation gate.

For a uniform `C`-subset of all targets and independent uniform orders, let
`P(s)` denote the resource-incidence union bound on the right of (6.4).
Then

\[
 \mathbb E P(s)={C-1\over D-1}\left[
 { (h+1)^2(r-2)\over r+1}
 +{2h^2({r\choose2}-1)\over r(r+1)}\right]
       =(4+o(1)){h^2\over r}.                         \tag{6.8}
\]

The actual normalized conflict degree satisfies `d(s)/M<=P(s)`.  Hence
`P(s)=o(1)` in probability when `h=o(sqrt(r))`; in particular a `1-o(1)`
fraction of random candidates satisfies the local Haxell pressure bound.
This is neither an exact graph-degree expectation nor a deterministic
all-task selection theorem.

## 7. Exact guard structural zeros

Fix oriented left and right exterior pieces which are already internally
resident.  Let `L_s` be the intersection of their last `s` owner occurrences
and `R_s` the intersection of their first `s`.  Define the clean-age sets

\[
\begin{aligned}
 C_L&=\{x:\ell(x)\in\{0\}\cup[h+1,\infty)\},\\
 C_R&=\{x:\rho(x)\in\{0\}\cup[h+1,\infty)\}.
\end{aligned}                                         \tag{7.1}
\]

Before choosing the omitted labels, it is necessary that every
`x\notin U` lie in `C_L\cap C_R`; the socket trace is zero on those
coordinates and terminates both exterior runs.  Subject to that condition,
the label assigned to socket position `j` must lie in

\[
\begin{aligned}
 B_0&=U\cap R_1\cap C_L,\\
 B_h&=U\cap L_1\cap C_R,\\
 B_j&=U\cap L_{h+1-j}\cap R_{j+1}\qquad(1\le j\le h-1).
\end{aligned}                                           \tag{7.2}
\]

Guard-compatible socket orders are exactly the systems of distinct
representatives of `(B_0,...,B_h)`.  Thus existence is ordinary Hall and
their number is the associated permanent.  In particular

\[
                   |U\cap L_1\cap R_1|\ge h-1          \tag{7.3}
\]

is necessary.  Residence of the separate exterior pieces gives no lower
bound on (7.3): their persistent cores may be disjoint.  Omitting the
clean-age sets makes the SDR statement false already at `h=1`: an incoming
one-step `v_0` run is terminated by the first socket zero.

For occurrence-filtered candidate lists `\mathcal A_U`, Haxell's
independent-transversal theorem gives the following sufficient bound:

\[
 \min_U|\mathcal A_U|\ge
 2\max_s\left(\sum_{F\in O(s)}d_O(F)
             +\sum_{G\in L(s)}d_L(G)+d_{guard}(s)\right),       \tag{7.4}
\]

where the three terms count candidates in other task parts conflicting on
owner, lower, and occurrence-labelled guard resources.  This bound is not
necessary, and it does not encode coloured casualty restoration, graphic
independence, source/common-cap compatibility, or compiler rows.  The
Catalan reservoir theorem does not imply the clean-age condition, (7.2),
or this Haxell bound.

## 8. Exact remaining all-`k` theorem

The compact socket can participate in a `B+O(1)` induction only through a
state satisfying all of the following simultaneously.

1. **Coloured restoration:** equation (1.2) for every immediate-upper
   colour, not scalar surplus.
2. **Hereditary contraction:** (5.2), or the robust matching form (5.4),
   after every residual history with dimension-uniform weights.
3. **Dispersed socket menus:** bounded facet/lower loads sufficient for
   (6.5), plus the clean-age and occurrence Hall rows (7.1)--(7.2).
4. **Typed absorbers:** endpoint, missing-lower, source/head and provider
   resources matched jointly; the forced singleton endpoint cuts are
   included.
5. **Topology, chronology and compiler:** the contracted component edges
   are graphic-independent, the final ordered pieces satisfy every
   residence and deeper-shadow row, and one occurrence-labelled common-`Q`
   source/cap matching realizes the literal lower compiler.

The resident facet theorem supplies none of items 1--5 automatically.
Items 1--4 plus the local socket theorem give only a resident
owner/immediate-shadow closure module.  Adding the complete all-depth and
literal common-`Q` rows in item 5 upgrades that conditional module to a
physical contiguous-OR compiler.  The smallest missing mathematical
statement is therefore a **correlated coloured absorber theorem**, not
another endpoint-count or raw branching estimate.
