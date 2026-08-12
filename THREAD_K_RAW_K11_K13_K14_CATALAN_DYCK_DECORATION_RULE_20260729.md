# Thread K: raw `k=11,13,14` Catalan/Dyck decoration audit and the exact incidence-dual rule

Date: 2026-07-29

## 1. Verdict and scope

The raw answers have an exact Catalan description, but they do **not** yet
give a closed semilength-raising rule for every odd `k`.

What is proved here is stronger than a numerical pattern:

1. For every odd `k=2m+1`, a translation-orbit of a lower-rainbow middle
   edge is canonically a Dyck word of semilength `m` together with two marked
   outside tokens.  Hence a translation-invariant exact carrier is exactly a
   marked Catalan selector satisfying one explicit degree-two condition.
2. The frozen `k=11` and `k=13` answers give complete, exact selector tables
   on all `C_5=42` and `C_6=132` Dyck rows.  Their choice labels, physical
   run boundaries, `q=2,3` witnesses, and upper excess are extracted below.
3. The apparently unrelated structured shore in the frozen `k=14` answer is
   an endpoint-completed facet path from a second opening `F_B`.  Only after
   deletion of coordinate `13`, complementation, and explicit invariant
   recovery does its cyclic edge set equal the incidence transpose
   \(\mathscr D(F_{13})\).  This same-scale, non-row-power dual transform carries
   the entire lower/upper flag tower with an exact depth and phase shift; it
   does not automatically preserve residence.
4. The other `k=14` shore is exactly a three-piece cut/reorientation of the
   archived opening `F_A`.  Thus the literal child is a six-sector braid of
   pieces of `F_A` and the completed dual opening of `F_B`, not a formal
   \(F\mapsto\mathscr D(F)\) path operation.

The missing all-odd theorem is sharply isolated: one still needs an explicit
map which raises semilength, selecting the two marks on every member of
`D_{m+1}` from a selector on `D_m`.  The obvious peak-deletion/ECO rules fail
on the frozen `m=5 -> 6` tables by wide margins.  Incidence duality is exact
but stays at the same semilength.  No claim of an all-odd deterministic rule
is therefore made.

This audit used only lightweight exact parsing and identity checks.  It ran no
SAT solver or carrier search; the only exhaustive census is the bounded set of
462 already-defined peak-insertion relations.

## 2. The exact Catalan quotient alphabet

Let `n=2m+1`, let `Omega=Z_n`, and let `rho` be coordinate rotation.  An
upper-middle vertex is an `(m+1)`-set.  A Johnson edge between upper-middle
vertices has the form

\[
 X\cup\{a\}\;--\;X\cup\{b\},                 \tag{2.1}
\]

where `X` is an `m`-set and `a,b` are distinct coordinates outside `X`.

### Theorem 2.1 (marked-Dyck parametrization)

Every rotation orbit of `m`-sets has size `n` and has a unique representative
whose zero/one coordinate word, with zero contributing `+1` and one
contributing `-1`, has strictly positive balance on every nonempty prefix.
The representative begins with zero.  Delete that zero and read every
remaining zero as `U` and every one as `D`.  This is a Dyck word `P` of
semilength `m`, and the construction is a bijection

\[
 \binom{\Omega}{m}/\langle\rho\rangle
       \longleftrightarrow {\cal D}_m.          \tag{2.2}
\]

Label the `m+1` outside positions of the rooted lower set by `0,1,...,m`,
where token `0` is the deleted initial zero and tokens `1,...,m` are the `U`
steps of `P` in left-to-right order.  Then a rotation orbit of an edge (2.1)
is uniquely a triple

\[
              (P;\{i,j\}),\qquad 0\le i<j\le m. \tag{2.3}
\]

Orienting the edge replaces the unordered pair by `i -> j`.

#### Proof

An orbit with period `d<n` would repeat a block `n/d` times, forcing `n/d`
to divide `m`.  Since `gcd(2m+1,m)=1`, this is impossible.  The cycle lemma
gives the unique strict-positive rotation and the standard Dyck bijection.
After rooting `X`, the two elements added in (2.1) are exactly two of its
`m+1` zero positions.  Conversely the rooted lower set and two such positions
recover the entire edge orbit.  This proves all assertions.

For a rank-`m+1` necklace use the dual convention: rotate to the unique word
with strictly positive one-minus-zero prefixes, delete its initial one, and
obtain another member of `D_m`.  Let

\[
 \psi_m(P,i)\in {\cal D}_m
\]

be the upper Dyck word obtained by adding outside token `i` to the lower row
`P` and rerooting by this upper convention.

### Corollary 2.2 (selector normal form)

A function

\[
 \pi_m:P\longmapsto\{i(P),j(P)\}\subseteq\{0,\ldots,m\} \tag{2.4}
\]

defines a translation-invariant lower-rainbow exact middle factor if and only
if the multigraph

\[
 \Gamma(\pi_m)=
 \bigl\{\psi_m(P,i(P))\;--\;\psi_m(P,j(P)):P\in {\cal D}_m\bigr\} \tag{2.5}
\]

has degree two at every vertex of `D_m`.

Indeed, lifting every selected quotient edge through all `n` rotations uses
every lower color once.  Degree two in (2.5) is exactly degree two at every
physical upper-middle vertex.  Thus (2.4), not a forced layer statistic, is
the finite object for which a closed formula is needed.

If a directed quotient component has length `ell` and total rotation voltage
`v in Z_n`, its lift has `gcd(n,v)` physical cycles, each of length
`ell*n/gcd(n,v)`.  The ordered choice labels also determine chronology: the
run begun by `i -> j` lasts until the next deletion of the inserted physical
coordinate `j`.  Consequently residence and all deeper flags depend on the
**global ordered selector**, not on the row `(P;{i,j})` alone.

For an oriented physical cycle `T_i`, put

\[
 L_q(i)=\bigcap_{h=0}^qT_{i+h},\qquad
 U_q(i)=\bigcup_{h=0}^qT_{i+h}.             \tag{2.6}
\]

The `q=2,3` witness tables below are therefore literal consecutive-edge
decorations of `Gamma(pi_m)`, not independent rankwise marginals.

## 3. Frozen inputs and reconstruction

The three answer hashes are

```text
746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850  answers/k11.word
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0  answers/k13.word
7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17  answers/k14.word
```

Write \(D_{\lor}\) for the adjacent-OR derivative in this section, reserving
\(\mathscr D\) for the incidence dual of Section 8.  For `k=11` put
\(T=D_{\lor}^3A\).  Closing `159--219` converts the opened raw path
into one translation-invariant cycle.  Its strict quotient formula is

\[
        T_{42t+j}=\rho^{2t}T_j,              \tag{3.1}
\]

so the quotient has length `42`, voltage `2`, and one physical cycle of
length `462`.

For `k=13` put \(T=D_{\lor}^3A\).  Delete the unique non-source seam
`2515--2391` and restore `2515--2395` and `2167--2391`.  This gives exactly
the frozen source factor `F_13`, edge for edge.  Its two templates satisfy

\[
\begin{aligned}
 T_{119t+j}&=\rho^{5t}B_j &&(0\le j<119),\\
 T_{1547+13t+j}&=\rho^{6t}C_j &&(0\le j<13).
\end{aligned}                                      \tag{3.2}
\]

Thus the quotient components have lengths `119,13`, voltages `5,6`, and
physical lengths `1547,169`.

## 4. Exact choice labels

There are two label systems in the old artifacts.  The invariant labels used
by the new atlas are the stable triples `[lower necklace representative,a,b]`.
The older certificate IDs below are included only to make the frozen path
order directly auditable.  The full stable triples, rooted Dyck words, token
heights/subtree sizes, ordered marks, upper endpoints, and run lengths are in
`scratch/k11_k13_k14_dyck_choice_atlas_20260729.json`.

### 4.1 `k=11`

The old catalogue choice IDs around the quotient cycle are

```text
179,614,284,462,107,93,521,580,526,24,304,367,320,55,
337,558,500,469,376,234,221,489,87,298,597,432,553,413,
442,626,127,68,186,401,206,346,245,154,135,30,1,256
```

In the Dyck-token convention of Theorem 2.1, every one of the fifteen token
pairs occurs.  Their multiplicities are

```text
01:3 02:2 03:3 04:2 05:2
12:2 13:3 14:5 15:2
23:5 24:3 25:2
34:3 35:2 45:3
```

Token `0` occurs in `12` choices and `16` choices use adjacent token labels.
The deletion and insertion coordinate words in old physical labels (`A=10`)
are

```text
delete 0417A528460395A178345A90263814529A07615874
insert A5284091A58703549A16238945027A163582746598
```

These words have Berlekamp--Massey complexities `21,22`; their difference
word has complexity `21`.  This is a scoped finite obstruction to a short
linear recurrence, not an impossibility theorem for nonlocal Catalan rules.
Likewise, the frozen polynomial-feature audit is inconsistent for total
degrees `0,1,2,3`; degree `4` has full row rank `42` and merely interpolates
the complete table.

### 4.2 `k=13`

Label a choice by the index of its lower necklace in the sorted 132-row
source catalogue.  The quotient component of length `119` has labels

```text
28,1,2,14,20,4,10,42,36,46,105,83,93,108,39,37,49,40,53,22,
116,122,66,64,67,94,51,47,98,62,32,31,65,25,109,124,128,127,
45,57,91,16,41,50,59,110,113,23,21,70,99,26,6,68,103,89,90,
12,79,73,101,86,80,72,58,0,55,19,87,9,38,119,11,95,44,43,
112,111,81,34,5,88,56,92,24,126,61,84,118,125,54,17,15,114,
117,85,13,104,120,123,96,107,60,63,8,7,35,18,3,30,82,115,76,
75,78,100,130,121,129
```

and the component of length `13` has labels

```text
27,131,71,33,52,97,106,69,102,77,74,48,29
```

All 21 Dyck-token pairs occur.  Their multiplicities are

```text
01:7 02:4 03:6 04:10 05:5 06:5
12:4 13:8 14:6 15:5 16:9
23:9 24:6 25:10 26:2
34:9 35:6 36:6
45:4 46:5 56:6
```

Token `0` occurs in `37` rows and `39` rows use adjacent token labels.  The
13-cycle is not a first-return sector.  For the **upper-Dyck vertex labels**
of `Gamma(pi_6)`, its six sector counts are

\[
                 (1,2,3,1,2,4).                 \tag{4.1}
\]

For the lower selector-row Dyck labels, the corresponding vector is
`(4,1,2,1,1,4)`.  Either convention rules out the tempting identification of
the exceptional component with one standard Catalan first-return block.

## 5. Run-boundary chronology

For each quotient arc, the atlas records the cyclic run begun by its inserted
coordinate.  The exact quotient histograms are

```text
k=11: 4^13 5^12 6^5 7^4 8^2 9^1 10^2 11^1 12^1 14^1
k=13: 4^33 5^23 6^16 7^17 8^9 9^10 10^8 11^1 12^1
      13^8 14^2 15^1 16^2 18^1
```

Here `r^c` means `c` quotient insertions have run length `r`.  Translation
lifting repeats every row `k` times.  In particular all cyclic middle runs
are at least four in both odd factors, and the lower first-shadow runs are
one shorter.

For `k=11`, the coordinate shifts of the coordinate-zero run template are

```text
coordinate: 0   1   2   3   4   5   6   7   8   9  10
position:   0 252  42 294  84 336 126 378 168 420 210
```

because the shift is `42*(6c mod 11)`.  The cut prefix/suffix one-runs are

```text
(1,6),(3,9),(0,4),(12,2),(2,3),(0,0),
(10,0),(4,1),(0,0),(0,0),(0,0).
```

Thus the shorter linear runs are cut artifacts; they are not short cyclic
residences.

For `k=14`, coordinate `13` is uniquely distinguished.  Along the middle
path its membership word is

\[
 0^{419}1^3 0^{270}1^{966}0^{1027}1^{747}.       \tag{5.1}
\]

Every old coordinate has `526--530` total middle runs and minimum positive
internal run `3`; coordinate `13` has only six total runs and three positive
blocks.  The five cross-sector seams, in path order, are

```text
position  intersection  union   exchanged coordinates
418       2382          10575   0,13
421       2916          11116   3,13
691       1326          13614   12,13
1657      7008          15204   2,13
2684      462           10702   11,13
```

## 6. Exact `q=2,3` loads and witnesses

The following are opened-path central-window loads.  They are included
because the requested witness chronology is not forced by layer sizes.

```text
          lower q2                       lower q3
k=11      0^1 1^209 2^109 3^11          1^12 2^55 3^55 4^43
k=13      1^860 2^427                    1^156 2^222 3^235 4^102
k=14      1^1013 2^653 3^233 4^103       1^153 2^238 3^272 4^128
                                           5^69 6^38 7^51 9^14
                                           10^15 11^10 12^13

          upper q2                       upper q3
k=11      1^33 2^45 3^55 4^32           3^1 5^21 6^22 7^11
k=13      1^224 2^219 3^181 4^65         1^14 2^51 3^53 4^64
          5^25 6^1                       5^52 6^13 7^26 11^1 12^12
k=14      1^1157 2^498 3^255 4^66        1^235 2^271 3^234 4^132
          5^25 6^1                       5^77 6^14 7^25 11^1 12^12
```

The upper histograms count only windows of the expected rank; turnaround
windows are omitted.  The omitted counts are

```text
          upper q2  upper q3
k=11          44       142
k=13         118       507
k=14         117       623
```

Thus “complete” means every expected-rank target occurs, not that every
consecutive window has the expected rank.

### 6.1 `k=11` rigid and boundary witnesses

Two rigid occurrences singled out by the exact audit are lower `q=2` orbit
`201`, at physical start `68`, using consecutive old choices `553,413`, and
lower `q=3` orbit `137`, at physical start `169`, using choices
`614,284,462`.  These are quotient positions `1,2,3` and certificate option
rows `40,18,30`, with stable triples `[339,9,10]`, `[157,9,10]`, and
`[217,8,9]`.

Opening the cycle removes lower `q=1` target `155` and lower `q=2` target
`154`.  The raw OR word restores them literally:

\[
 D_{\lor}^2A[0]=D_{\lor}^2A[462]=155,
 \qquad
 D_{\lor} A[463]=A[463]\cup A[464]=26\cup152=154. \tag{6.1}
\]

No `q=3` target is lost.  The terminal flag is the nested chain

\[
                     155\supset154\supset152.    \tag{6.2}
\]

### 6.2 `k=13` seam witnesses

The sole splice is between starts `1546` and `1547`.  Its exact crossing
witnesses are

```text
q2 start1545: lower 2323, load1
q2 start1546: lower 339,  load2; upper 3543, load6

q3 start1544: lower 2321, load3
q3 start1545: lower 275,  load3
q3 start1546: lower 337,  load4
```

No valid upper-`q=3` window crosses this seam.  The upper-`q=3` singleton
fibres consist of the complete orbit

\[
 (64+119t,\rho^{5t}(3455)),\qquad 0\le t<13,     \tag{6.3}
\]

plus the cut-created partial singleton `3959` at start `1023`.

### 6.3 `k=14` seam-exclusive witnesses

The six-sector braid has exactly the following targets which have no witness
wholly inside one of its six pieces:

```text
lower q2: 2374 @418, 2404 @420, 2852 @421
lower q3: 2596 @421
upper q2: 10718 @2683 and @2684
upper q3: none
```

The literal middle windows are

```text
2374: [2383,10574,10598]
2404: [10598,11108,2924]
2852: [11108,2924,2862]
2596: [11108,2924,2862,2734]
10718:[2518,2510,8654] and [2510,8654,8666]
```

In the source word itself, the shortest-window depths are

```text
rank 5:  0^1774 1^228
rank 4:  0^963  1^38
rank 9:  4^2002
rank 10: 5^1001
```

Thus central-shadow completeness and literal word realizability have both
been checked; they are not being conflated.

## 7. Upper `q=1` concentration and duplicate provenance

Two quantities must be separated.  For target loads `ell_y`, the duplicate
mass

\[
 E_1=\sum_y(\ell_y-1)^+
\]

is forced once coverage and the total number of valid occurrences are fixed.
The non-forced concentration statistic is the above-cap mass

\[
 E_2=\sum_y(\ell_y-2)^+,
\]

or equivalently the distance from the two-floor profile.

For `k=11`, the opened profile is

\[
                     1^{199}2^{131};              \tag{7.1}
\]

after restoring the closure it is `1^198 2^132`.  It is already the exact
two-floor profile, so `E_2=0`.  The twelve doubled upper necklaces have representatives

```text
127,223,247,351,379,431,443,463,493,501,699,727.
```

For `k=13`, the opened and cyclic profiles are respectively

\[
1^{937}2^{272}3^{78},\qquad
1^{936}2^{273}3^{78}.                              \tag{7.2}
\]

There are six quotient upper necklaces of load three.  Relative to the
opened floor profile `1^859 2^428`, there are 78 above-cap units and the
minimum `L^1` correction is `156`.

For `k=14`, the exact final profile is

\[
                     1^{2652}2^{274}3^{77}.         \tag{7.3}
\]

Its floor profile is `1^2575 2^428`, so the minimum `L^1` correction is
`154`, and `E_2=77`.  Its forced duplicate mass is `E_1=428`.  More
importantly, that duplicate mass has an exact six-sector provenance:

* the three `F_13` pieces on the `A` shore have internal profile
  `1^938 2^272 3^77`, duplicate mass `426`, and above-cap mass `77`;
* the three `B` pieces have `1713` distinct upper colors and miss precisely
  `10702,13614,15204`;
* three cross seams supply exactly those missing colors;
* the other two seam unions, `10575` and `11116`, are duplicates.

Hence the two seam duplicates raise the duplicate mass from `426` to `428`.
This is not factorial-floor excess.  Notice
that `F_13` lower-`q=2` does **not** control this `k=14` upper-`q=1` ledger.
It controls the opposite `B` shore after the duality below.  This shore swap
is essential.

## 8. The exact incidence dual

Let `F=(T_i)` be a cyclic lower-rainbow exact Johnson factor on the `r`-sets
of a `(2r-1)`-set `Omega`.  Put

\[
 X_i=T_i\cap T_{i+1},\qquad
 (\mathscr D F)_i=S_i=\Omega\setminus X_i.        \tag{8.1}
\]

### Theorem 8.1 (complement-line duality)

\(\mathscr D(F)\) is again a lower-rainbow exact Johnson factor.  Moreover

\[
                 \mathscr D^2(F)_i=T_{i+1},        \tag{8.2}
\]

so \(\mathscr D\) is an involution on unoriented cyclic edge sets and an involution up
to one cyclic phase on oriented rows.  With the notation (2.6),

\[
 U_q(\mathscr D F)_i=\Omega\setminus L_{q+1}(F)_i
       \quad(q\ge0),                               \tag{8.3}
\]

and

\[
 L_q(\mathscr D F)_i=\Omega\setminus U_{q-1}(F)_{i+1}
       \quad(q\ge1).                               \tag{8.4}
\]

Both the depth shift and the start shift in (8.4) are necessary.  The maps
preserve occurrence multiplicities target by target.

Equations (8.3)--(8.4) are unconditional set identities.  Interpreting a
window as a depth-`q` shadow target still requires it to have the expected
rank; equivalently, the relevant residence or coresidence condition must be
checked.  The finite calibrations below make that validity check explicitly.

#### Proof

The lower-rainbow hypothesis makes the incident facets `X_{i-1}` and `X_i`
distinct.  They are two `(r-1)`-subsets of `T_i`, hence

\[
 X_{i-1}\cup X_i=T_i.
\]

Therefore consecutive dual vertices meet in

\[
 S_{i-1}\cap S_i
   =\Omega\setminus(X_{i-1}\cup X_i)
   =\Omega\setminus T_i,                            \tag{8.5}
\]

an `(r-1)`-set.  The `X_i` run through all `(r-1)`-sets, so the `S_i` run
through all `r`-sets; the `T_i` run through all `r`-sets, so the colors in
(8.5) run through all `(r-1)`-sets.  This proves exactness and (8.2).

Finally,

\[
\begin{aligned}
\bigcup_{h=0}^q S_{i+h}
 &=\Omega\setminus\bigcap_{h=0}^qX_{i+h}
  =\Omega\setminus\bigcap_{h=0}^{q+1}T_{i+h},\\
\bigcap_{h=0}^q S_{i+h}
 &=\Omega\setminus\bigcup_{h=0}^qX_{i+h}
  =\Omega\setminus\bigcup_{h=1}^{q}T_{i+h}
       \qquad(q\ge1),
\end{aligned}
\]

which are (8.3)--(8.4), occurrence by occurrence.

If a component is a strict spiral \(T_{i+N}=\rho^vT_i\), (8.1) immediately
gives \((\mathscr DT)_{i+N}=\rho^v(\mathscr DT)_i\); oriented voltage is
preserved.  Reversing a component negates its voltage.  This accounts for the
two orientation conventions in Section 9.

Indices in this theorem are taken separately on every cyclic component of a
factor.  Applying \(\mathscr D\) to an uncompleted path of `W` vertices
produces only `W-1` vertices, and applying it twice produces only `W-2`.
Endpoint completion is not optional.

More precisely, if `C_*` is the omitted lower core, a left completion is
legal only when \(C_*\subseteq T_0\), and a right completion is legal only
when \(C_*\subseteq T_{W-1}\).  At `k=11` both containments hold, so the path is a
cut of a cyclic dual.  At `k=13` only the terminal containment holds; the raw
path cannot be treated as a cyclic row without first undoing its internal
splice and recovering the two source cycles.

There is also an exact residence warning.  If

\[
 t_i={\bf1}_{\{x\in T_i\}},
\]

then

\[
 \mathbf 1_{\{x\in(\mathscr D F)_i\}}=1-t_it_{i+1}. \tag{8.6}
\]

Thus a cyclic zero-run of length `ell` in `F` becomes a one-run of length
`ell+1` in \(\mathscr D(F)\), while a one-run of length `ell` in `F` becomes a zero-run
of length `ell-1`.  In particular, \(\mathscr D(F)\) is `d`-resident exactly when `F`
is `(d-1)`-coresident.  Duality transports shadows, not residence.  Direct
audits give 99 depth-three residence failures for the `k=11` dual and 416
for the `k=13` dual.

For exactness of the run correspondence, note that a one-run of length one in
`F` would give `X_{i-1}=X_i=T_i\setminus\{x\}`, contradicting lower-rainbow
exactness.  Hence the dual one-runs produced from adjacent zero-runs cannot
merge through a singleton source one-run.

### 8.2 Exact calibration on `F_13`

The following cyclic load identities were checked occurrence by occurrence:

```text
F lower q2 = 1^858 2^429
             = complement of dual upper q1
F upper q1 = 1^936 2^273 3^78
             = complement of dual lower q2
F lower q3 = 1^156 2^221 3^234 4^104
             = complement of dual upper q2
F upper q2 = 1^221 2^221 3^182 4^65 5^26
             = complement of dual lower q3
F lower q4 = 2^13 3^39 4^26 5^65 6^39 7^52 9^13 10^13 11^13 12^13
             = complement of dual upper q3
```

In the rooted Catalan tables, \(\mathscr D\) is an incidence transpose, not a rowwise
relabeling.  Among the same 132 Dyck row keys it changes both selected marks
on `68` rows, exactly one mark on `58`, and neither mark on only `6`.  The
new row indexed by the complement of an old upper vertex depends on the two
distinct source rows incident at that vertex.  This is the precise global
rule which explains why the transform is non-row-power.

## 9. The complete `k=13 -> 14` recursive correspondence

Let `F_A` be the archived `k=13` splice and let `F_B` be the separately
opened `path001` splice of the same underlying two-cycle edge set.  They are
not the same linear path.  Section 3 recovers `F_A`; the separate four-add,
one-delete recovery below identifies the complemented `F_B` facet shore.
Both recoveries refer to the same underlying factor `F_13`.  Let `A` denote the shore cut from `F_A`
and let `B` denote the shore which becomes \(\mathscr D(F_{13})\) after deleting
coordinate `13`, complementing the old coordinates, and cyclically recovering
the four cut edges.  The `k=14` middle order is exactly

\[
              A_1^F\ B_2^R\ A_3^F\ B_1^F\ A_2^R\ B_3^F, \tag{9.1}
\]

with piece lengths

\[
                   419,3,270,966,1027,747.         \tag{9.2}
\]

On the `A` shore, after the inverse relabeling

```text
[8,6,4,2,7,1,10,12,11,9,0,3,5]
```

the order is literally

\[
 P_{13}[0:419]
 +P_{13}[1446:1716]
 +\operatorname{rev}P_{13}[419:1446].             \tag{9.3}
\]

On the `B` shore the three internal components have lengths `3,966,747`.
Its uncomplemented core order is the reversed `path001` intersection order
with the unique missing lower core `5402` appended; the corresponding opened
upper hole is `5422`.
After cyclic recovery, their complemented old-coordinate edge set is
literally \(\mathscr D(F_{13})\), with physical component lengths `169,1547`.  The
recovery adds

```text
(1183,5275), (2773,6865), (2789,6853), (5809,7729)
```

and deletes `(2773,6853)`.  The natural dual templates retain voltages
`5,6`; the lexicographically oriented table records `5,7=-6` because it
reverses the small component.

The physical `B` shore is actually coordinate `13` joined to the
**uncomplemented** facet path `X_i`.  Complementation is the device which
recognizes its quotient factor as \(\mathscr D(F_{13})\).  The positive runs of the facet
path are the source positive runs eroded from minimum `4` to minimum `3`,
exactly matching the depth drop from three to two.

Consequently Theorem 8.1 proves exact ownership and flag-tower transport, but
does not by itself preserve residence or construct the source-word pin
assignment.  The frozen `answers/k14.word` supplies that additional
artifact-specific compiler.  This caveat prevents an unjustified promotion
of (9.1) to a general odd-to-even compiler theorem.

Equally, one must not apply \(\mathscr D\) directly to the opened `k=13` raw path.  Its
missing first-shadow core is not supported by both endpoints.  The equality
with \(\mathscr D(F_{13})\) holds only after deleting the internal splice and restoring the
two source-cycle closures specified in Section 3.  This is why (9.1) is a
two-opening braid, not a formal \(\text{path}\mapsto\mathscr D(\text{path})\) operation.

## 10. Why the odd semilength recursion is still missing

The exact `m=5 -> 6` peak-insertion audit considered every relation obtained
by inserting one Dyck peak into a semilength-five word.  There are `462`
such parent-child relations.  Only

```text
24 relations preserve the unordered selected pair,
16 relations preserve its orientation,
17 of 132 children have any parent preserving the unordered pair,
 9 of 132 children have any parent preserving the ordered pair.
```

For the four canonical choices of parent, the results are

```text
parent rule             unordered inherited  ordered inherited  uses new token
leftmost peak                     6                  4                39
rightmost peak                    7                  4                33
first deepest peak                7                  4                30
last deepest peak                 7                  5                34
```

Simple local mark rules fare similarly.  On `k=11` the best of the tested
root/first/last/deepest/two-child rules hits only `3/42`; on `k=13` the best
hits `9/132`.  On `k=13`, even the signature consisting of root degree,
number of peaks, maximum height, and the two selected token heights/subtree
sizes has 17 collision classes with different insertion-run lengths.  Thus
run chronology cannot be reconstructed from that bounded local signature.

The canonical MSW factor also does not provide the missing quotient rule.
It is not coordinate-translation invariant: for `k=11` each lower necklace
sees `6--11` distinct rooted MSW choices, and for `k=13` it sees `7--13`.
There is no invariant MSW necklace at either size.  Against the raw physical
factor, MSW shares only `32/462` edges at `k=11` and `87/1716` at `k=13`;
the remaining symmetric difference is connected in both cases.  The raw
choice occurs among the `k` rooted MSW choices on only `26/42` and `73/132`
necklaces.  Hence “take the canonical MSW row and quotient it” is not even a
well-defined construction.

There is a second invariant obstruction to identifying the hidden `k=13`
factor with a relabeling of the canonical local MMM/Dyck base factor.  The
canonical factor has physical component spectrum

```text
26,52,78,78,78,156,156,156,156,156,156,156,156,156,
```

whereas both `F_13` and \(\mathscr D(F_{13})\) have `169,1547`.  Component spectrum is
preserved by coordinate relabeling and rooting.

These are scoped no-go statements.  They rule out the tested local and direct
peak-inheritance rules, as well as the relabeling-only explanations of the two
frozen tables.  They do not rule out a different hereditary or genuinely
nonlocal Catalan recursion.

## 11. Sharp all-odd target

The deterministic all-odd problem can now be stated without reference to a
SAT model.

> **Catalan rotor recursion `CR_m`.**  Give an explicit formula for selectors
> `pi_m:D_m -> binom({0,...,m},2)` and an orientation of every component of
> `Gamma(pi_m)` such that:
>
> 1. every upper Dyck vertex has degree two;
> 2. the lifted voltages and ordered deletions/insertions give the required
>    residence lower bound;
> 3. the consecutive flags (2.6), at least through the compiler depth, cover
>    the required lower and upper targets; and
> 4. `pi_{m+1}` is obtained from `pi_m` by a stated Catalan operation, allowing
>    a globally coupled alternating correction rather than rowwise mark
>    inheritance.

The frozen data identify two exact finite operations relevant to this target:

* the specific endpoint-compatible cuts, reversals, and piece reorderings in
  the frozen six-sector certificate (arbitrary arc reordering need not give a
  legal Johnson seam); and
* apply the exact incidence transpose \(\mathscr D\), which swaps the two flag towers
  according to (8.3)--(8.4).

What they do not identify is the semilength-raising operation in item 4.
Accordingly, the honest conclusion is an exact finite Catalan rotor and an
exact same-scale dual recursion, not a proved deterministic rule for every
odd `k`.

## 12. Reproduction and frozen artifacts

The main raw-answer atlas and recursion audit are

```text
49695340c42c36a8ec06ab1c436608f4f2ec748c002b9c57a646c6da2f7ac0f6  scratch/audit_k11_raw_quotient_signatures.py
3ff9c2c37ff4f4d5fe5652900986cc2cd1be5f26329cbbd7cf9e33660024328a  scratch/fast_sigma_pattern_audit.json

80db16976a877daa74e4711600f0bf3b3306ef7ee27c7db9bade6f35cd59f304  scratch/analyze_k11_k13_k14_dyck_choice_atlas.py
b77f40e1b60a6329e1c193f5f0ed9271b3e04945cb8e4d9d050cd9ce5ab6db06  scratch/k11_k13_k14_dyck_choice_atlas_20260729.json

b03c845f629390008c35c3a3ca042f10a10dcd4d204013cb06b59a4c47daf2b2  scratch/analyze_dyck_choice_recursion.py
70194e2f461ab0b1d1c5bfa5f76575dbb80ad523fad78bb84962b667c6c2d734  scratch/k11_k13_dyck_recursion_tests_20260729.json

dbb791502891dadd2644fc4b8298443a58007a6b65248b17288695cea4778e6b  scratch/compare_raw_dyck_selectors_to_msw.py
8f94b878ca6e1a9d625f6f1183c09ae186b3c063811ab96ba1f1d6294bb7fee1  scratch/k11_k13_raw_vs_msw_selector_20260729.json
```

The exact `k=13 -> 14` dual/fold tables are

```text
24c4194eebf9b50b6333c2a63850c568ae24c72eec0668215929a588fb4f5382  scratch/audit_k14_hidden_k13_dual_section.py
1445d0c8e5d47136ac97ee09a0ee75071f40734f044ae329395455db4b9b00a9  scratch/k14_hidden_k13_dual_tables_20260729.json
```

Internal stable-table hashes in that JSON are

```text
29608df6fc880315dbaacc25df5ece3d9c4e5f47c20e6b3483691ae3eed458d4  source choice triples
54db14a5cdae3e662aef6c121da112bf733e1150810561348a8d4369f5b0f65e  dual choice triples
e65ecd8c2127371ec76eeb5fab6091c4d279d055945375ef1b61449e0de99792  source rooted-Dyck rows
1c732ca1f7540dc3ba19bcd7516552f065c5a58f716b6c2de8c2e2c29ae2a907  dual rooted-Dyck rows
deace728d41d7eb25b69d1fb053ba59c15c066ef7df48dd82e3083feff8fbd68  oriented dual quotient arcs
```

Their canonical physical-edge hashes, using sorted undirected pairs serialized
as ASCII `a b\n`, are

```text
aca41881562a0e5ccd88158beafaa3edc9298a26cb9a94414efa95e3cd7e7fac  F13 = dual-squared(F13)
f8a88a03f8e6da6a901dde285087fa9f641199d9791753c0ad14da22e109213c  incidence-dual(F13)
```

All files are deterministic parsers or identity certificates.  None invokes a
solver.  The only exhaustive step is the explicitly bounded comparison of 462
existing peak-insertion relations; it does not search for new carriers.
