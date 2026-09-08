# UPMBC scope audit, exact PBBS q1 source, and the neutral-orbit reduction gate

Date: 2026-07-29

Status: unconditional audit and reduction theorems.  The PBBS source
assumption passes for every nontrivial odd dimension.  The architecture-free
flat-middle gate and the stronger PBBS/protected wrapper are separated
exactly.  No uniform protected component-reduction theorem and no all-odd
coefficient-one theorem are claimed.

## 0. Verdict

Let

\[
 k=2m+1,\qquad r=m+1,\qquad
 W=\binom{k}{r},
\]

Assume `m>=1`; the case `m=0` (`k=1`) is trivial and is kept separate.
Let `d=d(k)` be the monotone-deadline depth.  There are three distinct
statements which must not be conflated.

1. The architecture-free flat-middle target is the existence of some
   permutation `T` of \(\binom{[k]}r\) which is upper-complete and for which
   the full system `COMP_d(T)` is feasible.  This is sufficient for
   `nu(k)=W+d`, and it is necessary and sufficient among flat-middle optimal
   certificates.
2. `UPMBC(m)` is a stronger sufficient method for producing such a `T`: it
   chooses a protected endpoint in the PBBS q1-factor fibre with at most two
   components, opens it safely, and solves the pinned compiler.  Algebraic
   reachability is required; a primitive-by-primitive protected route is not.
3. The particular PBBS source required in item 2 really is q1-exact.  This
   does not follow from all-depth support; it follows from an independent
   antipodal two-perfect-matching identity proved below.

Consequently, a sparse protected connector cut, a trapped neutral orbit, or
a one-seam kernel obstruction is a no-go only for that fixed
factor/library/port implementation.  Even a universal no-go for a declared
protected route does not refute endpoint-form `UPMBC(m)`, which permits one
simultaneous algebraic transform.  Refuting UPMBC itself requires excluding
every factor/opening/compiler quadruple in its definition.  None of these
local certificates is by itself a no-go for an unrelated upper-complete `T`,
the flat-middle gate, or coefficient one.

## 1. The exact architecture-free flat-middle gate

For a linear middle word

\[
 T=(T_0,\ldots,T_{W-1}),
\]

call `T` **upper-complete** if every subset of rank greater than `r` is the
union of a contiguous interval of `T`.  The Boolean system `COMP_d(T)` is
the exact system in
`MATH_THEOREM_K_ALL_ODD_PBBS_MARKOV_BOUNDARY_COMPILER_REDUCTION_20260729.md`,
Section 5: its feasible points are precisely the nonempty source words `A`
of length `W+d` satisfying `D^dA=T` and covering every target below rank
`r`.

### Theorem 1.1 (flat-middle equivalence)

The following are equivalent.

1. There is a universal nonempty word `A` of length `W+d` such that `D^dA`
   is a permutation of \(\binom{[k]}r\).
2. There is a permutation `T` of \(\binom{[k]}r\) which is upper-complete and
   for which `COMP_d(T)` is feasible.

Either condition implies

\[
 \nu(k)=W+d.
\]

#### Proof

Assume item 2.  A feasible compiler gives a nonempty word `A` of length
`W+d` with `D^dA=T` and every lower target.  The entries of `T` give every
middle target.  If an upper target is

\[
 Y=T_i\cup\cdots\cup T_j,
\]

then

\[
 Y=A_i\cup\cdots\cup A_{j+d}.
\]

Thus `A` is universal.  The monotone-deadline lower bound gives equality.

Conversely, let `A` satisfy item 1 and put `T=D^dA`.  The exact compiler
theorem says that `A` itself certifies `COMP_d(T)`.  Every interval `[a,b]`
of at most `d+1` source letters is contained in a full window `[i,i+d]`,
because

\[
 [\max(0,b-d),\min(a,W-1)]\ne\varnothing.
\]

It is therefore contained in one rank-`r` entry of `T`.  Let an upper target
`Y` be witnessed by `A_a,...,A_b`.  Its witness has at least `d+2` letters.
Every source position in `[a,b]` lies in at least one full `(d+1)`-window
contained in `[a,b]`; hence

\[
 Y=\bigcup_{p=a}^{b}A_p
  =\bigcup_{i=a}^{b-d}T_i.
\]

The right side is a contiguous interval of `T`, so `T` is upper-complete.
QED.

The positive-slack deadline theorem does not force `D^dA` to be a middle
permutation for every optimal word.  Theorem 1.1 is therefore an exact
equivalence inside the flat-middle normal form and an architecture-free
sufficient gate for the upper theorem.  Bare equality is not currently
known to imply this normal form.

## 2. Independent audit of PBBS q1 exactness

Put

\[
 \mathcal X=\binom{[2m+1]}m,
 \qquad \mathcal U=\binom{[2m+1]}{m+1},
\]

and let `f` be the canonical PBBS permutation on \(\mathcal X\).  Define two
maps from the lower to the upper shore by

\[
 M_+(A)=f(A)^c,
 \qquad M_-(A)=f^{-1}(A)^c.                            \tag{2.1}
\]

The audited PBBS inputs are

\[
 A\cap f(A)=\varnothing                                \tag{2.2}
\]

and the fact that `g=f^2` is a Johnson factor:

\[
 |C\cap f^2(C)|=m-1.                                   \tag{2.3}
\]

### Theorem 2.1 (antipodal PBBS q1-exact lift)

For every `m>=1`, `M_+` and `M_-` are edge-disjoint perfect matchings of the
rank-`m`/rank-`m+1` inclusion graph.  Their union `F_PBBS` is a simple
spanning two-factor.  After suppressing the rank-`m` shore, every rank-`m`
lower-q1 colour occurs exactly once.

#### Proof

By (2.2), `f(A)^c` contains `A`.  Applying (2.2) to `f^{-1}(A)` gives
`A\cap f^{-1}(A)=\varnothing`, so `f^{-1}(A)^c` also contains `A`.
Their rank is `m+1`, so they give incidence edges.  Each map is a bijection
because it is the composition of a permutation with complementation.  Thus
each is a perfect matching.

Substitute `C=f^{-1}(A)` in (2.3).  This gives

\[
 |f^{-1}(A)\cap f(A)|=m-1,                             \tag{2.4}
\]

so `f^{-1}(A)` and `f(A)` are distinct.  The two matching edges incident
with `A` are therefore distinct, proving edge-disjointness and simplicity.

The two upper neighbours of `A` are distinct rank-`m+1` supersets of the
same rank-`m` set `A`.  Their intersection is exactly `A`.  Suppressing the
lower vertex consequently creates one Johnson edge whose lower colour is
`A`.  This occurs once for each \(A\in\mathcal X\), proving multiplicity one,
not merely positive support.  QED.

No prime, quotient-freeness, PBBS homomesy, or shadow-load theorem is used in
this q1 argument.  For `m=1`, `f` is a 3-cycle, the bipartite factor is a
6-cycle, and its suppression is the q1-rainbow triangle.  For `m=0`, the two
matchings coincide, so `k=1` must remain the separate trivial case.

## 3. Identification with the all-depth source

The preceding q1-exact factor is not a different PBBS object accidentally
sharing the same cardinalities.  On a `g=f^2` component, write

\[
 B_{i+1}=g(B_i).
\]

Then the upper owner between `B_i` and `B_{i+1}` is

\[
 T_i=f(B_i)^c=M_+(B_i)=M_-(B_{i+1})
     =B_i\cup B_{i+1},                                 \tag{3.1}
\]

and

\[
 T_i\cap T_{i+1}=B_{i+1}.                              \tag{3.2}
\]

Thus the two-matching union is exactly the carrier used in
`THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md`.
The audited PBBS `q`-edge path theorem lifts through (3.1)--(3.2) to all
lower depths, and complementation supplies all upper depths.

Indeed, complementation sends the `M_+` edge
`A--f(A)^c` to the `M_-` edge `f(A)--A^c`; hence it preserves the factor and
exchanges the matchings.  Also

\[
 \bigcap_{a=-1}^{q}T_{i+a}
 =\bigcap_{a=0}^{q}B_{i+a},
\]

which is the literal lower-tower lift used by the all-depth audit.

The logical dependencies are therefore:

* Theorem 2.1 gives lower-q1 exactness.
* The PBBS chronology theorem gives deeper lower/upper support.
* Neither theorem gives growing `d`-residence.

There is a convention trap worth recording.  The bare centered factor
`g=f^2` on rank `m` has every adjacent union colour exactly once, while its
intersection loads may be one, two, or three.  It is the antipodal lift
(2.1), equivalently the rank-`m+1` carrier (3.1), which has the lower-q1
palette required by the UPMBC inclusion graph exactly once.

## 4. Exact protected component-reduction refinements

These statements apply only after a protected factor and a literal safe
switch library have been fixed.

### Theorem 4.1 (neutral-orbit positive-cut criterion)

Let `G_P` be the graph of protected q1-exact factors under the declared safe
switches, and let `c(F)` be component count.  At level `c`, connect factors
only by neutral switches; call the resulting connected components neutral
orbits.  Every factor has a route to component count at most two on which
`c` never increases if and only if every neutral orbit at every level
`c>2` has an incident safe switch to a lower level.

#### Proof

Inside a neutral orbit, route to a lower boundary edge and take it.  Induct
on the integer component count.  Conversely, a neutral orbit with no lower
boundary cannot be left by a nonincreasing route: neutral moves stay inside
it and every other exit raises the level.  QED.

For one specified source, contract neutral orbits and direct strict-decrease
edges downward.  Existence of one successful route is exactly directed
reachability of some level-at-most-two orbit.  It does **not** require every
other reachable branch to have a lower exit.  Requiring every reachable
state to remain completable gives that stronger robust quantifier.

This theorem captures a neutral legality router followed by a local circuit
splitter.  The obstruction for that fixed library is an entire trapped
neutral orbit, not one locally minimal factor.

### Lemma 4.2 (raw PBBS-star conflict degree)

The natural PBBS legal-star support hypergraph is linear and has degree at
most `m` at each physical centre.  If raw conflicts mean intersecting centre
triples, then, for `m>=2`,

\[
 \Delta_{\rm raw}\le3(m-1)=3r-6.                       \tag{4.1}
\]

Indeed, each of the three centres of a star belongs to at most `m-1` other
stars.  This is not the protected conflict degree: a separate collar/full-
signature heredity theorem is needed to prove that centre-disjoint stars
compose without destroying residence or a last shadow witness.
For `m=1,2` the legal-star atlas is empty.

### Lemma 4.3 (fixed-depth kernel multiplicity)

For `q>=1`, on a cycle of length greater than `2q`, suppose a fixed-depth
target has `t` distinct based `q`-edge witness windows.  If `K` is the
intersection of their edge spans, then

\[
 |K|\le\max\{q-t+1,0\}.                                \tag{4.2}
\]

If `K` is nonempty, cut at a common edge.  The witness starts lie among `q`
consecutive positions; their span is at least `t-1`, leaving common edge
length at most `q-(t-1)`.  In particular more than `q` occurrences force an
empty cut kernel.

This reduces safe-cut dispersion to exact componentwise multiplicity data.
PBBS supplies one canonical witness and hence only the weak bound `|K|<=q`
on a supporting component.  No audited theorem currently controls the
componentwise multiplicity distribution strongly enough to give a uniform
safe port.

### Lemma 4.4 (coupled lower/upper seam diamonds)

A Johnson edge is uniquely determined by its intersection `L` and union
`U`: if \(U\setminus L=\{a,b\}\), its endpoints are
\(L\cup\{a\}\) and \(L\cup\{b\}\).  Hence a genuinely new seam cannot
simultaneously reproduce both labels of one deleted edge.  In a fixed-window protected
opening, lower cut-colour recycling and last-occurrence upper repair are
therefore one off-diagonal diamond SDR, not two independent counts.  The two
outer source cells provide capacity for at most two unrecycled lower q1
colours; with two source cycles this frees the unique seam at the q1 capacity
level to serve upper chronology, as in the audited `k=15` nonrecycling
opening.  Simultaneous absorption remains subject to pinned full compiler
feasibility.

The independently audited ribbon identity further sharpens the component
calculus.  For a packet `pi` on `s` ports with old return `rho`, if
`t=c(rho)`, `o` is the orbit count of \(\langle\pi,\rho\rangle\), `b` is the cycle rank
of the packet--old-component incidence graph, and `g` is its ribbon genus
sum, then

\[
 \Gamma=t-o-b+2g.
\]

For one connected circuit this is `Gamma=2t-s-1+2g`.  The six-port fibre
`P=(01)(23)(45)`, `pi_E=(024)`, `pi_O=(135)` with endpoint deck loads
`(3,3)` and atomic loads `(0,6),(6,0)` is an exact abstract packet lock:
neither C6 is quota-protected alone, while the two-C6 endpoint is protected
and connected.  Thus the pointwise connected-exchange lemma is false for
generic abstract quota-protected fibres.  This does not instantiate the
residence/all-depth PBBS protected face; PBBS may still
satisfy a chronology-specific extraction or plateau-escape theorem.  The
full ribbon proof is in
`MATH_THEOREM_L_PBBS_PROTECTED_RIBBON_POSITIVE_CUT_AND_PACKET_LOCK_20260729.md`.

The full loose-fusion, acyclic target-token, and componentwise cut-product
statements are in
`MATH_THEOREM_K_PROTECTED_COMPONENT_REDUCTION_LOOSE_FUSION_AND_TOKEN_FLOW_20260729.md`
and
`MATH_THEOREM_K_ALL_ODD_PBBS_MARKOV_BOUNDARY_COMPILER_REDUCTION_20260729.md`.

## 5. Precise proved/conditional boundary

Let \(\mathscr P_{m,d}\) denote the `d`-resident, q1-exact, all-depth
protected factor face of the companion report.  The following are
unconditional.

1. The selected PBBS all-depth source is physically q1-exact for every
   `m>=1`.
2. All q1-exact factors lie in one algebraic alternating-circuit fibre.
3. The flat-middle target is exactly an upper-complete middle permutation
   `T` plus feasible full `COMP_d(T)`.
4. For a fixed protected switch library, neutral-orbit lower-boundary
   positivity is necessary and sufficient for nonincreasing component
   descent.
5. Endpoint-form UPMBC's component clause is exactly
   \(\min_{G\in\mathscr P_{m,d}}c(G)\le2\); protected routes are only
   sufficient certificates for this minimum.
6. Raw PBBS-star conflicts have degree at most `3r-6` for `m>=2`; promotion
   to protected compatibility is open.
7. Fixed-depth cut kernels obey (4.2); the required PBBS component-dispersion
   census is open.
8. The generic additive-quota pointwise connected-circuit exchange lemma is
   false by the six-port packet lock; no literal PBBS counterexample is known.

The continuing UPMBC attack must still produce, simultaneously:

* a resident/all-depth protected endpoint with at most two components;
* an upper-safe opening, equivalently a port outside its exact killed-target
  kernel/collar cover; and
* a feasible full `COMP_d(T)` with all boundary pins.

A more general many-component opening whose cut losses the compiler absorbs
would be a replacement wrapper leading directly to Theorem 1.1, not a
literal instance of UPMBC's at-most-two-component clause.

`LFE(m)`, `APF(m)`, and the neutral-orbit condition are useful sufficient
component-reduction routes.  A failure certificate for one does not refute
the others.  A route obstruction refutes endpoint-form UPMBC only if it also
proves that no protected at-most-two-component endpoint exists under a
simultaneous transform.  Even a complete endpoint obstruction would close
only this PBBS wrapper; the architecture-free target of Theorem 1.1 would
remain.
