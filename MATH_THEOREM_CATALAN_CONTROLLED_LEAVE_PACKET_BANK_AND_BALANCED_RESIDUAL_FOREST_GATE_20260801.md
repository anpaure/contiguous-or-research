# A Catalan controlled-leave packet bank reduces exact odd synchronization
# to one balanced residual forest

Date: 2026-08-01  
Lane: mixed-head SCD reservoir / tight one-to-two activation / exact odd
owner forest  
Status: packet construction and asymptotic local-load theorem remain valid.
**The balanced residual-forest conclusion is superseded and impossible for
this frozen interface** by the coordinate-cocycle obstruction in
`MATH_THEOREM_CATALAN_CONTROLLED_LEAVE_RESIDUAL_COORDINATE_COCYCLE_NOGO_20260801.md`.

> Correction (2026-08-01).  Saturating all residual uppers and slots would
> force the `C` unused lower resources to contain the distinguished letter
> `a` exactly `2C-2Cat_(m-1)>C` times.  Thus Sections 4--6 are a conditional
> reduction with an unsatisfiable hypothesis, not the sole remaining open
> gate.  Sections 1--3 and the packet identity are unaffected.

## 0. Outcome

Use the notation

\[
 \Omega=[2m-1],\qquad
 \mathcal L={\Omega\choose m-1},\quad
 \mathcal M={\Omega\choose m},\quad
 \mathcal U={\Omega\choose m+1},
\]

\[
 W=|\mathcal L|=|\mathcal M|,qquad
 U=|\mathcal U|,qquad
 C=\operatorname {Cat}_m=W-U.
\]

The preceding isolated-reservoir theorem proved that one mixed-head SCD
bank contains `C` well-spread isolated providers, but also found a zero
shore: those providers can add only targets containing their distinguished
coordinate `a`.

That zero shore does **not** force `m-1` strata if the target leave is chosen
together with the provider bank.  This note constructs a single-stratum
controlled leave of order exactly `C`.

Fix an SCD successor bijection

\[
 \sigma:{G\choose m-2}\longrightarrow {G\choose m-1},
 \qquad S\subset\sigma(S),qquad |G|=2m-3.          \tag{0.1}
\]

There is a second incidence bijection `beta` such that

\[
                  S\subset\beta(S),qquad
                  \beta(S)\ne\sigma(S).             \tag{0.2}
\]

Put `tau=sigma^(-1) beta`.  It is a derangement.  An independent set in its
cycle graph has order at least one third of the whole layer, so for all
sufficiently large `m` it contains a `C`-set `P`.

For `S in P`, write

\[
             L=\sigma(S)=S+x,qquad
             V=\beta(S)=S+b.                        \tag{0.3}
\]

The exact tight packet is

\[
 \boxed{
 (azL,aS;\ aL,azS)
 \quad\longrightarrow\quad
 (azV,aS;\ azS,aV)
 \ +\
 (azL,L;\ aL,zL).}                                  \tag{0.4}
\]

Thus the four new tickets are

\[
             \text{target }azV,\qquad
             \text{lower }L,\qquad
             B=aV,\qquad D=zL.                      \tag{0.5}
\]

The independent-set condition `P cap tau(P)=emptyset` makes every resource
in all `C` packets distinct.  The packets therefore form a literal
`2^C` off/on cube.

Reserve the complete packet interface:

* delete the `C` auxiliary and `C` target upper colours;
* delete the `C` old and `C` new lower colours;
* at the provider endpoints `A=aL,C_0=azS`, reserve both slots; and
* at the future attachment endpoints `B=aV,D=zL`, reserve one slot and
  leave the other for the residual forest.

The exact residual counts become

\[
 \begin{array}{c|c}
 \text{resource}&\text{residual count}\\ \hline
 \text{upper}&U-2C=W-3C\\
 \text{lower}&W-2C\\
 \text{owner slots}&2W-6C=2(U-2C).
 \end{array}                                        \tag{0.6}
\]

Hence the missing owner-layer theorem is now one balanced object:

> Find a matching in the induced residual host which saturates every
> residual upper colour and every residual owner slot, and whose physical
> projection is a forest.

Such a forest has exactly `C` components and endpoint bank exactly `B cup D`.
Activating all packets in (0.4) attaches the old provider endpoints as
leaves, produces an upper-exact physical forest of order `U`, and leaves
exactly `C` components.  Every lower colour and owner slot is already
integral; no target/provider, `B`, `D`, or new-lower Hall problem remains.

The complete packet bank can be chosen with local load
`O(m^2/log m)`.  Thus the induced residual host remains asymptotically
regular with codegree `o(m^2)`.  Delcourt--Postle gives an
`(U-2C)-o(W)` residual forest, but not the exact saturation required above.
That exact balanced-forest step is the sole remaining owner-layer gate in
this construction.

## 1. A deranged incidence matching

Let

\[
                     \mathcal S={G\choose m-2},qquad
                     \mathcal V={G\choose m-1},qquad
                     N=|\mathcal S|=|\mathcal V|.   \tag{1.1}
\]

Form the bipartite graph `K_sigma` on `mathcal S,mathcal V` by

\[
                  S\sim V
       \quad\Longleftrightarrow\quad
                  S\subset V\ \hbox{ and }\ V\ne\sigma(S).    \tag{1.2}
\]

### Lemma 1.1 (the non-successor square graph is regular)

`K_sigma` is `(m-2)`-regular.  Consequently it has a perfect matching

\[
                       \beta:\mathcal S\longrightarrow\mathcal V. \tag{1.3}
\]

#### Proof

Every `S` has `m-1` rank-`(m-1)` supersets in `G`, exactly one of which is
`sigma(S)`.  Every `V` has `m-1` rank-`(m-2)` facets, exactly one of which
is `sigma^(-1)(V)`.  Deleting the SCD matching therefore leaves degree
`m-2` on both shores.  Every regular bipartite graph has a perfect
matching. \(\square\)

Define

\[
                          \tau=\sigma^{-1}\circ\beta.           \tag{1.4}
\]

Since `beta(S) != sigma(S)`, `tau` has no fixed point.

### Lemma 1.2 (large cycle-independent bank)

The undirected graph with edges `{S,tau(S)}` has an independent set `I`
with

\[
                              |I|\ge N/3.                       \tag{1.5}
\]

For every `m>=23`, `I` contains a `C`-subset.

#### Proof

The graph is a disjoint union of cycles of lengths at least two.  A
two-cycle has independence ratio `1/2`, a three-cycle ratio `1/3`, and a
cycle of length `ell>=4` has an independent set of order `floor(ell/2)`.
This proves (1.5).

The exact ratio is

\[
 {C\over N}={4(2m-1)\over m(m+1)}.                 \tag{1.6}
\]

It is at most `1/3` from `m=23` onward. \(\square\)

## 2. The exact packet identity

Take `S in I` and use (0.3).  Since `beta(S) != sigma(S)`, we have

\[
                              x\ne b,qquad b\notin L.            \tag{2.1}
\]

The mixed-head provider is

\[
                         f_S=(azL,aS;\ aL,azS).                  \tag{2.2}
\]

In the notation of the tight one-to-two augmenter, substitute

\[
 \widehat L=aS,qquad
 \widehat a=z,qquad
 \widehat b=b,qquad
 \widehat c=x,qquad
 \widehat x=a.                                      \tag{2.3}
\]

Then

\[
\begin{array}{lll}
 \widehat A=azS,&\widehat B=aV,&\widehat R=azV,\\
 \widehat C=aL,&\widehat D=zL,&\widehat L'=L,
\end{array}                                         \tag{2.4}
\]

and the auxiliary upper colour is `azL`.  This proves (0.4).

### Theorem 2.1 (resource-disjoint activation cube)

Let `P subseteq I`.  Across all packets indexed by `P`, the following
eight resource maps have pairwise-disjoint images whenever their resource
types agree:

\[
\begin{array}{c|cc}
 &\text{off/auxiliary}&\text{new/target}\\ \hline
 \text{upper}&az\sigma(S)&az\beta(S)\\
 \text{lower}&aS&\sigma(S)\\
 \text{owner bank 1}&a\sigma(S)&a\beta(S)\\
 \text{owner bank 2}&azS&z\sigma(S).
\end{array}                                         \tag{2.5}
\]

In fact all four physical owner banks in (2.5) are mutually disjoint.
Therefore every subset of `P` may be activated independently, giving an
exact `2^|P|` owner-slot matching cube.

#### Proof

Every individual map in (2.5) is injective because `sigma,beta` are
bijections.  If an auxiliary upper equals a target upper, then

\[
                    \sigma(S)=\beta(T)=\sigma(\tau(T)),
\]

so `S=tau(T)`, forbidden by independence of `I`.  The same argument
separates the two `a`-only owner banks.

The old and new lower banks are separated by the presence of `a`.  The
four physical owner signatures are respectively

\[
              a\bar z,\qquad a\bar z,qquad az,qquad \bar a z,
\]

and the only repeated signature is the pair already separated by
independence.  Thus all resources are distinct.  The off/on identity uses
the same auxiliary upper and the same two retained owner slots within one
packet, exactly as required by the tight augmenter.  Different packets
share nothing, so their activations commute. \(\square\)

## 3. A spread `C`-packet subbank

Choose `P` uniformly among the `C`-subsets of one independent set `I`
satisfying (1.5).  Its inclusion density obeys

\[
                 {C\over|I|}\le {3C\over N}\le {25\over m}    \tag{3.1}
\]

for all sufficiently large `m`.

Reserve the packet resources exactly as follows.  For each `S in P`:

* the off provider uses one slot at `A=aL` and one at `C_0=azS`;
* delete the complementary slots at `A,C_0`, so both physical endpoints
  are closed to the residual bulk; and
* reserve one future packet slot at `B=aV` and one at `D=zL`, leaving the
  other slot at each of `B,D` in the residual host.

Let

\[
 \mathcal R_*\subseteq\mathcal U,\qquad
 \mathcal L_*\subseteq\mathcal L,\qquad
 \rho:\mathcal M\longrightarrow\{0,1,2\}            \tag{3.2}
\]

record the reserved uppers, reserved lowers and number of reserved slots at
each physical owner.  Thus `rho=2` on `A cup C_0`, `rho=1` on `B cup D`,
and zero elsewhere.

### Lemma 3.1 (exact residual degree formulas)

For a surviving upper `R`, lower `K`, and owner slot `T^i`, respectively,

\[
\begin{aligned}
 d_*(R)
 &=\sum_{\{x,y\}\subset R}
   1_{R-\{x,y\}\notin\mathcal L_*}
   (2-\rho(R-x))(2-\rho(R-y)),\\
 d_*(K)
 &=\sum_{\{x,y\}\subset\Omega-K}
   1_{K+\{x,y\}\notin\mathcal R_*}
   (2-\rho(K+x))(2-\rho(K+y)),\\
 d_*(T^i)
 &=\sum_{x\in T,\ y\notin T}
   1_{T-x\notin\mathcal L_*}
   1_{T+y\notin\mathcal R_*}
   (2-\rho(T-x+y)).                                  \tag{3.3}
\end{aligned}
\]

Consequently, if `A_R,S_R` count reserved lower two-facets and reserved
owner slots on facets of `R`, if `A_K,S_K` are the dual counts at `K`, and
if `A_T^-,A_T^+,J_T` count reserved lower facets, upper cofacets and
reserved slots on Johnson neighbours of `T`, then

\[
\begin{aligned}
 2m(m+1)-d_*(R)&\le4A_R+2mS_R,\\
 2m(m-1)-d_*(K)&\le4A_K+2(m-1)S_K,\\
 2m(m-1)-d_*(T^i)&\le
       2(m-1)A_T^-+2mA_T^++J_T.                     \tag{3.4}
\end{aligned}
\]

The underlying candidate-class orders are at most

\[
\begin{array}{c|cc}
 &A&S\\ \hline
 R&2{m+1\choose2}&2(m+1)\\
 K&2{m\choose2}&2m
\end{array},
\qquad
 A_T^-\le2m,\quad A_T^+\le2(m-1),\quad J_T\le2m(m-1). \tag{3.5}
\]

The factors two allow the two resource maps of the same rank.  Slot weights
are already included in `S_R,S_K,J_T`.

#### Proof

An atom through `R` is determined by the deleted pair `{x,y}`.  Its lower
resource is `R-{x,y}`, and it has independently any surviving slot at the
two owner facets `R-x,R-y`; this is the first identity.  The second is its
added-pair dual.  An atom through `T^i` is indexed by deleting `x` and
adding `y`; its other owner is `T-x+y`, which gives the third identity.

For (3.4), charge a bad lower or upper two-shadow resource four possible
slot pairs.  A reserved facet slot occurs with at most `2m` atoms in an
upper star and `2(m-1)` atoms in a lower star.  In an owner-slot star, a
bad lower facet fixes `x`, a bad upper cofacet fixes `y`, and a reserved
neighbour slot kills one atom.  The candidate counts in (3.5) are the
numbers of two-facets, facets, cofacets and Johnson neighbours, with a
factor two for the two packet maps. \(\square\)

### Theorem 3.2 (the complete packet interface is asymptotically invisible)

There is a `C`-subset `P subseteq I` for which deletion of all reserved
upper, lower and slot resources lowers every surviving odd-host degree by

\[
                         O\left({m^2\over\log m}\right)=o(m^2). \tag{3.6}
\]

The maximum codegree remains at most `2m`.  The same statement holds while
retaining any fixed resource-disjoint protected forest of order
`O(sqrt(m))`.

#### Proof

All packet maps of one resource type are injective by Theorem 2.1.  For a
fixed upper star, the candidate packet lower resources lie among its
two copies of its `binom(m+1,2)` lower two-facets and the candidate packet
owner resources among two copies of its `m+1` owner facets.  For a fixed
lower star the corresponding safe counts are `2 binom(m,2)` and `2m`.
For a fixed owner-slot star, candidate
packet lower facets, upper cofacets and owner neighbours have orders at
most

\[
                    2m,\qquad 2(m-1),\qquad 2m(m-1).            \tag{3.7}
\]

A packet contributes at most two upper or lower resources.  Its endpoint
slot weights are `2,2,1,1` on the `A,C_0,B,D` banks, so it has weight at
most six in any fixed physical-owner candidate class.  These constants are
independent of `m`.

For a hypergeometric count `X` from a `K`-element candidate class,

\[
             E X\le {25K\over m},
 \qquad
             Pr(X\ge t)\le\left({eE X\over t}\right)^t.        \tag{3.8}
\]

Use thresholds

\[
                         t_1={64m\over\log m},
             \qquad     t_2={64m^2\over\log m}.                \tag{3.9}
\]

After the possible factor six for one packet's endpoint weights, a
facet/cofacet class
exceeds `t_1` with probability at most

\[
                         \exp(-(10-o(1))m),                     \tag{3.10}
\]

while a two-shadow or Johnson-neighbour class exceeds `t_2` with
probability `exp(-Omega(m^2))`.  There are fewer than `2^(2m+1)` host
vertices.  A union bound therefore makes all these inequalities hold
simultaneously.

Equations (3.4) and (3.7)--(3.10) consequently imply the asserted
`O(m^2/log m)` degree loss.

A fixed protected bank excludes only `O(sqrt(m))` candidate packets,
because every map in (2.5) is injective.  Its direct loss is
`O(m^(3/2))`.  Neither change affects the argument. \(\square\)

### Corollary 3.3 (near residual forest)

The induced residual host contains a physical linear forest of order

\[
                              (U-2C)-o(W).                       \tag{3.11}
\]

#### Proof

Theorem 3.2 leaves an asymptotically regular four-graph with maximum
codegree `o(m^2)`.  Apply the audited Delcourt--Postle short-cycle
colouring, then delete one edge from each surviving long physical cycle
and take the slow cycle-cutoff diagonal. \(\square\)

The `o(W)` in (3.11) is the only loss in the owner-layer construction below.

## 4. Exact residual counts

The packet bank removes or reserves the following typed resources.

* Upper: the `C` auxiliary colours `az sigma(P)` and the `C` target colours
  `az beta(P)`.
* Lower: the `C` provider colours `aP` and the `C` future colours
  `sigma(P)`.
* Owner slots: both slots at each of the `2C` physical owners in the
  `A,C_0` banks, and one slot at each of the `2C` owners in the `B,D`
  banks.

Theorem 2.1 says there is no overlap inside any row.  Therefore the exact
residual counts are (0.6).

### Lemma 4.1 (balanced saturation forces the endpoint bank)

Let `F_res` be an owner-slot matching in the induced residual host which
saturates every residual upper colour.  If it also saturates every residual
owner slot, then its physical projection has

* degree zero at every `A,C_0` provider endpoint;
* degree one at every `B,D` attachment endpoint; and
* degree two at every other physical owner.

If its projection is a forest, it is a union of exactly `C` paths whose
endpoint set is exactly `B cup D`.

#### Proof

The degree assertions are the numbers of residual slots at the four owner
types.  The physical vertex set used by `F_res` has order `W-2C`, since
the `2C` owners in `A cup C_0` have no residual slot.  Saturating every
residual upper gives

\[
                         |F_{res}|=U-2C=W-3C.                    \tag{4.1}
\]

A forest on `W-2C` vertices with `W-3C` edges has `C` components.  Its
maximum degree is two and it has exactly `2C` degree-one vertices, namely
`B cup D`, so every component is a path. \(\square\)

## 5. Exact completion from the balanced residual forest

### Theorem 5.1 (controlled-leave completion)

Assume the induced residual host has an owner-slot matching `F_res` which

1. saturates every residual upper colour;
2. saturates every residual owner slot; and
3. has a physical forest projection.

Then activating all `C` packets in (0.4) gives an owner-slot matching `F`
such that

1. every upper colour in `mathcal U` occurs exactly once;
2. every selected lower colour is distinct;
3. every physical owner has degree at most two;
4. the physical projection is a linear forest of order `U`; and
5. that forest has exactly `C` components.

#### Proof

Before activation, adjoin the `C` off providers `f_S` to `F_res`.  The
resource reservation makes this an owner-slot matching.  Its order is

\[
                     (U-2C)+C=U-C.                              \tag{5.1}
\]

Its upper colours are every member of `mathcal U` except the target bank
`az beta(P)`.

Activate every packet.  Theorem 2.1 proves that the simultaneous exchange
is resource-disjoint.  Each activation retains its auxiliary upper and old
lower colour, adds its target upper and new lower colour, retains one slot
at each old provider endpoint, and consumes the reserved slots at its
`B,D` endpoints.  The final order is

\[
                              U-C+C=U.                           \tag{5.2}
\]

The upper rows partition into residual, auxiliary and target banks of
orders `U-2C,C,C`, proving exact upper coverage.  The lower banks are
disjoint by Theorem 2.1 and by the residual deletion.

By Lemma 4.1, before activation `F_res` is a `C`-path forest with endpoints
`B cup D`, while each off provider `A---C_0` is an isolated edge.  The
activation deletes that isolated edge and adds

\[
                         C_0---B,\qquad A---D.                   \tag{5.3}
\]

Thus `A,C_0` become new leaves at two old path endpoints.  No cycle or
degree-three vertex is created, even when `B,D` belong to the same
residual path.  Every residual path remains one path, so the final graph
has exactly `C` components. \(\square\)

### Remark 5.2 (all ordinary Hall rows have disappeared)

The theorem does not ask for a post hoc target/provider matching.  The
maps `beta,sigma` already give the target, lower, `B` and `D` tickets
bijectively.  Nor is there a later component connector matching: balanced
slot saturation makes `B cup D` the endpoint bank automatically, and the
packet activations are leaf extensions.

## 6. The exact remaining owner theorem

The construction reduces odd owner synchronization to:

> **Balanced residual forest lemma.**  For a spread packet bank `P` from
> Theorem 3.2, the induced host obtained by deleting the two upper banks,
> two lower banks and the `6C` declared slot vertices has a matching which
> saturates every residual upper and owner-slot vertex and whose physical
> projection is a forest.

The scalar and asymptotic rows are exact:

\[
 |\mathcal U_{res}|=U-2C,qquad
 |\mathcal S_{res}|=2(U-2C),qquad
 |\mathcal L_{res}|=W-2C=|\mathcal U_{res}|+C,      \tag{6.1}
\]

and Theorem 3.2 gives asymptotic regularity.  Corollary 3.3 misses only
`o(W)` atoms.  What remains is integral exact saturation plus acyclicity;
neither follows from Delcourt--Postle.

This is strictly sharper than the earlier arbitrary-leave cover-down
problem.  The zero shore is now deliberately covered by the residual
forest, while the leave, its providers, both new capacity resources and
the complete endpoint bank are chosen in advance by one Catalan packet
system.

## 7. Exact residual integer system and black-box scope

Let `H_res` be the residual owner-slot host, and for an atom `e` let
`pi(e)` be its unordered physical Johnson edge.  The balanced residual
forest lemma is exactly feasibility of the following zero-one system:

\[
\begin{aligned}
 &\sum_{e\ni R}x_e=1
       &&(R\in\mathcal U_{res}),\\
 &\sum_{e\ni L}x_e\le1
       &&(L\in\mathcal L_{res}),\\
 &\sum_{e\ni s}x_e\le1
       &&(s\in\mathcal S_{res}),\\
 &\sum_{e:\,\pi(e)\subseteq X}x_e\le |X|-1
       &&(\varnothing\ne X\subseteq\mathcal M),\\
 &x_e\in\{0,1\}.                                    \tag{7.1}
\end{aligned}
\]

Here the third row is equality automatically.  The first row selects
`|U_res|` atoms, every atom uses two distinct slots, and
`|S_res|=2|U_res|`; hence slot injectivity uses every residual slot.  The
fourth row is exactly graphic independence of the physical projection.

This formulation shows precisely where the two standard black boxes stop.

### Delcourt--Postle

Theorem 3.2 supplies its asymptotic regularity and codegree hypotheses, and
bounded physical cycles may be put in the conflict system.  The conclusion
is nevertheless only a matching of order

\[
                         |\mathcal U_{res}|-o(W),     \tag{7.2}
\]

not equality in the first and third rows of (7.1).  The theorem has no
prescribed endpoint-saturation conclusion.  Thus another invocation of the
same colouring theorem cannot prove the balanced residual forest lemma.

### Ordinary matroid intersection

The slot-injectivity row of (7.1) is already a graph-matching independence
system on the slot vertices, not a matroid.  The standard exchange failure
is a three-edge slot path

\[
                        s_0s_1,\quad s_1s_2,\quad s_2s_3.        \tag{7.3}
\]

The middle edge is an independent set of order one; the two outside edges
form an independent set of order two; neither outside edge augments the
middle one.  Literal Johnson realizations with distinct upper and lower
colours exist for `m>=4`: for an `(m-2)`-core `K` and distinct
`p,q,a,b,c` outside it, use consecutive owners

\[
 Kpa,\quad Kpb,\quad Kqb,\quad Kqc.                \tag{7.4}
\]

Their three intersections and unions are pairwise distinct.  Choosing the
shared slot at each internal owner realizes (7.3).

Therefore the resource rows are not one matroid to be intersected with the
graphic matroid.  If tail and head roles are split artificially, they
become several partition matroids, still accompanied by the upper, lower
and graphic rows.  The ordinary two-matroid intersection theorem does not
apply.

The exact missing theorem is consequently an integral **coloured
linear-factor** theorem for the specially punctured Boolean host (7.1), or
an absorber which upgrades (7.2) to (7.1).  All scalar balances, local
degrees, target tickets and final component counts are already exact.
