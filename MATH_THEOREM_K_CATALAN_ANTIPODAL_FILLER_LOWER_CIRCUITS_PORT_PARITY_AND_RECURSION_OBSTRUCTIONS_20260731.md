# Lower-turn circuits, port parity, and recursion obstructions for antipodal Catalan fillers

Date: 2026-07-31  
Status: exact all-parameter matching/circuit theorems, a positive-density
canonical-MSW repair lower bound, a fixed-port obstruction at `n=3`, an
exact local repair atom, and independently replayed fillers at `n=2,3,4`.
The all-parameter three-sector residual matching theorem remains open.

## 0. Scope and result

Let

\[
 C_n=\frac1{n+1}\binom{2n}{n},\qquad
 M_n=\binom{2n}{n},\qquad
 N_n=\binom{2n}{n-1}=nC_n.                            \tag{0.1}
\]

An antipodal-geodesic Catalan filler (`AGCF`) is a partition of the middle
level of a `2n`-set into `C_n` Johnson paths

\[
 X_0,X_1,\ldots,X_n=\overline{X_0}                    \tag{0.2}
\]

whose `N_n` lower turns and `N_n` upper turns are both bijective.
Every coordinate flips exactly once on every component, so this is the
universal-residence filler required by the independent filler theorem.

The updated
`MATH_THEOREM_CATALAN_INDEPENDENT_FILLER_GUARD_FACTORIZATION_20260731.md`
proves that the canonical Chung--Feller/MSW construction already gives the
middle partition, upper turns, and universal residence.  The sole missing
row is the lower-turn bijection.  The conclusions below sharpen that row.

1. The lower row is an exact partition-matroid circuit condition.  The
   palette-only common basis exists for every `n`; the obstruction is its
   correlation with the complement-geodesic middle factor.
2. Lower repair is intrinsically nonlocal between physical paths.
3. Canonical MSW has at least `C_(n-3)` pairwise disjoint hereditary lower
   collisions.  Any upper-preserving repair changes at least that many
   upper blocks and touches at least that many distinct physical paths.
4. At `n=3`, retaining all five canonical Dyck endpoint pairs is impossible,
   although an endpoint-flexible AGCF exists.  The obstruction is an exact
   parity law for the first and last coordinates.
5. The `n=3` repair is a literal twenty-state atom.  Its resource exports
   give an exact sufficient port-circulation theorem, but a formal five-atom
   circulation is physically indivisible without a branched port router.
6. An intact tensor bank of smaller AGCFs is a sealed separator.  Embedding
   a fixed `a`-filler in the central sector of parameter `N=a+b` requires
   at least

   \[
   K_*=\left\lceil\frac{
       \binom{2N}{N}-\binom{2a}{a}\binom{2b}{b}}{N}\right\rceil \tag{0.3}
   \]

   deleted suspended edges before a global AGCF can result.  For fixed
   `a=3,4`, this is asymptotically at least `11/16` and `93/128` of all
   global path units.  Conversely, palette/socket-disjoint paired punctures exist
   at this full scale up to `o(C_N)` loss, isolating global socket routing as
   the remaining tensor gate.  Small fillers are bases, not sealed tensor
   generators.
7. Global AGCFs exist at `n=2,3,4`, and the `n=4` filler can be chosen on the
   exact three-sector recursive face over the `n=3` filler.

No claim about downstream rooted sides, deep shadows, or the lower compiler
is made here.

## 1. Exact lower-turn matroid and functional circuit

Let `J_n` be the set of Johnson edges on `binom(Omega,n)`.  For
`e={A,B}`, put

\[
                \ell(e)=A\cap B,\qquad u(e)=A\cup B.  \tag{1.1}
\]

Let `L` and `U` be the partition matroids on `J_n` whose parallel classes
are the lower and upper colours.  Thus

\[
 r_{\mathsf L}(S)=|\ell(S)|,
 \qquad
 r_{\mathsf U}(S)=|u(S)|.                              \tag{1.2}
\]

### Theorem 1.1 (exact circuit criterion)

Let `F` be an upper-rainbow antipodal-geodesic middle factor.  The following
are equivalent:

1. `F` is an AGCF;
2. `F` has bijective lower turns;
3. `r_L(F)=N_n`;
4. `F` contains no circuit of `L`.

The circuits in item 4 are exactly pairs of edges with a common lower turn.

#### Proof

The middle, topology, antipodality, and upper rows are hypotheses.  There
are exactly `N_n` selected edges and exactly `N_n` possible lower colours.
Consequently the lower row is bijective exactly when its support has order
`N_n`, equivalently when the selected set is independent in the indicated
partition matroid.  The minimal dependent sets of a partition matroid are
pairs in one block. `square`

Because `u:F -> binom(Omega,n+1)` is bijective, define

\[
 \sigma_F(e)=u^{-1}\!\left(\overline{\ell(e)}\right). \tag{1.3}
\]

### Corollary 1.2 (functional form)

\[
 \boxed{F\text{ is lower-rainbow}\iff\sigma_F
        \text{ is a permutation of }F.}               \tag{1.4}
\]

Indeed, the indegree of `f` is the multiplicity of the lower colour
`overline(u(f))`.  Thus the desired lower row is exactly that the functional
digraph of `sigma_F` be a directed cycle cover.

### Theorem 1.3 (palette-only integrality is automatic)

Let `B_n` be the bipartite graph with shores

\[
 \binom{\Omega}{n-1},\qquad \binom{\Omega}{n+1},
\]

and edge `L--U` when `L subset U`.  It is

\[
                         \binom{n+1}{2}\text{-regular}. \tag{1.5}
\]

Hence it decomposes into perfect matchings.  Each matching lifts uniquely
to `N_n` Johnson edges with both palettes exact.

#### Proof

A fixed lower colour has `n+1` available outside coordinates and is
contained in `binom(n+1,2)` upper colours.  A fixed upper colour contains
the same number of lower colours.  A regular bipartite graph has a perfect
matching by Hall; delete it repeatedly.  If `U-L={a,b}`, the unique lift is
the Johnson edge between `L+a` and `L+b`. `square`

More generally, on a restricted bank `B subset J_n`, a simultaneous palette
basis exists if and only if

\[
 r_{\mathsf U}(A)+r_{\mathsf L}(B\setminus A)\ge N_n
                    \quad(A\subseteq B),              \tag{1.6}
\]

the ordinary matroid-intersection inequality.  Equivalently, the restricted
upper-versus-lower colour graph has a perfect matching.  Relative common
bases differ by alternating even colour circuits.

Theorem 1.3 closes the palette-only question.  It does not control physical
middle degrees, linearity, or complementary endpoints; those are the actual
integral-correlation gate.

## 2. Lower repair must be cross-component

Write one complement geodesic as

\[
 X_i=\{a_{i+1},\ldots,a_n\}\cup\{b_1,\ldots,b_i\},
                 \qquad 0\le i\le n.                  \tag{2.1}
\]

Its turns are

\[
\begin{aligned}
 \ell_i&=\{a_{i+1},\ldots,a_n\}\cup\{b_1,\ldots,b_{i-1}\},\\
 u_i&=\{a_i,\ldots,a_n\}\cup\{b_1,\ldots,b_i\}.
\end{aligned}                                         \tag{2.2}
\]

### Lemma 2.1 (same-path exclusion)

For `n>=2`,

\[
                   \overline{\ell_i}\ne u_j
             \qquad(1\le i,j\le n).                  \tag{2.3}
\]

#### Proof

One has

\[
 \overline{\ell_i}
 =\{a_1,\ldots,a_i\}\cup\{b_i,\ldots,b_n\}.          \tag{2.4}
\]

Equality with `u_j` first forces

\[
 \{a_1,\ldots,a_i\}=\{a_j,\ldots,a_n\}.
\]

Because the `a` labels are distinct, this forces `i=n,j=1`.  The `b` parts
would then force `b_n=b_1`, impossible for `n>=2`. `square`

### Corollary 2.2 (path-interaction state)

Every arc `e -> sigma_F(e)` in an AGCF goes between two different physical
paths.  Contracting each path gives a loopless directed multigraph with
indegree and outdegree exactly `n` at every vertex.

In particular, no path-private selector can enforce the missing lower row.
Also no nontrivial AGCF is closed under edge complementation: complementation
would send a component containing `X` to the same component containing
`bar X`, and a complementary edge on that component would contradict
Lemma 2.1.

### Lemma 2.3 (alteration lower bound)

For an upper-rainbow factor define

\[
 D(F)=N_n-r_{\mathsf L}(F)
     =\sum_L(m_L(F)-1)_+.                              \tag{2.5}
\]

If another upper-rainbow selection `F'` differs from `F` in `t` upper-colour
blocks, then

\[
 r_{\mathsf L}(F')\le r_{\mathsf L}(F)+t.             \tag{2.6}
\]

Consequently `F'` lower-rainbow implies `t>=D(F)`.  A `2s`-edge alternating
colour circuit changes `s` selected blocks, so the total selected half-
support of any circuit repair is at least `D(F)`.

#### Proof

Each changed upper block introduces at most one lower colour not previously
in the support.  This proves (2.6), and the conclusions follow. `square`

## 3. A hereditary positive-density collision in canonical MSW

Use `1` for an up-step.  For every Dyck word `V` of semilength `n-3`, the
two canonical roots

\[
             A=111000V,\qquad B=110100V               \tag{3.1}
\]

begin their canonical MSW paths as

\[
\begin{array}{c|ccc}
A&111000V&101001V&100101V\\
B&110100V&110001V&100011V.
\end{array}                                            \tag{3.2}
\]

This follows directly from the flaw-layer successor rule; equivalently it
is the first two steps of the audited concatenation identity for a Dyck
prefix followed by a Dyck suffix.  The suffix is a spectator during these
steps.  The second lower turns in (3.2) coincide:

\[
 (101001V)\cap(100101V)
 =(110001V)\cap(100011V)=100001V.                     \tag{3.3}
\]

### Theorem 3.1 (hereditary MSW defect)

For every `n>=3`, the canonical MSW factor has

\[
                      D(\mathrm{MSW}_n)\ge C_{n-3}.   \tag{3.4}
\]

The collision pairs in this proof use disjoint edge pairs on disjoint
physical path pairs.  Hence every upper-preserving lower-rainbow repair
changes at least `C_(n-3)` selected upper blocks and touches at least
`C_(n-3)` distinct physical paths.

#### Proof

Distinct `V` give distinct labels `100001V`; each has multiplicity at least
two by (3.3).  The roots with prefixes `111000` and `110100` are all
distinct, and (3.2) shows that the displayed edges are distinct.  Thus the
excess sum (2.5) is at least the number `C_(n-3)` of suffixes.  To remove
each duplicate, at least one edge in its disjoint pair must change; the
last assertion follows. `square`

Moreover

\[
                  \frac{C_{n-3}}{C_n}\longrightarrow\frac1{64}. \tag{3.5}
\]

So an `o(C_n)`-block repair of canonical MSW is impossible.  Equivalently,
the repair must touch a positive density, asymptotically at least `1/64`, of
the original physical paths.  This is not a positive density of all
`N_n=nC_n` edge blocks, and it does not exclude a bounded-depth move applied
on `Theta(C_n)` paths.  The conclusion is architecture-specific: it is not
a no-go for another exact wreath factor or for the global AGCF problem.

## 4. Exact port parity and the `n=3` fixed-port obstruction

Suppose every oriented root contains coordinate `1` and excludes coordinate
`2n`.  On a path let `r` be the transition which removes `1`, and `s` the
transition which inserts `2n`.

Let `A` be the lower colours containing `1` and excluding `2n`, and `B` the
upper colours with the same condition.  This path contributes

\[
             \min(r-1,s)+\min(r,s-1)                  \tag{4.1}
\]

members to `A union B`.  The number (4.1) is even if `r=s` and odd if
`r!=s`.

### Lemma 4.1 (direct-swap parity)

In an exact two-palette factor,

\[
 \#\{P:r_P=s_P\}\equiv C_n\pmod2.                    \tag{4.2}
\]

#### Proof

There are

\[
 |A|=|B|=\binom{2n-2}{n-2},                           \tag{4.3}
\]

so the total contribution is even.  By (4.1), the number of paths with
`r!=s` is even.  Subtracting it from the total `C_n` proves (4.2). `square`

At `n=3`, orient from the five Dyck roots

\[
 123,124,125,134,135                                  \tag{4.4}
\]

to their complements.  A direct `1 -> 6` swap cannot occur in any clean
vertex-disjoint path with these ten fixed ports:

* at transition two, the only nonport rank-three set containing `1` and
  excluding `6` is `145`; its direct swap is the occupied port `456`;
* at transition one, every root except `123` swaps directly to an occupied
  complementary port; `123 -> 236` is the only exception, but each possible
  next state `346,356,246,256` is an occupied port;
* transition three is the reversed transition-one argument.

Since `C_3=5` is odd, Lemma 4.1 requires an odd number of direct swaps.  We
obtain the following sharp conclusion.

### Theorem 4.2 (fixed canonical ports fail at `n=3`)

No AGCF at `n=3` retains all five canonical Dyck endpoint pairs.

This does not refute existence: the explicit AGCF in Section 7 changes two
endpoint pairs.  More generally, since

\[
 v_2(C_n)=s_2(n+1)-1,                                 \tag{4.5}
\]

`C_n` is odd exactly when `n=2^q-1`; any fixed-Dyck-port construction in
those dimensions must export an odd direct extreme-coordinate swap.

## 5. The exact `n=3` repair atom and a sufficient circulation theorem

The canonical `n=3` lower multiset duplicates `16,34` and misses `14,36`.
The explicit AGCF has signed lower delta

\[
                       +14+36-16-34.                  \tag{5.1}
\]

It keeps the canonical endpoint pairs based at masks `13,19,21`, while
replacing

\[
 (7,56),(11,52)\quad\text{by}\quad(25,38),(26,37).   \tag{5.2}
\]

In set notation its endpoint degree flux is

\[
 +\{123,456,124,356\}-\{145,236,245,136\},           \tag{5.3}
\]

where a positive sign means that an old endpoint becomes internal.  The
middle and upper resource deltas are zero.

The same twenty-state substitution may be suspended over a spectator set
`K`: every label in (5.1)--(5.3) is replaced by its union with `K`.  This is
a literal local carrier replacement, not a claim that the suspended
fragment is already a global complement path.

### Theorem 5.1 (resource-circulation sufficiency)

Let a middle-exact, upper-rainbow factor be modified by local replacements
whose interiors are resource-disjoint and whose middle and upper multiset
deltas are zero.  For replacement `j`, record

1. its signed lower-colour delta `Delta_j`;
2. its signed boundary degree flux `partial_j`; and
3. the occurrence-labelled pairing of its retained path fragments after
   contraction.

The modified object is an AGCF provided that

\[
 m_L^{\rm old}+\sum_j\Delta_j(L)=1\quad\text{for every lower colour }L, \tag{5.4}
\]

the summed degree flux gives degree one exactly at the final endpoints and
degree two elsewhere, and the contracted fragment pairing is a linear
forest whose endpoint pairs are complementary.  More generally, zero delta
may be replaced by the explicit requirement that the summed middle and
upper resource equations remain exact.

#### Proof

Resource-disjointness makes the signed ledgers additive.  The hypotheses
preserve the exact middle and upper rows, while (5.4) is exactly lower
bijectivity.  The degree and contracted-pairing hypotheses give the required
physical path forest; its prescribed endpoint pairs and total edge count
make every component a complement geodesic. `square`

This three-row export `(Delta,partial,pairing)` is minimal in the following
sense: none is implied by the other two.  Palette balance alone permits
cycles or wrong endpoint monodromy; flux balance alone permits lower repeats;
and correct pairing alone does not restore either resource ledger.

### A formal pentagon and its physical obstruction

Let

\[
 \tau=(1\ 4\ 2\ 5\ 3),\qquad \tau(6)=6.              \tag{5.5}
\]

Then `tau` sends the positive port bank in (5.3) to the negative bank.
The formal orbit sum of five conjugate atoms has zero endpoint flux.  Its
nonzero lower delta is

\[
 +\{13,14,24,25,35\}-\{12,15,23,34,45\}.             \tag{5.6}
\]

Thus endpoint cancellation does not force lower inertness.

However the formal pentagon is not a literal resource-disjoint deck.  A
complementary port pair of a suspended six-block atom has intersection `K`
and union `K union B`, where `B` is its six-coordinate carrier.  If the two
ports are identified with one complementary positive pair of a neighbour,
their intersection and union force the neighbour to have the same `K` and
the same `B`; the two twenty-state supports coincide.  Therefore a
resource-disjoint circulation must split each complementary port pair among
different downstream carriers.  A simple atom-to-atom cycle is impossible;
a literal recursion needs a branched per-port router or a larger carrier.

## 6. Sealed central tensor banks and the graded recursion state

Split the ambient `2N`-set as

\[
 \Omega=A\mathbin{\dot\cup}B,\qquad
 |A|=2a,\quad |B|=2b,\quad N=a+b.                    \tag{6.1}
\]

For every `b`-set `Y subset B`, suspend one fixed parameter-`a` AGCF on
`A` by adjoining `Y` to every vertex.  The resulting intact bank partitions
the central sector

\[
 \mathcal M_a=\left\{X\in\binom{\Omega}{N}:|X\cap A|=a\right\},
 \qquad
 M=|\mathcal M_a|=\binom{2a}{a}\binom{2b}{b}.         \tag{6.2}
\]

Its internal edges use every lower colour with `A`-rank `a-1` exactly once
and every upper colour with `A`-rank `a+1` exactly once.

### Lemma 6.1 (sealed-sector obstruction)

No cross edge between sectors `a-1` and `a` can be added while the intact
bank remains: its lower colour repeats a saturated colour.  No cross edge
between sectors `a` and `a+1` can be added: its upper colour repeats a
saturated colour.  Hence the intact central bank cannot occur inside a
global parameter-`N` AGCF when `b>0`.

#### Proof

An edge from `a-1` to `a` has intersection `A`-rank `a-1` and `B`-rank `b`,
exactly one of the suspended lower colours.  The upper argument is dual.
An added `BB` edge inside the central sector could meet only endpoints of
the intact suspended paths, since all their interior vertices already have
degree two.  Such an edge joins two distinct suspended paths.  The resulting
component would traverse both whole paths and flip every `A` coordinate at
least twice, contradicting complement geodesicity.  Hence no central join is
possible either.  The suspended components remain `a`-edge paths whose
endpoints are not complementary in `Omega` when `b>0`. `square`

### Theorem 6.2 (quantitative central-bank alteration floor)

Any conversion of this intact bank into a global AGCF deletes at least

\[
 K_*=\left\lceil\frac{\binom{2N}{N}-M}{N}\right\rceil \tag{6.3}
\]

of its suspended edges.

#### Proof

Every global complement geodesic meets sector `a`: if its first vertex has
`A`-rank `j`, its complement has rank `2a-j`, and the rank changes by at
most one per edge.  Therefore an outside-containing path has at most `N`
outside vertices among its `N+1` vertices.  There are `binom(2N,N)-M`
outside vertices, so at least `K_*` paths use an outside sector.  Each such
path also meets the central sector and hence enters and leaves it, giving at
least two central boundary crossings.

Let `D` and `U` be the numbers of crossings at the lower-saturated and
upper-saturated boundaries.  Then `D+U>=2K_*`.  Deleting `e` suspended edges
frees at most `e` lower and at most `e` upper colours, so exact palettes give
`D<=e` and `U<=e`.  Hence `2K_*<=D+U<=2e`, proving `e>=K_*`. `square`

For fixed `a` and `b -> infinity`,

\[
 \frac{M}{\binom{2N}{N}}\longrightarrow
 \frac{\binom{2a}{a}}{4^a}.                           \tag{6.4}
\]

After division by `C_N`, the alteration floor (6.3) tends to

\[
 1-\frac{\binom{2a}{a}}{4^a}.                         \tag{6.5}
\]

It is `11/16` for `a=3` and `93/128` for `a=4`.  Consequently the verified
small fillers cannot be propagated by intact central substitution followed
by bounded correction.

At the first steps, `a=3,b=1,N=4` gives
`K_*=ceil((70-40)/4)=8`.  At `N=5`, the `a=3,b=2` bank has `M=120` and
`K_*=ceil(132/5)=27`; the `a=4,b=1` bank has `M=140` and
`K_*=ceil(112/5)=23`.  These are literal deletion floors, not asymptotic
estimates.

The palette factor two in Theorem 6.2 is locally sharp.

### Lemma 6.3 (zero-waste paired puncture)

Write one suspended edge as

\[
 P=L+x,\qquad Q=L+y,\qquad
 L=l_A\cup Y,                                         \tag{6.6}
\]

where `|l_A|=a-1`, `|Y|=b`, and `x,y` are in `A-l_A`.  Put
`U=L+x+y`.  Choose `w in Y` and `z in B-Y`.  Deleting `PQ` and adding

\[
 P\;--\;D,\quad D=L+z\in\mathcal M_{a-1},
 \qquad
 Q\;--\;H,\quad H=U-w\in\mathcal M_{a+1}             \tag{6.7}
\]

uses the freed lower colour `L` on the first edge and the freed upper colour
`U` on the second.  Its other two colours are

\[
 R=L+x+z,\qquad S=l_A+(Y-w)+y,                       \tag{6.8}
\]

of `A`-ranks `a` and `a`, respectively, so neither belongs to the two
saturated central banks.  The degrees of `P,Q` are preserved and `D,H` are
the two exposed sockets.

#### Proof

The first new edge has intersection `L` and union `R`; the second has
intersection `S` and union `U`.  The displayed ranks and degree statement
are immediate. `square`

Thus equality in the palette lower bound can only be approached by a bank
of such paired down/up punctures, or an equivalent zero-waste pairing, with
distinct sockets and distinct unsaturated colours.  The remaining task is
an integral simultaneous matching of these sockets into complement paths.
This identifies the constructive residual gate more sharply than the scalar
bound: fractional paired collars may be abundant while their common path
routing still fails.

For the first Pascal step `b=1`, this tradeoff has an exact scalar form.

### Corollary 6.4 (binary seam budget when `b=1`)

Let `B_0` be the number of selected central edges that swap the two
coordinates of the `B` block, and let `D,U` be the down/up central-boundary
crossing counts.  Every global AGCF satisfies

\[
 D+B_0=U+B_0=C_{a+1}.                                \tag{6.9}
\]

In particular `D=U=C_(a+1)-B_0` and `D>=K_*`.

#### Proof

In the low extreme sector, all internal edges are `AA`.  Exactness of the
lower colours of `A`-rank `a-2` forces exactly `binom(2a,a-2)` such edges.
The upper colours of `A`-rank `a` are supplied exactly by those extreme
`AA` edges, the `D` down crossings, and the `B_0` central `BB` edges.  Hence

\[
 D+B_0=\binom{2a}{a}-\binom{2a}{a-2}=C_{a+1}.        \tag{6.10}
\]

Complementation gives the upper-boundary identity.  Theorem 6.2 then gives
`2D=D+U>=2K_*`. `square`

Thus a first-step recursion has an exact binary seam budget: every unit is
either a central `BB` join or a paired down/up excursion.  This does not
force all Catalan units to cross, but it is a useful finite exported state.

The paired punctures are also plentiful enough at the correct asymptotic
scale.

### Theorem 6.5 (collision-free puncture bank)

Fix `a` and let `b=N-a` tend to infinity.  Put

\[
 p_a=\frac{\binom{2a}{a}}{4^a}.                       \tag{6.11}
\]

For every fixed `epsilon>0` and all sufficiently large `N`, the intact
central bank contains a family of at least `K_*` paired punctures from
Lemma 6.3 with pairwise distinct

* deleted base edges;
* down and up sockets `D,H`; and
* new upper and lower colours `R,S`.

More quantitatively, one can obtain

\[
 (1-p_a+\epsilon)C_N-O_{a,\epsilon}(C_N/N)            \tag{6.12}
\]

such punctures before truncating to `K_*`.

#### Proof

Choose a suspended base edge uniformly, orient its two endpoints uniformly,
and choose `w in Y`, `z in B-Y` uniformly.  Let `E_0` be the number of
suspended edges, and let `U_a,L_a` denote the rank-`N+1,N-1` colour banks
of `A`-rank `a`.  For two independent sampled punctures, a union bound gives

\[
 \Pr(\text{resource conflict})\le
 \frac1{E_0}+\frac1{|\mathcal M_{a-1}|}
 +\frac1{|\mathcal M_{a+1}|}
 +\frac{a+1}{a}\left(\frac1{|\mathcal U_a|}
                      +\frac1{|\mathcal L_a|}\right). \tag{6.13}
\]

Here `D` is uniform because the suspended lower palette is bijective, and
`H` is uniform by the upper palette.  The distributions of `R,S` are
middle-endpoint incidence distributions.  Their maximum-to-average degree
ratio is at most

\[
                    \frac2{2a/(a+1)}=\frac{a+1}{a},  \tag{6.14}
\]

which proves the last two terms.  For fixed `a`, every denominator in
(6.13) is `Theta_a(NC_N)`.  Sampling `s=Theta(C_N)` atoms therefore creates
only `O_a(C_N/N)` conflicting pairs in expectation.  Some sample has at
most that many.  Delete one atom for each conflicting pair; the survivors
are collision-free in the listed resources and lose at most `O_a(C_N/N)` atoms.

Finally

\[
 \frac{K_*}{C_N}\longrightarrow1-p_a.                \tag{6.15}
\]

Taking `s=(1-p_a+epsilon)C_N` and then `N` sufficiently large leaves at
least `K_*` survivors. `square`

Two deleted base edges may share an endpoint.  This is harmless: each
puncture replaces its own incident base edge by one new incident edge at
that endpoint, so simultaneous punctures preserve the original middle
degrees.  The theorem claims distinct edge/socket/colour resources, not
vertex-disjoint twenty-state supports.

Thus local puncture supply and collision packing are not the asymptotic
obstruction.  The missing theorem is the global complement-path routing of
the distinct sockets together with the graded turn ledger.

The exact graded state required by any block recursion can also be written
without approximation.  Let `M_j=binom(2a,j)binom(2b,N-j)`.  Let `A_j,C_j`
count selected edges staying in sector `j` and swapping inside `A,B`, let
`X_j` count cross edges between sectors `j-1,j`, and let `p_j` count path
endpoints in sector `j`.  With out-of-range terms zero, every AGCF obeys

\[
\begin{aligned}
 A_{l+1}+C_l+X_{l+1}
   &=\binom{2a}{l}\binom{2b}{N-1-l},\\
 A_{u-1}+C_u+X_u
   &=\binom{2a}{u}\binom{2b}{N+1-u},\\
 2A_j+2C_j+X_j+X_{j+1}&=2M_j-p_j,\\
p_j&=p_{2a-j},\qquad \sum_jp_j=2C_N.
\end{aligned}                                         \tag{6.16}
\]

The first two rows classify exact lower and upper colours by `A`-rank; the
third is the degree sum in sector `j`; the last is complement pairing.
Moreover a path beginning in sector `j` has cross-type counts satisfying

\[
                     x_{BA}-x_{AB}=2(a-j),             \tag{6.17}
\]

so every off-central sector needs at least `2|a-j|` cross-block transfers.
Equations (6.16)--(6.17), not a central scalar Catalan count, are the minimum
graded export of a Pascal/tensor recursion.

## 7. Independently verified small parameters

### `n=2`

In bitmask notation the two paths are

```text
3 5 12
6 10 9
```

They partition all six middle vertices and both four-colour turn palettes.

### `n=3`

The five paths are

```text
13 41 35 50
19 22 14 44
21 28 56 42
25 49 52 38
26 11 7 37
```

They partition all twenty middle vertices and both fifteen-colour turn
palettes.  Every endpoint pair is complementary and every coordinate flips
once.  Section 4 explains exactly why two canonical endpoint pairs had to
move.

### `n=4`

The complete candidate catalogue contains `20,160` unoriented complement
geodesics.  Each covers five middle, four lower, and four upper resources;
all `182` resources have candidate degree `1,440`.  An exact cover by
fourteen paths exists.  Literal replay checks all `70` middle vertices and
both `56` turn palettes exactly once, with complementary endpoints and one
flip per coordinate.

The witness and clean replay are

```text
scratch/catalan_antipodal_geodesic_filler_n4_20260731.witness.txt
scratch/audit_k_catalan_n4_global_complement_geodesic_exact_cover_20260731.py
scratch/k_catalan_n4_global_complement_geodesic_exact_cover_20260731.audit.json
```

with hashes

```text
witness  4cb494aaffc4887b261745c8d68ffc1faedf5b9a6264c8a0738a6e752846018d
replay   038ddebbf2843c96e50e4504853473e70d9aef8dbebaa539b46e9b20fd249d1f
JSON     b56999544df0dc1f78d7e353eec338d5ecb3b452527d15d6f8a921c128665e19
```

This is global `n=4` existence, not merely survival in the failed
canonical-plus-one-conjugate two-parent bank.

### Exact recursive `n=3 -> 4` face

The stronger witness retains all five `n=3` paths, extends each by one
new-coordinate swap, and completes them with nine monotone three-sector
paths.  It realizes exactly the recursive split proved in
`MATH_THEOREM_CATALAN_ANTIPODAL_FILLER_POINTED_WREATH_AND_THREE_SECTOR_RECURSION_20260731.md`.

```text
scratch/catalan_antipodal_geodesic_filler_n3_to_n4_recursive_20260731.witness.txt
scratch/audit_catalan_antipodal_geodesic_filler_n3_to_n4_recursive_20260731.py
scratch/catalan_antipodal_geodesic_filler_n3_to_n4_recursive_20260731.audit.json
```

The hashes are

```text
witness  cd7ede950afc2733f43d30f0af797192d854c9cd0d7bff05918d3fd87e77eb81
replay   27392fec87698b8b0be94c1f487fd4ac60dcf36840f8921d19a17c69792f527c
JSON     eea25d066cc5b87ea189494af3956b3306c521dddeb9a9bce5ca25597d480ab9
```

The small-case independent audit has hashes

```text
script   b3e5a89ac8cd68cb515b5cf6d6ecc3341cfa1dfb6c811089fff6354287814dd2
JSON     39335a0a0bb4baf28991d85a76478582cd1d049565e6dee6619a066d08d5e7b5
```

The prefix-collision, fixed-port, repair-atom, and formal-pentagon replay is

```text
scratch/audit_k_catalan_antipodal_lower_turn_obstructions_20260731.py
scratch/k_catalan_antipodal_lower_turn_obstructions_20260731.audit.json
```

with hashes

```text
script   4e880b49f2666cb11319bbb919925af3a8988ad91ccf71d207ee7589a04d4675
JSON     b86fb6668b8f7b0b1e876b7612457310c52121356ec64c47ca031163ae2c2b5f
payload  b8cdacc097b373e372b9de698728da0d2f123e7ab0e401a84ce413f741abb0c4
```

All replays are light.  The global `n=4` witness was found by one capped
H100 CPU exact-cover run; the frozen witness is independently checkable
without rerunning that search.

## 8. The exact ordinary-Hall router on the three-sector face

The three-sector residual theorem becomes one ordinary bipartite matching
problem after its three internal forests are fixed.  This is the useful
deterministic routing condition left by the puncture construction.

Let

\[
 K=C_{n+1}-C_n.                                       \tag{8.1}
\]

Suppose each of the three residual vertex sectors has been partitioned into
`K` oriented path components

\[
\begin{aligned}
 T_i&:A_i^0\longrightarrow A_i^1
       &&\text{in rank }n+1,\\
 M_j&:X_j^0\longrightarrow X_j^1
       &&\text{in rank }n,\\
 B_k&:L_k^0\longrightarrow L_k^1
       &&\text{in rank }n-1.
\end{aligned}                                         \tag{8.2}
\]

Assume:

1. all three internal forests are linear and together have the exact
   internal lower/upper palette ledger;
2. their four endpoint colour banks are exactly the four palette deficits
   to be supplied by the two seam families; and
3. there is a bijection `kappa` from top to bottom components such that

\[
                     L_{\kappa(i)}^1=\Omega\setminus A_i^0. \tag{8.3}
\]

Define a bipartite graph `G` on the top indices `i` and middle indices `j`
by

\[
 i\sim j
 \quad\Longleftrightarrow\quad
 X_j^0\subset A_i^1
 \ \text{and}\ 
 L_{\kappa(i)}^0\subset X_j^1.                        \tag{8.4}
\]

### Theorem 8.1 (three-sector socket router)

Within this fixed-forest face, a residual complement-geodesic factor exists
if and only if `G` has a perfect matching.  Equivalently, the exact remaining
condition is the ordinary Hall system

\[
                         |N_G(S)|\ge|S|\qquad(S\subseteq[K]). \tag{8.5}
\]

#### Proof

Let `pi` be a perfect matching of `G`.  For every top index `i`, concatenate

\[
 T_i,\quad
 A_i^1\;--\;(z+X_{\pi(i)}^0),\quad
 z+M_{\pi(i)},\quad
 (z+X_{\pi(i)}^1)\;--\;(cz+L_{\kappa(i)}^0),\quad
 cz+B_{\kappa(i)}.                                    \tag{8.6}
\]

The first seam is Johnson exactly when `X_pi(i)^0 subset A_i^1`; the second
is Johnson exactly when `L_kappa(i)^0 subset X_pi(i)^1`.  Thus (8.4) is
precisely physical seam legality.  Because `pi` and `kappa` are bijections,
every internal component is used once.  The seam lower/upper multisets are
the four endpoint banks from assumption 2, independent of the assignment,
so both residual palettes become exact.

By (8.3), the final endpoint `cz+L_kappa(i)^1` is the complement, in
`Omega+c+z`, of the initial endpoint `A_i^0`.  The concatenations are
vertex-disjoint paths.  Each residual sector has `N_n` vertices and `K`
components, so the three forests plus the `2K` seams have

\[
 3(N_n-K)+2K=3N_n-K=K(n+1)                           \tag{8.7}
\]

edges.  Every one of the `K` complementary-endpoint paths has Johnson
distance `n+1`; equality in the total forces every path to be a geodesic.

Conversely, any residual factor which retains the three fixed oriented
forests assigns one middle component to each top component and one bottom
component through `kappa`.  Vertex-disjointness makes the assignment a
permutation, and its two seams force both containments in (8.4).  It is
therefore a perfect matching of `G`.  Hall's theorem gives (8.5). `square`

Theorem 8.1 is stronger than a generic path-packing restatement: once the
internal palette-deficit forests and outer complement pairing are built,
all topology and both seam palettes collapse to one ordinary Hall graph.
The live constructive task is therefore to build those three forests so
that this two-containment graph expands.  This is not proved for every `n`.

### Corollary 8.2 (balanced pressure suffices)

If every top index has at least `d` compatible middle indices and every
middle index is compatible with at most `d` top indices, for some `d>=1`,
then `G` has a perfect matching.

Indeed, for every `S` on the left,

\[
 d|S|\le e_G(S,N_G(S))\le d|N_G(S)|.                 \tag{8.8}
\]

More generally, and equivalently to Hall, it is enough to exhibit
nonnegative weights on compatible pairs with every row sum one and every
column sum at most one.  Since both shores have order `K`, every column sum
is then one, and the supported doubly stochastic matrix contains a perfect
matching.

Separate seam matchings do not imply this joint condition.  As an abstract
endpoint-containment system on a six-set, set `kappa=id` and take

\[
\begin{aligned}
 A_1^1&=1234,& A_2^1&=3456,\\
 X_1^0=X_1^1&=123,&X_2^0=X_2^1&=456,\\
 L_1^0&=45,&L_2^0&=12.
\end{aligned}                                         \tag{8.9}
\]

The first-containment graph `X_j^0 subset A_i^1` has only the identity
matching, while the second-containment graph `L_i^0 subset X_j^1` has only
the transposition.  Their same-`j` compatibility graph (8.4) is empty.
Thus separate lower/upper incidence bases or separate uniform marginals do
not establish the router; the common two-containment pressure must be
exported explicitly.  This two-by-two example is not asserted to be a
completed three-sector forest: its unused outer endpoints and internal
palette ledgers have deliberately not been supplied.

### Corollary 8.3 (triangular leaf-router state)

Suppose the two shores can be paired and ordered as
`(l_t,r_t)`, `1<=t<=K`, so that every diagonal edge `l_t r_t` is present
and, for every `t`, at least one of

\[
\begin{aligned}
 N(l_t)\cap\{r_1,\ldots,r_t\}&=\{r_t\},\\
 N(r_t)\cap\{l_1,\ldots,l_t\}&=\{l_t\}
\end{aligned}                                         \tag{8.10}
\]

holds.  Then `G` is leaf-peelable and its diagonal perfect matching is
unique.

#### Proof

Restrict first to pairs `1,...,K`.  Condition (8.10) makes `l_K` or `r_K`
a leaf, so its diagonal edge is forced.  Delete that pair and repeat with
`K-1`; induction peels every pair and forces the full diagonal. `square`

This state is recursively closed under appending ordered blocks: it is
enough that each newly appended diagonal pair have a private containment
on one shore relative to all earlier pairs.  Compatibilities pointing only
to later blocks disappear before that pair is peeled.  Hence a concrete
all-parameter target is to order the Catalan triples so each new residual
component exports one private containment side, rather than proving generic
expansion from scratch.

The frozen `n=3 -> 4` recursive witness already lies on this face.  Its
nine-component router graph has left neighbourhoods

```text
[0] [1] [2] [3] [4] [5] [6] [5,7] [8]
```

and right degrees `1,1,1,1,1,2,1,1,1`.  It is an 18-vertex, 10-edge,
8-component forest, completely leaf-peelable, with the unique identity
matching.  Independent replay is frozen at

```text
scratch/audit_k_catalan_n3_to_n4_router_graph_20260731.py
  SHA a9f5a5d5bb31d7ee56ea638ba6da46cd1b1eb7e1d7d7110a6f28b66ab6a4934d
scratch/k_catalan_n3_to_n4_router_graph_20260731.audit.json
  SHA 6d95aebf879871cae09a70c583c1f75c6c9feaec36591b06aa95b0bbb79125e6
  payload 1a45cc24ab833b0fb75b774cadd66d32d33931e503337789b97caf6ea703a0f7
```

## 9. Exact proved/conditional boundary

The existence of AGCFs for every `n` is not proved here.  The strongest
current positive recursive target is the lossless three-sector residual
theorem: orient a parent AGCF, extend each parent rail by one tag swap, and
perfectly cover the remaining three equal middle sectors together with both
remaining turn palettes by monotone complement geodesics.  It is realized
at `n=3 -> 4`; its all-parameter perfect-resource matching remains open.

The unrestricted candidate-hypergraph route has independently reached the
same boundary.  The exact resource degree and maximum pair-codegree are

\[
 D=\frac{(n+1)(n!)^2}{2},\qquad
 \Delta_2=(n!)^2=\frac{2D}{n+1}.                     \tag{9.1}
\]

Moreover, for `n>=3`, a literal `2<->2` resource trade embeds through every
candidate edge.  A leave expressed as a union of designated candidate edges
is therefore absorbable whenever pairwise resource-disjoint reserved
absorber instances have been assigned to those edges.  This is proved in
`MATH_THEOREM_CATALAN_AGCF_RESOURCE_HYPERGRAPH_CODEGREES_LATTICE_AND_ABSORPTION_GATE_20260731.md`.
Thus local absorption is no longer the missing row.  The unrestricted route
still needs an edge-aligned cover-down, while the structured three-sector
route needs the fixed internal forests and Hall graph of Theorem 8.1.

The results above delimit any proof of that theorem:

* palette matching itself is automatic and therefore cannot be the missing
  argument;
* every successful lower assignment is cross-component;
* canonical MSW needs changes on a positive density of its path components;
* fixed canonical ports already fail at `n=3`;
* formal zero-flux local atoms need a branched physical router; and
* intact central tensor copies need positive-density deletion.

Thus the live construction must coordinate lower circuits, endpoint
monodromy, and graded cross-sector transport in one step.  This is a genuine
all-parameter matching/recursion gate, not another scalar Catalan identity.
