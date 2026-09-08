# Endpoint-current audit of the resident facet socket

Date: 2026-08-01  
Lane: Thread D / SCD endpoint current / resident facet extraction  
Status: unconditional local current and child-colour ledger.  The resident
facet theorem supplies a legal path block, but by itself supplies no
positive-current extraction column.  A component-preserving embedding is
globally current-neutral; its gain on selected coordinates is exactly an
insertion-label transfer from the removed ambient arcs.

## 1. The Johnson-arc current identity

Let `X->Y` be an oriented Johnson edge between rank-`r` owners.  Put

\[
 \ell(X,Y)=X\cap Y,
 \qquad \iota(X,Y)=Y\setminus X.
\]

Thus `iota(X,Y)` is a singleton.  In the endpoint-current notation, using
this edge services the lower colour `ell(X,Y)` and consumes the incoming
source ticket at its head `Y`.  Its signed contribution is

\[
 j_q(X,Y)={\bf1}_{q\in X\cap Y}-{\bf1}_{q\in Y}.
\]

### Lemma 1.1 (one edge is one negative insertion letter)

For every coordinate `q`,

\[
 \boxed{j_q(X,Y)=-{\bf1}_{q\in\iota(X,Y)}.}       \tag{1.1}
\]

Consequently, if a legal rethread removes an arc multiset `E^-` and adds
an arc multiset `E^+`, then

\[
\begin{aligned}
 \Delta H_q
   &=\sum_{e\in E^-}{\bf1}_{q\in\ell(e)}
     -\sum_{e\in E^+}{\bf1}_{q\in\ell(e)},\\
 \Delta S_q
   &=\sum_{e\in E^-}{\bf1}_{q\in\operatorname{head}(e)}
     -\sum_{e\in E^+}{\bf1}_{q\in\operatorname{head}(e)}.
                                                        \tag{1.2a}
\end{aligned}
\]

Indeed, deleting an old edge exposes its lower colour as a hole and its
head as a source; adding a new edge consumes both.  Hence
`Delta kappa_q=Delta S_q-Delta H_q`, and

\[
 \boxed{
 \Delta\kappa_q
  =d^-_q-d^+_q,
 \qquad
 d^\pm_q=|\{e\in E^\pm:\iota(e)=q\}|.}          \tag{1.2b}
\]

In particular,

\[
 \boxed{\sum_q\Delta\kappa_q=|E^-|-|E^+|.}       \tag{1.3}
\]

#### Proof

Write `Y=K+y` and `X=K+x`, where `K=X cap Y` and `y` is the
unique element of `Y-X`.  Then

\[
 {\bf1}_K-{\bf1}_{K+y}=-{\bf1}_{\{y\}}.
\]

This is (1.1).  Removing an edge negates its contribution and adding an
edge contributes it, which proves (1.2b).  Summing (1.1) over coordinates
gives `sum_q j_q(e)=-1` for every edge and proves (1.3).  Notice that
(1.1) already combines the serviced lower colour and the consumed head.
Charging them once more as independent benefits is the same double count
that invalidated the apparent gain-two paired-ear ledger.  \(\square\)

For a directed linear forest on a fixed owner set, `|E|=|V|-c(F)`, so
(1.3) can also be written

\[
                \sum_q\Delta\kappa_q
                  =c(F^+)-c(F^-).                 \tag{1.4}
\]

Thus a rethread which preserves the number of path components cannot
create total coordinate current.  A detached extra component creates one
unit, but the edge which later reconnects that component consumes exactly
one unit again, in its insertion coordinate.

## 2. Exact compact-socket ledger

Let `U` be a rank-`(r+1)` block and choose distinct

\[
                    v_0,v_1,\ldots,v_t\in U.
\]

Put `F_i=U-v_i` and orient the facet path forward:

\[
                    F_0\longrightarrow F_1
                    \longrightarrow\cdots\longrightarrow F_t. \tag{2.1}
\]

For the compact resident socket, `t=h`; for the self-buffering socket,
`t=2h+1`.

The `i`th edge has the exact ordered transition

\[
 F_i\setminus F_{i+1}=\{v_{i+1}\},
 \qquad
 F_{i+1}\setminus F_i=\{v_i\},                    \tag{2.2}
\]

upper colour `U`, and lower colour

\[
                     K_i=U-\{v_i,v_{i+1}\}.       \tag{2.3}
\]

The `K_i` are pairwise distinct.  Their complete coordinate-degree ledger
is

\[
 d_K(q)=\sum_{i=0}^{t-1}{\bf1}_{q\in K_i}
 =\begin{cases}
 0,&q\notin U,\\
 t,&q\in U-\{v_0,\ldots,v_t\},\\
 t-1,&q=v_0\text{ or }q=v_t,\\
 t-2,&q=v_j,\quad 1\le j\le t-1.
 \end{cases}                                      \tag{2.4}
\]

The consumed head owners are `F_1,...,F_t`, with coordinate degrees

\[
 d_H(q)=\sum_{i=1}^{t}{\bf1}_{q\in F_i}
 =\begin{cases}
 0,&q\notin U,\\
 t,&q\in U-\{v_1,\ldots,v_t\},\\
 t-1,&q=v_j,\quad1\le j\le t.
 \end{cases}                                      \tag{2.5}
\]

Subtracting (2.5) from (2.4) gives the intrinsic socket current

\[
 \boxed{j(P)=-\sum_{i=0}^{t-1}{\bf e}_{v_i}.}     \tag{2.6}
\]

The terminal omitted label `v_t` is the unique selected label spared by
the forward orientation.  Reversing the path gives

\[
 \boxed{j(P^{\rm rev})=-\sum_{i=1}^{t}{\bf e}_{v_i},} \tag{2.7}
\]

so the reverse orientation instead spares `v_0`.

Equations (2.4)--(2.7) are the exact child cut-colour and endpoint ledgers.
For example, if a coordinate `z` belongs to every facet but is not one of
the selected omitted labels, then all `t` new lower colours contain `z`,
but all `t` consumed heads also contain `z`; its net gain is zero.  If
`z=v_i` is nonterminal, the lower service falls short of the consumed-head
count by one, and the socket has `z`-current `-1`, not `+1`.  If `z` is the
terminal omitted label, the two counts agree and its current is zero.

The upper ledger is also exact: (2.1) contributes `t` copies of `U`.  If
`U` was previously missing, one copy restores it and the remaining `t-1`
copies enter the repeated-upper multiset.  Therefore a global Hamilton-path
application must charge `(t-1) 1_U` to the repeat-upper cocycle; these
copies are not free palette rows.

In particular, for `t>=2` the socket is **not** an edge switch inside the
upper-injective forest face used by the preceding SCD current theorem.  It
lives in the larger upper-surjective/repeated-upper connector model.  To
compare it with an upper-exact base, all `t-1` excess copies of `U` and the
same number of displaced repeat slots must be included in the extraction
column.  Omitting that row would be another palette double count.

The complete consecutive lower tower is equally rigid.  At depth
`q=1,...,t`, the socket exposes

\[
 K^{(q)}_i=\bigcap_{s=0}^{q}F_{i+s}
          =U-\{v_i,v_{i+1},\ldots,v_{i+q}\},
 \qquad 0\le i\le t-q.                              \tag{2.8}
\]

These are `t+1-q` distinct rank-`(r-q)` colours.  A selected label `v_j`
occurs in exactly

\[
 (t+1-q)-
 \left(\min(j,t-q)-\max(0,j-q)+1\right)_+           \tag{2.9}
\]

of them, while every coordinate of `U-{v_0,...,v_t}` occurs in all
`t+1-q`.  Thus a compiler using the socket must reserve the entire
triangular family (2.8), not only its immediate intersections (2.3).

## 3. Exact extraction-and-rethread signature

Let `R` be any set of ambient Johnson arcs removed in order to extract the
facets, and let `B_ext` contain every added bypass, exterior guard, and
attachment arc other than the internal socket edges.  For the forward
orientation, (1.2b) and (2.6) give

\[
 \boxed{
 \Delta\kappa_q
 =|\{e\in R:\iota(e)=q\}|
  -|\{e\in B_{\rm ext}:\iota(e)=q\}|
  -{\bf1}_{q\in\{v_0,\ldots,v_{t-1}\}}.}          \tag{3.1}
\]

For an active coordinate set `A` (in particular `A={a,z}`),

\[
 \boxed{
 \Delta\kappa_A
 =d_R(A)-d_{B_{\rm ext}}(A)
  -|A\cap\{v_0,\ldots,v_{t-1}\}|.}                \tag{3.2}
\]

This is a necessary and sufficient signed-current test once the literal
ambient arcs have been specified.  In particular, the local resident
facet theorem does not determine even the sign of `Delta kappa_A`: it
specifies the last term of (3.2), but it specifies neither of the first
two terms.

There is a sharper obstruction for the most literal extraction attempt.
Suppose one merely replaces the old outgoing arc of every socket tail
`F_i`, `0<=i<t`, by the forward socket arc.  If
`F_i->Y_i` is a Johnson arc, its insertion label lies outside `F_i`.
Because `U-F_i={v_i}`, one has

\[
 \iota(F_i,Y_i)\in U\quad\Longrightarrow\quad
 \iota(F_i,Y_i)=v_i.                              \tag{3.2a}
\]

Consequently, for every active coordinate set `A subseteq U`, the removed
outgoing arcs contribute at most `|A cap {v_0,...,v_(t-1)}|`, exactly the
forced socket charge in (3.2).  Added exterior arcs can only decrease the
current further.  Hence **outgoing-facet replacement alone has
`Delta kappa_A<=0`**.  Positive active current must be supplied by deleted
incoming arcs or by a genuinely nonlocal background rethread.

There is a useful normal form when the `t+1` facets are extracted from
pairwise disjoint internal positions.  Write the old local arcs as

\[
                 P_j\to F_j\to Q_j,
                 \qquad 0\le j\le t,
\]

and suppose every bypass `P_j->Q_j` is itself Johnson.  Removing the
`2(t+1)` old arcs, adding the `t+1` bypasses, and adding the `t` socket
arcs leaves the socket as one new detached path.  Its exact current is

\[
\begin{split}
 \Delta\kappa_q={}&
 \sum_{j=0}^{t}
 \bigl({\bf1}_{\iota(P_j,F_j)=q}
      +{\bf1}_{\iota(F_j,Q_j)=q}
      -{\bf1}_{\iota(P_j,Q_j)=q}\bigr)\\
 &-\sum_{i=0}^{t-1}{\bf1}_{v_i=q}.                 \tag{3.3}
\end{split}
\]

The coefficients in (3.3) sum to one: this is exactly the extra detached
component.  Inserting the socket into an ambient path deletes one ambient
arc and adds the two attachment arcs, restoring the old component count;
the final closed column has coefficient sum zero.

The corresponding literal palette ledger is

\[
\begin{array}{c|c|c}
 &\text{removed}&\text{added}\\ \hline
\text{lower}&
 \ell(P_j,F_j),\ \ell(F_j,Q_j)&
 \ell(P_j,Q_j),\ K_0,\ldots,K_{t-1}\\
\text{upper}&
 P_j\cup F_j,\ F_j\cup Q_j&
 P_j\cup Q_j,\ U^{\times t}.
\end{array}                                        \tag{3.4}
\]

Any insertion-site boundary arcs must be appended to the appropriate
column of (3.4).  Thus the finite extraction cascade is not encoded by
`U` and the facet order: the old neighbours `P_j,Q_j`, the bypasses, and
the insertion boundaries determine every new casualty.

### Lemma 3.1 (positive current forces an upper-provider cascade)

Assume the ambient forest is upper-injective and `U` is missing.  Every
removed arc counted by `d_R(A)` has a distinct old upper colour different
from `U`.  The internal socket arcs restore only `U`.  Therefore a closed
column with active-current gain `g>0` needs at least `g` external repairs
of distinct lost upper colours whose added insertion labels lie outside
`A` (or an equivalent correlated repair with the same signed ledger).

#### Proof

Upper injectivity makes the upper colours of removed arcs distinct.  None
is `U`, because `U` had no old provider.  Each removed insertion label in
`A` contributes one positive unit in (3.2).  An added repair whose insertion
label is also in `A` cancels one such unit.  Hence retaining net gain `g`
requires at least `g` restored old colours without an `A`-label charge.
The socket's `t` internal copies of `U` restore none of those colours.
\(\square\)

Thus a facet socket can be a useful **carrier** of current, but it never
eliminates the provider problem.  Its positive-current columns are exactly
upper-loss/repair cascades, not free local absorbers.

### Proposition 3.2 (sharp all-depth raw transporter)

The obstruction does not say that the hard-coordinate sign is always
nonpositive.  Fix `z notin U` and

\[
 x\in U-\{v_0,\ldots,v_t\}.
\]

For `0<=i<t`, replace the outgoing arcs

\[
 F_i\longrightarrow F_i-x+z
\]

by the facet-path arcs `F_i->F_(i+1)`, regarding `F_t` as an isolated old
vertex.  The old arcs insert `z` and have distinct upper colours
`U-v_i+z`; the new arcs insert `v_i` and all have upper colour `U`.
Therefore

\[
 \boxed{\Delta\kappa
       =t e_z-\sum_{i=0}^{t-1}e_{v_i}},             \tag{3.5}
\]

while the signed upper coordinate-incidence ledger is

\[
 \boxed{t\mathbf1_U-
        \sum_{i=0}^{t-1}\mathbf1_{U-v_i+z}
       =\sum_{i=0}^{t-1}e_{v_i}-t e_z
       =-\Delta\kappa.}                            \tag{3.6}
\]

Thus, if neither hard coordinate is among the omitted `v_i` and one is
`z`, the hard-pair current gain is exactly `t` for every `t`.  It is a
uniform positive transporter, not a closed positive actuator: every unit
is paired with one distinct lost cofacet child.

## 4. Finite exact-19 calibration: a positive raw signature is not closure

The frozen `k=17` exact-19 support assignment contains one reconstructible
compact `h=3` row which is useful as a sign check.  Its provenance is

* `scratch/k17_m9_support_master_residual19_compact_sockets_20260801.tsv`,
  target `U=70398`, length `4`;
* `scratch/k17_allmin_support_closure_20260801/k17_support_b19_m1.solve.out`
  with its map and verified residual row
  `(component,pattern,option,cut)=(1053,2131,1,4)`.

The proposed new owner segment is

\[
 82684\to70396\to70394\to70390\to70270\to67198,   \tag{4.1}
\]

where the four central owners are the facets of `70398` omitting zero-based
labels `(1,2,3,7)`.  Direct bit replay gives new insertion labels

\[
                         (12,1,2,3,10),             \tag{4.2}
\]

new lower colours

\[
                 (66300,70392,70386,70262,66174),  \tag{4.3}
\]

and new upper colours

\[
                 (86780,70398,70398,70398,71294).  \tag{4.4}
\]

The six deleted ambient arcs have insertion labels

\[
                         (16,15,5,10,2,0).          \tag{4.5}
\]

Therefore (1.2b) gives the raw exact signature

\[
 \boxed{
 \Delta\kappa
 =e_{16}+e_{15}+e_5+e_0-e_{12}-e_1-e_3.}          \tag{4.6}
\]

Its coefficient sum is `+1`, and with the distinguished coordinates
`(a,z)=(15,16)` it has raw two-coordinate gain `+2`.  This is genuine
evidence that a facet extraction can transfer current into the two hard
coordinates.  It does not contradict Section 3: the raw row has one extra
path component.

Nor is it a legal closed column.  The lower colours `70392` and `66174`
collide with retained old edges.  Releasing those two edges, whose insertion
labels are `0` and `15`, changes the formal lower-clean signature to

\[
 e_{16}+2e_{15}+e_5+2e_0-e_{12}-e_1-e_3,          \tag{4.7}
\]

whose coefficient sum is `+3`: the apparent strengthening is exactly two
additional unresolved component releases.  The row also loses seven upper
colours; `70391` has no extendable one-seam provider in the frozen atlas.
In (4.4), the three copies of `70398` are one restored occurrence plus two
repeats, and `86780` is a third repeat because another occurrence remains.

Thus the exact-19 calibration proves both sides of the abstract result:
positive `a+z` signatures exist, but the first such signature currently
known is paid for by component, lower-palette, repeated-upper, and casualty
debts.  It is a scoped lead, not an all-dimensional actuator.

## 5. Consequence for the endpoint-current gate

The resident facet socket is not intrinsically a non-neutral actuator.

* As a block added to isolated facets, its current is coordinatewise
  nonpositive by (2.6).
* In a component-preserving extraction and rethread, its total current is
  zero by (1.4).
* It may nevertheless have positive `a+z` current, but only when the
  removed ambient arcs have more `a/z` insertion labels than the socket,
  bypasses, and attachment arcs together.  Equation (3.2), not the number
  of serviced facet colours, is the exact criterion.  Any such gain is a
  transfer from the other coordinates.
* Leaving the socket as one additional path gives one unit of total current,
  but this is precisely one unresolved topology component.  Closing that
  component consumes the unit again.

Accordingly, an all-dimensional positive theorem needs a typed extraction
bank whose columns include the complete data in (3.3)--(3.4) and satisfy,
for the two-coordinate deficit set,

\[
 \sum_s x_s\,
 \Bigl(d_{R_s}(\{a,z\})-d_{B_{{\rm ext},s}}(\{a,z\})
       -|\{a,z\}\cap V_s^{\to}|\Bigr)
 \ge I_m-c+D_{\rm long}-2,                         \tag{5.1}
\]

where `V_s^to={v_0,...,v_(t-1)}` (use `{v_1,...,v_t}` in reverse).
This must hold together with owner disjointness, lower-colour injection, the repeated-upper
cocycle, rooted degree, residence guards, and graphic independence.  The
local socket theorem proves the legality of its internal path and gives the
last term of each column.  It proves neither the positive sign nor the
supply required by (5.1).

This is also the precise interface with the finite exact-19 cascade: that
cascade computes the missing ambient terms in (3.3)--(3.4).  Its extraction
counts cannot be converted into endpoint-current gain without decoding the
ordered insertion labels of every removed, bypass, and attachment arc.
