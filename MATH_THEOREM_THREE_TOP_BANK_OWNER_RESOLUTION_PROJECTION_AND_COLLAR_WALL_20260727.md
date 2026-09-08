# Three-top bank installation: the exact owner projection and the collar wall

## A seeded-residual equivalence, exact growing codegrees, and a no-growth theorem for shore absorbers

Date: 2026-07-27

Scope: constant-one program; pure mathematics only.  No computation,
search, solver, or external matching theorem is used.

The two exact inputs are
`MATH_THEOREM_THREE_TOP_CONVEYOR_DENSE_ORBIT_PACKING_AND_SIGNING_20260727.md`
and
`MATH_THEOREM_CONVEYOR_BANK_LITERAL_OR_SPLICE_AND_DELAY_H_BOUNDARY_20260727.md`.

## 0. Verdict

Put

\[
 n=2m,\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N=N_H=\binom{2m}{m-H},
\tag{0.1}
\]

and assume

\[
 H\ge2,\qquad M\ge8H,\qquad H=o(m).
\tag{0.2}
\]

For the near-spanning conclusion, take the usual critical calibration:
\(H\) is the least integer for which \(R_H\ge M\).  Then

\[
 M\le R_H<(M-1){M\over m-H+1}=M+O(H),
 \qquad MN=W-o(W).                                      \tag{0.2a}
\]

Indeed \(R_{H-1}<M-1\) by minimality and
\(R_H/R_{H-1}=M/(m-H+1)\), which proves the strict upper
bound.  Since \(H=o(m)\), division by \(R_H\) gives the second
assertion.  The projection and wall theorems below do not require this
extra calibration; it is needed only for \(W-o(W)\) owner capacity.

Let

\[
 R_H={W\over N},\qquad
 P_H=9M^2+
 \left(9+256\sum_{q=1}^Hq^2\right)R_H.
\tag{0.3}
\]

The dense-orbit theorem supplies a bank \(\mathscr B\) from which we
fix

\[
 K=\left\lfloor {W\over P_H}\right\rfloor
\tag{0.4}
\]

three-top conveyors with pairwise disjoint top triples and pairwise
disjoint \(3M\)-element middle-owner sets.  The literal-bank theorem
compiles any shore choice with exactly \(6HK\) nonprincipal reset
positions and, at protected depth \(q\), with exactly
\(6(H+q-1)K\) changed ordered ports.

This note proves that these two theorems do **not** by themselves give
an absorber for the remaining owners.  The obstruction is an exact
projection identity:

\[
 \boxed{
 \mathbf 1_{\mathcal T(P^0)}=\mathbf 1_{\mathcal T(P^1)},
 \qquad
 \mathbf 1_{\mathcal O(P^0)}=\mathbf 1_{\mathcal O(P^1)}.}
\tag{0.5}
\]

Thus the difference of the two shore columns is killed by the complete
top-plus-middle incidence matrix.  Signing, shared collars, and every
sequence of shore switches leave all middle holes and all middle
multiplicities unchanged, not merely unchanged in expectation.

After one shore of every bank packet is frozen, global installation is
exactly the following seeded residual problem: find a matching in the
ordinary promotion-frame hypergraph after deleting the bank's \(3K\)
tops and \(3MK\) owners.  A completion covers \(W-o(W)\) middle owners
if and only if that residual matching covers

\[
                         W-3MK-o(W)                         \tag{0.6}
\]

residual owners.  The shore variables disappear completely from this
condition.

The packet reservoir is sparse on the owner scale:

\[
 3MK\le {3MW\over P_H}\le {W\over3M}=o(W),
\tag{0.7}
\]

and it is sparse on the root scale:

\[
 {3K\over N}
 \le {3R_H\over P_H}
 \le {3\over 9+256\sum_{q=1}^Hq^2}=o(1).
\tag{0.8}
\]

Even if one is allowed to replace all \(K\) packet skeletons by other
packet skeletons, at most \(3MK=o(W)\) previously uncovered owners can
become covered.  In particular the reservoir cannot repair a
\(\Theta(W)\) owner deficit.

There is a sharper local wall.  Delete \(b\) installed packets and
permit a replacement to use only their \(3Mb\) freed principal owners
and all \(6Hb\) reset endpoints as possible extra rank-\(m\) owner
slots.  If the replacement contains \(3b+g\) complete promotion
frames with pairwise distinct principal owners, then

\[
                         \boxed{Mg\le6Hb.}                   \tag{0.9}
\]

Consequently \(g=0\) for one packet, and any gain of one top requires

\[
                         b\ge\left\lceil{M\over6H}\right\rceil.
\tag{0.10}
\]

The reset/shared-collar bank is therefore subcritical as an owner
absorber.  Its collars cost only

\[
 6HK\le {2H\over3M^2}W=o(W),                         \tag{0.11}
\]

and its complete protected port boundary is

\[
 \sum_{q=1}^H6(H+q-1)K
 =(9H^2-3H)K
 \le {H^2\over M^2}W=o(W).                           \tag{0.12}
\]

Thus trace leakage is harmless, but it supplies no owner growth.

There is nevertheless an exact relative installation theorem. Starting
from any integral ordinary owner resolution with \(h\) missing owners,
delete every frame meeting a packet top or packet owner and then insert
the bank. The resulting integral installation has at most

\[
                         h+3M^2K=h+o(W)
\tag{0.13}
\]

missing owners. Thus the dense seed creates no new asymptotic integral
gate: an unseeded \(W-o(W)\) owner resolution automatically yields a
seeded one. What remains unproved is the **unseeded** growing-uniformity
matching theorem itself. Fractional feasibility does not establish it,
and packet shore choice or the collar compiler cannot substitute for it.

## 1. The ordinary owner-resolution hypergraph

Let

\[
 \mathcal T=\binom{[n]}M,
 \qquad
 \mathcal X=\binom{[n]}m.
\tag{1.1}
\]

For \(U\in\mathcal T\), let \(\pi\) be a directed cyclic order of
\(U\), modulo rotation.  Write

\[
 I_\pi(i,m)=\{\pi_i,\pi_{i+1},\ldots,\pi_{i+m-1}\},
 \qquad i\in\mathbb Z_M,
\tag{1.2}
\]

with cyclic subscripts, and put

\[
 \mathcal O(U,\pi)=
 \{I_\pi(i,m):i\in\mathbb Z_M\}.
\tag{1.3}
\]

The sets in (1.3) are distinct.  Indeed their complements in \(U\)
are the \(H\)-intervals of the same labelled cycle, and two such
intervals with the same underlying set have the same first position.

The ordinary owner-resolution hypergraph \(\mathcal G_H\) has vertex
classes \(\mathcal T,\mathcal X\) and edges

\[
 e(U,\pi)=\{U\}\sqcup\mathcal O(U,\pi).
\tag{1.4}
\]

It is \((M+1)\)-uniform.  Matching means both that a top is used at
most once and that a middle owner is used at most once.

### Proposition 1.1 (exact degrees and pair codegrees)

In the directed representation catalogue, every top and every owner
have degrees

\[
 R=(M-1)!,
 \qquad
 D=\binom mH H!m!={ (m!)^2\over(m-H)!}.
\tag{1.5}
\]

Two distinct tops have codegree zero.  A top-owner pair \((U,X)\) has
codegree zero unless \(X\subset U\), and otherwise has codegree

\[
                         H!m!.                              \tag{1.6}
\]

Let \(X,Y\in\mathcal X\) be distinct and put

\[
 d=|X\setminus Y|=|Y\setminus X|.
\tag{1.7}
\]

For \(1\le d<H\), their codegree is

\[
 d_{\mathcal G}(X,Y)
 ={2d!^2(m-d)!^2\over(m-H)!},
 \qquad
 {d_{\mathcal G}(X,Y)\over D}
 ={2\over\binom md^2}.                                 \tag{1.8}
\]

For \(d=H\), it is

\[
 d_{\mathcal G}(X,Y)=H!^2(m-H+1)!,
 \qquad
 {d_{\mathcal G}(X,Y)\over D}
 ={m-H+1\over\binom mH^2},                            \tag{1.9}
\]

and for \(d>H\) it is zero.  In particular the largest owner-owner
codegree is

\[
                         \Delta_{XX}={2D\over m^2}.          \tag{1.10}
\]

#### Proof

There are \((M-1)!\) directed cyclic orders of one labelled \(M\)-set,
proving the first formula in (1.5).  For a fixed owner \(X\), choose
the other \(H\) labels of its top in \(\binom mH\) ways.  In a fixed
top, make \(X\) one cyclic interval: order its labels in \(m!\) ways
and the complementary interval in \(H!\) ways.  This proves the second
formula in (1.5), and the same fixed-top count proves (1.6).

Suppose first that \(d<H\).  A common top is equivalently the complement
of an \((m-H)\)-set contained in \(X\cap Y\), so there are

\[
                         \binom{m-d}{H-d}                    \tag{1.11}
\]

common tops.  In one such top the two residual \(H\)-intervals have
overlap \(H-d\).  Their three nonempty Venn blocks, followed by the
outside block, occur in either orientation around the cycle.  Ordering
inside the blocks gives

\[
                         2d!^2(H-d)!(m-d)!                   \tag{1.12}
\]

orders.  Multiplying (1.11) and (1.12) gives (1.8).

If \(d=H\), the common lower root is forced and the two residual
\(H\)-sets are disjoint.  Contract each to one cyclic object.  Together
with the \(m-H\) outside singletons this gives \(m-H+2\) cyclic
objects, hence \((m-H+1)!\) cyclic orders; the two blocks have
\(H!^2\) internal orders.  This proves (1.9).  If \(d>H\), then
\(|X\cap Y|<m-H\), so no common lower root exists.  Formula (1.8) is
maximal at \(d=1\), while (1.9) is smaller for all sufficiently large
\(m\), proving (1.10). \(\square\)

### Corollary 1.2 (exact fractional root factor)

Under the critical calibration (0.2a), assigning weight \(1/R\) to
every ordinary edge representation is a fractional matching.  It gives
load one to every top and the common load

\[
                         {D\over R}={MN\over W}={M\over R_H}\le1
\tag{1.13}
\]

to every middle owner.  Its total edge weight is exactly \(N\).

#### Proof

The top load is \(R/R=1\), and the owner load is \(D/R\).  Double
counting all edge-owner incidences gives \(NRM=WD\), which proves
(1.13).  Finally there are \(NR\) edge representations, each of weight
\(1/R\). \(\square\)

The exact degrees are enormous and the normalized pair codegree is
small, but the uniformity \(M+1\) grows linearly.  These static facts
give the exact uniform fractional point above and efficient isolated
bites; they do
not, without a hereditary or absorber theorem, give an integral
near-perfect matching.

## 2. Adding packet and shore columns

For a labelled three-top conveyor packet \(P\), let

\[
 \mathcal T(P)=\{U_0(P),U_1(P),U_2(P)\},
\tag{2.1}
\]

and let \(P^0,P^1\) be its two shores.  Each shore consists of one
cyclic frame on every top in (2.1).  Let \(\mathcal O(P^\epsilon)\) be
the union of their three owner decks.

The local squarefree theorem says, exactly,

\[
 \mathcal O(P^0)=\mathcal O(P^1)=:\mathcal O(P),
 \qquad |\mathcal O(P)|=3M.                            \tag{2.2}
\]

Define the augmented owner-resolution system by adjoining the two
packet columns

\[
 E(P,\epsilon)=\mathcal T(P)\sqcup\mathcal O(P)
 \qquad(\epsilon\in\{0,1\})                            \tag{2.3}
\]

to the ordinary columns (1.4).  Equivalently, (2.3) is a
\(3(M+1)\)-uniform hyperedge with two labelled realizations.  The two
realizations meet in all top and owner vertices, so a matching cannot
select both.

The shore label is not forgotten.  It determines the protected flag
profile and hence the floor-gradient column.  It simply has no effect
on the owner projection.  The literal compiler adds the following
nonnegative budget coordinates to either realization:

\[
 c(P,\epsilon)=6H,
 \qquad
 b_q(P,0,1)=6(H+q-1),\quad1\le q\le H.                \tag{2.4}
\]

Here \(c\) counts reset endpoints and \(b_q\) counts changed
top-indexed ordered ports.  These are additive trace costs, not new
middle-owner vertices.  Top-disjointness already prevents two selected
packets from sharing a top-indexed collar carrier.  If one formally
records every protected port position in a separate layer, one packet
has total protected boundary uniformity

\[
 \sum_{q=1}^H6(H+q-1)=9H^2-3H.                       \tag{2.5}
\]

Thus the fully decorated packet column has growing size

\[
 3+3M+(9H^2-3H),                                      \tag{2.6}
\]

but its port layers add no collision beyond top collision in a
top-disjoint bank.

### Theorem 2.1 (owner-projection kernel)

Let \(A_{T,X}\) be the incidence matrix whose rows are all tops and
middle owners and whose columns include all labelled shore options.
For every packet \(P\),

\[
                         A_{T,X}(e_{P,1}-e_{P,0})=0.          \tag{2.7}
\]

Consequently, for arbitrary integers \(\sigma_P\), every combination

\[
                         \sum_P\sigma_P(e_{P,1}-e_{P,0})     \tag{2.8}
\]

has zero top and middle incidence.  In particular all middle coverage
indicators and all middle multiplicities are invariant under every
sequence of shore switches.

#### Proof

Both shores use the same three tops by construction, and (2.2) gives
the identical middle-owner set.  Their two incidence columns are
therefore equal on every row of \(A_{T,X}\), proving (2.7).  Linearity
gives (2.8).  Since an incidence coordinate records the exact
multiplicity of its owner, the final assertion is coordinatewise, not
merely aggregate. \(\square\)

This is the owner analogue of load neutrality, but it is stronger than
the protected-floor statement: it holds for the complete principal
middle deck and for every integral sequence of switches.

## 3. Exact seeded-residual equivalence

Let \(\mathscr B\) be a family of packet skeletons with pairwise
disjoint top and owner sets.  Choose one shore \(\epsilon(P)\) for each
\(P\in\mathscr B\), and put

\[
 T_{\mathscr B}=\bigsqcup_{P\in\mathscr B}\mathcal T(P),
 \qquad
 X_{\mathscr B}=\bigsqcup_{P\in\mathscr B}\mathcal O(P).
\tag{3.1}
\]

Let \(\mathcal G_H-\mathscr B\) denote the ordinary hypergraph obtained
by deleting the vertices in (3.1) and every incident ordinary edge.
In this section the augmented system means
\(\mathcal G_H\) together with only the two labelled columns of each
packet in \(\mathscr B\).

### Theorem 3.1 (installation is exactly residual matching)

There is a one-to-one correspondence between

1. matchings in this augmented system which contain exactly one shore
   of every packet in \(\mathscr B\) (and hence have no packet column
   outside \(\mathscr B\)), and
2. matchings in \(\mathcal G_H-\mathscr B\).

If the residual matching has \(f\) edges, the augmented matching uses

\[
 3|\mathscr B|+f\quad\hbox{tops},
 \qquad
 3M|\mathscr B|+Mf\quad\hbox{middle owners}.          \tag{3.2}
\]

It covers \(W-o(W)\) owners if and only if

\[
                         3M|\mathscr B|+Mf=W-o(W).            \tag{3.3}
\]

The correspondence and (3.2)--(3.3) are independent of every shore
choice.

#### Proof

Remove the frozen packet columns from an augmented matching.  Every
remaining ordinary edge avoids their top and owner vertices, hence lies
in \(\mathcal G_H-\mathscr B\).  Conversely, adjoining any residual
matching to one selected shore of every packet gives an augmented
matching because the deleted resource sets are precisely the possible
collisions.  This proves the bijection.  Each ordinary frame uses one
top and \(M\) owners; each packet uses three times those quantities.
Disjointness makes the sums in (3.2) exact, and (3.3) follows.  Theorem
2.1 removes the shore labels from all these equations. \(\square\)

Thus the dense bank is a legal prescribed seed.  It is not an absorber:
the completion problem is passed, without any gain, to the residual
ordinary hypergraph.

### Corollary 3.2 (conditional global literal compilation)

If the residual matching in Theorem 3.1 covers \(W-3MK-h\) owners,
where \(h=o(W)\), then the bank and residual frames have one literal OR
word of length

\[
 \begin{aligned}
 L
 &=3MK+Mf+6HK+2Hf+O(H)\\
 &=W-h+2H(3K+f)+O(H).
 \end{aligned}                                           \tag{3.4}
\]

In particular \(L=W+o(W)\).  Repairing the \(h\) missing middle owners
by one mask each, if required by the ambient construction, still gives
\(W+o(W)\).

#### Proof

The packet bank compiler contributes \(3MK\) principal endpoints and
\(6HK\) resets.  Apply the one-frame compiler to each of the \(f\)
residual cyclic frames; it contributes \(Mf\) principal endpoints and
\(2Hf\) resets.  Concatenation is source-blind, and one final ambient
reset costs \(O(H)\), proving the first line.  Equation (3.3) with
defect \(h\) proves the second.

Since the matching uses \(3K+f\le W/M\) pairwise owner-disjoint complete
frames,

\[
                         2H(3K+f)\le {2H\over M}W=o(W),      \tag{3.5}
\]

and \(h=o(W)\).  Appending the missing owner itself as one nonempty mask
represents that owner at its endpoint, so these repairs cost at most
\(h\) further symbols. \(\square\)

Thus the new splice theorem completely settles the word-interface side
once seeded residual matching is supplied.  It does not help prove that
matching.

### Theorem 3.3 (integral installation by pruning an unseeded resolution)

Let \(\mathcal F\) be any matching in the ordinary hypergraph
\(\mathcal G_H\), covering \(W-h\) owners. Let \(\mathscr B\) be the
dense bank of \(K\) pairwise top- and owner-disjoint packets. One can
delete frames from \(\mathcal F\) and insert one arbitrary shore of
every packet so that the resulting augmented matching covers at least

\[
                         W-h-3M^2K
\tag{3.6}
\]

owners. At the tuned scale \(3M^2K=o(W)\). Hence every unseeded
\(W-o(W)\) integral owner resolution admits, after \(o(W)\) owner loss,
a literal installation of the entire signed dense bank.

#### Proof

Delete from \(\mathcal F\) every frame whose top lies in
\(T_{\mathscr B}\), and every frame whose owner deck meets
\(X_{\mathscr B}\). At most \(3K\) frames are deleted for the first
reason. For the second reason, choose from each deleted frame one owner
in its intersection with \(X_{\mathscr B}\). Distinct frames of
\(\mathcal F\) have disjoint owner decks, so the chosen witnesses are
distinct. Therefore at most

\[
                         |X_{\mathscr B}|=3MK
\tag{3.7}
\]

additional frames are deleted.

The surviving ordinary frames avoid all packet tops and owners. We may
therefore adjoin either shore of every packet. If \(q\) frames were
deleted, the final owner count is

\[
                         (W-h)-Mq+3MK.
\tag{3.8}
\]

Using \(q\le3K+3MK\), this is at least

\[
 W-h-M(3K+3MK)+3MK=W-h-3M^2K,
\tag{3.9}
\]

which proves (3.6). Finally,

\[
 \frac{3M^2K}{W}\le\frac{3M^2}{P_H}
 =O\left(\frac{M}{H^3}\right)=o(1)
\tag{3.10}
\]

under the critical calibration, because
\(P_H=(256/3+o(1))MH^3\). All steps are integral; no fractional
matching or randomized rounding is used. \(\square\)

Combining Theorem 3.3 with Corollary 3.2 gives a literal word of length
\(W+o(W)\) whenever the unseeded matching has owner leave \(o(W)\).
The shore signs may be chosen after pruning, because Theorem 2.1 makes
the resource set independent of those signs.

## 4. Quantitative sparsity and residual degree loss

Let \(\mathscr B\) now be the dense-orbit subbank of size \(K\) fixed
in (0.4).  Equations (0.7)--(0.8) follow immediately from

\[
 P_H\ge9M^2,
 \qquad
 P_H\ge\left(9+256\sum_{q=1}^Hq^2\right)R_H.          \tag{4.1}
\]

The bank perturbs the ordinary catalogue only slightly on average at
the tuned scale.  Put

\[
                         \alpha={3M^2K\over W}.               \tag{4.2}
\]

### Proposition 4.1 (average residual-link loss)

For a top \(U\notin T_{\mathscr B}\), let \(\ell(U)\) be the fraction
of its \(R=(M-1)!\) cyclic frames which meet at least one owner in
\(X_{\mathscr B}\).  Then

\[
 {1\over N}\sum_{U\in\mathcal T\setminus T_{\mathscr B}}
 \ell(U)\le\alpha,
\tag{4.3}
\]

and, for every \(\eta>0\), at most \(\alpha N/\eta\) undeleted tops
lose more than an \(\eta\)-fraction of their frame catalogue through
owner deletion.  The separate deleted-top contribution is exactly
\(3K/N\).

#### Proof

Choose a uniformly random pair \((U,\pi)\) consisting of a top and one
of its cyclic frames.  By double counting frame-owner incidences, a
fixed owner occurs with probability

\[
                         {M\over W}.                         \tag{4.4}
\]

Indeed the total number of pairs is \(NR\), every pair has \(M\)
owners, and all \(W\) owners have equal degree.  A union bound over the
\(|X_{\mathscr B}|=3MK\) deleted owners gives probability at most

\[
                         {M\over W}(3MK)=\alpha.              \tag{4.5}
\]

Averaging first over \(\pi\) gives (4.3) on undeleted tops.  Markov's
inequality gives the exceptional-top count.  Deleted tops contribute
the separately stated \(3K/N\). \(\square\)

At the usual tuned scale, where \(3M^2/P_H=o(1)\), (4.3) says that all
but \(o(N)\) roots retain a \(1-o(1)\) fraction of their options.  Pair
codegrees can only decrease after vertex deletion.  This removes a
time-zero degree obstruction, but it is not an integral matching proof:
a growing-uniformity residual can still concentrate its surviving links
along the trajectory of a matching.

At the critical calibration this smallness is explicit.  Since
\(R_H\ge M\) and \(S_2(H)=\sum_{q\le H}q^2\),

\[
\alpha\le {3M^2\over256S_2(H)R_H}
\le {3M\over256S_2(H)}=O(M/H^3)=o(1).                \tag{4.6}
\]

For the last equality, the exact product

\[
 R_H=\prod_{i=1}^H{m+i\over m-i+1}
\tag{4.7}
\]

and \(\log(1+x)=x+O(x^2)\), uniformly for \(H=o(m)\), give
\(\log R_H=H^2/m+O(H/m+H^3/m^2)\).  Minimality in (0.2a), applied
also to \(H-1\), first gives \(H=\Theta(\sqrt{m\log m})\) from the
elementary two-sided bounds on this sum and then gives
\(H=(1+o(1))\sqrt{m\log m}\).  Hence \(M/H^3=o(1)\).

Taking \(\eta=\sqrt\alpha\) in Proposition 4.1 leaves only
\(\sqrt\alpha N=o(N)\) owner-damaged exceptional roots, in addition
to the \(o(N)\) roots occupied by the bank.  This is a genuine robust
degree statement, but it still stops before integral rounding.

## 5. The exterior-wall and no-growth inequalities

### Theorem 5.1 (packet-skeleton replacement wall)

Let \(\mathscr B_0,\mathscr B_1\) be two families, each containing at
most \(K\) pairwise owner-disjoint packet skeletons.  Then the number of
owners uncovered by \(\mathscr B_0\) and covered by \(\mathscr B_1\)
is at most

\[
                         3MK.                               \tag{5.1}
\]

Moreover,

\[
 \left\|
 \mathbf1_{X_{\mathscr B_1}}-
 \mathbf1_{X_{\mathscr B_0}}
 \right\|_1\le6MK.                                    \tag{5.2}
\]

For the dense reservoir both quantities are \(o(W)\).

#### Proof

The new family has at most \(3MK\) owners, proving (5.1).  Each of the
two incidence vectors in (5.2) has \(\ell_1\)-norm at most \(3MK\), so
the triangle inequality proves (5.2).  Equation (0.7) gives the final
assertion. \(\square\)

Thus even changing packet skeletons, rather than merely changing their
shores, cannot repair a positive-density owner leave at reservoir size
\(W/P_H\).

### Theorem 5.2 (shared-collar block-growth wall)

Fix \(b\ge1\) installed packets.  Suppose an augmentation deletes their
three frames per packet and installs \(3b+g\) complete promotion frames,
all with pairwise distinct principal middle owners.  Assume that outside
the \(3Mb\) freed principal owners the augmentation is allowed to use
only rank-\(m\) sets witnessed at the old bank's nonprincipal reset
endpoints.  Then

\[
                         Mg\le6Hb.                           \tag{5.3}
\]

In particular (0.10) holds, and no single packet can absorb one
additional frame under (0.2).

#### Proof

The deleted packets free exactly \(3Mb\) principal owner vertices.  The
replacement frames require exactly \(M(3b+g)\) distinct principal owner
vertices.  Hence at least \(Mg\) of them must come from outside the
freed principal set.

The literal-bank compiler has exactly \(6Hb\) nonprincipal reset
endpoints.  At any one physical endpoint the last-occurrence prefix
chain contains at most one set of rank \(m\).  Therefore these endpoints
can supply at most \(6Hb\) distinct exterior rank-\(m\) sets, even under
the most favorable possible alignment.  Thus \(Mg\le6Hb\).  Since
\(M\ge8H>6H\), \(b=1\) forces the integer \(g\) to be zero.  Solving
\(M\le6Hb\) gives (0.10). \(\square\)

This theorem grants the collar every possible benefit: all its middle
sets may be distinct, previously unused, and correctly aligned.  Actual
collar collisions can only strengthen the wall.

### Corollary 5.3 (no collar avalanche)

If disjoint blocks containing altogether at most \(K\) original packets
are augmented under the hypothesis of Theorem 5.2, their total gain in
complete frames is at most

\[
                         {6HK\over M}=o(K).                  \tag{5.4}
\]

The number of newly covered principal owners is at most \(6HK=o(W)\).

#### Proof

Sum (5.3) over the blocks.  Since \(H/M=o(1)\), the first assertion
follows.  Multiplication by \(M\), or direct use of the collar count,
gives the second. \(\square\)

The conclusion is not that no global augmentation exists.  It is that
an augmentation which reaches new owner territory only through the
bank's shared collars cannot bootstrap the sparse bank into a
near-spanning owner resolution.

## 6. Exact trace ledger

For completeness, the literal-bank theorem gives

\[
 C_{\rm reset}=6HK.                                      \tag{6.1}
\]

Using (0.4) and \(P_H\ge9M^2\),

\[
 C_{\rm reset}
 \le {6HW\over9M^2}
 ={2H\over3M^2}W=o(W),                                  \tag{6.2}
\]

which is (0.11).  Summing the exact depth-\(q\) boundary gives

\[
\begin{aligned}
 C_{\rm port}
 &=6K\sum_{q=1}^H(H+q-1)\\
 &=6K\left(H^2+{H(H+1)\over2}-H\right)\\
 &=(9H^2-3H)K\\
 &\le {9H^2\over9M^2}W
 ={H^2\over M^2}W=o(W),
\end{aligned}                                           \tag{6.3}
\]

proving (0.12).  A final ambient reset costs at most \(2H+1=o(W)\)
more.  Hence neither private resets nor a shared-collar realization can
cause a coefficient-sized trace loss for this bank.

## 7. The precise surviving theorem

Let \(\mathscr B\) be the selected and signed dense bank. Theorem 3.1
gives the exact seeded residual statement, while Theorem 3.3 shows that
it follows with \(o(W)\) additional loss from the corresponding unseeded
statement:

> **Unseeded promotion-frame near-resolution.** The ordinary hypergraph
> \(\mathcal G_H\) has an integral matching covering \(W-o(W)\) of its
> middle-owner vertices.

The static data available for this statement are:

1. ordinary uniformity \(M+1\), growing linearly;
2. exact degrees and codegrees (1.5)--(1.10);
3. deleted root fraction bounded by (0.8);
4. deleted owner fraction bounded by (0.7); and
5. average residual-link loss bounded by (4.3).

These imply the uniform fractional feasibility of the undeleted
catalogue up to a small average perturbation, but not its integral
rounding. The packet installation itself is closed up to \(o(W)\): once
an unseeded near-resolution is given, pruning installs the whole bank and
the splice theorem compiles it. Any proof of the remaining unseeded
statement must use a genuinely global integral matching or an absorber
whose exterior owner access is not confined to packet collars.

## 8. Proved and not proved

Proved here:

1. the exact augmented owner-resolution system with ordinary frame and
   two-shore packet columns;
2. exact ordinary degrees and all pair codegrees;
3. the shore-difference owner kernel (2.7);
4. the exact seeded-residual matching equivalence;
5. the \(o(N)\) root and \(o(W)\) owner size of the dense seed;
6. the average residual degree-loss bound;
7. integral pruning installation with owner loss at most
   \(3M^2K=o(W)\);
8. the packet-skeleton repair ceiling \(3MK=o(W)\);
9. the shared-collar growth wall \(Mg\le6Hb\); and
10. the complete \(o(W)\) reset and protected-port ledger.

Not proved here:

1. an unseeded integral matching covering \(W-o(W)\) owners;
2. dynamic hereditary estimates for a slow nibble;
3. an absorber with genuinely external, noncollar owner access; or
4. the coefficient-one theorem.

The bank is therefore globally installable at \(o(W)\) additional loss
relative to any unseeded near-resolution. Shore switches and collars do
not themselves construct that near-resolution; the remaining open gate
is the unseeded growing-uniformity matching problem.
