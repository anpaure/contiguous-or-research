# The minimal depth-one \(C_6\) trade and the complete upper-histogram lattice

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Result

Let

\[
 \mathscr E=E(J(n,m)),\qquad
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal U=\binom{[n]}{m+1}.
\]

For a Johnson edge \(e=XY\), put

\[
 L(e)=X\cap Y,\qquad U(e)=X\cup Y,
\]

and let \(B_0,B_-,B_+\) record, respectively, its two middle endpoints,
its lower colour, and its upper colour.  The integral fixed-owner,
fixed-lower trade lattice is

\[
 \mathcal T_{n,m}:=\ker_{\mathbb Z}B_0\cap\ker_{\mathbb Z}B_-.
 \tag{0.1}
\]

Let \(P_{m+1}\) be point-versus-\((m+1)\)-set incidence.  In every
nontrivial central case (\(m\ge2\) and \(n\ge m+2\)) one has the exact
integral equality

\[
 \boxed{
 B_+(\mathcal T_{n,m})=\ker_{\mathbb Z}P_{m+1}.}
 \tag{0.2}
\]

Thus point margins are not merely necessary invariants of the upper
histogram.  They are the **complete integer additive invariants** of the
unrestricted fixed-owner, fixed-lower trade module.  There is no hidden
rational invariant and no finite-index lattice obstruction.

The reverse inclusion in (0.2) is furnished by one support-minimal packet.
On five active coordinates it replaces three disjoint edges by three
disjoint edges.  It preserves every involved owner degree and every lower
colour, while its upper action is the elementary rectangle

\[
 e_{Cbc}+e_{Cad}-e_{Cbd}-e_{Cac},
 \qquad |C|=m-1,
 \tag{0.3}
\]

where \(a,b,c,d\notin C\) are distinct.  No nontrivial binary two-edge
switch can preserve an injective lower-colour ledger.  Hence three removed
and three inserted edges, equivalently an alternating \(C_6\), is the
smallest possible lower-rainbow switch packet.

For a lower-colour-complete cycle on a fixed owner set, (0.2) gives an exact
algebraic answer to the two-sided \(q=1\) question.  On even ground
\(n=2m\), the all-one upper histogram is in the same trade fibre if and
only if every point belongs to exactly half of the selected owners.  This
is algebraic sufficiency only: the resulting integral signed trade need
not be binary, eligible at the given cycle, or connectivity-preserving.
Those are the surviving nonlinear gates.

Terminological caution is useful.  The lower-colour-complete projected
cycle has

\[
 N_-=\binom n{m-1}
\]

edges and is Hamiltonian on its selected owner support.  In the even
central case it is not Hamiltonian on all of \(J(2m,m)\), whose owner count
is larger.  Equivalently, the underlying lower-layer cycle is Hamiltonian
in \(J(n,m-1)\).

## 1. The universal point invariant

For \(k\ge1\), write \(P_k\) for point-versus-\(k\)-set incidence.  On each
Johnson edge one has the literal valuation identity

\[
 \boxed{
 P_{m-1}B_-+P_{m+1}B_+=P_mB_0.}
 \tag{1.1}
\]

Indeed, for every point \(v\) and every edge \(XY\),

\[
 \mathbf1_{v\in X\cap Y}+\mathbf1_{v\in X\cup Y}
 =\mathbf1_{v\in X}+\mathbf1_{v\in Y}.
\]

Consequently

\[
 B_+(\mathcal T_{n,m})\subseteq\ker_{\mathbb Z}P_{m+1}.
 \tag{1.2}
\]

We now prove that this necessary condition is exact over the integers.

## 2. The integer kernel of point incidence

For (2\le k\le n-2), let \(\mathcal R_{n,k}\) be the lattice generated
by the elementary rectangles

\[
 \rho(C;a,b,c,d)
 :=e_{Cbc}+e_{Cad}-e_{Cbd}-e_{Cac},
 \tag{2.1}
\]

where (|C|=k-2) and (a,b,c,d) are four distinct points outside (C).
Every such vector has zero point margin, so

\[
 \mathcal R_{n,k}\subseteq\ker_{\mathbb Z}P_k.
 \tag{2.2}
\]

### Theorem 2.1 (integral rectangle generation)

For (2\le k\le n-2),

\[
 \boxed{\mathcal R_{n,k}=\ker_{\mathbb Z}P_k.}
 \tag{2.3}
\]

#### Proof

We first prove the rank-two base.  Let integer weights (w_{ij}=w_{ji})
on the edges of (K_n) satisfy

\[
 \sum_{j\ne i}w_{ij}=0\qquad(i\in[n]).
 \tag{2.4}
\]

For every (3\le i<j\le n), subtract a suitable multiple of

\[
 e_{ij}+e_{12}-e_{i1}-e_{j2}
 \tag{2.5}
\]

to kill (w_{ij}).  These are rectangles.  The remaining vector is
supported on the edges incident with (1) or (2).  Equation (2.4) at
each (i\ge3) gives

\[
 w_{1i}=-w_{2i}=:a_i.
\]

The equations at (1) and (2) then give

\[
 w_{12}=0,\qquad \sum_{i=3}^n a_i=0.
\]

Fixing (3) as a reference, the residual vector is

\[
 \sum_{i=4}^n a_i
 \bigl(e_{1i}+e_{23}-e_{2i}-e_{13}\bigr),
 \tag{2.6}
\]

again an integral sum of rectangles.  This proves (2.3) for (k=2).

We use induction on (n).  The terminal case (n=k+2) reduces by
complementation to the rank-two case.  Explicitly, for
(z\in\ker_{\mathbb Z}P_k), first note that

\[
 k\sum_Az_A=\sum_{v=1}^n\sum_{A\ni v}z_A=0,
\]

so (sum_Az_A=0).  Put

\[
 w_B=z_{[n]\setminus B}\qquad(|B|=2).
\]

For every point (v),

\[
 \sum_{B\ni v}w_B
 =\sum_{A:v\notin A}z_A
 =\sum_Az_A-\sum_{A\ni v}z_A=0.
\]

Thus (w\in\ker_{\mathbb Z}P_2).  Complementation sends every rank-two
rectangle to a rank-(k) rectangle because (n=k+2).

Now suppose (n>k+2).  Split the coefficients of (z) according to
whether their (k)-set contains (n):

\[
 a_S:=z_{S\cup\{n\}},\qquad S\in\binom{[n-1]}{k-1}.
\]

The point-(n) equation says (sum_Sa_S=0).  The Johnson graph
(J(n-1,k-1)) is connected.  Therefore the integer zero-sum vector (a)
is an integer sum of differences (e_S-e_T) over adjacent pairs (S,T).
This last elementary fact follows, for example, by choosing a rooted
spanning tree and successively pushing each leaf's integer weight toward
the root.

Write one adjacent pair as

\[
 S=C\cup\{a\},\qquad T=C\cup\{b\},
 \qquad |C|=k-2.
\]

Because (n>k+2), choose

\[
 c\notin C\cup\{a,b,n\}.
\]

The rectangle

\[
 e_{Cna}+e_{Cbc}-e_{Cnb}-e_{Cac}
 \tag{2.7}
\]

has (n)-containing part exactly (e_S-e_T).  Subtracting the
corresponding integral sum of (2.7) from (z) kills every coefficient on
a set containing (n).  The residual vector is supported on
\(inom{[n-1]}k\) and still has zero point margins.  The induction
hypothesis finishes the proof. \(\square\)

In particular, \(\ker_{\mathbb Z}P_k\) is generated by vectors with
coefficients in \(\{-1,0,1\}\).  It is a saturated lattice: if a nonzero
integer multiple of an integral vector has zero point margin, then the
vector itself has zero point margin.

For comparison, the same conclusion over \(\mathbb Q\) has a short dual
proof.  If a function (f) on (k)-sets annihilates every rectangle,
then, for distinct (a,b), the difference

\[
 f(S\cup\{a\})-f(S\cup\{b\})
\]

is independent of the ((k-1))-set (S) disjoint from (a,b), by
connectivity of (J(n-2,k-1)).  These differences are
\(\beta_a-\beta_b\), whence

\[
 f(A)=\alpha+\sum_{i\in A}\beta_i.
\]

Thus the rectangle orthogonal complement is exactly the row space of
(P_k).  The integral proof above additionally rules out a finite-index
gap.

## 3. One five-coordinate (C_6) realizes every rectangle

Take (k=m+1), fix an ((m-1))-set (C), and choose distinct
(a,b,c,d\notin C).  Choose one point (p\in C), and put

\[
 K=C\setminus\{p\},\qquad |K|=m-2.
\]

Consider the following six middle owners, written cyclically:

\[
\begin{array}{lll}
 X_1=K\cup\{a,b\},&
 X_2=K\cup\{b,c\},&
 X_3=K\cup\{b,p\},\\
 X_4=K\cup\{p,d\},&
 X_5=K\cup\{a,p\},&
 X_6=K\cup\{a,c\}.
\end{array}
\tag{3.1}
\]

Every consecutive pair is Johnson-adjacent.  Remove the matching

\[
 E^-=\{X_1X_2,\ X_3X_4,\ X_5X_6\}
 \tag{3.2}
\]

and insert the opposite matching

\[
 E^+=\{X_2X_3,\ X_4X_5,\ X_6X_1\}.
 \tag{3.3}
\]

Let \(z=\mathbf1_{E^+}-\mathbf1_{E^-}\).  The complete ledger is

\[
\begin{array}{c|c|c|c}
\text{sign}&\text{edge}&\text{lower colour}&\text{upper colour}\\ \hline
-&X_1X_2&K b&Kabc\\
-&X_3X_4&K p&Kbpd\\
-&X_5X_6&K a&Kapc\\ \hline
+&X_2X_3&K b&Kbcp\\
+&X_4X_5&K p&Kapd\\
+&X_6X_1&K a&Kabc
\end{array}
\tag{3.3a}
\]

Here juxtaposition means union with the displayed singleton coordinates.

### Theorem 3.1 (minimal \(C_6\) rectangle packet)

The packet (3.2)--(3.3) satisfies

\[
 B_0z=0,\qquad B_-z=0,
 \tag{3.4}
\]

and

\[
 \boxed{
 B_+z=e_{Cbc}+e_{Cad}-e_{Cbd}-e_{Cac}.}
 \tag{3.5}
\]

#### Proof

Both (3.2) and (3.3) are perfect matchings on the same six owners, proving
owner neutrality.  Their lower colours, in the displayed order, are both

\[
 K\cup\{b\},\qquad K\cup\{p\},\qquad K\cup\{a\},
\]

once each.  They are pairwise distinct.

The negative upper colours are

\[
 Kabc,\qquad C\cup\{b,d\},\qquad C\cup\{a,c\},
\]

and the positive upper colours are

\[
 C\cup\{b,c\},\qquad C\cup\{a,d\},\qquad Kabc.
\]

The common colour (Kabc) cancels, leaving (3.5). \(\square\)

Combining Theorems 2.1 and 3.1 with (1.2) proves (0.2) whenever
(n\ge m+3).  If (n=m+2), then (P_{m+1}=P_{n-1}) is injective: after
indexing its columns by omitted points it is the matrix (J-I).  Hence
its kernel is zero and (0.2) follows from (1.2).  The still thinner
boundary (n=m+1) is equally trivial because there is only one upper
target.

The construction also proves that the equality is integral, rather than
only rational: every integral rectangle generator has an integral
preimage whose coefficients are \(\pm1\).

Equivalently, there is an exact sequence of free abelian groups

\[
 0\longrightarrow
 \bigl(\ker_{\mathbb Z}B_0\cap\ker_{\mathbb Z}B_-
                    \cap\ker_{\mathbb Z}B_+\bigr)
 \longrightarrow\mathcal T_{n,m}
 \mathop{\longrightarrow}^{B_+}
 \ker_{\mathbb Z}P_{m+1}
 \longrightarrow0.
 \tag{3.6}
\]

Thus every algebraic fixed-owner, fixed-lower trade is congruent, modulo a
trade neutral on all three ledgers, to an integral sum of the five-axis
\(C_6\) packets.  This is a statement about the trade module.  It does not
assert that the sum is a conformal sequence of moves legal at one fixed
lower-rainbow cycle.

When \(1\le m+1\le n-1\), the rows of \(P_{m+1}\) are rationally
independent.  Indeed, if point weights \(\alpha_i\) sum to zero on every
\((m+1)\)-set, comparison of two sets differing only in \(i,j\) gives
\(\alpha_i=\alpha_j\); their common value is then zero.  Hence

\[
 \operatorname{rank}_{\mathbb Z}
 B_+(\mathcal T_{n,m})
 =\binom n{m+1}-n.
 \tag{3.7}
\]

The total upper load is already a linear combination of the point margins,
since summing all point margins counts each upper target \(m+1\) times.
Thus (3.7) leaves exactly the \(n\) point valuations and no additional
linear invariant.

## 4. Support minimality and the exact Hamilton legality condition

Call a binary packet at a lower-rainbow graph a pair of disjoint edge sets
(E^-,E^+), with (E^-) present and (E^+) absent, such that

\[
 B_0(\mathbf1_{E^+}-\mathbf1_{E^-})=0,
 \qquad
 B_-(\mathbf1_{E^+}-\mathbf1_{E^-})=0.
 \tag{4.1}
\]

The lower colours on (E^-) are necessarily distinct.

### Theorem 4.1 (no lower-rainbow two-switch)

A nontrivial binary packet satisfying (4.1) has

\[
 |E^-|=|E^+|\ge3.
 \tag{4.2}
\]

Thus Theorem 3.1 is support-minimal.

#### Proof

Summing the owner equations gives (|E^-|=|E^+|).  One edge on each side
would have the same two endpoints and hence would be the same edge.

Suppose there were two on each side.  After cancelling common edges, owner
neutrality forces their union to be an alternating four-cycle

\[
 X_0X_1X_2X_3X_0,
\]

with (X_0X_1,X_2X_3) negative and (X_1X_2,X_3X_0) positive.

We use the following elementary observation.  If three distinct middle
sets (A,B,C) form a Johnson two-path and

\[
 A\cap B=B\cap C=S,
\]

then (A\cap C=S): the three sets are (S\cup\{a\}),
(S\cup\{b\}), and (S\cup\{c\}) with distinct extra points.

The two negative lower colours are distinct.  Equality of the negative
and positive two-element colour multisets has two possible pairings.  In
the first pairing,

\[
 L(X_0X_1)=L(X_1X_2)=S,
 \qquad
 L(X_2X_3)=L(X_3X_0)=T.
\]

The observation applied to the two opposite two-paths gives
(X_0\cap X_2=S=T), a contradiction.  In the other pairing it gives
(X_1\cap X_3=S=T), the same contradiction.  Hence no two-switch exists.
\(\square\)

The (C_6) packet is also compatible with Hamilton connectivity for an
exact, nonvacuous port pattern.  Write its six owners as (A,B,C,D,E,F)
in cyclic order, so

\[
 E^-=\{AB,CD,EF\},\qquad E^+=\{BC,DE,FA\}.
\]

If deleting (E^-) from the ambient Hamilton cycle leaves three paths
whose endpoint pairing is

\[
 \{AC,BE,DF\},
 \tag{4.3}
\]

then both

\[
 E^-\cup\{AC,BE,DF\}
 \quad\hbox{and}\quad
 E^+\cup\{AC,BE,DF\}
\]

are single alternating six-cycles on the path quotient.  Therefore the
replacement preserves one Hamilton cycle.  Condition (4.3) is an exact
eligibility condition, not a theorem that every lower-rainbow cycle
contains such an occurrence.

For completeness, five active coordinates are also minimal for a legal
lower-rainbow packet with nonzero upper action.  If all involved owners lie
over at most four active coordinates, let (s) be their local rank.

* For (s=1), every local edge has the same lower colour, so a
  lower-rainbow state cannot contain the at least three negative edges.
* For (s=3), every local edge has the same upper colour, and owner
  neutrality forces total signed edge count zero.
* For (s=2), write a local edge in (J(4,2)) as (z_{ij}), where (i)
  is its singleton lower colour and (j) is the unique omitted point of
  its triple upper colour.  Lower neutrality says every row sum is zero.
  The owner equation at the pair ({a,b}), together with the row
  equations, gives (z_{ab}+z_{ba}=0).  Hence (z) is skew-symmetric,
  so every column sum, which is an upper-colour coefficient, is zero.

The packet (3.1)--(3.3) uses exactly the five active points
(p,a,b,c,d), so it attains this bound.

## 5. Exact change in upper repeat defect

Let (u(U)) be the current upper load and

\[
 R^+(u)=\sum_{U\in\mathcal U}(u(U)-1)_+.
\]

For the forward (C_6) packet, put

\[
 A=\{Cbc,Cad\},\qquad D=\{Cbd,Cac\}.
\]

The four targets are distinct.  Removing one occurrence decreases repeat
excess precisely when its old load is at least two; adding one occurrence
increases repeat excess precisely when its old load is at least one.
Therefore

\[
 \boxed{
 \Delta R^+
 =\mathbf1_{u(Cbc)\ge1}+\mathbf1_{u(Cad)\ge1}
  -\mathbf1_{u(Cbd)\ge2}-\mathbf1_{u(Cac)\ge2}.}
 \tag{5.1}
\]

Thus one eligible packet can decrease the upper defect by two.  In
particular, union multiplicities are genuinely mobile under
intersection-complete, owner-fixed trades.  Reversal of a cycle has zero
edge action, while complementation gives the dual packet which preserves
upper colours and performs a lower rectangle.

The four targets in (5.1) have Johnson diameter at most two.  Consequently
this minimal library still has the familiar local lock: if every repeated
upper target is at Johnson distance at least three from every upper hole,
neither orientation of an eligible (C_6) can strictly descend.  The
complete lattice theorem does not imply a statewise descent theorem.

## 6. Exact lower-to-upper algebraic criterion

Let (C_0) now be a lower-colour-complete cycle, and write (x) for its
edge indicator, (v) for its selected-owner indicator, and

\[
 u=B_+x.
\]

Then

\[
 B_-x=\mathbf1_{\mathcal L},\qquad
 B_0x=2v,
\]

so (1.1) gives

\[
 \boxed{
 P_{m+1}u=2P_mv-P_{m-1}\mathbf1_{\mathcal L}.}
 \tag{6.1}
\]

Let (b\in\mathbb Z^{\mathcal U}) be any proposed upper histogram.  By
(0.2), there exists an integral fixed-owner, fixed-lower signed trade
(z) with

\[
 B_+z=b-u
\]

if and only if

\[
 \boxed{
 P_{m+1}b=2P_mv-P_{m-1}\mathbf1_{\mathcal L}.}
 \tag{6.2}
\]

This is the promised complete linear and integral characterization.

On even ground (n=2m), one has

\[
 |\mathcal U|=|\mathcal L|=:N_-.
\]

Taking (b=\mathbf1_{\mathcal U}) in (6.2), and using

\[
 P_{m-1}\mathbf1_{\mathcal L}
 +P_{m+1}\mathbf1_{\mathcal U}=N_-\mathbf1_{[2m]},
\]

gives the exact criterion

\[
 \boxed{
 b=\mathbf1_{\mathcal U}\text{ is algebraically reachable}
 \iff
 (P_mv)_q=N_-/2\quad(q\in[2m]).}
 \tag{6.3}
\]

Thus point balance is both necessary and sufficient at the integral trade
module level.  On odd ground an injective upper histogram is a
(0/1)-vector (b) of mass (N_-), and (6.2) is its exact algebraic
feasibility test.

In particular, if \(N_-\) is odd, (6.3) is impossible.  This recovers the
exact parity obstruction to a fixed-owner two-sided cycle.  When \(N_-\)
is even, parity disappears and (6.3) says that there is no further
additive or lattice obstruction; conformal eligibility is then the whole
remaining switch-space issue.

## 7. Proved boundary

The following statements are now exact.

1. Point margins are the only additive invariants of upper histograms
   under arbitrary integral fixed-owner, fixed-lower Johnson trades.
2. The image lattice is saturated; fractional or rational feasibility
   introduces no additional lattice obstruction.
3. A five-coordinate alternating (C_6) is the smallest binary packet
   that can occur in a lower-rainbow state and change the upper histogram.
4. Its upper action and its repeat-defect change are given exactly by
   (3.5) and (5.1).

What remains unproved is nonlinear and state-dependent: a given
lower-colour-complete Hamilton cycle need not contain the three negative
edges with the quotient pairing (4.3), a sum of rectangle preimages need
not stay binary at intermediate stages, and connectivity need not persist.
Therefore this theorem does not construct a two-sided cycle and does not
claim coefficient one.  It reduces the exact (q=1) upgrade to an
eligibility/connectivity problem for a support-minimal (C_6) rectangle
atlas, with no residual linear or integer-lattice ambiguity.
