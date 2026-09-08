# Actual one-bite residuals and horizontal rotor expansion

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Outcome and scope

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad M=m+H,
 \qquad N=\binom{2m}{M},
\tag{0.1}
\]

and work at the calibrated crossing

\[
 \rho:=\frac{MN}{W}=1-o(1),\qquad Q=o(H),\qquad H=o(m).
\tag{0.2}
\]

This note analyzes the residual left by one rigorous owner-scale bite from
`MATH_ATTACK_LADDER_PRIORITY_OWNER_SCALE_NIBBLE_20260725.md`.  Suppose the
bite selects exactly (k) carrier trajectories.  Write

\[
 F\subseteq\binom{[2m]}m
\tag{0.3}
\]

for their middle-owner support.  Since every trajectory has (M) distinct
owners and the selected trajectories are owner-disjoint,

\[
 \boxed{|F|=kM.}
\tag{0.4}
\]

For the proved bite, (k=\Theta(N/M)), after discarding surplus selected
paths if necessary.  Thus

\[
 |F|=\Theta(N)=\Theta(W/M).
\tag{0.5}
\]

There are five conclusions.

1. The protected/catalogue middle-hole antichain after one bite has exact
   size \(W-kM=W-o(W)\).  If the bite paths are already compiled, let
   \(r_{\rm init}\) be their nonphase initialization/seam ledger.  Their
   physical literal middle-hole family still has size at least
   \(W-kM-r_{\rm init}\); under the standard compilation
   \(r_{\rm init}\le(2Q+1)k=o(W)\).  Therefore an appended repair made of
   \(O(Q)\)-phase blocks cannot be coefficient-safe: it needs
   \(\Omega(W/Q)\) blocks and \(W-o(W)\) new state positions.
2. There is nevertheless an exact positive statement about the complete
   protected residual, not merely about collision donors.  Fix any
   symmetric chain decomposition of the Boolean lattice.  After setting
   aside at most

   \[
   \boxed{2QkM=o(W)}
   \tag{0.6}
   \]

   protected residual masks, all remaining protected holes are covered by
   exactly (W-kM) inclusion chains.  This number is best possible because
   the retained family contains all (W-kM) middle holes.
3. On the complete radius-(Q) state reservoir there is a sharp additive
   successor-Hall theorem.  If (b) state columns are forbidden, the
   induced good-state rotor graph has matching deficiency at most (b).
   Its directed girth is at least (2Q+2).  Consequently all good state
   columns have a literal path cover with at most

   \[
   \frac{|G|}{2Q+2}
   +\left(1-\frac1{2Q+2}\right)b
   \tag{0.7}
   \]

   paths, and a cover by blocks of at most (2Q+2) phases with at most

   \[
   \boxed{b+\left\lceil\frac{|G|}{Q+1}\right\rceil}
   \tag{0.8}
   \]

   blocks.
4. Applied only to used middle owners, the forbidden state density is
   (kM/W=O(1/M)=o(1/Q)).  Hence the complete residual-owner state
   reservoir has an integral literal (O(Q))-phase block cover of the
   correct order (O(|G|/Q)).  Applied instead to columns required to avoid
   every already claimed protected row, the direct density estimate is
   (O(Q/M)).  At the calibrated value (Q^2/M\sim\log\log m), (0.8)
   then loses a factor of order (1+Q^2/M).  The row-density argument alone
   does not give (O(|G|/Q)) blocks in this stronger all-row sense.
5. The positive full-reservoir theorem does not yet select one state column
   for each of the (W-kM) chains in item 2.  A thin balanced table can have
   no rotor edge at all.  The exact remaining gate is therefore an
   **integral SCD--rotor thinning theorem**, not another donor-width or
   average-degree estimate.

### Protected residuals versus literal holes

For each signed protected row (r\in\{-Q,\ldots,Q\}), let (Z_r) be the
family of targets certified as claimed by the bite, and put

\[
 \mathcal H_r=\binom{[2m]}{m+r}\setminus Z_r.
\tag{0.9}
\]

The family (\mathcal H_r) is the **protected residual**.  At nonmiddle
ranks it may contain masks which happened to be emitted at unclaimed
phases of the literal bite word.  Hence it is generally a superset of the
literal holes of that word.  At the middle rank the selected trajectory
phases give the exact catalogue identity

\[
 \mathcal H_0=\binom{[2m]}m\setminus F
\tag{0.10}
\]

for the complement of the selected phase owners.  A compiled
initialization or seam can incidentally expose further middle masks.  If
there are \(r_{\rm init}\) such extra state positions, the physical literal
middle-hole family \(\mathcal L_0\) satisfies

\[
 |\mathcal L_0|\ge W-kM-r_{\rm init}.
\tag{0.11}
\]

For the standard independent path compilation,

\[
 r_{\rm init}\le(2Q+1)k=o(W).
\tag{0.12}
\]

Thus the exact protected middle identity and the physical literal lower
bound have the same \(W-o(W)\) scale.  Positive covers below are proved for
the larger protected residual and therefore also cover the literal holes.

### Lemma 0.1 (one mask of each rank per word endpoint)

Fix a right endpoint \(t\) in a literal OR word.  The ORs of intervals
ending at \(t\), as the left endpoint moves left, form an inclusion chain.
Consequently at most one distinct interval OR ending at \(t\) has any
prescribed cardinality.

In particular, \(L\) new word positions can expose at most \(L\) new masks
in each fixed rank, including the middle rank.

#### Proof

If \(s'<s\le t\), the interval \([s,t]\) is contained in \([s',t]\), so
its OR mask is contained in the latter OR mask.  Two comparable finite
sets of equal cardinality are equal.  Assign every interval to its right
endpoint and sum over endpoints. \(\square\)

Lemma 0.1 is the literal justification for (0.11), (0.12), (1.6e), and
the physical-support estimate (4.9).

## 1. Exact actual-hole condensation after one bite

We use the standard exact symmetric chain decomposition of the Boolean
lattice (2^{[2m]}).  Its existence is a frozen input.  Every symmetric
chain contains exactly one rank-(m) set, so the decomposition has exactly
(W) chains.

### Theorem 1.1 (one-bite SCD condensation)

Let (\mathcal H=\bigcup_{r=-Q}^Q\mathcal H_r) be the protected residual
after a bite with owner set (F), (|F|=kM).  There is a subfamily
(E\subseteq\mathcal H) satisfying

\[
 \boxed{|E|\le 2QkM}
\tag{1.1}
\]

such that (\mathcal H\setminus E) has an inclusion-chain cover of exact
cardinality

\[
 \boxed{W-kM.}
\tag{1.2}
\]

In particular, for an owner-scale bite (k=O(N/M)),

\[
 |E|=O(QN)=O(WQ/M)=o(W).
\tag{1.3}
\]

#### Proof

Fix a symmetric chain decomposition (\mathscr D).  Delete from it the
(|F|=kM) chains whose unique middle members lie in (F).  Let (E) be
the protected residual masks in the controlled band which lie on one of
these deleted chains.

The middle member of a deleted chain belongs to (F=Z_0), so it is not a
residual hole.  A chain has at most one member in every rank and there are
only (2Q) nonmiddle controlled ranks.  Hence each deleted chain
contributes at most (2Q) members to (E), proving (1.1).

Every member of (\mathcal H\setminus E) lies on one of the remaining
(W-kM) SCD chains.  Intersecting those chains with
(\mathcal H\setminus E) gives a chain cover with at most (W-kM) chains.
On the other hand, all (W-kM) middle sets outside (F) belong to
(\mathcal H\setminus E), and they form an antichain.  Every chain cover
therefore has at least (W-kM) chains.  This proves (1.2).

Finally, (k=O(N/M)) gives (kM=O(N)), and (0.2) gives
(QN=\rho WQ/M=o(W)).  This proves (1.3). \(\square\)

The theorem concerns the actual complement target families (\mathcal H_r),
not the locations of duplicate or withheld donor claims.

### Corollary 1.2 (sharp one-bite width scale)

The complete protected residual satisfies

\[
 \operatorname{width}(\mathcal H)\ge W-kM.
\tag{1.4}
\]

After the (o(W)) exceptions in Theorem 1.1, equality holds:

\[
 \operatorname{width}(\mathcal H\setminus E)=W-kM.
\tag{1.5}
\]

For (k=\Theta(N/M)),

\[
 W-kM=W-\Theta(N)=W\left(1-\Theta(1/M)\right)=W-o(W).
\tag{1.6}
\]

If the bite has already been compiled with \(r_{\rm init}\) nonphase state
positions, its physical literal hole poset \(\mathcal L\) obeys

\[
 \boxed{\operatorname{width}(\mathcal L)
 \ge |\mathcal L_0|
 \ge W-kM-r_{\rm init}=W-o(W).}
\tag{1.6a}
\]

### Theorem 1.2a (physical literal SCD condensation)

Let \(F_{\rm lit}\subseteq\binom{[2m]}m\) be the family of **all distinct
middle masks physically exposed** by the already compiled bite, including
trajectory, initialization, and seam positions, and put

\[
 f:=|F_{\rm lit}|.
\tag{1.6b}
\]

Let \(\mathcal L\) be the literal hole poset in the controlled band.  There
is \(E_{\rm lit}\subseteq\mathcal L\) such that

\[
 \boxed{|E_{\rm lit}|\le2Qf}
\tag{1.6c}
\]

and

\[
 \boxed{\operatorname{width}
   (\mathcal L\setminus E_{\rm lit})
 =\text{minimum chain-cover number}
 =W-f.}
\tag{1.6d}
\]

Under the standard one-bite compilation,

\[
 kM\le f\le kM+r_{\rm init}=O(N),
\qquad |E_{\rm lit}|=O(QN)=o(W).
\tag{1.6e}
\]

#### Proof

Fix the same SCD as in Theorem 1.1 and delete the \(f\) chains whose middle
members belong to \(F_{\rm lit}\).  Let \(E_{\rm lit}\) be the literal holes
on those deleted chains.  The middle member of every deleted chain is
physically covered and hence is not a literal hole.  There are only \(2Q\)
controlled nonmiddle ranks, proving (1.6c).

Every remaining literal hole lies on one of the \(W-f\) retained SCD
chains.  Conversely, the \(W-f\) middle masks outside \(F_{\rm lit}\) are
literal holes and form an antichain.  Hence both the width and the minimum
chain-cover number are exactly \(W-f\), proving (1.6d).

The \(kM\) selected phase owners are distinct and physically exposed, so
\(f\ge kM\).  At most one new middle mask is exposed per additional word
position, giving \(f\le kM+r_{\rm init}\).  Now use
\(kM=O(N)\), \(r_{\rm init}=o(N)\), and \(QN=o(W)\). \(\square\)

### Corollary 1.2b (the exceptional SCD chains are already cheap)

The protected exception family \(E\) in Theorem 1.1 has an integral
literal repair of length at most

\[
 \boxed{(2Q+2)kM=o(W).}
\tag{1.6f}
\]

The physical exception family \(E_{\rm lit}\) in Theorem 1.2a has one of
length at most

\[
 \boxed{(2Q+2)f=o(W).}
\tag{1.6g}
\]

#### Proof

On every deleted SCD chain, extend its controlled-band intersection to one
saturated radius-\(Q\) state column.  That one column covers every
exceptional mask on the chain.  Initialize it independently; the buffered
one-state path has length \(1+(2Q+1)=2Q+2\).  Sum over the \(kM\), or
respectively \(f\), deleted chains and use \(QkM,Qf=o(W)\). \(\square\)

Thus exceptional-chain patching is closed.  It is not part of the main
horizontal thinning gate.

### Corollary 1.3 (short appended blocks are not coefficient-safe here)

Suppose an appended **phase-block cover** assigns every physical literal
middle hole, apart from \(e=o(W)\) literal exceptions, to a designated
state column in one of \(S\) blocks, each having at most \(L\le CQ\)
designated state columns.  Initialization positions are not credited as
additional unlisted cover cells in this strengthened statement.  With
\(f=|F_{\rm lit}|\) from Theorem 1.2a,

\[
 \boxed{S\ge\frac{W-f-e}{L}
       \ge (1-o(1))\frac{W}{CQ}.}
\tag{1.7}
\]

Moreover, the blocks contain at least \(W-f-e=W-o(W)\) designated state
positions.  In the buffered full-state convention used in the present
path ledger, a cover with \(B\) state columns and \(S\) paths has length

\[
 B+(2Q+1)S.
\tag{1.8}
\]

A direct hard-reset convention can save one position per path and has
ledger \(B+2QS\).  Consequently, even using this shorter convention, if
all paths have at most \(CQ\) state columns, the compiled length is at
least

\[
 \boxed{
 (W-f-e)+2Q
 \left\lceil\frac{W-f-e}{CQ}\right\rceil
 \ge\left(1+\frac2C-o(1)\right)W.}
\tag{1.9}
\]

Thus bounded-(CQ)-length blocks cannot be appended at (o(W)) cost and
cannot themselves compile the one-bite residual at coefficient one.

#### Proof

One state column has one middle owner and hence covers at most one of the
distinct middle holes.  Theorem 1.2a gives exactly \(W-f\) physical
middle holes.  Count those holes over the blocks and exceptions.
This gives (1.7), and the same count gives the state-position lower bound.
Substitution into the shorter direct-reset ledger \(B+2QS\) gives (1.9);
the buffered ledger (1.8) is one position longer per path.
\(\square\)

Without the designated-cell convention, initialization or seam positions
may themselves witness further middle holes.  The unconditional statement
for blocks with at most \(L\) designated phases is

\[
 \boxed{
 S\ge
 \frac{W-f-e}{L+2Q+1}
 \ge(1-o(1))\frac{W}{(C+2)Q}}
\tag{1.10}
\]

when \(L\le CQ\), because one buffered block has at most \(L+2Q+1\)
literal endpoints and Lemma 0.1 permits at most one middle mask per
endpoint.  More fundamentally,

\[
 \boxed{\text{appended literal length}\ge
 W-f-e=W-o(W),}
\tag{1.11}
\]

because a word position supplies at most one new length-\(m\) interval.
Thus arbitrary reset contamination can invalidate the extra \(2/C\) in
(1.9), but it cannot turn this one-bite residual into an \(o(W)\)-cost
appended reserve.

Therefore an (O(Q))-phase theorem at the one-bite scale can contribute to
coefficient one only if its state positions replace the corresponding
baseline segment.  It cannot be used as a separate sparse reserve.

## 2. The exact global saturated-column rotor graph

Put

\[
 \ell=m-Q.
\tag{2.1}
\]

A global radius-(Q) state column is a saturated chain

\[
 S=(S_0\subset S_1\subset\cdots\subset S_{2Q}),
 \qquad |S_h|=\ell+h.
\tag{2.2}
\]

Write

\[
 S_h=L\cup\{z_1,\ldots,z_h\},
 \qquad |L|=\ell,
\tag{2.3}
\]

and let the full residual block be

\[
 R=[2m]\setminus S_{2Q},\qquad |R|=\ell.
\tag{2.4}
\]

Thus the number of global columns is

\[
 V:=|\mathscr S_Q|=\frac{(2m)!}{(\ell!)^2}.
\tag{2.5}
\]

### Theorem 2.1 (exact global successor criterion)

For two saturated columns (S,T\in\mathscr S_Q), there is a literal rotor
edge (S\to T) if and only if there are

\[
 x\in S_0,\qquad y\notin S_{2Q}
\tag{2.6}
\]

such that

\[
 \boxed{T_0=S_0-x+y,}
\tag{2.7}
\]

and

\[
 \boxed{T_h=S_{h-1}+y\qquad(1\le h\le2Q).}
\tag{2.8}
\]

The directed graph on (\mathscr S_Q) is

\[
 \boxed{D_\star\text{-in/out regular},\qquad D_\star=\ell^2=(m-Q)^2.}
\tag{2.9}
\]

#### Proof

The rotor update is

\[
 (L;z_1,\ldots,z_{2Q};R)
 \longmapsto
 (L-x+y;x,z_1,\ldots,z_{2Q-1};R-y+z_{2Q}).
\tag{2.10}
\]

Its bottom flag is (2.7).  For (h\ge1), its rank-((\ell+h)) flag is

\[
 (L-x+y)+\{x,z_1,\ldots,z_{h-1}\}
 =S_{h-1}+y,
\]

which proves necessity and sufficiency of (2.7)--(2.8).

There are (\ell) choices for (x) and (\ell) choices for (y), and
distinct pairs give distinct target columns.  For the reverse count, write

\[
 T_h=L'\cup\{w_1,\ldots,w_h\}.
\]

Choose the old arrival (y\in L') and the old last queue label
(v\notin T_{2Q}).  Then the predecessor is forced:

\[
 L=L'-y+w_1,
\]

its first (2Q-1) queue labels are (w_2,\ldots,w_{2Q}), and its last
queue label is (v).  Again there are (\ell^2) choices.  This proves
(2.9). \(\square\)

### Fixed-carrier specialization

If a carrier (U\) of size (M) is fixed, then the arrival must lie in
(U\setminus S_{2Q}), of size (H-Q).  The fixed-carrier graph is

\[
 (m-Q)(H-Q)\text{-in/out regular}.
\tag{2.11}
\]

The global criterion is physically legitimate: the complete full MTF
state has residual block ([2m]\setminus S_{2Q}).  Restricting arrivals to
one top is an additional architectural condition, not a condition for a
literal MTF edge.

A path supplied by the global graph may change the inferred \(M\)-top from
one edge to the next.  It is therefore a literal trajectory in the full
\([2m]\) MTF state space, but not necessarily a trajectory inside one
fixed truncated top fibre.  Charging such a path to one reserve top tag
would require an additional host/portal theorem.  All fixed-top claims in
this report use the specialization (2.11), not the global degree
\((m-Q)^2\).

## 3. Exact grid-strip form of the successor

For a return-free geodesic grid, write

\[
 G_{i,j}
 =C\cup\{a_{i+1},\ldots,a_g\}
    \cup\{b_1,\ldots,b_j\}.
\tag{3.1}
\]

For an interior phase

\[
 Q\le t\le g-Q-1,
\tag{3.1a}
\]

so that the complete current queue, the exchange label, and the
phase-\((t+1)\) state are all defined, its quotient state is

\[
 L_t=G_{t+Q,t},
 \qquad z_{t,s}=a_{t+Q-s+1}\quad(1\le s\le2Q).
\tag{3.2}
\]

The canonical transition choices are

\[
 x_t=a_{t+Q+1},\qquad y_t=b_{t+1}.
\tag{3.3}
\]

They give the phase-((t+1)) state.

For an arbitrary legal arrival (y) from the current residual block, the
arrival-controlled bases are

\[
 B_0(t)=G_{t+1,t},
\tag{3.4}
\]

\[
 B_{-q}(t)=G_{t+q+1,t}\qquad(1\le q<Q),
\tag{3.5}
\]

and

\[
 B_{+q}(t)=G_{t-q+1,t}\qquad(1\le q\le Q).
\tag{3.6}
\]

The successor flags are

\[
 X'=B_0(t)+y,qquad
 L'_q=B_{-q}(t)+y,qquad
 U'_q=B_{+q}(t)+y,
\tag{3.7}
\]

while the deepest lower flag is

\[
 L'_Q=G_{t+Q,t}-x+y.
\tag{3.8}
\]

Equations (3.4)--(3.8) are just Theorem 2.1 expressed in the two-chain
grid coordinates.  For the canonical choices (3.3), they become

\[
 G_{t+q+1,t+1},\quad G_{t-q+1,t+1},
\]

which are exactly the phase-((t+1)) lower and upper strip flags.

### Corollary 3.1 (exact forbidden-successor degree)

Let (Z_r) be forbidden target families in the protected rows.  For a
state (\omega), let (Y(\omega)) be the arrivals (y) for which at least
one arrival-controlled target in (3.7) belongs to its (Z_r).  Then the
number of all-row-good fixed-carrier successors is exactly

\[
 \boxed{
 (m-Q)\bigl(H-Q-|Y(\omega)|\bigr)
 -\#\{(x,y):y\notin Y(\omega),\ L-x+y\in Z_{-Q}\}.}
\tag{3.9}
\]

For the global graph, replace (H-Q) by (m-Q).  No independence or
uniformity assumption is present in (3.9).

## 4. Exact bad-state density after one bite

For signed rank (r\in\{-Q,\ldots,Q\}), let

\[
 \Phi_r(S)=S_{Q+r}.
\tag{4.1}
\]

Given target families (Z_r), call a column bad when

\[
 \Phi_r(S)\in Z_r
\]

for at least one (r).  Let (B\subseteq\mathscr S_Q) be the bad set and
put (b=|B|).

### Proposition 4.1 (exact row-density average)

Put

\[
 \eta=\sum_{r=-Q}^Q
 \frac{|Z_r|}{\binom{2m}{m+r}}.
\tag{4.2}
\]

Then

\[
 \boxed{b\le \eta V.}
\tag{4.3}
\]

Moreover, among all (D_\star V) directed rotor edges, the proportion
whose destination is bad is exactly (b/V), and hence at most (\eta).

#### Proof

The coordinate group is transitive on the rank-((m+r)) targets and on
the saturated state columns.  Therefore every target in row (r) occurs
as (\Phi_r(S)) in exactly

\[
 \frac{V}{\binom{2m}{m+r}}
\]

state columns.  Sum this count over (Z_r) and then use the union bound
over the rows to prove (4.3).

Every state has indegree (D_\star), so exactly (D_\star b) edges have
their destination in (B).  Divide by (D_\star V). \(\square\)

### Fixed-carrier form

Let

\[
 V_U=\frac{M!}{(m-Q)!(H-Q)!}
\tag{4.3a}
\]

be the number of states over one top \(U\), and let \(b_U\) be the number
whose displayed column meets a claimed family.  Then

\[
 \boxed{
 \frac{b_U}{V_U}
 \le
 \eta_U:=
 \sum_{r=-Q}^Q
 \frac{|Z_r\cap\binom{U}{m+r}|}{\binom{M}{m+r}}.}
\tag{4.3b}
\]

The binomial identity

\[
 \binom{2m}{m+r}
 \binom{2m-m-r}{M-m-r}
 =
 \binom{2m}{M}\binom{M}{m+r}
\tag{4.3c}
\]

gives the exact average

\[
 \boxed{\frac1N\sum_{U}\eta_U=\eta.}
\tag{4.3d}
\]

The fixed-carrier rotor graph is \((m-Q)(H-Q)\)-regular.  Therefore, for
every set \(A\) of good fixed-carrier states,

\[
 |N^+_{G_U}(A)|\ge |A|-b_U.
\tag{4.3e}
\]

The girth and matching-to-path arguments in Section 5 apply without
change.  This is the exact per-carrier Hall ratio; only its average over
tops is controlled by the global row densities.

### Corollary 4.2 (one-bite constants)

For a bite of (k) trajectories, the proved common-priority matching has

\[
 |Z_0|=kM,
 \qquad |Z_{-q}|=|Z_{+q}|=k\bar c_q,
\tag{4.4}
\]

where

\[
 \bar c_q\le c_q\le \frac{R_q}{N},
 \qquad R_q=\binom{2m}{m-q}.
\tag{4.5}
\]

Consequently

\[
 \boxed{
 \eta
 \le \frac{kM}{W}+\frac{2Qk}{N}
 =\frac{k}{N}(\rho+2Q).}
\tag{4.6}
\]

If (k\le C N/M), then

\[
 \eta\le C\frac{2Q+\rho}{M}=O(Q/M)=o(1).
\tag{4.7}
\]

If only used owners are forbidden, then no union bound is needed.  The
bad set

\[
 B_0=\{S:\Phi_0(S)\in F\}
\]

has the exact density

\[
 \boxed{\frac{|B_0|}{V}=\frac{|F|}{W}=\frac{kM}{W}
 =\rho\frac{k}{N}.}
\tag{4.8}
\]

For (k=O(N/M)), this is (O(1/M)=o(1/Q)).

### Physical-support warning

Equations (4.4)--(4.7) concern the certified claimed families \(Z_r\).
They do not count every mask incidentally emitted at an unclaimed phase or
initialization position of the literal bite word.  If
\(Z_r^{\rm lit}\) denotes the complete distinct physical support in row
\(r\), then the elementary position count gives

\[
 |Z_r^{\rm lit}|\le kM+r_{\rm init}
 \qquad(-Q\le r\le Q).
\tag{4.9}
\]

Consequently Proposition 4.1 gives the different bound

\[
 \boxed{\eta_{\rm lit}
 \le \frac{kM+r_{\rm init}}{W}
       \bigl(1+2\Lambda_Q\bigr),\qquad
 \Lambda_Q=\sum_{q=1}^Q\lambda_q.}
\tag{4.10}
\]

Thus claimed-target cleanliness and complete physical-support cleanliness
are different requirements.  The owner-only theorem remains at density
\(O(1/M)\), up to the additional \(r_{\rm init}/W=o(1/Q)\), because every
position contributes only one middle owner.

## 5. Additive Hall, directed girth, and a literal block cover

Let (G=\mathscr S_Q\setminus B), where (B) is any forbidden state set.
Use left and right copies of (G), with the rotor edges induced from the
full graph.

### Theorem 5.1 (deleted-state successor Hall)

For every (A\subseteq G),

\[
 \boxed{|N_G^+(A)|\ge |A|-b.}
\tag{5.1}
\]

Equivalently, the maximum matching deficiency of the induced successor
graph on (G) is at most (b).

#### Proof

The full rotor bipartite graph is (D_\star)-regular, so Hall gives

\[
 |N_{\mathscr S_Q}^+(A)|\ge|A|.
\]

Passing to the good right class deletes at most the (b) vertices in
(B).  This proves (5.1). \(\square\)

### Lemma 5.2 (exact directed girth lower bound)

Every directed rotor cycle has length at least

\[
 \boxed{2Q+2.}
\tag{5.2}
\]

#### Proof

Consider a coordinate (x) selected from the lower block on the first
edge of a purported cycle.  After that edge it occupies queue position
one.  After (s\) moves, (1\le s\le2Q), it occupies queue position (s).
On move (2Q+1) it is ejected from the last queue position into the
residual block.  Since the arrival is chosen before that ejection, (x)
cannot be selected as an arrival on the same move.  The earliest it can be
selected from the residual block is move (2Q+2), after which it returns
to the lower block.  Before then the lower block cannot equal its initial
lower block.  Hence the state cannot recur in at most (2Q+1) moves.
\(\square\)

### Theorem 5.3 (full-reservoir literal path and block cover)

The good state set (G) has a vertex-disjoint cover by literal directed
rotor paths with at most

\[
 \boxed{
 \frac{|G|}{2Q+2}
 +\left(1-\frac1{2Q+2}\right)b}
\tag{5.3}
\]

components.  It has a cover by literal directed blocks of at most
(2Q+2) state columns with at most

\[
 \boxed{b+\left\lceil\frac{|G|}{Q+1}\right\rceil}
\tag{5.4}
\]

blocks.

#### Proof

Take a maximum matching in the bipartite successor graph on (G), and
identify the two copies of every state.  The resulting directed graph has
indegree and outdegree at most one.  Its components are directed paths,
isolated vertices, and directed cycles.

The number of path components, with isolated vertices included, is

\[
 |G|-|P|,
\]

the matching deficiency; call it \(d\le b\).  Those \(d\) path components
use at least \(d\) vertices.  By Lemma 5.2 every cycle component contains
at least \(g=2Q+2\) vertices, so there are at most
\((|G|-d)/g\) cycle components.  Cut one edge in every cycle.  The number
of resulting paths is at most

\[
 d+\frac{|G|-d}{g}
 =\frac{|G|}{g}+\left(1-\frac1g\right)d
 \le\frac{|G|}{g}+\left(1-\frac1g\right)b,
\]

which proves (5.3).

Now split every resulting path into consecutive pieces of at most
(g=2Q+2) vertices.  If there are (p) paths with vertex counts (v_i),
then

\[
 \sum_i\left\lceil\frac{v_i}{g}\right\rceil
 \le \frac{|G|}{g}+\left(1-\frac1g\right)p.
\tag{5.5}
\]

Insert (5.3) into (5.5).  The result is strictly below

\[
 b+\frac{2|G|}{2Q+2}=b+\frac{|G|}{Q+1},
\]

up to the final integer rounding, proving (5.4).  Every selected edge is
an actual rotor update, so all blocks preserve literal chronology.
\(\square\)

### Corollary 5.4 (positive owner-only horizontal expansion)

Delete precisely the state columns whose owner belongs to the complete
physically exposed owner set \(F_{\rm lit}\), of size \(f\).  Then the
complete literal-residual-owner state reservoir has a literal
block cover satisfying

\[
 \boxed{
 S\le \frac{f}{W}V
 +\left\lceil\frac{V}{Q+1}\right\rceil.}
\tag{5.6}
\]

For \(k=O(N/M)\) and \(r_{\rm init}\le(2Q+1)k\), Theorem 1.2a gives
\(f=O(N)\), and therefore

\[
 \boxed{S=O(V/Q),}
\tag{5.7}
\]

and in fact the first term in (5.6) is (o(V/Q)).

If only the certified phase-owner set \(F\) is forbidden, replace \(f\) by
\(kM\); then (4.8) is exact.

This is an integral block theorem.  It is not a fractional stationary
flow: the matching in Theorem 5.3 selects literal rotor edges, and the
cycle cuts produce literal paths.

### Corollary 5.5 (the all-row density loss)

If a state column is declared bad whenever any of its protected flags was
already claimed in the bite, then

\[
 S
 \le
 V\left(
 \frac1{Q+1}+\frac{k}{N}(\rho+2Q)
 \right)+1.
\tag{5.8}
\]

For (k=\Theta(N/M)), this is

\[
 S
 \le
 O\left(\frac{V}{Q}\left(1+\frac{Q^2}{M}\right)\right).
\tag{5.9}
\]

At the current calibration

\[
 \frac{Q^2}{M}=(1+o(1))(\log\log m+\gamma(m)),
\tag{5.10}
\]

so (5.9) retains a growing (\log\log m)-scale loss.  This is a limitation
of the direct row-density/union estimate.  It is not a proof that a more
correlated all-row block selection is impossible.

## 6. Exact occurrence-level grid-strip cover

The grid formulas give a second version which retains a prescribed
canonical chronology rather than rebuilding it by matching.

### Theorem 6.1 (balanced-strip deletion and block count)

Let (\mathscr P) be a finite multiset of literal linear grid strips,
with (T) total phase occurrences and (P) strips.  Assume its owner
occurrence multiset is exactly (\mu)-regular on the middle layer, so

\[
 T=\mu W.
\tag{6.1}
\]

Delete every phase whose owner belongs to (F).  The remaining phase
occurrences admit a literal chronological cover by blocks of at most
(L) phases with

\[
 \boxed{S\le \frac{T}{L}+P+\mu|F|.}
\tag{6.2}
\]

If every strip has length at least (g), then

\[
 \boxed{
 \frac ST\le\frac1L+\frac1g+\frac{|F|}{W}.}
\tag{6.3}
\]

#### Proof

Exact owner regularity says that the number of deleted phase occurrences
is exactly (\mu|F|).  Deleting (d) positions from one linear strip
leaves at most (d+1) chronological runs.  Summing over strips gives at
most (P+\mu|F|) runs.

Split each run into consecutive pieces of at most (L) phases.  The
number of pieces is at most the number of retained phases divided by
(L), plus the number of runs.  This proves (6.2).  If every strip has
length at least (g), then (P\le T/g); use (6.1) to obtain (6.3).
\(\square\)

A complete coordinate orbit of any fixed grid-strip template is exactly
owner-regular, by transitivity.  For the physical residual take
\(F=F_{\rm lit}\); Theorem 1.2a gives \(|F|/W=O(1/M)\).  Taking

\[
 L=2Q+2,qquad g\asymp H,qquad |F|/W=O(1/M)
\]

in (6.3) gives

\[
 S\ge\frac{T-\mu|F|}{2Q+2}
 =\left(1-O(1/M)\right)\frac{T}{2Q+2},
\tag{6.3a}
\]

because every block has at most \(2Q+2\) retained phases.  Together with
(6.3), \(Q=o(H)\), and \(|F|/W=O(1/M)\), this yields

\[
 \boxed{S=(1+o(1))\frac{T}{2Q+2}.}
\tag{6.4}
\]

Every block in (6.4) follows the canonical grid successor (3.3), so no
abstract transition must be literalized later.

If phases are instead deleted whenever any displayed row lies in its
claimed family (Z_r), a row-balanced coordinate orbit and Proposition
4.1 give the analogous estimate

\[
 \frac ST\le\frac1L+\frac1g+\eta.
\tag{6.5}
\]

At (L\asymp Q), (6.5) has the same (Q^2/M) loss as Corollary 5.5.

## 7. Why the positive reservoir theorem does not yet finish the holes

Theorem 1.1 and Corollary 5.4 are both integral, but they concern different
integral objects.

* Theorem 1.1 chooses (W-kM) inclusion chains, one for every residual
  middle owner, and covers the protected holes up to (o(W)) exceptions.
* Corollary 5.4 covers **every saturated state completion** of every
  residual middle owner.  Each owner has

  \[
  (m)_Q^2
  \tag{7.1}
  \]

  global saturated state completions.  Deploying the complete reservoir is
  therefore far beyond the (W+o(W)) length ledger.

To compose the two theorems one must choose, for every retained SCD chain,
one saturated extension which contains that chain's protected members,
and the chosen extensions must inherit (O(W/Q)) rotor blocks.  The full
reservoir Hall theorem does not imply that its arbitrary thin transversal
has any edge.

This warning is sharp.  The explicit shifted-table construction in
`MATH_ATTACK_TRP_BALANCED_FLOW_HIDDEN_COLOR_OBSTRUCTION_20260725.md`
provides, at one top, an integral table of (M) state columns whose proper
rank flags are all distinct and exactly locally balanced, but whose
induced rotor successor graph has no edge.  Its queue-offset word has two
different successive-difference values; a rotor edge would force all
successive queue-offset differences to be equal.  Thus even perfect rank
balance does not preserve successor Hall under thin integral selection.

The exact remaining theorem is the following.

### Integral SCD--rotor thinning theorem (open)

For the (W-kM) retained SCD chains in Theorem 1.1, choose one global
saturated extension per chain so that the chosen columns admit a literal
rotor path cover with

\[
 O(W/Q)
\tag{7.2}
\]

blocks of (O(Q)) phases, while the (2QkM=o(W)) exceptional protected
holes are handled by the already proved \(o(W)\)-cost patch in Corollary
1.2b (or absorbed into the same blocks).

This is the literal bounded-phase block theorem requested by the local
reserve architecture.  At the present one-bite scale, however, it is not
yet coefficient-safe: the selected column mass is \(W-o(W)\), and
\(O(W/Q)\) independent initializations may cost \(O(W)\).  A standalone
coefficient-one compiler needs the sharper

\[
 \boxed{p=o(W/Q),}
\tag{7.3}
\]

equivalently average rotor-run length \(\omega(Q)\), unless the
initialization intervals are absorbed in-place into a deleted baseline
segment.

No result in this note proves this thinning theorem.  In particular:

1. the SCD condensation is about the actual protected complement, not
   donor strings;
2. the successor-Hall theorem is exact and integral on the complete state
   reservoir;
3. dividing the complete reservoir by the state-fibre multiplicity would
   be only a fractional answer;
4. the hidden-color table prevents any deduction from rank balance alone.

## 8. Final boundary

The one-bite analysis now has a precise proved/conditional boundary.

Proved:

\[
 \boxed{
 \begin{gathered}
 |\mathcal H_0|=W-kM=W-o(W),\\
 \mathcal H\setminus E\text{ has exact chain-cover number }W-kM,\\
 |E|\le2QkM=o(W),\\
 |\mathcal L_0|=W-f,\quad
 \mathcal L\setminus E_{\rm lit}\text{ has exact width }W-f,\\
 |E_{\rm lit}|\le2Qf=o(W),\\
 \text{the full residual-owner state reservoir has an integral}\
 O(Q)\text{-phase block cover of order }O(V/Q).
 \end{gathered}}
\tag{8.1}
\]

Not proved:

\[
 \boxed{
 \begin{gathered}
 \text{an integral }W\text{-scale thinning which simultaneously keeps}\\
 \text{the SCD hole cover and }O(W/Q)\text{ literal rotor blocks};\\
 \text{for a standalone coefficient-one compiler, the still sharper}\\
 p=o(W/Q)\text{ run bound (or an exact in-place reset absorption).}
 \end{gathered}}
\tag{8.2}
\]

Also proved is the sharp architectural warning that the one-bite middle
mass is still (W-o(W)).  Therefore a short-block theorem at this stage
must be an in-place baseline replacement; as an appended reserve it costs
another (W-o(W)) positions and cannot yield coefficient one.
