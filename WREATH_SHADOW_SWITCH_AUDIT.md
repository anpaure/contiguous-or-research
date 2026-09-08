# Depth-one shadow switches in exact odd-graph wreath factors

## 1. Verdict

Let

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 N_1=\binom{n}{m-1}.
\]

The Mütze--Standke--Wiechert theorem supplies a spanning 2-factor of
`KG(n,m)` whose components are all minimum odd cycles of length `n`; these
components are exactly the cyclic-interval wreaths.  The present note audits
the smallest exchanges which keep that exact structure while changing the
rank-`m-1` cyclic shadows.

There are three conclusions.

1. The depth-one objective has an exact vertex-local description.  If `F` is
   an exact wreath factor and `X` is a middle vertex, its shadow colour is the
   intersection of the two `F`-neighbours of `X`.
2. The shortest nontrivial exchange which can take one exact wreath factor to
   another is an alternating eight-cycle.  It necessarily cuts two wreaths
   twice each, reconnects the four resulting paths in two pairs, and the two
   wreaths must have the same unordered cut-length profile.  We call this a
   **balanced two-wreath switch**.
3. Strict shadow-defect descent under these switches is false.  For `m=4`,
   the MSW factor has four missing depth-one colours and exactly one improving
   balanced switch.  That switch reaches a one-step local minimum with two
   colours missing (it has neutral but no improving neighbours).  However a
   six-switch **nonincreasing** path with defect

   \[
       4,4,4,2,1,1,0
   \]

   reaches an exact wreath factor which is complete at *every* depth.  Thus
   the move class is useful and monotone nonincrease is still viable, but a
   proof requiring a strict improvement at every step is ruled out.

No asymptotic near-losslessness theorem is claimed.  The new positive finite
certificate says that the natural switch space can reach the desired vertical
property; the new negative theorem says that it has genuine flat traps for
strict descent.

## 2. The exact depth-one colour

Let `G=KG(2m+1,m)` and let `F` be a spanning 2-factor all of whose components
have length `n`.  At a vertex `X`, write its two factor neighbours as
`Y_F(X)` and `Z_F(X)`, and define

\[
 c_F(X)=Y_F(X)\cap Z_F(X).                       \tag{2.1}
\]

Both neighbours are `m`-subsets of the `(m+1)`-set `X^c`.  They are distinct,
so they omit two different coordinates of `X^c`.  Consequently

\[
 |c_F(X)|=m-1.                                    \tag{2.2}
\]

On one minimum odd cycle, if its omitted-edge label word is
`q_0,...,q_(n-1)`, the middle vertices are

\[
 A_i=\{q_{i+1},q_{i+3},\ldots,q_{i+2m-1}\}.
\]

The two neighbours of `A_i` are `A_(i-1),A_(i+1)`, and their intersection is
the same alternating subword as the usual cyclic interval of length `m-1`.
Thus the multiset

\[
 \mu_F(S)=|\{X:c_F(X)=S\}|,
 \qquad S\in\binom{[n]}{m-1},                    \tag{2.3}
\]

is exactly the depth-one wreath-shadow multiset.

There are `W` slots and `N_1` possible colours.  Put

\[
 M(F)=N_1-|\operatorname{supp}\mu_F|,
 \qquad
 D(F)=\sum_S(\mu_F(S)-1)_+.
\]

Then

\[
 D(F)=W-|\operatorname{supp}\mu_F|
     =(W-N_1)+M(F).                                \tag{2.4}
\]

Minimizing missing colours and minimizing duplicate excess are therefore
exactly the same objective.

## 3. The local alternating-cycle formula

Let `C` be a simple even cycle of `G` whose edges alternate between `F` and
`E(G)\F`, and put

\[
 F'=F\mathbin\triangle C.                          \tag{3.1}
\]

Every vertex on `C` loses one factor edge and gains one nonfactor edge, so
`F'` is again a spanning 2-factor.  At a cycle vertex `X`, let

* `h_X` be the factor neighbour whose edge is not in `C`;
* `r_X` be the removed factor neighbour; and
* `a_X` be the added neighbour.

The old and new local colours are exactly

\[
 c_X^-=h_X\cap r_X,\qquad c_X^+=h_X\cap a_X.       \tag{3.2}
\]

Define the removal and addition histograms

\[
 \rho_C(S)=|\{X\in V(C):c_X^-=S\}|,
 \qquad
 \alpha_C(S)=|\{X\in V(C):c_X^+=S\}|.
\]

Then the complete global update is

\[
 \boxed{\mu_{F'}(S)=\mu_F(S)-\rho_C(S)+\alpha_C(S).} \tag{3.3}
\]

In particular,

\[
\begin{aligned}
 M(F')-M(F)
  ={}&|\{S:\mu_F(S)>0,
             \mu_F(S)-\rho_C(S)+\alpha_C(S)=0\}|\\
    &-|\{S:\mu_F(S)=0,\ \alpha_C(S)>0\}|,          \tag{3.4}
\end{aligned}
\]

and equivalently

\[
 D(F')-D(F)
 =\sum_S\left[(\mu_F(S)-\rho_C(S)+\alpha_C(S)-1)_+
                    -(\mu_F(S)-1)_+\right].          \tag{3.5}
\]

Formula (3.4) is the exact switch rule: newly covered colours help only if
they were globally absent, while a colour is lost only if the switch removes
all of its old occurrences and adds none back.  There is no sign forced by
the fact that `C` is alternating.

## 4. Which shortest switches preserve exact wreaths

Every length-`n` cycle in `G` is induced.  Indeed every such cycle is a
wreath, so its vertex set is the `n` length-`m` intervals in one cyclic
coordinate order.  Two of these intervals are disjoint exactly when their
starts differ by `m` or `m+1` modulo `n`; these are precisely their two cycle
neighbours.  Hence the wreath has no chord.

Consider an alternating cycle `C`.  Its removed `F`-edges are pairwise
vertex-disjoint.  If an old wreath contains exactly one removed edge, deleting
it leaves an `n`-vertex path.  In `F'` that path cannot close by itself: the
only edge joining its two endpoints directly is the edge just removed.  Its
new component must therefore contain additional vertices and has length
strictly greater than `n`.  Hence:

> **Single-cut obstruction.**  In an exact-wreath-preserving alternating
> switch, every touched old wreath is cut at least twice.

An alternating four-cycle does not exist in the odd graph.  An alternating
six-cycle removes only three factor edges.  By the single-cut obstruction all
three would have to lie in one wreath, but then every added edge would be a
chord of that induced wreath.  Therefore no alternating switch of length less
than eight preserves an exact wreath factor.

Now let `C` have length eight.  It removes four factor edges.  The single-cut
obstruction and inducedness leave only the distribution `2+2`: two cuts in
one old wreath and two cuts in another.  Cutting the first wreath produces
paths of vertex lengths

\[
 a,\ n-a,
\]

and cutting the second produces paths of lengths

\[
 b,\ n-b.
\]

All four new edges run between the two old wreaths.  After contracting the
four paths, exactness requires two two-path components rather than one
four-path component.  Each new component contains one path from each old
wreath, and both have length `n` precisely when, after possibly swapping the
second pair,

\[
 a+b=n \quad\text{or}\quad a=b.                    \tag{4.1}
\]

Equivalently,

\[
 \boxed{\{a,n-a\}=\{b,n-b\}.}                       \tag{4.2}
\]

Conversely, if the contracted reconnection gives two components and (4.2)
holds, both new cycles have length `n`; all untouched wreaths remain as they
were.  This proves the promised characterization of balanced two-wreath
eight-switches.

## 5. Exhaustive small-dimensional audit

The checker

`scratch/check_wreath_shadow_switches.py`

constructs the MSW factor directly from the Chung--Feller `g,h` maps.  It
then enumerates every simple alternating cycle of each requested order,
deduplicates by its physical edge set, toggles it, and retains it exactly when
all resulting components have length `n`.  It independently recomputes the
global shadow multiset and verifies (3.3) from the changed vertices alone.

For all `m<=5`, it confirms that no alternating six-cycle preserves the exact
wreath factor and that every exact eight-switch has the balanced `2+2`
signature (4.2).  At the initial MSW factors the results are:

| `m` | wreaths | initial `M(F)` | exact 8-switches | histogram of `M(F')-M(F)` |
|---:|---:|---:|---:|:---|
| 1 | 1 | 0 | 0 | -- |
| 2 | 2 | 0 | 5 | `0:5` |
| 3 | 5 | 0 | 5 | `0:3, +1:2` |
| 4 | 14 | 4 | 14 | `-2:1, 0:7, +1:6` |
| 5 | 42 | 32 | 45 | `-2:3, -1:2, 0:22, +1:18` |

For `m=4`, the single improving switch leads from `M=4` to `M=2`.  Exhaustive
enumeration at the new factor gives

\[
 \#\{\Delta M=0,+1,+2\}=7,6,1,                    \tag{5.1}
\]

so it is a one-step local minimum: no balanced switch lowers the defect,
although seven neutral switches are available.  Section 6 shows that neutral
plateau routing escapes it.

For `m=5`, deterministic steepest descent gives

\[
 32\to30\to28\to26\to25,                           \tag{5.2}

\]

where the last factor has exact-switch histogram

\[
 \#\{\Delta M=0,+1,+2\}=22,17,5.                   \tag{5.3}

\]

This is a second verified positive-defect local minimum.

Run the archived assertions with

```text
python3 scratch/check_wreath_shadow_switches.py --regression
```

The exhaustive part is small: the full regression through `m=5` takes about
two seconds on the current machine.

## 6. A nonincreasing switch path reaches full verticality at `m=4`

The failure of strict descent is not a failure of the move class.  Starting
from the MSW factor at `m=4`, six balanced two-wreath switches give the
depth-one missing-count trace

\[
 4\longrightarrow4\longrightarrow4\longrightarrow2
  \longrightarrow1\longrightarrow1\longrightarrow0. \tag{6.1}

\]

The exact six edge sets are archived as
`M4_NONINCREASING_FULL_VERTICAL_SWITCHES` in the checker.  At every step the script verifies
that the edge set is a currently alternating eight-cycle, has the balanced
cut signature, and leaves fourteen cycles of length nine.

More strongly, after the sixth switch the missing counts of cyclic intervals
at depths `0,1,2,3,4` are

\[
 (0,0,0,0,0).                                        \tag{6.2}

\]

Thus this switch-derived factor covers every rank in the nine-coordinate
Boolean cube by its cyclic intervals.  It is an independent full-vertical
factor, alongside the SAT certificate
`m4_fully_vertical_wreath_factor.txt`.  Linearizing its fourteen wreaths in
the standard way would use `14(9+7)=224` singleton entries and cover every
nonzero nine-bit mask.

The first complete factor has depth-one multiplicity histogram

\[
 1^{43}2^{40}3^1.
\]

Two further balanced switches, both neutral for `M`, preserve completeness at
all depths and produce

\[
 \boxed{1^{42}2^{42}}.                                \tag{6.3}
\]

This is the optimally balanced possible depth-one histogram: there are 126
slots on 84 targets, every target is positive, and (6.3) distributes the 42
forced extra occurrences one per target.  The two switches are archived as
`M4_BALANCING_SWITCHES`.

The derived factors are written explicitly as

* `m4_switch_fully_vertical_wreath_factor.txt`; and
* `m4_switch_balanced_vertical_wreath_factor.txt`.

The independent verifier `scratch/verify_m4_vertical_wreath_factor.py`
checks the second file at ranks one through eight and constructs the verified
224-entry word `m4_switch_balanced_vertical_wreath_word_224.txt`.

The checker does not claim that the particular SAT factor lies in the same
balanced-switch component.  It proves the stronger property-level fact that
the balanced switch component of the MSW factor already contains *some*
fully vertical factor.

## 7. Proved / false / open ledger

### Proved

1. Depth-one colours are the vertex-local intersections (2.1).
2. The global defect update under any alternating cycle is exactly
   (3.3)--(3.5).
3. No alternating cycle shorter than eight can preserve an exact wreath
   factor.
4. Every exact eight-switch is a balanced two-wreath switch characterized by
   (4.2), together with the two-component reconnection condition.
5. The complete `m<=5` MSW switch census in Section 5 is exhaustively
   reproducible.
6. A six-switch nonincreasing path from the `m=4` MSW factor reaches complete
   shadows at every depth.
7. Two additional neutral switches reach the optimally balanced first-shadow
   histogram `1^42 2^42` without losing any deeper shadow.

### False

1. Every nonperfect exact wreath factor has a defect-decreasing balanced
   switch.
2. Strictly decreasing balanced-switch descent from the MSW factor always
   reaches depth-one completeness.
3. Every positive-defect exact wreath factor has an immediately
   defect-decreasing balanced switch.

The first two fail already at `m=4`; (5.1) is the exhaustive certificate.

### Open

1. Does every `m` admit an exact wreath factor with `M_1=o(W)` (or even
   `M_1=0`)?
2. Is the MSW factor connected to such a factor by balanced eight-switches
   for every `m`, if bounded temporary increases are allowed?
3. What potential or absorber controls neutral plateaux and any larger energy
   barriers?  The raw missing count is not a strict Lyapunov function.
4. Are larger exact alternating trades necessary asymptotically, or do
   balanced two-wreath switches generate a sufficiently large component?
5. Can a plateau-aware schedule be made simultaneously good through
   `H=sqrt(m omega(m))` depths, with total omissions `o(W)`?

The fifth item is still the all-dimensional ordered-trace frontier.  The
present audit advances its first gate and identifies the correct local move,
but does not prove the weak multiscale wreath lemma.
