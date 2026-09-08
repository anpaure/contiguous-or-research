# Independent audit of Math Attack I

Date: 2026-07-25

## 1. Material reviewed

I read the complete local proof bodies associated with top-level thread I:

* `MATH_ATTACK_I_ENTROPY_REPORT_RAW_20260724.md`;
* `MATH_ATTACK_I_NONLOCAL_FACTOR_CIRCUITS_20260724.md`;
* `MATH_ATTACK_I_NONLOCAL_FACTOR_CIRCUITS_CROSS_AUDIT_20260724.md`;
* `MATH_ATTACK_I_ENTROPY_REPAIR_FUSION_20260725.md`;
* the thread's final theorem, which was not copied into a separate file.

The critical new assertion in the final theorem is the marked-gap collision
bound

\[
 M_1(F_m^{\rm MSW})\ge
 (2m-3)\operatorname{Cat}_{m-2}-\frac{2W}{m+2}.
 \tag{1.1}
\]

The earlier files did not contain this theorem.  In particular, the older
raw entropy report's statement that no asymptotic lower bound opposite to
\(M_1=o(W)\) was known is superseded if (1.1) is accepted.

## 2. The contextual insertion identity

The short argument in the thread final can be completed rigorously.  This
section gives the missing induction.

Let \(R\) be a Dyck word of length \(2s\), and number its gaps
\(g=0,\ldots,2s\).  Put

\[
 d_0=1100,\qquad d_1=1010,
 \qquad R^{(i)}=\operatorname{ins}_g(d_i,R).
\]

The four inserted physical positions are

\[
 I_g=\{g+1,g+2,g+3,g+4\}.
\]

Let \(e_g\) erase these four labels and shift every label larger than
\(g+4\) down by four.  The strong form of the required identity is:

> **Insertion--erasure lemma.**  In each permutation
> \(\rho(R^{(i)})\), the labels in \(I_g\) form one linear consecutive
> block.  Erasing that block and applying \(e_g\) to all remaining labels
> gives \(\rho(R)\).  In particular, the outside order and the location of
> the inserted block are common for \(i=0,1\).

### Proof

Induct on the semilength of \(R\).  Both inserted words are invariant under
reverse-complement:

\[
 \mu(1100)=1100,
 \qquad
 \mu(1010)=1010.
 \tag{2.1}
\]

The empty base follows from

\[
 \rho(1100)=(4,2,3,1),
 \qquad
 \rho(1010)=(2,1,4,3).
 \tag{2.2}
\]

For nonempty \(R\), write its first-return decomposition as

\[
 R=1u0v,
 \qquad a=|u|+2,
\]

and use

\[
 \rho(1u0v)=
 \bigl(a,\ a-\rho(\mu u),\ 1,\ a+\rho(v)\bigr).
 \tag{2.3}
\]

There are three cases.

1. If \(g=0\), then \(R^{(i)}=d_iR\).  The MSW concatenation law
   \(\rho(PQ)=(\rho(P),|P|+\rho(Q))\) puts the four new labels in the
   initial block and leaves the shifted outside order equal to
   \(\rho(R)\).
2. If \(g\ge a\), the insertion lies in \(v\), at local gap
   \(h=g-a\).  The initial three blocks of (2.3) are identical for the two
   insertions.  By induction the four new local labels form a consecutive
   block in \(\rho(\operatorname{ins}_h(d_i,v))\); the final affine shift
   by \(a\) preserves consecutiveness and the common outside order.
3. If \(1\le g<a\), the insertion lies in \(u\), at local gap
   \(h=g-1\).  Reverse-complement turns it into insertion of the same
   \(d_i\) in \(\mu u\) at reflected gap
   \(|u|-h\).  By induction its four labels form a consecutive block in
   \(\rho(\mu u')\).  The affine map
   \(z\mapsto a+4-z\) in the second block of (2.3) preserves their order
   as a block and maps their label set exactly to
   \(\{g+1,g+2,g+3,g+4\}\).  On all outside labels, erasure changes
   \(a+4-\rho(\mu u')\) back to \(a-\rho(\mu u)\).  The new closing label
   \(a+4\) erases to \(a\), and every suffix label
   \(a+4+z\) erases to \(a+z\).

The boundary gap \(g=a\) is case 2 with \(h=0\).  These cases exhaust all
gaps and prove the lemma. \(\square\)

Appending the distinguished omitted label \(\infty\) and cyclically
rotating to put the inserted block first gives

\[
 q(R^{(i)})=(\pi_i,t_0,t_1,\ldots,t_{2m-4}),
 \qquad |\pi_i|=4,
 \tag{2.4}
\]

with the same outside word for \(i=0,1\).  At the cut after \(\pi_i\), the
MSW first lower shadow is therefore

\[
 \{t_0,t_2,\ldots,t_{2m-4}\}
 \tag{2.5}
\]

for both roots.  The contextual collision identity is correct.

## 3. Distinctness and collision counting

There are exactly \(2m-3\) gaps in a word of length \(2m-4\), so the
number of certificate pairs is

\[
 K=(2m-3)\operatorname{Cat}_{m-2}.
 \tag{3.1}
\]

The pointed slots are genuinely distinct, even though the same Dyck root
can occur in several pairs.  From a root together with the pointed cut,
the four preceding omitted labels recover the set \(I_g\).  This recovers
the gap \(g\); the root substring on that set says whether the endpoint is
the \(1100\) or \(1010\) member; deleting it recovers \(R\).  Hence no
pointed occurrence is reused by two certificates.

If a target has multiplicity \(t\), a collection of certificate pairs with
disjoint pointed slots uses at most \(\lfloor t/2\rfloor\) pairs there.
Consequently

\[
 K\le\sum_S\left\lfloor\frac{\mu_1(S)}2\right\rfloor
 \le\sum_S(\mu_1(S)-1)_+=D_1.
 \tag{3.2}
\]

Since the total first-shadow mass is \(W\), while

\[
 N_1=\binom{2m+1}{m-1}=\frac{m}{m+2}W,
\]

the exact identity

\[
 D_1=W-(N_1-M_1)=\frac{2W}{m+2}+M_1
 \tag{3.3}
\]

proves (1.1).  The asymptotic constant is also correct:

\[
 \frac{K}{W}
 =\frac{m(m+1)}{4(2m-1)(2m+1)}longrightarrow\frac1{16}.
 \tag{3.4}
\]

## 4. Stability under row replacement

A canonical root participates once for each occurrence of \(1100\) or
\(1010\) in it.  Two such occurrences cannot start at consecutive
positions.  There are \(2m-3\) possible starts, so the certificate degree
of one row is at most

\[
 \left\lceil\frac{2m-3}{2}\right\rceil=m-1.
\]

If an exact factor \(F'\) is at row distance
\(b=|F'\triangle F^{\rm MSW}|/2\), exactly \(b\) canonical rows were
removed.  At least \(K-(m-1)b\) disjoint-slot certificates remain, giving

\[
 M_1(F')\ge
 \left[K-(m-1)b-\frac{2W}{m+2}\right]_+.
 \tag{4.1}
\]

As \(W=(2m+1)\operatorname{Cat}_m\), a factor with \(M_1=o(W)\) must
satisfy

\[
 b\ge(1/8-o(1))\operatorname{Cat}_m.
 \tag{4.2}
\]

Both the maximum-degree factor and the constant \(1/8\) are correct.

## 5. Verdicts on the final theorem

1. **Marked-gap collision theorem: verified, unconditional.**  The written
   final answer only sketched the hard contextual induction; Section 2
   above supplies the missing proof.  No finite-data assumption is used.
2. **Row-distance stability theorem: verified, unconditional.**  It is a
   stability statement relative to the canonical MSW row set, not a
   lower bound for distant exact factors.
3. **Signed-face entropy lower bound: verified with scope.**  The witnesses
   \(y_S=1\) on the first-shadow holes give
   \(D_{\rm frac},D_{\rm det}\ge M_1\) and
   \(\Psi\ge(1+\log2)M_1\).  Here \(D_{\rm det}\) is the canonical
   signed-face-plus-literal repair value.  This is not a lower bound for an
   arbitrary stateful contiguous-OR completion.
4. **Trace dispersion and common-kernel bound: verified.**  A complementary
   trace cell contains at most
   \((2+o(1))2^{-d}W\) rank-\((m-1)\) targets for \(d=o(n)\), giving at
   least \((1/32-o(1))2^d\) occupied cells.  Five fixed common coordinates
   allow only \((1/32+o(1))W\) targets, contradicting the marked-gap lower
   bound, so the common kernel has size at most four eventually.
5. **Projective two-coordinate suspension theorem: verified.**  A
   projective child with shorter new-label distance \(d\) owns
   \(m+2-d\) tag-zero and \(2d\) tag-one targets assigned to its unique
   parent row.  The two exact sector ledgers imply at most three projective
   children per parent and hence at least
   \(\operatorname{Cat}_{m+1}-3\operatorname{Cat}_m\) nonprojective rows.
6. **Positive conclusion: still conditional.**  No low-cost signed-face
   repair factor, trace-condensation lemma, MWB theorem, or coefficient-one
   OR word is constructed.

## 6. Verdicts on the associated report files

### Raw entropy report

The Fenchel dual, rank-profile lower bounds, complement-even Walsh
description, fixed-window owner constraints, and deletion-diamond Hall
reduction are correct.  Its old statement that the sign of the canonical
MSW first-shadow density was unknown is superseded by the marked-gap
theorem.  The dynamic diamond-orientation lemma remains unproved.

### Nonlocal exact-factor circuits

The group-component product, group-Haar identity, floor-subtracted energy,
static rectangle reduction, and endpoint quadratic circuit law are
correct.  The companion cross-audit's qualifications must be retained:

* the rectangle lemma requires \(n\ge5\);
* a larger group has fewer component blocks but not necessarily fewer
  distinct product factors;
* only centered conditional heat innovations have additive variance;
  raw state-dependent increments may have negative cross-time covariance;
* \((\mathrm{CHF}_A)\) is a strong sufficient condition, not an
  equivalence or a proved minimal gate;
* the final OR implication requires the fixed-window hypothesis for every
  fixed \(A\), followed by diagonalization and the SCD-product tail.

### Entropy repair fusion

The exact entropy dual, seam insertion before a full reverse MTF reset,
trace-corridor upper bound, chain incompressibility example, endpoint-loss
ledger, and fixed-pair Gaussian type-capacity no-go are correct under their
stated hypotheses.  The stationary fixed-frame no-go does not apply to a
mixed-frame or positive-density reflagging construction.

## 7. Overall classification

Thread I contains a real new unconditional obstruction:

\[
 M_1(F_m^{\rm MSW})\ge(1/16-o(1))W,
\]

plus the sharp local stability radius
\((1/8-o(1))\operatorname{Cat}_m\).  It does not prove the target
coefficient-one theorem.  Its best role in the retained portfolio is as a
canonical-factor and sparse-repair no-go lane, not as a positive
construction lane.
