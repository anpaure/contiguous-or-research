# Global recursive SCD-to-promotion-ring factorization: exact target and hereditary obstructions

**Dated audit: 2026-07-26. Constant-one lane only.**

## 0. Verdict

The exact one-baseline theorem makes the proposed global target sufficient. At the critical height

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 M=m+H,\qquad
 N_H=\binom{2m}{m-H}=(1+o(1)){W\over m},
\tag{0.1}
\]

one repaired promotion ring per critical top gives

\[
 p=N_H=o(W/H),\qquad 2Hp=o(W).
\tag{0.2}
\]

If the active tagged chains in those rings have total repeat excess \(o(W)\), then their missing-shadow count is also \(o(W)\), and the one-baseline compilation gives length \(W+o(W)\).

There is no completed recursion producing this factorization. Two natural recursive architectures admit exact obstructions.

1. **Confluent hereditary residence fails.** If cyclic frames are inherited by restriction and the result is independent of the deletion path, all critical-top frames are restrictions of one ambient cyclic order. Such frames cover at most

   \[
   2m\,2^{-H}W=o(W)
   \]

   distinct middle owners. Thus a globally confluent order recursion misses \(W-o(W)\) owners.

   More generally, if all top frames come from \(L\) hereditary ambient-order profiles, then

   \[
   L\ge(1-o(1)){2^H\over2m}
   \tag{0.3}
   \]

   is necessary for an approximate SCD. In particular every bounded-state or \(\exp(o(H))\)-profile restriction hierarchy fails.

2. **A one-type critical-top suspension is not closed.** Under the standard two-coordinate lift from \(B_{2m}\) to \(B_{2m+2}\), only \(1/2+o(1)\) of the new critical tops project to an old critical top when \(H\) stays constant; when \(H\) rises by one, the proportion is \(1/4+o(1)\). Hence a recursion which carries only the critical top type must rebuild a positive proportion of all rings at every step. A genuine inheritance recursion must carry off-critical top sizes and deletion histories.

There is a second quantitative warning. Any randomized recursive law which couples roots only in independent blocks of size \(b\) leaves a linear middle hole floor unless

\[
 b\ge(1-o(1)){\binom{m+H}{H}\over m+H},
\tag{0.4}
\]

whose logarithm is

\[
 \left({1\over2}+o(1)\right)\sqrt m\,(\log m)^{3/2}.
\tag{0.5}
\]

Thus a successful recursion must be simultaneously

- nonconfluent, so that the same projected top can carry different history-dependent cyclic orders;
- multitype in top size;
- equipped with at least \(\exp(\Omega(H))\) order profiles; and
- globally coupled across a superpolynomial root family.

This is a recursion-specific obstruction, not a nonexistence theorem for an arbitrary globally designed promotion-ring factor. The surviving object is a nonconfluent, globally coupled recursive configuration LP, not a local PBBS patch or a standard product SCD.

## 1. Exact factorization target from the one-baseline theorem

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\tag{1.1}
\]

and choose

\[
 q_0=\lceil m^{1/4}\rceil.
\tag{1.2}
\]

Use the covering-side critical height, so

\[
 T:=MN_H=W+o(W),\qquad N_H=o(W/H).
\tag{1.3}
\]

For every top

\[
 U\in\binom{[2m]}M,
\tag{1.4}
\]

choose an oriented cyclic frame

\[
 \pi_U=(c_0,\ldots,c_{M-1}).
\tag{1.5}
\]

A phase \(i\), tagged to depth \(d_i\le H\), owns at rank \(m+r\), \(|r|\le d_i\),

\[
 C_{U,i}(r)
 =U\setminus
   \{c_{i+H+r},c_{i+H+r+1},\ldots,c_{i+2H-1}\}.
\tag{1.6}
\]

At most one phase in a top has tag \(H\). The active phases are required to form one cyclic interval; deleting the complementary interval and one cyclic edge leaves one promotion path.

The exact retained-SCD census is

\[
 \#\{(U,i):d_i=d\}=N_d-N_{d+1}
 \quad(q_0\le d<H),
\qquad
 \#\{(U,i):d_i=H\}=N_H.
\tag{1.7}
\]

It has

\[
 \sum_{d=q_0}^{H-1}(N_d-N_{d+1})+N_H=N_{q_0}
\tag{1.8}
\]

active chains.

### Proposition 1.1 (one repaired ring per top is sufficient)

Suppose the frames, active intervals, and tags satisfy (1.7), and let

\[
 E_r=\sum_{S\in\binom{[2m]}{m+r}}(\mu_r(S)-1)_+
\tag{1.9}
\]

be the repeat excess at signed rank \(m+r\). If

\[
 \sum_{r=-H}^HE_r=o(W),
\tag{1.10}
\]

then the constant-one conclusion follows.

#### Proof

There are \(N_{q_0}\) active chains in at most \(N_H\) promotion paths. Their literal compilation costs

\[
 N_{q_0}+2HN_H.
\tag{1.11}
\]

At every controlled depth \(q_0\le |r|\le H\), the occurrence count is \(N_{|r|}\), exactly the number of targets at that rank. Hence the hole count equals \(E_r\). For \(|r|<q_0\), the occurrence count is \(N_{q_0}\), so the hole count is

\[
 N_{|r|}-N_{q_0}+E_r.
\tag{1.12}
\]

Appending the holes gives length at most

\[
 W+2HN_H
 +2\sum_{q=1}^{q_0-1}(N_q-N_{q_0})
 +\sum_{r=-H}^HE_r.
\tag{1.13}
\]

The path term is \(o(W)\) by (0.2), the shallow term is \(O(Wq_0^3/m)=o(W)\), and (1.10) handles the last term. The audited exterior compiler costs \(o(W)\). \(\square\)

Thus the requested recursive theorem is exactly a construction of (1.5)--(1.10). It does not need a second baseline, an annulus overlay, or a local PBBS patch.

## 2. What cyclic-window residence demands from an SCD

Let

\[
 C_{-d}\subset C_{-d+1}\subset\cdots\subset C_d
\tag{2.1}
\]

be a symmetric chain of radius \(d\), clipped at \(H\) when necessary.

### Lemma 2.1 (exact residence word)

If this chain occupies phase \(i\) of the frame \(\pi_U\) with tag \(d\), then

\[
 C_r=C_{U,i}(r)\qquad(-d\le r\le d),
\tag{2.2}
\]

and its coordinate-insertion word is the consecutive frame segment

\[
 \boxed{
 c_{i+H-d},c_{i+H-d+1},\ldots,c_{i+H+d-1}.}
\tag{2.3}
\]

Its middle owner and endpoints are

\[
 C_0=U\setminus I_{\pi_U}(i+H,H),
\tag{2.4}
\]

\[
 C_{-d}=U\setminus I_{\pi_U}(i+H-d,H+d),
\qquad
 C_d=U\setminus I_{\pi_U}(i+H+d,H-d).
\tag{2.5}
\]

#### Proof

In (1.6), increasing \(r\) by one deletes the first coordinate of the omitted interval. Therefore

\[
 C_{U,i}(r+1)
 =C_{U,i}(r)\cup\{c_{i+H+r}\}.
\]

Letting \(r\) run from \(-d\) to \(d-1\) gives (2.3), and (2.4)--(2.5) are the corresponding specializations of (1.6). \(\square\)

### Corollary 2.2 (the top anchors are forced)

In every full SCD, the chains reaching rank \(m+H\) are in bijection with the \(N_H\) top masks \(U\). In a promotion-ring factorization, the chain containing \(U\) must be the unique tag-\(H\) phase of ring \(U\).

#### Proof

Every rank-\((m+H)\) target lies in one SCD chain, and a tag-\(H\) phase satisfies \(C_H=U\) by (2.5). Conversely no tag below \(H\) reaches that rank. \(\square\)

This gives the natural recursive starting point: anchor one ring at each top using the SCD chain containing that top, and assign every shorter retained chain to one of the other phase positions. The hard condition is that all insertion words assigned to a top must be translates of one cyclic frame, not merely compatible pairwise.

## 3. Confluent restriction recursion collapses to one ambient order

The most direct way to enforce (2.3) “from the start” is to carry a cyclic frame through the recursion and require deletion of a coordinate to restrict that frame.

### Definition 3.1

A family of top frames is **restriction-confluent** if whenever two recursive deletion histories reach the same coordinate subset, they induce the same oriented cyclic order on that subset. Equivalently, frames on overlapping top sets have identical restrictions to every common subset of size at least three.

### Theorem 3.2 (global-order collapse)

Let \(V\) be a finite set and \(4\le M<|V|\). Suppose every \(M\)-subset \(U\subset V\) has an oriented cyclic order \(\pi_U\), and the family is restriction-confluent. Then there is one oriented cyclic order \(\pi\) on \(V\) such that

\[
 \boxed{\pi_U=\pi|_U\quad\text{for every }U\in\binom VM.}
\tag{3.1}
\]

#### Proof

Every three-set lies in an \(M\)-set. Give a triple \(\{x,y,z\}\) the cyclic orientation induced by any containing \(M\)-set. This is well defined: two containing \(M\)-sets can be joined by exchanges of elements outside the triple, with consecutive sets intersecting in at least the triple; confluence preserves the orientation at every exchange.

Every four-set lies in an \(M\)-set, so the induced orientations on its four triples are those of one cyclic order. Fix \(z\in V\), and define a binary relation on \(V\setminus\{z\}\) by

\[
 x<y\quad\Longleftrightarrow\quad(z,x,y)
\text{ has positive cyclic orientation}.
\tag{3.2}
\]

For any three \(x,y,w\), the four-set \(\{z,x,y,w\}\) lies in an \(M\)-set; its cyclic order shows that (3.2) is total and transitive. Hence it is a linear order. Placing \(z\) before that linear order gives an oriented cyclic order \(\pi\) on \(V\). Its restriction has the prescribed orientation on every triple, hence equals \(\pi_U\) on every \(M\)-set. \(\square\)

Thus full deletion-path confluence is much stronger than needed locally: it collapses all root frames to one global order.

## 4. One ambient order has an exponential middle-owner deficit

We now count exactly how much middle coverage is possible after the collapse in Theorem 3.2.

Fix an oriented cyclic order \(\pi\) on \([2m]\). For every \(M\)-top \(U\), use the restricted frame \(\pi|_U\).

### Lemma 4.1 (gap characterization)

A middle mask \(X\in\binom{[2m]}m\) is a length-\(m\) cyclic window in \(\pi|_U\) for some top \(U\supset X\), \(|U|=M\), if and only if the cyclic binary word of \(X\) in \(\pi\) has a gap containing at least \(H\) consecutive elements of \(X^c\).

#### Proof

Write \(U=X\sqcup J\), where \(|J|=H\). The set \(X\) is a cyclic interval of \(\pi|_U\) if and only if its complement \(J\) is a cyclic interval there. This happens exactly when all elements of \(J\) lie in one gap between consecutive elements of \(X\) in the ambient order. Such a \(J\) exists exactly when that gap contains at least \(H\) elements of \(X^c\). \(\square\)

### Theorem 4.2 (ambient-profile coverage bound)

The total number of middle masks covered by all restricted top frames from one ambient order is at most

\[
 \boxed{
 2m\binom{2m-H}{m}
 \le 2m\,2^{-H}W.}
\tag{4.1}
\]

In particular it is \(o(W)\) at the critical height.

#### Proof

By Lemma 4.1, every covered \(X\) has an ambient cyclic interval of \(H\) consecutive coordinates contained in \(X^c\). There are \(2m\) possible starts for this interval. For a fixed interval, all \(m\) elements of \(X\) must be chosen from the remaining \(2m-H\) coordinates, giving \(\binom{2m-H}{m}\) possibilities.

Finally,

\[
 {\binom{2m-H}{m}\over\binom{2m}{m}}
 =\prod_{j=0}^{H-1}{m-j\over2m-j}
 \le2^{-H}.
\tag{4.2}
\]

The union bound proves (4.1). Since \(H\to\infty\), its ratio to \(W\) tends to zero. \(\square\)

Deleting phases, making one-hole repairs, or lowering tags cannot create a new middle owner, so the same obstruction applies to repaired tagged rings.

### Corollary 4.3 (order-profile entropy floor)

Suppose every top frame is the restriction of one of \(L\) ambient cyclic orders, with the profile allowed to depend arbitrarily on the top. If the resulting rings cover \(W-o(W)\) distinct middle masks, then

\[
 \boxed{
 L\ge(1-o(1)){2^H\over2m}.}
\tag{4.3}
\]

Consequently

\[
 \log L\ge(\log2-o(1))H
 =(\log2-o(1))\sqrt{m\log m}.
\tag{4.4}
\]

#### Proof

The set of masks which can be covered using profile \(j\) has size at most \(2m\,2^{-H}W\) by Theorem 4.2. The union of all \(L\) such sets must contain \(W-o(W)\) masks. Rearrangement gives (4.3). \(\square\)

This rules out every recursion whose entire history is compressed to \(\exp(o(H))\) hereditary order profiles. It does not rule out a deliberately nonconfluent recursion with exponentially many histories.

## 5. A single critical top type is not stable under suspension

There is a second obstruction before any shadow calculation.

Let

\[
 H_m=\lfloor\sqrt{m\log m}\rfloor,
\qquad M_m=m+H_m.
\tag{5.1}
\]

For all sufficiently large \(m\),

\[
 H_{m+1}-H_m\in\{0,1\}.
\tag{5.2}
\]

Lift from the old coordinate set \(V\), \(|V|=2m\), to

\[
 V'=V\sqcup\{a,b\}.
\]

### Proposition 5.1 (critical-top ancestry fractions)

If \(H_{m+1}=H_m\), the proportion of new critical tops \(U'\in\binom{V'}{M_m+1}\) whose projection \(U'\cap V\) is an old critical top is

\[
 {2\binom{2m}{M_m}\over\binom{2m+2}{M_m+1}}
 ={2(M_m+1)(2m+1-M_m)\over(2m+2)(2m+1)}
 ={1\over2}+o(1).
\tag{5.3}
\]

If \(H_{m+1}=H_m+1\), the corresponding proportion is

\[
 {\binom{2m}{M_m}\over\binom{2m+2}{M_m+2}}
 ={(M_m+2)(M_m+1)\over(2m+2)(2m+1)}
 ={1\over4}+o(1).
\tag{5.4}
\]

#### Proof

In the first case the new top size is \(M_m+1\). Its old-coordinate projection has size \(M_m\) exactly when it contains one of \(a,b\), giving the numerator in (5.3).

In the second case the new top size is \(M_m+2\). Its projection has size \(M_m\) exactly when it contains both new coordinates, giving the numerator in (5.4). The displayed binomial ratios and \(M_m/m\to1\) prove the asymptotics. \(\square\)

### Consequence 5.2

A recursion whose only persistent objects are critical-top rings can inherit at most \(1/2+o(1)\) of the next layer's rings at an ordinary step and at most \(1/4+o(1)\) at a height-increment step. It must rebuild the other rings, or carry parent frames at the off-critical top sizes

\[
 M_m-1,\quad M_m,\quad M_m+1
\]

and their further descendants. Hence cyclic residence is not closed under a one-type SCD suspension.

This is an architectural obstruction, not a hole lower bound: a multitype recursion may escape it.

## 6. Local product recursion needs superpolynomial root coupling

The one-order obstruction concerns too much confluence. The opposite extreme—independent local recursive choices—also fails.

For a middle target, the number of roots capable of selecting it is

\[
 R_H=\binom mH.
\tag{6.1}
\]

Under a uniform cyclic frame in a compatible top, its selection probability is

\[
 \varpi_H={M\over\binom MH}.
\tag{6.2}
\]

At the covering-side critical height,

\[
 R_H\varpi_H={MN_H\over W}=1+o(1).
\tag{6.3}
\]

### Theorem 6.1 (recursive block-product obstruction)

Partition the roots into blocks of size at most \(b\). Inside each block allow an arbitrary joint distribution of frames, but assume distinct blocks are independent and every root has the uniform cyclic-frame marginal. If

\[
 b\varpi_H\le\alpha<1,
\tag{6.4}
\]

then the expected number \(Z\) of missed middle targets satisfies

\[
 \boxed{
 \mathbb EZ
 \ge W\exp\left(-{1+o(1)\over1-\alpha}\right).}
\tag{6.5}
\]

Consequently a law supported on \(o(W)\)-hole selections must have

\[
 \boxed{
 b\ge(1-o(1)){1\over\varpi_H}
 =(1-o(1)){\binom{m+H}{H}\over m+H}.}
\tag{6.6}
\]

#### Proof

Fix a middle target \(X\). In block \(j\), let \(Y_j\) count the compatible roots whose frames select \(X\), and put \(\mu_j=\mathbb EY_j\). Markov's inequality gives

\[
 \Pr(Y_j=0)\ge1-\mu_j.
\]

Here \(0\le\mu_j\le b\varpi_H\le\alpha\), and

\[
 \sum_j\mu_j=R_H\varpi_H=1+o(1).
\]

Block independence and

\[
 \log(1-x)\ge-{x\over1-\alpha}\qquad(0\le x\le\alpha)
\]

give

\[
 \Pr(X\text{ is missed})
 \ge\exp\left(-{1+o(1)\over1-\alpha}\right).
\]

Sum over all \(W\) middle targets. If a law is supported on selections with \(o(W)\) holes, its expected hole count is \(o(W)\); (6.5) then forces \(b\varpi_H\ge1-o(1)\), proving (6.6). \(\square\)

Stirling's formula yields

\[
 \boxed{
 \log{1\over\varpi_H}
 =\left({1\over2}+o(1)\right)
   \sqrt m\,(\log m)^{3/2}.}
\tag{6.7}
\]

Thus bounded, polynomial, and \(\exp(o(\sqrt m(\log m)^{3/2}))\)-sized independent recursive blocks cannot solve even the middle-owner ledger. This theorem applies to an actual block-product recursive law. It does not apply to a deterministic globally coordinated selection merely because that selection was described recursively; symmetrizing one deterministic selection introduces a global common seed.

## 7. The surviving recursive architecture

The preceding theorems leave one precise possibility.

### Definition 7.1 (nonconfluent multitype ring recursion)

A candidate recursion must retain states of the form

\[
 (U,\pi,\tau,\mathfrak h),
\tag{7.1}
\]

where

- \(U\) is a top in a band of sizes around \(m+H\);
- \(\pi\) is a cyclic frame on \(U\);
- \(\tau\) is a monotone tag word with one top anchor;
- \(\mathfrak h\) is a deletion history or order-profile label.

Different histories reaching the same set \(U\) are allowed to carry different frames. Recursive merging is performed only through a global matching or circulation which simultaneously preserves

1. the exact tag census (1.7);
2. one anchor at every critical top;
3. the consecutive insertion-word identity (2.3);
4. middle-owner capacity one up to \(o(W)\);
5. both nested signed target ledgers up to total \(o(W)\); and
6. one active interval per critical top.

### Theorem 7.2 (necessary quantitative complexity)

Any recursive construction satisfying the promotion-ring target must escape all three audited failure classes:

1. it cannot be restriction-confluent;
2. it cannot use only one critical top type;
3. it cannot be an independent root-block product below the scale (6.6).

If its frames are unions of hereditary ambient-order profiles, it must use at least the number in (4.3).

#### Proof

Items 1--3 are Theorem 4.2, Proposition 5.1, and Theorem 6.1, respectively. The profile count is Corollary 4.3. \(\square\)

This necessary complexity explains why a standard SCD recursion, a single canonical order, or bounded local frame repairs do not reach the critical promotion-ring factor.

## 8. Final synthesis

### Theorem 8.1 (recursive promotion-ring decision)

The following statements are rigorous.

1. One repaired promotion ring per critical top, with the exact retained-SCD tag census and total repeat excess \(o(W)\), has \(p=N_H=o(W/H)\) and proves the one-baseline constant-one theorem.
2. Cyclic-window residence forces every assigned SCD insertion word to be a consecutive segment of its top frame.
3. A deletion-confluent recursive enforcement of that residence collapses to one ambient cyclic order and covers only \(o(W)\) middle owners.
4. Even a union of hereditary profiles requires at least \(2^H/(2m)\) profiles.
5. A single critical top type loses a positive fraction of top ancestry at each two-coordinate suspension.
6. An independent-block recursive law needs superpolynomial block size (6.6).

Therefore no natural local or confluent SCD recursion currently yields the promotion-ring factorization. The recursion is not ruled out in full generality, but any surviving version must be a globally coupled, nonconfluent, multitype recursion with an exponentially large history space. Constructing its integral matching/circulation is equivalent to the global promotion-ring selection gate; it is not a simplification to a local PBBS correction.

## 9. Dependency ledger

This audit uses:

- MATH_THEOREM_FLAG_COHERENT_SCD_ONE_BASELINE_REDUCTION_20260726.md for the one-baseline compilation;
- MATH_THEOREM_PROMOTION_RING_ONE_HOLE_OWNER_FACTOR_AND_NESTED_TAG_GATE_20260726.md for the exact promotion-ring formula, retained-SCD tag census, and one-hole owner normal form;
- MATH_THEOREM_PROMOTION_RING_BLOCK_FACTOR_HOLE_FLOOR_20260726.md for the root block-product hole mechanism;
- MATH_THEOREM_EP_MULTISCALE_ROTOR_AND_CONTEXT_HALL_OBSTRUCTION_20260726.md for the literal promotion transition and full-top ring;
- TOP_FIBRE_PROMOTION_PACKET_REDUCTION_20260725.md for the critical-height capacity and cyclic-window interpretation.

No computation, web input, or generic growing-rank matching theorem is used.
