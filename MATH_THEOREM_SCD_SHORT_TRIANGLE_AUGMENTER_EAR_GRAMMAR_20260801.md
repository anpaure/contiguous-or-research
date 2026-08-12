# The tight augmenter turns every SCD short triangle into a two-stage Catalan ear

Date: 2026-08-01  
Lane: SCD multi-funnel / tight odd-diamond augmenter / rooted owner forest  
Status: unconditional local algebra, exact colour image and multiplicities,
exact endpoint ledger, and an exact SDR/forest reduction.  The square-SDR
and recursive long-core completion are not proved in all dimensions.

## 0. Outcome

Let

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad |G|=2m-3,
\]

and use the four-row Greene--Kleitman matching `M_0` from the SCD funnel
theorem.  A short central chain is

\[
                         S<L=S+x,
 \qquad |S|=m-2.                                      \tag{0.1}
\]

Put

\[
 A_S=aS,\qquad B_S=zS,\qquad C_S=L.                  \tag{0.2}
\]

The rooted triangle

\[
 C_S\longrightarrow A_S\longrightarrow B_S
       \longrightarrow C_S                                  \tag{0.3}
\]

is monochromatic of upper colour `azL`.  The tight one-to-two augmenter
acts on it literally as a rotation.

For every `b in G-L`, the first rotation is

\[
 \boxed{
 C_S\to A_S\ [azL]
 \quad\rightsquigarrow\quad
 A_S\to B_S\ [azL]
 \; + \;
 C_S\to P(L+b)\ [z(L+b)], }
                                                               \tag{0.4}
\]

where `P(U)=M_0^{-1}(U)`.  The second rotation is

\[
 \boxed{
 A_S\to B_S\ [azL]
 \quad\rightsquigarrow\quad
 B_S\to C_S\ [azL]
 \; + \;
 A_S\to Q(S+b)\ [a(L+b)], }
                                                               \tag{0.5}
\]

where `Q(V)=M_0^{-1}(aV)`.  Taking the same `b` in both steps gives the
paired Boolean-square ear

\[
 \boxed{
 \{C_S\to A_S\}
 \rightsquigarrow
 \{B_S\to C_S\to P(U),\ A_S\to Q(V)\}, }
 \qquad
 U=L+b,\quad V=S+b.                                  \tag{0.6}
\]

Its three upper colours are exactly

\[
                         azL,\qquad zU,\qquad aU.    \tag{0.7}
\]

The physical support in (0.6) is the disjoint union of a two-edge path and
an edge.  A third rotation inside the same triangle is impossible: after
(0.6), all three lower/tail resources `C_S,A_S,B_S` are occupied, whereas
the third augmenter would have to reuse `C_S`.

For the standard Greene--Kleitman short bank, the union of all possible
new `z`-colours, and separately of all possible new `a`-colours, has the
exact order

\[
 \boxed{
 \left|\bigcup_{S<L}\{z(L+b):b\in G-L\}\right|
 =\left|\bigcup_{S<L}\{a(L+b):b\in G-L\}\right|
 =I_m=\operatorname {Cat}_m-2\operatorname {Cat}_{m-1}. }
                                                               \tag{0.8}
\]

Thus the colour image of the local augmenter is *exactly* the internal
Catalan-convolution mass already isolated by the multi-funnel recurrence.
This is an equality of literal colour families, not only a scalar analogy.

The strongest clean global reduction is a square-SDR.  One must choose one
incidence `L subset U` for every serviced short triangle so that both `U`
and `V=U-x` are injective and the induced short-to-short arcs are acyclic.
Under those conditions the paired ears are resource-disjoint and form a
physical linear forest.  They do not by themselves form a short-core
Hamilton path: every first rotation exits to a long-chain root.  The exact
remaining positive object is therefore a recursive ear forest through the
long SCD core, not another ordering of the short triangles alone.

## 1. The frozen four-row matching

For a short chain (0.1), the four-row matching gives

\[
 M_0(A_S)=aL,\qquad M_0(B_S)=azS,\qquad M_0(C_S)=zL. \tag{1.1}
\]

Consequently the three arcs in (0.3) have physical owner edges

\[
 aL\,azS,\qquad azS\,zL,\qquad zL\,aL               \tag{1.2}
\]

and common union `azL`.

Every rank-`m` set `U subset G` lies in a long SCD chain and has a unique
rank-`(m-1)` predecessor `P(U)` with

\[
                         M_0(P(U))=U.                \tag{1.3}
\]

For every rank-`(m-1)` `V subset G`, write `p(V)` for the rank-`(m-2)`
member immediately below it in its central SCD segment.  The third row of
the matching gives

                         Q(V)=a\,p(V),
 \qquad                  M_0(Q(V))=aV.              \tag{1.4}

If `V=L_T` is the top of another short chain, then `Q(V)=A_T`.

## 2. First rotation: the requested substitution off `C_S -> A_S`

Fix `b in G-L`.  In the notation of the tight augmenter, substitute

\[
 \widehat L=L,\qquad
 \widehat a=z,\qquad
 \widehat b=b,\qquad
 \widehat c=a,\qquad
 \widehat x=x=L-S.                                  \tag{2.1}
\]

The auxiliary colour is `azL`, and the three relevant owner labels are

\[
 \widehat A=zL=M_0(C_S),\qquad
 \widehat C=aL=M_0(A_S),\qquad
 \widehat D=azS=M_0(B_S).                           \tag{2.2}
\]

Moreover

\[
 \widehat L'=(L-x)+a=aS=A_S,\qquad
 \widehat R=L+z+b=z(L+b).                           \tag{2.3}
\]

The new target owner is `L+b`, whose rooted head is `P(L+b)`.  Substitution
in the one-to-two identity now gives exactly (0.4).

### Theorem 2.1 (first SCD rotation)

The replacement (0.4) is a legal fixed-`M_0` one-to-two augmentation.  It
retains the old colour `azL`, adds the colour `z(L+b)`, consumes exactly

* the unused lower/tail ticket `A_S` at the terminal of `C_S -> A_S`;
* the incoming/head ticket of `B_S`; and
* the incoming/head ticket of `P(L+b)`.

The old lower/tail `C_S` remains occupied throughout.  On physical owners,

\[
                         zL-aL
 \quad\rightsquigarrow\quad
                         aL-azS\quad+\quad zL-(L+b). \tag{2.4}
\]

If the original provider, `B_S`, and `P(L+b)` are isolated components,
then (2.4) is automatically a linear forest and lowers their total
component count by one.

#### Proof

Equations (2.1)--(2.3) verify every set in the tight augmenter literally.
The fixed-phase rows are `M_0(L)=zL` and `M_0(aS)=aL`.  The rerouted
auxiliary edge has owners `aL,azS`, hence roots `A_S,B_S`; the target edge
has owners `zL,L+b`, hence roots `C_S,P(L+b)`.  The ticket and topology
statements follow directly. \(\square\)

## 3. Second rotation and the paired square

Starting from the auxiliary edge `A_S -> B_S`, use

\[
 \widehat L=aS,\qquad
 \widehat a=x,\qquad
 \widehat b=b,\qquad
 \widehat c=z,\qquad
 \widehat x=a.                                      \tag{3.1}
\]

Then

\[
 \begin{array}{lll}
 \widehat A=aL=M_0(A_S),&
 \widehat C=azS=M_0(B_S),&
 \widehat D=zL=M_0(C_S),\\
 \widehat L'=zS=B_S,&
 \widehat R=a(L+b),&
 \widehat B=a(S+b).
 \end{array}                                        \tag{3.2}

This proves (0.5).

### Theorem 3.1 (paired-square ear)

For one `b in G-L`, put `U=L+b` and `V=S+b`.  Applying (0.4), followed by
(0.5), replaces the one-edge provider by (0.6).  The physical edges are

\[
                         azS-zL-U,
 \qquad                  aL-aV.                     \tag{3.3}

They form a linear forest.  The three colours in (0.7) are distinct, and
all old physical owner resources survive.

No third rotation of the surviving `azL` occurrence is legal in the same
tail matching.  Such a rotation would replace `B_S -> C_S` by an auxiliary
copy with tail `C_S`, but `C_S` is already the tail of `C_S -> P(U)`.

#### Proof

The first two assertions are (2.4) and (3.2).  The five owner labels in
(3.3) are distinct by their `{a,z}` signatures, except for the deliberate
shared vertex `zL`; its physical degree is two.  Hence (3.3) is a path plus
an edge.  The final tail set is exactly

\[
                         \{A_S,B_S,C_S\},            \tag{3.4}
\]

which proves the saturation assertion. \(\square\)

## 4. Exact component-ticket ledger

Let `P=P(U)` and `Q=Q(V)`.  The directed role ledger is

\[
\begin{array}{c|c|c|c}
\text{state}&\text{selected arcs}&\text{used tails}&\text{used heads}\\ \hline
0&C\to A&\{C\}&\{A\}\\
1&C\to P,\ A\to B&\{C,A\}&\{P,B\}\\
2&C\to P,\ A\to Q,\ B\to C&\{C,A,B\}&\{P,Q,C\}.
\end{array}                                         \tag{4.1}
\]

Thus the first rotation consumes **exactly** the unused lower/tail ticket
at the old terminal `A`; the second consumes exactly the corresponding
terminal tail ticket `B` of the rerouted auxiliary component.  Every tail
used at an earlier stage remains used.

For literal component endpoints:

* state 0 has the path `C -> A` and isolated `B,P,Q`;
* state 1 has paths `C -> P` and `A -> B`;
* state 2 has paths `B -> C -> P` and `A -> Q`.

The old source ticket at `C` is preserved by the first rotation and
consumed by the second edge `B -> C`.  The old terminal ticket at `A` is
consumed by the first rotation, while the old used incoming role at `A` is
released and becomes the source ticket of `A -> B` or `A -> Q`.  Therefore
the move preserves the lower-tail ledger monotonically, but it does **not**
preserve both free path endpoints literally.  Any global connector argument
must use the endpoint transformation in (4.1), not merely the component
count.

## 5. The exact new-colour image is the internal Catalan bank

Let `mathcal L_sh` be the standard Greene--Kleitman family of short tops in
`B_G`, and put

\[
                         \mathcal U_sh=\partial^+\mathcal L_sh
 \subseteq {G\choose m}.                            \tag{5.1}
\]

Equations (0.4)--(0.5) give the literal colour families

\[
 \mathcal Z=z\mathcal U_sh,
 \qquad
 \mathcal A=a\mathcal U_sh.                         \tag{5.2}
\]

They are disjoint because of their `{a,z}` signatures.

### Theorem 5.1 (Catalan image identity)

For every `m>=3`,

\[
 \boxed{
 |\mathcal U_sh|
 ={2m-3\choose m-3}-{2m-3\choose m-4}
 =\operatorname {Cat}_m-2\operatorname {Cat}_{m-1}
 =I_m. }                                             \tag{5.3}
\]

#### Proof

Encode a subset of the ordered ground `G` by a walk, giving an absent
coordinate step `+1` and a present coordinate step `-1`.  A rank-`(m-1)`
word is a Greene--Kleitman short top exactly when its total is `-1` and its
minimum prefix sum is `-1`.

A rank-`m` word `U` has total `-3`.  It contains a short top exactly when
its minimum prefix sum is `-3`.  Indeed, if its minimum is `-3`, flip any
down-step no later than the first visit to level `-2`; before the flip the
walk has not gone below `-1`, and after the flip every suffix is raised by
two, so the resulting word is a short top.  Conversely, reversing such a
flip lowers a suffix of a short-top walk by two and can never go below
`-3`.

Reverse the walk and negate its steps.  Rank-`m` words of minimum `-3`
become paths from zero to three which stay nonnegative.  The ballot/reflection
count is

\[
 {4\over m+1}{2m-3\choose m-3}
 ={2m-3\choose m-3}-{2m-3\choose m-4}.              \tag{5.4}
\]

Using

\[
 {2m-3\choose m-3}={m-2\over2}\operatorname {Cat}_{m-1}
\]

reduces (5.4) to the middle expression in (5.3). \(\square\)

### Theorem 5.2 (exact occurrence multiplicity)

For `U in mathcal U_sh`, let `tau(U)` be the first time its walk reaches
level `-2`.  The number of short triangles capable of producing either
new colour `zU` or `aU` is

\[
 \boxed{
 \mu(U)=\#\{L\in\mathcal L_sh:L\subset U\}
       ={\tau(U)\over2}+1. }                         \tag{5.5}
\]

In particular

\[
 2\le\mu(U)\le m-1,
 \qquad
 \sum_{U\in\mathcal U_sh}\mu(U)
       =(m-2)\operatorname {Cat}_{m-1},              \tag{5.6}
\]

and the mean multiplicity is

\[
                         {m+1\over2}.                \tag{5.7}
\]

#### Proof

Deleting a present coordinate from `U` gives a short top precisely when
that down-step occurs no later than the first visit to `-2`.  Before that
visit the old prefix is at least `-1`; afterward the flip raises the walk
by two.  At time `tau`, if there were `u` up-steps and `d` down-steps, then
`d-u=2` and `tau=u+d`; hence `d=tau/2+1`.  This proves (5.5).  The bounds
are sharp.  Summing incidences instead over the short tops gives
`(m-2)Cat_(m-1)`, because every short top has exactly `m-2` rank-`m`
extensions.  Divide by (5.3) to obtain (5.7). \(\square\)

The equality `|mathcal U_sh|=I_m` is the promised comparison with the
multi-funnel recurrence: the residual internal convolution is exactly the
image of one SCD short-triangle augmenter phase.

## 6. Exact SDR and forest conditions

### 6.1 One rotation

For a source family `X subseteq mathcal L_sh` and a forbidden/free-bulk
upper bank `F subseteq mathcal U_sh`, make the graph

\[
 L\sim U
 \quad\Longleftrightarrow\quad
 L\subset U,\quad U\notin F.                        \tag{6.1}
\]

Because `U` determines both the new colour `zU` and the rooted head
`P(U)`, one first-stage ear per source can be selected resource-disjointly
if and only if

\[
 \boxed{
 |\partial^+Y\setminus F|\ge |Y|
 \qquad\text{for every }Y\subseteq X. }              \tag{6.2}
\]

This is ordinary Hall and is exact.  If every `P(U)` is an isolated/free
component, the selected ears are automatically a physical linear forest.

The full standard short bank fails even the total cut at `m=3,4`:

\[
 (c,I_m)=(2,1),(5,4).                                \tag{6.3}
\]

For `m>=5`, the total cut passes because

\[
                         {I_m\over c}
 ={2(m-2)\over m+1}\ge1.                            \tag{6.4}
\]

Equation (6.4) alone is not Hall; the subset inequalities in (6.2) remain
load-bearing.  The exact audit accompanying this note finds saturating
matchings for the standard bank through `5<=m<=11`, but no all-`m` proof is
claimed here.

### 6.2 Two rotations: the square-SDR

For every short chain `S<L=S+x`, and every `b in G-L`, form the bipartite
edge

\[
 U=L+b\quad--\quad V=S+b=U-x,                       \tag{6.5}
\]

and colour it by the source short chain `S<L`.  A **square-SDR** is a
rainbow matching containing one edge of every serviced source colour.

Equivalently, it is a choice `b(S)` such that simultaneously

\[
 U_S=L_S+b(S)\text{ are distinct},
 \qquad
 V_S=S+b(S)\text{ are distinct}.                    \tag{6.6}
\]

This is the exact non-graphic resource condition for pairwise-disjoint
paired ears: `U_S` indexes both new upper colours and the `P` head, while
`V_S` indexes the `Q` head.  The two projection Hall systems

\[
 \left|\bigcup_{S\in X}\{L_S+b:b\in G-L_S\}\right|\ge|X|,
 \quad
 \left|\bigcup_{S\in X}\{S+b:b\in G-L_S\}\right|\ge|X|        \tag{6.7}
\]

are necessary but, by themselves, do not remove the three-partite
correlation in (6.6).  The square-SDR is the sharp literal condition.

For a chosen square-SDR, draw an arc `S -> T` exactly when `V_S=L_T` is
the top of another selected short chain.  If `V_S` belongs to a long
central chain, regard the arc as exiting the short bank.

### Theorem 6.1 (paired-ear forest criterion)

A square-SDR lifts to a resource-disjoint physical linear forest of paired
ears if and only if the induced directed graph on the short chains has no
directed cycle.  In that forest every serviced block is replaced by the
two paths in (0.6), and all `3|X|` displayed upper colours are distinct.

#### Proof

The `U` injection makes the `P(U)` heads and both `aU,zU` colour banks
injective.  The `V` injection makes the `Q(V)` heads injective.  Coordinate
signatures separate every other resource class.  The `B-C-P` paths always
exit to long-chain `P` roots, so they cannot cycle inside the selected
bank.  The only possible inter-gadget continuation is

\[
                         A_S\to Q(V_S)=A_T,
\]

which is exactly the displayed short-chain arc.  Hence cycles agree
bijectively. \(\square\)

With a background forest present, the same statement holds after
contracting its components: the square-SDR edges must be independent in
the contracted graphic matroid.  This is precisely the serial two-union--
find condition, now written on the SCD ear grammar.

## 7. Recursive-ear conclusion and Hamilton scope

The first rotation cannot connect directly to another short-triangle root.
Its new owner `U=L+b` contains neither `a` nor `z`, and (1.3) says its head
`P(U)` is the central top root of a **long** SCD chain.  It therefore differs
from every short `A_T,B_T,C_T` by either its chain type or its `{a,z}`
signature.

Consequently no nonempty family of first rotations can, by itself, be a
Hamilton path on the `3c` short-triangle vertices.  Even if the `A`-arcs of
a square-SDR form one Hamilton path on all short blocks, the result still
contains the exported paths

\[
                         B_S\to C_S\to P(U_S)        \tag{7.1}
\]

ending in the long core.

This is not merely a failure.  Equations (0.6) and (7.1) give a positive
recursive grammar:

\[
 \boxed{
 \text{short triangle }(S<L)
 \longmapsto
 \bigl(B_S-C_S-P(U)\bigr)
 \sqcup
 \bigl(A_S-Q(V)\bigr), }
                                                               \tag{7.2}
\]

where the two exits are the predecessor ports of the Boolean square

\[
                         S<L,\quad S<V,\quad L,V<U.  \tag{7.3}
\]

The exact next theorem is therefore:

> **Recursive square-ear completion.**  Choose a square-SDR satisfying
> Theorem 6.1, then continue the exported long-chain ports by the same
> prospective owner/upper rules so that all remaining upper colours are
> represented and the contracted ear graph is one rooted path.

If that theorem holds around the protected pivot, the tight augmenters
turn the SCD shell into an upper-exact physical linear forest before the
separate final Catalan connector step.  What is now ruled out is the
stronger hope that rotating only within the disjoint short triangles
already Hamiltonizes their core.

## 8. Audit artifact

`scratch/audit_scd_short_augmenter_ear_20260801.cpp` independently
enumerates the standard short chains, their two colour images, the exact
phase-one Hall matching number, and the alternate-top matching number.
It is a deterministic `-O3` C++ audit, not a search used in any proof.
For `m=3,...,11` it reports

\[
\begin{array}{c|rrrrrrrrr}
m&3&4&5&6&7&8&9&10&11\\ \hline
c&2&5&14&42&132&429&1430&4862&16796\\
|\mathcal U_sh|&1&4&14&48&165&572&2002&7072&25194\\
\nu(\mathcal L_sh,\mathcal U_sh)&1&4&14&42&132&429&1430&4862&16796.
\end{array}                                         \tag{8.1}
\]

The first two failures are forced by (6.3).  The later matching values are
finite evidence only; the proof-safe all-dimensional statement is Hall
(6.2), followed by the square-SDR and acyclicity conditions of Theorem 6.1.
