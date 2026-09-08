# Paired-conveyor obstruction and a separated eight-template Latin coboundary

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, search, or web input
is used.

## 0. Outcome

The \(W/4\) owner-duplication obstruction in
FOUR_TEMPLATE_PAIRED_CONVEYOR_OWNER_DUPLICATION_AUDIT_20260725.md is
correct. Two qualifications strengthen it.

1. The conveyor states called coalesced have the same lower block and
   collar, hence the same exposed owners, but their residual blocks and
   carrier tags can still differ.
2. A useful four-template block separates its two source owners only when
   the collar swap straddles positions \(Q,Q+1\). It separates its endpoint
   owners only when the source swap occupies positions \(Q-2,Q-1\). Thus
   no useful adjacent-swap block is owner-simple at both boundaries.

There is a genuine local positive replacement. Four carrier chains arranged
as a Boolean Latin square give an eight-path switch

\[
 4\text{ positive paths}\longleftrightarrow4\text{ negative paths}
\]

with all of the following properties.

* Each side uses one path on each of four distinct carriers.
* All twelve middle-owner occurrences in the four selected two-step path
  segments—four sources, four intermediate states, and four endpoints—are
  pairwise distinct on either side.
* The complete prefix-incidence difference vanishes at every Boolean rank
  except one prescribed interior rank. At that rank it is one elementary
  four-mask rectangle, with
  \(\ell^1\)-norm and squared \(\ell^2\)-norm both equal to four.
* Within each carrier the two routes have the same source, the same
  two-step endpoint, and the same continuation. The switch has no reset,
  seam, or length toll.

This settles the local separated eight-template problem.  The formerly
missing transport is now closed: two common-departure updates take the
complementary triple fibres to fresh singleton fibres without an owner
collision, and the common residual reservoir is conserved.  See
`MATH_ATTACK_PSTUBE8_LATIN_TRANSPORT_AND_PROTECTED_STRIP_ABSORBER_20260725.md`.
The remaining dense-conveyor problem is the global committed whole-tube
owner near-factor, not a finite connector.

## 1. Corrected audit of the paired conveyor

Write a quotient state as

\[
 \omega=(L;z_1,\ldots,z_{2Q};R).
\]

Its middle owner is

\[
 F_Q(\omega)=L\cup\{z_1,\ldots,z_Q\}.
\tag{1.1}
\]

Suppose two source collars differ only by interchanging positions
\(p,p+1\).

### Lemma 1.1 (both boundary tests)

The two source owners agree if and only if

\[
 p\ne Q.
\tag{1.2}
\]

After the useful two-update diamond, the endpoint owners agree if and only
if

\[
 p\ne Q-2.
\tag{1.3}
\]

In particular, for \(Q\ge3\), no useful block has distinct owners at both
its source and its endpoint.

#### Proof

At the source, both swapped labels belong to the first \(Q\) collar
positions when \(p<Q\), and neither belongs to them when \(p>Q\). The
owner changes only when the pair straddles the cut, namely \(p=Q\).

Two updates move the old pair to positions \(p+2,p+3\). It then straddles
the owner cut exactly when \(p+2=Q\), namely \(p=Q-2\). If the pair has
fallen into the unresolved tail, the exposed endpoint states coalesce, so
the same conclusion holds. \(\square\)

The front injection begins with a common lower block and collar, so its
source owners agree. Its residual blocks need not agree.

### Lemma 1.2 (duplicate-pair charge)

Suppose \(J\) occurrence-disjoint pairs of middle-owner occurrences are
designated, with equal owner in each pair. If

\[
 D_0=\sum_X(\mu(X)-1)_+,
\]

then

\[
 \boxed{D_0\ge J.}
\tag{1.4}
\]

#### Proof

Let \(j_X\) be the number of designated pairs carrying \(X\).
Occurrence-disjointness gives \(\mu(X)\ge2j_X\), hence
\((\mu(X)-1)_+\ge j_X\). Sum over \(X\). \(\square\)

### Theorem 1.3 (quantitative conveyor obstruction)

Let \(N_H\) be the number of calibrated carriers and leave \(R\) carriers
unpaired. Run the odd conveyor, or the explicitly completed even conveyor,
on every remaining adjacent carrier pair. Then

\[
 \boxed{
 D_0\ge
 \frac14MN_H-
 O\!\left(MR+\frac{MN_H}{Q}+QN_H\right).}
\tag{1.5}
\]

Consequently, if \(R=o(N_H)\), \(Q\to\infty\), \(Q=o(M)\), and
\(MN_H=W-o(W)\), then

\[
 \boxed{D_0\ge(1/4-o(1))W.}
\tag{1.6}
\]

#### Proof

An odd cycle has one two-update injection and \(Q\) useful two-update
blocks, hence \(2(Q+1)\) updates. At most one useful source has \(p=Q\);
the injection source agrees. Thus at least \(Q\) source pairs per cycle
have equal owners.

For the even conveyor, take the two-update injection, one common update
which shifts positions \(1,2\) to \(2,3\), the \(Q-1\) useful blocks at
\(p=2,4,\ldots,2Q-2\), and one common cleanup update. This again uses
\(2(Q+1)\) updates. The injection and cleanup sources agree, and at least
\(Q-2\) useful sources agree, again producing at least \(Q\) designated
pairs.

After \(O(Q)\) initial and terminal updates, one carrier pair supplies

\[
 J_{\mathrm{pair}}
 \ge Q\left\lfloor
 \frac{M-1-O(Q)}{2(Q+1)}
 \right\rfloor
 =\frac M2-O(M/Q+Q)
\tag{1.7}
\]

occurrence-disjoint equal-owner pairs. Different carrier pairs use
disjoint occurrences. Lemma 1.2 and multiplication by
\((N_H-R)/2\) prove (1.5). \(\square\)

There is no hidden carrier-pairing assumption. Partition \([2m]\) into
\(m\) coordinate pairs. On every \(M\)-set having a mixed coordinate
pair, flip the least mixed pair. This is a fixed-point-free involution
pairing Johnson-adjacent carriers. The exceptional carriers are unions of
whole coordinate pairs, at most \(2^m=o(N_H)\). Adjacent carriers
intersect in \(M-1=m+H-1\) coordinates, enough to contain the common
visible set of size \(m+Q+2\) when \(H-Q\ge3\).

## 2. The Latin-square chain identity

Put

\[
 k_-=m-Q-1,\qquad k_+=m+Q.
\tag{2.1}
\]

Choose four special labels

\[
 S=\{s,s',y,y'\}
\tag{2.2}
\]

and a saturated chain
\(\mathcal K=(K_k)_{k_-\le k\le k_+}\), disjoint from \(S\), with

\[
 |K_k|=k-1.
\tag{2.3}
\]

Define four saturated base chains

\[
 C^s_k=K_k+s,\quad
 C^{s'}_k=K_k+s',\quad
 C^y_k=K_k+y,\quad
 C^{y'}_k=K_k+y'.
\tag{2.4}
\]

For a base chain \(\mathcal C\) and arrival labels \(u,v\), write

\[
 D_{\mathcal C}(u,v)
 :=I(P_{\mathcal C}^{\,u})-I(P_{\mathcal C}^{\,v}).
\tag{2.5}
\]

At Boolean rank \(\ell=k+1\), the complete arrival-diamond theorem gives

\[
 D_{\mathcal C}(u,v)_\ell
 =e_{C_k+u}-e_{C_k+v}.
\tag{2.6}
\]

### Lemma 2.1 (rankwise Latin cancellation)

\[
 \boxed{
 D_{C^s}(y,y')
 -D_{C^{s'}}(y,y')
 -D_{C^y}(s,s')
 +D_{C^{y'}}(s,s')=0}
\tag{2.7}
\]

at every Boolean rank.

#### Proof

At base rank \(k\), the left side is

\[
\begin{aligned}
 &e_{K_k+s+y}-e_{K_k+s+y'}
 -e_{K_k+s'+y}+e_{K_k+s'+y'}\\
 &\quad-e_{K_k+y+s}+e_{K_k+y+s'}
 +e_{K_k+y'+s}-e_{K_k+y'+s'}.
\end{aligned}
\]

Every mask cancels with its identical opposite term. Each diamond is zero
outside its displayed rank range. \(\square\)

## 3. An adjacent perturbation isolates one rank

Interchange two adjacent collar increments \(\alpha,\beta\) of
\(\mathcal K\). Let \(\widetilde{\mathcal K}\) be the resulting chain,
which differs from \(\mathcal K\) only at base rank \(k_*\), and put

\[
 \widetilde C^s_k=\widetilde K_k+s.
\tag{3.1}
\]

The ordinary collar-swap range is

\[
 m-Q+2\le r=k_*+1\le m+Q.
\tag{3.2}
\]

Define

\[
\begin{aligned}
 \Omega={}&D_{\widetilde C^s}(y,y')
 -D_{C^{s'}}(y,y')\\
 &-D_{C^y}(s,s')
 +D_{C^{y'}}(s,s').
\end{aligned}
\tag{3.3}
\]

### Theorem 3.1 (separated eight-template coboundary)

The vector \(\Omega\) vanishes at every rank except
\(r=k_*+1\). If

\[
 K_{k_*}=E+\alpha,\qquad
 \widetilde K_{k_*}=E+\beta,
\tag{3.4}
\]

then

\[
 \boxed{
\begin{aligned}
 \Omega_r={}&e_{E+s+\beta+y}
             -e_{E+s+\beta+y'}\\
            &-e_{E+s+\alpha+y}
             +e_{E+s+\alpha+y'}.
\end{aligned}}
\tag{3.5}
\]

The four masks are distinct and

\[
 \boxed{\|\Omega\|_1=4,\qquad\|\Omega\|_2^2=4.}
\tag{3.6}
\]

#### Proof

Add and subtract \(D_{C^s}(y,y')\) in (3.3). Lemma 2.1 cancels the four
unperturbed chains, leaving

\[
 \Omega=D_{\widetilde C^s}(y,y')-D_{C^s}(y,y').
\]

The two \(s\)-chains differ only at \(k_*\), so every other rank cancels.
Substitution of (3.4) proves (3.5). The labels
\(\alpha,\beta,s,y,y'\) are distinct and outside \(E\), giving (3.6).
\(\square\)

Expanding (3.3), its two positive configurations are

\[
 \boxed{
 \mathcal P^+=
 \{P_{\widetilde C^s}^{\,y},
   P_{C^{s'}}^{\,y'},
   P_{C^y}^{\,s'},
   P_{C^{y'}}^{\,s}\},}
\tag{3.7}
\]

\[
 \boxed{
 \mathcal P^-=
 \{P_{\widetilde C^s}^{\,y'},
   P_{C^{s'}}^{\,y},
   P_{C^y}^{\,s},
   P_{C^{y'}}^{\,s'}\}.}
\tag{3.8}
\]

Thus there are eight path templates, four on either side.

## 4. Exact physical realization on four carriers

Let \(x\) be the first increment of \(\mathcal K\), put

\[
 A=K_{k_-}+x,
\tag{4.1}
\]

and let the remaining \(2Q\) increments be the common collar
\(Z=(z_1,\ldots,z_{2Q})\). Thus \(|A|=m-Q-1\). Choose

\[
 x'\in A,\qquad x'\ne x.
\tag{4.2}
\]

Choose a common filler \(F\) of size \(H-Q-4\) and distinct labels
\(f_s,f_{s'},f_y,f_{y'}\), all disjoint from \(A\cup Z\cup S\). This is
possible for all sufficiently large \(m\), since the complement of
\(A\cup Z\cup S\) has size \(m-Q-3\) and \(H=o(m)\).

For \(t\in S\), define

\[
 U_t=A\cup Z\cup S\cup F\cup\{f_t\}.
\tag{4.3}
\]

Every \(U_t\) has size \(M=m+H\), and the four carriers are distinct.
Their source lower and residual blocks are

\[
 L_t=A+t,\qquad
 R_t=(S\setminus\{t\})\cup F\cup\{f_t\}.
\tag{4.4}
\]

Use the following chain and arrival pairs:

\[
\begin{array}{c|c|c}
\text{carrier}&\text{base chain}&\text{arrival pair}\\ \hline
U_s&\widetilde C^s&(y,y')\\
U_{s'}&C^{s'}&(y,y')\\
U_y&C^y&(s,s')\\
U_{y'}&C^{y'}&(s,s')
\end{array}
\tag{4.5}
\]

and use departures \(x,x'\) in every carrier.

### Theorem 4.1 (legal four-carrier switch)

The exchange

\[
 \boxed{\mathcal P^-\longleftrightarrow\mathcal P^+}
\tag{4.6}
\]

is a literal one-path-per-carrier switch with complete incidence difference
\(\Omega\). It changes no initialization, reset, continuation, or
word-length term.

#### Proof

Equations (4.3)--(4.5) contain every source-chain coordinate and every
required arrival label. Thus all eight routes are legal. Equations
(3.7)--(3.8) choose exactly one route on each tag. Within one tag, reversing
the two arrivals preserves the source and the state after two updates.
Only the intermediate state contributes to the route difference, and
Theorem 3.1 applies. \(\square\)

## 5. All twelve local middle owners are distinct

For an unperturbed chain \(C^t\), the three middle owners in either
two-step route are

\[
 \text{source: }C^t_m=K_m+t,
\tag{5.1}
\]

\[
 \text{intermediate: }C^t_{m-1}+u,
\tag{5.2}
\]

where \(u\) is the first arrival, and

\[
 \text{endpoint: }C^t_{m-2}+\{u,v\}
 =K_{m-2}+t+u+v.
\tag{5.3}
\]

Equation (5.3) follows directly from the endpoint state: the two
departures reappear among its first \(Q\) collar positions, while both
arrivals enter the lower block.

### Theorem 5.1 (twelve-owner separation)

On either side of (4.6), all twelve source, intermediate, and endpoint
owner occurrences are pairwise distinct.

#### Proof

The source owners meet \(S\) in the four singletons

\[
 \{s\},\quad\{s'\},\quad\{y\},\quad\{y'\}.
\tag{5.4}
\]

On the positive side, the intermediate owners meet \(S\) in

\[
 \{s,y\},\quad\{s',y'\},\quad
 \{y,s'\},\quad\{y',s\};
\tag{5.5}
\]

on the negative side they meet \(S\) in

\[
 \{s,y'\},\quad\{s',y\},\quad
 \{y,s\},\quad\{y',s'\}.
\tag{5.6}
\]

Each list contains four distinct two-subsets. The endpoint owners meet
\(S\) in the four distinct triples

\[
 \{s,y,y'\},\quad\{s',y,y'\},\quad
 \{y,s,s'\},\quad\{y',s,s'\}.
\tag{5.7}
\]

Owners from different state layers cannot agree because they contain,
respectively, one, two, and three special labels.

The perturbed \(s\)-chain differs at only \(k_*\). If
\(k_*\notin\{m,m-1,m-2\}\), none of these owners changes. If \(k_*\)
is one of those indices, the corresponding \(s\)-owner replaces
\(\alpha\) by \(\beta\), where \(\beta\) is outside the relevant
unperturbed \(K\)-set and outside \(S\). Its special-label count is
unchanged, and the new coordinate \(\beta\) prevents equality with the
other three owners in that layer. \(\square\)

Thus the Latin square removes both boundary defects from Lemma 1.1.

## 6. Immediate repetition is impossible

At the four sources, the lower blocks have signatures

\[
 A+t,\qquad t\in S,
\tag{6.1}
\]

so they are singleton-special fibres. After the two updates, their lower
blocks have the four complementary triple signatures

\[
 (A\setminus\{x,x'\})+T,\qquad T\in\binom S3.
\tag{6.2}
\]

In each carrier, the one unused special label is the unique member of
\(S\) left in the residual block.

### Proposition 6.1 (immediate-repeat obstruction)

Using one nonzero arrival-diamond edge on each of these same four endpoint
states cannot give a rank-isolated four-edge coboundary.

#### Proof

The first departure of a proposed next diamond may itself be special.
After that departure has been reinserted as the first chain increment,
however, every later base rank again has one of the four signatures
\(S\setminus\{q_i\}\), with the \(q_i\)'s distinct. The endpoint collars
contain no special labels, so this remains true at all \(2Q\)
post-first-departure base ranks. Only \(q_i\) is available from \(S\) in
carrier \(i\).

Write \(D_r\) for the common nonspecial part of the base at the
post-first-departure rank under consideration.  For \(i\ne j\), equality
of two legal augmented bases at that rank,

\[
 (S\setminus\{q_i\})+p
 =(S\setminus\{q_j\})+q,
\tag{6.3}
\]

is possible only when \(p=q_i\) and \(q=q_j\), producing the common
vertex \(D_r\cup S\). Adding an outside label leaves two different
three-subsets of \(S\), so it cannot produce equality.

A nonzero diamond edge has two distinct arrivals.  Since only one of
them can be \(q_i\), at least one is outside \(S\).  Thus the edge may
use the one common vertex \(D_r\cup S\), but its other endpoint has the
unique special trace \(S\setminus\{q_i\}\) and cannot occur on another
carrier. Hence that endpoint is unbalanced, and the four-edge graph is
not Eulerian at any post-first-departure rank.

A rank-isolated identity could fail to cancel at only one rank, whereas
there are \(2Q\ge2\) such ranks. Therefore immediate four-edge repetition
cannot be rank-isolated.
\(\square\)

This obstruction is not caused by absent carrier coordinates: every
carrier in (4.3) contains all four special labels. It rules out only
immediate repetition of the same four-edge arrival architecture.

The transport statement left open here is now proved in
`MATH_ATTACK_PSTUBE8_LATIN_TRANSPORT_AND_PROTECTED_STRIP_ABSORBER_20260725.md`.
If \(q_i\) is the unique old special label in carrier \(i\)'s residual and
\(P=\{p_1,p_2,p_3,p_4\}\) is a fresh four-set in the common residual
intersection, choose common lower departures \(d_1,d_2\) and use

\[
 (d_1,p_i),\qquad(d_2,q_i).
\]

The first transport owners have special signatures
\((S-\{q_i\})+p_i\) and are pairwise distinct.  The second states have a
common lower core plus the singleton \(p_i\), the transported allowed
adjacent-swap collar braid, and the other three labels of \(P\) in the
residual block.  Thus they are legal sources for the next Latin block.  The
transport is common to both signs and cancels from the signed incidence.
At central depth the common-residual loss at swap/ejection boundary
crossings is only \(O(M/Q)=o(H-Q)\), so the construction runs for
\(\Theta(M)\) updates.

An \(O(Q)\)-update flush is insufficient for coefficient-scale packing:
it reduces the number of useful \(O(1)\)-incidence directions per carrier
from \(\Theta(M)\) to \(O(M/Q)\). The \(O(1)\) transport requirement is
therefore essential.

## 7. Adversarial audit

* The \(W/4\) obstruction counts occurrence-disjoint pairs, not distinct
  owner labels. Reusing one label only increases duplicate excess.
* The exceptional whole-pair carriers in the explicit pairing involution
  are exponentially negligible relative to \(N_H\).
* The eight-template identity is a switch between two positive
  four-path configurations, not a formal signed word.
* The twelve-owner proof includes all three local states and all swap
  positions, including \(k_*=m,m-1,m-2\).
* Rank isolation includes the refined prefix rank \(m+Q+1\): the Latin
  identity cancels there rankwise, and the perturbed chains have already
  recoalesced.
* At the very first base rank of a proposed repeat, cross-carrier special
  departures can make two bases coincide and permit pairwise cancellation.
  Proposition 6.1 deliberately does not count that rank: after those
  departures are reinserted, each of the following \(2Q\) collar ranks has
  a carrier-unique noncommon endpoint, so at least two ranks remain
  non-Eulerian.
* The two-update Latin transport is now closed.  No claim is made here that
  the resulting length-\(M\) four-carrier tubes form a global owner
  near-factor.  That committed tube-packing theorem is the remaining global
  chronology/positivity gate.
