# Facet fixed-base subset-core frames: an exponential-in-`q` local amplifier

Date: 2026-08-02  
Status: unconditional literal owner/target-simple local construction and
exact conditional packing reduction.  The source-occurrence ledger is
audited exactly.  No inter-frame packing, chronology, component fusion, or
OR-word upper bound is claimed.

## 0. Outcome

Put

\[
 q=d+2,\qquad c=r-q+1=r-d-1,
 \qquad W=\binom{k}{r},                                      \tag{0.1}
\]

and assume `q>=4` and `c>=2`.  A length-`q` facet module has a
`c`-core `C`, a disjoint `q`-tag set `V`, and owner block

\[
                  \{C\cup(V-\{v\}):v\in V\}.                \tag{0.2}
\]

There is a large simultaneous family which makes every named resource
injective without slopes, private tag banks, or a post-hoc low matching.

Choose a partition

\[
 [k]=D\ \dot\cup\ G\ \dot\cup\ V,
 \qquad 1\le |D|=a\le c-1,\quad |V|=q,                     \tag{0.3}
\]

and put

\[
                         t=c-a.                              \tag{0.4}
\]

For every `X in binom(G,t)`, use the core

\[
                         C_X=D\cup X.                        \tag{0.5}
\]

Fix one point `beta in D`, one oriented cyclic order on `V`, and fixed
distinct tags `w,h in V`; reuse them in every module.  Then every owner,
every high target, and both low targets of module `X` have intersection
with `G` exactly equal to `X`.  Hence all

\[
                         M_a=\binom{k-a-q}{c-a}               \tag{0.6}
\]

modules are pairwise owner- and target-simple.

The construction is literal.  In module `X`, the source common core is

\[
                         K_X=(D-\{\beta\})\cup X,             \tag{0.7}
\]

and the standard length-`q=d+2` word supplies exactly one primitive `P`,
one primitive `H`, and `d` short `H` buffers.  Sharing `V` and its order
does not share any source occurrence; the corrected ledger is multiplied
by `M_a` exactly.

The choice `a=1` maximizes (0.6).  It gives

\[
 M_1=\binom{k-q-1}{c-1}
    =\binom{k-q-1}{r-q}
    =\Theta(W/2^q).                                         \tag{0.8}
\]

More sharply, in the canonical middle-layer regime,

\[
             {M_1\over W}
             \sim 2^{-(q+1)}e^{-\pi/16}.                    \tag{0.9}
\]

Thus one fixed-base frame contains exponentially many in `q` completely
labelled primitive modules.  A requested buffered inventory

\[
                         t_*=\Theta(W/q^2)                   \tag{0.10}
\]

has the formal local quotient

\[
                         \Theta(2^q/q^2)                     \tag{0.11}
\]

maximum frames, with one partial final frame if necessary.  This supersedes
the local `Theta(q)` prime-slope amplification and the narrower
`Theta(q^2)` singleton-marker construction.  It does **not** give a global
packing target: Section 5 proves that pairwise disjoint prelabelled
singleton-base frames have cardinality at most `2q+1`, so (0.11) is
impossible for the common-low-label `a=1` family.  A viable global route
cannot use complete reservoirs in the locally useful small-base regime:
Section 6 proves that such owner-disjoint frames have pairwise disjoint tag
sets and hence number at most `floor(k/q)`.  Even using the locally largest
reservoirs, their total module count is `o(W/q^2)`.  A viable amplification
route must extract partial reservoirs and solve their owner/high matching
jointly, then either retain the internal low labels or postpone them to the
exact Hall stage.  A complete-reservoir route would have to jump to base
size `Theta(k)`, where this note makes no global no-go claim.

## 1. The literal subset-core frame

Fix the data in (0.3), a point `beta in D`, an oriented cyclic order

\[
                         \sigma=(w,v_1,\ldots,v_{d+1})        \tag{1.1}
\]

of `V`, and one distinguished primitive-`H` tag

\[
                         h\in V-\{w\}.                        \tag{1.2}
\]

For `X in binom(G,t)`, define `C_X` and `K_X` by (0.5) and (0.7).  Since

\[
 |K_X|=(a-1)+(c-a)=c-1,                                    \tag{1.3}
\]

the literal source cycle

\[
 \begin{aligned}
   S_{X,0}&=K_X\cup\{w\},\\
   S_{X,i}&=K_X\cup\{\beta,v_i\}
            =C_X\cup\{v_i\},
            \qquad 1\le i\le d+1
 \end{aligned}                                               \tag{1.4}
\]

is exactly the sharp length-`q` primitive word.

### Lemma 1.1 (literal role and buffer audit)

For each `X`, the cycle (1.4) has:

1. one state of type `P=(c-1,2,1,...,1)`;
2. `d+1` states of type `H=(c,1,...,1)`;
3. the `q` distinct rank-`r` owners

   \[
             O_{X,v}=D\cup X\cup(V-\{v\}),
             \qquad v\in V;                                 \tag{1.5}
   \]

4. one fully marked primitive `P`, the `H` occurrence indexed by `h`
   fully marked as the primitive `H`, and the remaining `d` `H`
   occurrences marked as short buffers.

#### Proof

Equation (1.4) is the literal construction in the sharp buffered one-copy
primitive theorem, with its common source core equal to `K_X` and its
deleted point `b` equal to `beta`.  Every `d+1` consecutive source letters
contain all of `C_X` and omit exactly one private tag in `V`, giving (1.5).
At position zero the current source is `K_X+w` and the age-one cell is
`{beta,v_(d+1)}`, which is type `P`.  Every other large source has refreshed
`K_X+beta=C_X` and gives type `H`.  The mark assignment is exactly the one
primitive plus `d` short-buffer assignment of the cited theorem. \(\square\)

In particular `beta in C_X`, `w,h in V`, `w!=h`, and `C_X cap V=empty`.
No literal role or buffer condition is relaxed.

## 2. Exact owner and named-target simplicity

The complete named deck of module `X` is

\[
\begin{array}{c|c}
\text{rank}&\text{resources}\\ \hline
r&D\cup X\cup(V-\{v\}),\quad v\in V,\\
c&(D-\{\beta\})\cup X\cup\{w\},\\
c+1&D\cup X\cup\{h\},\\
c+j&D\cup X\cup J,
      \quad J\text{ a cyclic }j\text{-interval of }\sigma,
      \quad 2\le j\le q-2.
\end{array}                                                   \tag{2.1}
\]

### Theorem 2.1 (fixed-base subset-core amplifier)

The decks (2.1), as `X` ranges over `binom(G,t)`, are pairwise disjoint at
every displayed rank.  Hence one frame contains exactly `M_a` completely
labelled, pairwise owner- and target-simple primitive facet modules.

#### Proof

Every resource in (2.1) has intersection with `G` exactly equal to `X`,
because `D`, `G`, and `V` are disjoint.  Equality between same-rank
resources from modules `X` and `Y` would therefore imply `X=Y`.

Within one module, owner simplicity and target simplicity are the literal
facet-module theorem: the owners are distinct facets, proper cyclic
intervals of one fixed length have distinct starts, and each low row has
one target.  \(\square\)

The proof permits the same order and same low tags in every module.  It is
also why deleting the common point is essential.  If `a=0` there is no
common `beta`.  If one instead deletes a varying element of `X`, the
primitive-`P` target no longer necessarily recovers `X`, and collisions are
not excluded.  The theorem deliberately starts at `a=1`.

### Corollary 2.2 (the old marker frame)

Take `a=c-1`, so `t=1`.  Then

\[
 M_{c-1}=\binom{k-c-q+1}{1}=k-r.                             \tag{2.2}
\]

Writing `X={gamma}` recovers the codimension-one marker frame: every
resource contains the unique marker `gamma`.  Thus the earlier quadratic
amplifier is the last member of the family (0.6), while `a=1` is the first
and largest member.

## 3. Exact resource ledger

### Proposition 3.1 (one `a`-frame)

A fixed-base frame with `M_a` modules consumes

\[
\begin{array}{c|c}
\text{resource}&\text{consumption}\\ \hline
e_{d+1}&M_a,\\
e_{d-1}&(q-1)M_a,\\
\text{short-loop slack }L-H&dM_a,\\
\text{rank-}c\text{ targets}&M_a,\\
\text{rank-}(c+1)\text{ targets}&M_a,\\
\text{rank-}(c+j)\text{ targets},\ 2\le j\le q-2&qM_a,\\
\text{rank-}r\text{ owners}&qM_a.
\end{array}                                                   \tag{3.1}
\]

Its owner/named-target edge has total size

\[
                         M_a(q^2-2q+2).                       \tag{3.2}
\]

#### Proof

Apply the exact length-`q`, `B=0` row of the corrected module ledger to
each literal module and sum.  Theorem 2.1 proves that no named resource is
identified across modules.  There are `q-3` high target ranks, so the named
total is

\[
 qM_a+2M_a+(q-3)qM_a=M_a(q^2-2q+2).
\]

\(\square\)

The frame does **not** compress source occurrences.  Globally, a selected
total of `t_*` modules still requires

\[
 t_*\le A_{d+1},\quad
 (q-1)t_*\le A_{d-1},\quad
 dt_*\le L-H,\quad
 qt_*\le n_{c+2}.                                           \tag{3.3}
\]

The gain is solely that owner and every named-target row are solved jointly
inside one very large batch.

## 4. Optimal base size and asymptotics

### Lemma 4.1 (the singleton base is largest)

The frame sizes `M_a` strictly decrease with `a` throughout
`1<=a<=c-1`:

\[
                    {M_{a+1}\over M_a}
                    ={c-a\over k-a-q}<1.                    \tag{4.1}
\]

#### Proof

Use

\[
 {\binom{n-1}{s-1}\over\binom ns}={s\over n}
\]

with `n=k-a-q` and `s=c-a`.  Since `c<k-q`, the ratio is below one. \(\square\)

For `a=1`, the exact ratio to the middle layer is

\[
 {M_1\over W}
 ={\binom{k-q-1}{r-q}\over\binom kr}
 ={(k-r)(r)_q\over(k)_{q+1}},                               \tag{4.2}
\]

where `(x)_j=x(x-1)...(x-j+1)`.

### Lemma 4.2 (sharp canonical asymptotic)

If `q=d+2` has its canonical value, then (0.9) holds.

#### Proof

Uniformly for `q=O(sqrt(r))`, pair the `q` factors `(r-i)` in (4.2) with
the first `q` factors of `(k)_(q+1)` and leave one denominator factor with
`k-r`.  In either parity,

\[
 \log {M_1\over W}
 =-(q+1)\log2-{q^2\over4r}+o(1).                            \tag{4.3}
\]

The canonical relation `q^2/r -> pi/4` gives

\[
 {M_1\over W}
 \sim 2^{-(q+1)}e^{-\pi/16}.
\]

\(\square\)

Now let `t_*` be any physically requested number satisfying (3.3).  Divide
it into full `a=1` frames and one remainder.  If

\[
                         t_*=\Theta(W/q^2),                  \tag{4.4}
\]

then (0.9) gives

\[
             \left\lceil{t_*\over M_1}\right\rceil
             =\Theta(2^q/q^2).                              \tag{4.5}
\]

For comparison, if only the buffer-coordinate ceiling is saturated,

\[
 t_*={A_{d-1}\over q-1}
 \sim {\pi\over2}e^{-\pi/4}{W\over q^2},                    \tag{4.6}
\]

the frame count is

\[
 \left\lceil{t_*\over M_1}\right\rceil
 \sim \pi e^{-3\pi/16}{2^q\over q^2}.                      \tag{4.7}
\]

The local comparison is therefore

\[
\begin{array}{c|c|c}
\text{frame}&\text{modules per frame}&
\text{frames for }\Theta(W/q^2)\text{ modules}\\ \hline
\text{prime-slope}&\Theta(q)&\Theta(W/q^3)\\
\text{singleton marker}&\Theta(q^2)&\Theta(W/q^4)\\
\text{singleton-base subset-core}&\Theta(W/2^q)&
                                  \Theta(2^q/q^2).
\end{array}                                                   \tag{4.8}
\]

This is a local amplification comparison only.  The resource edge of one
singleton-base frame is itself enormous, of size
`M_1(q^2-2q+2)`, and fewer edges do not by themselves prove that they can be
packed disjointly.

## 5. Exact `P`-deck intersection and the global prelabelled no-go

For one prelabelled `a`-frame `i`, write

\[
 B_i=D_i-\{\beta_i\},\qquad
 A_i=B_i\cup\{w_i\},\qquad
 F_i=\{\beta_i\}\cup(V_i-\{w_i\}).                          \tag{5.1}
\]

Thus `|B_i|=a-1`, `|A_i|=a`, `|F_i|=q`, and the primitive-`P` deck is the
exact Boolean cylinder

\[
 {\cal P}_i=\left\{S\in\binom{[k]}c:
                   A_i\subseteq S,\quad S\cap F_i=\varnothing\right\}.
                                                                    \tag{5.2}
\]

### Lemma 5.1 (exact cylinder intersection)

Two `P` decks intersect if and only if

\[
 A_i\cap F_j=A_j\cap F_i=\varnothing,
 \qquad |A_i\cup A_j|\le c\le k-|F_i\cup F_j|.              \tag{5.3}
\]

#### Proof

A common target must contain `A_i union A_j` and avoid `F_i union F_j`, so
(5.3) is necessary.  Conversely, if (5.3) holds, extend `A_i union A_j` by
arbitrary coordinates outside all mandatory and forbidden coordinates
until the set has size `c`.  The resulting set belongs to both cylinders.
\(\square\)

The canonical range eventually satisfies

\[
                         k-r\ge q+1.                          \tag{5.4}
\]

For two frames with the same `B_i=B_j=B`, the two size inequalities in
(5.3) are then automatic.  Their `P` decks intersect when `w_i=w_j`.
When the two tags are distinct, the decks are disjoint exactly when

\[
                         w_j\in F_i\quad\hbox{or}\quad
                         w_i\in F_j.                          \tag{5.5}
\]

### Theorem 5.2 (fixed-base tournament bound)

For every fixed `(a-1)`-set `B`, a pairwise `P`-deck-disjoint family of
prelabelled `a`-frames with base remainder `B_i=B` has size at most

\[
                         2q+1.                                \tag{5.6}
\]

Consequently every pairwise fully resource-disjoint family of prelabelled
`a`-frames has size at most

\[
                         (2q+1)\binom{k}{a-1}.                \tag{5.7}
\]

#### Proof

In a disjoint family with common `B`, the distinguished `w_i` are all
different.  Draw the directed arc `i->j` when `w_j in F_i`.  Condition
(5.5) says that every unordered pair supports at least one arc.  But
`|F_i|=q`, so the outdegree of every vertex among the distinguished tags is
at most `q`.  Therefore

\[
             \binom f2\le fq,
\]

where `f` is the family size, and hence `f<=2q+1`.  Grouping an arbitrary
family by its value of `B_i` gives (5.7). \(\square\)

### Corollary 5.3 (the maximum local frame cannot be packed globally)

At `a=1` there is only the empty remainder `B`.  Hence at most `2q+1`
prelabelled singleton-base frames can be pairwise resource-disjoint.  Since

\[
                         2q+1=o(2^q/q^2),                    \tag{5.8}
\]

the formal quotient (0.11) cannot be realized.  This is a theorem, not a
failure of a particular greedy argument.

For general `a`, Theorem 5.2 gives the necessary prelabelled capacity

\[
 U_a=(2q+1)\binom{k}{a-1}M_a.                               \tag{5.9}
\]

The base size required merely to remove this obstruction has a sharp first
order scale.

### Proposition 5.4 (signature-capacity threshold)

Fix `epsilon>0` and put natural logarithms in the formulas below.  For

\[
                         a={\lambda q\over\log q}+O(1)        \tag{5.10}
\]

with fixed `lambda>0`,

\[
                 \log {U_a\over W}
                 =(\lambda-\log2)q+o(q).                    \tag{5.11}
\]

Therefore:

* if `lambda<log 2`, even the upper bound (5.9) is
  `o(W/q^2)`, so such prelabelled frames cannot carry the requested
  primitive inventory;
* if `lambda>log 2`, the fixed-`B` tournament count no longer gives a
  scalar obstruction to carrying `Theta(W/q^2)` modules.

The second statement is not an existence theorem.

#### Proof

For `a=o(q)`, repeated use of (4.1) and `q=Theta(sqrt(k))` gives

\[
                         M_a=M_1 2^{-(a-1)}e^{o(q)}.          \tag{5.12}
\]

Also Stirling's formula gives, for `a=lambda q/log q+O(1)`,

\[
 \log\binom{k}{a-1}
 =(a-1)\log{k\over a-1}+a+o(q)
 =\lambda q+o(q).                                           \tag{5.13}
\]

Combine (0.9), (5.9), (5.12), and (5.13); the factors `2q+1`,
`2^{-(a-1)}`, and every polynomial term contribute only `o(q)` beyond the
displayed leading exponent. \(\square\)

Thus the first prelabelled family not ruled out by the low cylinder has

\[
                         a\asymp {q\over\log q},              \tag{5.14}
\]

not `a=1`.  Proving an owner/high/low resource-disjoint packing at or above
that scale remains a correlated interval-spread problem.

## 6. The owner cylinder rules out the entire small-base regime

For a frame `i` and one omitted tag `v in V_i`, its corresponding owner
cylinder is

\[
 {\cal O}_{i,v}=\left\{S\in\binom{[k]}r:
  D_i\cup(V_i-\{v\})\subseteq S,\quad v\notin S\right\}.     \tag{6.1}
\]

The full owner deck is the union over `v in V_i`.

### Lemma 6.1 (exact owner-cylinder criterion)

The two cylinders `O_(i,v)` and `O_(j,v')` intersect if and only if

\[
 \begin{aligned}
 v'&\notin D_i\cup(V_i-\{v\}),\\
 v &\notin D_j\cup(V_j-\{v'\}),\\
 \left|D_i\cup(V_i-\{v\})\cup
        D_j\cup(V_j-\{v'\})\right|&\le r.
 \end{aligned}                                               \tag{6.2}
\]

#### Proof

The first two rows say exactly that neither cylinder requires the tag
forbidden by the other.  The last row says their two mandatory sets fit in
one rank-`r` set.  Since at most two coordinates are forbidden and
`r<=k-2` eventually, these three conditions are also sufficient: fill the
mandatory union arbitrarily to rank `r`. \(\square\)

### Corollary 6.2 (simplified small-base criterion)

Suppose

\[
                         a_i+a_j+2q-2\le r.                   \tag{6.3}
\]

Then two complete frames `i,j` have disjoint owner decks if and only if

\[
 V_i\cap V_j=\varnothing
 \quad\hbox{and}\quad
 \left(V_i\subseteq D_j\ \hbox{or}\ V_j\subseteq D_i\right). \tag{6.4}
\]

#### Proof

Condition (6.3) makes the last row of (6.2) automatic.  If
`x in V_i cap V_j`, omit `x` in both frames; the first two rows hold and the
owners collide.  If the tag sets are disjoint, (6.2) has a solution exactly
when both `V_i-D_j` and `V_j-D_i` are nonempty.  Negating this condition
gives (6.4). \(\square\)

### Theorem 6.3 (small-base complete-reservoir no-go)

Fix `a` with

\[
                         2a+2q-2\le r.                        \tag{6.5}
\]

Every pairwise owner-disjoint family of complete `a`-frames has size at
most

\[
                         \left\lfloor{k\over q}\right\rfloor. \tag{6.6}
\]

Its total number of modules is at most

\[
             \left\lfloor{k\over q}\right\rfloor M_1
             =O(qW/2^q)=o(W/q^2).                           \tag{6.7}
\]

#### Proof

Corollary 6.2 makes the `q`-sets `V_i` pairwise disjoint, proving (6.6).  Lemma
4.1 gives `M_a<=M_1` for every frame, and `k/q=Theta(q)`.  Combine this with
`M_1=Theta(W/2^q)` to obtain (6.7). \(\square\)

The low-cylinder threshold `a=Theta(q/log q)` lies far inside (6.5), so
increasing `a` merely to clear Proposition 5.4 cannot rescue the complete
reservoir.  A complete-reservoir strategy would have to jump to

\[
                         a>{r-2q+2\over2}=\Theta(k),          \tag{6.8}
\]

where the local reservoir is much smaller.  This note makes no no-go claim
for that large-base regime.  For the intended amplification, partial
reservoir extraction is the proof-safe target.

## 7. Partial reservoirs: exact conflict matchings and flow boundary

Let `R_i` be the module set of a fixed frame, or any selected subset of its
full reservoir.  Temporarily omit the two low labels and retain only owners
and high targets.

### Theorem 7.1 (cross-reservoir partial-matching decomposition)

For two fixed frames `i,j`, the owner/high conflict graph on
`R_i dotcup R_j` is the union of at most

\[
                         Q=q^2(q-2)                           \tag{7.1}
\]

partial matchings.  In particular, every module of either reservoir
conflicts with at most `Q` modules of the other reservoir.

If the common prelabelled `P,H` targets are retained, two further partial
matchings suffice, giving `Q+2`.

#### Proof

Fix one module `X` of frame `i`.

For an owner collision, choose the omitted tag `v in V_i` and the omitted
tag `v' in V_j`.  Equality of the two owners uniquely determines

\[
 X'=
 \left(D_i\cup X\cup(V_i-\{v\})\right)
       -\left(D_j\cup(V_j-\{v'\})\right).                   \tag{7.2}
\]

It is either the unique valid module of frame `j` for this footprint pair,
or it is invalid.  Reversing (7.2) uniquely recovers `X`, so every one of
the `q^2` omitted-tag pairs defines a partial matching.

At high rank `c+s`, `2<=s<=q-2`, choose one of the `q` cyclic `s`-intervals
in each frame.  Equality

\[
                         D_i\cup X\cup J
                         =D_j\cup X'\cup J'                  \tag{7.3}
\]

again uniquely determines `X'`, and the reverse equality determines `X`.
Thus each ordered pair `(J,J')` is a partial matching.  There are `q^2`
such pairs at each of the `q-3` high ranks.  Together with owners this is

\[
                         q^2+(q-3)q^2=q^2(q-2).
\]

Each low row has one footprint per module and equality again determines the
other reservoir index uniquely, adding two partial matchings. \(\square\)

This gives an exact finite optimization model.  With one binary variable
`z_(i,X)` per module, partial-reservoir extraction is

\[
 \begin{aligned}
 \max\quad &\sum_{i,X}z_{i,X},\\
 \text{subject to}\quad
 &\sum_{(i,X):R\in\operatorname{Deck}(i,X)}z_{i,X}\le1
       &&\text{for every named resource }R,\\
 &z_{i,X}\in\{0,1\}.
 \end{aligned}                                               \tag{7.4}
\]

Every resource row contains at most one variable from each reservoir,
because Theorem 2.1 makes each reservoir internally simple.

### Corollary 7.2 (the exact two-reservoir flow)

For two reservoirs, let `H_ij` be their bipartite conflict graph.  The
maximum number of jointly retainable modules is

\[
             |R_i|+|R_j|-\nu(H_{ij}),                        \tag{7.5}
\]

where `nu` is maximum matching.  Hence the two-reservoir problem is an
ordinary bipartite flow computation.

#### Proof

A retained union is an independent set of the bipartite graph.  Its
complement is a vertex cover.  Konig's theorem identifies the minimum
vertex-cover size with `nu(H_ij)`. \(\square\)

For `f>=3` reservoirs the matrix in (7.4) is not generally a network
matrix.  The decomposition gives the unconditional degree bound

\[
                         \Delta\le Q(f-1),                    \tag{7.6}
\]

and therefore only

\[
 \alpha\ge
 \max\left\{max_i|R_i|,
 {\sum_i|R_i|\over Q(f-1)+1}\right\}.                       \tag{7.7}
\]

The first term takes one whole reservoir; the second is greedy colouring of
the conflict graph.  For equal reservoirs the second term is smaller by a
factor about `Q`, so (7.7) does not accumulate the internal gains.

This limitation is physical, not merely abstract.  Take several different
cyclic orders on the same `D,V`.  For every core index `X`, their owner
decks are identical, so the cross-conflict graph contains the identity
matching `X<->X` between every pair of reservoirs.  Internal simplicity and
the `Q`-partial-matching decomposition alone can therefore force no gain
beyond distributing the same core indices among the copies.

The exact missing high-deck statement is consequently:

> **Correlated partial-reservoir extraction.**  Choose the frame signatures
> `(D_i,V_i,sigma_i)` and subfamilies `R_i subset binom(G_i,c-a_i)` jointly
> so that (7.4), restricted to owners and high targets, has value
> `Omega(W/q^2)`.

Theorem 7.1 supplies a sparse pairwise language for this problem, but no
unconditional theorem here reaches that value.  In particular, the
existing `W/(18q^3)` joint module greedy theorem remains the stronger
general extraction bound.

## 8. Two proof-safe global routes and scope

There are now two legitimate global targets.

1. **Partial-reservoir extraction.**  In every small-base frame keep only a selected
   subfamily `X_i subset binom(G_i,c-a_i)` and choose these subfamilies
   jointly so their owner and high decks are disjoint.  Theorem 2.1 says
   each individual reservoir is already a matching; Lemma 6.1 explains why
   retaining all its vertices is impossible globally.  Alternatively a
   complete-reservoir construction must use the large-base range (6.8),
   with a separately audited inventory count.
2. **Postponed low labeling.**  During the partial extraction ignore
   `beta,w,h`, pack only owners and high decks, and then apply the exact
   two-stage low-rank Hall theorem module by module.  This avoids the
   prelabelled cylinder bound, but owner/high simplicity alone is not
   sufficient: the affine-line counterexample shows that the exact Hall
   cuts, or the robust multiplicity bounds `Delta_H<=q` and
   `Delta_P<=c(q-1)`, must still be proved.

Neither route currently proves:

* resource disjointness between different frames;
* allocation of the aggregate primitive and short-buffer occurrences in
  (3.3);
* placement of the separate length-`q` source cycles into one physical
  chronology or fusion of their components;
* arbitrary upper shadows, global residence, protected interfaces, or the
  final compiler.

A frame is a resource-simple **bundle of literal components**, not one
already fused component.  The unconditional conclusion is exactly local:
one fixed-base frame simultaneously labels `M_a` modules with no owner or
named-target collision, including both low rows.

## 9. Dependencies

The literal length-`q` primitive and its `d` short buffers are proved in
`MATH_THEOREM_R_PRIMITIVE_MIXED_ROTOR_SHARP_BUFFERED_ONE_COPY_LIFT_20260801.md`.
The exact named deck is in
`MATH_THEOREM_FACET_ABSORBER_MIXED_STAR_DECOMPOSITION_AND_TARGET_COLLISION_GATE_20260802.md`.
The corrected source and named-resource ledger is in
`MATH_THEOREM_FACET_MODULE_LEDGER_AND_WEIGHTED_JOINT_GREEDY_SPREAD_20260802.md`.
The independent low-label Hall obstruction for arbitrary high-simple
packings is in
`MATH_THEOREM_FACET_LOW_RANK_HALL_MULTIPLICITY_AND_AFFINE_LINE_COUNTEREXAMPLE_20260802.md`;
the fixed-base invariant avoids that obstruction by construction.
