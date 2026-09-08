# Lower-neutral trade atlases: exact upper-hole descent, diameter locking, and the carrier-occurrence threshold

Date: 2026-07-26

Method: pure mathematics only.  No probabilistic independence between the
cycle, its upper defect, and a carrier frame is assumed.

## 0. Outcome

Let

\[
 \mathcal M=\binom{[n]}m,\qquad
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal U=\binom{[n]}{m+1},\qquad
 W=|\mathcal M|,
 \tag{0.1}
\]

where \(n\in\{2m,2m+1\}\).  Let \(C\) be a Hamilton cycle of
\(J(n,m)\) with complete lower support.  Thus every member of
\(\mathcal L\) is the intersection colour of at least one edge of \(C\).

This note does **not** construct an unconditional positive-density
lower-neutral trade bank.  It proves a distance/occurrence obstruction which
rules out the direct enlargement of the six-coordinate pentagon by any fixed
bounded collection of sublinear partition frames as an atlas valid for every
lower-complete Hamilton cycle.  Cycle-adaptive or sufficiently many
overlapping frames are not ruled out.

The conclusions are as follows.

1. For an arbitrary integral lower-neutral switch, the exact upper-repeat
   change is given by (2.5).  This is the missing-upper-shadow objective,
   not a lattice-span surrogate.

2. If the repeated and missing upper targets of the current cycle are at
   Johnson distance \(\rho\), no switch whose entire upper support has
   diameter less than \(\rho\) can strictly decrease the upper repeat
   excess.  This remains true with nonsquarefree coefficients.

3. A common-core carrier on a \(d\)-set has upper-support diameter at most
   \(\lfloor d/2\rfloor\).  Hence such a carrier can cross a defect gap
   \(\rho\) only if
   \[
                         d\ge 2\rho.                 \tag{0.2}
   \]

4. The scale \(\rho=\Theta(\sqrt m)\) is a genuine first-order
   possibility.  There are upper load profiles of exact mass \(W\), with
   positive-density repeats and holes separated by \(\Theta(\sqrt m)\),
   whose point margins differ from uniformity by only \(o(mW)\) in
   \(\ell^1\).  This is a load-profile construction, not a claim that such
   a profile is realized by a lower-complete Hamilton cycle.  It proves that
   scalar and point-margin information cannot certify bounded-diameter
   descent.

5. For every Hamilton cycle, the exact number \(I_D(C)\) of cycle edges
   whose exchanged pair lies in a fixed \(d\)-set \(D\) satisfies
   \[
     \sum_{D\in\binom{[n]}d} I_D(C)
       =W\binom{n-2}{d-2}.                           \tag{0.3}
   \]
   Consequently
   \[
     \mathbb E_D I_D(C)
       =W\frac{d(d-1)}{n(n-1)}.                     \tag{0.4}
   \]
   This holds for every \(C\), without using lower completeness.

6. More efficiently, let \(\Pi\) be a uniformly random partition of
   \([n]\) into \(d\)-sets.  If \(I_\Pi(C)\) counts the cycle edges whose
   exchanged coordinates lie in one part, then
   \[
     \boxed{\mathbb E_\Pi I_\Pi(C)
       =W\frac{d-1}{n-1}.}                           \tag{0.5}
   \]
   Every owner-disjoint collection of legal common-core trades carried by
   \(\Pi\) has total possible upper-repeat descent at most
   \(I_\Pi(C)\).  Thus a bounded number of random \(d=o(n)\) partitions
   has only \(o(W)\) physical descent capacity for every fixed \(C\), with
   probability tending to one.  Equivalently, no fixed such atlas can have
   \(\Omega(W)\) capacity for every lower-complete Hamilton cycle: a
   coordinate relabelling of any one lower-complete cycle defeats it.

7. In particular, increasing the pentagon diameter to
   \(d=\Theta(\sqrt m)\) addresses the possible defect distance but not the
   occurrence shortage: one random partition exposes only
   \(\Theta(W/\sqrt m)\) cycle-edge mass.  At least
   \[
                         J=\Omega(n/d)               \tag{0.6}
   \]
   genuinely different frames are necessary even to expose \(\Omega(W)\)
   negative-edge mass.  Exposure is still weaker than occurrence of a
   complete negative trade factor and weaker again than actual descent.

8. More generally, a fixed overlapping family \(\mathscr D\) of
   \(d\)-coordinate blocks cannot work for every lower-complete Hamilton
   cycle unless
   \[
                         |\mathscr D|=\Omega(n^2/d^2).          \tag{0.7}
   \]
   Indeed a coordinate relabelling makes its total exposed cycle-edge mass
   at most
   \(W|\mathscr D|\binom d2/\binom n2\).  Thus the obstruction is not an
   artefact of requiring disjoint blocks.

The surviving positive route is therefore precise.  It must use either
linear-size carriers, or \(\Omega(n/d)\) overlapping/moving frames at scale
\(d\), and it must prove a matching of complete negative factors whose
positive upper targets are holes and whose negative upper targets carry
excess.  Counting coordinate pairs or proving that the trade vectors span a
lattice does not meet this condition.

## 1. Loads and lower-neutral switches

For an edge \(e=XY\) of \(J(n,m)\), write

\[
 L(e)=X\cap Y,\qquad U(e)=X\cup Y.                  \tag{1.1}
\]

Let \(x_C\) be the edge indicator of \(C\), and let

\[
 u_C(U)=|\{e\in E(C):U(e)=U\}|.                    \tag{1.2}
\]

The upper repeat excess and upper hole set are

\[
 R^+(C)=\sum_{U\in\mathcal U}(u_C(U)-1)_+,
 \qquad
 \mathcal H(C)=\{U:u_C(U)=0\}.                     \tag{1.3}
\]

Also put

\[
 \mathcal R(C)=\{U:u_C(U)\ge2\}.                   \tag{1.4}
\]

An integral switch is a vector \(z\) on Johnson edges.  It is
owner- and lower-neutral when

\[
                         B_0z=0,\qquad B_-z=0,       \tag{1.5}
\]

where \(B_0\) records the two middle endpoints and \(B_-\) records the
intersection colour.  It is legal at \(C\) if \(x_C+z\) is the indicator
of a Hamilton cycle.  Write its upper change as

\[
 \delta=B_+z,\qquad
 \delta^+(U)=\max\{\delta(U),0\},\qquad
 \delta^-(U)=\max\{-\delta(U),0\}.                  \tag{1.6}
\]

Since every Johnson edge has one upper colour and \(B_0z=0\),

\[
 \sum_U\delta(U)=0,
 \qquad
 \sum_U\delta^+(U)=\sum_U\delta^-(U)=:s.           \tag{1.7}
\]

The number \(s\) is the number of upper edge-units moved by the switch.

## 2. The exact nonlinear descent formula

### Theorem 2.1 (exact upper-repeat variation)

For every legal switch,

\[
\boxed{
 \begin{aligned}
 R^+(C+z)-R^+(C)
  ={}&s-
     |\{U:u_C(U)=0,\ \delta^+(U)>0\}|\\
    &-\sum_U\min\{\delta^-(U),(u_C(U)-1)_+\}.
 \end{aligned}}                                    \tag{2.1}
\]

If \(\delta\) is squarefree, with positive support \(P\) and negative
support \(N\), this reduces to

\[
 \boxed{
 R^+(C+z)-R^+(C)
   =|P\setminus\mathcal H(C)|-|N\cap\mathcal R(C)|.}
 \tag{2.2}
\]

#### Proof

Put \(f(a)=(a-1)_+\).  Adding \(r>0\) units at a target of load \(a\)
changes \(f\) by \(r\) if \(a\ge1\), and by \(r-1\) if \(a=0\).
Deleting \(r\le a\) units changes \(f\) by

\[
                         -\min\{r,(a-1)_+\}.         \tag{2.3}
\]

Sum these identities and use (1.7).  Formula (2.2) is the special case in
which every nonzero coefficient has magnitude one. \(\square\)

Thus a formal nonzero upper vector is irrelevant unless it places positive
mass on current holes and deletes enough mass from current repeated targets.

### Theorem 2.2 (diameter lock)

Define

\[
 \rho(C)=d_J(\mathcal R(C),\mathcal H(C)),           \tag{2.4}
\]

with value \(+\infty\) if one family is empty.  Suppose the upper support

\[
 \operatorname {supp}\delta
   =\{U:\delta(U)\ne0\}
\]

has Johnson diameter strictly less than \(\rho(C)\).  Then

\[
                         R^+(C+z)\ge R^+(C).         \tag{2.5}
\]

#### Proof

The support cannot contain both a positive target in \(\mathcal H(C)\)
and a negative target in \(\mathcal R(C)\).  If it contains no positive
hole, the first subtraction in (2.1) is zero and the last subtraction is at
most \(s\).  If it contains a positive hole, it contains no negative
repeated target, so the last subtraction is zero and the number of positive
holes is at most the total positive mass \(s\).  In both cases the
right-hand side of (2.1) is nonnegative. \(\square\)

This is the exact extension of the diameter-two pentagon obstruction.  It
does not assume that the trade coefficients are squarefree.

## 3. Common-core carriers and their maximum reach

Fix a \(d\)-set \(D\subset[n]\), a set \(K\subset[n]\setminus D\), and an
integer \(r\).  A rank-\(r\) common-core carrier has all of its middle
owners in

\[
                         \{K\cup A:A\in\tbinom Dr\}. \tag{3.1}
\]

Every upper target appearing on an edge of this carrier is

\[
                         K\cup B,\qquad B\in\tbinom D{r+1}.   \tag{3.2}
\]

For two such targets,

\[
 d_J(K\cup B,K\cup B')=d_J(B,B')
 \le \min\{r+1,d-r-1\}
 \le\lfloor d/2\rfloor.                             \tag{3.3}
\]

Combining (3.3) with Theorem 2.2 proves (0.2).  Notice that making the local
factor combinatorially richer does not change this reach bound; only the
number of active coordinates does.

## 4. A sharp first-order \(\sqrt m\) defect gap

This section constructs a load profile, not a Hamilton cycle.

Take \(n=2m\), split \([2m]=A\sqcup B\) with \(|A|=|B|=m\), and for
\(U\in\binom{[2m]}{m+1}\) put

\[
 T(U)=|U\cap A|-{m+1\over2}.                        \tag{4.1}
\]

For a uniformly random upper target,

\[
                         {T(U)\over\sqrt m}
       \Longrightarrow N(0,1/8).                    \tag{4.2}
\]

Choose constants \(0<a<b\) for which

\[
 \Pr\{|Z|\le a\}=\Pr\{|Z|\ge b\}=:\gamma>0,
 \qquad Z\sim N(0,1/8).                             \tag{4.3}
\]

Let

\[
 \mathcal R_0=\{U:|T(U)|\le a\sqrt m\},\qquad
 \mathcal H_0=\{U:|T(U)|\ge b\sqrt m\},            \tag{4.4}
\]

with integer endpoints rounded outward.  The hypergeometric central limit
theorem gives

\[
 |\mathcal R_0|=(\gamma+o(1))|\mathcal U|,
 \qquad
 |\mathcal H_0|=(\gamma+o(1))|\mathcal U|.          \tag{4.5}
\]

One Johnson move changes \(|U\cap A|\) by at most one, hence

\[
 d_J(\mathcal R_0,\mathcal H_0)
       \ge(b-a)\sqrt m-O(1).                        \tag{4.6}
\]

Both families in (4.4) are invariant under

\[
 (S_A\times S_B)\rtimes\langle A\leftrightarrow B\rangle,
 \tag{4.7}
\]

which is transitive on the coordinate set.  Each family therefore has
exactly uniform point degrees.

Start with load two on \(\mathcal R_0\), load zero on \(\mathcal H_0\),
and load one elsewhere.  Its total mass differs from \(|\mathcal U|\) by
\(o(W)\).  Since

\[
 W-|\mathcal U|={W\over m+1}=o(W),                  \tag{4.8}
\]

changing multiplicities on \(o(W)\) targets inside the central occupied
region makes the total mass exactly \(W\), without introducing a new hole
or a new repeated target between the two bands.  The resulting point-margin
change has \(\ell^1\)-norm at most \(2(m+1)o(W)=o(mW)\).

Thus all scalar constraints are exact, point balance is asymptotically
perfect at the scale relevant to an \(\Omega(W)\) obstruction, yet the
repeat and hole supports remain \(\Theta(\sqrt m)\)-separated.  This proves
that a uniform bounded-diameter descent theorem cannot follow from the known
point-margin identity.  Chronological realizability by a lower-complete
Hamilton cycle is deliberately not asserted.

## 5. Exact physical occurrence census

For a Johnson edge \(e=XY\), let

\[
                         p(e)=X\triangle Y,          \tag{5.1}
\]

the unordered pair of exchanged coordinates.  For \(D\in\binom{[n]}d\),
put

\[
 I_D(C)=|\{e\in E(C):p(e)\subseteq D\}|.            \tag{5.2}
\]

### Theorem 5.1 (one-frame census)

For every Hamilton cycle \(C\), (0.3)--(0.4) hold.

#### Proof

Fix an edge \(e\).  Exactly \(\binom{n-2}{d-2}\) of the \(d\)-sets contain
the two coordinates in \(p(e)\).  Sum this fact over the \(W\) edges of
\(C\), then divide by \(\binom nd\). \(\square\)

Suppose a legal common-core trade in a \(D\)-fibre deletes \(s_a\) edges of
the current cycle.  Every deleted edge is counted by \(I_D(C)\), and its
upper-repeat improvement is at most \(s_a\), by (2.1).  Consequently, for
any collection \(\mathcal A_D\) of such trades whose deleted edge sets are
pairwise disjoint,

\[
 \sum_{a\in\mathcal A_D}
   \bigl(R^+(C)-R^+(C+a)\bigr)_+
 \le \sum_{a\in\mathcal A_D}s_a
 \le I_D(C).                                        \tag{5.3}
\]

If every carrier deletes at least \(s_0\) edges, its owner-disjoint packing
number is at most \(I_D(C)/s_0\).  Thus (0.4) bounds actual removable edge
mass, not merely the number of formal trade vectors.

### Theorem 5.2 (partition-frame census)

Assume \(d\mid n\), and let \(\Pi\) be a uniformly random partition of
\([n]\) into \(d\)-sets.  Put

\[
 I_\Pi(C)=\sum_{D\in\Pi}I_D(C).                     \tag{5.4}
\]

Then (0.5) holds.

#### Proof

For a fixed unordered coordinate pair, after placing its first coordinate,
exactly \(d-1\) of the remaining \(n-1\) positions lie in the same part.
Therefore

\[
                         \Pr\{p(e)\text{ lies in one part}\}
                            ={d-1\over n-1}.         \tag{5.5}
\]

Sum over the \(W\) cycle edges. \(\square\)

For \(J\) independent partition frames \(\Pi_1,\ldots,\Pi_J\),

\[
 \mathbb E\sum_{j=1}^J I_{\Pi_j}(C)
   =JW{d-1\over n-1}.                               \tag{5.6}
\]

Even if every exposed edge could be assigned perfectly to a compatible
descending trade, \(\Omega(W)\) total capacity therefore requires
\(Jd/n=\Omega(1)\).  Markov's inequality also gives, for every fixed
\(\varepsilon>0\),

\[
 \Pr\left\{\sum_{j=1}^J I_{\Pi_j}(C)
                  \ge\varepsilon W\right\}
 \le {J(d-1)\over\varepsilon(n-1)}.                 \tag{5.7}
\]

Hence \(J=o(n/d)\) random frames fail with probability tending to one for
each fixed lower-complete Hamilton cycle.

### Corollary 5.3 (no fixed subcritical atlas works for every cycle)

Fix partitions \(\Pi_1,\ldots,\Pi_J\) of \([n]\) into \(d\)-sets, and let
\(C_0\) be any lower-complete Hamilton cycle.  There is a coordinate
permutation \(\sigma\in S_n\) such that

\[
 \sum_{j=1}^J I_{\Pi_j}(\sigma C_0)
       \le JW{d-1\over n-1}.                        \tag{5.8}
\]

In particular, if \(Jd/n=o(1)\), no trade atlas all of whose carriers are
confined to these partition blocks can have \(\Omega(W)\) physical descent
capacity for every lower-complete Hamilton cycle.

#### Proof

Choose \(\sigma\) uniformly from \(S_n\).  For each fixed \(j\) and each
edge of \(C_0\), the image of its exchanged coordinate pair is a uniformly
random pair, and therefore lies in one part of \(\Pi_j\) with probability
\((d-1)/(n-1)\).  Hence the expectation of the left side of (5.8) is its
right side, so at least one \(\sigma\) attains at most the expectation.
Coordinate relabelling preserves Hamiltonicity and complete lower support.
Finally apply the descent-capacity bound (5.3) in every block. \(\square\)

### Corollary 5.4 (arbitrary overlapping block atlas)

Let \(\mathscr D\) be any fixed multiset of \(d\)-subsets of \([n]\).  For
every lower-complete Hamilton cycle \(C_0\), some coordinate permutation
\(\sigma\) satisfies

\[
 \boxed{
 \sum_{D\in\mathscr D} I_D(\sigma C_0)
 \le W|\mathscr D|{\binom d2\over\binom n2}.}
 \tag{5.9}
\]

Consequently, an atlas whose every carrier is contained in one member of
\(\mathscr D\) cannot have \(\Omega(W)\) owner-disjoint physical descent
capacity for every lower-complete Hamilton cycle when

\[
                         |\mathscr D|d^2/n^2=o(1).   \tag{5.10}
\]

#### Proof

Let

\[
 \lambda(\{a,b\})=|\{D\in\mathscr D:\{a,b\}\subset D\}|.
 \tag{5.11}
\]

Then

\[
 \sum_{D\in\mathscr D}I_D(C)
       =\sum_{e\in E(C)}\lambda(p(e)).               \tag{5.12}
\]

Under a uniformly random coordinate permutation, each \(p(e)\) is a
uniformly random pair.  The mean of \(\lambda\) over pairs is

\[
 {1\over\binom n2}\sum_{\{a,b\}}\lambda(\{a,b\})
       =|\mathscr D|{\binom d2\over\binom n2}.       \tag{5.13}
\]

Taking expectations in (5.12) and choosing a permutation attaining at most
the mean proves (5.9).  Any selected trade may be charged to a block which
carries it; (5.3) then bounds its improvement by the charged exposed
negative-edge mass. \(\square\)

The order in (0.6) is sharp only at the pair-exposure level.  A resolvable
pair design, when available, uses \((n-1)/(d-1)\) parallel classes and puts
every coordinate pair in exactly one block.  It then gives

\[
                         \sum_jI_{\Pi_j}(C)=W        \tag{5.14}
\]

for every Hamilton cycle.  But (5.14) does not say that the other deleted
edges of any lower-neutral factor occur, and says nothing about whether its
positive targets are holes.  It is therefore an exact sharpness statement
for the occurrence census, not a trade construction.

## 6. The three scale regimes

The two obstructions combine as follows.

### (i) \(d=o(\sqrt m)\)

These common-core carriers cannot cross all load profiles permitted by the
known scalar and point constraints, by (3.3) and Section 4.  A theorem
claiming statewise descent for every lower-complete cycle would first need a
new chronological result excluding such separated profiles.

### (ii) \(d=\Theta(\sqrt m)\), or more generally \(d=o(m)\)

The diameter may reach the Gaussian defect scale, but a bounded number of
partition frames has only

\[
                         O(Wd/m)=o(W)                \tag{6.1}
\]

exposed negative-edge mass.  At scale \(\sqrt m\), at least
\(\Omega(\sqrt m)\) moving frames are necessary before complete-factor
occurrence is even a meaningful question.

### (iii) \(d=\Theta(m)\)

A bounded number of frames can expose \(\Theta(W)\) cycle-edge mass.  This
is the first frame-oblivious scale not excluded by the census.  It still
does not provide a lower-neutral replacement factor or align the factor
with the upper defect.

Thus there is no free intermediate scale: \(\sqrt m\) coordinates are
needed for possible reach, while linear coordinates or linearly many total
frame incidences are needed for frame-oblivious physical supply.

## 7. Exact remaining gate

For each proposed carrier \(a\), let \(F_a^-\subset E(C)\) be its complete
negative factor and let \(\delta_a=B_+z_a\).  The carrier is usable only if

\[
 F_a^-\subset E(C),
 \tag{7.1}
\]

the replacement is a Hamilton cycle, and its exact score from (2.1) is
negative.  A positive theorem must find a compatible subfamily with

\[
 \sum_a
 \left[
  |\{U:u_C(U)=0,\ \delta_a^+(U)>0\}|
  +\sum_U\min\{\delta_a^-(U),(u_C(U)-1)_+\}
  -\|\delta_a^+\|_1
 \right]
 =\Omega(W),                                        \tag{7.2}
\]

with the scores interpreted sequentially or on target-disjoint supports.
Neither a span theorem for the vectors \(\delta_a\), nor the pair-exposure
identity (5.14), implies (7.1) or (7.2).

The six-coordinate pentagon fails because both its reach and its fixed-frame
occurrence are too small.  Merely enlarging it to a \(\sqrt m\)-coordinate
common-core gadget fixes only the first defect.  The exact unresolved escape
is a multi-frame complete-factor theorem using \(\Omega(\sqrt m)\) correlated
frames, or a linear-scale lower-neutral factor with a direct configuration-
Hall proof.  Absent such a theorem, the two-sided rainbow pseudofactor and
its endpoint-compatible Hamiltonization gate remain the only construction
in this lane already carrying \(W-o(W)\) genuine lower and upper colours.
