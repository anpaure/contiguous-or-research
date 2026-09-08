# TPC one-copy coloured-Euler rounding: exact lattice obstruction and two integral faces

Date: 2026-08-01  
Status: exact abstract reduction, exact modular obstruction, and two exact
conditional integral theorems.  A stationary private-label pull-clock
circulation by itself does **not** imply a one-copy rounding or bounded
route-inspection cost.  No claim is made here that the actual all-parameter
TPC menu satisfies either positive hypothesis below.

## 0. Outcome

Let `V` be the literal order-`d` de Bruijn state set and let `C` be the
rank-`r` owners.  For owner `c`, let `E_c` be its menu of admissible marked
trace arcs.  Fixed boundary-comparator arcs are collected in `P`.  Put

\[
 \partial(u\to v)={\bf1}_v-{\bf1}_u,
 \qquad \eta=\sum_{e\in P}\partial e .                 \tag{0.1}
\]

After deleting the owners consumed by `P`, the exact one-copy balance
problem is

\[
 x(E_c)=1\quad(c\in C),\qquad
 x\in\{0,1\}^{E},\qquad
 \partial x=-\eta .                                  \tag{0.2}
\]

Weak connectedness of the selected support is an additional condition.  It
is not part of (0.2).

Every marked trace also has a residual-target incidence vector `a(e)`.  If
`lambda^P` is the target vector already paid by the boundary bank, the full
private-label system additionally requires

\[
                    \sum_e a(e)x_e={\bf1}-\lambda^P. \tag{0.3}
\]

All negative results below apply already to the owner-plus-state projection
(0.2), and hence also to the full system.  The positive TU theorem closes
(0.3) only under its explicit payload-transparency hypothesis.  If target
payload varies with the chosen tail/head pair, (0.3) remains another coupled
integer layer and no TU claim is made.

This formulation conditions on one literal choice `P` of the boundary
permutation/root.  Before that choice, even the target projection needs
binary variables `y_P` with

\[
 \sum_Py_P=1,qquad
 \sum_ea(e)x_e+\sum_P\lambda^P y_P={\bf1},            \tag{0.4}
\]

and the chosen `P` also fixes the comparator endpoint states.  Averaged
boundary marginals do not justify fixing an arbitrary `P`; a positive proof
must either retain (0.4) or exhibit one compatible root.

For route-inspection cost `K`, add at most `K` uncoloured de Bruijn arcs `b`
and require

\[
 \partial(x+P+b)={\bf1}_t-{\bf1}_s                 \tag{0.5}
\]

with weakly connected positive support.  Equation (0.2) is the zero-cost
circuit face after the fixed pins have been transferred to `eta`.  The open
trail and bounded-`K` versions are treated by the same parity and flow rows.

For completeness, the unfrozen boundary/root is one correlated object, not
`d` independent marginals.  Let `Pi` be the admissible literal roots.  For
`pi in Pi` let `P_pi` be its boundary trace multiset, `lambda^pi` its target
vector, `rho_{pi,c}` the number of owner-coloured traces of owner `c` in
`P_pi`, and `(s_pi,t_pi)` its endpoints.  With binary `y_pi` and `x_e` and
nonnegative integral uncoloured route arcs `b`, the exact master is

\[
\begin{aligned}
 &\sum_{\pi\in\Pi}y_\pi=1,\\
 &\sum_{e\in E_c}x_e+\sum_{\pi\in\Pi}\rho_{\pi,c}y_\pi=1
                                                  &&(c\in C),\\
 &\sum_ea(e)x_e+\sum_{\pi\in\Pi}\lambda^\pi y_\pi={\bf1},\\
 &\partial\!\left(\sum_e x_e e+b+
                    \sum_{\pi\in\Pi}y_\pi P_\pi\right)
      =\sum_{\pi\in\Pi}y_\pi({\bf1}_{t_\pi}-{\bf1}_{s_\pi}),\\
 &\sum_e b_e\le K ,
\end{aligned}                                             \tag{0.6}
\]

together with weak connectedness.  Thus a positive proof must retain the
single root variable or exhibit one compatible root; averaged boundary
marginals are insufficient.  If `rho_{pi,c}>=2`, that root is immediately
infeasible in the one-copy model.  Equations (0.2)--(0.5) are the
specialization after one feasible root has been fixed and its owner usage
has been transferred to the boundary bank.

If a comparator pin prescribes an **adjacent transition pair**, edge
selection and balance are not enough: the exact master also needs successor
variables (or contracts the prescribed pair to one protected macroedge).
Every topology exchange below is understood to preserve those protected
macroedges.

The conclusions are these.

1. The matrix consisting of owner rows and de Bruijn incidence rows is not
   totally unimodular in general.  Fractional stationarity does not round
   formally.  This failure already occurs in the literal triangular
   private clock at `k=4`.
2. Every lattice obstruction has an exact modular-potential certificate:
   a state potential whose increment is constant on each owner menu but
   whose total increment is incompatible with the pins.
3. If every owner menu is a **payload-transparent tail/head rectangle**, the
   balance problem is an ordinary integral network flow.  Hence every
   fractional solution with integral comparator boundary has an integral
   one-copy solution.
4. If every owner is a reversible pair, the exact criterion is the classical
   prescribed-outdegree cut system.  Without pins it reduces simply to:
   every state has even degree.
5. Neither integral balance nor connected fractional support implies bounded
   route-inspection.  A pin-preserving component 2-switch condition is a
   sufficient zero-cost topology theorem.  Already the literal depth-one
   triangular system at every even `k` and rank two has connected fractional
   support but sharp one-copy open/circuit route costs `k/2-1` and `k/2`.

Thus the post-TPC gate is not another fractional stationary law.  It is an
integral correlation theorem proving either a transparent rectangularization
or the disappearance/absorption of the modular owner signatures, followed by
a protected component-switch theorem.

There is a preliminary pin qualification.  If the requested comparator pin
is the immediate passage `G,v,G` from the two-guard root theorem, then the
one-copy problem is already impossible: its incoming and outgoing traces are
different arcs of the same owner.  The positive pinned theorems below apply
only after one side has been moved to an uncoloured boundary layer, owner
exactness has been punctured, or a different comparator address uses at most
one pinned trace of each owner.

## 1. The exact coloured boundary system

Parallel trace occurrences remain distinct.  An arc carries all of its
private lower labels and all guard/comparator eligibility.  Accordingly,
replacing one arc by another is legal below only when that payload is
preserved literally.

The rational TPC circulation supplies numbers `x_e>=0` satisfying

\[
 \sum_{e\in E_c}x_e=1,\qquad
 \sum_e x_e\partial e=-\eta,\qquad
 \sum_e a(e)x_e={\bf1}-\lambda^P.                    \tag{1.1}
\]

Clearing denominators gives an Eulerian multigraph with repeated owner
colours.  Dividing that tour by its denominator does not choose one physical
arc of every colour.  System (0.2) is exactly the missing assertion.

Choose a base arc `e_c^0` in every unpinned menu and define

\[
 L=\operatorname{span}_{\mathbb Z}
 \{\partial e-\partial e_c^0:e\in E_c,\ c\in C\}
       \subseteq \mathbb Z^V .                       \tag{1.2}
\]

Every integral selector has boundary in the affine lattice

\[
             \beta_0+L,qquad
 \beta_0=\eta+\sum_c\partial e_c^0.                  \tag{1.3}
\]

This lattice condition is only necessary: it forgets that at most one
difference may be used in each owner fibre.

## 2. Complete modular certificates for the lattice relaxation

### Theorem 2.1 (modular-potential obstruction)

Suppose there are an integer `q>=2` and a potential

\[
                   \phi:V\longrightarrow\mathbb Z/q\mathbb Z
\]

such that, for every owner `c`, the increment

\[
       \phi(\operatorname{head}e)-\phi(\operatorname{tail}e)
                    =\delta_c\pmod q                 \tag{2.1}
\]

is independent of `e in E_c`.  Then (0.2) is impossible whenever

\[
 \sum_c\delta_c+
 \sum_{e\in P}
  \bigl(\phi(\operatorname{head}e)-
        \phi(\operatorname{tail}e)\bigr)
                         \ne0\pmod q .                \tag{2.2}
\]

Conversely, assume the fractional equations (1.1), so that there is no real
linear obstruction.  If `-beta_0` does not belong to `L`, then some finite
modulus and potential give a certificate of the form (2.1)--(2.2).

#### Proof

Pair a selected boundary with `phi`.  An arc contributes its potential
increment, so every one-copy selection contributes the fixed residue in
(2.2), whereas a balanced selection contributes zero.  This proves the
first statement.

For the converse, take the Smith normal form of the integer matrix whose
columns are the generators in (1.2).  Real feasibility eliminates every
free-part separating functional.  Failure of lattice membership is
therefore detected in a finite cyclic factor of `Z^V/L`.  The corresponding
character is a row vector modulo `q`, hence a potential `phi`; annihilating
all within-owner differences is exactly (2.1), and nonannihilation of the
desired affine boundary is (2.2).  \(\square\)

This is a complete obstruction only to the lattice relaxation.  Even when
all such characters vanish, the finite Minkowski sum

\[
               \partial E_{c_1}+\cdots+\partial E_{c_{|C|}}
\]

need not contain `-eta`.

For `q=2` and `phi=1_S`, the increment is the indicator that the trace arc
crosses the state cut `delta(S)`.  Hence a particularly checkable necessary
row is:

> if every option of owner `c` has the same crossing parity `p_c(S)`, then
> `sum_c p_c(S)` plus the pinned crossing parity must be even.

These are the literal coloured cut-parity rows of the pull-clock atlas.

### Corollary 2.2 (state-parity route lower bound)

Suppose that at each state in a set `Z`, the parity of the boundary
coefficient is independent of every owner choice and is odd after adding
the pins.  Then every one-copy selector `z` has

\[
             \sum_v |\partial z(v)+\eta(v)|\ge |Z|. \tag{2.3}
\]

If `chi(z+P)` is the number of extra de Bruijn arcs needed to make one Euler
trail, then

\[
                         \chi(z+P)\ge |Z|/2-1.       \tag{2.4}
\]

Indeed, every odd coordinate has absolute value at least one, and an added
arc decreases positive imbalance mass by at most one; one open Euler trail
has positive imbalance mass at most one.

### Proposition 2.3 (fixed-endpoint `T`-join separator)

For an integral selected multiset `z`, let

\[
             \mathcal O(z)=\{v:\partial(z+P)(v)\text{ is odd}\}.
\]

If added route arcs turn it into an Euler trail from fixed `s` to fixed `t`,
then, modulo two, the endpoint set of those added arcs is

\[
                    \mathcal O(z)\mathbin\triangle\{s,t\}. \tag{2.5}
\]

Consequently their number is at least half the size of (2.5), and their
total state-distance is at least the minimum metric `T`-join cost for that
set in the underlying de Bruijn state graph.

#### Proof

Modulo two, the boundary of an arc `u -> v` is
`e_u+e_v`.  The final trail boundary has odd support `{s,t}`.  Taking the
symmetric difference gives (2.5).  Every added edge pairs two odd endpoints;
shortest-path replacement gives the metric `T`-join lower bound. \(\square\)

The directed imbalance and connectivity rows may increase this cost; the
`T`-join is the exact first parity separator, not a sufficient directed
completion theorem.

## 3. The matrix is not TU

Take two states `u,v`.  Give each of three owners the two choices

\[
                         u\to v,qquad v\to u.        \tag{3.1}
\]

Weight both choices by `1/2`.  This is a connected stationary fractional
circulation with owner mass one.  An integral selector chooses `f` forward
arcs and `3-f` reverse arcs.  Balance would require

\[
                             f=3-f,
\]

which is impossible.  Equivalently, `phi(u)=0, phi(v)=1` modulo two makes
every owner increment one and gives the obstruction `3=1 mod 2`.

There is already a determinant-two minor.  Using owner rows `c_1,c_2`, one
state-incidence row, and columns

\[
 c_1:(u\to v),\quad c_1:(v\to u),\quad c_2:(u\to v),
\]

gives, up to row and column signs,

\[
 \begin{pmatrix}
 1&1&0\\
 0&0&1\\
 1&-1&1
 \end{pmatrix},
 \qquad \det=2.                                      \tag{3.2}
\]

Thus neither a network-matrix claim nor ordinary matroid intersection is
available for arbitrary trace menus.

This example is abstract.  It is not asserted to embed in the Boolean TPC
catalogue.  Its role is logical: the hypotheses “one fractional stationary
circulation, connected support, and fixed comparator pins” do not themselves
imply one-copy integrality.

### Theorem 3.1 (literal `k=4` TPC parity obstruction)

The same failure occurs inside the exact Boolean triangular system.  Take

\[
                       k=4,\qquad r=2,\qquad d=1,
\]

so the six owners are the pairs `{i,j}`.  For every owner use its two
private-period-two clock arcs

\[
                           i\to j,\qquad j\to i.      \tag{3.3}
\]

Give each direction total trace weight `1/2`, split as marked weight `1/3`
and unmarked weight `1/6`.  Then:

* every owner has total mass one;
* every singleton state has incoming and outgoing mass `3/2`;
* every singleton target has marked load one; and
* the positive support is connected.

Nevertheless there is no balanced one-copy selector and not even an
unbridged one-copy open Euler trail.

#### Proof

The fractional assertions follow by direct degree counting in `K_4`.
Choosing one direction in (3.3) for every owner is an orientation of `K_4`.
At every vertex its divergence has the parity of its underlying degree,
which is three.  Hence all four divergences are odd and nonzero.  A circuit
would require zero divergences, while an open Euler trail permits exactly
two nonzero divergences.  Both are impossible. \(\square\)

The exact owner-plus-three-independent-state matrix of this instance has a
minor of determinant `-8`.  Its sharp route costs are one added arc for an
open trail and two for a circuit.  These finite statements are independently
replayed by
`scratch/audit_threadD_tpc_onecopy_k4_parity_20260801.py` and its JSON audit.

### Proposition 3.2 (immediate comparator-owner obstruction)

Let

\[
 v=(\{f_1\},\ldots,\{f_d\}),\qquad F=\{f_1,\ldots,f_d\}.
\]

The immediate same-guard comparator passage `G,v,G` uses the two distinct
trace arcs

\[
 (G,\{f_1\},\ldots,\{f_d\}),\qquad
 (\{f_1\},\ldots,\{f_d\},G).                         \tag{3.4}
\]

Both have owner `F union G`.  Therefore no owner-perfect one-copy selector
can contain the passage.  Two guards give the same obstruction in two owner
fibres.  Denominator-cleared fractional Euler tours evade it only by using
multiple copies of each owner.

This is stronger than non-TU: for this literal comparator geometry the pin
set itself is outside the owner partition matroid.  It must be changed before
any balance-rounding theorem can apply.

## 4. A positive TU face: payload-transparent rectangles

For owner `c`, let `A_c` and `H_c` be sets of tail and head states.  Say that
its menu is a **payload-transparent rectangle** if

\[
                         E_c=A_c\times H_c             \tag{4.1}
\]

and every pair in (4.1) realizes the same **complete** target/pin signature
`a(e)=a_c`, including all private labels, guard obligations and pin status
belonging to owner `c`.

### Theorem 4.1 (rectangular coloured-flow integrality)

After fixing any comparator arcs **with distinct consumed owners**, suppose
every remaining owner menu is a
payload-transparent rectangle.  If the fractional balance system (1.1) is
feasible with integral pin boundary `eta`, then (0.2) has an integral
solution, and that solution also satisfies the private-label rows (0.3).

#### Proof

For every owner introduce two nodes `c^-`,`c^+` and a fixed unit arc
`c^- -> c^+`.  For each `u in A_c` add `u -> c^-`; for each `v in H_c` add
`c^+ -> v`.  Impose state boundary `partial f=-eta` and flow conservation
at the owner nodes.  One unit through the fixed owner arc forces exactly one
selected incoming tail and one selected outgoing head.

The tail and head marginals of any fractional solution of (1.1) give a
feasible flow in this network.  Its node-arc incidence matrix is totally
unimodular and all supplies and capacities are integral, so it has an
integral feasible flow.  Every owner then chooses one tail and one head.
Their pair is an admissible literal trace by (4.1), and the state equations
are exactly (0.2).  Payload transparency makes `a(e)` constant throughout
each owner rectangle.  Hence the target sum depends only on the owner
equations and equals its value in the assumed fractional solution, namely
(0.3).  \(\square\)

The theorem remains true after restricting an owner to a smaller rectangle
`A'_c times H'_c`; an arbitrary nonrectangular subset is not covered.
A fixed comparator trace is handled by deleting its owner and transferring
its boundary to `eta`.  A nonrectangular list of allowed tail/head pairs is
precisely where this network proof ceases to be sound.

## 5. A second positive face: reversible owner pairs

Assume every free owner `c` offers exactly the two payload-identical reverse
arcs on an undirected state edge `u_c v_c`.  Let `G` be the resulting
undirected multigraph.  Fixed comparator arcs contribute the boundary
`eta` in (0.1).  Write `deg_G(v)` for free degree and put

\[
                         d_v={\deg_G(v)+\eta(v)\over2}.       \tag{5.1}
\]

### Theorem 5.1 (exact prescribed-orientation criterion)

There is a one-copy balanced orientation extending all fixed comparator arcs
if and only if every `d_v` is an integer and, for every `S subseteq V`,

\[
             |E_G(S)|\le \sum_{v\in S}d_v
               \le |E_G(S)|+|\delta_G(S)|.           \tag{5.2}
\]

Without pins (`eta=0`), this is equivalent simply to every degree of `G`
being even.  If `G` is connected, the selected directed support is weakly
connected and hence is one Euler circuit; its route-inspection cost is zero.

#### Proof

Orienting an edge out of `v` assigns that edge to endpoint `v`.  The balance
equation at `v` is

\[
 \eta(v)+\deg_G(v)-2\operatorname{out}_G(v)=0,
\]

so the required number of assignments to `v` is exactly (5.1).  The problem
is a bipartite `b`-matching between free edges and their two endpoints.
Condition (5.2) is its compressed Hall system: every internal edge of `S`
must be assigned in `S`, and at most the internal plus boundary edges may be
assigned there.  Hall's theorem proves sufficiency and integrality.

When `eta=0`, even degree makes (5.1) integral and

\[
 \sum_{v\in S}d_v=|E_G(S)|+|\delta_G(S)|/2,
\]

so all cuts hold automatically.  Conversely, balance forces even degree.
A connected balanced directed multigraph has an Euler circuit. \(\square\)

For a prescribed open trail from `s` to `t`, add one protected dummy
comparator arc `t -> s`, apply the theorem, and delete that dummy arc.

## 6. Topology: an exact pin-preserving component switch

Suppose a balanced one-copy selector contains unpinned arcs

\[
                  e_c:u\to v,qquad e_f:x\to y         \tag{6.1}
\]

in two different weak components.  If the same payloads admit

\[
                  e'_c:u\to y,qquad e'_f:x\to v,      \tag{6.2}
\]

then replacing (6.1) by (6.2) preserves every state indegree and outdegree,
one-copy ownership, private labels, and all fixed comparator arcs.

### Lemma 6.1 (component merge)

The switch (6.1)--(6.2) reduces the number of weak support components by
one.

#### Proof

Every edge of a weakly connected balanced directed component lies on a
directed cycle, hence is not a bridge of its underlying undirected graph.
Removing the two arcs in (6.1) therefore leaves both old components weakly
connected.  Each new arc crosses between them, so (6.2) joins them. \(\square\)

Consequently, if at every nontrivial partition of the current components
there is a pin-avoiding transparent switch of this form, repeated switches
produce one connected Euler circuit at zero added length.  More generally,
if switching leaves `a=O(1)` components whose endpoint states can be ordered
with total de Bruijn overlap deficit `C=O(1)`, the exact trace-Euler splice
theorem gives route-inspection cost at most `C`.

This switching property does not follow from rectangular balance.  It is the
separate topology hypothesis.

## 7. A literal even-`k` linear route-cost obstruction

### Theorem 7.1 (depth-one private-clock family)

For every even `k>=4`, take

\[
                         r=2,\qquad d=1,\qquad b_1=0. \tag{7.1}
\]

For every pair-owner `{u,v}`, use the two private-clock traces `u->v` and
`v->u`.  Give each direction total weight `1/2`, split into marked and
unmarked weights

\[
             {1\over k-1},\qquad {1\over2}-{1\over k-1}
                    ={k-3\over2(k-1)}.               \tag{7.2}
\]

This is an exact connected triangular marked-trace circulation.  Yet every
one-copy selection requires at least

\[
              {k\over2}-1\quad\hbox{route arcs for an open trail},
        \qquad {k\over2}\quad\hbox{for a circuit}.    \tag{7.3}
\]

Both bounds are sharp.

#### Proof

The two directions of each owner have total mass one.  At every singleton
state, incoming and outgoing mass are both `(k-1)/2`.  A fixed singleton
target is the marked head of `k-1` directed traces, so (7.2) gives it load
one.  Finally

\[
 q_1={\binom{k}{1}\over\binom{k}{2}}={2\over k-1},
\]

which is exactly the aggregate marked suffix mass.  The bidirected complete
support is connected.

A one-copy selector orients `K_k`.  Every state has underlying degree
`k-1`, which is odd, so every divergence is odd.  A circuit sidecar must
toggle all `k` odd states and an open-trail sidecar must toggle all but its
two endpoints.  Each added arc toggles at most two parities, proving the two
lower bounds in (7.3).

For equality in the circuit case, add a perfect matching to `K_k`; the
resulting connected multigraph has even degree at every vertex and hence an
Euler orientation.  For the open case, add a matching on all but two
vertices; the resulting connected multigraph has exactly two odd vertices
and hence an Euler-trail orientation.  Restricting either orientation to the
original edges chooses exactly one direction of every owner. `square`

This is a literal Boolean/private-label family, not merely an abstract
parity gadget.  For `k>4`, however, `(r,d)=(2,1)` is not asserted to be the
central-rank/deadline slice of the main asymptotic problem.  The theorem
refutes a generic implication from fractional TPC stationarity to `O(1)`
one-copy route cost; a positive theorem on the central slice may still use
additional Boolean structure.

The exact Fraction/integer checker
`scratch/audit_threadD_tpc_evenk_route_obstruction_20260801.py` reconstructs
sharp witnesses for `k=4,6,8,10,12`.  Its payload is
`scratch/threadD_tpc_evenk_route_obstruction_20260801.audit.json`.

## 8. Exact surviving TPC gate

Once the private-label stationary pull-clock circulation is granted, the
smallest proof-safe one-copy programme is:

1. **Lattice audit.**  Prove that all modular state potentials (2.1) obey
   the pin congruence (2.2), preferably by a local pull-clock circuit basis.
2. **Correlation.**  Prove an integer-decomposition theorem for the owner
   boundary-and-target Minkowski sum.  A payload-transparent
   rectangularization would suffice.  A reversible-pair decomposition
   satisfying Theorem 5.1 closes only the state rows unless its two
   orientations carry the same target payload.
3. **Topology.**  Prove a protected 2-switch expansion as in Lemma 6.1, or
   exhibit a selected support with only `O(1)` total overlap-reset distance.
4. **Pins.**  Treat comparator traces as fixed columns throughout; checking
   them only after rounding is unsound.

The stationary circulation proves the real-cone part of Step 1 and no more.
The determinant-two and linear route-cost examples show that each later
step is logically load-bearing.
