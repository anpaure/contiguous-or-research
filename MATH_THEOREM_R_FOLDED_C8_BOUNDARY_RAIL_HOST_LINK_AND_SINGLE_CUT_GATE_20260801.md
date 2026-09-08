# Folded-C8 minimal hosts force an internal link run; one cut cannot serve two independent aligned hosts

Date: 2026-08-01  
Lane: R, quotient-folded C8 physical host  
Status: exact all-`d` obstruction for two independent full-window hosts, and
an exact sufficient interface for the surviving coupled endpoint rail.  No
existence of that endpoint rail in a Pascal child is claimed.

## 0. Result

Let a cyclic rank-`r` Johnson owner word be compiled at depth `d>=2`.  If a
source occurrence has value `X`, is used by the usual `d+1` consecutive
owner windows, and

\[
                         |X|=r-d+1,                    \tag{0.1}
\]

then those owners, after deleting `X`, form a length-`d` walk on
`(d-1)`-subsets.  Such a walk always contains a positive coordinate run

\[
                         0\,1^\ell\,0,qquad
                         1\leq \ell\leq d-1,           \tag{0.2}
\]

strictly between its endpoints.  Therefore a full-window host of the
minimal rank (0.1) is never internally depth-`d` resident.  Any global cut
which repairs it must cross one of the `d` transition edges among its
`d+1` owner windows.

For the aligned folded-C8 addresses

\[
                         p_R-p_L=d,                    \tag{0.3}
\]

the two transition-edge sets are disjoint.  Hence one global cut cannot
repair **two independent** full-window minimal hosts at `p_L,p_R`.  The
fact that a chosen coordinate can have traces `1,0,...,0,1` on the left and
`0,1,...,1,0` on the right does not evade this: the link-size argument
forces another internal island on the left.

The surviving construction is genuinely different.  Open the owner cycle
first, and place the two folded host blocks at the two source boundaries,

\[
 X_L,b_L^\epsilon,\ldots,b_R^\epsilon,X_R,             \tag{0.4}
\]

so neither `X_L` nor `X_R` is constrained by an internal family of `d+1`
owners.  The exact remaining conditions are the ordinary source-screen and
reconstruction equations, occurrence-labelled lower/upper palette
injectivity, the boundary run test, and one cap-compatible background
matching.  Under those hypotheses the already proved folded ray identities
give a free `2d-2` ray bank and the antitone birail theorem gives terminal
Hall deficiency zero.

Thus (0.3) identifies the correct place to seek a boundary rail, but does
not itself prove that rail exists.

## 1. Owner links of a minimal host

Let

\[
 O=(O_i)_{i\in\mathbb Z/N\mathbb Z}
\]

be a cyclic word of distinct `r`-subsets with

\[
                         |O_{i-1}\triangle O_i|=2.     \tag{1.1}
\]

Use the convention that source position `p` occurs in owners

\[
                  O_{p-d},O_{p-d+1},\ldots,O_p.        \tag{1.2}
\]

Suppose a nonempty source letter `X` is contained in every owner in (1.2)
and satisfies (0.1).  Put

\[
 H_j=O_{p-d+j}\setminus X,qquad 0\leq j\leq d.        \tag{1.3}
\]

Then

\[
 |H_j|=d-1,qquad |H_{j-1}\triangle H_j|=2.            \tag{1.4}
\]

Indeed both adjacent owners contain `X`, so their exchanged coordinates
lie outside `X`.  Thus (1.3) is a walk of length `d` in a Johnson graph on
`(d-1)`-subsets.  If `X` is the maximal source screen at `p`, then also

\[
                         \bigcap_{j=0}^d H_j=\varnothing. \tag{1.5}
\]

The next theorem does not need (1.5).

### Theorem 1.1 (forced internal run)

Every walk (1.3)--(1.4) has a coordinate whose indicator on
`H_0,H_1,...,H_d` contains a maximal positive run

\[
                 H_s,H_{s+1},\ldots,H_t,qquad
                 1\leq s\leq t\leq d-1.              \tag{1.6}
\]

In particular its length is at most `d-1` and the run is bounded by zeros
on both sides.

#### Proof

At each of the `d` transitions choose the unique arriving coordinate

\[
                         a_j\in H_j\setminus H_{j-1}. \tag{1.7}
\]

Occurrence (1.7) starts a positive run after `H_0`.  If the same coordinate
arrives twice, its first such run ended before the second arrival and hence
is of the form (1.6).  Otherwise the `d` arrivals are distinct.  If none of
their runs ended before `H_d`, all `d` arriving coordinates would belong to
`H_d`, contrary to `|H_d|=d-1`.  Thus some arriving run ends before `H_d`,
again giving (1.6).  Its length is at most `(d-1)-1+1=d-1`.  \(\square\)

### Corollary 1.2 (internal flat-host obstruction)

If every internal positive owner run must have length at least `d+1`, a
minimal host (0.1) cannot remain an internal full-window source occurrence.
The obstruction is owner-geometric; it does not depend on a particular
decomposition of `X`, on the lower compiler, or on the phase labels
`a_1,a_3`.

This sharpens the earlier rank-only flat-split obstruction.  Even if one
rethreads the `d+1` owners so that they all contain the enlarged host, the
link itself forces residence debt.

## 2. Which cuts can absorb one link ear

Write

\[
 e_i=(O_{i-1},O_i)
\]

for owner transition edges, and define the host-transition set

\[
 \Gamma(p)=\{e_{p-d+1},e_{p-d+2},\ldots,e_p\}.         \tag{2.1}
\]

A cyclic positive run on vertices `O_s,...,O_t` is boundary-clipped after
cutting an edge `e` exactly when `e` is one of the internal or two boundary
edges of that run.  In particular, every edge capable of clipping the
forced run (1.6) belongs to `Gamma(p)`.

### Theorem 2.1 (necessary single-ear cut condition)

If a full-window minimal host at `p` is depth-`d` resident after opening the
owner cycle at `e`, then

\[
                              e\in\Gamma(p).           \tag{2.2}
\]

More exactly, let `R_<(p)` be the collection of all positive runs of length
at most `d` wholly contained in the host link.  For a run `R`, let
`cl(R)` be its internal and two boundary transition edges.  Then the host
link is residence-safe after the cut if and only if

\[
              e\in \bigcap_{R\in R_<(p)}\operatorname{cl}(R), \tag{2.3}
\]

provided every run meeting the exterior is resident **after** the local
replacement.  Thus membership in `Gamma(p)` is necessary, while (2.3) is
the exact cut condition.

#### Proof

Theorem 1.1 supplies a nonempty `R_<(p)`.  A cut outside the closure of a
short run leaves that run internal with the same length.  Conversely a cut
in its closure makes it a leading run, a trailing run, or two clipped
boundary pieces.  Applying this independently to all local short runs gives
(2.3), and every such closure lies in (2.1).  \(\square\)

### A useful sufficient normal form for one ear

Let `U={u_1,...,u_(d-1)}` and `V={v_1,...,v_(d-1)}` be disjoint.  If, after
placing the cut at the last host transition,

\[
 H_j=(U\setminus\{u_1,\ldots,u_j\})
       \cup\{v_1,\ldots,v_j\},qquad 0\leq j\leq d-1, \tag{2.4}
\]

then the retained `d-1` link transitions are one-way and all `v_j` runs are
trailing boundary runs.  Let `lambda(u_j)` be the number of consecutive
exterior owners immediately preceding `H_0` which contain `u_j`.  The old
run ending at `H_(j-1)` is resident precisely when

\[
                         \lambda(u_j)+j\geq d+1.       \tag{2.5}
\]

Thus (2.4)--(2.5), together with residence of unchanged exterior runs, is
an explicit sufficient one-ear certificate.  It also shows why one cut can
absorb one extra delete/reinsert: after the cut only `d-1` one-way swaps
remain.

For the retained transition `j`, the exact palette colours are

\[
 \begin{aligned}
  I_j&=X\cup(H_{j-1}\cap H_j), &&|I_j|=r-1,\\
  U_j&=X\cup(H_{j-1}\cup H_j), &&|U_j|=r+1.
 \end{aligned}                                          \tag{2.6}
\]

The formulas make palette checking finite and occurrence-labelled; they do
not by themselves show that these colours avoid the exterior palette.

## 3. Two aligned independent hosts need two cut opportunities

Assume `N>2d`, and let

\[
                         p_R=p_L+d                     \tag{3.1}

\]
in one unwrapped cyclic chart.  Then

\[
 \begin{aligned}
  \Gamma(p_L)&=\{e_{p_L-d+1},\ldots,e_{p_L}\},\\
  \Gamma(p_R)&=\{e_{p_L+1},\ldots,e_{p_L+d}\}.
 \end{aligned}                                         \tag{3.2}
\]

These sets are disjoint.

### Theorem 3.1 (two-independent-host one-cut no-go)

Suppose both desired folded hosts `X_L,X_R`:

1. have rank `r-d+1`;
2. are each contained in all `d+1` owners of their native source occurrence;
3. retain those two full owner-window families after rethreading; and
4. are required to be internally depth-`d` resident after one global cut.

If their addresses obey (3.1), no such one-cut realization exists.

#### Proof

By Theorem 2.1 the cut edge must belong to `Gamma(p_L)` and to
`Gamma(p_R)`.  Equation (3.2) makes this impossible.  \(\square\)

### Audit of the tempting paired trace

Cutting `e_(p_L+1)=(O_(p_L),O_(p_L+1))` can indeed clip a right-link trace

\[
                         0,1,\ldots,1,0.               \tag{3.3}
\]

A left-link coordinate with trace

\[
                         1,0,\ldots,0,1                \tag{3.4}

is also individually harmless if its initial run has enough exterior age
and its final `1` is clipped.  But (3.4) is not the run forced by Theorem
1.1.  The left `(d-1)`-link has another run of form (1.6); its closure lies
in `Gamma(p_L)`, whereas the displayed cut lies in `Gamma(p_R)`.  That run
remains internal.  For `d=2` the complete local picture is already

\[
                         101\quad\text{and}\quad010.    \tag{3.5}
\]

Clipping the former does not remove the latter.

The theorem is deliberately scoped to **independent full-window hosts**.
It does not rule out a coupled endpoint rail in which one or both host
occurrences see fewer than `d+1` owners, nor a nonflat deadline jump, two
cuts, or an owner rethread which moves the two host arcs so their transition
sets overlap.

## 4. Exact surviving coupled endpoint interface

Open the owner cycle at a selected edge and write the resulting owner path

\[
                         \widetilde O_0,\ldots,
                         \widetilde O_{M-1}.            \tag{4.1}

For source positions `0<=s<M+d`, define the maximal boundary screens

\[
 E_s=\bigcap_{i=\max(0,s-d)}^{\min(M-1,s)}\widetilde O_i. \tag{4.2}
\]

The following elementary criterion is the exact owner/common-`Q` test.

### Proposition 4.1 (boundary source criterion)

A nonzero source word `Q_0,...,Q_(M+d-1)` dilates to (4.1) at depth `d` if
and only if

\[
 \varnothing\ne Q_s\subseteq E_s\quad(0\leq s<M+d),   \tag{4.3}
\]

and

\[
             \bigcup_{s=i}^{i+d}Q_s=\widetilde O_i
             \quad(0\leq i<M).                        \tag{4.4}
\]

For two folded phases, a pointwise common cap `C_s` is legal exactly when
both phase words satisfy (4.3)--(4.4) and

\[
                         Q_s^\epsilon\subseteq C_s     \tag{4.5}

for every `s,epsilon`.  Any selected compiler cell adds its literal OR
equation to (4.3)--(4.5); caps alone do not imply those equations.

#### Proof

Every source letter used by owner `i` must be a subset of that owner,
giving (4.3).  The value of owner window `i` is exactly the left side of
(4.4), so (4.4) is necessary and sufficient.  Equation (4.5) is precisely
pointwise cap legality.  \(\square\)

For the folded comparator, put

\[
 \begin{array}{ll}
 b_L^0=K+za_3+f_1,&b_L^1=K+za_1+f_1,\\
 b_R^0=K+za_1+f_d,&b_R^1=K+za_3+f_d,
 \end{array}                                           \tag{4.6}
\]

and

\[
 X_L=K+za_1a_3+f_1,qquad X_R=K+za_1a_3+f_d.          \tag{4.7}

### Theorem 4.2 (conditional coupled boundary-rail closure)

Suppose one can choose the cut, the owner paths in both phases, and source
words satisfying Proposition 4.1 with the following extra properties.

1. The source begins with the prefix block `(X_L,b_L^epsilon)` and ends
   with the suffix block `(b_R^epsilon,X_R)`, with the appropriate adjacent
   decreasing filler fans.  Thus `X_L,X_R` are clipped boundary
   occurrences, not the two independent internal occurrences of Theorem
   3.1.
2. All owners have rank `r`, are pairwise distinct in the required owner
   bank, and consecutive owners are Johnson adjacent.
3. The retained owner edges have pairwise-distinct required lower colours
   `O_(i-1) intersect O_i`; their required upper colours
   `O_(i-1) union O_i` are complete.  Any colour of the deleted cut edge is
   supplied by an explicitly named sidecar.
4. Every internal positive owner run has length at least `d+1`.  Equivalently,
   every shorter cyclic run has the selected cut in its closure.
5. One occurrence-labelled old compiler matching transports in the common
   cap state (4.5), disjointly from the new boundary fan cells.
6. Every interval meeting both marked endpoint blocks is phase-common.  It
   is enough that the intervening body has a phase-common full union; in the
   literal two-host rail it follows from
   `b_L^0 union b_R^0=b_L^1 union b_R^1` together with the common filler
   body.
7. In the terminal two-prefix compiler reduction, the occurrence labels of
   the left and right ray cells admit the antitone threshold pairing (or the
   same pairing is reached by certified matching-closed comparators).  This
   is the occurrence-level reachability clause; the two marginal multisets
   alone do not imply it.

Then the two boundary fans realize, in distinct physical cells,

\[
 \begin{aligned}
  \mathcal P_\epsilon
    &=\{K+z+a_{3-2\epsilon}+F[1,j]:1\leq j<d\},\\
  \mathcal S_\epsilon
    &=\{K+z+a_{1+2\epsilon}+F[j,d]:1<j\leq d\},
 \end{aligned}                                         \tag{4.8}

with pointwise caps `X_L,X_R`.  Their packet matroid is

\[
                         U_{2d-2,2d-2}.               \tag{4.9}

No interval wraps across the global cut.  Long intervals meeting both
endpoint blocks still exist, but hypothesis 6 makes all of them
phase-common, so they create no exclusive cross-host debt.  Combining the
fan diagonal with the transported old matching closes local common-`Q`
Hall.  Moreover the canonical threshold marginals are both

\[
                         \{0^{d-1},1,\ldots,d-1\},     \tag{4.10}

so the antitone birail theorem gives terminal corner deficiency zero.

#### Proof

The prefix block and its decreasing filler fan give the `d-1` literal
prefix intervals in (4.8); the suffix block gives the `d-1` suffix
intervals.  They lie at opposite ends of the linear source word and hence
are distinct, and no physical interval can cross the removed cyclic edge.
The cap containments follow from (4.6)--(4.7).  This gives a literal diagonal
matching on all `2d-2` targets and proves (4.9).  Hypothesis 5 supplies the
cell-disjoint background matching.  Finally (4.10) has
`N=2d-2` and left/right excesses `d-1,d-1`; the exact antitone formula
`(E_L+E_R-N)_+` is zero, and hypothesis 7 realizes the minimizing pairing.
\(\square\)

## 5. Exact remaining datum

The aligned folded audit proves the numerical address relation (0.3), the
two ray supports, owner/lower-q1/Hamilton structure before host planting,
and resident nonzero inverses.  It does **not** prove any of hypotheses
1--5 of Theorem 4.2 for boundary-planted hosts.  In particular:

* rerooting alone only changes the screens (4.2); it does not imply
  reconstruction (4.4);
* the native internal screens at `p_L,p_R` are the strict bases
  `b_L^epsilon,b_R^epsilon`, not `X_L,X_R`;
* Theorem 3.1 rules out treating the proposed boundary rail as two unchanged
  internal host links; and
* distinct ray support and scalar zero birail deficiency do not supply the
  occurrence-labelled background matching in hypothesis 5.

Accordingly the smallest honest next certificate is an occurrence-level
pair of phase source words satisfying (4.3)--(4.5), the four fixed boundary
letters (4.6)--(4.7), the owner/palette checks in hypotheses 2--3, and the
run condition in hypothesis 4.  That certificate would make the compiler
conclusion automatic by Theorem 4.2.  Without it, the exact result is the
two-independent-host obstruction of Theorem 3.1, not a physical folded-C8
comparator lift.
