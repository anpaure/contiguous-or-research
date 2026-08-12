# O: prefix freezing plus owner-fixed spikes — exact grouping capacity

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Outcome

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed and \(m\) is sufficiently large that \(H<m\).

The proposed deterministic theorem which would group an arbitrary family of
\(t\) owner-fixed spike moves into \(O(t/H)\) literal physical pieces while
retaining every earlier flag is **false for the presently certified spike
architecture**.  The decisive obstruction is not abstract rainbow binning,
and it is not the number of available lower histories.  It is an exact
omitted-phase residence constraint at the deepest upper layer.

Fix one omitted phase

\[
A_0=\{\alpha_1,\alpha_2\}.
\]

If a depth-\(H\) upper owner-fixed spike from phase \(A_0\) is actually
switched at owner start \(i\), while all its upper flags of depths
\(<H\) are retained, then its literal upper tower has

\[
X_i,\ldots,X_{i+H-1}\text{ disjoint from }A_0,
\qquad
X_{i+H}\cap A_0\ne\varnothing.
\tag{0.1}
\]

Consequently the \((H+1)\)-owner intervals belonging to two switched
spikes from the same phase are disjoint.  Across an arbitrary collection
of literal pieces of total owner-state length \(L\), if \(r_{A_0}\) such
spikes are switched, then

\[
\boxed{L\ge (H+1)r_{A_0}.}
\tag{0.2}
\]

If the pieces are genuine zero-portal radius-\(H\) rotor runs, positive
residence strengthens this to

\[
\boxed{L\ge (2H+1)r_{A_0}-H P_{A_0},}
\tag{0.3}
\]

where \(P_{A_0}\) is the number of nonempty pieces containing a switched
phase-\(A_0\) spike.  The slightly weaker convention-independent form

\[
L\ge 2Hr_{A_0}-(H-1)P_{A_0}
\tag{0.4}
\]

is therefore always valid in that setting.

The ordinary collision floor gives the deterministic conversion from
energy descent to switched occurrences.  If every serviced old fibre has
load at most \(K\), and a final corner decreases the old collision count
by \(\Delta_{A_0}\), then

\[
r_{A_0}\ge \frac{\Delta_{A_0}}{K-1}.
\tag{0.5}
\]

Hence every literal compilation retaining the shallower upper flags obeys

\[
\boxed{
L\ge \frac{H+1}{K-1}\,\Delta_{A_0}.}
\tag{0.6}
\]

For \(f\) load-two fibres whose old collision is removed, this is simply

\[
L\ge(H+1)f.
\tag{0.7}
\]

The lower owner-fixed spike commutes with the upper spike and fixes the
entire upper tower.  It therefore cannot alter (0.1).  Common-owner prefix
freezing also cannot alter (0.1) without releasing one of the very earlier
flags that the proposed theorem is required to retain.  At \(q=H\) there
is no deeper controlled tail in which to hide the discrepancy.

Thus a nominal count of \(O(t/H)\) packet labels is not a physical
amortization: one packet containing \(H\) same-phase deepest spikes needs
\(\Omega(H^2)\) owner-state positions.  In a word of length \(W+o(W)\), a
necessary condition is

\[
\boxed{
\max_{A_0} r_{A_0}=O(W/H),
}
\tag{0.8}
\]

and the radius-\(H\), few-piece version forces the sharper constant
\(\max_{A_0}r_{A_0}\le(1/2+o(1))W/H\).  A load bound
\(2\le\mu\le K\), abstract rainbow binning, and small permanent-prefix
cost do not imply this phase-dispersion condition.

There is a complementary exact fixed-core obstruction.  On one ordered
root/owner block, all possible multiway histories move at most \(q-1\)
depth-\(q\) lower flags.  If one additionally asks for clean spikes all at
one fixed depth, a constant-conjugation piece carries at most one such
spike: the apparently larger \(q-1\) menu is a diagonal collar, with
different first-change depths at its different starts.  This proves
precisely why the known block chart handles collars but not a diffuse
horizontal same-depth sector.

The positive boundary is equally precise.  A coefficient-one theorem may
still exist if it first proves phase dispersion at scale \(W/H\), then
uses the other \(W-r_{A_0}H\) principal owners as globally useful fillers,
and finally constructs one cross-phase stateful owner braid.  Nothing in
this report rules out such a new braid.  What is ruled out is the requested
deterministic grouping lemma from prefix cost and the existing spike atoms
alone.

## 1. Why a depth-sensitive grouping lemma would have been sufficient

Write

\[
N_q=\binom n{m-q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\qquad 1\le q\le H.
\tag{1.1}
\]

For fixed \(A\), put

\[
C_{A,m}=\max_{1\le q\le H}c_q.
\]

The exact ratio is

\[
\frac W{N_q}
=\prod_{j=1}^q\frac{m+j+1}{m-j+1}.
\tag{1.2}
\]

Hence \(C_{A,m}=O_A(1)\).  For example, from
\(\log(1+x)\le x\), for all sufficiently large \(m\),

\[
C_{A,m}\le \exp(3(A+1)^2).
\tag{1.3}
\]

Let \(r_q\) be the number of owners whose first permanent release is just
before depth \(q\), and put

\[
R_p=\sum_{q\le p}r_q.
\]

The exact permanent-prefix cost is

\[
\mathcal C
=\sum_{p=1}^H\frac{R_p}{c_p}
=\sum_{q=1}^Hr_q H_q,
\qquad
H_q:=\sum_{p=q}^H\frac1{c_p}.
\tag{1.4}
\]

For \(2\le q\le H\),

\[
H_q\ge\frac{H-q+1}{C_{A,m}}
\tag{1.5}
\]

and

\[
(q-1)(H-q+1)\ge H-1.
\tag{1.6}
\]

Therefore

\[
\boxed{
\sum_{q=2}^H\frac{r_q}{q-1}
\le
\frac{C_{A,m}}{H-1}\,\mathcal C.
}
\tag{1.7}
\]

In particular, if \(\mathcal C=o(W)\), then the right side of (1.7) is
\(o(W/H)\).

This is the exact quantitative reason that a clean theorem grouping
\(q-1\) first-depth-\(q\) changes per physical packet would compose with
common-owner prefix freezing.  No logarithm or unproved Gaussian estimate
is missing from that bookkeeping.  The failure is physical: existing
spike occurrences at a common depth do not admit that grouping, and the
deepest upper trace proves that even an arbitrary rotating-frame braid
must spend \(\Omega(H)\) owner positions per same-phase switched spike.

Equation (1.7) concerns permanent release.  A rank-isolated spike can in
principle rejoin and evade the Hardy tail in (1.4).  The theorem below is
independent of that overcharge; it uses the literal tower itself.

## 2. Exact collision descent per switched occurrence

Let \(\mu=(\mu_T)\) be one rank histogram, and let

\[
\Phi(\mu)=\sum_T\binom{\mu_T}{2}
\tag{2.1}
\]

be its ordinary collision floor.  Suppose \(r_T\) old occurrences leave
cell \(T\), \(n_T\) occurrences enter it, and

\[
\nu_T=\mu_T-r_T+n_T.
\]

Then the exact cellwise identity is

\[
\begin{aligned}
\Phi(\mu)-\Phi(\nu)
=\sum_T\bigg[&r_T\mu_T-\binom{r_T+1}{2}\\
&-n_T(\mu_T-r_T)-\binom{n_T}{2}\bigg].
\end{aligned}
\tag{2.2}
\]

Indeed, first remove \(r_T\) units and then add \(n_T\) units.  The two
successive changes of \(\binom{x}{2}\) are exactly the two lines in
(2.2).

If every old cell from which a unit is removed has load at most \(K\),
then the arrival terms in (2.2) are nonpositive and

\[
r_T\mu_T-\binom{r_T+1}{2}
\le r_T(\mu_T-1)
\le (K-1)r_T.
\]

Writing \(r=\sum_Tr_T\), we obtain the sharp universal bound

\[
\boxed{
\Phi(\mu)-\Phi(\nu)\le(K-1)r.
}
\tag{2.3}
\]

This proves (0.5).  It also fixes the quantifier omitted by a purely Haar
argument: a low-energy cube corner need not switch half of its bits.  What
is true deterministically is that a corner producing descent \(\Delta\)
must switch at least \(\Delta/(K-1)\) occurrences.

For load two, one moved occurrence destroys at most the unique old pair,
so eliminating \(f\) such pairs requires at least \(f\) moved
occurrences.  Equality is possible when every moved occurrence lands in
an empty cell.

## 3. The deepest upper omitted-phase trace

Fix one pair-omission source phase \(A_0=\{\alpha_1,\alpha_2\}\).  At a
source occurrence \(e_i=(S_i,Y_i)\), let

\[
U_0(i)=Y_i\subset U_1(i)\subset\cdots\subset U_H(i)
\]

be its upper tower.  At depth \(H\), let

\[
\{b_i\}=U_H(i)\setminus U_{H-1}(i),
\]

choose \(z_i\notin U_H(i)\cup A_0\), and let \(\theta_i\) exchange the
ordered pair \((b_i,z_i)\) with the ordered pair
\((\alpha_1,\alpha_2)\), in either bijective order.  This is precisely the
audited owner-fixed upper spike.

Every old flag in the source phase avoids \(A_0\).  For \(h<H\), the flag
\(U_h(i)\) contains neither \(b_i\) nor \(z_i\), while \(U_H(i)\)
contains \(b_i\) and omits \(z_i\).  Consequently the switched tower
satisfies

\[
\boxed{
\theta_iU_h(i)\cap A_0=\varnothing\quad(0\le h<H),
\qquad
|\theta_iU_H(i)\cap A_0|=1.
}
\tag{3.1}
\]

This conclusion is independent of which of the two bijections is chosen.

Let a literal physical piece have successive middle owner states

\[
X_0,X_1,\ldots,X_{\ell-1}.
\]

For a natural radius-\(H\) occurrence starting at \(i\), its upper flags
are

\[
U_h(i)=\bigcup_{j=0}^hX_{i+j}.
\tag{3.2}
\]

Thus (3.1) implies (0.1): every owner in
\(X_i,\ldots,X_{i+H-1}\) avoids both points of \(A_0\), whereas
\(X_{i+H}\) contains one of them.

### Theorem 3.1 — unconditional same-phase tower packing

Let \(i<j\) be two actually switched depth-\(H\) upper spikes from the
same phase \(A_0\) in one literal physical piece, and suppose all their
upper flags below depth \(H\) are retained.  Then

\[
\boxed{j-i\ge H+1.}
\tag{3.3}
\]

#### Proof

If \(1\le j-i\le H\), then

\[
j\le i+H\le j+H-1.
\]

The first spike makes \(X_{i+H}\) meet \(A_0\), while the second spike's
shallower frozen tower requires every owner
\(X_j,\ldots,X_{j+H-1}\) to avoid \(A_0\).  This is a contradiction.
\(\square\)

The intervals \([i,i+H]\) are therefore pairwise disjoint.  Each one
contains \(H+1\) owner states, including for the last spike before a path
boundary.  Summing over arbitrary pieces proves (0.2), with no boundary
correction.

This argument does not assume that a constant coordinate frame persists
between spikes.  It permits arbitrary changes of conjugacy, arbitrary
owner-path geometry between the displayed starts, and either choice of
the marker in \(A_0\).  It is therefore strictly stronger than the old
two-marker capacity for constant-frame row intervals.

## 4. Radius-\(H\) residence refinement

Use the directed Johnson convention

\[
X_{t+1}=X_t-\{r_t\}+\{a_t\}.
\tag{4.1}
\]

A zero-portal radius-\(H\) rotor run obeys

\[
a_p\ne r_q\qquad(0<q-p\le H).
\tag{4.2}
\]

Equivalently, every internally bounded positive coordinate run contains at
least \(H+1\) owners.

For a switched spike at start \(i\), let \(\alpha\in A_0\) be the unique
point in its depth-\(H\) flag.  By (0.1), \(\alpha\) is inserted at the
transition from \(X_{i+H-1}\) to \(X_{i+H}\).  If a later same-phase
spike starts at \(j\), its owner \(X_j\) avoids \(A_0\), so \(\alpha\)
must have been removed before \(X_j\).  Condition (4.2) gives

\[
\boxed{j-i\ge2H+1.}
\tag{4.3}
\]

Now consider one nonempty piece of owner-state length \(\ell\) containing
\(r\) switched phase-\(A_0\) spikes.  Consecutive starts are separated by
at least \(2H+1\), and the final start requires its complete
\((H+1)\)-owner tower.  Hence

\[
\ell\ge(r-1)(2H+1)+(H+1)
=(2H+1)r-H.
\tag{4.4}
\]

Summing (4.4) over the \(P_{A_0}\) nonempty pieces proves (0.3).  Dropping
one unit from every internal separation gives the convention-independent
weaker form (0.4).

On a cyclic zero-portal piece there is no terminal boundary rebate, and
the cyclic gaps give

\[
L\ge(2H+1)r_{A_0}.
\tag{4.5}
\]

The only way to discard the residence refinement is to put a portal or a
release seam between successive spikes.  That creates another physical
piece for the present ledger.  Even then the unconditional disjoint-tower
bound (0.2) survives.

## 5. Why lower spikes and prefix stopping do not cancel the trace

An owner-fixed lower spike has support inside the lower root
\(S_i\subset Y_i\).  Every upper flag contains \(S_i\), so the lower
permutation fixes every upper flag setwise.  The audited upper and lower
spikes commute occurrencewise.  Therefore adding an arbitrary lower spike
choice to the same owner leaves (3.1)--(4.5) unchanged.

At the deepest controlled depth, common-owner prefix freezing has only two
choices:

1. retain the upper flags through \(H-1\), in which case (3.1) and the
   tower-packing theorem apply; or
2. release an earlier upper flag, which violates the hypothesis that the
   grouping should not damage earlier flags and incurs the corresponding
   stopping cost.

There is no depth \(>H\) in the fixed window at which a deepest spike can
rejoin while leaving the displayed depth-\(H\) change intact.

The mismatch between the two ledgers is quantitative.  A deepest release
of \(t\) owners contributes only \(t/c_H\) to permanent-prefix cost, and
\(c_H=O_A(1)\).  Thus \(t=o(W)\) is enough for that scalar cost to be
\(o(W)\).  Literal packing instead requires

\[
t=O(W/H)
\tag{5.1}
\]

inside each omitted phase.  For example, \(t=W/\log m\) has
\(t/c_H=o(W)\) but violates (5.1) by a diverging factor.  Prefix cost alone
therefore cannot imply physical spike fusion.

The lower side has no analogous unavoidable global marker bottleneck.
For a depth-\(H\) lower spike, the helper may be chosen as any
\(a_i\in L_H(i)\), and \(|L_H(i)|=m-H\).  Given \(t\) lower spike jobs,
there is a helper assignment with maximum coordinate load at most

\[
\left\lceil\frac{t}{m-H}\right\rceil.
\tag{5.2}
\]

Indeed, give every coordinate \(c=\lceil t/(m-H)\rceil\) copies.  For
every nonempty job set \(J\), the union of its allowed helper sets has
size at least \(m-H\), hence copy capacity at least
\(c(m-H)\ge t\ge|J|\).  Capacitated Hall gives (5.2).

This does not solve lower chronology or lower cross-target Gram signs.  It
only shows that the sharp universal residence obstruction in this report
is the common two-point omitted phase on the upper side, not a forced
common lower helper.

## 6. Complete normal form for a fixed ordered central block

The phase-trace theorem already refutes the universal combined grouping
claim.  The following independent classification explains exactly why
arbitrary multiway histories do not enlarge the known fixed-core collar
chart.

Work in one tight row universe of size \(2m-1\).  Fix an ordered block

\[
S_j=I_\pi(j,m-1),\qquad
Y_j=I_\pi(j-1,m),\qquad 0\le j<t,
\tag{6.1}
\]

where \(1\le t\le m-1\).  Put

\[
d_j=S_j\setminus S_{j+1},\quad
a_j=S_{j+1}\setminus S_j\quad(0\le j<t-1),
\]

\[
G=\bigcap_{j<t}S_j,\qquad |G|=g=m-t,
\qquad y=Y_0\setminus S_0.
\tag{6.2}
\]

### Theorem 6.1 — exact same-core history normal form

Every pointed cyclic tight row realizing the identical ordered
root/owner block (6.1) has, after the displayed choice of origin, the
coordinate order

\[
\boxed{
(d_0,\ldots,d_{t-2},
 \gamma_1,\ldots,\gamma_g,
 a_0,\ldots,a_{t-2},
 e_1,\ldots,e_g,y),
}
\tag{6.3}
\]

where \((\gamma_1,\ldots,\gamma_g)\) is an arbitrary ordering of \(G\),
and \((e_1,\ldots,e_g)\) is an arbitrary ordering of the exterior
all-zero membership class.  Conversely every order (6.3) realizes
(6.1).

#### Proof

For consecutive roots, the unique disappearing and appearing coordinates
are \(d_j\) and \(a_j\).  Their distinct membership signatures across
\(S_0,\ldots,S_{t-1}\) force the two displayed boundary strings in that
order.  The common all-one membership class is exactly \(G\), and the
roots do not distinguish its internal order.  The predecessor owner
\(Y_0\) forces \(y\) immediately before \(S_0\).  The remaining
coordinates form the all-zero membership class and may occur in arbitrary
order between the right boundary and \(y\).  Counting gives

\[
(t-1)+g+(t-1)+g+1=2m-1,
\]

so no coordinate is missing.  Reading the \((m-1)\)- and \(m\)-windows
of (6.3) proves the converse. \(\square\)

For depth \(q\), the lower flag at start \(j\) is

\[
L_q(j)=I_\pi(j+q-1,m-q).
\tag{6.4}
\]

It depends on the ordering \(\gamma\) exactly when it contains a proper,
nonempty suffix of that string.  Writing

\[
r=j+q-t,
\]

this occurs exactly for \(1\le r\le m-t-1\).  Therefore the exact number
of movable depth-\(q\) starts is

\[
\boxed{
c_m(t,q)
=\left|[q-t,q-1]\cap[1,m-t-1]\cap\mathbb Z\right|
}
\tag{6.5}
\]

or equivalently

\[
c_m(t,q)=
\max\!\left(
0,
\min(q-1,m-t-1)-\max(q-t,1)+1
\right).
\tag{6.6}
\]

In particular,

\[
\boxed{c_m(t,q)\le q-1.}
\tag{6.7}

\]

The bound is sharp: reversing \(\gamma\) changes every proper nonempty
suffix in (6.5).  For \(q\le m/2\), taking \(t=q-1\) gives
\(c_m(t,q)=q-1\).

Thus arbitrary non-involutive, multiway, or factorial-size history menus
do not change more than \(q-1\) depth-\(q\) occurrences on one fixed
ordered block.  For \(C\) such blocks, positive-density motion at
\(q\le H\) requires \(C=\Omega(W/q)\), and at \(q\asymp H\) requires
\(\Omega(W/H)\) blocks.

### Corollary 6.2 — the collar is diagonal, not horizontal

Fix one coordinate permutation \(\gamma\) stabilizing all roots in a
typed interval.  Let \(s_0\) be the first boundary position at which the
relevant suffix of the common class is not \(\gamma\)-invariant.  At a
start \(i\), the first changed lower depth is the unique \(q\) satisfying

\[
i+q-1=s_0.
\tag{6.8}
\]

Hence, for any one fixed depth \(q\), a constant-conjugation typed piece
contains at most one clean lower \(q\)-spike.  The upper statement is the
same with prefixes of the exterior all-zero class.  A simultaneous
upper/lower product may place one clean spike of each sign at that depth,
but no more.

This is the exact meaning of “the block chart handles only collars.”  Its
up to \(q-1\) movable starts have different first-change depths along the
diagonal (6.8).  They do not group a horizontal family of distinguished
spikes all occurring at one depth.  Therefore \(t\) same-depth clean
spikes need at least \(t\) constant-frame typed pieces.  A stateful braid
which changes frame or central adjacency inside a long component is the
only escape from this corollary; Theorem 3.1 still constrains such a braid
on the deepest upper side.

### Proposition 6.3 — an explicit legal load-two horizontal catalogue

The preceding same-depth obstruction is nonvacuous already for
\(t\le m/2\) legal owner-fixed upper spikes.  Fix a source universe

\[
Q=[n]\setminus A_0,
\qquad |Q|=2m-1.
\]

Choose a set \(P\subset Q\) of size \(m+1\), a point \(p\in P\),
pairwise distinct points

\[
c_i^0,c_i^1\in P\setminus\{p\}
\qquad(1\le i\le t),
\]

and pairwise distinct points \(e_i\in Q\setminus P\).  The choices are
possible whenever

\[
2t\le m,\qquad t\le m-2.
\tag{6.9}
\]

For \(\varepsilon\in\{0,1\}\), put

\[
Y_i^\varepsilon=P\setminus\{c_i^\varepsilon\},
\qquad
S_i^\varepsilon=P\setminus\{c_i^\varepsilon,p\},
\tag{6.10}
\]

\[
U_{1,i}^\varepsilon
=Y_i^\varepsilon\cup\{e_i\},
\qquad
U_{2,i}=P\cup\{e_i\}.
\tag{6.11}
\]

Thus the depth-two target \(U_{2,i}\) has load exactly two in the
displayed catalogue, while targets belonging to different \(i\)'s are
distinct.  All roots and owners in (6.10) are pairwise distinct.  The
local cyclic order

\[
(p,\;S_i^\varepsilon\text{ in any order},\;e_i,\;c_i^\varepsilon,\ldots)
\tag{6.12}
\]

realizes (6.10)--(6.11): the predecessor \(m\)-window is
\(Y_i^\varepsilon\), the root is \(S_i^\varepsilon\), and the next two
upper entries are \(e_i,c_i^\varepsilon\).  Complete the unused positions
arbitrarily.  For fixed Gaussian \(H\), there are enough remaining
coordinates to extend the upper tower and choose the usual helper outside
\(U_H\).

Map \(c_i^\varepsilon\) to a fixed point \(\alpha\in A_0\), using the
other omitted coordinate for the outside helper.  The owner-fixed spike
fixes \(S_i^\varepsilon,Y_i^\varepsilon,U_{1,i}^\varepsilon\) and all
lower flags, while it changes

\[
U_{2,i}\longmapsto
V_i^\varepsilon
=(U_{2,i}\setminus\{c_i^\varepsilon\})\cup\{\alpha\}.
\tag{6.13}
\]

No one coordinate permutation can realize the switch at occurrence
\((i,\varepsilon)\) and simultaneously stabilize the owner of a different
occurrence \((j,\delta)\).  Indeed,

\[
c_i^\varepsilon\in Y_j^\delta
\quad(i,\varepsilon)\ne(j,\delta),
\]

and clean preservation of \(U_{1,i}^\varepsilon\), together with
\(U_{2,i}=U_{1,i}^\varepsilon\cup\{c_i^\varepsilon\}\) and (6.13),
forces

\[
\gamma(c_i^\varepsilon)=\alpha.
\]

This contradicts setwise stabilization of \(Y_j^\delta\), because
\(\alpha\notin Y_j^\delta\).  Thus every choice of one occurrence from
each load-two fibre occupies \(t\) distinct constant-frame seam classes.

Taking \(t=\lfloor H\rfloor\) for \(H=\lceil A\sqrt m\rceil\), condition
(6.9) holds for all sufficiently large \(m\).  This legal catalogue needs
\(\Theta(H)\) typed pieces, while the proposed bound \(O(t/H)\) is
\(O(1)\).

Each displayed cyclic row is a row of a labelled conjugate copy of an
exact local factor on \(Q\): conjugate one fixed factor so that one of its
rows has the order (6.12).  The catalogue is therefore integral and
literal occurrence by occurrence, with distinct central roots and owners.
It is **not** asserted that all these rows coexist in one preassigned
factor \(F_{A_0}\).  Accordingly Proposition 6.3 refutes an owner-local or
labelled-row deterministic compiler; it does not replace the stronger
same-phase direct-path obstruction of Theorem 3.1 and does not rule out a
new multirow exact-factor trade.

## 7. Sharp local freedom and the terminal-state caveat

The component lower bounds above must not be misread as an \(H\)-letter
cost for every lower profile change.  There is exact factorial local
freedom at the boundary scale.

Let

\[
\Sigma_0=(B,\{x_{H-1}\},\ldots,\{x_0\},R)
\]

be an MTF state.  Choose distinct
\(b_0,\ldots,b_{s-1}\in B\) and distinct fresh
\(a_0,\ldots,a_{s-1}\in R\), where \(s\le H\).  For
\(\pi\in S_s\), define

\[
B_r^\pi
=B-\{b_{\pi(0)},\ldots,b_{\pi(r-1)}\}
 +\{a_0,\ldots,a_{r-1}\}.
\tag{7.1}
\]

At principal step \(r\), append

\[
B_{r+1}^\pi=B_r^\pi-b_{\pi(r)}+a_r.
\]

Inductively, the central owners are

\[
X_r=X_0-\{x_0,\ldots,x_{r-1}\}
       +\{a_0,\ldots,a_{r-1}\},
\tag{7.2}
\]

independent of \(\pi\), while the live lower queue is

\[
Q_r^\pi
=(x_r,\ldots,x_{H-1},
  b_{\pi(0)},\ldots,b_{\pi(r-1)}).
\tag{7.3}

Every step is an ordinary one-letter update.  Thus one fixed ordered
\((s+1)\)-owner block has \(s!\) literal histories at zero internal bridge
excess.  At \(s=H\), suitable histories differ on \(H-1\) deepest lower
flags, attaining the order of (6.7).

The terminal base and owner are common, but the terminal queues retain the
\(\pi\)-order of the \(b\)'s.  Therefore (7.1)--(7.3) are not a common
two-port packet.  Chaining the terminal queue classes, or paying the exact
useful-prefix bridge needed to align them, is still necessary.  This local
construction proves that the lower \(\Omega(W/H)\) block scale is sharp;
it does not weaken the upper omitted-phase tower packing theorem, because
all its histories preserve the upper flags.

## 8. Consequence for the requested load-\(2,\ldots,K\) theorem

Consider a final selected corner, not merely the abstract spike cube.  For
each omitted phase \(A_0\), let

\[
\Delta_{A_0}
\]

be the ordinary depth-\(H\) collision descent obtained from old fibres of
load at most \(K\), and let \(r_{A_0}\) be the number of its actually
switched upper spike occurrences.  The proved inequalities are

\[
\Delta_{A_0}\le(K-1)r_{A_0},
\tag{8.1}
\]

\[
L\ge(H+1)r_{A_0},
\tag{8.2}
\]

and, for zero-portal radius-\(H\) pieces,

\[
L\ge(2H+1)r_{A_0}-HP_{A_0}.
\tag{8.3}
\]

Therefore a universal conclusion

\[
P_{A_0}=O(r_{A_0}/H)
\]

does not provide the desired amortization.  Substitution in (8.3) leaves

\[
L=(2-o(1))Hr_{A_0},
\]

not \(O(r_{A_0})\).  Even without residence, (8.2) leaves
\(L\ge(H+1)r_{A_0}\).

In particular, if one phase contains \(r_{A_0}\gg W/H\) moves needed by
the selected bounded-load corner, no literal word of length \(W+o(W)\)
can compile them while retaining the shallower flags.  This remains true
if every lower spike is simultaneously activated on the same owners.

The theorem does **not** prove that every exact factor necessarily has
such a phase-concentrated diffuse sector.  It proves the precise missing
hypothesis in any positive theorem:

1. establish phase dispersion \(\max_{A_0}r_{A_0}=O(W/H)\), with the
   sharper constant required by (8.3);
2. show that the \(\Theta(H)\) filler owners between same-phase switches
   are globally useful principal owners rather than paid padding;
3. construct an integral cross-phase braid with common literal ports; and
4. preserve the lower marker stratification and all earlier flag quotas.

No existing common-owner prefix theorem, spike Gram inequality, or
rainbow binning lemma supplies items 1--3.  Accordingly, the requested
deterministic grouping lemma is sharply refuted at its stated level of
generality, while the cross-phase profile-changing seam route remains
open.

## 9. Audit and implication scope

The decisive steps were independently checked as follows.

1. At depth \(H\), the old upper target contains \(b_i\) and omits
   \(z_i\); every shallower target contains neither.  Exchanging
   \((b_i,z_i)\) with \(A_0\) therefore gives exactly one phase marker at
   depth \(H\), not two.
2. The proof of (3.3) uses avoidance of the whole pair \(A_0\), so it does
   not matter which of its two coordinates is the marker.  There is no
   lost factor two.
3. The last spike in a piece still needs all \(H+1\) owner states of its
   tower.  Hence (0.2) has no path-boundary rebate.
4. Under the transition convention (4.1), the marker is inserted at
   transition \(i+H-1\).  Positive residence (4.2) forbids its removal
   through transition \(i+2H-1\), giving the exact separation
   \(2H+1\) in (4.3).  The weaker bound (0.4) is retained to make the
   conclusion insensitive to a one-step indexing convention.
5. Equation (2.2) was expanded directly from binomial coefficients.  Its
   arrival terms can only reduce descent, so the constant \(K-1\) in
   (2.3) is exact and sharp.
6. The normal form (6.3) accounts for all \(2m-1\) row coordinates.  The
   moving-suffix index is \(r=j+q-t\), producing exactly (6.5), including
   \(t=1\), \(t=m-1\), and empty-intersection boundary cases.
7. The factorial construction (7.1)--(7.3) has a common terminal owner but
   not a common terminal ordered queue.  No two-port conclusion is drawn
   from it.

This report refutes a compiler built from common-owner prefix freezing and
the audited owner-fixed spike charts solely under a bounded fibre-load
hypothesis.  It does not refute a new exact-factor theorem which proves
phase dispersion and realizes a globally useful cross-phase rotor, and it
does not prove or disprove the constant-one conjecture.
