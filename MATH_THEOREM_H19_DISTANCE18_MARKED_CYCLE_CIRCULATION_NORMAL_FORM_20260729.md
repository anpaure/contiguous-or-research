# H19 distance-18 marked-cycle circulation normal form

Date: 2026-07-29

Status: exact finite normal form and audited exact finite obstruction.  This
note classifies every support-distance-18 q1 repair of the authoritative H19
middle path as a marked-cycle circulation.  The complete six-branch model
and one unbranched replay are all infeasible already at the q1 marked
2-factor level.  The corrected unbranched model also closes the formerly
omitted marked-cycle distance-16 class.  This is not a global obstruction
beyond fixed H19 and distances 16/18, and it does not claim a literal
contiguous-OR word.

No new finite search was used to derive the normal form, though the `d_A=3`
specialization imports the prior exhaustive 17-row audit.  The model in
Section 9 was run only on H100 CPU; Section 12 records the frozen outputs.

## 1. Frozen H19 data

Let `P_0` be the authoritative H19 Hamilton path on the rank-eight vertices
of `Q_15`, with distinguished coordinate `z=14`.  Write A for owners
containing `z` and B for owners avoiding it.  Its endpoints are

\[
 O=\{7779,9901\}\subset B.
\tag{1.1}
\]

Its channel counts are

\[
 (AA,BB,X)=(3004,2574,856).
\tag{1.2}
\]

Let `E_0` be its 856 A-run endpoint labels, equivalently its cross lower
labels.  Let `S_0` be the 2,573-label support of its 2,574 BB edges.  Then

\[
 E_0\cap S_0=\{g\},\qquad g=3868,
\tag{1.3}
\]

the sole repeated BB lower label is 12685, and the four labels absent from
both old channels are

\[
 H=\{5801,7267,8877,13620\}.
\tag{1.4}
\]

Consequently the old BB-zero set is

\[
 M_0=\binom{[14]}7\setminus S_0
     =(E_0\setminus\{g\})\mathbin{\dot\cup}H.
\tag{1.5}
\]

## 2. Marked closure formulation

Let `F=F_A union F_B union F_X` be a proposed final Hamilton path, and let

\[
 c=pq
\tag{2.1}
\]

be a marked BB edge not in `F`.  It is intended to join the two final B
endpoints.  Write

\[
 h=p\cap q,qquad U_c=p\cup q.
\tag{2.2}
\]

For an edge statistic, `delta` means final-path multiplicity minus H19
multiplicity.  Superscripts `low` and `up` denote intersection and union
labels.

### Theorem 2.1 (exact marked-cycle equations)

The graph `F union {c}` is a q1-perfect Hamilton cycle if and only if the
following conditions hold.

For every old-ground rank-six label `K`,

\[
 m_A^0(K)+\delta_A^{\rm low}(K)=1.
\tag{2.3}
\]

For every old-ground rank-seven label `T`,

\[
 m_{BX}^0(T)+\delta_B^{\rm low}(T)+\delta_X^{\rm low}(T)
 +1_{\{h=T\}}=1.
\tag{2.4}
\]

For every A owner `v`,

\[
 \delta_A(v)+\delta_X(v)=0.
\tag{2.5}
\]

For every B owner `v`,

\[
 \delta_B(v)+\delta_X(v)+1_{\{v\in c\}}=1_{\{v\in O\}}.
\tag{2.6}
\]

Every z-containing upper-q1 colour satisfies

\[
 m_{z,\rm up}^0(U)+\delta_A^{\rm up}(U)
 +\delta_X^{\rm up}(U)\ge1,
\tag{2.7}
\]

and every no-z upper-q1 colour satisfies

\[
 m_{0,\rm up}^0(U)+\delta_B^{\rm up}(U)
 +1_{\{U_c=U\}}\ge1.
\tag{2.8}
\]

Finally, `F union {c}` is connected.

#### Proof

Equations (2.3)--(2.4) say exactly that the closed graph has every lower-q1
colour once.  Equations (2.5)--(2.6) compare the old path degrees
`2-1_O` with the new path degrees `2-1_c`; hence adding `c` makes every
middle owner degree two.  Equations (2.7)--(2.8) are exactly complete upper
q1.  The result is therefore a spanning 2-factor with both q1 conditions.
Connectedness makes it one Hamilton cycle.  Conversely, deleting the marked
BB edge from any such cycle gives every displayed equation. \(\square\)

For the stronger **open-path upper** requirement, delete the closure term
from (2.8): the path BB edges themselves must cover every no-z upper colour.
This distinction is essential below.

By `MATH_THEOREM_TRACE_QUARANTINE_COLLAPSE_20260729.md`, Theorem 2.1 is also
the exact interface to a decorated B-quarantined tight enumeration of the
four old-ground levels.  No preselected GMM forests or separate port Hall
condition remains after the global cycle is constructed.

## 3. Exact distance budget

Suppose the support symmetric difference between `F` and `P_0` is 18.  There
are unique integers `i,j,k>=0` such that

\[
\begin{array}{c|ccc}
&AA&BB&X\\ \hline
\text{removed}&i+1&j+1&k\\
\text{inserted}&i&j&k+2.
\end{array}
\tag{3.1}
\]

Indeed the channel current is `(-1,-1,+2)`.  The distance equation is

\[
 (2i+1)+(2j+1)+(2k+2)=18,
\]

or equivalently

\[
 \boxed{i+j+k=7.}
\tag{3.2}
\]

Residence excludes `i=0`: the only distance-one exact AA choices split a
run as `2+2` or `3+5`.  No theorem presently excludes `i=2,...,6`.

## 4. Exact row-fibre normal form

Let `F_A` be a residence-safe exact AA forest and let `E` be its 858 endpoint
labels.  The marked closure lower label must satisfy

\[
 h\notin E,
\tag{4.0}
\]

because otherwise the closure duplicates a cross lower colour.  Put

\[
 R=E_0\setminus E,qquad P=E\setminus E_0,qquad |R|=t,quad |P|=t+2.
\tag{4.1}
\]

The target cross lower labels are exactly `E`.  Hence the cross exchange
consists of:

* the `t` forced deletions on labels in `R`;
* the `t+2` forced additions on labels in `P`; and
* `c>=0` same-lower cross reroutes on retained endpoint labels.

Thus

\[
 d_X=2t+2+2c,qquad k=t+c.
\tag{4.2}
\]

The target BB lower-label set is exactly

\[
 B(E,h)=\binom{[14]}7\setminus(E\cup\{h\}).
\tag{4.3}
\]

Define the forced number of BB label insertions

\[
 a=|M_0\setminus(E\cup\{h\})|.
\tag{4.4}
\]

Using (1.5), this has the exact endpoint formula

\[
 \boxed{
 a=t+4-|R\cap\{g,h\}|-|P\cap H|-1_{\{h\in H\}}.
 }
\tag{4.5}
\]

The forced BB row current removes `a+1` occurrences and inserts `a`; the
extra one is the old duplicate multiplicity.  If `b>=0` same-lower BB
substitutions are used for upper or degree repair, then

\[
 d_B=2a+1+2b,qquad j=a+b.
\tag{4.6}
\]

Combining (3.2), (4.2), and (4.6) gives the single statewise budget

\[
 \boxed{i+a+b+t+c=7.}
\tag{4.7}
\]

Equations (4.1)--(4.7) are necessary and sufficient for all lower-row and
support-count conditions.  Only upper columns, owner degrees, connectedness,
and residence remain.

## 5. Complete numerical branch table

Since `a+t>=1`, equation (4.7) gives `1<=i<=6`.  Applying the already audited
minimum-AA upper toll to the `d_A=3` row, but before statewise endpoint
filtering of the larger-AA rows, the complete sector-distance catalogue is

\[
\begin{array}{c|l}
d_A&(d_A,d_B,d_X)\\ \hline
3&(3,13,2),(3,11,4)\\
5&(5,11,2),(5,9,4),(5,7,6),(5,5,8),(5,3,10),(5,1,12)\\
7&(7,9,2),(7,7,4),(7,5,6),(7,3,8),(7,1,10)\\
9&(9,7,2),(9,5,4),(9,3,6),(9,1,8)\\
11&(11,5,2),(11,3,4),(11,1,6)\\
13&(13,3,2),(13,1,4).
\end{array}
\tag{5.1}
\]

A search limited to the 17 old distance-three AA rows is therefore not a
complete distance-18 search.

### Proposition 5.1 (the minimum-AA branches)

For `d_A=3`, the lower-row budget and the two unavoidable old unique-upper
losses leave exactly two sector architectures:

\[
 (d_A,d_B,d_X)=(3,13,2),\qquad(3,11,4).
\tag{5.2}
\]

The first uses no old-cross deletion and therefore can use only the six AA
rows with endpoint delta `+2/-0`, namely rows

\[
 1,2,7,8,12,13.
\tag{5.3}
\]

For the strong open-path-upper target, the second architecture's BB distance
11 can attain its full upper-incidence bound only on rows

\[
 2,7,13.
\tag{5.4}
\]

These are necessary incidence-tight candidates, not sufficient graphical
repairs.

For (5.2)'s first architecture, if `h in H` then `(a,b,c)=(3,3,0)`;
if `h notin H` then `(a,b,c)=(4,2,0)`.  For the second architecture,
`(a,b,c)=(3,2,1)` in the old-hole case.  Every case still needs the owner-
degree, marked-closure, upper-column, and connectivity tests.

For the weaker marked-cycle target, the closure can carry one missing upper
colour.  Therefore (5.4) is not a sound pruning rule: the `(3,11,4)` branch
must retain all 15 distance-three AA rows with at most one lost old endpoint
(six with `t=0`, nine with `t=1`) and test the marked closure statewise.  Only
the two rows with `t=2` are excluded by the cross-distance budget.

## 6. The complete `d_A=5` AA catalogue

At AA distance five, remove three old edges and insert two.  In the frozen
H19 AA multiset, label 756 has multiplicity two and every other lower label
has multiplicity one.  The exact AA lower-colour equation therefore has only
two forms:

1. delete one old 756 occurrence and replace two distinct ordinary lower
   colours within their fibres;
2. delete both old 756 occurrences, insert one new 756 edge, and replace one
   ordinary lower colour.

Thus the two inserted AA edges determine all three deletions, apart from the
choice of old 756 occurrence in the first form.

Pair red removed and blue inserted half-edges arbitrarily at balanced
owners.  Up to reversal and paired-piece permutation, the complete list of
alternating trail/circuit **signatures** is

\[
\begin{array}{c|l}
t&\text{AA signed components}\\ \hline
0&RBRBR;\quad R+C_4\\
1&RBR+RB;\quad R+RBRB\\
2&R+RB+RB;\quad RBR+R+B;\quad BRB+R+R\\
3&R+R+B+RB\\
4&R+R+R+B+B.
\end{array}
\tag{6.1}
\]

Red-major ends are new AA endpoints and blue-major ends are lost old
endpoints.  These are pairing signatures, not necessarily the connected
components of the unpaired symmetric-difference graph: an owner with two red
and two blue incidences can be four-valent before pairing.  Distance 18
excludes the `t=4` row because (4.5) gives `a>=2`, so `t+a>5`.

For forced removed and inserted AA sets, exact AA legality is finite:

* at every old internal A owner, `0<=r_v-s_v<=1`;
* at every old A endpoint, `0<=s_v-r_v<=1`;
* the two blue edges are distinct valid nonold AA edges and, after deleting
  the red edges, form an acyclic quotient multigraph on the old components;
  and
* every final component has at least four vertices.

These conditions are necessary and sufficient for a spanning 429-path
forest with z-residence at least four.

The `d_A=5` distance equation is

\[
 t+a+b+c=5.
\tag{6.2}
\]

It is therefore a bounded pair-of-new-AA-edges catalogue rather than a
triple-deletion search.

## 7. Degree, upper, and cross-flow conditions

For a fully specified BB exchange, let `r_v^B,s_v^B` be its removed and
inserted incidences; define `r_v^X,s_v^X` similarly.  The final B-endpoint
indicator is forced by

\[
 \boxed{
 f_v=1_{\{v\in O\}}+r_v^B+r_v^X-s_v^B-s_v^X.
 }
\tag{7.1}
\]

The exact endpoint condition is

\[
 f_v\in\{0,1\},\qquad \sum_vf_v=2,
\tag{7.2}
\]

and the two vertices in `supp(f)` must be Johnson adjacent with intersection
`h`.

Equivalently, after fixing the final BB graph and marked endpoint pair, put

\[
 \kappa_V=2-f_V-\deg_{BB}(V).
\tag{7.3}
\]

Ignoring the prescribed number of retained old cross edges, cross completion
is an integral capacitated containment matching.  It exists if and only if

\[
 \kappa_V\ge0,qquad\sum_V\kappa_V=858,
\tag{7.4}
\]

\[
 |Q|\le\sum_{V\in N(Q)}\kappa_V
 \quad(Q\subseteq E),
\tag{7.5}
\]

and

\[
 \lambda_A(V)+\kappa_V\ge1
 \quad(V\in\tbinom{[14]}8),
\tag{7.6}
\]

where `lambda_A(V)` is the multiplicity of `V` as an AA union.  To impose
cross distance `2t+2+2c`, the matching must additionally retain exactly
`856-t-c` old cross edges.  Hall plus this scalar equality is not by itself
an iff criterion: it is a coloured-cardinality b-matching condition, which
the branch-free integer model encodes exactly.

The no-z upper condition is

\[
 \mu_{BB}(U)+1_{\{U=U_c\}}\ge1
\tag{7.7}
\]

for marked-cycle recognition, or the stronger

\[
 \mu_{BB}(U)\ge1
\tag{7.8}
\]

for an upper-complete open carrier.

After these local conditions, connectedness is the only q1 graph condition.
It may be imposed by exact subtour cuts.  Full all-coordinate residence and
deeper shadows are chronology checks on the resulting Hamilton path.

## 8. Alternating-circuit normal form

Add a formal red chord joining the two old endpoints and a blue copy of the
marked closure `c`.  Together with the nine removed and nine inserted
physical edges, every middle owner has equal red and blue degree.  Hence the
resulting `10+10` coloured multigraph decomposes into alternating circuits.

If the two marked chords lie on one alternating circuit, deleting them leaves
two old-to-new endpoint trails.  If they lie on different circuits, one gets
a blue-blue trail between the old endpoints and a red-red trail between the
new endpoints.  Every other component is an alternating cycle.  This is the
exact endpoint-moving analogue of the fixed-endpoint alternating-trail form.

## 9. Sound bounded exact model

There is a branch-free exact formulation over the middle Johnson edges.
For every physical middle edge `e`, let `y_e` indicate membership in the
final path.  For every BB edge let `c_e` indicate that it is the marked
closure.  Impose:

1. exactly one `c_e`, and `y_e+c_e<=1`;
2. at every middle owner,

   \[
   \sum_{e\ni v}y_e+\sum_{e\ni v}c_e=2;
   \]

3. for every lower-q1 colour `L`,

   \[
   \sum_{\ell(e)=L}y_e+\sum_{\ell(e)=L}c_e=1;
   \]

4. the upper inequalities (2.7)--(2.8), or their strong path form;
5. exactly nine old path edges deleted and nine nonold path edges inserted;
6. optionally one sector row of (5.1);
7. subtour cuts until `y+c` is connected; and
8. exact short-residence cuts on any decoded **open-path internal** defect
   after deleting `c` (boundary runs and the cyclic run through `c` are not
   constrained).

### Theorem 9.1 (model equivalence)

At distance 18, the integral solutions of items 1--5 are exactly the
possibly disconnected marked q1-perfect 2-factors satisfying equations
(2.3)--(2.8).  After item 7 they satisfy Theorem 2.1.  After item 8 they are
exactly the internally residence-clean open Hamilton paths in scope.

#### Proof

Items 1--3 are precisely (2.3)--(2.6) written without sector notation;
item 4 is (2.7)--(2.8); item 5 is the physical support distance.  Thus every
solution is a spanning q1-perfect 2-factor with one marked BB edge, and every
such marked 2-factor supplies the variables.  A proper component of a
2-factor is a cycle, so the standard internal-edge cut eliminates it without
eliminating any Hamilton cycle.  After deleting `c`, a decoded short internal
residence run is supported by its two bounding path edges and all intervening
path edges; forbidding that complete edge set is a valid, reversal-invariant
cut.  Boundary runs and the cyclic run through `c` are intentionally not
residence defects.  Iteration gives the final equivalence. \(\square\)

This model includes every row in (5.1).  Therefore either the unbranched run
or the conjunction of all six AA-distance runs is a complete distance-18 q1
test; a proper subset of the branch runs is only diagnostic.

## 10. Distance-16 scope correction

The saved distance-16 audit is complete for the **strong open-path upper**
target used in its theorem: if the open lower hole `h` is not in `H`, the raw
BB current is `5 -> 4`, and the two unavoidable unique-upper losses still
need two same-lower relays, already forcing BB distance 13.

That old artifact was not complete for the weaker marked-cycle equations
(2.3)--(2.8).  In
that setting a non-old-hole closure may itself restore one of upper colours
2044 or 4028, leaving only one BB relay and fitting BB distance 11.  The old
script restricted `h` to `H` and required the path BB edges alone to cover
all 2,002 no-z upper colours.

The branch-free marked-cycle model in Section 9 includes precisely this
missing class and every larger-AA distance-16 branch.  Its unbranched
distance-16 run returned `INFEASIBLE` before any subtour or residence cut.
Thus fixed H19 has no q1-perfect marked 2-factor at distance 16 in either the
strong or weak scope.

## 11. Proved and open boundary

Proved here:

* the marked-cycle equations and alternating-circuit form;
* the complete distance-18 sector table, including all larger-AA branches;
* the exact endpoint/BB-row toll formula;
* the complete `d_A=5` AA exchange classification; and
* a branch-free finite integral model equivalent to the q1/residence target;
  and
* infeasibility of every distance-18 marked q1 2-factor on fixed H19, before
  connectivity or residence is imposed.

Open:

* distance 20 and larger marked-cycle repairs;
* preservation of all deeper shadows by a q1 candidate;
* the common compiler and literal word.

## 12. Exact distance-18 exhaustion

The production model is

```text
scratch/search_k15_h19_marked_cycle_distance_exact_cpsat.py
SHA-256 81e468a3094e2bcfa8dec7d47d5c555c8d27b1c752bea5a78312438ddc0925b8
```

It has 180,180 physical middle-edge variables and 72,072 marked-BB-closure
variables.  Every run used the frozen H19 source SHA-256

```text
86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
```

and `upper_mode=cycle`.  The six exhaustive AA-distance runs returned:

\[
\begin{array}{c|c|c|c}
d_A&\text{status}&\text{subtour cuts}&\text{residence cuts}\\ \hline
3&\mathrm{INFEASIBLE}&0&0\\
5&\mathrm{INFEASIBLE}&0&0\\
7&\mathrm{INFEASIBLE}&0&0\\
9&\mathrm{INFEASIBLE}&0&0\\
11&\mathrm{INFEASIBLE}&0&0\\
13&\mathrm{INFEASIBLE}&0&0.
\end{array}
\tag{12.1}
\]

An independent unbranched run, with no AA-distance constraint, also returned
`INFEASIBLE` with zero lazy cuts in 21.16 seconds.  Thus the obstruction is
already in the integral owner-degree plus exact-lower plus complete-upper q1
marked-2-factor system.  Connectivity, residence, deeper shadows, and the
compiler are not used.

The frozen unbranched artifacts are

```text
scratch/d18_cycle_all_s18042.json
  SHA-256 844edc357b7f6537657d063d799fc5c84e6e5dfe97332241084462b9674bc614
scratch/d18_cycle_all_s18042.log
  SHA-256 26559c315d5eb7057e3326713edf8178ffa100b243105f140d34c3fe7a6bf27c
```

All six branch files, the unbranched distance-18 replay, and the corrected
unbranched distance-16 replay are checked by

```text
scratch/audit_k15_h19_distance18_marked_cycle_exhaustion.py
  SHA-256 d51d8ac208135b9bd6b603521e86d62813ac14fe5b85871281eb786f48880283
scratch/k15_h19_distance18_marked_cycle_exhaustion.audit.json
  SHA-256 981891d2a8266264bbd0b22245a0ba14417de1ffbb4379f34919b177d9eebe87
```

The audit verifies the source/model provenance, exact AA branch set, solver
status, zero lazy-cut counts, and every JSON/log hash.  The distance-16
unbranched replay is

```text
scratch/d16_cycle_all_s16043.json
  SHA-256 68978749db6fb4c3b01bdab79593dc9dbdd45e933ceea85697eb6733277665b3
scratch/d16_cycle_all_s16043.log
  SHA-256 0107a93207f3b4b8b7b6dd119d7177751af96dcaf3f14e0aabb7314c60f4501b
```

It returned `INFEASIBLE` with zero lazy cuts in 18.48 seconds.  Hence the
first fixed-H19 marked-q1 repair, if one exists, has support distance at
least 20.  Nothing here implies infeasibility at distance 20 or larger.
