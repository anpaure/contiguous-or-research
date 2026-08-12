# AD25: adversarial full-connector audit of the truncated static cube

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Exact verdict

The directed flush-and-reload theorem and the literal state-count ledger in
`TRUNCATED_ROTOR_STATIC_CUBE_COMPILATION_20260725.md` are correct.  The
connector analysis can, however, be sharpened substantially.

Let

\[
 n=2Q,
 \qquad
 F_h(A;z_1,\ldots,z_n;B)
   =A\cup\{z_1,\ldots,z_h\},
 \qquad 0\le h\le n.
\]

Write \(\widetilde I_h(E)\) for the complete aggregate multiplicity vector
of the rank-\((m-Q+h)\) masks over the compiled path for cube vertex \(E\),
including marked states, flush states, and the two-step port seams.

If an adjacent source-collar pair in positions \(r,r+1\) is transposed,
then one flush-and-reload route has, already after aggregation over time,

\[
 \|\Delta_h\|_2^2=4
 \qquad(r+1\le h\le n-1).
 \tag{0.1}
\]

The target reload is supported only at \(h\le r\), so it cannot cancel
(0.1).  This confirms the earlier single-route connector audit.

The new point is that the two opposite source traces on the two sides of a
two-step port seam cannot cancel each other either.  For an interior cell
\((i,j)\), \(j<t-1\), put

\[
 q=q_{ij}=4t+2i-2j+1,
 \qquad
 r=Q-q.
 \tag{0.2}
\]

The pair occurs in positions \(r,r+1\) at \(A_j\), and in positions
\(r+2,r+3\) at \(C_j\).  At every prefix rank

\[
 r+3\le h\le 2Q-1,
 \tag{0.3}
\]

the first source trace is supported on masks which contain both of the last
two old collar labels and neither label of the next column pair.  After the
two cyclic updates, those last two collar labels are in the tail, whereas
the next flush first promotes one label of the next column pair while the
other remains in the core.  Hence the second source trace is supported on
masks with the opposite four-label signature.  The two supports are
disjoint, independently of every legal buffer choice.  Consequently the
**complete compiled path**, not merely one routed transition, satisfies

\[
 \boxed{
 \|\widetilde I_h(E\oplus e_{ij})-
       \widetilde I_h(E)\|_2^2=8
 \quad(r+3\le h\le2Q-1),}
 \tag{0.4}
\]

and therefore

\[
 \boxed{
 \sum_{h=0}^{2Q}
 \|\widetilde I_h(E\oplus e_{ij})-
       \widetilde I_h(E)\|_2^2
 \ge 8(Q+q_{ij}-3).}
 \tag{0.5}
\]

Since \(q_{ij}\ge2t+3\), the right side is at least
\(8(Q+2t)\).  Thus shifted buffers do not produce a cross-port telescope.
This is an exact aggregate-mask statement, not a time-resolved estimate.

At the middle owner, \(h=Q\), (0.4) gives squared difference exactly eight
for every interior bit.  A last-column bit has only the first source trace
and has squared difference exactly four.  The affine middle-owner theorem
in the source is correct for the slot-equivariant unpadded path, and its
fair independent cube law in fact has the exact trace

\[
 \boxed{
 \operatorname{tr}\operatorname{Cov}(O(E))
 =2p(t-1)+p=2pt-p=(1/8-o(1))M.}
 \tag{0.6}
\]

In particular its middle-row trace is \(\Theta(M)\), not \(o(M)\).  The
source upper bound \(16pt\) is valid but very crude; there is no missing
factor of two in its inequality.

There is also a routing-independent variance--drift obstruction to a
common-seed repair.  On \(p-t+1=(1/2-o(1))Q\) lower rows, exactly \(t\)
support-disjoint marked rectangles occur, where

\[
 t=(1+o(1))\frac{M}{8Q}\longrightarrow\infty.
 \tag{0.7}
\]

For any random physical increment \(Z_q\), including all connector terms,
if its conditional mean retains coefficient reversion rate \(\alpha_a\)
in those orthogonal rectangle modes, then

\[
 \boxed{
 \mathbb E\|Z_q\|_2^2\ge\sum_{a\text{ on row }q}\alpha_a^2.}
 \tag{0.8}
\]

Thus \(O(1)\) squared discrepancy on such a row forces the root-mean-square
retained drift rate to be \(O(t^{-1/2})=o(1)\).  If an order-one rate is
retained in a positive fraction of all \(pt=(1/16-o(1))M\) cells, summing
(0.8) forces \(\Omega(M)\) total vertical second moment.  Common-seed
correlation, including interval-discrepancy correlation, cannot evade this
inequality: connector cancellation can lower the physical norm only by
also canceling the mean in the marked repair modes.

The exact conditional boundary is important.  This rules out a common seed
which keeps order-one drift in the coefficient-scale family of marked cell
modes.  It does not rule out a lower-dimensional, load-adaptive drift, nor
a genuinely global cross-carrier exchange whose useful drift is not the
cellwise cube drift.

## 1. Audit of the literal route and all length factors

The source quotient update is

\[
 (A;z_1,\ldots,z_n;B)
 \longmapsto
 (A-x+y;x,z_1,\ldots,z_{n-1};B-y+z_n),
 \tag{1.1}
\]

where \(x\in A\), \(y\in B\), and \(n=2Q\).  In the first \(n+1\)
updates of the routing theorem, the core choices are

\[
 x_1,\ldots,x_n,a
\]

and the tail choices are

\[
 b,z_n,z_{n-1},\ldots,z_1.
\]

Every displayed tail choice is legal: at update \(s\ge2\), the chosen old
collar label dropped at update \(s-1\).  After these updates the blocks and
collar are

\[
 A_1=(A-\{x_1,\ldots,x_n,a\})+b+\{z_1,\ldots,z_n\},
\]

\[
 B_1=(B-b)+x_1,
 \qquad
 (a,x_n,\ldots,x_2).
\]

The next \(n\) updates select target collar labels in reverse target order
and use \(x_1,\ldots,x_n\) as tail choices.  They end at the prescribed
target.  Hence the exact transition count is

\[
 2n+1=4Q+1.
\]

The hypothesis \(|A|\ge n+1\) holds eventually because
\(|A|=m-Q\) and \(Q=o(m)\).

For \(t\) marked port pairs there are \(t\) routes \(A_j\to B_j\),
\(t-1\) routes \(C_j\to A_{j+1}\), and \(2(t-1)\) cyclic seam updates.
Adding the initial state gives

\[
\begin{aligned}
 N
 &=1+t(4Q+1)+(t-1)(4Q+1+2)\\
 &=(2t-1)(4Q+2).
\end{aligned}
\tag{1.2}
\]

Thus there is no missing endpoint or seam occurrence in the source count.
Initializing the first radius-\(Q\) state uses \(2Q+2\) letters, and every
subsequent state uses one, so the unpadded word length is

\[
 N+2Q+1.
 \tag{1.3}
\]

Let \(t\) be maximal subject to \(N\le M\).  Since

\[
 N(t+1)-N(t)=8Q+4,
\]

the exact padding gap \(\delta=M-N\) obeys

\[
 \boxed{0\le\delta<8Q+4.}
 \tag{1.4}
\]

The arbitrary padding invoked in Section 4 of the source is not covered by
the affine proof in its Section 6.2, which explicitly removes that padding.
One must not combine the padded Section 7 ledger with the unpadded affine
claim without auditing a padding rule.  Quantitatively this is not a
coefficient-one length obstruction: over \(N_H\asymp W/M\) carriers, both
the gap and the initialization ledger have size

\[
 O(QN_H)=O(QW/M)=o(W).
 \tag{1.5}
\]

Thus one may keep the unpadded theorem and charge the missing occurrences
to an \(o(W)\) defect ledger.  This observation does not by itself cover
those missing targets.  Alternatively one may append a routed padding
segment at the same \(o(W)\) length scale, but then its incidence and
variance must be included.

## 2. Exact aggregate incidence of one source toggle

Fix a source collar with

\[
 z_r=u,
 \qquad
 z_{r+1}=v,
 \qquad 1\le r<n,
\]

and compare it with the collar obtained by swapping \(u,v\).  Couple the
routes by the same buffer slots.  Define, for a set \(L\) containing
neither \(u\) nor \(v\),

\[
 \Phi_{uv}(L)=e_{L+u}-e_{L+v}.
 \tag{2.1}
\]

After \(s\le n\) flush updates the collar is

\[
 (x_s,x_{s-1},\ldots,x_1,z_1,\ldots,z_{n-s}).
 \tag{2.2}
\]

For \(0\le s\le n-r\), the two routes have the same core and differ at
exactly the prefix boundary

\[
 h=r+s.
\]

The corresponding aggregate contribution is \(\Phi_{uv}(K_h)\), where,
for \(s=h-r\ge1\),

\[
 K_h=A+b+\{z_1,\ldots,z_{r-1}\}
       +\{z_{n-s+2},\ldots,z_n\}.
 \tag{2.3}
\]

At the next state

\[
 s_*=n-r+1,
\]

the label which dropped first has entered the core and the other has just
dropped into the tail.  Every prefix differs, with the opposite
orientation.  Write its base as \(J_h\); explicitly,

\[
\begin{aligned}
 J_h={}&A-\{x_1,\ldots,x_{s_*}\}+b
       +\{z_{r+2},\ldots,z_n\}\\
 &+\operatorname{pref}_h
   (x_{s_*},\ldots,x_1,z_1,\ldots,z_{r-1}).
\end{aligned}
\tag{2.4}
\]

After one further update both labels are in the core, so the source toggle
has disappeared.

At \(h=n\), \(K_n=J_n\), and the two terms cancel.  For

\[
 r+1\le h\le n-1,
\]

one has \(z_{r+2}\in J_h\setminus K_h\).  The four masks

\[
 K_h+u, K_h+v, J_h+u, J_h+v
\]

are therefore distinct, and the aggregate source-flush difference is

\[
 \Phi_{uv}(K_h)-\Phi_{uv}(J_h),
\]

of squared norm four.

During target reload, the target label in position \(r+1\) is inserted
first.  At that state only \(h=0\) distinguishes its orientation.  The
next insertion moves the unique distinguishing boundary to \(h=1\), and
each later insertion moves it one step right.  The complete target-order
contribution is therefore supported on

\[
 h=0,1,\ldots,r.
 \tag{2.5}
\]

This proves (0.1) after aggregation over every occurrence of the route.

## 3. Exact cross-port non-telescoping theorem

The single-route estimate does not alone rule out cancellation against the
oppositely oriented source trace after the next port seam.  The following
four-label invariant does.

### Theorem 3.1 (two-step seam separates the two source traces)

Fix an interior cell \((i,j)\), \(0\le j<t-1\), and toggle only
\(E_{ij}\).  Use arbitrary legal, slot-equivariant buffer choices in both
flush routes, with all buffer slots fixed independently of \(E\), as in the
source's Section 6.2.  Let \(r=Q-q_{ij}\).  For the complete unpadded
compiled path,

\[
 \|\widetilde I_h(E\oplus e_{ij})-
       \widetilde I_h(E)\|_2^2=8
 \qquad(r+3\le h\le n-1).
 \tag{3.1}
\]

The statement remains true after any continuation which begins after the
two compared paths have coalesced at \(A_{j+1}\).

#### Proof

In \(A_j\), the row pair \(u,v\) occupies collar positions \(r,r+1\).
In \(B_j\) it occupies the same two slots with complementary orientation.
Write the target collar of \(B_j\) as

\[
 (z'_1,\ldots,z'_n).
\]

All row swaps occur in the first \(Q\) collar slots, and the column swaps
change the unordered core and tail but no collar label.  Hence the final
two source- and target-collar labels agree.  Put

\[
 L=\{z'_{n-1},z'_n\}=\{z_{n-1},z_n\}.
 \tag{3.2}
\]

Let \(C=\{c,d\}\) be the two labels of the next column transposition
\(\beta_{j+1}\).  At phase \(s_j\), both labels of \(C\) lie beyond the
current owner/core boundary and outside the collar, whereas the first tail
choice in the route \(A_j\to B_j\) is a label of \(\beta_j\), not of
\(C\).

Consider a rank \(h\ge r+3\).  In (2.3) one has \(s=h-r\ge3\), so its
suffix contains both \(z_{n-1},z_n\).  Formula (2.4) also contains both,
through \(\{z_{r+2},\ldots,z_n\}\).  Neither base contains \(c\) or
\(d\).  Thus every mask in the first source trace has signature

\[
 |S\cap L|=2,
 \qquad
 |S\cap C|=0.
 \tag{3.3}
\]

Now take the two prescribed cyclic rotor updates from \(B_j\) to \(C_j\).
Their collars are

\[
 (x,z'_1,\ldots,z'_{n-1})
\]

and

\[
 (y,x,z'_1,\ldots,z'_{n-2}).
\]

The labels \(z'_n,z'_{n-1}\) have therefore dropped into the tail.  The
two cyclic tail choices are the labels entering through the right owner
boundary; by the disjoint cut geometry and \(Q=o(H)\), neither is in
\(L\).  Hence both labels of \(L\) are in the tail of \(C_j\).

The states \(C_j\) and \(A_{j+1}\) differ in their unordered blocks by
exactly the exchange \(C=\{c,d\}\).  In the route
\(C_j\to A_{j+1}\), one of \(c,d\) is the distinguished core element and
the other is the first tail choice.  The distinguished core element is
selected only at flush update \(n+1\), whereas every boundary or special
state contributing to the source trace occurs by update \(n\).  The first
tail element is promoted at update one and is not one of the core buffers.
Consequently every base of the second source trace has signature

\[
 |S\cap L|=0,
 \qquad
 |S\cap C|=2.
 \tag{3.4}
\]

The pair \(u,v\) is disjoint from \(L\cup C\).  Adding either \(u\) or
\(v\) preserves (3.3)--(3.4), so the mask supports of the two source traces
are disjoint.  At \(C_j\) the pair has shifted to positions
\(r+2,r+3\).  Section 2 applied with \(r+2\) shows that its second source
trace has squared norm four for every \(h\ge r+3\); the first trace also
has squared norm four there.

It remains only to check that no third occurrence depending on \(E_{ij}\)
appears at these ranks.  A target reload of a pair ending in positions
\(r,r+1\) is supported at \(h\le r\).  The two cyclic seam states
distinguish the pair only at \(h=r+1\) and \(h=r+2\).  The target
\(A_{j+1}\) depends on column \(j+1\), not on \(E_{ij}\).  Hence for
\(h\ge r+3\) the complete difference is precisely the sum of the two
disjoint source traces.  This proves (3.1).  Both paths reach the same
state \(A_{j+1}\), so all later occurrences agree. \(\square\)

There are

\[
 (n-1)-(r+3)+1=n-r-3=Q+q_{ij}-3
\]

ranks in (3.1), proving (0.5).

For the last column \(j=t-1\), the unpadded path ends at \(B_{t-1}\) and
has no second source trace.  Section 2 still gives

\[
 \sum_h\|\Delta_h\|_2^2
 \ge4(n-r-1)=4(Q+q_{i,t-1}-1).
 \tag{3.5}
\]

An unaudited bit-dependent padding could alter (3.5), which is another
reason to keep the padding scope explicit.  The interior theorem, covering
\(p(t-1)=(1-o(1))pt\) cells, is unaffected by end padding because the two
paths have already coalesced.

### Exact endpoint and seam table

For later use, the dependence of one interior bit is as follows.

1. If \(j>0\), its appearance as the target order of
   \(C_{j-1}\to A_j\) is supported only at \(h\le r\).
2. In \(A_j\to B_j\), both endpoint orders depend on the bit.  The source
   flush has the trace in Section 2; the target reload is supported at
   \(h\le r\).  The final terms at \(h=r\) are part of the marked
   rectangle ledger.
3. The first cyclic seam state moves the adjacent pair to slots
   \(r+1,r+2\) and can distinguish it only at \(h=r+1\).  The second seam
   state, namely \(C_j\), moves it to \(r+2,r+3\) and can distinguish it
   only at \(h=r+2\).
4. In \(C_j\to A_{j+1}\), only the source order depends on the bit; its
   noncancelling source trace starts at \(h=r+3\).  At \(A_{j+1}\) the two
   paths coalesce.

Thus the two cyclic updates were counted correctly in the length ledger,
but they are not incidence-neutral outside the middle row.

## 4. Middle-owner affine theorem: passed, sharpened, and scoped

At middle rank \(h=Q\), a source adjacent pair can affect an owner at two
states:

1. when its two collar slots straddle \(Q,Q+1\);
2. when the first dropped label has entered the core and the other has just
   entered the tail.

At the next update both labels are in the core.  During target reload, one
target label remains in the core while the other is inserted in the first
collar slot, and then both are in the first two slots.  All these locations
belong to the middle owner, so target reload contributes no middle-owner
difference.  Also

\[
 r+2=Q-q_{ij}+2<Q
\]

because \(q_{ij}\ge2t+3\), so the two cyclic seam steps do not split the
pair at the middle boundary.

The middle-boundary events for all source pairs occur before any original
pair reaches its core--tail split event.  At each such occurrence at most
one disjoint row pair is split.  With buffer slots fixed independently of
orientations, there is therefore no two-bit interaction.  The complete
unpadded middle-owner vector has the affine form

\[
 O(E)=O(0)+\sum_{i,j}E_{ij}d_{ij}.
 \tag{4.1}
\]

An interior bit affects at most four owner occurrences, and each occurrence
difference has \(\ell_1\)-norm two.  Hence

\[
 \|d_{ij}\|_1\le8,
 \qquad
 \|d_{ij}\|_2^2\le64.
 \tag{4.2}
\]

For independent fair bits, the source's estimates give

\[
 \operatorname{tr}\operatorname{Cov}(O(E))
 =\frac14\sum_{i,j}\|d_{ij}\|_2^2
 \le16pt.
 \tag{4.3}
\]

Thus every factor in the source upper bound is valid.  It uses only the
crude implication \(\|d\|_2^2\le\|d\|_1^2\).  Even before using the exact
chronology below, the zero coordinate-sum of every direction improves this
to \(\|d\|_2^2\le32\): its total positive and total negative masses are
equal and at most four, and concentrating each mass maximizes its squared
norm.  This gives the upper bound \(8pt\).

The cross-port theorem supplies the exact value.  Since
\(Q\ge r+3\), (3.1) at \(h=Q\) gives

\[
 \|d_{ij}\|_2^2=8
 \qquad(0\le j<t-1).
 \tag{4.4}
\]

For a last-column bit, Section 2 gives exactly one source trace of squared
norm four at \(h=Q\); its target reload and the preceding target reload are
supported below the middle boundary.  Therefore

\[
 \operatorname{tr}\operatorname{Cov}(O(E))
 =\frac14\bigl(8p(t-1)+4p\bigr)
 =2pt-p.
 \tag{4.5}
\]

Because \(pt=(1/16-o(1))M\) and \(t\to\infty\), this is

\[
 \operatorname{tr}\operatorname{Cov}(O(E))
 =(1/8-o(1))M.
 \tag{4.6}
\]

The correct interpretation of Section 6.2 of the source is therefore:
connector variation is affine and has coefficient-scale, rather than
superlinear, trace.  It is not a low-variance middle-row kernel.

## 5. Exact number of independent cells on a hard row

Write

\[
 d=i-j.
\]

Then all cells on the same lower depth satisfy

\[
 q(d)=4t+2d+1.
 \tag{5.1}
\]

For sufficiently large \(m\), \(p>t\), because

\[
 p=(1/2-o(1))Q,
 \qquad
 t=(1+o(1))\frac{M}{8Q},
 \qquad
 \frac{t}{p}=O(M/Q^2)=o(1).
\]

For every integer

\[
 0\le d\le p-t,
\]

all \(t\) pairs

\[
 (i,j)=(j+d,j),
 \qquad0\le j<t,
\]

are legal.  Hence exactly \(t\) support-disjoint rectangles occur at each
of the \(p-t+1\) distinct depths (5.1).  Moreover

\[
 t(p-t+1)=(1-o(1))pt=(1/16-o(1))M.
 \tag{5.2}
\]

Thus almost every marked cell lies in a row containing the maximal row
population \(t\).

## 6. Common-seed discrepancy versus retained drift

The following statement allows arbitrary connector contamination and
arbitrary dependence among all cube bits.

### Theorem 6.1 (orthogonal-mode variance--drift inequality)

Let \(\rho_1,\ldots,\rho_K\) be the support-disjoint elementary rectangles
on one hard row, so

\[
 \langle\rho_a,\rho_b\rangle=0\quad(a\ne b),
 \qquad
 \|\rho_a\|_2^2=4.
\]

Put

\[
 \lambda_a(v)=\frac{\langle v,\rho_a\rangle}{4}.
 \tag{6.1}
\]

Let \(Z\) be any random integral physical row increment generated by any
common-seed coupling, and let \(E_a\in\{0,1\}\) denote the current cell
coefficients.  Suppose its net conditional mean, including every connector
term, satisfies

\[
 \lambda_a(\mathbb E[Z\mid E])
 =-\alpha_a(E_a-1/2)
 \qquad(1\le a\le K).
 \tag{6.2}
\]

Then, pointwise at every cube vertex,

\[
 \boxed{
 \mathbb E(\|Z\|_2^2\mid E)
 \ge\sum_{a=1}^K\alpha_a^2.}
 \tag{6.3}
\]

#### Proof

The vectors

\[
 u_a=\rho_a/2
\]

are orthonormal.  Put \(\mu=\mathbb E[Z\mid E]\).  By (6.1)--(6.2),

\[
 \langle\mu,u_a\rangle
 =2\lambda_a(\mu)
 =-2\alpha_a(E_a-1/2),
\]

whose absolute value is \(\alpha_a\).  Jensen's inequality and Bessel's
inequality give

\[
 \mathbb E(\|Z\|_2^2\mid E)
 \ge\|\mu\|_2^2
 \ge\sum_a|\langle\mu,u_a\rangle|^2
 =\sum_a\alpha_a^2.
\]

No independence, reversibility, or assumption on the connector map is
used. \(\square\)

On each plateau row from Section 5, \(K=t\).  If

\[
 \mathbb E\|Z\|_2^2\le C
\]

on that row, Theorem 6.1 gives

\[
 \left(\frac1t\sum_{a=1}^t\alpha_a^2\right)^{1/2}
 \le\sqrt{C/t}.
 \tag{6.4}
\]

Thus \(C=O(1)\) forces root-mean-square rate \(o(1)\).  More generally,
if \(\alpha_a\ge c>0\) on a positive fraction of all plateau cells, then
summing (6.3) over the plateau rows and using (5.2) yields

\[
 \sum_q\mathbb E\|Z_q\|_2^2
 \ge(c^2/16-o(1))M.
 \tag{6.5}
\]

The vertical low-variance descent criterion requires the left side to be
\(o(M)\).  Therefore an order-one cellwise drift on a coefficient-scale
subcube is incompatible with that criterion, even if a common seed makes
all connector intervals cancel as efficiently as algebraically possible.

There is a stronger identity when connector terms have zero projection on
the rectangle span and the update remains inside the marked bit cube.  If

\[
 \mathbb E(E'_a-E_a\mid E)
 =-\alpha(E_a-1/2)
\]

for all \(a\), then each bit flips with probability \(\alpha/2\).  Since a
flipped cell contributes squared norm four and the rectangles are
orthogonal,

\[
 \mathbb E\left\|
 \sum_a(E'_a-E_a)\rho_a
 \right\|_2^2=2\alpha K.
 \tag{6.6}
\]

Arbitrary common-seed correlations among the flips do not change (6.6).
Equation (6.3), rather than (6.6), is the robust statement for the complete
physical path, because connectors may project onto the marked rectangle
coordinates.

In particular, suppose all cell bits are deterministic functions of one
common seed, every bit is fair, and an update replaces that seed by an
independent fresh seed.  Conditional on the present seed,

\[
 \mathbb E(E'_a-E_a)=-\bigl(E_a-1/2\bigr),
\]

so \(\alpha_a=1\) for every cell.  Theorem 6.1 forces second moment at
least \(t\) on every plateau row and at least
\((1/16-o(1))M\) after summing those rows, irrespective of how small the
associated scalar interval discrepancy is.  Therefore fresh common-seed
resampling cannot be an \(O(1)\)-per-row physical kernel while preserving
the fair marked drift.

### Why interval discrepancy cannot keep all the drift

The source-toggle footprint is interval-like in the rank index: a source
pair beginning at boundary \(r\) contributes at every
\(h=r+1,\ldots,2Q-1\).  A shared seed can correlate the orientations of
many such intervals and may make a scalar signed interval sum small.
There are two independent limitations.

First, the vector entries are actual Boolean masks, not scalar interval
counts.  Theorem 3.1 exhibits a four-label signature which prevents even
the most natural opposite cross-port pair from canceling at any of the
overlapping ranks.

Second, even a hypothetical stronger routing which canceled all connector
components would still face Theorem 6.1.  If the physical increment has
\(O(1)\) squared norm on a row with \(t\) orthogonal marked modes, then its
conditional mean has only \(O(1)\) squared projection on those modes.  It
cannot simultaneously retain order-one mean reversion in all \(t\) modes.
If connector components cancel the marked projections themselves, they
also cancel the proposed repair drift.

## 7. Precise proved and unproved boundary

The following statements are proved.

1. The \(4Q+1\)-update route, the number
   \((2t-1)(4Q+2)\) of state occurrences, and the initialization toll
   \(2Q+1\) beyond those occurrences are exact.
2. A single adjacent source toggle has aggregate connector squared norm
   four at every prefix rank \(r+1,\ldots,2Q-1\).
3. In the actual rectangular compiler, the opposite source traces across a
   two-step port seam have disjoint support for all
   \(h\ge r+3\).  Hence every interior compiled bit has the exact full-path
   row norm (0.4) and the vertical lower bound (0.5).
4. The unpadded complete middle-owner vector is affine.  For independent
   fair bits its covariance trace is exactly (0.6), and is therefore
   \(\Theta(M)\).
5. On \((1/2-o(1))Q\) rows there are exactly \(t\to\infty\) orthogonal
   marked cells.  Any common-seed physical kernel retaining order-one
   cellwise drift in a positive fraction of these directions has
   \(\Omega(M)\) total vertical second moment.

The following statements are not proved and must not be inferred.

1. The arbitrary final padding in the source has no audited incidence or
   variance identity.  It is only an \(o(W)\) length issue.
2. The present argument does not prove that directions belonging to
   different cells cannot cancel under a specially designed simultaneous
   multi-bit, multi-carrier update.  It proves that such cancellation
   cannot preserve order-one drift in all orthogonal marked modes while
   having \(o(M)\) second moment.
3. A lower-dimensional adaptive kernel which targets only the current load
   gradient, instead of reverting every cube coefficient, is not excluded.
4. No literal coefficient-one cover follows from the designated marked
   cube alone.  The full connector word is literal, but its coefficient-
   scale fluctuation is a genuine part of the physical load.

The static cube therefore remains a valid coefficient-scale literal
capacity theorem, but its natural local low-variance deployment is closed:
shifted-buffer cross-port telescoping fails exactly, and an \(O(1)\)-per-row
common-seed discrepancy can retain only vanishing root-mean-square drift in
the marked cell family.
