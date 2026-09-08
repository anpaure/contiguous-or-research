# Nonproduct packet aggregation with literal MTF states

Date: 2026-07-25

## 0. Outcome

Throughout, \(k\ge2\).  Let

\[
W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]

This report develops the exact nonproduct packet formula

\[
\nu(k)
\le
W(k)+\sum_\alpha(t_\alpha-M_\alpha)
       +\sum_\alpha(b_\alpha-1)
\tag{0.1}
\]

in two directions.

### Positive result — proved

For even \(k=2m\), there is a growing depth \(H=H(m)\to\infty\) and an
explicit family of literal MTF packets covering every target in

\[
\mathcal B_H
=
\bigcup_{q=-H}^{H}\binom{[2m]}{m+q}
\tag{0.2}
\]

such that

\[
\boxed{
\sum_\alpha(t_\alpha-M_\alpha)=o(W),
\qquad
\sum_\alpha(b_\alpha-1)=o(W).}
\tag{0.3}
\]

The packets arise from a target-disjoint matching of cyclic strips.  Every
principal packet has

\[
t_\alpha=M_\alpha=2\ell,
\qquad
b_\alpha=2H+2,
\tag{0.4}
\]

and all unmatched band targets are handled by one exact two-block-root
repair packet.  The resulting literal word has length

\[
W+o(W)
\tag{0.5}
\]

while covering

\[
|\mathcal B_H|=(2H+1+o(H))W
\tag{0.6}
\]

targets.  Thus it is asymptotically optimal for this growing band.

For any one fixed finite-block product-SCD partition, a common coordinate
relabeling makes all but \(o(p)\) principal packets—equivalently, a
\(1-o(1)\) fraction—
**parent-rainbow**: the \(2\ell\) middle targets of each such packet lie in
\(2\ell\) distinct product parents.  The construction therefore genuinely
crosses the fixed-product cells obstructed by the fixed-atomic-count no-go.

There is also a deeper overlapping-cover version, reaching every depth

\[
J=o(\sqrt{\log m})
\tag{0.7}
\]

central ranks in the audited economical-cover range.  An exact ownership
map converts the overlapping cover into target packets, and a general
two-block-root embedding converts each literal strip word into an MTF walk.
Its aggregate state and root surpluses are again \(o(W)\).

### New obstruction — proved

For arbitrary independently serviced literal packets covering the whole
Boolean lattice, let \(n_\alpha\) be packet length and let \(M_\alpha\) be
its owned middle-target count.  Put

\[
\Gamma
=\sum_\alpha(n_\alpha-M_\alpha)
=\sum_\alpha n_\alpha-W.
\tag{0.8}
\]

For the reverse-block-initialized packet realization
\(n_\alpha=b_\alpha+t_\alpha-1\), exactly

\[
\Gamma
=\sum_\alpha(t_\alpha-M_\alpha)
 +\sum_\alpha(b_\alpha-1).
\tag{0.9}
\]

For every set \(I\) of \(B\) proper ranks, define

\[
D_I=\sum_{r\in I}\left(W-\binom{k}{r}\right).
\tag{0.10}
\]

Then the exact literal rank-chronology inequality is

\[
\boxed{
\sum_\alpha\sum_{j=1}^{n_\alpha}(B-j)_+
\le B\Gamma+D_I.}
\tag{0.11}
\]

It implies a Gaussian **middle-packet mass theorem**, not merely existence
of one long word.  If \(\Gamma=o(W)\), then for every fixed
\(0<\eta<1\), at least

\[
(1-\eta-o(1))W
\tag{0.12}
\]

middle targets lie in packets containing more than

\[
(\sqrt{3\eta}+o(1))\sqrt{k}
\tag{0.13}
\]

owned middle targets.  In particular, at least \((3/4-o(1))W\) middle
targets lie in packets with more than

\[
\left(\frac{\sqrt3}{2}+o(1)\right)\sqrt{k}
\tag{0.14}
\]

middle targets.

Consequently the positive polylogarithmic strip packets cannot be completed
to the full cube by adding targets independently while keeping those
principal packets separate and retaining their middle ownership: every such
completion has

\[
\Gamma\ge(1-o(1))W,
\tag{0.15}
\]

and therefore length at least \((2-o(1))W\).  A coefficient-one completion
must merge or reassign a leading middle mass into Gaussian-scale packets, or
must use intervals crossing packet seams—a genuine global braid.  Merging
the principal packets is explicitly outside (0.15).

No full-cube coefficient-one theorem is claimed.

---

## 1. Exact packet and overlapping-ownership aggregation

An ordered partition of \([k]\) is

\[
\Pi=(B_1,\ldots,B_b),
\tag{1.1}
\]

where the \(B_i\) are disjoint nonempty blocks with union \([k]\).  Its
prefix-union chain is

\[
\operatorname{Pref}(\Pi)
=\{B_1,B_1\cup B_2,\ldots,B_1\cup\cdots\cup B_b\}.
\tag{1.2}
\]

For a nonempty mask \(X\), the move-to-front update is

\[
M_X(\Pi)
=(X,B_1\setminus X,\ldots,B_b\setminus X),
\tag{1.3}
\]

after empty blocks are deleted.  This is exactly the last-occurrence state
change caused by appending \(X\) to a Boolean word.  The suffix ORs ending
at that position are exactly the prefix unions of the new state.

### Theorem 1.1 — disjoint packet aggregation

Partition all nonempty Boolean targets into packets
\(\mathcal P_\alpha\).  Suppose packet \(\alpha\) has a genuine MTF walk

\[
\Pi_{\alpha,1},\ldots,\Pi_{\alpha,t_\alpha}
\tag{1.4}
\]

whose prefix chains cover \(\mathcal P_\alpha\).  Let \(b_\alpha\) be the
number of blocks in the first state, and let \(M_\alpha\) be the number of
owned targets in one fixed middle layer of size \(W(k)\).  Then

\[
t_\alpha\ge M_\alpha
\tag{1.5}
\]

and

\[
\boxed{
\nu(k)
\le W(k)
 +\sum_\alpha(t_\alpha-M_\alpha)
 +\sum_\alpha(b_\alpha-1).}
\tag{1.6}
\]

#### Proof

If

\[
\Pi_{\alpha,1}=(B_1,\ldots,B_{b_\alpha}),
\]

write the blocks in reverse order.  This initializes the exact state in
\(b_\alpha\) letters.  Append one update mask for each of the remaining
\(t_\alpha-1\) states.  The packet word therefore has length

\[
b_\alpha+t_\alpha-1.
\tag{1.7}
\]

A prefix chain contains at most one target from the middle antichain, giving
(1.5).  Concatenate the packet words.  Since

\[
\sum_\alpha M_\alpha=W(k),
\tag{1.8}
\]

summing

\[
b_\alpha+t_\alpha-1
=M_\alpha+(t_\alpha-M_\alpha)+(b_\alpha-1)
\]

proves (1.6).  Every witness stays in one literal packet segment. \(\square\)

### Theorem 1.2 — overlapping packets with exact ownership

The target families exposed by different walks may overlap.  Suppose
\(\mathcal F_\alpha\) cover all nonempty targets, and choose an ownership map

\[
\rho:2^{[k]}\setminus\{\varnothing\}\longrightarrow\{\alpha\}
\tag{1.9}
\]

such that \(T\in\mathcal F_{\rho(T)}\).  Define

\[
\mathcal P_\alpha=\rho^{-1}(\alpha).
\tag{1.10}
\]

If walk \(\alpha\) exposes \(\mathcal F_\alpha\), then it exposes its owned
packet \(\mathcal P_\alpha\).  With \(M_\alpha\) counting only the owned
middle targets, equations (1.5)--(1.8) remain exact.  Extra exposures are
harmless.

The same two theorems apply to a partial target family containing a complete
middle layer, with the ownership map in (1.9) defined only on that partial
family.  They then bound the minimum word covering that family, not
\(\nu(k)\) for the full lattice.

### Lemma 1.3 — embedding any literal packet word into an MTF packet

Let

\[
X_0,X_1,\ldots,X_{P-1}
\tag{1.11}
\]

be a literal packet word, with \(X_0\) nonempty and proper.  Put

\[
\Pi_0=(X_0,X_0^c),
\qquad
\Pi_j=M_{X_j}(\Pi_{j-1})\quad(1\le j<P).
\tag{1.12}
\]

Then every contiguous OR represented by (1.11) is a prefix union in the
corresponding state.  The word

\[
X_0^c,X_0,X_1,\ldots,X_{P-1}
\tag{1.13}
\]

therefore realizes the packet as an MTF walk with

\[
\boxed{t=P,\qquad b=2,\qquad\text{length}=P+1.}
\tag{1.14}
\]

#### Proof

After reading \(X_j\), the coordinates whose last occurrence is at least
the time of \(X_i\) are exactly

\[
\bigcup_{r=i}^{j}X_r.
\]

Coordinates are grouped in decreasing order of last occurrence, so this
union is a prefix union of \(\Pi_j\).  Equation (1.13) reverse-initializes
\((X_0,X_0^c)\), proving the claim. \(\square\)

---

## 2. The proved full-strip matching input

For this section let

\[
k=2m,\qquad W=\binom{2m}{m},
\qquad N_q=\binom{2m}{m-q}.
\tag{2.1}
\]

Choose disjoint cores \(C,D\subset[2m]\), each of size \(m-\ell\), and
cyclically order the remaining \(2\ell\) coordinates.  Write

\[
I(t,a)=\{z_t,z_{t+1},\ldots,z_{t+a-1}\}
\tag{2.2}
\]

with indices modulo \(s=2\ell\).  The full radius-\(H\) strip is

\[
\mathcal E(C,D,\gamma)
=
\left\{
C\cup I(t,\ell+d):
-H\le d\le H, t\in\mathbb Z_s
\right\}.
\tag{2.3}
\]

It has exactly \(s\) targets in every one of the \(2H+1\) band ranks.

### Imported proved theorem 2.1 — economical target-disjoint strip matching

Put

\[
L=\log m,\qquad \lambda=\log\log m,
\qquad
\omega=(L/\lambda)^{1/3},
\tag{2.4}
\]

and choose

\[
H=\left\lfloor
\sqrt{\frac{L}{64\omega\lambda}}
\right\rfloor,
\qquad
\ell=\lceil\omega H\rceil.
\tag{2.5}
\]

Then

\[
H\to\infty,\qquad \ell/H\to\infty,\qquad \ell=o(m).
\tag{2.6}
\]

There is a matching of \(p\) pairwise target-disjoint full strips for which
the uncovered counts are

\[
u_0=W-sp,
\qquad
u_q^-=u_q^+=N_q-sp,
\tag{2.7}
\]

and

\[
\boxed{
U:=u_0+\sum_{q=1}^{H}(u_q^-+u_q^+)
=O(WL^{-10})=o(W).}
\tag{2.8}
\]

This is the previously proved and independently audited growing-uniformity
matching theorem for the full-strip hypergraph.  Its exact input parameters
are: uniformity \(2\ell(2H+1)\), rank-\((m+d)\) degree

\[
D_d=\frac{(m+d)!(m-d)!}{2(m-\ell)!^2},
\tag{2.9}
\]

The maximum hypergraph codegree \(\Gamma_{\rm hyp}\) satisfies

\[
\frac{\Gamma_{\rm hyp}}{\max_dD_d}
\le\frac{2\ell}{m-H}.
\tag{2.10}
\]

For (2.4)--(2.5), the rank-uniformity, degree spread, and codegree satisfy
the full quantitative near-regular matching hypotheses, including

\[
e^{4\ell(2H+1)}\Gamma_{\rm hyp}\log(\max_dD_d)
=o(\max_dD_d),
\tag{2.11}
\]

and the required minimum-degree defect bound.  That theorem gives (2.8).
No fractional matching is being promoted to an integral packet family here:
theorem 2.1 already supplies the integral target-disjoint matching.

---

## 3. Explicit literal MTF states for one matched strip

Fix one strip from theorem 2.1.  Put

\[
T_i=C\cup I(i,\ell),
\qquad
L_i=C\cup I(i+H,\ell-H).
\tag{3.1}
\]

The middle targets are \(T_0,\ldots,T_{s-1}\).  Define

\[
R_0
=T_0^c\setminus\{z_{s-H},\ldots,z_{s-1}\},
\tag{3.2}
\]

and

\[
\Theta_0
=
(\{z_{s-1}\},\{z_{s-2}\},\ldots,\{z_{s-H}\},R_0).
\tag{3.3}
\]

Recursively set

\[
\Theta_{i+1}
=
(\{z_i\},\Theta_i\setminus\{z_{i+\ell}\}),
\tag{3.4}
\]

where the coordinate is deleted from every old block and empty blocks are
removed.  Finally define

\[
\boxed{
\Pi_i
=
\bigl(
L_i,
\{z_{i+H-1}\},\ldots,\{z_i\},
\Theta_i
\bigr),
\qquad 0\le i<s.}
\tag{3.5}
\]

The first \(H\) blocks of \(\Theta_i\) are

\[
\{z_{i-1}\},\ldots,\{z_{i-H}\}.
\tag{3.6}
\]

### Lemma 3.1 — exact MTF transition

For \(0\le i<s-1\),

\[
\boxed{\Pi_{i+1}=M_{L_{i+1}}(\Pi_i).}
\tag{3.7}
\]

#### Proof

The new lower core is

\[
L_{i+1}
=(L_i\setminus\{z_{i+H}\})\cup\{z_{i+\ell}\}.
\tag{3.8}
\]

It becomes the new first block.  The residue of the old first block is
\(\{z_{i+H}\}\), followed by the surviving future singleton blocks

\[
\{z_{i+H-1}\},\ldots,\{z_{i+1}\}.
\]

The old singleton \(\{z_i\}\) becomes the first past singleton.  The newly
inserted coordinate \(z_{i+\ell}\) is deleted from the old tail.  The oldest
past singleton remains a separate block inside the unrestricted tail
partition; no block merger is asserted.  Finally,
\(z_{i+\ell}\notin\{z_{i-1},\ldots,z_{i-H}\}\) because \(H<\ell\).
Thus prepending \(\{z_i\}\) inductively gives the first \(H\) markers in
(3.6).  This is exactly (3.4)--(3.6) with \(i\) replaced by \(i+1\).
\(\square\)

### Lemma 3.2 — exact exposed flag

The prefix unions of \(\Pi_i\) contain

\[
C\cup I(i+q,\ell-q),
\qquad 0\le q\le H,
\tag{3.9}
\]

at ranks \(m-q\), and

\[
C\cup I(i-q,\ell+q),
\qquad 1\le q\le H,
\tag{3.10}
\]

at ranks \(m+q\).  As \(i\) varies, these are exactly all \(s\) strip
targets in every band rank.

#### Proof

Starting from \(L_i\), the future singleton blocks fill the cyclic interval
back to \(T_i=C\cup I(i,\ell)\).  The first \(q\) past singleton blocks
then extend it to \(C\cup I(i-q,\ell+q)\).  Cyclic translation of \(i\)
enumerates each row. \(\square\)

### Literal packet word and exact local ledger

The root state \(\Pi_0\) has \(2H+2\) blocks.  Its reverse initialization,
followed by the update masks in (3.7), is

\[
\boxed{
R_0,
\{z_{s-H}\},\ldots,\{z_{s-1}\},
\{z_0\},\ldots,\{z_{H-1}\},
L_0,L_1,\ldots,L_{s-1}.}
\tag{3.11}
\]

This word has length

\[
s+2H+1.
\tag{3.12}
\]

Assign the entire full-strip target set to this packet.  It has exactly
\(s\) owned middle targets and \(s\) visited states, so

\[
\boxed{
t_\alpha=M_\alpha=s,
\qquad
b_\alpha-1=2H+1.}
\tag{3.13}
\]

There is no state surplus inside a principal packet.

---

## 4. Exact global band ledger

The matched strip target sets are disjoint.  List all \(U\) uncovered band
targets as

\[
X_1,\ldots,X_U.
\tag{4.1}
\]

If \(U>0\), put them in one repair packet.  Set

\[
\Sigma_1=(X_1,X_1^c),
\qquad
\Sigma_j=M_{X_j}(\Sigma_{j-1})\quad(2\le j\le U).
\tag{4.2}
\]

The literal repair word is

\[
X_1^c,X_1,X_2,\ldots,X_U.
\tag{4.3}
\]

Every \(X_j\) is the first block of \(\Sigma_j\).  Therefore

\[
t_{\rm rep}=U,
\qquad
M_{\rm rep}=u_0,
\qquad
b_{\rm rep}=2.
\tag{4.4}
\]

The principal packets plus the repair packet form a genuine partition of
\(\mathcal B_H\).  Their exact state surplus is

\[
\boxed{
\Delta
:=\sum_\alpha(t_\alpha-M_\alpha)
=U-u_0.}
\tag{4.5}
\]

Their exact root surplus is

\[
\boxed{
R
:=\sum_\alpha(b_\alpha-1)
=(2H+1)p+\mathbf1_{\{U>0\}}.}
\tag{4.6}
\]

Since \(p=(W-u_0)/(2\ell)\),

\[
R
\le
\frac{2H+1}{2\ell}W+1
=o(W),
\tag{4.7}
\]

while \(\Delta\le U=o(W)\).  The exact literal length is

\[
\begin{aligned}
W+\Delta+R
&=W+(U-u_0)+(2H+1)p+\mathbf1_{\{U>0\}}\\
&=W+o(W).
\end{aligned}
\tag{4.8}
\]

Uniformly for \(|q|\le H=o(\sqrt m)\),

\[
N_q=(1+o(1))W.
\tag{4.9}
\]

Hence

\[
|\mathcal B_H|=(2H+1+o(H))W.
\tag{4.10}
\]

The middle antichain gives a lower bound \(W\) on every word covering the
band, so (4.8) is asymptotically optimal.

---

## 5. The packets can cross many fixed product-SCD parents

Fix a partition of the coordinates into \(r\) blocks, where \(r\) is fixed,
and fix arbitrary SCDs in the block cubes.  Their chain products partition
the Boolean lattice into product parents.

Let \(A,B\) be two middle targets at Johnson distance \(d\).  Under a common
uniform coordinate permutation, conditional on the image of \(A\), the
deleted and added sets

\[
D=A\setminus B,
\qquad
E=B\setminus A
\tag{5.1}
\]

are independent uniform \(d\)-subsets of \(A\) and \(A^c\).  There are
\(\binom md^2\) possibilities.

If the two images lie in one \(r\)-chain product parent, the local downward
and upward displacement compositions determine the second point uniquely:
each factor chain contains at most one point at a prescribed local rank.
There are at most

\[
\binom{d+r-1}{r-1}^2
\tag{5.2}
\]

such pairs of weak compositions.  Therefore

\[
\boxed{
\Pr(A,B\text{ lie in one product parent})
\le
a_d:=
\frac{\binom{d+r-1}{r-1}^2}{\binom md^2}.}
\tag{5.3}
\]

Moreover,

\[
\frac{a_{d+1}}{a_d}
=\left(\frac{d+r}{m-d}\right)^2.
\tag{5.4}
\]

The middle row of one cyclic strip has \(s\) unordered pairs at every cyclic
gap \(d<\ell\), and \(\ell\) antipodal pairs at gap \(\ell\).  Since
\(\ell=o(m)\),

\[
\sum_{d=1}^{\ell}a_d=O_r(m^{-2}).
\tag{5.5}
\]

Thus the probability that one strip repeats a product parent in its middle
row is

\[
O_r(\ell/m^2).
\tag{5.6}
\]

By linearity of expectation, one common permutation makes the number of bad
principal packets at most

\[
O_r(p\ell/m^2)=o(p).
\tag{5.7}
\]

Every other principal packet has its \(2\ell\) middle targets in
\(2\ell\) pairwise distinct product parents.  The common permutation
preserves target disjointness, all MTF identities, and the exact ledgers.

This is for one prescribed product-SCD partition, or for any fixed finite
list by a union bound.  It is not simultaneous over all possible partitions.

---

## 6. A deeper overlapping packet cover

The target-disjoint matching construction is the cleanest literal packet
partition.  A deeper central band is available if overlapping exposed
families are allowed and targets are assigned by ownership.

### Imported proved theorem 6.1 — economical cyclic-strip cover

Let \(n=2m+1\), let

\[
W=\binom{2m+1}{m}=\binom{2m+1}{m+1},
\tag{6.1}
\]

and choose

\[
J\sim\frac{\sqrt{\log m}}{g},
\qquad
\ell\sim\frac{\sqrt{\log m}}{\sqrt g},
\tag{6.2}
\]

where \(g\to\infty\) and \(g=o(\sqrt{\log m})\).  There is a cover of the
ranks

\[
m-J,m-J+1,\ldots,m+J+1
\tag{6.3}
\]

by at most

\[
C
\le
\frac{W}{2\ell}(1+\varepsilon_m),
\qquad
\varepsilon_m=o(1),
\tag{6.4}
\]

cyclic strips.  Each strip has a literal word of length

\[
P=2\ell+2J+1.
\tag{6.5}
\]

One explicit strip word takes the \(2\ell\) cyclic intervals of the shortest
strip length and then repeats its first \(2J+1\) intervals.  Consecutive
unions expose every target in that strip.  The audited economical-cover
estimate gives

\[
\varepsilon_m
=O(J^2/m)+\exp(-\Omega(g^{3/2})).
\tag{6.6}
\]

### Exact ownership and MTF ledger

Assign every band target to one strip that covers it.  This makes the owned
target packets disjoint, although their exposed strip families may overlap.
Let \(M_\alpha\) count the owned targets in rank \(m+1\).  Then

\[
\sum_\alpha M_\alpha=W.
\tag{6.7}
\]

Apply Lemma 1.3 to every length-\(P\) strip word.  Thus

\[
t_\alpha=P,
\qquad
b_\alpha=2.
\tag{6.8}
\]

The exact aggregate state surplus is

\[
\begin{aligned}
\sum_\alpha(t_\alpha-M_\alpha)
&=CP-W\\
&\le
W\left[
(1+\varepsilon_m)
\left(1+\frac{2J+1}{2\ell}\right)-1
\right]
=o(W),
\end{aligned}
\tag{6.9}
\]

because \(J/\ell\sim g^{-1/2}\to0\).  The root surplus is

\[
\sum_\alpha(b_\alpha-1)=C=O(W/\ell)=o(W).
\tag{6.10}
\]

Consequently this deeper overlapping system has exact literal length

\[
W+o(W)
\tag{6.11}
\]

and covers the whole band (6.3).  Taking
\(g\to\infty\) with \(g=(\log m)^{o(1)}\) gives

\[
J=(\log m)^{1/2-o(1)}.
\tag{6.12}
\]

The even-dimensional analogue uses ranks \(m-J,\ldots,m+J\) and strip-word
length \(2\ell+2J\).

---

## 7. A literal rank-chronology inequality

The constructions above solve a growing band, not the full Boolean lattice.
The following obstruction applies to every independent literal packet
system, whether or not it was obtained from MTF states.

Partition all nonempty targets into owned packets.  Packet \(\alpha\) has a
literal word of length \(n_\alpha\), and every assigned witness lies wholly
inside that packet word.  Let \(M_\alpha\) be its number of owned targets in
one fixed middle layer.  Thus

\[
\sum_\alpha M_\alpha=W.
\tag{7.1}
\]

Put

\[
\Gamma
=\sum_\alpha(n_\alpha-M_\alpha)
=\sum_\alpha n_\alpha-W.
\tag{7.2}
\]

For the reverse-block realization of theorem 1.1, if packet \(\alpha\) is
supplied by an MTF walk, then

\[
n_\alpha=b_\alpha+t_\alpha-1,
\]

and hence exactly

\[
\Gamma
=\sum_\alpha(t_\alpha-M_\alpha)
 +\sum_\alpha(b_\alpha-1).
\tag{7.3}
\]

Fix a set \(I\subseteq\{1,\ldots,k-1\}\) of \(B\) proper ranks and define

\[
D_I
=\sum_{r\in I}\left(W-\binom{k}{r}\right).
\tag{7.4}
\]

### Theorem 7.1 — literal rank-chronology

Every full-lattice independent packet system satisfies

\[
\boxed{
\sum_\alpha\sum_{j=1}^{n_\alpha}(B-j)_+
\le B\Gamma+D_I.}
\tag{7.5}
\]

#### Proof

At the \(j\)-th position of one packet, there are only \(j\) suffix
intervals ending there.  Their ORs are nested, so they contain at most one
target of each rank and meet at most \(j\) ranks in \(I\).  That endpoint
therefore omits at least

\[
(B-j)_+
\tag{7.6}
\]

ranks of \(I\).

For fixed \(r\in I\), one endpoint represents at most one rank-\(r\) target.
Covering all \(\binom{k}{r}\) distinct targets requires at least that many
endpoints that meet rank \(r\).  There are \(W+\Gamma\) packet endpoints in
total, so at most

\[
\Gamma+W-\binom{k}{r}
\tag{7.7}
\]

endpoints omit rank \(r\).  Sum (7.7) over \(r\in I\), and double-count
endpoint-rank omissions. \(\square\)

Duplicate witnesses, arbitrary reset letters, foreign targets, and arbitrary
cross-parent packet contents do not affect the proof.  The exact escape is a
witness interval crossing a packet seam, which is no longer independent
packet concatenation.

---

## 8. Gaussian middle-packet mass obstruction

Define

\[
F_B(n)=\sum_{j=1}^{n}(B-j)_+.
\tag{8.1}
\]

Every packet needs at least one right endpoint per owned middle target, so

\[
n_\alpha\ge M_\alpha.
\tag{8.2}
\]

For \(M_\alpha\le B\),

\[
\begin{aligned}
F_B(n_\alpha)
&\ge F_B(M_\alpha)\\
&=BM_\alpha-\frac{M_\alpha(M_\alpha+1)}2\\
&\ge\frac{B-1}{2}M_\alpha.
\end{aligned}
\tag{8.3}
\]

For \(B\ge2\), theorem 7.1 therefore gives

\[
\boxed{
\sum_{\alpha:M_\alpha\le B}M_\alpha
\le
\frac{2(B\Gamma+D_I)}{B-1}.}
\tag{8.4}
\]

Now take \(k=2m\) and

\[
I=\{m-H,m-H+1,\ldots,m+H\},
\qquad B=2H+1.
\tag{8.5}
\]

For \(h\ge1\),

\[
\frac{\binom{2m}{m+h}}W
=\prod_{i=1}^{h}\frac{m-i+1}{m+i}.
\tag{8.6}
\]

Using \(1-\prod_i(1-a_i)\le\sum_i a_i\),

\[
1-\frac{\binom{2m}{m+h}}W
\le\frac{h^2}{m}.
\tag{8.7}
\]

Consequently

\[
\boxed{
D_I
\le
\frac{W H(H+1)(2H+1)}{3m}
=\frac{BW H(H+1)}{3m}.}
\tag{8.8}
\]

### Theorem 8.1 — middle-packet quantiles

Assume \(\Gamma=o(W)\).  For every fixed \(0<\eta<1\),

\[
\boxed{
\sum_{\alpha:
M_\alpha\le(\sqrt{3\eta}+o(1))\sqrt{k}}
M_\alpha
\le(\eta+o(1))W.}
\tag{8.9}
\]

#### Proof

Choose

\[
H=\left\lfloor\sqrt{\frac{3\eta m}{2}}\right\rfloor.
\tag{8.10}
\]

Then

\[
B=(\sqrt{3\eta}+o(1))\sqrt{k}.
\tag{8.11}
\]

Substitute (8.8) into (8.4).  The \(B\Gamma\) term is \(o(BW)\), while

\[
\frac{2D_I}{B-1}
\le
\left(\frac{2H^2}{3m}+o(1)\right)W
=(\eta+o(1))W.
\]

This proves (8.9). \(\square\)

For example, \(\eta=1/4\) gives

\[
\boxed{
\text{at least }(3/4-o(1))W
\text{ middle targets lie in packets with }
M_\alpha>
\left(\frac{\sqrt3}{2}+o(1)\right)\sqrt{k}.}
\tag{8.12}
\]

Letting \(\eta\uparrow1\) diagonally gives

\[
\boxed{
\max_\alpha M_\alpha
\ge(\sqrt3-o(1))\sqrt{k}.}
\tag{8.13}
\]

This differs from the earlier interval-counting maximum-word bound: it
controls the number of owned middle targets in a packet and, more strongly,
the mass distribution of those targets.  It makes no SCD-chain-packet
assumption.

### Corollary 8.2 — sub-Gaussian middle packets have negligible mass

For every sequence \(\varepsilon_k\downarrow0\), a full-lattice independent
packet cover with \(\Gamma=o(W)\) satisfies

\[
\boxed{
\sum_{\alpha:M_\alpha\le\varepsilon_k\sqrt{k}}M_\alpha=o(W).}
\tag{8.14}
\]

#### Proof

Choose a central-band size \(B\) such that

\[
\varepsilon_k\sqrt{k}\ll B\ll\sqrt{k}.
\tag{8.15}
\]

For every packet in (8.14),

\[
F_B(M_\alpha)=(1-o(1))BM_\alpha.
\tag{8.16}
\]

Equation (8.8) gives \(D_I=o(BW)\), and theorem 7.1 gives (8.14). \(\square\)

---

## 9. Exact additive-completion penalty

Suppose a partial construction already assigns

\[
(1-o(1))W
\tag{9.1}
\]

middle targets to independent packets satisfying

\[
\max M_\alpha=o(\sqrt{k}).
\tag{9.2}
\]

Any purported full-lattice independent-packet completion retaining this
ownership has

\[
\boxed{\Gamma\ge(1-o(1))W.}
\tag{9.3}
\]

#### Proof

Choose \(B\) with

\[
\max M_\alpha\ll B\ll\sqrt{k}.
\tag{9.4}
\]

The retained packets contribute at least

\[
(1-o(1))B\sum M_\alpha
=(1-o(1))BW
\tag{9.5}
\]

to the left side of (7.5).  By (8.8), \(D_I=o(BW)\).  Thus

\[
(1-o(1))BW
\le B\Gamma+o(BW),
\]

which proves (9.3). \(\square\)

For every fixed \(0<\theta\le1\), the same proof with retained middle mass
\((\theta-o(1))W\) gives

\[
\Gamma\ge(\theta-o(1))W.
\tag{9.3a}
\]

In the target-disjoint strip construction, retain the principal packets
separately and disregard the repair packet for this argument.  The repair
packet owns only \(u_0=o(W)\) middle targets, but its individual middle mass
need not be \(o(\sqrt{k})\).  For every principal packet,

\[
M_\alpha=2\ell=o(\sqrt{k})
\]

and the principal packets own \(W-u_0=(1-o(1))W\) middle targets.  The same
is true of the economical overlapping cover because one strip owns at most
\(2\ell=o(\sqrt{k})\) middle targets.  Therefore neither positive band
construction can be completed additively at coefficient one while those
small packets remain separate and retain their middle assignment.  Any such
independent-packet completion has total length at least

\[
W+\Gamma\ge(2-o(1))W.
\tag{9.6}
\]

This conclusion permits arbitrary rewording inside each retained packet and
arbitrary additional packet targets.  It is not confined to the canonical
strip states.  Merging principal packets is an explicit escape, even if one
informally retains their old target labels: after merging, their owned middle
mass belongs to a larger packet.  Reassignment to larger packets and
intervals crossing packet seams are the other escapes.

---

## 10. Exact scope and remaining gate

### Proved

1. The packet formula (1.6) remains exact for overlapping exposed families
   after an ownership map is chosen.
2. Target-disjoint cyclic-strip packets cover a growing central band with
   both aggregate surpluses \(o(W)\).
3. Every principal strip transition is a literal MTF update, and every root
   and repair letter is explicitly charged.
4. For any prescribed fixed finite-block product-SCD partition, almost all
   principal packets can be made parent-rainbow by one relabeling.
5. A deeper economical overlapping strip cover also has an exact
   \(o(W)\)-surplus MTF packetization.
6. The literal rank-chronology inequality (7.5) forces Gaussian-scale packet
   mass in every near-width full-lattice independent packet system.
7. Retaining all but \(o(W)\) middle mass in sub-Gaussian packets forces a
   full extra \((1-o(1))W\) letters in any additive completion.  More
   generally, retaining \((\theta-o(1))W\) such middle mass forces at least
   \((\theta-o(1))W\) excess.

### Not proved

1. Neither central-band construction covers the ranks between its
   polylogarithmic depth and the outer-tail threshold at \(o(W)\) cost.
2. No partition of the full Boolean lattice satisfying (0.3) is constructed.
3. The chronology theorem does not obstruct one or a few global
   Gaussian-or-larger packets.
4. It does not apply when witness intervals cross packet seams; that is the
   genuine global-braid route.
5. The parent-rainbow relabeling is relative to one prescribed fixed-block
   product-SCD partition, not all partitions simultaneously.

The surviving full-cube target is therefore precise:

> Repacketize or reassign a leading fraction of the middle layer into
> Gaussian-scale-or-larger literal MTF packets while keeping both state
> surplus and root surplus \(o(W)\); or construct a global word whose
> decisive witnesses cross the packet seams. Sub-Gaussian independent packet
> fusion is now ruled out in mass, not merely in maximum packet size.
