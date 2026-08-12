# Staged residence repair as a coloured alternating-matching problem

Date: 2026-07-27

## 1. Outcome

The residence gate in `K11_K12_OVERLAY_CERTIFICATE_20260727.md` has a clean
exact exchange formulation.  A `k`-opt move is not best viewed as a
permutation of path segments: after the `k` old path edges are cut, it is a
perfect-matching exchange on the `2k` exposed ends.  Hamiltonicity,
lower-colour rainbowness, upper-colour surjectivity, and the staged residence
conditions each become explicit conditions on this small matching.

This yields:

1. a proof-level characterization of every alternating path exchange;
2. a locality theorem for the depth-two and depth-three defects;
3. a necessary hitting-set bound on the order of any one-shot repair; and
4. for the certified `k=11` path, a concrete sequence of colour-preserving
   3-opt improvements reducing the short-run spectrum
   
   \[
   (83,67)\longrightarrow(10,77)
   \]
   
   at lengths two and three.

The resulting path is still not delay-three factorable, but the first stage
is reduced from 83 defects to 10.  Those ten defects have pairwise disjoint
three-edge witness intervals.  Consequently **any single exchange that
removes all ten must cut at least ten old edges**.  This explains why 3-opt
descent stops, and it reduces the next exact search to a coloured perfect
matching on only 20 exposed ends (at most 190 candidate seams), rather than a
new Hamilton-path search on 462 vertices.

The authoritative finite artifacts are:

* `scratch/census_k11_three_opt.cpp`;
* `scratch/k11_q1_threeopt_local_min.txt`;
* `scratch/verify_k11_threeopt_local_min.py`.

No old factor labels need be preserved during this central exchange.  Once a
residence-safe central path is found, the maximal-envelope/interval-stabbing
and Hall machinery can recompile the lower factor.  The central exchange
problem should therefore enforce q=1 colours and residence first, followed
by the independent pin/Hall feasibility audit.

## 2. Ports and the staged residence statistic

Let

\[
P=(T_0,T_1,\ldots,T_{N-1})
\]

be a Hamilton path of `J(n,r)`.  Orient it from left to right and write

\[
T_{i+1}=T_i-\{a_i\}+\{b_i\}.
\]

The lower and upper colours of the edge `i` are

\[
\ell_i=T_i\cap T_{i+1},\qquad u_i=T_i\cup T_{i+1}.
\]

At an internal vertex `T_i`, the incoming edge uses the port `b_{i-1}` and
the outgoing edge uses the port `a_i`.  Thus the cooldown condition has the
particularly local form

\[
b_i\ne a_{i+q}\qquad(1\le q\le d).
\tag{2.1}
\]

Put

\[
L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h},\qquad
\rho_q(P)=\#\{i:L_i^{(q)}=L_{i+1}^{(q)}\}.
\]

The identity in the overlay certificate gives the following staged form.

### Proposition 2.1 (staged cooldown)

If `rho_h(P)=0` for every `h<q`, then

\[
L_i^{(q)}=L_{i+1}^{(q)}
\quad\Longleftrightarrow\quad
b_i=a_{i+q}.
\tag{2.2}
\]

The occurrences counted by `rho_q` are exactly the internal coordinate
one-runs of length `q`.  Hence a lower-rainbow path has `rho_1=0`, and a
delay-three factor exists at the central level exactly when the two remaining
stages `rho_2=rho_3=0` are achieved.

This separates the central work from global shadow balancing: at stage `q`
one forbids only equal *adjacent* cells in the `q`th intersection row.

## 3. The exact seam-reconnection lemma

Choose a set `S` of `k` path edges and delete them.  The old path splits into
`k+1` path components.  Each deleted edge contributes two exposed component
ends, so there is a set `X_S` of `2k` exposed ends.  The two outer components
have one exposed end each; every inner component has two.

Let `A_S` be the graph on `X_S` in which `xy` is an edge precisely when
`x` and `y` are in different components and are adjacent in `J(n,r)`.

### Lemma 3.1 (alternating seam lemma)

A set `M` of new seams produces a Hamilton path on the original vertex set
if and only if:

1. `M` is a perfect matching of `X_S` in `A_S`; and
2. the graph obtained by contracting each old path component and retaining
   the seams in `M` is connected.

When this holds, its lower- and upper-colour multisets are exactly

\[
\begin{aligned}
\mathcal L(P_M)
  &=\bigl(\mathcal L(P)\setminus\{\ell_s:s\in S\}\bigr)
    \uplus\{x\cap y:xy\in M\},\\
\mathcal U(P_M)
  &=\bigl(\mathcal U(P)\setminus\{u_s:s\in S\}\bigr)
    \uplus\{x\cup y:xy\in M\}.
\end{aligned}
\tag{3.1}
\]

#### Proof

Every exposed end must receive exactly one new path edge, which is precisely
the perfect-matching condition.  After contraction, the two outer components
have degree one and every inner component degree two.  There are `k+1`
component vertices and `k` matching edges.  Connectivity therefore makes the
contracted graph a path, and expanding its vertices gives a Hamilton path on
the unchanged central vertex set.  Conversely, every reconnection into one
path necessarily has these properties.  Only the cut edges have changed, so
(3.1) follows.  QED.

The deleted seams themselves form a perfect matching `M_0` on `X_S`.
Therefore `M triangle M_0` is a union of even alternating circuits.  This is
the exact sense in which every path `k`-opt is an alternating-circuit move.

### Corollary 3.2 (q=1 constraints on the small matching)

Suppose the old lower colours are all distinct and omit only `C_*`.  Put

\[
R_S=\{\ell_s:s\in S\}.
\]

Then the reconnected path is lower-rainbow if and only if its `k` new lower
labels are distinct and lie in

\[
R_S\cup\{C_*\}.
\tag{3.2}
\]

The unique unused member of this `(k+1)`-set is the new lower hole.  If
`m_P(U)`, `r_S(U)`, and `n_M(U)` denote the old, removed, and new
multiplicities of an upper colour `U`, upper surjectivity is equivalent to

\[
m_P(U)-r_S(U)+n_M(U)\ge1
\qquad\hbox{for every }U.
\tag{3.3}
\]

Thus all q=1 constraints are checked on the `k` matching edges.  In the
strong colour-exact version, the new and old lower multisets and the new and
old upper multisets agree; such alternating circuits can be composed without
any q=1 bookkeeping at all.

## 4. Residence is local at the seams

An internal one-run of length `q`, born at transition `i`, occupies the
vertices

\[
T_{i+1},\ldots,T_{i+q}
\]

and has the zero boundary transitions `i` and `i+q`.  Associate to it the
`(q+1)`-edge witness interval

\[
I_{i,q}=\{i,i+1,\ldots,i+q\}.
\tag{4.1}
\]

### Lemma 4.1 (uncut defects persist)

If a seam reconnection uses a cut set `S` disjoint from `I_{i,q}`, then the
corresponding length-`q` internal one-run persists in the new path.

#### Proof

The whole binary substring `0,1,...,1,0` lies inside one uncut path
component.  Reconnection either retains or reverses that component.  The
substring, and hence the run, survives in either orientation.  QED.

Consequently, a one-shot repair of all stage-`q` defects requires `S` to be a
hitting set for their witness intervals.

There is also an exact positive locality statement.  All old shadow-repeat
indicators whose `(q+1)`-edge windows avoid the cuts are unchanged (up to
reversal).  Every changed indicator lies within distance `q` of a new seam.
Thus the change in `(rho_2,rho_3)` is computed from a constant-size boundary
word around each seam; no interior of a long reversed component must be
reanalysed.

If every inner component has at least `d+1` vertices, a one-run of length at
most `d` cannot cross two new seams.  In that case each candidate matching
edge `xy` can be declared residence-safe independently by concatenating the
last `d` old vertices ending at `x` and the first `d` old vertices beginning
at `y` (the reverse orientation gives the same run lengths).  The entire
delay-`d` reconnection problem is then a **coloured perfect matching** in
`A_S`, with:

* the lower-label constraint (3.2);
* the upper-deficiency constraint (3.3);
* the per-seam finite boundary test; and
* connectivity cuts on the contracted component graph.

The boundary test has a closed form.  For an exposed end `x` of an old
component and a coordinate `c`, let

\[
\tau_x(c)=\max\{t:\text{the first }t\text{ vertices, read from }x
\text{ inward, all contain }c\}.
\tag{4.2}
\]

Thus `tau_x(c)=0` when `c` is absent from `x`.  Suppose every old run of
length at most `d` has been hit by a cut and all inner components have at
least `d+1` vertices.  Then a candidate seam `xy` is residence-safe through
stage `d` if and only if, for every coordinate `c`,

\[
\begin{array}{rll}
c\in x\setminus y&\Longrightarrow&\tau_x(c)\ge d+1,\\
c\in y\setminus x&\Longrightarrow&\tau_y(c)\ge d+1,\\
c\in x\cap y&\Longrightarrow&\tau_x(c)+\tau_y(c)\ge d+1.
\end{array}
\tag{4.3}
\]

Indeed, these are respectively the terminal run closed by the seam, the
initial run opened by it, and the two endpoint runs merged across it.  The
component-length assumption ensures that a short run cannot meet two seams,
so these are all possibilities.  Formula (4.3) makes residence a static
label on an auxiliary matching edge; no shadow rows need be constructed.

For short components, the same formulation remains finite after decorating a
component end by its length-`d` boundary state; residence becomes a
finite-memory condition along the contracted component path.

## 5. Exact finite k=11 reduction

The original certified q=1 path has short internal one-run spectrum

\[
(\#\text{length 2},\#\text{length 3})=(83,67).
\]

The program `scratch/census_k11_three_opt.cpp` exhausts all standard 3-opt
reconnections (three cuts, with the seven nonidentity permutations and
orientations of the middle blocks).  On the original certificate it finds:

\[
\begin{array}{c|r}
\text{Johnson-valid 3-opt reconnections}&698394\\
\text{lower-rainbow and upper-surjective}&212650\\
\text{strict total short-run improvements}&41\\
\text{colour-exact reconnections}&211621\\
\text{colour-exact strict improvements}&11.
\end{array}
\]

The best one-step total score is `(82,64)`, reducing 150 defects to 146;
the best staged (length-two first) score is `(79,69)`.

Repeated deterministic staged 3-opt descent yields the stored path

`scratch/k11_q1_threeopt_local_min.txt`, independently checked by
`scratch/verify_k11_threeopt_local_min.py`.  It has:

\[
\begin{array}{c|c}
\text{central vertices}&462\text{ distinct rank-six sets}\\
\text{lower colours}&1^{461},\text{ sole hole }59\\
\text{upper colours}&1^{210}2^{109}3^{11},\text{ all 330 present}\\
\text{short internal runs}&0,10,77\text{ at lengths }1,2,3.
\end{array}
\tag{5.1}

It is a strict local minimum for the lexicographic staged objective among all
standard 3-opt moves: no q=1-preserving 3-opt reduces the ten length-two
runs, and none preserving ten reduces the 77 length-three runs.

The ten length-two runs start at the following central-vertex positions:

\[
18,89,172,182,202,285,304,398,417,421.
\]

Their required cut intervals are

\[
\begin{gathered}
[17,19],[88,90],[171,173],[181,183],[201,203],\\
[284,286],[303,305],[397,399],[416,418],[420,422].
\end{gathered}
\tag{5.2}

These ten intervals are pairwise disjoint.  Lemma 4.1 therefore proves:

\[
\boxed{\text{Any single reconnection eliminating all ten defects uses at
least ten cuts.}}
\tag{5.3}
\]

This is a statewise mathematical obstruction to one-shot 3-opt (or any
`k`-opt with `k<10`), not merely a failed heuristic.

Choose one cut from each interval in (5.2), spaced so the resulting inner
components have at least four vertices.  The next q=2 connector is then an
instance on:

\[
20\text{ exposed ends},\qquad {20\choose2}=190
\text{ possible pairs before filtering}.
\]

For example,

\[
S_0=\{17,88,171,181,201,284,303,397,416,422\}
\tag{5.4}
\]

hits the ten intervals and has consecutive gaps at least six.  Thus the
closed-form seam test (4.3) is exact for this cut set, with `d=2` at the
first stage.

This particular example is now ruled out before the residence test.  The
explicit endpoint-incidence certificate in
`K11_TEN_CUT_S0_MATCHING_OBSTRUCTION_20260727.md` shows that every exposed
end contains exactly one member of \(R_{S_0}\cup\{C_*\}\), namely its original
deleted-edge lower colour, and no end contains `C_*=59`.  Therefore the
q=1 lower-rainbow seam graph is ten disjoint copies of `K_2`; its unique
perfect matching is the deleted matching itself.  Thus (5.4) is inert and
cannot remove any of the ten q=2 defects.  The remaining cut-choice problem
should first filter for a nontrivial rainbow alternating circuit in the
lower-label incidence graph.  The same certificate also checks all forty
vertices occurring in the ten three-edge witness intervals: none contains
the old lower hole `59`.  Thus every one-cut-per-witness connector must
permute its ten deleted lower colours exactly; the hole cannot supply an
extra seam colour.

Filter those pairs by Johnson adjacency, (3.2), (3.3), and the length-two
boundary test, then find a connected perfect matching of size ten.  There are
only `3^10=59049` choices if exactly one cut is chosen from each witness
interval.  This is the sharply finite replacement for a global 462-vertex
Hamilton-path search.

After q=2 is eliminated, recompute the genuine q=3 defects and apply the same
construction with four-edge witness intervals and length-three boundary
states.  Earlier stages remain hard constraints in the candidate seam
filter.

This staging is forced quantitatively on the present path.  It has 77
length-three runs, each with a four-edge witness interval, while one cut
edge can hit at most four such intervals.  Hence every direct ten-cut move
leaves at least `77-4*10=37` old length-three runs untouched.  A one-shot
delay-three repair from this path needs at least `ceil(77/4)=20` cuts; the
ten-cut connector can only be the q=2 stage.

## 6. What is proved, and what remains

Proved:

1. the exact alternating-matching characterization of every `k`-opt;
2. exact q=1 colour conditions on its new seams;
3. locality and the witness-interval hitting obstruction for residence;
4. a verified q=1-perfect path with only ten (rather than 83) q=2 defects;
5. the lower bound `k>=10` for a one-shot repair of that path.

Open:

1. whether one of the 20-end coloured matchings eliminates those ten defects;
2. whether the subsequent q=3 matching exists while preserving q=2;
3. whether the repaired central path passes the separate pin/Hall factor
   recompilation test.

The main conceptual gain is that the unresolved residence connector is no
longer a global Hamiltonicity problem.  Once cuts are chosen, Hamiltonicity
is connectivity of a matching on exposed component ends, and residence is a
finite boundary-state label on those matching edges.
