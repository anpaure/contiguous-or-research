# Fixed-core flagged chain/state common base and reset cuts

**Date:** 2026-08-02  
**Lane:** A, integral rotor fusion  
**Status:** exact joint literal formulation, exact invariant fractional orbit
quotient, and exact monotone-reset cuts.  This integrates the K19/K21
fixed-core chainizations without freezing a chain table.  Integral rounding
of the joint system remains open.

## 0. Outcome

The K17 nested-address no-go is a fibre obstruction: it fixes one exact
`24,310`-row chain/owner table and then proves that no one-transition nested
state assignment exists over that table.  It does **not** imply that every
depth-three chain allocation has the same defect.

For K19 and K21, the fixed-core split theorem gives an orbit-symmetric
family from which the chain factor may still be chosen.  On this unfrozen
family, chain allocation and literal state balance can be selected jointly
by one exact configuration master.  The four long flags become a monotone
four-state automaton and short rows are literal reset sockets.

For a fixed core, both configurations and compatible ordered pairs have
only polynomially many orbit types at depth three.  Averaging over the core
stabilizer gives an **exact fractional** orbit quotient.  This is not yet an
integral theorem: a three-resource parity tensor shows that orbit counts and
all marginal equations alone need not lift to a one-copy configuration.
The surviving gate is therefore an integral fixed-core common base, not a
new static chainization or a separately frozen predecessor matching.

## 1. Literal joint configuration master

Let `k=2r+1` be odd.  Let

\[
 \mathcal L=\{S\subseteq[k]:1\leq |S|\leq r\},
 \quad W={k\choose r},\quad \Lambda=|\mathcal L|=2^{k-1}-1. \tag{1.1}
\]

A **decorated depth-three row** `q` consists of

1. a strict chain
   \[
          C_1(q)\subset\cdots\subset C_{\ell(q)}(q)=U(q),
          \qquad 1\leq\ell(q)\leq3,                  \tag{1.2}
   \]
   in `mathcal L`, with `|U(q)|=r`;
2. an owner `T(q)` of rank `r+1` containing `U(q)`;
3. three nonempty source letters
   \[
                         a(q)=(a_1(q),a_2(q),a_3(q))  \tag{1.3}
   \]
   whose union is `U(q)`; and
4. one strict nested contiguous-address flag on which the chain (1.2) is
   realized by interval unions of (1.3).

There are `6,9,4` possible address shapes when the row length is `1,2,3`.
Let `mathcal Q` be any prescribed bank of such rows.  Put a directed arc
`q -> q'` exactly when

\[
 a_2(q)=a_1(q'),\qquad a_3(q)=a_2(q'),
 \qquad a_1(q)\cup U(q')=T(q').                     \tag{1.4}
\]

The last equality says that the discarded outer cell of `q` supplies the
owner increment of the head row `q'`.

### Theorem 1.1 (exact joint chain/state master)

There is a balanced one-copy depth-three factor supported on `mathcal Q`
if and only if there are binary variables

\[
                         y_q,qquad x_{qq'}           \tag{1.5}
\]

with `x_qq'` present only on arcs (1.4), satisfying

\[
\begin{aligned}
 \sum_{q:S\in C(q)}y_q&=1 &&(S\in\mathcal L),\\
 \sum_{q:T(q)=T}y_q&=1 &&(|T|=r+1),\\
 \sum_{p:p\to q}x_{pq}&=y_q &&(q\in\mathcal Q),\\
 \sum_{p:q\to p}x_{qp}&=y_q &&(q\in\mathcal Q).
                                                               \tag{1.6}
\end{aligned}
\]

The selected support has one chronology component if and only if the arcs
with `x=1` form one directed cycle.  Replacing this by at most `c` directed
cycles gives exactly a `c`-component balanced factor.

#### Proof

The first row of (1.6) partitions every lower target, including every
rank-`r` root, into selected chains.  Hence exactly `W` rows are selected.
The second row attaches the `W` distinct owners.  The last two rows give
the unique chosen literal state of every selected row one predecessor and
one successor, and (1.4) makes every transition carry its head owner.
Thus a solution is precisely a balanced decorated factor.

Conversely, record the selected rows and transitions of any such factor.
Target and owner uniqueness give the first two rows of (1.6), and balance
gives the last two.  Components are exactly directed cycles.  \(\square\)

This theorem chooses chains and source states together.  There is no prior
table to which one subsequently tries to attach states.

## 2. Fixed-core orbit form

Fix a core `H` and let `Gamma` be either
`S_H times S_([k]-H)` or the pointwise stabilizer of `H`, as appropriate.
Assume from this point that the prescribed bank `mathcal Q` is
`Gamma`-invariant.  The group acts on lower targets, owners, decorated rows
and compatible ordered pairs.

A row orbit is described by finite data:

* the nested address flag;
* the membership pattern of every core coordinate in the three source
  letters and the owner increment; and
* the numbers of noncore coordinates in each Venn pattern of those sets.

An arc orbit requires the corresponding bounded Venn table for an ordered
pair of rows.  Individual row-orbit labels alone are not enough: equality
of the two retained literal cells is a relational condition.

At depth three the number of involved sets is absolute.  Hence the row and
arc orbit catalogues have size `k^O(1)` for fixed `H`.  They remain
polynomial when a pointwise fixed core has size `O(log k)`, because its
membership patterns contribute only `2^{O(|H|)}` possibilities.

### Theorem 2.1 (exact invariant fractional quotient)

The fractional relaxation of (1.6) is feasible if and only if its
fixed-core orbit system is feasible.  The orbit system has:

1. one variable for each decorated-row orbit and compatible ordered-pair
   orbit;
2. exact target- and owner-orbit incidence equations; and
3. exact incoming and outgoing incidence equations at every row orbit,

with coefficients equal to the corresponding literal orbit-incidence
degrees.

#### Proof

Average a fractional solution of (1.6) over `Gamma`.  Every variable is now
constant on its orbit, and summing the literal equations gives the stated
type equations.

Conversely, spread each orbit variable uniformly over its literal orbit.
Transitivity makes the number of incident configurations or arcs constant
at every literal member of a resource or row orbit.  The orbit-incidence
equations therefore become every literal equation in (1.6).  \(\square\)

Thus the fixed-core type system is not a heuristic marginal model.  It is
the exact quotient of the **fractional** common-base problem.

### Proposition 2.2 (why integral lifting is a separate theorem)

Orbit counts alone do not imply an integral one-copy selection.  Consider
three resource shores `{a1,a2}`, `{b1,b2}`, `{c1,c2}` and four configurations

\[
 (a_1,b_1,c_1),\ (a_1,b_2,c_2),\
 (a_2,b_1,c_2),\ (a_2,b_2,c_1).                     \tag{2.1}
\]

Weighting every configuration by `1/2` covers every resource exactly once,
but no two configurations are disjoint, so no integral exact cover exists.

#### Proof

Each resource appears in exactly two configurations, proving the fractional
claim.  Every pair of configurations shares an `a`, `b`, or `c` resource,
proving the integral no-go.  \(\square\)

This is genuinely orbit-symmetric: identify each subscript with a bit and
let `(u,v) in F_2^2` translate the three bits by `(u,v,u+v)`.  The action is
transitive on the four configurations and on each two-element resource
shore.  The integral orbit total says to choose two configurations; its
invariant literal spread assigns weight `1/2` to all four and covers every
resource once.  Thus even an **integral orbit count** can have no integral
literal lift.

This parity tensor is an abstract warning, not a Boolean K19/K21
counterexample.  A positive Boolean theorem must prove additional
balancedness, a circuit-rounding theorem, or an absorber for the literal
configuration hypergraph.  It may not infer an integral table merely by
spreading a feasible type circulation uniformly.

## 3. Four-flag drift as orbit-linear reset cuts

For a selected length-three row, order its four flags by

\[
                        0=12/1<1=12/2<2=23/2<3=23/3. \tag{3.1}
\]

### Theorem 3.1 (monotone long blocks in the joint master)

In every integral solution of (1.6), a long-to-long selected transition
has nondecreasing flag.  Hence each maximal block of consecutive long rows
is nondecreasing, and an all-long component is flag-constant.

#### Proof

For a decreasing flag pair, equality of the two retained source cells
forces the two rows to share either their bottom named target `C1` or their
second named target `C2`.  The exact-cover row of (1.6) forbids two distinct
selected rows from sharing that target.  The two rows would therefore be
the same decorated chain.  A self-transition is impossible because its
discarded source cell lies inside `U`, while the owner equality in (1.4)
requires it to contain `T-U`.  \(\square\)

Let `S` be the selected short rows, and for `t=1,2,3` let `A_t` be the
selected long rows of flag at least `t`.  Flow conservation and Theorem 3.1
give the exact identity

\[
 x(L_{<t},A_t)+x(S,A_t)=x(A_t,S),                    \tag{3.2}
\]

where `L_<t` is the set of long rows below flag `t`.  In particular

\[
              x(L_{<t},A_t)\le |S|\qquad(t=1,2,3),   \tag{3.3}
\]

and

\[
 \sum_{\substack{q\to q'\\q,q'\text{ long}}}
          (\operatorname{flag}(q')-\operatorname{flag}(q))x_{qq'}
       \le 3|S|.                                     \tag{3.4}
\]

These are linear fixed-core orbit cuts: group arc orbits by their two flag
levels and short/long roles.  They express the exact reset burden without
freezing which physical chains are short.

There is a sharper three-threshold form.  Put

\[
 D_t=x(\{\hbox{long flag}\le t\},
       \{\hbox{long flag}>t\})\qquad(t=0,1,2),        \tag{3.5}
\]

and let `b=x(S,L)=x(L,S)` be the number of maximal short blocks meeting a
long block.  Define

\[
 \rho(D)=D_0+(D_1-D_0)_+ +(D_2-D_1)_+
        =\max\{D_0,D_1,D_2,D_0+D_2-D_1\}.            \tag{3.6}
\]

### Theorem 3.2 (sharp short-block reset cut)

Every integral solution of (1.6) satisfies

\[
                         \boxed{\rho(D)\le b\le |S|}. \tag{3.7}
\]

#### Proof

Delete the short blocks from each directed cycle.  Every remaining long
block is nondecreasing, so the set of thresholds it crosses is one interval
of the three-edge path `0--1--2--3` (possibly empty).  Thus the load vector
`(D0,D1,D2)` is a sum of at most `b` interval incidence vectors.

For a three-edge path the minimum number of intervals having edge loads
`(D0,D1,D2)` is exactly (3.6): start `D0` intervals at the first edge; start
another `(D1-D0)_+` at the second and `(D2-D1)_+` at the third, while
continuing as many earlier intervals as possible.  This constructs the
decomposition and proves its optimality at every left boundary.  Hence
`rho(D)<=b`.  Each maximal short block contains a selected short row, so
`b<=|S|`.  \(\square\)

Equivalently, (3.7) is the four linear orbit-cut family

\[
 D_0\le b,\quad D_1\le b,\quad D_2\le b,
 \quad D_0+D_2-D_1\le b.                             \tag{3.8}
\]

## 4. K19 and K21 calibration

For any depth-three anchored factor, let `n_l` be the number of rows of
length `l`.  Then

\[
 n_1+n_2+n_3=W,qquad n_1+2n_2+3n_3=\Lambda,         \tag{4.1}
\]

so

\[
                   2n_1+n_2=E:=3W-\Lambda.           \tag{4.2}
\]

The number `N_short=n1+n2` of selected short rows, hence the raw reset-row
budget, therefore obeys

\[
                  \left\lceil{E\over2}\right\rceil
                  \le N_{\rm short}\le E.           \tag{4.3}
\]

For the three calibrated dimensions, the unrestricted scalar ranges are

\[
\begin{array}{c|r|r|r|c}
k&W&\Lambda&E&N_{\rm short}\text{ range}\\ \hline
17&24310&65535&7395&3698\ldots7395\\
19&92378&262143&14991&7496\ldots14991\\
21&352716&1048575&9573&4787\ldots9573.
\end{array}                                           \tag{4.4}
\]

The frozen K17 table chose `(n1,n2,n3)=(1748,3899,18663)`, hence `5,647`
short rows, yet its complete nested union projection is still deficient by
`484`.  That is a failure of one fibre, not a scalar shortage of resets.

The fixed K19/K21 three-block chronologies impose a much sharper ledger.
Let the bottom, middle and top block sizes be `a,b,W`, and let `x=n3` be
the number of chains meeting all three blocks.  Every bottom or middle
target lies in a row ending at one top target, so

\[
\begin{aligned}
 n_3&=x,\\
 n_2&=a+b-2x,\\
 n_1&=W-a-b+x,\\
 N_{\rm short}&=W-x,
 \qquad a+b-W\le x\le b.                            \tag{4.5}
\end{aligned}
\]

(Here `a>=b`, as in both fixed-core splits.)  Therefore

\[
                       W-b\le N_{\rm short}
                       \le 2W-a-b.                   \tag{4.6}
\]

For K19 this is

\[
 14976\le N_{\rm short}\le14991,                    \tag{4.7}
\]

with the minimum-short-row profile `(n1,n2,n3)=(15,14961,77402)`.  For K21,

\[
 8736\le N_{\rm short}\le9573,                      \tag{4.8}
\]

with minimum-short-row profile `(837,7899,343980)`.  These are necessary
ranges; the Dilworth proof does not assert that either endpoint profile is
attained.  The joint master itself chooses `x`.  The actual reset-block
capacity is `b` from (3.7), which can be strictly smaller than `N_short`
when short rows are consecutive or form a short-only cycle.

For K19 use the fixed-triple blocks `P0,P1,P2`; for K21 use the fixed-core
blocks `A,B,C` from
`MATH_THEOREM_K19_K21_FIXED_CORE_NORMAL_SPLITS_AND_ALLK_ORBIT_TRANSPORT_GATE_20260802.md`.
Restrict `mathcal Q` in Theorem 1.1 to chains whose named targets advance in
those block orders, allow skipped blocks as in the global orbit-Hall lift,
and attach all `6/9/4` nested flags.  The resulting configuration bank is
fixed-core invariant, so Theorems 2.1 and 3.1 apply verbatim.

The static resource projection of this joint master is feasible by the
K19/K21 chainization theorem.  Local nested states also exist for every
strict chain: use its nonempty successive increments, distributing surplus
root coordinates inside the selected interval flag.  What remains unknown
is whether one common integral selection also satisfies the transition
rows of (1.6).  Equations (3.2)--(3.4) are necessary cuts for that selection,
not an existence proof.

## 5. Exact next gate

The K19/K21 fixed-core result should therefore be used in the following
order.

1. Build the fixed-core decorated-row and relational arc orbits.
2. Solve the joint target/owner/state master, not a static table followed by
   a predecessor matching.
3. Enforce the three reset cuts (3.2), or equivalently carry the four-state
   monotone automaton in the orbit flow.
4. Prove an integral common-base/absorber theorem for the Boolean
   configuration hypergraph.

Only after Step 4 is there a balanced literal factor.  Connected topology
adds one-cycle/subtour cuts.  Residence histories, arbitrary-width upper
witnesses, endpoint aperture, source factorability, common cap and compiler
remain downstream and are not implied here.

The important separation is now exact:

* static chain allocation at K19/K21 is solved;
* the frozen K17 nested-address fibre is impossible;
* the fixed-core invariant fractional joint system is polynomial and exact;
* its integral Boolean common-base rounding is the live gate.
