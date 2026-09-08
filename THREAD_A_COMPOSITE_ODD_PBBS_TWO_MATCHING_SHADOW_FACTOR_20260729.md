# Composite-odd PBBS two-matching shadow factor

Date: 2026-07-29

Status: unconditional all-odd-`k` solution of the raw quotient-factor
conditions and, more strongly, complete correct-window support on the entire
lower and upper shadow towers.  Connectivity, unit voltage, residence,
opening, and the common compiler are not claimed.

Primary inputs:

* `MATH_THEOREM_COMPOSITE_ODD_QUOTIENT_FACTOR_MASTER_20260729.md`;
* `MATH_THEOREM_Q1_RAINBOW_CYCLE_AFFINE_NO_GO_AND_GLOBAL_FACTOR_FIBER_20260729.md`;
* `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, especially Theorem 21.2;
* `MATH_AUDIT_PBBS_ALLQ_CORRIDOR_AND_FIXED_BAND_WORDS_20260726.md`;
* `MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md`.

## 0. Verdict

The four raw constraints of the composite-odd quotient factor master have
an explicit solution for every odd

\[
 k=2m+1\qquad(m\ge1).
\]

Let \(f\) be the canonical PBBS permutation of the rank-\(m\) subsets of
\(\mathbb Z_k\).  The two maps

\[
 M_+(A)=f(A)^c,\qquad M_-(A)=f^{-1}(A)^c             \tag{0.1}
\]

are edge-disjoint perfect matchings of the middle-levels incidence graph.
Their union is a spanning degree-two factor.  If

\[
 \theta(A)=f^{-1}(A)\cap f(A),                       \tag{0.2}
\]

then the lower-`q2` colour at the upper vertex \(A^c\) is exactly
\(\theta(A)\), while the upper-`q1` colour at the lower vertex \(A\) is
exactly \(\theta(A)^c\).  The audited PBBS first-turn theorem says that
\(\theta\) covers every rank-\((m-1)\) set, with physical loads between one
and three.  Hence both required colour shores are complete simultaneously.

The same construction is all-depth.  Every correct PBBS \(q\)-edge
intersection path gives both a lower carrier window at depth \(q+1\) and,
after complementation, an upper carrier window at depth \(q\).  The audited
all-depth PBBS theorem therefore covers the entire Boolean lattice through
one spanning factor.  This is a support statement: not every window has the
correct rank, and no residence or safe-cut conclusion follows.

The construction commutes with cyclic coordinate rotation.  Central
freeness therefore makes it a binary solution of the composite quotient
master.  Short target orbits at composite \(k\) cause no problem because
the theorem proves physical coverage before quotienting.

Thus the raw `k=15` CNF is not an existence gate if it contains exactly the
four constraints in the master and permits the weighted quotient-loop
convention.  It remains useful as an encoding audit or after adding genuinely
extra requirements such as connectivity, voltage, residence, or compiler
constraints.

## 1. A general antipodal two-matching lemma

Let

\[
 \Omega=[2m+1],\qquad {\cal X}=\binom{\Omega}{m},
 \qquad {\cal T}=\binom{\Omega}{m+1},\qquad
 W=|{\cal X}|=|{\cal T}|.
\]

Let \(B_m\) be the bipartite incidence graph between \({\cal X}\) and
\({\cal T}\).  We first isolate the precise properties of PBBS which are
used.

### Theorem 1.1 (antipodal two-matching lift)

Suppose \(f:{\cal X}\to{\cal X}\) is a permutation satisfying

\[
 A\cap f(A)=\varnothing                                      \tag{1.1}
\]

for every \(A\), and suppose

\[
 |f^{-1}(A)\cap f(A)|=m-1                                   \tag{1.2}
\]

for every \(A\).  Define \(M_+,M_-\) by (0.1), and put
\(F=M_+\cup M_-\).  Then:

1. \(M_+\) and \(M_-\) are edge-disjoint perfect matchings of \(B_m\);
2. \(F\) is a spanning simple two-factor of \(B_m\);
3. the two-step monodromy of \(F\) on \({\cal X}\) is \(f^2\);
4. after suppressing the \({\cal X}\)-shore, the resulting Johnson factor
   on \({\cal T}\) has every lower-`q1` colour exactly once;
5. its lower-`q2` and upper-`q1` colours are respectively

   \[
    R(A^c)=\theta(A),\qquad U(A)=\theta(A)^c,          \tag{1.3}
   \]

   where \(\theta\) is (0.2).

Consequently, if \(\theta({\cal X})=\binom{\Omega}{m-1}\), then \(F\)
has complete lower-`q2` and upper-`q1` support.

#### Proof

By (1.1), \(f(A)^c\) and \(f^{-1}(A)^c\) both contain \(A\), and both
have size \(m+1\).  Thus (0.1) gives incidence edges.  Each map in (0.1)
is a bijection from \({\cal X}\) to \({\cal T}\), being a composition of
a permutation with complementation.  Hence each is a perfect matching.

Condition (1.2) implies \(f^{-1}(A)\ne f(A)\), so the two matching edges at
\(A\) are distinct.  They are therefore edge-disjoint everywhere, and
their union is a spanning simple two-factor.

Follow first the \(M_+\)-edge out of \(A\).  It reaches \(f(A)^c\).  The
lower endpoint of the \(M_-\)-edge at that upper vertex is the unique \(C\)
such that

\[
 f^{-1}(C)^c=f(A)^c,
\]

namely \(C=f^2(A)\).  This proves the monodromy assertion.

At a lower vertex \(A\), the two upper neighbours are distinct
rank-\((m+1)\) supersets of \(A\).  Their intersection is therefore exactly
\(A\).  Thus the Johnson edge obtained by suppressing \(A\) has lower colour
\(A\), and every such colour occurs once.

The union of those same two upper neighbours is

\[
 f^{-1}(A)^c\cup f(A)^c
   =\bigl(f^{-1}(A)\cap f(A)\bigr)^c
   =\theta(A)^c.                                      \tag{1.4}
\]

This is the upper-`q1` colour centred at \(A\).

Now fix the upper vertex \(A^c\).  Its \(M_+\)-neighbour is
\(f^{-1}(A)\), while its \(M_-\)-neighbour is \(f(A)\).  Their intersection
is \(\theta(A)\), which is the lower-`q2` turn colour at \(A^c\).  This
proves (1.3), and surjectivity of \(\theta\) proves the final assertion.
\(\square\)

### Corollary 1.2 (the two target histograms are identical)

For \(R\in\binom{\Omega}{m-1}\), put

\[
 \mu(R)=|\{A\in{\cal X}:\theta(A)=R\}|.              \tag{1.5}
\]

In the factor of Theorem 1.1, the physical lower-`q2` load of \(R\) and
the physical upper-`q1` load of \(R^c\) are both exactly \(\mu(R)\).

#### Proof

This is occurrence-wise (1.3), not merely equality after summation.
\(\square\)

This equality is the useful extra structure absent from an arbitrary
fractional Hall solution: a single turn design controls both shores.

## 2. PBBS supplies the required turn design

Let \(f\) now be the canonical PBBS update on the odd graph
\(KG(2m+1,m)\).  The audited PBBS facts used below are:

1. \(f\) is a permutation and \(A\cap f(A)=\varnothing\);
2. \(f\) commutes with every cyclic coordinate rotation;
3. \(g=f^2\) is a Johnson cycle factor on \(\binom{\Omega}{m}\); and
4. for every \(R\in\binom{\Omega}{m-1}\), there is a forward edge
   \(C\to g(C)\) with

   \[
    C\cap g(C)=R,                                    \tag{2.1}
   \]

   and the number of such oriented starts is between one and three.

Item 4 is Theorem 21.2 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` at \(q=1\); its indexing and
shared-coordinate cases are independently checked in
`MATH_AUDIT_PBBS_ALLQ_CORRIDOR_AND_FIXED_BAND_WORDS_20260726.md`.

### Theorem 2.1 (all-odd PBBS shadow-factor theorem)

For every \(m\ge1\), the PBBS matchings (0.1) form a spanning middle-levels
two-factor with all of the following exact properties:

1. every rank-\((m+1)\) owner has degree two;
2. every rank-\(m\) lower-`q1` colour occurs exactly once;
3. every rank-\((m-1)\) lower-`q2` target occurs;
4. every rank-\((m+2)\) upper-`q1` target occurs;
5. corresponding complementary targets in items 3 and 4 have equal physical
   load, lying in \(\{1,2,3\}\).

#### Proof

The step-two Johnson property gives

\[
 |C\cap f^2(C)|=m-1                                  \tag{2.2}
\]

for every \(C\).  Substituting \(C=f^{-1}(A)\) gives

\[
 |f^{-1}(A)\cap f(A)|=m-1,                           \tag{2.3}
\]

so Theorem 1.1 applies.

Moreover, under the same substitution,

\[
 C\cap g(C)=f^{-1}(A)\cap f(A)=\theta(A).            \tag{2.4}
\]

As \(A\) ranges over \({\cal X}\), so does \(C=f^{-1}(A)\).  The audited
PBBS theorem therefore says that \(\theta\) covers every rank-\((m-1)\)
target with load between one and three.  Theorem 1.1 and Corollary 1.2 now
give all five conclusions.  \(\square\)

There is no probabilistic rounding and no appeal to a fixed-uniformity
nibble in this proof.  The two perfect matchings and their common colour
profile are explicit functions of the PBBS permutation.

### Theorem 2.2 (the complete two-sided shadow tower)

Orient every component of \(g=f^2\); on one component write

\[
 \ldots,B_{i-1},B_i,B_{i+1},\ldots,
 \qquad B_{i+1}=g(B_i),                              \tag{2.5}
\]

and put

\[
 T_i=f(B_i)^c=B_i\cup B_{i+1}.                       \tag{2.6}
\]

Then \((T_i)\) is the corresponding rank-\((m+1)\) carrier component and

\[
 T_i\cap T_{i+1}=B_{i+1}.                            \tag{2.7}
\]

Across this family of components, for every \(1\le q\le m\) and every
\(S\in\binom{\Omega}{m-q}\), there are a component and an index \(i\) such
that

\[
 \bigcap_{a=0}^{q}B_{i+a}=S.                         \tag{2.8}
\]

The same occurrence gives simultaneously

\[
 \boxed{\bigcap_{a=-1}^{q}T_{i+a}=S}                 \tag{2.9}
\]

at lower carrier depth \(q+1\), and

\[
 \boxed{\bigcup_{a=0}^{q}B_{i+a}^c=S^c}             \tag{2.10}
\]

at upper carrier depth \(q\) on the complement component.  Consequently
the PBBS factor covers every target at every lower and upper rank.  The
complementary physical correct-window loads agree occurrencewise and obey

\[
 1\le \mu_q(S)=\mu_q^+(S^c)\le\binom{2q+1}{q}.       \tag{2.11}
\]

#### Proof

Both \(B_i\) and \(B_{i+1}=f^2(B_i)\) are disjoint from \(f(B_i)\).
They are distinct \(m\)-subsets with intersection of size \(m-1\), so their
union is the full \((m+1)\)-set \(f(B_i)^c\), proving (2.6).  Equation
(2.6) also gives

\[
 M_+(B_i)=T_i=M_-(B_{i+1}),
\]

so these are precisely the alternating factor components.  Equation (2.7)
follows because consecutive distinct rank-\((m+1)\) owners contain the
common facet \(B_{i+1}\).

The audited all-depth PBBS theorem supplies (2.8), with the load bound in
(2.11).  Intersecting the adjacent identities (2.7) gives

\[
 \bigcap_{a=-1}^{q}T_{i+a}
 =\bigcap_{a=0}^{q}(T_{i+a-1}\cap T_{i+a})
 =\bigcap_{a=0}^{q}B_{i+a}=S,
\]

which proves (2.9).  The upper owners
\(B_i^c,B_{i+1}^c,\ldots\) are consecutive on the complement component:
\(B_j^c\) and \(B_{j+1}^c\) share the selected lower neighbour \(f(B_j)\).
De Morgan's law now gives (2.10).  The two occurrence maps use the same
oriented PBBS start, so the correct-window loads agree exactly; here
\(\mu_q^+\) denotes the complementary upper correct-window load.  \(\square\)

Depth one below the carrier and the central owner layer were already exact
in Theorem 2.1.  Together with \(q=1,\ldots,m\) above, Theorem 2.2 covers
all ranks \(0,1,\ldots,2m+1\).

### Corollary 2.3 (complement symmetry and a Catalan component bound)

The factor \(F\) is complement-invariant, and complementation exchanges
\(M_+\) with \(M_-\).  If the PBBS permutation cycles have lengths
\(P_1,\ldots,P_c\), then

\[
 c(F)=\sum_{j=1}^c\gcd(P_j,2),                      \tag{2.12}
\]

and every component of \(F\) contains a multiple of \(k\) lower vertices.
Consequently

\[
 \boxed{c(F)\le \frac{W}{k}=\operatorname{Cat}_m.} \tag{2.13}
\]

If \(P_j\) is odd, its lifted component is self-complementary.  If \(P_j\)
is even, it gives two components exchanged by complementation.

#### Proof

The complement of the \(M_+\)-edge from \(A\) to \(f(A)^c\) is the
\(M_-\)-edge from \(f(A)\) to \(A^c\).  This proves the first assertion.

On an \(f\)-cycle of length \(P_j\), the lower-shore monodromy \(f^2\)
has \(\gcd(P_j,2)\) cycles, each of length
\(P_j/\gcd(P_j,2)\), proving (2.12).  The audited PBBS coordinate-homomesy
theorem says that every \(P_j\) is divisible by the odd integer \(k\).
If \(P_j\) is even, its cofactor \(P_j/k\) is even, so \(P_j/2\) remains
divisible by \(k\).  Thus every \(f^2\)-cycle has at least \(k\) vertices,
and their total number is at most \(W/k\).  The parity description also
gives the final complement statement.  \(\square\)

## 3. Exact descent to the composite quotient master

Return to cyclic ground \(\Omega=\mathbb Z_k\), and let \(\rho\) denote
coordinate rotation.  For a lower vertex \(A\), define the two omitted
coordinates

\[
 \{a_+(A)\}=\Omega\setminus(A\cup f(A)),\qquad
 \{a_-(A)\}=\Omega\setminus(A\cup f^{-1}(A)).       \tag{3.1}
\]

Each right-hand side is a singleton.  In the pair-choice notation of the
quotient master, select at \([A]\) the pair

\[
 \boxed{\{a_+(A),a_-(A)\}.}                          \tag{3.2}
\]

Indeed,

\[
 f(A)^c=A\cup\{a_+(A)\},\qquad
 f^{-1}(A)^c=A\cup\{a_-(A)\}.                       \tag{3.3}
\]

### Theorem 3.1 (binary quotient certificate for every odd `k`)

The choices (3.2) are well defined on rotation orbits and satisfy all four
constraints of the exact composite-odd quotient factor master:

1. exactly one pair is selected at every rank-\(m\) orbit;
2. every rank-\((m+1)\) orbit has weighted quotient degree two;
3. every rank-\((m+2)\) orbit is covered by a selected upper-`q1` colour;
4. every rank-\((m-1)\) orbit is covered by a lower-`q2` turn colour.

#### Proof

PBBS equivariance gives

\[
 f(\rho A)=\rho f(A),\qquad
 a_\pm(\rho A)=\rho a_\pm(A),                       \tag{3.4}
\]

so (3.2) is independent of the orbit representative.  The action on the
two central ranks is free for every odd \(k\), by the central-freeness lemma
in the composite master.  The physical factor from Theorem 2.1 therefore
descends to one binary pair choice per lower orbit.

Every physical upper owner has degree two.  On quotienting, an ordinary
edge contributes one incidence and a quotient loop contributes two, so the
weighted degree equation remains exactly two.  This proves items 1--2.

Items 3--4 follow by quotienting the physical coverage in Theorem 2.1.
This step uses no freeness of the shadow ranks.  If a shadow has a short
rotation orbit, one PBBS witness still covers that entire actual orbit;
only its physical multiplicity differs from an unweighted quotient count.
\(\square\)

Thus the theorem is valid without a prime hypothesis and without imposing
the obsolete quotient load cap on short shadow orbits.

The same physical-first argument descends Theorem 2.2 at every depth: every
actual target orbit has a correct PBBS witness orbit.  At noncentral ranks
this is an orbit-coverage assertion only; its quotient load must again be
weighted by the actual stabilizer.

### Corollary 3.2 (exact short-orbit accounting)

Let \(R\) be a rank-\((m-1)\) target, let \(s=|[R]|\) be its rotation-orbit
length, and let \(q_R\) be the number of free central domain orbits whose
PBBS turn image lies in \([R]\).  Then

\[
 \boxed{\mu(R)=q_R\frac{k}{s}.}                     \tag{3.5}
\]

Moreover a shadow target at either rank \(m-1\) or rank \(m+2\) has
stabilizer order only one or three.  Hence:

* on a free target orbit, \(q_R=\mu(R)\in\{1,2,3\}\);
* on a short target orbit, \(s=k/3\), \(\mu(R)=3\), and \(q_R=1\).

#### Proof

The central domain action is free.  On one domain orbit whose image is
\([R]\), equivariance maps its \(k\) elements uniformly onto the \(s\)
targets in \([R]\), giving \(k/s\) occurrences of each.  Summing the
contributing domain orbits proves (3.5).

If a translation stabilizer has order \(d\), every invariant set is a union
of \(d\)-element coordinate orbits, so \(d\) divides both \(k\) and its
rank.  But

\[
 \gcd(k,m-1)=\gcd(3,m-1),\qquad
 \gcd(k,m+2)=\gcd(3,m+2).                           \tag{3.6}
\]

Thus \(d\in\{1,3\}\).  In the short case, (3.5) and the PBBS bound
\(1\le\mu(R)\le3\) force \(q_R=1\) and \(\mu(R)=3\).  The upper statement
follows by complementation.  \(\square\)

## 4. Counts and the two current calibrations

Put

\[
 W=\binom{2m+1}{m}=\binom{2m+1}{m+1},\qquad
 M=\binom{2m+1}{m-1}=\binom{2m+1}{m+2}.             \tag{4.1}
\]

There are \(W\) occurrences on each target shore, and

\[
 W-M=\frac{2W}{m+2}.                                \tag{4.2}
\]

The two complementary PBBS load histograms are identical, supported on
\(M\) targets, and have values only in \(\{1,2,3\}\).  Their total repeat
excess is exactly the unavoidable value (4.2).  The theorem does not assert
that the load-three count vanishes.

At `k=9` one has

\[
 W=126,\qquad M=84,\qquad W-M=42.                   \tag{4.3}
\]

The previously decoded connected coprime-voltage factor is stronger than
Theorem 3.1 in topology, but is not needed for raw existence.

The frozen PBBS first-shadow audit gives the physical load histogram

\[
 1^{45}2^{36}3^3,                                    \tag{4.4}
\]

and therefore quotient loads \(1^6 2^4\) on each of the two target
palettes.  The unique short target orbit has physical load three and
quotient load one, as Corollary 3.2 requires.  The PBBS quotient factor uses
three projected Johnson loops, so the known connected loop-free calibration
is genuinely stronger rather than a decoding of this particular factor.

At `k=15` one has

\[
 W=6435,\qquad M=5005,\qquad W-M=1430.              \tag{4.5}
\]

There are 429 central orbits and 335 actual target orbits on each shadow
shore.  The audited physical PBBS histogram is

\[
 1^{3630}2^{1320}3^{55};                             \tag{4.6}
\]

after quotienting, both palettes have the exact histogram

\[
 \boxed{1^{244}2^{88}3^3.}                          \tag{4.7}
\]

The two size-five target orbits are among the load-one quotient targets and
have physical load three.  Thus Theorem 3.1 gives an analytic satisfying
assignment for the raw 12,012-choice model.  A CNF which additionally
requests one quotient cycle, unit voltage, residence, loop-free
serialization, or compiler compatibility is a strictly stronger model and
is not settled by this construction.  A direct quotient audit finds that the
PBBS certificate uses two of the fourteen projected-loop choices at `k=15`;
the weighted degree convention of the master counts each correctly twice.

## 5. Exact boundary after the construction

The theorem closes the factor-and-all-shadow-support existence gate.

1. The components of the factor are the cycles of \(g=f^2\).  They need
   not form one Hamilton cycle and need not have unit quotient voltage.
2. Theorem 2.2 supplies complete lower and upper support at every depth, but
   it does not say that every nominal-depth window has the correct rank,
   eliminate short residence intervals, or produce a safe common opening.
3. No assertion here couples the factor to the lower compiler, owner Hall,
   or a literal finite word without seam costs.
4. Excluding quotient loops or prescribing a particular component topology
   can discard the explicit certificate and requires a separate theorem.

In particular, Hall, matroid intersection, and absorption are unnecessary
for the raw four-constraint master.  They become relevant only when one adds
one of the later seam gates in items 1--4.

## 6. Adversarial audit

The proof has three nontrivial dependencies, each used at its exact scope.

* Disjointness \(A\cap f(A)=\varnothing\) makes (0.1) incidence matchings;
  it does not imply turn coverage.
* The step-two Johnson property gives the pointwise rank identity (2.3);
  it does not imply that all turn colours occur.
* PBBS Theorem 21.2 at \(q=1\) supplies the missing surjectivity and the
  load-three bound; at general \(q\) it supplies Theorem 2.2.  It is a
  correct-window support theorem, not a residence or connectivity theorem.

The lower and upper coverage claims are checked twice: locally by (1.3),
and globally by the bijective reindexing (2.4).  Composite target
stabilizers are handled only after physical coverage is proved.  Therefore
no unweighted quotient load is being mistaken for a physical multiplicity.
