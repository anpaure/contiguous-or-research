# Lane L: corrected chronology, the linear-seam trace gate, and the exact surviving PBBS problem

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
computation is used.

## 0. Verdict

Put

\[
 N=2m+1,\qquad W=\binom{N}{m},\qquad
 B_m=\operatorname {Cat}_m=\frac{W}{N},
 \qquad H_A=\lceil A\sqrt m\rceil .
\]

The proposed implication

\[
 d(D)=1\Longrightarrow
 \text{the next return has gap }2\operatorname {ht}(D)+1
\]

is false, even for primitive roots.  I therefore retract all consequences
of the claimed Catalan-density lower bound: in particular, no lower bound
\(\nu_{H_A}(P_m)\ge c_A B_m\sqrt m\), no disproof of \((RP_A)\), and no
claim that global fusion is forced survives.

There is, however, an independent coefficient-one advance.  The audited
dominance-staircase chart repairs one cut in \(4H-1\) literal nonzero
letters.  With endpoint-capped erosion, a cyclic owner component of length
\(L\) cut at \(J\) transition edges therefore costs exactly at most

\[
 \boxed{L+(5H-1)J.}                                      \tag{0.1}
\]

Consequently the central-band word has the deterministic length bound

\[
 \boxed{
 \mathcal L_H
 \le W+2HB_m+2(5H-1)\nu_H(P_m).}                        \tag{0.2}
\]

The true sufficient fixed-window gate furnished by (0.2) is not the
Catalan-order bound stated in the first seam report.  It is the strictly
weaker condition

\[
 \boxed{
 \nu_{H_A}(P_m)=o_A(B_m\sqrt m),}                       \tag{ST_A}
\]

or, equivalently after the rotation-deck reduction,

\[
 \boxed{
 \overline\nu_{H_A}=o_A(B_m/\sqrt m).}                  \tag{QST_A}
\]

If \((ST_A)\) holds for every fixed \(A>0\), then the product-SCD outer
tail and a diagonal choice of \(A\to\infty\) prove

\[
 \nu(k)\le(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]

This is a proved reduction, not a proof of its hypothesis.

The audited height trace already gives the scale-correct estimate

\[
 \boxed{
 \overline\nu_H
 \le\sum_{h\le H-1}\frac{b_{m,h}}{h+2}
 \le C\frac{B_m}{\sqrt m},}                         \tag{0.3}
\]

where \(b_{m,h}\) is the number of semilength-\(m\) Dyck roots of height
\(h\).  Thus only a vanishing improvement over the exact reciprocal-height
trace capacity remains.  This is a factor \(\sqrt m\) weaker than the old
quotient form of \((RP_A)\), which asked for \(o(B_m/m)\).

For genuine zero-winding returns, the strict PBBS chronology, exact partial
wreath, triangular Pascal fan, and fixed-profile multislot fibre bound all
survive the correction.  They do not yet prove \((QST_A)\): a start-fibre
rarity bound and an edge-volume bound combine automatically by their
minimum, not their product.  The missing positive assertion is now a joint
trace-capacity gain by any factor \(o(1)\), rather than the old additional
factor \(o(1/\sqrt m)\).

There is also a new, independently audited intermediate-phase trace chart.
Every genuine zero-winding start of height \(s\) injects into a product of
two first-passage strip kernels and one terminal corridor kernel.  Summed
over \(s\le A\sqrt m\), its total ambient capacity is

\[
 O_A(B_m/\sqrt m).
\]

The formal chart has matching order on every fixed Gaussian height band.
Thus genuine same-row compatibility across the transported seams, not a
second independent endpoint count, is exactly where a vanishing factor
must enter.

## 1. Exact retraction and the facts which survive it

For a Dyck root write the canonical first-maximum factorization

\[
 D=P1R0S,qquad
 \delta(D)=|P|+1,qquad d(D)=|S|+1,
\]

and put \(\tau=\phi^2\).  The literal two-step identity

\[
 \boxed{\tau(P1R0S)=S1P0R}                         \tag{1.1}
\]

is valid.  What is invalid is the assertion that the displayed deepest
spine remains canonical through all formal sector shifts whenever
\(S=\varnothing\).  A transported off-spine forest can be attached at
positive depth and become the first deepest forest.

The primitive counterexample

\[
 D=1111100001110000
\]

has height five and \(d(D)=1\), but its five-state \(\tau\)-cycle has
deficits

\[
 (1,1,1,7,1)
\]

and first-maximum positions

\[
 (11,5,5,5,11).
\]

Starting from the displayed root, the five deficits sum to \(11\), whereas
the terminal first-maximum position is \(5\).  Hence there is no proposed
gap-eleven return.  The smaller primitive example

\[
 1110011000
\]

has \((\delta,d)=(3,1),(3,5),(7,1)\) around its three-state
\(\tau\)-cycle, and \(1+5+1=7\ne3\).

The following downstream assertions are therefore retracted.

1. Primitive roots of Gaussian height are not known to be return starts.
2. Their positive Catalan mass gives no residence-packing lower bound.
3. \((RP_A)\) is neither proved nor disproved.
4. A shared global fusion theorem is a possible fallback, not a forced
   conclusion.

Two conditional calculations from the discarded argument remain valid but
have no return family to which they can presently be applied.  Bounded-
height primitive roots have positive Catalan mass at a fixed Gaussian
height, and an actual family of \(R\) quotient return starts of length at
most \(H+1\) would greedily contain \(R/(2H+1)\) edge-disjoint quotient
intervals, whose full deck gives \(N R/(2H+1)\) physical intervals.

## 2. The chronology-free one-cut theorem

Let

\[
 X_{i+1}=X_i-\{r_i\}+\{a_i\}
\]

be a rank-\((m+1)\) Johnson walk, cut between \(X_{-1}\) and \(X_0\).
Assume

\[
 2H\le m+1.                                        \tag{2.1}
\]

For \(1\le s,t\le H\), put

\[
 P_{s,t}=\bigcap_{i=-s}^{t-1}X_i,qquad
 C=X_{-1}\cap X_0.
\]

The floor-correct size is

\[
 \boxed{|P_{s,t}|=m+2-s-t.}                       \tag{2.2}
\]

For \(x\in C\), let \(u_x,v_x\in[H]\) be its capped positive-run
extents to the left and right of the cut.  Then

\[
 \boxed{
 P_{s,t}=\{x\in C:u_x\ge s,\ v_x\ge t\}.}         \tag{2.3}
\]

### Lemma 2.1 (floor correctness excludes a southwest point)

If (2.2) holds, there is no \(x\in C\) with

\[
 u_x<s,qquad v_x<t.                               \tag{2.4}
\]

#### Proof

List the \(s+t\) owners in the defining window.  Map every coordinate of
the first owner which is absent from the total intersection to its first
departure transition.  This map is injective because each Johnson
transition removes one coordinate.  If (2.4) holds, \(x\) has an internal
arrival on the left and a later internal departure on the right.  The later
departure is not the first-departure image of any initial coordinate: if
\(x\) was initially absent it is not an initial coordinate, and if it was
initially present it departed before its displayed re-entry.  Thus at most
\(s+t-2\) of the \(s+t-1\) transitions are used by the injection, and

\[
 |P_{s,t}|\ge(m+1)-(s+t-2)=m+3-s-t,
\]

contradicting (2.2).  \(\square\)

Take the Pareto-minimal points among \((u_x,v_x)\), in increasing first
coordinate, and join them by a southeast unit staircase \(\Gamma\) from
\((1,H)\) to \((H,1)\), moving east before south between successive
minima.  It has exactly

\[
 |V(\Gamma)|=2H-1.                                 \tag{2.5}
\]

The southwest exclusion implies that, for every floor-correct query
\(q=(s,t)\) and every extent point \(p\ge q\), the rectangle \([q,p]\)
meets \(\Gamma\).  Along \(\Gamma\), the condition \(z_1\ge s\) is a
suffix condition and \(z_2\ge t\) is a prefix condition.  Consequently

\[
 \boxed{
 P_{s,t}=\bigcup_{\substack{z\in V(\Gamma)\\z\ge(s,t)}}P_z,} \tag{2.6}
\]

and the sets on the right occur in one contiguous subword of the staircase.
Every helper is nonempty, because

\[
 |P_z|\ge m+2-z_1-z_2\ge m+2-2H\ge1.              \tag{2.7}
\]

Thus the \(2H-1\) staircase letters cover every correct lower crossing
target.  The chronological owner word

\[
 X_{-H},X_{-H+1},\ldots,X_{H-1}
\]

has \(2H\) nonzero letters and covers every upper crossing union of at
most \(H+1\) owners.  Concatenating the two blocks proves the literal
one-cut length

\[
 \boxed{(2H-1)+2H=4H-1.}                          \tag{2.8}
\]

No primitive-root, zero-winding, FIFO, LIFO, or endpoint-order assertion
enters this proof.  In particular Section 23's correction does not alter
it.

## 3. Several cuts and the exact global ledger

Cut a cyclic projected-owner component of length \(L\) at \(J\ge1\)
transition edges meeting every positive residence interval of length at
most \(H\).  Endpoint-capped erosion of the resulting paths uses

\[
 L+HJ
\]

letters.  It covers every correct owner window remaining inside one path.
Append the \((4H-1)\)-letter chart of Section 2 at every cut.  A window
crossing several nearby cuts may be assigned to any one of them; the chart
uses the actual original chronological collar.  Therefore the component
cost is (0.1).

On an active cycle \(C\), let \(J_C\) be a minimum circular transversal
of the residence intervals.  Circular interval packing gives

\[
 J_C\le\nu_H(C)+1\le2\nu_H(C),                    \tag{3.1}
\]

because an active cycle has \(\nu_H(C)\ge1\).  An inactive cycle uses its
cyclic erosion word at overhead \(2H\).  The number of projected cycles is
at most \(B_m\).  Summing proves (0.2).

The all-depth PBBS support theorem says that the floor-correct consecutive
intersections and complementary unions contain every required target in
the central ranks.  Hence (0.2) is an integral literal OR word, not a
signed relaxation or a family chosen independently at different depths.

For fixed \(A\), (0.2) gives

\[
 \frac{\mathcal L_{H_A}-W}{W}
 \le
 \frac{2H_A}{N}
 +\frac{2(5H_A-1)\nu_{H_A}(P_m)}{NB_m}.            \tag{3.2}
\]

Since \(H_A/N=O_A(m^{-1/2})\), the second term is \(o_A(1)\) precisely
under \((ST_A)\).  Thus the previously advertised assumption
\(\nu_{H_A}=O_A(B_m)\) remains sufficient but is much stronger than the
actual seam-ledger requirement.

### Theorem 3.1 (linear-seam trace reduction)

If \((ST_A)\) holds for every fixed \(A>0\), then

\[
 \boxed{
 \nu(k)\le(1+o(1))\binom{k}{\lfloor k/2\rfloor}.} \tag{3.3}
\]

#### Proof

For every fixed integer \(j\), (3.2) tends to zero at
\(H=\lceil j\sqrt m\rceil\).  Choose thresholds \(M_j\) increasing so
that above \(M_j\) the central normalized excess is at most \(1/j\),
\(2\lceil j\sqrt m\rceil\le m+1\), and the audited product-SCD word
outside that central window has normalized length at most

\[
 C(1+j^2)e^{-j^2/2}.
\]

Put \(a(m)=j\) for \(M_j\le m<M_{j+1}\), and
\(H_m=\lceil a(m)\sqrt m\rceil\).  Then

\[
 a(m)\to\infty,\qquad H_m=o(m),
\]

the central excess is \(o(W)\), and the product-SCD outer tail is also
\(o(W)\).  This proves (3.3) in odd dimension.  The audited trimmed
one-coordinate lift preserves the leading constant in even dimension.
\(\square\)

A slightly more general sufficient condition, useful for a direct
double-limit proof, is

\[
 \boxed{
 \lim_{A\to\infty}
 A\limsup_{m\to\infty}
 \frac{\nu_{H_A}(P_m)}{B_m\sqrt m}=0.}             \tag{3.4}
\]

The factor \(A\) is exact at the scale of (3.2).

## 4. Deck reduction and the corrected quotient scale

Let \(\overline\nu_H\) be the maximum packing of nonwrapping short-return
intervals on the long \(\tau\)-quotient cycles, and let \(Z_H\) be the
number of quotient edges on cycles of length at most \(H+1\).  The exact
deck inequalities are

\[
 \boxed{
 N\overline\nu_H
 \le\nu_H(P_m)
 \le2N\overline\nu_H+NZ_H.}                       \tag{4.1}
\]

When \(H=H_A\), voltage-itinerary rigidity gives

\[
 Z_H\le(2H+2)N^{2H+2}=\exp(o(m)),                 \tag{4.2}
\]

and hence \(NZ_H=o(B_m\sqrt m)\).  Equations (4.1)--(4.2) prove the
equivalence of \((ST_A)\) and \((QST_A)\).

Substitution of (4.1) into (3.2) gives the explicit quotient ledger

\[
 \frac{\mathcal L_H-W}{W}
 \le
 \frac{2H}{N}
 +4(5H-1)\frac{\overline\nu_H}{B_m}
 +2(5H-1)\frac{Z_H}{B_m}.                         \tag{4.3}
\]

Thus the quotient double-limit criterion is

\[
 \boxed{
 \lim_{A\to\infty}
 A\limsup_{m\to\infty}
 \frac{\sqrt m\,\overline\nu_{H_A}}{B_m}=0.}     \tag{4.4}
\]

The old \((RP_A)\) quotient target \(o(B_m/N)=o(B_m/m)\) is sufficient
but no longer necessary for the proved seam construction.  The new target
\(o(B_m/\sqrt m)\) is larger by a factor of order \(\sqrt m\).

## 5. The audited reciprocal-height trace and its exact gap

The normalized PBBS map preserves Dyck height.  Let

\[
 b_{m,h}=\#\{D\in\mathcal D_m:\operatorname {ht}(D)=h\}.
\]

A residence-\(\ell\) return has omitted-label gap \(2\ell-1\).  The
peak-deletion height-gap theorem gives

\[
 2\ell-1\ge2h+1,
\]

so \(\ell\ge h+1\).  Its projected interval, including insertion and
removal edges, therefore has at least \(h+2\) quotient edges.  Every edge
of such an interval remains in the height-\(h\) stratum.  Hence any
nonwrapping edge-disjoint family \(\mathcal P\) satisfies

\[
 (h+2)|\mathcal P_h|\le b_{m,h},                  \tag{5.1}
\]

which proves the first inequality in (0.3).

For completeness, if \(F_m(t)\) counts Dyck paths of height at most \(t\),
then

\[
 F_m(t)=\frac2{t+2}\sum_{j=1}^{t+1}
 \sin^2\!\frac{\pi j}{t+2}
 \left(2\cos\frac{\pi j}{t+2}\right)^{2m}.       \tag{5.2}
\]

For \(t\le\sqrt m\), pairing conjugate eigenvalues gives

\[
 F_m(t)
 \le C B_m\left(\frac{\sqrt m}{t}\right)^3
       \exp\!\left(-c\frac m{t^2}\right).        \tag{5.3}
\]

Heights at least \(\sqrt m\) contribute at most \(B_m/\sqrt m\) to
the reciprocal sum.  On the dyadic class

\[
 2^{-j-1}\sqrt m<h\le2^{-j}\sqrt m,
\]

(5.3) bounds the contribution by

\[
 C\frac{B_m}{\sqrt m},2^{4j}e^{-c4^j}.
\]

The series is summable, proving the second inequality in (0.3).

The implication boundary is now exact.  The trace theorem gives

\[
 \overline\nu_{H_A}=O_A(B_m/\sqrt m),              \tag{5.4}
\]

whereas coefficient one through the linear seam follows from

\[
 \overline\nu_{H_A}=o_A(B_m/\sqrt m).              \tag{5.5}
\]

No Catalan-density return family is known to saturate (5.4).  The invalid
primitive argument supplied precisely that nonexistent saturation claim.

There is an independent critical-scale charge for positive winding.  Put

\[
 \mathscr D_m=\sum_{D\in\mathcal D_m}d(D),
 \qquad d(D)=|S(D)|+1.                             \tag{5.6}
\]

The audited first-highest-component moment theorem gives

\[
 \boxed{\mathscr D_m=\Theta(\sqrt m\,B_m).}        \tag{5.7}
\]

If \(I\) is a return of step-two duration \(s\) and winding \(a(I)\),
its exact deficit-core weight is

\[
 w(I):=\sum_{j=0}^{s-1}d(D_j)
      =\delta(D_s)+Na(I).                          \tag{5.8}
\]

Hence every nonwrapping quotient-edge-disjoint positive-winding family
\(\mathcal P_+\) satisfies

\[
 N|\mathcal P_+|
 \le\sum_{I\in\mathcal P_+}
       w(I)
 \le\mathscr D_m,
\]

and therefore

\[
 \boxed{|\mathcal P_+|=O(B_m/\sqrt m).}            \tag{5.9}
\]

This again reaches only the critical big-oh scale.  A proof of
\((QST_A)\) must show that positive-winding families cannot asymptotically
saturate the deficit ledger, or must combine (5.8) with a genuinely new
chronological capacity.

## 6. What the corrected zero-winding chronology really proves

Assume now that \(D_0\) begins an actual zero-winding return after
\(2s+1<N\) PBBS steps.  Put

\[
 D_j=\tau^jD_0=P_j1R_j0S_j,qquad
 C_j=\sum_{q<j}d(D_q),qquad
 M_j=\delta(D_j)-C_j.
\]

The exact voltage identities give

\[
 \boxed{M_{j+1}-M_j=-d(\phi D_j)<0.}              \tag{6.1}
\]

Since \(M_s=0\), the proper values are positive.  This strict chronology,
not a static sector shift, proves

\[
 \boxed{
 \operatorname {ht}(D_j)=s\ (0\le j\le s),
 \qquad d(D_0)=1.}                                \tag{6.2}
\]

It also yields the literal staircase prefix

\[
 \boxed{
 P_s1=(S_{s-1}1)(S_{s-2}1)\cdots(S_01),
 \qquad \operatorname {ht}(S_j)\le j.}           \tag{6.3}
\]

The omitted labels before the returned endpoint are pairwise distinct.
Writing

\[
 a_j=\lambda_{2j}\ (0\le j\le s),
 \qquad b_j=\lambda_{2j+1}\ (0\le j<s),
\]

there are disjoint cores \(K,K'\), each of size \(m-s\), such that

\[
 A_{2j}=K\cup\{a_0,\ldots,a_{j-1}\}
             \cup\{b_j,\ldots,b_{s-1}\},         \tag{6.4}
\]

\[
 A_{2j+1}=K'\cup\{b_0,\ldots,b_{j-1}\}
               \cup\{a_{j+1},\ldots,a_s\}.       \tag{6.5}
\]

Thus a genuine zero-winding segment is an exact factor-native partial
wreath.  Equations (6.4)--(6.5) use the whole return and do not turn
\(d(D_0)=1\) into a converse.

Repeated peak deletion gives a further chronology-safe theorem.  Put

\[
 D^{(j)}=\partial^jD_0,qquad r_j=|D^{(j)}|_{\rm semi},
\]

and let \(\ell\) be the first level at which
\(r_\ell=s-\ell\).  Then \(D^{(\ell)}\) is the mountain
\(1^{s-\ell}0^{s-\ell}\), and for every

\[
 0\le j\le\ell,qquad0\le a\le j,
\]

the level-\(j\) PBBS has the exact return interval

\[
 \boxed{
 I_{j,a}=[2a,\,2s+1-2(j-a)]}                     \tag{6.6}
\]

of common gap \(2(s-j)+1\).  This triangular fan follows from the two
canonical child passages and the height-gap lower bound; it uses no
first-deepest-spine transport.

Fix

\[
 k\le\min(\ell,\lfloor s/2\rfloor).
\]

At inverse level \(j\), \(1\le j\le k\), the free mass is

\[
 y_j=r_{j-1}-2r_j+r_{j+1},
\]

distributed among \(2r_j+1\) ordered slots.  The unrestricted conditional
fibre has size

\[
 F_j=\binom{r_{j-1}+r_{j+1}}{2r_j}.               \tag{6.7}
\]

The fan fixes \(j\) distinct slot variables, after transport to one common
phase, to prescribed nonnegative values.  Hence the compatible fibre is
at most

\[
 K_j\le
 \binom{r_{j-1}+r_{j+1}-j}{2r_j-j}.               \tag{6.8}
\]

For every fixed bottom core and realizable rank profile, the exact
multilevel upper ratio is therefore

\[
 \boxed{
 Q_k(\mathbf r)
 =\prod_{j=1}^k\prod_{i=0}^{j-1}
 \frac{2r_j-i}{r_{j-1}+r_{j+1}-i}.}               \tag{6.9}
\]

There are three necessary scope corrections.

1. The transported prescribed values in (6.8) need not be zero.  Replacing
   their total by zero only maximizes the displayed upper bound.
2. On the formal harmonic profile \(r_j=R/(j+1)\), the proved statement is
   only

   \[
   \lim_{k\to\infty}\lim_{R\to\infty}kQ_k=e.
   \]

   The inner limit keeps \(k\) fixed.  It does not establish a diagonal
   Gaussian-depth asymptotic or a dynamically admissible harmonic return.
3. A start-fibre estimate and the trace estimate (5.1) combine without
   further structure as a minimum.  Multiplying the two factors requires
   a joint transported-fibre capacity or clustering theorem.

Under the old \((RP_A)\) quotient target, an optimistic \(1/s\) fibre gain
still needed another interval factor \(1/s\) and a further little-oh.  Under
the proved seam reduction, the trace factor already has the correct order
\(B_m/s\).  Any genuine joint gain \(\eta_m\to0\) over that capacity would
now suffice.  This is the quantitative benefit of (0.2), but the joint gain
itself remains unproved.

## 7. The intermediate-phase three-strip trace chart

The forward and dual staircases can be cancelled at an arbitrary
intermediate phase without assuming a static deepest spine.  Define

\[
 F_0(z)=F_1(z)=1,
 \qquad F_{j+1}(z)=F_j(z)-zF_{j-1}(z),             \tag{7.1}
\]

and the first-passage and corridor kernels

\[
 A_a(x)=\frac{x^a}{F_a(x^2)},
 \qquad
 G_s(x)=\frac{x^s}{F_{s+1}(x^2)}.                 \tag{7.2}
\]

The kernel \(A_a\) counts nonnegative walks which first reach height
\(a\) at their last step.  The kernel \(G_s\) counts walks from height
\(s\) to zero which stay in the corridor \([0,s]\).

For the genuine zero-winding block of Section 6 and \(0\le t<s\), put

\[
 Q_t=(S_{t-1}1)\cdots(S_01)                       \tag{7.3}
\]

and

\[
 V_t=(\overline T_{s-1}1)\cdots
     (\overline T_{t+1}1)\overline T_t,           \tag{7.4}
\]

where the audited dual blocks satisfy

\[
 S_t1P_t=P_{t+1}1\overline T_t,
 \qquad \operatorname {ht}(T_t)\le s-1-t.        \tag{7.5}
\]

### Theorem 7.1 (exact intermediate cancellation)

For every \(0\le t<s\),

\[
 \boxed{P_t=Q_tV_t.}                              \tag{7.6}
\]

Consequently the ambient generating function for the phase-\(t\) trace is

\[
 \boxed{
 H_{s,t}(x)
 =A_t(x)A_{s-t}(x)G_s(x)
 =\frac{x^{2s}}
 {F_t(x^2)F_{s-t}(x^2)F_{s+1}(x^2)}.}             \tag{7.7}
\]

Every genuine zero-winding start of duration \(s\), after applying the
bijection \(D_0\mapsto D_t=\tau^tD_0\), gives a distinct word counted by
\([x^{2m}]H_{s,t}(x)\).

#### Proof

The terminal dual factorization gives

\[
 P_01=(\overline T_{s-1}1)\cdots(\overline T_01)=V_01,
\]

so \(P_0=Q_0V_0\).  Also

\[
 Q_{t+1}=S_t1Q_t,
 \qquad V_t=V_{t+1}1\overline T_t.
\]

Assume \(P_t=Q_tV_t\).  Using (7.5),

\[
 \begin{aligned}
 P_{t+1}1\overline T_t
 &=S_t1P_t\\
 &=S_t1Q_tV_t\\
 &=Q_{t+1}V_{t+1}1\overline T_t.
 \end{aligned}
\]

Right cancellation in the free word monoid proves (7.6) inductively.

The height caps in (6.3) make \(Q_t\) a first-passage strip word of height
\(t\).  The reversed/complemented dual caps make \(V_t1\) one of height
\(s-t\).  After the first maximum, the remainder of \(D_t\) is a corridor
walk from height \(s\) to zero.  These three uniquely delimited pieces give
(7.7).  Since \(\tau\) is a permutation, distinct starts give distinct
phase-\(t\) roots.  \(\square\)

At \(t=0\),

\[
 H_{s,0}(x)=\frac{x^{2s}}{F_s(x^2)F_{s+1}(x^2)}  \tag{7.8}
\]

is exactly the generating function for Dyck words of height exactly
\(s\), which checks the endpoint normalization.  Moreover

\[
 F_a(1/4)=\frac{a+1}{2^a},                        \tag{7.9}
\]

and hence

\[
 H_{s,t}(1/2)
 =\frac{2}{(t+1)(s-t+1)(s+2)}.                   \tag{7.10}
\]

Relative to the full height-\(s\) class, the exact critical-mass ratio is

\[
 \boxed{
 \frac{H_{s,t}(1/2)}{H_{s,0}(1/2)}
 =\frac{s+1}{(t+1)(s-t+1)}.}                     \tag{7.11}
\]

Thus a central phase has formal mass smaller by order \(1/s\).

### Lemma 7.2 (uniform central-strip coefficient)

Fix \(\varepsilon>0\).  There are constants
\(c_\varepsilon,C_\varepsilon>0\) such that, whenever

\[
 \varepsilon s\le t\le(1-\varepsilon)s,
\]

one has

\[
 \boxed{
 [x^{2m}]H_{s,t}(x)
 \le C_\varepsilon 4^m s^{-5}
      \exp\!\left(-c_\varepsilon\frac m{s^2}\right).} \tag{7.12}
\]

#### Proof

Normalize coefficients by

\[
 u_a(\ell)=2^{-\ell}[x^\ell]A_a(x),
 \qquad
 v_s(\ell)=2^{-\ell}[x^\ell]G_s(x).               \tag{7.13}
\]

Finite-path diagonalization, with the two endpoint eigenvector factors and
the eigenvector normalization retained, together with the two-barrier
short-time cancellation, gives absolute constants \(c,C\) such that, for
\(a\ge1\) and \(s\ge1\),

\[
 \|u_a\|_1=\frac1{a+1},
 \qquad
 \|v_s\|_1=\frac2{s+2},                           \tag{7.14}
\]

\[
 u_a(\ell)
 \le\frac{C}{(a+1)^3}
       \exp\!\left(-\frac{c\ell}{(a+1)^2}\right), \tag{7.15}
\]

and

\[
 v_s(\ell)
 \le\frac{C}{(s+2)^3}
       \exp\!\left(-\frac{c\ell}{(s+2)^2}\right). \tag{7.16}
\]

For clarity about the uniformity in these two estimates, when
\(\ell\le(a+1)^2\), two-barrier reflection gives

\[
 u_a(\ell)
 \le C(\ell+1)^{-3/2}
       \exp\!\left(-c\frac{(a+1)^2}{\ell+1}\right)
 \le C(a+1)^{-3}.                                 \tag{7.16a}
\]

When \(\ell\ge(a+1)^2\), pairing the finite-path spectral modes gives
(7.15), including its exponential time decay.  The same two-regime
argument gives (7.16).  Taking absolute values termwise in the spectral
sum at short times would lose this cancellation and is not sufficient.

Now

\[
 4^{-m}[x^{2m}]H_{s,t}
 =(u_t*u_{s-t}*v_s)(2m).                           \tag{7.17}
\]

In every convolution term one of the three lengths is at least \(2m/3\).
Apply (7.15) or (7.16) to that factor and sum the other two with (7.14).
All three strip widths are \(\Theta_\varepsilon(s)\), giving (7.12).
\(\square\)

Since, with \(y=m/s^2\),

\[
 s^{-5}e^{-c m/s^2}
 =m^{-5/2}y^{5/2}e^{-cy}
 \le C m^{-5/2},                                  \tag{7.18}
\]

each fixed height contributes at most \(C_\varepsilon B_m/m\).
For \(s\ge2\), choosing \(t=\lfloor s/2\rfloor\) permits the fixed choice
\(\varepsilon=1/3\); the bounded case \(s=1\) is absorbed directly from
(7.8).  Summing gives

\[
 \begin{aligned}
 \sum_{s\le A\sqrt m}[x^{2m}]H_{s,\lfloor s/2\rfloor}
 &\le C4^m\sum_{s\ge1}s^{-5}e^{-cm/s^2}\\
 &=O_A(4^m/m^2)\\
 &=\boxed{O_A(B_m/\sqrt m).}                      \tag{7.19}
 \end{aligned}
\]

In particular, the total number of genuine zero-winding quotient starts
in the fixed Gaussian window is \(O_A(B_m/\sqrt m)\).  This is a start
count, so it also bounds their quotient interval packing.

The order in (7.19) cannot be improved from the ambient three-strip chart
alone.  If

\[
 a\sqrt m\le s\le b\sqrt m,
 \qquad t=\lfloor s/2\rfloor,
\]

the matching local finite-path lower estimates give

\[
 [x^{2m}]H_{s,t}
 =\Theta_{a,b}(4^m s^{-5})
 =\Theta_{a,b}(B_m/m).                             \tag{7.20}
\]

Summing a fixed Gaussian height band gives formal capacity
\(\Theta_{a,b}(B_m/\sqrt m)\).  This lower estimate concerns the ambient
chart; it does not assert that its words satisfy the complete PBBS return
identities.

Let \(Z^{(0)}_{m,s}\) be the set of actual certified zero-winding starts
of duration \(s\), and put

\[
 E_{m,s}=\tau^{\lfloor s/2\rfloor}Z^{(0)}_{m,s}.
\]

Thus \(E_{m,s}\) is an explicitly defined subset of the central chart,
and its members satisfy every simultaneous PBBS seam identity.  A precise
sufficient same-row chronology statement for the zero-winding part of
\((QST_A)\) is

\[
 \boxed{
 \sup_{a\sqrt m\le s\le A\sqrt m}
 \frac{|E_{m,s}|}{[x^{2m}]H_{s,\lfloor s/2\rfloor}}
 \longrightarrow0}                               \tag{7.21}
\]

for every fixed \(0<a<A\).  The small-height part is uniformly suppressed
by the exponential in (7.12): first take the \(m\to\infty\) limsup and
then let \(a\downarrow0\).  Equation (7.21) would therefore turn (7.19)
into \(o_A(B_m/\sqrt m)\) for zero winding.  It does not by itself settle
positive winding.

The point of (7.21) is genuinely chronological: the product (7.7) remembers
one intermediate seam but forgets compatibility of all transported seams.
Counting several phases independently is invalid because the same orbit
word can recycle across phases.  No statement here uses
\(d(D)=1\) as a return criterion.

The decisive cancellation (7.6), the three-kernel normalization, the
\(4^{-m}\) convolution, and the big-oh/little-oh scope were independently
audited.  That audit is why the short-time two-wall estimate (7.16a) is
stated explicitly rather than hidden inside a termwise spectral bound.

## 8. Exact proved and unproved boundary

### Proved

1. The primitive \(d=1\) converse and every residence lower bound derived
   from it are false and retracted.
2. \((RP_A)\) is neither proved nor disproved.
3. The literal one-cut chart has length \(4H-1\), and the several-cut
   component cost is \(L+(5H-1)J\).
4. The global central-band ledger is (0.2).
5. The fixed-window gate \((ST_A)\), equivalently \((QST_A)\), implies
   coefficient one after the standard tail diagonalization.
6. The reciprocal-height trace gives only the critical big-oh estimate
   (0.3).
7. Conditional on an actual zero-winding return, the strict staircase,
   exact partial wreath, triangular Pascal fan, and multislot fibre ratio
   (6.9) are valid and integral.
8. The three-strip trace chart (7.7) is exact, and the total number of
   fixed-window genuine zero-winding starts is
   \(O_A(B_m/\sqrt m)\).  The ambient chart has matching order on every
   fixed Gaussian height band.
9. Positive-winding quotient packings satisfy the independent critical
   bound \(O(B_m/\sqrt m)\) by the exact deficit ledger.

### Unproved

1. The vanishing trace-capacity gain

   \[
   \overline\nu_{H_A}=o_A(B_m/\sqrt m).
   \]

2. A joint Catalan/Pascal transported-fibre inequality that supplies this
   gain for zero winding, together with a corresponding positive-winding
   charge.
3. A deck-shared dynamic-frame braid or any other global fusion theorem.
4. The unconditional constant-one theorem.

The corrected sole gate in this lane is therefore not a Catalan-density
obstruction and not forced fusion.  It is the chronology-sensitive strict
version of the reciprocal-height trace bound.  The audited Pascal fan is a
valid source of additional constraints, but those constraints must be
coupled to edge capacity before they imply coefficient one.
