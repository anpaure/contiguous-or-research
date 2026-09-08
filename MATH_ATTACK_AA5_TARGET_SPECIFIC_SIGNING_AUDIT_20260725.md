# Independent audit of fifth-wave AA target-specific signing

Date: 2026-07-25

Audited source:
`MATH_ATTACK_AA5_TARGET_SPECIFIC_SIGNING_20260725.md`.

Method: pure mathematics only.  No web search, finite search, experiment,
or solver is used.

## 0. Audit verdict

The report passes after correction of notation and scope.  Its main
positive theorem is exact:

\[
\boxed{
\vartheta(F_\varepsilon,\beta)
\le\tau_{\mathrm{pkt}}(F_\varepsilon,\beta)
\le\Omega_\beta(F_\varepsilon)
\le
\Omega_{\mathrm{sep}}
+\mathfrak A_{\mathrm{tar}}
\le
\Omega_{\mathrm{sep}}
+\sqrt{S_{\mathrm{tar}}\delta_{\mathrm{tar}}}.}
\tag{A.1}
\]

The rounded \(\varepsilon\) is one common signing of whole genuine
ownership components, so it produces one integral exact child factor at
all depths simultaneously.  There is no missing factor \(2\) or \(4\) in
(A.1).

For every fixed \(A>0\), the condition

\[
\Omega_{\mathrm{sep}}
+\sqrt{S_{\mathrm{tar}}\delta_{\mathrm{tar}}}
=o_A(\operatorname{Cat}_m/\sqrt m)
\tag{A.2}
\]

is sufficient for \(\mathrm{FSP}_A\).  Condition (A.2) is not proved.
The report therefore proves a route theorem, not FSP, MWB, or the final
contiguous-OR theorem.

The exact incompatibility theorem also passes:

\[
\sum_jd(F_{j-1},F_j)
\ge
\left(\frac1{256}-o(1)\right)\operatorname{Cat}_m
\tag{A.3}
\]

for every exact-factor path from the canonical MSW factor to an FSP
endpoint.  This is a canonical-basin obstruction, not a disproof of the
existential theorem.

## 1. Quota and packet normalization

At rank \(r=m-q\), a transposition has

\[
F_q=\binom{n-2}{r}+\binom{n-2}{r-2}
\]

fixed targets and

\[
P_q=\binom{n-2}{r-1}
\]

moved target pairs.  Thus \(N_q=F_q+2P_q\).  If \(\rho_q\) targets must
receive the upper quota, then:

* for \(\rho_q\le2P_q\), use \(\rho_q\bmod2\) fixed targets and
  \((\rho_q-(\rho_q\bmod2))/2\) moved pairs;
* for \(\rho_q>2P_q\), use all moved pairs and
  \(\rho_q-2P_q\le F_q\) fixed targets.

This verifies the existence of a \(\tau\)-invariant balanced quota vector.
The assumption \(q\le m-2\) guarantees fixed targets exist.
If a prescribed family of \(L\) moved pairs is reserved first, the same
proof applies whenever \(0\le\rho_q-2L\le F_q+2(P_q-L)\); this is the
extension used in the MSW application.

For one exact factor \(G\), put

\[
\Omega_\beta(G)=\sum_a(\mu_a(G)-\beta_a)_+.
\]

For every overfull resource choose exactly its excess number of owners and
take the union.  The union is quota-safe and has size at most the sum of
the excesses.  Hence

\[
\vartheta(G,\beta)\le\tau_{\mathrm{pkt}}(G,\beta)\le\Omega_\beta(G).
\tag{A.4}
\]

The constant is one.  The same deletion family is common to all depths,
and it is a subset of an already exact factor, so no completion theorem is
hidden.  Since FSP requires little-
\(o_A(\operatorname{Cat}_m/\sqrt m)\), a mere big-\(O_A\) estimate is
insufficient.

## 2. Pair-overload constants

For a moved target pair with invariant quota \(b\), fixed pair mass \(M\),
and signed difference \(D\), the two loads are

\[
\frac{M+D}{2},\qquad\frac{M-D}{2}.
\]

Their overload is

\[
\ell(D)
=
\left(\frac{M+D}{2}-b\right)_+
+
\left(\frac{M-D}{2}-b\right)_+.
\]

Direct case separation gives

\[
\boxed{
\ell(D)=
\max\left\{
0,
M-2b,
\frac{M+|D|}{2}-b
\right\}.}
\tag{A.5}
\]

Thus \(\ell\) is even, nondecreasing in \(|D|\), and
\(1/2\)-Lipschitz.  If

\[
r=\min_{\eta}|\sum_Kz_K\eta_K|,
\]

the local floor is obtained by replacing \(|D|\) with \(r\) in (A.5).
Both \(\sigma\) and \(-\sigma\) attain it.

If a common signing \(\varepsilon\) disagrees with the preferred antipode
\(t\sigma\) on component \(K\), then \(D\) changes by \(2z_K\).  The
Lipschitz loss is therefore exactly at most \(|z_K|\).  Summing proves

\[
\Omega_\beta(F_\varepsilon)
\le
\Omega_{\mathrm{sep}}
+\sum_{p,K}|z_{pK}|
\mathbf1_{\{\varepsilon_K\ne t_p\sigma_K^p\}}.
\tag{A.6}
\]

The fixed-target overload in \(\Omega_{\mathrm{sep}}\) is essential:
those counts do not change anywhere in the \(\tau\)-cube.

## 3. Synchronization rounding

Let \(a_{pK}=|z_{pK}|\) and \(S=\sum a_{pK}\).  With unit vectors, define

\[
\delta
=
\sum_{p,K}a_{pK}
\frac{1-\sigma_K^p\langle u_K,v_p\rangle}{2}.
\]

Hyperplane rounding gives component signs \(\varepsilon_K\) and target
phases \(t_p\).  The violation probability is

\[
\frac{\arccos(\sigma_K^p\langle u_K,v_p\rangle)}{\pi}.
\]

The scalar inequality

\[
\frac{\arccos x}{\pi}
\le\sqrt{\frac{1-x}{2}}
\]

and weighted Cauchy--Schwarz give angular cost at most \(\sqrt{S\delta}\).
There is no extra multiplier because (A.6) already has coefficient one.
Every rounded outcome is a common whole-component signing, not a
depthwise relaxation.

The angular value in fact equals the exact discrete frustration.  The
rounding argument gives \(\mathfrak f_{\mathrm{tar}}\le
\mathfrak A_{\mathrm{tar}}\).  Conversely, scalar vectors
\(u_K=\varepsilon_Ke\), \(v_p=t_pe\) associated with an optimal discrete
signing have angle zero on satisfied incidences and \(\pi\) on violated
ones.  Their angular cost is exactly \(\mathfrak f_{\mathrm{tar}}\), so

\[
\mathfrak f_{\mathrm{tar}}
=\mathfrak A_{\mathrm{tar}}
\le\sqrt{S\delta}.
\]

Zero discrete frustration is equivalent to satisfiability of
\(\varepsilon_K=t_p\sigma_K^p\) on every active incidence.  Equivalently,
for some joint choice among tied local minimizers, every signed bipartite
cycle has positive sign product; a forest is
sufficient.  The report does not claim that genuine cyclic-prefix geometry
forces this condition.

## 4. Linear target and sequence audit

For component profile difference \(\Delta_K=a_K-\tau a_K\), direct
substitution gives

\[
p(F_\varepsilon)
=\frac{p(F)+p(\tau F)}2
+\frac12\sum_K\varepsilon_K\Delta_K.
\]

Therefore

\[
\min_\varepsilon\langle y,p(F_\varepsilon)\rangle
=
\frac{L_y(F)+L_y(\tau F)}2
-\frac12\sum_K|\langle y,\Delta_K\rangle|.
\]

Illegal resourcewise signs replace the last absolute value by the sum of
the coordinatewise absolute values.  The loss is exactly

\[
\Lambda_y
=\frac12\sum_K
\left(
\sum_a|y_a\Delta_{K,a}|
-\left|\sum_ay_a\Delta_{K,a}\right|
\right).
\]

The triangle-equality condition in the report is correct: within every
component, all nonzero \(y_a\Delta_{K,a}\) must have one weak sign.

Each component side has equal cardinality and every wreath owns \(n\)
targets at a fixed depth, so its rankwise profile difference sums to zero.
Thus depth-dependent but target-uniform weights are factor-constant.  This
confirms that genuine target nonuniformity is necessary for a linear route.

The same-transposition cell identity also passes.  Every cube vertex
chooses one side of each intrinsic pair \(\{K,\tau K\}\); recomputing the
same \(\tau\)-overlay only reverses selected sides.  Hence an arbitrary
same-\(\tau\) sequence composes to one terminal common signing.

For varying targets, telescoping gives the exact debt

\[
\langle y_*,p_0-p_T\rangle
=
\sum_j\langle y_j,p_{j-1}-p_j\rangle
+
\sum_j\langle y_*-y_j,p_{j-1}-p_j\rangle.
\]

The exact cycle \(F\to\tau F\to F\) verifies that the debt can erase all
reported local gain.  The controlled recurrence theorem avoids this flaw
by bounding the actual nonlinear overload after every exact child.  Its
fixed quota vector must be invariant under every transposition used; the
report now states this hypothesis explicitly.

## 5. Packet metric and canonical obstruction

For the same quota vector \(\beta\), extend a packet cover from \(F\) to
\(G\) by retaining common-row weights and assigning weight one to every
new row.  A packet wholly on common rows is the same labelled packet in
both factors.  Hence

\[
|\vartheta_\beta(F)-\vartheta_\beta(G)|\le d(F,G).
\]

Taking the minimum over the common finite family of balanced quota vectors
preserves the Lipschitz constant.  Combining this with the audited genuine
canonical bound

\[
\vartheta_*(F_m^{\mathrm{MSW}})
\ge\operatorname{Cat}_{m-4}
\]

and path-length triangle inequality proves

\[
\sum_jd(F_{j-1},F_j)
\ge
\operatorname{Cat}_{m-4}-\vartheta_*(F_T).
\]

Finally,

\[
\frac{\operatorname{Cat}_{m-4}}{\operatorname{Cat}_m}
=\frac1{256}+O(m^{-1}),
\]

which verifies (A.3).  The variation is half row symmetric difference;
it is not an MTF connector cost.

The direct-overlay compression statement is correctly scoped.  It gives
an exact shortest-variation path when arbitrary exact-pair ownership
component moves are allowed.  It does not assert connectivity by
transposition-only moves.

## 6. MSW application and PTAD scope

The cited genuine MSW calculation is symbolically checkable.  The base
target word \(Q=10111101\), with complement \(27\), has exactly the three
owners \(11110000,11101000,11001100\).  Its transposed word
\(Q'=11011101\), with complement \(37\), has exactly the one owner
\(11011000\).  Suffix separation makes the lifted paired loads exactly
\((3,1)\).  The private component contains \(11001100V\), which owns
\(QV\) but not \(Q'V\), and \(10101100V\), which owns neither.  Switching
therefore changes the pair to \((2,2)\).  Distinct suffixes use distinct
components.  Reserving both upper quotas in every such pair uses
\(2\operatorname{Cat}_{m-4}<2W/(m+2)\) slots for \(m\ge4\); the extended
invariant-quota construction fills the remainder.  Thus the restricted
Catalan target family has zero local floor and zero synchronization
frustration after one common exact signing.  The row cost is exactly
\(2\operatorname{Cat}_{m-4}\).

This does not control any other resource and does not prove FSP.

The PTAD trace linearization is algebraically correct, but it starts only
after a literal legal MTF path system, bridge ordering, hole family, and
proper trace set exist.  An odd-dimensional exact-factor trajectory cannot
splice its different states or depths into that one word.  The report
correctly claims no PTAD implication.

## 7. Final scope ledger

### Proved

1. A target-pair discrepancy theorem yielding one exact child.
2. Exact synchronization constants and signed-cycle criterion.
3. A sufficient fixed-window theorem for FSP.
4. Same-cell collapse and moving-target debt.
5. Packet-value Lipschitz continuity and the positive-density canonical
   path obstruction.
6. A genuine common signing which repairs the known MSW Catalan target
   family.

### Not proved

1. The smallness condition (A.2) in any full genuine factor.
2. FSP, PTAD, MWB, or the coefficient-one theorem.
3. Any translation from exact-factor recourse to one MTF chronology.
4. Any claim that the repaired MSW child is globally packet-balanced.

The audit therefore confirms a new exact route and a sharp exact-factor
incompatibility theorem, while preserving every required quantifier and
scope limitation.
