# Balanced owner paths, exact multisocket Hall cuts, and the reciprocal barrier

**Date:** 2026-08-03  
**Status:** unconditional balanced Boolean path-cover theorem and exact
adaptive-boundary multisocket max-flow criterion.  The rankwise-sharp
majorization consequence of balance fails at the optimal depth.  The note
does **not** prove the remaining named flag factor, and it does not assert
that a balanced path cover satisfies the multisocket cuts.  No computation
is used.

## 0. Outcome

Let \(r\) be a widest rank on the lower interval of \(\mathcal B_k\), in
the precise sense that

\[
 W=\binom{k}{r},\qquad C_s=\binom{k}{s}\le W
 \quad(0\le s\le r),\qquad p_s=\frac{C_s}{W}.
\tag{0.1}
\]

This includes either middle rank in odd dimension and the unique middle
rank in even dimension.

There is a family of exactly \(W\) saturated descending Boolean paths,
one starting at each rank-\(r\) owner, such that every rank-\(s\) set is
visited either

\[
 \left\lfloor\frac{W}{C_s}\right\rfloor
 \quad\hbox{or}\quad
 \left\lceil\frac{W}{C_s}\right\rceil
\tag{0.2}
\]

times.  This is an integral lower-bounded network-flow theorem.  In
particular every strict-lower Boolean target is visited at least once.

Fix any such owner-path bank, or indeed any owner-path bank.  At rank
\(s\), prescribe an adaptive boundary size \(b_s\), so the required named
target count is

\[
                         N_s=C_s-b_s.                 \tag{0.3}
\]

For a family \(Q\) of owner paths, let \(e_s(Q)\) be the number of
rank-\(s\) sets all of whose visiting paths belong to \(Q\).  Then one can
choose exactly \(N_s\) distinct rank-\(s\) targets at every rank and assign
them to visiting paths, with at most \(d\) chosen targets on each path, if
and only if

\[
 \boxed{
   \sum_{s=1}^{r-1}\bigl(e_s(Q)-b_s\bigr)_+
      \le d|Q|
   \qquad(Q\subseteq\mathcal P).}
\tag{0.4}
\]

This is the exact multisocket Hall condition.  Its maximum violation is
the exact target deficiency.  The targets selected on any one path are
automatically one literal inclusion flag below its owner.

The balanced visit multiplicities (0.2), however, do not by themselves
prove (0.4).  Write

\[
                         m_s=\left\lfloor\frac W{C_s}\right\rfloor.
\tag{0.5}
\]

The exact worst possible number of rank-\(s\) visitor blocks captured by a
\(q\)-path family is an explicit function \(\Phi_s(q)\) given in Section 3.
Consequently

\[
 \sum_s\bigl(\Phi_s(q)-b_s\bigr)_+\le dq
 \qquad(0\le q\le W)                                  \tag{0.6}
\]

is a sufficient condition based only on balanced rank marginals.  It is
rankwise sharp.  For the even specialization \(k=2r\), at the optimal
lower depth and triangular boundary,

\[
 \frac d{\sqrt r}\longrightarrow\frac{\sqrt\pi}{2},
 \qquad \sum_sb_s=O(r),                                \tag{0.7}
\]

condition (0.6) fails by \(\Theta(q\sqrt r)\) for some fixed-density
\(q=\Theta(W)\).  The decisive reciprocal constant already from the first
two multiplicity zones is

\[
 \frac{\sqrt{\log2}+\sqrt{\log3}}2
       >\frac{\sqrt\pi}{2}.                            \tag{0.8}
\]

This is a sharp obstruction to a marginal-only uniform-splitting proof,
not an obstruction to a jointly designed Boolean path bank.  A successful
multisocket proof must establish cross-rank decorrelation: no one path
family \(Q\) may simultaneously capture the small visitor blocks at too
many ranks.

Some genuine multisocket cuts are already automatic.  Every balanced path
bank passes the empty cut, every one-path cut, and the whole-bank cut for
the optimal inventory in all sufficiently large dimensions.  Thus the
unresolved content lies in collective intermediate path families.

Finally, (0.4) deliberately forgets the no-adjacent-residual-rank law of
the optimal anonymous schedule.  Restoring that law gives the exact
zero--one system in Section 5, not the one-commodity flow in Section 2.
At the level of abstract set partitions, the full anonymous schedule and
balanced visit multiplicities are compatible rank by rank; Proposition
5.1 proves this exactly.  What remains is to realize those partitions by
one nested Boolean path bank.
Thus the weakest still-unproved serial statement is already (0.4) for a
suitably chosen path bank; the pattern-faithful named lift is stronger.

## 1. An integral balanced owner-path cover

An **owner path** is a saturated chain

\[
 T=P_T(r)\supset P_T(r-1)\supset\cdots\supset
 P_T(0)=\varnothing,
 \qquad |P_T(s)|=s,                                    \tag{1.1}
\]

indexed by its owner \(T\in\binom{[k]}r\).  Different owner paths are
allowed to meet below rank \(r\).

### Theorem 1.1 (balanced Boolean path cover)

There is an owner path \(P_T\) for every rank-\(r\) owner such that, for
every \(S\in\binom{[k]}s\),

\[
 \mu(S):=|\{T:P_T(s)=S\}|
 \in
 \left\{
  \left\lfloor\frac W{C_s}\right\rfloor,
  \left\lceil\frac W{C_s}\right\rceil
 \right\}.                                             \tag{1.2}
\]

### Proof

Direct every Boolean cover edge downward.  Split every Boolean node \(S\)
of rank \(s\) into an entrance and an exit joined by one node arc.  Give
that arc the integral lower and upper capacities

\[
 m_s=\left\lfloor\frac W{C_s}\right\rfloor,
 \qquad
 M_s=\left\lceil\frac W{C_s}\right\rceil.              \tag{1.3}
\]

Join a source to each rank-\(r\) entrance by an arc fixed at one, retain
all downward Boolean arcs between split nodes with capacity \(W\), and
join the empty-set exit to a sink by an arc fixed at \(W\).

This lower-bounded network has a fractional feasible flow.  Give every
rank-\(s\) node arc the value

\[
                              \frac W{C_s}.              \tag{1.4}
\]

For a rank-\(s\) node with \(s\ge1\), split this value equally over its
\(s\) downward arcs, giving each such arc value

\[
                              \frac W{sC_s}.              \tag{1.5}
\]

A fixed rank-\((s-1)\) node has \(k-s+1\) immediate supersets.  The
identity

\[
                       sC_s=(k-s+1)C_{s-1}               \tag{1.6}
\]

shows that its incoming flow is \(W/C_{s-1}\), so conservation holds.
At rank \(r\), (1.4) equals one; at rank zero it equals \(W\).  The node
bounds (1.3) contain (1.4), so the fractional flow is feasible.

Integral lower-bounded network flows have integral vertices.  Hence the
same network has an integral feasible flow.  Decompose its value \(W\)
into unit source--sink paths.  Every rank-\(r\) source arc has value one,
so exactly one path starts at each owner.  The integral value on the node
arc of \(S\) is exactly the number \(\mu(S)\) of decomposed paths visiting
\(S\), and (1.3) gives (1.2).  \(\square\)

Since \(C_s\le W\) for \(s\le r\), every lower bound in (1.3) is at least
one.  Thus Theorem 1.1 really covers every lower set; it is not merely an
average visitation statement.

## 2. Exact adaptive-boundary multisocket Hall theorem

Fix an arbitrary owner-path bank

\[
                         \mathcal P=(P_T:T\in\mathcal O),
 \qquad \mathcal O=\binom{[k]}r.                          \tag{2.1}
\]

For a lower set \(S\), define its visitor set

\[
                         V(S)=\{T:P_T(|S|)=S\}.           \tag{2.2}
\]

For \(Q\subseteq\mathcal O\), put

\[
 e_s(Q)=
 \left|\left\{S\in\binom{[k]}s:V(S)\subseteq Q\right\}\right|.
\tag{2.3}
\]

The empty visitor set is allowed in this definition.  In particular, the
cut \(Q=\varnothing\) checks that at most \(b_s\) unvisited rank-\(s\)
sets must be retained.

### Theorem 2.1 (exact multisocket cut and deficiency)

Let \(0\le b_s\le C_s\), put \(N_s=C_s-b_s\), and assume

\[
                              N:=\sum_sN_s\le dW.         \tag{2.4}
\]

There are families

\[
 \mathcal A_s\subseteq\binom{[k]}s,
 \qquad |\mathcal A_s|=N_s,                              \tag{2.5}
\]

and an assignment \(\phi\) of every selected target \(S\) to a visiting
path \(P_{\phi(S)}\), with at most \(d\) assigned targets on any path, if
and only if (0.4) holds.

More generally, if shortages from the demands \(N_s\) are permitted, the
minimum total shortage is

\[
 \boxed{
 \delta(\mathcal P;b,d)=
 \max_{Q\subseteq\mathcal O}
 \left[
   \sum_s\bigl(e_s(Q)-b_s\bigr)_+-d|Q|
 \right]_+.}
\tag{2.6}
\]

### Proof

Use the network

\[
 \text{source}\longrightarrow s\longrightarrow S
 \longrightarrow T\longrightarrow\text{sink}.          \tag{2.7}
\]

The source--rank arc has capacity \(N_s\).  A rank node \(s\) is joined
to every rank-\(s\) target \(S\) with capacity one.  The target \(S\) is
joined to every \(T\in V(S)\) with capacity \(N+1\), and every path node
\(T\) is joined to the sink with capacity \(d\).  An integral flow of
value \(N\) is exactly (2.5) and the required assignment.

It remains to calculate all cuts.  Let \(A\) be the rank nodes and \(Q\)
the path nodes on the source side.  A finite minimum cut puts a target
\(S\) of a rank in \(A\) on the source side precisely when
\(V(S)\subseteq Q\); doing so saves its unit rank--target arc and costs no
large target--path arc.  Targets at ranks outside \(A\) give no saving.
Thus the least cut with fixed \(A,Q\) has capacity

\[
 \sum_{s\notin A}N_s
 +\sum_{s\in A}\bigl(C_s-e_s(Q)\bigr)
 +d|Q|.                                                  \tag{2.8}
\]

Requiring (2.8) to be at least \(N\) is equivalent to

\[
 \sum_{s\in A}\bigl(e_s(Q)-b_s\bigr)\le d|Q|.           \tag{2.9}
\]

For fixed \(Q\), the left side is maximized by taking exactly the ranks
with \(e_s(Q)>b_s\).  Hence all inequalities (2.9) are equivalent to
(0.4).

The same cut calculation and max-flow/min-cut show that the difference
between \(N\) and the maximum flow value is the maximum positive violation
in (2.6).  All capacities are integral, so maximum flow is integral.
\(\square\)

### Corollary 2.2 (fixed named boundary)

Suppose instead that fixed target families

\[
                         \mathcal L_s\subseteq\binom{[k]}s
\tag{2.10}
\]

must all be assigned.  Put

\[
 e_{\mathcal L}(Q)=
 |\{S\in\bigcup_s\mathcal L_s:V(S)\subseteq Q\}|.
\tag{2.11}
\]

Then the fixed targets fit at depth \(d\) if and only if

\[
                         e_{\mathcal L}(Q)\le d|Q|
                         \qquad(Q\subseteq\mathcal O),   \tag{2.12}
\]

and the exact deficiency is

\[
              \max_Q\bigl(e_{\mathcal L}(Q)-d|Q|\bigr)_+.
\tag{2.13}
\]

This is ordinary capacitated Hall after conjugating the usual target-set
cuts to path families.

### Corollary 2.3 (literal flag interpretation)

Every feasible assignment from Theorem 2.1 partitions the selected named
targets into ownerwise inclusion flags of length at most \(d\).
Conversely, every such ownerwise flag realization can be extended to an
owner-path bank satisfying (0.4).

### Proof

Targets assigned to one path occur at distinct ranks on one saturated
chain and are therefore nested below its rank-\(r\) owner.  Conversely,
extend each finite owner flag downward to the empty set and fill every
missing rank up to its owner.  The resulting saturated paths may meet,
which is allowed.  The original target assignment is a feasible flow in
(2.7), so Theorem 2.1 supplies (0.4).  \(\square\)

Thus choosing a path bank with (0.4) is not a relaxation magically weaker
than the static named-flag problem.  It is an exact serial reformulation of
that problem when only the total row capacity is imposed.

## 3. The rankwise-sharp consequence of balanced visitation

Assume now that \(\mathcal P\) is balanced as in Theorem 1.1.  Fix a rank
\(s<r\), abbreviate \(m=m_s=\lfloor W/C_s\rfloor\), and put

\[
 a_s=(m+1)C_s-W,
 \qquad
 c_s=W-mC_s.                                             \tag{3.1}
\]

Exactly \(a_s\) rank-\(s\) visitor blocks have size \(m\), exactly
\(c_s\) have size \(m+1\), and

\[
                         a_s+c_s=C_s.                     \tag{3.2}
\]

For \(0\le q\le W\), define

\[
 \Phi_s(q)=
 \min\left\{a_s,\left\lfloor\frac q m\right\rfloor\right\}
 +
 \min\left\{
 c_s,
 \left\lfloor
   \frac{(q-ma_s)_+}{m+1}
 \right\rfloor
 \right\}.                                              \tag{3.3}
\]

### Lemma 3.1 (exact one-rank capture envelope)

For every \(q\),

\[
 \max_{Q\subseteq\mathcal O:\ |Q|=q}e_s(Q)=\Phi_s(q).   \tag{3.4}
\]

### Proof

At rank \(s\), the nonempty visitor sets \(V(S)\) partition the \(W\)
path labels.  A \(q\)-set \(Q\) contains the visitor sets of at most
\(\lfloor q/m\rfloor\) size-\(m\) blocks, up to the available \(a_s\).
After all \(a_s\) small blocks have been included, every further captured
block costs \(m+1\) path labels.  This proves the upper bound (3.3).

For equality, take as many complete size-\(m\) visitor blocks as possible,
then as many complete size-\((m+1)\) blocks as possible, and fill any
unused positions of \(Q\) arbitrarily.  This realizes (3.3).  \(\square\)

### Corollary 3.2 (balanced-marginal sufficient condition)

If

\[
 \boxed{
 \sum_{s=1}^{r-1}\bigl(\Phi_s(q)-b_s\bigr)_+\le dq
 \qquad(0\le q\le W),}                                  \tag{3.5}
\]

then every balanced owner-path bank satisfies (0.4), and hence supports
the complete adaptive inventory \((N_s)\) at depth \(d\).

### Proof

For \(Q\) of size \(q\), Lemma 3.1 gives
\(e_s(Q)\le\Phi_s(q)\) at every rank.  Insert these inequalities into
(0.4).  \(\square\)

Condition (3.5) uses no information about how the small visitor blocks at
different ranks are aligned.  Lemma 3.1 says that its input is exact at
each individual rank.  Its only possible loss is simultaneous: the path
family maximizing (3.4) can depend on \(s\).

### Corollary 3.3 (empty, singleton, and whole-bank cuts)

Assume

\[
 k=2r,\qquad
 \frac d{\sqrt r}\longrightarrow\frac{\sqrt\pi}{2},
 \qquad \sum_sN_s\le dW.                                \tag{3.6}
\]

For every balanced owner-path bank and all sufficiently large \(r\), the
exact multisocket inequality (0.4) holds whenever

\[
                         |Q|\in\{0,1,W\}.               \tag{3.7}
\]

### Proof

Balanced visitation has no unvisited target, so \(e_s(\varnothing)=0\)
at every rank.  This proves the empty cut.  For \(Q=\mathcal O\), one has
\(e_s(Q)=C_s\), and (0.4) is precisely
\(\sum_sN_s\le dW\).

Now let \(Q\) consist of one path.  A target can have all its visitors in
\(Q\) only when its visit multiplicity is one.  Such a target can occur
only at a rank with

\[
                         p_s=\frac{C_s}{W}>\frac12.      \tag{3.8}
\]

There is at most one such target on the path at each rank.  By the same
central-binomial ratio used below, the number of ranks satisfying (3.8)
is

\[
                         (\sqrt{\log2}+o(1))\sqrt r.     \tag{3.9}
\]

This is less than \(d\) for all sufficiently large \(r\).  Indeed
\(e^{3/4}>1+3/4+(3/4)^2/2>2\), so
\(\log2<3/4<\pi/4\).  Boundary subtraction can only reduce the left side
of (0.4).  Hence every singleton cut holds.  \(\square\)

## 4. The reciprocal two-zone barrier

The following theorem audits (3.5) on the optimal asymptotic scale.

### Theorem 4.1 (rankwise-envelope obstruction)

Assume

\[
 k=2r,\qquad
 \frac d{\sqrt r}\longrightarrow\alpha=\frac{\sqrt\pi}{2},
 \qquad
 B_\partial:=\sum_{s=1}^{r-1}b_s=O(r).                  \tag{4.1}
\]

Then there are absolute constants \(\theta,c>0\) such that, with
\(q=\lfloor\theta W\rfloor\), for all sufficiently large \(r\),

\[
 \sum_s\bigl(\Phi_s(q)-b_s\bigr)_+
 \ge (d+c\sqrt r)q.                                     \tag{4.2}
\]

Thus the balanced-marginal sufficient condition (3.5) fails by
\(\Theta(\sqrt r\,W)\).

### Proof

For \(j=O(\sqrt r)\), the central binomial ratio satisfies uniformly on
fixed scaled windows

\[
 p_{r-j}=\exp(-j^2/r+o(1)).                              \tag{4.3}
\]

The first visit-multiplicity zone has \(m_s=1\) when \(p_s>1/2\); the
second has \(m_s=2\) when \(1/3<p_s\le1/2\).  Their limiting scaled
widths are respectively

\[
 \sqrt{\log2},
 \qquad
 \sqrt{\log3}-\sqrt{\log2}.                             \tag{4.4}
\]

Put

\[
 \beta=\sqrt{\log2}
 +\frac12\bigl(\sqrt{\log3}-\sqrt{\log2}\bigr)
 =\frac{\sqrt{\log2}+\sqrt{\log3}}2.                   \tag{4.5}
\]

This constant is strictly larger than \(\alpha\).  One elementary check
is

\[
 \log2>\frac23,\qquad \log3>1,\qquad \pi<\frac{22}{7},  \tag{4.6}
\]

where the first two inequalities follow from strict midpoint lower bounds
for the integral of \(1/x\).  Moreover

\[
 \left(1+\sqrt{\frac23}\right)^2
 =\frac53+2\sqrt{\frac23}>\frac{22}{7},                 \tag{4.7}
\]

the last inequality following after squaring from
\(8/3>961/441\).  Hence
\(\sqrt{\log2}+\sqrt{\log3}>\sqrt\pi\), proving
\(\beta>\alpha\).

Choose a sufficiently small \(\eta>0\) so that

\[
 \beta_\eta:=
 \sqrt{-\log(1/2+\eta)}
 +\frac12\left(
   \sqrt{-\log(1/3+\eta)}-\sqrt{\log2}
 \right)>\alpha.                                       \tag{4.8}
\]

Then choose a fixed \(\theta>0\) with
\(\theta<\min\{2\eta,6\eta\}\), and put
\(q=\lfloor\theta W\rfloor\).

If \(p_s\ge1/2+\eta\), then \(m_s=1\) and the number of
multiplicity-one visitor blocks is

\[
                         a_s=(2p_s-1)W\ge2\eta W>q.      \tag{4.9}
\]

Therefore \(\Phi_s(q)=q\).  If
\(1/3+\eta\le p_s<1/2\), then \(m_s=2\) and

\[
             2a_s=2(3p_s-1)W\ge6\eta W>q,               \tag{4.10}
\]

so \(\Phi_s(q)=\lfloor q/2\rfloor\).

Equation (4.3) counts

\[
 \bigl(\sqrt{-\log(1/2+\eta)}+o(1)\bigr)\sqrt r        \tag{4.11}
\]

ranks of the first kind and

\[
 \left(
  \sqrt{-\log(1/3+\eta)}-\sqrt{\log2}+o(1)
 \right)\sqrt r                                        \tag{4.12}
\]

ranks of the second kind.  Since \((x-b)_+\ge x-b\), the
contribution of just these two rank windows is at least

\[
 \bigl(\beta_\eta+o(1)\bigr)q\sqrt r
 -B_\partial-O(\sqrt r).                                \tag{4.13}
\]

Here the final term absorbs the floors in \(q/2\).  Because
\(q=\Theta(W)\) while \(B_\partial=O(r)\), the last two terms are
\(o(q\sqrt r)\).  Equations (4.1) and (4.8) now give (4.2) with any fixed
\(c<\beta_\eta-\alpha\), after decreasing \(c\) if necessary.
\(\square\)

The lower bound just proved is also of the asserted order from above:
\(\Phi_s(q)\le C_s\), while
\(\sum_{s<r}C_s=O(\sqrt r\,W)\) and \(dq=O(\sqrt r\,W)\).

Theorem 4.1 does **not** exhibit a set \(Q\) violating (0.4) in every
balanced Boolean path bank.  Lemma 3.1 maximizes one rank at a time, and
the maximizing \(Q\)'s may differ.  The theorem proves the precise weaker
negative statement: balanced node multiplicities, followed by independent
rankwise worst-case estimates or a uniform-splitting estimate using only
those multiplicities, cannot certify the required depth.  Any improvement
must use the common cross-rank geometry of the visitor partitions.

## 5. Restoring the anonymous residual rank law

Return in this section to the even optimal specialization \(k=2r\).

Let

\[
 J=\{1,\ldots,r-a-1\}
\tag{5.1}
\]

be the residual ranks, on which adjacent selected ranks are forbidden;
collar ranks are unrestricted.  For a fixed path bank, introduce binary
variables

\[
 x_{T,s}=1
 \quad\Longleftrightarrow\quad
 \text{the rank-}s\text{ set }P_T(s)\text{ is marked on path }T.
\tag{5.2}
\]

First separate the purely rankwise partition issue from Boolean nesting.
Let

\[
                         R_1,\ldots,R_W\subseteq[r-1]   \tag{5.3}
\]

be any anonymous pattern schedule, and put

\[
 I_s=\{i:s\in R_i\},\qquad |I_s|=N_s\le C_s.           \tag{5.4}
\]

### Proposition 5.1 (abstract balanced socket compatibility)

For every rank \(s\), there is a partition of the \(W\) row labels into
\(C_s\) nonempty blocks, each of size

\[
 \left\lfloor\frac W{C_s}\right\rfloor
 \quad\hbox{or}\quad
 \left\lceil\frac W{C_s}\right\rceil,                 \tag{5.5}
\]

such that no block contains two members of \(I_s\).

Consequently the entire anonymous schedule can be placed in balanced
abstract sockets with distinct target labels at every rank, while
preserving every row pattern \(R_i\).

### Proof

Prescribe the unique floor/ceiling block-size histogram whose total is
\(W\).  There are \(C_s\) blocks and \(|I_s|=N_s\le C_s\) active row
labels.  Inject the active labels into different blocks.  Every block has
capacity at least one.  The unfilled block capacity is exactly
\(W-N_s\), equal to the number of inactive labels, so fill it arbitrarily.
Repeat independently at every rank and label the \(C_s\) blocks by the
\(C_s\) named rank-\(s\) sets.  An active row uses its block label; active
labels lie in distinct blocks, so no named target repeats.  \(\square\)

Proposition 5.1 is not a Boolean flag theorem.  For a genuine owner-path
bank, the block containing row \(i\) at rank \(s\) must be labelled by a
set contained in the label of its block at rank \(s+1\), and the rank-
\(r\) label must be its owner.  The independent partitions above impose
neither condition.  They prove that balanced multiplicity and the
anonymous schedule have no rankwise conflict; the missing constraint is
their simultaneous nested realization.

### Proposition 5.2 (exact pattern-faithful serial system)

The optimal anonymous rank counts \((N_s)\) have an exact named realization
on the fixed path bank, with no adjacent residual ranks and depth at most
\(d\), if and only if the following zero--one system is feasible:

\[
 \sum_Tx_{T,s}=N_s
 \qquad(1\le s<r),                                      \tag{5.6}
\]

\[
 \sum_{T:P_T(s)=S}x_{T,s}\le1
 \qquad\left(S\in\binom{[k]}s\right),                   \tag{5.7}
\]

\[
 x_{T,s}+x_{T,s+1}\le1
 \qquad(s,s+1\in J),                                   \tag{5.8}
\]

\[
 \sum_{s=1}^{r-1}x_{T,s}\le d
 \qquad(T\in\mathcal O).                               \tag{5.9}
\]

### Proof

Given a feasible zero--one vector, mark the unique rank-\(s\) set on
path \(T\) whenever \(x_{T,s}=1\).  Equation (5.6) gives the exact rank
inventory, (5.7) forbids reuse of a named target, (5.8) is the residual
rank law, and (5.9) is the depth cap.  All marked sets on one path are
nested below its owner.

Conversely, extend every owner flag in a named realization to a saturated
owner path and set \(x_{T,s}=1\) exactly at its marked ranks.  The four
properties of the realization give (5.6)--(5.9).  \(\square\)

If (5.8) is deleted, Proposition 5.2 is exactly the integral flow problem
of Theorem 2.1.  With (5.8) present, a marked occurrence simultaneously
uses a named-target capacity and an edge position in the residual rank
path.  The balanced owner-path flow of Theorem 1.1 supplies neither a
solution nor an integrality theorem for this coupled zero--one system.

In particular, it is invalid to argue that a balanced visitation flow can
first be decomposed into paths and that the optimal anonymous rank schedule
can then be placed on those paths by a second independent application of
network-flow integrality.  The target repetitions in (5.7) and the
within-path conflicts in (5.8) are coupled.

## 6. Exact remaining conjectures

The weakest named serial statement exposed by this note is the following.

### Conjecture 6.1 (capacity-only serial socket Hall)

For the optimal rank deficits \(b_s\) and depth \(d\), there is an
owner-path bank \(\mathcal P\) for which

\[
 \sum_s\bigl(e_s(Q)-b_s\bigr)_+\le d|Q|
 \qquad(Q\subseteq\mathcal P).                           \tag{6.1}
\]

By Corollary 2.3, this conjecture is exactly the rank-resolved adaptive-
boundary owner-flag theorem with only the total depth constraint.  It is
not proved here.  Theorem 1.1 proves that balanced covering paths exist;
Theorem 4.1 proves that their rank marginals alone do not imply (6.1).

The actual lift of the optimal anonymous noncontiguous rank inventory is
the stronger statement:

### Conjecture 6.2 (pattern-faithful serial socket lift)

There is an owner-path bank for which (5.6)--(5.9) is feasible for the
optimal counts \(N_s\).

The one-socket cross-SCD theorem proves special faces of these statements
by a uniform containment matching.  The balanced path cover supplies
sockets at every rank and therefore removes the lack-of-visitation issue.
What it does not supply is the simultaneous expansion of those sockets
across ranks.

The precise missing positive property can be stated without any reference
to a construction method:

\[
 \boxed{
 \text{choose one owner-path bank whose visitor partitions satisfy every
 cut (6.1), and then satisfy the residual conflicts (5.8).}}
\tag{6.2}
\]

No complete named lower flag factor, physical chronology, boundary-chain
placement, or upper-side compiler follows from the results in this note.

## 7. Relation to the preceding lower-side theorems

The conclusions are consistent with all five earlier projections.

* The one-socket cross-SCD theorem proves (a special) Hall family by
  uniform containment into one complete socket layer.  Equation (0.4) is
  the all-socket serial cut after the sockets have been organized into
  owner paths.
* The antitone theorem balances anonymous row loads exactly, while (0.4)
  records which named Boolean targets are forced into a path family.
  Antitone permutation does not control these sets.
* Sparse-top SCD rounding proves exact residual flags, but its whole chunks
  have the collar-capacity obstruction already audited.  Theorem 1.1
  discards those chunks and globally reflows all Boolean visits.
* Collar-hole majorization is a row-capacity cut for fixed residual loads.
  Equation (0.4) is the conjugate named-socket cut after the serial paths
  themselves are fixed.
* Rank-separated matroid intersection balances named containment ports but
  not their nesting.  Here nesting is built into the paths, and the missing
  condition reappears as simultaneous target uniqueness and socket Hall.

The proof-safe gain is therefore

\[
 \boxed{
 \begin{array}{c}
 \text{balanced integral visitation at every Boolean rank;}\\
 \text{exact adaptive multisocket max-flow cuts and deficiency;}\\
 \text{a sharp }\Theta(\sqrt r)\text{ reciprocal barrier to
 rank-marginal certification.}
 \end{array}}
\tag{7.1}
\]

Nothing stronger is claimed.
