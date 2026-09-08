# Cyclic packetization of exact balanced nested flags

Date: 2026-07-25  
Line: E — exact cyclic flag packetization

## 0. Verdict

Let an integral fiber-balanced common nested resolution through
`K=ceil(A sqrt(m))` be fixed.  This report does **not** prove that its labelled
owner flags can be packetized into wreath rows, nor that one can always choose
the integral flow resolution to make this possible.

It gives an exact formulation and four rigorous advances.

1. Exact packets are precisely support-compatible directed `n`-cycles which
   are rainbow in the first deletion label and packetwise point-regular.  The
   point equations force residence time exactly `m`.
2. Every SCC of the full owner compatibility digraph has a polynomially
   computable packet capacity, using every deletion column, all depthwise
   point supplies, a directed coordinate min-cut, and the SCC period.  If
   deleting `L` owners leaves exact packets, then

   \[
   L\ge W-n\sum_C\widehat T_C.
   \]

   This is a support-aware Hall obstruction strictly stronger than global
   point margins.
3. A higher-order co-incidence hierarchy gives polynomial LP lower bounds on
   residence defect.  Pair and `s`-set counts can detect an obstruction even
   when every componentwise singleton margin is exact.
4. In the forced-cycle regime the maximum exact packet subfactor is solved
   completely: one must delete every bad cycle, and the sharp cleanup loss is
   at most `n\Delta`.  The factor `n` is attained, so deletion-only cleanup
   cannot give the desired Gaussian-window scale.

There is also a limited positive Hall theorem at the coordinate-pair
projection: regularity decomposes the pair arcs into permutation covers, and
subtours can be spliced into Hamilton cycles with an explicit number of
failed pair slots.  Its universal loss is `\Theta(W)`, and it does not enforce
owner support, higher prefixes, or residence.

All results keep labelled ownership.  Whenever exact packets are retained,
one owner permutation is used at every depth and every orbit has length
`n=2m+1`.

## 1. Fixed balanced flags and the compatibility digraph

Put

\[
n=2m+1,\qquad \Omega=\binom{[n]}m,\qquad
W=|\Omega|,\qquad B=\frac Wn,
\]

and

\[
K=\lceil A\sqrt m\rceil,\qquad
N_q=\binom n{m-q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor.
\tag{1.1}
\]

Throughout, `A` is fixed and `m` is sufficiently large that `2<=K<=m-2`.

For every labelled owner `X\in\Omega`, the given integral flow resolution is

\[
P_0(X)=X\supset P_1(X)\supset\cdots\supset P_K(X),
\]

with

\[
d_t(X)=P_{t-1}(X)\setminus P_t(X),
\qquad 1\le t\le K.
\tag{1.2}
\]

Every rank-`(m-q)` target has `c_q` or `c_q+1` owners.  No rankwise
reassignment or owner relabelling will be allowed below.

Define the **full support-compatible successor digraph** `D_K(P)` on the
owner set `Omega` by

\[
X\longrightarrow Y
\tag{1.3}
\]

if and only if

\[
Y\setminus X=\{d_1(Y)\}
\tag{1.4}
\]

and

\[
d_{t+1}(Y)=d_t(X)\qquad(1\le t<K).
\tag{1.5}
\]

Condition (1.4) says that the first label of `Y` is exactly its entering
coordinate.  Condition (1.5) is the full visible deletion-word shift law.

### Definition 1.1 (exact packet)

An exact depth-`K` packet is a simple directed cycle

\[
X_0\to X_1\to\cdots\to X_{n-1}\to X_0
\tag{1.6}
\]

in `D_K(P)` such that:

1. `j\mapsto d_1(X_j)` is a bijection onto `[n]`; and
2. for every coordinate `a`,

   \[
   |\{j:a\in X_j\}|=m.
   \tag{1.7}
   \]

### Theorem 1.2 (lossless packet criterion)

A cycle (1.6) is one oriented wreath row carrying precisely the prescribed
flags through depth `K` if and only if it satisfies Definition 1.1.

#### Proof

Write

\[
g_j=d_1(X_j).
\]

By (1.4), `g_j` enters on the transition `X_{j-1}->X_j`.  Rainbow condition
1 says that every coordinate enters exactly once.  A coordinate which has
left cannot re-enter, because every entering coordinate is the unique label
`g_j`.  Its membership positions therefore form one cyclic interval beginning
at its entry.  Equation (1.7) makes that interval have length exactly `m`.
Consequently

\[
X_j=\{g_j,g_{j-1},\ldots,g_{j-m+1}\}.
\tag{1.8}
\]

Repeated use of (1.5) gives

\[
d_t(X_j)=g_{j-t+1}\qquad(1\le t\le K).
\tag{1.9}
\]

Thus the owners are the `m`-windows of the cyclic coordinate order and their
given flags are exactly canonical.  The converse follows immediately from a
wreath row.  QED.

The exact packet hypergraph `\mathcal H_K(P)` has vertex set `\Omega` and one
hyperedge for every packet in Definition 1.1.  Full packetization is exactly
a perfect matching in this `n`-uniform hypergraph.  This formulation is
lossless but is not an ordinary bipartite Hall problem.

If packets cover all owners, their cycles define one permutation `sigma` of
`Omega`; (1.9) shows that this same `sigma` synchronizes every depth.

## 2. Coordinate-pair projection and a bounded-loss Hall theorem

Assume `K>=2`.  Form the directed coordinate-pair multigraph `Gamma(P)` on
`[n]`, with one labelled owner arc

\[
d_2(X)\longrightarrow d_1(X)
\tag{2.1}
\]

for every `X\in\Omega`.

### Proposition 2.1 (Hamilton projection)

Every exact packet contributes one directed Hamilton cycle to `Gamma(P)`.
Hence a full packetization forces `Gamma(P)` to decompose into `B` directed
Hamilton cycles.

For every partition

\[
\Pi=\{S_1,\ldots,S_r\}
\]

of `[n]` into nonempty parts, let `M_cross(Pi)` count owner arcs whose
endpoints lie in different parts.  Then necessarily

\[
\boxed{M_{\rm cross}(\Pi)\ge Br.}
\tag{2.2}
\]

In particular, for every nonempty proper `S\subset[n]`,

\[
\boxed{
|\delta^+_{\Gamma}(S)|\ge B,
\qquad
|\delta^-_{\Gamma}(S)|\ge B.}
\tag{2.3}
\]

#### Proof

On a packet, (1.9) gives

\[
d_2(X_j)=g_{j-1},\qquad d_1(X_j)=g_j,
\]

so its owner arcs are the directed Hamilton cycle

\[
g_0\to g_1\to\cdots\to g_{n-1}\to g_0.
\]

After contracting the parts of `Pi`, a Hamilton cycle which visits every
part has at least `r` transitions between distinct parts.  Summing over `B`
packets proves (2.2).  Taking the two-part partition gives (2.3), with the
incoming inequality obtained by replacing `S` by its complement.  QED.

This is strictly stronger than coordinate degree balance.  For example,
take two disjoint directed coordinate cycles, give every internal arc
multiplicity `B`, and replace one copy of an arc in each cycle by two crossed
arcs.  Every coordinate still has indegree and outdegree `B`, and the graph
is strongly connected, but the cut between the two old cycles has only one
arc in each direction.  For `B>1`, (2.3) fails.  This is a projection
countermodel, not a claimed balanced flag resolution.

There is a robust form.  Suppose an owner permutation has rainbow `n`-cycles
but `E` transitions fail the depth-two identity in (1.5).  The ideal
Hamilton arc entering `d_1(X)` then differs from the owner arc (2.1) at no
more than `E` owners.  Therefore

\[
\boxed{
E\ge\max_{\Pi}
\bigl(Br-M_{\rm cross}(\Pi)\bigr)_+.}
\tag{2.4}
\]

### Theorem 2.2 (limited pair-Hall packetization)

If `Gamma(P)` is `B`-in/`B`-out regular, its labelled owner arcs decompose
into `B` directed permutation cycle covers.  If cover `i` has `c_i` subtours,
it can be changed into one directed Hamilton label cycle using exactly
`c_i` failed pair slots when `c_i>1`, and none when `c_i=1`.  Thus one obtains
`B` rainbow coordinate cycles with at most

\[
\sum_{i:c_i>1}c_i
\le B\left\lfloor\frac n2\right\rfloor
=O(W)
\tag{2.5}
\]

failed pair slots.

#### Proof

Represent every coordinate once on a left side and once on a right side.
The owner arcs form a `B`-regular bipartite multigraph.  Repeated Hall
matching, equivalently bipartite edge-coloring, decomposes it into `B`
perfect matchings.  Each matching is a directed permutation cover.

For a cover with subtours `C_1,...,C_c`, choose an arc `u_i->v_i` from each.
Delete those arcs and insert

\[
u_i\longrightarrow v_{i+1}
\]

cyclically in `i`.  The cut subtours become one Hamilton cycle.  The inserted
arcs are the `c` failed pair slots.  If `c=1`, no change is needed.  Since
`d_1(X)!=d_2(X)`, there are no one-vertex subtours, so `c<=floor(n/2)`.
Summing proves (2.5).  QED.

The theorem solves only the pair projection.  Its loss is linear in `W`, and
the inserted arcs need not satisfy owner adjacency (1.4), higher overlap
(1.5), or residence.  It identifies the subtour obstruction left after
ordinary Hall, but cannot prove Gaussian-window alignment.

## 3. Support-aware SCC Hall capacity

Let `mathfrak C` be the strongly connected components of the full owner
digraph `D_K(P)`.  Every exact packet is contained in one such SCC.

For `C\in\mathfrak C`, define every deletion-column supply

\[
h_{C,t}(a)=|\{X\in C:d_t(X)=a\}|,
\qquad 1\le t\le K,
\tag{3.1}
\]

and every depthwise point supply, with `P_0(X)=X`,

\[
s_{C,q}(a)=|\{X\in C:a\in P_q(X)\}|,
\qquad 0\le q\le K.
\tag{3.2}
\]

For `K>=2`, let `Gamma_C` be the coordinate multigraph formed by the owner
arcs (2.1) for `X in C`, and set

\[
\lambda_C=min_{\varnothing\ne S\subsetneq[n]}
|\delta^+_{\Gamma_C}(S)|.
\tag{3.3}
\]

This is a directed global min-cut and is polynomially computable.

If `C` contains a directed cycle, let

\[
\gamma_C=\gcd\{\text{length}(Z):Z\text{ a directed cycle in }C\}
\tag{3.4}
\]

be its period.  If it contains no directed cycle, call it acyclic.

For `K>=2`, put

\[
T_C=min\left\{
\min_{1\le t\le K,\ a\in[n]}h_{C,t}(a),
\quad
\min_{0\le q\le K,\ a\in[n]}
\left\lfloor\frac{s_{C,q}(a)}{m-q}\right\rfloor,
\quad
\lambda_C
\right\}.
\tag{3.5}
\]

For `K=1`, omit the `lambda_C` term.  Finally define

\[
\widehat T_C=
\begin{cases}
T_C,&C\text{ is cyclic and }\gamma_C\mid n,\\
0,&\text{otherwise}.
\end{cases}
\tag{3.6}
\]

### Theorem 3.1 (SCC packet-capacity loss bound)

If deleting `L` labelled owners leaves a disjoint union of exact depth-`K`
packets using arcs of `D_K(P)`, then

\[
\boxed{
L\ge W-n\sum_{C\in\mathfrak C}\widehat T_C.}
\tag{3.7}
\]

Every term on the right is computable in time polynomial in the explicit
owner digraph.

#### Proof

Let `t_C` be the number of retained packets inside SCC `C`.

Every packet uses each coordinate exactly once in every deletion column, by
(1.9).  Hence

\[
t_C\le h_{C,t}(a)
\qquad(t\le K, a\in[n]).
\tag{3.8}
\]

At depth `q`, an exact packet has `m-q` states containing each coordinate.
Therefore

\[
(m-q)t_C\le s_{C,q}(a)
\qquad(q\le K, a\in[n]).
\tag{3.9}
\]

Its pair arcs form a directed Hamilton coordinate cycle, which crosses every
nontrivial directed coordinate cut.  Thus, for `K>=2`,

\[
t_C\le\lambda_C.
\tag{3.10}
\]

Finally, the owner packet is a directed cycle of length `n` inside `C`.
Every directed cycle length in a cyclic SCC is divisible by its period, so
`gamma_C` must divide `n`.  An acyclic SCC supports no packet.  Equations
(3.8)-(3.10) prove

\[
t_C\le\widehat T_C.
\]

Since the retained owner count is `W-L=n sum_C t_C`, (3.7) follows.  QED.

The period is also polynomially computable: fix rooted directed distances in
an SCC and take the gcd of the arc discrepancies

\[
\operatorname{dist}(u)+1-\operatorname{dist}(v).
\]

A period-two support component is therefore wholly unusable because `n` is
odd, even if every singleton supply and pair degree is perfect.

The partition cuts from Proposition 2.1 strengthen (3.10): for every
coordinate partition `Pi` into `r` parts,

\[
t_C\le
\left\lfloor\frac{M_C^{\rm cross}(\Pi)}r\right\rfloor.
\tag{3.11}
\]

The two-part min-cut is the polynomial member of this larger Hall family.

### Corollary 3.2 (componentwise equalities for a full packetization)

If all owners of `C` are packetized and

\[
b_C=\frac{|C|}{n},
\]

then necessarily

\[
h_{C,t}(a)=b_C
\qquad(t\le K, a\in[n]),
\tag{3.12}
\]

and, even before imposing residence `m`,

\[
s_{C,q}(a)=s_{C,0}(a)-qb_C.
\tag{3.13}
\]

Under exact residence these become

\[
\boxed{s_{C,q}(a)=b_C(m-q).}
\tag{3.14}
\]

Indeed, each packet deletes each coordinate exactly once in every word
column; after `q` columns it has removed `q` occurrences of that coordinate.

Global fiber balance and global coordinate margins do not imply any of
(3.12)-(3.14), because supplies cannot move between incompatible SCCs.  This
is the principal explicit obstruction stronger than point marginals.

## 4. Higher-order co-incidence obstruction

The SCC point supplies can all be exact while residence still fails.  The
next hierarchy detects concentrated multi-coordinate incidence.

Assume an SCC `C` is fully decomposed into

\[
b_C=|C|/n
\]

locally compatible rainbow `n`-cycles, possibly with nonconstant residence
lengths.  Let their total residence defect be

\[
\Delta_C=\frac12
\sum_{R\subset C}\sum_{x\in[n]}|r_R(x)-m|.
\tag{4.1}
\]

For a coordinate set `A` of size `s` and `q<=K`, define

\[
I_{C,q}(A)=|\{X\in C:A\subseteq P_q(X)\}|,
\tag{4.2}
\]

and, when `2<=s<=m-q`,

\[
E_{C,q}(A)=
\left[
I_{C,q}(A)-b_C(m-q-s+1)
\right]_+.
\tag{4.3}
\]

For each coordinate, put

\[
p_C(x)=\sum_{R\subset C}(r_R(x)-m)_+.
\tag{4.4}
\]

Since every packet has total residence `nm`,

\[
\sum_xp_C(x)=\Delta_C.
\tag{4.5}
\]

### Theorem 4.1 (co-incidence tensor bound)

For every admissible `q,A`,

\[
\boxed{
E_{C,q}(A)\le\sum_{x\in A}p_C(x).}
\tag{4.6}
\]

Consequently, for any nonnegative weights `w_{q,A}` satisfying

\[
\sum_{q,A\ni x}w_{q,A}\le1
\qquad(x\in[n]),
\tag{4.7}
\]

one has

\[
\boxed{
\Delta_C\ge
\sum_{q,A}w_{q,A}E_{C,q}(A).}
\tag{4.8}
\]

#### Proof

In one rainbow residence cycle, coordinate `x` occurs among the depth-`q`
states on the cyclic interval

\[
[\operatorname{arr}(x)+q,
  \operatorname{arr}(x)+r_R(x)-1],
\tag{4.9}
\]

of length `r_R(x)-q`.  Its canonical comparator has the same first position
and length `m-q`.

Take `s` distinct coordinates.  If their canonical intervals have nonempty
intersection, cut the circle at a common point.  Their `s` distinct starting
positions span at least `s-1` steps, so the intersection has length at most

\[
m-q-s+1.
\tag{4.10}
\]

If the intersection is empty the same upper bound is immediate.  Shortening
an interval cannot enlarge the intersection; extending coordinate `x`'s
interval can add at most `(r_R(x)-m)_+` points.  Thus one packet contributes
at most

\[
m-q-s+1+
\sum_{x\in A}(r_R(x)-m)_+
\]

states containing `A`.  Sum over the `b_C` packets to obtain (4.6).

Multiply (4.6) by `w_{q,A}`, sum, use (4.7), and then use (4.5).  This proves
(4.8).  QED.

For any fixed tensor order `s_0`, the best bound (4.8) is a polynomial LP of
size `O_A(K n^{s_0})`.  Equivalently, define

\[
\Lambda_C=min\sum_x z_x
\tag{4.11}
\]

over `z_x>=0` with

\[
z_x\ge[s_{C,0}(x)-b_Cm]_+
\]

and

\[
\sum_{x\in A}z_x\ge E_{C,q}(A)
\]

for all `q<=K` and `2<=|A|<=s_0`.  The actual `p_C` is feasible, so

\[
\boxed{\Delta_C\ge\Lambda_C.}
\tag{4.12}
\]

For pairs alone,

\[
\Delta_C\ge
\max\left\{
\sum_{x<y}w_{xy}E_{C,q}(\{x,y\}):
w_{xy}\ge0,
\ \sum_{y\ne x}w_{xy}\le1
\right\}.
\tag{4.13}
\]

In particular,

\[
\Delta_C\ge\max_{x<y}E_{C,q}(\{x,y\}),
\qquad
\Delta_C\ge
\frac1{n-1}\sum_{x<y}E_{C,q}(\{x,y\}).
\tag{4.14}
\]

These bounds can be positive when every singleton equation (3.14) is exact;
they constrain the distribution of pair and higher intersections, not merely
their one-coordinate marginals.

Here is an exact algebraic separation.  Fix coordinates `x,y`.  Give
multiplicity `m` to every `m`-set containing both `x,y`, multiplicity `m-1`
to every `m`-set containing neither, and multiplicity zero to sets containing
exactly one.  The degree of `x` and `y` is

\[
D=m\binom{n-2}{m-2}.
\]

For any other coordinate `z`, its degree is

\[
m\binom{n-3}{m-3}
+(m-1)\binom{n-3}{m-1}=D,
\tag{4.15}
\]

by direct binomial simplification with `n=2m+1`.  Thus this integral
multicover is point-regular.  Writing

\[
b=D/m=\binom{n-2}{m-2},
\]

the total multiplicity is `nb` by double-counting point-set incidences.  Its
`x,y` co-incidence is `D=mb`, exceeding the canonical pair ceiling
`b(m-1)` by `b`.  This proves that the pair constraint is not a consequence
of point regularity.  The example is a multicover, not a simple-owner flag
resolution or a packetization counterexample.

For exact packetization `Delta_C=0`, every excess in (4.3) must vanish.

## 5. A sharp bounded-loss decomposition theorem in the forced regime

The general packet hypergraph need not have a matching even when every
displayed SCC capacity is positive.  There is, however, one regime in which
the maximum packet subfactor is exactly solvable.

### Theorem 5.1 (forced-cycle cleanup)

Assume the full compatibility digraph `D_K(P)` is exactly a disjoint union of
simple directed `n`-cycles.  Assume each is rainbow and obeys the arrival and
prefix laws.  Call a component **good** when every coordinate residence is
`m`, and **bad** otherwise.  If `\mathcal B_{\rm bad}` is the set of bad components,
then the largest exact packet subfactor deletes exactly

\[
\boxed{L=n|\mathcal B_{\rm bad}|}
\tag{5.1}
\]

owners.  Moreover,

\[
\boxed{L\le n\Delta,}
\tag{5.2}
\]

where `Delta` is the total residence defect of the forced cycle cover.  The
factor `n` is best possible.

#### Proof

A proper subset of a simple directed cycle contains no directed cycle.  With
no compatibility arcs between components, a retained exact packet must be
one entire forced component.  Theorem 1.2 says precisely that the good
components are exact packets.  Hence every bad component, and only those,
must be deleted, proving (5.1).

Every nonconstant integral residence vector has positive and negative
deviations of equal total, so its half-`ell^1` defect is an integer at least
one.  Therefore

\[
|\mathcal B_{\rm bad}|\le\Delta,
\]

which gives (5.2).  QED.

The protected radius-one two-cycle construction has two forced bad
components, residence defect one in each, and no cross-component
compatibility arcs.  Concretely, use coordinate orders

\[
h^A=(0,1,\ldots,2m),
\]

\[
h^B=(1,0,2,4,\ldots,2m,3,5,\ldots,2m-1),
\]

replace in each row the one canonical owner
`W_m^h=\{h_1,\ldots,h_m\}` by

\[
X_m^h=W_m^h-\{h_1\}+\{h_0\},
\]

and use `d_t(X_j^h)=h_{j-t+1}` for `t<=m-1`.  Each row then has residence
vector `(m+1,m-1,m,...)`.  For `m>=10`, the ordinary numeric-cycle edge
count is at least `m-2` on every `A`-owner and at most `5` on every `B`-owner;
one Johnson exchange changes this count by at most two.  Thus no cross-row
owners are equal or Johnson-adjacent, and the within-row arrival labels force
the intended predecessor.  The induced compatibility graph is exactly the
two forced cycles.  It therefore satisfies

\[
L=2n=n\Delta.
\tag{5.3}
\]

That construction is an induced `2n`-owner obstruction, not a completed
fiber-balanced resolution on all `Omega`.  It proves sharpness of the cleanup
constant, not a global counterexample.

On the fixed Gaussian window,

\[
\sum_{q\le K}\frac1{c_q}=O_A(\sqrt m).
\]

Even if a prior argument gives `Delta=o(W/sqrt(m))`, (5.2) only gives a
potential owner loss of order `n Delta`; this need not be `o(W/sqrt(m))` or
even `o(W)`.  Since equality is possible, whole-cycle deletion cannot close
the route.  A successful theorem must rewire across bad cycles while keeping
all flags and owners exact.

## 6. Consequences for the given balanced flow

The integral flow resolution is packetizable only if all of the following
hold simultaneously.

1. Every used SCC is cyclic with period dividing the odd number `n`.
2. Its deletion-column supplies satisfy (3.8).
3. Its depthwise point supplies satisfy (3.9), and a fully used component
   satisfies the equalities (3.12)-(3.14).
4. Its pair graph satisfies every Hamilton cut (3.10)-(3.11).
5. Its pair and higher co-incidences satisfy Theorem 4.1 with zero excess.
6. After these projections, the actual admissible `n`-cycles must still have
   a perfect matching in the packet hypergraph.

These conditions are componentwise.  Global fiber balance cannot average a
deficit in one SCC against a surplus in another, because a packet cannot
cross SCCs.

The smallest remaining positive statement is therefore the following.

### Unproved cross-cycle absorber lemma `CP_A`

For every fixed `A`, one can choose the integral balanced nested flow through
`K=ceil(A sqrt(m))` so that its compatibility digraph admits a perfect
matching by exact packet cycles, or at least a packet subfactor with
`o(W/sqrt(m))` exceptional owners which can be absorbed without changing any
prescribed flag or target fiber.

The SCC theorem shows that `CP_A` must arrange componentwise supplies,
periods, coordinate cuts, and co-incidences before any absorber can act.  No
such theorem is proved here.

## 7. Independent adversarial audit

The main steps were independently audited with the following qualifications.

1. **Use the full owner digraph.**  The SCC capacity theorem applies to SCCs
   of `D_K(P)`, including the owner support condition (1.4), not merely to
   weak components of the ordered deletion-type graph.
2. **Pair orientation.**  The coordinate owner arc is `d_2->d_1`.  The
   min-cut term requires `K>=2`; it is omitted at `K=1`.
3. **Period.**  A singleton SCC without a directed loop is acyclic and has
   capacity zero.  For cyclic SCCs, the period divides every directed cycle
   length, so `gamma_C|n` is necessary.  It is not sufficient.
4. **Supply bounds are upper bounds.**  For a partial packet subfactor,
   (3.8)-(3.10) only bound the number of packets.  The exact equalities
   (3.12)-(3.14) require that every owner of that component be used.
5. **Tensor scope.**  The co-incidence theorem assumes rainbow arrivals and
   the resulting one-interval residence law.  Its depth range is
   `2<=|A|<=m-q`.
6. **Pair-Hall scope.**  Theorem 2.2 constructs Hamilton cycles only in the
   projected coordinate arc table.  Its spliced arcs may not be owner arcs
   of `D_K(P)`.
7. **Forced cleanup scope.**  Theorem 5.1 requires that the full compatibility
   digraph have no additional arcs.  It concerns deletion to a packet
   subfactor, not arbitrary rewiring or a balanced completion of the deleted
   owners.
8. **Sharp example scope.**  The equality example (5.3) is an induced block,
   not an embedded globally balanced simple-owner resolution.
9. **Necessity, not sufficiency.**  Positive SCC capacities, correct period,
   all Hamilton cuts, and zero tensor excess still do not prove a compatible
   Hamilton decomposition or a perfect packet matching.

The audited conclusion is exact: ordinary point margins are far from enough.
Packetization is controlled first by support-compatible SCCs, then by
Hamilton coordinate cuts and higher co-incidences, and finally by a genuinely
global cycle matching.  The missing operation is a cross-cycle absorber, not
another rankwise integral flow.
