# Adjacent-priority aligned path switches in the pair-omission token system

Date: 2026-07-25

Critical legality and floor-energy audit: see
`MATH_ATTACK_S11_INTERVAL_PACKET_FLOOR_ENERGY_AUDIT_20260725.md`.
That audit proves a complementary orientation-preserving interval-packet
cube with total (o(W/H)) boundaries and the exact dichotomy “one strict
floor-quadratic interval descent, or the entire packet cube is orthogonal
and energy-flat.”

## 0. Outcome

Let

\[
 n=2m+1
\]

and let (P_1,\ldots ,P_m) be disjoint coordinate pairs, with one
coordinate left unpaired.  Compare the two first-avoided-pair token
matchings obtained by interchanging two adjacent priorities

\[
 A=P_j,
 \qquad
 B=P_{j+1},
\]

without changing the local factors attached to the omitted pairs.

This report proves the following exact results.

1. The changed lower targets are precisely

   \[
   D_j=left\{S:
       S\cap P_h\ne\varnothing\ (h<j),
       \quad S\cap(A\cup B)=\varnothing
       \right\}.
   \]

   The old and new token edges on (D_j) form alternating paths and
   cycles.  A shared middle owner necessarily avoids (A\cup B).

2. Arbitrary component-side choices need not preserve few physical row
   runs.  On a cycle only the two complete sides are legal; on a path all
   legal central interpolants are monotone thresholds in exchange order.
   Exchange order need not agree with physical row order for arbitrary
   fixed factors.  Thus the (O(j)) changed membership intervals per row
   do not by themselves prove a low-run hybrid.

3. There is an exact choice of fixed factors which removes this order
   obstruction.  Choose an arbitrary exact factor (F_A), let
   \(	heta:Q_A\to Q_B\) fix the common ground and map (B) bijectively
   to (A), and define (F_B) by applying (	heta) to the reversals of
   all rows of (F_A).  In this fixed pair of factors, the alternating
   components are exactly the maximal (D_j)-intervals in the rows of
   (F_A).  Every component is a path, and every legal threshold on it
   uses one interval in its (F_A)-row and one interval in its (F_B)-row.

4. If (K_j) is the number of these paths, then

   \[
   K_j\le \min\{2jR_m,|D_j|\},
   \qquad
   R_m=\frac1{2m-1}\binom{2m-1}{m-1}.
   \]

   Every simultaneous choice of path thresholds has at most (2K_j)
   more runs than either endpoint, before the already audited endpoint
   ledger is added.  Uniformly in (j),

   \[
   K_j=O\left(\frac{W\log m}{m}\right).
   \]

   For (j=1), (K_1=R_m=O(W/m)), while the changed mass is exactly

   \[
   |D_1|=\frac m2R_m.
   \]

   Consequently the mean path length is exactly (m/2), and at least
   half of the changed tokens lie on paths of length at least (m/4).
   No pointwise lower bound holds: singleton paths may coexist with the
   long paths.

5. On a path of (b) lower vertices, a complete side switch has, at
   signed depth (q), at most

   \[
   2\min\{b,q-1\}
   \]

   lower occurrences and

   \[
   2\min\{b,q+1\}
   \]

   upper occurrences in its load difference.  In particular,

   \[
   \|z_{K,q}^-\|_1+\|z_{K,q}^+\|_1\le4q.
   \]

   For an explicitly completed long path with (b\ge H+1), equality
   holds at every (q\le H): there are (q-1) removed and (q-1)
   inserted lower flags, and (q+1) removed and (q+1) inserted upper
   flags.  Hence

   \[
   \sum_{q=1}^H
   \bigl(\|z_{K,q}^-\|_1+\|z_{K,q}^+\|_1\bigr)
   =2H(H+1),
   \]

   independently of (b).

6. This gives an actual integral defect-reducing block switch.  At the
   first upper depth the long path replaces exactly two old boundary
   targets by two new boundary targets.  If the old targets have load at
   least two and the new targets are holes, first-upper collision excess
   drops by exactly two while the run count changes by at most two.
   Moreover the geometrically weighted all-depth corridor energy defined
   in Theorem 6.3 below drops by at least

   \[
   \frac{38}{49}.
   \]

   Thus the requested contraction per (O(1)) new row boundaries is
   literal and proved, under an explicit endpoint load condition.

7. The endpoint load condition is not forced by path geometry.  At
   Gaussian depth the whole (j=1) swap changes at most

   \[
   O\left(\frac{WH^2}{m}\right)=O(W)
   \]

   signed-depth occurrences, and only (O(W/m)) first-upper occurrences.
   Therefore one adjacent swap cannot remove a \(\Theta(W)\) first-upper
   collision defect.  The geometric energy is also too weak to certify
   (o(W)) defect separately at every depth.  Iterating enough adjacent
   swaps would require a compatible factor atlas and a nonaccumulating
   run theorem; neither is proved here.  Constant one is not claimed.

All switches below remain inside one fixed integral token system.  Every
selected token retains both of its literal Pascal parents, and every row
cut is paid by the standard initialization collar.  No histogram
cancellation is used as a substitute for physical realizability.

## 1. Setup and the exact changed family

Put

\[
 V_-={ [n]\choose m-1},
 \qquad
 V_0={ [n]\choose m},
 \qquad
 W=|V_0|.
\]

For an omitted pair (P), let

\[
 Q_P=[n]\setminus P.
\]

A cyclic row

\[
 \pi=(x_0,\ldots ,x_{2m-2})
\]

in an exact local factor (F_P) supplies, at cyclic start (i), the
token

\[
 e(P,\pi,i)=(S_i,Y_i),
\]

where

\[
 S_i=I_\pi(i,m-1),
 \qquad
 Y_i=I_\pi(i-1,m).
\tag{1.1}
\]

For (1\le q\le H), its two literal flags are

\[
 L_q(e)=I_\pi(i+q-1,m-q),
 \qquad
 U_q(e)=I_\pi(i-1,m+q).
\tag{1.2}
\]

The first-avoided rule assigns (Sin V_-) to the least priority pair it
avoids.  Let (M) be the resulting token matching in the order

\[
 P_1,\ldots ,P_{j-1},A,B,P_{j+2},\ldots ,P_m,
\]

and let (N) be the matching obtained after interchanging (A,B), with
every local factor kept fixed.

### Proposition 1.1 (exact support of an adjacent priority swap)

The lower target (S) changes token carrier if and only if

\[
 S\in D_j
 :=\left\{S\in V_-:
 S\cap P_h\ne\varnothing\ (h<j),
 \quad
 S\cap A=S\cap B=\varnothing
 \right\}.
\tag{1.3}
\]

Moreover

\[
 \boxed{
 |D_j|
 =\sum_{t=0}^{j-1}(-1)^t\binom{j-1}{t}
   \binom{2m-3-2t}{m-1}.}
\tag{1.4}
\]

In particular,

\[
 \boxed{
 |D_1|=\binom{2m-3}{m-1}
 =\frac{m(m+1)}{4(2m-1)(2m+1)}W.}
\tag{1.5}
\]

#### Proof

If (S) avoids an earlier pair, both orders decide it before reaching
(A,B).  If (S) avoids (A) but meets (B), both orders assign it to
(A); the symmetric assertion holds if it meets (A) and avoids (B).
If it meets both, neither of these priorities decides it.  It changes
carrier exactly when it reaches this adjacent pair and avoids both, which
is (1.3).

The common ground

\[
 R=[n]\setminus(A\cup B)
\]

has (2m-3) coordinates.  Inclusion-exclusion over the (j-1) earlier
pairs gives (1.4).  Taking (j=1) gives the first equality in (1.5); the
second follows by direct factorial cancellation.  \(\square\)

## 2. General overlay structure and the fragmentation gate

Retain the labelled token edges on (D_j), including parallel edges.
Every (S\in D_j) has one old (F_A)-edge and one new (F_B)-edge.
Each endpoint family is a middle-simple matching.

### Proposition 2.1 (alternating components and shared owners)

The labelled overlay on (D_j\sqcup V_0) is a disjoint union of even
alternating paths and cycles.  If a middle owner occurs on both sides,
then it avoids (A\cup B).

#### Proof

Every changed lower vertex has degree two, one edge of each colour.  Every
middle vertex has degree at most one in each colour, hence total degree at
most two.  The component assertion follows.

An old owner belongs to (Q_A) and therefore avoids (A).  A new owner
belongs to (Q_B) and therefore avoids (B).  Equality of the two owners
forces avoidance of both pairs.  \(\square\)

The phrase “choose sides on the alternating components” needs one exact
qualification on open paths.

### Theorem 2.2 (all legal central interpolants)

Let an alternating path be written

\[
 y_0,S_1,y_1,S_2,\ldots ,S_b,y_b,
\]

with old edges (y_{i-1}S_i) and new edges (S_i y_i).  A subset of
these edges saturates all (S_i) and is middle-simple if and only if, for
a unique (r\in\{0,1,\ldots ,b\}), it takes

\[
 \{y_{i-1}S_i:i\le r\}
 \cup
 \{S_i y_i:i>r\}.
\tag{2.1}
\]

On an alternating cycle, the only two legal choices are the complete old
side and the complete new side.

#### Proof

Write (u_i=1) if the old edge at (S_i) is chosen and (u_i=0) if the
new edge is chosen.  At internal owner (y_i), the pattern

\[
 (u_i,u_{i+1})=(0,1)
\]

would choose both incident edges.  Thus

\[
 u_i\ge u_{i+1}.
\]

On a path this forces the unique word (1^r0^{b-r}).  On a cycle the
inequalities are cyclic and all bits are equal.  Conversely these choices
are directly middle-simple and saturate every lower vertex.  \(\square\)

### Proposition 2.3 (number of open paths)

For any two lower-saturating token matchings, the number (p) of open
alternating paths obeys

\[
 \boxed{p\le W-|V_-|=\frac{2W}{m+2}.}
\tag{2.2}
\]

#### Proof

An open path has one old-only and one new-only middle endpoint.  Hence
(p=|U_M\setminus U_N|), where (U_M,U_N) are the two used middle sets.
Both have size (|V_-|), so (U_M\setminus U_N) is contained in the
middle set missed by (N).  The displayed binomial difference is exact.
\(\square\)

Neither (2.2) nor the low-run bounds at the two endpoints control hybrid
fragmentation.  The exact reason is that the exchange order in Theorem
2.2 can be interlaced arbitrarily through physical row order.

For completeness, give every changed lower vertex (S) its bit (u_S),
where (u_S=1) means its old edge is selected.  Direct every exchange
arc so that legality is

\[
 u_S\ge u_T.
\tag{2.3}
\]

Along every old physical row, a (0\to1) transition of these bits is a
new old-row run start.  Along every new physical row, a (1\to0)
transition is a new new-row run start.  Thus, if (E_M^{\rm phys}) and
(E_N^{\rm phys}) are the directed physical adjacency sets, the exact
interior boundary functional is

\[
 \begin{aligned}
 T(u)
 ={}&|\{S\to T\in E_M^{\rm phys}:u_S=0,u_T=1\}|\\
 &+|\{S\to T\in E_N^{\rm phys}:u_S=1,u_T=0\}|.
 \end{aligned}
\tag{2.4}
\]

Every edge counted by (T(u)) is a distinct selected-run start.  Hence

\[
 J(u)\ge T(u).
\tag{2.5}
\]

One exchange path can be ordered in a physical row as

\[
 1,b,2,b-1,3,b-2,\ldots .
\]

The central threshold (1^r0^{b-r}) then has

\[
 T(u)\ge2\min\{r,b-r\}-2,
\]

although both endpoint words have one physical block.  Therefore the
premises “(O(j)) changed intervals per row” and “both endpoints have
few runs” do not prove low-run side selection for arbitrary fixed
factors.

## 3. Reverse-correlated fixed factors

The obstruction in Section 2 disappears under one exact joint choice of
the two local factors.

Choose a bijection

\[
 \theta:Q_A=R\sqcup B\longrightarrow Q_B=R\sqcup A
\tag{3.1}
\]

which fixes (R) pointwise and maps (B) bijectively to (A).  Choose
any exact local factor (F_A).  For each cyclic row (piin F_A), reverse
its cyclic orientation and apply (	heta) coordinatewise.  Let the
resulting row family be (F_B).

### Lemma 3.1 (factor exactness)

(F_B) is an exact local factor on (Q_B).

#### Proof

Reversing a cyclic order preserves, up to reindexing, its collections of
length-((m-1)) and length-(m) windows.  Applying the coordinate
bijection (	heta) sends the exact partitions supplied by (F_A) to
exact partitions on (Q_B).  \(\square\)

The two factors are now fixed.  Only the priority order is changed.

### Theorem 3.2 (maximal changed intervals are whole aligned paths)

In the reverse-correlated factors of (3.1), the alternating components
on (D_j) are exactly the maximal cyclic intervals of (D_j)-starts in
the rows of (F_A).  Every component is an open path.

If such an interval has starts

\[
 S_i=I_\pi(i,m-1),
 \qquad a\le i<a+b,
\]

then exchange order is increasing (i) in the (F_A)-row and decreasing
physical position in the corresponding (F_B)-row.  Every legal threshold
of Theorem 2.2 therefore selects one interval in each of these two rows.

#### Proof

Because (S_i\in D_j), it is contained in (R), and (	heta(S_i)=S_i).
In the old row its owner is

\[
 I_\pi(i-1,m)=S_i\cup\{\pi_{i-1}\}.
\]

In the reversed new row its owner is

\[
 \theta(I_\pi(i,m))
 =S_i\cup\{\theta(\pi_{i+m-1})\}.
\]

If (S_{i+1}\in D_j), then (pi_{i+m-1}\in R), so (	heta) fixes it,
and

\[
 S_i\cup\{\pi_{i+m-1}\}
 =I_\pi(i,m)
 =S_{i+1}\cup\{\pi_i\}.
\tag{3.2}
\]

The left side is the new owner of (S_i); the right side is the old owner
of (S_{i+1}).  Hence consecutive changed starts are consecutive in one
alternating path.

Conversely, a shared owner avoids (A\cup B) by Proposition 2.1.  In the
exact factor (F_A) it is a unique length-(m) window.  Its old and new
preimages are therefore precisely the two adjacent length-((m-1))
facets displayed in (3.2).  If the adjacent facet is not in (D_j), no
other changed token can continue the component.  Thus maximal changed
intervals are exactly the whole components.

No row can consist entirely of (D_j)-starts, since every such start
avoids both coordinates of (B), while every coordinate occurs in some
length-((m-1)) window of a cyclic row.  Hence every component has two
middle endpoints and is a path.

Finally, Theorem 2.2 chooses an initial interval in exchange order on the
old row and the complementary terminal interval on the new row.  Reversal
makes both sets physical intervals.  \(\square\)

### Corollary 3.3 (component and run bounds)

Put

\[
 A_m=\binom{2m-1}{m-1},
 \qquad
 R_m=\frac{A_m}{2m-1}
 =\frac{m+1}{2(2m+1)(2m-1)}W.
\tag{3.3}
\]

Let (K_j) be the number of paths in Theorem 3.2.  Then

\[
 \boxed{K_j\le\min\{2jR_m,|D_j|\}.}
\tag{3.4}
\]

For arbitrary simultaneous legal thresholds on these paths,

\[
 \boxed{J(M_{\rm child})\le J(M)+2K_j.}
\tag{3.5}
\]

The same inequality holds with (N) in place of (M).

#### Proof

In one old row, a changed start avoids (B) and meets every earlier pair.
For one coordinate pair, the cyclic start set of length-((m-1)) windows
which avoid both coordinates has at most two circular components.  The
avoid-(B) set has at most two components; subtracting the union of the
(j-1) earlier-pair avoid sets leaves at most

\[
 2+2(j-1)=2j
\]

components.  There are (R_m) rows, proving the first bound in (3.4); the
second is trivial.

On one path threshold, deleting a cyclic selected interval from its old
row changes that row's run count by at most one, and adding the new
interval changes the new row's count by at most one.  Summing gives (3.5).
The cyclic all-selected exception only improves this bound.  \(\square\)

The category-tail estimate from the first-avoided construction gives an
absolute (C) such that

\[
 |D_j|\le C\sqrt m,A_m(3/4)^{j-1}.
\tag{3.6}
\]

Combining (3.4) and (3.6), and splitting at

\[
 t=\lceil20\log m\rceil,
\]

gives uniformly in (j)

\[
 \boxed{K_j=O\left(\frac{W\log m}{m}\right).}
\tag{3.7}
\]

Thus a single adjacent-priority interpolation adds (o(W/H)) runs for
(H=o(m/\log m)).  The endpoint first-avoided matching itself has the
stronger restriction (H=o(m/\log ^2m)), so no run quantifier is lost in
the currently relevant Gaussian range.

### Proposition 3.4 (path sizes)

Every path in Theorem 3.2 has between (1) and (m-1) lower vertices.
For (j=1),

\[
 |D_1|=\frac m2R_m,
 \qquad
 K_1=R_m.
\tag{3.8}
\]

Consequently the mean path length is exactly (m/2), and at least
(|D_1|/2) changed tokens lie on paths of length at least (m/4).

#### Proof

If (b) consecutive starts all avoid (B), their union is a consecutive
coordinate segment of size (m+b-2) containing no coordinate of (B).
Only (2m-3) common coordinates are available, so

\[
 m+b-2\le2m-3,
\]

or (b\le m-1).

For (j=1), delete the two positions occupied by (B) from one cyclic
row.  The remaining common coordinates form two linear arcs whose lengths
sum to (2m-3).  Exactly one arc has length at least (m-1): at least one
does by averaging, and both cannot because their sum is (2m-3).  That
long arc contains one nonempty interval of length-((m-1)) windows
avoiding (B), while the short arc contains none.  Hence every row
contributes exactly one path and (K_1=R_m).  Equations (1.5) and (3.3)
then give mean length (m/2).

If more than half of the changed tokens lay on paths shorter than (m/4),
those paths would contain fewer than

\[
 K_1\frac m4=\frac{|D_1|}{2}
\]

tokens, a contradiction.  \(\square\)

This is only a mass statement.  It does not exclude singleton paths.

## 4. One explicit long component

The following finite construction makes every flag boundary visible.

Let

\[
 A=\{\alpha _0,\alpha _1\},
 \qquad
 B=\{\beta _0,\beta _1\},
\]

and fix

\[
 1\le H\le b-1,
 \qquad
 1\le b\le m-1.
\tag{4.1}
\]

Choose distinct common coordinates

\[
 x_0,\ldots ,x_{b+m-3}
\]

such that

\[
 S_i:=\{x_i,\ldots ,x_{i+m-2}\}
\tag{4.2}
\]

meets every earlier pair (P_h), (h<j), for all (0\le i<b).  Put

\[
 r=m-b-1
\]

and complete the common coordinates by distinct

\[
 y_0,\ldots ,y_{r-1}.
\]

Take the two cyclic rows

\[
 \begin{aligned}
 \pi_A={}&(\beta _0,x_0,\ldots ,x_{b+m-3},
                \beta _1,y_0,\ldots ,y_{r-1}),\\
 \pi_B={}&(\alpha _0,x_{b+m-3},\ldots ,x_0,
                \alpha _1,y_{r-1},\ldots ,y_0).
 \end{aligned}
\tag{4.3}
\]

They have exactly (2m-1) entries.  The second is the reverse-correlated
image of the first under

\[
 \theta(\beta _0)=\alpha _1,
 \qquad
 \theta(\beta _1)=\alpha _0.
\]

One prescribed row is legitimate in an exact factor: complete the desired
cyclic order, take any existing exact factor, and relabel one of its rows
coordinate-by-coordinate to this order.  Defining the second whole factor
by reverse correlation then realizes both rows while keeping both factors
fixed.  This argument prescribes one row in (F_A); Theorem 3.2, rather
than an unproved multirow extension lemma, supplies the simultaneous
global family.

Let (e_i) be the old (F_A)-token at (S_i) and (f_i) the new
(F_B)-token at the corresponding reversed start.

### Theorem 4.1 (whole long alternating path)

The (2b) labelled token edges form the whole alternating path

\[
 \begin{aligned}
 \{\beta _0\}\cup S_0
 &\;--\;S_0\;--\;X_0\;--\;S_1\;--\;X_1\;--\cdots\\
 &\cdots--\;X_{b-2}\;--\;S_{b-1}
   \;--\;\{\alpha _0\}\cup S_{b-1},
 \end{aligned}
\tag{4.4}
\]

where

\[
 X_i=\{x_i,\ldots ,x_{i+m-1}\}.
\tag{4.5}
\]

Every legal threshold changes the total source-row run count by at most
two relative to either endpoint.

#### Proof

The old owners are

\[
 Y_i^-=
 \begin{cases}
 S_0\cup\{\beta _0\},&i=0,\\
 S_i\cup\{x_{i-1}\},&1\le i<b,
 \end{cases}
\tag{4.6}
\]

and the new owners are

\[
 Y_i^+=
 \begin{cases}
 S_i\cup\{x_{i+m-1}\},&0\le i<b-1,\\
 S_{b-1}\cup\{\alpha _0\},&i=b-1.
 \end{cases}
\tag{4.7}
\]

Thus

\[
 Y_i^+=Y_{i+1}^-=X_i
 \qquad(0\le i<b-1).
\]

The left endpoint contains a coordinate of (B), so it cannot occur in
an (F_B)-token.  The right endpoint contains a coordinate of (A), so
it cannot occur in an (F_A)-token.  Exact middle-window uniqueness in
the two factors excludes every other continuation.  Hence (4.4) is a
whole component.

The old starts (0,\ldots ,b-1) form one interval in (pi_A), while
the new starts form one interval in the reversed row.  The monotone
threshold theorem leaves an interval in each.  Deleting one interval and
adding one interval changes the two cyclic run counts by at most one each.
\(\square\)

The earlier-pair condition in (4.2) is essential.  A simple sufficient
condition is to place one coordinate from each earlier pair in

\[
 \bigcap_{i=0}^{b-1}S_i
 =\{x_{b-1},\ldots ,x_{m-2}\},
\]

which is possible if

\[
 b\le m-j+1.
\tag{4.8}
\]

This is not necessary.  At the maximal length (b=m-1), put the unpaired
coordinate at (x_{m-2}) and the remaining pairs outside (A,B) at

\[
 \{x_h,x_{h+m-1}\},
 \qquad 0\le h\le m-3.
\]

Then every window in (4.2) meets every one of these pairs.

## 5. Exact multidepth boundary span

Write

\[
 [a,b]_x:=\{x_a,x_{a+1},\ldots ,x_b\}.
\]

For the complete side switch (e_i\mapsto f_i), let

\[
 z_q^-=\mu_q^-(\text{new})-\mu_q^-(\text{old}),
 \qquad
 z_q^+=\mu_q^+(\text{new})-\mu_q^+(\text{old}).
\]

### Theorem 5.1 (lower and upper telescoping)

For (1\le q\le H),

\[
 L_q(e_i)=[i+q-1,i+m-2]_x,
 \qquad
 L_q(f_i)=[i,i+m-q-1]_x.
\tag{5.1}
\]

Consequently

\[
 \boxed{
 z_q^-
 =\sum_{s=0}^{q-2}{\bf e}_{[s,s+m-q-1]_x}
 -\sum_{s=b}^{b+q-2}{\bf e}_{[s,s+m-q-1]_x}.}
\tag{5.2}
\]

In particular,

\[
 \|z_q^-\|_1=2(q-1).
\tag{5.3}
\]

For the upper flags, the old terms with token indices

\[
 i=1,\ldots ,b-q-1
\]

equal the new terms with indices

\[
 i=q,\ldots ,b-2.
\]

After this cancellation, exactly (q+1) old and (q+1) new upper
occurrences remain.  Every remaining old upper target meets (B) and
avoids (A); every remaining new upper target meets (A) and avoids
(B).  Hence no old-new cancellation is possible and

\[
 \|z_q^+\|_1=2(q+1).
\tag{5.4}
\]

Thus

\[
 \boxed{
 \|z_q^-\|_1+\|z_q^+\|_1
 =\|z_q^-\|_2^2+\|z_q^+\|_2^2
 =4q.}
\tag{5.5}
\]

#### Proof

Equation (5.1) follows directly from the two row orientations and (1.2).
The old lower term at (i) equals the new lower term at (i+q-1).
The common range is (0\le i\le b-q), leaving the two boundary sums in
(5.2).  Proper cyclic windows in a row of distinct coordinates are
distinct, proving (5.3).

For upper flags, the old (i)-term and new ((i+q-1))-term are the same
length-((m+q)) (x)-interval whenever

\[
 1\le i\le b-q-1.
\]

The old boundary consists of its left endpoint term and (q) right
terms; the new boundary consists of (q) left terms and its right endpoint
term.  In the full rows (4.3), crossing the old changed interval at either
end encounters (eta _0) or (eta _1), while crossing the new interval
encounters (alpha _1) or (alpha _0).  This proves the asserted sector
separation and (5.4).  Summing (5.3)--(5.4) gives (5.5).  \(\square\)

At the first upper depth the four targets are especially simple:

\[
 \begin{aligned}
 O_L&=\{\beta _0,x_0,\ldots ,x_{m-1}\},\\
 O_R&=\{x_{b-2},\ldots ,x_{b+m-3},\beta _1\},\\
 P_L&=\{x_0,\ldots ,x_{m-1},\alpha _1\},\\
 P_R&=\{\alpha _0,x_{b-2},\ldots ,x_{b+m-3}\}.
 \end{aligned}
\tag{5.6}
\]

Thus

\[
 z_1^+={\bf e}_{P_L}+{\bf e}_{P_R}
       -{\bf e}_{O_L}-{\bf e}_{O_R},
 \qquad
 z_1^-=0.
\tag{5.7}
\]

### Corollary 5.2 (short paths and arbitrary thresholds)

For a reverse-correlated component with (b) lower vertices, and also for
the subinterval changed by any legal threshold,

\[
 \boxed{
 \|z_q^-\|_1\le2\min\{b,q-1\},
 \qquad
 \|z_q^+\|_1\le2\min\{b,q+1\}.}
\tag{5.8}
\]

Therefore

\[
 \|z_q^-\|_1+\|z_q^+\|_1\le4q
\tag{5.9}
\]

without any lower bound on (b).

#### Proof

The lower cancellation in Theorem 5.1 uses only consecutive starts inside
the changed subinterval, so truncating the interval gives the first bound
immediately.

For the upper bound one must also retain the (	heta)-twist; consecutive
starts alone are not a sufficient explanation.  Write the switched block
as (a\le i\le c) in its (F_A)-row.  Before applying (	heta), the old
upper windows have cyclic starts

\[
 [a-1,c-1],
\]

while the underlying windows of the reversed new flags have starts

\[
 [a-q,c-q].
\]

The unmatched shifted tails contribute at most (q-1) old and (q-1)
new occurrences.  In the overlap, pair an old window (W) with the new
window (	heta W).  The consecutive changed lower windows strictly
inside the block cover all of (W) except possibly its two endpoint
coordinates.  Away from the two extreme overlap positions, the adjacent
changed lower windows also cover those endpoints.  Since every changed
lower window avoids (A\cup B), such an interior (W) avoids
(A\cup B), and hence (	heta W=W).  Only the two extreme overlap
windows can fail this equality, contributing at most two additional old
and two additional new occurrences.  Thus the upper (ell _1)-difference
is at most

\[
 2(q-1)+4=2(q+1).
\]

If the block has fewer than (q+1) tokens, the trivial bound (2b) is
sharper.  This proves (5.8).  \(\square\)

For the complete long path through depth (H), (5.5) gives the exact
stacked ledger

\[
 \boxed{
 \sum_{q=1}^H
 \bigl(\|z_q^-\|_1+\|z_q^+\|_1\bigr)
 =2H(H+1).}
\tag{5.10}
\]

If depth (q) has weight (w_q), then

\[
 \boxed{
 \sum_{q=1}^Hw_q
 \bigl(\|z_q^-\|_2^2+\|z_q^+\|_2^2\bigr)
 =4\sum_{q=1}^Hq,w_q.}
\tag{5.11}

This is the exact multidepth flag-difference span of one aligned path: its
column lies in the direct sum of the signed zero-mass rank spaces and has
only (4q) unit boundary cells at depth (q), independent of the path's
interior length.

There is also a useful pointed invariant valid without reverse
correlation.  At upper depth (q), define

\[
 \chi_{A,B}(T)
 ={f1}_{\{T\cap A\ne\varnothing\}}
  -{f1}_{\{T\cap B\ne\varnothing\}}.
\tag{5.12}
\]

Every removed old flag avoids (A), and every inserted new flag avoids
(B).  Therefore every old-to-new component or threshold switch satisfies

\[
 \boxed{
 \langle\chi_{A,B},z_q^+\rangle
 =\#\{\text{inserted flags meeting }A\}
  +\#\{\text{removed flags meeting }B\}
 \ge0.}
\tag{5.13}
\]

For the exact long component in (4.3), equality in the sector counts gives

\[
 \langle\chi_{A,B},z_q^+\rangle=2(q+1).
\tag{5.14}
\]

Thus all old-to-new component columns lie in one closed half-space.  Their
exclusive (A/B) boundary parts cannot cancel between components.

## 6. Exact defect and energy changes

Let (mu_T) be the load of a fixed signed rank before a switch, let
(d_T) be its integral load difference, and let (c) be the exact integer
floor at that rank.

Define the floor corridor and floor-corrected quadratic functions

\[
 \psi_c(u)=(c-u)_++(u-c-1)_+,
\tag{6.1}
\]

\[
 \phi_c(u)=\frac12(u-c)(u-c-1).
\tag{6.2}
\]

### Lemma 6.1 (exact scalar switch laws)

For every integral switch,

\[
 \boxed{
 \Delta\mathcal C
 =\sum_T\bigl[\psi_c(\mu_T+d_T)-\psi_c(\mu_T)\bigr],}
\tag{6.3}
\]

and

\[
 \boxed{
 \Delta\Phi
 =\sum_T\left[
 d_T(\mu_T-c)+\frac{d_T(d_T-1)}2
 \right].}
\tag{6.4}
\]

Moreover (psi_c) is one-Lipschitz on the integers, so

\[
 |\Delta\mathcal C|\le\sum_T|d_T|.
\tag{6.5}
\]

#### Proof

Equation (6.3) is the definition.  Expanding
(phi_c(\mu+d)-\phi_c(\mu)) gives (6.4).  The distance from an integer to
the two-point corridor ({c,c+1}) changes by at most one under a unit
step, proving (6.5) by telescoping.  \(\square\)

For a long aligned path, let (mathcal O_q^pm) and
(mathcal P_q^pm) be respectively its removed and inserted boundary
targets.  They have sizes

\[
 |\mathcal O_q^-|=|\mathcal P_q^-|=q-1,
 \qquad
 |\mathcal O_q^+|=|\mathcal P_q^+|=q+1.
\tag{6.6}
\]

If one weight (w_q) is used for both signs at depth (q), the floor
constants cancel separately within each signed rank in (6.4), giving

\[
 \boxed{
 \Delta\Phi_H
 =\sum_{q=1}^Hw_q\left[
   \sum_{T\in\mathcal P_q^-\cup\mathcal P_q^+}\mu_T
  -\sum_{T\in\mathcal O_q^-\cup\mathcal O_q^+}\mu_T
  +2q
 \right].}
\tag{6.7}

Thus the path is a strict quadratic descent exactly when the weighted old
boundary-load advantage exceeds

\[
 2\sum_{q=1}^Hq,w_q.
\tag{6.8}
\]

For the ordinary squared distance rather than (phi_c), both sides of
(6.7) are multiplied by two.

### Theorem 6.2 (literal first-upper block descent)

Suppose the four targets in (5.6) are evaluated in the current matching
and satisfy

\[
 \mu(O_L),\mu(O_R)\ge2,
 \qquad
 \mu(P_L)=\mu(P_R)=0.
\tag{6.9}
\]

Then switching the whole alternating path gives

\[
 \boxed{\Delta C_1^+=-2,}
\tag{6.10}
\]

where

\[
 C_1^+=\sum_T(\mu_T-1)_+,
\]

and

\[
 \boxed{|\Delta J|\le2.}
\tag{6.11}
\]

For squared rank-constant load energy, the (q=1) contribution decreases
by at least four.

#### Proof

Removing one occurrence from a target of load at least two decreases
((\mu-1)_+) by one.  Adding one occurrence to a hole changes its load
from zero to one and costs zero.  The four targets are distinct by their
cyclic-window positions and their (A/B) sectors.  Hence (6.10) follows.
The run bound is Theorem 4.1.  The squared-energy formula is (6.7) with
the factor two: the inserted load sum is zero, the removed load sum is at
least four, and there are two removed targets.  \(\square\)

This is an actual defect-reducing block component, not a marginal or
fractional move.

### Theorem 6.3 (all-depth geometric contraction)

At every signed depth let (c_q^pm) be its exact floor and put

\[
 \mathcal C_q^pm
 =\sum_T\psi_{c_q^pm}(\mu_{q,T}^pm).
\]

Define

\[
 \Lambda_H
 =\mathcal C_1^+
  +\sum_{q=2}^H8^{1-q}
       (\mathcal C_q^-+\mathcal C_q^+).
\tag{6.12}
\]

Under (6.9), the long path switch satisfies

\[
 \boxed{
 \Delta\Lambda_H\le-\frac{38}{49},
 \qquad
 |\Delta J|\le2.}
\tag{6.13}
\]

#### Proof

The first-upper term decreases by two.  At depth (q\ge2), (5.5) and
the one-Lipschitz property give

\[
 |\Delta(\mathcal C_q^-+\mathcal C_q^+)|\le4q.
\]

Therefore

\[
 \begin{aligned}
 \Delta\Lambda_H
 &\le-2+4\sum_{q=2}^{\infty}\frac q{8^{q-1}}\\
 &=-2+4\left(\frac1{(1-1/8)^2}-1\right)\\
 &=-2+\frac{60}{49}
 =-\frac{38}{49}.
 \end{aligned}
\]

The run assertion is unchanged.  \(\square\)

The exponentially small deepest weight in (6.12) is deliberate.  It
proves a genuine integral multidepth descent, but small (Lambda_H) does
not imply (o(W)) unweighted defect at every depth when (H\to\infty).
Thus Theorem 6.3 is not, by itself, the clustered balanced token lemma.

### Proposition 6.4 (one-shot component variance criterion)

Let (z_K) be the complete weighted flag-load difference of path component
(K), let

\[
 z=\sum_Kz_K=\mu(N)-\mu(M),
\]

and let

\[
 Q(X)=\|\mu(X)-\lambda\|_w^2
\]

for a fixed target mean vector (lambda).  Independently choose the old
or new complete side of every path with probability (1/2).  Every
resulting child has the run bound (3.5), and

\[
 \boxed{
 \mathbb E Q(\text{child})
 =\frac{Q(M)+Q(N)}2
  -\frac12\sum_{K<L}\langle z_K,z_L\rangle_w.}
\tag{6.14}

Consequently, if

\[
 \sum_{K<L}\langle z_K,z_L\rangle_w
 >|Q(M)-Q(N)|,
\tag{6.15}
\]

some integral child has energy strictly below both endpoints.

At first upper depth in the (j=1) reverse-correlated construction,

\[
 \langle z_K,z_L\rangle\ge0
\tag{6.16}
\]

for distinct paths: positive cells lie in the (A)-meeting,
(B)-avoiding sector and negative cells in the disjoint (B)-meeting,
(A)-avoiding sector.  Strict overlap of same-sign boundary targets gives
strict inequality.

#### Proof

Write a random child as

\[
 \frac{\mu(M)+\mu(N)}2
 +\frac12\sum_K\varepsilon_Kz_K,
 \qquad \varepsilon_K\in\{-1,1\}.
\]

Orthogonality of the independent signs gives

\[
 \mathbb E Q
 =\left\|\frac{\mu(M)+\mu(N)}2-\lambda\right\|_w^2
  +\frac14\sum_K\|z_K\|_w^2.
\]

The average endpoint energy is the same midpoint term plus

\[
 \frac14\left\|\sum_Kz_K\right\|_w^2.
\]

Expanding the last square proves (6.14).  Condition (6.15) makes the
expectation smaller than the smaller endpoint, so one deterministic child
does as well.  Sector separation proves (6.16).  \(\square\)

No lower bound for the overlap sum in (6.14) follows from the current
factor theorem.  Disjoint component boundary supports give equality and
no contraction.  This is the exact first invalid implication in an
unconditional variance-contraction argument.

## 7. Quantitative global limits

For (j=1), Proposition 3.4 gives exactly (R_m) paths.  By (5.9), an
arbitrary simultaneous threshold choice changes at most

\[
 4qK_1=4qR_m
 =O\left(\frac{Wq}{m}\right)
\tag{7.1}
\]

signed-depth occurrences at depth (q), and at most

\[
 2H(H+1)K_1
 =2H(H+1)R_m
 =O\left(\frac{WH^2}{m}\right)
\tag{7.2}
\]

through depth (H).

At (H=A\sqrt m+O(1)), (7.2) is (O_A(W)), not (o(W)).  At each
individual Gaussian depth, (7.1) is (o(W)).

At first upper depth, one path threshold changes at most two old
occurrences and two new occurrences.  Since deleting one occurrence can
decrease collision excess by at most one, the total possible decrease
under this entire adjacent transposition is at most

\[
 2K_1=2R_m=O(W/m).
\tag{7.3}
\]

Thus a single adjacent priority swap cannot repair a
(Theta(W)) first-upper collision defect, even though its long paths and
run ledger are optimal in scale.

One can impose reverse compatibility along the original chain of pair
labels: choose (F_1), then recursively define (F_{j+1}) as the
reverse-correlated image of (F_j).  This proves the aligned theorem for
each original adjacent pair separately.  It does not provide a complete
permutation atlas.  After priority transpositions create new adjacencies,
the required pairwise identifications have triangle/holonomy consistency
conditions which are not supplied by the recursive chain.  Nor is there a
proved theorem preventing run boundaries from accumulating over enough
successive transpositions to obtain (Theta(W)) total first-upper motion.

## 8. Exact proved/conditional boundary

The following statements are proved.

1. Adjacent priority swaps have the exact changed family (1.3), alternating
   overlay, shared-owner avoidance, and legal-threshold classification.
2. General endpoint low-run bounds do not control hybrid fragmentation.
3. Reverse-correlated fixed factors make every changed interval a whole
   exchange path and align every legal threshold with physical row blocks.
4. The component, length, run, and (4q) multidepth boundary constants are
   exact.
5. Conditions (6.9), (6.8), and (6.15) are exact checkable descent
   criteria.  Under (6.9), collision excess drops by two and the all-depth
   geometric corridor drops by at least (38/49), for at most two new
   runs.
6. All these operations are integral inside fixed exact local factors and
   yield literal token-row OR realizations after the standard collars are
   paid.

The following statements remain unproved and are not inferred here.

1. A collision does not force one of the aligned paths to have overloaded
   old endpoints and hole new endpoints.
2. The component overlap in (6.14) need not be large; path geometry alone
   does not imply energy contraction for the standard all-depth weights.
3. One adjacent swap has only (O(W/m)) first-upper repair capacity.
4. A compatible atlas supporting enough successive adjacent swaps, with
   total (o(W/H)) row boundaries, is not constructed.
5. The geometrically weighted descent does not certify the unweighted
   (o(W)) multidepth defect required for constant one.

Accordingly, the lane now contains a genuine defect-reducing block switch
with (O(1)) new boundaries and a scalable (O(W/m))-path aligned
factor pair.  The remaining gate is no longer physical realizability or
row fragmentation.  It is the global accessibility of favorable endpoint
loads, together with compatible iteration across enough adjacent pair
orders.
