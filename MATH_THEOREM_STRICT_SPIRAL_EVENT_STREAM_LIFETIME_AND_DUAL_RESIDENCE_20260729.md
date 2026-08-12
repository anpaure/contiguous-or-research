# Strict-spiral event streams, forced lifetime matching, and dual residence

Date: 2026-07-29

Status: exact necessary-and-sufficient quotient-stream normal form; exact
complement duality; exact fixed-width lower/upper shadow formulas.  This is
a structural theorem only.  It does not prove target coverage or a compiler
matching at `k=15`.

This note complements
`MATH_THEOREM_RUN_TRANSVERSAL_CSPACE_MARKOV_BASIS_AND_TWO_DECK_TRADES_20260729.md`
and
`MATH_THEOREM_JOHNSON_EVENT_STREAM_RUN_DEFICIT_AND_MMM_POTENTIAL_20260729.md`.
Those notes parameterize the scalar trace and prove the aggregate run-defect
identities.  The new points here are:

1. a necessary-and-sufficient realizability theorem stated directly in the
   quotient deletion/insertion streams `alpha,beta`;
2. the fact that the lifetime matching is forced by cyclic event order, not
   an additional permutation to choose; and
3. a literal dual-residence theorem: upper shadows of `T` are complements of
   lower shadows of the complement carrier, with zero gaps playing exactly
   the role played by one-run lengths on the lower side.

## 1. Normalized strict spirals and their event streams

Put

\[
 k=2m+1,\qquad r=m+1,\qquad
 W={k\choose r}=kN,
\]

and write `rho(x)=x+1` on `Z_k`.  Normalize a unit-voltage strict spiral so
that

\[
 T_{i+N}=\rho T_i.                                    \tag{1.1}
\]

At physical transition `i`, write

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.               \tag{1.2}
\]

It is enough to store the quotient maps

\[
 \alpha,\beta:\mathbb Z_N\longrightarrow\mathbb Z_k,
\]

because (1.1) forces

\[
 \alpha_{j+tN}=\alpha_j+t,
 \qquad
 \beta_{j+tN}=\beta_j+t.                             \tag{1.3}
\]

These are maps `Z_N -> Z_k`; unless `N=k`, they are not permutations.  The
permutations in the run-transversal description are instead the residues
modulo `N` of the lifted run starts and run ends.

Let

\[
 c_i={\bf1}_{\{0\in T_i\}},\qquad i\in\mathbb Z_W.    \tag{1.4}
\]

Then the complete carrier is recovered from one scalar trace:

\[
 \boxed{T_i=\{x\in\mathbb Z_k:c_{i-xN}=1\}.}          \tag{1.5}
\]

For a general unit voltage `v`, first multiply coordinates by `v^{-1}`;
equivalently replace `alpha,beta` below by `v^{-1}alpha,v^{-1}beta`.

## 2. Exact event placement and realizability

For quotient transition `j`, define two physical seam positions

\[
 s_j=j-N\beta_j\pmod W,
 \qquad
 e_j=j-N\alpha_j\pmod W.                             \tag{2.1}
\]

Here `s_j` is the last zero immediately before coordinate zero is inserted,
and `e_j` is the last one immediately before it is deleted:

\[
 c_{s_j}=0,\ c_{s_j+1}=1,
 \qquad
 c_{e_j}=1,\ c_{e_j+1}=0.                            \tag{2.2}
\]

Thus both seam sets contain exactly one point in every residue class modulo
`N`.

### Theorem 2.1 (quotient-stream realizability)

Given maps `alpha,beta:Z_N -> Z_k`, form

\[
 S=\{s_j:j\in\mathbb Z_N\},
 \qquad
 E=\{e_j:j\in\mathbb Z_N\}
\]

by (2.1).  They realize a rank-`r`, unit-voltage equivariant cyclic Johnson
walk if and only if all of the following hold.

1. `S` and `E` are disjoint and strictly alternate in their cyclic order on
   `Z_W`, an insertion seam followed by a deletion seam followed by an
   insertion seam, and so on.
2. Pair every `s_j` with the next point of `E` in cyclic order.  If that
   point is `e_{pi(j)}`, put

   \[
   \ell_j=(e_{\pi(j)}-s_j)_W\in\{1,\ldots,W-1\}.     \tag{2.3}
   \]

   If `s_{tau(j)}` is the next insertion seam after `e_{pi(j)}`, put

   \[
   g_j=(s_{\tau(j)}-e_{\pi(j)})_W\in\{1,\ldots,W-1\}.\tag{2.4}
   \]

3. The one-mass is correct:

   \[
   \sum_{j\in\mathbb Z_N}\ell_j=rN.                 \tag{2.5}
   \]

When these conditions hold, the scalar trace, the physical carrier, and
the lifetime matching are unique.  Explicitly, `c` is one on the cyclic
arcs

\[
                       (s_j,e_{\pi(j)}]
\]

and zero on their complement.  In particular, `pi` is not an additional
free matching: alternation forces it to be “the next deletion”.

The lifted lengths can be read directly from the streams:

\[
 \boxed{
 \ell_j\equiv
 \pi(j)-j+N\bigl(\beta_j-\alpha_{\pi(j)}\bigr)
 \pmod W,}                                           \tag{2.6}
\]

where the representative is selected by cyclic order, and

\[
 \boxed{
 g_j\equiv
 \tau(j)-\pi(j)
 +N\bigl(\alpha_{\pi(j)}-\beta_{\tau(j)}\bigr)
 \pmod W.}                                           \tag{2.7}
\]

Moreover

\[
 \sum_jg_j=(k-r)N=mN,
 \qquad
 \sum_j(\ell_j+g_j)=W.                              \tag{2.8}
\]

#### Proof

Necessity follows from the coordinate-zero trace.  Every quotient insertion
`beta_j` has a unique lift at which the inserted coordinate is zero.  Solving
`beta_j+t=0` gives the seam `j+tN=s_j`; the deletion calculation is the same.
Starts and ends of a cyclic binary word alternate, and its number of ones is
the sum of its one-run lengths.  Equations (2.6)--(2.7) are obtained by
substituting (2.1) into (2.3)--(2.4).

Conversely, alternation defines a unique binary word by filling every arc
`(s_j,e_(pi(j))]` with ones.  Define `T` by (1.5).  At a physical seam
`i=j+tN`, translating `S` by coordinate multiples of `N` shows that exactly
one coordinate changes `0 -> 1`, namely `beta_j+t`; translating `E` shows
that exactly one coordinate changes `1 -> 0`, namely `alpha_j+t`.  The two
coordinates are distinct because `S` and `E` are disjoint.  Hence every
transition is a Johnson transition and (1.3) is recovered exactly.

All ranks are therefore constant.  Summing them over the physical cycle and
using (1.5) gives

\[
 \sum_i|T_i|=k|c|=k(rN)=rW,
\]

so their common value is `r`.  Formula (1.5) also gives
`T_(i+N)=rho T_i`.  This proves sufficiency and uniqueness.  Finally the
one-runs and following zero gaps partition `Z_W`, which proves (2.8).
\(\square\)

### Corollary 2.2 (Hamilton and first-shadow tests)

Rotation is free on ranks `r=m+1` and `r-1=m`, because both ranks are
coprime to `k=2m+1`.  Consequently:

* the physical walk is a Hamilton cycle of the middle layer if and only if
  `T_0,...,T_(N-1)` are pairwise rotation-inequivalent; and
* its lower first shadow is perfect if and only if

  \[
  T_j\setminus\{\alpha_j\},\qquad j\in\mathbb Z_N,
  \]

  are pairwise rotation-inequivalent.

Thus realizability, middle Hamiltonicity, and the lower rainbow are three
separate exact tests.

## 3. All fixed-width shadows from the streams

For `q>=0`, define forward lower and upper windows

\[
 I_i^{(q)}=\bigcap_{a=0}^{q}T_{i+a},
 \qquad
 U_i^{(q)}=\bigcup_{a=0}^{q}T_{i+a}.                 \tag{3.1}
\]

For every cyclic Johnson walk, without any residence assumption,

\[
 \boxed{
 I_i^{(q)}=T_i\setminus
       \{\alpha_i,\ldots,\alpha_{i+q-1}\},}          \tag{3.2}
\]

\[
 \boxed{
 U_i^{(q)}=T_i\cup
       \{\beta_i,\ldots,\beta_{i+q-1}\}.}           \tag{3.3}
\]

The same statement for an arbitrary interval of `w` carrier vertices is

\[
 \bigcup_{a=0}^{w-1}T_{i+a}
 =T_i\cup\{\beta_i,\ldots,\beta_{i+w-2}\}.           \tag{3.4}
\]

The strict spiral makes every shadow equivariant:

\[
 I_{i+N}^{(q)}=\rho I_i^{(q)},
 \qquad
 U_{i+N}^{(q)}=\rho U_i^{(q)}.                       \tag{3.5}
\]

Hence the exact missing families are

\[
 { [k]\choose r-q}\setminus
 \bigcup_{j=0}^{N-1}\operatorname{Orb}_\rho(I_j^{(q)}),
 \qquad
 { [k]\choose r+q}\setminus
 \bigcup_{j=0}^{N-1}\operatorname{Orb}_\rho(U_j^{(q)}),
                                                               \tag{3.6}
\]

provided the windows have the displayed ranks.  At composite `k`, nonmiddle
target ranks can have short rotation orbits.  Therefore one must take the
actual orbit unions in (3.6); merely counting `N` quotient representatives
is not a valid coverage test.

## 4. Rank exactness, lazy shadows, and the one-step distinction

The one-run lengths of `c` are the `ell_j`, and its zero-run lengths are the
`g_j`.  The exact aggregate identities are

\[
 \boxed{
 \sum_{i=0}^{W-1}\bigl(|I_i^{(q)}|-(r-q)\bigr)
   =k\sum_j(q-\ell_j)^+,}                            \tag{4.1}
\]

\[
 \boxed{
 \sum_{i=0}^{W-1}\bigl((r+q)-|U_i^{(q)}|\bigr)
   =k\sum_j(q-g_j)^+.}                               \tag{4.2}
\]

Each summand on the left of (4.1) and (4.2) is nonnegative.  It follows
that

\[
 |I_i^{(q)}|=r-q\ \hbox{for every }i
 \quad\Longleftrightarrow\quad
 \min_j\ell_j\ge q,                                 \tag{4.3}
\]

and

\[
 |U_i^{(q)}|=r+q\ \hbox{for every }i
 \quad\Longleftrightarrow\quad
 \min_jg_j\ge q.                                     \tag{4.4}
\]

There is an important one-step distinction.  Under (4.3), `I^(q)` is a
*lazy* Johnson walk and

\[
 I_{i+1}^{(q)}=
 \bigl(I_i^{(q)}\cup\{\beta_i\}\bigr)
       \setminus\{\alpha_{i+q}\},                    \tag{4.5}
\]

where the two displayed coordinates can coincide.  They coincide exactly
when the run inserted at seam `i` has length `q`; in that case (4.5) is a
stationary step.  When they are distinct, `alpha_(i+q)` belongs to the old
shadow and `beta_i` does not, so (4.5) is an ordinary Johnson swap.  Therefore

\[
 I^{(q)}\text{ is a genuine Johnson walk}
 \quad\Longleftrightarrow\quad
 \min_j\ell_j\ge q+1.                                \tag{4.6}
\]

Similarly, under (4.4), `U^(q)` is a lazy Johnson walk with

\[
 U_{i+1}^{(q)}=
 \bigl(U_i^{(q)}\setminus\{\alpha_i\}\bigr)
       \cup\{\beta_{i+q}\},                          \tag{4.7}
\]

and

\[
 U^{(q)}\text{ is a genuine Johnson walk}
 \quad\Longleftrightarrow\quad
 \min_jg_j\ge q+1.                                   \tag{4.8}
\]

More precisely, the number of stationary physical steps in `I^(q)` is

\[
 k\,\#\{j:\ell_j=q\},                                \tag{4.9}
\]

and the number in `U^(q)` is

\[
 k\,\#\{j:g_j=q\}.                                   \tag{4.10}
\]

Equations (4.3)--(4.8) are the proof-safe version of “residence through
depth `q`”.  Exact rank needs minimum length `q`; a non-lazy shadow chronology
needs minimum length `q+1`.

## 5. Complement duality

Put

\[
 \overline T_i=[k]\setminus T_i.
\]

Then `bar T` is a rank-`m`, unit-voltage equivariant Johnson walk with

\[
 \overline T_{i+1}
 =\overline T_i-\{\beta_i\}+\{\alpha_i\}.             \tag{5.1}
\]

Its scalar trace is `1-c`.  Consequently:

* its deletion stream is `beta` and its insertion stream is `alpha`;
* its one-run lengths are exactly the original zero gaps `g_j`; and
* its zero gaps are exactly the original one-run lengths `ell_j`.

Moreover, pointwise and at every depth,

\[
 \boxed{
 [k]\setminus U_i^{(q)}
   =\bigcap_{a=0}^{q}\overline T_{i+a},}              \tag{5.2}
\]

\[
 \boxed{
 [k]\setminus I_i^{(q)}
   =\bigcup_{a=0}^{q}\overline T_{i+a}.}              \tag{5.3}
\]

Thus upper depth-`q` coverage for `T` is literally lower depth-`q` coverage
for the complement carrier, after complementing targets.  This is an exact
equivalence, not an analogy.

Call the carrier **biresident through `(d,u)`** if

\[
 \min_j\ell_j\ge d+1,
 \qquad
 \min_jg_j\ge u+1.                                   \tag{5.4}
\]

Then the lower shadows through depth `d` and upper shadows through depth
`u` are simultaneously rank-exact, non-lazy equivariant Johnson walks.  In
particular, every fixed-depth coverage question on either side becomes an
ordinary quotient-orbit coverage question of the form (3.6).

This is a strong sufficient normal form, not a necessary condition for
covering the upper layers: a carrier may cover all upper targets using some
rank-exact windows even when other windows have repeated insertions.

## 6. Compiler residence and the maximal erosion envelope

Let `D` be adjacent union, `(DA)_i=A_i union A_(i+1)`.  For cyclic words,

\[
 D^dA=T
\]

is possible if and only if every one-run of every coordinate trace in `T`
has length at least `d+1`, equivalently

\[
                       \min_j\ell_j\ge d+1.           \tag{6.1}
\]

The maximal legal compiler envelope is

\[
 E_j=\bigcap_{a=0}^{d}T_{j-a}
    =T_{j-d}\setminus
      \{\alpha_{j-d},\ldots,\alpha_{j-1}\}.           \tag{6.2}
\]

Every compiler word satisfying `D^dA=T` obeys `A_j subseteq E_j`, and the
maximal choice `A=E` itself satisfies `D^dE=T`.  The remaining lower-layer
problem is exactly the integral choice of suitable subsets inside these
envelopes; residence solves legality and chronology but not the graded Hall
matching.

The complement gives the exact upper analogue: demanding
`min g_j >= u+1` is precisely demanding a depth-`u` erosion controller for
the complement carrier.

## 7. The current `k=15` seed: exact diagnosis

For

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
```

the scalar trace has `N=429` one-runs and 429 zero gaps.  Its one-run lengths
have

\[
 \min\ell=4,\qquad \operatorname{avg}\ell=8,
 \qquad\max\ell=32,
\]

while its zero gaps have

\[
 \min g=1,\qquad \operatorname{avg}g=7,
 \qquad\max g=44,
\]

including

\[
 \#\{g=1\}=71,\qquad \#\{g=2\}=54,
 \qquad \#\{g=3\}=34.                                \tag{7.1}
\]

Thus the seed is exactly residence-clean for compiler depth `d=3`, but it
is very far from dual residence through depth three.  The exact physical
upper rank deficits forced before target collisions are even considered are

\[
 E_2^+=15\cdot71=1065,
\]

and

\[
 E_3^+=15\bigl(2\cdot71+54\bigr)=2940.               \tag{7.2}
\]

At depth one there are `15*71=1065` stationary steps in the upper-shadow
sequence.  This does not prove an upper coverage obstruction, but it explains
why a carrier can be perfect on the lower erosion tower while presenting a
much poorer native upper chronology.

## 8. Search consequence

The quotient variables `alpha,beta` are not free phase labels.  Their exact
feasible region is:

1. compute the lifted seams by (2.1);
2. enforce alternating cyclic order;
3. take the forced next-end lifetime matching;
4. enforce the one-mass equation (2.5); and
5. separately enforce middle, lower-shadow, and desired upper/lower orbit
   coverage.

For a two-sided construction, one should optimize both tails

\[
 \sum_j(q-\ell_j)^+,
 \qquad
 \sum_j(q-g_j)^+,                                    \tag{8.1}
\]

not residence alone.  The first is the exact lower native-rank defect and
the second the exact upper native-rank defect.  Requiring both to vanish one
step beyond the desired depths yields the clean biresident normal form; when
that is too restrictive, (4.1)--(4.2) give the exact soft penalties.
