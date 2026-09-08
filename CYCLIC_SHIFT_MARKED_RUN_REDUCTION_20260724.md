# Cyclic alignment as a marked-run problem

Date: 2026-07-24

## Verdict

Fixing an oriented exact wreath factor turns every middle owner into a
canonical deletion permutation.  Every full nested balanced resolution is
then obtained by assigning a second permutation to each owner.  The labelled
synchronization loss is **exactly** the weighted area of the nontrivial
common-prefix excursions between those two permutations.

There is also a literal one-step shift law along the wreath cycles.  Marking
its failures gives a useful sufficient bound, but counts of shift failures
alone are not enough: a cyclic shift of a deletion word has no one-step shift
failures and nevertheless remains out of synchronization at every proper
depth.  Thus any successful use of the shift law must control the lengths of
the marked runs, not just their number.

On a fixed window `H=ceil(A sqrt(m))`, the quota capacities are bounded.  In
that regime the desired `o(W)` synchronization theorem is equivalent to
`o(W)` total marked-run area.  In particular, all but `o(W)` middle owners
must retain their entire forced deletion prefix through the window.  Merely
choosing an arbitrary integral balanced flow cannot give this: coordinate
relabelings of any balanced flow have expected mismatch

\[
 W\left(1-\binom mq^{-1}\right)
\]

at depth `q`.

The final section gives a Hall-type corridor obstruction.  It identifies the
extra estimate needed by a bounded-run alignment proof and shows why
rankwise local corridor feasibility still does not control run length.

## 1. The forced shift law

Put

\[
 n=2m+1,\qquad W=\binom nm.
\]

Let `F` be an oriented exact middle wreath factor.  Its pointed middle sets
are all the members of `Omega=binom([n],m)`.  On every oriented wreath write

\[
 X_j=I_\pi(j,m),\qquad \tau X_j=X_{j+1}.
\]

Thus `tau` is a permutation of `Omega`, all of whose cycles have length `n`.
Define

\[
 \ell(X)=X\setminus\tau^{-1}X.
\tag{1.1}
\]

This is a singleton, identified below with its unique coordinate.  The
actual depth-`q` lower flag is

\[
 \Gamma_q(X)=I_\pi(j,m-q).
\]

### Lemma 1 (forced deletion word)

For `1<=t<=m`, put

\[
 a_t(X)=\ell(\tau^{-(t-1)}X).
\tag{1.2}
\]

Then

\[
 \boxed{
 \Gamma_q(X)=X\setminus\{a_1(X),\ldots,a_q(X)\}
 }
\tag{1.3}
\]

and

\[
 \boxed{a_{t+1}(\tau X)=a_t(X).}
\tag{1.4}
\]

Equivalently,

\[
 \Gamma_q(X)=X\cap\tau^{-1}X\cap\cdots\cap\tau^{-q}X.
\tag{1.5}
\]

### Proof

If the cyclic coordinate word is `z_0,...,z_(n-1)`, then

\[
 X_j=\{z_j,\ldots,z_{j+m-1}\},
 \qquad \ell(X_j)=z_{j+m-1}.
\]

Hence

\[
 a_t(X_j)=z_{j+m-t},
\]

which proves (1.3) and (1.4).  Intersecting the `q+1` consecutive middle
windows leaves exactly `z_j,...,z_(j+m-q-1)`, proving (1.5).  QED.

For every fixed deletion time `t` and every coordinate `x`, one also has the
exact homomesy

\[
 \boxed{\#\{X:a_t(X)=x\}=W/n.}
\tag{1.6}
\]

Indeed, on each wreath the map `j -> a_t(X_j)` runs through every coordinate
once.

## 2. Every balanced resolution is a family of owner permutations

Take any integral nested balanced resolution all the way to the empty set:

\[
 P_0(X)=X\supset P_1(X)\supset\cdots\supset P_m(X)=\varnothing.
\]

Write

\[
 d_t(X)=P_{t-1}(X)\setminus P_t(X).
\tag{2.1}
\]

Both `(a_1(X),...,a_m(X))` and `(d_1(X),...,d_m(X))` are permutations of
`X`.  There is therefore a unique `rho_X in S_m` such that

\[
 d_t(X)=a_{\rho_X(t)}(X).
\tag{2.2}
\]

Let `[q]={1,...,q}`.  Then

\[
 \boxed{
 P_q(X)=\Gamma_q(X)
 \quad\Longleftrightarrow\quad
 \rho_X([q])=[q].
 }
\tag{2.3}
\]

Thus cyclic alignment is a prefix-set problem for one permutation per
middle owner.

## 3. Exact common-prefix excursion decomposition

For one owner `X`, let

\[
 C_X=\{q\in\{0,1,\ldots,m\}:\rho_X([q])=[q]\}.
\]

Write its elements in increasing order as

\[
 0=r_0<r_1<\cdots<r_s=m.
\]

For consecutive common times `r_(i-1)<r_i`, the permutation maps the block

\[
 \{r_{i-1}+1,\ldots,r_i\}
\]

onto itself.  If its length is at least two, then no proper prefix of the
block is invariant.  Call the open state interval

\[
 \mathcal R_i(X)=\{r_{i-1}+1,\ldots,r_i-1\}
\tag{3.1}
\]

a **marked excursion run**.  It is precisely a maximal interval of depths
at which `P_q(X) != Gamma_q(X)`.

Let

\[
 E_H(F,P)=\sum_{q=1}^H\frac{e_q(F,P)}{c_q},
 \qquad
 e_q(F,P)=\#\{X:P_q(X)\ne\Gamma_q(X)\}.
\]

### Theorem 2 (exact marked-run coarea identity)

For every `H<=m`,

\[
 \boxed{
 E_H(F,P)=
 \sum_{X\in\Omega}\ \sum_i\ 
 \sum_{q\in\mathcal R_i(X)\cap[H]}\frac1{c_q}.
 }
\tag{3.2}
\]

This is an identity, not an estimate.

For fixed `A>0` and `H=ceil(A sqrt(m))`, there is a constant `C_A` with

\[
 1\le c_q\le C_A\qquad(q\le H).
\]

Consequently, if

\[
 R_H(F,P)=\sum_X\#\{q\le H:P_q(X)\ne\Gamma_q(X)\},
\]

then

\[
 \boxed{
 C_A^{-1}R_H(F,P)\le E_H(F,P)\le R_H(F,P).
 }
\tag{3.3}
\]

In particular,

\[
 \boxed{
 E_H(F,P)=o(W)\quad\Longleftrightarrow\quad R_H(F,P)=o(W)
 }
\tag{3.4}
\]

on every fixed Gaussian window.  This forces all but `o(W)` owners to agree
with their wreath flag at **every** depth through `H`.

### Proof

Equation (2.3) says exactly that the marked depths for owner `X` are the
disjoint union of the intervals (3.1).  Summing their depth weights proves
(3.2).  The fixed-window estimate

\[
 \log(W/N_q)=q(q+1)/m+O_A(m^{-1/2})
\]

gives the bounded capacities and hence (3.3)--(3.4).  QED.

This shows how strong the labelled alignment route is.  It is not enough
that the same exceptional owners be reused at many depths: the objective
charges the complete vertical area of every excursion.

## 4. Marked deletion sites and necessary point homomesy

Call `(X,t)` a marked deletion site when

\[
 d_t(X)\ne a_t(X).
\]

Put

\[
 K_H=\#\{(X,t):t\le H,\ d_t(X)\ne a_t(X)\}.
\]

### Lemma 3 (sites are controlled by run area)

Let `B_H` be the number of nontrivial owner-permutation blocks whose right
endpoint is at most `H`.  Then the sharper form is

\[
 \boxed{K_H\le R_H(F,P)+B_H\le2R_H(F,P).}
\tag{4.1}
\]

### Proof

Consider one nontrivial permutation block of length `l`.  If it ends by
depth `H`, it contains at most `l` moved positions and contributes `l-1`
mismatched prefix states, hence costs at most one site beyond its run area.
If it crosses `H`, the number of its marked positions at most `H` is no more
than its truncated run area.  Summing gives the first inequality.  Every
completed nontrivial block contains at least one mismatched prefix state, so
`B_H<=R_H`, proving the second.  QED.

There is also an exact site/run formula.  For one owner, let

\[
 z_1<\cdots<z_k
\]

be the moved deletion positions `rho_X(t)!=t`, put `z_(k+1)=m+1`, and set

\[
 \beta_j=1_{\{\rho_X([z_j])\ne[z_j]\}}.
\]

The prefix state cannot change at an unmoved position.  Hence this owner's
exact contribution is

\[
 \boxed{
 \sum_{j=1}^k\beta_j
 \sum_{q=z_j}^{\min(H,z_{j+1}-1)}\frac1{c_q}.
 }
\tag{4.1a}
\]

Formula (4.1a) is the literal `marked sites + marked runs` ledger: a moved
site starts, ends, or changes a run, while the complete gap to the next moved
site is charged whenever the prefix remains mismatched.

For the desired flow, define its deletion-position margins

\[
 p_{t,x}=\#\{X:d_t(X)=x\}.
\]

Using (1.6), changing `k_t` deletion labels changes the margin histogram by
`L1` distance at most `2k_t`.  Therefore

\[
 \boxed{
 \sum_{t=1}^H\frac12\sum_{x\in[n]}
 \left|p_{t,x}-\frac Wn\right|
 \le K_H\le2R_H\le2C_AE_H.
 }
\tag{4.2}
\]

Thus low-cost cyclic alignment forces the balanced flow to have almost
perfect deletion-coordinate homomesy in total over the whole window.  The
floor/ceiling quotas on the remaining sets do not imply these margins.

There is also a necessary one-step shift estimate.  Put

\[
 v_t=\#\{X:d_{t+1}(\tau X)\ne d_t(X)\}.
\tag{4.3}
\]

By (1.4), a violation in (4.3) requires at least one of its two deletion
sites to be marked.  Hence

\[
 \boxed{
 \sum_{t=1}^{H-1}v_t
 \le2K_H\le4R_H\le4C_AE_H.
 }
\tag{4.4}
\]

Consequently `(CA_A)` implies both total point-margin error `o(W)` and total
one-step shift defect `o(W)`.  These are genuine additional necessary tests
for any proposed balanced-flow construction.

### Theorem 4 (weighted crossing coarea)

For `rho in S_m`, an arc `t -> rho(t)` crosses the depth cut `q` when

\[
 \min\{t,\rho(t)\}\le q<\max\{t,\rho(t)\}.
\]

For one owner define its truncated weighted footrule

\[
 \mathcal D_H(\rho)
 =\sum_{t=1}^m
 \sum_{\substack{q\le H\\
 \min(t,\rho(t))\le q<\max(t,\rho(t))}}
 \frac1{c_q}.
\tag{4.5}
\]

Equivalently, define the open-token count across cut `q` by

\[
 \kappa_X(q)=\#\{t\le q:\rho_X(t)>q\}.
\tag{4.5a}
\]

The same number of permutation arcs crosses in the opposite direction, so

\[
 \rho_X([q])\ne[q]\quad\Longleftrightarrow\quad\kappa_X(q)>0,
\]

and

\[
 \frac12\mathcal D_H(\rho_X)
 =\sum_{q=1}^H\frac{\kappa_X(q)}{c_q}
 =\sum_{t:\rho_X(t)>t}
 \sum_{q=t}^{\min(H,\rho_X(t)-1)}\frac1{c_q}.
\tag{4.5b}
\]

Thus (4.6) is the level-one coarea inequality
`1_{kappa>0}<=kappa`.  It is exact whenever at most one token crosses each
prefix cut, including the cyclic-shift obstruction in Section 6.

Then

\[
 \boxed{
 E_H(F,P)\le\frac12\sum_X\mathcal D_H(\rho_X).
 }
\tag{4.6}
\]

In particular, if every owner permutation has bandwidth at most `D`, then

\[
 \boxed{
 E_H(F,P)\le\frac D2
 \#\{(X,t):\rho_X(t)\ne t,
 \ [\min(t,\rho_X(t)),\max(t,\rho_X(t)))\cap[H]\ne\varnothing\}.
 }
\tag{4.7}
\]

Thus, for fixed `D`, `o(W)` moved deletion sites are sufficient for the
fixed-window cyclic-alignment theorem.

### Proof

If `rho([q])!=[q]`, at least one permutation arc crosses the cut from left to
right.  Since `rho` is bijective, the number crossing from right to left is
the same.  Hence at least two arcs cross every mismatched prefix cut.  Thus

\[
 1_{\{\rho([q])\ne[q]\}}
 \le\frac12\#\{t:\text{the arc }t\to\rho(t)
 \text{ crosses }q\}.
\]

Multiply by `1/c_q`, sum over `q<=H`, reverse the sums, and then sum over
owners.  This proves (4.6).  Under bandwidth `D`, each moved arc crosses at
most `D` relevant cuts and every weight is at most one, proving (4.7).
QED.

The unweighted full-depth version is the familiar Spearman-footrule bound

\[
 \#\{q:\rho([q])\ne[q]\}
 \le\frac12\sum_t|\rho(t)-t|.
\tag{4.8}
\]

This is the cleanest positive `marked sites + marked runs` statement: either
control the total displacement directly, or control both the number of
moved sites and their maximum displacement.  Neither ingredient alone is
enough, as Section 6 shows.

## 5. Diagonal shift runs give a sufficient bound

For a base owner `Z`, diagonalize the desired labels by

\[
 y_t(Z)=d_t(\tau^{t-1}Z).
\tag{5.1}
\]

The forced word is constant on this diagonal:

\[
 a_t(\tau^{t-1}Z)=\ell(Z).
\]

There is a unique integer offset

\[
 h_t(Z)=t-\rho_{\tau^{t-1}Z}(t)
 \in\{-(m-1),\ldots,m-1\}
\tag{5.1a}
\]

such that

\[
 \boxed{y_t(Z)=\ell(\tau^{h_t(Z)}Z).}
\tag{5.1b}
\]

Because a wreath uses every coordinate once and `|h_t|<n`, the following
are exact:

* `h_t(Z)=0` iff the deletion site is unmarked;
* `h_(t+1)(Z)!=h_t(Z)` iff the corresponding one-step shift law fails;
* `|h_t(Z)|` is the displacement of that deletion occurrence in the owner
  permutation.

Thus the diagonal picture is an integer height field: anchor error is its
boundary value, shift error is its discrete gradient, and the weighted
footrule controls its `L1` mass.  In particular,

\[
 \sum_Z\sum_{t=1}^H|h_t(Z)|
 \le
 H\sum_Z|h_1(Z)|
 +\sum_Z\sum_{s=1}^{H-1}(H-s)
 |h_{s+1}(Z)-h_s(Z)|.
\tag{5.1c}
\]

This elementary Poincare bound explains the necessary run-length weights:
unweighted anchor and gradient counts cannot replace the factors `H` and
`H-s`.

Let `J_Z` be the maximal intervals `[u,v]` on which

\[
 y_t(Z)\ne\ell(Z).
\]

Put

\[
 w_t=\sum_{q=t}^H\frac1{c_q}.
\tag{5.2}
\]

### Theorem 5 (diagonal marked-run upper bound)

\[
 \boxed{
 E_H(F,P)
 \le
 \sum_Z\ \sum_{[u,v]\in J_Z}\ \sum_{t=u}^v w_t.
 }
\tag{5.3}
\]

Equivalently, using the offset field,

\[
 E_H(F,P)
 \le\sum_Z\sum_{t=1}^Hw_t1_{\{h_t(Z)\ne0\}}
 \le\sum_Z\sum_{t=1}^Hw_t|h_t(Z)|.
\tag{5.3a}
\]

Consequently the weighted boundary-gradient estimate is

\[
\begin{aligned}
E_H(F,P)\le{}&
\left(\sum_{t=1}^Hw_t\right)\sum_Z|h_1(Z)|\\
&+\sum_{s=1}^{H-1}
\left(\sum_{t=s+1}^Hw_t\right)
\sum_Z|h_{s+1}(Z)-h_s(Z)|.
\end{aligned}
\tag{5.3b}
\]

For one run,

\[
 \boxed{
 \sum_{t=u}^v w_t
 =\sum_{q=u}^{v-1}\frac{q-u+1}{c_q}
 +(v-u+1)\sum_{q=v}^H\frac1{c_q}.
 }
\tag{5.4}
\]

Uniformly in the Gaussian range `H=o(m^(2/3))`,

\[
 w_t\le
 C e^{-t^2/m}
 \min\left\{H-t+1,\frac{\sqrt m}{1+t/\sqrt m}\right\}.
\tag{5.5}
\]

Thus it is sufficient to make the sum of the corresponding Gaussian
marked-run costs `o(W)`.

This diagonal union bound is deliberately only sufficient and can lose a
full factor `H`.  In the cyclic-shift example of Section 6, the true cost of
one modified wreath is

\[
 n\sum_{q\le H}\frac1{c_q},
\]

whereas (5.3) gives

\[
 n\sum_{q\le H}\frac q{c_q}.
\]

The exact prefix-excursion identity (3.2), the moved-site formula (4.1a), or
the crossing coarea bound (4.6) should therefore be used whenever a sharp
`o(W)` ledger is needed.

### Proof

If all desired deletion labels through time `q` equal their forced labels,
then the two depth-`q` states agree.  Therefore

\[
 1_{\{P_q(X)\ne\Gamma_q(X)\}}
 \le\sum_{t=1}^q1_{\{d_t(X)\ne a_t(X)\}}.
\]

Sum first over owners and then over `q`, and use the bijection
`X=tau^(t-1)Z`.  This gives (5.3).  Reversing the order of the two sums on
one interval gives (5.4).  Finally

\[
 c_q\ge\tfrac12 W/N_q,
 \qquad
 \log(W/N_q)=q(q+1)/m+o(1),
\]

followed by the finite and infinite Gaussian-tail bounds, proves (5.5).
QED.

A run starting after time one is born at a one-step shift violation; a run
starting at time one is born at an anchor mismatch `d_1(Z)!=ell(Z)`.
However, its cost depends on its **length**, not merely on its birth.
More exactly, if

\[
 B_0=\#\{Z:d_1(Z)\ne\ell(Z)\},
\]

then

\[
 \boxed{
 \sum_Z|J_Z|\le B_0+\sum_{t=1}^{H-1}v_t.
 }
\tag{5.6}
\]

Indeed, a later bad run begins with a `0 -> 1` change of the diagonal bad
indicator and therefore with a one-step label change.  Bound (5.6) controls
the number of run births only; Sections 5--6 show why their weighted
lifetimes remain the essential quantity.

## 6. Sharp no-go: zero shift defects can coexist with one maximal run

Take one wreath and replace, for every owner on that wreath, its forced
deletion word by the cyclic shift

\[
 (d_1,d_2,\ldots,d_m)=(a_2,a_3,\ldots,a_m,a_1).
\tag{6.1}
\]

Leave all other wreaths unchanged.  This is a valid family of nested flags.
For every base owner on the modified wreath and every `t<m`,

\[
 y_t(Z)=a_{t+1}(\tau^{t-1}Z)=\ell(\tau^{-1}Z),
\]

which is independent of `t` and differs from `ell(Z)`.  Hence:

* through every window `H<=m-1`, every one-step shift defect in (4.3)
  with `t<H` is zero;
* every diagonal has one bad run `[1,m-1]`;
* every owner has one prefix excursion through all depths `1,...,m-1`.

The modified wreath contributes

\[
 n\sum_{q=1}^H\frac1{c_q}
\]

to the synchronization loss.  Moreover, every intermediate desired state
is mismatched.  This construction is not asserted to be balanced.  Its role
is structural: one-step shift counts alone cannot control the marked-run
cost.  A return/common-prefix estimate is indispensable.

There is a separate bounded-corridor obstruction.  Let `rho` be the
successor permutation of the cyclic ordering

\[
 1,3,5,\ldots,\text{largest odd},
 \text{largest even},\text{largest even}-2,\ldots,2,1.
\tag{6.2}
\]

Consecutive entries in this cycle differ by at most two, including the last
step `2 -> 1`.  Hence

\[
 |\rho(i)-i|\le2\qquad(i\in[m]).
\tag{6.3}
\]

The permutation is one `m`-cycle, so it leaves no proper prefix `[q]`
invariant.  Assigning

\[
 d_t(X)=a_{\rho(t)}(X)
\tag{6.4}
\]

therefore creates one maximal prefix excursion through depths `1,...,m-1`.
In fact its open-token count from (4.5a) is exactly

\[
 \kappa(q)=1\qquad(1\le q<m):
\tag{6.4a}
\]

at an odd cut the unique right-moving arc starts at that odd position, and
at an even cut it starts at the preceding odd position.
Nevertheless (6.3), applied also to `rho^(-1)`, gives at every depth

\[
 \boxed{
 \Gamma_{q+2}(X)\subseteq P_q(X)\subseteq\Gamma_{q-2}(X)
 }
\tag{6.5}
\]

whenever the displayed indices lie in `[0,m]` (with the evident endpoint
truncation otherwise).  Indeed,

\[
 [q-2]\subseteq\rho([q])\subseteq[q+2].
\]

Thus uniformly bounded local containment also fails to control return time.
The cyclic shift (6.1) and the bandwidth-two cycle (6.2) isolate the two
independent missing estimates: shift anchoring and common-prefix return.

## 7. A Hall obstruction for bounded excursion blocks

For `D<=min(q,m-q)`, define the `D`-corridor of a depth-`q` target by

\[
 X\sim_{q,D}S
 \quad\Longleftrightarrow\quad
 \Gamma_{q+D}(X)\subseteq S\subseteq\Gamma_{q-D}(X).
\tag{7.1}
\]

For a target family `A subset binom([n],m-q)`, put

\[
 \mathcal N_{q,D}(A)=
 \{X:\text{some }S\in A\text{ satisfies }X\sim_{q,D}S\}.
\tag{7.2}
\]

For an owner family `B subset Omega`, put dually

\[
 \mathcal M_{q,D}(B)=
 \{S:\text{some }X\in B\text{ satisfies }X\sim_{q,D}S\}.
\tag{7.2a}
\]

Call the marked prefix excursion containing `q` **`D`-local at `q`** when
its two common-prefix endpoints lie within `q-D` and `q+D`.  (A total block
span at most `D` is a stronger sufficient condition.)  Every `D`-local
assignment necessarily satisfies (7.1) for `S=P_q(X)`.

### Theorem 6 (corridor Hall deficiency)

For every balanced nested resolution,

\[
 \boxed{
 e_q(F,P)\ge
 \max\left\{
 \max_A\left(c_q|A|-|\mathcal N_{q,D}(A)|\right)_+,\ 
 \max_B\left(|B|-(c_q+1)|\mathcal M_{q,D}(B)|\right)_+
 \right\}.
 }
\tag{7.3}
\]

More precisely, the first term lower-bounds non-`D`-local assignments into
`A`, while the second lower-bounds owners in `B` forced to use non-`D`-local
assignments.

### Proof

`N_(q,D)(A)`, so there are at most `|N_(q,D)(A)|` such assignments.  This
gives the first deficiency.
Balance assigns at least `c_q|A|` owners to targets in `A`.  Every assignment
coming from a `D`-local excursion uses a distinct owner in `N_(q,D)(A)`, so
there are at most `|N_(q,D)(A)|` such assignments.  This gives the first
deficiency.
`N_(q,D)(A)`, so there are at most `|N_(q,D)(A)|` such assignments.  This
gives the first deficiency.

Dually, the `D`-local assignments of owners in `B` can use only targets in
`M_(q,D)(B)`, whose total upper capacity is
`(c_q+1)|M_(q,D)(B)|`.  Every remaining owner of `B` must use a
non-`D`-local marked excursion, giving the second deficiency.  QED.

These two Hall families are jointly sharp at one rank.  In the corridor
bipartite graph, give every owner demand one and every target capacity
`[c_q,c_q+1]`.  Hoffman circulation (equivalently, lower/upper-capacitated
Hall) says that a completely corridor-supported balanced assignment exists
if and only if

\[
 c_q|A|\le|\mathcal N_{q,D}(A)|\quad\text{for every target family }A
\tag{7.3a}
\]

and

\[
 |B|\le(c_q+1)|\mathcal M_{q,D}(B)|
 \quad\text{for every owner family }B.
\tag{7.3b}
\]

Thus a bounded-run proof needs uniform corridor expansion strong enough to
make every cut deficiency in (7.3) negligible.  Even that is not sufficient
rank by rank: the bandwidth-two construction (6.2)--(6.5) stays in one fixed
corridor at every depth while forming one excursion of maximal length.  The
missing theorem must also rule out long directed cycles of locally legal
choices, or break them into `o(W)` total return time.

For `D=1`, fixing the states at depths `q-1` and `q+1` leaves exactly two
possible sibling states at depth `q` for every owner.  They form the two
endpoints of an edge in a target multigraph `G_q`; choosing states is an
orientation toward the chosen endpoint.  Conditions (7.3a)--(7.3b) reduce
to the exact indegree-bounds criterion

\[
 \boxed{
 i_{G_q}(U)\ge c_q|U|,
 \qquad
 e_{G_q}(U)\le(c_q+1)|U|
 \quad\text{for every target set }U,
 }
\tag{7.4}
\]

where `i_G(U)` counts edges incident with `U` and `e_G(U)` counts edges
internal to `U`.  An adjacent transposition of deletion positions `q,q+1`
changes only the depth-`q` state, so (7.4) is an exact integral cost-one
local repair gate.  It still cannot be applied independently at successive
depths: changing depth `q` changes the sibling-option multigraphs at
`q-1,q+1`, and the recorded `n=9` Hall example shows that separately chosen
balanced neighboring marginals need not glue.

There is an even cleaner simultaneous formulation if the whole resolution
is required to stay in the `D=1` corridor.  Define the two fixed options for
owner `X` at depth `q` by

\[
 S^0_q(X)=\Gamma_q(X),
 \qquad
 S^1_q(X)=\Gamma_{q+1}(X)\cup\{a_q(X)\}.
\tag{7.5}
\]

The second is obtained by swapping the forced deletion positions `q,q+1`.

### Theorem 7 (exact adjacent-toggle resolver)

A full owner flag stays in the symmetric `D=1` corridor at every depth if
and only if its relative permutation is a product of disjoint adjacent
transpositions.  Equivalently, there is an independent set

\[
 T_X\subseteq\{1,\ldots,m-1\}
\]

in the path of deletion depths such that

\[
 P_q(X)=
 \begin{cases}
 S^1_q(X),&q\in T_X,\\
 S^0_q(X),&q\notin T_X.
 \end{cases}
\tag{7.6}
\]

Every marked excursion is then a singleton and the owner cost is exactly

\[
 \sum_{q\in T_X\cap[H]}\frac1{c_q}.
\tag{7.7}
\]

Consequently a `D=1` proof of `(CA_A)` is **exactly** the following
conflict-free orientation problem.  In every sibling multigraph `G_q`,
choose one endpoint of every owner-edge so that all target indegrees are in
`{c_q,c_q+1}`, subject to the sole cross-depth conflict

\[
 (X,q)\text{ and }(X,q+1)
 \quad\text{cannot both choose the sibling endpoint}.
\tag{7.8}
\]

The total weight of sibling choices must be `o(W)`.

### Proof

The corridor inclusions at all cuts are equivalent to

\[
 [q-1]\subseteq\rho_X([q])\subseteq[q+1]
 \qquad(1\le q<m),
\]

which is equivalent to `|rho_X(t)-t|<=1` for every `t`.  A permutation of
bandwidth one consists exactly of fixed points and disjoint adjacent
transpositions.  A transposition `(q,q+1)` changes only the prefix at depth
`q`, giving (7.5)--(7.7).  Disjointness of the transpositions is precisely
the path-independent-set conflict (7.8).  QED.

Theorem 7 is sharper than separate rankwise Hall feasibility: (7.4) solves
each orientation in isolation, while (7.8) is the exact remaining gluing
condition for a globally nested bandwidth-one repair.

### Corollary 8 (two-stage parity resolver)

For every even depth `q`, choose a balanced orientation of `G_q` and let
`T_q` be its set of sibling choices.  There are no conflicts among these
even-depth choices.  For an odd depth put

\[
 B_q=T_{q-1}\cup T_{q+1}.
\tag{7.9}
\]

Force every owner in `B_q` to its actual endpoint in `G_q`.  Then the
even-depth orientations extend to one simultaneous `D=1` balanced
resolution if and only if every resulting odd-depth orientation problem is
feasible.  The odd problems are mutually independent.

After subtracting the forced actual-endpoint preload, feasibility of each
odd problem is again given exactly by the lower/upper Hall cuts for the
remaining owner-edge/target network.  Therefore a sufficient radius-one
absorber theorem is:

1. choose balanced even orientations of total weighted reversal cost
   `o(W)`;
2. prove that deleting/forcing the adjacent owner sets (7.9) preserves all
   odd lower/upper Hall cuts;
3. choose the odd orientations with total weighted reversal cost `o(W)`.

The union of the two reversal families then obeys (7.8), is balanced at all
depths, and has exact synchronization cost `o(W)` by (7.7).

This parity reduction isolates the needed robustness: not an arbitrary
multirank matching theorem, but stability of the sibling-orientation Hall
conditions under a sparse forced preload inherited from the opposite
parity.

## 8. Balanced flow by itself gives no alignment

Let `P` be any integral balanced nested resolution and, for a coordinate
permutation `sigma`, set

\[
 P_q^\sigma(X)=\sigma P_q(\sigma^{-1}X).
\tag{8.1}
\]

This remains integral, nested, commonly owned, and balanced at every depth.

### Proposition 7 (orbit-average misalignment)

For uniform `sigma` and every fixed owner `X`,

\[
 \Pr(P_q^\sigma(X)=\Gamma_q^F(X))=\binom mq^{-1}.
\tag{8.2}
\]

Consequently,

\[
 \boxed{
 \mathbb E_\sigma e_q(F,P^\sigma)
 =W\left(1-\binom mq^{-1}\right).
 }
\tag{8.3}
\]

On a fixed window `H=ceil(A sqrt(m))`, some balanced relabeling has weighted
alignment cost `Theta_A(W sqrt(m))`, essentially the maximum possible.

### Proof

Conditional on `Y=sigma^(-1)X`, the restriction of `sigma` from `Y` to `X`
is a uniformly random bijection.  The fixed `(m-q)`-subset `P_q(Y)` is
therefore sent uniformly to one of the `binom(m,q)` subsets of `X` of that
size.  This proves (8.2), and summing over `X` proves (8.3).  QED.

This does not rule out choosing a special balanced resolution jointly with
`F`.  It proves that the lower-bounded-flow theorem, without a new
alignment selection principle, contains no hidden synchronization.

## 9. Exact sparse owner-trade formulation

For an owner `X` and a permutation `rho in S_m`, let

\[
 P_q^{X,\rho}
 =X\setminus\{a_{\rho(1)}(X),\ldots,a_{\rho(q)}(X)\}
\]

and define its multidepth trade vector relative to the forced flag by

\[
 T_{X,\rho}(q,S)
 =1_{\{S=P_q^{X,\rho}\}}-1_{\{S=\Gamma_q(X)\}}.
\tag{9.1}
\]

Its weighted prefix-support cost is

\[
 \kappa_H(X,\rho)
 =\sum_{q=1}^H\frac{1_{\{\rho([q])\ne[q]\}}}{c_q}.
\tag{9.2}
\]

Choosing a balanced nested resolution is exactly choosing one permutation
`rho_X` for every owner so that

\[
 \mu_q(S)+\sum_XT_{X,\rho_X}(q,S)\in\{c_q,c_q+1\}
\tag{9.3}
\]

at every target and depth.  Its synchronization objective is exactly

\[
 \sum_X\kappa_H(X,\rho_X).
\tag{9.4}
\]

Ignoring the support restrictions in (9.1), the minimum amount of rank-`q`
transport is `O_q(F)`.  Therefore every feasible owner-trade selection obeys

\[
 \boxed{
 \sum_X\kappa_H(X,\rho_X)
 \ge\sum_{q=1}^H\frac{O_q(F)}{c_q}.
 }
\tag{9.5}

The difference between the two sides is the exact cyclic/nesting gluing
penalty.  The marked-run theorem asks for a positive integral selection of
the highly structured owner trades (9.1), not merely a balanced aggregate
flow or a signed decomposition of the quota defect.

## Exact remaining marked-run theorem

For every fixed `A`, it would suffice to choose one exact factor `F_m` and
one integral balanced full deletion resolution `P_m` such that

\[
 \boxed{
 \sum_X\sum_i
 \#\bigl(\mathcal R_i(X)\cap[\lceil A\sqrt m\rceil]\bigr)
 =o(W).
 }
\tag{MR_A}
\]

By (3.3), `(MR_A)` is exactly the labelled cyclic-alignment target on the
fixed window.  A possible proof must provide both:

1. corridor expansion/absorption eliminating the Hall deficiencies (7.3);
2. a return mechanism breaking long cycles such as (6.1) into total
   common-prefix excursion area `o(W)`.

The second requirement is not visible in separate rank marginals or in the
one-step shift-defect count.  This is the sharp obstruction exposed by the
marked-run formulation.
