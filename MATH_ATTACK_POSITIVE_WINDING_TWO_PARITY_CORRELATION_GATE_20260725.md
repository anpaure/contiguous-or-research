# Positive-winding PBBS returns: the two-parity correlation gate

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B_r=\operatorname{Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil.
\]

For a Dyck root \(D\), use

\[
 a(D)=\delta(D),\qquad c(D)=d(D),
 \qquad \widehat c(D)=d(\phi D),
\]

and write \(D_j=\tau^jD\), where \(\tau=\phi^2\).  A positive-winding
return interval of step-two length \(s\) has the two exact ledgers

\[
 \sum_{j<s}c(D_j)=a(D_s)+wN,
 \qquad
 \sum_{j<s}\widehat c(D_j)=a(D_0)+wN,
 \qquad w\ge1.                                      \tag{0.1}
\]

This note proves four statements.

1. Quotient-edge disjointness on the even parity automatically gives
   quotient-edge disjointness on the odd parity.

2. Multiplying the two ledgers gives an exact two-point correlation charge.
   If the relevant PBBS first-dominant correlations have total mass
   \(O_A(NB_r)\), then the positive-winding part of \((\mathrm{CP}_A)\)
   follows immediately.

3. No nonnegative additive combination of the two ledgers can improve the
   already known \(O(B_r/\sqrt r)\) estimate.  More strongly, there is an
   exact abstract orbit satisfying both ledgers, the potential telescope,
   the complete first-return chronology, and disjointness on both parities,
   with packing density \(\Theta(N^{-1/2})\).  Thus the missing square root
   cannot come from the scalar ledgers alone.

4. At an actual first-dominant PBBS boundary, the two initial parity
   deficits are lengths of two disjoint literal Dyck fringes.  This is the
   additional word geometry which any proof of the correlation estimate
   must exploit.

The note does not prove or disprove \((\mathrm{CP}_A)\).  It replaces an
invalid multiplication of two first-moment bounds by the exact nonlinear
statement which is still needed.

## 1. Both parity supports are disjoint

Let \(I=(D,s)\) denote the directed quotient-edge interval

\[
 D,\tau D,\ldots,\tau^{s-1}D.
\]

Its half-shifted interval is

\[
 \phi I=(\phi D,s)
 =\phi D,\tau\phi D,\ldots,\tau^{s-1}\phi D,
\]

because \(\phi\tau=\tau\phi\).

### Lemma 1.1 (parity transfer)

If a family \(\mathcal J\) of quotient intervals is pairwise
edge-disjoint, then the family \(\phi\mathcal J\) is also pairwise
edge-disjoint.

### Proof

The map \(\phi\) is a permutation of the Dyck quotient-edge set and
commutes with \(\tau\).  It therefore maps the edge support of \(I\)
bijectively onto the edge support of \(\phi I\).  Images of disjoint sets
are disjoint. \(\square\)

Thus one may spend the \(c\)-ledger on the even edge support and the
\(\widehat c\)-ledger on a genuinely disjoint odd edge support.  The next
section records the exact way in which the two budgets combine.

## 2. The exact product charge

Let \(\mathcal J\) be a pairwise quotient-edge-disjoint family of
nonwrapping positive-winding return intervals, each of length at most
\(H\).  For \(I=(D,s)\), put

\[
 C(I)=\sum_{j=0}^{s-1}c(\tau^jD),
 \qquad
 \widehat C(I)=\sum_{j=0}^{s-1}\widehat c(\tau^jD).
\]

Equation (0.1) gives

\[
 C(I)\ge N+1,\qquad \widehat C(I)\ge N+1.          \tag{2.1}
\]

### Theorem 2.1 (two-parity product packing inequality)

One has

\[
 \boxed{
 N^2|\mathcal J|
 \le
 \sum_{I=(D,s)\in\mathcal J}
 \sum_{0\le j,k<s}
 c(\tau^jD)\widehat c(\tau^kD).}                  \tag{2.2}
\]

Moreover, if \(\mathcal A_{H,\ell}(\mathcal J)\) is the set of roots
\(E\) for which the ordered pair

\[
 (E,\tau^\ell E)
\]

occurs at relative displacement \(\ell\) inside an interval of
\(\mathcal J\), then

\[
 \boxed{
 N^2|\mathcal J|
 \le
 \sum_{|\ell|<H}
 \sum_{E\in\mathcal A_{H,\ell}(\mathcal J)}
 c(E)\widehat c(\tau^\ell E).}                    \tag{2.3}
\]

For each fixed \(\ell\), every root occurs at most once in the inner sum.

### Proof

Multiply the two inequalities in (2.1) and sum over \(I\).  This gives
(2.2).  Expanding the product associates to \((j,k)\) the displacement
\(\ell=k-j\).  Since the intervals are nonwrapping, this identifies the
ordered pair with

\[
 E=\tau^jD,\qquad \tau^\ell E=\tau^kD.
\]

For fixed \(\ell\), two occurrences of the same \(E\) in two selected
intervals would place the quotient edge \(E\) in both intervals, contrary
to edge-disjointness.  Regrouping by \(\ell\) proves (2.3). \(\square\)

For the first-loss problem, let
\(\mathcal A^{\rm fd}_{H,\ell}\) be the set of roots which can occur in
the displayed relative position inside a positive-winding interval whose
start is first-dominant.  Theorem 2.1 gives the following exact sufficient
statement.

### Corollary 2.2 (first-dominant correlation gate)

If, for every fixed \(A\),

\[
 \boxed{
 \sum_{|\ell|<H}
 \sum_{E\in\mathcal A^{\rm fd}_{H,\ell}}
 c(E)\widehat c(\tau^\ell E)
 =O_A(NB_r),}                                      \tag{2.4}
\]

then every edge-disjoint family of positive-winding first-dominant
intervals has size

\[
 O_A(B_r/N).
\]

This is exactly the positive-winding quotient scale required by
\((\mathrm{CP}_A)\).

The admissibility restriction in (2.4) is essential.  Replacing it by all
Dyck roots at every displacement loses the chronology which the problem is
asking us to exploit.

## 3. Why the two scalar ledgers do not multiply

Since \(\phi\) is a permutation,

\[
 \sum_D\widehat c(D)=\sum_Dc(D)
 =\Theta(\sqrt r\,B_r).                            \tag{3.1}
\]

Let \(\alpha,\beta\ge0\).  Equations (0.1) give every positive-winding
interval the additive charge

\[
 \sum_{j<s}\bigl(\alpha c(D_j)+
                    \beta\widehat c(D_j)\bigr)
 \ge(\alpha+\beta)N.                              \tag{3.2}
\]

By Lemma 1.1 and edge-disjointness, the available global mass is at most

\[
 (\alpha+\beta)\Theta(\sqrt r\,B_r).              \tag{3.3}
\]

Thus every argument which merely adds the two ledgers stops at

\[
 O(B_r/\sqrt r).                                   \tag{3.4}
\]

The following exact abstract example shows that this is not just a defect
of the displayed calculation.

### Proposition 3.1 (exact two-ledger saturation model)

For every even integer \(s\ge4\), put

\[
 q=s+1,\qquad N=sq-1=s^2+s-1,
\]

and set

\[
 a_j=1,\qquad c_j=\widehat c_j=q,
 \qquad b_j=N-a_j-c_j=N-q-1.                      \tag{3.5}
\]

Then:

1. \(a_j,b_j,c_j,\widehat c_j\) are positive odd integers and satisfy
   the exact block ledgers
   \[
   c_j=N-a_j-b_j,\qquad
   \widehat c_j=N-b_j-a_{j+1};                    \tag{3.6}
   \]
2. the length-\(s\) interval has winding one in both parities,
   \[
   \sum_{j<s}c_j=N+a_s,
   \qquad
   \sum_{j<s}\widehat c_j=N+a_0;                 \tag{3.7}
   \]
3. the associated ordinary one-step displacement sequence
   \[
   a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1},a_s
   \]
   has no proper return modulo \(N\), and returns for the first time after
   all \(2s+1\) steps.

Consequently, on a formal quotient cycle of length \(L\) divisible by
\(s\), placing this data periodically gives \(L/s=\Theta(L/\sqrt N)\)
pairwise edge-disjoint positive-winding intervals.  Their half-shifted
odd supports are also pairwise edge-disjoint.

### Proof

Because \(s\) is even, \(q=s+1\) and \(N=s^2+s-1\) are odd.  Formula
(3.5) gives

\[
 b_j=(s-1)q-2>0,
\]

which is odd.  Equations (3.6) are immediate.  Also

\[
 sq=N+1,
\]

which proves (3.7).

After \(2j\) ordinary steps, the accumulated displacement is

\[
 j(a+b)=j(N-q)\equiv-jq\pmod N.                  \tag{3.8}
\]

Since \(\gcd(q,N)=\gcd(q,sq-1)=1\), this is nonzero for
\(1\le j\le s\).  After \(2j+1\) steps it is

\[
 j(N-q)+1\equiv1-jq\pmod N.                      \tag{3.9}
\]

For \(0\le j<s\), its absolute representative is strictly between zero
and \(N\), whereas at \(j=s\),

\[
 1-sq=-N.
\]

Thus the final return is the first one.  Taking every \(s\)-th start on a
formal cycle gives disjoint even intervals; applying the parity
permutation gives disjoint odd intervals. \(\square\)

Proposition 3.1 is not asserted to be a Dyck/PBBS orbit.  Its precise
logical meaning is that

\[
 \boxed{
 \text{two ledgers + their telescope + first-return chronology
 + two-parity disjointness}
 }
\]

do not imply the missing square-root contraction.  A successful proof has
to use a further literal property of the first-dominant block rotation.

## 4. The literal two-fringe structure at a first-dominant start

Call \(D\) first-dominant if its first primitive component \(V\) is the
unique component of maximum height.  Write

\[
 D=VC,
\]

so \(\operatorname{ht}(C)<\operatorname{ht}(V)=h\).  In the canonical
first-maximum factorization write

\[
 D=P\,1\,R\,0\,C.                                 \tag{4.1}
\]

The prefix \(P\) ends at height \(h-1\).  Let \(P^-\) be the shortest
prefix of \(P\) which reaches height \(h-1\), and write

\[
 P=P^-P^+.                                         \tag{4.2}
\]

### Lemma 4.1 (two disjoint terminal fringes)

The word \(\overline{P^+}\) is Dyck and

\[
 \boxed{
 c(D)=|C|+1,
 \qquad
 \widehat c(D)=|P^+|+1.}                          \tag{4.3}
\]

Thus the initial even and odd deficit charges are the lengths of two
disjoint literal Dyck fringes of \(D\).

### Proof

The first identity is the definition of the suffix deficit in (4.1).
Since the displayed up-step is the first step reaching height \(h\), the
path \(P\) never exceeds height \(h-1\).  After its first hit of that
height, every relative prefix of \(P^+\) is nonpositive and its total is
zero.  Complementing zeroes and ones therefore makes
\(\overline{P^+}\) a Dyck word.

The exact one-step formula is

\[
 \phi D=\overline R\,1\,\overline C\,0\,
         \overline{P^-}\,\overline{P^+}.          \tag{4.4}
\]

The displayed one is the first step reaching the maximum of \(\phi D\).
While reading \(\overline C\), the height stays positive because
\(\operatorname{ht}(C)<h\).  After the displayed zero, reading
\(\overline{P^-}\) lowers the path from height \(h-1\) to zero, and the
minimality of \(P^-\) says that zero is reached for the first time at its
end.  Hence the terminal Dyck suffix in the canonical factorization of
\(\phi D\) is exactly \(\overline{P^+}\).  This proves the second
identity in (4.3). \(\square\)

Lemma 4.1 is the first genuinely PBBS-specific information not present in
the saturation model of Proposition 3.1.  It shows what a proof of (2.4)
must control: correlations of two disjoint first-dominant fringes under
the subsequent block rotations, not merely the marginal suffix moments.

## 5. Exact remaining positive-winding theorem

The positive-winding first-loss branch of the primitive recursion is at
the \((\mathrm{CP}_A)\) scale if either of the following equivalent proof
targets is established:

* the direct packing estimate
  \[
  |\mathcal J^{\rm fd,+}_H|=O_A(B_r/N);
  \]
* the admissible two-parity correlation estimate (2.4).

The second is a sufficient nonlinear charge, not asserted to be
necessary.  The exact audit above proves that simply summing the two
winding ledgers cannot establish it.  The remaining gain must come from a
PBBS-specific restriction on which pairs of the two fringes in Lemma 4.1
can reappear within one Gaussian first-return interval, or from an
equivalent equality-particle two-visit estimate.

Accordingly, the honest status is:

\[
 \boxed{
 \text{positive winding has an exact two-parity correlation gate,
 but the required first-dominant anticorrelation is still unproved.}}
\]

