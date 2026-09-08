# Audit of the equality-resolved top-strip first-moment drift

Date: 2026-07-27

Scope: the conditional input (2.1) in
`MATH_THEOREM_AGGREGATE_FIRST_MOMENT_TOP_STRIP_QUARANTINE_20260727.md`.

## 0. Verdict

The asserted closed comparison

\[
 \mathcal L_t Z_{\tau,X}
 \le
 \left({\dot Y_{\tau,X}\over Y_{\tau,X}}
             +\epsilon_{\tau,X}(t)\right)Z_{\tau,X},
 \qquad \int_0^T|\epsilon_{\tau,X}(t)|\,dt=o(1),
 \tag{0.1}
\]

is **not proved by the stated inputs**, and the proposed last-row
argument is false for a general mixed type.  Equality resolution removes
the false multiplicity coming from coincident formal rows.  It does not
remove the positive first-order correction produced when one future
edge or one future compensation resource deletes two or more distinct
physical rows of the configuration at once.

The exact generator is triangular in excess:

\[
 (\mathcal L_t-\partial_t\log Y_{\tau,X})Z_{\tau,X}
 \ \le\
 \sum_{d\ge1}\sum_{\tau':\,\omega(\tau')=\omega(\tau)+d}
       \gamma_{\tau,\tau'}(t)Z_{\tau',X}.
 \tag{0.2}
\]

There is no established relative estimate turning the right side of
(0.2) into \(\epsilon_{\tau,X}Z_{\tau,X}\), especially at the outer
boundary.  This is exactly the one-column top flux which the static
mixed-diagram theorem explicitly leaves open.

Consequently the Doob argument (2.2)--(2.3) of the quarantine note does
not currently apply.  The top strip remains open.  This audit does not
prove that no aggregate affine quarantine can close it; it proves that
the advertised per-type nonnegative supermartingale is unavailable.

## 1. What exposing the last physical row actually proves

Fix an equality partition of the formal rows and let \(b=b(\tau)\) be
the number of its physical blocks.  Expose a prefix consisting of
\(b-1\) physical rows and the already displayed columns.  Conditional
on a live prefix \(C\), let \(A_C\) be the number of possible last
physical rows.  Then

\[
                         Z_{\tau,X}=\sum_C w_C A_C
\tag{1.1}
\]

with nonnegative stopped prefix weights.  For the compensated process,
the exact cluster generator is

\[
                         \mathcal L A_C=-\mathsf D_1(C)+\mathsf K_C,
 \qquad \mathsf K_C\le0.
\tag{1.2}
\]

Thus the last-row calculation gives an upper bound at **one physical-row
loss rate**.  It does not by itself give the logarithmic derivative of
the full base

\[
 Y_{\tau,X}\asymp
 d_t(X)^{\,b}(K\Delta_t)^{c(\tau)}
 \times(\hbox{survivor-density factors}).
\tag{1.3}
\]

Saying that death of a prefix has nonpositive contribution is
insufficient: the right side of (0.1) contains the negative reference
rates of the other \(b-1\) physical rows and of the displayed columns.
To compare with (1.3), their losses must be present with the correct
rate, not merely with the correct sign.

There is also a normalization fork which must be made explicit.

* If (1.3) uses the number \(a\) of formal copies, then an equality
  block of size \(k\) is assigned \(k\) reference row rates although it
  has only one physical row rate.  Equality resolution directly refutes
  that normalization.
* If it uses \(b\), then the static estimate stated with the deliberately
  loose factor \(d(X)^a\) is not the claimed initialization.  A
  quotient-row version with \(d(X)^b\) can plausibly be reproved by the
  row-exploration argument, but it is a different statement and still
  does not address common future deletion events.

The hidden row factor is therefore \(b\), not the number of formal
replicas.  Core compression only gives \(b\le2\omega\); it does not make
\(b=1\).

## 2. The exact common-event correction

For a displayed physical configuration \(\gamma\), let \(U(\gamma)\)
be the set of its currently unprotected resources.  The compensated
joint-hazard identity gives

\[
 \Lambda_t(U(\gamma))
 ={|U(\gamma)|\over r}
   -{J_t(U(\gamma))\over r\Delta_t},
 \qquad
 J_t(S)=\sum_{v\in S}d_t(v)
       -\left|\bigcup_{v\in S}\mathcal E_t(v)\right|.
\tag{2.1}
\]

The product reference uses the first term.  Hence the normalized
first-order defect of the complete type is the positive quantity

\[
 {1\over r\Delta_t Z_{\tau,X}}
       \sum_{\gamma\in\Omega_{\tau,X}}J_t(U(\gamma)).
\tag{2.2}
\]

Expanding \(J_t\) says exactly what (2.2) counts: adjoin one future edge
column meeting \(t\ge2\) displayed physical rows/resources.  That
column raises excess by \(t-1\).  Known resource coincidences can be
put into the equality/witness partition.  A future edge meeting two
otherwise separated rows cannot; it is a child type in the generator.

This recovers the already proved formal triangularity

\[
 \mathcal L\widehat Z_\omega
 \le \dot z_\omega^{\rm ref}
   +\sum_{d\ge1}(C(\omega+d)^4)^d\widehat Z_{\omega+d},
\tag{2.3}
\]

with the \(m^{-2d}\) factors carried by the child normalization.
Equation (2.3), from the static mixed-diagram file, is incompatible
with replacing the child sum by a closed multiplicative error without
an additional dynamic estimate.

The first-moment statement (4.2) in the buffered-generator audit does
not supply that estimate at the top.  It is explicitly qualified by
“while the corresponding first-moment hierarchy is valid.”  Applied to
an excess-\(\omega\) type, its first nontrivial multiplicity extension
has excess \(\omega+1\).  At \(\omega=L\), and recursively throughout a
moving top strip, that is precisely the missing outer level.

## 3. Literal physical mechanism: distinct rows, not equality collapse

The failure is not the all-equal-row diagonal.  The literal separated-
endpoint construction in
`MATH_THEOREM_STARRED_C4_COIN_ENDPOINT_AND_EDGE_ONLY_WEIGHTED_GATE_20260727.md`,
Theorem 4.1, gives distinct repaired rows coupled by a common future
edge.  In the simpler exact notation, if a current link has size \(A_C\)
and one effective event satisfies

\[
                         A_C(g)=A_C,
\tag{3.1}
\]

then

\[
 \mathsf D_2(C)=A_C\mathsf D_1(C).
\tag{3.2}
\]

For the distinct-row component of \([A_C]_2\), or equivalently the
corresponding equality-resolved two-row mixed type, the common event
deletes the pair once.  The product base assigns one marginal loss to
each row.  If \(\mathsf D_1(C)=\lambda_CA_C\), the actual normalized
pair decay can be \(-\lambda_C\), whereas the product pair reference
decays at \(-2\lambda_C\).  The normalized defect is
\(\lambda_C=\Theta(1)\), not an integrable \(o(1/T)\) error.

This is precisely the top-square calculation already recorded in
`MATH_AUDIT_REPAIRED_RING_BUFFERED_STOPPED_GENERATOR_ESCAPE_20260727.md`.
Calling the equality-resolved pair count a “first moment of a mixed
type” does not change the event: it remains a degree-two monomial in
physical rows, and one future column can kill both rows.

The legal-coin construction in Theorem 3.1 of the same file gives the
analogous shared-resource mechanism.  Complete witness-coincidence
resolution can move a known shared resource into the child type, but it
does not remove the future-edge mechanism of Theorem 4.1.

## 4. Why the proposed threshold does not prove (0.1)

Before quarantine, the proposed stopping rule gives only absolute
envelopes

\[
 {Z_{\tau',X}\over Y_{\tau',X}}
 \le \bar\alpha^{\omega(\tau')/2}
\tag{4.1}
\]

for monitored child types.  It gives no lower bound on
\(Z_{\tau,X}/Y_{\tau,X}\).  Therefore an additive child flux in (0.2)
cannot be divided by \(Z_{\tau,X}\) to obtain the relative error in
(0.1).  A parent may lie far below its threshold while a child lies
near its own threshold.

One could instead seek an affine/triangular barrier and estimate the
immigration from all higher types.  That would be a different argument.
It would still require a terminal envelope for children above \(L\),
because at \(\omega=L\) the first common-event column is unrecorded.
The present proof supplies neither ingredient.

## 5. Exact sufficient replacement

For the per-type supermartingale (0.1), the missing hypothesis can be
stated without ambiguity.  For every equality-resolved type and owner,
up to its stopping time, require

\[
 \boxed{
 {1\over r\Delta_t}
 \sum_{\gamma\in\Omega_{\tau,X}}J_t(U(\gamma))
 \le \epsilon_{\tau,X}(t)Z_{\tau,X},
 \qquad
 \int_0^T\epsilon_{\tau,X}(t)\,dt=o(1).}
\tag{Q1-MDLE}
\]

Together with the corresponding physical-block reference drift for the
prefix rows and columns, Q1-MDLE implies (0.1) directly from (2.1).
It is a relative, dynamic common-column estimate.  Static time-zero
mixed-diagram bounds and equality resolution do not imply it in an
endogenous residual.

An alternative sufficient replacement is an aggregate triangular
barrier for (0.2), with an explicit outer-level envelope.  Such a
barrier may be weaker than Q1-MDLE, but it has not yet been proved.

## 6. Consequences for the graded hierarchy

The following pieces remain valid:

1. arbitrary static mixed diagrams have the claimed excess scale;
2. equality partitions must be resolved at the physical-row level;
3. the graded moment choice keeps every requested \(q\)-moment below
   the ceiling for \(\omega<L/4\);
4. the type count and the numerical estimate
   \(\bar\alpha^{L/8}=\exp[-\Omega((\log m)^3)]\) are correct.

What fails is the bridge from those facts to the stopped per-type
supermartingale.  Hence the claim that the finite excess hierarchy has
no remaining outer boundary should be withdrawn.  The exact surviving
gate is Q1-MDLE or a genuinely aggregate affine top-strip barrier with a
proved terminal envelope.

