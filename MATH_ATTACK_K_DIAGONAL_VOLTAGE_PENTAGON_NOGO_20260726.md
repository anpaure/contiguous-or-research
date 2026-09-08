# The diagonal-voltage pentagon lift is not literal

## Exact product-resource rigidity and the action--fragmentation bound

### Scope

This note concerns the once-suspended five-row pentagon packet and its
literal tensor over `k` pairwise disjoint marked fringe slots.  The two
local shores are denoted by `F^-` and `F^+`.  Every physical `X/Y`
resource, every root port, every slot carrier, and every exterior context
is retained pointwise.  Thus this is not a quotient ledger in which two
different slot/context occurrences are declared to have the same colour.

The conclusion is statewise.  It applies to every integral hybrid made
from the two local row catalogues, including correlated hybrids.  It does
not assume that the line choices are independent or translation
invariant.

The main conclusion is:

> A diagonal order-five voltage cannot carry pentagon changes in two
> distinct slots.  More generally, if a fraction `f` of all local
> slot-fibres is changed, then the size-biased overlay component moment
> satisfies
> \[
>                         \chi\ge 5^{fk}.
> \]
> Consequently bounded `chi` forces the fraction of available tagged
> pentagon action to be `O(1/k)`.

This closes the proposed diagonal/voltage escape within the literal
product-resource architecture.  Forgetting context colours produces a
small quotient graph, but that quotient is not an exact factor on the
original physical resources.

## 1. The local edge-coloured resource graph

Let

\[
                         \Omega=\mathbb Z/5\mathbb Z
\]

index the five roots in the suspended pentagon packet.  Let
`mathcal R` be its complete local owned-resource set, including the
`X`- and `Y`-resources and the rooted ports.  The two local factors give
owner maps

\[
                  o^-,o^+:\mathcal R\longrightarrow\Omega.
\]

Define the edge-coloured bipartite graph

\[
 \mathcal B=(\Omega^-\sqcup\Omega^+,E),
 \qquad
 e_t=\bigl(o^-(t)^-,o^+(t)^+\bigr),\quad t\in\mathcal R,       \tag{1.1}
\]

where the edge has its physical resource `t` as colour.  The rooted port
at root `a` gives a diagonal edge `a^-a^+`.  Contract these five diagonal
port edges.  The resulting multigraph on `Omega` is connected; indeed the
wrapped owner routing contains a five-cycle.  Label `Omega` around one
such cycle.  Its successive edges then have displacement `+1` in
`Z_5` (up to reversing the labelling).

The fact used below is connectedness, not the absence of additional
edges.

### Lemma 1.1 (Boolean ownership equation)

Suppose a hybrid chooses the minus row at root `a` when `b(a)=0` and the
plus row when `b(a)=1`.  Exact ownership of the resource `t` is equivalent
to

\[
                         b(o^-(t))=b(o^+(t)).                    \tag{1.2}
\]

Consequently every exact hybrid of the two local catalogues is constant
on every connected component of the port-closed graph `mathcal B`.

#### Proof

The resource `t` occurs in the minus catalogue only in its owner row
`o^-(t)` and in the plus catalogue only in its owner row `o^+(t)`.  Its
number of occurrences in the hybrid is

\[
                       (1-b(o^-(t)))+b(o^+(t)).
\]

This equals one if and only if (1.2) holds.  Apply this equality along
every edge.  \(\square\)

For the pentagon, connectedness makes the local Boolean state constant on
all five roots.  There is no proper local two-shore subtrade.

## 2. The literal `k`-slot product atlas

Fix a skeleton with `k` marked suspended-pentagon slots.  Its root set is

\[
                         V=\Omega^k=\mathbb F_5^k.                \tag{2.1}
\]

For a slot `h in [k]` and an exterior tuple
`z in Omega^([k] setminus {h})`, put

\[
 L_{h,z}=\{x\in V:x_{\widehat h}=z\}.                            \tag{2.2}
\]

This is an axis-parallel five-point line.  Write
`iota_(h,z)(a)` for its point with `h`-coordinate `a`.

Every local resource `t` in slot `h` and context `z` has a distinct
literal product colour

\[
                         [h,z,t].                                \tag{2.3}
\]

Its two owners are exactly

\[
 \iota_{h,z}(o^-(t))
       \quad\hbox{and}\quad
 \iota_{h,z}(o^+(t)).                                            \tag{2.4}
\]

The colour in (2.3) is not bookkeeping added after the fact.  The marked
slots lie on disjoint physical coordinate carriers.  An internal global
`X` token has exactly one carrier restriction which is neither a root port
nor a complementary port; that restriction locates `h` and identifies
the local `X` token.  An internal global `Y` token has exactly one carrier
restriction of the local upper rank, which likewise locates `h` and its
local `Y` token.  On every other carrier the restriction is a root or
complement port, and the rooted five-row catalogue makes these spectator
restrictions injective in the exterior filling.  Therefore equality of
physical product resources forces equality of `h`, `z`, and `t`.
Boundary connector tokens are common identity resources and only add
diagonal edges.  This is the same context-separation property under which
the unary substitutions in the tensor construction have disjoint token
ledgers and commute.

### Theorem 2.1 (one-coordinate voltage rigidity)

After the row labels (2.1) are used, every edge of colour `[h,z,t]` has
displacement

\[
                    (o^+(t)-o^-(t))e_h.                          \tag{2.5}
\]

In particular it fixes every coordinate other than `h`.  The five-cycle
inside the local overlay lifts on every line `L_(h,z)` to a coordinate
five-cycle.  Hence that entire line lies in one overlay component whenever
the local pentagon packet is active there.

#### Proof

Formula (2.4) gives (2.5).  Lifting the connected local resource graph by
`iota_(h,z)` gives a connected graph on all five points of the line.
\(\square\)

### Corollary 2.2 (the full tensor component)

If the pentagon is active in every slot and exterior context, the
contracted overlay is connected on all `5^k` roots.  Thus its unique
nontrivial component has `5^k` rows on each shore.

#### Proof

The lifted local five-cycles supply every coordinate translation `e_h`
through every point.  These translations generate `F_5^k`. \(\square\)

There is an equally direct Boolean formulation.  Let `b(x)` select a
shore at root `x`.  Lemma 1.1 on every active line says

\[
                 b(x)=b(x+e_h)\qquad(x\in V, h\in[k]).          \tag{2.6}
\]

The only solution of all equations (2.6) is a constant.

## 3. Classification of diagonal subgroups and group quotients

The proposed diagonal lift asks that a common voltage vector
`v in F_5^k` generate a component

\[
                         x+\langle v\rangle                           \tag{3.1}
\]

of size at most five, while the same orbit carries local changes in many
slots.

### Theorem 3.1 (diagonal subgroup obstruction)

Let `D<=F_5^k` be a subgroup whose cosets are intended to contain all
resource edges in a set `I` of active slot directions.  Then

\[
                         e_h\in D\qquad(h\in I)                    \tag{3.2}
\]

and therefore

\[
                         |D|\ge5^{|I|}.                            \tag{3.3}
\]

In particular an order-five diagonal subgroup can support at most one
slot direction.  It cannot support two slots, much less `Theta(k)` slots.

#### Proof

For every active `h`, a lifted local five-cycle contains two roots whose
difference is a nonzero multiple of `e_h`.  If both lie in one `D`-coset,
then that multiple, and hence `e_h`, lies in `D`.  The vectors
`{e_h:h in I}` are linearly independent over `F_5`, proving (3.3).
\(\square\)

The conclusion is unchanged for cyclic or nonabelian voltage notation.
Every literal component has a projection to the physical root tuples in
`F_5^k`.  The projected path group contains the independent coordinate
translations in (3.2), so the component has at least as many vertices as
their `5^|I|`-point orbit.  An auxiliary sheet voltage can enlarge or merge
this orbit; it cannot collapse distinct physical roots in it.

### Proposition 3.2 (why a subdirect quotient is spurious)

Let

\[
             \pi:\mathbb F_5^k\longrightarrow Q                \tag{3.4}
\]

be a group quotient.  It is possible algebraically to arrange, for
example, `pi(e_1)=...=pi(e_k)=g` with `g` of order five.  The quotient
graph then displays one diagonal-looking five-cycle.  It is not a literal
resource overlay unless `pi` is injective.

Indeed, if `pi(x)=pi(y)` with `x ne y`, the quotient identifies the two
distinct root-port colours `P_x` and `P_y`, as well as their distinct
context-labelled resources.  If those colours are restored, the vertices
in `ker pi` are restored too, and the lifted coordinate translations
again generate `F_5^k`.  A quotient can hide the large component but cannot
fragment it.

The special sum map

\[
            \pi(x_1,\ldots,x_k)=x_1+\cdots+x_k                 \tag{3.5}
\]

is the cleanest example: all coordinate steps project to `+1`, but each
quotient vertex represents `5^(k-1)` distinct rooted rows.  Those rows
cannot be identified in an exact factor.

### Explicit diagonal failure

The five diagonal roots

\[
                     (a,a,\ldots,a),\qquad a\in\mathbb F_5,    \tag{3.6}
\]

do not form a legal packet.  In slot `h`, the old local owner `a` is
matched by the new local owner whose tuple is

\[
                 (a,\ldots,a,a+1,a,\ldots,a),                  \tag{3.7}
\]

not by `(a+1,...,a+1)`.  The latter changes the restrictions on every
spectator carrier, so it does not own the same physical resource.

## 4. Arbitrary correlated line choices

Translation invariance is unnecessary.  Let `mathscr L` be any family of
active axis-parallel five-point lines.  Choices may depend arbitrarily on
the complete exterior tuple.  Let

\[
                          L=|\mathscr L|.                          \tag{4.1}
\]

Let `C_1,...,C_J` be the row sets of the resulting port-closed overlay
components after the diagonal root edges are contracted, and put

\[
 N=5^k,qquad s_j=|C_j|,qquad
 \chi={1\over N}\sum_{j=1}^J s_j^2.                              \tag{4.2}
\]

Every active line belongs wholly to one `C_j` by Theorem 2.1.

### Lemma 4.1 (five-ary full-line isoperimetry)

For every `C subseteq F_5^k`, the number `ell(C)` of axis-parallel
five-point lines wholly contained in `C` satisfies

\[
                       \ell(C)\le {|C|\log_5|C|\over5}.          \tag{4.3}
\]

#### Proof

Induct on `k`.  Split `C` into its five slices in the last coordinate,
with sizes `n_0,...,n_4`, total `n`, and let

\[
             t=\left|\bigcap_{a=0}^4 C_a\right|.
\]

The lines in the first `k-1` directions lie inside the slices and the
last-direction lines are counted by `t`.  The induction hypothesis gives

\[
 5\ell(C)\le\sum_{a=0}^4n_a\log_5n_a+5t.                         \tag{4.4}
\]

Put `p_a=n_a/n` and `p_min=min p_a`.  Since `t<=np_min`, it is enough to
use

\[
             H_5(p):=-\sum_ap_a\log_5p_a\ge5p_{\min}.           \tag{4.5}
\]

For fixed `p_min=u`, entropy is minimized at
`(1-4u,u,u,u,u)` up to permutation.  Along `0<=u<=1/5`, its entropy minus
`5u` is concave and is zero at both endpoints, proving (4.5).  Substituting
it in (4.4) yields `5ell(C)<=n log_5 n`. \(\square\)

Coordinate subcubes attain equality in (4.3), so the constant is exact.

### Theorem 4.2 (statewise action--fragmentation inequality)

Let

\[
             f={L\over k5^{k-1}}                                \tag{4.6}
\]

be the fraction of all slot/context lines on which the local pentagon is
active.  Then

\[
                         \boxed{\chi\ge5^{fk}.}                  \tag{4.7}
\]

In particular:

1. if every component has at most `M` rows per shore, then
   \[
                          f\le{\log_5M\over k};                  \tag{4.8}
   \]
2. if `chi=O(1)`, then `f=O(1/k)`;
3. if `f>=rho>0`, then `chi>=5^(rho k)`.

#### Proof

By Lemma 4.1 and the fact that every active line is contained in a
component,

\[
  5L\le\sum_j s_j\log_5s_j.                                    \tag{4.9}
\]

Choose a uniform root and let `S` be the size of its overlay component.
Then

\[
 \mathbb E\log_5S
 ={1\over N}\sum_js_j\log_5s_j
 \ge {5L\over N}=fk.                                           \tag{4.10}
\]

Also `E S=chi`.  Jensen's inequality for the exponential function gives

\[
             \chi=\mathbb E5^{\log_5S}
                    \ge5^{\mathbb E\log_5S}\ge5^{fk},
\]

which is (4.7).  The consequences follow immediately. \(\square\)

For the explicit suspended pentagon, every active line carries tagged
complete depth-one `l_1` action `18`.  Thus the total tagged action in
this architecture is

\[
                              18L,                               \tag{4.11}
\]

while the all-line tensor has action `18k5^(k-1)`.  Hence `f` is exactly
the fraction of the available tagged action retained.  Formula (4.8)
shows that components of size at most five retain at most `1/k` of that
action.  Constant action density forces exponential `chi`.

Physical target aggregation may cancel tagged action, so (4.11) is an
upper reservoir count, not a cap gain.  This only strengthens the no-go:
the diagonal lift fails before any statewise hinge signs are considered.

## 5. Spectator sheets and generalized voltage coverings

Adding spectator tuples does not create a loophole.  Suppose rows are
labelled by

\[
                         (x,s)\in\mathbb F_5^k\times\Sigma.       \tag{5.1}
\]

There are two possibilities.

### 5.1 Literal spectator contexts

If `s` is an actual exterior filling or carrier state, then restriction of
a physical `X/Y` resource to the exterior carrier records `s`.  Its full
colour is `[h,z,s,t]`, and every ownership edge fixes `s` as well as
`x_(hat h)`.  Theorems 2.1--4.2 apply separately on every sheet.  A
nonzero sheet voltage is impossible.

### 5.2 Resource-identical formal sheets

If the colour deliberately forgets `s`, the construction has made several
formal copies of one physical resource.  Keeping all copies violates
unique ownership; identifying them identifies distinct rooted rows and
their root ports.  Either operation leaves the exact factor fibre.

A pointwise colour-preserving auxiliary cover may attach extra sheet
motion to an allowed coordinate edge, but its component still projects
onto the coordinate component.  Therefore its cardinality is at least
the cardinality in (3.3), and the cover can only increase fragmentation.

A global permutation of slot carriers can evade the phrase “fixes `h`”
only by permuting physical resource colours.  That is a coordinate
conjugacy/relabeling, not a pointwise product-resource trade, and is the
already separated relabeling lane.

## 6. Exact boundary

The proved obstruction is architecture-specific but complete for that
architecture.

* It covers the full tensor, arbitrary correlated subsets of local
  slot-fibres, cyclic voltages, subdirect abelian quotients, nonabelian
  auxiliary sheets, and arbitrary integral component states.
* It uses the pointwise physical `X/Y` ledger and root ports.  It does not
  merely count aggregate degrees.
* It proves that a bounded-size component cannot act through a positive
  density of the `k` local pentagon slots.  More quantitatively, positive
  density `f` costs `chi>=5^(fk)`.

The only genuine escape must violate at least one defining feature of the
product packet: it must use a new exact factor whose resources are not a
union of context-separated copies of the local pentagon, or a nonlocal
resource whose single physical colour simultaneously sees several slot
carriers.  Merely assigning the old local edges diagonal voltages cannot
do so.
