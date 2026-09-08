# Audit of the clean-H three-primary and period-three transition theorem

Date: 2026-07-31  
Lane: R, Hamilton-compatible quotient transition systems  
Audited files:

- `MATH_THEOREM_CATALAN_THREE_PRIMARY_QUOTIENT_REDUCTION_20260731.md`;
- `MATH_THEOREM_CATALAN_PERIOD3_FILTER_RECURSION_20260731.md`;
- `MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md`;
- `MATH_REDUCTION_GLOBAL_QUOTIENT_MATCHING_PHYSICAL_FOREST_SOCKET_VOLTAGE_20260731.md`;
- `MATH_THEOREM_K16_THREE_PRIMARY_SPIRAL_BRAID_ANATOMY_20260731.md`;
- `MATH_THEOREM_R_CYCLIC_QUOTIENT_PORT_VOLTAGE_AND_M4_BINARY_CORE_20260731.md`.

## 0. Verdict

The clean cyclic reduction is valid.  For

\[
 q=2m-1,\qquad s=3^{v_3(q)},\qquad h=q/s,\qquad
 H=\langle s\rangle\cong\mathbb Z_h,
\]

the correct topology object is the occurrence-labelled skew permutation

\[
                         T(x,g)=(\tau(x),g+\delta_x).
\]

For every cycle \(C\) of \(\tau\), put
\(V_C=\sum_{x\in C}\delta_x\pmod h\).  The exact physical component count
is

\[
                         c(F)=\sum_C\gcd(h,V_C).
\]

Thus all balanced-fragment subtours collapse exactly to

\[
 \tau\text{ one occurrence cycle},\qquad
 \gcd\!\left(h,\sum_x\delta_x\right)=1.
\]

This statement requires free \(H\)-action, an invariant saturating
one-in/one-out transition, and literal physical injectivity.  It controls
topology only; palette, deeper-shadow, residence and compiler guards remain
separate literal hypotheses.

The period-three theorem correctly identifies the two
\(\operatorname{Cat}_a\)-indexed exceptional colour banks and proves the
universal lower bound \(2\operatorname{Cat}_a\) on partially occupied full
rotation edge orbits.  Its new Theorem 3 attains this bound when
\(v_3(q)=1\) by a complement-paired, middle-endpoint-disjoint clean-\(H\)
provider bank at the local exceptional-bank level.  Its Corollary 2.1
further proves the global lower bound \(2\operatorname{Cat}_a+1\) when
\(3\nmid\operatorname{Cat}_a\), so the local sharpness statement is not a
claim about the whole matching.

The matching-first theorem removes the provider-extension quantifier.  The
clean quotient of the complete diamond graph is balanced regular, hence it
has a perfect matching; restricting the lift chooses every exceptional
provider inside an already global matching.  This guarantees the two
adjacent palettes and pairwise-distinct filter middle endpoints, but not a
linear middle forest, protected sockets, guards, or unit voltage.  Those are
the exact remaining gates.

## 1. Clean-H arithmetic and freeness

The identity

\[
 (m^2-1)\operatorname{Cat}_m
   =2(2m-1)\binom{2m-2}{m-2}
\]

and \(\gcd(2m-1,m^2-1)=\gcd(2m-1,3)\) prove
\(h\mid\operatorname{Cat}_m\).  The action of \(H\) on ranks
\(m-1,m,m+1\) is free.  When \(3\mid q\), the full rotation action has
order-three outer-rank stabilizers, and a free full edge orbit meets their
colour orbit three-to-one.  Therefore a fully \(\mathbb Z_q\)-invariant
exact lower-rainbow edge set is impossible.

The rank-set theorem does not directly assert path-component freeness, but
the needed implication is valid: a setwise path stabilizer acts through an
automorphism group of order at most two; since \(|H|\) is odd, it fixes the
path pointwise, and vertex freeness makes the stabilizer trivial.

## 2. Exact sector criterion

An explicit sector partition is additional data, not a consequence of
mere \(H\)-invariance.  If

\[
 {\cal Q}=\bigsqcup_{a\in S}{\cal Q}_a,\qquad
 \tau({\cal Q}_a)={\cal Q}_{\pi(a)},
\]

then for a cycle \(A\) of \(\pi\), the return permutation

\[
 R_A=\tau^{|A|}\big|_{{\cal Q}_a}
\]

is defined on one sector in \(A\).  Its cycles are in bijection with the
cycles of \(\tau\) above \(A\).  If \(V_{A,D}\) is the full clean-\(H\)
voltage associated with a return cycle \(D\), then

\[
 c(F)=\sum_{A\in{\cal C}(\pi)}
          \sum_{D\in{\cal C}(R_A)}\gcd(h,V_{A,D}).
\]

Hence sector connectedness alone is insufficient.  Hamiltonicity requires
one sector cycle, one return-map cycle, and primitive full-return voltage.
After each sector is first compressed to one protected macro path, this
reduces to a cyclic ordering of the sector macros plus unit total voltage.

Residual symmetry must break somewhere in the complete exact lower-rainbow
selection when \(3\mid q\).  It need not break in the bridge family itself:
a residual-invariant bridge orbit is compatible with the theorem when the
internal forest or repair choices already break residual symmetry.

## 3. Exact period-three clean-H rows

Write \(q=6a+3\) and

\[
 {\cal N}_a=\binom{\mathbb Z_{2a+1}}a/\mathbb Z_{2a+1},\qquad
 |{\cal N}_a|=\operatorname{Cat}_a.
\]

The shortened lower and upper full-rotation colour orbits form two copies
of \({\cal N}_a\).  One such colour orbit has size

\[
                         q/3=(s/3)h
\]

and therefore splits into \(s/3\) free \(H\)-colour orbits.  A free full
edge orbit splits into \(s\) free \(H\)-edge orbits, exactly three over each
exceptional \(H\)-colour orbit.  Consequently the clean quotient contains

\[
 |{\cal X}^-|=|{\cal X}^+|
   =(s/3)\operatorname{Cat}_a
\]

exceptional service rows.  After fixing one contributing full edge orbit,
an \(H\)-invariant section is a phase function

\[
                         \phi:\mathbb Z_{s/3}\to\mathbb Z_3.
\]

Only for \(v_3(q)=1\) is this one scalar choice among three phase orbits.
There are exactly \(3^{s/3}\) such \(H\)-invariant phase words in one fixed
provider orbit, and the free residual \(\mathbb Z_s\)-action leaves
\(3^{s/3}/s\) cyclic classes.  Without \(H\)-invariance there are
\(3^{q/3}\) arbitrary physical sections.

Complementation pairs the lower and upper row indices, but it supplies no
common edge, port, phase, transition or voltage.  Indeed the two provider
families are disjoint because a shortened lower colour contains \(\infty\)
and a shortened upper colour does not.

For the global toll, put \(C=\operatorname{Cat}_a\),
\(E=(q/3)C\), and \(R=\binom{2m}{m-1}\).  The nonexceptional lower colours
form free full-rotation orbits, hence \(q\mid R-E\).  Equality in the
exceptional \(2C\) floor would leave \(R-2E\) selected edges in full orbits,
so \(q\mid R-2E\).  Subtracting forces \(q\mid E\), equivalent to
\(3\mid C\).  This proves Corollary 2.1 and also shows that the extra
partial orbit must be nonexceptional when \(3\nmid C\).

## 4. Audit of the source theorem's scope

The current corrected source has the following exact boundary.

1. Theorem 2 proves
   \[
      \#\{\text{partial full edge orbits}\}
        \ge 2\operatorname{Cat}_a.
   \]
   Theorem 3 constructs equality when \(v_3(q)=1\), for the local
   exceptional-bank contribution at the palette and
   middle-endpoint-matching level.  Corollary 2.1 shows that
   when \(3\nmid\operatorname{Cat}_a\), a complete two-sided-rainbow edge set
   nevertheless needs at least one additional partial orbit whose two colour
   orbits are nonexceptional.  General attainability at higher 3-adic order,
   with compatible phase words, is not proved.
2. Section 3 now correctly distinguishes \(3^{q/3}\) unrestricted physical
   sections from \(3^{s/3}\) \(H\)-invariant phase words.  A constant
   one-of-three phase occurs only when \(s=3\).
3. At higher 3-adic order the period-three note's exact unconditional object is
   \(s/3\) ternary positions per necklace.  The residual action and section
   counts are proved.  After the matching-first theorem, a globally
   extendable, middle-disjoint provider restriction is obtained by choosing
   the quotient perfect matching first; a prescribed complement-paired
   phase word still need not extend, and no spanning path construction is
   thereby proved.

Theorem 3 itself is valid.  For each necklace representative \(A\), its
edge \(e_A^-\) has exceptional lower colour \(L_A\); its complement
\(e_A^+\) has exceptional upper colour \(U_{\bar A}\).  Translation gives
one clean-\(H\) orbit of each, the opposite-shore colours recover the
translated data, and the endpoint reconstruction proves pairwise
middle-vertex disjointness.  This is a provider bank, not yet a collection
of port macros.

The numerical calibrations remain valid.  At \(m=5\),
\((q,s,h,a)=(9,9,1,1)\), giving three clean rows per bank, exceptional-bank
floor two, and global lower bound three.  At \(m=8\),
\((q,s,h,a)=(15,3,5,2)\), giving two rows per bank, exceptional-bank floor
four, and global lower bound five.

## 5. Audited matching-first forest/socket gate

Put
\[
 K=\operatorname{Cat}_m,\qquad
 N_m=(m+1)K=\binom{2m}{m},\qquad
 R_m=mK=\binom{2m}{m-1}.
\]
Let \(\overline M\) be a perfect matching of the clean quotient diamond
multigraph and let \(J(M)\) be the Johnson graph obtained from its physical
lift.  The audit verifies the following exact claims.

1. \(J(M)\) has \(R_m\) edges on all \(N_m\) middle vertices and uses every
   lower and upper adjacent colour once.  The exceptional filters are
   internal selected edges; they are not demands to be extended later.
   Their endpoints are mutually distinct, but a nonexceptional selected
   diamond can still meet one, so the degree rows remain necessary.
2. Because the clean group has odd order and acts freely on the middle rank,
   \(J(M)\to\overline J\) is an ordinary regular multigraph cover with no
   edge inversion.  The physical graph is a spanning linear forest exactly
   when
   \[
      \deg_{\overline J}(v)\le2,
      \qquad |E_{\overline J}(S)|\le |S|-1
          \quad(\varnothing\ne S\subseteq V(\overline J)),       \tag{5.1}
   \]
   with loops and parallel pairs counted as cycles.
   This is an independent condition.  At \(m=5\), where \(h=1\), the
   standard BTK perfect diamond matching has five distinct induced edges at
   \(E_5=\{0,2,4,6,8\}\), so quotient regularity does not imply the degree
   bound even in a clean Catalan instance.
3. Under (5.1), \(\overline J\) has \(K/h\) path components and its lift has
   \(K\).  Counting ports by degree deficit gives \(2K/h\) quotient and
   \(2K\) physical endpoint occurrences; an isolated vertex contributes two
   different port occurrences at the same vertex.
4. An invariant closure uses exactly \(K/h\) quotient seam orbits and \(K\)
   physical seams.  It is one physical Hamilton cycle exactly when the
   endpoint occurrence successor is one cycle and its total voltage is a
   unit in \(\mathbb Z_h\).  Pairwise-distinct seam-colour orbits on each
   typed shore give precisely the cap-two profile
   \(1^{R_m-K}2^K\).
5. A symmetry-broken physical Hamilton path instead uses \(K-1\) seams and
   exists exactly when the contracted seam graph is one path.  Pairwise
   distinct seam colours give \(1^{R_m-K+1}2^{K-1}\).  For \(h>1\) this
   single path cannot be \(H\)-invariant, since an odd nontrivial group cannot
   act freely through the order-at-most-two automorphism group of a path.

Thus the residual Kneser Hall problem is retired only for filters chosen as
the restriction of a global quotient matching.  A filter-closed shore is an
obstruction only in a fixed preassigned-provider subfibre.  The exact
unproved existence theorem is to select \(\overline M\) satisfying (5.1)
whose endpoint occurrences admit private literal seams with one-cycle/unit
voltage (or one physical path), while the internal forest and seams jointly
pass deeper-shadow, residence, boundary and compiler replay.  No all-\(m\)
existence follows from regular quotient Hall alone.

There is no remaining socket requirement merely to *extend* an exceptional
filter edge: it is already part of \(M\).  A private socket is still required
if that edge is to host a protected packet or if an endpoint is to carry a
closure seam.  Such a socket must record phase, ordered endpoints, voltage,
collar, host and witness resources; distinct filter middle endpoints alone
do not give this capacity.  This agrees with the exact variable reduction in
`MATH_REDUCTION_GLOBAL_QUOTIENT_MATCHING_PHYSICAL_FOREST_SOCKET_VOLTAGE_20260731.md`.

The reduction's core rows audit as follows.  `(QM)` is exactly quotient
perfect matching with parallel atoms retained.  `(D)` uses incidence
multiplicity two for loops and `(G)` is precisely the graphic-independence
system, so together they are equivalent to (5.1), not merely necessary
relaxations; `(D+)` is the exact additional prohibition on trivial path
components.  After `(D)--(G)`, `(C0)--(C2)` coherently orient every forest
path and form one quotient directed cycle; `(CE)/(CEp)` are needed to stop
catalogue aliases from reusing a literal edge.  The edge-count identity then
forces exactly \(K/h\) closure arcs.  `(V)` is the standard
voltage-generation condition for \(h>1\), and is correctly omitted for the
trivial group.  `(BW0)--(BW3)` are a conditional stronger block-wedge face:
they are exact only for the stated exhaustive phase-labelled seam catalogue.
Deleting one declared *physical phase occurrence* through `(B)` opens the
connected lift into one path; deleting the whole orbit would instead leave
\(h\) paths when \(h>1\).  Socket capacities and physical Benders rows are
sound only with the stated orbit-complete refinement and exact atom-to-lift
map.  No row in this formulation proves feasibility, guards, or compilation
automatically.

## 6. K16 interlaced-block reconciliation

The independent anatomy in
MATH_THEOREM_K16_THREE_PRIMARY_SPIRAL_BRAID_ANATOMY_20260731.md
changes the interpretation, not the validity, of the clean-\(H\) theorem.
The authenticated carrier consists of four strict co-oriented
\(\mathbb Z_{15}\)-spirals with base lengths
\[
                         426,\ 426,\ 3,\ 3
\]
and common exponent \(4\).  For \(H=\langle R^3\rangle\cong\mathbb Z_5\),
each block quotient has three sector subpaths, sector permutation
\((0\,1\,2)\), and full-tour voltage \(4\bmod5\).  The sector-tour return
map fixes the four block labels after contracting each \(n_i\)-vertex
sector subpath (the raw return takes \(3n_i\) quotient-edge transitions), so
the clean formula gives
\[
                         4\gcd(5,4)=4
\]
closed physical components.  Every block interlaces all three residual
sectors; the four blocks are not sector parts in the sense of the
contiguous-sector theorem.

The final K16 braid is outside the invariant cyclic theorem.  It deletes
one physical closure occurrence from each spiral and adds three
phase-specific Johnson seams, thereby producing one physical Hamilton path.
The fourth wrap has symmetric difference six and is not a Johnson edge.
Accordingly:

- clean voltage certifies each closed spiral before opening;
- the final path is certified by the physical \(t\)-block splice with
  \(t-1\) literal seams;
- there is no global unit-voltage condition for the final path; and
- a cyclic conclusion would require an additional literal Johnson seam.

For deleted closures \(D\), inserted seams \(J\), and background lower/upper
loads \(\mu^\pm\), exact adjacent-palette coverage is
\[
                         \mu^\pm(z)-d^\pm_z+j^\pm_z\ge1
\]
for every required colour \(z\).  Exact multiplicity preservation replaces
the inequality by equality to the prescribed load.  This condition is
necessary and sufficient because \(D\cup J\) is the complete edge
difference; deeper witnesses, residence and compilation remain separate.

The exact block count is
\[
 c\text{ parent cycles}\longmapsto2c\text{ A/B blocks}
   \longmapsto2c-1\text{ seams for a linear child}.
\]
It is a topology identity only.  K16 realizes \(2\mapsto4\mapsto3\).

Finally, the four spiral defects are not the four exceptional
period-three providers one-for-one: only one changed lower colour is short
and no changed upper colour is short; moreover Corollary 2.1 gives global
partial-orbit floor five, not four, for an edge set satisfying its exact
two-sided-rainbow hypotheses.  The paired-necklace theorem may organize
internal provider choices, but it does not label the K16 block connectors.
The correct reusable target is a palette-safe connector path through
sector-interlaced strict blocks, followed by a fully physical compiler
audit.

No all-\(m\) existence claim is made.
