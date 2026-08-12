# Compact facet sockets expose one exact GK gain-two terminal reversal, but the clean shared-provider bank is finite-dimensional

Date: 2026-08-01  
Lane: K / standard four-row GK host / endpoint current / resident facet sockets  
Status: **exact current and extraction identities; exact long-chain
gain-two basis change; exact graphic, upper-repeat, child-provider, and
root-extension interfaces; and an architecture-specific shared-provider
ceiling.  The compact common-upper rail is not intrinsically gain two.  A
prepared long-chain terminal reversal is genuinely `(+1,+1)`, but clean
standard-GK short rethreads plus these sockets cannot pass the two active
current cuts for any `m>=19`.  No all-dimensional forest, compiler, or
contiguous-OR word is claimed.**

## 0. Verdict

Put

\[
 c=\operatorname {Cat}_{m-1},\qquad
 C=\operatorname {Cat}_m,\qquad
 I=C-2c,
 \qquad K={2m-4\choose m-4}.                         \tag{0.1}
\]

For a directed Johnson edge `e:T->H`, let

\[
 \sigma(e)=H\setminus T
\]

denote its insertion label.  Its endpoint-current column is exactly

\[
                    j(e)=-\mathbf e_{\sigma(e)}.     \tag{0.2}
\]

Consequently the forward compact facet rail

\[
 F_0\longrightarrow F_1\longrightarrow\cdots
 \longrightarrow F_h,
 \qquad F_i=V-\{v_i\},                               \tag{0.3}
\]

has intrinsic current

\[
                  -\sum_{i=0}^{h-1}\mathbf e_{v_i}. \tag{0.4}
\]

Reversing the rail changes current only by

\[
                        \mathbf e_{v_0}-\mathbf e_{v_h}. \tag{0.5}
\]

Thus the common-upper rail itself is a one-unit transfer, never an
intrinsic gain-two actuator.

There is nevertheless one exact standard-GK gain-two face.  On a long
chain

\[
 R\subset S=R+\rho\subset L=S+x\subset U=L+y,       \tag{0.6}
\]

a reversed-D `a`-option and an intact direct `zU` provider contain

\[
                 U\xrightarrow{z}zL\xrightarrow{a}azS.       \tag{0.7}
\]

Reverse the same two physical edges:

\[
                 azS\xrightarrow{x}zL\xrightarrow{y}U.       \tag{0.8}
\]

The lower palettes in (0.7),(0.8) are both `{L,zS}`, the upper palettes
are both `{zU,azL}`, and the undirected edge set is identical.  Hence the
graphic state is unchanged and

\[
 \boxed{\Delta\kappa
       =\mathbf e_a+\mathbf e_z-\mathbf e_x-\mathbf e_y,}
 \qquad
 \boxed{(\Delta\kappa_a,\Delta\kappa_z)=(1,1).}     \tag{0.9}
\]

This is a genuine open gain-two **column**.  It is a physical actuator
without additional degree repair only on the exposed/closed endpoint faces
specified in Section 3.  It is **not** a fixed-`M_0` switch: it changes the
lower--tail assignments

\[
 (L,U),(zS,zL)\quad\longmapsto\quad(L,zL),(zS,azS). \tag{0.10}
\]

It can be made the terminal edge and right seam of the compact resident
socket with parent `azL`; the preceding `h-1` facet edges are a residence
buffer.  They are not free.  They require an owner/lower extraction,
named upper-child returns, a new hole--terminal containment matching, and
`h-1` repeat-upper slots.

There is a sharp common-resource ceiling.  If `p` denotes one-unit short
provider rethreads and `b` denotes clean terminal gain-two sockets, both
consume the same bank of `I` intact direct `zU` providers, so

\[
                              p+b\le I.              \tag{0.11}
\]

If `D_long` is the number of reversed-long D choices, the active-current
sum requires

\[
                    p+2b\ge I-c+D_{\rm long}-2.      \tag{0.12}
\]

The standard GK image theorem gives `D_long>=K-c`.  Maximizing the left
side of (0.12) under (0.11) gives at most `2I`, while the right side is at
least `K+I-2c-2`.  The inequality fails for every `m>=19`.  Thus the
terminal reversal is real, but the clean standard-GK socket bank is not an
all-`m` escape.

## 1. The insertion-label current identity

Let `F` be a directed lower-injective support on rank-`r` owners.  Write
`H_q` for the number of unused rank-`(r-1)` lower colours containing `q`,
`S_q` for the number of source owners containing `q`, and

\[
                         \kappa_q=1+S_q-H_q.         \tag{1.1}
\]

### Lemma 1.1 (one-edge column)

If `e:T->H`, then (0.2) holds.

#### Proof

Write `T=L+x`, `H=L+y`.  Adding `e` adds the used lower incidence
`1_L` and the used head incidence `1_H`.  Since unused-lower change has
the opposite sign,

\[
                  j(e)=\mathbf1_L-\mathbf1_H
                      =-\mathbf e_y.                \tag{1.2}
\]

Here `y=sigma(e)`.  \(\square\)

### Corollary 1.2 (exact replacement current)

If a rethread deletes old arcs `D` and adds arcs `A`, then

\[
 \boxed{\Delta\kappa_q
   =|\{e\in D:\sigma(e)=q\}|-
     |\{e\in A:\sigma(e)=q\}|.}                   \tag{1.3}
\]

For the compact socket (0.3),

\[
 \sigma(F_i,F_{i+1})=v_i,
 \qquad 0\le i<h,                                  \tag{1.4}
\]

which proves (0.4).  The reverse orientation inserts
`v_1,...,v_h`, proving (0.5).

Equation (1.3) is the first scope correction.  A socket earns positive
current only through the arcs which its extraction removes.  Every child,
return, or exterior attachment must be charged on the added side of
(1.3).

## 2. Fixed-root legality and why closed fixed-`M_0` sockets have no current

Let

\[
 M_0:{\Omega\choose r-1}\longrightarrow{\Omega\choose r}       \tag{2.1}
\]

be the rooted lower--tail bijection.  A physical edge of lower colour `L`
is fixed-`M_0` admissible only when its tail is `M_0(L)`.

For the socket edge `F_i->F_(i+1)`, the lower colour is

\[
                         K_i=V-\{v_i,v_{i+1}\}.      \tag{2.2}
\]

### Lemma 2.1 (facet-digraph criterion)

The whole forward socket is fixed-`M_0` admissible if and only if

\[
 \boxed{M_0(V-\{v_i,v_{i+1}\})=V-v_i
        \quad(0\le i<h).}                           \tag{2.3}
\]

Equivalently, define the directed facet graph `D_V` on labels in `V` by

\[
 x\longrightarrow y
 \quad\Longleftrightarrow\quad
 M_0(V-\{x,y\})=V-x.                                \tag{2.4}
\]

Then `v_0->...->v_h` must be a directed simple path in `D_V`.

#### Proof

The lower colour of the `i`th socket arc is (2.2), and its physical tail
is `V-v_i`.  This is exactly (2.3).  \(\square\)

If a closed rethread preserves the complete used-lower set and the
complete used-head set, then both `H_q` and `S_q` are unchanged.  Hence

\[
                             \Delta\kappa\equiv0.    \tag{2.5}
\]

In particular, a fixed-`M_0` socket whose exposed tails and heads are
returned to the same rooted resource shores cannot be gain two.  Any
positive claim must exhibit the open change of source or lower basis
literally.  The reversal (0.10) does so.

## 3. The exact standard-GK terminal actuator

The standard four-row matching on the long chain (0.6) contains

\[
 M_0(L)=U,\qquad M_0(zS)=zL,qquad M_0(azR)=azS.     \tag{3.1}
\]

The retained direct provider of `zU` is the physical edge

\[
 U\longrightarrow zL,qquad
 \ell=L,\quad \operatorname {up}=zU,\quad \sigma=z. \tag{3.2}
\]

The reversed-D auxiliary edge is

\[
 zL\longrightarrow azS,qquad
 \ell=zS,\quad \operatorname {up}=azL,\quad \sigma=a. \tag{3.3}
\]

### Theorem 3.1 (algebraic palette- and graphic-neutral gain two)

Replacing (3.2),(3.3) by their reverse orientations preserves the lower
multiset, upper multiset, undirected graph, component count, and cycle
state.  Its current change is (0.9).  The reversed directed support is
degree-legal without exterior repair when this two-edge path is a whole
component; otherwise Section 3.2 gives the exact open boundary.

#### Proof

The reverse of (3.3) is `azS->zL`; it still has lower `zS` and upper
`azL`, but inserts `x` because `L=S+x`.  The reverse of (3.2) is
`zL->U`; it still has lower `L` and upper `zU`, but inserts `y` because
`U=L+y`.  Lemma 1.1 gives

\[
 (-\mathbf e_x-\mathbf e_y)-(-\mathbf e_z-\mathbf e_a)
  =\mathbf e_a+\mathbf e_z-\mathbf e_x-\mathbf e_y. \tag{3.4}
\]

The unoriented edges are literally unchanged.  \(\square\)

If `U->zL->azS` is an entire path component, the old source is `U` and
the new source is `azS`; the hole set is unchanged.  This is the source
form of (3.4):

\[
                   \mathbf1_{azS}-\mathbf1_U
                  =\mathbf e_a+\mathbf e_z-\mathbf e_x-\mathbf e_y.
                                                               \tag{3.5}
\]

The ordinary-coordinate debts `-e_x-e_y` are real.  A bank must place
them within the ordinary current reserve; active-coordinate gain alone is
not enough.

### 3.2 Terminal-suffix form

Suppose instead that the component contains

\[
                         P\to U\to zL\to azS.        \tag{3.6}
\]

Delete only `P->U` and reverse the terminal two-edge suffix.  Put

\[
                         K=P\cap U,qquad W=P\cup U. \tag{3.7}
\]

The new state has one additional component, one additional source `azS`,
one additional lower hole `K`, and loses the upper witness `W`.  Therefore

\[
                         \Delta\kappa
                    =\mathbf1_{azS}-\mathbf1_K.      \tag{3.8}
\]

Since \(K\subset G\), (3.8) is again exactly `(+1,+1)` on `(a,z)`.  It
exports the typed child `(K,P,W)`: missing lower `K`, terminal `P=M_0(K)`,
and missing upper `W`.

A same-ticket return from `P` cannot both preserve the gain and restore
`W`.  Indeed, a fixed-ticket return has head `K+g`.  Equality of its upper
with `W` forces `K+g=U`, but `U` already has its incoming edge from `zL`.
Thus a blocked terminal needs either a different source ticket plus a
separate `W` provider or an alternative upper-`W` facet edge which changes
the lower ticket.  This is a genuine basis-changing child, not an
anonymous extra seam.

## 4. Embedding the actuator in the compact resident socket

Set the compact socket parent to

\[
                         B=azL.                     \tag{4.1}
\]

Choose

\[
 v_h=a,qquad v_{h-1}=x,qquad
 v_0,\ldots,v_{h-2}\in B-\{a,z,x\}                 \tag{4.2}
\]

distinct.  Then

\[
                         F_{h-1}=azS,qquad F_h=zL. \tag{4.3}
\]

Consequently the last socket edge and its right attachment are exactly

\[
                         azS\to zL\to U,             \tag{4.4}
\]

the new side of Theorem 3.1.

The labels in (4.2) exist whenever `h-1<=m-2`.  To invoke the resident
facet-socket theorem with its frozen stated hypotheses, assume in addition

\[
                              m\ge2h+1.              \tag{4.2a}
\]

It then supplies the exact two-sided residence guards.  In particular:

* `x=v_(h-1)` needs a right positive prefix of length `h`; the adjacent
  owner `U` supplies its first occurrence;
* `a=v_h` needs the prescribed left extension, while its right age is
  clean because `U` omits `a`; and
* every earlier omitted label is ordinary, so the prefix rail has no
  intrinsic `a`- or `z`-insertion charge.

This proves residence only when all the remaining guard ages from the
socket theorem are supplied.  The bare three-owner reversal is not a
depth-`h` residence theorem.

Let `D_pad` and `A_pad` be, respectively, every deleted and added arc
outside the two terminal edges of Theorem 3.1.  The full socket column has

\[
 \Delta\kappa
 =\mathbf e_a+\mathbf e_z-\mathbf e_x-\mathbf e_y
   +\sum_{e\in D_{pad}}\mathbf e_{\sigma(e)}
   -\sum_{e\in A_{pad}}\mathbf e_{\sigma(e)}.       \tag{4.5}
\]

Thus it remains clean gain two exactly when the padding/extraction term in
(4.5) is zero on `a,z`.  The local facet theorem does not imply this row.

### 4.1 Named extraction children

For an earlier facet `F_i=B-v_i`, an old outgoing edge inserting
`alpha_i` has upper child

\[
                         R_i=B-v_i+\alpha_i.         \tag{4.6}
\]

An incoming edge `G_i->F_i` analogously exports the child `G_i union F_i`.
Distinct useful special entries export distinct cofacet children unless
one is the parent `B` itself.  The **bare two-edge palette reversal**
exports no upper or lower child: its two palettes are identical.  A
non-exposed terminal suffix instead exports `(K,P,W)` exactly as in Section
3.2.  The right seam is already
committed to `zU`, so at most the left seam can absorb one early child.
Every other last witness needs a provider SDR.

For a fixed root matching, providers of a lost upper target `R` are the
literal arcs

\[
 T=M_0(L)\longrightarrow L+(R-T),qquad
 L\subset R,\quad T\subset R.                       \tag{4.7}
\]

They must be selected jointly with tail capacity, head capacity, lower
injectivity, and the active-current tax `sigma=R-T`.  The unrooted fact
that `R` has many facets is not a fixed-`M_0` provider theorem.

### 4.2 A conditional interior boundary formula and the exact graphic row

For a clean interior host, put

\[
 A=\{F_0,\ldots,F_{h-1}\},\qquad
 H=\{F_1,\ldots,F_h\},                              \tag{4.8}
\]

and let `f` be the old tail-to-head partial permutation.  If every member
of `A` has an old outgoing edge and every member of `H` an old incoming
edge, then forcing the socket opens exactly

\[
                         \chi=h-|f(A)\cap H|         \tag{4.9}
\]

external predecessor tails and `chi` external child heads.  Since an
upper-injective host contains at most one old edge between facets of `B`,

\[
                              \chi\ge h-1.           \tag{4.10}
\]

A direct component-neutral return is a matching between these two
boundary banks by legal rooted Johnson arcs, simultaneously covering every
unsupported child from (4.6).  This is a labelled tail--head--lower--upper
matching problem, not ordinary colour Hall.

Formula (4.9) is only the fully interior, tail-rooted owner-degree face.  It
is **not** the extraction count of the terminal actuator itself:
`F_(h-1)=azS` is an old terminal, so not every member of `A` has an old
outgoing edge.  Moreover, if an earlier socket lower `K_i` is not rooted at
tail `F_i`, its remote old provider must also be deleted or the lower--tail
basis must be changed.  All such remote provider deletions and the terminal
endpoint credit/defect belong in `D_pad,A_pad` in (4.5).  The general
column is always (1.3); (4.9) is a useful special case, not a replacement
for it.

Delete all conflicting old arcs and contract every component of the
residual forest.  The socket prefix and every return edge are graphic-legal
if and only if their images are independent in the contracted graphic
matroid, equivalently

\[
                         |E[J]|\le |J|-1             \tag{4.11}
\]

for every nonempty contracted vertex set `J`.  The terminal reversal
itself changes no unoriented edge, so all new graphic risk lies in the
prefix and returns.

### 4.3 Root-basis extension

The old terminal `azS` is naturally paired with the unused root `azR`
because `M_0(azR)=azS`.  After reversal the terminal is `U`, while

\[
                              azR\not\subset U.      \tag{4.12}
\]

Thus even the zero-child isolated reversal breaks the old hole--terminal
containment matching.  For one actuator it extends precisely when the
modified containment graph has a perfect matching, equivalently when the
old matching has an alternating augmenting path from the displaced hole
`azR` to the new terminal `U`.  For a bank, the exact condition is full
Hall, or equivalently a family of disjoint alternating paths in the
symmetric difference with a new perfect matching.

This is also the common-cap warning.  The fixed background cells were
admissible under `M_0`; (0.10) changes their tail basis.  A simultaneous
full-block/background transport theorem is required.  Palette equality of
the two terminal edges does not prove compiler admissibility.

## 5. Repeat-upper and owner capacity

Start from a `C`-component upper-exact Catalan forest.  A compact socket
has `h` edges all of upper colour `B`.  At most one is the representative
copy of `B`; its other `h-1` edges are repeat-upper edges.  A final spanning
Hamilton path has exactly `C-1` edges beyond the `W-C` representative
upper palette.  Therefore every edge-disjoint bank of `b` compact sockets
satisfies

\[
 \boxed{(h-1)b\le C-1.}                              \tag{5.1}
\]

This conclusion is independent of the number of extraction cuts.  More
formally, if `R` old distinct upper witnesses are deleted, the socket
parents restore at most `b` of them and all other casualties need `R-b`
return edges.  The net edge gain is at least `b(h-1)`.

If the full socket supports are pairwise owner-disjoint, the crude owner
bound is

\[
                              (h+1)b\le W.           \tag{5.2}

\]

Equation (5.2) is not asserted for merely edge-disjoint paths, which may
share endpoints or concatenate.  Such a bank must instead be charged by
its actual owner-union and degree-two component ledger.

Distinct long chains have disjoint terminal triples `(U,zL,azS)`, distinct
lower pairs `(L,zS)`, and distinct terminal upper pairs `(zU,azL)`.  Their
additional `h-1` facets need not be disjoint.  Hence (5.2) is not
sufficient: the padding supports require an owner SDR, and their return
columns require the labelled matching and graphic rows in Section 4.

Short chains supply no terminal actuator.  A short D option already has
the opposite edge `azS->zL` and there is no long owner `U` giving the
right-hand direct provider in (0.7).

## 6. Exact standard-GK bank capacity

For this section, a **clean standard-GK socket bank** means that the
representative upper-exact layer remains a standard flexible four-row GK
selection.  The terminal reversal changes only the orientations/rooted
assignments of its two displayed representative edges; padding
extractions are returned without changing the option/provider counts
entering `D_long`, apart from the explicitly counted short rethreads and
intact direct providers.  A padding cascade which replaces those rows by
nonstandard representative edges is a changed-base construction and is
outside the ceiling below.

There are

\[
 E={2m-3\choose m-3}={m-2\over2}c                  \tag{6.1}
\]

long native `zU` provider rows.  The all-`G` target augmentations consume
exactly

\[
 J_G={2m-3\choose m+1}=E-I                         \tag{6.2}
\]

distinct providers.  Thus precisely `I` direct provider edges remain.
Every one-unit short rethread replaces one of these direct providers, and
every clean terminal reversal needs one intact direct provider.  This
proves (0.11).

Let \(\mathcal D\) be the selected reversed-long D chains and
\(\mathcal P\) the chains whose direct provider is intact.  The actual
clean socket bank must
lie in

\[
                            \mathcal B\subseteq
                            \mathcal D\cap\mathcal P. \tag{6.3}
\]

Neither the cardinality of \(\mathcal D\) nor that of \(\mathcal P\)
proves a large intersection.  Prospectively selecting \(\mathcal B\)
requires the
all-`G` provider matching to avoid it:

\[
 |N_{allG}(X)\setminus\mathcal B|\ge |X|
 \quad\hbox{for every family of all-`G` targets }X.  \tag{6.4}
\]

It also requires every selected `U` to be an exposed source, or else the
terminal-suffix child of Section 3.2 must be closed.

Before neutral conjugate transfers, a clean bank has

\[
 \kappa_a^*=c-D_{long}+1+b,
 \qquad
 \kappa_z^*=1-I+p+b.                                \tag{6.5}
\]

If a neutral component transfers `r` units from `a` to `z`, the two cuts
are feasible exactly when a reachable component subset gives

\[
 I-1-p-b\le r\le c-D_{long}+1+b.                   \tag{6.6}
\]

In particular, total current gives (0.12).  Equations (0.11),(5.1),
(6.3),(6.4), and (6.6) are all independent necessary rows.

Every chosen reversal also spends one unit of ordinary current at each of
`x` and `y`.  If \(d_{\mathcal B}(q)\) is the number of selected increment
pairs containing ordinary coordinate `q`, then the complete bank needs the
coordinatewise reserve inequalities

\[
 d_{\mathcal B}(q)+d_{pad}(q)
       \le \kappa_q^{reserve}+g_q^{other}
 \qquad(q\in G),                                    \tag{6.7}
\]

where `d_pad` is computed from (4.5), not estimated by gross socket size.

## 7. Two sharp standard-GK ceilings

The GK diagonal-image theorem gives

\[
                         D_{long}\ge K-c.            \tag{7.1}
\]

### Theorem 7.1 (no rescue after activating every short root)

Suppose first that all `p=c` one-unit short rethreads have already been
used.  The remaining current deficit at the best value in (7.1) is

\[
                         \Delta_m=K+I-3c-2.          \tag{7.2}
\]

Only `I-c` intact direct providers remain, so clean gain-two sockets can
supply at most `2(I-c)`.  For every `m>=14`,

\[
 \Delta_m-2(I-c)=K-I-c-2
 =c\,{m^3-16m^2+31m-12\over
             2(2m-3)(m+1)}-2>0.                    \tag{7.3}
\]

Hence the compact terminal bank cannot rescue the already-all-short
standard state from `m=14` onward.

#### Proof

The cubic in (7.3) equals `30` at `m=14`.  Its derivative is positive and
increasing thereafter; the displayed Catalan multiple already exceeds
`2` at `m=14`.  \(\square\)

### Theorem 7.2 (reoptimized clean short/socket bank)

Allow `p,b` to be reoptimized jointly.  From (0.11),

\[
                             p+2b\le2I.              \tag{7.4}
\]

By (0.12),(7.1), passage needs

\[
                             p+2b\ge K+I-2c-2.       \tag{7.5}
\]

For every `m>=19`,

\[
 (K+I-2c-2)-2I=K-I-2c-2
 =c\,{m^3-20m^2+33m-6\over
             2(2m-3)(m+1)}-2>0.                    \tag{7.6}
\]

Thus no clean standard-GK bank made from the one-unit short rethreads,
the gain-two terminal sockets, and neutral conjugate switches can pass
both active current rows for `m>=19`.

#### Proof

The cubic in (7.6) is negative at `m=18`, equals `260` at `m=19`, and is
strictly increasing thereafter.  Equations (7.4),(7.5) are incompatible.
Neutral conjugate switching preserves `kappa_a+kappa_z`, so it cannot
repair the failure.  \(\square\)

The thresholds are scope-sharp for these scalar rows only.  For
`m=10,...,13`, sockets may fit after all short gains; for
`m=14,...,18`, only a reoptimized short/socket mixture remains scalarly
possible.  None of the owner, provider-Hall, root-basis, residence,
ordinary-current, repeat-upper, or graphic rows is automatic there.

There are two useful robustness corollaries.

1. Even if the shared-provider obstruction is bypassed but every actuator
   remains exactly gain two and every full socket has `h>=3`, (5.1) gives
   total gain at most `C-1`; this is below (7.2) for every `m>=24` because
   `Delta_m-(C-1)=K-5c-1>0`.  Indeed

   \[
        {K\over c}={(m-2)(m-3)\over2(2m-3)},        \tag{7.7}
   \]

   which first exceeds `5+1/c` at `m=24` and increases thereafter.
2. On the **fixed-tail direct-extraction face** where every new socket
   lower is unused or its incumbent provider is already one of the
   incident arcs counted in Section 4.2, a compact extraction touches at
   most `2(h+1)` host arcs.  Its active gain is then at most `2(h+1)`
   before child taxes.  Combining this with (5.1) gives at most `4(C-1)`
   for `h>=3`, below (7.2) for every `m>=71`, since

   \[
   \Delta_m-4(C-1)=K-11c-3I+2,
   \quad
   {2(2m-3)(m+1)\over c}(K-11c-3I)
      =m(m^2-72m+107).                              \tag{7.8}
   \]

   The last polynomial is positive from `m=71` onward.  A basis-changing
   socket with additional remote lower-provider deletions, or any
   noncompact cascade, is outside this bound.

## 8. Reconciliation with the authoritative `m=9` / `k=17` v7 state

The finite `k=17` socket lane has advanced strictly beyond pairwise seam
support.  The authenticated v7 bank has

\[
 38\text{ sockets},\qquad 6258\text{ final resident pieces}, \tag{8.1}
\]

and closes its raw rank-ten socket-support row.  This is not contradicted
by Theorem 7.2: here `m=9`, before the universal standard-GK current
ceiling, and the finite task is no longer the two active-current cuts.

The exact contextual seam census has `100` rank-ten colours with zero
context-extendable ordinary seam support.  Every one of those `100` rows
has an explicit compact `L=3` socket.  Their individual minimum extra-cut
sum is

\[
                              213.                  \tag{8.2}
\]

Exactly `99` are child-clean.  The sole first-generation child is `14309`,
and it has child-clean compact sockets.  This statement is individual, not
simultaneous: the round-one clean `L=3` child shares facet `10213` with its
displayed parent `75749`, while the generation-three `L=3/L=4` rows collide
with frozen socket `69605` on guard segment `755`.  The generation-three
`L=5` row is the presently certified parent-plus-bank-compatible child
closure.  Thus neither local socket existence nor pairwise seam enumeration
is the finite gate.

The correct v7 master is a **joint multi-choice selector**.  It must choose
facet orders, component options and guards simultaneously, with

1. owner and lower-resource capacity;
2. all named child/provider rows, including regenerative use of the
   `14309` socket;
3. the modified hole--terminal/common-basis Hall row from Section 4.3;
4. contracted graphic independence and a final chronology;
5. arbitrary-depth upper replay, not merely raw rank-ten support; and
6. the final occurrence-labelled common-cap compiler.

This finite selector is an instance of the exact column system in Sections
4--6, but not evidence for the clean all-`m` supply inequalities.  The
separately proved noncanonical pivot-rich geodesic packet is also a valid
changed-base route; it is not a missing lemma and lies outside the clean
standard-GK ceiling by definition.

More sharply, the displayed one-`L=3`/one-`L=4` menu is not itself a
packing: targets `8060` and `15996` force the same facet `7804` and
incompatible component-22 options `6` and `3`.  Freezing all old 38 sockets
leaves 88 targets locally dead after exact guard-domain propagation.  Hence
the word “joint” above necessarily includes reselection of the old sockets,
not merely appending the 100 new rows.  The exact scoped theorem is
`MATH_THEOREM_THREAD_D_K17_V7_SOCKET_MULTICHOICE_AND_REGENERATIVE_GATE_20260801.md`.

## 9. Exact surviving gate and scope

The compact facet socket is therefore correctly classified as follows.

* **Rail alone:** resident under its explicit guards, with a complete
  lower chain, but intrinsically a negative current column and only a
  one-unit orientation transfer.
* **Prepared long terminal:** the last rail edge plus the direct-provider
  seam realizes the exact gain-two reversal (0.9), with no terminal
  palette or graphic loss.
* **Full physical socket:** gain two survives only if the padding
  extraction is `a,z`-neutral, every named child is restored, the changed
  hole--terminal basis extends, all background common-cap cells remain
  admissible, and the contracted graphic and residence rows pass.
* **Clean standard bank:** unable to solve all dimensions; the shared
  direct-provider ledger closes it for `m>=19`.

An all-dimensional escape must violate at least one clean-bank premise:

1. reuse a `zU` provider already occupied by a short/all-`G` packet through
   a closed alternating cascade;
2. share or recycle the `h-1` repeated parent-upper edges across many
   actuators;
3. create more than two hard-current units per packed aperture; or
4. change the standard GK upper-exact/component ledger or rooted basis on
   a macroscopic correlated set.

The theorem does not claim that any finite surviving bank passes the
common-cap compiler, deeper shadows, or literal chronology.  It isolates
the exact positive actuator and proves the strongest clean standard-host
ceiling presently available.

## 10. Independent audit

The lightweight independent audit

* exhausts the one-edge identity and ordered compact sockets on small
  Boolean layers;
* reconstructs the standard GK fixed-`M_0` facet digraph through `m=9`;
* checks the terminal reversal as a literal lower/upper/undirected set
  identity for `m=4,...,20`; and
* verifies the exact first-failure dimensions `14`, `19`, `24`, and `71`
  for the four scoped ceilings above.
* independently replays the v7 counts in (8.1),(8.2), the `100/99/1`
  child split, and the clean second-generation socket for `14309`.

Artifacts:

* `scratch/audit_k_resident_facet_socket_current_ceiling_20260801.py`,
  SHA-256 `84e1c8665ccdb43b7a0b0c6b0fcd2818332209ef3486192918545d7349b82ff4`;
* `scratch/k_resident_facet_socket_current_ceiling_20260801.audit.json`,
  SHA-256 `8775b82a3314d614fcca251ae31b46e1e0b908b24c747f22ac7ce6372fb3e07f`.

The source local residence theorem is
`MATH_THEOREM_RESIDENT_FACET_SOCKET_20260801.md`, SHA-256
`b57c7cace40a3fcc3f93bba7d1c96446cb99c909ea73b6008a4a16867169ab1c`.
The preceding standard-GK current ceiling is
`MATH_THEOREM_K_SCD_CONJUGATE_HYBRID_CURRENT_CEILING_AND_OPEN_ACTUATOR_GATE_20260801.md`,
SHA-256 `548e84adad6e1213e17f7f3ae37c935b622163598ed7ed6e640958e944fcd8d8`.
