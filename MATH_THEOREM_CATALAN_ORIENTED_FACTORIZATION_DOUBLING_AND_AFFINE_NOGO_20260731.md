# Ordered-diamond factorization: exact doubling theorem and the local affine no-go

Date: 2026-07-31  
Status: general implication and scoped no-go proved; literal `m=2,3`
factorizations independently replayed; no all-`m` factorization is claimed

## 0. Verdict

Let `|Omega|=2m` and put

\[
 \mathcal L={\binom\Omega{m-1}},\qquad
 \mathcal X={\binom\Omega m},\qquad
 \mathcal U={\binom\Omega{m+1}},
\]

\[
 d={m(m+1)\over2},\qquad q=2d=m(m+1).
\]

An ordered diamond is

\[
        \alpha=(L,U,T,H),\qquad L=T\cap H,\quad U=T\cup H,
                                                        \tag{0.1}
\]

with `T != H`.  A proper `q`-colouring means that no colour repeats at any
fixed lower, upper, tail, or head resource.

This note proves three facts.

1. Every two-balanced one-factorization of the unoriented diamond graph
   canonically produces a proper `q`-colouring of all ordered diamonds.
   A forest factor produces two acyclic ordered colour classes.
2. The converse holds exactly inside the **reverse-paired** subclass.  The
   literal `m=2,3` colourings are not in that subclass, so the ordered route
   is genuinely broader than merely renaming the existing two-balanced
   route.
3. The tempting explanation `q=|AGL(1,m+1)|` does not yield a uniform local
   group rule.  More generally, no construction obtained by coherently
   labelling every `(m+1)`-set with one common `(m+1)`-letter alphabet and
   encoding its ordered pair injectively can satisfy the two diamond shores
   for any `m>=2`.  The obstruction propagates through a connected odd
   graph.

The finite replay gives

| `m` | `q` | class size | acyclic classes | cyclic classes |
|---:|---:|---:|---:|---:|
| 2 | 6 | 4 | 6 | 0 |
| 3 | 12 | 15 | 10 | 2 |

Thus `chi=q` and an acyclic colour are true at `m=2,3`.  The `m=3`
certificate has no nonidentity coordinate automorphism even after arbitrary
renaming of colours.  These are positive finite data, not an explicit group
law and not an all-`m` proof.

## 1. The exact ordered conflict graph

Let `C_m` have the ordered diamonds as vertices, with two atoms adjacent
when they share any one of `L,U,T,H`.  Every lower fibre and every upper
fibre is a clique of size

\[
               (m+1)m=q.                              \tag{1.1}
\]

Consequently `chi(C_m)>=q`.  A proper `q`-colouring has a stronger forced
structure: every colour occurs exactly once at every lower and every upper
resource, and at most once at every tail and every head.  Hence every colour
is an ordered four-transversal, except that its directed trace can contain
cycles.

Therefore the all-colours strengthening of Catalan Linear Matching is

\[
 \boxed{\chi(C_m)=q\text{ and some colour class is acyclic}.}          \tag{1.2}
\]

This is stronger than asking for one acyclic ordered four-transversal.

## 2. Doubling a two-balanced one-factorization

Let `B_m` be the unoriented diamond graph on
`mathcal L sqcup mathcal U`.  Its edges are in bijection with Johnson edges

\[
 (L,U)\longmapsto\{L+a,L+b\},\qquad U-L=\{a,b\}.       \tag{2.1}
\]

Suppose

\[
                E(B_m)=P_1\sqcup\cdots\sqcup P_d       \tag{2.2}
\]

is a two-balanced one-factorization: every `P_j` is a perfect matching of
`B_m`, and its Johnson lift `G_j` has maximum degree at most two.

### Theorem 2.1 (orientation doubling)

Every factorization (2.2) gives a proper `q=2d` colouring of all ordered
diamonds.  If `G_j` is a linear forest, both ordered colours arising from
`P_j` are acyclic.

#### Proof

Orient each path and each cycle component of `G_j` consistently.  For a
physical edge oriented `T -> H`, give the atom `(L,U,T,H)` colour `(j,+)`
and its reverse atom `(L,U,H,T)` colour `(j,-)`.

At a fixed `L` or `U`, the perfect matching `P_j` has one unoriented edge;
its two atoms receive the two colours `(j,+),(j,-)`.  Thus every one of the
`2d=q` colours occurs exactly once on that fibre.

At a middle set `X`, a consistently oriented maximum-degree-two graph has
indegree and outdegree at most one.  Hence colour `(j,+)` occurs at most once
with tail `X` and at most once with head `X`; the reverse colour has the same
property.  This proves properness in all four resource classes.

The directed trace of `(j,+)` is the chosen orientation of `G_j`, and that
of `(j,-)` is its reversal.  They are acyclic exactly when `G_j` is.
\(\square\)

This theorem explains the numerical `q=m(m+1)` immediately: it is twice
the ordinary diamond degree.  It does **not** prove that a two-balanced
one-factorization exists.

## 3. The reverse-paired boundary

Call a proper ordered colouring **reverse-paired** if its colours admit a
fixed-point-free involution `c -> bar(c)` such that reversing every atom of
colour `c` gives exactly the atoms of colour `bar(c)`.

### Proposition 3.1

Reverse-paired proper `q`-colourings are equivalent to two-balanced
one-factorizations together with component orientations.

#### Proof

The forward construction is Theorem 2.1.  Conversely, merge every colour
pair `{c,bar(c)}` and forget atom orientation.  At a lower or upper resource,
the two paired atoms are the two orientations of one underlying diamond, so
each merged class is a perfect matching of `B_m`.  Tail and head injectivity
show that at most two merged physical edges meet a middle vertex.  The
merged classes partition all unoriented diamonds and hence form a
two-balanced one-factorization. \(\square\)

The authenticated finite colourings are not reverse-paired.  At `m=2`, the
reverse atoms of each colour occupy four distinct colours; at `m=3`, the
numbers of reverse colours seen by one colour have profile

\[
                  5^1\,7^2\,8^5\,9^3\,10^1.          \tag{3.1}
\]

In particular no colour has a unique reverse partner.  The direct ordered
route can therefore escape an obstruction confined to every unoriented
two-balanced factorization.

## 4. Why the obvious affine group rule cannot work

The identity

\[
                  q=m(m+1)                            \tag{4.1}
\]

is the order of a sharply two-transitive affine group on `m+1` letters when
such a group exists.  This suggests labelling every local `(m+1)`-set and
using the unique group element carrying a fixed ordered base pair to the
ordered pair `(a,b)`.  The following theorem rules out that entire coherent
local-label scheme, independently of whether the alphabet supports a group.

### Theorem 4.1 (odd-graph label propagation)

Let `Q` be a set of size `m+1`.  There do not exist bijections

\[
                 ell_S:S\longrightarrow Q
       \qquad(S\in\tbinom\Omega{m+1})                 \tag{4.2}
\]

such that whenever `A,U` are `(m+1)`-sets with
`A intersection U={a,b}`, the ordered-pair labels agree:

\[
          (ell_A(a),ell_A(b))=(ell_U(a),ell_U(b)).     \tag{4.3}
\]

Consequently no colour rule obtained by applying one injective encoding to
those local ordered-pair labels can colour both the lower and upper diamond
fibres.

#### Proof

Fix `x in Omega`.  Form a graph whose vertices are the `(m+1)`-sets
containing `x`, joining `S,T` when `|S intersection T|=2`.  Delete `x` and
then take complements in `Omega-{x}`.  A vertex becomes an `(m-1)`-subset
of a `(2m-1)`-set, and adjacency becomes disjointness.  The graph is
therefore the odd graph

\[
                         KG(2m-1,m-1).                \tag{4.4}
\]

It is connected.  One elementary proof is that the Johnson graph on
`(m-1)`-subsets is connected, and if two such sets differ by one element,
the complement of their union has size `m-1` and is disjoint from both;
thus every Johnson step is a two-edge walk in (4.4).

Equation (4.3) propagates `ell_S(x)` across every edge, so connectedness
makes it a global value `ell(x)`, independent of `S`.  Any two coordinates
`x,y` occur together in some `(m+1)`-set; bijectivity of its local labelling
forces `ell(x) != ell(y)`.  Hence `2m` coordinates require `2m` distinct
values in the `(m+1)`-set `Q`, impossible for `m>=2`. \(\square\)

For a sharply two-transitive group, the group element carrying a fixed
ordered pair to `(ell_S(a),ell_S(b))` determines that ordered pair
injectively.  Equality of the group colours on the two diamond shores would
therefore imply (4.3), so Theorem 4.1 applies.

This is deliberately scoped.  It does not rule out a context-dependent
group construction with noncoherent gauges, nor a recursive or switching
construction.  It says the numerical coincidence (4.1) is not by itself an
all-dimensional affine factorization.

## 5. Finite replay and current target

The replay script

```text
scratch/audit_catalan_oriented_factorization_m2_m3_20260731.py
```

independently reconstructs all ordered atoms, decodes the Kissat models,
checks all four resource partitions, counts directed cycles, tests reverse
pairing, and enumerates coordinate automorphisms up to arbitrary colour
renaming.  Its frozen output is

```text
scratch/catalan_oriented_factorization_m2_m3_20260731.audit.json.
```

The exact census is:

* `m=2`: six classes of size four, all six acyclic; six coordinate
  automorphisms up to colour renaming;
* `m=3`: twelve classes of size fifteen, ten acyclic and two with one cycle;
  only the identity coordinate automorphism.

The clean all-`m` statement still missing is (1.2).  The finite witnesses
show that the direct ordered factorization can be better than orientation
doubling, but their lack of reverse pairing and the trivial `m=3` symmetry
mean they currently supply no reusable group law.

