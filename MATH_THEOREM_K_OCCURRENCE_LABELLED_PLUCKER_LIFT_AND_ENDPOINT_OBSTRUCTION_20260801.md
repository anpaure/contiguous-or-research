# Occurrence-labelled Plucker lifts: the exact square Markov theorem and the endpoint obstruction

Date: 2026-08-01  
Status: exact abstract theorem and exact application to the coatom `q=2`
action.  The theorem identifies a sufficient and, for universal fibres,
necessary labelled lift condition.  It does not construct the exterior
return bank required by the coatom compiler.

## 0. Outcome

After the common core is deleted, the `q=2` lower-shadow action of the
mixed coatom tensor is

\[
 (b,f_1)+(a,f_d)\quad\longleftrightarrow\quad
 (a,f_1)+(b,f_d).                                      \tag{0.1}
\]

Thus it is literally the quadratic Plucker relation on a Johnson square.
The two physical erosion columns are fixed; only their endpoint labels are
exchanged.

For an occurrence-labelled compiler table, let `G` be the bipartite graph
whose left vertices are source-fixed physical anchors and whose right
vertices are allowed endpoint labels.  Integral tables with fixed source
and endpoint marginals are the nonnegative integral fibres of the incidence
matrix of `G`.  Then:

1. the signed circuits of all even cycles of `G` form an exact Markov basis;
2. physical `2 x 2` Plucker switches form a Markov basis for every integral
   fibre if and only if `G` is chordal bipartite and every four-cycle of `G`
   is a certified physical square;
3. the smallest genuinely labelled obstruction is an induced six-cycle;
4. square switches preserve the set of used physical columns, so they can
   route alternating **cycles** but cannot close an alternating **path** or
   improve fixed-basis Hall deficiency; and
5. for a nested/Ferrers exterior bank, both the Markov row and the Hall row
   are explicit.  Quadrics suffice, and if
   `N_1 subseteq ... subseteq N_m`, then

   \[
       \delta=\max_{1\le j\le m}(j-|N_j|)^+.             \tag{0.2}
   \]

For the two coatom exposure chains, an exterior Ferrers bank with the two
deficiencies in (0.2) summing to an absolute constant would therefore give
an exact bounded-endpoint repair theorem.  The planted tensor does not
supply this bank: its exact local trace-guarded return graph is empty, so
its endpoint deficiency remains `2(d-1)`.  The Plucker theorem does not
alter that obstruction.

## 1. The literal coatom square at depth two

Use the notation of
`MATH_THEOREM_THREAD_D_COATOM_U5_NATIVE_COLUMNS_AND_RETURN_HALL_20260801.md`.
Put

\[
 V_0=\{\mathord\infty,b,c\},\qquad
 V_1=\{\mathord\infty,a,c\}.
\]

At `q=2`, the prefix and suffix filler profiles are

\[
 P_2=\{f_1,\ldots,f_{d-1}\},\qquad
 S_2=\{f_2,\ldots,f_d\}.
\]

The four old/new targets are

\[
\begin{array}{c|cc}
 &\text{prefix column}&\text{suffix column}\\ \hline
 \epsilon=0&K\cup V_0\cup P_2&K\cup V_1\cup S_2\\
 \epsilon=1&K\cup V_1\cup P_2&K\cup V_0\cup S_2.
\end{array}                                                  \tag{1.1}
\]

Factor out

\[
 R=K\cup\{\mathord\infty,c\}
      \cup\{f_2,\ldots,f_{d-1}\}.                            \tag{1.2}
\]

The four residual pairs in (1.1) are precisely

\[
 \{b,f_1\},\quad\{a,f_d\},\quad
 \{a,f_1\},\quad\{b,f_d\}.                                 \tag{1.3}
\]

They are the four vertices of the `J(4,2)` square on
`{a,b,f_1,f_d}`.  If `x_(u,v)` denotes the occurrence assigning endpoint
label `u` to source profile `v`, the packet binomial is

\[
 x_{b,f_1}x_{a,f_d}-x_{a,f_1}x_{b,f_d}.                      \tag{1.4}
\]

This proves (0.1).  Notice that (1.4) is occurrence-sensitive: the
prefix and suffix physical columns remain fixed.  A projected equality of
the four target masks does not by itself certify that those two particular
columns admit both endpoint choices with all trace guards.

## 2. Source-fixed occurrence tables

Let `S` be a finite set of physical source anchors, let `T` be a finite set
of endpoint labels, and let

\[
                         G=(S,T;E)                              \tag{2.1}
\]

be the exact allowed-incidence graph.  An edge belongs to `E` only when all
literal owner, trace, residence, pin and common-cap guards pass.  Envelope
containment alone is not an edge.

For prescribed nonnegative integral marginals `b_s,c_t`, define

\[
 \mathcal F_G(b,c)=
 \left\{x\in\mathbb Z_{\ge0}^{E}:
   \sum_{t:st\in E}x_{st}=b_s,
   \quad
   \sum_{s:st\in E}x_{st}=c_t\right\}.                       \tag{2.2}
\]

The matching case has `b_s,c_t in {0,1}`.  A physical quadratic switch on
the complete rectangle `{s,s'} x {t,t'}` is

\[
 e_{st}+e_{s't'}\quad\longleftrightarrow\quad
 e_{st'}+e_{s't}.                                             \tag{2.3}
\]

It is a legal nonnegative move exactly in the orientation whose two
subtracted entries are positive.  It preserves every marginal in (2.2).

If only a specified catalogue `Q` of physical coatom squares is available,
then (2.3) is allowed only for rectangles in `Q`.  This distinction is
load-bearing: an abstract four-cycle in the target projection need not be
a literal packet in the occurrence-labelled chronology.

## 3. Exact Markov basis

### Theorem 3.1 (even-cycle Markov basis)

For every bipartite support graph `G`, the signed moves on its simple even
cycles connect every nonempty fibre (2.2).

#### Proof

Take `x,y in F_G(b,c)`.  Colour `x-y` copies of an edge red when the
difference is positive and `y-x` copies blue when it is negative.  At every
vertex, equality of the marginals says that red degree equals blue degree.
Starting with any unused red edge and alternating red and blue therefore
closes an even circuit.  Remove its minimum multiplicity and continue.
This decomposes `x-y` into conformal alternating even circuits.

Flipping one such circuit subtracts only red edges which are present in the
current table, so every intermediate table is nonnegative.  Repeating the
operation reaches `y`.  Splitting a repeated circuit at a repeated vertex
gives simple even cycles.  \(\square\)

### Theorem 3.2 (quadratic criterion)

Assume every four-cycle of `G` belongs to the physical catalogue `Q`.
Then the physical quadrics (2.3) connect every integral fibre of `G` if and
only if `G` is chordal bipartite, meaning that every simple cycle of length
at least six has a chord.

#### Proof

Suppose first that `G` is chordal bipartite.  A chord of an alternating
cycle splits it into two shorter even cycles.  Orient the first subcycle so
that its move adds one copy of the chord; all of its subtracted nonchord
edges occur on the positive side of the original alternating circuit.
After that move the chord is present.  Orient the second subcycle so that it
subtracts the chord.  The two moves sum to the original cycle move and all
intermediate entries are nonnegative.  Induction on cycle length reduces
every move from Theorem 3.1 to physical four-cycles.

Conversely, suppose `G` has an induced cycle `C` of length `2r>=6`.  Give
every vertex of `C` marginal one and every vertex outside `C` marginal zero.
The two alternating perfect matchings of `C` lie in the same fibre.  No
four-cycle move is possible: vertices outside `C` have zero marginal and
the induced subgraph on `V(C)` has no four-cycle.  Hence that fibre is
disconnected.

If a four-cycle of `G` is omitted from `Q`, put marginal one on its four
vertices and zero elsewhere.  Its two diagonal matchings cannot be joined,
so availability of every four-cycle is also necessary for a universal
all-fibre statement.  \(\square\)

In toric language, map `z_(st)` to `u_s v_t`.  The kernel is generated by
the binomials of even cycles; it is generated by the physical quadratic
Plucker binomials exactly under Theorem 3.2.  No probabilistic or asymptotic
input is needed.

### Corollary 3.3 (Ferrers banks)

Suppose the source anchors can be ordered so that

\[
                 N(s_1)\subseteq N(s_2)\subseteq\cdots
                    \subseteq N(s_m).                         \tag{3.1}
\]

Then `G` is chordal bipartite.  Consequently all occurrence-labelled
tables on this bank are connected by physical squares whenever every
four-cycle is a certified coatom square.

#### Proof

On a cycle of length at least six, choose a source having largest
neighbourhood.  It is adjacent to both neighbours of every earlier source
on the cycle.  At least one of those endpoints is nonconsecutive to the
chosen source, giving a chord.  Apply Theorem 3.2.  \(\square\)

## 4. Why an unlabelled square need not lift

Suppose a projection forgets physical source identities.  A projected
quadratic move records only that two old corner counts are replaced by two
new corner counts.  At a labelled state, let `A_1,A_2` be the two sets of
currently occupied anchors which can legally take the respective new
endpoint labels.  If a physical packet additionally restricts which pair
of anchors may be switched together, let `H` be that compatibility graph
on `A_1 dotcup A_2`.

### Proposition 4.1 (atomic lift criterion)

One projected square lifts at the current labelled state if and only if

\[
                              E(H)\ne\varnothing.              \tag{4.1}
\]

For `k` parallel copies, the exact condition is that `H` contain a matching
of size `k`.  In the absence of pair restrictions this reduces to the two
individual nonemptiness conditions `A_1,A_2 != empty`.

#### Proof

A lifted switch must name the two source occurrences whose old incidences
are deleted and whose new incidences are inserted.  They are precisely an
edge of `H`.  Conversely such an edge names the literal four incidences and
the certified physical packet.  The parallel statement is the same
argument with source-disjointness.  \(\square\)

Even if every projected step has a lift somewhere, labelled fibres can be
disconnected.  The minimal obstruction is

\[
\begin{array}{c|ccc}
 &t_1&t_2&t_3\\ \hline
 s_1&1&1&0\\
 s_2&0&1&1\\
 s_3&1&0&1.
\end{array}                                                   \tag{4.2}
\]

The two matchings

\[
 \{s_1t_1,s_2t_2,s_3t_3\},\qquad
 \{s_1t_2,s_2t_3,s_3t_1\}                                   \tag{4.3}
\]

have identical unlabelled endpoint counts.  The support is an induced
six-cycle and contains no square, so (4.3) cannot be connected by quadratic
moves.  The missing primitive is the cubic circuit

\[
 z_{s_1t_1}z_{s_2t_2}z_{s_3t_3}
   -z_{s_1t_2}z_{s_2t_3}z_{s_3t_1}.                           \tag{4.4}
\]

This example is minimal after the one-square missing-incidence failure:
an induced bipartite cycle longer than four needs at least three vertices
on each shore.

Thus a projected Markov basis lifts through all labelled states under two
separate hypotheses:

1. every projected step has the occurrence-level lift (4.1); and
2. every fixed projected fibre is connected, for example by the chordal
   criterion of Theorem 3.2.

Under these hypotheses one lifts a projected path step by step and then
uses fibre moves at its endpoint.  The six-cycle shows that neither
projected connectivity nor target-level Hall implies the second row.

## 5. Square moves preserve the physical basis

Let `M` be a matching from compiler obligations to physical cells and put

\[
                       Q(M)=\{c:c\text{ is used by }M\}.        \tag{5.1}
\]

Every square switch replaces two incidences on two cells by the opposite
two incidences on the **same** cells.  Hence

\[
                          Q(M')=Q(M)                            \tag{5.2}
\]

after every sequence of Plucker moves.

This yields a sharp separation.

### Theorem 5.1 (cycles versus endpoint paths)

Let `M_0,M_1` be two matchings saturating the same left shore.  Their
symmetric difference is a disjoint union of alternating cycles and
alternating paths.  The number of path components is

\[
                  \frac{|Q(M_0)\mathbin\triangle Q(M_1)|}{2}. \tag{5.3}
\]

If every alternating cycle lies in a chordal physical-square support, all
cycle components can be implemented by Plucker switches.  No path component
can be implemented by Plucker switches alone.  A basis-changing return or
boundary move is necessary for each path endpoint pair.

#### Proof

Degree in the symmetric difference is at most two.  Since the left degrees
agree in the two matchings, every path has both endpoints on the cell shore,
one in `Q(M_0)-Q(M_1)` and one in `Q(M_1)-Q(M_0)`.  This proves the
decomposition and (5.3).  Theorem 3.2 handles the cycles.  Equation (5.2)
rules out every path.  \(\square\)

For a fixed physical basis `Q`, define

\[
              \delta_Q=|L|-\nu(G[L,Q]).                       \tag{5.4}
\]

No sequence of q2 squares can decrease (5.4).  It is a Hall invariant of
the frozen basis, not a mixing-time issue.  Choosing a new basis requires
an alternating path to an unused cell.

## 6. Exact Ferrers Hall row and a bounded-defect criterion

Let `x_1,...,x_m` be obligations with nested cell lists

\[
                  N_1\subseteq N_2\subseteq\cdots\subseteq N_m.\tag{6.1}
\]

### Lemma 6.1 (nested Hall formula)

The minimum number of unmatched obligations is

\[
                    \delta=\max_{1\le j\le m}(j-|N_j|)^+.     \tag{6.2}
\]

#### Proof

The first `j` obligations have union neighbourhood `N_j`, giving the lower
bound.  For an arbitrary subset `X`, let `j=max X`.  Then
`N(X)=N_j` and `|X|<=j`, so its Hall deficit is at most the corresponding
quantity in (6.2).  Hall's deficiency formula proves equality.  \(\square\)

Combine Lemma 6.1 and Corollary 3.3.  If the prefix and suffix coatom
exposure chains have disjoint exterior banks with nested legal lists
`N_j^-` and `N_j^+`, and every four-cycle is a literal source-fixed coatom
square, then:

* their exact total unmatched endpoint count is

  \[
  \beta_{\rm end}=
   \max_j(j-|N_j^-|)^++\max_j(j-|N_j^+|)^+;                  \tag{6.3}
  \]

* every fixed-margin ambiguity in the matched core is removable by q2
  Plucker switches; and
* appending the `beta_end` unmatched soft targets is an exact
  `+beta_end` terminal repair.

Thus the concrete sufficient row for an additive constant is

\[
             \sup_d\beta_{\rm end}(d)<\infty.                 \tag{6.4}
\]

This is stronger and more checkable than a generic expansion hypothesis:
it is a list of prefix inequalities plus literal certification of the
rectangles.  It is not automatic from set inclusion of the lower targets.
Trace guards can delete a nonmonotone set of incidences, so (6.1) must be
proved for the exact occurrence-labelled bank.

## 7. Application and exact boundary

For the planted tensor, the q1 hinge is already a closed alternating cycle.
At depths `2<=q<=d`, the native exchange graph has `2(d-1)` deep rungs.
Thread D's exact trace audit proves that every local candidate return
incidence deletes a complete filler occurrence, so the trace-guarded local
return graph is empty.  Therefore

\[
                 \delta_{\rm ret,loc}=2(d-1).                  \tag{7.1}
\]

The q2 Plucker square (1.4) does not contradict (7.1).  It exchanges the
labels on the two native columns and hence handles a cycle component; it
does not create an exterior return column and cannot change the used-cell
basis by Theorem 5.1.

The exact remaining occurrence-labelled theorem is now narrow:

> Construct exterior trace-guarded source-fixed banks for the two nested
> coatom chains whose neighbourhoods are Ferrers (or, more generally,
> chordal bipartite with all four-cycles physically certified) and whose
> Hall deficiency is bounded absolutely as in (6.3).

An exterior bank satisfying that statement would turn the projected q2
Johnson-square action into a literal labelled Markov action and would bound
the return endpoints.  It would still need joint compatibility with the
higher-depth cap equations and with the packet task `U5`; the q2 theorem
alone does not prove full compiler feasibility or `B(k)+O(1)`.

## 8. The all-depth companion of an adjacent filler swap

The preceding q2 theorem is rankwise.  A canonical packet is not a pure
q2 move: its lower action is the entire antisymmetric filler flag.  The
exact companion can nevertheless be calculated and then cancelled
algebraically.

Let `F` be a `d`-element internal filler set, let

\[
 \pi=(x,y,h_1,\ldots,h_{d-2}),\qquad
 \pi'=(y,x,h_1,\ldots,h_{d-2}),                              \tag{8.1}
\]

and let `A_F(pi)` be the antisymmetric maximal-chain signature from
`MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`.
Put

\[
                         D_F(x,y)=A_F(\pi)-A_F(\pi').          \tag{8.2}
\]

### Lemma 8.1 (two-layer support, `d>=3`)

Assume `d>=3`.

The only nonzero layers of `D_F(x,y)` are

\[
\begin{aligned}
 (D_F)_1&=e_{\{x\}}-e_{\{y\}},\\
 (D_F)_{d-1}&=e_{F-\{y\}}-e_{F-\{x\}}.                       \tag{8.3}
\end{aligned}
\]

Equivalently, the packet-depth support is exactly `q=d` and `q=2`.

#### Proof

Swapping positions one and two changes only the first prefix.  It changes
only one suffix as well: the `(d-1)`-suffix is the complement of the first
entry.  Every other prefix and suffix set is unchanged.  Substitution in
`A_F(pi)_t=e_(P_t(pi))-e_(S_t(pi))` gives (8.3).  Since
`t=d+1-q`, the two layers correspond to `q=d` and `q=2`.  \(\square\)

After applying the active-label embedding

\[
 \Psi_{a,b}(e_X)=e_{G\cup\{a\}\cup X}
                    -e_{G\cup\{b\}\cup X},                  \tag{8.4}
\]

both rows of (8.3) are Johnson-square moves.  Thus an adjacent flag swap
does isolate q2 up to one forced reflected companion at q=d.  A lone q2
square with zero q=d action is impossible for a serial canonical-packet
combination: its nonzero pair-degree change would violate the reflected
pair-degree invariant.

At `d=2`, the indices `t=1` and `t=d-1` coincide.  Prefix and suffix
changes occur in the same layer and add, giving

\[
                         D_F(x,y)_1=2(e_{\{x\}}-e_{\{y\}}).
\]

Thus the sole physical row is `2Q_G` at `q=2=q=d`; there are not two
separately indexed companion rows.  The cross-filler construction below
therefore starts at `d>=3`, while `d=2` is a bounded base case.

## 9. Exact cross-filler commutator

Assume `d>=3`.  Take mutually distinct fillers `x,y,u,v` and a set `H` of
`d-3` further fillers.  Put

\[
 F_u=H\mathbin{\dot\cup}\{x,y,u\},\qquad
 F_v=H\mathbin{\dot\cup}\{x,y,v\}.                          \tag{9.1}
\]

In both flags put `x,y` first, use the same order on `H`, and put `u` or
`v` last.  Define

\[
                    C=D_{F_u}(x,y)-D_{F_v}(x,y).               \tag{9.2}
\]

### Theorem 9.1 (pure-q2 cube)

The commutator (9.2) has zero action at every depth except q2.  Its q2
filler action is

\[
 C_{q=2}=
 e_{Hxu}+e_{Hyv}-e_{Hyu}-e_{Hxv}.                            \tag{9.3}
\]

After (8.4), the complete physical-value action is the eight-term cube

\[
                (e_a-e_b)\otimes(e_x-e_y)\otimes(e_u-e_v),   \tag{9.4}
\]

with the fixed core `G union H` adjoined to every corner.  In particular,
all point and pair degrees of (9.4) vanish.

#### Proof

The q=d rows of the two summands in (9.2) are both `e_x-e_y`, so they
cancel.  Lemma 8.1 says there are no other possible rows besides q2.  At
q2,

\[
\begin{aligned}
 (D_{F_u})_{d-1}&=e_{Hxu}-e_{Hyu},\\
 (D_{F_v})_{d-1}&=e_{Hxv}-e_{Hyv},
\end{aligned}
\]

which gives (9.3).  Expanding (8.4) gives (9.4).  Every one- or two-factor
marginal of a threefold alternating tensor is zero.  \(\square\)

At the packet level, (9.2) is the signed four-toggle word

\[
 +\Delta(F_u,\pi_u)-\Delta(F_u,\pi_u')
 -\Delta(F_v,\pi_v)+\Delta(F_v,\pi_v').                       \tag{9.5}
\]

Thus the first all-depth-neutral q2 primitive obtained from adjacent flag
swaps is not a quadratic move but a `2 x 2 x 2` cube.  This is forced by
the reflection invariant: a pure-q2 action must have zero pair-degree
change, whereas one Johnson square does not.

For `d=2`, q2 and q=d are the same row, so there is no distinct companion
to cancel and (9.1) is unavailable.  That dimension must be handled as the
separate bounded base case described after Lemma 8.1.

## 10. Physical lift conditions and the canonical collision

Formula (9.5) is an exact counter identity, not automatically four
simultaneously plantable intervals.  A literal realization requires all of
the following.

1. **Four oriented slots.**  The carrier must contain the four old/new
   packet phases named in (9.5), with the indicated orientations and with
   identical `G,a,b,x,y,H` labels.
2. **Topology resolution.**  Their occurrence-labelled owner union must be
   resolvable to a simple degree-two path/factor.  Pairwise disjoint owner
   sets are sufficient but are not necessary if a certified shared-owner
   splice is supplied.
3. **Boundary separation.**  Every lower window of width at most `d+1`
   crossing a slot boundary must be literally unchanged, or its signed
   contribution must be included in (9.5).  The ordinary common endpoint
   block condition is sufficient.
4. **U1--U4 guards.**  Each serial intermediate replacement must retain the
   exact owner, immediate-palette, OR-deck and residence certificates.
5. **Address-labelled U5.**  The eight q2 corners must be represented by one
   co-selectable common-cap bank.  Equality of the value counter (9.4) does
   not identify physical cells at different slots.

The naive private-slot lift fails condition 2 for the canonical packet.
For a fixed internal filler set `F` and fixed unordered active pair
`{a,b}`, the two order variants in (8.1) both contain the upper-screen owner

\[
              O_F=K\cup\{\mathord\infty,c,a,b\}\cup F.        \tag{10.1}
\]

This owner contains neither private extreme filler nor the private active
label `e`.  Hence changing those customary private labels does not separate
the two copies.  The two `F_u` slots in (9.5) collide at `O_(F_u)`, and the
two `F_v` slots collide at `O_(F_v)`.  Four pairwise owner-disjoint canonical
slots therefore do not realize the commutator.

A physical theorem must add one of two genuinely new ingredients:

* a shared-owner four-arm resolver which identifies `O_F` once and reconnects
  the two packet fragments into degree-two Johnson paths while preserving
  all boundary decks; or
* a modified flag-order actuator whose packet fingerprint privatizes
  (10.1) without changing the signed rows (8.3).

This collision is not an algebraic invariant: the independently proved
three-packet active-label triangle avoids it because its three exceptional
owners carry the distinct pairs `{x,y},{y,z},{z,x}`.  That triangle,
however, cancels the q2 action together with every deeper action.  It does
not supply the pure-q2 cube (9.4).

Consequently the exact current boundary is:

> the cross-filler commutator cancels the forced deep companion and gives a
> an exact pure-q2 cube algebraically; its first physical obstruction is
> the two repeated central upper owners, before common-cap Hall is even
> tested.

## 11. Markov basis after exact companion cancellation

Assume `d>=3` throughout this section.

There is an exact Markov interpretation of the cube (9.4).  Fix the common
core and the active pair `{a,b}`.  Let `X` index the first extreme filler
and let `U` index the filler which distinguishes the internal core.  Write

\[
                         n_{\alpha xu}\qquad
       (\alpha\in\{a,b\},\ x\in X,\ u\in U)                  \tag{11.1}
\]

for the q2 occurrence table.  By the reflected pair-degree invariant,
requiring zero q=d companion fixes all q2 pair degrees, hence all
two-coordinate marginals of (11.1).  In particular put

\[
 m_{xu}=n_{axu}+n_{bxu},\qquad z_{xu}=n_{axu}.                \tag{11.2}
\]

Then `n_bxu=m_xu-z_xu`, and the remaining fixed two-way marginals say
exactly that `z` has prescribed row and column sums, subject to

\[
                              0\le z_{xu}\le m_{xu}.           \tag{11.3}
\]

Under this identification, the cross-filler cube (9.4) is one rectangle
move on `z`.

### Theorem 11.1 (pure-q2 all-depth-neutral Markov basis)

Let

\[
                         G_m=(X,U;\{xu:m_{xu}>0\}).             \tag{11.4}
\]

The alternating moves on all even cycles of `G_m` connect every nonempty
fibre (11.2)--(11.3).  Cross-filler cubes alone connect every such fibre if
and only if `G_m` is chordal bipartite and every four-cycle has a literal
physical resolver satisfying Section 10.

#### Proof

For two feasible tables `z,z'`, orient a cell according to the sign of
`z-z'`.  Equality of row and column sums decomposes the discrepancy into
sign-alternating even cycles of `G_m`.  A unit cycle move subtracts only at
cells where `z>z'` and adds only where `z<z'`.  Hence it remains between
zero and `m` at every cell and reduces the distance to `z'`.

If `G_m` is chordal bipartite, split a long cycle along a chord.  If the
transient chord is not at capacity, first use the subcycle which adds it and
then the subcycle which consumes it; if the chord is at capacity, use the
opposite order.  (At an intermediate value either order is feasible.)
Induction gives a capacity-feasible sequence of rectangles.  In the
original three-way table these rectangle moves are exactly (9.4).
Conversely, an
induced even cycle with unit capacities has two alternating feasible
tables and no cube move.  The omitted-four-cycle obstruction is identical.
\(\square\)

Thus the correct hierarchy is:

* one packet carries the entire flag, whose q2 and q=d rows are reflected
  squares;
* for `d>=3`, an adjacent-order difference cancels all other rows and gives
  exactly those two companion squares;
* a cross-filler difference gives a pure-q2 cube; and
* a chordless cycle in the cross-filler support requires the corresponding
  higher cube-cycle macro.

This theorem is exact at the occurrence-counter level and preserves the
all-depth reflected quadratic margins.  It still does not change the used
physical compiler basis (Section 5), and it still depends on the unresolved
owner/palette-transparent resolver in Section 10.  Hence it can remove
cycle ambiguity after an exterior return matching is found, but it cannot
by itself reduce return-Hall endpoint deficiency.
