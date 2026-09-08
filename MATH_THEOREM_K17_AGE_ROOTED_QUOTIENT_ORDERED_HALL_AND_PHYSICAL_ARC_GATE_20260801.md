# `k=17`: the exact age-rooted quotient port graph and its ordered-Hall obstruction

Date: 2026-08-01  
Lane: one certified age type per `Z_17` owner orbit  
Status: unconditional finite min--max theorem.  It does not assert that the
required labelled state, nonzero-voltage cycle, or upper-safe opening exists.

## 0. Verdict

The certified circulation on the nine age **types** is not a circulation on
the 1430 physical owner orbits.  Its Euler circuit supplies only a cyclic
type word.  Before an owner-level arc may be used, one must choose a single
labelled age partition on each owner orbit and verify the literal Johnson
exchange between those two chosen partitions.  Different incident type arcs
cannot silently use different partitions of the same owner.

After those choices are frozen, there is an exact ordered-Hall theorem.  Fix
a legal physical quotient arc `a_*:z->r` as the closing/root arc.  For every
rooted total order

\[
                 r=O_1\prec O_2\prec\cdots\prec O_N=z,
                 \qquad N=1430,                       \tag{0.1}
\]

whose adjacent type counts, together with `a_*`, equal the certified
16-entry transition ledger, retain only forward legal physical arcs.  Split
each owner orbit into a tail and a head copy and let `B_(sigma,prec)` be the
resulting bipartite graph.  Put

\[
 \delta_\sigma(\prec)=
 \max_{X\subseteq\mathcal O_L}
       \bigl(|X|-|N_{B_{\sigma,\prec}}(X)|\bigr).      \tag{0.2}
\]

Then the fixed root arc extends to a typed quotient Hamilton cycle if and
only if

\[
                         \min_\prec\delta_\sigma(\prec)=1.  \tag{0.3}
\]

Thus the exact topological failure certificate is either an empty admissible
state/order family, or, for every state and every compatible order, a set
`X` with

\[
             |N_{B_{\sigma,\prec}}(X)|\le |X|-2.       \tag{0.4}
\]

Equation (0.3) certifies a physical **support** cycle.  Three further rows
remain separate and literal:

1. its parallel quotient arcs must admit labels whose total voltage is
   nonzero modulo 17;
2. the labelled suffixes must give the required rank-`2,...,8` target-orbit
   bijections; and
3. the chosen physical opening must retain all strict-upper witnesses.

The age certificate supplies the correct numbers for these rows, but not
their simultaneous realization.

## 1. The fixed type ledger

Let `G=<rho>=Z_17` act by coordinate rotation.  Since the action is free on
proper nonempty subsets, the rank-9 owner-orbit set

\[
       \mathcal O={ [17]\choose9}/G
\]

has

\[
                    N=|\mathcal O|={1\over17}{17\choose9}=1430. \tag{1.1}
\]

The certified age types and their required owner-orbit multiplicities are

| type `c=(c_0,c_1,c_2,c_3)` | `m(c)` |
|---|---:|
| `(1,5,2,1)` | 139 |
| `(1,6,1,1)` | 297 |
| `(2,5,1,1)` | 8 |
| `(3,3,2,1)` | 20 |
| `(3,4,1,1)` | 20 |
| `(4,3,1,1)` | 140 |
| `(5,1,2,1)` | 127 |
| `(5,2,1,1)` | 237 |
| `(6,1,1,1)` | 442 |

Write `f(c,c')` for the following 16 nonzero transition counts:

```text
(1,5,2,1) -> (6,1,1,1) : 139

(1,6,1,1) -> (5,1,2,1) : 127
(1,6,1,1) -> (6,1,1,1) : 170

(2,5,1,1) -> (6,1,1,1) :   8
(3,3,2,1) -> (5,2,1,1) :  20
(3,4,1,1) -> (3,3,2,1) :  20
(4,3,1,1) -> (4,3,1,1) : 139
(4,3,1,1) -> (6,1,1,1) :   1

(5,1,2,1) -> (2,5,1,1) :   8
(5,1,2,1) -> (5,2,1,1) : 119

(5,2,1,1) -> (1,5,2,1) : 139
(5,2,1,1) -> (5,2,1,1) :  98

(6,1,1,1) -> (1,6,1,1) : 297
(6,1,1,1) -> (3,4,1,1) :  20
(6,1,1,1) -> (4,3,1,1) :   1
(6,1,1,1) -> (6,1,1,1) : 124
```

Its row and column sums both equal `m`.  Its positive type support is
weakly connected, so an abstract Euler circuit exists.  This fact concerns
1430 **type occurrences** only.

## 2. Exact labelled owner states

Fix once and for all one representative `T_O` of each owner orbit
`O in \mathcal O`.  Changing these representatives only changes the voltage
gauge.

An **age-labelled owner state** consists first of the following data.

1. A type assignment

   \[
      \tau:\mathcal O\longrightarrow\mathcal C,
      \qquad |\tau^{-1}(c)|=m(c).                     \tag{2.1}
   \]

2. For every `O`, one labelled partition of its fixed representative,

   \[
       P_O=(C_{O,0},C_{O,1},C_{O,2},C_{O,3}),
       \quad T_O=\mathbin{\dot\bigcup}_{i=0}^3 C_{O,i},
       \quad |C_{O,i}|=\tau(O)_i.                    \tag{2.2}
   \]

   In particular `C_(O,3)={alpha_O}` is a literal singleton.

3. Any fixed boundary macro, forbidden-resource, provider, or compiler data
   that are intended to restrict quotient arcs.  A non-edge-local condition
   is recorded as a predicate on the eventual full order and arc labelling;
   it is not projected to a pairwise arc without proof.

For an available suffix rank

\[
 R(\tau(O))=
 \{c_0,c_0+c_1,c_0+c_1+c_2\}\cap[1,8],               \tag{2.3}
\]

let

\[
 S_{O,s}=C_{O,0}\cup\cdots\cup C_{O,j-1}
 \quad\hbox{when }s=c_0+\cdots+c_{j-1}.              \tag{2.4}
\]

The state is **lower-exact** if, for each `2<=s<=8`,

\[
 O\longmapsto [S_{O,s}]_G
 \quad\text{from }\{O:s\in R(\tau(O))\}
 \text{ to }{[17]\choose s}/G                       \tag{2.5}
\]

is a bijection.  The certified capacity equalities show that the two sets
in (2.5) have the same cardinality.  They do not prove injectivity.

## 3. The physical voltage-labelled quotient port graph

For two distinct owner orbits `O,O'` and `v in Z_17`, put

\[
                    T'=\rho^vT_{O'},
        \qquad C'_i=\rho^v C_{O',i}.                  \tag{3.1}
\]

There is a physical labelled quotient arc

\[
                         a=(O,O',v)                   \tag{3.2}
\]

when all of the following hold.

1. `T_O` and `T'` are Johnson adjacent and the deleted coordinate is the
   unique oldest coordinate:

   \[
       T'=T_O-\{\alpha_O\}+\{\beta\}                 \tag{3.3}
   \]

   for the unique `beta in T'-T_O`.

2. The one already chosen partition at `O'`, in the gauge (3.1), is the
   literal age update of the one already chosen partition at `O`:

   \[
        C'_{i+1}\subseteq C_{O,i}\quad(0\le i<3),     \tag{3.4}
   \]

   \[
        C'_0=\{\beta\}\mathbin{\dot\cup}
             \mathbin{\dot\bigcup}_{i=0}^{2}
                    (C_{O,i}-C'_{i+1}).               \tag{3.5}
   \]

3. The arc passes every frozen edge-local physical guard in the state.

Let `A_sigma` be this voltage-labelled directed multigraph.  Parallel arcs,
including distinct voltages between the same ordered pair, are retained.
Loops on owner orbits are excluded because a Hamilton cycle on 1430
distinct quotient vertices does not use them.

This is also the required vertex-consistency condition.  If a lifted walk
reaches `O` in phase `g`, its incoming arc ends at `rho^g P_O`; rotating any
outgoing arc of (3.2) by the same `g` starts at that identical partition.
Thus incoming and outgoing transitions concatenate literally.

Equations (3.3)--(3.5), rather than the inequalities
`c'_(i+1)<=c_i`, are the physical arc test.  They also show that the rank-8
lower colour of every outgoing arc from `O` is

\[
       [T_O\cap T']_G=[T_O-\{\alpha_O\}]_G
                     =[S_{O,8}]_G.                   \tag{3.6}
\]

Consequently a lower-exact state makes the selected rank-8 quotient edges
rainbow automatically.  No analogous conclusion follows from the type of
`O` alone.

The **support port digraph** `D_sigma` forgets the labels of `A_sigma` but
keeps an arc `O->O'` exactly when at least one labelled arc (3.2) exists.
This forgetting is used only for the Hall topology test.  Labels are
restored in Section 6.

## 4. Rooting at a physical closing arc

Choose a labelled arc

\[
                 a_*=(z,r,v_*)\in A_\sigma           \tag{4.1}
\]

and regard it as the closing arc across the intended quotient cut.  A total
order `prec=(O_1,...,O_N)` is **`(sigma,a_*,f)`-admissible** when

\[
                         O_1=r,\qquad O_N=z,           \tag{4.2}
\]

and, for every pair of certified types `(c,c')`,

\[
 \#\{i<N:(\tau(O_i),\tau(O_{i+1}))=(c,c')\}
 =f(c,c')-
   \mathbf1_{(\tau(z),\tau(r))=(c,c')}.              \tag{4.3}
\]

Any authenticated boundary-macro order predicate may be added to this
definition.  In particular the physical root port must really be the free
head and the terminal port the free tail; merely naming two vertices does
not prove this.

Write `Pi(sigma,a_*,f)` for these orders.  The abstract Euler circuit in the
nine-type multigraph shows that some cyclic **type word** has counts `f`.
It does not show that `Pi(sigma,a_*,f)` is nonempty for a prescribed root,
nor that any such order has physical support arcs.

For `prec in Pi(sigma,a_*,f)`, retain the arcs `O->O'` of `D_sigma` with
`O prec O'`.  Split every owner orbit into a left tail copy and a right head
copy.  The corresponding bipartite graph is

\[
 B_{\sigma,a_*,\prec}=(\mathcal O_L,\mathcal O_R;E_\prec). \tag{4.4}
\]

The right copies are independent copies: placing `O_L` in a Hall set does
not remove `O_R` from its neighbourhood.

## 5. Exact ordered-Hall min--max

### Theorem 5.1 (fixed-state rooted typed cycle theorem)

For a fixed state `sigma` and fixed closing arc `a_*`, the following are
equivalent.

1. There is a quotient Hamilton cycle containing `a_*`, using physical
   support arcs from `D_sigma`, rooted immediately after `a_*`, and having
   exactly the transition counts `f`.
2. There is an order `prec in Pi(sigma,a_*,f)` such that

   \[
       \max_{X\subseteq\mathcal O_L}
       \bigl(|X|-|N_{B_{\sigma,a_*,\prec}}(X)|\bigr)=1. \tag{5.1}
   \]

Equivalently, if the minimum over an empty order family is `+infinity`, the
exact fixed-state obstruction number is

\[
 \boxed{
 \Delta(\sigma,a_*;f)=
 \min_{\prec\in\Pi(\sigma,a_*,f)}
 \max_{X\subseteq\mathcal O_L}
       (|X|-|N_{B_{\sigma,a_*,\prec}}(X)|).}          \tag{5.2}
\]

The rooted typed physical-support cycle exists exactly when
`Delta(sigma,a_*;f)=1`.

#### Proof

Fix `prec`.  By the bipartite deficiency form of Hall's theorem, the maximum
matching size in (4.4) is

\[
 N-max_X(|X|-|N(X)|).                                \tag{5.3}
\]

All retained arcs increase `prec`, so a matching selects a directed path
forest: each vertex has at most one selected outgoing and incoming arc and
no directed cycle is possible.  A matching of size `N-1` therefore has one
path component and spans all `N` vertices.  Its path order must be exactly
`O_1,...,O_N`, because every selected arc increases the total order.  Adding
`a_*:O_N->O_1` gives the required Hamilton cycle, and (4.3) gives its exact
type-transition counts.

Conversely, delete `a_*` from such a rooted Hamilton cycle and order its
vertices along the resulting Hamilton path.  Its `N-1` arcs form a matching
in (4.4), so the deficiency is at most one.  It is at least one because the
first right copy has no forward predecessor (equivalently no acyclic
forward graph has a perfect matching).  Hence it equals one. `square`

### Corollary 5.2 (global cut alternative)

Let `Sigma_age` be any declared family of exact labelled states, including
all fixed boundary and resource conditions.  Exactly one of the following
holds at the physical-support topology level.

1. Some `sigma in Sigma_age`, some labelled root arc `a_*`, and some
   admissible order extend to a rooted typed quotient Hamilton cycle.
2. Either the state/root/order family is empty, or for every such triple
   there is a Hall set `X` with

   \[
             |N_{B_{\sigma,a_*,\prec}}(X)|\le |X|-2. \tag{5.4}
   \]

Thus (5.4) is the minimal cut obstruction after the exact physical state is
fixed.  A cut in the nine-vertex type graph is neither necessary nor
sufficient for this owner-level alternative.

## 6. Parallel labels, voltage, and literal completion gates

Condition (5.1) forces the support edges between each consecutive pair
`O_i,O_(i+1)`.  Let

\[
 V_i=\{v\in Z_{17}:(O_i,O_{i+1},v)\in A_\sigma\}
 \qquad(1\le i<N),                                   \tag{6.1}
\]

after any edge-local guards.  A nonzero-voltage labelling exists exactly
when

\[
 \bigl(v_*+V_1+\cdots+V_{N-1}\bigr)\setminus\{0\}
 \ne\varnothing.                                     \tag{6.2}
\]

If labels share a bank or another global resource, (6.2) is replaced by
the same condition over the jointly admissible label tuples; independent
sumsets must not be assumed.

Under (6.2), choose labels with total voltage `h\ne0`.  Starting with the
fixed representative of `O_1`, one quotient traversal changes the rotation
phase by `h`.  Since 17 is prime, translation by `h` is a 17-cycle on the
phases.  The voltage lift is therefore one physical cycle on

\[
                         17\cdot1430=24310             \tag{6.3}
\]

owners.  If `h=0`, it is instead 17 disjoint quotient-length cycles.  Hall
support alone cannot distinguish these cases.

Together with literal age conditions (3.3)--(3.5), a lower-exact state and
nonzero voltage give the one-copy owner cycle, residence, and the rank-2
through rank-8 quotient rainbows required by the age reduction.  To infer
the optimal linear word one must still choose a physical cut for which all
rank-10 through rank-17 targets have nonwrapping owner-interval witnesses.
This **upper-safe opening** is a predicate of the fully labelled lifted
cycle and its cut.  It is not an edge-local property of `D_sigma` and is not
proved by (5.1).

### Theorem 6.1 (sufficient finite certificate)

Suppose there are `sigma`, `a_*`, and `prec` such that:

1. `sigma` is lower-exact;
2. `prec in Pi(sigma,a_*,f)` and (5.1) holds;
3. the consecutive support arcs admit a jointly legal choice satisfying
   (6.2); and
4. the resulting physical lift has an upper-safe opening at the declared
   root (including any protected boundary-macro socket and provider rows).

Then the certificate-decorated quotient cycle of
`MATH_REDUCTION_K17_CATALAN_ORBIT_AGE_DECORATED_RAINBOW_CYCLE_20260801.md`
exists.  Consequently `nu(17)=24313`.

This theorem is sufficient, not an existence assertion: none of items
1--4 is inferred merely from the stationary type masses.

## 7. Why type arc counts do not align automatically

The invalid quantifier swap is

\[
 \bigl[\text{choose a type Euler circuit}\bigr]
 \quad\Longrightarrow\quad
 \bigl[\text{infer physical arcs between arbitrary owners in its slots}\bigr].
                                                               \tag{7.1}
\]

The type condition

\[
                         c'_{i+1}\le c_i              \tag{7.2}
\]

says only that **some** survivor choice exists between abstract partitions
of those sizes.  It does not say that the already chosen partitions
`P_O,P_(O')` satisfy (3.3)--(3.5), or even that some rotation of the named
owners is Johnson adjacent.

Nor are aggregate block counts enough.  Two available `c->c'` arcs may
share the same physical tail owner, while a second owner assigned type `c`
has no legal successor.  Raw inequalities such as

\[
                  |A_\sigma(c,c')|\ge f(c,c')        \tag{7.3}
\]

do not provide distinct tails, distinct heads, or one globally compatible
order.  In a rooted order the terminal owner is already the one allowed
unmatched tail; any second forced dead tail appears with it in a deficiency-
two Hall set.  This is exactly the concentration detected by (5.4).

There is a second, subtler incompatibility.  If arcs are generated by
allowing a fresh witness partition separately for every ordered owner pair,
an incoming arc at `O` and an outgoing arc at `O` may use different
partitions of `T_O`.  Such a pair does not concatenate to a source trace.
The single partition choice (2.2) must therefore precede construction of
`A_sigma`.

## 8. Quantifier audit

The valid existence order is

\[
\begin{aligned}
 &\exists\ \tau
 \ \exists\ (P_O)_{O\in\mathcal O}
 \ \exists\ \text{frozen boundary/resource state} \\
 &\quad \exists\ a_*\in A_\sigma
 \ \exists\ \prec\in\Pi(\sigma,a_*,f)
 \ \forall X\subseteq\mathcal O_L \\
 &\qquad |N_{B_{\sigma,a_*,\prec}}(X)|\ge |X|-1,    \tag{8.1}\\
 &\quad \exists\ \text{joint parallel-arc labels with nonzero voltage}
 \ \exists\ \text{an upper-safe physical opening}.
\end{aligned}
\]

The lower-exact bijections (2.5) are predicates on the partition choice in
the first line.  Hall's theorem converts the universal cut line to the
existence of the unique-order Hamilton connector, but it does not commute
the first line past the cut test and it does not imply either existential in
the last line.

In particular, the following weaker statements cannot replace (8.1):

* the 16-entry type ledger is balanced and connected;
* every displayed type transition has a nonempty abstract survivor relation;
* every owner orbit admits at least one partition of its assigned type;
* every type block contains at least as many physical arcs as its required
  transition multiplicity; or
* the unlabelled physical quotient support is connected.

The exact finite target is the 1430-vertex labelled state above, followed by
its ordered-Hall cut system and the two genuinely global gates in Section 6.
