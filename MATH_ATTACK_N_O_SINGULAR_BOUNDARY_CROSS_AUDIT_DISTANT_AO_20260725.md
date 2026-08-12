# Cross-audit of Lane O and a distant-factor AO theorem

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
long-running computation is used.

## 0. Verdict

The two highlighted results of
`MATH_ATTACK_O_SINGULAR_BOUNDARY_EXACT_GATES_20260725.md` have different
statuses relative to \(\mathrm{AO}_A\).

1. The prime-cycle theorem is correct with all its stated arithmetic
   restrictions. If \(n=2m+1\) is prime and \(m\ge3\) is odd, no exact
   wreath factor is invariant under a fixed coordinate \(n\)-cycle.
   This is only a full-equivariance obstruction. It gives no quantitative
   distance from equivariance and no AO lower bound.
2. The \(\Omega(W\sqrt m)\) MSW-basin bound is correct for the declared
   **irreversible permanent-prefix cost**. It uses only the depth-one hole
   layer. The factor \(\sqrt m\) comes from charging each owner which ever
   leaves its old prefix at every subsequent depth. An AO owner can leave at
   depth one and rejoin at depth two, so the AO consequence is only the
   already audited linear bound \(T_1=\Omega(W)\).
3. Exact endpoint point-regularity, zero-margin cycles, overlap components,
   cyclic endpoint span caps, and the prime packet obstruction require a
   second exact endpoint factor. They do not automatically hold for an
   ownerwise AO history on one factor. Imposing them on AO would be the
   labelled-synchronization overreach excluded by the frozen brief.
4. The shadow-quota matroid *does* transfer to AO. This gives a new exact
   AO-valid one-rank obstruction combining Hall-base distance with the
   actual point-margin displacement produced by sibling toggles.
5. There is a genuine distant-factor theorem. The marked-gap obstruction
   holds around every coordinate relabeling of MSW, and any \(o(W)\)-AO
   candidate must have row distance at least
   \((1/8-o(1))\operatorname{Cat}_m\) from **every** relabelled MSW factor.
   Conversely, relabelled MSW factors themselves form a factorially large
   family of pairwise distant bad factors. In particular, there is an exact
   factor at maximal row distance \(B\) from the canonical MSW factor which
   still has \(T_1\ge(1/16-o(1))W\).

The last statement is a counterexample to any claim that merely leaving one
fixed canonical MSW row basin removes the obstruction. It does not refute
existential \(\mathrm{AO}_A\): all these distant bad factors lie in one
\(S_n\)-isomorphism class. Factors distant from the entire MSW orbit remain
unresolved.

## 1. The two cost models must not be identified

Put

\[
 n=2m+1,\qquad
 W=\binom nm,\qquad
 B=\frac Wn=\operatorname{Cat}_m,
 \qquad K=\lceil A\sqrt m\rceil.
\]

At depth \(q\), put

\[
 r_q=m-q,\qquad
 N_q=\binom n{r_q},\qquad
 W=c_qN_q+\rho_q,
 \quad 0\le\rho_q<N_q.
\tag{1.1}
\]

As in Lane O, for all sufficiently large \(m\) we use the fixed bound

\[
 1\le c_q\le
 C_A:=\left\lceil e^{2(A+1)(A+2)}\right\rceil
 \qquad(q\le K).
\tag{1.1a}
\]

### 1.1 Permanent-prefix cost

Lane O compares an old factor \(F\) with an endpoint path system and gives
each owner one stopping depth \(a(X)\). Once \(a(X)<q\), that owner belongs
to the permanent release set at every later depth:

\[
 \mathcal R_q=\{X:a(X)<q\},\qquad
 R_q=|\mathcal R_q|,
\]

\[
 \mathcal C_{\rm perm}
 =\sum_{q=1}^K\frac{R_q}{c_q}
 =\sum_XH_{a(X)+1},
 \qquad
 H_d=\sum_{q=d}^K\frac1{c_q}.
\tag{1.2}
\]

Thus one first-depth release costs \(H_1=\Theta_A(\sqrt m)\), even if the
new and old paths later meet again.

### 1.2 AO toggle cost

For one exact factor, a one-pass adjacent-deletion history has a stage
indicator \(\varepsilon_q(X)\). Its cost is

\[
 \mathcal C_{\rm AO}
 =\sum_{q=1}^K\frac{T_q}{c_q},
 \qquad
 T_q=\#\{X:\varepsilon_q(X)=1\}.
\tag{1.3}
\]

An owner is charged only at the depths at which its selected cell differs
from its canonical anchor. A no-toggle decision resets the carry and may
make the path canonical again. Therefore \(R_q\) is monotone in \(q\),
whereas the sets counted by \(T_q\) need not be.

This distinction is decisive in Sections 3 and 4 below.

## 2. Audit of the prime-cycle obstruction

Assume throughout this section that

\[
 n=2m+1\text{ is prime},\qquad m\ge3\text{ is odd},
\tag{2.1}
\]

equivalently \(n\equiv3\pmod4\) and \(n\ge7\). Fix an \(n\)-cycle
\(\tau\) on the coordinates. A cyclic row is understood modulo phase
rotation; reversing it gives the same unpointed packet and the other
orientation.

### Theorem 2.1 -- Lane O's full-cycle obstruction is correct

No exact oriented or unpointed wreath factor is setwise invariant under
\(\tau\).

#### Proof audit

For a cyclic order \(C=(z_0,\ldots,z_{n-1})\), let

\[
 X_i=\{z_i,\ldots,z_{i+m-1}\}.
\]

Among the \(n\) packet members, two meet in \(m-1\) points exactly when
their phase distance is one. Hence the packet recovers the phase cycle,
and the leaving labels \(X_i\setminus X_{i+1}=\{z_i\}\) recover \(C\)
up to rotation and reversal.

If a packet is fixed by \(\tau\), its induced action on the recovered
phase cycle is nontrivial: otherwise every proper nonempty \(X_i\) would
be fixed by the prime cycle. An order-\(n\) element of the dihedral group
is a nonzero rotation. Therefore, for some
\(a\in\mathbb Z_n^*\), the order is

\[
 z_i=\tau^{ai}(z_0).
\tag{2.2}
\]

The choices \(a\) and \(-a\), and only those, give the two traversals of
one unpointed packet. Thus there are exactly

\[
 \frac{n-1}{2}=m
\tag{2.3}
\]

fixed unpointed packets. There are two fixed orientations over each, but
an exact factor can select at most one because both orientations own the
same \(n\) middle sets.

If an exact factor were invariant, its \(B\) rows would split into fixed
rows and free \(n\)-orbits:

\[
 B=f+nt,\qquad0\le f\le m.
\tag{2.4}
\]

Modulo \(n\),

\[
 \binom{n-1}{m}\equiv(-1)^m,
 \qquad
 (m+1)^{-1}\equiv2,
\]

so

\[
 B=\frac1{m+1}\binom{n-1}{m}
 \equiv2(-1)^m
 \equiv n-2=2m-1\pmod n.
\tag{2.5}
\]

The least nonnegative residue \(2m-1\) is larger than \(m\), contradicting
(2.4). \(\square\)

The restrictions in (2.1) are essential to the theorem as proved. At
\(m=1\) the fixed packet exists. When \(m\) is even the residue is two,
and for composite \(n\) nonfixed row orbits need not have size \(n\).

### 2.1 The congruence has no quantitative stability by itself

Let the full row universe be decomposed into \(\tau\)-orbits. If a
\(B\)-row subset \(A\) has occupancy \(x_O\) in a nonfixed orbit \(O\),
then exactly

\[
 \boxed{
 \frac1n\sum_{i=0}^{n-1}d_{\rm row}(A,\tau^iA)
 =\frac1n\sum_Ox_O(n-x_O).}
\tag{2.6}
\]

Indeed, in one orbit the average intersection of a fixed \(x_O\)-subset
with a random cyclic translate is \(x_O^2/n\).

The Catalan residue is compatible with only one partial orbit: take
\(n-2\) consecutive members of a nonfixed orbit and add full orbits until
the total size is \(B\). Then

\[
 d_{\rm row}(A,\tau A)=1,
 \qquad
 \frac1n\sum_i d_{\mathrm{row}}(A,\tau^iA)
 =\frac{2(n-2)}n<2.
\tag{2.7}
\]

This relaxed row set need not be an exact factor. Even adding the exact-
factor fact that two distinct factors cannot differ in only one unpointed
row does not change the scale. Indeed, if two exact factors shared all but
one row, their common rows would cover the same owners and the two remaining
rows would have the same middle packet; packet rigidity would make them the
same unpointed row. For all sufficiently large relevant \(m\),
take \(n-1\) members in each of two nonfixed row orbits and add full
orbits. Its size has residue

\[
 2(n-1)\equiv n-2\pmod n,
\]

and

\[
 d_{\mathrm{row}}(A,\tau^iA)=2
 \qquad(1\le i<n).
\tag{2.8}
\]

For an actual exact factor \(F\), Theorem 2.1 applies to every nontrivial
power \(\tau^i\), while the preceding one-row argument excludes distance
one. Hence the exact conclusion currently available is only

\[
 d_{\rm row}(F,\tau^iF)\ge2\quad(1\le i<n),
 \qquad
 \frac1n\sum_{i=0}^{n-1}d_{\rm row}(F,\tau^iF)
 \ge\frac{2(n-1)}n.
\tag{2.9}
\]

Thus row-orbit sizes, the fixed-row cap, the Catalan congruence, and the
absence of a one-row exact trade are jointly compatible with uniformly
\(O(1)\) power distance. A quantitative \(\Omega(B)\) consequence would
require a new exact-owner-partition trade-rigidity theorem. The prime-cycle
arithmetic alone cannot supply it.

In particular, Theorem 2.1 gives no obstruction to a non-equivariant exact
factor, a non-equivariant AO history, or even an approximately equivariant
candidate.

## 3. Audit of the \(\Omega(W\sqrt m)\) MSW-basin bound

Put

\[
 J_m=(2m-3)\operatorname{Cat}_{m-2},
 \qquad
 \rho_1=\frac{2W}{m+2}.
\tag{3.1}
\]

For an exact factor \(F'\) at row distance \(b\) from canonical MSW, the
audited marked-gap theorem gives

\[
 M_1(F')
 \ge D_b:=\bigl[J_m-(m-1)b-\rho_1\bigr]_+.
\tag{3.2}
\]

The distance may be taken on unpointed packets. Reversing one cyclic row
permutes its same \(n\) rank-\((m-1)\) interval anchors, so it leaves that
row's first-shadow histogram unchanged. Equivalently, common unpointed rows
may first be reoriented to agree with MSW without changing \(M_1\), after
which the oriented stability proof applies.

### Theorem 3.1 -- exact permanent cost

Every balanced permanent-prefix completion satisfies

\[
 \boxed{
 R_t\ge D_b\quad(1\le t\le K),
 \qquad
 \mathcal C_{\rm perm}\ge H_1D_b
 \ge\frac K{C_A}D_b.}
\tag{3.3}
\]

#### Proof

At depth one, \(c_1=1\). Every old first-shadow hole must receive a new
endpoint occurrence, and distinct holes require distinct released owners.
Thus \(R_1\ge M_1(F')\ge D_b\). Permanent release sets are nested, so
\(R_t\ge R_1\) for every later \(t\). Summing their weighted costs proves
(3.3). \(\square\)

The constants in Lane O are therefore correct:

\[
 \frac{J_m}{W}
 =\frac{m(m+1)}{4(2m-1)(2m+1)}\longrightarrow\frac1{16},
 \qquad
 \frac{\rho_1}{W}=\frac2{m+2},
\tag{3.4}
\]

and, uniformly for
\(b\le(1/8-\varepsilon)B\),

\[
 D_b\ge(\varepsilon/2+o(1))W.
\tag{3.5}
\]

Since \(K=(A+o_A(1))\sqrt m\), (3.3) yields

\[
 \mathcal C_{\rm perm}(F_m^{\rm MSW})
 \ge\left(\frac{A}{16C_A}+o_A(1)\right)W\sqrt m,
\tag{3.6}
\]

and throughout the stated edit basin,

\[
 \mathcal C_{\rm perm}(F')
 \ge\left(\frac{A\varepsilon}{2C_A}+o_A(1)\right)W\sqrt m.
\tag{3.7}
\]

There is no overlap or double-counting error in these inequalities: repeated
charging is exactly the definition of permanent exposure. But there is only
one defective layer, \(q=1\). The \(\sqrt m\) multiplier does **not** come
from singular defects at \(\Theta(\sqrt m)\) different depths.

### Corollary 3.2 -- the exact AO consequence is only linear

For an adaptive adjacent-deletion history,

\[
 \boxed{
 T_1(F')\ge D_b,
 \qquad
 \mathcal C_{\rm AO}\ge D_b.}
\tag{3.8}
\]

No factor \(H_1\) follows. Hence Lane O's basin theorem excludes the same
MSW row basin from \(o(W)\) AO cost, but at scale \(\Omega(W)\), not
\(\Omega(W\sqrt m)\).

## 4. Exact no-transfer lemma for permanent exposure

Let one owner's canonical deletion word be

\[
 a_1,a_2,\ldots,a_{K+1},
\]

and

\[
 L_q=X\setminus\{a_1,\ldots,a_q\}.
\]

### Lemma 4.1 -- one legal AO toggle has permanent cost \(H_1\)

Toggle at stage one and make no toggle at every later stage. Then

\[
 P_1=L_2\cup\{a_1\}\ne L_1,
 \qquad
 P_q=L_q\quad(q\ge2).
\tag{4.1}
\]

Thus this owner has AO cost exactly one, but its largest common initial
prefix has stopping depth zero and its permanent-prefix cost is \(H_1\).

#### Proof

Initially the carried letter is \(\kappa_1=a_1\). A stage-one toggle keeps
it, so the alternate rank-\((m-1)\) endpoint is
\(L_2\cup\{a_1\}\). At stage two, a no-toggle decision resets the carry
to \(a_3\), giving
\(P_2=L_3\cup\{a_3\}=L_2\). Every later no-toggle similarly gives
\(P_q=L_q\). The two cost assertions follow from (1.2)--(1.3).
\(\square\)

The same construction can be performed independently on any specified
set of owners, giving AO cost \(|Z|\) and permanent exposure
\(|Z|H_1\). It is a literal allowed interval block \([1,2]\) in every
touched deletion word.

This lemma is a model-separation counterexample, not a balanced AO
construction. It proves that permanent-prefix lower bounds cannot be
transferred to AO by an ownerwise cost comparison. A transfer would require
a new theorem showing that global balancedness forbids almost all such
resets; no such theorem is present in Lane O.

### Lemma 4.2 -- the exact worst-case comparison loses a full window

For an arbitrary one-pass history, let \(s(X)\) be an owner's first toggle,
with no contribution when it never toggles, and define its permanent
envelope by charging every depth from \(s(X)\) onward. Then

\[
 \boxed{
 \mathcal C_{\rm AO}
 \le \mathcal C_{\rm env}
 \le C_AK\,\mathcal C_{\rm AO}.}
\tag{4.2}
\]

#### Proof

Every toggled depth lies at or after the first toggle, so the permanent
envelope contains every term of the AO sum. Conversely, a touched owner has
envelope cost at most \(K\), while its AO cost is at least
\(1/C_A\). Sum over touched owners. \(\square\)

Lemma 4.1 realizes the \(\Theta_A(\sqrt m)\) loss in (4.2) ownerwise.
Therefore the \(\Omega(W\sqrt m)\) permanent basin theorem can yield at
most an \(\Omega(W)\) AO statement through a model comparison, exactly as
the direct hole bound does.

## 5. Which singular-boundary constraints actually survive in AO

Fix one exact factor \(F\), one stage \(q\), and an arbitrary legal earlier
AO history. Write

\[
 r=m-q,\qquad N=\binom nr,\qquad W=cN+\rho,
\]

and let \(\mu\) be the canonical anchor histogram at this rank. A balanced
AO orientation has load

\[
 b=c\mathbf1+\mathbf1_H,
 \qquad |H|=\rho.
\tag{5.1}
\]

Let \(\mathsf M_q\) be Lane O's rank-\(\rho\) shadow-quota matroid, and
write \(\mathfrak B(\mathsf M_q)\) for its bases. Finally put

\[
 d=Br-c\binom{n-1}{r-1}=\frac{r\rho}{n}.
\tag{5.2}
\]

### Theorem 5.1 -- AO Hall-base and point-displacement obstruction

Every balanced supported AO orientation satisfies

\[
 \boxed{H\in\mathfrak B(\mathsf M_q),}
\tag{5.3}
\]

\[
 \boxed{
 \frac12\|b-\mu\|_1\le T_q,
 \qquad
 \frac12\|\deg H-d\mathbf1\|_1\le T_q.}
\tag{5.4}
\]

Consequently, if

\[
 \Phi_q(F)=
 \min_{H\in\mathfrak B(\mathsf M_q)}
 \max\left\{
 \frac12\|\mu-(c\mathbf1+\mathbf1_H)\|_1,
 \frac12\|\deg H-d\mathbf1\|_1
 \right\},
\tag{5.5}
\]

then every fixed-window AO history obeys

\[
 \boxed{
 T_q\ge\Phi_q(F),
 \qquad
 \mathcal C_{\rm AO}
 \ge\sum_{q=1}^K\frac{\Phi_q(F)}{c_q}.}
\tag{5.6}
\]

#### Proof

Each owner is assigned to a contained rank-\(r\) endpoint. Thus, for every
cell family \(\mathcal U\), the owners assigned into \(\mathcal U\) have
distinct middle roots in its upper shadow:

\[
 c|\mathcal U|+|H\cap\mathcal U|
 =b(\mathcal U)
 \le|\Gamma(\mathcal U)|.
\]

These are exactly the independence inequalities of the shadow-quota
matroid. Since \(|H|=\rho\), \(H\) is a base, proving (5.3).

Every toggled owner changes one canonical anchor to one alternate endpoint,
so

\[
 b-\mu
 =\sum_{X:\varepsilon_q(X)=1}
 \left(\mathbf e_{P_q(X)}-\mathbf e_{L_q(X)}\right).
\tag{5.7}
\]

The two endpoint cells have the same cardinality and differ by one
coordinate. Taking histogram \(\ell^1\)-norm gives the first inequality in
(5.4). Taking point degrees in (5.7), and using

\[
 \deg\mu=Br\mathbf1,
 \qquad
 \deg b=c\binom{n-1}{r-1}\mathbf1+\deg H,
\]

gives

\[
 \deg H-d\mathbf1
 =\sum_{X:\varepsilon_q(X)=1}
 \left(\mathbf e_{\kappa_q(X)}-\mathbf e_{a_{q+1}(X)}\right).
\tag{5.8}
\]

Its \(\ell^1\)-norm is at most \(2T_q\). Minimize over the necessary base
family and sum over depths. \(\square\)

The first term in (5.5) contains the exact two-sided floor baseline

\[
 \max\left\{
 \sum_S(c-\mu(S))_+,
 \sum_S(\mu(S)-c-1)_+
 \right\}.
\tag{5.9}
\]

The second term is the AO-valid replacement for Lane O's exact endpoint
point-regularity. It is small only if the chosen Hall base is nearly regular;
exact regularity cannot be assumed.

### Scope table

The following Lane O constraints transfer to AO without any extra theorem:

* the mobile containment cuts and the shadow-quota base condition (5.3);
* the immutable-anchor floor/ceiling transport bound (5.9);
* the approximate point-margin identity (5.8);
* the ownerwise carry and interval-composition laws.

The following do **not** transfer to a general AO history:

* exact point-regularity of \(H\);
* exact zero point margins and deleted-letter margins between two factors;
* overlap-component alternating-cycle localization;
* cyclic endpoint row-span and high-slot caps for a second exact factor;
* the prime-cycle packetization obstruction;
* permanent violation-token widths and the \(H_1\) amplification.

An AO family \(P_q(X)\) consists of legal ownerwise sibling choices, but
those choices need not regroup into any exact cyclic endpoint factor. A new
packetization theorem would be required before the second list could be
used.

Lane O's near-regular containment-base theorem does not make (5.6)
subcritical for every old factor: it supplies a Hall base with small point
error, but gives no bound on that base's histogram distance from the
prescribed \(\mu_q^F\). Conversely, a base close to \(\mu_q^F\) need not
have small point error or admit the actual sibling support. This is the
remaining one-rank coupling.

### 5.1 Audit of the remaining Lane O packages

The other theorem packages used in Lane O were checked with their stated
scopes; no algebraic correction was found.

1. **Shadow-quota matroid.** The mandatory clone set is independent by the
   normalized upper-shadow Hall inequality. The full transversal matroid has
   rank \(W\) by the dual normalized lower-shadow inequality, so contraction
   has rank exactly \(W-c_qN_q=\rho_q\). This verifies the matroid and
   laminar-intersection claims.
2. **Near-regular leave.** Pipage rounding supplies the stated pairwise
   covariance bound; one-point exchanges regularize the base in at most half
   its degree \(\ell^1\)-error. Intersecting the old and regularized bases
   matches exactly \(W-L_q\) owners. The regularized family need not remain
   a shadow-matroid base, which is why the theorem correctly leaves \(L_q\)
   unmatched owners rather than claiming a zero-leave endpoint.
3. **Coprime cyclic quotient.** Free coordinate-cycle orbits and integral
   quotient flow do give a nested balanced point-regular Boolean resolution.
   Its lifted root orbits are not wreath packets, so it supplies no literal
   factor and no AO support theorem.
4. **Regular support and zero margins.** The positive support identity,
   half-\(\ell^1\) formulas, and alternating-cycle decompositions are correct
   for two exact factors. Their exact point cancellation is precisely what
   fails to be automatic in AO and is replaced by (5.8).
5. **Violation widths and cyclic high-slot cuts.** The token-chain proofs
   are correct for monotone permanent releases, and convex concentration of
   row residence gives the stated cyclic span cap for a literal endpoint
   factor. Neither proof is an AO theorem because rejoining destroys
   monotone exposure and ownerwise carried sets need not be endpoint row
   intervals.

## 6. Every low-cost AO factor is far from the whole MSW orbit

Let \(F_0=F_m^{\rm MSW}\), and for \(\sigma\in S_n\) let

\[
 F_\sigma=\sigma F_0.
\]

All row distances in this section are unpointed. Put

\[
 b_\sigma(F)=d_{\rm row}(F,F_\sigma)
 =\frac12|F\triangle F_\sigma|.
\tag{6.1}
\]

### Theorem 6.1 -- all-conjugate MSW exclusion

For every exact factor \(F\), every balanced stage-one AO orientation, and
every \(\sigma\in S_n\),

\[
 \boxed{
 T_1(F)
 \ge
 \bigl[J_m-(m-1)b_\sigma(F)-\rho_1\bigr]_+.}
\tag{6.2}
\]

Equivalently,

\[
 \boxed{
 \min_{\sigma\in S_n}b_\sigma(F)
 \ge
 \left\lceil
 \frac{[J_m-\rho_1-T_1(F)]_+}{m-1}
 \right\rceil.}
\tag{6.3}
\]

Hence every sequence of factors admitting \(o(W)\)-cost AO histories must
satisfy

\[
 \boxed{
 d_{\rm row}\bigl(F,S_nF_0\bigr)
 \ge(1/8-o(1))B.}
\tag{6.4}
\]

#### Proof

Coordinate relabeling carries every marked-gap certificate, its common
first-shadow target, and its row certificate degree to the corresponding
objects for \(F_\sigma\). Therefore the audited row-stability theorem
centered at \(F_\sigma\) gives

\[
 M_1(F)\ge
 [J_m-(m-1)b_\sigma(F)-\rho_1]_+.
\]

Every first-shadow hole requires a distinct stage-one toggle, so
\(T_1(F)\ge M_1(F)\), proving (6.2). Rearrangement gives (6.3). If the
total AO cost is \(o(W)\), then \(T_1=o(W)\). Divide (6.3) by
\(B=W/(2m+1)\) and use (3.4) to obtain (6.4). \(\square\)

This is a genuine structural theorem about every possible distant AO
candidate. It closes the union of all relabelled MSW basins, not merely the
basin of one written representative.

## 7. Factorially many distant bad exact factors

Let \(\mathscr W_m\) be the universe of unpointed wreath packets on
\([n]\). Packet rigidity gives

\[
 |\mathscr W_m|=\frac{n!}{2n}=\frac{(2m)!}{2}=: \mathcal N_m.
\tag{7.1}
\]

The \(S_n\)-action on \(\mathscr W_m\) is transitive.

### Theorem 7.1 -- relabelled-MSW distance averaging

For every fixed exact factor \(G\) and uniformly random
\(\sigma\in S_n\),

\[
 \boxed{
 \mathbb E|G\cap F_\sigma|
 =\frac{B^2}{\mathcal N_m}.}
\tag{7.2}
\]

More generally, for fixed exact factors \(G_1,\ldots,G_L\) and
\(0<\delta<1\),

\[
 \boxed{
 \mathbb P\left(
 \exists i:\ d_{\rm row}(G_i,F_\sigma)<(1-\delta)B
 \right)
 \le
 \frac{2L}{\delta(m+1)(m!)^2}.}
\tag{7.3}
\]

#### Proof

For fixed packets \(P,Q\), transitivity gives

\[
 \mathbb P(\sigma Q=P)=\frac1{\mathcal N_m}.
\]

Summing over \(P\in G\) and \(Q\in F_0\) proves (7.2). If
\(d_{\rm row}(G,F_\sigma)<(1-\delta)B\), then
\(|G\cap F_\sigma|>\delta B\). Markov's inequality and (7.2) give

\[
 \mathbb P(\text{this event})
 \le\frac{B}{\delta\mathcal N_m}.
\]

Finally,

\[
 \frac{B}{\mathcal N_m}
 =\frac{2}{m!(m+1)!}
 =\frac{2}{(m+1)(m!)^2},
\tag{7.4}
\]

and a union bound proves (7.3). \(\square\)

### Corollary 7.2 -- a maximally distant obstructed factor

For every \(m\ge2\), there is a coordinate relabeling \(\sigma\) such
that

\[
 F_0\cap F_\sigma=\varnothing,
 \qquad
 d_{\rm row}(F_0,F_\sigma)=B.
\tag{7.5}
\]

Nevertheless every balanced stage-one orientation of \(F_\sigma\) obeys

\[
 \boxed{
 T_1(F_\sigma)
 \ge
 \left[J_m-\rho_1\right]_+
 =(1/16-o(1))W.}
\tag{7.6}
\]

#### Proof

For \(G=F_0\), the expectation in (7.2) is

\[
 \frac{B^2}{\mathcal N_m}
 =\frac{2B}{m!(m+1)!}<1
 \qquad(m\ge2).
\]

The inequality holds at \(m=2\), where the value is \(1/3\), and its
ratio at successive \(m\) is

\[
 \frac{2(2m+1)}{(m+1)(m+2)^2}<1.
\]

Since the intersection size is a nonnegative integer, some relabeling has
intersection zero. Coordinate relabeling preserves the first-shadow
histogram up to relabeling its cells, hence preserves its hole count.
Apply the audited marked-gap theorem and the universal inequality
\(T_1\ge M_1\). \(\square\)

Thus bad exact factors occur at maximal labelled row distance from the
canonical MSW representative.

### Corollary 7.3 -- factorial packing of bad factors

For every fixed \(0<\delta<1\), there are at least

\[
 \boxed{
 \left\lfloor
 \frac{\delta(m+1)(m!)^2}{4}
 \right\rfloor}
\tag{7.7}
\]

relabelled MSW exact factors which are pairwise at row distance at least
\((1-\delta)B\). Every one has the lower bound (7.6).

#### Proof

Choose factors greedily. After \(L\) have been selected, (7.3) shows that
a new relabeling at the required distance exists whenever

\[
 \frac{2L}{\delta(m+1)(m!)^2}<1.
\]

Stopping at half this threshold gives (7.7). \(\square\)

For example, with \(\delta=1/2\), there are at least

\[
 \left\lfloor\frac{(m+1)(m!)^2}{8}\right\rfloor
\]

pairwise \(B/2\)-distant bad centers. Their
\((1/8-\varepsilon)B\)-row basins are pairwise disjoint, and every factor
in each such basin has

\[
 T_1\ge(\varepsilon/2-o(1))W.
\]

This is a quantitatively distant-factor obstruction in labelled row space.
Its exact limitation is equally important: the centers form one
\(S_n\)-orbit. It gives no information about a factor satisfying (6.4).

## 8. Precise proved and open boundary

### Proved by the cross-audit

1. Lane O's prime-cycle packet rigidity, fixed-packet count, and Catalan
   congruence are correct under (2.1).
2. Their implication is qualitative only. Equations (2.6)--(2.8) prove
   that the audited orbit arithmetic is compatible with \(O(1)\) row
   asymmetry; exact trade rigidity is the missing quantitative input.
3. Lane O's \(\Omega(W\sqrt m)\) constants are correct for permanent
   prefix exposure. The factor \(\sqrt m\) is irreversible residence of
   one depth-one defect, not an AO cost.
4. The exact AO consequence in the MSW basin is (3.8), of order \(W\).
5. The shadow-quota matroid and the approximate point-displacement bound
   combine into the AO-valid obstruction (5.5)--(5.6).
6. Every \(o(W)\)-AO factor must be \((1/8-o(1))B\)-far from the full
   relabelled MSW orbit.
7. There are factorially many pairwise distant exact bad factors, including
   one at maximal distance \(B\) from the canonical MSW representative.

### Not proved

1. A positive AO construction for a factor satisfying the all-orbit
   distance condition (6.4).
2. A universal lower bound

   \[
   \sum_{q\le K}\frac{\Phi_q(F)}{c_q}=\Omega(W)
   \]

   for every exact factor. Such a theorem would obstruct distant AO
   candidates, but neither the prime congruence nor the existing singular
   constraints imply it.
3. A trade-rigidity theorem ruling out an exact factor with only
   \(O(1)\) row boundary under a prime coordinate cycle.
4. A packetization theorem turning an AO ownerwise endpoint system into a
   second exact cyclic factor. Without it, exact point regularity,
   zero-margin components, and cyclic high-slot caps remain unavailable.
5. An existential counterexample to \(\mathrm{AO}_A\). The distant bad
   factors in Section 7 are all MSW relabelings, so a factor outside that
   entire isomorphism orbit may still work.

No constant-one contiguous-OR conclusion follows. The exact remaining AO
lane is now: either prove a critical lower bound for the AO-valid quantity
\(\Phi_q\) on every factor outside the full MSW orbit, or construct one
such factor together with supported interval-composition orientations of
total cost \(o(W)\).
