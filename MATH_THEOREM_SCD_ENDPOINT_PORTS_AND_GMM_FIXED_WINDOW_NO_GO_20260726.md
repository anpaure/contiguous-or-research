# SCD endpoint ports: an exact coordinate criterion and a fixed-window GMM no-go

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, or external input
is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom nm,
 \qquad N_r=\binom nr .
\tag{0.1}
\]

The sparse-morphological-preimage theorem shows that, after a wholesale
rewrite, a prescribed middle chronology can be retained while every
physical letter is made small enough to serve as a lower endpoint.  The
remaining issue is whether the lower endpoint flags can be chosen like
the chains of an SCD.  This note gives an exact normal form for that
question and tests the canonical Greene--Kleitman/GMM ordering.

There are four conclusions.

1. Every SCD gives the correct endpoint-radius distribution automatically.
   If the unique chain through the middle owner at endpoint \(t\) has lower
   radius \(h_t\), then

   \[
    \boxed{\#\{t:h_t\ge q\}=\binom n{m-q}.}
   \tag{0.2}
   \]

   Moreover, at depth \(q\), its active endpoints carry every
   rank-\((m-q)\) target exactly once.

2. For an arbitrary nested suffix schedule, the forbidden-interval
   criterion has a sharper **port-block form**.  For a coordinate \(x\),
   only the first target in an endpoint flag which drops \(x\) matters.
   It leaves a port block immediately before its forbidden suffix, and
   that port must escape every other forbidden suffix for \(x\).

3. For a fixed \((H+1)\)-position middle window, every endpoint whose SCD
   radius is at least \(H\) has no start-time freedom: its rank
   \(m,m-1,\ldots,m-H\) witnesses use all \(H+1\) suffixes.  If \(x\)
   is deleted at depth \(d_t(x)\), its port is the singleton

   \[
                 p_t(x)=t-H+d_t(x)-1.               \tag{0.3}
   \]

   Two adjacent endpoints which both delete \(x\) must then satisfy

   \[
                 \boxed{d_{t+1}(x)=d_t(x)-1.}       \tag{0.4}
   \]

   This is the exact coordinatewise staircase condition sought after
   Theorems 5.1 and 6.1 of the baseline-fusion note.

4. The recursive GMM SCD order violates (0.4) at every sufficiently long
   parent block.  In either orientation there are adjacent chains sharing
   a coordinate which is deleted at depths \((1,2)\).  If the checkpoints
   are allowed to separate by inserted physical positions, that pair must
   be separated by at least \(H\) positions.  Consequently every
   checkpoint-faithful fixed-window realization of the GMM order has

   \[
    \boxed{
     L\ge W+(H-1)\binom{2m-1}{m-H-2}-O(H).}
   \tag{0.5}
   \]

   At \(H=A\sqrt m+O(1)\), the binomial factor is

   \[
    \left(\frac14e^{-A^2}+o_A(1)\right)W,           \tag{0.6}
   \]

   so this particular endpoint schedule costs \(\Omega_A(HW)\), not
   \(W+o(W)\).

Thus the abstract SCD radius ledger is exactly right, but the known GMM
order is physically incompatible with the preserved fixed middle windows.
The surviving construction must change the SCD/order, use nonlocal middle
witnesses extending outside the preserved windows, or interleave two
different flag systems.

## 1. The exact SCD-quality endpoint schedule

Let \(\mathscr C\) be any symmetric-chain decomposition of
\(2^{[n]}\).  Every chain has the form

\[
 C_t:
 S_{t,h_t}\subset S_{t,h_t-1}\subset\cdots
 \subset S_{t,1}\subset S_{t,0}\subset\cdots,
 \qquad |S_{t,q}|=m-q,                              \tag{1.1}
\]

where \(S_{t,0}\) is its unique rank-\(m\) member and

\[
                 h_t=m-\min\{|S|:S\in C_t\}.       \tag{1.2}
\]

If a chronology lists every rank-\(m\) set once, assign to its endpoint
\(t\) the unique SCD chain containing that middle owner.  This assignment
does not require the chronology itself to come from the SCD.

### Lemma 1.1 (exact radius census)

For every \(0\le q\le m\),

\[
 \#\{t:h_t\ge q\}=N_{m-q}.                          \tag{1.3}
\]

The targets

\[
 \{S_{t,q}:h_t\ge q\}                              \tag{1.4}
\]

are exactly \(\binom{[n]}{m-q}\), with multiplicity one.

#### Proof

A symmetric chain reaches rank \(m-q\) if and only if its minimum rank is
at most \(m-q\), equivalently if and only if \(h_t\ge q\).  Every such
chain contains exactly one member of that rank.  Since the SCD partitions
the whole Boolean lattice, these members partition the rank.  This proves
both assertions. \(\square\)

Thus an SCD is not merely capacity-correct: it supplies the unique optimal
abstract lower endpoint ledger at every depth simultaneously.  The whole
problem is realization by suffixes of one physical word.

## 2. The port-block form of the forbidden-interval criterion

Fix checkpoint positions \(t\).  At endpoint \(t\), prescribe the nested
targets

\[
 S_{t,0}\supset S_{t,1}\supset\cdots\supset S_{t,\bar h_t},
 \qquad \bar h_t:=\min(h_t,H),                       \tag{2.1}
\]

and nested suffix intervals

\[
 I_{t,q}=[s_{t,q},t],
 \qquad
 s_{t,0}<s_{t,1}<\cdots<s_{t,\bar h_t}.             \tag{2.2}
\]

All intervals are directed intervals in the same linear or cyclic word.
The strict inequalities in (2.2) are necessary because the targets have
distinct ranks.

For a coordinate \(x\), define its first-drop depth at endpoint \(t\) by

\[
 d_t(x)=
 \begin{cases}
  \min\{q:0\le q\le\bar h_t,\ x\notin S_{t,q}\},
       &\text{if this set is nonempty},\\
  \bar h_t+1,&\text{if }x\in S_{t,\bar h_t}.
 \end{cases}                                        \tag{2.3}
\]

When \(d_t(x)\le\bar h_t\), put

\[
 Z_t(x):=I_{t,d_t(x)}.                              \tag{2.4}
\]

This is the longest prescribed interval at endpoint \(t\) whose target
omits \(x\).  Put

\[
 F_x:=\bigcup_{t:d_t(x)\le\bar h_t}Z_t(x),
 \qquad A_x:=[L]\setminus F_x.                      \tag{2.5}
\]

If \(1\le d_t(x)\le\bar h_t\), define the dropout port block

\[
 P_t(x):=I_{t,d_t(x)-1}\setminus I_{t,d_t(x)}
        =[s_{t,d_t(x)-1},s_{t,d_t(x)}-1].            \tag{2.6}
\]

If \(d_t(x)=\bar h_t+1\), define the survivor port block

\[
 P_t(x):=I_{t,\bar h_t}.                            \tag{2.7}
\]

There is no port when \(d_t(x)=0\), because then even the middle target
omits \(x\).

### Theorem 2.1 (exact endpoint-port criterion)

The target/interval data admit a set-valued word realizing every
\(S_{t,q}\) if and only if

\[
 \boxed{
 P_t(x)\cap A_x\ne\varnothing
 \quad\text{for every }(t,x)\text{ with }d_t(x)\ge1.}
\tag{2.8}
\]

They admit such a word with every physical letter nonempty if and only if,
in addition,

\[
 \boxed{\bigcup_{x\in[n]}A_x=[L].}                 \tag{2.9}
\]

#### Proof

For a fixed endpoint and coordinate, membership down the SCD flag is an
initial segment in \(q\).  Consequently all absent-target intervals at
that endpoint are contained in the first one, \(Z_t(x)\), so (2.5) is
exactly the forbidden set from Theorem 5.1 of the baseline-fusion note.

Suppose first that \(1\le d=d_t(x)\le\bar h_t\).  The shortest interval
whose target still contains \(x\) is \(I_{t,d-1}\), and

\[
 I_{t,d-1}=P_t(x)\,\dot\cup\,Z_t(x).                \tag{2.10}
\]

The second term lies in \(F_x\).  Hence
\(I_{t,d-1}\cap A_x\ne\varnothing\) is equivalent to
\(P_t(x)\cap A_x\ne\varnothing\).  Every earlier present-target interval
contains \(I_{t,d-1}\), so it gives no additional condition.

If \(d_t(x)=\bar h_t+1\), there is no absent target at this endpoint and
the shortest present-target interval is (2.7), giving the same condition.
If \(d_t(x)=0\), no target at this endpoint contains \(x\).

Thus (2.8) is exactly the coordinatewise forbidden-interval criterion.
The nonempty-letter assertion is exactly its maximal-realization condition
\(\bigcup_xA_x=[L]\). \(\square\)

Theorem 2.1 removes all set-valued ambiguity.  A proposed SCD schedule is
valid precisely when every dropout/survivor port escapes the union of the
first-zero suffixes for the same coordinate.

## 3. Fixed windows force singleton ports and staircases

To expose ranks \(m,m-1,\ldots,m-H\) at one endpoint requires \(H+1\)
distinct suffix unions.  Accordingly, the exact fixed-window version of
the wholesale preimage uses

\[
 M_t=S_{t,0}=\bigcup_{j=t-H}^{t}Q_j.                \tag{3.1}
\]

This is the natural one-position extension of Theorem 6.1 of the
baseline-fusion note.  More explicitly, apply that theorem with window
parameter \(H+1\).  It first gives seed letters of size at most
\(m-H-1\).  At position \(t\), every coordinate in

\[
 D_t^+=\bigcap_{s=t}^{t+H}M_s                              \tag{3.1a}
\]

may be added to \(Q_t\) without changing any of the represented middle
windows; consecutive Johnson adjacency gives \(|D_t^+|\ge m-H\).
Therefore the seed letters may be enlarged, as the endpoint assignment
requires, up to the eligible cap \(m-H\).  The upper dilation tower is
still determined by unions of the unchanged middle windows.  This
enlargement freedom is not itself a construction of the lower flags--it
is exactly the freedom tested below.

The one-position reindexing is necessary: an \(H\)-position window has
only \(H\) nonempty suffixes and therefore cannot display all \(H+1\)
ranks from \(m\) through \(m-H\).

### Lemma 3.1 (full-radius starts are forced)

Suppose \(h_t\ge H\), the fixed middle witness is (3.1), and all lower
witnesses are suffixes contained in that same window.  Then necessarily

\[
 I_{t,q}=[t-H+q,t]
 \qquad(0\le q\le H).                               \tag{3.2}
\]

#### Proof

There are precisely \(H+1\) nonempty suffixes of the window in (3.1).
The \(H+1\) prescribed targets have distinct cardinalities, hence require
distinct suffixes.  Their inclusion order fixes the correspondence, giving
(3.2). \(\square\)

Under (3.2), a coordinate first deleted at depth
\(1\le d_t(x)\le H\) has

\[
 P_t(x)=\{p_t(x)\},
 \qquad p_t(x):=t-H+d_t(x)-1,                       \tag{3.3}
\]

and

\[
 Z_t(x)=(p_t(x),t].                                 \tag{3.4}
\]

All intervals are directed; in a linear chart (3.4) is
\([p_t(x)+1,t]\).

### Theorem 3.2 (dropout-arc/staircase law)

In every realizable fixed-window schedule:

1. every dropout boundary obeys

   \[
                     p_t(x)\notin\bigcup_u Z_u(x);  \tag{3.5}
   \]

2. if \([a,b]\) is the positive middle-residence run of \(x\) containing
   \(t\), then

   \[
    a\le p_t(x)\le b-H,                             \tag{3.6}
   \]

   or equivalently

   \[
    H+1+a-t\le d_t(x)\le b+1-t;                    \tag{3.7}
   \]

3. for two dropout endpoints \(t<u\) in one linear residence chart,

   \[
    \boxed{p_u(x)=p_t(x)\quad\text{or}\quad p_u(x)>t;}             \tag{3.8}
   \]

4. in particular, if \(u=t+1\), then

   \[
    \boxed{d_{t+1}(x)=d_t(x)-1.}                    \tag{3.9}
   \]

Thus the dropout arcs for one coordinate occur in packets with a common
left boundary, or in disjoint chronological packets.  Within a packet,
successive endpoint deletion labels descend by one.

#### Proof

Part 1 is Theorem 2.1 with the singleton port (3.3).

Every endpoint \(u\) with \(x\notin M_u\) contributes its full middle
window \([u-H,u]\) to \(F_x\).  A position escapes all such windows if
and only if the entire endpoint interval \([p,p+H]\) lies in a positive
middle-residence run of \(x\).  For the run \([a,b]\), this is exactly
\(a\le p\le b-H\).  Substitution of (3.3) gives (3.7).

For part 3, suppose first that \(p_u<p_t\).  Since
\(p_t\le t<u\), one has \(p_t\in(p_u,u]=Z_u(x)\), contradicting
(3.5).  If \(p_t<p_u\le t\), then
\(p_u\in(p_t,t]=Z_t(x)\), again a contradiction.  The only possibilities
are equality or \(p_u>t\), proving (3.8).

If \(u=t+1\), then \(d_u(x)\le H\) gives

\[
 p_u=u-H+d_u-1=t-H+d_u\le t,                        \tag{3.10}
\]

so the disjoint alternative is impossible.  Equality of (3.3) at the two
endpoints is precisely \(d_{t+1}=d_t-1\). \(\square\)

More generally, if \(u-t=\Delta\), equality of ports gives

\[
 d_u=d_t-\Delta,                                    \tag{3.11}
\]

while the disjoint alternative requires

\[
 \Delta\ge H-d_u+2.                                 \tag{3.12}
\]

This quantitative form prices inserted positions exactly.

### Corollary 3.3 (residence-diagonal condition)

Let \(\partial_d(C_t)\) be the coordinate deleted at depth \(d\) in the
assigned SCD chain at a full-radius endpoint \(t\).  Every realizable
fixed-window schedule satisfies

\[
 \boxed{
  \partial_d(C_t)\in
  \bigcap_{s=t-H+d-1}^{\,t+d-1}M_s
  \qquad(1\le d\le H).}
\tag{3.13}
\]

Thus the first-deleted coordinate must already have resided in the middle
chronology for \(H\) preceding transitions, while the last-deleted
coordinate must survive for \(H-1\) following transitions.  The whole
deletion list must lie on the diagonal interpolation between these two
requirements.

#### Proof

For \(x=\partial_d(C_t)\), its forced port is
\(p=t-H+d-1\).  By (3.6), the complete interval \([p,p+H]\) lies in one
positive middle-residence run of \(x\).  Since
\(p+H=t+d-1\), this is exactly (3.13). \(\square\)

Condition (3.13) is often the fastest way to reject a proposed ordering:
it uses only the middle chronology and the SCD deletion labels, before
the survivor ports or the nonempty-letter condition are inspected.

## 4. The recursive GMM order violates the staircase law

Write a saturated symmetric chain as

\[
 C=(L;z_1,\ldots,z_{2r+1}),                         \tag{4.1}
\]

where \(r\) is its lower radius.  Its middle member and deletion order are

\[
 M(C)=L+z_1+\cdots+z_r,
 \qquad
 \partial_j(C)=z_{r-j+1}.                           \tag{4.2}
\]

Here \(\partial_j(C)\) is the coordinate present at depth \(j-1\) and
deleted on passing to depth \(j\).

The first-star and last-star children are

\[
 f(C)=(L+z_2;z_3,\ldots,z_{2r+1}),                  \tag{4.3}
\]

\[
 \ell(C)=(L+z_{2r+1};z_1,\ldots,z_{2r-1}).          \tag{4.4}
\]

### Lemma 4.1 (the two directed GMM violations)

If \(r\ge2\), then:

1. \(C\to f(C)\) has a shared coordinate \(z_r\) with deletion depths
   \((1,2)\);
2. \(\ell(C)\to C\) has a shared coordinate \(z_{r-1}\) with deletion
   depths \((1,2)\).

#### Proof

In \(C\), the coordinate \(z_r\) is deleted first.  The middle member of
\(f(C)\) is

\[
 L+z_2+z_3+\cdots+z_{r+1}.                          \tag{4.5}
\]

Its downward deletion order begins \(z_{r+1},z_r\), so \(z_r\) is
deleted second.

The middle member of \(\ell(C)\) is

\[
 L+z_{2r+1}+z_1+\cdots+z_{r-1}.                    \tag{4.6}
\]

Thus \(z_{r-1}\) is deleted first there, while (4.2) deletes it second in
\(C\). \(\square\)

The odd-dimensional recursive GMM order replaces every ordinary parent
chain in dimension \(2m-1\) by

\[
 A,\quad \ell(A),\quad \ell(f(A)),\quad f(A)        \tag{4.7}
\]

or its reverse.  Since \(\ell(f(A))=f(\ell(A))\), the displayed
orientation contains the directed boundary

\[
 \ell(A)\longrightarrow f(\ell(A)),                \tag{4.8}
\]

of type 1 in Lemma 4.1.  The reverse orientation contains

\[
 \ell(A)\longrightarrow A,                         \tag{4.9}
\]

of type 2.

A parent of minimum rank \(a\) has all relevant chains reaching rank
\(m-H\) whenever

\[
                         a\le m-H-2.                \tag{4.10}
\]

The number of such parents is exactly

\[
 B_{m,H}=\binom{2m-1}{m-H-2}.                       \tag{4.11}
\]

### Theorem 4.2 (fixed-window GMM checkpoint lower bound)

Consider a cyclic checkpoint-faithful realization of the recursive GMM
chain order, where \(H\ge2\).  Assume every chain of radius at least \(H\) exposes its
rank \(m,m-1,\ldots,m-H\) targets by suffixes inside its preserved
\((H+1)\)-position middle window.  If its physical length is \(L\), then

\[
 \boxed{L\ge W+(H-1)B_{m,H}-O(H).}                  \tag{4.12}
\]

In particular, no such schedule has length \(W+o(W)\) for any
\(H\to\infty\) with \(H=O(\sqrt m)\) and
\(B_{m,H}=\Omega(W)\).

#### Proof

For every parent counted by (4.11), equations (4.8)--(4.9) and Lemma 4.1
give two consecutive chain checkpoints with a shared coordinate whose
deletion depths are \((1,2)\).  If their checkpoint positions differ by
\(\Delta\), the equal-port alternative (3.11) is impossible, while
(3.12) with \(d_u=2\) gives

\[
                         \Delta\ge H.               \tag{4.13}
\]

Every ordinary gap between distinct middle checkpoints is at least one.
The bad gaps belong to disjoint parent blocks, so summing the cyclic gaps
adds at least \(H-1\) beyond the ordinary unit cost for each counted
parent.  Opening the cyclic order can lose only one such gap, producing
the harmless \(O(H)\) term.  This proves (4.12). \(\square\)

For fixed \(A>0\) and \(H=A\sqrt m+O(1)\), the elementary central-binomial
ratio gives

\[
 \frac{B_{m,H}}W
 =\left(\frac14+o_A(1)\right)e^{-A^2}.              \tag{4.14}
\]

Therefore (4.12) is much stronger than a positive-density excess in this
fixed-window model: its lower bound is \(\Omega_A(\sqrt m\,W)\).

## 5. Exact surviving target

The obstruction is deliberately scoped.  It does not rule out:

1. a different SCD;
2. a different order of its middle owners;
3. lower witnesses whose middle suffix starts before the preserved
   \((H+1)\)-window;
4. two coherently interleaved SCDs; or
5. a wholesale schedule not checkpoint-faithful to one SCD.

For any one-SCD fixed-window attempt, however, Theorem 3.2 supplies a
sharp local screen.  A candidate ordering must satisfy:

> **Staircase-compatible SCD ordering.** For every pair of adjacent
> full-radius endpoints and every coordinate deleted in both lower flags,
> the deletion depth at the second endpoint is exactly one less than at
> the first.  More generally, its dropout arcs must split into
> equal-left-endpoint packets separated by disjoint gaps, and every
> survivor port and every physical position must satisfy (2.8)--(2.9).

The radius census (1.3) proves that such an ordering would have exactly
the correct annular capacity.  Theorem 4.2 proves that the known recursive
GMM order is not such an ordering.  Finding a noncanonical ordering with
only \(o(W)\) violations, or proving that every SCD ordering has a
positive-density family of violations, is the precise next problem.

## 6. Status

Proved here:

1. the exact SCD endpoint-radius and target census;
2. the port-block reformulation of the forbidden-interval criterion;
3. the fixed-window singleton-port and dropout-staircase laws;
4. the explicit \((1,2)\) deletion-depth defect at both orientations of
   every long GMM parent block; and
5. the quantitative fixed-window GMM lower bound (4.12).

Not proved here:

1. existence of a noncanonical staircase-compatible SCD ordering;
2. a universal obstruction covering all SCDs/orders;
3. realization by longer, nonlocal middle suffixes; or
4. coefficient one.

The concrete advance is that the lower endpoint problem is no longer an
unstructured set-valued compatibility question.  It is a coordinatewise
port-escape problem, and the first canonical SCD/GMM schedule fails by an
explicit family of singleton-port collisions.
