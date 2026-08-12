# Strict `D_4` fringe packets lie in the endpoint-profile kernel

## Exact coverage, product legality, the `V_4` indivisibility consequence, and the five/six/seven-cell thresholds

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Result

Put `C_t=Cat_t`, let

\[
 s=\min\{t:C_t\ge p\},\qquad \theta={C_s\over p},      \tag{0.1}
\]

and consider the four canonical endpoint root families in the size-`s+1`
parent

\[
 \begin{aligned}
 \mathcal R_s={}&\{1u0:u\in\mathcal D_s\}\\
 &\dot\cup\{10\,1v0:v\in\mathcal D_{s-1}\}\\
 &\dot\cup\{1v0\,10:v\in\mathcal D_{s-1}\}\\
 &\dot\cup\{10\,1w0\,10:w\in\mathcal D_{s-2}\}.
 \end{aligned}                                        \tag{0.2}
\]

Their total canonical preload is

\[
 M_s=C_s+2C_{s-1}+C_{s-2}=\rho_s C_s,                 \tag{0.3}
\]

where

\[
 \boxed{
 \rho_s={5s(5s-7)\over4(2s-1)(2s-3)}
           \longrightarrow {25\over16}.}              \tag{0.4}
\]

The two endpoint coordinate swaps generate one `V_4` ownership component
containing all four families in (0.2).  By the stated exact overlay result,
choosing a coordinate-component shore only permutes the four cells and
leaves their maximum at least `C_s`; it cannot implement an abstract
four-cell discrepancy signing.

The non-coordinate fourteen-row `D_4` factor does not repair this when it
is deployed by the dense **strict fringe** construction.

### Theorem A (coverage and exact product legality)

Let `a_t` count size-`t` Dyck trees having no fringe subtree of size four.
All but

\[
                         R_s=a_s+2a_{s-1}+a_{s-2}       \tag{0.5}
\]

members of (0.2) split into exact fourteen-row packets, and

\[
                         R_s=o(C_s)                    \tag{0.6}
\]

exponentially.  On each packet one may independently choose the canonical
MSW `D_4` factor or the certified non-coordinate `D_4` factor.  Every
product of these choices is one integral exact factor on the union of the
four tagged root families.

### Theorem B (endpoint-profile kernel obstruction)

Every packet in Theorem A is strictly inside the Dyck filling of its
canonical endpoint occurrence and fixes its two complementary local ports.
The matched endpoint window contains both ports.  Hence its local
intersection is empty before and after every packet choice.  Consequently

\[
 \boxed{
 \text{every strict `D_4` fringe choice fixes each of the four
 canonical physical endpoint targets occurrence by occurrence}.}       \tag{0.7}
\]

Thus the exact product cube of Theorem A has **zero direct action** on the
four-cell contingency table.  It neither redistributes the endpoint
preload nor attaches a marker to those four endpoint targets.  The same
conclusion holds for any number of states in the complete local
`D_4`-port fibre, not merely the two displayed factors.

If one merely follows the fringe choices by a **global** endpoint
coordinate relabelling, the latter only permutes the four cell loads, so
their maximum remains at least `C_s`.  This still rules out the direct
fringe-plus-global-relabel construction when `C_s>p`, even in the range
`M_s<=4p`.

There is one rigorously open distinction.  Internal `X/Y` ownership has
changed, so the `V_4` ownership overlay recomputed after the fringe choices
could conceivably have smaller interaction components.  Endpoint-profile
invisibility alone does not prove that this recomputed overlay remains
connected, nor does it exclude markers on shorter boundary-cut windows.
An overlay-invariance theorem or an explicit fragmentation theorem is
still required for that two-stage route.

This is stronger than a supply failure: coverage and integrality are both
present, but the entire strict-fringe library lies in the kernel of the
required boundary statistic.

### Theorem C (exact number of cells a surviving library must expose)

Even with zero other background, any parent-aligned library serving the
preload (0.3) needs at least

\[
 \boxed{
 L_s(\theta)=\left\lceil{M_s\over p}\right\rceil
             =\lceil\rho_s\theta\rceil}               \tag{0.8}
\]

distinct physical cells.  Define

\[
 \theta_j(s)={j\over\rho_s}
 ={4j(2s-1)(2s-3)\over5s(5s-7)}.                      \tag{0.9}
\]

Then the scalar requirements are exactly

\[
\begin{array}{c|c}
\text{overshoot range}&\text{minimum cell count}\\ \hline
\theta_4(s)<\theta\le\theta_5(s)&5,\\
\theta_5(s)<\theta\le\theta_6(s)&6,\\
\theta_6(s)<\theta< C_s/C_{s-1}&7.
\end{array}                                           \tag{0.10}
\]

The three limiting thresholds are

\[
 \theta_4\to{64\over25},\qquad
 \theta_5\to{16\over5},\qquad
 \theta_6\to{96\over25}.                             \tag{0.11}
\]

Seven cells are always enough at the level of total mass for the minimal
Catalan scale, whereas four cells are already impossible above
`theta_4(s)`.  Whenever the actual overshoot satisfies
`theta>theta_6(s)`, a ternary-by-binary boundary product has only six cells
and is impossible.  A Cartesian two-boundary alphabet with both factors
nontrivial then needs at least eight or nine potential cells, for example
`4 x 2` or `3 x 3`, before background and balancing are considered.  This
does not exclude a nonproduct seven-state menu, and it does not assert that
the top interval occurs for infinitely many arithmetic values of `p`.

There is an exact finite seed for the `4 x 2` option.  With

\[
 H_4=\langle(2\ 3),(4\ 5),(6\ 7)\rangle,              \tag{0.12}
\]

the reanchored `H_4`-orbits of the canonical and non-coordinate factors at
the fixed port `1256` realize the four first-insertion labels

\[
                              \{3,4,7,8\}.             \tag{0.13}
\]

Together with a phase-disjoint binary endpoint on fresh coordinates this
gives eight distinct **formal** target cells.  It is not yet a packet
theorem: in a strict fringe it is erased by Theorem B, while in a
parent-aligned placement one factor state controls all fourteen rows and
no balanced full-preload action is proved.

The only surviving construction is therefore a genuinely
**parent-aligned** multi-state atom whose changed slab meets an endpoint of
the serviced window.  Such an atom is outside the strict-fringe product
proof and needs a new joint ownership certificate.

## 1. Exact first-fringe packetization

Let `a_t` be as in Theorem A and put

\[
                         A(z)=\sum_{t\ge0}a_tz^t.       \tag{1.1}
\]

There are fourteen binary trees of size four.  Root decomposition gives

\[
                         A(z)=1+zA(z)^2-14z^4.          \tag{1.2}
\]

Indeed, a tree avoids a size-four fringe exactly when its two root
subtrees avoid one, except that the fourteen trees of total size four are
created by `1+zA^2` and must be removed.  Hence

\[
                 A(z)={1-\sqrt{1-4z+56z^5}\over2z}.   \tag{1.3}
\]

At `z=1/4` the discriminant is `7/128>0`.  Since `A` has nonnegative
coefficients, its radius of convergence is strictly greater than `1/4`.
It follows that

\[
                         {a_t\over C_t}=o(1)            \tag{1.4}
\]

exponentially.

For a nonavoiding tree, mark its first size-four fringe root in preorder.
Varying the marked fringe subtree over all fourteen size-four trees does
not change the marked root: all material preceding it is fixed, and a
size-four tree has no proper size-four fringe.  Thus

\[
                \mathcal D_t\setminus\mathcal A_t
\quad\text{is partitioned into}\quad
                {C_t-a_t\over14}                       \tag{1.5}
\]

fourteen-element packets.

Apply (1.5) separately to the four **tagged** families in (0.2).  Their
packet total is

\[
 \boxed{
 P_s={M_s-R_s\over14}
 ={C_s-a_s+2(C_{s-1}-a_{s-1})+(C_{s-2}-a_{s-2})\over14}.}             \tag{1.6}
\]

Equation (1.4), together with the fixed Catalan ratios between adjacent
indices, proves (0.6).

### Lemma 1.1 (product exactness)

Choose independently on every packet either of the two certified exact
`D_4`-port factors.  Every joint choice is an integral exact factor on the
union of the packet rows.

#### Proof

The two local factors have the same fourteen ports and each owns every
local `X`-state and every local `Y`-state once.  In a fixed common context,
replacing one by the other therefore preserves the complete ownership
ledger of the union of its fourteen rows and preserves its two boundary
ports rowwise.

The first-fringe packets partition the root rows.  Distinct packets hence
have disjoint old ownership slabs, and each replacement stays within its
own slab.  The four copies in (0.2) are tagged and disjoint as occurrence
families.  Consequently choices on different packets commute and their
ownership ledgers add without collision. \(\square\)

This proves Theorem A.  Notice that it proves the strongest desired
integrality statement for the strict-fringe deployment; failure below is
not caused by dependent rounding.

## 2. The port-kernel lemma

Let `J` be the eight-coordinate ground set of one installed `D_4` packet.
In the row rooted at `P`, every state choice has the same two ports

\[
                         X_0=P,\qquad X_4=J\setminus P. \tag{2.1}
\]

### Lemma 2.1 (swallowed port factors are invisible)

Let `W` be a matched intersection window which contains the entire local
packet slab, in particular both states in (2.1).  If `O_W` is the
intersection of all coordinates outside `J` along `W`, then for every
exact `D_4`-port factor `H`,

\[
                         T_H(W)=O_W.                   \tag{2.2}
\]

The complementary upper target is fixed as well.

#### Proof

The local part of the lower target is contained in

\[
                         X_0\cap X_4
                         =P\cap(J\setminus P)
                         =\varnothing.                 \tag{2.3}
\]

Thus only the exterior intersection `O_W` remains.  Dually, the local
union contains `X_0 union X_4=J`, so its complementary upper contribution
is fixed. \(\square\)

### Theorem 2.2 (strict-fringe `D_4` kernel)

For every occurrence in each family of (0.2), a first-fringe packet is
strictly contained in its Dyck filling, while the canonical matched
endpoint window contains the complete filling.  Therefore every packet
edge of Lemma 1.1 has zero signed action on that occurrence's endpoint
target.  Equivalently, if

\[
 \pi_{\rm end}(H)=
   (\mu_H(T_{00}),\mu_H(T_{10}),
     \mu_H(T_{01}),\mu_H(T_{11}))                      \tag{2.4}
\]

is the four-cell endpoint profile, then

\[
             \boxed{\pi_{\rm end}(H)=\pi_{\rm end}(H')}
                                                                  \tag{2.5}
\]

whenever `H,H'` differ by any collection of strict `D_4` fringe packet
choices.

#### Proof

The marked size-four fringe subtree lies inside the tagged Dyck word in
(0.2); the fixed outer `10` atoms, when present, lie outside it.  The
matched endpoint occurrence indexed by that word traverses its whole Dyck
filling.  It therefore swallows both packet ports.  Lemma 2.1 applies
occurrence by occurrence.  Summing the resulting zero signed vectors gives
(2.5). \(\square\)

The proof did not use which two `D_4` factors were chosen.  It applies to
the entire fibre of exact local factors with the ports (2.1).  It also
shows that strict-fringe choices cannot distinguish two outer contexts by
these endpoint targets: they leave the full endpoint target, including its
exterior carrier, unchanged.  Other, shorter windows which cut the packet
need not be invariant.

### Corollary 2.3 (no four-cell signing from dense fringe packets)

The abstract bounded-block discrepancy theorem cannot be instantiated by
the packet partition (1.6) for the endpoint cells.  Although every block
has size fourteen and the choices are product-legal, the induced sign of
every occurrence is constant: the packet library has zero endpoint
action.  In particular it does not break the stated one-component `V_4`
indivisibility by a direct endpoint-cell move.

### Corollary 2.4 (direct fringe plus global relabelling no-go)

Allow arbitrary product-legal strict `D_4` fringe choices, followed by one
global element of the endpoint coordinate group `V_4`.  Then the four
endpoint loads still satisfy

\[
                         \max_{\epsilon,\eta}
                         \mu(T_{\epsilon,\eta})\ge C_s.\tag{2.6}
\]

Consequently their cap defect is at least `(C_s-p)_+`.

#### Proof

Theorem 2.2 fixes the four-cell profile under every strict fringe edge.  A
global endpoint coordinate relabelling only permutes its four entries.
Their maximum is therefore the principal entry `C_s`.  This proves (2.6)
and the hinge lower bound. \(\square\)

Corollary 2.4 does **not** cover a new component-shore choice in the
ownership overlay recomputed after the internal modifications.  Whether
that overlay fragments is a separate unanswered incidence question.

## 3. Exact cell-count thresholds

Suppose a future parent-aligned library sends the invariant preload `M_s`
to `L` distinct physical cells, each of cap `p`, and ignore all additional
background.  Necessarily

\[
                         M_s\le Lp.                    \tag{3.1}
\]

 Since `M_s=rho_s theta p`, (3.1) proves (0.8)--(0.10).

The Catalan quotient gives

\[
                 1\le\theta<{C_s\over C_{s-1}}
                 ={2(2s-1)\over s+1}.                 \tag{3.2}
\]

Moreover

\[
 \rho_s{C_s\over C_{s-1}}
 ={5s(5s-7)\over2(2s-3)(s+1)}<7                       \tag{3.3}
\]

for every `s>=2`, because

\[
 14(2s-3)(s+1)-5s(5s-7)
 =3s^2+21s-42>0.                                      \tag{3.4}
\]

 Thus `M_s<7p` throughout the minimal-scale interval, proving the scalar
 seven-cell assertion.  Taking `s -> infinity` in (0.9) gives (0.11).

These are only necessary total-mass thresholds.  A physical construction
must additionally balance the cell loads against the **residual**
capacities after all canonical collars and other contexts are included.

For reference, the abstract contingency cost below the four-cell threshold
is already constant in the packet size.  If a future boundary-active
construction gives two independently selectable packet partitions of the
complete `M_s` occurrences, with block size at most `B` and `R` exceptions,
then fixed-dimensional extreme-point signing gives

\[
       \max_{a,b}n_{ab}
       \le {M_s\over4}+{5B+3R\over4}.                 \tag{3.5}
\]

This is Theorem 2.2 and Corollary 2.3 of
`MATH_THEOREM_PRELOADED_BOOLEAN_THRESHOLD_AND_MULTISTATE_GATE_20260726.md`:
one first balances the left block degrees with error `B`, then applies a
two-dimensional extreme-point rounding to the right block vectors to make
the right marginal and correlation errors at most `2B`; the four-cell
Fourier formula gives total error `5B/4`, and adversarial exceptions add
`3R/4`.

Thus for fourteen-row packets the zero-background numerical condition is

\[
                         4p-M_s\ge70+3R.              \tag{3.6}
\]

With actual cell capacities `c_ab=(p-beta_ab)_+`, the corresponding strong
sufficient condition is

\[
                         {M_s+70+3R\over4}
                         \le\min_{a,b}c_{ab}.          \tag{3.7}
\]

The strict fringe packets cannot instantiate (3.5): Theorem 2.2 says that
their putative occurrence signs have zero endpoint action.  Hence below
`theta_4(s)` the remaining obstruction is geometric ownership/carrier
realization, not abstract integral discrepancy.

## 4. The four-state `D_4/H_4` seed

Let `F` and `G` be the canonical and new complete `D_4`-port factors.  For
`h in H_4`, reanchor `hF` or `hG` at `P=1256`; that is, use at `P` the
coordinate image under `h` of the old row rooted at `h^{-1}P`.  The exact
first-insertion table is

\[
\begin{array}{c|c|c|c}
h&h^{-1}P&b_1^{hF}(P)&b_1^{hG}(P)\\ \hline
1&1256&4&7\\
(6\ 7)&1257&4&3\\
(4\ 5)&1246&8&3\\
(4\ 5)(6\ 7)&1247&7&3\\
(2\ 3)&1356&3&3\\
(2\ 3)(6\ 7)&1357&3&4\\
(2\ 3)(4\ 5)&1346&3&8\\
(2\ 3)(4\ 5)(6\ 7)&1347&3&8.
\end{array}                                           \tag{4.1}
\]

### Proposition 4.1 (literal four-state fixed-port menu)

Every row in (4.1) belongs to a legal exact `D_4`-port factor state, and
the support of either target column is exactly `{3,4,7,8}`.  If a second
independent endpoint supplies two labels in a disjoint coordinate block,
the marked occurrence has eight pairwise distinct formal targets.

#### Proof

The group `H_4` preserves the Dyck port family.  Coordinate conjugation
preserves both complete ownership ledgers, and reanchoring chooses the
unique row whose transformed port is `P`; hence every table entry is
port-legal and exact.  The two target supports are read literally from
(4.1).  With a disjoint two-label block, intersection with the four-label
and two-label coordinate sets recovers both states, proving the eight
targets distinct. \(\square\)

### Proposition 4.2 (the seed is not a full-preload library)

Installing any of the states in (4.1) in a strict first-fringe packet has
zero two-endpoint action.  Installing it parent-aligned may expose the four
labels, but a state choice simultaneously fixes all fourteen rooted paths;
(4.1) supplies neither independently assignable four-state blocks covering
`M_s-o(M_s)` occurrences nor a residual-capacity bound.

#### Proof

The strict-fringe assertion is Lemma 2.1, which applies to the entire local
port fibre.  The second assertion is a quantifier audit: (4.1) concerns one
marked port under a whole-factor choice, while Theorem A's independent
blocks are strict and therefore invisible.  No displayed construction
gives parent-aligned disjoint row blocks with the asserted coverage.
\(\square\)

Thus the finite eight-cell geometry required above the four-cell threshold
exists, but its extensive integral deployment is exactly the missing
theorem.

## 5. Cross-context carrier audit

Suppose a boundary-active context `C` would expose cells

\[
                  T_C^{ab}=K_C\cup\{x_C^a,y_C^b\}.     \tag{5.1}
\]

If `T_C^{ab}=T_D^{a'b'}`, then every element of `K_C\K_D` must be one of
the two active labels of `D`, and conversely.  Hence

\[
                         |K_C\triangle K_D|\le4.       \tag{5.2}
\]

Thus core distance greater than four is an exact separator.  For arbitrary
constant-weight `k`-cores in an `n`-coordinate universe, however, one core
has as many as

\[
                         D_{n,k}=\sum_{i=0}^2
                         \binom{k}{i}\binom{n-k}{i}    \tag{5.3}
\]

cores at distance at most four.  Greedy code selection therefore certifies
only a `1/D_(n,k)` fraction of a general atlas, a polynomial coefficient
loss.  It cannot be credited as coefficient-one cross-context separation.

The proof of (5.2) is the literal set difference of (5.1), and (5.3)
chooses the `i=0,1,2` deleted and inserted coordinates.  A dense theorem
must instead supply private markers, exploit special aligned-core
congestion, or round all collision colours against their residual
capacities.  Neither the strict fringe packetization nor the four-state
table supplies such a theorem.

## 6. A packet-measurable recomputed-overlay obstruction

The endpoint-kernel lemma alone does not decide the ownership overlay
after internal modification.  The following token-union criterion gives a
strict partial answer.

Let an anchored exact factor `H` have row-token supports `C_P`, indexed by
its ports `P in D`.  Here tokens are the full **uncoloured physical**
`X`-vertices and `Y`-colours used in the canonical ownership overlay,
including the anchored root tokens; no phase colour is attached.  Define

\[
                         U_H(A)=\bigcup_{P\in A}C_P
                         \qquad(A\subseteq D).         \tag{6.1}
\]

For each `g in V_4`, let `alpha_g` be the reanchoring bijection such that
the row rooted at `P` in `gH` is `g C_(alpha_g(P))`.

### Lemma 6.1 (exact component-union criterion)

A port set `A` is a union of connected components of the ownership
overlay of `(gH)_(g in V_4)` if and only if

\[
                 \boxed{
                 U_H(A)=gU_H(\alpha_g(A))
                 \quad\text{for every }g\in V_4.}     \tag{6.2}
\]

#### Proof

The token set owned by the rows with ports in `A` on the `g`-shore is
exactly `gU_H(alpha_g(A))`.  If `A` is a union of components, the
finite-group ownership lemma says that all shores of those components own
the same token set, proving (6.2).

Conversely, suppose (6.2) holds.  A token whose owner has port in `A` on
one shore then has its owner in `A` on every shore.  Hence no ownership
hyperedge crosses from the row set `A` to its complement.  Those rows are
therefore a union of connected components. \(\square\)

Let `H_sigma` be any factor obtained from the canonical factor `F` by the
independent first-fringe choices.  For every complete fourteen-root packet
`B`, exact local ownership gives

\[
                         \boxed{U_{H_\sigma}(B)=U_F(B).}\tag{6.3}
\]

Call a port set packet-measurable if it is a union of complete first-fringe
packets together with any exceptional roots; the exceptional rows are left
canonical in `H_sigma`, so their individual token supports are unchanged.

### Theorem 6.2 (no packet-measurable new split)

Suppose `A` and every reanchored set `alpha_g(A)` are packet-measurable.
Then `A` satisfies the component closure equations (6.2) for `H_sigma` if
and only if it satisfies them for the canonical factor `F`.  In
particular, inside the canonical no-interior-return component there is no
new nonempty proper component union of this packet-measurable kind.

#### Proof

Add (6.3) over all packets in `A` and in each `alpha_g(A)`.  Every token
union in (6.2) is then identical to its canonical value.  Thus the four
closure equations are literally the canonical equations.  The stated
canonical `V_4` theorem says that the no-interior-return root block is one
component, so it has no nontrivial closed port subset. \(\square\)

### Corollary 6.3 (where genuine fragmentation must occur)

If strict `D_4` fringe choices do fragment the recomputed principal
`V_4` overlay, then some new component cuts a fourteen-root packet on at
least one reanchored shore.  Therefore
the independent packet coordinates of Theorem A are not themselves the
new component coordinates.  Exploiting such a split requires an explicit
internal fourteen-row ownership-overlay analysis and a new joint
common-completion ledger.

Theorem 6.2 does not rule out this packet-cutting fragmentation; it isolates
it exactly.  In particular the nonzero short-window `D_4` profiles may
still participate in such a two-stage construction.

There is also a finite rigidity inside each packet.

### Theorem 6.4 (the local `F/G` ownership overlay is connected)

Let `F` be the canonical `D_4` factor and `G` the certified
non-coordinate factor.  Their two-factor ownership overlay has one
component containing all fourteen rooted rows.  Consequently the complete
fourteen-for-fourteen `F/G` replacement has no proper ownership-component
subtrade.

#### Proof

Use a canonical `X`-state token in each displayed row of `F` and locate
its owner in the displayed `G` ledger.  With root names written as their
four-subsets, the canonical first internal `X`-states give the following
undirected overlay adjacencies:

\[
\begin{array}{c|c@{\qquad}c|c}
1234&1346&1235&1235\\
1236&1234&1237&1256\\
1245&1347&1246&1347\\
1247&1236&1256&1345\\
1257&1357&1345&1245\\
1346&1257&1347&1247\\
1356&1245&1357&1257.
\end{array}                                           \tag{6.4}
\]

The self-edge at `1235` is supplemented by its canonical second internal
state `1458`, which the `G` ledger assigns to row `1346`.  Thus the overlay
contains the connected chain

\[
 1235-1346-1234-1236-1247-1347-1245-1345-1256-1237,   \tag{6.5}
\]

and the branches

\[
 1347-1246,qquad 1245-1356,qquad
 1346-1257-1357.                                      \tag{6.6}
\]

Equations (6.5)--(6.6) contain all fourteen roots.  Since every displayed
edge is equality of one literal `X`-token owned by the indicated old and
new rows, they lie in the ownership overlay.  Hence that overlay is
connected. \(\square\)

Theorem 6.4 rules out obtaining smaller independently switchable blocks by
decomposing the local comparison `F` versus `G`.  It does not by itself
settle the four-factor overlay after differently chosen packets are
conjugated at the two outer endpoints; those outer incidences are the
remaining possible source of packet-cutting fragmentation.

## 7. Precise surviving lemma

The strict-fringe deployment is now closed: it has exact packet coverage
and exact product legality but identically zero exported endpoint action.
The canonical coordinate `V_4` deployment is closed by the stated
one-component overlay theorem.  The composition in which fringe choices
are first used to alter the ownership incidence and a **new** `V_4`
component decomposition is then selected remains open; solving it requires
the full recomputed overlay, not the four-cell histogram alone.

A surviving local theorem must instead construct boundary-crossing atoms.
One sufficient formulation is the following.

> **Parent-aligned multi-state `D_4/H_4` atlas.**  Partition all but
> `o(M_s)` of the four tagged occurrence families into bounded joint atoms.
> For each atom give a common-completion library of integral exact parent
> factors, at least one of whose changed `D_4/H_4` slabs meets a serviced
> window endpoint.  The joint choices must be product-compatible after all
> overlapping atoms are merged.  At overshoot `theta`, their physical
> endpoint profiles must expose at least `L_s(theta)` carrier-separated
> cells and place the complete canonical preload plus all other-context
> background within the corresponding residual capacities, simultaneously
> at every protected depth.

Theorem 2.2 explains why “use more internal `D_4` states” is insufficient:
parent alignment is not an optional refinement but a necessary condition
for any exported action.  Theorem C shows that a uniform binary-by-binary
library is also numerically insufficient above `64/25`, and that a
ternary-by-binary library misses every actually realized overshoot above
`theta_6(s)`.  No such
boundary-crossing, carrier-separated joint atlas is presently proved.
