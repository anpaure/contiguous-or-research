# Rooted isolated-reservoir coverdown and the exact SCD target Hall graph

Date: 2026-08-01  
Lane: K / prospective owner forest / tight one-to-two coverdown  
Status: unconditional fixed-`M_0` local theorem, exact rank-three colourful
reduction, and exact ordinary-Hall reduction on the prepared SCD
short-triangle bank.  Expansion/capture of the actual asymptotic leave is
not proved.

## 0. Outcome

The isolated-provider face removes both unresolved rows of the generic
tight augmenter.

Let an oriented upper-injective/lower-injective Johnson linear forest be
decorated by a perfect incidence matching `M_0`.  Each component has one
unused lower ticket at its terminal.  If an auxiliary edge

\[
                         A\longrightarrow C                         \tag{0.1}
\]

is an isolated component, then its terminal ticket is automatically the
`L'` required by the tight one-to-two identity.  If `B,D` are starts of
two other components, the replacement

\[
                  AC\longmapsto AB+CD                               \tag{0.2}
\]

keeps `M_0` pointwise fixed, preserves the two far terminal tickets, uses
the isolated ticket exactly once, and changes three rooted components into
two.  It is therefore a literal coverdown, not a rematching argument.

For a bank of isolated providers, every legal target--provider incidence
consumes exactly three component resources: the provider component and the
two host components.  Thus simultaneous coverdown is exactly a colourful
matching problem in rank-three component-footprint hypergraphs.  The
standard sufficient all-cut condition is

\[
 \nu\!\left(\bigcup_{R\in X}\mathcal A_R\right)>3(|X|-1)
             \qquad(\varnothing\ne X\subseteq\mathcal Z).          \tag{0.3}
\]

No separate graphic row remains after the footprints are disjoint.

On the prepared four-row SCD short-triangle bank, one of the two host
components is private to the provider and the other is indexed injectively
by the target.  Consequently (0.3) collapses to ordinary Hall in the exact
incidence graph

\[
                         L\sim U\quad\Longleftrightarrow\quad L\subset U.
                                                                        \tag{0.4}
\]

This is the requested rooted isolated-reservoir coverdown.  It absorbs an
`o(W)` missing shore whenever that shore is captured by the prepared banks
and satisfies their Hall cuts.  Neither capture nor those cuts follow from
the scalar assertion `o(W)` alone.

## 1. Decorated rooted forests and terminal tickets

Put

\[
 \Omega=[2m-1],\qquad
 \mathcal L={\Omega\choose m-1},\quad
 \mathcal M={\Omega\choose m},\quad
 \mathcal U={\Omega\choose m+1}.                                  \tag{1.1}
\]

Let `F` be an oriented linear forest on `mathcal M`, with distinct lower
edge colours and distinct upper edge colours.  Let

\[
                         M_0:\mathcal L\longrightarrow\mathcal M \tag{1.2}
\]

be a perfect containment matching satisfying

\[
                  M_0(X\cap Y)=X
              \qquad\text{for every oriented edge }X\to Y.       \tag{1.3}
\]

For a component `K` with terminal owner `t_K`, define

\[
                         \tau_K=M_0^{-1}(t_K).                     \tag{1.4}
\]

Every nonterminal owner is the image of the lower colour on its outgoing
edge.  Hence the `tau_K` are exactly the lower colours unused by `F`, one
per component, and

\[
                         \tau_K\subset t_K.                        \tag{1.5}
\]

This is precisely the endpoint common-basis certificate from
`MATH_THEOREM_K_PROSPECTIVE_UPPER_EXACT_FOREST_PAIR_BANK_AND_ROOTED_CONNECTOR_20260801.md`.

## 2. Automatic tight alignment of an isolated provider

Let one component of `F` consist of the single oriented edge

\[
                         p:A\longrightarrow C.                     \tag{2.1}
\]

Write

\[
 L=A\cap C,\qquad S=A\cup C,qquad A=L+a,qquad C=L+c.             \tag{2.2}
\]

By (1.3), `M_0(L)=A`.  Let `tau_p=M_0^{-1}(C)` be the terminal ticket of
this isolated component.

### Lemma 2.1 (the terminal ticket is the tight facet)

There is a unique `x in L` such that

\[
               \tau_p=C-x=(L-x)+c.                                \tag{2.3}
\]

Consequently

\[
                         D_p:=\tau_p+a=(L-x)+a+c                  \tag{2.4}
\]

is exactly the second new owner in the tight augmenter.

#### Proof

Containment gives `tau_p=C-y` for a unique `y in C`.  If `y=c`, then
`tau_p=L`, contradicting injectivity because `M_0(L)=A` and
`M_0(tau_p)=C` with `A!=C`.  Therefore `y in L`; call it `x`.  Equation
(2.4) follows.  \(\square\)

Thus no choice of a fresh facet ticket is needed on this face.  The common-
basis certificate itself supplies the correct one.

For every `b in Omega-S`, put

\[
 R_p(b)=A+b=L+a+b,\qquad B_p(b)=L+b.                               \tag{2.5}
\]

Equivalently, `R_p(b)` is characterized by

\[
                         R_p(b)\cap S=A.                           \tag{2.6}
\]

The provider has exactly `m-2` structural target neighbours before start,
slot, and protection filters are imposed.

## 3. The rooted three-to-two coverdown theorem

Let `K_B,K_D` be two components of `F`, distinct from one another and from
`p`, whose starts are respectively

\[
                         B=B_p(b),\qquad D=D_p.                     \tag{3.1}
\]

Write their oriented paths and terminal tickets as

\[
 B\leadsto b_*,\quad \tau_B\subset b_*;qquad
 D\leadsto d_*,\quad \tau_D\subset d_*.                           \tag{3.2}
\]

### Theorem 3.1 (fixed-`M_0` isolated coverdown)

Replace (2.1) by

\[
                         A\longrightarrow B,qquad
                         C\longrightarrow D.                     \tag{3.3}
\]

Then:

1. the old upper colour `S` is retained and the new upper colour `R_p(b)`
   is added;
2. the old lower colour `L` is retained and the terminal ticket `tau_p`
   is consumed;
3. `M_0` is unchanged pointwise;
4. the three paths

   \[
       [A\to C],\qquad[B\leadsto b_*],\qquad[D\leadsto d_*]
   \]

   become the two paths

   \[
       [A\to B\leadsto b_*],\qquad[C\to D\leadsto d_*];          \tag{3.4}
   \]

5. the exterior terminal tickets `tau_B,tau_D` are unchanged, while
   `tau_p` disappears with the lost component.

In particular, the component count and the unused-ticket count both change
from three to two.

#### Proof

The Boolean identities are

\[
\begin{aligned}
 A\cap B&=L,&A\cup B&=R_p(b),\\
 C\cap D&=\tau_p,&C\cup D&=S.                                   \tag{3.5}
\end{aligned}
\]

The first row of (3.5) follows from (2.5), and the second from
`D=tau_p+a`, (2.2)--(2.3).  Thus (3.3) is a literal tight replacement.
Before the move, (1.3)--(1.4) use

\[
                         M_0(L)=A,qquad M_0(\tau_p)=C.             \tag{3.6}
\]

After the move, these are exactly the predecessor equations for the two
new edges.  Every other value of `M_0` is untouched, proving item 3.

Because `B,D` are starts of distinct components, (3.3) attaches one end of
the split isolated edge to each component and cannot create a cycle.
Their far terminals are still `b_*,d_*`, so their tickets persist.  The
remaining assertions follow from (3.5).  \(\square\)

At the anonymous owner-slot level, the old slots at `A,C` are reused and
each start `B,D` has an available incoming slot.  Thus no additional slot
matching is hidden in Theorem 3.1.

## 4. Exact target-neighbour and component-footprint systems

Let `mathcal I` be a bank of unprotected isolated components of `F`, and
let `mathcal Z` be a set of missing upper colours.  A pair `(R,p)` is
**isolated-legal** when

1. `R=R_p(b)` for the unique `b=R-A_p`, equivalently `R cap S_p=A_p`;
2. `B_p(b)` and `D_p` are starts of two distinct components, neither equal
   to the provider component;
3. all protected-role and literal slot guards pass.

Define the target--provider graph

\[
 G_{\rm iso}\subseteq\mathcal Z\times\mathcal I,qquad
                         R\sim p\iff(R,p)\text{ is isolated-legal}. \tag{4.1}
\]

Every provider has structural degree at most `m-2`.  Before the readiness
filters, a target has at most `(m+1)(m-2)` possible oriented providers:
choose its common facet `A` and the exterior coordinate of the auxiliary
upper.

Ordinary Hall in `G_iso` is necessary but not sufficient in general,
because assignments using different providers may consume the same host
component.  The exact resource is the component footprint

\[
 \Phi(R,p)={K_p,K_{B_p(b)},K_{D_p}}.                              \tag{4.2}
\]

For every target `R`, let `mathcal A_R` be the rank-three hypergraph on the
component set of `F` whose labelled edges are the footprints (4.2).

### Theorem 4.1 (exact isolated-reservoir coverdown)

The missing bank `mathcal Z` admits simultaneous component-disjoint
isolated coverdowns preserving `M_0` if and only if the family

\[
                         (\mathcal A_R:R\in\mathcal Z)             \tag{4.3}
\]

has a rainbow matching.

A sufficient all-cut condition is

\[
 \boxed{
 \nu\!\left(\bigcup_{R\in X}\mathcal A_R\right)>3(|X|-1)
       \qquad(\varnothing\ne X\subseteq\mathcal Z).}              \tag{4.4}
\]

The elementary stronger condition

\[
                     \nu(\mathcal A_R)>3(|\mathcal Z|-1)
                       \qquad(R\in\mathcal Z)                     \tag{4.5}
\]

also suffices.

#### Proof

A rainbow matching chooses one legal move per target with pairwise-disjoint
provider and host components.  Apply Theorem 3.1 independently on those
component triples.  Every move keeps `M_0` fixed, and disjoint triples make
their union a linear forest without a separate graphic test.  Conversely,
every component-disjoint isolated coverdown records those disjoint
footprints, proving the equivalence.

Condition (4.4) is the colourful hypergraph Hall theorem at rank three.
For (4.5), greedily process the targets.  Each previously selected
three-set meets at most three edges of a fixed matching in `mathcal A_R`.
\(\square\)

The drop from rank four in the generic direct-augmenter theorem to rank
three here is exact: `tau_p` is uniquely bound to the provider component by
`M_0`.  If a purported support exposes several possible tickets at `C`, or
if no endpoint certificate has yet been fixed, a ticket token must be added
and the rank-four theorem applies instead.

### Corollary 4.2 (cross-private ordinary Hall)

Suppose the legal-incidence bank is **cross-private**: whenever `p!=q`,
every legal footprint through `p` is disjoint from every legal footprint
through `q`.  Then all missing targets can be covered down if and only if

\[
                         |N_{G_{\rm iso}}(X)|\ge|X|
                              \qquad(X\subseteq\mathcal Z).        \tag{4.6}
\]

#### Proof

Hall selects distinct providers.  Cross-privacy makes their complete
component footprints disjoint, so Theorem 4.1 applies.  Necessity is
immediate.  \(\square\)

A convenient sufficient form of cross-privacy is: every provider has a
private `D`-host, every legal target incidence has a private `B`-host, and
the provider, `B`-host, and `D`-host banks are mutually disjoint.

## 5. Exact component ledger for an asymptotic leave

Let

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1}=W-\operatorname {Cat}_m.                     \tag{5.1}
\]

If `F` has `U-h` edges, then it has

\[
                         \operatorname {Cat}_m+h                  \tag{5.2}
\]

components and the same number of terminal tickets.  Applying `h`
component-disjoint isolated coverdowns gives an upper-exact forest with
exactly

\[
                         \operatorname {Cat}_m                     \tag{5.3}
\]

components and terminal tickets, while retaining the same perfect matching
`M_0`.

Therefore an `o(W)` upper leave is absorbed on this face once (4.4) holds
for all its targets.  The size statement `h=o(W)` alone gives neither
capture in `G_iso` nor expansion in (4.4).

## 6. The prepared SCD short-triangle bank

Use the four-row SCD matching on

\[
                         [2m-1]=G\mathbin{\dot\cup}\{a,z\}.        \tag{6.1}
\]

Every short central chain

\[
                         S<L=S+x,qquad |S|=m-2                    \tag{6.2}
\]

has roots

\[
                         A_S=aS,qquad B_S=zS,qquad C_S=L          \tag{6.3}
\]

and

\[
 M_0(A_S)=aL,qquad M_0(B_S)=azS,qquad M_0(C_S)=zL.              \tag{6.4}
\]

Choose the triangle edge `C_S to A_S` as the isolated provider and leave
`B_S` as its private isolated start.  On physical owners the provider is

\[
                         zL\longrightarrow aL                       \tag{6.5}
\]

with terminal ticket `aS`.  For `b in G-L`, put

\[
                         U=L+b.                                    \tag{6.6}
\]

The isolated coverdown is exactly

\[
 C_S\to A_S [azL]
 \quad\rightsquigarrow\quad
 A_S\to B_S [azL];+;C_S\to P(U) [zU],                         \tag{6.7}
\]

where `M_0(P(U))=U`.  Its three component resources are

\[
   \{	ext{provider }C_S\to A_S, 	ext{private start }B_S,
                      	ext{long-root component }P(U)\}.          \tag{6.8}
\]

Different short chains have disjoint first two resources, and distinct
`U` have distinct long roots.  Coordinate signatures separate all three
banks.  Hence this is exactly the cross-private face of Corollary 4.2.

Let `mathcal L_sh` be the short-top bank and

\[
                         \mathcal U_{\rm sh}
                           =\partial^+\mathcal L_{\rm sh}.          \tag{6.9}
\]

The target graph, after removing the common coordinate `z`, is

\[
 G_{\rm SCD}\subseteq\mathcal U_{\rm sh}\times\mathcal L_{\rm sh},
                    \qquad U\sim L\iff L\subset U.                \tag{6.10}
\]

### Theorem 6.1 (exact SCD isolated-coverdown Hall theorem)

Let `X subseteq mathcal U_sh`, and suppose the components displayed in
(6.8) are present with the stated orientations and are disjoint from the
protected pivot.  Then all missing upper colours

\[
                         \{zU:U\in X\}                             \tag{6.11}
\]

are absorbed simultaneously, with `M_0` unchanged, if and only if

\[
 \boxed{
 \left|\{L\in\mathcal L_{\rm sh}:L\subset U
                  \text{ for some }U\in Y\}\right|\ge|Y|
                   \qquad(Y\subseteq X).}                         \tag{6.12}
\]

No additional graphic or endpoint-common-basis test is required.

#### Proof

Equation (6.12) is Hall's theorem for (6.10), saturating the missing target
side.  A matching chooses distinct short providers and distinct `U`.
Equation (6.8) makes their complete component footprints disjoint, so
Corollary 4.2 and Theorem 3.1 apply.  Conversely any such coverdown chooses
a distinct provider for each target and gives the Hall matching.  \(\square\)

The exact graph parameters are

\[
\begin{aligned}
 |\mathcal L_{\rm sh}|&=c:=\operatorname {Cat}_{m-1},\\
 \deg(L)&=m-2,\\
 |\mathcal U_{\rm sh}|&=I_m
     :=\operatorname {Cat}_m-2\operatorname {Cat}_{m-1},\\
 \deg(U)&=\mu(U)\in[2,m-1],\\
 |E(G_{\rm SCD})|&=(m-2)c.                                      \tag{6.13}
\end{aligned}
\]

More precisely, if `tau(U)` is the first time the associated walk reaches
level `-2`, then

\[
                         \mu(U)={\tau(U)\over2}+1,                 \tag{6.14}
\]

whose mean over `mathcal U_sh` is `(m+1)/2`.

One funnel can service at most `c` missing targets.  For `m>=6`, the full
reachable target bank has `I_m>c`, so (6.12) necessarily fails on the full
bank.  This is not an obstruction to an `o(W)` leave captured by several
prepared funnels; it proves that scalar target membership alone is not the
all-bank theorem.

## 7. Support-first versus fixed-`M_0` scope

The distinction is exact.

* **Fixed physical support only.**  An isolated edge `AC` and an arbitrary
  facet `L' subset C` do not constitute a typed coverdown.  There need not
  be a perfect incidence matching with `M_0(L')=C`, and `B,D` need not be
  free incoming starts.
* **Prospective support-first construction.**  One may plant the provider,
  choose its orientation and terminal-ticket state inside the endpoint
  common-basis problem, and orient the two hosts to start at `B,D`.  These
  are forced states in that common-basis instance, not consequences of an
  anonymous physical forest.
* **Certified fixed `M_0`.**  Once (1.3)--(1.5) and the start conditions
  hold, Lemma 2.1 makes the residual predecessor edge automatic and
  Theorem 3.1 keeps `M_0` literally unchanged.  The fixed-residual
  singleton blockers from the general typed catalogue do not occur on
  this isolated-terminal face.

The theorem controls owner/lower/upper synchronization, physical
acyclicity, and the endpoint common-basis certificate.  It does not imply
residence, deeper-shadow support, source-word realizability, or the final
common-cap compiler.  Those guards must be planted in, or verified after,
the resulting forest.

## 8. Sharp remaining expansion statement

The weakest exact isolated-reservoir theorem still missing for the
asymptotic construction is:

> Build the protected `U-o(W)` forest and its endpoint common-basis
> certificate so that every missing upper lies in the captured target
> graph and the rank-three all-cut inequality (4.4) holds; on the SCD
> private face it is enough that the ordinary Hall inequalities (6.12)
> hold across a union of prepared short-triangle banks.

The local component algebra, terminal-ticket accounting, and physical
forest row are now closed.  What remains is a genuine prospective
expansion/capture theorem.  It is weaker than a full owner-slot
`Delta`-edge-colouring and stronger than scalar Catalan slack or raw menu
size.
