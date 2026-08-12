# Adversarial cross-audit: necklace rounding and coupled two-block switches

Date: 2026-07-24

Source audited: `MATH_ATTACK_W_NECKLACE_ROUNDING_REPORT_RAW_20260724.md`.

No web search and no finite or computational search were used.  The switch
was reconstructed directly from the pair-flip word, and all constants below
were rederived independently.

## 0. Verdict

The report contains a genuine exact two-necklace switching theorem and a
valid conditional route to a literal contiguous-OR word.  Its principal
enumerative constants survive audit:

\[
 V_h=(\sqrt\pi+o(1))W\sqrt m,
 \qquad
 \mathbb E E=\left(\frac{\sqrt\pi}{e}+o(1)\right)W\sqrt m,
\]

the one-block old-only mass is

\[
 2+8\min\{d,\ell-2\},
\]

and the coupled two-block old-only mass is

\[
 8\max\{0,\min(d,\ell-2)-1\}.
\]

The coupled switch really preserves the complete middle multiplicity vector
and both depth-one multiplicity vectors.  At every deeper certified rank its
effect is a sum of two signed \(2\times2\) rectangles.  In particular, it
preserves every ground-coordinate point margin separately at every rank and
sign.

The following corrections and scope restrictions are necessary.

1. The exact switch theorem is underspecified in the raw report.  It needs
   \(\ell\ge3\), a common certification type, a common core and exterior,
   and synchronization of the complete outside direction trace and phase.
   The asymptotic hypotheses eventually imply \(\ell\ge3\), but an exact
   theorem must say so.
2. The sentence “a fully occupied rectangle is collision-neutral” is false
   if “occupied” means load at least one.  Such a rectangle is
   nonimproving; it is neutral only when every decremented cell is already
   overloaded.
3. The local context-row and local-colour column sums do vanish.  The
   context rows vary between switches, however, so no single global fine
   row table has been defined.  The genuine switch-independent global
   invariant is the vector of coordinate point margins.
4. The independent Bernoulli calculation is a theorem.  The projected-
   middle compatibility estimate alone does not imply Poisson shadow loads
   for every middle-matching algorithm.  Poisson follows only under the
   additional fixed-tuple factorization hypothesis stated in the report.
5. The one-block replacement identity is exact.  Its transitive average
   gives an additive inequality \(n_1\ge n_0-o(W)\); the displayed
   multiplicative version is justified only in the nonsuccess regime
   \(n_0\not=o(W)\).  The abstract \(0,1,3\) profile shows only that this
   averaged inequality is insufficient.  It is not a physical local
   minimum and does not rule out using the full family of one-block
   inequalities.
6. The Packet-Gain Lemma is a sufficient integral local-descent hypothesis,
   and its stated implication is valid after making slot neutrality
   explicit.  It is not an equivalent or “exact” missing theorem.  Its
   sublinear packet bound is not used in the descent or in the final word
   construction and makes it strictly stronger than mere existence of one
   low-excess typed multiset.

Thus the report is a valid conditional construction plus an exact local
primitive, but “sharp reduction” and “exact missing theorem” must be read as
one proposed sufficient route, not as a necessary characterization of the
remaining contiguous-OR problem.

## 1. Radius law, rounding, and slot ledgers

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \rho_q=\frac{N_q}{W},\qquad R=2\ell,
\]

and assume

\[
 \frac h{\sqrt m}\longrightarrow\infty,qquad
 h=o(m^{2/3}),\qquad h=o(\ell),\qquad \ell=o(m).
\]

Define

\[
 p_0=1-\rho_1,qquad
 p_d=\rho_d-\rho_{d+1}\quad(1\le d<h),qquad
 p_h=\rho_h.
\]

### 1.1 Exact tail and moment identities

If \(D\) has law \(p_d\), then telescoping gives

\[
 \Pr(D\ge q)=\rho_q\quad(1\le q\le h),
 \qquad \sum_{d=0}^hp_d=1.
\]

Discrete tail summation gives the two exact identities

\[
 \sum_{d=0}^h(2d+1)p_d
 =1+2\sum_{q=1}^h\rho_q                                      \tag{1.1}
\]

and

\[
 \sum_{d=0}^h(2d+1)^2p_d
 =1+8\sum_{q=1}^h q\rho_q.                                  \tag{1.2}
\]

The local central-binomial estimate and a Gaussian tail bound yield

\[
 \sum_{q=1}^h\rho_q
 =\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m,
 \qquad
 \sum_{q=1}^h q\rho_q
 =\left(\frac12+o(1)\right)m.                                \tag{1.3}
\]

For example, for \(q=O(\sqrt m)\),

\[
 \log\rho_q=-q^2/m+o(1),
\]

while the elementary ratio product gives a summable bound of the form

\[
 \rho_q\le \exp\!\left(-\frac{q^2}{m+q}\right).
\]

The hypothesis \(h/\sqrt m\to\infty\) makes truncation beyond \(h\)
negligible.  Therefore

\[
 V_h:=W+2\sum_{q=1}^hN_q
   =(\sqrt\pi+o(1))W\sqrt m,                                 \tag{1.4}
\]

and the second moment omitted from the raw report has the sharper value

\[
 \sum_{d=0}^h(2d+1)^2p_d=(4+o(1))m.                          \tag{1.5}
\]

### 1.2 Rounding constants

Choose nonnegative integers \(k_d\) with

\[
 k_d=\frac{Wp_d}{R}+\epsilon_d,qquad |\epsilon_d|\le1.
\]

Then

\[
 \left|R\sum_{d=0}^hk_d-W\right|
 \le R(h+1),                                                  \tag{1.6}
\]

and, by (1.1),

\[
 \left|R\sum_{d=0}^h(2d+1)k_d-V_h\right|
 \le R\sum_{d=0}^h(2d+1)
 =R(h+1)^2.                                                   \tag{1.7}
\]

Both errors are \(o(W)\).  More strongly, for every \(q\),

\[
 \left|R\sum_{d=q}^hk_d-N_q\right|
 \le R(h-q+1).                                                \tag{1.8}
\]

Consequently, on the rounded type fibre,

\[
 \left|R\,|\mathcal M|-W\right|
 +2\sum_{q=1}^h\left|Rn_{\ge q}-N_q\right|
 \le R(h+1)^2=o(W).                                          \tag{1.9}
\]

Thus approximate rank-by-rank slot balance is already forced directly by
the chosen type counts.  The rigidity inequality in the report remains
useful for arbitrary, not-yet-type-fixed selections, but collisions are not
needed to prove (1.9) on the rounded fibre.

### 1.3 Rigidity inequality and coverage identity

For each class \(j\)—the middle class or one fixed rank and sign—let
\(T_j,V_j,E_j,U_j\) denote its slot count, number of targets, collision
excess, and number of holes.  Since

\[
 |\{S:c_S>0\}|=T_j-E_j,
\]

one has

\[
 T_j-V_j=E_j-U_j.                                             \tag{1.10}
\]

Write \(\delta_j=T_j-V_j\).  Since
\(\delta_j^+\le E_j\),

\[
 \sum_j|\delta_j|
 =2\sum_j\delta_j^+-\sum_j\delta_j
 \le2E+|T-V_h|.                                               \tag{1.11}
\]

This is exactly the boxed rigidity inequality in the raw report, with the
constant \(2\) intact.  Summing (1.10) also gives

\[
 \boxed{U=V_h-T+E.}                                           \tag{1.12}
\]

By (1.7), \(|T-V_h|=o(W)\) on the rounded type fibre, and hence

\[
 E=o(W)\quad\Longleftrightarrow\quad U=o(W).                  \tag{1.13}
\]

All claims in Section 1 of the raw report are therefore valid; (1.8)--(1.9)
are useful strengthenings and clarify which part follows from type rounding
alone.

## 2. Independent rounding and the projected-middle claim

### 2.1 Exact Bernoulli calculation

For the canonical typed fractional cover, besides

\[
 \sum_{e\ni S}x_e=1,
\]

the variance calculation uses the type-mass identity

\[
 \sum_{e:d(e)=d}x_e=\frac{Wp_d}{R}.                            \tag{2.1}
\]

This follows by summing the type-\(d\) middle degrees.  It should be stated
explicitly.  If parallel parameter occurrences are retained, the Bernoulli
variables are indexed by those labelled occurrences; this is consistent
with the multiset convention used later.

For a target \(S\), let \(C_S\) be its independently selected load.  Since
\(\mathbb EC_S=1\),

\[
 \mathbb E(C_S-1)_+
 =\mathbb EC_S-\Pr(C_S>0)
 =\Pr(C_S=0).                                                  \tag{2.2}
\]

If \(\varepsilon_m=\max_ex_e=o(1)\), then uniformly in \(S\),

\[
\begin{aligned}
 \log\Pr(C_S=0)
 &=\sum_{e\ni S}\log(1-x_e)\\
 &=-1+O\!\left(\sum_{e\ni S}x_e^2\right)
 =-1+O(\varepsilon_m).
\end{aligned}                                                 \tag{2.3}
\]

Equations (1.4), (2.2), and (2.3) give

\[
 \boxed{
 \mathbb EE
 =\left(\frac{\sqrt\pi}{e}+o(1)\right)W\sqrt m.}
                                                                    \tag{2.4}
\]

The constant \(\sqrt\pi/e\) is correct.

### 2.2 Efron--Stein constant

A type-\(d\) edge contains

\[
 K_d=R(2d+1)
\]

certified masks.  Resampling its Bernoulli variable changes \(E\) by at
most \(K_d\).  Efron--Stein therefore gives

\[
 \operatorname{Var}E
 \le\sum_ex_e(1-x_e)K_e^2
 \le\sum_ex_eK_e^2.                                          \tag{2.5}
\]

Using (2.1) and (1.5),

\[
\begin{aligned}
 \sum_ex_eK_e^2
 &=WR\sum_dp_d(2d+1)^2\\
 &=(4+o(1))WRm.
\end{aligned}                                                 \tag{2.6}
\]

Thus

\[
 \frac{\operatorname{Var}E}{(\mathbb EE)^2}
 =O(R/W)=o(1),                                                 \tag{2.7}
\]

and Chebyshev yields

\[
 E=\left(\frac{\sqrt\pi}{e}+o_{\Pr}(1)\right)W\sqrt m.
                                                                    \tag{2.8}
\]

The independent-rounding failure is therefore a proved, concentrated
statement.

### 2.3 What the compatibility estimate does and does not prove

Let \(\mathcal F_S\) be a nonmiddle target clique in a projected reservoir
of degree \(\Delta\), and let \(e\in\mathcal F_S\).  For each middle mask
\(X\in\bar e\), the mixed codegree estimate gives

\[
 |\{f\in\mathcal F_S:X\in\bar f\}|
 \le\left(\frac2{m-h}+o(m^{-1})\right)\Delta.
\]

A union bound over the \(R\) middle masks of \(\bar e\) proves

\[
 |\{f\in\mathcal F_S:\bar f\cap\bar e\ne\varnothing\}|
 \le(2+o(1))\frac{R\Delta}{m-h}=o(\Delta),                    \tag{2.9}
\]

because \(R=o(m)\).  This exact conclusion is valid: a
\(1-o(1)\) fraction of ordered pairs in each target clique are compatible
with the projected middle-matching constraint.

Equation (2.9) alone does not force a Poisson load law.  A deliberately
shadow-correlated selection of projected blocks may use the many compatible
pairs in a highly nonfactorizing way.  A sufficient precise version of the
extra hypothesis is:

- \(|\mathcal F_S|=(1+o(1))\Delta\);
- each \(e\in\mathcal F_S\) has marginal
  \((1+o(1))/\Delta\);
- uniformly for every fixed \(r\), every projected-middle-disjoint
  \(r\)-tuple is selected with probability
  \((1+o(1))\Delta^{-r}\);
- incompatible tuples are never selected.

Then (2.9) makes the proportion of incompatible fixed \(r\)-tuples
\(o(1)\), so

\[
 \mathbb E(C_S)_r=1+o(1)
\]

for each fixed \(r\).  The factorial moments give
\(C_S\Rightarrow\operatorname{Poisson}(1)\).  Thus the conditional
sentence in the raw report is sound, but the heading “base-only nibbles fail
sharply” must not be interpreted as a theorem about every algorithm that
first enforces middle disjointness.

Finally,

\[
 \frac1{V_h}\sum_S\Pr(C_S=0)=\frac{\mathbb EU}{V_h}.           \tag{2.10}
\]

The claimed \(o(m^{-1/2})\) average is exactly the requirement
\(\mathbb EU=o(W)\).  A law merely having some successful outcome, or even
having high-probability success with too large a failure probability, need
not satisfy (2.10).  “Successful law” should mean an expected-defect
guarantee or a sufficiently strong outcome-wise guarantee.

## 3. One-block descent

### 3.1 Exact replacement identity

Let \(A\) be a selected simple certified edge and let \(B\) be another
edge of the same type.  Put \(c_S=c_S(\mathcal M)\).  Directly,

- removing an occurrence at load \(c\ge2\) lowers excess by one;
- removing the sole occurrence at load one leaves excess unchanged;
- adding at positive load raises excess by one;
- adding into a hole leaves excess unchanged.

Because \(|A\setminus B|=|B\setminus A|\), these contributions rearrange
to

\[
 \boxed{
 E(\mathcal M-A+B)-E(\mathcal M)
 =|(A\setminus B)\cap\{c=1\}|
  -|(B\setminus A)\cap\{c=0\}|.}                              \tag{3.1}
\]

The raw identity is exact.

### 3.2 Exact content of the transitive average

Let \(H_j\) be the number of holes in class \(j\), and let \(n_0,n_1\)
be the total numbers of load-zero and load-one targets in the whole band.
At a one-block local minimum, (3.1) is nonnegative for every selected
type-\(d\) block \(A\) and every physical type-\(d\) block \(B\).

Average \(B\) over the transitive full type-\(d\) family.  A hole cannot
belong to \(A\), and a uniform type-\(d\) block hits a target in an eligible
class \(j\) with probability \(R/V_j\).  Dropping the nonnegative overlap
loss on the unique side gives

\[
 |A\cap\{c=1\}|
 \ge R\sum_{j\text{ eligible for }d}\frac{H_j}{V_j}.           \tag{3.2}
\]

Sum (3.2) over all selected blocks.  Every unique target is counted once,
and the number of selected slots in class \(j\) is \(T_j\).  Therefore

\[
 n_1\ge\sum_j H_j\frac{T_j}{V_j}
 \ge n_0-\sum_j(V_j-T_j)_+.                                   \tag{3.3}
\]

On the rounded type fibre, (1.9) gives the exact useful form

\[
 \boxed{n_1\ge n_0-R(h+1)^2=n_0-o(W).}                        \tag{3.4}
\]

If \(n_0\not=o(W)\), then along a subsequence on which the construction is
not already successful, (3.4) becomes

\[
 n_1\ge(1-o(1))n_0.
\]

Without that nonsuccess qualification, the multiplicative statement need
not follow when \(n_0\) is smaller than the rounding error.

The abstract profile

\[
 n_0=\frac25V_h,qquad n_1=\frac25V_h,qquad
 n_3=\frac15V_h
\]

has total slot mass \(V_h\), satisfies \(n_1=n_0\), and has
\(E=2V_h/5\).  Up to harmless integer rounding, it correctly proves that
the single averaged inequality (3.4) cannot force low excess.  It is not
shown to arise from physical necklaces or to satisfy all one-block local
inequalities.  The justified no-go is therefore against transitivity plus
this average, not against every possible theorem based on full one-block
local optimality.

## 4. Exact adjacent-direction switch

The raw report gives the correct counts but omits the finite hypotheses and
the definitions needed to verify them.  The following formulation is
self-contained.

### 4.1 Standard block model

Assume \(\ell\ge3\).  Decompose the coordinate ground set as

\[
 [2m]=C\mathbin{\dot\cup}E\mathbin{\dot\cup}Q
       \mathbin{\dot\cup}\bigdotcup_{i=1}^{\ell-2}P_i,         \tag{4.1}
\]

where

\[
 |C|=|E|=m-\ell,qquad
 Q=\{a,b,c,d\},qquad |P_i|=2.
\]

The core \(C\) occurs in every middle state, the exterior \(E\) in none,
and every active pair contributes one of its two coordinates.  A direction
word \(\pi\pi\) toggles the \(\ell\) active pairs in the order \(\pi\),
then toggles them in the same order again.  It gives a simple cyclic block
of \(R=2\ell\) middle states.

Swapping two adjacent directions in \(\pi\) makes the same swap at the two
antipodal occurrences in \(\pi\pi\).  At each occurrence, the endpoints of
the local two-edge path are unchanged and only its intermediate middle
state changes.  Hence exactly two middle positions change.  For
\(\ell\ge3\), the two removed middle masks and the two added middle masks
are distinct, so the middle old-only and new-only masses are both two.

For a depth-\(q\) lower window, only two windows at one occurrence can have
a different intersection: the window ending at the changed intermediate
state and the window beginning there.  A window containing both unchanged
local endpoints makes the intermediate state redundant in its intersection.
The same argument applies to unions.  Therefore, for

\[
 1\le q\le\ell-2,
\]

each occurrence contributes two changed lower masks and two changed upper
masks.  The two antipodal occurrences give exactly four old and four new
masks of each sign.  The presence of at least one untraversed outside
direction in this range makes the four contexts distinct.

At \(q=\ell-1\), an \(\ell\)-vertex window traverses all but one of the
\(\ell\) active directions.  Its intersection is the fixed core plus the
currently selected coordinate of the omitted pair.  As the start runs
around the cycle, each coordinate of every active pair appears once,
independently of the order \(\pi\).  The union statement is the complementary
one with the fixed exterior.  Thus the signed histogram effect at
\(q=\ell-1\) is zero, although individual window positions may change.

If the common certification type is \(d\le\ell-1\), define old-only mass as

\[
 \sum_S(\mu_{\rm old}(S)-\mu_{\rm new}(S))_+.
\]

The preceding count gives exactly

\[
 \boxed{2+8\min\{d,\ell-2\}.}                                \tag{4.2}
\]

The condition \(\ell\ge3\) is real.  For \(\ell=2\), swapping the two
directions merely reverses or rotates the four-cycle support, and the
claimed old-only middle mass fails.  In the asymptotic lane,
\(h/\sqrt m\to\infty\) and \(h=o(\ell)\) make \(\ell\ge3\) automatic for
all sufficiently large \(m\).

## 5. The coupled two-necklace diamond

### 5.1 Exact alignment hypotheses

Use the common decomposition (4.1).  The first block uses active pairings

\[
 \{a,b\}\mid\{c,d\},
\]

and the second uses

\[
 \{b,d\}\mid\{a,c\}.
\]

The two displayed \(Q\)-directions occupy the same adjacent positions in
the two direction words.  All other active pairs, their cyclic order, the
core, the exterior, their initial orientations, and the marked antipodal
phase are identical.  Both blocks have the same certification type \(d\).
This is the precise content needed from the raw phrase “aligned outside
active pairs, order, and marked state.”  Equality of only the abstract
outside pair set or order is not enough; the complete outside middle trace
must agree at corresponding positions.

At one marked occurrence the old local paths are

\[
 ac\longrightarrow bc\longrightarrow bd,
 \qquad
 ab\longrightarrow ad\longrightarrow cd,                     \tag{5.1}
\]

and the new paths are

\[
 ac\longrightarrow ad\longrightarrow bd,
 \qquad
 ab\longrightarrow bc\longrightarrow cd.                     \tag{5.2}
\]

At the antipodal occurrence all active choices are complemented and the
same calculation repeats.

### 5.2 Middle preservation and middle disjointness

The old intermediate \(Q\)-sections in (5.1) are \(bc\) and \(ad\); the
new switch merely exchanges them between the two blocks.  The endpoints do
not change.  Since the outside traces are aligned, the full combined middle
multiplicity vector is exactly unchanged at each occurrence and hence
globally.

For \(\ell\ge3\), the two old blocks are middle-disjoint, and so are the two
new blocks.  At a common outside state, their local \(Q\)-sections in
(5.1), or in (5.2), are different.  A possible equality involving opposite
antipodal halves is excluded because at least one of the \(\ell-2\) outside
active pairs is complemented between those halves.  This also explains why
the exceptional case \(\ell=2\) must be removed.

### 5.3 Exact depth-one histograms

At the marked occurrence, suppress the common outside context.  The four
old and new lower edge colours are

\[
\begin{array}{c|cccc}
 &1&2&3&4\\ \hline
 \text{old}&c&b&a&d\\
 \text{new}&a&d&b&c.
\end{array}                                                   \tag{5.3}
\]

They are the same multiset \(\{a,b,c,d\}\).  The four upper edge colours
are

\[
\begin{array}{c|cccc}
 &1&2&3&4\\ \hline
 \text{old}&abc&bcd&abd&acd\\
 \text{new}&acd&abd&abc&bcd.
\end{array}                                                   \tag{5.4}
\]

Again the multisets agree.  The antipodal occurrence has the complementary
calculation.  Therefore the coupled switch preserves the entire lower and
upper depth-one multiplicity vectors, not merely their total sizes.

### 5.4 Deeper rectangular effect

Fix

\[
 2\le q\le\min\{d,\ell-2\}.
\]

For antipodal phase \(\sigma\in\{0,1\}\), let
\(L_{\sigma,q}\) be the common outside-\(Q\) intersection context in the
depth-\(q\) window ending at the changed intermediate state, and let
\(R_{\sigma,q}\) be the corresponding context in the window beginning
there.  These contexts have size \(m-q-1\) and avoid \(Q\).  With
\(\Delta=\text{new}-\text{old}\), direct cancellation of the intermediate
\(a\)- and \(d\)-terms from the two blocks gives

\[
\boxed{
 \Delta_q^-=
 \sum_{\sigma=0}^1
 \left(
  \mathbf1_{L_{\sigma,q}+b}
 -\mathbf1_{L_{\sigma,q}+c}
 -\mathbf1_{R_{\sigma,q}+b}
 +\mathbf1_{R_{\sigma,q}+c}
 \right).}                                                   \tag{5.5}
\]

For \(q=1\), one has
\(L_{\sigma,1}=R_{\sigma,1}\), which is the cancellation in (5.3).  For
\(q=\ell-1\), all outside directions in either boundary window are
traversed and again \(L_{\sigma,q}=R_{\sigma,q}\), so the signed effect is
zero.  In the displayed interior range, the left and right windows omit
different nonempty parts of the outside direction arc.  The four contexts
across the two phases are distinct enough that the four positive and four
negative lower masks in (5.5) are all distinct.

The upper formula is the complement-dual rectangle: the same calculation
uses union contexts and replaces the local singleton columns by the
corresponding \(Q\setminus\{b\}\) and
\(Q\setminus\{c\}\) columns.  It likewise has four old-only and four
new-only masks.

Thus, for every certified depth from \(2\) through
\(r=\min\{d,\ell-2\}\), the coupled move has four removed and four added
masks at each sign.  Middle and depth one have zero net histogram effect,
and depth \(\ell-1\) also has zero effect.  Its total old-only mass is

\[
 \boxed{8\max\{0,r-1\}
 =8\max\{0,\min(d,\ell-2)-1\}.}                       \tag{5.6}
\]

The two switch constants and the exact preservation claims in the raw
report therefore pass audit under the explicit hypotheses above.

## 6. Rectangle margins and the real obstruction

### 6.1 Local and global invariants

For one phase, (5.5) has coefficient matrix

\[
 \begin{pmatrix}1&-1\\-1&1\end{pmatrix}                     \tag{6.1}
\]

on rows \(L,R\) and columns \(b,c\).  Its two row sums and two column sums
vanish.  This proves the local context-row and local-colour column statement.

The contexts \(L_{\sigma,q},R_{\sigma,q}\) change from one physical
diamond to another.  Unless a coherent global table or component is first
defined, (6.1) does not give a single fine context-row invariant shared by
the whole move library.

There is, however, a genuine global invariant.  For every ground coordinate
\(i\),

\[
 \boxed{
 \sum_{S\ni i}\Delta_q^-(S)=0,
 \qquad
 \sum_{S\ni i}\Delta_q^+(S)=0.}                              \tag{6.2}
\]

For an outside coordinate, cancellation occurs within each row of (6.1).
For \(b\) and \(c\), it occurs between the two rows.  The same verification
holds in the upper complementary rectangle.  Thus every sequence of these
coupled diamonds preserves the point-margin vector separately at every
depth and sign.  It also preserves the entire depth-one load vector.

The point margins give a quantitative obstruction.  In one rank-\(r\)
class, let \(\mu(S)\) be the load and define its deviation from the all-one
cover by

\[
 a_i=\sum_{S\ni i}(\mu(S)-1).
\]

With

\[
 E_r=\sum_S(\mu(S)-1)_+,
 \qquad U_r=|\{S:\mu(S)=0\}|,
\]

one has

\[
 \boxed{
 E_r\ge\frac1r\sum_i(a_i)_+,
 \qquad
 U_r\ge\frac1r\sum_i(-a_i)_+.}                              \tag{6.3}
\]

Indeed, summing all positive occurrence deviations over their \(r\)
coordinates gives \(rE_r\), and similarly every hole contributes \(r\)
negative point incidences.  Hence a diamond component with macroscopic
point-margin imbalance has a macroscopic collision or hole floor which no
sequence of these diamonds can remove.

### 6.2 Correction of “fully occupied is neutral”

Consider one simple rectangle, let \(P\) be its incremented diagonal and
\(N\) its decremented diagonal, and let \(c\) be the pre-switch load.  Slot
neutrality gives the exact excess change

\[
 \Delta E
 =|\{x\in N:c_x=1\}|-|\{x\in P:c_x=0\}|.                    \tag{6.4}
\]

If all four cells are occupied, the second term vanishes, but the first need
not:

\[
 \Delta E=|\{x\in N:c_x=1\}|\ge0.                            \tag{6.5}
\]

Thus a fully occupied rectangle is collision-nonimproving, not necessarily
neutral.  It is neutral when both decremented cells already have load at
least two.  Equivalently, “fully overloaded” is a sufficient neutrality
condition.  This is the one literal false assertion in the switch-obstruction
list of the raw report.

The other caveats are valid and independent:

- the move cannot alter depth-one excess at all;
- the required aligned partner need not be selected;
- all point margins in (6.2) are invariant;
- one switch bit controls both signs, both antipodal phases, and every depth,
  so individually preferred rectangle orientations can conflict.

Consequently the diamond is a genuine higher-depth trade, but no expansion,
Hall, or descent theorem follows from its existence.

## 7. Middle-support rigidity

The support-rigidity statement is correct for \(\ell\ge2\).  Encode active
orientations by \(\mathbb F_2^\ell\), and let

\[
 p_j=e_1+\cdots+e_j,qquad 0\le j<\ell.
\]

Up to translation, the standard block support is

\[
 \{p_j:0\le j<\ell\}\mathbin{\dot\cup}
 \{\mathbf1+p_j:0\le j<\ell\}.                              \tag{7.1}
\]

Within one half, Johnson distance is \(|i-j|\); between halves it is
\(\ell-|i-j|\).  Hence the middle support induces exactly the chordless
cycle \(C_{2\ell}\).  Its adjacency graph determines the cyclic order up to
rotation and reversal.

Every certified lower or upper mask is respectively the intersection or
union of \(q+1\) consecutive middle states.  Rotation and reversal preserve
the multiset of all such windows.  Therefore a same-type one-block
replacement with exactly the same middle support changes no certified
shadow histogram.  This only rules out one-block moves preserving that
support; it says nothing against arbitrary one-block replacements that
change middle ownership.

## 8. Bad native chains

Inside one type-\(d\) block, the \(R\) native symmetric-chain segments are
pairwise mask-disjoint.  If a target has multiplicity \(c\ge2\), it occurs
in \(c\) native chain instances and can contaminate at most those \(c\)
instances.  Since

\[
 c\le2(c-1)\qquad(c\ge2),
\]

a union bound gives

\[
 \boxed{
 \#\{\text{bad native chains}\}
 \le\sum_{S:c_S\ge2}c_S
 \le2E(\mathcal M).}                                         \tag{8.1}
\]

The constant \(2\) is correct.  The clean-chain conclusion uses the rounded
middle-size ledger:

\[
 R|\mathcal M|=W+o(W).
\]

Thus, if \(E=o(W)\),

\[
 \#\{\text{clean native chains}\}
 \ge R|\mathcal M|-2E=W-o(W).                                \tag{8.2}
\]

Without the rounded-size hypothesis, \(E=o(W)\) alone would not imply
(8.2).  Also, (8.2) does not imply that all but \(o(W/R)\) blocks are wholly
clean: one bad chain may occur in every selected block.

## 9. Packet-Gain descent

### 9.1 Exact algebra

Let \(\mathcal A\) be a removable submultiset of \(\mathcal M\), let
\(\mathcal B\) be a physical replacement multiset with the same type
multiset, and define the net certified incidence vector

\[
 z=\iota(\mathcal B)-\iota(\mathcal A).
\]

Let \(c_S\) be the pre-replacement load.  Suppose

\[
 z_S\in\{-1,0,1\}
\]

for every certified target.  Directly,

\[
 \Delta E
 =|\{S:z_S=1,\ c_S\ge1\}|
  -|\{S:z_S=-1,\ c_S\ge2\}|.                                 \tag{9.1}
\]

Because the packets have the same type multiset, their slot counts agree in
every class.  In particular,

\[
 \sum_Sz_S=0,
 \qquad |\{z=1\}|=|\{z=-1\}|.                                \tag{9.2}
\]

Using (9.2) to complement the two sets in (9.1) gives

\[
 \boxed{
 \Delta E
 =|\{S:z_S=-1,\ c_S=1\}|
  -|\{S:z_S=1,\ c_S=0\}|.}                                  \tag{9.3}
\]

The raw formula is therefore correct, but its proof requires the slot-
neutrality step (9.2).  Without it, (9.3) is false.  The prose “holes are
added” should read “original holes are filled.”

If the second count in (9.3) is strictly larger than the first, then
\(\Delta E\le-1\).  The replacement remains integral and retains every
\(k_d\).  Since \(E\) is a nonnegative integer, repeated application ends
after finitely many moves at

\[
 E\le\eta_mW=o(W).                                             \tag{9.4}
\]

No convergence, compactness, or algorithmic-time assertion is needed.

### 9.2 Logical strength of the unproved lemma

The following parts remain completely unproved:

- existence of a support-feasible improving packet in every high-excess
  physical multiset;
- the coordinatewise bound \(z\in\{-1,0,1\}\) for such a packet;
- the simultaneous gain after all ranks, signs, and antipodal phases are
  combined;
- the sublinear packet-size bound.

Moreover, the Packet-Gain Lemma is not equivalent to low-excess necklace
rounding.  If one good typed multiset \(\mathcal M_*\) exists, replacing an
arbitrary bad \(\mathcal M\) by \(\mathcal M_*\) wholesale uses
\(\Theta(W/R)\) blocks.  It does not imply an improving packet of size
\(o(W/R)\), nor a monotone path through intermediate physical states.  The
bound

\[
 s_m=o(W/R)
\]

is not used anywhere in (9.1)--(9.4) or in the final word-length accounting.
It is an additional, strictly stronger locality demand.

Accordingly, Section 6 should be titled “one sufficient local-descent
hypothesis,” not “the exact missing theorem.”  Other logically possible
routes include a direct correlated construction, nonmonotone plateau moves,
or a global replacement whose support is not sublinear.

The raw report consistently works with physical multisets, under which
repeated copies of one physical block are allowed.  If instead a simple
reservoir selection is intended, the replacement packet must additionally
avoid block occurrences already selected outside \(\mathcal A\); that
condition is not in the stated lemma.

## 10. Conditional OR implication and exact scope

Assume the Packet-Gain hypothesis, with the multiset convention, and start
from any physical typed multiset with the rounded counts.  At termination,
(9.4) and (1.12) give

\[
 U=V_h-T+E=o(W).                                               \tag{10.1}
\]

The number of middle positions in the selected physical cycles is

\[
 R\sum_dk_d=W+O(Rh).                                          \tag{10.2}
\]

The audited cyclic linearization and endpoint padding cost

\[
 O\!\left(h\sum_dk_d\right)
 =O(hW/R)+O(h^2)=o(W),                                        \tag{10.3}
\]

because \(h=o(\ell)\) and \(R=2\ell\).  Appending the uncovered band masks
costs \(U=o(W)\).  The audited symmetric-chain product tail word has length

\[
 O\!\left(\left(1+\frac{h^2}{m}\right)N_h\right)=o(W),        \tag{10.4}
\]

since \(h/\sqrt m\to\infty\) and \(h=o(m^{2/3})\).  This is a
compressed outer-tail construction; literal enumeration of all outer masks
would require a stronger cutoff.

Combining (10.1)--(10.4), the resulting literal word has length

\[
\begin{aligned}
 L
 &\le W+O(Rh)+O(hW/R)+U+o(W)\\
 &=W+o(W).
\end{aligned}                                                 \tag{10.5}
\]

Therefore the conditional implication claimed in the raw report is valid:

\[
 \boxed{
 \text{Packet-Gain}
 \quad\Longrightarrow\quad
 \nu(2m)\le\binom{2m}{m}+o\!\binom{2m}{m}.}                  \tag{10.6}
\]

The standard trimmed one-bit lift then transfers the coefficient-one bound
to the other parity.

This route is compatible with the frozen integrality requirement because it
constructs a literal OR word from integral physical blocks; the fractional
cover in Section 2 is used only as a negative diagnostic.  It does not prove
MWB, does not construct an exact odd middle-wreath factor with balanced
histograms, and does not prove labelled common-owner synchronization.  It
also proves no converse: a coefficient-one OR word need not yield
Packet-Gain or any necklace rounding of this form.

## 11. Final audit ledger

### Proved and accepted

- the radius distribution and both rounding estimates;
- the constant \(V_h/(W\sqrt m)\to\sqrt\pi\);
- the rigidity inequality with constant \(2\) and the exact coverage
  identity;
- the independent Bernoulli constant \(\sqrt\pi/e\) and concentration;
- the projected-middle incompatibility bound (2.9);
- the one-block replacement formula;
- the adjacent-direction one-block mass (4.2), for \(\ell\ge3\);
- exact preservation of the combined middle and depth-one histograms in the
  aligned coupled switch;
- the deeper rectangular formula and coupled mass (5.6);
- local row/column cancellation and global point-margin invariance;
- middle-support rigidity;
- the bad-native-chain bound with constant \(2\);
- the packet descent algebra, conditional on the packet's existence; and
- the final literal-OR implication (10.6), conditional on Packet-Gain.

### Corrected

- “fully occupied is collision-neutral” becomes “fully occupied is
  collision-nonimproving; neutrality additionally requires the decremented
  cells to be overloaded”;
- the one-block average is naturally additive, \(n_1\ge n_0-o(W)\);
- the projected-middle Poisson conclusion requires an explicit
  factorization law;
- “context-row margins” are local, while coordinate point margins are the
  unconditional global invariant;
- the switch theorem needs \(\ell\ge3\), common type, and complete outside
  trace/phase alignment;
- “holes are added” becomes “holes are filled”; and
- Packet-Gain is a strong sufficient local theorem, not the exact or
  equivalent remaining statement.

### Unproved

- any shadow-correlated projected-middle rounding theorem with total defect
  \(o(W)\);
- availability of aligned partner blocks in an arbitrary selected multiset;
- any depth-one-capable move theorem;
- any expansion or Hall theorem overcoming the fixed point margins and the
  simultaneous multidepth sign conflicts;
- the support-feasible Packet-Gain Lemma itself; and
- any derivation of Packet-Gain from the two-necklace diamond.

The exact exhausted conclusion is therefore narrower than the raw report's
last box:

\[
\boxed{
 \begin{gathered}
 \text{The higher-depth aligned diamond is proved, but a support-feasible}\\
 \text{depth-one-capable low-excess construction remains open.}
 \end{gathered}
}
\]
