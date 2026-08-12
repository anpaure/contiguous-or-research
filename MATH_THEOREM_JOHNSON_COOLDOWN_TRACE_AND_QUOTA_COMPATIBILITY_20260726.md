# Johnson cooldown, trace transport, and common quota compatibility

Date: 2026-07-26

Method: pure mathematics only; no finite search or computation.

## 0. Outcome

Let

\[
 C=(X_i)_{i\in\mathbb Z/L\mathbb Z}
\]

be a cycle in \(J(2m,m)\), written

\[
 X_{i+1}=X_i-a_i+b_i,
 \qquad a_i\in X_i,\quad b_i\notin X_i,
 \qquad D_i=\{a_i,b_i\}.
\]

Call the cycle **\(H\)-delayed** when every \(H\) consecutive transition
supports \(D_i,\ldots,D_{i+H-1}\) are pairwise disjoint.  Thus a coordinate
may recur at separation \(H\), but not sooner.

The universal delay bound is sharp:

\[
                         H\le m.                    \tag{0.1}
\]

Equality is completely rigid.  Every component then has length exactly
\(2m\); its first \(m\) transition supports form a perfect matching of the
\(2m\) coordinates, and the second half repeats the same matching in the
same order with every exchange reversed.  Consequently no Hamilton cycle
of \(J(2m,m)\) is \(m\)-delayed for \(m\ge2\), and an \(m\)-delayed spanning
2-factor can exist only if

\[
                         2m\mid\binom{2m}{m}.        \tag{0.2}
\]

This is not an obstruction at \(H\asymp\sqrt{m\log m}\): delay alone has
linear headroom.  Its useful consequence is instead an exact common-owner
compatibility law.  For a Hamilton cycle let \(t_x\) be the number of
cyclic membership runs of coordinate \(x\).  Then, simultaneously for
every \(q\le H\),

\[
\begin{aligned}
 \sum_{T\ni x}\ell_q^-(T)&={W\over2}-qt_x,\\
 \sum_{T\ni x}\ell_q^+(T)&={W\over2}+qt_x,
 \qquad W=\binom{2m}{m}.                            \tag{0.3}
\end{aligned}
\]

Thus all depths and both signs have one common affine point-degree vector;
balanced quota families cannot be chosen independently.  Sections 4--6
give the exact compatibility equations, an \(L^1\) separation inequality,
and an unconditional support-defect bound.

## 1. Return-free windows and the sharp delay bound

For \(1\le q\le H\), put

\[
 I_{i,q}=\bigcap_{j=0}^{q}X_{i+j},\qquad
 U_{i,q}=\bigcup_{j=0}^{q}X_{i+j}.                  \tag{1.1}
\]

### Lemma 1.1 (literal geodesic windows)

Every \(q\)-window is return-free and

\[
 I_{i,q}=X_i\setminus\{a_i,\ldots,a_{i+q-1}\},
 \qquad
 U_{i,q}=X_i\cup\{b_i,\ldots,b_{i+q-1}\}.          \tag{1.2}
\]

In particular,

\[
                         |I_{i,q}|=m-q,qquad
                         |U_{i,q}|=m+q.              \tag{1.3}
\]

#### Proof

The \(2q\) coordinates in
\(D_i\cup\cdots\cup D_{i+q-1}\) are distinct.  A coordinate removed at a
later transition has not appeared earlier in the window, so it was already
present in \(X_i\).  An inserted coordinate was absent from \(X_i\), and
cannot be removed within the window.  This proves (1.2) and (1.3). \(\square\)

### Proposition 1.2 (sharp cooldown bound)

Every \(H\)-delayed cycle satisfies \(H\le m\).

#### Proof

One block of \(H\) transitions uses \(2H\) distinct coordinates, all in a
ground set of size \(2m\). \(\square\)

The convention sometimes called “strict delay \(H\)” forbids recurrence at
separation \(H\) as well.  Under that convention, apply Proposition 1.2 to
\(H+1\) consecutive transitions and obtain \(H\le m-1\).  All remaining
statements use the block convention stated above.

## 2. Equality classification

### Theorem 2.1 (all \(m\)-delayed components)

If \(C\) is \(m\)-delayed, then \(L=2m\).  After a cyclic shift, there are
pairwise disjoint pairs

\[
 P_j=\{u_j,v_j\},\qquad j=0,\ldots,m-1,             \tag{2.1}
\]

partitioning \([2m]\), such that

\[
 D_j=D_{j+m}=P_j,qquad
 (a_{j+m},b_{j+m})=(b_j,a_j).                       \tag{2.2}
\]

The initial vertex contains exactly one endpoint of every \(P_j\).  The
first half of the cycle flips the pairs in the order
\(P_0,\ldots,P_{m-1}\), and the second half flips the same pairs in the same
order back to the initial choices.  Conversely, every ordered perfect
matching and every choice of one initial endpoint per pair gives such an
\(m\)-delayed \(2m\)-cycle.

#### Proof

Every block \(D_i,\ldots,D_{i+m-1}\) consists of \(m\) disjoint pairs and
therefore partitions \([2m]\).  Compare this block with the block beginning
at \(i+1\).  Their common \(m-1\) supports cover
\([2m]\setminus D_i\), so the new support must be

\[
                         D_{i+m}=D_i.                \tag{2.3}
\]

During the first \(m\) transitions every coordinate is toggled exactly
once.  Hence

\[
                         X_{i+m}=[2m]\setminus X_i.  \tag{2.4}
\]

At time \(i+m\), membership on the pair \(D_i\) is reversed, and (2.3)
therefore forces the reversed orientation in (2.2).  It follows that
\(X_{i+2m}=X_i\).

The cyclic component has at least \(m\) transitions, because an
\(m\)-block must contain \(m\) different supports.  Its minimal period
divides \(2m\), while (2.4) shows that it does not divide \(m\).  The only
divisor of \(2m\) which is larger than or equal to \(m\) and does not divide
\(m\) is \(2m\).  Thus \(L=2m\).  The remaining assertions are immediate
from (2.2)--(2.4).

For the converse, exchange the present endpoint with the absent endpoint
inside \(P_0,\ldots,P_{m-1}\) in order, and then perform the reverse
exchanges on the same pairs in the same order.  Every \(m\)-transition
block contains every pair support once,
so the resulting cycle is \(m\)-delayed; the first and second visits to a
pair have opposite orientations, and the \(2m\) states are distinct by the
same active-pair description used in Proposition 2.3.  This also proves
that (0.1) is sharp for every \(m\). \(\square\)

### Corollary 2.2 (Hamilton and divisibility consequences)

For \(m\ge2\), \(W=\binom{2m}{m}>2m\), so an \(m\)-delayed Hamilton cycle
does not exist.  Every component of an \(m\)-delayed spanning 2-factor has
size \(2m\), proving the necessary divisibility condition (0.2).

### Proposition 2.3 (intracomponent trace injectivity at equality)

On an \(m\)-delayed component, each of the maps

\[
 i\longmapsto I_{i,q},\qquad i\longmapsto U_{i,q}   \tag{2.5}
\]

is injective for every \(1\le q<m\).  At \(q=m\), all lower traces are
empty and all upper traces are \([2m]\).

#### Proof

Relative to the fixed pairing (2.1), a lower \(q\)-trace contains neither
endpoint of the \(q\) consecutive active pairs and exactly one endpoint of
every inactive pair.  Its zero pairs recover the active cyclic \(q\)-block.
The \(m\) such blocks are distinct for \(q<m\).  Starts separated by \(m\)
have the same active pair block but complementary choices on every inactive
pair, of which there is at least one.  Thus all \(2m\) lower traces are
different.  The upper proof is identical, with two endpoints on active
pairs and one on inactive pairs.  The assertion at \(q=m\) follows from
(2.4). \(\square\)

This proposition is an important scope check: large delay does not itself
create shallow trace collisions.  The difficulty is global target
allocation among components.

## 3. Transport of the trace cycles

### Theorem 3.1 (shifted-direction trace recurrence)

For \(1\le q\le H-1\), consecutive traces are Johnson neighbors and obey

\[
\begin{aligned}
 I_{i+1,q}&=I_{i,q}-a_{i+q}+b_i,\\
 U_{i+1,q}&=U_{i,q}-a_i+b_{i+q}.                    \tag{3.1}
\end{aligned}
\]

Moreover, each trace walk is \((H-q)\)-delayed: every \(H-q\) consecutive
lower trace transitions use distinct coordinates, and the same is true on
the upper side.

#### Proof

The \(q+1\) supports \(D_i,\ldots,D_{i+q}\) are disjoint.  Apply (1.2) at
starts \(i\) and \(i+1\).  The lower window loses the new terminal removal
\(a_{i+q}\) and gains the expired initial insertion \(b_i\); the upper
window loses \(a_i\) and gains \(b_{i+q}\).  This proves (3.1).

A block of \(H-q\) lower trace transitions uses coordinates of the form

\[
 b_i,\ldots,b_{i+H-q-1},qquad
 a_{i+q},\ldots,a_{i+H-1}.                          \tag{3.2}
\]

They are all drawn, with no repetition, from the disjoint transition
supports \(D_i,\ldots,D_{i+H-1}\).  The upper statement is symmetric.
\(\square\)

Thus delay is inherited by the complete nested lower and upper trace
walks, with the exact loss of \(q\) units.  No marginal re-selection of
depths is present in this identity.

### Theorem 3.2 (nested Euler--Johnson tower)

Let an \(H\)-delayed spanning \(2\)-factor be oriented componentwise, and
let \(\ell_q^\pm\) denote its trace loads.  For
\(1\le q\le H-1\), form the lower trace multigraph \(G_q^-\) by putting
one edge

\[
                         I_{i,q}I_{i+1,q}                  \tag{3.3}
\]

for every start \(i\) on every component.  Then \(G_q^-\) is a loopless
multigraph on \(\binom{[2m]}{m-q}\) with all degrees even (equivalently,
every nontrivial component is Eulerian), and

\[
\begin{aligned}
 d_{G_q^-}(T)&=2\ell_q^-(T),\\
 \#\{e:e\text{ has intersection }K\}&=\ell_{q+1}^-(K),\\
 \#\{e:e\text{ has union }P\}&=\ell_{q-1}^-(P).
\end{aligned}                                             \tag{3.4}
\]

Here \(\ell_0^-(X)=1\).  On the upper side, the analogous multigraph
\(G_q^+\) on \(\binom{[2m]}{m+q}\) satisfies

\[
\begin{aligned}
 d_{G_q^+}(T)&=2\ell_q^+(T),\\
 \#\{e:e\text{ has intersection }K\}&=\ell_{q-1}^+(K),\\
 \#\{e:e\text{ has union }P\}&=\ell_{q+1}^+(P),
\end{aligned}                                             \tag{3.5}
\]

with \(\ell_0^+(X)=1\).

#### Proof

The recurrence (3.1) shows that consecutive traces are distinct Johnson
neighbors.  Directly from (1.2),

\[
\begin{aligned}
 I_{i,q}\cap I_{i+1,q}&=I_{i,q+1},&
 I_{i,q}\cup I_{i+1,q}&=I_{i+1,q-1},\\
 U_{i,q}\cap U_{i+1,q}&=U_{i+1,q-1},&
 U_{i,q}\cup U_{i+1,q}&=U_{i,q+1}.              \tag{3.6}
\end{aligned}
\]

Every occurrence of a trace vertex has one preceding and one following
edge on its oriented factor component, proving the degree identities.
As \(i\) ranges cyclically, (3.6) proves all four edge-colour
multiplicity identities. \(\square\)

There is an exact integral transport form.  On the lower side, put
\(k=m-q\).  A Johnson edge on rank \(k\) is uniquely determined by its
intersection \(K\in\binom{[2m]}{k-1}\) and union
\(P\in\binom{[2m]}{k+1}\), with \(K\subset P\).  Hence the three
marginals in (3.4) can occur in some multigraph if and only if there are
integers \(z_{K,P}\ge0\), indexed by \(K\subset P\), \(|P\setminus K|=2\),
such that

\[
\boxed{\begin{aligned}
 \sum_{P\supset K}z_{K,P}&=\ell_{q+1}^-(K),\\
 \sum_{K\subset P}z_{K,P}&=\ell_{q-1}^-(P),\\
 \sum_{K\subset T\subset P}z_{K,P}&=2\ell_q^-(T).
\end{aligned}}                                           \tag{3.7}
\]

Necessity follows from (3.4).  Conversely, \(z_{K,P}\) parallel copies
of the unique edge between the two intermediate \(k\)-sets give the
required multigraph.  There is an identical upper transport with the
roles of \(q-1\) and \(q+1\) interchanged as in (3.5).

In particular, (3.7) implies genuine capacitated Hall cuts.  For every
\(\mathcal S\subseteq\binom{[2m]}{m-q}\),

\[
\boxed{\begin{aligned}
 2\sum_{T\in\mathcal S}\ell_q^-(T)
 &\le
 \sum_K\ell_{q+1}^-(K)
       \min\{2,|\{T\in\mathcal S:K\subset T\}|\},\\
 2\sum_{T\in\mathcal S}\ell_q^-(T)
 &\le
 \sum_P\ell_{q-1}^-(P)
       \min\{2,|\{T\in\mathcal S:T\subset P\}|\}.
\end{aligned}}                                           \tag{3.8}
\]

Indeed, group the degree incidences of \(\mathcal S\) first by edge
intersection and then by edge union.  Each edge contributes at most the
displayed truncated incidence.  The upper trace has the two analogous
cuts obtained from (3.5).

Equations (3.7)--(3.8) are necessary at every depth simultaneously.
They are not by themselves a chronology theorem: independently chosen
multigraphs \(G_q^\pm\) need not admit one common edge indexing and one
common system of Euler circuits descending to the middle \(2\)-factor.
That common chronological lift is the remaining integral gate.

## 4. Exact point-degree laws

For a coordinate \(x\), let

\[
 s_x=\#\{i:x\in X_i\}                               \tag{4.1}
\]

and let \(t_x\) be the number of cyclic one-runs of the membership word
\(1_{x\in X_i}\), equivalently the number of removals of \(x\), or the
number of insertions of \(x\).  A constant membership word has \(t_x=0\).

### Theorem 4.1 (point-degree ledger on an arbitrary delayed cycle)

For every \(q\le H\),

\[
\begin{aligned}
 \#\{i:x\in I_{i,q}\}&=s_x-qt_x,\\
 \#\{i:x\in U_{i,q}\}&=s_x+qt_x.                  \tag{4.2}
\end{aligned}
\]

#### Proof

Successive uses of coordinate \(x\) are separated by at least \(H\)
transitions.  Hence every nonconstant one-run and zero-run has length at
least \(H\).  A one-run of length \(r\) contains exactly \(r-q\) starts of
\((q+1)\)-state windows lying wholly in that run.  Summing over the \(t_x\)
one-runs gives \(s_x-qt_x\), which is the first equation.

The union fails to contain \(x\) precisely on a window lying wholly in a
zero-run.  Those starts number \((L-s_x)-qt_x\); subtracting from the \(L\)
starts gives the second equation.  The constant cases follow directly and
obey the same formulas. \(\square\)

For a Hamilton cycle all middle vertices occur once, so

\[
 s_x={W\over2},qquad \sum_{x=1}^{2m}t_x=W.         \tag{4.3}
\]

Every one-run and zero-run has length at least \(H\), whence

\[
                         0<t_x\le {W\over2H}.        \tag{4.4}
\]

Writing \(\ell_q^\pm\) for the signed trace loads, (4.2) now becomes the
announced identity (0.3).  In particular the same integer vector
\((t_x)_x\) controls all protected depths.

## 5. Exact balanced-quota compatibility

Put

\[
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q},\qquad
 f_q=\left\lfloor{W\over N_q}\right\rfloor,
 \qquad r_q=W-f_qN_q.                              \tag{5.1}
\]

An exact balanced signed quota vector has load \(f_q+1\) on a bonus family
\(\mathcal B_q^\pm\) of size \(r_q\), and load \(f_q\) elsewhere.  Define
its centered point degrees by

\[
\begin{aligned}
 \delta_{q,x}^-&=\deg_{\mathcal B_q^-}(x)
                 -{r_q(m-q)\over2m},\\
 \delta_{q,x}^+&=\deg_{\mathcal B_q^+}(x)
                 -{r_q(m+q)\over2m}.               \tag{5.2}
\end{aligned}
\]

### Theorem 5.1 (common affine quota line)

If one \(H\)-delayed Hamilton cycle realizes prescribed exact balanced
quota families at every \(q\le H\), then there are integers \(t_x\) obeying
(4.3)--(4.4) such that, for every \(x\) and every \(q\le H\),

\[
 \boxed{
 \delta_{q,x}^-=-q\left(t_x-{W\over2m}\right),
 \qquad
 \delta_{q,x}^+= q\left(t_x-{W\over2m}\right).}    \tag{5.3}
\]

Equivalently,

\[
 -{\delta_{q,x}^-\over q}
 ={\delta_{q,x}^+\over q}
 =t_x-{W\over2m}                                  \tag{5.4}
\]

is independent of the depth and the sign.

#### Proof

The number of rank-\((m-q)\) targets containing \(x\) is
\(N_q(m-q)/(2m)\).  Therefore the prescribed lower point load is

\[
 f_q{N_q(m-q)\over2m}+\deg_{\mathcal B_q^-}(x)
 ={W(m-q)\over2m}+\delta_{q,x}^-.                  \tag{5.5}
\]

Equate (5.5) with \(W/2-qt_x\) from (0.3).  This gives the first equation
in (5.3).  The upper calculation uses \(N_q(m+q)/(2m)\) and
\(W/2+qt_x\), giving the second. \(\square\)

Thus independently balanced quota families are generally incompatible
with a common cycle even before chronology, connectivity, or absorption
is considered.  When \(r_q=0\) for one protected depth, (5.3) forces
\(t_x=W/(2m)\) for every coordinate, and in particular forces
\(2m\mid W\).

### Theorem 5.2 (quantitative \(L^1\) quota cut)

Let \(\beta_q^\pm\) be arbitrary prescribed balanced quota vectors with
centered bonus degrees \(\delta_{q,x}^\pm\), and let \(\ell_q^\pm\) be the
loads of an \(H\)-delayed Hamilton cycle.  Put

\[
 E_q^\pm=\sum_T|\ell_q^\pm(T)-\beta_q^\pm(T)|,
 \qquad v_x=t_x-{W\over2m}.                         \tag{5.6}
\]

Then

\[
\boxed{\begin{aligned}
 E_q^-&\ge {1\over m-q}\sum_x|qv_x+\delta_{q,x}^-|,\\
 E_q^+&\ge {1\over m+q}\sum_x|qv_x-\delta_{q,x}^+|.
\end{aligned}}                                      \tag{5.7}
\]

Consequently any common choice through \(H\) obeys the sum of (5.7) over
all protected depths, minimized over integer vectors \((t_x)\) satisfying
(4.3)--(4.4).

#### Proof

For the lower sign, the discrepancy between the actual and prescribed
point loads at \(x\) is \(-qv_x-\delta_{q,x}^-\).  On the other hand it is
also

\[
 \sum_{T\ni x}(\ell_q^-(T)-\beta_q^-(T)).           \tag{5.8}
\]

Sum the absolute values of (5.8) over \(x\).  A target discrepancy is
counted at most \(m-q\) times, giving the first inequality.  The upper
proof is identical, with point discrepancy \(qv_x-\delta_{q,x}^+\) and
target size \(m+q\). \(\square\)

For example, two lower quota families at depths \(q,r\) necessarily
satisfy

\[
 {m-q\over q}E_q^-+{m-r\over r}E_r^-
 \ge\sum_x\left|{\delta_{q,x}^-\over q}
                 -{\delta_{r,x}^-\over r}\right|. \tag{5.9}
\]

There is a symmetric cross-sign inequality with the difference in (5.9)
replaced by
\(\delta_{q,x}^-/q+\delta_{r,x}^+/r\).

## 6. Honest support consequence

Let

\[
 M_q^\pm=N_q-|\operatorname{supp}\ell_q^\pm|        \tag{6.1}
\]

be the number of uncovered signed targets.  The point ledger alone yields
the following necessary bound.

### Theorem 6.1 (point-cut support deficit)

For every \(q\le H\),

\[
 \boxed{
 M_q^\pm\ge {1\over2m}\sum_{x=1}^{2m}
 \left(q\left|t_x-{N_q\over2m}\right|
             -{W-N_q\over2}\right)_+.}             \tag{6.2}
\]

#### Proof

Fix \(x\).  For the lower sign, let

\[
 A={N_q(m-q)\over2m},\qquad D={W\over2}-qt_x.       \tag{6.3}
\]

There are \(A\) targets containing \(x\), while at most \(D\) supported
targets containing \(x\), since each supported target consumes at least
one occurrence.  There are \(N_q-A\) targets avoiding \(x\), while at most
\(W-D\) supported targets avoiding it.  Hence the number of missing targets
in the two classes is at least

\[
 (A-D)_+ + (N_q-A-W+D)_+.                           \tag{6.4}
\]

Writing \(\Delta=W-N_q\), expression (6.4) is

\[
 \left(q\left|t_x-{N_q\over2m}\right|-{\Delta\over2}\right)_+.
                                                               \tag{6.5}
\]

For each fixed \(x\), every missing target lies in exactly one of the two
classes.  Summing (6.4) over all \(2m\) coordinates counts every missing
target exactly \(2m\) times on the left and proves (6.2).  For the upper
sign use \(A=N_q(m+q)/(2m)\) and \(D=W/2+qt_x\); the same expression
(6.5) results. \(\square\)

Bound (6.2) is sometimes a genuine linear Hall cut, but it is not a
universal obstruction in the regime \(H=o(m)\).  The tolerance
\((W-N_q)/(2q)\) can contain all feasible point-run degrees.  Therefore no
existence or nonexistence conclusion at
\(H\asymp\sqrt{m\log m}\) follows from cooldown and point degrees alone.

## 7. Verified boundary

The unconditional conclusions are:

1. \(H\le m\), with the complete \(H=m\) component classification;
2. exact return-free ranks and shifted Johnson trace recurrences;
3. inherited trace cooldown \(H-q\);
4. the all-depth, two-sign point ledger (0.3);
5. the common affine balanced-quota condition (5.3);
6. the quantitative quota and support cuts (5.7) and (6.2).

They do not construct a Hamilton cycle at growing delay, nor do they
exclude one for \(H=o(m)\).  A positive theorem still needs a Hamilton or
spanning-2-factor construction whose common run vector and full target
histograms meet the affine compatibility while preserving cross-depth
row/column slack.  A negative theorem must use structure beyond the
universal cooldown ledger proved here.
