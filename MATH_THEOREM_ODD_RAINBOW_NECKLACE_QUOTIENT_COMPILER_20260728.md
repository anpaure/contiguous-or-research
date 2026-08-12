# Odd rainbow-necklace quotient cycles and the exact compiler gate

Date: 2026-07-28

Status: proved conditional sufficient theorem and exact audit of
`/Users/amir.nuriyev/Downloads/opusproblem/work`.  The quotient lift,
degree count, voltage criterion, residence transfer, and compiler interface
below are proved.  The central equivariant rainbow/unit-voltage base is
already supplied for every odd `k` by Merino--Mička--Mütze.  The extra
residence, upper-shadow/cut, and exact-compiler existence package in
Section 10 is not proved by that theorem or by the audited sources.

## 1. Parameters and the central necklace layers

Fix

\[
 k=2m+1\ge 3,\qquad r=m+1,\qquad
 W=\binom{k}{r},\qquad N=\frac Wk=\operatorname {Cat}_m.
\tag{1.1}
\]

Let `rho` be addition by one on `Z_k`, acting on subsets coordinatewise.
Put

\[
 \mathcal U=\binom{\mathbb Z_k}{r},\qquad
 \mathcal L=\binom{\mathbb Z_k}{m}.
\tag{1.2}
\]

The letters `U` and `L` refer respectively to the upper and lower sides of
the odd middle-levels graph.  Both sides have physical size `W`.

Let `nu_OR(k)` (denoted `nu(k)` elsewhere in the project) be the minimum
length of a set word over `[k]` in which every letter is nonempty and whose
unions over nonempty contiguous intervals contain every nonempty subset of
`[k]`.  We reserve `v` below for graph voltage.

### Lemma 1.1 (central freeness)

The cyclic group `C_k=<rho>` acts freely on both `mathcal U` and
`mathcal L`.  Consequently each side has exactly `N=Cat_m` necklace
orbits.

#### Proof

If a nonidentity rotation has order `a>1`, each of its coordinate cycles has
length `a`.  Every invariant subset is a union of these cycles and therefore
has cardinality divisible by `a`.  But `a|k`, while

\[
 \gcd(k,m)=\gcd(2m+1,m)=1,
 \qquad
 \gcd(k,m+1)=1.
\]

Thus neither a rank-`m` nor a rank-`r` set has a nontrivial stabilizer.  The
orbit count is

\[
 \frac1k\binom{2m+1}{m+1}
 =\frac1{m+1}\binom{2m}{m}
 =\operatorname {Cat}_m.\qquad\square
\]

Freeness is being used only on the two central layers.  For composite `k`,
noncentral layers can have shorter orbits; every later coverage hypothesis is
therefore stated using the actual set of orbits, never the false count
`binom(k,s)/k`.

## 2. The coloured Johnson necklace multigraph

Let `J(k,r)` be the Johnson graph on `mathcal U`.  Every edge `AB` has the
rank-`m` colour

\[
 \gamma(AB)=A\cap B.                                      \tag{2.1}
\]

Retain the quotient

\[
 \overline J=J(k,r)/C_k                                  \tag{2.2}
\]

as a pseudograph: parallel edge orbits are distinct, and an edge orbit whose
two endpoints lie in the same vertex orbit is a loop.  A loop contributes
two incidences to degree.

Every edge orbit is free.  Indeed, an element stabilizing an edge setwise
stabilizes its intersection colour, and the action on `mathcal L` is free by
Lemma 1.1.  The same argument excludes edge inversions.  Hence the quotient
projection is a regular cyclic graph cover; in particular, the two darts of
a quotient loop are distinct and each has a unique lifted dart at a chosen
sheet.

A **rainbow necklace selection** is a set `Fbar` of edge orbits containing
exactly one edge orbit of every colour orbit in `mathcal L/C_k`.

### Lemma 2.1 (degree two forces middle-orbit coverage)

Suppose `Fbar` is a rainbow necklace selection and every vertex of
`overline J` has weighted degree at most two.  Then every vertex has weighted
degree exactly two.

#### Proof

There are `N` lower colour orbits, so `Fbar` contains exactly `N` edges.
There are also `N` upper necklace vertices.  The weighted degree sum is
`2N`.  Since it is the sum of `N` integers each at most two, every summand is
two.  In particular no middle necklace is omitted.  \(\square\)

Thus the scripts' constraints

```text
one choice per lower orbit + weighted degree at most two
```

already imply exact degree two and exact middle-orbit coverage.  This count
is valid only because both central actions are free and their orbit counts
are equal.

If `Fbar` is also connected, it is one multigraph cycle.  The conventions
include a one-loop cycle and a two-parallel-edge cycle.

## 3. Voltage and the physical lift

Choose one representative `x_v` of each upper necklace vertex.  For a dart
`e:u->v` of `overline J`, let `alpha(e) in Z_k` be defined by the unique lift

\[
 x_u\longrightarrow \rho^{\alpha(e)}x_v.                 \tag{3.1}
\]

Then `alpha(reverse(e))=-alpha(e)`.  If the quotient cycle is oriented as
`C=e_0...e_(N-1)`, define its voltage

\[
 v(C)=\sum_{i=0}^{N-1}\alpha(e_i)\pmod k.                 \tag{3.2}
\]

Changing the section to `x'_v=rho^{h_v}x_v` changes a dart label by

\[
 \alpha'(e)=\alpha(e)+h_u-h_v.                            \tag{3.3}
\]

The terms telescope around `C`, so `v` is gauge invariant.  Reversing the
orientation negates it.  In the convention of `cpsat.py`, if the two physical
endpoints are `rho^{s_u} uhat` and `rho^{s_v} vhat`, the dart label is
`s_v-s_u mod k`.

### Theorem 3.1 (rainbow necklace quotient lift)

Let `Fbar` satisfy:

1. exactly one selected edge orbit has each lower colour orbit;
2. every upper necklace has weighted degree at most two;
3. `Fbar` is connected; and
4. its cycle voltage satisfies

   \[
   \gcd(k,v)=1.                                           \tag{3.4}
   \]

Then the complete physical lift `F` is one Hamilton cycle of `J(k,r)`.  Its
`W` edge intersections are exactly the `W` rank-`m` subsets, each once.

More generally, if the quotient has weighted-degree-two components `C_j`
of lengths `n_j` and voltages `v_j`, then the lift of `C_j` consists of

\[
 \gcd(k,v_j)                                               \tag{3.5}
\]

cycles, each of length

\[
 \frac{n_jk}{\gcd(k,v_j)}.                                \tag{3.6}
\]

Consequently a physical single cycle is equivalent to one quotient
component and generator voltage.

#### Proof

Lemma 2.1 makes the selected quotient two-regular, and hypothesis 3 makes it
connected; hence it is one cycle.  Starting a lifted traversal in sheet `s`,
one quotient lap ends in sheet `s+v`.  Addition by `v` on `Z_k` has
`gcd(k,v)` orbits, each of
length `k/gcd(k,v)`.  Multiplying by the quotient-cycle length proves
(3.5)--(3.6), and (3.4) gives one cycle of length `Nk=W`.

For the colour statement, the selected edge orbit of a lower colour
necklace `[L]` has the `k` distinct colours

\[
 L,\rho L,\ldots,\rho^{k-1}L,
\]

once each.  Selecting one edge orbit for each of the `N` colour necklaces
therefore uses every physical rank-`m` colour exactly once.  \(\square\)

It is essential for composite `k` to require `gcd(k,v)=1`; merely requiring
`v!=0` is enough only when `k` is prime.

### Small quotient boundary cases

* For `k=3`, `N=1`: the quotient cycle is one loop.  It counts twice toward
  degree, and a unit-voltage lift is the physical triangle.  The loop is
  excluded in `cpsat.py` because an `AddCircuit` self-loop means “skip this
  node,” not because the mathematics forbids it.
* For `k=5`, `N=2`: the quotient cycle consists of two parallel edges,
  traversed in opposite directions.
* For `k>=7`, `N>=5`: connected weighted degree two rules out a selected
  loop or parallel two-cycle, so the quotient cycle is an ordinary simple
  cycle.

Parallel edge orbits must never be collapsed before selection: they can have
different lower colours and different voltages.

## 4. The solved Merino--Mička--Mütze base and strict spirals

We use the following published theorem in precisely the form relevant here.

### Theorem 4.1 (Merino--Mička--Mütze)

Theorem 1 of *On a combinatorial generation problem of Knuth*
(arXiv:2007.07164) states the following.

For every `k=2m+1` and every unit `s in Z_k`, the middle-levels graph on
ranks `m` and `m+1` has a `k`-fold rotation-symmetric Hamilton cycle with
fundamental shift `s` (up to reversing the cycle, which replaces `s` by
`-s`).

### Corollary 4.2 (unconditional rainbow necklace base)

For every odd `k>=3` and every unit `s mod k`, there is a rainbow necklace
selection satisfying all four hypotheses of Theorem 3.1, with quotient
voltage `s` up to sign.  Equivalently, there is a strict-spiral Johnson
Hamilton cycle whose adjacent intersections are all rank-`m` sets exactly
once.

#### Proof

Contract every rank-`m` vertex of the rotation-symmetric middle-levels
Hamilton cycle.  Its two rank-`r` neighbours differ by one exchange, so the
contraction is a Johnson Hamilton cycle.  Every rank-`m` vertex of the
middle-levels graph occurred exactly once, hence the Johnson edge colours
are every rank-`m` set exactly once.  Rotation symmetry makes the cycle a
union of complete edge orbits.  Contracting first projects it to a connected
weighted-degree-two cycle on the `N` upper necklaces; expanding each selected
colour gives the corresponding bipartite cycle on all `N` upper and `N`
lower necklaces.  Its prescribed fundamental shift is the quotient voltage
up to sign.  Since `s` is a unit, Theorem 3.1 recovers one physical Hamilton
lift.  \(\square\)

Therefore no all-`m` theorem about degree two, lower-q1 rainbow, quotient
connectivity, or unit voltage remains to be proved.  In particular these
central gates are available unconditionally for `k=15`; they must not be
listed as the finite obstruction there.

For any such quotient cycle, gauge the oriented quotient so that all
internal dart labels vanish and the complete voltage lies on its seam.  There
are representatives

\[
 X_0,X_1,\ldots,X_{N-1},\qquad X_N=\rho^v X_0,            \tag{4.1}
\]

and the physical Hamilton cycle has the strict spiral form

\[
 T_{jN+i}=\rho^{jv}X_i,
 \qquad 0\le j<k,\quad0\le i<N.                          \tag{4.2}
\]

This is the general form of the audited `k=11` identity with `N=42` and
`v=2`.  It concerns the derived middle carrier `T`, not necessarily the
compiled source word `A`.

For later residence checks define the coordinate-zero mega-trace

\[
 S_{jN+i}=\mathbf 1_{\{-jv\in X_i\}}.                    \tag{4.3}
\]

More explicitly,

\[
 \mathbf 1_{\{c\in T_{jN+i}\}}
 =S_{((j-cv^{-1})\bmod k)N+i}.                            \tag{4.4}
\]

Thus the trace of coordinate `c` is a cyclic sheet-shift of `S`.  Once `v`
is a unit, all-coordinate cyclic residence is equivalent to the single
statement that every cyclic 1-run in `S` has the required length.

### Proposition 4.3 (the canonical `k=15` base does not pass the extras)

An independent exact replay of the published shift-one MMM cycle at `k=15`
gives

\[
 W=6435,\qquad N=429,\qquad v=1.
\]

It has all 6,435 middle owners and all 6,435 lower-q1 intersections exactly
once, but its extra support is

| Gate | Covered | Missing |
|---|---:|---:|
| upper q1, rank 9 | `4455/5005` | 550 |
| lower q2, rank 6 | `4455/5005` | 550 |
| lower q3, rank 5 | `2475/3003` | 528 |
| all upper ranks 9 through 15 | `8611/9949` | 1338 |

At `d(15)=3`, it also has 1,500 cyclic 1-runs of length two and 480 of
length three, hence 1,980 cyclic residence defects.  One cut can turn at
most one cyclic run per coordinate into boundary runs, so every cut retains
at least

\[
 1980-15=1965
\]

internal residence defects.  A cut can only delete cyclic upper windows and
therefore cannot repair any of the 1,338 upper holes.  Thus this particular
strict spiral has no resident upper-safe cut.

This is a certificate-specific obstruction, not a no-go for other MMM
cycles, other unit shifts, or modified rainbow necklace cycles.  The exact
audit is `MATH_MERINO_MICKA_MUTZE_STRICT_SPIRAL_PROJECTION_20260729.md`.

## 5. What quotient orbit coverage proves

Extend (4.1) bi-infinitely by

\[
 X_{i+N}=\rho^v X_i.                                     \tag{5.1}
\]

### Lemma 5.1 (cyclic orbit-to-physical coverage)

Suppose an upper necklace `[U]`, `|U|>r`, has a quotient-window witness

\[
 \left[\bigcup_{h=a}^{b}X_h\right]=[U].                  \tag{5.2}
\]

with `1<=b-a+1<=W`.

Then every physical member of `[U]` occurs as the union of a cyclic
consecutive block of the physical cycle `T`.

Likewise, if a lower necklace `[L]` has a witness

\[
 \left[\bigcap_{h=0}^{q}X_{a+h}\right]=[L],              \tag{5.3}
\]

then every physical member of `[L]` occurs as the corresponding cyclic
intersection window of `T`.

#### Proof

Translating the start by `jN` rotates the union or intersection by
`rho^{jv}`.  Since `v` generates `Z_k`, these translations run through
every rotation of the witness.  Repetitions caused by a noncentral
stabilizer do no harm.  \(\square\)

Thus canonical-orbit checks are valid on the **cyclic** physical lift.
Actual Burnside orbits must be used off the central layers.

There are two qualifications.

1. The upper test in `cpsat.py` permits a window of any length.  That is
   enough for literal contiguous-OR coverage.  The stronger aligned-shadow
   condition `D^qT` covering every rank-`r+q` set is convenient but is not
   logically necessary.
2. A physical cut destroys the translation symmetry.  One surviving cyclic
   witness for the necklace `[U]` need not leave a witness for each
   particular physical target `U`.  Cut-safe coverage must be checked on
   physical targets, not just on one canonical representative per orbit.

## 6. Residence and the maximal erosion

Let

\[
 \Lambda=\sum_{s=1}^{r-1}\binom{k}{s},                   \tag{6.1}
\]

and let `d=d(k)` be the least nonnegative integer satisfying

\[
 dW+\binom{d+1}{2}\ge\Lambda.                            \tag{6.2}
\]

Since each of the `r-1` lower layers has size at most `W`,

\[
 1\le d(k)\le r-1.
\]

Call the physical cycle `d`-resident if every cyclic 1-run of every
coordinate has length at least `d+1`.

Cut the edge preceding `T_c` and write the resulting path as

\[
 R_i=T_{c+i\pmod W},\qquad 0\le i<W.                     \tag{6.3}
\]

Its maximal linear erosion is

\[
 P_p=\bigcap_{\max(0,p-d)\le i\le\min(p,W-1)}R_i,
 \qquad 0\le p<W+d.                                      \tag{6.4}
\]

### Lemma 6.1 (residence after every cut)

If `T` is cyclically `d`-resident, then every cut path `R` satisfies

\[
 D^dP=R.                                                  \tag{6.5}
\]

For `1<=q<=d` and `0<=i<W-q`, it also satisfies

\[
 (D^{d-q}P)_{i+q}=\bigcap_{h=0}^{q}R_{i+h}.              \tag{6.6}
\]

#### Proof

Work coordinatewise.  A cyclic run not meeting the cut remains an internal
linear run of length at least `d+1`.  The one run meeting the cut becomes at
most two boundary runs, for which the clipped intersections in (6.4) impose
no minimum length.  In any internal run `[a,b]` of length at least `d+1`,
the erosion has that coordinate at positions `[a+d,b]`; every `d+1` window
starting inside `[a,b]` meets this interval.  This proves (6.5), including
the analogous clipped boundary calculation.

For (6.6), let `[a,b]` be the maximal linear 1-run containing
`[i,i+q]`.  If it is internal, its support in `P` is exactly `[a+d,b]`.
The inequalities

\[
 a+d\le i+d,\qquad i+q\le b
\]

show that `[a+d,b]` meets `[i+q,i+d]`.  A left-boundary run `[0,b]` has
`P`-support `[0,b]`, so use `p=i+q`; a right-boundary run `[a,W-1]` has
`P`-support `[a+d,W+d-1]`, so use `p=i+d`.

Conversely, if `p in [i+q,i+d]` and the coordinate lies in `P_p`, then

\[
 p-d\le i\le i+q\le p,
\]

so (6.4) puts the coordinate in every one of
`R_i,...,R_(i+q)`.  This proves (6.6).  \(\square\)

For a resident Johnson path and `q<=d`, the intersection in (6.6) has rank
exactly `r-q`.  If one of the `q` deleted coordinates were not an
as-yet-undeleted member of `R_i`, it would have been inserted after time
`i`; deleting it inside the window would end a 1-run of length at most
`q<=d`.  Residence forbids this.  Hence the deletions are `q` distinct
members of `R_i`.

### Theorem 6.2 (previously proved monotone-deadline bound)

With `d(k)` defined by (6.2), every universal nonempty set word satisfies

\[
 \nu_{\rm OR}(k)\ge W+d(k).                               \tag{6.7}
\]

This is the established endpoint-blocker/monotone-deadline theorem recorded
in `MATH_EXACT_CENTRAL_COMPILER_THEOREM_20260727.md` and
`MATH_SEAMED_CARRIER_TO_OPTIMAL_WORD_THEOREM_20260728.md`.  It is invoked,
not reproved, in Theorem 7.1.

Therefore Claude's cyclic lower-q2/q3 tests certify exact labels in rows of
the maximal envelope `P`.  They do **not** certify the final compiled word:

* a cut deletes the `q` cyclic windows meeting its seam;
* punching `P` down to a word `A` can erase a positive witness in those
  intermediate cells or in the central row;
* ranks below `r-d` are not supplied by the intersection tower; and
* a compiler can realize a lower target in a different short interval, so
  complete intersection-orbit coverage is not even necessary in general.

It is a useful intermediate-pin atlas, not a lower compiler.

## 7. The exact lower compiler

For a fixed cut path `R`, call a nonempty word

\[
 A=(A_0,\ldots,A_{W+d-1})                                \tag{7.1}
\]

an **exact lower compiler** if

\[
 \varnothing\ne A_p\subseteq P_p,                        \tag{7.2}
\]

\[
 \bigcup_{p=i}^{i+d}A_p=R_i
 \qquad(0\le i<W),                                      \tag{7.3}
\]

and every nonempty `S` with `|S|<r` is the union of an interval of at most
`d` consecutive letters of `A`.

The length bound on a lower witness is forced: an interval of length at
least `d+1` contains a complete central window (7.3), whose union already
has rank `r`.

Call the cut **upper-safe** if, for every `U` with `|U|>r`, there are
`0<=a<=b<W` with

\[
 U=R_a\cup R_{a+1}\cup\cdots\cup R_b.                    \tag{7.4}
\]

This is a physical, nonwrapping condition.  Cyclic coverage of one
representative per upper orbit does not imply (7.4) after an arbitrary cut.

### Theorem 7.1 (odd rainbow-necklace compiler theorem)

Suppose a selected Johnson edge-orbit family satisfies hypotheses 1--4 of
Theorem 3.1.  Let `T` be its physical lift.  Suppose further that

1. `T` is cyclically `d`-resident; and
2. some physical cut is upper-safe and has an exact lower compiler `A`.

Then every nonempty subset of `[k]` is a contiguous union of `A`.  The word
has length `W+d`, and therefore

\[
 \nu_{\rm OR}(k)\le W+d.                                  \tag{7.5}
\]

Together with the monotone-deadline lower bound in Theorem 6.2, this gives

\[
 \boxed{\nu_{\rm OR}(k)=W+d(k)}.                          \tag{7.6}
\]

#### Proof

Theorem 3.1 makes `T`, and hence `R`, a permutation of all rank-`r` sets.
Equation (7.3) realizes them as the `W` length-`d+1` windows of `A`.
The exact lower compiler realizes every nonempty set below rank `r`.

If `U` has rank above `r`, choose (7.4).  Then

\[
 \bigcup_{h=a}^{b}R_h
 =\bigcup_{h=a}^{b}\ \bigcup_{p=h}^{h+d}A_p
 =\bigcup_{p=a}^{b+d}A_p,                                 \tag{7.7}
\]

a contiguous union of `A`.  Thus `A` is universal.  Its length is `W+d`.
The established monotone-deadline theorem supplies the reverse inequality
in (7.6).  \(\square\)

The rainbow q1 property is stronger than Theorem 7.1 needs after a compiler
has been supplied, but it is the exact middle-levels/necklace structure in
Claude's construction and supplies the full adjacent lower layer before the
cut.  The compiler must replace the one q1 colour lost at that cut.

Likewise, once (7.2)--(7.3) have been exhibited, linear residence of the
chosen cut is already necessary and automatic.  Cyclic residence remains in
the theorem because it is the quotient-level, cut-independent gate used by
Claude's construction: Lemma 6.1 makes every prospective cut centrally
factorable before the compiler is chosen.

## 8. Exact common-word criterion; raw Hall is insufficient

The compiler condition can be stated without a SAT solver.

Let `C_d` be the set of intervals in `[0,W+d-1]` having lengths
`1,...,d`.  For `I in C_d`, put

\[
 E(I)=\bigcup_{p\in I}P_p.                                \tag{8.1}
\]

Any compiled word induces an injection

\[
 \phi:\{S:1\le |S|<r\}\hookrightarrow\mathcal C_d       \tag{8.2}
\]

choosing one witness interval for each lower target.  It necessarily has
`S subseteq E(phi(S))`.  Thus Hall in this target--interval graph is
necessary, but it records only positive containment.

For a proposed injective assignment `phi`, define the positions still
available to coordinate `x` after all negative requirements by

\[
 Z_x={p:x\in P_p\}
 \setminus
 \bigcup_{S:\,x\notin S}\phi(S).                         \tag{8.3}
\]

### Theorem 8.1 (exact common-`A` test for a fixed assignment)

The assignment `phi` is realized by one nonempty word `A subseteq P` with
`D^dA=R` if and only if all three conditions hold:

\[
 \phi(S)\cap Z_x\ne\varnothing
 \qquad(S,\ x\in S),                                     \tag{8.4}
\]

\[
 [i,i+d]\cap Z_x\ne\varnothing
 \qquad(0\le i<W,\ x\in R_i),                           \tag{8.5}
\]

and

\[
 \bigcup_x Z_x=[0,W+d-1].                                \tag{8.6}
\]

When they hold, the maximal realization is

\[
 A_p=\{x:p\in Z_x\}.                                     \tag{8.7}
\]

#### Proof

Assume (8.4)--(8.6) and define (8.7).  If `x notin S`, definition (8.3)
removes `x` from every letter in `phi(S)`; if `x in S`, (8.4) inserts it at
least once.  Hence the union on `phi(S)` is exactly `S`.

Every `A_p` lies in `P_p`.  For a central window `[i,i+d]`, membership in
`P` already excludes every coordinate outside `R_i`, while (8.5) supplies
every coordinate inside `R_i`.  Thus `D^dA=R`.  Condition (8.6) makes every
letter nonempty.

Conversely, suppose one word realizes `phi` and the central row.  Every
occurrence of coordinate `x` lies in `P`, and every target not containing
`x` forbids `x` throughout its assigned interval.  Thus all actual
occurrences of `x` lie in `Z_x`.  Positive target witnesses, central
witnesses, and nonempty letters respectively force (8.4), (8.5), and
(8.6).  \(\square\)

This is the precise common-word obstruction.  In a specified pinned/literal
compiler normal form, PCSH can encode the corresponding positive/negative
pin system by a core-plus-Hall certificate.  An ordinary matching of lower
targets to intervals does not imply (8.4)--(8.6), and standard literal-PCSH
should not be identified with arbitrary nonsingleton interval compilation
without first defining that generalized form.

The source audit agrees with this distinction:

* the `hopcroft_karp` helper in `lib.py` is not used by `gates.py`;
* `gates.py` encodes nonzero letters, central positive survival, and all
  positive and negative target clauses in one SAT instance;
* `equi2.py`, `equicegar.py`, and `cpsat.py` stop at cyclic carrier/shadow
  gates; and
* `cutcompile.py` separately chooses a physical cut, checks path residence
  and upper coverage, solves the common lower compiler, and finally verifies
  the literal word.

Therefore the phrase `ALL CYCLIC GATES PASS` in a carrier search is not a
certificate for the contiguous-OR problem.

### 8.2 Priority-0 selector-interface correction

There is also a certificate-decoding bug independent of the mathematics.
`cpsat.py` excludes quotient self-loop choices, whereas `equi2.py` retains
them.  Nevertheless `cutcompile.py` imports `equi2.Carrier` and decodes the
bare integer choice IDs emitted by `cpsat.py`.  The ordered tables therefore
diverge as soon as the first excluded loop is passed:

| `k` | `equi2` choices | `cpsat` choices | loops skipped | first divergent zero-based ID |
|---:|---:|---:|---:|---:|
| 9 | 140 | 135 | 5 | 3 |
| 11 | 630 | 625 | 5 | 4 |
| 15 | 12012 | 11998 | 14 | 6 |

Thus a `cpsat.py` selector JSON must **not** be interpreted through the
`equi2.py` choice array.  This invalidates that decoding route, not the
abstract selector theorem and not a final word independently checked by all
of its literal intervals.

A theorem-grade selector certificate must store explicit choice tuples
`(lower_representative,a,b)` (and, when orientation matters, the directed
arc and phase), together with an enumerator version and a digest of the full
ordered choice table.  A decoder must reject a digest mismatch.  Importing
the exact same `QModel` enumeration is a weaker source-dependent repair.

In particular, a bare `cpsat.py` integer-ID artifact is not, by this decoding
route alone, a physical-carrier certificate.  The Merino--Mička--Mütze
theorem removes the need to salvage it for the central base, but any claimed
extra-gate witness still requires provenance-correct tuple decoding followed
by fresh physical residence, upper-window, cut, and compiler audits.

## 9. Exact comparison with middle-levels and necklace machinery

Let `T_0...T_(W-1)` be a physical rainbow Johnson Hamilton cycle and put

\[
 L_i=T_i\cap T_{i+1}\qquad(i\bmod W).                    \tag{9.1}
\]

The alternating cycle

\[
 T_0,L_0,T_1,L_1,\ldots,T_{W-1},L_{W-1},T_0             \tag{9.2}
\]

is a Hamilton cycle of the bipartite middle-levels graph: all rank-`r`
vertices occur once because `T` is Hamilton, and all rank-`m` vertices occur
once because the edge colours are rainbow.  Conversely, contracting every
rank-`m` vertex of any middle-levels Hamilton cycle gives a rainbow Johnson
Hamilton cycle.

At quotient level, expanding each selected coloured Johnson edge through
its lower-colour necklace makes `Fbar` a Hamilton cycle of the full
bipartite necklace multigraph.  The unit-voltage condition is exactly what
makes its regular `C_k` lift connected.

For `k=3`, the expanded quotient has one upper and one lower vertex joined
by two parallel incidence edges; this is the two-vertex Hamilton cycle in
the retained multigraph convention.

This equivalence has three scope boundaries.

1. It applies to `C_k`-invariant physical middle-levels Hamilton cycles.
   An arbitrary physical Hamilton cycle projects only to a quotient closed
   walk, generally visiting each necklace `k` times; it need not be a union
   of complete edge orbits.
2. A Hamilton cycle in the **simple** upper-necklace adjacency graph is only
   a vertex-order skeleton.  In particular, `explicit1.py` stores canonical
   neighbours in a set and thereby collapses parallel edge orbits.  One must
   still choose actual edges whose lower colours are a bijection and whose
   voltage is a unit.
3. The middle-levels theorem and the necklace quotient solve only the
   central Hamilton/rainbow layer.  They do not imply residence, higher
   union-window coverage, survival under one linear cut, or a simultaneous
   lower compiler.

Thus the hierarchy is

\[
\begin{array}{c}
\text{simple Dyck/necklace Hamilton order}\\
\xrightarrow[\text{if such a choice exists}]
 {+\text{ compatible coloured parallel edges}}\\
\text{rainbow Hamilton cycle in the full necklace multigraph}\\
\xrightarrow[\text{if primitive}]{+\ \gcd(k,v)=1}\\
\text{one physical equivariant middle-levels Hamilton cycle}\\
\xrightarrow[\text{if jointly feasible}]
 {+\text{ residence, cut-safe upper atlas, compiler}}\\
\text{literal universal word of length }W+d.
\end{array}                                                \tag{9.3}
\]

Each arrow is conditional on the displayed additional existence datum; the
preceding line alone does not certify the next.  The Merino--Mička--Mütze
theorem supplies the third line directly, with any prescribed unit voltage,
for every odd `k`; it does not supply the final line.

## 10. The solved base and the modular remaining package

Define the **MMM base property** to mean a rotation-invariant middle-levels
Hamilton cycle with unit fundamental shift, or equivalently its
strict-spiral rainbow Johnson projection.  Theorem 4.1 guarantees this
property for every odd `k` and every prescribed unit shift; no particular
algorithmic output family is fixed.

The remaining construction package tested in Claude's architecture is the
following.

### EXTRA-RNQC(`k`) (not proved by MMM or the audited sources)

For every odd `k=2m+1>=3`, some MMM-base cycle has a Johnson projection `T`
such that

1. `T` is cyclically `d(k)`-resident;
2. cyclic consecutive unions of `T` cover every physical upper target,
   including the rank-`r+1` upper-q1 layer and every deeper layer; and
3. it has a physical cut which is simultaneously
   * upper-safe in the sense of (7.4), and
   * feasible for the exact common lower compiler of Section 8, meaning
     that some injective assignment `phi` satisfies (8.4)--(8.6).  In a
     specified pinned/literal normal form this may instead be certified by
     its corresponding exact PCSH/common-`Q` system.

Theorem 7.1 proves

\[
 \mathrm{EXTRA\!\!-\!RNQC}(k)\quad\Longrightarrow\quad
 \nu_{\rm OR}(k)=W+d(k).                                  \tag{10.1}
\]

The base and extra gates are therefore separated exactly:

| Gate | Status |
|---|---|
| quotient degree two and all middle necklaces | solved by Corollary 4.2 |
| perfect lower-q1 rainbow | solved by Corollary 4.2 |
| unit voltage / strict spiral | solved for any unit shift by Corollary 4.2 |
| cyclic residence | not supplied uniformly for a chosen MMM-base cycle |
| upper q1 and deeper cyclic windows | not supplied uniformly |
| survival of all upper targets under one cut | not supplied |
| one exact lower common-word/PCSH compiler at that cut | not supplied |

Item 2 in EXTRA-RNQC is recorded separately because it is an actual carrier
audit gate.  Logically, item 3's upper-safe clause already implies it; the
separation identifies whether failure occurs before or only after cutting.

This package is a natural modular sufficient theorem, not a logically
minimal hypothesis list for an arbitrary word.  In a bare existential
statement which already includes `A`, exact compilation certifies linear
residence of the chosen cut, so cyclic residence is redundant; the entire
necklace/rainbow form is also a stronger normal form than Theorem 7.1's
literal transfer calculation needs.

After choosing an MMM-base cycle which is resident and cyclically
upper-complete, the irreducible missing bridge is narrower:

> **Cut/PCSH bridge (unproved in the audited sources).**  Some physical cut
> is both upper-safe and exact-common-compiler feasible.

This bridge is exact for the transfer route fixed in this note.  It is not
claimed necessary for every possible optimal word: an upper mask could in
principle be realized by an `A`-interval not aligned to a union of complete
middle windows, and an optimal word need not have necklace symmetry.

No theorem in the audited sources proves that bridge.  In particular, the
following proposed substitute is unsupported:

\[
 \text{cyclic q2/q3 orbit coverage + ordinary Hall}
 \ \Longrightarrow\ 
 \text{one literal lower compiler}.                       \tag{10.2}
\]

The failure is structural, not merely computational: orbit coverage lives
in the maximal envelope and before a cut, while (8.4)--(8.6) are coupled
positive/negative requirements on one punched physical word after the cut.

No all-`m` construction or counterexample to EXTRA-RNQC(`k`) is proved here.
