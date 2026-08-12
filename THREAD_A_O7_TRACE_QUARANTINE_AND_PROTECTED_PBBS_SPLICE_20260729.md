# Thread A: the `O_7` trace collapse and a protected PBBS segment-splice theorem

Date: 2026-07-29

Status: pure theorem and sharply finite sufficient condition.  No existence
of the final splice is claimed.  The trace-quarantine theorem reduces the
immediate carrier problem to turn coverage, while the PBBS factor supplies
all required turn/flag witnesses before fusion.  A native-order segment
splice preserves those witnesses exactly when one of their canonical
intervals avoids the cut set.  The remaining finite gates are a protected
cut transversal, an odd-graph endpoint connector cycle, and ten local label
tests per seam.

## 1. Odd-graph notation and the global collapse

Let

\[
 \mathcal V=\binom{[15]}7,\qquad W=|\mathcal V|=6435,
 \qquad C=\operatorname{Cat}_7=429,
\]

and let `O_7=KG(15,7)`.  For an oriented odd-graph cycle

\[
 H=(A_0,A_1,\ldots,A_{W-1},A_0),
\]

write

\[
 z_j=[15]\setminus(A_j\cup A_{j+1})                 \tag{1.1}
\]

for its edge label and

\[
 \chi_j=A_{j-1}\cap A_{j+1}\in\binom{[15]}6        \tag{1.2}
\]

for its turn colour.  The label in (1.1) is a singleton, which we identify
with its element.

### Lemma 1.1 (odd return gaps)

On every simple odd-graph cycle, consecutive occurrences of a fixed edge
label have odd cyclic gap at least three.  Consequently (1.4) is equivalent
to saying that every consecutive same-label gap is at least seven.

#### Proof

Fix a coordinate `x` and put

\[
                         u_j=\mathbf1_{\{x\in A_j\}}.
\]

Adjacent odd-graph vertices are disjoint, so the cyclic binary word `u` has
no `11`.  Since two adjacent seven-sets have union of size fourteen,

\[
                         z_j=x\quad\Longleftrightarrow\quad
                         (u_j,u_{j+1})=(0,0).
\]

Between two consecutive `x`-labelled edges there is no other `00`; together
with the absence of `11`, the intervening bits alternate.  Starting and
ending with `00` therefore gives an odd edge gap.  Gap one would make the two
neighbours of `A_(j+1)` both equal to
`A_(j+1)^c\setminus\{x\}`, contradicting simplicity.  Hence the gap is odd
and at least three.  Excluding gaps three and five is exactly the asserted
minimum seven. \(\square\)

For a Hamilton cycle, every symbol occurs as an edge label exactly

\[
 W-2\binom{14}{6}=6435-6006=429                  \tag{1.2a}
\]

times: its vertex-membership word has `binom(14,6)` ones, no `11`, and its
`00` edges are precisely the occurrences of that label.  Thus the average
same-symbol gap is 15.  Conditions (1.4) have no scalar histogram
obstruction.

### Theorem 1.2 (odd-graph carrier collapse at `k=15`)

Suppose `H` is Hamiltonian and satisfies

\[
 \{\chi_j:j\in\mathbb Z_W\}
 \supseteq\binom{[15]}6,                              \tag{1.3}
\]

and

\[
 z_j\ne z_{j+3},\qquad z_j\ne z_{j+5}
 \qquad(j\in\mathbb Z_W).                            \tag{1.4}
\]

Define, using that multiplication by two permutes `Z_W`,

\[
 X_i=A_{2i},\qquad T_i=\overline{A_{2i-1}}.          \tag{1.5}
\]

Then:

1. `T` is a Hamilton cycle of `J(15,8)` and
   \[
   T_i\cap T_{i+1}=X_i;
   \]
   hence its immediate lower intersections are every rank-seven set
   exactly once;
2. its adjacent unions cover every rank-nine set;
3. the associated Middle Levels cycle is complement coherent, with
   complementation acting as its half-turn;
4. `T` is cyclically depth-three resident; and
5. for every distinguished coordinate, `T` induces the exact decorated
   four-level quarantine of
   `MATH_THEOREM_TRACE_QUARANTINE_COLLAPSE_20260729.md`.  In particular the
   intrinsic first-band ownership and the port matching carried by its own
   cross seams are automatic.  This does not say that `T` extends either
   member of a pair of preselected GMM forests.  Its channel census is
   \[
   (AA,AB,BB)=(3003,858,2574),
   \]
   with 2,002 selectable protected `BB` occurrences and 572 merge `BB`
   edges.

#### Proof

Consecutive odd-graph owners are disjoint.  The two sets
`A_(2i-1),A_(2i+1)` are distinct seven-subsets of the eight-set
`overline(A_(2i))`; their union is that eight-set.  Therefore

\[
 T_i\cap T_{i+1}=A_{2i}=X_i.                         \tag{1.6}
\]

The `X_i` enumerate `V`, proving item 1.  De Morgan gives

\[
 \overline{T_i\cup T_{i+1}}
   =A_{2i-1}\cap A_{2i+1}=\chi_{2i}.                 \tag{1.7}
\]

Since the even residues also enumerate `Z_W`, (1.3) is exactly complete
adjacent-union coverage, proving item 2.  The standard bipartite
double-cover lift of an odd cycle of odd length is one cycle, and its second
half is the complement of its first.  This proves item 3.

The step-two Johnson transition of `T` inserts `z_(2i)` and later deletes
`z_(2i+2t-1)`.  Thus depth-three residence is exactly the inequality of
these labels for `t=1,2,3`.  The `t=1` equality would repeat an odd-graph
vertex after two steps and is impossible; the other two inequalities are
(1.4).  This proves item 4.  Items 1 and 2 say precisely that `T` is a
q1-perfect global middle carrier, so the trace-quarantine collapse theorem
gives item 5. \(\square\)

This theorem is stronger than a two-forest splice reduction: once (1.3)
holds on one global Hamilton cycle, no separate rankwise port Hall theorem
remains at q1.  It does not supply the deeper flag tower or the exact lower
compiler.  The protected `BB` occurrences may be selected separately after
the final cycle for each distinguished coordinate; the theorem does not
produce one common all-coordinate protected-edge marking.

### Theorem 1.3 (exact finite successor form)

Choose a map

\[
 \ell:\mathcal V\longrightarrow[15],
 \qquad \ell(A)\notin A,                             \tag{1.8}
\]

and put

\[
                         f(A)=A^c\setminus\{\ell(A)\}.\tag{1.9}
\]

The desired `O_7` object exists if and only if one can choose `ell` so that:

1. `f` is one permutation cycle on `V`;
2. the values
   \[
   \tau(A)=A^c\setminus
      \{\ell(f^{-1}A),\ell(A)\}                      \tag{1.10}
   \]
   cover every six-set; and
3. cyclically for every `A`,
   \[
   \ell(A)\ne\ell(f^3A),\qquad
   \ell(A)\ne\ell(f^5A).                            \tag{1.11}
   \]

#### Proof

Every oriented odd-graph edge from `A` has the unique form (1.9), so a
Hamilton cycle gives and is given by items 1 and (1.8).  At centre `A`, its
predecessor and successor are the two seven-subsets of `A^c` obtained by
deleting the incoming and outgoing labels.  Their intersection is (1.10).
The outgoing label at cyclic distance `h` is `ell(f^hA)`, so (1.11) is
exactly (1.4), including wraparound. \(\square\)

Theorem 1.3 has only eight local successor options at each owner, but its
one-cycle and turn-support conditions are global.  It is an exact finite
normal form, not an existence proof.

## 2. The audited PBBS input

Let `f` be the canonical PBBS permutation of `V`.  Its directed arcs

\[
                         A\longrightarrow f(A)       \tag{2.1}
\]

form an oriented cycle factor `F` of `O_7`.  Every `f`-orbit length is a
multiple of 15.  Consequently, if `p` is the number of PBBS components,

\[
                              p\le W/15=C=429.        \tag{2.2}
\]

For `1<=q<=7` and

\[
 S\in\binom{[15]}{7-q},
\]

let `I_q(S)` be the family of directed `2q`-edge PBBS intervals

\[
 I=(B_0,f(B_0),f^2(B_0),\ldots,f^{2q}(B_0))          \tag{2.3}
\]

such that

\[
                 \bigcap_{t=0}^{q}f^{2t}(B_0)=S.    \tag{2.4}
\]

The audited all-depth PBBS theorem gives

\[
 1\le|\mathcal I_q(S)|\le\binom{2q+1}{q}.           \tag{2.5}
\]

For `q=1`, the interval in (2.3) has turn centre `f(B_0)`, and (2.4) is
exactly its colour (1.2).  Thus the unfused PBBS factor already has complete
turn support.

The audited PBBS return classification also gives:

1. its edge-label words have no same-label gap three; and
2. they have exactly
   \[
                      15(7-1)=90                    \tag{2.6}
   \]
   same-label gap-five starts.

Let `R_5` be the corresponding family of closed six-edge cyclic intervals

\[
 (e_j,e_{j+1},\ldots,e_{j+5})\quad
 \text{with }z(e_j)=z(e_{j+5}).                     \tag{2.7}
\]

All statements in this section concern the genuine PBBS factor, not a
generic odd-graph factor.

## 3. Native-order segment splices

Let `D\subset E(F)` contain at least one directed edge from every PBBS
component.  Deleting `D` gives exactly `s=|D|` directed path segments,
including singleton segments when two cuts are adjacent.  On a segment `P`,
write `a(P)` and `b(P)` for its initial and terminal vertices in the native
PBBS orientation.

### Definition 3.1 (connector certificate)

A connector certificate for `D` is a cyclic ordering

\[
                         P_0,P_1,\ldots,P_{s-1}      \tag{3.1}
\]

of all path segments such that

\[
                         b(P_i)\cap a(P_{i+1})=\varnothing
                         \quad(i\in\mathbb Z_s),     \tag{3.2}
\]

and the added odd-graph edges in (3.2), together with `F-D`, form a simple
cycle.  Denote that cycle by `H(D,P)`.  Thus a certificate is equivalently a
directed Hamilton cycle in the auxiliary digraph on the `s` segments, with
an arc `P->Q` when `b(P)` and `a(Q)` are disjoint, subject only to excluding
a reused retained edge.

This is a finite endpoint problem on at most `s` objects.  Native direction
is essential for the PBBS flag-survival statement below; allowing a reversed
segment requires a separately audited reverse flag bank.

### Proposition 3.2 (exact cut-tail permutation certificate)

Let `R` be the set of cut tails, so

\[
                         D=\{x\mathbin{\to}f(x):x\in R\}.
\]

Let `rho:R->R` send `x` to the next cut tail encountered when one follows
the old PBBS component from `f(x)`.  For a permutation `theta` of `R`,
extended identically off `R`, put

\[
 f_\theta(x)=
 \begin{cases}
 f(\theta x),&x\in R,\\
 f(x),&x\notin R.
 \end{cases}                                         \tag{3.3}
\]

Then `f_theta` is a spanning functional odd-graph cycle cover exactly when

\[
                         x\cap f(\theta x)=\varnothing
                         \qquad(x\in R).              \tag{3.4}
\]

If it has no directed two-cycle, this functional cover is also a simple
undirected odd-graph `2`-factor.  After contracting the retained PBBS
segments, its successor permutation on
their terminal cut labels is

\[
                              \rho\circ\theta.        \tag{3.5}
\]

Consequently `f_theta` is Hamiltonian exactly when (3.4) holds and
`rho theta` is one cycle.  Every native-order connector certificate is of
this form.

#### Proof

The old outgoing heads at cut tails are the distinct vertices `f(R)`.
Equation (3.3) merely permutes these heads, so indegree and outdegree remain
one everywhere.  It is a functional odd-graph cycle cover precisely when
every new tail and head are disjoint, which is (3.4).  A directed two-cycle
uses one undirected edge twice; excluding these is exactly the additional
condition needed for a simple undirected `2`-factor.

The retained segment beginning at `f(y)` terminates at `rho(y)`.  From a
terminal cut tail `x`, the new edge enters the segment beginning at
`f(theta x)`, whose terminal cut label is `rho(theta x)`.  Thus contraction
gives (3.5).  A functional spanning cycle cover is one Hamilton cycle exactly
when this contracted permutation is one cycle.  Conversely every
native-order connector bijects the cut tails with the old heads `f(R)`, and
hence determines a unique `theta`. \(\square\)

### Corollary 3.3 (no two-tail coherent fusion)

No nontrivial two-tail head permutation is legal.  Hence the smallest local
native-order odd-graph reconnection has at least three cut tails.

#### Proof

A nontrivial permutation of two tails swaps their heads.  If both new edges
were legal, any coincidence among the four endpoints would create a loop or
repeat an old factor vertex; otherwise the two old and two new edges would
form a `C_4` in `O_7`.
There is no such cycle: two distinct seven-sets have union of size at least
eight, whose complement has size at most seven, so they cannot have two
distinct common disjoint seven-set neighbours. \(\square\)

### Lemma 3.4 (turn and flag locality)

Let `H=H(D,P)` be a connector certificate.

1. A turn centre not incident with a deleted edge has exactly the same two
   neighbours and the same turn colour in `F` and `H`.
2. If `I in I_q(S)` satisfies
   \[
                              E(I)\cap D=\varnothing,\tag{3.6}
   \]
   then the same directed interval occurs in `H`; hence the `q`-step
   intersection flag with value `S` survives.

#### Proof

Only endpoints of the paths `F-D` acquire new neighbours, proving item 1.
Condition (3.6) places the whole interval (2.3) inside one retained directed
segment.  Its order and all its vertices are therefore unchanged in `H`,
which proves item 2. \(\square\)

The exact turn-support criterion after a fixed splice is consequently

\[
 \begin{split}
 \binom{[15]}6\subseteq{}&
 \{\chi_F(v):v\text{ is incident with no edge of }D\}\\
 &\cup\{\chi_H(v):v\text{ is incident with an edge of }D\}.
                                                               \tag{3.7}
 \end{split}
\]

A simpler sufficient condition, independent of the new endpoint turns, is

\[
 \boxed{
 \forall S\in\binom{[15]}6\quad
 \exists I\in\mathcal I_1(S):E(I)\cap D=\varnothing.}          \tag{3.8}
\]

### Proposition 3.4a (exact flag-load transport)

In the cut-tail model of Proposition 3.2, put

\[
 \pi_0=f^2,\qquad \pi_\theta=f_\theta^2,
 \qquad
 \Delta_\theta=\{A:\pi_\theta(A)\ne\pi_0(A)\}.      \tag{3.8a}
\]

Then

\[
 \Delta_\theta\subseteq R\cup f^{-1}(R).            \tag{3.8b}
\]

For `q>=1`, define

\[
 \mathcal J_q=
 \bigcup_{h=0}^{q-1}\pi_0^{-h}(\Delta_\theta),
 \qquad |\mathcal J_q|\le2q|R|,                     \tag{3.8c}
\]

and

\[
 \Phi_q^\eta(A)=\bigcap_{h=0}^{q}\pi_\eta^h(A)
 \qquad(\eta\in\{0,\theta\}).
\]

If `mu_q^eta(S)` is the load of target `S` in this row, then exactly

\[
\boxed{
 \mu_q^\theta(S)=\mu_q^0(S)
 -|\{A\in\mathcal J_q:\Phi_q^0(A)=S\}|
 +|\{A\in\mathcal J_q:\Phi_q^\theta(A)=S\}|.}       \tag{3.8d}
\]

#### Proof

The first `f_theta` step differs from `f` only at `R`; the second can also
differ when its first image lies in `R`.  This proves (3.8b).  If
`A notin J_q`, none of the first `q` old step-two states lies in
`Delta_theta`.  Induction gives

\[
 \pi_\theta^h(A)=\pi_0^h(A)\qquad(0\le h\le q),
\]

so all starts outside `J_q` cancel in the difference of the two load
functions.  The remaining starts give (3.8d), and the union bound with
`|Delta_theta|<=2|R|` gives (3.8c). \(\square\)

Thus targetwise positivity of the right side of (3.8d) is necessary and
sufficient for support after a fixed head permutation.  The protected-bank
condition (3.8) is a convenient stronger certificate.  The PBBS upper load
cap does not permit replacing (3.8d) by a scalar estimate, because some
target fibres may be singletons.

### Lemma 3.5 (distance-three/five collar locality)

Assume `D` meets every interval in `R_5`.  Then every equality

\[
 z_H(j)=z_H(j+3)\quad\text{or}\quad z_H(j)=z_H(j+5)              \tag{3.9}
\]

in the spliced cycle has its closed intervening edge interval meeting an
added connector edge.  Conversely, if all such connector-crossing intervals
pass (3.9) with inequality, the spliced label word avoids distances three
and five.

There are at most

\[
                               (3+1)+(5+1)=10         \tag{3.10}
\]

ordered interval tests per connector edge.

#### Proof

An interval of the new cycle which contains no connector lies wholly inside
one native PBBS segment.  At distance three it is safe by the PBBS
no-gap-three theorem.  At distance five it is safe because any old bad
six-edge interval was hit by `D` and therefore cannot lie wholly in a
retained segment.  This proves the first assertion and the converse.

For a fixed connector and offset `h`, exactly `h+1` possible starts have
that connector in their closed `h`-edge interval.  Sum over `h=3,5` to get
(3.10). \(\square\)

### Corollary 3.6 (unavoidable and available cut scales)

Every native-order PBBS segment splice satisfying (1.4) must have

\[
                              |D|\ge15.              \tag{3.11}
\]

It also has `|D|>=p`.  On the other hand, without imposing flag survival or
connector feasibility, there is always a component-and-gap hitting set with

\[
                              |D|\le p+90\le519.     \tag{3.12}
\]

#### Proof

The cut set must meet all 90 six-edge intervals in `R_5`, by Lemma 3.5.
One edge lies in at most six such intervals, proving (3.11).  At least one cut
is needed to open each old component.  For (3.12), take one arbitrary edge
from every old component and one edge from every member of `R_5`, then
discard repetitions. \(\square\)

The lower bound (3.11) is scoped to splices which preserve the PBBS order
inside segments.  A general odd-graph Hamilton cycle need not be measured by
this cut set.

The PBBS turn word has `6435-5005=1430` excess occurrences.  A raw cut set
at the upper scale (3.12) touches at most `2|D|<=1038` old turn centres, so
there is aggregate slack 392.  This rules out a mere cardinality obstruction
but proves no protected transversal: the touched centres may include unique
target occurrences.  Corollary 3.3 and (3.11) also show that a construction
using a static family of disjoint three-tail `C_6` reconnections, whose final
cut set is the union of their original PBBS tails, needs at least five such
circuits.  This does not cover a sequential overlapping schedule which
leaves the native-segment model.

## 4. The finite protected-splice theorem

### Theorem 4.1 (q1 protected PBBS fusion)

Suppose there are a cut set `D` and connector certificate `P` satisfying:

1. `D` contains an edge of every PBBS component;
2. `D` meets every one of the 90 intervals in `R_5`;
3. the at most `10|D|` connector-crossing tests of Lemma 3.5 all have
   unequal endpoint labels; and
4. the protected turn condition (3.8) holds, or more generally the exact
   endpoint-repair condition (3.7) holds.

Then `H(D,P)` is an `O_7` Hamilton cycle whose turn colours cover every
six-set and whose edge-label word avoids distances three and five.  Its
Middle Levels lift is complement coherent, q1-perfect, depth-three resident,
and supplies the exact intrinsic every-coordinate decorated quarantine of
Theorem 1.2.  It need not be compatible with any preselected GMM forests.

#### Proof

The connector certificate is Hamiltonian by definition.  Lemma 3.4 and
condition 4 give complete turn support.  Conditions 2 and 3, together with
the PBBS no-gap-three theorem, give (1.4) by Lemma 3.5.  Theorem 1.2 gives
all conclusions about the lifted carrier. \(\square\)

### Theorem 4.2 (optional preservation of complete PBBS flag support)

Under the hypotheses of Theorem 4.1, assume additionally that

\[
 \boxed{
 \forall q\in\{1,\ldots,7\},\quad
 \forall S\in\binom{[15]}{7-q},\quad
 \exists I\in\mathcal I_q(S):E(I)\cap D=\varnothing.}         \tag{4.1}
\]

Then the step-two order of `H(D,P)` has complete lower flag support at every
depth.  By complement coherence, its lifted rank-eight chronology has the
complete upper flag tower as well.

#### Proof

Lemma 3.4 preserves the selected occurrence for every pair `(q,S)` in
(4.1).  These are exactly the descending odd-graph flags.  The all-depth
complement identity carries lower depth `q+1` support to upper depth `q`,
proving the second assertion. \(\square\)

Condition (4.1) is sufficient, not necessary: a connector collar may create
a replacement occurrence for a PBBS flag whose old occurrences were all
cut.

## 5. A sharply finite certificate and its exact obstruction

The cut-and-witness part of Theorem 4.2 has an exact finite formulation.
Use a binary variable `x_e` for every PBBS edge and a witness variable
`y_(q,S,I)` for every `I in I_q(S)`.  Require

\[
 \sum_{e\in E(K)}x_e\ge1
 \qquad(K\text{ a PBBS component}),                 \tag{5.1}
\]

\[
 \sum_{e\in R}x_e\ge1
 \qquad(R\in\mathcal R_5),                          \tag{5.2}
\]

and

\[
 \sum_{I\in\mathcal I_q(S)}y_{q,S,I}\ge1,
 \qquad
 y_{q,S,I}\le1-x_e\quad(e\in E(I)).                \tag{5.3}
\]

For q1 only, (5.3) has 5,005 target rows.  For the full tower it has

\[
 \sum_{j=0}^{6}\binom{15}j
 =1+15+105+455+1365+3003+5005
 =9949                                                   \tag{5.4}
\]

target rows, and each row has at most the number of candidates in (2.5).
No marginal or probabilistic interpretation is present: (5.1)--(5.3) are
literal component, gap, and protected-occurrence conditions.

If (5.1)--(5.3) are feasible, they have a solution with at most `p+90<=519`
cuts.  Indeed, from any feasible cut set retain one of its edges for each
component clause and one for each gap-five clause, discarding repetitions.
Passing to this subset cannot destroy an uncut witness in (5.3).  This
shrinking argument applies only to the cut-and-witness subsystem; the
smaller endpoint system need not retain a connector Hamilton cycle.

After a solution `D` is fixed, connector feasibility is exactly a directed
Hamilton-cycle problem on the `s=|D|` native segments, followed by at most
`10s` label comparisons.  If one of the at-most-519 protected cut sets above
also admits a connector, this auxiliary problem has at most 519 vertices and
5,190 label tests.  The shrinking argument does not prove that connector
feasibility can always be retained at that scale; a more highly cut
connector remains possible.

This yields three exact, reusable scoped obstructions:

1. if (5.1)--(5.3) are infeasible, no native-order PBBS segment splice can
   simultaneously hit every gap-five return and preserve the selected PBBS
   flag tower;
2. if they are feasible but every corresponding endpoint digraph lacks a
   directed Hamilton cycle, the obstruction is connector topology, not
   shadow support; and
3. if a connector cycle exists but every one fails a collar comparison, the
   obstruction is precisely residence at a new seam.

Failure of this finite class would not rule out a non-PBBS `O_7` Hamilton
cycle or a fusion which deliberately destroys and recreates protected
turns/flags.

## 6. Complement pairing is automatic downstairs

### Proposition 6.1 (odd-graph fusion is the correct antipodal quotient)

Every `O_7` cycle of odd length lifts to one complement-antipodal Middle
Levels cycle.  Every even odd-graph cycle lifts to two Middle Levels cycles
exchanged by complementation.  If odd-graph cycles are fused by a native
segment splice to one Hamilton cycle, the lifted result is automatically one
complement-antipodal Hamilton cycle; every connector edge lifts with its
complementary incidence seam.

#### Proof

The Middle Levels graph is the bipartite double cover of the odd graph.  The
lift of a base cycle is connected exactly when its length is odd.  In the
connected case, the deck involution is the half-turn; in the disconnected
case, it exchanges the two lifts.  The connector statement follows because
the double-cover functor lifts every base edge together with its deck mate.
Finally `W=6435` is odd, so the lift of a Hamilton base cycle is connected.
\(\square\)

Thus PBBS components should not be fused independently on one Middle Levels
shore.  Such an upstairs operation requires an explicit antipodal mate and
can break complement coherence.  Fusing them in `O_7` automatically performs
the paired operation.  What is not automatic is protected flag survival:
that is exactly condition (4.1), and the audited PBBS multiplicity theorem
provides only a nonempty candidate family, not a cut-avoiding member.

### Proposition 6.2 (fixed-one-shore switch obstruction)

Identify the rank-eight owner (U_X=X^c) with
(X\in\mathcal V).  For two edge-disjoint incidence matchings `M_0,M_1` put

\[
 a(X)=M_0(U_X),\qquad b(X)=M_1(U_X).                 \tag{6.1}
\]

With the two matching roles fixed, their union is the Middle Levels lift of
an oriented odd-graph factor exactly when

\[
                              a=b^{-1}.              \tag{6.2}
\]

Consequently a switch which holds `M_0` fixed and changes only `M_1` cannot
preserve this complement-coherent quotient structure unless it is trivial.

#### Proof

For an odd-graph successor `g`, the two lower neighbours of `U_X` are
`g^{-1}(X)` and `g(X)`.  In the fixed role convention this says
`a=g^{-1}` and `b=g`, proving necessity.  Conversely, if (6.2) holds, take
`g=b`; incidence of `M_1` says (g(X)\subset X^c), so `g` is an odd-graph
successor and the two matchings are its predecessor/successor lift.  Fixing
`a` in (6.2) fixes `b=a^{-1}`. \(\square\)

Thus the published PBBS paired-`C_6` atlas which switches one fixed matching
solves a different Hamiltonization problem.  A usable connector here must
act on the odd-graph successor itself, as in Proposition 3.2, or switch both
shore maps inversely.

### Proposition 6.3 (the published MNW base join is not a safe collar)

The audited MSW/MNW base `beta`-switch, translated to its odd-graph label
word, creates exactly seven distance-three equalities and three
distance-five equalities.  Its signed turn-colour change is nonzero even
though its turn point degrees cancel.  Hence alternation, component merging,
and the published context compatibility do not imply either condition 3 or
condition 4 of Theorem 4.1.

This is a scoped obstruction: six of those defects remain inside an isolated
radius-five context collar, but later overlapping switches could repair
them.  It rules out importing the MNW joining theorem without a correlated
collar and target-support audit; it does not rule out an appropriately
compound MNW-style schedule or the direct PBBS head-permutation certificate.

## 7. Boundary of the result

The trace-quarantine collapse proves that Theorem 4.1 already closes the
entire q1 quarantine/port interface.  Therefore demanding (4.1) is stronger
than necessary for that immediate carrier theorem.  It becomes relevant
only when one wants to transport the PBBS all-depth support rather than
solve the deeper flags by another construction.

No argument here proves that (5.1)--(5.3) has a solution, that its endpoint
digraph is Hamiltonian, or that all seam collars pass.  The minimum positive
next lemma is consequently one of the following:

* a q1 protected-cut/connector theorem satisfying Theorem 4.1; or
* the stronger all-depth protected-cut/connector theorem satisfying
  Theorem 4.2.

The finite gate is substantially smaller than the original independent-
forest formulation: at q1 it consists of 90 forced return collars, 5,005
protected target rows, one exact `rho theta` subtour test, and ten new label
comparisons per chosen cut tail.  On the unproved raw hitting scale this is
at most 519 segments and 5,190 comparisons.  Exact compiler Hall and a safe
linear cut remain outside this theorem.
