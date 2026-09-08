# Independent Y-lane audit of the linear PBBS dominance seam

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Verdict

The dominance-staircase theorem in
MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md is valid.
For a cut in an arbitrary rank-\((m+1)\) Johnson walk and

\[
 2H\le m+1,
\tag{0.1}
\]

there is a nonzero literal seam word of exact constructed length

\[
 \boxed{4H-1}
\tag{0.2}
\]

which exposes

1. every floor-correct lower intersection of at most \(H+1\) consecutive
   owners crossing the cut; and
2. every upper union of at most \(H+1\) consecutive owners crossing the
   cut.

The lower chart has \(2H-1\) letters and the upper chart has \(2H\)
letters.  Endpoint-capped erosion plus these charts gives, on one active
cycle of length \(\ell\) cut at \(J\) edges,

\[
 \boxed{\ell+(5H-1)J.}
\tag{0.3}
\]

Consequently the full PBBS central-band word obeys

\[
 \boxed{
 L_H\le
 W+2H B_m+2(5H-1)\nu_H(P_m),\qquad
 B_m=\operatorname {Cat}_m={W\over2m+1}.}
\tag{0.4}
\]

Thus, for every fixed \(A\), the still-unproved hypothesis

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)=O_A(B_m)
\tag{0.5}
\]

now suffices for coefficient one after the already audited fixed-\(A\)
diagonalization and product-SCD tails.

This linear theorem strictly supersedes the valid \(O(H^{3/2})\) fallback
in MATH_ATTACK_Y14_PBBS_SUBQUADRATIC_CUT_SEAM_20260725.md.  The fallback
covers every lower crossing mask, including wrong-rank masks; the linear
chart needs only, and covers exactly, every floor-correct lower mask.
That is the correct scope for restoring selected PBBS support.

## 1. Exact dominance model

Open the owner cycle at

\[
 \ldots,X_{-2},X_{-1}\mid X_0,X_1,\ldots,
\qquad |X_i|=m+1,
\tag{1.1}
\]

with consecutive owners Johnson adjacent.  Put

\[
 C=X_{-1}\cap X_0,\qquad |C|=m.
\tag{1.2}
\]

For \(1\le s,t\le H\), define

\[
 P_{s,t}=\bigcap_{i=-s}^{t-1}X_i.
\tag{1.3}
\]

This window has \(s+t\) owners and \(s+t-1\) transitions, so

\[
 |P_{s,t}|\ge m+2-s-t.
\tag{1.4}
\]

Call it floor-correct when equality holds.

For each \(x\in C\), define the capped consecutive positive-run extents

\[
\begin{aligned}
 u_x&=\max\{u\in[H]:x\in X_{-u}\cap\cdots\cap X_{-1}\},\\
 v_x&=\max\{v\in[H]:x\in X_0\cap\cdots\cap X_{v-1}\}.
\end{aligned}
\tag{1.5}
\]

Write \(p_x=(u_x,v_x)\) and let

\[
 \mathcal D=\{p_x:x\in C\}\subseteq[H]^2
\tag{1.6}
\]

with multiplicities retained when recovering set coordinates.

### Lemma 1.1

For every \((s,t)\in[H]^2\),

\[
 \boxed{
 P_{s,t}=\{x\in C:u_x\ge s,\ v_x\ge t\}.}
\tag{1.7}
\]

#### Proof

The owner interval in (1.3) contains \(X_{-1}\) and \(X_0\), so its
intersection lies in \(C\).  A coordinate of \(C\) survives the whole
interval exactly when its positive run through the cut extends at least
\(s\) owners to the left and \(t\) owners to the right. \(\square\)

This dominance identity is exact even when a coordinate has several
positive runs elsewhere on the owner cycle.

## 2. Audit of the floor-correct southwest exclusion

### Lemma 2.1

If \(P_{s,t}\) is floor-correct, then

\[
 \boxed{
 \nexists x\in C:\quad u_x<s\text{ and }v_x<t.}
\tag{2.1}
\]

#### Proof

List the \(L=s+t\) owners in (1.3) as

\[
 Y_0=X_{-s},Y_1,\ldots,Y_{L-1}=X_{t-1}.
\tag{2.2}
\]

Map every coordinate of \(Y_0\setminus P_{s,t}\) to the transition at
which it first departs.  This is an injection into the \(L-1\) internal
transitions, because one Johnson transition removes only one coordinate.

Suppose \(x\in C\) has \(u_x<s\) and \(v_x<t\).  The first strict
inequality gives an internal arrival of \(x\) into its positive run through
the cut.  The second gives a later internal departure.

That later departure transition is not in the first-departure image.  If
\(x\notin Y_0\), then \(x\) is not an initial coordinate.  If
\(x\in Y_0\), then \(x\) departed before the displayed re-arrival, so the
later departure is not its first.  Since the transition removes \(x\), it
cannot simultaneously be the first departure of another coordinate.

At most \(L-2\) transitions are therefore used by the injection, and

\[
 |P_{s,t}|
 \ge(m+1)-(L-2)
 =m+3-s-t,
\tag{2.3}
\]

contrary to floor correctness. \(\square\)

This proof explicitly permits repeated runs.  The later departure is the
unused transition which makes equality in (1.4) impossible.

## 3. Audit of the Pareto staircase

Discard multiplicities from \(\mathcal D\), and list its Pareto-minimal
points by increasing first coordinate:

\[
 d_1=(a_1,b_1),\ldots,d_r=(a_r,b_r).
\tag{3.1}
\]

Their second coordinates strictly decrease.  Construct a southeast unit
lattice path \(\Gamma\) from \((1,H)\) to \((H,1)\) through all the
\(d_i\), moving east before south between successive required points.
It has exactly

\[
 (H-1)+(H-1)+1=2H-1
\tag{3.2}
\]

vertices.

### Lemma 3.1 (rectangle interception)

Let \(q=(s,t)\in[H]^2\) have no point of \(\mathcal D\) strictly southwest
of it.  If \(p\in\mathcal D\) and \(p\ge q\), then

\[
 \boxed{\Gamma\cap[q,p]\ne\varnothing.}
\tag{3.3}
\]

#### Proof

Choose a Pareto-minimal \(d\in\mathcal D\) with \(d\le p\).  A minimum
inside \(\mathcal D\cap(-\infty,p]\) is automatically a global Pareto
minimum, so \(\Gamma\) passes through \(d\).

If \(d\ge q\), use \(d\).  Otherwise southwest exclusion leaves exactly
two one-sided cases.

If \(d_1<s\) and \(d_2\ge t\), follow \(\Gamma\) forward until its first
coordinate reaches \(s\).  Every Pareto minimum encountered while its
first coordinate is below \(s\) has second coordinate at least \(t\);
otherwise it would lie strictly southwest of \(q\).  The east-before-south
convention therefore produces

\[
 z=(s,z_2),\qquad z_2\ge t.
\tag{3.4}
\]

Forward monotonicity gives \(z_2\le d_2\le p_2\), while \(s\le p_1\).
Thus \(q\le z\le p\).

If \(d_1\ge s\) and \(d_2<t\), traverse \(\Gamma\) backward.  Backward
motion is north before west.  Until height \(t\) is reached, southwest
exclusion keeps the first coordinate at least \(s\), so the path contains

\[
 z=(z_1,t),\qquad z_1\ge s.
\tag{3.5}
\]

Backward monotonicity gives \(z_1\le d_1\le p_1\), and \(t\le p_2\).
Again \(q\le z\le p\).  The same argument includes the initial and final
endpoint segments of \(\Gamma\). \(\square\)

The direction convention is essential: east-before-south forward is
north-before-west backward.

## 4. The literal \(2H-1\)-letter lower chart

For every staircase vertex \(z=(r,w)\), emit the actual set

\[
 Q_z=P_{r,w}.
\tag{4.1}
\]

### Theorem 4.1

For every floor-correct \(P_{s,t}\),

\[
 \boxed{
 P_{s,t}
 =\bigcup_{\substack{z\in\Gamma\\z\ge(s,t)}}Q_z.}
\tag{4.2}
\]

The sets on the right occur in one contiguous subword of the staircase
word.

#### Proof

Along \(\Gamma\), the first coordinate is nondecreasing and the second is
nonincreasing.  Hence \(z_1\ge s\) is a suffix condition and \(z_2\ge t\)
is a prefix condition.  Their intersection is one contiguous subpath.

For every selected \(z\ge(s,t)\), Lemma 1.1 gives
\(Q_z\subseteq P_{s,t}\).  Conversely, take \(x\in P_{s,t}\).  Then
\(p_x\ge(s,t)\).  Lemma 2.1 supplies the hypothesis of Lemma 3.1, so there
is a staircase vertex

\[
 (s,t)\le z\le p_x.
\tag{4.3}
\]

Lemma 1.1 then gives \(x\in Q_z\).  This proves (4.2), coordinate by
coordinate and with all multiplicities harmless. \(\square\)

Every staircase letter is nonzero.  It intersects at most \(2H\)
consecutive owners, hence

\[
 |Q_z|\ge m+2-2H\ge1
\tag{4.4}
\]

under (0.1).

## 5. Upper chart, several cuts, and exact constants

The \(2H\)-letter owner word

\[
 X_{-H},X_{-H+1},\ldots,X_{H-1}
\tag{5.1}
\]

exposes every crossing union of at most \(H+1\) owners as one literal
contiguous OR.  Concatenating (5.1) with the lower staircase gives

\[
 (2H-1)+2H=4H-1.
\tag{5.2}
\]

If a cycle of length \(\ell\) is cut at \(J\) transition edges meeting all
positive residence intervals of length at most \(H\), endpoint-capped
erosion of the resulting \(J\) paths costs \(\ell+HJ\).  Append one
\((4H-1)\)-letter chart at every cut.  Every destroyed depth-at-most-\(H\)
window crosses at least one selected cut and is represented in that
cut's chart, defined from the original cyclic owners.  This remains true
when cuts are closer than \(H\).  The total is therefore

\[
 \ell+HJ+(4H-1)J=\ell+(5H-1)J.
\tag{5.3}
\]

For PBBS cycles, the unextended owner lengths total \(W\), the number of
inactive cycles is at most \(B_m\), and a minimum transversal on every
active cycle satisfies

\[
 \sum_CJ_C\le2\nu_H(P_m).
\tag{5.4}
\]

Inactive cyclic erosion costs \(2H\) per cycle.  Equations
(5.3)--(5.4) give (0.4).

The scope restriction \(2H\le m+1\) is part of (0.4).  It holds for
\(H=\lceil A\sqrt m\rceil\) once \(A\) is fixed and \(m\) is sufficiently
large, and it is explicitly enforced during a slow fixed-\(A\)
diagonalization.

## 6. Coefficient-one implication and quantifiers

Assume (0.5) for every fixed \(A>0\).  Fix \(A\), put
\(H=\lceil A\sqrt m\rceil\), and let \(K_A\) be the implied constant.
Dividing (0.4) by \(W=(2m+1)B_m\) gives

\[
 {L_H-W\over W}
 \le
 {2H+2K_A(5H-1)\over2m+1}
 =O_{A,K_A}(m^{-1/2}).
\tag{6.1}
\]

Thus every fixed Gaussian central window has a literal word of length
\(W+o_A(W)\).

The audited product-SCD construction supplies a word for the two outer
tails with normalized fixed-\(A\) cost tending to zero as
\(A\to\infty\).  Choose increasing integer values \(A=j\), and for each
\(j\) choose a threshold beyond which

1. (0.5) holds with its fixed constant \(K_j\);
2. the right side of (6.1) is at most \(1/j\);
3. \(2\lceil j\sqrt m\rceil\le m+1\); and
4. the product-SCD tail is within \(1/j\) of its fixed-\(j\) limiting
   bound.

Take \(j=j(m)\) piecewise constant between successive thresholds.  Then
\(j(m)\to\infty\), every nonuniform fixed-\(j\) estimate is used only
beyond its own threshold, the central excess is \(o(W)\), and the tail
cost is \(o(W)\).  The standard trimmed-coordinate lift transfers the
same leading constant to even dimension.

Therefore (0.5) implies

\[
 \boxed{
 \nu(k)\le(1+o(1)){k\choose\lfloor k/2\rfloor}.}
\tag{6.2}
\]

No literal enumeration of the outer ranks is used.

## 7. Adversarial checks and exact boundary

The following potential failures were checked independently.

1. **Repeated coordinate runs.**  They do not affect Lemma 2.1; the later
   departure after the run through the cut is still outside the
   first-departure injection.
2. **Multiplicity of extent points.**  The staircase uses distinct Pareto
   points, while (4.2) is proved coordinatewise, so coincident points
   carry every coordinate with that extent.
3. **First and last Pareto points.**  The endpoint segments from
   \((1,H)\) and to \((H,1)\) use the same east-before-south convention and
   satisfy Lemma 3.1.
4. **Boundary equality.**  Points directly west or directly south of a
   correct query are permitted.  The rectangle proof treats these as its
   two one-sided cases; only a point strictly southwest is forbidden.
5. **Contiguity.**  The witness in (4.2) is prefix intersect suffix on one
   monotone path, not a union of separated intervals.
6. **Nonempty helpers.**  The full square chart, rather than only the
   triangular target region, explains the stronger condition
   \(2H\le m+1\).
7. **Nearby cuts.**  A chart uses original cyclic owners and is appended
   as a whole block; endpoint dummy choices at other cuts cannot alter it.
8. **Implication scope.**  The deterministic seam is proved.  The
   Catalan residence estimate (0.5) is not.

The proved local order is \(O(H)\).  A clean collar with \(H\) distinct
equal-rank crossing targets gives the elementary lower bound
\(\Omega(H)\), so the worst-case order of the deterministic one-cut seam
is

\[
 \boxed{\Theta(H).}
\tag{7.1}
\]

No claim is made that the constant \(4\) is optimal.  The remaining PBBS
coefficient-one gate is the Catalan-order residence estimate (0.5), not a
literal cut-seam obstruction.
