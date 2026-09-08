# The decorated-SCD gate at the top tag: common-base rigidity and recursive packets

Date: 2026-07-25

Method: pure mathematics only. No search, computation, or generic
discrepancy rounding is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 H=\lceil A\sqrt m\rceil .
\]

The decorated-SCD bridge gate \(\mathrm{EP}_A\) from
ROTOR_MULTI_FRAME_PACKET_RESOLUTION_20260725.md is not proved here.
The bridge-one classification does, however, give an exact rigidity theorem
for the tag-\(H\) chains, the only chains having no collar-extension freedom:

\[
 \boxed{\text{on two distinct tag-\(H\) chains of one SCD,
 bridge one is equivalent to a genuine radius-\(H\) rotor arc.}}
 \tag{0.1}
\]

Singleton promotion does not enlarge the induced graph on the top tag. It
preserves the full rank-\(m+H\) endpoint, which two distinct chains of an
SCD cannot share. Identity is equally impossible. Thus the bridge
relaxation is useful only through lower-tag collars and through edges joining
different tags; it gives no new top-tag adjacency.

This has two consequences.

First, if \(\lambda_H(\mathcal D)\) is the maximum number of edges in a
directed vertex-disjoint rotor path forest on the tag-\(H\) class of a
clipped SCD \(\mathcal D\), then every bridge-one path cover of the decorated
SCD with \(p\) components satisfies

\[
 \boxed{
 p\ge
 \bigl(2N_H-W-\lambda_H(\mathcal D)\bigr)_+.}
 \tag{0.2}
\]

For \(A<\sqrt{\log2}\), the term \(2N_H-W\) is a positive linear fraction
of \(W\). Hence \(\mathrm{EP}_A\) forces a positive-density family of actual
top-tag rotor edges. In particular the BTK SCD, whose positive-radius
induced rotor graphs are empty, cannot satisfy \(\mathrm{EP}_A\) in this
range, regardless of how all lower tags are decorated.

Second, every recursive radius-\(H\) cube packet is exactly the right local
top-tag atom: its \(2\ell\) chains form one bridge-one rotor cycle. If the
tag-\(H\) class of one SCD could be tiled by mask-disjoint recursive packets,
then cutting one edge per packet would give only

\[
 \frac{N_H}{2\ell}=O(W/m)=o(W/H)
 \tag{0.3}
\]

top-tag components when \(m/2<\ell\le m\). The obstacle is not local
adjacency. It is exact common-base completion: choose those packets so that
all their lower and upper endpoint colors are globally injective at every
recursive layer and the remaining masks complete to the lower tag classes
of the same SCD.

The exact layerwise condition is the forced-target agreement of two Boolean
perfect matchings. At layer \(h\), a retained rotor edge \(e:v\to w\) lifts
if and only if the lower endpoint matching at \(v\) and the upper-complement
matching at \(w\) take two prescribed values \(\lambda(e)\) and \(\rho(e)\).
Thus a viable recursive construction must solve one compatible sequence of
these common-base matching problems with total edge loss \(o(W/H)\).

Stationary common-base constructions are ruled out at the top tag: fixing
either the lower base or the upper carrier yields no edge between distinct
tag-\(H\) chains. The surviving construction must transport both extremal
bases by genuine rotor shifts, exactly as the recursive cube packet does.

## 1. Tag-\(H\) states and their extremal bases

Let \(\mathcal D\) be a saturated SCD of the central band
\(m-H,\ldots,m+H\). Its clipped radius census is

\[
 \gamma_d=N_d-N_{d+1}\quad(0\le d<H),
 \qquad
 \gamma_H=N_H.
 \tag{1.1}
\]

A tag-\(H\) chain state is

\[
 \omega=(L;z_1,\ldots,z_{2H};R),
 \qquad |L|=|R|=m-H.
 \tag{1.2}
\]

Write

\[
 Z(\omega)=\{z_1,\ldots,z_{2H}\},
 \qquad
 X(\omega)=L+\{z_1,\ldots,z_H\}
 \tag{1.3}
\]

for its middle owner, and define its two extremal band masks by

\[
 B(\omega)=L,
 \qquad
 T(\omega)=L+Z(\omega)=[2m]\setminus R.
 \tag{1.4}
\]

Thus \(B(\omega)\) has rank \(m-H\) and \(T(\omega)\) has rank \(m+H\).
Only tag-\(H\) chains meet either boundary rank. Since \(\mathcal D\)
partitions the band, the maps

\[
 \omega\longmapsto B(\omega),
 \qquad
 \omega\longmapsto T(\omega)
 \tag{1.5}
\]

are bijections from \(\mathcal D_H\) onto the two boundary ranks. In
particular,

\[
 |\mathcal D_H|=N_H.
 \tag{1.6}
\]

There is no decoration choice on this class. A tag-\(d\) state with \(d<H\)
has

\[
 \bigl((m-d)_{H-d}\bigr)^2
\]

radius-\(H\) extensions, whereas a tag-\(H\) state has exactly one.

## 2. The bridge-one relaxation vanishes on the top tag

For a complete radius-\(H\) useful state, the bridge-one classification has
three cases:

\[
 \begin{array}{ll}
 \text{identity:}&
 L'=L,\quad z'_1,\ldots,z'_{2H}=z_1,\ldots,z_{2H};\\[2mm]
 \text{rotor shift:}&
 L'=L-x+y,\quad
 (z'_1,\ldots,z'_{2H})=(x,z_1,\ldots,z_{2H-1}),\\
 &x\in L,\ y\in R;\\[2mm]
 \text{promotion:}&
 L'=L-x+z_j,\quad
 (z'_1,\ldots,z'_{2H})
 =(x,z_1,\ldots,\widehat z_j,\ldots,z_{2H}),\\
 &x\in L,\quad1\le j\le2H.
 \end{array}
 \tag{2.1}
\]

### Theorem 2.1 (top-tag bridge rigidity)

Let \(\omega,\omega'\in\mathcal D_H\) be distinct tag-\(H\) states of one
clipped SCD. Then

\[
 \omega\longrightarrow\omega'
 \text{ is bridge one}
 \quad\Longleftrightarrow\quad
 \omega\longrightarrow\omega'
 \text{ is a radius-\(H\) rotor arc.}
 \tag{2.2}
\]

Equivalently, the bridge-one digraph induced by \(\mathcal D_H\) is exactly
the radius-\(H\) rotor digraph induced by \(\mathcal D_H\).

#### Proof

In the identity case of (2.1), the useful prefixes agree. Their complements
determine the same residual set \(R\), so the two complete tag-\(H\) states
are equal, contrary to the hypothesis.

In the promotion case,

\[
 \begin{aligned}
 T(\omega')
 &=L-x+z_j+\{x,z_1,\ldots,\widehat z_j,\ldots,z_{2H}\}\\
 &=L+\{z_1,\ldots,z_{2H}\}
 =T(\omega).
 \end{aligned}
 \tag{2.3}
\]

The boundary bijection (1.5) forbids two distinct tag-\(H\) chains from
sharing this rank-\(m+H\) mask. Hence promotion is impossible.

The only remaining case is the rotor shift, which is exactly the
radius-\(H\) rotor rule. Conversely every such rotor shift is case two of
the bridge-one classification. \(\square\)

The proof uses the full top endpoint, not merely the first-band union. This
is why collar freedom at lower tags cannot repair the induced top-tag graph.

### Corollary 2.2 (stationary common-base no-go)

No bridge-one arc joins two distinct tag-\(H\) chains while keeping either
of the following fixed:

1. the lower base \(B=L\);
2. the upper carrier \(T=L+Z\).

#### Proof

If \(L'=L\), (2.1) leaves only identity. If \(T'=T\), the only additional
case is promotion, excluded by Theorem 2.1. \(\square\)

Thus a common-base recursion which holds one extremal base stationary cannot
produce even one top-tag edge. On an actual rotor shift,

\[
 B'=B-x+y,
 \qquad
 T'=T-z_{2H}+y.
 \tag{2.4}
\]

Both bases must move coherently.

## 3. A quantitative necessary condition for \(\mathrm{EP}_A\)

Let \(\lambda_H(\mathcal D)\) be the maximum number of edges in a directed
vertex-disjoint path forest in the induced rotor graph on
\(\mathcal D_H\).

### Theorem 3.1 (top-tag density bound)

If a decoration of \(\mathcal D\) has a bridge-one path cover with \(p\)
components, then

\[
 \lambda_H(\mathcal D)\ge 2N_H-W-p,
 \tag{3.1}
\]

or equivalently (0.2).

#### Proof

Read each path of the cover as a word over the alphabet
\(\{\mathsf H,\mathsf O\}\), according as a vertex has tag \(H\) or a
smaller tag. Let \(r_H\) be the total number of nonempty \(\mathsf H\)-runs.
Every \(\mathsf O\)-vertex can separate at most two neighboring
\(\mathsf H\)-blocks, and each of the \(p\) paths contributes at most one
initial \(\mathsf H\)-run. More directly, path by path,

\[
 \#\{\mathsf H\text{-runs}\}
 \le \#\{\mathsf O\text{-vertices}\}+1.
\]

Summing gives

\[
 r_H\le (W-N_H)+p.
 \tag{3.2}
\]

The number of cover arcs with both ends tagged \(H\) is exactly

\[
 e_{HH}=N_H-r_H
 \ge2N_H-W-p.
 \tag{3.3}
\]

Those arcs form a vertex-disjoint directed linear forest. By Theorem 2.1
they are genuine radius-\(H\) rotor arcs, so
\(e_{HH}\le\lambda_H(\mathcal D)\). This proves (3.1). \(\square\)

For fixed \(A\),

\[
 \frac{N_H}{W}=e^{-A^2+o(1)}.
 \tag{3.4}
\]

Hence:

### Corollary 3.2 (small-window hard core)

If \(0<A<\sqrt{\log2}\) and \(\mathrm{EP}_A\) holds, its SCD must satisfy

\[
 \lambda_H(\mathcal D)
 \ge
 \bigl(2e^{-A^2}-1-o(1)\bigr)W.
 \tag{3.5}
\]

In particular, any SCD whose tag-\(H\) induced rotor graph has \(o(W)\)
edges cannot satisfy \(\mathrm{EP}_A\) in this range.

The BTK SCD has no positive-radius induced rotor edges. Therefore:

### Corollary 3.3 (BTK orbit no-go for \(\mathrm{EP}_A\))

For every fixed \(0<A<\sqrt{\log2}\), no coordinate relabeling of the BTK
SCD, and no choice of collars on its lower tags, satisfies
\(\mathrm{EP}_A\).

This is stronger than a toll comparison for BTK: it is a direct bridge-path
cover obstruction.

For \(A\ge\sqrt{\log2}\), the binary run count (3.1) is silent because the
lower tags are numerous enough to separate all top-tag vertices in
principle. It neither proves nor disproves \(\mathrm{EP}_A\) there.

## 4. Recursive packets are exact positive top-tag atoms

Let \(\ell\) be a power of two with \(H\le\ell/2\). A recursive cube cycle
gives tag-\(H\) states

\[
 \omega_0,\ldots,\omega_{2\ell-1}
 \tag{4.1}
\]

whose chains are pairwise mask-disjoint and whose states form a directed
radius-\(H\) rotor cycle.

### Proposition 4.1 (packet path-cover ledger)

Suppose a clipped SCD \(\mathcal D\) contains a mask-disjoint collection
\(\mathscr Q\) of recursive radius-\(H\) packets. Let \(S\) be the set of
tag-\(H\) chains not contained in these packets. Then the induced
bridge-one graph on \(\mathcal D_H\) has a spanning path forest with at most

\[
 |\mathscr Q|+|S|
 \tag{4.2}
\]

components.

#### Proof

Cut one rotor edge in every packet cycle and retain all other packet edges.
Theorem 2.1 makes them bridge-one edges of \(\mathcal D\). Insert the states
in \(S\) as singletons. \(\square\)

If the packets cover all tag-\(H\) chains and all have \(R=2\ell\) states,
then

\[
 |\mathscr Q|=\frac{N_H}{R}.
 \tag{4.3}
\]

For the largest power of two \(\ell\le m\), one has \(R\ge m+1\), and

\[
 \frac{N_H}{R}=O_A(W/m)=o_A(W/H).
 \tag{4.4}
\]

Thus recursive packets solve the top-tag path-cover scale with room to
spare. The unresolved part is placing a one-fold packet family inside one
SCD.

### Definition 4.2 (recursive-packet extension gate)

Let \(\mathrm{RPE}_{A}^{H}\) be the following statement.

There is a collection of recursive radius-\(H\) packets such that:

1. their chains are pairwise disjoint as Boolean mask sets;
2. their lower endpoints partition \(\binom{[2m]}{m-H}\);
3. their upper endpoints partition \(\binom{[2m]}{m+H}\); and
4. after removing every packet chain, the remaining masks in the central
   band admit a saturated symmetric-chain decomposition with tags below
   \(H\).

### Proposition 4.3

\(\mathrm{RPE}_{A}^{H}\) produces a clipped SCD whose tag-\(H\) class has
a bridge-one path cover with \(O_A(W/m)=o_A(W/H)\) components.

#### Proof

Items 1--4 give the clipped SCD. Items 2--3 and the boundary census imply
that its tag-\(H\) class consists exactly of the selected packet chains.
Apply Proposition 4.1 and (4.4). \(\square\)

The outer endpoint partitions in Definition 4.2 are not sufficient by
themselves. Packet chains can still collide at an interior rank, and even a
mask-disjoint partial SCD with the correct leave cardinalities need not
complete. The completion clause is essential.

The exact packet orbit proves a scaled integral multicover by these atoms.
It does not select the one-fold family required by
\(\mathrm{RPE}_{A}^{H}\).

There is also an exact frame requirement. Fix one coordinate perfect
matching. A rank-\(m-H\) target having \(f\) full pairs has count

\[
 T_{f,H}
 =\frac{m!}{f!(f+H)!(m-2f-H)!}\,2^{m-2f-H},
 \tag{4.5}
\]

whereas the number of middle starts of the only source type which can
produce it inside that frame is

\[
 V_f
 =\frac{m!}{f!^2(m-2f)!}\,2^{m-2f}.
 \tag{4.6}
\]

Consequently every tag-\(H\) packet family confined to that frame misses at
least

\[
 D_{m,H}=\sum_f(T_{f,H}-V_f)_+
 =\bigl(e^{-A^2}\Delta(A)+o(1)\bigr)W
 \tag{4.7}
\]

lower boundary masks, where
\(\Delta(A)=\Phi_{\rm G}(A/2)-e^{A^2}\Phi_{\rm G}(-3A/2)>0\).
Thus \(\mathrm{RPE}_{A}^{H}\) must mix coordinate frames; no exact
common-base construction confined to one fixed pair frame can satisfy even
its lower-boundary partition.

## 5. The exact recursive common-base condition

The packet gate can be attacked from the center outward. Suppose an exact
depth-\(h\) band SCD has active top states

\[
 v=(L_v;z_1(v),\ldots,z_{2h}(v);R_v).
 \tag{5.1}
\]

Choose an active set \(A_h\) of exactly \(N_{h+1}\) states to extend to the
next layer. For an inherited rotor edge \(e:v\to w\), using
\(x_e\in L_v\) and \(y_e\in R_v\), define

\[
 \lambda(e)=L_v-\{x_e\},
 \qquad
 \rho(e)=R_v-\{y_e\}.
 \tag{5.2}
\]

Let \(\mathfrak M_-(A_h)\) consist of the perfect matchings

\[
 P^-:A_h\longrightarrow\binom{[2m]}{m-h-1},
 \qquad P^-(v)\subset L_v,
 \tag{5.3}
\]

and define \(\mathfrak M_+(A_h)\) analogously by
\(P^+(v)\subset R_v\).

### Theorem 5.1 (forced common-base agreement)

For fixed \(P^-\in\mathfrak M_-(A_h)\) and
\(P^+\in\mathfrak M_+(A_h)\), an inherited edge \(e:v\to w\) lifts to a
radius-\(h+1\) rotor edge if and only if

\[
 P^-(v)=\lambda(e),
 \qquad
 P^+(w)=\rho(e).
 \tag{5.4}
\]

Consequently, if \(E_h\) is the inherited active edge set and

\[
 M_h^\star
 =\max_{P^-,P^+}
 \left|
 \{e=v\to w\in E_h:
 P^-(v)=\lambda(e),\ P^+(w)=\rho(e)\}
 \right|,
 \tag{5.5}
\]

then the exact minimum number of inherited edges which must be cut at this
layer is

\[
 \boxed{k_h^{\min}=|E_h|-M_h^\star.}
 \tag{5.6}
\]

#### Proof

Extending \(v\) chooses \(\ell_v\in L_v\) and \(u_v\in R_v\), producing
new boundary masks

\[
 P^-(v)=L_v-\{\ell_v\},
 \qquad
 P^+(v)=R_v-\{u_v\}.
 \tag{5.7}
\]

The exact rotor-lift criterion forces

\[
 \ell_v=x_e,
 \qquad
 u_w=z_{2h}(v)
 \tag{5.8}
\]

for \(h\ge1\), with \(u_w=x_e\) at \(h=0\). The first equality is exactly
the lower equation in (5.4). Since

\[
 R_w=R_v-\{y_e\}+\{z_{2h}(v)\},
\]

the second is exactly the upper equation. The remaining exclusion
conditions are automatic from injectivity of the two perfect matchings:
otherwise two sources have the same lower image or two targets the same
upper-complement image. Hence all edges in the agreement set lift
simultaneously, and every exact extension retains only agreement edges.
Maximizing proves (5.6). \(\square\)

This is the exact common-base requirement, not a fractional surrogate. The
two matchings must be chosen on the same active set, their agreement edges
must be retained simultaneously, and the choices must be recursively
compatible with all previous layers.

Within one recursive packet, the \(\lambda\)-colors and the \(\rho\)-colors
of its edges are already injective by the two-sided rainbow theorem. Across
different packets they may collide, and even a maximum collision-free
subfamily need not extend to the two perfect matchings in (5.3). Thus there
are two exact losses:

\[
 \begin{aligned}
 &\text{paired-rainbow loss: forced colors collide across packets},\\
 &\text{Boolean-completion loss: a collision-free forced-color family
   does not extend to }P^-,P^+.
 \end{aligned}
 \tag{5.9}
\]

No stationary-base trick removes either loss, by Corollary 2.2.

## 6. What an exact recursive construction must prove

A natural recursive packet attempt is:

1. start with a two-sided-rainbow Johnson linear forest in the middle rank;
2. choose nested active sets of sizes \(N_1,N_2,\ldots,N_H\);
3. at layer \(h\), choose the two endpoint perfect matchings from
   Theorem 5.1; and
4. retain the inherited path edges on the active set.

To reach the packet scale, the active choices should keep long cyclic or
path intervals together instead of cutting one interval independently in
every layer. Assigning one common final tag to a whole recursive packet
does this: the packet is either active as a unit or stopped as a unit at
each layer.

If instead each of the \(O(W/m)\) packet paths is cut independently once at
each of the \(H\) layers, the resulting boundary ledger is only

\[
 O(HW/m)=O(W/H),
 \tag{6.1}
\]

not the strict \(o(W/H)\) required by \(\mathrm{EP}_A\). The little-oh must
come from whole-packet tagging, cross-packet fusion, or a genuinely more
global active ordering.

The exact tag-\(H\) recursive target is therefore:

> **Top-tag recursive common-base theorem \(\mathrm{TCB}_A\).** Choose one
> nested active sequence and one compatible pair of endpoint perfect
> matchings at every layer so that:
>
> 1. the final \(N_H\) active states split into recursive rotor packets,
>    apart from \(o_A(W/H)\) exceptional states; and
> 2. the total paired-rainbow and Boolean-completion loss in (5.6), together
>    with all active/inactive boundary cuts, is \(o_A(W/H)\).

\(\mathrm{TCB}_A\) gives the top-tag module required by
\(\mathrm{EP}_A\). It is not by itself the full decorated-SCD theorem,
because the lower-tag collars must still be arranged into the same global
bridge-one path cover.

## 7. Audit conclusion

The new bridge-one operation does not soften the hardest no-collar class:

\[
 G_{\rm bridge}[\mathcal D_H]
 =G_{\rm rotor}[\mathcal D_H].
\]

For small fixed windows, every proof of \(\mathrm{EP}_A\) must therefore
construct a positive-density family of genuine top-tag rotor edges. The
recursive cube factor supplies ideal local cycles at exactly the right
component scale, but selecting them inside one SCD is an exact
common-base/completion problem.

The strongest concrete positive route found is recursive packet completion
\(\mathrm{RPE}_{A}^{H}\), or equivalently the layerwise forced-matching
construction \(\mathrm{TCB}_A\). Neither is proved. The exact obstruction is
not lack of collar capacity, degree, or local bridge successors; it is
simultaneous, recursively compatible lower- and upper-endpoint matching
with a strict \(o(W/H)\) loss budget.
