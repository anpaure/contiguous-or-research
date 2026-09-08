# Self-closure of the dangerous list and the sharpened seam saving

## 1. The missing observation

Fix `1<c<2` and list **all** directed internal coordinate-peak plateaux of
edge cost greater than `ca` in word order.  Let `P=[u_0,v]` and
`P'=[u,v']` be consecutive members.  Suppose their seam is nonabsorbed.

The inherited seam-local maximum lemma produces a full-word internal
threshold run

\[
                         R\subseteq[v,u],
 \qquad \lambda(R)\le g+1,                          \tag{1.1}
\]

where `g` is the strict gap size.

The effective cost of this seam is not merely at most `g+1`.  It is at most

\[
                         \boxed{\min(g+1,ca).}        \tag{1.2}
\]

This follows from closure of the complete dangerous list.

## 2. Extraction of a peak plateau

In the seam-local proof, `R` is a maximal component of `{d>=M}`, where `M`
is the maximum of the predecessor's rising cross-coordinate `d` on the seam.
It is contained in `[v,u]`.  Hence in fact `d=M` throughout `R`, and `R` is
a constant-coordinate internal peak plateau.

There is also a proof which uses only the threshold-run statement.  Take a
maximum coordinate value `H` on `R` and a maximal contiguous `H`-block `Q`.
Its two full-word neighbours have smaller coordinate value: inside `R` by
maximality of the `H`-block, and outside `R` because those points lie below
the threshold.  Thus `Q` is an internal peak plateau and

\[
                         \lambda(Q)\le\lambda(R).    \tag{2.1}
\]

If `Q` is nondirected along its fixed coordinate line, one cross-coordinate
has an interior strict extremum.  It yields a singleton internal peak, of
cost zero.

If `Q` is directed and `lambda(Q)>ca`, then `Q` is itself a `c`-dangerous
plateau.  It cannot equal `P`, because its fixed coordinate is the rising
cross-coordinate of `P`; it cannot equal `P'`, because that fixed-successor
case is precisely absorption.  A positive-length `Q subseteq[v,u]` lies
strictly between `P` and `P'` in word order, contradicting their
consecutiveness.  When `u=v`, the seam run is a singleton and already has
cost zero.  Shared endpoints therefore cause no exception.

This proves (1.2).

## 3. Sharpened fixed-threshold saving

Normalize consecutive dangerous lengths and gap by

\[
 p={\lambda(P)\over a},\qquad
 s={\lambda(P')\over a},\qquad
 z={g\over a}.
\]

The exact safe predecessor supply from the audited seam repair is

\[
                         b(p,s,z)=\min\{p,(4-s-z)_+\}. \tag{3.1}
\]

Every one of these starts was formerly assigned the successor at cost `sa`
and may instead use the run from (1.2), of normalized cost at most
`min(c,z)+o(1)`.  Therefore the physical nonabsorbed saving is

\[
 \boxed{
 \phi_c^\star(p,s,z)
 =\min\{p,(4-s-z)_+\}\,[s-\min(c,z)].}               \tag{3.2}
\]

Because `s>c`, the second factor is positive.  This strictly strengthens
the former scalar-gap saving

\[
 \phi(p,s,z)=\min\{p,(4-s-z)_+\}(s-z)_+,             \tag{3.3}
\]

and agrees with it only when `z<=c`.

The modified first-dangerous bound is obtained by replacing `phi` by
`phi_c^star` in the nonabsorbed integral.  Span, disjoint source intervals,
endpoint congestion, and boundary errors are unchanged.

## 4. Short-hull record cost

When `p+s+z<=4`, the whole predecessor edge-interior may use the seam run.
Gap starts still use the cheaper neighbouring peak.  Thus

\[
 C_{N,c}(p,s,z)
 =p\min(c,z)+z\min(p,s).                              \tag{4.1}
\]

Compared with the former sharp service cost from
`SHARP_NONABSORBED_SERVICE.md`, the additional saving is

\[
 p\,[\min(s,z)-c]_+.                                 \tag{4.2}
\]

In particular, the sole old neutral triple satisfies

\[
 C_{N,c}(4/3,4/3,4/3)
 ={4c\over3}+{16\over9}
 <{32\over9}                                         \tag{4.3}
\]

for every fixed `c<4/3`.

## 5. Elimination of the mass-9/8 neutral ledger

The coherent scalar equality candidate

\[
 \rho={9\over8}\delta_{(4/3,4/3,4/3)}
\]

had old service cost exactly four.  Under (4.1), at any fixed
`1<c<4/3` it instead has

\[
 {Q(c)\over a^3}
 \le {9\over8}
 \left({4c\over3}+{16\over9}\right)+o(1)
 =2+{3c\over2}+o(1)<4.                              \tag{5.1}
\]

Hence no physical middle order with `D=o(a^2)` can realize that ledger.  Its
apparent equality came from treating a `>ca` internal peak inside the gap as
invisible, contradicting completeness of the dangerous list.

## 6. Scope

This closes the unique equality case of the old two-sided short-hull
functional.  It does not yet control absorbed seams or arbitrary bad-hull
mass.  The next analytic task is to optimize the strengthened saving
`phi_c^star` jointly with absorbed positive-line geometry and the bad-hull
budget across one common threshold.

