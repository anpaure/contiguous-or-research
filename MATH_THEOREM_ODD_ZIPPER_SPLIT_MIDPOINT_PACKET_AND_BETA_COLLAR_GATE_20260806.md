# The zipper splits the first-connector payment into two exact halves

**Date:** 2026-08-06  
**Method:** literal zipper coordinates and signed connector charge; no
computation and no scalar-connectivity substitution  
**Status:** unconditional charge and local-path theorem.  It removes the
raw protected `p_1` connector from the setup shuttle.  One bounded directed
terminal beta-collar remains explicit in Section 5.

## 1. The two zipper bits

For a ternary digit `a` put

\[
 B(a)=\beta(a),\qquad G(a)=\gamma(a),
\]

so

\[
 (B(a),G(a))\in\{(0,0),(2,0),(2,2)\}
\tag{1.1}
\]

for `a=0,1,2`.  In the literal zipper, `B_1` is the second coordinate of
the active first clock `c(B_1)=(1,B_1)`, while `G_1` is the first coordinate
of the following record `(G_1,B_2)`.  Complement has the exact code

\[
       (B^*(a),G^*(a))=(2-G(a),,2-B(a)).
\tag{1.2}
\]

Write `epsilon(a)=a-1`.

### Lemma 1.1 (equal half payments)

For every `a in {0,1,2}`,

\[
 G^*(a)-G(a)=B^*(a)-B(a)=-2\epsilon(a).
\tag{1.3}
\]

#### Proof

For `a=0,1,2`, the two differences in (1.3) are respectively `2,0,-2`.
\(\square\)

Thus setup may advance only `G_1` to its final target value while leaving
the active `p_1` row unchanged.  Teardown advances only `B_1`.  No raw
rewrite of the connector `C(a_1)` is needed while `p_1` is the shadow clock.

## 2. Exact compensation of the two collar halves

Let the fixed collar be `C(a)|C(b)` and put

\[
 c=\epsilon(a)+\epsilon(b),\qquad
 q=\epsilon(a_1)+c.
\tag{2.1}
\]

After deleting the first connector and collar, the residual extreme bank
has signed charge `-q`.  Replacing every residual extreme by the midpoint
block `M=11` changes its mass by minus twice its charge.  Hence the total
residual source-to-midpoint change is

\[
                         2q.
\tag{2.2}
\]

By Lemma 1.1, advancing `G_1` contributes `-2epsilon(a_1)`.  Therefore

\[
 2q-2\epsilon(a_1)=2c.
\tag{2.3}
\]

On the other hand the source-collar to double-head change is

\[
 \operatorname{mass}(02|02)-\operatorname{mass}(C(a)|C(b))
   =4-2(a+b)=-2c.
\tag{2.4}
\]

Equations (2.3)--(2.4) cancel exactly.  The same calculation applies on
teardown: every residual midpoint-to-target change is again `2q`, advancing
`B_1` contributes `-2epsilon(a_1)`, and `02|02` to the complemented collar
contributes `-2c`.

### Theorem 2.1 (zipper-split midpoint balance)

For every collar type and every residual multiplicity `0,1,2,3`, the two
collar conversions can be paid without an anonymous reservoir:

1. source collar to `02|02` is paired with residual source-to-`11` and
   `G_1 -> G_1^*`;
2. `02|02` to target collar is paired with residual `11`-to-target and
   `B_1 -> B_1^*`.

The first operation leaves the unordered `p_1` clock row untouched, so the
three-state ordered-collar record remains available throughout the bulk
pass.

## 3. Literal one-coordinate cross paths

The part of the payment involving `G_1` or `B_1` has a literal local model.
If a collar extreme is followed by the paying zipper coordinate, use

\[
 \begin{aligned}
 00|2 &: 002\to011\to020=02|0,\\
 22|0 &: 220\to211\to121\to112\to022=02|2.
 \end{aligned}
\tag{3.1}
\]

Every arrow is one adjacent unit transfer.  Reflections handle the opposite
physical order.  Reversing the appropriate line gives the terminal half:

\[
             02|2\leadsto22|0,
       \qquad02|0\leadsto00|2.
\tag{3.2}
\]

The unused coordinate `B_2` of the following zipper record may be appended
unchanged to every state in the setup paths.  Consequently the whole record
block `(G_1,B_2)` can be shuttled as one labelled two-coordinate block,
changed next to the fixed collar by (3.1), and returned to its address.

## 4. Source recovery at the split midpoint

Advancing `G_1` alone does not have to encode `a_1`.  The collar record gives
`a,b`, while the signed residual count gives `q`; hence

\[
                 \epsilon(a_1)=q-\epsilon(a)-\epsilon(b).
\tag{4.1}
\]

This includes the zero-residual case `q=0`.  Thus the collar record, the
oriented residual midpoint/tag bank, and the literal residual addresses
recover `a_1` even though the mixed zipper pair `(B_1,G_1^*)` is not by
itself injective.  No source information is lost before `B_1` is written.

## 5. Exact remaining directed collar

The setup half now touches only `(G_1,B_2)`, which lies after the active
`p_1` shadow clock and is an ordinary labelled work block.  It is covered by
an occurrence-labelled marked shuttle once that shuttle's finite short-
corridor cases are supplied.

The teardown half is different: `B_1` is a coordinate of the selected
`p_1` clock itself.  Scalar component routing does not prove that it can be
changed while a target collar block is returned to its fixed berth.  The
remaining statement is the following finite interface.

> **Terminal beta-collar lemma.**  Bring one `H=02` collar block to the
> protected `p_1` neighbourhood while the ordered-collar record and root
> phase are retained.  Realize the appropriate path in (3.2), with `B_1`
> in place of its one-coordinate endpoint, so that a later selected target
> clock remains available while the complemented collar block returns to
> its fixed berth.  Then apply the audited aperture-retirement collar.  All
> strict states must retain the collar record, root signature, or a marked
> corridor occurrence label.

This is a fixed three-coordinate transition plus a marked return, not a
growing reservoir theorem.  It is not established merely by the existing
component-mass ladder, because that ladder does not preserve an occurrence
label while changing the active clock.

## 6. Scope

The theorem proves that protected `p_1` does not obstruct the **setup** and
that all four residual multiplicities have exactly balanced literal
payments.  Together with the balanced midpoint packet theorem it removes
the arbitrary reservoir premise.  The odd collar is fully closed only after
the finite short-corridor visible-cart table and the Terminal beta-collar
lemma are proved.
