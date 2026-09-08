# H25 multi-collar circulation and the exact cross-stratum gate

Date: 2026-07-28

Status: exact integral reduction, exact maximum-shore separator, and one
certified positive two-braid Hall compound `H25 -> H25 -> H24`.  The
one-common-word lift remains open.  The authoritative base of the compound
is Hall 25, not Hall 29.

## 0. Result

Let `H25` denote the chronology in
`scratch/k15_segment_braid_hall25.json`.  An arbitrary integral reconnection
of oriented retained segments has an exact port description: after adjoining
one common formal closing seam between the two prescribed path ends, its old
and new seam matchings differ by a disjoint union of alternating even cycles.
This is the correct
**multi-collar circulation**.  Port balance alone is insufficient: the new
segment graph must be one cycle (one path after deleting the closing seam),
every new seam must be Johnson-legal, and all overlapping dependency collars
must be materialized jointly.

For pairwise disjoint full collars, their signed target-neighbourhood and
lower/upper trace columns add exactly, while their local residence tests
compose.  At depth three, a seam can affect at most `9,10,11` compiler-cell starts in rows
`0,1,2`, hence at most `30` old and `30` new cells.  The smaller count obtained
from the visible erosion intervals alone is unsafe: the mandatory-coordinate
mask has the full middle dependency interval

\[
                         [s-6,s+h+3]                 \tag{0.1}
\]

for a row-`h` cell starting at `s`.

The H25 maximum-deficiency shores form a very large distributive lattice, but
the condition that one signed boundary bank opens **all** of them is one
ordinary integral minimum cut built over a `9,256`-node residual-DM quotient
(with one auxiliary node per nonforced gained cell).  This is an exact
Benders separator for an integral collar master.  It does not replace
the near-critical Hall cuts, the cross-depth shadow rows, or the one-common-
word pin test.

There is now a concrete positive Hall-layer circulation.  From H25 apply

\[
 \operatorname{FR}(1512,2458,4103),\qquad
 \operatorname{FR}(2664,3491,6201).                 \tag{0.2}
\]

The score sequence is `25 -> 25 -> 24`.  The first braid is a nonidentity
portal move which relocates the active maximum shore; the second discharges
that replacement shore.  Their composition is an integral endpoint
circulation in the sense of Theorem 2.1 and, by Theorem 4.1, its signed
boundary opens every H25 maximum-deficiency shore simultaneously.  It
preserves the exact lower-hole vector, all upper supports, the deck, and
residence.  It is not yet a coefficient-one compiler.

The one-common-word test remains integral and global.  Once a final chronology
and an injective target-to-cell assignment have been chosen, it is decided
coordinatewise by the maximal allowed-position sets.  It does not decompose
into separately feasible collar words.  The joint target assignment/pinning
matrix is not generically TU: its minimal interval blockers contain the usual
determinant-two triangle.

Thus the surviving construction target is one integral oriented-segment
reconnection and one integral target/cell assignment satisfying, for the
same choice:

1. one-path topology, Johnson seams, and depth-three residence;
2. every protected upper and lower last-witness inequality;
3. all H25 Hall-current cuts;
4. the necessary lower prefix corridor;
5. one maximal common physical word.

The present one-braid local minimum proves that no single move in the complete
stored `FF/RF/FR/RR` catalogue satisfies all of these Hall descent cuts.  The
compound (0.2) proves that bounded lookahead defeats this local obstruction.

## 1. Authoritative H25 data

Here

\[
 k=15,\qquad r=8,\qquad d=3,\qquad
 W=\binom{15}{8}=6435.
\]

The maximal erosion has `W+d=6438` physical positions.  The three lower cell
rows have

\[
                  6438+6437+6436=19311              \tag{1.1}
\]

cells.  Their bipartite graph against all `16,383` nonempty targets of ranks
at most seven has matching size `16,358` and deficiency

\[
                              D(H25)=25.              \tag{1.2}
\]

The exact lower-hole vector is

\[
                         (4,19,4,1,0,0,0),            \tag{1.3}
\]

while every upper depth `q=1,...,7` has complete support.  In particular the
older value `h_2=21` is not the H25 value.

Every resident flat-middle optimum in this dimension satisfies the prefix
inequalities

\[
                  h_1\le2,\qquad h_2\le h_1+3\le5.  \tag{1.4}
\]

Consequently a successful endpoint of this lane must remove at least two of
the four first-shadow holes and at least fourteen of the nineteen
second-shadow holes.  Hall descent alone is not yet a coefficient-one
compiler.

The audited descent into this state is

\[
 H29\longrightarrow H28\longrightarrow H27\longrightarrow H26
 \xrightarrow{\operatorname{FR}(3259,3823,5264)}H25. \tag{1.5}
\]

An exhaustive scan from H25 contains

\[
 551986\text{ Johnson moves},\quad12029\text{ resident moves},\quad
 9233\text{ upper-safe moves},                         \tag{1.6}
\]

and its best Hall score remains `25`.  This is the one-move local-minimum
theorem used below.

The certified two-braid continuation is

\[
 H25\xrightarrow{\operatorname{FR}(1512,2458,4103)}H25^{\rm portal}
 \xrightarrow{\operatorname{FR}(2664,3491,6201)}H24. \tag{1.7}
\]

It is audited independently in
`scratch/k15_segment_braid_hall24_portal_audit.json`.

## 2. Integral endpoint circulation

Cut H25 into nonempty retained segments

\[
                         S_1,S_2,\ldots,S_b.
\]

Give segment `i` two endpoint ports `i^-` and `i^+`, and let `K` be the
matching which joins the two ports of each segment.  Let `e_L,e_R` be the two
prescribed external path ports.  An open seam matching `M` pairs every other
port and leaves exactly `e_L,e_R` unmatched.  Adjoin the same formal closing
edge `e_Le_R` to both the old and new systems and write

\[
                    \overline M=M\cup\{e_Le_R\}.    \tag{2.0}
\]

### Theorem 2.1 (port representation)

An oriented ordering of all retained segments, using each exactly once and
having the prescribed two external endpoints, is equivalent to a seam
matching `M` for which

\[
                         K\cup\overline M             \tag{2.1}
\]

is one alternating cycle.  Deleting the formal closing edge turns (2.1) into
the required single path.  Here the union is a two-edge-coloured multigraph
union: a segment edge and a seam edge are retained as distinct parallel
copies if their endpoint pair happens to agree.  If `M_0` is the old open
seam matching, then

\[
               \overline M\mathbin\triangle\overline M_0
                =M\mathbin\triangle M_0              \tag{2.2}
\]

is a disjoint union of alternating even cycles.  Conversely, flipping any
family of those alternating cycles preserves the port degrees; it gives a
physical segment ordering precisely when (2.1) is still one cycle.

#### Proof

Traverse alternately through a retained segment edge in `K` and an edge of
`overline M`.  Every port has degree two in their union, so the union is a disjoint
collection of alternating cycles.  It encodes one ordering of every segment
exactly when it has one component.  The formal closing edge marks the two
external ends.  The symmetric difference of two perfect matchings has even degree at every
port and therefore decomposes into alternating even cycles.  Flipping a
component interchanges its old and new matching edges and preserves degree
one in the augmented seam matching; the common closing edge stays fixed.
Connectivity is the only remaining topological condition.  \(\square\)

The components of (2.2) are the collar circuits.  A directed
exit-to-entrance encoding gives the usual integral assignment degree rows
after segment orientations are fixed.  It must still include the one-cycle
subtour inequalities.  Thus “balanced port flow” by itself may produce
several chronology components and is not the desired object.

Every new physical seam in `M` (not the label-free formal closing edge) also
has to satisfy

\[
                        |T_{\rm left}\cap T_{\rm right}|=7. \tag{2.3}
\]

This is independent of the port-degree equations.

## 3. Exact collar locality

For a final depth-three-resident chronology `T`, put

\[
 P_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T_i,
 \qquad0\le p<W+3.                                  \tag{3.1}
\]

A lower compiler cell `c=(h,s)`, `0<=h<=2` and
`0<=s<W+3-h`, occupies the physical interval

\[
                         I_c=[s,s+h].                \tag{3.2}
\]

Its envelope depends on `P_s,...,P_{s+h}`.  Its mandatory mask also needs the
complete carrier tuple of every central coordinate that might be forced on a
subset of (3.2).  A possible central start lies between `s-3` and `s+h`, and
deciding its whole four-position carrier tuple inspects (3.1) from three
positions before it through three positions after it.  Hence the exact
middle dependency is (0.1), intersected with `[0,W-1]` at a global end.

### Lemma 3.1 (thirty cells per seam)

An interior cut can affect at most

\[
                              9+h                    \tag{3.3}
\]

row-`h` cell starts.  Thus one seam has at most

\[
                         9+10+11=30                 \tag{3.4}
\]

compiler cells in either its deleted or inserted bank.

#### Proof

The interval `[s-6,s+h+3]` crosses a fixed cut for exactly `9+h` possible
values of `s`, before truncation at the two global ends.  Summing over
`h=0,1,2` gives (3.4).  \(\square\)

For a depth-`q` intersection or union row, only the `q` starts whose
`q+1`-vertex window crosses a seam can change.  Residence changes only in
the depth-three seam run collars.  Reversal or translation of an internal
segment transports all wholly internal windows and their complete cell
profiles bijectively.

Consequently, if every old and new dependency collar is disjoint from every
other one, all signed ledgers add.  If two dependency intervals overlap,
the purported atoms are not independent: they must be contracted to one
macro-collar and their final chronology, erosion, mandatory masks, pins, and
cell profiles must be recomputed jointly.  This is an exact hypothesis, not
a probabilistic separation convenience.

## 4. Signed Hall current across all strata

Let `G_0` be the H25 compiler graph.  For a target shore
`X` define

\[
 g_0(X)=|X|-|N_{G_0}(X)|,
 \qquad \sigma_0(X)=25-g_0(X).                       \tag{4.1}
\]

For a materialized multi-collar endpoint `F`, put

\[
                  J_F(X)=|N_{G_F}(X)|-|N_{G_0}(X)|. \tag{4.2}
\]

Equivalently, cancel old and new cells by their complete target-neighbourhood
profiles.  If `B^-` and `B^+` are the remaining banks, then

\[
 J_F(X)=\#\{c\in B^+:\Gamma(c)\cap X\ne\varnothing\}
       -\#\{c\in B^-:\Gamma(c)\cap X\ne\varnothing\}. \tag{4.3}
\]

### Theorem 4.1 (all-shore criterion)

The new Hall deficiency is

\[
 D(G_F)=25-\min_X\bigl(\sigma_0(X)+J_F(X)\bigr).    \tag{4.4}
\]

In particular,

\[
 D(G_F)\le24
 \quad\Longleftrightarrow\quad
 J_F(X)\ge1-\sigma_0(X)\quad\hbox{for every }X,     \tag{4.5}
\]

and

\[
 D(G_F)=0
 \quad\Longleftrightarrow\quad
 J_F(X)\ge g_0(X)\quad\hbox{for every }X.           \tag{4.6}
\]

#### Proof

Hall deficiency is the maximum of `|X|-|N(X)|`.  Substituting (4.1) and
(4.2) gives

\[
 |X|-|N_{G_F}(X)|=25-\sigma_0(X)-J_F(X),
\]

and taking the maximum proves (4.4).  The two equivalences follow by
integrality.  \(\square\)

Thus opening every old maximum shore means

\[
              \min_{X:\sigma_0(X)=0}J_F(X)\ge1,    \tag{4.7}
\]

but (4.7) alone is not sufficient for descent: a near-critical shore can
receive negative current and become the new blocker.  Equation (4.5), not
only (4.7), is the final one-unit test.

There is also a completely integral primal certificate.  Fix an H25 maximum
matching `M`.  If materializing the compound destroys `r` edges of `M`, let
`M_0` be the surviving matching.  Then the compound descends to deficiency at
most 24 if and only if the final graph contains `r+1` vertex-disjoint
`M_0`-augmenting paths.  Indeed, the symmetric difference of `M_0` with a
matching larger by `r+1` contains at least that many `M_0`-augmenting
components (discard any components of the opposite sign and keep `r+1`);
the converse follows by augmenting along them.  This certificate is often
smaller than listing all dual shores, but it still depends on the whole
compound boundary bank.

For disjoint or already-contracted macro-collars `gamma`, define the signed
profile column

\[
 \Delta_\gamma(U)=
 \#\{\hbox{new cells of profile }U\}
 -\#\{\hbox{old cells of profile }U\}.              \tag{4.8}
\]

An integral selection `z_gamma` then has

\[
 J_z(X)=\sum_\gamma z_\gamma
          \sum_U\Delta_\gamma(U)\mathbf1[U\cap X\ne\varnothing]. \tag{4.9}
\]

Every blocking shore returned by (4.5) therefore gives the exact Benders row

\[
 \sum_\gamma z_\gamma J_\gamma(X)
                         \ge1-\sigma_0(X).          \tag{4.10}
\]

The same `z` must satisfy the upper and lower rows

\[
 m_q^\pm(S)+\sum_\gamma z_\gamma
                  \Delta_{\gamma,q}^\pm(S)\ge1     \tag{4.11}
\]

for every protected signed target.  This is the promised cross-stratum
coupling: independent choices for different depths are invalid.

## 5. The H25 maximum-shore lattice

Fix a maximum matching `M` of `G_0`.  In the residual bipartite digraph direct
every incidence edge from target to cell and add the reverse cell-to-target
arc for every matched edge.  Let `Z_-` be the vertices reachable from the
unmatched targets and let `Z_+` be the complement of the vertices from which
an unmatched cell is reachable.

### Theorem 5.1 (residual-DM representation)

The maximum-deficiency shores of H25 are precisely

\[
                           X=Z\cap L,                \tag{5.1}
\]

where `Z` is successor-closed in the residual digraph and

\[
                           Z_-\subseteq Z\subseteq Z_+. \tag{5.2}
\]

#### Proof

Equality in the matching lower bound forces every unmatched target into a
maximum shore, excludes unmatched cells from its neighbourhood, and forces
the matched target of every selected matched cell back into the shore.
Together with all target-to-cell arcs, this says exactly that
`X union N(X)` is successor-closed and satisfies (5.2).  Conversely, for
such a closed set, its selected cells are exactly `N(X)`.  Every optional
residual component is balanced between targets and matched cells, while the
forced part has excess 25.  Hence `|X|-|N(X)|=25`.  \(\square\)

The exact census is:

| quantity | value |
|---|---:|
| canonical minimum `(|X|,|N(X)|)` | `(1320,1295)` |
| canonical maximum `(|X|,|N(X)|)` | `(10629,10604)` |
| optional targets / cells | `9309 / 9309` |
| optional balanced SCCs | `9256` |
| quotient arcs | `15219` |
| quotient height | `8` |
| source / sink SCCs | `2214 / 5760` |

The optional SCC profile is

\[
 9237(1,1)+4(2,2)+8(3,3)+6(4,4)+1(16,16).          \tag{5.3}
\]

The minimum-shore rank profile is

\[
                 4:8,\quad5:72,\quad6:359,\quad7:881, \tag{5.4}
\]

with target digest

```text
89449e9fe9fb085c96ec911e3a9fad61f1e0409e4c6ef0133ed72677eb273e83
```

and the maximum-shore profile is

\[
                 4:24,\quad5:515,\quad6:3664,\quad7:6426, \tag{5.5}
\]

with digest

```text
e3be91d8130cb5022d526ac667c6d8e7f565bf92f383a01011abf2ff24f1c6da
```

In particular there are at least `2^5760` maximum shores.  They cannot be
audited one at a time.

The old H25 cells have the following exact activity classes over this
lattice:

| class | total | depths `0,1,2` | activity on a shore |
|---|---:|---:|---|
| forced | `1295` | `72,344,879` | `1` |
| optional | `9309` | `443,3322,5544` | one SCC indicator |
| excluded | `8707` | `5923,2771,13` | `0` |

## 6. One min-cut opens all maximum shores

Let `x_C` indicate that optional SCC `C` is in `Z`.  If the quotient has an
arc `C->D`, successor closure is

\[
                             x_C\le x_D.             \tag{6.1}
\]

For a gained boundary cell `c` with target neighbourhood `U`, its activity is

\[
 \phi_U(x)=
 \begin{cases}
 1,&U\cap (Z_-\cap L)\ne\varnothing,\\
 0,&U\cap (Z_+\cap L)=\varnothing,\\
 \displaystyle\bigvee_{C\in K(U)}x_C,&\text{otherwise},
 \end{cases}                                      \tag{6.2}
\]

where `K(U)` is the set of optional target SCCs met by `U`.  A lost old cell
has activity `1`, `x_C`, or `0` according as it is forced, optional, or
excluded.  Hence the exact worst current on the whole maximum-shore lattice
is

\[
 \mu(B^-,B^+)=
 \min_{\substack{x\in\{0,1\}^{9256}\\x_C\le x_D\ (C\to D)}}
 \left(\sum_{c\in B^+}\phi_{\Gamma(c)}(x)
       -\sum_{c\in B^-}\psi_c(x)\right).            \tag{6.3}
\]

### Theorem 6.1 (maximum-closure separator)

The minimization (6.3) is one integral `s-t` cut.  All H25 maximum shores are
opened simultaneously if and only if

\[
                              \mu(B^-,B^+)\ge1.       \tag{6.4}
\]

#### Proof

Put the forced gained-minus-lost activity in a constant `c_0`.  Give optional
SCC `C` reward equal to the number of lost optional cells lying in `C`.  Give
each nonforced gained cell one auxiliary node of cost one.  Add infinite-
capacity implications `C->D` for (6.1), and `C->y_c` whenever
`C in K(Gamma(c))`.  A closed set has weight

\[
 \sum_C w_Cx_C-\sum_c y_c,
\]

and, because the auxiliary weights are negative, it selects `y_c` exactly
when at least one of its predecessor SCCs is selected.  Maximizing this
closed-set weight is the standard source-sink minimum-cut construction.  Its
negative, plus `c_0`, is (6.3).  The construction is integral.  The cut's
selected target SCCs reconstruct a literal blocking shore by Theorem 5.1.
Finally (6.4) is exactly (4.7).  \(\square\)

Checking only the two canonical lattice extremes, or only individual sink
generators, is unsafe.  For example

\[
             1+\operatorname{OR}(x_1,x_2)-x_1-x_2  \tag{6.5}
\]

has value one on the empty choice and either singleton but value zero on the
pair.  A nonsink can similarly create a blocking filter not visible in sink-
only tests.

There is a concrete H25 warning.  The five canonical shores inherited from
the descent are nested,

\[
 X_{25}\subset X_{26}\subset X_{27}\subset X_{28}\subset X_{29}, \tag{6.6}
\]

and all five have deficiency 25 in H25.  Their sizes are

\[
 (1320,1295),(1480,1455),(1484,1459),(1489,1464),(1524,1499). \tag{6.7}
\]

For the inverse move `H25->H26`, the current is `-1` on
`X_26,X_27,X_28,X_29`, zero on `X_25`, and `+1` on the canonical maximum
shore.  Thus even opposite behaviour at the minimum and maximum shores does
not determine the answer.

For a fixed materialized endpoint, (6.3) is the compact first separator.
The complete descent oracle is still (4.5), equivalently one maximum matching
in the final graph.  The retained H25 scan records the scalar matching score,
not which slack-zero or near-critical shore blocks each candidate.

### 6.1 Certified two-braid portal escape

Let `G_0,G_1,G_2` be the compiler graphs of H25, the portal state, and H24 in
(1.7).  Exact reconstruction gives

\[
                  D(G_0),D(G_1),D(G_2)=25,25,24.    \tag{6.8}
\]

At all three states:

* all `6435` rank-eight masks occur exactly once;
* the chronology is a Johnson path and is depth-three resident;
* every upper support at depths `1,...,7` is complete;
* the lower-hole vector is exactly `(4,19,4,1,0,0,0)`;
* the seven zero-candidate targets are unchanged.

In the direct H25-to-H24 full-neighbourhood-profile cancellation, let `H` be
the common cell-profile multigraph and let `B^-`,`B^+` be the two residual
banks; write `R(H)` for its right-cell multiset.  For any boundary bank define

\[
            \operatorname{cap}_H(B)=\nu(H\sqcup B)-\nu(H). \tag{6.8a}
\]

Without assuming that the two braid columns add independently, exact
reconstruction gives

\[
 |R(H)|=19253,\qquad |B^-|=|B^+|=58,               \tag{6.9}
\]

and

\[
 \nu(H)=16323,\qquad
 \operatorname{cap}_H(B^-)=35,\qquad
 \operatorname{cap}_H(B^+)=36.                    \tag{6.10}
\]

Thus the final compound has one unit of additional contracted occurrence
capacity.  Equations (4.4)--(4.5) prove, without enumerating the maximum-shore
lattice, that

\[
 J_{02}(X):=|N_{G_2}(X)|-|N_{G_0}(X)|,
 \qquad
 J_{02}(X)\ge1
 \qquad\text{for every H25 maximum-deficiency shore }X. \tag{6.11}
\]

This is the requested simultaneous opening theorem.

The moving-shore mechanism is visible in the exact gap matrix.  If
\(X_0,X_1,X_2\) are the canonical DM shores of the three successive states,
then

\[
 \begin{pmatrix}
 |X_j|-|N_{G_i}(X_j)|
 \end{pmatrix}_{i,j=0}^2
 =
 \begin{pmatrix}
 25&24&23\\
 22&25&24\\
 21&24&24
 \end{pmatrix}.                                    \tag{6.12}
\]

The first braid opens the old canonical shore by three units but creates a
different gap-25 shore.  Its contracted boundary rank is neutral, `15->15`.
The second changes its contracted boundary rank `20->21`, lowers the global
maximum, and leaves two different gap-24 shores.  Therefore no monotone rule
which follows one fixed DM shore can prove the descent.

The composition in (1.7) is a literal integral segment reconnection and hence
has the alternating-cycle representation of Theorem 2.1.  The proof above
uses its exact final boundary bank (6.9), so it remains valid whether the two
sequential dependency collars are viewed as disjoint atoms or as one
contracted macro-collar.

What (6.11) does not prove is Hall zero or physical literalization.  H24 still
has seven zero-candidate targets, violates the necessary prefix corridor
(1.4), and has no audited injective target assignment satisfying the common-
word criterion below.

A separate certified two-braid Pareto branch has score

\[
                  (25,7)\longrightarrow(26,6)\longrightarrow(25,6), \tag{6.13}
\]

where the second coordinate is the number of zero-candidate targets.  It
creates a first candidate for target `2575`, but it has not been combined
with H24.  Hence the current data exhibit both required kinds of motion—DM
portal capacity and zero-target creation—on different integral branches,
not one common-word-compatible branch.

## 7. One-common-word compatibility

Fix one final integral segment reconnection `rho`, its chronology `T^rho`,
and the controller `P^rho` from (3.1).  Let `C` be the `19311` lower cells.
For every lower target `S`, choose binary assignment variables

\[
 \sum_c y_{S,c}=1,\qquad \sum_Sy_{S,c}\le1.        \tag{7.1}
\]

Only individually legal target/cell incidences may have `y_{S,c}=1`.  Put all
selected assignments and every fixed seam, endpoint, old, protected, and
reserved interval equality in one interval-label family `L`, and put every
additional positive-only demand in `Pi`.  For each coordinate `x`, define the
maximal allowed positions

\[
 \widehat H_x=
 \{p:x\in P^\rho_p\}
 \setminus
 \bigcup_{\substack{(I,S)\in\mathcal L\\x\notin S}}I. \tag{7.2}
\]

### Theorem 7.1 (maximal common-word criterion)

There is one nonzero physical word `A_0,...,A_{W+2}` realizing the final
middle deck, every selected interval label, and every positive-only demand in
`Pi` if and only if

\[
 \{i:x\in T^\rho_i\}
 =\bigcup_{p\in\widehat H_x}
       ([p-3,p]\cap[0,W-1])                         \tag{7.3}
\]

for every coordinate `x`,

\[
(p,x)\in\Pi\quad\Longrightarrow\quad p\in\widehat H_x, \tag{7.4}
\]

\[
x\in S\quad\Longrightarrow\quad
                  \widehat H_x\cap I\ne\varnothing \tag{7.5}
\]

for every `(I,S) in L`, and

\[
                 \{x:p\in\widehat H_x\}\ne\varnothing \tag{7.6}
\]

for every physical position `p`.  When these hold, the maximal word

\[
                         A_p=\{x:p\in\widehat H_x\} \tag{7.7}
\]

works.

#### Proof

Every negative interval equality forces the deletions in (7.2), so any word
is contained coordinatewise in (7.7).  Equation (7.3) says exactly that the
four-position dilation of (7.7) is the prescribed middle chronology.
Equation (7.4) supplies the positive-only pins, and (7.5) supplies every
positive coordinate in every selected target, while the negative coordinates
were already excluded by (7.2).  Equation (7.6) makes every physical letter
nonzero.  Hence (7.7) realizes all equalities.  Conversely, any realizing
word is contained in (7.7).  Enlarging it to (7.7) preserves every positive
hit and nonzero letter, while `widehat H_x` is still contained in the maximal
controller positions `{p:x in P^rho_p}` and therefore creates no false
central occurrence.  Its central and selected positive hits now imply
(7.3)--(7.6).  \(\square\)

For an internal controller run, (7.3) is equivalent to retaining both run
endpoints and leaving gaps at most four between consecutive allowed
positions, with the corresponding one-sided rules at the two global ends.
This gives a finite boundary signature for concatenating truly disjoint
collars: first allowed position, last allowed position, largest internal gap,
and every pending positive interval obligation.  Two locally feasible collar
words need not compose unless these signatures also compose.  They may
delete different points of one long coordinate run and jointly create a gap
larger than four.

The injectivity in (7.1) is exact Boolean ownership.  A trace-two bound is a
useful sufficient compression in other package theorems, but is not a
necessary condition in this minimal H25 formulation.

## 8. TU boundary and the exact master

For a fixed segment orientation, the bare port degree equations are an
assignment/network system.  Three additions prevent a generic TU conclusion:

1. one-component subtour conditions for the segment order;
2. the nonlinear neighbourhood activation represented by the Hall Benders
   rows;
3. common-word interval blockers shared by target assignments.

For the last item, let a required coordinate have a finite allowed set `R`.
Every minimal family `F` of selected negative pin intervals covering `R`
gives

\[
                         \sum_{e\in F}y_e\le |F|-1. \tag{8.1}
\]

For a positive obligation conditional on assignment `e_0`, the row is

\[
                 y_{e_0}+\sum_{e\in F}y_e\le |F|.  \tag{8.2}
\]

Three pair blockers can contain the coefficient minor

\[
 \begin{pmatrix}
 1&1&0\\0&1&1\\1&0&1
 \end{pmatrix},\qquad\det=2.                        \tag{8.3}
\]

Thus no class-level theorem can identify the full collar/assignment/common-
word system with a directed network matrix.  This does not assert that the
particular minor (8.3) occurs in every restricted H25 collar catalogue.

The exact finite master is nevertheless clean:

* integral seam variables satisfying the port degrees, Johnson eligibility,
  and one-cycle constraints;
* integral macro-collar variables for every overlapping dependency cluster;
* the shared cross-depth rows (4.11), residence, and the necessary corridor
  (1.4);
* Hall Benders rows (4.10), separated by Theorem 6.1 on the maximum-shore
  face and by exact final matching on all slack shells;
* integral target/cell variables (7.1) and the deterministic common-word
  test (7.2)--(7.6).

For any integral master point these tests are necessary and sufficient for
the advertised fixed-carrier compiler.  Fractional feasibility is only a
lower bound; (8.3) explains why ordinary flow rounding is not a proof.

## 9. Precise surviving gate

The Hall-layer construction is now positive:

* the topological part of a multi-collar move is an exact integral
  alternating-cycle circulation;
* disjoint full boundary signatures add across every protected stratum;
* all `at least 2^5760` H25 maximum shores have one exact integral min-cut
  separator;
* the concrete two-braid circulation (1.7) passes the complete all-shore
  criterion (4.5), as certified by its final matching, and reaches Hall 24;
* the common-word condition has a necessary-and-sufficient deterministic
  test after the integral target assignment is fixed.

What remains is not existence of a Hall-improving compound.  It is to continue
the portal mechanism until (4.6), while the same chronology enters (1.4) and
admits one target assignment passing Theorem 7.1.  The certified H24 endpoint
still has deficiency 24, seven zero-candidate targets, `h_1=4`, and `h_2=19`.
Thus it is a strict cross-stratum rounding advance but not a length-6438
word.  The sharp conclusion is:

\[
 \boxed{\text{H25 is a one-collar minimum but not a compound minimum:
 an integral two-braid opens every tight shore and reaches H24; common-word
 completion remains open.}}
\]

## 10. Sources and audit boundary

The chronology, descent, and one-move census are in

* `MATH_K15_THREE_CUT_SEGMENT_BRAID_DESCENT_20260728.md`;
* `scratch/k15_segment_braid_hall25.json`;
* `scratch/audit_k15_segment_braid_descent.py`;
* `scratch/threadD_k15_segment_braid_descent_audit.json`.

The positive compound is frozen in

* `MATH_K15_TWO_BRAID_DM_PORTAL_ESCAPE_20260728.md`;
* `scratch/k15_segment_braid_hall25_portal.json`;
* `scratch/k15_segment_braid_hall24.json`;
* `scratch/k15_segment_braid_hall24_portal_audit.json`;
* `scratch/audit_threadD_h25_h24_compound.py`;
* `scratch/threadD_h25_h24_compound_audit.json`.

The signed-current identity originates in
`THREAD_H_K15_TETRAHEDRAL_SEGMENT_BRAID_HALL_DESCENT_20260728.md`.
The common-word criterion is the controller form of
`MATH_EROSION_JOHNSON_CONTROLLER_DUALITY_20260728.md` and
`THREAD_D_EXACT_SHADOW_BRAID_INDUCTION_AND_CUT_AWARE_OBSTRUCTION_20260728.md`.

The residual-DM SCC counts and the inverse-current values in Sections 5--6
were independently reconstructed from the H25 graph during this audit.  They
are exact finite census statements.  No claim is made that the stored scalar
one-move scan identifies the blocking shore of every safe move.  The positive
claim is exactly the outer Hall-24 compound in Section 6.1; no common-word
target assignment or coefficient-one word is claimed.
