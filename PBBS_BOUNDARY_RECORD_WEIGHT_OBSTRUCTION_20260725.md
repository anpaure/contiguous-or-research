# Boundary-record depth alone gives no extra collision factor

Date: 2026-07-25

This note concerns only the coefficient-one PBBS gate.  It sharpens the
retraction in `PBBS_FIRST_HIT_BOUNDARY_SHARPENING_20260725.md` by showing
that the missing factor cannot be recovered from the common boundary word
alone.

Retain the critical capped-array law of
`PBBS_SHARED_BOUNDARY_COLLISION_20260725.md`.  Thus, after reversing the
dual array, its right boundary is read as a prefix of

\[
 (0D_1)(0D_2)\cdots,
\]

where the first Dyck block \(D_1\) has height cap \(a=\ell+1\) whenever
\(3\ell<s-2\).

## Proposition

For every \(\ell\ge2\), there is a balanced boundary word \(e_\ell\) of
length \(2\ell\), beginning and ending with zero, such that

\[
 \max_j\operatorname{net}
 \bigl(\operatorname{rev}(e_\ell)[1,j]\bigr)=\ell-1,
 \tag{1}
\]

but its dual-boundary probability is

\[
 \boxed{
 \Pr(\text{dual boundary}=e_\ell)
 =2^{1-2\ell}\frac{\ell+1}{\ell+2}
 =\Theta(4^{-\ell}).}
 \tag{2}
\]

Consequently no pointwise estimate of the form

\[
 \Pr(\text{dual boundary}=e)
 \le C\frac{4^{-\ell}}{1+M(\operatorname{rev}e)}
 \tag{3}
\]

can hold for the capped-array boundary marginal.

### Proof

Put

\[
 w_\ell=0\,1^\ell0^{\ell-1},
 \qquad e_\ell=\operatorname{rev}(w_\ell)
              =0^{\ell-1}1^\ell0.
 \tag{4}
\]

Both words have length \(2\ell\) and net zero, and \(e_\ell\) begins and
ends with zero.  The prefix heights of \(w_\ell\) start at \(-1\), then
rise to \(\ell-1\), and finally return to zero.  This proves (1).

The initial delimiter zero of the reversed dual array is deterministic.
Thus the event that its first \(2\ell\) bits equal \(w_\ell\) is exactly
the event that the capped Dyck block \(D_1\) begins with

\[
 P_\ell=1^\ell0^{\ell-1}.
\]

This prefix has length \(2\ell-1\), ends at height one, and never exceeds
height \(\ell<a+1=\ell+2\).  Under fair-walk weights, after this fixed
prefix the probability of hitting zero before the forbidden height
\(a+1=\ell+2\), starting from height one, is the gambler's-ruin value

\[
 \frac{a}{a+1}=\frac{\ell+1}{\ell+2}.
\]

After that first return, the arbitrary capped Dyck suffix has total
weight \(C_a(1/4)\), which cancels the normalization of the Boltzmann law.
Hence

\[
 \Pr(D_1\text{ begins with }P_\ell)
 =2^{-(2\ell-1)}\frac{\ell+1}{\ell+2},
\]

which is (2).  Since the record depth in (1) tends to infinity, (3) is
impossible. \(\square\)

## Consequence for the coefficient-one attack

The weighted bridge estimate

\[
 \sum_{e:\operatorname{net}(e)=0}\frac1{M(e)+2}
 =O\!\left(\frac{4^\ell}{\ell+1}\right)
\]

is a correct abstract reflection estimate.  The obstruction above shows
that its weight is not present in either boundary marginal.  The only
possible source of such a gain is therefore the additional physical
coupling by the copied word \(0S_s0\).  Proposition 4.2 of
`MATH_ATTACK_QST_TWO_SEAM_TRANSFER_KERNEL_20260725.md` shows that this word
may cross a dual-block separator.  Thus the correct remaining state must
retain both unmatched carrier height and block index; a one-dimensional
record statistic of \(E\) cannot close the zero-winding sector.

