# AD24: exact audit of the delayed departure-swap rotor diamond

Date: 2026-07-25

Pure mathematics only.  No computation, solver, search, or web input is
used.

## 0. Verdict

The proposed diamond is correct under the exact residual-size hypothesis

\[
 Q\ge1,qquad H-Q\ge2.
\tag{0.1}
\]

Put \(n=2Q\).  Starting from

\[
 \omega_0=(L;z_1,\ldots,z_n;R),
 \qquad |L|=m-Q,quad |R|=H-Q,
\tag{0.2}
\]

choose distinct \(x_1,x_2\in L\), choose \(y_1\in R\), and choose

\[
 y_2\in R-y_1+z_n.
\tag{0.3}
\]

The two initial routes are

\[
 A:(x_1,y_1),(x_2,y_2),
 \qquad
 B:(x_2,y_1),(x_1,y_2).
\tag{0.4}
\]

After these two edges the lower and residual blocks agree, while the queues
are

\[
 (x_2,x_1,z_1,\ldots,z_{n-2}),
 \qquad
 (x_1,x_2,z_1,\ldots,z_{n-2}).
\tag{0.5}
\]

Apply the same legal moves \((a_s,b_s)\) to both arms for
\(1\le s\le n-1\).  Before move \(n-1\) their residual blocks still
agree.  That move ejects \(x_1\) on arm \(A\) and \(x_2\) on arm \(B\).
The resulting residual blocks have intersection of exact size

\[
 |R|-1=H-Q-1.
\tag{0.6}
\]

Choose \(a_n\) in the common lower block and choose the final arrival
\(b_n\) in this intersection.  The final edge ejects \(x_2\) on arm
\(A\) and \(x_1\) on arm \(B\).  Both the queues and residual blocks then
agree.  Hence the arms rejoin after exactly

\[
 2+n=2Q+2
\tag{0.7}
\]

edges.

For \(0\le j\le n\), let rank \(j\) mean Boolean rank

\[
 r_j=m-Q+j.
\tag{0.8}
\]

The signed difference between the complete state-flag incidence columns of
the two arms is

\[
 \boxed{
 \Delta
 =\sum_{j=0}^{n}
 \left(
 e_{K_j+x_2}^{(r_j)}-e_{K_j+x_1}^{(r_j)}
 \right),}
\tag{0.9}
\]

where

\[
 K_0=L-\{x_1,x_2\}+y_1,
\tag{0.10}
\]

and, for \(1\le j\le n\),

\[
 K_j=L-\{x_1,x_2\}
       +\{y_1,y_2,b_1,\ldots,b_{j-1}\}.
\tag{0.11}
\]

Thus there is exactly one unmatched target occurrence on each arm in each
controlled rank, and the two occurrences differ by the unit exchange
\(x_1\leftrightarrow x_2\).  Equivalently, the signed vector has two
nonzero target coordinates in each rank.  Therefore

\[
 \boxed{
 \sum_{j=0}^{n}\|\Delta_{r_j}\|_2^2
 =2(n+1)=2(2Q+1).}
\tag{0.12}
\]

There are no hidden repeated quotient states.  Each arm is simple, and the
two arms are internally vertex-disjoint.  The only common states are their
initial and final endpoints.  This follows from the monotone trajectory of
the distinguished pair \(x_1,x_2\): they pass through

\[
 LL,\quad LQ,\quad QQ,\ldots,QQ,\quad QR,\quad RR,
\tag{0.13}
\]

with their ordered queue positions advancing strictly at every intermediate
step.

The sole correction to the informal claim is linguistic.  The incidence
**difference** is not supported on one target coordinate per rank; it is
one elementary exchange and hence has support two per rank.  Formula
(0.12) already reflects the correct interpretation.

## 1. State transition and flags

For a quotient state

\[
 \omega=(D;q_1,\ldots,q_n;S),
\]

a rotor edge \((x,y)\), with \(x\in D\) and \(y\in S\), is

\[
 \mathcal R_{x,y}(\omega)
 =\left(
 D-x+y;
 x,q_1,\ldots,q_{n-1};
 S-y+q_n
 \right).
\tag{1.1}
\]

The state target at rank \(r_j=m-Q+j\) is the prefix flag

\[
 F_j(\omega)=D+\{q_1,\ldots,q_j\},
 \qquad0\le j\le n.
\tag{1.2}
\]

The case \(j=0\) is the lower endpoint, \(j=Q\) is the middle owner, and
\(j=n\) is the upper endpoint.

## 2. The first two edges

After the first edge, arm \(A\) is

\[
 \omega^A_1=left(
 L-x_1+y_1;
 x_1,z_1,\ldots,z_{n-1};
 R-y_1+z_n
 \right),
\tag{2.1}
\]

and arm \(B\) is

\[
 \omega^B_1=left(
 L-x_2+y_1;
 x_2,z_1,\ldots,z_{n-1};
 R-y_1+z_n
 \right).
\tag{2.2}
\]

The second departure is legal because \(x_2\) remains in the lower block
of (2.1) and \(x_1\) remains in the lower block of (2.2).  The common
second arrival is legal by (0.3).  Substitution in (1.1) gives

\[
 \omega^A_2=left(
 D_0;
 x_2,x_1,z_1,\ldots,z_{n-2};
 S_0
 \right),
\tag{2.3}
\]

\[
 \omega^B_2=left(
 D_0;
 x_1,x_2,z_1,\ldots,z_{n-2};
 S_0
 \right),
\tag{2.4}
\]

where

\[
 D_0=L-\{x_1,x_2\}+\{y_1,y_2\},
\tag{2.5}
\]

\[
 S_0=R-y_1+z_n-y_2+z_{n-1}.
\tag{2.6}
\]

All displayed operations are set operations in a state partition.  In
particular (2.6) remains valid when \(y_2=z_n\).

## 3. Queue chronology and exact rejoining time

For \(1\le s\le n-1\), choose the same departure \(a_s\) from the common
lower block and the same arrival \(b_s\) from the common residual block,
as long as the latter is common.  After \(k\) such moves, where
\(0\le k\le n-2\), the queues are

\[
 Q^A_k=(a_k,\ldots,a_1,x_2,x_1,z_1,\ldots,z_{n-2-k}),
\tag{3.1}
\]

\[
 Q^B_k=(a_k,\ldots,a_1,x_1,x_2,z_1,\ldots,z_{n-2-k}).
\tag{3.2}
\]

Here the initial string \((a_k,\ldots,a_1)\) is empty at \(k=0\).
The lower and residual blocks agree on the two arms throughout these
states.

The next common move, numbered \(n-1\), is chosen while the residual
blocks still agree.  It produces queues

\[
 Q^A_{n-1}=(a_{n-1},\ldots,a_1,x_2),
 \qquad
 Q^B_{n-1}=(a_{n-1},\ldots,a_1,x_1).
\tag{3.3}
\]

If the common residual block just before this move is \(S\) and its common
arrival is \(b_{n-1}\), the two new residual blocks are

\[
 S^A=(S-b_{n-1})+x_1,
 \qquad
 S^B=(S-b_{n-1})+x_2.
\tag{3.4}
\]

At that moment \(x_1,x_2\notin S\), because they occupy the final two queue
positions.  Hence

\[
 S^A\cap S^B=S-b_{n-1},
 \qquad |S^A\cap S^B|=|R|-1.
\tag{3.5}
\]

Hypothesis \(|R|=H-Q\ge2\) supplies a final common arrival

\[
 b_n\in S^A\cap S^B.
\]

The lower blocks have remained equal, so choose one common final departure
\(a_n\).  Applying (1.1) once more gives the common queue

\[
 (a_n,a_{n-1},\ldots,a_1)
\tag{3.6}
\]

and the common residual block

\[
 (S-b_{n-1}-b_n)+\{x_1,x_2\}.
\tag{3.7}
\]

The lower blocks are also equal.  This proves exact rejoining after
\(n+2=2Q+2\) edges.

## 4. Rank-by-rank flag difference

At time one, the lower targets are

\[
 F_0(\omega^A_1)=K_0+x_2,
 \qquad
 F_0(\omega^B_1)=K_0+x_1,
\tag{4.1}
\]

with \(K_0\) from (0.10).  At every positive prefix length, the departure
is restored by the first queue coordinate, so

\[
 F_j(\omega^A_1)=F_j(\omega^B_1)
 \qquad(1\le j\le n).
\tag{4.2}
\]

Now let \(1\le j\le n\), put \(k=j-1\), and consider the state after
\(2+k=j+1\) edges.  Its common queue prefix of length \(k\) is

\[
 a_k,a_{k-1},\ldots,a_1.
\]

At prefix length \(j=k+1\), arm \(A\) next contains \(x_2\), while arm
\(B\) next contains \(x_1\).  All shorter prefixes agree; every longer
prefix contains both \(x_1,x_2\) and also agrees.  Restoring the common
departures \(a_1,\ldots,a_k\) to the common lower block shows that the
rank-\(r_j\) targets are precisely

\[
 F_j(\omega^A_{j+1})=K_j+x_2,
 \qquad
 F_j(\omega^B_{j+1})=K_j+x_1,
\tag{4.3}
\]

with \(K_j\) from (0.11).

The arrival labels

\[
 y_1,y_2,b_1,\ldots,b_{n-1}
\]

are automatically pairwise distinct and lie outside the original \(L\).
Indeed, once an arrival enters the lower block, even if it is chosen as a
later departure it must traverse all \(n\) queue slots before returning to
the residual block, and the diamond ends first.  The same delay prevents
an original lower label other than the distinguished exiting pair from
becoming an arrival during the arm.  Consequently

\[
 |K_j|=m-Q+j-1,
\]

so both targets in (4.3) have exactly the asserted rank \(r_j\).

Therefore, for a fixed rank \(r_j\), all paired state occurrences cancel
except the one pair in (4.1) or (4.3).  This proves (0.9).  Since
\(x_1,x_2\notin K_j\) and \(x_1\ne x_2\), each row difference has squared
Euclidean norm two, proving (0.12).

## 5. No duplicate states

No freshness hypothesis on the filler moves is needed.  Track only the
two distinguished labels.

* At time zero, both \(x_1,x_2\) lie in the lower block.
* At time one, one lies in queue position one and the other remains lower.
* At times \(2,3,\ldots,n\), both lie in consecutive queue positions, and
  these positions increase strictly by one at every time.
* At time \(n+1\), one lies in the residual block and the other in the last
  queue position.
* At time \(n+2\), both lie in the residual block.

Thus one arm cannot repeat a state at two different times.  The same block
pattern rules out equality of opposite-arm states at different stages.
Within the double-queue stage, if an arm-\(A\) state at offset \(k\) equaled
an arm-\(B\) state at offset \(\ell\), the positions of \(x_1,x_2\) would
force simultaneously

\[
 k+2=\ell+1,
 \qquad k+1=\ell+2,
\]

which is impossible.  At equal times the labels occupy opposite positions
or opposite blocks until the last edge.  Hence the two arms meet only at
their prescribed endpoints.

## 6. Exact scope

The audit proves an integral equal-length rotor-walk exchange with vertical
squared movement \(2(2Q+1)=O(Q)\).  It preserves the carrier, literal
chronology, and both endpoints.  It does not by itself prove the
mean-reversion identity required by the simultaneous LVMR theorem; one
must still orient and distribute many applicable diamonds so that their
rankwise unit exchanges correlate with the current discrepancy vectors.

The hypotheses actually used are:

1. \(Q\ge1\), so the queue has at least two slots;
2. \(|L|=m-Q\ge2\), to choose distinct \(x_1,x_2\);
3. \(|R|=H-Q\ge2\), exactly for the final common arrival; and
4. every filler move is chosen legally and identically until the final
   residual split.

No distinctness or freshness condition is required for the filler labels.
