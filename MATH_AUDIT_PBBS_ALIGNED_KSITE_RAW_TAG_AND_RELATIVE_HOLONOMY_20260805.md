# Audit of aligned PBBS multi-site fusion: raw tag monodromy and relative fan holonomy

**Date:** 2026-08-05  
**Audited file:** `MATH_THEOREM_PBBS_ALIGNED_KSITE_FUSION_AND_FAN_HOLONOMY_GATE_20260805.md`  
**Method:** cut-path permutation and gauge-normalized complete-state calculus; no computation or search  
**Verdict:** the topology formula is correct.  The original pointwise holonomy equation is incompatible with fusion once physical occurrence tags are included.  The correct condition is deck invariance under the unavoidable strand permutation, equivalently identity of a gauge-normalized **relative** holonomy.  Pure changes of active frame cannot cancel coherent voltage.

## 0. Corrections

For `k` aligned positive sites on three old cycles:

1. the terminal topology has `gcd(3,k)` components, exactly as stated;
2. the raw complete-state holonomy has strand-tag projection

   \[
                            \tau^k,
   \qquad \tau=(0\ 1\ 2);                              \tag{0.1}
   \]

3. consequently raw pointwise identity implies `3|k` and can never coexist with fusion;
4. zero signed fan current needs only a deck-preserving occurrence permutation, not raw pointwise identity;
5. after choosing a literal pure-tag transport `hat tau`, the correct pointwise sufficient condition is

   \[
                            \overline H
                            :=\widehat\tau^{-k}H=I;      \tag{0.2}
   \]

6. changing an active frame from preserving to reversing orientation is a gauge change.  Its conjugation at a site is cancelled by the inverse conjugation in the intersite transport.  Thus the proposed independent signed-exponent product is invalid without a genuine nongauge history actuator.

In particular, a raw holonomy-`I` aligned double does not exist.  Nor does a raw holonomy-`I` aligned four-site fusion.  Under the corrected relative criterion, `k=2` remains the smallest possible fusion count, but it requires one literal normalized inverse fan actuator; a reflected relabelling alone does not supply it.

## 1. Topology replay

At site `j`, cut one edge on each old cycle `C_i`.  Let `P_(i,j)` be the old directed path from the head of the cut at site `j` to the tail of the cut at site `j+1`.  A positive reconnection sends the latter tail to the head on cycle `i+1`.  Therefore the successor map on cut paths is

\[
                         (i,j)\longmapsto(i+1,j+1)       \tag{1.1}
\]

on `\mathbb Z_3\times\mathbb Z_k`.

Its orbit length is `lcm(3,k)`, so its number of orbits is

\[
 {3k\over\operatorname {lcm}(3,k)}=\gcd(3,k).          \tag{1.2}
\]

Thus the original topology theorem is correct, including `k=2` and `k=4` fusion and `k=3` topology neutrality.

## 2. Raw occurrence tags cannot return in a fusion

Let `Omega_j` be the disjoint union of the three complete fan-state fibres entering site `j`.  The state includes the physical old-cycle occurrence tag

\[
                         p:\Omega_j\longrightarrow\mathbb Z_3. \tag{2.1}
\]

Let `S_j` be the positive site reconnection and `E_j` the subsequent transport along the old path segment to site `j+1`.  Put

\[
                         T_j=E_jS_j.                     \tag{2.2}
\]

The site changes the old-cycle tag by `+1`; transport inside the receiving old cycle does not change it.  Hence

\[
                         p(T_j\omega)=p(\omega)+1.       \tag{2.3}
\]

### Theorem 2.1 (raw tag monodromy)

For

\[
                         H=T_{k-1}\cdots T_1T_0,        \tag{2.4}
\]

one has

\[
                         p(H\omega)=p(\omega)+k.        \tag{2.5}
\]

Consequently

\[
                         H=I\quad\Longrightarrow\quad3\mid k. \tag{2.6}
\]

#### Proof

Iterate (2.3).  If `H` is the identity on a state containing `p`, its tag projection is the identity, so `k=0` in `Z_3`. `square`

### Corollary 2.2 (pointwise identity is the wrong fusion criterion)

No aligned positive family can simultaneously satisfy raw complete-state identity and fuse the three old cycles.  This is independent of coherent versus noncoherent internal fan typing.

Thus the original phrase “the smallest possible escape is `k=2` satisfying `H=I`” is inconsistent with its own occurrence-tag convention.  The same applies to `k=4`.

## 3. Exact zero-current condition

Let `\Xi_0\subset\Omega_0` be the planted bank of the three incoming
complete states.  Let

\[
                         \mathscr D(\Xi)                 \tag{3.1}
\]

denote the complete occurrence-labelled triangular deck, with literal target values, penetration addresses, and the declared occurrence transport retained.

Every site current is a difference of the outgoing and incoming deck potentials.  Because `E_j` is an occurrence bijection, consecutive potentials cancel after transport.  Hence the total transported current is

\[
                         \mathscr D(H\Xi_0)-\mathscr D(\Xi_0). \tag{3.2}
\]

Here equality is understood under the declared terminal-to-initial occurrence identification.

### Theorem 3.1 (deck-stabilizer criterion)

The aligned macro has zero complete fan current whenever

\[
                         \mathscr D(H\Xi_0)=\mathscr D(\Xi_0). \tag{3.3}
\]

Raw pointwise identity is sufficient but not necessary.  A nontrivial permutation of the three complete state occurrences is allowed when it preserves their literal deck as a multiset.

#### Proof

Equation (3.2) is the serial coboundary identity.  Condition (3.3) makes its right side zero. `square`

This is the exact correction to the old necessity statement.  A nonidentity action on a visible coordinate obstructs **universal pointwise** return when that coordinate is independently labelled, but it need not obstruct a specially symmetric planted deck or a declared occurrence permutation.

## 4. Relative holonomy

Assume the aligned typing declares a literal pure-tag transport

\[
                         \widehat\tau:\Omega_{i,0}\longrightarrow
                         \Omega_{i+1,0}                  \tag{4.1}
\]

which changes only the strand occurrence address and preserves the complete fan datum under its declared occurrence bijection.  Define

\[
                         \overline H=\widehat\tau^{-k}H. \tag{4.2}
\]

Its tag projection is the identity.

### Theorem 4.1 (relative-identity criterion)

If

\[
                         \overline H=I,                  \tag{4.3}
\]

then `H=hat tau^k` is the unavoidable topology-tag permutation, and the complete fan current is zero.

More generally, it is enough that `bar H` belong to the stabilizer of the planted deck.

#### Proof

By definition, (4.3) gives `H=hat tau^k`.  The pure-tag transport preserves literal fan data and merely permutes the three occurrence addresses, so it preserves the multiset (3.1).  Apply Theorem 3.1. `square`

The existence of `hat tau` with complete literal data is load-bearing.  A rank-only or q1-only identification does not define (4.2).

## 5. Frame changes are gauge, not voltage

First separate the internal clean-C6 voltage from the physical tag shift.
In the diagonal-to-shifted notation, the old deck is

\[
                         D_{id}=\sum_iM_{ii},
\]

whereas a positive site has

\[
                         D_r=\sum_iM_{r(i),i},
 \qquad                  r(i)=i-1.
\]

The permutation `r` moves the **left-history index while the central/right
index remains fixed**.  It is therefore not the pure whole-strand tag
permutation `widehat tau`.  It has order three and is exposed already by
the q3 flag deck

\[
 \sum_i[K-\{d,e_{r(i)}\}+a_i]
 \quad\hbox{versus}\quad
 \sum_i[K-\{d,e_i\}+a_i].
\]

Distinct `e_i` make this relative voltage visible.  Any normalization
which identifies `r` with the physical tag shift would incorrectly erase
the audited q3 obstruction.

Let `r` be the normalized complete relative fan action of one coherent site.  At site `s`, choose an active frame `phi_s`.  In a fixed ambient notation the local action is

\[
                         R_s=\phi_s r\phi_s^{-1}.        \tag{5.1}
\]

If the intersite path is only the corresponding literal change of frame, its transport is

\[
                         E_s=\phi_{s+1}\phi_s^{-1}.      \tag{5.2}
\]

Use cyclic indexing, so `phi_k=phi_0`.

### Theorem 5.1 (gauge telescoping)

The chronological relative product is

\[
 \begin{aligned}
 (E_{k-1}R_{k-1})\cdots(E_0R_0)
 &=\phi_0r^k\phi_0^{-1}.                              \tag{5.3}
 \end{aligned}
\]

It is independent of how many frames `phi_s` reverse the cyclic order.

#### Proof

Each factor is

\[
 E_sR_s
 =\phi_{s+1}\phi_s^{-1}\phi_sr\phi_s^{-1}
 =\phi_{s+1}r\phi_s^{-1}.
\]

Multiplication telescopes all intermediate frames and gives (5.3). `square`

### Corollary 5.2 (signed-frame correction)

Writing `phi_s r phi_s^-1=r^(epsilon_s)` locally and then multiplying the exponents `epsilon_s` while omitting (5.2) is not gauge invariant.  In particular, the formal word `(+,+,-,-)` does **not** prove a four-site zero-current macro.  A genuine nongauge history actuator must be exhibited in one of the `E_s` or in a nonconjugate site action.

There is also no parity rule requiring an even number of negative absolute frames.  On a cyclic list the number of orientation-changing **transitions** is automatically even; the number of negatively oriented frames can be odd.  This removes the proposed abstract reason for preferring four sites over two.

## 6. The coherent lock after normalization

Suppose the coherent normalized action `r` has exact order three and is nontrivial on a visible complete-history coordinate.  Pure-gauge retypings give, by (5.3),

\[
                         \overline H\sim r^k.            \tag{6.1}
\]

Thus relative pointwise return requires `3|k`, while topology fusion requires `3` not divide `k`.

### Corollary 6.1 (genuine coherent relative lock)

The coherent monodromy lock survives the audit, but it is a statement about the normalized internal voltage `r`, not raw occurrence tags and not absolute frame signs.  Reflected relabellings do not escape it.

A specially symmetric planted deck could still be stabilized by `r^k`; the no-go is pointwise/universal on independently visible histories.

## 7. The corrected `k=2` gate

At two positive sites, raw tag monodromy is `tau^2`, so raw `H=I` is impossible.  After factoring this tag permutation, topology is already fused and the exact local target becomes

\[
                         \boxed{\overline T_1\overline T_0=I}, \tag{7.1}
\]

or, more generally, membership of the product in the planted deck stabilizer.

If both sites are coherent copies joined only by frame transport, Theorem 5.1 gives

\[
                         \overline T_1\overline T_0\sim r^2\ne I. \tag{7.2}
\]

Calling the second active frame “reflected” does not change (7.2).  A successful aligned double needs a literal normalized inverse actuator

\[
                         r_1=r_0^{-1}                  \tag{7.3}
\]

after both are transported to one common gauge.  This inverse must act on the complete paired histories, not only q1/q2 or the active-role triangle.

### Corollary 7.1 (minimality after correction)

`k=2` remains the smallest topology-fusing site count under the corrected relative criterion.  It is not constructed by a reflected frame alone.  If a separate theorem rules out every literal nongauge inverse actuator at two sites, then `k=4` is the next topology-fusing count (`k=3` is topology-neutral).  No such two-site physical no-go is proved by frame arithmetic itself.

Under the raw identity criterion there is no “next” fusion count at all: Theorem 2.1 rules out every `k` coprime to three.

## 8. Audited scope

Validated:

1. the `gcd(3,k)` topology calculation;
2. serial complete-state coboundary telescoping;
3. the coherent order-three lock after relative normalization.

Corrected:

1. raw `H=I` cannot be the condition for a fused occurrence-tagged macro;
2. the exact condition is deck invariance, with `bar H=I` a strong sufficient form;
3. reflected active frames are gauge choices and do not independently change the chronological exponent;
4. no abstract even-reflection rule makes four sites minimal.

Still open:

1. a literal PBBS nongauge inverse actuator satisfying (7.3);
2. a two-site or four-site complete paired-history deck stabilizer;
3. simultaneous q2/source/residence/common-cap planting; and
4. any unconditional all-`k` upper bound.
