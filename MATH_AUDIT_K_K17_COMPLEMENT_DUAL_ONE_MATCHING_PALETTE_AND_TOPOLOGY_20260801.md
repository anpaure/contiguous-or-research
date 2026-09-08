# Audit: the `k=17` complement-dual one-matching face

## Scope

This note audits the proposed restriction

\[
                 H=C D^{-1}C                                      \tag{0.1}
\]

in the actual voltage-labelled `Z_17` incidence quotient between rank-9
owner necklaces and rank-8 facet necklaces.  Here `D` and `H` are both
viewed as owner-to-facet perfect matchings; an oriented factor follows a
`D` edge and then an inverse `H` edge.  This convention matters.

The palette claim is correct: after imposing $D\cap H=\varnothing$, the
rank-7 turn at the complementary owner is literally the complement of the
rank-10 turn at the original facet, occurrence by occurrence.  There is,
however, an intrinsic topology obstruction: an exactly complement-dual
factor cannot be a single quotient cycle because the owner successor is a
square permutation on the even set of 1,430 owner orbits.  Thus this is a
valid palette-exact cycle-cover subclass, but a connected carrier requires
a subsequent move leaving the exact complement-dual face.

## 1. Complement on the gauged incidence quotient

Let `rho` be cyclic coordinate rotation, let `T_O` be the fixed rank-9
representative of owner orbit `O`, and let `Q_F` be the fixed rank-8
representative of facet orbit `F`.  Write

\[
 \begin{aligned}
 C T_O&=\rho^{u_O}Q_{c_9(O)},\\
 C Q_F&=\rho^{v_F}T_{c_8(F)} .                         \tag{1.1}
 \end{aligned}
\]

The maps `c_9` and `c_8` are inverse bijections between the two quotient
shores, and freeness of the nontrivial `Z_17` subset orbits gives

\[
       v_{c_9(O)}=-u_O,\qquad u_{c_8(F)}=-v_F\pmod {17}.             \tag{1.2}
\]

An incidence is

\[
              e=(O,F,s),\qquad \rho^sQ_F\subset T_O.                \tag{1.3}
\]

### Lemma 1.1 (exact dual-incidence gauge)

Complement induces the incidence involution

\[
 j(O,F,s)=
 \bigl(c_8(F),c_9(O),u_O-s-v_F\bigr).                              \tag{1.4}
\]

#### Proof

Complementing (1.3) gives

\[
 \rho^{u_O}Q_{c_9(O)}
       \subset \rho^{s+v_F}T_{c_8(F)}.
\]

Rotate the entire incidence by `-(s+v_F)` to put its owner at the chosen
representative.  The resulting facet shift is `u_O-s-v_F`, proving
(1.4).  Equations (1.2) then give $j^2(e)=e$.  \(\square\)

In the repository's canonical-mask notation, if

\[
 C Q_F=\rho^aT_{c_8(F)},\qquad C T_O=\rho^bQ_{c_9(O)},
\]

then the dual shift is exactly `b-s-a`.  This is the convention used in
`scratch/build_k17_age_complement_dual_matching_master_20260801.cpp`.

### Lemma 1.2 (no self-dual incidence orbit)

The 12,870 quotient incidences split into 6,435 two-element `j`-orbits;
there is no fixed incidence.

#### Proof

A physical incidence has one distinguished coordinate, namely the unique
element of `T-Q`.  If its incidence orbit were fixed by complement, some
rotation would carry its complemented incidence back to itself and hence
fix this distinguished coordinate.  A nonidentity rotation of 17
coordinates fixes no coordinate, so that rotation must be the identity.
It would then require $Q=CT$, impossible because $Q\subset T$ and both
$Q$ and $CT$ have size eight.  \(\square\)

## 2. One matching produces the second matching

Let `D` be a perfect matching in the quotient incidence multigraph and
also denote by `D` its translation-equivariant physical lift.  Define

\[
                         H=j(D)=C D^{-1}C.                         \tag{2.1}
\]

Because `j` swaps and bijects the two incidence shores, `H` is again a
perfect matching.

Let $d:\mathcal O_9\to\mathcal O_8$ be the underlying orbit bijection of
`D`, and put

\[
                         A=c_8\circ d                              \tag{2.2}
\]

on the owner orbits.  Then

\[
               d=c_9A,\qquad h=c_9A^{-1},                         \tag{2.3}
\]

where `h` is the underlying owner-to-facet bijection of `H`.

### Lemma 2.1 (edge-disjointness in the multigraph)

The following are equivalent.

1. $D\cap H=\varnothing$.
2. No complementary pair `{e,j(e)}` has both members in `D`.
3. For every owner `O` with `A^2O=O`, the two **labelled** quotient
   incidences `D(O)` and `H(O)` are different.

In particular, it is sufficient, but not necessary, that `A` have no
cycle of length one or two.

#### Proof

At owner `O`, equations (2.3) give the underlying facet orbits

\[
          D(O)=c_9(AO),\qquad H(O)=c_9(A^{-1}O).
\]

Thus equality of the labelled edges can occur only when `A^2O=O`; in that
case it occurs exactly when the two parallel-incidence labels also agree.
By definition, `H(O)` is the dual of the `D` edge selected at the other
endpoint, so this is exactly simultaneous selection of `e` and `j(e)` in
`D`.  \(\square\)

For a phase-labelled version, let the equivariant physical permutation
`A=CD` send `(O,g)` to `(AO,g+a_O)`.  Then

\[
 D(O)=H(O)\quad\Longleftrightarrow\quad
 A^2O=O\ \hbox{ and }\ a_O+a_{AO}=0\pmod {17}.                    \tag{2.4}
\]

For a fixed point of `A`, (2.4) would say `2a_O=0`, hence `a_O=0`; this
would be a self-dual incidence and is excluded by Lemma 1.2.  On a
two-cycle of `A`, overlap occurs exactly when that two-cycle has zero
total voltage.  This is why retaining parallel incidence labels is
essential: an `A` one- or two-cycle can still give two distinct factor
edges.

Thus an exact one-matching master needs the clauses
`not(D_e and D_j(e))` for the 6,435 dual pairs.  These clauses are not
optional: without them the purported rank-10 and rank-7 turns can collapse
to ranks nine and eight.

## 3. Occurrencewise rank-7/rank-10 complementarity

Fix a physical rank-8 facet `F` and put

\[
               X=D^{-1}(F),\qquad Y=H^{-1}(F).                     \tag{3.1}
\]

Under edge-disjointness, `X` and `Y` are distinct rank-9 one-element
extensions of `F`.  Hence

\[
        X\cap Y=F,\qquad U_F=X\cup Y\quad\hbox{has rank ten}.       \tag{3.2}
\]

Inverting (2.1) also gives `D=C H^{-1}C`.  Therefore at the complementary
rank-9 owner `CF`,

\[
        D(CF)=CY,\qquad H(CF)=CX.                                  \tag{3.3}
\]

Consequently

\[
 \begin{aligned}
 D(CF)\cap H(CF)&=CY\cap CX=C(X\cup Y)=CU_F,\\
 D(CF)\cup H(CF)&=CY\cup CX=C(X\cap Y)=CF.             \tag{3.4}
 \end{aligned}
\]

The second line is the proposed identity

\[
 C\bigl(D^{-1}(F)\cap H^{-1}(F)\bigr)=D(CF)\cup H(CF),             \tag{3.5}
\]

while the first line is the identity that directly compares the turn
palettes.  The map $F\mapsto CF$ bijects physical occurrences and commutes
with `rho`.  Therefore the complete rank-7 load vector is the complemented
rank-10 load vector, including multiplicities.  In particular, rank-10
orbit surjectivity implies rank-7 orbit surjectivity automatically.  This
does not imply any deeper rank row.

## 4. The square-permutation topology obstruction

With both matchings written owner-to-facet, the oriented owner successor
is

\[
            \pi=h^{-1}d=A^2.                                      \tag{4.1}
\]

### Theorem 4.1 (exact complement duality is never connected at `k=17`)

No edge-disjoint complement-dual factor `D union C D^{-1}C` is a single
cycle on the 1,430 quotient owner orbits.

More precisely, an `A`-cycle of odd length contributes one `pi`-cycle,
whereas an `A`-cycle of even length contributes two `pi`-cycles.  Hence

\[
 c(\pi)=\#\{\hbox{odd }A\hbox{-cycles}\}
          +2\#\{\hbox{even }A\hbox{-cycles}\}.                    \tag{4.2}
\]

This number is positive and even.

#### Proof

Equation (4.1) follows at once from (2.3).  Squaring an odd cycle remains
one cycle, while squaring an even cycle splits its two parity classes.
Because the sum of the `A`-cycle lengths is the even number 1,430, the
number of odd `A`-cycles is even.  In particular `A^2` cannot be one
1,430-cycle.  \(\square\)

This obstruction is independent of incidence geometry, rank-10 rows,
voltage, and the age word.  A connected-subtour separator applied while
preserving exact complement duality must eventually reject every model.
Such an UNSAT result would close only this sufficient subclass, not the
unrestricted two-matching master.

The sharp near-connected target inside the dual face is two quotient
cycles.  A later non-dual alternating connector may merge them, but that
connector must separately preserve or repair the paired rank-7/rank-10
palette identity.

## 5. Voltage in the complement-dual face

Suppose the selected `D` incidence at owner `O` is `(O,d(O),s_O)`.  The
physical permutation `A=CD` has phase increment

\[
              a_O=s_O+v_{d(O)}\pmod {17}.                           \tag{5.1}
\]

Following the factor from `O` to `A^2O` has incidence-dart voltage

\[
                         a_O+a_{AO}.                               \tag{5.2}
\]

For an odd `A`-cycle, the sole `A^2` component has voltage
`2 sum_O a_O`.  For an even `A`-cycle, its two `A^2` components have the
same voltage `sum_O a_O`.  Thus a single even `A`-cycle with nonzero total
voltage lifts to exactly two physical cycles of length `715*17=12,155`
each, not one physical cycle of length 24,310.

#### Proof

From (1.1), `CD` sends `(O,g)` to `(AO,g+a_O)`.  The factor successor is
its square, proving (5.2).  Summing over the parity classes of an `A`-cycle
gives the stated formulas.  \(\square\)

## 6. Audited boundary

The complement-dual one-matching restriction rigorously removes the
coupled immediate palette row:

* choose one quotient perfect matching `D`;
* forbid the 6,435 dual-pair double selections;
* set `H=j(D)` with the shift rule (1.4);
* enforce rank-10 surjection only;
* obtain rank-7 surjection, with exactly complementary occurrence loads.

What it does **not** provide is a connected quotient or physical owner
cycle.  The correct engine scope is therefore “palette-exact cycle-cover
seed, followed by an explicitly non-dual connector,” not “a smaller exact
Hamilton master.”  Residence, deletion-spine feasibility, deeper upper
opening, and the free-type exact-mass companion remain independent gates.

## 7. Exact two-cycle exit condition

Assume now that `A` is one 1,430-cycle.  The dual factor then consists of
exactly the two parity cycles of `A`; by Section 5 they have the same
quotient voltage

\[
                         V_0=\sum_O a_O.                            \tag{7.1}
\]

Thus `V_0!=0` makes each parity cycle lift to one physical cycle of length
12,155.  This is the sharp connectedness obtainable without leaving the
dual face.

There is a precise minimal way to leave that face.  Retain `D`.  Choose
two `H` edges

\[
                pF=H(p),\qquad qG=H(q),                            \tag{7.2}
\]

one on each parity cycle.  Suppose the cross incidences `pG` and `qF`
exist (with specified quotient shifts), neither is a `D` edge, and replace

\[
                    \{pF,qG\}\quad\hbox{by}\quad\{pG,qF\}.         \tag{7.3}
\]

### Theorem 7.1 (non-dual rectangle connector)

The switch (7.3) produces a connected quotient factor.  Conversely, any
two-edge change of `H` that preserves its perfect-matching rows and joins
the two quotient cycles has this cross-rectangle form.

If the old `H` incidence shifts are `h_p,h_q` and the new cross-edge
shifts are `h'_p,h'_q`, the joined cycle has voltage

\[
             V'=2V_0+h_p+h_q-h'_p-h'_q\pmod {17}.                  \tag{7.4}
\]

It lifts to one physical owner cycle exactly when `V'!=0`.

#### Proof

Deleting one edge from each alternating cycle leaves two paths.  The
crossed reconnection in (7.3) joins the two paths into one alternating
cycle.  A two-edge perfect-matching exchange has to preserve the two owner
degrees and two facet degrees, so the crossed reconnection is its only
nontrivial form.  Around a complete oriented quotient cycle, voltage is
the sum of the `D` incidence shifts minus the sum of the `H` incidence
shifts.  Before the switch the two cycle voltages sum to `2V_0`; replacing
the two displayed shifts gives (7.4).  \(\square\)

### Exact palette ledger

Only four turn occurrences change.  At facets `F,G`, let the old and new
rank-10 labels be

\[
 \begin{array}{ll}
 U_F=D^{-1}(F)\cup p, &U'_F=D^{-1}(F)\cup q,\\
 U_G=D^{-1}(G)\cup q, &U'_G=D^{-1}(G)\cup p,
 \end{array}                                                     \tag{7.5}
\]

where every owner is understood in the physical alignment supplied by
its stated incidence.  At owners `p,q`, let

\[
 \begin{array}{ll}
 L_p=D(p)\cap F, &L'_p=D(p)\cap G,\\
 L_q=D(q)\cap G, &L'_q=D(q)\cap F,
 \end{array}                                                     \tag{7.6}
\]

again in the corresponding owner gauges.  No other immediate turn label
changes.

For `r in {7,10}`, write `mu_r(Z)` for the old multiplicity of target
orbit `Z`, and write `m_r^-(Z),m_r^+(Z)` for its multiplicity in the two
old and two new labels in (7.5) or (7.6).  Then the switch preserves both
palette surjections if and only if

\[
        \mu_r(Z)-m_r^-(Z)+m_r^+(Z)\ge1
        \quad\hbox{for every target }Z\hbox{ and }r=7,10.           \tag{7.7}
\]

Equation (7.7), together with incidence existence and (7.4), is the exact
finite connector test.  Exact multiset preservation is the stronger
special case

\[
 \{U_F,U_G\}=\{U'_F,U'_G\},\qquad
 \{L_p,L_q\}=\{L'_p,L'_q\}.                                      \tag{7.8}
\]

Because a surjective immediate palette has 1,430 occurrences on 1,144
target orbits, each shore has exactly

\[
                     1430-1144=286                                \tag{7.9}
\]

spare occurrence units.  Complement duality identifies the two old load
vectors under target complement.  Hence a useful sufficient version of
(7.7) is that the two deleted labels on each shore consume no more than
the available spare multiplicity `mu_r(Z)-1` of every target `Z`.
Repeated occurrences are therefore an exact connector reserve, not merely
a scalar heuristic.  The number 286 alone does **not** prove that a legal
cross rectangle hits four spare tokens; this is the remaining coloured
incidence question.  If a deleted unique label is recreated among the new
labels, (7.7) allows it without spending a repeat unit.

There is a useful one-palette formulation of the deletion test.  In the
old dual factor,

\[
                  L_p=C U_{Cp},\qquad L_q=C U_{Cq}.                \tag{7.10}
\]

Therefore a simple sufficient connector certificate is a cross rectangle
for which the four old rank-10 occurrences indexed by

\[
                           F, G, Cp, Cq                          \tag{7.11}
\]

all lie within their target's spare multiplicity (counting coincidences
with multiplicity), and for which (7.4) is nonzero.  Then both old labels
removed on both shores are dispensable, so arbitrary legal new labels
preserve surjectivity.  The more general test (7.7) can still pass when
one of these four occurrences is unique, provided the switch recreates
its target.

The same ledger applies to a longer non-dual alternating circuit: replace
the two-element old/new multisets in (7.7) by all turn labels changed by
that circuit.  Residence, deletion-spine, and deep-opening guards must
still be audited on the resulting connected order.

## 8. Engine consequence

The incidence involution implemented in
`scratch/build_k17_age_complement_dual_matching_master_20260801.cpp` has
the correct canonical-gauge shift `b-s-a`.  Its perfect-`D`, dual-support,
dual-pair exclusion, and eager rank-10 rows encode exactly the palette face
proved above.

The correct topology pipeline for that file is not the unrestricted
factor connectedness separator.  It is:

1. use the selected `D` edges to form `A=c_8d` and impose that `A` is one
   1,430-cycle by lazy cuts on the `D` variables;
2. require the total `A` voltage `V_0` to be nonzero;
3. materialize the two parity components of `A^2`;
4. find a non-dual rectangle or longer alternating circuit satisfying
   (7.4) and (7.7);
5. only then run residence, deletion-spine, free-type, and upper-opening
   replay on the connected result.

Running the ordinary connected-subtour CEGAR directly on
`D union j(D)` can only end in subclass-UNSAT by Theorem 4.1.  It must not
be reported as evidence against the unrestricted two-matching model.
