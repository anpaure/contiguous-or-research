# Boolean shadow cuts, an optimal SCD socket funnel, and exact canonical
# owner-layer obstructions

Date: 2026-08-01  
Lane: owner-layer upper representatives and free-port connectors  
Status: unconditional Boolean cut identities, an unconditional
`Cat_(m-1)` prospective socket construction, and exact obstructions to the
raw Greene--Kleitman/canonical-order route.  A correlated upper-exact
four-funnel forest containing the tight-pivot phase is not constructed.

## 0. Outcome

Fix a perfect incidence matching `M_0` between ranks `m-1` and `m` of
`[2m-1]`, and let `Q_0` be an upper-exact rooted Catalan forest.  This note
adds five exact facts to the coloured directed-path reduction.

1. Every connector Hall cut has an exact restricted-shadow formula,
   including the same-component closing correction that ordinary shadow
   counts miss.
2. Kruskal--Katona gives a useful positive shell theorem: at Catalan scale,
   distinct terminal roots can be assigned distinct containing rank-`m`
   owner labels while avoiding `m-1` prescribed labels.  This does not
   assign the free incoming roots.
3. One fixed pair of coordinates and one SCD give exactly
   `Cat_(m-1)` pairwise resource-distinct legal connector sockets.  This is
   best possible for that fixed funnel.  Scalar coverage of `Cat_m` ports
   therefore needs four funnels for `m>=6`.
4. The unchanged Greene--Kleitman chain-mate upper transversal is never a
   matching for `m>=3`: one explicit fibre has `m-1` distinct colours and
   one common head.  Any repair retaining the coordinate-sum monotonicity,
   or retaining the same canonical ballot bank on both port shores, still
   fails one-defect Hall.
5. Already at `m=3`, one upper-exact `Q_0` fails Hall by two, while another
   passes every one-defect Hall cut but can complete only through a directed
   two-cycle.  Hall expansion and acyclic serialization are independent.

Thus the first live unrooted prospective construction is a **correlated
four-funnel/four-sector upper-exact forest with nonmonotone resets**.  The
tight-pivot version is stronger: its perfect matching must contain the
predecessor phase and its rooted connector order must start at the protected
successor component.  Raw Kruskal--Katona, one canonical SCD funnel, or a
post-hoc total order cannot close either gate.

Greene--Kleitman is used only as calibration.  The independently proved
protected branch DP has deletion density
`0.356895867892...`, and local matching squares cannot detach its two
extreme stars.  Nothing below proposes pruning or locally repairing that
support.  The positive SCD object in Section 4 is instead a born-linear
socket bank selected directly in a new perfect matching.

No finite search is used below.  The `m=3` examples are literal deductions
from the frozen arc table in
`MATH_THEOREM_OWNER_LAYER_RAINBOW_PATH_CUT_COUNTEREXAMPLE_AND_ACYCLIC_HALL_20260801.md`.

## 1. Exact Boolean endpoint cuts

Let `mathcal C=Comp(Q_0)`.  Orient every component as a directed path.  For
`K in mathcal C`, let

\[
 s_K=\text{its free incoming root},\qquad
 o_K=\text{its free outgoing root},\qquad
 J_K=M_0(s_K).                                      \tag{1.1}
\]

Thus `s_K,o_K` have rank `m-1`, while `J_K` has rank `m`.  Put

\[
                         \mathcal J=\{J_K:K\in\mathcal C\}.
\]

### Theorem 1.1 (restricted-shadow connector identity)

The full free-port component graph has the literal rule

\[
 \boxed{K\longrightarrow K'
   \iff K\ne K'\text{ and }o_K\subset J_{K'}.}       \tag{1.2}
\]

For `X subseteq mathcal C`, put

\[
 \mathcal T_X=\{o_K:K\in X\}
\]

and put

\[
 e_X=\#\{K'\in X:\{K\in X:o_K\subset J_{K'}\}=\{K'\}\}.
\]

Then

\[
 \boxed{|N(X)|=|\mathcal J\cap\partial^+\mathcal T_X|-e_X.} \tag{1.3}
\]

Consequently the matching deficiency of the full port graph is

\[
 \boxed{
 \delta(Q_0)=\max_{X\subseteq\mathcal C}
 \bigl(|X|-|\mathcal J\cap\partial^+\mathcal T_X|+e_X\bigr).} \tag{1.4}
\]

One-defect Hall is exactly `delta(Q_0)<=1`.

#### Proof

An incidence from `o_K` to the middle set `J_(K')` contracts to an arc
whose head is `M_0^(-1)(J_(K'))=s_(K')`.  When `K!=K'`, this incidence is
not the matching edge of `o_K`, because the lower root `o_K` belongs to a
different component from `s_(K')`.  This proves (1.2).

The intersection in (1.3) counts precisely the incoming-port labels which
contain some terminal in `X`.  The only counted labels which are not legal
external neighbours are those supported solely by their own component's
terminal; their number is `e_X`.  This proves (1.3).  The deficiency form
of Hall gives (1.4). \(\square\)

### Corollary 1.2 (principal-filter cuts)

For every coordinate set `A`, one-defect Hall requires

\[
 \#\{K:A\subseteq J_K\}
 \ge \#\{K:A\subseteq o_K\}-1.                      \tag{1.5}
\]

Indeed every neighbour of a terminal containing `A` has its matched
middle label containing `A`.

This shows why an unconditioned shadow theorem is insufficient.  For
`m>=4`, each of the families

\[
 \{L:z\in L,\ |L|=m-1\},\qquad
 \{T:z\notin T,\ |T|=m\}
\]

has at least `Cat_m` members.  Choosing `Cat_m` outgoing roots from the
first and `Cat_m` incoming middle labels from the second makes the cut
`A={z}` fail maximally.  These abstract endpoint banks are not asserted to
come from an upper-exact `Q_0`; they prove that sizes and full-shadow
expansion alone cannot select the incoming bank.

## 2. The exact Catalan-scale shadow surplus

Put

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad C=\operatorname {Cat}_m.
\]

### Theorem 2.1 (central Kruskal--Katona surplus)

For every nonempty `mathcal X subseteq mathcal L` with `|mathcal X|<=C`,

\[
 \boxed{|\partial^+\mathcal X|\ge |\mathcal X|+m-1.} \tag{2.1}
\]

#### Proof

Complement `mathcal X` to a family of rank-`m` sets and put
`x=|mathcal X|`.  Suppose first that `m>=4`.  Since

\[
 C< {2m-2\choose m},
\]

write

\[
 x={s\choose m}+b,qquad
 m\le s\le2m-3,qquad 0\le b<{s\choose m-1}.         \tag{2.2}
\]

The initial colex family consists of all rank-`m` sets on `[s]` and `b`
further sets containing `s+1`.  Kruskal--Katona therefore gives

\[
 |\partial^+\mathcal X|
 \ge {s\choose m-1}+\partial_{m-1}(b).              \tag{2.3}
\]

The remainder is a family of `b` rank-`(m-1)` sets on at most `s` points.
Because `s<=2m-3`, normalized matching from rank `m-1` down to rank `m-2`
gives `partial_(m-1)(b)>=b`.  Hence

\[
 |\partial^+\mathcal X|-x
 \ge D(s):={s\choose m-1}-{s\choose m}.             \tag{2.4}
\]

Now `D(m)=m-1`, and

\[
 D(s+1)-D(s)={s\choose m-2}-{s\choose m-1}\ge0
\]

through `s<=2m-3`.  This proves (2.1).  At `m=3`, the exact minimum
shadow sizes for `x=1,2,3,4,5` are respectively

\[
                              3,5,6,6,8,
\]

which gives the same surplus two. \(\square\)

### Corollary 2.2 (robust prospective owner shell)

Let `mathcal T` be at most `C` distinct rank-`(m-1)` terminal roots, and
delete any family `F` of at most `m-1` rank-`m` labels.  There is an
injection

\[
 \psi:\mathcal T\longrightarrow{[2m-1]\choose m}\setminus F,
 \qquad L\subset\psi(L).                             \tag{2.5}
\]

#### Proof

For every nonempty `X subseteq mathcal T`, Theorem 2.1 gives

\[
 |\partial^+X\setminus F|
 \ge |X|+m-1-|F|\ge|X|.
\]

Hall applies. \(\square\)

The allowance `m-1` is sharp: deleting all `m` supersets of one terminal
kills every possible label for it.  Corollary 2.2 solves only the owner
label shell.  It does not make those labels equal to the free matched
middle bank `mathcal J`, choose their lower preimages, or build `Q_0`.

## 3. Generic rainbow matching is below threshold

For a fixed `M_0`, every immediate-upper colour has `m+1` candidate arcs,
while the tail--head occurrence graph has maximum degree `Delta=m-1`.

The Aharoni--Berger--Meshulam bounded-degree theorem guarantees a full
rainbow matching in an `r`-uniform edge-coloured hypergraph from the generic
condition `|E_i|>=r Delta`; Wdowinski proves this sharp by constructing
examples with every class of size at least `r Delta-1` and no full rainbow
matching ([arXiv:2401.06029](https://arxiv.org/abs/2401.06029),
Theorems 1--2).  For graphs the generic
threshold is therefore `2 Delta=2m-2`.  Our Boolean class size `m+1` is
strictly below it for every `m>=4`.

Thus no argument using only maximum degree and colour-class size can choose
the upper-exact shore.  A positive theorem must use Boolean incidence and a
correlated choice of `M_0`; the false shortcut “class size greater than
`Delta` suffices” is unavailable.  Wdowinski's sharp examples are in the
multi-hypergraph universe and may use parallel edges: they do not exclude a
stronger theorem with an additional simple-bipartite hypothesis, but such a
theorem would already be using structure beyond the three generic
parameters `(r,Delta,|E_i|)`.

## 4. An optimal fixed-pair SCD socket funnel

Write

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad |G|=2m-3,
\]

and fix a symmetric-chain decomposition of `2^G`.  Put

\[
 D={2m-3\choose m-2},\qquad E={2m-3\choose m-3}.
\]

At the four central ranks, a relevant chain is either

\[
 R\subset S\subset L\subset U
\]

of ranks `m-3,m-2,m-1,m`, or a short central chain `S subset L`.  There
are `E` long chains and

\[
                         D-E=\operatorname {Cat}_{m-1} \tag{4.1}
\]

short chains.

### Theorem 4.1 (literal SCD funnel)

There is a perfect incidence matching `M_0` given by

\[
\begin{array}{c|c|c}
\text{lower type}&\text{long chain}&\text{short chain}\\ \hline
azR&azS&-\\
zS&zL&azS\\
aS&aL&aL\\
L&U&zL
\end{array}                                          \tag{4.2}
\]

such that every short chain supplies the legal connector socket

\[
 A_S=aS\longrightarrow B_S=zS,\qquad
 M_0(B_S)=T_S=azS.                                  \tag{4.3}
\]

These `Cat_(m-1)` sockets have pairwise distinct tails, heads, middle
owners and immediate-upper colours `azL`.  Their physical Johnson endpoints
are `aL` and `azS`; these two endpoint banks are separately injective and
cross-disjoint.  Hence the physical support itself is a matching.  In
particular the funnel is a born-linear partial integral solution of the
joint upper/lower/owner-cap/graphic rows, not a pruning of the
Greene--Kleitman projection.

#### Proof

The lower layer splits into the four types

\[
 azR,\quad zS,\quad aS,\quad L.
\]

The rows in (4.2) map them by literal containment onto the disjoint upper
types `azS,zL,aL,U`.  On long chains the first, second and fourth rows have
orders `E,E,E`; on short chains the missing parts have order `D-E`; the
third row has order `D` on all chains.  Thus every lower and upper set is
used exactly once, so `M_0` is perfect.

For a short chain, `M_0(zS)=azS`, while `M_0(aS)=aL`.  Hence the incidence
`aS--azS` is outside `M_0` and contracts to `aS->zS`.  Its upper colour is

\[
 M_0(aS)\cup azS=aL\cup azS=azL.
\]

Distinct SCD chains have distinct `S,L`.  The physical endpoints `aL`
omit `z`, whereas the endpoints `azS` contain it, so the two endpoint banks
are cross-disjoint as well.  This proves all injectivity and born-linearity
claims.
\(\square\)

### Theorem 4.2 (fixed-funnel capacity is sharp)

For every perfect `M_0`, a family satisfying

\[
                         M_0(zS)=azS
\]

has order at most `D-E=Cat_(m-1)`.

#### Proof

Every one of the `E` lower sets `azR` can match only into the `D` upper sets
`azS`.  The declared socket rows consume distinct members of that same
upper block.  Therefore `E+|mathcal S|<=D`.  Theorem 4.1 attains equality.
\(\square\)

Since

\[
 \frac{\operatorname {Cat}_m}{\operatorname {Cat}_{m-1}}
 =\frac{2(2m-1)}{m+1}=4-\frac6{m+1},                \tag{4.4}
\]

fixed-pair funnels need at least four classes for `m>=6` and at least three
for `3<=m<=5`, even before their sockets are fitted into one `Q_0`.

## 5. Acyclic potential reservoirs are rigid

### Theorem 5.1 (total-order collapse)

Order the `C` components as `K_1<...<K_C` and retain only forward connector
arcs.  This acyclic reservoir satisfies one-defect Hall if and only if

\[
                         K_i\longrightarrow K_{i+1}
                         \qquad(1\le i<C).            \tag{5.1}
\]

#### Proof

The forward consecutive arcs plainly form the required matching.  Conversely,
a forward matching of size `C-1` omits one source and one head.  If its
partial injection is `f(i)>i`, then each selected edge raises the index by
at least one.  The sum of its head indices minus its source indices is the
omitted source minus the omitted head, at most `C-1`.  With `C-1` edges,
equality is forced: the omitted source is `C`, the omitted head is `1`, and
`f(i)=i+1` for every `i`. \(\square\)

Thus a potential order does not turn shadow expansion into a soft
certificate.  It asks for the literal endpoint containments

\[
                         o_{K_i}\subset M_0(s_{K_{i+1}})
\]

in one complete order.

### Theorem 5.2 (height/reset lower bound)

Suppose every edge of `Q_0` and every allowed connector strictly increases
an integer potential taking only `H` values on the `W` owner vertices.  If
`nu` connectors are selected, then

\[
 \boxed{C-\nu\ge\left\lceil\frac WH\right\rceil.}   \tag{5.2}
\]

A one-component completion requires at least
`ceil(W/H)-1` non-increasing reset connectors.

#### Proof

The selected `Q_0` and connector edges form a path cover on all `W`
vertices with `C-nu` paths.  A strict-potential path has at most `H`
vertices, proving (5.2).  Cutting a completed path at every reset edge
leaves strict-potential segments, proving the second assertion.
\(\square\)

## 6. The unchanged Greene--Kleitman choice fails

This section is a calibration/no-go for the most tempting canonical
selection.  The positive-density GK pruning obstruction already rules out
using it as a near seed; the lemmas below identify the additional exact
head and port cuts which any superficially similar canonical recursion
would inherit.

Represent sets by binary words, with `1` meaning membership.  Pair every
`1` with the latest unpaired `0` to its left.  The standard
Greene--Kleitman matching `M_0` changes the first free `0` of a
rank-`(m-1)` word to `1`.

For a long-chain word `L` whose first two free zeros are `a<b`, the
unchanged chain-mate upper choice uses the off-matching incidence
`L--(L+b)` and carries colour `L+a+b`.  These colours enumerate all
rank-`(m+1)` sets exactly once.

### Theorem 6.1 (an `(m-1)`-fold head funnel)

For every `m>=3`, this upper-exact choice is not a matching.

#### Proof

Put

\[
\begin{aligned}
 V_*&=1(01)^{m-1},\\
 L_j&=1(01)^{j-1}00(01)^{m-1-j},\\
 R_j&=1(01)^{j-1}11(01)^{m-1-j}
              \qquad(1\le j<m).
\end{aligned}                                       \tag{6.1}
\]

In `L_j`, the initial `1` is free and the displayed `00` are its first two
free zeros.  The colours `R_j` are distinct, but the off-matching middle
endpoint `L_j+b` is `V_*` for every `j`.  Moreover

\[
                         M_0^{-1}(V_*)=0(01)^{m-1}.
\]

Thus all `m-1` contracted arcs have one head. \(\square\)

The collision occurs before graphic or connector Hall constraints and is
inherited by relabelled/reflected copies of the same standard choice.

### Corollary 6.2 (GK-monotone support needs many resets)

Let `sigma(S)=sum_(i in S)i`.  Every unchanged long-chain arc above is
strictly `sigma`-increasing.  Any Hamilton completion which retains such a
`sigma`-increasing `Q_0` needs at least

\[
 \left\lceil\frac{W}{m(m-1)+1}\right\rceil-1        \tag{6.2}
\]

strictly `sigma`-decreasing connector resets.  In particular, a reservoir
containing only `sigma`-increasing connectors cannot complete it.

#### Proof

Write the free positions of `L` as free ones
`u_1<...<u_p` followed by the first free zeros `a<b`, where `p>=1`.  In
`V=L+b`, the positions `a,b` pair, and the GK inverse flips the last
remaining free one `u_p`.  The contracted head is

\[
                         H=L-u_p+b,
\]

so `sigma(H)-sigma(L)=b-u_p>0`.  On rank-`(m-1)` subsets of `[2m-1]`,
`sigma` takes `H=m(m-1)+1` values.  Also

\[
 W={2m-1\choose m-1}
 \ge {2m-1\choose2}>m(m-1)+1
\]

for `m>=3`.  Apply Theorem 5.2. \(\square\)

### Theorem 6.3 (the common ballot puncture fails Hall)

Let `mathcal B_m` be the `Cat_m` rank-`(m-1)` ballot words with no free
`1` and one free `0`.  If `mathcal B_m` is used as both the free-tail and
free-head bank, then the connector graph has Hall deficiency at least two.

#### Proof

Let `H in mathcal B_m`, and let `a` be its unique free zero.  A connector
from another ballot word `L` into `H` has

\[
                         L=H+a-b
\]

for some `b in H`.  Ballotness of `L` forces `b<a`: if `b>a`, changing the
unmatched zero at `a` to one makes the prefix balance negative before the
compensating change at `b`.  Therefore every such connector strictly
decreases `sigma`.

On `mathcal B_m`, the potential ranges from `m(m-1)` to
`3m(m-1)/2`, so it has at most `binom(m,2)+1` values.  Since

\[
                         \operatorname {Cat}_m>{m\choose2}+1
                         \qquad(m\ge3),               \tag{6.3}
\]

some layer has multiplicity at least two.  For such a `t`, let

\[
                         X_t=\{L\in\mathcal B_m:\sigma(L)\le t\}.
\]

Every neighbour lies in the strict sublevel `sigma<t`, and therefore

\[
 |X_t|-|N(X_t)|
 \ge\#\{L\in\mathcal B_m:\sigma(L)=t\}\ge2.        \tag{6.4}
\]

This is an explicit Boolean Hall cut. \(\square\)

Thus repairing only the head collision while retaining a common canonical
puncture bank still cannot work.

## 7. Two dimension-minimal upper-exact forest obstructions

Use the `m=3` vertices and arc table (3.1)--(3.3) of the owner-layer path
theorem.

### Proposition 7.1 (an actual Hall-deficient `Q_0`)

The set

\[
 Q_0=\{A\to D,\ H\to G,\ D\to J,\ B\to I,\ F\to C\} \tag{7.1}
\]

uses the five upper colours `1234,1235,1245,1345,2345` exactly once and is
a directed forest with components

\[
 A\to D\to J,\quad B\to I,\quad F\to C,\quad E,
 \quad H\to G.                                      \tag{7.2}
\]

The terminal `E` has no external free-port successor because its two arcs
enter the non-initial roots `D,C`.  The terminal `G` likewise enters only
the non-initial roots `I,J`.  Hence the two corresponding components form
a set `X` with `N(X)=\varnothing`, and `delta(Q_0)>=2`.

### Proposition 7.2 (Hall succeeds only through a cycle)

The upper-exact forest

\[
 Q_0=\{A\to D,\ G\to I,\ D\to J,\ I\to F,\ F\to C\} \tag{7.3}
\]

has components

\[
 K_0=A\to D\to J,\quad K_1=B,\quad
 K_2=G\to I\to F\to C,\quad K_3=E,\quad K_4=H.
\]

Its external connector arcs are exactly

\[
 K_0\to K_3,\quad K_1\to K_0,\quad
 K_2\to K_0,\quad K_2\to K_4,\quad
 K_4\to K_2,\quad K_4\to K_3.                      \tag{7.4}
\]

The matching

\[
 K_1\to K_0,\quad K_0\to K_3,\quad
 K_2\to K_4,\quad K_4\to K_2
\]

has size four, so every one-defect Hall cut passes.  But no Hamilton path
exists: `K_1` is the unique possible source and its only continuation is

\[
                         K_1\to K_0\to K_3,
\]

which terminates before `K_2,K_4`.  The Hall witness necessarily spends
its remaining two edges on the cycle `K_2<->K_4`.  Thus no acyclic
one-defect-Hall subreservoir exists.

Both propositions are direct readings of the displayed arc table; no
enumeration is used.  They are dimension-minimal.  At `m=2`, `D_(M_0)` is
a directed three-cycle; an upper-exact `Q_0` is one arc and either adjacent
remaining arc connects its two components acyclically.

## 8. Exact prospective frontier

The proved positive rows are now:

1. a robust injective owner-label shell for every Catalan-size terminal
   bank, even after `m-1` forbidden labels; and
2. an optimal explicit `Cat_(m-1)` SCD socket bank for one coordinate pair.

For the tight-pivot/double-crossrail application, the protected component
`K_*` is distinguished: it must be the first component of the final owner
path.  Thus an ordered construction must take `K_*=K_1` in Theorem 5.1,
and the exact rooted Hall row asks for every consecutive connector starting
from that component.  In an arbitrary acyclic reservoir it is

\[
 |N^-_{\mathcal A}(Y)|\ge|Y|
 \qquad(Y\subseteq\mathcal C\setminus\{K_*\}),       \tag{8.1}
\]

after deleting the incoming copy of `K_*`.  Unrooted one-defect Hall is not
enough.

There is a further literal port condition.  If `L_0` is the first root of
the protected successor path, the selection of `R` must forbid every
unprotected arc entering `L_0`.  Then `L_0=s_(K_*)` is genuinely the free
incoming root of the distinguished component.  Merely putting an internally
embedded protected path inside the first component would start the physical
word before the protected collar.  Dually, a prescribed terminal collar
must reserve its last root as the free outgoing port.

The support-first target is a born-linear, upper-surjective directed forest
`R` containing the correlated protected successor path `P_1`.  Choosing
one representative per upper colour inside `R` produces `Q_0`; all other
edges of `R` are already acyclic connectors.  Section 4 supplies one
optimal born-linear socket sector which could be part of such an `R`, but
does not correlate its perfect matching with the protected predecessor
bank `P_0`.

The protected odd-diamond marginal theorems separately extend the same
tight-pivot bank to an upper/lower-injective selector and to an
upper-exact owner-cap-two selector under `6Hh<=m-2`.  Their natural joint
matrix has a determinant-`2` triangle minor, so those two flows do not
synchronize automatically.  The SCD funnel is stronger locally: its
`Cat_(m-1)` sockets satisfy both marginal systems and the graphic row in one
born-linear packet.  What is missing is a multi-funnel packet covering the
entire upper palette while retaining the protected phase.

The missing theorem is therefore not generic rainbow matching, diffuse
shadow expansion, or GK pruning.  It must jointly choose:

1. a bridge/tight-pivot phase and a perfect `M_0` containing its predecessor
   shore `P_0`;
2. a born-linear upper-surjective `R` containing the successor path `P_1`,
   thereby avoiding the explicit GK head funnel;
3. different, correlated free-tail and free-head banks;
4. at least three/four coordinate funnels, with an order beginning at
   `K_*` in which their sockets become the consecutive connectors required
   by Theorem 5.1; and
5. enough nonmonotone reset arcs to escape the height and ballot cuts.

Corollary 2.2 proves an adequate owner-label shell for any protected bank of
order at most `m-1`.  Separately, the authenticated bridge theorem extends
the exact bare and right-continued predecessor matchings under
`2d+3<=m-1` and `3d+3<=m-1`, respectively.  Theorem 4.1 proves the socket
matching for one SCD funnel.  It is exactly their **joint** matching and
upper-exact linear support which remains unproved.  None of these marginal
theorems implies that intersection.

Even after these rows, higher-depth upper witnesses, residence and the
compiler remain outside scope.
