# All-k compiler defect, shadow-braid seams, and the Pascal plateau gate

Date: 2026-07-30  
Lane: R  
Status: exact general theorems and a sharp conditional `B(k)+O(1)`
criterion; no unconditional all-`k` upper bound is claimed

## 0. Result

Write

\[
 r=\lceil k/2\rceil,
 \qquad W={k\choose r},
 \qquad d=B(k)-W,
\]

where `B(k)` is the proved monotone-deadline lower bound.  This note proves
three reusable statements.

1. For one depth-`d` resident middle chronology `T`, there is an exact
   **compiler deletion number** `lambda_d(T)`.  It is the minimum number of
   lower targets that must be discarded before the remaining lower targets,
   all middle owners, and one common nonzero physical antecedent can coexist.
   It has an exact common-`Q` interval formulation.  If `u(T)` upper targets
   are absent from the interval-union tower of `T`, then

   \[
             \nu(k)\le W+d+\lambda_d(T)+u(T).       \tag{0.1}
   \]

   The proof is literal: construct the common antecedent and append one copy
   of each remaining hole.

2. In a robust one-core compiler atlas, `lambda_d(T)` is bounded by an
   ordinary Hall deficiency.  For two nested endpoint banks this deficiency
   is exactly the maximum of `(d+1)^2` prefix cuts.  Consequently, a family
   of upper-complete resident carriers with uniformly bounded endpoint Hall
   deficiency proves

   \[
             \nu(k)\le B(k)+O(1).                    \tag{0.2}
   \]

   This is a genuine sufficient theorem, not an assertion that the required
   carriers exist.  The hard obstruction before Hall is the common-`Q`
   condition: one central or protected positive coordinate may have no final
   allowed position even though all sector compilers are separately feasible.

3. The deadline depths on an odd-to-even Pascal step obey the exact
   dichotomy

   \[
      d(2m+2)\in\{d(2m+1)-1,\ d(2m+1)\}.             \tag{0.3}
   \]

   On a depth-drop step, ordinary depth-`d(2m+1)` residence supplies exactly
   the extra run unit required by the adjacent-intersection sector of the
   six-piece odd-to-even braid.  On a plateau step it does not: a second
   chronology with one-sided over-residence, or a direct replacement for it,
   is an additional hypothesis.  This precisely separates the successful
   `11->12`, `13->14` calibrations from the plateau `15->16` gate without
   inferring a finite obstruction from those examples.

The resulting minimal all-`k` countercondition is stated in Section 7.  It is
not “many components” or “a failed scalar Hall test.”  A proposed Pascal or
PBBS package must fail either a hard common-`Q`/residence/upper-occurrence
condition, or have unbounded exact compiler deletion defect after all compatible
seams and boundary flags are installed.

## 1. Exact flat-middle notation

Let

\[
 T=(T_0,\ldots,T_{W-1})
\]

be a permutation of the rank-`r` layer.  Its maximal depth-`d` erosion is

\[
 P_p=\bigcap_{\substack{0\le i<W\\i\le p\le i+d}}T_i,
 \qquad 0\le p<W+d.                                  \tag{1.1}
\]

Empty intersections do not occur in (1.1).  Call `T` **factor-resident** if

\[
 P_p\ne\varnothing\quad(0\le p<W+d),
 \qquad D^dP=T.                                      \tag{1.2}
\]

For a Johnson chronology, the coordinate run theorem says that (1.2) is
equivalent to every internal one-run having length at least `d+1`, together
with the displayed nonempty-envelope condition.  Boundary runs may be
shorter.

Let

\[
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad
 \mathcal U=\{S\subseteq[k]:|S|>r\}.                 \tag{1.3}
\]

Let `IntOR(X)` denote all nonempty contiguous interval unions of a word `X`.
Define the upper defect of `T` by

\[
 u(T)=|\mathcal U\setminus\operatorname{IntOR}(T)|.  \tag{1.4}
\]

For any nonzero word `A` with `D^dA=T`, every lower target occurring in `A`
has a witness of length at most `d`: an interval of length at least `d+1`
contains one complete central window and therefore has rank at least `r`.

## 2. The exact compiler deletion number

For a family `F subseteq L`, choose one nonempty physical interval `I_S` of
length at most `d` for every `S in F`.  Define

\[
 C_p=P_p\cap\bigcap_{\substack{S\in F\\p\in I_S}}S, \tag{2.1}
\]

and

\[
 Q_x=\{p:x\in C_p\}.                                 \tag{2.2}
\]

Consider the following three conditions.

* **CQ0:** `C_p` is nonempty for every physical position `p`.
* **CQ1:** for every `i` and `x in T_i`,

  \[
                   Q_x\cap[i,i+d]\ne\varnothing.    \tag{2.3}
  \]

* **CQ2:** for every selected lower pin `S` and every `x in S`,

  \[
                   Q_x\cap I_S\ne\varnothing.       \tag{2.4}
  \]

### Theorem 2.1 (common-`Q` compiler deletion theorem)

There is one nonzero word `A` with

\[
 D^dA=T,
 \qquad F\subseteq\operatorname{IntOR}(A),           \tag{2.5}
\]

if and only if one can choose the intervals `I_S` so that CQ0--CQ2 hold.
When they hold, the maximal word

\[
                         A_p=C_p                     \tag{2.6}
\]

works.

#### Proof

Suppose first that `A` realizes (2.5), and choose one short witness `I_S`
for each `S`.  A letter at `p` is contained in every central target whose
window contains `p`, hence `A_p subseteq P_p`.  It is also contained in every
selected pin label whose interval contains `p`.  Thus `A_p subseteq C_p`.
Nonzeroness gives CQ0, and the positive coordinates of every central and
lower pin give CQ1 and CQ2.

Conversely, set `A_p=C_p`.  Equation (2.1) makes the union on each central
window a subset of `T_i`, while CQ1 gives the reverse inclusion one
coordinate at a time.  The same argument using CQ2 gives

\[
                   \bigcup_{p\in I_S}A_p=S
\]

for every selected lower pin.  CQ0 makes the word nonzero.  Hence (2.5)
holds.  QED.

Define

\[
 \lambda_d(T)
   =|\mathcal L|-
     \max\{|F|:F\subseteq\mathcal L
                   \text{ admits CQ0--CQ2}\}.         \tag{2.7}
\]

This is an integer intrinsic to the fixed chronology.  Theorem 2.1 shows
equivalently that it is the minimum number of lower masks absent from a
nonzero factor `A` with `D^dA=T`.

### Theorem 2.2 (additive-defect upper bound)

For every factor-resident rank-`r` permutation chronology `T`,

\[
             \boxed{\nu(k)\le B(k)+\lambda_d(T)+u(T).} \tag{2.8}
\]

#### Proof

Choose `A` attaining (2.7).  It covers the selected lower family and every
middle target.  If an upper target `U` equals

\[
 U=T_i\cup T_{i+1}\cup\cdots\cup T_j,
\]

then

\[
 U=A_i\cup A_{i+1}\cup\cdots\cup A_{j+d}.            \tag{2.9}
\]

Thus `A` misses at most `lambda_d(T)+u(T)` nonzero masks.  Append those
missing masks themselves, one per new cell.  Every old witness remains in
the prefix and every appended mask is supplied by its singleton interval.
The resulting literal word has the length in (2.8).  QED.

### Corollary 2.3 (architecture-free bounded-defect target)

Put

\[
 \Theta_k=\min_T\{\lambda_{d(k)}(T)+u(T)\},           \tag{2.10}
\]

where the minimum is over factor-resident permutations of the middle layer,
and is infinity if none exists.  Then

\[
                         \nu(k)\le B(k)+\Theta_k.     \tag{2.11}
\]

In particular, `sup_k Theta_k<infinity` proves `nu(k)<=B(k)+O(1)`, while
`Theta_k=0` proves equality.  This condition uses neither PBBS provenance nor
a prescribed one-core normalization.

The deadline slack has an exact collision interpretation.  For a fixed
antecedent `A`, let `mu_A(S)` count its intervals of lengths `1,...,d` with
union `S`, put

\[
 C_<(A)=\sum_{1\le|S|<r}(\mu_A(S)-1)^+,
 \qquad
 R_=(A)=\sum_{|U|=r}\mu_A(U),
\]

and let

\[
 \sigma=dW+{d+1\choose2}-|\mathcal L|.
\]

Counting all short interval occurrences gives the exact identity

\[
 \boxed{
   \#\{S\in\mathcal L:\mu_A(S)=0\}
     =C_<(A)+R_=(A)-\sigma.}                          \tag{2.11a}
\]

Thus the lower compiler is complete exactly when its lower duplicate and
rank-`r` short-window mass equals the compulsory deadline slack.  An excess
of at most `C` gives `B(k)+C` after literal augmentation when `T` is
upper-complete (and gives `B(k)+C+u(T)` in general).

### The exact non-Hall obstruction and a weighted `B(k)+O(1)` criterion

The deletion number in (2.7) has a sharper finite representation, proved in
the companion report
`MATH_THEOREM_R_ALLK_NEGATIVE_WINDOW_CONFLICT_MASS_COMPILER_20260730.md`.
For each lower target `S`, make one part whose vertices are its candidate
short witness intervals.  A transversal family is declared conflicting
exactly when its negative windows erase the last positive occurrence of a
coordinate from

1. a central window,
2. one of the selected target intervals, or
3. one source letter.

The inclusion-minimal conflicting families form a hypergraph of rank at
most

\[
       \rho(T)=\max\{d+1,\max_p|P_p|\}\le r.         \tag{2.12}
\]

Its independent-transversal deletion number is exactly `lambda_d(T)`.  In
particular, this is the necessary-and-sufficient obstruction omitted by an
ordinary target-to-address Hall model; two pins at different addresses may
still jointly delete the last two allowed occurrences of one coordinate.

There is also an integral alteration form.  Omit an exceptional target
family `O`; independently choose one candidate interval for every other
target; and let `Psi` be the sum, over all conflict edges, of the product of
the probabilities of its vertices.  Deleting one target from each realized
conflict edge leaves a compatible selector, so

\[
 \boxed{
   \nu(k)\le B(k)+u(T)+|O|+\lfloor\Psi\rfloor .}     \tag{2.13}
\]

Thus an upper-complete resident carrier with `Psi<1` gives equality, and a
family with `u(T)+|O|+Psi=O(1)` proves `B(k)+O(1)`.  This product estimate is
only a proof device after one physical chronology is fixed; it does not
assume independent physical seam switches.

Large total conflict mass is not itself an obstruction.  Join two conflict
edges when they use alternatives from a common target part.  If

\[
 p_E=\prod_{(S,I)\in E}\pi_S(I)
 \le y_E\prod_{F\sim E}(1-y_F),\qquad 0\le y_E<1,    \tag{2.14}
\]

then the finite asymmetric local lemma gives a full compatible selector.
In particular, if every edge has at most `Delta` neighbors and

\[
 p_E\le {\Delta^\Delta\over(\Delta+1)^{\Delta+1}}   \tag{2.15}
\]

for `Delta>=1` (or `p_E<1` for `Delta=0`), then
`nu(k)<=B(k)+u(T)`; upper completeness gives equality.  This is the
compiler analogue of a bounded-dependency Hall theorem: dependencies are
by target parts, not by physical overlap of two candidate intervals.

## 3. A Hall-defect theorem for robust cores

The exact compiler in Section 2 is not generally a matching problem.
Nevertheless, the robust-core specialization has a useful integral Hall
form which gives a directly checkable sufficient bound on `lambda_d(T)`.

Fix a common-`Q` pin family `Pi_0` and let its maximal word be `C`.  Assume
`C` covers a lower family `F_0`, has `D^dC=T`, and is nonzero.  For a residual
target `S in R=L\F_0`, define its safe one-cell list by

\[
\begin{aligned}
 N_C(S)=\{p:\;&C_p\subseteq S\subseteq P_p,\\
            &S\subseteq R_c
              \text{ for every fixed pin }(I_c,R_c)\in\Pi_0
              \text{ with }p\in I_c\}.
                                                               \tag{3.1}
\end{aligned}
\]

The second line is the transparency condition: expanding `C_p` to `S` may
not insert a forbidden coordinate into an already protected interval.

Put

\[
 \delta_C(R)=
   \max_{X\subseteq R}\bigl(|X|-|N_C(X)|\bigr)_+,
 \qquad N_C(X)=\bigcup_{S\in X}N_C(S).                \tag{3.2}
\]

### Theorem 3.1 (robust-core Hall augmentation)

There is a factor word with chronology `T` which covers `F_0` and all but
`delta_C(R)` members of `R`.  Consequently

\[
             \nu(k)\le B(k)+u(T)+\delta_C(R).         \tag{3.3}
\]

Moreover, `delta_C(R)` is the exact number of unmatched targets in a maximum
matching of the bipartite graph `(R,[W+d])` with lists (3.1).

#### Proof

The deficiency form of Hall's theorem gives a matching of size
`|R|-delta_C(R)`, and no larger matching.  For every matched pair `(S,p)`,
replace `C_p` by `S`; leave every unmatched position equal to `C_p`.
Matched positions are distinct.  Because `C_p subseteq S subseteq P_p`, no
central coordinate is removed and no coordinate outside a central target is
inserted.  The transparency line of (3.1) preserves every fixed pin; all its
old positive hits remain because letters only grow.  The new singleton at
`p` realizes `S`.  Thus the modified factor misses at most the unmatched
targets.  Apply Theorem 2.2, or append the unmatched targets directly, to get
(3.3).  QED.

This theorem is optional, not a normalization of unrestricted `COMP_d(T)`.
The audited `k=9` word proves that an unrestricted compiler need not admit
the stronger `DA=DP` one-core form.  The present statement is therefore a
sufficient branch, not a necessary all-`k` architecture.

### Corollary 3.2 (exact two-boundary prefix defect)

Suppose the only residual ports are nested left and right banks

\[
 L_1,\ldots,L_d,qquad R_1,\ldots,R_d,
\]

of `2d` distinct physical positions, and every target has a list

\[
 N_C(S)=\{L_1,\ldots,L_{\ell_L(S)}\}
        \cup\{R_1,\ldots,R_{\ell_R(S)}\}.             \tag{3.4}
\]

Then

\[
 \boxed{
 \delta_C(R)=
 \max_{0\le a,b\le d}
   \left(
     \#\{S:\ell_L(S)\le a,\ \ell_R(S)\le b\}-a-b
   \right)_+.}                                       \tag{3.5}
\]

#### Proof

The targets with `ell_L<=a,ell_R<=b` have their whole neighbourhood inside
the first `a` left and first `b` right ports, giving the lower bound in
(3.5).  Conversely, for any target family `X`, let

\[
 a=\max_{S\in X}\ell_L(S),
 \qquad b=\max_{S\in X}\ell_R(S).
\]

Its neighbourhood has exactly `a+b` ports, while `X` is contained in the
rectangle counted in (3.5).  Hence no arbitrary Hall set has larger
deficiency.  QED.

Thus a uniform constant `C` satisfying all prefix inequalities

\[
 \#\{S:\ell_L(S)\le a,\ell_R(S)\le b\}\le a+b+C     \tag{3.6}
\]

on upper-complete resident carriers proves `nu(k)<=B(k)+C` in this robust
branch.

## 4. Seam topology is cheap; labels and common `Q` are not

Let a middle-layer path cover have `c` components of total size `W`, each
longer than `q`.  Its number of internal windows on `q+1` consecutive owners
is

\[
                         W-cq.                        \tag{4.1}
\]

Joining the pieces by `c-1` seams creates exactly `q(c-1)` crossing windows,
so the final count is

\[
             W-cq+q(c-1)=W-q.                        \tag{4.2}
\]

This is the exact seam-cost identity.  It says that component topology has
the correct scalar capacity.  It does not say that the new windows have the
lost labels.

At depth `q`, one deleted transition belongs to at most `q` old windows and
one new seam belongs to at most `q` new windows.  With `J` deleted and `J`
inserted transition slots, the old/new occurrence symmetric difference is
therefore supported on at most `2qJ` window occurrences.  Every window
meeting several seams is counted once in the exact
old-avoiding/new-crossing partition.  No claim about the physical support of
the compiler erosion follows merely by comparing these transition slots;
that support must be recomputed in the rethreaded order.

For lower `q=1`, a q1-rainbow `c`-cycle factor loses `c` distinct cut
facets.  The `c-1` seams may restore any number of them.  Since a depth-`d`
linear compiler has exactly two q1 boundary channels, the sharp necessary
condition is

\[
             |R\setminus Q|\le2,
 \qquad |R\cap Q|\ge c-2.                             \tag{4.3}
\]

For `c=2`, scalar q1 capacity is therefore automatic even when the seam
recycles neither cut facet.  The run-boundary pair lemma gives the stronger
local fact: each deleted endpoint facet and the retained endpoint-edge facet
are distinct facets of the same owner, so their union is that owner.  Hence
each deleted facet is locally eligible at its own outer boundary port.

Neither statement proves global compiler feasibility.  Other pins may erase
the last allowed occurrence of one coordinate at that port.  In the notation
of Section 2, the actual condition remains CQ0--CQ2; in the robust endpoint
branch it is exactly (3.5).  This is the point at which scalar seam counting,
residence, and separate sector compilers cease to imply a word.

### Corollary 4.1 (bounded-defect shadow-braid theorem)

Suppose a Pascal/PBBS cut-and-join construction produces, for each `k`,

1. a factor-resident middle permutation `T_k`;
2. at most `C_U` upper targets without a retained or new seam occurrence;
3. a common-`Q` robust lower core whose residual two-boundary lists have
   prefix deficiency at most `C_L`.

Then

\[
             \nu(k)\le B(k)+C_U+C_L.                 \tag{4.4}
\]

In particular, fixed constants `C_U,C_L` give `B(k)+O(1)`.  If both are
zero, the deadline lower bound is attained.

#### Proof

The exact old/new occurrence partition preserves every upper target outside
the declared `C_U` residuals.  Theorem 3.1 installs all but `C_L` lower
residuals in one physical factor.  Append the at most `C_U+C_L` remaining
labels.  QED.

The hypotheses are intentionally physical.  Replacing the common-`Q` core
by independently feasible sector compilers is invalid: the resident `k=6`
collar `136,123,124,145` with singleton pins `3` and `2` is the minimal
two-pin example where both sectors are feasible and every final letter is
nonempty, yet coordinate `1` disappears from the central `123` window.

### Exact upper collars and the limit of bounded safe-pair braids

The companion report
`MATH_THEOREM_R_ALLK_SAFE_PAIR_SHADOW_BRAID_AND_SEAM_GRID_OBSTRUCTION_20260730.md`
gives a complementary theorem for arbitrary-width upper targets.  At one
deleted cycle edge, compress the distinct suffix-union chain to
`L^0 subsetneq ... subsetneq L^a` and the prefix-union chain to
`R^0 subsetneq ... subsetneq R^b`.  In the uncompressed indexing, the lost
cyclic labels are exactly the suffix/prefix joins `L_i union R_j` with
`j<i`; consequently they lie in the compressed grid envelope

\[
                  \{L^p\cup R^q:0\le p\le a,
                                      0\le q\le b\}, 
                                                               \tag{4.5}
\]

where `a,b<=k-r`.  Appending the nonzero increment word

\[
 \Delta L_a,\ldots,\Delta L_1,
 L^0\cup R^0,
 \Delta R_1,\ldots,\Delta R_b                         \tag{4.6}
\]

realizes the whole grid in only

\[
                    \gamma=a+b+1\le2(k-r)+1           \tag{4.7}
\]

letters.  Thus opening `c` cyclic upper-complete components, and separately
supplying one lower-complete antecedent for the joined owner path, gives

\[
                    \nu(k)\le B(k)+\sum_{e=1}^c\gamma_e.
                                                               \tag{4.8}
\]

The compatibility restriction `j<i` means that (4.5) may be a strict
envelope, but the collar deliberately realizes the entire envelope.  This
is a deterministic general upper-shadow repair theorem.  It becomes
`B(k)+O(1)` exactly when the total compressed boundary-chain cost is
bounded.

That boundedness does not follow merely from residence, local q1
squarefreeness, and the existence of the seam-crossing cyclic witnesses.
For `k=2s+3,r=s+2` there is an explicit simple Johnson cycle whose opened
path is depth-`d` resident for every `d<=s`, whose q1 edge colours are
distinct, and which has `s(s+1)/2` distinct seam-exclusive upper targets.
Meanwhile `t` disjoint adjacent replacements which preserve the OR of each
edited pair can create new labels only in `2t` nested endpoint chains, at
most `2t(k+1)` labels.  Hence any such protected repair needs

\[
             t\ge\left\lceil {s(s+1)\over4(k+1)}\right\rceil
              =(1/16+o(1))k.                          \tag{4.9}
\]

This is a sharp scoped obstruction to constant many disjoint safe-pair
braids, not to overlapping packets, segment transpositions, or nonlocal
changes of the boundary-union grid.

## 5. Exact odd-to-even deadline arithmetic

Put

\[
 d_o=d(2m+1),\qquad d_e=d(2m+2),
 \qquad W={2m+1\choose m+1},
\]

and write `t_j=binom(j+1,2)`.  The two lower-ideal sizes are

\[
 \Lambda_o=2^{2m}-1,
 \qquad
 \Lambda_e=2^{2m+1}-W-1
          =2\Lambda_o-W+1,                            \tag{5.1}
\]

while the next width is `2W`.

### Theorem 5.1 (deadline drop-or-plateau dichotomy)

For every `m>=0`,

\[
              \boxed{d_e\in\{d_o-1,d_o\},}           \tag{5.2}
\]

where the negative option is omitted when `d_o=0`.

#### Proof

The odd lower ideal has `m` nonempty ranks below the middle and every such
rank has size at most `W`; hence `d_o<=m`.  Also

\[
 W\ge t_{d_o}+1.                                     \tag{5.3}
\]

For `m=0,1` this is immediate.  For `m>=2`, use `d_o<=m` and

\[
 {2m+1\choose m}\ge {m+2\choose m}={m+2\choose2}>t_m.
\]

The odd feasibility inequality and (5.1) give

\[
\begin{aligned}
 2d_oW+t_{d_o}-\Lambda_e
 &=2(d_oW+t_{d_o}-\Lambda_o)+W-t_{d_o}-1\\
 &\ge0.
\end{aligned}
\]

Thus `d_e<=d_o`.

If `d_o>=2`, minimality at `d_o-1` gives

\[
 \Lambda_o\ge(d_o-1)W+t_{d_o-1}+1.
\]

Therefore

\[
 \Lambda_e>
 2(d_o-2)W+t_{d_o-2},                                \tag{5.4}
\]

indeed the difference is at least
`W+2t_(d_o-1)-t_(d_o-2)+3`.  Hence `d_o-2` is infeasible
for the even problem, and `d_e>=d_o-1`.  The cases `d_o<=1` are immediate.
QED.

### Corollary 5.2 (the exact Pascal residence plateau)

In the adjacent-intersection odd-to-even lift, every internal coordinate
one-run loses one vertex.  To make the completed intersection sector
depth-`d_e` resident, the source chronology needs relevant one-runs of length
at least

\[
                         d_e+2.                       \tag{5.5}
\]

Ordinary depth-`d_o` residence supplies length at least `d_o+1`.  Hence:

* if `d_e=d_o-1`, the required run margin is automatic on intact internal
  runs;
* if `d_e=d_o`, it is not automatic, and one needs a one-sided
  over-resident source chronology or a direct replacement for the
  intersection-sector argument.

The inserted missing facet and the two physical endpoints still require
their separate endpoint checks in both cases.

This is exactly the arithmetic behind the successful depth-drop
calibrations `11->12` and `13->14`.  The statement does not claim that the
other six-piece seam, upper-shadow, or compiler conditions follow.  On a
plateau such as `15->16`, it identifies a necessary extra input to this
specific intersection lift, not an obstruction to every odd-to-even braid.

### Owner stutters and the exact one-cell Pascal credit

The companion report
`MATH_THEOREM_R_ALLK_PASCAL_STUTTER_COMPILER_AND_MIXED_COVER_GATE_20260730.md`
turns the residence input into an exact integral parameter.  If `y_i`
additional consecutive copies of owner `T_i` are inserted, then the
stuttered chronology is depth-`d` resident exactly when every maximal
internal coordinate one-run `R` satisfies

\[
             \sum_{i\in R}y_i\ge(d+1-|R|)^+.         \tag{5.6}
\]

Let `tau_d(T)` be the minimum `sum_i y_i` in this interval multicover.
Stuttering preserves every owner and every arbitrary-width upper witness.
If `eta_d` is the optimized lower compiler deletion number after a minimum
stutter, then

\[
              \nu(k)\le B(k)+\tau_d(T)+\eta_d.       \tag{5.7}
\]

The curvature deficit

\[
 \Psi_d(T)=\sum_{x,R}(d+1-|R|)^+
\]

gives the integral lower bound

\[
                       \tau_d(T)\ge
                       \left\lceil{\Psi_d(T)\over r}\right\rceil.
                                                               \tag{5.8}
\]

For a facet sector required at child depth three, the authenticated
`k=11,13,15` openings give lower bounds `29,72,204`.  The first two do not
apply to the actual depth-two children `12,14`; the third is the relevant
fixed-facet toll on the `15->16` plateau.  These finite data rule out only a
smaller stutter budget on those named facets, not a different parent or
asymptotic boundedness.

There is also an exact local seam identity.  Inserting one source position
at an internal cut deletes the `d-1` crossing old intervals of length `d`
from the short band and creates two endpoint fans with `2d-1` distinct
cells, for net gain

\[
                         (2d-1)-(d-1)=d.              \tag{5.9}
\]

Consequently `s` collar-disjoint one-cell Pascal credits, together with
complete owner/upper support and one global common-`Q` table having optimized
deletion defect `h`, give the literal conditional theorem

\[
                         \nu(k)\le B(k)+s+h.          \tag{5.10}
\]

The two fans are actual interval cells, not `d` abstract free slots; the
lost length-`d` pins and all cross-sector negative windows must be included
in the one common compiler test.

## 6. The even-to-odd braid and the same hard gate

The generalized two-sector Pascal equations give an exact middle 2-factor
and both q1 decks.  Their `AA` subgraph is a path forest, and its component
sizes are exactly the positive runs of the distinguished new coordinate.
Consequently target-depth residence requires every selected `AA` component
to have at least `d+1` vertices.  Old-coordinate residence, deeper protected
occurrences, and the common physical compiler are separate conditions.

Thus q1-perfect algebra does not imply the hypothesis of Theorem 2.2.  A
valid even-to-odd induction package must select the Pascal sector solution
and residence together, then pass the upper occurrence and common-`Q`
compiler gates.  The fixed-path `k=15` generalized-braid solution with 1,527
residence defects is a calibration of this distinction, not a general
counterexample.

## 7. Precise minimal countercondition

The retained factorized certificates provide a direct calibration.  At
`k=11,12,13,14,15`, their authenticated middle chronologies are
upper-complete and their literal compilers are feasible, so the corresponding
certified packages have

\[
                         u(T)=\lambda_d(T)=0.          \tag{7.1}
\]

The `k=16` length-`B(16)+1` word proves the global numerical upper bound but
does not, merely from its length, certify a `W+d` flat prefix with
`u+lambda<=1`; no such inference is made here.

The Pascal residence dichotomy also matches the construction record.  The
steps `5->6`, `11->12`, and `13->14` are depth drops, while `7->8`,
`9->10`, and `15->16` are plateaux.  The six-piece intersection lift succeeds
on the displayed larger depth-drop calibrations and its fixed source fails
residence on the displayed plateau calibrations.  Corollary 5.2 explains the
direction of this evidence, but does not turn those finite failures into a
uniform converse.

For an all-`k` shadow-braid proof with additive constant `C`, it is enough to
prove the following bounded-defect package property.

> **BDP(C).**  For every `k`, there is a factor-resident middle permutation
> `T_k`, obtained by any literal carrier/braid construction, and one selected
> common-`Q` compiler package such that
>
> \[
>              u(T_k)+\lambda_{d(k)}(T_k)\le C.       \tag{7.2}
> \]

Theorem 2.2 proves

\[
              \mathrm{BDP}(C)\Longrightarrow
              \nu(k)\le B(k)+C\quad\text{for all }k. \tag{7.3}
\]

In the robust two-boundary branch, `lambda` may be replaced by the explicit
prefix defect (3.5).  The seam identity and run-boundary pair lemma show why
two-component topology and q1 count are not additional asymptotic costs.

Inside the owner-stutter/two-fan Pascal architecture of (5.6)--(5.10), the
corresponding optimized condition is boundedness of both the residence
multicover `tau_d` and the residual compiler deletion number `eta_d`.  A
single mixed common-`Q` cover core refutes only one fixed pin selector; it
does not refute `B(k)+O(1)`.  A negative theorem for that architecture must
show that one of these two optimized integer quantities is unbounded.

The exact ways a proposed package can fail are now separated.

1. **Hard carrier failure:** no factor-resident middle permutation is
   produced.  On an odd-to-even deadline plateau, failure to provide the
   extra run unit is one concrete instance.
2. **Hard occurrence failure:** an upper or protected lower target has no
   surviving/new literal occurrence after the seam surgery.
3. **Hard common-`Q` failure:** CQ0, CQ1, or CQ2 fails after all negative
   pins are intersected.  This cannot be repaired by a rankwise matching.
4. **Soft compiler defect:** common `Q` passes, but the maximum simultaneously
   installable lower family leaves `lambda_d(T)` targets.  In a robust
   one-cell atlas this is exactly Hall deficiency; in a two-boundary atlas it
   is (3.5).

Equivalently, without choosing a robust one-cell atlas, the exact soft
obstruction is an unavoidable edge of the bounded-rank negative-window
conflict hypergraph described after (2.12).  Ordinary Hall sees only the
special case in which every incompatibility is literal address contention.

Therefore a rigorous negative result against this route must show, with the
correct quantifier, that for infinitely many `k` every candidate package has
a hard failure or has soft defect tending to infinity.  A failed fixed
carrier, a scalar depth count, a local-minimum switch library, or separately
feasible sector compilers do not establish that countercondition.

Conversely, the weakest concrete positive target exposed here is not a full
exact compiler theorem: construct carriers for which the hard gates pass and
the exact deletion number in (2.7), or the prefix defect in (3.5), stays
bounded.  That alone already yields the nontrivial general upper bound
`B(k)+O(1)`.

## 8. Audit boundary

Proved in this note:

* the common-`Q` characterization of the maximum simultaneously compilable
  lower family;
* the bounded-rank conflict-hypergraph representation and product-mass
  alteration bound (proved in the companion report cited after (2.11));
* the literal additive-defect upper bound (2.8);
* the robust-core Hall augmentation theorem and exact prefix-defect formula;
* the cut/join window count and its bounded-defect corollary; and
* the exact odd-to-even deadline drop-or-plateau dichotomy.

Not proved:

* `BDP(C)` for any uniform constant `C`;
* existence of uniformly resident upper-complete PBBS/Pascal carriers;
* automatic common-`Q` composition from separate sector compilers;
* an unconditional `B(k)+O(1)` upper bound; or
* the exact formula beyond the certified finite range.
