# A cloned-hypergraph route to an asymptotic two-sided central row

This note formalizes a purely asymptotic construction for the two adjacent
shadows of the middle layer.  It proves an unconditional result:

> For `k=2m`, there is a sequence of middle `m`-sets of length
> `W+o(W)`, where `W=binom(2m,m)`, whose adjacent intersections cover every
> `(m-1)`-set and whose adjacent unions cover every `(m+1)`-set.

The proof uses a cloned 4-uniform hypergraph, a conflict-free matching theorem,
and a diagonal fixed-girth argument.  It does **not** prove the required longer
shadows, coordinate-run factorability, or pin survival, so it is not yet an
asymptotically optimal universal-OR construction.

All degree and conflict estimates are proved below.  The theorem applications
are audited against their actual hypotheses, including the ambient-size
restriction that prevents one otherwise natural black box from being used.

## 1. The four vertex classes

Let the ground set be `[2m]`, and put

\[
 W=\binom{2m}{m},\qquad
 N=\binom{2m}{m-1}=\binom{2m}{m+1}
   =\frac{m}{m+1}W.                                                  \tag{1.1}
\]

Define a 4-uniform hypergraph `G_m` with four vertex classes:

\[
 \mathcal L=\binom{[2m]}{m-1},\quad
 \mathcal U=\binom{[2m]}{m+1},\quad
 \mathcal M^0,\quad \mathcal M^1,                                  \tag{1.2}
\]

where `mathcal M^0,mathcal M^1` are two labelled clones of the middle layer.
Write `X^a` for clone `a in {0,1}` of the middle set `X`.

For every incidence

\[
 S\in\mathcal L,qquad U\in\mathcal U,qquad S\subset U,           \tag{1.3}
\]

there are exactly two intermediate middle sets.  If

\[
 U\setminus S=\{x,y\},qquad
 X=S\cup\{x\},\quad Y=S\cup\{y\},                                  \tag{1.4}
\]

insert the four hyperedges

\[
 \{S,U,X^a,Y^b\},\qquad (a,b)\in\{0,1\}^2.                          \tag{1.5}
\]

Every hyperedge projects to the Johnson edge `XY` in `J(2m,m)` and records
both of its colours:

\[
 X\cap Y=S,qquad X\cup Y=U.                                       \tag{1.6}
\]

### Lemma 1 (meaning of a matching)

If `M` is a matching in `G_m`, then its projected Johnson graph `P(M)` has:

1. maximum degree at most two;
2. no repeated edge;
3. pairwise distinct lower intersection colours; and
4. pairwise distinct upper union colours.

#### Proof

At most one selected hyperedge can use each clone `X^0` or `X^1`, so the
projected degree of `X` is at most two.  Two lifts of the same projected edge
share its lower vertex `S` and upper vertex `U`, so a matching cannot contain
both.  Finally, every selected hyperedge contains its lower and upper colour
vertices; disjointness makes both colour families rainbow.  QED.

This is exactly why two clones, rather than one, are used: matching in the
auxiliary hypergraph enforces projected maximum degree two without forbidding
a middle set from serving as the internal vertex of a path.

## 2. Exact degrees and codegrees

### Lemma 2 (vertex degrees)

Every lower or upper colour vertex has degree

\[
 d_{\rm col}=4\binom{m+1}{2}=2m(m+1),                               \tag{2.1}
\]

and every middle clone has degree

\[
 d_{\rm clone}=2m^2.                                                \tag{2.2}
\]

Consequently `G_m` is asymptotically regular:

\[
 \frac{\delta(G_m)}{\Delta(G_m)}=\frac{m}{m+1}=1-o(1),qquad
 D:=\Delta(G_m)=2m(m+1).                                            \tag{2.3}
\]

#### Proof

Fix `S in mathcal L`.  Its complement has size `m+1`; choosing two new
elements determines `U`, and each incidence has four clone choices.  This
gives (2.1).  The upper calculation is symmetric.

Fix `X^a`.  The middle set `X` has `m^2` Johnson neighbours, obtained by
choosing one element to remove and one to insert.  For each neighbour, the
clone of the other endpoint has two choices, giving (2.2).  QED.

The exact global counts are

\[
 |V(G_m)|=2N+2W=2W\frac{2m+1}{m+1},                                 \tag{2.4}
\]

and

\[
 |E(G_m)|=4N\binom{m+1}{2}=2m(m+1)N=DN=2m^2W.                       \tag{2.5}
\]

### Lemma 3 (pair codegrees)

The nonzero pair codegrees are as follows.

\[
\begin{array}{c|c}
\text{pair type}&\text{codegree}\ \\hline
S\in\mathcal L,\ U\in\mathcal U,\ S\subset U&4\\
S\in\mathcal L,\ X^a,\ S\subset X&2m\\
U\in\mathcal U,\ X^a,\ X\subset U&2m\\
X^a,Y^b,\ |X\triangle Y|=2&1.
\end{array}                                                         \tag{2.6}
\]

Every other pair has codegree zero.  In particular,

\[
 \Delta_2(G_m)=2m=o(D).                                             \tag{2.7}
\]

#### Proof

The first line is the four clone choices in (1.5).  Given `S subset X`, the
second new element of `U` has `m` choices and the clone at the other middle
endpoint has two choices.  This gives `2m`; the upper case is dual.  Two
adjacent middle sets determine `S=X cap Y` and `U=X union Y` uniquely, and
fixed clones determine one hyperedge.  Two clones of the same underlying
middle set never occur together.  QED.

## 3. What the classical nibble already proves

The Pippenger--Frankl--Rodl almost-perfect matching theorem applies to every
fixed-uniformity sequence whose minimum and maximum degrees are asymptotic and
whose maximum codegree is `o(D)`.  Lemmas 2 and 3 verify these hypotheses.

### Theorem 4 (near-complete two-sided pseudoforest)

There is a matching `M_m subseteq E(G_m)` with

\[
 |M_m|=W-o(W).                                                       \tag{3.1}
\]

Its projection has maximum degree at most two and uses `W-o(W)` distinct
lower and `W-o(W)` distinct upper colours.

#### Proof

The cited matching theorem covers all but `o(|V(G_m)|)=o(W)` vertices.
Therefore its size is `|V(G_m)|/4-o(W)=W-o(W)`.  This is compatible with the
colour-class ceiling `N=W-W/(m+1)=W-o(W)`.  Lemma 1 gives all projected
properties.  QED.

The projection is a disjoint union of paths and cycles, plus isolated middle
vertices.  The theorem alone does not bound the number of cycles: there could
still be linearly many short cycles.  That gap is real and motivates the
conflict system below.

## 4. Conflicts encoding projected short cycles

Fix an integer `L>=3`.  Define a configuration hypergraph `C_L` on
`V(C_L)=E(G_m)`.  A set of `ell` vertices of `C_L`, for `3<=ell<=L`, is a
conflict when:

1. those `ell` hyperedges form a matching in `G_m`; and
2. their projected Johnson edges form a simple cycle of length `ell`.

Thus a `C_L`-free matching projects to a graph of girth greater than `L`.
The word “matching” in item 1 is important: a configuration hypergraph in the
matching theorems is required to consist of forbidden submatchings.  It also
automatically enforces that every projected cycle is rainbow in both colour
systems and uses the two clones alternately at each projected vertex.

Let

\[
 Q=m^2                                                           \tag{4.1}
\]

be the degree of the Johnson graph `J(2m,m)`.

### Lemma 5 (conflict degrees)

For every fixed `L`, constants below depend only on `L`.  For `3<=i<=L`,

\[
 \Delta_i(C_L)=O_L(Q^{i-2})=O_L(D^{i-2}),                            \tag{4.2}
\]

where `Delta_i` is the maximum number of size-`i` conflicts containing one
fixed hyperedge of `G_m`.

For `2<=j<i<=L`,

\[
 \Delta_{i,j}(C_L)=O_L(Q^{i-j-1})=O_L(D^{i-j-1}).                    \tag{4.3}
\]

#### Proof

Fix one lifted edge `e`, whose projection is a fixed Johnson edge `xy`.  An
`i`-cycle containing it is obtained from a path of length `i-1` from `y` back
to `x`.  Ignoring simplicity and the forced final endpoint gives at most
`Q^(i-2)` projected choices.  Once the projected cycle and `e` are fixed,
there are at most `2^(i-2)` ways to distribute the two clones at the remaining
cycle vertices.  Repeated colours or failed disjointness only reduce the
count.  This proves (4.2).

Now fix `j` lifted edges.  If they extend to a simple projected cycle, their
projection is a disjoint union of `c>=1` paths; if it already contains a
smaller cycle, there is no extension.  There are only `O_L(1)` cyclic orders
and orientations of these path components.  The `i-j` new edges form `c`
nonempty connecting paths between prescribed endpoints.  A connecting path
of length `t` has at most `Q^(t-1)` choices.  Multiplying over the `c` gaps
gives at most

\[
 Q^{(i-j)-c}\le Q^{i-j-1}
\]

projected completions.  The clone multiplicity is at most `2^i`, proving
(4.3).  QED.

There are no size-two conflicts.  Consequently:

\[
 \text{maximum common 2-degree of }C_L=0,                            \tag{4.4}
\]

and the maximum 2-codegree of `G_m` with `C_L`, in the terminology of
Delcourt--Postle, is also zero.

## 5. Auditing the conflict-free theorem

We use the small-codegree coloring corollary in Delcourt and Postle,
[Finding an almost perfect matching in a hypergraph avoiding forbidden
submatchings](https://arxiv.org/abs/2204.08981), specialized to one large
matching.  For fixed uniformities `r,g` and fixed `beta>0`, it says, in the
notation relevant here:

* `Delta(G)<=D` and `Delta_2(G)<=D^(1-beta)`;
* `Delta_i(C)<=alpha D^(i-1) log D`;
* `Delta_(i,j)(C)<=D^(i-j-beta)`;
* the two additional 2-codegrees are at most `D^(1-beta)`;

then there is a `C`-free matching of size at least

\[
 \frac{|E(G)|}{D}(1-D^{-\alpha}),                                   \tag{5.1}
\]

for a positive `alpha` depending only on the fixed parameters.  Importantly,
this theorem has no upper bound on `|V(G)|`.

### Lemma 6 (all Delcourt--Postle hypotheses hold)

For every fixed `L`, the pair `(G_m,C_L)` satisfies the theorem above for all
sufficiently large `m`.

#### Proof

Take `r=4`, `g=L`, and for instance `beta=1/3`.  Lemma 3 gives

\[
 \Delta_2(G_m)=2m\le D^{2/3}=D^{1-\beta}
\]

for large `m`.  By Lemma 5,

\[
 \Delta_i(C_L)=O_L(D^{i-2})
       \le \alpha D^{i-1}\log D
\]

for every fixed positive theorem-constant `alpha` once `D` is large.  Also,

\[
 \Delta_{i,j}(C_L)=O_L(D^{i-j-1})
       \le D^{i-j-1/3}.
\]

Finally both extra 2-codegrees vanish by (4.4).  These are all the listed
hypotheses.  QED.

Since `|E(G_m)|/D=N` exactly, we obtain:

### Theorem 7 (fixed-girth near-complete matching)

For every fixed `L`, there is a matching `M_(m,L)` such that

\[
 |M_{m,L}|=N-o_L(W)=W-o_L(W),                                       \tag{5.2}
\]

and its projected graph has maximum degree at most two and no cycle of length
at most `L`.

### Why the Glock--Joos--Kim--Kuhn--Lichev black box cannot be cited here

The original conflict-free matching theorem in
[Conflict-free hypergraph matchings](https://arxiv.org/abs/2205.05564)
contains an ambient-size hypothesis of the form

\[
 |V(G)|\le \exp(D^{\varepsilon^3})                                  \tag{5.3}
\]

as well as `Delta_2(G)<=D^(1-epsilon)`.  In our hypergraph,

\[
 |V(G_m)|=\exp(\Theta(m)),\qquad D=\Theta(m^2),\qquad
 \Delta_2(G_m)=\Theta(m)=D^{1/2+o(1)}.                              \tag{5.4}
\]

The codegree condition forces `epsilon<=1/2+o(1)`.  Then

\[
 D^{\varepsilon^3}\le m^{1/4+o(1)}=o(m),                            \tag{5.5}
\]

so (5.3) fails exponentially.  Thus that theorem, and later black boxes with
the same ambient restriction, do not justify this application.  The
Delcourt--Postle small-codegree theorem is used precisely because its statement
does not impose (5.3), and Lemma 6 verifies its stronger conflict-codegree
requirements directly.

## 6. From fixed girth to an asymptotic linear forest

The projected graph in Theorem 7 has maximum degree two, so its cycles are
vertex-disjoint.  Since every cycle has length greater than `L`, deleting one
edge from each cycle deletes at most

\[
 \frac{W}{L+1}                                                       \tag{6.1}
\]

edges and produces a linear forest.

For every fixed `eta>0`, first choose `L>2/eta`, then take `m` sufficiently
large in Theorem 7.  The resulting linear forest has at least

\[
 W-o_L(W)-\frac{W}{L+1}\ge(1-\eta)W                                \tag{6.2}
\]

edges.  A standard diagonal choice makes `L=L(m)` tend to infinity slowly:
for each integer `t`, choose a threshold beyond which the fixed-`L=t` theorem
has error at most `W/t`, and use the largest eligible `t`.  This proves the
following single asymptotic statement.

### Theorem 8 (two-sided rainbow near-spanning linear forest)

There is a spanning linear forest `F_m` on the `W` middle sets with

\[
 |E(F_m)|=W-o(W),                                                    \tag{6.3}
\]

such that its edge intersections are distinct and cover all but `o(W)` of
the `(m-1)`-sets, while its edge unions are distinct and cover all but `o(W)`
of the `(m+1)`-sets.

#### Proof

Use the diagonal fixed-girth matching and delete one edge from every remaining
cycle.  Deletion preserves the two rainbow properties.  Add every unused
middle vertex as an isolated component, making the forest spanning.  Since a
forest on `W` vertices with `W-o(W)` edges has `o(W)` components, it is a
near-spanning linear forest in the required sense.  QED.

No endpoint-connectability in the Johnson graph is needed for the next
corollary.  Orient each path arbitrarily and concatenate its vertex list with
the lists of the other path and singleton components.  The seams may be
arbitrary pairs of middle sets; they do not destroy any internal colour.

### Corollary 9 (near-complete adjacent-shadow permutation)

There is a permutation

\[
 T_1,T_2,\ldots,T_W
\]

of all middle `m`-sets whose adjacent intersections contain all but `o(W)`
rank-`m-1` masks and whose adjacent unions contain all but `o(W)` rank-`m+1`
masks.

## 7. Repairing the missing adjacent colours with `o(W)` repetitions

Corollary 9 misses only `o(W)` colours on either side.  They can be repaired
without a matching theorem.

For every missing `(m-1)`-set `S`, choose any `(m+1)`-set `U` containing it.
The interval `[S,U]` contains exactly two middle sets `X,Y`; append the pair
`X,Y`.  Its intersection is `S`.  For every still-missing `(m+1)`-set `U`,
choose any `(m-1)`-subset `S` and append its two intermediate middle sets;
their union is `U`.

There are `o(W)` missing colours, and every repair adds two entries.

### Theorem 10 (unconditional asymptotic two-sided adjacent-shadow row)

For `k=2m`, there is a sequence `T` of middle `m`-sets with

\[
 |T|=W+o(W)                                                         \tag{7.1}
\]

such that

\[
 \{T_i\cap T_{i+1}\}\supseteq\binom{[2m]}{m-1},\qquad
 \{T_i\cup T_{i+1}\}\supseteq\binom{[2m]}{m+1}.                   \tag{7.2}
\]

Every middle set also occurs, because the initial part of `T` is the
permutation from Corollary 9.

This theorem establishes the previously conjectural adjacent two-sided
central skeleton asymptotically, allowing `o(W)` repeated middle vertices.

## 8. What this does and does not solve

### Proved

1. The cloned 4-graph is asymptotically regular with `Delta_2=o(D)`.
2. A classical nibble selects `W-o(W)` simultaneous lower/upper colours and
   enforces projected maximum degree two.
3. Fixed projected girth can be imposed using the Delcourt--Postle theorem;
   all its degree and codegree hypotheses hold.
4. A diagonal fixed-girth argument yields a two-sided rainbow linear forest
   with `W-o(W)` edges and `o(W)` path components.
5. Adding `o(W)` explicit two-vertex repairs gives a `W+o(W)` middle row with
   complete adjacent intersection and union shadows.

### Not proved

The row from Theorem 10 is not known to have:

* complete intersection/union shadows at depths two and larger;
* the long coordinate runs required to factor it with near-optimal delay;
* a lower-band growth-diagram completion; or
* coordinatewise pin survival.

Therefore Theorem 10 does not yet imply

\[
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]

It does remove one genuine obstruction: asymptotically complete simultaneous
rank-`m-1` and rank-`m+1` adjacent shadows, with only `o(W)` repetitions, now
follow from general matching theory rather than an unproved Catalan
linearization conjecture.  The next asymptotic theorem must add factorability
and the deeper shadows without losing the `o(W)` error budget.
