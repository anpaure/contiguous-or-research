# Paired SCDs under products: a self-product obstruction and the exact skeleton-completion count

Date: 2026-07-26

Method: pure mathematics.  The small (B_4) example is used only through
its displayed chains; no search or solver is used.

## 0. Verdict

The paired-(SCD) property of
`MATH_THEOREM_SCD_DIAMOND_GRAPH_AND_STRIP_COMPATIBILITY_20260726.md`
is **not** closed under the ordinary product recursion for symmetric-chain
decompositions.

More precisely, let the standard product of two chains use the usual
boundary paths in their rectangular product.  If the two factor chains
have the same positive radius, then one positive-radius product chain has
its alternative middle corner in a radius-zero singleton product chain.
Consequently the alternative-corner map of the product SCD does not even
preserve its domain.  In particular, the standard self-product of every
nontrivial SCD fails the paired property.  This applies to the (B_4)
paired seed already at $B_4\times B_4=B_8$.

The obstruction is specific enough to leave the correct escape visible.
A different recursion must replace the standard equal-radius product
resolver by a nonlocal resolver.  Existing quartet-flux identities then
show that a fixed-frame (B_4) tensor cannot be repaired with sparse
seams: ((1/4+o(1))W) central diamonds must be cross-frame, off-centre, or
moving-frame diamonds.  Thus there is no local closure theorem hiding
behind the (B_4) example.

There is also an exact answer to the proposed counting route.  Fix the
entire nonmiddle skeleton of an SCD and contract each central flag to the
edge joining its two possible middle corners.  The resulting graph (J)
has (W) vertices and (N=W-D) edges, where

\[
 D=\operatorname {Cat}_m=\frac{W}{m+1}.
\]

If the skeleton has any central completion, then (J) is a pseudoforest.
If its tree components have orders (t_1,\ldots,t_D), and it has (u)
unicyclic components, then the number of central completions is exactly

\[
 \boxed{Z(J)=2^u\prod_{i=1}^{D}t_i.}
 \tag{0.1}
\]

The periodic points of the resulting diamond map are exactly the vertices
on the unique cycles of the unicyclic components; vertices in trees
attached to those cycles are not periodic.  If (C(J)) is the total core
cycle mass and (B=W-C(J)), then, using the double-rainbow girth-four
condition,

\[
 \boxed{
 Z(J)\le
 2^{(W-B)/4}\left(\frac{B}{D}\right)^D.}
 \tag{0.2}
\]

Hence a counting proof would work if one could show that the **average
number of central completions per nonmiddle skeleton** is

\[
 \exp\!\left(\left(\frac{\log2}{4}-o(1)\right)W\right).
 \tag{0.3}
\]

No current SCD enumeration gives this quotient.  A lower bound on the raw
number of SCDs is insufficient because the number of nonmiddle skeletons
must be divided out at exponential precision.  Formula (0.1), rather than
raw cardinality, is the sharp pigeonhole interface.

Finally, even (0.3) would prove only that (W-o(W)) middle owners lie on
central-diamond cycles.  It gives neither long components nor the physical
strip and nested-flag identities needed at depths (q>1).

## 1. The standard chain-product resolver

Let

\[
 C=(c_0<c_1<\cdots<c_p),\qquad
 E=(e_0<e_1<\cdots<e_q)
\]

be symmetric saturated chains, where (p\le q).  The standard SCD of
their product rectangle consists of the paths

\[
 \begin{split}
 P_k={}&(c_k,e_0),(c_k,e_1),\ldots,(c_k,e_{q-k}),\\
      &(c_{k+1},e_{q-k}),\ldots,(c_p,e_{q-k}),
 \end{split}
 \qquad 0\le k\le p.
 \tag{1.1}
\]

The first and last ranks of (P_k) sum to (p+q), and the paths in
(1.1) partition the rectangle.  Applying (1.1) independently to every
pair of factor chains is the ordinary boundary-peeling product SCD.

### Theorem 1.1 (equal-radius escape)

Suppose (C) and (E) both have positive radius (r), so

\[
                         p=q=2r.
\]

In their standard product rectangle, the middle member of (P_{2r-1})
has positive radius one, but its alternative central corner is the middle
member of the singleton path (P_{2r}).  Therefore the product
alternative-corner map does not preserve its positive-radius domain.

#### Proof

For (k=2r-1), (1.1) is the three-element chain

\[
 (c_{2r-1},e_0) <
 (c_{2r-1},e_1) <
 (c_{2r},e_1).
 \tag{1.2}
\]

Its middle member is

\[
                         X=(c_{2r-1},e_1).
\]

The opposite corner of the Boolean diamond determined by the lower and
upper members of (1.2) is

\[
                         Y=(c_{2r},e_0).
 \tag{1.3}
\]

But (1.1) with (k=2r) is exactly the singleton chain

\[
                         P_{2r}=\{(c_{2r},e_0)\}.
\]

Thus (X) belongs to the domain of the central map and (g(X)=Y) does
not.  In particular (g) cannot be a permutation of the positive-radius
middle centers. \(\square\)

### Corollary 1.2 (no standard product closure)

For all \(a,b\ge1\), the standard product of arbitrary SCDs of
\(B_{2a}\) and \(B_{2b}\) fails the paired-SCD property.  In particular,
the paired \(B_4\) seed does not produce a paired SCD of \(B_8\) by the
ordinary product recursion.

#### Proof

Every SCD of \(B_{2a}\) contains

\[
 \binom{2a}{a-1}-\binom{2a}{a-2}>0
\]

chains of radius one.  Thus the two factor decompositions have an
equal positive-radius pair, and Theorem 1.1 applies. \(\square\)

The theorem is independent of coordinate order inside the two factor
chains.  It concerns the product resolver (1.1), not merely the
Greene--Kleitman choice of the factor SCDs.

### Proposition 1.3 (exact \(B_4\times B_4\) cyclic core)

For the displayed \(B_4\) seed on each factor, the standard product SCD of
\(B_8\) has exactly four periodic central-diamond components, all copies
of the original \(C_4\).  Thus only \(16\) of its

\[
                         \binom83=56
\]

positive-radius middle centers are periodic.

#### Proof

The seed has one chain of radius two, three chains of radius one, and two
singleton chains.  Pairing a singleton chain in either factor with the
six chains in the other factor leaves a complete copy of the seed
unchanged.  The two singleton choices on each shore therefore give four
disjoint \(C_4\)'s.

It remains to rule out a periodic orbit supported by a pair of nontrivial
factor chains.

For two chains of the same radius \(r\), the middle centers of their
standard product paths are

\[
                         (c_k,e_{2r-k}),\qquad 0\le k\le2r.
\]

Their alternative-corner map is the directed path

\[
 (c_0,e_{2r})\longrightarrow(c_1,e_{2r-1})
 \longrightarrow\cdots\longrightarrow(c_{2r},e_0),
 \tag{1.4}
\]

whose last member is the singleton product chain.  Hence equal-radius
pairs contribute no periodic point.

The only unequal pair has radii one and two.  In the radius-two seed chain,
the three relevant alternative corners at ranks one, two, and three are,
respectively,

\[
                         1\mapsto4,\qquad
                         14\mapsto12,\qquad
                         124\mapsto134.
 \tag{1.5}
\]

Every image in (1.5) belongs to a radius-one chain.  Consequently an
unequal product center enters an equal-radius-one product square at the
same global rank, after which (1.4) sends it to a singleton.  The argument
is symmetric when the radius-two chain is in the first factor.  Thus there
are no further periodic points. \(\square\)

This exact \(16/56\) census is a diagnostic for the standard recursion,
not an asymptotic obstruction to a different moving-frame product.

## 2. What survives from the (B_4) seed

Let ({\cal S}_4) be the displayed paired SCD of (B_4), whose four
positive-radius centers form one physical (C_4).  Let ({\cal T}) be
an arbitrary SCD of (B_{2b}).  For every radius-zero singleton middle
chain ({K}) of ({\cal T}), the six products

\[
                         C\times\{K\},qquad C\in{\cal S}_4,
\]

are unchanged copies of the six chains of ({\cal S}_4).  Hence the
standard product contains at least one inherited physical (C_4) for
each singleton chain of ({\cal T}), namely at least

\[
                         \operatorname {Cat}_b
\]

inherited components and (4\operatorname {Cat}_b) inherited cyclic
middle owners.

Relative to the full middle layer in (B_{2b+4}), this guaranteed mass is

\[
 \frac{4\operatorname {Cat}_b}{\binom{2b+4}{b+2}}
 =\frac{b+2}{(2b+1)(2b+3)}
 =\left(\frac14+o(1)\right)\frac1b.
 \tag{2.1}
\]

Thus the direct suspension theorem supplies only a vanishing
(\Theta(W/b)) owner mass.  Other periodic components may occur for a
particular factor SCD, so (2.1) is a guaranteed lower count, not an exact
classification.  In particular it is not evidence for positive-density
closure.

There are two further independent failures.

1. Every inherited component has length four.  Replicating it over
   (W-o(W)) owners without fusing components would give
   ((1/4-o(1))W) components, whereas the compiler needs
   (o(W/H)).
2. Its swap-support word repeats after two steps.  It is a physical
   (C_4), hence exactly (2)-safe, but it is not (3)-safe.  Suspension
   does not change this word.  Therefore no direct replication supplies
   the nested physical flags required for any mesoscopic (H\ge3).

The fixed-quartet flux theorem in
`MATH_OBSTRUCTION_N_PAIRED_SCD_CATALAN_PARITY_AND_QUARTET_FLUX_20260726.md`
is stronger than these two observations for sparse-seam tensoring.  In a
fixed partition into quartets, every SCD has

\[
 (1/4+o(1))W
\]

central diamonds which are not pure central (B_4)-seed diamonds.
Therefore any positive-density recursive construction must perform a
linear number of cross-quartet, off-centre, or moving-frame resolutions.

An independent and sharper bound applies when a full first global SCD
retains the child-product-box owner census.  The cross-box theorem in
\`MATH_THEOREM_PAIRED_SCD_PRODUCT_AND_B4_SCALING_OBSTRUCTION_20260726.md\`
forces at least

\[
 W_aW_b-\operatorname {Cat}_a\operatorname {Cat}_b
\]

central edges between different child-chain boxes.  With a \(B_4\) outer
factor this is

\[
 \frac{m(3m-4)}{2(2m-1)(2m-3)}W
 >\frac38W.
 \tag{2.2}
\]

Thus even arbitrary internal decompositions of the fixed product boxes
cannot turn the seed into a sparse-seam recursion.  The only unexcluded
product input is the weaker datum of half-chain skeletons whose middle
owners and singleton leave are globally reassigned before either full SCD
is formed.

### Proposition 2.1 (balanced growing products are not density-obstructed)

The preceding positive-density tax is specific to a bounded outer factor.
Split \(B_{4s}\) into two copies of \(B_{2s}\), and put

\[
 W_s=\binom{2s}s,\qquad W_{2s}=\binom{4s}{2s}.
\]

Then the common-box lower bound is only

\[
 W_s^2-\operatorname {Cat}_s^2
 =\left(\sqrt{\frac{2}{\pi s}}+o(s^{-1/2})\right)W_{2s}.
 \tag{2.3}
\]

Moreover, the number of forced equal-radius escapes in the standard
product is

\[
 \sum_{r=1}^{s}c_{s,r}^2
 =\left(\frac1{2s}+o(s^{-1})\right)W_{2s},
 \tag{2.4}
\]

where

\[
 c_{s,r}=\binom{2s}{s-r}-\binom{2s}{s-r-1}.
\]

#### Proof

Stirling's formula gives

\[
 \frac{W_s^2}{W_{2s}}
 =\left(\sqrt{\frac{2}{\pi s}}+o(s^{-1/2})\right),
\]

and \(\operatorname {Cat}_s/W_s=1/(s+1)\), proving (2.3).

For \(r=x\sqrt s\), the local central-binomial estimate and the exact
chain census give

\[
 \frac{c_{s,r}}{W_s}
 =\frac{2x}{\sqrt s}e^{-x^2}
   +o(s^{-1/2})
 \tag{2.5}
\]

uniformly for \(x\) in compact intervals; the Gaussian tail makes the
remaining terms summable uniformly.  Hence the Riemann sum is

\[
 \begin{aligned}
 \frac1{W_s^2}\sum_{r\ge1}c_{s,r}^2
 &=(1+o(1))\frac4{\sqrt s}
   \int_0^\infty x^2e^{-2x^2}\,dx\\
 &=(1+o(1))\frac{\sqrt\pi}{2\sqrt{2s}}.
 \end{aligned}
 \tag{2.6}
\]

Multiplying (2.6) by
\(W_s^2/W_{2s}=(1+o(1))\sqrt{2/(\pi s)}\) proves (2.4).
\(\square\)

Thus the proved product obstructions do **not** exclude a balanced
growing-block resolver: both displayed defect scales are \(o(W_{2s})\).
What remains formidable is their geometry.  A naive \(O(H)\) flag loss per
cross-box resolution would cost

\[
                         \Theta(HW_{2s}/\sqrt s),
\]

which is not \(o(W_{2s})\) in the Gaussian window
\(H\gtrsim\sqrt s\).  A viable balanced recursion must therefore route
the cross-box edges in long physical components and preserve nested flags
collectively; treating the seams independently still fails.

## 3. Central completions of one fixed nonmiddle skeleton

Fix the lower and upper half-chains of an SCD, including their pairing into
central flags

\[
                         R\subset U,qquad |U\setminus R|=2.
\]

Call this data a **nonmiddle skeleton** (Sigma).  Contract every flag to
the edge joining its two possible middle corners.  The resulting graph

\[
                         J_\Sigma
\]

has vertex set $\binom{[2m]}m$, hence $W$ vertices, and one edge for
each rank-((m-1)) set, hence

\[
                         N=W-D
\]

edges.  Distinct flags give distinct edges.

A central completion of (Sigma) chooses one endpoint of every edge so
that no middle vertex is chosen twice.  Equivalently, subdivide every edge
once at its flag vertex; a completion is a matching saturating all
subdivision vertices.

### Lemma 3.1 (pseudoforest normal form)

If (J_\Sigma) admits a central completion, every connected component is
a tree or is unicyclic.  The number of tree components is exactly (D).

#### Proof

In a component with (e) edge-flags and (v) middle vertices, a matching
saturating all edge-flags uses (e) distinct middle vertices, so (e\le v).
A connected graph with (e\le v) is a tree or unicyclic.  Summing
(v-e) over all components gives

\[
                         W-N=D.
\]

A tree contributes one and a unicyclic component contributes zero, proving
the count. \(\square\)

### Theorem 3.2 (exact completion multiplicity)

Let the (D) tree components of (J_\Sigma) have orders
(t_1,\ldots,t_D), and let (u) be the number of unicyclic components.
Then

\[
                         Z(J_\Sigma)=2^u\prod_{i=1}^{D}t_i.
 \tag{3.1}
\]

#### Proof

In a tree component, exactly one middle vertex is unmatched.  Once that
root is chosen, every edge is forced to choose its endpoint farther from
the root.  Thus a tree of order (t) has exactly (t) completions.

In a unicyclic component every middle vertex is matched.  The edges on the
unique cycle have precisely two consistent orientations.  Once one is
chosen, every edge in a tree attached to the cycle is forced away from the
cycle.  Thus each unicyclic component has exactly two completions.
Independence across components proves (3.1). \(\square\)

For the \(B_4\) seed, \(J_\Sigma\) is one \(C_4\) plus the two isolated
middle vertices \(13,24\).  Thus \(D=2\), \(u=1\),
\(t_1=t_2=1\), and (3.1) gives \(Z=2\): precisely the displayed SCD and
its simultaneous central flip.  This is equality in the bound (4.3)
below.

### Proposition 3.3 (cyclic mass is skeleton-invariant)

For every central completion of a fixed skeleton, the periodic points of
its alternative-corner map are exactly the middle vertices on the unique
cycles of the unicyclic components of (J_\Sigma).  In particular, their
total number (C(J_\Sigma)) is independent of the completion.

#### Proof

In a tree component, orienting from each chosen endpoint to the other
endpoint directs every orbit toward the unique unmatched root, so there is
no periodic point.  In a unicyclic component, all attached-tree orbits feed
the core cycle, while the two possible cycle orientations give the same
periodic vertex set. \(\square\)

This proposition is the counting analogue of fixed-skeleton component
rigidity: having many completions does not allow one to move cyclic mass
between components.

## 4. The sharp pigeonhole threshold

The edge graph (J_\Sigma) has no cycles of length one, two, or three.
Loops and parallel edges are excluded because a flag is determined by its
two middle corners.  In a triangle, either all three Johnson edges have the
same lower colour or all three have the same upper colour, contradicting
the fact that the skeleton uses every lower and upper flag endpoint once.
Thus every core cycle has length at least four.

Put

\[
                         C=C(J_\Sigma),\qquad B=W-C.
\]

Then

\[
                         u\le C/4=(W-B)/4.
 \tag{4.1}
\]

All vertices in tree components lie outside the core, so

\[
                         \sum_{i=1}^{D}t_i\le B.
 \tag{4.2}
\]

The arithmetic--geometric mean inequality and Theorem 3.2 give

\[
 \begin{aligned}
 Z(J_\Sigma)
 &\le 2^{C/4}
       \left(\frac{\sum_i t_i}{D}\right)^D\\
 &\le 2^{(W-B)/4}\left(\frac BD\right)^D.
 \end{aligned}
 \tag{4.3}
\]

Since (D=W/(m+1)), if (B\ge\varepsilon W), then

\[
 \log Z(J_\Sigma)
 \le
 \left(\frac{\log2}{4}-\frac{\varepsilon\log2}{4}+o(1)\right)W.
 \tag{4.4}
\]

Let ({\sf SCD}_{2m}) be the set of SCDs and let ({\sf Skel}_{2m}) be
the set of nonmiddle skeletons admitting a completion.  Since every SCD is
one completion of one skeleton,

\[
 \frac{|{\sf SCD}_{2m}|}{|{\sf Skel}_{2m}|}
 =\frac1{|{\sf Skel}_{2m}|}
   \sum_{\Sigma\in{\sf Skel}_{2m}} Z(J_\Sigma).
 \tag{4.5}
\]

### Corollary 4.1 (exact counting criterion)

If

\[
 \log\frac{|{\sf SCD}_{2m}|}{|{\sf Skel}_{2m}|}
 \ge\left(\frac{\log2}{4}-o(1)\right)W,
 \tag{4.6}
\]

then some nonmiddle skeleton has

\[
                         C(J_\Sigma)=W-o(W).
 \tag{4.7}

#### Proof

If (4.7) failed, there would be a fixed $\varepsilon>0$ along a
subsequence for which every skeleton has $B\ge\varepsilon W$.  Equations
(4.4)--(4.5) would contradict (4.6). \(\square\)

The criterion needs the quotient in (4.6), not merely a lower bound on
(|{\sf SCD}_{2m}|).  The trivial relations

\[
 |{\sf Skel}_{2m}|\le |{\sf SCD}_{2m}|
 \le |{\sf Skel}_{2m}|
       \exp\!\left(\left(\frac{\log2}{4}+o(1)\right)W\right)
 \tag{4.8}

leave the entire required exponential interval open.  Present abundance
results for SCDs do not control (4.6), so raw cardinality cannot yet force
a good skeleton.

Even Corollary 4.1 would give only a central (q=1) cyclic core after
discarding (o(W)) owners.  Formula (4.7) does not bound the number of
cycles, make them physical, or identify the SCD depth-(q) flags with
consecutive cycle windows.  These remain independent requirements.

There is in fact a tension between completion multiplicity and the final
component target.

### Corollary 4.2 (long-factor skeletons have subexponential fibres)

Suppose a sequence of skeletons has periodic core mass \(W-B=W-o(W)\)
and has

\[
                         u=o(W/H)
\]

unicyclic components, as required by the whole-component compiler.  Then

\[
                         \log Z(J_\Sigma)=o(W).
 \tag{4.9}
\]

#### Proof

Theorem 3.2 and the arithmetic--geometric mean inequality give

\[
 \log Z(J_\Sigma)
 \le u\log2+
 D\log\!\left(\frac BD\right).
 \tag{4.10}
\]

Here \(u=o(W/H)=o(W)\), while \(B\le W\) and
\(D=W/(m+1)\), so the second term is at most

\[
 \frac{W}{m+1}\log(m+1)=o(W).
\]

This proves (4.9). \(\square\)

Thus a maximum-fibre pigeonhole argument is pointed at the wrong final
object.  Exponentially many completions are supplied by many independently
orientable core cycles, whereas coefficient one needs only
\(o(W/H)\) long components.  SCD abundance could still prove existence by
controlling the **number and geometry of skeletons**, but not by forcing one
skeleton to carry an exponentially large completion fibre.

## 5. Exact surviving recursive target

The (B_4) paired property therefore has the following audited status.

1. **All-(m) exact closure is impossible.**  Catalan parity excludes
   every (m=2^a-1).
2. **Ordinary self-product closure is impossible.**  The equal-radius
   escape in Theorem 1.1 occurs before component or flag estimates enter.
3. **Fixed-frame sparse-seam closure is impossible.**  Quartet flux forces
   \(\Omega(W)\) genuinely nonlocal central resolutions, and retaining a
   full product-box owner census forces more than \(3W/8\) cross-box edges
   for a \(B_4\) outer factor.
4. **Direct suspension is too sparse and too shallow.**  It guarantees
   only (Theta(W/m)) inherited owner mass, in (C_4)'s which fail at
   depth three.
5. **A counting proof has an exact but presently unmet threshold.**  It
   must control completions per nonmiddle skeleton at the exponential rate
   (4.6); total SCD abundance alone does not do this.

The only product-like route not excluded here is therefore a dense
moving-frame resolver which changes a linear number of central flags,
fuses the resulting cycles to average length (omega(H)), and enforces
the nested flag identities through depth (H).  This is a new global
construction, not a closure property of the (B_4) seed.
