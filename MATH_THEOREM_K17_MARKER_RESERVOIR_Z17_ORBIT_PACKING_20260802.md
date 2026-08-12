# `k=17`: a 96-module marker-reservoir packing in the cyclic quotient

Date: 2026-08-02  
Status: unconditional finite owner/named-target packing with an independently
replayed literal witness.  This is not a chronology and not a universal word.

## 1. Setup

At `k=17` the facet parameters are

\[
q=5,\qquad c=5,\qquad r=9.
\]

Use coordinates `0,...,16` cyclically and fix

\[
D=\{0\},\qquad V=(1,2,3,4,5),\qquad G=\{6,\ldots,16\}.
\]

Take `beta=0`, primitive-`P` tag `w=1`, and primitive-`H` tag `h=2`.
For every four-set `X subset G`, the fixed-base marker theorem gives a
literal length-five primitive module with core

\[
C_X=D\cup X.
\]

Its named resource deck is

\[
\begin{array}{c|l}
5&X\cup\{1\},\\
6&D\cup X\cup\{2\},\\
7&D\cup X\cup J,\quad J\text{ a cyclic two-interval of }V,\\
8&D\cup X\cup J,\quad J\text{ a cyclic three-interval of }V,\\
9&D\cup X\cup(V-\{v\}),\quad v\in V.
\end{array}
\tag{1.1}
\]

Thus one module carries `1,1,5,5,5` named resources at ranks `5,...,9`.

Let `rho` rotate all 17 coordinates.  Since 17 is prime, its action is free
on every nonempty proper subset of `[17]`, in particular on all five ranks
in (1.1).

## 2. Orbit conflict graph

Call a module internally orbit-simple when its 17 named resources lie in
17 different typed rotation orbits.  Join two internally orbit-simple
modules when any named resource of one is a rotation of a same-rank named
resource of the other.

The complete four-subset reservoir has 330 candidates.  Direct literal
enumeration gives:

\[
\begin{array}{c|r}
\text{raw modules}&330\\
\text{internally non-orbit-simple}&1\\
\text{conflict-graph vertices}&329\\
\text{conflict edges}&1663\\
\text{minimum/maximum degree}&2/21.
\end{array}
\tag{2.1}
\]

The retained witness in
`scratch/k17_marker_orbit_packing_20260802/k17_marker_orbit.witness.tsv`
is an independent set of 96 vertices in this graph.  No maximality claim is
made; 96 is merely an explicit lower bound.

## 3. Development theorem

### Theorem 3.1

Develop the 96 base modules and all their named resources under
`rho^0,...,rho^16`.  The result contains 1,632 literal primitive modules and
27,744 pairwise distinct named resources.  The rank counts are

\[
\begin{array}{c|rrrrr}
\text{rank}&5&6&7&8&9\\ \hline
\text{resources}&1632&1632&8160&8160&8160.
\end{array}
\tag{3.1}
\]

#### Proof

Within one developed orbit, internal orbit-simplicity and freeness of the
rotation action exclude collisions.  Between two base modules, independence
in the conflict graph says that no typed resource orbit is shared.  Hence
their developments are disjoint as well.  Multiplying the per-module deck
`(1,1,5,5,5)` by `96*17` gives (3.1).  \(\square\)

This conclusion was also replayed without using canonical orbit keys: the
independent verifier explicitly generated all 1,632 translated modules,
inserted every actual 17-bit resource into typed hash sets, and rejected any
duplicate.

## 4. Literal source audit and exact boundary

For each developed module the five source values are

\[
S_0=X\cup\{w\},\qquad
S_i=X\cup D\cup\{v_i\}\quad(1\le i\le4),
\tag{4.1}
\]

with all symbols rotated together.  The independent verifier checked that
every four consecutive cyclic source values have union

\[
D\cup X\cup(V-\{v\})
\]

of rank nine, and that all local source ranks and owner identities are
correct.  There were zero local window failures.

The 1,632 modules require 6,528 occurrence-labelled `H`/buffer positions.
As unlabelled subset values these comprise 6,154 distinct masks, with
maximum mask multiplicity two.  This is not a contradiction: source slots
are physical occurrences, not named target capacities.  It does show why
the present theorem must not be promoted directly to a chronology.  Binding
those occurrences to distinct legal positions, fusing components, and
preserving residence are separate gates.

The theorem proves only the following finite layer:

* literal primitive roles and local depth-three owner windows;
* pairwise distinct rank-9 owners;
* pairwise distinct named targets at ranks 5--8.

It does **not** prove one connected owner chronology, ranks 10--17, global
residence, the lower common-cap compiler, or a length-24,313 word.

## 5. Reproducibility

Artifacts are in
`scratch/k17_marker_orbit_packing_20260802/`.

* witness SHA-256:
  `88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403`;
* search audit SHA-256:
  `abbc69a34b8e92d0e8cc62f1bc9e4683e641a78bc39c7103b8938b41fc3c85c0`;
* independent literal audit SHA-256:
  `28a4d4cd6e19c4c6b77a8140c85bd1fceac11421e5eea0dd8ae0e50ea8d119ab`;
* generator source SHA-256:
  `9632163defe008148d5db638e73a37a69c1b7a61db032cb468308bff80a91cc5`;
* independent verifier source SHA-256:
  `8ba65f4fa8214388638782d7ca4f1ed31374df745096be111a388b4dc9a8ffe4`.

The H100 run root is
`/home/amodo/or15/work/root_k17_marker_orbit_packing_20260802`.

## 6. Significance

The intact-reservoir no-go remains correct: two complete 330-module frames
cannot coexist.  The theorem instead exhibits the required escape route—
split one reservoir, retain an orbit-simple subfamily, and use cyclic
development to make all rank constraints cluster orbitwise.  The resulting
1,632-module bank is substantially larger than the 610-module two-frame
partial extraction and larger than the initial 58-base-module target.

The next exact question is whether this bank embeds in the authenticated
`k=17` owner/q1 factor with its 6,528 positional buffer occurrences.  Only
after that embedding passes should its upper and compiler gates be tested.
