# Growing port factors: sparse rooted component variance and the phase-expansion obstruction

Date: 2026-07-26

Method: pure mathematics only.

Audited inputs:

* `MATH_THEOREM_TWO_SEED_COMPONENT_MIXING_20260726.md`;
* `MATH_ATTACK_N_SINGLE_TRANSPOSITION_OVERLAY_COMPONENT_ACTION_20260726.md`;
* `MATH_ATTACK_AB_OVERLAY_EXPANSION_REPORT_RAW_20260724.md` and its
  independent audit;
* `MATH_AUDIT_ITERATED_S1_COMPONENT_ROUTING_20260726.md`;
* `MATH_THEOREM_V4_COMPONENT_AND_D4_FRINGE_INDIVISIBILITY_20260726.md`;
* `MATH_AUDIT_GROWING_CATALAN_SKELETON_HYPERGRAPH_AND_PORT_OBSTRUCTION_20260726.md`.

## 0. Verdict

Replacing the canonical MSW seed by a genuinely growing
\(\mathcal D_s\)-port factor does leave one exact-factor heat route open,
but growth of the seed is not itself the useful property.  The useful
property is the conjunction of

1. a small common root block system for the two complete ownership
   partitions, and
2. a small **full cyclic-profile edit budget** inside each root-matched
   pair of rows.

The main new estimate is the following.  If \(b\) is the largest rooted
ownership component and \(L_H(F,G)\) is the weighted sum of the
root-by-root half-\(L^1\) distances of the complete depth profiles, then
the exact component variance satisfies

\[
                         \boxed{V_H(F,G)\le 2bL_H(F,G).}       \tag{0.1}
\]

No coordinate-relabeling relation between \(F\) and \(G\) is used.  If
the two cyclic orders at every root differ only inside \(k\) consecutive
positions, with the exterior carrier fixed, then every crossing collar is
included and

\[
 \boxed{L_H(F,G)\le 2(k-1)\operatorname {Cat}_s
                    \sum_{q\le H}w_q.}                       \tag{0.2}
\]

Consequently bounded components and bounded consecutive edits give a
floor-energy residue \(O(H\operatorname {Cat}_s)\) on a Gaussian window.
More generally, at \(H=A\sqrt s\), the residue is \(o(W_s)\) whenever

\[
                              bk=o(\sqrt s),                  \tag{0.3}
\]

where \(W_s=\binom{2s+1}{s}=(2s+1)\operatorname {Cat}_s\).
This is a genuine mesoscopic growing-seed regime.

There is an exact opposing obstruction.  In the common-phase-layer
subclass, let \(\sigma_t\) be the root permutation comparing the two
phase-\(t\) transversals.  Every full ownership component contains an
orbit of \(\langle\sigma_t:0\le t\le s\rangle\).  If this group is
transitive, the full overlay is connected and component switching produces
only the original two factors.  Thus phase-owner expansion, by itself,
destroys rather than supplies heat coordinates.

The bounded-seed no-go is therefore not reversed.  Even granting a strict
interior \(\mathcal D_4\) packet acceptable variance, it is invisible to
the charged boundary statistic, while a literal operadic growing-skeleton
transport reaches only \(o(\operatorname {Cat}_s)\) roots.  The precise
remaining construction is a genuinely growing pair of port factors having
counterbias (or coherent separation), small rooted owner blocks, and small
complete-profile edit budget.  Section 7 states the exact lemma.

## 1. Root-contracted ownership graph

Put

\[
 n=2s+1,\qquad C_s=\operatorname {Cat}_s,\qquad
 W_s=nC_s=\binom{2s+1}{s}.
\]

Let \(F\) and \(G\) be arbitrary exact \(\mathcal D_s\)-port factors on
the same coordinate set \(\Omega\).  Their rows are indexed by
\(P\in\mathcal D_s\), and the row indexed by \(P\) has the prescribed
port \(P\) (and prescribed complementary terminal port).  No relation by a
coordinate permutation is assumed.

For a middle set \(X\in\binom\Omega s\), let

\[
                 \rho_F(X),\rho_G(X)\in\mathcal D_s
\]

be its unique row owners in the two exact factors.  Define the rooted
owner multigraph \(\Gamma(F,G)\) on \(\mathcal D_s\) by putting, for every
middle set \(X\), one undirected edge

\[
                         \{\rho_F(X),\rho_G(X)\}.        \tag{1.1}
\]

Loops and parallel edges are retained for the definition, although loops
do not affect connectivity.

### Theorem 1.1 (root-contracted component theorem)

The connected components of \(\Gamma(F,G)\) are exactly the root-label
sets of the full bipartite ownership components of \(F\) and \(G\), after
the prescribed port edges have been contracted.  In particular, if
\(K\subseteq\mathcal D_s\) is one component, then both shores contain
exactly the rows indexed by \(K\), and either complete shore may be chosen
while preserving an exact \(\mathcal D_s\)-port factor.

#### Proof

The middle port \(P\) is owned by row \(P\) in both factors.  Hence the
ownership edge labelled by \(P\) pairs the two rows with label \(P\), and
these port edges form a perfect matching between the shores.  Contract
them.  The ownership edge labelled by an arbitrary middle set \(X\) then
has endpoints \(\rho_F(X)\) and \(\rho_G(X)\), which is exactly (1.1).
This proves the component assertion.

For one component, its middle-set edge labels are partitioned by its
\(F\)-rows and also by its \(G\)-rows.  Choosing either whole shore
therefore covers those middle sets once, and the contracted port matching
shows that the same root labels occur on both shores.  Independent choices
over components preserve exact ownership and every prescribed port.
\(\square\)

This theorem is special to rooted factors in one useful respect: it gives
a canonical row pairing \(P\leftrightarrow P\) inside every component.
That pairing is what makes the sparse variance estimate below possible.

## 2. Phase expansion is an obstruction to switching

Suppose now that \(F\) and \(G\) lie in the common-phase-layer subclass.
Thus, at every \(X\)-phase \(0\le t\le s\), both factors use the same
transversal \(L_t\subseteq\binom{[2s]}s\).  Write

\[
 i_t^F,i_t^G:\mathcal D_s\longrightarrow L_t             \tag{2.1}
\]

for the two root-to-state bijections and put

\[
                 \sigma_t=(i_t^G)^{-1}i_t^F
                    \in\operatorname {Sym}(\mathcal D_s). \tag{2.2}
\]

The endpoint conditions give \(\sigma_0=\sigma_s=1\).

### Theorem 2.1 (phase-orbit lower bound on full components)

Every rooted ownership component is a union of orbits of

\[
                 \mathfrak G(F,G)
                   =\langle\sigma_t:0\le t\le s\rangle. \tag{2.3}
\]

Equivalently, each \(\mathfrak G(F,G)\)-orbit is contained in one full
ownership component.  The remaining middle states, equivalently the
adjacent-union colour ledger, may merge these orbits but cannot split them.
In particular, if \(\mathfrak G(F,G)\) is transitive, then the full overlay
is connected and the two-shore component switch has only the endpoint
outcomes \(F\) and \(G\).

#### Proof

For \(P\in\mathcal D_s\), the phase-\(t\) state in its \(F\)-row is
\(i_t^F(P)\).  Its owner in \(G\) is the unique \(Q\) satisfying

\[
 i_t^G(Q)=i_t^F(P),
\]

namely \(Q=\sigma_t(P)\).  Therefore \(\Gamma(F,G)\) contains every edge
\(P--\sigma_t(P)\).  Connectivity under these edges is exactly the orbit
relation of (2.3).  Adding all other ownership edges only coarsens that
partition.  Transitivity gives one component.  A connected two-factor
overlay has one Boolean shore choice, hence only its two shores.
\(\square\)

Thus a growing factor whose comparison phases act transitively on the
Catalan roots is maximally unsuitable for component heat, even if those
phases look highly dispersed targetwise.  To have components of size at
most \(b\), all phase comparison permutations must preserve a common block
system whose blocks have size at most \(b\), and every remaining colour
owner edge must preserve the same blocks.

## 3. Exact sparse rooted variance bound

For \(1\le q\le H\le s-1\), put

\[
 \mathcal X_q=\binom\Omega{s-q}.
\]

Let \(z_{q,P}^F\in\{0,1\}^{\mathcal X_q}\) be the complete incidence
vector of all cyclic \((s-q)\)-intervals in the row of \(F\) rooted at
\(P\); define \(z_{q,P}^G\) similarly.  Each vector has exactly \(n\)
ones.  For an ownership component \(K\), its signed depth profile is

\[
 \delta_{q,K}
   =\sum_{P\in K}(z_{q,P}^G-z_{q,P}^F).                 \tag{3.1}
\]

Let \(w_q\ge0\) be arbitrary weights and define

\[
 V_H(F,G)=\sum_{q=1}^Hw_q\sum_K\|\delta_{q,K}\|_2^2,   \tag{3.2}
\]

\[
 L_H(F,G)=\frac12\sum_{q=1}^Hw_q
            \sum_{P\in\mathcal D_s}
             \|z_{q,P}^G-z_{q,P}^F\|_1.               \tag{3.3}
\]

Thus \(L_H\) counts the weighted root-matched cyclic targets which fail to
cancel row by row.  For a standalone growing factor these are all physical
cyclic starts, including the starts which cross the distinguished port.
For a lift into a larger ambient word, \(z_{q,P}\) must instead be defined
from the complete **ambient** cyclic-window histogram (or from a common
start-resolved push-forward); the local vector displayed above does not by
itself account for new carrier starts.  In either interpretation this is
not a marked-occurrence statistic.  Put

\[
                         b(F,G)=\max_K|K|.               \tag{3.4}
\]

### Theorem 3.1 (sparse rooted component variance)

For arbitrary exact rooted factors \(F,G\),

\[
             \boxed{V_H(F,G)\le2b(F,G)L_H(F,G).}         \tag{3.5}
\]

More precisely, if

\[
 r_{q,K}=\frac12\|\delta_{q,K}\|_1,
\]

then

\[
 \|\delta_{q,K}\|_2^2\le2|K|r_{q,K},\qquad
 \sum_Kr_{q,K}\le\frac12\sum_P
                  \|z_{q,P}^G-z_{q,P}^F\|_1.          \tag{3.6}
\]

#### Proof

At a fixed target, each shore of a component of size \(|K|\) contributes
an integer between zero and \(|K|\).  Hence

\[
                    \|\delta_{q,K}\|_\infty\le |K|.
\]

Therefore

\[
 \|\delta_{q,K}\|_2^2
 \le\|\delta_{q,K}\|_\infty\|\delta_{q,K}\|_1
 \le2|K|r_{q,K}.
\]

Formula (3.1) and the triangle inequality give

\[
 2r_{q,K}
 \le\sum_{P\in K}\|z_{q,P}^G-z_{q,P}^F\|_1.
\]

Sum over the component partition, multiply by \(w_q\), and then sum over
\(q\).  This proves (3.5).  \(\square\)

The gain over the raw bound
\(\|\delta_{q,K}\|_2^2\le2n|K|^2\) is decisive when the two complete row
profiles are close.  The estimate is completely independent of whether
the two seeds are coordinate conjugates.

## 4. A full collar bound for consecutive row edits

The edit budget in (3.3) can be checked directly on cyclic orders.

### Lemma 4.1 (consecutive-block collar lemma)

Let two cyclic orders of the same \(n\) coordinates agree at every
position outside one cyclic interval \(I\) of \(k\) positions.  Inside
\(I\) they may be arbitrary permutations of the same \(k\) coordinates.
For every window length \(1\le r<n\), let \(z_r,z'_r\) be their cyclic
window incidence vectors.  Then

\[
                  \boxed{\frac12\|z_r-z'_r\|_1
                          \le2(k-1).}                   \tag{4.1}
\]

This counts all windows crossing either boundary of \(I\).

#### Proof

A positional cyclic \(r\)-window has the same coordinate set in both
orders unless it contains a nonempty proper part of \(I\).  Every window
with such a proper intersection has at least one of its two boundary cuts
strictly inside \(I\).  There are \(k-1\) internal cuts.  For a fixed
window length, each cut is the left boundary of one window and the right
boundary of one window.  Hence at most \(2(k-1)\) positional windows can
change.

All cyclic windows of a fixed proper length in a cyclic order of distinct
coordinates are distinct.  Keeping the unchanged positional windows
paired shows that the half-\(L^1\) distance between the two incidence
vectors is at most the number of changed old windows.  This proves (4.1).
\(\square\)

### Corollary 4.2 (rootwise bounded-arc variance)

Suppose that, for every root \(P\), the two row orders differ only inside
a cyclic block of at most \(k\) consecutive positions.  Put

\[
                         \Omega_H=\sum_{q=1}^Hw_q.
\]

Then

\[
 L_H(F,G)\le2(k-1)C_s\Omega_H,                          \tag{4.2}
\]

and

\[
 \boxed{V_H(F,G)\le4b(F,G)(k-1)C_s\Omega_H.}           \tag{4.3}
\]

#### Proof

Apply Lemma 4.1 with \(r=s-q\) to every root and depth, then use Theorem
3.1. \(\square\)

For a standalone row, or for two ambient cyclic words which differ in the
same one-block fashion, an exterior carrier causes no hidden term: every
window crossing the changed block is already among the windows counted in
(4.1).  A merely formal bounded-slab embedding need not have this property;
then one must apply Theorem 3.1 to its actual ambient profiles, or sum the
internal-cut bound over all changed ambient blocks.  Conversely, if an
entire growing seed block of length
\(\Theta(s)\) is freely reordered, (4.2) has \(k=\Theta(s)\).  One may not
call such a substitution a bounded-collar operation merely because it has
one formal port.

There is a complementary formulation in the adjacent-edit metric.  Since
cyclic interval profiles do not see a rotation or reversal, define
\(d(P)\) to be the minimum number of adjacent swaps needed to pass from the
row order of \(F\) at \(P\) to that of \(G\), after choosing the better
dihedral representatives.  Any displayed adjacent-swap sequence gives a
valid upper bound if the minimum is inconvenient to compute.

### Corollary 4.3 (adjacent-edit component theorem)

With \(b_K=|K|\),

\[
 \boxed{
 V_H(F,G)
 \le4\Omega_H\sum_K b_K\sum_{P\in K}d(P).}             \tag{4.4}
\]

In particular,

\[
 V_H(F,G)
 \le4\Omega_H b(F,G)\sum_{P\in\mathcal D_s}d(P).       \tag{4.5}
\]

#### Proof

Swapping two adjacent coordinates changes a cyclic window set only when
the window contains exactly one of the two coordinates.  At a fixed proper
window length there are exactly two such positional windows.  Therefore
one adjacent swap changes the row incidence vector by half-\(L^1\) distance
at most two, and the triangle inequality gives

\[
 {1\over2}\|z_{q,P}^G-z_{q,P}^F\|_1\le2d(P).           \tag{4.6}
\]

Use the componentwise form (3.6):

\[
 \|\delta_{q,K}\|_2^2
 \le2b_Kr_{q,K}
 \le4b_K\sum_{P\in K}d(P).
\]

Sum with the weights \(w_q\).  This proves (4.4), and (4.5) follows by
\(b_K\le b(F,G)\). \(\square\)

## 5. Floor-corrected consequences

Let

\[
 \lambda_q={W_s\over|\mathcal X_q|},\qquad
 c_q=\lfloor\lambda_q\rfloor,
\]

and use the standard weights \(w_q=1/c_q\).  Let \(f^F,f^G\) be the
centered complete load vectors, and let \(B_H\) be the exact integer-floor
baseline.  Write

\[
 \mathcal Q_H(F)=\|f^F\|_H^2-B_H,
\]

and define the midpoint floor defect

\[
 \mathfrak M_H(F,G)
   =\left\|{f^F+f^G\over2}\right\|_H^2-B_H.             \tag{5.1}
\]

The quantity in (5.1) need not be nonnegative, because the midpoint need
not be integral.

Combining the audited two-seed component identity with Theorem 3.1 gives
the following statement; no heat identity is reproved here.

### Theorem 5.1 (one-shot non-relabeling rounding theorem)

Some exact component-side child \(F_*\) of \(F,G\) satisfies

\[
 \boxed{
 \mathcal Q_H(F_*)
 \le \mathfrak M_H(F,G)+{b(F,G)\over2}L_H(F,G).}        \tag{5.2}
\]

Under the consecutive-block hypothesis of Corollary 4.2,

\[
 \boxed{
 \mathcal Q_H(F_*)
 \le \mathfrak M_H(F,G)
      +b(F,G)(k-1)C_s\Omega_H.}                         \tag{5.3}
\]

#### Proof

The exact fair-component formula is

\[
 \mathbb E\mathcal Q_H(F_\varepsilon)
       =\mathfrak M_H(F,G)+\frac14V_H(F,G).
\]

Theorem 3.1 bounds the last term by \(bL_H/2\).  At least one integral
component child is no worse than the expectation.  Corollary 4.2 gives
(5.3). \(\square\)

There is also a genuine local-minimum/contraction form.  Put

\[
                         A_H(F,G)=\|f^G-f^F\|_H^2.
\]

### Theorem 5.2 (sparse-comparator contraction)

Suppose \(G\) is an arbitrary exact \(\mathcal D_s\)-port factor such
that

\[
 \mathcal Q_H(G)\le\mathcal Q_H(F),\qquad
 A_H(F,G)\ge\eta\mathcal Q_H(F)                         \tag{5.4}
\]

for some \(\eta>0\).  Then one exact component child obeys

\[
 \boxed{
 \mathcal Q_H(F_*)
 \le\left(1-\frac\eta4\right)\mathcal Q_H(F)
       +{b(F,G)\over2}L_H(F,G).}                        \tag{5.5}
\]

In particular, suppose that every exact factor \(F\) admits such a
comparator with fixed \(\eta>0\), and uniformly

\[
                         b(F,G)L_H(F,G)\le R_s.          \tag{5.6}
\]

Then some exact factor satisfies

\[
                         \boxed{\mathcal Q_H\le {2R_s\over\eta}.}       \tag{5.7}
\]

Under the rootwise \(k\)-block hypothesis and \(b(F,G)\le b\), this is

\[
 \boxed{
 \mathcal Q_H\le {4b(k-1)C_s\Omega_H\over\eta}.}       \tag{5.8}
\]

#### Proof

The audited two-seed drift formula and (5.4) give

\[
 \mathbb E\mathcal Q_H(F_\varepsilon)
 \le \mathcal Q_H(F)-\frac14A_H(F,G)+\frac14V_H(F,G).
\]

Apply (3.5), then choose one child no worse than the expectation.  This is
(5.5).  If \(\mathcal Q_H(F)>2R_s/\eta\), (5.5) gives a strict descent.
Minimizing over the finite exact-factor fibre, or iterating strict descent,
proves (5.7).  Equation (5.8) follows from (4.2). \(\square\)

Neither theorem uses equality of endpoint energies, a group average, or a
coordinate relabelling.  Their price is explicit: counterbias in (5.2), or
coherent separation by a no-higher-energy comparator in (5.4).

## 5A. The midpoint and cube-orientation obstructions

The variance estimates do not remove the other half of the two-seed gate.
There are two exact reasons.  Let

\[
 a={f^F+f^G\over2},\qquad
 U=\operatorname {span}\{\delta_K:K\text{ an ownership component}\}.
\]

Every component-cube vertex has the form

\[
                         f_\varepsilon
      =a+{1\over2}\sum_K\varepsilon_K\delta_K.          \tag{5A.1}
\]

### Proposition 5A.1 (immovable midpoint projection)

For every genuine component child,

\[
 P_{U^\perp}f_\varepsilon=P_{U^\perp}a,                \tag{5A.2}
\]

and hence

\[
 \boxed{
 \mathcal Q_H(F_\varepsilon)
 \ge\|P_{U^\perp}a\|_H^2-B_H.}                         \tag{5A.3}
\]

Consequently a necessary condition for this fixed cube to contain a child
with \(\mathcal Q_H=o(W_s)\) is

\[
                         \|P_{U^\perp}a\|_H^2
                         \le B_H+o(W_s).                \tag{5A.4}
\]

#### Proof

The displacement in (5A.1) belongs to \(U\), proving (5A.2).  Orthogonal
Pythagoras gives

\[
 \|f_\varepsilon\|_H^2
 \ge\|P_{U^\perp}a\|_H^2.
\]

Subtract the factor-independent floor baseline. \(\square\)

Thus even arbitrarily small components and arbitrarily small variance do
not move a common bias perpendicular to their signed effects.  Full
midpoint counterbias in Theorem 5.1 is a convenient sufficient condition;
(5A.4) is the weaker unavoidable condition for an optimally correlated
signing.

There is also a general orientation no-go which does not use a relabelling
symmetry.  Put

\[
 \overline{\mathcal Q}_{\rm cube}
   =2^{-r}\sum_{\varepsilon\in\{\pm1\}^r}
                         \mathcal Q_H(F_\varepsilon),    \tag{5A.5}
\]

where \(r\) is the number of components.

### Proposition 5A.2 (exact two-seed cube-orientation no-go)

For the genuine component cube,

\[
 \boxed{
 \overline{\mathcal Q}_{\rm cube}
 =\|a\|_H^2-B_H+{1\over4}\sum_K\|\delta_K\|_H^2.}     \tag{5A.6}
\]

Fairly resampling all components from any oriented corner has expected
value (5A.6).  Therefore its drift at the corner \(\varepsilon\) is

\[
              \overline{\mathcal Q}_{\rm cube}
                         -\mathcal Q_H(F_\varepsilon),   \tag{5A.7}
\]

whose average over all orientations is zero.  Unless the energy is
constant on the cube, some genuine orientations have positive drift and
some have negative drift.  At a minimum-energy cube corner, neither fair
resampling nor selection of its better antipodal mate gives a strict
descent.

In particular, component sizes, root edit distances, and all other data
unchanged by reorienting the same cube cannot by themselves imply descent
from every corner.

#### Proof

Average (5A.1) over independent uniform signs.  All linear and mixed terms
vanish, while each diagonal term contributes
\(\|\delta_K\|_H^2/4\).  This proves (5A.6), and fair resampling chooses
the uniform cube law independently of the starting orientation.  Equation
(5A.7) follows.

Its average is zero by definition.  If it is not identically zero, it must
have both signs.  At a cube minimum every other corner, including the
antipode, has no smaller energy. \(\square\)

This proposition is the non-relabeling analogue of the earlier
transposition-cube orientation obstruction.  It does not refute the
local-minimum strategy in Theorem 5.2: that strategy is allowed to choose
a new comparator cube at the current factor.  It proves that a fixed
growing seed pair, together with unsigned component control, is not a
universal descent mechanism.  One must prove counterbias, signed coherent
separation, or that every minimum of every relevant cube is already at the
desired floor.

## 6. Exact Gaussian-window accounting

Fix \(A>0\) and put

\[
                         H=\lceil A\sqrt s\rceil.
\]

For all sufficiently large \(s\), \(H\le s-1\).  Since \(c_q\ge1\),

\[
                         \Omega_H\le H.                 \tag{6.1}
\]

The consecutive-edit residue in (5.3) has exact ratio

\[
 {b(k-1)C_s\Omega_H\over W_s}
 \le {b(k-1)H\over2s+1}
 =\left({A\over2}+o_A(1)\right){b(k-1)\over\sqrt s}.    \tag{6.2}
\]

Hence:

1. If \(b(k-1)=O_A(1)\), the residue is
   \(O_A(HC_s)=O_A(W_s/\sqrt s)\).
2. If \(b(k-1)=o(\sqrt s)\), the residue is \(o(W_s)\).
3. In the general edit-budget form, the exact requirement is
   \(bL_H=o(W_s)\).

Therefore Theorem 5.1 gives the audited fixed-window overload conclusion
whenever

\[
 \mathfrak M_H(F,G)=o(W_s),\qquad bL_H=o(W_s),           \tag{6.3}
\]

and Theorem 5.2 gives it whenever its comparator hypotheses hold with
\(R_s=o(W_s)\).  With bounded \(b,k\), the stronger Catalan-floor scale
\(O_A(HC_s)\) follows.  Since

\[
 {HC_s\over W_s}={H\over2s+1}=O_A(s^{-1/2}),            \tag{6.4}
\]

both conclusions are genuinely \(o(W_s)\), with no suppressed factor of
\(s\).

## 7. What the old no-gos leave, exactly

The prior bounded-seed and component-expansion results fit the new theorem
without contradiction.

### 7.1 Strict interior bounded packets

The dense first-fringe \(\mathcal D_4\) packets have bounded ownership
blocks and bounded local edits before an outer embedding.  If an embedding
places the changed coordinates in a bounded consecutive slab, (4.3) also
controls their complete physical variance.  For a general embedding this
must be checked from \(L_H\); bounded abstract seed size alone does not
control the collars.  Independently of that issue, the protected
two-endpoint target contains both local complementary ports, so its value
is independent of the local shore.  In the charged direction their
coherent separation is zero.  Thus even a favorable variance audit would
not supply the midpoint/comparator hypothesis.

### 7.2 Literal growing-skeleton transport

For a fixed shape-respecting port interface, usable growing Catalan
skeleton packets cover only \(o(C_s)\) roots.  Such packets cannot supply a
root-scale counterbiased pair.  This says nothing against a genuinely new
\(\mathcal D_s\)-port factor whose complete \(X/Y\) ledgers are proved
directly.

### 7.3 A genuinely growing factor

A new growing factor removes the coverage objection, but Theorem 2.1 adds
an ownership objection.  If its comparison phase maps generate a large
orbit, then \(b\) is at least that orbit size; if they are transitive, no
new component child exists at all.  If the entire growing block is
reordered, Lemma 4.1 must be used with \(k=\Theta(s)\), not with the size of
some bounded seed hidden inside it.

Thus exactness and growth alone imply none of (6.3).  The surviving
construction cannot be described merely as “find a non-MSW growing seed.”

### Constructive lemma left by this audit

For every fixed \(A>0\), construct, for all sufficiently large \(s\), two
exact \(\mathcal D_s\)-port factors \(F_s,G_s\) satisfying

\[
 \boxed{
 \begin{aligned}
 &\mathfrak M_{H_s}(F_s,G_s)=o(W_s),\\
 &b(F_s,G_s)L_{H_s}(F_s,G_s)=o(W_s),\\
 &H_s=\lceil A\sqrt s\rceil,
 \end{aligned}}                                        \tag{7.1}
\]

where \(L_{H_s}\) is computed from the complete physical cyclic profiles,
including all carrier and collar windows.  A checkable stronger version is

\[
 \boxed{
 \begin{aligned}
 &b(F_s,G_s)k_s=o(\sqrt s),\\
 &\text{every root-matched row pair differs inside a cyclic block of}\\
 &\qquad\text{at most }k_s\text{ positions},\\
 &\mathfrak M_{H_s}(F_s,G_s)=o(W_s).
 \end{aligned}}                                        \tag{7.2}
\]

Then Theorem 5.1 produces one literal exact factor with
\(\mathcal Q_{H_s}=o(W_s)\).  Alternatively, prove the comparator version:
for every factor above the desired floor, find \(G_s\) satisfying (5.4)
with \(bL_H=o(W_s)\); Theorem 5.2 then gives the same conclusion.

The ownership part of (7.1) is not generic pseudorandomness.  It requires
a common small block system for all root-owner relations.  The target part
is not a marked first-insertion transfer.  It requires counterbias or
coherent separation in the full weighted depth vector.  These are the two
exact, nonredundant requirements.

## 8. Proved/conditional boundary

### Proved

1. The exact root-contracted owner graph for two arbitrary growing port
   factors (Theorem 1.1).
2. The common-phase orbit obstruction and the connected-overlay no-go
   (Theorem 2.1).
3. The non-relabeling sparse variance estimate \(V_H\le2bL_H\)
   (Theorem 3.1).
4. The full crossing-collar bound for a consecutive row edit
   (Lemma 4.1 and Corollary 4.2), and the component-weighted adjacent-edit
   bound (Corollary 4.3).
5. The one-shot floor-corrected rounding theorem and the sparse-comparator
   contraction theorem, with exact residues (Theorems 5.1--5.2).
6. The immovable-midpoint projection and the non-relabeling cube-orientation
   no-go (Propositions 5A.1--5A.2).
7. The explicit sufficient growing regime \(bk=o(\sqrt s)\) at
   \(H=A\sqrt s\), and the stronger \(O_A(HC_s)\) residue for bounded
   \(b,k\).

### Not proved

1. No pair satisfying (7.1) or (7.2) is presently constructed.
2. No arbitrary growing port factor is asserted to have small ownership
   components or sparse complete row edits.
3. A root-scale first-insertion menu does not imply midpoint counterbias in
   the full depth vector.
4. The theorem does not turn strict-interior \(\mathcal D_4\) fringe
   packets into boundary-active packets.

The heat lane therefore survives, but only as the precise growing
small-block/sparse-profile lemma (7.1), not as a consequence of replacing
MSW by an unspecified growing seed.
