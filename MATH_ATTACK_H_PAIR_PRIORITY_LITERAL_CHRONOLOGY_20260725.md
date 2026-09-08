# Pair-priority swap cube: literal two-sided chronology is already closed

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, finite search,
solver, or long-running job is used.

## 0. Result

Put

\[
 n=2m+1,\qquad
 W=\binom{n}{m},\qquad
 N_1=\binom{n}{m-1},\qquad
 d=W-N_1=\frac{2W}{m+2}.
\tag{0.1}
\]

The adjacent pair-priority swap cube in
`PAIR_PRIORITY_ADJACENT_SWAP_CUBE_20260725.md` does not need a block-switch
refinement for literal chronology.  Every one of its corners already has
a flagged-transition path cover with negligible full signed rotor cost.

There is a notation collision in the source reports.  The quantity denoted
\(J(M_\rho)\) in their component estimate is the number of maximal selected
tight-row intervals.  In the notation of the exact portal ledger, it is
\(C\), not the priority-portal excess \(J_{\rm port}\).

### Theorem 0.1 -- every swap-cube corner is chronology-good

Fix \(H\le m-1\).  For every pair-priority permutation \(\rho\), and hence
for every corner \(\epsilon\) of the disjoint adjacent-swap cube, the
first-avoided token matching \(M_\rho\) has a vertex-disjoint path cover
such that

\[
 \boxed{
 C_\rho=O\left(\frac{W\log^2m}{m}\right),
 \qquad J_{\rm port}(M_\rho)=0.}
\tag{0.2}
\]

Every path simultaneously realizes its endogenous canonical lower and
upper token flags through depth \(H\) as literal contiguous unions.  Thus
its full signed core word
has exact length

\[
 \boxed{N_1+2HC_\rho.}
\tag{0.3}
\]

After giving each of the \(d\) omitted middle owners an arbitrary isolated
signed radius-\(H\) flag, the exact length is

\[
 \boxed{
 L_\rho=W+2H(C_\rho+d).}
\tag{0.4}
\]

Consequently, for every fixed \(A>0\) and
\(H=\lceil A\sqrt m\rceil\), for all sufficiently large \(m\) and
uniformly over all cube corners,

\[
 \frac{HC_\rho+J_{\rm port}(M_\rho)}W
 =O_A\left(\frac{\log^2m}{\sqrt m}\right)=o(1),
\tag{0.5}
\]

and

\[
 L_\rho=W+o(W).
\tag{0.6}
\]

No switch seam is omitted from (0.3)--(0.4).  The swap bits select one
final matching; they are not physical transitions that must be traversed
by the word.  After the bits are fixed, selected starts are regrouped into
their maximal tight-row intervals, and every change of interval is already
charged by \(2H C_\rho\).

This settles the literal lower-plus-upper chronology part of the swap-cube
route.  It does not prove constant one because the cube's flag-covariance
estimate (6.1) in the source report remains unproved.  No marginal claim is
re-audited here.

## 1. Tight local rows have zero portal cost

Partition \(2m\) coordinates into disjoint pairs

\[
 P_1,\ldots,P_m
\]

and leave one coordinate unpaired.  For a pair \(P\), put

\[
 Q_P=[n]\setminus P,
 \qquad |Q_P|=2m-1.
\]

Fix an exact central row factor on \(Q_P\).  A row has a cyclic order

\[
 \pi=(x_0,\ldots,x_{2m-2}),
\]

and its middle owners are the length-\(m\) cyclic windows

\[
 X_i=I_\pi(i,m).
\tag{1.1}
\]

Every coordinate is present in exactly \(m\) consecutive owners and absent
from exactly \(m-1\) consecutive owners.  In the increasing owner
orientation, the signed flags owned at \(X_i\) are

\[
 \Gamma^-_{i,q}=\bigcap_{s=0}^qX_{i+s}=I_\pi(i+q,m-q),
 \qquad
 \Gamma^+_{i,q}=\bigcup_{s=0}^qX_{i-s}=I_\pi(i-q,m+q).
\tag{1.2}
\]

The first-avoided extraction uses the decreasing orientation, in which the
same owner-aligned formulas become

\[
 \Gamma^-_{i,q}=\bigcap_{s=0}^qX_{i-s}=I_\pi(i,m-q),
 \qquad
 \Gamma^+_{i,q}=\bigcup_{s=0}^qX_{i+s}=I_\pi(i,m+q).
\tag{1.2a}
\]

### Lemma 1.1 -- exact two-sided tight interval lift

Let \(I\) be any linear interval of \(t\ge1\) consecutive owners in one
local row, traversed in the decreasing orientation used by the
first-avoided extraction.  For every \(H\le m-1\), all owner-aligned signed
flags in (1.2a) have a literal word of exact length

\[
 \boxed{t+2H.}
\tag{1.3}
\]

Every transition between selected owners is a nonqueued rotor transition,
so its priority-portal weight is zero.

#### Proof

The present residence \(m\) is at least \(H+1\), and the absent residence
\(m-1\) is at least \(H\).  Therefore the next \(H\) departure labels and
previous \(H\) departure labels form the exact lower and upper singleton
queues throughout the interval.  More explicitly, at \(X_i\) in decreasing
orientation the lower deletion queue is

\[
 (x_{i+m-1},x_{i+m-2},\ldots,x_{i+m-H}),
\]

the upper queue is

\[
 (x_{i+m},x_{i+m+1},\ldots,x_{i+m+H-1}),
\]

and the base is \(I_\pi(i,m-H)\), with cyclic subscripts.  Initialize the
first owner by writing those upper markers in reverse recency, then the
lower markers in reverse state order, and finally the base.  This takes
\(2H+1\) letters and its final letter already marks the first owner with
exactly the flags (1.2a).

Explicitly, the initialization word is

\[
 \{x_{i+m+H-1}\},\ldots,\{x_{i+m}\},
 \{x_{i+m-1}\},\ldots,\{x_{i+m-H}\},
 I_\pi(i,m-H).
\tag{1.3a}
\]

Its final state begins

\[
 (I_\pi(i,m-H),
  \{x_{i+m-H}\},\ldots,\{x_{i+m-1}\},
  \{x_{i+m}\},\ldots,\{x_{i+m+H-1}\},\ldots).
\tag{1.3b}
\]

Each of the remaining \(t-1\) owners is reached by one base update.  The
total is

\[
 (2H+1)+(t-1)=t+2H.
\]

At the terminal selected owner, the next \(H\) departure labels are already
present as its lower singleton queue, even if the corresponding later row
owners are unselected.  Thus no terminal collar entry is required.

The state prefixes are exactly the owner-aligned windows in (1.2a), so
every witness is a literal contiguous union.  No
transition has an equal lower flag at any depth, hence the portal-loop
identity gives weight zero.  \(\square\)

The older last-occurrence tail may remain refined.  It lies after every
displayed signed prefix and neither changes the witnesses nor creates a
reset charge.

## 2. The first-avoided extraction is a uniform path cover

Let \(\rho\) be any priority ordering of the pairs.  Assign every
rank-\((m-1)\) target \(S\) to the first pair in the \(\rho\)-order which
it avoids, and take its unique token in the chosen local factor for that
pair.  The proved first-avoided theorem gives exactly \(N_1\) distinct
middle owners and one token over every lower target.

Inside each local cyclic row, break the selected starts into maximal
consecutive intervals and orient them so that the assigned lower target is
the outgoing intersection colour.  These intervals are vertex-disjoint
paths because the selected middle owners are distinct.

### Lemma 2.1 -- uniform component bound

For every priority permutation \(\rho\), the number \(C_\rho\) of maximal
selected intervals satisfies

\[
 \boxed{
 C_\rho=O\left(\frac{N_1\log^2m}{m}\right).}
\tag{2.1}
\]

The implied constant is independent of \(\rho\), of the local factor
choices, and of the swap bits.

#### Proof

Only priority positions enter the component argument.  Write

\[
 A_m=\binom{2m-1}{m-1},
 \qquad R_m=\frac{A_m}{2m-1}
\tag{2.2}
\]

for the number of local targets and local rows.  At priority position
\(r\), selection inside one row requires meeting all \(r-1\) earlier
pairs.  For one earlier pair, the starts whose cyclic length-\((m-1)\)
window avoids both coordinates form at most two circular intervals.
Therefore the selected starts in one row have at most \(2r\) components.

If \(N_r\) is the number of targets whose first avoided pair occurs at
position \(r\), then

\[
 C_r\le\min\{N_r,2rR_m\}.
\tag{2.3}
\]

The already proved first-avoided tail estimate, which is invariant under
renaming the disjoint pairs, is

\[
 N_r\le C_0\sqrt m\,A_m(3/4)^{r-1}
\tag{2.4}
\]

for an absolute constant \(C_0\).  With
\(T=\lceil20\log m\rceil\),

\[
 \begin{aligned}
 C_\rho
 &\le\sum_{r\le T}2rR_m+
       \sum_{r>T}N_r\\
 &=O(R_m\log^2m)+O(A_m m^{-2})\\
 &=O(N_1\log^2m/m),
 \end{aligned}
\]

because \(A_m=\Theta(N_1)\).  Every step depends only on \(r\), not the
name of the pair occupying that priority position.  \(\square\)

### Proof of Theorem 0.1

Apply Lemma 1.1 to all \(C_\rho\) maximal selected intervals.  Their total
number of marked owners is \(N_1\), so summing (1.3) gives

\[
 N_1+2HC_\rho.
\]

Every internal edge is tight and has portal weight zero.  This proves
(0.2)--(0.3).  An isolated arbitrary signed radius-\(H\) flag costs
\(2H+1\) letters.  Adding the \(d\) omitted owners therefore gives

\[
 (N_1+2HC_\rho)+d(2H+1)
 =W+2H(C_\rho+d),
\]

which is (0.4).  Finally, for \(H=O_A(\sqrt m)\),

\[
 \frac{H(C_\rho+d)}W
 =O_A\left(\frac{\log^2m}{\sqrt m}\right)
  +O_A\left(\frac1{\sqrt m}\right)
 =o(1).
\]

This proves (0.5)--(0.6).  \(\square\)

## 3. Disjoint swap bits create no physical seam

For an odd priority position \(j\), let \(\mathcal D_j\) be the lower
targets which meet every earlier pair and avoid both pairs at positions
\(j,j+1\).  The proved disjointness identity is

\[
 \mathcal D_j\cap\mathcal D_k=\varnothing
 \qquad(j\ne k, j,k\text{ odd}).
\tag{3.1}
\]

Choosing any set of the disjoint adjacent transpositions produces one
ordinary priority permutation \(\rho_\epsilon\).  Hence its selected token
set is exactly the first-avoided matching \(M_{\rho_\epsilon}\), not a
formal signed combination of incompatible fragments.

### Proposition 3.1 -- seam-free cube selection

After any set of swap bits is fixed, regrouping the selected starts into
maximal intervals of their final local rows gives the path cover in
Theorem 0.1.  There is no connector between the old and new token assigned
to a target in \(\mathcal D_j\), and hence no additional switch-portal
term.

#### Proof

The conditional-expectation or vector-balancing argument selects a corner
of the finite cube.  It does not ask the literal word to visit intermediate
corners.  At the selected corner, every target has one actual token in one
actual local row.  Consecutive selected starts in that row use the tight
transition from Lemma 1.1; nonconsecutive starts lie in different maximal
components and are independently initialized.  The latter cost is already
the term \(2HC_{\rho_\epsilon}\).  There is no third kind of seam.
\(\square\)

This also explains why the macroscopic first affected family
\(\mathcal D_1\) is harmless chronologically.  Its switch may move many
tokens between two local factors, but both final token families are again
unions of tight-row intervals and are covered by the same uniform component
bound.

## 4. Exact constant-one boundary

The swap cube therefore satisfies the complete literal chronology demand
for the selected corner's endogenous canonical token flags:

\[
 2HC_\epsilon+J_{\rm port}(M_\epsilon)+2Hd=o(W)
\tag{4.1}
\]

uniformly over its vertices on every fixed Gaussian window.  Both lower
and upper flag witnesses are physical, every reset is charged, and no
switch interface is suppressed.

What remains in this lane is not a positive block-switch chronology lemma.
It is the source report's unproved load statement

\[
 \|\mu_c-\lambda\|_w^2-B
 +\frac14\sum_j\|\Delta_j\|_w^2=o(W).
\tag{4.2}
\]

If (4.2), or any weaker already-audited marginal condition sufficient for
the fixed-window theorem, is proved for one choice of the local factors,
the selected cube corner already has the literal word (0.4); no further
rotor, seam, reset, or block-switch theorem is needed.

Conversely, enlarging adjacent pair switches to block switches may be
useful for (4.2), but chronology supplies no reason to do so.  No
quantitative block covariance improvement is proved here, and none is
claimed.

Thus this report closes the assigned literal lower-plus-upper chronology
gate for the disjoint pair-priority cube, while leaving the explicitly
separate covariance gate open.  The constant-one conjecture is not proved.

## 5. A chronology-safe block-permutation refinement

Although no refinement is needed for the portal ledger, the disjoint
two-point switches give each lower root at most two possible token labels.
There is a larger chronology-safe family with a nontrivial label menu on
almost every root.

Put

\[
 b=\left\lceil\frac{4\log m}{\log(4/3)}\right\rceil
\tag{5.1}
\]

and divide the priority positions into consecutive blocks of size \(b\),
apart from a final shorter block.  Keep the order of the blocks fixed but
allow an arbitrary permutation of the pair priorities inside every block.

### Theorem 5.1 -- positive block menu with unchanged chronology cost

Every block-permutation choice satisfies (0.2)--(0.6).  Moreover, all but
\(o(W)\) rank-\((m-1)\) roots avoid at least two pairs in their earliest
priority block containing an avoided pair.  Hence all but \(o(W)\) roots
have at least two possible first-avoided pair labels across the
block-permutation family.

#### Proof

Every block choice is an ordinary priority permutation, so Theorem 0.1
applies without alteration.  It remains to count the exceptional roots.

Take independent coordinate indicators with

\[
 p=\frac{m-1}{2m+1}
\]

and later condition their total to be \(m-1\).  For one coordinate pair,
the probability that the random set meets the pair is

\[
 a=1-(1-p)^2<\frac34.
\tag{5.2}
\]

The pair events are independent before conditioning.  In a full block,
the probability of exactly one avoided pair is

\[
 b(1-a)a^{b-1}.
\]

Summing over the possible earliest active full blocks and charging the
final incomplete block by the event that every pair in the preceding
positions is met gives

\[
 \Pr_{\rm iid}(\text{exceptional})
 \le
 \frac{b(1-a)a^{b-1}}{1-a^b}+a^{m-b}.
\tag{5.3}
\]

The conditioning event has probability

\[
 \Pr(\operatorname{Bin}(2m+1,p)=m-1)=\Theta(m^{-1/2}),
\]

because its mean is exactly \(m-1\).  Therefore the exceptional fraction
among actual rank-\((m-1)\) roots is at most \(O(\sqrt m)\) times (5.3).
By (5.1)--(5.2),

\[
 b a^{b-1}=O(m^{-4}\log m),
 \qquad a^{m-b}=e^{-\Omega(m)},
\]

so this fraction is \(o(1)\).  Every nonexceptional root has two avoided
pairs in its earliest active block, and either may be placed first by an
internal block permutation.  \(\square\)

This is a positive enlargement of the switch family, but not a completed
flag-balancing theorem.  The block permutations are globally coupled, and
different first-avoided labels can still carry identical lower flag data
for symmetric local factor choices.  The theorem proves only that the
larger menu preserves the exact zero-portal two-sided chronology and
removes one-label pinning for almost every root.

## 6. Adversarial chronology audit

1.  The cube bits are not themselves literal rotor edges.  For arbitrary
    local factors, the old and new deletion queues of a switched token can
    be unrelated.  Even in the pair-symmetric choice, a distinct old/new
    owner transition is a priority-zero lower connector of cost \(H\) and
    does not reproduce the destination row's prescribed upper queue.
    Proposition 3.1 avoids this issue by selecting one corner first and
    independently initializing its final tight-row components.
2.  The flags literalized here are precisely the canonical token flags
    used in the swap cube's load vector.  They are not identified with an
    independently chosen AH-balanced flag extension.
3.  Every component reset appears in \(2HC_\rho\), and every isolated
    omitted-owner reset appears in \(2Hd\).  There is no uncharged collar
    or row-change term.
4.  Section 5 enlarges the priority menu but does not make the choices
    rootwise independent and does not prove that two labels yield two
    distinct lower ladders.
5.  The theorem therefore closes chronology uniformly over the cube but
    does not prove the covariance estimate (4.2) or the constant-one
    conjecture.

The main theorem, its two-sided ownership indexing, and all length and
component estimates were independently audited after these scope
corrections.
