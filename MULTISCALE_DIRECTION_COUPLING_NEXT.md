# Multiscale contraction and direction-labelled realizability

## 1. Outcome

This note attacks the remaining obstruction in
MIXED_PROFILE_SEAM_NEXT.md and LARGE_DEFECT_DICHOTOMY_NEXT.md.
It uses neither the rejected A'/B' charging scheme nor a pointwise run
ceiling.

There are five conclusions.

1. The predecessor couplings and predecessor gaps at different dangerous
   thresholds are not independent. They are all contractions of one ordered
   marked plateau list. For a surviving successor, the preceding gap is
   monotone under threshold increase, and when a plateau is deleted its
   length and its two adjacent gaps are merged additively. This gives an
   exact finite multiscale law.
2. The particular broad thresholdwise ledger in Section 6 of
   MIXED_PROFILE_SEAM_NEXT.md cannot be obtained from one labelled order.
   On a positive band of successor lengths it changes a positive gap into
   a zero gap as the threshold is raised, contradicting gap monotonicity.
3. This does **not** eliminate the broad length profile. There is a single
   explicit alternating-pair order whose contractions, at every fixed
   threshold, have the broad measure
   \[
                    \mu(dx)=2\mathbf 1_{[1,2]}(x)\,dx,
   \]
   satisfy the exact additive gap law, satisfy direction-labelled absorption
   capacity with one fixed set of labels, and have modified scalar cost
   strictly greater than four at every threshold. Hence nested scalar
   length/gap bookkeeping, even with direction-labelled line capacity, is
   still insufficient.
4. The same alternating-pair object cannot be lifted to actual selected
   coordinate lines in the three-box hexagon. As the threshold tends down
   to one, absorption forces total level measure
   \(2\mathbf 1_{[0,1]}dt\). The strongest cross-line inequality would
   require zero cross-direction intersections, while line uniqueness forces
   intersection density at least \(1/4\).
5. More generally, no actual broad-profile order can saturate the integrated
   absorption-lifetime capacity \(1/2\). A finite wedge-cover count forces
   at least \((5-2\sqrt6)a-o(a)\) plateaux onto nonpositive lines, yielding
   the explicit lifetime deficit (6.14). This still leaves partial-absorption
   broad profiles open.

Thus the previous broad **static** ledger is not multiscale-realizable, but
there is a repaired broad **nested scalar** obstruction. The exact remaining
gate is the simultaneous realization of

* one threshold-contraction order,
* fixed direction and level labels,
* the tail cross-line/additive-triple inequalities, and
* the seam saving functional.

This is a strict narrowing: threshold nesting by itself is now ruled out as
the missing theorem.

## 2. The finite threshold-contraction law

Let

\[
 P_1,P_2,\ldots,P_m
\]

be pairwise disjoint plateau vertex intervals in their word order. Write

\[
 \lambda_i=|P_i|-1
\]

for their edge lengths. It is convenient first to use a cyclic order. The
linear correction is recorded below.

For a threshold \(h\), call \(i\) active when \(\lambda_i>h\). If \(i\) is
active, let

\[
 \pi_h(i)=\text{the preceding active index in cyclic order}.
\]

Let \(G_h(i)\) be the set of word positions strictly between
\(P_{\pi_h(i)}\) and \(P_i\) which lie in no active plateau, and put
\(g_h(i)=|G_h(i)|\). Changing between the edge-gap and vertex-gap
conventions changes every formula below by at most one per contraction and
therefore by only \(O(m)\) globally.

### Theorem 2.1 (tail contraction)

If \(h_1<h_2\) and \(i\) is active at \(h_2\), then

\[
\boxed{
  \pi_{h_2}(i)=\pi_{h_1}^{\,q}(i),
}
                                                              \tag{2.1}
\]

where \(q\ge1\) is the least exponent for which
\(\lambda_{\pi_{h_1}^{q}(i)}>h_2\). Moreover

\[
\boxed{
  G_{h_1}(i)\subseteq G_{h_2}(i),
  \qquad g_{h_1}(i)\le g_{h_2}(i).
}
                                                              \tag{2.2}
\]

If the indices contracted between \(\pi_{h_2}(i)\) and \(i\) are
\(j_1,\ldots,j_r\), then, up to the endpoint convention,

\[
\boxed{
 g_{h_2}(i)
  =g_{h_1}(i)
   +\sum_{q=1}^{r}\bigl(\lambda_{j_q}+g_{h_1}(j_q)\bigr).
}
                                                              \tag{2.3}
\]

#### Proof

The active list at \(h_2\) is obtained from the active list at \(h_1\) by
deleting precisely the vertices whose lengths lie in \((h_1,h_2]\).
Therefore the predecessor of \(i\) at the new threshold is obtained by
iterating the old predecessor until the first undeleted vertex is met. This
is (2.1).

The physical interval between that older predecessor and \(P_i\) contains
the old interval between \(\pi_{h_1}(i)\) and \(P_i\). It additionally
contains every deleted intervening plateau and the gaps immediately before
those plateaux. These pieces are disjoint in the vertex-gap convention,
which proves (2.2) and (2.3). QED.

### Corollary 2.2 (monotone marked-gap measures)

Fix \(h_1<h_2\), a Borel length set \(B\subset(h_2,\infty)\), and a
nondecreasing nonnegative function \(\psi\). Labelling a plateau by its
physical identity gives

\[
\sum_{\substack{i:\lambda_i\in B}}
      \psi(g_{h_1}(i))
\le
\sum_{\substack{i:\lambda_i\in B}}
      \psi(g_{h_2}(i)).                                     \tag{2.4}
\]

In particular, for every \(r\ge0\), the number of successors in \(B\) whose
preceding gap is larger than \(r\) cannot decrease as the threshold is
raised while every member of \(B\) survives.

### Edge lifetime form

For two plateau indices \(j<i\), put

\[
 H(j,i)=\max_{j<q<i}\lambda_q,
\]

with the maximum of an empty set equal to zero. The directed predecessor
edge \(j\to i\) occurs exactly on the threshold interval

\[
\boxed{
      H(j,i)\le h<\min\{\lambda_j,\lambda_i\}.
}                                                             \tag{2.5}
\]

Thus every physical seam has one contiguous threshold lifetime. The whole
family of tail couplings is encoded by one weighted predecessor tree, not by
an arbitrary collection of stationary couplings.

### Absorption-lifetime bound

Give a physical successor plateau normalized length \(s\) and fixed
absorbing line level \(t\).  Let \(p_c\) be the length of its immediate
predecessor after filtering at threshold \(c\).  As \(c\) increases,
\(p_c\) is nondecreasing: it changes only when the old predecessor is
deleted, and its replacement has length greater than the new threshold
whereas the deleted predecessor does not.

Absorption requires

\[
                     p_c-1\le t\le2-s.                        \tag{2.6}
\]

Consequently the total Lebesgue length of thresholds \(c>1\) at which this
one successor can absorb is at most

\[
                 \boxed{\min\{s-1,2-s\}_+.}                  \tag{2.7}
\]

For the broad measure, the total successor-line lifetime capacity is

\[
 2\int_1^2\min\{s-1,2-s\}\,ds={1\over2}.                     \tag{2.8}
\]

The original broad static ledger absorbs mass \(2(3-2c)\) for
\(1<c<3/2\), whose threshold integral is also \(1/2\).  It therefore
**saturates**, rather than violates, this natural lifetime bound.  Equality
forces almost every used successor to absorb for its whole available
threshold lifetime; for \(s>3/2\), it also forces \(t=2-s\).
The alternating-pair construction below realizes this saturation.  Thus
absorption-lifetime accounting alone does not close the broad case.

### Linear words

For a linear word the first active plateau has no predecessor. Theorems
2.1--2.2 hold for every other active plateau. For any fixed finite set of
thresholds, deleting one boundary successor per threshold changes normalized
seam measures by \(O(1/a)\). No continuum-uniform boundary assertion is
needed below; all contradictions use two fixed thresholds or a countable
diagonal subsequence.

## 3. The published broad static ledger violates contraction

For \(1<c<3/2\), Section 6 of MIXED_PROFILE_SEAM_NEXT.md uses the following
high-block gap allocation. Put

\[
 r(c)=\sqrt{2(c^2-3c+4)}.
\]

For successors of normalized length \(s\in[3-c,2]\), it assigns

\[
z_c(s)=
\begin{cases}
s,&3-c\le s\le r(c),\\
0,&r(c)<s\le2.
\end{cases}                                                   \tag{3.1}
\]

On \((1,3/2)\), \(r'(c)=(2c-3)/r(c)<0\). Choose fixed

\[
 1<c_1<c_2<3/2
\]

with \(c_2\) sufficiently close to \(c_1\) that
\(r(c_2)>3-c_1\). Then the length band

\[
                      B=(r(c_2),r(c_1))                       \tag{3.2}
\]

has positive measure and lies above \(c_2\). Every successor in \(B\)
survives both thresholds. At \(c_1\), (3.1) gives a gap at least
\(r(c_2)a+o(a)\); at \(c_2\), it gives gap \(o(a)\). Taking
\(\psi(z)=\mathbf1_{\{z>r(c_2)a/2\}}\) contradicts Corollary 2.2.

Therefore the displayed family of thresholdwise couplings and gap
allocations cannot come from one labelled plateau order.

This does not invalidate its stated use: it remains a correct witness that
each threshold **separately** passes the reduced scalar relaxation. It does
show that the witness cannot be promoted unchanged to a word.

## 4. A common nested broad ledger

The preceding contradiction does not eliminate the broad profile. We now
construct a different ledger which obeys Theorem 2.1 simultaneously at all
thresholds.

### 4.1 Alternating complement pairs

Let \(u\in[1,3/2]\), and pair the two lengths

\[
                        L(u)=u,
             \qquad H(u)=3-u.                                 \tag{4.1}
\]

For a large integer \(a\), divide \([1,3/2]\) into \(K_a\) bins, where

\[
                  K_a\longrightarrow\infty,
            \qquad K_a=o(a).                                  \tag{4.2}
\]

In each bin take \(a/K_a+o(a/K_a)\) pair occurrences. At the integer scale
there are about \(a/(2K_a)\) distinct low lengths in a bin, so use two
copies of each such length (with harmless endpoint rounding), form their
complementary pairs, and order them

\[
L(u_{b,1}),H(u_{b,1}),L(u_{b,2}),H(u_{b,2}),\ldots.            \tag{4.3}
\]

Thus normalized lengths within one bin differ by \(o(1)\). The two copies
of one integer level are assigned different coordinate directions; cycling
the directions along (4.3) ensures that no direction--level pair is reused.
There are three available directions for only two copies, so this is always
possible (and endpoint rounding affects \(o(a)\) marks). This prevents
hidden reuse of one geometric line in the capacity calculation. Order the
bins by increasing \(u\). Give the original adjacent plateau
blocks zero intervening gap. Integer rounding, the \(K_a\) bin transitions,
and the two word ends affect only \(o(a)\) seams and \(o(a^2)\) edge mass.

The empirical length measure is

\[
{1\over a}\sum_i\delta_{\lambda_i/a}
      \Longrightarrow2\mathbf1_{[1,2]}(s)\,ds.                \tag{4.4}
\]

Fix \(1<c\le3/2\). In a bin with \(u>c\), both members survive, so typical
tail edges alternate by reflection:

\[
                        p=3-s.                                 \tag{4.5}
\]

In a bin with \(u<c\), the low members are deleted and the high members
become consecutive; within that bin their lengths differ by \(o(1)\), so

\[
                        p=s                                    \tag{4.6}
\]

in the limiting coupling. The deleted low block immediately preceding a
surviving high block has length \(u=3-s\). Hence the complete limiting
ledger is

\[
\begin{array}{c|c|c|c}
\text{successor }s&\text{predecessor }p&\text{gap }z
      &\text{status}\\ \hline
c\le s\le3-c&3-s&0&\text{absorbed},\\
3-c<s\le2&s&3-s&\text{nonabsorbed}.
\end{array}                                                     \tag{4.7}
\]

When \(3/2<c<2\), all low members are deleted. The surviving high bins have
\(s>c\); typical edges remain within a bin, so

\[
                p=s,\qquad z=3-s,\qquad c<s\le2.              \tag{4.8}
\]

Because the bins are ordered by increasing \(u\), the retained high bins
form one prefix. Deleted whole bins accumulate in the terminal outside-word
gap, which is not used by the internal first-dangerous seam sum. The
\(o(a)\) bin transitions likewise have no limiting contribution.

Equations (4.7)--(4.8) are not independently chosen couplings. They are the
actual contractions of the single list (4.3), and (2.3) holds at every
deletion.

### 4.2 One fixed direction-labelled absorption lift

On every reflected edge \(p=3-s\), the absorption interval is the singleton

\[
               [p-1,2-s]=\{2-s\}.                             \tag{4.9}
\]

Assign the physical plateau directions cyclically among the three
coordinates, and declare the rising cross-coordinate of each plateau to be
the fixed direction of the next plateau in (4.3). Give a successor of
length \(s\) the positive fixed level

\[
                           t=2-s.                               \tag{4.10}
\]

Across the three directions, the level pushforward has total density two
on the relevant level interval. Cyclic distribution gives density \(2/3\)
in each direction, below the exact capacity \(dt\). The directions and
levels are assigned once, before the threshold is chosen. Thus this object
passes not merely the aggregate \(3dt\) relaxation but the three separate
direction-labelled line-capacity inequalities at every threshold.

This is still an abstract marked plateau list. Section 6 proves that its
line labels cannot be embedded as actual selected coordinate lines.

## 5. Scalar cost of the nested ledger

For the broad tail,

\[
         e_c=(2-c)^2.                                         \tag{5.1}
\]

On a reflected edge the seam is absorbed. On a high identity edge in
(4.7)--(4.8),

\[
p=s,\qquad z=3-s,
\]

so

\[
\begin{aligned}
H\text{-density}&=(s-c)(3-s),\\
\phi(s,s,3-s)
  &=\min\{s,1\}(2s-3)=2s-3.
\end{aligned}                                                   \tag{5.2}
\]

The factor two below is the density of the broad length measure.

For \(1<c\le3/2\), the modified scalar value is

\[
\begin{aligned}
U_1(c)
&=3c+2(2-c)^2
  +2\int_{3-c}^{2}(s-c)(3-s)\,ds
  -2\int_{3-c}^{2}(2s-3)\,ds\\
&={29\over3}-10c+7c^2-{5\over3}c^3.                          \tag{5.3}
\end{aligned}
\]

Its excess above four is decreasing on this interval and satisfies

\[
                        U_1(c)-4\ge U_1(3/2)-4={19\over24}.    \tag{5.4}
\]

For \(3/2\le c<2\),

\[
\begin{aligned}
U_2(c)
&=3c+2(2-c)^2
  +2\int_c^{2}(s-c)(3-s)\,ds
  -2\int_c^{2}(2s-3)\,ds\\
&={56\over3}-19c+7c^2-{1\over3}c^3.                          \tag{5.5}
\end{aligned}
\]

The minimum occurs at \(c=7-\sqrt{30}\), and

\[
       \min_{[3/2,2]}(U_2(c)-4)
         ={331\over3}-20\sqrt{30}
         =0.788821\ldots>0.                                   \tag{5.6}
\]

Thus

\[
\boxed{
      U_c>4\quad\text{for every fixed }1<c<2
}
                                                              \tag{5.7}
\]

in one common nested scalar ledger.

This proves a no-go theorem for a purely multiscale scalar attack: adding
the exact threshold-contraction and additive-gap laws to the mixed seam
functional still does not force a strict-sub-four assignment.

## 6. Why the nested ledger is not line-realizable

Although the direction labels in Section 4.2 satisfy separate line
capacity, they do not satisfy the geometry of the selected coordinate
lines.

Let the dangerous threshold tend down to one through continuity values. The
nonreflected high block has vanishing mass. On every remaining reflected
edge, (4.9) forces the successor level \(t=2-s\). Therefore any putative
line realization has total limiting level measure

\[
               \nu_x+\nu_y+\nu_z
                    =2\mathbf1_{[0,1]}(t)\,dt.                 \tag{6.1}
\]

Line uniqueness gives \(\nu_i\le dt\). Write

\[
                        a_i=\nu_i([0,1/2]).                    \tag{6.2}
\]

Then

\[
                a_x+a_y+a_z=1,
            \qquad0\le a_i\le1/2.                             \tag{6.3}
\]

Every pair of levels in \([0,1/2]\) from different directions gives two
coordinate lines which genuinely intersect in the hexagon, since
\(u+v\le1\). Hence the normalized intersecting-pair density obeys

\[
\begin{aligned}
I
&\ge a_xa_y+a_ya_z+a_za_x\\
&=\frac{1-(a_x^2+a_y^2+a_z^2)}2
\ge\frac14.                                                    \tag{6.4}
\end{aligned}
\]

The last inequality is sharp at \((1/2,1/2,0)\). Because all limiting
levels are nonnegative and absolutely continuous, the additive-triple
density is

\[
                             \theta=0.                         \tag{6.5}
\]

On the other hand, the broad tail has

\[
                f=2,\qquad\ell=3,\qquad\tau=1.                \tag{6.6}
\]

The strongest mixed cross-line inequality is

\[
      \ell\le2f-\tau-I+\theta.                                \tag{6.7}
\]

Substitution of (6.6) requires \(I\le\theta=0\), contradicting (6.4).

This argument is legitimately obtained as \(c\downarrow1\): for each fixed
\(c>1\) the cross-line theorem applies, the exceptional high block has mass
\(O(c-1)\), and a diagonal subsequence followed by \(c\downarrow1\) gives
(6.1)--(6.7). No theorem at the literal threshold \(c=1\) is assumed.

### 6.1 Every lifetime-saturating broad realization is impossible

The preceding \(I\ge1/4\) calculation uses the explicit level choice of the
alternating-pair ledger.  A second argument excludes **every** actual broad
realization which saturates the absorption-lifetime bound (2.8).

Let \(A_a(c)\) be the normalized number of absorbed successors at threshold
\(c\).  If

\[
 \mu_a\Longrightarrow2\mathbf1_{[1,2]}(s)\,ds
 \quad\text{and}\quad
 \int_1^2 A_a(c)\,dc\longrightarrow {1\over2},                \tag{6.8}
\]

then the nonnegative individual lifetime deficits in (2.7) have sum
\(o(a)\).  Away from arbitrarily small endpoint bands, every plateau has
available lifetime bounded below.  Hence all but \(o(a)\) of the
\((2+o(1))a\) plateaux absorb at some threshold.  Every such plateau has
strictly positive fixed level, because \(t\ge p_c-1>c-1>0\).

This is incompatible with covering the hexagon. Here is a quantitative
finite count. Let \(q_a a\) be the number of selected plateaux whose fixed
line has nonpositive level. Broad edge mass gives

\[
 \sum_P\lambda(P)=(3+o(1))a^2.
\]

Plateau edge sets are disjoint and plateau vertex overlaps number only
\(O(a)\), so their vertex union, and therefore the union \(\Lambda\) of
their complete coordinate lines, misses only \(o(a^2)\) points of \(H_a\).

For each coordinate direction \(d\) and each missing positive integer level
\(t\in\{1,\ldots,a\}\), consider the \(t-1\) points on the line \(d=t\)
whose other two coordinates are strictly negative.  These wedge sets are
disjoint over \(d,t\).  They lie on no selected positive line.  One selected
negative line in either other direction covers at most \(2a\) wedge points
in total.

There are only \((2-q_a+o(1))a\) positive-level plateaux, hence at most that
many distinct selected positive lines. (Any same-line repetition only makes
the bound stronger.) Therefore the total number of missing positive levels
across the three directions is at least

\[
                         (1+q_a+o(1))a.                        \tag{6.9}
\]

If the three missing-level counts are \(r_1,r_2,r_3\), the smallest possible
total wedge size is

\[
 \sum_{i=1}^3 {r_i(r_i-1)\over2}
 \ge { (r_1+r_2+r_3)^2\over6}-O(a).                          \tag{6.10}
\]

The nonpositive selected lines can cover at most \(2q_a a^2+o(a^2)\) of
these points.  Since \(\Lambda\) misses only \(o(a^2)\), (6.9)--(6.10) give

\[
             {(1+q)^2\over6}\le2q
 \quad\text{for every limit point }q\text{ of }q_a.           \tag{6.11}
\]

Therefore

\[
                 q\ge q_0:=5-2\sqrt6=0.101020\ldots.          \tag{6.12}
\]

A nonpositive line can never be an absorbing successor.  Under the broad
length measure, the least total available lifetime carried by any plateau
subfamily of normalized count \(q\) is obtained from equal endpoint bands:

\[
 \inf_{\mu(B)=q}\int_B\min\{s-1,2-s\}\,d\mu(s)
                         ={q^2\over8}.                         \tag{6.13}
\]

Combining (6.12)--(6.13) proves the strict lifetime deficit

\[
\boxed{
 \limsup_{a\to\infty}\int_1^2 A_a(c)\,dc
 \le {1\over2}-{(5-2\sqrt6)^2\over8}.
}                                                             \tag{6.14}
\]

In particular, (6.8) is impossible.  This theorem is stable under
vanishing perturbations of the broad profile, but it does not exclude a
partial-absorption broad realization: the explicit deficit in (6.14) is
small, and no argument here converts it into a strict-sub-four seam value at
one threshold.

### Interpretation

The alternating-pair object satisfies

* one common successor order,
* exact gap coalescence,
* fixed direction labels,
* fixed positive absorption levels, and
* separate \(dt\) line capacities,

but it fails because those labelled lines cannot coexist with the required
plateau edge mass in the hexagon. Thus the missing resource is not merely
the name of a direction. It is the joint direction--level intersection
geometry.

## 7. The combined realizability relaxation

The preceding results suggest the correct next object. A realizable limiting
ledger must consist of the following **single** marked process.

1. A stationary or boundary-negligible ordered process of marks

   \[
      (s_i,d_i,t_i,r_i,g_i),                                  \tag{7.1}
   \]

   where \(s_i\) is length, \(d_i\) is the fixed coordinate direction,
   \(t_i\) is its fixed level, \(r_i\ne d_i\) is the rising
   cross-coordinate, and \(g_i\) is the base predecessor gap.
2. For every threshold \(c\), the tail process is obtained by contracting
   the marks with \(s_i\le c\), exactly as in Theorem 2.1. No new coupling
   or gap allocation is chosen.
3. Absorption at a tail edge \(i\to j\) is allowed only when

   \[
       d_j=r_i,\qquad s_i-1\le t_j\le2-s_j.                    \tag{7.2}
   \]
4. The one fixed family of direction--level measures, restricted to
   \(s>c\), satisfies at every continuity threshold the strongest cross-line
   gate

   \[
   \ell(c)\le
   2f(c)-\tau(c)
   -{f(c)^2-\sum_d\alpha_d(c)^2\over2}
   +\eta(c)+\theta(c),                                        \tag{7.3}
   \]

   where \(\eta\) and \(\theta\) arise from the same three level sets, not
   from independent threshold optimizations.
5. The modified seam value is computed from the actual contracted triples
   \((p_c,s,z_c)\):

   \[
   U(c)=3c+2e(c)+H(c)
   -\int\min\{p,(4-s-z)_+\}(s-z)_+\,d(\rho_c-\alpha_c).
                                                                   \tag{7.4}
   \]

Every actual three-box middle order produces such data. Therefore a proof
that every such process has \(U(c)<4\) at some common threshold would, by
the large-defect transfer theorem, force a positive quadratic local defect.

The alternating-pair process proves that Items 1--3 and (7.4) alone are
insufficient. Section 6 proves that one natural optimizer is removed by
Item 4. What is not yet proved is that **every** process satisfying
Items 1--4 must have a strict-sub-four threshold.

## 8. Adversarial audit

### 8.1 Label identity is essential in Section 3

Weak marginal measures alone cannot compare the gap attached to one
successor at two thresholds. Theorem 2.1 compares the same physical
plateau. The contradiction in Section 3 uses a whole length band on which
every successor is positive-gapped at the first threshold and zero-gapped
at the second, so relabelling within an equal-length atom cannot repair it.

### 8.2 Boundary and endpoint conventions

One first successor per fixed threshold is discarded in a linear word.
Shared plateau endpoints change (2.3) by \(O(1)\) per deletion. There are
\(O(a)\) plateaux, so all normalized formulas change by \(o(1)\) or
\(o(a^3)\) in the cost ledger. No cyclic wraparound witness is used in an
OR array.

### 8.3 Terminal deleted bins

For \(c>3/2\), the bins are ordered so that the retained high bins form one
prefix and all deleted whole bins lie in the terminal outside-word gap.
First-dangerous service uses only internal predecessor gaps. Hence that
macroscopic boundary reservoir contributes neither seam charge nor
guaranteed saving. Only \(o(a)\) bin transitions remain exceptional.

### 8.4 Direction-labelled capacity is not line geometry

The cyclic direction assignment in Section 4.2 proves only

\[
       \kappa\{d=d_0,t\in B\}\le |B|
\]

for each direction. It does not prove that the corresponding coordinate
lines and plateau intervals can be embedded in \(H_a\). Section 6 explicitly
finds the violated cross-line inequality, so no geometric construction is
claimed.

### 8.5 No rejected seam claims are used

The proof never asserts a pointwise run ceiling, a bounded-congestion
poison union, a staircase normal form, or the live-trace A'/B' injection.
The only seam saving is the independently audited integrand

\[
            \min\{p,(4-s-z)_+\}(s-z)_+.
\]

### 8.6 Why this does not prove the three-box theorem

The displayed broad static ledger is eliminated, but it was only one
optimizer of a relaxed fixed-threshold problem. The new paired process
shows that multiscale scalar feasibility survives. Although that particular
process fails (7.3), another marked process could trade absorption, line
levels, direction balance, and gap placement differently. Excluding all
such processes is exactly the remaining theorem.

## 9. Theorem ledger

### Proved here

1. The exact finite threshold-contraction, gap-monotonicity, additive-merge,
   and seam-lifetime laws.
2. Non-realizability of the specific broad thresholdwise ledger from
   MIXED_PROFILE_SEAM_NEXT.md.
3. A single explicit nested broad scalar ledger satisfying additive gap
   contraction at every threshold.
4. A fixed direction-labelled absorption-capacity lift of that nested
   ledger.
5. The exact scalar values (5.3)--(5.7), all strictly greater than four.
6. Non-realizability of the lift by actual selected coordinate lines, via
   the quantitative intersection lower bound \(I\ge1/4\).
7. The quantitative lifetime deficit (6.14) for every actual broad
   realization.
8. The combined marked-process relaxation (7.1)--(7.4) as a necessary
   condition for an actual middle order.

### Not proved

1. Exclusion of every marked process satisfying (7.1)--(7.4).
2. A quadratic lower bound for every three-box word.
3. A subquadratic three-box construction.
4. A realizable broad plateau order in the hexagon.
5. The all-\(k\) contiguous-OR conjecture.

The next valid mathematical target is now narrower than “couple thresholds”:
threshold contraction and even direction-labelled capacity admit the broad
profile. One must couple the contracted successor edges to the **same
direction--level line arrangement** which satisfies (7.3), or prove that no
such arrangement can keep (7.4) above four at every threshold.
