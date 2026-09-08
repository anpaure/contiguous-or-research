# Growing root-operadic skeleton packets: exact incidence, codegree obstruction, and the suspension gap

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Verdict

Let `T_s` be the set of ordered full binary trees with `s` internal nodes,
so `|T_s|=C_s=Cat_s`.  Fix `1<=t<=s`.  For an ordered forest

\[
                         \mathbf U=(U_0,\ldots,U_t),
 \qquad \sum_{i=0}^t|U_i|=s-t,                        \tag{0.1}
\]

let

\[
 E_{\mathbf U}=\{S[U_0,\ldots,U_t]:S\in\mathcal T_t\}\subseteq\mathcal T_s
                                                                  \tag{0.2}
\]

be all `C_t` bracketings of the fixed ordered spectators.  These sets form
the root-operadic skeleton hypergraph `H_(s,t)`.

The exact positive incidence facts are:

\[
 \boxed{|E_{\mathbf U}|=C_t,}                          \tag{0.3}
\]

\[
 \boxed{
 |\mathcal E_{s,t}|=[z^{s-t}]C(z)^{t+1}
 ={t+1\over2s-t+1}\binom{2s-t+1}{s-t},}              \tag{0.4}
\]

and the average vertex degree is

\[
 \boxed{
 \bar d_{s,t}
 =\binom{2t}{t}{(s)_t\over(2s)_t}.}                   \tag{0.5}
\]

Here `(x)_t=x(x-1)...(x-t+1)`.  Uniformly for
`t -> infinity`, `t=o(sqrt(s))`,

\[
 \boxed{
 \bar d_{s,t}=(1+o(1)){2^t\over\sqrt{\pi t}}.}        \tag{0.6}
\]

Thus the proposed average-degree gain is real.

It does not by itself give a near-perfect matching.

1. Degrees are not uniform.  At least `2^t C_(s-t)` vertices have degree
   one, although their proportion is only `(1+o(1))2^{-t}`.
2. More decisively, maximum pair codegree is not small on the degree scale:

   \[
   \boxed{
   \Delta_2(\mathcal H_{s,t})
   \ge\bar d_{s-2,t-2}
   =\left({1\over4}+o(1)\right)\bar d_{s,t}.}          \tag{0.7}
   \]

   A single root rotation inherits every root cut of a common large
   spectator.  Hence the usual near-regular, `codegree=o(degree)` nibble
   theorem cannot be invoked on the full hypergraph.

There is a still earlier exact-factor obstruction.  A hyperedge in (0.2)
is a packet of **ports**, not automatically a common `X/Y` ownership slab.
For general nonempty spectators, changing the outer bracketing moves
spectator Dyck words across the skeleton parentheses.  The roots are not
images of `D_t` under the fixed-exterior affine one-hole context used by
the proved port-factor substitution theorem.  This failure occurs already
at `t=2` and can have unbounded Hamming support.

The guaranteed literal parent-aligned subfamily consists of the common
suffix contexts

\[
                         S\longmapsto S A,qquad A\in\mathcal T_{s-t},
                                                                  \tag{0.8}
\]

and its left/right mirror.  One boundary therefore covers exactly

\[
                         C_tC_{s-t}                    \tag{0.9}
\]

roots in disjoint `C_t`-packets.  If `t -> infinity` and `t=o(s)`, its
density is

\[
 \boxed{
 {C_tC_{s-t}\over C_s}
 =(1+o(1)){1\over\sqrt\pi,t^{3/2}}=o(1).}             \tag{0.10}
\]

For `t=4`, (0.9) is the audited `14C_(s-4)` and its limiting density is
`14/4^4=7/128` per boundary.  Growing `t` makes this proved literal
coverage smaller, not larger.

Consequently a near-perfect matching of the **root** hypergraph, even if
proved by a nonstandard argument, would not yet assemble an exact factor.
One needs a new multi-hole Catalan-operadic suspension theorem which
partitions both physical `X`-vertices and `Y`-colours for every selected
forest packet.  No such theorem is presently proved.

Finally, fixed `D_4`/rooted primitives do not by themselves make a growing
`D_t` factor boundary-rich.  A root-aligned `D_4` chart reaches only
`C_4C_(t-4)` of the `C_t` ports per boundary, asymptotic fraction `7/128`;
two boundary charts cover at most `7/64+o(1)` before compatibility and
overlap losses.  Strict internal charts are erased.  Therefore the
remaining factor problem is genuinely growing: construct noncanonical
`D_t`-port factors with extensive boundary-state action, not merely a
fixed collection of suspended `D_4` atoms.

The route is not disproved in its strongest possible form.  What is
closed is the inference

\[
 \text{large average root degree}
 \Longrightarrow
 \text{near-perfect exact-factor packetization}.      \tag{0.11}
\]

Both a new matching argument and a new operadic `X/Y` suspension theorem
are required.

## 1. Edge size and edge count

Write a binary tree as a term in the free nonsymmetric binary operad.  If
`S` has `t` internal nodes, it has `t+1` ordered leaves, so the substitution
in (0.2) has total size

\[
                         t+\sum_i|U_i|=s.              \tag{1.1}
\]

### Lemma 1.1 (fixed-forest injectivity)

For a fixed ordered forest `U`, the map

\[
                         S\longmapsto S[\mathbf U]     \tag{1.2}
\]

from `T_t` to `T_s` is injective.

#### Proof

At the root, a skeleton splits its ordered leaves after a unique index
`j`.  The size of the substituted left tree is

\[
                 j+\sum_{i=0}^{j}|U_i|,               \tag{1.3}
\]

with the harmless choice of indexing convention absorbed into `j`.  This
quantity is strictly increasing with the number of leaves on the left.
Equality of two substituted trees therefore forces the same root leaf
split.  Apply the same argument recursively to the two children. \(\square\)

Thus every edge has size `C_t`.

### Lemma 1.2 (the ordered forest is recoverable from its edge)

Distinct ordered forests give distinct sets (0.2).

#### Proof

The Tamari order on `T_t` is preserved by substitution of fixed ordered
trees.  Hence `E_U` has a unique Tamari-maximum member, the right-comb
bracketing

\[
             U_0\bigl(U_1(\cdots(U_{t-1}U_t)\cdots)\bigr).             \tag{1.4}
\]

Starting at its root, successively read the left child down the right
spine.  This recovers `U_0,U_1,...,U_t` in order.  Thus the edge determines
the forest. \(\square\)

The number of edges is therefore the number of ordered forests in (0.1):

\[
                         |\mathcal E_{s,t}|
                         =[z^{s-t}]C(z)^{t+1}.          \tag{1.5}
\]

The Lagrange coefficient identity

\[
                         [z^n]C(z)^k
 ={k\over2n+k}\binom{2n+k}{n}                        \tag{1.6}
\]

with `n=s-t`, `k=t+1` proves (0.4).

## 2. Exact vertex degrees and their mean

A root skeleton cut of a tree `T` is an ancestor-closed set of internal
nodes containing the root.  Removing a cut of size `t` leaves an ordered
forest of `t+1` spectator subtrees.  Thus the degree `d_t(T)` is exactly
the number of size-`t` root skeleton cuts.

Define the cut polynomial recursively by

\[
 D_{\bullet}(z)=1,
 \qquad
 D_{(L,R)}(z)=1+zD_L(z)D_R(z).                         \tag{2.1}
\]

Then

\[
                         \boxed{d_t(T)=[z^t]D_T(z).}   \tag{2.2}
\]

Indeed, a nonempty root cut contains the root and independently chooses a
root cut in each child; (2.1) records their total size.

Double-counting incidences gives

\[
                         \bar d_{s,t}
 ={C_t|\mathcal E_{s,t}|\over C_s}.                   \tag{2.3}
\]

Using (0.4) and `C_r=binom(2r,r)/(r+1)`, one obtains the exact cancellation

\[
 { |\mathcal E_{s,t}|\over C_s}
 =(t+1){(s)_t\over(2s)_t},                            \tag{2.4}
\]

and (0.5) follows.

For `t=o(sqrt(s))`,

\[
 \log{(s)_t\over(2s)_t}
 =-t\log2-{t(t-1)\over4s}+O\left({t^3\over s^2}
                                      +{t\over s}\right),             \tag{2.5}
\]

while

\[
                         \binom{2t}{t}
 =(1+O(t^{-1})){4^t\over\sqrt{\pi t}}.                \tag{2.6}
\]

Equations (2.5)--(2.6) prove (0.6).

### Proposition 2.1 (a vanishing but exact low-degree family)

At least `2^t C_(s-t)` vertices have degree exactly one.

#### Proof

Choose a left/right orientation sequence of length `t` and form a rooted
comb of `t` internal nodes, putting a leaf on the chosen side at every
step and an arbitrary tree `A in T_(s-t)` after the final continuation.
An ancestor-closed root set of `t` internal nodes must take the entire
outer comb: stopping earlier leaves only a leaf on the other side, while
entering `A` would require all `t` comb nodes first and hence use at least
`t+1` nodes.  Thus its size-`t` cut is unique.

The first `t` orientations and the terminal tree are recovered from the
resulting tree, so all `2^t C_(s-t)` constructions are distinct. \(\square\)

For `t=o(s)`, their proportion is `(1+o(1))2^{-t}`.  Thus low degree alone
does not block an almost-perfect matching when `t -> infinity`, but the
hypergraph is not uniformly regular.

## 3. A constant-scale codegree obstruction

For distinct trees `T,T'`, let `lambda_t(T,T')` be the number of edges
containing both.

### Theorem 3.1 (one rotation carries all inner refinements)

For `2<=t<=s-2`,

\[
                 \max_{T\ne T'}\lambda_t(T,T')
                 \ge\bar d_{s-2,t-2}.                 \tag{3.1}
\]

#### Proof

Choose `A in T_(s-2)` with

\[
                         d_{t-2}(A)\ge\bar d_{s-2,t-2};\tag{3.2}
\]

such an `A` exists by averaging.  Let `o` denote the empty tree and put

\[
                         T_L=((A,o),o),
 \qquad                  T_R=(A,(o,o)).                \tag{3.3}
\]

These are the two sides of one root rotation and have size `s`.

For every size-`t-2` root cut of `A`, let
`(U_0,...,U_(t-2))` be its spectator forest.  Add the two empty spectators
from (3.3).  Both `T_L` and `T_R` are bracketings of the resulting ordered
forest of `t+1` trees by a skeleton of size `t`.  Thus they lie in a common
edge of `H_(s,t)`.  Distinct cuts give distinct ordered forests and hence,
by Lemma 1.2, distinct edges.  This proves (3.1). \(\square\)

If `t -> infinity` and `t=o(sqrt(s))`, formula (0.6) applied twice gives

\[
 {\bar d_{s-2,t-2}\over\bar d_{s,t}}
 ={1\over4}\sqrt{t\over t-2}\,(1+o(1))
 ={1\over4}+o(1),                                     \tag{3.4}
\]

which proves (0.7).

Theorem 3.1 does not disprove a near-perfect matching.  It proves that the
standard route from (0.6) through a maximum-codegree nibble has a false
hypothesis.  Any matching proof must exploit the nested rotation geometry,
thin or orient the hypergraph in a structure-sensitive way, or use an
explicit packet selector.

## 4. Why a root packet is not yet a port-factor packet

Use the standard Dyck encoding

\[
                         w((L,R))=1w(L)0w(R),
 \qquad                  w(\bullet)=\varnothing.       \tag{4.1}
\]

The existing exact local-factor context theorem applies when all roots in
a packet agree outside one fixed set of `2t` local coordinates.  Equivalently,
their ports have the form

\[
                         E\mathbin{\dot\cup}\iota(P),
 \qquad                  P\in\mathcal D_t,             \tag{4.2}
\]

for one exterior set `E` and one coordinate injection `iota`; the matching
`X`- and `Y`-ledgers are then pushed forward through the same context.

General operadic edges do not have this form.  The failure is already
visible at `t=2`.  Take

\[
                         w(U_0)=(10)^a,
 \qquad                  U_1=U_2=\bullet.             \tag{4.3}
\]

The two outer bracketings have words

\[
                         x_a=11(10)^a00,
 \qquad                  y_a=1(10)^a010.              \tag{4.4}
\]

Their Hamming distance is `2a`.  For `a>2` this exceeds the four local
coordinates available to a `D_2` hole.  Hence no fixed exterior/injection
representation (4.2) exists for this edge.  Embedding the same rotation
inside a larger skeleton and choosing `a>t` gives, for every `t>=2`, an
edge whose variation is supported on more than `2t` coordinate positions.

This refutes an automatic use of the proved affine context functor.  It
does not refute a new **multi-hole operadic suspension theorem** whose
token map is allowed to move spectator coordinates coherently.  Such a
theorem would have to prove, rather than assume, that the selected packets'
complete physical `X`- and `Y`-token unions are disjoint and common across
all `C_t` bracketings.

## 5. The proved literal subfamily has vanishing density

Put all spectators except the rightmost one equal to the empty tree.  Then

\[
              w(S[\bullet,\ldots,\bullet,A])=w(S)w(A),\tag{5.1}
\]

so the `C_t` roots form the common suffix context required by the existing
port-factor suspension theorem.  For different `A in T_(s-t)`, the packets
are disjoint: their first `2t` bits recover `S` and their suffix recovers
`A`.  This proves the exact packet and coverage count (0.9).

The mirror construction gives the opposite boundary.  Even before their
overlap and joint-legality constraints are imposed, their union covers at
most `2C_tC_(s-t)` roots.

Using the Catalan asymptotic, uniformly for `t -> infinity`, `t=o(s)`,

\[
 {C_tC_{s-t}\over C_s}
 =(1+o(1)){1\over\sqrt\pi,t^{3/2}}
             \left({s\over s-t}\right)^{3/2},         \tag{5.2}
\]

which is (0.10) when `t=o(s)`.  At fixed `t=4`, the limiting ratio is
`C_4/4^4=7/128`, exactly the audited literal parent-aligned coverage.

Thus the full operadic hypergraph has large average degree only because it
uses moving multi-spectator interfaces not covered by the current exact
factor context theorem.  The subhypergraph on which factor suspension is
already legal has an explicit matching, but it covers `o(C_s)` vertices
when `t -> infinity`.

## 6. Boundary states of a growing local factor

Suppose, conditionally, that a future theorem makes selected edges of
`H_(s,t)` into common exact-factor packets.  One still needs a family of
noncanonical `D_t`-port factors whose complete parent-aligned boundary
profiles occupy enough residual cells.

A fixed root-aligned `D_4` chart in `D_t` has one-boundary port coverage

\[
                         C_4C_{t-4}=14C_{t-4}.         \tag{6.1}
\]

Therefore

\[
                         {14C_{t-4}\over C_t}
                         \longrightarrow {14\over4^4}
                         ={7\over128}.                \tag{6.2}
\]

Two opposite charts cover at most `7/64+o(1)` of the ports, and the useful
two-boundary intersection can only be smaller.  Any `D_4` chart strictly
inside the local skeleton is swallowed by the serviced window and has zero
endpoint action.

Consequently no finite collection of the presently certified fixed
rooted primitives gives near-complete boundary action as `t -> infinity`.
A successful factor theorem must use a genuinely growing `D_t` path
factor or a growing family of boundary-active primitives with an audited
common-completion ledger.  It must also retain the entire carrier-resolved
profile, not only the marked first-insertion label.

## 7. Exact remaining theorem

The growing-skeleton route now has two independent missing statements.

1. **Operadic packing and suspension.**  Select disjoint forest edges
   covering `C_s-o(C_s)` roots and prove that each selected edge is a
   common physical `X/Y` ownership slab supporting arbitrary integral
   `D_t`-port-factor shores.  The root hypergraph matching and the token
   suspension must be proved jointly; neither implies the other.
2. **Growing boundary library.**  Construct product-compatible
   noncanonical `D_t`-port factors with enough parent-aligned states on
   almost all packet roots, and prove their complete multidepth residual-
   capacity and carrier separation inequalities.

The exact counts (0.4)--(0.6) show that root supply is abundant.  The
codegree bound (0.7) blocks the off-the-shelf nibble, while Sections 4--6
show that fixed-size suspension does not convert that supply into integral
exact-factor action.  Absent one of the two theorems above, the justified
pivot is to genuinely growing `D_t` path factors rather than further fixed
`D_4` fringe iteration.

