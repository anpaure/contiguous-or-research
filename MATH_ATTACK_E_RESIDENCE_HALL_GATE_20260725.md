# Exact residence-time and Hall gates for cyclic flag packetization

Date: 2026-07-25  
Line: E — next cyclic packetization wave

## 0. Verdict

This route does **not** prove the contiguous-OR width conjecture, overload
MWB, or the stronger labelled theorem `CA_A`.

It does isolate the exact residence obstruction more sharply and gives four
unconditional advances.

1. There is a polynomial family of support-aware, layered queue min-cuts on
   the fixed window `K=ceil(A sqrt(m))`.  Any exact common owner schedule must
   route `B=W/n` vertex-disjoint copies of every visible coordinate queue.
2. The full shadow-clean scheduling problem has an exact fractional Hall
   dual, and its residence-cost version has an exact potential dual.  These
   are exact for the fractional program; integrality remains unproved.
3. A new conservation law corrects the naive absorber picture.  A bad cycle
   can never be repaired together with one good cycle.  Every family of
   cycles repartitionable into exact packets must have coordinatewise
   zero total residence defect.  Consequently, two-cycle absorbers exist
   only between opposite defect vectors.
4. For each opposite-defect pair, the optimal whole-cycle two-absorber repair
   is an ordinary bipartite matching.  Its exact loss is the sum of a defect-
   type imbalance and twice a Hall deficiency, and the deficiency is exposed
   by a literal minimum cut.  An explicit `2n`-owner construction has opposite
   defects and exact aggregate depthwise point laws, but its Hall graph has no
   edge.  Thus even the incidence gate can pass while the support gate fails.

All owner labels and all prescribed nested flags are retained in every
absorber edge.  No separate depthwise reassignment, fractional factor, or
unlabelled histogram replacement is used.  The explicit obstruction is an
induced block, not a completed balanced resolution on all middle owners.

## 1. Setup and the residence vector

Put

\[
n=2m+1,\qquad
\Omega=\binom{[n]}m,\qquad
W=|\Omega|,\qquad
B=\frac Wn.
\tag{1.1}
\]

Fix `A>0` and, for all sufficiently large `m`, put

\[
K=\lceil A\sqrt m\rceil\le m-1.
\tag{1.2}
\]

Let

\[
P_0(X)=X\supset P_1(X)\supset\cdots\supset P_K(X)
\qquad(X\in\Omega)
\tag{1.3}
\]

be one integral nested owner resolution, and write

\[
d_t(X)=P_{t-1}(X)\setminus P_t(X),
\qquad 1\le t\le K.
\tag{1.4}
\]

The full support-compatible digraph `D_K(P)` has vertex set `Omega` and an
arc

\[
X\longrightarrow Y
\tag{1.5}
\]

if and only if

\[
Y\setminus X=\{d_1(Y)\}
\tag{1.6}
\]

and

\[
d_{t+1}(Y)=d_t(X)
\qquad(1\le t<K).
\tag{1.7}
\]

A **local rainbow cycle** is a directed cycle

\[
C=(X_0,X_1,\ldots,X_{n-1})
\tag{1.8}
\]

in `D_K(P)` for which

\[
g_j:=d_1(X_j),\qquad j\in\mathbb Z_n,
\tag{1.9}
\]

is a bijection onto `[n]`.  Define its residence vector and defect vector by

\[
r_C(a)=|\{j:a\in X_j\}|,
\qquad
\boldsymbol\delta_C(a)=r_C(a)-m.
\tag{1.10}
\]

Also put

\[
\Delta(C)=\frac12\|\boldsymbol\delta_C\|_1.
\tag{1.11}
\]

Every coordinate enters the cycle exactly once, at its unique transition
labelled by that coordinate.  It cannot re-enter after leaving, because a
second entry would repeat a first label.  Hence its membership positions form
one nonempty cyclic interval, whose length is `r_C(a)`.  Since the cycle has
`n` owners of size `m`,

\[
\sum_{a=1}^n r_C(a)=nm,
\qquad
\sum_{a=1}^n\boldsymbol\delta_C(a)=0.
\tag{1.12}
\]

Repeated use of (1.7) gives

\[
d_t(X_j)=g_{j-t+1}
\qquad(1\le t\le K).
\tag{1.13}
\]

Define the canonical middle shadow of slot `j` by

\[
W_j(C)=\{g_j,g_{j-1},\ldots,g_{j-m+1}\}.
\tag{1.14}
\]

### Lemma 1.1 (exact residence criterion and coarea identity)

A local rainbow cycle is an exact labelled wreath packet carrying the
prescribed flags through depth `K` if and only if

\[
\boldsymbol\delta_C=0.
\tag{1.15}
\]

For every local rainbow cycle,

\[
\boxed{
\sum_{j\in\mathbb Z_n}|X_j\mathbin\triangle W_j(C)|
=\sum_{a=1}^n|r_C(a)-m|
=2\Delta(C).}
\tag{1.16}
\]

In particular,

\[
|\{j:X_j\ne W_j(C)\}|\le\Delta(C).
\tag{1.17}
\]

#### Proof

The actual membership interval of coordinate `g_i` begins at slot `i` and
has length `r_C(g_i)`.  Its canonical interval in (1.14) begins at the same
slot and has length `m`.  Their symmetric difference therefore has size
`|r_C(g_i)-m|`.  Summing first over coordinates and then over slots proves
(1.16).  Two unequal `m`-sets have symmetric difference at least two, so
(1.17) follows.

If the defect is zero, every membership interval has length `m`, so
`X_j=W_j(C)` for every `j`.  Equations (1.13)-(1.14) then identify the given
deletion prefix with the canonical prefix of this wreath row.  Conversely,
every wreath row contains each coordinate in exactly `m` middle windows, so
its defect is zero.  QED.

If local rainbow cycles partition all `W` owners, then their defects cancel
coordinatewise:

\[
\sum_C\boldsymbol\delta_C(a)
=\binom{n-1}{m-1}-Bm
=\frac{mW}{n}-\frac{mW}{n}
=0
\qquad(a\in[n]).
\tag{1.18}
\]

Equation (1.18) is automatic global point balance.  It says nothing about
how the nonzero defect vectors are grouped among cycles.

## 2. Polynomial visible-queue min-cuts

For `x in [n]` and `1<=q<=K`, let

\[
V_q(x)=\{X\in\Omega:d_q(X)=x\}.
\tag{2.1}
\]

Exact flag packetization requires the deletion-column margins

\[
|V_q(x)|=B
\qquad(x\in[n],\ 1\le q\le K),
\tag{2.2}
\]

because every packet uses each coordinate once in every deletion position.
The theorem below assumes (2.2).  Failure of (2.2) is already an exact
obstruction.

Fix `x` and `1<=t<K`.  Form the layered graph

\[
Q_{x,t}:
V_1(x)\longrightarrow V_2(x)\longrightarrow\cdots
\longrightarrow V_{t+1}(x)
\tag{2.3}
\]

by retaining precisely the arcs of `D_K(P)` between consecutive displayed
layers.  Give every owner vertex capacity one.  The layers are disjoint,
because the deletion letters of one owner are distinct.  Let `lambda_{x,t}`
be the maximum number of vertex-disjoint paths from the first layer to the
last.

### Theorem 2.1 (queue min-cut)

If the flags admit an exact partition into local rainbow cycles, then

\[
\boxed{\lambda_{x,t}=B}
\qquad(x\in[n],\ 1\le t<K).
\tag{2.4}
\]

Equivalently, every layered vertex cut separating `V_1(x)` from
`V_{t+1}(x)` has capacity at least `B`.

#### Proof

In each packet, let `X_0` be the unique owner with `d_1(X_0)=x`, and follow
the common owner successor for `t` steps.  Equation (1.7) gives

\[
d_1(X_0)=d_2(X_1)=\cdots=d_{t+1}(X_t)=x.
\tag{2.5}
\]

Thus every packet supplies one first-to-last path in `Q_{x,t}`.  The `B`
packets are owner-disjoint, so these paths are vertex-disjoint.  Hence
`lambda_{x,t}>=B`; the first layer has only `B` vertices, giving equality.
Integral vertex-capacitated max-flow/min-cut proves the cut statement.  QED.

For `t=1`, this is ordinary Hall and the exact deficit is

\[
B-\lambda_{x,1}
=\max_{U\subseteq V_1(x)}
\bigl(|U|-|N^+(U)\cap V_2(x)|\bigr).
\tag{2.6}
\]

There is a quantitative bypass form.

### Corollary 2.2 (cost of bypassing queue cuts)

Suppose a permutation of the owners has `B` rainbow `n`-cycles, but uses
`e_tr` successor transitions outside `D_K(P)`.  Put

\[
\varepsilon_{x,t}=(B-\lambda_{x,t})_+.
\tag{2.7}
\]

Then

\[
\boxed{
e_{\rm tr}\ge
\frac1t\sum_{x=1}^n\varepsilon_{x,t}}
\qquad(1\le t<K).
\tag{2.8}
\]

#### Proof

For fixed `x`, the `B` length-`t` queues supplied by the proposed cycles are
owner-disjoint.  At most `lambda_{x,t}` of them can use compatible transitions
throughout, so at least `\varepsilon_{x,t}` contain a bad transition.  In one
rainbow cycle, a fixed transition lies in at most `t` of the length-`t`
queues, because their starting slots are distinct.  The same is true after
summing over all cycles.  Hence

\[
\sum_x\varepsilon_{x,t}\le t e_{\rm tr},
\]

which is (2.8).  QED.

The queue cuts use the full owner-support arcs.  They are stronger than
separate layer sizes, but remain coordinatewise projections: passing them
for every `x,t` does not select one common owner permutation, and
`t<K=O(sqrt(m))` does not enforce departure at time `m`.

## 3. The full fractional shadow-resource Hall gate

Let \(\mathscr Q_K(P)\) be the family of all local rainbow cycles in
`D_K(P)`.
Use two disjoint copies of the middle owner universe,

\[
\mathcal R=\Omega_{\rm act}\sqcup\Omega_{\rm sh}.
\tag{3.1}
\]

A candidate \(C\in\mathscr Q_K(P)\) consumes its `n` actual labelled owners
in the first copy and its `n` canonical shadows (1.14) in the second.  The
shadows are distinct cyclic `m`-windows of a coordinate permutation.  Thus
the resource set `R(C)` has size exactly `2n`.

An integral perfect matching of `B` such resource sets is exactly a
shadow-clean local cycle schedule: every actual owner is used once and every
canonical middle shadow is used once.  The shadows then form an exact middle
wreath factor.

Consider the fractional packing program

\[
\nu^*=\max\sum_{C\in\mathscr Q_K(P)}z_C
\tag{3.2}
\]

subject to

\[
z_C\ge0,
\qquad
\sum_{C:r\in R(C)}z_C\le1
\quad(r\in\mathcal R).
\tag{3.3}
\]

Its dual is

\[
\tau^*=\min\sum_{r\in\mathcal R}y_r
\tag{3.4}
\]

subject to

\[
y_r\ge0,
\qquad
\sum_{r\in R(C)}y_r\ge1
\quad(C\in\mathscr Q_K(P)).
\tag{3.5}
\]

### Theorem 3.1 (fractional packet-Hall dual)

There is a fractional cover which saturates every actual and shadow resource
if and only if

\[
\boxed{\tau^*=B.}
\tag{3.6}
\]

Consequently, any nonnegative resource weighting satisfying

\[
\sum_{r\in R(C)}y_r\ge1
\quad\hbox{for every candidate }C,
\qquad
\sum_{r\in\mathcal R}y_r<B,
\tag{3.7}
\]

is an exact fractional deficient-cut certificate.

#### Proof

The constant weighting

\[
y_r=\frac1{2n}
\tag{3.8}
\]

is dual feasible and has value `2W/(2n)=B`, so `tau^*<=B`.  Strong LP
duality gives `nu^*=tau^*`.

If every resource is fractionally saturated, summing its `2W` load equations
shows that the total packet weight is `B`.  Conversely, if a feasible packing
has total weight `B`, then its total resource load is

\[
2nB=2W.
\]

There are `2W` resource loads, each at most one, so every load equals one.
This proves (3.6), and (3.7) follows by weak duality.  QED.

For example, if every candidate uses at least `h` resources from
\(U\subseteq\mathcal R\), then \(y=\mathbf 1_U/h\) is dual feasible.
Therefore

\[
|U|<Bh
\tag{3.9}
\]

rules out even fractional packetization.  If every candidate uses at most
`h` resources from `U`, applying the same argument to the complement shows
that

\[
|U|>Bh
\tag{3.10}
\]

is also an obstruction.

Every integral packing contains at most `tau^*` packets.  It therefore leaves
at least

\[
\boxed{2n(B-\tau^*)}
\tag{3.11}
\]

actual-plus-shadow resources uncovered.

### Theorem 3.2 (exact fractional residence-cost dual)

Assume that fractional perfect resource covers exist.  Give candidate `C`
the cost `Delta(C)` from (1.11), and minimize

\[
\sum_C\Delta(C)z_C
\tag{3.12}
\]

subject to the exact resource equations

\[
\sum_{C:r\in R(C)}z_C=1
\quad(r\in\mathcal R),
\qquad z_C\ge0.
\tag{3.13}
\]

The optimum equals

\[
\boxed{
\max\sum_{r\in\mathcal R}\alpha_r}
\tag{3.14}
\]

over free real potentials `alpha_r` satisfying

\[
\boxed{
\sum_{r\in R(C)}\alpha_r\le\Delta(C)
\quad(C\in\mathscr Q_K(P)).}
\tag{3.15}
\]

#### Proof

This is the ordinary LP dual of (3.12)-(3.13): equality constraints give free
dual variables, and each nonnegative primal variable gives one inequality
(3.15).  Feasibility and finiteness permit strong duality.  QED.

If an **integral** perfect resource matching has total cost `Delta`, Lemma
1.1 shows that at most `Delta` actual slots differ from their shadows.  At
every other slot, (1.13) makes every prescribed depth-`q` flag equal to the
canonical flag of the shadow row.  Because both actual owners and shadows
are used exactly once, only those bad slots can contribute to labelled
mismatch.  Hence

\[
e_q\le\Delta
\qquad(q\le K).
\tag{3.16}
\]

Writing

\[
S_K=\sum_{q=1}^K\frac1{c_q},
\tag{3.17}
\]

we obtain

\[
\boxed{
\sum_{q=1}^K\frac{e_q}{c_q}
\le\Delta S_K.}
\tag{3.18}
\]

On the fixed window, `S_K<=K=O_A(sqrt(m))`.  Thus an integral perfect
resource matching of cost

\[
\Delta=o(W/S_K)
\tag{3.19}
\]

would prove the labelled fixed-window bound.  A fractional cover of that
cost does not suffice without a new integrality or absorber theorem.

## 4. The residence conservation law for absorbers

Suppose a family \(\mathcal S\) of `k` local rainbow cycles is replaced, on
the same `kn` labelled owners, by `k` exact packets carrying the prescribed
flags.  Coordinate incidence in the union of owners is invariant under this
repartition.

### Theorem 4.1 (zero-sum absorber law)

Every such absorber family satisfies

\[
\boxed{
\sum_{C\in\mathcal S}\boldsymbol\delta_C=0}
\tag{4.1}
\]

coordinatewise.

#### Proof

For coordinate `a`, the original cycles contain it in

\[
km+\sum_{C\in\mathcal S}\boldsymbol\delta_C(a)
\]

owner slots.  Each of the `k` exact output packets contains `a` in exactly
`m` owner slots, for a total of `km`.  The owner supports have not changed,
so the two quantities are equal.  This proves (4.1) for every `a`.  QED.

Two immediate consequences are fundamental.

1. A good cycle has defect zero.  Therefore a genuinely bad cycle cannot be
   repaired with one good cycle into two exact packets.
2. A two-cycle absorber can join only cycles with defects

   \[
   \boldsymbol\alpha\quad\hbox{and}\quad-\boldsymbol\alpha.
   \tag{4.2}
   \]

The zero-sum condition is necessary, not sufficient: it sees owner-point
incidence but not support-compatible successor arcs or labelled deletion
words.

## 5. Exact opposite-defect Hall theorem

Assume that the owners have first been partitioned into local rainbow
`n`-cycles.  Cycles of defect zero are already exact packets by Lemma 1.1 and
will be retained.

For every unordered nonzero defect pair

\[
\{\boldsymbol\alpha,-\boldsymbol\alpha\},
\tag{5.1}
\]

let the smaller defect class be `L_alpha` and the larger one `R_alpha`
(ties are oriented arbitrarily), with

\[
\ell_\alpha=|L_\alpha|\le r_\alpha=|R_\alpha|.
\tag{5.2}
\]

Define the **flag-preserving pair-absorber graph** `A_alpha` between these
classes.  An edge `CD` is present exactly when the induced `2n` labelled
owners of `C union D` can be partitioned into two exact packets in the full
digraph `D_K(P)`.  Thus an edge certifies all of the following at once:

- the actual owner supports are unchanged;
- every prescribed deletion prefix is retained;
- the two output cycles have length exactly `n` and rainbow first labels;
- both output cycles have residence exactly `m` for every coordinate.

Let \(\nu_\alpha\) be the maximum matching size and put

\[
\eta_\alpha=
\max_{S\subseteq L_\alpha}
\bigl(|S|-|N_{A_\alpha}(S)|\bigr).
\tag{5.3}
\]

### Theorem 5.1 (optimal whole-cycle two-absorber repair)

Among all repairs obtained by applying flag-preserving `2-to-2` exact
absorbers to whole original cycles, the number of unrepaired cycles of type
pair (5.1) is exactly

\[
\boxed{
u_\alpha
=\ell_\alpha+r_\alpha-2\nu_\alpha
=(r_\alpha-\ell_\alpha)+2\eta_\alpha.}
\tag{5.4}
\]

Consequently the exact unrepaired owner count in this model is

\[
\boxed{
L_2
=n\sum_{\{\pm\boldsymbol\alpha\}}u_\alpha.}
\tag{5.5}
\]

When the two defect classes both have size `N_alpha`, their contribution is

\[
\boxed{2n\eta_\alpha.}
\tag{5.6}
\]

#### Proof

Theorem 4.1 forces every two-cycle absorber to pair opposite defect classes.
Different unordered pairs (5.1) use disjoint cycle classes.  Within one pair,
whole-cycle absorbers must be vertex-disjoint, so they are precisely matchings
in `A_alpha`.  A matching of size \(\nu_\alpha\) repairs
\(2\nu_\alpha\) cycles and leaves
\(\ell_\alpha+r_\alpha-2\nu_\alpha\) cycles.

Hall's deficiency theorem gives

\[
\nu_\alpha=\ell_\alpha-\eta_\alpha.
\tag{5.7}
\]

Substitution proves (5.4); multiplying by `n` and summing proves (5.5).
Equal side sizes give (5.6).  Distinct matching edges use disjoint original
owner sets, so all certified repartitions can be made simultaneously.

The same optimum applies to any sequence in which every operation consumes
two current cycles and immediately outputs two exact packets.  Once an exact
packet has been produced, its zero defect prevents it from participating in
a later repair with one nonzero-defect cycle, by Theorem 4.1.  Thus such a
sequence cannot evade the matching bound.  QED.

Formula (5.4) separates two different obstructions:

\[
\underbrace{r_\alpha-\ell_\alpha}_{\text{defect-type imbalance}}
\quad+\quad
\underbrace{2\eta_\alpha}_{\text{support/label Hall shortage}}.
\tag{5.8}
\]

Global cancellation (1.18) does not force
\(\ell_\alpha=r_\alpha\); three or more different vectors can cancel
without any opposite pair.

### The literal minimum deficient cut

Fix one graph `A_alpha`.  Build a network with arcs

\[
s\to C\quad(C\in L_\alpha),
\qquad
C\to D\quad(CD\in E(A_\alpha)),
\qquad
D\to t\quad(D\in R_\alpha).
\tag{5.9}
\]

Give the exterior arcs capacity one and the middle arcs capacity
\(\ell_\alpha+1\).  A minimum cut never cuts a middle arc, because the cut
\(\{s\}\) has capacity \(\ell_\alpha\).  If
\(S\subseteq L_\alpha\) lies on the source side, all of `N(S)` must also
lie there.  The least cut with that `S` has
capacity

\[
\ell_\alpha-|S|+|N(S)|.
\tag{5.10}
\]

Minimizing (5.10) is equivalent to maximizing (5.3), and gives

\[
\min\operatorname{cut}
=\ell_\alpha-\eta_\alpha
=\nu_\alpha.
\tag{5.11}
\]

Thus a maximizing set in (5.3) is an exact, polynomially recoverable minimum
deficient-cut certificate.

Equivalently, fix a maximum matching and start from its unmatched left
vertices.  Follow unmatched edges left-to-right and matched edges
right-to-left.  If `S` and `T` are the reachable left and right vertices,
then no vertex of `T` is unmatched, or there would be an augmenting path;
all neighbors of `S` lie in `T`; and matching edges biject `T` with the
matched vertices of `S`.  Hence

\[
T=N(S),
\qquad
|S|-|T|=\eta_\alpha.
\tag{5.12}
\]

### Corollary 5.2 (support-expansion criterion)

Suppose every left cycle in `A_alpha` has degree at least `d` and every right
cycle has degree at most `D`, where `D>0`.  Then, for every
\(S\subseteq L_\alpha\),

\[
d|S|
\le e(S,N(S))
\le D|N(S)|.
\tag{5.13}
\]

Therefore

\[
|N(S)|\ge\frac dD|S|.
\tag{5.14}
\]

If `d>=D`, Hall saturates the left side; if additionally the class sizes are
equal, every cycle in the pair is repaired.  If `d<D`, then

\[
\eta_\alpha
\le\left(1-\frac dD\right)\ell_\alpha
\tag{5.15}
\]

and

\[
u_\alpha
\le(r_\alpha-\ell_\alpha)
+2\left(1-\frac dD\right)\ell_\alpha.
\tag{5.16}
\]

#### Proof

Every edge leaving `S` ends in `N(S)`.  Summing the left lower degrees and
the right upper degrees proves (5.13), hence (5.14).  If `d>=D`, (5.14) is
Hall's inequality.  If `d<D`,

\[
|S|-|N(S)|
\le\left(1-\frac dD\right)|S|
\le\left(1-\frac dD\right)\ell_\alpha.
\]

Maximizing over `S` proves (5.15), and (5.4) gives (5.16).  QED.

The degree hypothesis concerns the actual flag-preserving absorber graph,
not a projection to coordinate pairs or defect types.

## 6. Higher arity is genuinely necessary

The correct static absorber object is a hypergraph on the original local
cycles.  A set \(\mathcal S\) is a hyperedge when its labelled owners can be
repartitioned into \(|\mathcal S|\) exact packets in `D_K(P)`.  Theorem 4.1 says
that every hyperedge lies inside the zero-sum family

\[
\sum_{C\in\mathcal S}\boldsymbol\delta_C=0.
\tag{6.1}
\]

The graphs `A_alpha` are exactly the two-uniform components of this absorber
hypergraph.

Pair repair is not incidence-complete.  For distinct coordinates `a,b,c`,
the formal defect vectors

\[
\boldsymbol\delta_1=e_a-e_b,
\qquad
\boldsymbol\delta_2=e_b-e_c,
\qquad
\boldsymbol\delta_3=e_c-e_a
\tag{6.2}
\]

satisfy

\[
\boldsymbol\delta_1+
\boldsymbol\delta_2+
\boldsymbol\delta_3=0,
\tag{6.3}
\]

but no two are opposite.  Thus a collection with these defect types passes
aggregate point balance while no two-cycle absorber is even incidence-
feasible.  Statement (6.2) is an algebraic minimal-arity obstruction; it is
not asserted here that three such cycles form a protected subinstance of a
balanced resolution.

Any continuation of the pair route therefore needs a matching theorem in
the zero-sum absorber hypergraph, not a bad-to-good reservoir matching.

## 7. An exact opposite-defect block with an empty Hall graph

The next theorem shows that even perfect opposite-defect balance does not
create a support-compatible absorber edge.

### Theorem 7.1 (protected two-cycle Hall obstruction)

Let `m>=10`, `n=2m+1`, and `2<=K<=m-1`.  There are `2n` distinct labelled
middle owners with legal deletion words of length `K` such that:

1. their induced full compatibility digraph is exactly two directed rainbow
   `n`-cycles;
2. their two residence defects are

   \[
   e_0-e_1
   \quad\hbox{and}\quad
   e_1-e_0;
   \tag{7.1}
   \]

3. every coordinate occurs exactly twice in every deletion position and
   exactly `2(m-q)` times in the residual states after depth `q`;
4. every fixed consecutive deletion-block histogram is independent of its
   starting depth;
5. the opposite-defect absorber graph has one vertex on each side and no
   edge.  In fact, the induced block has no exact packet at all.

Thus its Hall deficiency is one and its exact two-absorber owner loss is

\[
2n.
\tag{7.2}
\]

#### Construction

Work with coordinate indices modulo `n`.  Take the two cyclic coordinate
orders

\[
h^A=(0,1,2,\ldots,2m)
\tag{7.3}
\]

and

\[
h^B=(1,0,2,4,\ldots,2m,3,5,\ldots,2m-1).
\tag{7.4}
\]

For either order `h=(h_0,...,h_{n-1})`, define the canonical supports

\[
C_j^h=\{h_{j-m+1},\ldots,h_j\},
\tag{7.5}
\]

then replace only the support at `j=m`:

\[
X_j^h=C_j^h\quad(j\ne m),
\qquad
X_m^h=(C_m^h\setminus\{h_1\})\cup\{h_0\}.
\tag{7.6}
\]

Set

\[
d_t(X_j^h)=h_{j-t+1}
\qquad(1\le t\le K).
\tag{7.7}
\]

#### Legality and the intended cycles

Only `X_m^h` is noncanonical.  At that owner, the deletion positions used in
(7.7) are

\[
m,m-1,\ldots,m-K+1\subseteq\{2,\ldots,m\},
\]

so every deleted letter remains in (7.6); this is where `K<=m-1` is used.
Directly from (7.5)-(7.6),

\[
X_j^h\setminus X_{j-1}^h=\{h_j\}
\tag{7.8}
\]

at every transition, including the two transitions around the modified
owner.  Also

\[
d_{t+1}(X_j^h)=h_{j-t}=d_t(X_{j-1}^h).
\tag{7.9}
\]

Hence each row supplies its intended directed rainbow `n`-cycle.

Within one row, the canonical supports are distinct cyclic intervals in
position space.  The exceptional position set is

\[
\{0,2,3,\ldots,m\},
\]

which is not a cyclic interval, so it duplicates none of them.

#### Separation of the two rows

Let `Gamma` be the ordinary numeric cycle

\[
0,1,2,\ldots,2m,0
\]

and let `epsilon(S)` count the edges of `Gamma` induced by `S`.

Every canonical `A`-support is a numeric cyclic interval and has
`epsilon=m-1`; the exceptional `A`-support is

\[
\{0,2,3,\ldots,m\}
\]

and has `epsilon=m-2`.  Thus every `A`-support satisfies

\[
\varepsilon(S)\ge m-2.
\tag{7.10}
\]

Write the `B`-order as

\[
[1,0][E_1,\ldots,E_m][O_1,\ldots,O_{m-1}],
\qquad E_r=2r,\quad O_r=2r+1.
\tag{7.11}
\]

Every canonical length-`m` block in this order has `epsilon<=2`:

- a block avoiding `1,0` is either all evens or an even suffix followed by
  an odd prefix; the length equation leaves at most one numeric adjacent
  even-odd pair;
- a block containing both `1,0` is an odd suffix, followed by `1,0`, followed
  by an even prefix; its only possible numeric edges are `01` and `12`;
- a block containing exactly one of `1,0` has no numeric edge.

The exceptional `B`-support is

\[
\{1,2,4,\ldots,2m-2\},
\]

and has `epsilon=1`.  Therefore every `B`-support `T` satisfies

\[
\varepsilon(T)\le2.
\tag{7.12}
\]

If an `A`-support `S` and a `B`-support `T` were Johnson-adjacent, deleting
the unique element of `S\setminus T` could destroy at most two numeric-cycle
edges.  Hence

\[
\varepsilon(T)\ge\varepsilon(S)-2\ge m-4>2,
\]

contradicting (7.12).  Equality of supports is even more immediate.  Thus
the rows have no equal or Johnson-adjacent supports.

Because `K>=2`, any predecessor `Y` of `X_j^h` in the induced digraph must
satisfy

\[
d_1(Y)=d_2(X_j^h)=h_{j-1}.
\tag{7.13}
\]

Within that row, first labels are bijective, so `Y=X_{j-1}^h`.  A candidate
in the other row is excluded by the absence of cross-row Johnson adjacency.
The induced compatibility digraph is therefore exactly the two intended
cycles.

#### Exact margins and failure of residence

Relative to a canonical row, modification (7.6) gives `h_0` one extra owner
slot and `h_1` one fewer.  In row `A` this is defect `e_0-e_1`.  In row `B`,
`h_0=1` and `h_1=0`, so the defect is `e_1-e_0`.  The aggregate residence of
every coordinate is therefore exactly `2m`.

For fixed `t`, the map

\[
j\longmapsto h_{j-t+1}
\]

is a coordinate bijection in each row.  Thus every coordinate appears twice
at deletion position `t`.  After `q` deletions it occurs in exactly

\[
2m-2q=2(m-q)
\tag{7.14}
\]

residual states.  The same cyclic-shift argument applied to any consecutive
block of deletion positions proves the stated block stationarity.

Neither forced cycle has zero defect, so neither is exact.  Since the induced
digraph has no other directed cycle, the `2n` owners admit no exact packet
and in particular no two-packet repartition.  This proves every claim.  QED.

For fixed `A`, condition `2<=K<=m-1` holds for all sufficiently large `m`.
The construction therefore survives the entire `A sqrt(m)` window.  It is
not a balanced completion on all of `Omega`; owners outside the block could
introduce new absorber routes in a global resolution.

## 8. Consequences and the smallest remaining gate

The residence/Hall route now has three logically separate levels.

1. **Visible common routing.**  The column laws and every queue cut in
   Theorem 2.1 must pass.  These conditions are polynomial but only
   coordinatewise necessary.
2. **Shadow-resource feasibility.**  The fractional dual in Theorem 3.1 must
   have value `B`, and the cost dual in Theorem 3.2 must permit total cost
   `o(W/S_K)`.  These are full resource statements but remain fractional.
3. **Integral zero-sum absorption.**  Defect cancellation must be organized
   into support-compatible zero-sum absorber hyperedges.  Pair absorbers are
   completely controlled by Theorem 5.1, but they fail both when the defect
   multiset is not centrally symmetric and when an opposite pair lacks a
   support-compatible edge, as in Theorem 7.1.

The smallest clean replacement statement exposed by this wave is the
following unproved lemma.

### Unproved zero-sum resource-rounding lemma `ZSR_A`

For fixed `A`, within the shadow-resource hypergraphs arising from integral
balanced nested flags through `K=ceil(A sqrt(m))`, every fractional perfect
resource cover of cost `o(W/S_K)` can be rounded to an integral perfect
resource matching of cost `o(W/S_K)` by flag-preserving zero-sum absorber
operations.

By (3.18), `ZSR_A` would convert a low-cost fractional construction into the
desired labelled bound.  The phrase **zero-sum** is indispensable by Theorem
4.1.  Theorem 7.1 shows that point margins, deletion-column laws, block
stationarity, opposite defect, and local cycle length do not by themselves
prove the needed absorber expansion.

No total-unimodularity, balanced-hypergraph, or bounded-arity absorber theorem
establishing `ZSR_A` is known here.  It is strictly an integral labelled
statement; it is not equivalent to overload MWB.

## 9. Independent adversarial audit

The main opposite-defect Hall step was independently audited.  The audit
accepted the theorem with the following scope corrections, all incorporated
above.

1. **Bad plus good is impossible.**  A bad-to-good pair absorber violates
   coordinate-incidence conservation.  Pair graphs must join opposite
   nonzero defects.
2. **Defect zero needs the local hypotheses.**  The implication
   \(\boldsymbol\delta=0\Rightarrow\) exact packet uses the rainbow first labels, full
   support-compatible successor law, and word-overlap identities.  It is not
   a statement about an arbitrary list of owners.
3. **Pair optimality is restricted.**  Formula (5.5) is optimal for whole-
   cycle exact `2-to-2` operations.  A three-cycle absorber, a larger global
   repartition, or an operation with intermediate nonexact cycles may evade
   every pair Hall cut.
4. **Type balance is not global point balance.**  Equation (1.18) does not
   imply equal multiplicities of `alpha` and `-alpha`.
5. **Absorber edges are fully labelled.**  Opposite residence vectors alone
   do not create an edge.  Each edge contains a witness using the actual
   owners, full support arcs, and prescribed flags.
6. **The queue cuts are projections.**  Separate coordinate routes need not
   combine into one owner permutation, and they see only the first `K`
   residence stages.
7. **The packet dual is fractional.**  Equality `tau^*=B` does not imply an
   integral perfect matching.  Separation over all candidate cycles may be
   as difficult as packetization itself.
8. **Actual and shadow resources are distinct copies.**  Merging them would
   fail to encode both labelled owner coverage and global shadow cleanliness.
9. **Partial packing is not a factor.**  Any positive uncovered-resource
   bound is an obstruction or partial decomposition statement, not an exact
   middle factor unless an extension theorem is supplied.
10. **The protected block is local.**  Theorem 7.1 proves an induced
    `2n`-owner obstruction and the sharp Hall deficiency inside that block.
    It does not prove that the block embeds protectedly in a full balanced
    resolution.

The audited conclusion is therefore exact: the residence gate is a zero-sum
hypergraph-matching problem.  Ordinary point balance provides only the total
zero-sum identity; ordinary pair Hall applies only after defect types are
oppositely paired; and support-compatible labelled absorption remains the
unproved global step.
