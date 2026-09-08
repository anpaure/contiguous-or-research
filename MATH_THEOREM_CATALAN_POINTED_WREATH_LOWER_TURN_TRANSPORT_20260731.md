# Pointed-wreath lower-turn transport and the circuit obstruction

Date: 2026-07-31  
Status: dimension-uniform exact reduction and sharp circuit-only
obstruction.  The finite `n=4` calibrations concern the two authenticated
AGCF witnesses only.  No all-parameter supply of topology-safe augmenting
packets is claimed.

## 0. Verdict

The lower-turn repair problem for a fixed exact middle wreath factor has a
particularly small signed state.

Let `F` and `G` be upper-exact selections of Boolean diamonds on `[2n]`,
with `F` the canonical MSW/Chung--Feller complement-path factor and `G` an
AGCF.  Index both selections by their common upper colour `U`.  Every
changed column gives a directed lower-colour transport arc

```text
                    L_F(U) -> L_G(U).                 (0.1)
```

If `delta_F(L)` is the lower load of `L` in `F` minus one, then the complete
transport graph `T(F,G)` satisfies

```text
                    div T(F,G) = delta_F.             (0.2)
```

More generally, toggling a set `A` of columns gives

```text
                    delta_(F_A) = delta_F-div A.       (0.3)
```

This is the exact lower-turn ledger.  Directed cycles have zero divergence.
They are precisely the alternating circuits in the lower--upper diamond
graph; a directed triangle is the standard alternating `C6`.  Consequently
no ordered packet made only from palette-transparent circuits or hexagons
can repair a nonzero lower defect.  Every repair contains exactly

```text
                    D(F)=1/2 sum_L |delta_F(L)|       (0.4)
```

unit open transports from surplus colours to holes, in addition to optional
cycles.

There is a separate physical gate.  A column packet preserves
complement-path topology exactly when its Johnson lift passes the
fragment-contraction, degree and antipodal-endpoint tests below.  Thus
"palette-transparent" and "topology-transparent" must not be conflated.
The all-`n` sufficient repair theorem is: find `D(F)` successively
topology-safe open transports.  Each lowers (0.4) by one, while exact middle
and upper ownership and universal residence remain automatic.

At `n=4`, canonical MSW has twelve load-two lower colours and twelve holes,
so `D(F)=12`.  Relative to the symmetry-fixed DLX AGCF, the transport has
49 changed columns and four acyclic weak components.  Relative to the
recursive `n=3 -> 4` AGCF, it has 51 changed columns and five weak
components, whose three cycle cores have lengths `8,5,3`; these are
alternating `C16,C10,C6`.  None of the seven nonempty unions of those cycle
cores is a complement-path factor when toggled from MSW.  Hence the one
literal hexagon in the recursive comparison is neither a lower repair nor
a valid physical first step by itself.

The complete binary endpoint faces are even more rigid.  The union of MSW
with the symmetry-fixed target supports 50 complement paths, but has only
the two endpoint exact covers, of target weights `0,49`.  The recursive
union supports 43 complement paths and again has only its two endpoints, of
weights `0,51`.  Thus no proper monotone prefix inside either literal
MSW--target union preserves complement-path topology.  This is a finite
endpoint-face theorem, not an obstruction to a macro which temporarily uses
a third diamond outside the union.

This result concerns rethreading an already upper-exact pointed wreath.  It
is distinct from the three-sector residual exact-cover problem used to
construct a child AGCF recursively.

## 1. Diamond columns and the pointed-wreath row

Put

```text
 L = binom([2n],n-1),  X = binom([2n],n),
 U = binom([2n],n+1).
```

A Boolean diamond is a pair `(L,U)` with `L subset U`.  If
`U-L={a,b}`, its physical Johnson edge is

```text
                 e(L,U)={L+a,L+b}.                    (1.1)
```

An **upper-exact column selection** is a map

```text
                 f: U -> L,       f(U) subset U.      (1.2)
```

Its physical lift is `{e(f(U),U):U in U}`.  Its lower load is

```text
                 d_f(L)=|{U:f(U)=L}|,
                 delta_f(L)=d_f(L)-1.                 (1.3)
```

The two shores have equal size, so `sum_L delta_f(L)=0`.  The selection is
lower-exact exactly when `delta_f=0`.

If the lift of `f` is a spanning factor into `Cat_n` length-`n`
complement paths, adjoining the pointed coordinate at infinity gives the
exact middle wreath factor of the pointed-wreath theorem.  The upper-column
condition is the containing-interval row, while `delta_f=0` is exactly the
additional rainbow of interior `(n-1)`-turns.  Thus an AGCF is precisely a
complement-path selection with `delta_f=0`.

## 2. Exact signed transport

Let `f,g` be two upper-exact selections.  For every column with
`f(U)!=g(U)`, form the `U`-labelled arc

```text
                         f(U) -> g(U).                 (2.1)
```

Call the resulting directed multigraph `T(f,g)`.  For an arc set `A`, use

```text
 div_A(L)=out_A(L)-in_A(L).                            (2.2)
```

Let `f_A` agree with `g` on the columns of `A` and with `f` elsewhere.

### Theorem 2.1 (lower-turn transport identity)

For every `A subseteq T(f,g)`, one has

```text
                 delta_(f_A)=delta_f-div_A.            (2.3)
```

If `g` is lower-exact, then

```text
                 div T(f,g)=delta_f.                   (2.4)
```

#### Proof

Replacing column `U` removes one occurrence of `f(U)` and adds one
occurrence of `g(U)`.  Therefore it subtracts the tail unit vector and adds
the head unit vector to the lower-load vector.  Summing over `A` gives
(2.3).  Taking all changed columns gives `f_A=g`; if `delta_g=0`, (2.4)
follows.  `square`

### Corollary 2.2 (exact defect flow)

Put

```text
 D(f)=sum_L max(delta_f(L),0)
     =sum_L max(-delta_f(L),0)
     =1/2 sum_L |delta_f(L)|.                          (2.5)
```

If `g` is lower-exact, the arcs of `T(f,g)` decompose into exactly `D(f)`
directed unit paths, each starting at a surplus unit and ending at a hole
unit, together with directed cycles.  Vertices of zero defect may occur
internally on those paths.

#### Proof

Equation (2.4) is an integral unit-capacity flow with prescribed integral
divergence.  The standard flow-decomposition algorithm starts at a vertex
of positive divergence, follows unused outgoing arcs until it reaches a
negative-divergence vertex, removes that path, and repeats.  Exactly
`D(f)` source units and `D(f)` sink units are consumed.  What remains has
zero divergence and hence is a disjoint union of directed circuits.
`square`

### Lemma 2.3 (functional-pseudoforest shape)

If `g` is lower-exact, every lower colour has indegree at most one in
`T(f,g)`.  Consequently every weak component has at most one undirected
cycle.  A cyclic component has one directed cycle, with directed trees
oriented outward from it; an acyclic component is an outward-oriented tree.

#### Proof

There is exactly one `g`-column with lower colour `L`.  It supplies at most
one changed arc entering `L`.  Hence `indeg(L)<=1`.  In a weak component on
`v` vertices, the number of arcs is the sum of the indegrees and is at most
`v`; therefore its cyclomatic number is at most one.  In the unicyclic case
every cycle vertex uses its unique incoming arc on the cycle, which fixes
the stated orientation.  `square`

## 3. Why alternating circuits cannot repair the rainbow

In the bipartite lower--upper diamond graph, a directed cycle

```text
 L_0 -U_0-> L_1 -U_1-> ... -U_(r-1)-> L_0            (3.1)
```

is the alternating circuit

```text
 (L_0,U_0),(L_1,U_0),(L_1,U_1),(L_2,U_1),... .        (3.2)
```

It has length `2r`.  For `r=3`, (3.2) is the standard incidence hexagon.

### Theorem 3.1 (sharp circuit-only obstruction)

For a column packet `A`, the following are equivalent.

1. The packet preserves the complete lower multiplicity vector.
2. `div_A=0`.
3. Its directed transport arcs decompose into directed cycles.
4. Its old/new diamond incidences decompose into alternating circuits.

Therefore a sequence of fixed-decoration/palette-transparent circuit
packets leaves `delta_f` invariant.  It reaches a lower-exact factor if and
only if the initial factor was already lower-exact.

#### Proof

The equivalence of 1 and 2 is (2.3).  Every finite balanced directed
multigraph has an Euler decomposition into directed cycles, proving 2 iff
3.  The correspondence (3.1)--(3.2) proves 3 iff 4.  Applying (2.3) after
each packet proves the final assertion.  `square`

This obstruction is algebraic and precedes every physical-topology test.
An ordered transparent gluing list from the decorated-middle-levels theory
uses exactly such zero-divergence rows; it can transport an already chosen
decoration, but it cannot create the missing lower rainbow of canonical
MSW.

## 4. Exact physical complement-path test

The preceding sections ignore how the selected diamonds join the middle
vertices.  That gate is exact and elementary.

Let `H` be a complement-path factor on `X`.  Delete a set `A` of old
Johnson edges and add an equally large set `B` of distinct new Johnson
edges, where `B` is disjoint from `H-A`.  Put

```text
                         H'=H-A+B.                    (4.1)
```

The components of `H-A` are the retained fragments.  Contract each retained
fragment and let `K_(A,B)` be the multigraph induced by `B`; an edge of `B`
inside one fragment becomes a loop.

### Theorem 4.1 (fragment-contraction complement-path criterion)

The exchange (4.1) is again a spanning factor into `Cat_n` length-`n`
complement paths if and only if all three conditions hold.

1. Every physical middle vertex has degree at most two in `H'`.
2. `K_(A,B)` is loopless and acyclic.
3. Every component of `H'` has two distinct degree-one endpoints `x,y`
   with `y=bar(x)`.

When `A,B` replace the same upper columns, upper exactness is automatic.

#### Proof

The graph `H-A` is a forest.  Adding `B` creates a physical cycle exactly
when `K_(A,B)` has a loop or cycle, so condition 2 is equivalent to
acyclicity of `H'`.  Condition 1 then makes every component a path or an
isolate.

There are `(n+1)Cat_n` middle vertices and `n Cat_n` edges in `H'`.
Thus an acyclic `H'` has exactly `Cat_n` components.  Condition 3 excludes
isolates and says that every component joins complementary `n`-sets.  Their
Johnson distance is `n`, so every component has at least `n` edges.  The
sum over the `Cat_n` components is exactly `n Cat_n`; hence every component
has exactly `n` edges and is a complement geodesic.  The converse is
immediate.  `square`

Call a packet satisfying Theorem 4.1 **topology-transparent**.  This is not
the same as palette transparency: its divergence may be nonzero.

There is also a second, independent circuit obstruction.  Regard the old
and new Johnson edges as a signed graph on the middle vertices.  Its
boundary at `X` is

```text
                  deg_(H')(X)-deg_H(X).              (4.2)
```

Consequently a packet which is a union of physical Johnson-alternating
circuits preserves the complete middle degree vector and hence the endpoint
set of every path factor.  If two complement-path factors have different
endpoint sets, no sequence of such physically degree-transparent circuits
can connect them.  This is different from Theorem 3.1: a lower--upper
diamond circuit preserves lower loads, while a physical Johnson circuit
preserves middle degrees.  Neither notion alone captures a general
topology-safe open augmentor.

## 5. Dimension-free lower-turn augmenting theorem

A directed column packet is a **unit lower augmentor** at the current
selection if

```text
                  div A = e_s-e_t,                    (5.1)
```

where `d(s)>=2` and `d(t)=0`.  Equivalently, after cancelling internal
cycles its transport is one open path from a surplus colour to a hole.

### Theorem 5.1 (ordered topology-safe augmentation)

Let `f_0` be an upper-exact complement-path factor.  Suppose that whenever
`D(f_j)>0` there is a unit lower augmentor `A_j` whose physical exchange is
topology-transparent relative to `f_j`.  Then after exactly `D(f_0)` such
steps the selection is an AGCF.

At every intermediate step:

* all middle vertices and all upper turns remain exact;
* the physical components remain complement geodesics;
* every coordinate flips exactly once on every component, so all positive
  and zero internal residence runs are absent; and
* `D(f_(j+1))=D(f_j)-1`.

#### Proof

By (2.3) and (5.1), the source load drops by one, the hole load rises from
zero to one, and every other lower load is unchanged.  Thus (2.5) drops by
one.  Theorem 4.1 preserves the complement-path factor, while replacing a
diamond in the same `U`-column preserves upper exactness.  A length-`n`
path between complementary `n`-sets flips all `2n` coordinates exactly
once, proving the residence claim.  After `D(f_0)` steps the nonnegative
integer (2.5) is zero, so every lower load is one.  The pointed-wreath
equivalence then gives an AGCF.  `square`

### Corollary 5.2 (sharp missing all-`n` row)

An all-parameter theorem asserting the existence of a topology-transparent
unit lower augmentor in every defective MSW-reachable pointed wreath would
prove the universal AGCF filler theorem by descent.  Alternating-circuit or
hexagon abundance is insufficient: those moves lie in `ker(div)` and do
not satisfy (5.1).

The statement remains useful with larger macros.  A packet of divergence

```text
       sum_i e_(s_i)-sum_i e_(t_i)                    (5.2)
```

repairs the corresponding number of surplus/hole units in one step, if it
passes Theorem 4.1.  Temporary debt is allowed inside an ordered macro, but
the completed macro must have the advertised boundary (5.2).

## 6. Exact `n=4` calibration

The clean-room canonical MSW construction has lower-load histogram

```text
                         1^32 2^12,                   (6.1)
```

and therefore twelve absent lower colours.  Hence `D(MSW_4)=12`.

For the two authenticated AGCF targets, literal occurrence-labelled
upper-column comparison and exhaustive continuation pairing give:

```text
target               common changed sym-diff  weak  minimum decomposition
symmetry-fixed DLX       7      49      98       4   12 open, 0 closed
recursive n=3 -> 4       5      51     102       5   12 open, 1 closed C6
```

The four DLX components are acyclic transport trees.  The recursive target
has two acyclic and three unicyclic components.  Its directed cycle cores
are alternating `C6`, `C10`, and `C16`, with lower/upper label cycles

```text
C6:  (4a,68,51);                (7a,79,5b)
C10: (46,4c,58,54,52);          (6e,7c,5d,57,5e)
C16: (0e,8a,1a,38,d0,15,16,1c);(ae,da,ba,f8,d5,97,9e,1f).
```

Here lower masks and upper labels are hexadecimal.  Exhausting all `2^10`
continuation pairings shows that the `C10` and `C16` cores can be absorbed
into open surplus-to-hole trails; the balanced three-vertex component makes
the `C6` unavoidable.  Exactly 384 pairings attain this one-circuit
minimum.  For the symmetry-fixed target all `2^8` pairings attain the
zero-circuit minimum.  Toggling any of the seven nonempty unions of the
recursive cycle cores from canonical MSW violates the physical degree cap,
so none is a topology-transparent first packet.  Applying or omitting a
cycle core also cannot change (6.1), by Theorem 3.1.

For both targets the two 28-element middle endpoint sets have intersection
14 and symmetric difference 28.  Thus physical degree-transparent circuit
packets are also impossible even if allowed to use edges outside the literal
binary face; an eventual repair aimed at either displayed endpoint must
carry nonzero endpoint current.  This does not obstruct a different AGCF
with the same endpoints as MSW.

The primary occurrence audit stores every removed/added path-step record,
all four/five weak components, every raw cycle, one minimum decomposition,
and the exhaustive pairing census:

```text
scratch/audit_h_catalan_msw_agcf_n4_transport_20260731.py
  SHA 7c33ef2d68912698cafebee1a877798e351e5a68abc10ed54610d827d567b1f5
scratch/h_catalan_msw_agcf_n4_transport_20260731.audit.json
  SHA 432cbaa88a92fd4ae9f25de281ef8833123d373e3288016fce67296779781c38
  payload 2884916cfefc6e868085cc5af320f1fac361870b89889cd0dc1ca7a7ccd787d2
```

There is a stronger exact-cover rigidity statement.  Build the catalogue of
all length-four complement paths supported by the literal union of the MSW
and target diamond edges, and ask for an exact cover of all 70 middle
vertices.

```text
target                 supported paths  exact covers  target weights
symmetry-fixed DLX            50              2          0,49
recursive n=3 -> 4            43              2          0,51
```

The two covers in each row are exactly the MSW and AGCF endpoints.  Hence
there is no proper nonempty binary state which is a complement-path factor,
and therefore no ordering of the literal target-column replacements whose
proper prefixes remain in the complement-path class.  The full replacement
is one valid global endpoint jump; it cannot be refined monotonically inside
this binary face.

This exact finite assertion is independently replayed by

```text
scratch/audit_catalan_msw_agcf_n4_packet_referee_20260731.py
  SHA 4af35b95ee91e67f2f68bc6913bb51388380523232e1a698cb7da54d65b8b523
scratch/catalan_msw_agcf_n4_packet_referee_20260731.audit.json
  SHA 4308ce5463ed0eab19cc4cee6c697648d54e9b52766ed4a599a5a9bb7eedfa5c
  payload fd1284dc756eb23b05d0479b1c97c3adac370468de9ddf9e4ca54871f44a66b5
```

These facts do not rule out an ordered sequence containing open augmenting
macros which use diamonds outside the endpoint union, nor do they assert
that the displayed full MSW-to-AGCF difference has a unique circuit/path
decomposition.  They show exactly why extracting hexagons from the symmetric
difference is not by itself a lower-turn repair theorem.

## 7. Scope

Proved here:

* the exact signed transport identity;
* its pseudoforest and path-plus-circuit normal forms;
* the circuit-only obstruction;
* the exact physical fragment-contraction criterion; and
* the dimension-free ordered augmenting-packet implication.

Not proved here:

* that every canonical MSW factor has a topology-safe open augmentor;
* that the `n=4` full differences admit a bounded-size ordered packetization
  after outside-union diamonds are allowed;
* an all-`n` AGCF, residual three-sector matching, or exact contiguous-OR
  word; or
* preservation of unrelated deep-shadow or compiler state outside the
  universal complement-path filler row.
