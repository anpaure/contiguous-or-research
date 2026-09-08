# Thread A: audit of the k=15 cyclic zero signal and equivariant fallback

Date: 2026-07-28

## 1. Verdict

The phrase “the six persistent rank-six zero candidates are cyclic shifts of
2709” conflates two different states.

1. **Verified historical fact.**  At the old Hall-37 checkpoint, its six
   rank-six zero candidates are six rotations of 2709.
2. **Refuted persistence claim.**  At the current audited H19 carrier there
   are four rank-six and two rank-seven zeros, lying in six distinct cyclic
   orbits.  Only 17738 lies in the orbit of 2709.
3. **Equivariance is not an automatic repair.**  In a genuinely equivariant
   target-cell incidence graph, degree is constant on target orbits and a
   maximum Hall-deficiency shore can be chosen orbit-invariant.  Hence a
   surviving **degree-zero** 2709 obstruction becomes one complete
   15-target orbit hole.  A new equivariant factor may instead cover that
   orbit, but no k=15 certificate in the inspected Claude directory proves
   this.
4. **Strict spiral is not the essential restriction.**  It is exactly the
   normal form of a connected, unit-voltage equivariant Hamilton cycle.  A
   disconnected or nonunit-voltage equivariant 2-factor is strictly more
   general and is a legitimate fallback, but it still needs an exact seam,
   owner, residence, support, and compiler-Hall completion.

No search was run for this audit.  All computations below are direct parsing
or small exact checks of frozen artifacts.

## 2. The Hall-37 observation is exact but state-specific

The artifact

```text
scratch/k15_targetpalette_p1_h37.fast_hall.json
```

has SHA-256

```text
eba2b2b5c7de3b80fa203a55996ee1118e3ee61926b656b082af4044c020092f
```

and records deficiency 37 with eight zero-candidate targets.  The six
rank-six zeros are

\[
 5397,\ 8869,\ 10794,\ 17738,\ 21588,\ 21672.            \tag{2.1}
\]

If \(\rho\) rotates the 15 coordinates one step, then these are

\[
 \rho^8(2709),\ \rho^{13}(2709),\ \rho^9(2709),
 \ \rho^{14}(2709),\ \rho^{10}(2709),\ \rho^3(2709).    \tag{2.2}
\]

The other two zeros are the rank-seven masks

\[
 8877=\rho^{13}(2741),\qquad13589=\rho^8(2741).           \tag{2.3}
\]

Thus the historical pattern is real.  It was not an invariant orbit hole:
only six of the fifteen rotations of 2709 were zero.  The Hall-37 compiler
was already symmetry-broken.

Nor were Hall-zero and direct lower support identical.  On the corresponding
middle path, the rotations of 2709 absent from the linear three-window
intersection support were

\[
 \{5397,8869,10577,10794,17738,21588,21672\}.             \tag{2.4}
\]

The extra mask 10577 was a direct \(q=2\) support hole but had positive
compiler degree.

## 3. The current six zeros are in six distinct orbits

The initial monotone spine starts from
`scratch/k15_doubletrans_05_213_hall29.json`.  It is followed by a deliberate
zero-reduction detour which temporarily returns from H22 to H23.  The exact
zero ledger is:

\[
\begin{array}{c|c|l}
\text{state}&\#Z&Z\\ \hline
H29\text{ through first }H22&7&2575,5801,13616,13620,17738,21641,29776\\
\text{detour }H23\to H22\to H22&6&5801,13616,13620,17738,21641,29776\\
H21\text{ through }H19&6&5801,13616,13620,17738,21641,29776.
\end{array}                                               \tag{3.1}
\]

The three zero-six detour artifacts are

```text
scratch/k15_segment_braid_hall23_zero6_from22.json
scratch/k15_segment_braid_hall22_zero6.json
scratch/k15_segment_braid_hall22_portal_to21.json.
```

Thus “H22” is ambiguous without the branch label: the first H22 checkpoint
has seven zeros, while the current H22 detour state has six.

There is also a separate H29 checkpoint,
`scratch/k15_segment_braid_hall_best.json`, with nine zeros obtained by
adjoining 6347 and 6632 to the seven-target set above.  It is not the parent
of the selected H28 artifact and must not be spliced into this descent table.

For the current six, rank and cyclic canonical representative are

\[
\begin{array}{c|c|c}
T&|T|&\min_s\rho^sT\\ \hline
5801&7&4821\\
13616&6&851\\
13620&7&3405\\
17738&6&2709\\
21641&6&2473\\
29776&6&1861.
\end{array}                                               \tag{3.2}
\]

The canonical representatives are pairwise distinct.  In particular, the
current set consists of four rank-six and two rank-seven targets, not six
rank-six targets.

In shift order, the complete orbit of 2709 is

\[
\begin{split}
(&2709,5418,10836,21672,10577,21154,9541,19082,\\
 &5397,10794,21588,10409,20818,8869,17738).               \tag{3.3}
\end{split}
\]

It has trivial stabilizer and size 15.  Its exact candidate-degree vector in
the audited H19 compiler is

\[
 (2,3,1,3,2,3,2,1,3,4,6,3,1,2,0).                       \tag{3.4}
\]

Thus 17738 is the only zero in this orbit.  Equation (3.4) is also a direct
certificate that the rooted linear compiler is not cyclically equivariant.

At H19 the direct \(q=2\) holes within this orbit are

\[
 \{8869,17738\},                                          \tag{3.5}
\]

whereas only 17738 has compiler degree zero.  Orbitwise raw support is a
useful necessary ledger, but it is not the compiler Hall graph.

## 4. What full equivariance actually implies

Let a finite group \(G\) act on a bipartite graph

\[
 B=(L,R,E)                                                 \tag{4.1}
\]

by graph automorphisms.  For \(A\subseteq L\), define

\[
 \delta(A)=|A|-|N(A)|.                                    \tag{4.2}
\]

**Theorem 4.1 (equivariant degree and Hall shore).**

1. Candidate degree is constant on every \(G\)-orbit in \(L\).
2. The zero-degree set is a union of \(G\)-orbits.
3. If Hall fails, some maximum-deficiency set \(A\) is \(G\)-invariant.

**Proof.**  For \(g\in G\), the map \(r\mapsto gr\) is a bijection from
\(N(x)\) to \(N(gx)\), proving 1 and 2.  Also

\[
 N(A\cup C)=N(A)\cup N(C),\qquad
 N(A\cap C)\subseteq N(A)\cap N(C).                      \tag{4.3}
\]

Hence \(\delta\) is supermodular:

\[
 \delta(A\cup C)+\delta(A\cap C)
 \ge \delta(A)+\delta(C).                                \tag{4.4}
\]

If \(A,C\) both maximize \(\delta\), each term on the left is at most the
same maximum, so their union and intersection are maximizers too.  Repeatedly
unioning all translates \(gA\) gives a \(G\)-invariant maximizer.  \(\square\)

For a cyclic action, the invariant maximizer is a weighted quotient Hall
cut: it is a union of target orbits, and its neighborhood is a union of cell
orbits.  Orbit sizes are the weights.

**Corollary 4.2.**  In a fully \(\mathbb Z_{15}\)-equivariant compiler, if
2709 has degree zero, then all fifteen members of (3.3) have degree zero and
form a deficiency-15 cut.  If all six current orbit shapes in (3.2) remained
zero, their six free orbits would contribute at least 90 isolated targets.

Positive degree on every orbit is still insufficient: Theorem 4.1 permits a
multi-orbit maximum Hall cut.

This theorem does not apply to the current endpoint-conditioned compiler.
A cyclic middle factor may be equivariant, but cutting it into a linear path
distinguishes the closing seam; maximal erosion, endpoint collars, and the
resulting physical cells need not be carried to one another by rotation.
The varying degrees in (3.4) exhibit precisely that symmetry breaking.

Naively adjoining all fifteen rotated, copy-labeled versions of the H19
catalogue would make every target in (3.3) have degree

\[
 2+3+1+3+2+3+2+1+3+4+6+3+1+2+0=36.                     \tag{4.5}
\]

But it also uses fifteen copies of every owner resource.  Dividing by
fifteen is only a fractional averaging argument.  Neither operation is an
integral one-baseline compiler.

## 5. Strict spiral versus an equivariant 2-factor

The strict-spiral ansatz in Claude's `equi.py` has the form

\[
 T_{jN+i}=\rho^{jv}X_i,\qquad N=429,\qquad \gcd(15,v)=1. \tag{5.1}
\]

The following identifies exactly what topology (5.1) imposes.

**Theorem 5.1 (quotient voltage normal form).**  Let \(k\) be odd, let
\(\rho\) generate a free \(\mathbb Z_k\)-action on the middle layer, and let
\(F\) be a \(\rho\)-invariant spanning 2-factor.  Suppose its quotient,
with loops and parallel incidences counted with their natural weights, is
connected and has \(N>1\) vertices.  Then the quotient is one cycle.  After
choosing an orientation and successive lifts

\[
 X_0,X_1,\ldots,X_{N-1},                                  \tag{5.2}
\]

the closing edge is

\[
 X_{N-1}\longrightarrow\rho^vX_0                         \tag{5.3}
\]

for a unique voltage \(v\in\mathbb Z_k\).  The lift has

\[
 \gcd(k,v)                                                 \tag{5.4}
\]

physical cycles, each of length \(Nk/\gcd(k,v)\).  It is one Hamilton cycle
if and only if \(\gcd(k,v)=1\); in that case its cyclic order is exactly
(5.1).  Conversely, every strict spiral (5.1) is the unit-voltage lift of
this quotient cycle.

**Proof.**  Freeness and odd \(k\) rule out a nonidentity element fixing or
inverting an undirected edge.  The quotient therefore has weighted degree
two, so connectedness makes it a cycle.  Traversing one quotient circuit
changes the sheet coordinate by
\(v\).  Its repeated lifts follow the cosets of the subgroup
\(\langle v\rangle\le\mathbb Z_k\).  There are \(\gcd(k,v)\) cosets, and
the order of \(v\) is \(k/\gcd(k,v)\), giving (5.4) and the component
lengths.  The unit-voltage case visits every sheet and gives (5.1).  The
converse follows by quotienting any valid spanning strict spiral (5.1).
\(\square\)

Here the quotient is the multigraph of vertex and edge orbits: an edge orbit
between distinct vertex orbits contributes one incidence at each endpoint,
while a same-orbit edge contributes a loop counted twice.  When \(N>1\), a
loop at a weighted-degree-two vertex would isolate that vertex, so a
connected quotient has no loop.  Parallel edges are allowed; for \(N=2\),
two parallel edges form the length-two quotient cycle.  The voltage is
unique after fixing the orientation and the successive lifts; reversing the
orientation replaces \(v\) by \(-v\).

The free-action premise holds on the k=15 middle and adjacent color layers.
A nonidentity rotation of 15 has coordinate cycles of length 3, 5, or 15,
so a fixed subset has cardinality divisible by 3 or 5.  Ranks 7 and 8 are
divisible by neither.

For \(k=15\), the possibilities for a connected quotient are

\[
\begin{array}{c|c|c}
v&\text{physical cycles}&\text{cycle length}\\ \hline
1,2,4,7,8,11,13,14&1&6435\\
3,6,9,12&3&2145\\
5,10&5&1287\\
0&15&429.
\end{array}                                               \tag{5.5}
\]

Therefore strict spiral is not stronger than a cyclically invariant
Hamilton cycle: it is its normal form.  It is stronger than the legitimate
fallback consisting of disconnected quotient cycles and/or nonunit
voltages.  Each quotient component then has its own voltage and lifts to its
own family of physical cycles.

Neither the H29 nor H19 path satisfies

\[
 T_{i+429}=\rho^vT_i                                      \tag{5.6}
\]

for any \(1\le v<15\).  Their partial-orbit zero patterns say nothing
directly about existence of a strict spiral.

## 6. Audit of Claude's k=15 artifacts

The inspected directory is

```text
/Users/amir.nuriyev/Downloads/opusproblem/work
```

and contains model source but no k=15 theorem certificate:

* `k15_cegar.log` is zero bytes;
* no `k15_carrier_sel.json` or other k=15 selected-factor artifact exists;
* `equi.py` assumes, but its checker does not itself verify, that the
  \(X_i\) are a complete rank-eight orbit transversal or that
  \(\gcd(v,15)=1\);
* `equi15.py` selects edge orbits for an equivariant degree-two factor, then
  demands quotient connectivity and one physical cycle.  A success would
  therefore lie in the strict-spiral case of Theorem 5.1, not the general
  2-factor fallback;
* its header promises lazy lower-\(q=2,3\) enforcement, but the main loop
  merely prints `lo2,lo3` and declares its cyclic gates passed when the upper
  list alone is empty;
* its advertised upper cover-clause constructor is unimplemented;
* none of `equi.py`, `equi15.py`, or `equi2.py` builds and matches the exact
  endpoint-conditioned flexible-compiler Hall graph.

The generic `equi2.py` fixes the stopping test for lower support, but still
forces quotient connectivity and a single physical lift.  It is not yet an
implementation of the proposed arbitrary 2-factor fallback.

Thus Claude's files are useful specifications and small-\(k\) experiments,
not evidence that k=15 equivariance removes the Hall obstruction.

## 7. What the 2-factor fallback must prove

There is an exact precedent at \(k=13\).  The frozen equivariant factor

```text
scratch/k13_res0_onehole_repair_history16x5.round0.disconnected.json
```

has two physical cycles of lengths 1547 and 169.  Its full audit proves no
residence defect of length at most three and complete lower/upper support at
every depth \(q=1,\ldots,6\).  One seam produces the owner-exact middle path

```text
scratch/k13_two_cycle_one_seam_path_000.json
```

and its exact Hall artifact

```text
scratch/k13_two_cycle_one_seam_path_000.hall.json
```

has status `PASS`, matching 4095 of 4095 targets.  Hence strict
Hamiltonicity is unnecessary in principle.  The fused path has one lower
\(q=1\) support hole; the exact Hall completion absorbs it.

For \(k=15\), an equivariant 2-factor fallback still has to provide all of:

1. exact degree two at every middle owner and the required rank-seven
   color-orbit ownership;
2. component orientations satisfying depth-three residence;
3. cuts and connectors producing one owner-exact linear path;
4. complete upper support after the connector collars, with every lower
   support loss represented in the exact compiler graph;
5. endpoint-conditioned erosion and common-owner/common-\(Q\) compatibility;
6. a perfect matching in the complete 19,311-cell compiler graph.

Removing isolated orbit targets is only a necessary preliminary check.
Theorem 4.1 shows that an orbit-level Hall cut may remain even when every
orbit has positive degree.

## 8. Reproducibility

The lightweight audit script

```text
scratch/threadA_audit_k15_cyclic_zero_orbits.py
```

rebuilds the selected frozen H29-through-H19 Hall graphs, separately records
the other H29 checkpoint, checks the historical H37
shift identities, computes the current orbit representatives and degree
vector, distinguishes direct support from compiler degree, verifies absence
of a strict voltage in H29/H19, and records the Claude artifact hashes.  Its
certificate is

```text
scratch/threadA_k15_cyclic_zero_orbits_audit.json
```

with status `PASS`.

The principal k=13 hashes are

```text
2987fe2e3ef6de56c538038688835246e6aafafc5c6a7dd576b3df986ee44ef9  source factor
adaee329852ceaa2ce0a95b97e9306bc04ff91f8fe7c52e1eab844523039d68f  factor audit
baa204bf8208c531cc1905c6cf53a2438db85a0b778231c0e59a631eef4b7973  fused path
2a7b7eb4ece4711214dd24f93ad216f8d77dd53c27bd7edda0162b3059f8c137  Hall PASS
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0  exact word
```
