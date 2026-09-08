# Global promotion rings: the common-floor representative theorem and the exact anchored leave absorber

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Verdict

Put

\[
 H=\lfloor\sqrt{m\log m}\rfloor,\qquad M=m+H,
 \qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad N=N_H.
\tag{0.1}
\]

This note does **not** prove the missing `fcpath` estimate and therefore
does not prove the constant-one theorem.  It proves two sharper interfaces
to that gate.

First, there is an edge-transitive, all-depth promotion-configuration
multihypergraph \({\cal C}_{m,H}\) with one identical cumulative floor
profile in every root fibre.  If \(\nu=\nu({\cal C}_{m,H})\), then its
best global weighted representative constant is exactly \(\nu/N\).  Thus
all arbitrary nonnegative duals collapse to the single unweighted
matching number.  Moreover

\[
 \boxed{\nu({\cal C}_{m,H})=N-o(N/\sqrt m)}
\tag{0.2}
\]

would give, by a literal one-baseline compilation,

\[
                         W+o(W).
\tag{0.3}
\]

This implication uses the exact word ledger, not an SCD completion.  The
matching estimate (0.2) remains unproved.

Second, after fixing a background full SCD, every rank-\(m-H\) root has
an exact promotion-ring tag-\(H\) anchor.  For a census-exact anchored
atlas, deleting a set \(D\) of nonanchor chains leaves an exact
two-sided symmetric-chain absorber problem.  The absorber exists if and
only if an explicitly defined hole-chain hypergraph has a matching
saturating the tokens in \(D\).  If \(D\) occupies \(b(D)\) deletion
runs and the absorber has an \(a(D)\)-path bridge-one cover, then

\[
 \boxed{
 \operatorname{fcpath}_{1,H}\le N+b(D)+a(D).}
\tag{0.4}
\]

In particular, a simplifying deletion of size \(o(W/H)\) whose leave has
an exact absorber proves the `fcpath` gate.  The two-sided linkage is a
real condition: correct counts and the two separate one-sided Hall
systems do not suffice.

Finally, the block-factor obstruction survives both formulations.
For the common-floor catalogue, any uniform-marginal law supported on
\(o(W)\)-hole selections and factoring over independent root blocks must
have a block of size

\[
 (1-o(1))\binom mH.
\tag{0.5}
\]

Even after a full SCD anchor is fixed in every root, the necessary block
size is at least

\[
 \boxed{
 (1-o(1)){\binom{m-H}{H}\over m-2H+1}}
\tag{0.6}
\]

and the logarithm of either scale is

\[
 \left({1\over2}+o(1)\right)
       \sqrt m\,(\log m)^{3/2}.
\tag{0.7}
\]

Consequently no product or local-reservoir scheme whose genuine
correlation components remain polynomial-sized can prove the theorem.
The exact remaining object is a fibre-dense global
representative, followed in the literal `fcpath` formulation by one
common-root leave linkage.

## 1. Critical counts and the positive-radius census

Write

\[
 \lambda_q={W\over N_q},\qquad
 \delta_m=\sqrt{m\log m}-H\in[0,1).
\tag{1.1}
\]

Uniform Taylor expansion in the present range gives

\[
 \log\lambda_H
 = {H^2\over m}-{H^2\over2m^2}
   +O\!\left({H^4\over m^3}+{H\over m^2}\right)
 =\log m-2\delta_m{H\over m}+o(H/m).
\tag{1.2}
\]

Therefore

\[
 \lambda_H=m-2\delta_mH+o(H),
\tag{1.3}
\]

and hence

\[
 MN-W
  =(1+2\delta_m+o(1)){WH\over m}=o(W),
\tag{1.4}
\]

\[
 N=(1+o(1)){W\over m}=o(W/H),
 \qquad HN=o(W).
\tag{1.5}
\]

For the exact positive-radius SCD census put

\[
 \gamma_d=N_d-N_{d+1}\quad(1\le d<H),
 \qquad \gamma_H=N.
\tag{1.6}
\]

Then

\[
 \sum_{d=1}^H\gamma_d=N_1,
 \qquad W-N_1={W\over m+1}.
\tag{1.7}
\]

The mean number of positive-radius chains per root is

\[
 {N_1\over N}
 ={m\over m+1}\lambda_H
 =m-1-2\delta_mH+o(H).
\tag{1.8}
\]

Thus the unused phase interval in a root has length

\[
 M-{N_1\over N}
 =(1+2\delta_m+o(1))H+1=\Theta(H).
\tag{1.9}
\]

The scalar capacity is therefore on the correct side with a genuine
\(\Theta(H)\) dump in every root.

## 2. Exact and common-floor nested profiles

For \(1\le q\le H\), divide

\[
 N_q=Nk_q+r_q,
 \qquad
 k_q=\left\lfloor{N_q\over N}\right\rfloor,
 \qquad 0\le r_q<N.
\tag{2.1}
\]

Then

\[
 k_1\ge k_2\ge\cdots\ge k_H=1.
\tag{2.2}
\]

The two uses of (2.1) must be distinguished.

### Lemma 2.1 (exact balanced integral profiles)

The roots can be indexed by \(j\in[N]\) and assigned integers

\[
 a_{j,q}=k_q+\mathbf 1_{\{j\le r_q\}}
\tag{2.3}
\]

so that

\[
 a_{j,1}\ge a_{j,2}\ge\cdots\ge a_{j,H}=1,
 \qquad
 \sum_{j=1}^{N}a_{j,q}=N_q
\tag{2.4}
\]

for every \(q\).

#### Proof

The sum in (2.4) is immediate from (2.1).  If
\(k_q=k_{q+1}\), monotonicity of \(N_q/N\) gives
\(r_q\ge r_{q+1}\), so the initial segments in (2.3) are nested.  If
\(k_q\ge k_{q+1}+1\), then even the smaller value at level \(q\) is at
least the larger value at level \(q+1\).  Finally
\(N_H=N\), so \(k_H=1,r_H=0\).  This proves (2.4). \(\square\)

Choose nested terminal phase intervals of lengths \(a_{j,q}\).  The
difference \(a_{j,d}-a_{j,d+1}\) is the number of tag-\(d\) phases in
root \(j\), and the unique terminal phase has tag \(H\).  Summing over
roots recovers (1.6) exactly.  By (1.8), all active intervals are proper
and all dumps have length \(\Theta(H)\).

This settles exact scalar tag integrality and one-path-per-root geometry.
It says nothing yet about physical target compatibility.

### Lemma 2.2 (common-floor profile and its total loss)

Alternatively, give **every** root the same threshold counts \(k_q\).
The signed quota shortfall at depth \(q\) is exactly \(r_q\), and

\[
 \sum_{q=1}^H r_q<HN=o(W).
\tag{2.5}
\]

Moreover

\[
 \sum_{q=1}^Hk_q=O(m^{3/2}).
\tag{2.6}
\]

#### Proof

Only (2.6) needs proof.  From the exact ratio product,

\[
 {N_q\over W}
 =\prod_{i=1}^q{m-i+1\over m+i}
 \le \exp\!\left(-{q^2\over m+H}\right)
 \qquad(q\le H).
\tag{2.7}
\]

Together with \(W/N=O(m)\), this gives

\[
 k_q\le {N_q\over N}
 \le Cm\exp\!\left(-{q^2\over m+H}\right).
\tag{2.8}
\]

The elementary Gaussian-sum estimate
\(\sum_{q\ge1}e^{-q^2/(m+H)}=O(\sqrt m)\) proves (2.6). \(\square\)

The common-floor profile loses exact SCD census but only by the
\(o(W)\) quantity (2.5).  Its advantage is that every root fibre is now
literally the same, which restores full coordinate transitivity.

## 3. The common-floor physical configuration hypergraph

It is convenient to use the lower-root form of a promotion ring.  A root
is

\[
 A\in\binom{[2m]}{m-H},
 \qquad U_A=[2m]\setminus A,qquad |U_A|=M.
\tag{3.1}
\]

Take a directed cyclic order \(\pi\) of \(U_A\) with a distinguished
phase zero.  Write \(I_\pi(i,s)\) for its cyclic interval of length
\(s\) beginning at phase \(i\).  For phase \(j\), put

\[
 X_j=A\cup I_\pi(j,H),
\tag{3.2}
\]

\[
 X^-_{j,q}=A\cup I_\pi(j+q,H-q),
 \qquad
 X^+_{j,q}=A\cup I_\pi(j-q,H+q).
\tag{3.3}
\]

Activate the phase set

\[
 P_q=\{0,1,\ldots,k_q-1\}
\tag{3.4}
\]

at threshold \(q\).  Thus phase \(j<k_1\) has radius

\[
 d_j=\max\{q:j<k_q\}.
\tag{3.5}
\]

The sets in (3.2)--(3.3) form a saturated symmetric chain through
radius \(d_j\).  The active middle phases are one interval, consecutive
phases are literal promotion states, and \(k_H=1\) ensures that at most
one phase reaches depth \(H\).  The standard cyclic-interval argument
also shows that, within one configuration, all designated masks of one
fixed signed rank are distinct.

Define \({\cal C}_{m,H}\) as the labelled multihypergraph whose vertices
are:

* a typed selector for each root \(A\);
* one typed middle vertex for every \(m\)-set; and
* for each \(q\), typed lower and upper copies of every rank-\(m-q\)
  and rank-\(m+q\) set.

A labelled edge consists of one root selector and all designated masks
of one aligned frame.  Parallel labelled edges are retained.  Root
selectors and physical lower-depth-\(H\) cells are typed separately; one
may instead identify the redundant copies without changing any matching
statement.

Every edge has

\[
 K=k_1+2\sum_{q=1}^Hk_q=O(m^{3/2})
\tag{3.6}
\]

physical cells, in addition to its root selector.  Let
\(\Delta=M!\) be the number of aligned directed frames in one root
fibre.

### Theorem 3.1 (fractional exactness and edge transitivity)

The action of \(S_{2m}\) is transitive on the labelled edges of
\({\cal C}_{m,H}\).  Giving every edge weight \(1/\Delta\) is a
fractional matching of value exactly \(N\).  Hence

\[
                         \nu^*({\cal C}_{m,H})=N.
\tag{3.7}
\]

#### Proof

A coordinate permutation can map one root to another and then map the
ordered labels of one aligned frame position by position to those of the
other.  This proves edge transitivity.

Every root selector has degree \(\Delta\).  By transitivity within each
typed physical rank and double counting, a middle target has degree
\(d_0\) and a signed depth-\(q\) target has degree \(d_q^\pm\), where

\[
 Wd_0=N\Delta k_1,
 \qquad N_qd_q^\pm=N\Delta k_q.
\tag{3.8}
\]

Their loads under weight \(1/\Delta\) are at most one by (2.1).
The total edge weight is \(N\).  Root capacity gives the reverse upper
bound, proving (3.7). \(\square\)

### Theorem 3.2 (exact global weighted representative constant)

Let \(\nu=\nu({\cal C}_{m,H})\).  For every nonnegative weight \(y\) on
the labelled configuration edges, some matching \(Q\) satisfies

\[
 \boxed{
 y(Q)\ge {\nu\over N}\,
 {1\over\Delta}\sum_{A}\sum_{e\in{\cal C}(A)}y_e.}
\tag{3.9}
\]

The coefficient \(\nu/N\) is best possible.  Equivalently, the complete
arbitrary-dual representative problem for this catalogue is exactly the
single unweighted integrality ratio \(\nu/N\).

#### Proof

Fix a maximum matching \(Q_0\).  Average its images under \(S_{2m}\).
Edge transitivity makes the inclusion probability of every labelled
edge equal to

\[
                         {\nu\over N\Delta}.
\tag{3.10}
\]

The expected weight of the random image is therefore the right side of
(3.9), so one image attains at least that value.  Taking \(y\equiv1\)
shows that no larger universal coefficient is possible. \(\square\)

The theorem is a genuine all-weight statement, but it supplies no lower
bound on \(\nu\).  Averaging only reproduces the factor \(\nu/N\).

## 4. Exact literal leave ledger

### Theorem 4.1 (global matching suffices for coefficient one)

If (0.2) holds, the central-through-\(H\) band has a literal Boolean-OR
word of length \(W+o(W)\).  After the audited economical exterior is
appended, the standing coefficient-one conclusion follows.

More exactly, if

\[
 \nu=N-L,
\tag{4.1}
\]

then the central length is at most

\[
 \boxed{
 W+2H(N-L)+2\sum_{q=1}^H(r_q+Lk_q).}
\tag{4.2}
\]

#### Proof

A matching of size \(N-L\) supplies \(N-L\) disjoint promotion paths,
each with \(k_1\) middle states.  Bridge-one compilation has length

\[
 (N-L)k_1+2H(N-L).
\tag{4.3}
\]

The selected middle owners are distinct.  Append each of the other
\(W-(N-L)k_1\) middle masks once.  This gives the baseline

\[
                         W+2H(N-L).
\tag{4.4}
\]

At either signed depth \(q\), the matching owns exactly
\((N-L)k_q\) distinct designated targets.  Its designated hole count is

\[
 N_q-(N-L)k_q=r_q+Lk_q.
\tag{4.5}
\]

Append these holes.  Nonowned outer collars may accidentally cover some
of them and can only improve the bound.  Summing (4.5) gives (4.2).

Now (1.5), (2.5), and (2.6) imply

\[
 2HN=o(W),\qquad
 2\sum_qr_q=o(W),\qquad
 L\sum_qk_q=o(W)
\tag{4.6}
\]

whenever \(L=o(N/\sqrt m)\).  This proves the central assertion.  Since
\(H/\sqrt m\to\infty\) and \(H=o(m)\), the economical exterior costs
\(o(W)\). \(\square\)

This theorem is not an exact SCD completion.  The appended targets are
literal singleton repairs.  It nevertheless proves coefficient one
with a single \(W\)-baseline if (0.2) is established.

## 5. Exact SCD anchors

Fix a full symmetric-chain decomposition \({\cal D}^0\) of
\(B_{2m}\).  Every root

\[
 A\in\binom{[2m]}{m-H}
\tag{5.1}
\]

lies on a unique chain of radius at least \(H\).  Write its central
segment as

\[
 A=C_A(-H)\subset C_A(-H+1)\subset\cdots
 \subset C_A(H).
\tag{5.2}
\]

These \(N\) segments are pairwise mask-disjoint at every rank.

### Lemma 5.1 (every SCD segment is one promotion phase)

The segment (5.2) can be realized as the tag-\(H\) phase of a promotion
ring rooted at \(A\).

#### Proof

Let \(z_1,\ldots,z_{2H}\) be the successive labels added along (5.2),
so

\[
 C_A(-H+t)=A\cup\{z_1,\ldots,z_t\}.
\tag{5.3}
\]

In the cyclic order on \(A^c\), put the \(2H\) labels consecutively in
positions chosen so that the nested intervals
\(I_\pi(-r,H+r)\), \(-H\le r\le H\), add them in the order
\(z_1,\ldots,z_{2H}\).  Explicitly, if the distinguished phase is
zero, place \(z_t\) at cyclic position \(H-t\).  Put the remaining
\(m-H\) labels in the complementary arc in an arbitrary order.  Then

\[
 A\cup I_\pi(-r,H+r)=C_A(r)
\tag{5.4}
\]

for every \(r\), proving the claim. \(\square\)

Thus every root has a fixed mask-disjoint anchor and
\((m-H)!\) residual anchored-frame choices.  Keeping the complete native
chains outside the band will later make an exact central repair into a
full SCD, not merely a clipped one.

## 6. The exact anchored leave absorber

There is first a direct one-baseline ledger which does not require an
exact SCD repair.  In a census-exact one-path-per-root atlas, let
\(E_0\) be the middle occurrence excess and let \(E_q^- ,E_q^+\) be
the two signed occurrence excesses at depth \(q\).  Since the occurrence
mass is \(N_1\) at the middle and \(N_q\) on either signed depth-
\(q\) rank, excess equals the number of holes beyond the unavoidable
middle singleton sector.  Consequently the literal central word has
length at most

\[
 \boxed{
 W+2HN+E_0+\sum_{q=1}^H(E_q^-+E_q^+).}
\tag{6.0}
\]

Indeed, the ring paths themselves cost \(N_1+2HN\); the middle holes
number \(W-N_1+E_0\), and the signed holes number \(E_q^\pm\).
Thus aggregate all-depth excess \(o(W)\) already proves the direct
coefficient-one word.  It does **not** prove exact `fcpath`, because the
holes have not been linked into symmetric chains.

Start with an anchored, one-segment-per-root atlas having the exact
census (1.6).  Its nonanchor chains may collide across roots.  Delete a
set \(D\) of nonanchor chains so that

1. every remaining designated mask is simple;
2. no remaining nonanchor mask meets an anchor mask; and
3. the anchors themselves are never deleted.

For \(e\in D\), write \(d(e)\) for its radius and put

\[
 D_q=|\{e\in D:d(e)\ge q\}|.
\tag{6.1}
\]

Because the undeleted core is simple and the original occurrence census
at either signed depth \(q\) was exactly \(N_q\), it leaves exactly
\(D_q\) holes at each such rank.  At the middle rank the positive-radius
core leaves

\[
                         W-N_1+|D|
\tag{6.2}
\]

holes.

Define the **hole-chain absorber hypergraph** \({\cal A}(D)\) as follows.
It has one token vertex for every labelled \(e\in D\), and physical
vertices equal to the signed holes and unused middle owners.  A candidate
edge incident with token \(e\), of radius \(d=d(e)\), is a saturated
symmetric chain

\[
 B_d^-\subset\cdots\subset B_1^-\subset X
 \subset B_1^+\subset\cdots\subset B_d^+
\tag{6.3}
\]

such that every \(B_q^\pm\) is in the corresponding signed hole set and
\(X\) is an unused middle owner.

### Theorem 6.1 (exact absorber equivalence)

The annular leave has an exact replacement family with the radius
multiset of \(D\) if and only if \({\cal A}(D)\) has a matching
saturating all token vertices.

#### Proof

An exact replacement family plainly supplies such a matching.  Conversely,
a token-saturating matching chooses \(|D|\) pairwise mask-disjoint chains.
At signed depth \(q\), precisely \(D_q\) chosen tokens have radius at
least \(q\).  The hole set also has size \(D_q\), so distinctness forces
the selected chains to cover it exactly.  Their middle owners are
distinct and avoid the core.  The remaining \(W-N_1\) middle holes are
declared radius-zero singleton chains.  This gives the required exact
central partition. \(\square\)

### Theorem 6.2 (path and full-SCD ledger)

Let \(b(D)\) be the number of maximal deletion intervals occupied by
\(D\) along the original root paths.  If an exact absorber from Theorem
6.1 can be equipped with complete radius-\(H\) collars having a
bridge-one cover by \(a(D)\) paths, then the resulting full SCD satisfies

\[
 \operatorname{fcpath}_{1,H}\le N+b(D)+a(D).
\tag{6.4}
\]

In particular, singleton absorber paths give

\[
 \operatorname{fcpath}_{1,H}\le N+b(D)+|D|\le N+2|D|.
\tag{6.5}
\]

#### Proof

Before deletion there is one promotion path per root.  Removing
\(b(D)\) path intervals increases the number of surviving components by
at most \(b(D)\), giving at most \(N+b(D)\) core paths.  Add the
\(a(D)\) absorber paths.

Inside \(|r|\le H\), Theorem 6.1 and the singleton chains partition
every rank.  Outside that band, retain the original portions of all
native radius-at-least-\(H\) chains of \({\cal D}^0\).  Their central
anchor segments are unchanged, so they splice back to those exterior
portions.  No chain of radius below \(H\) reaches an exterior rank.
Thus the completed object is a full SCD, and (6.4) is its bridge-one
path bound. \(\square\)

Since \(N=o(W/H)\), Theorem 6.2 proves the exact `fcpath` gate whenever

\[
                         b(D)+a(D)=o(W/H).
\tag{6.6}
\]

The stronger but simpler sufficient condition is \(|D|=o(W/H)\).

### Proposition 6.3 (collision excess versus simplifying deletion)

Let \(K_{\rm coll}\) be total occurrence excess over the middle and all
signed controlled cells, and let \(\tau\) be the minimum number of
nonanchor chains whose deletion makes the rest simple.  Then

\[
 {K_{\rm coll}\over2H-1}\le\tau\le K_{\rm coll}.
\tag{6.7}
\]

#### Proof

A nonanchor chain has radius at most \(H-1\), so it occupies at most
\(2H-1\) controlled cells.  Deleting it can reduce total excess by at
most that number, proving the lower bound.  For each repeated target,
mark all but one of its incident occurrences, and delete every chain
carrying a mark.  If the target contains its unique anchor occurrence,
leave that anchor unmarked and mark all nonanchor excess occurrences.
Thus only nonanchor chains are deleted.  At most one chain is charged
per unit of excess, and all repetitions disappear.  This proves the
upper bound. \(\square\)

Thus aggregate \(o(W)\) collision excess suffices for the direct word
ledger but does not by itself supply the \(o(W/H)\) exact absorber leave.

### Proposition 6.4 (separate Hall is insufficient)

Correct row counts and independent lower-to-middle and middle-to-upper
Hall matchings do not imply Theorem 6.1.

#### Proof

In \(B_4\), take the simple central core

\[
 1<14<124,\qquad
 3<23<123,\qquad
 4<24<234,
\tag{6.8}
\]

together with the singleton \(34\).  Its holes are

\[
 \{2\}\quad\hbox{at rank }1,
 \qquad \{12,13\}\quad\hbox{at rank }2,
 \qquad \{134\}\quad\hbox{at rank }3.
\tag{6.9}
\]

The lower incidence has the matching \(2\to12\), and the upper incidence
has the matching \(13\to134\).  But no common middle root
\(X\in\{12,13\}\) satisfies

\[
                         2\subset X\subset134.
\tag{6.10}
\]

Hence the residual radius-one chain does not exist.  This is an abstract
linkage obstruction; it is not asserted to be a promotion-ring leave.
\(\square\)

## 7. Why the representative/absorber must be global

The following specialization of the block-factor argument applies
directly to the common-floor catalogue.

### Theorem 7.1 (common-floor block hole floor)

Partition the \(N\) roots into blocks of size at most \(b\).  In each
block choose common-floor aligned frames by an arbitrary joint law, but
assume distinct blocks are independent and each individual root has the
uniform aligned-frame marginal.  If \(Z\) is the number of middle
targets missed by all selected active phase intervals, put

\[
 R_0=\binom mH,qquad
 L_0=\binom MH,qquad
 p_1={k_1\over L_0},qquad
 \theta_1=R_0p_1={Nk_1\over W}=1-o(1).
\tag{7.1}
\]

If \(bp_1\le\alpha<1\), then

\[
 \boxed{
 \mathbb EZ\ge
 W\exp\!\left(-{\theta_1\over1-\alpha}\right).}
\tag{7.2}
\]

Consequently a block-product law supported on \(o(W)\)-hole selections
must have

\[
 b\ge(1-o(1))p_1^{-1}
   =(1-o(1))\binom mH.
\tag{7.3}
\]

#### Proof

Fix a middle target.  Exactly \(R_0\) roots can display it.  At each such
root, a uniform aligned frame places its prescribed \(H\)-set in one of
the \(k_1\) active phase positions with probability \(p_1\).  If
\(Y_j\) is the number of hits from block \(j\), then

\[
 \mu_j=\mathbb EY_j=p_1r_j,
 \qquad \sum_j\mu_j=R_0p_1=\theta_1,
 \qquad \mu_j\le bp_1\le\alpha.
\tag{7.4}
\]

Markov's inequality gives
\(\Pr(Y_j=0)\ge1-\mu_j\).  Block independence and
\(\log(1-x)\ge-x/(1-\alpha)\) give

\[
 \Pr(\hbox{target missed})
 \ge\prod_j(1-\mu_j)
 \ge\exp\!\left(-{\theta_1\over1-\alpha}\right).
\tag{7.5}
\]

Sum over targets.  If a good supported law had
\(bp_1\le1-\eta\) along a subsequence, (7.2) would force a positive
linear expected hole count.  Hence \(bp_1\ge1-o(1)\).  Finally
\(R_0p_1=1-o(1)\), proving (7.3). \(\square\)

The same conclusion applies to the partial matching target (0.2).
Indeed, adjoin a null option at every root.  After symmetrizing a matching
of size \(N-L\), every root is nonnull with probability

\[
 \rho={N-L\over N}=1-o(m^{-1/2}),
\tag{7.5a}
\]

and, conditional on being nonnull, its aligned frame is uniform.  Replace
\(p_1\) in the proof by \(p_*=\rho p_1\).  Then
\(R_0p_*=1-o(1)\), so any independent-block representation of this
symmetrized near-matching still requires

\[
                         b\ge(1-o(1))R_0.
\tag{7.5b}
\]

Thus neither independent frames nor a block-product absorber whose
genuine correlation blocks have size \(o(\binom mH)\) can establish
(0.2).  The statement does not rule out sequential local moves whose
overlapping dependency component becomes root-star dense.

The same phenomenon survives a fixed SCD anchor.

### Theorem 7.2 (anchored block scale)

Fix the anchors from Section 5.  In every root choose the remaining
anchored-frame order uniformly, allow arbitrary dependence inside each
root block, and assume distinct blocks are independent.  If the law is
supported on **full \(M\)-window anchored-ring** selections with
\(o(W)\) middle holes, then the largest block has size at least (0.6).
The assertion also applies when an originally considered selection has
phases deleted or tagged: restoring all phases gives the corresponding
full anchored rings and can only reduce its hole set.

#### Proof

For a fixed root, write the anchored cyclic order as one fixed consecutive
block

\[
 z_1,\ldots,z_{2H}
\tag{7.6}
\]

and a uniformly ordered complementary set \(P\) of size
\(s=m-H\).  An \(H\)-window is of exactly one of three kinds.

* If it lies inside \(P\), a prescribed \(H\)-set occurs with
  probability
  \[
  p_{\rm int}={s-H+1\over\binom sH}.
  \tag{7.7}
  \]
* There are \(H+1\) deterministic \(H\)-windows inside the fixed
  \(2H\)-block.
* For every \(1\le k<H\), there are two seam types using a prescribed
  \(k\)-set of \(P\); each occurs with probability
  \(1/\binom sk\).

The total expected noninternal incidence mass per root is therefore

\[
 (H+1)+2(H-1)=3H-1.
\tag{7.8}
\]

Over all roots this is \((3H-1)N=o(W)\).  Let \(\theta_X\) be the total
mean full-ring load of middle target \(X\), and let \(\beta_X\) be its
noninternal part.  A supported \(o(W)\)-hole law has expected hole count
\(o(W)\), and

\[
 \Pr(X\hbox{ hit})\le\min(1,\theta_X).
\tag{7.9}
\]

Hence

\[
 \sum_X(1-\theta_X)_+=o(W).
\tag{7.10}
\]

Also \(\sum_X\theta_X=MN=W+o(W)\), so
\(\sum_X(\theta_X-1)_+=o(W)\).  Together with
\(\sum_X\beta_X=o(W)\), this shows that outside an \(o(W)\) exceptional
set,

\[
 \theta_X=1+o(1),\qquad \beta_X=o(1),
 \qquad p_{\rm int}r_X=1+o(1),
\tag{7.11}
\]

after the usual diagonal choice, where \(r_X\) is the number of
internal-compatible roots for \(X\).

For such a target, if every block contained at most
\((1-\eta)/p_{\rm int}\) internal-compatible roots, let
\(Y_j^{\rm int}\) count its internal hits from block \(j\), and put
\(\mu_j=\mathbb EY_j^{\rm int}=p_{\rm int}r_{j,X}\).  Block
independence and the Markov-product estimate give

\[
 \Pr(\hbox{no internal hit})
 \ge\prod_j(1-\mu_j)
 \ge\exp\!\left(-{p_{\rm int}r_X\over\eta}\right)
 =\exp(-(1+o(1))/\eta).
\tag{7.11a}
\]

If \(B_X\) is the event of at least one noninternal hit, the union bound
gives \(\Pr(B_X)\le\beta_X=o(1)\).  Therefore

\[
 \Pr(X\hbox{ missed})
 \ge \Pr(\hbox{no internal hit})-\Pr(B_X)
 \ge e^{-(1+o(1))/\eta}-o(1).
\tag{7.11b}
\]

This positive lower bound on a positive fraction of targets contradicts
the supported \(o(W)\)-hole assumption.
Therefore, for every fixed \(\eta>0\), all but \(o(W)\) targets have a
block containing at least \((1-\eta)/p_{\rm int}\) internal roots.
Letting \(\eta\downarrow0\) gives

\[
 b\ge(1-o(1))p_{\rm int}^{-1}
  =(1-o(1)){\binom{m-H}{H}\over m-2H+1}.
\tag{7.12}
\]

Stirling's formula gives (0.7). \(\square\)

The theorem is a no-go for bounded-component/product absorption, not for
a single globally designed atlas.  In the unanchored catalogue, averaging
one good deterministic atlas over coordinate permutations produces
uniform marginals with precisely the permitted global dependence.  For
the anchored statement the same is true only after averaging the pair
\((\mathcal D^0,\hbox{atlas})\); a general permutation moves the background
SCD, so no transitive averaging claim is made inside one fixed anchored
instance.

## 8. Adversarial audit and exact boundary

The following distinctions are essential.

1. **Full rings versus floor-profile configurations.**  A matching of
   full \(M\)-owner rings cannot leave \(o(N/\sqrt m)\) roots: capacity
   forces leave at least
   \[
   N-W/M=(1+2\delta_m+o(1))NH/m
          =\omega(N/\sqrt m).
   \]
   The common-floor edge has only \(k_1< W/N\) middle cells, so it avoids
   this scalar obstruction.

2. **Transitivity versus integrality.**  Theorem 3.2 gives the exact
   factor \(\nu/N\); it does not prove \(\nu/N=1-o(m^{-1/2})\).
   The uniform point lies in the elementary fractional matching polytope,
   but membership near the integral matching polytope is exactly (0.2).

3. **Unrestricted versus anchored catalogues.**  The common-floor
   transitivity is valid for unrestricted aligned frames.  Conditioning
   on one fixed SCD anchor restricts a frame to a prescribed consecutive
   \(2H\)-block and destroys fixed-instance edge transitivity.  Theorem
   7.2 quantifies, rather than removes, that restriction.

4. **Direct word versus exact `fcpath`.**  Theorem 4.1 appends physical
   holes and proves a literal word conditionally.  It does not turn those
   holes into symmetric chains.  Theorems 6.1--6.2 give the additional
   common-root condition required for a full SCD and exact `fcpath`.

5. **Marginal Hall versus common ownership.**  Proposition 6.4 shows
   that separate lower and upper Hall systems can choose incompatible
   middle roots.  The matching in \({\cal A}(D)\) is the minimum exact
   two-sided linkage statement; replacing it by row counts is invalid.

6. **Collision mass versus absorber size.**  The bounds (6.7) allow
   collision excess \(o(W)\) with a simplifying transversal much larger
   than \(o(W/H)\).  Exact `fcpath` needs the path-sensitive quantity in
   (6.6), whereas the direct word only needs aggregate repair \(o(W)\).

The strongest unproved positive statement exposed here is therefore:

> **Global anchored representative--absorber gate.**  Choose one exact
> balanced profile and one anchored phase segment in every root so that,
> after deleting nonanchor chains in \(b=o(W/H)\) path intervals, the
> remaining masks are simple and the resulting hole-chain hypergraph has
> a token-saturating matching with an \(o(W/H)\)-path bridge-one cover.

Its zero-deletion specialization gives
\(\operatorname{fcpath}_{1,H}\le N=o(W/H)\).  No theorem in this note
proves that global gate.  What has been closed is the scalar/tag census,
the all-weight dual bookkeeping for the unrestricted floor-profile
catalogue, the exact leave-to-full-SCD implication, and every
uniform-marginal independent-block route whose genuine correlation
blocks remain sub-star sized.
