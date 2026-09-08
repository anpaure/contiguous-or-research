# Independent audit: global PBBS slack and protected reset packing

Date: 2026-07-31.

## 0. Verdict

The arithmetic spine and the one-path protected-packing theorem are valid
with the scope corrections now present in
`MATH_THEOREM_K_GLOBAL_PBBS_SLACK_COMPONENT_PACKAGING_20260731.md`:

1. the terminal-plateau proof uses a polynomial lower bound on the Wallis
   correction before discarding the exponentially smaller deadline term;
2. the P1--P4 equivalence is stated for one fixed fragmentation and one
   spanning path; and
3. the rectangular reset theorem requires \(O_q\cap I_q=\varnothing\).

The two large counterexamples to the empirical Catalan-third law replay by
exact integer arithmetic.  The q1 conservation law, cut-kernel conditions,
fixed-fragmentation P1--P4 equivalence, rectangular Hall construction, and
halo-debt estimate also pass.

This is not an audit proof of the missing PBBS port-expansion or common-cap
existence hypotheses.  In particular, neither scalar slack nor the
factor-three component census implies protected routing.

Three minor wording/scope corrections were also applied:

* the direct-gap opening in Corollary 3.1 requires \(c<C\), or else one must
  open and audit a different cyclic ledger edge;
* the atomic LLL selection must be uniform as well as independent; and
* the random-injection inequality (4.3) is sufficient, not an UNSAT
  detector.  Its failure cannot certify the example in Section 9.1.

None changes the stated conditional route to \(\nu(k)=B(k)\).

## 1. Authentication and exact replay

Audited source hashes at the time of this report are

```text
MATH_THEOREM_K_GLOBAL_PBBS_SLACK_COMPONENT_PACKAGING_20260731.md
  7e8bbcc034a90258fb9fed7ce92c4b567cadbe1062ddc8a2dd83bfb89d4c9e90
MATH_THEOREM_K_PROTECTED_RAINBOW_RESET_FRAGMENT_PACKING_20260731.md
  10006594c19a00cf3c3ad5434da5063fd068653eb2cc0fe15167a0ff34a2ab47
scratch/audit_global_pbbs_slack_component_20260731.py
  b743c9f816ccb566946faac372a1536c802d4440b9d59784eb9fdc92621042fc
```

The authenticated exact output is

```text
scratch/global_pbbs_slack_component_20260731.bigint.audit.json
  11a56f0552a9a1552c8247a8285727554262721389972d6569d8f8d5dc5ceba7
```

The command

```text
python3 scratch/audit_global_pbbs_slack_component_20260731.py --bigint
```

returns `PASS`.  In particular, for \(m=225669\), the exact SHA-256
digests of \(C_m,s_m,-S_m(420),C_m-3s_m\) are respectively

```text
380ccd38e8cc61f3660f80cd61228d7d493cb5e3dbaa356d416ee7f13b090a71
776efe6a7219c2ffe6e2a69a6f7dcfd8a797206f4f398ba9f5409ac0e62dd29b
c9afc56726a8fff79b23bbb81ca88ec3a0151dcf67102f61fc2049296abc81ca
e4e3da597deb78be8677bb8b9b5450da3cf65de321b7f7120f347a2d0a9020c4
```

and for \(m=691583\) they are

```text
9eb44b3974e74b4e4443e1d02f8e35df734c7914ff927c045bdafd561232e3ac
3e643e1703e385659e333b0a19916fa9281bee393e20952edb9064d36ef57b12
8fd85b34620e8aa1d36261fd37bda178ccdc6aad544871ae0e1948c65cc03772
97b5ac54c15e54e92a6cb66317164f622f00841bc6829de65e5256f084957bde
```

The previously truncated 63-hex first \(C_m-3s_m\) digest has been fixed
in the replay script.

## 2. Deadline arithmetic

Write

\[
C_m=\operatorname{Cat}_m,
\quad W_m=(2m+1)C_m,
\quad Q_d=\binom{d+1}{2},
\quad S_m(d)=dW_m+Q_d-(4^m-1).
\]

Direct substitution verifies

\[
C_{m+1}=\frac{2(2m+1)}{m+2}C_m,
\qquad
W_{m+1}=4W_m-C_{m+1},
\]

and

\[
S_{m+1}(d)=4S_m(d)-dC_{m+1}-3(Q_d+1).
\]

If \(S_m(d)<0\), the right side is negative, so \(d_m\) is
nondecreasing.  The displayed formula for \(S_{m+1}(d+1)\), together with
\(d_m\le m\) and \(W_m\ge m(m+1)\), verifies
\(d_{m+1}-d_m\in\{0,1\}\).

If \(d_{m+1}=d_m=d\), feasibility at \(m+1\) gives exactly

\[
s_m\ge \frac d4C_{m+1}+\frac34(Q_d+1)
=\frac{d(2m+1)}{2(m+2)}C_m+\frac34(Q_d+1).
\]

Thus \(s_m>C_m/2\) for \(d\ge1\), and \(s_m>C_m\) for \(d\ge2\).
Consequently every Catalan-third failure is terminal on its depth plateau.
The alternative proof using \(C_{m+1}/C_m>2\) should be read for \(m\ge2\);
at \(m=1\) the ratio equals two, but its premise is false, so the
corollary itself is unaffected.

## 3. Wallis window, critical roots, and Weyl scope

For \(\rho_m=4^m/W_m\), one has

\[
\rho_{m+1}=\rho_m\frac{2m+4}{2m+3}.
\]

Putting \(u_m=4\rho_m^2/\pi-m-5/4\) gives

\[
u_{m+1}=\left(\frac{2m+4}{2m+3}\right)^2u_m
-\frac1{4(2m+3)^2}
\]

and backward iteration gives the positive series in Lemma 2.1.  It yields

\[
\frac1{16(m+2)^2}<u_m<\frac1{16m}.
\]

The upper inequality gives the stated Wallis window.  The lower inequality
is also logically useful: at the integer immediately above

\[
x_d=\frac{4d^2}{\pi}-\frac54,
\]

the resulting infeasibility margin is polynomial, whereas
\((Q_d+1)/W_m\) is exponential.  Hence the terminal plateau index really is
one of

\[
\lfloor x_d\rfloor-1,\qquad \lfloor x_d\rfloor.
\]

If \(\theta_d=\{x_d\}\), direct subtraction of squares gives

\[
\frac{s_{M_d}}{C_{M_d}}
=d\theta_d+O(d^{-1})
\]

in the second case, and \(d(1+\theta_d)+O(d^{-1})\) in the first.  The
sign and the ordering of these two cases are correct.

Weyl equidistribution applies because \(4/\pi\) is irrational.  It proves
only that the set of depths satisfying
\(s_{M_d}\le C_{M_d}/3\) has natural density zero.  It does not prove that
there are finitely many such depths.  Separately, all critical dimensions
already have density zero among dimensions because there are only
\(O(\sqrt M)\) of them up to \(M\).

The Machin rational bounds reproduce both exact certificates.  Their
integer signs prove

\[
d_m=421,\quad 0<s_m<C_m/3
\quad(m=225669),
\]

and

\[
d_m=737,\quad 0<s_m<C_m/3
\quad(m=691583).
\]

The first \(10^{12}\)-scaled slack ratios are respectively
`62419986187` and `202091367868`.

## 4. Factor-three constants and Catalan neutrality

If \(a_m\) normalized periods equal one and every other normalized period
is an odd integer at least three, then

\[
C_m\ge a_m+3(c_m-a_m).
\]

Therefore

\[
c_m-a_m\le\left\lfloor\frac{C_m-a_m}{3}\right\rfloor,
\qquad
c_m\le\left\lfloor\frac{C_m+2a_m}{3}\right\rfloor.
\]

To infer \(c_m-1\le s_m\) from the second inequality, the exact floor
condition is

\[
C_m+2a_m\le3s_m+5.
\]

The constant five is correct: for integral \(X=C_m+2a_m\),
\(\lfloor X/3\rfloor\le s_m+1\) is equivalent to \(X\le3s_m+5\).

For a closure-aware halo with unit charge on nonminimum components and
charge at most \(\eta\) on minimum components,

\[
M\le(c_m-a_m)+\eta a_m
\le\frac{C_m}{3}+\left(\eta-\frac13\right)a_m.
\]

When \(\eta=0\), strict \(M<C_m/3\) uses the independently proved PBBS
fact \(a_m\ge\tau(m)\ge1\).  Without that fact, the displayed algebra alone
would only give \(M\le C_m/3\).

The component-neutral Pascal count

\[
(N-c)+2c+(C-c)=N+C
\]

is correct.  A *retained direct gap* exists only when \(c<C\).  At \(c=C\)
one may still delete some cyclic ledger edge to obtain one fewer slot, but
its endpoint, protection, and colour legality require a separate audit.

## 5. Exact q1 and cut-kernel ledgers

After \(b\) cuts, \(p\) path components, and \(n\) non-Johnson seams, the
number of Johnson seams is \(A=b-p-n\).  If \(R\) is the deleted colour
bank and \(Q\) the multiset of new Johnson colours, then

\[
\mu(C)=1-\mathbf1_R(C)+m_Q(C).
\]

Summing multiplicities gives

\[
W-H+E=W-b+A=W-p-n,
\]

so exactly

\[
H-E=p+n,\qquad H=p+n+E.
\]

For one final path and one q1-capable boundary port, exact completion
therefore forces \(n=E=0\) and
\(Q=R\setminus\{\rho\}\).  The seam colours must recycle all but the one
boundary colour; a mere collection of distinct foreign colours does not
suffice.

For one cut \(e_i\), the kernel identity

\[
e_i\notin\bigcap_{I\in\mathcal W_i(Z)}E(I)
\]

is exactly equivalent to retaining an internal witness.  For a cut set
\(K_i^{\rm cut}\), the correct condition is the stronger

\[
\exists I\in\mathcal W_i(Z):
E(I)\cap K_i^{\rm cut}=\varnothing.
\]

The union of these internal witnesses and literal suffix--whole-fragment--
prefix crossing witnesses is the complete upper ledger for a fixed final
order.

## 6. P1--P4 scope

For one fixed cut set, fixed fragment orientations, and an exhaustive seam
catalogue, P1 is exactly one directed spanning path: maximum in/out degree
one, \(b-1\) arcs, and all subtour cuts.  P2 is exactly the q1 statement in
Section 5 above.  P3 is exact by the internal/crossing interval dichotomy,
and P4 is exact by the arbitrary-start staircase optimizer.  With an
integral common cap, these conditions produce the claimed word.

The restrictions are essential.  A union catalogue of alternative cuts or
orientations also needs exact-one and owner-partition constraints.  A
\(p>1\) path forest has no unique \(T_x\), crossing bank, or
\(\Psi_d(T_x)\) until an ordered boundary completion is specified.  The
patched theorem correctly avoids both overclaims.

## 7. Hall, reset, and halo proofs

After fixing a colour injection \(\gamma\), ordinary Hall on the guarded
exit--entry graph is necessary and sufficient.  A saturating matching gives
one source, one sink, and otherwise degree two; the acyclic skeleton
excludes cycle components.  Its distinct seam colours are precisely
\(\gamma(L)\), so the q1 conclusion follows literally.

The random-injection sum is a valid sufficient condition.  For fixed
\(X,Y\), the probability is exactly \(R(X,Y)/(b)_{|X|}\), and every Hall
failure is contained in one of the enumerated trapping events.  This is a
union bound, not a converse.

For the atomic criterion, choose independently and uniformly from each
\(\mathcal A_i\).  Every two-source conflict event has probability at most
\(m^{-2}\), and disjoint source-variable sets are independent.  Thus the
symmetric LLL gives

\[
e(\Gamma+1)\le m^2.
\]

Unary failures must be deleted before recomputing \(m\) and \(\Gamma\).
The Aharoni--Haxell coefficients in the comparison paragraph are also
correct: two shared resources give coefficient two, and three genuinely
shared resources give coefficient three.  For the full two-resource bank,
\(\nu\le b-1\), so the condition would demand
\(b-1>2(b-2)\), impossible for \(b\ge3\).

In the rectangular theorem, the two Hall matchings biject tails to colours
and colours to heads.  The explicit disjointness
\(O_q\cap I_q=\varnothing\) prevents a composed self-loop, while the common
strict potential excludes every directed cycle.  The run proof is also
complete: a short internal run is either internal to one fragment, bounded
across one seam, or contains a whole intervening fragment.  Assumption 3
excludes the first two cases and fragment length at least \(d+1\) excludes
the third.  Hence the flat staircase has loss zero.

For the charged version, an initial ideal \(B\) cannot be re-entered after
the selected path leaves it.  Since the path is spanning, its first exactly
\(M\) owners are all of \(B\).  The run assumptions give

\[
\rho_j=0\quad(j<d),\qquad \rho_d\le M,
\]

and therefore

\[
\mathfrak D_d(T)=\sum_{j=1}^d\rho_j\le M.
\]

This checks the halo boundary index: a length-\(d\) run starting at owner
\(M\) is a suffix-boundary run and costs exactly \(M\), not \(M+1\).

## 8. Residual editorial qualifications

The companion theorem now uses the minimal three-port marginal-Hall
obstruction

\[
\mathcal A_1=\{(u,\alpha)\},
\qquad
\mathcal A_2=\{(v,\alpha),(u,\beta)\}.
\]

Direct checking of the two colour injections makes every fixed-colour Hall
system fail.  Inequality (4.3), however, remains only sufficient, not an
UNSAT detector.  The load-bearing conclusion remains
the same: exact equality still requires literal protected reset-rainbow
port expansion, upper-witness survival/service, the boundary colour, and
the integral common cap.
