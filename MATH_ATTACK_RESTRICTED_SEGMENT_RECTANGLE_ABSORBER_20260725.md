# Restricted-segment rectangles repair the owner collapse

Date: 2026-07-25

Pure mathematics only. No computation, search, solver, web input, or
probabilistic black box is used.

## 0. Verdict

The complementary-long-segment repair of the full-packet rectangle works
exactly.

Let a top \(U\) have size

\[
M=m+H,
\]

and let \(1\le Q\le H\), with \(Q=o(m)\).  Start from two disjoint adjacent
position swaps \(\tau,\sigma\) in one cyclic order \(\pi\), and write

\[
\pi_{00}=\pi,
\qquad
\pi_{10}=\tau\pi,
\qquad
\pi_{01}=\sigma\pi,
\qquad
\pi_{11}=\tau\sigma\pi.
\tag{0.1}
\]

There are two cyclic phase intervals \(S,T\subseteq\mathbb Z_M\) such that

\[
S\cup T=\mathbb Z_M,
\qquad
|S\cap T|=O(Q),
\tag{0.2}
\]

and the two diagonal segment configurations

\[
\mathcal C^-=(\pi_{00}|S)\sqcup(\pi_{11}|T),
\qquad
\mathcal C^+=(\pi_{10}|S)\sqcup(\pi_{01}|T)
\tag{0.3}
\]

satisfy, simultaneously for every hard-band length

\[
m-Q\le s\le m+Q,
\tag{0.4}
\]

the exact identity

\[
\boxed{
\operatorname{Inc}_s(\mathcal C^+)
-\operatorname{Inc}_s(\mathcal C^-)
=B_s(\pi_{10})+B_s(\pi_{01})
-B_s(\pi_{00})-B_s(\pi_{11}).
}
\tag{0.5}
\]

Thus restricted segments retain the full rectangle's exact rank-selector
property on the entire hard band.  They avoid the fatal owner loss of a
full-packet \(0/2\) deployment:

* each configuration has \(M+O(Q)\) state occurrences;
* it contains at least \(M-O(1)\) distinct middle owners;
* relative to the principal packet \(\pi_{00}\), it loses only \(O(1)\)
  middle owners and adds only \(O(Q)\) duplicate occurrences;
* each of the two pieces is an actual contiguous promotion path; and
* two resets per top cost \(O(HN_H)=o(W)\), while all overlap state excess
  costs
  \[
  O(QN_H)=O(WQ/m)=o(W).
  \tag{0.6}
  \]

At every fixed controlled length the replacement of one principal packet by
one segment configuration removes at most four of that packet's interval
occurrences.  Hence its aggregate damage over the \(2Q+1\) hard rows is
only \(O(QN_H)=o(W)\), not \(O(Q^2N_H)\).

For a selector separation \(r\), the rank-\(r\) images of all relabelled
segment rectangles generate exactly

\[
\ker_{\mathbb Z}A_r,
\tag{0.7}
\]

the integral zero-point-margin lattice.  Both signs occur, so their
unrestricted real cone is \(\ker_{\mathbb R}A_r\).

What is not proved is a global positive absorber theorem.  A chosen
configuration \(\mathcal C^-\) can be switched once to \(\mathcal C^+\),
and the move is reversible, but the resulting pair of paths need not be the
negative diagonal required for the next desired rectangle.  The remaining
gate is therefore a support-feasible multi-top allocation/Markov theorem,
after an owner-only packet near-transversal has first been chosen.

## 1. Phase-restricted interval incidence

Fix a representative cyclic order

\[
\rho=(x_0,x_1,\ldots,x_{M-1})
\]

of \(U\), with positions indexed by \(\mathbb Z_M\).  For
\(1\le s<M\), let

\[
I_s(\rho,t)=\{x_t,x_{t+1},\ldots,x_{t+s-1}\}
\tag{1.1}
\]

be the cyclic \(s\)-interval beginning at phase \(t\).  For a phase set
\(R\subseteq\mathbb Z_M\), define

\[
B_s^R(\rho)=\sum_{t\in R}e_{I_s(\rho,t)}.
\tag{1.2}
\]

Thus the full packet incidence is

\[
B_s(\rho)=B_s^{\mathbb Z_M}(\rho).
\tag{1.3}
\]

If \(R\) is a cyclic interval of phases, the states indexed by \(R\), in
cyclic phase order, form one contiguous promotion path.  Consecutive
middle windows differ by deleting the first label and promoting the next
outside label.

## 2. The two-start support lemma

Let \(\tau\) swap the labels at adjacent positions \(p,p+1\) of \(\rho\).

### Lemma 2.1 (exact support of one adjacent swap)

For every \(1\le s<M\),

\[
B_s(\tau\rho)-B_s(\rho)
\]

is supported in phase space on exactly the two possible starts

\[
\boxed{
D_s(\tau)=\{p-s+1,\ p+1\}\subseteq\mathbb Z_M.
}
\tag{2.1}
\]

Equivalently, if \(t\notin D_s(\tau)\), then

\[
I_s(\tau\rho,t)=I_s(\rho,t).
\tag{2.2}
\]

#### Proof

An interval changes as an unlabelled set only if it contains exactly one of
the two swapped positions.  Among cyclic intervals of length \(s\), the
unique interval containing \(p\) but not \(p+1\) starts at \(p-s+1\), and
the unique interval containing \(p+1\) but not \(p\) starts at \(p+1\).
Every other interval contains both positions or neither.  This proves
(2.1)--(2.2).  At the degenerate endpoints the two signed target changes
may coincide or cancel, but there are never further affected starts.
\(\square\)

Over the hard band, the complete affected-start set is therefore

\[
\begin{aligned}
D_Q(\tau)
&=\bigcup_{s=m-Q}^{m+Q}D_s(\tau)\\
&=\{p+1\}
  \cup\{p-m-Q+1,\ldots,p-m+Q+1\},
\end{aligned}
\tag{2.3}
\]

with cyclic interpretation and

\[
|D_Q(\tau)|\le2Q+2.
\tag{2.4}
\]

The two components of (2.3) are precisely the two boundary neighborhoods
mentioned in the proposed repair.

## 3. Choosing the two long segments

### Lemma 3.1 (complementary phase intervals)

For \(1\le Q\le H<m\) and all sufficiently large \(m\), there are cyclic
phase intervals \(S,T\subseteq\mathbb Z_M\) such that

\[
S\cup T=\mathbb Z_M,
\qquad
D_Q(\tau)\subseteq S\cap T,
\qquad
|S\cap T|=O(Q).
\tag{3.1}
\]

#### Proof

Regard a cyclic interval as the circle with one open complementary arc.
Choose the complementary arc of \(S\) in one component of
\(\mathbb Z_M\setminus D_Q(\tau)\), and that of \(T\) in the other
component.  Extend the two complements until only \(O(Q)\)-neighborhoods of
their four endpoints remain doubly covered.  Then the complements are
disjoint, so \(S\cup T=\mathbb Z_M\), while every point of \(D_Q(\tau)\)
is in both \(S\) and \(T\).  Formula (2.3) shows that the total required
double cover is \(O(Q)\).

If the shorter gap in the complement closes when \(Q\) is comparable with
\(H\), take one segment to be the whole cut cycle and the other to be a
cyclic interval containing \(D_Q(\tau)\).  Its length is \(O(H)=O(Q)\) in
that case.  Thus (3.1) holds uniformly for \(1\le Q\le H\).  \(\square\)

Put

\[
R=S\cap T,
\qquad b=|R|=O(Q).
\tag{3.2}
\]

The two segments contain \(M+b\) phase occurrences in total.

## 4. Exact restricted rectangle identity

Let \(\tau\) and \(\sigma\) be disjoint adjacent position swaps in
\(\pi\).  They commute and do not move each other's two positions.  Use
the four orders (0.1), and let \(S,T\) satisfy (3.1) for \(\tau\).

For a segment configuration define

\[
\operatorname{Inc}_s(\mathcal C^-)
=B_s^S(\pi_{00})+B_s^T(\pi_{11}),
\tag{4.1}
\]

\[
\operatorname{Inc}_s(\mathcal C^+)
=B_s^S(\pi_{10})+B_s^T(\pi_{01}).
\tag{4.2}
\]

### Theorem 4.1 (segment rectangle equals full rectangle on the hard band)

For every \(m-Q\le s\le m+Q\), identity (0.5) holds.

#### Proof

Subtract (4.1) from (4.2):

\[
\begin{aligned}
\Delta_s^{\mathrm{seg}}
={}&\bigl[B_s^S(\pi_{10})-B_s^S(\pi_{00})\bigr]\\
&+\bigl[B_s^T(\pi_{01})-B_s^T(\pi_{11})\bigr].
\end{aligned}
\tag{4.3}
\]

The first bracket is the \(\tau\)-swap difference based at \(\pi\).  The
second is the negative \(\tau\)-swap difference based at \(\sigma\pi\).
Since \(\sigma\) is disjoint from \(\tau\), both differences have phase
support contained in the same set \(D_s(\tau)\).  By (3.1), that set is
contained in both \(S\) and \(T\).  Restricting either difference to its
respective segment therefore deletes no nonzero term.  Hence

\[
\begin{aligned}
\Delta_s^{\mathrm{seg}}
={}&B_s(\pi_{10})-B_s(\pi_{00})\\
&+B_s(\pi_{01})-B_s(\pi_{11}),
\end{aligned}
\]

which is (0.5).  \(\square\)

### Corollary 4.2 (exact vertical selector)

Suppose the cyclic separation between the two swap cuts is \(r\) in one
direction and \(M-r\) in the other.  Then throughout the hard band the
segment move is zero at every length except those among

\[
\{r,M-r\}.
\tag{4.4}
\]

At length \(r\) its image is, up to sign,

\[
e_{Kac}-e_{Kbc}-e_{Kad}+e_{Kbd},
\qquad |K|=r-2,
\tag{4.5}
\]

and the length-\((M-r)\) image is the complementary square.

In particular, choosing \(r=m-q\) isolates lower depth \(q\), and choosing
\(r=m+q\) isolates upper depth \(q\), subject to the same endpoint
exceptions as the full-packet selector.  For \(q>0\), the middle length
\(m\) is not exceptional, so

\[
\operatorname{Inc}_m(\mathcal C^+)
=\operatorname{Inc}_m(\mathcal C^-)
\tag{4.6}
\]

exactly, as a multiplicity vector.

### 4.1 The exact counterterm without the overlap condition

The overlap condition is also sharp in the following transparent sense.
For arbitrary \(S,T\) with \(S\cup T=\mathbb Z_M\), put

\[
\Delta_s^{\mathrm{full}}
=B_s(\pi_{10})+B_s(\pi_{01})
-B_s(\pi_{00})-B_s(\pi_{11}).
\]

Then

\[
\boxed{
\begin{aligned}
E_s
&:=\Delta_s^{\mathrm{seg}}-\Delta_s^{\mathrm{full}}\\
&=-\bigl[B_s^{S^c}(\pi_{10})-B_s^{S^c}(\pi_{00})\bigr]\\
&\phantom{={}}-\bigl[B_s^{T^c}(\pi_{01})-B_s^{T^c}(\pi_{11})\bigr].
\end{aligned}}
\tag{4.7}
\]

By Lemma 2.1, the first line on the right is supported only on
\(D_s(\tau)\setminus S\), and the second only on
\(D_s(\tau)\setminus T\).  Thus (4.7) is the exact boundary counterterm.
It vanishes under (3.1); if an affected start is omitted, its corresponding
two-target swap term survives unless it happens to cancel with the other
boundary term.

## 5. Middle-owner audit

At length \(m\), write

\[
F_t=I_m(\pi_{00},t),
\qquad
G_t=I_m(\pi_{11},t).
\tag{5.1}
\]

Both maps \(t\mapsto F_t\) and \(t\mapsto G_t\) are injective.  Since
\(\pi_{11}\) differs from \(\pi_{00}\) by two adjacent swaps,

\[
F_t=G_t
\qquad(t\notin D),
\tag{5.2}
\]

where

\[
D=D_m(\tau)\cup D_m(\sigma),
\qquad |D|\le4.
\tag{5.3}
\]

### Proposition 5.1 (near-full owner support)

Each of \(\mathcal C^-\) and \(\mathcal C^+\) has \(M+b\) middle-state
occurrences, at least \(M-8\) distinct middle owners, and at most \(b+8\)
duplicate occurrences.

Relative to its principal full packet, it misses at most four principal
owners and introduces at most four nonprincipal owners.

#### Proof

Consider \(\mathcal C^-\); the other diagonal is identical after relabeling.
Its owner multiset is

\[
F(S)\sqcup G(T).
\]

Within each segment there are no repetitions.  If \(t,u\notin D\) and
\(F_t=G_u\), then (5.2) gives \(F_t=F_u\), so injectivity forces \(t=u\).
Such a common owner therefore comes only from \(t=u\in S\cap T\).  Pairs
involving a phase of \(D\) contribute at most \(2|D|\le8\) further common
owners.  Hence

\[
|F(S)\cap G(T)|\le b+8.
\tag{5.4}
\]

Since \(|S|+|T|=M+b\), the union has size at least \(M-8\), and its
duplicate count is at most \(b+8\).

For the comparison with the principal packet, use

\[
\begin{aligned}
B_m^S(\pi_{00})+B_m^T(\pi_{11})-B_m(\pi_{00})
={}&B_m^{S\cap T}(\pi_{00})\\
&+B_m^T(\pi_{11})-B_m^T(\pi_{00}).
\end{aligned}
\tag{5.5}
\]

The first term consists of \(b\) extra occurrences.  The second is
supported on \(D\), so it removes and introduces at most four owners.
\(\square\)

This is the precise distinction from the failed full-packet \(0/2\)
proposal.  Two complete diagonal packets have \(2M\) occurrences but at
most \(M+4\) distinct owners.  The segment configuration has only
\(M+O(Q)\) occurrences and still has \(M-O(1)\) distinct owners.

If a family of principal packets already has middle collision
\(C_0=o(W)\), replacing every packet by one of these segment configurations
creates at most

\[
O(QN_H)=o(W)
\tag{5.6}
\]

additional duplicate occurrences and at most \(O(N_H)=o(W)\) new middle
holes.  Hence it retains \(W-o(W)\) distinct owners.  Moreover (4.6) says
that changing diagonals later preserves the entire resulting owner
multiplicity vector, not merely its support size.

## 6. Flag-hole and word-length ledgers

Fix a controlled length \(s\).  Comparing \(\mathcal C^-\) to the full
principal packet gives

\[
\begin{aligned}
\operatorname{Inc}_s(\mathcal C^-)-B_s(\pi_{00})
={}&B_s^{S\cap T}(\pi_{00})\\
&+B_s^T(\pi_{11})-B_s^T(\pi_{00}).
\end{aligned}
\tag{6.1}
\]

The first term only adds occurrences.  The second is the effect of two
adjacent swaps and is supported on at most four phase starts.  Thus the
segmentization removes at most four principal interval occurrences at
each length \(s\).  It may add \(b+4=O(Q)\) occurrences, but additions do
not create holes.

Consequently, if the chosen principal packets have aggregate flag-hole
count \(h\) over the hard band, either diagonal segmentization has flag-hole
count at most

\[
h+O(QN_H).
\tag{6.2}
\]

The factor is \(Q\), not \(Q^2\): there are \(O(Q)\) ranks and only
\(O(1)\) removed occurrences per top at each rank.

At calibrated depth,

\[
N_H=(1+o(1))\frac Wm.
\tag{6.3}
\]

The complete ledger is therefore:

\[
\begin{array}{c|c}
\text{source} & \text{aggregate excess or loss}\\ \hline
\text{overlap state occurrences} & O(QN_H)=O(WQ/m)=o(W)\\
\text{middle holes from segmentization} & O(N_H)=o(W)\\
\text{middle duplicate occurrences} & O(QN_H)=o(W)\\
\text{hard-band flag holes added} & O(QN_H)=o(W)\\
\text{two promotion-path resets per top} & O(HN_H)=o(W).
\end{array}
\tag{6.4}
\]

Here \(Q\le H=o(m)\).  The reset estimate uses the existing compiler bound
of \(O(H)\) bridge excess per initialized top path.  In particular, the
repair does not hide a factor \(H\) in the owner-overlap term: the duplicate
states are retained in their two paths, not cut out and repaired
individually.

## 7. Rank lattice and positivity

Let

\[
A_r:\mathbb Z^{\binom{[2m]}r}\longrightarrow\mathbb Z^{[2m]}
\]

be point-versus-\(r\)-set incidence.  The full-packet rectangle note proves
that elementary squares

\[
g(K;a,b;c,d)
=e_{Kac}-e_{Kbc}-e_{Kad}+e_{Kbd}
\tag{7.1}
\]

generate exactly \(\ker_{\mathbb Z}A_r\).  Every such square whose support
fits in a top is realized by a relabelled full rectangle.  Theorem 4.1
replaces that full rectangle by a segment rectangle without changing any
hard-band incidence.  Therefore:

### Theorem 7.1 (segment image lattice)

At every supported hard-band rank \(r\), the integral lattice generated by
all relabelled restricted-segment rectangles is

\[
\boxed{
\Lambda_r^{\mathrm{seg}}=\ker_{\mathbb Z}A_r.
}
\tag{7.2}
\]

There is no additional parity invariant.  Since both diagonal orientations
are available,

\[
\operatorname{cone}_{\mathbb R}
\{g,-g:g\text{ a segment rectangle image}\}
=\ker_{\mathbb R}A_r.
\tag{7.3}
\]

This is the unrestricted signed cone.  Positivity has three distinct
levels.

1. **One prescribed move is positive.**  Install \(\mathcal C^-\) as two
   promotion paths.  Replacing it by \(\mathcal C^+\) never creates a
   negative state multiplicity and preserves path count and state count.
2. **The move is reversible.**  After switching, the opposite orientation
   is support-feasible.
3. **Sequential connectivity is open.**  The new two-path configuration is
   not automatically the negative diagonal of a rectangle with a new
   separation, core, or target rank.  The equality of the abstract cone in
   (7.3) does not supply a nonnegative path through configurations.

Unlike the full-packet \(0/2\) proposal, positivity at level 1 no longer
destroys half the owner mass.  But levels 2--3 show why the local repair is
not yet a global absorption theorem.

## 8. The exact remaining two-stage gate

The viable order of construction is forced by the owner audit.

### Stage A: owner near-transversal

Choose one principal packet in every top so that the total middle collision
is \(o(W)\).  A full owner matching is unnecessary, but a one-packet-per-top
near-transversal is essential.  The old \(0/2\) diagonal deployment cannot
replace this stage.

### Stage B: restricted-segment absorption

On selected tops replace the principal packet by a diagonal segment
configuration.  The total owner and word-length perturbation is \(o(W)\)
by (6.4).  Then use rank-selecting diagonal switches to balance the flag
rows.

The remaining exact lemma may be stated as follows.

> **Restricted-segment absorber connectivity
> \(\mathrm{RSAC}_Q\).**  Starting from an owner near-transversal of
> principal packets, choose at most boundedly many two-segment
> configurations per top, with total overlap \(O(QN_H)\), so that a
> support-feasible sequence of diagonal switches leaves aggregate residual
> flag holes \(o(W)\) over all depths \(q\le Q\).

Theorem 4.1 proves \(\mathrm{RSAC}_Q\) after replacing
"support-feasible sequence" by "signed integral combination."  Proposition
5.1 proves that installing the absorber support need not spoil coefficient
one.  What remains is an allocation/connectivity theorem across many tops,
not an incidence identity, a rank-lattice question, or an owner-capacity
obstruction.

## 9. Audit ledger

### Proved

1. One adjacent swap affects exactly two phase starts at every interval
   length.
2. The affected starts over the full hard band occupy \(O(Q)\) boundary
   neighborhoods.
3. Two complementary cyclic phase intervals can cover all phases and
   doubly cover all affected starts with only \(O(Q)\) overlap.
4. The restricted diagonal difference equals the full four-order rectangle
   exactly at every hard-band length.
5. Omitting an affected start produces the explicit counterterm (4.7).
6. The exact lower/upper rank-selector property is retained.
7. Every segment configuration uses \(M+O(Q)\) occurrences and has
   \(M-O(1)\) distinct owners.
8. Middle duplicates, hard-band flag damage, overlap states, and resets all
   have aggregate \(o(W)\) cost at calibrated depth.
9. Switching diagonals preserves the complete middle-owner incidence
   vector.
10. The rank-\(r\) segment-image lattice is \(\ker_{\mathbb Z}A_r\), with
    no extra parity obstruction, and the unrestricted signed cone is the
    corresponding real kernel.

### Open

1. The owner-only near-transversal of principal packets.
2. A multi-top support-feasible sequence furnishing enough prescribed
   rectangle orientations and separations.
3. Positivity/connectivity of sequential correction, equivalently
   \(\mathrm{RSAC}_Q\).
4. Therefore aggregate \(o(W)\) flag holes and coefficient one by this
   route.

The proposed repair succeeds at exactly the point where the full-packet
rectangle failed: it retains the exact vertical trade while preserving
\(W-o(W)\) distinct owners.  Its unresolved part is now cleanly separated:
global positive scheduling of the locally valid two-segment absorbers.
