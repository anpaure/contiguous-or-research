# Audit of the all-phase PBBS corner atlas

Date: 2026-07-25  
Method: pure mathematics only; no computation or search

Audited report:
`MATH_ATTACK_PBBS_ALL_PHASE_CORNER_ATLAS_20260725.md`.

## 0. Verdict

The substantive theorem passes. In particular:

1. the phase-lattice indices and forbidden strip are exact;
2. the interior common-boundary factorization contains one literal copy of
   \(Z\), not two;
3. both axis boundary cases are correct, including the endpoint location
   of \(Z\);
4. both proposed charged roots are actual roots in the quotient support,
   and equality of charges gives a genuine common edge;
5. the two-corner rectangle concatenation is exact, with all collar orders
   and phase indices correct.

No substantive correction to the attacked report is needed. There are two
minor formal qualifications:

* the finite-chain formula uses the same rectangle cancellation once one
  of the two nonoverlap corners is no longer minimal. The proof remains
  valid verbatim because minimality is used only to guarantee that the
  lower cross is overlap. Stating this generalized rectangle lemma would
  make the induction formally self-contained;
* if the theorem is intended literally for every duration, one should say
  \(s\ge2\), or declare the phase lattice vacuous for \(s<2\). All intended
  Gaussian-sector applications have \(s\ge2\).

Neither point changes a formula or conclusion.

## 1. One-copy and boundary audit

At an interior minimal corner \(c=(a,b)\), put

\[
 r=a+b,\qquad u=s-b-1.
\]

The two coordinate predecessors are overlap. Their exact inequalities give

\[
 |\mathcal L_{a-1}|+|\mathcal U_b|
 \le \Lambda-(r-1)<\Lambda,
\]

and

\[
 |\mathcal L_a|+|\mathcal U_{b-1}|
 \le \Lambda-(r-1)<\Lambda.
\]

Because

\[
 U=ER_0,
 \qquad
 V=R_s(0S_s)E,
\]

these inequalities put \(\mathcal U_b\) wholly inside the prefix copy of
\(E\), and \(\mathcal L_a\) wholly inside the suffix copy of the same
word \(E\). The predecessor identities are literally

\[
 \mathcal U_b=\mathcal U_{b-1}H_RZ,
 \qquad
 \mathcal L_a=ZH_L\mathcal L_{a-1}.
\]

Moreover

\[
 |\mathcal U_b|+|\mathcal L_a|-|E|
 =B_{a,b}-\Lambda=|Z|.
\]

Hence their intersection inside \(E\) has length exactly \(|Z|\). It is
simultaneously the suffix \(Z\) displayed in \(\mathcal U_b\) and the
prefix \(Z\) displayed in \(\mathcal L_a\). Removing only this duplicate
display yields

\[
 \boxed{
 E=\mathcal U_{b-1}H_RZH_L\mathcal L_{a-1}.}
\]

The total length is \(|E|=\Lambda\), and the net is

\[
 -(b-1)+(r-1)-r+(r-1)-(a-1)=0.
\]

Thus the one-copy assertion is literal and floor-free.

For \(a=0<b\), one has

\[
 |\mathcal U_b|=\Lambda+|Z|,
 \qquad
 \mathcal U_b=\mathcal U_{b-1}H_RZ.
\]

Since \(\mathcal U_b\) is a prefix of \(ER_0\), its first \(\Lambda\)
letters are exactly

\[
 E=\mathcal U_{b-1}H_R,
\]

and the following \(Z\) is a prefix of \(R_0\). The case \(b=0<a\) is
the exact suffix dual:

\[
 \mathcal L_a=ZH_L\mathcal L_{a-1},
 \qquad
 E=H_L\mathcal L_{a-1},
\]

with \(Z\) a suffix of \(R_s(0S_s)\). Since \(\Lambda>0\), \((0,0)\)
cannot be a minimal nonoverlap point, so these two axis cases and the
interior case are exhaustive.

## 2. Canonical charge audit

For \(a>0\), the adjacent tail identity and the predecessor factorization
give

\[
 R_a0S_a=\overline T_{a-1}0R_{a-1}
          =ZH_LR_{a-1}.
\]

Therefore the charged root is exactly

\[
 \boxed{D_a=P_a1ZH_LR_{a-1}.}
\]

This is an actual support root. Its asserted intrinsic marker is also
correct: \(P_a1\) first reaches the global maximum;
\(\overline T_{a-1}\) has nonpositive relative prefixes and net zero, so
it runs from that first maximum to its last maximum; after its following
zero, \(R_{a-1}\), based one level lower, cannot regain the maximum. Thus
the length of \(\overline T_{a-1}\) is recoverable from \(D_a\) without
choosing a staircase position.

For \(b>0\), with \(u+1=s-b\), one has

\[
 0S_{u+1}=H_RZ,
\]

and hence

\[
 \boxed{D_{u+1}=P_{u+1}1R_{u+1}H_RZ.}
\]

Here \(0S_{u+1}\) is the unique terminal forest in the canonical
first-maximum factorization. The index bounds are exact:

\[
 0\le a\le s-2,
 \qquad
 1\le u+1=s-b\le s
\]

whenever the corresponding charge is defined. Thus both roots belong to
\(D_0,\ldots,D_{s+1}\). Choosing the lexicographically first minimal
corner and an available side produces one support edge per return; on an
edge-disjoint family those chosen edges are automatically distinct.

The specialized roots

\[
 D_{t+1}=1^s0^KY0^s,
 \qquad
 D_u=1^s0^sY0^K
\]

are therefore correctly identified as the two boundary charges in the
audited corner construction.

## 3. Rectangle audit

Let \(c=(a,b)\) and \(c'=(a',b')\) be incomparable minimal corners with
\(a<a'\) and \(b>b'\). Put

\[
 u=s-b-1,
 \qquad
 u'=s-b'-1.
\]

The lower cross \(p=(a,b')\) is below both minimal corners and is therefore
overlap. Its bridge \(H_p\) obeys

\[
 A_{a,u'}=R_{u'}H_p,
 \qquad
 C_{a,u'}=H_pR_a.
\]

With

\[
 A^\times=A_{a,a'},
 \qquad
 C^\times=C_{u,u'},
\]

the two corner equations cancel to

\[
 A^\times=Z_{a',b'}H_p,
 \qquad
 C^\times=H_pZ_{a,b}.
\]

When \(a'+b\le s-2\), the upper cross \((a',b)\) is a valid nonoverlap
pair, and

\[
\begin{aligned}
 R_u
 &=A_{a,u}Z_{a,b}\\
 &=A_{a',u}A^\times Z_{a,b}\\
 &=A_{a',u}Z_{a',b'}H_pZ_{a,b}.
\end{aligned}
\]

Uniqueness of the nonoverlap corridor gives

\[
 \boxed{Z_{a',b}=Z_{a',b'}H_pZ_{a,b}.}
\]

The net is exactly

\[
 -(a'+b')+(a+b')-(a+b)=-(a'+b).
\]

The touching case \(a'+b=s-1\) has \(a'=u\), so the same cancellation
gives

\[
 R_u=Z_{a',b'}H_pZ_{a,b}.
\]

For \(a'+b\ge s\), the phase ranges are disjoint. All boundary cases in
the rectangle statement are therefore correct.

For completeness, the cancellation just used needs only:

1. two incomparable nonoverlap points;
2. an overlap lower cross; and
3. a valid upper cross.

It does not require both nonoverlap points to be minimal. In the chain
formula, the relevant lower cross \((a_i,b_{i+1})\) is overlap because it
lies strictly below the minimal corner \((a_i,b_i)\). Applying the
generalized cancellation inductively proves the reported alternating
concatenation. This supplies the one sentence implicit in Section 6.

## 4. Proved boundary

The atlas is a genuine same-return free-monoid theorem. It closes the
proposed same-return third-phase/noncommuting lane, but it gives no
coefficient saving across distinct returns. The remaining class-B/class-I
packing problem and the coefficient-one theorem remain open, exactly as
stated in the attacked report.

