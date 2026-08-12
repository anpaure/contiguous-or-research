# Exploration F: structural forms for equal compact boxes

Date: 2026-07-25

## 0. Outcome

Write

\[
Q_t^{(d)}=[0,t]^d,
\qquad
g_d(t)=g_d(t,\ldots,t).
\]

This attack does not prove either

\[
g_3(t)=w_3(t)+o(t^2)
\quad\text{or}\quad
g_4(t)=w_4(t)+o(t^3).
\]

It does extract a rigorous small-to-large structure.

1. **Exact Boolean normal forms.**

   \[
   g_3(1)=4,\qquad g_4(1)=7.
   \]

   Every optimum consists, at the rank-two level, of one contiguous
   singleton Euler spine and complementary literal pair chords.  For four
   coordinates the spine graph is exactly one of

   \[
   K_4-e,\qquad C_4,\qquad
   \text{triangle plus pendant edge},\qquad P_4.
   \]

2. **Exact translated-cell characterization.**  A word for
   \(Q_t^{(d)}\) is universal if and only if every translated unit cell has
   a segmented Boolean trace which is universal for the nonzero Boolean
   \(d\)-cube.  Thus the Euler-spine/chord forms occur literally in every
   tight local cell, not only at \(t=1\).

3. **Height-slab contraction and superadditivity.**  Every consecutive
   block of \(q\) height levels in an equal-box word projects to a universal
   word for \(Q_q^{(d)}\).  Therefore

   \[
   g_d(q_1+\cdots+q_s)\ge\sum_{j=1}^s g_d(q_j).
   \]

4. **A human exact side-two theorem.**

   \[
   \boxed{g_3(2)=10.}
   \]

   Section 4 gives a finite combinatorial impossibility proof for length
   nine, independent of the previously available DRAT certificate.
   Consequently

   \[
   g_3(t)\ge
   10\left\lfloor\frac t2\right\rfloor
   +4(t\bmod2).
   \]

5. **Exact endpoint-track normal form.**  Every near-width family of
   selected middle witnesses decomposes into monotone unit-delay tracks.
   Rank-capped starts then give the following endpoint dual.  If a
   universal word of length \(N\) admits a selected middle-witness system
   in which every displacement is at most \(\rho t\), then, in the
   respective dimension,

   \[
   \begin{aligned}
   N-w_3(t)
   &\ge
   \left(\frac13-\frac{\rho}{2}-o(1)\right)t^2
   &&(\rho<2/3),\\
   N-w_4(t)
   &\ge
   \left(\frac14-\frac{\rho}{3}-o(1)\right)t^3
   &&(\rho<3/4).
   \end{aligned}
   \]

   Hence the small Euler trails cannot be repeated at bounded depth:
   a near-width word needs average middle-witness displacement at least
   \((2/3-o(1))t\) in dimension three and
   \((3/4-o(1))t\) in dimension four.

6. **Precise inductive gates.**

   - The three-box gate is a separator-safe two-shell splice

     \[
     g_3(t+2)\le g_3(t)+3t+6+O(1).
     \]

     It would imply \(g_3(t)=w_3(t)+O(t)\).

   - The four-box gate is the cycle-chord shell braid

     \[
     \sigma_t=2t^2+2t+1+o(t^2),
     \]

     where \(\sigma_t\) is the minimum word length for the exact
     complementary shell in Section 7.  It would imply
     \(g_4(t)=w_4(t)+o(t^3)\).

Both gates are explicitly marked **UNPROVED**.  The small cases support
their local chronology, while the endpoint-track theorem specifies the
linear-depth overlap which any scalable realization must add.

No web search or new finite/computational search is used.

---

## 1. Exact segmented unit-cell traces

Let

\[
A=(A_1,\ldots,A_N),\qquad A_j\in Q_t^{(d)}\setminus\{0\}.
\]

Fix a cell top

\[
q=(q_1,\ldots,q_d)\in[1,t]^d.
\]

Call a position \(q\)-clean if \(A_j\le q\).  Split the \(q\)-clean
positions into their maximal physical runs.  Inside one such run, delete
every letter at most

\[
q-\mathbf1=(q_1-1,\ldots,q_d-1).
\]

For every retained letter record its nonempty facet support

\[
\sigma_q(A_j)=\{i:(A_j)_i=q_i\}\subseteq[d].
\]

The resulting family of Boolean words, one per \(q\)-clean run, is the
**segmented \(q\)-trace**.

### Theorem 1.1 (unit-cell trace equivalence)

The word \(A\) is universal for \(Q_t^{(d)}\) if and only if, for every
\(q\in[1,t]^d\), the segmented \(q\)-trace represents every nonempty
subset of \([d]\) by a contiguous union lying inside one segment.

#### Proof

For \(S\ne\varnothing\), define the upper corner of the translated Boolean
cell

\[
x(q,S)_i=
\begin{cases}
q_i,&i\in S,\\
q_i-1,&i\notin S.
\end{cases}
\tag{1.1}
\]

Suppose first that \(A\) is universal and choose a witness for \(x(q,S)\).
Every letter in it is at most \(x(q,S)\le q\), so the witness lies in one
\(q\)-clean run.  Delete its letters at most \(q-\mathbf1\).  A retained
letter can touch only facets in \(S\), and every facet in \(S\) is touched
somewhere because the interval maximum is \(x(q,S)\).  The retained
positions remain contiguous in that trace segment and their Boolean union
is exactly \(S\).

Conversely, let \(x\in Q_t^{(d)}\setminus\{0\}\).  Put

\[
q_i=\max(1,x_i),
\qquad
S=\{i:x_i>0\}.
\]

Then \(x=x(q,S)\).  Select a Boolean witness for \(S\) in one \(q\)-trace
segment and take the original physical interval between its first and last
retained positions.  Every intervening position is \(q\)-clean.  A retained
facet letter touches only coordinates in \(S\), while every deleted
interior letter is at most \(q-\mathbf1\).  Hence every intervening letter
is at most \(x\), and the trace witness supplies value \(x_i=q_i\) in every
coordinate \(i\in S\).  The physical interval maximum is exactly \(x\).
\(\square\)

### Corollary 1.2 (cell trace lower bound)

Let

\[
F(q)=\#\{j:A_j\le q\}.
\]

Then

\[
\boxed{
F(q)-F(q-\mathbf1)\ge \nu(d),}
\tag{1.2}
\]

where \(\nu(d)=g_d(1)\) is the nonzero Boolean optimum.

#### Proof

The left side is the total number of letters retained across all segments
of the \(q\)-trace.  Concatenate those Boolean segments.  All selected
witnesses internal to the segments survive, so the concatenation is a
universal Boolean word and has length at least \(\nu(d)\). \(\square\)

For \(q=(h,\ldots,h)\), (1.2) says that the height-\(h\) subsequence,
projected to the coordinates attaining height \(h\), is a universal
Boolean word.  The stronger block version is proved in Section 3.

---

## 2. Boolean optima are Euler spines plus chords

Write \(i\) for the singleton \(\{i\}\) and \(ij\) for
\(\{i,j\}\).

### Lemma 2.1 (pair-transition count)

In a Boolean word, let

- \(a\) be the number of singleton-letter positions;
- \(b\) the number of pair-letter positions;
- \(c\) the number of positions of size at least three; and
- \(r\) the number of maximal physical runs consisting of singleton
  letters.

Then the number of represented pair types is at most

\[
b+(a-r)=N-c-r.
\tag{2.1}
\]

#### Proof

A pair target which does not occur as a pair letter has a witness containing
only singleton letters of its two vertices.  Somewhere in that witness the
two singleton types occur at consecutive physical positions.  Such a
transition lies inside a singleton run.  There are at most \(a-r\) singleton
transitions, and each transition has one pair type.  Add the at most \(b\)
literal pair types. \(\square\)

### Theorem 2.2 (all optimal Boolean three-words)

\[
\boxed{\nu(3)=4.}
\]

Every length-four optimum has one singleton run whose transition edges and
literal pair chords partition \(E(K_3)\).  Up to relabelling and reversal,
the two forms are

\[
1,2,3,1
\tag{2.2}
\]

and

\[
13,1,2,3.
\tag{2.3}
\]

#### Proof

The three singleton targets force \(a\ge3\).  Applying (2.1) to the three
pair targets in a four-letter word gives

\[
3\le4-c-r.
\]

Thus \(c=0,r=1\), and equality holds throughout (2.1).  The singleton
transitions are distinct edges and the literal pair letters are distinct
complementary chords.

If \(b=0\), the singleton run is an Euler circuit of \(K_3\), giving
(2.2).  If \(b=1\), its transition graph is \(K_3\) minus one edge, hence a
three-vertex path, giving (2.3).  Both displayed words visibly cover all
seven nonempty subsets.  Three positions have only six nonempty intervals,
so four is optimal. \(\square\)

### Theorem 2.3 (all optimal Boolean four-word skeletons)

\[
\boxed{\nu(4)=7.}
\]

In every length-seven optimum:

1. no letter has size at least three;
2. all singleton letters form one physical run;
3. the distinct transitions of that singleton run form an Euler trail in a
   connected spanning simple graph \(H\);
4. the literal pair letters are exactly \(E(K_4)\setminus E(H)\).

If \(b\) is the number of literal pair chords, then \(1\le b\le3\), and

\[
\begin{array}{c|c}
b&H\\ \hline
1&K_4-e,\\
2&C_4\ \text{or a triangle with one pendant edge},\\
3&P_4.
\end{array}
\tag{2.4}
\]

Every graph type in (2.4) is realized by a universal word.

#### Proof

Four singleton targets force \(a\ge4\).  If \(N=7\), the six pair targets
and (2.1) give

\[
6\le7-c-r.
\]

Therefore \(c=0,r=1\), with equality in the pair count.  This proves
items 1--4.  The case \(b=0\) would require an Euler trail using every edge
of \(K_4\), impossible because \(K_4\) has four odd-degree vertices.
Also \(a\ge4\) gives \(b\le3\).

For \(b=1\), \(H=K_4-e\).  For \(b=2\), \(H\) is a connected spanning
unicyclic graph with at most two odd vertices, hence \(C_4\) or a triangle
with one pendant edge.  For \(b=3\), \(H\) is a spanning tree with at most
two odd vertices, hence \(P_4\).

The following templates, with distinct displayed vertices, realize all
four cases:

\[
\begin{array}{c|l}
K_4-uv&w,z,u,w,v,z,uv,\\
C_4&ac,a,b,c,d,a,bd,\\
\triangle abc\text{ plus }da&db,dc,d,a,b,c,a,\\
P_4:a-b-c-d&ad,bd,a,b,c,d,ac.
\end{array}
\tag{2.5}
\]

Their adjacent singleton transitions and literal chords cover all six
pairs.  The consecutive three-singleton windows, together with the chord
seams, cover all four triples, and a longer displayed interval covers
\([4]\).

It remains only to exclude length six.  By (2.1), a six-letter word
represents at most

\[
6-c-r\le5
\]

pair types, fewer than the required six. \(\square\)

### Example 2.4 (canonical four-word with every witness visible)

Take

\[
\boxed{13,1,2,3,4,1,24.}
\tag{2.6}
\]

The pairs are

\[
13,\ 12,\ 23,\ 34,\ 14,\ 24.
\]

The triples have witnesses

\[
123:[2,4],\quad
234:[3,5],\quad
134:[4,6],\quad
124:[6,7],
\]

and \(1234=[2,5]\).  This supplies a literal optimal seed for the
four-box shell recurrence in Section 7.

By Theorem 1.1, whenever a translated unit-cell trace has the minimum
length four or seven, its concatenated trace has exactly the corresponding
Euler-spine/chord skeleton.  A segment boundary cannot cut one of the
selected spine transitions; chord caps may lie in separate clean segments.

---

## 3. Height-slab contraction

For \(A\in Q_t^{(d)}\), put

\[
\operatorname{ht}(A)=\max_i A_i.
\]

### Theorem 3.1 (height-slab projection)

Fix

\[
0\le a<a+q\le t.
\]

From a universal word for \(Q_t^{(d)}\), retain exactly the letters
satisfying

\[
a<\operatorname{ht}(A_j)\le a+q
\]

and replace each by

\[
\pi_a(A_j)=((A_{j,1}-a)_+,\ldots,(A_{j,d}-a)_+).
\tag{3.1}
\]

The resulting nonzero word is universal for \(Q_q^{(d)}\).

#### Proof

Let \(u\in Q_q^{(d)}\setminus\{0\}\) and choose a witness in the original
word for

\[
T=a\mathbf1+u.
\]

Every letter in that witness is at most \(T\), hence has height at most
\(a+q\).  Delete its letters of height at most \(a\).  The retained
positions form a nonempty contiguous factor of the global slab
subsequence.  If \(u_i=0\), every projected \(i\)-coordinate is zero.  If
\(u_i>0\), some original letter attains \(T_i=a+u_i>a\), is retained, and
projects to \(u_i\).  Thus the projected maximum is exactly \(u\).
\(\square\)

### Corollary 3.2 (superadditivity)

For every composition \(t=q_1+\cdots+q_s\),

\[
\boxed{
g_d(t)\ge\sum_{j=1}^s g_d(q_j).}
\tag{3.2}
\]

In particular,

\[
\boxed{
g_3(t)\ge
10\left\lfloor\frac t2\right\rfloor
+4(t\bmod2),}
\tag{3.3}
\]

using Theorems 2.2 and 4.1 below, while

\[
g_4(t)\ge7t.
\tag{3.4}
\]

These numerical bounds are eventually weaker than width.  Their real
content is structural: every two-level height slab in every equal
three-box word contains a projected universal side-two word.

---

## 4. A human proof that \(g_3(2)=10\)

### Theorem 4.1

\[
\boxed{g_3(2,2,2)=10.}
\tag{4.1}
\]

#### Upper bound

The word

\[
\begin{aligned}
&(0,1,0),(0,2,0),(0,1,1),(0,0,2),(1,0,0),\\
&(0,0,1),(2,0,0),(1,1,0),(1,2,0),(1,1,1)
\end{aligned}
\tag{4.2}
\]

has the following witnesses:

\[
\begin{array}{c|c@{\qquad}c|c}
100&[5,5]&200&[7,7]\\
010&[1,1]&110&[8,8]\\
210&[7,8]&020&[2,2]\\
120&[9,9]&220&[7,9]\\
001&[6,6]&101&[5,6]\\
201&[6,7]&011&[3,3]\\
111&[10,10]&211&[6,8]\\
021&[2,3]&121&[9,10]\\
221&[6,9]&002&[4,4]\\
102&[4,5]&202&[4,7]\\
012&[3,4]&112&[3,5]\\
212&[3,7]&022&[2,4]\\
122&[2,5]&222&[2,7].
\end{array}
\tag{4.3}
\]

Thus \(g_3(2)\le10\).

#### Lower bound: shell reduction

For a letter of height \(h\in\{1,2\}\), record the nonempty set of
coordinates at which it equals \(h\).  The height-\(h\) subsequence is a
universal Boolean three-word by Theorem 3.1 with \(q=1\), and therefore has
at least four positions.  A hypothetical nine-letter word has shell sizes

\[
(|W_1|,|W_2|)=(5,4)\quad\text{or}\quad(4,5).
\tag{4.4}
\]

Every length-four Boolean three-word has one of the two forms in Theorem
2.2.  We use

\[
H_x=(2,0,0),\quad H_y=(0,2,0),\quad H_z=(0,0,2)
\]

and

\[
O_{ij}=
\text{the target with coordinate }i\text{ equal to }2,
\ j\text{ equal to }1,\text{ and the third equal to }0.
\tag{4.5}
\]

There are six directed outer targets \(O_{ij}\).

We need one elementary boundary observation.  At one oriented boundary of
a maximal lower run, at most one indirect outer target can enter.  If two
candidate targets have different high coordinates, the farther pure-high
provider crosses the nearer incompatible height-two letter.  If they are
\(O_{ij}\) and \(O_{ik}\) with the same high coordinate—even if they use
different duplicate occurrences of \(H_i\)—both intervals contain the
boundary prefix or suffix through their first required \(j\)- and
\(k\)-positive pins.  Whichever pin is nearer lies in the interval reaching
the farther and supplies its forbidden coordinate; coincident pins
contaminate both.  This also proves the one-sided branch statement used
below.

#### Case A: four top letters and five lower letters

If the top trace has path-chord type, its order is

\[
Q_{xy},H_x,H_z,H_y.
\]

The bare target \((2,2,0)\) forces \(Q_{xy}=(2,2,0)\).  The bare targets
\((2,0,2)\) and \((0,2,2)\) force every lower letter in the gaps
\(H_x\!-\!H_z\) and \(H_z\!-\!H_y\) to omit \(y\) and \(x\), respectively.
Now \(O_{xy}\) cannot use the \(H_x\!-\!H_z\) gap, whose letters omit
\(y\), and therefore forces the \(Q_{xy}\!-\!H_x\) gap nonempty.
\(O_{xz}\) cannot share that same oriented boundary with \(O_{xy}\), so
the \(H_x\!-\!H_z\) gap is nonempty.  At \(H_z\), \(O_{zx}\) cannot use
the \(H_z\!-\!H_y\) gap, whose letters omit \(x\), and \(O_{zy}\) cannot
share the other oriented boundary with \(O_{zx}\); hence the
\(H_z\!-\!H_y\) gap is nonempty.  Finally \(O_{yx}\) cannot use that
\(x\)-free gap and forces an external run after \(H_y\).  Thus all four
gaps

\[
Q_{xy}\!-\!H_x,\quad
H_x\!-\!H_z,\quad
H_z\!-\!H_y,\quad
\text{after }H_y.
\tag{4.6}
\]

are nonempty.

If the top trace has cycle type, write it

\[
U_x,H_y,H_z,V_x.
\]

The three bare top pairs force the three internal lower gaps to omit,
respectively, \(z,x,y\).  The two outer targets of \(H_y\) cannot use the
same side; the coordinate omissions force one into each of the first two
gaps.  Likewise the outer targets of \(H_z\) force use of the second and
third gaps.  None of these gaps can represent \(111\), so an external
lower run is also nonempty.

In either top type, five lower letters occupy at least four nonempty runs.
The total number of physical intervals contained in them is at most

\[
\binom{2+1}{2}+1+1+1=6,
\]

whereas the seven nonzero points of \(Q_1^{(3)}\) require seven distinct
lower intervals.  Contradiction.

#### Case B: four lower letters and five top letters

If the lower trace has cycle type \(x,y,z,x\), its three pair targets force
all four letters to form one physical lower block.  Let \(p_i\) count pure
occurrences \(H_i\), and let \(d\) count outer targets occurring directly
as top letters.  Every indirect \(O_{ij}\) must connect a pure \(H_i\) to
the one-sided lower block, and one pure occurrence serves at most one such
target.  Therefore at most

\[
d+p_x+p_y+p_z\le5
\]

of the six outer targets can be covered.

If the lower trace has path-chord type, it consists of a literal

\[
R=xy
\]

and a physically contiguous singleton run

\[
S=x,z,y.
\]

These one or two lower runs have at most four boundaries, each serving at
most one indirect outer target.  Hence at least two outer targets occur
directly.  The five top positions are therefore exactly

\[
H_x,H_y,H_z
\quad\text{and two direct outer letters},
\]

and all four lower-run boundaries are saturated.

The literal \(R\) and run \(S\) must be separated.  One pure high provider
must serve the two facing central boundaries.  It cannot instead serve two
boundaries with both lower runs on the same side: reaching the farther run
crosses the nearer \(xy\) letter and supplies a forbidden coordinate.
The exact central capability table is

\[
\begin{array}{c|ccc}
&H_x&H_y&H_z\\ \hline
R=xy&O_{xy}&O_{yx}&-\\
\text{left of }S=x,z,y&O_{xz}&O_{yx}&O_{zx}\\
\text{right of }S=y,z,x&O_{xy}&O_{yz}&O_{zy}.
\end{array}
\tag{4.7}
\]

Only \(H_x\) serves two distinct targets at the facing central boundaries,
namely \(O_{xy}\) and \(O_{xz}\).  The left external boundary is then
served by \(H_y\), giving \(O_{yx}\), and the right by \(H_z\), giving
\(O_{zy}\).  The two direct top letters must be

\[
O_{yz},\qquad O_{zx}.
\]

Neither may lie between a pure portal and its assigned lower boundary,
because it has a forbidden top or lower coordinate there.  Thus both direct
letters lie either beyond the left \(H_y\) or beyond the right \(H_z\).

The bare target \((2,0,2)\) is now impossible.  Its only \(x=2\) provider
is the central \(H_x\).  Every \(z=2\) provider is either \(H_z\) or the
direct \(O_{zx}\).  A provider on the right is separated from \(H_x\) by
the \(y\)-letter in \(S\); a provider on the left is separated from \(H_x\)
by \(H_y\) (and by the \(xy\) side).  Every candidate interval therefore
contains a forbidden positive \(y\)-coordinate.  This final contradiction
proves \(g_3(2)\ge10\). \(\square\)

### Structural reading of the optimum

In (4.2), the height-two top-support word is the Boolean cycle

\[
y,z,x,y.
\]

The selected middle-rank profile may be chosen as two disjoint adjacent
tracks of length three plus one cap:

\[
\begin{aligned}
021&:[2,3],&012&:[3,4],&102&:[4,5],\\
201&:[6,7],&210&:[7,8],&120&:[8,9],\\
111&:[10,10].
\end{aligned}
\tag{4.8}
\]

This is genuine small-case structure, but Section 5 proves that bounded
adjacent tracks cannot scale.

---

## 5. Endpoint tracks and the short-span dual

Let \(P\) be a graded box, let \(H\) be a rank-\(h\) antichain of size
\(M\), and suppose a word of length

\[
N=M+D
\]

represents every target.  Choose one interval for each member of \(H\) and
sort these intervals by left endpoint.

### Theorem 5.1 (unit-delay track normal form)

The selected intervals have the exact form

\[
I_i=[i+\alpha_i,i+\beta_i],
\qquad
0\le\alpha_i\le\beta_i\le D,
\tag{5.1}
\]

where both \((\alpha_i)\) and \((\beta_i)\) are nondecreasing.

For \(1\le k\le D\), put

\[
S_k=\{i:\alpha_i<k\le\beta_i\}.
\tag{5.2}
\]

Then:

1. every \(S_k\) is an interval of indices;
2. the left and right endpoints of the nonempty \(S_k\)'s are
   nondecreasing in \(k\);
3.

   \[
   r_i-\ell_i=\#\{k:i\in S_k\};
   \tag{5.3}
   \]

4.

   \[
   \sum_i(r_i-\ell_i)=\sum_{k=1}^D|S_k|.
   \tag{5.4}
   \]

If every displacement is at most one, the nonempty tracks are disjoint and,
for \(S_k=[p,q]\),

\[
I_i=[i+k-1,i+k]\qquad(p\le i\le q).
\tag{5.5}
\]

Thus \(S_k\) is literally one adjacent-join trail and every remaining
selected target is a literal cap.

#### Proof

Equal-rank target intervals cannot contain one another.  Their left
endpoints are distinct, their right endpoints are distinct, and sorting the
left endpoints sorts the right endpoints.  Each endpoint sequence is an
\(M\)-subset of \([M+D]\), giving (5.1).

For fixed \(k\), the inequality \(\alpha_i<k\) defines a prefix and
\(\beta_i\ge k\) defines a suffix.  Their intersection is an interval.
As \(k\) increases, both boundary indices move only to the right.  Equations
(5.3)--(5.4) are the layer-cake identity for
\(\beta_i-\alpha_i\).  If this difference is at most one and \(i\in S_k\),
then \((\alpha_i,\beta_i)=(k-1,k)\), proving (5.5). \(\square\)

### Lemma 5.2 (literal pin sign in track form)

Let \([u,v]\) be an internal positive run in the middle-target incidence
word of any coordinate-threshold atom.  Then

\[
\boxed{
\#\{k:S_k\supseteq[u-1,v+1]\}
=(\beta_{u-1}-\alpha_{v+1})_+
\le v-u.}
\tag{5.6}
\]

No one-common-pin assumption is used.

#### Proof

A track contains \([u-1,v+1]\) exactly when

\[
\alpha_{v+1}<k\le\beta_{u-1},
\]

which proves the equality.

Choose a literal occurrence of the atom pinning target \(u\).  It lies in
\(I_u\).  It cannot lie in \(I_{u-1}\), whose target omits the atom; because
left endpoints increase, the pin must therefore be strictly after
\(r_{u-1}\).  Symmetrically it is strictly before \(\ell_{v+1}\).  Hence

\[
r_{u-1}+2\le\ell_{v+1}.
\]

Substitute

\[
r_{u-1}=u-1+\beta_{u-1},
\qquad
\ell_{v+1}=v+1+\alpha_{v+1}
\]

to obtain (5.6). \(\square\)

### Theorem 5.3 (rank-capped-start dual)

Let \(L_{<h}\) be the number of nonzero targets below rank \(h\), and put

\[
d_i=r_i-\ell_i.
\]

Then

\[
\boxed{
L_{<h}\le\sum_{i=1}^M d_i+(h-1)D
=\sum_{k=1}^D|S_k|+(h-1)D.}
\tag{5.7}
\]

Consequently, if \(h\ge2\) and every \(d_i\le q\),

\[
\boxed{
D\ge
\left\lceil
\frac{L_{<h}-qM}{h-1}
\right\rceil_+.}
\tag{5.8}
\]

Here \(\lceil x\rceil_+=\max\{0,\lceil x\rceil\}\).

#### Proof

Group arbitrary selected witnesses of the lower targets by their left
endpoint.  At a selected middle start \(\ell_i\), a lower witness must end
before \(r_i\), and therefore supplies at most \(d_i\) distinct lower
targets.  There are \(D\) unused starts.  At one fixed start, interval
maxima form a chain and contain at most one nonzero target in each rank
\(1,\ldots,h-1\).  This proves (5.7); (5.8) follows from
\(\sum_i d_i\le qM\). \(\square\)

### Corollary 5.4 (critical spans in equal boxes)

For the equal three-box,

\[
M=\left(\frac34+o(1)\right)t^2,\quad
L_{<h}=\left(\frac12+o(1)\right)t^3,\quad
h=\left(\frac32+o(1)\right)t.
\]

For the equal four-box,

\[
M=\left(\frac23+o(1)\right)t^3,\quad
L_{<h}=\left(\frac12+o(1)\right)t^4,\quad
h=2t.
\]

Substitution in (5.8) proves the two lower bounds stated in Section 0.
Moreover, if \(D=o(M)\), (5.7) gives

\[
\frac1M\sum_i d_i
\ge
\begin{cases}
(2/3-o(1))t,&d=3,\\
(3/4-o(1))t,&d=4.
\end{cases}
\tag{5.9}
\]

Therefore no scalable near-width construction can keep the small-case
literal-cap/adjacent-trail form.  For a width-plus-\(O(t)\) three-box word,
the \(O(t)\) unit tracks must have average area \(\Theta(t^2)\).  For a
width-plus-\(O(t^2)\) four-box word, the \(O(t^2)\) tracks must have average
area \(\Omega(t^2)\).

---

## 6. Three-box shell consequences

### Lemma 6.1 (inner-run deletion constraint)

In a word for \(Q_t^{(d)}\), the letters of height at most \(t-1\) are split
by height-\(t\) letters into maximal inner runs.  Those inner runs,
collectively and without witnesses crossing between them, cover every
target of \(Q_{t-1}^{(d)}\).

#### Proof

A witness whose maximum lies in \(Q_{t-1}^{(d)}\) contains no height-\(t\)
letter.  It is therefore wholly contained in one inner run. \(\square\)

Thus inserting a new shell arbitrarily into an optimal inner word is not a
valid induction: the retained inner runs themselves must form a segmented
factor cover.

### Theorem 6.2 (four-gap top-shell lemma)

Let \(t\ge2\).  If a universal word for \(Q_t^{(3)}\) has exactly four
height-\(t\) letters, then its lower-height letters occupy at least four
nonempty maximal runs.  If \(L\) is the number of lower-height letters,
then

\[
\boxed{
t^3-1\le\binom{L-2}{2}+3,}
\tag{6.1}
\]

and hence

\[
\boxed{
L\ge
\left\lceil
\frac{5+\sqrt{8t^3-31}}2
\right\rceil.}
\tag{6.2}
\]

#### Proof

The height-\(t\) facet-support word is an optimal Boolean three-word and
has one of the two forms in Theorem 2.2.  Repeat Case A of Theorem 4.1 with

\[
H_i=(t,0,0),\quad
B_{ij}=(t,t,0),\quad
O_{ij}=(t,1,0).
\]

The argument uses only the distinction between top value \(t\) and lower
values, not the special value \(t=2\).  Path-chord type forces four lower
runs by its two bare-pair corridors and directed outer targets.  Cycle type
forces three coordinate-omitting internal gaps and an external run for
\((1,1,1)\).

Every one of the \(t^3-1\) nonzero targets in \(Q_{t-1}^{(3)}\) needs an
interval inside one lower run.  With \(L\) letters split among at least four
nonempty runs, convexity maximizes the interval count at run lengths
\(L-3,1,1,1\), giving

\[
\binom{L-2}{2}+3.
\]

This proves (6.1)--(6.2). \(\square\)

At \(t=2\), (6.2) gives \(L\ge6\), exactly the four-top-letter branch of
Theorem 4.1.

### Conjecture 6.3 (separator-safe two-shell splice — UNPROVED)

There is an absolute constant \(C\) such that

\[
\boxed{
g_3(t+2)\le g_3(t)+3t+6+C.}
\tag{TSS}
\]

The intended construction is stronger than the numerical inequality: the
height-\(\le t\) letters must retain a segmented universal factor cover as
in Lemma 6.1, while the top two levels contain the side-two spine/gap
structure of (4.2).

The exact width identity is

\[
w_3(t+2)-w_3(t)=3t+6.
\tag{6.3}
\]

Thus (TSS) implies

\[
g_3(t)=w_3(t)+O(t)
\]

by induction separately on the two parities.

Theorem 3.1 makes the side-two seed compulsory in every two-height slab,
but it does not prove the separator-safe splice.  Theorem 5.3 further says
that the splice must create linearly deep, heavily overlapping tracks; a
bounded-span repetition of (4.8) is impossible.

---

## 7. Exact four-box shell recurrence

Put

\[
R_t=[0,t]^2
\]

and split it into the outer hook

\[
L_t=
\{(0,j):0\le j\le t\}
\cup
\{(i,t):1\le i\le t\}
\tag{7.1}
\]

and the translated interior

\[
I_t=\{1,\ldots,t\}\times\{0,\ldots,t-1\}
=(1,0)+R_{t-1}.
\tag{7.2}
\]

The set \(L_t\) is the saturated chain

\[
(0,0)<(0,1)<\cdots<(0,t)<(1,t)<\cdots<(t,t).
\]

Pair the four coordinates as \(R_t\times R_t\), and define the
complementary shell

\[
\mathcal S_t=
(L_t\times R_t)
\mathbin{\dot\cup}
(I_t\times L_t).
\tag{7.3}
\]

Its complement is

\[
I_t\times I_t
=\delta+Q_{t-1}^{(4)},
\qquad
\delta=(1,0,1,0).
\tag{7.4}
\]

### Theorem 7.1 (exact shell width)

\[
\boxed{
w(\mathcal S_t)=
(t+1)^2+t^2
=2t^2+2t+1
=w_4(t)-w_4(t-1).}
\tag{7.5}
\]

#### Proof

Let

\[
P_s(z)=1+z+\cdots+z^s.
\]

The outer-hook identity is

\[
P_t(z)^2=P_{2t}(z)+zP_{t-1}(z)^2.
\tag{7.6}
\]

Therefore the shell rank polynomial is

\[
\begin{aligned}
P_{\mathcal S_t}(z)
&=P_{2t}(z)\bigl(P_t(z)^2+zP_{t-1}(z)^2\bigr)\\
&=P_t(z)^4-z^2P_{t-1}(z)^4.
\end{aligned}
\tag{7.7}
\]

The first piece of (7.3) is abstractly
\([0,t]^2\times[0,2t]\), of width \((t+1)^2\).  The second, including its
rank-one translation, is abstractly
\([0,t-1]^2\times[0,2t]\), of width \(t^2\).  Their standard product-hook
SCDs are both centered at ambient rank \(2t\).  Together they form an SCD
of the disjoint shell, so widths add and give (7.5). \(\square\)

Let \(\sigma_t\) be the minimum length of an ambient literal word covering
every nonzero target of \(\mathcal S_t\).

### Theorem 7.2 (shell recurrence)

\[
\boxed{
g_4(t)\le g_4(t-1)+1+\sigma_t.}
\tag{7.8}
\]

#### Proof

Translate a universal word for \(Q_{t-1}^{(4)}\) by \(\delta\).  It covers
every point of \(I_t\times I_t\) except the translated local origin
\(\delta\), which is added once.  Concatenate this block with a shell word.
Every selected witness stays inside its target block, and (7.3)--(7.4)
partition the full box. \(\square\)

### Boolean seed

For \(t=1\), the inner target is \(\delta=13\), and

\[
1,2,3,4,1,24
\tag{7.9}
\]

covers the remaining shell.  Five positions are impossible: the shell
contains four singleton targets and five pair targets, while Lemma 2.1
bounds the number of pair types in five positions by four.  Hence

\[
\boxed{
\sigma_1=6=w(\mathcal S_1)+1.}
\tag{7.10}
\]

Prefixing \(13\) recovers the optimal word (2.6).

### Conjecture 7.3 (cycle-chord shell braid — UNPROVED)

\[
\boxed{
\sigma_t=2t^2+2t+1+o(t^2).}
\tag{CCSB}
\]

By (7.5), (7.8), and telescoping,

\[
\mathrm{CCSB}
\quad\Longrightarrow\quad
g_4(t)=w_4(t)+o(t^3).
\tag{7.11}
\]

The stronger error \(\sigma_t-w(\mathcal S_t)=O(t)\) would give
\(g_4(t)=w_4(t)+O(t^2)\).

The two pieces of (7.3) cannot simply be serviced separately at their own
leading widths.  Abstractly they have shapes

\[
(t,t,2t)
\quad\text{and}\quad
(t-1,t-1,2t).
\]

The audited boundary three-box lower bound gives a quadratic excess at
least \((1/24-o(1))t^2\) for the first.  The second contains the boundary
subbox \((t-1,t-1,2t-2)\) with the same width \(t^2\), and inherits the same
asymptotic toll.  Thus any architecture using separate component-restricted
words pays at least

\[
w(\mathcal S_t)+\left(\frac1{12}-o(1)\right)t^2.
\tag{7.12}
\]

This is not a lower bound on \(\sigma_t\): it proves that CCSB must
cross-fuse the complementary pieces, exactly as the Boolean optimum fuses
its singleton Euler spine with complementary chords.

---

## 8. Adversarial audit and exact frontier

### 8.1 What the small structures do prove

- The unit-cell theorem is an equivalence, not merely a necessary shadow
  condition.  Its sufficiency keeps every selected Boolean factor inside
  one \(q\)-clean physical run, so no deleted outside letter can
  contaminate the lifted box target.

- The Euler-spine/chord description follows from equality in the pair
  transition count.  It is a normal form for every Boolean optimum, not a
  claim of uniqueness of the all-singleton cycle.

- The side-two three-box lower proof was independently reconstructed for
  arbitrary literal letters, without the DRAT certificate.  Coordinate
  closure reduces arbitrary increment masks to triples without increasing
  length.  Its only delicate point is the boundary observation in Section
  4: it remains valid when two candidates use different duplicate
  pure-high occurrences, because their intervals share the same oriented
  lower-run prefix or suffix and the nearer required pin contaminates the
  farther witness.  With that formulation, both shell cases and the final
  \(202\) obstruction pass the audit.

- The shell recurrence (7.8) concatenates complete target packets.  It does
  not insert outer letters through selected inner witnesses.

### 8.2 The decisive negative audit

It is tempting to extrapolate the \(t=1\) Euler trails or the adjacent
tracks in (4.8) and conjecture that all middle targets can remain literal
or adjacent.  Theorem 5.3 rules this out quantitatively.

If a word of length \(N\) had every selected middle witness equal to a
literal cap or an adjacent pair, then \(q\le1=o(t)\).  Equations
(5.8)--(5.9) would force, in the respective dimension,

\[
N\ge w_3(t)+\left(\frac13-o(1)\right)t^2
\]

and

\[
N\ge w_4(t)+\left(\frac14-o(1)\right)t^3.
\]

Equivalently, an interval serving a lower target cannot contain a complete
middle cap or adjacent-pair witness.  More precisely, when \(q\le1\),
selected middle starts contribute capacity for at most \(M\) distinct
lower targets and the unused starts for at most \((h-1)D\).  Thus, when
\(D=o(M)\), the rank-capped lower-target capacity

\[
M+(h-1)D=o(t^d)
\]

is too small for the volume-order family of lower targets.  This is a
capacity statement, not a bound on the raw number of physical intervals.

Thus the scalable content of the small cases is the **track topology** and
the chord/facet pin placement, not their unit length.  A successful braid
must dilate those tracks to linear depth while keeping the exact pin
inequality (5.6).

### 8.3 Final status

The strongest unconditional new construction theorem is the exact
four-shell recurrence (7.8) with its optimal Boolean seed.  The strongest
unconditional new lower structure is the combination of:

\[
\text{segmented cell traces}
\;+\;
\text{height-slab contraction}
\;+\;
\text{monotone unit-delay tracks}
\;+\;
\text{critical-span dual}.
\]

The smallest positive replacement lemmas are TSS for three boxes and CCSB
for four boxes.  Neither is proved.  Any future endpoint dual must go beyond
short middle spans; any future construction must implement linearly deep
tracks and separator-safe nested shell service.
